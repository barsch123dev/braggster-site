---
title: "Killer Sudoku: How to Solve Cages Without Guessing"
slug: how-to-play-killer-sudoku
locale: en
type: game
category: puzzle
game_id: killersudoku
meta_title: "Killer Sudoku: How to Solve Cages Without Guessing"
meta_description: "Killer Sudoku strategy: the rule of 45, forced cage combinations, and the sum tables worth memorising. Endless generated puzzles, offline and ad free."
primary_keyword: "killer sudoku strategy"
secondary_keywords:
  - "killer sudoku rules"
  - "rule of 45 killer sudoku"
  - "killer sudoku cage combinations"
  - "killer sudoku app offline"
  - "sum sudoku how to play"
search_intent: informational
priority: 1
schema:
  - Article
  - FAQPage
  - HowTo
internal_links:
  - /games/
  - /blog/puzzle-games/
  - /blog/how-to-play-sudoku/
trademark_note: null
---

# Killer Sudoku: How to Solve Cages Without Guessing

Killer Sudoku looks like Sudoku with extra decoration and plays like a completely different puzzle.
Most grids start with **very few givens, or none at all**, which is alarming the first time you see
one. The information is all there. It is just written as sums instead of digits.

## The rules

1. Every row, column and 3x3 box holds 1 to 9 exactly once. Standard Sudoku.
2. The 81 cells are partitioned into **cages**, drawn with dashed borders and a small sum in the
   corner.
3. Every cage's digits are **distinct** and **add up to its sum**.

That third rule is doing an enormous amount of work, because a cage is a freeform shape rather than a
row or a box, so distinctness is not automatic the way it is in plain Sudoku. It has to be imposed,
and it is what makes the sums informative.

## Start with the forced cages

Some sums have exactly one possible combination. These are free information and should be your first
pass over any grid.

| Cage size | Sum | Only possible digits |
|---|---|---|
| 2 cells | 3 | 1, 2 |
| 2 cells | 4 | 1, 3 |
| 2 cells | 16 | 7, 9 |
| 2 cells | 17 | 8, 9 |
| 3 cells | 6 | 1, 2, 3 |
| 3 cells | 7 | 1, 2, 4 |
| 3 cells | 23 | 6, 8, 9 |
| 3 cells | 24 | 7, 8, 9 |
| 4 cells | 10 | 1, 2, 3, 4 |
| 4 cells | 11 | 1, 2, 3, 5 |
| 4 cells | 29 | 5, 7, 8, 9 |
| 4 cells | 30 | 6, 7, 8, 9 |

You do not know the order yet, but you know the set, and knowing the set eliminates candidates
everywhere those cells look.

## The rule of 45

The single most useful technique in Killer Sudoku, and the reason experienced solvers open grids that
look impossible.

Every row, column and box contains 1 through 9, so it **sums to 45**.

If a set of cages fits entirely inside one row, add their sums. The difference from 45 is the total
of whatever cells are left over in that row. When exactly one cell is left over, you have just solved
it outright.

The same works in reverse: if a cage sticks one cell out of a box, the sum of the cages inside the
box minus 45 gives you that one cell's value.

Chain this across two or three rows at once and the technique is sometimes called the "innie and
outie" method. It is the workhorse of hard Killer grids.

## Cage geometry matters

Because a cage's digits are distinct, its shape restricts it further:

- A cage inside a single row, column or box can never repeat, and neither can the unit, so nothing
  new. But a cage **spanning two boxes** can tell you which box a digit lives in.
- A two cell cage summing to 17 must be 8 and 9. If it lies in one row, that row's 8 and 9 are placed
  and every other cell in the row loses both candidates.

## How Braggster generates them

The generator grows a cage partition off a complete Sudoku solution, and does it **digit aware**,
because a freeform cage is not automatically distinct the way a row, column or box is. Growing cages
blindly would produce cages with repeats, which is not a legal Killer cage.

It then verifies uniqueness under the **combined** Sudoku and cage constraint together, using a cage
aware backtracking solver. Checking the two constraints separately would not do: a grid can be
ambiguous under Sudoku alone and unique once the cages are applied, and the reverse.

If a sparse attempt cannot be proven unique inside the search budget, the generator falls back to
Sudoku's already verified given set for the tier. The consequence is that **every puzzle you are
dealt is genuinely uniquely solvable**, never a maybe.

## The board

The Killer board reuses Sudoku's grid anatomy and adds a cage layer: five tints, dashed cage borders
and a corner sum label. Five tints is enough for adjacent cages to always differ without the grid
turning into a colour chart.

Assists are pencil notes and hints. There is no live wrong entry feedback anywhere in Braggster's
puzzles, so mistakes are counted silently and revealed in the solve summary. Scoring is solve time
plus a penalty per mistake and hint, lowest wins.

## Frequently asked questions

**Can digits repeat inside a Killer Sudoku cage?**
No. Cage digits must be distinct, which is what makes the sums useful. This is the opposite of
Calcudoku, where cage digits may repeat.

**What is the rule of 45?**
Every row, column and box sums to 45. Comparing that against the cages inside a unit reveals the
total of the leftover cells, and often solves one outright.

**Why do Killer Sudoku puzzles have so few given numbers?**
The cages carry the constraint instead. A well constructed Killer grid can start with zero givens and
still have exactly one solution.

**Is Killer Sudoku harder than regular Sudoku?**
Different rather than strictly harder. It requires arithmetic alongside the logic, but the cage sums
provide information a plain grid does not have.

**Do the puzzles repeat?**
No. They are generated fresh on demand and verified unique before they are shown.

---

**More:** see all thirteen [logic puzzles](/blog/puzzle-games/), read about
[Sudoku difficulty](/blog/how-to-play-sudoku/), or browse the catalogue at
[braggster.com/games](/games/).
