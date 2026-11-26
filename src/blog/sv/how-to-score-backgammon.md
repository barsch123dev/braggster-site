---
title: "Poängräkning i backgammon: vanlig vinst, gammon och backgammon"
slug: how-to-score-backgammon
locale: sv
type: game
category: board
game_id: backgammon
meta_title: "Poängräkning i backgammon: vinst, gammon, backgammon"
meta_description: "Vad en vinst i backgammon är värd: 1 för vanlig, 2 för gammon, 3 för backgammon. Dessutom ett spelbart bräde och en datormotståndare som kör expectimax."
primary_keyword: "backgammon poängräkning"
secondary_keywords:
  - "vad är gammon i backgammon"
  - "backgammon regler"
  - "spela backgammon offline"
  - "backgammon poäng match"
  - "backgammon mot datorn"
  - "spela backgammon online med vänner"
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

# Poängräkning i backgammon: vanlig vinst, gammon och backgammon

Backgammon är det äldsta spelet i Braggsters katalog med bred marginal, och det har det renaste
poängsystemet av dem alla. Tre utfall, tre värden, och hela skillnaden mellan en vanlig vinst och en
krossande ligger i om din motståndare fick hem en bricka.

## De tre resultaten

| Resultat | Värde | Villkor |
|---|---|---|
| **Vanlig vinst** | 1 poäng | Förloraren har tagit av minst en bricka |
| **Gammon** | 2 poäng | Förloraren har inte tagit av någon |
| **Backgammon** | 3 poäng | Förloraren har inte tagit av någon och har dessutom en bricka kvar på vinnarens hemmaplan eller på baren |

Det är hela poängsystemet. Poängen läggs ihop över partierna som en löpande ställning och den som har
högst total leder.

Gammonregeln är det som ger backgammon dess spänning i slutspelet. En spelare som tydligt ligger
under spelar inte längre för att vinna, utan för att få av **en enda bricka** innan motståndaren blir
klar, för det halverar skadan. Att se någon rusa hem med en ensam bricka för att undvika gammon hör
till det mer dramatiska som finns i sällskapsspel.

## Varför det inte finns någon dubbleringskub här

Seriöst backgammon använder en dubbleringskub som multiplicerar insatsen mitt i spelet och kan
dubbleras igen. Braggster har ingen dubbleringskub, och det är medvetet: ingenting i appen
registrerar en insats. Poängen är spelets resultat, 1, 2 eller 3, och inget mer.

Spelar du med kub hemma, skriv in resultatet av varje spel och låt kuben ligga kvar på brädet.

## Grunderna i spelet

Varje sida har femton brickor som rör sig i motsatta riktningar runt tjugofyra punkter, med målet att
få in alla på sin egen hemmaplan och sedan ta av dem.

- Kasta två tärningar och flytta två brickor, eller en bricka två gånger.
- **Dubbelkast spelas fyra gånger**, inte två.
- En punkt som hålls av två eller fler av motståndarens brickor är stängd för dig.
- En ensam bricka är en **blott**. Landar du på den går den till baren, och den måste komma in igen på
  motståndarens hemmaplan innan den spelaren får flytta något annat.
- När alla femton är hemma börjar du ta av dem.

## Det spelbara brädet

Braggsters Backgammon har ett bräde för spel på en och samma enhet: kasta de två tärningarna, tryck
på en bricka och sedan på en markerad punkt för att flytta den, slå ut blottor till baren, kom in
igen och ta av. Det färdiga spelet går rakt in i den löpande ställningen, så ett spel på telefonen
kan aldrig räknas annorlunda än ett som skrivits in för hand.

Två startuppställningar stöds:

- **Standard**, den vanliga startuppställningen.
- **Nackgammon**, som flyttar två brickor längre bak så att det tidiga spelet blir mindre ett rent
  lopp och mer positionsspel.

## Spela tillsammans på två telefoner, på plats eller online

Du kan också spela med en telefon var. Med [Spela tillsammans](/play-together/) startar en telefon ett
bord och visar en QR-kod, den andra skannar den, och båda spelarna ser samma bräde live. Ni kastar och
flyttar var och en från er egen telefon, det senaste draget markeras på båda brädena, och det färdiga
spelet ger 1, 2 eller 3 poäng i ställningen på båda telefonerna. På samma wifi behövs inget internet,
och för att spela backgammon online med en vän någon annanstans skickar du en inbjudningslänk eller
koden på 8 tecken. Inget konto behövs, och bara värden behöver ha spelet. [Guiden till att spela
tillsammans på flera telefoner](/blog/play-games-together-on-multiple-phones/) går igenom det steg
för steg.

## Datormotståndaren, och varför den är annorlunda

Backgammon har en övningsskärm mot datorn med tre nivåer, där du spelar som Ljus eller Mörk.

Det som är värt att veta är att den inte kan fungera som de andra motorerna i Braggster. Schack, Dam,
Internationell dam och Othello använder alla alfa-beta-sökning, som förutsätter att spelet är
deterministiskt: du vet exakt vilka lägen som går att nå härifrån.

Backgammon har tärningar. Varje nod i trädet är en slumpnod, med tjugoett olika kast att ta hänsyn
till. Därför kör backgammonmotorn en **expectimax**-sökning i stället, som tar medelvärdet över de
kasten i stället för att anta att motståndaren väljer det sämsta för dig. Den kör i en bakgrundstråd
så att brädet förblir responsivt medan den tänker.

Övningspartier registreras aldrig, så att spela mot datorn påverkar inte din statistik.

## Vanliga frågor

**Hur många poäng är en gammon värd?**
2 poäng. En vanlig vinst är 1 och en backgammon är 3.

**Vad är skillnaden mellan gammon och backgammon?**
Båda kräver att förloraren inte har tagit av något. Det är bara en backgammon om förloraren fortfarande
har en bricka på baren eller på vinnarens hemmaplan när spelet slutar.

**Flyttar man fyra gånger vid dubbelkast i backgammon?**
Ja. Slår du 5-5 får du fyra drag om fem, inte två.

**Finns det en dubbleringskub i appen?**
Nej. Braggster registrerar bara spelets resultat, utan någon insats någonstans i appen.

**Kan jag spela backgammon offline mot datorn?**
Ja. Motorn körs helt på din enhet, utan uppkoppling och utan konto.

**Kan två personer spela backgammon på två telefoner, eller online?**
Ja. Med Spela tillsammans använder varje spelare sin egen telefon. Den ena startar ett bord, den andra
skannar dess kod, och spelet pågår live på båda skärmarna. På samma wifi behövs inget internet, och
vänner på andra platser går med online via en inbjudningslänk eller koden på 8 tecken.

**Vad är Nackgammon?**
En startuppställning som drar två brickor längre bak, vilket gör öppningen mer positionell och mindre
ett rent lopp. Braggster stöder den vid sidan av standardöppningen.

---

**Mer:** bläddra bland alla spel på [braggster.com/games](/games/), eller läs översikten över
[poängräkning i sällskapsspel](/blog/board-game-score-sheets/).
