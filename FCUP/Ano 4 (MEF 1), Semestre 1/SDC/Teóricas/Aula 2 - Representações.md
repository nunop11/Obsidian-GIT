# Representações de Sistemas Dinâmicos
![[sdc_3|1000]]
- Um sistema Dinâmico é deste tipo, sendo que temos a caraterística especial que $Y$ depende da entrada $U$ e do **tempo** $t$:
$$Y(t)=f(U(t),t)$$

- Vejamos como podemos então representar e estudar sistemas deste tipo

## 1 - ODE
- Só isso, uma ODE de $y$ e $u$
- Consideremos um exemplo, para o qual voltaremos ao longo desta aula:
$$\ddot{y}(t)+5\dot{y}(t)+6y(t)=4u(t)~~~~;~~ y(t=0)=y_{0}$$
evidentemente, se soubermos a entrada $u(t)$ num intervalo $[0,T]$ então podemos determinar (nem que numericamente) a saída nesse intervalo.
- Precisamos ainda de saber a condição inicial de $y$: $y_{0}$

## 2 - TF / Laplace
(TF = Transfer Function)
- Geralmente assumimos que a condição inicial é $y_{0}=0$
- Assim, fazemos transformada de Laplace:
$$s^{2}Y+5sY+6Y=4U$$
em que podemos obter a função transferência:
$$\frac{Y}{U}=\frac{4}{s^{2}+5s+6}=\frac{4}{(s+2)(s+3)}$$

## 3 - Espaço de Estados (SS)
(SS = Space State)
- Transformamos a equação diferencial num sistema de 2 equações direrenciais de 1ª ordem. Isto vem ao custo de introduzir uma nova variável: $x$.
- Ora, esta variável $x$ é escolhida para simplificar a EDO e os cálculos necessários, pelo que pode não ter significado físico.
- Assim, temos:
$$\begin{cases}
\dot{x}=Ax+Bu \\
y=Cx+Du
\end{cases}$$

- Vejamos como fica o nosso exemplo:
    - Fazemos a escolha de variável: $x=\begin{pmatrix}x_{1} \\ x_{2}\end{pmatrix}$ em que $\begin{cases}x_{1}=y\\x_{2}=\dot{y}\end{cases}$
    - Podemos escrever a derivada: $\dot{x}=\begin{pmatrix}\dot{x}_{1}\\ \dot{x}_{2}\end{pmatrix}$
    - Mas podemos ver que $\dot{x}_{1}=\dot{y}=x_{2}$
    - Além disso, podemos usar a equação diferencial para ver que $\dot{x}_{2}=\ddot{y}=-5\dot{y}-6y+4u=-6x_{1}-5x_{2}+4u$
    - Podemos então escrever isto como uma equação de matrizes: $$\dot{x}=\begin{pmatrix}0 & 1 \\ -6 & -5\end{pmatrix}x+\begin{pmatrix}0 \\ 4\end{pmatrix}u$$
    - E como temos $x_{1}=y$ é evidente que a segunda equação fica $y=\begin{pmatrix}1 & 0\end{pmatrix}x+0u$
    - Assim: $$A=\begin{pmatrix}0 & 1 \\ -6 & -5\end{pmatrix}~~;~~B=\begin{pmatrix}0 \\ 4\end{pmatrix}~~;~~C=\begin{pmatrix}1 & 0\end{pmatrix}~~;~~D=0$$
    - Esta dedução é igualmente aplicável para TF invés de EDO

- Assim, nesta representação precisamos de conhecer $A,B,C,D$ e $x_{0}$ para prever o sistema.

**MIMO**
- Vejamos agora um caso mais genérico.
- Consideremos um MIMO com $m$ inputs e $p$ outputs. Teremos: $$u(t)\in\mathbb{R}^{m}\quad;\quad y(t)\in\mathbb{R}^{p}\quad;\quad x(t)\in\mathbb{R}^{n}$$
em que, conforme dito na aula anterior, é costume ter $n\ge p$

## 4 - Passagem SS $\to$ TF
- Se fizermos TF da equação 1 do sistema:
$$\begin{align*}
\dot{x}&= Ax+Bu\\
&\downarrow\\
sX&= AX+BU\\
(sI-A)X&= BU\\
X&= (sI-A)^{-1}BU
\end{align*}$$
e podemos substituir na equação 2:
$$\begin{align*}
Y &= Cx+Du\\
Y &= C(sI-A)^{-1}BU + DU\\
\frac{Y}{U}&= C(sI-A)^{-1}B + D
\end{align*}$$
e temos então a função de transferência, *obtida a partir do espaço de estados*!
- Podemos ter várias representações válidas no SS (conforme a escolha de $x_{1},x_{2}$). Mas todas as representações têm que dar a mesma TF.

## 5 - Formas da FT
- Ver resumo da próxima aula - na secção das notas da TP.

## 6 - Mudança de coordenadas
- Como sabemos, um vetor no espaço 2D é sempre o mesmo, independentemente da base em que o representamos.
- Temos então um vetor $\mathbf{x}$. Vamos representar na base $\boldsymbol{f}$  : $\begin{pmatrix}f_{1} & f_{2}\end{pmatrix}$ e na base $\boldsymbol{e}:\begin{pmatrix}e_{1} & e_{2}\end{pmatrix}$
- Podemos então definis a matriz de mudança de base:
$$\begin{pmatrix}e_{1} & e_{2}\end{pmatrix}=T \begin{pmatrix}f_{1} & f_{2}\end{pmatrix}$$
- A representação do vetor em cada base é $$\begin{align*}
\mathbf{x}&= x_{1}^{e} e_{1} + x_{2}^{e} e_{2}=\begin{pmatrix}e_{1} & e_{2}\end{pmatrix}\begin{pmatrix}x_{1}^{e}\\ x_{2}^{e} \end{pmatrix}\\\\
\mathbf{x}&= x_{1}^{f} f_{1} + x_{2}^{f} f_{2}=\begin{pmatrix}f_{1} & f_{2}\end{pmatrix}\begin{pmatrix}x_{1}^{f}\\ x_{2}^{f} \end{pmatrix}\\
\end{align*}$$
- Ora, como dissemos no início, estas 2 representações têm que ser equivalentes:
$$\begin{pmatrix}x_{1}^{f}\\ x_{2}^{f}\end{pmatrix}=\underbrace{\begin{pmatrix}f_{1} & f_{2}\end{pmatrix}^{-1}\begin{pmatrix}e_{1} & e_{2}\end{pmatrix}}_{T} \begin{pmatrix}x_{1}^{e}\\ x_{2}^{e}\end{pmatrix}$$

**Mudança de base SS**
- Temos:
$$\begin{cases}
\dot{x}=Ax+Bu \\
y=Cx+ Du
\end{cases}$$
- A mudança de variável consiste em $x=T\tilde{x}$ e temos:
$$\begin{align*}
\dot{x}&= Ax+Bu\\
&\downarrow\\
T \dot{\tilde{x}}&= AT \tilde{x} + Bu\\
\dot{\tilde{x}}&= T^{-1}AT \tilde{x}+T^{-1}Bu
\end{align*}$$
analogamente:
$$\begin{align*}
y&= Cx+Du\\
&\downarrow\\
y&= CT \tilde{x} + D
\end{align*}$$
- E assim podemos escrever:
$$\begin{cases}
\dot{\tilde{x}}=\tilde{A}\tilde{ x}+\tilde{B}u \\
y=\tilde{C}\tilde{x}+\tilde{D}u
\end{cases} \quad \quad;\quad \boxed{\begin{align*}
\tilde{A}&= T^{-1}AT\\
\tilde{B}&= T^{-1}B\\
\tilde{C}&= CT\\
\tilde{D}&= D
\end{align*}}$$

# Notas da  TP
- Temos nas equações acima $(sI-A)^{-1}$. Para uma matriz 2x2, podemos calcular a inversa da forma:
$$M = \begin{pmatrix}a & b \\ c & d\end{pmatrix} \quad;\quad M^{-1} = \frac{1}{\det(M)}\begin{pmatrix}d & -b \\ -c & a\end{pmatrix}=\frac{1}{ab-cd}\begin{pmatrix}d & -b \\ -c & a\end{pmatrix}$$

- Notemos ainda que aqui ficaremos sempre com algo deste género (abaixo temos o mesmo exemplo que temos usado até agora):
$$sI-A=\begin{pmatrix}s & -1 \\ 6 & s+5\end{pmatrix}~~~~\to~~~~ (sI-A)^{-1}=\frac{1}{(s+2)(s+3)}\begin{pmatrix}s+5 & 1  \\ -6 & s\end{pmatrix}$$
- Neste exemplo a função transferência fica:
$$\frac{Y}{U}=\begin{pmatrix}1 & 0\end{pmatrix}\cdot \frac{1}{(s+2)(s+3)}\begin{pmatrix}s+5 & 1  \\ -6 & s\end{pmatrix} \cdot \begin{pmatrix}1 \\ 0\end{pmatrix}=\frac{1}{(s+2)(s+3)}$$
e podemos expandir em fraços parciais:
$$\frac{Y}{U}=\frac{1}{s+2} - \frac{1}{s+3}$$
(No resumo da próxima aula (e respetiva TP) teremos mais informação sobre isto)