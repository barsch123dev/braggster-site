---
title: "Backgammon-poeng: Enkel seier, gammon og backgammon"
slug: how-to-score-backgammon
locale: nb
type: game
category: board
game_id: backgammon
meta_title: "Backgammon-poeng: Enkel seier, gammon og backgammon"
meta_description: "Hva en backgammon-seier er verdt: 1 poeng for enkel seier, 2 for gammon, 3 for backgammon. Pluss et spillbart brett og en motstander som bruker expectimax."
primary_keyword: "backgammon regler"
secondary_keywords:
  - "hva er gammon i backgammon"
  - "backgammon poengtelling"
  - "spille backgammon offline"
  - "backgammon turnering poeng"
  - "backgammon mot datamaskinen"
  - "spille backgammon på nett med venner"
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

# Backgammon-poeng: Enkel seier, gammon og backgammon

Backgammon er det eldste spillet i Braggsters katalog med god margin, og det har det reneste
poengsystemet av alle. Tre utfall, tre verdier, og hele forskjellen mellom en vanlig seier og en
knusende seier ligger i om motstanderen fikk én brikke i mål.

## De tre resultatene

| Resultat | Verdi | Vilkår |
|---|---|---|
| **Enkel seier** | 1 poeng | Taperen har tatt ut minst én brikke |
| **Gammon** | 2 poeng | Taperen har ikke tatt ut noen |
| **Backgammon** | 3 poeng | Taperen har ikke tatt ut noen, og har fortsatt en brikke i vinnerens hjemmefelt eller på baren |

Det er hele poengsystemet. Poengene samles som en løpende sum over partiene, og den som har høyest
sum, leder.

Gammon-regelen er det som gir backgammon spenningen i sluttspillet. En spiller som tydelig taper,
spiller ikke lenger for å vinne, men for å få **én eneste brikke** ut før motstanderen blir ferdig,
for det halverer skaden. Å se noen løpe med en enslig brikke hjem for å redde seg fra gammon er noe
av det mest dramatiske i brettspill.

## Hvorfor det ikke finnes noen dobleterning her

Seriøs backgammon bruker en dobleterning, som flerdobler verdien av partiet underveis og kan
dobles på nytt. Braggster har ingen dobleterning, og det er bevisst: ingenting i appen registrerer
noen innsats. Poengsummen er resultatet av partiet, 1, 2 eller 3, og ikke noe mer.

Spiller du med dobleterning hjemme, kan du føre resultatet av hvert parti og la terningen ligge på
brettet.

## Grunnleggende spilleregler

Hver side har femten brikker som beveger seg i motsatt retning rundt tjuefire punkter, med mål om å
få dem alle inn i sitt eget hjemmefelt og så ta dem ut.

- Kast to terninger og flytt to brikker, eller én brikke to ganger.
- **Dobbelkast spilles fire ganger**, ikke to.
- Et punkt som holdes av to eller flere av motstanderens brikker, er stengt for deg.
- En enslig brikke er en **blot**. Lander du på den, havner den på baren, og den må inn igjen i
  motstanderens hjemmefelt før den spilleren kan flytte noe annet.
- Når alle femten er hjemme, begynner du å ta dem ut.

## Det spillbare brettet

Backgammon i Braggster har et brett for to på samme enhet: kast de to terningene, trykk på en brikke
og så på et uthevet punkt for å flytte den, slå blots ut på baren, kom inn igjen og ta brikkene ut.
Det ferdige partiet føres rett inn i den løpende summen, så et parti spilt på telefonen kan aldri gi
annen poengsum enn et som er ført for hånd.

To startoppstillinger støttes:

- **Standard**, den vanlige startposisjonen.
- **Nackgammon**, som flytter to brikker lenger bak slik at åpningen blir mindre et kappløp og mer et
  posisjonsspill.

## Spill sammen på to telefoner, i nærheten eller på nett

Du kan også spille med én telefon hver. Med [Spill sammen](/play-together/) starter én telefon et
bord og viser en QR-kode, den andre skanner den, og begge spillerne ser det samme brettet direkte.
Dere kaster og flytter hver fra deres egen telefon, det siste trekket er markert på begge brettene,
og det ferdige partiet gir 1, 2 eller 3 poeng i summen på begge telefonene. På samme Wi-Fi trengs
ikke internett, og for å spille backgammon på nett med en venn et annet sted sender du en
invitasjonslenke eller koden på 8 tegn. Det trengs ingen konto, og bare verten trenger spillet.
[Veiledningen for å spille sammen på flere telefoner](/blog/play-games-together-on-multiple-phones/)
tar deg gjennom det steg for steg.

## Datamotstanderen, og hvorfor den er annerledes

Backgammon har en øvingsskjerm mot datamaskinen med tre nivåer, der du spiller som Lys eller Mørk.

Det som er verdt å vite, er at den ikke kan fungere slik de andre motorene i Braggster gjør. Sjakk,
Dam, Internasjonal dam og Othello bruker alle alfa-beta-søk, som forutsetter at spillet er
deterministisk: du vet nøyaktig hvilke posisjoner som kan nås herfra.

Backgammon har terninger. Hver node i treet er en sjansenode, med tjueen forskjellige kast å ta
hensyn til. Derfor kjører backgammon-motoren et **expectimax**-søk i stedet, som tar gjennomsnittet
over disse kastene i stedet for å anta at motstanderen velger det verste for deg. Den kjører i en
bakgrunnstråd, så brettet forblir responsivt mens den tenker.

Treningspartier registreres aldri, så å spille mot datamaskinen påvirker ikke statistikken din.

## Vanlige spørsmål

**Hvor mange poeng er en gammon verdt?**
2 poeng. En enkel seier er 1 og en backgammon er 3.

**Hva er forskjellen på gammon og backgammon?**
Begge krever at taperen ikke har tatt ut noe. Det er bare en backgammon hvis taperen fortsatt har en
brikke på baren eller i vinnerens hjemmefelt når partiet er slutt.

**Spilles dobbelkast fire ganger i backgammon?**
Ja. Kaster du 5-5, får du fire trekk på fem, ikke to.

**Finnes det en dobleterning i appen?**
Nei. Braggster registrerer bare resultatet av partiet, uten noen innsats noe sted i appen.

**Kan jeg spille backgammon offline mot datamaskinen?**
Ja. Motoren kjører helt på enheten din, uten tilkobling og uten konto.

**Kan to personer spille backgammon på to telefoner, eller på nett?**
Ja. Med Spill sammen bruker hver spiller sin egen telefon. Den ene starter et bord, den andre skanner
koden, og partiet spilles direkte på begge skjermene. På samme Wi-Fi trengs ikke internett, og venner
andre steder blir med på nett med en invitasjonslenke eller koden på 8 tegn.

**Hva er Nackgammon?**
En variant av startposisjonen som trekker to brikker lenger bak, slik at åpningen blir mer et
posisjonsspill og mindre et rent kappløp. Braggster støtter den ved siden av standardåpningen.

---

**Mer:** bla gjennom alle spillene på [braggster.com/games](/games/), eller les oversikten over
[poengføring i brettspill](/blog/board-game-score-sheets/).
