---
title: "Board Game Score Sheets and Playable Boards"
slug: board-game-score-sheets
locale: en
type: pillar
category: board
meta_title: "Board Game Score Sheets and Playable Boards"
meta_description: "How to keep score for board games like Dominoes, Backgammon, Rummikub and Chess, plus which boards you can play on your phone. Local first, no account."
primary_keyword: "board game score sheet"
secondary_keywords:
  - "board game scorekeeper app"
  - "how to keep score in board games"
  - "play board games on phone"
  - "two player board games app"
  - "board game score tracker"
search_intent: informational
priority: 1
schema:
  - Article
  - FAQPage
  - ItemList
internal_links:
  - /games/
  - /blog/how-to-score-dominoes/
  - /blog/how-to-score-backgammon/
  - /blog/how-to-score-rummikub/
  - /blog/card-game-score-sheets/
  - /blog/dice-game-score-sheets/
  - /blog/puzzle-games/
trademark_note: "Rummikub, Cluedo and Connect Four are the trademarks of their respective publishers. Braggster is not affiliated with or endorsed by them and each name is used referentially only."
---

# Board Game Score Sheets and Playable Boards

Board games split into two awkward groups when it comes to scoring. Some produce a running number
every round, like Dominoes and Rummikub, and want a real calculating sheet. Others produce nothing
at all inside a single game: Chess and Tic Tac Toe just end, and what you actually want tracked is
the tally across the evening.

Braggster handles both, and for ten board games it also gives you the board itself.

## Games that score a number

**Dominoes** races to a target, 100 in Block and Draw, 150 in All Fives, off the pips your opponents
are left holding. All Fives adds scoring during play whenever the open ends total a multiple of five,
which is where a paper sheet usually starts to drift.

**Rummikub** is tile rummy: you score the tiles still on your rack at the end of a round, as a
negative, with the winner collecting the rest. Big swings, lots of arithmetic, and a classic case for
a scorecard that adds up for you.

**Cluedo** is the odd one out. It is deduction, not scoring, so Braggster gives it a private detective
notepad instead of a scorecard: one column for the solution envelope and one for free text notes,
across all 21 cards. There are no per opponent columns, because the app never deals or sees anyone's
hand. It is your notepad, on your device.

Deep dives: [Dominoes scoring](/blog/how-to-score-dominoes/),
[Rummikub scoring](/blog/how-to-score-rummikub/).

## Games with no score inside one game

Chess, Checkers, International draughts, Connect Four and Tic Tac Toe have exactly one outcome per
game: someone wins, or it is a draw. There is no number to write down.

Braggster treats a finished game as a round worth one win, so the match becomes a session tally.
That matches how people actually play these: not one game, but a run of them, and the interesting
number is 5 to 3, not the position on the board.

Backgammon sits between the two. A finished game is worth 1 for a single win, 2 for a gammon and 3
for a backgammon, and those points accumulate as a running tally.

Deep dive: [Backgammon scoring, gammons and backgammons](/blog/how-to-score-backgammon/).

## Boards you can actually play on the phone

Ten board games in Braggster are playable on the device, not just scored:

| Game | What the in app board is |
|---|---|
| Chess | Hotseat 8x8 board with full legal move enforcement: check, checkmate, stalemate, castling, en passant, promotion |
| Checkers | Hotseat 8x8 board, American and English rules, forced and multi jump captures |
| International draughts | Hotseat 10x10 board, flying kings, compulsory maximum capture, tapped out square by square |
| Backgammon | Hotseat board: roll, tap to move, hit blots, re-enter and bear off |
| Dominoes | Hotseat tile board: place on the matching open end, draw or pass per variant |
| Connect Four | Hotseat 7x6 board, tap a column and gravity picks the row |
| Tic Tac Toe | Hotseat 3x3 grid with auto win and draw detection |
| Sudoku | Generated puzzle grid, five difficulty tiers |

Every one of these commits its result through the same round path as a hand entered sheet, so a game
you played in the app can never score differently from one you keyed in.

## Playing against the computer

Four of the board games also have a practice screen against a computer opponent, each with three
levels:

- **Chess** uses an alpha beta search with piece square evaluation. You can play White or Black,
  and the board flips to suit.
- **Checkers** searches multi jump chains as the single turn they are.
- **International draughts** does the same over the 10x10 board, where a whole capture sequence is
  one move.
- **Backgammon** cannot use alpha beta at all, because the dice make every node a chance node. It
  runs an expectimax over the twenty one distinct rolls instead.

All four run on a background thread so the board stays responsive while the engine thinks. Practice
games are never recorded, so they do not pollute your statistics or your win rate.

## Accessibility built in, not bolted on

Every board in Braggster tells pieces apart by shape as well as colour. Connect Four uses a solid
disc against a ring with a centre dot rather than red against yellow, because colour is never the
only signal in the app. Boards from 12x12 upward use pinch to zoom and pan rather than shrinking
cells below a comfortable tap target.

## Frequently asked questions

**Can two people play on one phone?**
Yes. The playable boards are hotseat, or pass and play: you hand the device across the table. There
is no online multiplayer and no account.

**Does the app work for a board game that is not in the list?**
Yes. The always free Blank scorecard keeps score for anything, and there is a generic board game
scorecard for untracked titles.

**Do computer games count towards my statistics?**
No. Practice games against the computer are deliberately never recorded.

**Is there a doubling cube in Backgammon?**
No. There is no doubling cube and nothing is staked anywhere in the app.

**Why is Sudoku listed as a board game on some pages?**
It should not be. Sudoku belongs with the puzzles, along with the eleven other single player puzzles
Braggster now ships. See the [puzzle guide](/blog/puzzle-games/).

---

**Next:** browse the full catalogue at [braggster.com/games](/games/), or read the companion guides
for [card games](/blog/card-game-score-sheets/), [dice games](/blog/dice-game-score-sheets/) and
[puzzles](/blog/puzzle-games/).
