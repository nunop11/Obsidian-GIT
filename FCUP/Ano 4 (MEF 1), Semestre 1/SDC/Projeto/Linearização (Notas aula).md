- Consideremos um sistema não linear:
$$\dot{x}=f(x,u)\quad;\quad y=g(x,u)$$
que queremos converter num sistema linear, para melhor estar, deste tipo:
$$\dot{\tilde{x}}=A\tilde{x}+B\tilde{u} \quad;\quad \tilde{y}=C\tilde{x}+D\tilde{u}$$

- O sistema linear será o resultado de aproximar o sistema original a linear numa região de tempo suficientemente reduzida.
- Essa aproximação é ainda feita em torno de um *ponto de equilíbrio*

**Série de Taylor**
- Recordemos que
$$f(z)=f(\overline{z})+\frac{\partial f}{\partial z}(\overline{z})(z-\overline{z})+\dots$$
em que a derivada se torna numa matriz Jacobiana para dimensões >1

### 1 - Encontrar ponto de equilíbrio
- O ponto de equilíbrio é definido como o ponto $(\overline{x},\overline{u})$ em que temos: $$f(\overline{x},\overline{u})=0~~\to~~ \dot{x}=0$$

### 2 - Sistema Dinâmico
- Consideremos que:
$$\tilde{x}=x-\overline{x}\quad;\quad \tilde{u}=u-\overline{u}$$
logo:
$$\dot{\tilde{x}}=\dot{x}-\dot{\overline{x}}$$
ora:
$$\begin{align*}
\dot{\tilde{x}} &= f(x,u) - f(\overline{x},\overline{u})\\
&= f(x,u) - 0\\
&= f(\overline{x},\overline{u}) + \frac{\partial f}{\partial x}(\overline{x},\overline{u})\cdot(x-\overline{x}) + \frac{\partial f}{\partial u}(\overline{x},\overline{u})\cdot(u-\overline{u})\\
&= 0 + \frac{\partial f}{\partial x}(\overline{x},\overline{u})\cdot(x-\overline{x}) + \frac{\partial f}{\partial u}(\overline{x},\overline{u})\cdot(u-\overline{u})\\
&= \frac{\partial f}{\partial x}(\overline{x},\overline{u})\cdot \tilde{x} + \frac{\partial f}{\partial u}(\overline{x},\overline{u})\cdot \tilde{u}\\
\end{align*}$$
e porque não definir:
$$\dot{\tilde{x}}=A \tilde{x}+B \tilde{u}$$
- Ou seja:
$$\begin{align*}
A&= \frac{\partial f}{\partial x}(\overline{x}, \overline{u})\\
B&= \frac{\partial f}{\partial u}(\overline{x}, \overline{u})\\
C&= \frac{\partial g}{\partial x}(\overline{x}, \overline{u})\\
D&= \frac{\partial g}{\partial u}(\overline{x}, \overline{u})
\end{align*}$$
