- Temos o sistema
$$\begin{cases}
\dot{x}=Ax+B\tilde{u} \\
\dot{\tilde{x}}=(A-K_{e}C)\tilde{x} + B \tilde{u} + K_{e}y \\
\tilde{u}=\frac{-K \tilde{x}+\beta}{I}
\end{cases}$$
- Logo
$$\begin{align*}
\dot{e}&= \dot{x} - \dot{\tilde{x}}\\
&= Ax+B\tilde{u} - (A-K_{e}C)\tilde{x} -B \tilde{u} + K_{e}y \\
&= Ae + K_{e}(y- C \tilde{x})\\
&= Ae + K_{e}(Cx-C \tilde{x})\\
&= (A-K_{e}C)e
\end{align*}$$
- Temos que o inclinómetro mede $\theta$ logo teremos $C=\begin{pmatrix}1 & 0\end{pmatrix}$ e temos
$$A - K_{e}C = \begin{pmatrix}0 & 1 \\ 79 & 0\end{pmatrix} - \begin{pmatrix}k_{e1} \\ k_{e2}\end{pmatrix}\begin{pmatrix}1 & 0\end{pmatrix}=\begin{pmatrix}-k_{e1} & 1 \\ 79-k_{e2} & 0\end{pmatrix}$$
logo
$$\det(sI - A + K_{e}C)=\det \begin{pmatrix}s + k_{e1} & -1 \\ k_{e2}-79 & s\end{pmatrix}=s^{2} + k_{e1}s + k_{e2}-79$$
- Queremos que o erro seja inferior a $10\%$ em $t=2$. Como $\dot{e}=(A-K_{e}C)e$ temos $e(t) = e_{0}e^{(A-K_{e}C)t}$. Assumindo que inicialmente temos um erro de $1$ (100%, caso máximo). 
- O erro máximo estará associado ao valor próprio máximo do expoente, ou seja: 
$$\begin{align*}
e^{\lambda_{max}t}&\le e_{max}\\
e^{2\lambda_{max}}&\le 0.1\\
\lambda_{max}&\le -1.15
\end{align*}$$

-  Temos $\lambda_{max}\le-1.15$ logo decidimos colocar os polos em $\lambda=-2$. Assim
$$\begin{align*}
s^{2} + k_{e1}s + k_{e2}-79 &= (s-\lambda)^{2}\\
&= s^{2}-2\lambda+\lambda^{2}
\end{align*}$$
logo
$$\begin{align*}
k_{e1}&= -2\lambda\\
k_{e2}&= 79 + \lambda^{2}
\end{align*}$$