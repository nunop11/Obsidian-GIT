## 1 - Valores e vetores próprios
- Tendo uma matriz $A\in\mathbb{R}^{n\times n}$, será possível determinar *valores próprios* $\lambda_{i}$ ($i=1,\dots,N$) (assumindo que têm todos multiplicidade 1)
- Estes valores são definidos por:
$$\det(\lambda_{i}I_{n\times n}-A)=0$$
tal que existem vetores $v_{i}$ - os *vetores próprios* - em que
$$Av_{i}=\lambda_{i}v_{i}$$
em que $v_{i}$ é o vetor associado ao valor $\lambda_{i}$.

### Multiplicidade
- Um valor próprio $\lambda_{j}$ pode ter multiplicidade $m_{j}$ (encontrasse repetido): $\lambda_{j \ell}~,~\ell=1,\dots,m_{j}$
- Chamamos $m_{1}$ à multiplicidade do valor - *mutiplicidade algébrica*
- Este valor e os seus múltiplos (e respetivos vetores) geram um espaço de dimensão $m_{2}$ - *multiplicidade geométrica*, em que $m_{2}\le m_{1}$

### Matriz Diagonalizável
- Se uma matriz $A$ for diagonalizável, podemos escrever:
$$A=PDP^{-1} \quad;\quad D=\begin{pmatrix}\lambda_{1} & 0 & 0 \\ 0 & \lambda_{2} & 0 \\ 0 & 0 & \lambda_{3}\end{pmatrix} \quad;\quad P=\begin{pmatrix}\vdots & \vdots & \vdots \\ v_{1} & v_{2} & v_{3} \\ \vdots & \vdots & \vdots\end{pmatrix}$$
- Se tivermos algum valor próprio com multiplicidade acima de 1. Assim, teremos um **bloco de Jordan**:
$$A=PJP^{-1}\quad;\quad J=\begin{pmatrix}\lambda_{1} & 1 & 0 & 0 \\ 0 & \lambda_{1} & 1 & 0 \\ 0 & 0 & \lambda_{1} & 0 \\ 0 & 0 & 0 & \lambda_{2}\end{pmatrix} \quad;\quad P=\begin{pmatrix}\vdots & \vdots \\ v_{1} & v_{2} \\ \vdots & \vdots\end{pmatrix}$$
- Consideremos um exemplo:
$$A=\begin{pmatrix}1 & 1 & 12 \\ -1 & 0 & 0 \\ 0 & 0 & 1\end{pmatrix}~~~~\to~~~~ J=\begin{pmatrix}1 & \begin{matrix}0 & 0\end{matrix} \\ \begin{matrix}0 \\ 0\end{matrix} & \begin{bmatrix}2 & 1 \\ 0 & 2\end{bmatrix}\end{pmatrix}$$
aquilo salientado em baixo é o diagrama de Jordan.

## 2 - Sistema Fundamental
- O sistema fundamental de $\dot{x}(t)=A x(t)$ é um operador:
$$\Phi(t,\tau):\mathbb{R}\times \mathbb{R}\to\mathbb{R}^{n\times n}$$
tal que: $$\frac{d\Phi}{dt}=A \Phi \quad,\quad \Phi(\tau,\tau)=I$$
- Temos as propriedades:
    - $\forall t_{1},t_{2}$
        - $\det(\Phi(t_{1},t_{2}))\neq0$
        - $\Phi(t_{1},t_{2})=\Phi^{-1}(t_{2},t_{1})$
    - $\forall t_{1},t_{2},t_{3}$ 
        - $\Phi(t_{1},t_{2})=\Phi(t_{1},t_{2})\Phi(t_{2},t_{3})$
    - $\forall x_{0}\in \mathbb{R}^{n}$
        - $x(t)=\Phi(t,t_{0})x_{0}$ é a solução de $\dot{x}=Ax~,~t\ge t_{0},x(t_{0}=x_{0})$

- Consideremos o sistema descrito em SS por:
$$\dot{x}=Ax+Bu$$
podemos fazer a mudança de variável $\tilde{x}:x=\Phi(t,t_{0})\tilde{x}$ e temos:
$$\begin{align*}
\dot{x}&= \frac{d}{dt} \left[\Phi(t,t_{0})\tilde{x} \right]\\
&= \frac{d\Phi}{dt}\tilde{x} + \Phi(t,t_{0}) \dot{\tilde{x}}\\
&= A\underbrace{\Phi(t,t_{0})\tilde{x}}_{x} + \Phi(t,t_{0}) \dot{\tilde{x}}\\
\\
\dot{\tilde{x}}&= \Phi(t_{0},t)[\dot{x}-Ax]
\end{align*}$$
e temos: $\dot{x}=Ax+Bu$ logo $Bu=\dot{x}-Ax$. Assim:
$$\dot{\tilde{x}}=\Phi(t_{0},t)Bu$$
- Podemos integrar esta equação
$$\tilde{x}(t)=\tilde{x}(t_{0})+\int_{t_{0}}^{t}\Phi(t_{0},\tau)Bu(\tau)d\tau$$
e temos:
$$\begin{align*}
x(t)&= \Phi(t,t_{0})\tilde{x}(t)\\
&= \Phi(t,t_{0})x(t_{0}) + \int_{t_{0}}^{t}\Phi(t,\tau)Bu(\tau)d \tau
\end{align*}$$
em que o primeiro termo representa o *estado inicial* e o segundo termo representa *controlo*.

# Notas TP 
## Formas de representação
### Forma Canónica Controlável
- Uma EDO tem a forma:
$$y^{(n)}+a_{1}y^{(n-1)}+\dots+a_{n-1}y'+a_{n}y= b_{0}u^{(n)}+b_{1}u^{(n-1)}+\dots+b_{n}u$$
- Fazemos transformada de Laplace e ficamos com:
$$\frac{Y}{U}= \frac{b_{0}s^{n}+b_{1}s^{n-1}+\dots+b_{n-1}s+b_{n}}{s^{n}+a_{1}s^{n-1}+\dots+a_{n-1}s+a_{n}}$$
podemos colocar de fora o termo $b_{0}$ (isto é feito ao fazer divisão de polinómios):
$$\begin{align*}
\frac{Y}{U}&= b_{0}+\frac{(b_{1}-a_{1}b_{0})s^{n-1}+\dots+(b_{n}-a_{n}b_{0})}{s^{n}+a_{1}s^{n-1}+\dots+a_{n-1}s+a_{n}}\\\\
&= b_{0}+ \frac{\beta_{1}s^{n-1}+\dots+\beta_{n}}{s^{n}+a_{1}s^{n-1}+\dots+a_{n-1}s+a_{n}}
\end{align*}$$

- A forma controlável consiste em:
$$A_{C}=\begin{pmatrix}0 & 1 & 0 & 0 & \cdots & 0 \\ 0 & 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ -a_{n} & -a_{n-1} & -a_{n-2} & -a_{n-3} & \cdots & -a_{1}\end{pmatrix}$$
$$B_{C}=\begin{pmatrix}0 \\ 0 \\ 0 \\  \vdots  \\  1\end{pmatrix}~~;~~C_{C}=\begin{pmatrix}\beta_{n} \\ \beta_{n-1} \\ \beta_{n-2} \\ \vdots \\ \beta_{0}\end{pmatrix}^{T}~~;~~D_{C}=b_{0}$$

### Forma Canónica Observável
$$A_{O}=A_{C}^{T}~~,~~B_{O}=C_{C}^{T}~~,~~C_{O}=B_{O}^{T}~~,~~D_{O}=D_{C}$$

### Forma Canónica Diagonal
- Vejamos apenas o caso em que temos polos distintos (não há multiplicidade >1)
- Tal como acima, colocamos a função de transferência na forma:
$$\frac{Y}{U}=b_{0} +\frac{\sum\limits b_{i}}{\sum\limits a_{i}s^{i}}$$
e queremos *farotorizar o denominador*: $\sum a_{i}s^{i}=\prod(s+p_{i})$ em que $p_{i}$ são os **polos** (zeros) do denominador.
- Assim fica:
$$\frac{Y}{U}=b_{0}+ \sum\limits \frac{c_{i}}{s-p_{i}}$$

e assim, sabendo todos os $p_{i},c_{i}$ temos a forma canónica diagonal:
$$A_{C}=\begin{pmatrix}-p_{1} & 0 & 0 & 0 & \cdots & 0 \\ 0 & -p_{2} & 0 & 0 & \cdots & 0 \\ 0 & 0 & -p_{3} & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0& 0 & 0 & \cdots & -p_{n}\end{pmatrix}$$
$$B_{C}=\begin{pmatrix}1 \\ 1 \\ 1 \\  \vdots  \\  1\end{pmatrix}~~;~~C_{C}=\begin{pmatrix}c_{1} \\ c_{2} \\ c_{3} \\ \vdots \\ c_{n}\end{pmatrix}^{T}~~;~~D_{C}=b_{0}$$

#### EXEMPLO
- Temos a equação diferencial:
$$y'''+2y''-y'-2y=u'-2u$$
e podemos calcular a LT:
$$(s^{3}+2s^{2}-s-2)Y=(s-2)U$$
logo temos a TF:
$$\frac{Y}{U}=\frac{s-2}{s^{3}+2s^{2}-s-2}$$
como o numerador é polinómio de grau inferior ao denominador temos $b_{0}=0$. Ou seja, o que temos acima já está na forma $\frac{Y}{U}=b_{0}+\frac{\sum\limits}{\sum\limits}$. 
- Assim temos automaticamente a forma *controlável*:
$$A_{C}=\begin{pmatrix}0 & 1 & 0 \\ 0 & 0 & 1 \\ 2 & 1 & -2\end{pmatrix}~~,~~ B_{C}=\begin{pmatrix}0 \\ 0 \\ 1\end{pmatrix}~~,~~C_{C}=\begin{pmatrix}-2 & 1 & 0\end{pmatrix}~~,~~D_{C}=0$$
(podemos notar que em C e na linha de baixo de A temos os coeficientes do numerador e denominador (respetivamente) da direita para a esquerda conforme eles aparecem na fração)

- Daqui ter a forma *observável* é trivial:
$$A_{O}=\begin{pmatrix}0 & 0 & 2 \\ 1 & 0 & 1 \\ 0 & 1 & -2\end{pmatrix}~~,~~ B_{O}=\begin{pmatrix}-2 \\ 1 \\ 0\end{pmatrix}~~,~~C_{O}=\begin{pmatrix}0 & 0 & 1\end{pmatrix}~~,~~D_{O}=0$$
- Aqui notemos algo importante:
    - os valores próprios da matriz $A$ (da representação SS)
    - os polos da função transferência
    - as raízes do denominador da função transferência
    - as raízes do polinómio caraterístico da EDO
são **todos os mesmos valores!!!**

- O polinómio $s^{3}+2s^{2}-s-2$ tem as raízes: $-2,-1,2$. Assim, podemos reescrever a TF como
$$\frac{Y}{U}=\frac{c_{1}}{s+2}+ \frac{c_{2}}{s+1} + \frac{c_{3}}{s-2}$$
- Recordemos de *Sinais e Sistemas* como se calcula os C:
$$c_{1}=\frac{s-2}{(s-1)(s+1)}\biggr|_{s=-2}=- \frac{4}{3}$$
$$c_{2}=\frac{s-2}{(s-1)(s+2)}\biggr|_{s=-1}= \frac{3}{2}$$
$$c_{3}=\frac{s-2}{(s+1)(s+2)}\biggr|_{s=1}=- \frac{1}{6}$$
temos simplesmente: $$c_{i}=\left[\frac{Y}{U}\cdot(s-p_{i})\right]_{s=p_{i}}$$
e ficamos com a forma *diagonal*:
$$A_D =\begin{pmatrix}-2 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 2\end{pmatrix}~~,~~B_{D}=\begin{pmatrix}1 \\ 1 \\ 1\end{pmatrix}~~,~~ C_{D}=\begin{pmatrix}-4/3 \\ 3/2 \\ -1/6\end{pmatrix}^{T} ~~,~~ D_{D}=0$$

### Mudança de Base
- Consideremos o exemplo atrás. Temos as matrizes $A$ controlável e diagonal. Queremos então trocar entre estas bases. Temos:
$$A_{D}=T^{-1} A_{C} T$$
para determinar $T$ temos que calcular os vetores próprios de $A_{C}$. Não vou fazer aqui. Fica:
$$T=\begin{pmatrix}1 & 1 & 1 \\ -2 & -1 & 1 \\ -4 & 1 & 1\end{pmatrix}~~,~~T^{-1}=\frac{1}{6}\begin{pmatrix}-2 & 0 & 2 \\ 6 & -3 & -3 \\ 2 & 3 & 1\end{pmatrix}$$
- Podemos substituir e confirmar que:
$$A_{D}=T^{-1}A_{C}T~~,~~B_{D}=T^{-1}B_{C}~~,~~ C_{D}=C_{C}T~~,~~D_{D}=D_{C}$$

### Forma Real
- Consideremos a equação diferencial
$$y'''+4y''+6y'+4y=u$$
que resulta na FT:
$$\frac{Y}{U}=\frac{1}{s^{3}+4s^{2}+6s+4}$$
- Ora, os polos são complexos:
$$\frac{Y}{U}=\frac{1}{(s+2)(s+1+i)(s+1-i)}$$
como já vimos, estes são os valores próprios. E temos:
$$A_{D}=\begin{pmatrix}-2 & 0 & 0 \\ 0 & -1+i & 0 \\ 0 & 0 & -1-i\end{pmatrix}$$
e teremos $T=\begin{pmatrix}v_{1} & v_{2} & v_{3}\end{pmatrix}$

- Mas por vezes não é conveniente trabalhar com matrizes complexas. Assim, usamos a *forma real*: a matriz mais próxima de diagonal e com coeficientes reais:
$$A_{D_{R}}=\begin{pmatrix}-2 & 0 & 0 \\ 0 & -1 & 1 \\ 0 & -1 & 1\end{pmatrix}$$
em que temos: $T=\begin{pmatrix}v_{1} & \frac12(v_{2}+v_{3}) & \frac12(v_{2}-v_{3})\end{pmatrix}$
- Em 3x3 temos:
$$A_{D}=\begin{pmatrix}\lambda_{1} & 0 & 0 \\ 0 & a+bi & 0 \\ 0 & 0 & a-bi\end{pmatrix}~~\to~~A_{D_{R}}=\begin{pmatrix}\lambda_{1} & 0 & 0\\ 0 & a & b \\ 0 & -b & a\end{pmatrix}$$
