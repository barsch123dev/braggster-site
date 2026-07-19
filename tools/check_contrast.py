#!/usr/bin/env python3
"""WCAG 2.1 contrast gate for the Braggster palette.

The prototype shipped white labels on brag orange (2.51:1), #98A2B3 eyebrows on
felt (2.39:1), and link text in table blue on felt (4.45:1). All three fail AA.
This test pins the corrected pairings so a future palette edit cannot silently
reintroduce the failure.
"""

from __future__ import annotations

import sys

INK = "#16243D"
BRAG = "#F08A24"
# Brand fill colour. Decorative use only: it is 4.45:1 on felt, so not for text.
TABLE = "#2D6BE4"
# Same hue, 5% darker, for link text.
LINK = "#2B66D9"
FELT = "#F7F5F0"
SURFACE = "#FFFFFF"
MUTED = "#5B6B85"
MUTED_ON_DARK = "#93A2BD"
WHITE = "#FFFFFF"
# Badge and tile tints, used behind ink labels on the games page.
TINT_BLUE = "#E3ECFC"
TINT_ORANGE = "#FDEBD6"

AA_NORMAL = 4.5
AA_LARGE = 3.0

# (description, foreground, background, required ratio)
PAIRS = [
    ("body text on felt", INK, FELT, AA_NORMAL),
    ("muted body on felt", MUTED, FELT, AA_NORMAL),
    ("eyebrow on felt", MUTED, FELT, AA_NORMAL),
    ("link text on felt", LINK, FELT, AA_NORMAL),
    ("link text on surface", LINK, SURFACE, AA_NORMAL),
    ("card body on surface", MUTED, SURFACE, AA_NORMAL),
    ("primary CTA label on brag orange", INK, BRAG, AA_NORMAL),
    ("hero CTA label on ink", FELT, INK, AA_NORMAL),
    ("announcement text on ink", FELT, INK, AA_NORMAL),
    ("announcement 'New' on ink", BRAG, INK, AA_LARGE),
    ("banner sub on ink", MUTED_ON_DARK, INK, AA_NORMAL),
    ("banner heading on ink", FELT, INK, AA_NORMAL),
    # Games page.
    ("game meta on surface", MUTED, SURFACE, AA_NORMAL),
    ("game tag words on surface", MUTED, SURFACE, AA_NORMAL),
    ("'Play in app' badge on blue tint", INK, TINT_BLUE, AA_NORMAL),
    ("'Lowest wins' badge on orange tint", INK, TINT_ORANGE, AA_NORMAL),
    ("unselected filter label on surface", INK, SURFACE, AA_NORMAL),
    ("selected filter label on ink", FELT, INK, AA_NORMAL),
    ("games page intro on felt", MUTED, FELT, AA_NORMAL),
]

# Pairings the design shipped that must never come back.
REGRESSIONS = [
    ("white label on brag orange", WHITE, BRAG),
    ("faint #98A2B3 on felt", "#98A2B3", FELT),
    ("brand table blue as link text on felt", TABLE, FELT),
]


def _channel(value: int) -> float:
    c = value / 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _channel(r) + 0.7152 * _channel(g) + 0.0722 * _channel(b)


def contrast(fg: str, bg: str) -> float:
    a, b = luminance(fg), luminance(bg)
    lighter, darker = max(a, b), min(a, b)
    return (lighter + 0.05) / (darker + 0.05)


def main() -> int:
    failures = []

    for label, fg, bg, required in PAIRS:
        ratio = contrast(fg, bg)
        status = "ok " if ratio >= required else "FAIL"
        print(f"  {status} {ratio:5.2f}:1 (needs {required}) {label}")
        if ratio < required:
            failures.append(f"{label}: {ratio:.2f}:1 below {required}:1")

    for label, fg, bg in REGRESSIONS:
        ratio = contrast(fg, bg)
        if ratio >= AA_NORMAL:
            failures.append(f"{label} now passes; update this guard")
        else:
            print(f"  ok  {ratio:5.2f}:1 known-bad pairing stays unused: {label}")

    if failures:
        print("\ncontrast check failed:", file=sys.stderr)
        for line in failures:
            print(f"  {line}", file=sys.stderr)
        return 1

    print("\ncontrast check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
