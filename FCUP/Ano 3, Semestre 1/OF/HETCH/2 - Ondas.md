## 2.1 - Ondas 1-D
- Uma onda é uma perturbação do meio em que se propaga e que se auto-sustenta. Assim temos ondas:
    - *longitudinais* - o meio é deslocado na direção de propação da onda (ondas sonoras)
    - *transversais* - o meio é deslocado numa direção perpendicular a este (ondas num fio)

- Em qualquer dos casos, é útil recordar que consoante a onda se propaga, as partículas que ela afeta oscilam entre as suas posições de equilíbrio, mas não se propagam com a onda. 
- Devemos notar que dizer que temos uma onda 1-D não significa que a onda existe em 1D (como uma onda sonora). Uma onda como a que se propaga num fio também é 1D: precisamos apenas de uma variável espacial para a descrever.

- Consideremos uma perturbação $\psi$ a deslocar-se no espaço e tempo com velocidade $v$: $$\psi(x,t)=f(x,t)$$
- Para saber o formato/*perfil* da onda num instante $t=a$ basta tornar o tempo constante: $\psi(x,t)|_{t=a}=f(x,a)$ 
- Para já consideraremos apenas ondas que não alteram de forma consoante se deslocam. Assim, de deixarmos passar um tempo $t$, a onda terá-se movido uma distância $vt$; mas todas as suas outras caraterísticas ficaram iguais. A onda só "desliza" para o lado.
![[onda progressiva.png]]

- Assim, podemos mudar o referencial de $S$ (referencial do LAB) para um referencial $S'$ que se move com a onda, com velocidade $v$. Ora, neste referencial temos $x\to x'$ e a onda já não varia com o tempo, é sempre constante:
![[onda prog referencial em movimento.png]]

- Ora, se juntarmos os 2 referenciais numa imagem temos
![[onda prog mudança referencial.png]]
- Vemos claramente que $x=x' + vt$. Assim: $x'=x-vt$, de onde, no referencial $S'$ temos que $$\psi(x)=f(x-vt)$$
esta é a forma mais simples/geral de escrever uma onda 1D a mover-se no sentido positivo dos $x$ com velocidade $v$.

> **EXEMPLO**
> ![[impulso f.png|300]]
> - Consideremos que temos o impulso $f(x)=\frac{3}{10x^{2}+1}$
> - Queremos então definir uma onda $\psi$ a deslocar-se no sentido positivo dos $x$ com velocidade $v$ e perfil igual a $f$.
> - Basta usar a equação acima e temos: $$\psi(x,t)=f(x-vt)=\frac{3}{10(x-vt)^{2}+1}$$
> - Usando $v=1$, podemos traçar a onda para $t=0,1,2,3$: 
> ![[onda com perfil definido por f.png|300]]

- Podemos ainda escrever noutras formas: $$f(x-vt)=F\left(t- \frac{x}{v}\right)$$

### 2.1.1 - Equação de Onda Diferencial
- Equação diferencial parcial, linear, homogénea de 2ª ordem. Descreve ondas em meios sem perdas. Temos muitos tipos de ondas $\psi$, muito diferentes, mas que são todas soluções desta equação.

- Tendo em conta que $\psi(x,t)=f(x\mp vt)=f(x')$ podemos escrever:
$$\frac{\partial \psi}{\partial x}= \frac{\partial f}{\partial x} $$
ora, temos que $x'=x\mp vt$. Logo:
$$\frac{\partial \psi}{\partial x}= \frac{\partial f}{\partial x'} \cancelto{~=1}{\frac{\partial x'}{\partial x}}= \frac{\partial f}{\partial x'}\tag{1}$$
- Por outro lado, em termos de tempo temos:
$$\frac{\partial \psi}{\partial t}=\frac{\partial f}{\partial t}=\frac{\partial f}{\partial x'} \frac{\partial x'}{\partial t}=\mp v \frac{\partial f}{\partial x'}\tag2$$
- Juntando as equações 1 e 2 temos:
$$\frac{\partial \psi}{\partial t}=\mp v \frac{\partial \psi}{\partial x}$$
isto diz-nos que a forma como $\psi$ varia ao longo do tempo e posição são iguais, a menos da multiplicação por uma constante.

- Vejamos então as 2ª derivadas:
    - Para a posição simplesmente temos: $$\frac{\partial^{2}\psi}{\partial x^{2}}=\frac{\partial^{2}f}{\partial x'^{2}}\tag3$$
    - Para o tempo: $$\frac{\partial^{2}\psi}{\partial t^{2}}=\frac{\partial}{\partial t} \left(\mp v \frac{\partial f}{\partial x'}\right)=v^{2} \frac{\partial^{2} f}{\partial x'^{2}}\tag4$$
- Novamente, juntando as equações 3 e 4 obtemos a famigerada equação de onda (1D): $$\boxed{\frac{\partial^{2}\psi}{\partial x^{2}}=\frac{1}{v^{2}} \frac{\partial^{2}\psi}{\partial t^{2}}}$$

- Por esta ser uma equação *homogénea*, se $\psi$ é uma solução, qualquer múltiplo de $\psi$. Dito isto, esta equação aplicasse a sistemas *sem amortecimento* (pelo que se acrescia um termo $\frac{\partial \psi}{\partial t}$).

## 2.2 - Ondas Harmónicas / Sinusoidais
- Consideremos uma onda com perfil:
$$\psi(x,t)|_{t=0}=\psi(x)=A\sin kx=f(x)$$em que $k$ é o **número de propagação** (que na prática serve para tornar o argumento do seno em algo sem unidades).

- Novamente, para obter a a função que descreve a onda substituimos $x\to x-vt$ e temos $$\psi(x,t)=A\sin k(x-vt)=f(x-vt)$$

### Comprimento de Onda, $\lambda$
- Basicamente é o *período espacial*. Pode aparecer em $nm,\mu m,\dot{A}$.
- Por definição, temos $\psi(x,t)=\psi(x+\lambda,t)$
- No caso da onda harmónica, por esta ser descrita por um seno, acrescentar $\lambda$ a $x$ é equivalente a acrescentar $2\pi$ ao argumento:
$$\sin k(x-vt)=\sin k[(x\pm \lambda)-vt]=\sin[k(x-vt)\pm 2\pi] \quad \longrightarrow \quad |k\lambda|=2\pi$$
ou seja, 
$$k = \frac{2\pi}{\lambda}$$

### Período, $\tau$
- É o *período temporal*. Tempo que tem que passar para que a onda inteira passe num certo ponto.
- Por definição: $\psi(x,t)=\psi(x,t+\tau)$
- Para uma onda harmónica:
$$\sin k(x-vt)=\sin k[x-v(t\pm \tau)]=\sin[k(x-vt)\pm 2\pi] \quad \longrightarrow \quad |kv \tau|=2\pi$$
logo:
$$\tau=\frac{\lambda}{v}$$

### Frequência, $\nu$
- O inverso do período: $\nu=1/\tau$
- Podemos escrever a equação acima como:
$$\tau=\frac{\lambda}{v}=\frac{1}{\nu} \quad \longrightarrow \quad \boxed{v=\nu \lambda}$$

### Frequência angular, $\omega$
$$\omega\equiv \frac{2\pi}{\tau}=2\pi \nu$$

### Número de onda, $\kappa$
$$\kappa\equiv \frac{1}{\lambda}$$
- Na prática, funciona como uma frequência espacial.

---
- Usando as relações acima podemos reescrever a funnção da onda harmónica como:
$$\psi=A\sin k(x\mp vt)=A\sin 2\pi\left(\frac{x}{\lambda}\mp \frac{t}{\tau}\right)=A\sin 2\pi(\kappa x\pm \nu t) = A\sin(kx\mp \omega t)=A\sin 2\pi\nu\left(\frac{x}{v}\mp t\right)$$

## 2.3 - Fase e Velocidade de Fase
- Consideremos a onda harmónica: $$\psi(x,t)=A \sin(kx-\omega t)$$
em que a **fase** da função é $$\varphi=kx-\omega t$$
- Podemos invés disto ter uma forma mais geral:
$$\psi(x,t)=A \sin(kx-\omega t + \varepsilon)$$
em que $\varepsilon$ é a *fase inicial*. Esta pode ou não ser zero, conforme o valor de $\psi(0,0)$
    - Por outro lado consideremos $\varepsilon=\pi$. Temos: $$\psi(x,t)=A \sin(kx-\omega t+\pi)=A\sin(\omega t-kx)$$
    - Ora, tanto a 1ª com a 2ª função descrevem ondas harmónicas iguais, a deslocar-nos no sentido positivo dos xx. Apenas têm uma diferença de fase de $\pi$. Dito isto, quando a fase inicial não importa, **qualquer uma destas formas pode ser usada** ($kx-\omega t$ ou $\omega t-kx$)

- Assim, de forma geral, a fase de uma função harmónica é escrita como $$\varphi=kx-\omega t+ \varepsilon=\varphi(x,t)$$
pelo que $$\left|\left(\frac{\partial \varphi}{\partial t}\right)_{x} \right|=\omega \quad \quad;\quad \quad \left| \left(\frac{\partial \varphi}{\partial t}\right)_{t} \right|=k$$(notemos que estamos a usar a notação comum em termodinâmica em que $\left(\frac{\partial f}{\partial x}\right)_{y}$ é a derivada parcial de $f$ em $x$, mantendo $y$ constante,)

- Podemos então escrever:
$$\left(\frac{\partial x}{\partial t}\right)_{\varphi}= \frac{-\left(\frac{\partial \varphi}{\partial t}\right)_{x}}{ \left(\frac{\partial \varphi}{\partial x}\right)_{t}}= \pm \frac{\omega}{k}=\pm v$$
esta é a **velocidade de fase** - velocidade com que o perfil da onda se move no espaço.

### Fase Constante
- Para uma onda de fase constante temos $$\psi=A\sin k(x-vt)$$
- Ora, se a fase é constante, se $t$ aumenta, $x$ também aumenta. 
- Ou seja, neste caso temos que também $\psi$ é constante. Ou seja: $\frac{\partial \psi}{\partial t}=0$.
- Podemos então obter a equação:
$$\pm v=\frac{-\left(\frac{\partial \psi}{\partial t}\right)_{x}}{ \left(\frac{\partial \psi}{\partial x}\right)_{t}}$$
- Um exemplo prático disto é: ondas causadas por objeto cair em água.
    - Verificamos que existem circunferência de pontos, todos à mesma distância do centro e com a mesma fase.
    - Ora, se dentro dessas circunferências a fase é constante, também $\psi$ o é.
    - Ou seja, os picos e vales da onda têm que corresponder a círculos.

## 2.4 - Princípio da Sobreposição
- A equação de onda diferencial é **linear**. Isso permite-nos verificar uma propriedade importante destas: o princípio de sobreposição. Ou seja, sendo $\psi_{1},\psi_{2}$ soluções da equação de onda; também a onda $\Psi=\psi_{1}+\psi_{2}$ será solução. 
    - Ou seja, temos: $$\frac{\partial^{2}\psi_{1}}{\partial x^{2}}=\frac{1}{v^{2}} \frac{\partial^{2}\psi_{1}}{\partial t^{2}} \quad \quad;\quad \quad \frac{\partial^{2}\psi_{2}}{\partial x^{2}}=\frac{1}{v^{2}} \frac{\partial^{2}\psi_{2}}{\partial t^{2}}$$
    - Se somarmos as duas equações obtemos: $$\begin{align*}
\frac{\partial^{2}\psi_{1}}{\partial x^{2}}+\frac{\partial^{2}\psi_{2}}{\partial x^{2}}&= \frac{1}{v^{2}} \frac{\partial^{2}\psi_{1}}{\partial t^{2}}+\frac{1}{v^{2}} \frac{\partial^{2}\psi_{2}}{\partial t^{2}}\\
\frac{\partial^{2}}{\partial x^{2}}(\psi_{1}+\psi_{2})&= \frac{1}{v^{2}} \frac{\partial^{2}}{\partial t^{2}}(\psi_{1}+\psi_{2})\\
\frac{\partial^{2}\Psi}{\partial x^{2}}&= \frac{1}{v^{2}} \frac{\partial^{2}\Psi}{\partial t^{2}}
\end{align*}$$sendo esta, portanto, outra solução.

- Na prática, isto significa que se 2 ondas se estiverem a propagar na mesma região elas podem **sobrepôr-se**, sem que nenhuma delas se altere ou destrua.
- Para obter o resultado da sobreposição simplesmente se soma o valor de cada onda em cada ponto, conforme vemos no exemplo abaixo:
  ![[sobreposiçao ondas.png|425]]
  - Torna-se ainda evidente que, quando as ondas têm amplitudes próximas e frequências iguais, o maior fator que afeta a sua sobreposição é a *diferença* de fase. Vejamos 4 casos intuitivos:
![[sobrepos ondas varios angulos - 1.png|555]]   ![[sobrepos ondas varios angulos - 2.png|560]]

## 2.5 - Representação Complexa
(Para mais informação, ver revisões disto feitas pelo Ariel 🧜)
- Por vezes as funções seno e cosseno podem resultar em cálculos excessivamente complicados. Assim, frequentemente usamos *complexos*.
- Temos as 2 formas:
**Algébrica**
$$z=x+iy$$
**Polar ou Exponencial**
$$z=r e^{i\theta}=r\cos\theta+ir\sin\theta$$
- Temos ainda o conjugado: $$z^{*}=x-iy=r\cos\theta-i\sin\theta=re^{-i\theta}$$
- De forma geral, para fazer somas/subtrações usamos a forma algébrica (em que complexos funcionam como vetores) e para multiplicação/divisão usamos a forma polar.
- O módulo é dado por $r=|z|=\sqrt{z^{*}\cdot z}$

- Podemos ainda representar complexos na forma:
$$z= \text{Re}(z)+i\text{Im}(z)$$
em que $\text{Re}(z)=\frac{1}{2}(z+z^{*})~~,~~\text{Im}(z)=\frac{1}{2}(z-z^{*})$. Ou então: $\text{Re}(z)=r\cos\theta~~,~~\text{Im}(z)=r\sin\theta$

- Assim, podemos representar ondas na forma:
$$\psi(x,t)=\text{Re}\left[ Ae^{i(\omega t-kx+\varepsilon)}\right]=A\cos(\omega t-kx+\varepsilon)$$
pelo que, especialmente ao multiplicar ondas, fazemos:
$$\psi(x,t)=Ae^{i(\omega t-kx+\varepsilon)}=A e^{i\varphi}$$
e no final dos cálculos é que poderemos representar a onda como sendo a parte real da exponencial imaginária.
- De notar que para fazer operações como **produto vetorial ou escalar** temos que ter $\psi$ na forma real!!

## 2.6 - Fasores e Soma de Ondas
![[fasores - 1.png]]     ![[fasores - 2.png|550]]
- Consideremos o sistema acima. Temos uma seta com amplitude $A$ a rodar com velocidade constante $\omega$, ou seja, com argumento $\omega t$.
- Ora, a seta juntamente com o seu ângulo de fase formam um **fasor**:
$$A ~\angle~ \varphi $$
- Ou seja, uma onda $\psi=A\sin(kx+\omega t)$ (a mover-se para a esquerda)é equivalente a um fasor com amplitude $A$ a rodar com ângulo $\omega t$ (em sentido anti-horário).

- Quando se sobrepõe ondas, estamos interessados em determinar a amplitude e fase da onda resultante. 
    - Para 2 ondas *em fase*, tal como vimos na secção 2.4, a onda resultante tem a mesma fase e a amplitude $A=A_{1}+A_{2}$. Isto é equivalente a somar 2 vetores colineares: 
![[soma fasores 1.png]]
    - Similarmente, quando a diferença de fase é igual a $\pi$ a força resultante terá a amplitude será $A=A_{1}-A_{2}$. Isto é como se somassemos 2 vetores com direções iguais e sentidos opostos.
![[soma fasores 3.png]]
(sendo que a onda resultante está em fase com $A_{1}$ e em oposição de fase com $A_{2}$)

- Ora, fasores podem ser somados quase como que vetores. 
- Por exemplo, se tivermos uma onda com $\varepsilon=0$ e a ela somarmos uma onda com $\varepsilon=\pi/3$  temos:
![[soma fasores 2.png]]
(equivalente à parte b) da figura da secção 2.4)

## 2.7 - Ondas Planas
- A luz pode ser descrita em cada ponto. Mas é muito mais útil descrevê-la a partir de superfícies: **frentes de onda**.
- Consideremos uma onda causada por um objeto cair em água. Se juntarmos todos os pontos em que a fase da onda (na sua componente 1D) tem a mesma fase e a mesma amplitude, vemos que eles formam um círculo.
- Ou seja, de forma geral, para qualquer onda 3D a *frente de onda é o conjunto de pontos com a mesma fase*.

- Dito isto, uma **onda plana** é a forma mais simples de onda 3D. Nela, num certo instante, o conjunto de pontos que têm a mesma fase *constitui um plano*.

- Matematicamente, um plano perpendicular a um vetor $\mathbf{k}$ que passa num ponto $(x_{0},y_{0},z_{0})$ é descrito por
$$(\mathbf{r}-\mathbf{r_{0}})\cdot \mathbf{k}=0$$
em que todos os pontos arbitrários $\mathbf{r}$ que satistaçam esta equação pertencem ao plano.
- Além disso, se definirmos o vetor normal como $\mathbf{k}=(k_{x},k_{y},k_{z})$ temos:
$$\begin{align*}
(\mathbf{r}-\mathbf{r_{0}})\cdot \mathbf{k}&= 0\\
k_{x}(x-x_{0})+k_{y}(y-y_{0})+k_{z}(z-z_{0})&= 0\\
k_{x}x+k_{y}y+k_{z}z&= \underbrace{k_{x}x_{0}+k_{y}y_{0}+k_{z}z_{0}}_{\equiv ~a}\\
k_{x}x+k_{y}y+k_{z}z&= a \quad\to\quad \mathbf{k}\cdot \mathbf{r}=a
\end{align*}$$

- Podemos então definir uma onda como $$\psi(\mathbf{r})=A\sin(\mathbf{k}\cdot \mathbf{r})$$
ou seja, esta função vai descrever uma série de planos, em que todos os pontos têm a mesma amplitude e fase. Ora:
![[onda plana.png|456]]

**Onda parada no tempo**
- Podemos visualizar ondas planas de outra forma:
![[onda plana v2.png|450]]
- Consideremos que um feixe de luz é formado por infinitos feixes, todos a oscilar com a mesma frequência e fase, tendo-se as ondas na figura acima.
- Ora, consideremos que "cortamos" este feixe em 2 planos, a uma distância de 1 comprimento de onda, como vemos acima.
- Ora, fica evidente que todos os pontos do mesmo plano têm a mesma amplitude e fase. Ou seja, temos 2 planos com amplitudes iguais. Consoante o feixe (e portanto todas as ondas) avançam, a amplitude do plano varia de forma sinusoidal. De notar ainda que como a amplitude da onda será a mesma em todo o plano, temos uma onda **homogénea**.
- O facto que estes 2 planos, distanciados de 1 comprimento de onda, têm a mesma amplitude de onda pode ser escrito como:
$$\psi(\mathbf{r})=\psi\left(\mathbf{r}+\lambda \frac{\mathbf{k}}{k}\right)$$
Ora, então temos:
$$Ae^{i \mathbf{k}\cdot\mathbf{r}}=Ae^{i(\mathbf{r}+\lambda \frac{\mathbf{k}}{k})} = Ae^{i \mathbf{k}\cdot \mathbf{r}}e^{i\lambda k}=Ae^{i \mathbf{k}\cdot \mathbf{r}}$$

o que implica:
$$e^{i\lambda k}=1=e^{i2\pi}~~\longrightarrow~~\lambda k=2\pi\to \boxed{k=\frac{2\pi}{\lambda}}$$
sendo que o vetor $\mathbf{k}$, de módulo $k$, que indica a direção de propagação da onda é o **vetor de propagação**.

**Onda a mover-se no tempo**
- Para passar de $\psi(\mathbf{r})$ para uma função que evolui no tempo basta fazer:
$$\psi(\mathbf{r},t)=A e^{i(\mathbf{k}\cdot \mathbf{r}\mp \omega t)}$$
novamente, em cada instante, as frentes de onda são as superfícies que contém os pontos que têm a mesma fase.
- Ora, agora a amplitude pode não ser constante. Aliás, é comum ter $A=A(\mathbf{r})$, pelo que a onda pode ser **não homogénea**.

![[onda plana geral.png|500]]
Na figura acima temos um ponto $\mathbf{r}$ cuja componente na direção de $\mathbf{k}$ é $r_{k}$

- Ora, seja $dr_{k}$ um movimento da partícula na direção de $\mathbf{k}$ que ocorre após um intervalo de tempo $dt$. Se olharmos para um ponto da onda e o seguirmos durante o deslocamento veremos que nada muda. Por outras palavras, tendo um ponto, se acrescentar-mos uma distância a $\mathbf{r}$ e o tempo correspondente a $t$  a onda será a mesma. Temos ainda que, conforme a figura acima, $\psi(\mathbf{r})=\psi(r_{k})$ porque pertencem à mesma frente da onda para a qual consideramos $A$ constante. Assim:
$$\psi(\mathbf{r},t)=\psi(r_{k}+dr_{k},t+dt)=\psi(r_{k},t)$$
que em forma exponencial fica:
$$Ae^{i(\mathbf{k}\cdot\mathbf{r}\mp\omega t)} = Ae^{i(kr_{k}+kdr_{k}\mp\omega t\mp \omega dt)}=Ae^{i(kr_{k}\mp \omega t)}$$
ou seja, será necessário que $$kdr_{k}=\pm\omega dt~~\to~~ \frac{dr_{k}}{dt}=\pm \frac{\omega}{k}=\pm v$$

### Exemplo
![[sobrepos ondas planas.png]]
- Consideremos o caso acima. As 2 ondas têm o mesmo comprimento de onda $\lambda$, ou seja, têm $k_{1}=k_{2}=k$
- O vetor arbitrário será $\mathbf{r}=(y,z)$
- Temos $\mathbf{k_{1}}=k \mathbf{z}, ~~\mathbf{k_{2}}=k\cos\theta \mathbf{z}+k\sin\theta\mathbf{y}$ 
- Para $\psi_1$ temos que $\mathbf{k_{1}}\cdot \mathbf{r}=kz$. Daí vem: $$\psi_{1}=A_{1}\cos \left(\frac{2\pi}{\lambda}z-\omega t\right)$$
- Para $\psi_{2}$ temos $\mathbf{k_{2}}\cdot \mathbf{r}=k\cos\theta z+k\sin\theta y$ e obtemos:
$$\psi_{2}=A_{2}\cos\left[\frac{2\pi}{\lambda}(z\cos\theta+y\sin\theta)- \omega t\right]$$

- Devemos notar que **qualquer onda 3D** pode ser representada como uma combinação de ondas planas
- Além disso, temos que, *na teoria* ondas planas estendem-se até ao infinito. Obviamente isso é fisicamente impossível. Como tal, a "semelhança" entre ondas reais e ondas planas teóricas é suficientemente grande para que possamos aproximar.

## 2.8 - Equação de Onda Diferencial 3D

- Uma onda plana pode ser escrita como:
$$\psi=Ae^{i(k_{x}x+k_{y}y+k_{z}z\mp \omega t)}$$
ou, com *cossenos direcionais*:
$$\psi=Ae^{i[k(\alpha x+\beta y+ \gamma z)\mp\omega t]}$$
em que:
$$\alpha=\frac{k_{x}}{k}~~~~;~~~~\beta=\frac{k_{y}}{k}~~~~;~~~~\gamma=\frac{k_{z}}{k}$$
- Ora, se procedermos de forma semelhante ao que fizemos para deduzir a equação de onda 1D obtemos:
$$\begin{align*}
\frac{\partial^{2}\psi}{\partial x^{2}} &= -\alpha^{2}k^{2}\psi\\
\frac{\partial^{2}\psi}{\partial y^{2}} &= -\beta^{2}k^{2}\psi\\
\frac{\partial^{2}\psi}{\partial z^{2}} &= -\gamma^{2}k^{2}\psi\\
\frac{\partial^{2}\psi}{\partial t^{2}} &= -\omega^{2}\psi\\
\end{align*}$$
ao somar as 3 primeiras equações obtemos: $$\frac{\partial^{2}\psi}{\partial x^{2}}+\frac{\partial^{2}\psi}{\partial y^{2}}+\frac{\partial^{2}\psi}{\partial z^{2}}=-k^{2}\psi$$
(sendo que $\alpha^{2}+\beta^{2}+\gamma^{2}=1$)
- Ora, temos que $v=\omega/k$ e obtemos a equação de onda em 3D:
$$\boxed{\frac{\partial^{2}\psi}{\partial x^{2}}+\frac{\partial^{2}\psi}{\partial y^{2}}+\frac{\partial^{2}\psi}{\partial z^{2}}= \frac{1}{v^{2}} \frac{\partial^{2}\psi}{\partial t^{2}}}$$
sendo que podemos escrever o termo da esquerda com o laplaciano: $$\nabla^{2}\psi=\frac{1}{v^{2}} \frac{\partial^{2}\psi}{\partial t^{2}}$$
- Devemos notar que temos 2 soluções gerais:
    - Uma onda a mover-se no sentido positivo de $\mathbf{k}$: $$\psi=f(\mathbf{r}\cdot \mathbf{k}/k-vt)$$
    - Uma onda a mover-se no sentido negativo de $\mathbf{k}$: $$\psi=g(\mathbf{r}\cdot \mathbf{k}/k+vt)$$
- Ora, todas as soluções desta equação diferencial não passam de combinações lineares destas 2:
$$\psi(\mathbf{r},t)=C_{1} f(\mathbf{r}\cdot \mathbf{k}/k-vt)+C_{2} g(\mathbf{r}\cdot \mathbf{k}/k+vt)$$

## 2.9 - Ondas Esféricas
- Quando algo cai em água geram-se ondas circulares em 2D.
- Vamos imaginar isto em 3D: temos uma esfera a pulsar, coberta por um fluido. Consoante a esfera se contrai e expande gera oscilações/ondas esféricas no fluido.
![[Attachments/FCUP/A3S1/OF/coordenadas esfericas.png|400]]
- Imaginemos agora uma fonte de luz pontual. Também esta gera ondas esféricas. Ora, parece óbvio que devemos estudar este caso em **coordenadas esféricas**:
$$\nabla^{2}= \frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial}{\partial r}\right) + \frac{1}{r^{2}\sin\theta} \frac{\partial}{\partial \theta}\left(\sin\theta \frac{\partial}{\partial \theta}\right) + \frac{1}{r^{2}\sin^{2}\theta} \frac{\partial^{2}}{\partial\phi^{2}}$$
em que
$$x=r\sin\theta\cos\phi~~,~~y=r\sin\theta\sin\phi~~,~~z=r\cos\theta$$
- Ora, no caso da fonte de luz pontual, temos ondas esféricas e que, portanto, não dependem de $\theta,\phi$. Ou seja fica:
$$\nabla^{2}\psi(r)=\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial\psi}{\partial r}\right)$$
(no Hecht há uma dedução deste termo do laplaciano ????)
- Podemos reescever isto como:
$$\nabla^{2}\psi(r)=\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial\psi}{\partial r}\right)=\frac{1}{r} \frac{\partial^{2}}{\partial r^{2}}(r\psi)$$
e a equação de onda 3D fica na forma:
$$\boxed{\frac{\partial^{2}}{\partial r^{2}}(r\psi)=\frac{1}{v^{2}} \frac{\partial^{2}}{\partial t^{2}}(r\psi)}$$
sendo que isto não passa de uma variação da equação 1D da Equação de Onda Diferencial em que função é $r \psi$. A solução desta equação diferencial é portanto:
$$r\psi(r,t)=f(r-vt)~~~~\to~~~~ \psi(r,t)=\frac{f(r-vt)}{r}$$
que será uma onda esférica a mover-se para longe do centro.
- Outra solução será uma onda esférica a mover-se em direção ao centro, tal que:
$$\psi(r,t)=\frac{g(r+vt)}{r}$$
ou seja, as soluções da equação de onda em coordenadas esféricas são uma combinação linear de:
$$\psi(r,t)=C_{1} \frac{f(r-vt)}{r} + C_{2} \frac{g(r+vt)}{r}$$

- Ora, um caso especial é a *onda harmónica esférica*:
$$\psi(r,t)= \left(\frac{\mathcal{A}}{r}\right)\cos k(r\mp vt)= \left(\frac{\mathcal{A}}{r} \right)e^{ik(r\mp vt)}$$
em que $\mathcal{A}$ é a força de fonte. 

- Na prática as frentes de onda consistem em várias superfícies esféricas concentricas a convergirem para a fonte ou a afastar-se dela. Dito isto, a frente de onda consiste nos conjuntos de pontos com o mesmo $kr$.
- Notemos agora que a amplitude **não** é constante. Temos $A=A(r)=\mathcal{A}/r$. Assim, a amplitude decai com $r$.
- Temos então:
![[ondas esfericas.png|350]]

- Por fim, outra observação a fazer é que, consoante o raio aumenta e as frentes de onda se afastam da fonte, temos que secções das frentes de onda são aproximadamente frentes de onda planas:
![[ondas esfericas para planas.png]]

## 2.10 - Ondas Cilíndricas
- Consideremos um cilindro infinito na direção $z$.
![[coordenadas cilindricas.png|300]]

- Comecemos por ver que o laplaciano em coordenadas cilindrícas tem a forma:
$$\nabla^{2}\psi= \frac{1}{r} \frac{\partial}{\partial r}\left( r \frac{\partial\psi}{\partial r}\right)+ \frac{1}{r^{2}} \frac{\partial^{2}\psi}{\partial\theta^{2}} + \frac{\partial^{2}\psi}{\partial z^{2}}$$
em que $x=r\cos\theta~~,~~ y=r\sin\theta~~,~~ z=z$

- Consideremos então que este cilindro está a pulsar e gera ondas. Por o cilindro sem infinito temos: $$\psi(\mathbf{r})=\psi(r,\theta,z)=\psi(r)$$
assim, temos que serão originadas ondas cilindricas coaxiais.

- Temos então que a equação de onda diferencial fica:
$$\frac{1}{r} \frac{\partial}{\partial r} \left(r- \frac{\partial\psi}{\partial r} \right)=\frac{1}{v^{2}} \frac{\partial^{2}\psi}{\partial t^{2}}$$
se reorganizarmos temos vemos que a equação passa a ser uma **equação de Bessel**. Ora, para $r$ suficientemente elevado as soluções dessa equação tornam-se funções trigonométricas:
$$\psi(r,t)\approx \frac{\mathcal{A}}{\sqrt{r}} e^{ik(r\mp vt)}$$
- Ao contrário de ondas planas e esféricas, não conseguimos definir as soluções deste caso a partir de funções arbitrárias.
- Tem-se ainda que, na realidade, para criar ondas cilíndricas é comum usar obstáculos com fendas muito finas:
![[ondas cilindricas fenda.png|400]]

## 2.11 - Luz Torcida
- Desde os anos 1900s que é possível gerar feixes de luz em espiral AKA luz torcida.
- Estas ondas possuem um termo de fase com $e^{i\ell\phi}$ em que $\ell$ é um inteiro.
- Nestas ondas temos algo assim:
![[luz torcida.png|475]]

- Na forma mais simples, temos uma onda em que a frente de onda segue uma espiral contínua em torno de um eixo central.
- Ora, nestas ondas $\phi$ é a **dependência azimutal da fase**.
- Podemos imaginar uma onda destas a ser intersetada por um plano, tal como fizemos atrás para mostrar ondas planas:
![[luz torcida v2.png|350]]
A linha a tracejado, em espiral, marca os máximos de cada "onda pequena". Ora, este será então o traçado da frente de onda.

- Vejamos outra coisa: na figura acima (das ondas pequenas intersetadas por um plano). Imaginemos que deslizamos cada uma destas ondas radialmente para o eixo central. Vemos que teríamos um sobreposição infinita de ondas, em que todas as fases estariam presentes. Assim, diz-se que o eixo é uma **singularidade de fase**. Aliás, para cada fase, temos do lado oposto do eixo uma outra onda com fase oposta (isto é visível na figura, a onda em cima de todo está num máximo e a de baixo num mínimo).