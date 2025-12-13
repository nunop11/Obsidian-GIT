## MA
- Demos modelo AM antes de modelo AR, mas agora para estimar densidade espectral demos em ordem contrária. Isso foi feito porque MA é mais difícil e porque irá envolver AR na sua resolução
- Como sabemos, um modelo MA é do tipo
$$y(t)=C(q^{-1})e(t)$$
em que temos $C(q^{-1})=1+c_{1}q^{-1}+\dots+c_{n}q^{-n}$ e $e(t)$ é ruído branco de média nula e variância $\sigma^{2}$.

### Densidade espectral
- Assumimos sempre que modelos MA são estacionários. 
- Vimos na aula 2 que a densidade espectral de um sistema com função transferência $G(q)$ é:
$$\Phi_{yy}(\omega)=|G(e^{j\omega})|^{2}\Phi_{uu}(\omega)$$
como o nosso input é $e(t)$ e a nossa função transferência é $C(q^{-1})$ então temos:
$$\Phi_{yy}(\omega)=|C(e^{-j\omega})|^{2}\sigma^{2}=|1+c_{1}e^{-j\omega} + \dots+ c_{n}e^{-jn\omega}|^{2}\sigma^{2}$$
ou seja, se estimarmos $C(q^{-1})$ estimamos $\Phi_{yy}(\omega)$

## Função geradora autocovariância
- Vejamos isto como um exemplo

### EX: processo MA(1)
#### Covariância
- Consideremos o modelo $y(t)=e(t)+c_{1}e(t-1)$
- E notamos que os parâmetros que definem o modelo são $c_{1},\sigma^{2}$
- Podemos obter as equações de Yule-Walker:
    1. Multiplicamos tudo por $y(t)$ e calculamos o valor esperado: $$\begin{align*}y(t)^{2}&= [e(t) + c_{1}e(t-1)]y(t)\\y(t)^{2}&= [e(t) + c_{1}e(t-1)][e(t) + c_{1}e(t-1)]\\y(t)^{2}&= e(t)^{2} + c_{1}^{2}e(t-1)^{2}+ 2c_{1}e(t)e(t-1)\\\mathbb{E}[y(t)^{2}] &= \mathbb{E}[e(t)^{2}] + \mathbb{E}c_{1}^{2}[e(t-1)^{2}] + 2c_{1}\mathbb{E}[e(t)e(t-1)]\\\lambda_{yy}(0)&= \sigma^{2} + c_{1}^{2}\sigma^{2} + 0\\\lambda_{yy}(0)&= (1 + c_{1}^{2})\sigma^{2}\end{align*}$$Notemos que aqui substituimos $y(t)$ pela equação de termos $e(t)$. No modelo AR não podíamos fazer isto então ficamos com termos $\lambda_{ye}(\tau)$. Mas regra geral: devemos fazer como temos aqui quando possível, é mais fácil trabalhar com valores médios de produtos $e(t)e(t+\tau)$
    2. Multiplicar tudo por $y(t)$ e calcular $\mathbb{E}$:$$\begin{align*}y(t)y(t-1)&= [e(t)+c_{1}e(t-1)]y(t-1)\\y(t)y(t-1)&= [e(t)+c_{1}e(t-1)][e(t-1)+c_{1}e(t-2)]\\y(t)y(t-1)&= e(t)e(t-1) + c_{1}e(t)e(t-2) + c_{1}e(t-1)^{2}+c_{1}^{2}e(t-1)e(t-2)\\&\downarrow \mathbb{E}\\\lambda_{yy}(1)&= c_{1}\sigma^{2}\end{align*}$$Em que todos os termos cruzados desaparecem: porque todas as observações do ruído branco são independentes temos $\mathbb{E}[e(t)e(t-\tau)]=0~,~\forall \tau\neq0$
    3. Pela lógica explicada, temos $\lambda_{yy}(\tau>1)=0$
-  Ou seja, temos a sequência de covariância teórica:
$$\begin{cases}
\lambda_{yy}(0)=(1+c_{1}^{2})\sigma^{2} \\
\lambda_{yy}(1)=\lambda_{yy}(-1)=c_{1}\sigma^{2} \\
\lambda_{yy}(\tau)=0 ~,~|\tau|>1
\end{cases}$$
e notemos que teríamos em MA(n):
$$\text{MA}(n):~~~~\lambda_{yy}(0)=(1+c_{1}^{2}+c_{2}^{2}+\dots+c_{n}^{2})\sigma^{2}$$

#### Transferência
- Neste modelo temos a função transferência: $H(z)=1+c_{1}z^{-1}$
- E temos a densidade espectral: $\Phi_{yy}(e^{j\omega})=H(e^{j\omega})H(e^{-j\omega})\sigma^{2}$
- Temos a **função geradora de autocovariância**
$$\begin{align*}
\Phi_{yy}(z)&= H(z)H(z^{-1})\sigma^{2}\\
&= (1+c_{1}z^{-1})(1+c_{1}z)\sigma^{2}\\
&= [1 + c_{1}z + c_{1}z^{-1} + c_{1}^{2}]\sigma^{2}\\
&= c_{1}\sigma^{2}z + (1+c_{1}^{2})\sigma^{2} + c_{1}\sigma^{2}z^{-1}\\
&= \lambda_{yy}(-1)z + \lambda_{yy}(0) + \lambda_{yy}(1)z^{-1}
\end{align*}$$
e os zeros desta função são:
$$\begin{align*}
\Phi_{yy}(z)=\lambda_{yy}(1)z + \lambda_{yy}(0)+\lambda_{yy}(1)z^{-1}&= 0\\
\lambda_{yy}(1)z^{2}+\lambda_{yy}(0)z+\lambda_{yy}(1)&= 0\\
z_{1}=\frac{- \lambda_{yy}(0) \pm \sqrt{\lambda_{yy}(0)^{2}-4\lambda_{yy}(1)^{2}}}{2\lambda_{yy}(1)}
\end{align*}$$
e escolhemos a solução positiva:
$$z_{1}=-\frac{\lambda_{yy}(0)}{2\lambda_{yy}(1)} + \frac{\sqrt{\left(\frac{\lambda_{yy}(0)}{\lambda_{yy}(1)}\right)^{2}-4}}{2}$$
- Que, como $\lambda_{yy}(0)=(1+c_{1}^{2})\sigma^{2}~,~\lambda_{yy}(1)=c_{1}\sigma^{2}$, obtemos:
$$z_{1}=-c_{1} \quad;\quad z_{2}=\frac{1}{z_{1}}=\frac{-1}{c_{1}}$$

#### Autocorrelação
- Como já vimos: $\rho_{yy}(1)=\frac{\lambda_{yy}(1)}{\lambda_{yy}(0)}$
- E podemos escrever $z_{1}$:
$$\begin{align*}
z_{1}&= - \frac{1}{2}\frac{\lambda_{yy}(0)}{\lambda_{yy}(1)} + \frac{\sqrt{\left(\frac{\lambda_{yy}(0)}{\lambda_{yy}(1)}\right)^{2}-4}}{2}\\
&= \frac{-1}{2\rho_{yy}(1)} + \frac{\sqrt{\left(\frac{1}{\rho_{yy}(1)}\right)^{2}-4}}{2}\\
&= \frac{-1 + \rho_{yy}(1)\sqrt{\left(\frac{1}{\rho_{yy}(1)}\right)^{2}-4}}{2}\\
&= - \frac{1-\sqrt{1-4\rho_{yy}(1)^{2}}}{2}
\end{align*}$$
- E vimos acima que :
$$z_{1}=-c_{1}~~\to~~ c_{1}=\frac{1-\sqrt{1-4\rho_{yy}(1)^{2}}}{2}$$
$$\lambda_{yy}(0)=(1+c_{1}^{2})\sigma^{2}~~\to~~ \sigma^{2}=\frac{\lambda_{yy}(0)}{1+c_{1}^{2}}$$
- Notemos que é necessário termos o coeficiente $c_{1}$ **REAL**, logo temos a seguinte *restrição*:
$$1-4\rho_{yy}^{2}(1)>0~~\to~~ |\rho_{yy}(1)| < \frac{1}{2}$$
- E notemos que se $\rho_{yy}(1)=\pm \frac12$ temos $z_{1}=\pm1$ e o sistema é **inversamente instável** (temos o polo no limite do circulo unitário)

### Algoritmo
1. Estimar sequência de autocovariância $\tau=-n,\dots,n$. Notemos que $n$ é ordem MA(n)
    - Usar `xcov` no Matlab
    - Ou usar estas fórmulas: $$\hat{\lambda}_{yy}(\tau)=\begin{cases}\frac{1}{N-\tau}\sum_{t=\tau+1}^{N}y(t)y(t-\tau) & , & 0\le\tau\le n \\\hat{\lambda}_{yy}(\tau)=\hat{\lambda}_{yy}(-\tau) & , & -n\le\tau\le -1 \\0 & , & |\tau|>n \end{cases}$$
2. Calcular os zeros da função geradora de autocovariância (que abaixo temos já convertida em polinómio): $$\hat{\lambda}_{yy}(n)z^{2n} + \dots+ \hat{\lambda}_{yy}(1)z^{n+1}+\hat{\lambda}_{yy}(0)z^{n}+\hat{\lambda}_{yy}(1)z^{n-1}+\dots+\hat{\lambda}_{yy}(n)=0$$
3. Selecionar os zeros  $z_{1},\dots,z_{n}$ que estão dentro do circulo unitário: $$z_{i}z_{i}^{*} = \|z_{i}\|^{2}< 1$$
4. Determinar a função transferência
$$\hat{H}(z)=(1-z_{1}z^{-1})(1-z_{2}z^{-1})\cdots(1-z_{n}z^{-1})$$
5. Cada coeficiente $c_k$ é igual à soma de todos os produtos dos zeros $z_i$, tomados $k$ a $k$, com sinal alternado determinado por $(-1)^k$.
$$c_k = (-1)^{k} \sum\limits_{1 \le i_1 < i_2 < \cdots < i_k \le n} z_{i_1} z_{i_2} \cdots z_{i_{k}\quad;\quad}k=1,\dots,n$$
6. Temos a variância: 
$$\sigma^{2}=\frac{\hat{\lambda}_{yy}(0)}{1+c_{1}^{2}+\dots+c_{n}^{2}}$$

### Problema
Este método é muito direto e simples. Mas tem alguns problemas:
- Esta técnica baseia-se na estimação da sequência de covariância, pelo que temos sempre erros de base
- Por esta razão, é muito possível gerarmos zeros no limite do círculo unitário e , como consequência, temos *coeficientes complexos* -- Isso NÃO pode ser!
    - Isto acontece devido a acumulação de erros de aproximação
- Nas palavras do professor, este método parece muito bom na teoria mas não presta

## Resposta Impulsional Truncada
-  Temos um processo MA(n). A sua função transferência é: 
$$H(z)=1+c_{1}z^{-1}+\dots+c_{n}z^{-n}$$
- Este método baseia-se em aproximar isto a um processo AR(p). Nisto, trabalhamos com o modelo AR, que é mais fácil. A base da ideia é simples:
    - $\text{MA(n)}:~~ y(t)=H(z)e(t)$
    - $\text{AR}(\infty):~~ e(t)=\frac{1}{H(z)}y(t)$
- Podemos escrever:
$$H(z)=\frac{1}{\frac{1}{H(z)}}$$
e podemos expandir:
$$\begin{align*}
\frac{1}{H(z)}&= \frac{1}{1+c_{1}z^{-1}+\dots+c_{n}z^{-n}}\\
&\approx 1+a_{1}z^{-1}+\dots+a_{p}z^{-p}
\end{align*}$$
- Temos 2 opções para fazer esta expansão:
    1. Divisão longa de $1/H$
    2. Transformada Z inversa

### Truncagem
- Passamos ao passo seguinte: truncar a expressão
- Ao expandir $\frac{1}{H}$ ficamos com um polinómio com infinito termos
- Mas, claro, não podemos fazer contas nem estimar infinitos termos. Assim, *truncamos* o polinómio AKA cortamos. Definimos um termo $p$, e só consideramos o polinómio até ele:
$$\frac{1}{H(z)}\approx 1+a_{1}z^{-1}+\dots+a_{p}z^{-p}\equiv A(z^{-1})$$
- Ora, notemos que estamos a fazer esta aproximação:
$$\begin{align*}
\text{MA}(n)&: &&y(t)=e(t) + c_{1}e(t-1)+\dots+c_{n}e(t-n)\\
\text{AR}(p)&: &&y(t)+a_{1}y(t-1)+\dots+a_{n}y(t-n)=e(t)
\end{align*}$$
- Mas *porquê* que podemos fazer isto? Porque $H(z)$ é inversamente estável.

### Coeficientes C
- Agora voltamos para trás
- Temos a função que descreve o sistema AR truncado: $A(z^{-1})=1+a_{1}z^{-1}+\dots+a_{p}z^{-p}$
- E temos que:
$$\frac{1}{H(z^{-1})}\sim A(z^{-1}) ~~\to~~ a_{k}=\mathcal{Z}^{-1}\left\{\frac{1}{H(z^{-1})}\right\}$$
podemos fazer o oposto:
$$\frac{1}{A(z^{-1})}\sim H(z^{-1})~~\to~~ \hat{c}_{k}=\mathcal{Z}^{-1}\left\{\frac{1}{A(z^{-1})}\right\}$$
(ou podemos só expandir $\frac{1}{A(z^{-1})}$ com uma divisão longa)

- Novamente, obtemos um polinómio com infinitos termos. Truncamos no termo de ordem $n$
- Finalmente, temos a estimativa do modelo MA(n):
$$\hat{H}(z^{-1})=1+\hat{c}_{1}z^{-1} + \dots+\hat{c}_{n}z^{-n}$$
de onde vem o modelo estimado
$$y(t)=e(t)+\hat{c}_{1}e(t-1)+\dots+\hat{c}_{n}e(t-n)$$
e a variância
$$\hat{\sigma}^{2}=\frac{\hat{\lambda}_{yy}(0)}{1+\hat{c}_{1}^{2}+\dots+\hat{c}_{n}^{2}}$$

#### Ordem
- Se tivermos estimativa da sequência de autovocariância do modelo MA, podemos usar a correlação parcial para determinar a ordem do modelo AR.

### Conclusão
- Este método consiste em:
    1. Definir a função transferência $H(z^{-1})$ do modelo MA(n)
    2. Converter $\frac{1}{H(z^{-1})}$ num polinómio, truncado na ordem $p$
    3. Esse polinómio é a função transferência $A(z^{-1})$ de um processo AR(p)
    4. Converter $\frac{1}{A(z^{-1})}$ num polinómio, truncado na ordem $n$
    5. Esse polinómio é a nossa estimativa do modelo MA(n): $\hat{H}(z^{-1})$

### Transformada Z inversa
- Agora voltemos a um ponto acima. Vejamos o que significa acima quando falamos em transformada Z inversa.
**Definição**
- A transformada Z é definida como:
$$X(z)=\sum\limits_{n=-\infty}^{+\infty}x(k) z^{k}$$
e temos a inversa:
$$x(k)=\frac{1}{2\pi j}\oint X(z)z^{k-1}dz=\frac{1}{2\pi}\int_{-\pi}^{+\pi}X(e^{i\omega})e^{i\omega k}d\omega$$
(sendo que em $\oint$ integramos dentro da região de convergência)

- Agora, é fundamental *entender* o que é cada uma destas coisas:
    - Exemplo de  função $X(z)$: $$X(z)=\frac{1}{1- \frac{3}{2}z^{-1}+ \frac{1}{2}z^{-2}}$$
    - Exemplo de sequência $x(k)$, obtida pelo integral: $$x(k)=\left\{1, \frac{3}{2}, \frac{7}{4}, \frac{15}{8}, \dots\right\}$$
- Notemos que a sequência $x(k)$ tem um número infinito de termos, podemos só aumentar $k$ e o integral continuará a dar algo

**Waittttt**
- Agora notemos algo muito interessante. Vamos fazer a expansão longa:
$$
\begin{array}{@{}l@{}|@{}l@{}}
\begin{array}{@{}l@{}}
1 \\[2pt]
1- \frac{3}{2}z^{-1}+ \frac{1}{2}z^{-2} \\ \hline
0+ \frac{3}{2}z^{-1}- \frac{1}{2}z^{-2} \\[2pt]
\hspace{1.5em} ~\frac{3}{2}z^{-1}- \frac{9}{4}z^{-2}+ \frac{3}{4}z^{-3} \\ \hline
\hspace{1.9em} 0 ~~~~~~+ \frac{7}{4}z^{-2}- \frac{3}{4}z^{-3}\\[2pt]
\hspace{5.2em} \frac{7}{4}z^{-2} - \frac{21}{8}z^{-3} + \frac{7}{8}z^{-4} \\ \hline
\hspace{5.2em} 0~~~~~~~+ \frac{15}{8}z^{-3}- \frac{7}{8}z^{-4} \\[2pt]
\hspace{8em} \vdots
\end{array}
&
\displaystyle
\begin{matrix}\dfrac{1- \frac{3}{2}z^{-1} + \frac{1}{2}z^{-2}}{1+ \frac{3}{2}z^{-1}+ \frac{7}{4}z^{-2}} \\  \\  \\  \\  \\  \\  \\  \end{matrix}
\end{array}$$
- Mas wait. A **sequência da transformada inversa é o conjunto de coeficientes do resultado da divisão**.
    - Isto bate certo, porque a sequência é infinita e este polinómio resultante da divisão também pode ir até à parcela $z^{-\infty}$

**Aplicação**
- Ok, voltemos ao problema em causa nesta aula. Temos uma função transferência:
$$H(z)= 1 + c_{1}z^{-1}+\dots+c_{n}z^{-n}$$
e queremos definir:
$$\frac{1}{H(z)}=1+a_{1}z^{-1}+\dots+a_{n}z^{-n}$$
- Ora, o que acabamos de ver acima é que podemos obter os coeficientes ao fazer:
$$\boxed{a_{k}= \mathcal{Z}^{-1} \left\{\frac{1}{H(z)}\right\}_{(k)}=\frac{1}{2\pi}\int_{-\pi}^{+\pi}\frac{e^{j\omega k}}{H(e^{j\omega})}d\omega}$$
já que a **sequência da transformada inversa é o conjunto de coeficientes do resultado da divisão**.

## Mínimos Quadrados MA
- Como vimos muitas vezes, podemos representar um processo estocástico como sendo a saída de um SLIT cujo input é ruído branco
- Ora, podemos medir $y(t)$. Se conseguíssemos conhecer $e(t)$, obter $H(q)$ seria um problema de identificação de sistemas - bastante fácil computacionalmente
- O estimador de mínimos quadrados tenta estimar $e(t)$

### AR
- Começamos por aproximar o modelo MA(n) a um modelo AR(p) com $p$ elevado:
$$\hat{e}(t)=y(t)+\hat{a}_{1}y(t-1)+\dots+\hat{a}_{p}y(t-p)$$
sendo que fazemos isto com divisão longa ou transformada Z inversa
- Para determinar esta "ordem p elevada" temos que
    1. Fazer análise de correlação parcial
    2. Confirmar se essa ordem foi alta o suficiente fazendo um teste de brancura dos resíduos
        - Depois de escolher a ordem e determinar o modelo estimado, vemos os resíduos: erros de estimação
        - Calculamos a sequência de autocovariância do erro. Tem que estar abaixo dum patamar para ser ruído branco
- Ou seja, primeiro estimamos os coeficientes $\hat{a}_i$ 
- Usando os coeficientes e $y(t-i)$ podemos estimar o ruído usando a equação acima, com um modelo AR

### Regressão
- Estimando $\hat{e}(t)$, o modelo MA fica na forma:
$$y(t)=\hat{e}(t)+c_{1}\hat{e}(t-1)+\dots+c_{n}\hat{e}(t-n)$$
- Mas notemos uma forma matricial aqui:
$$\theta=\begin{bmatrix}c_{1} \\ 
\vdots \\ c_{n}\end{bmatrix} \quad;\quad \varphi(t)=\begin{bmatrix}\hat{e}(t-1) \\ \vdots \\ \hat{e}(t-n)\end{bmatrix}$$
e temos
$$y(t)=\varphi(t)^{T}\theta + \hat{e}(t)$$
em que temos que os resíduos deste estimador linear são $\hat{e}(t)$, ruído branco!

- Podemos então definir os parâmetros $\hat{\theta}$ num método LS:
$$\hat{\theta}=(\Phi^{T}\Phi)^{-1}\Phi^{T}Y$$
em que
$$\Phi=\begin{bmatrix}\varphi(n+1)^{T} \\ \varphi(n+2)^{T} \\ \vdots \\ \varphi(N-1)^{T} \\ \varphi(N)^{T}\end{bmatrix}=\begin{bmatrix}\hat{e}(n) & \hat{e}(n-1) & \cdots & \hat{e}(1) \\ \hat{e}(n+1) & \hat{e}(n) & \cdots & \hat{e}(2) \\ \vdots & \vdots & \ddots & \vdots \\ \hat{e}(N-2) & \hat{e}(N-3) & \cdots & \hat{e}(N-n+1) \\ \hat{e}(N-1) & \hat{e}(N-2) & \cdots & \hat{e}(N-n) \end{bmatrix}$$
e temos $$Y=\begin{bmatrix}y(n+1) & y(n+2) & \cdots & y(N)\end{bmatrix}^{T}$$
- Notemos as dimensões:
    - $\hat{\theta}: n\times1$
    - $\Phi:N-n\times n$
    - $Y:N-n\times1$

### Correlação
- Vamos repetir um truque que já vimos bastante. Podemos reescrever a solução LS assim:
$$\hat{\theta}= \left(\frac{1}{N-n-1}\Phi^{T}\Phi \right)^{-1} \frac{1}{N-n-1}\Phi^{T}Y$$
- E podemos ver que a *primeira parcela* é uma matriz quadrada $n\times n$:
$$\frac{\Phi^{T}\Phi}{N-n-1}=\begin{bmatrix}\frac{\sum\limits_{t=n}^{N-1}\hat{e}(t)^{2}}{N-n-1} & \frac{\sum\limits_{t=n}^{N-1}\hat{e}(t-1)^{2}}{N-n-1} & \cdots & \frac{\sum\limits_{t=n}^{N-1}\hat{e}(t-n+1)^{2}}{N-n-1} \\ \frac{\sum\limits_{t=n-1}^{N-2}\hat{e}(t+1)^{2}}{N-n-1} & \frac{\sum\limits_{t=n-1}^{N-2}\hat{e}(t)^{2}}{N-n-1} & \cdots & \frac{\sum\limits_{t=n-1}^{N-2}\hat{e}(t-n+2)^{2}}{N-n-1} \\ \vdots & \vdots & \ddots & \vdots \\ \frac{\sum\limits_{t=1}^{N-n}\hat{e}(t+n-1)^{2}}{N-n-1} & \frac{\sum\limits_{t=1}^{N-n}\hat{e}(t+n-2)^{2}}{N-n-1} & \cdots & \frac{\sum\limits_{t=1}^{N-n}\hat{e}(t)^{2}}{N-n-1}
\end{bmatrix}$$
mas notamos que existe aqui um padrão. Temos algo bastante parecido à formula da autocovariância. Tão parecido aliás que temos
$$\lim_{n\to\infty} \frac{1}{N-n-1}\Phi^{T}\Phi=\begin{bmatrix}\lambda_{\hat{e}\hat{e}}(0) & \lambda_{\hat{e}\hat{e}}(1) & \cdots & \lambda_{\hat{e}\hat{e}}(n-1) \\ \lambda_{\hat{e}\hat{e}}(1) & \lambda_{\hat{e}\hat{e}}(0) & \cdots & \lambda_{\hat{e}\hat{e}}(n-2) \\ \vdots & \vdots & \ddots & \vdots \\ \lambda_{\hat{e}\hat{e}}(n-1) & \lambda_{\hat{e}\hat{e}}(n-2) & \cdots & \lambda_{\hat{e}\hat{e}}(0)\end{bmatrix}$$
e para ruído branco temos sempre:
$$\lambda_{\hat{e}\hat{e}}(\tau)=\begin{cases}
\hat{\sigma}^{2} & , &  \tau=0 \\
0 & , & \tau\neq0
\end{cases}$$
logo:
$$\lim_{N\to\infty}\frac{1}{N-n-1}\Phi^{T}\Phi=\hat{\sigma}^{2}I_{n}$$

- E temos a *segunda* parcela que é um vetor $n\to 1$
$$\Phi^{T}Y=\begin{bmatrix}\frac{\sum\limits_{t=n}^{N-1}\hat{e}(t)y(t+1)}{N-n-1} \\ \frac{\sum\limits_{t=n-1}^{N-2}\hat{e}(t)y(t+2)}{N-n-1} \\ \vdots \\ \frac{\sum\limits_{t=1}^{N-n}\hat{e}(t)y(t+n)}{N-n-1}\end{bmatrix}$$
e temos, simalarmente ao caso anterior:
$$\lim_{N\to\infty}\frac{1}{N-n-1}\Phi^{T}\Phi=\begin{bmatrix}\lambda_{y\hat{e}}(1) & \lambda_{y\hat{e}}(2) & \cdots & \lambda_{y\hat{e}}(m)\end{bmatrix}^{T}$$

- Ao *juntar as 2 parcelas*:
$$\lim_{N\to\infty}~\hat{\theta}= \begin{bmatrix}\dfrac{\lambda_{y\hat{e}(1)}}{\hat{\sigma}^{2}} & \dfrac{\lambda_{y\hat{e}(2)}}{\hat{\sigma}^{2}}  & \cdots  & \dfrac{\lambda_{y\hat{e}(n)}}{\hat{\sigma}^{2}}\end{bmatrix}$$
logo temos
$$\boxed{\hat{c}_{k}= \frac{\hat{\lambda}_{y\hat{e}}(k)}{\hat{\sigma}^{2}} \quad,\quad k=1,\dots,n}$$

### Minimizar erro
- Minimizar o erro significa minimizar esta função:
$$J(\theta)=\frac{1}{2}\sum\limits_{t=1}^{N}\hat{e}^{2}(t,\theta)$$
- Ou seja, o estimador otimizado terá os parâmetros:
$$\hat{\theta}=\min_{\theta}J(\theta)$$
- E temos o caso assintotico $\lim_{N\to\infty} \hat{\theta}=\theta_{0}$, em que $\theta_{0}$ são os valores verdadeiros dos parâmetros
- Como sempre, minimizar implica fazer cálculo de gradiente:
$$\frac{dJ(\theta)}{d\theta} = \begin{bmatrix} \dfrac{\partial J}{\partial c_{1}} & \dfrac{\partial J}{\partial c_{2}} & \cdots & \dfrac{\partial J}{\partial c_{n}} \end{bmatrix}^{T}$$
- Teoricamente, minimizavamos o erro ao atingir gradiente nulo: $\frac{dJ}{d\theta}=\mathbf{0}$. Mas essa equação não tem solução analítica
- Assim, usamos um **método iterativo**:
$$\theta^{(i+1)}=\theta^{(i)}- \eta \frac{dJ(\theta)}{d\theta}$$
e definimos a *tava de aprendizagem* $\eta>0$

### Cálculo de gradiente
- Os componentes do vetor gradiente são derivadas do tipo
$$\frac{\partial J(\theta)}{\partial c_{k}}=\sum\limits_{t=1}^{N}\frac{\partial \hat{e}(t,\theta)}{\partial c_{k}}\hat{e}(t,\theta)$$
- Ora, sabemos que no caso ideal temos $y(t)-\hat{y}(t,\theta)=\hat{e}(t,\theta)$ : o erro do nosso estimador é apenas o ruído branco, que não podemos remover.

#### Dedução
- Num modelo MA temos:
$$y(t)=C(q^{-1})\hat{e}(t,\theta)~~\to~~ \hat{e}(t,\theta)=\frac{1}{C(q^{-1})}y(t)$$
- Derivamos tudo em função de $c_{k}$:
$$\begin{align*}
\frac{\partial y(t)}{\partial c_{k}}&= \frac{\partial}{\partial c_{k}} \left[C(q^{-1})\hat{e}(t,\theta) \right]\\
0&= \frac{\partial}{\partial c_{k}}\left[C(q^{-1})\right]\hat{e}(t,\theta) + C(q^{-1})\frac{\partial \hat{e}(t,\theta)}{\partial c_{k}} \end{align*}$$
**Termo 1**
- Notemos que $$\begin{align*}
C(q^{-1})&= 1+c_{1}q^{-1}+\dots+c_{k}q^{-k}+\dots+c_{n}q^{-n}\\
\end{align*}$$
pelo que temos:
$$\begin{align*}
\frac{\partial C(q^{-1})}{\partial c_{k}}&= 0+q^{-1}\frac{\partial c_{1}}{\partial c_{k}}+\dots+q^{-k} \frac{\partial c_{k}}{\partial c_{k}}+\dots+q^{-n} \frac{\partial c_{n}}{\partial c_{k}}\\
&= 0+0+\dots+q^{-k}\cdot1+\dots+0\\
&= q^{-k}
\end{align*}$$
- E o primeiro termo fica:
$$\frac{\partial C(q^{-1})}{\partial c_{k}}\hat{e}(t,\theta)=q^{-k}\hat{e}(t,\theta)=\hat{e}(t-k,\theta)$$

**Derivada**
- Conhecemos o 1º termo da equação. Podemos usar isso para determinar como calcular a derivada do erro:
$$\begin{align*}
0&= \hat{e}(t-k,\theta) + C(q^{-1})\frac{\partial \hat{e}(t,\theta)}{\partial c_{k}}\\
-\hat{e}(t-k,\theta)&=  C(q^{-1})\frac{\partial \hat{e}(t,\theta)}{\partial c_{k}}\\
\end{align*}$$
$$\boxed{\frac{\partial \hat{e}(t,\theta)}{\partial c_{k}}= \frac{-1}{C(q^{-1})}\hat{e}(t-k,\theta)}$$

**Erro base**
- Num modelo MA temos o estimador: $$\hat{y}(t)=\frac{C(q^{-1})-1}{C(q^{-1})}y(t)$$
- No caso ideal, o erro de estimação **é** ruído branco (apenas ficamos com o ruído que nunca podemos a retirar):
$$\begin{align*}
\hat{e}(t,\theta)&= y(t) - \hat{y}(t)\\
&= y(t) - \frac{C(q^{-1})-1}{C(q^{-1})}y(t)\\
&= \frac{1}{C(q^{-1})}y(t)
\end{align*}$$
e conseguimos estimar o ruído branco com o sinal $y(t)$, que podemos medir!

#### Sequência
- Tudo o que deduzimos acima reduz-se nisto:
![[descida gradiente MA esquema.png]]
- Notemos que os $n$ blocos com $q^{-1}$ representam os $n$ coeficientes de $C(q^{-1})$

**Variáve nova**
- Definimos uma nova variável:
$$e_{F}(t,\theta)=\frac{-1}{C(q^{-1})}\hat{e}(t,\theta)$$
se a substituirmos na fórmula da derivada:
$$\frac{\partial \hat{e}(t,\theta)}{\partial c_{k}}= \frac{-1}{C(q^{-1})}q^{-k}\hat{e}(t,\theta)=q^{-k}e_{F}(t,\theta)=e_{F}(t-k,\theta)$$
- Assim vemos que esta variável permite representar facilmente a derivada, através de uma divisão:
$$\boxed{e_{F}(t-k,\theta )=\frac{\partial \hat{e}(t,\theta)}{\partial c_{k}}}$$

### Algoritmo
- **Inicialização:** definir $\theta^{(0)}$ e começar com $i=0$
    1. Aproximar o modelo MA(n) a AR(p). Obter $\hat{a}_{i}$. Assim temos o nosso estimador de $\hat{e}(t)$: $\hat{e}(t)=y(t)+\hat{a}_{1}y(t-1)+\dots+\hat{a}_{p}y(t-p)$
    2. Fazer uma primeira estimativa dos parâmetros: $\hat{c}_{k}= \frac{\hat{\lambda}_{y\hat{e}}(k)}{\hat{\sigma}^{2}}$
    3. Com estes parâmetros definimos $\theta^{(0)}$
     (invés disto, poderíamos usar outro método qualquer de estimação MA)
- **Repetir até convergir:**
    1. Estimar o erro: $\hat{e}(t,\theta^{(i)})=\frac{1}{C^{(i)}(q^{-1})}y(t)$
    2. Calcular: $e_{F}(t,\theta^{(i)})=\frac{-1}{C^{(i)}(q^{-1})}\hat{e}(t,\theta^{(i)})$
    3. Determinar o gradiente:$$\begin{align*}\frac{dJ(\theta)}{d\theta} &= \begin{bmatrix} \dfrac{\partial J}{\partial c_{1}} & \dfrac{\partial J}{\partial c_{2}} & \cdots & \dfrac{\partial J}{\partial c_{n}} \end{bmatrix}^{T}\\&= \begin{bmatrix}\sum\limits_{t=1}^{N}\frac{\partial \hat{e}(t,\theta^{(i)})}{\partial c_{1}}\hat{e}(t,\theta^{(i)}) & \sum\limits_{t=1}^{N}\frac{\partial \hat{e}(t,\theta^{(i)})}{\partial c_{2}}\hat{e}(t,\theta^{(i)}) & \cdots & \sum\limits_{t=1}^{N}\frac{\partial \hat{e}(t,\theta^{(i)})}{\partial c_{n}}\hat{e}(t,\theta^{(i)})\end{bmatrix}^{T}\\&= \begin{bmatrix}\sum\limits_{t=1}^{N}e_{F}(t-1,\theta^{(i)})\hat{e}(t,\theta^{(i)}) & \cdots & \sum\limits_{t=1}^{N}e_{F}(t-n,\theta^{(i)})\hat{e}(t,\theta^{(i)})\end{bmatrix}^{T}\\&= \sum\limits_{t=1}^{N}\begin{bmatrix}e_{F}(t-1,\theta^{(i)})\\e_{F}(t-2,\theta^{(i)})\\\vdots\\e_{F}(t-n,\theta^{(i)})\end{bmatrix} \hat{e(t,\theta^{(i)})}\end{align*}$$
    4. Atualizar $\theta^{(i+1)}=\theta^{(i)}- \eta \frac{dJ(\theta)}{d\theta}$
    5. Incrementar $i$

## Autocorrelação MA
- Como vimos na aula anterior, a autocorrelação de um processo estacionário é definida como:
$$\rho_{yy}(\tau)=\frac{\lambda_{yy}(\tau)}{\lambda_{yy}(0)}$$
- No caso de um processo MA(n) temos $\lambda_{yy}(\tau)=0~,~|\tau|>n$ logo $$\rho_{yy}(\tau)=0~~,~~ |\tau|>n$$
- Ora, para determinar a ordem dum processo MA chegaria então ver a ordem $n$ a partir da qual $\rho_{yy}(\tau)=0$

### Na prática
- Infelizmente, na prática temos **probabilidade nula** de ter $\rho_{yy}(\tau)=0$ porque usamos dados reais.
- Mas felizmente, se o valor teórico/real for $\rho_{yy}(\tau)=0$ então a estimativa que calculamos seguirá:
$$\hat{\rho}_{yy}(\tau)\sim \mathcal{N}\left(0, \frac{1}{N}\right)$$
- E assim decidimos que um modelo MA tem ordem $n$, sendo $n$ o último termo da sequência que está **fora** do intervalo de confiança desta distribuição normal!
![[autocorrelacao MA.png]]
Aqui consideraríamos ordem $n=3$. 