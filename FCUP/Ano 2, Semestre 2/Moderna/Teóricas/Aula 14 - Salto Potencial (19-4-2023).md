# 1 - Salto de Potencial
![[salto potencial.png]]
- Num salto de potencial temos:
$$V(x)=\begin{cases}0 &; &x<0\\ V_{0} &; &x\geq0\end{cases}$$
- Temos a equação de Schrödinger: $i\hbar \frac{\partial}{\partial t}\Psi=\left[ - \frac{\hbar^{2}}{2m} \frac{\partial^{2}}{\partial x^{2}} - V \right]\Psi$ de onde tiramos:
$$\Psi(x,t)=\Psi(x) e^{-i \frac{E}{\hbar}t}$$
- Considerando a situação acima como estacionário (independente do tempo) temos:
$$- \frac{\hbar^{2}}{2m}\Psi''(x) + V(x)\Psi(x)=E \Psi(x)$$
- Assim, consideremos 2 casos da, conforme a energia da partícula, $E$

## 1.1 - $E>V_{0}$
#### -- $x<0$
- Temos $V=0$ logo:
$$\begin{align*}
\frac{\hbar^{2}}{2m}\Psi'' + E\Psi&= 0\\
\textsf{Pol. Caraterístico }\to \quad \quad r^{2} &=  - \frac{2m}{\hbar^{2}}E\\
r &= \sqrt{- k_{1}^{2}} \quad;\quad k_{1}=\sqrt{\frac{2mE}{\hbar^{2}}} \\
\textsf{Método Euler}\to \quad \quad \Psi_{1}(x)&= A e^{ik_{1}x} + B e^{-ik_{1}x}
\end{align*}$$
#### -- $x>0$
- Temos $V=V_{0}$ logo:
$$\begin{align*}
-\frac{\hbar^{2}}{2m}\Psi'' - \Psi&(V_{0}-E)= 0\\
\textsf{Pol. Caraterístico }\to \quad \quad r^{2}&= \sqrt{ \frac{2m}{\hbar^{2}}(E-V_{0})}\\
r &= \sqrt{k_{2}^{2}} \quad;\quad k_{2}=\sqrt{\frac{2m}{\hbar^{2}} (E-V_{0})}\in\mathbb R \\
\textsf{Método Euler}\to \quad \quad \Psi_{1}(x)&= C e^{k_{2}x} + D e^{-k_{2}x}
\end{align*}$$

- Temos então as condições de fronteira.
    - Como $\Psi$ é contínua, então $\Psi_{1}(0)=\Psi_{2}(0)=0$, logo $\large A+B=C+D$
    - As derivadas das funções também são contínuas, logo: $$\begin{align*}
\Psi_{1}'(x)&= ik_{1}Ae^{ik_{1}x} - ik_{1}Be^{-ik_{1}x}\\
\Psi_{2}'(x)&= k_{2}Ce^{k_{2}x} - k_{2}De^{-k_{2}x}\\
\Psi_{1}'(0)=\Psi_{2}'(0)&= 0 \longrightarrow ik_{1}A-ik_{2}B = k_{2}C-k_{2}D
\end{align*}$$
    - $\Psi$ tem que ser sempre finita, logo $\large C=0$

- Ora, temos então um sistema:
$$\begin{cases}A+B = D\\ ik_{1}A-ik_{2}B = k_{2}D\end{cases}\Longrightarrow \begin{cases}A = \frac{D}{2} \left(1+ i \frac{k_{2}}{k_{1}} \right)\\ B = \frac{D}{2} \left(1-i \frac{k_{2}}{k_{1}} \right) \end{cases}$$

## 1.2 - Probabilidades
- Consideremos as seguintes variáveis, que indicam o fluxo de partículas:
$$\small\begin{align*}
\textsf{Incidente}\rightarrow \quad \mathcal{J}_{i}&= \textsf{\# partículas atravessa a barreira p/área, p/tempo, em x<0, a mover segundo }+\hat{x}\\
\textsf{Refletido}\rightarrow \quad \mathcal{J}_{r}&= \textsf{\# partículas atravessa a barreira p/área, p/tempo, em x<0, a mover segundo }-\hat{x}\\
\textsf{Transmitido}\rightarrow \quad \mathcal{J}_{i}&= \textsf{\# partículas atravessa a barreira p/área, p/tempo, em x>0, a mover segundo }-\hat{x}\\
\end{align*}$$
Ora, sendo $n=\frac{\#~particulas}{volume}$ a densidade de partículas e $v_{1},v_{2}$ as velocidades com que as partículas se movem à esquerda e direita do salto de potencial, temos:
$$\mathcal{J}_{i} = n_{i}v_{1} \quad;\quad \mathcal{J}_{r} = n_{r}v_{1} \quad ;\quad \mathcal{J}_{t} = n_{t}v_{2}$$
- Assim, podemos definir 2 coeficientes:
$$\begin{align*}
\textsf{Coeficiente de Reflexão } \to R &= \frac{\mathcal{J}_{r}}{\mathcal{J}_{i}}= \frac{n_{r}}{n_{i}}\\
\textsf{Coeficiente de Transmissão } \to \tau &= \frac{\mathcal{J}_{t}}{\mathcal{J}_{i}}= \frac{n_{t}}{n_{i}} \frac{v_{2}}{v_{1}}
\end{align*}$$
- Como estes são coeficientes relativos ao número de partículas incidentes (que acaba por ser o número total de partículas) temos que:
$$R + \tau = 1$$
- Ora, tendo-se $\Psi_{1}(x,t)=\left[ A e^{ik_{1}x}+ Be^{-ik_{1}x}\right] e^{-i \frac{E}{\hbar} t}$, podemos escrever $\frac{E}{\hbar}=\omega$ e assim temos:
$$\Psi_{1}(x,t)=A e^{i(k_{1}x-\omega t)} + B e^{-i(kx+\omega t)}$$
Como vimos em Ondas e Meios Contínuos, $kx$ e $\omega t$ terem sinais iguais indica que a partícula se move para trás, e sinais diferentes indicam que a partícula de move para a frente. Ou seja, o termo com $A$ move-se para a frente (*incidente*) e o termo com $B$ move-se para trás (*refletido*). Ora, aqui estamos a falar de probabilidades e, como já vimos, em mecânica quântica não são as amplitudes que indicam probabilidades mas sim intensidades/módulos. Ou seja, temos:
$$R = \frac{|B|^{2}}{|A|^{2}}$$
- Temos:
![[salto potencial ondas E maior.png]](sendo que à esquerda temos $t=0$ e à direita $t=\frac{1}{4}T$)
- Vemos que a densidade de probabilidade não depende com o tempo.

## 1.3 - $E<V_{0}$
- Repetimos a análise feita acima:

#### -- $x<0$
- Nada muda por termo $E<V_{0}$ ou seja, temos:
$$\Psi_{1}'(x)=Ae^{i k_{1}'x} + Be^{-ik_{1}'x} \quad \quad;\quad \quad k_{1}'=\sqrt{\frac{2mE}{\hbar^{2}}}$$
#### -- $x>0$
- Neste caso, como temos $k_{2}'=\sqrt{ \frac{2m}{\hbar^{2}}(E-V_{0})}$, agora não teremos $k_{2}\in\mathbb R$, mas sim $k_{2}'$ será _complexo_. Assim:
$$\Psi_{2}'(x)= Ce^{ik_{2}'x} + De^{-ik_{2}'x} \quad \quad;\quad \quad k_{2}'=\sqrt{ \frac{2m}{\hbar^{2}}(E-V_{0})}$$

- Ao aplicar as condições de fronteira temos:
    - $\Psi$ contínua : $\large A+B=C+D$
    - $\Psi'$ contínua : $\large ik_{1}'(A-B)=ik_{2}'(C-D)$

- Tal como vimos há pouco para $x<0$, $A$ representa uma partícula a incidir ($\rightarrow$) e $B$ reperesenta uma particúla a ser refletida/ir para trás ($\leftarrow$). Ora, o mesmo pode ser dito para o outro lado do salto de potencial: $C$ é incidir ($\rightarrow$) e $D$ é refletir ($\leftarrow$). Ora, à direita do salto de potencial temos que a energia incial da partícula é menor do que o potencial nela aplicado, ou seja, é impossível que ela seja refletida. Assim: $\large D=0$

- Para este caso temos:
$$R = \left(\frac{1-\sqrt{1-\frac{V_{0}}{E}}}{1+\sqrt{1-\frac{V_{0}}{E}}} \right)^{2}$$
- Temos:
![[salto potencial ondas E menor.png]](sendo que à esquerda temos $t=0$ e à direita $t=\frac{1}{4}T$)
- Vemos que a densidade de probabilidade é independente do tempo.

### 1.3.1 - Princípio de Incerteza
- Uma partícula penetrar a barreira de potencial é um fenómeno que está associado à natureza de onda da partícula e ao princípio de incerteza. 
- Ora, temos:
$$\Psi_{1}'=Ae^{ik_{1}x} + Be^{-ik_{1}x} \Longrightarrow |\Psi_{1}'|^{2} \propto e^{-2k_{1}x}$$
- Se definirmos $\Delta x$ como sendo a distância em que a probabilidade de encontrar uma partícula diminui um fator de $1/e$, então temos:
$$e^{-2k_{1}\Delta x}=e^{-1} \longrightarrow \Delta x=\frac{1}{2k_{1}}=\frac{1}{2} \frac{\hbar}{\sqrt{2m(V_{0}-E)}}$$

- Ora, para uma partícula passar a barreira, tem que ganhar uma energia de, pelo menos, $V_{0}-E$. Além disso, para se mover em $x>0$ a partícula tem que ganhar energia cinética. Ora, isto quebra a conservação de energia. 
- Mas temos, do princípio de incerteza, $\Delta E\Delta t \sim\hbar$. Ora, isto significa que o princípio de conservação de energia _não se aplica_ em tempos para os quais $\Delta E\sim \frac{\hbar}{\Delta t}$. Na prática, isto significa que a particula recebe energia a mais (de modo a não haver conservação), mas devolve a energia após $\Delta t\sim \frac{\hbar}{\Delta E}$.
- Ora, temos $$\Delta t = \frac{\hbar}{V_{0}-E+E_{c}}$$ e sendo a velocidade da partícula $v=\sqrt{\frac{2E_{c}}{m}}$ temos $$\Delta x=\frac{1}{2}v \Delta t=\frac{1}{2}\sqrt{\frac{2E_{c}}{m}}\frac{\hbar}{V_{0}-E+E_{c}} = \frac{1}{2} \frac{\hbar}{\sqrt{2m(V_{0}-E)}}$$
- Ora, a fórmula acima indica o $\Delta x_{max}$ que podemos ter. 
- Assim, demonstramos que a penetração da barreira por uma partícula segundo a teoria de Schrödinger é completamente consistente com o princípio de incerteza.

#moderna #fisica #schrodinger 