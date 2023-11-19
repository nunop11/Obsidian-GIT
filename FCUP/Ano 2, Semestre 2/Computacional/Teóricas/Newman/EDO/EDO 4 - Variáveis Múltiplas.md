# 4 - Múltiplas Variáveis
- Consideremos agora que temos 2 equações diferenciais, mas em que continuamos a ter *1 variável independente*:
$$\frac{dx}{dt}=f_{x}(x,y,t) \quad \quad;\quad \quad \frac{dy}{dt}=f_{y}(x,y,t)$$
Podemos simplesmente generalizar para qualquer número de variveis, tal que:
$$\frac{d\mathbf{r}}{dt}=\mathbf{f}(\mathbf{r},t)$$
sendo $\mathbf{r}=(x,y,\dots)$ e $\mathbf{f}(\mathbf{r},t)=(f_{x}(\mathbf{r},t),f_{y}(\mathbf{r},t),\dots)$
- Temos então a resolução com o método Runge-Kutta de 4ª ordem:
$$\begin{align*}
\mathbf{k}_{1}&= h \mathbf{f}(\mathbf{r},t)\\
\mathbf{k}_{2}&= h \mathbf{f}(\mathbf{r}+ \tfrac12 \mathbf{k_{1}},t+\tfrac12h)\\
\mathbf{k}_{3}&= h \mathbf{f}(\mathbf{r}+ \tfrac12 \mathbf{k_{2}},t+\tfrac12h)\\
\mathbf{k}_{4}&= h \mathbf{f}(\mathbf{r} + \mathbf{k}_{3},t+h)\\
\mathbf{r}(t+h)&= \mathbf{r}(t) + \tfrac16(\mathbf{k}_{1}+2\mathbf{k}_{2}+2\mathbf{k}_{3}+\mathbf{k}_{4})
\end{align*}$$
sendo que em Python, $\mathbf{r}, \mathbf{f}$ serão arrays. Assim, o código será muito parecido àquele de resolução de 1 equação diferencial. (Ver página 345 do Newman - 355 do pdf)
- Podemos pensar nisto como sendo um sistema de equações diferenciais simultaneas.

#computacional #programacao #eqs_difs 