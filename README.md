# braggster.com

The marketing site for [Braggster](https://braggster.com), the score-keeping companion for
real-life game nights. Static HTML, no framework, and the only script on the page is the
Microsoft Clarity tag (see [Analytics](#analytics)). Deployed to GitHub Pages on every push to
`main`.

The Braggster app itself lives in a separate, private repository. This repo contains only the
public website.

## Layout

```
src/home.html          page template
src/games.html         games catalogue template
src/privacy.html       privacy policy template
src/games.json         the game catalogue: 54 entries, extracted from the app
src/styles.css         all styling; brand tokens live in :root
src/locales/*.json     one file per language, all copy
assets/                logos, favicons, self-hosted fonts, share card, app screenshots
tools/build.py         renders src/ into dist/
tools/build_fonts.py   subsets the font TTFs to Latin woff2 (rarely needed)
tools/build_og.py      regenerates the Open Graph share card (rarely needed)
tools/build_screenshots.py  resizes the app's store captures into web WebP (per app release)
tools/check_copy.py    no em dashes, locale key parity, no unrendered tokens, games.json shape
tools/check_contrast.py WCAG AA contrast gate for the palette
```

English is canonical and served from `/`. The other six languages live under `/nl/`, `/es/`,
`/fr/`, `/de/`, `/pt-br/` and `/it/`, matching the app's seven launch languages. Links between
pages are relative, so the output works from a subpath as well as from the apex domain.

## The games catalogue

`src/games.json` is the one home for the game list. It was extracted from the app repo's game
definitions (`app/lib/games/*/*_game_definition.dart`), and the counts it encodes are the app's:
54 games, 33 card / 2 dice / 10 board / 7 sports / 2 always free, 12 playable in the app,
7 that rank lowest-wins, 6 that carry a publisher disclaimer. Those numbers are not written into
the copy: the locales spell them `{n}`, `{play}` and `{low}`, and `build.py` counts games.json and
substitutes. They were spelled out until the app shipped its 54th game and all seven locales had
to be chased, and `check_copy.py` now fails on a placeholder that survives into the HTML. `/games/` renders from it, and the
home page teaser chips take their names from it too, so nothing here is hand-kept twice.

Game names are proper nouns and are never translated. Neither is `functionality`, which is
reference data in English that the page deliberately does not render as prose: doing so would put
untranslated English paragraphs on six of the seven locales. What the page shows is the name, the
player count, the category, the badges and the tag words, all of which are either language-neutral
or come from `src/locales/`. The tag words are other names, regional names and translations, and
they are rendered as real text because they exist to be found.

The category filter and the play-in-app toggle are plain radio and checkbox inputs with **no
JavaScript**. `build.py` generates `:has(:checked)` rules from `games.json` into a `<style>` block
on the page, including the rules that show the empty state for the three filter pairs that
genuinely match nothing. A browser without `:has()` shows all 54, which is the right fallback for
a page whose job is to list them. If you add a category, the CSS follows automatically; there is
no hand-written selector to keep in sync.

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

## Analytics

The site runs [Microsoft Clarity](https://clarity.microsoft.com) for heatmaps and scroll depth,
pinned to cookieless mode. `build.py` emits the tag followed immediately by

```js
window.clarity('consentv2', {ad_Storage: 'denied', analytics_Storage: 'denied'});
```

The tag shim queues that call before the remote script loads, so Clarity sees a denied signal
before it can write anything: no `_clck`, no `_clsk`, no third-party cookie, and no id that
survives a page view. That is what keeps the site free of a cookie banner. The cost is deliberate:
returning visitors are not stitched together, so session counts and recordings are weaker than a
consented setup would give.

Cookies are switched off in the Clarity project settings as well (Settings, then Setup). The two
controls are independent on purpose and neither one is redundant. The dashboard setting is the
account-level default and can be flipped by anyone with access to the project; the `consentv2`
call is the one that lives in version control, ships with the page, and is reviewable in a diff.
Keep both.

Clarity is still a third party receiving visitor IP addresses and interaction data, so it is
disclosed in `privacy_website_p` in all seven locales. **If you remove the `consentv2` call, add a
consent banner, or point the tag at a different project, the privacy copy has to change with it.**

## Two deliberate deviations from the design handover

The design prototype specified white labels on brag orange and `#98A2B3` eyebrow text. Both fail
WCAG AA (2.51:1 and 2.36:1). Link text in `#2D6BE4` on felt also fell just short, at 4.45:1. This
site uses ink navy on orange (6.18:1), `#5B6B85` for eyebrows (4.96:1), and a 5% darker
`#2B66D9` for link text (4.81:1). The brand orange, navy, felt and the decorative table blue are
unchanged. `tools/check_contrast.py` pins these and guards against the old pairings returning.

Three em dashes in the prototype copy were rewritten as colons and commas, per the project's
user-text rule.

## Screenshots

The phone screenshots are real captures of the app, one set per language. They are not made here:
the app repo has a harness that renders the four listing screens in all seven languages on a 6.9"
simulator, and it is the same set the App Store listing uses.

```bash
# in the app repo
fvm flutter drive \
  --driver=integration_test/store_screenshot_driver.dart \
  --target=integration_test/store_screenshots_test.dart \
  --dart-define=SCREENSHOT_DEVICE=iphone69 \
  -d <simulator udid>

# back here, pointing at build/screenshots/iphone69/
python3 tools/build_screenshots.py --src <that folder>
```

`build_screenshots.py` only resizes and re-encodes: 1320x2868 PNGs of about 450KB become WebP at
320 and 640 CSS pixels, 1.2MB for all 56 files. If a screenshot is wrong, fix it in the harness and
capture again rather than editing pixels here. The hero image loads eagerly and the three gallery
shots lazily, so a first view pulls one 21KB image rather than four.

## Fonts

Baloo 2 and Outfit are self-hosted under the SIL Open Font License 1.1. See
[`assets/fonts/OFL.txt`](assets/fonts/OFL.txt). They are not hot-linked from Google Fonts, so no
visitor IP addresses are shared with a third party.

The upstream `.ttf` files stay in `assets/fonts/` as sources but are never served: `build.py`
excludes them from `dist/`. The site loads the Latin `.woff2` subsets that `build_fonts.py`
generates beside them. Baloo 2 ships a full Devanagari set that no locale here can render, and
dropping it took the two faces from 794KB to 68KB. Both keep their variable weight axis.
