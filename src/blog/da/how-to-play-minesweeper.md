---
title: "Minestryger uden gætteri: Derfor tvinger de fleste versioner dig til at gætte"
slug: how-to-play-minesweeper
locale: da
type: game
category: puzzle
game_id: minesweeper
meta_title: "Minestryger uden gætteri: Derfor må du ofte gætte"
meta_description: "Klassisk Minestryger ender ofte i stillinger uden et logisk træk. Her er hvorfor, mønstrene der løser de fleste baner, og en version uden gætteri."
primary_keyword: "minestryger uden gætteri"
secondary_keywords:
  - "minestryger strategi"
  - "minestryger mønstre 1-2-1"
  - "minestryger uden at gætte"
  - "minestryger app offline"
  - "sådan spiller du minestryger"
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

# Minestryger uden gætteri: Derfor tvinger de fleste versioner dig til at gætte

Her er noget, ingen fortæller om klassisk Minestryger: **det er ikke en logisk gåde.** Ikke pålideligt. En
almindelig tilfældig bane ender jævnligt i en stilling, hvor alle de resterende træk er plat eller
krone, og spillet slutter, fordi du valgte det forkerte af to lige gode felter.

Det er ikke en svær gåde. Det er en fair gåde, der løb tør for oplysninger.

## Reglerne i korte træk

Åbn et felt, og det viser, hvor mange miner der rører ved det, med alle otte naboer talt med. Åbn alle
de felter, der ikke er miner, og banen er løst. Tryk og hold for at sætte et flag på et felt, du har
regnet ud.

Braggster har fem niveauer:

| Niveau | Bane | Miner |
|---|---|---|
| Begynder | 9x9 | 10 |
| Let | 9x9 | 13 |
| Middel | 16x16 | 40 |
| Svær | 16x24 | 70 |
| Djævelsk | 16x30 | 99 |

## De to regler, der løser det meste af en bane

**Opfyldt.** Et tal med lige så mange flag omkring sig, som dets værdi angiver, har alle sine miner
fundet. Alle andre naboer er sikre og kan åbnes.

**Opbrugt.** Et tal, hvor antallet af uåbnede naboer er præcis lig med det, der mangler, betyder, at
alle naboerne er miner. Sæt flag på dem alle.

Skift mellem de to regler, og du rydder langt størstedelen af enhver bane. De fleste spillere gør det
instinktivt uden at give det et navn.

## Når de ikke er nok

Det klassiske tilfælde er **1-2-1-mønsteret** langs en kant: tre tal i række med værdierne 1, 2, 1 og
tre ukendte felter under dem. Ingen af de to regler ovenfor afgør det, men en sammenligning af
begrænsningerne gør. 2'eren har brug for to miner blandt tre felter, og hver 1'er har brug for én
blandt to. Den eneste konsekvente fordeling lægger minerne under de to 1'ere og lader feltet i midten
være sikkert.

Det er **delmængde-reglen** i generel form: når ét tals ukendte naboer er en delmængde af et andets,
trækker du begrænsningerne fra hinanden, og forskellen er givet. Det er den teknik, der adskiller
spillere, der klarer ekspertbaner, fra spillere, der når frem til de sidste tyve felter og begynder at
gætte.

## Hvad "uden gætteri" betyder her

Braggster laver en bane og **beviser, at den kan løses fra start til slut med ren logik**, før du
overhovedet ser den.

Kontrollen tager udgangspunkt i et garanteret sikkert åbningsområde og kører en deterministisk
deduktionsløser med præcis de regler, der er nævnt ovenfor: opfyldte og opbrugte tal samt
delmængde-reglen for to tal. Kan banen ikke løses på den måde, kasseres den og laves forfra. Hvis
gentagne forsøg mislykkes, sættes antallet af miner ned, indtil der findes en løsbar bane.

Den praktiske garanti: **hvis du sidder fast, findes der en slutning.** Du er ikke løbet tør for
oplysninger, du har bare ikke fundet den endnu. Det er en helt anden fornemmelse end klassisk
Minestryger, og det er hele grunden til at spille netop denne version.

## At ramme en mine afslutter ikke spillet

Braggster tilpasser den klassiske fejlmodel. Åbner du en mine, tæller det som **én stille fejl**, og
spillet fortsætter.

Det svarer til, hvordan Sudoku i appen tæller et forkert tal. At miste hele banen på en enkelt
fejltryk i træk nummer halvfems er en straffemodel, der er lånt fra arkadespil og ikke fra gåder, og
den passer dårligt til en bane, der fra start var garanteret løsbar.

Fejl tælles i stilhed uden live-feedback og vises i opsummeringen af løsningen. Din score er løsningstid
plus en straf for hver fejl og hvert hint, og den laveste vinder.

## Ofte stillede spørgsmål

**Hvad betyder Minestryger uden gætteri?**
Hver bane er bevist løsbar med ren deduktion, før den bliver givet. Der er aldrig en stilling, hvor du
er nødt til at gætte mellem to lige sandsynlige felter.

**Hvordan bliver det kontrolleret?**
En deterministisk løser arbejder sig gennem banen fra et garanteret sikkert åbningsområde med opfyldte
og opbrugte tal plus en delmængde-regel for to tal. Baner, den ikke kan færdiggøre, laves forfra.

**Slutter spillet, hvis jeg rammer en mine?**
Nej. Det tæller som én fejl i din score, og spillet fortsætter, på samme måde som et forkert tal i
Sudoku.

**Hvad er 1-2-1-mønsteret?**
Tre tal i række med værdierne 1, 2, 1 og ukendte felter under dem. Minerne ligger under de to 1'ere,
og feltet i midten er sikkert. Det er det mest nyttige mønster at lære.

**Hvad er den sværeste bane?**
Djævelsk, på 16x30 med 99 miner. Begynder er 9x9 med 10.

**Virker det offline?**
Ja. Banerne laves og bevises på din egen enhed, så der er intet at hente og ingen konto at oprette.

---

**Mere:** se alle nitten [logiske gåder](/blog/puzzle-games/), læs om
[Sudokus sværhedsgrader](/blog/how-to-play-sudoku/), eller gå på opdagelse i kataloget på
[braggster.com/games](/games/).
