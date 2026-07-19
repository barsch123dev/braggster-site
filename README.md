# braggster.com

The marketing site for [Braggster](https://braggster.com), the score-keeping companion for
real-life game nights. Static HTML, no framework, no client-side JavaScript. Deployed to GitHub
Pages on every push to `main`.

The Braggster app itself lives in a separate, private repository. This repo contains only the
public website.

## Layout

```
src/home.html          page template
src/privacy.html       privacy policy template
src/styles.css         all styling; brand tokens live in :root
src/locales/*.json     one file per language, all copy
assets/                logos, favicons, self-hosted fonts, share card
tools/build.py         renders src/ into dist/
tools/build_fonts.py   subsets the font TTFs to Latin woff2 (rarely needed)
tools/build_og.py      regenerates the Open Graph share card (rarely needed)
tools/check_copy.py    no em dashes, locale key parity, no unrendered tokens
tools/check_contrast.py WCAG AA contrast gate for the palette
```

English is canonical and served from `/`. The other six languages live under `/nl/`, `/es/`,
`/fr/`, `/de/`, `/pt-br/` and `/it/`, matching the app's seven launch languages. Links between
pages are relative, so the output works from a subpath as well as from the apex domain.

## Build and check

```bash
python3 tools/build.py          # writes dist/
python3 tools/check_contrast.py # WCAG AA gate
python3 tools/check_copy.py     # copy and i18n gate
python3 -m http.server -d dist  # preview at localhost:8000
```

No dependencies beyond the Python standard library. CI runs the same three commands.

The two asset builders are **not** part of that loop and do not run in CI. Their output is committed,
so you only run them when the input changes: `build_fonts.py` after replacing a source `.ttf`
(needs `fonttools` and `brotli`), `build_og.py` after changing the lockup (needs `Pillow`).

## Adding or changing copy

Every user-facing string lives in `src/locales/`. Add the key to `en.json` first, then to all six
other locales; `check_copy.py` fails the build if a locale is missing a key. Em dashes are banned
in every language, as they are in the app.

## Two deliberate deviations from the design handover

The design prototype specified white labels on brag orange and `#98A2B3` eyebrow text. Both fail
WCAG AA (2.51:1 and 2.36:1). Link text in `#2D6BE4` on felt also fell just short, at 4.45:1. This
site uses ink navy on orange (6.18:1), `#5B6B85` for eyebrows (4.96:1), and a 5% darker
`#2B66D9` for link text (4.81:1). The brand orange, navy, felt and the decorative table blue are
unchanged. `tools/check_contrast.py` pins these and guards against the old pairings returning.

Three em dashes in the prototype copy were rewritten as colons and commas, per the project's
user-text rule.

## Fonts

Baloo 2 and Outfit are self-hosted under the SIL Open Font License 1.1. See
[`assets/fonts/OFL.txt`](assets/fonts/OFL.txt). They are not hot-linked from Google Fonts, so no
visitor IP addresses are shared with a third party.

The upstream `.ttf` files stay in `assets/fonts/` as sources but are never served: `build.py`
excludes them from `dist/`. The site loads the Latin `.woff2` subsets that `build_fonts.py`
generates beside them. Baloo 2 ships a full Devanagari set that no locale here can render, and
dropping it took the two faces from 794KB to 68KB. Both keep their variable weight axis.
