# O que é
- Uma regressão linear consiste em usar dados ou informação previamente conhecidos para prever um dado futuro.
    - Por exemplo, prever as emissões de um motor novo, sabendo o seu tamanho, número de cilindros e consumo; assim como dados de outros motores.

## Outros tipos
- Regressão Linear
- Regressão Polinomial
- Regressões de Lasso ou Ridge 
- Regressão ordinal
- Regressão linear Bayesiana
- Regressão de Rede Neuronal

# Como se faz curve fit
- Temos um conjunto de dados e queremos determinar um certo parâmetro associado a estes. Normalmente isto implica fazer "curve fit", que como o nome indica consiste em ajustar uma curva aos dados.
- Queremos então determinar a função que "passa" pelos dados e segue a sua disposição no espaço o melhor possível.
- Consideremos os dados $(y_{n},x_{n})\in\mathbb{R}\times \mathbb{R}^{l}$

- Assim a tarefa de fazer um curve fit consiste em 2 partes:
    1. Escolher o tipo de função que descreve os dados (linear, quadrática, etc)
    2. Escolher os parâmetros que garantem um bom ajuste

## Escolher tipo de função
- Este passo pode ser resumido a:
    - Temos dados $(y_{n},x_{n})~,~y_{n}\in\mathbb{R}~,~x_{n}\in\mathbb{R}^{l}$ e um conjunto paramétrico de funções: $\mathcal{F}:= \{f_{\theta}(\cdot) : \theta\in\mathcal{A}\subset\mathbb{R}^{K}\}$
    - Queremos encontrar uma função pertencente a $\mathcal{F}$, $f(\cdot)$, tal que ao receber um valor $\boldsymbol{x}\in\mathbb{R}^{l}$ temos o valor $f(\boldsymbol{x})$ que melhor se aproxima de $y\in\mathbb{R}$

- Para fazer esta decisão, devemos usar o máximo de informação prévia sobre os dados que conseguirmos, como por exemplo o mecanismo físico a que os dados estão associados.
- Normalmente usamos diferentes famílias de funções, testamos e escolhemos aquela que tem a melhor performance (segundo o certo critério que decidimos)

## Funções de Custo e Perda
- Ok, escolhemos a família de funções $\mathcal{F}$. Vamos estimar os parâmetros.
- Torna-se então útil uma forma de quantificar o quão bem ajustada a regressão está aos dados. Essa é a *função de perda*.
- Ela mede a relação desvio/erro entre o valor medido $y$ e aquele previsto usando $f(x)$ ($f\in\mathcal{F}$)

- Procedemos então assim:
    1. Escolhemos uma possível função de perda que seja não-negativa: $\mathcal{L}(\cdot,\cdot):\mathbb{R}\times\mathbb{R}\to [0,\infty[$. Esta função é usada para calcular a qualidade do ajuste *em cada ponto*
    2. Calculamos uma estimativa, $\theta_{*}$. Este será o valor de melhor ajuste. Isso será quanto temos a *mínima perda total*

- Ora, a "perda total" é aquilo a que chamamos *custo*. Ou seja, podemos definir a função de custo:
$$J(\theta):=\sum\limits_{n=1}^{N}\mathcal{L}(y_{n},f_\theta(x_{n}))$$
e teremos
$$\theta_{*}=\underset{\theta\in\mathcal{A}}{\text{argmin}[J(\theta)]}$$

- Claro, isto tudo é feito assumindo que **existe** um mínimo. Pode não existir, ou podem haver vários.

### Função de perda de erro quadrado
- Este é um tipo de função de erro definido como
$$\mathcal{L}(y,f_{\theta}(x))=(y-f_{\theta}(x))^{2}$$
- Ao fazer o método acima estamos a fazer o método de *Least-Squares* (LS).
- Usar LS para ajustes lineares tem várias vantagens computacionais, que são a razão porque este é um dos métodos mais populares.
    - Obtemos uma solução única
    - Os parâmetros são dados por um sistema de equações lineares

# Regressão Linear
- Queremos então relacionar uma VA dependente $\text{y}$ com VAs independentes $\text{x}_{1},\dots,\text{x}_{l}$. 
- Podemos pensar nisto como um sistema:
    - Temos a saída $\text{y}$
    - Temos as entradas $\text{x}_{1},\text{x}_{2},\dots,\text{x}_{l}$ que formam um VeA $\mathbf{x}$ 
    - Esta relação está associada a um termo de **ruído** $\eta$
    - Queremos saber um parâmetro $\theta$ que relaciona a saída e a entrada.
- Para determinar $\theta$ queremos usar $N$ medições $(y_{n},\boldsymbol{x}_{n})$. A este conjunto chamamos de *dados de treino*.

## LS
- No caso linear temos:
$$\text{y}=\theta_{0} + \theta_{1}\text{x}_{1}+\dots+\theta_{l}\text{x}_{l}+\eta=\begin{bmatrix}\boldsymbol{\theta}^{T} & \theta_{0}\end{bmatrix}\begin{bmatrix}\mathbf{x}\\1\end{bmatrix} + \eta$$
ou seja:
$$\text{y} = \boldsymbol{\theta}^{T}\mathbf{x} + \eta $$
(aqui inserimos $\theta_{0}$ em $\text{y}$ e aumentamos $\textbf{x}$ em 1. $\theta_{0}$ é o *bias ou interseção*)

#### Como? - v1
- Ora, usando esta lógica para um estimador, temos:
$$\hat{y}=\boldsymbol{x}\hat{\boldsymbol{\theta}}$$
usando LS e considerando $\hat{\boldsymbol{\theta}}=\boldsymbol{\theta}_{*}$ temos:
$$J(\boldsymbol{\theta})=\sum\limits_{n=1}^{N}(y_{n}-\boldsymbol{x}_{n}\boldsymbol{\theta})^{2}$$
queremos o $\boldsymbol{\theta}$ que minimiza isto. Assim:
$$\begin{align*}
L(\boldsymbol{\theta})&= \sum\limits_{n=1}^{N}\left[y_{n}^{2}- 2y_{n} \boldsymbol{x}_{n}\boldsymbol{\theta} + x_{n}^{2} \boldsymbol{\theta}^{2} \right]\\
\frac{dL}{d\boldsymbol{\theta}}&= \sum\limits_{n=1}^{N}\left[0 - 2y_{n}\boldsymbol{x}_{n} + 2\boldsymbol{x}_{n}^{2}\boldsymbol{\theta} \right]\\
\end{align*}$$
num mínimo temos derivada nula:
$$\begin{align*}
\frac{dL}{d\boldsymbol{\theta}}\Biggr|_\hat{\boldsymbol{\theta}} &= 0\\
\left(\sum\limits_{n=1}^{N}\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{T}\right)\hat{\boldsymbol{\theta}}&= \sum\limits_{n=1}^{N}y_{n}\boldsymbol{x}_{n}\\
\hat{\boldsymbol{\theta}}&= \frac{\sum\limits_{n=1}^{N}y_{n}\boldsymbol{x}_{n}}{\sum\limits_{n=1}^{N}\boldsymbol{x}_{n}\boldsymbol{x}_{n}^{T}}
\end{align*}$$

#### Como? - v2
- Podemos definir a *matriz de entrada* $X$ de dimensão $N\times(l+1)$ em que:
$$X:=\begin{pmatrix}\boldsymbol{x}_{1}^{T}\\ \boldsymbol{x}_{2}^{T}\\\vdots\\\boldsymbol{x}_{N}^{T}\end{pmatrix}=\begin{pmatrix}x_{11} & \cdots & x_{1l} & 1 \\ x_{21} & \cdots & x_{2l} & 1 \\ \vdots & \ddots & \vdots & \vdots \\ 
x_{N1} & \cdots & x_{Nl} & 1\end{pmatrix}$$
- Temos $\hat{y}=\hat{\boldsymbol{\theta}}^{T}\boldsymbol{x}$. Passemos para matrizes. Ora, $Y$ tem dimensão $N\times 1$ e $X$ tem dimensão $N\times(l+1)$. Assim, $\Theta^{T}$ tem que ter dimensão $(l+1)\times 1$. Ou seja:
$$Y = X\Theta^{T} ~~\to~~(N,1)=(N,l+1)(l+1,1)$$
(os dois lados têm a dimensão de $Y$)

- Podemos reescrever:
$$X^{T}Y=X^{T}X \Theta^{T} ~~~~~~\to~~ (l+1,N)(N,1)=(l+1,N)(N,l+1)(l+1,1)$$
(os dois lados têm a dimensão de $\Theta^{T}$)

ficando 
$$\Theta^{T}=(X^{T}X)^{-1}X^{T} Y$$
- Se tivermos $y=\boldsymbol{\theta}^{T}\boldsymbol{x}+\eta$ tal que $\eta\sim\mathcal{N}(0,\sigma_{\eta}^{2})$ então o estimador acima será *unbiased e eficiente*.
- Se o ruído não for gaussiano isto já não é verdade.

#### Regularização
- Como já foi dito, a regressão linear obtida usando LS é *única*.
- Assim, a solução vai depender da variância do ruído (o quão dispersos os dados estão).
- Ora, o estimador LS tem variância mínima e é unbiased, assumindo que:
    - usamos um modelo linear
    - o white noite presente é *gaussiano*
- Fazemos *regularização* para **impôr informação a-priori** na solução.
    - Também podemos ver esta tarefa como uma forma de impôr *bias* num estimador.

#### Regularização em ML
- Não temos dados suficientes para garantir que a matriz $X^{T}X$ será sempre inversível ao fornecer dados de teste.
- Existe demasiado ruído
- Não existe informação suficiente nos dados para especificar a solução
- Assim, no caso de ML a regularização consiste em limitar as escolhas de funções de erro. Podemos ainda introduzir um termo de regularização na função de erro para controlar overfitting

- No caso de LS, a tarefa de LS consiste em tentar reduzir a norma das estimativas de parâmetro $\theta$. Ou seja, reformulamos o método LS assim:
    - Queremos determinar o $\boldsymbol{\theta}$ que minimiza $J(\boldsymbol{\theta})=\sum_{n=1}^{N}(y_{n}-\boldsymbol{\theta}^{T}\boldsymbol{x}_{n})^{2}$, em que nos limitamos a $\boldsymbol{\theta}$ tal que $\|\boldsymbol{\theta}\|^{2}\le\rho$
- Podemos então reescrever esta formulação na forma:
    - Queremos determinar o $\boldsymbol{\theta}$ que minimiza $L(\boldsymbol{\theta},\lambda)=\sum_{n=1}^{N}(y_{n}-\boldsymbol{\theta}^{T}\boldsymbol{x})^{2}+\lambda\|\boldsymbol{\theta}\|^{2}$

- Ora, claro, para certos valores de $\lambda\ge0,\rho$ as 2 formulações acima são *equivalentes*.
- Vamos então derivar:
$$\begin{align*}
L(\boldsymbol{\theta},\lambda)&= \sum\limits_{n=1}^{N}(y_{n}-\boldsymbol{x}_{n}\boldsymbol{\theta})^{2} + \lambda \|\boldsymbol{\theta}\|^{2}\\
\frac{dL}{d\boldsymbol{\theta}}&= \sum\limits_{n=1}^{N}[-2y_{n}\boldsymbol{x}_{n} + 2 \boldsymbol{x}_{n}^{2}\boldsymbol{\theta}] + 2\lambda\|\boldsymbol{\theta}\|\\
\end{align*}$$
queremos, claro, ter a derivada nula:
$$\begin{align*}
\frac{dL}{d\boldsymbol{\theta}}\Biggr|_{\hat{\boldsymbol{\theta}}}&= 0\\
\sum\limits_{n=1}^{N} \boldsymbol{x}_{n}^{2}\hat{\boldsymbol{\theta}} + \lambda \|\hat{\boldsymbol{\theta}}\|&= \sum\limits_{n=1}^{N} y_{n}\boldsymbol{x}_{n}\\
\left[\sum\limits_{n=1}^{N} \boldsymbol{x}_{n}\boldsymbol{x}_{n}^{T} + \lambda I \right] \hat{\boldsymbol{\theta}}&= \sum\limits_{n=1}^{N}y_{n}\boldsymbol{x}_{n}\\
\hat{\boldsymbol{\theta}}&= \frac{\sum\limits_{n=1}^{N}y_{n}\boldsymbol{x}_{n}}{\sum\limits_{n=1}^{N} \boldsymbol{x}_{n}\boldsymbol{x}_{n}^{T} + \lambda I}
\end{align*}$$

 - Nitidamente, $\lambda$ introduz bias na solução, em comparação com a versão unbiased.

### Regularização generalizada
- Para ter uma melhor regularização, temos (para obter um parâmetro $\mathbf{w}$)
$$\mathcal{L}(\mathbf{w})=\frac{1}{2} \left[\sum\limits_{n=1}^{N}(y_{n}-\mathbf{w}^{T}\mathbf{x})^{2} + \lambda\sum\limits_{n=1}^{D}\|w_{i}\|^{q} \right]$$
- Para $q=1$ temos a *regressão de lasso*

# Problemas inversos
- Problemas inversos são tipicamente **ill-posed** 
    - Problemas **well-posed** têm sempre solução única e estável.
    - Em ML a estabilidade não é respeitada, denominando-se os problemas de ill-posed.
    - Também temos o termo *ill-conditioning*.
- Isto ocorre porque podemos ter um número elevado de parâmetros desconhecidos em comparação com o número de dados. Assim, conforme escolhemos grupos de dados distintos obtemos uma solução diferente.
    - Assim, não temos informação sufiicente para arranjar bons parâmetros. 
    - Neste caso o ruído e outliers também terão um elevado peso
    - Regularização ajuda neste caso.
        - Esta regularização, no caso linear, normalmente consiste em *restringir a norma* do parâmetro estimado
        - Para regressões mais complexas podemos criar uma *restrição da suavidade*

## Melhorar regressão
- O que vimos atrás (LS, etc) consiste em determinar um ou mais parâmetros $\boldsymbol{\theta}$. Vamos agora ver a mesma lógica para ajustes.

- Uma tarefa de ajuste não linear pode ser escrita como $\text{y}=g(\mathbf{x})+\eta$

- Vamos considerar que vamos fazer isto ML, usando um método de MSE.
- Temos os dados $\text{y}$ e as observações $\mathbf{x}=\boldsymbol{x}\in\mathbb{R}^{l}$. Queremos então determinar o ajuste não-linear $\hat{y}:=\hat{g}(\boldsymbol{x})$, tal que:
$$\hat{g}(\boldsymbol{x})=\text{argmin}_{f:\mathbb{R}^{l}\to\mathbb{R}}\mathbb{E}[(\text{y}-f(\boldsymbol{x}))^{2}]$$
($\hat{y}$ são os valores de ajuste ótimos)
- Ora, é possível demonstrar que.
$$\hat{g}(\boldsymbol{x})=\mathbb{E}[\text{y}|\boldsymbol{x}]:=\int_{-\infty}^{+\infty} y \cdot p(y|\boldsymbol{x})dy$$
    - Demonstração presente no PPT "Regressão Linear" (slide 34)

- Este resultado é elegante e é aquilo que às vezes se chama de "regressão de y conditionado em x". Em geral, isto resulta em $\hat{g}$ não-linear
    - No entanto, se $(\text{x},\boldsymbol{x})\in\mathbb{R}\times\mathbb{R}^{l}$ e juntos seguem uma distribuição gaussiana, então temos $\mathbb{E}[\text{x}|\boldsymbol{x}]$ *linear*.

*y vetor*
- Claro, tudo isto acima é generalizável para o caso em que temos $\mathbf{y}\in\mathbb{R}^{k}$:
$$\hat{\boldsymbol{g}}(\boldsymbol{x})=\mathbb{E}[\mathbf{y}|\boldsymbol{x}] \quad \quad(\hat{\boldsymbol{g}}(\boldsymbol{x})\in\mathbb{R}^{k})$$

*Explicação física*
- Consideremos que a variável de ruído tem média zero.
- Assim, para um certo valor $\mathbf{x}=\boldsymbol{x}$ temos $\mathbb{E}[\text{y}|\boldsymbol{x}]=g(\boldsymbol{x})$
- O MSE desse ajuste será
$$\text{MSE}=\mathbb{E} \left[ (\text{y}-\mathbb{E}[\text{y}|\boldsymbol{x}])^{2} \right]=\sigma_{\eta}^{2}$$
este será o melhor resultado possível - nunca podemos ter MSE menor que a variância do ruído - por essa razão chamamos a $\sigma_{\eta}^{2}$ a *incerteza intríseca* do sistema.

- Qualquer outra função $f(\boldsymbol{x})$ irá resultar em MSE maior, por u fator $(\mathbb{E}[\text{y}|\boldsymbol{x}]-f(\boldsymbol{x}))^{2}$.

*Tradeoff Bias-Variância*
- A estimativa ótima de $\text{y}$ é dada por $\mathbb{E}[\text{y}|\boldsymbol{x}]$
- Na prática, temos estimador baseado num conjunto de dados de treino $\mathcal{D}$. Como sabemos, a estimativa é dependente do data set, tendo-se $f(\boldsymbol{x};\mathcal{D})$
- Assim, podemos medir a performance de um estimador através do desvio Mean-Square do estimador ótimo, ou seja: $\mathbb{E}_\mathcal{D}[(f(\boldsymbol{x};\mathcal{D})-\mathbb{E}[\text{y}|\boldsymbol{x}])^{2}]$ (aqui, $\mathbb{E}$ é feito usando **todos** os datasets possíveis deste tamanho)
- Podemos acrescentar e subtrair $\mathbb{E}_\mathcal{D}[f(\boldsymbol{x};\mathcal{D})]$:
$$\begin{align*}
\mathbb{E}_\mathcal{D}[(f(\boldsymbol{x};\mathcal{D})-\mathbb{E}[y|\boldsymbol{x}])^{2}]&= \underbrace{\mathbb{E}_\mathcal{D}[(f(\boldsymbol{x};\mathcal{D})-\mathbb{E}_\mathcal{D}[f(\boldsymbol{x};\mathcal{D})])^{2}]}_\text{Variância}+\\
&+\underbrace{\mathbb{E}_{\mathcal{D}}[(\mathbb{E}_\mathcal{D}[f(\boldsymbol{x};\mathcal{D})]-\mathbb{E}[\text{y}|\boldsymbol{x}])^{2}]}_{\text{Bias}^{2}}
\end{align*}$$
(em que consideramos que o outro termo obtido ao expandir o quadrado tem média nula)
- Ora, o tradeoff bias-variância consiste no facto que é **impossível** diminuir os 2 termos acima em simultâneo!!! Para um número fixo de $N$ pontos do dataset  $\mathcal{D}$, diminunir o termo de variância aumenta o de bias e vice-versa.
    - Isto acontece porque para reduzir o bias temos que aumentar o número de parâmetros do estimador, o que aumenta a variância (obtemos overfitting)
- A única forma de diminuir os 2 em simultâneo é, claro, aumentar $N$. Além disso, será útil aumentar com cuidado a complexidade (para diminuir bias sem arriscar overfitting)

## Regra de Occam's Razor / Navalha de Ockham
- O tradeoff bias-variância é na realidade uma consequência de uma regra maior: regra de Occam's razor, que diz algo do género
    - "nunca devemos complicar a menos que necessário"
    - ou "a solução mais correta provavelmente será a mais simples"
- Também Dirac concordou com isto, dizendo "a teoria mais bonita matematicamente é mais provável estar correta".
- No caso de ML isto quer dizer: devemos escolher o ajuste que melhor **explica** dos dados, não um ajuste complexo que consegue **encaixar** os dados.

# Interpretação Probabilisitica de LMS
(LMS == Least Mean Squares )
- Vamos considerar que temos dados $(y_{n},\mathbf{x}_{n})$ e vamos considerar que se relacionam na forma $y_{n}=\theta^{T}\mathbf{x}_{n}+\epsilon_{n}$ ($\epsilon_{n}$ representa erro e ruido)
- Vamos assumir que $\epsilon_{n}\sim\mathcal{N}(0,\sigma^{2})$. Ou seja, $y_{n}\sim\mathcal{N}(\theta^{T}\mathbf{x}_{n},\sigma^{2})$
- Assim: $$p(y_{n}|\mathbf{x_{n}},\theta)=\frac{1}{\sqrt{2\pi}\sigma}\exp\left(- \frac{(y_{n}-\theta^{T}\mathbf{x}_{n})^{2}}{2\sigma^{2}}\right)$$
- Assumindo que os $\mathbf{x}_{n},y_{n}$ são independentes:
$$\begin{align*}
L(\theta)&= \prod_{n=1}^{B}p(y_{n}|\mathbf{x}_{n},\theta)\\
&= \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^{N}\exp\left(- \frac{\sum_{n=1}^{N}(y_{n}-\theta^{T}\mathbf{x}_{n})^{2}}{2\sigma^{2}}\right)
\end{align*}$$
- Calculando o log-likelihood:
$$l(\theta)=\ln L(\theta)=N\log\left(\frac{1}{\sqrt{2\pi}\sigma}\right)- \frac{1}{2\sigma^{2}}\sum\limits_{n=1}^{N}(y_{n}-\theta^{T}\mathbf{x}_{n})^{2}$$
    - Vemos que o último termo é $\frac{1}{2\sigma^{2}}\mathcal{L}(\theta)$
- Ou seja, assumindo que o ruído é gaussiano e que há independência, LMS é equivalente a determinar a estimativa de máxima likelihood.

# MAP
- Assumimos que $\theta$ segue uma distribuição a priori:
$$p(\theta)=\mathcal{N}(\mathbf{0},\sigma^{2}\mathbf{I})$$
- Pelo teorema de Bayes temos: $p(\theta|\mathbf{X},\mathbf{y})\propto p(\mathbf{y}|\mathbf{X},\theta)p(\theta)$

- Assim, usando a distribuição *a priori* ($p(\theta)$) e a função $p(\mathbf{y}|\mathbf{X},\theta)$ conseguimos determinar $p(\theta|\mathbf{X},\mathbf{y})$ - a distribuição *a posteriori*. Ora, ao maximizar esta última podemos determinar $\theta$.
    - Ao calcular o log negativo desta função é possível verificar que arranjar o máximo desta corresponde a minimizar o erro da Regressão de Ridge
- A esta técnica chamamos *MAP* - maximum a posteriori

*Como?*
1. Em MAP consideramos $\theta$ um VeA (não um parâmetro), descrito pela PDF $p(\theta)$ que conhecemos.
2. Temos $$\mathbf{X}=\begin{pmatrix}\mathbf{x}_{1}^{T} \\ \mathbf{x}_{2}^{T} \\ \vdots \\ \mathbf{x}_{N}^{T}\end{pmatrix}$$
3. Do teorema de Bayes: $$p(\theta|\mathbf{X})=\frac{p(\mathbf{X}|\theta)p(\theta)}{p(\mathbf{X})}$$
4. $\theta$ será dado por $$\theta_\text{MAP} = \text{argmax}_{\theta} p(\theta|\mathbf{X})$$
# Regressão de Bayes
- A *probabilidade posterior* é algo que podemos fazer ao examinar os dados e consiste em estimar a densidade de probabilidade de $\theta$: $p(\theta)$
- Uma escolha comum é $p(\theta)=\mathcal{N}(\mathbf{0},\rho^{2}\mathbf{I})$
- Do teorema de Bayes: $p(\theta|\mathbf{X},\mathbf{y})\propto p(\mathbf{y}|\mathbf{X},\theta)p(\theta)$
- Assim:
$$\begin{align*}
p(\theta|\mathbf{x},\mathbf{y})&\propto \prod_{n=1}^{N}p(y_{n}|\mathbf{x}_{n},\theta)p(\theta)=\\
&= \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^{N}\exp\left(- \frac{\sum_{n=0}^{N}(y_{n}-\theta^{T}\mathbf{x}_{n})^{2}}{2\sigma^{2}}\right) \frac{1}{\sqrt{2\pi}\sigma}\exp\left(- \frac{\theta^{T}\theta}{2\rho^{2}}\right)\\
&= \left(\frac{1}{\sqrt{2\pi}\sigma}\right)^{N}\exp\left(- \frac{\sum_{n=0}^{N}(\mathbf{y}-\mathbf{X}\theta)^{T}(\mathbf{y}-\mathbf{X}\theta)}{2\sigma^{2}}\right) \frac{1}{\sqrt{2\pi}\sigma}\exp\left(- \frac{\theta^{T}\theta}{2\rho^{2}}\right)
\end{align*}$$
- E podemos deduzir que
$$p(\theta|\mathbf{X},\mathbf{y})\sim N(\boldsymbol{\mu},\boldsymbol{\Sigma})$$
em que
$$\boldsymbol{\Sigma}^{-1}=\frac{\mathbf{I}}{\rho^{2}}+ \frac{\mathbf{X}^{T}\mathbf{X}}{\sigma^{2}}\quad ;\quad \boldsymbol{\mu}=\frac{\boldsymbol{\Sigma}\mathbf{X}^{T}\mathbf{y}}{\sigma^{2}}$$
