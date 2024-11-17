- Sabemos que um sistema pode ser descrita por:
$$\dot{x}=Ax+Bu$$
e vimos na aula anterior que temos a solução:
$$x(t)=\Phi(t,t_{0})x(t_{0})+\int_{t_{0}}^{t}\Phi(\tau,t_{0})Bu(\tau)d\tau$$

- Vimos ainda que num **LTI** (sistema Linear Time Invariant) temos:
$$\Phi(t,t_{0})=e^{A(t-t_{0})}$$
ou seja:
$$x(t)=e^{A(t-t_{0})}x(t_{0})+\int_{t_{0}}^{t}e^{A(\tau-t_{0})}Bu(\tau)d\tau$$

## Propriedades da Função $\Phi$
- Temos:
    1. Como já sabemos: $x(t_{1})=\Phi(t_{1},t_{0})x(t_{0})$ e $x(t_{2})=\Phi(t_{2},t_{1})x(t_{1})$. Daqui surge que: $x(t_{2})=\Phi(t_{2},t_{0})x(t_{0})$
    2. $\det(e^{A(t-t_{0})})\neq0~~\forall t\in \mathbb{R}$
    3. Tendo-se o valor e vetor próprios generalizados $(\bar \lambda,\bar v)$ temos:
        1. $(\bar\lambda^{k}, \bar v)$  são eig de $A^{k}$
        2. $(e^{\bar\lambda \tau},\bar v)$ são eig de $e^{A\tau}$
    4. Podemos aplicar a mudança de base à exponencial: $\tilde{A}=T^{-1}AT~\to~e^{\tilde{A}\tau}=T^{-1}e^{A\tau}T$ 
    5. Se $A$ for diagonal: $A=\text{diag}(\lambda_{1},\dots,\lambda_{n})$ também a exponencial será: $e^{A\tau}=\text{diag}(e^{\lambda_{1}\tau},\dots,e^{\lambda_{n}\tau})$
    6. O bloco de Jordan fica: $$A=\begin{bmatrix}\lambda & 1 & 0 \\ 0 & \lambda & 1 \\ 0 & 0 & \lambda\end{bmatrix}~~\to~~e^{A\tau}=\begin{bmatrix}1 & \frac{\tau}{1!} & \frac{\tau^{2}}{2!} \\ 0 & 1 & \frac{\tau}{1!} \\ 0 & 0 & 1\end{bmatrix}$$
    7. Consideremos uma matriz $A$ 2x2 em que $u(t)=0$. Temos os eig: $(\lambda=\sigma+i\mu,v=v_{R}+iv_{I})$. $\lambda^{*},v^{*}$ são os conjugados complexos.
        1. Se conseguirmos escrever $x(t_{0})$ como $x(t_{0})=\alpha v+\beta v^{*}$, então temos $x(t)=\alpha e^{\lambda(t-t_{0})} v +\beta e^{\lambda^{*}(t-t_{0})}v^{*}$ 
        2. Podemos ainda fazer uma mudança de base: $v_{A}=\frac12(v+v^{*})~,~v_{B}=\frac12(v-v^{*})$ e ficamos com: $$\tilde{A}=\begin{bmatrix}\sigma & -\mu \\ \mu & \sigma\end{bmatrix}~~\to~~ e^{\tilde{A}(t-t_{0})}=e^{\sigma(t-t_{0})}\begin{bmatrix}\cos(\mu(t-t_{0})) & -\sin(\mu(t-t_{0})) \\ \sin(\mu(t-t_{0})) & \cos(\mu(t-t_{0}))\end{bmatrix}$$
## Computar a matriz exponencial
### 1 - Laplace
- Para o caso em que $u=0$, da transformada de Laplace temos:
$$\begin{align*}
\dot{x}&= Ax\\
&\downarrow~(\mathcal{L})\\
sX-X_{0}&= AX\\
(sI-A)X&= X_{0}\\
X&= (sI-A)^{-1}X_{0}
\end{align*}$$
se fizermos Laplace inverso:
$$x(t)=\mathcal{L}\{(sI-A)^{-1}\}x(0)$$
ora, também temos que (para um LTI) $x(t)=e^{At}x(0)$.
- Logo, uma forma de determinar a matriz exponencial é:
$$e^{At}=\mathcal{L}^{-1}\{(sI-A)^{-1}\}$$

### 2 - Diagonal
- Se $A$ não tiver nenhum valor próprio com multiplicidade >1 podemos escrever:
$$A=T \Lambda T^{-1}$$
assim, conforme uma das propriedades acima:
$$e^{At}=Te^{\Lambda t}T^{-1}$$
em que $e^{\Lambda t}=\text{diag}(e^{\lambda_{1}t},\dots,e^{\lambda_{n}t})$.

#### NOTA TP
- Para isto, pode ser útil fazer divisão por frações parciais (com matrizes!)
- Por exemplo, temos:
$$(sI-A)^{-1}=\frac{1}{(s+2)(s+1)(s-1)}\begin{pmatrix}s^{2}+2s-1 & s+2 & 1 \\ 2 & s(s+2) & 2 \\ 2s & s+2 & s^{2}\end{pmatrix}$$
e podemos fazer divisão em frações parciais normalmente:
$$(sI-A)^{-1}=\frac{A_{1}}{s+2}+ \frac{A_{2}}{s+1} + \frac{A_3}{s-1}$$
em que:
$$A_{1}=\frac{\text{Adj}(sI-A)}{(s+1)(s-1)}\Biggr|_{s=-2}~~,~~A_{2}=\frac{\text{Adj}(sI-A)}{(s+2)(s-1)}\Biggr|_{s=-1}~~,~~A_{3}=\frac{\text{Adj}(sI-A)}{(s+2)(s+1)}\Biggr|_{s=1}$$
e ficamos com:
$$(sI-A)^{-1}=\mathcal{L}^{-1}\left\{\frac{\frac{1}{3}\begin{pmatrix}-1 & 0 & 1 \\ 2 & 0 & -2 \\ -4 & 0 & 4\end{pmatrix}}{s+2} + \frac{\frac{1}{2}\begin{pmatrix}2 & -1 & -1 \\ -2 & 1 & 1   \\ 2 & -1 & -1\end{pmatrix}}{s+1} + \frac{\frac{1}{6} \begin{pmatrix}2 & 3 & 1 \\ 2 & 3 & 1 \\ 2 & 3 & 1\end{pmatrix}}{s-1}\right\}$$

### 3 - Teorema de Cayley-Hamilton
- Tendo uma matriz $A\in \mathbb{R}^{n\times n}$, podemos escrever:
$$e^{At}=\alpha_{0}(t)I + \alpha_{1}(t)A + \alpha_{2}(t)A^{2}+\dots+\alpha_{n-1}(t)A^{n-1}$$
- Consequentemente, temos:
$$e^{\lambda_{i}t}=\alpha_{0}(t) + \alpha_{1}(t)\lambda_{i} + \alpha_{2}(t)\lambda_{i}^{2}+\dots+\alpha_{n-1}(t)\lambda_{i}^{n-1}$$
- Assim, se para cada instante resolvemos este sistema com $n$ lambdas e $n$ alfas, temos a exponencial $e^{At}$.

*Multiplicidade >1*
- Imaginemos que $\lambda_{j}$ tem multiplicdade 2. Neste caso teremos 2 equações para este valor (invés de 2 equações para 2 valores difrentes):
$$\begin{cases}
e^{\lambda_{j}t}=\alpha_{0}(t) + \alpha_{1}(t)\lambda_{j} + \alpha_{2}(t)\lambda_{j}^{2}+\dots+\alpha_{n-1}(t)\lambda_{j}^{n-1} \\
te^{\lambda_{j}t}= \alpha_{1}(t)+ 2\lambda_{i}\alpha_{2}(t) +\dots+ (n-1)\lambda_{i}^{n-1}\alpha_{n-1}(t)
\end{cases}$$

#### EX
- Temos a matriz: $$A=\begin{pmatrix}1 & 2 \\ 0 & 1\end{pmatrix}~~~~,~~~~ \lambda_{1}=\lambda_{2}=1$$
- Como a matriz é 2x2 temos:
$$e^{At}=\alpha_{0}(t)I + \alpha_{1}(t)A$$
e temos o sistema:
$$\begin{cases}
e^{\lambda t} = \alpha_{0} + \alpha_{1}\lambda \\
t e^{\lambda t}=\alpha_{1}
\end{cases}~~\to~~\begin{cases}
\alpha_{0}=e^{t}-te^{t} \\
\alpha_{1}=te^{t}
\end{cases}$$
e ficamos com:
$$e^{At}=(e^{t}-te^{t})I + te^{t}A = \begin{pmatrix}e^{t} & 2e^{t} \\ 0 & e^{t}\end{pmatrix}$$

## Controlabilidade
- Um sistema é controlável se conseguimos *sempre* ir de um certo $x(t_{0})$ para um qualquer $x(t)$.
- Como sabemos:
$$\begin{align*}
\dot{x}&= Ax+Bu\\
&\downarrow\\
x(t)&= e^{A(t-t_{0})}x_{0}+\int_{t_{0}}^{t}e^{A(\tau-t_{0})}Bu(\tau)d\tau\\
\underbrace{x(t)-e^{A(t-t_{0})}x_{0}}_{z}&=\int_{t_{0}}^{t}e^{A(\tau-t_{0})}Bu(\tau)d\tau\\
z&= \int_{t_{0}}^{t}e^{A(\tau-t_{0})}Bu(\tau)d\tau\\
&= \int_{t_{0}}^{t} \left(\sum\limits_{i=0}^{n-1} \alpha_{i}(t-\tau)A^{i} \right)(t-\tau)Bu(\tau)d\tau\\
&= \sum\limits_{i=0}^{n-1}A^{i}B\int_{t_{0}}^{t}(t-\tau)u(\tau)d\tau
\end{align*}$$
- Assim, para o sistema ser controlável, é preciso que "z consiga atingir qualquer ponto de $\mathbb{R}^{n}$"

- Temos ainda a *matriz de controlabilidade*:
$$M=\begin{bmatrix}B &| &  AB^{2} &| & \cdots & | & A^{n-1}B \end{bmatrix}$$
que, para o sistema ser controlável tem que *span* $\mathbb{R}^{n}$. De outra forma, é preciso que:
$$\text{rank}(M)=n$$
mais especificamente, se o input for escalar, isto é equivalente a
$$\det(M)\equiv|M|\neq0$$
- O **rank** é a "dimensão do subespaço vetorial que cosneguimos criar com as colunas da matriz" ou "o número de colunas que são vetores linearmente independentes".

**EX**
- Temos $$A=\begin{pmatrix}1 & 2 \\ 0 & 1\end{pmatrix}~~,~~B=\begin{pmatrix}1 \\ 0\end{pmatrix}$$
logo temos:
$$M=\begin{pmatrix}B & AB\end{pmatrix}=\begin{pmatrix}1 & 1 \\ 0 & 0\end{pmatrix}$$
logo $\text{rank}(M)=1$. Como estamos em $\mathbb{R}^{2}$, o sistema *não* é controlável.

## Observabilidade
- Um sistema é observável se, conhecendo o output $y$ conseguimos determinar o estado do sistema $x$ em **tempo finito**
- Podemos definir a matriz de observabilidade:
$$Q=\begin{pmatrix}C & CA & CA^{2} & \cdots & CA^{n-1}\end{pmatrix}^{T}$$
e o sistema é observável se
$$\text{rank}(Q)=n~~,~~ A\in\mathbb{R}^{n\times n}$$
