## 1.2 - Operações
### 1.2.1 - Adição
Aula anterior

### 1.2.2 - Subtração
#### Decimal
- Recordemos subtração à primária em base decimal, com a conta $231-19$:
![[subtracao 10.png|475]]

- Simplesmente percorremos os números da direita para a esquerda e a cada algarismo de cima (diminuendo) subtraimos o algarismo de baixo (diminuidor) com ele alinhado.
- Ora, temos 1 caso particular: quando um algarismo de cima é inferior ao de baixo, pelo que obteríamos um número negativo. Assim, nós "levamos 1 emprestado". Ora, não podemos simplesmente acrescentar 10 ao algarismo menor que o de baixo (no caso acima, o $1-9\to11-9$). Para corrigir a conta temos que subtrair 10 ao diminuendo ou acrescentar 10 ao diminuidor. Acima vemos os 2 casos.
- De uma forma mais geral estamos a diminuir ou acrescentar $10^{n}$, tal como é o caso em $2045_{10}-910_{10}$, em "levar 1 emprestado" na conta $0-9\to10-9$ implica acrescentar 100 ao diminuidor ou subtrair 100 ao diminuendo.
- De resto, quando temos um número maior ou igual em cima, apenas subtraimos.

#### Binário
- Agora *base binária*. Funciona praticamente igual. Em base 10, ao "emprestar um 1"/*borrow* immplica acrescentar ou diminuir 10 como já disse. Na base 2 iremos acrescentar ou subtrair 2.
- De forma mais geral, iremos acrescentar $2^{n}$.
- Vejamos um exemplo:
![[subtracao 2.png|500]]
(NOTA: temos aqui a mesma conta 2 vezes, mas desenvolvi a técnica de subtrair ao diminuendo e a de acrescentar ao diminuidor)
- Irei usar a ténica de subtrair ao diminuidor.
- Vejamos um exemplo maior:
![[subtracao 2-2.png|500]]
- Algumas notas:
    - Podemos sempre converter os números em base 10 e verificar a conta. No entanto, isto pode ser demasiado trabalhoso para números elevados
    - Podemos ainda reverter a conta ($a-b=c\to b+c=a$) e para verificar

### 1.2.3 - Multiplicação
#### Decimal
- Em decimal temos
![[multiplicacao 10.png|275]]
- Temos um caso partícular. Ao multiplicar um número por $10^{n}$ simplesmente matemos o número e deslizamo-lo $n$ casas para a esquerda: $251\cdot10^{2}=25100$

#### Binário
- Em binário é igual:
![[multiplicacao 2.png|325]]
- E temos o mesmo caso partícular: $1101_{2}\cdot2^{3}_{10}=1101000_{2}$
    - Ou seja, por exemplo, sabendo que $26_{10}=11010_{2}$ temos que $26\cdot4=26 \cdot2^{2}=1101000_{2}$

### 1.2.4 - Divisão 
#### Decimal
- Recordemos divisão em base decimal:
![[divisao 10.png|500]]
normalmente não escrevemos isto com tanto detalhe, mas é assim que funciona: procuramos o menor número da esquerda para a direita que é maior que o divisor (e que pode ser dividido por ele).

#### Binário
- Funciona como base decimal:
![[divisao 2.png|500]]
Vejamos um exemplo maior para entender o que acontece ao certo:
![[divisao 2-2.png|500]]
Ou seja:
1. Da esquerda para a direita, escolhemos o primeiro número maior que o divisor ($10000>1111$ no exemplo de baixo). Colocamos um 1 no quociente e subtraimos o divisor a este número. Sempre que fazemos isto desce um algarismo "automaticamente" (no exemplo de cima isto aconteceu com um $1$, no de baixo com um $0$; ambos a cinzento).
2. Comparamos o número obtido do resultado da subtração com o algarismo que desce ($1011$ no exemplo de cima, $100$ no de baixo):
    1. Se este for maior que o divisor, subtraimos.
    2. Se for menor (como nos 2 exemplos), descemos mais 1 algarismo e acrescentamos um 0 ao quociente.
3. Repetir o passo 2 sucessivamente até chegarmos ao resto da divisão.

## 1.3 - Dimensão de Dados e Overflow
- Se tivermos uma operações (de números sem sinal) representados por um sistema 4bit ocorre o seguinte:
![[overflow.png|500]]
ou seja, apenas os primeiros 4 bits (da vírgula para a esquerda) é que são representados, cortando-se os restantes.
- Assim, ocorre overflow quando o resultado da operação tem mais bits do que aqueles que temos para fazer a representação, de forma que o resultado apresentado está errado. Isto ocorre devido ao "e vai 1"/carry no último bit.

## 1.4 - Números com Sinal
- Existem 2 formas de representar o sinal:
    - Existe 1 bit extra que $=1$ se o número é negativo e $=0$ se positivo (forma menos comum)
    - **Complemento para 2** (mais comum) (abaixo)

### Complemento para 2 (C2)
- Tendo-se um número $X$ representado em complemento de 2 por $X_{2}=b_{n-1}b_{n-2}\dots b_{2}b_{1}b_{0}$
- Ora, o valor deste número é dado por: $-b_{n-1}2^{n-1}+b_{n-2}2^{n-2}+\dots+b_{2}2^{2}+b_{1}2^{1}+b_{0}2^{0}$, em que apenas o bit mais significativo (*MSB* - most significant bit) tem peso negativo.
- O simétrico de $X$ é $-X=2^{n}-X$

- Ora, se o MSB for $1$ o número será negativo, se for $0$ então este é postivo.
    - O maior número negativo (em módulo) para $n$ bits é um 1 com $n-1$ 0s ($-2^{n-1}$)
    - O maior número positibo para $n$ bits é um 0 com $n-1$ 1s ($2^{n-1}-1$)
    - Ou seja, um número representado em complemento de 2 com $n$ bits está no intervalo $[-2^{n-1};2^{n-1}-1]$

### Representar número
- Representamos um número como a sequência de bits: $X\to b_{n-1}b_{n-2}\dots b_{2}b_{1}b_{0}$ (seta para  a direita é usada para dizer "X é representado por...")
    - Se for positivo representamos como normalmente, com pelo menos 1 zero à esquerda (para que $MSB=0$)
    - Se for negativo temos a mesma representação que o positivo (em valor) mas com o MSB trocado ($MSB=1$)

### Obter simétrico de número
1. Como vimos, para obter o simétrico podemos fazer $2^{n}-X$ (para uma representação com $n$ bits). De notar que fazemos esta operação em base binária (em que $2^{n}$ é um 1 com $n$ 0s)
2. Podemos simplesmente fazer: $2^{n}-1-X+1$
    1.  Ao fazer $2^{n}-1$ ficamos com $n$ 1s
    2. Ao fazer $(2^{n}-1)-X$ acabamos por trocar todos os bits da representação de $X$. 
    3. Ao somar $1$ ficamos com o simétrico.
    4. Ou seja, invés de pensar e fazer a conta, podemos simplesmente trocar os bits de $X$ e acrescentar 1.
3. Maneira "à engenheiro" (shoutout ao prof das TP). Consiste em resumir o método 2 ainda mais. Basicamente, começamos da direita para a esquerda. Repetimos o número, até encontrar o 1º um. A partir dele (ele não incluído) trocar todos os números.
    - Consideremos $1001010100$ em C2 ($=-428_{10}$). Fazemos assim (direita para esquerda): $0\to00\to100$. Encontramos o um!!. Agora contínuamos: $100\to1100\to01100\to101100\to0101100\to10101100\to110101100\to0110101100$. Podemos facilmente ver que isto representa $+428_{10}$

Vejamos um exemplo para ver que isto bate certo:
![[obter simetrico C2.png|500]]

### Adição
- Tratamos o MSB como um bit normal
- Apenas consideramos os $n$ bits da direita do resultado final (cortar o carry do MSB)
- Temos **2 sinais de overflow**:
    1. Quando a soma de 2 números com o mesmo sinal dá um com sinal diferente
    2. Quando os últimos 2 carries são diferentes
- Normalmente overflow ocorre quando o resultado da soma está fora do range dos bits (por exemplo, $3+7=10$ representado com 4 bits irá dar overflow, pois o range desta representação em C2 é: $[-2^{n-1},2^{n-1}-1]=[-8,7]$ a que $10$ não pertence)
- Podemos escrever subtração como $A-B=A+(-B)$
![[somas C2.png]]
Notas:
    - Nos Exemplos A,B,D vemos que cortamos os bits acima de $n=4$
    - Em B,C vemos casos de overflow

### Subtração
- Podemos fazer $A-B=A+(-B)$ ou simplesmente subtrair os números:
![[subtração C2.png|500]]
- Notas:
    - Em A temos um overflow. Em subtração, overflow ocorre quando subtraimos operadores de sinais opostos e o resultado não bate certo. Ao subtrair números com o mesmo sinal nunca ocorre overflow.
    - Em C,D usamos a técnica de trocar o sinal.

### Extensão de Sinal
- Aquilo que fazemos ao realizar operações com números com dimensões diferentes ou quando queremos um resultado de dimensão específica. 
- Consideremos 2 exemplos:
![[extensão sinal.png]]
- Notas:
    - No exemplo A vemos como somar números de dimensões diferentes. Torna-se ainda evidente que, para números negativos em complemento de 2 acrescentar em 1s à esquerda não afeta o valor, e igualmente para acrescentar 0s a números positivos.
    - No exemplo B queremos que o resultado tenha 8 bits. Fazemos como temos acima. De notar que podíamos simplesmente tirar os primeiros dois 1s do número e teríamos o mesmo valor, mas aqui o que importa são os bits do número.

## 1.5 - Representação em Vírgula Flutuante
- Como temos sempre um número finito de bits, a vírgula pode ser movida de forma a variar a precisão que temos
- Como sabemos, em notação científica é costume apenas colocar 1 número à *esquerda* da vírgula ($2,345\cdot10^{6}$ invés de $234,5\cdot10^{4}$)
    - De notar que no exemplo dado entre  parentesis estamos a deslocar a vírgula $n$ casas para a esquerda, até termos apenas 1 algarismo à esquerda dela.
    - Para compensar, acrescemos o expoente do 10 em $n$ unidades.

- Ora, tudo isto funciona igualmente em base 2.
- Desta forma, de forma genérica, teremos números na forma:
$$\pm1,mm\dots m\cdot2^{\pm eee\dots e}$$
    - Em que a parte $mmmm$ chamamos de **mantissa** (1 à esquerda da vírgula não incluido)
    - Em que a parte $eeee$ se chama **expoente**.
        - A ele está associado um *bias*. O verdadeiro expoente é $\pm eee\dots e-bias$
        - Usamos os expoentes $000\dots0,111\dots1$ para representar valores especiais: $\text{NaN},\pm\infty$

## 1.6 - IEEE 754
- Define uma série de precisões para representar números binários em vírgula flutuante: simples (32 bits), dupla (64 bits), estendida (128 bits). Estes consistem nos bits que temos disponíveis / que "podemos ocupar".
- Define ainda as regras a usar em casos de arredondamento e erro.

### 1.6.1 -  Simples (32)
- Temos 32 bits:
    - 1 bit para o sinal (S) (0 se positivo, 1 se negativo, como já vimos)
    - 8 bits para o expoente (E) - Com excesso 127 (acrescentar 127 ao expoente da notação científica)
    - 23 bits para a mantissa (M) (tal como dito acima, o 1 inicial é implicito AKA não indicado)
EX:
![[ieee.png]]
- Temos os valores especiais:
    - Zero: $0~00000000~000000000000000000000000$
    - $+\infty$: $0~11111111~000000000000000000000000$
    - $-\infty$: $1~11111111~000000000000000000000000$
    - $\text{NaN}$: $x~11111111~MMMMMMMMMMMMMMMMMMMMMMMM~~(M\neq0)$

### 1.6.2 - Dupla (64)
- Temos 64 bits:
    - 1 bit para o sinal (S) (0 se positivo, 1 se negativo, como já vimos)
    - 11 bits para o expoente (E) - Com excesso 1023 (acrescentar 1023 ao expoente da notação científica)
    - 52 bits para a mantissa (M) (tal como dito acima, o 1 inicial é implicito AKA não indicado)
- Exemplo Hex $\to$ decimal no PPT