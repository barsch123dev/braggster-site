# braggster.com

The marketing site for [Braggster](https://braggster.com), the score-keeping companion for
real-life game nights. Static HTML, no framework, and the only script on a page is the
Microsoft Clarity tag (see [Analytics](#analytics)), with one exception: the Live Table invite
fallback at `/t/` (see [Live Table invite links](#live-table-invite-links)) carries a 10-line
inline script instead and no Clarity tag. Deployed to GitHub Pages on every push to `main`.

The Braggster app itself lives in a separate, private repository. This repo contains only the
public website.

## Layout

```
src/home.html          page template
src/games.html         games catalogue template
src/game.html          one page per game, /games/<id>/
src/play-together.html the Play together landing page, /play-together/
src/gamepages/*.json   per-game prose (lead, scoring), one file per language
src/privacy.html       privacy policy template
src/table.html         Live Table invite fallback (/t/), noindex, not in the sitemap
src/well-known/        files served from /.well-known/ (apple-app-site-association)
src/blog.html          blog index template
src/article.html       one blog article
src/blog/<locale>/*.md the articles themselves; see src/blog/README.md
src/games.json         the game catalogue: 73 entries, extracted from the app
src/gamenames.json     each game's name in each locale, copied from the app's ARBs
src/styles.css         all styling; brand tokens live in :root
src/locales/*.json     one file per language, all copy
assets/                logos, favicons, self-hosted fonts, share card, app screenshots
tools/build.py         renders src/ into dist/
tools/build_fonts.py   subsets the font TTFs to Latin woff2 (rarely needed)
tools/build_og.py      regenerates the Open Graph share card (rarely needed)
tools/build_screenshots.py  resizes the app's store captures into web WebP (per app release)
tools/sync_game_names.py    copies the app's localized game names into src/gamenames.json (per app release)
tools/check_copy.py    no em dashes, locale key parity, no unrendered tokens, games.json shape, gamepages and gamenames parity
tools/check_contrast.py WCAG AA contrast gate for the palette
```

English is canonical and served from `/`. The other six languages live under `/nl/`, `/es/`,
`/fr/`, `/de/`, `/pt-br/` and `/it/`, matching the app's seven launch languages. Links between
pages are relative, so the output works from a subpath as well as from the apex domain.

## The games catalogue

`src/games.json` is the one home for the game list. It was extracted from the app repo's game
definitions (`app/lib/games/*/*_game_definition.dart`), and the counts it encodes are the app's
(v3.1.0): 73 games, 34 card / 2 dice / 10 board / 18 puzzle / 7 sports / 2 always free, 31
playable in the app, 6 against the computer, 6 playable together on several phones, 25 that rank
lowest-wins, 9 that carry a publisher disclaimer. Those numbers are not written into the copy: the
locales spell them `{n}`, `{play}`, `{ai}`, `{together}`, `{puzzles}` and `{low}`, and `build.py`
counts games.json and substitutes. They were spelled out until the app shipped its 54th game and all seven locales had
to be chased, and `check_copy.py` now fails on a placeholder that survives into the HTML. `/games/` renders from it, and the
home page teaser chips take their names from it too, so nothing here is hand-kept twice.

Game names are proper nouns and are never translated. Neither is `functionality`, which is
reference data in English that the page deliberately does not render as prose: doing so would put
untranslated English paragraphs on six of the seven locales. What the page shows is the name, the
player count, the category, the badges and the tag words, all of which are either language-neutral
or come from `src/locales/`. The tag words are other names, regional names and translations, and
they are rendered as real text because they exist to be found.

The category filter and the three toggles (play in app, play the computer, play together) are plain
radio and checkbox inputs with **no JavaScript**. `build.py` generates `:has(:checked)` rules from
`games.json` into a `<style>` block on the page, including the rules that show the empty state for
the filter combinations that genuinely match nothing. A browser without `:has()` shows all 73, which is the right fallback for
a page whose job is to list them. If you add a category, the CSS follows automatically; there is
no hand-written selector to keep in sync.

## Per-game pages and Play together

Every game has its own page at `/games/<id>/` in all seven languages, 511 pages in all. The prose
is two fields per game in `src/gamepages/<locale>.json`: `lead` (what the game is, also the meta
description, so at most 160 characters) and `scoring` (what braggster's sheet or board does).
Everything else on the page is generated from the `games.json` flags and shared `game_*` locale
keys: the H1 ("Play X" when playable, "X score sheet" otherwise), the "What you can do" list, a
two or three question FAQ, related games from the same category, a link to the game's blog guide
(any article whose `game_id` names it), and the trademark disclaimer when `trademark` is set. Each
page emits `WebPage`, `BreadcrumbList` and `FAQPage` JSON-LD. `check_copy.py` fails if any locale
is missing a game, has an empty field or an over-long lead, or (in English) uses wagering words.

`/play-together/` is the landing page for the multi-phone mode (`pt_*` keys). Its games list comes
from the `playTogether` flag, so a game the app adds to Play together appears there by itself. The
copy says "the same Wi-Fi" and never "online": the mode is local network only.

## The blog

`/blog/` and `/blog/<slug>/`, in all seven languages, from markdown under `src/blog/<locale>/`.
Nineteen articles: four category pillars, the Play together guide and fourteen per-game guides, written to give the site
something to rank for besides the home page and `/games/`.

`build.py` renders the markdown itself, in a deliberately small closed subset rather than through a
library, because the no-dependency rule above matters more here than generality. It raises on any
construct it does not recognise, so an unsupported one fails the build rather than reaching a page
as literal text. Each article emits `Article`, `BreadcrumbList` and `FAQPage` JSON-LD, the last
lifted out of the article's own FAQ section.

Front matter shape, the copy rules, the translation brief and the backlog all live in
[`src/blog/README.md`](src/blog/README.md). Read that before writing or editing an article.

## Build and check

```bash
python3 tools/build.py          # writes dist/
python3 tools/check_contrast.py # WCAG AA gate
python3 tools/check_copy.py     # copy and i18n gate
python3 -m http.server -d dist  # preview at localhost:8000
```

No dependencies beyond the Python standard library. CI runs the same three commands.

`dist/` is **not committed**: it is in `.gitignore`, and `.github/workflows/deploy.yml` builds it on
every push to `main` and deploys it to Pages. Pull requests run the build and both gates only.

## Updating the site for an app release

1. **Catalogue.** Re-extract `src/games.json` from `GameRegistry.standard` in the app repo
   (unregistered definitions such as Bingo stay out). Check every flag against its definition:
   `playInApp` is `hasInAppPlay`, `vsComputer` is `hasComputerOpponent`, `playTogether` is
   `supportsLiveTable` (pinned in `app/test/unit/game_live_table_test.dart`), `lowestWins` is
   `rankingDirection: lowerWins`, `trademark` is a non-null `trademarkDisclaimer`, and the player
   counts come from `sideStructure`. Use the app's English display names.
2. **Local names.** Run `python3 tools/sync_game_names.py --app <app repo>/app` (default
   `~/GitHub/Spelletjesapp/app`). It rewrites `src/gamenames.json` from each definition's `BrandName`
   key in the seven ARBs; a locale that lacks the key keeps the English name, never the Dutch
   fallback. It fails on any site id it cannot map (add an alias in `SITE_TO_APP_ID` when an id
   differs) and prints English names that differ from `games.json`, which should match.
3. **Per-game prose.** Add a `lead` and `scoring` for every new id to `src/gamepages/en.json`, from
   the definition and its rules text, then to the six other locales (`check_copy.py` enforces it).
4. **Counts.** Nothing to do if the copy uses the `{n}`-style tokens. Grep the locales and the blog
   for spelled-out numbers that the tokens cannot reach, such as the card and puzzle pillar titles.
5. **Screenshots.** Regenerate them (below) and look at every frame before committing.
6. **Blog fact check.** Read the pillars for anything the release changed: new games, new play
   modes, anything the app now does that an article says it does not.
7. **Build and gates**, then read the home page, `/games/` and one new game page in two languages.

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

## Live Table invite links

Braggster's online Live Tables are joined with `https://braggster.com/t#WK7QF3XP`: an 8-character
code after the `#`. With the app installed the link opens it (iOS universal link, Android App
Link). Without it, the phone lands on `/t/` (and `/nl/t/`, `/es/t/` and so on), which reads
`location.hash`, validates it against the app's alphabet and shows the code as `WK7Q-F3XP`.

- **`/.well-known/apple-app-site-association`** comes from `src/well-known/`. It lands in a hidden
  folder of `dist/`, so the deploy depends on two things: `.nojekyll` (which `build.py` writes) and
  `actions/upload-pages-artifact@v3`, whose archive step keeps hidden paths. **Do not bump that
  action to v4 or later** without checking: those versions exclude every dot-path and the app's
  universal links would silently stop working. The workflow fails a build whose `dist/` lacks the
  manifest.
- **`/.well-known/assetlinks.json`** (Android App Links) does not exist yet. It needs the Play app
  signing certificate SHA-256 from Play Console, App integrity. Add it as
  `src/well-known/assetlinks.json` and copy it in `build.py` next to the AASA file.
- **The inline script on `/t/`** is the one script on the site besides Clarity's tag, and Clarity
  is deliberately not loaded there: the code sits in the URL fragment and a session recorder would
  capture it. The script makes no network call and uses no storage.

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
the app repo has a harness that renders the listing screens in all seven languages on a 6.9"
simulator, the same captures the App Store listing draws from. The site serves the six named in
`SHOTS` in `tools/build.py` (home, play-together, chess, games, murdoku, yahtzee).
`tools/build_screenshots.py` maps capture file names to those site names and accepts two source
layouts, both as `<folder>/<lang>/NN-name.png` with `pt_BR` for Brazilian Portuguese: the app
harness output (`app/build/screenshots/iphone69/`, files like `01-home.png`) and a listing handoff
folder such as `~/Documents/Braggster/handoff-3.0/captures/iphone69/` (files like
`01-hook-UPDATE.png`). A capture that is not in the map is ignored; a language missing any served
shot fails the run.

```bash
# in the app repo
fvm flutter drive \
  --driver=integration_test/store_screenshot_driver.dart \
  --target=integration_test/store_screenshots_test.dart \
  --dart-define=SCREENSHOT_DEVICE=iphone69 \
  -d <simulator udid>

# back here, pointing at build/screenshots/iphone69/ or a handoff captures/iphone69/ folder
python3 tools/build_screenshots.py --src <that folder>
```

`build_screenshots.py` only resizes and re-encodes: 1320x2868 PNGs of about 450KB become WebP at
320 and 640 CSS pixels. If a screenshot is wrong, fix it in the harness and capture again rather
than editing pixels here. The hero image loads eagerly and the five gallery shots lazily. The
`sudoku` and `crossword` files are written too but not currently served.

## Fonts

Baloo 2 and Outfit are self-hosted under the SIL Open Font License 1.1. See
[`assets/fonts/OFL.txt`](assets/fonts/OFL.txt). They are not hot-linked from Google Fonts, so no
visitor IP addresses are shared with a third party.

The upstream `.ttf` files stay in `assets/fonts/` as sources but are never served: `build.py`
excludes them from `dist/`. The site loads the Latin `.woff2` subsets that `build_fonts.py`
generates beside them. Baloo 2 ships a full Devanagari set that no locale here can render, and
dropping it took the two faces from 794KB to 68KB. Both keep their variable weight axis.
