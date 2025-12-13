******- Como sabemos, podemos definir um SLIT no espaço de estados na forma
$$\begin{cases}
x(t+1)=Ax(t)+Bu(t) \\
y(t)=Cx(t)+Du(t)
\end{cases}$$
em que temos:
    - $y\in \mathbb{R}^{\ell}$ - saída do sistema
    - $u\in \mathbb{R}^{m}$ - entrada do sistema
    - $x\in\mathbb{R}^{n}$ - vetor de variáveis de estado do sistema
    - $A\in\mathbb{R}^{n\times n},B\in\mathbb{R}^{n\times m},C\in\mathbb{R}^{\ell\times n},D\in\mathbb{R}^{\ell\times m}$
- Ora, para poder estudar e *prever* o comportamento do sistema queremos saber $A,B,C,D$. 
- Mas para isso, apenas conseguimos medir a entrada $u$ e a saída do sistema $y$. Assim, surge o principal **problema** que queremos resolver:
    - Como estimar $x(t)$ sabendo $y(t)$???
- Notemos que em sistemas físicos muitas vezes podemos medir as variáveis de estado com sensores (a velocidade de um objeto pode ser uma variável destas), mas vamos estudar os casos em que não temos essa ajuda.

# Observadores determinísticos
- Observadores são modelos do sistema que estima $x$ a partir de $u,y$
- Como dito acima, este tipo de modelos permite entender e compreender o sistema linear em estudo. Mas, *na prática* isso permite:
    - estabilizar sistemas através de realimentação
    - monitorizar e prever sistemas
    - detetar avarias
    - criar sensores software, que substituem sensores reais caros

## Abordagem 1 - mesmo modelo
- Nesta abordagem consideramos um observador com o **mesmo modelo** que o sistema que ele está a observar:
$$\begin{cases}
\hat{x}(t+1)=A \hat{x}(t)+Bu(t) \\
\hat{y}(t)=C \hat{x}(t)+Du(t)
\end{cases}$$
e teremos um erro:
$$\tilde{x}(t)=x(t)-\hat{x}(t)$$
- Uma **nota sobre notação**:
    - $x$ (letra normal) é um sinal teórico/desconhecido
    - $\hat{x}$ (letra com chapéu) é a estimativa que é feita de $x$
    - $\tilde{x}$ (letra com til) é o erro da estimação: $\tilde{x}=x-\hat{x}$
- Podemos expandir o erro:
$$\begin{align*}
\tilde{x}(t+1)&= x(t+1)-\hat{x}(t+1)\\
&= Ax(t)+\cancel{Bu(t)}-A \hat{x}(t)-\cancel{Bu(t)}\\
&= A[x(t)-\hat{x}(t)]\\
&= A \tilde{x}(t)
\end{align*}$$
- Assim, o erro evolui de forma *igual ao sistema*. Isto implica que:
    - O erro **só se anula** se o sistema for **estável**
    - *Não* conseguimos observar sistemas instáveis
    - Não podemos controlar a dinâmica do erro de forma nenhuma, ela será sempre igual ao sistema

### EX
- No PPT o professor faz um exemplo em que temos um sistema que representa um motor:
$$\begin{cases}
x_{1}(t+1)=x_{1}(t)+x_{2}(t) \\
x_{2}(t+1)=0.9x_{2}(t)+10u(t) \\
y(t)=x_{1}(t)
\end{cases}$$
em que $x_{1}$ é a posição angular do motor e $x_{2}$ a sua velocidade.
- Podemos facilmente ver que
$$A=\begin{pmatrix}1 & 1 \\ 0 & 0.9\end{pmatrix}~~~~\to~~~~ \lambda_{A1}=1~~,~~\lambda_{A2}=0.9$$
logo temos um sistema instável - o erro nunca se vai anular.
- Ao simular o sistema obtem-se:
![[estimador mesmo modelo.png]]
A estimativa inicial começa errada e o sistema nunca consegue "apanhar" o sistema real. Mais concretamente, o erro da velocidade ($x_{2}$) eventualmente é anulado, mas o da posição ($x_{1}$) nunca o é, ficando-se com o traçado estimado paralelo ao real.

## Abordagem 2 - Luenberger
- Este é o modelo que demos em SDC:
$$\begin{cases}
\hat{x}(t+1) = A \hat{x}(t)+Bu(t) + L [y(t) - C \hat{x}(t) - Du(t)] \\
\hat{y}(t) = C \hat{x}(t) + Du(t)
\end{cases}$$
ou seja, estamos a fazer *realimentação* - à dinâmica do sistema real ($A\hat{x}+Bu$) acrescentamos um novo termo. Este consiste no erro da saída estimada com $\hat{x}(t)$ relativamente à saída $y(t)$ *que conseguimos medir*. Isto permite aplicar correções na hora.
- Temos ainda um ganho $L$ que conseguimos controlar.
- Podemos expandir o erro:
$$\begin{align*}
\tilde{x}(t)&= x(t)-\hat{x}(t)\\
&= Ax(t)+\cancel{Bu(t)}-A\hat{x}(t)-\cancel{Bu(t)}-L[y(t)-C\hat{x}(t)-Du(t)]\\
&= A[x(t)-\hat{x}(t)] - L[Cx(t)+\cancel{Du(t)}-C\hat{x}(t)-\cancel{Du(t)}]\\
&= (A-LC)\tilde{x}(t)
\end{align*}$$
- Agora temos:
    - Sistema linear "simples"
    - Podemos controlar a dinâmica através de $L$, forçando até estabilidade do observador
    - Isto quer dizer que conseguimos *observar sistemas instáveis*, desde que $A,C$ sejam **observáveis**

### EX
- Vejamos como podemos controlar a dinâmica do sistema. Temos:
$$A-LC=\begin{pmatrix}1 & 1  \\ 0 & 0.9\end{pmatrix}-\begin{pmatrix}\ell_{1} \\ \ell_{2}\end{pmatrix}\begin{pmatrix}1 & 0\end{pmatrix}=\begin{pmatrix}1-\ell_{1} & 1 \\ -\ell_{2} & 0.9\end{pmatrix}$$
e temos o polinómio caraterístico:
$$\begin{align*}
A_{0}(\lambda)&= \det[\lambda I - (A-LC)]\\
&= \begin{vmatrix}\lambda-(1-\ell_{2}) & -1\\
\ell_{2} & \lambda-0.9\end{vmatrix}\\
&=\lambda^{2} - (1.9-\ell_{1})\lambda + (1-\ell_{1})0.9+\ell_{2}
\end{align*}$$
- Ora, consideremos que queremos colocar os valores próprios em $\lambda_{1},\lambda_{2}$. Teríamos então:
$$\begin{align*}
A_{0}(\lambda)&= (\lambda-\lambda_{1})(\lambda-\lambda_{2})\\
&= \lambda^{2}-(\lambda_{1}+\lambda_{2})\lambda + \lambda_{1}\lambda_{2}
\end{align*}$$
- Assim, para controlar o observador com $L$ fazemos:
$$\begin{align*}
\lambda^{2}-(1.9-\ell_{1})\lambda + (1-\ell_{1})0.9+\ell_{2}&= \lambda^{2}-(\lambda_{1}+\lambda_{2})\lambda+\lambda_{1}\lambda_{2}\\
\end{align*}$$
logo
$$\begin{align*}
&\begin{cases}
1.9-\ell_{1}=\lambda_{1}+\lambda_{2}\\
(1-\ell_{1})0.9+\ell_{2}=\lambda_{1}\lambda_{2}
\end{cases}\\
&~~~~~~\downarrow\\
&\begin{cases}
\ell_{1}=1.9-(\lambda_{1}+\lambda_{2})\\
\ell_{2}=0.81-0.9(\lambda_{1}+\lambda_{2})+\lambda_{1}\lambda_{2}
\end{cases}
\end{align*}$$
- E assim podemos obter o vetor $L$ que coloca os valores próprios do observador em $\lambda_{1},\lambda_{2}$ - estes valores são escolhidos por nós.
- Consideremos alguns exemplos:
![[ganhos e lambdas luenberger - 4 observadores.png]]
- Todos estes 4 observadores foram simulados. Todos eles aparentam funcionar muito bem ao visualizar só $\hat{x}_{i}(t)$ vs $x(t)$. Assim, vejamos a evolução do erro de cada observador:
![[estimacao luenberger resultado.png]]
- NOTAS:
    - O observador 1 tem a resposta mais lenta. Isto acontece porque ele tem os valores próprios mais *perto de 1*
    - O observador 4 tem a resposta mais rápida. Ao estimar $x_{2}$, conseguiu anular o erro em **1 iteração**! Notemos que ele tem os 2 valores próprios na *origem*
    - Quanto mais rápido for o observador, maior será o seu erro por overshoot. Isto também implica que estes observadores rápidos são muito mais reativos e começam a oscilar facilmente

- Assim surge uma dúvida: **como escolher os valores próprios?**
    - Se forem muito altos teremos um observador demasiado lento
    - Se forem muito baixos teremos um observador demasiado sensível
    - Queremos então balancear o tradeoff entre velocidade e sensibilidade

