# 9 - Método do Midpoint Modificado
- Outra caraterística importante do Leapfrog é que o seu erro é uma função **par** de $h$. Novamente, isto é causado pelo facto de o método ter simetria de time-reversal.

- Sabemos que 1 passo do método de leapfrog tem erro de ordem $h^{3}$, ou seja, podemos definir o erro de 1 passo como sendo uma função $\varepsilon(h)$, cujo primeiro termo é proporcional a $h^{3}$.
- Consideremos que, num intervalo $[0,h]$, o erro aumenta. Ou seja, o erro de $0\to h$ será $\varepsilon(h)$ e será *positivo*. No entanto, se formos no sentido $h\to0$ o erro irá diminuir e temos $\varepsilon(-h)$ que será *negativo*. Ou seja, podemos escrever: $$\varepsilon(-h)=-\varepsilon(h)$$
- Ora, isto é a definição de uma função *ímpar*. Assim temos: $$\varepsilon(h)=c_{3}h^{3}+c_{5}h^{5}+c_{7}h^{7}+\dots$$

- No entanto, como já vimos antes, o erro de 1 passo de Leapfrog é de ordem $h^{3}$, mas o erro resultante de fazer muitos passos de tamanho $h$ será 1 ordem menor: $h^{2}$. Ou seja, para determinar a solução de uma EDO num intervalo de tempo de duração $\Delta$ precisamos de $\Delta/h$ passos. O erro da operação total será: $\varepsilon(h)\cdot \tfrac{\Delta}{h}$. Ou seja, ficaremos com uma fórmula do erro em que as parcelas têm $h$ com expoentes pares.

- Ou seja, o erro do método de Leapfrog é par (os passos intermédios do leapfrog mais exatamente)
- No entanto, para iniciar o método de leapfrog e obter o midpoint usamos o método de Euler. Ora, este tem erro de ordem $h^{2}$. E este não apresenta parcelas com termos apenas pares, tal como vimos acima para o leapfrog. Ou seja, o facto de fazermos este primeiro passo impede-nos de ter uma função do erro do método de Leapfrog par.

**Solução**
- Consideremos que queremos determinar a solução de uma EDO num intervalor de tempo $[t,t+H]$, usando $n$ passos de tamanho $h=H/n$.
- Podemos escrever: $$\begin{align*}
x_{0}&= x(t)\\
y_{1}&= x_{0} + \tfrac12hf(x_{0},t)
\end{align*}$$
de onde temos, de uma forma geral: $$\begin{align*}
y_{m+1}&= y_{m} + hf(x_{m},t+mh)\\
x_{m+1}&= x_{m} + hf(y_{m+1},t+(m+\tfrac12)h)
\end{align*}$$
- Ou seja, os 2 valores finais que calculamos são: $y_{n}:x(t+H-\tfrac12h)$ e $x_{n}:x(t+H)$, em que normalmente considerariamos $x_{n}$ o nosso valor final de $x(t+H)$.
- No entanto, podemos determinar um outro valor de $x(t+H)$, usando $y$: $$x(t+H)=y_{n}+\tfrac12hf(x_{n},t+H)$$
- Podemos então combinar os 2 valores de $x(t+H)$, fazendo a sua média: $$x(t+H)=\frac{1}{2}[x_{n}+y_{n}+\tfrac12hf(x_{n},t+H)]$$
- Ora, devido a matemática e magia, determinar o último valor da solução desta forma faz com que os termos de expoente ímpar causados pelo método de Euler no primeiro passo se *anulem*, sendo que ficamos com um erro definido por uma *função par*.
- Este método, que consiste em fazer o Leapfrog com um passo final extra, é o **midpoint modificado**, que é basicamente inútil sozinho. A sua importância reside no facto de ser a base do método de Bulirsch-Stoer.

#computacional #programacao #resumo 