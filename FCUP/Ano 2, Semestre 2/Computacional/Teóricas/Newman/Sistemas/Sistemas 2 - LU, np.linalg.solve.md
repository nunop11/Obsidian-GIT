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

# 4 - Solve
```
import numpy as np

x = np.linalg.solve(A,v)
```
- Esta função permite resolver sistema de equações lineares simultâneas de forma muito rápida.
- No mínimo, é bom para verificar os resultados que obtemos com os nossos programas.

#computacional #programacao #matrizes 
