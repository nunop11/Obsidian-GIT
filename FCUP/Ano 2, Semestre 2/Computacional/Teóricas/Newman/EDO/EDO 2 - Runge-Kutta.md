# 2 - Runge-Kutta
- Conforme o que vimos na secção anterior, a causa do erro relativamente alto do método de Euler é o facto de desprezar-mos os termos da série de Taylor a partir de $h^{2}$. Assim, pode parecer sensato incluir o termo com $h^{2}$, tendo-se:
$$\frac{1}{2}h^{2} \frac{d^{2}x}{dt^{2}}= \frac{1}{2}h^{2} \frac{df}{dt}$$
mas a derivada de $f$ pode ser bastante difícil de determinar, porque nem sempre temos uma fórmula que define $f$, apenas um conjunto de valores. Mas mesmo que tenhamos uma fórmula, determinar derivadas é menos conveniente do que o método de Runge-Kutta.

- Ora, o método de Runge-Kutta consiste numa série de métodos, com diferentes graus. Aliás, o método de Euler pode ser considerado um método de Runge-Kutta: *Método de Runge-Kutta de 1º grau*.

## 2.1 - Runge-Kutta 2ª Ordem
![[metodo euler.png]]
- Uma equação diferencial $\frac{dx}{dt}=f(x,t)$ diz-nos que o declive da curva $x(t)$ num certo $t$ será $f(x,t)$.
- Ora, no Método de Euler, usamos esta informação para extrapolar o ponto $x(t+h)$ usando o ponto $x(t)$ e a função $f$. Mas vemos na imagem acima que se a solução da eq Dif for curva, então poderemos ter erros elevados.

- Consideremos agora que, partindo de $x(t)$ usamos o declive no *midpoint* $t+ \frac{1}{2}h$ para extrapolar o ponto seguinte, como temos acima. Isto normalmente irá dar aproximações melhores que o método de Euler, pelo que é a base do método Runge-Kutta de 2ª ordem.

- Em termos matemáticos, fazemos uma expansão de Taylor de $x(t+h)$ em torno de $t+ \frac{1}{2}h$:
$$\small x(t+h)=x(t+ \tfrac{1}{2}h) + \tfrac{1}{2}h \left( \frac{dx}{dt}\right)_{t+ \tfrac{1}{2}h} + \tfrac{1}{8} h^{2} \left( \frac{d^{2}x}{dt^{2}} \right)_{t+ \tfrac{1}{2}h} + O(h^{3})$$
Podemos fazer o mesmo para $x(t)$ e temos:
$$\small x(t+h)=x(t+ \tfrac{1}{2}h) - \tfrac{1}{2}h \left( \frac{dx}{dt}\right)_{t+ \tfrac{1}{2}h} + \tfrac{1}{8} h^{2} \left( \frac{d^{2}x}{dt^{2}} \right)_{t+ \tfrac{1}{2}h} + O(h^{3})$$
- Facilmente vemos que isto nos dá:
$$\begin{align*}
x(t+h)&= x(t) + h \left( \frac{dx}{dt} \right)_{t+ \tfrac{1}{2}h} + O(h^{3})\\
&= x(t) + h ~f(x(t+ \tfrac{1}{2}h), t + \tfrac12 h) + O(h^{3})
\end{align*}$$
- Notemos que agora apenas eliminamos os termos a partir de $h^{3}$, o que irá resultar em mais exatidão. Ou seja, recordando o capítulo de integrais, o termo de Runge-Kutta de 2ª ordem significa que tem alta exatidão até $h^{2}$.

- No entanto, este método implica que, para determinar $x(t+h)$ precisamos de $x(t)$, que conhecemos, e $x(t+\tfrac12)$, que não conhecemos.
- Para resolver isto, usamos o método de Euler. Ou seja, determinamos $x(t+\tfrac12h)$ usando: $x(t+\tfrac12h)=x(t)+\tfrac12hf(x,t)$. Ou seja, o processo de aplicação deste método é:

0. Começamos num ponto $x(t)$ conhecido.
1. Determinar $k_{1}=hf(x,t)$
2. Determinar $k_{2}= hf(x+\tfrac12k_{1}, t+ \tfrac12h)$, que será o declive no midpoint
3. Determinar $x(t+h)=x(t)+k_{2}$, o próximo ponto
4. Repetir o processo com $x(t+h)$ para obter $x(t+2h)$

- Para um mesmo $h$, este método é muito mais preciso que o de Euler. Aliás, podemos aumentar $h$ para reduzir o tempo de execução e ainda assim obter a mesma exatidão que o método de Euler.
- De notar que, ao fazer a aproximação com método de Euler para obter o declive no midpoint *não* estamos a aumentar o erro de forma significativa, porque o erro dessa aproximação também depende de $h^{3}$. (Demo na página 33 do Newman).

## 2.2 - Runge-Kutta 4ª Ordem
- Ao fazer um processo semelhante à dedução do método de 2ª ordem, mas mais complicado, podemos obter o seguinte método:

$$\begin{align*}
k_{1}&= hf(x,t)\\
k_{2}&= hf(x+\tfrac12k_{1}, t+\tfrac12h)\\
k_{3}&= hf(x+\tfrac12k_{2}, t+\tfrac12h)\\
k_{4}&= hf(x+k_{3},t+h)\\
x(t+h)&= x(t)+ \tfrac16(k_{1}+2k_{2}+2k_{3}+k_{4})
\end{align*}$$
- Este é o método mais comum. É preciso até $h^{4}$ e o seu erro varia com $h^{5}$. Por exemplo, para uma equação testada no Newman, os resultados obtidos para $N=1000$ com Euler são semelhante obtidos com $N=20$ com Runge-Kutta de 4ª ordem.
- De notar que, se as 5 fórmulas acima forem mal escritas no programa, poderemos obter erros elevados, mas ainda assim dificeis de ver à primeira.

#computacional #programacao #eqs_difs 