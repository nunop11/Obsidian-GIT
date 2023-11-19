> NOTA: Isto consiste em 2 aulas que foram dadas seguidas, no mesmo dia.
# 1 - Função de Onda - PSI
- Assim, como vimos na aula anterior, os físicos viram que ao estudar radiação umas vezes tinham que usar teoria corpuscular (Compton) e outras vezes a teoria ondulatória (Difusão de raios X).
- Assim, pela interpretação de Bohr, existe uma dualidade Onda-Partícula, sendo que não podemos ver radiação como só uma onda nem só uma partícula. Ora, era então necessária uma nova teoria, mais geral.

- Acerca de intensidade da radiação:
    - Na teoria ondulatória temos: $$I=\frac{1}{2}\varepsilon_0c|\vec{E}|^{2}$$
    - Na teoria corpuscular a radiação é compota por fotões e temos: $$I=Nhf$$sendo $N$ a densidade de fotões por unidade de área e unidade de tempo.
    - Ou seja, teríamos $\frac{1}{2}\varepsilon_{0}c|\vec{E}|^{2}=Nhf$, logo $|\vec{E}|^{2}\propto N$.

---

- Temos a função de onda (função complexa): $\large \Psi(\vec{r}, t)$
- Ora, segundo Born nós não sabemos a posição exata de uma partícula num instante $t$, pelo que usamos $\large |\Psi(\vec{r}, t)|^{2}=\Psi^{*}(\vec{r}, t)\Psi(\vec{r}, t)=|\Psi(\vec{r})|^{2}$ para saber dá-nos a densidade de probabilidade de a partícula estar na posição $\vec{r}$ no instante $t$.

- Veremos então que $\vec{E}$ e $\Psi$ são funções análogas: ambas funções no espaço e tempo, ambas satisfazem a equação de onda. 
- Basicamente, 
    - $\vec{E}$ associa uma onda a um fotão (radiação)
    - $\Psi$ associa uma onda a matéria
- Temos ainda que para ambas podemos recorrer ao _Princípio da sobreposição_: $\Psi=\Psi_{1}+\Psi_{2}$, tal como $\vec{E}=\vec{E}_{1}+\vec{E}_{2}$

## 1.1 - Em 1 Dimensão
$$\Psi(x,t)$$
- Ora, neste caso $\Large |\Psi(x,t)|^{2}dx$ dá-no a _probabilidade_ de a partícula estar no intervalo $x\in [x~~;~~x+dx]$ no instante $t$
- E temos, portanto: $\int_{-\infty}^{+\infty}|\Psi(x,t)|^{2}dx=1$ 
- Isto funciona analogamente em dimensões superiores.

## 1.2 - Equação de Schrödinger independente do tempo
- Tendo-se $\large \Psi(x)=A\sin(kx)$ temos:$$\frac{d\Psi}{dx}=kA\cos kx \quad \quad;\quad \quad \frac{d^{2}\Psi}{dx^{2}} = -k^{2}A\sin kx=-k^{2}\Psi(x)$$
- Sendo $E_{c}=\frac{p^{2}}{2m}=\frac{\left( \frac{h}{\lambda}\right)^{2}}{2m}=\frac{\hbar^{2}k^{2}}{2m}$, então temos:
$$\frac{d^{2}\Psi}{dx^{2}}=-k^{2}\Psi(x) =- \frac{2m}{\hbar^{2}}E_{c} \Psi(x)=- \frac{2m}{\hbar^{2}}(E-V)\Psi(x)$$
sendo $E, V$, as energias total e potêncial do sistema.
- Assim, temos a __*Equação de Schrödinger 1-D independente do tempo*__:
$$\boxed{- \frac{\hbar^{2}}{2m} \frac{d^{2}\Psi}{dx^{2}} + V \Psi=E \Psi} \tag{Eq. 1}$$

- Mas isto dá-nos apenas o formato da onda para $t=0$. Ora, consoante o tempo varia temos $$\Psi(x,t)=\Psi(x)e^{-i\omega t}$$

## 1.3 - Resolução da Equação
1. Partir da Eq.1 e substituir com o $V(x)$ apropriado.
2. Resolver a equação diferencial.
3. Podem haver várias soluções da equação. Aplicar condições de fronteira.
4. Se $V(x)$ for descontínua, aplicar condições de contínuidade nos pontos de descontínuidade (com $d\psi/dx$ ) 
5. A equação de Schrodinger é linear: se $\Psi$ é solução, também $C \cdot \Psi$ também é. Escolher um $C$ de forma que, como vimos acima, $\int_{-\infty}^{+\infty} |C \Psi |^{2}dx=1$ (A isto chama-se _normalizar_ a função)
6. Como a função de Schrodinger representa uma probabilidade, nenhuma função que assuma valores infinitos no seu domínio pode ser solução.
7. A probabilidade de uma partícula estar entre 2 posições $x_{1}, x_{2}$ é $P(x_{1}: x_{2})=\int_{x_{1}}^{x_{2}} |\Psi(x)|^{2} dx$, sendo que esta probabilidade tem que estar sempre entre $0$ e $1$
8. O valor médio (_valor esperado_) de qualquer função $f(x)$ é dado por: $[f(x)]_{med}=\int_{-\infty}^{+\infty}|\Psi(x)|^{2}f(x)dx$

## 1.4 - Equação de Schrödinger 
- Consideremos a carga de um eletrão. De acordo com a física clássica, o seu potencial em relação ao núcleo de um átomo de número atómica $Z$, na posição $(x,y,z)$ (consideramos que o núcleo está na origem) será:
$$V=V(x,y,z)= \frac{-Ze^{2}}{4\pi\varepsilon_{0}\sqrt{x^{2}+y^{2}+z^{2}}}$$
- Temos que a energia do eletrão (cuja massa consideramos como sendo igual a $\mu$) é:
$$\begin{align*}
E_{c}&+V= E\\
\frac{1}{2\mu}(p_{x}^{2}+p_{y}^{2}&+p_{z}^{2})+V(x,y,z)= E \quad \quad \textsf{(Eq. 2)}
\end{align*}$$
- Da relação de Broglie temos $\lambda=h/p$. Temos ainda a função de onda $\Psi(x)= Ae^{ikx}$. Ora, podemos derivar $\Psi$ tendo:
$$\frac{d\Psi}{dx}=iAk~e^{ikx}=iA \frac{2\pi}{\lambda}e^{ikx}=i\frac{p}{\hbar} Ae^{ikx}=i \frac{p}{\hbar}\Psi$$
ou seja, podemos escrever:
$$\begin{align*}
\frac{d}{dx}\Psi&= i \frac{p}{\hbar}\Psi\\
\frac{1}{i} \hbar\frac{d}{dx} =p &\longrightarrow p= -i\hbar \frac{d}{dx}
\end{align*}$$
Analogamente temos $$p_{x}=-i\hbar \frac{\partial}{\partial x}\quad;\quad p_{y}=-i\hbar \frac{\partial}{\partial y} \quad;\quad p_{z}=-i\hbar \frac{\partial}{\partial z}$$
Pelo que na equação acima podemos escrever:
$$\frac{1}{2\mu}(p_{x}^{2}+p_{y}^{2}+p_{z}^{2})=-\frac{\hbar^2}{2\mu} \nabla^{2}$$

- Ao substituir na eq.2 temos:
$$-\frac{\hbar^{2}}{2\mu} \nabla^{2}+V= E $$
e podemos multiplicar ambos os lados pela função de onda:
$$\left[-\frac{\hbar^{2}}{2\mu} \nabla^{2}+V \right]\Psi=E \Psi$$
- De notar que acima temos $\LARGE H\Psi=E\Psi$ em que $H$ é o operador _Hamiltoniano_: $\large H=-\frac{\hbar^2}{2\mu} \nabla^{2}+V$
- Devido à equação dependente do tempo de Schrödinger (não vou fazer a dedução disto) temos que:
$$E\Psi=i\hbar \frac{\partial\Psi}{\partial t}$$
pelo que, finalmente, temos:
$$i\hbar \frac{\partial}{\partial t}\Psi(\vec{r}, t)=\left[- \frac{\hbar^{2}}{2m}\nabla^{2}+V(\vec{r}, t) \right]\Psi(\vec{r}, t) \tag{Eq. 2}$$
- Basicamente a versão geral da Eq. 1, mas para $t$ variável e para qualquer dimensão.

##  1.5 - Resolução da ES para Partícula Livre
- Temos a Eq.2 para 1 dimensão:
$$i\hbar \frac{\partial}{\partial t}\Psi(x,t)=- \frac{\hbar^{2}}{2m} \frac{\partial^{2}}{\partial x^{2}}\Psi(x,t)$$
sendo que o potencial considerado na Eq.2 é em relação ao núcleo, pelo que numa partícula livre temos $V=0$
- Definimos $\Psi(x,t)=\Phi(x)T(t)$ e temos:
$$\begin{align*}
\frac{\partial}{\partial t} \Psi(x,t)&= \Phi(x) \frac{d}{dt}T(t)\\
\frac{\partial}{\partial x}\Psi(x,t)&= T(t) \frac{d}{dx}\Phi(x)\\
\frac{\partial^{2}}{\partial x^{2}}\Psi(x,t)&= T(t) \frac{d^{2}}{dx^{2}}\Phi(x)
\end{align*}$$
- Usaremos a notação $\large\frac{dT}{dt}=\dot T$, $\large\frac{d\Phi}{dx}=\Phi'$ 
- Ao substituir na Eq.2 temos:
$$i\hbar \Phi \dot T= - \frac{\hbar^{2}}{2m}\Phi'' T$$
e dividimos os 2 lados por $\Phi T$ e temos: $$i\hbar \frac{\dot T}{T} = - \frac{\hbar^{2}}{2m} \frac{\Phi''}{\Phi}$$
e vemos que o lado esquerdo depende apenas de $t$ e o direito apenas de $x$

- Sendo que podemos definir $$A=\text{constante}= i\hbar \frac{\dot T}{T}= - \frac{\hbar^{2}}{2m} \frac{\Phi''}{\Phi}$$
e podemos ver que $A$ tem unidades de _energia_.
- Podemos então escrever $A=E$, pelo que se tem:
$$\begin{cases}i\hbar \frac{dT}{dt}=ET \\- \frac{\hbar^{2}}{2m} \Phi''=E \Phi\end{cases}=\begin{cases}\int \frac{dT}{T} = - \frac{iE}{\hbar}\int dt \\ \Phi''+ \frac{2m}{\hbar^{2}}E \Phi=0  \end{cases}$$
- Daqui temos $\large T=C e^{-i \frac{Et}{\hbar}}$ . Ora, para um fotão temos: 
$$E=hf = h \frac{1}{T}=h \frac{1}{T} \frac{2\pi}{2\pi}=\frac{h}{2\pi} \frac{2\pi}{T}=\hbar ~\omega$$
logo temos: $\Large T = Ce^{-i \frac{\hbar\omega}{\hbar}t}=Ce^{-i\omega t}$ 
- Para $\Phi$ temos uma equação diferencial de 2ª ordem, homogénea e com coeficientes constantes, que sabemos resolver facilmente. Definimos $k^{2}=\frac{2mE}{\hbar^{2}}$. Pelo método de Euler temos: $$\Phi(x)=C_{1}e^{ikx}+C_{2} e^{-ikx} $$
- Assim, temos:
$$\Psi(x,t)=\Phi(x)T(t)=C_{1} e^{i(kx-\omega t)} + C_{2}e^{-i(kx+\omega t)}$$
E para 1 partícula temos $\Large \Psi(x,t)=Ce^{i(kx-\omega t)}$

- Verifiquemos as condições de normalização:
    - Verifica-se que $\int_{-\infty}^{+\infty}|\Psi(x,t)|^{2}dx=1$
    - Temos $\Psi^{*}(x,t)=C^{*}e^{-i(kx-\omega t)}$, pelo que $\Psi \Psi^{*}=CC^{*}$
    - Logo, $\int_{-\infty}^{+\infty}\Psi \Psi^{*}dx=\int_{-\infty}^{+\infty}CC^{*}$ diverge e é _diferente de  1_.
    - Ou seja, $\int_{-\infty}^{+\infty}|\Psi|^{2}dx\neq \int_{-\infty}^{+\infty}\Psi \Psi^{*}dx$

## 1.6 - Sistema de 2 ondas/partículas
- Temos 2 ondas, tais que:
    - $\omega_{1}=\omega ~~;~~ k_{1}=k$
    - $\omega_{2}=w+dw ~~;~~ k_{2}=k+dk$
- Temos $\Psi_{1}(x,t)=A\sin(kx-\omega t) ~~;~~ \Psi_{2}(x,t)=A\sin((k+dk)x - (\omega-d \omega)t)$ e assim:
$$\Psi_{1}+\Psi_{2}=A\cos \left[\frac{dk}{2}x- \frac{d\omega}{2}t \right]\sin \left[\frac{k+dk}{2}x - \frac{\omega-d\omega}{2}t \right]$$
- Se tivermos $k\gg dk~~;~~ \omega\gg d\omega$ então
$$\Psi_{1}+\Psi_{2}\approx 2A\cos \left[\frac{dk}{2}x - \frac{d\omega}{2} t \right]\sin \left[\frac{k}{2}x - \frac{\omega}{2}t \right]$$
pelo que o gráfico desta função de onda será do tipo de um batimento

### 1..6.1 - Velocidades
- Tal como em OMC, temos que a velocidade de uma partícula será a _velocidade de fase_:
$$v_{f}=\lambda f=\frac{\omega}{k}$$
- Temos que $\large v=\frac{p}{m}$ e temos as relações de Broglie e Einstein: $\Large p=\frac{h}{\lambda}~~;~~ E=hf$ 
pelo que $$\omega=2\pi f=2\pi \frac{E}{h} \quad \quad; \quad \quad k=\frac{2\pi}{\lambda}=\frac{2\pi p}{h}$$
e temos $$v_{f}=\frac{\omega}{k}=\frac{E}{p}=\frac{\frac{p^{2}}{2m}}{p}=\frac{p}{2m}$$

- Por outro lado, a velocidade da onda $\Psi_{1}+\Psi_{2}$ será a _velocidade de grupo_:
$$v_{g}=\frac{d\omega}{dk}$$
temos $$E=\hbar \omega\rightarrow d\omega=\frac{dE}{\hbar} \quad \quad; \quad \quad p=hk\rightarrow dk=\frac{dp}{h}=\frac{dp}{\hbar}$$
Logo:
$$v_{g}=\frac{d\omega}{dk}=\frac{dE}{dp}=\frac{d}{dp}\left(\frac{p^{2}}{2m} \right)=\frac{p}{m}=2v_{f}$$

## 1.7 - Sistema de 3 ondas/partículas
- Tendo agora 3 ondas constantes no tempo definidas por:
    - $k_{1}=k_{0} ~~;~~ A_{1}=A_{0}$
    - $k_{2}=k_{0}+ \frac{\Delta k}{2}~~;~~ A_{2}=\frac{A_{0}}{2}$
    - $k_{3}=k_{0}- \frac{\Delta k}{2}~~;~~ A_{3}=\frac{A_{0}}{2}$

- Ou seja: $\large \Psi_{1}=A_{0}e^{ik_{0}x}$ ; $\large \Psi_{2}=\frac{A_{0}}{2} e^{i(k+ \frac{\Delta k}{2})x}$ ;  $\large \Psi_{3}=\frac{A_{0}}{2} e^{i(k- \frac{\Delta k}{2})x}$
- Pelo que temos $$\Psi_{1}+\Psi_{2}+\Psi_{3}=A_{0} e^{ik_{0}x}\left[1+\cos \left( \frac{\Delta k}{2}x\right) \right]$$
- Temos:
    - máximos para $x=0,2\pi,4\pi,\dots$
    - a onda anula-se para quando $\frac{\Delta k}{2}x=\pi,3\pi,5\pi,\dots$

- Assim, tendo 2 pontos em que a onda se anula, $x_{1},~x_{2}$ tais que $\frac{\Delta k}{2}x_{1}=\pi~~;~~ \frac{\Delta k}{2}x_{2}=3\pi$, temos que $x_{2}-x_{1}$ nos dá a incerteza da posição $x$ da partícula: $$x_{2}-x_{1}=\Delta x=\frac{4\pi}{\Delta k}$$
Logo $$\Delta x \Delta k=4\pi \rightarrow \Delta x \Delta p=4\pi \hbar$$
(Aqui tem-se que $p=\frac{h}{\lambda}=\hbar k\rightarrow dp=\hbar \cdot dk$ e que $\hbar = \frac{h}{2\pi}\rightarrow h=2\pi\hbar$)

#  2 - Princípio de Incerteza
- As teorias da física clássica são deterministas: sabendo $\vec{r}$ e $\vec{p}$ em $t=0$ conseguimos prever todo o comportamento do sistema.
- Mas Heisenberg e Bohr questionavam se isto poderia ser feito com radiação. Assim, temos que não é possível, numa certa experiência, com uma precisão maior do que aquela indicada pelo _princípio da incerteza de Heisenberg_.
    - Primeiro, temos que, numa experiência, não conseguimos fisicamente medir o momento linear ($p_{x}$) e a posição ($x$), tendo-se que $$\Delta p_{x} \Delta x \geq \frac{\hbar}{2}$$(sendo $\Delta p_{x}$ e $\Delta x$ as incertezas associadas das medições feitas)
    - De notar que este princípio não tem nada a ver com os instrumentos de medição. Aliás, a fórmula acima diz-nos que mesmo com _intrumentos ideias_ nunca teremos incerteza menos do que aquela indicada.
    - Temos ainda um produto de incertezas, pelo que se diminuirmos a incerteza de $p_{x}$ iremos aumentar a de $x$.

> __*EXEMPLO*__
> É feita uma medição da velocidade de um corpo com uma incerteza de $1.0 \cdot10^{-3}m/s$. Qual será a incerteza mínima da posição do corpo que conseguimos determinar?
>
> Temos que $\Delta v=10^{-3}m/s$. Como $p=mv$ então $\Delta p=m \Delta v$
> Pelo que a incerteza mínima que conseguimos obter para a posição é $$\Delta x \Delta p\geq \frac{\hbar}{2}\longrightarrow \Delta x_{min}=\frac{\hbar}{2\Delta p}$$
>
> Assim, se o corpo em estudo fosse:
> - um _eletrão_ 
> Temos $\Delta p=m \Delta v=9.11\cdot10^{-11} \times10^{-3}=9.1\cdot10^{-34}~kg~m/s$ pelo que $$\Delta x_{min}(e^{-})=\frac{\hbar}{2\Delta p}=\frac{6.0\cdot10^{-34}~Js}{4\pi (9.1\cdot10^{-34}~kg~m/s)}=5.2~cm$$
> - uma _bola de bowling_ (considerando $m=6~kg$)
> Temos $\Delta p=m \Delta v=6\cdot10^{-3}~kg~m/s$ pelo que $$\Delta x_{min}(bowling)=\frac{\hbar}{2\Delta p}=\frac{6.0\cdot10^{-34}~Js}{4\pi (6\cdot10^{-3}~kg~m/s)}=8\cdot10^{-33}~m$$
> Verificasse então o que foi dito acima: quanto menor for a incerteza de uma das variávels, maior será a da outra (no eletrão $\Delta p$ tinha incerteza muito reduzida e $\Delta x$ muito elevada; na bola de bowling ao contrário)

#moderna #fisica #schrodinger