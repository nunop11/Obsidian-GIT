# RESUMO DE ANALISE 2 - PARTE 1
## Vetores
- Temos que os elementos de $R^n$ podem ser vistos tanto como pontos ou vetores. Assim, tendo 2 vetores temos que são ortogonais se $A\cdot B=0$. A *norma* de uma vetor é dada por $\Vert A\Vert=\sqrt{A\cdot A}$
- Temos então a desigualdade de Cauchy-Schwartz: $\large|A\cdot B|\leq\Vert A\Vert\Vert B\Vert$
- Conclui-se então que um vetor é *unitário* se a sua norma for 1.
- Temos ainda que 2 vetores, $A$ e $B$, têm o mesmo sentido se $A=\lambda B,~~\lambda\in\mathbb R^+$, e nesse caso: $A\cdot B\geq0$. Estes vetores são também paralelos
- Desigualdade Triangular: $\large\Vert A+B\Vert\leq\Vert A\Vert+\Vert B\Vert$. Temos ainda que $\large\Vert A+B\Vert=\Vert A\Vert+\Vert B\Vert$ se verifica apenas se A e B tiverem a mesma direção e sentido)
- Temos que a distância entre dois pontos é $d(A,B)=\Vert A-B\Vert$
- Temos que $\large A\cdot B=\Vert A\Vert\Vert B\Vert\cos\theta$, pelo que o ângulo entre 2 vetores é dado por $\large\cos\theta=\frac{A\cdot B}{\Vert A\Vert\Vert B\Vert}$
- A projeção de A ao longo de B é dada por $\large P=\frac{A\cdot B}{\Vert B\Vert^2}B$
- Dois segmentos orientados (vetor com origem num ponto e fim noutro) são *equipolentes* se têm o mesmo comprimento, direção e sentido. Todos os vetores têm um vetor unico, com origem na origem do referencial, equipolente a ele.
- Um vetor diz-se *de uma reta* ou *de um plano* se tem a direção da reta ou de uma reta do plano
- Em 3D: 2 planos são perpendiculares se os seus vetores normais são perpendiculares e são paralelos se os vetores normais são paralelos. O ângulo entre os planos é o menor ângulo entre os vetores normais.
- Produto vetorial: $$A\times B=\begin{vmatrix}\hat i&\hat j&\hat k\\A_1& A_2& A_3\\ B_1& B_2& B_3\end{vmatrix}$$
- Propriedades de produto vetorial:
![[Pasted image 20220625231400.png]]

## Funções escalares
- $\text{Dom }f$ é domínio e é conjunto dos pontos em que a func está definida. $\text{Im }f$ é a imagem/contradomínio, conjunto das imagens de todos os pontos do domínio. Gráfico: $\text{Gra } f=\{(X, f(X))\in \mathbb R^{m+n}:X\in\text{Dom }f\}\subseteq \mathbb R^{m+n}$ 
- No caso de $n=1$ temos um *conjunto de nível de c*. Para $R^2$ estas são curvas de nível, para $R^3$ são superfície de nível e para $R^{~m\geq4}$ são hipersuperfícies de nível. Para R2 e R3 estes conjuntos são aquilo que resulta da interseção do gráfico com a reta $y=c$ (R2) ou plano $z=c$ (R3).

# Curvas
- Uma *curva* é uma função $c:I\to\mathbb R^n$ em que $I$ é um intervalo degenerado (não vazio e não reduzido a um ponto). À imagem de $c$ dá-se o nome de *traço da curva*.
- Curva ==**suave**== - curva em que todas as derivadas consideradas existem e são contínuas no domínio da curva (infinitamente derivável, na prática)
- Curva ==**regular**== - curva em que $c'$ nunca se anula.

---
### Reparametrização
- **Mudança de parâmetro** - Bijeção de $\lambda:J\to I$ entre intervalos de R, tal que $\lambda$ e $\lambda^{-1}$ são ambas suaves.
- Seja $\gamma:I\to\mathbb R^3$ uma curva. A $\overline\gamma =\gamma \circ\lambda$ chama-se à **reparametrização** de $\gamma$ com $\lambda$
---

### Bola
- $B(X_0;r)$ é a bola de raio $r$ e centro em $X_0$. Este conjunto é dado por $$B(X_0,r)=\{X\in\mathbb R^n:\Vert X-X_o\Vert\leq r\}$$
Basicamente, é o conjunto dos pontos a uma distância r de $X_0$
- Um conjunto $A\subseteq\mathbb R^n$ é ==*limitado*== se existir uma bola $B(X_0,r)$ tal que $A\subseteq B(X_0,r)$
- Um conjunto $A\subseteq\mathbb R^n$ é ==*aberto*== se para todo o $X\in A$ existir $\varepsilon>0$ tal que $B(X;\varepsilon)\subset A$. Por outras palavras, não tem um limite bem definido. Se tivesse, não poderia existir uma bola de $\varepsilon\neq0$ para os pontos dos limites de A.
- Um conjunto é ==*fechado*== se o seu conjunto complementar for aberto.

### Ponto de Acumulação
- Seja $A\subseteq\mathbb R^n$ . Um ponto $X_0$ de Rn ´um **ponto de acumulação** de A se $$\forall\delta>0~~(B(X_0;\delta)\backslash\{X_0\})~\cap~A\neq0$$
Ou seja, é ponto de acumulaçãp se existirem elementos do conjunto próximos a $X_0$, independentemente de o quão próximo estamos a procurar.

## Limite
- Só existem em pontos de acumulação.
- Seja I um conjunto de reais, $t_0$ um ponto de acumulação de E e $c:I\to\mathbb R^n$ uma curva. Temos que o limite de $c$ quando $t$ tende para $t_0$ é:
$$\lim_{t\to t_0}c(t)=a$$
Este limite existe se $$\forall\varepsilon>0,\exists\delta>0:~(t\in I\wedge0<|t-t_0|<\delta)\Rightarrow \Vert c(t)-a\Vert<\varepsilon$$
- Uma curva tem limite se todas as *funções componentes de ordem i* também têm.

## Continuidade
Tendo $c:I\to\mathbb R^n$ uma função e $t_0\in I$. 
- Se $t_0$ for um ponto isolado de I, dizemos que a função é contínua em $t_0$
- Se for um ponto de acumulação, dizemos que é contínua se existir limite me $t_0$.

- Uma curva $c$ é contínua num intervalo $J\subseteq I$ se for contínua em todos os pontos de J.
- Mais uma vez, temos que uma curva é contínua num ponto se todas as suas funções componentes também o forem.

#### Continuidade e operaçãoes
Sendo $\alpha,\beta:I\to\mathbb R^n$ duas curvas e $~f:I\to\mathbb R,~g:J\to\mathbb R$ duas funções.
- Se $\alpha$ e $\beta$ forem contínuas em I, então $\alpha+\beta$ também é
- Se $\alpha$ e $f$ forem contínuas em $t_0\in I$, então $f\alpha$ também o é.
- Se $g$ é contínua em $x_0\in J$ e $\alpha$ é contínua em $t_0=g(x_0)\in I$, então a curva $\alpha\circ g:J\to\mathbb R$ é contínua em $x_0$.
---

## Derivadas
Para uma curva $c: I\to\mathbb R^n$, se existir $$\lim_{t\to t_0}\frac{c(t)-c(t_0)}{t-t_0}=c'(t_0)$$
então diz-se que c é ==derivável== em t0.
- $c$ é derivável em I se for derivável em todos os pontos de I.
- Uma curva é de **==classe==** $C^n$ se exisitr e for contínua a sua derivada de ordem $n$.

- Curva **SUAVE**- Curva de classe $C^n$ em que $n\leq\infty$ é suficientemente grande para abarcar todas as derivadas que precisamos de considerar. Ou seja, é uma curva em que todas as derivadas consideradas existem e são contínuas no domínio da curva.

### Velocidade e Aceleração
- $c'(t_0)$ é o vetor *velocidade* da curva em $t_0$
- $c''(t_0)$ é o vetor *aceleração* da curva nesse ponto.
- A **velocidade escalar** da curva em $t_0$ é dada por $\Vert c'(t_0)\Vert=v_e(t_0)$

### Reta tangente
- Um ponto é *regular* se $c'(t_0)\neq0$. Caso contrário, este é um ponto *singular*.
- Uma curva é **regular** se todos os seus pontos forem regulares.

- A reta tangente a uma curva $c$ num ponto $t_0$ é aquela definida pelo ponto $c(t_0)$ e pelo vetor $c'(t_0)$. Temos a equação vetorial:
$$X=c(t_0)+\lambda c(t_0),~~~~\lambda\in\mathbb R$$
### Derivadas de operações:
![[Pasted image 20220711171154.png]]
$(c\circ f)'(t)=c'(f(t))~f'(t)$

---
## Comprimento de arco
- O comprimento de curva entre os instantes $t=a$ e $t=b$ é dado por $$\int_a^b\Vert\alpha'(t)\Vert$$
- Uma curva diz-se *parametrizada por comprimento de arco* se para todo o $t\in I$ se tem que $v_e(t)=1$
- Para qualquer curva parametrizada por comprimento de arco, temos $c''(t)\cdot c'(t)=0$

- Se uma curva for a reparametrização de outra, elas terão o mesmo traço.

- Seja $\beta:[c,d]\to\mathbb R^n$ uma reparametrização da curva $\alpha:[a,b]\to\mathbb R^n$; o comprimento de $\beta$ de $c$ a $d$ é igual ao comprimento de $\alpha$ de $a$ a $b$
> Uma reparametrização de uma curva regular também será regular

- Uma curva possui reparametrização por comprimento de arco se e só se ela for regular. 
- Para uma curva reparametrizada por comprimento de arco tem-se sempre que $||\alpha'(t)||=1$ 
- Seja $\gamma:I\to\mathbb R^n$ uma curva suave regular e $\alpha_1:J_1\to\mathbb R^n$ uma reparametrização de gamma por comp de arco. A curva $\alpha_2:J_2\to\mathbb R^n$ é também reparametrização de gamma por comp de arco se e só se $\alpha_1=\alpha_2\circ\lambda$ sendo $\lambda:J_1\to J_2$ uma aplicação definida por $\lambda(t)=\pm t+c$ para alguma constante c. 

### TNB
- **Vetor tangente unitário** à curva regular $c:I\to\mathbb R^n$ é dado por $$T=\frac{c'(t)}{||c'(t)||}$$

### Aceleração
- A partir do que sabemosd de mecânica, temos que $\vec a=a_n\hat e_n+a_t\hat e_t$. Assim, o vetor aceleração de uma curva $\alpha$ é dado por:
$$\alpha''(t)=v_e'(t)T_\alpha(t)+v_e(t)T'_\alpha(t)$$

- ==Notação==: Aceleração tangencial da curva $\alpha$ em $t$: $a_{T,\alpha}(t)=v_e'(t)T_\alpha(t)$
- ==Notação==: Aceleração normal da curva $\alpha$ em $t$: $a_{N,\alpha}(t)=v_e(t)T'_\alpha(t)$

- Tem-se ainda:
$\alpha''(t)=a_{T,\alpha}(t)+a_{N,\alpha}(t)$
$a_{N,\alpha}(t)=\alpha''(t)-a_{T,\alpha}(t)$
$\large a_{N,\alpha}(t)=\frac{\alpha''(t)\cdot\alpha'(t)}{||\alpha'(t)||^2}\alpha'(t)$

> Para uma curva parametrizada com comprimento de arco, não há aceleração tangencial.

### Curvatura, kappa
$$\kappa(t)=\frac{||T'(t)||}{v(t)}=\frac{||a_N(t)||}{v^2(t)}=\frac{||\alpha'(t)\times\alpha''(t)||}{||\alpha'(t)||^3}$$
- Não depende da reparametrização, só do traço.
- O **raio da curvatura** é dado por $1/\kappa$
- Este é o raio da circunferência a que se melhor aproxima o traço da curva em $t$, a **circunferência osculadora**

- Se $\kappa(t)=0,\forall t$; então a  curva é uma reta.
- Se $\kappa(t)\neq0$, mas for constante, então a curva é uma circunferência.

> 2 vetores unitários tangentes são ortogonais.

### Vetor unitário normal
$$N(t)=\frac{T'(t)}{||T'(t)||}=\frac{a_N(t)}{||a_N(t)||}$$
- **Plano osculador** - plano que contém a circunferência osculadora. O seu vetor normal é $N$

### Vetor unitário binormal
$$B(t)=T(t)\times N(t)$$

### Parametros e parametrização
- $\kappa$ e $N$ não dependem da parametrização da curva, só do traço.
- Se houver reparametrização por $\lambda$, $T$ e $B$ ou se mantêm inalterados ou trocam de sinal, conforme $\lambda'$ tiver valores positivos ou negativos.

### Torção, tau
$$\tau(t)=\frac{N'(t)\cdot B(t)}{v(t)}=\frac{(\alpha'(t)\times\alpha''(t))\cdot\alpha'''(t)}{||\alpha'(t)\times\alpha''(t)||^2}$$
- Basicamente, representa o quanto a curva se "afasta" do plano inicial
- Se $\tau=0$ a curva é plana
- 

## Triedo de Frenet
Para uma curva reparametrizada por comprimento de arco:
$$T(s)=\beta'(s),~~~~N(s)=\frac{\beta''(s)}{||\beta''(s)||},~~~~B(s)=\beta'(s)\times\frac{\beta''(s)}{\kappa(s)}$$

- As 3 fórmulas de frenet permitem representar vetores $T',N',B'$ (derivadas) na base de frenet $b_F=(T(t), N(t), B(t))$:
$$T'(t)=v(t)\kappa(t)N(t)$$
$$N'(t)=-v(t)\kappa(t)T(t)+v(t)\tau(t)B(t)$$
$$B'(t)=-v(t)\tau(t)N(t)$$
>![[Pasted image 20220712174214.png]]

- Se tivermos as derivadas de TNB de uma curva reparametrizada por com arco:
>![[Pasted image 20220712174308.png]](porque temos sempre $\alpha'=1=v$)

## Equações de t e k
- Sejam $\kappa, \tau:I\to\mathbb R$ duas funções contínuas com $\kappa>0$. Assim, existe uma curva $\gamma:I\to\mathbb R^3$ parametrizada por comprimento de arco tal que $\kappa(s),\tau(s)$ são a curvatura e torção de gamma em cada $s$. O traço dessa curva é **único**.

#### Extensão para Rn
- O que temos até agora é apenas para R3. Para Rn teríamos n vetores $e_1,e_2,...,e_n$ que formariam um *referencial de Frenet*
![[Pasted image 20220712175833.png]]

---
## Coordenadas Polares
- Seja $P(x,y)$ um ponto no plano R2  À distância $r$ e ângulo $\theta$. As suas coordenadas polares são $P(r,\theta)$
---

#anal2 #resumo #matematica 