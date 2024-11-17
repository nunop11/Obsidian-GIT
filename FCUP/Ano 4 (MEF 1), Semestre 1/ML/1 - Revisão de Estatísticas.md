# Probabilidade
## Definição
- Podemos definir probabilidade de forma *axiomática*. Vejamos então uma definição que fortemente relaciona as teorias de proobabilidade e de conjuntos:
    1. A probabilidade de um evento $A$ é não negativa: $P(A)\ge0$
    2. A probabilidade de um efeito que ocorre garantidamente é 1: $P(C)=1$
    3. Se 2 eventos, $A$ e $B$, são exclusivos (ou ocorre um ou outro, nunca os dois) então a probablidade de um deles acontecer (escrito como $A\cup B$) é: $P(A\cup B)=P(A)+P(B)$
- Estes 3 axiomas são suficientes para desenvolver a teoria.

## VA discretas
- Uma VA $\text{x}$ é discreta se o conjunto de valores que pode tomar $\mathcal{X}$ for finito ou infinito e contável.
- A probabilidade de acontecer o evento $\text{x}=x$ é escrita como $P(\text{x}=x)\equiv P(x)$

- Assumindo que 2 valores não podem ocorrer em simultâneo temos $$\sum\limits_{x\in\mathcal{X}}P(x)=1$$
- Vamos escrever a *interseção* de 2 probablidades como $$P(A,B)\quad \quad \quad\left[~\equiv P(A\cap B)\right]$$

**2 Variáveis**
- Se tivermos 2 VA $\text{x}\in\mathcal{X},\text{y}\in\mathcal{Y}$, temos a regra:
$$P(x)=\sum\limits_{\text{y}\in\mathcal{Y}} P(x,y)$$

**Probabilidade Condicionada**
- Definida como:
$$P(A|B):= \frac{P(A,B)}{P(B)}$$

- Se 2 variáveis forem *independentes* temos:
$$P(A,B)=P(A)P(B)$$

- O **teorema de Bayes** diz-nos que:
$$P(x|y)=\frac{P(y|x)P(x)}{P(y)} \quad;\quad P(y|x)=\frac{P(x|y)P(y)}{P(x)}$$

    - Do ponto de vista de ML, isto pode ser visto como: "a incerteza de $y$ respetiva a um output $x$ será representada como $P(y|x)$. Podemos escrever esta incerteza ao contrário: em função da probabilidade $P(x|y)$ e as probabilidades de $x,y$"

## VA contínuas
- Uma VA $\text{x}$ é contínuas se pode tomar infinitos valores em qualquer intervalo do conjunto de números reais $\mathbb{R}$.

- Temos a CDF - *função de distribuição acumulada*, definida como: $$F_{\text{x}}(x):=P(\text{x}\le x)$$
(ou seja, é a probabilidade de acontecer o evento discreto "$\text{x}$ é menor ou igual a $x$")

- Da definição acima é evidente que: $P(x_{1}<\text{x}\le x_{2})=F_{\text{x}}(x_{2}) - F_{\text{x}}(x_{1})$
- Ora, se $F$ for derivável, teremos a *função de densidade de probabilidade* - PDF: $$p_{\text{x}}(x):= \frac{dF_{\text{x}}(x)}{dx} \quad; \quad P(x_{1}<\text{x}\le x_{2})=\int_{x_{1}}^{x_{2}}p_{\text{x}}(x)dx$$
e, claro:
$$F_{\text{x}}(x)=\int_{-\infty}^{x}p_{\text{x}}(z)dz$$

*Probabilidade total*
$$\int_{-\infty}^{+\infty}p_{\text{x}}(x)dx=1$$

*Probabilidade condicionada*
$$p(x|y)=\frac{p(x,y)}{p(y)}$$
*Propriedade de 2 variáveis*
$$p_{\text{x}}(x)=\int_{-\infty}^{+\infty}p(x,y)dy$$

## Média, Var e Cov
- A *média* de uma VA contínua é:
$$\mathbb{E}[\text{x}]:=\int_{-\infty}^{+\infty}xp(x)dx$$
- A *variância* de uma VA contínua é:
$$\sigma_{x}^{2}:=\int_{-\infty}^{+\infty} (x-\mathbb{E}[\text{x}])^{2}p(x)dx$$
(para VAs discretas, trocamos integrais por somatório)

*Duas variáveis*
- A média de 2 VA é: $$\mathbb{E}[\text{x},\text{y}]=\mathbb{E}_{\text{x}}[\mathbb{E}_\text{y|x} [f(\text{x},\text{y})]]$$
- Tendo 2 VA, a sua *covariância* será:
$$\text{cov}(\text{x},\text{y}):=\mathbb{E}[(\text{x}-\mathbb{E}[\text{x}])(\text{y}-\mathbb{E}[\text{y}])]$$
e a sua *correlação* é:
$$r_{x,y}:= \mathbb{E}[\text{xy}]=\text{cov}(\text{x},\text{y})-\mathbb{E}[\text{x}]\mathbb{E}[\text{y}]$$


## VeA - Vetor Aleatório
- Um VeA é um conjunto de VAs: $\mathbf{x}=[\text{x}_{1},\text{x}_{2},\dots,\text{x}_{l}]^{T}$. A sua PDF:
$$p(\boldsymbol{x})=p(x_{1},x_{2},\dots,x_{l})~~~~~~,~~~~ \boldsymbol{x}=[x_{1},x_{2},\dots,x_{l}]^{T}$$

- A **matriz de covariância** do VeA é:
$$\text{cov}(\mathbf{x}):= \mathbb{E}[(\mathbf{x}-\mathbb{E}[\mathbf{x}])(\mathbf{x}-\mathbb{E}[\mathbf{x}])^{T}]$$
tendo-se:
$$\text{cov}(\mathbf{x})=\begin{pmatrix}\text{cov}(\text{x}_{1},\text{x}_{1}) & \cdots & \text{cov}(\text{x}_{1},\text{x}_{l}) \\ \vdots & \ddots & \vdots \\ \text{cov}(\text{x}_{l},\text{x}_{1}) & \cdots & \text{cov}(\text{x}_{l},\text{x}_{l})\end{pmatrix}$$

- A **matriz de correlação** é dada por
$$R_{x}:=\mathbb{E}[\mathbf{xx}^{T}]=\begin{pmatrix}\mathbb{E}[\text{x}_{1},\text{x}_{1}] & \cdots & \mathbb{E}[\text{x}_{1},\text{x}_{l}] \\ \vdots & \ddots & \vdots \\ \mathbb{E}[\text{x}_{l},\text{x}_{1}] & \cdots & \mathbb{E}[\text{x}_{l},\text{x}_{l}]\end{pmatrix}=\text{cov}(\mathbf{x})+\mathbb{E}[\mathbf{x}]\mathbb{E}[\mathbf{x}^{T}]$$

- As matrizes $\text{cov}$ e $R_{x}$ são **positive semidefinite**, ou seja:
$$\mathbf{y}^{T}R_{x}\mathbf{y}\ge0~~~~,~~\forall~\mathbf{y}\in\mathbb{R}^{l}$$
$$\mathbf{y}^{T}\text{cov}(\mathbf{x})\mathbf{y}\ge0~~~~,~~\forall~\mathbf{y}\in\mathbb{R}^{l}$$

## VA complexa
- Podemos ter uma VA complexa: $$\text{z}:=\text{x}+j \text{y}$$
em que a PDF de $\text{z}$ será a *junção* das PDFs de $\text{x},\text{y}$:
$$p(x):= p(x,y)$$

# Distribuições Discretas
## Bernoulli
- A VA é binária e consiste em $\mathcal{X}=\{0,1\}$. Definimos então:
$$P(\text{x}=1)=p~~,~~P(\text{x}=0)=1-p$$
- Isto frequentemente é associado a experiências do tipo: "lançamos uma moeda. Cara é 1, coroa é 0".
- Temos então a PDF:
$$\begin{align*}
\text{x}&\sim\text{Bern}(x|p)\\
P(x)&= \text{Bern}(x;p):=p^{x}(1-p)^{1-x}
\end{align*}$$
- Temos a média:
$$\mathbb{E}[\text{x}]=\sum\limits xP(x)=1p + 0(1-p)=p$$
e a variância:
$$\sigma_{x}^{2}=\sum\limits(x-\mathbb{E}[\text{x}])^{2}P(x)=(1-p)^{2}p + p^{2}(1-p)=p(1-p)$$

## Binomial
- Escrevemos uma VA que segue esta distribuição como:
$$\text{x}\sim \text{Bin}(x|n,p)$$
em que 
$$P(\text{x}=k):=\text{Bin}(k|n,p)=\begin{pmatrix}n \\ k\end{pmatrix}p^{k}(1-p)^{n-k} ~~~~;~~~~k=0,1,\dots,n$$
e temos, então, $\mathcal{X}=\{0,1,\dots,n\}$

- De um ponto de vista mais concreto, esta distribuição representa a quantidade de vezes que sai "cara" (=1) ocorre em $n$ lançamentos de uma moeda. Ou seja, consiste em repetir $n$ vezes uma experiência de Bernoulli.
    - Assim, podemos ver a distribuição de Bernoulli como um caso particular de distribuição Binomial, em que $n=1$.

- Temos a média
$$\mathbb{E}[\text{x}]=np$$
e a variância
$$\sigma_{x}^{2}=np(1-p)$$

- A PDF e CDF têm a seguinte forma:
![[cdf e pdf.png]]

## Multinomial
- Generalização da distribuição binomial. Consiste no caso em que o output de cada experiência _não_ é binário. Temos então $K$ possibilidades em cada experiência.
    - Enquanto que podemos comparar a distribuição binomial a lançar uma moeda várias vezes, a distribuição multinomial será comparável a lançar um dado várias vezes, tendo-se $K=6$

- Tendo cada um dos K outcomes probabilidade $P_{1},P_{2},\dots P_{K}$ então temos:
$$\mathbf{P}=[P_{1},P_{2},\dots,P_{K}]^{T}$$
- Após $n$ experiências, consideremos $x_{i}$ o número de vezes que o outcome $i$ aconteceu. Temos então o VeA:
$$\mathbf{x}=[\text{x}_{1},\text{x}_{2},\dots,\text{x}_{K}]^{T}$$
teremos então que este VeA segue a distribuição multinomial:
$$\mathbf{x}\sim\text{Mult}(\boldsymbol{x}|n,\mathbf{P}):= \begin{pmatrix}n\\ x_{1},x_{2},\dots,x_{K}\end{pmatrix}\prod_{i=1}^{K}P_{k}^{x_{k}}$$
em que temos: $\sum_{k=1}^{K}x_{k}=n~,~\sum_{k=1}^{K}P_{k}=1$

# Distribuições Contínuas
## Uniforme
- Tendo uma VA $\text{x}$ contínua num intervalo $[a,b]$, se ela tem distribuição uniforme escrevemos $\text{x}\sim\mathcal{U}(a,b)$ em que $a>-\infty~,~b<+\infty$ e temos:
$$p(x)=\begin{cases}
\frac{1}{b-a} & , & a\le x\le b \\
0 & , & \text{resto}
\end{cases}$$
- A média e variância são:
$$\mathbb{E}[\text{x}]=\frac{a+b}{2} ~~~~,~~~~ \sigma_{x}^{2}=\frac{1}{12}(b-a)^{2}$$
- Ora, notemos uma coisa. Se $b-a<1$, teremos *densidade* de probabilidade acima de 1 no intervalo $[a,b]$. Isto pode parecer estranho, mas a limitação que temos num sistema de probabilidades é:
$\int_{-\infty}^{+\infty}p(x)dx=1$

## Gaussiana / Normal
- Temos uma VA $\text{x}$. Ela tem distribuição normal com média $\mu$ e variância $\sigma^{2}$, o que representamos com
$$\text{x}\sim \mathcal{N}(\mu,\sigma^{2})$$ e temos
$$p(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp \left(- \frac{(x-\mu)^{2}}{2\sigma^{2}} \right)$$
e temos, claro
$$\mathbb{E}[\text{x}]=\mu \quad;\quad \sigma_{x}^{2}=\sigma^{2}$$

### Gaussiana multivariável
- Generalização da distribuição gaussiana para um VeA $\mathbf{x}\in\mathbb{R}^{l}$. Dizemos: $$\mathbf{x}\sim\mathcal{N}(\mathbf{x}|\boldsymbol{\mu},\Sigma)$$
e temos
$$p(\boldsymbol{x})=\frac{1}{(2\pi)^{l/2} |\Sigma|^{1/2}}\exp\left(-\frac12 (\boldsymbol{x}-\boldsymbol{\mu})^{T}\Sigma^{-1}(\boldsymbol{x}-\boldsymbol{\mu})\right)$$
($|\Sigma|$ é o determinante da matriz)
em que, claro:
$$\mathbb{E}[\mathbf{x}]=\boldsymbol{\mu}~~~~~,~~~~ \text{cov}(\mathbf{x})=\Sigma$$

**Isovalue curves**
- Numa gaussiana podemos definir curvas em que temos:
$$(\boldsymbol{x}-\boldsymbol{\mu})^{T}\Sigma^{-1} (\boldsymbol{x}-\boldsymbol{\mu})=\text{constante}=c$$
![[Attachments/FCUP/A4S1/ML/gaussiana 2d.png]]
- No PPT há uma demonstração de porquê que as isovalue lines são elipses/elipsoides.

### Propriedades de Dist Gaussiana
- Se a matriz de covariância, $\Sigma$, for diagonal, então temos que $\text{cov}(\text{x}_{i},\text{x}_{j})=0~~,~i\neq j$. Isto é geral. No caso concreto de uma distribuição gaussiana isto significa que *as variáveis são independentes*! Ou seja: $p(\boldsymbol{x})=\prod_{i=1}^{l}p(x_{i})$

#### Teorema do Limite Central
- Temos $N$ VAs independentes, cada uma com uma distribuição diferente com média $\mu_{i}$ e variância $\sigma_{i}^{2}$. Se definirmos uma nova VA: $$\text{x}=\sum\limits_{i=1}^{N}\text{x}_{i}$$
então teremos
$$\mu=\sum\limits_{i=1}^{N}\mu_{i} \quad;\quad \sigma_{x}^{2}=\sum\limits_{i=1}^{N}\sigma_{i}^{2}$$
- Ora, se $N\to\infty$ então podemos fazer a mudança de variável:
$$z=\frac{x-\mu}{\sigma}$$
e temos que: $$\text{z}\sim \mathcal{N}(z|0,1)$$
sendo esta a **distribuição normal padrão**.

- Na realidade, pode chegar $N=5-10$ e a combinação das variáveis já atinge uma boa aproximação da distribuição normal padrão.
