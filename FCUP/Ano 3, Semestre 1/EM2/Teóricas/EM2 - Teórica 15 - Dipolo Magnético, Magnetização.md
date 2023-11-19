![[Pasted image 20231114225510.png]]
- Consideremos um loop de corrente, com corrente de intensidade $I$ e com área $S=ab$ como representado acima. Este loop está sujeito a um campo magnético uniforme $\vec{B}$ com direção $\hat{z}$.
- A forças aplicadas nos 2 lados de comprimento $a$ (diagonais, que intersetam o eixo dos xx em $x=\pm b/2$) *anulam-se*, sendo estas as 2 forças desenhadas a amarelo na figura da esquerda (usar regra da mão direita com $\vec{F}=I\vec{\ell}\times\vec{B}$, em que $\vec{I}$ gira em torno da espira conforme indicado pelos vetores $d\vec{\ell}$ na figura).
- Assim, as unicas forças aplicadas nesta linha de corrente estão nos lados de comprimento $b$ (que são paralelos ao eixo xx). Podemos então definir:
$$\vec{\ell}=\pm b\hat{x}~~~~,~~~~\vec{B}=B\hat{z}$$
e temos:
$$\vec{F}=I\vec{\ell}\times\vec{B}=\mp IbB\hat{y}$$
- Ora, o sinal/direção de $\vec{\ell}$ é escolhido conforme a direção da corrente traçado na figura. Por exemplo, no lado da esquerda (onde temos $d \vec{\ell_{1}}$) a corrente vai no sentido positivo dos xx e temos $\vec{\ell}=b\hat{x}$ e portanto $\vec{F}=-IbB\hat{y}$.
- Com estes 2 vetores $\vec{F}$ e sabendo que não há força total nos lados de comprimento $a$ é fácil entender a representação na figura da direita: temos uma vista transversal (a partir do eixo xx) do loop, com as forças aplicadas.

- Por uma questão de simplificação, vamos seguir a figura da direita e indicar que $\vec{F}=-IbB\hat{y}$, sendo a força do outro lado $-\vec{F}$.
- Ora, podemos imaginar que as forças $\vec{F},-\vec{F}$ tentam "esticar" o loop, mas também o tentam "girar". Esta última parte é mais importante, tendo-se então que elas geram *torque*.
- Se definirmos $\vec{r_{L}},\vec{r_{R}}$ (L-left, R-right) os vetores que vão da origem aos lados da esquerda e direita. Temos que o torque total é:
$$\begin{align*}
\tau&= (\vec{r_{L}}\times \vec{F}) + (\vec{r_{R}}\times(-\vec{F}))\\
&= (\vec{r_{L}}\times \vec{F}) - (\vec{r_{R}}\times\vec{F})\\
&= (\vec{r_{L}}-\vec{r_{R}})\times\vec{F}
\end{align*}$$
- Usando o ângulo $\theta$ assinalado (inclinação do loop em relação aos eixos yy e zz) podemos escrever o vetor que une as 2 pontas do loop:
$$\vec{r}=-a\cos\theta\hat{y}+a\sin\theta\hat{z}=\vec{r_{L}}-\vec{r_{R}}$$
e ficamos com:
$$\begin{align*}
\tau&= \vec{r}\times\vec{F}\\
&= (-a\cos\theta\hat{y}+a\sin\theta\hat{z})\times (-IbB\hat{y})\\
&= IbBa\sin\theta\hat{x}= IS\sin\theta B\hat{x}
\end{align*}$$
- Ora, se definirmos o vetor $\vec{m}=IS\hat{n}$  temos:
$$\vec{\tau}=\vec{m}\times\vec{B}=IS\hat{n}\times B\hat{z}=IS(\sin\theta\hat{y}+\cos\theta\hat{z})\times B\hat{z}=IS\sin \theta B\hat{x}$$
este vetor $\vec{m}$ é o **_Momento Dipolar Magnético_** em que:
$$\boxed{\vec{\tau}=\vec{m}\times\vec{B}}$$
de notar que para um dipolo elétrico tinhamos $\vec{\tau}=\vec{p}\times\vec{E}$
- De notar ainda que esta fórmula é válida para qualquer loop de corrente na presença de um campo uniforme $\vec{B}$. OU válido para dipolos de tamanho infinitesimal na presença de um campo não uniforme.

# Campo Magnético na Matéria
- No dia a dia ouvimos falar em magnetismo no contexto de imans e coisas do género. Ora, estas coisas não parecem ter nada a ver com linhas de corrente a gerar campos magnéticos.
- No entanto, na realidade temos que todos os materiais têm cargas elétricas a mover-se AKA correntes (eletrões a orbitar o núcleo):
![[Pasted image 20231114235556.png]]
- Ora, a uma escala macroscópica os átomos e as respetivas correntes são tão pequenos que podemos considerá-los **dipolos magnéticos**.
- Normalmente, eles anulam-se todos porque os átomos têm orientações aleatórias. Mas se um campo magnético passar pelo material, estes dipolos alinham-se e o material fica **magnetizado**.
- Ora, na *Polarização* tinhamos sempre que $\vec{P}\parallel\vec{E}$. No caso da magnetização:
    - **Materiais Paramagnéticos** - $\vec{M}\parallel\vec{B}$ (ocorre em átomos/moléculas com eletrões desemparelhados)
    - **Materiais Diamagnéticos** - $\vec{M}\parallel-\vec{B}$ (anti-paralelo) (ocorre em átomos/moléculas com todos os eletrões emparalhados)
- Temos ainda o caso de **Materiais Ferromagnéticos** - mantém/têm $\vec{M}\neq0$ mesmo quando $\vec{B}=0$
- De notar que os dipolos não são gerados por todos os eletrões nos átomos, apenas pelos eletroes *não emparelhdos*! 

## Campo Magnético VS Orbita Atómica
![[Pasted image 20231115092403.png]]
- Consideremos um eletrão a orbitar em torno do nucleo com raio $R$ e a velocidade $v$, tal que o período é $T=\frac{2\pi R}{v}$. Consideremos que o eletrão forma uma corrente constante na órbita (na realidade isto não acontece, mas podemos aproximar porque o período é muito reduzido). Essa corrente será:
$$I=\frac{\Delta q}{\Delta t}=\frac{-e}{T}=- \frac{ev}{2\pi R}$$
pelo que:
$$\vec{m}=IS\hat{n}=- \frac{1}{2}evR\hat{z}$$

- Consideremos que é aplicado um campo $\vec{B}$. Ele irá alterar o spin dos eletrões, sendo isto o que gera o paramagnetismo. No entanto, o campo também muito dificilmente roda todo o átomo.
- Mas há um efeito mais importante: o campo *acelera ou desacelera o eletrão*.
- Para o eletrão a orbitar o núcleo *sem campo magnético* temos:
$$\begin{align*}
F&= ma\\
\frac{1}{4\pi\varepsilon_{0}} \frac{e^{2}}{R^{2}}&= m_{e} \frac{v^{2}}{R}\tag{1}\\
\end{align*}$$
e ao aplicar o campo $\vec{B}$ passamos a ter uma força magnética. Consideremos que o campo é perpendicular à área do loop na figura. Temos $F=q \vec{v'}\times\vec{B}=qv'B$ (em que $\vec{v'}$ é a velocidade com campo) e fica:
$$\frac{1}{4\pi\varepsilon_{0}} \frac{e^{2}}{R^{2}}+e v'B= m_{e} \frac{v'^{2}}{R}\tag2$$
e subtraindo $(2) - (1)$ temos:
$$ev'B=\frac{m_{e}}{R}(v'^{2}-v^{2})=\frac{m_{e}}{R}(v'+v)(v'-v)$$
- Assumindo que a variação de velocidade é muito reduzida temos: $v'-v=\Delta v~,~v'+v=2v~,~v'=v$ e fica:
$$\begin{align*}
evB&= \frac{m_{e}}{R}2v \Delta v\\
\Delta v&= \frac{eRB}{2m_{e}}
\end{align*}$$
ou seja, $\Delta v>0$ e o eletrão acelera ao introduzir um campo magnético externo.
- Daqui temos:
$$\Delta \vec{m}=- \frac{1}{2} e (\Delta v)R \hat{z}= - \frac{e^{2}R^{2}}{4m_{e}}\hat{z}$$
ou seja, o momento dipolar magnético varia opostamente ao campo introduzido.
- Se tivessemos um eletrão a girar na direção oposta, com este mesmo campo, o eletrão iria desacelerar mas a *variação* seria postiva na mesma, porque a velocidade era negativa.
- Este é o fenómeno que gera o diamagnetismo.

## Magnetização
$$\vec{M}= \frac{d \vec{m}}{dV}$$

## Campo de objeto magnetizado
- Podemos definir o vetor potencial de um dipolo magnético:
$$\vec{A}_{dipolo}= \frac{\mu_{0}}{4\pi} \frac{\vec{m}\times(\vec{r}-\vec{r'})}{|\vec{r}-\vec{r'}|^{3}}$$
- E para um material magnetizado cada volume infinitesimal tem um momento $\vec{m}=\vec{M}d^{3}r$. Ora, o vetor potencial total do material será:
$$\begin{align*}
\vec{A}(\vec{r})&= \frac{\mu_{0}}{4\pi}\int \frac{\vec{M}(\vec{r'})\times(\vec{r}-\vec{r'})}{|\vec{r}-\vec{r'}|^{3}}d^{3}r'\\
&=\frac{\mu_{0}}{4\pi} \int \vec{M}(\vec{r'})\times \nabla \left(\frac{1}{|\vec{r}-\vec{r'}|} \right)d^{3}r'\\
&= \frac{\mu_{0}}{4\pi} \left[ \int \frac{1}{|\vec{r}-\vec{r'}|}\nabla'\times\vec{M}(\vec{r'})d^{3}r' - \int \nabla'\times\left(\frac{\vec{M}(\vec{r'})}{|\vec{r}-\vec{r'}|}\right)d^{3}r' \right]\\
&= \frac{\mu_{0}}{4\pi} \left[ \int \frac{1}{|\vec{r}-\vec{r'}|}\nabla'\times\vec{M}(\vec{r'})d^{3}r' + \oint \frac{\vec{M}(\vec{r'})\times\hat{n}}{|\vec{r}-\vec{r'}|}ds' \right]
\end{align*}$$
(em que se usou $\vec{A}\times\nabla f=f \nabla \times \vec{A}-\nabla \times (f \vec{A})$ e o teorema de Gauss)
- E podemos escrever como:
$$\vec{A}(\vec{r})=\frac{\mu_{0}}{4\pi}\left[\int \frac{\vec{\mathcal{J}_{m}}(\vec{r'})}{|\vec{r}-\vec{r'}|} d^{3}r'+\oint \frac{\vec{k_{m}}(\vec{r'})}{|\vec{r}-\vec{r'}|}ds' \right] $$

#### Densidade superficial de corrente
![[Pasted image 20231115180854.png]]
- Consideremos a seguinte representação de uma material uniformemente magnetizado.
- Vemos que as "correntes" que geram a magnetização se anulam todas. Sempre que temos uma corrente, a corrente adjacente vai no sentido oposto. Isto para todo o volume *exceto a berma*. Aí, como vemos na figura, temos linhas de corrente triangulares, em que um dos lados nunca é cancelado.
- Ou seja, se considerarmos todos os loops de corrente e respetivos lados que não são cancelados, temos uma "fita" de corrente assim:
![[Pasted image 20231115181158.png]]

- Consideremos 1 dos loops da figura inicial. Ele tem área $a$ e espessura/profundidade $t$. Podemos então escrever o momento dipolar de 1 loop em função de $M$:
$$m=Mat$$
- Ora, temos ainda que $m=Ia$ logo: $$m=Ia=Mat\to I=Mt$$ e em 1 linha de espessura infinitesimal ao longo da "fita" temos: $k_{m}=\frac{I}{t}=M$, que é a **densidade superficial de corrente**. Considerando o vetor normal à "fita" $\hat{n}$ na 2ª figura, podemos escrever o vetor da densidade de corrente, que tem o sentido da corrente:
$$\vec{k_{m}}=\vec{M}\times\hat{n}$$
- De notar que, apesar de chamarmos a isto "corrente", nenhum eletrão irá descrever este percurso pela berma do material. Isto porque, tal como tinhamos na Polarização, os eletrões estão *presos* aos átomos.
- Comparar à densidade superficial de carga de polarização: $\sigma_{p}=\vec{P}\cdot\hat{n}$

#### Densidade Volúmica de Corrente
![[Pasted image 20231115182138.png]]
- A Magnetização num material não é sempre uniforme. Consideremos a figura acima, parte a): temos que em $y$ a magnetização é menor que a magnetização um pouco ao lado, em $y+dy$: $M(y)<M(y+dy)$
- Ora, neste caso as correntes também não são todas iguais e não se anulam!
- Consideremos a superfície onde eles se juntam. Irá existir uma corrente com direção $x$. Conforme vimos acima, $I=Mt$, que neste caso nos dá: $$I_{x}=Mt\to I_{x}= \Delta M t=\Delta M dz=(M_{z}(y+dy)-M_{z}(y))dz=\frac{\partial M_{z}}{\partial y}dydz$$
que nos dá a densidade volúmica de corrente:
$$(\mathcal{J}_{m})_{x}=\frac{\partial M_{z}}{\partial y}$$
- Se procedermos da mesma forma vemos que na figura, na parte b) temos também uma corrente na direção $x$ e obtemos: $(\mathcal{J}_{b})_{x}=\frac{-\partial M_{y}}{\partial z}$
- A densidade total se juntarmos estas 2 será então:
$$(\mathcal{J}_{m})_{x}= \frac{\partial M_{z}}{\partial y}-\frac{\partial M_{y}}{\partial z}$$
e é evidente que podemos generalizar assim:
$$\vec{\mathcal{J}_{m}}=\nabla \times \vec{M}$$
- Comparar à densidade volúmica de carga de polarização: $\rho_{p}=- \nabla \cdot \vec{P}$