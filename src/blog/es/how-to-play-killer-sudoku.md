---
title: "Killer Sudoku: Cómo Resolver las Jaulas sin Adivinar"
slug: how-to-play-killer-sudoku
locale: es
type: game
category: puzzle
game_id: killersudoku
meta_title: "Killer Sudoku: Cómo Resolver las Jaulas"
meta_description: "Estrategia de Killer Sudoku: la regla del 45, las combinaciones forzadas de jaula y las tablas de sumas que conviene memorizar. Puzles infinitos, sin anuncios."
primary_keyword: "killer sudoku estrategia"
secondary_keywords:
  - "killer sudoku reglas"
  - "regla del 45 killer sudoku"
  - "combinaciones de jaula killer sudoku"
  - "killer sudoku app sin conexión"
  - "sudoku de sumas como se juega"
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

# Killer Sudoku: Cómo Resolver las Jaulas sin Adivinar

Killer Sudoku parece un Sudoku con decoración extra y se juega como un puzle completamente
distinto. La mayoría de las cuadrículas empiezan con **muy pocos números iniciales, o ninguno**, lo
cual es alarmante la primera vez que lo ves. Toda la información está ahí. Solo que está escrita
como sumas en lugar de cifras.

## Las reglas

1. Cada fila, columna y caja de 3x3 contiene del 1 al 9 exactamente una vez. Sudoku estándar.
2. Las 81 celdas se reparten en **jaulas**, dibujadas con bordes discontinuos y una pequeña suma en
   la esquina.
3. Las cifras de cada jaula son **distintas entre sí** y **suman el total indicado**.

Esa tercera regla hace un trabajo enorme, porque una jaula tiene una forma libre en lugar de ser
una fila o una caja, así que la distinción entre cifras no es automática como sí lo es en el
Sudoku normal. Hay que imponerla, y es lo que hace que las sumas resulten útiles.

## Empieza por las jaulas forzadas

Algunas sumas tienen exactamente una combinación posible. Son información gratis y deberían ser tu
primer barrido sobre cualquier cuadrícula.

| Tamaño de jaula | Suma | Únicas cifras posibles |
|---|---|---|
| 2 celdas | 3 | 1, 2 |
| 2 celdas | 4 | 1, 3 |
| 2 celdas | 16 | 7, 9 |
| 2 celdas | 17 | 8, 9 |
| 3 celdas | 6 | 1, 2, 3 |
| 3 celdas | 7 | 1, 2, 4 |
| 3 celdas | 23 | 6, 8, 9 |
| 3 celdas | 24 | 7, 8, 9 |
| 4 celdas | 10 | 1, 2, 3, 4 |
| 4 celdas | 11 | 1, 2, 3, 5 |
| 4 celdas | 29 | 5, 7, 8, 9 |
| 4 celdas | 30 | 6, 7, 8, 9 |

Todavía no sabes el orden, pero ya sabes el conjunto, y conocer el conjunto elimina candidatos en
todas partes donde esas celdas influyen.

## La regla del 45

La técnica más útil de Killer Sudoku, y la razón por la que los jugadores con experiencia abren
cuadrículas que parecen imposibles.

Cada fila, columna y caja contiene del 1 al 9, así que **suma 45**.

Si un conjunto de jaulas cabe entero dentro de una fila, suma sus totales. La diferencia con 45 es
el total de las celdas que sobran en esa fila. Cuando solo sobra una celda, acabas de resolverla
directamente.

Lo mismo funciona al revés: si una jaula deja una sola celda fuera de una caja, la suma de las
jaulas dentro de la caja menos 45 te da el valor de esa celda.

Encadenar esto en dos o tres filas a la vez es lo que a veces se llama el método de "lo que entra y
lo que sale". Es el caballo de batalla de las cuadrículas Killer difíciles.

## La geometría de la jaula importa

Como las cifras de una jaula son distintas entre sí, su forma la restringe todavía más:

- Una jaula dentro de una sola fila, columna o caja nunca puede repetir cifras, y tampoco puede la
  unidad, así que no aporta nada nuevo. Pero una jaula que **abarca dos cajas** sí puede decirte en
  qué caja vive una cifra.
- Una jaula de dos celdas que suma 17 tiene que ser 8 y 9. Si está dentro de una fila, el 8 y el 9
  de esa fila quedan colocados, y el resto de celdas de la fila pierden ambos candidatos.

## Cómo los genera Braggster

El generador hace crecer una partición en jaulas a partir de una solución de Sudoku completa, y lo
hace **con conciencia de las cifras**, porque una jaula de forma libre no es automáticamente
distinta como sí lo es una fila, una columna o una caja. Hacer crecer jaulas a ciegas produciría
jaulas con cifras repetidas, lo cual no es una jaula Killer válida.

Luego verifica la unicidad bajo la restricción **combinada** de Sudoku y de jaulas a la vez, usando
un solucionador por retroceso consciente de las jaulas. Comprobar las dos restricciones por
separado no serviría: una cuadrícula puede ser ambigua solo bajo Sudoku y única en cuanto se aplican
las jaulas, y también al revés.

Si un intento con pocas cifras no se puede demostrar único dentro del presupuesto de búsqueda, el
generador recurre al conjunto de números iniciales ya verificado de Sudoku para ese nivel. La
consecuencia es que **cada puzle que te toca es de verdad resoluble de forma única**, nunca un
quizás.

## El tablero

El tablero de Killer reutiliza la anatomía de la cuadrícula de Sudoku y le añade una capa de
jaulas: cinco tonos, bordes discontinuos y una etiqueta de suma en la esquina. Cinco tonos bastan
para que las jaulas contiguas siempre se diferencien sin que la cuadrícula se convierta en una
carta de colores.

Las ayudas son las notas a lápiz y las pistas. No hay indicación en vivo de errores en ningún puzle
de Braggster, así que los errores se cuentan en silencio y se revelan en el resumen final. La
puntuación es el tiempo de resolución más una penalización por error y por pista, y gana el total
más bajo.

## Preguntas frecuentes

**¿Se pueden repetir cifras dentro de una jaula de Killer Sudoku?**
No. Las cifras de una jaula deben ser distintas, que es lo que hace útiles las sumas. Esto es lo
contrario de Calcudoku, donde las cifras de una jaula sí pueden repetirse.

**¿Qué es la regla del 45?**
Cada fila, columna y caja suma 45. Comparar eso con las jaulas dentro de una unidad revela el total
de las celdas que sobran, y muchas veces resuelve una directamente.

**¿Por qué los puzles de Killer Sudoku tienen tan pocos números iniciales?**
Las jaulas cargan con la restricción en su lugar. Una cuadrícula Killer bien construida puede
empezar sin ningún número inicial y aun así tener exactamente una solución.

**¿Es Killer Sudoku más difícil que el Sudoku normal?**
Distinto más que estrictamente más difícil. Exige aritmética además de lógica, pero las sumas de
las jaulas aportan información que una cuadrícula normal no tiene.

**¿Se repiten los puzles?**
No. Se generan al momento y se verifica que sean únicos antes de mostrarse.

---

**Más:** consulta los trece [puzles de lógica](/blog/puzzle-games/), lee sobre la
[dificultad del Sudoku](/blog/how-to-play-sudoku/), o explora el catálogo en
[braggster.com/games](/games/).
