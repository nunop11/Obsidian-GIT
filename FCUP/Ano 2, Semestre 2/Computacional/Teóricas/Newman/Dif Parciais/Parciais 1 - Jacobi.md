
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

#computacional #programacao #eqs_difs 