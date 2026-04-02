Começamos aqui a Parte 2 de PMAP
# Revisão de probabilidades
- Temos as VAs $X,Y$ dos espaços $\mathbb{R}^{n},\mathbb{R}^{m}$. 

## PDF
- Podemos definir as suas funções de densidade de probabilidade (PDF)
    - $f_{X}:\mathbb{R}^{n}\to\mathbb{R}_{0}^{+}~~~~,~~ (\int_{\mathbb{R}^{n}}f_{X}(x)dx=1)$
    - $f_{Y}:\mathbb{R}^{m}\to\mathbb{R}_{0}^{+}~~~~,~~ (\int_{\mathbb{R}^{m}}f_{Y}(y)dy=1)$
- E temos a função de probabilidade conjunta:
$$f_{X,Y}:\mathbb{R}^{n+m}\to \mathbb{R}_{0}^{+}~~~~,~~ \int_{\mathbb{R}^{n+m}}f_{X,Y}(x,y)dxdy=1$$
e podemos definir:
$$f_{X}(x)=\int_{\mathbb{R}^{m}}f_{X,Y}(x,y)dy~~,~~f_{Y}(y)=\int_{\mathbb{R}^{n}}f_{X,Y}(x,y)dx$$
- MAS, no caso de **x,y independentes** temos
$$\text{X,Y independentes:}~~~~ f_{X,Y}(x,y)=f_{X}(x)f_{Y}(y)$$

## Valor esperado
- Podemos definir o valor esperado de várias VAs como:
$$\mathbb{E}[X]=\mu_{X}=\int_{\mathbb{R}^{n}}xf_{X}(x)dx ~~~~,~~~~ \mathbb{E}[Y]=\mu_{y}=\int_{\mathbb{R}^{m}}yf_{Y}(y)dy$$
e podemos definir ainda o valor médio do produto de 2 variáveis (usa-se a PDF conjunta):
$$\mathbb{E}[XY^{T}]=\int_{\mathbb{R}^{n+m}}xy^{T}f_{X,Y}(x,y)dxdy$$

## Covariâncias
- Podemos definir como
$$\begin{align*}
\text{cov}(X)&= \text{cov}(X,X)\equiv\text{autocovariância de X}\\
&= \mathbb{E}[(X-\mathbb{E}[X])(X-\mathbb{E}[X])^{T}]\\
&= \int_{\mathbb{R}^{n}}(x-\mu_{X})(x-\mu_{X})^{T}f_{X}(x)dx\\
\text{cov}(Y)&= \mathbb{E}[(Y-\mathbb{E}[Y])(Y-\mathbb{E}[Y])^{T}]\\
&= \int_{\mathbb{R}^{m}}(y-\mu_{Y})(y-\mu_{Y})^{T}f_{Y}(y)dy\\
\text{cov}(X,Y)&\equiv \text{covariância cruzada de X e Y}\\
&= \mathbb{E}[(X-\mathbb{E}[X])(Y-\mathbb{E}[Y])^{T}]\\
&= \int_{\mathbb{R}^{n+m}}(x-\mu_{X})(y-\mu_{Y})^{T}f_{X,Y}(x,y)dxdy
\end{align*}$$

### Escalar
- Se tivermos $X,Y$ escalar então teríamos **variâncias** e não covariâncias
- Representaríamos estas com $\sigma_{X}^{2},\sigma_{Y}^{2},\sigma_{XY}^{2}$
- E podemos definir o coeficiente de correlação:
$$\rho_{XY}=\frac{\sigma_{XY}}{\sigma_{X}\sigma_{Y}}$$

### Propriedades de média e cov
- Temos **sempre**
$$\begin{align*}
\mathbb{E}[X+Y]&= \mathbb{E}[X]+\mathbb{E}[Y]\\
\text{cov}(X,Y)&= \mathbb{E}[XY^{T}] - \mathbb{E}[X]\mathbb{E}[Y]^{T}\\
\text{cov}(X+Y)&= \text{cov}(X) + \text{cov}(Y) + \text{cov}(X,Y)+\text{cov}(Y,X)
\end{align*}$$

- Quando temos $X,Y$ **independentes**:
$$\begin{align*}
\mathbb{E}[XY^{T}]&= \mathbb{E}[X]\mathbb{E}[Y]^{T}\\
\text{cov}(X,Y)&= 0\\
\text{cov}(X+Y)&= \text{cov}(X) + \text{cov}(Y)
\end{align*}$$

- Se tivermos uma constante $A$:
$$\begin{align*}
\mathbb{E}[X+A]&= \mathbb{E}[X]+A\\
\mathbb{E}[AX]&= A \mathbb{E}[X]\\
\text{cov}(X+A)&= \text{cov}(X)\\
\text{cov}(AX)&= A\text{cov}(X)A^{T}
\end{align*}$$

#### Independentes VS não correlacionados
- Ora, quando temos VAs independentes, temos $\text{cov}(X,Y)=0$.
- Mas, se tivermos 2 variáveis desconhecidas $X,Y$ e calcularmos que $\text{cov}(X,Y)=0$ NÃO podemos dizer que são independentes. Apenas dizemos que são **não correlacionados**.
- Assim:
    - 2 variáveis independentes SÃO não correlacionadas
    - 2 variáveis não correlacionadas PODEM NÃO SER independentes
- Isto quer dizer que "assumir que X,Y são não correlacionadas" é uma assunção *mais fraca* do que dizer que são independentes.

- Quando temos variáveis não correlacionadas, temos que
$$\text{cov}(X+Y)=\text{cov}(X)+\text{cov}(Y)$$

## PDF condicional
- A PDF de $X$ dado que $Y=y$ é dada por
$$f_{X|Y}(x|y)=\frac{f_{X,Y}(x,y)}{f_{Y}(y)}~~~~,~~ f_{Y}(y)>0$$
- A PDF de $Y$ dado que $X=x$ é:
$$f_{Y|X}(y|x)=\frac{f_{X,Y}(x,y)}{f_{X}(x)}~~~~,~~f_{X}(x)>0$$

### Teorema de Bayes
- Podemos aplicar o teorema de Bayes a estas probabilidades condicionais:
$$\begin{align*}
f_{X|Y}(x|y)&= \frac{f_{Y|X}(y|x)f_{X}(x)}{f_{Y}(y)}\\
f_{Y|X}(y|x)&= \frac{f_{X|Y}(x|y)f_{Y}(y)}{f_{X}(x)}
\end{align*}$$

## Distribuição normal
- Podemos ter uma variável com $k$ dimensões que segue uma distribuição normal:
$$X=(x_{1},x_{2},\dots,x_{k})^{T}~\sim~ N(\mu,\Sigma)$$
em que temos a média $\mu$ e covariância $\Sigma$
- Isto quer dizer que a variável segue a seguinte distribuição gaussiana:
$$f_{X}(X)=\frac{1}{\sqrt{(2\pi)^{k}|\Sigma|}}\exp\left(- \frac{1}{2} (X-\mu)^{T}\Sigma^{-1}(X-\mu)\right)$$

### Exemplo 2D
- Temos duas variáveis $X_{1},X_{2}$ que são normais *em conjunto*:
$$X=\begin{bmatrix}X_{1} \\ X_{2}\end{bmatrix}\sim N \left( \begin{bmatrix}\mu_{1} \\ \mu_{2}\end{bmatrix}~,~ \begin{bmatrix}\Sigma_{11} & \Sigma_{12} \\ \Sigma_{12}^{T} & \Sigma_{22}\end{bmatrix} \right)$$
- Notemos que podemos sempre assumir uma matriz de covariância simétrica como acima.

#### Soma
A soma destas variáveis será:
$$Z=A_{1}X_{1}+A_{2}X_{2}$$
que também segue uma distribuição normal:
$$\begin{align*}
\mathbb{E}[Z]&= A_{1}\mu_{1}+A_{2}\mu_{2}\\
\text{cov}(Z)&= A_{1}\Sigma_{11}A^{T}_{1} + A_{1}\Sigma_{12}A_{2}^{T}+A_{2}\Sigma_{12}^{T}A_{1}^{T}+A_{2}\Sigma_{22}A_{2}^{T}
\end{align*}$$

#### Condicional
Consideremos que conhecemos um valor $X_{2}=a$. Nesse caso:
$$\begin{align*}
&(X_{1}|X_{2}=a)\sim N(\overline{\mu},\overline{\Sigma})\\
\\
\overline{\mu}&= \mu_{1}+\Sigma_{12}\Sigma_{22}^{-1}(a-\mu_{2})\\
\overline{\Sigma}&= \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{12}^{T}
\end{align*}$$

#### Elipses de incerteza
- São regiões do espaço (neste exemplo em 2D) em que temos **PDF constante**. Ou seja, quando podemos igualar o expoente da exponencial a uma constante:
$$(X-\mu)^{T}\Sigma^{-1}(X-\mu)=s$$
- A área dentro da elipse correspondem a uma probabilidade dessa região. 
- O caso mais simples é quando temos variáveis independentes/sem correlação:
$$\Sigma=\begin{pmatrix}\sigma_{X}^{2} & 0 \\ 0 & \sigma_{Y}^{2}\end{pmatrix}~~\to~~ \left(\frac{x}{\sigma_{X}}\right)^{2}+\left(\frac{y}{\sigma_{Y}}\right)^{2}=s$$
em que temos uma elipse simples. $\sigma_{X},\sigma_{Y}$ controlam os eixos. 
- Ao aumentar o $s$ aumentamos a área e a probabilidade contida:
![[elipse incerteza.png|600]]

# Sistemas lineares estocásticos
- Temos um sistema SS discreto:
$$\begin{cases}
x_{k+1}&=Ax_{k} + Bu_{k} + Fw_{k} \\
y_{k}&=Cx_{k}+Gv_{k}
\end{cases}$$
em que temos matrizes $A\in\mathbb{R}^{n\times n},B\in\mathbb{R}^{n\times p},F\in\mathbb{R}^{n\times q},C\in\mathbb{R}^{m\times n},G\in\mathbb{R}^{m\times r}$
- E temos as variáveis: 
    - $u_{k}$ é o sinal de entrada determinístico
    - $w_{k}$ e $v_{k}$ são ruído branco gaussiano independente ($w,v$ são independentes um do outro e cada instante é independente dos outros) do tipo $w_{k},v_{k}\sim N(0,1)$
    - $x_{0}$ é uma VA gaussiana que é independente dos ruídos $w_{k},v_{k}$, sendo que $P_{0}=\text{cov}(x_{0})$

**Probabilidade aplicada**
- Podemos definir: $\hat{x}_{k}=\mathbb{E}[x_{k}]~~~~,~~~~P_{k}=\text{cov}(x_{k})$
- Assim, para cada iteração/instante podemos calcular valores estatísticos:
$$\begin{align*}
\hat{x}_{k+1}&= \mathbb{E}[Ax_{k}+Bu_{k}+Fw_{k}]=A \hat{x}_{k} + Bu_{k}\\
P_{k+1}&= \text{cov}(Ax_{k}+Bu_{k}+Fw_{k})\\
&= \text{cov}(Ax_{k}) + \text{cov}(Fw_{k})\\
&= A \text{cov}(x_{k})A^{T}+ F \text{cov}(w_{k})F^{T}\\
&= AP_{k}A^{T}+FF^{T}
\end{align*}$$
- NOTAS:
    - Recordemos que $w_{k}\sim N(0,1)$ logo $\mathbb{E}[w_{k}]=0~,~\text{cov}(w_{k})=1$
    - Assim, na equação de $\hat{x}_{k+1}$ ficamos apenas com $x,u$
    - Na equação de $P_{k+1}$ perdemos o termo $u_{k}$ porque este é um sinal determinístico, logo consideramos que não tem incerteza nem variância: $\text{cov}(u_{k})=0$

### Simulação monte carlo
- Consideremos um sistema discreto $x_{k+1}=Ax_{k}+Bu_{k}+Fw_{k}$
- Fazer uma simulação monte carlo consiste em:
    1. Gerar (na realidade, fazer sampling) das variáveis $x_{0},w_{k}$
    2. Simular a evolução do sistema dinâmico
    3. Repetir 2 para muitos instantes de tempo (para $k\gg1$)

- Podemos definir a média e covariância amostral:
$$\begin{align*}
\overline{X}&= \frac{1}{N}\sum\limits_{i=1}^{N}X_{i}\\
S&= \frac{1}{N-1}\sum\limits_{i=1}^{N}(X_{i}-\overline{X})(X_{i}-\overline{X})^{T}\\
&= \frac{1}{N-1} \left[\sum\limits_{i=1}^{N}X_{i}X_{i}^{T} - N\overline{X}~\overline{X}^{T} \right]
\end{align*}$$

#### Exemplo
- Temos o sistema:
$$x_{k+1}=0.9x_{k}+0.1w_{k}~~,~~x_{0}=0~~,~~w_{k}\sim N(0,1)$$
1. Começamos por gerar $N$ valores de $w_{k}$ ($k=1,2,\dots,N$)
2. Para cada valor de $k$ calculamos $x_{k+1}$
3. No final, pegamos nos $N$ valores e podemos: fazer histograma, calcular variância e média amostral, fazer outros tipos de análise, etc

- Neste exemplo do prof, ele fez $N=5000$, fez o histograma:
![[resultado monte carlo.png]]
(tem um erro lol, era suposto dizer $x_{5000}$)
- Foi ainda calculado:
$$\overline{X}=-2.6\cdot10^{-4}~~,~~ S=0.0504$$

# Estimação
- Num sistema real, nunca conhecemos o estado $x\in\mathbb{R}^n$. O que podemos fazer é medir $z\in\mathbb{R}^{l}$. 
- Usando isso, podemos estimar o estado: $\hat{x}$
- Vamos então ver como podemos estimar o estado de um sistema. Notemos, claro, que o estado pode incluir informações como posição, coordenadas, orientações, aceleração, etc.

### Caraterísticas desejadas em estimador
- **Unbiased** (sem viés) - o valor esperado do estimador é *igual* ao valor real que estamos a estimar: $\mathbb{E}[\hat{x}]=x$
- **Variância mínima (unbiased)** - a variância do estimador é *mínima* entre todos os estimadores sem bias
- **Consistente** - a estimativa converge para o valor real consoante o número de medições aumenta: $\lim_{N\to\infty}\hat{x}=x$

## Estimador LSQ
- Podemos modelar a medição feita como $$z=Hx+v$$
em que $x\in\mathbb{R}^{n}~,~Z\in \mathbb{R}^{l}~,~ H\in\mathbb{R}^{l\times n}~,~v\in\mathbb{R}^{l}$
- Notemos que $v$ é o **erro de medição**
- O estimador LSQ tem uma série de pressupostos:
    - $l\ge n$ - temos mais medições do que variáveis/componentes a estimar. Assim, existem medições redundantes e isso ajuda-nos a remover o efeito de outliers e ruído
    - $H$ é full rank. Isso implica que as medições são independentes entre si e que existe *solução única* do estimador LSQ

**Estimador LSQ**
- O estimador consiste então em determinar o $\hat{x}_{LS}$ tal que temos o valor mínimo de $J=(z-H \hat{x})^{T}(z-H \hat{x})$. Isto pode ser calculado de forma semelhante ao que fazemos em regressões lineares, tendo-se:
$$\boxed{\hat{x}_{LS} = (H^{T}H)^{-1}H^{T}z}$$

**Estimador LSQ pesado**
- Podemos definir uma variante do estimador com pesos. Consideremos uma matriz $R^{-1}$ simetrica definida positiva. 
- O estimador passa a desterminar o $\hat{x}_{WLS}$ que minimiza $J=(z-H \hat{x})^{T}R^{-1}(z-H \hat{x})$. Essa estimativa é dada por
$$\hat{x}_{WLS}=(H^{T}R^{-1}H)^{-1}H^{T}R^{-1}z$$

## Estimador Max Likelihood
- Neste método não assumimos nenhum modelo probabilistico para $x$ mas assumimos para $v$ - assumimos que este é ruído branco.
    - Assim temos $v\sim N(0,R)$
- Dessa forma, temos $\hat{x}_{ML}$ que *maximiza a probabilidade* das medições obtidas acontecerem.
- Isso consiste em maximizar a PDF de $v$ centrado em $Hx$:
$$f_{Z|X}(z|x)=\frac{1}{\sqrt{(2\pi)^{l}|R|}} \exp \left(-  \frac{1}{2} (z-Hx)^{T}R^{-1}(z-Hx)\right) $$
notemos que $z-Hx=v$

- Assim temos:
$$\hat{x}_{ML}=\max f_{Z|X}(z|x)=\min (z-Hx)^{T}R^{-1}(z-Hx)$$
logo
$$\boxed{\hat{x}_{ML}=(H^{T}R^{-1}H)^{-1}H^{T}R^{-1}z}$$
- Sim, isto tem a mesma equação que o LSQ pesado. Mas existe uma diferença: aqui $R$ é a matriz de covariância dos erros dos dados medidos.

## Estimador de Bayes
- No estimador LSQ não assumimos nada. No estimador ML consideramos o ruído aleatório / branco.
- Agora, no estaimdor de Bayes consideramos que $v$ é ruído branco e que conhecemos uma distribuição do estado: a *distribuição a priori* $f_{X}(x)$
- Usando esta queremos saber a distribuição *a posteriori*
$$f_{X|Z}(x|z)=\frac{f_{Z|X}(z|x)f_{X}(x)}{f_{Z}(z)}$$
- Podemos obter a melhor estimativa ao *minimizar* o custo
$$J=\int (\hat{x}-x)^{T}S(\hat{x}-x)f_{X|z}(x|z)dx$$
em que $S$ é uma matriz semidefinida positiva arbitrária. 
- Ao igualar $\frac{\partial J}{\partial \hat{x}}=0$ podemos obter $\hat{x}=\int xf_{X|z}(x|z)dx=\mathbb{E}[x|z]$

**Assumir que a priori é gaussiana**
- Tudo isto fica muito mais simples ao assumir que $v$ E $x$ ambos seguem distribuições normais:
$$v\sim N(0,R)~~~~,~~~~ x\sim N(0,P_{0})$$
e ficamos com
$$\hat{x}=(P_{0}+H^{T}R^{-1}H)^{-1}H^{T}R^{-1}z$$

## Filtro de Kalman
- Podemos escrever um sistema linear:
$$x_{k}=A_{k-1}x_{k-1}+B_{k-1}w_{k-1}$$
em que obtemos medições:
$$z_{k}=H_{k}x_{k}+v_{k}$$
- Consideramos que:
    - $w_{k}\sim N(0,Q_{k})$
    - $v_{k}\sim N(0,R_{k})$
    - $x_{0}\sim N(\hat{x}_{0},P_{0})$ - independente dos dois ruídos aciam

### Estimativas
- Tendo uma *estimativa anterior* $x_{k}^{-}$ de $x_{k}$ feita no instante anterior, podemos atualizá-la para a *estimativa atual* $x_{k}^{+}$ usando a medição do instante atual $z_{k}$
- Para isso, consideramoa que há **dependência linear**:
$$\hat{x}_{k}^{+}=K_{k}'\hat{x}_{k}^{-} + K_{k}z_{k}$$
em que os Ks são matrizes de pesos que variam em cada instante $k$.

### Erros
- Podemos definir o erro da estimativa anterior e da atual:
$$e_{k}^{-}=\hat{x}_{k}^{-}-x_{k} ~~~~,~~~~ e_{k}^{+}=\hat{x}_{k}^{+}-x_{k}$$
- Assim podemos escrever:
$$\begin{align*}
e_{k}^{+}&= \hat{x}_{k}^{+}-x_{k}\\
&= K_{k}'x_{k}^{-}+K_{k}z_{k}-x_{k}\\
&= K_{k}'x_{k}^{-}+K_{k}H_{k}x_{k}+K_{k}v_{k}-x_{k}\\
&= K_{k}'x_{k}^{-}+K_{k}H_{k}x_{k}+K_{k}v_{k}-x_{k}\\
&= K_{k}'(e_{k}^{-}+x_{k})+K_{k}H_{k}x_{k}x-x_{k}+K_{k}v_{k}\\
&= [K_{k}' + K_{k}H_{k}-I]x_{k}+K_{k}'e_{k}^{-} + K_{k}v_{k}
\end{align*}$$
- Para termos um estimador sem bias, temos que ter $\mathbb{E}[e_{k}^{-}]=0=\mathbb{E}[e_{k}^{+}]$. Como $\mathbb{E}[v_{k}]=0$, a igualdade acima só se mantem se:
$$K_{k}'=I - K_{k}H_{k}$$
- E a equação de *atualizar a estimativa* fica
$$\hat{x}_{k}^{+}=\hat{x}_{k}^{-} + K_{k}(z_{k}- H_{k}\hat{x}_{k}^{-})$$
e o erro dessa estimativa é
$$e_{k}^{+}=(I-K_{k}H_{k})e_{k}^{-}+K_{k}v_{k}$$
- Notemos, na equação de $\hat{x}_{k}^{+}$ temos um termo que é a estimativa anterior e outro que é `ganho * erro da estimativa anterior`

### Covariâncias
- Podemos definir as covariâncias das 2 estimativas como
$$P_{k}^{-}=\mathbb{E}[e_{k}^{-}(e_{k}^{-})^{T}]~~~~,~~~~P_{k}^{+}=\mathbb{E}[e_{k}^{+}(e_{k}^{+})^{T}]$$
- Podemos aplicar isto à equação de erro acima:
$$\begin{align*}
P_{k}^{+}&= \mathbb{E}[e_{k}^{-}(v_{k})^{T}]\\
&= \text{cov}([I-K_{k}H_{k}]e_{k}^{-}) + \text{cov}(K_{k}v_{k})\\
&= (I-K_{k}H_{k})P_{k}^{-}(I-K_{k}H_{k})^{T} + K_{k}R_{k}K_{k}^T 
\end{align*}$$

### Ganho de Kalman
- Para um filtro de Kalman temos que $K_{k}$ minimiza $J=\text{traço}[P_{k}^{+}]$ (o traço de uma matriz é a soma dos elementos da sua diagonal)
- Com algumas contas, isto resulta em:
$$K_{k}=P_{k}^{-}H_{k}^{T}[H_{k}P_{k}^{-}H_{k}^{T} + R_{k}]^{-1}$$
- Usando esta equação, podemos reescrever a covariância da nova estimativa como
$$P_{k}^{+}=[I - K_{k}H_{k}]P_{k}^{-}$$

### Previsões
- Ok, temos as equações que nos dão a informação sobre as estimativas *atuais*: $\hat{x}_{k}^{+},P_{k}^{+}$
- Mas o que nos verdadeiramente nos interessa no filtro de Kalman é **prever** o próximo estado. Assim, podemos definir as estimativas do próximo estado:
$$x_{k+1}^{-}=A_{k}x_{k}^{+}~~~~,~~~~ P_{k+1}^{-}=A_{k}P_{k}^{+}A_{k}^{T} + B_{k}Q_{k}B_{k}^{T}$$
- Claro, ao passarmos para o próximo instante teremos $x_{k+1}^{-}\equiv x_{k}^{-}$ -- a nossa *estimativa anterior*. Todo este ciclo repete-se

### Steady state
- Consideremos que temos um sistema estável. A certo ponto, será correto e prático considerar que a dinâmica do sistema é constante: $H_{k}\equiv H, A_{k}\equiv A, B_{k}\equiv B, R_{k}\equiv R,Q_{k}\equiv Q$.
- Assim, em cada iteração, apenas calculamos o ganho $K_{k}$ e a covariância $P_{k}$. Temos as equações:
$$\begin{align*}
K_{k}&= P_{k}^{-}H^{T}[HP_{k}^{-}H^{T}+R]^{-1}\\
P_{k}^{+}&= [I-K_{k}H]P_{k}^{-}\\
P_{k+1}^{-}&= AP_{k}^{+}A^{T}+BQB^{T}
\end{align*}$$
- Podemos em certos casos definir ainda uma solução steady state para $K_{k}$ e $P_{k}$:
$$\begin{align*}
K&= P^{-}H(HP^{-}H^{T}+R)^{-1}\\
P^{+}&= P^{-}- P^{-}H(HP^{-}H^{T}+R)^{-1}HP^{-}=[I-KH]P^{-}
\end{align*}$$

### Versão condicional
- Num filtro de Kalman com tudo steady temos:
$$\begin{align*}
z&= Hx+v\\
K&= P^{-}H(HP^{-}H^{T}+R)^{-1}\\
x^{+}&= x^{-}+K(z_{0}-Hx^{-})\\
P^{+}&= P^{-}- P^{-}H(HP^{-}H^{T}+R)^{-1}HP^{-}
\end{align*}$$
- Podemos ver que isto (as duas últimas equações) seguem as equações dum caso com variáveis juntamente normais: $(X_{1}|X_{2}=a)\sim N(\overline{\mu},\overline{\Sigma})$ em que
$$\overline{\mu}=\mu_{1} + \Sigma_{12}\Sigma_{22}^{-1}(a-\mu_{2})$$
$$\overline{\Sigma}=\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{12}^{T}$$
- Aliás podemos escrever isto como $(x|z=z_{0})\sim N(x^{+},P^{+})$ e temos
$$\begin{bmatrix}x \\ z\end{bmatrix}\sim N \left(\begin{bmatrix}x^{-} \\ Hx^{-}\end{bmatrix} ~,~\begin{bmatrix}P^{-} & P^{-}H^{T} \\ HP^{-} & HP^{-}H^{T}+R\end{bmatrix}\right)$$
e vemos que bate tudo certinho!!

### Kalman contínuo
- Ao passar para o contínuo passamos a ter derivadas invés de diferenças.
- O sistema passa a ser escrito na forma $\dot{x}=Fx+Gw$ e as medições na forma $z=Hx+v$
- Continuamos a considerar que $w,v$ são o equivalente contínuo de ruído branco, com variâncias $Q,R$
- Podemos converter em espaço contínuo:
$$\begin{align*}
t_{k+1}-t_{k}=\Delta t &\to 0\\
A_{k} &\to I+F \Delta t\\
B_{k}Q_{k}B_{k}^{T} &\to GQG^{T}\Delta t\\
R_{k} &\to R/\Delta t
\end{align*}$$

**Propagação de covariância**
- Não copiei a dedução, mas ficamos com
$$\dot{P}=FP + PF^{T}+GQG^{T}-PH^{T}R^{-1}HP$$

**Atualização de estado**
- Não copiei a dedução, mas ficamos com
$$\dot{\hat{x}}=F \hat{x}+PH^{T}R^{-1}[z-H \hat{x}]$$
em que $K=PH^{T}R^{-1}$ é o ganho de Kalman.

