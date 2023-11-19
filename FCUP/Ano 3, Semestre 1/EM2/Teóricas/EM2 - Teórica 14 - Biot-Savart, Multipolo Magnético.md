## Correntes
- Podemos definir densidades de corrente volúmicas, superfíciais e lineares:
$$\begin{align*}
\vec{\mathcal{J}}=\rho \vec{v} \quad \quad;\quad \quad \left(\rho=\frac{dq}{dV}\right)\\
\vec{\kappa}=\sigma \vec{v} \quad \quad;\quad \quad \left(\sigma=\frac{dq}{ds}\right)\\
\vec{I}=\lambda \vec{v} \quad \quad;\quad \quad \left(\lambda=\frac{dq}{d\ell}\right)
\end{align*}$$
sendo que podemos escrever:
$$\begin{align*}
\vec{\mathcal{J}}d^{3}r=\rho \vec{v}~d^{3}r&= dq ~\vec{v}\\
\vec{\kappa}~ds=\sigma \vec{v}~ds&= dq ~\vec{v}\\
\vec{I}~d\ell=\lambda \vec{v}~d\ell&= dq ~\vec{v}
\end{align*}$$

## Lei de Biot-Savart
- Na aula anterior obtivemos:
$$\vec{A}(\vec{r})= \frac{\mu_{0}}{4\pi} \int \frac{\vec{\mathcal{J}}(\vec{r'})}{|\vec{r}-\vec{r'}|}d^{3}r'$$
e temos:
$$\vec{B}=\nabla \times \vec{A}=\nabla \times \left(\frac{\mu_{0}}{4\pi} \int \frac{\vec{\mathcal{J}}(\vec{r'})}{|\vec{r}-\vec{r'}|}d^{3}r'\right)$$
- Temos que $\nabla \times (f \vec{C})= f \nabla \times \vec{C} - \vec{C}\times \nabla f$ (para qualquer função escalar $f$ e campo vetorial $\vec{C}$). Sendo $f=\frac{1}{|\vec{r}-\vec{r'}|}$ e $\vec{C}=\vec{\mathcal{J}}(\vec{r'})$ temos:
$$\begin{align*}
\vec{B}=\nabla \times \vec{A}&= \frac{\mu_{0}}{4\pi} \left[\int \frac{1}{|\vec{r}-\vec{r'}|} \nabla \times \vec{\mathcal{J}}~d^{3}r'- \int \vec{\mathcal{J}}(\vec{r'})\times \nabla \left(\frac{1}{|\vec{r}-\vec{r'}|}\right) d^{3}r'\right] \\
&= - \frac{\mu_{0}}{4\pi} \int \vec{\mathcal{J}}(\vec{r'})\times \nabla\left(\frac{1}{|\vec{r}-\vec{r'}|}\right) d^{3}r'
\end{align*}$$
em que temos $\nabla \times \vec{\mathcal{J}}=0$ porque $\nabla=(\partial_{x},\partial_{y},\partial_{z})$ e $\vec{\mathcal{J}}$ apenas depende de $\vec{r'}$.
- E ficamos com:
$$\vec{B}=\frac{\mu_{0}}{4\pi} \int \frac{\vec{\mathcal{J}}(\vec{r'})\times(\vec{r}-\vec{r'})}{|\vec{r}-\vec{r'}|^{3}}d^{3}r'$$

- Consideremos que temos um fio com corrente elétrica AKA uma densidade linear de corrente. Temos:
$$\vec{\mathcal{J}} d^{3}r'=\rho \vec{v}~d^{3}r'= \frac{dq}{d^{3}r} \frac{d\vec{r}}{dt}d^{3}r= dq \frac{d\vec{r}}{dt}=\frac{dq}{dt}d\vec{r}=I d \vec{r}=I d\vec{\ell}$$
em que podemos sempre fazer a substituição:
$$\boxed{\vec{\mathcal{J}}d^{3}r ~~ \Longleftrightarrow ~~ I d \vec{\ell}}$$
- A equação acima fica então na forma:
$$\vec{B}=\frac{\mu_{0}I}{4\pi} \int \frac{d \vec{\ell}\times(\vec{r}-\vec{r'})}{|\vec{r}-\vec{r'}|^{3}}$$
em que esta é a **Lei de Biot-Savart**.

## Continuidade do campo magnético perto de distribuição superficial de corrente
![[descontinuidade de B 1.png]]
- Consideremos uma caixa como a da figura acima, a atravessar uma superfície com densidade de corrente $\vec{\kappa}$. Consideremos que a caixa é infinitesimal, ou seja, o campo nele é basicamente igual ao campo imediatamente acima e abaixo da superfície.
- Consideremos as componentes do campo magnético *perpendiculares à superfície com corrente*. $B_{\perp}^{+}$ será o campo acima da superfície e $B_{\perp}^{-}$ o campo abaixo.
- Ora, sabemos que o fluxo do campo magnético através desta superfície é 0, logo:
$$\oint \vec{B}\cdot d \vec{s}=0 ~~\to ~~ B_{\perp}^{+}-B_{\perp}^{-}=0 \to B_{\perp}^{+}=B_{\perp}^{-}$$
Ao fazer $\vec{B}\cdot d \vec{s}$ estamos a projetar o campo na direção normal à superfície. Ou seja, apenas temos a componente normal à superfície e portanto apenas temos o fluxo através da face de cima e de baixo, que são iguais. As áreas portanto cortam e ficamos então apenas com a intensidade do campo elétrico acima e abaixo. (Mal explicado mas pronto)

![[descontinuidade de B 2.png]]
- Vejamos agora a componente *paralela à superfície com corrente*. Temos um percurso retangular traçado através da superfície. Tal como para a caixa, consideremos que este percurso tem dimensões infinitesimais.
- Façamos o integral de linha do campo aqui:
$$\oint \vec{B}\cdot d \vec{\ell}=(B_{\parallel}^{+}-B_{\parallel}^{-})l$$
Ao fazer $\vec{B}\cdot d \vec{\ell}$ estamos a projetar o campo nessa direção e ficamos apenas com o valor da componente paralela à superfície a multiplicar pelo comprimento do lado. Para os lados verticais e que de facto atravessam a superfície temos $\vec{B}\perp d \vec{\ell}$ e então o produto escalar é nulo.
- Por outro lado, temos a equação de Ampere-Maxwell para a magnetostática:
$$\nabla \times \vec{B}=\mu_{0}\vec{\mathcal{J}}$$
podemos fazer o integral de superfície dos 2 lados:
$$\int (\nabla \times \vec{B})\cdot d \vec{s}=\mu_{0}\int \vec{\mathcal{J}}\cdot d\vec{s}$$
e podemos aplicar o teorema de Stokes ao termo da direita:
$$\oint \vec{B}\cdot d \vec{\ell}= \mu_{0} \int \vec{\mathcal{J}}\cdot d \vec{s}=\mu_{0}I$$
em que se usou: $$\vec{\mathcal{J}}\cdot d \vec{s}=\mathcal{J}_{n}ds=\rho v ds=\frac{dq}{dV} \frac{dr}{dt} ds=\frac{dq}{dt} \frac{dr \cdot ds}{dV}=\frac{dq}{dt}=I$$
e podemos ainda reescever isto:
$$\kappa l = \sigma v l =\frac{dq}{ds} \frac{dr}{dt} dr=\frac{dq}{dt} \frac{dr \cdot dr}{ds}=\frac{dq}{dt}=I$$
e ficamos com:
$$\oint \vec{B}\cdot d \vec{\ell}= \mu_{0}\kappa l$$
- Se igualarmos as duas definições deste integral de linha temos:
$$(B_{\parallel}^{+}-B_{\parallel}^{-})l=\mu_{0}\kappa l$$
o que nos dá:
$$B_{\parallel}^{+}-B_{\parallel}^{-}=\mu_{0}\kappa$$
ou, de forma mais generalizada:
$$\vec{B}^{+}-\vec{B}^{-}=\mu_{0} \vec{\kappa}\cdot \hat{n}$$
## Expansão Multipolar
- Além de multipolos de carga elétrica, este tipo de expansão é útil quando temos distribuições de corrente válida a distâncias da distribuição ($r$) muito longas.
- Recordemos que esta expansão permite tornar uma função do tipo $1/r$ numa série em que quase todos os termos desaparecem em $r\to \infty$.
- Mais especificamente, vimos que:
$$\frac{1}{|\vec{r}-\vec{r'}|}=\frac{1}{\sqrt{r^{2}+(r')^{2}+2rr'\cos\alpha}}=\frac{1}{r} \sum\limits_{n=0}^{\infty} \left(\frac{r'}{r}\right)^{n} P_{n}(\cos \theta')$$
em que $\vec{r},\vec{r'}$ são as posições do ponto em estudo e da fonte/carga/corrente. $\theta'$ é o ângulo que estes 2 vetores formam.
- Temos então o vetor potencial:
$$\vec{A}(\vec{r})= \frac{\mu_{0}}{4\pi} \int \frac{\vec{\mathcal{J}}(\vec{r'})}{|\vec{r}-\vec{r'}|}d^{3}r'$$
que fica:
$$\begin{align*}
\vec{A}(\vec{r})&= \frac{\mu_{0}}{4\pi}\sum\limits_{n=0}^{\infty} \frac{1}{r^{n+1}} \int (r')^{n} P_{n}(\cos\theta')\vec{\mathcal{J}}(\vec{r'})d^{3}r'\\
&= \frac{\mu_{0}I}{4\pi}\sum\limits_{n=0}^{\infty} \frac{1}{r^{n+1}}\int (r')^{n} P_{n}(\cos\theta')d \vec{\ell}\\
&= \frac{\mu_{0}I}{4\pi}\left[ \frac{1}{r}\oint d\vec{\ell} + \frac{1}{r^{2}}\oint r'\cos\theta' d \vec{\ell} + \frac{1}{r^{3}}\oint (r')^{2} \left( \frac{3}{2}\cos \frac{^{2}\theta'-1}{2} \right)d \vec{\ell} + \dots \right]\\
&= \frac{\mu_{0}I}{4\pi}\left[ \frac{1}{r^{2}}\oint r'\cos\theta' d \vec{\ell} + \frac{1}{r^{3}}\oint (r')^{2} \left( \frac{3}{2}\cos \frac{^{2}\theta'-1}{2} \right)d \vec{\ell} + \dots \right]
\end{align*}$$
em que o 1º termo da soma é anulado pois corresponde ao monopolo magnético, que vimos que não existe.

- Assim, quando $r\to\infty$ o termo dominante passa a ser o termo $1/r^{2}$ (menor expoente) - o termo do *dipolo*. Nesse caso temos então:
$$\vec{A}_{dip}(\vec{r})= \frac{\mu_{0}I}{4\pi r^{2}}\oint r' \cos\theta' d \vec{\ell}=\frac{\mu_{0}I}{4\pi r^{2}} \oint \hat{r}\cdot \vec{r'}d \vec{\ell} $$
- Podemos fazer a seguinte igualdade (nem o Avelino nem o Griffiths mostraram esta dedução): $$\oint (\hat{r}\cdot \vec{r'})= -\hat{r}\times \int d \vec{s'}$$
e ficamos com:
$$\begin{align*}
\vec{A}_{dip}(\vec{r})&= -\frac{\mu_{0}I}{4\pi r^{2}} \hat{r}\times \int d \vec{s'}\\
&= \frac{\mu_{0}I (\int d \vec{s'})\times \hat{r}}{4 \pi r^{2}}\\
&= \frac{\mu_{0}}{4\pi} \frac{\vec{m}\times \hat{r}}{r^{2}}
\end{align*}$$
em que $$\vec{m}= I \int d \vec{s}=I \vec{a}=Is \hat{n}$$
sendo este o **_Momento Dipolar Magnético_**. O sentido deste vetor é dado pela regra da mão direita. Consideremos que temos uma corrente circular. Se fecharmos a mão na direção que a corrente circular o polegar irá apontar na direção de $\vec{m}$.
- Aqui apenas estudamos o termo dipolo. E sim, existem os termos quadrupolo, octopolo, etc. que também existem. Mas verifica-se que o que determinamos aqui se $r$ for bastante maior que o tamanho do loop de corrente.
![[dipolo real e teorico 1.png]]

- Podemos escrever:
$$\vec{A}_{dip}(\vec{r})=\frac{\mu_{0}}{4\pi} \frac{\vec{m}\times \hat{r}}{r^{2}}=\frac{\mu_{0}}{4\pi} \frac{m\sin\theta}{r^{2}}\hat{\phi}$$
(com $\vec{m}=m \hat{z}~,~ \vec{r}=r\sin\theta \hat{\phi}+z \hat{z}$)
e temos:
$$\vec{B}_{dip}(\vec{r})=\nabla \times \vec{A}= \frac{\mu_{0}m}{4\pi r^{3}}(2\cos\theta \hat{r} + \sin\theta\hat{\theta})$$
