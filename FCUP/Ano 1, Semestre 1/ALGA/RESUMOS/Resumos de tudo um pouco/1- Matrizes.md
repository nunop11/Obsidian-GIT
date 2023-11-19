# Matrizes
$$M=\begin{pmatrix}
1 & 2 & -2\\
3 & 0 & 2\pi
\end{pmatrix}$$
- Tendo uma matriz, diz-se que ela tem dimensões $m\times n$, com m a ser o *número de linhas (altura)* e n a ser o *número de linhas* (comprimento)
- Tendo uma matriz A, para representar uma certa entrada usa-se a notação $a_{ji}$, sendo j o número da sua linha (de cima para baixo) e i o número da sua linha (da esquerda para a direita). Por exemplo, na matriz acima, $m_{23}=2\pi$
## Soma de matrizes
- Simplesmente soma-se as suas entradas. Tendo duas matrizes:
$$\begin{align}
A=\begin{pmatrix} a & b \\ c & d \end{pmatrix} 
&&&
B=\begin{pmatrix}t & u \\ v & w\end{pmatrix}
\end{align}$$
, tem-se que:
$$A+B=\begin{pmatrix}a+t & b+u \\ c+v & d+w\end{pmatrix}$$
## Produto de matriz com escalar
- Só se multiplica cada entrada pelo escalar:
$$A=\begin{pmatrix}x\\y\end{pmatrix} \hspace{2cm} logo, \hspace{5mm}\alpha.A=\begin{pmatrix}\alpha x\\ \alpha y\end{pmatrix}$$

## Produto de matrizes
- Mais difícil de explicar, mas tendo 2 matrizes:
$$A=\begin{pmatrix}2&0\\1&0\\3&1\end{pmatrix} \hspace{1cm} e \hspace{1cm} B=\begin{pmatrix}0&1&0&5\\0&0&-1&1\end{pmatrix}$$
, assim tem-se:
$$A.B=\begin{pmatrix}0&2&0&10\\0&1&0&5\\0&3&-1&16\end{pmatrix}$$
- O que acontece é que pegámos em cada linha de A e fazemos o produto escalar dela com cada coluna de B, como se fossem vetores. O resultado do produto escalar da linha 1 de A com a primeira coluna de B irá dar origem à primeira entrada da linha 1 matriz do produto e por aí fora.
    - Vejamos como se obtiveram as entradas da linha 3 de $A.B$:
$$\begin{align}
0 &=(3,1)\cdot(0,0) \\ 3 &=(3,1)\cdot(1,0) \\-1 &=(3,1)\cdot(0,-1) \\16 &=(3,1)\cdot(5,1) \\
\end{align}$$
### Notas sobre produto de matrizes
- Tendo duas matrizes, $A, m\times n$ e $B,s\times l$ . O produto delas ($A\cdot B$) ==existe apenas se n=s== e será uma matriz de dimensões $m\times l$.
- O produto de matrizes <ins>NÃO É COMUTATIVO</ins>
- O produto de matrizes *é associativo*: $a(A\cdot B)=(aA) \cdot B$

## Matriz transposta
- Indicado por ter a matriz "elevada a T"
- Basicamente, a matriz é refletida através da diagonal principal:
$$A=\begin{pmatrix}2&0\\1&0\\3&1\end{pmatrix} \hspace{5mm} logo: \hspace{5mm} A^T=\begin{pmatrix}2&1&3\\ 0&0&1\end{pmatrix}$$
## Matriz Identidade
$$I_2=\begin{pmatrix}1&0\\0&1\end{pmatrix} \hspace{1cm} I_3=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix} \hspace{1cm} (...)$$

## Matrix Inversa
- Só matrizes ==quadradas têm inversa==
- A matriz inversa de A ($A^{-1}$) é aquela para o qual:
$$A \cdot A^{-1}=I_n$$
(Mais info abaixo)

## Determinante de Matrix
- Só pode ser calculado em matrizes quadradas
### De matriz 2x2
Tendo a matriz $A=\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}$, 2x2, então o seu determinante pode ser calculado
$$det\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}=a_{11}a_{22}-a_{12}a_{21}$$
### De matrix 3x3 
Tendo a matriz $A=\begin{pmatrix}a_{11}&a_{12}&a_{13}\\ a_{21}&a_{22}&a_{23}\\ a_{31}&a_{32}&a_{33}\end{pmatrix}$, 3x3, então o seu determinante pode ser calculado assim:
$$det\begin{pmatrix}a_{11}&a_{12}&a_{13}\\ a_{21}&a_{22}&a_{23}\\ a_{31}&a_{32}&a_{33}\end{pmatrix}= +a_{11}det(M_1) - a_{12}det(M_2) + a_{13}det(M_3)$$
- $M_1, M_2, M_3$ são os *menores* da matriz original. Cada um deles é obtido pegando um dos elementos da primeira linha. No caso de $M_1$ será $a_{11}$. Assim, tira-se a **a linha e a coluna** dessa entrada, ou seja, a primeira linha e a primeira coluna, ficando-se com a matriz quadrada 2x2, $\begin{pmatrix}a_{22}&a_{23} \\ a_{32}&a_{33}\end{pmatrix}=M_1$. Repete-se isto para cada elemento da primeira coluna de A. O determinante de A será a soma dos determinantes destes menores, sendo que serão multiplicados pela entrada de A correspondente e por +1 ou -1 alternadamente (começando com +1).
- Há muitas maneiras de fazer isto, e muitos vídeos na net que explicam muito melhor do que eu alguma vez conseguirei explicar por texto.

### De matrix nxn
- Aplica-se a mesma estratégia que nas matrizes 3x3. Vai-se repetindo até só restarem matriz 2x2, que podemos facilmente calcular.

### Casos especiais de determinantes
-> ==Matriz Diagonal== - Det(A) será o produto das entradas da diagonal.
-> ==Matriz triangular== - Det(A) será o produto das entradas da diagonal.

## Propriedades dos determinantes
Nota: todas as propriedades abaixo aplicam-se a **linhas e colunas** da matriz.
1. Se trocarmos a ordem de duas colunas de uma matriz, o sinal do determinante alterna
2. Se houverem duas colunas seguidas iguais, o determinante é zero
3. Se tivermos uma matriz A, de $det(A)=x$, e multiplicarmos uma das colunas por $t$, passaremos a ter $det(A)=xt$
4. Se a uma das colunas da matriz acrescentarmos um múltiplo de outra, o determinante não se altera
5. Para qualquer matriz quadrada, $det(A)=det(A^T)$
6. Para qualquer par de matrizes com a mesma dimensão, $det(A \cdot B)=det(A)det(B)$

### Info extra sobre determinantes
- Se tivermos um certo paralelogramo definido pelas vetores $A(a_1, a_2)$ e $B(b_1, b_2)$, tem-se que 
$$A_{paralelogramo}=\Biggr|det\begin{pmatrix}A\\ B\end{pmatrix}\Biggr|=\Biggr|det\begin{pmatrix}a_1&a_2\\ b_1 &b_2\end{pmatrix}\Biggr|$$
- Pode-se ainda calcular o volume de um paralelepípedo através dos vetores que o definem, verificar se pontos são complanares e obter a equação de um plano usando 3 vetores contidos nele usando o determinante.

## Matriz Inversa Pt.2
- Tendo $A$ e $A^{-1}$, a sua matriz inversa, tem-se que:
$$A\cdot A^{-1}=A^{-1}\cdot A = I$$
$$det(A^{-1})=\frac{1}{det(A)}$$
- A partir da segunda equação, conclui-se que ==se uma matriz tem inversa, det é diferente de 0==

### Cálculo de A^-1 com o método de Gauss
1. Parte-se da matriz estendida $(A|I)$. Por exemplo, se $A=\begin{pmatrix}1&2 \\ -3&2 \end{pmatrix}$, então teríamos:
$$\begin{pmatrix}
1 & 2 &\bigr|&1 & 0\\ -3&2&\bigm| &0&1\end{pmatrix}$$
2. Fazer mudanças às linhas da matriz até que do lado esquerdo da linha vertical fique a matriz identidade.
3. Se durante estas operações aparecer uma linha vazia, a matriz A não tem inversa
4. Se não aparecer nenhuma linha nula, no final deveremos de ter $(I|A^{-1})$

> Se soubermos que transformações transformam a matriz A em identidade, ao repetir essas transformações na matriz identidade iremos obter a matriz inversa de A.

#matrizes #alga 