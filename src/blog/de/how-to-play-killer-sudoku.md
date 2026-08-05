---
title: "Killer Sudoku: Käfige lösen, ohne zu raten"
slug: how-to-play-killer-sudoku
locale: de
type: game
category: puzzle
game_id: killersudoku
meta_title: "Killer Sudoku: Käfige lösen ohne zu raten"
meta_description: "Killer Sudoku Strategie: die Regel der 45, erzwungene Käfig-Kombinationen, und Summentabellen zum Merken. Endlos generiert, offline, ohne Werbung."
primary_keyword: "killer sudoku strategie"
secondary_keywords:
  - "killer sudoku regeln"
  - "regel der 45 killer sudoku"
  - "killer sudoku käfig kombinationen"
  - "killer sudoku app offline"
  - "summen sudoku spielen"
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

# Killer Sudoku: Käfige lösen, ohne zu raten

Killer Sudoku sieht aus wie Sudoku mit zusätzlicher Deko und spielt sich wie ein völlig anderes
Rätsel. Die meisten Gitter starten mit **sehr wenigen Vorgaben oder gar keinen**, was beim ersten Mal
beunruhigend wirkt. Die Information ist trotzdem komplett da. Sie steht nur als Summen statt als
Ziffern.

## Die Regeln

1. Jede Zeile, Spalte und jeder 3x3 Block enthält 1 bis 9 genau einmal. Ganz normales Sudoku.
2. Die 81 Zellen sind in **Käfige** eingeteilt, gezeichnet mit gestrichelten Rändern und einer
   kleinen Summe in der Ecke.
3. Die Ziffern jedes Käfigs sind **verschieden** und **ergeben zusammen seine Summe**.

Diese dritte Regel leistet enorm viel, weil ein Käfig eine freiformige Fläche ist statt einer Zeile
oder eines Blocks, Verschiedenheit ist also nicht automatisch gegeben wie im normalen Sudoku. Sie muss
auferlegt werden, und genau das macht die Summen aussagekräftig.

## Beginn mit den erzwungenen Käfigen

Manche Summen haben genau eine mögliche Kombination. Das ist kostenlose Information und sollte dein
erster Durchgang durch jedes Gitter sein.

| Käfiggröße | Summe | Einzig mögliche Ziffern |
|---|---|---|
| 2 Zellen | 3 | 1, 2 |
| 2 Zellen | 4 | 1, 3 |
| 2 Zellen | 16 | 7, 9 |
| 2 Zellen | 17 | 8, 9 |
| 3 Zellen | 6 | 1, 2, 3 |
| 3 Zellen | 7 | 1, 2, 4 |
| 3 Zellen | 23 | 6, 8, 9 |
| 3 Zellen | 24 | 7, 8, 9 |
| 4 Zellen | 10 | 1, 2, 3, 4 |
| 4 Zellen | 11 | 1, 2, 3, 5 |
| 4 Zellen | 29 | 5, 7, 8, 9 |
| 4 Zellen | 30 | 6, 7, 8, 9 |

Du kennst die Reihenfolge noch nicht, aber du kennst die Menge, und das Wissen um die Menge streicht
Kandidaten überall dort, wo diese Zellen hinschauen.

## Die Regel der 45

Die nützlichste Technik in Killer Sudoku, und der Grund, warum erfahrene Löser Gitter öffnen, die
unmöglich aussehen.

Jede Zeile, Spalte und jeder Block enthält 1 bis 9, also **ergibt die Summe 45**.

Passt eine Gruppe von Käfigen komplett in eine Zeile, addier ihre Summen. Die Differenz zu 45 ist die
Summe der übrig gebliebenen Zellen in dieser Zeile. Bleibt genau eine Zelle übrig, hast du sie damit
direkt gelöst.

Das Gleiche funktioniert umgekehrt: Ragt ein Käfig mit einer Zelle aus einem Block heraus, ergibt die
Summe der Käfige im Block minus 45 den Wert genau dieser einen Zelle.

Verkettest du das über zwei oder drei Zeilen gleichzeitig, wird die Technik manchmal die "Innie und
Outie" Methode genannt. Sie ist das Arbeitspferd schwerer Killer Gitter.

## Käfiggeometrie zählt

Weil die Ziffern eines Käfigs verschieden sein müssen, schränkt seine Form ihn weiter ein:

- Ein Käfig innerhalb einer Zeile, Spalte oder eines Blocks kann sich nie wiederholen, aber die
  Einheit auch nicht, also nichts Neues. Aber ein Käfig, der **über zwei Blöcke ragt**, kann dir
  verraten, in welchem Block eine Ziffer liegt.
- Ein Zwei-Zellen-Käfig mit Summe 17 muss 8 und 9 sein. Liegt er in einer Zeile, sind in dieser Zeile
  die 8 und die 9 bereits gesetzt, und jede andere Zelle der Zeile verliert beide Kandidaten.

## Wie Braggster sie generiert

Der Generator lässt eine Käfig-Partition auf einer vollständigen Sudoku-Lösung wachsen, und tut das
**zifferbewusst**, weil ein freiformiger Käfig nicht automatisch verschieden ist wie eine Zeile,
Spalte oder ein Block. Käfige blind wachsen zu lassen, würde Käfige mit Wiederholungen erzeugen, was
kein legaler Killer Käfig ist.

Danach wird die Eindeutigkeit unter der **kombinierten** Sudoku- und Käfig-Bedingung zusammen geprüft,
mit einem käfigbewussten Backtracking-Löser. Die beiden Bedingungen getrennt zu prüfen, würde nicht
reichen: Ein Gitter kann unter Sudoku allein mehrdeutig und mit den Käfigen eindeutig sein, und
umgekehrt.

Kann ein dünn besetzter Versuch innerhalb des Suchbudgets nicht als eindeutig bewiesen werden, fällt
der Generator auf die bereits geprüfte Vorgabenmenge von Sudoku für diese Stufe zurück. Die Folge:
**Jedes Rätsel, das du bekommst, ist wirklich eindeutig lösbar**, nie ein Vielleicht.

## Das Brett

Das Killer Brett übernimmt Sudokus Gitteranatomie und fügt eine Käfig-Ebene hinzu: fünf Farbtöne,
gestrichelte Käfigränder und eine Summenbeschriftung in der Ecke. Fünf Farbtöne reichen, damit
benachbarte Käfige sich immer unterscheiden, ohne dass das Gitter zur Farbtabelle wird.

Hilfen sind Notizen und Hinweise. Es gibt nirgendwo in Braggsters Rätseln sofortige Fehlerrückmeldung,
Fehler werden also still gezählt und in der Lösungszusammenfassung gezeigt. Die Wertung ist
Lösungszeit plus eine Strafe pro Fehler und Hinweis, die niedrigste gewinnt.

## Häufige Fragen

**Können sich Ziffern in einem Killer Sudoku Käfig wiederholen?**
Nein. Käfig-Ziffern müssen verschieden sein, genau das macht die Summen nützlich. Das ist das
Gegenteil von Calcudoku, wo sich Käfig-Ziffern wiederholen dürfen.

**Was ist die Regel der 45?**
Jede Zeile, Spalte und jeder Block ergibt 45. Vergleichst du das mit den Käfigen in einer Einheit,
zeigt sich die Summe der übrig gebliebenen Zellen, und oft löst das eine direkt.

**Warum haben Killer Sudoku Rätsel so wenige Vorgaben?**
Die Käfige tragen die Bedingung stattdessen. Ein gut gebautes Killer Gitter kann mit null Vorgaben
starten und trotzdem genau eine Lösung haben.

**Ist Killer Sudoku schwerer als normales Sudoku?**
Eher anders als strikt schwerer. Es verlangt Rechnen zusätzlich zur Logik, aber die Käfigsummen liefern
Information, die ein einfaches Gitter nicht hat.

**Wiederholen sich die Rätsel?**
Nein. Sie werden auf Abruf frisch generiert und vor der Anzeige als eindeutig geprüft.

---

**Mehr:** sieh dir alle dreizehn [Logikrätsel](/blog/puzzle-games/) an, lies über
[Sudoku Schwierigkeitsgrade](/blog/how-to-play-sudoku/), oder durchstöbere den Katalog auf
[braggster.com/games](/games/).
