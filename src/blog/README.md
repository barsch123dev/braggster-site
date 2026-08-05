# The blog

Eighteen articles, seven languages, 126 markdown files. They exist to give the site something to
rank for besides the home page: before this, `/games/` was the only URL that could answer any game
query, and it is one list page carrying the whole catalogue.

## Structure

Four **category pillars** and fourteen **per-game articles**, hub and spoke. Each spoke links up to
its pillar and out to `/games/`; each pillar links down to its spokes and across to the other three.

| Pillar | Spokes |
|---|---|
| `card-game-score-sheets` | Klaverjassen, Hearts, Bridge, Solitaire, Pesten |
| `board-game-score-sheets` | Dominoes, Backgammon, Rummikub |
| `dice-game-score-sheets` | Yahtzee, Dudo |
| `puzzle-games` | Sudoku, Killer Sudoku, Minesweeper, Murder Sudoku |

Per-game articles were picked on search demand against how much the app actually does, not one per
game. A game that only gets a plain scorecard has nothing to say that would outrank the established
rules sites. Every one of the fourteen either has a genuinely fiddly scoring system worth explaining
(the boompje, the Joker rule, All Fives, bridge vulnerability) or a real in-app feature to talk about
(Hearts against the computer, the Klondike board, the no-guess Minesweeper generator).

## How a file becomes a page

`src/blog/<locale>/<slug>.md` renders to `/<locale>/blog/<slug>/`. The index is `/<locale>/blog/`.

Slugs are **English in every locale**, and the `slug:` field must match the filename. One slug per
article across all seven languages keeps hreflang, the renderer and the cross-links simple, and the
slug is a minor ranking factor next to the title and the body.

`tools/build.py` holds the renderer. It is a small closed subset of markdown rather than a library,
because this repo has no dependencies and adding one for eighteen articles would be the largest
thing in it. It handles ATX headings, paragraphs, bold, inline code, links, pipe tables, both list
kinds and rules, and raises on anything it does not recognise so an unsupported construct fails the
build instead of rendering as literal text.

Two things worth knowing before editing an article:

- **The H1 comes from the body, and the build asserts it equals `title:`.** They cannot drift.
- **Links are written as absolute site paths** (`/games/`, `/blog/<slug>/`) and rewritten to the
  right relative prefix per locale at build time. Do not hand-write `../../`.

## Front matter

```yaml
title:               # H1 and og:title. Must equal the `# ` heading in the body
slug:                # URL segment; must equal the filename
locale:              # this file's locale code
type:                # pillar | game
category:            # card | board | dice | puzzle
game_id:             # matches an id in src/games.json, per-game articles only
meta_title:          # <title>, 60 characters or fewer
meta_description:    # <meta name="description">, 110 to 160 characters
primary_keyword:     # the single term this page is built to rank for
secondary_keywords:  # supporting terms, used in the H2s and the body
search_intent:       # informational | transactional
priority:            # 1 publish first, 2 second
schema:              # JSON-LD types
internal_links:      # every in-site link the article makes
trademark_note:      # rendered as a footer disclaimer, or null
```

Every article closes with an FAQ section. That is not decoration: `faq_pairs()` in `build.py` lifts
those question and answer pairs into `FAQPage` JSON-LD, which is what wins the "People also ask"
style result for a rules or scoring query. A question is recognised by shape, a fully bold line
ending in a question mark, so it works in all seven languages without a per-locale marker. Every
article also emits `Article` and `BreadcrumbList`; the index emits `ItemList`.

## Rules

- **No em dashes and no en dashes**, anywhere, including front matter. `tools/check_copy.py` gates it.
- **No wagering vocabulary.** Nothing says bet, stake, chip, pot, ante or payout except in the
  sentences that state the app has none of them. That is a real differentiator on the Poker,
  Blackjack, Dudo and Backgammon queries, so the articles say it plainly rather than dodging it.
- **Game names are proper nouns and are not translated**, matching `src/games.json`. The exceptions
  are names with an established local equivalent that is what people actually search: Buscaminas,
  Démineur and Campo Minado for Minesweeper, Gamão for Backgammon, Paciência for Solitaire, Kniffel
  and Yams for Yahtzee. `games.json` carries those as tags, so `/games/` still bridges the two.
- **Keywords are re-targeted per language, not translated.** The Dutch Klaverjassen article aims at
  "klaverjassen puntentelling", the German Yahtzee article at "kniffel punkte". A literal rendering
  of the English phrase is almost never what anyone types.
- **Feature claims are checked against the app.** The articles were written from the game inventory
  in the app repo, so nothing here promises something the scorecard does not do.

`TRANSLATION-BRIEF.md` in this directory is the full brief handed to translators.

## Backlog

Not written yet, ranked by expected value. All are viable; none were dropped for lack of material.

**Sports wave.** The category the first batch skipped, and several of these have stronger
informational demand than anything already published: bowling (the frame bonus is genuinely
confusing and the app implements it properly), darts (checkout tables are highly linkable), tennis,
padel, table tennis, kegelen, midgetgolf.

**Remaining puzzles.** Kakuro, Nonogram, Futoshiki, Binairo, Calcudoku. Plus Logikwis, Woordkraker,
Kruiswoord and Woordzoeker, which are better written directly in Dutch and English than translated,
since the puzzles are language specific.

**Regional card games.** Skat, Belote, Briscola, Scopa, Truco, Canasta, Spades, Euchre, Whist, Jass,
Toepen, Jokeren, Bollen, Cuarenta, Loteria, Burro, Mus, Doppelkopf, Schnapsen, Twenty-Five, 500, All
Fours, Königrufen. Individually small, collectively the reason a 33 game card catalogue exists. The
right approach is one article per game **in its own market's language first**, Skat in German,
Belote in French, Briscola in Italian, Truco in Portuguese and Spanish, rather than English first
and translated.

**Comparison and feature pages.** Not game specific but stronger commercial intent: an offline
score keeping comparison, the local-first privacy angle, running a game night tournament across
several games.

## Known gap

`/games/` has **no per-game anchors**. The only ids on it are the filter inputs, and because the
filter is a CSS `:has(:checked)` trick a fragment link does not even apply the filter, so an article
cannot deep link to the game it is about and every one of them links to the catalogue page plainly.

The cheap fix is an `id` per game card. The fix worth making is a real `/games/<id>/` page per game,
which would turn 66 list entries into 66 indexable URLs and give all 126 of these articles something
specific to point at.
