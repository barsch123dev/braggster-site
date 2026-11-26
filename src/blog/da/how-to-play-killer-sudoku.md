---
title: "Killer Sudoku: Sådan løser du burene uden at gætte"
slug: how-to-play-killer-sudoku
locale: da
type: game
category: puzzle
game_id: killersudoku
meta_title: "Killer Sudoku: Løs burene uden at gætte"
meta_description: "Killer Sudoku strategi: 45-reglen, tvungne burkombinationer og de summer, der er værd at lære udenad. Uendelige gåder, offline og uden reklamer."
primary_keyword: "killer sudoku regler"
secondary_keywords:
  - "killer sudoku strategi"
  - "45-reglen killer sudoku"
  - "killer sudoku kombinationer"
  - "killer sudoku app offline"
  - "sum sudoku sådan spiller du"
search_intent: informational
priority: 1
updated: 2026-10-21
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

# Killer Sudoku: Sådan løser du burene uden at gætte

Killer Sudoku ligner Sudoku med lidt ekstra pynt, men spiller som en helt anden gåde. Gitrene starter
med **langt færre givne tal end en almindelig Sudoku**, og det er alarmerende første gang, du ser et.
Oplysningerne er der alle sammen. De står bare som summer i stedet for som tal.

## Reglerne

1. Hver række, hver kolonne og hver boks på 3x3 indeholder tallene 1 til 9 præcis én gang. Helt
   almindelig Sudoku.
2. De 81 felter er delt op i **bure**, tegnet med stiplede kanter og en lille sum i hjørnet.
3. Tallene i hvert bur er **forskellige** og **giver tilsammen burets sum**.

Den tredje regel gør et enormt stykke arbejde. Et bur er en fri form og ikke en række eller en boks,
så forskellighed er ikke givet på forhånd, som den er i almindelig Sudoku. Den skal påtvinges, og det
er den, der gør summerne til brugbare oplysninger.

## Start med de tvungne bure

Nogle summer har præcis én mulig kombination. Det er gratis information, og den bør du tage først på
ethvert gitter.

| Burets størrelse | Sum | De eneste mulige tal |
|---|---|---|
| 2 felter | 3 | 1, 2 |
| 2 felter | 4 | 1, 3 |
| 2 felter | 16 | 7, 9 |
| 2 felter | 17 | 8, 9 |
| 3 felter | 6 | 1, 2, 3 |
| 3 felter | 7 | 1, 2, 4 |
| 3 felter | 23 | 6, 8, 9 |
| 3 felter | 24 | 7, 8, 9 |
| 4 felter | 10 | 1, 2, 3, 4 |
| 4 felter | 11 | 1, 2, 3, 5 |
| 4 felter | 29 | 5, 7, 8, 9 |
| 4 felter | 30 | 6, 7, 8, 9 |

Du kender endnu ikke rækkefølgen, men du kender mængden, og mængden fjerner kandidater overalt, hvor
de felter kigger hen.

## 45-reglen

Den mest nyttige teknik i Killer Sudoku, og grunden til at erfarne løsere kaster sig over gitre, der
ser umulige ud.

Hver række, hver kolonne og hver boks indeholder 1 til 9, så den **summer til 45**.

Hvis en række bure ligger helt inde i én række, lægger du deres summer sammen. Forskellen til 45 er
summen af de felter, der er tilbage i rækken. Når der kun er ét felt tilbage, har du løst det med det
samme.

Det virker også den anden vej: hvis et bur stikker ét felt ud af en boks, giver summen af burene inde i
boksen minus 45 værdien af netop det ene felt.

Kæder du det sammen over to eller tre rækker på én gang, kaldes teknikken nogle gange "innie og
outie"-metoden. Den er arbejdshesten i svære Killer-gitre.

## Burets form har betydning

Fordi tallene i et bur er forskellige, begrænser formen det yderligere:

- Et bur inde i én række, kolonne eller boks kan aldrig gentage et tal, og det kan enheden heller ikke,
  så der er ikke noget nyt i det. Men et bur, der **spænder over to bokse**, kan fortælle dig, i hvilken
  boks et tal bor.
- Et bur på to felter med summen 17 skal være 8 og 9. Ligger det i én række, er rækkens 8 og 9 placeret,
  og alle andre felter i rækken mister begge kandidater.

## Sådan laver Braggster dem

Generatoren vokser en burinddeling ud fra en komplet Sudoku-løsning, og det sker **med tallene i
tankerne**, fordi et bur i fri form ikke automatisk har forskellige tal, som en række, en kolonne eller
en boks har. Hvis burene voksede blindt, ville der opstå bure med gentagelser, og det er ikke
et lovligt Killer-bur.

Derefter kontrolleres entydigheden under de **kombinerede** Sudoku- og burbetingelser med en
burbevidst backtracking-løser. At tjekke de to sæt regler hver for sig ville ikke række: et gitter kan
være flertydigt under Sudoku alene og entydigt, når burene tages med, og omvendt.

Den starter fra et sæt givne Sudoku-tal, der allerede er entydigt, og fjerner så givne tal ét ad
gangen. En fjernelse bliver kun stående, hvis løseren inden for et lille søgebudget kan bevise, at
gåden stadig har præcis én løsning. Et givent tal, der ikke kan bevises overflødigt, bliver stående.
Derfor falder antallet med niveauet: omkring 32 givne tal på Begynder, 24 på Let, 16 på Mellem og
omkring et dusin på Svær og Ond, hvor burene også er større. Konsekvensen er, at **hver eneste gåde, du
får, har helt sikkert én og kun én løsning**, aldrig et måske.

## Brættet

Killer-brættet genbruger Sudokus gitter og lægger et burlag oven på: fem nuancer, stiplede burkanter og
en sum i hjørnet. Fem nuancer er nok til, at nabobure altid kan skelnes, uden at gitteret bliver et
farvekort.

Hjælpemidlerne er blyantsnoter og hint. Der er ingen live-feedback på forkerte tal nogen steder i
Braggsters gåder, så fejl tælles i stilhed og vises i opsummeringen af løsningen. Scoren er løsningstid
plus en straf for hver fejl og hvert hint, og den laveste vinder.

## Ofte stillede spørgsmål

**Kan tal gentages inde i et bur i Killer Sudoku?**
Nej. Tallene i et bur skal være forskellige, og det er det, der gør summerne brugbare. Det er det
modsatte af Calcudoku, hvor tallene i et bur godt må gentages.

**Hvad er 45-reglen?**
Hver række, hver kolonne og hver boks summer til 45. Sammenligner du det med burene inde i en enhed,
får du summen af de resterende felter, og ofte løser det ét felt direkte.

**Hvorfor har Killer Sudoku så få givne tal?**
Burene bærer en del af begrænsningen i stedet. Et velbygget Killer-gitter kan starte helt uden givne
tal og stadig have præcis én løsning, og i Braggster falder antallet fra omkring 32 på Begynder til
omkring et dusin på Ond.

**Er Killer Sudoku sværere end almindelig Sudoku?**
Anderledes snarere end strengt sværere. Du skal regne ved siden af logikken, men burenes summer giver
oplysninger, som et almindeligt gitter ikke har.

**Gentager gåderne sig?**
Nej. De laves friske, når du beder om dem, og bevises entydige, før du ser dem.

---

**Mere:** se alle nitten [logiske gåder](/blog/puzzle-games/), læs om
[Sudokus sværhedsgrader](/blog/how-to-play-sudoku/), eller gå på opdagelse i kataloget på
[braggster.com/games](/games/).
