# 1 - EDO de 1 Variável
- Uma equação diferencial ordinária (EDO) de 1 variável será do tipo $$\frac{dx}{dt}=f(x,t)$$
- Para determinara a solução completa de uma equação deste tipo, também precisamos de conhecer os valores iniciais: $x(t=0)$. 

## 1.1 - Método de Euler
- Tendo uma equação diferentecial do tipo $\frac{dx}{dt}=f(x,t)$ em que conhecemos $x$ num certo valor de $t$, podemos determinar o valor de $x$ após um curto intervalo $h$ usando uma série de Taylor:
$$\begin{align*}
x(t+h)&= x(t) + h \frac{dx}{dt} + \frac{1}{2}h^{2} \frac{d^{2}x}{dt^{2}} + \dots\\
&= x(t) + h f(x,t) + O(h^{2})
\end{align*}$$
(ignoramos os termos acima de $h^{2}$, porque sendo $h$ um intervalo reduzido, o seu quadrado será ainda mais reduzido AKA $\approx0$)
- Ou seja, ficamos com $$\boxed{x(t+h)=x(t)+hf(x,t)}$$
- E está. Desde que $h$ seja suficientemente reduzido, a equação acima permite-nos determinar $x$ para quantos valores de $t$ quantos quisermos, com uma precisão bem boa.
- Na prática, consideremos que temos uma equação diferencial em que conhecemos $x(t=a)$ e queremos saber a solução da equação de $a$ a $b$. Definimos um $h$ reduzido e apenas usamos esta fórmula repetidamente até ficarmos com $t=b$.

- No entanto, neste método eliminamos os termos da série de Taylor a partir de $h^{2}$. Isto dá-nos aproximações decentes, mas ao fazer isto ficamos com um erro igual a $\frac{1}{2}h [f(x(b),b)-f(x(a),a)]$, que é proporcional a $h$. Ou seja, ao diminuir $h$ para metade também o erro diminui para metade, o que não é muito. Por outro lado, $N= \frac{b-a}{h}$, ou seja para diminuir $h$ (e o erro) para metade, iremos aumentar o número de passos (e o tempo de execução) para o dobro.

#computacional #programacao #eqs_difs 