---
title: "Killer Sudoku: Como Resolver Gaiolas Sem Chutar"
slug: how-to-play-killer-sudoku
locale: pt-BR
type: game
category: puzzle
game_id: killersudoku
meta_title: "Killer Sudoku: Como Resolver Gaiolas Sem Chutar"
meta_description: "Estratégia de Killer Sudoku: a regra do 45, combinações forçadas de gaiola, e as tabelas de soma que vale a pena decorar. Quebra-cabeças infinitos, offline."
primary_keyword: "estrategia de killer sudoku"
secondary_keywords:
  - "regras do killer sudoku"
  - "regra do 45 killer sudoku"
  - "combinacoes de gaiola killer sudoku"
  - "app killer sudoku offline"
  - "como jogar sudoku de somas"
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

# Killer Sudoku: Como Resolver Gaiolas Sem Chutar

O Killer Sudoku parece um Sudoku com decoração extra e joga como um quebra-cabeça completamente
diferente. A maioria das grades começa com **muito poucas pistas, ou nenhuma**, o que assusta na
primeira vez que você vê uma. A informação toda está lá. Só que escrita como somas em vez de
dígitos.

## As regras

1. Toda linha, coluna e quadrante 3x3 tem os números de 1 a 9 exatamente uma vez. Sudoku padrão.
2. As 81 células são divididas em **gaiolas**, desenhadas com bordas tracejadas e uma pequena soma
   no canto.
3. Os dígitos de cada gaiola são **distintos** e **somam o valor indicado**.

Essa terceira regra faz um trabalho enorme, porque uma gaiola é uma forma livre em vez de uma
linha ou um quadrante, então a distinção não é automática como no Sudoku comum. Ela precisa ser
imposta, e é isso que torna as somas informativas.

## Comece pelas gaiolas forçadas

Algumas somas têm exatamente uma combinação possível. São informação de graça e devem ser sua
primeira passada em qualquer grade.

| Tamanho da gaiola | Soma | Únicos dígitos possíveis |
|---|---|---|
| 2 células | 3 | 1, 2 |
| 2 células | 4 | 1, 3 |
| 2 células | 16 | 7, 9 |
| 2 células | 17 | 8, 9 |
| 3 células | 6 | 1, 2, 3 |
| 3 células | 7 | 1, 2, 4 |
| 3 células | 23 | 6, 8, 9 |
| 3 células | 24 | 7, 8, 9 |
| 4 células | 10 | 1, 2, 3, 4 |
| 4 células | 11 | 1, 2, 3, 5 |
| 4 células | 29 | 5, 7, 8, 9 |
| 4 células | 30 | 6, 7, 8, 9 |

Você ainda não sabe a ordem, mas já sabe o conjunto, e conhecer o conjunto elimina candidatos em
todos os lugares onde essas células enxergam.

## A regra do 45

A técnica mais útil do Killer Sudoku, e o motivo pelo qual solucionadores experientes abrem
grades que parecem impossíveis.

Toda linha, coluna e quadrante contém de 1 a 9, então sua **soma é 45**.

Se um conjunto de gaiolas cabe inteiramente dentro de uma linha, some seus totais. A diferença
para 45 é o total do que sobrou naquela linha. Quando sobra exatamente uma célula, você acabou de
resolvê-la diretamente.

O mesmo funciona ao contrário: se uma gaiola deixa uma célula para fora de um quadrante, a soma
das gaiolas dentro do quadrante menos 45 dá o valor dessa célula.

Encadeie isso em duas ou três linhas de uma vez e a técnica às vezes é chamada de método "dentro
e fora". É o carro-chefe das grades Killer difíceis.

## A geometria da gaiola importa

Como os dígitos de uma gaiola são distintos, a forma dela restringe ainda mais:

- Uma gaiola dentro de uma única linha, coluna ou quadrante nunca pode repetir, e a unidade
  também não, então nada de novo aí. Mas uma gaiola **que atravessa dois quadrantes** pode
  indicar em qual quadrante um dígito está.
- Uma gaiola de duas células somando 17 só pode ser 8 e 9. Se ela estiver em uma linha, o 8 e o
  9 dessa linha já estão posicionados, e toda outra célula da linha perde os dois candidatos.

## Como o Braggster gera os quebra-cabeças

O gerador constrói uma partição de gaiolas a partir de uma solução completa de Sudoku, e faz isso
**consciente dos dígitos**, porque uma gaiola de forma livre não é automaticamente distinta como
uma linha, coluna ou quadrante. Fazer crescer as gaiolas às cegas produziria gaiolas com
repetições, o que não é uma gaiola Killer válida.

Depois ele verifica a unicidade sob a restrição **combinada** de Sudoku e gaiolas juntas, usando
um solucionador de backtracking consciente das gaiolas. Verificar as duas restrições separadamente
não bastaria: uma grade pode ser ambígua só pelo Sudoku e única depois que as gaiolas entram, e
também o contrário.

Se uma tentativa esparsa não puder ser comprovada única dentro do orçamento de busca, o gerador
recorre ao conjunto de pistas já verificado do Sudoku para aquele nível. A consequência é que
**todo quebra-cabeça que você recebe é realmente solúvel de forma única**, nunca um talvez.

## O tabuleiro

O tabuleiro Killer reaproveita a anatomia de grade do Sudoku e soma uma camada de gaiolas: cinco
tons, bordas de gaiola tracejadas e uma etiqueta de soma no canto. Cinco tons bastam para gaiolas
vizinhas sempre diferirem sem a grade virar um gráfico de cores.

As ajudas são anotações a lápis e dicas. Não existe feedback ao vivo de entrada errada em nenhum
quebra-cabeça do Braggster, então os erros são contados silenciosamente e revelados no resumo da
solução. A pontuação é o tempo de resolução mais uma penalidade por erro e por dica, e menor
pontuação vence.

## Perguntas frequentes

**Os dígitos podem se repetir dentro de uma gaiola do Killer Sudoku?**
Não. Os dígitos da gaiola precisam ser distintos, o que é o que torna as somas úteis. É o oposto
do Calcudoku, onde os dígitos da gaiola podem se repetir.

**O que é a regra do 45?**
Toda linha, coluna e quadrante soma 45. Comparar isso com as gaiolas dentro de uma unidade revela
o total das células que sobraram, e às vezes resolve uma diretamente.

**Por que os quebra-cabeças Killer Sudoku têm tão poucos números dados?**
As gaiolas carregam a restrição no lugar deles. Uma grade Killer bem construída pode começar sem
nenhuma pista e ainda ter exatamente uma solução.

**O Killer Sudoku é mais difícil que o Sudoku comum?**
É diferente, mais do que estritamente mais difícil. Exige aritmética junto com a lógica, mas as
somas das gaiolas dão uma informação que uma grade comum não tem.

**Os quebra-cabeças se repetem?**
Não. São gerados na hora sob demanda e verificados como únicos antes de serem mostrados.

---

**Mais:** veja os treze [quebra-cabeças de lógica](/blog/puzzle-games/), leia sobre a
[dificuldade do Sudoku](/blog/how-to-play-sudoku/), ou veja o catálogo em
[braggster.com/games](/games/).
