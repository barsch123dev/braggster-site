---
title: "Backgammon Scoren: Enkel, Gammon en Backgammon"
slug: how-to-score-backgammon
locale: nl
type: game
category: board
game_id: backgammon
meta_title: "Backgammon Scoren: Enkel, Gammon en Backgammon"
meta_description: "Wat een backgammonoverwinning waard is: 1 punt voor enkel, 2 voor een gammon, 3 voor een backgammon. Plus een speelbaar bord met computertegenstander."
primary_keyword: "backgammon scoren"
secondary_keywords:
  - "wat is een gammon bij backgammon"
  - "backgammon spelregels"
  - "backgammon offline spelen"
  - "backgammon puntentelling"
  - "backgammon tegen de computer"
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

# Backgammon Scoren: Enkel, Gammon en Backgammon

Backgammon is met afstand het oudste spel in de catalogus van Braggster, en het heeft het duidelijkste
scoresysteem van allemaal. Drie uitkomsten, drie waarden, en het hele verschil tussen een gewone winst
en een verpletterende zit in de vraag of je tegenstander een steen thuis kreeg.

## De drie uitkomsten

| Resultaat | Waarde | Voorwaarde |
|---|---|---|
| **Enkel** | 1 punt | De verliezer heeft minstens één steen uitgebordeld |
| **Gammon** | 2 punten | De verliezer heeft geen enkele steen uitgebordeld |
| **Backgammon** | 3 punten | De verliezer heeft niets uitgebordeld, en heeft nog een steen in het thuisbord van de winnaar of op de bar |

Dat is het complete scoresysteem. Punten stapelen zich op over meerdere potjes als een lopende stand,
en het hoogste totaal staat voor.

De gammonregel geeft backgammon zijn spanning aan het einde. Een speler die duidelijk verliest speelt
niet meer om te winnen, maar om **één enkele steen** uit te bordelen voordat de tegenstander klaar is,
omdat dat de schade halveert. Iemand een eenzame steen naar huis zien racen om een gammon te
voorkomen is een van de echt dramatische momenten in bordspellen.

## Waarom er hier geen dobbelverdubbelaar is

Serieus backgammon gebruikt een dobbelverdubbelaar, die de inzet halverwege het spel vermenigvuldigt
en opnieuw verdubbeld kan worden. Braggster heeft geen dobbelverdubbelaar, en dat is bewust: er wordt
nergens in de app een inzet geregistreerd. De score is het resultaat van het potje, 1, 2 of 3, en
meer is het niet.

Speel je thuis met een verdubbelaar, noteer dan het resultaat van elk potje en houd de verdubbelaar
apart bij het bord.

## De basis van het spel

Elke kant heeft vijftien stenen die in tegenovergestelde richtingen over vierentwintig punten
bewegen, met als doel ze allemaal naar het eigen thuisbord te krijgen en dan uit te bordelen.

- Gooi twee dobbelstenen en zet twee stenen, of één steen twee keer.
- **Dubbels tellen vier keer**, niet twee keer.
- Een punt bezet door twee of meer stenen van je tegenstander is voor jou gesloten.
- Een eenzame steen is een **blot**. Land erop en hij gaat naar de bar, en moet weer binnenkomen in
  het thuisbord van de tegenstander voordat die speler iets anders mag zetten.
- Zodra alle vijftien thuis zijn, begin je met uitbordelen.

## Het speelbare bord

Backgammon van Braggster heeft een hotseat-bord: gooi de twee dobbelstenen, tik een steen aan en dan
een gemarkeerd punt om hem te verplaatsen, sla blots naar de bar, kom weer binnen, en bordel uit. Het
afgeronde potje scoort rechtstreeks in de lopende stand, dus een potje dat op de telefoon gespeeld is
kan nooit anders scoren dan een handmatig genoteerd potje.

Twee openingen worden ondersteund:

- **Standaard**, de gewone startpositie.
- **Nackgammon**, waarbij twee stenen verder naar achteren staan, wat het beginspel minder een race en
  meer positioneel maakt.

## De computertegenstander, en waarom die anders is

Backgammon heeft een oefenscherm tegen de computer met drie niveaus, spelend als Licht of Donker.

Wat de moeite waard is om te weten: dit kan niet werken zoals de andere engines in Braggster. Chess,
Checkers en International draughts gebruiken allemaal alpha-beta zoekstrategie, die erop leunt dat het
spel deterministisch is: je weet precies welke stellingen vanaf hier bereikbaar zijn.

Backgammon heeft dobbelstenen. Elk knooppunt in de boom is een kansknooppunt, met eenentwintig
verschillende worpen om te overwegen. Daarom draait de backgammon-engine in plaats daarvan een
**expectimax**-zoekstrategie, die middelt over die worpen in plaats van aan te nemen dat de
tegenstander de slechtste voor jou kiest. Hij draait op een achtergrondthread, zodat het bord soepel
blijft terwijl hij nadenkt.

Oefenpotjes worden nooit opgeslagen, dus tegen de computer spelen raakt je statistieken niet.

## Veelgestelde vragen

**Hoeveel punten is een gammon waard?**
2 punten. Een enkele overwinning is 1 en een backgammon is 3.

**Wat is het verschil tussen een gammon en een backgammon?**
Bij allebei moet de verliezer niets uitgebordeld hebben. Het is alleen een backgammon als de verliezer
nog een steen op de bar of in het thuisbord van de winnaar heeft als het potje eindigt.

**Tellen dubbels vier keer bij backgammon?**
Ja. Een worp van 5-5 geeft je vier zetten van vijf, niet twee.

**Is er een dobbelverdubbelaar in de app?**
Nee. Braggster registreert alleen het resultaat van het potje, zonder dat er ergens in de app iets op
het spel staat.

**Kan ik offline tegen de computer backgammon spelen?**
Ja. De engine draait volledig op je toestel, geen verbinding en geen account nodig.

**Wat is Nackgammon?**
Een variantstartpositie waarbij twee stenen verder naar achteren staan, wat de opening meer
positioneel en minder een rechttoe-rechtaan race maakt. Braggster ondersteunt hem naast de standaard
opening.

---

**Meer:** blader door elk spel op [braggster.com/games](/games/), of lees het overzicht van
[bordspel scoren](/blog/board-game-score-sheets/).
