---
title: "Punteggio a Backgammon: singole, gammon e backgammon"
slug: how-to-score-backgammon
locale: it
type: game
category: board
game_id: backgammon
meta_title: "Punteggio a Backgammon: singole, gammon, backgammon"
meta_description: "Quanto vale una vittoria a backgammon: 1 per una singola, 2 per un gammon, 3 per un backgammon. Con tabellone giocabile e avversario expectimax."
primary_keyword: "regole del backgammon"
secondary_keywords:
  - "punteggio backgammon"
  - "cos'è un gammon nel backgammon"
  - "giocare a backgammon offline"
  - "punteggio partita backgammon"
  - "backgammon contro il computer"
  - "giocare a backgammon online con gli amici"
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

# Punteggio a Backgammon: singole, gammon e backgammon

Backgammon è il gioco più antico nel catalogo di Braggster con ampio margine, e ha il sistema di
punteggio più pulito di tutti. Tre risultati, tre valori, e l'intera differenza tra una vittoria
tranquilla e una schiacciante sta nel fatto che l'avversario sia riuscito a portare a casa una pedina
o no.

## I tre risultati

| Risultato | Valore | Condizione |
|---|---|---|
| **Singola** | 1 punto | Chi perde ha già portato a casa almeno una pedina |
| **Gammon** | 2 punti | Chi perde non ha portato a casa nessuna pedina |
| **Backgammon** | 3 punti | Chi perde non ha portato a casa nessuna pedina, e ha ancora una pedina nella casa del vincitore o sulla barra |

Questo è l'intero sistema di punteggio. I punti si accumulano tra le partite in un conteggio
progressivo e vince il totale più alto.

La regola del gammon è ciò che dà al backgammon la sua tensione di fine partita. Un giocatore che sta
chiaramente perdendo non gioca più per vincere, gioca per portare a casa **una sola pedina** prima
che l'avversario finisca, perché così dimezza il danno. Guardare qualcuno correre con l'ultima pedina
per salvarsi da un gammon è una delle cose più autenticamente drammatiche nei giochi da tavolo.

## Perché qui non c'è il dado raddoppiante

Il backgammon serio usa un dado raddoppiante, che moltiplica la posta a metà partita e può essere
rilanciato. Braggster non ha nessun dado raddoppiante, ed è una scelta deliberata: in nessuna parte
dell'app viene registrata una posta. Il punteggio è il risultato della partita, 1, 2 o 3, e questo è
tutto.

Se a casa giochi con il dado, registra il risultato di ogni partita e tieni il dado sul tabellone.

## Le basi del gioco

Ogni lato ha quindici pedine che si muovono in direzioni opposte lungo ventiquattro punti, con
l'obiettivo di portarle tutte nella propria casa e poi farle uscire.

- Tira due dadi e muovi due pedine, oppure una pedina due volte.
- **I doppi si giocano quattro volte**, non due.
- Un punto occupato da due o più pedine dell'avversario è chiuso per te.
- Una pedina sola è una **pedina isolata**. Se ci atterri sopra va sulla barra, e deve rientrare nella
  casa dell'avversario prima che quel giocatore possa muovere qualsiasi altra cosa.
- Una volta che tutte e quindici sono a casa, cominci a portarle fuori.

## Il tabellone giocabile

Il Backgammon di Braggster include un tabellone hotseat: tira i due dadi, tocca una pedina e poi il
punto evidenziato per muoverla, colpisci le pedine isolate mandandole sulla barra, rientra e porta le
pedine a casa. La partita finita si registra direttamente nel conteggio progressivo, quindi una
partita giocata dal telefono non può mai avere un punteggio diverso da una registrata a mano.

Sono supportate due aperture:

- **Standard**, la posizione di partenza normale.
- **Nackgammon**, che sposta indietro due pedine per rendere l'inizio partita meno una corsa e più
  posizionale.

## Gioca insieme su due telefoni, vicini o online

Puoi anche giocare con un telefono a testa. Con [Gioca insieme](/play-together/), un telefono apre
un tavolo e mostra un codice QR, l'altro lo scansiona, ed entrambi i giocatori vedono lo stesso tabellone dal vivo. Ognuno tira e muove dal proprio telefono, l'ultima mossa
resta segnata su entrambi i tabelloni, e la partita finita segna 1, 2 o 3 punti nel conteggio su
entrambi i telefoni. Sulla stessa rete Wi-Fi non serve internet, e per giocare a backgammon online con amici lontani basta mandare un link di invito o il codice di 8 caratteri. Non serve nessun account, e solo l'host deve avere il gioco. La [guida per giocare insieme su più telefoni](/blog/play-games-together-on-multiple-phones/)
spiega tutti i passaggi.

## L'avversario del computer, e perché è diverso

Backgammon ha una modalità di allenamento contro il computer su tre livelli, giocando con le pedine
Chiare o Scure.

Vale la pena sapere che non può funzionare come gli altri motori di Braggster. Chess, Checkers,
International draughts e Othello usano tutti la ricerca alpha beta, che si basa sul fatto che il
gioco sia deterministico: sai esattamente quali posizioni sono raggiungibili da qui.

Backgammon ha i dadi. Ogni nodo dell'albero è un nodo di probabilità, con ventuno tiri distinti da
considerare. Così il motore del backgammon usa invece una ricerca **expectimax**, facendo la media su
quei tiri invece di supporre che l'avversario scelga il peggiore per te. Gira su un processo in
background così il tabellone resta reattivo mentre pensa.

Le partite di allenamento non vengono mai registrate, quindi giocare contro il computer non tocca le
tue statistiche.

## Domande frequenti

**Quanti punti vale un gammon?**
2 punti. Una singola vale 1 e un backgammon vale 3.

**Qual è la differenza tra un gammon e un backgammon?**
In entrambi chi perde non deve aver portato a casa nulla. È un backgammon solo se chi perde ha ancora
una pedina sulla barra o nella casa del vincitore quando la partita finisce.

**I doppi si muovono quattro volte nel backgammon?**
Sì. Tirare 5-5 ti dà quattro mosse da cinque, non due.

**C'è il dado raddoppiante nell'app?**
No. Braggster registra solo il risultato della partita, senza nessuna posta in nessuna parte
dell'app.

**Posso giocare a backgammon offline contro il computer?**
Sì. Il motore gira interamente sul tuo dispositivo, senza bisogno di connessione né di account.

**Possono giocare due persone a backgammon su due telefoni, anche online?**
Sì. Con Gioca insieme ogni giocatore usa il proprio telefono. Uno apre un tavolo, l'altro scansiona il suo codice, e la partita si svolge dal vivo su entrambi gli schermi. Sulla stessa rete Wi-Fi non serve internet; gli amici lontani si uniscono online con un link di invito o il codice di 8 caratteri.

**Cos'è il Nackgammon?**
Una posizione di partenza alternativa che arretra due pedine, rendendo l'apertura più posizionale e
meno una corsa pura. Braggster la supporta accanto all'apertura standard.

---

**Continua:** sfoglia ogni gioco su [braggster.com/games](/games/), oppure leggi la panoramica del
[punteggio nei giochi da tavolo](/blog/board-game-score-sheets/).
