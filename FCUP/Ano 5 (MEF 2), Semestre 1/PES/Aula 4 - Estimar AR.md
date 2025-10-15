# Estimação de densidade espectral
## Intro
- Este processo é essencial para fazer processamento estatístico de sinal e é aplicado em várias áreas:
    - telecomunicações
    - processamento de áudio
    - geofísica
- A densidade espectral consiste na distribuição da energia do sinal pelas suas frequências: ou seja, é uma transformada de Fourier
    - Isto permite-nos determinar fenómenos periódicos (temos frequências com muita energia)
    - Ao zerar parte da densidade podemos remover ruído

## Métodos
- Temos métodos **paramétricos**;
    - Baseando-se em modelos AR, MA e ARMA
    - Que podemos usar quando temos poucos dados mas conhecemos minimamente o modelo do processo estocástico
- E temos os **não paramétricos**:
    - Não fazemos suposições sobre o processo
    - Temos mais flexibilidade e maior eficiência computacional
    - Por outro lado, podemos ter muita variância e baixa resolução espectral

- Esta última desvantagem de métodos não paramétricos pode ser visualizada abaixo: (periodograma é um método não paramétrico)
![[Pasted image 20251013160434.png]]

## Paramétricos
### AR
- Temos a equação que define processos AR:
$$A(q^{-1})y(t)=e(t) \quad;\quad A(q^{-1})=1+a_{1}q^{-1}+\dots+a_{n}q^{-n}$$
e $e(t)$ é ruído branco com média nula e variância $\sigma^{2}$
- Como já vimos, modelos AR são estacionários. 
- E neste caso temos a densidade espectral:
$$y(t)=\frac{1}{A(q^{-1})}\quad\to\quad \Phi_{yy}(\omega)=\frac{\sigma^{2}}{|A(e^{-j\omega})|^{2}}$$
- Como tal, determinar a densidade espectral implica determinar os coeficientes $a_{1},\dots,a_{n}$

### AR : Yule-Walker
- Como vimos na aula anterior, podemos determinar os parâmetros $a_{i}$ do modelo AR a partir da sequência de autocovariância
- Consideremos o modelo AR(n) (AR de ordem $n$). Temos:
$$\small\begin{align*}
y(t)+a_{1}q^{-1}y(t)+a_{2}q^{-2}y(t)+\dots+ a_{n}q^{-n}y(t)&= e(t)\\
y(t)+a_{1}y(t-1)+a_{2}y(t-2)+\dots+a_{n}y(t-n)&= e(t)\\
y(t)y(t)+a_{1}y(t-1)y(t)+a_{2}y(t-2)y(t)+\dots+a_{n}y(t-n)y(t)&= e(t)y(t)\\
&\downarrow \text{calcular }\mathbb{E}\\
\lambda_{yy}(0)+a_{1}\lambda_{yy}(1)+a_{2}\lambda_{yy}(2)+\dots+a_{n}\lambda_{yy}(n)&= \lambda_{ye}(0)\\
\lambda_{yy}(0)+a_{1}\lambda_{yy}(1)+a_{2}\lambda_{yy}(2)+\dots+a_{n}\lambda_{yy}(n)&= \sigma^{2}
\end{align*}$$
- Se fizermos isto a multiplicar tudo por $y(t-1)$ e calcular o valor médio obtemos:
$$\begin{align*}
\lambda_{yy}(1) + a_{1}\lambda_{yy}(0) + a_{2}\lambda_{yy}(1)+\dots+a_{n}\lambda_{yy}(n-1)=0\\
a_{1}\lambda_{yy}(0) + a_{2}\lambda_{yy}(1)+\dots+a_{n}\lambda_{yy}(n-1)=-\lambda_{yy}(1)
\end{align*}$$
- Se repetirmos com $y(t-i)$ para $i=1,\dots,n$ e obtemos:
$$\begin{cases}
\lambda_{yy}(0)a_{1} + \lambda_{yy}(1)a_{2}+\dots+\lambda_{yy}(n-1)a_{n}= -\lambda_{yy}(1) \\
\lambda_{yy}(1)a_{1} + \lambda_{yy}(0)a_{2}+\dots+\lambda_{yy}(n-2)a_{n}= -\lambda_{yy}(2) \\
\quad \vdots \\
\lambda_{yy}(n-1)a_{1}+\lambda_{yy}(n-2)a_{2}+\dots+\lambda_{yy}(0)a_{n}=-\lambda_{yy}(n)
\end{cases}$$
e estas são as **equações de Yule-Walker**, que usamos para estimar $a_{1},\dots,a_{n}$.

#### Matrizes
- Podemos reescever este sistema de forma matricial:
$$\boxed{\boldsymbol{\Lambda}_{n}\boldsymbol{\theta}^{(n)} = - \boldsymbol{\lambda}_{1:n}}$$
em que temos:
$$\begin{align*}
\boldsymbol{\Lambda}_{n}&= \begin{pmatrix}\lambda_{yy}(0) & \lambda_{yy}(1) & \cdots & \lambda_{yy}(n-1)\\
\lambda_{yy}(1) & \lambda_{yy}(0) & \cdots & \lambda_{yy}(n-2)\\
\vdots & \vdots & \ddots & \vdots\\
\lambda_{yy}(n-1) & \lambda_{yy}(n-2) & \cdots & \lambda_{yy}(0)\end{pmatrix}\\
\boldsymbol{\theta}^{(n)}&= \begin{pmatrix}a_{1} & a_{2} & a_{3} & \cdots & a_{n}\end{pmatrix}^{T}\\
\boldsymbol{\lambda}_{1:n}&= \begin{pmatrix}\lambda_{yy}(1) &  \lambda_{yy}(2) & \cdots & \lambda_{yy}(n)\end{pmatrix}^{T}
\end{align*}$$
- Usando esta formulação, os parâmetros do estimador AR são dados por:
$$\boldsymbol{\theta}^{(n)}=- \boldsymbol{\Lambda}_{n}^{-1}\boldsymbol{\lambda}_{1:n}$$
- Na prática usamos estimativas de $\lambda_{yy}$

#### Variância
- Como vimos na aula anterior, a variância do ruído branco $e(t)$ é dada por
$$\sigma^{2}=\lambda_{yy}(0)+a_{1}\lambda_{yy}(1)+\dots+a_{n}\lambda_{yy}(n)$$

#### EXEMPLO
- Consideremos o seguinte processo estocástico que medimos:
![[Pasted image 20251014093648.png]]

- Determinamos a sequência de  autocovariância deste sinal em Matlab:
![[Pasted image 20251014093713.png]]

- Tendo isto, queremos determinar o **modelo AR que gera este sinal**. 
- Decidiu-se usar apenas os primeiros 4 termos da sequência:
$$\begin{align*}
\hat\lambda_{yy}(0)&= 8.1539\\
\hat\lambda_{yy}(1)&= 6.7480\\
\hat\lambda_{yy}(2)&= 3.3389\\
\hat\lambda_{yy}(3)&= -0.4452
\end{align*}$$
- Podemos definir a matriz das covariâncias:
$$\hat{\boldsymbol{\Lambda}}_{3}=\begin{pmatrix}\hat{\lambda}_{yy}(0) & \hat{\lambda}_{yy}(1) & \hat{\lambda}_{yy}(2) \\ \hat{\lambda}_{yy}(1) & \hat{\lambda}_{yy}(0) & \hat{\lambda}_{yy}(1) \\ \hat{\lambda}_{yy}(2) & \hat{\lambda}_{yy}(1) & \hat{\lambda}_{yy}(0)\end{pmatrix}=\begin{pmatrix}8.1539 & 6.7480 & 3.3389 \\ 6.7480 & 8.1539 & 6.7480 \\ 3.3389 & 6.7480 & 8.1539\end{pmatrix}$$
(notemos que $\hat\lambda_{yy}(3)$ NÃO aparece aqui)
- E temos o vetor de autocovariâncias:
$$\hat{\boldsymbol{\lambda}}_{1:3}=\begin{pmatrix}\hat{\lambda}_{yy}(1) \\ \hat{\lambda}_{yy}(2) \\ \hat{\lambda}_{yy}(3)\end{pmatrix}=\begin{pmatrix}6.7480 \\ 3.3389 \\ -0.4452\end{pmatrix}$$
(notemos que $\hat{\lambda}_{yy}(0)$ NÃO aparece aqui)

- E podemos determinar os parâmetros:
$$\begin{align*}
\hat{\boldsymbol{\theta}}&= \hat{\boldsymbol{\Lambda}}_{3}^{-1}\hat{\boldsymbol{\lambda}}_{1:3}\\
&= \begin{pmatrix}8.1539 & 6.7480 & 3.3389 \\ 6.7480 & 8.1539 & 6.7480 \\ 3.3389 & 6.7480 & 8.1539\end{pmatrix}^{-1} \begin{pmatrix}6.7480 \\ 3.3389 \\ -0.4452\end{pmatrix}\\
&= \begin{pmatrix}1.6480 & -2.5559 & 1.4404\\
-2.5559 & 4.3531 & -2.5559\\
1.4404 & -2.5559 & 1.6480\end{pmatrix}\begin{pmatrix}6.7480 \\ 3.3389 \\ -0.4452\end{pmatrix}\\
&= \begin{pmatrix}-1.9462\\
1.5755\\
-0.4523\end{pmatrix}
\end{align*}$$
- Ou seja, estimamos o modelo:
$$(1-1.9462q^{-1} + 1.5755q^{-2} - 0.4523q^{-3})y(t) = e(t)$$
e temos a variância de ruído branco:
$$\hat{\sigma}^{2}=\lambda_{yy}(0)+a_{1}\lambda_{yy}(1)+a_{2}\lambda_{yy}(2)+a_{3}\lambda_{yy}(3)=0.4825$$

##### Validar teórico
- Podemos calcular a sequência de autocovariância para a nossa estimativa AR:
![[Pasted image 20251014095401.png]]
- Vemos que as sequências sao identicas para $\tau=-3,\dots,3$ e que o erro vai aumentando com $\tau$. Isto faz sentido porque apenas usamos $|\tau|\le3$ para estimar o modelo
- Podemos fazer a seguinte comparação:
![[Pasted image 20251014095632.png]]
Em azul temos a densidade espectral determinada com os coeficientes estimados $\Phi(\omega)=\sum_{\tau}\lambda_{yy}(\tau)e^{-j\omega}$, a laranja temos a densidade teórica $\Phi(\omega)=\frac{\sigma^{2}}{|A(j\omega)|^{2}}$

##### Erro de estimação 
![[Pasted image 20251014100143.png]]
- Aqui vemos o sinal $y$, a estimativa $\hat{y}$ e o erro $\hat{e}=y-\hat{y}$
- Ao calcular a variância do erro de estimação temos $\mathbb{E}[\hat{e}^{2}(t)]=0.8759$, que é bastante **maior que** a variância de ruído branco estimada 
    - Notemos que o ruído branco será o erro num caso ideal: a única fonte de erro que nunca podemos controlar é o ruído branco e a sua aleatoriedade

### Levinson-Durbin
- Ora, vimos que as equações de Yule-Walker se resumem a: $\boldsymbol{\Lambda}_{n}\boldsymbol{\theta}^{(n)}=-\boldsymbol{\lambda}_{1:n}$
- Observemos melhor a matriz das covariâncias:
$$\small
\begin{pmatrix}
\textcolor{red}{\lambda_{yy}(0)} & \textcolor{blue}{\lambda_{yy}(1)} & \textcolor{green!60!black}{\lambda_{yy}(2)} & \textcolor{orange}{\lambda_{yy}(3)} & \cdots & \textcolor{purple}{\lambda_{yy}(n-2)} & \textcolor{teal}{\lambda_{yy}(n-1)} \\
\textcolor{blue}{\lambda_{yy}(1)} & \textcolor{red}{\lambda_{yy}(0)} & \textcolor{blue}{\lambda_{yy}(1)} & \textcolor{green!60!black}{\lambda_{yy}(2)} & \cdots & \textcolor{orange}{\lambda_{yy}(n-3)} & \textcolor{purple}{\lambda_{yy}(n-2)} \\
\textcolor{green!60!black}{\lambda_{yy}(2)} & \textcolor{blue}{\lambda_{yy}(1)} & \textcolor{red}{\lambda_{yy}(0)} & \textcolor{blue}{\lambda_{yy}(1)} & \cdots & \textcolor{green!60!black}{\lambda_{yy}(n-4)} & \textcolor{orange}{\lambda_{yy}(n-3)} \\
\textcolor{orange}{\lambda_{yy}(3)} & \textcolor{green!60!black}{\lambda_{yy}(2)} & \textcolor{blue}{\lambda_{yy}(1)} & \textcolor{red}{\lambda_{yy}(0)} & \cdots & \textcolor{blue}{\lambda_{yy}(n-5)} & \textcolor{green!60!black}{\lambda_{yy}(n-4)} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
\textcolor{purple}{\lambda_{yy}(n-2)} & \textcolor{orange}{\lambda_{yy}(n-3)} & \textcolor{green!60!black}{\lambda_{yy}(n-4)} & \textcolor{blue}{\lambda_{yy}(n-5)} & \cdots & \textcolor{red}{\lambda_{yy}(0)} & \textcolor{blue}{\lambda_{yy}(1)} \\
\textcolor{teal}{\lambda_{yy}(n-1)} & \textcolor{purple}{\lambda_{yy}(n-2)} & \textcolor{orange}{\lambda_{yy}(n-3)} & \textcolor{green!60!black}{\lambda_{yy}(n-4)} & \cdots & \textcolor{blue}{\lambda_{yy}(1)} & \textcolor{red}{\lambda_{yy}(0)}
\end{pmatrix}$$
- Com as cores assinaladas, conseguimos ver que os elementos das diagonais são todos iguais!! 
- Além disso, na diagonal $i$ acima (ou abaixo) da diagonal principal temos o valor $\lambda_{yy}(\tau=i)$
- Estas caraterísticas dizem-nos que $\boldsymbol{\Lambda}_{n}$ é uma **matriz de Toeplitz**!
- Temos ainda que a matriz é igual acima e abaixo da diagonal principal: é **simétrica**
- Ou seja, a matriz de covariâncias é de Toeplitz simétrica

#### Vantagens de Levinson-Durbin
- Ora, como sabemos que a matriz de covariâncias tem propriedades tão específicas, será inteligente usar um algoritmo que se aproveite delas: o algoritmo de Levinson-Durbin faz precisamente isso 
- Por causa disto, o algoritmo tem complexidade de tempo $n^{2}$ 
    - Isto quer dizer que o tempo de execução do progama aumenta proprocionalmente a $n^{2}$, em que $n$ é a dimensão da da matriz
    - Por exemplo, Gauss-Jordan é o algoritmo para resolver sistemas "normai" e tem complexidade $n^{3}$
- Este método permite calcular recursivamente os parâmetros AR de ordem $1$ até $n$. Isto significa que podemos ir testando ordens, sem ter que recomeçar todos os cálculos ao decidir mudar a ordem

#### Notação
- Introduzimos um "expoente" na notação dos coeficiente e do modelo:
$$A^{(k)}(q^{-1})=1+a_{1}^{(k)}q^{-1} + \dots + a_{k}^{(k)}q^{-k}$$
em que $(k)$ é a **ordem** em que estamos a calcular: para AR(1) temos apenas $a_{1}^{(1)}$, mas para AR(2) temos $a_{1}^{(2)},a_{2}^{(2)}$. O algoritmo calcula tudo de forma recursivamente e precisamos de guardar a que ordem corresponde o quê.
- Isto está relacionado com o facto que o índice $a_{3}$ de ordem $k=4$ NÃO será o mesmo que $a_{3}$ de ordem $k=10$, porque temos mais termos a interagir.
- Por palavras, o algoritmo calcula 
$$\boldsymbol{\theta}^{(k+1)}=\begin{pmatrix}a^{(k+1)}_{1} & a^{(k+1)}_{2} & \dots & a^{(k+1)}_{k} & a^{(k+1)}_{k+1}\end{pmatrix}^{T}$$
usando 
$$\boldsymbol{\theta}^(k)=\begin{pmatrix}a^{(k)}_{1} & a^{(k)}_{2} & \dots & a^{(k)}_{k}\end{pmatrix}$$
notemos, claro, que temos $n$ parâmetros na ordem $n$.

#### Primeiro passo
- As equações de Yule-Walker reduzem-se simplesmente a 1 equação quando temos $k=1$ (ordem 1):
$$a_{1}^{(1)}\lambda_{yy}(0)= - \lambda_{yy}(1)~~\to~~ \boldsymbol{\theta}^{(1)}=\begin{pmatrix}a_{1}^{(1)}\end{pmatrix}=\begin{pmatrix}\frac{-\lambda_{yy}(1)}{\lambda_{yy}(0)}\end{pmatrix}$$

#### Estrutura de Toeplitz
- Voltemos à estrutura da matriz de covariâncias

$$\boldsymbol{\Lambda}_{k+1}=\left[\begin{array}{ccccc|c}
\lambda_{yy}(0) & \lambda_{yy}(1) & \lambda_{yy}(2) & \cdots & \lambda_{yy}(k-1) & \lambda_{yy}(k) \\
\lambda_{yy}(1) & \lambda_{yy}(0) & \lambda_{yy}(1) & \cdots & \lambda_{yy}(k-2) & \lambda_{yy}(k-1) \\
\lambda_{yy}(2) & \lambda_{yy}(1) & \lambda_{yy}(0) & \cdots & \lambda_{yy}(k-3) & \lambda_{yy}(k-2) \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
\lambda_{yy}(k-1) & \lambda_{yy}(k-2) & \lambda_{yy}(k-3) & \cdots & \lambda_{yy}(0) & \lambda_{yy}(1) \\
\hline
\lambda_{yy}(k) & \lambda_{yy}(k-1) & \lambda_{yy}(k-2) & \cdots & \lambda_{yy}(1) & \lambda_{yy}(0)
\end{array}\right]$$
- Se olharmos bem para a porção superior esquerda, vemos que ela não passa da matriz $\boldsymbol{\Lambda}_{k}$, a matriz de covariância da ordem anterior!!
- Notamos que os cantos superior direito e inferior esquerdo são o mesmo vetor, transposto. Este consiste apenas uma lista de autocovariâncias, ou seja: $\boldsymbol{\lambda}_{k:1}$
- No canto inferior direito simplesmente temos $\lambda_{yy}(0)$ isolado
- Juntando tudo:
$$\boldsymbol{\Lambda}_{k+1}=\left[\begin{array}{c|c}\boldsymbol{\Lambda}_{k} & \boldsymbol{\lambda}_{k:1}\\
\hline\boldsymbol{\lambda}_{k:1}^{T} & \lambda_{yy}(0)\end{array} \right]$$
- Notemos que:
$$\boldsymbol{\Lambda}_{k}\boldsymbol{\theta}^{(k)}=- \boldsymbol{\lambda}_{1:k}$$

#### Atualizar parâmetros
- Podemos definir:
$$\boldsymbol{\theta}^{(k+1)}= \left[\begin{array}{c}\boldsymbol{\theta}^{(k)}\\ \hline 0
\end{array} \right] + \left[\begin{array}{c}\boldsymbol{\epsilon}_{k}\\ \hline a_{k+1}^{(k+1)}
\end{array} \right]$$
em que $\boldsymbol{\epsilon}_{k}$ é um vetor que possui a variação de $\boldsymbol{\theta}^{(k)}$ ao passar para $\boldsymbol{\theta}^{(k+1)}$
- Podemos então escrever o sistema de Yule-Walker na forma:
$$\left[\begin{array}{c|c}\boldsymbol{\Lambda}_{k} & \boldsymbol{\lambda}_{k:1}\\ \hline \boldsymbol{\lambda}_{k:1}^{T} & \lambda_{yy}(0)\end{array}\right] \left(\left[\begin{array}{c}\boldsymbol{\theta}^{(k)}\\ \hline 0
\end{array} \right] + \left[\begin{array}{c}\boldsymbol{\epsilon}_{k}\\ \hline a_{k+1}^{(k+1)}
\end{array} \right] \right)=- \left[ \begin{array}{c}\boldsymbol{\lambda}_{1:k} \\ \hline \lambda_{yy}(k+1)\end{array} \right]$$
podemos desenvolver isto com produto de matrizes normal:
$$\begin{align*}
\left[\begin{array}{c|c}\boldsymbol{\Lambda}_{k} & \boldsymbol{\lambda}_{k:1}\\ \hline \boldsymbol{\lambda}_{k:1}^{T} & \lambda_{yy}(0)\end{array}\right]\left[\begin{array}{c}\boldsymbol{\theta}^{(k)}\\ \hline 0
\end{array} \right] + \left[\begin{array}{c|c}\boldsymbol{\Lambda}_{k} & \boldsymbol{\lambda}_{k:1}\\ \hline \boldsymbol{\lambda}_{k:1}^{T} & \lambda_{yy}(0)\end{array}\right]\left[\begin{array}{c}\boldsymbol{\epsilon}_{k}\\ \hline a_{k+1}^{(k+1)}
\end{array} \right]&= - \left[ \begin{array}{c}\boldsymbol{\lambda}_{1:k} \\ \hline \lambda_{yy}(k+1)\end{array} \right]\\
\left[\begin{array}{c|c} \boldsymbol{\Lambda}_{k}\boldsymbol{\theta}^{(k)} + 0\cdot \boldsymbol{\lambda}_{k:1} \\ \hline \boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\theta}^{(k)} + 0\cdot \lambda_{yy}(0) \end{array} \right] + \left[\begin{array}{c|c} \boldsymbol{\Lambda}_{k}\boldsymbol{\epsilon}_{k} + a_{k+1}^{(k+1)} \boldsymbol{\lambda}_{k:1} \\ \hline \boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\epsilon}_{k} + a_{k+1}^{(k+1)} \lambda_{yy}(0) \end{array} \right]&= - \left[ \begin{array}{c}\boldsymbol{\lambda}_{1:k} \\ \hline \lambda_{yy}(k+1)\end{array} \right]\\
\end{align*}$$
- Separando a parte de sima e de baixo das matrizes:
$$\begin{cases}
\boldsymbol{\Lambda}_{k}\boldsymbol{\theta}^{(k)} + \boldsymbol{\Lambda}_{k}\boldsymbol{\epsilon}_{k} + a_{k+1}^{(k+1)} \boldsymbol{\lambda}_{k:1} = - \boldsymbol{\lambda}_{k:1}\\
\boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\theta}^{(k)}+\boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\epsilon}_{k} + a_{k+1}^{(k+1)}\lambda_{yy}(0)=-\lambda_{yy}(k+1)
\end{cases}$$
- Notemos que a primeira equação é vetorial e a segunda é escalar 
- Acima vimos que $\boldsymbol{\Lambda}_{k}\boldsymbol{\theta}^{(k)}=- \boldsymbol{\lambda}_{1:k}$. Utilizando isso aqui temos:
$$\begin{align*}
\boldsymbol{\Lambda}_{k}\boldsymbol{\theta}^{(k)} + \boldsymbol{\Lambda}_{k}\boldsymbol{\epsilon}_{k} + a_{k+1}^{(k+1)} \boldsymbol{\lambda}_{k:1} &=  - \boldsymbol{\lambda}_{k:1}\\
\cancel{\boldsymbol{\Lambda}_{k}\boldsymbol{\theta}^{(k)}} + \boldsymbol{\Lambda}_{k}\boldsymbol{\epsilon}_{k} + a_{k+1}^{(k+1)} \boldsymbol{\lambda}_{k:1} &= \cancel{\boldsymbol{\Lambda}_{k} \boldsymbol{\theta}^{(k)}}\\
\boldsymbol{\Lambda}_{k}\boldsymbol{\epsilon}_{k}&= - a_{k+1}^{(k+1)}\boldsymbol{\lambda}_{k:1}
\end{align*}$$
E precisamos de saber $\boldsymbol{\lambda}_{k:1}$

#### Yule-Walker ao contrário
- Vamos ver as equações de Yule-Walker *ao contrário*. 
    - "Ao contrário" significa inverter a ordem: na linha superior temos $\lambda_{yy}(k) + a_{1}^{(k)}\lambda_{yy}(k-1)+\dots+a_{k-1}^{(k)}+a_{k}^{(k)}\lambda_{yy}(0)=0$ e por aí fora
    - Vamos também inverter a ordem dos termos em cada linha: os termos aparecem de forma a termos $a_{k},a_{k-1},\dots,a_{2},a_{1}$
    - Já veremos porque raio estamos a fazer isto
- Ficamos então com:
$$\small\begin{cases}
\lambda_{yy}(0)a_{k}^{(k)} + \lambda_{yy}(1)a_{k-1}^{(k)}+\lambda_{yy}(2)a_{k-2}^{(k)}\dots+\lambda_{yy}(k-1)a_{1}^{(k)}=-\lambda_{yy}(k) \\
\lambda_{yy}(1)a_{k}^{(k)} + \lambda_{yy}(0)a_{k-1}^{(k)}+\lambda_{yy}(1)a_{k-2}^{(k)}\dots+\lambda_{yy}(k-2)a_{1}^{(k)}=-\lambda_{yy}(k-1) \\
\lambda_{yy}(2)a_{k}^{(k)} + \lambda_{yy}(1)a_{k-1}^{(k)}+\lambda_{yy}(0)a_{k-2}^{(k)}\dots+\lambda_{yy}(k-3)a_{1}^{(k)}=-\lambda_{yy}(k-2) \\
\quad\vdots \\
\lambda_{yy}(k-2)a_{k}^{(k)} + \lambda_{yy}(k-3)a_{k-1}^{(k)}+\dots+\lambda_{yy}(0)a_{2}^{(k)}+\lambda_{yy}(1)a_{1}^{(k)}=-\lambda_{yy}(2) \\
\lambda_{yy}(k-1)a_{k}^{(k)} + \lambda_{yy}(k-2)a_{k-1}^{(k)}+\dots+\lambda_{yy}(1)a_{2}^{(k)}+ \lambda_{yy}(0)a_{1}^{(k)}=-\lambda_{yy}(1)
\end{cases}$$

e podemos escrever isto de forma matricial:
$$\small\begin{bmatrix}\lambda_{yy}(0) & \lambda_{yy}(1) & \lambda_{yy}(2) & \cdots & \lambda_{yy}(k-1) \\ \lambda_{yy}(1) & \lambda_{yy}(0) & \lambda_{yy}(1) & \cdots & \lambda_{yy}(k-2) \\ \lambda_{yy}(2) & \lambda_{yy}(1) & \lambda_{yy}(0) & \cdots & \lambda_{yy}(k-3) \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ \lambda_{yy}(k-2) & \lambda_{yy}(k-3) & \cdots  & \lambda_{yy}(0) & \lambda_{yy}(1) \\ \lambda_{yy}(k-1) & \lambda_{yy}(k-2) & \cdots & \lambda_{yy}(1) & \lambda_{yy}(0) \end{bmatrix} \begin{bmatrix}a^{(k)}_{k} \\ a^{(k)}_{k-1} \\ a^{(k)}_{k-2} \\ \vdots \\ a^{(k)}_{2} \\ a^{(k)}_{1}\end{bmatrix}=- \begin{bmatrix}\lambda_{yy}(k) \\ \lambda_{yy}(k-1) \\ \lambda_{yy}(k-2) \\ \vdots \\ \lambda_{yy}(2) \\ \lambda_{yy}(1)\end{bmatrix}$$
- Notamos que a matriz de covariâncias ficou igual ao inverter o sistema, mas os dois vetores trocaram. Ou seja, ficamos com:
$$\boldsymbol{\Lambda}_{k}\boldsymbol{\theta}_{R}^{(k)}=-\boldsymbol{\lambda}_{k:1}$$
em que $\boldsymbol{\theta}_{R}$ é o vetor dos parâmetros com a ordem trocada ($a_{k},\dots,a_{1}$ quando em $\boldsymbol{\theta}$ temos $a_{1},\dots,a_{k}$) e $\boldsymbol{\lambda}_{k:1}$ é o vetor de autocovariâncias desde $\lambda_{yy}(k)$ até $\lambda_{yy}(1)$ 

#### Continuar dedução do algoritmo
- Ok, agora temos uma equação de $\boldsymbol{\lambda}_{k:1}$. Substituímos isto na equação para subir de $\boldsymbol{\epsilon}_{k}$ acima:
$$\begin{align*}
\boldsymbol{\Lambda}_{k}\boldsymbol{\epsilon}_{k}&= -a_{k+1}^{(k+1)} \boldsymbol{\lambda}_{k:1}\\
\boldsymbol{\Lambda}_{k}\boldsymbol{\epsilon}_{k}&=+ a_{k+1}^{(k+1)}\boldsymbol{\Lambda}_{k} \boldsymbol{\theta}_{R}^{(k)}\\
\boldsymbol{\epsilon}_{k}&= a_{k+1}^{(k+1)}\boldsymbol{\theta}_{R}^{(k)}\\
\end{align*}$$
e temos uma equação para $\boldsymbol{\epsilon}_{k}$!!!

- Assim, falta um último elemento: $a_{k+1}^{(k+1)}$, o último parâmetro da próxima ordem.

#### Última peça
- Pegamos na equação de $\boldsymbol{\epsilon}_{k}$ e multiplicamos os 2 lados à esquerda por $\boldsymbol{\lambda}_{k:1}^{T}$:
$$\begin{align*}
\boldsymbol{\epsilon}_{k}&= a_{k+1}^{(k+1)}\boldsymbol{\theta}_{R}^{(k)}\\
\boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\epsilon}_{k}&=\boldsymbol{\lambda}_{k:1}^{T} a_{k+1}^{(k+1)}\boldsymbol{\theta}_{R}^{(k)}\\
\boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\epsilon}_{k}&=\boldsymbol{\lambda}_{1:k}^{T} \boldsymbol{\theta}^{(k)} \cdot a_{k+1}^{(k+1)}\\
\end{align*}$$
em que no último passo usamos: $\boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\theta}_{R}^{(k)}=\boldsymbol{\lambda}_{1:k}^{T}\boldsymbol{\theta}^{(k)}$, uma equação relativamente intuitiva.

- Acima, obtivemos o seguinte sistema a partir de Yule-Walker:
$$\begin{cases}
\boldsymbol{\Lambda}_{k}\boldsymbol{\theta}^{(k)} + \boldsymbol{\Lambda}_{k}\boldsymbol{\epsilon}_{k} + a_{k+1}^{(k+1)} \boldsymbol{\lambda}_{k:1} = - \boldsymbol{\lambda}_{k:1}\\
\boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\theta}^{(k)}+\boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\epsilon}_{k} + a_{k+1}^{(k+1)}\lambda_{yy}(0)=-\lambda_{yy}(k+1)
\end{cases}$$
- Antes pegamos apenas na 1ª equação, vejamos agora a segunda (a equação escalar)
$$\boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\theta}^{(k)}+\boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\epsilon}_{k} + a_{k+1}^{(k+1)}\lambda_{yy}(0)=-\lambda_{yy}(k+1)$$
e substituímos $\boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\epsilon}_{k}=\boldsymbol{\lambda}_{1:k}^{T} \boldsymbol{\theta}^{(k)} \cdot a_{k+1}^{(k+1)}$, obtendo-se:
$$\boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\theta}^{(k)}+\boldsymbol{\lambda}_{1:k}^{T} \boldsymbol{\theta}^{(k)} a_{k+1}^{(k+1)} + a_{k+1}^{(k+1)}\lambda_{yy}(0)=-\lambda_{yy}(k+1)$$
e podemos isolar $a_{k+1}^{(k+1)}$:
$$\boxed{a_{k+1}^{(k+1)} = - \frac{\lambda_{yy}(k+1) + \boldsymbol{\lambda}_{k:1}^{T}\boldsymbol{\theta}^{(k)}}{\lambda_{yy}(0) + \boldsymbol{\lambda}_{1:k}^{T}\boldsymbol{\theta}^{(k)}}}$$
em que usamos apenas os parâmetros da ordem $k$ e o primeiro e último termos da sequência de autocovariância, que facilmente calculamos com Matlab.

#### RESUMO 
- **Passo 1:** Inicialização
$$\boldsymbol{\theta}_{1}^{(1)}=a_{1}^{(1)}=\frac{-\lambda_{yy}(0)}{\lambda_{yy}(1)}$$
- **Passo 2:** Recursão
    - Para uma certa ordem $k=1,\dots,n$ temos:
$$\begin{align*}
\text{Ultimo parâmetro próx ordem:} &&a_{k+1}^{(k+1)}&= - \frac{\lambda_{yy}(k+1) + \boldsymbol{\lambda}_{k:1}^{T} \boldsymbol{\theta}^{(k)}}{\lambda_{yy}(0) + \boldsymbol{\lambda}_{1:k}^{T} \boldsymbol{\theta}^{(k)}}\\
\\
\text{Vetor epsilon para próx ordem:} &&\boldsymbol{\epsilon}_{k}&= \boldsymbol{\theta}_{R}^{(k)}a_{k+1}^{(k+1)}\\
\\
\text{Parâmetros da próx ordem:} &&\boldsymbol{\theta}^{(k+1)}&= \left[\begin{array}{c}\boldsymbol{\theta}^{(k)}\\ \hline 0
\end{array} \right] + \left[\begin{array}{c}\boldsymbol{\epsilon}_{k}\\ \hline a_{k+1}^{(k+1)}
\end{array} \right]
\end{align*}$$
- A equação 3 foi escrita como vimos mais acima. No powerpoint está escrita desta forma:
$$\begin{bmatrix}a_{1}^{(k+1)} \\ \vdots \\ a_{k}^{(k+1)}\end{bmatrix} = \begin{bmatrix}a_{1}^{(k)} \\ \vdots \\ a_{k}^{(k)}\end{bmatrix} + a_{k+1}^{(k+1)}\begin{bmatrix}a_{k}^{(k)} \\ \vdots \\ a_{1}^{(k)}\end{bmatrix}$$
Presumo que seja para reforçar que $\boldsymbol{\theta}^{(k+1)}$ tem $k+1$ parâmetros pelo que o professor achou mais fácil escrever por extenso invés de fazer aquela cena com vetores.

### Estimador de erro de previsão
- Estas são ferramentas que estimam modelos paramétricos de processos estocásticos ou sistemas determinístico-estocásticos
- Ajustamos os parâmetros do sistema de forma a minimizar o erro (diferença entre previsões e valores previstos)
- Estes métodos são essenciais para reforçar e melhorar a estimativa

#### Propriedades
**Consistência**
- Estes estimadores são *consistentes*: as estimativas convergem para os valores reais consoante aumentamos o número de observações

**Optimo em processos gaussianos**
- Estes estimadores são *óptimos*: nenhuma estimador consegue minimizar o erro quadrático médio (MSE) dos parâmetros de modelos gaussianos

#### Estimador
##### Estimador AR
- Consideremos um processo estocástico AR $y(t)$. A nossa previsão será dada pelo estimador AR que vimos na aula 3:
$$\begin{align*}
\hat{y}(t,a_{1},\dots,a_{n})&= \hat{y}(t, \theta_{n})\\
&= [1 - A(q^{-1})] y(t)\\
&= -a_{1}y(t-1) - \dots - a_{n}y(t-n)
\end{align*}$$
e o erro de previsão é dado por
$$\hat{e}(t,\theta_{n})=y(t)- \hat{y}(t,\theta_{n})$$
(Aqui estou a usar a notação $\theta_{n}$ invés de $a_{1},\dots,a_{n}$ porque é mais curto e rápido de escrever)

##### Critério quadrático
- O critério quadrático é a função que mede o erro quadrático *total* e depende apenas dos parâmetros:
$$V(\theta_{n})=\frac{1}{2} \sum\limits_{t=1}^{N} \hat{e}^{2}(t, \theta_{n})$$
- Recordando Machine Learning, podemso minimizar isto ao fazer:
$$\Phi^{T}\Phi \hat\theta=\Phi^{T}Y$$
em que temos:
$$\Phi=\begin{pmatrix}-y(n) & -y(n-1) & \cdots & -y(1) \\ -y(n+1) & -y(n) & \cdots & -y(2) \\ \vdots & \vdots & \ddots & \vdots \\ -y(t-1) & -y(t-2) & \cdots & -y(t-n) \\ \vdots & \vdots & \ddots & \vdots \\ -y(N-1) & -y(N-2) & \cdots & -y(N-n)\end{pmatrix}\in \mathbb{R}^{(N-n)\times n}$$
em que temos $N$ observações ($N$ intervalos temporais) e estamos a estudar um modelo AR de ordem $n$

- Temos ainda o vetor:
$$Y=\begin{pmatrix}y(n+1) & y(n+2) & \cdots &  y(t) & \cdots & y(N)\end{pmatrix} \in \mathbb{R}^{N-n}$$
em que cada elemento $i$ corresponde ao valor de $y(t)$ que estamos a estimar na linha $i$ da matriz $\Phi$, usando a fórmula do estimador AR. Exemplo: $y(t)=-a_{1}y(t-1) - \dots - a_{n}y(t-n)$ 

- Ora, a solução deste sistema é dada por (assumindo que $\Phi^{T}\Phi$ não é singular):
$$\hat{\theta}= (\Phi^{T}\Phi)^{-1}\Phi^{T}Y$$

##### Yule-Walker???
- Ora, isto relaciona-se com Yule-Walker. Podemos escrever a equação de $\hat{\theta}$ na forma:
$$\hat{\theta}= \left(\frac{1}{N-n}\Phi^{T}\Phi \right)^{-1} \frac{1}{N-n}\Phi^{T}Y$$
em que:
$$\begin{align*}
\frac{1}{N-n}\Phi^{T}\Phi&= \frac{1}{N-n} \begin{bmatrix}\sum\limits_{t=n}^{N-1}y^{2}(t) & \cdots &  \sum\limits_{t=n}^{N-1}y(t)y(t-n+1)\\
\sum\limits_{t=n-1}^{N-2}y(t)y(t+1) & \cdots & \sum\limits_{t=n-1}^{N-2}y(t)y(t-n+2)\\
\vdots & \ddots & \vdots\\
\sum\limits_{t=1}^{N-n}y(t)y(t+n-1) & \cdots & \sum\limits_{t=1}^{N-n}y^{2}(t)
\end{bmatrix}\\
&= \begin{bmatrix}\hat{\lambda}_{yy}(0) & \hat{\lambda}_{yy}(1) & \cdots & \hat{\lambda}_{yy}(n-1)\\
\hat{\lambda}_{yy}(1) & \hat{\lambda}_{yy}(0) & \cdots & \hat{\lambda}_{yy}(n-2)\\
\vdots & \vdots & \ddots & \vdots\\
\hat{\lambda}_{yy}(n-1) & \hat{\lambda}_{yy}(n-2) & \cdots & \hat{\lambda}_{yy}(0)\end{bmatrix}\\
&= \hat{\boldsymbol{\Lambda}}_{n}
\end{align*}$$
e igualmente com a outra parcela:
$$\frac{1}{N-n}\Phi^{T}Y=\frac{-1}{N-n} \begin{bmatrix}\sum\limits_{t=n}^{N-1}y(t)y(t+1) \\ \sum\limits_{t=n-1}^{N-2}y(t)y(t+2) \\ \vdots \\ \sum\limits_{t=1}^{N-n}y(t)y(t+n)\end{bmatrix}=\begin{bmatrix}\hat{\lambda}_{yy}(1) \\ \hat{\lambda}_{yy}(2) \\ \vdots \\ \hat{\lambda}_{yy}(n)\end{bmatrix}=\hat{\boldsymbol{\lambda}}_{1:n} $$

**Ou seja...**
- Se tivermos um elevado número de observações ($N\to\infty$) então as "estimativas" do método de erro de previsão passam a ser efetivamente os valores teóricos. Logo:
$$\hat{\theta}=\hat{\boldsymbol{\Lambda}}_{n}^{-1}\hat{\boldsymbol{\lambda}}_{1:n} ~~~~\substack{\longrightarrow\\N\to\infty}~~~~ \theta=\boldsymbol{\Lambda}_{n}^{-1}\boldsymbol{\lambda}_{1:n}$$

### Correlação parcial
- Veremos agora algo que nos permite **determinar a ordem do modelo AR**
- Como sabemos, um processo AR é modelado como sendo uma combinação linear de valores anteriores de $y(t)$. Sabemos ainda que a ordem do modelo simplesmente indica o quão atrás vamos buscar valores de $y(t)$
- A função de correlação determina a influência de cada termo $y(t-i)$ sobre $y(t)$. Se a influência for suficientemente baixa, paramos de aumentar a ordem.
- Ou seja, a correlação parcial determina a correlação direta entre 2 observações do processo, excluindo o efeito de todas as observações intermédias!

#### Autocorrelação parcial
- Determina a correlação entre $y(t)$ e $y(t-k)$ _sem os atrasos intermédios_
- Para $k=1$ temos
$$\phi_{yy}(1)=\rho_{yy}(1)=\frac{\mathbb{E}\{y(t)y(t-1)\}}{\sqrt{\mathbb{E}[y^{2}(t)]\mathbb{E}[y^{2}(t-1)]}}=\frac{\Lambda_{yy}(1)}{\lambda_{yy}(0)}$$

#### k=2 
- Neste caso temos:
$$y(t) + a_{1}y(t-1) + a_{2}y(t-2)=e(t)$$
- Para isto dividimos $y(t)$ em 2  partes:
    - Relação de $y(t-1)$ em $y(t)$: $$y(t)=y(t-1)\hat{\alpha}_{1}^{(1)} + e_{0}^{(1)}(t)$$ 
        - Em que $y(t-1)\hat{\alpha}$ representa a parte de  correlacionada com $y(t)$. Por outras palavras, é a **porção de y(t) explicada** por $y(t-1)$ 
        - Já $e_{0}^{(1)}$ é o *erro de previsão*, ou seja, o erro que temos por considerar apenas a correlação com $y(t-1)$
        - Logo $e_{0}^{(1)}$ representa a parte de $y(t)$ NÃO correlacionada com $y(t-1)$. Assim, por definição temos $$\mathbb{E}[e_{0}^{(1)}(t)y(t-1)]=0$$
    - Relação entre $y(t-2)$ e $y(t-1)$: $$y(t-2)=y(t-1)\hat{\beta}_{1}^{(1)} + e_{2}^{(1)}(t)$$
        - Tal como acima, o termo $y(t-1)\hat{\beta}$ é a porção de $y(t-2)$ que se correlaciona com $y(t-1)$: é a parte de $y(t-2)$ que é explicada pela observação seguinte
        - E novamente, $e_{2}^{(1)}$ é o erro: é a parte de $y(t-2)$ que NÃO é explicada e não se correlaciona com $y(t-1)$. Por definição temos: $$\mathbb{E}[e_{2}^{(1)}(t)y(t-1)]=0$$

- Com esta informação, podemos calcular a correlação parcial entre $y(t)$ e $y(t-2)$:
$$\phi_{yy}(2)=\frac{\mathbb{E}\{ e_{0}^{(1)}(t)e_{2}^{(1)}(t) \}}{\sqrt{\mathbb{E}[e_{0}^{(1)}(t)^{2}]\mathbb{E}[e_{2}^{(1)}(t)^{2}]}}$$

#### Atraso genérico k
- Consideremos agora o caso genério: correlação parcial entre $y(t)$ e $y(t-k)$
- O objetivo é isolar o termo $y(t-k)$. Temos 2 partes iniciais:
    - Equação de $y(t)$: $$y(t) = \begin{bmatrix}y(t-1) & y(t-2) & \cdots & y(t-k+1)\end{bmatrix}\hat{\alpha}^{(k-1)} + e_{0}^{(k-1)}(t)$$
        - A primeira parcela identifica a correlação de $y(t)$ com todas as observações $y(t-1),\dots,y(t-k+1)$. 
        - Excluimos então o termo $y(t-k)$, cuja importância/correlação está inserida no termo $e_{0}^{(k-1)}(t)$
    - Equação de $y(t-k)$: $$y(t-k)=\begin{bmatrix}y(t-1) & y(t-2) & \cdots & y(t-k+1) \end{bmatrix}\hat{\beta}^{(k-1)}+e_{k}^{(k-1)}(t)$$
        - Agora o objetivo é inverso: temos na primeira parcela as correlações de $y(t-k)$ com todos os termos $y(t-1),\dots,y(t-k+1)$.
        - Assim excluimos o termo $y(t)$, que está inserido em $e_{k}^{(k-1)}(t)$

- E temos a correlação parcial:
$$\phi_{yy}(k)=\frac{\mathbb{E}\{ e_{0}^{(k-1)}(t)e_{k}^{(k-1)}(t) \}}{\sqrt{\mathbb{E}[e_{0}^{(k-1)}(t)^{2}]\mathbb{E}[e_{k}^{(k-1)}(t)^{2}]}}$$

- Ou seja, a lógica da dedução é:
    - Fazer uma equação em que temos $y(t)$ dividido entre correlação com $y(t-k)$ na função de erro e correlação com as outras observações na primeira parcela : A *primeira função de erro* descreve $y(t)$ através de $y(t-k)$
    - Fazer uma segunda equação com $y(t-k)$ dividido entre a correlação com $y(t)$ na função de rro e correlação com as restantes observações na primeira parcela: A *segunda função de erro* descreve $y(t-k)$ através de $y(t)$
    - Notemos que, por causa da forma como fazemos estas 2 divisões, as duas funções de erro NÃO se correlacionam com as observações entre $y(t)$ e $y(t-k)$
    - Conseguimos então definir a correlação entre 2 observações, nas duas "direções" e sem envolver os termos intermédios

#### Na prática
- Usamos as 2 equações acima para escrever $y(t)$ e $y(t-k)$ como regressões lineares de $y(t-1),\dots,y(t-k+1)$ 
- Para isso precisamos de determinar os coeficientes $\hat{\alpha}$ e $\hat{\beta}$, usando-se técnicas de **mínimos quadrados** - fazemos uma espécie de regressão
- As estimativas dos erros  $e_{0}^{(k-1)}(t)$ e $e_{k}^{(k-1)}(t)$ são os *resíduos* das estimações das duas equações
    - Ou seja, "fitamos" $y(t), y(t-k)$ com métodos LS e a função de erro é os resíduos do ajuste
- Como para determinar 1 correlação parcial precisamos de 2 funções de erro, então é fácil entender que para determinar $n$ correlações precisamos de $2n$ regressões lineares (faz sentido, temos 2 equações)

- As regressões resultam nos parâmetros:
$$\begin{align*}
\hat{\alpha}^{(k-1)}&= \left(\frac{1}{N-k-1} \left[X_{f}^{(k-1)}\right]^{T} X_{f}^{(k-1)} \right)^{-1}\frac{1}{N-k-1}\left[X_{f}^{(k-1)}\right]^{T}Y_{f}^{(k-1)}\\
\hat{\beta}^{(k-1)}&= \left(\frac{1}{N-k-1} \left[X_{b}^{(k-1)}\right]^{T} X_{b}^{(k-1)} \right)^{-1}\frac{1}{N-k-1}\left[X_{b}^{(k-1)}\right]^{T}Y_{b}^{(k-1)}
\end{align*}$$
e temos
$$\begin{align*}
X_{f}^{(k-1)}&= \begin{bmatrix}y(k-1)  & y(k-2) & \cdots & y(1)\\
y(k) & y(k-1) & \cdots & y(2)\\ \vdots & \vdots & \ddots & \vdots \\ y(N) & y(N-1) & \cdots & y(N-k+1) \end{bmatrix}\\\\
X_{b}^{(k-1)}&= \begin{bmatrix}y(N)  & y(N-1) & \cdots & y(N-k+2)\\ y(N-1) & y(N-2) & \cdots & y(N-k+1) \\ \vdots & \vdots & \ddots & \vdots \\ y(k) & y(k-1) & \cdots & y(2) \end{bmatrix}\\\\
Y_{f}^{(k-1)} &= \begin{bmatrix} y(k) & y(k+1) & \cdots & y(N) \end{bmatrix}^{T}\\\\
Y_{b}^{(k-1)} &= \begin{bmatrix}y(N-k+1)  & y(N-k) & \cdots & y(1) \end{bmatrix}^{T}
\end{align*}$$

#### Relação com Levinson-Durbin
- Temos um processo estacionário $y(t)$ com média nula. O coeficiente de autocorrelação parcial $\Phi_{yy}(k)$ entre $y(t)$ e $y(t-k)$ é dado por:
$$\Phi_{yy}(k)=-\alpha_{k}^{(k)}$$
sendo $\alpha^{(k)}=\begin{pmatrix}\alpha_{1}^{(k)} & \cdots & a_{k}^{(k)}\end{pmatrix}^{T}$

- Dedução enorme no Powerpoint
- Ou seja: se conhecermos o modelo AR(k) facilmente temos o coeficiente de correlação parcial: é o coeficiente da última observação $y(t-k)$

#### Conclusão
- A autocorrelação parcial é fundamental para determinar a ordem AR(k)
- O coeficiente de correlação parcial $\phi_{yy}(k)$ é igual a $-a_{k}^{(k)}$ - o simétrico do último parâmetro do modelo AR de ordem $k$
- Podemos usar o algoritmo de Levinson-Durbin para calcular estes coeficientes de autocorrelação, já que calculá-los não passa de calcular o modelo de ordem $k$ que melhor se ajusta ao processo.