---
title: "Killer Sudoku: Kooien Oplossen Zonder te Gokken"
slug: how-to-play-killer-sudoku
locale: nl
type: game
category: puzzle
game_id: killersudoku
meta_title: "Killer Sudoku: Kooien Oplossen Zonder te Gokken"
meta_description: "Killer Sudoku-strategie: de regel van 45, gedwongen kooicombinaties en de somtabellen die het onthouden waard zijn. Eindeloos gegenereerd, offline."
primary_keyword: "killer sudoku strategie"
secondary_keywords:
  - "killer sudoku regels"
  - "regel van 45 killer sudoku"
  - "killer sudoku kooicombinaties"
  - "killer sudoku app offline"
  - "somsudoku uitleg"
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

# Killer Sudoku: Kooien Oplossen Zonder te Gokken

Killer Sudoku ziet eruit als Sudoku met extra versiering en speelt als een compleet andere puzzel. De
meeste roosters beginnen met **heel weinig gegeven getallen, of helemaal geen**, wat de eerste keer
dat je er eentje ziet best verontrustend is. Alle informatie is er gewoon. Hij staat alleen genoteerd
als sommen in plaats van cijfers.

## De regels

1. Elke rij, kolom en 3x3 vak bevat 1 tot en met 9 precies één keer. Gewone Sudoku.
2. De 81 vakjes zijn verdeeld in **kooien**, getekend met stippellijnen en een kleine som in de hoek.
3. De cijfers in elke kooi zijn **verschillend** en **tellen op tot die som**.

Die derde regel doet ontzettend veel werk, omdat een kooi een vrije vorm heeft in plaats van een rij
of een vak, waardoor verschillendheid niet vanzelfsprekend is zoals bij gewone Sudoku. Ze moet
opgelegd worden, en dat is precies wat de sommen informatief maakt.

## Begin met de gedwongen kooien

Sommige sommen hebben maar precies één mogelijke combinatie. Dat is gratis informatie en zou je
eerste stap door elk rooster moeten zijn.

| Kooigrootte | Som | Enige mogelijke cijfers |
|---|---|---|
| 2 vakjes | 3 | 1, 2 |
| 2 vakjes | 4 | 1, 3 |
| 2 vakjes | 16 | 7, 9 |
| 2 vakjes | 17 | 8, 9 |
| 3 vakjes | 6 | 1, 2, 3 |
| 3 vakjes | 7 | 1, 2, 4 |
| 3 vakjes | 23 | 6, 8, 9 |
| 3 vakjes | 24 | 7, 8, 9 |
| 4 vakjes | 10 | 1, 2, 3, 4 |
| 4 vakjes | 11 | 1, 2, 3, 5 |
| 4 vakjes | 29 | 5, 7, 8, 9 |
| 4 vakjes | 30 | 6, 7, 8, 9 |

Je weet de volgorde nog niet, maar je weet de verzameling, en het kennen van die verzameling
schrapt kandidaten overal waar die vakjes naar kijken.

## De regel van 45

De nuttigste techniek in Killer Sudoku, en de reden dat ervaren spelers roosters openen die onmogelijk
lijken.

Elke rij, kolom en vak bevat 1 tot en met 9, dus **telt op tot 45**.

Past een groep kooien volledig in één rij, tel dan hun sommen op. Het verschil met 45 is het totaal
van de vakjes die in die rij overblijven. Blijft er precies één vakje over, dan heb je die meteen
opgelost.

Hetzelfde werkt andersom: steekt een kooi met één vakje buiten een vak, dan geeft de som van de kooien
binnen dat vak min 45 de waarde van dat ene overblijvende vakje.

Ketent je dit over twee of drie rijen tegelijk, dan heet de techniek soms de "innie en outie"-methode.
Het is het werkpaard van moeilijke Killer-roosters.

## Kooivorm doet ertoe

Omdat de cijfers in een kooi verschillend zijn, beperkt de vorm haar verder:

- Een kooi binnen één rij, kolom of vak kan nooit herhalen, en dat kan de eenheid ook niet, dus dat
  levert niets nieuws op. Maar een kooi die **over twee vakken heen** loopt, kan wel verraden in welk
  vak een cijfer zit.
- Een kooi van twee vakjes met som 17 moet 8 en 9 zijn. Ligt hij in één rij, dan liggen de 8 en 9 van
  die rij vast en verliest elk ander vakje in de rij allebei die kandidaten.

## Hoe Braggster ze genereert

De generator laat een kooiverdeling groeien vanuit een volledige Sudoku-oplossing, en doet dat
**cijferbewust**, omdat een vrije-vormkooi niet automatisch verschillend is zoals een rij, kolom of
vak dat wel is. Kooien blindelings laten groeien zou kooien met herhalingen opleveren, en dat is geen
geldige Killer-kooi.

Vervolgens verifieert hij de uniciteit onder de **gecombineerde** Sudoku- en kooibeperking samen, met
een kooibewuste backtracking-oplosser. De twee beperkingen los van elkaar checken zou niet volstaan:
een rooster kan ambigu zijn onder Sudoku alleen en uniek worden zodra de kooien toegepast worden, en
andersom.

Kan een schaarse poging niet binnen het zoekbudget bewezen worden uniek te zijn, dan valt de generator
terug op de al geverifieerde gegeven-set van Sudoku voor die moeilijkheidsgraad. Het gevolg is dat
**elke puzzel die je krijgt echt eenduidig oplosbaar is**, nooit misschien.

## Het bord

Het Killer-bord hergebruikt de roosteropbouw van Sudoku en voegt een kooilaag toe: vijf tinten,
gestippelde kooiranden en een somlabel in de hoek. Vijf tinten is genoeg om naast elkaar liggende
kooien altijd te laten verschillen zonder dat het rooster een kleurkaart wordt.

Hulpmiddelen zijn potloodnotities en hints. Er is nergens in de puzzels van Braggster directe feedback
bij een foute invoer, dus fouten worden stilzwijgend geteld en pas onthuld in de samenvatting na
afloop. De score is oplostijd plus een straf per fout en per hint, en het laagste totaal wint.

## Veelgestelde vragen

**Kunnen cijfers herhalen binnen één Killer Sudoku-kooi?**
Nee. De cijfers in een kooi moeten verschillend zijn, en dat is precies wat de sommen nuttig maakt.
Dat is het tegenovergestelde van Calcudoku, waar cijfers binnen een kooi wel mogen herhalen.

**Wat is de regel van 45?**
Elke rij, kolom en vak telt op tot 45. Dat vergelijken met de kooien binnen een eenheid onthult het
totaal van de overgebleven vakjes, en lost er vaak meteen eentje op.

**Waarom hebben Killer Sudoku-puzzels zo weinig gegeven getallen?**
De kooien dragen de beperking in plaats daarvan. Een goed opgebouwd Killer-rooster kan met nul gegeven
getallen beginnen en toch precies één oplossing hebben.

**Is Killer Sudoku moeilijker dan gewone Sudoku?**
Eerder anders dan strikt moeilijker. Het vraagt rekenwerk naast de logica, maar de kooisommen geven
informatie die een gewoon rooster niet heeft.

**Herhalen de puzzels zich?**
Nee. Ze worden vers gegenereerd op aanvraag en geverifieerd als uniek voordat ze getoond worden.

---

**Meer:** bekijk alle dertien [logicapuzzels](/blog/puzzle-games/), lees over
[Sudoku-moeilijkheidsgraad](/blog/how-to-play-sudoku/), of blader door de catalogus op
[braggster.com/games](/games/).
