---
title: "13 Logic Puzzles in One App, All Generated and All Solvable"
slug: puzzle-games
locale: en
type: pillar
category: puzzle
meta_title: "13 Logic Puzzles in One App, Endless and Solvable"
meta_description: "Sudoku, Killer Sudoku, Kakuro, Nonogram, Minesweeper, Futoshiki, Binairo and more. Every puzzle generated fresh and verified to have one solution."
primary_keyword: "logic puzzle app"
secondary_keywords:
  - "offline puzzle games app"
  - "sudoku and kakuro app"
  - "nonogram app"
  - "unique solution puzzle generator"
  - "puzzle games no ads"
search_intent: informational
priority: 1
schema:
  - Article
  - FAQPage
  - ItemList
internal_links:
  - /games/
  - /blog/how-to-play-sudoku/
  - /blog/how-to-play-killer-sudoku/
  - /blog/how-to-play-minesweeper/
  - /blog/how-to-play-murder-sudoku/
  - /blog/card-game-score-sheets/
  - /blog/board-game-score-sheets/
  - /blog/dice-game-score-sheets/
trademark_note: null
---

# 13 Logic Puzzles in One App, All Generated and All Solvable

Most puzzle apps ship a bank of puzzles and eventually run out. Braggster generates every puzzle
fresh on demand and then proves it has exactly one solution before showing it to you. That second
half is the part almost nobody does, and it is the difference between a puzzle you can reason your
way through and one where you eventually have to guess.

Here are the thirteen, what each one actually asks of you, and how they are scored.

## The number placement family

**Sudoku.** The classic 9x9. Every row, column and 3x3 box holds 1 to 9 exactly once. Five tiers,
Beginner through Evil, and the tier genuinely changes the solving technique required: Beginner and
Easy are solvable with singles alone, the harder tiers are not.

**Killer Sudoku.** Sudoku's grid plus a partition of the 81 cells into cages, each with a printed
sum. Every cage's digits are distinct and add to that sum. Killer puzzles typically start with few
givens or none at all, because the cages carry the constraint instead.

**Kakuro.** The cross sum puzzle. Every run of white cells holds distinct digits 1 to 9 adding up to
the clue at its head. Grids run 6x6 up to 10x10.

**Calcudoku.** A Latin square with arithmetic cages: every row and column holds 1 to N once, and each
heavy bordered cage combines to a target under a printed operator. Digits may repeat inside a cage,
because a cage is a freeform shape rather than a row or a box.

**Futoshiki.** A Latin square with inequality signs between adjacent cells, drawn so the vertex
always points at the smaller value. 4x4 up to 7x7.

**Binairo.** Also called Takuzu or simply the binary puzzle. Two symbols, 0 and 1. No three identical
symbols in a row or column, exactly half of each per line, and no two identical rows or columns.
6x6 up to 12x12, always even. Tap a cell to cycle it through empty, 0 and 1: with two symbols there
is no number pad to get in the way.

Deep dives: [Sudoku](/blog/how-to-play-sudoku/), [Killer Sudoku](/blog/how-to-play-killer-sudoku/).

## The grid deduction family

**Minesweeper.** Five tiers from 9x9 with 10 mines up to 16x30 with 99. Every field is proven
solvable start to finish by pure logic before you ever see it, from a guaranteed safe opening region.
No guessing, ever. And revealing a mine does not end the game: it counts one silent mistake and play
continues, matching how Sudoku counts a wrong digit.

**Nonogram.** Picture logic. Row and column clues give the run lengths of filled cells, and the
finished grid is a picture with a title. Difficulty scales the grid rather than the technique,
5x5 up to 15x15, because a nonogram's difficulty is really picture complexity.

**Logikwis.** The classic logic grid puzzle: N subjects and K categories that pair up one to one,
solved on a cross reference elimination grid from a handful of clues. Each case draws a random theme
from people, ships, cafes, planets, trains or islands, and a random subset of twelve categories, so
you are not solving person plus colour plus pet plus drink for the hundredth time.

**Murder Sudoku.** A whodunnit crossed with a placement puzzle on a 5x5 room grid. Place four
suspects and a victim so at most one person sits in each row and column, satisfy every clue, and the
killer is whoever ends up sharing the victim's room. Every case comes wrapped in a full puzzle book
story: a scene, a named cast, a briefing and a numbered clue list.

Deep dives: [Minesweeper](/blog/how-to-play-minesweeper/),
[Murder Sudoku](/blog/how-to-play-murder-sudoku/).

## The word family

**Woordkraker.** Wordle style word guessing with an on screen keyboard. Six tries, four length tiers
from 4 to 7 letters. Letter states are never signalled by colour alone: right spot is a solid tile
with a bar, in the word elsewhere is a ring with a dot, absent is struck through.

**Kruiswoord.** A crossword generated at runtime from a large clued word dictionary rather than a
shipped bank, so the puzzles are unlimited. Mini 5x5, Midi 7x7 and Standard 15x15.

**Woordzoeker.** Word search. Words run in any of eight directions, forwards or backwards, and you
find one by dragging from its first letter to its last. 8x8 with 5 words up to 14x14 with 12.

## How puzzles are scored

Every puzzle scores the same way, and it is the opposite of the rest of the app: **lowest total
wins.** Your score is your solve time plus a penalty for each mistake and each hint. Fast and clean
beats slow and assisted.

There is one deliberate design choice worth flagging. **There is no live wrong entry feedback.**
Put a wrong digit in and the app will not flash it red at you. Mistakes are counted silently and
revealed in the solve summary at the end. A puzzle that tells you immediately when you are wrong is
not really a logic puzzle any more, it is a guessing game with a validator.

Assists are pencil notes and hints only, depending on the puzzle.

## Why unique solutions matter

Every generated puzzle in Braggster is put through a solver before it reaches you:

- Sudoku, Kakuro, Futoshiki, Binairo and Calcudoku are checked by backtracking solvers that confirm
  exactly one completion exists.
- Killer Sudoku is verified under the combined Sudoku and cage constraint together, not each in
  isolation.
- Minesweeper goes further and proves the field is solvable by pure deduction from the opening
  region, reseeding boards that fail.
- Nonograms come from a curated bank of hand authored pictures, each verified against its own clues
  by a line solver plus bounded search.
- Logikwis and Murder Sudoku verify their case has one consistent assignment before writing the
  briefing.

The practical effect: if you are stuck, there is always a next deduction. You are never being asked
to guess and check.

## Frequently asked questions

**Do the puzzles run out?**
No. Everything except Nonogram is generated fresh on demand, so the supply is unlimited. Nonogram
draws from a curated bank of hand authored pictures because a random bitmap is not a good picture.

**Do they work offline?**
Yes. Generation happens on the device, so there is nothing to download and no connection required.

**Are there ads or timers pressuring me?**
No ads anywhere in the app. The timer feeds your score, but nothing expires and nothing interrupts.

**Which puzzles are available in my language?**
Sudoku and Logikwis are in all seven app languages. The word puzzles are language specific by
nature, and each now ships its own word and clue lists in all seven.

**Can I play with pencil notes?**
Yes, on the number grid puzzles. Binairo and Nonogram use a two state cell grammar instead, which is
the natural fit for a two symbol puzzle.

---

**Next:** browse the full catalogue at [braggster.com/games](/games/), or read the companion guides
for [card games](/blog/card-game-score-sheets/), [board games](/blog/board-game-score-sheets/) and
[dice games](/blog/dice-game-score-sheets/).
