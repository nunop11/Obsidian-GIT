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
