---
title: "Killer Sudoku: come risolvere le gabbie senza indovinare"
slug: how-to-play-killer-sudoku
locale: it
type: game
category: puzzle
game_id: killersudoku
meta_title: "Killer Sudoku: risolvere le gabbie senza indovinare"
meta_description: "Strategia Killer Sudoku: la regola del 45, le combinazioni di gabbia obbligate e le tabelle delle somme da imparare a memoria. Puzzle infiniti, offline."
primary_keyword: "killer sudoku regole"
secondary_keywords:
  - "killer sudoku strategia"
  - "regola del 45 killer sudoku"
  - "killer sudoku combinazioni gabbie"
  - "killer sudoku app offline"
  - "sudoku a somme come si gioca"
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

# Killer Sudoku: come risolvere le gabbie senza indovinare

Killer Sudoku sembra un Sudoku con decorazioni in piu e si gioca come un puzzle completamente
diverso. La maggior parte delle griglie parte con **pochissimi numeri gia dati, o nessuno**, il che
la prima volta e allarmante. L'informazione c'e tutta. E solo scritta come somme invece che come
cifre.

## Le regole

1. Ogni riga, colonna e riquadro 3x3 contiene i numeri da 1 a 9 esattamente una volta. Sudoku
   classico.
2. Le 81 celle sono suddivise in **gabbie**, disegnate con bordi tratteggiati e una piccola somma
   nell'angolo.
3. Le cifre di ogni gabbia sono **distinte** e **sommano al valore indicato**.

Quella terza regola fa un lavoro enorme, perche una gabbia e una forma libera invece che una riga o
un riquadro, quindi la distinzione delle cifre non e automatica come nel Sudoku normale. Va imposta,
ed e proprio questo che rende utili le somme.

## Comincia dalle gabbie obbligate

Alcune somme hanno esattamente una combinazione possibile. Sono informazioni gratuite e dovrebbero
essere il tuo primo passaggio su qualsiasi griglia.

| Celle nella gabbia | Somma | Uniche cifre possibili |
|---|---|---|
| 2 celle | 3 | 1, 2 |
| 2 celle | 4 | 1, 3 |
| 2 celle | 16 | 7, 9 |
| 2 celle | 17 | 8, 9 |
| 3 celle | 6 | 1, 2, 3 |
| 3 celle | 7 | 1, 2, 4 |
| 3 celle | 23 | 6, 8, 9 |
| 3 celle | 24 | 7, 8, 9 |
| 4 celle | 10 | 1, 2, 3, 4 |
| 4 celle | 11 | 1, 2, 3, 5 |
| 4 celle | 29 | 5, 7, 8, 9 |
| 4 celle | 30 | 6, 7, 8, 9 |

Non conosci ancora l'ordine, ma conosci l'insieme, e conoscere l'insieme elimina candidati ovunque
quelle celle guardino.

## La regola del 45

La tecnica piu utile in assoluto nel Killer Sudoku, ed e il motivo per cui i solutori esperti aprono
griglie che sembrano impossibili.

Ogni riga, colonna e riquadro contiene i numeri da 1 a 9, quindi **somma 45**.

Se un insieme di gabbie sta interamente dentro una riga, somma i loro valori. La differenza da 45 e
il totale delle celle rimaste in quella riga. Quando resta esattamente una cella, l'hai appena
risolta del tutto.

Funziona anche al contrario: se una gabbia sporge di una cella fuori da un riquadro, la somma delle
gabbie dentro il riquadro meno 45 ti da il valore di quella cella.

Incatena questo ragionamento su due o tre righe insieme e la tecnica viene talvolta chiamata metodo
"innie and outie". E il cavallo di battaglia delle griglie Killer difficili.

## La geometria della gabbia conta

Poiche le cifre di una gabbia sono distinte, la sua forma la limita ulteriormente:

- Una gabbia dentro una singola riga, colonna o riquadro non puo mai ripetere nulla, e nemmeno
  l'unita puo, quindi non aggiunge niente di nuovo. Ma una gabbia **che attraversa due riquadri** puo
  dirti in quale riquadro vive una certa cifra.
- Una gabbia di due celle che somma 17 deve essere 8 e 9. Se sta in una riga, l'8 e il 9 di quella
  riga sono gia piazzati e ogni altra cella della riga perde entrambi i candidati.

## Come li genera Braggster

Il generatore fa crescere una suddivisione in gabbie a partire da una soluzione Sudoku completa, e lo
fa **tenendo conto delle cifre**, perche una gabbia a forma libera non e automaticamente distinta come
lo e una riga, una colonna o un riquadro. Far crescere le gabbie alla cieca produrrebbe gabbie con
ripetizioni, il che non e una gabbia Killer legale.

Poi verifica l'unicita sotto il vincolo **combinato** di Sudoku e gabbie insieme, usando un solutore a
backtracking che conosce le gabbie. Verificare i due vincoli separatamente non basterebbe: una
griglia puo essere ambigua sotto il solo Sudoku e unica una volta applicate le gabbie, e viceversa.

Se un tentativo con poche celle date non puo essere dimostrato unico entro il budget di ricerca, il
generatore ripiega sull'insieme di numeri dati gia verificato per quel livello nel Sudoku. La
conseguenza e che **ogni puzzle che ricevi e davvero risolvibile in modo unico**, mai forse.

## Il tabellone

Il tabellone Killer riusa la struttura della griglia Sudoku e aggiunge un livello di gabbie: cinque
tinte, bordi tratteggiati delle gabbie e un'etichetta con la somma nell'angolo. Cinque tinte bastano
perche le gabbie adiacenti siano sempre diverse senza trasformare la griglia in un grafico di colori.

Gli aiuti sono appunti a matita e suggerimenti. Non c'e mai un riscontro immediato sugli errori nei
puzzle di Braggster, quindi gli errori vengono contati in silenzio e rivelati nel riepilogo finale. Il
punteggio e il tempo di risoluzione piu una penalita per ogni errore e ogni suggerimento, vince il
totale piu basso.

## Domande frequenti

**Le cifre possono ripetersi in una gabbia di Killer Sudoku?**
No. Le cifre di una gabbia devono essere distinte, ed e questo che rende utili le somme. E il
contrario di Calcudoku, dove le cifre di una gabbia possono ripetersi.

**Cos'e la regola del 45?**
Ogni riga, colonna e riquadro somma 45. Confrontando questo valore con le gabbie dentro un'unita si
scopre il totale delle celle rimaste, e spesso se ne risolve una del tutto.

**Perche i puzzle Killer Sudoku hanno cosi pochi numeri dati?**
Sono le gabbie a portare il vincolo. Una griglia Killer ben costruita puo partire con zero numeri dati
e avere comunque esattamente una soluzione.

**Killer Sudoku e piu difficile del Sudoku normale?**
Diverso piuttosto che strettamente piu difficile. Richiede aritmetica oltre alla logica, ma le somme
delle gabbie forniscono informazioni che una griglia normale non ha.

**I puzzle si ripetono?**
No. Sono generati al momento e verificati come unici prima di essere mostrati.

---

**Continua:** scopri tutti e tredici i [puzzle di logica](/blog/puzzle-games/), leggi della
[difficolta di Sudoku](/blog/how-to-play-sudoku/), oppure sfoglia il catalogo su
[braggster.com/games](/games/).
