---
title: "Killer Sudoku: kuinka ratkaista häkit arvaamatta"
slug: how-to-play-killer-sudoku
locale: fi
type: game
category: puzzle
game_id: killersudoku
meta_title: "Killer Sudoku: kuinka ratkaista häkit arvaamatta"
meta_description: "Killer Sudokun strategia: 45:n sääntö, pakolliset häkkiyhdistelmät ja muistamisen arvoiset summataulukot. Loputtomasti pulmia, offline ja ilman mainoksia."
primary_keyword: "killer sudoku säännöt"
secondary_keywords:
  - "killer sudoku strategia"
  - "45 sääntö killer sudoku"
  - "killer sudoku häkit yhdistelmät"
  - "killer sudoku sovellus offline"
  - "summasudoku miten pelataan"
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

# Killer Sudoku: kuinka ratkaista häkit arvaamatta

Killer Sudoku näyttää sudokulta, johon on lisätty koristeita, mutta pelaa aivan eri tavalla.
Ruudukoissa on alussa **paljon vähemmän annettuja numeroita kuin tavallisessa sudokussa**, mikä
hätkähdyttää ensimmäisellä kerralla. Tieto on silti kaikki tallella. Se on vain kirjoitettu summina
numeroiden sijaan.

## Säännöt

1. Jokaisella rivillä, sarakkeessa ja 3x3-laatikossa on numerot 1-9 täsmälleen kerran. Tavallinen
   sudoku.
2. 81 ruutua on jaettu **häkkeihin**, jotka on piirretty katkoviivareunoin ja joiden kulmassa on pieni
   summa.
3. Jokaisen häkin numerot ovat **erilaisia** ja niiden **summa on häkin summa**.

Kolmas sääntö tekee valtavan paljon työtä, sillä häkki on vapaamuotoinen alue eikä rivi tai laatikko,
joten erilaisuus ei synny itsestään kuten tavallisessa sudokussa. Se on asetettava erikseen, ja juuri
se tekee summista informatiivisia.

## Aloita pakollisista häkeistä

Joillakin summilla on täsmälleen yksi mahdollinen yhdistelmä. Tämä on ilmaista tietoa, ja sen pitäisi
olla ensimmäinen asia, jota etsit mistä tahansa ruudukosta.

| Häkin koko | Summa | Ainoat mahdolliset numerot |
|---|---|---|
| 2 ruutua | 3 | 1, 2 |
| 2 ruutua | 4 | 1, 3 |
| 2 ruutua | 16 | 7, 9 |
| 2 ruutua | 17 | 8, 9 |
| 3 ruutua | 6 | 1, 2, 3 |
| 3 ruutua | 7 | 1, 2, 4 |
| 3 ruutua | 23 | 6, 8, 9 |
| 3 ruutua | 24 | 7, 8, 9 |
| 4 ruutua | 10 | 1, 2, 3, 4 |
| 4 ruutua | 11 | 1, 2, 3, 5 |
| 4 ruutua | 29 | 5, 7, 8, 9 |
| 4 ruutua | 30 | 6, 7, 8, 9 |

Et vielä tiedä järjestystä, mutta tiedät joukon, ja joukon tunteminen poistaa ehdokkaita kaikkialta,
minne nuo ruudut näkevät.

## 45:n sääntö

Killer Sudokun hyödyllisin yksittäinen tekniikka ja syy siihen, miksi kokeneet ratkaisijat avaavat
ruudukoita, jotka näyttävät mahdottomilta.

Jokaisessa rivissä, sarakkeessa ja laatikossa on luvut 1-9, joten sen **summa on 45**.

Jos joukko häkkejä mahtuu kokonaan yhdelle riville, laske niiden summat yhteen. Ero 45:een on
kyseisen rivin jäljelle jäävien ruutujen yhteissumma. Kun jäljelle jää täsmälleen yksi ruutu, olet
juuri ratkaissut sen suoraan.

Sama toimii myös toisin päin: jos häkki pistää yhden ruudun verran ulos laatikosta, laatikon sisällä
olevien häkkien summa miinus 45 kertoo tuon yhden ruudun arvon.

Kun ketjutat tätä kahden tai kolmen rivin yli kerralla, tekniikkaa kutsutaan joskus "sisään ja ulos"
-menetelmäksi (innie and outie). Se on vaikeiden Killer-ruudukoiden työjuhta.

## Häkin muoto vaikuttaa

Koska häkin numerot ovat erilaisia, sen muoto rajaa sitä edelleen:

- Häkki, joka on kokonaan yhdellä rivillä, sarakkeessa tai laatikossa, ei voi koskaan toistaa
  numeroa, eikä yksikkökään voi, joten mitään uutta ei synny. Mutta **kahteen laatikkoon ulottuva**
  häkki voi kertoa, missä laatikossa jokin numero on.
- Kahden ruudun häkki, jonka summa on 17, on 8 ja 9. Jos se on yhdellä rivillä, rivin 8 ja 9 on
  sijoitettu, ja jokainen muu rivin ruutu menettää molemmat ehdokkaat.

## Miten Braggster luo ne

Generaattori kasvattaa häkkijaon valmiin sudokuratkaisun päälle ja tekee sen **numerotietoisesti**,
koska vapaamuotoinen häkki ei ole automaattisesti erilaisia numeroita sisältävä kuten rivi, sarake
tai laatikko. Häkkien kasvattaminen sokkona tuottaisi häkkejä, joissa on toistoja, eikä se ole
laillinen Killer-häkki.

Sen jälkeen se varmistaa ratkaisun yksikäsitteisyyden sudokun ja häkkien **yhdistetyllä** ehdolla
häkkitietoisella peruutusratkaisijalla. Ehtojen tarkistaminen erikseen ei riittäisi: ruudukko voi
olla moniselitteinen pelkän sudokun kannalta ja yksikäsitteinen häkkien kanssa, ja päinvastoin.

Se aloittaa jo valmiiksi yksikäsitteisestä sudokun annettujen numeroiden joukosta ja poistaa
annettuja numeroita yksi kerrallaan, ja poisto jää voimaan vain, jos ratkaisija todistaa pulmalla
olevan yhä täsmälleen yksi ratkaisu pienen hakubudjetin sisällä. Annettu numero, jonka
tarpeettomuutta se ei pysty todistamaan, säilyy. Siksi lukumäärä pienenee tason mukana: noin 32
Aloittelijalla, 24 Helpolla, 16 Keskitasolla ja noin tusina Vaikealla ja Paholla, joissa häkitkin
ovat isompia. Seurauksena **jokainen jaettu pulma on aidosti yksikäsitteisesti ratkaistavissa**,
ei koskaan "ehkä".

## Pelilauta

Killer-lauta käyttää uudelleen sudokun ruudukon rakennetta ja lisää häkkikerroksen: viisi sävyä,
katkoviivahäkkireunat ja kulmassa summa. Viisi sävyä riittää siihen, että vierekkäiset häkit
eroavat aina toisistaan, ilman että ruudukosta tulee värikarttaa.

Apuvälineet ovat kynämuistiinpanot ja vihjeet. Braggsterin pulmissa ei ole missään jatkuvaa
palautetta väärästä merkinnästä, joten virheet lasketaan äänettömästi ja paljastetaan
ratkaisuyhteenvedossa. Pisteytys on ratkaisuaika plus rangaistus jokaisesta virheestä ja vihjeestä,
pienin tulos voittaa.

## Usein kysytyt kysymykset

**Voivatko numerot toistua Killer Sudokun häkin sisällä?**
Eivät. Häkin numeroiden on oltava erilaisia, ja juuri se tekee summista hyödyllisiä. Tämä on
päinvastoin kuin Calcudokussa, jossa häkin numerot saavat toistua.

**Mikä on 45:n sääntö?**
Jokaisen rivin, sarakkeen ja laatikon summa on 45. Kun sitä vertaa yksikön sisällä oleviin häkkeihin,
saa selville jäljelle jäävien ruutujen yhteissumman, ja usein yhden ruudun suoraan ratkaistua.

**Miksi Killer Sudoku -pulmissa on niin vähän annettuja numeroita?**
Häkit kantavat osan ehdoista. Hyvin rakennettu Killer-ruudukko voi alkaa nollalla annetulla
numerolla ja silti olla täsmälleen yksi ratkaisu, ja Braggsterissa lukumäärä laskee noin 32:sta
Aloittelijalla noin tusinaan Pahalla.

**Onko Killer Sudoku vaikeampi kuin tavallinen sudoku?**
Erilainen pikemmin kuin tiukasti vaikeampi. Se vaatii logiikan rinnalle laskemista, mutta häkkien
summat antavat tietoa, jota tavallisessa ruudukossa ei ole.

**Toistuvatko pulmat?**
Eivät. Ne luodaan tuoreina tarpeen mukaan ja varmistetaan yksikäsitteisiksi ennen kuin ne näytetään.

---

**Lisää:** katso kaikki yhdeksäntoista [logiikkapulmaa](/blog/puzzle-games/), lue
[sudokun vaikeustasoista](/blog/how-to-play-sudoku/) tai selaa valikoimaa osoitteessa
[braggster.com/games](/games/).
