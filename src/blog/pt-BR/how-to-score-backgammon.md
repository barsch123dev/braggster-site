---
title: "Pontuação do Backgammon: Simples, Gamão e Gamão Duplo"
slug: how-to-score-backgammon
locale: pt-BR
type: game
category: board
game_id: backgammon
meta_title: "Pontuação do Backgammon: Simples, Gamão, Gamão Duplo"
meta_description: "O valor de cada vitória no Backgammon, o Gamão: 1 ponto no simples, 2 no gamão, 3 no gamão duplo. Com tabuleiro jogável e adversário virtual com expectimax."
primary_keyword: "gamao regras"
secondary_keywords:
  - "o que e gamao no backgammon"
  - "regras do backgammon"
  - "jogar gamao offline"
  - "pontuacao de partida de gamao"
  - "gamao contra o computador"
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

# Pontuação do Backgammon: Simples, Gamão e Gamão Duplo

O Backgammon, conhecido no Brasil como Gamão, é de longe o jogo mais antigo do catálogo do
Braggster, e tem o sistema de pontuação mais simples de todos. Três resultados, três valores, e
toda a diferença entre uma vitória tranquila e um resultado arrasador está em saber se o
adversário conseguiu tirar pelo menos uma peça do tabuleiro.

## Os três resultados

| Resultado | Vale | Condição |
|---|---|---|
| **Simples** | 1 ponto | O perdedor já tirou pelo menos uma peça do tabuleiro |
| **Gamão** | 2 pontos | O perdedor não tirou nenhuma peça |
| **Gamão duplo** | 3 pontos | O perdedor não tirou nenhuma peça, e ainda tem uma peça na casa do vencedor ou na barra |

É todo o sistema de pontuação. Os pontos se acumulam partida após partida em um total corrido, e
quem tem a maior pontuação está na frente.

A regra do gamão é o que dá tensão ao fim de jogo do Gamão. Um jogador claramente perdendo já não
está mais jogando para vencer, está jogando para tirar pelo menos uma peça antes que o adversário
termine, porque isso reduz o prejuízo pela metade. Ver alguém correr com uma única peça até em
casa para escapar do gamão é uma das cenas mais dramáticas que existem nos jogos de tabuleiro.

## Por que não há dado dobrador aqui

O Backgammon competitivo usa um dado dobrador, que multiplica o valor da partida no meio do jogo e
pode ser redobrado. O Braggster não tem dado dobrador, e isso é proposital: nada no app registra
uma aposta em lugar nenhum. A pontuação é só o resultado da partida, 1, 2 ou 3, e é só isso.

Se você joga com dado dobrador em casa, registre o resultado de cada partida e deixe o dado
dobrador só no tabuleiro físico.

## O básico do jogo

Cada lado tem quinze peças que se movem em direções opostas ao longo de vinte e quatro casas, com
o objetivo de levar todas para a própria casa final e depois tirá-las do tabuleiro.

- Jogue os dois dados e mova duas peças, ou uma peça duas vezes.
- **Dados duplos valem quatro jogadas**, não duas.
- Uma casa ocupada por duas ou mais peças do adversário fica fechada para você.
- Uma peça sozinha é um **blot**. Se você cair nela, a peça vai para a barra, e precisa reentrar
  pela casa final do adversário antes que esse jogador possa mover qualquer outra peça.
- Quando as quinze peças estiverem na casa final, você começa a tirá-las do tabuleiro.

## O tabuleiro jogável

O Backgammon do Braggster tem um tabuleiro para jogar passando o celular: jogue os dois dados,
toque em uma peça e depois na casa destacada para movê-la, mande blots para a barra, reentre e
tire as peças do tabuleiro. A partida terminada entra direto no total corrido, então uma partida
jogada no celular nunca pode pontuar diferente de uma registrada à mão.

Duas posições iniciais são compatíveis:

- **Padrão**, a posição inicial normal.
- **Nackgammon**, que recua duas peças para deixar o início de jogo menos uma corrida e mais
  posicional.

## O adversário virtual, e por que ele é diferente

O Backgammon tem uma tela de treino contra o computador com três níveis, jogando com as peças
claras ou escuras.

Vale saber que ele não pode funcionar do mesmo jeito que os outros motores do Braggster. Chess,
Checkers e International draughts usam busca alfa beta, que depende do jogo ser determinístico:
você sabe exatamente quais posições são alcançáveis a partir de cada momento.

O Backgammon tem dados. Todo nó da árvore de decisão é um nó de chance, com vinte e um resultados
distintos de dados a considerar. Por isso o motor do Backgammon roda uma busca **expectimax**,
calculando a média sobre esses resultados em vez de supor que o adversário sempre tira o pior para
você. Ele roda em segundo plano para o tabuleiro continuar respondendo enquanto o computador pensa.

Partidas de treino nunca são registradas, então jogar contra o computador não afeta suas
estatísticas.

## Perguntas frequentes

**Quanto vale um gamão?**
2 pontos. Um simples vale 1 e um gamão duplo vale 3.

**Qual a diferença entre gamão e gamão duplo?**
Nos dois casos o perdedor não tirou nenhuma peça. Só é gamão duplo se o perdedor ainda tiver uma
peça na barra ou na casa final do vencedor quando a partida termina.

**Dados duplos valem quatro jogadas no Backgammon?**
Sim. Tirar 5 e 5 dá quatro jogadas de cinco casas, não duas.

**Existe dado dobrador no app?**
Não. O Braggster registra só o resultado da partida, sem nenhuma aposta em lugar nenhum do app.

**Dá para jogar Backgammon offline contra o computador?**
Sim. O motor roda totalmente no seu aparelho, sem precisar de conexão nem de cadastro.

**O que é Nackgammon?**
Uma posição inicial alternativa que recua duas peças ainda mais, deixando a abertura mais
posicional e menos uma corrida direta. O Braggster oferece essa opção junto com a posição padrão.

---

**Mais:** veja todos os jogos em [braggster.com/games](/games/), ou leia o panorama de
[pontuação de jogos de tabuleiro](/blog/board-game-score-sheets/).
