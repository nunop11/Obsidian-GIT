- Temos uma função $f(x)$ que conhecemos apenas em 2 pontos $a,b$.
- **Interpolação** resume-se a tentar determinar 1 ponto de $f$ algures entre $a$ e $b$.

![[interpolacao.png]]
- O caso mais simpls é *interpolação linear*.
- Basicamente, presumimos que a função é uma reta, que terá declive: $$m=\frac{f(b)-f(a)}{b-a}$$
- Tendo um ponto $x$ como ilustrado acima, temos:
$$\begin{align*}
f(x) \approx f(a) + y &=  f(a) + \frac{f(b)-f(a)}{b-a}(x-a)\\
&= \frac{(b-x)f(a)+(x-a)f(b)}{b-a}
\end{align*}$$
de notar que esta fórmula também pode ser usada para *extrapolar* pontos além de $[a,b]$.

## Erros
- Procedemos da mesma forma que fizemos com derivadas. Começamos com 2 séries de Taylor:
$$\begin{align*}
f(a)=f(x) + (a-x)f'(x)+ \frac{1}{2}(a-x)^{2}f''(x)+\dots\\
f(b)=f(x) + (b-x)f'(x)+ \frac{1}{2}(b-x)^{2}f''(x)+\dots
\end{align*}$$
- Substituímos $f(a),f(b)$ na fórmula de $f(x)$ acima e temos:
$$f(x)= \frac{(b-x)f(a)+(x-a)f(b)}{b-a} + (a-x)(b-x)f''(x)+\dots$$
ou seja o erro é:
$$\epsilon=(a-x)(b-x)f''(x)+\dots$$
- De notar que consoante $x\to a, x\to b$ temos que $\epsilon\to0$. Isto faz sentido e indica que o erro máximo será no centro do intervalo.
- Presumindo que $f''$ varia devagar, podemos definir $b-a=h$ e temos que, no centro do intervalo, $\epsilon=\frac{1}{4}h^{2}|f''(x)|$. Ou seja, o erro de aproximação varia da mesma forma que o erro da derivada ao centro e conseguimos reduzi-lo ao *diminuir* $h$.
- No entanto, como na interpolação fazemos *somas* em vez de subtrações (que era o caso das derivadas), não precisamos de nos preocupar com erros de arredondamento.
- Se só conhecermos 2 pontos, interpolação linear é a melhor aproximação que podemos fazer.

#computacional #programacao 