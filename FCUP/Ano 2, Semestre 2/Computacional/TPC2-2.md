# 2.1
- A dedução deste sistema é bastante semelhante ao sistema do exercício 1.2
- Conforme o enunciado temos a transformada de Fourier: $-m\omega^{2}x_{i}(\omega)=-k_{i}\left(x_{i}(\omega)-x_{i-1}(\omega)\right)+k_{i+1}\left(x_{i+1}(\omega)-x_{i}(\omega)\right)+\frac{2\gamma F}{\gamma^{2}+(\omega-\Omega)^{2}}\delta_{il}$. Ora, como $\omega=\Omega$ temos:
$$-m\omega^{2}x_{i}(\omega)=-k_{i}\left(x_{i}(\omega)-x_{i-1}(\omega)\right)+k_{i+1}\left(x_{i+1}(\omega)-x_{i}(\omega)\right)+\tilde F\delta_{il}$$sendo que $l=1, \tilde F=1, m=1$. Assim:
- Ora, podemos substituir $i$ por alguns valores:
$$\begin{align*}
i=1 : \quad -m\omega^{2}x_{1}(\omega)&= -k_{1}\left(x_{1}(\omega)-x_{0}(\omega)\right)+k_{2}\left(x_{2}(\omega)-x_{1}(\omega)\right)+\tilde F \cdot1\Longrightarrow -\tilde F = \cancelto0{x_{0}k_{1}} + x_{1}(-k_{2}-k_{1}+m\omega^{2}) + x_{2}k_{2}\\
i=2 : \quad -m\omega^{2}x_{2}(\omega)&= -k_{2}\left(x_{2}(\omega)-x_{1}(\omega)\right)+k_{3}\left(x_{3}(\omega)-x_{2}(\omega)\right)+\tilde F \cdot0\Longrightarrow 0 = x_{1}k_{2} + x_{2}(-k_{3}-k_{2}+m\omega^{2}) + x_{3}k_{3}\\
&(\dots)\\
\textsf{massa }i: \quad -m\omega^{2}x_{i}(\omega)&= -k_{i}\left(x_{i}(\omega)-x_{i-1}(\omega)\right)+k_{i+1}\left(x_{i+1}(\omega)-x_{i}(\omega)\right)+\tilde F \cdot0\Longrightarrow 0 = x_{i-1}k_{i} + x_{i}(-k_{i+1}-k_{i}+m\omega^{2}) + x_{i+1}k_{i+1}\quad\\
&(\dots)\\
i=N-1 : \quad -m\omega^{2}x_{N-1}(\omega) &= -k_{N-1}\left(x_{N-1}(\omega)-x_{N-2}(\omega)\right)+k_{N}\left(x_{N}(\omega)-x_{N-1}(\omega)\right)+\tilde F \cdot0\Longrightarrow 0= x_{N-2}k_{N-1} + x_{N-1}(-k_{N}-k_{N-1}+m\omega^{2}) + x_{N}k_{N}\\
i =N: \quad -m\omega^{2}x_{N}(\omega) &= -k_{N-1}\left(x_{N}(\omega)-x_{N-1}(\omega)\right)+k_{N+1}\left(x_{N+1}(\omega)-x_{N}(\omega)\right)+\tilde F \cdot0\Longrightarrow 0= x_{N-1}k_{N} + x_{N}(-k_{N+1}-k_{N}+m\omega^{2}) + \cancelto0{x_{N+1}k_{N+1}}\\
\end{align*}$$
Sendo que aqui é útil recordar $x_{i}(\omega)$ é o desvio relativamente à posição de equilíbrio de uma massa $i$. Como tal $x_{0}=X_{N+1}=0$.
- Ora, podemos escrever isto na forma de matriz:
$$\begin{pmatrix}
-k_{1}-k_{2}+m\omega^2 &k_{2} &\dots  &\dots &\dots &\dots &\dots\\ 
k_{2} &-k_{2}-k_{3}+m\omega^2 &k_{3} &\dots &\dots &\dots &\dots\\ 
\dots &\ddots  &\ddots &\ddots &\dots &\dots &\dots\\ 
\dots &\dots &k_{i} &-k_{i+1}-k_{i}+m\omega^2 &k_{i+1}  &\dots &\dots\\ 
\dots &\dots  &\dots &\ddots &\ddots &\ddots &\dots\\ 
\dots &\dots &\dots &\dots &k_{N-1} &-k_{N}-k_{N-1}+m\omega^2 &k_N \\ 
\dots &\dots &\dots &\dots &\dots &k_{N} &-k_{N+1}-k_{N}+m\omega^2
\end{pmatrix}
\begin{pmatrix}X_{1} \\ X_{2}  \\ \dots \\ X_{i} \\ \dots \\ X_{N-1} \\ X_{N}\end{pmatrix}=\begin{pmatrix} -\tilde F \\ 0 \\ \dots  \\ 0 \\ \dots \\ 0 \\ 0\end{pmatrix}$$
- Conforme o enunciado, temos $L=1, m=1, \tilde F=1$ e temos que as contantes de mola $k_{1},k_{2},\dots, k_{N}, k_{N+1}$ são geradas aleatoriamente a partir de uma distribuição normal. 
- Assim, temos a função `sistForcadoSolve`, que recebe a lista de $k$ e um valor de $\omega$. Esta função cria a matriz $A$ e vetor $v$ conforme mostrado acima e retorna a solução do sistema usando a função `gaussPivot` do exercício 1.1.
- Assim, no programa abaixo eu estou a aplicar esta função para cada valor de uma lista de $\omega$. Os valores de $\omega$ foram obtidos por tentativa e erro. Verifiquei que o gráfico $|x(\omega)|$ apenas apresenta picos até perto de $2$. No entanto, por causa da natureza aleatória dos $k$ usados, pode acontecer que tenhamos um pico após $\omega=2$, pelo que a lista de $\omega$ que criei vai de $0$ a $2.2$.


# 2.2
- O sistema de equações correspondente às $N$ massas em oscilação por ação de uma força externa a oscilar com frequência $\omega$ pode ser escrito da forma:
$$A \begin{pmatrix}x_1 \\ x_{2}  \\ \vdots  \\  x_{N}\end{pmatrix}=-m\omega^{2}\begin{pmatrix}x_1 \\ x_{2}  \\ \vdots  \\  x_{N}\end{pmatrix}$$
sendo $A$ a matriz que define o sistema sem forças externas aplicadas.
- Definindo $\begin{pmatrix}x_1 \\ x_{2}  \\ \vdots  \\  x_{N}\end{pmatrix}=X$, temos:
$$\begin{align*}
AX=-m\omega^{2}X\\
(A+m\omega^{2}I)X=0
\end{align*}$$
Ora, Isto tem a mesma forma que $A-\lambda I=0$, a definição dos autovalores. Assim, por comparação e, sendo $m=1$ temos:
$$\omega^{2}=-\lambda \Longrightarrow \omega=\sqrt{-\lambda}$$
