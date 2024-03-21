- Iremos ver como resolver sistemas de equações lineares.
- Assim, consideremos este sistema:
$$\begin{cases}2\omega+x+4y+z=-4\\ 3\omega+4x-y-z=3\\ \omega-4x+y+5z=9\\ 2\omega-2x+y+3z=7 \end{cases} \Longrightarrow \begin{pmatrix}2&1&4&1\\3&4&-1&-1\\1&-4&1&5\\2&-2&1&3\end{pmatrix}\begin{pmatrix}\omega\\x\\y\\z\end{pmatrix}=\begin{pmatrix}-4\\3\\9\\7\end{pmatrix}$$
ora, podemos escrever a forma matricial como $$Ax=v$$
- Iremos ver várias técnicas úteis

# 1 - Eliminação Gaussiana
- Tendo o sistema escrito como $Ax=v$, recordemos algumas regras úteis:
    - Podemos multiplicar todos os termos de uma matriz por uma constante e a equação continua a ser válida e as solução não muda. Na forma matricial, se multiplicarmos os termos de uma linha da matriz $A$ por uma constante, também temos que multiplicar o termo dessa linha na matriz $v$.
    - Podemos combinar equações linearmente. Ou seja, se adicionarmos a uma linha da matriz $A$ um múltiplo de outra linha (e fizermos o mesmo na matriz $v$) então a solução não muda.

- Assim, conseguimos recordar ALGA. Ora, este método consiste em ir somando a linhas da matriz $A$ múltiplos de outras linhas até ficarmos com uma matriz diagonalizada.
- Ou seja, ficamos com uma matriz do tipo:
$$\begin{pmatrix}1&a_{01}&a_{02}&a_{03}\\0&1&a_{12}&a_{13}\\0&0&1&a_{23}\\0&0&0&1\end{pmatrix} \begin{pmatrix}\omega\\x\\y\\z\end{pmatrix}=\begin{pmatrix}v_{0}\\v_{1}\\v_{2}\\v_{3}\end{pmatrix}$$
isto equivale:
$$\begin{cases}\omega+a_{01}x+a_{02}y+a_{03}z=v_{0}\\ x+a_{12}y+a_{13}z=v_{1}\\ y+a_{12}z=v_{2}\\ z=v_{3}\end{cases}$$
- Daqui temos $z=v_{3}$
- Mas assim, $y=v_{2}-a_{23}z$ torna-se $y=v_{2}-a_{23}v_{3}$
- E da mesma form para $x$ e $\omega$. Basta ir substituindo "para cima".

- Assim, para resolver o sistema no topo desta página temos este código:
```
import numpy as np

A = np.array([[ 2, 1, 4, 1 ],
            [ 3, 4, -1, -1 ] , 
            [ 1, -4, 1, 5 ] , 
            [ 2, -2, 1, 3 ]], float)

v = np.array( [ -4, 3, 9, 7 ] ,float) 
N = len(v)

# Gaussian elimination 
for m in range(N):
    # Dividir todos os elementos da linha pelo elemento da diagonal
    div = A[m,m] 
    A[m, :] /= div 
    v[m] /= div
    
    # Subtrair a todas as linhas abaixo
    for i in range(m+1,N): 
        mult = A [i ,m] 
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

# Backsubstitution
x = np.empty(N,float)

# Percorrer matriz de cima para baixo e substituir
for m in range(N-1,-1,-1): 
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m, i] * x[i]

print(x)
```
- De notar que ao termo da diagonal pelo qual dividimos a linha chamamos de *pivô*

## 1.2 - Eliminação de Gauss Jordan
- Consiste em evitar fazer pivotagem. Para isso, continuamos a fazer eliminação de modo que a matriz se torna diagonal. Ou seja:
$$Ax=v\to Ix=v'\to x=v'$$
- Na prática:
```
def solveGJordan(A,v):
    M = A.copy()
    v = v.copy()
    N = len(u)

    for i in range(N):
        div = M[i,i]
        M[i,:] /= div
        v[i] /= div
        for m in range(i+1,N):
            mult = M[m,i]
            M[m,:] -= mult*M[i,:]
            v[m] -= mult*v[i]
            
# eliminar os elementos acima da diagonal
    for i in range(N-1,0,-1): 
        for m in range(i):
            mult = M[m,i]
            M[m,:] -= mult*M[i,:]
            v[m] -= mult*v[i]
            
    return v # o próprio vetor u corresponde à solução
```
- Ou seja, após fazer eliminação gaussiana da matriz, repetimos o processo com a matriz triangular, mas agora de baixo para cima. Do notar que apenas fazemos pivotagem na primeira parte. Na segunda não será necessário.
- Normalmente pior que eliminação gaussiana.

# 2 - Pivoting
$$\begin{pmatrix}0&1&4&1\\3&4&-1&-1\\1&-4&1&5\\2&-2&1&3\end{pmatrix}\begin{pmatrix}\omega\\x\\y\\z\end{pmatrix}=\begin{pmatrix}-4\\3\\9\\7\end{pmatrix}$$
- Temos este sistema. Ele é igual ao da secção anterior, mas o primeiro termo da 1ª linha é $0$. Ora, como na eliminação gaussiana dividíamos os termos pelo 1º, não podemos fazer isso quando ele é 0. Ou seja, precisamos de outro método.
- Assim, fazemos _pivoting_. Ou seja, trocamos 2 linhas (primeira e segunda), como temos abaixo:
$$\begin{pmatrix}3&4&-1&-1\\0&1&4&1\\1&-4&1&5\\2&-2&1&3\end{pmatrix}\begin{pmatrix}\omega\\x\\y\\z\end{pmatrix}=\begin{pmatrix}3\\-4\\9\\7\end{pmatrix}$$
de notar que temos também que trocar na matriz $v$, mas não trocamos na matriz $x$.

## Pivot Parcial
- Consiste em fazer a eliminação gaussiana como vimos antes mas:
1. A cada passo, ao chegar a uma linha $m$ procurar o elemento $m$ (que pertence à diagonal).
2. Ver todas as linhas abaixo e comparar o elemento $m$ de cada uma. Trocar a linha $m$ com aquela que tiver o elemento $m$ mais longe de 0.



# 3 - Decomposição LU
- Muitas vezes em física queremos resolver vários sistemas $Ax=v$, em que todos têm a mesma matriz $A$, mas matrizes $v$ diferentes. Nesses casos, é desnecessário fazer uma eliminação gaussiana para cada sistema, porque em todas elas iremos transformar $A$ na mesma matriz triangular, apenas $v$ irá mudar.
- Assim, temos o _método da decomposição LU_: em que "memorizamos" as operações feitas para tranformar $A$ numa matriz triangular, de modo a replicar essas operações em quantas matrizes $v$ quantas quisermos.

- Temos uma matriz:
$$A=\begin{pmatrix}a_{00} &a_{01} &a_{02} &a_{03}\\ a_{10} &a_{11} &a_{12} &a_{13}\\a_{20} &a_{21} &a_{22} &a_{23}\\a_{30} &a_{31} &a_{32} &a_{33}\end{pmatrix}$$
- Vamos então fazer eliminação gaussiana, mas de forma _matricial_.
- Ora, nós começamos por dividir toda a linha $0$ por $a_{00}$. De seguida subtraimos a todas as linhas $i$ abaixo de $0$ : $i \cdot\text{linha 0}$. Ou seja, temos:
$$\frac{1}{a_{00}} \begin{pmatrix}1 &0 &0 &0\\ -a_{10} &a_{00} &0 &0\\-a_{20} &0 &a_{00} &0\\-a_{0} &0 &0 &a_{00}\end{pmatrix}\begin{pmatrix}a_{00} &a_{01} &a_{02} &a_{03}\\ a_{10} &a_{11} &a_{12} &a_{13}\\a_{20} &a_{21} &a_{22} &a_{23}\\a_{30} &a_{31} &a_{32} &a_{33}\end{pmatrix} = \begin{pmatrix}1 &b_{01} &b_{02} &b_{03}\\ 0 &b_{11} &b_{12} &b_{13}\\ 0 &b_{21} &b_{22} &b_{23}\\ 0 &b_{31} &b_{32} &b_{33}\end{pmatrix}$$

de onde podemos definir:
$$L_{0}=\frac{1}{a_{00}} \begin{pmatrix}1 &0 &0 &0\\ -a_{10} &a_{00} &0 &0\\-a_{20} &0 &a_{00} &0\\-a_{30} &0 &0 &a_{00}\end{pmatrix}$$

- Continuando com a eliminação:
$$\frac{1}{b_{11}} \begin{pmatrix}b_{11} &0 &0 &0\\ 0 &1 &0 &0\\0 &-b_{21} &b_{11} &0\\0 &-b_{31} &0 &b_{11}\end{pmatrix}\begin{pmatrix}1 &b_{01} &b_{02} &b_{03}\\ 0 &b_{11} &b_{12} &b_{13}\\ 0 &b_{21} &b_{22} &b_{23}\\ 0 &b_{31} &b_{32} &b_{33}\end{pmatrix} = \begin{pmatrix}1 &c_{01} &c_{02} &c_{03}\\ 0 &1 &c_{12} &c_{13}\\ 0 &0 &c_{22} &c_{23}\\ 0 &0 &c_{32} &c_{33}\end{pmatrix}$$
de onde tiramos:
$$L_{1}=\frac{1}{b_{11}} \begin{pmatrix}b_{11} &0 &0 &0\\ 0 &1 &0 &0\\0 &-b_{21} &b_{11} &0\\0 &-b_{31} &0 &b_{11}\end{pmatrix}$$

- Logo, não é difícil concluir que teremos:
$$L_{2}=\frac{1}{c_{22}} \begin{pmatrix}c_{22} &0 &0 &0 \\ 0 &c_{22} &0 &0 \\ 0 &0 &1 &0 \\ 0 &0 &-c_{32} &c_{22} \end{pmatrix} \quad \quad;\quad \quad L_{3}=\frac{1}{d_{33}} \begin{pmatrix}d_{33} &0 &0 &0 \\ 0 &d_{33} &0 &0 \\ 0 &0 &d_{33} & 0\\ 0 &0 &0 &1\end{pmatrix}$$

- Ou seja, o que temos na eliminação Gaussiana é:
$$L_{3}L_{2}L_{1}L_{0}~Ax= L_{3}L_{2}L_{1}L_{0} ~v$$
- Na prática, interepretar a eliminação assim é melhor, porque as matrizes $L_{0},\dots,L_{3}$ contém todas as operações que precisamos de executar.
- Ou seja, tendo uma matriz 4x4, só precisamos de calcular $L_{0},L_{1},L_{2},L_{3}$ 1 vez e depois só temos que multiplicar por cada nova matriz $v$. 

- Ou seja, a decomposição em LU consiste nisto, em fazer a eliminação gaussiana com matrizes. No entanto, usamos outra técnica:
- Definimos $$\begin{align*}
L = L_{0}^{-1}L_{1}^{-1}L_{2}^{-1}L_{3}^{-1} \quad \quad \textsf{Lower triangular}\\
U = L_{0}L_{1}L_{2}L_{3}A \quad \quad \textsf{Upper triangular}
\end{align*}$$
de modo que $\large LU=A$, pelo que podemos reescrever o sistema $Ax=v$ como $$LUx=v$$
Ou seja, acabamos de decompor $A$ em $L$ e $U$.

- Ora, $L$ será uma matriz lower triangular, de forma que temos:
$$L_{0}=\frac{1}{a_{00}} \begin{pmatrix}1 &0 &0 &0\\ -a_{10} &a_{00} &0 &0\\-a_{20} &0 &a_{00} &0\\-a_{0} &0 &0 &a_{00}\end{pmatrix} \Longrightarrow L_{0}^{-1}= \begin{pmatrix}a_{00} &0 &0 &0\\ a_{10} &1 &0 &0\\a_{20} &0 &1 &0\\a_{30} &0 &0 &1\end{pmatrix}$$
Analogamente:
$$\small L_{1}^{-1}=\begin{pmatrix}1 &0 &0 &0 \\ 0 &b_{11} &0 &0 \\ 0 &b_{21} &1 &0\\ 0 &b_{31} &0 &1 \end{pmatrix} \quad;\quad L_{2}^{-1} = \begin{pmatrix}1 &0 &0 &0 \\ 0 &1 &0 &0 \\ 0 &0 &c_{22} &0\\ 0 &0 &c_{32} &1 \end{pmatrix} \quad ;\quad L_{3}^{-1} = \begin{pmatrix}1 &0 &0 &0 \\ 0 &1 &0 &0 \\ 0 &0 &1 &0\\ 0 &0 &0 &d_{33} \end{pmatrix}$$
de tal como que $$L=L_{0}^{-1}L_{1}^{-1}L_{2}^{-1}L_{3}^{-1}=\begin{pmatrix} a_{00} &0 &0 &0 \\ a_{10} &b_{11} &0 &0 \\ a_{20} &b_{21} &c_{22} &0\\ a_{30} &b_{31} &c_{32} &d_{33} \end{pmatrix}$$
- De recordar que fazemos operações com matrizes da direita para a esquerda. Ou seja, temos isto:
![[decomp LU.png]]
- Sendo que temos que fazer 2 _back substitutions_. Primeiro para obter $y_{0},y_{1},y_{2}$ e depois substituir isso em cima para obter $x_{0},x_{1},x_{2}$ (que são as verdadeiras soluções do sistema).
- De notar que é também preciso incluir _pivoting_.

# 4 - Np.Linalg.Solve
```
import numpy as np

x = np.linalg.solve(A,v)
```
- Esta função permite resolver sistema de equações lineares simultâneas de forma muito rápida.
- No mínimo, é bom para verificar os resultados que obtemos com os nossos programas.
- 

# 5 - Matriz inversa
- Uma forma bastante direta de resolver um sistema $Ax=v$ é multiplicar os 2 lados da equação pela _inversa de A_:
$$Ax=v \Longrightarrow A^{-1}Ax = A^{-1}v \Longrightarrow x=A^{-1}v$$
- No entanto, isto não é mutio eficiente.

- E, tal como já vimos antes, fazer as coisas da forma que faríamos em álgebra está longe do mais adequado a fazer com programação.
- Assim, começamos por consderar um sistema $$AX=V$$
mas em que agora temos que $X,V$ são matrizes $N \times N$.
- Para fazer isto, podemos usar eleminação gaussiana ou LU como vimos antes. Aqui, cada coluna de $X$ será a solução correspondente a uma coluna de $V$ 
- Consideremos agora que $V=I$, sendo $I$ uma _**matriz identidade**_. Assim, por definição:
$$AX=I \Longrightarrow X=A^{-1}$$
- Na prática, fazemos a eliminanação gaussiana como até agora, mas nas partes aplicavamos as mesmas alterações à matriz $v$ faze-mo-lo à matriz $I$:
![[codigo mat inversa.png]]

- Podemos ainda usar :
```
import numpy as np
(...)
X = np.linal.inv(A)
```



# 6 - Matriz Tridiagonal
- Este é um caso especial que frequentemente aparece em física. Temos um sistema $Av=x$, mas com $$A = \begin{pmatrix}a_{00} &a_{01} &0 &0 &0 \\ a_{10} &a_{11} &a_{12} &0 &0 \\0  &a_{21}&a_{22} &a_{23} &0 \\ 0 &0  &a_{32} &a_{33} &a_{34} \\ 0 &0 &0 &a_{43} &a_{44} \end{pmatrix}$$
- Ou seja, apenas temos elementão _não-zero na diagonal e subdiagonais superior e inferior_.
- Neste caso, eliminação gaussiana é suficiente. Isto porque, nem precisamos de fazer o método inteiro. Isto porque apenas precisamos de subtrair uma certa linha `m` à linha `m+1` e a mais nenhuma (porque ficaríamos com `A[m+2, :] -= 0 * A[m, :]`)
- Após a eliminação gaussiana, ficamos com uma matriz com 1s na diagonal principal e números não-zero apenas na diagonal superior. Tudo o resto são 0s. Ou seja, também a backsubstitution é mais simples.

- Mais concretamente, na backsubstitution ficamos com algo do tipo:
![[backsubstitution.png]]
- Ao método de eliminação de gauss simplificado explicado acima chamamos de _Thomas Algorithm_. Para matrizes tridiagonais, isto costuma ser mais rápido que o `np.linalng.solve`

# 7 - Matriz Banded
- Matrizes em que há mais do que 1 subdiagonal diferente de 0 acima e abaixo.
![[matriz banded.png]]
- Basicamente, podemos resolver estas matrizes ao simplificar o Thomas Algorithm:
    - Temos uma matriz com `N` subdiagonais não nulas, acima e abaixo
    - Ao fazer eliminação gaussiana, se tivermos na linha `m`:
        - Comparamos o elemento da diagonal, `A[m, m]`, apenas com os elementos na zona `A[m:m+N , m]` (`N` linhas abaixo da linha atual) para fazer pivotagem parcial.
        - Apenas subtraímos a linha `A[m, :]` às `m` linhas abaixo.
    - Fazemos backsubstitution conforme temos na imagem na secção acima, mais ou menos.

- Isto é um tipo comum de sistemas em física, pelo que é útil escrever um código geral que podemos usar sempre.

#  8 - Autovalores e Autovetores
- Este é um problema que frequente temos em física.
- Para uma _matriz simétrica_ $A$ temos:
$$A v = \lambda v$$
sendo $v$ um **autovetor** de $A$ e $\lambda$ o **autovalor** respetivo. Para uma matriz $N \times N$ temos $v_{1},\dots,v_{N}$ autovetores e $\lambda_{1},\dots,\lambda_{N}$ autovalores.
- Temos as propriedades:
    - $\large v_{i}\cdot v_{j}=0~~;~~i\ne j$ 
    - $\large v_{i}\cdot v_{i}=1$ -- _Vetores unitários_ (isto não é necessariamente verdade, mas iremos presumir que é este o caso)

- Assim, podemos definir $v_{1},\dots,v_{N}$ como sendo as colunas de uma matriz $V, ~N \times N$. Do mesmo modo, podemos definir $D$ como sendo uma matriz $N \times N$ diagonal, em que os termos da diagonal são $\lambda_{1}\dots\lambda_{N}$. Ou seja:
$$AV=VD$$
- De notar que $V$ é ortogonal, ou seja: $VV^{T}=V^{T}V=VV^{-1}=I$.

# 9 - Decomposição QR
- Basicamente temos (à semelhança de LU):
$$Ax=v \Longrightarrow QRx=v$$
sendo que, neste caso, $Q$ é uma matriz ortogonal e $R$ é uma matriz triangular superior.
- A forma como se obtem é:
> Temos uma matriz $$A= \begin{pmatrix}| &| &| &\dots \\ a_{0} &a_{1} &a_{2} &\dots \\ | &| &| &\dots\end{pmatrix}$$sendo $a_{0}, \dots, a_{N}$ os vetores correspondentes a colunas de $A$
> 
> Assim: 
> 
> $$\begin{align*}
u_{0} &= a_{0} \quad &;\quad q_{0}=\frac{u_{0}}{|u_{0}|}\\
u_{1} &= a_{1}-(q_{0}\cdot a_{1})q_{0} \quad &;\quad q_{1}=\frac{u_{1}}{|u_{1}|}\\
u_{2} &= a_{2} - (q_{0}\cdot a_{2})q_{0} - (q_{1}\cdot a_{2})q_{1} \quad &;\quad q_{2}=\frac{u_{2}}{|u_{2}|}\\
&\dots &\dots \quad \quad\\
u_{n}&= a_{n} - \sum\limits_{i=0}^{n-1} (q_{i}\cdot a_{n})q_{i} \quad &; \quad q_{n}= \frac{u_{n}}{|u_{n}|}
\end{align*}$$
> 
> Sendo que ficamos com $$\small Q= \begin{pmatrix}| &| &| &\dots \\ q_{0} &q_{1} &q_{2} &\dots \\ | &| &| &\dots\end{pmatrix} \quad \quad;\quad \quad R= \begin{pmatrix}|u_{0}| &q_{0}\cdot a_{1} &q_{0}\cdot a_{2} &\dots &q_{0}\cdot a_{N-1}\\ 0 &|u_{1}| & q_{1}\cdot a_{2} &\dots &q_{1}\cdot a_{N-1}\\ 0 &0 &|u_{2}| &\dots &q_{2}\cdot a_{N-1} \\ \vdots &\vdots &\vdots &\ddots &\vdots \\ 0 &0 &0 &\dots &|u_{N-1}|\end{pmatrix}$$sendo $Q, U, R$ matrizes $N \times N$.

- Ora, vejamos como obter autovalores e autovetores.
- Se tivermos uma matriz $A$ e a decomposermos em $Q,R$ temos:
$$A = Q_{1}R_{1}$$
podemos multiplicar tudo por $Q^{T}$ e, como por definição $Q$ é ortogonal, temos $Q^{T}Q=I$, ou seja:
$$A=Q_{1}R_{1}\Longrightarrow Q_{1}^{T}A=Q_{1}^{T}Q_{1}R_{1}\to Q_{1}^{T}A=R_{1}$$
- Podemos então definir uma nova matriz $A_{1}$ tal que $$\begin{align*}
A_{1}=R_{1}Q_{1}\\
A_{1}=Q_{1}^{T}AQ_{1}
\end{align*}$$em que apenas subtituimos $R_{1}=Q_{1}^{T}A$, conforme obtivemos acima.

- Da mesma forma temos:
$$\begin{align*}
A_{2}&= Q_{2}R_{2}\\
A_{2}&= Q_{2}^{T}Q_{1}^{T}AQ_{1}Q_{2}
\end{align*}$$
- Isto repete-se sempre assim, de forma que temos:
$$A_{k}=(Q_{k}^{T}\dots Q_{1}^{T})A(Q_{1}\dots Q_{k})$$
- Se continuarmos a repetir isto, os elementos fora da diagonal vão-se tornando cada vez menores, de forma que, eventualemente obtemos uma matriz $A_{k}$ que é basicamente *diagonal*, a que chamaremos $D$.
- Ora, podemos também definir $V=Q_{1}Q_{2}\dots Q_{k}=\prod\limits_{i=1}^{k}Q_{i}$
- Ora, podemos escrever aquilo acima como:
$$A_{k}=V^{T}AV=D$$
o que é equivalente a $$AV=DV$$
- Ora, vemos facilmente que isto é a definição de um autovetor. Ou seja, a _diagonal de D é os autovalores_ e _V dá os autovetores_

## 9.1 - Aplicar
- Na prática, o que fazemos é:
1. Escolher uma precisão $\epsilon$ do programa. Criar $V$, uma matriz identidade $N \times N$ que irá guardar os autovetores.
2. Fazer decomposição $A=QR$
3. Fazer $A=RQ$, o que nos faz perder a matriz original
4. Multiplicar `V @ Q` (ou `np.dot(V, Q)`)
5. Se todos os valores de $A$ forem menor que $\epsilon$ acabou. Senão, voltar ao passo 2.

## 9.2 - Numpy
- Tal como no `np.linalg.solve`, o numpy traz funções para obter os autovalores e autovetores. Fazemos isto:
```
A = np.array([[------], [------], ...])

X, V = np.linalg.eigh(A)
```
sendo que neste código, ficamos com `X` um array com os autovalores e `V` um array com os autovetores.

- Por vezes queremos apenas os _autovalores_. E é útil calculá-lo apenas a eles, pois calcular os autovetores gasta mais tempo, porque exige muitas operações. Assim, para obter _apenas_ os autovalores temos:
```
x = np.linalg.eigvalsh(A)
```

- De notar que as 2 funções acima são apenas para ***Matrizes simétricas***. Se colocarmos uma matriz não simetrica, as funções presumem que a metade acima da diagonal é igual à metade inferior.
- Estas funções funcionam com valores complexos (consideram a matriz como hermitiana).

## 9.3 - QR Householder
- Ao fazer $QR$ obtemos uma matriz $Q$ em que cada coluna $Q_{i}$ é dada por:
$$
\mathbf{Q}_i = \mathbf{I}-2\mathbf{v}_i\mathbf{v}_i^T\,, \quad \quad \mathbf{v}_i = \frac{\mathbf{x}_i-||\mathbf{x}_i||\mathbf{e}_i}{||\mathbf{x}_i-||\mathbf{x}_i||\mathbf{e}_i||}
$$
sendo $\mathbf{e}_{i}$ é o vetor unitário dessa direção (todos os elementos 0 exceto o elemento $i$)
que na prática usamos assim:
![[qr v2.png]]
(não entendo quase nada do que está aqui escrito)

# 10 - Método de Relaxação
- Consideremos que temos a seguinte equação:
$$x = 2 - e^{-x}$$
- Um método computacional comum para resolver equações é _iteração_. Basicamente, escolhemos um valores inicial e continuamos a partir daí:
$$\begin{align*}
x_{0}&= 1 \\
x_{1}&= 2 - e^{-1} \approx 1.632 \\
x_{2}&= 2- e^{-1.632} \approx 1.804
\end{align*}$$
- Ora, é preciso ter uma equação do tipo $\large x=f(x)$, em que $f$ é uma função conhecida. Por vezes temos que reorganizar a função para ficar nesta forma.
- Além disso, isto apenas funciona quando $f(x)$ ***converge***.
- Mesmo aí, devemos notar que a função $f$ pode ter 2 ou mais soluções. No entanto, podemos resolver isto ao variar $x$. Isto porque este método irá converter para a solução mais próxima de $x_{0}$.

- Às vezes, em vez de converger, o método começa a oscilar entre2 valores, tal como acontecer com $x=e^{1-x^{2}}~~;~~x_{0}=\frac{1}{2}$. Por vezes, podemos resolver isto  ao restruturar a equação. No exemplo acima, se fizermos logaritmos dos 2 lados e reorganizarmos algumas coisas conseguimos obter $x=\sqrt{1-\log x}$ . Esta equação já converge.

## 10.1 - Explicação analítica
- Consideremos a equação $x=f(x)$, que tem a solução $x=x^{*}$ 
- Assim, algures durante o método iremos ter $x'$ (que consideramos que está próximo de $x^{*}$), sendo que a tentativa anterior é $x$. Assim, temos $x'=f(x)$. Podemos expandir isto em série de Taylor:
$$x' = f(x) = f(x^{*}) + (x-x^{*})f'(x*)$$(em que ignoramos os termos a partir da 2ª derivada)
- Ora, $x^{*}$ é a solução pelo que $f(x^{*})=x^{*}$. Podemos então escrever a equação acima como: $$x'-x^{*}=(x-x^{*})f'(x^{*})$$
- Ou seja, a distância a que estamos da solução numa certa tentativa é apenas multiplicada pela derivada de $f$ na solução ao passar para a tentativa seguinte.
- Ou seja, o método apenas converge se $\large |f'(x^{*})|<1$. Este é o *critério a verificar*.
- No entanto, se tivermos $|f'(x^{*})|>1$, na maioria dos casos teremos $|(f^{-1})'(x^{*})|<1$. Ou seja, se a função não converter, queremos transformá-la na **função ivnersa**.

- Ou seja, neste método só iremos obter a solução se o método convergir. Por vezes, uma função em que o método não converge pode ser resolvida ao usar a função inversa. Mesmo aí, o método pode não ser útil.

## 10.2 - Rate de conversão
- Assumindo que uma certa função $f$ converge, é importante saber o quão rápido o faz.
- Isto é-nos dado pela equação que vimos acima: $\large x' -x^{*}=(x-x^{*})f'(x^{*})$. Como $f'(x^{*})$ é constante, temos que a distância à solução diminui *exponencialmente* com o número de iterações. Existem métodos mais rápidos, mas isto é bom.

- No entanto, também é útil saber quando parar de iterar.
- Se precisamos apenas de uma solução rápida e *precisão não é o nosso maior foco*. Por exemplo, consideremos que apenas queremos uma precisão de 6 casas decimais. Assim, podemos simplesmente iterar até vermos que as primeiras 6 casas deixam de variar.

- Por outro lado, podemos querer ser *muito precisos* ou se queremos parar mal tenhamos a precisão desejada (por *performance*). Vejamos como proceder:
- Seja $\epsilon$ o erro de 1 certa iteração, tal que $x^{*}=x+\epsilon$ em que, novamente, $x^{*}$ é a solução verdadeira. Analogamente, $\epsilon'$ ser+a o erro da iteração $x'$. Daqui temos $x-x^{*}=-\epsilon~~,~~x'-x^{*}=\epsilon'$. Assim, podemos reescrever:
$$x'-x^{*}=(x-x^{*})f'(x^{*}) \Longrightarrow \epsilon'=\epsilon f'(x^{*})\leftrightarrow \epsilon= \frac{\epsilon'}{f'(x^{*})}$$
Ou seja:
$$x^{*}=x+\epsilon=x+\frac{\epsilon'}{f'(x^{*})}=x'+\epsilon'$$
Daqui temos:
$$\epsilon'= \frac{x-x'}{1 - \frac{1}{f'(x^{*})}}\sim \frac{x-x'}{1- \frac{1}{f'(x)}}$$
Aqui presumimos que $x$ está próximo de $x^{*}$, daí $f'(x^{*})\approx f'(x)$
- Assim, deste modo podemos determinar o erro da nossa tentativa, usando a _tentativa anterior e sem saber o valor real_. 
- No entanto, isto implica que conheçamos $f$ e consigamos determinar $f'$. Por vezes, podemos ter que obter derivadas, como vimos na devida secção.

- Mas podemos fazer isto sem usar derivadas.
- Tendo 3 tentativas consecutivas: $x,x',x''$, tem-se que o erro da última é $$\epsilon''\approx \frac{x'-x''}{1- \frac{1}{f'(x)}}$$
- Ora, temos que $f'(x)\approx \frac{f(x)-f(x')}{x-x'}$ para 2 pontos $x,x'$ próximos. Temos ainda que, neste método, cada $x'$ é a imagem do $x$ anterior, $f(x)=x'$ e $f(x')=x''$. Ou seja, $f'(x)\approx \frac{x'-x''}{x-x'}$
- Assim, ao substituir na equação de $\epsilon''$ acima, temos:
$$\epsilon''= \frac{x'-x''}{1- \frac{x-x'}{x'-x''}}= \frac{(x'-x'')^{2}}{2x'-x-x''}$$
- Ou seja, podemos obter o erro sem derivadas, se mantivermos as últimas 3 tentativas.

## 10.3 - Relaxação para 2+ variáveis
- Se tivermos $N$ equações de $N$ variáveis $x_{1},x_{2},\dots,x_{N}$ que consguimos reescrever na forma:
$$\begin{align*}
x_{1}&= f_{1}(x_{1},x_{2},\dots,x_{N})\\
x_{2}&= f_{2}(x_{1},x_{2},\dots,x_{N})\\
&\dots\\
x_{N}&= f_{N}(x_{1},x_{2},\dots,x_{N})
\end{align*}$$
- Podemos escolher valores iniciais para cada variável e utilizar o método da relaxação. Se após um certo número de iterações todas as variáveis tiverem valores constantes, essas serão as soluções do sistema de equações não-lineares.
- No entanto, mais uma vez, é preciso que todas as funções convirjam.

## 10.4 - Sobre-relaxação sucessiva
- Acrescentamos um parâmetro $\omega$ para fazer overshoot ao passar para a próxima tentativa. Na prática, se $\omega$ for um bom valor, isto vai fazer com que tenhamos convergência mais rápido. Isto assemelha-se ao que temos no método de *Descida do Gradiente* na secção de Máximos e Mínimos.
- Temos:
$$x'=(1+\omega)f(x)-\omega x$$send o erro:
$$\epsilon'=\frac{x-x'}{1- \frac{1}{(1+\omega)f'(x)-\omega x} }$$
- $\omega$ é obtido por tentativa e erro. Se:
    - *omega postivo* - convergência direta e mais rápida
    - *omega negativo* - convergência oscilatória com amplitudes cada vez menores

# 11 - Binary Search
- Método mais robusto para resolver equações não lineares de 1 variável $x$.
- De uma forma reduzida, definimos um intervalo em que queremos encontrar 1 solução da equação e este método vai sempre encontrá-la.

- Tendo uma equação de 1 variável qualquer, podemos sempre colocá-la na forma $\large f(x)=0$. Assim, ao procurar soluções estamos na realidade a procurar _zeros/raízes_. Esta é a base do método de Binary Search.

![[binary search.png]]

### Explicação do método
- Assim, queremos encontrar um zero de $f$ entre $x_{1}$ e $x_{2}$. 
- Começamos por determinar $f(x_{1}), f(x_{2})$. 
    - Podemos ter que um destes pontos é positivo e outro negativo. Neste caso, desde que a função $f$ seja contínua, temos pelo menos 1 zero neste intervalo.
- De seguida determinamos $f(x')$, a imagem do ponto médio do intervalo: $\large x'=\frac{1}{2}(x_{1}+x_{2})$. 	
- Se $f(x')=0$ já temos o zero. Senão, este ponto será necessariamente positivo ou negativo. Ou seja, tem o mesmo sinal que um dos pontos $f(x_{1}),f(x_{2})$ e sinal oposto ao outro. Consideremos o caso na figura acima: $f(x')$ tem sinal oposto $f(x_{1})$.
- Assim, tal como vimos antes, se $f(x_{1}),f(x')$ têm sinais opostos e $f$ é contínua, deverá haver 1 zero entre $x_{1}$ e $x'$. No entanto, a distância entre estes 2 pontos é metade daquela entre os 2 pontos iniciais.
- Assim, repetimos o processo, ficando cada iteração com um intervalo menor por um fator de 2, até encontrar o zero.

### Explicação para fazer código
1. Decidir os limites do intervalo: $x_{1},x_{2}$ e a precisão $\epsilon$ que desejamos.
2. Determinar as respetivas imagens: $f(x_{1}),f(x_{2})$ e ver se têm sinais opostos.
3. Determinar o ponto médio: $x'=\frac{1}{2}(x_{1}+x_{2})$ e calcular $f(x')$
4. Se $x'$ tem o mesmo sinal que $x_{1}$ definir $x_{1}=x'$. Caso contrário, $x_{2}=x'$
5. Voltar ao passo 2 e repetir até $|x_{1}-x_{2}|<\epsilon$. Se tivermos a precisão desejada, obter o ponto médio uma última vez e isso será o zero.

## 11.1 - Rapidez e Nº de Passos
- Tal como o método de relaxação, o _erro diminui exponencialmente com as iterações_.
- Consideremos que os pontos iniciais $x_{1},x_{2}$ estão a uma distância $\Delta$. Em cada iteração dividimos essa distância em 2. Ou seja, a distância do intervalo após $N$ iterações é $\Delta/2^{N}$. Ou seja, se queremos uma precisão $\epsilon$, o número de iterações que precisamos é:
$$N = \log_{2} \frac{\Delta}{\epsilon}$$
- Assim, este método é muito rápido. Por exemplo, se tivermos $\Delta=10^{10}, \epsilon=10^{-10}$, precisaremos apenas de $\approx 67$ passos.

## 11.2 - Aplicação e problemas
- Se $f(x_{1}),f(x_{2})$ tiverem o mesmo sinal, ou a função não tem zeros ou tem um número par. Em ambos os casos, o método não funciona.
- Muitas vezes, ao usar este método não fazemos ideia de onde esperamos ter zeros (ou se eles existem), portanto quaisquer $x_{1},x_{2}$ por mais longe que estejam servem, desde que tenham _sinais opostos_.
- Se a função, por alguma razão física, será negativa ou positiva a partir de um certo valor, devemos usar isso para definir o intervalo inicial.
- Se esperamos ter um zero num certo $x$, começar com $x_{1},x_{2}$ próximos de $x$. Se não encontrarmos zero, duplicar $x_{1},x_{2}$ e repetir.
- Outra situação em que o método falha é **raízes múltiplas par**: como temos por exemplo em $f(x)=(1-x)^{2}$. Nestes casos, a função passa no zero mas *não muda de sinal*, pelo que o método não deteta o zero.
- Por fim, este método não funciona para resolver sistemas de equações.

# 12 - Método de Newton-Raphson
***AKA Método de Newton***
![[newton raphson.png]]
- Tal como no Binary Search, começamos por colocar a equação num formato $f(x)=0$
- Primeiro escolhemos 1 ponto inicial $x$. Usando o declive da tangente nesse ponto obtemos outro. Assim:
    - Em $x$ temos: $\large f'(x)\approx f\frac{x}{\Delta x}$
    - Daí temos a nossa próxima tentativa: $$\begin{align*}x' &= x-\Delta x\\ x' &= x - \frac{f(x)}{f'(x)}\end{align*}$$
- E é isto. Este método, apesar de tornar necessário que saibamos a derivada, permite obter o zero rapidamente.
- Além disso, este método tende a levar-nos para o zero mais próximo de $x$. Assim, se houver vários zeros, basta variar $x$ que eventualmente conseguiremos obter todos os zeros.

## 12.1 - Erros
- Tal como antes, vamos considerar $x^{*}$ o zero verdadeiro
- Novamente, temos a série de Taylor:
$$f(x^{*})= f(x)+ (x^{*}-x)f'(x) + \frac{1}{2}(x^{*}-x)^{2}f''(x)+\dots $$
- Mas, como $x^{*}$ é um zero, $f(x^{*})=0$. Dividindo tudo por $f'(x)$ temos:
$$x^{*}= \left[ x- \frac{f(x)}{f'(x)} \right] - \frac{1}{2}(x^{*} -x)^{2} \frac{f''(x)}{f'(x)}+\dots$$
mas, tal como definimos antes: $x' = x - \frac{f}{f'}$, logo:
$$x^{*}=x' - \frac{1}{2}(x^{*} -x)^{2} \frac{f''(x)}{f'(x)}+\dots$$
- Ora, definindo $x^{*}=x+\epsilon$ temos $\epsilon=x^{*}-x$. Analogamente, $x^{*}=x' + \epsilon'$. Juntando esta 2 equações com a de cima temos
$$\epsilon'= \left[ \frac{-f''(x)}{2f'(x)} \right]\epsilon^{2}$$
- Ou seja, o erro evolui de forma **quadrática**: $\epsilon\to \epsilon^{2}$. Isto é bastante mais rápido que os métodos de relaxação e binary search. Na prática isto quer dizer que se o erro inicial for $\epsilon_{0}$ e se tivermos $\frac{-f''(x)}{2f'(x)}\approx~constante~=c$, então após $N$ iterações o erro será $\epsilon\approx (c \epsilon_{0})^{2^{N}}$. Ou seja, será a *exponencial de uma exponencial*.

### 12.1.1 - Erros, mas útil
- No entanto, na prática não precisamos de fazer derivadas.
- Temos que $x^{*}=x+\epsilon$ e $x^{*}=x'+\epsilon'=x'+c \epsilon^{2}$ (conforme a fórmula do erro teórico). Ao igualar as 2 equações temos:
$$\begin{align*}
x+\epsilon&= x' + c \epsilon^{2}\\
x' - x &= \epsilon-c \epsilon^{2}\\
x' - x &= \epsilon(1-c \epsilon) \approx \epsilon
\end{align*}$$
- Ou seja, para saber o erro de uma tentativa $x$ basta ver a ***distância para a tentativa seguinte***, $x'$.
- Outra forma de interpretar isto é ver que este método converge tão rápido que a próxima tentativa já é tão boa que basicamente já é o zero.
- Por outro lado, para obter o erro em $x'$ precisamos de fazer a iteração anterior.

## 12.2 - Problemas
1. Para usar este método temos que saber a derivada $f'$
2. O método nem sempre converge.
    - Isto pode acontecer por a derivada ser muito baixa e então ao fazer $x' = x - \frac{f}{f'}$ apenas nos estamos a afastar do zero.
    - Por outro lado podemos ter um caso como na figura abaixo em que a derivada no ponto em que estamos apontar para o lado oposto ao zero:
![[newton raphson 2.png]]


# 13 - Método da Secante
- Como vimos, o método de Newton exige ter uma função para a derivada de $f$
- No entanto, isto nem sempre é possível. Assim, podemos "adaptar" o método de Newton, usando conhecimentos do capítulo de derivadas.

1. Começamos com os pontos $x_{1},x_{2}$, que escolhemos. Ao contrário de binary search, não precisa de estar um de cada lado do zero.
2. Calculamos uma aproximação da derivada em $x_{2}$: $$f'(x_{2})\approx \frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}$$
3. Aplicamos o método de Newton ($x_{2}=x_{1}-f(x_{1})/f'(x_{1})$) com esta aproximação da derivada: $$x_{3}=x_{2}-f(x_{2}) \frac{x_{2}-x_{1}}{f(x_{2})-f(x_{1})}$$
4. Repetir como no método de Newton.

- Ora, de notar que neste método precisamos de usar as *duas últimas tentativas*, ao contrário de usar apenas a última no método de Newton.


# 14 - Método de Newton para 2+ Variáveis
- Tendo um sistema de $N$ equações, de $N$ variáveis, começamos por o escrever da forma:
$$\begin{cases}f_{1}(x_{1},x_{2},\dots,x_{N})=0 \\ f_{2}(x_{1},x_{2},\dots,x_{N})=0\\ \quad\quad\vdots\\f_{N}(x_{1},x_{2},\dots,x_{N})=0
\end{cases}$$
- Consideremos que a solução verdadeira do sistema é $x_{1}^{*},x_{2}^{*},\dots,x_{N}^{*}$. Podemos fazer a expansão em Taylor:
$$f_{i}(x_{1}^{*},\dots,x_{N}^{*})=f_{i}(x_{1},\dots,x_{N}) + \sum\limits_{j}(x_{j}^{*}-x_{j}) \frac{\partial f_{i}}{\partial x_{j}}+\dots$$
que, na forma matricial, pode ser escrito como:
$$\mathbf{f}(\mathbf{x}^{*})=\mathbf{f}(\mathbf{x}) + \mathcal{J}\cdot(\mathbf{x}^{*}-\mathbf{x})+\dots$$
sendo:
- $\mathbf{f}$ - lista das $f_{1},\dots,f_{N}$ funções do sistema
- $\mathbf{x^{*}}$ - lista dos zeros $x_{1}^{*},\dots,x_{N}^{*}$ do sistema
- $\mathbf{x}$ -  lista dos valores das variáveis $x_{1},\dots,x_{N}$
- $\mathcal{J} \longrightarrow J_{ij}=\frac{\partial f_{i}}{\partial x_{j}}$ - Matriz *Jacobiana* $N \times N$

- Por definição de zero de uma função, $\mathbf{f}(\mathbf{x}^{*})=0$
- Se definirmos $\Delta \mathbf{x}=\mathbf{x}-\mathbf{x}^{*}$ e ignorarmos os termos acima da 1ª derivada temos:
$$\mathcal{J}\cdot \Delta \mathbf{x}=\mathbf{f}(\mathbf{x})$$
- De realçar que, em computacional, a matriz jacobiana acima consiste em calcular todas as derivadas em $\mathbf{x}$.
- Isto não passa de um sistema $Ax=v$. Podemos usar qualquer um dos métodos anteriores e obter $\Delta \mathbf{x}$.
- Assim, e recordemos que $\mathbf{x}$ é apenas a 1ª tentativa, temos a próxima tentativa:
$$\mathbf{x}'=\mathbf{x} - \Delta \mathbf{x}$$


# 15 - Cenas do Viana
 - Esta secção é composta por coisas que foram dadas pelo Viana mas não estão no Newman.
## 15.1 - Método de Jacobi
- Uma matriz $A$ é *diagonal-Dominante* se: $$|a_{ii}|> \sum\limits_{i\ne j} |aij|, \forall i$$
Ou seja, em todas as linhas, o elemento da diagonal é o maior elemento, em módulo.

- Tendo um sistema $Ax=v$, sendo $A$ diagonal-dominante, podemos escrever:
$$A=D+L+U$$
sendo esta matrizes: a sua diagona, uma triangular inferior e uma triangular superior.
- A solução poderá convergir, de modo que ao iterar várias vezes temos:
$$x_{n+1}=D^{-1}(v-(L+U)x_{n})$$
e temos $$(x_{n})_{i} = \frac{1}{a_{ii}} (v_{i}- \sum\limits_{i\ne j} a_{ij}(x_{n-1})_{j})$$(isto não passa de eliminação de gauss)

### 15.1.1 - Na prática
![[Attachments/FCUP/A2S2/Computacional/codigo jacobi.png]]
- Podemos ver que isto consiste em apenas aplicar a última fórmula.
- Se a matriz não for diagonal-dominante, não teremos convergência

## 15.2 - Método de Gauss-Seidel
- Também precisamos de ter uma matriz Diagonal-Dominante para haver convergência
- Agora definimos: $$A=L+U$$
sendo ambas matrizes triangulares (inferior e superior) com 0s na diagonal principal.

- Da iteração temos:
$$x_{n+1}=L^{-1}(v- Ux_{n})$$
e temos, para cada elemento: $$(x_{n})_{i}=\frac{1}{a_{ii}} \left(v_{i} -\sum\limits_{j=1}^{i-1}a_{ij}(x_{n})_{j} - \sum\limits_{j=i+1}^{N}a_{ij}(x_{n-1})_{j} \right)$$
## 16.1 - Na prática
![[gauss seidel.png]]

#computacional #programacao #matrizes 