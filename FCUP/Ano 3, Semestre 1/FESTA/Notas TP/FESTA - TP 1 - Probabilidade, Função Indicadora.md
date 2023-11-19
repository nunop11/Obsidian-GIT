# EXS de Probabilidade
- Em exercícios de probabilidade, usamos uma função indicadora $\chi(x)$. A probabilidade de um acontecimento $A$ será $$P=\sum\limits_{\{R\}} P_{R}\cdot \chi_{A}(R) \quad \quad \quad \quad;\quad \quad \chi_{A}(R)=\begin{cases}0&;&R\not\subset A\\1&;&R\subset A\end{cases}$$
em que $\{R\}$ são partições do espaço de acontecimentos. 
- Assim, na prática, a função indicadora serve para anular o sumatório nos termos que não pertencem à região do espaço $A$. Ou seja, terá valor $1$ apenas nos pontos que cumprem o acontecimento que $A$.

![[ex1.4.png]]
![[1.4 partiçoes.png|400]]

- Consideremos que se divide o quadrado em $M$ partes de cada lado. Assim, a probabilidade de acertar em cada uma destas divisões é $1/M^{2}$
- Assim, podemos considerar que todas as divisões são iguais com dimensões: $$\Delta x=\frac{\ell}{M} \quad \quad;\quad \quad \Delta y= \frac{\ell}{M}$$
- Podemos então definir a probabilidade de acertar no círculo como sendo:
$$P_{\circ}=\sum\limits_{(m,n)} \chi_{\circ}(n,m)\cdot \frac{1}{M^{2}}$$
usando as relações acima temos que $\frac{1}{M}=\frac{\Delta x}{\ell}=\frac{\Delta y}{\ell}$ e podemos substituir:
$$P_{\circ}=\sum\limits_{(m,n)} \chi_{\circ}(n,m)\cdot \frac{\Delta x}{\ell}\frac{\Delta y}{\ell}$$
então se considerarmos que as divisões do quadrado são muiiiiiiiiito pequenas, ou seja $\Delta x\to0, \Delta y\to0$ podemos fazer:
$$P_{\circ}=\int_{\frac{-\ell}{2}}^{\frac{\ell}{2}} dx \int_{\frac{-\ell}{2}}^{\frac{\ell}{2}} dy \frac{1}{\ell^{2}} \chi_{\circ}(x,y) $$

- A função indicadora terá então a forma:
![[função indicadora 1.4.png|400]]
pelo que para isto podemos usar a função de Heaviside (função degrau):
$$\chi_{\circ}(x,y)=\Theta \left(\frac{\ell^{2}}{4}-x^{2}-y^{2}\right)$$
e ficamos com a probabilidade:
$$P_{\circ}=\frac{1}{\ell^{2}}\int_{\frac{-\ell}{2}}^{\frac{\ell}{2}} dx\int_{\frac{-\ell}{2}}^{\frac{\ell}{2}} dy \Theta \left(\frac{\ell^{2}}{4}-x^{2}-y^{2}\right)$$
- Agora, podemos fazer as substituições:
$$x\to \sqrt{\frac{\ell^{2}}{4}-y^{2}} \quad \quad;\quad \quad y\to \ell\sin\theta$$
ou converter o problema em coordenadas polares:
$$x^{2}+y^{2}\to r$$ e temos:
$$\begin{align*}
P_{\circ} &=  \frac{1}{\ell^{2}}\int_{0}^{2\pi}d \theta\int_{0}^{+\infty}r~dr~\Theta \left(\frac{\ell^{2}}{4}-r^{2}\right)\\
&= \frac{2\pi}{\ell^{2}}\int_{0}^{+\infty}\Theta \left(\frac{\ell^{2}}{4}-r^{2}\right)\\
&= \frac{2\pi}{\ell^{2}} \int_{0}^{\frac{\ell}{2}}r~dr =\frac{2\pi}{\ell^{2}}\cdot \frac{\ell^{2}}{8}= \frac{\pi}{4}
\end{align*}$$

![[ex1.5.png]]

- Consideremos que o intervalo de graus de lançamento $[0,\pi/2]$ está dividido em $M$ partes. Temos que cada uma dessas partes tem uma amplitude $\Delta \theta=\frac{\pi}{2M}$. Assim, consideremos $\theta_{m}=m \Delta \theta$ como sendo um ângulo de lançamento que corresponde a $m$ divisões.
- Podemos escrever que $M=\frac{\pi}{2\Delta\theta}$. Assim, a probabilidade de de escolher 1 ângulo destes é:
$$P_{\theta_{m}}=\frac{1}{M}=\frac{2\Delta\theta}{\pi}$$
(1 ângulo em $M$, todos com a mesma probabilidade)

- A partir daqui, consideremos $P_{C},\chi_{C}$ como sendo a probabilidade e função indicadora correspondentes ao evento "Acertar no crocodilo". Temos:
$$P_{C}=\sum\limits_{\theta_{m}}P_{\theta_{m}}\chi_{C}(\theta)=\sum\limits_{\theta_{m}} \frac{2\Delta\theta}{\pi} \chi_{C}(\theta) \longrightarrow \frac{2}{\pi}\int_{0}^{\frac{\pi}{2}} d \theta \chi_{C}(\theta)$$

- Ora, de mecânica temos que $$\begin{cases}
x(t)=v_{0x}t \\
y(t)= v_{0y}t- \frac{1}{2}gt^{2}
\end{cases} \longrightarrow \begin{cases}
x(t)=v_{0}\cos\theta t\\ y(t)=v_{0}\sin\theta t-\frac{1}{2}gt^{2}
\end{cases}$$ $$$$em que o tempo de voo é dado por $t_{voo}\rightarrow y(t_{voo})=0 \longrightarrow t_{voo}=\frac{2v_{0}\sin\theta}{g}$
- Assim, como o alcance $x_{max}$ corresponde a $x(t_{voo})$ temos:
$$x_{max}=x(t_{voo})=\frac{2}{g} v_{0}^{2} \sin\theta\cos\theta=500\sin\theta\cos\theta=250\sin2\theta$$
- Ora, para que acertemos no crocodilo é preciso que $100\le x_{max}\le 107$. Assim a função indicadora terá o seguinte traçado:
![[função indicadora.png|500]]
- Ou seja, podemos escrever a função como a subtração de 2 funções Heaviside:
$$\chi_{C}(\theta)=\Theta(250\sin2\theta-100)- \Theta(250\sin2\theta-107)$$
e ficamos com:
$$\begin{align*}
P_{C}=\frac{2}{\pi}\int_{0}^{\frac{\pi}{2}} d \theta \chi_{C}(\theta)&= \frac{2}{\pi}\int_{0}^{\frac{\pi}{2}} d \theta [\Theta(250\sin2\theta-100)- \Theta(250\sin2\theta-107)] \\
&= \frac{2}{\pi}\cdot 2\int_{0}^{\frac{\pi}{4}} d \theta [\Theta(250\sin2\theta-100)- \Theta(250\sin2\theta-107)] \\
&= \frac{4}{\pi}(\theta_{107}-\theta_{100})
\end{align*}$$
- Aqui usamos que:
$$\int_{0}^{\frac{\pi}{2}}d\theta ~g(\sin\theta)=2\int_{0}^{\frac{\pi}{4}}d\theta ~g(\sin\theta)$$
sendo que no EX acima podemos fazer esta divisão porque para $\theta=\frac{\pi}{4}$ teremos o alcance máximo.