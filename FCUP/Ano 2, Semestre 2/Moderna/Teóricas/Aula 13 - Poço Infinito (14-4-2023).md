- Comecemos por ver algumas variantes da equação de Schrödinger:
### Eq Schrödinger para V constante no tempo
$$i\hbar \frac{\partial}{\partial t}\Psi(\vec{r}, t) = \left[- \frac{\hbar^{2}}{2m} \nabla^{2} + V(\vec{r}, t) \right]\Psi$$
logo, se tivermos $V(\vec{r}, t)=V(\vec{r})$ então:
$$\Psi(\vec{r}, t)=\Psi(\vec{r}) T(t)=\Psi(\vec{r}) e^{\frac{-E}{\hbar} t}$$(A dedução de $T(t)$ foi feita na aula anterior)

### Eq Schrödinger independente de tempo
- Temos $$\left[- \frac{\hbar^{2}}{2m}\nabla^{2}+V(\vec{r})\right]\Psi(\vec{r})=E \Psi(\vec{r}) \longrightarrow H\Psi=E\Psi$$
(a escrita da direita é a forma como escrevemos a equação como produto de matrizes)

## Propriedades de $\Psi(\vec{r})$
- Recordando a interpretação de Born temos: $|\Psi(\vec{r}, t)|^{2}=\Psi^{*}(\vec{r}, t)\Psi(\vec{r}, t)=P(\vec{r}, t)$
- Temos que $\Psi$ tem as propriedades:
    - Finita e normalizável, pelo que $\int |\Psi(\vec{r},t)|^{2} d\vec{r}=1$
    - Contínua
    - Unívoca: uma partícula não pode estar em 2 pontos ao mesmo tempo

# 1 - Quantização de Energia
- Queremos mostrar que *nunca temos uma solução normalizável* se $E<V_{min}$. 
### Física clássica
- Temos que a energia de um eletrão é dado por $E=E_{c}+V(x)$, em que $E\geq0$ e $V>0, V=0 \textsf{  ou  } V<0$
- Assim, o valor mínimo de $E$ é $E_{min}=0$
- Ora, nesta física não podemos ter energias negativas, mas podemos ter energia nula

### Física  Quântica
- Da equação de Schrödinger independente do tempo temos $$\frac{-\hbar^{2}}{2m} \Psi''=(E-V)\Psi \rightarrow \Psi''=\frac{2m}{\hbar^{2}} (V-E)\Psi$$(em que $\Psi''=\frac{d^{2}}{dx^{2}}\Psi(x)$)
- Se $E<V_{min}$ então $V-E>0$, logo $\Psi''$ tem o mesmo sinal de $\Psi$
- Vê-se ainda que na física quântica $E>0$

# 2 - Poço Infinito
![[Attachments/FCUP/A2S2/Moderna/poço infinito.png]]
- Temos então:
$$V(x)=\begin{cases}0 &; &0\leq x\leq L  \\ \infty &; &x<0 ~~;~~x>L\end{cases}$$
de notar que podíamos fazer este estudo para $U$ a ser igual a qualquer constante para $0\leq x\leq L$.
- Ao falar disto, $0\leq x\leq L$ significa que estamos "dentro do poço".

- Como $U$ é diferente de forma descontínua em regiões diferente, temos que encontrar uma solução da equação de Schrodinger para cada região. 
- Partimos da equação: $$- \frac{\hbar^{2}}{2m} \frac{d^{2}\Psi}{dx^{2}} +V(x)\Psi(x)=E\Psi(x)$$
### Fora do poço
- Vemos que para não ter $U\to \infty$, temos que ter $\Psi=0$ para que $U\Psi\neq \infty$. Interpretando isto de forma probabilística, considerando que as paredes do poço são rígidas, pelo que as partículas nunca conseguem passar para o lado de fora. Ou seja, há probabilidade nula de encontrar partículas fora do poço, logo $$\Psi(x)=0 \quad \quad;\quad \quad x<0~~;~~x>L$$

### Dentro do poço
- Temos $V(x)=0$, logo $$- \frac{\hbar^{2}}{2m} \frac{d^{2}\Psi}{dx^{2}}=E \Psi(x)$$
- Ao resolver a equação diferencial temos:
$$\begin{align*}
\Psi&= C_{1}e^{ikx} + C_{2}e^{-ikx} \quad \quad; \quad k=\sqrt{\frac{2mE}{\hbar^{2}}}\\
&= A\sin(kx) + B\cos(kx)
\end{align*}$$
- Apliquemos as condições de fronteira. Temos:
$$\Psi(0)=A \cdot0 + B \cdot 1=0 \longrightarrow B=0$$
$$\Psi(L)=A \cdot \sin(kL)+0\cdot\cos(kL)=0$$
logo $$\begin{align*}
\sin(kL)=0\\
kL=n\pi\\
\frac{2\pi}{\lambda}L=n\pi\\
\lambda=\frac{2L}{n}
\end{align*}$$
- Ou seja, a solução da equação de Schrödinger para o poço infinito é _um conjunto de modos normais de uma onda de extremos fixos_.
- Ora, como apenas alguns valores de $k$ podem ocorrer, então apenas alguns valores de $E$ podem ocorrer. Assim, temos $$k=\sqrt{\frac{2mE}{\hbar^{2}}} \longrightarrow E= \frac{k^{2}\hbar^{2}}{2m}= \frac{\hbar^{2}\pi^{2}n^{2}}{2mL^{2}}=\frac{h^{2}n^{2}}{8mL^{2}}$$
- Assim temos $$\begin{align*}
E_{1}&= \frac{h^{2}}{8mL^{2}}\\
E_{2}&= \frac{h^{2}2^{2}}{8mL^{2}}=2^{2}E_{1}=4E_{1}\\
E_{3}&= \frac{h^{2}3^{2}}{8mL^{2}}=3^{2}E_{1}=9E_{1}\\
E_{4}&= \frac{h^{2}4^{2}}{8mL^{2}}=4^{2}E_{1}=16E_{1}\\
&\dots\\
E_{n}&= n^{2}E_{1}
\end{align*}$$

- Mas voltemos à resolução da equação de Schrödinger, em que precisamos de determinar $A$. Aplicando a indição de normalização:
$$\begin{align*}
\int_{-\infty}^{+\infty} |\Psi(x)|^{2}dx&= \cancelto0{\int_{-\infty}^{0}|\Psi(x)|^{2}dx} + \int_{0}^{L}|\Psi(x)|^{2}dx + \cancelto0{\int_{L}^{+\infty}|\Psi(x)|^{2}dx}=1\\
&= \int_{0}^{L} A^{2}\sin^{2} \frac{n\pi x}{L} dx=1\\
&= |A|^{2} \frac{L}{\pi n}\int\sin^{2}(u)du ~~~~;~~~~ u=\left(\frac{\pi nx}{L} \right)~~,~~dx=\frac{L}{\pi n}du\\
\end{align*}$$
ora, temos $$\begin{align*}
\cos2x &= \cos^{2}x-\sin^{2}x\\
&= 1-2\sin^{2}x\\
\sin^{2}x &= \frac{1}{2}(1-\cos2x)
\end{align*}$$
Logo:
$$\begin{align*}
\int_{-\infty}^{+\infty}|\Psi(x)|^{2}dx&=  |A|^{2} \frac{L}{\pi n} \left( \int \frac{1}{2}du - \int \cos2u ~du\right)=1\\
&= |A|^{2} \frac{L}{\pi n} \left[ \frac{u}{2} - \sin2u\right]\\
&\textsf{(anular a substituição)}\\
&= |A|^{2}\left[\frac{x}{2} - \frac{L\sin \left(\frac{2\pi nx}{L}\right)}{4\pi n} \right]_{0}^{L}\\
&= |A|^{2}\left(\frac{L}{2}-0 - 0 + 0\right)\\\\
|A|^{2} \frac{L}{2}&= 1 \longrightarrow |A| = \sqrt{\frac{2}{L}}
\end{align*}$$

![[poço infinito ondas e probab.png]]

## 2.1 - Observações sobre poço infinito
**1.** Na versão
$$\Psi_{n}(x,t)=\sqrt{\frac{2}{a}}\sin \left(\frac{n\pi x}{L} \right)e^{-i \frac{E_{n}}{\hbar}t}~~~~;~~~~n=1,2,3\dots$$

**2.** De forma geral, temos:
$$\Psi(x,t)=\sum\limits_{n=1}^{\infty}a_{n}\Psi_{n}(x,t)$$


## 2.2 - Poço Infinito em 2D
![[poço infinito 2d.png]]
$$V(x)=\begin{cases}0 &; &0<x<L_{x} \quad,\quad 0<y<L_{y}\\ \infty &; &restante~~espaço\end{cases}$$
Pelo que a equação independente do tempo
$$\frac{-\hbar^{2}}{2m} \left[ \frac{\partial^{2}}{\partial x^{2}}+ \frac{\partial^{2}}{\partial y^{2}}\right]\Psi(x,y) + (V-E)\Psi(x,y)=0$$
Aplicamos o método de separação de variáveis:
$$\Psi(x,y)=X(x)Y(y)$$
pelo que:
$$\frac{\partial^{2}}{\partial x^{2}}\Psi(x,y)=X''Y \quad \quad; \quad \quad \frac{\partial^{2}}{\partial y^{2}}\Psi(x,y)=XY''$$
e ao substituir na equação independente do tempo:
$$\begin{align*}
\frac{-\hbar^{2}}{2m} \left[ \frac{\partial^{2}}{\partial x^{2}}+ \frac{\partial^{2}}{\partial y^{2}}\right]\Psi(x,y) + (V-E)\Psi(x,y)&= 0\\
- \frac{\hbar^{2}}{2m} \left(X''Y + XY'' \right) + (V-E)XY&= 0\\
- \frac{\hbar^{2}}{2m} \frac{X''}{X} - \frac{\hbar^{2}}{2m} \frac{Y''}{Y} + (V-E)&= 0 \quad \quad (\textsf{dividimos por }XY)
\end{align*}$$
- Podemos ver que na equação que obtivemos no fim, a primeira parcela só depende $x$ e a segunda de $y$.

- Ou seja, temos $$\begin{cases}- \frac{\hbar^{2}}{2m} \frac{X''}{X} = A \\ - \frac{\hbar^{2}}{2m} \frac{Y''}{Y} = B\end{cases} ~\Longrightarrow~A+B+(V-E)=0 $$
- Recordemos que as condições de fronteira são:
$$0<x<L_{x} \quad;\quad 0<y<L_{y} \quad;\quad V=0$$
- E temos ainda, ao dividir a equação de $A,B,V,E$ nas componentes temos:
$$\begin{cases}A+V_{x}-E_{x}=0\\ B+V_{y}-E_{y}=0 \end{cases}=\begin{cases}X(x)=C_{x}\sin(k_{x}x)+D_{x}\cos(k_{x}x)\\ Y(y)=C_{y}\sin(k_{y}y) + D_{y}\cos(k_{y}y) \end{cases}$$
- Pelo que temos $$\Psi(x,y)=X(x)Y(y)=[C_{x}\sin(k_{x}x)+D_{x}\cos(k_{x}x)][C_{y}\sin(k_{y}y) + D_{y}\cos(k_{y}y)]$$
- As condições de fronteira no poço são:
    - $\Psi(x=0~,~y)=0$ (lado esquerdo do poço) pelo que temos $\large D_{x}=0$
    - $\Psi(x~,~y=0)=0$ (lado inferior do poço) pelo que temos $\large D_{y}=0$
    - $\Psi(x=L_{x}~,~y)=0$ (lado direito do poço) pelo que temo: $$\Psi(L_{x},y)=0\leftrightarrow C_{x}C_{y}\sin(k_{x}L_{x})\sin(k_{y}y)=0 \longrightarrow k_{x}=\frac{n_{x}\pi}{L_{x}}$$
    - $\Psi(x, y=L_{y})=0$ (lado superior do poço) pelo que temos: $\large k_{y}=\frac{n_{y}\pi}{L_{y}}$

- Assim, sendo $L_{x}=L_{y}=L$ e $C_{x}C_{y}=C$:
$$\Psi(x,y)=C \sin \left( \frac{n_{x}\pi}{L}x\right)\sin \left( \frac{n_{y}\pi}{L}y\right)$$
- Apliquemos a condição de normalização:
$$\iint \Psi^{2}dxdy=1 \Longrightarrow \int\limits_{0}^{L}\int\limits_{0}^{L} C^{2} \sin^{2} \left( \frac{n_{x}\pi}{L}x\right)\sin^{2} \left( \frac{n_{y}\pi}{L}y\right)~dxdy=1$$
de onde se tem $\LARGE C = \frac{2}{L}$, sendo que $C_{x}=C_{y}=\sqrt{\frac{2}{L}}$


- Retomemos a equação de Schrödinger independente do tempo:
$$\frac{-\hbar^{2}}{2m} \left[ \frac{\partial^{2}}{\partial x^{2}}+ \frac{\partial^{2}}{\partial y^{2}}\right]\Psi(x,y) + (V-E)\Psi(x,y)=0$$
Substituindo $V=0$ e $\Psi(x,y)=\frac{2}{L} \sin \left( \frac{n_{x}\pi}{L}x\right)\sin \left( \frac{n_{y}\pi}{L}y\right)$ temos:
$$\begin{align*}
E &=  \frac{\hbar^{2}\pi^{2}}{2mL^{2}}(n_{x}^{2}+n_{y}^{2})= \frac{h^{2}}{8mL^{2}}(n_{x}^{2}+n_{y}^{2})\\
E &=  E_{0}(n_{x}^{2}+n_{y}^{2})
\end{align*}$$
- Vemos que temos a mesma energia $E_{0}=E_{1}$ para o estado fundamental, que ocorre quando temos $(n_{x},n_{y})=(1,0) \vee (n_{x},n_{y})=(0,1)$. Notemos que estes $n$ se chamam __*números quânticos*__.
- Note-se ainda que ter $(n_{x},n_{y})=(A,B)$ ou $(n_{x},n_{y})=(B,A)$ irá dar-nos a mesma energia. A isto chamamos __degenerância__.
- Iremos usar a notação: $$(n_{x},n_{y})=(1,2) \Longrightarrow \Psi_{1,2}(x,y)$$
- Assim, por exemplo temos o *nível fundamental*:
$$\Psi_{1,1}(x,y)=\frac{2}{L}\sin \left(\frac{\pi x}{L} \right) \sin\left(\frac{\pi y}{L} \right) \quad \quad ;\quad \quad E_{1,1}=\hbar^{2}\pi^{2}/2mL^{2}(1^{2}+1^{2})=\frac{\hbar^{2}\pi^{2}}{mL^{2}}$$
![[poço infinito 2d ondas e probab.png]]

#moderna #fisica #schrodinger