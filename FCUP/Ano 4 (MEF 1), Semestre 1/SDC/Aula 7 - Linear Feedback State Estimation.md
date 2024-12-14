## Linear Feedback State Estimation
- Outra coisa que falamos no início da UC foi que a variável/vetor de estado, $x$, normalmente não pode ser medida normalmente. Em muitos casos nem tem significado físico.
- Assim, introduzimos um estimador no sistema, que estima $x$ usando o output $y$:
![[Pasted image 20241125113640.png]]
e vemos que a única coisa nova é $K_{e}$!

- Podemos ver que a nossa estimativa é:
$$\dot{\tilde{x}}=A \tilde{x}+Bu+K_{e}(y-C \tilde{x})$$
- E temos claro o nosso erro:
$$e=x-\tilde{x}$$
que deve convergir para zero o mais rapidamente possível. De preferência mais rápido do que o sistema atua. O que temos *sempre* é:
$$e(t)\to0~~,~~t\to\infty$$

### Observável
- Tal como era o caso de um sistema de feedback, podemos determinar um vetor $K_{e}$ que nos permite calcular o erro, *se e só se* o sistema é **Observável**
    - Aqui voltamos à definição de "observabilidade" que vimos mais atrás: um sistema é observável se o seu estado $x$ pode ser determinado usando a saída $y$ num tempo finito.
- A demonstração deste teorema está no PPT

### Ke agora com feedback
- Voltemos de novo ao sistema de feedback com estimador. Podemos reescrever a equação de $\dot{\tilde{x}}$ assim:
$$\dot{\tilde{x}}=(A-BK-K_{e}C)\tilde{x} + K_{e}y$$
logo
$$\dot{e}=\dot{x}-\dot{\tilde{x}}=(A-K_{e}C)e$$
- Assim, teremos um sistema em que o *erro converge para zero* SE:
$$\text{Re}[\text{eig}(A-K_{e}C)]<0$$

### Métodos de determinar Ke
#### Determinar polos
- Consideremos que queremos que o erro em $t=5$ esteja abaixo de $0.001$.
- Temos
$$\dot{e}=(A-K_{e}C)e$$
logo
$$e(t)=e_{0}e^{(A-K_{e}C)t}$$
e podemos diagonalizar esta matriz exponencial:
$$e(t)=e_{0} P e^{Dt}P^{-1}$$
em que
$$e^{Dt}=\begin{pmatrix}e^{\lambda_{1}t} & 0 & 0 \\ 0 & e^{\lambda_{2}t} & 0 \\ 0 & 0 & e^{\lambda_{3}t}\end{pmatrix}$$
- Considerando que $\|e_{0}\|=1$, o nosso objetivo de erro pode ser escrito como:
$$\begin{align*}
\|e(t=5)\|&\le 0.001\\
e^{\lambda_{max}\cdot5} &\le 0.001\\
5\lambda_{max}&\le \ln(0.001)\\
\lambda_{max}&\le \frac{\ln(0.001)}{5}\\
\lambda_{max}&\le -1.3816\dots
\end{align*}$$
em que podemos arredondar e temos: $$\lambda_{max}=-2$$
- Ou seja, para garantir que temos o erro desejado podemos simplesmente definir:
$$p(s)=(s+2)(s+3)(s+4)$$
em que temos os autovalores -2,-3,-4. O máximo é aquele que vimos então o erro irá comportar-se como desejado.

#### Método direto
- De forma idêntica ao que fizemos para determinar $K$, temos o polinómio desejado que nos dá o erro que queremos:
$$\phi(s)=(s-p_{1})(s-p_{2})\cdots(s-p_{n})$$
e podemos determinar $K_{e}=\begin{pmatrix}K_{e}^{1} & K_{e}^{2} & \cdots  & K_{e}^{n}\end{pmatrix}$ igualando:
$$\det(sI-A+K_{e}C)=\phi(s)$$
e resolvemos o sistema.
- Este método funciona mas, como sabemos, é muito trabalhoso.

#### Fórmula de Ackermann
- A fórmula de ackerman para este tipo de sistema é
$$K_{e}=\tilde{\phi}(A)Q^{-1}\begin{pmatrix}0 \\ 0 \\ \vdots \\ 0 \\ 1\end{pmatrix}$$
em que:
    - $A$ é a matriz do sistema
    - $Q$ é a matriz de observabilidade
    - $\tilde{\phi}(\cdot)$ é o polinómio caraterístico do erro aplicado a matrizes.

#### COF
- Temos um sistema numa forma que NÃO a COF
- Podemos definir a matriz de transformação para a representação COF, $U$. Podemos escrevê-la como:
$$U=WQ^{T}$$
em que $Q$ é a matriz de observabilidade e temos
$$W=\begin{pmatrix}a_{n-1} & a_{n-2} & \dots & a_{1} & 1 \\ a_{n-2} & a_{n-3} & \dots & 1 & 0 \\ \vdots & \vdots && \vdots & \vdots \\ a_{1} & 1  & \dots & 0 & 0 \\ 1 & 0 & \dots & 0 & 0\end{pmatrix}$$
(sim, é a mesma que para calcular $K$)
- Não sei demonstrar, mas temos:
$$K_{e}=U^{-1}\begin{pmatrix}\beta_{n}-a_{n} \\ \beta_{n-1}-a_{n-e} \\ \vdots \\ \beta_{1}-a_{1}\end{pmatrix}$$

### E se não for observável?
- Novamente, o PPT tem indicações de formas como podemos contornar isto.

## Juntar tudo em forma matricial
- Consideremos então um sistema assim:
![[Pasted image 20241125122333.png]]
em que 
$$\begin{cases}
\dot{x}=Ax+Bu \\
y=Cx \\
\dot{\tilde{x}}=(A-K_{e}C)\tilde{x}+Bu+K_{e}y \\
u=-K \tilde{x}
\end{cases}$$
ou seja, $u$ depende da *estimativa* de $x$, não do estado em si!

- Novamente, temos o erro $e=x-\tilde{x}~~\to~~ \tilde{x}=x-e$
- Podemos escrever isto tudo assim:
$$\begin{pmatrix}\dot{x} \\ \dot{e}\end{pmatrix}=\begin{pmatrix}A-BK & BK \\ 0 & A-K_{e}C\end{pmatrix}\begin{pmatrix}x \\ e\end{pmatrix}$$
  