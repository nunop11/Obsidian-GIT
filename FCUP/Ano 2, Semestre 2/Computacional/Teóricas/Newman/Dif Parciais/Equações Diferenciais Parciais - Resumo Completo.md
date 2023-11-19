# 1 - Condição de Fronteira
- Uma técnica muito útil é o *método das finitas diferenças*.
- Consideremos o seguinte problema de eletroestática:
![[problema condicao fronteira.png]]
    - Temos uma caixa em que todas as paredes estão a $0~\text{Volt}$, exceto a de cima que está a um potencial $V$. Consideramos que elas estão isoladas. Queremos determinar o potencial nos pontos na caixa.
    - Para isto usamos a equação de Laplace: $\nabla^{2} \phi=0$
    - Consideremos um problema em 2D, sendo que temmos: $$\frac{\partial^{2}\phi}{\partial x^{2}} + \frac{\partial^{2}\phi}{\partial y^{2}}=0$$
    - Ora, o desafio é aplicar as *condições de fronteira*. 
    - Usemos então o método das diferenças finitas. Para isso, começamos por dividir o espaço em estudo numa grelha, incluindo pontos na fronteira e fora dela.
    - Consideremos que dividimos o quadrado acima numa grelha de quadrados de lado $a$ e que pretendemos determinar o potencial num ponto $(x,y)$. Usando a fórmula que vimos para a segunda derivada de uma funnção na respetiva secção temos: $$\begin{align*}
\frac{\partial^{2}\phi}{\partial x^{2}}&= \frac{\phi(x+a,y) + \phi(x-a,y)-2\phi(x,y)}{a^{2}}\\
\frac{\partial^{2}\phi}{\partial y^{2}}&= \frac{\phi(x,y+a) + \phi(x,y-a)-2\phi(x,y)}{a^{2}}
\end{align*}$$ sendo que em ambos os casos usamos os pontos adjacentes (na direção $x$ e $y$) ao ponto $(x,y)$.
    - Ou seja, a Equação de Laplace fica: $$\small\frac{\phi(x+a,y) + \phi(x-a,y)-2\phi(x,y) + \phi(x,y+a) + \phi(x,y-a)-2\phi(x,y)}{a^{2}}=0$$
    - Ora, teremos uma equação destas para cada ponto da grelha. Ou seja, transformamos uma equação diferencial parcial num sistema de equações lineares.

## 1.1 - Método de Relaxação - Jacobi
- Ora, podemos usar decomposição de Gauss ou LU para resolver o sistema obtido, claro. Mas neste caso é muito melhor usar o método de relaxação.
- Para isso, reorganizamos a equação para ter $$\small\phi(x,y)= \tfrac{1}{4} [ \phi(x+a,y) + \phi(x-a,y) + \phi(x,y+a) + \phi(x,y-a)]$$
- Definimos então $\phi=V$ para os pontos no topo da caixa e $\phi=0$ para os restantes lados.
- De seguida adivinhamos valores para os pontos dentro da caixa. Podemos colocá-los todos iguais a 0, podemos escolher aleatoriamente, tanto dá.
- Usamos a equação acima para determinar o potencial em cada ponto. De seguida repetimos o processo, até vermos que quase não há mudança na matriz, ou seja, já resolvemos a equação diferencial.



## 1.2 - Overshoot
- Ao usar o método de Jacobi que vimos atrás, os valores vão lentamente convergindo para os valores reais. 
- Ora, consideremos que num certo exercício, um valor vai de $0.1$ para $0.3$ em 1 iteração e depois converge para $0.5$ mais lentamente. Ora, este processo seria acelerado se fizessemos um *overshoot* e saltássemos logo de $0.1$ para $0.4$.

- Voltemos ao problema da caixa com condições de fronteira bem definidas nas paredes.
- Consideremos que uma certa tentativa para um certo ponto é $\phi(x,y)$ e a tentativa seguinte será $\phi'(x,y)$. Podemos relacioná-las da seguinte forma: $$\phi'(x,y)=\phi(x,y)+\Delta \phi(x,y)$$em que $\Delta \phi(x,y)=\phi'(x,y)-\phi(x,y)$
- Podemos então definir uma outra tentativa que consiste em valor com overshoot, dados por: $$\phi_\omega(x,y)=\phi(x,y)+(1+\omega)\Delta \phi(x,y) \quad;\quad \omega>0$$
- Neste caso ficamos com $\phi_{\omega}(x,y)=(1+\omega)\phi'(x,y)-\omega \phi(x,y)$. A equação completa do potencial num ponto fica: $$\small\phi_\omega(x,y)= \frac{1+\omega}{4} [ \phi(x+a,y) + \phi(x-a,y)+ \phi(x,y+a) + \phi(x,y-a) ]$$
## 1.3 - Gauss-Seidel
- No método de Jacobi e no de Overshoot que temos acima estamos a calcular todos os valores da matriz de novo e depois substituir a matriz por uma nova.
- Ora, no método de Gauss-Seidel presumimos que todos os valores que determinamos serão melhores que os anteriores. Assim, mal determinamos o novo valor de um certo ponto da grelha deitamos o valor antigo fora e ficamos com esse. Na prática, basta usar um único array e apenas fazer overwrite dos valores.
- Para representar isto usamos:
$$\small\phi(x,y)\leftarrow \tfrac{1}{4} [ \phi(x+a,y) + \phi(x-a,y) + \phi(x,y+a) + \phi(x,y-a)]$$
(esta notação usada em CC significa que calculamos o valor da direita e depois ele é usado para substituir o da esquerda)
- Podemos ainda combinar os métodos de Gauss-Seidel e Overshoot e temos:
$$\small\phi(x,y)\leftarrow \frac{1+\omega}{4} [ \phi(x+a,y) + \phi(x-a,y)+ \phi(x,y+a) + \phi(x,y-a) ]$$
- Esta última combinação é mais rápida, em grande parte devido ao overshoot. No entanto, devemos notar que o método de Gauss-Seidel permite usar menos memória porque só temos 1 array
- Além disso, devemos combinar sempre estes 2, porque o método de Overshoot para grelhas quadradas é muito frequentemente *instável* AKA não converge.

### 1.3.1 - Escolher $\omega$
- Depende muito do problema e equações em específico. 
- Quase sempre, este método apenas converge para $\omega<1$. Dentro disso, normalmente maior será melhor, mas apenas até certo ponto.
- Regra geral: quanto maior melhor, mas é uma questão de experimentar.
- Por exemplo, no caso da caixa com condições de Fronteira, $\omega=0.9$ é o melhor valor. No Newman diz que o autor usou este método e o programa demorou 38s, enquanto que com o método de Jacobi demorou 10 minutos.

# 2 - Valores Iniciais
- Estes são problemas em que temos uma equação diferencial e conhecemos os valores iniciais de uma variável. Com estes, pretendemos prever o comportamento da variável para $t>0$.

- Vejamos o exemplo da *equação de difusão em 1D*: $$\frac{\partial\phi}{\partial t}=D \frac{\partial^{2}\phi}{\partial x^{2}} $$
em que $D$ é o coeficiente de Difusão.
- Vemos que temos $\phi$ a depender de 2 variáveis: $x,t$. Ora, poderíamos então pensar que podemos operar da mesma forma que nos problemas de condição de fronteira. Mas não é possível, porque os valor que conhecemos não existem em todo o domínio do tempo, apenas em $t=0$ (em comparação ao exemplo da caixa com o potencial dos lados conhecido, um problema de condições iniciais seria o equivalente a conhecer o potencial de 1 lado apenas).

## 2.1 - FTCS
- AKA **_Forward-time centered-space method_**.
- Começamos por dividir as dimensões espaciais numa grelha. Para o exemplo em estudo (Equação de Difusão 1D) isto significa um linha dividida, com pontos em intervalos de tamanho $a$.
- A segunda derivada de $\phi$ em $x$ será conforme a equação que vimos no capítulo das derivadas:
$$\frac{\partial^{2}\phi}{\partial x^{2}}=\frac{\phi(x+a,t)+\phi(x-a,t)-2\phi(x,t)}{a^{2}}$$
e a equação de difusão passa a ser:
$$\frac{d\phi}{dt}= \frac{D}{a^{2}} [\phi(x+a,t)+\phi(x-a,t)-2\phi(x,t)]$$
- Ora, se pensarmos em cada $\phi(x,t), \phi(x+a,t),\phi(x-a,t)\dots$ como a sua própria variável de tempo, vemos que este problema consiste num sistema de EDO de 1ª ordem.
- Ora, para resolver estas equações usamos o método de Euler. De notar que tanto este método como a equação da 2ª derivada usada têm erros que variam com $h^{2}$, pelo que é inútil usar um método de Runge-Kutta com maior exatidão.
- Assim, recordemos do método de Euler que, para resolver uma eq dif do tipo $\frac{d\phi}{dt}=f(\phi,t)$ fazemos expansão em série de taylor: $\phi(t+h)\simeq \phi(t)+h \frac{d\phi}{dt} =\phi(t)+hf(\phi,t)$. Ou seja, para o exemplo em estudo temos:
$$\phi(x,t+h)=\phi(x,t)+h \tfrac{D}{a^{2}} [ \phi(x+a,t)+\phi(x-a,t)-2\phi(x,t) ]$$
- Ou seja, partindo de $t=0$ conseguimos determinar $\phi(x,t)$ para todos os pontos em todos os instantes. 
- De realçar ainda que, neste exemplo, para os resultados convergirem é necessário que $$h\le \frac{a^{2}}{2D}$$

#computacional #programacao #eqs_difs