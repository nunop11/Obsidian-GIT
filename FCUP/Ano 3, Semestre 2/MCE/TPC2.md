Consideremos a equação de Calor em 2D, sem termos de fonte:
$$\frac{\partial u}{\partial t} = \alpha\left(\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}\right)$$
Usemos o método ADI. Para isto, dividimos a derivada temporal em 2 intervalos: $[n,n+ \frac{1}{2}]dt$ e $[n + \frac{1}{2},n+1]dt$. 
Consideremos ainda que temos um domínio quadrado (tal como é o caso do forno) com $N$ pontos: teremos $\Delta x=\Delta y=\Delta r$.

**1.**
Começamos pelo intervalo $\left[n,n + \frac{1}{2}\right]dt$. Consideramos que as derivadas espaciais são feitas em tempos diferentes: $u_{xx}$ calculado em $(n+ \frac{1}{2})dt$ e $u_{yy}$ em $ndt$. Temos:
$$\begin{align*}
\frac{u_{i,j}^{n+ \frac{1}{2}}-u_{i,j}^{n}}{\Delta t/2} &= \alpha\left(\frac{u_{i-1,j}^{n+ \frac{1}{2}} -2 u_{i,j}^{n+ \frac{1}{2}}+u_{i+1,j}^{n+ \frac{1}{2}}}{\Delta r^{2}}+\frac{u_{i,j-1}^{n} -2 u_{i,j}^{n}+u_{i,j+1}^{n}}{\Delta r^{2}}\right) \\
u_{i,j}^{n+ \frac{1}{2}}-u_{i,j}^{n}&= \frac{1}{2}G \left( u_{i-1,j}^{n+ \frac{1}{2}} -2 u_{i,j}^{n+ \frac{1}{2}}+u_{i+1,j}^{n+ \frac{1}{2}} + u_{i,j-1}^{n} -2 u_{i,j}^{n}+u_{i,j+1}^{n}\right)\\
\end{align*}$$
$$- \frac{1}{2}Gu_{i-1,j}^{n+ \frac{1}{2}} + (1+G) u_{i,j}^{n+ \frac{1}{2}}- \frac{1}{2}Gu_{i+1,j}^{n+ \frac{1}{2}}= \frac{1}{2}G u_{i,j-1}^{n} +(1-G) u_{i,j}^{n}+ \frac{1}{2}Gu_{i,j+1}^{n}$$

**2.**
Consideremos agora o 2º intervalo: $[n+ \frac{1}{2},n+1]dt$. Iremos calcular $u_{xx}$ em $(n+ \frac{1}{2})dt$ e $u_{yy}$ em $(n+1)dt$:
$$\begin{align*}
\frac{u_{i,j}^{n+ 1}-u_{i,j}^{n + \frac{1}{2}}}{\Delta t/2} &= \alpha\left(\frac{u_{i-1,j}^{n+ \frac{1}{2}} -2 u_{i,j}^{n+ \frac{1}{2}}+u_{i+1,j}^{n+ \frac{1}{2}}}{\Delta r^{2}}+\frac{u_{i,j-1}^{n+1} -2 u_{i,j}^{n+1}+u_{i,j+1}^{n+1}}{\Delta r^{2}}\right) \\
u_{i,j}^{n+ 1}-u_{i,j}^{n+\frac{1}{2}}&= \frac{1}{2}G \left( u_{i-1,j}^{n+ \frac{1}{2}} -2 u_{i,j}^{n+ \frac{1}{2}}+u_{i+1,j}^{n+ \frac{1}{2}} + u_{i,j-1}^{n} -2 u_{i,j}^{n}+u_{i,j+1}^{n}\right)\\
\end{align*}$$
$$- \frac{1}{2}Gu_{i,j-1}^{n+1} + (1+G) u_{i,j}^{n+1}- \frac{1}{2}Gu_{i,j+1}^{n+1}= \frac{1}{2}G u_{i-1,j}^{n+\frac{1}{2}} +(1-G) u_{i,j}^{n+\frac{1}{2}}+ \frac{1}{2}Gu_{i+1,j}^{n+\frac{1}{2}}$$

Assim, é evidente que podemos escrever estas duas equações na forma:
$$\begin{align*}
A u_{i}^{n+ \frac{1}{2}}&= B u_{j}^{n}\\
A u_{j}^{n+ 1}&= B u_{i}^{n+ \frac{1}{2}}
\end{align*}$$
em que:
$$A=\begin{pmatrix}1+G & -\frac{1}{2}G & 0 & 0 & \cdots & 0 & 0 \\ -\frac{1}{2}G & 1+G & -\frac{1}{2}G & 0 & \cdots & 0 & 0 \\ 0 & -\frac{1}{2}G & 1+G & -\frac{1}{2}G & \cdots & 0  & 0\\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots  & \vdots\\ 0 & 0 & 0 & 0 & \dots & -\frac{1}{2}G&  1+G\end{pmatrix}$$
$$B=\begin{pmatrix}1-G & \frac{1}{2}G & 0 & 0 & \cdots & 0 & 0 \\ \frac{1}{2}G & 1-G & \frac{1}{2}G & 0 & \cdots & 0 & 0 \\ 0 & \frac{1}{2}G & 1-G & \frac{1}{2}G & \cdots & 0  & 0\\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots  & \vdots\\ 0 & 0 & 0 & 0 & \dots & \frac{1}{2}G&  1-G\end{pmatrix}$$
em que, claramente:
$$B = -A+2I$$

Algumas notas:
    - Acima definimos $G=\frac{\alpha \Delta t}{\Delta r^{2}}$. Ora, se o domínio não fosse quadrado teríamos $\Delta x\neq \Delta y$ logo teríamos $G_{x},G_{y}$. Desta forma, teríamos: $A u_{i}^{n+ \frac{1}{2}}= B u_{j}^{n}~,~C u_{j}^{n+ 1}= D u_{i}^{n+ \frac{1}{2}}$. Estas matrizes seriam quase iguais, apenas variando a presença de $G_{x}$ ou $G_{y}$.
    - Desta forma, vemos que o facto de o domínio em estudo ser quadrado torna os cálculos mais simples.
    - Na última equação apresentada, $I$ é a matriz identidade com a mesma dimensão que $A$.
    - Uma vez que as matrizes são tridiagonais, usei o módulo de matrizes esparsas do scipy.

