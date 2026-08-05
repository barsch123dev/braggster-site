---
title: "Comptage des points au Bridge : contrats, vulnérabilité et robres"
slug: how-to-score-bridge
locale: fr
type: game
category: card
game_id: bridge
meta_title: "Bridge : comptage des points, contrats et vulnérabilité"
meta_description: "Comment compter les points au bridge : valeur des levées, manches, chelems, contre et vulnérabilité, avec une feuille qui fait le calcul pour toi."
primary_keyword: "comment compter les points au bridge"
secondary_keywords:
  - "bridge comptage des points"
  - "regles du bridge vulnerabilite"
  - "feuille de score bridge"
  - "chelem bridge points"
  - "application score jeux de societe"
search_intent: informational
priority: 2
schema:
  - Article
  - FAQPage
  - HowTo
internal_links:
  - /games/
  - /blog/card-game-score-sheets/
trademark_note: null
---

# Comptage des points au Bridge : contrats, vulnérabilité et robres

Le bridge a la feuille de score la plus intimidante des jeux de cartes, et cette réputation n'est
qu'à moitié méritée. Le calcul n'est pas tant compliqué que **construit en couches** : une valeur de
levée, puis une série de bonus par dessus, puis un multiplicateur, puis une autre série de nombres
selon que tu es vulnérable ou non.

Une fois que tu vois ces couches séparément, ça cesse d'être un exercice de mémoire.

## Première couche : le contrat lui-même

Les enchères se terminent sur un contrat : un nombre de levées au dessus de six, et une couleur
d'atout ou sans atout. « Quatre cœurs » veut dire que le camp déclarant s'est engagé à remporter dix
levées avec cœur comme atout.

Réussir le contrat rapporte par levée demandée, selon ce barème :

| Couleur | Par levée demandée |
|---|---|
| Trèfle ou carreau (mineures) | 20 |
| Cœur ou pique (majeures) | 30 |
| Sans atout | 40 pour la première, 30 pour chaque suivante |

Donc quatre cœurs réussi, c'est 4 x 30 = 120 sous la ligne. Trois sans atout, c'est 40 + 30 + 30 =
100.

## Deuxième couche : le seuil de la manche

**100 points sous la ligne font une manche.** Ce seul nombre explique la majeure partie de la
théorie des enchères.

- Trois sans atout, c'est exactement 100. Manche.
- Quatre cœurs ou quatre piques, c'est 120. Manche.
- Cinq trèfles ou cinq carreaux, c'est 100. Manche aussi, mais il faut onze levées, ce qui explique
  pourquoi on évite les manches à une couleur mineure quand trois sans atout est possible.

Tout ce qui n'atteint pas 100 est un score partiel, et les scores partiels s'accumulent jusqu'à ce
que quelqu'un fasse une manche.

## Troisième couche : la vulnérabilité

Une fois qu'un camp a fait une manche, il devient **vulnérable**. La vulnérabilité ne change pas ce
que tu marques pour réussir un contrat. Elle change les bonus et, plus important encore, les
pénalités :

| | Non vulnérable | Vulnérable |
|---|---|---|
| Bonus de manche | 300 | 500 |
| Petit chelem (12 levées) | 500 | 750 |
| Grand chelem (13 levées) | 1000 | 1500 |
| Chute non contrée | 50 chacune | 100 chacune |

Être vulnérable double à peu près le coût d'une chute, ce qui fait du sacrifice une vraie décision
plutôt qu'une option gratuite.

## Quatrième couche : le contre

Un contre multiplie le score de levées et durcit nettement les pénalités. Un surcontre le multiplie
encore. Un contrat contré qui réussit rapporte en plus une prime pour l'insulte, et un contrat
contré qui chute grimpe vite :

Les chutes contrées non vulnérables valent 100, 300, 500, puis 300 chacune ensuite. Les chutes
contrées vulnérables valent 200, puis 300 chacune. C'est la couche où une feuille de score papier se
trompe le plus souvent, parce que la progression n'est pas un taux fixe.

## Cinquième couche : les levées supplémentaires et les honneurs

Les levées supplémentaires rapportent au taux normal quand le contrat n'est pas contré, et 100 ou
200 chacune quand il l'est, selon la vulnérabilité. Détenir quatre ou cinq honneurs d'atout dans une
même main vaut 100 ou 150 en bridge robre.

## Le bridge robre et le bridge duplicate

**Le bridge robre** est le jeu de salon classique : le premier camp à deux manches remporte le
robre, qui vaut 700 points si l'adversaire n'a aucune manche et 500 s'il en a une. Les scores
partiels se reportent d'une donne à l'autre jusqu'à ce qu'une manche referme la ligne.

**Le duplicate** remplace le robre par un résultat par donne, comparé à toutes les autres tables qui
jouent les mêmes cartes, ce qui retire la part de chance de la distribution. Les valeurs de levées et
de bonus sont les mêmes, mais les bonus de manche sont attribués par donne plutôt que par robre.

## Compter les points sans faire le calcul

Braggster propose au Bridge une feuille de score pour quatre joueurs répartis en deux partenariats
fixes sur un jeu de 52 cartes standard, pour que les camps soient correctement en place dès le début
plutôt que d'avoir quatre colonnes indépendantes que tu dois te rappeler d'associer.

L'intérêt d'une feuille numérique ici n'est pas que le calcul du bridge soit impossible à la main.
C'est que la progression des chutes contrées et le changement de vulnérabilité sont exactement le
genre de règle qu'on applique de mémoire, mal, en fin de longue soirée.

## Questions fréquentes

**De combien de points a-t-on besoin pour une manche au bridge ?**
100 points sous la ligne, uniquement issus des levées demandées. Les bonus ne comptent pas.

**Quelle est la différence entre être vulnérable et ne pas l'être ?**
La vulnérabilité augmente tes bonus quand tu réussis un contrat, et augmente tes pénalités quand tu
le rates. Tu deviens vulnérable après avoir fait une manche.

**Combien vaut un chelem ?**
Un petit chelem vaut 500 non vulnérable et 750 vulnérable. Un grand chelem vaut 1000 et 1500. Les
deux s'ajoutent au bonus de manche et au score de levées.

**Le bridge duplicate se compte-t-il différemment du bridge robre ?**
Les valeurs de levées et les bonus de chelem sont les mêmes. Le duplicate attribue un bonus de manche
par donne au lieu de jouer un robre, et compare ton résultat à celui d'autres tables qui jouent les
mêmes cartes.

**Peut-on jouer au Bridge contre l'ordinateur dans Braggster ?**
Non. Le Bridge dans Braggster est une feuille de score pour une vraie table de quatre joueurs. Les
jeux de cartes jouables dans l'app sont le Blackjack, le Solitaire, le Loteria, le Hearts et la table
Freestyle.

---

**En savoir plus :** découvre tous les jeux de cartes sur [braggster.com/games](/games/), ou lis
l'aperçu du [calcul des points aux jeux de cartes](/blog/card-game-score-sheets/).
