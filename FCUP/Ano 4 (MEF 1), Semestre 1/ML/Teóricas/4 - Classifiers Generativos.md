## Features e Classifiers
- Consideremos uma observação $\mathbf{x}$ com $P$ fetaures. Podemos definir $\mathbf{x}$ como um *feature vector*:
$$\mathbf{x}=\begin{pmatrix}x_{1} \\ x_{2} \\ \vdots \\ x_{P}\end{pmatrix}$$
podemos ainda definir o *espaço de features*: $\mathbb{R}^{P}$ que contem todos os vetores de features possíveis.

- Um **classifier**/Classificador mapeia um vetor de features para 1 de $K$ *classes*:
$$\mathbf{x}\to \mathcal{C}_{i}\in \{\mathcal{C}_{1},\mathcal{C}_{2},\dots,\mathcal{C}_{K}\}$$
ou seja, um classificador divide o espaço de features em K partes:
$$f(\mathbf{x})=\begin{cases}
\mathcal{C}_{1} & ; & \mathbf{x}\in R_{1} \\
\mathcal{C}_{2} & ; & \mathbf{x}\in R_{2} \\
\vdots \\
\mathcal{C}_{K} & ; & \mathbf{x}\in R_K 
\end{cases}$$

## Teoria de decisão de Bayes
- Teoria que decide em que categoria fica cada ponto usando probabilidades para equilibrar tradeoffs 
- Um exemplo muito simples:
    - Consideremos $\mathcal{C}$ uma VA "tipo de peixe". Em que $\mathcal{C}=\mathcal{C}_{1}$ para truta e $\mathcal{C}=\mathcal{C}_{2}$ para salmão. Para os restantes casos, temos $P(\mathcal{C}_{1}),P(\mathcal{C}_{2})$ as propabilidades **a priori** de o próximo peixe ser truta ou salmão, respetivamente

### Probabilidades A Priori
- Refletem o nosso conhecimento sobre o sistema em estudo e sobre cada uma das classes.
    - As probabilidades podem refletir coisas como zona de pesca, altura do ano, composição da água, etc, etc
- No caso acima, se não houver mais nenhum tipo de peixe no local onde estamos então teremos
$$P(\mathcal{C}_{1})+P(\mathcal{C}_{2})=1$$
num caso genérico teremos $\sum_{i}P(\mathcal{C}_{i})=1$

**Fazer decisão com isto**
- Podemos simplesmente fazer:
$$\mathcal{C}=\begin{cases}
\mathcal{C}_{1} & ; & P(\mathcal{C}_{1})>P(\mathcal{C}_{2}) \\
\mathcal{C}_{2} & ; & \text{restantes casos}
\end{cases}$$
e a probabilidade de atribuirmos a categoria de forma errada será $$P(\text{erro})=\min\{P(\mathcal{C}_{1}), P(\mathcal{C}_{2})\}$$
bastante alto ngl

#### Probabilidades dependentes de classe
- Vamos melhorar o processo de decisão
- Consideremos $x$ uma VA que carateriza a lightness (em cor) do peixe. 
- Assim, as probabilidades condicionadas $P(x|\mathcal{C}_{1}),P(x|\mathcal{C}_{2})$ permitem-nos ter em conta a cor do peixe apanhado:
![[prior prob.png|450]]

### Probabilidades A Posteriori
- Consideremos que sabemos $P(\mathcal{C}_{j}),P(x|\mathcal{C}_{j})$. 
- Medimos $x$ para um peixe
- Definimos então $P(\mathcal{C}_{j}|x)$ como a *probabilidade a posteriori* (obtido depois de medição, como o nome indica)
- Assim, usamos o teorema de *Bayes*:
$$P(\mathcal{C}_{j}|x)=\frac{P(x|\mathcal{C}_{j})P(\mathcal{C}_{j})}{P(x)}$$
em que $P(x)=P(x|\mathcal{C}_{1})P(\mathcal{C}_{1})+P(x|\mathcal{C}_{2})P(\mathcal{C}_{2})$

**Fazer decisão, segunda tentativa**
- Chamamos:
    - *Likelihood* - $P(x|\mathcal{C}_{j})$
    - *Evidence* - $P(x)$

- Podemos então decidir com:
$$\mathcal{C}=\begin{cases}
\mathcal{C}_{1} & ; & P(\mathcal{C}_{1}|x)>P(\mathcal{C}_{2}|x) \\
\mathcal{C}_{2} & ; & \text{restantes casos}
\end{cases}=\begin{cases}
\mathcal{C}_{1} & ; & \frac{P(x|\mathcal{C}_{1})}{P(x|\mathcal{C}_{2})}>\frac{P(\mathcal{C}_{2})}{P(\mathcal{C}_{1})} \\
\mathcal{C}_{2} & ; & \text{restantes casos}
\end{cases}$$

com isto, podemos determinar os limiares de decisão (thresholds) ótimos para 2 casos de priors diferentes:
![[limiar decisao ideal.png]]
no segundo caso o limiar desliza para a direita porque C1 tem mair probabilidade a priori.

- A **probabilidade de erro** agora é
$$P(\text{erro}|x)=\begin{cases}
P(\mathcal{C}_{1}|x) & ; & \mathcal{C}_{2} \\
P(\mathcal{C}_{2}|x) & ; & \mathcal{C}_{1}
\end{cases}$$
mas podemos calcular a probabilidade de erro média:
$$p(\text{erro})=\int P(\text{erro}|x)P(x)dx$$

![[limiar ideal bayes e erro.png]]
podemos ver neste gráfico que em $x_{B}$ temos o ponto ótimo, em que se minimiza a áre total debaixo das curvas - minimizasse a probabilidade de erro de decisão.

### Confusion Matrix
- Podemos definir uma confusion matrix como
![[exemplo tabela de confusao.png]]

## Bayes mais geral
- O que vimos funciona bem. Mas é muito restrito.
- Queremos generalizar.
- Para termos:
    - mais de 1 feature - precisamos de substituir $x$ por um vetor $\mathbf{x}$
    - mais de 2 categorias possíveis - alterar notação
    - permitir ações além de decisões - permitir rejeitar uma opção
    - considerar a hipotese de um erro ter consequências - definir quão custosa cada ação é

### Classificação de rate de erro mínimo
- Temos as classes/categorias $\{\mathcal{C}_{1},\dots,\mathcal{C}_{K}\}$
- temos o vetor $\mathbf{x}$ com D componentes - vetor de features
- Se todos os erros tiverem o mesmo custo, a regra de decisão para erro mínimo é: $$\mathcal{C}_{1} \text{ if } P(\mathcal{C}_{i}|x)>P(\mathcal{C}_{j}|x)~~\forall j\neq i$$
e o erro que fica é o *erro de Bayes*. Melhor performance teoricamente possível.

## Agora na vida real - Estimar probabilidades
- A teoria de Bayes assume que conhecemos as probabilidades. Assim, como podemos saber/estimar $p(\mathbf{x}|\mathcal{C}_{j})$??
- Temos então uma série de modelos para isto:
    - parametricos - assumir forma da densidade de probabilidade
        - modelos de densidade
        - modelos de mistura
        - hidden markob models
        - redes de belief bayesiano
    - não paramétricos
        - estimação com histogramas
        - estimação com Parzen window
        - estimação de vizinho mais próximo (KNN)

### Densidade Gaussiana
- O modelo gaussiano é algo que podemos usar quando consideramos os vetores de features como contínuos
- Algumas propriedades de guassianas:
    - facilmente estudado de forma analítica
    - definido pela sua média e variância
    - muitos processos são assintoticamente gaussianos (teorema do limite central)
    - para variáveis gaussianas, elas não terem correlação implica que são independentes

#### Gaussiana 1 variável
- Como sabemos
$$P(x)=N(\mu,\sigma^{2})=\frac{1}{\sqrt{2\pi} \sigma}\exp\left[- \frac{(x-\mu)^{2}}{2\sigma^{2}}\right]$$
em que $\mu=\mathbb{E}[x]~,~\sigma^{2}=\mathbb{E}[(x-\mu)^{2}]$

#### Gaussiana multivariável
- Para $\mathbf{x}\in\mathbb{R}^{D}$:
$$p(\mathbf{x})=N(\boldsymbol{\mu},\Sigma)=\frac{1}{(2\pi)^{\frac{D}{2}}|\Sigma|^{\frac{1}{2}}} \exp \left[- \frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^{T}\Sigma^{-1}(\mathbf{x}-\boldsymbol{\mu}) \right]$$
![[Attachments/gaussiana 2d.png]]
as linhas vermelhas são poontos em que o expoente do exponencial é constante. 

### Classificador Linear de Bayes
- Assumimos que as densidades condicionais da class são gaussianas, e que todas têm a mesma matriz de covariância:
$$p(\mathbf{x}|\mathcal{C}_{k})=\frac{1}{(2\pi)^{\frac{D}{2}}|\Sigma|^{\frac{1}{2}}}\exp\left[- \frac{1}{2}(\mathbf{x}-\boldsymbol{\mu}_{k})^{T}\Sigma^{-1}(\mathbf{x}-\boldsymbol{\mu}_{k}) \right]$$
assim calculamos:
$$p(\mathcal{C}_{k}|\mathbf{x})=\frac{p(\mathbf{x}|\mathcal{C}_{k})p(\mathcal{C}_{k})}{\sum\limits_{j=1}^{K} p(\mathbf{x}|\mathcal{C}_{j})p(\mathcal{C}_{j})}$$
se só houverem 2 classes, a boundary de decisão é linear:
![[limiar decisao par 2 gaussianas.png]]
as 2 classes seriam separadas por um plano que corta o espaço a meio entre as 2 gaussianas.

### Modelo Quadrático Descriminante
- A superfície que limita as decisões (do tipo, se temos um ponto à esquerda desta superficie então decidimos X) é:
    - planar se todas as classes têm a mesma matriz de covarância
    - quadrática se caso contrário

## Estamos mais perto da vida real
- OK, já temos uma forma teórica que nos permitirá obter as probabilidades condicionadas de classe. Mas na prática como fazemos?
- Usando os dados de treino, podemos determinar 
$$\hat{\boldsymbol{\mu}}=\frac{1}{n}\sum\limits_{i=1}^{n} \mathbf{x}_{i}~~~~,~~~~ \hat{\Sigma}=\frac{1}{n}\sum\limits_{i=1}^{n}(\mathbf{x}_{i}-\hat{\boldsymbol{\mu}})(\mathbf{x}_{i}-\hat{\boldsymbol{\mu}})^{T}$$
![[comportamento normal de samples.png]]

## Exemplo 2D
![[dados random ex1.png|400]]
- Consideremos um problema em que temos 2 classes com 2 features. (2 classes em 2D)
- A partir dos dados de treino podemos obter as probabilidades condicionadas de classe:
$$p(\mathbf{x}|\mathcal{C}_{1})=\begin{pmatrix}x_{1} \\ x_{2}\end{pmatrix}\in N ( \begin{pmatrix}4 \\ 2\end{pmatrix}, \begin{pmatrix}1 & 1 \\ 1 & 2\end{pmatrix})$$
$$p(\mathbf{x}|\mathcal{C}_{2})=\begin{pmatrix}x_{1} \\ x_{2}\end{pmatrix}\in N(\begin{pmatrix}1 \\ 1\end{pmatrix}, \begin{pmatrix}1 & 1 \\ 1 & 2\end{pmatrix})$$
assumimos ainda que temos perdas iguais em caso de erro e assumimos que temos priors iguais ($P(\mathcal{C}_{1})=P(\mathcal{C}_{2})=0.5$). Queremos saber a equação que divide as classes.

**Como fazer**
- Temos 
$$\Sigma^{-1}=\begin{pmatrix}2 & -1 \\ -1 & 1\end{pmatrix}$$
- Definimos:
$$d(\mathbf{x})=(\mathbf{x}-\boldsymbol{\mu}_{1})^{T}\Sigma^{-1}(\mathbf{x}-\boldsymbol{\mu}_{1})-(\mathbf{x}-\boldsymbol{\mu}_{2})^{T}\Sigma^{-1}(\mathbf{x}-\boldsymbol{\mu}_{2})$$
que nos dá
$$d(\mathbf{x})=\begin{pmatrix}5  \\ -2\end{pmatrix}\mathbf{x}-9.5=5x_{1}-2x_{2}-9.5$$
que fica:
![[ajustes gaussianos e limiar ex1.png|425]]

## Matriz de perdas
- Podemos definir
$$L=\begin{pmatrix}\ell_{11} & \ell_{12} \\ \ell_{21} & \ell_{22}\end{pmatrix}$$
em que, por exemplo, $\ell_{12}$ é o custo/penalização por atribuir classe $\mathcal{C}_{2}$ a algo que na realidade é $\mathcal{C}_{1}$.

- Assim, podemos definir:
    - Custo de atribuir classe $\mathcal{C}_{1}$: $$\ell_{11}p(\mathcal{C}_{1}|\mathbf{x})+\ell_{21}p(\mathcal{C}_{2}|\mathbf{x})$$
    - Custo de atribuir classe $\mathcal{C}_{2}$: $$\ell_{12}p(\mathcal{C}_{1}|\mathbf{x}) + \ell_{22}p(\mathcal{C}_{2}|\mathbf{x})$$

- Podemos então redefinir as regras de decisão. 
    - Decidimos classe $\mathcal{C}_{1}$ se:![[deducao condição para pesos.png|442]]

## Estimação de Densidade
- Um estimador de densidade establece uma relação entre os atributos de um input e a sua probabilidade (recebe input e dá densidade de probabilidade dele)
- AKA Estimação de parâmetros se a distribuição de probabilidade for conhecida
![[estimacao densidade.png]]

### Estimação de parâmetros com dados iid
- **iid** - independent, identically distributed (casos / inputs)
- Temos $N$ casos de treino iid:
$$D=\{\mathbf{x}_{1},\mathbf{x}_{2},\dots,\mathbf{x}_{N}\}$$
- Uma approach é: **MLE** - maximum likelihood estimation
- Este é um dos estimadores mais comuns neste caso
- Definimos a likelihood dos dados como: $L(\theta)=P(\mathbf{x}_{1},\dots,\mathbf{x}_{N};\theta)$
- Assim:
$$\boldsymbol{\theta}^{*}=\text{argmax}_{\theta}L(\boldsymbol{\theta})=\text{argmax}_\theta\log L(\theta)$$

# Naive Bayes
- Consiste em aprender a classificação ao aprender $P(y|\mathbf{x})$.
- Temos:
![[ex_classificadores.png]]
e consideramos $y$=Wealth, $\mathbf{x}$=(Gender, HrsWorked)
- Aqui temos 2 parâmetros de $x$, então é fácil estudar o sistema.

- Mas e se tivéssemos mais, tipo 30??
- Temos $\mathbf{x}=\{x_{1},\dots,x_{n}\}$. Do teorema de Bayes:
$$P(y|\mathbf{x})=\frac{P(\mathbf{x}|y)P(y)}{P(\mathbf{x})}$$
ou, mais concretamente:
$$P(y_{i}|\mathbf{x_{j}})=\frac{P(\mathbf{x}_{j}|y_{i})P(y_{i})}{\sum_{k}P(\mathbf{x}_{j}|y_{k})P(y_{k})}$$

### Suposição de Naive Bayes
Assumimos que
$$P(x_{1},x_{2},\dots,x_{n}|y)=P(x_{1}|y)P(x_{2}|y)\cdots P(x_{n}|y)$$
ou seja, $x_{i},x_{j}$ são condicionalmente independentes para um certo $y$ ($i\neq j$)

- **Condicionalmente Independente**
    - X é condicionalmente independente de Y dado Z, se a distribuição de X é independente da de Y, para um certo valor de Z.
    - $P(X|Y,Z)=P(X|Z)$

- Então, com esta suposição fica:
$$\begin{align*}
P(y_{k}|x_{1},\dots,x_{n})&= \frac{P(y_{k})P(x_{1},\dots,x_{n}|y_{k})}{\sum_{j}P(u_{j})P(x_{1},\dots , x_{n}|y_{j})}\\
&= \frac{P(y_{k})\prod_{i}P(x_{i}|y_{k})}{\sum_{j}P(y_{j})\prod_{i}P(x_{i}|y_{j})}
\end{align*}$$
- Assim, se $\mathbf{x}_{new}=\{x_{1},x_{2},\dots,x_{n}\}$ temos $$y_{new}=\text{argmax}_{y_{k}}P(y_{k})\prod_{i}P(x_{i}^{new}|y_{k})$$

#### Algoritmo
- Treino
    - Para cada valor $y_{k}$, estimar $\pi_{k}=P(y=y_{k})$
    - Para cada valor $x_{ij}$ dum atributo $x_{i}$, estimar _$\theta_{ijk}=P(x_{i}=x_{ij}|y=y_{k})$
    - (Acho que isto pode ser tudo calculado diretamente com código, a calcular casos favoráveis / casos totais)
- Classificar um vetor de teste $\mathbf{x}^{new}$
    - A fórmula de $y^{new}$ acima fica: $$y^{new}=\text{argmax}_{y_{k}}\pi_{k}\prod_{i}\theta_{ijk}$$
- Temos então os estimadores MLE:
$$\begin{align*}
\hat{\pi}&= \hat{P}(y=y_{k})=\frac{\# D\{y=y_{k}\}}{|D|}\\
\hat{\theta}_{ijk}&= \hat{P}(x_{ij}|y=y_{k})=\frac{\# D\{x_{i}=x_{ij}\wedge y=y_{k}\}}{\# D\{y=y_{k}\}}
\end{align*}$$
(ou seja, é mesmo só calcular casos favoráveis / casos totais)

### Subtlety nº1
- Pode acontecer $P(x_{i}|y)=0$
- Isto pode parecer insignificante porque é só 1 atributo possivelmente em dezenas
- Mas como vimos, na aproximação de condiconalmente independentes, temos uma *multiplicação* desta probabilidade para *todos* os atributos.
    - Se algum deles for zero, o resultado vai ser zero.
- Uma forma de impedir isto é usar estimadores **MAP**:
$$\begin{align*}
\hat{\pi}&= \hat{P}(y=y_{k})=\frac{\# D\{y=y_{k}\}+\alpha_{k}}{|D|+\sum_{m}\alpha_{m}}\\
\hat{\theta}_{ijk}&= \hat{P}(x_{ij}|y=y_{k})=\frac{\# D\{x_{i}=x_{ij}\wedge y=y_{k}\}+\alpha_{k}'}{\# D\{y=y_{k}\}+\sum_{m}\alpha_{m}'}
\end{align*}$$
em que MAP = **Maximum A Posteriori** - usamos $\hat{\theta}=\text{argmax}_{\theta}P(\theta|\mathcal{D})$

### Distribuição Beta
Consiste em:
$$P(\theta)=\frac{\theta^{\beta_{H}-1}(1-\theta)^{\beta_{T}-1}}{B(\beta_{H},\beta_{T})}\sim \text{Beta}(\beta_{H},\beta_{T})$$
![[distribuicao beta.png]]
em que temos a função de likelihood $$P(\mathcal{D}|\theta)=\theta^{\alpha_{H}}(1-\theta)^{\alpha_{T}}$$
e o posterior será do tipo
$$\begin{align*}
P(\theta|\mathcal{D})&\propto P(\mathcal{D}|\theta)P(\theta)\\
&= \frac{\theta^{\beta_{H}+\alpha_{H}-1}(1-\theta)^{\beta_{T}+\alpha_{T}-1}}{B(\beta_{H}+\alpha_{H},\beta_{T}+\alpha_{T})}
\end{align*}$$

### Distribuição de Dirichlet
- Consiste em ter:
$$P(\theta_{1},\theta_{2},\dots,\theta_{K})=\frac{1}{B(\alpha)}\prod_{i}^{K}\theta_{i}^{a_{i}-1}$$

### Subtlety nº2
- Na vida real, é comum as variáveis $x_{i}$ não serem condicionalmente independentes.
- No entanto, mesmo que a probabilidade esteja errada, pode ser possível obter classificações boas
- Por exemplo, se tivermos 2 cópias $x_{i}=x_{j}$ então teríamos 2 atributos que sabemos que não são independentes de qualquer forma. Isto provavelmente irá resultar num enviesament na distribuição

### Naive Bayes para documentos de texto
- Por exemplo
    - Classificar mails como spam
    - Classificar que páginas web são de estudantes
- A grande dúvida é como representar/introduzir os documentos de texto no Naive Bayes
- Uma técnica mais básica é *bag of words*, que consiste em contar quantas vezes cada palavra aparece.

#### Técnica mais geral
0. Queremos classificar um documento com "É interessante? Sim ou Não" $\{+,-\}$ 
1. Consideramos cada documento de texto como um vetor de atributos, em que cada palavra é um atributo
2. Para treinar o modelo, podemos usar exemplos, que permitam estimar $P(+),P(-),P(doc|+),P(doc|-)$

- Aqui poderia ainda ser útil fazer outra suposição (além da de independência condicional):
$$P(a_{i}=w_{k}|v_{j})=P(a_{m}=w_{k}|v_{j})~~\forall i,m$$
ou seja, para um certo resultado final (sendo que $v_{j}$) 

### Naive Bayes X Contínuo, Y discreto
- Imaginemos agora que $x_{i}$ é contínuo
- Se considerarmos um perfil gaussiano temos:
$$P(x_{i}=x|y=y_{k})=\frac{1}{\sigma_{ik}\sqrt{2\pi}}e^{-\frac{(x-\mu_{ik})^{2}}{2\sigma_{ik}^{2}}}$$
podemos assumir que a variância é
    - independente de $y$
    - independente de $x_{i}$
    - independente de ambas

#### Algoritmo
- Com os dados de treino, para cada valor $y_{k}$ estimar $\pi_{k}=P(y=y_{k})$
- Para cada atributo $x_{i}$ estimar $\mu_{ik},\sigma_{ik}$
- Tendo um valor não-de-treino $x^{new}$, podemos classificá-lo com:
$$y^{new}=\text{argmax}_{y_{k}}\pi_{k}\prod_{i}\text{Normal}(x_{i}^{new},\mu_{ik},\sigma_{ik})$$
em que $\mu_{ik}$ é a média da feature i, classe k

- Na prática:
$$\begin{align*}
\hat{\mu}_{ik}&= \frac{1}{\sum_{j}\delta(Y^{j}=y_{k})}\sum\limits_jX_{i}^{j}\delta(Y^{j}=y_{k})\\
\hat{\sigma}_{ik}^{2}&= \frac{1}{\sum_{j}\delta(Y^{j}=y_{k})}\sum\limits_{j}(X_{i}^{j}-\hat{\mu}_{ik})^{2}\delta(Y^{j}=y_{k})
\end{align*}$$

# Estimação de Densidade
- Temos técnicas *paramétricas*
    - Max Likelihood (ML)
    - Max A Posteriori (MAP)
    - Inferência Bayesiana
    - Modelos de Mistura Gaussiana (GMM)
- Técnias *não-paramétricas*
    - Histogramas
    - Janelas de Parzen
    - KNN

## Não-paramétricas
- Métodos paramétricos dão-nos densidades que funcionam mas não são as verdadeiras
- Além disso, técnicas paramétricas são unimodais, mas muitos problemas reais são multimodais 
- Métodos não paramétricos permitem determinar densidades sem antes assumir algo (possivelmente errado) sobre elas

### Histogramas
- Mais simples e intuitivo
- Como sabemos, 
    - dividimos cada dimensão $x_{i}$ do vetor $\mathbf{x}$ em $m$ intervalos ($m$ é um valor fixo)
    - teremos então $M$ caixas (bin) de volume igual $V$ que indicam quantos pontos caem dentro de cada intervalo/bin
- Consideremos que temos $N$ samples ($x_{i},i=1,\dots,N$). O número de pontos no bin $i$ ($b_{i}$) é $n_{i}$. 
- Assim, com o histograma estimamos a densidade como sendo
$$\hat{p}(\mathbf{x})=\frac{n_{i}}{NV}~~~~,~~\mathbf{x}\in b_{i}$$
ou seja, a densidade $p$ só depende do bin $b_{i}$ 

- Temos a função de densidade:
$$\int \hat{p}(\mathbf{x})dx=\sum\limits_{i=1}^{M}\int_{b_{i}}\frac{n_{i}}{NV}dx=1$$
- Obviamente, $M$ é um parâmetro fundamental: decide o smoothing dos dados.

**Notas sobre aplicação**
- Estimar PDF com histograma é uma técnica eficiente: podemos simplesmente ir guardando as contagens, sem ter que guardar os valores previamente inserido.
- *Problema*: podemos ter descontinuidades que se devem apenas à forma como o intervalo foi dividido, e não às propriedades dos dados.
- Só é verdadeiramente útil para sets com baixa dimensão. Um set com $D$ dimensões terá $M^{D}$ bins para estudar. ($M$ aumenta exponencialmente)

### PW e KNN
- Imaginemos que as observações são retiradas de uma densidade de probabilidade $p(\mathbf{x})$ de D dimensões. Queremos portanto estimar $p(\mathbf{x})$
- Consideramos uma região $\mathcal{R}$ de volume $V$ que contém $\mathbf{x}$ (o ponto de interesse) (e em princípio está centrada neste potno)
- Recolhemos um data set com $N$ observações (retiradas de $p(\mathbf{x})$ claro)
- Cada ponto deste data set terá uma probabilidaded $P$ de estar dentro da região pré-defenida $\mathcal{R}$. Ora, ou um ponto está em $\mathcal{R}$ ou não está -- distribuição kinda binomial
- O número de pontos que *está* dentro de $\mathcal{R}$ é $K\simeq NP$ (média de uma distribuição binomial)

- Mas, e se considerarmos que $\mathcal{R}$ é mesmo muito pequeno? Ora, se for suficientemente pequeno teremos que $p(\mathbf{x})$ é constante nesta região. Assim:
$$P\approx p(\mathbf{x})V~~\to~~ p(\mathbf{x})=\frac{K}{NV}$$
($V$ é o "volume" da região, de D dimensões)

**Contradição**
- Consideramos que $\mathcal{R}$ será tão pequeno que $p(\mathbf{x})$ é constante
- Também consideramos que $\mathcal{R}$ é grande o suficiente para $K$ ser elevado o suficiente que conseguimos ter uma boa aproximação.
- Isto é obviamente contraditório

**Impedir problemas**
- Para garantir que temos uma boa aproximação de $p(\mathbf{x})$ enquanto que podemos considerar $p(\mathbf{x})$ constante em $\mathcal{R}$, precisamos que hajam sempre muitos pontos em $\mathcal{R}$ independentemente do seu tamanho
    - Podemos fixar o volume $V$ e tirar vários samples neste volume. Assim $K/N\to P$. **Mas** ao fazer isto no final teremos uma estimativa da *média* de $p(\mathbf{x})$, não da densidade em si (porque estaremos a fazer a média da densidade estimada em cada sample, e $K/N$ irá variar de sample para sample)
    - Podemos invés, fixar $N$ e variar o volume tal que $V\to0$. Assim, $p(\mathbf{x})$ vai-se tornando constnate no volume. **Mas** eventualmetne teremos uma região tão pequena que não temos samples dentro ($N$ é finito)

- Ou seja: a 2ª approach não é aplicável 
- A 1ª opção, apesar de imperfeita, é algo que temos de aceitar.

**Volume**
- Mas, precisamos de saber que volume $V$ escolher. É preciso que
    - $V$ seja grande o suficiente para ter um bom número $K$
    - Seja pequeno o suficiente para considerar $p(\mathbf{x})\simeq\text{constante}$ ser uma suposição minimamente lógica.

- Temos 2 formas principais de tratar disto:
    - Fixar o valor de $K$ e determinar o volume $V$ que os dados ocupam (recolher dados, ver onde estão, ver que volume $V$ ocupam os $K$ dados mais na região). Isto introduz o método **KNN** (K-Neares-Neighbour)
    - Fixar o volume $V$ e contar quantos pontos estão nele : $K$. Isto é o *kernel approach* AKA **PW** (Parzen Windows)

- Pode-se demonstrar que tanto KNN como PW convergem para o valor real de densidade quando $N\to\infty$

#### PW (Parzen Windows)
- O número de pontos que estão dentro da região escolhida é contado com uma *windowing function*, daí o nome.
- Consideramos que $\mathcal{R}$ é um hipercubo $d$-dimensional de lado $h$.
    - Assim: $V=h^{d}$
- Assim, definimos uma função janela (AKA kernel function) que quantos samples estão em $\mathcal{R}$ ($K$):
$$\phi(\mathbf{u})=\begin{cases}
1 & ; & |\mathbf{u}_{j}|\le \frac{1}{2}~~~~j=1,2,\dots,d \\
0 & ; & \text{restantes casos}
\end{cases}$$
em que $$\mathbf{u}=\frac{\mathbf{x}-\mathbf{x}_{i}}{h}$$
em que, aqui, $\mathbf{x}$ é o ponto no centro do cubo e também o ponto em que queremos saber a densidade.
![[parzen.png]]

- Assim teremos:
$$K=\sum\limits_{i=1}^{N}\phi\left(\frac{\mathbf{x}-\mathbf{x}_{i}}{h}\right)$$

- Juntando isto ao facto que a estimativa de $p(\mathbf{x})$ de 1 sample é $p(\mathbf{x})=\frac{k_{n}}{V_{n}n}$ temos:
$$\tilde{p}(\mathbf{x})=\frac{1}{n}\sum\limits_{i=1}^{N} \frac{1}{V}\phi\left(\frac{\mathbf{x}-\mathbf{x}_{i}}{h}\right)=\frac{1}{nh^{d}}\sum\limits_{i=1}^{N}\phi\left(\frac{\mathbf{x}-\mathbf{x}_{i}}{h}\right)$$

**Na prática**
- Queremos determinar $\hat{p}(\mathbf{x})$ - a densidade no ponto $\mathbf{x}$
- Teremos os dados de treino $\mathbf{x}_{i}$. De acordo com a fórmula acima, estimamos $\hat{p}(\mathbf{x})$ ao *interpolar* os valores de $\phi$ na região, usando a distância de cada ponto $\mathbf{x}_{i}$ a $\mathbf{x}$.
- Se $\phi$ também for uma distribuição, então $\hat{p}(\mathbf{x})$ irá converger para $p(\mathbf{x})$ conforme aumenta $N$
- Uma escolha frequente de $\phi$ é a *gaussiana*.
    - Determinamos então $p(\mathbf{x})$ ao fazer uma série de sobreposições de gaussianas, tais que $h$ é a **variância** destas.

- A escolha de $h$ (variância AKA bandwidth da gaussiana). Se for muito grande teremos pouca resolução na estimativa, se for muito baixa a estimativa terá demasiada variabilidade.
![[knn dependencia h.png]]

- Um baixo $h$ também levará a boundaries mais complexas (over fitting), enquanto que um valor alto pode levar a boundaries mais simples (possivelmente under fitting):
![[knn dependencia h 2d.png]]

#### KNN (K Nearest Neighbours)
- Estimamos a densidade a partir de $N$ dados de treino. Centramos um volume $V$ em torno de $\mathbf{x}$.
- Dos $N$ pontos, aqueles que estão dentro de $V$ são os $K$ nearest neighbours.
- Em pontos em que temos grande densidade (de probabilidade e portanto de pontos) em torno de $\mathbf{x}$, usamos volumes menores.
- $K$ funciona de forma similar a $h$ em PW

**KNN como classificador**
- Temos $N$ samples e um volume $V$ em torno de $\mathbf{x}$. Dentro de $V$ temos $K$ pontos, de modo que estimamos$$\hat{p}=\frac{K}{NV(\mathbf{x})}$$
- Consideremos que temos $M$ classes, de modo que temos $K_{m}$ pontos da classe $\mathcal{C}_{m}$ (temos $\sum_{m=1}^{M}K_{m}=K$)
- Temos ainda que o número total de pontos na classe $\mathcal{C}_{m}$ é $N_{m}$ (temos $\sum_{m=1}^{M}N_{m}=N$)
- Podemos estimar então a densidade condicional de classe:
$$\hat{p}(\mathbf{x}|\mathcal{C}_{m})=\frac{K_{m}}{N_{m}V}$$
e a probabilidade prior:
$$\hat{p}(\mathcal{C}_{m})=\frac{N_{m}}{N}$$
- Usando estas estimativas com a regra de decisão:
$$\mathbf{x}\in \mathcal{C}_{m} \text{ se } \forall i:~\hat{p}(\mathcal{C}_{m}|\mathbf{x})\ge \hat{p}(\mathcal{C}_{i}|\mathbf{x})$$
que, pelo teorema de Bayes fica:
$$\mathbf{x}\in \mathcal{C}_{m} \text{ se } \forall i:~K_{m}\ge K_{i}$$
- Por outras palavras, atribuimos $\mathbf{x}$ à classe que contém uma maior porção dos KNN.
- Podemos simplesmente escolher $K=1$, o que atribui a $\mathbf{x}$ a classe do ponto mais próximo. Esta regra é muito simples e imperfeita, mas se tivermos muitos pontos de treino isto resulta num erro sempre inferior ao dobro do rate de Bayes

### PW vs KNN
- Parzen necessita que se guarde todas as $N$ observações **E** das $N$ avaliações, o que rapidamente se torna computacionalmente pesado
- KNN apenas necessita que se guarde as $N$ observações
- Histogramas não necessitam que se guarde as observações, apenas das configurações dos bins. Mas o número de bins cresce exponencialmente com as Dimensões!

### Vantagens e Desvantagens de métodos não-paramétricos
**Vantagens**
- Mais geral: dá para vários tipos de dados
- Não precisamos de assumir nada sobre as densidades
- Se tivermos muitos pontos, é exato

**Desvantagens**
- Precisa de muitos dados/pontos
- Aumentar o número de dimensões aumenta imenso número de dados necessários
- PW e KNN são mais pesados computacionalmente