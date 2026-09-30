#!/usr/bin/env python3
"""Copy the app's localized game names into src/gamenames.json.

Run by hand at release time, like tools/build_screenshots.py, and commit what it
writes. CI never runs this: build.py reads the committed JSON, so the build
needs neither the app repo nor anything outside the standard library.

    python3 tools/sync_game_names.py --app <path to the app/ folder>

The app names each game through a BrandName key in its ARB files, picked in
lib/games/<dir>/<dir>_game_definition.dart:

    static const String gameId = 'chess';
    ...
    (l10n) => l10n.gameChessBrandName;

This script pairs every definition's gameId with that key, reads the key from
the seven ARBs, and writes {locale: {site id: name}} for every games.json id.
A locale whose ARB lacks the key keeps the games.json (English) name. It never
takes the Dutch the app itself would fall back to, since nl is the app's
gen-l10n template and a Dutch name on a French page would be wrong twice.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAMES_FILE = ROOT / "src" / "games.json"
OUT_FILE = ROOT / "src" / "gamenames.json"

DEFAULT_APP = Path.home() / "GitHub" / "Spelletjesapp" / "app"

# Site locale code -> the app's ARB suffix.
ARB_SUFFIX = {
    "en": "en",
    "nl": "nl",
    "de": "de",
    "es": "es",
    "fr": "fr",
    "it": "it",
    "pt-BR": "pt_BR",
}

# Site ids that differ from the app's gameId. The site's URLs were set before
# the app ids were settled, and a URL is not worth breaking for a rename.
SITE_TO_APP_ID = {
    "generic": "generic_board",
    "unoflip": "unoFlip",
}

GAME_ID = re.compile(r"""\bgameId\s*=\s*['"]([^'"]+)['"]""")
BRAND_KEY = re.compile(r"\bl10n\.(game\w*BrandName)\b")


def app_brand_keys(app: Path) -> dict[str, str]:
    """App gameId -> its BrandName ARB key, one pair per game definition."""
    keys: dict[str, str] = {}
    files = sorted(app.glob("lib/games/*/*_game_definition.dart"))
    if not files:
        sys.exit(f"no game definitions under {app / 'lib' / 'games'}; is --app the app/ folder?")
    for path in files:
        text = path.read_text("utf-8")
        ids = set(GAME_ID.findall(text))
        brands = set(BRAND_KEY.findall(text))
        if len(ids) != 1 or len(brands) != 1:
            sys.exit(f"{path}: expected one gameId and one BrandName key, found {ids} and {brands}")
        (game_id,), (key,) = ids, brands
        if game_id in keys:
            sys.exit(f"{path}: gameId {game_id!r} is defined twice")
        keys[game_id] = key
    return keys


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--app", type=Path, default=DEFAULT_APP, help="the app repo's app/ folder")
    app = parser.parse_args().app.expanduser().resolve()

    games = json.loads(GAMES_FILE.read_text("utf-8"))["games"]
    keys = app_brand_keys(app)

    # Every site game must map to an app definition; app-only ids (a game the
    # site does not list yet) are simply not asked for.
    unmapped = [g["id"] for g in games if SITE_TO_APP_ID.get(g["id"], g["id"]) not in keys]
    if unmapped:
        sys.exit(f"no app game definition for site id(s): {', '.join(unmapped)}")

    arbs = {}
    for code, suffix in ARB_SUFFIX.items():
        path = app / "lib" / "l10n" / f"app_{suffix}.arb"
        if not path.exists():
            sys.exit(f"missing ARB: {path}")
        arbs[code] = json.loads(path.read_text("utf-8"))

    names: dict[str, dict[str, str]] = {}
    fallbacks: dict[str, list[str]] = {}
    for code in sorted(ARB_SUFFIX):
        table = {}
        for game in games:
            key = keys[SITE_TO_APP_ID.get(game["id"], game["id"])]
            name = arbs[code].get(key)
            if not isinstance(name, str) or not name.strip():
                name = game["name"]
                fallbacks.setdefault(code, []).append(game["id"])
            table[game["id"]] = name.strip()
        names[code] = dict(sorted(table.items()))

    OUT_FILE.write_text(json.dumps(names, indent=2, ensure_ascii=False, sort_keys=True) + "\n", "utf-8")

    print(f"wrote {OUT_FILE.relative_to(ROOT)}: {len(games)} games x {len(names)} locales")
    for code in sorted(ARB_SUFFIX):
        local = sum(1 for g in games if names[code][g["id"]] != names["en"][g["id"]])
        kept = fallbacks.get(code, [])
        note = f", kept games.json name for {', '.join(kept)}" if kept else ""
        print(f"  {code}: {local} differ from English{note}")
    mismatched = [
        f"{g['id']} ({g['name']!r} in games.json, {names['en'][g['id']]!r} in the app)"
        for g in games
        if names["en"][g["id"]] != g["name"]
    ]
    if mismatched:
        print("English names that differ from games.json:\n  " + "\n  ".join(mismatched))


if __name__ == "__main__":
    main()
