---
title: "Sudoku Difficulty, Explained: What Actually Makes One Hard"
slug: how-to-play-sudoku
locale: en
type: game
category: puzzle
game_id: sudoku
meta_title: "Sudoku Difficulty Explained: What Makes One Hard"
meta_description: "Why the number of givens does not set Sudoku difficulty, which techniques each tier needs, and how every puzzle is proven to have one solution. No ads."
primary_keyword: "sudoku difficulty levels"
secondary_keywords:
  - "sudoku solving techniques"
  - "offline sudoku app no ads"
  - "sudoku unique solution"
  - "how to get better at sudoku"
  - "sudoku pencil marks"
search_intent: informational
priority: 1
schema:
  - Article
  - FAQPage
  - HowTo
internal_links:
  - /games/
  - /blog/puzzle-games/
  - /blog/how-to-play-killer-sudoku/
trademark_note: null
---

# Sudoku Difficulty, Explained: What Actually Makes One Hard

Most people assume a Sudoku with fewer starting numbers is harder. It is a reasonable guess and it is
wrong often enough to be worth correcting, because it leads people to the wrong practice.

Difficulty in Sudoku is not about how many givens there are. It is about **which solving technique
you are forced to use** before the grid opens up.

## The rule, in one line

Every row, every column and every 3x3 box holds the digits 1 to 9 exactly once. That is the whole
game.

## The technique ladder

Sudoku solving techniques form a ladder, and a puzzle's real difficulty is the highest rung you have
to climb.

**Naked single.** A cell where only one digit is possible, because the other eight appear in its row,
column or box. Scan for these first, always.

**Hidden single.** A digit that can only go in one cell of a row, column or box, even though that
cell has several candidates of its own. Beginners miss these constantly, because they look at cells
rather than at digits.

Those two alone solve an enormous number of published puzzles. In Braggster, **Beginner and Easy are
guaranteed solvable with singles alone**, which is exactly what makes them a good place to build
speed.

**Naked and hidden pairs.** Two cells in a unit sharing exactly two candidates: those two digits
belong to those two cells, so they can be eliminated everywhere else in the unit. Triples work the
same way with three.

**Pointing and claiming.** If a digit in a box is confined to one row, it can be eliminated from the
rest of that row outside the box. And the reverse.

**X-Wing and beyond.** Patterns that span multiple units at once. This is where puzzles stop being a
grind and start being interesting, and where Braggster's Hard and Evil tiers live.

## Why "fewer givens" is a bad proxy

A grid with 24 givens arranged helpfully can be a singles-only walk. A grid with 30 givens arranged
awkwardly can require pairs and pointing. The count tells you almost nothing on its own.

This is why Braggster grades by technique rather than by given count. The chosen variant is stored on
the match, and the generator deals a puzzle graded to it.

| Tier | What it requires |
|---|---|
| Beginner | Naked and hidden singles only |
| Easy | Naked and hidden singles only |
| Medium | Pairs and box line interactions |
| Hard | Multiple advanced techniques |
| Evil | Sustained advanced technique |

## Every puzzle has exactly one solution

The generator is pure and seeded, and it verifies that each puzzle it deals has a **unique solution**
before you see it.

This matters more than it sounds. A puzzle with two solutions is not a logic puzzle, it is a
guessing exercise dressed as one, and you will hit a point where no deduction is available and both
branches are legal. If you have ever been stuck on a puzzle from a cheap book and eventually
discovered your answer was "also right", that is what happened.

Because generation runs on your device, the supply is unlimited and works entirely offline.

## No wrong entry feedback, on purpose

Braggster will not flash a digit red when you place it wrongly.

This is a deliberate design decision, and it applies across all thirteen puzzles in the app. Live
error feedback turns a logic puzzle into a validator game: you stop deducing and start probing,
because the app will tell you if you are wrong. Take that away and you have to actually be sure.

Mistakes are counted silently and revealed in the solve summary at the end, so you find out how clean
your solve was without being nannied through it.

Assists available: **pencil notes and hints.** Nothing else.

## How a solve is scored

Your score is **solve time plus a penalty for each mistake and each hint**, and lowest wins. Fast and
unassisted beats slow and hint heavy, and a fast solve with four mistakes may well lose to a slower
clean one.

Solves land in the same statistics as every other game in the app, so your Sudoku record sits
alongside your card and board game records rather than in a separate silo.

## Frequently asked questions

**What is the hardest Sudoku difficulty in Braggster?**
Evil, the fifth tier. Beginner and Easy are solvable with singles alone, Medium introduces pairs, and
Hard and Evil require sustained advanced technique.

**Does the app tell me when I make a mistake?**
Not while you play. Mistakes are counted silently and shown in the solve summary. This is deliberate
across every puzzle in the app.

**Can I use pencil marks?**
Yes. Pencil notes and hints are the two assists.

**Do the puzzles ever repeat?**
No. They are generated fresh on demand from a seeded generator rather than drawn from a shipped bank,
so the supply is unlimited.

**Does Sudoku work offline?**
Yes, entirely. Generation happens on your device.

**How is my Sudoku score calculated?**
Solve time plus a penalty per mistake and per hint. Lowest total wins, which is the opposite of most
games in the app.

---

**More:** see all thirteen [logic puzzles](/blog/puzzle-games/), try
[Killer Sudoku](/blog/how-to-play-killer-sudoku/), or browse the catalogue at
[braggster.com/games](/games/).
