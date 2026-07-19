#!/usr/bin/env python3
"""Generate the Open Graph / Twitter card image.

Deliberately text-free: the card's headline and description come from the
per-locale og:title and og:description tags, so one image serves all seven
locales and no locale can ship a card whose baked-in text contradicts its own
copy. It carries the lockup on ink navy with the brand's orange glow, which is
the same treatment as the CTA banner.

1200x630 is the size Facebook, WhatsApp, LinkedIn, Slack and X all crop from
cleanly. Anything smaller than 600x315 gets downgraded to a small summary card.

    python3 tools/build_og.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
LOGO = ROOT / "assets" / "logo" / "lockup-on-dark.png"
OUT = ROOT / "assets" / "web" / "og-card.png"

WIDTH, HEIGHT = 1200, 630
INK = (22, 36, 61)  # --ink
BRAG = (240, 138, 36)  # --brag

LOCKUP_WIDTH = 760


def main() -> int:
    if not LOGO.exists():
        raise SystemExit(f"missing lockup: {LOGO}")

    card = Image.new("RGB", (WIDTH, HEIGHT), INK)

    # Orange glow behind the lockup, mirroring .btn--glow's drop shadow. Drawn on
    # its own layer and blurred hard so it reads as light, not as a shape.
    glow = Image.new("RGB", (WIDTH, HEIGHT), INK)
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse(
        [WIDTH // 2 - 300, HEIGHT // 2 - 130, WIDTH // 2 + 300, HEIGHT // 2 + 170],
        fill=(70, 52, 46),
    )
    card = Image.blend(card, glow.filter(ImageFilter.GaussianBlur(120)), 0.9)

    # A thin brand rule along the top edge, so the card still reads as ours when
    # a client crops the sides.
    ImageDraw.Draw(card).rectangle([0, 0, WIDTH, 8], fill=BRAG)

    lockup = Image.open(LOGO).convert("RGBA")
    height = round(lockup.height * (LOCKUP_WIDTH / lockup.width))
    lockup = lockup.resize((LOCKUP_WIDTH, height), Image.LANCZOS)
    card.paste(lockup, ((WIDTH - LOCKUP_WIDTH) // 2, (HEIGHT - height) // 2), lockup)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    card.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT.relative_to(ROOT)} ({WIDTH}x{HEIGHT}, {OUT.stat().st_size:,}B)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
