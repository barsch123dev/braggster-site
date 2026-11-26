---
title: "Backgammonin pisteytys: tavallinen voitto, gammon ja backgammon"
slug: how-to-score-backgammon
locale: fi
type: game
category: board
game_id: backgammon
meta_title: "Backgammonin pisteytys: voitto, gammon, backgammon"
meta_description: "Mitä backgammon-voitto on arvoltaan: 1 tavallisesta, 2 gammonista, 3 backgammonista. Lisäksi pelattava lauta ja tietokonevastustaja, joka käyttää expectimaxia."
primary_keyword: "backgammon pisteytys"
secondary_keywords:
  - "mikä on gammon backgammonissa"
  - "backgammon säännöt"
  - "pelaa backgammonia offline"
  - "backgammon pistelasku"
  - "backgammon tietokonetta vastaan"
  - "backgammon verkossa kavereiden kanssa"
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

# Backgammonin pisteytys: tavallinen voitto, gammon ja backgammon

Backgammon on Braggsterin valikoiman ylivoimaisesti vanhin peli, ja sillä on niistä selkein
pisteytys. Kolme lopputulosta, kolme arvoa, ja koko ero tavallisen voiton ja murskaavan voiton välillä
on siinä, saiko vastustaja yhdenkään nappulan kotiin.

## Kolme tulosta

| Tulos | Arvo | Ehto |
|---|---|---|
| **Tavallinen voitto** | 1 piste | Häviäjä on vienyt pois vähintään yhden nappulan |
| **Gammon** | 2 pistettä | Häviäjä ei ole vienyt pois yhtään nappulaa |
| **Backgammon** | 3 pistettä | Häviäjä ei ole vienyt pois yhtään nappulaa, ja hänellä on yhä nappula voittajan kotialueella tai palkilla |

Siinä koko pisteytysjärjestelmä. Pisteet kertyvät peleistä käynnissä olevaksi summaksi, ja korkein
summa johtaa.

Gammon-sääntö antaa backgammonin loppupelille sen jännityksen. Selvästi häviöllä oleva pelaaja ei
enää pelaa voittaakseen vaan viedäkseen pois **yhden ainoan nappulan**, ennen kuin vastustaja
valmistuu, koska se puolittaa vahingon. Yksinäisen nappulan kilpajuoksun seuraaminen kotiin gammonin
välttämiseksi on yksi lautapelien aidosti jännittävimmistä hetkistä.

## Miksi tässä ei ole tuplauskuutiota

Vakavassa backgammonissa käytetään tuplauskuutiota, joka kertoo panoksen kesken pelin ja jonka voi
tuplata uudelleen. Braggsterissa ei ole tuplauskuutiota, ja se on tarkoituksellista: mikään
sovelluksessa ei kirjaa panosta. Pisteet ovat pelin tulos, 1, 2 tai 3, eikä muuta.

Jos pelaat kotona kuutiolla, kirjaa jokaisen pelin tulos ja pidä kuutio laudalla.

## Pelaamisen perusteet

Kummallakin puolella on viisitoista nappulaa, jotka liikkuvat vastakkaisiin suuntiin kahdenkymmenenneljän
pisteen ympäri, ja tavoitteena on saada ne kaikki omalle kotialueelle ja viedä sitten pois laudalta.

- Heitä kaksi noppaa ja siirrä kahta nappulaa tai yhtä nappulaa kahdesti.
- **Tuplat pelataan neljä kertaa**, ei kahta.
- Piste, jota pitää kaksi tai useampi vastustajan nappula, on sinulle suljettu.
- Yksinäinen nappula on **blot**. Jos siihen osuu, se menee palkille, ja sen on tultava takaisin
  vastustajan kotialueelle, ennen kuin kyseinen pelaaja voi siirtää mitään muuta.
- Kun kaikki viisitoista ovat kotona, alat viedä niitä pois.

## Pelattava lauta

Braggsterin Backgammonissa on yhden laitteen lauta: heitä kaksi noppaa, napauta nappulaa ja sitten
korostettua pistettä siirtääksesi sen, osu blotteihin palkille, tule takaisin ja vie nappulat pois.
Valmis peli kirjautuu suoraan käynnissä olevaan summaan, joten puhelimella pelattu peli ei voi koskaan
pisteytyä eri tavalla kuin käsin kirjattu.

Tuettuja aloituksia on kaksi:

- **Perus**, tavallinen aloitusasetelma.
- **Nackgammon**, joka siirtää kaksi nappulaa taaemmas, jolloin alkupeli on vähemmän kilpajuoksua ja
  enemmän asemapeliä.

## Pelatkaa yhdessä kahdella puhelimella, lähellä tai verkossa

Voit pelata myös niin, että kummallakin on oma puhelin. [Pelatkaa yhdessä](/play-together/) -toiminnolla
yksi puhelin aloittaa pöydän ja näyttää QR-koodin, toinen skannaa sen, ja molemmat pelaajat näkevät
saman laudan livenä. Kumpikin heittää ja siirtää omalta puhelimeltaan, viimeinen siirto on merkitty
molemmilla laudoilla, ja valmis peli kirjaa 1, 2 tai 3 pistettä summaan molemmille puhelimille. Samassa
Wi-Fissä verkkoyhteyttä ei tarvita, ja jos haluat pelata backgammonia verkossa kaverin kanssa muualla,
lähetä kutsulinkki tai 8 merkin koodi. Tiliä ei tarvita, ja vain isännällä on oltava peli. [Opas
usealla puhelimella pelaamiseen](/blog/play-games-together-on-multiple-phones/) käy sen läpi vaihe
vaiheelta.

## Tietokonevastustaja ja miksi se on erilainen

Backgammonissa on harjoitusnäkymä tietokonetta vastaan kolmella tasolla, ja pelaat joko Vaaleana tai
Tummana.

Tärkeää on tietää, että se ei voi toimia samoin kuin Braggsterin muut moottorit. Shakki, Checkers,
kansainvälinen dammi ja Othello käyttävät kaikki alfa-beta-hakua, joka perustuu siihen, että peli on
deterministinen: tiedät täsmälleen, mihin asemiin täältä pääsee.

Backgammonissa on nopat. Jokainen puun solmu on satunnaissolmu, ja huomioitavia heittoja on
kaksikymmentäyksi erilaista. Siksi backgammon-moottori ajaa **expectimax**-haun, joka laskee
keskiarvon näiden heittojen yli sen sijaan, että olettaisi vastustajan valitsevan sinulle pahimman.
Se toimii taustasäikeessä, joten lauta pysyy ohjattavana sen miettiessä.

Harjoituspelejä ei koskaan tallenneta, joten tietokonetta vastaan pelaaminen ei kosketa tilastojasi.

## Usein kysytyt kysymykset

**Montako pistettä gammon on arvoltaan?**
2 pistettä. Tavallinen voitto on 1 ja backgammon 3.

**Mitä eroa on gammonilla ja backgammonilla?**
Molemmat edellyttävät, ettei häviäjä ole vienyt pois yhtään nappulaa. Kyseessä on backgammon vain,
jos häviäjällä on pelin päättyessä yhä nappula palkilla tai voittajan kotialueella.

**Pelataanko tuplat backgammonissa neljä kertaa?**
Kyllä. Heitto 5-5 antaa neljä viiden siirtoa, ei kahta.

**Onko sovelluksessa tuplauskuutio?**
Ei. Braggster kirjaa vain pelin tuloksen, eikä sovelluksessa ole missään panosta.

**Voinko pelata backgammonia offline tietokonetta vastaan?**
Kyllä. Moottori toimii kokonaan laitteellasi, ilman verkkoyhteyttä ja ilman tiliä.

**Voiko kaksi ihmistä pelata backgammonia kahdella puhelimella tai verkossa?**
Kyllä. Pelatkaa yhdessä -toiminnolla jokainen pelaaja käyttää omaa puhelintaan. Toinen aloittaa pöydän,
toinen skannaa sen koodin, ja peli etenee livenä molemmilla näytöillä. Samassa Wi-Fissä verkkoyhteyttä
ei tarvita, ja muualla olevat kaverit liittyvät verkossa kutsulinkillä tai 8 merkin koodilla.

**Mikä on Nackgammon?**
Aloitusasetelman muunnelma, joka vetää kaksi nappulaa kauemmas taakse, jolloin alkupeli on
asemapainotteisempi eikä pelkkää kilpajuoksua. Braggster tukee sitä tavallisen aloituksen rinnalla.

---

**Lisää:** selaa kaikkia pelejä osoitteessa [braggster.com/games](/games/) tai lue
[lautapelien pisteytyksen yleiskatsaus](/blog/board-game-score-sheets/).
