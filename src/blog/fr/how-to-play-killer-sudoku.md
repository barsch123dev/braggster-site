---
title: "Killer Sudoku : comment résoudre les cages sans deviner"
slug: how-to-play-killer-sudoku
locale: fr
type: game
category: puzzle
game_id: killersudoku
meta_title: "Killer Sudoku : résoudre les cages sans deviner"
meta_description: "Stratégie du Killer Sudoku : la règle du 45, les combinaisons de cages forcées et les sommes à connaître par coeur. Grilles illimitées, hors ligne et sans pub."
primary_keyword: "killer sudoku règles"
secondary_keywords:
  - "règle du 45 killer sudoku"
  - "combinaisons de cages killer sudoku"
  - "stratégie killer sudoku"
  - "application killer sudoku hors ligne"
  - "sudoku tueur comment jouer"
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

# Killer Sudoku : comment résoudre les cages sans deviner

Le Killer Sudoku ressemble à un Sudoku avec de la décoration en plus, mais se joue comme un
casse-tête complètement différent. La plupart des grilles démarrent avec **très peu de chiffres
donnés, voire aucun**, ce qui est déstabilisant la première fois qu'on en voit une. L'information est
pourtant bien là. Elle est juste écrite sous forme de sommes plutôt que de chiffres.

## Les règles

1. Chaque ligne, chaque colonne et chaque carré de 3x3 contient les chiffres de 1 à 9, chacun une
   seule fois. Comme un Sudoku classique.
2. Les 81 cases sont réparties en **cages**, dessinées avec des bordures en pointillés et une petite
   somme dans un coin.
3. Dans chaque cage, les chiffres sont **distincts** et **totalisent la somme indiquée**.

Cette troisième règle fait un travail énorme, parce qu'une cage a une forme libre plutôt que d'être
une ligne ou un carré, donc la distinction des chiffres n'est pas automatique comme dans un Sudoku
classique. Elle doit être imposée, et c'est ce qui rend les sommes utiles.

## Commence par les cages forcées

Certaines sommes n'ont qu'une seule combinaison possible. C'est de l'information gratuite, et ça doit
être ton premier passage sur n'importe quelle grille.

| Taille de la cage | Somme | Seuls chiffres possibles |
|---|---|---|
| 2 cases | 3 | 1, 2 |
| 2 cases | 4 | 1, 3 |
| 2 cases | 16 | 7, 9 |
| 2 cases | 17 | 8, 9 |
| 3 cases | 6 | 1, 2, 3 |
| 3 cases | 7 | 1, 2, 4 |
| 3 cases | 23 | 6, 8, 9 |
| 3 cases | 24 | 7, 8, 9 |
| 4 cases | 10 | 1, 2, 3, 4 |
| 4 cases | 11 | 1, 2, 3, 5 |
| 4 cases | 29 | 5, 7, 8, 9 |
| 4 cases | 30 | 6, 7, 8, 9 |

Tu ne connais pas encore l'ordre, mais tu connais l'ensemble, et connaître l'ensemble élimine des
candidats partout où ces cases regardent.

## La règle du 45

La technique la plus utile du Killer Sudoku, et la raison pour laquelle les joueurs expérimentés
ouvrent des grilles qui semblent impossibles.

Chaque ligne, chaque colonne et chaque carré contient les chiffres de 1 à 9, donc **la somme vaut
toujours 45**.

Si un ensemble de cages tient entièrement dans une ligne, additionne leurs sommes. La différence avec
45 donne le total des cases restantes de cette ligne. Quand il ne reste qu'une seule case, tu viens de
la résoudre directement.

Ça marche aussi à l'envers : si une cage dépasse d'une case en dehors d'un carré, la somme des cages à
l'intérieur du carré moins 45 te donne la valeur de cette case isolée.

Enchaîne cette méthode sur deux ou trois lignes à la fois, et on l'appelle parfois la méthode « innie
and outie ». C'est le cheval de bataille des grilles Killer difficiles.

## La géométrie des cages compte aussi

Comme les chiffres d'une cage sont distincts, sa forme la contraint encore plus :

- Une cage entièrement dans une seule ligne, colonne ou carré ne peut jamais avoir de répétition, mais
  l'unité non plus, donc rien de nouveau ici. En revanche, une cage **qui s'étend sur deux carrés**
  peut te dire dans quel carré vit un chiffre.
- Une cage de deux cases qui totalise 17 ne peut être que 8 et 9. Si elle se trouve dans une ligne, le
  8 et le 9 de cette ligne sont placés, et toutes les autres cases de la ligne perdent ces deux
  candidats.

## Comment Braggster les génère

Le générateur fait pousser une répartition de cages à partir d'une solution de Sudoku complète, et le
fait **en tenant compte des chiffres**, parce qu'une cage à forme libre n'est pas automatiquement
distincte comme l'est une ligne, une colonne ou un carré. Faire pousser les cages à l'aveugle
produirait des cages avec des répétitions, ce qui n'est pas une cage Killer valide.

Il vérifie ensuite l'unicité en combinant **ensemble** la contrainte du Sudoku et celle des cages, à
l'aide d'un solveur de retour en arrière conscient des cages. Vérifier les deux contraintes
séparément ne suffirait pas : une grille peut être ambiguë avec le Sudoku seul et devenir unique une
fois les cages appliquées, et inversement.

Si une tentative avec peu de chiffres donnés ne peut pas être prouvée unique dans le budget de
recherche imparti, le générateur retombe sur l'ensemble de chiffres donnés déjà vérifié du Sudoku pour
ce niveau. La conséquence, c'est que **chaque grille qui t'est distribuée est réellement soluble de
façon unique**, jamais un peut-être.

## Le plateau

Le plateau Killer réutilise l'anatomie de la grille du Sudoku et ajoute une couche de cages : cinq
teintes, des bordures de cage en pointillés et une somme inscrite dans un coin. Cinq teintes
suffisent pour que deux cages voisines soient toujours différentes sans transformer la grille en
nuancier.

Les aides sont les notes au crayon et les indices. Il n'y a jamais de retour d'erreur en direct dans
aucun casse-tête de Braggster, donc les erreurs sont comptées en silence et révélées dans le résumé de
fin de partie. Le score est le temps de résolution plus une pénalité par erreur et par indice, et le
plus bas gagne.

## Questions fréquentes

**Les chiffres peuvent-ils se répéter dans une cage de Killer Sudoku ?**
Non. Les chiffres d'une cage doivent être distincts, ce qui rend les sommes utiles. C'est l'inverse du
Calcudoku, où les chiffres d'une cage peuvent se répéter.

**Qu'est-ce que la règle du 45 ?**
Chaque ligne, chaque colonne et chaque carré totalise 45. Comparer ce nombre aux cages présentes dans
une unité révèle le total des cases restantes, et résout souvent une case directement.

**Pourquoi les grilles de Killer Sudoku ont-elles si peu de chiffres donnés ?**
Ce sont les cages qui portent la contrainte à la place. Une grille Killer bien construite peut
démarrer avec zéro chiffre donné et avoir quand même exactement une solution.

**Le Killer Sudoku est-il plus difficile que le Sudoku classique ?**
Différent plutôt que strictement plus difficile. Il demande du calcul en plus de la logique, mais les
sommes des cages fournissent une information qu'une grille classique n'a pas.

**Est-ce que les grilles se répètent ?**
Non. Elles sont générées à la demande et vérifiées uniques avant d'être affichées.

---

**En savoir plus :** découvre les treize [casse-têtes de logique](/blog/puzzle-games/), lis notre
article sur [la difficulté au Sudoku](/blog/how-to-play-sudoku/), ou parcours le catalogue sur
[braggster.com/games](/games/).
