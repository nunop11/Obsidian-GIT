## Recordar ARMA
- Podemos descrever um processo ARMA como
$$A(q^{-1})y(t)=C(q^{-1})e(t)$$
e temos: $A(q^{-1})=1+a_{1}q^{-1}+\dots+a_{n}q^{-n}~,~C(q^{-1})=1+c_{1}q^{-1}+\dots+c_{m}q^{-m}$ e $e(t)$ é ruído branco de média nula e variância $\sigma^{2}$
- Notemos então que consideramos processos arma com ordem AR $n$ e ordem MA $m$ logo ARMA(n,m)

### Densidade Espectral
- Como sabemos, processos ARMA são estacionários logo podemos definir a densidade espectral com a equação:
$$\begin{align*}
\Phi_{yy}(\omega)&= |H(e^{-j\omega})|^{2} \Phi_{uu}(\omega)\\
&= \frac{|C(e^{-i\omega})|^{2}}{|A(e^{-j\omega})|^{2}}\sigma^{2}\\
&= \frac{|1+c_{1}e^{-j\omega}+\dots+c_{m}e^{-j\omega m}|^{2}}{|1+c_{1}e^{-j\omega} + \dots+a_{n}e^{-j\omega n}|^{2}}\sigma^{2}
\end{align*}$$
logo se conseguirmos estimar $A,C$ (e os seus parâmetros) temos a densidade espectral do processo ARMA.
- Dito isto, este é uma tarefa complicada por termos que conjudar processos de 2 naturezas distintas.

## Método dos esfasamentos superiores
- Este método permite estimar os parâmetros AR(n) de forma a excluir a influência da parte MA(m)
- Obtemos os coeficientes AR com as equações de Yule-Walker.
    - Multiplicamos os 2 lados da equação ARMA por $y(t-\tau)~,~\tau>m$
    - Calculamos o valor médio, ficando com equações de autocovariâncias

- Vejamos como exemplo o caso em que multiplicamos por $y(t-1)$:
$$\Tiny\begin{align*}
y(t)+a_{1}y(t-1)+a_{2}y(t-2)+\dots&= e(t)+c_{1}e(t-1)+c_{2}e(t-2)+\dots\\
y(t)y(t-1)+a_{1}y(t-1)^{2}+a_{2}y(t-1)y(t-2)+\dots&= e(t)y(t-1) + c_{1}e(t-1)y(t-1)+c_{2}e(t-2)y(t-1)+\dots\\
\lambda_{yy}(1)+a_{1}\lambda_{yy}(0)+a_{2}\lambda_{yy}(1)+\dots&= \lambda_{ye}(1)+c_{1}\lambda_{ye}(0)+c_{2}\lambda_{ye}(1)+\dots\\
\lambda_{yy}(1)+a_{1}\lambda_{yy}(0)+a_{2}\lambda_{yy}(1)+\dots&=c_{1}\lambda_{ye}(0)\\
\lambda_{yy}(1)+a_{1}\lambda_{yy}(0)+a_{2}\lambda_{yy}(1)+\dots&=c_{1}\sigma^{2}\\
\end{align*}$$
- Mas nós queremos determinar $a_{1},a_{2},\dots$ SEM o efeito do modelo MA. Assim, fazemos isto apenas para $\tau>m$
    - O lado direito da equação será $e(t)+c_{1}e(t-1)+\dots+c_{m}e(t-m)$
    - Temos $\mathbb{E}[y(t-a)e(t-b)]=\lambda_{ye}(|a-b|)$ e $\lambda_{ye}(0)=\sigma^{2}~,~\lambda_{ye}(\tau\neq0)=0$. 
    - Assim, para garantir que não temos nenhum termo do lado direito diferente de zero, usamos $\tau>m$, pelo que nunca teremos um produto $y(\cdot)\times e(\cdot)$ em que temos esfasamento nulo. Por começarmos com $\tau$ elevado usamos o termo de *esfasamentos superiores*!

- As equações YW ficam:
$$\begin{cases}
a_{1}\lambda_{yy}(m) + a_{2}\lambda_{yy}(m-1)+\dots+a_{n}\lambda_{yy}(m+1-n)=-\lambda_{yy}(m+1) \\
a_{1}\lambda_{yy}(m+1) + a_{2}\lambda_{yy}(m)+\dots+a_{n}\lambda_{yy}(m+1-n)=-\lambda_{yy}(m+2) \\
~~\vdots \\
a_{1}\lambda_{yy}(m+n) + a_{2}\lambda_{yy}(m+n-1)+\dots+a_{n}\lambda_{yy} (m)= -\lambda_{yy}(m+n+1)
\end{cases}$$
- Os resíduos desta estimação AR seguem um modelo MA. Ou seja, se determinarmos o modelo AR com estas equações, depois podemos estimar a parte MA com os métodos que vimos atrás aplicados aos resíduos.

## Ajuste da Resposta Impulsional
- Seguimos um método semelhante ao método da resposta impulsional que usamos em MA
    - Aproximamos o processo a um modelo AR(p) truncado
    - Igualamos os primeiros $n+m+1$ valores da resposta impulsional ARMA(m,n) com os termos da aproximação AR(p)
    - Invés disso, podemos fazer estimadores de mínimos de mínimos quadrados para aproximar um número de termos *maior* que $n+m+1$
- Seja $h(0),h(1),\dots,h(n+m)$ a resposta impulsional da aproximação AR(p)

**Modelo ARMA(n,m)**
- Podemos escrever a resposta impulsional do modelo como:
$$y(t)=e(t)+c_{1}e(t-1)+\dots+c_{m}e(t-m)-a_{1}y(t-1)-\dots-a_{n}y(t-n)$$
- Na resposta impulsional temos a entrada $e(t)=\delta(t)=\begin{cases}1 & , & t=0 \\ 0 & , & t\neq 0\end{cases}$
- E temos:
$$\begin{align*}
h(0)&= e(0)=1\\
h(1)&= c_{1}-a_{1}h(0)\\
h(2)&= c_{2}-a_{1}h(1)-a_{2}h(0)\\
&\vdots\\
h(m)&=-c_{m}-a_{1}h(m-1)-a_{2}h(m-2)-\dots-a_{m}h(0)\\
&\vdots\\
h(n+m)&= -a_{1}h(n+m-1)-\dots-a_{n}h(m)
\end{align*}$$

### Cálculo de parâmetros
- Temos que:
$$\begin{align*}
&\left[\begin{array}{c|c}
\begin{array}{}\mathbf{I}_{m} \\ \hline \mathbf{0}_{n\times m}\end{array} & -\boldsymbol{\mathcal{H}}_{n+m}
\end{array}\right]\boldsymbol{\theta}= \boldsymbol{h}_{1:n+m}\\
&\boldsymbol{\theta}= \left[\begin{array}{c|c}
\begin{array}{}\mathbf{I}_{m} \\ \hline \mathbf{0}_{n\times m}\end{array} & -\boldsymbol{\mathcal{H}}_{n+m}
\end{array}\right]^{-1}\boldsymbol{h}_{1:n+m}
\end{align*}$$
- E podemos definir matriz:
$$\boldsymbol{\mathcal{H}}_{n+m}=\begin{bmatrix}1 & 0 & \cdots & 0 \\ h(1)  & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ h(n) & h(n-1) & \cdots & 1 \\ \vdots & \vdots & \ddots & \vdots \\ h(n+m) & h(n+m-1) & \cdots & h(m) \end{bmatrix}\in\mathbb{R}^{(n+m)\times n}$$
e temos o vetor de parâmetros
$$\boldsymbol{\theta}=\begin{bmatrix}c_{1} & \cdots & c_{m} & a_{1} & \cdots & a_{n}\end{bmatrix}^{T}\in \mathbb{R}^{n+m}$$
e a resposta impulsional em forma de vetor
$$\boldsymbol{h}_{1:n+m}=\begin{bmatrix} h(1) & \cdots & h(n+m) \end{bmatrix}^{T}\in \mathbb{R}^{n+m}$$

## Método de mínimos quadrados
- Expandimos o que fizemos com mínimos quadrados para modelos MA, agora para modelos ARMA
    - Aproximamos o modelo a um modelo AR(p)
    - Estimamos o modelo ARMA através do estimador de mínimos quadrados em que consideramos os resíduos como sinal de entrada
- Temos o modelo:
$$y(t)=\hat e(t)+c_{1}\hat e(t-1)+\dots+c_{m}\hat e(t-m)-a_{1}y(t-1)-\dots-a_{n}y(t-n)$$
em que $\hat{e}$ é a entrada, que são os resíduos.

**Componentes**
- Em forma vetorial temos
$$y(t)=\boldsymbol{\varphi}^{T}(t)\boldsymbol{\theta} + \hat{e}(t)$$
- Definimos:
$$\boldsymbol{\varphi}(t)=\begin{bmatrix} \hat{e}(t-1) \\ \vdots \\ \hat{e}(t-m) \\ -y(t-1) \\ \vdots \\ -y(t-n) \end{bmatrix}$$
$$\boldsymbol{\theta}=\begin{bmatrix} c_{1} & \cdots & c_{m} & a_{1} & \cdots & a_{n} \end{bmatrix}^{T}$$

- E o estimador é dado por
$$\hat{\boldsymbol{\theta}}=(\boldsymbol{\Phi}^{T}\boldsymbol{\Phi})^{-1}\boldsymbol{\Phi}^{T}\boldsymbol{Y}$$
e temos
$$\boldsymbol{\Phi}=\begin{bmatrix}\hat{e}(r) & \cdots & \hat{e}(r-m) & -y(r) & \cdots & -y(r-n) \\ \vdots && \vdots & \vdots && \vdots \\ \hat{e}(N-1) & \cdots & \hat{e}(N-1-m) & -y(N-1) & \cdots & -y(N-1-n) \end{bmatrix}$$
e o vetor das amostras
$$\boldsymbol{Y}=\begin{bmatrix} y(r+1) & y(r+2) & \cdots & y(N) \end{bmatrix}^{T}$$
em que temos $$r=\max(m,n)$$
