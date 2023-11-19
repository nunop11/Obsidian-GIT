# Poço Infinito não constante
- Sendo $V(x)=ax/L$ ficamos com $$\tiny\begin{align*}
H_{mn}&= \frac{2}{L}\int_{0}^{L} \sin \frac{\pi mx}{L} \left[ \frac{-\hbar^{2}}{2M} \frac{d^{2}}{dx^{2}} + \frac{ax}{L} \right]\sin \frac{\pi nx}{L} dx\\
&= \frac{2}{L} \left[ \frac{-\hbar^{2}}{2M} \int_{0}^{L}  \sin \frac{\pi mx}{L} \frac{d^{2}}{dx^{2}} \sin \frac{\pi nx}{L} dx + \frac{a}{L} \int_{0}^{L} x \sin \frac{\pi mx}{L}\sin \frac{\pi nx}{L} dx \right]\\
&= \frac{\hbar^{2}n^{2}\pi^{2}}{ML^{3}} \left[\int_{0}^{L} \sin \frac{\pi mx}{L}\sin \frac{\pi nx}{L} dx \right] + \frac{2a^{2}}{L^{2}}\begin{cases}0&;&m\ne n,ambos~(im)pares\\- (\tfrac{2L}{\pi})^{2} \frac{mn}{(m^{2}-n^{2})^{2}} &;&m\neq n, 1par,1impar\\ \frac{L^{2}}{4} &;&m=n\\\end{cases} \\\\
&= \frac{\hbar^{2}n^{2}\pi^{2}}{ML^{3}} \begin{cases}
\frac{L}{2}&;&m=n\\0&;&m\neq n\end{cases} + \frac{2a^{2}}{L^{2}}\begin{cases}0&;&m\ne n,ambos~(im)pares\\- (\tfrac{2L}{\pi})^{2} \frac{mn}{(m^{2}-n^{2})^{2}} &;&m\neq n, 1par,1impar\\ \frac{L^{2}}{4} &;&m=n\\\end{cases} \\
\end{align*}$$
E ficamos com a expressão geral:
$$H_{mn}=\begin{cases}
\frac{\hbar^{2}n^{2}\pi^{2}}{2ML^{2}} + \frac{a^{2}}{2} &;& m=n \\
0 &;& m\ne n \textsf{ e ambos pares ou ímpares} \\
-\frac{8a^{2}}{\pi^{2}} \frac{mn}{(m^{2}+n^{2})^{2}} &;& m\ne n \textsf{ 1 par e outro impar}
\end{cases}$$

---
---
---

# Glicólise
Temos
$$\begin{cases}-x + ay +x^{2}y=0 \\ b-ay -x^{2}y=0\end{cases} \to \begin{cases} --- \\ y = \frac{b}{x^{2}+a} \end{cases}\to \begin{cases} -x + \frac{b(x^{2}+a)}{x^{2}+a}=0\to x=b \\ --- \end{cases} $$


---
$$x = y(a+x^{2})\quad \quad;\quad \quad y = \frac{b}{a+x^{2}}$$
temos 
$$a+x^{2}=\frac{x}{y} \to x = \sqrt{\frac{x}{y}-a}$$
$$y = \frac{b}{\frac{x}{y}}\to y = \frac{by}{x}\to x = b$$
---
Vejamos como é que este sistema pode ser resolvido:
$$\begin{align*}
\begin{cases}-x + ay +x^{2}y=0 \\ b-ay -x^{2}y=0\end{cases}\\
\downarrow\\
yx^{2}-x + ay &= 0\\
\end{align*}$$

---
---
# 13 - Constante Wien
- Temos:
$$I(\lambda)=\frac{ 2\pi hc^{2} \lambda^{-5} }{ e^{\frac{hc}{\lambda k_{B}T}}-1}=\frac{ 2\pi hc^{2} }{ \lambda^{5}e^{\frac{hc}{\lambda k_{B}T}}-\lambda^{5}}$$
Ora, máximo da intensidade radiada, ou seja, o máximo da função $I(\lambda)$ ocorrerá quando o seu denominador atingir um mínimo. Sendo $D(\lambda)$ a função do denominador temos:
$$\begin{align*}
D'(\lambda)&= 0\\
5\lambda^{4}e^{\frac{hc}{\lambda k_{B}T}} - \lambda^{5}\cdot\frac{hc}{\lambda^{2} k_{B}T}e^{\frac{hc}{\lambda k_{B}T}} - 5\lambda^{4}&= 0\\
5e^{\frac{hc}{\lambda k_{B}T}}-\frac{hc}{\lambda k_{B}T}e^{\frac{hc}{\lambda k_{B}T}}-5&= 0\\
(\textsf{dividir por }e^{\frac{hc}{\lambda k_{B}T}})\\
5 - \frac{hc}{\lambda k_{B}T} - 5e^{\frac{-hc}{\lambda k_{B}T}}&= 0\\
5e^{\frac{-hc}{\lambda k_{B}T}} + \frac{hc}{\lambda k_{B}T} -5&= 0
\end{align*}$$
- Ora, se substituirmos $x=\frac{hc}{\lambda k_{B}T}$ ficamos com $$\begin{align*}
5e^{-x}+x-5&= 0\\
x &= 5 - e^{-x}
\end{align*}$$
não sei calcular a solução disto analiticamente.

- Um zero desta equação será $x_{z}=\frac{hc}{\lambda_{max}k_{B}T}$. Assim:
$$\lambda_{max}=\frac{hc}{k_{B}T x_{z}}=\frac{b}{T} = \frac{\frac{hc}{k_{B}x_{z}}}{T}$$
logo a constante de Wien é dada por $$b = \frac{hc}{k_{B}x_{z}}$$

---
---
# 16 - POnto Lagrange
- A força que a terra aplica no satélite é $F_{T}=\frac{GMm_{s}}{r^{2}}$. A força que a lua aplica é $F_{L}=\frac{Gmm_{s}}{(R-r)^{2}}$. 
- Por outro lado, a velocidade que a Terra aplica na lua é $F_{TL}=\frac{GMm}{R^{2}}$
- Tanto a lua como o satelite se deslocam com velocidade angular $\omega$. Ou seja:

$$\begin{cases}
F_{T}-F_{L}=m_{s}r\omega^{2} \\
F_{TL}=m R\omega^{2}
\end{cases}=\begin{cases}
\frac{GMm_{s}}{r^{2}}-\frac{Gmm_{s}}{(R-r)^{2}}=m_{s}r \omega^{2} \\
\frac{GMm}{R^{2}}=mR \omega^{2} 
\end{cases}$$
Vemos logo que as massas cortam:
$$\begin{cases}
\frac{GM}{r^{2}}-\frac{Gm}{(R-r)^{2}}=r \omega^{2} \\
\frac{GM}{R^{2}}=R \omega^{2} 
\end{cases}$$
- Ora, verificamos que a equação 1 é aquela que pretendemos demonstrar.
---
Da alínea anterior temos:
$$\frac{GM}{r^{2}}-\frac{Gm}{(R-r)^{2}}=r \omega^{2}$$
Ao multiplicar tudo por $r^{2}(R-r)^{2}$ ficamos com:
$$GM(R-r)^{2}-G mr^{2}=\omega^{2} r^{3}(R-r)^{2} $$


$$F = q*\vec{v}\times \vec{B}$$

---
---
# 17 - Circuito com díodo
- Para o nodo $V_{2}$ temos: 
  $$\frac{V_{2}-V_{+}}{R_{3}} + \frac{V_{2}}{R_{4}}=0$$
--- 
Temos o sistema:
$$\begin{cases}
\frac{V_{1}-V_{+}}{R_{1}} + \frac{V_{1}}{R_{2}} + I_{0}(e^{(V_{1}-V_{2})/V_{T}}-1)=0 \\
\frac{V_{2}-V_{+}}{R_{3}}+ \frac{V_{2}}{R_{4}}+I_{0}(e^{(V_{2}-V_{1})/V_{T}}-1)=0
\end{cases}$$
Ora, podemos reorganizá-lo, tal que:
$$\begin{cases} 
V_{1}= \left(\frac{R_{1}R_{2}}{R_{1}+R_{2}}\right) \left[\frac{V_{+}}{R_{1}}- I_{0}(e^{(V_{1}-V_{2})/V_{T}}-1)\right] \\  
V_{2}= \left(\frac{R_{3}R_{4}}{R_{3}+R_{4}}\right) \left[\frac{V_{+}}{R_{3}}- I_{0}(e^{(V_{2}-V_{1})/V_{T}}-1)\right] \\
\end{cases}$$

---
---
# 6 - HMS 
- A equação $\frac{d^{2}x}{dt^{2}}=-\omega^{2}x$ pode ser representada como um sistema de equações diferenciais simultâneas, tais que:
$$\begin{cases}
\frac{dx}{dt} = y \\
\frac{dy}{dt}=-\omega^{2}x
\end{cases}$$
---
Temos $$\frac{d^{2}x}{dt^{2}}-\mu(1-x^{2}) \frac{dx}{dt} + \omega^{2}x=0$$
- Fazendo novamente $y=\frac{dx}{dt}$ ficamos com:
$$\begin{cases}
\frac{dx}{dt}=y \\ \\
\frac{dy}{dt}= \mu(1-x^{2})y - \omega^{2}x
\end{cases}$$

---
---
# 1 - Poisson
- Temos:
$$\begin{align*}
\frac{\partial^{2}\phi}{\partial x^{2}}&= \frac{\phi(x+a,y) + \phi(x-a,y)-2\phi(x,y)}{a^{2}}\\
\frac{\partial^{2}\phi}{\partial y^{2}}&= \frac{\phi(x,y+a) + \phi(x,y-a)-2\phi(x,y)}{a^{2}}
\end{align*}$$
- Ou seja, a equação de Poisson ($\nabla^{2}\phi = \rho$) é dada por:
$$\begin{align*}
\phi(x+a,y) + \phi(x-a,y) + \phi(x,y+a) + \phi(x,y-a) - 4\phi(x,y) = a^{2}\rho(x,y)\\
\phi(x,y) = \frac{1}{4}\left[ \phi(x+a,y) + \phi(x-a,y) + \phi(x,y+a) + \phi(x,y-a) - a^{2}\rho(x,y) \right] 
\end{align*}$$
- Logo, a nossa tentiva seguinte para um certo ponto será:
$$\phi'(x,y) = \frac{1}{4}\left[ \phi(x+a,y) + \phi(x-a,y) + \phi(x,y+a) + \phi(x,y-a) - a^{2}\rho(x,y) \right] $$

- Ora, no método de Gauss Seidel temos: $\phi_{\omega}(x,y)=(1+\omega)\phi'(x,y)-\omega \phi(x,y)$, pelo que:
$$\begin{align*}
\phi_{\omega}(x,y)\leftarrow \frac{\omega+1}{4} \left[ \phi(x+a,y) + \phi(x-a,y) + \phi(x,y+a) + \phi(x,y-a) - a^{2}\rho(x,y) \right] - \omega \phi(x,y)
\end{align*}$$

---
---

# 4 - Temperatura Terra
- A equação do calor é: $$T_{0}(t)=D \frac{\partial^{2}T}{\partial x^{2}}$$

em que $D$ é uma constante conhecida e $T$ a temperatura, que varia com a profundidade $x$.

- A partir das formulas da segunda derivada:

$$\begin{align*}

T(x+a) + T(x-a) -2T(x) = \frac{a^{2}T_{0}}{D}\\

T(x) = \tfrac{1}{2}[T(x+a) + T(x-a) - \tfrac{a^{2}T_{0}}{D}]

\end{align*}$$

- Pelo que o método de Gauss-Seidel:

$$\begin{align*}

T_{\omega}(x)\leftarrow \frac{\omega+1}{4} \left[ T(x+a) + T(x-a) - \tfrac{a^{2}T_{0}}{D}\right] - \omega T(t)
\end{align*}$$

---
---
# 4 - Difusao termica V2
- A equação do calor é: $$\frac{\partial T}{\partial t}=D \frac{\partial^{2}T}{\partial x^{2}}$$

em que $D$ é uma constante conhecida e $T$ a temperatura, que varia com a profundidade $x$.

- A partir das formulas da segunda derivada:

$$\begin{align*}
\frac{T(x,t+a) - T(x,t)}{a} = D \frac{T(x+a,t) + T(x-a,t) - 2T(x,t) }{a^{2}}\\
T(x,t) = \tfrac{D}{a}[T(x+a,t) + T(x-a,t)] - \tfrac{2D}{a}T(x,t)-T(x,t+a)\\
T(x,t) (1- \tfrac{2D}{a}) = \tfrac{D}{a}[T(x+a,t) + T(x-a,t) - \tfrac{a}{D}T(x,t+a)]\\
T(x,t)= \frac{\frac{D}{a}}{\frac{a-2D}{a}}[T(x+a,t) + T(x-a,t) - \tfrac{a}{D}T(x,t+a)]\\
T(x,t)= \tfrac{D}{a-2D}[T(x+a,t) + T(x-a,t) - \tfrac{a}{D}T(x,t+a)]\\
\end{align*}$$

- Pelo que o método de Gauss-Seidel:
$$\begin{align*}

T_{\omega}(x,t)\leftarrow \tfrac{\omega+1}{4} \tfrac{D}{a-2D} \left[ T(x+a,t) + T(x-a,t) - \tfrac{a}{D}T(x,t+a)\right] - \omega T(x,t)
\end{align*}$$
---
---
# 5 - Corda de Piano
- A equação de onda é:
$$\frac{\partial^{2}\phi}{\partial t^{2}}= v^{2} \frac{\partial^{2}\phi}{\partial x^{2}}$$
com $v=100$
- Usando a definição de 2ª derivada temos:
$$\frac{\partial^{2}\phi}{\partial t^{2}}= \frac{v^{2}}{a^{2}}\left[ \phi(x+a,t)+\phi(x-a,t)-2 \phi(x,t) \right]$$
- E podemos então definir as equações simultâneas:
$$\begin{cases}
\frac{d\phi}{dt}=\psi(x,t) \\
\frac{d\psi}{dt} = \frac{v^{2}}{a^{2}}\left[ \phi(x+a,t)+\phi(x-a,t)-2 \phi(x,t) \right]
\end{cases}$$
- Apliquemos o método de Euler:
$$\begin{cases}
\phi(x,t+h) = \phi(s,t)+h \psi(x,t) \\
\psi(x, t+h)=\psi(x,t) + h \frac{v^{2}}{a^{2}}[\phi(x+a,t)+\phi(x-a,t)-2 \phi(x,t)]
\end{cases}$$