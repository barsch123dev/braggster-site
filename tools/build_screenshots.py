#!/usr/bin/env python3
"""Turn the app's store captures into the web screenshots the site serves.

Run by hand, like tools/build_og.py and tools/build_fonts.py, and commit what it
writes. build.py copies assets/ wholesale into dist/, so the output needs no
further wiring. CI never runs this: it needs Pillow, and the build itself stays
on the standard library.

    python3 tools/build_screenshots.py --src <dir>

The captures come from the app repo's own harness, which renders the listing
screens in all seven languages on a 6.9" simulator, or from a listing handoff
folder in the same <lang>/ layout; the site serves the handful named in
SITE_NAMES below:

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
#
# Two capture layouts are accepted, and the map holds both. The app repo's own
# harness writes app/build/screenshots/iphone69/<lang>/NN-name.png; the 3.0
# listing handoff (~/Documents/Braggster/handoff-3.0/captures/iphone69/<lang>/)
# names the same screens after their slot and status. A stem that is not in the
# source folder is skipped; a folder missing any of SITE_NAMES fails.
SHOTS = {
    # The app harness.
    "01-home": "home",
    "02-games": "games",
    "03-yahtzee": "yahtzee",
    "05-chess": "chess",
    "07-murdoku": "murdoku",
    "08-sudoku": "sudoku",
    "10-play-together": "play-together",
    # The 3.0 listing handoff.
    "01-hook-UPDATE": "home",
    "02-games-UPDATE": "games",
    "03-play-together-NEW": "play-together",
    "04-dice-UPDATE": "yahtzee",
    "05-boards-CHECK": "chess",
    "06-murder-sudoku-CHECK": "murdoku",
    "07-solo-CHECK": "sudoku",
    "08-crossword-UPDATE": "crossword",
    # Supporting captures the listing does not use, served in the blog guides.
    "xx-backgammon-SUPPORTING": "backgammon",
}

#: The shots the site actually serves (SHOTS in tools/build.py). Every one of
#: them has to come out of a run, whichever layout the captures are in.
SITE_NAMES = {"home", "play-together", "chess", "games", "murdoku", "yahtzee"}

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
        produced: set[str] = set()
        for stem, name in SHOTS.items():
            source = args.src / folder / f"{stem}.png"
            if not source.exists():
                continue
            produced.add(name)
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
        missing = SITE_NAMES - produced
        if missing:
            print(f"{args.src / folder}: no capture for {sorted(missing)}", file=sys.stderr)
            return 1

    total = sum(size for _, size in written)
    biggest = max(written, key=lambda entry: entry[1])
    print(f"wrote {len(written)} files, {total / 1024:.0f}KB total")
    print(f"largest: {biggest[0]} at {biggest[1] / 1024:.0f}KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
