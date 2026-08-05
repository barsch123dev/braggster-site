---
title: "Puntuación de Backgammon: Simples, Gammons y Backgammons"
slug: how-to-score-backgammon
locale: es
type: game
category: board
game_id: backgammon
meta_title: "Puntuación de Backgammon: Simples y Gammons"
meta_description: "Cuánto vale una victoria en backgammon: 1 punto una simple, 2 un gammon, 3 un backgammon. Con tablero jugable y un rival que corre un expectimax."
primary_keyword: "reglas del backgammon"
secondary_keywords:
  - "que es un gammon en backgammon"
  - "puntuacion del backgammon"
  - "jugar backgammon sin conexion"
  - "backgammon puntuacion por partido"
  - "backgammon contra el ordenador"
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

# Puntuación de Backgammon: Simples, Gammons y Backgammons

Backgammon es el juego más antiguo del catálogo de Braggster con diferencia, y tiene el sistema de
puntuación más limpio de todos. Tres resultados, tres valores, y toda la diferencia entre una
victoria tranquila y una aplastante está en si tu rival llegó a sacar alguna ficha.

## Los tres resultados

| Resultado | Vale | Condición |
|---|---|---|
| **Simple** | 1 punto | Quien pierde ha sacado al menos una ficha |
| **Gammon** | 2 puntos | Quien pierde no ha sacado ninguna ficha |
| **Backgammon** | 3 puntos | Quien pierde no ha sacado ninguna ficha, y todavía tiene una ficha en la casa del ganador o en la barra |

Ese es todo el sistema de puntuación. Los puntos se acumulan partida tras partida como un marcador
corrido, y lidera el total más alto.

La regla del gammon es lo que le da a backgammon su tensión de final de partida. Un jugador que va
claramente perdiendo ya no juega para ganar, juega para sacar **una sola ficha** antes de que su
rival termine, porque eso reduce el daño a la mitad. Ver a alguien correr con una ficha solitaria
hacia casa para evitar un gammon es una de las cosas genuinamente más dramáticas que pasan en los
juegos de mesa.

## Por qué no hay cubo aquí

El backgammon serio usa un cubo doblador, que multiplica lo que está en juego a mitad de partida y
se puede volver a doblar. Braggster no tiene cubo doblador, y es deliberado: nada en toda la app
registra una cantidad puesta en juego. La puntuación es el resultado de la partida, 1, 2 o 3, y eso
es todo.

Si juegas con cubo en casa, anota el resultado de cada partida y deja el cubo sobre el tablero.

## Lo básico del juego

Cada lado tiene quince fichas que se mueven en direcciones opuestas alrededor de veinticuatro
puntos, buscando llevarlas todas a su propia casa y luego sacarlas.

- Tira dos dados y mueve dos fichas, o una ficha dos veces.
- **Los dobles juegan cuatro veces**, no dos.
- Un punto ocupado por dos o más fichas del rival queda cerrado para ti.
- Una ficha sola es una **ficha suelta**. Si el rival cae sobre ella, va a la barra, y tiene que
  reingresar por la casa del rival antes de poder mover cualquier otra ficha.
- Cuando las quince están en casa, empiezas a sacarlas.

## El tablero jugable

El Backgammon de Braggster incluye un tablero local: tira los dos dados, toca una ficha y luego el
punto resaltado para moverla, golpea fichas sueltas hacia la barra, reingresa, y saca fichas. La
partida terminada se anota directamente en el marcador corrido, así que una partida jugada desde el
móvil nunca puede puntuar distinto de una anotada a mano.

Se admiten dos aperturas:

- **Estándar**, la posición inicial normal.
- **Nackgammon**, que retrasa dos fichas para que el juego inicial sea menos una carrera y más
  posicional.

## El rival del ordenador, y por qué es distinto

Backgammon tiene una pantalla de práctica contra el ordenador con tres niveles, jugando con las
Claras o las Oscuras.

Lo interesante es que no puede funcionar como los otros motores de Braggster. Chess, Checkers y las
damas internacionales usan todos búsqueda alfa beta, que depende de que el juego sea determinista:
sabes exactamente qué posiciones se pueden alcanzar desde aquí.

Backgammon tiene dados. Cada nodo del árbol es un nodo de azar, con veintiuna tiradas distintas que
considerar. Así que el motor de backgammon corre en su lugar una búsqueda **expectimax**, que
promedia sobre esas tiradas en lugar de asumir que el rival elige la peor para ti. Corre en un hilo
en segundo plano para que el tablero siga respondiendo mientras piensa.

Las partidas de práctica nunca se registran, así que jugar contra el ordenador no afecta a tus
estadísticas.

## Preguntas frecuentes

**¿Cuántos puntos vale un gammon?**
2 puntos. Una simple vale 1 y un backgammon vale 3.

**¿Cuál es la diferencia entre un gammon y un backgammon?**
Ambos exigen que quien pierde no haya sacado ninguna ficha. Es un backgammon solo si además le
queda una ficha en la barra o en la casa del ganador cuando termina la partida.

**¿Los dobles se mueven cuatro veces en backgammon?**
Sí. Sacar 5-5 te da cuatro movimientos de cinco, no dos.

**¿Hay cubo doblador en la app?**
No. Braggster registra solo el resultado de la partida, sin nada puesto en juego en ningún lugar de
la app.

**¿Puedo jugar backgammon sin conexión contra el ordenador?**
Sí. El motor corre por completo en tu dispositivo, sin conexión y sin cuenta necesaria.

**¿Qué es Nackgammon?**
Una posición inicial alternativa que retrasa dos fichas, lo que hace la apertura más posicional y
menos una carrera directa. Braggster la ofrece junto a la apertura estándar.

---

**Más:** explora todos los juegos en [braggster.com/games](/games/), o lee el resumen sobre
[puntuación de juegos de mesa](/blog/board-game-score-sheets/).
