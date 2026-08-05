---
title: "Backgammon Regeln: Einfache Siege, Gammons und Backgammons"
slug: how-to-score-backgammon
locale: de
type: game
category: board
game_id: backgammon
meta_title: "Backgammon Regeln: Punkte, Gammon, Backgammon"
meta_description: "Was ein Backgammon Sieg wert ist: 1 Punkt für einfachen Sieg, 2 für ein Gammon, 3 für Backgammon. Dazu ein spielbares Brett und ein KI Gegner mit Expectimax."
primary_keyword: "backgammon regeln"
secondary_keywords:
  - "was ist ein gammon backgammon"
  - "backgammon punkte"
  - "backgammon offline spielen"
  - "backgammon gegen computer"
  - "backgammon spielanleitung"
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

# Backgammon Regeln: Einfache Siege, Gammons und Backgammons

Backgammon ist mit weitem Abstand das älteste Spiel im Braggster Katalog, und es hat das klarste
Wertungssystem von allen. Drei Ergebnisse, drei Werte, und der ganze Unterschied zwischen einem
lockeren Sieg und einem vernichtenden liegt darin, ob dein Gegner überhaupt einen Stein nach Hause
gebracht hat.

## Die drei Ergebnisse

| Ergebnis | Wert | Bedingung |
|---|---|---|
| **Einfacher Sieg** | 1 Punkt | Der Verlierer hat mindestens einen Stein ausgetragen |
| **Gammon** | 2 Punkte | Der Verlierer hat keinen Stein ausgetragen |
| **Backgammon** | 3 Punkte | Der Verlierer hat keinen Stein ausgetragen und hat noch einen Stein im Heimfeld des Gewinners oder auf der Bar |

Das ist das komplette Wertungssystem. Punkte sammeln sich über mehrere Partien als laufende Summe, und
die höchste Summe führt.

Die Gammon Regel ist es, die dem Spiel seine Endphasen-Spannung gibt. Ein Spieler, der klar verliert,
spielt nicht mehr auf Sieg, sondern darauf, **einen einzigen Stein** auszutragen, bevor der Gegner
fertig ist, weil das den Schaden halbiert. Zuzusehen, wie jemand einen einzelnen Stein nach Hause
jagt, um ein Gammon zu vermeiden, gehört zu den wirklich dramatischen Momenten in Brettspielen.

## Warum es hier keinen Dopplerwürfel gibt

Ernsthaftes Backgammon nutzt einen Dopplerwürfel, der den Einsatz mitten in der Partie vervielfacht
und erneut verdoppelt werden kann. Braggster hat keinen Dopplerwürfel, und das ist Absicht: Nirgendwo
in der App wird ein Einsatz gespeichert. Der Punktestand ist das Ergebnis der Partie, 1, 2 oder 3,
und mehr nicht.

Spielst du zu Hause mit Dopplerwürfel, notier einfach das Ergebnis jeder Partie und behalte den Würfel
auf dem Brett.

## Die Grundlagen des Spiels

Jede Seite hat fünfzehn Steine, die in entgegengesetzter Richtung über vierundzwanzig Punkte laufen,
mit dem Ziel, alle ins eigene Heimfeld zu bringen und dann auszutragen.

- Würfle zwei Würfel und bewege zwei Steine, oder einen Stein zweimal.
- **Ein Pasch zählt vierfach**, nicht zweifach.
- Ein Punkt mit zwei oder mehr Steinen des Gegners ist für dich gesperrt.
- Ein einzelner Stein ist ein **Blot**. Landest du darauf, geht er auf die Bar und muss im Heimfeld des
  Gegners wieder einlaufen, bevor der etwas anderes ziehen darf.
- Sind alle fünfzehn zu Hause, kannst du mit dem Austragen beginnen.

## Das spielbare Brett

Backgammon in Braggster hat ein Brett zum Weiterreichen am gleichen Gerät: Würfle die zwei Würfel, tipp
auf einen Stein und dann auf ein markiertes Feld, um ihn zu bewegen, triff Blots und schick sie auf die
Bar, lass Steine wieder einlaufen, und trag sie aus. Die fertige Partie fließt direkt in die laufende
Summe ein, sodass eine auf dem Handy gespielte Partie nie anders zählt als eine von Hand eingetragene.

Zwei Startaufstellungen werden unterstützt:

- **Standard**, die normale Startposition.
- **Nackgammon**, bei der zwei Steine weiter zurückgesetzt werden, was das frühe Spiel weniger zum
  Wettlauf und mehr zur Positionsfrage macht.

## Der Computergegner, und warum er anders ist

Backgammon hat einen Übungsbildschirm gegen den Computer mit drei Stufen, wahlweise als Hell oder
Dunkel.

Wissenswert ist, dass er nicht so funktionieren kann wie die anderen Engines in Braggster. Schach,
Dame und Internationales Damespiel nutzen alle eine Alpha-Beta-Suche, die darauf setzt, dass das Spiel
deterministisch ist: Du weißt genau, welche Stellungen von hier aus erreichbar sind.

Backgammon hat Würfel. Jeder Knoten im Suchbaum ist ein Zufallsknoten mit einundzwanzig
unterschiedlichen Würfen zur Auswahl. Deshalb läuft die Backgammon Engine stattdessen mit einer
**Expectimax** Suche, die über diese Würfe mittelt, statt anzunehmen, dass der Gegner immer den für
dich schlechtesten wählt. Sie läuft in einem Hintergrundthread, damit das Brett reaktionsfähig bleibt,
während sie rechnet.

Übungsspiele werden nie gespeichert, sodass ein Spiel gegen den Computer deine Statistik nicht
berührt.

## Häufige Fragen

**Wie viele Punkte ist ein Gammon wert?**
2 Punkte. Ein einfacher Sieg ist 1, ein Backgammon ist 3.

**Was ist der Unterschied zwischen Gammon und Backgammon?**
Bei beiden muss der Verlierer keinen einzigen Stein ausgetragen haben. Es ist nur dann ein Backgammon,
wenn der Verlierer beim Ende der Partie noch einen Stein auf der Bar oder im Heimfeld des Gewinners
hat.

**Zählt ein Pasch bei Backgammon vierfach?**
Ja. Wer 5-5 würfelt, bekommt vier Züge von fünf, nicht zwei.

**Gibt es in der App einen Dopplerwürfel?**
Nein. Braggster speichert nur das Ergebnis der Partie, ohne dass irgendwo in der App ein Einsatz
vorkommt.

**Kann ich Backgammon offline gegen den Computer spielen?**
Ja. Die Engine läuft komplett auf deinem Gerät, ohne Verbindung und ohne Konto.

**Was ist Nackgammon?**
Eine Startaufstellung, bei der zwei Steine weiter zurückgesetzt werden, was die Eröffnung positioneller
und weniger zu einem reinen Wettlauf macht. Braggster unterstützt sie neben der Standardaufstellung.

---

**Mehr:** durchstöbere alle Spiele auf [braggster.com/games](/games/), oder lies den Überblick zur
[Brettspiel Wertung](/blog/board-game-score-sheets/).
