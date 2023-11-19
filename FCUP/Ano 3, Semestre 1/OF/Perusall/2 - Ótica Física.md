# 2 - Ótica Física
## 2.1 - Luz como fenómeno Magnético
- Temos as equações de Maxwell:
$$\boxed{\begin{align*}
\nabla \cdot \vec{E}&= \frac{\rho}{\varepsilon_{0}}\\
\nabla \cdot \vec{B}&= 0\\
\nabla \times \vec{B}&= \mu_{0}\vec{\mathcal{J}} + \varepsilon_{0}\mu_{0} \partial_{t}\vec{E}\\
\nabla \times \vec{E}&= - \partial_{t}\vec{B}
\end{align*}}$$
- Temos as constantes: 
    - permissividade elétrica - $\varepsilon_{0}=8.854\cdot10^{-12}C^{2}/NM^{2}$
    - permeabilidade magnética - $\mu_{0}=4\pi\cdot10^{-7}Tm/A$

- A luz segue estas equações, sendo uma onda eletromagnética com frequência mutio alta e velocidade $c\simeq3\cdot10^{8}m/s$.

### 2.1.1 - Equações de Maxwell para Ótica
- Partindo das equações de Maxwell conseguimos obter as equações que descrevem ondas eletromagnéticas.

#### Divergência das Equações
- Partindo da *Equação de Faraday*:
$$\nabla \times \vec{E}=- \partial_{t}\vec{B}$$
podemos tomar a divergência dos 2 lados:
$$\nabla \cdot (\nabla \times \vec{E})=0=\nabla \cdot (-\partial_{t}\vec{B})$$
em que $\nabla \cdot (\nabla \times \vec{A})=0$ para qualquer campo vetorial.

- Podemos então reescrever:
$$\partial_{t}(\nabla \cdot \vec{B})=0$$
- Isto é concordante com a 2ª equação de Maxwell. Mais concretamente, esta equação diz-nos que esta equação é constante e verdadeira em todo o tempo.

- Passemos agora à *equação de Ampere-Maxwell*:
$$\nabla \times \vec{B}=\mu_{0} \vec{\mathcal{J}} + \varepsilon_{0}\mu_{0}\partial_{t}\vec{E}$$
e façamos a sua divergência:
$$\nabla \cdot (\nabla \times \vec{B})=0=\mu_{0} (\nabla \cdot \vec{\mathcal{J}}) + \mu_{0}\varepsilon_{0}\partial_{t}(\nabla \cdot \vec{E})$$
que, reorganizando e substituindo a 1ª equação de Maxwell, nos dá:
$$\nabla \cdot \vec{\mathcal{J}}+\partial_{t}\rho=0\to \nabla \cdot \vec{\mathcal{J}}=- \partial_{t}\rho$$
sendo que esta é a **equação da continuidade de carga**. Ou seja, para que a equação de Ampere-Maxwell seja válida e compatível com as outras equações de Maxwell, é necessário que haja conservação de carga. Inversamente, as equações de Maxwell são consistentes *se* houver conservação da carga.

#### Rotacional das Equações
- Voltemos à equação de Faraday e façamos o seu rotacional:
$$\nabla \times (\nabla \times \vec{E})=- \nabla \times \partial_{t}\vec{B}$$
sendo que $\nabla \times (\nabla \times \vec{A})=\nabla(\nabla \cdot \vec{A})-\nabla^{2}\vec{A}$ podemos escrever:
$$\nabla(\nabla \cdot \vec{E})-\nabla^{2}\vec{E}=- \partial_{t}(\nabla \times \vec{B})$$
Substituindo a equação de Ampere-Maxwell em $\nabla \times \vec{B}$ e a 1ª equação de Maxwell em $\nabla \cdot \vec{E}$ obtemos:
$$\begin{align*}
\nabla\left(\frac{\rho}{\varepsilon_{0}}\right)- \nabla^{2} \vec{E}&= -\mu_{0}\partial_{t}(\vec{\mathcal{J}}) - \mu_{0}\varepsilon_{0} \partial_{t}^{2}\vec{E}\\
\frac{1}{c^{2}}\partial_{t}^{2}\vec{E}-\nabla^{2}\vec{E}&= -\frac{1}{\varepsilon_{0}}\nabla \rho - \mu_{0} \partial_{t}\vec{\mathcal{J}}
\end{align*}$$
(em que se usou $\mu_{0}\varepsilon_{0}=1/c^{2}$)

- Agora o rotacional da equação de Ampere-Maxwell:
$$\nabla \times(\nabla \times \vec{B})=\mu_{0} (\nabla \times \vec{\mathcal{J}}) + \mu_{0}\varepsilon_{0} \partial_{t}(\nabla \times \vec{E})$$
podemos escrever:
$$\nabla (\nabla \cdot \vec{B})- \nabla^{2} \vec{B}=\mu_{0}(\nabla \times \vec{\mathcal{J}}) + \mu_{0}\varepsilon_{0}\partial_{t}(\nabla \times \vec{E})$$
em que podemos usar $\nabla \cdot \vec{B}=0$ (2ª equação Maxwell) e substituir a equação de Faraday em $\nabla \times \vec{E}$ e temos:
$$\begin{align*}
-\nabla^{2}\vec{B}&= \mu_{0}(\nabla \times \vec{\mathcal{J}}) -\mu_{0}\varepsilon_{0} \partial_{t}^{2}\vec{B}\\
\frac{1}{c^{2}}\partial_{t}^{2}\vec{B}-\nabla^{2}\vec{\mathcal{J}}&= \mu_{0}(\nabla \times \vec{\mathcal{J}})
\end{align*}$$
(em que se usou $\mu_{0}\varepsilon_{0}=1/c^{2}$)

- Temos então as 2 equações de Maxwell que descrevem ondas eletromagnéticas (???) 

### 2.1.2 - Ondas Eletromagnéticas no vazio

#### Campo Elétrico
- Começamos por tomar o rotacional da equação de Faraday:
$$\nabla \times(\nabla \times \vec{E})=-\nabla \times \partial_{t}\vec{B}=-\partial_{t}(\nabla \times \vec{B})$$
substituindo $\nabla \times \vec{B}$ pela equação de Ampere-Maxwell e considerando $\mathcal{\vec{J}}=0$ temos:
$$\nabla \times \nabla \times \vec{E}=- \mu_{0}\varepsilon_{0}\partial_{t}^{2}\vec{E}$$
em que podemos usar a identidade $\nabla \times (\nabla \times \vec{A})=\nabla(\nabla \cdot \vec{A})-\nabla^{2}\vec{A}$ e temos:
$$\begin{align*}
\nabla(\nabla \cdot \vec{E}) - \nabla^{2}\vec{E}&= - \mu_{0}\varepsilon_{0}\partial_{t}^{2}\vec{E}\\
\nabla\left(\frac{\rho}{\varepsilon_{0}}\right)-\nabla^{2}\vec{E}&= - \mu_{0}\varepsilon_{0}\partial_{t}^{2}\vec{E}
\end{align*}$$
assumindo que estamos no vazio e temos $\rho=0$, obtemos a **equação de onda para o campo elétrico** no vazio:
$$\nabla^{2}\vec{E}-\mu_{0}\varepsilon_{0}\partial_{t}^{2}\vec{E}=0 \Longleftrightarrow \nabla^{2}\vec{E} = \frac{1}{c^{2}} \partial^{2}_{t}\vec{E}$$

**Solução Particular**
- Podemos verificar que $\vec{E}(\vec{r},t)=\vec{E_{0}} \sin(\vec{k}\cdot\vec{r}-\omega t +\varphi_{0})$ é solução desta equação de onda.
- Em que podemos escrever:
$$\begin{align*}
k=\frac{2\pi}{T} \quad \quad &; \quad \quad \omega=\frac{2\pi}{T}\\
\omega=ck \quad \quad &; \quad \quad \lambda=cT
\end{align*}$$
- Uma frente de onda consiste no conjunto de pontos que têm a mesma fase, sendo eles definidos por:
$$\begin{align*}
\vec{k}\cdot\vec{r}-\omega t+\varphi_{0}&= \varphi
\end{align*}$$
- Decompondo $\vec{r}$ em $\vec{r}=\vec{r}_{\perp}+\vec{r}_{\parallel}$ (sendo estas as componentes perpendicular e paralela a $\vec{k}$) ficamos com:
$$k ~r_{\parallel}-\omega t=\varphi-\varphi_{0}~~\to~~ r_{\parallel}=\frac{1}{k}(\omega t+(\varphi-\varphi_{0}))$$
- Ora, podemos escrever a componente paralela na forma $\vec{r}_{\parallel}=r_{\parallel} \frac{\vec{k}}{k}$ e ficamos com:
$$\vec{r}(t)= \vec{r}_{\perp} + \frac{1}{k^{2}}(\omega t+(\varphi-\varphi_{0}))\vec{k}$$
e podemos escrever $\vec{v}=\frac{\omega}{k^{2}}\vec{k}$, obtendo:
$$\vec{r}(t)=\vec{r}_{\perp}+\vec{v}t+\vec{r'}_{\parallel}$$
em que $\vec{r'}_{\parallel}=\frac{\varphi-\varphi_{0}}{k^{2}}\vec{k}$ 

#### Campo Magnético
- A equação de onda que obtivemos acima também se aplica ao campo magnético, tendo-se:
$$\nabla^{2}\vec{E} = \frac{1}{c^{2}} \partial^{2}_{t}\vec{E}$$
em que temos a **solução particular**:
$$\vec{B}(\vec{r},t)=\vec{B_{0}} \sin(\vec{k'}\cdot\vec{r}-\omega't+\varphi_{0}')$$
em que podemos relacionar com a solução do campo elétrico assim:
$$\vec{k}=\vec{k'} \quad;\quad \omega=\omega' \quad;\quad \vec{B_{0}}=\frac{\vec{k}\times \vec{E_{0}}}{\omega}$$
- De notar que o campo magnético é muitas vezes ignorado em Ótica, porque este apenas é significativo para partículas carregadas a mover-se a velocidade perto de $c$.
- Espetro eletromagnético:
![[espetro eletromag.png]]

### 2.1.3 - Princípio da Sobreposição de Ondas Eletromagnéticas
- Consiste no facto que a soma de 2 soluções da equação de onda também é uma solução:
$$\vec{E}(\vec{r},t)=\vec{E_{1}}(\vec{r},t)+\vec{E_{2}(\vec{r},t)}$$
(em que $\vec{E_{1}},\vec{E_{2}}$ são 2 soluções da equação)

#### Interferência entre ondas
- É logo claro que, graças ao princípio da sobreposição, podemos definir uma solução complexa da equação de onda como uma soma de soluções mais simples.
- Assim, a relação de fase é um fator importante a ter em conta ao somar ondas, uma vez que esta decide se ocorrem interferências.
- **Interferências** - fenómemo em que a sobreposição de 2+ ondas resulta numa onda com amplitude maior ou menor.

-  Consideremos 2 ondas planas monocromáticas:
$$\begin{align*}
\vec{E_{1}}(x,t)=\vec{E_{0}}\sin(kx-\omega t +\varphi_{1})\\
\vec{E_{2}}(x,t)=\vec{E_{0}}\sin(kx-\omega t+\varphi_{2})
\end{align*}$$
>- Temos 
>$$\begin{align*}
\sin(a+b)=\sin a\cos b + \cos a\sin b\\
\sin(a-b)=\sin a\cos b - \cos a\sin b\\
\end{align*}$$
>e podemos escrever
>$$\sin(a+b)+\sin(a-b)=2\sin a\cos b$$
>definindo $A=a+b~,~B=a-b$ obtemos $$\sin A+\sin B= 2 \sin \left(\frac{A+B}{2}\right)\cos\left(\frac{A-B}{2}\right)$$

- Usando isto para somar as 2 ondas obtemos:
$$\vec{E}(x,t)=\vec{E_{1}}(x,t)+\vec{E_{2}}(x,t)=2\vec{E_{0}}\cos\left(\frac{\varphi_{1}-\varphi_{2}}{2}\right)\sin\left(kx-\omega t + \frac{\varphi_{1}+\varphi_{2}}{2}\right)$$
- Se $\varphi_{1}-\varphi_{2}=2n\pi~,~n\in\mathbb{N}$ temos que $\vec{E_{1}}(x,t)=\vec{E_{2}}(x,t)$ e temos:
$$\vec{E}(x,t)=2\vec{E_{0}}\sin\left(kx-\omega t+ \frac{\varphi_{1}+\varphi_{2}}{2}\right)$$
AKA interferência construtiva.

- Por outro lado, se $\varphi_{1}-\varphi_{2}=\pm \pi + 2n\pi ~,~ n\in\mathbb{N}$ temos $\vec{E_{1}}(x,t)=- \vec{E_{2}}(x,t)$ e temos:
$$\vec{E}(x,t)=\vec{0}$$
AKA interferência ~~construtiva~~ destrutiva (aiai Ariel) 

- Se por outro lado tivermos $\varphi_{1}-\varphi_{2} \in ~]0,\pi[$ temos uma onda $\vec{E}$ com $$\varphi=\frac{\varphi_{1}-\varphi_{2}}{2} \quad \quad;\quad \quad \vec{E_{0}'}=\vec{E_{0}}\cos\left(\frac{\varphi_{1}-\varphi_{2}}{2}\right)$$

- Vejamos qual será o valor esperado do campo elétrico conforme a fase $\delta\varphi=\varphi_{2}-\varphi_{1}$:
$$\langle \vec{E}(x,t)\rangle = \int_{-\pi}^{+\pi} p(\delta\varphi) 2 \vec{E_{0}}\cos\left(\frac{\delta\varphi}{2}\right)\sin(kx-\omega t+\varphi_{1}+\frac{\delta\varphi}{2})d(\delta \varphi)$$
em que consideraremos uma distribuição de probabilidade uniforme:
$$p(\delta \varphi)= \begin{cases}
\frac{1}{2\Delta\varphi} &; &|\delta\varphi-\delta\varphi_{0}|<\Delta\varphi \\
0 &; &\text{restante}
\end{cases}$$(em que $\delta \varphi_{0}$ é o valor médio dos $\delta \varphi$)
- Assim, se $\Delta \varphi=0$ só podemos ter $\delta \varphi=0$ e temos novamente o caso de interferência construtiva.
- Para $\Delta \varphi>0$, a diferença de fase pode ter vários valores em torno de $\delta \varphi_{0}$ e temos:
$$\langle \vec{E}(x,t)\rangle=\vec{E_{0}}\left[1+\frac{\cos(\delta \varphi_{0})\cos(\Delta \varphi)\sin(\Delta \varphi)}{\Delta \varphi}\right]\sin(kx-\omega t+\varphi_{1})$$
- Vemos que se $\Delta \varphi\to \infty$ ficamos com $\langle \vec{E}(x,t)\rangle=\vec{E_{0}}\sin(kx-\omega t+\varphi_{1})$, ou seja, já não ocorre interferência. Por outras palavras, quando temos muiiiiitos valores possíveis de $\delta \varphi$ 

#### Polarização
- Para uma onda monocromática podemos escrever o campo elétrico a partir das suas componentes dos eixos:
$$\begin{align*}
\vec{E}(x,t)&= E_{x}\hat{x}+ E_{y}\hat{y}+ E_{z}\hat{z}\\
&= \left[\vec{E}(x,t)\cdot\hat{x}\right]\hat{x} + \left[\vec{E}(x,t)\cdot\hat{y}\right]\hat{y} +\left[\vec{E}(x,t)\cdot\hat{z}\right]\hat{z}
\end{align*}$$
- No vazio temos $\nabla \cdot \vec{E}=0$ então temos que o campo magnético no vazio é sempre perpendicular à direção de propagação (um campo a mover-se nos xx oscila nos yy ou nos zz).
- Ou seja, para uma onda eletromagnética no vazio, cada componente descreve um campo qye evolui sem sair de um plano definido pelo versor e que contém a direção de propagação. Cada uma destas ondas é dita de **polarizada linearmente**.
    - Por exemplo o campo $\vec{E_{0}}=(0,E_{0}\cos\theta,E_{0}\sin\theta)$ tem as componentes: $$\begin{align*}
\vec{E_{y}}(x,t)=E_{0}\cos\theta\sin(kx-\omega t+\varphi_{0})\hat{y}\\
\vec{E_{z}}(x,t)=E_{0}\sin\theta\sin(kx-\omega t+\varphi_{0})\hat{z}
\end{align*}$$

![[polarizaçoes de ondas.png]]
- Ora, este tipo de polarização (representado acima) é denominado linear, porque o vetor campo elétrico "desenha" um segmento de reta ao longo da evolução da onda.

- Ou seja, vimos que uma onda pode ser composta por ondas com polarização linear. Se, inversamente, tivermos 2 ondas com polarização linear:
$$\begin{align*}
\vec{E_{y}}(x,t)=\vec{E}_{0y}\cos\theta\sin(kx-\omega t+\varphi_{y})\\
\vec{E_{z}}(x,t)=\vec{E}_{0x}\sin\theta\sin(kx-\omega t+\varphi_{z})
\end{align*}$$
a sua sobreposição *pode não ser* linearmente polarizada. Dependendo da diferença de fase $\delta \varphi=\varphi_{y}-\varphi_{z}$, o vetor campo pode "desenhar" um segmento de reta, círculo ou uma elipse AKA polarização circular e polarização elíptica.

#### Representação Complexa e Decomposição de Fourier
- Usar funções trigonométricas como vimos acima frequentemente gera cálculos bastante complexos. Assim, é frequente usar representações complexas.
- Podemos escrever:
$$\begin{align*}
\sin\alpha=\frac{1}{2i} (e^{i\alpha}-e^{-i\alpha})\\
\cos\alpha=\frac12 (e^{i\alpha}+e^{-i\alpha})
\end{align*}$$
e podemos escrever o campo $\vec{E}(\vec{r},t)=\vec{E_{0}}\sin(\vec{k}\cdot\vec{r}-\omega t + \varphi)$ na forma:
$$\vec{E}(\vec{r},t)=\frac{1}{2} \vec{E_{0}} e^{i(\vec{k}\cdot \vec{r}-\omega t + \theta)} + \frac{1}{2} \vec{E_{0}^{*}} e^{-i(\vec{k}\cdot \vec{r}-\omega t + \theta)}$$
