- Na prática, muitas vezes só conseguimos estudar um sistema a partir de um certo intstante. Ora, não conseguimos determinar o passado do sistema. Felizmente, apenas precisamos de o conhecer no instante em que começamos a estudá-lo: **condições iniciais**

# Problemas de Condição Inicial - 1ª Ordem
- Recordemos que um SLIT de 1ª ordem é descrito por uma equação diferencial do tipo: $$\alpha_{1} \frac{dy}{dt} + \alpha_{0}y=\beta_{1} \frac{dx}{dt} + \beta_{0}x$$
- Consideramos que se conhece:
    - $x(t)~~;~~t>0$
    - $y(0)$
- E pretendemos determinar $y(t)~~;~~t>0$

## Abordagem habitual
1. Determinar a solução homogénea da Eq Dif ($\alpha_{1} \frac{dy_{h}}{dt} + \alpha_{0}y_{h}=0$)
2. Determinar a solução particular não homogénea. Normalmente isto significa substituir $x(t)=\text{Re}[x_{0}e^{i\omega_{0}t}]~~;~~y(t)=\text{Re}[Ye^{i\omega_{0}t}]$
3. Somar as 2 e obter a solução geral.

### Problemas
- Para sistemas de ordem superior pode ser complicado.
- A solução particular pode ser, também, complicado, sendo que muitas vezes dependemos de ter sinais harmónicos.

## Abordagem com Laplace
- Temos:
$$\begin{align*}
\alpha_{1} \frac{dy}{dt} + \alpha_{0}y&= \beta_{1} \frac{dx}{dt} + \beta_{0}x\\
x(t)=0~,~t>0 \quad \quad&;\quad \quad y(0)=y_{0}~,~y_{0}\in\Re
\end{align*}$$
ora, $x(t)$ é então um *sinal direito*.
- Podemos aplicar a transformada de Laplace aos 2 lados:
$$\begin{align*}
\alpha_{1} \frac{dy}{dt} + \alpha_{0}y&= \beta_{1} \frac{dx}{dt} + \beta_{0}x\\
\alpha_{1}[sY-y(0)]+\alpha_{0}Y&= \beta[sX-x(0)]+\beta_{0}X\\
Y= \frac{\beta_{1}s+\beta_{0}}{\alpha_{1}s+\alpha_{0}}X &+ \frac{1}{\alpha_{1}s+\alpha_{0}}[\alpha_{1}y(0)-\beta_{1}x(0)]\\
Y=HX &+ \frac{1}{\alpha_{1}s+\alpha_{0}}[\alpha_{1}y(0)-\beta_{1}x(0)]
\end{align*}$$
- Voltamos a ver o que já obtivemos em exemplos da aula anterior: o sinal de saída tem 2 partes, uma influenciada pelas condições inicias, outra pelo sinal de entrada e sistema. Ou seja:
$$Y_{sinal}(s)=H(s)X(s)\quad;\quad Y_{inicial}(s)=\frac{1}{\alpha_{1}s+\alpha_{0}}[\alpha_{1}y(0)-\beta_{1}x(0)]$$
Esquematicamente:
![[cond inicial.png]]

## Estado inicial
- Acabamos de ver o que são os *valores inciais* - $x(0),y(0),\dots$
- Temos ainda o **Estado Inicial**. Este resume-se ao valor dos estados internos no instante $t=0$. Tendo em conta que eles se relacionam aos armazendores de energia do sistema, o estado inicial pode ser interpretado como sendo o nível de armazenamento de energia dos elementos internos em $t=0$
- Vejamos um exemplo:
![[cond inicial diagrama.png]]
- Usando a *Forma Direta II* temos:
$$\begin{align*}
y(t)&= [x(t)-\alpha_{0}z(t)] \frac{1}{\alpha_{1}}\beta_{1} + \beta_{0}z(t)\\
(t&= 0)\\
y(0)&= [x(0)-\alpha_{0}z(0)] \frac{1}{\alpha_{1}}\beta_{1} + \beta_{0}z(0)\\
\alpha_{1}y(0)-\beta_{1}x(0)&= [\alpha_{1}\beta_{0}-\alpha_{0}\beta_{1}]z(0)
\end{align*}$$
- Assim, juntando isto ao que obtivemos anteriormente: $Y_{inicial}(s)=\frac{1}{\alpha_{1}s+\alpha_{0}}[\alpha_{1}y(0)-\beta_{1}x(0)]$ temos:
$$Y_{inicial}(s)=G(s)Zz(0) \quad;\quad G(s)=\frac{\alpha_{1}\beta_{0}-\alpha_{0}\beta_{1}}{\alpha_{1}s+\alpha_{0}}$$
- Assim podemos escrever:
$$\boxed{Y(s)=H(s)X(s)+G(s)z(0)}$$
> __*EXEMPLO 1 - CIRCUITO RC*__
> Consideremos um circuito RC assim:
> ![[circuito RC exemplo.png]]
> (mas sem conhecer $R,C$)
> - Nos terminais de um condensador temos: $$Q=C\Delta V \to i_{C}=\frac{dQ}{dt}=C \frac{d}{dt}\Delta V=C \left[ \frac{dV_{in}}{dt}- \frac{dV_{out}}{dt} \right]$$
> - Por outro lado temos $$i_{R}(t)=\frac{V_{out}(t)}{R}$$
> - Ora, necessariamente temos $i_{C}=i_{R}$, logo:
> $$V_{out}(t)=\tau \left[ \frac{dV_{in}(t)}{dt}- \frac{dV_{out}(t)}{dt} \right]~~~~;~~~~\tau=RC$$
> Fazendo a transformada de Laplace Unilateral: 
> $$\begin{align*}
V_{out}(s)&= \tau[sV_{in}(t)-V_{in}(0) -sV_{out}(t)+V_{out}(0) ]\\
V_{out}(s)&= \frac{s\tau}{s\tau+1}V_{in}(s)- \frac{\tau}{s\tau+1}[V_{in}(0)-V_{out}(0)]
\end{align*}$$
> De onde facilmente vemos que $$H(s)=\frac{s\tau}{s\tau+1} \quad;\quad G(s)=\frac{-\tau}{s\tau+1} \quad;\quad z(0)=\Delta V_{C}(0)$$
- Neste exemplo acima torna-se ainda evidente a diferença entre valor e estado inicial, de tal modo que o estado inicial que determinamos é a diferença entre os valores iniciais.

### Repouso
- Se num certo sistema tivermos $z(0)=0$, então diz-se que o *sistema está em repouso* até $t=0$.

## Unilateral VS Bilateral
- A resposta de um sistema a um sinal bilateral $[-\infty,+\infty]$ será igual à resposta a um sinal unilateral $[0,+\infty]$ *menos os termos transitórios*.

## Partes da Solução
Num exercício das TP obtem-se:
$$y(t)= \frac{2x_{0}}{4+ (\omega_{0}t)^{2}}e^{\frac{-2t}{\tau}}+ |H(j\omega_0)|x_{0}\cos[\omega_{0}t+\Theta(\omega_{0})] + (y_{0}-x_{0})e^{\frac{-2t}{\tau}}$$
em que:
![[partes y com cond inicial.png]]

# Problemas de Condição Inicial - 2ª Ordem
Definidos por equações do tipo:
$$\begin{align*} \alpha_2\frac{d^2y}{dt^2}(t) + \alpha_1\frac{dy}{dt}(t) + \alpha_0y(t) = \beta_2\frac{d^2x}{dt^2}(t) + \beta_1\frac{dx}{dt}(t) + \beta_0x(t) \end{align*}$$
- Conhecendo $y(0), \frac{dy}{dt}(0),x(0), \frac{dx}{dt}(0)$, temos:
$$\begin{align*}
L_{U} \left[ \frac{dy}{dt}(t) \right] &= sY(s)-y(0)\\
L_{U} \left[ \frac{dx}{dt}(t) \right] &= sX(s)-x(0)\\
L_{U} \left[ \frac{d^{2}y}{dt^{2}}(t) \right] &= s^{2}Y(s)- \left[ sy(0) + \frac{dy}{dt}(0) \right]\\
L_{U} \left[ \frac{d^{2}x}{dt^{2}}(t) \right] &= s^{2}X(s)- \left[ sx(0) + \frac{dx}{dt}(0) \right]
\end{align*}$$
ao fazer a transformada de Laplace dos 2 lados da equação diferencial obtemmos:
$$\begin{align*} Y(s) &= \frac{\beta_2s^2 + \beta_1s + \beta_0}{\alpha_2s^2 + \alpha_1s + \alpha_0}X(s) + \frac{[\alpha_2s + \alpha_1]y(0) + \alpha_{2} \frac{dy}{dt}(0) - [\beta_2s + \beta_1]x(0) - \beta_{2} \frac{dx}{dt}(0)}{\alpha_2s^2 + \alpha_1s + \alpha_0} = \\ \\
&= H(s)X(s) + \frac{s[\alpha_2y(0) - \beta_2x(0)] + \alpha_{2} \frac{dy}{dt}(0) - \beta_{2} \frac{dx}{dt}(0) +\alpha_1y(0) - \beta_1x(0)}{\alpha_2s^2 + \alpha_1s + \alpha_0} \end{align*}$$
- Podemos representar sistemas de 2ª ordem como um diagrama de blocos com ***Forma Direta III***:
![[cond inicial diagrama 2a ordem.png]]
de onde obtemos as equações:
$$y(t)=\frac{1}{\alpha_{2}} z_{1}(t) + \frac{\beta_{2}}{\alpha_{2}}x(t) \quad \quad;\quad \quad \frac{dz_{1}}{dt} = z_{2}(t)+\beta_{1}x(t) -\alpha_{1} y(t)$$
Podemos derivar a primeira equação, isolar $\frac{dz_{1}}{dt}$ e substituir na segunda equação: $$\frac{dy}{dt} = z_{2} + \frac{\beta_{2}}{\alpha_{2}} \frac{dx}{dt} + \frac{1}{\alpha_{2}} z_{2} - \frac{\alpha_{1}}{\alpha_{2}}y(t)$$
e então obtemos: 
$$\begin{align*}
z_{1}(0)&= \alpha_{2}y(0) - \beta_{2}x(0)\\
z_{2}(0)&= \alpha_{1}y(0) + \alpha_{2} \frac{dy}{dt}(0) - \beta_{1}x(0) - \beta_{2} \frac{dx}{dt}(0)
\end{align*}$$
- E podemos reescrever a equação de $Y(s)$ acima como:
$$Y(s)=H(s)X(s) + \frac{sz_{1}(0)+z_{2}(0)}{\alpha_{2}s^{2}+\alpha_{1}s+\alpha_{0}}$$

# Problemas de Condição Inicial - Ordem Superior
Estes sistemas são descritos por equações diferenciais do tipo:
$$\sum_{n=0}^N \alpha_n\frac{d^n y(t)}{dt^n} = \sum_{n=0}^N \beta_n\frac{d^nx(t)}{dt^n}$$
- Aqui, se usassemos os métodos que vimos para ordem 1 e 2 ficaremos com expressões muito extensas e complicadas. Assim, usamos o *Espaço de Estados*.
- Como isto é um problema de valores iniciais então conhecemos: $y(0), \frac{dy}{dt}(0), \frac{d^{2}y}{dt^{2}}(0),\cdots, \frac{d^{n}t}{dt^{n}}(0)$ (e para $x$ também).

- Sabemos que, no espaço de estados temos:
$$\frac{d\mathbf{z}}{dt}=A \mathbf{z}+Bx(t) \quad;\quad y(t)=C \mathbf{z} +Dx(t)$$
em que:
    - $x,y,D$ são escalares
    - $\mathbf{z}$ é um vetor com $N$ entradas
    - $A$ é matriz $N \times N$
    - $B$ é matriz $N \times 1$
    - $C$ é matriz $1 \times N$

Se fizermos as transformadas de Laplace temos:
$$\begin{align*}
L\left[ \frac{d\mathbf{z}}{dt}\right]&= L[A \mathbf{z}+Bx] \\
s \mathbf{Z}- \mathbf{z}(0)&= A \mathbf{Z}+BX\\
\mathbf{Z}(sI-A)&= BX + \mathbf{z}(0)\\
\mathbf{Z} &= (sI-A)^{-1}BX + (sI-A)^{-1}\mathbf{z}(0)\\
&\downarrow\\
L(y)&= L[C \mathbf{z}+Dx]\\
Y&= C \mathbf{Z}+DX\\
&\textsf{(Substiruir $\mathbf{Z}$ acima)}\\
Y&= [(sI-A)^{-1}B+D]X + C(sI-A)^{-1}\mathbf{z}(0)\\
Y(s) &= H(s)X(s) + G(s)\mathbf{z}(0)
\end{align*}$$
e temos, protanto, $$H(s)=(sI-A)^{-1}B+D \quad \quad;\quad \quad G(s)=C(sI-A)^{-1}$$em forma de esquema temos:
![[cond inicial esquema v2.png]]
- De notar que podemos usar isto para sistemas de 1ª e 2ª ordem. Basta definir as equações diferencias e obter as matrizes.

# Z a partir de entrada e saída
- Para um certo problemas temos as seguintes funções e respetivas condições iniciais (para $x$ e $y$):
$$\begin{align*} \textbf x(t) = \begin{bmatrix} x(t) \\ \frac{dx}{dt}(t) \\ \frac{d^2x}{dt^2}(t) \\ \vdots \\ \frac{d^nx}{dt^n}(t) \end{bmatrix} \quad\quad\quad\quad \textbf y(t) = \begin{bmatrix} y(t) \\ \frac{dy}{dt}(t) \\ \frac{d^2y}{dt^2}(t) \\ \vdots \\ \frac{d^ny}{dt^n}(t) \end{bmatrix} \end{align*}$$
Assim, recordando que $\frac{d\mathbf{z}}{dt}=A \mathbf{z}+Bx(t)$ temos:
$$\begin{align*}
y(t)&= C \mathbf{z}(t)+Dx(t)\\
\frac{dy}{dt}(t)&= C \left[ \frac{d\mathbf{z}}{dt}=A \mathbf{z}+Bx(t) \right] + D \frac{dx}{dt}\\
&= CA \mathbf{z}(t)+CB \mathbf{x(t)} + D \frac{dx}{dt}\\
\frac{d^{2}y}{dt^{2}}(t)&=  C\left[A\left[A\textbf z(t) + Bx(t)\right] + B\frac{dx}{dt}\right] + D\frac{d^2x}{dt^2} \\
&= CA^{2}\mathbf{z}(t) + CAB x(t) + CB \frac{dx}{dt} + D \frac{d^{2}x}{dt^{2}}
\end{align*}$$
- Vemos então os padrões:
    - Ficamos sempre com um termo com $\mathbf{z}(t)$
    - Na derivada $n$ temos termos com derivadas de $x$ até ordem $n$, o que é causado pelo termo $\mathbf{z}(t)$

Assim podemos escrever:
$$\mathbf{z}(0)=W^{-1}[y(0)-Vx(0)]$$
sendo 
$$\begin{align*} W = \begin{bmatrix} C \\ CA \\ CA^2 \\[0.2cm] \vdots \\ CA^{N-1} \end{bmatrix} \quad\quad V = \begin{bmatrix} D & 0 & 0 & \cdots & 0 \\ CB & D & 0 & \cdots & 0 \\[0.2cm] CAB & CB & D & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ CA^{N-2}B & CA^{N-3}B & CA^{N-4}B & \cdots & D \end{bmatrix} \end{align*}$$

#sinais #fisica
