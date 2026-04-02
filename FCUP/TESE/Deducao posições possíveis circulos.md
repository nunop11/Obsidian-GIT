- O robot tem a previsão de pose atual $(x,y)$ e deteta 2 paredes:
    - Parede 1 associada a uma parede de referência com centro em $(a,b)$, a  uma distância $D$ do robot
    - Parede 2 associada a uma parede de referência com centro em $(c,d)$, a uma distância $E$ do robot

- Ora, o robot tem de estar numa das 2 posições dadas pela interseção dos seguintes circulos:
$$\begin{cases}
(x-a)^{2}+(y-b)^{2}=D^{2} \\
(x-c)^{2}+(y-d)^{2}=E^{2}
\end{cases}$$
logo podemos subtrair as 2 equações:
$$\begin{align*}
(x-a)^{2}-(x-c)^{2}+(y-b)^{2}-(y-d)^{2}&= D^{2}-E^{2}\\
x^{2}-2ax+a^{2}-x^{2}+2cx-c^{2}+y^{2}-2by+b^{2}-y^{2}+2dy-d^{2}&= D^{2}-E^{2}\\
x(2c-2a)+y(2d-2b)&= D^{2}-E^{2} - a^{2}-b^{2}+c^{2}+d^{2}\\
x(2c-2a)+y(2d-2b)&= D^{2}-E^{2} - a^{2}-b^{2}+c^{2}+d^{2}\\
y= \frac{D^{2}-E^{2} - a^{2}-b^{2}+c^{2}+d^{2}}{2d-2b}-\frac{2c-2a}{2d-2b}x\\
\end{align*}$$
ou seja:
$$y=A-Bx \quad \quad;\quad \begin{cases}
A=\frac{D^{2}-E^{2} - a^{2}-b^{2}+c^{2}+d^{2}}{2d-2b} \\
B=\frac{2c-2a}{2d-2b}
\end{cases}$$

- Podemos substituir isto na equação do circulo 1:
$$\begin{align*}
(x-a)^{2}+(y-b)^{2}&= D^{2}\\
x^{2}-2ax+a^{2}+y^{2}-2by+b^{2}&= D^{2}\\
x^{2}-2ax+(A-Bx)^{2}-2b(A-Bx)&= D^{2}-a^{2}-b^{2}\\
x^{2}-2ax+A^{2}-2ABx+B^{2}x^{2}-2bA+2bBx&= D^{2}-a^{2}-b^{2}\\
x^{2}(1+B^{2})+x(2bB-2a-2AB)+(A^{2}-2bA+a^{2}+b^{2}-D^{2})&= 0
\end{align*}$$
e temos a formula resolvente:
$$\begin{align*}
Fx^{2}+Gx+H&= 0\\
x&= \frac{-G\pm \sqrt{G^{2}-4FH}}{2F}\\
&= \frac{2a+2AB-2bB\pm \sqrt{(2a+2AB-2bB)^{2} + 4 (1+B^{2})(D^{2}+2bA-A^{2}-a^{2}-b^{2})}}{2(1+B^{2})}
\end{align*}$$

- Depois, naturalmente, temos:
$$\begin{align*}
y&= A-Bx\\
&= A - Bx_{\pm}
\end{align*}$$