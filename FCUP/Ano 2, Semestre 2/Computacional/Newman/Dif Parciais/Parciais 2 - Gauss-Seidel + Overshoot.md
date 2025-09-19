## 1.2 - Overshoot
- Ao usar o método de Jacobi que vimos atrás, os valores vão lentamente convergindo para os valores reais. 
- Ora, consideremos que num certo exercício, um valor vai de $0.1$ para $0.3$ em 1 iteração e depois converge para $0.5$ mais lentamente. Ora, este processo seria acelerado se fizessemos um *overshoot* e saltássemos logo de $0.1$ para $0.4$.

- Voltemos ao problema da caixa com condições de fronteira bem definidas nas paredes.
- Consideremos que uma certa tentativa para um certo ponto é $\phi(x,y)$ e a tentativa seguinte será $\phi'(x,y)$. Podemos relacioná-las da seguinte forma: $$\phi'(x,y)=\phi(x,y)+\Delta \phi(x,y)$$em que $\Delta \phi(x,y)=\phi'(x,y)-\phi(x,y)$ (sendo que $\phi'$ é a equação $\phi=\frac{1}{4}[\dots]$ que nos permite determinar um valor da matriz).
- Podemos então definir uma outra tentativa que consiste em valor com overshoot, dados por: $$\phi_\omega(x,y)=\phi(x,y)+(1+\omega)\Delta \phi(x,y) \quad;\quad \omega>0$$
- Neste caso ficamos com $\phi_{\omega}(x,y)=(1+\omega)\phi'(x,y)-\omega \phi(x,y)$. A equação completa do potencial num ponto fica: $$\small\phi_\omega(x,y)= \frac{1+\omega}{4} [ \phi(x+a,y) + \phi(x-a,y)+ \phi(x,y+a) + \phi(x,y-a) ] - \omega \phi(x,y)$$
## 1.3 - Gauss-Seidel
- No método de Jacobi e no de Overshoot que temos acima estamos a calcular todos os valores da matriz de novo e depois substituir a matriz por uma nova.
- Ora, no método de Gauss-Seidel presumimos que todos os valores que determinamos serão melhores que os anteriores. Assim, mal determinamos o novo valor de um certo ponto da grelha deitamos o valor antigo fora e ficamos com esse. Na prática, basta usar um único array e apenas fazer overwrite dos valores.
- Ou seja, para representar o método de Jacobi misturado com Gauss-Seidel usamos:
$$\small\phi(x,y)\leftarrow \tfrac{1}{4} [ \phi(x+a,y) + \phi(x-a,y) + \phi(x,y+a) + \phi(x,y-a)]$$
(esta notação usada em CC significa que calculamos o valor da direita e depois ele é usado para substituir o da esquerda)
- Podemos ainda combinar os métodos de Gauss-Seidel e Overshoot e temos:
$$\small\phi(x,y)\leftarrow \frac{1+\omega}{4} [ \phi(x+a,y) + \phi(x-a,y)+ \phi(x,y+a) + \phi(x,y-a) ] - \omega \phi(x,y)$$
- Esta última combinação é mais rápida, em grande parte devido ao overshoot. No entanto, devemos notar que o método de Gauss-Seidel permite usar menos memória porque só temos 1 array
- Além disso, devemos combinar sempre estes 2, porque o método de Overshoot para grelhas quadradas é muito frequentemente *instável* AKA não converge.

### 1.3.1 - Escolher $\omega$
- Depende muito do problema e equações em específico. 
- Quase sempre, este método apenas converge para $\omega<1$. Dentro disso, normalmente maior será melhor, mas apenas até certo ponto.
- Regra geral: quanto maior melhor, mas é uma questão de experimentar.
- Por exemplo, no caso da caixa com condições de Fronteira, $\omega=0.9$ é o melhor valor. No Newman diz que o autor usou este método e o programa demorou 38s, enquanto que com o método de Jacobi demorou 10 minutos.

#computacional #programacao #eqs_difs 