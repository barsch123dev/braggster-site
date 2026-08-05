#!/usr/bin/env python3
"""Copy and locale gate.

Four checks, mirroring the app's user-text lint and i18n parity test:

1. No em dashes (or en dashes used as punctuation) in any user-facing string.
2. Every locale defines exactly the same keys as the English base.
3. No unsubstituted {{token}} survives into the built HTML.
4. src/games.json holds the same strings rule, plus the shape the build relies on.

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
    "lowestWins": bool,
    "trademark": bool,
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

    # 4. The catalogue.
    check_games(failures)

    # 3. No unrendered tokens in the build output. Two kinds: the {{key}} the
    # templates use, and the {n} / {play} / {low} the catalogue's counts are
    # written as. The second only reaches HTML through a locale string, so a
    # leftover one means a locale spelled a count the build does not substitute.
    if DIST.exists():
        for page in sorted(DIST.rglob("*.html")):
            text = page.read_text("utf-8")
            for token in re.findall(r"\{\{\w+\}\}", text):
                failures.append(f"{page.relative_to(DIST)}: unrendered token {token}")
            for token in re.findall(r"\{(?:n|play|low|min|max)\}", text):
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
