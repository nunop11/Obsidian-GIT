# 1 - Introdução
## 1.1 - Fórmulas 
- Recordemos as fórmulas de relatividade úteis:
$$E=\sqrt{p^{2}c^{2}+m^{2}c^{4}}=\gamma m_{0}c^{2} = mc^{2} \quad;\quad \vec{p}=\gamma m_{0}\vec{v}=m \vec{v}$$
em que $m_{0}$ é a *massa de repouso*, sendo que a massa relativista é $m=\gamma m_{0}$.
- De recordar ainda que da mecânica Newtoniana/clássica temos:
$$E_{c}=\frac{p^{2}}{2m}  \quad \quad;\quad \quad \vec{p}=m \vec{v}$$
## 1.2 - Quando usar Quântica
- Definimos uma grandeza *ação*. Temos: $$[S] = \textsf{[energia] $\times$ [tempo]}= \textsf{[mom linear] $\times$ [comprimento]} = \textsf{[mom angular]}= L^{2}MT^{-1}$$
- Assim, se $S\ll \hbar$ então teoria de *Newton é suficiente*.

# 2 - Efeito Fotoelétrico
![[Circuito efeito fotoeletrico.png|350]]
- Basicamente, radiação indice na placa C, o que causa a emissão de eletrões. A circulação dos eletrões gera um campo elétrico como ilustrado acima. Podemos ainda aplicar uma diferença de potencial entre A e C.
- Não ocorre com eletrões livres.

- Para o efeito fotoelétrico temos os gráficos 1,2,3:
![[I(i) efeito fotoeletrico.png|285]]  ![[ii(V) efeito fotoeletrico.png|450]]  ![[V0(f) efeito fotoeletrico.png|310]]
- Em que $I$ é a intensidade da radiação incidente, $i$ a corrente elétrica entre as placas, $V$ a DDP entre as placas, $V_{0}$ o *potencial de paragem* (DDP em que nenhum eletrão chega a A) e $f$ a frequência da radiação incidente.
- Podemos definir:
$$I=\frac{\textsf{energia}}{\textsf{area $\times$ tempo}} \quad;\quad i = \frac{dq}{dt}$$
- Vejamos agora como cada teoria explica os gráficos:
### TOR
Neste teoria temos $I= \frac{1}{2} \varepsilon_{0}c E^{2}$
**Gráfico 1** - Temos que $I\propto \vec{E}$. Ou seja, como temos $F=-e \vec{E}=m \frac{dv}{dt}$, ao aumentar $I$ aumenta $\vec{E}$ e também $E_{c}$. Como $E_{c}$ aumenta, a energia total $E$. Para uma certa intensidade de radiação, temos $E=E_\textsf{ionização}$. Aí, começam a ser ejetados eletrões da placa C. O gráfico é explicado por esta teoria.
**Gráfico 2** - Consideremos que a radiação tem intensidade suficiente para que eletrões sejam projetados. Se a tensão for *retardadora* ($V<0$) a corrente irá ser menor. Se a corrente for aceleradora ($V>0$), então mais eletrões chegam à placa A e a corrente aumenta. No entanto, a partir de uma certa tensão, a corrente torna-se constante: *corrente de saturação*. Isto ocorre quando todos os eletrões emitidos chegam à placa A. A teoria TOR não explica porquê que $I=I_{1},I=I_{2}$ apresentam traçados diferentes.
**Gráfico 3** - Esta teoria não consegue explicar esta relação. Ela diz que o efeito deveria de ocorrer independentemente da frequência da radiação.

### TCR
- Nesta teoria temos que a energia de 1 fotão é $$E_\gamma=hf$$
- Temos que as colisões eletrão-fotão funcionam da seguinte forma: $\gamma+e^{-}_{ligado}=e^{-}_{livre}$, em que $e^{-}_{livre}$ terá uma energia total diferente da inicial.
- Temos: $I=\frac{\textsf{energia}}{\textsf{área}\times \textsf{tempo}}=\frac{\# \gamma hf}{\textsf{área}\times \textsf{tempo}}$

**Gráfico 1** - Aumentar $I$ aumenta o número de fotões incidentes, o que aumenta o número de colisões eletrão-fotão e o número de fotões libertados. Assim, $i$ aumenta com $I$ e verificasse o gráfico.
**Gráfico 2** - A TOR explica o formato geral do gráfico. A diferença entre os traçados correspondentes a $I_{1}>I_{2}$ são devidas a termos mais fotões e, portanto, mais eletrões a serem expelidos.
**Gráfico 3**:
    - Apliquemos conservação de energia à colisão eletrão-fotão: $$\begin{align*}
E_{\gamma}+E_{e^{-}_{ligado}}&= E_{e^{-}_{livre}}\\
hf + [\cancelto{\substack{em~repouso}}{E_{ce}}+\cancel{mc^{2}}+Be]&= E_{ce}' + \cancel{mc^{2}}\\
hf &= E_{ce}-Be
\end{align*}$$
    - Sendo que $Be$ é a energia de ligação do eletrão. Definimos então $\phi=-Be$, que é o *trabalho de extração do eletrão*. Assim: $hf=E_{ce}+\phi$
    - Apliquemos agora conservação de energia entre as placas A e C: $$\begin{align*}
E_{C}&= E_{A}\\
eV_{0} + \cancel{mc^{2}} &= E_{ce} + \cancel{mc^{2}}\\
eV_{0} &= E_{ce}
\end{align*}$$
    - Juntando as equações de $eV_{0}$ e de $hf$ acima temos: $$V_{0}= \frac{h}{e} (f-f_{0})$$

# 3 - Difusão de Compton
![[Colisão de fotão com eletrão no atomo.png|400]]  ![[I'(lambda ') para difusão de compton.png|385]]
- Consiste em ter um fotão a colidir com um eletrão livre, de forma que é libertado um fotão.

### TOR
- Neste teoria, a radiação incidente no eletrão seria do tipo $\vec{E}=\vec{E}_{0}\cos(\vec{k}\cdot \vec{r}-\omega t)$.
- Assim, temos $\vec{F}=-e \vec{E} \Rightarrow \vec{a}= \frac{-e\vec{E_{0}}}{m} \cos(\vec{k} \cdot \vec{r}-\omega t)$.
- Temos também a fórmula de Larmor não relativista: $P = \frac{2}{3}\frac{q^{2}a^{2}}{4\pi\varepsilon_{0}c^{3}}$
- Assim, a TOR não consegue explicar a ocorrência de difusões em que o fotão emitido após a colisão tem um comprimento de onda diferente do incidente ($\lambda'\ne \lambda$)

### TCR - Explicação de Compton
- Podemos descrever esta difusão como $$\gamma+e^{-}\to \gamma' + e^{-}$$
- Sendo $E_{\gamma},E_{e},p_{e}$ a energia e momento do fotão e eletrão antes da colisão e $E_{\gamma}',E_{e}',p_{e}'$ os mesmos após a colisão. Temos: 
    - $E_{\gamma}=p_{\gamma}c$ , $E_{e}=mc^{2}$ , $\vec{p_{e}}=\vec{0}$ (Aqui devesse notar que consideramos que, mesmo que o eletrão esteja num átomo, $Be\approx0$. Isto porque a energia de ligação será $\sim eV$, mas a energia do fotão será $\sim keV/MeV$)
    - $E_{\gamma}'=p_{\gamma}'c$ , $E_{e}'=\sqrt{p_{e}'c^{2}+m^{2}c^{4}}$

**Conservação Momento Linear**
- Temos $\vec{p}_{i}=\vec{p}_{f}$, o que nos dá: $\large \vec{p}_{e}'=\vec{p}_{\gamma}-\vec{p}_{\gamma}'$
- Se fizermos o produto escalar dos 2 lados da equação consigo próprio: 
$$p_{e}^{'~2}=p_{\gamma}^{2}+p_{\gamma}^{'~2}-2p_{\gamma}p~'_{\gamma}\cos \theta \tag{Eq. 1}$$

**Conservação de Energia**
- Temos $E_{i}=E_{f}\Longleftrightarrow E_{\gamma}+E_{e}=E_{\gamma}' + E_{e}'$
Assim:
$$\begin{align*}
\sqrt{p_{e}'^{~2}c^{2}+m^{2}c^{4}}&=p_{\gamma}c-p_{\gamma}'c+ mc^{2}\\
p_{e}^{'~2}c^{2}+\cancel{m_{e}^{2}c^{4}}&=p_{\gamma}^{2}c^{2}+p_{\gamma}^{'~2}c^{2}-2p_{\gamma}p~'_{\gamma}c^{2}+\cancel{m_{e}^{2}c^{4}}+2p_{\gamma}c \cdot m_{e}c^{2}-2p~'_{\gamma}c \cdot m_{e}c^{2} 
\end{align*}$$
Ao substituir $p_{e}'$ conforme a Equação 1 ficamos com: $2p_{\gamma}p_{\gamma}~'c^2(1-\cos\theta)=2m_{e}c^{3}(p_{\gamma}-p_{\gamma}~')$. Ao dividir isto por $2p_{\gamma}p_{\gamma}~'c^2$ ficamos com:
$1-\cos\theta=m_{e}c (\frac{1}{p_{\gamma}~'} - \frac{1}{p_{\gamma}})$.
- Temos que $E=pc=hf$, logo: $p= \frac{hf}{c}= \frac{h}{\lambda}$. Assim obtemos:
$$\lambda' = \lambda + \frac{h}{m_{e}c} (1-\cos\theta)$$
Ora, esta equação mostra-nos que é possível que a difusão ocorra com $\lambda'\ne \lambda$.
- Vemos ainda que se $\theta=0$ temos $\lambda'=\lambda$
- Se tivessemos $\theta\ne0$ poderíamos ter $\lambda'=\lambda$ na mesma. Isto porque na dedução acima consideramos que $Be=0$. Se considerarmos um eletrão muito próximo do núcleo, de tal forma que é como se o fotão colidisse com o núcleo em si, ficamos com $\lambda' = \lambda+\frac{h}{Mc}(1-\cos\theta)$, pelo que o segundo termo pode ser desprezável e ficamos com $\lambda'=\lambda$
$$\frac{h}{mc}= XXXXXXXXXXXXXX$$

# 4 - Raios X
![[Circuito de geração de raios X.png|450]]
- Filamento C aquece devido a tensão e liberta eletrões. Eles são acelerados por DDP elevada entre A e C. Ao colidirem com o ânodo A, é emitida radiação.
- Temos:
![[I(lambda) para raios X.png|450]]

### TOR
![[Eletrão a passar perto ao nucleo.png|400]]
- Temos que $F=ma=\frac{1}{4\pi\varepsilon_{0}} \frac{Ze^{2}}{r^{2}}$. Ou seja, $a\propto Z/r^{2}$. Vimos na fórmula de Larmor qye $P\propto a^{2}$.
- Ou seja, o cenário que temos aqui é o mesmo que descreve a radiação de Bremsstrahlung, cujo traçado coincide com o Espetro Contínuo da figura acima.
- Mas não conseguimos explicar o espectro Discreto nem o $\lambda_{min}$

### TCR
- A colisão que temos é:
$$e+\text{nuc}\to e' + \text{nuc}' + \gamma$$

**Conservação de Energia**
- Como o eletrão é acelerado por uma DDP = $V$, e sendo $m$ a massa do eletrão e $M$ a do protão, temos
$$\begin{align*}
E_{e}+E_{\text{nuc}}&=E_{e}~'+E_\text{nuc}~' + E_\gamma\\
&\downarrow\\
eV + \cancel{Mc^{2}} &= E_{e}~' + (\cancelto{\approx~0}{E_{c}}+ \cancel{Mc^{2}})+E_\gamma
\end{align*} $$
(aqui consideramos que a energia cinética do protão se mantém nula após colisão)
- Se assumirmos ainda que o eletrão perde toda a sua energia ao colidir com o ânodo, ou seja $E_{e}'=0$, ficamos com $$eV= \frac{hc}{\lambda}$$(de recordar que $E_{\gamma}=p_{\gamma}c=\frac{hc}{\lambda}$)
- Assim, explicamos a existência de $\lambda_{min}$ que será $$\lambda_{min}= \frac{hc}{eV}$$
# 5 - Produção de Pares
![[produçao de pares.png|450]]
- A maioria das partículas têm anti-partículas correspondentes. Eletrão - Positrão, Protão - Anti-Protão, etc. Estas são partículas com a mesma massa e spin, mas com carga de sinal oposto.

- Na **produção de pares** temos: $$\gamma \longrightarrow  \textsf{partícula} + \textsf{anti-partícula}$$
por exemplo: $\gamma\to e^{-}+e^{+}$ , $\gamma\to p + \bar p$

- Temos ainda a **aniquilação de pares**:
$$\textsf{partícula}+\textsf{anti-partícula}\longrightarrow \gamma, 2\gamma, 3\gamma \dots$$

## 5.1 - Produção de pares no vácuo
**Conservação de Energia**
- No vácuo, teríamos:
$$\begin{align*}
E_{\gamma}&= E_{-}+E_{+}\\
&= 2\gamma m_{e}c^{2} = hf = \frac{hc}{\lambda}
\end{align*}$$
em que consideramos o movimento relativista, com $m_{e}$ a massa de repouso do eletrão/positrão e $\gamma=1/\sqrt{1-(\frac{v}{c})^{2}}$ a constante de lorentz.

**Conservação de Momento Linear**
$$\vec{p}_{\gamma}=\vec{p}_{-}+\vec{p}_{+}$$
- Definimos $p_{-}=p_{+}=p$ e, ao considerar movimento apenas nos $xx$ temos:
$$\begin{align*}
\frac{h}{\lambda}&= 2p\cos\theta\\
\frac{h}{\lambda}&= 2\gamma m_{e}v\cos\theta\\
\frac{hc}{\lambda}&= 2\gamma m_{e}c^{2} \frac{v}{c}\cos\theta
\end{align*}$$
- O que é diferente da equação de $\frac{hc}{\lambda}$ que obtivemos através da conservação de energia. Ou seja, é preciso estar na presença de um *terceiro corpo* para que PP ocorra.

## 5.2 - Energia Mínima / Limiar
### 5.2.1 - Produção de Pares - PP
$$\gamma\to e^{-}+e^{+}$$
- Através da conservação de energia temos:
$$\begin{align*}
E_{\gamma}+Mc^{2}&= E_{e^{-}}+E_{e^{+}}+E~'_{N}\\
E_{\gamma}+\cancel{Mc^{2}}&= (E_{c}^{-}+m_{e}c^{2})+(E_{c}^{+}+m_{e}c^{2})+(E_{c}^{N}+\cancel{Mc^{2}})
\end{align*}$$
- Conseguimos concluir que a energia mínima para PP ocorrer será $E_{\gamma}=2m_{e}c^{2}$. Se considerarmos o referencial do CM, as energias do eletrão e positrão após a colisão irão anular-se na equação acima. Ora, a energia mínima será aquele em que obtemos $E_{c}^{N}=0$, ou seja:
$$E_{min}(PP) = 2m_{e}c^{2}= 1.022 \text{ MeV}$$

### 5.2.2 - Produção Tripleto - PT
- Consiste em ter $\gamma\to e^{-}+e^{+}$, na presença de um terceiro eletrão $e^{0}$.
- A dedução é mais longa e está na aula 4, pelo que:
$$E_{min}(PT)= 4m_{e}c^{2}= 2.044 \text{ MeV}$$

### 5.2.3 - Generalizado
- Se tivermos uma colisão:
$$1+2\to 3+4+5$$
- Temos $E^{2}-p^{2}c^{2}$, que é a **Invariante de Lorentz**, que tem o mesmo valor em todos os referenciais. Consideramos $S$ o ref do lab e $S'$ o ref do CM.
- Para usar isto, determinamos a invariante em 2 instantes e referenciais e igualá-mos os resultados obtidos (instante inicial no ref do lab e instante final no ref do CM, por exemplo).
- A dedução está na Aula 4 e temos:
$$E_{L}= \frac{(m_{3}+m_{4}+m_{5})^{2}c^{4}-m_{1}^{2}c^{4}-m_{2}^{2}c^{4}}{2m_{2}c^{2}}$$

# 6 - Coeficiente de Atenuação Linear
![[Fotão a colidir com parede.png|425]]
- Consideremos um feixe de $N_{0}$ fotões com energia $E_\gamma$ cada. Este está a incidir num alvo homogéneo de espessura $L$.
- Definimos então $\mu$, o *coeficiente de atenuação linear* que é a probabilidade de o fotão sofrer uma interação, por unidade de comprimento no meio/alvo.

- Numa secção de espessura $dx$, o número de eletrões que sofrem interações será $N(x)\mu dx$. Ora, estes fotões deixarão de fazer parte do feixe. Ou seja, a variação do número de eletrões do feixe numa secção de espessura $dx$ será dada por:
$$\begin{align*}
N(x)-N(x+dx)&= N(x)\mu dx\\
&\downarrow\\
N(x)&= N_{0} e^{-\mu x}
\end{align*}$$
- Ou seja, o número de eletrões (do feixe inicial) que sofrem alguma interação será: $N(0)-N(L)=N_{0}-N_{0}e^{-\mu L}$

# 7 - Secção Eficaz
- Consideremos um feixe de fotões com a mesma energia a incidir perpendicularmente com um alvo muito fino de área $A$. 
- No alvo há um orifício de área $\sigma$. A probabilidade de 1 partícula atravessar este orifício será: $\sigma/A$

- Daqui a diante, 
    - $a$ - número de projeteis
    - $v_{a}$ - velocidade das partículas $a$
    - $n_{a}$ - densidade do feixe de partículas $a$
    - $b$ - número de alvos
    - $n_{b}$ - densidade volúmica de alvos
    - $A,d$ - área e espessura do alvo

- Temos que o número de algos será $N_{b}=n_{b}Ad$.
- Consideremos o acontecimento: uma partícula $a$ passar por um dos orifícios $b$. Vemos que:
$$\begin{align*}
\frac{\textsf{\# de acontecimentos}}{1s}&= \frac{\textsf{\# de partículas}}{1s}\times N_{b} ~\times \textsf{Prob de 1 acontecimento}\\
\frac{\textsf{\# de acontecimentos}}{1s}&= \frac{\textsf{\# de partículas}}{1s}\times N_{b} ~\times \frac{\sigma}{A}\\
\frac{\textsf{\# de acontecimentos}}{1s} &= \Phi_{a}~N_{b}~\sigma
\end{align*}$$
em que $\Phi_{a} = \frac{\textsf{\# de partículas}}{\textsf{tempo . área}}=v_{a}n_{a}$

- Ou seja, tal como tínhamos acima no caso de um alvo com 1 orifício de área $\sigma$, aqui temos que a probabilidade de 1 acontecimento (1 partícula atravessar 1 orificio) continua a ser $\sigma/A$. Ou seja, $\sigma$ é a área do alvo equivalente a juntar todos os orifícios que as partículas *podem* atravessar num só, de tal modo que:
$$\sigma = \text{Secção Eficaz}=\frac{\textsf{\# de acontecimentos por unidade de tempo}}{\Phi_{a}~N_{b}}$$
ou seja, a secção eficaz representa uma espécie de área em que há probabilidade de um certo acontecimento acontecer.

# 8 - Modelos do Átomo
## 8.1 - Modelo de Thomson (Pudim de Passas)
**Limitações**
    - O átomo não seria estável
    - Não explica os espetros atómicos observados impiricamente. De acordo com este modelo, apenas existiria 1 risca.
    - Não explica difusão de partículas em ângulos grandes (Experiência de Rutherford)

### 8.1.1 - Experiência de Rutherford
Consiste em estudar o ângulo de difusão das partículas alpha de um feixe quando este embate numa placa de ouro.
![[Modelo thomson.png]]
Para o modelo de Thomson, teríamos
$$\begin{align*}
F=\frac{dp}{dt} &\longrightarrow \Delta p=F \Delta t\\
\Delta p_{y}&= F_{y}\Delta t\\
&= \frac{q_{\alpha}q_{N}}{4\pi \varepsilon_{0}R^{2}} \cdot \frac{R}{v} \\
&= \frac{q_{\alpha}q_{N}}{4\pi \varepsilon_{0}vR}
\end{align*}$$
Ou seja: $\tan\theta = \dfrac{P_{y}}{P_{x}} = \dfrac{\dfrac{q_{\alpha}q_{N}}{4\pi \varepsilon_{0}vR}}{m_{\alpha}v}$
- Daqui temos que, neste modelo, o ângulo médio de difusão após de 1 colisão é $\overline \theta\simeq 0.01\degree$.
- Assim, apliquemos o modelo de Thomson à experiência de Rutherford. 
- Ao percorrer a placa de ouro a partícula alfa sofre $N$ colisões. Assim, considerando que experimentalmente se verificou que uma partícula sofre uma difusão total de $100\degree$. Temos:$\sqrt{N}\cdot0.01=10^{2}\Longrightarrow N=10^{8}$
- No entanto, a probabilidade de todas estas difusões ocorrerem no mesmo sentido é: $$P= \left(\frac{1}{2} \right)^{N}=2^{-100~000~000}\simeq0$$
AKA impossível.

## 8.2 - Modelo de Rutherford (Modelo Planetário)
- Consideremos a experiência de Rutherford analisada conforme este modelo. Temos uma partícula alfa a incidir numa placa de ouro.
![[colisao thomson.png]]
- Temos que $b$ é o parâmetro de impacto. $\varphi$ é o ângulo de difusão - ângulo variante entre o eixo horizontal e a linha núcleo-eletrão.
- Temos:
$$\frac{1}{r}=\frac{1}{b}\sin \varphi + \frac{D}{2b^{2}}(\cos\varphi-1)$$
sendo $D$ a distância de maior aproximação ao núcleo na trajetória do projétil.
- Através da conservação de energia e momento angular temos:
$$D = \frac{1}{4\pi \varepsilon_{0}} \frac{q_{\alpha}q_{N}}{E_{c}}$$

### 8.2.1 - Parâmetro de Impacto e ângulo de difusão
- No final do movimento temos $\varphi=\pi-\theta~,~~ r\to\infty$
- Ao substituir $r=\infty,\varphi=\pi-\theta$ na equação de $\frac{1}{r}$ acima ficamos com
$$b= \frac{D}{c}\cot \frac{\theta}{2}=\frac{q_{\alpha}q_{N}}{8E_{c}\pi\varepsilon_{0}}\cot \frac{\theta}{2} \tag{Eq. 2}$$
### 8.2.1 - Difusão superior a um ângulo $\theta$
![[experiencia thomson.png]]
- Consideremos que o alvo é uma placa de ouro com 1 átomo de espessura. Teríamos algo como na figura acima. Cada átomo é um círculo de raio $\pi R^{2}$
- Para um projetil ser difundido com ângulo $\ge \theta$, é preciso que o parâmetro de impacto seja $\le b$. Ou seja, na figura acima, a partícula alfa tem que incidir algures num círculo de raio $b$.

- Consideremos agora que se tem uma placa de espessura $t$, área $A$, densidade $\rho$ e composta por um material com massa molar $M$. 
- O número de moles de átomos de ouro na placa será $\frac{m}{M}=\frac{\rho At}{M}$. 
- O número de átomos por unidade de volume na placa será: $n=N_{A}\cdot \frac{\rho At}{M}\cdot \frac{1}{At}=\frac{N_{A}~\rho}{M}$
- Assim, se considerarmos uma área transversal $a$ temos que o número de átomos de ouro nela será $na=\dfrac{N_{A}\rho a}{M}$ 
- Assim, considerando estes átomos de ouro na área $a$ e os projeteis distribuidos uniformemente, a porção de átomos com difusão $\ge \theta$ será:
$$f_{\le b}=f_{\ge \theta}=na\pi b^{2}$$

### 8.2.2 - Fórmula de Difusão de Rutherford
- As partículas que terão um ângulo de difusão no intervalo $[\theta,\theta+d\theta]$ serão aquelas que têm um parâmetro de impacto $[b,b+db]$. Assim, da equação acima temos $df=na \cdot 2\pi b~db$
- Ao derivar a Eq.2 (equação de $b$ que obtivemos acima) temos: $db = \frac{q_{\alpha}q_{N}}{8E_{c}\pi\varepsilon_{0}}\left(-\csc^{2}\left(\frac{\theta}{2}\right)\right)\left(\frac{1}{2}d\theta \right)$
- Ao juntar as 2 eqs acima temos: $|df|=\pi n a \left( \frac{q_{\alpha}q_{N}}{8E_{c}\pi\varepsilon_{0}}\right)^{2} \csc^{2} \frac{\theta}{2}\cot \frac{\theta}{2} d \theta$
- Podemos escrever $q_{\alpha}=z \cdot e$, $q_{N}=Z \cdot e$, sendo $z,Z$ os números atómicos do projétil e núcleo e $e=1.6\cdot10^{-19}~C$ a carga unitária. Assim, temos que $\large \frac{e^{2}}{4\pi\varepsilon_{0}}=1.44 eV \cdot nm$ e podemos reescrever a equação acima:
$$|df|=\pi n a \left(\frac{zZ}{2E_{c}}\right)^{2}\left(\frac{e^{2}}{4\pi\varepsilon_{0}}\right)^{2} \csc^{2} \frac{\theta}{2}\cot \frac{\theta}{2} d \theta$$
- Consideremos agora que temos um detetor correspodente a um intervalo $d\theta$
![[difusao rutherford.png]]
- A probabilidade de o projetil ser difundido e passar no detetor está relacionada à probabilidade de ele ser difundido e passar num anél de raio interno $r\sin\theta$ e espessura $rd\theta$. A unidade de área do anel será $dA=2\pi r \sin\theta \cdot rd\theta$.
- A probabilidade de um projetil passar num unidade de área do anel será $N(\theta)=\frac{|df|}{dA}$. Assim temos:
$$N(\theta) = \frac{na}{4r^{2}} \left(\frac{zZ}{2E_{c}}\right)^{2} \left(\frac{e^{2}}{4\pi\varepsilon_{0}}\right)^{2} \frac{1}{\sin^{4} \frac{\theta}{2}}=\frac{d \sigma}{d \Omega}$$
AKA **Fórmula da Difusão de Rutherford** aka derivada da secção eficaz no ângulo sólido.

### 8.2.3 - Estabilidade do Átomo de Rutherford
- Este átomo não seria estável. 
    - Se os eletrões estivessem em repouso, iriam acabar por cair para o núcleo. Isto não é o caso, porque os átomos seriam muito menores. 
    - Os eletrões podem ainda circular como planetas. Mas nesse caso eles teriam aceleração, pelo que iriam emitir radiação e, assim perder energia. Ou seja, os eletrões cairiam para o núcleo.

## 8.3 - Modelo de Bohr
- Os átomos circulam em orbitas circulares. Temos as equações, cujas deduções estão na aula 8:
$$\begin{align*}
&\textsf{Energia emitida: } &|E_{f}-E_{i}|\\
&\textsf{Velocidade:} &v_{n}= \frac{1}{4\pi\varepsilon_{0}} \frac{Ze^{2}}{n\hbar}\\
&\textsf{Raio:} &r_{n}= 4\pi \varepsilon_{0} \frac{n^{2}\hbar^{2}}{mZe^{2}}\\
&\textsf{Energia:} &E_{n}= \left(\frac{1}{4\pi \varepsilon_{0}}\right)^{2} \frac{mZ^{2}e^{4}}{4\pi\hbar^{3}}  \frac{1}{n^{2}}
\end{align*}$$
### 8.3.1 - Transições de níveis
- A energia de um fotão é $E=hf$. A frequência de um fotão emitido numa transição de um nível $n_{i}$ para um nível $n_{f}$ será: $f = \frac{E_{i}-E_{f}}{h}= \left(\frac{1}{4\pi \varepsilon_{0}}\right)^{2} \frac{mZ^{2}e^{4}}{4\pi\hbar^{3}} \left(\frac{1}{n_{f}^{2}} - \frac{1}{n_{i}^{2}} \right)$
- O espectro é:

| Série    | $1/\lambda$                                              | Radiação |
| -------- | -------------------------------------------------------- | -------- |
| Lyman    | $\frac{1}{\lambda}=R(\frac{1}{1^{2}}-\frac{1}{n^{2}})~~,~~n=2,3 ...$   | UV       |
| Balmer   | $\frac{1}{\lambda}=R(\frac{1}{2^{2}} - \frac{1}{n^{2}})~~,~~n=3,4 ...$ | UV       |
| Paschen  | $\frac{1}{\lambda}=R(\frac{1}{3^{2}} - \frac{1}{n^{2}})~~,~~ n=4,5 ...$ | IV       |
| Brackett | $\frac{1}{\lambda}=R(\frac{1}{4^{2}} - \frac{1}{n^{2}})~~,~~ n=5,6 ...$ | IV       |
| Pfund    | $\frac{1}{\lambda}=R(\frac{1}{5^{2}} - \frac{1}{n^{2}})~~,~~ n=6,7 ...$ | IV       |

### 8.3.2 - Espetro de Absorção
- Ver ponto 2 da aula 9

### 8.3.3 - Sistema de 2 partículas
- Não há de ser muito importanteeeeee

--- Fim deste resumo. Já me lembro da matéria a partir daqui e acho q os resumos estão slay ---