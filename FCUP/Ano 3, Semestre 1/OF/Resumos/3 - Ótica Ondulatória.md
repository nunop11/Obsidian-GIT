## 3.1 - Polarização
- Para uma onda EM, a direção de polarização é a direção paralela ao campo (a direção em que o campo oscila).

### 3.1.1 - Polarização Linear
![[polarizacao campo.png]]
- Temos luz polarizada linearmente quando o campo E oscila numa direção perpendicular à direção de propagação. Temos ainda que as 2 componentes estão em fase.
- Temos
$$\vec{E}(\vec{r},t)=\vec{E}_{x}(\vec{r},t)+\vec{E}_{y}(\vec{r},t)$$
em que (para uma onda a propagar-se nos zz):
$$\begin{align*}
\vec{E}_{x}(\vec{r},t)&= E_{x0}\sin(kz-\omega t+\phi)\hat{x}\\
\vec{E}_{y}(\vec{r},t)&= E_{y0}\sin(kz-\omega t+\phi)\hat{y}
\end{align*}$$
ou seja, podemos escrever:
$$\begin{align*}
\vec{E}(\vec{r},t)&= (E_{x0}\hat{x}+E_{y0}\hat{y})\sin(kz-\omega t+\phi)\\
&= E_{0}\hat{u}\sin(kz-\omega t+\phi)
\end{align*}$$
em que
$$E_{0}=\sqrt{E_{x0}^{2}+E_{y0}^{2}} \quad \quad;\quad \quad \hat{u}=\frac{E_{x0}\hat{x}+E_{y0}\hat{y}}{\sqrt{E_{x0}^{2}+E_{y0}^{2}}}$$

### 3.1.2 - Polarização Circular
- Ocorre quando as componentes têm a mesma amplitude mas uma diferenºa de fase de $\frac{\pi}{2}$:
$$\begin{align*}
\vec{E}_{x}(\vec{r},t)&= E_{0}\sin(kz-\omega t+\phi)\hat{x}\\
\vec{E}_{y}(\vec{r},t)&= E_{0}\sin\left(kz-\omega t+\phi\pm \frac{\pi}{2}\right)\hat{y}
\end{align*}$$
que resulta em:
$$\vec{E}(\vec{r},t)= E_{0}[\hat{x}\sin(kz-\omega t+\phi)\pm\hat{y}\cos(kz-\omega t+\phi)]$$
em que temos
$$\hat{u}(\vec{r},t)=\hat{x}\sin(kz-\omega t+\phi)\pm \hat{y}\cos(kz-\omega t+\phi)$$
![[Attachments/FCUP/A3S1/OF/polarizacao circular.png]]

- Podemos escrever uma onda com polarização linear como sendo a soma de 2 ondas com polarização circular a rodar em sentido oposto:
$$\begin{align*}
\vec{E}&= \vec{E}_{1}+\vec{E}_{2}\\
&= E_{0}[\hat{x}\sin(kz-\omega t+\phi)\pm\hat{y}\cos(kz-\omega t+\phi)] + E_{0}[\hat{x}\sin(-(kz-\omega t+\phi))\pm\hat{y}\cos(-(kz-\omega t+\phi))]\\
&= E_{0}[\hat{x}\cancel{\sin(kz-\omega t+\phi)}\pm\hat{y}\cos(kz-\omega t+\phi)] + E_{0}[-\hat{x}\cancel{\sin(kz-\omega t+\phi)}\pm\hat{y}\cos(kz-\omega t+\phi)]\\
&= \pm 2E_{0}\cos(kz-\omega t+\phi)\hat{y}
\end{align*}$$
![[polarizações circulares opostas.png]]

- A polarização circular pode ser caraterizada como esquerda (negativa) ou direita (positiva). Vejamos convenções:

#### Perspetiva da Fonte
- Colocamos o polegar direito a apontar na mesma direção da propagação da onda, $\hat{u}$. Se a rotação da polarização seguir os restantes dedos temos polarização circular *direita*. Senão temos *esquerda*.
- Por outras palavras, é como se estivessemos na fonte ("parte de trás" da onda) e vemos a polarização a rodar em sentido horário, em cima vai para a direita.

#### Perspetiva do Recetor
- Convenção usada na ótica!
- Fazemos o oposto. Colocamos o polegar direito a apontar para a fonte (sendito $-\hat{u}$). De resto é igual ao que temos acima, mas será tudo ao contrário.

### 3.1.3 - Polarização Elíptica
- Igual à polarização circular, mas as componentes têm amplitudes diferentes:
$$\begin{align*}
\vec{E}_{x}(\vec{r},t)&= E_{x0}\sin(kx-\omega t)\hat{x}\\
\vec{E}_{y}(\vec{r},t)&= E_{y0}\sin(kz-\omega t+\varphi)\hat{y}
\end{align*}$$
- Podemos obter:
$$\begin{align*}\\
\frac{E_{x}}{E_{x0}}&= \sin(kz-\omega t)\\
\frac{E_{y}}{E_{y0}}&= \sin(kz-\omega t+\varphi)=\sin(kz-\omega t)\cos\varphi + \cos(kz-\omega t)\sin\varphi
\end{align*}$$
e podemos substituir a equação de x na de y:
$$\begin{align*}
\frac{E_{y}}{E_{y0}}&= \frac{E_{x}}{E_{x0}}\cos\varphi + \cos(kz-\omega t)\sin\varphi\\
\frac{E_{y}}{E_{y0}} -\frac{E_{x}}{E_{x0}}\cos\varphi &= \cos(kz-\omega t)\sin\varphi
\end{align*}$$
podemos ainda escrever $\cos^{2}(kz-\omega t)=1- \left(\frac{E_{x}}{E_{x0}}\right)^{2}$, ficando com:
$$\begin{align*}
\frac{E_{y}}{E_{y0}} -\frac{E_{x}}{E_{x0}}\cos\varphi &= \sqrt{1- \left(\frac{E_{x}}{E_{x0}}\right)^{2}}\sin\varphi\\
\left(\frac{E_{y}}{E_{y0}}\right)^{2}-2 \frac{E_{y}}{E_{y0}}\frac{E_{x}}{E_{x0}}\cos\varphi + \left(\frac{E_{x}}{E_{x0}}\right)^{2}\cos\varphi^{2}&= \sin^{2}\varphi - \left(\frac{E_{x}}{E_{x0}}\right)^{2}\sin^{2}\varphi\\
\left(\frac{E_{y}}{E_{y0}}\right)^{2} + \left(\frac{E_{x}}{E_{x0}}\right)^{2}-2 \frac{E_{y}}{E_{y0}}\frac{E_{x}}{E_{x0}}\cos\varphi &= \sin^{2}\varphi
\end{align*}$$
- Podemos ainda determinar que se tem:
$$\tan2\alpha=\frac{2E_{x0}E_{y0}\cos\varphi}{E_{x0}^{2}-E_{y0}^{2}}$$
![[Attachments/FCUP/A3S1/OF/polarizacao eliptica.png]]

### 3.1.4 - Polarização Incoerente
(AKA Polarização Aleatória)
- Temos simplesmente
$$\vec{E}(\vec{r},t)=E_{0}\sin(kz-\omega r+\phi)\hat{u}$$
em que $\hat{u}$ tem direção aleatória com média nula.
- Este é o tipo de polarização daquela que chamamos "luz não polarizada".

### 3.1.5 - Estados de Polarização
- Podemos então referir-nos a uma onda usando o seu estado de polarização:
    - Luz linearmente polarizada está em estado $\mathcal{P}$
    - Luz polarizada circularmente à direita está em estado $\mathcal{R}$
    - Luz polarizada circularmente à esquerda está em estado $\mathcal{L}$
    - Luz elipticamente polarizada está em estado $\mathcal{E}$
- Tal como vimos para estado $\mathcal{P}$, o estado $\mathcal{E}$ pode ser obtido com sobreposição de estados $\mathcal{R},\mathcal{L}$.

### 3.1.6 - Vetor de Jones
- Constitui uma forma de caraterizar o estado de polarização sem que a escola de eixos e convenção importe.
- Temos as componentes x,y do campo:
$$\begin{align*}
\vec{E}_{x}(\vec{r},t)&= E_{x0}\exp[i(kz-\omega t+\phi_{x})]\hat{x}\\
\vec{E}_{y}(\vec{r},t)&= E_{y0}\exp[i(kz-\omega t+\phi_{y})]\hat{y}
\end{align*}$$
- E podemos escrever o campo elétrico como:
$$\begin{align*}
\vec{E}&= \vec{E_{x}}+\vec{E_{y}}\\
&= E_{x0}\exp[i(kz-\omega t+\phi_{x})]\hat{x} + E_{y0}\exp[i(kz-\omega t+\phi_{y})]\hat{y}\\
&= E_{0}\exp[i(kz-\omega t)] \left(\frac{E_{x0}}{E_{0}}\exp[i\phi_{x}]\hat{x} + \frac{E_{y0}}{E_{0}}\exp[i\phi_{y}]\hat{y}\right)\\
&= E_{0} \begin{bmatrix}\frac{E_{x0}}{E_{0}}\exp[i\phi_{x}]\\\frac{E_{y0}}{E_{0}}\exp[i\phi_{y}] \end{bmatrix}\exp[i(kz-\omega t)]
\end{align*}$$
em que temos o vetor de Jones:
$$\vec{J}=\begin{bmatrix}\frac{E_{x0}}{E_{0}}\exp[i\phi_{x}]\\\frac{E_{y0}}{E_{0}}\exp[i\phi_{y}] \end{bmatrix}$$
- Tabiêla:
$$\begin{array}{c|c} \text{Estado de polarização} & \text{Vetor de Jones} \\[10pt] \hline \\[5pt] \text{Polarização linear horizontal} & \begin{bmatrix} +1 \\[5pt] 0 \end{bmatrix} \\[20pt] \text{Polarização linear vertical} & \begin{bmatrix} 0 \\[5pt] +1 \end{bmatrix} \\[20pt] \text{Polarização linear }+45^\circ & \frac{1}{\sqrt2}\begin{bmatrix} +1 \\[5pt] +1 \end{bmatrix} \\[20pt] \text{Polarização linear }-45^\circ & \frac1{\sqrt2}\begin{bmatrix} +1 \\[5pt] -1 \end{bmatrix} \\[20pt] \text{Polarização circular direita} & \frac1{\sqrt2}\begin{bmatrix} +1 \\[5pt] -i \end{bmatrix} \\[20pt] \text{Polarização circular esquerda} & \frac1{\sqrt2}\begin{bmatrix} +1 \\[5pt] +i \end{bmatrix} \end{array}$$

### 3.1.7 - Estados de Polarização Ortogonais
- Tendo o vetor de jones $\vec{J}_{A}$ de um estado $A$ e o vetor $\vec{J}_{B}$ de um estado $B$. 
- Estes 2 estados de polarização são ortogonais se:
$$\vec{J}_{A}\cdot\vec{J}_{B}^{*}=0$$
- Sendo que qualquer estado tem um estado ortogonal associado e podemos escrever qualquer estado como uma combinação linear de estados ortogonais. (Sim, isto tem uma lógica parecida a estados quânticos)
- Para calcular isto usamos as matrizes como vetores:
$$\vec{J}_\mathcal{R} \cdot \vec{J}_\mathcal{L}^{*}= \begin{pmatrix}1\\ -i\end{pmatrix}\cdot \begin{pmatrix}1\\ i\end{pmatrix}^{*}=(1,-i)\cdot(1^{*},i^{*})=1\cdot 1^{*}+(-i)\cdot i^{*}=1 + (-i)^{2}=0$$

### 3.1.7 - Matriz de Jones
- Temos a matriz de transformação de um elemento ótico $\mathcal{A}$, $\vec{J_{i}}$ o vetor de Jones de um feixe incidente.
- O vetor de Jones do vetor transmitido através do elemento ótico é:
$$\vec{J}_{t}=\mathcal{J}\vec{J}_{i}$$

- Isto pode facilmente ser expandido para uma configuração de $n$ elementos óticos:
$$\vec{J}_{t}=\mathcal{A}_{n}\cdots\mathcal{A}_{2}\mathcal{A}_{1}\vec{J_{i}}$$

### 3.1.8 - Retardador de Fase
- Lâminas retardadoras (ou retardadoras de fase) são elementos óticos que afetam a polarização da luz ao alterar a diferença de fase entre as componentes.
- Geralmente feitos de materiais anisotrópicos.
- Temos
$$\vec{J}=\begin{pmatrix}e^{i\phi_{x}} & 0 \\  0 & e^{i\phi_{y}}\end{pmatrix}$$
em que se introduz um atraso de fase $\phi_{x},\phi_{y}$ nas compontens x,y.

## 3.2 - Polarizadores
- Dispositivo ótico que transforma luz em luz polarizada, pelo que de um polarizador sai luz no estado $\mathcal{P}$, sendo que apenas passa a componente do campo com a mesma direção do eixo de transmissão do polarizador.
- Para luz natural, presume-se que rodar um polarizador em torno de z apenas afeta a direção do campo que dele sai, mas não a intensidade (porque se assume que luz natural tem polarização perfeitamente aleatória)

### 3.2.1 - Lei de Malus
![[lei de malus montagem.png]]
- Temos 2 polarizadores em série. O segundo polarizador atua como um *analisador*, ficando com o eixo de transmissão vertical.
- O campo elétrico que passa do polarizador tem amplitude $E_{01}$. Quando este chega ao analisador, apenas a componente $E_{01}\cos\theta$ passa, em que $\theta$ é o ângulo entre os eixos de transmissão do polarizador e do analisador.
- A Lei de Malus (Não confundir com o teorema de Malus da ótica geométrica!) diz-nos que a intensdiade medida num detetor colocado a seguir ao analisador será:
$$I(\theta)= \frac{1}{2}c\varepsilon_{0}E_{01}^{2}\cos^{2}\theta=I(0)\cos^{2}\theta$$


## 3.3 - Birrefringência
- Propriedade ótica de cristais em que o índice de refração depende da direção de propagação E da polarização.
- Torna-se necessário usar tensores :D

## 3.4 - Modos Espaciais
- Modo estacionario do campo EM, normalmente obtido com o estado próprio de um operador diferencial hermítico.
- O conjunto de estado próprios forma uma base ortonormada e completa que permite escrever qualquer campo como sobreposição de modos.

### 3.4.1 - Decomposição Modal
- Decomposição modal consiste na decomposição de uma solução da Eq de Onda num conjunto de modos espaciais. O exemplo mais comum é a transformada de Fourier.

#### Equação para o Modo Espacial
- Temos a equação $\nabla \times (\nabla \times \vec{A})= \nabla (\nabla \cdot \vec{A}) - \nabla^{2}A$
- Assim, considerando um meio em que $\rho=0$ podemos escrever a equação de onda como:
$$\nabla \times \nabla \times \vec{E}=-\mu_{0}\varepsilon_{0}\partial_{t}^{2}\vec{E}$$
e temos soluções do tipo
$$\vec{E}=\vec{E}(\vec{r},t)=\exp(-i\omega t)\vec{u}(\vec{r})$$
em que $\vec{u}(\vec{r})$ é um **modo espacial**.
- Estes sao definidos pela operação:
$$\hat{D}\vec{u}(\vec{r})=\lambda\vec{u}(\vec{r})$$
em que $\hat{D}$ é um operador diferencial e $\lambda$ o valor próprio associado a $\vec{u}$.

- Podemos ainda generalizar esta equação para quando $\varepsilon_{r}$ depende do espaço:
$$\frac{c^{2}}{\varepsilon_{r}(\vec{r})}\nabla \times\nabla\times \vec{u}(\vec{r})=\omega^{2}\vec{u}(\vec{r})$$
em que vemos que $\hat{D}=\frac{c^{2}}{\varepsilon_{r}(\vec{r})}\nabla \times\nabla\times$, sendo que este operador não é hermítico, pelo que não podemos gerar uma base completa do campo EM com os seus vetores e valores próprios.

- Substituindo $\vec{v}(\vec{r})=\sqrt{\varepsilon_{r}(\vec{r})} \vec{u}(\vec{r})$ podemos reescrever a equação:
$$\frac{c}{\sqrt{\varepsilon_{r}(\vec{r})}} \nabla \times \nabla \times \frac{c}{\sqrt{\varepsilon_{r}(\vec{r})}}\vec{v}(\vec{r})=\omega^{2}\vec{v}(\vec{r})$$
em que agora temos um operador $\hat{D}=\frac{c}{\sqrt{\varepsilon_{r}(\vec{r})}} \nabla \times \nabla \times \frac{c}{\sqrt{\varepsilon_{r}(\vec{r})}}$ que é hermítico.

- Teoricamente, não podemos definir o campo elétrico como sendo uma combinação de uma função escalar e uma vetorial. Mas iremos fazer esta aproximação, trabalhando com ondas escalares, onde temos a equação de onda:
$$\nabla^{2}\phi- \frac{1}{c^{2}}\partial_{t}^{2}\phi=0$$

## 3.5 - Ondas Planas
- Consideremos uma onda a mover-se nos zz:
$$\nabla_{z}^{2}\phi- \frac{1}{c^{2}}\partial_{t}^{2}\phi=0$$
que resulta na solução geral:
$$\phi(z,t)=a f(z-ct)+b g(z+ct)$$

### 3.5.1 - Solução Particular
- Uma solução particular que conhecemos bem é aquela que deifne as ondas planas. Esta consiste em ondas em que $\vec{k}\cdot\vec{r}=constante$
- Temos então:
$$\phi(\vec{r},t)=\phi_{0}\exp[i(\vec{k}\cdot\vec{r}-\omega t+\theta)]$$

## 3.6 - Ondas Esféricas
- Temos o laplaciano em coordenadas esférica
$$\begin{align*}
\nabla^2 \phi &= \frac1{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial \phi}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta \frac{\partial \phi}{\partial \theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2\phi}{\partial \varphi^2}
\end{align*}$$
- Ondas esféricas propagam-se de forma radial a partir do centro, pelo que que $\phi$ não depende de $\theta,\varphi$. Temos então:
$$\nabla^{2}\phi=\frac{1}{r}\partial_{r}^{2}(r\phi)$$
e a equação de onda fica
$$\frac{1}{r}\partial_{r}^{2}\phi- \frac{1}{c^{2}}\partial_{t}^{2}\phi=0$$
que nos dá a solução geral:
$$\phi(\vec{r},t)= \frac{a}{r}f(r-ct)+ \frac{b}{r}g(r+ct)$$
- Temos a solução particular:
$$\phi(\vec{r},t)=\frac{A_{0}}{r}\exp[i(kr-\omega t+\theta)]$$
em que um grupo de pontos com a mesma fase é deifnido por $kr$ constante.

## 3.7 - Ondas Cilíndricas
- Ondas cilíndricas propagam-se a partir de um eixo central, não dependendo de $\theta$. Assim, o laplaciano fica
$$\nabla^{2}\phi= \frac{1}{\rho} \partial_\rho(\rho\partial_{\rho}\phi) + \partial_{z}^{2}\phi$$
- Temos os modos espaciais do operador diferencial $\frac{1}{\rho}\partial_{\rho}(\rho\partial_\rho)$:
$$\frac{1}{\rho}\partial_{\rho}(\rho\partial_{\rho)}\phi(\rho,z)=\mu^{2}\phi(\rho,z)$$
e podemos escrever a equação de onda
$$\mu^{2}\phi+\partial_{z}^{2}\phi- \frac{1}{c^{2}}\partial_{t}^{2}\phi=0$$
- Uma solução desta equação é
$$\phi(\rho,z,t)=a \varphi(\rho)f(\beta z-\omega t) + b\varphi(\rho)g(\beta z+\omega t)$$
- Temos então a solução particular:
$$\phi(\rho,z,t)=\varphi(\rho)\exp[i(\beta z-\omega t+\varphi_{0})]$$
que ao substituir na equação de onda nos dá
$$\mu^{2}- \beta^{2}+ \frac{1}{c^{2}}\omega^{2}=0$$
- Se $\mu^2 + c^{-2}\omega^2 >0$, $\beta$ é real e a solução corresponde a ondas que se propagam ao longo do eixo $zz'$.
- Se $\mu^2 + c^{-2}\omega^2 <0$, $\beta$ é imaginário e a solução corresponde a ondas evanescentes.
- Se $\mu^2 > c^{-2}\omega^2$ e $\beta = 0$, obtém-se ondas que correspondem a uma onda emitida no eixo $zz'$ e que se propaga para fora segundo a direção radial e perpendicular a $zz'$.

## 3.8 - Feixes Gaussianos
- Feixe de radiação Em monocromática. Os perfis transversais de amplitude do campo EM são dados por uma função de Gauss (distribuição normal, como vimos em feixes de luz, mais atrás)
- Partindo da equação $\frac{c}{\sqrt{\varepsilon_{r}(\vec{r})}} \nabla \times \nabla \times \frac{c}{\sqrt{\varepsilon_{r}(\vec{r})}}\vec{v}(\vec{r})=\omega^{2}\vec{v}(\vec{r})$ e usando a identidade $\nabla \times (\nabla \times \vec{A})= \nabla (\nabla \cdot \vec{A}) - \nabla^{2}A$ podemos obter:
$$\nabla^{2}\vec{u}(\vec{r})=-k^{2}\vec{u}(\vec{r}) \quad \quad;\quad \quad k^{2}=\frac{\varepsilon_{r}\omega^{2}}{c^{2}}$$
- Temos uma solução do tipo:
$$\vec{u}(\vec{r})=\psi(\vec{r})e^{ikz}\vec{u_{0}}$$

- Podemos calcular o Laplaciano da solução:
$$\begin{align*}
\nabla^{2}\vec{u}(\vec{r})= (\nabla^{2}\psi(\vec{r}))\exp[ikz]+ 2ikz[\vec{u_{z}}\cdot\nabla \psi(\vec{r})]\exp[ikz]-k^{2}\psi(\vec{r})\exp[ikz]
\end{align*}$$
que podemos substituir na equação $\nabla^{2}\vec{u}(\vec{r})=-k^{2}\vec{u}(\vec{r})$ e resulta que:
$$\nabla^{2}\psi(\vec{r})+2ik[\vec{u_{z}}\cdot\nabla\psi(\vec{r})]=0$$
e temos soluções:
$$\psi(\textbf r) = \frac{\omega_0}{\omega(z)} \exp\left[-\frac{r^2}{\omega^2(z)}\right]\exp\left[ik\frac{r^2}{2R(z)} + i\phi(z)\right]$$
com
$$\omega(z) = \sqrt{1 + \left(\frac{z}{z_{R}}\right)^{2}} \quad \quad;\quad \quad R(z) = z\left[1+ \left(\frac{z}{z_{R}}\right)\right] \quad \quad;\quad \quad z_{R}=\frac{\pi\omega_{0}^{2}}{\lambda}$$
- Este modo espacial corresponde ao feixe de saída de muitos lasers.
- Ou seja, determinamos a solução mais trivial da equação de onda $\nabla^{2}\vec{u}(\vec{r})=-k^{2}\vec{u}(\vec{r})$  e substitui-mo-la na equação, o que nos permitiu obter uma equação de onda escalar e que nos deu $\psi(\vec{r})$.

#### Foco do Feixe
- A posição $z_{0}$ é a posição em que o feixe tem menor largura, sendo muitas vezes chamado de foco.

#### Perfil de Amplitude
- Substituindo a equação de $\psi(\vec{r})$ de volta na solução $\vec{u}(\vec{r})=\psi(\vec{r})\exp(ikz)\vec{u_{0}}=\varphi(\vec{r})$ obtemos:
$$\varphi(\textbf r) = \frac{\omega_0}{\omega(z)} \exp\left[-\frac{r^2}{\omega^2(z)}\right]\exp\left[ikz + ik\frac{r^2}{2R(z)} + i\phi(z)\right]$$
## 3.9 - Cavidades Óticas e Guias de Onda
- O modo espacial do feixe gaussiano constitui uma classes de modos espaciais.
- Outra classe importante é a de ondas estacionárias guiadas.

### 3.9.1 - Ondas Estacionárias
- Temos uma onda EM plana e monocromática assim
![[refelxao onda EM.png]]
- A única condição de fronteira é que o campo elétrico tem que ser nulo na superfície do condutor, ou seja
$$\vec{E}(\vec{r},t)\biggr|_{x=0}=\vec{0}$$

- Temos então que a solução geral da Eq de Onda EM é:
$$\vec{E}(\vec{r},t)=\vec{E_{+}}\sin(kz-\omega t+\phi_{+})+ \vec{E_{-}}\sin(kx+\omega t+\phi_{-})$$
pelo que só satisfazemos a condição de fronteira se $\phi_{-}=\phi_{+}$ e $E_{+}=-E_{-}=E_{0}\vec{u_{y}}$
- Ou seja, podemos escrever
$$\vec{E}(\vec{r},t)=2\vec{E_{0}}\sin(kx)\cos(\omega t)$$
pelo que, como $\nabla\times\vec{E}=-\partial_{t}\vec{B}$ temos
$$\vec{B}(\vec{r},t)=2\vec{B_{0}}\cos(kx)\cos(\omega t) \quad \quad;\quad \quad \vec{B_{0}}=\frac{E_{0}}{c}\vec{u_{y}}$$
e temos as distibuições espaciais: $$2E_{0}\sin(kx) \quad \quad;\quad \quad 2B_{0}\cos(kx)$$
ou seja, o perfim de amplitude (que são as oscilações espaciais) não depende do tempo, pelo que temos um perfil fixo - ondas **estacionárias**

- Consideremos agora que a onda está fechada dentro de uma caixa de dimensões $L_{x},L_{y},L_{z}$, sendo as paredes feitas de condutor ideal.
- Pela mesma lógica que acima teríamos
$$\vec{E}(\vec{r},t)=2\vec{E_{0}}\sin(k_{x}x)\sin(k_{y}y)\sin(k_{z}z)\cos(\omega t)$$
em que $\omega^{2}=\frac{1}{c^{2}}(k_{x}^{2}+k_{y}^{2}+k_{z}^{2})$ e $k_{i}L_{i}=n_{i}\pi$
- A situações como esta chamamos de *cavidades óticas*

### 3.9.2 - Ondas Guiadas
![[onda guiada.png]]
- Temos um cavidade constituida por 2 superfícies planas de condutores ideais.
- Temos que, num sistema assim, as ondas são introduzidas de um lado e chegam ao outro quase sem perdas.

- Temos as condições de fronteira:
$$\vec{E}(\vec{r},t)\biggr|_{x=0}=\vec0=\vec{E}(\vec{r},t)\biggr|_{x=L_{x}}$$
- Se resolvermos a equação de onda por separação de variáveis obtemos:
$$\vec{E}(\vec{r},t)=2\vec{E_{0}}\sin(k_{x}x)\sin(k_{y}y)\sin(k_{z}z)\cos(\omega t)$$
em que $\omega^{2}=\frac{1}{c^{2}}(k_{x}^{2}+k_{y}^{2}+k_{z}^{2})$ e $k_{i}L_{i}=n_{i}\pi$

- A diferença de ondas guiadas para ondas estacionárias como a que vimos acima é:
    - Na direção $\vec{k}_{\parallel}=k_{x}\vec{u_{x}}$ temos uma onda estacionária.
    - Na direção $\vec{k}_{\perp}=k_{y}\vec{u_{y}}+k_{z}\vec{u_{z}}$ temos uma onda propagante.

- A *velocidade de fase* da componente propagante é
$$v_{f}=\frac{\omega}{k_{\perp}}=c \frac{k}{k_{\perp}}=c \sqrt{\frac{k_{\perp}^{2}+\frac{n^{2}\pi^{2}}{L_{x}^{2}}}{k_{\perp}^{2}}}$$
em que se usou
$$\begin{align*}
k_{\perp}^{2}+k_{\parallel}^{2} &= k^{2}\\
k_{\perp}^{2}+ \frac{n^{2}\pi^{2}}{L_{x}^{2}} &= k^{2}=\frac{\omega^{2}}{c^{2}}\\
k_{\perp}= \sqrt{\frac{\omega^{2}}{c^{2}}-\frac{n^{2}\pi^{2}}{L_{x}^{2}}} \quad\quad&;\quad\quad k= \sqrt{k_{\perp}^{2}+\frac{n^{2}\pi^{2}}{L_{x}^{2}}} 
\end{align*}$$

- E a *velocidade de grupo*:
$$\begin{align*}
v_{g}=\frac{\partial\omega}{\partial k_{\perp}}&= \frac{\partial}{\partial k_{\perp}} \left(c \sqrt{k_{\perp}^{2}+\frac{n^{2}\pi^{2}}{L_{x}
^{2}}} \right)\\
&= \frac{1}{2}\frac{c}{\sqrt{k_{\perp}^{2}+\frac{n^{2}\pi^{2}}{L_{x}
^{2}}}} \cdot 2k_{\perp} \\
&= \frac{k_{\perp}c}{k}<c
\end{align*}$$
e temos que
$$v_{f}\cdot v_{g}=c^{2}$$

- Temos $k_{\perp}= \sqrt{\frac{\omega^{2}}{c^{2}}-\frac{n^{2}\pi^{2}}{L_{x}^{2}}}$. Para que isto seja real (e não tenhamos uma onda evanescente na direção $\perp$) é preciso que:
$$\frac{\omega^2}{c^2} \ge \frac{n^2 \pi^2}{L_x^2} ~~\to~~ \omega \ge \frac{cn\pi}{L_x}\equiv \omega_c$$
em que $\omega_{c}$ é a **frequência de corte**, abaixo da qual é impossível ter propagação guiada. Ou seja, um guia de onda atua como um filtro de frequências.

## 3.10 - Sobreposição, Interferência, Batimentos
- Como já vimos a sobreposição de 2 ondas também será uma onda real (solução da Eq de Onda).
- Sobreposições de ondas planas resultam em interferêcias.

### 3.10.1 - Sobreposição de ondas escalares
- Consideremos 2 ondas escalares a propagar em z:
$$\phi_{1}=\phi_{01}\sin(kz-\omega t+\varphi_{1}) \quad \quad;\quad \quad \phi_{2}=\phi_{02}\sin(kz-\omega t+\varphi_{2})$$
- E temos
$$\begin{align*}
\phi(z,t)&= \phi_{1}(z,t)+\phi_{2}(z,t)\\
&= \phi_{01}\sin(kz-\omega t+\varphi_{1}) + \phi_{02}\sin(kz-\omega t+\varphi_{2}) 
\end{align*}$$
