### Informações
**Professor** : Hélio Mendonça
    Email : hsm@fe.up.pt
    Gabinete : I230 
**Testes** : 
    1. Semana de 1 de abril (esse dia em si é segunda feira de Páscoa)
    2. 20 de maio
**Avaliação** : Ver sigarra
**Projeto** : Feito a pares. Temos as últimas 2 semanas para o fazer.
**Programa** : Até ao teste 1 temos Eletrónica Digital. Depois e até ao fim do semestre temos Microprocessadores.

# 1 - Sistemas de Numeração e Aritmética
- Iremos representar um número $123$ na base $N$ como $123_{N}$.
- Numa base $N$ cada algarismo vai de $0$ a $N-1$.

## 1.1 - Bases
### 1.1.1 - Base binária
- No dia a dia contamos em base 10 - os algarismos vão de 0 a 9.
- Em eletrónica digital usamos base 2 (binário) - temos 0s e 1s. Um algarismo de código binário chama-se *bit*.
- Tendo $N$ bits podemos representar $2^{N}$ entidades diferentes.
- Por primeiros números binários inteiros são:
$$\begin{align*}
0_{10}=0_{2}\quad;\quad1_{10}=1_{2}\quad;\quad2_{10}=10\quad;\quad3_{10}=11_{2}\quad;\quad4_{10}=100_{2}\quad;\quad5_{10}=101_{2}\\
6_{10}=110_{2}\quad;\quad 7_{10}=111_{2}\quad;\quad8_{10}=1000_{2}\quad;\quad9_{10}=1001_{2}\quad;\quad 10_{10}=1010_{2}
\end{align*}$$
(podemos imaginar este vídeo: https://www.youtube.com/watch?v=zELAfmp3fXY)

### Números Inteiros
#### $2\to10$
- Consideremos um número em base 10. Temos:
$$452_{10}= 4\cdot10^{2}+5\cdot10^{1}+2\cdot10^{0}$$
- Ora, tendo um número em base binária temos precisamente o mesmo. Assim, tendo o número $1101_{2}$ podemos passá-lo para base 10 da seguinte forma:
$$1101_{2}=1\cdot2^{3}+1\cdot2^{2}+0\cdot2^{1}+1\cdot2^{0}=13_{10}$$
podemos ainda pensar nisto como somar os pesos ($2^{n}$) dos algarismos $\neq0$. Ou seja, tendo $11010$ temos: $11010_{2}=2^{4}+2^{3}+2^{1}=26_{10}$.
- Sendo assim, é útil saber as primeiras potências de base 2 de cor:
$$\begin{align*}
2^{0}=1 \quad;\quad 2^{1}=2 \quad;\quad 2^{2}=4 \quad&;\quad 2^{3}=8\quad;\quad 2^{4}=16\quad;\quad2^{5}=32\\
2^{6}=64 \quad;\quad 2^{7}=128\quad;\quad2^{8}=256\quad&;\quad2^{9}=512\quad;\quad2^{10}=1024\quad;\quad2^{11}=2048
\end{align*}$$

#### $10\to2$
- Simplesmente dividimos sucessivamente por 2:
![[10 to binario.png|450]]
e temos $37_{10}=100101_{2}$ (listamos os números conforme a seta)
- Por vezes, podemos simplesmente somar potências de base 2. Por exemplo: $37_{10}=32+4+1=2^{5}+2^{2}+2^{0}=100101_{2}$. No entanto, isto só funciona com números reduzidos.

### Números não inteiros
#### $2\to10$
- Consideremos um número não inteiro em base 10:
$$35,72=3\cdot10^{1}+5\cdot10^{0}+7\cdot10^{-1}+2\cdot10^{-2}$$
e, tal como fizemos para números inteiros, podemos usar a mesma lógica para números em base 2:
$$110,101_{2}=1\cdot2^{2}+1\cdot2^{1}+0\cdot2^{0}+1\cdot2^{-1}+0\cdot2^{-2}+1\cdot2^{-3}=6,625_{10}$$

#### $10\to2$
- Tratamos a parte inteira e decimal do número em separado. A parte interia dividimos por 2, como vimos atrás. A parte decimal multiplicamos por 2 e retiramos a parte inteira. Consideremos o número $3,25_{10}$:
![[10 to binario decimal.png|500]]
temos $3,25_{10}=11,01_{2}$
(Podemos pensar na parte de multiplicar por 2 como sendo dividir por $1/2=2^{-1}$)

- Pode ainda acontecer outra coisa: consonate multiplicamos a parte decimal por 2 podemos nunca chegar a um número inteiro:
![[10 to binario dizima infinita.png|500]]
e temos $0,72_{10}=0,101110000101(\dots)_{2}$. Isto é equivalente a ter $\frac{1}{3}=0,3333333\dots$

### 1.1.2 - Base Hexadecimal
- HexaDecimal == 16. Por vezes, usasse $H$ em índice para indicar esta base.
- Surge da necessidade de representar números maiores. Por exemplo: $300_{10}=100101100_{2}$.
- Assim, nesta base temos os algarismos $0\cdots9,A\cdots F$ ou seja $A=10,B=11,C=12,\dots$
#### $2\to16$
- Como $16=2^{4}$ escrever números nesta base consiste em agrupar números da base binária em grupos de 4, da vírgula para fora:
$$\begin{align*}
300_{10}&= 100101100_{2}=000100101100_{2}\\
&= \underbrace{0001}_{=1_{10}}~~\underbrace{0010}_{=2_{10}}~~\underbrace{1100}_{=12_{10}}= 12C_{16}=12C_{H}
\end{align*}$$

#### $16\to2$
- Fazemos o processo inverso. 
- Consideremos $C5_{H}$. Temos $C=12=1100_{2}$ e temos $5_{10}=0101_{2}$ (de notar que normalmente escreveríamos $5_{10}=101_{2}$ mas na base hexadecimal temos que ter grupos de 4 bits, portanto preenchemos os espaços que faltam com 0s). Temos então $$C5_{H}=11000101_{2}=197_{10}$$

### 1.1.3 - Base Octal
- Octal == 8
- Funciona de forma idêntica à base hexadecimal mas agrupamos os bits em grupos de 3.
- Temos os algarismos de $0$ a $7$.
#### $2\to8$
- Voltemos a considerar 300. Operamos quase da mesma forma que na base Hex:
$$\begin{align*}
300_{10}&= 100101100_{2}=\underbrace{100}_{=4_{10}}~~\underbrace{100}_{=5_{10}}~~\underbrace{100}_{=4_{10}}=454_{8}
\end{align*}$$

#### $8\to2$
- Novamente, o processo inverso:
- Consideremos $72_{8}$. Temos $7_{10}=111_{2}~~,~~2_{10}=10_{2}=010_{2}$ logo $$72_{8}=111010_{2}=58_{10}$$

## 1.2 - Operações
### 1.2.1 - Adição
- Consideremos que, em base 10, estamos a somar $173+329$:
![[soma 10.png|375]]
ora, isto do "e vai 1"/*carry* também acontece ao adicionar números em base binária.

- Consideremos $1011_{2}+0110_{2}$:
![[soma 2.png|400]]
vemos logo que se tem o mesmo sistema que na base decimal.
- Facilmente podemos verfiicar esta conta: $1011_{2}=11_{10}~~,~~110_{2}=6_{10}$. Ora, $10001_{2}=17_{10}=11+6$

- Podemos ainda facilmente determinar $1011_{2}+1000_{2}+111_{2}$:
![[soma 2-2.png|375]]
novamente, podemos verificar: $1011_{2}=11_{10}~~,~~1000_{2}=8_{10}~~,~~111_{2}=7_{10}$. Ora, $11010_{2}=26_{10}=11+8+7$
