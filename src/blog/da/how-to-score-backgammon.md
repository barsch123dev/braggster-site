---
title: "Backgammon point: Enkelt sejr, gammon og backgammon"
slug: how-to-score-backgammon
locale: da
type: game
category: board
game_id: backgammon
meta_title: "Backgammon point: Enkelt sejr, gammon, backgammon"
meta_description: "Hvad en backgammon-sejr er værd: 1 for en enkelt, 2 for en gammon, 3 for en backgammon. Plus et spilbart bræt og en computermodstander med expectimax."
primary_keyword: "backgammon regler"
secondary_keywords:
  - "hvad er en gammon i backgammon"
  - "backgammon point"
  - "spil backgammon offline"
  - "backgammon pointberegning"
  - "backgammon mod computeren"
  - "spil backgammon online med venner"
search_intent: informational
priority: 1
updated: 2026-10-21
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

# Backgammon point: Enkelt sejr, gammon og backgammon

Backgammon er det ældste spil i Braggsters katalog med en solid margin, og det har den reneste
pointgivning af dem alle. Tre udfald, tre værdier, og hele forskellen på en afslappet sejr og en
knusende sejr ligger i, om modstanderen fik en brik hjem.

## De tre resultater

| Resultat | Værd | Betingelse |
|---|---|---|
| **Enkelt** | 1 point | Taberen har taget mindst én brik ud |
| **Gammon** | 2 point | Taberen har ikke taget nogen brik ud |
| **Backgammon** | 3 point | Taberen har ikke taget nogen brik ud og har stadig en brik i vinderens hjemmefelt eller på baren |

Det er hele pointsystemet. Point lægges sammen på tværs af spil som en løbende stilling, og den højeste
total fører.

Gammon-reglen er det, der giver backgammon dets spænding i slutspillet. En spiller, der klart er ved at
tabe, spiller ikke længere for at vinde, men for at få **én eneste brik** ud, før modstanderen er
færdig, for det halverer skaden. At se nogen løbe en enkelt brik hjem for at redde en gammon er noget af
det mest dramatiske, der findes i brætspil.

## Hvorfor der ikke er nogen dobbeltterning her

Seriøst backgammon bruger en dobbeltterning, som fordobler spillets værdi midt i partiet og kan
redobles. Braggster har ingen dobbeltterning, og det er bevidst: intet sted i appen registreres en
indsats. Scoren er resultatet af spillet, 1, 2 eller 3, og det er det hele.

Spiller du med dobbeltterning derhjemme, så skriv resultatet af hvert spil ned og behold terningen på
brættet.

## Det grundlæggende i spillet

Hver side har femten brikker, der bevæger sig i hver sin retning rundt om fireogtyve felter, med målet
at få dem alle ind i eget hjemmefelt og derefter tage dem ud.

- Slå med to terninger og flyt to brikker, eller én brik to gange.
- **Pasch spilles fire gange**, ikke to.
- Et felt, som to eller flere af modstanderens brikker holder, er lukket for dig.
- En enkelt brik er en **blot**. Lander du på den, kommer den på baren, og den skal ind igen i
  modstanderens hjemmefelt, før den spiller kan flytte noget andet.
- Når alle femten er hjemme, begynder du at tage brikker ud.

## Det spilbare bræt

Braggsters Backgammon har et bræt til to spillere på samme enhed: slå med de to terninger, tryk på en
brik og derefter på et markeret felt for at flytte den, slå blotter ned på baren, kom ind igen, og tag
brikker ud. Det færdige spil scores direkte ind i den løbende stilling, så et spil på telefonen aldrig
kan give en anden score end et, der er skrevet ned i hånden.

To åbninger understøttes:

- **Standard**, den normale startstilling.
- **Nackgammon**, som flytter to brikker tilbage, så det tidlige spil bliver mindre et kapløb og mere
  positionsspil.

## Spil sammen på to telefoner, i nærheden eller online

Du kan også spille med en telefon hver. Med [Spil sammen](/play-together/) starter den ene telefon et
bord og viser en QR-kode, den anden scanner den, og begge spillere ser det samme bræt live. I slår og
flytter hver især fra jeres egen telefon, det sidste træk er markeret på begge bræt, og det færdige spil
giver 1, 2 eller 3 point i stillingen på begge telefoner. På samme wifi kræves der ikke internet, og vil
du spille backgammon online med en ven et andet sted, sender du et invitationslink eller koden på 8
tegn. Der er ingen konto, og det er kun værten, der skal have spillet. [Guiden til at spille sammen på
flere telefoner](/blog/play-games-together-on-multiple-phones/) viser det trin for trin.

## Computermodstanderen, og hvorfor den er anderledes

Backgammon har en træningsskærm mod computeren med tre niveauer, hvor du spiller som Lys eller Mørk.

Det er værd at vide, at den ikke kan fungere som de andre motorer i Braggster. Skak, Checkers,
Internationalt dam og Othello bruger alle alfa-beta-søgning, som forudsætter, at spillet er
deterministisk: du ved præcis, hvilke stillinger der kan nås herfra.

Backgammon har terninger. Hver knude i træet er en tilfældighedsknude med enogtyve forskellige slag at
tage stilling til. Derfor kører backgammon-motoren en **expectimax**-søgning i stedet, der tager
gennemsnittet over de slag i stedet for at antage, at modstanderen vælger det værste for dig. Den kører
på en baggrundstråd, så brættet forbliver responsivt, mens den tænker.

Træningsspil bliver aldrig registreret, så at spille mod computeren rører ikke din statistik.

## Ofte stillede spørgsmål

**Hvor mange point er en gammon værd?**
2 point. En enkelt sejr er 1, og en backgammon er 3.

**Hvad er forskellen på en gammon og en backgammon?**
Begge kræver, at taberen ikke har taget noget ud. Det er kun en backgammon, hvis taberen stadig har en
brik på baren eller i vinderens hjemmefelt, når spillet slutter.

**Flytter man fire gange med pasch i backgammon?**
Ja. Slår du 5-5, får du fire træk på fem, ikke to.

**Er der en dobbeltterning i appen?**
Nej. Braggster registrerer kun resultatet af spillet, og ingen steder i appen registreres en indsats.

**Kan jeg spille backgammon offline mod computeren?**
Ja. Motoren kører helt på din enhed, uden forbindelse og uden konto.

**Kan to personer spille backgammon på to telefoner, eller online?**
Ja. Med Spil sammen bruger hver spiller sin egen telefon. Den ene starter et bord, den anden scanner
dets kode, og spillet foregår live på begge skærme. På samme wifi kræves der ikke internet, og venner et
andet sted deltager online med et invitationslink eller koden på 8 tegn.

**Hvad er Nackgammon?**
En startstilling, der trækker to brikker længere tilbage, så åbningen bliver mere positionsspil og
mindre et rent kapløb. Braggster understøtter den ved siden af standardåbningen.

---

**Mere:** gå på opdagelse blandt alle spil på [braggster.com/games](/games/), eller læs oversigten over
[pointgivning i brætspil](/blog/board-game-score-sheets/).
