---
title: "Backgammon Scoring: Singles, Gammons and Backgammons"
slug: how-to-score-backgammon
locale: en
type: game
category: board
game_id: backgammon
meta_title: "Backgammon Scoring: Singles, Gammons, Backgammons"
meta_description: "What a backgammon win is worth: 1 for a single, 2 for a gammon, 3 for a backgammon. Plus a playable board and a computer opponent that runs expectimax."
primary_keyword: "backgammon scoring"
secondary_keywords:
  - "what is a gammon in backgammon"
  - "backgammon rules"
  - "play backgammon offline"
  - "backgammon match scoring"
  - "backgammon vs computer"
search_intent: informational
priority: 1
schema:
  - Article
  - FAQPage
  - HowTo
internal_links:
  - /games/
  - /blog/board-game-score-sheets/
  - /blog/dice-game-score-sheets/
trademark_note: null
---

# Backgammon Scoring: Singles, Gammons and Backgammons

Backgammon is the oldest game in Braggster's catalogue by a wide margin, and it has the cleanest
scoring system of any of them. Three outcomes, three values, and the whole difference between a
casual win and a crushing one lives in whether your opponent got a checker home.

## The three results

| Result | Worth | Condition |
|---|---|---|
| **Single** | 1 point | The loser has borne off at least one checker |
| **Gammon** | 2 points | The loser has borne off none |
| **Backgammon** | 3 points | The loser has borne off none, and still has a checker in the winner's home board or on the bar |

That is the entire scoring system. Points accumulate across games as a running tally and the highest
total leads.

The gammon rule is what gives backgammon its endgame tension. A player who is clearly losing is not
playing to win any more, they are playing to bear off **one single checker** before their opponent
finishes, because that halves the damage. Watching someone race a lone checker home to save a gammon
is one of the more genuinely dramatic things in board games.

## Why there is no cube here

Serious backgammon uses a doubling cube, which multiplies the stake mid game and can be redoubled.
Braggster has no doubling cube, and this is deliberate: nothing anywhere in the app records a stake.
The score is the result of the game, 1, 2 or 3, and that is all.

If you play with a cube at home, record the result of each game and keep the cube on the board.

## The basics of play

Each side has fifteen checkers moving in opposite directions around twenty four points, aiming to get
them all into their own home board and then bear them off.

- Roll two dice and move two checkers, or one checker twice.
- **Doubles play four times**, not twice.
- A point held by two or more of your opponent's checkers is closed to you.
- A lone checker is a **blot**. Land on it and it goes to the bar, and it has to re-enter in the
  opponent's home board before that player can move anything else.
- Once all fifteen are home, you start bearing off.

## The playable board

Braggster's Backgammon includes a hotseat board: roll the two dice, tap a checker and then a
highlighted point to move it, hit blots to the bar, re-enter, and bear off. The finished game scores
straight into the running tally, so a game played on the phone can never score differently from one
recorded by hand.

Two openings are supported:

- **Standard**, the normal starting position.
- **Nackgammon**, which moves two checkers back to make the early game less racing and more
  positional.

## The computer opponent, and why it is different

Backgammon has a practice screen against the computer with three levels, playing as Light or Dark.

What is worth knowing is that it cannot work the way the other engines in Braggster do. Chess,
Checkers and International draughts all use alpha beta search, which relies on the game being
deterministic: you know exactly which positions are reachable from here.

Backgammon has dice. Every node in the tree is a chance node, with twenty one distinct rolls to
consider. So the backgammon engine runs an **expectimax** search instead, averaging over those rolls
rather than assuming the opponent picks the worst one for you. It runs on a background thread so the
board stays responsive while it thinks.

Practice games are never recorded, so playing the computer does not touch your statistics.

## Frequently asked questions

**How many points is a gammon worth?**
2 points. A single is 1 and a backgammon is 3.

**What is the difference between a gammon and a backgammon?**
Both require the loser to have borne off nothing. It is a backgammon only if the loser still has a
checker on the bar or in the winner's home board when the game ends.

**Do doubles move four times in backgammon?**
Yes. Rolling 5-5 gives you four moves of five, not two.

**Is there a doubling cube in the app?**
No. Braggster records the game result only, with no stake anywhere in the app.

**Can I play backgammon offline against the computer?**
Yes. The engine runs entirely on your device, no connection and no account required.

**What is Nackgammon?**
A variant starting position that pulls two checkers further back, making the opening more positional
and less of a straight race. Braggster supports it alongside the standard opening.

---

**More:** browse every game at [braggster.com/games](/games/), or read the overview of
[board game scoring](/blog/board-game-score-sheets/).
