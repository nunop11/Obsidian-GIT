# 2 - Instrumentos Matemáticos da Mecânica Quântica
# 2.1 - Espaço de Funções de Onda de Uma Partícula 
- Como sabemos, $|\psi(\vec{r},t)|d^{2}r$ representa a probabilidade de encontrar uma partícula no volume $d^{3}r$ centrado na posição $\vec{r}$, no instante $t$. É portanto natural que $$\int_\textsf{todo o espaço} d^{3}r|\psi(\vec{r},t)|^{2}=1$$ porque temos que encontrar uma partícula *algures* em todo o espaço.
- Assim, as funções $\psi(\vec{r},t)$ terão de ser aquelas para as quais o integral acima converge. Ou seja, são funções de quadrado somável ($L^{2}$).
- Mas o grupo $L^{2}$ só por si é demasiado vasto para uma função com o significado físico de $|\psi|^{2}$. As funções $\psi$ que fazem sentido fisicamente são aquelas que são: contínuas, definidas e deriváveis infinitamente; em todos os pontos do espaço. Dependendo do caso, podemos até restringir este grupo às funções limitadas a um intervalo finito.
- Desta forma, de modo a ser mais geral, definimos o **espaço de funções de onda de 1 partícula**: $\mathscr{F}$ ($\mathscr{F}\subset L^{2}$)

## 2.1.1 - Estrutura de $\mathscr{F}$
### $\mathscr{F}$ é um espaço vetorial
- Se $\psi_{1}(\vec{r}),\psi_{2}(\vec{r})\in \mathscr{F}$ então: $$\psi(\vec{r})=\lambda_{1}\psi(\vec{r})+\lambda_{2}\psi_{2}(\vec{r})\in \mathscr{F} ~~~~~~(\lambda_{1},\lambda_{2}\in\mathbb{C})$$
Podemos ainda fazer o quadrado e verificar se $\psi$ é de quadrado somável:
$$|\psi(\vec{r})|^{2}=|\lambda_{1}|^{2}|\psi_{1}(\vec{r})|^{2}+|\lambda_{2}|^{2}|\psi_{2}(\vec{r})|^{2} + \lambda_{1}^{*}\lambda_{2}\psi_{1}^{*}(\vec{r})\psi_{2}(\vec{r})+\lambda_{1}\lambda_{2}^{*}\psi_{1}(\vec{r})\psi_{2}^{*}(\vec{r})$$
    - os primeiros 2 termos são de quadrado somável porque $\psi_{1},\psi_{2}\in\mathscr{F}\in L^{2}$
    - os últimos 2 termos não são tão diretos. No entanto temos a relação: $$2|\lambda_{1}||\lambda_{2}||\psi_{1}(\vec{r})||\psi_{2}(\vec{r})|\le |\lambda_{1}||\lambda_{2}|[|\psi_{1}(\vec{r})|^{2}+|\psi_{2}(\vec{r})|^{2}]$$logo se os integrais de $|\psi_{1}|^{2},|\psi_{2}|^{2}$ convergem, também $|\psi(\vec{r})|^{2}$ e temos que $\psi\in L^{2}$

### Produto Escalar
**Definição**
- Tendo-se 2 elementos de $\mathscr{F}$: $\varphi(\vec{r}),\psi(\vec{r})$, podemos definir o seu produto escalar:
$$(\varphi,\psi)=\int d^{3}r~\varphi^{*}(\vec{r})\psi(\vec{r}) ~~~~(\in\mathbb{C})$$
(se $\varphi,\psi\in\mathscr{F}$, o integral converge)

**Propriedades**
- Temos:
$$\begin{align*}
(\varphi,\psi)&= (\psi,\varphi)^{*}\\
(\varphi,\lambda_{1}\psi_{1}+\lambda_{2}\psi_{2})&= \lambda_{1}(\varphi,\psi_{1})+\lambda_{2}(\varphi,\psi_{2})\\
(\lambda_{1}\varphi_{1}+\lambda_{2}\varphi_{2},\psi)&= \lambda_{1}^{*}(\varphi_{1},\psi)+\lambda_{2}^{*}(\varphi_{2},\psi)
\end{align*}$$
ou seja, é *linear* com o 2º termo e *antilinear* com o primeiro.
- Se $(\varphi,\psi)=0$ então essas funções são **ortogonais**.
- Podemos escrever: $$(\psi,\psi)=\int d^{3}r~|\psi(\vec{r})|^{2}~~\ge0 \quad \quad (\in \mathbb{R})$$
- A *norma* de uma função consiste em $|\psi|=\sqrt{(\psi,\psi)}$
- Temos a **desigualdede de Schwarz**:
$$|(\varphi,\psi)|\le \sqrt{(\varphi,\varphi)}\sqrt{(\psi,\psi)}$$

### Operadores Lineares
**Definição**
- Por definição, um operador $A$ associa a uma função $\psi(\vec{r})\in\mathscr{F}$ uma função $\psi'(\vec{r})$ na forma:
$$\begin{align*}
A\psi(\vec{r})&= \psi'(\vec{r})\\\\
A[\lambda_{1}\psi_{1}(\vec{r})+\lambda_{2}\psi_{2}(\vec{r})]&= \lambda_{1}A\psi_{1}(\vec{r})+\lambda_{2}A\psi_{2}(\vec{r})
\end{align*}$$

- Exemplos de Operadores:
    - Operador *Paridade*: $\Pi \psi(x,y,z)=\psi(-x,-y,-z)$
    - Operador que multiplica por $x$: $X\psi(x,y,z)=x\psi(x,y,z)$
    - Operador *derivada* em $x$: $D_{x}\psi(x,y,z)=\frac{\partial}{\partial x}\psi(x,y,z)$
(O resultado de $X,D_{x}$ a atuar em $\psi\in\mathscr{F}$ pode já não ser de quadrado somável)

**Produto de Operadores**
- Sendo $A,B$ operadores lineares: $$(AB)\psi(\vec{r})=A[B\psi(\vec{r})]$$
- Em geral $AB\neq BA$, pelo que definimos o comutador entre os operadores:
$$[A,B]=AB-BA$$
por exemplo, $[X,D_{x}]=-1$

## 2.1.2 - Bases Discretas em $\mathscr{F}$
### Definição
- Consideremos um conjunto de funções de $\mathscr{F}$ identificadas por índices $i=1,2,\dots n\dots$
- O conjunto $\{u_{i}(\vec{r})\}$ é **ortonomal** se:
$$\boxed{(u_{i},u_{j})=\int d^{3}r~ u_{i}^{*}(\vec{r}) u_{j}(\vec{r})=\delta_{ij}}$$
($\delta_{ij}$ é o delta de Kronecker) (Esta fórmula é usada em basicamente todas as deduções neste capítulo)
> Isto é o mesmo que ter $\hat{x}\cdot\hat{y}=0~,~\hat{x}\cdot\hat{x}=1$ na base cartesiana

- Esse conjunto de funções forma uma base discreta completa de $\mathscr{F}$ se:
$$\psi(\vec{r})=\sum\limits_{i}c_{i}u_{i}(\vec{r}) \quad \quad (c_{i}\in\mathbb{C})$$
ou seja, é base completa se qualquer função $\psi\in\mathscr{F}$ pode ser escrita em função dos termos $u_{i}$, de uma só forma.
> Podemos, na base cartesiana, comparar isto a $\vec{r}=r_{x}\hat{x}+r_{y}\hat{y}+r_{z}\hat{z}$

### Componentes de $\psi$ na base $\{u_{i}(\vec{r})\}$
- Temos:
$$\psi(\vec{r})=\sum\limits_{i}c_{i}u_{i}(\vec{r})$$
es multiplicarmos os 2 lados por $u_{j}^{*}(\vec{r})$:
$$(u_{j},\psi)=\left(u_{j},\sum\limits_{i}c_{i}u_{i}\right)=\sum\limits_{i}c_{i}(u_{j},u_{i})=\sum\limits_{i}c_{i}\delta_{ij}=c_{j}$$
e podemos portanto escrever a componente de $\psi$ na função de índice $i$:
$$c_{i}=(u_{i},\psi)=\int d^{3}r~u_{i}^{*}(\vec{r})\psi(\vec{r})$$

> Na base cartesiana isto equivale a: $\hat{x}\cdot \vec{r}=r_{x}$

### Produto Escalar em função das componentes
- Consideremos 2 funções  $\varphi, \psi$ na base $\{u_{i}(\vec{r})\}$:
$$\varphi(\vec{r})=\sum\limits_{i} b_{i}u_{i}(\vec{r}) \quad\quad;\quad\quad \psi(\vec{r})=\sum\limits_{j}c_{j}u_{j}(\vec{r})$$
e podemos escrever:
$$(\varphi,\psi)=\left(\sum\limits_{i} b_{i}u_{i}, \sum\limits_{j}c_{j}u_{j} \right)=\sum\limits_{i,j}b_{i}^{*}c_{j}(u_{i},u_{j})=\sum\limits_{i,j}b_{i}^{*}c_{j}\delta_{ij}=\sum\limits_{i}b_{i}^{*}c_{i}$$
ou seja, temos 2 fórmulas úteis:
$$(\varphi,\psi)=\sum_{i}b_{i}^{*}c_{i} \quad \quad;\quad \quad (\psi,\psi)=\sum\limits_{i}|c_{i}|^{2}$$
> Na base cartesiana isto é iguala a ter $\vec{r}\cdot\vec{u}=r_{x}u_{x}+r_{y}u_{y}+r_{z}u_{z}$

### Relação de Fecho
- A relação de ortonormalização $(u_{i},u_{j})=\delta_{ij}$ descreve a relação necessária para que o conjunto $\{u_{i}(\vec{r})\}$ seja ortonormado.
- A relação de fecho que veremos a seguir descreve a relação necessária para que o conjunto seja uma base completa de $\mathscr{F}$.

- Se $\{u_{i}(\vec{r})\}$ for uma base de $\mathscr{F}$, tal como dito atrás, temos que conseguir definir todas as funções $\psi\in\mathscr{F}$ como combinações lineares da base $\{u_{i}\}$. Assim:
$$\psi(\vec{r})=\sum\limits_{i}c_{i}u_{i}(\vec{r})$$
que podemos escrever na forma:
$$\begin{align*}
\psi(\vec{r})&= \sum\limits_{i}(u_{i},\psi)u_{i}(\vec{r})\\
&= \sum\limits_{i} \left(\int d^{3}r'~u_{i}^{*}(\vec{r'})\psi(\vec{r'}) \right)u_{i}(\vec{r})\\
&= \int d^{3}r'~\psi(\vec{r'})\left[\sum\limits_{i}u_{i}(\vec{r})u_{i}^{*}(\vec{r'}) \right]= \int d^{3}r' \psi(\vec{r'})F(\vec{r}, \vec{r'})
\end{align*}$$
ora, a única forma de termos uma igualdade $\psi=\psi$ é se a função $F$ for um delta de dirac, ou seja:
$$\boxed{\sum\limits_{i}u_{i}(\vec{r})u_{i}^{*}(\vec{r'})=\delta(\vec{r}-\vec{r'})}$$
sendo esta a **Relação de Fecho**. 
- Ou seja, partindo de $\{u_{i}(\vec{r})\}$ que assumimos ser base de $\mathscr{F}$ obtivemos a relação de fecho. Inversamente, se um conjunto obedece à relação de fecho então é base.
- Podemos interpretar a relação de fecho na forma: As funções $u_{i}(\vec{r}),u_{i}(\vec{r'})$ podem ser vistas como 2 funções da base $\{u_{i}\}$ que "apontam na mesma direção"

## 2.1.3 - Bases que NÃO pertencem a $\mathscr{F}$
- Acima apenas consideramos bases $\{u_{i}(\vec{r})\}$ em que os termos pertencem a $\mathscr{F}$, o que faz sentido porque estamos a usá-las para definir funções de onda. 
- Mas muitas funções de onda podem ser definidas em bases que não são de quadrado somável.

### 2.1.3.1 - Ondas Planas
**Definição**
- Este é um exemplo que já kinda aprendemos em Física Moderna.
- Consideremos apenas o caso 1D.
- Temos a função $v_{p}(x)$ que descreve uma onda plana:
$$v_{p}(x)=\frac{1}{\sqrt{2\pi\hbar}}e^{i px/\hbar}$$
- Rapidamente verificamos que o integral de $|v_{p}(x)|^{2}$ em $x$ não converge, ou seja, $v_{p}\notin\mathscr{F}$. Vamos então definir $\{v_{p}(x)\}$ o conjunto de funções que descrevem ondas planas com parâmetro $p$, em que este é um parâmetro contínuo que varia de $-\infty$ a $+\infty$ (aka um *índice contínuo*).

- A transformada de Fourier e transformada inversa de Fourier de uma função $\psi(x)$ podem ser escritas como:
$$\begin{align*}
\psi(x)&= \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{+\infty}dp~\tilde\psi(p)e^{ipx/\hbar}\\
\tilde\psi(p)&= \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^{+\infty} dx~\psi(x)e^{-ipx/\hbar}
\end{align*}$$
em que podemos substituir $v_{p}(x)$:
$$\begin{align*}
\psi(x)&= \int_{-\infty}^{+\infty}dp~\tilde\psi(p)v_{p}(x)\\
\tilde\psi(p)&= \int_{-\infty}^{+\infty}dx~v_{p}^{*}(x)\psi(x)=(v_{p},\psi)
\end{align*}$$
estas 2 equações são equivalente a $\psi(\vec{r})=\sum\limits_{i}c_{i}u_{i}(\vec{r})$ e $c_{i}=(u_{i},\psi)$
- Ou seja, usando as ondas planas como uma base contínua, qualquer função de onda pode ser escrita como como uma combinação linear de funções de onda plana em que os coeficientes $c_{i}$ são os elementos da transformada de Fourier. Isto é uma interpretação direta da transformada de Fourier: qualquer função pode ser definida como uma soma infinita de senos e cossenos.
- Por outras palavras, a mesma função $\psi$ é representada na base $\{u_{i}\}$ pelos elementos $c_{i}$ e na base $\{v_{p}\}$ pelos elementos $\tilde\psi(p)$.

**Produto Escalar**
- De acordo com o teorema de Parseval: $\int_{-\infty}^{+\infty}|f(t)|^{2}dt=\frac{1}{2\pi} \int_{-\infty}^{+\infty}|\tilde f(\omega)|^{2}d\omega$. Isto significa que:
$$(\psi,\psi)=\int_{-\infty}^{+\infty}dp~|\tilde\psi(p)|^{2}$$
pelo que temos a equação equivalente: $(\psi,\psi)=\sum\limits_{i}|c_{i}|^{2}$.

**Relação de Fecho**
- Usando a transformada de Fourier do delta de Dirac ($\delta(u)=\frac{1}{2\pi}\int_{-\infty}^{+\infty}dl~e^{iku}$) conseguimos escrever:
$$\int_{-\infty}^{+\infty}dp~v_{p}(x)v_{p}^{*}(x')=\frac{1}{2\pi}\int_{-\infty}^{+\infty}\frac{dp}{\hbar}~e^{i \frac{p}{\hbar}(x-x')}=\delta(x-x')$$
tendo-se então a *relação de fecho* para a base das ondas planas.

**Ortonormalidade**
- Similarmente, podemos determinar o produto escalar entre 2 funções da base:
$$(v_{p},v_{p'})=\int_{-\infty}^{+\infty}dx~v_{p}^{*}(x)v_{p'}(x)=\frac{1}{2\pi}\int_{-\infty}^{+\infty}dx~e^{i \frac{x}{\hbar}(p'-p)}=\delta(p-p')$$
e temos uma *relação de ortonormalização* desta base. De notar que esta relação não é exatamente de ortonormalização, porque se $p=p'$ ficamos com $(v_{p},v_{p'})\to\infty$.

**Em 3D**
- Para generalizar esta base a 3D basta ter:
$$v_{\vec{p}}(\vec{r})=\left(\frac{1}{2\pi\hbar}\right)^{\frac{3}{2}}e^{i\vec{p}\cdot\vec{r}/\hbar}$$
pelo que em todas as relações establecidas acima basta subtituir $x\to\vec{r}~,~p\to\vec{p}$.

**Discreto VS Ondas Planas**
- A base das ondas planas é contínua, ou seja, o parâmetro que diferencia 2 funções ,$p$, é contínuo. As bases $\{u_{i}\}$ que vimos atrás tinham $i$ discreto, tendo-se bases discretas.
- Assim, podemos relacionar estes tipos de bases:
$$\boxed{\begin{align*}
Discreto &&\Longleftrightarrow&&& Ondas~Planas\\
i &&\Longleftrightarrow&&& \vec{p}\\
\sum\limits_{i} &&\Longleftrightarrow&&& \int d^{3}p\\
\delta_{ij} &&\Longleftrightarrow&&& \delta(\vec{p}-\vec{p'}) 
\end{align*}}$$

### 2.1.3.2 - Funções Delta
- Temos agora o conjunto de funções $\{\xi_{\vec{r_{0}}}(\vec{r})\}$, que tem o índice contínuo $\vec{r_{0}}$, e definimos como:
$$\xi_{\vec{r_{0}}}(\vec{r})=\delta(\vec{r}-\vec{r_{0}})$$
(é óbvio que estas funções não são de quadrado somável)

- Naturalmente, podemos escrever:
$$\begin{align*}
\psi(\vec{r})&= \int d^{3}r_{0}~\psi(\vec{r_{0}})\xi_{\vec{r_{0}}}(\vec{r})\\
\psi(\vec{r_{0}})&= (\xi_{\vec{r_{0}}},\psi)= \int d^{3}r~ \xi_{\vec{r_{0}}}^{*}(\vec{r})\psi(\vec{r})
\end{align*}$$
 novamente, isto é equivalente ao caso de uma base discreta em que $c_{i}\leftrightarrow \psi(\vec{r_{0}})$.

- Mais uma vez, a mesma função de onda $\psi$ é descrita pelos termos $c_{i}$ na base $\{u_{i}\}$ e pelos termos $\psi(\vec{r_{0}})$ na base $\{\xi_{\vec{r_{0}}}\}$

**Produto Escalar**
- Consideremos as funções $\varphi,\psi$ definidas na base $\{\xi_{\vec{r_{0}}}\}$:
$$\varphi(\vec{r})=\int d^{3}r_{0} ~\varphi(\vec{r_{0}})\xi_{\vec{r_{0}}}(\vec{r}) \quad \quad;\quad \quad \psi(\vec{r})=\int d^{3}r_{0}~\psi(\vec{r_{0}})\xi_{\vec{r_{0}}}(\vec{r})$$
e podemos fazer o produto escalar:
$$\begin{align*}
(\varphi, \psi)&= \int d^{3}r_{0}~ \varphi^{*}(\vec{r_{0}})\xi_{\vec{r_{0}}}^{*}(\vec{r}) \cdot \psi(\vec{r_{0}})\xi_{\vec{r_{0}}}(\vec{r})= \int d^{3}r_{0}~\varphi^{*}(\vec{r_{0}})\psi(\vec{r_{0}})
\end{align*}$$
sendo isto equivalente a $(\varphi,\psi)=\sum_{i} b_{i}^{*}c_{i}$ na base $\{u_{i}(\vec{r})\}$.

**Relação de Fecho**
- Seguindo o que fizemos para as ondas planas:
$$\int d^{3}r_{0}~\xi_{\vec{r_{0}}}(\vec{r})\xi_{\vec{r_{0}}}(\vec{r'})=\int d^{3}r_{0}~\delta(\vec{r}-\vec{r_{0}})\delta(\vec{r'}-\vec{r_{0}})=\delta(\vec{r}-\vec{r'})$$
para deduzir isto podemos seguir a dedução da relação de fecho numa base discreta:
$$\psi(\vec{r})=\int d^{3}r_{0}~\psi(\vec{r_{0}})\xi_{\vec{r_{0}}}(\vec{r})=\int d^{3}r_{0} \left(\int d^{3}r'~\xi_{\vec{r_{0}}}^{*}(\vec{r'})\psi(\vec{r'}) \right) \xi_{\vec{r_{0}}}(\vec{r})=\int d^{3}r'~ \psi(\vec{r'})\int d^{3}r_{0}~\xi_{\vec{r_{0}}}(\vec{r})\xi_{\vec{r_{0}}}(\vec{r'})=\int d^{3}r'~ \psi(\vec{r'})\delta(\vec{r}-\vec{r'})$$

**Ortonormalidade**
- Podemos calcular:
$$(\xi_{\vec{r_{0}}},\xi_{\vec{r_{0}'}})=\int d^{3}r~\xi_{\vec{r_{0}}}^{*}(\vec{r})\xi_{\vec{r_{0}'}}(\vec{r})=\int d^{3}r~\delta(\vec{r}-\vec{r_{0}})\delta(\vec{r}-\vec{r_{0}'})=\delta(\vec{r_{0}'}-\vec{r_{0}'})$$

**Discreto VS Deltas
$$\boxed{\begin{align*}
Discreto &&\Longleftrightarrow&&& Funções~Delta\\
i &&\Longleftrightarrow&&& \vec{r_{0}}\\
\sum\limits_{i} &&\Longleftrightarrow&&& \int d^{3}r_{0}\\
\delta_{ij} &&\Longleftrightarrow&&& \delta(\vec{r_{0}}-\vec{r_{0}'}) 
\end{align*}}$$

### 2.1.3.3 - Generalização : bases contínuas ortonormais 
**Definição**
- Aproveitando o que fomos vendo na base de funções de onda planas e na base de funções delta, vamos definir uma base geral de funções ortonormais e contínua. Temos então: $\{w_{\alpha}(\vec{r})\}$ em que $\alpha$ é o parâmetro contínuo. 
- Esta base terá que obedecer à *relação de fecho*:
$$\int d\alpha~w_{\alpha}(\vec{r})w_{\alpha}^{*}(\vec{r'})=\delta(\vec{r}-\vec{r'})$$
e à *relação de ortonormalização*:
$$(w_{\alpha},w_{\alpha'})=\int d^{3}r~ w_{\alpha}^{*}(\vec{r})w_{\alpha'}(\vec{r})=\delta(\alpha-\alpha')$$

- Tal como já disse nas funções de onda plana, se $\alpha=\alpha'$ o integral da relação de ortonormalização diverge. Assim, $w_{\alpha}(\vec{r})\notin\mathscr{F}$
- $\alpha$ pode ser um vetor (como foi o caso de $\vec{p}$ e $\vec{r_{0}}$)

**Componentes de função de onda $\psi(\vec{r})$**
- Podemos sempre escrever:
$$\psi(\vec{r})=\int d^{3}r'~\psi(\vec{r'})\delta(\vec{r}-\vec{r'})$$
se substituirmos o delta de Dirac pela relação de fecho para uma base ortonormal contínua:
$$\begin{align*}
\psi(\vec{r})&= \int d^{3}r' ~\psi(\vec{r'})\int d\alpha~w_{\alpha}(\vec{r})w_{\alpha}^{*}(\vec{r'})\\
&= \int d\alpha~w_{\alpha}(\vec{r})\int d^{3}r'~w_{\alpha}^{*}(\vec{r'})\psi(\vec{r'})\\
&= \int d\alpha~w_{\alpha}(\vec{r})(w_{\alpha},\psi)
\end{align*}$$
ou seja:
$$\begin{align*}
\psi(\vec{r})&= \int d\alpha ~c(\alpha)w_{\alpha}(\vec{r})\\
c(\alpha)&= (w_{\alpha},\psi)= \int d^{3}r~w_{\alpha}^{*}(\vec{r})\psi(\vec{r})
\end{align*}$$
sendo estas equações aquelas que nos permitem definir $\psi$ na base $\{w_{\alpha}\}$ com os seus componentes $c(\alpha)$.

**Produto Escalar e norma em função de componentes**
- Tendo-se 2 funções definidas na base $\{w_{\alpha}\}$:
$$\varphi(\vec{r})=\int d\alpha~b(\alpha)w_{\alpha}(\vec{r}) \quad \quad;\quad \quad \psi(\vec{r})=\int d\alpha' c(\alpha')w_{\alpha'}(\vec{r})$$
- O seu produto escalar será:
$$\begin{align*}
(\varphi,\psi)&= \int d^{3}r ~\varphi^{*}(\vec{r})\psi(\vec{r})\\
&= \int d\alpha\int d\alpha' b^{*}(\alpha)c(\alpha')~\underbrace{\int d^{3}r~w_{\alpha}^{*}(\vec{r})w_{\alpha'}(\vec{r})}_{\textsf{Ortonormalização}}\\
&= \int d\alpha\int d\alpha' b^{*}(\alpha)c(\alpha')\delta(\alpha-\alpha')\\
&= \int d\alpha ~b^{*}(\alpha)c(\alpha)
\end{align*}$$
que, em particular, nos dá:
$$(\psi,\psi)=|\psi|^{2}=\int d\alpha ~|c(\alpha)|^{2}$$
***Discreto VS Contínua***
$$\boxed{\begin{align*}
Discreto &&\Longleftrightarrow&&& Contínua\\
i &&\Longleftrightarrow&&& \alpha\\
\sum\limits_{i} &&\Longleftrightarrow&&& \int d\alpha\\
\delta_{ij} &&\Longleftrightarrow&&& \delta(\alpha-\alpha') 
\end{align*}}$$

**Bases mistas**
- Em certos problemas físicos, podemos ter uma região do espaço que é descrita por uma base discreta de funções $\{u_{i}(\vec{r})\}$ e outra por uma base contínua $\{w_{\alpha}(\vec{r})\}$. 
- Nesse caso as relações de ortonormalização são:
$$\begin{align*}
(u_{i},u_{j})&= \delta_{ij}\\
(w_{\alpha},w_{\alpha'})&= \delta(\alpha-\alpha')\\
(u_{i},w_{\alpha})&= 0
\end{align*}$$
e a relação de fecho:
$$\sum\limits_{i}u_{i}(\vec{r})u_{i}^{*}(\vec{r'}) + \int d\alpha~w_{\alpha}(\vec{r})w_{\alpha}(\vec{r'})=\delta(\vec{r}-\vec{r'})$$

### Tabela Discreto VS Contínuo
![[tabela base discreta e continua.png]]
(Já disse que adoro o Cohen? Adoro o Cohen)

## 2.2 - Notação de Dirac
### 2.2.1 - Intro
- O estado quântico de uma partícula num instante é dado pela sua função de onda $\psi(\vec{r})$. Devido ao seu significado físico/probabilístico, as funções de onda têm que ser funções de quadrado somável. 
- Desta forma, definimos a base de funções de onda de 1 partícula, $\mathscr{F}\in L^{2}$.
- Vimos que uma função de onda pode ser representada em várias bases distintas, sendo que terá os componentes:
![[bases contínuas.png]]

- Ora, a função de onda pode ser definida em qualquer base, sendo qualquer definição igualmente correta. Isto é o que temos no espaço R3: um ponto pode ser descrito num referencial cartesiano, esférico, cilindrico, etc e é sempre o mesmo ponto. 
- Na mecânica quântica iremos usar uma lógica semelhante: a função de estado é fisicamente a mesma em qualquer base, pelo que iremos usar um *vetor de estado* que pertence ao *espaço de estados da partícula* $\mathscr{E}_\vec{r}$. Por $\mathscr{F}\in L^{2}$, temos que $\mathscr{E}$ pertence ao espaço de Hilbert (basicamente um espaço em que existe produto interno e distâncias; [ver Wikipedia](https://en.wikipedia.org/wiki/Hilbert_space)).
- Assim, iremos introduzir a notação e regras de cálculo com vetores do espaço de estado. Isto permite muitas vezes simplificar as contas e até generalizar para problemas que não podem ser descritos por uma função de onda. Desta forma, as regras que vamos definir são válidas para qualquer sistema físico.

### 2.2.1 - Vetores Ket e Bra
#### 2.2.1.1 - Kets
- Todos os elementos do espaço de estados $\mathscr{E}$ são denominados de Ket. Por exemplo, são representados por $|\psi\rangle$
- Mais concretamente, para todas as funções de onda podemos dizer:
$$\psi(\vec{r})\in\mathscr{F} ~~\Longleftrightarrow ~~ |\psi\rangle \in \mathscr{E}_{\vec{r}}$$
- A primeira coisa a notar é que já não aparece a dependência de $\psi$ em $\vec{r}$. Isto porque $\vec{r}$ apenas representa os componentes de $|\psi\rangle$ numa base específica.
- Quando se escrever $\mathscr{E}_{x}$ estamos a tratar do espaço de estado de uma partícula sem spin em 1D. Ou seja, temos um espaço de estado que apenas inclui funções de onda 1D.

#### 2.2.1.2 - Bras
**Espaço dual de $\mathscr{E}$**
- Podemos definir um funcional linear $\chi$ que atua nos kets:
$$\begin{align*}
|\psi\rangle\in\mathscr{E}~~ &\xrightarrow{~~\chi~~} \chi(|\psi\rangle) ~~~~(\in\mathbb{C})\\
\chi(\lambda_{1}|\psi_{1}\rangle+\lambda_{2}|\psi\rangle)&= \lambda_{1}\chi(|\psi_{1}\rangle) + \lambda_{2}\chi(|\psi_{2}\rangle)
\end{align*}$$

ou seja, um funcional linear associa a cada ket um número complexo. Por outro lado, um operador linear associada a cada ket outro ket.

- O espaço dual do espaço de estados, que representaremos como $\mathscr{E}^{*}$, consiste no conjunto de todos os funcionais lineares. 
    - Noutras palavras: $\mathscr{E}$ é o conjunto de todos os kets. Para cada ket temos um funcional. $\mathscr{E}^{*}$ é o conjunto de todos os funcionais.

**Bra**
- Aos elementos dos espaço dual $\mathscr{E}^{*}$ chamamos de Bra. Por exemplo, podemos ter $\langle\chi|$, o bra que representa o funcionar linear $\chi$. Desse modo, iremos escrever a atuação do funcional sobre o ket $|\psi\rangle$ da forma:
$$\chi(|\psi\rangle)=\langle \chi|\psi\rangle$$
> Fun fact: ao símbolo $\langle~|~\rangle$ chamamos de "bracket". Daí "bra" e "ket"

#### 2.2.1.3 - Bras e Kets
**Para cada Ket há 1 Bra**
- Por existir produto escalar em $\mathscr{E}$ (por pertencer ao espaço de Hilbert), a cada ket $|\varphi\rangle\in\mathscr{E}$ podemos associar um bra $\langle\varphi|\in\mathscr{E}^{*}$.
- Tendo-se o ket $|\varphi\rangle$, podemos definir o funcional linear/bra correspondente como sendo aquele em que temos a relação:
$$\langle\varphi|\psi\rangle=(|\varphi\rangle,|\psi\rangle)$$
ou seja, o funcional que ao atuar em qualquer ket $|\psi\rangle\in\mathscr{E}$ dá o mesmo número complexo que o produto escalar $(|\varphi\rangle,|\psi\rangle)$.

**Correspondência Anti-Linear**
- Como já vimos, o produto escalar em $\mathscr{E}$ é anti-linear no 1º termo:
$$\begin{align*}
(\lambda_{1}|\varphi_{1}\rangle+\lambda_{2}|\varphi_{2}\rangle,|\psi\rangle)&= \lambda_{1}^{*}(|\varphi_{1}\rangle,|\psi\rangle) + \lambda_{2}^{*}(|\varphi_{2}\rangle,|\psi\rangle)\\
&= \lambda_{1}^{*} \langle \varphi_{1}|\psi\rangle + \lambda_{2}^{*} \langle \varphi_{2}|\psi\rangle\\
&= (\lambda_{1}^{*}\langle\varphi_{1}|+\lambda_{2}^{*}\langle\varphi_{2}|)|\psi\rangle
\end{align*}$$
ou seja, ao ket $\lambda_{1}|\varphi_{1}\rangle+\lambda_{2}|\varphi_{2}\rangle$ está associado o bra $\lambda_{1}^{*}\langle\varphi_{1}|+\lambda_{2}^{*}\langle\varphi_{2}|$.

- Daqui temos que podemos escrever $\lambda|\psi\rangle=|\lambda\psi\rangle$. Mas é importante não esquecer que $\langle\lambda\psi|=\lambda^{*}\langle\psi|$

**Propriedades do Produto Escalar escritas na notação de Dirac**
$$\begin{align*}
\langle\varphi|\psi\rangle&= \langle\psi|\varphi\rangle^{*}\\
\langle\varphi|\lambda_{1}\psi_{1}+\lambda_{2}\psi_{2}\rangle&= \langle\varphi|(\lambda_{1}|\psi_{1}\rangle+\lambda_{2}|\psi_{2}\rangle)=\lambda_{1}\langle\varphi|\psi_{1}\rangle+\lambda_{2}\langle\varphi|\psi_{2}\rangle\\
\langle\lambda_{1}\varphi_{1}+\lambda_{2}\varphi_{2}|\psi\rangle&= (\lambda_{1}^{*}\langle\varphi_{1}|+\lambda_{2}^{*}\langle\varphi_{2}|)|\psi\rangle=\lambda_{1}^{*}\langle\varphi_{1}\psi\rangle+\lambda_{2}^{*}\langle\varphi_{2}|\psi\rangle\\
\langle\psi|\psi\rangle&\ge 0
\end{align*}$$

**Há 1 Ket para cada Bra?**
- Vimos que cada ket tem 1 bra. No entanto, é possível que tenhamos bras sem kets correspondentes.

- No Cohen tem um bom exemplo com funções Delta $\xi_{x_{0}}^{(\varepsilon)}$, em que $\varepsilon$ é a largura do pico e $1/\varepsilon$ a sua amplitude. 
    - Consoante $\varepsilon\to0$, o ket $|\xi_{x_{0}}^{(\varepsilon)}\rangle$ deixa de pertencer a $\mathscr{E}_{x}$. 
    - No entanto, o bra $\langle\xi_{x_{0}}^{(\varepsilon)}|$ continua a pertencer a $\mathscr{E}_{x}^{*}$, sendo que para $\varepsilon\to0$ temos $\langle \xi_{x_{0}}|\psi\rangle=\psi(x_{0})$
    - Ou seja, para certos valores de $\varepsilon$ ficamos com bras sem kets correspondentes.
- Na prática, isto acontece porque para uma função ser um ket é preciso ser de quadrado somável ($\in \mathscr{F}$). Para um funcional ser um bra só precisa de converter todos os kets de $\mathscr{E}$ em algum número complexo.

- Consideremos agora a função de onda plana $v_{p_{0}}^{(L)}(x)=\frac{1}{\sqrt{2\pi\hbar}}e^{ip_{0}x/\hbar}$ definida no intervalo $\frac{-L}{2}\le x\le \frac{+L}{2}$. 
    - O ket associado a esta função será $|v_{p_{0}}^{(L)}\rangle$. Temos que $\int_{-L/2}^{L/2}|v_{p_{0}}|^{2}\sim \frac{L}{2\pi\hbar}$. Assim, se $L\to\infty$ passamos a ter $|v_{p_{0}}^{(L)}\rangle\notin\mathscr{E}_{x}$ porque $v_{p_{0}}^{(L)}\notin\mathscr{F}$
    - Para o bra temos: $\langle v_{p_{0}}^{(L)}|\psi\rangle=(v_{p_{0}}^{(L)},\psi)\simeq \frac{1}{\sqrt{2\pi\hbar}}\int_{-L/2}^{L/2}dx~e^{-ip_{0}x/\hbar}\psi(x)$.
    - Ora, se $L\to\infty$ ficamos com a fórmula da transformada de Fourier. Ou seja: $\lim_{L\to\infty}\langle v_{p_{0}}^{(L)}|=\langle v_{p_{0}}|\in\mathscr{E}_{x}^{*}$ em que $\langle v_{p_{0}}|\psi\rangle=\tilde \psi(p_{0})$

- Conforme ilustrado nos 2 exemplos acima, nos limites $\varepsilon\to0,L\to\infty$, esta falta de correspondência deve-se usarmos "bases" de funções $\notin\mathscr{F}_{x}$. Por essa razão, não temos kets para estas funções.
- No entanto, vimos que o produto escalar $(v_{p_{0}},\psi)$ ou $(\xi_{x_{0}},\psi)$ estava definido, pelo que conseguimos associar um funcional linear a $v_{p_{0}}/\xi_{x_{0}}$ AKA um bra $\in\mathscr{E}_{x}^{*}$.
- Ora, nós usamos estas funções porque nos permitem simplificar cálculos. Assim, iremos criar "kets generalizados" associados a funções de quadrado não somável, mas em que o produto escalar com qualquer função de $\mathscr{F}_{x}$ está definido. 
- Teremos então os "kets" $|\xi_{x_{0}}\rangle,|v_{p_{0}}\rangle$ que iremos usar em cálculos como kets normais, mas que devemos recordar que *não representam estados físicos*.

- Consideremos como exemplo a função $v_{p_{0}}$. Do ponto de vista matemático, esta "aproximação" não chega a causar problemas desde que $L$ seja sempre suficientemente superior às restantes dimensões do problema. 
    - Começamos por definir $|v_{p_{0}}\rangle$ que na realidade é $|v_{p_{0}}^{(L)}\rangle$
    - Nos cálculos intermédios nunca chegamos a calcular o limite $\lim_{L\to\infty}$, de modo a continuarmos a ter  $|v_{p_{0}}^{(L)}\rangle\in\mathscr{E}_{x}$ 
    - O resultado final obtido irá depender muito pouco de $L$, novamente, desde que ele seja suficientemente maior que as restantes dimensões. Podemos então simplesmente substituir $L=\infty$.
- Podemos ainda notar o "erro" em que (ao contrário de $\{v_{p_{0}}\}$), a base $\{v_{p_{0}}^{(L)}\}$ não é ortonormada e não segue a relação de fecho. Na realidade, desde que $L$ seja suficiente elevado em comparação aos outros comprimentos do problema, a base cumpre as 2 relações com uma aproximação suficientemente boa.
- Os 2 pontos acima podem ser repetidos para $\{\xi_{x_{0}}^{(\varepsilon)}\}$ tendo-se que $\varepsilon\to0$.

### 2.2.2 - Operadores Lineares
#### 2.2.2.1 - Definição
- Um operador linear $A$ associa a cada ket $|\psi\rangle\in\mathscr{E}$ outro ket $|\psi'\rangle\in\mathscr{E}$, tendo-se:
$$\begin{align*}
|\psi'\rangle&= A|\psi\rangle\\
A(\lambda_{1}|\psi_{1}\rangle+\lambda_{2}|\psi_{2}\rangle)&= \lambda_{1}A|\psi_{1}\rangle+\lambda_{2}A|\psi_{2}\rangle
\end{align*}$$
- O produto de dois operadoores lineares é definido como:
$$(AB)|\psi\rangle=A(B|\psi\rangle)$$
em que $B$ atua em $|\psi\rangle$, dando origem ao ket $B|\psi\rangle$, em que $A$ irá atuar.
- Temos o comutador entre 2 operadores lineares:
$$[A,B]=AB-BA$$
- Temos ainda o elemento da matriz de $A$:
$$\langle\varphi|(A|\psi\rangle)$$
- O elemento da matriz é portanto o produto escalar entre os kets $|\varphi\rangle$ e $A|\psi\rangle$, sendo um número complexo.

#### 2.2.2.2 - Projetores
**Nota sobre Notação de Dirac**
- Como vimos acima: $\langle\varphi|\psi\rangle$ reprenseta um bra $\langle\varphi|$ a atuar num ket $|\psi\rangle$. Isso será também igual ao produto escalar entre os kets $|\varphi\rangle,|\psi\rangle$.
- Consideremos agora que se escreveu $|\psi\rangle\langle\varphi|$.
- Consideremos um ket arbitrário $|\chi\rangle$. Se tivermos: $|\psi\rangle\langle\varphi|\chi\rangle$ 
    - O termo $\langle\varphi|\chi\rangle$ não passa de um bra a atuar no ket arbitrário (ou o produto escalar  $(|\varphi\rangle,|\chi\rangle)$), sendo este um número complexo.
    - Logo $|\psi\rangle\langle\varphi|\chi\rangle$ terá de ser um ket, porque estamos a multiplicar o ket $|\psi\rangle$ pelo escalar $\langle\varphi|\chi\rangle$.
    - Portanto $|\varphi\rangle\langle\psi|$ e um **_operador_**.

- Assim, a ordem em que os símbolos (kets, bras e operadores) aparecem é fundamental!
- Em qualquer equação de kets e bras, números/escalares podem ser movidos livremente:
$$\begin{align*}
|\psi\rangle\lambda&= \lambda|\psi\rangle\\
\langle\psi|\lambda&= \lambda\langle\psi|\\
A\lambda|\psi\rangle&= \lambda A|\psi\rangle\\
\langle \varphi|\lambda|\psi\rangle&= \lambda\langle\varphi|\psi\rangle=\langle\varphi|\psi\rangle\lambda
\end{align*}$$

**Projetor $P_{\psi}$ num ket $|\psi\rangle$**
- Consideremos um qualquer ket $|\psi\rangle$ normalizado ($\langle\psi|\psi\rangle=1$). O operador projetor em $|\psi\rangle$ é definido como:
$$P_{\psi}=|\psi\rangle\langle\psi|$$
- Ao atuar num ket arbitrário $|\varphi\rangle$: $$P_{\psi}|\varphi\rangle=|\psi\rangle\langle\psi|\varphi\rangle$$
temos, tal como visto acima, que $\langle\psi|\varphi\rangle$ é um escalar. Ou seja, quando o operador $P_{\psi}$ atua em $|\varphi\rangle$ resulta num ket proporcional a $|\psi\rangle$, em que a constante de proporcionalidade é dada pelo produto escalar.
- É evidente o significado geométrico deste operador: $P_{\psi}$ projeta os kets sobre o ket $|\psi\rangle$.
    - A forma de verificar se este é um projetor é ver se: $$\begin{align*}
P_{\psi}^{2}&= P_{\psi}\\
|\psi\rangle\underbrace{\langle\psi|\psi\rangle}_{=1}\langle\psi|&=|\psi\rangle\langle\psi| \\
|\psi\rangle\langle\psi|&= |\psi\rangle\langle\psi|
\end{align*}$$
    - Podemos ainda verificar que se $|\psi\rangle$ e $|\varphi\rangle$ forem ortogonais a projeção é nula. Se compararmos com vetores, isto faz sentido.

**Projetor num subespaço**
- Consideremos $q$ kets normalizados e ortogonais entre si: $|\varphi_{1}\rangle,|\varphi_{2}\rangle,\dots,|\varphi_{q}\rangle$. Teremos:
$$\langle\varphi_{i}|\varphi_{j}\rangle=\delta_{ij}\quad \quad;\quad i,j=1,2,\dots,q$$
- Podemos então definir o seguinte operador:
$$P_{q}=\sum\limits_{i=1}^{q}|\varphi_{i}\rangle\langle\varphi_{i}|$$
e podemos calcular o seu quadrado:
$$\begin{align*}
P_{q}^{2}&= \sum\limits_{i=1}^{q}\sum\limits_{j=1}^{q} |\varphi_{i}\rangle\langle \varphi_{i}|\varphi_{j}\rangle\langle\varphi_{j}|\\
&= \sum\limits_{i=1}^{q}\sum\limits_{j=1}^{q} |\varphi_{i}\rangle\delta_{ij}\langle\varphi_{j}|\\
&= \sum\limits_{i=1}^{q}|\varphi_{i}\rangle\langle\varphi_{i}|=P_{q}
\end{align*}$$
- Quando $P_{q}$ é aplicado a um ket arbitrário $|\psi\rangle$ temos: $P_{q}|\psi\rangle=\sum_{i=1}^{q}|\varphi_{i}\rangle\langle\varphi_{i}|\psi\rangle$ Vemos então que quando este atua num ket $\psi\rangle$, o resultado é a sobreposição das projeções de $|\psi\rangle$ em todos os kets que formam a base.

### 2.2.3 - Conjugação Hermítica
#### 2.2.3.1 - Ação de Operador Linear em Bra
- Consideremos um bra $\langle\varphi|$ e um ket arbitrário $|\psi\rangle$. Fixando $\langle\varphi|$ e tendo um operador linear $A$, a cada ket $|\psi\rangle$ podemos associar um número complexo: $\langle\varphi|(A|\psi\rangle)$ (em que convém recordar que $A|\psi\rangle$ é um ket). Por isto não passar de um produto escalar, temos que o número complexo $\langle\varphi|(A|\psi\rangle)$ varia linearmente com $|\psi\rangle$
- Por outro lado, se variarmos o bra $\langle\varphi|$ ou o operador $A$, o resultado de $\langle\varphi|(A|\psi\rangle)$ será outro. Assim, podemos considerar que $\langle\varphi|A$ formam um *funcional linear* em $\mathscr{E}$. Ou seja, $\langle\varphi|A$ gera um novo bra $\in\mathscr{E}^{*}$.
- Podemos portanto escrever:
$$(\langle\varphi|A)|\psi\rangle=\langle\varphi|(A|\psi\rangle)$$
(atenção aos parênteses)

- Assim, um operador linear $A$ associa a um bra $\langle\varphi|$ um novo bra $\langle\varphi'|$. 

**Relação Linear**
- Demonstremos que um operador linear atua num bra de forma linear.
- Temos o operador linear $A$ e o bra $\langle\chi|=\lambda_{1}\langle\varphi_{1}|+\lambda_{2}\langle\varphi_{2}|$
- Podemos escrever a atuação do bra $\langle\chi|A$ num ket $|\psi\rangle$:
$$\begin{align*}
(\langle\chi|A)|\psi\rangle&= \langle\chi|(A|\psi\rangle)\\
&= \lambda_{1}\langle\varphi_{1}|(A|\psi\rangle)+\lambda_{2}\langle\varphi_{2}|(A|\psi\rangle)\\
&= \lambda_{1}(\langle\varphi_{1}|A)|\psi\rangle+\lambda_{2}(\langle\varphi_{2}|A)|\psi\rangle\\
\end{align*}$$
e sendo o ket arbitrário, isto implica que:
$$\langle\chi|A=\lambda_{1}\langle\varphi_{1}|A+\lambda_{2}\langle\varphi_{2}|A$$
ou seja, a relação é linear.

> Na dedução acima, a transição $\langle\chi|(A|\psi\rangle)=\lambda_{1}\langle\varphi_{1}|(A|\psi\rangle)+\lambda_{2}\langle\varphi_{2}|(A|\psi\rangle)$ pode fazer-te confusão. O produto escalar não é antilinear para o 1º termo?
> Ora, a propriedade que aqui temos é a seguinte: $\langle\lambda_{1}\varphi_{1}+\lambda_{2}\varphi_{2}|\psi\rangle= (\lambda_{1}^{*}\langle\varphi_{1}|+\lambda_{2}^{*}\langle\varphi_{2}|)|\psi\rangle=\lambda_{1}^{*}\langle\varphi_{1}|\psi\rangle+\lambda_{2}^{*}\langle\varphi_{2}|\psi\rangle$
>     O produto escalar é antilinear, mas isso só se aplica ao caso em que temos o bra de uma combinação linear de funções. Posso pensar nisso na forma: "a conversão da função $\varphi$ (ou do ket $|\varphi\rangle$) para o bra $\langle\varphi|$ é antilinear".
>     Se tivermos, como acima, um bra que é uma combinação linear de bras, apenas temos a distribuição de termos normalmente.

- Vimos agora ao definir a ação de um operador num bra que temos:
$$\langle \varphi|(A|\psi\rangle)=(\langle\varphi|A)|\psi\rangle=\langle\varphi|A|\psi\rangle$$
pelo que deixaremos de usar parenteses ao representar os elementos da matriz de $A$.

#### 2.2.3.2 - Operador Adjunto
- Da mesma forma que a cada ket $|\psi\rangle$ associamos um bra $\langle\psi|$, a um operador $A$ veremos que podemos associar um operador adjunto $A^{\dagger}$. 

- Sendo $|\psi\rangle$ um ket arbitrário $\in\mathscr{E}$.
    - Já vimos que o operador linear $A$ associa a cada ket um outro ket: $|\psi'\rangle=A|\psi\rangle$.
    - Ora, ao ket $|\psi'\rangle$ terá que corresponder um bra $\langle\psi'|$.
    - Temos então o **operador adjunto de $A$**: associa a um bra $\langle\psi|\in\mathscr{E}^{*}$ outro bra $\langle\psi'|$: $$\langle\psi'|=\langle\psi|A^{\dagger}$$

**Adjunto é operador linear com Bra**
- O bra $\lambda_{1}\langle\psi_{1}|+\lambda_{2}\langle\psi_{2}|$ corresponde ao ket $\lambda_{1}^{*}|\psi\rangle+\lambda_{2}^{*}|\psi\rangle$.
- Ao aplicar o operador $A$ neste ket ficamos com $A(\lambda_{1}^{*}|\psi\rangle+\lambda_{2}^{*}|\psi\rangle)=\lambda_{1}^{*}A|\psi\rangle+\lambda_{2}^{*}A|\psi\rangle=\lambda_{1}^{*}|\psi_{1}'\rangle+\lambda_{2}^{*}|\psi_{2}'\rangle$.
- Ora, isto será correspondente ao bra $\lambda_{1}\langle\psi_{1}'|+\lambda_{2}\langle\psi_{2}'|$
- Por outras palavras:
$$\lambda_{1}\langle\psi_{1}'|+\lambda_{2}\langle\psi_{2}'|=(\lambda_{1}\langle\psi_{1}|+\lambda_{2}\langle\psi_{2}|)A^{\dagger}$$

- Podemos portanto escrever:
$$|\psi'\rangle=A|\psi\rangle ~~\Longleftrightarrow~~ \langle\psi'|=\langle\psi|A^{\dagger}$$

Se juntarmos esta relação ao facto que $\langle\psi'|\varphi\rangle=\langle\varphi|\psi'\rangle^{*}$, podemos escrever:
$$\langle\psi|A^{\dagger}|\varphi\rangle=\langle\varphi|A|\psi\rangle^{*}$$
em que esta relção é válida para quaisquer kets $|\varphi\rangle,|\psi\rangle$.

>*Dedução*
>Temos $\langle\psi|A^{\dagger}=\langle\psi'|$. Se multiplicarmos os 2 lados por um ket arbitrário $|\varphi\rangle$ ficamos com:
 >$$\begin{align*}
\langle\psi|A^{\dagger}|\varphi\rangle&=  \langle\psi'|\varphi\rangle\\&=  \langle\varphi|\psi'\rangle^{*}
\end{align*}$$
 >e temos que $|\psi'\rangle=A|\psi\rangle$. Logo:
 >$$\langle\psi|A^{\dagger}|\varphi\rangle=\langle\varphi|A|\psi\rangle^{*}$$

**Nota sobre notação**
- Tal como vimos atrás, podemos escrever $\lambda|\psi\rangle=|\lambda\psi\rangle$ e $\langle\lambda\psi|=\lambda^{*}\langle\psi|$.
- Podemos fazer algo com operadores:
    - Para kets podemos simplesmente escrever: $|A\psi\rangle=A|\psi\rangle$
    - Para bras fazemos o equivalente ao que faziamos com um escalar: $\langle A\psi|=\langle\psi|A^{\dagger}$ (de notar que o operador tem que estarr à direita do bra)

#### 2.2.3.3 - Correspondência entre Operador e seu Adjunto
- Das relações $\langle\psi|A^{\dagger}|\varphi\rangle=\langle\varphi|A|\psi\rangle^{*}$ e $|\psi'\rangle=A|\psi\rangle \Leftrightarrow \langle\psi'|=\langle\psi|A^{\dagger}$ podemos deduzir as seguintes propriedades:
$$\begin{align*}
(A^{\dagger})^{\dagger}&= A\\
(\lambda A)^{\dagger}&= \lambda^{*}A^{\dagger}\\
(A+B)^{\dagger}&= A^{\dagger}+B^{\dagger}\\
(AB)^{\dagger}&= B^{\dagger}A^{\dagger}
\end{align*}$$
vamos deduzir a última:
    - Consideremos o ket $|\varphi\rangle=AB|\psi\rangle=A(B|\psi\rangle)$. 
    - Vamos definir $|\chi\rangle=B|\psi\rangle$. Temos $|\varphi\rangle=A|\chi\rangle$.
    - Por definição: $$\begin{align*}
|\varphi\rangle=AB|\psi\rangle ~~\Longleftrightarrow~~ \langle\varphi|&= \langle\psi|(AB)^{\dagger}\\
&= \langle\chi|A^{\dagger}\\
\end{align*}$$
    - Mas temos, também por definição:$$\begin{align*}
|\chi\rangle=B|\psi\rangle~~\Longleftrightarrow~~ \langle\chi|=\langle\psi|B^{\dagger}
\end{align*}$$
    - Logo fica:$$|\varphi\rangle=AB|\psi\rangle ~~\Longleftrightarrow~~ \langle\varphi|=\langle\psi|B^{\dagger}A^{\dagger}$$
    - Ou seja: $$(AB)^{\dagger}=B^{\dagger}A^{\dagger}$$ 

- Tendo em conta as propriedades listadas podemos escrever a relação dos elementos da matris $(\langle\varphi|A)|\psi\rangle=\langle\varphi|(A|\psi\rangle)$ na forma:
$$\langle A^{\dagger}\varphi|\psi\rangle=\langle\varphi|A\psi\rangle$$
em que $\langle A^{\dagger}\varphi|=\langle\varphi|(A^{\dagger})^{\dagger}=\langle\varphi|A$

#### 2.2.3.4 - Conjugação Hermítica na Notação de Dirac
- Definimos o operador adjunto partindo da correspondência entre kets $|\psi\rangle$ e bras $\langle\psi|$. Ora, um ket e o bra correspondente são *conjugados hermíticos* um do outro.
- Também $A^{\dagger}$ é o conjugado hermítico de $A$ e vice-versa.
- O conjugado hermítico de uma constante/escalar é o seu complexo conjugado. 

- Vimos que quando esta operação ocorre, cada elemento se transforma no seu conjugado e os elementos trocam de ordem: 
    - $A|\psi\rangle$ torna-se $\langle\psi|A^{\dagger}$
    - Vimos também que $AB$ torna-se $B^{\dagger}A^{\dagger}$

- Temos outra relação útil:
$$(|u\rangle\langle v|)^{\dagger}=|v\rangle\langle u|$$
(na prática estamos a seguir a mesma lógica. Cada elemento se transforma no seu conjugado $|u\rangle\to\langle u|,\langle v|\to|v\rangle$ e troacam de ordem)

>*Demonstração*
>$|u\rangle\langle v|$ é um operador. Assim, podemos establecer a seguinte relação entre os elementos da sua matriz: $$\begin{align*}
\langle \psi|A^{\dagger}|\varphi\rangle&= \langle\varphi|A|\psi\rangle^{*}\\
&\downarrow\\
\langle \psi|(|u\rangle\langle v|)^{\dagger}|\varphi\rangle&= \langle\varphi|(u\rangle\langle v|)|\psi\rangle^{*}\\
&= \langle\varphi|u\rangle^{*}\langle v|\psi\rangle^{*}\\
&= \langle u|\varphi\rangle\langle \psi|v\rangle\\
&= \langle\psi|v\rangle\langle u|\varphi\rangle\\
&= \langle\psi|(|v\rangle\langle u|)|\varphi\rangle
\end{align*}$$
> Ou seja: $$(|u\rangle\langle v|)^{\dagger}=|u\rangle\langle v|$$

### Notinha resumo de complexo conjugado
![[trocar para conjugado hermitico.png]]


- Dois Exemplos:
    - $\lambda\langle u|A|v\rangle|w\rangle\langle\psi| ~\to~ |\psi\rangle\langle w| \langle v|A^{\dagger}|u\rangle \lambda^{*}=\langle v|A^{\dagger}|u\rangle \lambda^{*}~|\psi\rangle\langle w|$
    - $\lambda|u\rangle\langle v|w\rangle~\to~\langle w|v\rangle\langle u|\lambda^{*}=\lambda^{*}\langle w|v\rangle~\langle u|$ 

#### 2.2.3.5 - Operadores Hermíticos
- Um operador $A$ é hermítico se:
$$A=A^{\dagger}$$
- A relação $\langle \psi|A^{\dagger}|\varphi\rangle= \langle\varphi|A|\psi\rangle^{*}$ torna-se portanto:
$$\langle \psi|A|\varphi\rangle=\langle\varphi|A|\psi\rangle^{*}$$
- A relação $\langle A^{\dagger}\varphi|\psi\rangle=\langle \varphi|A\psi\rangle$ fica:
$$\langle A\varphi|\psi\rangle=\langle \varphi|A\psi\rangle=\langle\varphi|A|\psi\rangle$$
- O produto entre 2 operadores hermíticos é hermítico se $[A,B]=0$.
- Facilmente vemos que o operador $P_{\psi}=|\psi\rangle\langle\psi|$ é hermítico.

## 2.3 - Representações no espaço de estados
### 2.3.1 - Intro
- Para representar algo precisamos de uma base ortonormal (discreta ou contínua). Os vetores e operadores serão representados por números nesta base (os vetores pelas suas componentes, os operadores pelos elementos da sua matriz). 
- O cálculo vetorial que vimos atrás torna-se então em cálculo matricial.
- Nesta secção iremos então voltar a ver todas as noções de bases discretas e contínuas de $\mathscr{F}$, agora com representações em notação de Dirac.

### 2.3.2 - Relações caraterísticas de base ortonormada
#### 2.3.2.1 - Relação de Ortonormalização
- De forma semelhante ao que tínhamos na secção 2.1, temos agora:
**Bases discretas**
$$\langle u_{i}|u_{j}\rangle=\delta_{ij}$$
**Bases contínuas**
$$\langle w_{\alpha}|w_{\alpha'}\rangle=\delta(\alpha-\alpha')$$
em que $\langle w_{\alpha}|w_{\alpha}\rangle=\infty=|w_{\alpha}|^{2}$. Logo $|w_{\alpha}\rangle\notin\mathscr{E}$. Ou seja, os elementos de uma base contínua não podem representar estados físicos. De qualquer forma, iremos usar $|w_{\alpha}\rangle$ como kets normais, como um passo intermédio de cálculo (como já discutido atrás).

#### 2.3.2.2 - Relação de Fecho
**Bases discretas**
- Um estado $|\psi\rangle$ poderá ser representado na base $\{|u_{i}\rangle\}$ com uma expansão única:
$$|\psi\rangle=\sum\limits_{i}c_{i}|u_{i}\rangle$$
- Sendo a base ortonormada, ao multiplicar os 2 lados da equação acima pelo bra $\langle u_{j}|$ ficamos com: $$\langle u_{j}|\psi\rangle=c_{j}$$
- Ao substituir $c_{i}=\langle u_{i}|\psi\rangle$ na equação de $|\psi\rangle$ acima, podemos obter:
$$\begin{align*}
|\psi\rangle&= \sum\limits_{i}c_{i}|u_{i}\rangle\\
&= \sum\limits_{i} \langle u_{i}|\psi\rangle~|u_{i}\rangle\\
&= \sum\limits_{i} |u_{i}\rangle\langle u_{i}|\psi\rangle \\
&= \left(\sum\limits_{i} |u_{i}\rangle\langle u_{i}|\right)|\psi\rangle 
\end{align*}$$
(podemos fazer este último passo porque em $\langle u_{i}|\psi\rangle|u_{i}\rangle$ temos "constante x ket". Ao reorganizar para $|u_{i}\rangle\langle u_{i}|~|\psi\rangle$ ficamos com "operador x ket", que também é um ket)

- Ora, a única forma de na equação acima termos $|\psi\rangle=|\psi\rangle$ é se:
$$P_{\{u_{i}\}}=\sum\limits_{i}|u_{i}\rangle\langle u_{i}|=\mathbb{1}$$
sendo esta a relação de fecho de uma base discreta.

**Bases contínuas**
- Funciona tudo de forma análoga à base discreta, mas com integrais.
- Um estado $|\psi\rangle$ pode ser representado como uma combinação de elementos da base contínua $\{|w_{\alpha}\rangle\}$:
$$|\psi\rangle=\int d\alpha~c(\alpha)|w_{\alpha}\rangle$$
e podemos determinar a componente do estado num elemento $\alpha$ com a relação:
$$\langle w_\alpha'|\psi\rangle=c(\alpha')$$
(obtido da mesma forma que $\langle u_{i}|\psi\rangle=c_{i}$)

- Com uma dedução idêntica à das bases discretas temos a relação de fecho:
$$P_{\{w_\alpha\}}=\int d\alpha~|w_{\alpha}\rangle\langle w_{\alpha}|=\mathbb{1}$$

**Interpretação geométrica da relação de fecho**
- Vimos atrás que $\sum_{i}|u_{i}\rangle\langle u_{i}|$ projeta um ket no conjunto $\{|u_{i}\rangle\}=|u_{1}\rangle,|u_{2}\rangle,\dots$ que podemos denominar como sendo o subspaço $\mathscr{E}'\subseteq\mathscr{E}$.
- Se este conjunto $\{|u_{i}\rangle\}$ formar uma base em $\mathscr{E}$ então $\mathscr{E}'=\mathscr{E}$.
- Desta forma, faz todo o sentido que o operador que projeta um ket $|\psi\rangle\in\mathscr{E}$ na base $\{u_{i}\}=\mathscr{E}$ seja o operador unitário $\mathbb{1}$.

### Tabela Resumo
![[relação de fecho em bases.png]]

### 2.3.3 - Representação de Kets e Bras
#### 2.3.3.1 - Kets
- Na  base $\{|u_{i}\rangle\}$ o ket $|\psi\rangle$ é representado pelos seus componentes $c_{i}=\langle u_{i}|\psi\rangle$. Assim podemos representá-lo como um vetor vertical:
$$|\psi\rangle=\begin{pmatrix}\langle u_{1}|\psi\rangle\\\langle u_{2}|\psi\rangle\\\vdots\\\langle u_{i}|\psi\rangle\\\vdots\end{pmatrix}$$
- Numa base contínua $\{|w_{\alpha}\rangle\}$ teremos algo parecido mas com um eixo vertical de valores $\alpha$:
![[representação de ket em base continua.png]]

#### 2.3.3.2 - Bras
- Numa base contínua ou discreta, para um bra arbitrário $\langle\varphi|$ podemos escrever:
$$\begin{align*}
discreta:~~ \langle\varphi|&= \langle\varphi|\mathbb{1}=\langle\varphi|P_{\{u_{i}\}}=\sum\limits_{i}\langle \varphi|u_{i}\rangle\langle u_{i}|\\
contínua:~~ \langle\varphi|&= \langle\varphi|\mathbb{1}=\langle\varphi|P_{\{w_{\alpha}\}}=\int d\alpha~\langle \varphi|w_{\alpha}\rangle\langle w_{\alpha}|
\end{align*}$$
em que os componentes de $\langle\varphi|$ nestas bases são os **conjugados complexos dos componentes do ket** associado $|\varphi\rangle$ nessas bases.

- Graças à relação de fecho podemos representar um produto escalar $\langle\varphi|\psi\rangle$ em função das componentes de $|\varphi\rangle:b_{i}=\langle u_{i}|\varphi\rangle/b(\alpha)=\langle w_{\alpha}|\varphi\rangle$,$|\psi\rangle:c_{i}=\langle u_{i}|\psi\rangle/c(\alpha)=\langle w_{\alpha}|\psi\rangle$:
$$\begin{align*}
discreta:~~ \langle \varphi|\psi\rangle&= \langle \varphi|\mathbb{1}|\psi\rangle= \langle\varphi|P_{\{u_{i}\}}|\psi\rangle=\sum\limits_{i} \langle \varphi|u_{i}\rangle\langle u_{i}|\psi\rangle=\sum\limits_{i}b_{i}^{*}c_{i}\\
contínua:~~ \langle \varphi|\psi\rangle&= \langle \varphi|\mathbb{1}|\psi\rangle= \langle\varphi|P_{\{w_{\alpha}\}}|\psi\rangle=\int d\alpha~ \langle \varphi|w_{\alpha}\rangle\langle w_{\alpha}|\psi\rangle=\int d\alpha ~b^{*}(\alpha)c(\alpha)
\end{align*}$$

- Sendo então o produto "ket x bra" um escalar, faz sentido que, se o ket é representado como um vetor vertical, o bra seja representado como um vetor horizontal:
    - Em bases discretas: $$\langle\varphi|=\begin{pmatrix}\langle\varphi|u_{1}\rangle & \langle\varphi|u_{2}\rangle & \dots  & \langle\varphi|u_{i}\rangle & \dots\end{pmatrix}$$
    - Em bases contínuas:
    ![[representação de bra em base contínua.png]]

- De notar aqui que os vetores que descrevem um ket e bra correspondentes são *conjugados hermíticos* (num sentido matricial). Para converter uma matriz destas para o seu conjugado hermítico, transformamos cada elemento no seu conjugado complexo e trocamos as linhas e colunas.

### 2.3.4 - Representação de Operadores
#### 2.3.4.1 - Representação de $A$ com uma matriz quadrada
- Tendo um operador linear $A$ numa base $\{|u_{i}\rangle\}$ podemos associá-lo a um conjunto de escalares complexos na forma:
$$A_{ij}=\langle u_{i}|A|u_{j}\rangle$$
ou para uma base contínua $\{|w_{\alpha}\rangle\}$:
$$A(\alpha,\alpha')=\langle w_{\alpha}|A|w_{\alpha'}\rangle$$
pelo que podemos colocar estes valores numa matriz quadrada $i\times j$ ($i$ é as linhas e $j$ as colunas):
**Discreta**
$$A=\begin{pmatrix}A_{11} & A_{12} & \dots & A_{1j} & \dots \\ A_{21} & A_{22} & \dots &A_{2j} & \dots \\ \vdots  & \vdots & \ddots & \vdots & \cdots \\ A_{i1} & A_{i2} & \dots & A_{ij} & \dots \\ \vdots & \vdots & \vdots & \vdots & \ddots\end{pmatrix}$$
**Contínua**
![[representação de matriz de operador em base contínua.png]]

- Podemos verificar isto ao calcular o produto de 2 operadores $AB$ em termos das componentes:
$$\begin{align*}
\langle u_{i}|AB|u_{j}\rangle=\langle u_{i}|A\mathbb{1}B|u_{j}\rangle&= \langle u_{i}|AP_{\{u_{i}\}}B|u_{j}\rangle=\sum\limits_{k}\langle u_{i}|A|u_{k}\rangle\langle u_{k}|B|u_{j}\rangle
\end{align*}$$
ou seja, é equivalente ao produto de 2 matrizes.

#### 2.3.4.2 - Representam do ket $|\psi'\rangle=A|\psi\rangle$ 
- É natural concluir que este ket será dado pelo produto matricial da matriz $A$ com a matriz de $|\psi\rangle$. Provemos isso:

- Temos um ket $|\psi\rangle$ e um operador $A$, ambos definidos numa base $\{|u_{i}\rangle\}$. Queremos saber como representar o ket $|\psi'\rangle=A|\psi\rangle$. Um elemento de $|\psi'\rangle$ será:
$$c_{i}'=\langle u_{i}|\psi'\rangle=\langle u_{i}|A|\psi\rangle$$
podemos aqui introduzir a relação de fecho:
$$\begin{align*}
c_{i}'&= \langle u_{i}|A\mathbb{1}|\psi\rangle=\langle u_{i}|A P_{\{u_{i}\}}|\psi\rangle\\
&= \sum\limits_{j}\langle u_{i}|A|u_{j}\rangle\langle u_{j}|\psi\rangle\\
&= \sum\limits_{j} A_{ij}c_{j}
\end{align*}$$
o que é então representado como:
$$\begin{pmatrix}c_{1}'\\c_{2}' \\ \vdots \\ c_{i}'  \\ \vdots\\ \vdots \end{pmatrix}= \begin{pmatrix}A_{11} & A_{12} & \dots & A_{1j} & \dots \\ A_{21} & A_{22} & \dots &A_{2j} & \dots \\ \vdots  & \vdots & \ddots & \vdots & \cdots \\ A_{i1} & A_{i2} & \dots & A_{ij} & \dots \\ \vdots & \vdots & \vdots & \vdots & \ddots \\ \vdots & \vdots & \vdots & \vdots &\end{pmatrix}\begin{pmatrix}c_{1} \\ c_{2} \\ \vdots \\ \vdots \\ c_{j} \\ \vdots\end{pmatrix}$$

- Para uma base contínua $\{|w_{\alpha}\rangle\}$ temos:
$$\begin{align*}
c'(\alpha)&= \langle w_{\alpha}|\psi'\rangle=\langle w_{\alpha}|A|\psi\rangle\\
&= \int d\alpha'~\langle w_{\alpha}|A|w_{\alpha'}\rangle\langle w_{\alpha'}|\psi\rangle\\
&= \int d\alpha'~A(\alpha,\alpha')c(\alpha')
\end{align*}$$
- Esta dedução toda é semelhante para o bra $\langle\psi|A$

#### 2.3.4.3 - Expressão do número $\langle \varphi|A|\psi\rangle$
- Na base discreta temos:
$$\begin{align*}
\langle \varphi|A|\psi\rangle&= \langle\varphi|\mathbb{1}A\mathbb{1}|\psi\rangle=\langle\varphi|P_{\{u_{i}\}}AP_{\{u_{j}\}}|\psi\rangle\\
&= \sum\limits_{i,j}\langle\varphi|u_{i}\rangle\langle u_{i}|A|u_{j}\rangle\langle u_{j}|\psi\rangle\\
&= \sum\limits_{i,j}b_{i}^{*}A_{ij}c_{i}
\end{align*}$$
- Na base contínua:
$$\begin{align*}
\langle \varphi|A|\psi\rangle&= \langle\varphi|\mathbb{1}A\mathbb{1}|\psi\rangle=\langle\varphi|P_{\{w_{\alpha}\}}AP_{\{w_{\alpha'}\}}|\psi\rangle\\
&= \iint d\alpha d\alpha'~\langle\varphi|w_{\alpha}\rangle\langle w_{\alpha}|A|w_{\alpha'}\rangle\langle w_{\alpha'}|\psi\rangle\\
&= \iint d\alpha d\alpha'~ b^{*}(\alpha)A(\alpha,\alpha')c(\alpha')
\end{align*}$$

- Em termos matriciais isto tem a forma:
$$\langle\varphi|A|\psi\rangle=\begin{pmatrix}b_{1}^{*} & b_{2}^{*} & \cdots & b_{i} & \cdots & \end{pmatrix}\begin{pmatrix}A_{11} & A_{12} & \dots & A_{1j} & \dots \\ A_{21} & A_{22} & \dots &A_{2j} & \dots \\ \vdots  & \vdots & \ddots & \vdots & \cdots \\ A_{i1} & A_{i2} & \dots & A_{ij} & \dots \\ \vdots & \vdots & \vdots & \vdots & \ddots \\ \vdots & \vdots & \vdots & \vdots &\end{pmatrix}\begin{pmatrix}c_{1} \\ c_{2} \\ \vdots \\ \vdots \\ c_{j} \\ \vdots\end{pmatrix}$$
- A relação $(\langle\varphi|A)|\psi\rangle=\langle\varphi|(A|\psi\rangle)$ apenas expressa a associetividade do produto de 3 matrizes ilustrado acima.

- Utilizando as convenções que agora definimos, podemos verificar que $|\psi\rangle\langle\psi|$ é um operador:
$$|\psi\rangle\langle\psi|=\begin{pmatrix}c_{1} \\ c_{2} \\ \vdots \\ c_i \\ \vdots\end{pmatrix}\begin{pmatrix}c_{1}^{*} & c_{2}^{*} & \cdots & c_{j}^{*} & \cdots\end{pmatrix}=\begin{pmatrix}c_{1}c_{1}^{*} & c_{1}c_{2}^{*} & \dots & c_{1}c_{j}^{*} & \dots \\ c_{2}c_{1}^{*} & c_{2}c_{2}^{*} & \dots & c_{2}c_{j}^{*}  & \dots\\ \vdots & \vdots & \ddots & \vdots  & \cdots \\ c_{i}c_{1}^{*} & c_{i}c_{2}^{*} & \dots & c_{i}c_{j}^{*} & \dots \\ \vdots & \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

#### 2.3.4.4 - Representação matricial de $A^{\dagger}$
- Seguindo as mesmas relações de atrás podemos dizer que:
$$A_{ij}^{\dagger}=\langle u_{i}|A^{\dagger}|u_{j}\rangle=\langle u_{j}|A|u_{i}\rangle^{*}=A_{ji}^{*}$$
ou numa base contínua:
$$A^{\dagger}(\alpha,\alpha')=\langle w_{\alpha}|A^{\dagger}|w_{\alpha'}\rangle=\langle w_{\alpha'}|A|w_{\alpha}\rangle^{*}=A^{*}(\alpha',\alpha)$$

- Tal como previamente referido para o par conjugado hermítico ket/bra, as matrizes de $A$ e $A^{\dagger}$ são conjugados hermíricos. Assim, para passar de uma para a outra, basta tornar todos os elementos no seu conjugado complexo e trocar as linhas e colunas (transpor a matriz).

- Claro, se o operador $A$ for hermítico ficamos com:
$$\begin{align*}
A_{ij}&= A_{ji}^{*}\\
A(\alpha,\alpha')&= A^{*}(\alpha',\alpha)
\end{align*}$$
ou seja, os elementos das matrizes de $A,A^{\dagger}$ que são "simétricos" em relação à diagonal são *conjugados* simétricos ($A_{13}$ é conjugado simétrico de $A_{31}$).
- Por sua vez, isto implica que **os termos da diagonal são REAIS**!

### 2.3.5 - Mudança de representações
#### 2.3.5.1 - Intro
- Estamos numa base qualquer. Um certo ket é representado por uma matriz conhecida. Se mudarmos de base, como irá mudar a matriz que representa esse ket?

- Iremos considerar que estamos a ir de uma base discreta ortonormada $\{|u_{i}\rangle\}$ para outra base discreta ortonormada $\{|t_{k}\rangle\}$. 
- Podemos definir a matriz de mudança de base:
$$S_{ik}=\langle u_{i}|t_{k}\rangle$$
e o seu conjugado hermítico:
$$(S^{\dagger})_{ki}=(S_{ik})^{*}=\langle t_{k}|u_{i}\rangle$$

- Sendo $\{|u_{i}\rangle\},\{|t_{k}\rangle\}$ duas bases completas, terão que seguir a relação de fecho:
$$P_{\{u_{i}\}}=\sum\limits_{i}|u_{i}\rangle\langle u_{i}|=\mathbb{1} \quad \quad;\quad \quad P_{\{t_{k}\}}=\sum\limits_{k}|t_{k}\rangle\langle t_{k}|=\mathbb{1}$$
e a relação de ortonormalização:
$$\langle u_{i}|u_{j}\rangle=\delta_{ij} \quad \quad;\quad \quad \langle t_{k}|t_{l}\rangle=\delta_{kl}$$

- A matriz de transformação $S$ é unitária, ou seja: $$S^{\dagger}S=SS^{\dagger}=I \quad \quad,\quad I\equiv\textsf{matrix identidade}$$
isto é mostrado ao calcular:
$$(S^{\dagger}S)_{kl}=\sum\limits_{i}S_{ki}^{\dagger}S_{il}=\sum\limits_{i}\langle t_{k}|u_{i}\rangle\langle u_{i}|t_{l}\rangle=\langle t_{k}|t_{l}\rangle=\delta_{kl}$$
ou:
$$(SS^{\dagger})_{ij}=\sum\limits_{k}S_{ik}S_{kj}^{\dagger}=\sum\limits_{k}\langle u_{i}|t_{k}\rangle\langle t_{k}|u_{j}\rangle=\langle u_{i}|u_{k}\rangle=\delta_{ij}$$
e provou-se então que $S^{\dagger}S=SS^{\dagger}=I$

> **Nota sobre índices na dedução acima**
> - Temos que $S$  é a função de transformação da base $u$ para a $t$, ou seja, projeta os elementos da base $t$ na base $u$. O conjugado hermítico será o oposto: projeta $u$ em $t$.
> - Por isso, ao introduzir coisas como $S_{ik}$ estamos a projetar $t_{k}$ em $u_{i}$. Ao ter $S_{kj}^{\dagger}$ estamos a projetar $u_{j}$ em $t_{k}$. Ou seja, ao ter $(SS^{\dagger})_{ij}$ estamos a projetar $u_{i}\to t_{k}\to u_{j}$ 
> - Igualmente na primeira dedução: Ao ter $(S^{\dagger}S)_{kl}$ estamos a projetar $t_{k}\to u_{i}\to t_{l}$

#### 2.3.5.2 - Transformação dos componentes de um ket
- Temos o ket $|\psi\rangle$ e conhecemos as componentes  $\langle u_{i}|\psi\rangle$. Queremos saber as componentes do ket na base $\{|t_{k}\rangle\}$, $\langle t_{k}|\psi\rangle$. 
$$\begin{align*}
\langle t_{k}|\psi\rangle&= \langle t_{k}|\mathbb{1}|\psi\rangle=\langle t_{k}|P_{\{u_{i}\}}|\psi\rangle\\
&= \sum\limits_{i}\langle t_{k}|u_{i}\rangle \langle u_{i}|\psi\rangle\\
&= \sum\limits_{i}S^{\dagger}_{ki}\langle u_{i}|\psi\rangle
\end{align*}$$
- Comparando à nota feita acima: temos $S_{ki}^{\dagger}=\langle t_{k}|u_{i}\rangle$, o que equivale à projeção de $|u_{i}\rangle$ no ket $|t_{k}\rangle$. Ora, ao multiplicar isto pela componente $c_{i}=\langle u_{i}|\psi\rangle$ estamos a fazer algo do tipo: $|\psi\rangle$ vale $c_{i}$ na "direção" $|u_{i}\rangle$ e $|u_{i}\rangle$ vale $S_{ki}^{\dagger}$ na "direção" $|t_{k}\rangle$; logo $|\psi\rangle$ vale $S_{ki}^{\dagger}c_{i}$ na "direção" $|t_{k}\rangle$. Depois somamos as contribuições de todas as "direções" os $|u_{i}\rangle$.

- EX: 
    - $|\psi\rangle$ vale 3 em $|u_{i}\rangle$
    - $|u_{i}\rangle$ vale 9 em $|t_{k}\rangle$ (a base $\{|u_{i}\rangle\}$ é ortonormada, portanto $|u_{k}\rangle$ é um vetor unitário. Ou seja, 1 em $|u_{i}\rangle$ vale 9 em $|t_{k}\rangle$)
    - Assim $|\psi\rangle$ valerá $3\times9=27$ em $|t_{k}\rangle$

#### 2.3.5.3 - Transformação dos componentes de um bra
- Usando a mesma lógica no cálculo:
$$\begin{align*}
\langle \psi|t_{k}\rangle&= \langle \psi|\mathbb{1}|t_{k}\rangle=\langle\psi|P_{\{u_{i}\}}|t_{k}\rangle\\
&= \sum\limits_{i}\langle\psi|u_{i}\rangle\langle u_{i}|t_{k}\rangle\\
&= \sum\limits_{i}\langle \psi|u_{i}\rangle S_{ik}
\end{align*}$$
#### 2.3.5.4 - Transformação da matriz de um operador
$$\begin{align*}
A_{kl}=\langle t_{k}|A|t_{l}\rangle&= \langle t_{k}|\mathbb{1}A \mathbb{1}|t_{l}\rangle= \langle t_{k}|P_{\{u_i\}}AP_{\{u_{i}\}}|t_{l}\rangle\\
&= \sum\limits_{i,j}\langle t_{k}|u_{i}\rangle \langle u_{i}|A|u_{j}\rangle \langle u_{j}|t_{l}\rangle\\
&= \sum\limits_{i,j} S_{ki}^{\dagger}A_{ij}S_{jl}
\end{align*}$$
ou, inversamente:
$$\begin{align*}
A_{ij}=\langle u_{i}|A|u_{j}\rangle&= \langle u_{i}|\mathbb{1}A \mathbb{1}|u_{j}\rangle= \langle u_{i}|P_{\{t_{k}\}}AP_{\{y_{k}\}}|u_{j}\rangle\\
&= \sum\limits_{k,l}\langle u_{i}|t_{k}\rangle \langle t_{k}|A|t_{l}\rangle \langle t_{l}|u_{j}\rangle\\
&= \sum\limits_{k,l} S_{ik}A_{kl}S_{lj}^{\dagger}
\end{align*}$$
- Podemos ver que os índices da equação final "anulam-se": $$A_{kl}=S^{\dagger}_{ki}A_{ij}S_{jl}$$
temos os índices: $$kl=k\underbrace{i\cdot i}\underbrace{j\cdot j}l$$
(Eu sei que a notação e linguagem matemática a falar destes índices estão completamente erradas, mas para mim faz sentido)

## 2.4 - Valores Próprios e Observáveis
### 2.4.1 - Valores e Vetores Próprios de operador
- Um ket $|\psi\rangle$ é vetor próprio de um operador linear $A$ se:
$$A|\psi\rangle=\lambda|\psi\rangle \quad \quad, \quad \lambda\in\mathbb{C}$$
em que $\lambda$ será o valor próprio associado ao vetor próprio $|\psi\rangle$
- O conjunto de valores próprios de $A$ é o seu **espetro**.
- Se $|\psi\rangle$ for vetor próprio de $A$ com valor próprio $\lambda$, então $\alpha|\psi\rangle~~(\alpha\in\mathbb{C})$ será também vetor próprio de $A$, com o mesmo valor: $A(\alpha|\psi\rangle)=\alpha A|\psi\rangle=a\lambda|\psi\rangle=\lambda(\alpha|\psi\rangle)$. Em termos físicos, esta ambiguidade não irá afetar os resultados obtidos.

- Um valor próprio $\lambda$ é **não degenerado** se tem 1 único vetor próprio (a menos de multiplicação por uma constante; como vimos acima, $|\psi\rangle, \alpha|\psi\rangle$ têm o mesmo valor próprio).
- Por outro lado, se existirem $n>1$ vetores próprios linearmente independentes com o valor próprio $\lambda$ então ele tem **grau de degenerescência n**. Se um valor próprio $\lambda$ tem grau de degenerescência $g$ temos $g$ kets $|\psi^{i}\rangle$ tais que: $A|\psi^{i}\rangle=\lambda|\psi^{i}\rangle~~(i=1,2,\dots,g)$

- Mas isto quer dizer que podemos definir:
$$|\psi\rangle=\sum\limits_{i=1}^{g}c_{i}|\psi^{i}\rangle$$
e temos:
$$A|\psi\rangle=\sum\limits_{i=1}^{g} c_{i}A|\psi^{i}\rangle=\sum\limits_{i=1 }^{g}c_{i}\lambda |\psi^{i}\rangle=\lambda\sum\limits_{i=1}^{g}c_{i}|\psi^i\rangle=\lambda|\psi\rangle$$
- Ou seja, o conjunto de vetores próprios $\{|\psi^{i}\rangle\}$ associados ao mesmo valor próprio $\lambda$ permitem definir um espaço vetorial com $g$ dimensões, a que chamamos $|\psi\rangle$.
- Isto leva-nos ainda a concluir que dizer que um valor próprio é não degenerado ou com grau de degenerescência 1 é a mesma coisa.

> EXEMPLO
> - Consideremos o operador $P_{\psi}=|\psi\rangle\langle\psi|$: $$P_{\psi}|\varphi\rangle=\lambda|\varphi\rangle \quad \quad\to \quad \quad |\psi\rangle\langle\psi|\varphi\rangle=\lambda|\varphi \rangle$$
> - Ora, intuitivamente vemos que este operador terá apenas 2 valores próprios:
>     - $\lambda=1$ - quando temos o vetor próprio $|\psi\rangle$ 
>     - $\lambda=0$ - quando temos qualquer vetor ortogonal a $|\psi\rangle$
> - Portanto, o espetro de $P_{\psi}$ só tem 2 valores: $1$, que é não degenerado, e $0$ que tem grau de degenerescência infinito.

- Fazendo o conjugado hermítico da equação dos vetores/valores próprios:
$$\langle\psi|A^{\dagger} =\lambda^{*}\langle\psi|$$
ou seja, se $|\psi\rangle$ é um vetor próprio de $A$ com valor próprio $\lambda$, então podemos dizer que $\langle\psi|$ é um bra próprio de $A^{\dagger}$ com valor próprio $\lambda^{*}$. Sem conhecimento mais específico do problema, não podemos fazer conclusões sobre $\langle\psi|A$.

- Se fossemos completamente rigorosos, os únicos kets que aceitariamos como vetores próprios seriam aqueles que pertencem a $\mathscr{E}$ (norma finita). Na realidade, iremos considerar vetores próprios com norma infinita, sendo estes "kets generalizados".

#### 2.4.1.2 - Determinar valores e vetores próprios
- Consideremos um espaço dimensão finita $N$.
- Projetemos a equação dos vetores próprios na base discreta $\{|u_{i}\rangle\}$:
$$\langle u_{i}|A|\psi\rangle=\lambda\langle u_{i}|\psi\rangle$$
podemos fazer o costume:
$$\begin{align*}
\langle u_{i}|A\mathbb{1}|\psi\rangle&= \lambda\langle u_{i}|\psi\rangle\\
\sum\limits_{j}\langle u_{i}|A|u_{j}\rangle \langle u_{j}|\psi\rangle&= \lambda\langle u_{i}|\psi\rangle\\
\sum\limits_{j}A_{ij}~c_{j}&= \lambda~c_{i}\\
\sum\limits_{j}[A_{ij}-\lambda\delta_{ij}]c_{j}&= 0
\end{align*}$$
em que queremos determinar $\lambda,c_{i}$ (de recordar que $|\psi\rangle$ é um ket arbitrário)

**Equação Caraterística**
- A equação que deduzimos acima consiste num sistema de $N$ equações (uma para cada $i$) com $N$ incógnitas $c_{j}$ (uma para cada $j$). Por exemplo, se $N=3$ teríamos o sistema:
$$\begin{cases}
(A_{11}-\lambda)c_{1}+A_{12}c_{2}+A_{13}c_{3}=0 \\
A_{21}c_{1}+(A_{22}-\lambda)c_{2}+A_{23}c_{3}=0 \\
A_{31}c_{1}+A_{32}c_{2}+(A_{33}-\lambda)c_{3}=0
\end{cases}~~\Longrightarrow \begin{pmatrix}A_{11}-\lambda & A_{12} & A_{13} \\ A_{21} & A_{22}-\lambda & A_{23} \\ A_{31} & A_{32} & A_{33}-\lambda\end{pmatrix}\begin{pmatrix}c_{1} \\ c_{2} \\ c_{3}\end{pmatrix}=\begin{pmatrix}0 \\ 0 \\ 0\end{pmatrix}$$
- A solução trivial desse sistema é $c_{j}=0,\forall j$. 
- O sistema *não* tem a solução trivial se:
$$\boxed{\det[\mathscr{A}-\lambda I]=0}$$
em que $\mathscr{A}$ é a matriz $N\times N$ de elementos $A_{ij}$ e $I$ a matriz identidade $N\times N$. Esta é a *Equação Caraterística*.
- A equação acima permite-nos determinar os valores próprios, ao ter a forma:
$$\begin{vmatrix}A_{11}-\lambda & A_{12} & A_{13} & \cdots & A_{1N} \\ A_{21} & A_{22}-\lambda  & A_{23} & \cdots & A_{2N} \\\vdots & \vdots & \vdots & \ddots & \vdots \\ A_{N1} & A_{N2} & A_{N3} & \cdots & A_{NN}-\lambda\end{vmatrix}=0$$
pelo que obtemos um polinómio de grau $N$ em função de $\lambda$ (Polinómio Caraterístico). Os valores próprios serão os zeros.

**Determinação dos Vetores Próprios**
- Seja $\lambda_{0}$ um dos zeros do polinómio caraterístico, temos 2 casos:

*Valor Próprio Não Degenerado*
- Temos o sistema de equações: $\sum\limits_{j}[A_{ij}-\lambda\delta_{ij}]c_{j}= 0$
- Substituimos $\lambda=\lambda_{0}$. 
- Abaixo temos o que acontece no caso em que $N=2$:
$$\begin{cases}(A_{11}-\lambda_{0})c_{1}+A_{12}c_{2}=0 \\A_{21}c_{1}+(A_{22}-\lambda_{0})c_{2}=0 \\\end{cases}\to\begin{cases}------ \\c_{1}=- \frac{A_{22}-\lambda_0}{A_{21}}c_{2}\end{cases}\to \begin{cases}c_{2} =0\\----\end{cases}$$
(Este resultado obtido para $N=2$ irá acontecer para qualquer sistema. Ao reorganizar termos vamos acabar sempre com $c_{j}=0,\forall j$)
- Ou seja, temos na realidade $N-1$ equações independentes. Mas temos $N$ incógnitas. 

- Assim, podemos fixar o valor de 1 das incógnitas. Ficamos então com um sistema de $N-1$ equações e $N-1$ incógnitas.
- Consideremos que se fixou $c_{1}$
- A solução do sistema será: $$c_{j}=\alpha_{j}^{0}c_{1}$$
em que $\alpha_{j}^{0}=1$ para $c_{1}$ obviamente. Para os restantes $c_{j}$ depende da matriz $A_{ij}$ e de $\lambda_{0}$. Por exemplo, no sistema $N=2$ feito acima podemos ter $c_{2}=\alpha_{2}^{0}c_{1}=\frac{\lambda_{0}-A_{11}}{A_{12}}c_{1}$

- Assim, os vetores próprios dependem do $c_{1}$ escolhido. Desta forma temos:
$$|\psi_{0}(c_{1})\rangle=\sum\limits_{j}\alpha_{j}^{0}c_{1}|u_{j}\rangle=c_{1}|\psi_{0}\rangle$$
em que $|\psi_{0}\rangle=\sum_{j}\alpha_{j}|u_{j}\rangle$

*Zero do Polinómio caraterístico que se repete $g$ vezes*
Consideremos agora que $\lambda_{0}$ é um zero do polinómio caraterístico de ordem $g$. Das 2 uma:
1. Ao substituir $\lambda=\lambda_{0}$ no sistema visto atrás, continuamos a ter um sistema de $N-1$ equações independentes. Neste caso, apesar de o zero do polinómio ser repetido apenas temos 1 vetor próprio para este valor próprio. Neste caso não conseguimos diagonalizar $\mathscr{A}$ nem formar uma base do espaço de estados com os vetores próprios (não temos vetores suficientes: se o zero se repete $g$ vezes teremos $N-g$ vetores próprios)
2. Ao substituir $\lambda=\lambda_{0}$ no sistema ficamos com um sistema de $N-p$ equações independentes (em que $p$ será um número $1<p<g$). Este é o caso em que o valor próprio tem grau de degenerescência $p$. Neste caso temos então que a $\lambda_{0}$ corresponde um espaço vetorial de valores próprios de dimensão $p$

- Vejamos melhor o segundo caso. Consideremos $p=2$, ou seja, temos $N-2$ equações independentes para $N$ incógnitas.
- Procedendo de forma semelhante ao que fizemos para $\lambda_{0}$ não degenerado, podemos resolver a "falta" de 2 equações independentes fixando 2 incógnitas $c_{1},c_{2}$. Ficamos portanto com a solução do tipo:
$$c_{j}=\beta_{j}^{0}c_{1}+\gamma_{j}^{0}c_{2}$$
(em que $\beta_{1}^{0}=1,\gamma_{1}^{0}=0,\beta_{2}^{0}=0,\gamma_{2}^{0}=1$ de modo que $c_{1}=c_{1},c_{2}=c_{2}$)
- E podemos definir os vetores próprios na forma:
$$|\psi_{0}(c_{1},c_{2})\rangle=c_{1}|\psi_{0}^{1}\rangle+c_{2}|\psi_{0}^{2}\rangle$$
em que $|\psi_{0}^{1}\rangle=\sum_{j}\beta_{j}^{0}|u_{j}\rangle~,~|\psi_{0}^{2}\rangle=\sum_{j}\gamma_{j}^{0}|u_{j}\rangle$
- Aqui, tal como falado no início desta secção sobre vetores próprios, os vetores $|\psi_{0}(c_{1},c_{2})\rangle$ formam uma base 2D. 
- Não fazer confusão: apesar de dependerem dos parâmetros $c_1,c_2$ os vetores $c_{j}$ não são linearmente dependentes. 
- Além disso, $c_{1},c_{2}$ são quaisquer 2 vetores $\in\mathscr{E_{n}}$ que consigam formar uma base 2D (Ou seja, temos $n$ vetores quaisquer que consigam formar uma base do subespaço $\mathscr{E_{n}}$ de dimensão $n$). Sendo assim, $c_{1},c_{2}$ serão também linearmente independentes.

- Se o operador $A$ for Hermítico, o grau de degenerescência $p$ do valor próprio $\lambda$ é sempre igual à multiplicidade $g$ desse zero do polinómio caraterístico. 
- Para um operador Hermítico num espaço de dimensão finita $N$ temos sempre $N$ vetores próprios linearmente independentes. Ou seja, o 1º caso indicado acima nunca acontece com estes operadores (e portanto quase ou nunca irá aparecer em física quântica).

### 2.4.2 - Observáveis
#### 2.4.2.1 - Propriedades de valores e vetores próprios de operador hermítico
- Temos que $A$ é um operador hermítico.

**1.** - Os valores próprios do operador são REAIS
- Se multiplicarmos os 2 lados da equação dos vetores próprios pelo bra $\langle\psi|$ à esquerda temos:
$$\langle \psi|A|\psi\rangle=\lambda\langle\psi|\psi\rangle$$
em que $\langle\psi|\psi\rangle$ tem que ser real.
- Temos:
$$\langle\psi|A|\psi\rangle^{*}=\langle \psi|A^{\dagger}|\psi\rangle=\langle \psi|A|\psi\rangle$$
pelo que os termos da diagonal da matriz de $A$  são reais.
- Assim, temos que ter $\lambda\in\mathbb{R}$.

- Atrás vimos que ao fazer conjugado hermítico da equação dos vetores próprios obtemos $\langle\psi|A^{\dagger}=\lambda^{*}\langle\psi|$. Sendo $A$ hermítico e $\lambda$ real esta equação torna-se:
$$\langle\psi|A=\lambda\langle\psi|$$
em que podemos dizer que $\langle\psi|$ é um bra próprio de $A$.

**2.** - Vetores próprios associados a valores próprios diferentes são *ortogonais*!
- Consideremos 2 vetores próprios:
$$A|\psi\rangle=\lambda|\psi\rangle  \quad \quad;\quad \quad A|\varphi\rangle=\mu|\varphi\rangle \quad \quad(\lambda\neq\mu )$$
- Por $A$ ser hermítico, podemos escrever:
$$A|\psi\rangle=\lambda|\psi\rangle  \quad \quad;\quad \quad \langle\varphi|A=\langle\varphi|\mu$$
se multiplicarmos a equação de $|\psi\rangle$ por $\langle\varphi|$ à esquerda e a equação de $\langle\varphi|$ por $|\psi\rangle$ à direita:
$$\langle\varphi|A|\psi\rangle=\lambda\langle\varphi|\psi\rangle  \quad \quad;\quad \quad \langle\varphi|A|\psi\rangle=\langle\varphi|\psi\rangle \mu$$
ou seja:
$$\begin{align*}
\lambda\langle\varphi|\psi\rangle&= \mu\langle\varphi|\psi\rangle\\
\langle\varphi|\psi\rangle(\lambda-\mu)&= 0
\end{align*}$$
- Sendo $\lambda\neq\mu$, temos que ter $\langle\varphi|\psi\rangle=0$ AKA os vetores são ortogonais.

#### 2.4.2.2 - Observável
- Se tivermos um espaço de estados $\mathscr{E}$ de dimensão finita e um operador hermítico, podemos sempre formar uma base com os seus vetores próprios.
- Temos um operador linear hermítico $A$. Os seus valores próprios formam um espetro discreto $\{a_{n}\}$. O grau de degenerescência do valor próprio $a_{n}$ será $g_{n}$ ($g_{n}=1$ significa que $a_{n}$ é não degenerado).
- $|\psi_{n}^{i}\rangle~(i=1,2,\dots,g_{n})$ serão os $g_{n}$ vetores linearmente independentes escolhidos e associados a  $a_{n}$, tais que:
$$A|\psi_{n}^{i}\rangle=a_{n}|\psi_{n}^{i}\rangle$$
ora, estes vetores pertencem ao subespaço $\mathscr{E}_{n}$ que está associado a $a_{n}$.

- Mostramos acima que todos os vetores de $\mathscr{E}_{n}$ são ortogonais para todos os vetores de outro subespaço $\mathscr{E}_{n'}$ (associado ao valor próprio $a_n'\neq a_n$). Ou seja:
$$\langle \psi_{n}^{i}|\psi_{n'}^{j}\rangle=0 \quad \quad,\quad n\neq n'~~,~~\forall i,j$$
- Dentro do subespaço $\mathscr{E}_{n}$ podemos escolher vetores $|\psi_{n}^{i}\rangle$ que sejam ortogonais:
$$\langle \psi_{n}|^{i}|\psi_{n}^{j}\rangle=\delta_{ij}$$
- Desta forma temos:
$$\boxed{\langle \psi_{n}^{i}|\psi_{n'}^{i'}\rangle=\delta_{nn'}\delta_{ii'}}$$
e temos portanto um sistema ortonormado de vetores próprios de $A$.
- Por definição, este operador é uma **Observável** se este sistema de vetores forma uma base, ou seja segue a relação de fecho:
$$\boxed{\sum\limits_{n=1}^{\infty}\sum\limits_{i=1}^{g_{n}}|\psi_{n}^{i}\rangle\langle\psi_{n}^{i}|=\mathbb{1}}$$
- Por outras palavras, um operador é um observável se qualquer ket $\in\mathscr{E}$ puder ser representado em função dos vetores próprios do operador. 

**Espetro Parcialmente Contínuo**
- Consideremos agora que temos um operador hermítico cujo espetro tem uma parte contínua $\{a_{n}\}$ com grau de degenerescência $g_{n}$ e uma parte contínua $a(\nu)$ que assumimos que é não degenerado.
- Ora, a equação dos vetores próprios para estas 2 partes do espetro é:
$$A|\psi_{n}^{i}\rangle=a_{n}|\psi_{n}^{i}\rangle \quad \quad;\quad \quad A|\psi_\nu\rangle=a(\nu)|\psi_\nu\rangle$$
e podemos escolher os vetores de forma que formem um sistema ortonormado:
$$\begin{align*}
\langle \psi_{n}^{i}|\psi_{n'}^{i'}\rangle&= \delta_{nn'}\delta_{ii'}\\
\langle\psi_{\nu}|\psi_{\nu'}\rangle&= \delta(\nu-\nu')\\
\langle \psi_{n}^{i}|\psi_\nu\rangle&= 0
\end{align*}$$
e temos a relação de fecho:
$$\sum\limits_{n}\sum\limits_{i=1}^{g_{n}}|\psi_{n}^{i}\rangle\langle\psi_{n}^{i}|+\int_{\nu_{1}}^{\nu_{2}}d\nu~|\psi_{\nu}\rangle\langle\psi_\nu|=\mathbb{1}$$
- Se o operador obdecer a estas relações será um observável.

### 2.4.3 - CCOC
#### 2.4.3.1 - Teoremas
**Teorema 1**
- Se 2 operadores $A,B$ comutam e $\ket{\psi}$ é um vetor próprio de $A$ então $B\ket{\psi}$ é vetor próprio de $A$, com o mesmo valor próprio.

- Sendo $\ket{\psi}$ um vetor próprio de $A$ então temos $A\ket{\psi}=a\ket{\psi}$.
- Ao aplicar $B$ aos 2 lados fica: $BA\ket{\psi}=aB\ket{\psi}$
- Se $A$ e $B$ comutam podemos reescreever a equação anterior como $A(B\ket{\psi})=a(B\ket{\psi})$ e verfiica-se o teorema 1.

- De notar que se o valor próprio $a$ for degenerado, apenas podemos dizer que $B\ket{\psi}$ pertence ao subespaço dos vetores $\ket{\psi}$, $\mathscr{E}_{a}$. Isto significa ainda que o subespaço $\mathscr{E}_{a}$ é invariante para ação de $B$. Isto pode ser generalizdo:
*Teorema 1 (outra versão)* - se $A,B$ comutam, então todos os subespaços de $A$ são inveriantes perante ação de $B$.

**Teorema 2**
- Se 2 observáveis $A,B$ comutam e $\ket{\psi_{1}},\ket{\psi_{2}}$ são vetores próprios de $A$ com valores próprios diferentes, então o elemento da matriz de $B$ $\langle \psi_{1}|B|\psi_{2}\rangle$ é nulo.

- Temos 2 vetores próprios de $A$: $A\ket{\psi_{1}}=a_{1}\ket{\psi_{1}}~,~A\ket{\psi_{2}}=a_{2}\ket{\psi_{2}}$.
- Pelo teorema 1, os vetores $B\ket{\psi_{1}},B\ket{\psi_{2}}$ são vetores próprios de $A$ com valores $a_{1},a_{2}$.
- Temos ainda que isto implica que $B\ket{\psi_{1}}$ é ortogonal a $\ket{\psi_{1}}$, ou seja: $\langle \psi_{1}|B|\psi_{2}\rangle=0$, tendo-se provado o teorema.

**Teorema 3**
- Se 2 Observáveis $A,B$ comutam, então podemos formar uma base ortonormada do espaço de estados com vetores próprios comuns a $A$ e $B$.

- Consideremos duas observáveis $A,B$ que (para simplificar) têm espetros completamente contínuos. 
- Em $A$ teremos uma base de vetores próprios $\ket{u_{n}^{i}}$ definidos por $A\ket{u_{n}^{i}}=a_{n}\ket{u_{n}^{i}}~,~n=1,2,\dots~,~i=1,2,\dots,g_{n}$. Temos que $g_{n}$ é o grau de degenerescência do valor próprio $a_{n}$. $g_{n}$ irá também correspondender às dimensões do subespaço $\mathscr{E}_{n}$
- Temos que $\langle u_{n}^{i}|u_{n'}^{i'}\rangle=\delta_{nn'}\delta_{ii'}$ (relação de ortonormalização e fecho)
- E temos agora a pergunta: como é que é a matriz que representa $B$ na base $\{\ket{u_{n}^{i}}\}$?
    - Atrás já vimos que o elemento $\langle u_{n}^{i}|B|u_{n'}^{i'}\rangle$ é nulo se $n\neq n'$ ---> Os elementos fora da diagonal são nulos.
    - Se escrevermos os elementos da base por extenso: $\ket{u_{1}^{1}},\ket{u_{1}^{2}},\dots,\ket{u_{1}^{g_{1}}}; \ket{u_{2}^{1}},\dots,\ket{u_{2}^{g_{2}}};\dots$ vemos que existem BLOCOS - grupos de elementos que têm o mesmo $n$ mas com degenerescências distintas.
- Assim a matriz de $B$ será diagonal com blocos:
![[matriz ccoc.png]]

- Para os blocos, temos 2 casos:
    1. O autovalor $a_{n}$ é não degenerado. Neste caso só tem 1 vetor próprio, $\ket{u_{n}}$, e temos $g_{n}=1$. Isto significa que o subespaço correspondente $\mathscr{E}_{n}$ tem dimensão 1! Na matriz de $B$ isto significa que o "bloco" só tem 1 elemento (matriz 1x1). Isto mostra que, de facto, $\ket{u_{n}}$ será vetor próprio de $A$ **E** $B$. Para estes o teorema já está correto.
    2. O autovalor $a_{n}$ é degenerado, com grau $g_{n}>1$. O bloco terá dimensões $g_{n}\times g_{n}$. Ora, este bloco geralmente *não* é diagonal, pelo que os vetores $\ket{u_{n}^{i}}$ **não** sao vetores próprios de $B$. Falta arranjar uma "solução" para este caso.

- Tendo a matriz de $A$ um valor próprio $a_{n}$ com grau de degenerescência $g_{n}$, os vetores associados a esse valor geram um subespaço $\mathscr{E_{n}}$ de dimensão $n$.
- Consideremos que existe uma base $\{\ket{u^{i}_{n}}\}\in\mathscr{E_{n}}$ em que podemos representar $B$. A matriz que representa o operador nessa base terá elementos $\beta_{ij}^{(n)}=\langle u_{n}^{i}|B|u_{n}^{j}\rangle$.
- Sendo $B$ uma observável, este operador é hermítico e a matriz $\beta_{ij}$ também o será. Desta forma, ela será diagonalizável. Ou seja, deveremos conseguir diagonalizá-la e definir uma nova base $\{\ket{v_{n}^{i}}\}\in\mathscr{E_{n}}$. 
- Assim, com $B$ representado nesta base, a matriz passa a ter a forma: $\langle v_{n}^{i}|B|v_{n}^{j}\rangle=\beta_{i}^{(n)}\delta_{ij}$ (tal como dito acima, esta base é obtida ao diagonalizar a matriz que representa $B$ na base $|u_{i}\rangle$)
- Ou seja, os elementos da base $\{\ket{v_{n}^{i}}\}$ são *vetores próprios* de $B$: $B\ket{v_{n}^{i}}=\beta_{i}^{(n)}\ket{v_{n}^{i}}$
- Pertencendo estes vetores ao subespaço $\mathscr{E_{n}}$, por definição, eles são vetores próprios de $A$ também, com valor próprio $a_{n}$.
- Esta sequência de eventos pode ser repetida para cada subespaço criado por cada valor próprio degenerado de $A$. 
- No final, ficamos com uma base $\mathscr{E}$ composta de vetores próprios $\ket{v_{n}^{i}}$ comuns a $A$ e $B$; tendo-se provado o teorema.

*Inverso do Teorema*
- Se existe uma base de vetores próprios comuns a duas observáveis $A,B$, então elas comutam.

- Com a informação que temos é fácil escrever:
$$\begin{align*}
AB\ket{u_{n,p}^{i}}=b_{p}A\ket{u_{n,p}^{i}}=b_{p}a_{n}\ket{u_{n,p}^{i}}\\
BA\ket{u_{n,p}^{i}}=a_{n}B\ket{u_{n,p}^{i}}=a_{n}b_{p}\ket{u_{n,p}^{i}}
\end{align*}$$
se subtrairmos as equações: $$[A,B]\ket{u_{n,p}^{i}}=0$$
ou seja, os operadores comutam!

**Notação**
- Iremos representar vetores próprios comuns a $A,B$ com $\ket{u_{n,p}^{i}}$:
$$A\ket{u_{n,p}^{i}}=a_{n}\ket{u_{n,p}^{i}} \quad \quad;\quad \quad B\ket{u_{n,p}^{i}}=b_{p}\ket{u_{n,p}^{i}}$$
em que $i$ indica a degenerescência e $n,b$ indica a qual valor próprio de cada operador o vetor associado.

**Aplicação**
- Por vezes iremos reorganizar um problema de forma a ter: $C=A+B$ sendo $A,B,C$ 3 observáveis, tais que $[A,B]=0$. Isto porque se conhecermos a base de vetores próprios comuns de $A$ e $B$, então torna-se fácil analisar $C$. Por exemplo, um vetor própio de $A,B$ $\ket{u_{n,p}^{i}}$ será também vetor próprio de $C$, com valor próprio $a_{n}+b_{p}$.Isto será o caso para todos os vetores da base.

#### 2.4.3.2 - Conjuntos Completos de Observáveis que Comutam (CCOC)
- Temos uma observável $A$ e a base de $\mathscr{E}$ composta pelos seus vetores próprios $\ket{u_{n}^{i}}$.
- Se nenhum valor próprio de $A$ for degenerado, podemos associar a cada vetor próprio um valor próprio $a_{n}$. Ou seja, o índice $i$ é inútil e todos os subespaços $\mathscr{E_{n}}$ têm dimensão 1.
- Ou seja, só existe **1 base** de $\mathscr{E}$ definida por vetor próprios de $A$. Temos então que a observável $A$ (sozinha) forma um CCOC.

- Consideremos agora o cenário em que 1+ valores próprios de $A$ são degenerados. Neste caso, para um certo autovalor $a_{n}$ temos vários vetores que formam o subespaço $\mathscr{E_{n}}$.
- Ou seja, a base dos vetores próprios de $A$ **não** é única. Para cada autovalor degenerado $a_{n}$ podemos definir qualquer base dentro do seu subespaço $\mathscr{E_{n}}$ para o definir.

- Consideremos agora que temos outra observável $B$ que comuta com $A$.
- Vamos construir uma base ortonormada de vetores próprios comuns a $A,B$. Ora, $A,B$ formam um CCOC se e só se a base de vetores comum for única!
    - Isto significa que para cada par de valor próprios $\{a_{n},b_{p}\}$ só pode existir 1 vetor próprio da base.
    - Acima, para demonstrar o *teorema 3*, resolvemos a equação dos vetores próprios para $B$: $B\ket{v_{n}^{i}}=\beta_{i}^{(n)}\ket{v_{n}^{i}}$ dentro de cada subespaço $\mathscr{E_{n}}$ (associados a autovalores degenerados de $A$). Ora, para que $A,B$ constituam um CCOC é preciso que todos os autovalores $\beta_{i}$ de $B$ neste subespaço sejam *diferentes*. 
        - Acima, quanto tínhamos $A$ com um valor $a_{n}$ degenerado, $A$ não constituia um CCOC porque dentro do subespaço  $\mathscr{E_{n}}$ podemos definir qualquer base. Sendo $B$ definido no subespaço $\mathscr{E_{n}}$ por $n$ autovalores diferentes, então quer dizer que existe apenas 1 conjunto de $n$ vetores $\in\mathscr{E_{n}}$ que forma uma base e que são vetores próprios de $A$ e $B$.
- Desta forma, se para pelo menos 1 dos pares $\{a_{n},b_{n}\}$ existirem vários vetores próprios de $A,B$ então estes operadores não formam um CCOC.

- As conclusões aqui feitas podem ser generalizadas para 3+ Observáveis que formem um CCOC. De forma geral: "Um conjunto de Observáveis $A,B,C\dots$ forma um CCOC se existem uma única base ortonormada de vetores próprios comuns a estes operadores".
- Se $A,B$ formam um CCOC, um conjunto constituido por $A,B,C$ (em que $C$ comuta com $A,B$) também será um CCOC.

## 2.5 - Exemplos - $\ket{\vec{r}},\ket{\vec{p}}$
- Exemplos muito bem explicados no Cohen (Secção 2.E). Não acho que valha a pena eu escrever algo sobre isto. O livro está ótimo e achei bastante intuitivo. 
- Em regra geral o truque é: espetar a relação de fecho no meio de um produto escalar.