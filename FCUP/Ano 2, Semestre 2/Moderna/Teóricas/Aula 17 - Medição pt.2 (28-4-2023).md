# Postulado 4 
- Se numa medição de energia se obteve o valor $E_{n}$ correspondente à função de onda $\Psi_{n}(x,t)$ num instante $t=t_{0}$ (sendo o sistema descrito por $\Psi(x,t$)), então em $t>t_{0}$ o sistema fica no estado $\Psi_{n}$.

__*EXEMPLO 1*__
- Voltemos ao exemplo do poço infinito da aula anterior:
$$V(x)=\begin{cases}0 &; &0<x<a \\ \infty &; &complementar\end{cases}$$
em que temos:
$$\Psi(x,t)= \frac{1}{\sqrt{3}}\varphi_{1} e^{-i \frac{E_{1}}{\hbar} t} - i\sqrt{\frac{2}{3}} \varphi_{2} e^{-i\frac{E_{2}}{\hbar}t}$$
- Conforme vimos nos exemplos do Postulado 3, $|C_{1}|^{2}+|C_{2}|^{2}=1$
- Faz se a medição da energia em $t=t_{0}$. Tal como vimos no Postulado 3, a probabilidade de obter $E_{1}$ é $\frac{1}{3}$ e a de obter $E_{2}$ é $\frac{2}{3}$.
- Assim, se na medição se obteve $E_{1}$, então:
$$t\to t_{0}^{+} \quad \Longrightarrow \quad \Psi(x, t_{0}^{+})\to \varphi_{1}(x)$$
e, deste modo:
$$t>t_{0} \quad\Longrightarrow \quad \Psi(x, t>t_{0})=\varphi_{1} e^{-i \frac{E_{1}}{\hbar}(t-t_{0})}$$

# Postulado 5
- As grandezas físicas podem ser representadas por operadores $f\in F$, sendo $F$ a base de funções.

### Exemplo - Posição
- Temos $\Psi(x, 0) = \frac{1}{\sqrt{3}}\varphi_{1} - i \sqrt{\frac{2}{3}}\varphi_{2}$. Ou seja, temos os operadores $\{ \varphi_{n}, n=1,2,3,\dots \}$

- Podemos definir uma base das posições $(x,y,z)$. Nessa base:
$$\begin{align*}\\
x \to \hat X &= x\\
y \to \hat Y &= y\\
z \to \hat Z &= z\\
p_{x} \to \hat P_{x} &= \frac{\hbar}{i} \frac{\partial}{\partial x} \\
p_{y} \to \hat P_{y} &=  \frac{\hbar}{i} \frac{\partial}{\partial y} \\
p_{z} \to \hat P_{z} &=  \frac{\hbar}{i} \frac{\partial}{\partial z}
\end{align*}$$(sendo $X,Y,Z,P_{x},P_{y},P_{z}$ operadores.)
- Na **física clássica** temos $E_{c}=\frac{p^{2}}{2m}$. Ora, $p_{x}=\frac{\hbar}{i} \frac{\partial}{\partial x}$, logo $p_{x}^{2}= -\hbar^{2} \frac{\partial^{2}}{\partial x^{2}}$. Assim:
$$E_{c}= \frac{-\hbar^{2}}{2m} \left[ \frac{\partial^{2}}{\partial x^{2}} + \frac{\partial^{2}}{\partial y^{2}} + \frac{\partial^{2}}{\partial z^{2}} \right] = - \frac{\hbar^{2}}{2m} \nabla^{2}$$
- Ora, o operador *Hamiltoniano* pode ser esscrito como:
$$H = E_{c}+V = - \frac{\hbar^{2}}{2m} \nabla^{2} + V$$
pelo que podemos escrever a equação de Schrödinger da forma:
$$H \Psi=E \Psi$$

- Ainda acerca disto, temos:
$$E\to \hat{E}=i\hbar \frac{\partial}{\partial t}$$

#moderna #fisica #quantica 