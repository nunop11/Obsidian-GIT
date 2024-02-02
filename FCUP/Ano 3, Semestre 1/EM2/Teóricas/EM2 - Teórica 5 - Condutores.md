(isto na verdade foi na aula 4, mas fazia mais sentido meter nesta)
# Condutores
- Material em que existem eletrões livres. 
- Por isso, têm as seguintes propriedades:

**i)** $\vec{E}= \vec{0}$ (no interior do contudor, quando ele está em repouso)
**ii)** $\rho=0$ no interior do condutor. Temos $\nabla \cdot \vec{E}=\rho/\varepsilon_{0}$. Ora, se $\vec{E}=0$ também $\rho=0$
**iii)** As cargas distribuem-se apenas na superfície do condutor
**iv)** O condutor encontra-se todo com o mesmo potencial. Isto porque: $\Delta V=\int_{a}^{b} \vec{E}\cdot d \vec{r}=\int \vec{0} \cdot d \vec{r}=0$
**v)** O campo elétrico mesmo a seguir à superfície do condutor (do lado de fora) é perpendicular a esta. Se houvesse componente paralela, a carga na superfície entrava em movimento.

(a partir daqui já é da aula 5)
## Exemplos
![[condutor e carga.png]]
- A carga exterior atrai eletrões do condutor, criando uma zona com carga negativa na superfície do caondutor. 
- Isto gera défice de eletrões do outro lado do condutor, o que gera uma zona com carga positiva.
- As cargas das 2 zonas anulam-se e elas geram campos opostos. Assim, no total do condutor continuamos a ter carga e campo nulos.

![[carga em cavidade de condutor.png]]
- A carga positiva na cavidade atrai eletrões para a superfície da cavidade. Isto causa défice de eletrões na superfície externa.
- Assim, temos uma superfície com carga negativa e outra com carga positiva.
- Ora, pela lei de gauss, dentro de qualquer superfície gaussiana que tenhamos dentro do volume do condutor terá que haver carga total nula (para que $E=0$). Assim, é necessário que a carga induzida na superfície da cavidade seja igual a $-q$ (carga total da superfície).

![[percurso fechado carga em condutor com cavidade.png]]
- Por fim, temos uma cavidade vazia
- Como temos um condutor, é necessário que $\vec{E}=\vec{0}$ no seu interior. Isto leva a $\int \vec{E}\cdot d \vec{r}=0$ para qualquer percurso contido no condutor.
- Além disso, como estamos a considerar eletrostática temos que $\nabla \times \vec{E}=\vec{0}$. Pelo teorema de Stokes, isto implica que $\oint \vec{E}\cdot d \vec{r}=0$
- Juntamente com o que vimos acima, isto implica que $\vec{E}=\vec{0}$ **dentro da cavidade vazia**.

## Pressão Eletroestática
- Consideremos um condutor esférico de raio $R$ com carga $Q$ na superfície.
- Isto implica que a densidade de carga é $\sigma=\frac{Q}{4\pi R^{2}}$

- Sabemos que os campos no interior e exterior do condutor são dados por:
$$\vec{E}_{-}= \vec{0} \quad \quad;\quad \quad \vec{E}_{+} = \frac{Q}{4\pi\varepsilon_{0}R^{2}}\hat{r}=\frac{\sigma}{\varepsilon_{0}}\hat{r}$$
(em que $+$ significa "fora do condutor" e $-$ "dentro do condutor")

- Consideremos agora uma componente infinitesimal de área da superfície do condutor:
![[campo de unidade sup carga.png]]
sendo que esta acaba por ser equivalente a um plano com densidade de carga $\sigma$. Sendo assim, temos o campo acima e abaixo deste:
$$\vec{E}_{1-}= -\frac{\sigma}{2\varepsilon_{0}}\hat{r} \quad \quad;\quad \quad \vec{E}_{1+}= \frac{\sigma}{2\varepsilon_{0}}\hat{r}$$

Ora, o campo total que está aplicado nesta área infinitesimal será:
$$\vec{E}= \begin{cases}
\vec{E}_{-}- \vec{E}_{1-}=\frac{\sigma}{2\varepsilon_{0}}\hat{r} \\
\vec{E}_{+}- \vec{E}_{1+}= \frac{\sigma}{2\varepsilon_{0}}\hat{r}
\end{cases}$$
Pelo que o campo total da superfície do condutor atua nesta área quase como que um campo externo. Temos então que a direção de onde o campo vem não importa, ele terá este valor.

- Temos então que a força gerada pelo campo elétrico nesta área infinitesimal será:
$$d \vec{F}=dq \vec{E}=\sigma ds \frac{\sigma}{2\varepsilon_{0}}\hat{r}= \frac{\sigma^{2}}{2\varepsilon_{0}}ds \hat{r}$$
- Ora, dividindo uma força pela área de aplicação obtemos a pressão que ela gera. Assim, a **pressão eletroestática** é dada por:
$$\frac{dF}{ds}= \frac{\sigma^{2}}{2\varepsilon_{0}}=\frac{\varepsilon_{0}}{2} |\vec{E}_{+}|^{2}$$

## Capacidade
![[capacidade.png]]
- Temos 2 condutores. Um com carga $+Q$ e potencial $V_{+}$; outro com carga $-Q$ e potencial $V_{-}$. Temos então a diferença de potencial $V=V_{+}-V_{-}$
- Sendo $\vec{r}_{\pm}$ um ponto arbitrário dentro do condutor $+Q$ ou $-Q$, temos que o seu potencial será:
$$V(\vec{r}_{\pm})=\frac{1}{4\pi\varepsilon_{0}} \int \frac{dq(\vec{r}')}{|\vec{r}_\pm-\vec{r}'|}=\frac{1}{4\pi\varepsilon_{0}} \int \frac{\rho(\vec{r}')}{|\vec{r}_\pm-\vec{r}'|}dV$$
- Ora, nós sabemos que $V\propto Q$. 
- Mas será que se mudarmos ambos os condutores para o dobro da carga a diferença de potencial duplica? Ora, a forma como o potencial evolui com a carga é descrita através da **capacidade**:
$$Q=CV$$

- Imaginemos agora que queremos mover um destes condutores. Vimos atrás que o trabalho necessário para mover uma carga pontual é $W=qV$. Assim, para um condutor temos:
$$\begin{align*}
dW=Vdq~~~~\to~~~~ W=\int_{0}^{Q} Vdq=\int_{0}^{Q} \frac{q}{C} dq&= \frac{Q^{2}}{2C} = \frac{1}{2}CV^{2} 
\end{align*}$$

# Equação de Laplace / Poisson
- Quando queremos determinar o potencial num sistema com uma distribuição de carga em repouso, podemos usar:
$$V(\vec{r}_{\pm})=\frac{1}{4\pi\varepsilon_{0}} \int \frac{\rho(\vec{r}')}{|\vec{r}-\vec{r}'|} d^{3}r'$$
mas este integral rapidamente se torna em algo muito complicado e demoroso de resolver.

- Assim, muitas vezes é útil usar a *equação de Poisson*:
$$\nabla^{2}V=- \frac{\rho}{\varepsilon_{0}}$$
- Ou, quando queremos determinar o potencial em regiões em que não há cargas, a *equação de Laplace*: $$\nabla^{2}V=0$$

## Equação de Laplace
**1 Dimensão**
- Temos $V=V(x)$. Assim: $$\nabla^{2}V=\frac{d^{2}V}{dx^{2}}=0\to V(x)=\frac{1}{2}[V(x+a)+V(x-a)]$$
- Ou seja, o potencial é uma reta a subir ou descer. Assim, não há máximos nem mínimos na região com $\rho=0$. Os extremos encontram-se apenas nas fronteiras.

**N Dimensões**
- A ideia de 1-D pode ser expandida. Basicamente, se o potencial numa certa região satisfaz a equação de Laplace, então ele **não tem máximos nem mínimos locais nessa região**. 