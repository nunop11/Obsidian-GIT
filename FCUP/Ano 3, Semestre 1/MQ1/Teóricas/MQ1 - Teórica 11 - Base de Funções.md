# 3 - Formulação Axiomática de Mecânica Quântica
## 3.1 - Espaço de Funções de Onda de Uma Partícula
- O conjunto $L^{2}$ de funções (funções de quadrado somável) é definido por:
$$L^{p}: \left(\int|f(x)|^{p}~dx\right)^{\frac{1}{p}}<\infty ~~\longrightarrow~~ L^{2}: \left(\int|f(x)|^{2}~dx\right)^{\frac{1}{2}}<\infty$$
- Ou seja, consideremos o conjunto de funções $L^{2}$:
$$\int d^{3}r~|\psi(\vec{r},t)|^{2}=\int d^{3}r~ \psi^{*}(\vec{r},t)\psi(\vec{r},t)<\infty$$
em que exigimos continuidade da função e das suas derivadas. Chamaremos $\mathcal{F}$ a este conjunto $L^{2}$.

- Facilmente concluímos que $\mathcal{F}$ é um espaço vetorial. Tendo $\psi_{1},\psi_{2}\in\mathcal{F}$ podemos escrever:
$$\psi=\lambda_{1}\psi_{1}+\lambda_{2}\psi_{2}\in \mathcal{F}~~~~(\lambda_{1},\lambda_{2}\in\mathbb{C})$$

- Ora, determinemos então $|\psi|^{2}$:
$$\begin{align*}
|\psi|^{2}&= (\lambda_{1}^{*}\psi_{1}^{*}+\lambda_{2}^{*}\psi_{2}^{*})(\lambda_{1}\psi_{1}+\lambda_{2}\psi_{2})\\
&= \underbrace{|\lambda_{1}|^{2}|\psi_{1}|^{2}}_{\int ~finito} + \underbrace{|\lambda_{2}|^{2}|\psi_{2}|^{2}}_{\int~finito} + \underbrace{\lambda_{1}^{*}\lambda_{2}\psi_{1}^{*}\psi_{2}+\lambda_{1}\lambda_{2}^{*}\psi_{1}\psi_{2}^{*}}_{\int~pode~não~ser~finito} \\
\end{align*}$$
(em que $\int$ significa "o integral desta parcela")

- Sabemos que o quadrado de qualquer coisa não pode ser negativo:
$$\begin{align*}
(|\psi_{1}|+|\psi_{2}|)^{2} &\ge 0\\
|\psi_{1}|^{2}+ |\psi_{2}|^{2} - 2|\psi_{1}||\psi_{2}|&\ge 0\\
|\lambda_{1}||\lambda_{2}|(2|\psi_{1}||\psi_{2}|)&\le |\lambda_{1}||\lambda_{2}|(|\psi_{1}|^{2}+|\psi_{2}|^{2})
\end{align*}$$
de onde vem:
$$\int d^{3}r |\psi|^{2}\le \int d^{3}r~\left[ |\lambda_{1}|^{2}|\psi_{1}|^{2} + |\lambda_{2}|^{2}|\psi_{2}|^{2} + |\lambda_{1}||\lambda_{2}|(|\psi_{1}|^{2}+|\psi_{2}|^{2}) \right]<\infty$$
(Muito sinceramente não percebi nada do que se passa na parte acima :D)

## Produto Escalar
- Temos $\psi(\vec{r}),\varphi(\vec{r})\in\mathcal{F}$. Podemos escrever o *produto escalar entre as funções*:
$$(\varphi,\psi)=\int d^{3}r~\varphi^{*}(\vec{r})\psi(\vec{r})$$
### Propriedades
**1 - Conjugado**
$$(\varphi,\psi)=(\varphi,\psi)^{*}$$

**2 - Linear no 1º argumento**
$$(\varphi, \lambda_{1}\psi_{1}+\lambda_{2}\psi_{2})=\lambda_{1}(\varphi,\psi_{1})+\lambda_{2}(\varphi,\psi_{2})$$

**3 - Anti-linear no 2º argumento**
$$(\lambda_{1}\varphi_{1}+\lambda_{2}\varphi_{2},\psi)=\lambda_{1}^{*}(\varphi_{1},\psi)+\lambda_{2}^{*}(\varphi_{2},\psi)$$

#### Ortogonalidade
- 2 funções $\varphi,\psi$ são ortogonais se $(\varphi,\psi)=0$ (tal como com vetores)

#### Norma
- A norma de uma função pode ser obtida com a raiz do produto escalar dela consigo mesma:
$$|\psi|=\sqrt{(\psi,\psi)}=\int d^{3}r~ |\psi(\vec{r})|^{2}$$
- Ora, vemos logo que: $|\psi|=0\to \psi=0$

#### Desigualdade de Schwarz
(AKA desigualdade de Cauchy-Schwarz)
$$|(\varphi,\psi)|\le \sqrt{(\varphi,\varphi)}\sqrt{(\psi,\psi)}=|\varphi||\psi|<\infty$$

## Bases discretas em $\mathcal{F}$
- Como as funções de $\mathcal{F}$ são elementos de um espaço vetorial, deverá ser possível formar uma base de funções tal que qualquer elemento de $\mathcal{F}$ possa ser escrito como um **combinação linear** das funções base.
- Essa base será discreta se os elementos forem contáveis, ou seja:
$$\{u_{n}(\vec{r})\}~~~~,~~~~n\in\mathbb{N}$$

> EXEMPLO : Poço Infinito
> - Tínhamos que a função de onda solução da ESIT é descrita por $$\Psi(x)=\sum\limits_{n=1}^{\infty} C_{n}\psi_{n}(x)$$
> em que as funções base são $\{\psi_{n}(x)\}$ sendo que:
> $$\psi_{n}(x)= \sqrt{\frac{2}{a}} \sin \left( \frac{n\pi}{a}x \right)$$

- Ora, queremos então definir $\mathcal{F}$ como uma base **ortonormada** de funções. Ou seja queremos que:
$$(u_{i},u_{j})=\int d^{3}r ~u_{i}^{*}(\vec{r})u_{j}(\vec{r})=\delta_{i,j}$$
ou seja, o produto escalar de quaisquer funções base $u_{i},u_{j}$ é nulo se $i\neq j$ pelo que a base é ortogonal. Caso contrário, temos que o produto escalar é $1=|u_{i}|=|u_{j}|$, pelo que a base está normalizada. Portanto a base é Ortonormada!

#### Funções VS Vetores
**Definir função a partir de combinação linear das funções base**
- Temos ainda que, em cada instante, podemos expandir a função $\psi\in\mathcal{F}$ na base $\{ u_{n}(\vec{r})\}$ :
$$\psi(\vec{r},t)=\sum\limits_{n=1}^{\infty} C_{n}(t) u_{n}(\vec{r})$$
ou seja, $C_{n}(t)$ será o componente de $\psi$ na "direção" $u_{n}$, no instante $t$. 
    - Isto é equivalente a, com vetores, escrever: $\vec{v}=\sum\limits_{n=1}^{3} v_{i}\hat{x_{i}}$ 

**Obter componente com produto escalar**
- Podemos ainda escrever:
$$\begin{align*}
(u_{j},\psi)&= \int d^{3}r~ \sum\limits_{n=1}^{\infty} C_{n}(t)u_{j}^{*}(\vec{r})u_{n}(\vec{r})\\
&= \sum\limits_{n=1}C_{n}(t) \delta_{n,m}\\
&= C_{j}(t)
\end{align*}$$
    - Com vetores isto equivale a fazer: $\hat{e_{x}}\cdot \vec{v}=v_{x}$

- Tendo uma função $\varphi,\psi\in\mathcal{F}$, vamos escrever o seu produto escalar a partir das suas componentes:
$$\begin{align*}
(\varphi,\psi)&= \left(\sum\limits_{n=1}^{\infty}b_{n}u_{n}, \sum\limits_{m=1}^{\infty} c_{m}u_{m}\right)\\
&= \sum\limits_{n,m} b_{n}^{*}c_{m}(u_{n},u_{m})\\
&= \sum\limits_{n,m} b_{n}^{*}c_{m} \underbrace{\delta_{n,m}}_{\textsf{base ortonormada}}\\
&= \sum\limits_{n=1}^{\infty} b_{n}^{*}c_{m}\\
\end{align*}$$
- Ora, se $\varphi=\psi$ temos:
$$(\psi,\psi)=\sum\limits_{n=1}^{\infty} |c_{n}|^{2}=|\psi|^{2}$$

### Base completa
- Para a função $\psi\in\mathcal{F}$, expressa na base *ortonormada* $\{u_{n}(\vec{r}\}$ podemos escrever
$$\begin{align*}
\psi(\vec{r}) &= \sum\limits_{i} C_{i}u_{i}(\vec{r})\\
&= \sum\limits_{i} (u_{i},\psi)u_{i}(\vec{r})\\
&= \sum\limits_{i} \left( \int d^{3}r'~ u^{*}_{i}(\vec{r'})\psi(\vec{r'}) \right)u_{i}(\vec{r})\\
&= \int d^{3}r'~ \psi(\vec{r'}) \sum\limits_{i}u_{i}^{*}(\vec{r'})u_{i}(\vec{r'})
\end{align*}$$
ora, para a base se **completa** é preciso que a igualdade acima se verifique para TODAS as funções $\psi$. Assim, é necessário que:
$$\int d^{3}r'~ \psi(\vec{r'}) \sum\limits_{i}u_{i}^{*}(\vec{r'})u_{i}(\vec{r'})=\int d^{3}r'~ \psi(\vec{r'}) \delta(\vec{r}-\vec{r'})$$
de onde temos a **_Relação de Fecho_**:
$$\sum\limits_{i} u_{i}^{*}(\vec{r'})u_{i}(\vec{r'})=\delta(\vec{r}-\vec{r'})$$
- Pegando a igualdade acima, podemos voltar 1 passo atrás e desenvolver de forma diferente:
$$\begin{align*}
\psi(\vec{r})&= \int d^{3}r'~ \psi(\vec{r'})\delta(\vec{r}-\vec{r'})\\
&= \int d^{3}r'~\psi(\vec{r'})\sum\limits_{i} u_{i}^{*}(\vec{r'})u_{i}(\vec{r'})\\
&= \sum\limits_{i} C_{i} u_{i}(\vec{r})
\end{align*}$$
sendo que recuperamos a forma que vimos acima de definir a função como uma combinação linear das funções base.

## Bases Contínuas em $\mathcal{F}$
- Podemos definir um conjunto de funções $\{ u_{\alpha}(\vec{r})\}$ (em que $\alpha$ é um parâmetro contínuo) que *não* pertencem a $\mathcal{F}$, mas que nos permitem formar uma base de funções que pertencem a $\mathcal{F}$.
- Assim, podemos verificar todas as propriedades que vimos para bases contínuas

**Base ortonormada**
$$(u_{\alpha},u_{\alpha'})=\int d^{3}r~u_{\alpha}^{*}(\vec{r})u_{\alpha'}(\vec{r})=\delta(\alpha-\alpha')$$

**Expansão de $\psi(\vec{r},t)$ num instante**
$$\psi(\vec{r},t)=\int d \alpha ~c(\alpha,t) u_{\alpha}(t)$$
(isto é equivalente a $\sum_{n} c_{n}(t)u_{n}(\vec{r})$)

**Projeção da função na base**
$$\begin{align*}
(u_{\alpha},\psi)&= \int d^{3}r~ u_{\alpha}^{*}(\vec{r})\psi(\vec{r})= \int d^{3}r ~u_{\alpha}^{*} \left(\int d\alpha~ c(\alpha')u_{\alpha'}(\vec{r}) \right)\\
&= \int d\alpha' c(\alpha') \int d^{3}r u_{\alpha'}^{*}(\vec{r})a_{\alpha'}(\vec{r})=c(\alpha)
\end{align*}$$

**Produto escalar em termos das componentes**
$$\begin{align*}
(\phi,\psi)&= \int d^{3}r \left(\int d\alpha~b^{*}(\alpha)u_{\alpha}^{*}(\vec{r})\right) \left(\int d\alpha'~c(\alpha')u_{\alpha'}(\vec{r})\right)\\
&= \int d\alpha d\alpha' ~b^{*}(\alpha)c(\alpha)\int d^{3}r~u_{\alpha}^{*}(\vec{r}) u_{\alpha'}(\vec{r})=\int d\alpha~b^{*}(\alpha)c(\alpha)
\end{align*}$$
(que é equivalente a $\sum_{n} b_{n}^{*}c_{n}$)

**Relação de Fecho**
$$\begin{align*}
\psi(\vec{r})&= \int d \alpha~ c(\alpha) u_{\alpha}(\vec{r})=\int d\alpha \left(\int d^{3}r'~ u_{\alpha}^{*}(\vec{r'})\psi(\vec{r'})\right) u_{\alpha}(\vec{r})\\
&= \int d^{3}r' ~ \psi(\vec{r'}) \int d\alpha~u_{\alpha}^{*}(\vec{r})u_{\alpha}(\vec{r})
\end{align*}$$

> EXEMPLO : **ONDAS PLANAS**
> Podemos defini-las com $$u_{\vec{k}}(\vec{r})= \frac{1}{(2\pi)^{\frac{3}{2}}} e^{i\vec{k}\cdot\vec{r}}$$
> (em que $\alpha=\vec{k}$)
> Conseguimos verificar tudo o que tem acima:
> ![[exemplo base.png]]