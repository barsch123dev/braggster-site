# Handover: bringing braggster.com in line with the app

Written 18 July 2026. Audience: whoever picks up this repo next (human or agent). It assumes no
prior context on either repo.

The short version: the site is structurally healthy and needs no redesign. There is **one item that
matters** (the privacy page no longer matches what the app collects) and a handful of optional
refreshes. Read section 4 first.

---

## 1. What this repo is

- **`barsch123dev/braggster-site`**, public. The marketing site for Braggster, the game night
  scorekeeper app.
- Live at **braggster.com**, served by **GitHub Pages** from `dist/`. The apex domain is pinned by
  the `CNAME` file; DNS is managed at **TransIP**.
- Static: no framework, no JS build step, no runtime dependencies. Seven languages.
- The app itself lives in a separate repo, **`barsch123dev/Spelletjesapp`** (the product is
  Braggster; the repo keeps its original name).

## 2. How the site is built

```
src/home.html          Template with {{token}} placeholders
src/privacy.html       Same, for the privacy page
src/locales/*.json     All copy: en, nl, es, fr, de, pt-BR, it
src/styles.css         Styles
tools/build.py         Renders templates x locales into dist/
tools/check_copy.py    Copy gate
tools/check_contrast.py WCAG contrast gate
dist/                  GENERATED OUTPUT, committed to the repo
```

**`dist/` is generated. Never hand-edit it.** Change `src/`, then re-run the build. English renders
at the root (`dist/index.html`); the other six render at `dist/<lang>/`.

The two gates are not optional, and CI runs both on every pull request:

- **`check_copy.py`** enforces three things: **no em dashes** (or en dashes used as punctuation) in
  any user-facing string, **exact locale key parity** with the English base, and **no unsubstituted
  `{{token}}`** surviving into the built HTML. Adding a key to `en.json` and forgetting the other
  six locales fails the build.
- **`check_contrast.py`** pins the corrected WCAG AA colour pairings so a palette edit cannot
  silently reintroduce a contrast failure.

`.github/workflows/deploy.yml` builds and runs both gates on pull requests, and deploys to Pages on
push to `main`.

### The loop

```bash
cd braggster-site
git checkout -b my-change origin/main
# edit src/ and src/locales/*.json
python3 tools/build.py
python3 tools/check_copy.py
python3 tools/check_contrast.py
git add src dist          # commit BOTH the source and the generated output
git commit -m "..."
gh pr create --base main
# merge to main; Pages deploys automatically
```

## 3. Current state of the site

Last content change was **12 July 2026** ("Refresh games chips to reflect the current catalog").

- The games section is a **representative slice**, not a full catalogue: twelve chips
  (Klaverjassen, Poker, Bridge, Hearts, Briscola, Belote, Skat, Truco, Yahtzee, Dudo, Darts,
  Rummikub) plus an "Any board game" chip and a "coming soon" chip.
- **There is no total game count anywhere in the copy.** This is a good decision and worth keeping:
  the app's catalogue keeps growing, and a hardcoded number would go stale every time it does. No
  number needs chasing.
- `announce_text` still reads "Braggster is coming to iOS and Android", which is accurate while the
  app is pre-release.
- The hero image is still a **placeholder**: `phone_alt` is literally "Placeholder for a screenshot
  of the Braggster app". There is no real app screenshot on the site.
- Housekeeping: the local branch `update-games-catalog` has **no net content difference** from
  `origin/main`. It is spent and can be deleted.

## 4. Priority item: the privacy page no longer matches the app

**This is the one thing that should not wait.**

The privacy page was written on 10 July 2026 and says, under "What we collect":

> Nothing. Braggster has no analytics, no advertising, no trackers, and no crash reporting that
> identifies you.

On **16 July 2026** the app adopted **Firebase Crashlytics** (`Spelletjesapp/docs/DECISIONS.md`,
decision **D25**). Per `Spelletjesapp/docs/STORE_COMPLIANCE.md`, the app now collects exactly one
thing, crash diagnostics, and its store privacy labels declare **"Diagnostics / Crash Data, not
linked to identity, not used for tracking"** on Apple's App Privacy form and Google's Data Safety
form.

So the site currently leads with "Nothing" while the app's own store listing declares a data
collection. The hedge "no crash reporting **that identifies you**" is defensible in isolation, since
Crashlytics data is not linked to identity, but the leading "Nothing" is not, and a reviewer
comparing the privacy label against the linked privacy policy will see two different answers. The
site should say the same thing the store label says.

**What to change**

- Key **`privacy_collect_p`** in **all seven** locale files. Keep the "no analytics, no advertising,
  no trackers" promise, which still holds and is load-bearing. Replace the leading "Nothing" and the
  crash-reporting clause with an honest, narrow disclosure of crash diagnostics: what is sent (crash
  stacks, device model, OS version, a Crashlytics-generated install id), that it is not linked to
  identity, that it is not used for tracking, and that scores and players never leave the device.
- Key **`privacy_updated`** in all seven locales: bump from 10 July 2026 to the date you ship the
  change, in each locale's own date format (the existing values show the expected formats).
- Re-read the surrounding keys (`privacy_intro`, `privacy_stored_p`) and make sure none of them
  still imply zero collection.

**Source of truth:** `Spelletjesapp/docs/STORE_COMPLIANCE.md` (privacy label section) and
`docs/DECISIONS.md` D25. Match their wording rather than inventing new phrasing, so the site, the
App Store label and the Play Data Safety form all say one thing. If the app's crash reporting is
ever removed, this section reverts and the "Nothing" wording becomes correct again.

## 5. What changed in the app since the site was last touched

Context for the optional updates below. None of it breaks the site, because the site never committed
to a game count.

- **The catalogue is now about 50 games** plus the always-free Blank scorecard (the registry holds 51
  definitions). The site shows 12 representative chips, so nothing is factually wrong.
- **New since 12 July:** Chess, Checkers, Backgammon and Sudoku, all four with an in-app play mode.
  Also a Yahtzee scorecard fix and a new Home "brag mode".
- **The product is no longer only a scorekeeper.** Several games are now genuinely playable in the
  app rather than merely scored: Blackjack, Solitaire (Klondike), Dominoes (hotseat tile board),
  Loteria (single-device caller), Tic Tac Toe, Chess, Checkers, Backgammon (hotseat boards) and
  Sudoku (a generated 9x9 puzzle across five difficulty tiers). The site's current pitch is purely
  "keep score for any game", which undersells this.
- **Home brag mode:** a toggle turns each game tile's caption into your record for that game, a win
  rate or a win streak once it reaches two, and crowns the single best-streak game with a champion
  tile. The existing "Stats that brag" feature block already covers this thematically.

The app repo's `games.md` is the full inventory if you need per-game detail.

## 6. Optional updates, in rough priority order

These are judgement calls for the owner, not defects.

**a. Refresh the chip slice.** The twelve chips lean heavily card-game. Swapping two or three for
**Chess, Backgammon and Sudoku** would show the board and puzzle breadth the app now has. Edit
`GAME_NAMES` in `tools/build.py`. Chips are proper nouns and are deliberately **not translated**, so
this needs **no locale changes** and cannot break key parity. Keep the slice around a dozen; the
"Any board game" and "coming soon" chips carry the rest.

**b. Broaden the pitch from "score" to "score and play".** Feature block `f1` ("Score anything") and
the hero copy both frame Braggster as a scorekeeper only. Now that nine games are playable in-app,
one of the three feature blocks could say so. This is a **copy change, so all seven locales** must
change together or `check_copy.py` fails. Consider whether this is on-message before doing it: the
scorekeeper framing is clean and the in-app play is a bonus, so this may be deliberate.

**c. Replace the placeholder screenshot.** `phone_alt` is still placeholder text and there is no real
app image. A Home screenshot with brag mode on would be the strongest single visual upgrade. Needs an
image asset plus a real `phone_alt` alt text in all seven locales (it is alt text, so it must be
descriptive, not decorative).

**d. Flip the announcement at release.** `announce_text` says "coming to iOS and Android". Update it
when TestFlight or store release status changes, in all seven locales.

## 7. Verification checklist before merging anything

- [ ] `python3 tools/build.py` runs clean
- [ ] `python3 tools/check_copy.py` passes (watch for **em dashes** and **locale key parity**)
- [ ] `python3 tools/check_contrast.py` passes
- [ ] Both `src/` and the regenerated `dist/` are committed
- [ ] Spot-check a non-English page, for example `dist/nl/privacy/index.html`, for unsubstituted
      `{{tokens}}` and for the change actually landing in that locale
- [ ] If privacy copy changed: it says the same thing as
      `Spelletjesapp/docs/STORE_COMPLIANCE.md`, the App Store privacy label and the Play Data
      Safety form

## 8. Cross-repo reference

| Need | Where |
|---|---|
| Full game inventory | `Spelletjesapp/games.md` |
| Privacy and store label rules | `Spelletjesapp/docs/STORE_COMPLIANCE.md` |
| Why Crashlytics, and only Crashlytics | `Spelletjesapp/docs/DECISIONS.md` D25 |
| Design and tone rules, including the no-em-dash rule | `Spelletjesapp/docs/DESIGN_RULES.md` |
| Public summary of the app | `Spelletjesapp/README.md` |

One standing rule worth repeating, because it applies to both repos: **game names are referential
only.** Plain text, no logos, no box art, no characters. The site's existing disclaimer covers this
and should stay on any page that names a game.
