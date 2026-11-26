---
title: "Killer Sudoku: Slik løser du burene uten å gjette"
slug: how-to-play-killer-sudoku
locale: nb
type: game
category: puzzle
game_id: killersudoku
meta_title: "Killer Sudoku: Slik løser du burene uten å gjette"
meta_description: "Killer Sudoku-strategi: 45-regelen, tvungne burkombinasjoner og summetabellene som lønner seg å huske. Uendelig mange oppgaver, offline og uten reklame."
primary_keyword: "killer sudoku regler"
secondary_keywords:
  - "killer sudoku strategi"
  - "45-regelen killer sudoku"
  - "killer sudoku kombinasjoner"
  - "killer sudoku app offline"
  - "sum sudoku slik spiller du"
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

# Killer Sudoku: Slik løser du burene uten å gjette

Killer Sudoku ser ut som vanlig Sudoku med litt ekstra pynt, men spilles som et helt annet puslespill.
Rutenettet starter med **langt færre oppgitte tall enn en vanlig Sudoku**, og det kan virke
skremmende første gang. All informasjonen er der. Den står bare som summer i stedet for sifre.

## Reglene

1. Hver rad, hver kolonne og hver 3x3-boks inneholder tallene 1 til 9 nøyaktig én gang. Helt som i
   vanlig Sudoku.
2. De 81 rutene er delt inn i **bur**, tegnet med stiplede kanter og en liten sum i hjørnet.
3. Sifrene i hvert bur er **forskjellige** og **summerer seg til** burets sum.

Den tredje regelen gjør en enorm jobb. Et bur er en fri form og ikke en rad eller en boks, så
forskjellighet kommer ikke av seg selv slik den gjør i vanlig Sudoku. Den må settes som krav, og det
er den som gjør summene til nyttig informasjon.

## Begynn med de tvungne burene

Noen summer har nøyaktig én mulig kombinasjon. Det er gratis informasjon, og du bør gå gjennom hvert
rutenett etter slike bur først.

| Burstørrelse | Sum | Eneste mulige sifre |
|---|---|---|
| 2 ruter | 3 | 1, 2 |
| 2 ruter | 4 | 1, 3 |
| 2 ruter | 16 | 7, 9 |
| 2 ruter | 17 | 8, 9 |
| 3 ruter | 6 | 1, 2, 3 |
| 3 ruter | 7 | 1, 2, 4 |
| 3 ruter | 23 | 6, 8, 9 |
| 3 ruter | 24 | 7, 8, 9 |
| 4 ruter | 10 | 1, 2, 3, 4 |
| 4 ruter | 11 | 1, 2, 3, 5 |
| 4 ruter | 29 | 5, 7, 8, 9 |
| 4 ruter | 30 | 6, 7, 8, 9 |

Du vet ikke rekkefølgen ennå, men du kjenner settet, og settet fjerner kandidater overalt der disse
rutene ser.

## 45-regelen

Den aller mest nyttige teknikken i Killer Sudoku, og grunnen til at erfarne løsere tar fatt på
rutenett som ser umulige ut.

Hver rad, kolonne og boks inneholder 1 til 9, så den **summerer seg til 45**.

Hvis en gruppe bur ligger helt innenfor én rad, legger du sammen summene deres. Differansen til 45 er
summen av rutene som er igjen i raden. Når det bare er én rute igjen, har du nettopp løst den
direkte.

Det virker også motsatt vei: hvis et bur stikker én rute ut av en boks, gir summen av burene inni
boksen minus 45 verdien til akkurat den ruten.

Kjeder du dette sammen over to eller tre rader samtidig, kalles teknikken noen ganger «innie og
outie»-metoden. Den er arbeidshesten i vanskelige Killer-rutenett.

## Burenes form har betydning

Fordi sifrene i et bur er forskjellige, begrenser formen det ytterligere:

- Et bur inne i én enkelt rad, kolonne eller boks kan aldri gjenta et siffer, og det kan ikke enheten
  heller, så det gir ikke noe nytt. Men et bur som **strekker seg over to bokser**, kan fortelle deg
  hvilken boks et siffer hører hjemme i.
- Et bur på to ruter med sum 17 må være 8 og 9. Ligger det i én rad, er radens 8 og 9 plassert, og
  alle andre ruter i raden mister begge kandidatene.

## Slik lager Braggster dem

Generatoren bygger burinndelingen ut fra en fullstendig Sudoku-løsning, og gjør det **med
sifrene i tankene**, for et bur i fri form er ikke automatisk forskjellig slik en rad, en kolonne
eller en boks er. Hvis burene vokste på måfå, ville noen bur få gjentatte sifre, og det er ikke et
gyldig Killer-bur.

Deretter kontrollerer den at løsningen er unik under **både** Sudoku- og burkravene samtidig, med en
backtracking-løser som kjenner burene. Å sjekke kravene hver for seg holder ikke: et rutenett kan
være tvetydig under Sudoku alene og unikt når burene tas med, og omvendt.

Den starter med et sett oppgitte Sudoku-tall som allerede er unikt, og fjerner så oppgitte tall ett
om gangen. En fjerning blir stående bare hvis løseren beviser at oppgaven fortsatt har nøyaktig én
løsning innenfor et lite søkebudsjett. Et tall den ikke kan bevise er overflødig, beholdes. Derfor
faller antallet med nivået: omtrent 32 oppgitte tall på Nybegynner, 24 på Lett, 16 på Middels og
rundt et dusin på Vanskelig og Ond, der burene også er større. Resultatet er at **hver oppgave du får,
garantert har nøyaktig én løsning**, aldri bare kanskje.

## Brettet

Killer-brettet bruker samme rutenett som Sudoku og legger et burlag oppå: fem fargetoner, stiplede
burkanter og en sum i hjørnet. Fem toner er nok til at naboburene alltid skiller seg fra hverandre,
uten at rutenettet blir et fargekart.

Hjelpemidlene er blyantnotater og hint. Braggster gir aldri tilbakemelding på feil svar mens du spiller
puslespillene, så feil telles i det stille og vises i oppsummeringen etter løsningen. Poengsummen er
løsningstid pluss et tillegg for hver feil og hvert hint, og lavest vinner.

## Vanlige spørsmål

**Kan sifre gjentas inne i et bur i Killer Sudoku?**
Nei. Sifrene i et bur må være forskjellige, og det er det som gjør summene nyttige. Det er stikk
motsatt av Calcudoku, der sifrene i et bur kan gjentas.

**Hva er 45-regelen?**
Hver rad, kolonne og boks summerer seg til 45. Sammenligner du det med burene inne i en enhet, får du
summen av de gjenværende rutene, og ofte løser det én rute direkte.

**Hvorfor har Killer Sudoku så få oppgitte tall?**
Burene bærer en del av begrensningene i stedet. Et godt konstruert Killer-rutenett kan starte uten
noen oppgitte tall og likevel ha nøyaktig én løsning, og i Braggster faller antallet fra omtrent 32 på
Nybegynner til rundt et dusin på Ond.

**Er Killer Sudoku vanskeligere enn vanlig Sudoku?**
Annerledes snarere enn strengt tatt vanskeligere. Du trenger regning ved siden av logikken, men
bursummene gir informasjon et vanlig rutenett ikke har.

**Gjentar oppgavene seg?**
Nei. De lages på nytt hver gang og kontrolleres som unike før du får se dem.

---

**Mer:** se alle nitten [logikkoppgaver](/blog/puzzle-games/), les om
[vanskelighetsgradene i Sudoku](/blog/how-to-play-sudoku/), eller bla gjennom katalogen på
[braggster.com/games](/games/).
