- Uma esfera é definida por:
$$\begin{align*}
(x-x_{c})^{2}+ (y-y_{c})^{2}+ (z-z_{c})^{2}&= r^{2}\\
x^{2}-2xx_{c}+x_{c}^{2}+y^{2}-2yy_{c}+y_{c}^{2}+z^{2}-2zz_{c}+z_{c}^{2}&= r^{2}\\
2xx_{c}+2yy_{c}+2zz_{c}+(r^{2}-x_{c}^{2}-y_{c}^{2}-z_{c}^{2})&= x^{2}+y^{2}+z^{2}
\end{align*}$$
- Consideremos agora que $x=X=\begin{pmatrix}x_{1} & x_{2} & x_{3} & \cdots\end{pmatrix}^{T}$ e igual para $y,z$. Temos uma equação matricial:
$$\begin{align*}
2Xx_{c}+2Yy_{c}+2Zz_{c}+(r^{2}-x_{c}^{2}-y_{c}^{2}-z_{c}^{2})\mathbb{1}&= \begin{pmatrix} X^{2} & Y^{2} & Z^{2}\end{pmatrix}\mathbb{1}\\
&= f
\end{align*}$$
e podemos escrever isto como um problema de regressão linear:
$$f=A \theta$$
em que:
$$\begin{align*}
f&= \begin{pmatrix}X^{2} & Y^{2} & Z^{2}\end{pmatrix}\begin{pmatrix}1\\
1\\
1\end{pmatrix}= \begin{pmatrix}x_{1}^{2}+y_{1}^{2}+z_{1}^{2}\\ x_{2}^{2}+y_{2}^{2}+z_{2}^{2}\\
\vdots\\
x_{n}^{2}+y_{n}^{2}+z_{n}^{2}
\end{pmatrix}~~,~~N\times1\\
\theta&= \begin{pmatrix}2x_{c}\\
2y_{c}\\
2z_{c}\\
r^{2}-x_{c}^{2}-y_{c}^{2}-z_{c}^{2}\end{pmatrix}~~,~~ 3\times1\\
A&= \begin{pmatrix}X & Y & Z & \mathbb{1}\end{pmatrix}=\begin{pmatrix}x_{1} & y_{1} & z_{1} & 1\\
x_{2} & y_{2} & z_{2} & 1\\
\vdots & \vdots & \vdots & \vdots\\
x_{n} & y_{n} & z_{n} & 1\end{pmatrix}~~,~~N\times3
\end{align*}$$
e podemos determinar $\theta$ com um método LS:
$$\theta = (A^{T}A)^{-1}A^{T}f$$
que resulta de: $\frac{df}{d\theta}=0$ (minimizar o erro). 