- Temos 2 PCDs A e B. Queremos determinar a matriz 4x4 que minimiza o erro. Temos as coordenadas dos pontos da PCD:
$$R_{A},R_{B}~~-~~N\times4$$
- Temos:
$$R_{B}=HR_{A}~~~~,~~~~ H=\begin{pmatrix}R & t \\ 0 & 1\end{pmatrix}=\begin{pmatrix}R_{00} & R_{01} & R_{02} & t_{x} \\ R_{10} & R_{11} & R_{12} & t_{y} \\ R_{20} & R_{21} & R_{22} & t_{z} \\ 0 & 0 & 0  & 1\end{pmatrix}~~,~~4\times4$$
- Definimos o erro:
$$E=\|R_{B}-HR_{A}\|^{2}$$
e temos a solução LS:
$$\begin{align*}
\frac{\partial E}{\partial H}&= 0\\
2R_{A}(R_{B}-HR_{A})&= 0\\
H&= (R_{A}^{T}R_{A})^{-1}R_{A}^{T}R_{B}
\end{align*}$$

