###### Aula 15 - 18/4/2024 (dada por EVC)
**Energias Bloch**
- Vimos que o teorema de Bloch nos diz: se o potencial é periódico, numa rede de Bravais, a ESIT tem soluções do tipo *onda plana*: $\Psi_{\vec{k}}(\vec{r})=e^{i \vec{k}\cdot\vec{r}}e_{\vec{k}}(\vec{r})$
- No entanto, o teorema não nos dá os *valores próprios* do Hamiltoniano AKA as energias $E_{\vec{k}}$.

## Modelo dos Eletrões Quase Livres (Perturbação)
- Consideremos os eletrões sujeitos a um potencial:
$$\hat{H}=\hat{H_{0}}+\hat{V}$$
em que $\hat{H_{0}}$ é o Hamiltoniano de um eletrão livre (Hamiltoniano do Sommerfeld) e $\hat{V}$ é uma perturbação, tal que:
$$\langle \hat{V}\rangle\ll E_{\vec{k}}^{(0)} $$
(o $^{(0)}$ indica que são as energias do eletrão não perturbado, $\hat{H_{0}}$)

- Desta forma, vemos que $$\hat{H_{0}}=\frac{\hat{\vec{P}}}{2m}~~\to~~ \hat{H_{0}}\ket{\vec{k}}=\frac{\hbar^{2}k^{2}}{2m}\ket{\vec{k}}=E_{\vec{k}}^{(0)}\ket{\vec{k}}$$
- Usando esta notação, temos 
$$\psi_{\vec{k}}^{(0)}=\langle\vec{r}|\vec{k}\rangle=\frac{1}{\sqrt{v}}e^{i \vec{k}\cdot\vec{r}}$$
- Como fazíamos em MQ1 (lol) dividimos o problema em 2 partes: não degenerada e degenerada

### 1 - Caso não degenerado (2ª ordem)
- Para a perturbação em 2ª ordem (deduzida em MQ1) podemos escrever:
$$E_{\vec{k}}=E_{\vec{k}}^{(0)} + \bra{\vec{k}}\hat{V}\ket{\vec{k}}+\sum\limits_{\vec{k'}\neq \vec{k}}\frac{|\bra{\vec{k}}\hat{V}\ket{\vec{k'}}|^{2}}{E_{\vec{k}}^{(0)} - E_{\vec{k'}}^{(0)}}$$
- Ora, o termo $\bra{\vec{k}}\hat{V}\ket{\vec{k'}}$ simplesmente é a *transformada de Fourier* do potencial. E podemos escrever:
$$\bra{\vec{k}}\hat{V}\ket{\vec{k'}}=V_{\vec{k}-\vec{k'}}=\delta_{\vec{k}-\vec{k'},\vec{K}}V_{\vec{K}}$$
ou seja, isto é basicamente o *critério de Von Laue*! Esta matriz de $\hat{V}$ só tem elementos não nulos quando $\vec{k}-\vec{k'}$ correspondem a vetores do espaço recíproco AKA picos de Bragg AKA quando ocorre difração por raios X.
    - Além disso, como temos $\vec{K}=\vec{k}-\vec{k'}~\to~ \vec{k'}=\vec{k}-\vec{K}$. Ora, na equação temos $k$ constante. Podemos então escrever a soma em $\vec{k'}$s como uma soma em $\vec{K}$s.
- Podemos então definir a FT do potencial / perturbação:
$$V_{\vec{K}}=\int d\vec{x} e^{-i \vec{K}\cdot\vec{x}}V(\vec{x})$$
- Temos ainda que o termo da diagonal $\bra{\vec{k}}\hat{V}\ket{\vec{k}}$ é uma constante $V_{0}$
- Vamos então tentar simplificar a equação de teoria de perturbações de 2º ordem:
$$E_{\vec{k}}= E_{\vec{k}}^{(0)}+V_{0}+\sum\limits_\vec{K}\frac{|V_{\vec{K}}|^{2}}{E_{\vec{k}}^{(0)}- E_{\vec{k}-\vec{K}}^{(0)}}$$
    - Em que $V_{0}$ é a *correção de 1ª ordem*, que é constante.
    - Na *correção de 2ª ordem* temos termos para os valores de $K$ (ora, como vimos na aula anterior, podemos mudar de banda somando e subtraindo $\vec{K}$ a $\vec{k}$). Ou seja, dá para prever que iremos ter **repulsão de bandas**! 

**1ª Zona Brillouin**
- Consideremos agora apenas $\vec{k}\in \text{1ZB}$ (k na primeira zona brillouin)
- Isto implica que $\vec{k}+\vec{K}$ está noutras zonas
- Se traçarmos $E_{\vec{k}}(\vec{k})$ temos uma parábola, porque $E_{\vec{k}}^{(0)}=\frac{\hbar^{2}k^{2}}{2m}$

- Podemos escolher um ponto dentro da 1ZB, sendo que um ponto resultante de uma translação em $\vec{K}$ fica na 2ZB. Ora, deveríamos ter a mesma energia devido à periodicidade do sistema. Mas não é esse o caso:
    - Vemos que ao passar para outra zona de Brillouin de um cristal (aumentar $k$), a energia aumenta bastante já que segue a parábola $\propto k^{2}$
- Isto não significa que o teorema de Bloch está errado.
- Isto apenas mostra que até aqui ignoramos um 2º número quântico: $n$

**Agora com n**
- Como já vimos:
$$\Psi_{\vec{k},n}(\vec{r})=e^{i \vec{k}\cdot\vec{r}}u_{\vec{k},n}(\vec{r})$$
com energia $E_{\vec{k},n}$ em que $n$ é a **banda**!

- Assim, da teoria de perturgações temos:
$$V\to0~~:~~~~~~ E_{\vec{k},n}\Leftrightarrow E^{(0)}_{\vec{k}-\vec{K}}$$
(em que a seta para os 2 lados indica que haverá uma correspondência entre as energias)
- Isto significa que, quando $V\to0$ as teorias de Bloch e dos eletrões livres *têm que ser compatíveis*!
- Ou seja, em 1D isto dá:
$$E_{k,n}\Leftrightarrow E_{k\pm \frac{2\pi}{a}m}~~~~;~~ m,n\in\mathbb{Z}$$

- Assim, se $n=1$ corresponder à 1ZB temos: $E_{\vec{k},1}=E_{\vec{k}}^{(0)}$. Assim: $n=1 \Leftrightarrow m=0$
- Temos então o **Esquema de Zona Estendida**:
![[energias bloch sem perturbações.png|700]]
fazemos translação de todas as ZB para ficarem contidas dentro da 1ZB, usando $\pm 2\pi/a~,~\pm 4\pi/a~,~\dots$ (mais genericamente: $\pm\vec{K},\pm2\vec{K},\dots$)
- Podemos então pensar em $n$ como sendo a banda (zona Brillouin) em que estamos inicialmente e $m$ (que será par) a translação que temos que fazer para a mover para a 1ZB.
- Podemos ainda notar que "cada $n$ está associado a 2 bandas", ou seja, se $n=2$ temos a banda 2ZB positiva e negativa. Isto não se aplica para 1ZB, já que esta não se encontra dividida (Vimos isto no caso 2D quando definimos zonas de Brillouin há umas aulas)
- Por fim, temos o **efeito de repulsão entre bandas** que faz com que a banda $n=1$ baixe um pouco, a $n=2$ suba um pouco e todas as bandas acima subam. Quando maior $n$ mais sobe a banda. Isto pode ser mostrado usando a teoria de perturbações degenerada: o somatório de $\vec{K}$s irá diminuir a energia corrigida da banda 1 ($\vec{k}<\vec{K}$) e aumentar as restantes ($\vec{k}>\vec{K}$).

### 2 - Caso Degenerado (1ª Ordem)
- Ora, no que vimos acima, podemos usar a teoria de perturbações para corrigir as energias. Mas isto não se aplica nos pontos em que as bandas se tocam, porque aí temos degenerescência! 
- Isto porque neste pontos teremos $E_{\vec{k}}^{(0)}\simeq E_{\vec{k}\pm \vec{K}}^{(0)}$ logo o termo $\sum\limits_\vec{K}\frac{|V_{\vec{K}}|^{2}}{E_{\vec{k}}^{(0)}- E_{\vec{k}-\vec{K}}^{(0)}}$ da teoria de perturbações explode e a teoria deixa de funcionar corretamente.
- Ou seja, temos 2 estados a intersetarem-se. Para dimensões superiores teremos interseções de mais de 2 estados.
- Assim, a forma como evitamos este problema é: *diagonalizamos a perturbação no subespaço degenerado*.

**EX**
- Consideremos o espaço degenerado com dimensão $\dim=2$
- Definimos $\vec{k'}-\vec{K}=\vec{k}$
- Temos:
$$\begin{align*}
\bra{\vec{k}}\hat{H}\ket{\vec{k}}&= E_{\vec{k}}^{(0)}+V_{0}=\varepsilon_{0}(\vec{k})\\
\bra{\vec{k'}}\hat{H}\ket{\vec{k'}}&= E_{\vec{k'}}^{(0)}+V_{0}=\varepsilon_{0}(\vec{k'})=\varepsilon_{0}(\vec{k}+\vec{K})\\
\bra{\vec{k}}\hat{H}\ket{\vec{k'}}&= V_{\vec{k}-\vec{k'}}=V_{\vec{K}}^{*}\\
\bra{\vec{k'}}\hat{H}\ket{\vec{k}}&= V_{\vec{k}-\vec{k'}}^{*}=V_{\vec{K}}\\
\end{align*}$$
- Ou seja:
$$\begin{pmatrix}\varepsilon_{0}(\vec{k}) & V_{\vec{K}}^{*}\\ V_{\vec{K}}& \varepsilon_{0}(\vec{k}+\vec{K})\end{pmatrix} \begin{pmatrix}\alpha\\ \beta\end{pmatrix}=E_{\vec{k}}\begin{pmatrix}\alpha\\\beta\end{pmatrix}$$
isto permite obter:
$$\ket{\psi_{k}}=\alpha\ket{\vec{k}} + \beta \ket{\vec{k'}}=\alpha\ket{\vec{k}} + \beta \ket{\vec{k}+\vec{K}}$$
e temos a equação
$$\begin{align*}
\left[\varepsilon_{0}(\vec{k})-E_{\vec{k}}\right]\left[\varepsilon_{0}(\vec{k}+\vec{K})-E_{\vec{k}}\right]- |V_{\vec{K}}|^{2}=0\\
\end{align*}$$

- No caso específico em que temos um ponto $\vec{k}$ na fronteira da ZB teremos: $\vec{k'}=\vec{k}+\vec{K}$, logo $\varepsilon_{0}(\vec{k})=\varepsilon_{0}(\vec{k}+\vec{K})$ e da equação acima resulta:
$$E_{\vec{k}}=\varepsilon_{0}(\vec{k})\pm |V_\vec{K}|$$
- Ora, isto vai fazer com que nos pontos de junção (por exemplo entre $n=1,2$) a linha de cima ($n=2$) sobe e a linha de baixo ($n=1$) desce. Surge então uma **gap** entre os níveis, ou seja, uma regiãp de energia que não é permitida!!
- Se considerarmos k's perto da fronteira da ZB iremos obter coisas similares, mas mais fracas. Deste modo, a teoria de perturbações irá resultar num traçado mais suave, em que as secções "achatam" junto das fronteiras de ZBs:
![[energias bloch.png|625]]    ![[gap energias.png|225]]
- Se um lado da fronteira de ZB sobe $|V_{\vec{K}}|$ e o outro desce, então temos:
$$\text{Gap}=2|V_{\vec{K}}|$$
- Em 2D e 3D a Gap nem sempre existe.

### EX
- Consideremos $V(x)=V_{0}\cos\left(\frac{2\pi x}{a}\right)~~,~~V_{0}>0$
- As fronteiras de ZB1 encontram-se em $k=\pi/a,k'=-\pi/a$ tal que $k'-k=K=-2\pi/a$ e $E_{k}^{(0)}=E_{k'}^{(0)}$
- Podemos então definir:
$$\ket{\psi_{\pm}}=\frac{1}{\sqrt{2}}(\ket{k}\pm \ket{k'}) \Leftrightarrow E_{\pm}$$
- Assim, pelo teorema de Block (?):
$$\begin{align*}
\psi_{+}\sim e^{ix\pi/a}+e^{-ix\pi/a}\propto \cos(x\pi/a)\\
\psi_{-}\sim e^{ix\pi/a}-e^{-ix\pi/a}\propto \sin(x\pi/a)
\end{align*}$$
ou seja, temos:
![[Pasted image 20240603215118.png|267]]
- Consideremos agora que temos 2 pontos perto das fronteiras de 2 bandas: $k=n\pi/a+\delta~,~k'=-n\pi/a+\delta$. A equação caraterística fica:
$$E_{\pm}=\frac{\hbar^{2}(n\pi/a)^{2}}{2m}\pm|V_{\vec{K}}| + \frac{\hbar^{2}\delta^{2}}{2m} \left[1\pm \frac{\hbar^{2}(n\pi/a)^{2}}{m} \frac{1}{|V_{\vec{K}}|} \right]$$