# Equação de Onda
- Definida como $\phi(\vec{r},t)$, descreve a evolução da grandeza física modelada pela onda 
- Temos a equação de Onda:
$$\left[ \frac{\partial^{2}}{\partial t^{2}} - v^{2} \frac{\nabla^{2}}{\nabla \vec{r}^{2}} \right]\phi=0$$
Ora, podemos simplificar isto ao reduzir a casos em 1D e escrever com a seguinte notação:
$$[\partial^{2}_{t} - v\partial_{x}^{2}]\phi(x,t)=0$$
em que $\partial^{2}_{a}=\frac{\partial^{2}}{\partial a^{2}}$

## Propriedades
### Linearidade
- Sendo $h(x,t)=\alpha f(x,t)+\beta g(x,t)$ em que $f,g$ são soluções da equação de onda. A equação tem a propriedade que nos diz que $h$ também será solução. 

**Prova**
Podemos escrever as derivadas parciais de $h$:
$$\begin{align*}
\partial^{2}_{t}h&= \alpha \partial_{t}^{2}f + \beta \partial_{t}^{2} g\\
\partial_{x}^{2}h&= \alpha \partial_{x}^{2}f + \beta \partial_{x}^{2} g
\end{align*}$$
Assim se aplicarmos a equação de onda a $h$ temos:
$$\begin{align*}
[\partial^{2}_{t} - v\partial_{x}^{2}]h(x,t)&= 0\\
\alpha \partial_{t}^{2}f + \beta \partial_{t}^{2} g - (\alpha \partial_{x}^{2}f + \beta \partial_{x}^{2} g)&= 0\\
[\alpha \partial_{t}^{2}f - \alpha \partial_{x}^{2}f] + [\beta \partial_{t}^{2} g -\beta \partial_{x}^{2} g]&= 0\\
0+0&= 0\\
0&= 0 
\end{align*}$$
pelo que $h(x,t)$ é também solução da equação de onda.