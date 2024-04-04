## Resolução das equações 
- Temos a equação de Poisson 2D: $$\frac{\partial ^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}=f$$
num domínio $0\le x\le1,0\le y\le 1$ e em que consideramos $\Delta x=\Delta y=h$
**Fronteira**
- Consideremos as condições de fronteira:
$$\begin{align*}
u_{0i}&= \sin(2\pi x_{i})\quad \quad \text{-- Parde do topo}\\
u_{Ni}&= \sin(2\pi x_{i})\quad \quad \text{-- Parde de baixo}\\
u_{j0}&= 2\sin(2\pi y_{i})\quad \quad \text{-- Parde da esquerda}\\
u_{jN}&= 2\sin(2\pi y_{i})\quad \quad \text{-- Parde da direita}\\
\end{align*}$$

**Resolução**
- Vimos na aula anterior que
$$u_{i-1,j}+u_{i,j-1}u_{i,j+1}+u_{i+1,j}-4u_{i,j}=-h^{2}f_{i,j}$$
que equivale a
$$\nabla^{2}u_{i,j}=h^{2}f_{i,j}$$

**Forma matricial**
- Podemos resolver uma EDDP da forma matricial:
$$Au=bu$$
em que temos 4 matrizes $(N_{x}-1)\times (N_{y}-1)$
- Para o caso especial esta fica na forma:
$$A=\begin{pmatrix}T & I & 0 & 0 & \dots & \dots & \dots \\ I & T & I & 0 & 0 & \dots & \dots \\  \dots &\dots & \dots & \dots & \dots & \dots &\dots \\ \dots & \dots & \dots & 0 & I & T & I \\ \dots & \dots & \dots & \dots & 0 & I & T \end{pmatrix}$$
que geralmente fica (para Poisson 2D)
$$A=\begin{pmatrix}-4 & 1 & 0 & 0 & \dots & \dots & \dots \\ 1 & -4 & 1 & 0 & 0 & \dots & \dots \\  \dots &\dots & \dots & \dots & \dots & \dots &\dots \\ \dots & \dots & \dots & 0 & 1 & -4 & 1 \\ \dots & \dots & \dots & \dots & 0 & 1 & -4 \end{pmatrix}$$
e temos
![[matriz coeficientes poisson.png]]

## Consistência
- Conseguimos acima resolver a EDDP. Mas como sabemos se estamos próximos da realidade?
- Podemos definir o parâmetro *consistência*:
$$\tau_{h\to0}(x,y)=\lim\limits_{h\to0}(\nabla^{2}-\nabla^{2}_{h})u(x,y)=0$$
