#!/usr/bin/env python3
"""Turn the app's store captures into the web screenshots the site serves.

Run by hand, like tools/build_og.py and tools/build_fonts.py, and commit what it
writes. build.py copies assets/ wholesale into dist/, so the output needs no
further wiring. CI never runs this: it needs Pillow, and the build itself stays
on the standard library.

    python3 tools/build_screenshots.py --src <dir>

The captures come from the app repo's own harness, which renders the four
listing screens in all seven languages on a 6.9" simulator:

    fvm flutter drive \\
      --driver=integration_test/store_screenshot_driver.dart \\
      --target=integration_test/store_screenshots_test.dart \\
      --dart-define=SCREENSHOT_DEVICE=iphone69 \\
      -d <simulator udid>

Regenerate them there rather than editing pixels here. They arrive as 1320x2868
PNGs of about 450KB each; the site shows them 320 CSS pixels wide, so they go
out as WebP at 1x and 2x, which is roughly a fortieth of the weight.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "assets" / "screenshots"

DEFAULT_SRC = (
    Path.home() / "GitHub" / "Spelletjesapp" / "app" / "build" / "screenshots" / "iphone69"
)

# Capture folder -> site locale. Only the Brazilian one differs.
LOCALES = {
    "en": "en",
    "nl": "nl",
    "es": "es",
    "fr": "fr",
    "de": "de",
    "pt_BR": "pt-BR",
    "it": "it",
}

# Capture stem -> the name the site uses. The captures are numbered for the App
# Store's slot order; the site refers to them by what they show.
SHOTS = {
    "01-home": "home",
    "02-games": "games",
    "03-yahtzee": "yahtzee",
    "04-sudoku": "sudoku",
}

#: The phone frame is 320 CSS pixels wide on the site, and the srcset offers the
#: same again for denser screens.
WIDTH_1X = 320
WIDTH_2X = 640
WEBP_QUALITY = 82

#: Every capture is one 6.9" screen. A mismatch means the harness ran against
#: the wrong simulator, which is worth stopping for rather than quietly
#: publishing a set whose frames do not line up with each other.
EXPECTED_SIZE = (1320, 2868)


def encode(image: Image.Image, path: Path, width: int) -> int:
    height = round(image.height * width / image.width)
    resized = image.resize((width, height), Image.LANCZOS)
    path.parent.mkdir(parents=True, exist_ok=True)
    resized.save(path, "WEBP", quality=WEBP_QUALITY, method=6)
    return path.stat().st_size


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the site's app screenshots.")
    parser.add_argument("--src", type=Path, default=DEFAULT_SRC, help="capture folder")
    args = parser.parse_args()

    if not args.src.is_dir():
        print(f"no captures at {args.src}", file=sys.stderr)
        return 1

    written: list[tuple[str, int]] = []
    for folder, locale in LOCALES.items():
        for stem, name in SHOTS.items():
            source = args.src / folder / f"{stem}.png"
            if not source.exists():
                print(f"missing {source}", file=sys.stderr)
                return 1
            image = Image.open(source).convert("RGB")
            if image.size != EXPECTED_SIZE:
                print(
                    f"{source} is {image.size[0]}x{image.size[1]}, expected "
                    f"{EXPECTED_SIZE[0]}x{EXPECTED_SIZE[1]}",
                    file=sys.stderr,
                )
                return 1
            for width, suffix in ((WIDTH_1X, ""), (WIDTH_2X, "@2x")):
                out = OUT_DIR / locale / f"{name}{suffix}.webp"
                written.append((str(out.relative_to(ROOT)), encode(image, out, width)))

    total = sum(size for _, size in written)
    biggest = max(written, key=lambda entry: entry[1])
    print(f"wrote {len(written)} files, {total / 1024:.0f}KB total")
    print(f"largest: {biggest[0]} at {biggest[1] / 1024:.0f}KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
