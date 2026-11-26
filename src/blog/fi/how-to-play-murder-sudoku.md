---
title: "Murder Sudoku: murhamysteeri, jonka ratkaiset kuin logiikkaruudukon"
slug: how-to-play-murder-sudoku
locale: fi
type: game
category: puzzle
game_id: murdoku
meta_title: "Murder Sudoku: murhamysteeri ratkaistuna logiikalla"
meta_description: "Sijoita neljä epäiltyä ja uhri 5x5-huoneruudukkoon, täytä kaikki vihjeet, ja murhaaja on se, joka on uhrin huoneessa. Loputtomasti uusia tapauksia."
primary_keyword: "murhamysteeri pulmapeli"
secondary_keywords:
  - "päättelypulma sovellus"
  - "murder sudoku"
  - "murhamysteeri yksinpeli"
  - "salapoliisipulma offline"
  - "logiikkapulma päättelyruudukko"
search_intent: informational
priority: 2
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

# Murder Sudoku: murhamysteeri, jonka ratkaiset kuin logiikkaruudukon

Murder Sudoku syntyy, kun salapoliisitarina ja sijoituspulma rakennetaan samaksi esineeksi. Saat
näyttämön, henkilögallerian, uhrin ja numeroidun vihjelistan, ja ratkaiset sen kuin logiikkaruudukon:
et vaistolla siitä, kuka näyttää syylliseltä, vaan poissulkemalla, kunnes jäljelle jää vain yksi
järjestely.

Taustalla ei ole käsin kirjoitettujen tapausten pankkia. Jokainen tapaus luodaan tuoreena,
varmistetaan täsmälleen yksiratkaisuiseksi ja kääritään omaan tarinaansa.

## Miten se toimii

Lauta on **5x5-ruudukko huoneita**. Siinä on neljä epäiltyä ja yksi uhri.

Sijoitussääntö on sudokuosuus: **jokaisella rivillä ja jokaisessa sarakkeessa on enintään yksi
henkilö.** Viisi henkilöä, viisi riviä, viisi saraketta, joten kyse on permutaatiosta, ja jokainen
yhden henkilön lukitseva vihje rajoittaa kaikkia muita.

Sitten vihjeet. Jokaisen epäillyn vihje rajaa, missä hän voi olla, ja kaikkien on pidettävä
paikkansa.

Ratkaisu on järjestely, jossa kaikki pitää paikkansa. Ja sitten palkinto:

**Murhaaja on se, joka päätyy uhrin huoneeseen.**

Tuo viimeinen rivi tekee tästä tarinan eikä abstraktia harjoitusta. Et päättele murhaajaa suoraan.
Päättelet koko pohjapiirroksen, ja murhaaja putoaa siitä ulos.

## Vihjeperheet

Vihjeitä on useita muotoja, ja niiden lukemisen oppiminen on suurin osa taidosta:

- **Suorat tiedot.** Epäilty on tai ei ole nimetyssä huoneessa tai nimetyllä rivillä tai sarakkeessa.
  Helpoin tukipiste, ja siitä kannattaa aina aloittaa.
- **Suhteellinen sijainti.** Yksi epäilty on samassa huoneessa kuin toinen.
- **Ilmansuuntavihjeet.** Epäilty seisoo huonekalun pohjoispuolella, eteläpuolella, itäpuolella tai
  länsipuolella, tai pohjoisempana tai läntisempänä kuin toinen epäilty. Lue nämä huolellisesti:
  käytäntö on kiinteä, pohjoinen on ylhäällä, kuten laudan kompassimerkki näyttää, ja suunnan
  kääntäminen väärin päin tuottaa johdonmukaisen mutta väärän ruudukon.
- **Kielteiset tiedot.** Kukaan ei ole tietyssä huoneessa, tai epäilty ei ole jonkin vieressä.

Vaikeammilla tasoilla suorat tiedot harvenevat ja epäsuorat kantavat suuremman osan taakasta.

## Viisi tasoa

Aloittelija, Helppo, Keskitaso, Vaikea ja Ilkeä, sama tasokaava kuin Sudokussa, Killer Sudokussa ja
Logikwisissa. Taso muuttaa vihjeiden sekoitusta eikä lautaa: vaikeammissa tapauksissa on vähemmän
suoria tietoja ja enemmän vihjeitä, jotka tulevat käyttökelpoisiksi vasta, kun jokin muu on
ratkaistu.

## Jokainen tapaus on yksikäsitteinen ja varmistettu

Generaattori rakentaa tapauksen ja vahvistaa sitten ratkaisijalla, että sillä on **täsmälleen yksi**
kelvollinen järjestely, ennen kuin se kirjoittaa tapauksen kuvauksen.

Sillä on tässä enemmän väliä kuin useimmissa pulmissa, koska moniselitteinen murhamysteeri ei ole
pulma, jolla on kaksi vastausta, vaan tarina ilman loppua. Jos kaksi järjestelyä olisi molemmat
johdonmukaisia, kaksi eri henkilöä olisi molemmat murhaaja.

Koska tapaukset luodaan eikä toimiteta valmiina, tarjonta on rajaton.

## Lauta ja työkalut

Lauta on kuvitettu: epäiltyjen muotokuvamerkit, piirretyt huonekalut ja huoneiden nimet painettuna
ruudukkoon. Se on pohjapiirros, jota luet, ei taulukko.

Sijoittamisen ja pyyhkimisen lisäksi käytössäsi on **muistiinpano- ja yliviivauskerros**, joka on
työkalu, jolla oikeasti ratkaiset. Viivaa yli se, minkä vihje sulkee pois, ja jäljelle jäävät ruudut
ovat vastaus. Vihjeet ovat käytettävissä ja maksavat pisteissä.

Jokainen epäillyn, huoneen ja esineen nimi on omaperäinen. Lainattuja hahmoja tai lainattua kartanoa
ei ole.

## Pisteytys

Ratkaisuaika plus rangaistus jokaisesta virheestä ja jokaisesta vihjeestä. **Pienin kokonaistulos
voittaa**, kuten jokaisessa Braggsterin pulmassa.

Ja kuten sovelluksen muissakin pulmissa, **jatkuvaa palautetta väärästä merkinnästä ei ole**. Sijoita
joku väärään huoneeseen, eikä mikään vilku sinulle. Virheet lasketaan äänettömästi ja paljastetaan
ratkaisuyhteenvedossa. Päättelypulma, joka kertoo, kun olet väärässä, tekee päättelyn puolestasi.

## Nimi

Peli kantoi alun perin nimeä Murdoku. Se julkaistaan nimellä **Murder Sudoku**, koska lyhyemmällä
nimellä on voimassa oleva tavaramerkki. Kuvaileva nimi ei tarvitse tavaramerkkivastuuvapauslauseketta,
ja samasta syystä Killer Sudokua on turvallista käyttää.

## Usein kysytyt kysymykset

**Kuinka iso lauta on?**
5x5 huonetta, neljä epäiltyä ja yksi uhri.

**Miten löydän murhaajan?**
Ratkaise ensin sijoitus. Murhaaja on se epäilty, joka päätyy samaan huoneeseen uhrin kanssa.

**Voiko kaksi epäiltyä olla samalla rivillä?**
Ei. Jokaisella rivillä ja jokaisessa sarakkeessa on enintään yksi henkilö, mikä tekee järjestelystä
permutaation.

**Toistuvatko tapaukset?**
Eivät. Jokainen tapaus luodaan tarpeen mukaan ja varmistetaan täsmälleen yksiratkaisuiseksi, joten
tarjonta on rajaton.

**Millä kielillä se on saatavilla?**
Kaikilla yhdellätoista sovelluksen kielellä. Tarinateksti on kirjoitettu kielikohtaisesti eikä
konekäännetty, joten mysteeri on luonteva jokaisella kielellä.

**Liittyykö se johonkin olemassa olevaan lautapeliin?**
Ei. Jokainen epäillyn, huoneen ja esineen nimi on pelin omaperäinen.

---

**Lisää:** katso kaikki yhdeksäntoista [logiikkapulmaa](/blog/puzzle-games/), lue
[sudokun vaikeustasoista](/blog/how-to-play-sudoku/) tai selaa valikoimaa osoitteessa
[braggster.com/games](/games/).
