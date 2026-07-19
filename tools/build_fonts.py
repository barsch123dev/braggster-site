#!/usr/bin/env python3
"""Subset the brand fonts to Latin and repack them as woff2.

The upstream TTFs ship every script the family supports. Baloo 2 in particular
carries a full Devanagari set, which is most of its 683KB and none of which this
site can render: all seven locales are Latin. Subsetting to the ranges below and
recompressing as woff2 is the single largest weight saving available here.

Both faces stay variable. The CSS uses several weights per family, so instancing
them to statics would trade one download for several.

Sources live in assets/fonts/*.ttf and are not shipped; build.py copies only the
generated .woff2 (plus the OFL, which must travel with the fonts) into dist/.

Run after replacing a source TTF:

    python3 tools/build_fonts.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"

FACES = ["Baloo2", "Outfit"]

# Deliberately generous rather than derived from the current copy: a subset built
# from today's strings would silently lose glyphs the next time someone writes a
# word with an unusual accent. These ranges cover every Latin-script locale we
# could plausibly add, and cost about 2KB over a minimal subset.
UNICODES = ",".join(
    [
        "U+0020-007E",  # Basic Latin
        "U+00A0-00FF",  # Latin-1 Supplement: nl, es, fr, de, pt-BR, it accents
        "U+0100-017F",  # Latin Extended-A: headroom for further locales
        "U+2018-201D",  # curly quotes
        "U+2026",  # ellipsis
        "U+20AC",  # euro
    ]
)


def subset(face: str) -> tuple[int, int]:
    src = FONTS / f"{face}.ttf"
    dst = FONTS / f"{face}.woff2"
    if not src.exists():
        raise SystemExit(f"missing source font: {src}")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "fontTools.subset",
            str(src),
            f"--unicodes={UNICODES}",
            "--flavor=woff2",
            f"--output-file={dst}",
            # Keep the variable axes and the layout features the faces rely on.
            "--layout-features=kern,liga,calt",
            "--name-IDs=*",
            "--drop-tables+=DSIG",
        ],
        check=True,
        capture_output=True,
    )
    return src.stat().st_size, dst.stat().st_size


def main() -> int:
    before = after = 0
    for face in FACES:
        src_size, dst_size = subset(face)
        before += src_size
        after += dst_size
        pct = 100 * (1 - dst_size / src_size)
        print(f"  {face}.ttf {src_size:>7,}B -> {face}.woff2 {dst_size:>7,}B  ({pct:.1f}% smaller)")

    pct = 100 * (1 - after / before)
    print(f"fonts: {before:,}B -> {after:,}B ({pct:.1f}% smaller, {before - after:,}B saved)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
