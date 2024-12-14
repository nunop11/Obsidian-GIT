## 1.1 v0
(identificar parâmetros)
Temos que $y$ é a label de cada classe. Logo: $y=0,\dots,5$ e portanto $i=1,\dots,6$. 
Por sua vez temos 1119 observações, cada uma com 11 atributos. Assim: $j=1,\dots,1119$. Poderemos considerar os atributos dentro de cada observação como $x_{ij}$ com $i=1,\dots,11$.
Sabemos que $P(\textbf{x}|y)$ tem distribuição gaussiana, tal que $P(\mathbf{x}|y_{i})=\frac{1}{\sqrt{2\pi}\Sigma}\exp(- \frac{(x-\mu_{i})^{2}}{2\Sigma^{2}})$. A média $\mu_{i}$ de cada classe e a covariância $\Sigma$ (que é total para todas as classes) e depois os priors são calculados na função `fit`.
Ou seja: os parâmetros usados neste modelo são: $\mu_{i},\Sigma,P(\mathbf{x}|y_{i})$.

(identificar estimador)
Para classificar os dados precisamos das probabilidades posterior: $P(y|\textbf{x})$. Pelo teorema de Bayes:
$$p(y|\textbf{x})=\frac{P(\mathbf{x}|y)P(y)}{P(\mathbf{x})}$$
que podemos escrever como
$$P(y_{i}|x_{1}\dots x_{n})=\frac{P(x_{1}\dots x_{n}|y_{i})P(y_{i})}{\sum_{k} P(x_{1}\dots x_{n}|y_{k})P(y_{k})}$$
Assumindo que $x_{j}^{k},x_{j}^{m}$ ($k\neq m$) são condicionalmente independentes temos:
$$P(y_{i}|\mathbf{x})=\frac{P(y_{i})\prod_{j}P(x_{j}|y_{i})}{\sum_{k}P(y_{k})\prod_{j}P(x_{j}|y_{k})}$$
Um estimador MAP consiste em
$$\hat{y}=\text{argmax}_{y}P(y|\mathbf{x})$$
pelo que basta usar a equação acima e ver qual é o $y$ associado ao máximo.

## ## 1.1
(identificar parâmetros)\
Temos que $y_k$ é a label da classe $k$. Logo: $y=0,\dots,5$ e portanto $k=1,\dots,6$. Esta variável é discreta.\
Temos ainda as observações $x_{ij}$, que são contínuas. Por sua vez existem 1119 observações, cada uma com 11 atributos. Assim: $j=1,\dots,1119$. Poderemos considerar os atributos dentro de cada observação como $x_{ij}$ com $i=1,\dots,11$.\
Tendo em conta o que temos acima, podemos definir $K=6,J=1119,N=11$. No programa iremos usar os valores da shape dos arrays.

Sabemos que $P(\textbf{x}|y)$ tem distribuição gaussiana e que a matriz de covariância é a mesma , ou seja: $P(\mathbf{x}_{i}|y_{k})=\frac{1}{\sqrt{2\pi}\Sigma}\exp(- \frac{(\mathbf{x}_{i}-\mu_{ik})^{2}}{2\Sigma^{2}})$.\
Ou seja: os parâmetros usados neste modelo são: $\mu_{i},\Sigma$.

(identificar estimador)\
Podemos determinar estes parâmetros com:
$$\mu_{ik}=\frac{1}{\sum_{j} \delta(y_{j}=y_{k})}\sum\limits_{j}x_{ij}\delta(y_{j}=y_{k})$$
$$\Sigma^{2}=\frac{\sum_{k} n_{k}\sigma_{k}^{2}}{J}~~~~,~~~~ n_{k}=\sum\limits_{j}\delta(y_{j}=y_{k})$$
usando estes podemos determinar $P(\mathbf{x}_{i}|y_{k})$.
  
Neste LDA queremos usar o método MAP, logo o estimador da classe de um uma observação nova $\mathbf{x}^{new}$ é:
$$y^{new}=\text{argmax}_{y_{k}}P(y=y_{k})\prod_{i}P(\mathbf{x}_{i}^{new}|y_{k})$$
que podemos ainda escrever como:
$$y^{new}=\text{argmax}_{y_{k}}\frac{\# D\{y=y_{k}\}}{|D|}\prod_{i=1}^{N} \frac{1}{(2\pi)^{\frac{D}{2}}|\Sigma|^{\frac{1}{2}}}\exp\left[- \frac{1}{2}(\mathbf{x}_{i}-\boldsymbol{\mu}_{ik})^{T}\Sigma^{-1}(\mathbf{x}_{i}-\boldsymbol{\mu}_{ik}) \right]$$

## 1.3
Pelo teorema de Bayes:
$$p(y|\textbf{x})=\frac{P(\mathbf{x}|y)P(y)}{P(\mathbf{x})}$$
que podemos escrever como
$$P(y_{k}|x_{1}\dots x_{n})=\frac{P(x_{1}\dots x_{n}|y_{i})P(y_{k})}{\sum_{j} P(x_{1}\dots x_{n}|y_{j})P(y_{j})}$$
Assumindo que $x_{j}^{k},x_{j}^{m}$ ($k\neq m$) são condicionalmente independentes temos:
$$P(y_{k}|\mathbf{x})=\frac{P(y_{k})\prod_{m}P(\mathbf{x}_{m}|y_{k})}{\sum_{j}P(y_{j})\prod_{m}P(\mathbf{x}_{m}|y_{j})}$$
Ora, sabemos que $P(x_{j}|y_{k})$ é gaussiana. Como na função `fit` determinamos as médias e covariância temos:
$$P(y_{k}|\mathbf{x})=\frac{P(y_{k})\prod_{m} N(\mathbf{x}_{m}, \mu_{mk}, \Sigma)}{\sum\limits_{j}P(y_{j})\prod_{m}N(\mathbf{x}_{m},\mu_{mj},\Sigma)}$$


