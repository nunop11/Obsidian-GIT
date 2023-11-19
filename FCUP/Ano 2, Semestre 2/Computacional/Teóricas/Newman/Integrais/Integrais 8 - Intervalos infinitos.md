# 11 - Integrais em Intervalos Infinitos
- Os métodos que conhecemos não funcionam numa integral assim. Ora, a solução é simplesmente **trocar de variáveis**
- Consideremos que temos $$\int_{0}^{\infty}f(x)dx$$
a mudança de variável que fazemos é: $$z= \frac{x}{1+x}\leftrightarrow x = \frac{z}{1-z}$$ de onde temos: $$dx = \frac{1}{(1-z)^{2}}dz$$
e, assim: $$\int_{0}^{\infty}f(x)dx=\int_{0}^{1} \frac{1}{(1-z)^{2}} f \left( \frac{z}{1-z} \right) dz$$
que já sabemos fazer com qualquer método.

- Outras opções de mudanças de variável:
$$z = \frac{x}{c+x}, \forall c \quad \quad; \quad \quad z = x^{\gamma}(1+x^{\gamma}),\forall \gamma$$
- Normalmente, temos que ver qual é a melhor mudança variável, dependendo do caso.

---

- Para fazer um integral de $a$ a $\infty$ faríamos uma mudança do tipo:
$$z = \frac{x-a}{1+x-a} \leftrightarrow x= \frac{z}{1-z}+ a$$
que podemos ver como primeiro fazer a mudança $y=x-a$ e depois $z = \frac{y}{1+y}$. 
- Daqui temos:
$$\int_{0}^{\infty}f(x)dx = \int_{0}^{1} \frac{1}{(1-z)^{2}} f\left(\frac{z}{1-z} + a\right)dz$$
---

- Por outro lado, se tivermos um integral de $-\infty$ a $a$, fazemos tudo igual e no fim $z\to-z$.

---

- Para integrais de $-\infty$ a $+\infty$, dividimos o integral em 2 partes: $]-\infty,0]$ e $[0, +\infty[$. Ou então dividimos de $-\infty$ a $a$ e daí a  $+\infty$.
- Podemos ainda fazer 1 só substituição:
$$x = \frac{z}{1-z^{2}} \Longrightarrow dx= \frac{1+z^{2}}{(1-z^{2})^{2}}dz$$
de onde temos:
$$\int_{-\infty}^{+\infty}f(x)dx = \int_{-1}^{1} \frac{1+z^{2}}{(1-z^{2})^{2}} f\left(\frac{z}{1-z^{2}}\right) dz$$
- Outra possibilicadade seria: 
$$x = \tan z\Longrightarrow dx = \frac{1}{\cos^{2}z} dz$$
de onde temos:
$$\int_{-\infty}^{+\infty} f(x)dx = \int_\frac{-\pi}{2}^{\frac{+\pi}{2}} \frac{1}{\cos^{2}z} f(\tan z) dz$$

#computacional #programacao #integrais 
