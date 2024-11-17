- Temos que a relação que descreve os nossos dados é
$$f(\boldsymbol{x}) = \theta_{0} + \theta_{1}\sin(x_{1})+\theta_{2}\cos(x_{2})+\theta_{3}e^{x_{3}}$$
este ajuste é não linear.

- Mas podemos fazer umas mudanças de variável que o tornam linear:
$$y=\theta_{0}+\theta_{1}x_{1}' + \theta_{2}x_{2}'+\theta_{3}x_{3}'$$
em que
$$x_{1}'=\sin(x_{1})~~,~~ x_{2}'=\cos(x_{2})~~,~~ x_{3}'=e^{x_{3}}$$

- Assim, ficamos com uma relação linear, que fará com que seja mais fácil usar a relação do enunciado. Mais concretamente, a relação de $y$ que temos acima pode ser escrita na forma:
$$\boldsymbol{y}=\boldsymbol{\theta}\mathbf{X}$$
$$\begin{align*}
\boldsymbol{y}&= \mathbf{X}\boldsymbol{\theta}\\
\mathbf{X}^{T}\boldsymbol{y}&= \mathbf{X}^{T}\mathbf{X}\boldsymbol{\theta}\\
\end{align*}$$
$$\boldsymbol{\theta}=(\mathbf{X}^{T}\mathbf{X})^{-1}\mathbf{X}^{T}\boldsymbol{y}$$

