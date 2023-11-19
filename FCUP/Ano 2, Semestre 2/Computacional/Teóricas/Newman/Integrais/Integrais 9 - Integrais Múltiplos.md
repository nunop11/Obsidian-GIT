# 12 - Integrais Múltiplos
- Consideremos o integral: $$I = \int_{0}^{1}\int_{0}^{1}f(x,y)dxdy$$
de onde podemos definir $$\mathcal{F}(y)= \int_{0}^{1}f(x,y)dx$$
e, portanto, $$I = \int_{0}^{1}\mathcal{F}(y)dy$$
- Uma forma de fazer isto é usar quadratura gaussiana com $N$ pontos de $x,y$ e temos $$\mathcal{F}(y)\sim \sum\limits_{i=1}^{N}\omega_{i}f(x_{i},y)\quad;\quad I\sim \sum\limits_{j=1}^{N} \omega_{j}\mathcal{F}(y_{j})$$

- No entanto, se juntarmos as 2 fórmulas acima, temos a *Fórmula do produto de Gauss-Legendre*:
$$I\sim \sum\limits_{i=1}^{N}\sum\limits_{j=1}^{N}\omega_{i}\omega_{j}f(x_{i},y_{j})$$
- Isto meio que é a quadratura gaussiana em 2 D, em que os pesos e pontos estão distribuídos numa secção do plano $xOy$. 
- No entanto, em 2D, 3D, etc. não é tão claro quais são os melhores pontos para fazer a integração.

---- PAG 195 DO PDF ----

#computacional #programacao #integrais 
