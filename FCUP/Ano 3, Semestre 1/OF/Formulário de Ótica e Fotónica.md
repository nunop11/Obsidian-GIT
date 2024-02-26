## 0 - Constantes e Identidades
| Constante | Valor |
| ---- | ---- |
| $\varepsilon_{0}$ | $8.854187\cdot10^{-12} \text{F/m}$ |
| $\mu_{0}$ | $1.256637\cdot10^{-6}\text{N/A}^{2}$ |
| $c$ | $299792458 \text{m/s}$ |

**Laplaciano** :
    **Cartesianas** : $\nabla^{2}f=\partial_{x}^{2}f+\partial_{y}^{2}f+\partial_{z}^{2}f$
    **Cilíndricas** : $\nabla^{2}f = \frac{1}{\rho}\partial_{\rho}(\rho \partial_{\rho}f)+ \frac{1}{\rho^{2}}\partial_{\rho}^{2}f+\partial_{z}^{2}f$
    **Esféricas** : $\partial^{2}f=\frac{1}{r^{2}}\partial_{r}(r^{2}\partial_{r}g) + \frac{1}{r^{2}\sin\theta}\partial_{\theta}(\sin\theta\partial_{\theta}g)+ \frac{1}{r^{2}\sin^{2}\theta}\partial_{\varphi}^{2}f$

Identidade útil : $\nabla\times(\nabla \times\vec{A})=\nabla(\nabla\cdot\vec{A})-\partial^{2}\vec{A}$

## 1 - Ótica Física
### 1.1 - Eletromagnetismo
**Equações de Maxwell**
$$ \begin{align*} \nabla \cdot \vec E &= \frac \rho{\varepsilon_0} &\text{(Lei de Gauss)}&&&&|&&&& \nabla \cdot \vec D &= \rho_f\\
\nabla \cdot \vec B &= 0 &&&&&|&&&& \nabla \cdot \vec B &= 0\\
\nabla \times \vec E &= -\partial_t \vec B &\text{(Lei de Faraday)}&&&&|&&&& \nabla \times \vec E &= -\partial_t \vec B\\
\nabla \times \vec B &= \mu_0 \left(\vec{\mathcal{J}} + \varepsilon_0 \partial_t \vec E\right) &\text{(Lei de Ampère-Maxwell)} &&&&|&&&& \nabla \times \vec H &= \vec{\mathcal{J}}_f + \partial_t \vec D \end{align*}  $$
em que, num meio sem magnetização: $$\vec{D}=\varepsilon_{0}\vec{E}+\vec{P} \quad \quad;\quad \quad \vec{H}=\frac{1}{\mu_{0}}\vec{B}$$
**Equações de Onda** : $\nabla^{2}\vec{E}=\varepsilon_{0}\mu_{0}\partial_{t}^{2}\vec{B} \quad \quad;\quad \quad \nabla^2 \vec E -\varepsilon_0 \mu_0 \partial_t^2 \vec E = \mu_0 \partial^2_t \vec P$
**Onda Plana** : $\vec{E}(\vec{r},t)=\vec{E_{0}}\sin(\vec{k}\cdot\vec{r}-\omega t+\phi_{0})$
**Sobreposição de Ondas** : $\vec{E}(\vec{r},t)=2\vec{E_{0}}\cos\left(\frac{\phi_{1}-\phi_{2}}{2}\right)\sin\left(\vec{k}\cdot\vec{r}-\omega t+ \frac{\phi_{1}+\phi_{2}}{2}\right)$
**Amplitude do campo magnético** : $\vec{B_{0}}=\frac{\vec{k}\times\vec{E_{0}}}{\omega}=\frac{\hat{k}\times\vec{E_{0}}}{c}~~,~~|B_{0}|=\frac{|E_{0}|}{c}$
**Relações** : $\vec{k}=\frac{\omega}{v}\hat{k} \quad;\quad k=\frac{\omega}{v} \quad;\quad \mu_{0}\varepsilon_{0}=\frac{1}{c^{2}}$

### 1.2 - Energia
**Vetor Poynting** : $\vec S = \frac 1{\mu_0}(\vec E \times \vec  B) = \vec E \times \vec  H=c^{2}\varepsilon_{0}(\vec{E}\times\vec{B})$
**Módulo do vetor Poynting** : $S=c\varepsilon_{0}E_{0}^{2}$
**Densidade de Energia** : $u=u_{E}+u_{B}=\frac{1}{2}(\varepsilon_{0}E^{2}+ \frac{1}{\mu_{0}}B_{0}^{2})=\frac{1}{2}\varepsilon_{0}E^{2}$
**Intensidade de onda EM** : $I=\langle S\rangle=\frac{1}{2} c\varepsilon_{0}E_{0}^{2}=cu$
**Densidade momento linear** : $\vec p = \varepsilon_0 \vec E \times \vec B = \frac{\vec S}{c^2}$
**Densidade de momento angular**: $\vec{L}=(\vec{r}-\vec{r_{0}})\times\vec{p}=\vec{L}_{int}-\vec{L}_{orb}$ com $\vec{L}_{int}=\varepsilon_{0}(\vec{E}\times\vec{A})~~,~~\vec{L}_{orb}=\varepsilon_{0}\vec{E}[(\vec{r}-\vec{r_{0}})\times\nabla]\vec{A}$
**Pressão de radiação** : $P = \frac{\vec F \cdot \hat n}{A}=\frac{\vec S \cdot \hat n}{c}$
    *Reflexão total* : $P=\frac{2S}{c}=\frac{2I}{c}$
    *Absorção total* : $P=\frac{S}{c}=\frac{I}{c}$

### 1.3 - Matéria
**Susceptibilidade** : $\vec{P_{0}}(\omega)=\varepsilon_{0}\chi(\omega)\vec{E_{0}}$
**Relação Dispersão** : $D (\vec k,\omega) = \frac{c^2k^2}{1+\chi(\omega)}-\omega^2$
**Constante dielétrica** : $\varepsilon_{r}(\omega)=\varepsilon_{r}'(\omega)+i\varepsilon_{r}''(\omega)=1-\chi(\omega)$
**Índice de Refração Complexo** : $\mathcal{N}(\omega)=n'(\omega)+in''(\omega)=\sqrt{1+\chi(\omega)}=\sqrt{\varepsilon_{r}(\omega)}$
$$\begin{align*} n'(\omega) &= \sqrt{\frac12(1+\text{Re}[\chi(\omega)]) + \frac12\sqrt{\Delta^2 + \text{Im}[\chi(\omega)]^2}} \approx \sqrt{1 + \text{Re}[\chi(\omega)]} \\ n''(\omega) &= \frac{\text{Im}[\chi(\omega)]}{2n'(\omega)} \approx \frac{\text{Im}[\chi(\omega)]}{2\sqrt{1+\text{Re}[\chi(\omega)]}} \end{align*}$$
(com as aproximações feitas para meios pouco absroventes: $\small\text{Im}(\chi)\ll\text{Re}(\chi)$)
**Índice de Refração e número de onda** : $k = \frac{\mathcal N(\omega)\omega}{c} = \frac{[n'(\omega) + i n''(\omega)]}{c}\omega \quad \to\quad n'= \frac{c}{v}$
**Índice de Refração e campo** : $\vec E(\vec r,t) = \vec E_0 \exp[-n''\vec k_0\cdot \vec r]\exp[i(n'\vec k_0\cdot \vec r-\omega t)] \quad \quad;\quad \quad \vec{k_{0}}=\omega \frac{\vec{k}}{|ck|}$ 
    *onda propagante* : $n'\neq0~~,~~n''=0$
    *onda evanescente* : $n'=0~~,~~n''\neq0$
    *onda propagante atenuada* : $n'\neq0~~,~~n''\neq0$

**Lei de Lambert-Beer** : $I(z)=I_{0}\exp(-2n''k_{0}z)$
**Velocidade de fase** : $v_{f}=\frac{c}{n'}$
**Velocidade de grupo** : $v_{g}=\frac{\partial\omega}{\partial k}\approx \dfrac{v_f}{1 + \frac{ck}{n'}\frac{dn'}{d\omega}}$
*NOTA*: a velocidade de grupo é a velocidade envolvente da onda, ou seja $v_{g}\le c$. Mas $v_{f}$ pode ser maior. 
**Espessura da camada anti-reflexo** : $t = \frac{\lambda}{4n}$

### 1.4 - Modelo de Lorentz
Para campos fracos, em dielétricos. Assumimos que $\vec{\mathcal{J}}_{\ell}=\vec{0}$.
**Equação de Movimento** : $\begin{align*} m_e \Delta \ddot{\vec r} = q_e \vec E - m_e \gamma \Delta \dot{\vec r} -m_e \omega_0^2\Delta \vec r\to \frac{q_e}{m_e} \vec E= \Delta \ddot{\vec r} + \gamma \Delta \dot{\vec r} + \omega_0^2 \Delta \vec r \end{align*}$
**Resposta do Meio** : $\vec r_0(\omega) = \frac{q_e}{m_e}\cdot \frac{\vec E_0}{\omega^2_0 - i\omega \gamma -\omega^2}$
**Momento Dipolar** : $\vec P(\omega) = N \vec \mu (\omega) = N q_e\vec r_0 =\frac{Nq_e^2}{m_e}\cdot \frac{\vec E_0(\omega)}{\omega^2_0 - i\omega \gamma- \omega^2}$
**Susceptibilidade** : $\chi(\omega) = \sum_{n=0}^Nf_n\frac{\omega_p^2}{\omega^2_{0,n} - i\omega\gamma_n - \omega^{2}}\quad \quad;\quad \omega_{p}=\sqrt{\frac{Nq_{e}^{2}}{m_{e}\varepsilon_{0}}}~~(\text{frequência de plasma})$
**Índice de Refração** : $\mathcal N^2(\omega) = 1+\chi(\omega) = 1 + \sum_{n=0}^Nf_n\frac{\omega_p^2}{\omega^2_{0,n} - i\omega\gamma_n - \omega^2}$

### 1.5 - Sellmeier
$$n^{2}(\lambda_{0}) = 1 + \sum_{n=0}^{N} \frac{B_{n}\lambda_{0}^{2}}{\lambda_{0}^{2} - C_{n}} \quad \quad;\quad \quad B_{n} = \frac{f_{n}\omega_{p}^{2}}{\omega_{0,n}^{2}}\quad,\quad C_n = \left(\frac{2\pi c}{\omega_{0,n}}\right)^2$$

### 1.6 - Modelo de Drude
Considera-se $\vec{P}=\vec{0}$. Usado para condutores.
**Equação do movimento** : $m_{e}\ddot{\vec{r}}=q_{e}\vec{E}-m_{e}\gamma\dot{\vec{r}}$
**Densdiade de corrente livre** : $\vec{\mathcal{J}}_{\ell}=q_{e}N\langle v\rangle~~,~~\langle v\rangle=\int \frac{q_{e}}{m_{e}}\frac{E}{\gamma-i\omega}d\omega$
**Densidade Corrente** : $\vec{\mathcal{J}}_{0}(\vec r,\omega) = \left(\frac{Nq_e^2}{m_e}\right)\frac{\vec E_0(\vec r,\omega)}{\gamma - i\omega}$
**Índice Refração** : $\mathcal N^2(\omega) = \frac{k^2c^2}{\omega^2}= 1- \frac{\omega_p^2}{i\gamma\omega+\omega^2}$
**Relação Clausius-Mossoti** : $\frac{\varepsilon_r - 1}{\varepsilon_r + 2} = \frac{N\alpha}{3\varepsilon_0}$ ($N$ é o número de dipolos e $\alpha$ é a polarizabilidade atómica)
    *Susceptibilidade* : $\chi(\omega) = \frac{\frac{N\alpha}{\varepsilon_0}}{1-\frac{N\alpha}{3\varepsilon_0}}$
    *Índice de Refração* : $\frac{n^2 - 1}{n^2 + 2} = \frac{N\alpha}{3\varepsilon_0}$
**Resposta do Meio** : $\vec r_0(\omega) = \frac{q_e}{m_e}\cdot \frac{\textbf E_0}{\omega^2_0 - i\omega \gamma -\omega^2}$
**Densidade de Momento Dipolar** : $\vec P(\omega)= N \vec \mu (\omega)= N q_e\vec r_0=\frac{Nq_e^2}{m_e}\cdot \frac{\vec E_0(\omega)}{\omega^2_0 - i\omega \gamma- \omega^2}$

### 1.7 - Outros

**Meios LHA** : $\varepsilon_{r}=\begin{pmatrix}n_{x}^{2} & 0 & 0\\0 & n_{y}^{2} & 0\\0 & 0 & n_{z}^{2}\end{pmatrix}$
**Relação com as componentes** : $\frac{S_{x}^{2}}{n^{2}-n_{x}^{2}}+\frac{S_{y}^{2}}{n^{2}-n_{y}^{2}}+\frac{S_{z}^{2}}{n^{2}-n_{z}^{2}}=\frac{1}{n^{2}}$
**Meio Isotrópico** : $n_x= n_y = n_z = n_0 ~~\to~~ (n_0^2 - n^2)^2n^2 = 0$
**Meio Uniaxial** : $n_x = n_y = n_0 ~,~ n_z = n_e ~~\to~~ (n_0^2-n^2)\left(\frac1{n^2} - \frac{S_x^2 + S_y^2}{n_e^2} - \frac{S_z^2}{n_0^2}\right) = 0$ ; $\vec k = S_x \hat{\vec x}+ S_y \hat{\vec y}+ S_z \hat{\vec z}$
**Equações de Hamilton** : $\frac{d\textbf r}{dt} = \frac{\partial\omega}{\partial\textbf k}\quad\quad\frac{d\textbf k}{dt} = -\frac{\partial\omega}{\partial r}\quad\quad \frac{d\omega}{dt} = \frac{\partial \omega}{\partial t}$
**Lei de Snell** : $n_{i}\sin\theta_{i}=n_{t}\theta_{t}$

**Leis de Fresnel** : 
$$\begin{align*}
r_P &= \frac{E_r}{E_i} = \frac{n_t\cos\theta_i-n_i\cos\theta_t}{n_t\cos\theta_i+n_i\cos\theta_t} &&& t_P&= \frac{E_t}{E_i} = \frac{2n_i\cos\theta_i}{n_t\cos\theta_i+n_i\cos\theta_t}\\
r_S &= \frac{E_r}{E_i} = \frac{n_i\cos\theta_i - n_t\cos\theta_t}{n_i\cos\theta_i + n_t\cos\theta_t} &&& t_S &= \frac{E_t}{E_i} = \frac{2n_i\cos\theta_i}{n_i\cos\theta_i + n_t\cos\theta_t}
\end{align*}$$
e temos os coeficientes de reflexão e transmissão: $R_{P}=r_{p}^{2}~,~T_{P}=1-R_{P}~~;~~ R_{s}=r_{s}^{2}~,~T_{S}=1-R_{S}$
**Ângulo Brewster** : $\theta_{i}=\theta_{B}=\arctan\left(\frac{n_{t}}{n_{i}}\right)$ e temos $\theta_{B}+\theta_{t}=\pi/2$. Temos ainda que quando luz polarizada incide com ângulo de Brewster ela é refletida com polarização S.
**Ângulo Crítico** : $\theta_{i}=\theta_{c}=\arcsin\left(\frac{n_{t}}{n_{i}}\right)$

### 1.8 - Feixes
**Campo** : $\vec E(\vec r,t) = \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty} \exp\left(-\frac{\vec k^2_\perp}{2\Delta k^2_\perp}\right)\vec E_0 \exp[i(\vec k\cdot \vec r- \omega t)]dk^2_\perp$
**Largura do Feixe** : $\Delta r_\perp = \sqrt{\dfrac{1+ \frac{\textbf r^2_{||}c^2}{4\omega^2}}{\Delta k_\perp^2}}$

## 2 - Ótica Geométrica
### 2.1 - Refletores
**Elíptico** : $\left(\frac{x}{a}\right)^{2}+\left(\frac{y}{b}\right)^{2}=1$ com $a$ o eixo principal e $b$ o secundário. Temos $b=\sqrt{a^{2}-d^{2}}$ com $d$ a distância fonte-foco
**Parabólico** : $x=ay^{2}$ com $a=\frac{1}{4}q$ com $q$ a coordenada do foco com o centro da parábola em $z=0$
**Hiperbólico** : $\left(\frac{x}{a}\right)^{2}-\left(\frac{y}{b}\right)^{2}=1$
**Espelho Côncavo** (esférico) : $\frac{1}{p}+ \frac{1}{q}=\frac{2}{r}=\frac{1}{f}$
    *Erro aproximação de espelho concavo a parabólico* : $\delta_{xx}=\frac{y^{2}}{4r^{2}}$
    *Erro na utilização do plano principal* : $\delta_{xy}=\frac{y}{2r}$
**Espelho Convexo** : $- \frac{1}{p}+ \frac{1}{q}=\frac{2}{r}=\frac{1}{f}$
**Fator de Ampliação transversal** : $m_{T}=\frac{h_{i}}{h_{o}}$
**Fator de Ampliação Longitudinal** : $m_{L}=\frac{x_{2}'-x_{1}'}{x_{2}-x_{1}}$

### 2.1 - Dioptro
$\frac{n_{1}}{p}+\frac{n_{2}}{q}-(n_{2}-n_{1})\frac{1}{r}=0$
**Foco de Entrada** : $f_{e}=\frac{n_{2}}{n_{2}-n_{1}}r \quad \quad(p\to\infty)$
**Foco de Saída** : $f_{s}=\frac{n_{1}}{n_{2}-n_{1}}r \quad \quad(q\to\infty)$
**Dioptro oval cartesiana** : $n_1 p + n_2 q = n_1 \sqrt{(x-p)^2 + y^2} + n_2 \sqrt{(x+q)^2 + y^2}$

### 2.2 - Lentes
![[lente 2 dioptros.png|450]]
$$\frac{n_m}{s_{o1}}+\frac{n_m}{s_{i2}} = (n_l - n_m)\left(\frac1{R_1} - \frac1{R_2}\right) + \frac{n_l d}{(s_{i1} - d)(s_{o2} + s_{i1})}$$
com $n_{1}>n_{l}~,~R_{2}<0$. $s_{o},f_{o}$ são positivos à esquerda de $V$. $s_{i},f_{i}$ são positibos à direita de $V$.
**Equação das Lentes Finas** : $\frac1f = \frac1{s_o} + \frac1{s_i} = \left(\frac{n_l}{n_m} - 1\right)\left(\frac1{R_1} - \frac1{R_2}\right)$
**Potência de lente** : $P=\frac{1}{f}$ (Exemplo: Potência 8D - $f=\frac{1}{8}=0,125m$)
**Ampliação transversal** : $m_{T}=\frac{y_{i}}{y_{o}}=- \frac{s_{i}}{s_{o}}$
**Ampliação longitudinal** : $m_{L}=\frac{x_{2}'-x_{1}'}{x_{2}-x_{1}}$
**Combinação de Lentes Finas** :  $s_{i2} = \dfrac{f_2d - \frac{f_2s_{o1}f_1}{s_{o1}-f_1}}{d - f_2 - \frac{s_{o1}f_1}{s_{o1}-f_1}}$ 
**Espessura lente para minimizar lambda** : $d = \frac{\Delta \lambda}{4n_2\sqrt{1-\left(\frac{n_1-n_2}{n_1+n_2}\right)^2}}$
**Relações da distância focal** : $s_{o}s_{i}=f^{2}~~~~;~~~~ f=\frac{r}{2}=\frac{1}{\frac{1}{r_{1}}- \frac{1}{r_{2}}}$
**Aberração Esférica** : $\eta=$

![[magnificacoes lentes.png]]      ![[tipos lentes.png|216]]

Numa lente côncava os focos de entrada e saída estão trocados ($f_{e}$ do lado oposto à lente)
Raios:
    - Paralelo a eixo ótico $\to$ passar por foco de saída
    - Passa por foco de entrada $\to$ paralelo ao eixo ótico
    - Passa por centro da lente

### 2.3 - Matrizes transferência
$$\begin{bmatrix}x_{s}\\ \theta_{s}\end{bmatrix}=\begin{bmatrix}A & B\\C & D\end{bmatrix}\begin{bmatrix}x_{e}\\\theta_{e}\end{bmatrix}$$
em que $A=m_{T}$ e $B=0$ garante que estamos no plano da imagem.

-

| matriz | processo | matriz | processo |
| ---- | ---- | ---- | ---- |
| $\begin{pmatrix}1 & d\\0 & 1\end{pmatrix}$ | propagação no vazio | $\begin{pmatrix}1 & 0\\0 & \frac{n_1}{n_2}\end{pmatrix}$ | refração em interface plano |
| $\begin{pmatrix}1 & \frac{d}{n}\\0 & 1\end{pmatrix}$ | propagação em meio $n$ | $\begin{pmatrix}1 & 0\\ \frac{n_1-n_2}{n_2R} & \frac{n_1}{n_2}\end{pmatrix}$ | refração em interface curvo |
| $\begin{pmatrix}1 & 0\\- \frac1f & 1\end{pmatrix}$ | refração em lente fina ($f>0$ se a lente for convexa) | $\begin{pmatrix}1 & 0\\0 & 1\end{pmatrix}$ | reflexão em interface plano |
| $\frac{1}{\sqrt{2}}\begin{pmatrix}1 & -1\\1 & 1\end{pmatrix}$ | "beam splitter" | $\begin{pmatrix}1 & 0\\-\frac{2}{R_{e}} & 1\end{pmatrix}$ | reflexão em interface curvo <br>(com $R_e=R\cos\theta$ o raio de curvatura <br>efetivo num plano tangencial) |

## 2.4 - Telescópio
![[sistema 2 lentes ocular.png|500]]
$f_{o}$ é a distância focal da objetiva (amplifica objeto) e $f_{e}$ a distância focal da ocular. Temos a magnificação angular: $m_{A}=- \frac{f_{o}}{f_{e}}$. Se a objetiva estiver  a $>2f_{e}$ temos $|m_{T}|<1$ mesmo que $m_{A}\gg1$
Sendo $A_{o1}$ a distância olho-ocular, $f_{1}$ a distância focal da ocular, $f_{2}$ a da objetiva. As lentes estão distâncias em $d$. Então a distância entre a objetiva e o objeto será:
$$A_{o2}=\frac{f_{2}d-\frac{f_{2}A_{o1}f_{1}}{A_{o1}-f_{1}}}{d-f_{2}-\frac{A_{o1}f_{1}}{A_{o1}-f_{1}}}$$

## 3 - Ótica Ondulatória
### 3.1 - Polarização
**Linear** : $$\vec{E}(\vec{r},t)=E_{0}\sin(kz-\omega t+\phi)\vec{u} \quad \quad;\quad \quad E_{0}=\sqrt{E_{x0}^{2}+E_{y0}^{2}} \quad,\quad \vec{u}=\frac{E_{x0}\vec{u_{x}}+E_{y0}\vec{u_{y}}}{E_{0}}$$
**Circular** : $$\vec E_x(\vec r,t) = E_0\sin(kz-\omega t +\varphi)\vec u_x \quad;\quad\vec E_y (\vec r,t) = E_0 \sin\left(kz-\omega t+ \left(n+\frac12\right)\pi\right) \vec u_y$$
vemos se tem polarização direita ou esquerda ao apontar o polegar para a fonte ($-\vec{u}$)

**Elíptica** : 
$$ \begin{align*} \textbf E_x(\textbf r,t) &= E_{x0}\sin(kz-\omega t )\textbf u_x \\[10pt] \textbf E_y(\textbf r,t) &= E_{y0}\sin(kz-\omega t + \psi)\textbf u_y \end{align*} $$
em que temos
$$ \left(\frac{E_y}{E_{0y}}\right)^2 + \left(\frac{E_x}{E_{0x}}\right)^2 - 2\left(\frac{E_x}{E_{0x}}\right)\left(\frac{E_y}{E_{0y}}\right)\cos\psi = \sin^2\psi \quad\quad;\quad\quad \tan2\alpha = \frac{2E_{0x}E_{0y}\cos\psi}{E_{0x}^2 -E_{0y}^2} $$

**Quirilidade** : $\kappa=\frac{c\Delta t}{2d}$

#### 3.2 - Vetor de Jones
$$\vec{J}=\begin{bmatrix}\frac{E_{x0}}{E_{0}}\exp(i\phi_{x})\\ \frac{E_{y0}}{E_{0}}\exp(i\phi_{y})\end{bmatrix}$$

| Polarização | Matriz | Polarização | Matriz |
| ---- | ---- | ---- | ---- |
| Linear Horizontal | $\begin{pmatrix}1 \\0\end{pmatrix}$ | Linear Vertical | $\begin{pmatrix}0\\1\end{pmatrix}$ |
| Linear +45º | $\frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}$ | Linear -45º | $\frac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}$ |
| Circular Direita | $\frac{1}{\sqrt2}\begin{pmatrix}1\\-i\end{pmatrix}$ | Circular Esquerda | $\frac{1}{\sqrt2}\begin{pmatrix}1\\i\end{pmatrix}$ |
e temos $\vec{E}=E_{0}\vec{J}\exp[i(kz-\omega t)]$

$$\vec{J}=\begin{pmatrix}e^{i\phi_{x}} & 0\\0 & e^{i\phi_{y}}\end{pmatrix}$$

| Polarização | Matriz | Polarização | Matriz |
| ---- | ---- | ---- | ---- |
| Linear Horizontal | $\begin{pmatrix}1  & 0\\0 & 0\end{pmatrix}$ | Linear Vertical | $\begin{pmatrix}0 & 0\\0 & 1\end{pmatrix}$ |
| Linear +45º | $\frac{1}{2}\begin{pmatrix}1 & 1\\1 & 1\end{pmatrix}$ | Linear -45º | $\frac{1}{2}\begin{pmatrix}1 & -1\\-1 & 1\end{pmatrix}$ |
| Placa de quarto de onda com eixo rápido vertical | $e^{i\pi/4}\begin{pmatrix}1 & 0\\0 & -i\end{pmatrix}$ | Placa de quarto de onda com eixo rápido horizontal | $e^{i\pi/4}\begin{pmatrix}1 & 0\\0 & i\end{pmatrix}$ |

### 3.3 - Polarizadores
**Lei de Malus** : $I(\theta)=I(0)\cos^{2}\theta$ com $\theta$ a ser o ângulo entre analisador e polarizador

### 3.4 - Modos Espaciais
**Onda Plana** : $\vec{k}\cdot\vec{r}=\text{constante}~~,~~\phi(\vec{r},t)=\phi_0 \exp[i(\textbf k \cdot \textbf r - \omega t +\theta)]$ 
**Onda Esférica** : $kr=\text{constante}~~,~~\phi(\vec{r},t)=\frac{A_0}{r}\exp[i(kr - \omega t + \theta)]$
**Onda Cilíndrica** : $\mu^2\phi + \partial_z^2\phi - c^{-2}\partial_t^2 \phi = 0 ~~,~~ \phi(\rho,z,t)=\varphi(\rho)\exp[i(\beta z-\omega t + \varphi_0)]$
em que
    - $\mu^2 + c^{-2}\omega^2 >0$, $\beta$ toma um valor real e a solução corresponde a ondas que se propagam ao longo do eixo $zz'$.
    - $\mu^2 + c^{-2}\omega^2 <0$, $\beta$ toma uma valor imaginário e a solução corresponde a ondas evanescentes.
    - $\mu^2 > c^{-2}\omega^2$ e $\beta = 0$, obtém-se ondas que correspondem a uma onda emitida no eixo $zz'$ e que se propaga para fora segundo a direção radial e perpendicular a $zz'$.

### 3.5 - Feixe Gaussiano
$$u(\vec r) = \frac{\omega_0}{\omega(z)} \exp\left[-\frac{r^2}{\omega^2(z)}\right]\exp\left[ikz+ik\frac{r^2}{2R(z)} + i\phi(z)\right]$$
onde $\omega_0$ é a largura do feixe, $\omega(z)$ é o tamanho da cintura e $R(z)$ o raio de curvatura dados por
$\omega(z) = \sqrt{1 + \left(\frac{z}{z_R}\right)^{2} \quad}\quad;\quad \quad R(z) = z\left[1+ \left(\frac{z}{z_R}\right)\right]$
Temos ainda $z_{R}=\frac{\pi\omega_{0}^{2}}{\lambda}~~,~~\nabla^{2}u(r)=-k^{2}u(r)~,~k^{2}=\frac{\varepsilon_{r}\omega^{2}}{c^{2}}$

### 3.6 - Onda Estacionária
$$\vec E(\textbf r,t) = 2\vec E_0 \sin(kx)\cos(\omega t$$
### 3.7 - Onda Guiada
$$\vec E(\textbf r,t) = 2 \vec E_0 \sin(k_xx)\sin(k_yy)\sin(k_zz)\cos(\omega t)$$
**Velocidade de Fase** : $v_f = \frac\omega{k_\perp} = c\frac k{k_\perp} =c\sqrt{\frac{k^2_\perp + \frac{n^2\pi^2}{L_x^2}}{k^2_\perp}}$
**Velocidade de Grupo** : $v_g = \frac{\partial\omega}{\partial k_\perp} = \frac{k_\perp}{\omega}v_f^2 = c\frac{k_\perp}{k}<c$
temos que: $v_f \cdot v_g = c^2$

**Frequência de corte** : $\omega\ge \omega_{c}=\frac{cn\pi}{L_{x}}$ 
**Interferência** : $\bar I_{12}(\vec r,t) = \frac{c\varepsilon_0}2 \vec E_{01}\cdot \vec E_{02}\cos[(\vec k_1 - \vec k_2) \cdot \vec r + \varphi_1 - \varphi_2]$
**Coerência Temporal** : $\bar I(\tau) = \frac{\varepsilon_0c}{2}\langle E(t)E(t)\rangle = \frac{\varepsilon_0c}{2}E_0^2[1-\cos(\omega\tau)]$
**Contraste** : $c = \frac{I_{\text{máx}} - I_{\text{mín}}}{I_{\text{máx}} + I_{\text{mín}}}$

### 3.8 - Interferómetros
#### Dupla Fenda
$\delta = k(r_1 - r_2) = kb\sin\theta ~~~~;~~ n\in\mathbb{Z}$
    - interferência construtiva quando $\delta = 2\pi n$ ou $r_1 - r_2 = n\lambda$.
    - interferência destrutiva quando $\delta = \pi(2 n +1)$ ou $r_1- r_2 = (2n+1)\lambda/2$.

#### Michelson
$N = 2\frac{\Delta l}{\lambda}$

#### Fabri-Perot
$E_s = \frac{t^2}{1-r^2e^{ik2L}}e^{ikL}E_{e}\quad\quad;\quad\quad\bar I_s = \Big\vert \frac{t^2}{1-r^2e^{ik2L}}\Big\vert^2 \bar I_e = \frac1{1 + K\sin^2(kL)}\bar I_e$
em que $K$ é o coeficiente de finesse: $K=\left(\frac{2r}{1-r^{2}}\right)^{2}$

## 4 - Ótica Difrativa
### 4.1 - Difração 1 fenda
$$I(\theta)=I_{0}\left(\frac{\sin u}{u}\right)^{2} \quad \quad;\quad \quad u=\frac{\pi b\sin\theta}{\lambda}$$
com mínimos em $u=n\pi\to b\sin\theta=n\lambda$ e máximos em $u\simeq(2n+1)\frac{\pi}{2}\to b\sin\theta\simeq (2n+1)\frac{\lambda}{2}$
Temos ainda um poder resolutivo (ângulo mínimo entre raios emitidos por 2 fontes distantes, de forma que os padrões sejam distinguíveis): $\phi=\frac{\lambda}{b}$

### 4.2 - Difração por 2 fendas
$$E(\theta)=2E_{0}\cos(v)\frac{\sin(u)}{u}$$
com $v=\frac{1}{2}ka\sin\theta=\frac{1}{\lambda}\pi a\sin\theta$
$$I(\theta)=I_{0}\left(\cos(v)\frac{\sin(u)}{u}\right)^{2}$$
com poder resolutivo $R=Nn$ e dispersão $D=\frac{n}{b\cos\theta}$ com $v=n\pi$ nos máximos e $v=\frac{\pi}{2}(2n+1)$ nos mínimos

### 4.3 - Rede de difração (N fendas)
$$I(\theta) = I_0\left(\frac{\sin (Nv)}{\sin v}\frac{\sin u }{u}\right)^2$$

### 4.4 - Outros
**Cristal** - $\Delta\phi = \frac{4\pi d\sin\theta}{\lambda}$
**Lei de Babinet** - $\Delta \phi = \frac{2\pi}{\lambda}(n_e-n_o)\Delta \ell$ 

### 4.5 - Integral difração Kirchhoff
$$\begin{align*}E(x',y',z') = \frac1{i\lambda} \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}E(x,y,z)\frac1R\exp(ikR)\cos(\vec n,\vec R)\,dx\,dy\end{align*}$$
com $\vec{R}=(x-x',y-y',z-z')~~,~~\cos(\vec{n},\vec{R})=\frac{\vec{n}\cdot\vec{R}}{|\vec{n}||\vec{R}|}$
#### Fresnel
Assumimos $\cos(\vec n,\vec R)\approx 1$
$$\begin{align*} E(x',y',z') \approx& \frac1{i\lambda}\int\int E(x,y,z)\frac1{z-z'}\exp[ik(z-z')]\exp\left(ik\frac{(x-x')^2 + (y-y')^2}{2(z-z')}\right)dxdy \end{align*}$$

#### Fraunhofer
Assumimos ${\lambda}(x^2+ y^2) \ll z-z'~~\to~~\exp\left[ik\frac{x^2 + y^2}{2(z-z')}\right] \approx 1$
$$E(x',y',z') \approx \frac1{i\lambda}\frac1{(z-z')}\exp[ik(z-z')]\exp\left(ik\frac{(x')^2 + (y')^2}{2(z-z')}\right)\iint E(x,y,z)\exp\left[-ik\frac{xx'+yy'}{(z-z')}\right] dxdy$$

## 5 - Ótica de Fourier

$$ \begin{align*} \bar I(x',y',z') &= \varepsilon_0c^2 |E(x',y',z')|^2 \\[15pt] &= \frac{\varepsilon_0c^2}{\lambda^2(z-z')}\left| \mathcal F_y \left[\mathcal F_x[E(x,y,z)] \left[\frac{kx'}{(z-z')}\right]\right]\left[\frac{ky'}{(z-z')}\right] \right|^2 \end{align*} $$

**Onda Plana**
$\tau(x)=1 \quad;\quad\bar I(x',z') \propto |E_0\delta(x')|^2$

**Fenda Infinitesimal**
$\tau(x) = \delta(x)\quad;\quad \bar I(x',z') \propto |E_0|^2$

**Fenda Finita**
$\tau (x) = \begin{cases} 1 \quad \text{para }|x|<a \\[5pt] 0 \quad \text{caso contrário} \end{cases} \quad;\quad \bar I(x',z') \propto \left| E_0 2 \frac{\sin\left(\frac{kx'}{z'}a\right)}{x'}\right|^2$

**Dupla fenda**
$\tau(x) = \delta\left(x-\frac d2\right) + \delta\left(x+\frac d2\right) \quad;\quad \bar I(x',z') \propto\left|2\cos\left(\frac{kx'}{2z'}d\right)E_0\right|^2$

### 5.1 - Filtragem
**Passa Baixo** : $\tau(x)=\delta(x)$ - suaviza o perfil de intensidade do feixe, remove deformações ou imperfeições 
**Passa Alto** : $\tau(x)=1-\delta(x)$ - deixa a imagem muito escura. Só se vê as zonas com maior variação da intensidade
**Fase** : $\tau(x)=\Theta(x)$ - equivale a retirar da imagem de uma intensidade que é proporcional ao gradiente de fase segunda a direção do semi-plano rejeitado. 