- Pode ser representado como 
$$\partial_{t}\vec{q} =  D \nabla^{2}\vec{q} + \vec{R}(\vec{q})$$
- Em 2D podemos escrever isto como
$$\begin{pmatrix}\partial_{t}u_{x} \\ \partial_{t}u_{y}\end{pmatrix}=\begin{pmatrix}D_{x} & 0 \\ 0 & D_{y}\end{pmatrix} \begin{pmatrix}\partial_{xx}u_{x} \\ \partial_{xx}u_{y}\end{pmatrix} + \begin{pmatrix}R_{x}(\vec{u}) \\ R_{y}(\vec{u})\end{pmatrix}$$


- Consideremos $\vec{q}=u(x,y)=u_{ij}$ e $R(u)= R_{ij}$. Temos:
$$\begin{align*}
\partial_{t}u_{ij}&= D \nabla^{2}u_{ij} + R_{ij}\\
\frac{u_{ij}^{n+1}-u_{ij}}{\Delta t}&= D (\partial_{x}^{2}u_{ij}+\partial_{y}^{2}u_{ij}) + R_{ij}\\
u_{ij}^{n+1}&= u_{ij}+\Delta T \left[D(\partial_{x}^{2}u_{ij} + \partial_{y}^{2}u_{ij}) + R_{ij} \right]
\end{align*}$$


## Gray Scott
- Temos
$$\partial_{t}\begin{pmatrix}u \\ v\end{pmatrix} = \nabla^{2}\begin{pmatrix}u \\ v\end{pmatrix} + \begin{pmatrix}-uv^2+f(1-u) \\ uv^{2}-(f+k)v\end{pmatrix}$$
ou seja:
$$R(u,v)=\begin{pmatrix}-uv^{2}+f(1-u) \\ uv^{2}-(f+k)v\end{pmatrix}$$

- Em sistema:
$$\begin{cases}
\partial_{t}A = D_{A}\nabla^{2}A - AB^{2}+f(1-A) \\
\partial_{t}B = D_{B}\nabla^{2}B + AB^{2} - (f+k)B
\end{cases}$$