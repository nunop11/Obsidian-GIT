# 3 - Intervalos até infinito
- Vejamos agora o que fazer se queremos obter a solução de uma Eq Dif para $t\to\infty$. Não podemos usar os métodos atrás, porque isso implicaria usar $N=\infty$ pontos.
- Ora, basta fazer o mesmo que fizemos com integrais: **mudança de variáveis**, assim:
$$u= \frac{t}{1+t} \quad \quad;\quad \quad t= \frac{u}{1-u}$$
sendo que se $t\to\infty$ então $u\to1$.

- Podemos então escrever:
$$\frac{dx}{dt}=f(x,t) \Longrightarrow \frac{dx}{du} \frac{du}{dt}=f(x,t)$$
ou seja:
$$\frac{dx}{du}= \frac{dt}{du}f(x,\tfrac{u}{1-u})$$
mas, como temos $t= \frac{u}{1-u}$, então: $\frac{dt}{du}=\tfrac{1}{(1-u)^{2}}$. Logo:
$$\frac{dx}{du}=(1-u)^{-2}f(x,\tfrac{u}{1-u})=g(x,u)$$
O que já é uma EDO normal que sabemos resolver normalmente.

#computacional #programacao #eqs_difs 