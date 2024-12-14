**Output theta**
- Consideremos que podemos medir $\theta$. Neste caso teremos $y=\theta$ invés de $y=\begin{pmatrix}\theta &  \dot{\theta}\end{pmatrix}^{T}$
- Assim, como $$\begin{align*}
\dot{x}&= (A-BK)x\\
y&= Cx
\end{align*}$$
temos a segunda equação
$$\theta= C \begin{pmatrix}\theta \\ \dot{\theta}\end{pmatrix}$$
temos que ter:
$$C=\begin{pmatrix}1 & 0\end{pmatrix}$$
- Assim, a matriz de observabilidade associada a este output é:
$$O_{\theta}=\begin{pmatrix}C \\ C(A-BK)\end{pmatrix}=\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$$
que tem $\text{rank}(O_{\theta})=2$ logo o sistema é completamente observável a partir de $\theta$

**Output derivada de theta**
- Consideremos que podemos medir $\dot{\theta}$. Neste caso teremos $y=\dot{\theta}$ invés de $y=\begin{pmatrix}\theta &  \dot{\theta}\end{pmatrix}^{T}$
- Assim, como 
$$\begin{align*}
\dot{x}&= (A-BK)x\\
y&= Cx
\end{align*}$$
temos a segunda equação
$$\dot{\theta}= C \begin{pmatrix}\theta \\ \dot{\theta}\end{pmatrix}$$
temos que ter:
$$C=\begin{pmatrix}0 & 1\end{pmatrix}$$
- Assim, a matriz de observabilidade associada a este output é:
$$O_{\dot{\theta}}=\begin{pmatrix}C \\ C(A-BK)\end{pmatrix}=\begin{pmatrix}0 & 1 \\ -77.21 & -13.33\end{pmatrix}$$
que tem $\text{rank}(O_{\dot{\theta}})=2$ logo o sistema é completamente observável a partir de $\dot{\theta}$
