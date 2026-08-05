---
title: "Feuilles de score pour jeux de plateau et plateaux jouables"
slug: board-game-score-sheets
locale: fr
type: pillar
category: board
meta_title: "Jeux de plateau : feuilles de score et plateaux jouables"
meta_description: "Comment compter les points aux Dominoes, au Backgammon, au Rummikub et aux échecs, et quels plateaux jouer sur ton téléphone. Local, sans compte."
primary_keyword: "feuille de score jeu de societe"
secondary_keywords:
  - "regles du backgammon"
  - "compter les points aux dominos"
  - "application score jeux de societe"
  - "jouer aux echecs a deux joueurs"
  - "feuille de score rummikub"
search_intent: informational
priority: 1
schema:
  - Article
  - FAQPage
  - ItemList
internal_links:
  - /games/
  - /blog/how-to-score-dominoes/
  - /blog/how-to-score-backgammon/
  - /blog/how-to-score-rummikub/
  - /blog/card-game-score-sheets/
  - /blog/dice-game-score-sheets/
  - /blog/puzzle-games/
trademark_note: "Rummikub, Cluedo et Puissance 4 sont des marques déposées de leurs éditeurs respectifs. Braggster n'est ni affilié ni approuvé par ceux-ci, et chaque nom est utilisé uniquement à titre référentiel."
---

# Feuilles de score pour jeux de plateau et plateaux jouables

Les jeux de plateau se répartissent en deux groupes pas toujours faciles à noter. Certains
produisent un score qui évolue à chaque manche, comme les Dominoes et le Rummikub, et ont besoin
d'une vraie feuille de calcul. D'autres ne produisent rien du tout à l'intérieur d'une seule
partie : les Échecs et le Morpion se terminent, un point c'est tout, et ce que tu veux vraiment
suivre, c'est le décompte sur toute la soirée.

Braggster gère les deux cas, et pour dix jeux de plateau, il te donne aussi le plateau lui-même.

## Les jeux qui comptent un score

**Les Dominoes** filent vers un objectif : 100 points en Block et Draw, 150 en All Fives, calculés
sur les points restant dans la main de tes adversaires. All Fives ajoute un score en cours de
partie chaque fois que les extrémités ouvertes forment un multiple de cinq, et c'est exactement là
qu'une feuille papier commence à dériver.

**Le Rummikub** est un rami de jetons : tu comptes en négatif les jetons qui te restent sur ton
chevalet à la fin d'une manche, et le gagnant récupère le reste. De gros écarts, beaucoup de
calcul, et un cas d'école pour une feuille de score qui additionne à ta place.

**Cluedo** fait bande à part. C'est de la déduction, pas du score, donc Braggster lui donne un
carnet de détective privé plutôt qu'une feuille de score : une colonne pour l'enveloppe solution et
une pour tes notes libres, sur les 21 cartes. Il n'y a pas de colonne par adversaire, parce que
l'app ne distribue ni ne voit jamais la main de personne. C'est ton carnet, sur ton appareil.

Pour aller plus loin : [le score aux Dominoes](/blog/how-to-score-dominoes/),
[le score au Rummikub](/blog/how-to-score-rummikub/).

## Les jeux sans score à l'intérieur d'une partie

Les Échecs, les Dames, les Dames internationales, le Puissance 4 et le Morpion n'ont qu'un seul
résultat possible par partie : quelqu'un gagne, ou c'est nul. Il n'y a aucun nombre à noter.

Braggster traite une partie terminée comme une manche qui vaut une victoire, et le match devient un
décompte de la session. Cela correspond à la façon dont on joue vraiment à ces jeux : pas une seule
partie, mais une série, et ce qui compte, c'est le 5 à 3, pas la position sur le plateau.

Le Backgammon se situe entre les deux. Une partie terminée vaut 1 point pour une victoire simple, 2
pour un gammon et 3 pour un backgammon, et ces points s'additionnent au fil de la session.

Pour aller plus loin : [le score au Backgammon, gammons et backgammons](/blog/how-to-score-backgammon/).

## Les plateaux que tu peux vraiment jouer sur ton téléphone

Dix jeux de plateau dans Braggster se jouent directement sur l'appareil, pas seulement au score :

| Jeu | Ce qu'offre le plateau dans l'app |
|---|---|
| Échecs | Plateau 8x8 en chaise tournante avec l'application intégrale des règles : échec, échec et mat, pat, roque, prise en passant, promotion |
| Dames | Plateau 8x8 en chaise tournante, règles américaines et anglaises, prises forcées et multiples |
| Dames internationales | Plateau 10x10 en chaise tournante, dames volantes, prise maximale obligatoire, cases éliminées une à une |
| Backgammon | Plateau en chaise tournante : lance les dés, touche pour déplacer, prends les bâtons isolés, rentre et sors tes pions |
| Dominoes | Plateau de jetons en chaise tournante : pose sur l'extrémité ouverte correspondante, pioche ou passe selon la variante |
| Puissance 4 | Plateau 7x6 en chaise tournante, touche une colonne et la gravité choisit la ligne |
| Morpion | Grille 3x3 en chaise tournante avec détection automatique de victoire et de match nul |
| Sudoku | Grille générée, cinq niveaux de difficulté |

Chacun de ces plateaux enregistre son résultat par le même circuit qu'une feuille remplie à la
main, donc une partie jouée dans l'app ne peut jamais être comptée différemment d'une partie saisie
manuellement.

## Jouer contre l'ordinateur

Quatre de ces jeux de plateau ont aussi un écran d'entraînement contre un adversaire ordinateur,
chacun avec trois niveaux :

- **Les Échecs** utilisent une recherche alpha bêta avec une évaluation positionnelle des pièces.
  Tu peux jouer les Blancs ou les Noirs, et le plateau se retourne en conséquence.
- **Les Dames** analysent les enchaînements de prises multiples comme le tour unique qu'ils
  représentent réellement.
- **Les Dames internationales** font de même sur le plateau 10x10, où toute une séquence de prises
  compte comme un seul coup.
- **Le Backgammon** ne peut pas du tout utiliser l'alpha bêta, parce que les dés font de chaque
  nœud un nœud de hasard. Il utilise à la place un expectimax sur les vingt et un lancers distincts.

Les quatre tournent sur un thread en arrière-plan pour que le plateau reste réactif pendant que le
moteur réfléchit. Les parties d'entraînement ne sont jamais enregistrées, elles ne viennent donc
jamais fausser tes statistiques ni ton taux de victoire.

## L'accessibilité pensée dès le départ

Sur chaque plateau de Braggster, les pièces se distinguent par leur forme autant que par leur
couleur. Puissance 4 oppose un disque plein à un anneau avec un point central plutôt que du rouge
contre du jaune, parce que la couleur n'est jamais le seul signal dans l'app. Les plateaux à partir
de 12x12 se pincent pour zoomer et se déplacent au doigt plutôt que de réduire les cases en dessous
d'une zone tactile confortable.

## Questions fréquentes

**Deux personnes peuvent-elles jouer sur un seul téléphone ?**
Oui. Les plateaux jouables sont en chaise tournante, tu te passes l'appareil autour de la table. Il
n'y a ni multijoueur en ligne ni compte.

**L'app fonctionne-t-elle pour un jeu de plateau qui n'est pas dans la liste ?**
Oui. La feuille vierge, toujours gratuite, compte les points de n'importe quoi, et il existe aussi
une feuille de score générique pour les jeux de plateau non répertoriés.

**Les parties contre l'ordinateur comptent-elles dans mes statistiques ?**
Non. Les parties d'entraînement contre l'ordinateur ne sont volontairement jamais enregistrées.

**Y a-t-il un cube de doublement au Backgammon ?**
Non. Il n'y a pas de cube de doublement, et rien n'est misé nulle part dans l'app.

**Pourquoi le Sudoku apparaît-il comme jeu de plateau sur certaines pages ?**
Il ne devrait pas. Le Sudoku appartient aux puzzles, avec les onze autres puzzles solo que
Braggster propose désormais. Voir le [guide des puzzles](/blog/puzzle-games/).

---

**Ensuite :** découvre le catalogue complet sur [braggster.com/games](/games/), ou lis les guides
sur les [jeux de cartes](/blog/card-game-score-sheets/), les
[jeux de dés](/blog/dice-game-score-sheets/) et les [puzzles](/blog/puzzle-games/).
