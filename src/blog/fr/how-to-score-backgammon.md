---
title: "Comptage au Backgammon : simples, gammons et backgammons"
slug: how-to-score-backgammon
locale: fr
type: game
category: board
game_id: backgammon
meta_title: "Backgammon : comptage, simples, gammons, backgammons"
meta_description: "Ce que vaut chaque victoire au Backgammon : 1 point pour un simple, 2 pour un gammon, 3 pour un backgammon. Plateau jouable et IA en expectimax."
primary_keyword: "regles du backgammon"
secondary_keywords:
  - "comptage backgammon"
  - "qu'est ce qu'un gammon au backgammon"
  - "jouer au backgammon hors ligne"
  - "backgammon contre ordinateur"
  - "regles du jacquet"
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

# Comptage au Backgammon : simples, gammons et backgammons

Le Backgammon est de loin le plus ancien jeu du catalogue de Braggster, et il a le système de
comptage le plus simple de tous. Trois résultats, trois valeurs, et toute la différence entre une
victoire tranquille et une déroute tient à un seul détail : est-ce que ton adversaire a réussi à
sortir un pion.

## Les trois résultats

| Résultat | Valeur | Condition |
|---|---|---|
| **Simple** | 1 point | Le perdant a sorti au moins un pion |
| **Gammon** | 2 points | Le perdant n'a sorti aucun pion |
| **Backgammon** | 3 points | Le perdant n'a sorti aucun pion, et a encore un pion dans le jan intérieur du gagnant ou sur la barre |

C'est tout le système de comptage. Les points s'additionnent partie après partie, et le total le plus
haut mène.

La règle du gammon est ce qui donne au Backgammon sa tension de fin de partie. Un joueur qui perd
clairement ne joue plus pour gagner, il joue pour sortir **un seul pion** avant que son adversaire ne
termine, parce que ça réduit les dégâts de moitié. Voir quelqu'un faire courir un pion isolé jusqu'à
la maison pour éviter un gammon est l'un des moments les plus réellement dramatiques des jeux de
plateau.

## Pourquoi il n'y a pas de cube ici

Le Backgammon sérieux utilise un cube de doublement, qui multiplie l'enjeu en cours de partie et peut
être redoublé. Braggster n'a pas de cube de doublement, et c'est voulu : rien nulle part dans l'app
n'enregistre d'enjeu. Le score est le résultat de la partie, 1, 2 ou 3, et c'est tout.

Si tu joues avec un cube à la maison, note le résultat de chaque partie et garde le cube sur le
plateau.

## Les bases du jeu

Chaque camp a quinze pions qui se déplacent en sens opposés sur vingt-quatre flèches, en cherchant à
tous les amener dans leur propre jan intérieur avant de les sortir.

- Lance deux dés et déplace deux pions, ou un seul pion deux fois.
- **Les doubles jouent quatre fois**, pas deux.
- Une flèche occupée par deux pions adverses ou plus t'est fermée.
- Un pion isolé est exposé. S'il est touché, il va sur la barre, et il doit rentrer dans le jan
  intérieur adverse avant que ce joueur puisse déplacer autre chose.
- Une fois les quinze pions arrivés à la maison, tu commences à les sortir.

## Le plateau jouable

Le Backgammon de Braggster propose un plateau à jouer en te passant le téléphone : lance les deux dés,
touche un pion puis une flèche en surbrillance pour le déplacer, envoie les pions exposés sur la
barre, fais-les rentrer, puis sors-les. La partie terminée s'inscrit directement dans le total en
cours, donc une partie jouée sur le téléphone ne peut jamais donner un score différent d'une partie
notée à la main.

Deux mises en place sont proposées :

- **Standard**, la position de départ habituelle.
- **Nackgammon**, qui recule deux pions pour rendre le début de partie moins basé sur la course et
  plus sur le positionnement.

## L'adversaire ordinateur, et pourquoi il est différent

Le Backgammon propose un écran d'entraînement contre l'ordinateur avec trois niveaux, en jouant les
pions clairs ou foncés.

Ce qui vaut la peine d'être su, c'est qu'il ne peut pas fonctionner comme les autres moteurs de
Braggster. Chess, Checkers et International draughts utilisent tous une recherche alpha-bêta, qui
repose sur le fait que le jeu est déterministe : tu sais exactement quelles positions sont atteignables
à partir d'ici.

Le Backgammon utilise des dés. Chaque nœud de l'arbre est un nœud de hasard, avec vingt et un lancers
distincts à considérer. Le moteur de Backgammon utilise donc une recherche **expectimax** à la place,
qui fait la moyenne de ces lancers plutôt que de supposer que l'adversaire choisit toujours le pire
pour toi. Il tourne sur une tâche en arrière-plan pour que le plateau reste réactif pendant qu'il
réfléchit.

Les parties d'entraînement ne sont jamais enregistrées, donc jouer contre l'ordinateur ne touche
jamais à tes statistiques.

## Questions fréquentes

**Combien de points vaut un gammon ?**
2 points. Un simple vaut 1 et un backgammon vaut 3.

**Quelle est la différence entre un gammon et un backgammon ?**
Les deux exigent que le perdant n'ait sorti aucun pion. C'est un backgammon uniquement si le perdant a
encore un pion sur la barre ou dans le jan intérieur du gagnant à la fin de la partie.

**Les doubles jouent-ils quatre fois au Backgammon ?**
Oui. Un lancer de 5-5 te donne quatre déplacements de cinq, pas deux.

**Y a-t-il un cube de doublement dans l'app ?**
Non. Braggster enregistre uniquement le résultat de la partie, sans aucun enjeu nulle part dans l'app.

**Puis-je jouer au Backgammon hors ligne contre l'ordinateur ?**
Oui. Le moteur tourne entièrement sur ton appareil, sans connexion ni compte requis.

**Qu'est-ce que le Nackgammon ?**
Une position de départ alternative qui recule deux pions plus loin, rendant l'ouverture plus
positionnelle et moins proche d'une simple course. Braggster le propose en plus de la mise en place
standard.

---

**En savoir plus :** découvre tous les jeux sur [braggster.com/games](/games/), ou lis l'aperçu du
[calcul des points aux jeux de plateau](/blog/board-game-score-sheets/).
