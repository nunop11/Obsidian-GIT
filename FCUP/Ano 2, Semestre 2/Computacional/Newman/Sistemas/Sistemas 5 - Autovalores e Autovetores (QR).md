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

#computacional #programacao #matrizes #autovetores #autovalores 