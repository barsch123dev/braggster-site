#!/usr/bin/env python3
"""Copy and locale gate.

Three checks, mirroring the app's user-text lint and i18n parity test:

1. No em dashes (or en dashes used as punctuation) in any user-facing string.
2. Every locale defines exactly the same keys as the English base.
3. No unsubstituted {{token}} survives into the built HTML.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCALES_DIR = ROOT / "src" / "locales"
DIST = ROOT / "dist"

BASE = "en"
BANNED = {"—": "em dash", "–": "en dash"}


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

    # 3. No unrendered tokens in the build output.
    if DIST.exists():
        for page in sorted(DIST.rglob("*.html")):
            for token in re.findall(r"\{\{\w+\}\}", page.read_text("utf-8")):
                failures.append(f"{page.relative_to(DIST)}: unrendered token {token}")

    if failures:
        print(f"copy check failed ({len(failures)} problems):", file=sys.stderr)
        for line in failures:
            print(f"  {line}", file=sys.stderr)
        return 1

    print(f"copy check passed: {len(locales)} locales, {len(locales[BASE])} keys each")
    return 0


if __name__ == "__main__":
    sys.exit(main())
