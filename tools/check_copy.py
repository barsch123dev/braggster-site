#!/usr/bin/env python3
"""Copy and locale gate.

Six checks, mirroring the app's user-text lint and i18n parity test:

1. No em dashes (or en dashes used as punctuation) in any user-facing string.
2. Every locale defines exactly the same keys as the English base.
3. No unsubstituted {{token}} survives into the built HTML.
4. src/games.json holds the same strings rule, plus the shape the build relies on.
5. src/gamepages/<locale>.json has a non-empty lead and scoring for every game
   in every locale, no extra ids, leads short enough to serve as the meta
   description, and (in English) no wagering vocabulary.
6. src/gamenames.json names every game in every locale, non-empty, no dashes.

Check 4 exists because the catalogue is user-facing copy that does not live in
src/locales/: without it, the em dash rule would silently stop covering the
single largest body of text on the site.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCALES_DIR = ROOT / "src" / "locales"
GAMES_FILE = ROOT / "src" / "games.json"
GAMEPAGES_DIR = ROOT / "src" / "gamepages"
GAMENAMES_FILE = ROOT / "src" / "gamenames.json"
DIST = ROOT / "dist"

BASE = "en"
BANNED = {"—": "em dash", "–": "en dash"}

# Mirrors CATEGORIES in tools/build.py, which needs a games_cat_<name> key per
# category to render the filter.
GAME_CATEGORIES = {"card", "dice", "board", "puzzle", "sports", "free"}
GAME_FIELDS = {
    "id": str,
    "name": str,
    "category": str,
    "tags": list,
    "functionality": str,
    "playInApp": bool,
    "vsComputer": bool,
    "lowestWins": bool,
    "trademark": bool,
    "playTogether": bool,
}


def check_games(failures: list[str]) -> None:
    if not GAMES_FILE.exists():
        failures.append("src/games.json is missing")
        return

    games = json.loads(GAMES_FILE.read_text("utf-8"))["games"]

    seen: set[str] = set()
    for index, game in enumerate(games):
        where = game.get("id") or f"index {index}"

        for field, kind in GAME_FIELDS.items():
            if field not in game:
                failures.append(f"games.json: {where} is missing {field!r}")
            elif not isinstance(game[field], kind):
                failures.append(f"games.json: {where} field {field!r} is not a {kind.__name__}")

        if game.get("id") in seen:
            failures.append(f"games.json: duplicate id {game['id']!r}")
        seen.add(game.get("id"))

        if game.get("category") not in GAME_CATEGORIES:
            failures.append(f"games.json: {where} has unknown category {game.get('category')!r}")

        players = game.get("players")
        if not isinstance(players, dict) or not {"min", "max", "perSide"} <= set(players):
            failures.append(f"games.json: {where} has a malformed 'players' block")
        elif players["min"] > players["max"]:
            failures.append(f"games.json: {where} has min players above max")
        elif players["perSide"] > 1 and not (players["min"] == players["max"] == 2):
            # build.py renders these with one fixed "2 teams of 2" string.
            failures.append(f"games.json: {where} is a team game that is not 2 teams of 2")

        for char, name in BANNED.items():
            if char in json.dumps(game, ensure_ascii=False):
                failures.append(f"games.json: {where} contains a {name}")

    # The trademark disclaimer has to be renderable next to the names it covers,
    # so at least one game must carry the flag that puts it on the page.
    if not any(g.get("trademark") for g in games):
        failures.append("games.json: no game carries the trademark flag; check the extraction")

    # playTogether is independent of playInApp: Yahtzee has no in-app board, yet
    # each player fills their own column on their own phone. So the flag is only
    # checked for being present on at least one game.
    if not any(g.get("playTogether") for g in games):
        failures.append("games.json: no game carries the playTogether flag; check the extraction")


# Wagering vocabulary the per-game prose must never use (D54 in the app repo:
# braggster records results, never an amount staked). English only: several
# of these are ordinary words in other languages ("ante" is Spanish for
# "before", "pot" is Dutch for a jar), so the translations are reviewed by eye.
WAGER_WORDS = re.compile(
    r"\b(bet|bets|betting|stake|stakes|staked|wager\w*|pot|pots|ante|antes|payout\w*|gambl\w*|casino\w*|chips?)\b",
    re.IGNORECASE,
)

# The lead is also the page's meta description, which search results cut at
# about 160 characters.
LEAD_MAX = 160


def check_gamepages(failures: list[str], locale_codes: list[str]) -> None:
    """Every games.json id has a non-empty lead and scoring in every locale's
    src/gamepages/<locale>.json, and nothing else does."""
    ids = [g["id"] for g in json.loads(GAMES_FILE.read_text("utf-8"))["games"]]
    for code in locale_codes:
        path = GAMEPAGES_DIR / f"{code}.json"
        if not path.exists():
            failures.append(f"gamepages/{code}.json is missing")
            continue
        pages = json.loads(path.read_text("utf-8"))
        for gid in ids:
            entry = pages.get(gid)
            if not isinstance(entry, dict):
                failures.append(f"gamepages/{code}.json: no entry for {gid!r}")
                continue
            for field in ("lead", "scoring"):
                value = entry.get(field)
                if not isinstance(value, str) or not value.strip():
                    failures.append(f"gamepages/{code}.json: {gid} has an empty {field!r}")
                    continue
                for char, name in BANNED.items():
                    if char in value:
                        failures.append(f"gamepages/{code}.json: {gid}.{field} contains a {name}")
                if code == BASE and WAGER_WORDS.search(value):
                    word = WAGER_WORDS.search(value).group(0)
                    failures.append(f"gamepages/{code}.json: {gid}.{field} uses wagering word {word!r}")
            lead = entry.get("lead") or ""
            if len(lead) > LEAD_MAX:
                failures.append(
                    f"gamepages/{code}.json: {gid}.lead is {len(lead)} characters, over {LEAD_MAX} "
                    "(it is the meta description)"
                )
        for extra in sorted(set(pages) - set(ids)):
            failures.append(f"gamepages/{code}.json: unexpected id {extra!r}")


def check_gamenames(failures: list[str], locale_codes: list[str]) -> None:
    """src/gamenames.json (written by tools/sync_game_names.py) names every
    games.json id in every locale, with no empty name and no dash."""
    if not GAMENAMES_FILE.exists():
        failures.append("src/gamenames.json is missing; run tools/sync_game_names.py")
        return
    ids = [g["id"] for g in json.loads(GAMES_FILE.read_text("utf-8"))["games"]]
    names = json.loads(GAMENAMES_FILE.read_text("utf-8"))
    for code in locale_codes:
        table = names.get(code)
        if not isinstance(table, dict):
            failures.append(f"gamenames.json: no names for locale {code!r}")
            continue
        for gid in ids:
            name = table.get(gid)
            if not isinstance(name, str) or not name.strip():
                failures.append(f"gamenames.json: {code} has no name for {gid!r}")
                continue
            for char, label in BANNED.items():
                if char in name:
                    failures.append(f"gamenames.json: {code}.{gid} contains a {label}")
        for extra in sorted(set(table) - set(ids)):
            failures.append(f"gamenames.json: {code} has unexpected id {extra!r}")
    for extra in sorted(set(names) - set(locale_codes)):
        failures.append(f"gamenames.json: unexpected locale {extra!r}")


def main() -> int:
    failures: list[str] = []

    files = sorted(LOCALES_DIR.glob("*.json"))
    if not files:
        print("no locale files found", file=sys.stderr)
        return 1

    locales = {f.stem: json.loads(f.read_text("utf-8")) for f in files}

    # 1. Banned punctuation in user-facing strings.
    for code, data in sorted(locales.items()):
        for key, value in data.items():
            if not isinstance(value, str):
                continue
            for char, name in BANNED.items():
                if char in value:
                    failures.append(f"{code}.json: {key} contains a {name}: {value!r}")

    # 2. Key parity against the English base.
    if BASE not in locales:
        failures.append(f"missing base locale {BASE}.json")
    else:
        base_keys = set(locales[BASE])
        for code, data in sorted(locales.items()):
            if code == BASE:
                continue
            missing = base_keys - set(data)
            extra = set(data) - base_keys
            for key in sorted(missing):
                failures.append(f"{code}.json: missing key {key!r}")
            for key in sorted(extra):
                failures.append(f"{code}.json: unexpected key {key!r}")

    # 4. The catalogue, 5. the per-game prose and 6. the local game names, for
    # every locale.
    check_games(failures)
    check_gamepages(failures, sorted(locales))
    check_gamenames(failures, sorted(locales))

    # 3. No unrendered tokens in the build output. Two kinds: the {{key}} the
    # templates use, and the {n} / {play} / {low} the catalogue's counts are
    # written as. The second only reaches HTML through a locale string, so a
    # leftover one means a locale spelled a count the build does not substitute.
    if DIST.exists():
        for page in sorted(DIST.rglob("*.html")):
            text = page.read_text("utf-8")
            for token in re.findall(r"\{\{\w+\}\}", text):
                failures.append(f"{page.relative_to(DIST)}: unrendered token {token}")
            for token in re.findall(r"\{(?:n|play|ai|together|puzzles|low|min|max|name)\}", text):
                failures.append(f"{page.relative_to(DIST)}: unsubstituted count {token}")

    if failures:
        print(f"copy check failed ({len(failures)} problems):", file=sys.stderr)
        for line in failures:
            print(f"  {line}", file=sys.stderr)
        return 1

    games = json.loads(GAMES_FILE.read_text("utf-8"))["games"]
    print(
        f"copy check passed: {len(locales)} locales, {len(locales[BASE])} keys each, "
        f"{len(games)} games"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
