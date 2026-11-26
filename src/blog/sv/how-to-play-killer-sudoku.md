---
title: "Killer Sudoku: lös burarna utan att gissa"
slug: how-to-play-killer-sudoku
locale: sv
type: game
category: puzzle
game_id: killersudoku
meta_title: "Killer Sudoku: lös burarna utan att gissa"
meta_description: "Taktik för Killer Sudoku: regeln om 45, tvingade burkombinationer och summatabellerna värda att kunna. Oändligt med pussel, offline och utan reklam."
primary_keyword: "killer sudoku taktik"
secondary_keywords:
  - "killer sudoku regler"
  - "regeln om 45 killer sudoku"
  - "killer sudoku kombinationer"
  - "killer sudoku app offline"
  - "summa sudoku hur man spelar"
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

# Killer Sudoku: lös burarna utan att gissa

Killer Sudoku ser ut som vanlig sudoku med lite extra dekoration, men spelar sig som ett helt annat
pussel. Rutnäten börjar med **betydligt färre givna siffror än en vanlig sudoku**, vilket är en
skrämmande syn första gången. All information finns ändå där. Den är bara skriven som summor i
stället för siffror.

## Reglerna

1. Varje rad, kolumn och ruta på 3 gånger 3 innehåller siffrorna 1 till 9 exakt en gång. Som vanlig
   sudoku.
2. De 81 rutorna är uppdelade i **burar**, ritade med streckade kanter och en liten summa i hörnet.
3. Siffrorna i varje bur är **olika** och **tillsammans lika med burens summa**.

Den tredje regeln gör ett enormt jobb. En bur är en fri form och inte en rad eller en ruta, så att
siffrorna är olika kommer inte av sig självt som i vanlig sudoku. Det måste tvingas fram, och det är
just det som gör summorna användbara.

## Börja med de tvingade burarna

Vissa summor har bara en enda möjlig kombination. Det är gratis information, och det bör vara ditt
första varv över varje rutnät.

| Burens storlek | Summa | Enda möjliga siffror |
|---|---|---|
| 2 rutor | 3 | 1, 2 |
| 2 rutor | 4 | 1, 3 |
| 2 rutor | 16 | 7, 9 |
| 2 rutor | 17 | 8, 9 |
| 3 rutor | 6 | 1, 2, 3 |
| 3 rutor | 7 | 1, 2, 4 |
| 3 rutor | 23 | 6, 8, 9 |
| 3 rutor | 24 | 7, 8, 9 |
| 4 rutor | 10 | 1, 2, 3, 4 |
| 4 rutor | 11 | 1, 2, 3, 5 |
| 4 rutor | 29 | 5, 7, 8, 9 |
| 4 rutor | 30 | 6, 7, 8, 9 |

Du vet inte ordningen ännu, men du vet vilka siffror som ingår, och det räcker för att stryka
kandidater överallt där de rutorna ser.

## Regeln om 45

Den enskilt mest användbara tekniken i Killer Sudoku, och anledningen till att vana lösare öppnar
rutnät som verkar omöjliga.

Varje rad, kolumn och ruta innehåller 1 till 9, så den **summerar till 45**.

Om en grupp burar ryms helt inom en rad, lägg ihop deras summor. Skillnaden mot 45 är summan av de
rutor i raden som blir över. När bara en ruta blir över har du löst den direkt.

Det fungerar också åt andra hållet: om en bur sticker ut en ruta från en ruta på 3 gånger 3 ger
summan av burarna inuti, minus 45, den enda rutans värde.

Kedja ihop det över två eller tre rader samtidigt och tekniken kallas ibland "innie och outie". Den
är arbetshästen i svåra Killer-rutnät.

## Burens form spelar roll

Eftersom siffrorna i en bur är olika begränsar formen dem ytterligare:

- En bur inom en enda rad, kolumn eller ruta kan aldrig upprepa en siffra, och det kan inte heller
  enheten, så där tillkommer inget nytt. Men en bur som **sträcker sig över två rutor** kan avslöja i
  vilken ruta en siffra hör hemma.
- En bur på två rutor med summan 17 måste vara 8 och 9. Ligger den i en rad är radens 8 och 9
  placerade, och alla andra rutor i raden förlorar båda kandidaterna.

## Så skapar Braggster dem

Generatorn växer fram en burindelning ur en komplett sudokulösning och gör det **siffermedvetet**,
eftersom en fri bur inte automatiskt har olika siffror som en rad, kolumn eller ruta. Skulle burarna
växa blint skulle de få upprepningar, och det är ingen giltig Killer-bur.

Sedan kontrolleras att lösningen är unik under de **kombinerade** villkoren, sudoku och burar
tillsammans, med en burmedveten backtracking-lösare. Att kontrollera villkoren var för sig räcker
inte: ett rutnät kan vara flertydigt enbart under sudokureglerna men unikt när burarna läggs till,
och tvärtom.

Generatorn utgår från en uppsättning givna siffror som redan är unik och tar sedan bort en i taget.
En borttagning får bara stå kvar om lösaren bevisar att pusslet fortfarande har exakt en lösning
inom en liten sökbudget. En given siffra som den inte kan bevisa vara överflödig behålls. Därför
sjunker antalet med nivån: omkring 32 givna för Nybörjare, 24 för Lätt, 16 för Medel och ungefär ett
dussin för Svårt och Djävulskt, där burarna dessutom är större. Följden är att **varje pussel du
får garanterat har en enda lösning**, aldrig en kanske.

## Spelplanen

Killer-planen återanvänder sudokurutnätets uppbyggnad och lägger till ett burlager: fem nyanser,
streckade burkanter och en summa i hörnet. Fem nyanser räcker för att närliggande burar alltid ska
skilja sig åt utan att rutnätet förvandlas till ett färgdiagram.

Hjälpmedlen är anteckningar och tips. Ingenstans i Braggsters pussel får du direkt besked om fel
inmatning, så misstag räknas i tysthet och visas i sammanfattningen när du är klar. Poängen är
lösningstiden plus en påföljd för varje misstag och varje tips, och lägst vinner.

## Vanliga frågor

**Kan siffror upprepas inom en bur i Killer Sudoku?**
Nej. Siffrorna i en bur måste vara olika, och det är det som gör summorna användbara. Det är raka
motsatsen till Calcudoku, där siffror i en bur får upprepas.

**Vad är regeln om 45?**
Varje rad, kolumn och ruta summerar till 45. Jämför du det med burarna i en enhet får du summan av de
rutor som blir över, och ofta löser det en av dem direkt.

**Varför har Killer Sudoku så få givna siffror?**
Burarna bär en del av villkoren i stället. Ett välkonstruerat Killer-rutnät kan börja helt utan
givna siffror och ändå ha exakt en lösning, och i Braggster sjunker antalet från omkring 32 för
Nybörjare till ungefär ett dussin för Djävulskt.

**Är Killer Sudoku svårare än vanlig sudoku?**
Annorlunda snarare än strikt svårare. Du behöver räkna vid sidan av logiken, men burarnas summor ger
information som ett vanligt rutnät saknar.

**Upprepas pusslen?**
Nej. De skapas på nytt vid behov och bevisas ha en unik lösning innan du får se dem.

---

**Mer:** se alla nitton [logikpussel](/blog/puzzle-games/), läs om
[svårighetsgrader i sudoku](/blog/how-to-play-sudoku/), eller bläddra i katalogen på
[braggster.com/games](/games/).
