# ARMA
## Média Móvel (MA)
- AKA *Moving Average*
- Vimos atrás que podemos estudar um processo estocástico estacionário como sendo a **saída de um SLIT** em que a entrada é *ruído branco*:
![[slit com ruido branco.png]]
- E definimos a resposta impulsional:
$$h(t) = \begin{cases}
0 & , & t<0 \\
1 & , & t=0 \\
c_{t} & , & t>0
\end{cases}$$
- Assim, podemos representar a resposta do sistema como:
$$\begin{align*}
y(t)&= h(t)*e(t)\\
&= e(t)+c_{1}e(t-1) + \dots + c_{n}(t-n)+\dots
\end{align*}$$
e vemos que a resposta num instante $t$ depende dos $n$ instantes anteriores.

- Ora, quando temos um processo em que $$\boxed{c_{t}=0~~,~~ t>n \quad \longrightarrow \quad \text{Média móvel ordem }n}$$
- Ou seja, temos:
$$\begin{align*}
y(t)&= e(t) + c_{1}e(t-1) + \dots + c_{n}e(t-n)\\
&\downarrow\\
&= C(q^{-1})e(t)
\end{align*}$$
- Aqui, $q^{-1}$ é equivalente a $z^{-1}$ e é o *operador de unit delay*. Além disso, neste passo está implicito uma espécie de convolução
- O que importa é a função $C$:
$$C(q^{-1})=1 + c_{1}q^{-1}+\dots+c_{n}q^{-n}$$
que é a função de transferência de processos estocásticos de média móvel:
$$H(q)\equiv C(q^{-1})$$
Esta função é sempre **estável**.

### Estimador
- Vimos na aula anterior que o melhor estimador de um processo descrito pela função transferência $H(q)$ é dado por $\hat{y}(t)=[H(q)-1]H^{-1}(q)y(t)$. Assim temos o melhor estimador MA:
$$\begin{align*}
\hat{y}(t)&= [C(q^{-1}) - 1] C^{-1}(q^{-1})y(t)\\
&= \frac{1 + c_{1}q^{-1}+\dots+c_{n}q^{-n}-1}{1 + c_{1}q^{-1}+\dots+c_{n}q^{-n}}y(t)\\
&= \frac{c_{1}q^{-1}+\dots+c_{n}q^{-n}}{1 + c_{1}q^{-1}+\dots+c_{n}q^{-n}}y(t)\\
\hat{y}(t)&+c_{1}q^{-1}\hat{y}(t)+\dots+c_{n}q^{-n}\hat{y}(t)= c_{1}q^{-1}y(t)+\dots+c_{n}q^{-n}y(t)\\
\hat{y}(t)&= c_{1}y(t-1)+\dots+c_{n}y(t-n) - c_{1}\hat{y}(t-1)-\dots-c_{n}\hat{y}(t-n)
\end{align*}$$
- Notamos então que este estimador consiste numa combinação linear dos últimos $n$ valores estimados $\hat{y}$ e últimos $n$ valores medidos do processo  $y$
- Uma coisa a apontar: **filtros de média móvel**
    - Estes filtros são relativamente simples e consistem em fazer a média dos últimos $n$ valores medidos para suavizar um sinal.
    - O funcionamento é semelhante ao deste estimador de processo, mas há uma grande diferença: aqui temos pesos $c_{1},\dots,c_{n}$. No caso do filtro todas as medições têm um peso $1/n$

### Aproximação
- Como $H(q)$ é estável, a sua resposta impulsional $h(t)$ é *absolutamente somável* e tende para zero:
$$\lim_{t\to\infty}h(t)=0$$
e é *infinita no tempo*:
$$h(t)\neq0~~,~~\forall t\le0$$
- Voltando ao início desta aula, vemos que um processo estacionário pode ser escrito como:
$$\begin{align*}
y(t)&= h(t)*e(t)\\
&= e(t)+c_{1}e(t-1) + \dots + c_{n}(t-n)+\dots
\end{align*}$$
- Ora, juntando toda esta informação, vemos que **todos** os processos estacionários podem ser vistos como **processos MA** de ordem $n=\infty$.
- Ou seja, podemos sempre aproximar um processo a um processo MA, tendo-se que o erro de aproximação diminui ao aumentar $n$

## Auto-regressivo (AR)
- Como vimos, processos MA são simples e permitem aproximar qualquer processo. Mas para terem sucesso necessitam de ter uma ordem elevada
- Quando só conseguimos aproximar o processo com um $n$ enorme, é melhor usar modelos *auto-regressivos*:
$$y(t) + a_{1}y(t-1) + \dots + a_{n}y(t-n)=e(t)$$
- Este nome surge porque estamos a aplicar os ajuste diretamente na resposta $y(t)$ - estamos a ajustar a própria resposta (auto ajustar)
- Com a mesma lógica que aciam, podemos definir a função
$$A(q^{-1})=1+a_{1}q^{-1}+\dots+a_{n}q^{-n}$$
em que temos $A(q^{-1})y(t)=e(t)$.

- Definimos então a função de transferência:
$$H(q)=\frac{1}{A(q^{-1})} \quad \quad;\quad y(t)=H(q)e(t)$$
- Nestes processos costuma ser preciso uma ordem bastante inferior a processos MA
- Tal como no caso MA, $A(q^{-1})$ tem de ser estável

### Estimador
- Podemos definir o melhor estimador AR da mesma forma que acima:
$$\begin{align*}
\hat{y}(t)&= [H(q)-1]H^{-1}(q)y(t)\\
&= \left[ \frac{1}{A(q^{-1})} -1\right]A(q^{-1})y(t)\\
&= [1- A(q^{-1})]y(t)\\
&= -a_{1}q^{-1}y(t)-a_{2}q^{-2}y(t)-\dots-a_{n}q^{-n}y(t)\\
&= -a_{1}y(t-1) - a_{2}y(t-2)-\dots-a_{n}y(t-n)
\end{align*}$$
- Notemos que neste modelo apenas dependemos das medições do processo $y$. 
- Relativamente a modelos MA, isto introduz a vantagem que não iremos acumular erros de previsão

## ARMA
- Vejamos agora a combinação de modelos MA e AR: **modelo auto-regressivo de média móvel**
- Aplicamos diretamente regressões na saída e médias móveis na entrada:
$$A(q^{-1})y(t)=C(q^{-1})e(t)$$
e temos a função de transferência 
$$H(q)=\frac{C(q^{-1})}{A(q^{-1})}$$

### Estimador
- Aplicamos mais uma vez a mesma lógica que acima e obtemos:
$$\Tiny\begin{align*}
\hat{y}(t)&= [H(q)-1]H^{-1}(q)y(t)\\
&= \left[\frac{C(q^{-1})}{A(q^{-1})}-1 \right] \frac{A(q^{-1})}{C(q^{-1})}y(t)\\
&= \frac{C(q^{-1})-A(q^{-1})}{C(q^{-1})}y(t)\\
&= (c_{1}-a_{1})y(t-1) + \dots + (c_{n}-a_{n})y(t-n) - c_{1}\hat{y}(t-1) -\dots-c_{n}\hat{y}(t-n)
\end{align*}$$
em que temos literalmente uma combinação dos 2 métodos.

# Modelos de Estado
## Espaço de estados
- Vejamos 2 casos físicos comuns
**Tanque de água**
- Temos um tanque de água em que entra água de uma torneira com caudal variável $q_{i}(t)$. Na parte de baixo do tanque temos uma válvula, que gera um caudal de saída variável $q_{o}(t)$
- Assim, como o caudal são o volume que se move por unidade de tempo, temos que o volume de água dentro do tanque é dado por:
$$\begin{align*}
v(t)&= \int_{-\infty}^{r} \left[q_{i}(\tau)-q_{o}(\tau) \right]d\tau\\
&= \int_{-\infty}^{0} \left[q_{i}(\tau)-q_{o}(\tau) \right]d\tau + \int_{0}^{t} \left[q_{i}(\tau)-q_{o}(\tau) \right]d\tau\\
&= v(0) + \int_{0}^{t} \left[q_{i}(\tau)-q_{o}(\tau) \right]d\tau
\end{align*}$$
ou seja, vemos que $v(0)$ representa a **memória** do que aconteceu no sistema antes de $t=0$. Podemos então dizer  que $v(0)$ é uma *variável de estado*
- Podemos definir uma variável $u(t)=q_{i}(t)-q_{o}(t)$ que representa o **fluxo global** de água no tanque. Ou seja, esta variável representa toda a variação do nível de água no tanque!
- Podemos ver na equação de $v(t)$ que:
$$u(t)=\dot{v}(t)$$
logo podemos dizer que $u(t)$ representa o **estado** do sistema.

**Carrinho**
- Consideremos um carro de massa $m$ a mover-se numa superfície com constante de atrito $b$, empurrado por uma força $f$. 
- Podemos definir a sua equação de movimento, considerando a distância percorrida $d$:
$$f=m \ddot{d} +b \dot{d}$$
- Podemos definir as 2 variáveis: $x_{1}=d~,~x_{2}=\dot{d}$. Usando estas e a equação de movimento temos
$$\begin{cases}
\dot{x}_{1}=x_{2} \\
f=m \dot{x}_{2} + b x_{2}
\end{cases}= \begin{cases}
\dot{x}_{1}=x_{2} \\
\dot{x}_{2}=-\frac{b}{m}x_{2}+ \frac{f}{m}
\end{cases}$$
logo, podemos definir um estado $x=\begin{pmatrix}x_{1} \\ x_{2}\end{pmatrix}$ e considerar que a "entrada" deste sistema é $u=f$ e temos:
$$\dot{x}=Ax+Bu~~\to~~ \dot{x}=\begin{pmatrix}0 & 1 \\ 0 & \frac{-b}{m}\end{pmatrix}x + \begin{pmatrix}0 \\ \frac{1}{m}\end{pmatrix}f$$
- E temos um sistema descrito conforme equações do espaço de estados!

### Discreto
- Voltemos à área de análise de sinal. Teremos sempre sinais discretos no tempo, devido ao sampling com que medimos o sinal.
- Podemos discretizar uma derivada assim:
$$\dot{x}= \frac{dx}{dt}\simeq \frac{x(k+1) - x(k)}{T_{s}}$$
em que temos o tempo de sampling $T_{s}$ (inverso da frequência de sampling).
- Substituimos isto na equação genérica do espaço de estados:
$$\begin{align*}
\dot{x}&= Ax+Bu\\
\frac{x(k+1)-x(k)}{T_{s}}&= Ax(k)+Bu(k)\\
x(k+1)&= x(k) + AT_{s}x(k) + BT_{s}u(k)\\
&= [I + AT_{s}]x(k) + BT_{s}u(k)\\
&= A_{d}x(k) + B_{d}u(k)
\end{align*}$$
- Voltamos a obter a forma da equação que conhecemos!!! Notemos que $x(k+1)$ representa uma intergração e $x(k-1)$ uma diferenciação do termo $x(k)$

### Processos
- E agora voltemos ao programa desta UC: processos estocásticos. Como já vimos, quando estes são estacionários, podemos representá-los como as saídas de um SLIT cuja entrada é ruído branco.
- Assim, podemos escrever as equações de um SLIT que represente um processo estacionário:
$$\begin{cases}
x(t+1) = Ax(t) + Ke(t) \\
y(t) = Cx(t) + e(t)
\end{cases}$$
- Vamos obter a função de transferência. Para isso, começamos por alterar a 1ª equação:
$$\begin{align*}
x(t+1) &= Ax(t)+Ke(t)\\
qx(t)&= Ax(t) + Ke(t)\\
(qI-A)x(t)&= Ke(t)\\
x(t)&= (qI-A)^{-1}Ke(t)
\end{align*}$$
e substituimos na 2ª equação:
$$\begin{align*}
y(t)&= C(qI-A)^{-1}Ke(t)+e(t)\\
H(q)=\frac{y(t)}{e(t)}&= C(qI-A)^{-1}K+1
\end{align*}$$
- Claro, se definirmos $H(q)=\frac{C(q^{-1})}{A(q^{-1})}$ esta equação matricial passa a descrever um modelo de estado dum processo ARMA.

#### Inversa
- Podemos fazer uma coisa diferente: na 2ª equação isolamos o $e(t)$:
$$y(t)=Cx(t)+e(t)~~~~\to~~~~ e(t)=-Cx(t)+y(t)$$
e substituimos na 1ª equação:
$$\begin{align*}
x(t+1)&= Ax(t) + Ke(t)\\
&= (A-KC)x(t) + Ky(t)\\
qx(t)&= (A-KC)x(t) + Ky(t)\\
[qI- (A-KC)]x(t)&= Ky(t)\\
x(t)&= [qI - (A-KC)]^{-1}Ky(t)
\end{align*}$$
- Podemos substituir isto de volta na 2ª equação
$$\begin{align*}
e(t) &= -Cx(t) + y(t)\\
&= -C[qI - (A-KC)]^{-1}Ky(t) + y(t)\\
\frac{e(t)}{y(t)}=H(q^{-1})&= -C[qI-(A-KC)]^{-1}K+1
\end{align*}$$
notemos que isto é a função de transferência INVERSA: temos $H(q^{-1})$ invés de $H(q)$!!!!

- Temos que $H(q)$ tem de ser inversamente estável, logo os valores próprios de $A-KC$ são estáveis!

#### Estimador
- Com esta lógica, o melhor previsor linear de $y(t)$ é:
$$\begin{cases}
\hat{y}(t)=Cx(t) \\
x(t+1) = (A-KC)x(t) + Ky(t) 
\end{cases}$$
tendo que isto descreve um **filtro de Kalman estacionário**

# Covariâncias
## Autocovariância de MA
- Num modelo de MA temos:
$$y(t)=e(t) + c_{1}e(t-1)+\dots + c_{n}e(t-n)$$
- Vejamos como é a sequência de autocovariância neste tipo de processo:
$$\lambda_{yy}(\tau)=\mathbb{E}[y(t)y(t-\tau)]$$
- Vamos separar os vários casos:
    - $\tau=0$:    $$\begin{align*}
\lambda_{yy}(\tau)&= \lambda_{yy}(0)=\mathbb{E}[y(t)^{2}]\\
&= \mathbb{E}[e(t)^{2}+c_{1}^{2}e(t-1)^{2}+\dots+c_{n}^{2}e(t-n)^{2}+\\
&+ 2c_{1}e(t)e(t-1) + 2c_{n}e(t)e(t-n)+\dots+\\
&+ 2c_{1}c_{2}e(t-1)e(t-2)+\dots+2c_{1}c_{n}e(t-1)e(t-n)+\dots]\\
&= (1+c_{1}^{2}+\dots+c_{2}^{2})\sigma^{2}
\end{align*}$$
    - $1\le|\tau|<n$: $$\begin{align*}
\lambda_{yy}(\tau)&= \mathbb{E}[y(t)y(t-\tau)]\\
&= \mathbb{E}\bigg\{[e(t)+\dots+c_{\tau}e(t-\tau)+c_{\tau+1}e(t-\tau-1)+\dots+c_{n}e(t-n)]\times\\
&\times[e(t-\tau) + c_{1}e(t-\tau-1) + \dots c_{n}e(t-\tau-n)]\bigg\}\\
&= c_{\tau}\mathbb{E}[e(t-\tau)^{2}] + c_{1}c_{\tau+1}\mathbb{E}[e(t-\tau-1)^{2}]+\dots+c_{n-\tau}c_{n}\mathbb{E}[e(t-\tau-n)^{2}]\\
&= (c_{\tau}+c_{1}c_{\tau+1}+c_{2}c_{\tau+2}+\dots+c_{n}c_{n-\tau})\sigma^{2}
\end{align*}$$
    - $|\tau|=n$: $$\begin{align*}
\lambda_{yy}(\tau)&= \lambda_{yy}(n)=\mathbb{E}[y(t)y(t-n)]\\
&= \mathbb{E}\bigg\{ [e(t) + c_{1}e(t-1)+\dots+c_{n}e(t-n )]\times\\
&\times [e(t-n) + c_{1}e(t-n-1)+\dots+c_{n}e(t-2n)]\\
&= c_{n}\mathbb{E}[e(t-n)^{2}]=c_{n}\sigma^{2}
\end{align*}$$
    - $|\tau|>n$: $$\lambda_{yy}(\tau)=0$$
- Ou seja:
$$\lambda_{yy}^{\text{MA}}(\tau)= \begin{cases}
(1+c_{1}^{2}+c_{2}^{2}+\dots+c_{n}^{2})\sigma^{2} & , & \tau=0 \\
(c_\tau+c_{1}c_{\tau+1}+\dots +c_{n-\tau}c_{n})\sigma^{2} & , & 1\le |\tau|<n \\
c_{n}\sigma^{2} & , & |\tau|=n \\
0 & , & |\tau|>n
\end{cases}$$

**Explicação texto de cada uma das deduções**
1. Apenas ficam os termos de autocovariância, uma vez que $\mathbb{E}[e(t)e(t-\tau)]=0~,~\forall \tau\neq0$. Isto acontece porque consideramos todas as medições *independentes*, ou seja, o valor médio do produto será sempre ZERO para instantes diferentes.
2. No ramo 1 vimos que para ter uma covariância não nula, precisamos de ter termos correspondentes aos mesmos instantes. O processo $y(t-\tau)$ começa com o termo $e(t-\tau)$. Ora, no processo $y(t)$ teremos um termo $c_{\tau}e(t-\tau)$ algures entre $e(t)$ e $c_{n}e(t-n)$. Na dedução acima fiz precisamente isso. Ora, vemos que os *últimos* $n-\tau$ termos do processo $y(t)$ correspondem aos mesmos instantes que os *primeiros* $n-\tau$ termo de $y(t-\tau)$. 
3. Rapidamente vemos que o primeiro termo de $y(t-n)$ é $e(t-n)$. Ora, o último termo do processo $y(t)$ é $c_{n}y(t-n)$. Assim, é evidente que apenas estes 2 termos terão instantes coincidentes entre os 2 processos. Ou seja, ficamos apenas com $c_{n}\mathbb{E}[e(t-n)^{2}]$ na nossa covariância
4. Temos um caso mais extremo do ramo 3, em que nenhum par de termos tem o mesmo instante. Assim, ficamos com covariância nula: quando o desfasamento é maior que a ordem do modelo MA, temos processos independentes!

## Covariância cruzada de SLIT 
- Voltemos à nossa analogia em que um processo estocástico é equivalente a um SLIT excitado por ruído branco
- Temos que a resposta do SLIT será do tipo:
$$\begin{align*}
y(t)&= h(t)*u(t)\\
&= \sum\limits_{k=-\infty}^{+\infty}h(k)u(t-k)\\
&= \sum\limits_{k=-\infty}^{+\infty}h(k)q^{-k}u(t) 
\end{align*}$$
- Quando a entradad do sistema é ruído branco com média nula e variância $\sigma^{2}$, temos a covariância cruzada entre a entrada e a saída:
$$\lambda_{yu}(\tau)=\mathbb{E}[y(t)u(t-\tau)]=h(\tau)\sigma_{u}^{2}$$

**Demonstração**
- Partimos da equação de $y(t)$, multiplicando os 2 lados por $u(t-\tau)$:
$$y(t)u(t-\tau)=\sum\limits_{k=-\infty}^{+\infty}h(k)u(t-k)u(t-\tau)$$
E temos o valor esperado disso:
$$\mathbb{E}[y(t)u(t-\tau)]=\sum\limits_{k=-\infty}^{+\infty}h(k)\cdot \mathbb{E}[u(t-k)u(t-\tau)]\equiv \lambda_{yu}(\tau)$$
e temos então:
$$\lambda_{yu}(\tau)=\begin{cases}
\sigma^{2} & , & k=\tau \\
0 & , & k\neq \tau
\end{cases}=h(\tau)\sigma^{2}$$
- $h(\tau)$ é, claro, a resposta impulsional do sistema. Em sistemas causas causais temos $h(\tau)=0~,~\tau<0$

## Autocavariância de AR - 1ª ordem
- Consideremos um processo AR de 1ª ordem:
$$y(t)+a_{1}y(t-1)=e(t)$$
em que $e(t)$ é ruído branco de média nula e variância $\sigma^{2}$

### Sistema de equações
- Começamos por multiplicar os 2 lados por $y(t)$:
$$y(t)^{2}+a_{1}y(t)y(t-1)=y(t)e(t)$$
e calculamos o valor esperado:
$$\begin{align*}
\mathbb{E}[y(t)^{2}+a_{1}y(t)y(t-1)]&= \mathbb{E}[y(t)e(t)]\\
\mathbb{E}[y(t)^{2}] + a_{1}\mathbb{E}[y(t)y(t-1)]&= \mathbb{E}[y(t)e(t)]\\
\lambda_{yy}(0)+ a_{1}\lambda_{yy}(1)&= \lambda_{ye}(0)
\end{align*}$$
notemos que atrás fizemos $\mathbb{E}[e(i)e(j)]=\delta_{ij}\sigma^{2}$, mas isso apenas acontece com ruído branco, porque *todos os instantes são independentes*! Aqui temos autocovariância com deslocamento $\tau$.

- Podemos agora multiplicar os 2 lados por $y(t-1)$ e calcular o valor esperado:
$$\begin{align*}
y(t-1)y(t) + a_{1}y(t-1)^{2}&= y(t-1)e(t)\\
\mathbb{E}[y(t-1)y(t)] + a_{1}\mathbb{E}[y(t-1)^{2}]&= \mathbb{E}[y(t-1)e(t)]\\
\lambda_{yy}(1) + a_{1}\lambda_{yy}(0) &= \lambda_{ey}(1) = \lambda_{ye}(-1) 
\end{align*}$$
notemos que o caso de autocovariância $\lambda_{yy}$ não depende de onde está o deslocamento $\tau$: $\mathbb{E}[y(t)y(t-1)]=\mathbb{E}[y(t-1)y(t)]=\lambda_{yy}(1)$. Já no caso de covariância cruzada o termo de deslocamento importa muito: $\mathbb{E}[y(t)e(t-1)]=\lambda_{ye}(1)\neq\lambda_{ye}(-1)=\mathbb{E}[y(t-1)e(t)]$.

- Juntando estas 2 equação temos um sistema:
$$\begin{cases}
\lambda_{yy}(0) + a_{1}\lambda_{yy}(1) = \lambda_{ye}(0) \\
\lambda_{yy}(1) + a_{1}\lambda_{yy}(0) = \lambda_{ye}(-1)
\end{cases}$$

### Resposta impulsional
- Podemos pegar na equação do modelo AR e isolar o ruído branco:
$$\begin{align*}
y(t) + a_{1}y(t-1)&= e(t)\\
y(t)+a_{1}q^{-1}y(t)&= e(t)\\
[1+a_{1}q^{-1}]y(t)&= e(t)
\end{align*}$$
e temos:
$$y(t)=\frac{1}{1+a_{1}q^{-1}}e(t)$$

**Série geométrica**
- A soma de uma série geométrica é:
$$\sum\limits_{i=1}^{n}ar^{i-1}=\frac{a(1-r^{n})}{1-r}$$
e vemos que se tivermos $a=1,r=x,n\to\infty$ obtemos:
$$\sum\limits_{i=1}^{\infty}x^{i-1}=1+x+x^{2}+x^{3}+\dots=\frac{1}{1-x}$$
(sendo que é necessário $|x|<1$ para haver convergência)

**Maneira correta : divisão longa**
- A maneira "correta" de obter a resposta impulsional é através de divisão longa:
![[divisao longa 1.png]]
- Ao colocar isto no Desmos, vemos que isto apenas se aplica para $|x|<1$:
![[aproximacao divisao longa 1.png]]

### Resolver o sistema
- Acima vimos que a covariância de um sistema representado por um SLIT excitado por ruído branco é dada por
$$\lambda_{yu}(\tau)=h(\tau)\sigma_{u}^{2}$$
- Ora no sistema acima temos:
$$\begin{align*}
\lambda_{ye}(0)&= h(0)\sigma^{2}=(-a_{1})^{0}\sigma^{2}=\sigma^{2}\\
\lambda_{ye}(-1)&= h(-1)\sigma^{2}=0
\end{align*}$$

- Apenas resta $\lambda_{yy}(0)$ e $\lambda_{yy}(1)$, que resolvemos no sistema:
$$\begin{cases}
\lambda_{yy}(0)+a_{1}\lambda_{yy}(1)=\sigma^{2} \\
\lambda_{yy}(1)+a_{1}\lambda_{yy}(0)=0
\end{cases}\Leftrightarrow\begin{pmatrix} 1 & a_{1} \\ a_{1} & 1\end{pmatrix}\begin{pmatrix}\lambda_{yy}(0) \\ \lambda_{yy}(1)\end{pmatrix}=\begin{pmatrix}\sigma^{2} \\ 0\end{pmatrix}$$

#### Cramer
- Aplicamos a regra de Cramer:
![[regra de cramer.png|450]]
obtemos
$$\begin{align*}
\lambda_{yy}(0)&= \frac{\begin{vmatrix}\sigma^{2} & a_{1} \\ 0 & 1\end{vmatrix}}{\begin{vmatrix}1 & a_{1} \\ a_{1} & 1\end{vmatrix}}=\frac{1}{1-a_{1}}\sigma^{2}=\frac{(-a_{1})^{0}}{1-a_{1}^{2}}\sigma^{2}\\\\
\lambda_{yy}(1)&= \frac{\begin{vmatrix}1 & \sigma^{2} \\ a_{1} & 0\end{vmatrix}}{\begin{vmatrix}1 & a_{1} \\ a_{1} & 1\end{vmatrix}}=\frac{-a_{1}}{1-a_{1}}\sigma^{2}=\frac{(-a_{1})^{1}}{1-a_{1}^{2}}\sigma^{2}
\end{align*}$$
e temos os 2 primeiros termos da série de covariância!!

### Resto da série de covariância
- Podemos multiplicar a equação do modelo AR por $y(t-\tau)~,~\tau>1$ e temos
$$\begin{align*}
y(t)y(t-\tau) + a_{1}y(t-1)y(t-\tau)&= y(t-\tau)e(t)\\
\mathbb{E}[y(t)y(t-\tau)] + a_{1}\mathbb{E}[y(t-1)y(t-\tau)]&=\mathbb{E}[y(t-\tau)e(t)]\\
\lambda_{yy}(\tau)+a_{1}\lambda_{yy}(\tau-1)&= \lambda_{ye}(-\tau) 
\end{align*}$$
- Como já vimos, $\lambda_{ye}(\tau)=0~,~\tau<0$. Assim esta equação resulta em:
$$\lambda_{yy}(\tau)=-a_{1}\lambda_{yy}(\tau-1)$$
- Isto  é observado para qualquer $\tau>1$ logo:
$$\lambda_{yy}(\tau>1)=(-a_{1})^{\tau-1}\lambda_{yy}(1)=\frac{(-a_{1})^{\tau}}{1-a_{1}^{2}}\sigma^{2}$$
e temos toda a sequência de covariância!
- Notemos que esta equação aplica-se para qualquer $\tau\ge 0$. Se quisermos generalizar para *qualquer* deslocamento basta fazer:
$$\lambda_{yy}(-\tau)=\lambda_{yy}(\tau)=\frac{(-a_{1})^{|\tau|}}{1-a_{1}^{2}}\sigma^{2}~~,~~ \forall \tau\in\mathbb{Z}$$
e podemos representar graficamente esta sequência:
![[sequencia covariancia modelo AR.png|500]]

## Autocavariância de AR - 2ª ordem
- Temos a equação do modelo
$$y(t)-a_{1}y(t-1) + a_{2}y(t-2)=e(t)$$
em que $e(t)$ tem média nula e variância $\sigma^{2}$.

**Sistema de equações**
- Multiplicamos a equação por $y(t),y(t-1),y(t-2)$, calculamos o valor esperado e obtemos 3 equações:
$$\begin{cases}
\lambda_{yy}(0)+a_{1}\lambda_{yy}(1)+a_{2}\lambda_{yy}(2)=\sigma^{2} \\
\lambda_{yy}(1)+a_{1}\lambda_{yy}(0)+a_{2}\lambda_{yy}(1)=0 \\
\lambda_{yy}(2)+a_{1}\lambda_{yy}(1)+a_{2}\lambda_{yy}(0)=0
\end{cases}\Leftrightarrow \begin{pmatrix}1 & a_{1} & a_{2} \\ a_{1} & 1+a_{2} & 0 \\ a_{2} & a_{1} & 1\end{pmatrix}\begin{pmatrix}\lambda_{yy}(0) \\ \lambda_{yy}(1) \\ \lambda_{yy}(2)\end{pmatrix}=\begin{pmatrix}\sigma^{2} \\ 0 \\ 0\end{pmatrix}$$
- Aqui não deduzimos a resposta impulsional e $\lambda_{ye}(\tau)$. Consideramos sempre que temos $\lambda_{ye}(0)=\sigma^{2}$ e $\lambda_{ye}(\tau<0)=0$. Fazemos isto **sempre para o modelo AR**.
- Notemos, claro, podíamos calcular a divisão longa;
![[divisao longa 2.png]]
![[aproximacao divisao longa 2.png]]
- Ver nota sobre divisão longa [[PES - Divisao Longa]]

**Regra de Cramer**
- Obtemos:
$$\begin{align*}
\lambda_{yy}(0)=\frac{1+a_{2}}{(1-a_{2})(1+a_{2}-a_{1}^{2})}\sigma^{2}\\
\lambda_{yy}(1)=\frac{-a_{1}}{(1-a_{2})(1+a_{2}-a_{1}^{2})}\sigma^{2}\\
\lambda_{yy}(2)=\frac{a_{1}^{2}-a_{2}^{2}-a_{2}}{(1-a_{2})(1+a_{2}-a_{1}^{2})}\sigma^{2}
\end{align*}$$

**Generalizar**
- Tal como acima, multiplicamos os 2 lado da equação por $y(t-\tau)$ e calculamos o valor esperado. Obtemos:
$$\lambda_{yy}(\tau) + a_{1}\lambda_{yy}(\tau-1)+a_{2}\lambda_{yy}(\tau-2)=\lambda_{yy}(-\tau)=0$$
logo
$$\lambda_{yy}(\tau)=-a_{1}\lambda_{yy}(\tau-1) - a_{2}\lambda_{yy}(\tau-2)$$
- Esta equação é recursiva e aplicável para $\tau>2$.

## Autocavariância de AR - nª ordem
- Temos o modelo de ordem $n$:
$$y(t)+a_{1}(t-1)+\dots+a_{n}y(t-n)=e(t)$$
em que $e(t)$ é ruído branco de média nula e variância $\sigma^{2}$.

**Sistema de equações**
- Multiplicamos os 2 lados por $y(t),y(t-1),\dots,y(t-n)$ e calculamos o valor esperado. Obtemos um sistema de $n$ equações:
$$\begin{cases}
\lambda_{yy}(0) + a_{1}\lambda_{yy}(1)+a_{2}\lambda_{yy}(2) +\dots+a_{n}\lambda_{yy}(n)=\sigma^{2} \\
\lambda_{yy}(1)+a_{1}\lambda_{yy}(0)+a_{2}\lambda_{yy}(1)+\dots+a_{n}\lambda_{yy}(n-1)=0 \\
\lambda_{yy}(2)+a_{1}\lambda_{yy}(1)+a_{2}\lambda_{yy}(0)+\dots+a_{n}\lambda_{yy}(n-2) =0\\
\quad\quad\vdots \\
\lambda_{yy}(n)+a_{1}\lambda_{yy}(n-1)+a_{2}\lambda_{yy}(n-2)+\dots+a_{n}\lambda_{yy}(0)=0
\end{cases}$$
- Como atrás, consideramos que $\lambda_{ye}(0)=\sigma^{2}$ e $\lambda_{ye}(\tau<0)=0$
- De seguida resolvemos o sistema e obtemos $\lambda_{yy}(0),\lambda_{yy}(1),\dots,\lambda_{yy}(n)$
- Finalmente, para obter os termos da sequência de covariância com $\tau>n$ simplemsnete usamos:
$$\lambda_{yy}(\tau)=-a_{1}\lambda_{yy}(\tau-1)-a_{2}\lambda_{yy}(\tau-2)\dots-a_{n}\lambda_{yy}(\tau-n)$$

## Autocovariância ARMA
### Ordem 1
- A equação que descreve este modelo é:
$$y(t) + a_{1}y(t-1)=e(t)+c_{1}e(t-1)$$
em que $e(t)$ é ruído branco de média nula e variância $\sigma^{2}$.

**Sistema de equações**
- Multiplicamos os 2 lados da equação por $y(t),y(t-1)$ e determinamos os valores esperados. Obtemos 2 equações:
$$\begin{cases}
\lambda_{yy}(0)+a_{1}\lambda_{yy}(1)=\lambda_{ye}(0)+c_{1}\lambda_{ye}(1) \\
\lambda_{yy}(1)+a_{1}\lambda_{yy}(0)=\lambda_{ye}(-1) + c_{1}\lambda_{yy}(0)
\end{cases}$$

**Resposta impulsional**
- Temos:
$$\begin{align*}
y(t) + a_{1}y(t-1)&= e(t)+c_{1}e(t-1)\\
y(t)+a_{1}q^{-1}y(t)&= e(t)+c_{1}q^{-1}e(t)\\
\frac{y(t)}{e(t)}=H(q)&= \frac{1+c_{1}q^{-1}}{1+a_{1}q^{-1}}
\end{align*}$$
- Usando divisão longa temos:
![[divisao longa 3.png]]
ou seja:
$$H(x)=1+\sum\limits_{k=0}^{\infty}(-1)^{k}a_{1}^{k}(c_{1}-a_{1})x^{k+1}$$
![[aproximacao divisao longa 3.png]]
- Que nos dá a resposta impulsional:
$$\begin{align*}
h(t)&= H(q^{-1})\delta(t)\\
h(t)&= \delta(t) + \sum\limits_{k=0}^{\infty}(-1)^{k}a_{1}^{k}(c_{1}-a_{1})q^{-k-1}\delta(t)\\
&= \delta(t) + \sum\limits_{k=0}^{\infty}(-1)^{k}a_{1}^{k}(c_{1}-a_{1})\delta(t-k-1)\\
&= \delta(t) + (c_{1}-a_{1})\delta(t-1)-a_{1}(c_{1}-a_{1})\delta(t-2)+\dots
\end{align*}$$
logo temos:
$$h(0)=1 \quad ;\quad h(1)=c_{1}-a_{1} \quad;\quad h(2)=-a_{1}(c_{1}-a_{1})$$
e consideramos $h(-1)=0$ para o sistema ser *causal*.

**Resolver sistema**
- Considerando que $\lambda_{ye}(\tau)=h(\tau)\sigma_{e}^{2}$ ficamos com o sistema assim:
$$\begin{pmatrix}1 & a_{1} \\ a_{1} & 1\end{pmatrix}\begin{pmatrix}\lambda_{yy}(0) \\ \lambda_{yy}(1)\end{pmatrix}=\begin{pmatrix}1+c_{1}(c_{1}-a_{1}) \\ c_{1}\end{pmatrix}\sigma^{2}$$
e temos
$$\begin{cases}
\lambda_{yy}(0)=\frac{(1+c_{1}^{2}-2c_{1}a_{1})}{1-a_{1}^{2}}\sigma^{2} \\
\lambda_{yy}(1)=\frac{(1-c_{1})(c_{1}-a_{1})}{1-a_{1}^{2}}\sigma^{2}
\end{cases}$$

**Outros termos**
- Se multiplicarmos a equação do modelo ARMA por $y(t-\tau)~,~\tau>1$ e calcularmos o valor esperado, obtemos
$$\lambda_{yy}(\tau)+a_{1}\lambda_{yy}(\tau-1)=0~~\to~~ \lambda_{yy}(\tau)=a_{1}\lambda_{yy}(\tau-1)$$

### Ordem n
- O modelo ARMA de ordem $n$ é definido como
$$y(t)+\dots+a_{n}y(t-n)=e(t)+\dots+c_{n}e(t-n)$$
em que $e(t)$ é ruído branco de média nula e variância $\sigma^{2}$.

- Tal como já fizemos acima, multiplicamos os 2 lados por $y(t),y(t-1),\dots,y(t-n)$ e calculamos os valores esperados. Obtemos:
$$\begin{cases}
\lambda_{yy}(0)+a_{1}\lambda_{yy}(1)+\dots+a_{n}\lambda_{yy}(n)=[1+c_{1}h(1)+\dots+c_{n}h(n)]\sigma^{2} \\
\lambda_{yy}(1)+a_{1}\lambda_{yy}(0)+\dots+a_{n}\lambda_{yy}(n-1)=[c_{1}h(0)+\dots+c_{n}h(n-1)]\sigma^{2} \\
\quad \quad \vdots \\
\lambda_{yy}(n)+a_{1}\lambda_{yy}(n-1)+\dots+a_{n}\lambda_{yy}(0)=c_{n}h(0)\sigma^{2}
\end{cases}$$
em que já utilizamos $\lambda_{ye}(\tau)=h(\tau)\sigma^{2}$.
- Fazendo a divisão longa da função transferência:
$$H(q)=\frac{1+c_{1}q^{-1}+\dots+c_{n}q^{-n}}{1+a_{1}q^{-1}+\dots+c_{n}q^{-n}}$$
e podemos obter a resposta impulsional ao fazer $h(t)=H(q)\delta(t)$
- Finalmente, podemos multiplicar a equação do modelo por $y(t-\tau)$ e determinar o valor esperado. Obtemos:
$$\lambda_{yy}(\tau)=-a_{1}\lambda_{yy}(\tau-1)-\dots-a_{n}\lambda_{yy}(\tau-n)$$
