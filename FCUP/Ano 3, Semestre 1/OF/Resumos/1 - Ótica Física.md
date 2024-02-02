## 1.1 - Equações de Maxwell
$$\boxed{\begin{align*}
\nabla \cdot \vec{E}&= \frac{\rho}{\varepsilon_{0}} &&&& \textsf{(Lei de Gauss)} \\
\nabla \cdot \vec{B}&= 0 &&&& \textsf{(Sem nome)}\\
\nabla \times \vec{E}&= -\partial_{t}\vec{B} &&&& \textsf{(Lei de Faraday)}\\
\nabla \times \vec{E}&= \mu_{0}\vec{\mathcal{J}}+ \mu_{0}\varepsilon_{0}\vec{E} &&&& \textsf{(Lei de Ampere-Maxwell)}
\end{align*}}$$

## 1.2 - Ondas EM
- Ondas EM consistem um grupo específico de soluções das equações de Maxwell.
- Como tal, podemos definir a equação de onda para ondas EM (para dedução, vê os resumos de EM2):
$$\nabla^{2}\vec{E}= \mu_{0}\varepsilon_{0}\partial_{t}^{2}\vec{E} \quad \quad;\quad \quad \nabla^{2}\vec{B}= \mu_{0}\varepsilon_{0}\partial_{t}^{2}\vec{B}$$
(sendo que na maioria dos casos ignoramos o campo magnético, porque ele só se torna importante em comparação com $E$ para partículas a mover-se com $v\sim c$)

- Comparando estas equações com a equação de onda que vimos atrás, temos que as ondas EM se movem à velocidade da luz:
$$c=\frac{1}{\sqrt{\varepsilon_{0}\mu_{0}}}$$

- Facilmente vemos que a equação de onda do campo elétrico tem solução do tipo:
$$\vec{E}(\vec{r},t)=\vec{E_{0}}\sin(\vec{k}\cdot\vec{r}-\omega t-\phi_{0})$$
(sendo $\vec{k}$ o vetor de onda, que aponta na direção em que a onda se propaga)
- Podemos definir:
$$\omega=ck \quad \quad;\quad \quad \lambda=cT$$
- Para o campo magnético temos:
$$\vec{B}(\vec{r},t)=\vec{B_{0}}\sin(\vec{k}\cdot\vec{r}-\omega t+\phi_{0})$$
em que $$\vec{B_{0}}=\frac{\vec{k}\times\vec{E_{0}}}{\omega}$$
(dedução nos resumos de EM2)
- Este último resultado mostra que os campos elétrico e magnético são interdependentes.

### 1.2.1 - Frente de Onda
- Podemos definir uma frente de onda como sendo um conjunto de pontos que têm a mesma fase, ou seja:
$$\vec{k}\cdot\vec{r}-\omega t+\phi_{0}=\phi$$
- Podemos decompor o vetor $\vec{r}$ nas componentes perpendicular e paralela ao vetor de onda: $\vec{r}=\vec{r_{\perp}}+\vec{r_{\parallel}}$ .
- Temos portanto que $\vec{k}\cdot\vec{r}=\vec{k}\cdot\vec{r_{\parallel}}=kr_{\parallel}$
- E fica:
$$r_{\parallel}=\frac{1}{k}(\omega t-(\phi_{0}-\phi))$$
e podemos obter o vetor:
$$\begin{align*}
\vec{r_{\parallel}}&= \frac{1}{k^{2}} (\omega t-(\phi_{0}-\phi))\vec{k}\\
&= \frac{\omega t}{k^{2}}\vec{k} + \frac{\phi-\phi_{0}}{k^{2}}\vec{k}
\end{align*}$$

- Sendo que a frente de onda se move com velocidade:
$$\vec{v}=\frac{\omega}{k^{2}}\vec{k}$$
- Assim podemos escrever:
$$\begin{align*}
\vec{r}(t)&= \vec{r_{\perp}}+\vec{r_{\parallel}}\\
&= \vec{r_{\perp}} + \vec{v}t + \vec{r'_{\parallel}}
\end{align*}$$
em que definimos: $\vec{r_{\parallel}}=\vec{v}t-\vec{r'_{\parallel}}$ com $\vec{r'_{\parallel}}=\frac{\phi-\phi_{0}}{k^{2}}\vec{k}$.

### 1.2.2 - Princípio de Sobreposição
- Este princípio vem diretamente de a equação de onda ser linear, pelo que nos diz que se a soma de 2 soluções é solução.
- **Interferência** - Quando a sobreposição de 2 ondas gera uma nova onda.

#### Ondas Coerentes
- Ondas em que a diferença de fase é constante e bem definida.
- Consideremos 2 ondas planas monocromáticas.
$$\begin{align*}
\vec{E_{1}}(x,t)=\vec{E_{0}}\sin(kx-\omega t+\phi_{1})\\
\vec{E_{2}}(x,t)=\vec{E_{0}}\sin(kx-\omega t+\phi_{2})
\end{align*}$$
- Consideremos que elas se sobrepõe. A onda resultante será:
$$\begin{align*}
\vec{E}(x,t)&= \vec{E_{1}}(x,t)+\vec{E_{2}}(x,t)\\
&= \vec{E_{0}}\sin(kx-\omega t+\phi_{1}) + \vec{E_{0}}\sin(kx-\omega t+\phi_{2})\\
&= \vec{E_{0}}[\sin(kx-\omega t+\phi_{1})+\sin(kx-\omega t+\phi_{2})]\\
\end{align*}$$
- Temos:
$$\begin{align*}
\sin (a+b)=\sin a\cos b+\cos a\sin b\\
\sin (a-b)=\sin a\cos b-\cos a\sin b
\end{align*}$$
logo podemos somar as 2 equações e temos:
$$\sin(a+b)+\sin(a-b)=2\sin a\cos b$$
- Podemos ainda definir:
$$A=a+b=kx-\omega t+\phi_{1} \quad \quad;\quad \quad B=a-b=kx-\omega t+\phi_{2}$$
- Logo:
$$\sin A+\sin B=2\sin \frac{A+B}{2}\cos \frac{A-B}{2}$$
- Ou seja, o campo que descreve a onda resultante da sobreposição é:
$$\boxed{\vec{E}(x,t)=2\vec{E_{0}}\cos\left(\frac{\phi_{1}-\phi_{2}}{2}\right)\sin\left(kx-\omega t+\frac{\phi_{1}+\phi_{2}}{2}\right)}$$

#### Ondas Incoerentes
- Continuamos a considerar que as ondas têm a mesma frequência $\omega$ e amplitude $\vec{E_{0}}$.
- Podemos ter ondas em que a diferença de fase não está bem definida, pelo que esta pode ser considerada um variável aleatória:
$$\delta\phi\equiv \phi_{2}-\phi_{1}$$
- E podemos definir o valor esparado da amplitude da onda resultante:
$$\overline{\vec{E}}(x,t)=\int_{-\pi}^{+\pi}p(\delta\phi)2\vec{E_{0}}\cos\left(\frac{\delta\phi}{2}\right)\sin\left(kx-\omega t+\phi_{1}+\frac{\delta\phi}{2}\right)$$
em que assumimos que a fase tem distribuição uniforme:
$$p(\delta\phi)=\begin{cases}
\frac{1}{2\Delta\phi} &  & ; &  & |\delta\phi-\delta\phi_{0}|<\Delta\phi \\
0 &  & ; &  & \text{caso contrário}
\end{cases}$$

- Na prática, este valor esperado consiste no valor médio que um instrumento mediria ao medir a amplitude da onda (porque estes fazem uma média ao longo de um tempo de aquisição)

## 1.3 - Impulsos e Feixes
- As ondas planas e monocromáticas (harmónicas - senos e cossenos) são apenas approximaçõpes da realidade.
- Em laboratório são tipicamente gerados feixes e impulsos de luz.

### 1.3.1 - Feixes
- Feixes consistem em ondas em que a energia está concentrada em torno do eixo de propagação. (Nas ondas planas a energia está igualmente distribuída)
- Estes são descritos pelo seguinte campo:
$$\textbf E(\textbf r,t) = \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty} \exp\left(-\frac{\vec k^2_\perp}{2\Delta k^2_\perp}\right)\vec E_0 \exp[i(\vec k\cdot \vec r- \omega t)]dk^2_\perp$$
- Temos então que (na componente perpendicular ao deslocamento) a amplitude segue uma distribuição normal. Assim, na equação acima:
    - $\Delta k_{\perp}^{2}$ está relacionada com a largura da distrbiuição, quando menor mais estreita é a distribuição (relacionado ao desvio padrão).
    - integramos em $dk^{2}_{\perp}$ para considerar todas as direções possíveis no plano perpendicular à propagação.

- Usando as propriedades da transformada de Fourier podemos (não sei como) obter:
$$\vec{E}(\vec{r},t)=\vec{A}(\vec{r_{\parallel}})\exp\left(-\frac{\Delta k_{\perp}^{2}\vec{r_{\perp}^{2}}}{1+\frac{\vec{r_{\perp}^{2}}c^{2}}{2\omega^{2}}}\right) \exp(i\phi(\vec{r_{\parallel}}))$$
em que $\vec{A}(\vec{r_{\parallel}}),\phi(\vec{r_{\parallel}})$ são funções que nos dão a amplitude.

- Podemos reescrever isto com $\vec{E}(\vec{r},t)=\vec{A}(\vec{r_{\parallel}})\exp\left(-\frac{\vec{r_{\perp}^{2}}}{\Delta r_{\perp}^{2}}\right) \exp(i\phi(\vec{r_{\parallel}}))$ em que $\Delta r_{\perp}=\sqrt{\frac{1+ \frac{\vec r^2_{||}c^2}{4\omega^2}}{\Delta k_\perp^2}}$.
- Temos então 1 termo com uma exponencial real que indica que a onda desparece para $r_{\perp}$ suficientemente alto. Temos ainda o termo com a exponencial complexa que descreve a oscilação da onda na direção de propagação $r_{\parallel}$

### 1.3.2 - Impulsos
- Enquanto que um feixe está restrito na direção normal à propagação (como se fosse restrita a um cilindro centrado no eixo de propagação). Um impulso consiste em vários "picos" de luz curtos seguidos com espaçamento.
- Descritos pelo campo:
$$\vec E(\vec r,t) = \vec E_0 \exp\left[-\left(\frac{\vec r-\vec vt}{\Delta r_{||}}\right)\right]\exp[i(\vec k_0\cdot\vec r - \omega _0t)]$$
em que na prática os feixes laboratoriais contêm restrições na direção transversal.

## 1.4 - Simetrias e Conservação
- Um sistema ter uma certa simetria significa que se fizermos uma transformação associada à simetria, as propriedades do sistema ficam iguais. Por exemplo, num sistema de simetria no espaço, podemos fazer uma translação e o sistema não muda.

**Tipos de Simetria**
- *Simetrias Contínuas* - relacionadas com transformações infinitamente pequenas (como translação no espaço ou tempo)
- *Simetrias Contínuas* - relacionadas com transformações não contínuas (reflexão ou inversão no tempo)

Temos ainda:
- *Simetrias Globais* - simetrias que se mantêm em todos os pontos do espaço e tempo. 
- *Simetrias Locais* - oposto da de cima. Variam.

Podemos ainda indicar simetrias comuns:
- *Reflexão no espaço* - Temos Paridade (podemos inverter os sinais das variáveis). Não podemos definir uma direita ou esquerda absoluta.
- *Reflexão no tempo* - Temos reversibilidade do tempo. Não podemos definir o sentido do tempo.
- *Translação no espaço* - Temos conservação do momento linear. Não podemos definir uma posição absoluta
- *Translação no tempo* - Temos conservação da energia. Não podemos definir tempo aboluto
- *Rotação* - Temos conservação de momento angular. Não podemos definir uma orientação absoluta.

## 1.5 - Teorema de Poynting
- O vetor de Poyting descreve o fluxo de energia por unidade de tempo e área
$\boxed{\begin{align*}\nabla \cdot \vec{E}&= \frac{\rho}{\varepsilon_{0}} &&&& \textsf{(Lei de Gauss)} \\\nabla \cdot \vec{B}&= 0 &&&& \textsf{(Sem nome)}\\\nabla \times \vec{E}&= -\partial_{t}\vec{B} &&&& \textsf{(Lei de Faraday)}\\\nabla \times \vec{E}&= \mu_{0}\vec{\mathcal{J}}+ \mu_{0}\varepsilon_{0}\vec{E} &&&& \textsf{(Lei de Ampere-Maxwell)}\end{align*}}$

- Podemos fazer produto escalar da Lei de Faraday por $\frac{\vec{B}}{\mu_{0}}$:
$$\frac{\vec{B}}{\mu_{0}}\cdot(\nabla\times\vec{E})=- \frac{\vec{B}}{\mu_{0}}\cdot \partial_{t}\vec{B}$$
e produto escalar da Lei de Ampere por $\frac{\vec{E}}{\mu_{0}}$:
$$\frac{\vec{E}}{\mu_{0}}\cdot(\nabla \times \vec{B})=\vec{E}\cdot(\vec{\mathcal{J}_{\ell}} + \partial_{t}\vec{P}) + \varepsilon_{0}\vec{E}\cdot\partial_{t}\vec{E}$$
(temos que $\vec{\mathcal{J}}=\frac{1}{\mu_{0}}(\vec{\mathcal{J}}_{\ell}+\partial_{t}\vec{P})$ ???????)

- E podemos subtrair a primeira equação à segunda:
$$\begin{align*}
\frac{\vec{E}}{\mu_{0}}(\nabla \times\vec{B})-\frac{\vec{B}}{\mu_{0}}(\nabla \times\vec{E})= \vec{E}\cdot(\vec{\mathcal{J}_{\ell}} + \partial_{t}\vec{P}) +\varepsilon_{0}\vec{E}\cdot\partial_{t}\vec{E}+ \frac{\vec{B}}{\mu_{0}}\cdot \partial_{t}\vec{B}\\
\frac{\vec{E}}{\mu_{0}}(\nabla \times\vec{B})-\frac{\vec{B}}{\mu_{0}}(\nabla \times\vec{E}) -\varepsilon_{0}\vec{E}\cdot\partial_{t}\vec{E}- \frac{\vec{B}}{\mu_{0}}\cdot \partial_{t}\vec{B}=\vec{E}\cdot(\vec{\mathcal{J}_{\ell}} + \partial_{t}\vec{P})\\
\frac{\vec{B}}{\mu_{0}}(\nabla \times\vec{E}) -\frac{\vec{E}}{\mu_{0}}(\nabla \times\vec{B})+\varepsilon_{0}\vec{E}\cdot\partial_{t}\vec{E}+ \frac{\vec{B}}{\mu_{0}}\cdot \partial_{t}\vec{B}=-\vec{E}\cdot(\vec{\mathcal{J}_{\ell}} + \partial_{t}\vec{P})
\end{align*}$$
que podemos reescrever como:
$$\nabla\cdot\left(\vec{E}\times\frac{\vec{B}}{\mu_{0}}\right)+\partial_{t}\left(\varepsilon_{0} \frac{E^{2}}{2}+ \frac{1}{\mu_{0}}\frac{B^{2}}{\mu_{0}}\right)=-\vec{E}\cdot(\vec{\mathcal{J}}_{\ell}+\partial_{t}\vec{P})$$
que podemos reescrever como o teorema de Poyting:
$$\nabla\cdot\vec{S}=-\frac{\partial u}{\partial t}=-\partial_{t}u_{\text{campo}}-\partial_{t}u_\text{meio}$$
(em que $u$ são densidades de energia)

## 1.6 - Pressão de Radiação
- Podemos definir:
$$\mathcal{P}=\frac{\vec{F}\cdot\vec{n}}{A}=\frac{\frac{d\vec{P}}{dt}\cdot\vec{n}}{A}$$
e podemos escrever a densidade de momento linear: $\vec{p}=\frac{d\vec{P}}{dV}$ em que $dV$ é o volume infinitesimal que a onda cobre num intervalo $dt$.
- Assim:
$$\frac{d\vec{P}}{dt}=\vec{p}\frac{dV}{dt}=\vec{p}cA$$
- Podemos ainda definir:
$$\vec{p}=\varepsilon_{0}\vec{E}\times\vec{B}=\frac{\vec{S}}{c^{2}}$$
- Juntando tudo temos:
$$\mathcal{P}=\frac{\vec{S}\cdot\vec{n}}{c}$$

## 1.7 - Intensidade
$$I\equiv\langle S\rangle=\frac{1}{2}c\varepsilon_{0}E_{0}^2$$

## 1.8 - Geração e deteção de luz
### 1.8.1 - Fontes Óticas
**Modelo do Dipolo Elétrico**
- Este modelo de fontes óticas consiste num dipolo cujo momento dipolar $\mu$ oscila no tempo devido ao movimento das cargas que formam o dipolo, tendo-se:
$$\vec{\mu}(t)=\vec{\mu_{0}}\sin(\omega t)$$
![[vetor poynting.png]]

**Modelo do Corpo Negro**
- O modelo do dipolo elétrico é útil na escala microscópico, mas na macroscópica não é suficientemente complexo.
- Assim, o modelo do corpo negro é usado. Este consiste numa estatística de emissão:
$$n(\varepsilon,t)=\frac{g(\varepsilon)}{e^\frac{\varepsilon}{k_{B}T}-1}$$
($\varepsilon$ é a energia de 1 fotão)

### 1.8.2 - Detetores Óticos
- Normalmente medem um sinal elétrico que é proporcional à intensidade de luz, sendo medida a energia radiante numa certa gama.
- Exemplos:
    - Células fotoemissivas - emitem eletrões quando atingidas por fotões de energia suficientemente elevada
    - Células fotocondutores - a sua resistência varia quando sujeitos à luz
    - Células fotovoltaicas - geram força eletromotriz proprocional à energia radiante recebida

## 1.9 - Ótica na matéria
### 1.9.1 - Equações de Maxwell na Matéria
$$\boxed{\begin{align*}
\nabla\cdot\vec{D}&= \rho_{\ell}\\
\nabla\cdot\vec{B}&= 0\\
\nabla\times\vec{E}&= - \partial_{t}\vec{B}\\
\nabla\times\vec{H}&= \vec{\mathcal{J}_{\ell}} + \partial_{t}\vec{D}
\end{align*}}$$
em que
$$\vec{D}=\varepsilon_{0}\vec{E}+\vec{P} \quad \quad;\quad \quad \vec{H}=\frac{1}{\mu_{0}}\vec{B}$$

### 1.9.1 - Ondas EM em meios óticos
- Consideremos um meio isotrópico, homogéneo e não condutor ($\vec{\mathcal{J}}_{\ell}=\vec{0}~,~\nabla\cdot\vec{P}=0$)
- Começemos por fazer o rotacional da equação de Faraday:
$$\begin{align*}
\nabla\times(\nabla\times\vec{E})&= \nabla\times(-\partial_{t}\vec{B})\\
\nabla(\nabla\cdot\vec{E})-\nabla^{2} \vec{E}&= \nabla\times(-\partial_{t}\vec{B})
\end{align*}$$
Em que, como $\vec{\mathcal{J}}_{\ell}=0$ temos que $\nabla(\nabla\cdot\vec{E})=\nabla\rho=0$ porque a densidade de carga terá que ser constante no espaço e tempo. 
Além disso, temos a "equação de Ampere" na matéria (com $\vec{\mathcal{J}}_{\ell}=\vec{0}$):
$$\nabla\times\left(\frac{1}{\mu_{0}}\vec{B}\right)=\partial_{t}(\varepsilon_{0}\vec{E}+\vec{P})\to \nabla \times \vec{B}=\mu_{0}\partial_{t}(\varepsilon_{0}\vec{E}+\vec{P})$$
Podemos ainda reescrever o termo do campo magnético na equação acima como:
$$\nabla \times(-\partial_{t}\vec{E})=-\partial_{t}(\nabla\times\vec{B})$$
Assim ficamos com:
$$- \nabla^{2}\vec{E}=-\mu_{0}\partial_{t}^{2}(\varepsilon_{0}\vec{E}+\vec{P})$$
$$\boxed{\nabla^{2}\vec{E}-\varepsilon_{0}\mu_{0}\partial_{t}^{2}\vec{E}=\mu_{0}\partial_{t}^{2}\vec{P}}$$
sendo que temos as soluções:
$$\begin{align*}
\vec{E}(\vec{r},t)&= \vec{E_{0}}\exp[i(\vec{k}\cdot\vec{r}-\omega t)]\\
\vec{P}(\vec{r},t)&= \vec{P_{0}}\exp[i(\vec{k}\cdot\vec{r}-\omega t)]
\end{align*}$$
isto surge de presumir que quando uma radiação de frequência $\omega$ incide num meio, a polarização induzida também oscila com a mesma frequência $\omega$.

### 1.9.2 - Susceptibilidade Elétrica
- Podemos substituir as soluções na equação de onda:
$$\begin{align*}
\nabla^{2}\vec{E}-\varepsilon_{0}\mu_{0}\partial_{t}^{2}\vec{E}&= \mu_{0}\partial_{t}^{2}\vec{P}\\
\nabla^{2}(\vec{E_{0}}\exp[i(\vec{k}\cdot\vec{r}-\omega t)])-\varepsilon_{0}\mu_{0}\partial_{t}^{2}(\vec{E_{0}}\exp[i(\vec{k}\cdot\vec{r}-\omega t)])&= \mu_{0}\partial_{t}^{2}(\vec{P_{0}}\exp[i(\vec{k}\cdot\vec{r}-\omega t)])\\
-k^{2}\vec{E_{0}}+ \varepsilon_{0}\mu_{0}\omega^{2}\vec{E_{0}}&= -\mu_{0}\omega^{2}\vec{P_{0}}\\
\vec{P_{0}}(\omega)&= \varepsilon_{0} \left(\frac{k^{2}-\varepsilon_{0}\mu_{0}\omega^{2}}{\varepsilon_{0}\mu_{0}\omega^{2}}\right)\vec{E_{0}}\\
\vec{P_{0}}(\omega)&= \varepsilon_{0}\chi(\omega)\vec{E_{0}}
\end{align*}$$
em que $\chi$ é a susceptibilidade, uma grandeza adimensional que diz o quanto um material é suscetivel a ser polarizado. Este número é geralmente complexo.

- Consideremos que temos a susceptibilidade escrita como  $\chi=\chi_{0}\exp(i\delta)$. Neste caso, $\chi_{0}$ representa a magnitude da resposta do meio ao campo externo aplicado. Temos ainda $\delta$ representa o desfasamento temporal entre a respota do material e o campo que originou a polarização.
- Se por outro lado tivermos a susceptibilidade escrita na forma $\chi=\chi'+i\chi''$.  A parte imaginária está relacionada com a parte imaginária do índice de refração $n''$ e quantifica o decaimento da amplitude do campo elétrico ao entrar no material.

### Relação de Dispersão
$$\mathcal{D}(\vec{k},\omega)=\frac{c^{2}k^{2}}{1+\chi(\omega)}-\omega^{2}$$
sendo que esta grandeza depende do meio.

### Constante Dielétrica
- Podemos definir como
$$\varepsilon_{r}(\omega)\equiv \varepsilon'_{r}(\omega)+i\varepsilon''_{r}(\omega)=1+\chi(\omega)$$

### Índice de Refração Complexo
$$\mathcal{N}(\omega)\equiv n'(\omega)+in''(\omega)=\sqrt{1+\chi(\omega)}$$

- Para meios de absorção baixa temos $\text{Im}(\chi)\ll\text{Re}(\chi)$ (sendo estes meios transparentes). Assim, podemos aproximar:
$$\begin{align*}
n'(\omega)&\approx \sqrt{1+\text{Re}[\chi(\omega)]}\\
n''(\omega)&\approx \frac{\text{Im}[\chi(\omega)]}{2\sqrt{1+\text{Re}[\chi(\omega)]}}
\end{align*}$$
- Recordando a relação do secundário $\mathcal{N}=\frac{v}{c}$ temos:
$$k=\frac{\omega}{v}=\frac{\mathcal{N}(\omega)\omega}{c}=\frac{[n'(\omega)+in''(\omega)]\omega}{c}$$
sendo $\vec{k_{0}}=\frac{\omega}{c}\frac{\vec{k}}{k}$ e podemos escrever: $\vec{k}=[n'(\omega)+in''(\omega)]\vec{k_{0}}$.
- Daqui temos:
$$\vec{E}(\vec{r},t)=\vec{E_{0}}\exp(-n''\vec{k_{0}}\cdot\vec{r})\exp[i(n'\vec{k_{0}}\cdot\vec{r}-\omega t)]$$
em que vemos que a parte real do coeficiente descreve a oscilação do campo e a parte imaginária o seu decaimento conforme este penetra (😜) o material.


## 1.10 - Tipos de Ondas em meios óticos
### Ondas Propagantes
- Ocorrem quando temos $n'\neq0,n''=0$. A onda entra no meio e continua a propagar-se sem que este aborva energia.
- A onda move-se com a mesma frequência, mas com vetor de onda $\vec{k}=\vec{k_{0}}n'$ (pelo que temos velocidade $k=\frac{\omega}{v}=\frac{\omega}{c}n'\to c=vn' \to v=\frac{c}{n'}$)
![[refracao fisica otica.png]]

### Ondas Evanescentes
- Ocorrem quando temos $n'=0,n''\neq0$. A onda torna-se muito atenuada e sem oscilação. 
- As ondas são apenas caraterizadas por um comprimento caraterístico de atenuação. Assim, a onda fica localizada junto à superfície. Não transmitem energia.
![[refracao onda absorvida.png]]

### Onda Propagante Atenuada
- Consiste na mistura dos 2 casos acima. Temos $n'\neq0,n''\neq0$.
![[refracao onda atenuada mas continua a oscilar.png]]

## 1.11 - Dispresão da Luz
- Acima obtivemos a equação do campo no meio óptico:
$$\vec{E}(\vec{r},t)=\vec{E_{0}}\exp(-n''\vec{k_{0}}\cdot\vec{r})\exp[i(n'\vec{k_{0}}\cdot\vec{r}-\omega t)]$$
- Assim, a frente de onda é definida por:
$$n'(\omega)\vec{k_{0}}\cdot\vec{r}-\omega t+\phi_{0}=\phi$$
e temos
$$\vec{r}(t)=\vec{r}_{\perp}+\vec{v}t+\vec{r}_{\parallel}$$
em que, tal como fizemos acima, $\vec{r}_{\parallel}=\frac{\phi-\phi_{0}}{n'k_{0}^{2}}\vec{k_{0}}$ (apenas substituimos $k=k_{0}n'$)
- Em que temos a onda a mover-se com velocidade
$$\vec{v}=\frac{c}{n'(\omega)}\frac{\vec{k_{0}}}{k_{0}}$$

## 1.12 - Propriedades Fundamentais da Luz em Meios Óticos
### Campo Deslocamento
- Vimos que os campos $\vec{E},\vec{B}$ andam sempre em fase em meios isotrópicos. 
- Sabemos que podemos calcular o vetor deslocamento com:
$$\vec{D}(\vec{r},t)=\varepsilon(\omega)\vec{E}(\vec{r},t)$$
ou seja:
$$\vec{D}(\vec{r},t)=\varepsilon(\omega)\vec{E_{0}}\exp[i(\vec{k}\cdot\vec{r}-\omega t+\phi_{0})]$$
(não esquecer que isto continua a ver equivalente à forma de $\vec{E}$ que vimos com as 2 exponenciais, porque aqui temos $\vec{k}=[n'(\omega)+in''(\omega)]\vec{k_{0}}$)
- Temos que:
$$\varepsilon(\omega)=\sqrt{\varepsilon'(\omega)^{2}+\varepsilon''(\omega)^{2}}\exp(i\varphi)$$
pelo que:
$$\vec{D}(\vec{r},t)=\sqrt{\varepsilon'(\omega)^{2}+\varepsilon''(\omega)^{2}} \vec{E_{0}}\exp[i(\vec{k}\cdot\vec{r}-\omega t+\phi_{0}+\varphi)]$$
ou seja, o campo deslocamento inclui a contribuição do campo elétrico externo $\vec{E}$ e da resposta do meio.

### Vetor de Poyting
- Num meio dielétrico podemos escrever a densidade de energia como:
$$u=\frac{1}{2}\vec{D}\cdot\vec{E}+ \frac{1}{2}\vec{H}\cdot\vec{B}$$
- Sabemos ainda que o vetor Poyting é dado por
$$\vec{S}=\vec{E}\times\vec{H}$$
- O valor médio deste é:
$$\langle \vec S\rangle = \frac{\vec u}{4\mu_0}\frac{k+k^*}{\omega}(\vec E_0^* \cdot \vec E_0)\cos[(\vec k - \vec k^*)\cdot \vec r] + i\frac{\vec u}{4\mu_0}\frac{k-k^*}{\omega}(\vec E_0^* \cdot \vec E_0)\sin[(\vec k - \vec k^*)\cdot \vec r]$$
($\vec{u}$ _provavelmente_ é o vetor que indica a direção de propagação da onda)

## 1.13 - Modelos Óticos
### 1.13.1 - Modelo de Lorentz para Dielétricos
**Qualitativamente**
- Neste modelo consideramos que os átomos do meio se orientam conforme o campo elétrico que neles incide. Assim, os átomos irão dar origem a um campo no meio similar ao original, mas com atrasado de fase.
- Este modelo apenas é válido para *campos fracos*

- Assumimos que:
    - Os átomos/moléculas do material são idênticos e uniformemente distribuidos
    - Só 1 eletrão por átomo/molécula responde ao campo, tendo-se estes eletrões distribuidos uniformemente pelo meio.

**Quantitativamente**
- Consideramos que, quandos sujeitos a um campo elétrico, os átomos se comportam como um oscilador harmónico forçado e amortecido. Tendo em conta isto e o facto que assumimos que apenas 1 eletrão se move, temos que a equação do movimento é:
$$\begin{align*}
m_{e}\Delta\ddot{\vec{r}}&= q_{e}\vec{E} - m_{e}\gamma\Delta\dot{\vec{r}} - m_{e}\omega_{0}^{2}\Delta\vec{r}\\
\frac{q_{e}}{m_{e}}\vec{E}&= \Delta\ddot{\vec{r}} + \gamma\Delta\dot{\vec{r}} +\omega_{0}^{2}\Delta\vec{r}
\end{align*}$$
($\Delta\vec{r}$ é o deslocamento do eletrão em relação ao equilíbrio, $\gamma$ descreve o amortecimento do átomo, $\omega_{0}$ é a frequência de oscilação natural do átomo)

- Consideremos que o campo $\vec{E}$ que chega ao eletrão é a sobreposição de vários campos com frequências $\omega$ (por exemplo os campos gerados da interação do campo com outras átomos). Teremos:
$$\begin{align*}
\vec{E}(\vec{r},t)&= \int_{-\infty}^{+\infty} \vec{E_{0}}(\omega)\exp[i(\vec{k}\cdot\Delta\vec{r}-\omega t)]d\omega\\
&= \int_{-\infty}^{+\infty} \vec{E_{0}}(\omega)\exp(i\vec{k}\cdot\Delta\vec{r})\exp(-i\omega t)d\omega 
\end{align*}$$
ora, integramos em $\omega$ para contar as contribuições de todas as frequências possíveis. Na prática, temos uma transformada inversa de Fourier.
- Se tivermos o eletrão a comportar-se de frma idêntica ao campo teremos:
$$\Delta\vec{r}=\int_{-\infty}^{+\infty}\vec{r_{0}}(\omega)\exp(-i\omega t)d\omega$$
em que o termo $\exp(i\vec{k}\cdot\Delta\vec{r})$ desaparece porque o deslocamento do eletrão será muito reduzido e temos $\vec{k}\cdot\Delta\vec{r}\sim0$.

- Se substituiroms este campo na equação do movimento:
$$\begin{align*}
\frac{q_{e}}{m_{e}}\vec{E_{0}}&= (-i\omega)^{2}\vec{r_{0}}-i\omega\gamma\vec{r_{0}}+\omega_{0}^{2}\vec{r_{0}}\\
\vec{r_{0}}(\omega)&= \frac{q_{e}}{m_{e}}\cdot \frac{\vec{E_{0}}}{\omega_{0}^{2}-i\omega\gamma-\omega^{2}}
\end{align*}$$

- Podemos ainda escrever a densidade de momento dipolar:
$$\vec{P}(\omega)=N\vec{\mu}(\omega)=N q_{e}\vec{r_{0}}$$
em que $N$ é a densidade de eletrões polarizados por unidade de volume e $\vec{\mu}$ é o momento dipolar de 1 átomo. (Caso se tenhas esquecido, usou-se a equação de momento dipolar $\vec{\mu}=q\vec{d}$)
- Na prática, a densidade de momento dipolar $\vec{P}(\omega)$ é a transformada de Fourier da polarização $\vec{P}(\vec{r},t)$.
- Ao substituir $\vec{r_{0}}$ na equação da densidade de momento dipolar:
$$\vec{P}(\omega)=\frac{Nq_{e}^{2}}{m_{e}}\frac{\vec{E_{0}}(\omega)}{\omega_{0}^{2}-i\omega\gamma-\omega^{2}}$$
- Podemos definir:
$$\chi(\omega)=\frac{\omega_{p}^{2}}{\omega_{0}^{2}-i\omega\gamma-\omega^{2}}$$
em que $\omega_{p}$ é a frequência de plasma, que corresponde à frequência de ressonância, estando associada à resposta de todos os eletrões do meio em conjunto, de tal modo que:
$$\omega_{p}=\sqrt{\frac{Nq_{e}^{2}}{m_{e}\varepsilon_{0}}}$$
e fica
$$\vec{P}(\omega)=\varepsilon_{0}\chi(\omega)\vec{E_{0}}(\omega)$$
que é simplesmente a equação $P=\varepsilon_{0}\chi E$ que já vimos para dielétricos lineares, mas no domínio das frequências.

**Média de Susceptibilidades**
- Se, contrariamente ao que assumimos atrás, tivermos 2+ eletrões por átomo a reagir ao campo elétrico, a suscetibilidade de cada átomo passa a ser descrita por:
$$\chi(\omega)=\sum\limits_{n=0}^{N}f_{n}\frac{\omega_{p}^{2}}{\omega_{0,n}^{2}-i\omega\gamma_{n}-\omega^{2}}$$

**Índice de Refração**
- Tal como no vazio, temos:
$$\mathcal{N}(\omega)=\sqrt{1-\chi(\omega)}=\sqrt{1-\frac{\omega_{p}^{2}}{\omega_{0}^{2}-i\omega\gamma-\omega^{2}}}$$


### 1.13.2 - Modelo de Drude para Condutores
- O modelo de Lorentz assume que $\vec{\mathcal{J_\ell}}=\vec{0}$ e estudamos a polarização.
- O modelo de Drude faz o oposto: temos que $\vec{P}=\vec{0}$ e estudamos as cargas livres.

**Quantitativamente**
- A equação de onda num meio com $\vec{\mathcal{J_{\ell}}}\neq\vec{0}$ é dada por:
$$\nabla^{2}\vec{E}-\varepsilon_{0}\mu_{0}\partial_{t}^{2}\vec{E}=\mu_{0}\partial_{t}\vec{\mathcal{J_{\ell}}}$$
- As soluções desta equação serão uma sobreposição de oscilações sinusoidais (Fourier):
$$\begin{align*}
\vec{E}(\vec{r},t)=\int \vec{E_{0}}(\vec{r},\omega)\exp(-i\omega t)d\omega\\
\vec{\mathcal{J_{\ell}}}(\vec{r},t)=\int\vec{\mathcal{J}}_{0}(\vec{r},\omega)\exp(-i\omega t)d\omega
\end{align*}$$
- Acima dissemos que $\vec{P}(\omega)=N\vec{\mu}(\omega)$, ou seja, a densidade de momento dipolar consiste na junção dos momentos dipolares de todos os átomos. Ora, pela mesma lógica, para a corrente temos:
$$\vec{\mathcal{J_{\ell}}}=q_{e}N\langle \vec{v}\rangle$$
($N$ é a densidade volúmica de eletrões livres)

**Velocidade**
- Podemos escrever a equação do movimento em função da velocidade (em que agora não temos um termo da força de restituição - os eletrões estão livres):
$$\begin{align*}
m_{e}\dot{\vec{v}}=q_{e}\vec{E}-m_{e}\gamma\vec{v}\\
\dot{\vec{v}}+\gamma\vec{v}=\frac{q_{e}}{m_{e}}\vec{E}
\end{align*}$$
e temos soluções do tipo:
$$\vec{v}(t)=\int \vec{v_{0}}(\omega)\exp(-i\omega t)d\omega$$
novamente temos uma transformada de Fourier :D

- Não sei bem como, mas podemos daqui definir a velocidade média:
$$\langle\vec{v}(\vec{r},t)\rangle\approx \int \frac{q_{e}}{m_{e}}\frac{\vec{E}(\vec{r},\omega)}{\gamma-i\omega}d\omega$$
e ficamos com
$$\vec{\mathcal{J_{\ell}}}=\frac{Nq_{e}^{2}}{m_{e}}\frac{\vec{E}(\vec{r},\omega)}{\gamma-i\omega}$$

**Índice de Refração Complexo**
- Na equação de onda $\nabla^{2}\vec{E}-\varepsilon_{0}\mu_{0}\partial_{t}^{2}\vec{E}=\mu_{0}\partial_{t}\vec{\mathcal{J_{\ell}}}$ podemos calcular os 2 lados:
    - $\nabla^{2}\vec{E}-\varepsilon_{0}\mu_{0}\partial_{t}^{2}\vec{E}=(-k^{2}+\varepsilon_{0}\mu_{0}\omega^{2})\vec{E_{0}}e^{i(\vec{k}\cdot\vec{r}-\omega t)}=(-k^{2}+ \frac{\omega^{2}}{c^{2}})\vec{E_{0}}e^{i(\vec{k}\cdot\vec{r}-\omega t)}$
    - $\mu_{0}\partial_{t}\vec{\mathcal{J_{\ell}}}= \mu_{0}\partial_{t}\left(\frac{Nq_{e}^{2}}{m_{e}}\frac{\vec{E}(\vec{r},\omega)}{\gamma-i\omega}\right)= \frac{Nq_{e}^{2}}{m_{e}}\frac{\omega}{i\gamma+\omega}\vec{E_{0}}e^{i(\vec{k}\cdot\vec{r}-\omega t)}=\varepsilon_{0}\mu_{0}\omega_{p}^{2} \frac{\omega}{i\gamma+\omega}\vec{E_{0}}$ 
- Podemos juntar os dois:
$$\begin{align*}
\left(-k^{2}+\frac{\omega^{2}}{c^{2}}\right)\vec{E_{0}}= \frac{\omega_{p}^{2}}{c^{2}}\frac{\omega}{i\gamma+\omega}\vec{E_{0}}
\end{align*}$$
de onde temos:
$$k^{2}=\frac{\omega^{2}}{c^{2}}-\frac{\omega_{p}^{2}}{c^{2}}\frac{\omega}{i\gamma+\omega}$$
- Se assumirmos que $\gamma\sim0$ para $\omega$ elevado:
$$\begin{align*}
k^{2}&\approx \frac{1}{c^{2}}(\omega^{2}-\omega_{p}^{2})\\
(kc)^{2}= \left(\frac{\omega}{v}c\right)^{2} &= (\omega^{2}-\omega_{p}^{2})\\
\mathcal{N}^{2}(\omega)&= 1- \left(\frac{\omega_{p}}{\omega}\right)^{2}
\end{align*}$$
ou seja, vemos que quando $\omega<\omega_{p}$ temos um índice de refração complexo e a onda cai exponencialmente ao entrar no condutor. Caso contrário, a onda propaga-se e o condutor é transparente à radiação EM.

### 1.13.3 - Compatibilidade entre os 2 modelos
- No método de Lorentz obtivemos:
$$\mathcal{N}^{2}(\omega)= 1-\frac{\omega_{p}^{2}}{\omega_{0}^{2}-i\omega\gamma-\omega^{2}}$$
e no modelo de Drude:
$$\mathcal{N}^{2}(\omega)=1- \left(\frac{\omega_{p}}{\omega}\right)^{2}$$
- Ora, no limite em que $\omega_{0}\to0$ e para frequências em que $\gamma\sim0$ temos que estas equações são quase idênticas (mas fica um sinal oposto não sei porquê).
- Na prática, o modelo de Lorentz descreve um material com eletrões ligados, o de Drude um material com eletrões livres. Ora, num material real temos uma combinação de ambos, pelo que:
$$\chi(\omega)=\chi_\text{Lorentz}(\omega)+\chi_\text{Drude}(\omega)$$
![[modelos lorentz e drude.png]]

## 1.14 - Relação de Clausius-Mossoti
$$\frac{\varepsilon_{r}-1}{\varepsilon_{r}+2}=\frac{N\alpha}{3\varepsilon_{0}}$$
em que $N$ é o número de Dipolos por volume do meio e $\alpha$ a polarizabilidade atómica/molecular.

**Suscetibilidade Elétrica**
- Sendo $\varepsilon_{r}=1+\chi$ temos:
$$\chi(\omega)=\frac{\frac{N\alpha}{\varepsilon_{0}}}{1-\frac{N\alpha}{3\varepsilon_{0}}}$$

**Índice de Refração**
- Em EM2 vimos que $n\approx\sqrt{\varepsilon_{r}}$ e temos:
$$\frac{n^{2}-1}{n^{2}+2}=\frac{N\alpha}{3\varepsilon_{0}}$$

## 1.15 - Sellmeier
- Começamos com o modelo de Lorentz e assumimos que o meio não absorve energia da onda. Isto corresponde a fazer $\gamma=0$ (a energia gasta a amortecer as oscilações dos eletrões era "tirada" do campo). Isto por sua vez significa que a parte imaginária de $\chi(\omega)$ desaparece e temos:
$$\mathcal{N}^{2}(\omega)=1+\sum\limits_{n=0}^{N}f_{n}\frac{\omega_{p}^{2}}{\omega_{0,n}^{2}-\omega^{2}}=n^{2}(\omega)$$
- Temos o comprimento de onda do campo no vazio $\lambda_{0}=\frac{2\pi c}{\omega}$. Usando isto, temos:
$$\begin{align*} 
n^{2}(\lambda_{0}) &= 1 + \sum_{n=0}^{N}\left(\frac{f_{n}\omega^{2}_{p}}{\omega^{2}_{0,n}}\right)\frac{\lambda^{2}_{0}}{\lambda_{0}^{2} - \left(\frac{2\pi c}{\omega_{0,n}}\right)^{2}} \\
&= 1 + \sum_{n=0}^{N} \frac{B_{n}\lambda_{0}^{2}}{\lambda_{0}^{2} - C_{n}} \end{align*}$$em que
$$B_n \equiv \frac{f_n\omega_p^2}{\omega_{0,n}^2}\quad\quad;\quad\quad C_n \equiv \left(\frac{2\pi c}{\omega_{0,n}}\right)^2$$
são os **coeficientes de Sellmeier**. Estes são determinados experimentalmente e tabelados. Permitem-nos determinar o índice de refração com boa aproximação.
- Temos:
![[grafico sellmeyer.png]]

## 1.16 - Meios Óticos
- Como kinda vimos atrás, quando luz entra num meio ótico o seu comportamento difere daquele no vácuo. Podemos resumir este comportamento a 2 constantes: $\varepsilon,\mu$.
- Veremos principalmente materiais descritos por $\mu$ AKA meios dielétricos

### 1.16.1 - Meios Óticos LHI
(mais concretamente, Meios Óticos Lineares Homogéneos e Isotrópicos)
- Nestes temos
$$\vec{D}=\varepsilon_{0}\varepsilon_{r}\vec{E}$$
- A equação de onda toma a forma
$$\nabla^{2}\vec{E}=\mu_{0}\varepsilon_{0}\varepsilon_{r}\partial_{t}^{2}\vec{E}$$
- Como é costume, a onda plana é uma solução da equação
$$\vec{E}=\vec{E_{0}}\exp[i(\omega t-\vec{k}\cdot\vec{r})]$$
pelo que a substituirmos de volta na equação de onda obtemos
$$\varepsilon_{r}\omega^{2}=c^{2}k^{2}$$
ou seja, a *velocidade de fase* da onda é afetada pela constante dielétrica.

- Ora, como $\varepsilon_{r}$ é complexo (depende de $\chi$) temos que $\omega,\vec{k}$ também o serão. Daqui surge:
$$\vec{E}(\vec{r},t)=\vec{E_{0}}\exp[-(\omega''t-\vec{k''}\cdot\vec{r})]\exp[i(\omega't-\vec{k'}\cdot\vec{r})]$$

### 1.16.2 - Meios Óticos LHA
(Mais concretamente, Meios Óticos Lineares Homogéneos Anisotrópicos)
- Pensa na T9 de Labs 3.
- Ou seja, estes meios têm anisotropia ótica, o que significa que a velocidade da luz no meio depende do plano de polarização. Ou seja, é como se tivessemos 2+ constantes dielétricas AKA 2+ índices de refração.

**Tensor Constante Dielétrica**
- Para este tipo de meios, podemos definir a constante dielétrica como sendo um tensor do tipo:
$$\varepsilon_{r}=\begin{pmatrix}n_{x}^{2} & 0 & 0 \\ 0 & n_{y}^{2} & 0 \\ 0 & 0 & n_{z}^{2}\end{pmatrix}$$

## 1.17 - Continuidade do Campo EM
- Vamos agora estudar o que acontece quando uma onda EM atravessa um interface entre 2 meios distintos.

### 1.17.1 - Dentro de um Mesmo Meio
- Temos uma onda Em plana, monocromática:
$$\vec{E}(\vec{r},t)=\vec{E_{0}}\exp[i(\vec{k}\cdot\vec{r}-\omega t)]$$
- Em EM2 deduzimos:
$$\begin{align*}
\partial_{t}\vec{B}&= -i\omega\vec{B}\\
\nabla\times\vec{E}&= i\vec{k}\times\vec{E}
\end{align*}$$
- Partindo disto, vemos que as leis de Faraday e Ampere (considerando um meio sem corrente) ficam:
$$\begin{align*}
\nabla \times \vec{E}&= -\partial_{t}\vec{B} &&\to&& \omega\vec{B}=\vec{k}\times\vec{E} \\
\nabla\times\vec{H}&= \partial_{t}\vec{D} &&\to&& \omega\vec{D}=-\vec{k}\times\vec{H}
\end{align*}$$
- Usando as equações para meios LHI ($\vec{B}=\mu_{r}\mu_{0}\vec{H},\vec{D}=\varepsilon_{r}\varepsilon_{0}\vec{E}$) obtemos:
$$\begin{align*}
\omega \mu_{r}\mu_{0}\vec{H}&= \vec{k}\times\vec{E}\\
\omega\varepsilon_{r}\varepsilon_{0}\vec{E}&= -\vec{k}\times\vec{H} 
\end{align*}$$
pelo que estas equações são válidas em qualquer ponto do meio em que temos campo EM.

### 1.17.2 - Interface de Meios Diferentes
- Se tivermos na interface de 2 meios com valores diferentes de $\varepsilon_{r}$ ou $\mu_{r}$ as equações acima não se aplicam

**Sem cargas**
- Sendo $\vec{n}$ o vetor normal à superfície de interface dos meios, que aponta de $1$ para $2$, temos as condições:
$$\begin{align*}
\vec{n}\times(\vec{E_{2}}-\vec{E_{1}})&= \vec{0}\\
\vec{n}\times(\vec{H_{2}}-\vec{H_{1}})&= \vec{0}\\
(\vec{D_{2}}-\vec{D_{1}})\cdot\vec{n}&= 0\\
(\vec{B_{2}}-\vec{B_{1}})\cdot\vec{n}&= 0
\end{align*}$$
que são necessárias para que o campo EM respeita as equações de Maxwell integrais. São as relações que garantem a continuidade dos campos.

**Com cargas**
- Se tivermos uma densidade superficial de carga $\sigma_{s}$ entre os meios e uma densidade superficial de corrente $\vec{\mathcal{J}}_{s}$ nesse plano, as equações ficam:
$$\begin{align*}
\vec{n}\times(\vec{E_{2}}-\vec{E_{1}})&= \vec{0}\\
\vec{n}\times(\vec{H_{2}}-\vec{H_{1}})&= \vec{\mathcal{J}}_{s}\\
(\vec{D_{2}}-\vec{D_{1}})\cdot\vec{n}&= \sigma_{s}\\
(\vec{B_{2}}-\vec{B_{1}})\cdot\vec{n}&= 0
\end{align*}$$

## 1.18 - Leis de Fresnel
- Descrevem as relações entre amplitudes, fases, polarização das ondas incidentes, transmitidas e refletidas num interface entre 2 meios com índices de refração diferentes.
- Iremos considerar que os meios são dielétricos e não magnéticos ($\mu_{i}=\mu_{t}=\mu_{0}$). Isto é consistente com o modelo de Lorentz.

### 1.18.1 - Lei de Snell
- Tendo-se uma onda incidente com vetor de onda $\vec{k_{i}}$ a formar um ângulo $\theta_{i}$ com a normal do interface. Esta lei diz que a onda transmitida irá propagar-se numa direção que forma um ângulo $\theta_{t}$ com a normal, sendo que:
$$n_{1}\sin\theta_{i}=n_{2}\sin\theta_{t}$$
- Temos que a onda refletida descreve um ângulo $\theta_{r}=\theta_{i}$. Assim, as linhas que a onda incidente e refletida seguem formam o *plano de incidência*.
![[polarização P e S na reflexão.png]]
- Em que dizemos que a onda tem polarização $P$ quando o campo $\vec{E}$ é "paralelo" ao plano de incidência e polarização $S$ quando o campo "sticks out" do plano de incidência.

### 1.18.2 - Campo Elétrico Paralelo ao plano de incidência
![[interseção interface de meios.png]]
- Temos uma onda com polarização P. Temos o plano de incidência a ser o plano $z=0$ e o plano do interface a ser $y=0$.
- Para que haja conservação dos campos, é preciso que:
$$\begin{align*}
E_{0i}\cos\theta_{i}-E_{0r}\cos\theta_{r}&= E_{0t}\cos\theta_{t}\\
B_{0i}+B_{0r}&= B_{0t}
\end{align*}$$
podemos usar $B=\frac{n}{c}E$ e a 2ª equação fica:
$$n_{i}(E_{0i}+E_{0r})=n_{t}E_{0t}$$
- Usando esta relação e o facto que $\cos\theta_{i}=\cos\theta_{r}$ temos
$$\begin{align*}
E_{0i}\cos\theta_{i}-E_{0r}\cos\theta_{r}&= E_{0t}\cos\theta_{t}\\
(E_{0i}-E_{0r})\frac{\cos\theta_{i}}{\cos\theta_{t}}&= E_{0t}\\
(E_{0i}-E_{0r})\frac{\cos\theta_{i}}{\cos\theta_{t}}&= \frac{n_{i}}{n_{t}}(E_{0i}+E_{0r})\\
&\dots\\
\frac{E_{0r}}{E_{oi}}&= \frac{n_{t}\cos\theta_{i}-n_{i}\cos\theta_{t}}{n_{t}\cos\theta_{i}+n_{i}\cos\theta_{t}}
\end{align*}$$

- Podemos fazer o oposto: Da 1ª equação temos:
$$\begin{align*}
E_{0r}=E_{0i}-E_{0t}\frac{\cos\theta_{t}}{\cos\theta_{i}}
\end{align*}$$
e ao substituir na 2ª:
$$\begin{align*}
n_{i}(E_{0i}+E_{0r})&= n_{t}E_{0t}\\
n_{i}\left(2E_{0i}-E_{0t}\frac{\cos\theta_{t}}{\cos\theta_{i}}\right)&= n_{t}E_{0t}\\
&\dots\\
\frac{E_{0t}}{E_{0i}}&= \frac{2n_{i}\cos\theta_{i}}{n_{t}\cos\theta_{i}+n_{i}\cos\theta_{t}}
\end{align*}$$
- E temos então as Equações de Fresnel para a Onda P:
$$\boxed{\begin{align*} r_P &= \frac{E_r}{E_i} = \frac{n_t\cos\theta_i-n_i\cos\theta_t}{n_t\cos\theta_i+n_i\cos\theta_t} \\[10pt] t_P&= \frac{E_t}{E_i} = \frac{2n_i\cos\theta_i}{n_t\cos\theta_i+n_i\cos\theta_t} \end{align*}}$$

### 1.18.3 - Campo Elétrico Perpendicular ao Plano de Incidência
![[interseção de onda com polarização P.png]]
- Temos uma onda com polarização S. Temos o plano de incidência a ser o plano $z=0$ e o plano do interface a ser $y=0$.
- Usando as equações de continuidade dos campos (não quis deduzir) obtemos as Equações de Fresnel para a Onda S:
$$\boxed{\begin{align*} r_S &= \frac{E_r}{E_i} = \frac{n_i\cos\theta_i - n_t\cos\theta_t}{n_i\cos\theta_i + n_t\cos\theta_t} \\[10pt] t_S &= \frac{E_t}{E_i} = \frac{2n_i\cos\theta_i}{n_i\cos\theta_i + n_t\cos\theta_t} \end{align*}}$$
- De notar que para um referencial diferente daquele usado aqui para determinar as equações, podemos ter um ou outro sinal diferente. Assim, é importante ter o referencial em conta.

## 1.19 - Refletância e Transmitância
**Coeficiente de Reflexão**
$$R=\frac{I_{r}}{I_{i}}=\left(\frac{E_{0r}}{E_{0i}}\right)^{2}=r^{2}$$
em que $I$ são as *irradiâncias* das ondas incidente e refletida.
- Este $r$ é o mesmo valor que definimos acima, nas equações de Fresnel. Ao termos a equação $R=r^{2}$ o sinal do $r$ deixa de importar. Podemos portanto escrever $R_{P}=r_{P}^{2}~,~R_{S}=r_{S}^{2}$.
- Na equação acima usamos $I=\langle S\rangle\simeq\frac{E^{2}}{\mu_{0}}$

- Devemos notar que $R_{S},R_{P}$ apenas são a refletância de ondas S,P. Ou seja, $R_{S}$ é a fração de $I_{iS}$ refletida, não de $I_{i}$ (porque esta pode ter uma componente de polarização $P$). Assim é útil definir:
$$R=\frac{1}{2}(R_{P}+R_{S})$$

**Coeficiente de Transmissão**
- A luz que não é refletida terá que ser transmitida, pelo que:
$$\begin{align*}
T_{P}&= 1-R_{P}\\
T_{S}&= 1-R_{S}\\
T&= 1-R
\end{align*}$$

## 1.20 -  Outros
### 1.20.1 - Ângulo de Brewster
![[Attachments/FCUP/A3S1/OF/angulo de brewster.png]]
- Ângulo de Incidência para o qual a luz *com uma certa polarização* $\theta_{p}$ é perfeitamente transmitida (sem reflexão). Temos:
$$\theta_{p}+\theta_{t}=\frac{\pi}{2}$$
- Se, por outro lado (figura acima) tivermos uma luz não polarizada a incidir, para este ângulo apenas é refletida luz com polarização S (perpendicular ao plano de incidência).
- Podemos definir o ângulo de Brewster com:
$$\theta_{B}=\arctan\left(\frac{n_{t}}{n_{i}}\right)$$

### 1.20.2 - Ângulo Crítico
![[angulo critico.png]]
- Ângulo de incidência a partir do qual se dá reflexão interna total. Este é específico para casos em que $n_{i}>n_{t}$ (meio inicial é o mais lento).
- Podemos definir:
$$\theta_{c}=\arcsin\left(\frac{n_{t}}{n_{i}}\right)$$
(isto é diretamente deduzido da equação de Snell, tendo-se $\theta_{t}=\pi/2$)