- O trabalho de Maxwell leva a acreditar que a luz é um fenómeno eletromagnético.
- No entanto, mais recentemente verifficou-se que na realidade a luz tem um comportamento corpuscular, que ocorre a partir de *fotões*, partículas elementares com energia e sem massa.
- No entanto, a natureza quântica da luz nem sempre é útil em Ótica. Muitas vezes simplesmente é impossível distinguir fotões, devido ao equipamento usado.
- Quando o tamanho dos equipamentos/instrumentos é muiiiiito maior que o comprimento de onda da luz, podemos usar *Ótica Geométrica*, a aproximação mais simples.
- Quando o equipamento é mais pequeno, temos a **Física Ótica**, que é mais precisa. Nesta, a onda comporta-se maioriatariamente como uma onda, pelo que muitas vezes nem é preciso distinguir o tipo de onda: basta tratar a luz como *uma* onda eletromagnética.

- Como vimos em Mecânica Quântica, a teoria quântica declara que a luz E a matéria têm uma dualidade onda-partícula. Ora, para partículas materiais a equação que define o seu estado de onda é a Equação de Schrödinger. Já para a luz, o seu comportamento ondulatório é descrito pelo Eletromagnetismo Clássico: as **Equações de Maxwell**.
- Na luz, a dualidade onda-partícula ocorre assim:
    - Quando uma onda se move no espaço, atravessa fendas ou lentes, comporta-se de forma *ondulatória*
    - Quando sofre absorção ou emissão (processos que exigem transferências de energia radiante) comporta-se de forma corpuscular : transferências de enrgia ocorrem por fotões, não de forma contínua, com ondas.

- Dito isto, em regra geral, podemos considerar a luz como sendo uma onda eletromagnética; mas sem esquecer que na realidade é constituida por fotões.

## 3.1 - Leis de Eletromagnetismo
- Temos que uma partícula no espaço submersa num campo elétrico $\vec{E}$ é sujeita a uma força elétrica $\vec{F}_{E}=q \vec{E}$.
- Se a partícula estiver em movimento a velocidade $\vec{v}$, temos ainda a força magnética $\vec{F_{M}}=q \vec{v}\times \vec{B}$ em que $\vec{B}$ é o campo de indução magnética.
- Assim, se ambas as forças estiverem presentes temos a *força de Lorentz* : $\vec{F}=q \vec{E}+q \vec{v}\times \vec{B}$.

### 3.1.1 - Lei da Indução de Faraday
- Através de experiências, Faraday percebeu que um campo magnético a variar perto de fios/cabos, gera neles uma corrente elétrica. 
- Ao fazer passar um íman por uma bobina, ele verificou que se gerava uma DDP nos terminais da bobina. Esta DDP é conhecida por *força eletromotriz* (EMF) induzida (de notar que, apesar o nome, *não* é uma força, mas sim uma voltagem). Mais especificamente, a velocidade com que o íman é movido influencia a intensidade da EMF gerada - a amplitude da EMF depende da "velocidade" de variação de $B$ na bobina ($\Delta B/\Delta t$), não da intensidade de $B$ (um campo fraco a variar muito rápido pode gerar mais EMF que um campo forte a variar lentamente)

![[fluxo magnetico.png]]
- Se tivermos algo como na figura acima, em que o campo varia da mesma forma nos dois aneis condutores, a EMF será *mais forte no anel maior*. Ou seja, a EMF é proporcional à área $A$ do anel (perpendicular ao campo). 
- Por outro lado, se o anel estiver inclinado teremos uma EMF menor:
![[fluxo mag angulo.png]]
pelo que varia com $A\cos \theta$. Ora, se tivermos um campo magnético uniforme, é natural concluir que teremos EMF se a área perpendicular a este variar ($\Delta A_{\perp}/\Delta t$)

- Juntando os 2 casos que vimos acima temos:
$$\begin{align*}
A_{\perp}=\text{constante} ~~~~;~~~~ \text{emf}\propto A_{\perp} \frac{\Delta B}{\Delta t}\\
B=\text{constante} ~~~~;~~~~ \text{emf}\propto B \frac{\Delta A_{\perp}}{\Delta t}
\end{align*}$$

- Ou seja, deveremos conseguir definir uma grandeza que consista no produto do campo $B$ com a área $A_\perp$ e que indique o EMF. Essa grandeza é o **Fluxo do Campo Magnético**:
$$\Phi_{M}=B_{\perp}A=BA_{\perp}=BA\cos\theta$$
ou, na forma integral e mais comum:
$$\Phi_{M}= \iint_{\mathcal{S}} \vec{B}\cdot d \vec{s}$$
(em que $d \vec{s}$ é perpendicular à superfície e aponta para fora)

- A EMF é portanto o resultado da forma como o fluxo varia no tempo (como vimos atrás, proporcional à variação de $B$ ou $A_{\perp}$ no tempo) e temos:
$$\text{emf}=\varepsilon=- \frac{d \Phi_{M}}{dt} \quad \quad \quad \quad (\textsf{para 1 anel})$$
o sinal é negativo, porque o EMF gera uma corrente, que gera um campo magnético que "tenta" anular o campo magnético original. Se o EMF tivesse o mesmo sinal que a variação do fluxo, teríamos um aumento de campo infinito.

- Na definição mais simples (12º ou 11º), a força eletromotriz é trabalho por unidade de carga. Ou seja: $[\varepsilon]=\frac{[W]}{[Q]}=\frac{[F]\cdot[d]}{[Q]}\to [E]\cdot[d]$. Podemos escrever:
$$\varepsilon=\oint_\mathcal{P} \vec{E}\cdot d \vec{\ell}$$
(em que o percurso fechado $\mathcal{P}$ corresponde ao anel dos casos acima)

- Igualando as 2 definições de $\varepsilon$ temos:
$$\begin{align*}
\oint_\mathcal{P}\vec{E}\cdot d \vec{\ell}&= - \frac{d}{dt} \Phi_{M}\\
&= - \frac{d}{dt} \iint_{\mathcal{S}} \vec{B}\cdot d \vec{s}
\end{align*}$$
e temos a **Lei de Faraday Integral**:
$$\oint_\mathcal{P}\vec{E}\cdot d \vec{\ell}=-\iint_\mathcal{S} \frac{\partial\vec{B}}{\partial t}\cdot d \vec{s}\tag{Eq. 1}$$
em que, se usarmos o teorema de Stokes no termo do campo elétrico ficamos com:
$$\iint_\mathcal{S}(\nabla \times \vec{E}) \cdot d \vec{s}=-\iint_\mathcal{S} \frac{\partial\vec{B}}{\partial t}\cdot d \vec{s}
$$
de onde resulta a versão da **Lei de Faraday Diferenicial** que temos nas Equações de Maxwell: $$\nabla \times \vec{E}= - \frac{\partial\vec{B}}{\partial t}\tag{Eq.2}$$

### 3.1.2 - Lei de Gauss - Elétrica
- Relaciona o fluxo de campo elétrico com o fluxo de carga.
- Tal como fizemos para o campo magnético, podemos definir o fluxo elétrico:
$$\Phi_{E}=\oint_\mathcal{S} \vec{E}\cdot d \vec{s}$$
- Ora, se não tivermos cargas dentro da superfície fechada $\mathcal{S}$ então o fluxo elétrico é nulo. 
    - Isto é comparável a ter um fluído a escoar: Se considerarmos uma superfície fechada dentro dele, não teremos nenhum fluxo de fluido (no total da superficie). Apenas teremos um fluxo não nulo se tivermos uma fonte ou "furo" de fluido dentro dessa superfície. 

- Consideremos uma carga $q$. Queremos saber o fluxo elétrico através de uma superfície esférica de raio $r$ centrada em $q$. O campo será então perpendicular à superfície e a apontar para fora em todos os pontos. Ou seja:
$$\Phi_{E}=\oint_\mathcal{S}\vec{E}\cdot d \vec{s}=E\oint_\mathcal{S}ds=E4\pi r^{2}$$
Temos ainda a Lei de Coulomb, que nos diz que o campo gerado por uma carga pontual em função da distância a esta é:
$$E=\frac{1}{4\pi\varepsilon_{0}} \frac{q}{r^{2}}$$
e juntando as 2 equações acima temos:
$$\Phi_{E}=\frac{q}{\varepsilon_{0}}$$
, o fluxo elétrico gerado por uma carga pontual.

- Assim, é natural concluir que o fluxo de $N$ cargas numa superfície fechada será $\Phi_{E}=\frac{1}{\varepsilon_{0}}\sum\limits^{N}q$ 
- Assim, podmeos generalizar para $N\to\infty$ cargas e obtemos a **Lei de Gauss integral**:
$$\oint_\mathcal{S} \vec{E}\cdot d \vec{s}=\frac{1}{\varepsilon_{0}}\iiint_\mathcal{V} \rho ~d^{3}r\tag{Eq.3}$$
usando o teorema de gauss no termo com o campo elétrico obtem-se:
$$\iiint_\mathcal{V}\nabla \cdot \vec{E}~d^{3}r=\frac{1}{\varepsilon_{0}}\iiint_\mathcal{V}\rho~d^{3}r$$
- Isto dá-nos a **Lei de Gauss Diferencial**:
$$\nabla \cdot \vec{E}=\frac{\rho}{\varepsilon_{0}}\tag{Eq.4}$$

#### Permitividade
$$\varepsilon_{0}=8.8542 \cdot 10^{-12}~C^{2}/Nm^{2}$$
- Podemos interpretar este valor como o quanto o vácuo ou outro meio (se tivermos $\varepsilon$) "permite" a passagem e existência de campo elétrico.
- Assim, torna-se útil definir a *permitividade relativa*:
$$\varepsilon_{r}=\frac{\varepsilon}{\varepsilon_{0}}$$

### 3.1.3 - Lei de Gauss - Magnética
- Não existem monopolos/cargas magnéticas. Assim, não temos em momento algum o campo magnético a divergir de um ponto.
- Assim, é evidente que para o campo magnético a Lei de Gauss toma a forma:
$$\Phi_{M}=\oint_\mathcal{S}\vec{B}\cdot d \vec{s}=0\tag{Eq.5}$$
isto faz sentido, considerando a 2ª equação de Maxwell: $$\nabla \cdot \vec{B}=0\tag{Eq.6}$$

### 3.1.4 - Lei de Circuitos de Ampere
![[campo mag linha corrente.png]]
- Consideremos um fio reto com corrente $I$ no vácuo. Empiricamente foi determinado que o campo gerado por um fio assim, a uma distância $r$ dele (ver figura acima) é:
$$B=\frac{\mu_{0}I}{2\pi r}$$

- Ora, vamos **_==imaginar==_** que existem cargas magnéticas $q_m$. Consideremos que esta carga fica sob o efeito de uma força $q_{m}\vec{B}$ quando sujeita a um campo $\vec{B}$.
- Consideremos que essa carga é movida em torno do fio com corrente $I$, no percurso circular representado na figura acima. Vejamos qual o trabalho necessário para mover a carga assim.
- Dividimos o percurso em secções $\Delta \ell$. Ora, em cada secção a força será $q_{m}\vec{B}$ e o trabalho será $$\Delta \vec{W}=q_{m} \vec{B}\cdot \Delta \vec{\ell}\to \Delta W=q_{m}B_{\parallel}\Delta \ell$$
- Temos que o campo tem direção $\hat{\phi}$ (azimutal), ou seja, ele é tangente ao percurso traçado em todos os pontos. Ou seja, $B_{\parallel}=B=\mu_{0}I/2\pi r$. Neste percruso (que tem raio $r$ constante) temos até que o campo é igual em módulo todos os pontos.
- O trabalho total em 1 volta deste percurso será:
$$W= \sum\limits q_{m}B \Delta \ell=q_{m} B\sum\limits \Delta \ell=q_{m}B \cdot 2\pi r$$
se substituirmos $B$ obtemos:
$$W= q_{m} \frac{\mu_{0}I}{2\pi r}2\pi r =q_{m}\mu_{0}I$$
e vemos que ele *não* depende da distância ao fio. 

- Podemos então escrever:
$$q_{m}\sum\limits B_{\parallel} \Delta l =q_{m} \mu_{0}I \to \sum\limits B_{\parallel}\Delta \ell=\mu_{0}I$$
ora, enquanto que a equação acima é específica para o percurso da figura, ao não substituir $B_{\parallel}=B$ obtivemos uma expressão que é válida para *qualquer percurso*  fechado em torno de uma *corrente qualquer*. Além disso, a carga despareceu, pelo que a equação ja não é teórica ou fictícia.

- Ora, se tivermos mais que uma corrente a passar no percurso, os seus campos apenas se irão sobrepor e temos: $$\sum\limits B_{\parallel}\Delta \ell=\mu_{0}\sum\limits I\longrightarrow_{(\Delta\to0)} \oint_\mathcal{P}\vec{B}\cdot d \vec{\ell}=\mu_{0}\sum\limits I$$
- Podemos generalizar para quando a corrente tem densidade não uniforme, usando o vetor densidade de corrente $\mathcal{\vec{J}}$ e temos $$\oint_\mathcal{P}\vec{B}\cdot d \vec{\ell}=\mu_{0}\iint_\mathcal{S} \vec{\mathcal{J}}\cdot d \vec{s}\tag{Eq.7}$$

#### Permeabilidade 
$$\mu_{0}=4\pi \cdot 10^{-7} N s^{2}/C^{2}$$
- Novamente, num meio não-vácuo temos a permeabilidade relativa: $$\mu_{r}=\frac{\mu}{\mu_{0}}$$

#### Velocidade da Luz
- Temos então a permeabilidade e a permitividade definidas. É útil saber que elas se relacionam da seguinte forma:
$$\varepsilon_{0}\mu_{0}=\frac{1}{c^{2}} \quad \quad \quad;\quad \quad \quad (c\approx 3\cdot10^{8}m/s)$$

- Voltemos à Equação 7. Ela é frequentemente suficiente, mas há casos em que dá resultados errados. Consideremos um sistema como o abaixo (carregamento de um condensador):
![[fluxo mag por linha + condensador.png]]
- Ora, a equação que obtivemos não depende da área, desde que seja limitada pelo percurso $\mathcal{P}$ ($C$ na figura acima). Ora, podemos então definir as áreas $A_{1},A_{2}$ e a eq.7 deverá ser verdade em ambas.
    - Para a área $A_{1}$, temos uma corrente $i$ a passar nela, pelo que os lados da Eq. 7 são não nulos e deveremos obter algo correto.
    - Para a área $A_{2}$, porque ela apenas engloba a placa do condensador, temos que $\int_{A_{2}}\vec{\mathcal{K}}\cdot d \vec{s}=0$, pelo que o campo no percurso $C$ terá que ser 0.
- Ou seja, para 2 área diferentes definidas pelo mesmo percurso limite, obtemos 2 campos diferentes, com o mesmo sistema físico. Isto está obviamente errado.

- Isto ocorre porque até aqui presumimos que correntes AKA cargas em movimento são a única fonte de campo magnético.
- Aliás, num sistema como este, o campo magnetico entre as placas e no fio deverá ser o mesmo (para uma mesma distância ao centro).
- Se a área das placas for $A$ temos $$E=\frac{Q}{\varepsilon A}\to \varepsilon E=\frac{Q}{A}\longrightarrow \varepsilon \partial_{t}E=\frac{i}{A}$$
em que Maxwell definiu a *densidade de corrente de deslocamento*:
$$\vec{\mathcal{J}}_{D}\equiv \varepsilon \frac{\partial \vec{E}}{\partial t}$$
e agora sim temos a **Lei de Ampere-Maxwell**:
$$\oint_\mathcal{P}\vec{B}\cdot d \vec{\ell}=\mu \iint_\mathcal{S} \left(\vec{\mathcal{J}} + \varepsilon\frac{\partial \vec{E}}{\partial t}\right)\cdot d \vec{s}$$
que nos dá que quando temos um campo elétrico a variar no tempo gera-se um campo magnético.

### 3.1.5 - Equações de Maxwell
- Ao longo desta secção fomos obtendo as equações de maxwell integrais.
- Se considerarmos que não há correntes nem cargas no espaço ($\rho=0,\vec{\mathcal{J}}=\vec{0}$), temos:
$$\boxed{\begin{align*}
\oint_\mathcal{P} \vec{E}\cdot d \vec{\ell}&= -\iint_\mathcal{S} \frac{\partial \vec{B}}{\partial t}\cdot d \vec{s}\\
\oint_\mathcal{P}\vec{B}\cdot d \vec{\ell}&= \mu_{0}\varepsilon_{0}\iint_\mathcal{S}\frac{\partial \vec{E}}{\partial t}\cdot d \vec{s}\\
\oint_\mathcal{S} \vec{B}\cdot d \vec{s}&= 0\\
\oint_\mathcal{S} \vec{E}\cdot d \vec{s}&= 0
\end{align*}}$$
- Vemos que as equações dos 2 campos são quase simétricas e que eles se afetam mutuamente.
- Podemos ainda escrever na forma diferencial:
$$\boxed{\begin{align*}
\nabla \cdot \vec{E}&= \frac{\rho}{\varepsilon_{0}}\\
\nabla \cdot \vec{B}&= 0\\
\nabla \times \vec{B}&= \mu_{0}\vec{\mathcal{J}} + \varepsilon_{0}\mu_{0} \partial_{t}\vec{E}\\
\nabla \times \vec{E}&= - \partial_{t}\vec{B}
\end{align*}}$$

## 3.2 - Ondas Eletromagnéticas
### 3.2.0 - Dedução da Equação de Onda e Significado Físico
- Consideremos um campo elétrico num meio dielétrico com polarização $\vec{P}$. Temos:
$$\vec{D}=\varepsilon_{0}\vec{E}+\vec{P}$$em que $\vec{D}$ é o vetor deslocamento, que nos indica como seria o campo nesta região se não houvesse dielétrico.
- Se tivermos um dielétrico linear, istotrópico e homogénio temos que $\vec{P}\parallel \vec{E}$ e $P\propto E$. E temos:
$$\vec{D}=\varepsilon \vec{E}$$

- Agora, o campo magnético. Ao termos um dielétrico, temos *magnetização* ($M$) (contrariamente à polarização para o caso elétrico). Assim, temos o vetor de intensidade do campo magnético:
$$\vec{H}=\frac{\vec{B}}{\mu_{0}}-\vec{M}$$
em que se o dielétrico for linear, homogénio e isotrópico temos:
$$\hat{H}=\frac{\vec{B}}{\mu}$$
- Temos ainda a *Lei de Ohm*, que nos diz que: $$\vec{\mathcal{J}}=\sigma \vec{E}$$
(em que $\sigma$ é a condutividade do meio)

- Recordemos as equações de maxwell diferenciais:
$$\boxed{\begin{align*}
\nabla \cdot \vec{E}&= \frac{\rho}{\varepsilon_{0}}\\
\nabla \cdot \vec{B}&= 0\\
\nabla \times \vec{B}&= \mu_{0}\vec{\mathcal{J}} + \varepsilon_{0}\mu_{0} \partial_{t}\vec{E}=\mu_{0}\sigma \vec{E}+\varepsilon_{0}\mu_{0}\partial_{t}\vec{E}\\
\nabla \times \vec{E}&= - \partial_{t}\vec{B}
\end{align*}}$$

**Campo Magnético**
- Façamos o rotacional dos 2 lados da 3ª equação:
$$\begin{align*}
\nabla \times (\nabla \times \vec{B})&= \mu \sigma (\nabla \times \vec{E}) + \mu \varepsilon \partial_{t}(\nabla \times \vec{E})\\
&= -\mu \sigma \partial_{t}\vec{B}- \mu \varepsilon \partial_{t}^{2}\vec{B}
\end{align*}$$
(em que usamos a 4ª equação na transição para substituir $\nabla \times \vec{E}$)
- Mas temos ainda a indentidade de cálculo: $$\nabla \times(\nabla \times)=\nabla (\nabla \cdot) - \nabla^{2}$$
ou seja: $$\nabla \times (\nabla \times \vec{B})= \nabla (\nabla \cdot \vec{B}) - \nabla^{2}\vec{B}=- \nabla^{2} \vec{B}$$(pois a divergência do campo magnético é 0, pela 2ª equação de Maxwell)
igualando as 2 equações temos:
$$\nabla^{2}\vec{B}=\mu \varepsilon \partial^{2}_{t}\vec{B}-\mu \sigma \partial_{t}\vec{B}\tag{Eq.8}$$

**Campo Elétrico**
- Façamos então o rotacional dos 2 lados da 4ª equação:
$$\begin{align*}
\nabla \times (\nabla \times \vec{E})&= - \partial_{t}(\nabla \times \vec{B})\\
&= - \mu \sigma \partial_{t}\vec{E}- \mu \varepsilon \partial_{t}^{2}\vec{E}
\end{align*}$$
(em que usamos a 3ª equação na transição para substituir $\nabla \times \vec{B}$)
- Novamente, usamos a identidade $\nabla \times(\nabla \times)=\nabla (\nabla \cdot) - \nabla^{2}$ conseguimos obter:
$$\begin{align*}
\nabla \times (\nabla \times \vec{E})=\nabla (\nabla \cdot \vec{E}) - \nabla^{2}\vec{E}&= \nabla\left(\frac{\rho}{\varepsilon_{0}}\right)-\nabla^{2} \vec{E}
\end{align*}$$
(em que se usou a lei de gauss diferencial para substituir $\nabla \cdot \vec{E}$)
- Juntando as 2 equações de $\nabla \times (\nabla \times \vec{E})$ temos:
$$\nabla^{2}\vec{E}-\mu \varepsilon \partial_{t}^{2}\vec{E}-\mu \sigma \partial_{t} \vec{E}=\nabla \left(\frac{\rho}{\varepsilon_{0}}\right)$$
e temos, num meio sem carga:
$$\nabla^{2}\vec{E}=\mu \varepsilon \partial_{t}^{2}\vec{E}+\mu \sigma \partial_{t} \vec{E}\tag{Eq.9}$$

**Combinar os campos**
- Assumindo um meio não condutor $\sigma=0$, as equações 8 e 9 ficam na forma:
$$\begin{align*}
\nabla^{2}\vec{B}&= \mu \varepsilon \partial_{t}^{2}\vec{B}\\
\nabla^{2}\vec{E}&= \mu \varepsilon \partial_{t}^{2}\vec{E}
\end{align*}$$
- Sendo que assim:
$$\begin{align*}
\vec{H}=\frac{1}{\mu}\vec{B} ~~\to~~ \nabla^{2}\vec{H}&= \mu \varepsilon \partial_{t}^{2}\vec{H}\\
\vec{D}=\varepsilon\vec{E} ~~\to~~ \nabla^{2}\vec{D}&= \mu \varepsilon \partial_{t}^{2}\vec{D}\\
\end{align*}$$
- Se por fim introduzirmos ainda a condição de estarmos no vácuo ($\varepsilon_{r}=\mu_{r}=1$) temos:
$$\nabla^{2}\vec{E}= \mu_{0}\varepsilon_{0} \frac{\partial^{2}\vec{E}}{\partial t^{2}}= \frac{1}{c^{2}} \frac{\partial^{2}\vec{E}}{\partial t^{2}}$$
$$\nabla^{2}\vec{B}= \mu_{0}\varepsilon_{0} \frac{\partial^{2}\vec{B}}{\partial t^{2}}= \frac{1}{c^{2}} \frac{\partial^{2}\vec{B}}{\partial t^{2}}$$
aka **Equações de Onda de Ondas Eletromagnéticas**.

-  Consideremos uma carga que entra em movimento. No instante antes de ela se começar a mover, ela está a produzir um campo $\vec{E}$. Mal ela se começa a mover, o campo na sua vizinhaça altera-se. Essa alteração propaga-se para longe da carga à velocidade da luz.
- Por sua vez, essa campo elétrico a variar no tempo vai gerar um campo magnético ($\nabla \times \vec{B}=\mu_{0}\varepsilon_{0} \partial_{t}\vec{E}$). Se o movimento da carga for uniforme então o campo magnético varia de forma sempre igual e temos um campo magnético constante . 
- Se a carga tiver aceleração, o campo magnético gerado varia também com o tempo. Se por sua vez o campo magnético variar no tempo, gera também um campo elétrico. 
- Ou seja, quando temos um campo a variar no tempo, ele gera uma variação no outro, que gera uma variação de volta no primeiro. e sempre assim.

- Assim, vemos claramente que estes 2 campos fortemente se inter influenciam. Desta forma, $\vec{E}$ e $\vec{B}$ geram o *campo eletromagnético*.
- Assim, quando há uma perturbação neste campo, ela propaga-se no espaço até ao infinito da forma descrita acima, em que estes 2 campos se comportam como um só e em que as perturbações num perturbam o outro e eles se regeneram constantemente.

### 3.2.1 - Ondas Transversais
- Consideremos uma onda plana a propagar-se na direção $x$.
- Como tal, temos que o campo será constante num plano a mover-se com a onda e perpendicular a esta. Ou seja, podemos definir $\vec{E}=\vec{E}(x,t)$.
- COnsiderando que a onda se está a propagar no espaço ($\rho=0$), a Lei de Gauss fica na forma $\nabla \cdot \vec{E}=0$. Tendo em conta o campo que definimos acima, isto dá-nos: $$\frac{\partial E_{x}}{\partial x}=0$$
o que nos diz que, se hover uma componente do campo na direção $x$ então ela é igual para todos os pontos desta direção.
- Ora, isto indica-nos então que a onda é **transversal**. A única forma de o campo ter sempre o mesmo valor na direção de propagação é se este for zero!
- Apesar de a onda ser transversal, temos infinitas direções que a onda pode ter ($\hat{y},\hat{z}$ e qualquer combinação destas são direções transversais a $\hat{x}$). A essa direção chamamos de **Polarização** da luz.

- Por uma questão de simplificação, vamos considerar uma onda polarizada linearmente (sem com a mesma direção de oscilação) segundo a direção $y$:
$$\vec{E}=E_{y}(x,t)\hat{y}$$
- Se aplicarmos a Lei de Faraday a este campo temos:
$$\nabla \times \vec{E}=- \partial_{t}\vec{B} ~~~~\to~~~~ \partial_{x}E_{y}=-\partial_{t}B_{z}$$
(sendo que $E_{x}=E_{z}=0$)
- Ou seja, numa onda a mover-se na direção $x$, se tivermos $\vec{E}$ a oscilar em $y$ temos $\vec{B}$ a oscilar em $z$. Por outras palavras, **Ondas eletromagnéticas são transversais**! (Há excessões, mas por agora iremos ignorar a sua existência)

- Vamos aprofundar mais este estudo. Consideremos $E_{y}$ uma onda harmónica, tal que:
$$E_{y}(x,t)=E_{0y}\cos\left[\omega\left(t- \frac{x}{c}\right)+\varepsilon\right]$$
(em que $c$ é a velocidade da luz no vácuo AKA velocidade de propagação da onda)
- De acordo com a equação $\partial_{x}E_{y}=-\partial_{t}B_{z}$ acima, temos:
$$B_{z}=-\int \frac{\partial E_{y}}{\partial x}dt=- \frac{E_{0y}\omega}{c}\int \sin \left[\omega\left(t- \frac{x}{c}\right) +\varepsilon\right]dt=\frac{1}{c}E_{0y}\cos \left[\omega \left(t- \frac{x}{c} \right)+\varepsilon \right]$$
- E podemos representar estas funções $\vec{E},\vec{B}$ assim:
![[onda eletromagnética campos.png]]
- Vemos então que *no vácuo*:
    - $\vec{E},\vec{B}$ estão em fase 
    - $\vec{E},\vec{B}$ são mutuamente ortogonais e portanto $\vec{E}\times\vec{B}$ aponta na direção $\hat{x}$
    - Temos que estas funções apenas diferem pelo fator de 1 constante

- Mais especificamente, em materiais dielétricos "normais" (não condutores e não magnéticos) com permitividade $\varepsilon$ e permeabilidade $\mu$ temos:
$$E=cB \quad \quad;\quad\left(c=\frac{1}{\sqrt{\varepsilon\mu}}\right)$$
- Vimos no Cap 2 que existem ondas esféricas e planas. Tal como as ondas planas, essas também são soluções das equações de Maxwell. Assim, para ondas EM iremos considerar ondas esféricas, mas novamente: estas são apenas aproximações e algo impossível na vida real.

## 3.3 - Energia e Momento
- Ondas eletromagnéticas transportam energia e momento. Estudemos isto melhor.

### 3.3.1 - Vetor Poynting
- Como ondas EM transportam energia enquanto se movem no espaço, é natural definir um densidade volúmica de energia / densidada energética: $u$. Nisto, estamos a considerar que o campo elétrico contém energia em si. Como tal, se o campo for contínuo, a energia também o será.

- Temos um condensador de placas paralelas (de área $A$ e distanciadas de $d$) com capacidade $C$. Se ele for carregado de forma a ter DDP de $V$ entre as placas, a energia do condensador é $\frac{1}{2}CV^{2}$. Podemos então presumir que esta energia está armazenada no campo elétrico entre as placas. Assim podemos determinar a densidade energética.
    - O campo entre as placas será $E=\frac{\sigma}{\varepsilon_{0}}\to \sigma=\varepsilon_{0}E$ (consideramos as placas como planos infinitos carregados)
    - A DDP entre as placas, como o campo é uniforme, será $V=Ed$
    - Temos portanto: $$C=\frac{Q}{V}=\frac{\sigma A}{Ed}=\frac{\varepsilon_{0}EA}{Ed}=\varepsilon_{0} \frac{A}{d}$$
    - Disto resulta: $$u_{E}=\frac{\frac{1}{2}CV^{2}}{Ad}=\frac{\frac{1}{2} \varepsilon_{0} \frac{A}{d} (Ed)^{2}}{Ad}=\frac{\varepsilon_{0}}{2}E^{2}$$
sendo esta a **densidade energética do campo elétrico no vácuo**.

- Analogamente, para o campo magnético. Se considerarmos uma bobina de indutância $L$ com corrente $I$ podemos fazer contas e determinar a **densidade energética do campo magnético no vácuo**:
$$u_{B}=\frac{1}{2\mu_{0}}B^{2}$$
(não fiz a dedução porque não percebo o suficiente de magnetismo)

- Considerando que a relação $E=cB$ se aplica e usando $c=\frac{1}{\sqrt{\varepsilon_{0}\mu_{0}}}$ obtemos:
$$\begin{align*}
E=cB &\Leftrightarrow \frac{2}{\varepsilon_{0}} u_{E}=c^{2} \cdot 2\mu_{0}u_{B}\\
&\Leftrightarrow 2u_{B}= \cancelto1{c^{2}\mu_{0}\varepsilon_{0}} \cdot 2 u_{B}\\
&\Leftrightarrow u_{E}=u_{B}
\end{align*}$$
. Ou seja, a densidade energética de uma onda EM é **igualmente distribuida pelos campos elétrico e magnético**!!. Assim, a densidade energética total da onda é:
$$\begin{align*}
u&= u_{E}+u_{B}\\
&= 2u_{E}= \varepsilon_{0}E^{2}\\
&= 2u_{B}= \frac{1}{\mu_{0}}B^{2}
\end{align*}$$

- Recordemos agora que as ondas e os campos variam no tempo. Como tal, $u$ também irá variar.
- Tomemos $S$ como a energia transportada por unidade de tempo (AKA Potência) através de uma unidade de área. Ora, num intervalo $\Delta t$ a onda irá mover-se uma distância $c\Delta t$. Assim, temos:
$$S=\frac{u \cdot c\Delta t \cdot A}{\Delta t \cdot A}=uc$$
- Acima temos:
$$u=\varepsilon_{0}E^{2}=\frac{1}{\mu_{0}}B^{2}\to \varepsilon_{0}\mu_{0}E^{2}=B^{2}\to B^{2}=\frac{1}{c^{2}}E^{2}\to B=\frac{E}{c}$$
e podemos escrever $$u=\frac{1}{\mu_{0}}B^{2}=\frac{1}{\mu_{0}}B \cdot B=\frac{1}{\mu_{0}}B \cdot \frac{E}{c}=\frac{1}{c} \frac{1}{\mu_{0}}EB$$
e ficamos com:
$$S=uc=\frac{1}{\mu_{0}}EB$$
- Ora, é correto generalizar e escrever:
$$\vec{S}=c^{2}\varepsilon_{0}\vec{E}\times\vec{B}\tag{Eq.10}$$
(sendo que $\vec{E}\times \vec{B}$ nos dá a direção de propagação da onda AKA direção de propagação da energia)
este é o **VETOR POYNTING**.

- Sendo $\vec{E}=\vec{E_{0}}\cos(\vec{k}\cdot\vec{r}-\omega t)~,~\vec{B}=\vec{B_{0}}\cos(\vec{k}\cdot\vec{r}-\omega t)$ temos:
$$\vec{S}=c^{2}\varepsilon_{0} \vec{E_{0}}\times\vec{B_{0}}\cos^{2}(\vec{k}\cdot\vec{r}-\omega t)$$
sendo este o vetor que nos dá o *fluxo de energia por unidade de área e tempo*.

### Médias de Funções Harmónicas
- Consideremos que se quer calcular /  medir o valor do Vetor Poynting num instante. Ora, para ondas eletromagnéticas no vísivel temos que $\vec{E}$ e $\vec{B}$ têm frequência $\sim10^{15}Hz$. O vetor Poyting, por ter o quadrado do cosseno, terá o dobro da frequência.
- Ou seja, é inviável medir diretamente um vetor que varia tão rapidamente. Assim, usasse métodos com médias do sinal (averaging procedure)

- O valor médio de uma função $f(t)$ num intervalo $T$ será:
$$\langle f(t)\rangle_{T}=\frac{1}{T}\int_{t-T/2}^{t+T/2}f(t)dt$$
- Para uma função que descreva uma onda harmónica temos:
$$\begin{align*}
\langle e^{i\omega t}\rangle_{T}&= \frac{1}{T} \int_{t-T/2}^{t+T/2}e^{i\omega t}dt\\
&= \frac{1}{i\omega T} e^{i\omega t}\biggr|_{t-T/2}^{t+T/2}\\
&= \frac{1}{i\omega T}e^{i\omega t}\left(e^{i\omega \frac{T}{2}}- e^{-i\omega \frac{T}{2}} \right)\\
&= \frac{\sin\omega \frac{T}{2}}{\omega \frac{T}{2}}e^{i\omega t} = \text{sinc}\left(\omega \frac{T}{2}\right)e^{i\omega t}
\end{align*}$$
- Da equação acima podemos isolar as partes real e imaginária:
$$\begin{cases}
\Re & : & \langle\cos \omega t\rangle_{T}=(\text{sinc}u) \cos \omega t \\
\Im & : & \langle\sin \omega t\rangle_{T}=(\text{sinc}u) \sin \omega t
\end{cases}$$
(em que $u=\omega \frac{T}{2}$)
- Se $T$ for igual a 1 ou vários periodos (número inteiro de períodos) teremos que $\langle\cos\omega t\rangle_{T}=\langle\sin\omega t\rangle_{T}=0$
- Já para a função $\cos^{2}\omega t$ temos:
$$\langle\cos^{2}\omega t\rangle_{T}=\frac{1}{2}(1+ \text{sinc}\omega T\cos2\omega t)$$
- Temos que consoante $T$ aumenta a função $\text{sinc}$ diminui de valor rápido. Se analisarmos o sinal ótico por tempo suficiente para que $\text{sinc}\omega T\to0$, ficamos com $\langle\cos^{2}\omega t\rangle_{T}=\frac{1}{2}$. 

### 3.3.2 - Irradiância ($I$)
- Sempre que falamos da quantidade de luz que ilumina uma superfície, estamos a falar da **irradiância** AKA energia por unidade de área e tempo.
- O valor médio do vetor Poynting (para $T\gg \mathcal{T}$ (em que $\mathcal{T}$ é o período da luz)) é representado por $\langle S\rangle_{T}$ e não passa de uma medida de $I$.
- Para uma onda harmónica temos:
$$\langle S\rangle_{T}=c^{2}\varepsilon_{0}|\vec{E_{0}}\times\vec{B_{0}}|\langle\cos^{2}(\vec{k}\cdot\vec{r}-\omega t)\rangle= \frac{c^{2}\varepsilon_{0}}{2}|\vec{E_{0}}\times\vec{B_{0}}|$$
de onde vem (usando $E=cB$):
$$I\equiv \langle S\rangle_{T}= \frac{c\varepsilon_{0}}{2}E_{0}^{2}\tag{Eq. 11}$$
ou
$$I=\frac{c}{\mu_{0}}\langle B^{2}\rangle_{T}$$
$$I=\varepsilon_{0}c\langle E^{2}\rangle_{T}\tag{Eq.12}$$
e num meio não vácuo: $I=\varepsilon v \langle E^{2}\rangle_{T}$
- O campo elétrico é muito melhor que o magnético a exercer forças e realizar trabalho, iremos usar quase exclusivamente as eqs 11 e 12 e referiremo-nos ao campo elétrico como **Campo Ótico**.

### Lei do Quadrado Inverso
- Consideremos uma fonte isotrópico a emitir ondas esféricas (a emitir energia de forma igual em todas as direções)
![[Pasted image 20231114000358.png]]
- A amplitude da onda que passa nas superfícies esféricas de raio $r_{1},r_{2}$ será $E_{0}(r_{1}),E_{0}(r_{2})$. 
- Se houver conservação de energia, a energia total contida na onda ao passar na superfície de raio $r_{1}$ terá que ser a mesm que na outra superfície. Temos:
$$\begin{align*}
IA_{1}&= IA_{2}\\
c \varepsilon_{0} \langle E^{2}\rangle \cdot 4\pi r_{1}^{2}&= c \varepsilon_{0}\langle E^{2}\rangle \cdot 4\pi r_{2}^{2}\\
r_{1}^{2}(E_{0}(r_{1}))^{2}&= r_{2}^{2}(E_{0}(r_{2}))^{2}\\
r_{1}E_{0}(r_{1})&= r_{2} E_{0}(r_{2})
\end{align*}$$
- Como $r_{1},r_{2}$ são simplesmente raios arbitrários, podemos dizer que:
$$rE_{0}(r)=constante\to E_{0}=\frac{C}{r}$$
logo temos que a amplitude do campo cai com $r$. Ora, isto dá:
$$I=\varepsilon_{0}cE_{0}^{2}=\frac{\varepsilon_{0}cC^{2}}{r^{2}}$$
pelo que a Irradiância evolui com o **inverso do quadrado**.
- Ou seja, a Lei do Quadrado Inverso diz-nos que a Intensidade da Radiação Ótica de um qualquer sinal (e portanto a sua irradiância também) evoluem com o inverso do quadrado da distância à fonte!!!

### 3.3.3 - Fotões

--- PAGINA 62 ---
