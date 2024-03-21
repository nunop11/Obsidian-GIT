## 2.5 - Circuitos Integrados
- Temos CIs conhecidos por "série 74" que representamos por 74Xnnn em que
    - X indica as caraterísticas elétricas do tipo de circuito
    - nnn representa a função lógica

- Por exemplo, 74X00 tem 4 portas lógicas NAND com 2 entradas cada. Por exemplo, 74X04 tem 6 inversores (portas NOT). Alguns exemplos:
![[serie 74.png|400]]

- Para os usar ligamos o dispositivo a uma fonte DC de 5V
- As portas que não usamos devem ser ligadas a 0V ou 5V (0 ou  1). Se ligadas a 5V devemos usar resistência $[1,10]\text{k}\Omega$.
- Para reduzir o custo de um circuito dever-se-á escolher a combinação de CIs que permite definir a função booleana de forma mais eficiente.
- De notar que nenhum CI tem ANDs e ORs em simultaneo. Isto influencia os circuitos que podemos fazer.

## 2.6 - Transformação para NANDs
- NANDs (AND com NOT no fim) são mais baratas e rápidas que AND.
- Desta forma, uma maneira de medir a complexidade de um circuito digital é ver quantas portas lógicas NAND de 2 entradas são precisas para o fazer.

**Transformação**
- Consideremos o serguinte circuito AND-OR:
![[circuito ex 1.png]]
- Simplesmente transformamos os ANDs em NANDs (negar as saídas) e negar as entradas do OR:
![[circuito ex 2.png]]
como explicado na imagem, negamos as entradas no OR porque isso equivale a um NAND.
- Para os NOT podemos simplesmente colocar um NAND com 2 entradas:
    - $Y=0\to\overline Y=1 ~~;~~ \overline{Y.Y}=\overline{0.0}=\overline{0}=1$
    - $Y=1\to\overline{Y}=0~~;~~ \overline{Y.Y}=\overline{1.1}=\overline{1}=0$

## 3 - Circuitos Combinacionais
- O que vimos atrás (equação booleana formal, circuito de NANDs, descrever o menor circuito possível) apenas se aplica a circuitos "pequenos"
- Para circuitos complexos com dezenas de entradas este processo torna-se impraticável (por exemplo, se tivermos 32 entradas teremos uma tabela de verdade com $2^{32}\sim4\cdot10^{9}$ linhas)
- Assim, fazemos circuitos complexos à base de circuitos simples
    - P/Ex: fazemos um somador de 32bits usando fill-adders (somadores de 3 números de 1 bit)

### 3.1 - Funções Combinacionais Padrão
- Tipo de funções que usamos como bases dos sistemas complexos. Normalmente disponíveis em CIs.
- EXS:
    - somadores (com/sem deteção de overflow, com/sem sinal)
    - comparadores 
    - descodificadores e codificadores (binário, Hex, 7-seg)
    - multiplexers

### 3.2 - Desenho
- Para portas lógicas elementares usamos o seu símbolo (NOT, NAND, NOR)
- Para portas/funções complexas obviamente não temos um símbolo para cada função. Assim, metemos uma caixa com entradas (esquerda) e saídas (direita):
![[CI.png]]
- Como regra geral, desenhamos as entradas do lado esquerdo e as saídas do lado direito.

#### Barramentos
- Consideremos que temos $N$ sinais lógicos que representam um número com $N$ bits ($A=A_{7}~A_{6}~A_{5}~A_{4}~A_{3}~A_{2}~A_{1}~A_{0}$). Podemos simplesmente escrever $A=A[7:0]$:
![[barramentos.png]]

#### Nomes dos Sinais
- Podem ter letras, números e underscores. Primeiro carater deve ser uma letra. 
- Para marcar sinais que são ativados com 0 e não com 1 usamos $/$ no início ou $\#,\_L$ no fim ($OE\#,/OE,OE\_L$)
- Para representar barramentos usamos $A\_BUS[7:0],A\_BUS(7:0),A\_BUS<7:0>$  (em que temos um sinal $A\_BUS$ com 8 bits, de 7 a 0, com 7 o MSB e 0 o LSB)
- Podemos considerar que sinais com o mesmo nome estão ligados.

#### EX
Ver página 86 e seguintes do livro para ver um exemplo: calculador de máximo e mínimo.

## 3.3 - Codificadores e Descodificadores
- Permitem traduzir código binário de $N$ bits para código de $M$ bits possivelmente noutra base, sendo normalmente $M\neq N$
- Normalmente dizemos
    - Codificador - converte código noutro com menor número de bits
    - Descodificador - converte código noutro com maior número de bits
- EX: converter sinal que representa número em base decimal em código de 7bits para poder ser representado em mostrador de 7 segmentos.

### 3.3.1 - Codificador Binário
- Converte sinal de $2^{N}$ bits em sinal de $N$ bits.
- Temos o 74X148 -- 8:3:
![[codificadores 2.png]]

### 3.3.2 - Descodificador Binário
- Recebe um código de $N$ bits e converte-o num de $2^{N}$ bits.
- Como CI temos o 74X139 -- 2:4, 74X138 --  3:8
![[codificadores 1.png]]
as entradas G__ são canais de ativação / enables.
- Não percebi bem como funciona :DDDDD

### 3.3.3 - Descodificador para 7 segmentos
- Converte um código 4bits para outro de 7bits em que cada um faz acender ou não um dos 7 segmentos do mostrador.
- Usamos o 74X49:
![[7 segmentos.png]]

### 3.3.4 - Elevador
- Um exemplo prático é um elevador:
![[elevador exemplo.png]]
- Em cada piso temos um sensor que diz se o elevador está nele ou não (1 ou 0). 
- Obtemos então um código binário. O codificador faz esse processo: obtemos sinal de 4bits. Dado o contexto do problema, só podemos ter: $1000,0100,0010,0001$.
    - Mas há outro caso: quando o elevador está entre pisos iremos obter $0000$, o que não é ideal. Para evitar isto podemos acrescentar uma saída do codificador que dá 1 se pelo menos um sensor dá 1.
- O descodificador converte este sinal num sinal 7bits que permite usar o mostrador 7 segmentos.

- É possivel atribuir prioridades diferentes às entradas e saídas do codificador conforme a ordem em que são ativadas, de modo a evitar problemas quando 2 sinais são ativados ao mesmo tempo. No caso do elevador, isto seria o que ocorreria se tivessemos um outro codificador que deteta quando um botão de chamada fosse ativado em cada piso.

### 3.3.5 - Multiplexadores (Seletores)
- Temos 74X151 -- mux 8:1 , 74X153 -- 2 x mux 4:1 , 74X157 -- mux 2:1 (4bits)
- Tem $N$ entradas de seleção $S_{j}$, $2^{N}$ entradas de dados $I_{i}$ e 1 só saída $Y$
- Um mux com 2 linhas de seleção e 4 de dados seria representado assim:
![[mux.png]]
ou seja, as linhas de seleção descrevem um código binário cujo número decimal corresponde ao número da entrada que queremos (literalmente, seleciona o canal de entrada de dados)

- Podemos ainda usar o multiplexador como um gerador de função lógica:
![[mux 2.png]]
