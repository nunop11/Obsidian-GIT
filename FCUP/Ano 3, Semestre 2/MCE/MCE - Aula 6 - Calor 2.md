- Na aula anterior vimos os métodos Euler para Trás, que é explicito logo mais fácil. Mas também é mais instável.
- Vimos ainda Euler para a frente que é implícito, lgoo temos que resolver um sistema de equações ligadas que tem que ser resolvido. Assim, este método é mais difícil e trabalhoso computacionalmente, mas é bastante mais estável.
- Vimos ainda o método CN que é o mais trabalhoso mas mais estável e melhor.

# ---2D---
- Até agora só vimos 1D
- Ora, em 1D obtinhamos $A$ a ser uma matriz tridiagonal, o que nos facilitava a vida.
- Em 2D temos $A$ a ser uma *matriz diagonal* por bandas, com diagonais distânciadas de $N_{x}$

# ADI - Alternating Direction Implicit (Direções Alternadas Implícitas)
- Este método consiste em usar Crank Nicholson e Euler para Trás de forma alternada:
![[ADIfig1.png|315]]

- Basicamente dividimos o problema assim:
---------- caderno ---------------
(o esquema acima também pode ajudar)

- Ou seja, temos uma grelha com $J$ pontos na direção $x$, $I$ na direção $y$ e $N$ na direção $t$. Temos $x_{j},y_{i},t_{n}$. E podemos definir:
$$\Delta t=\frac{T}{N-1}~~;~~\Delta x=\frac{L_{x}}{J-1}~~;~~\Delta y=\frac{L_{y}}{I-1}$$

- A equação de calor neste sistema fica na forma:
![[ADI eq1.png]]

- Podemos juntar os índices todos num só ($k=j+iJ$):
![[ADI eq2.png]]
isto funciona como o caso de Poisson matricial.

- Ou seja, dividimos a equação assim:
![[ADI eqs.png|514]]
em que a parte azul é *explícita* e portanto a primeira a calcular. De seguinda, usando estes pontos, calculamos a parte a vermelho que é *implícita*. 

- Para o método éxplícito usamos a fórmula de 2ª derivada normal. Para implícito fazemos a mesma fórmula, mas no tempo futuro $n+ \frac{1}{2}$
- Nos pontos nas CF (de Neumann ou Robin, Dirichlet não importa) usamos o método associado à direção perpendicular a esse lado (no lado de cima usamos o método de para yy)

## Casos simétricos
- Se num certo problema a CF for simétrica, então a solução será simétrica segundo o eixo de simetria da CF.
- Assim, podemos dividir o problema a meio e resolver apenas 1 dos lados, tendo-se $\partial_{n}u=0$ no eixo de simetria.

# Schrödinger
- Temos a eq Schrödinger *dependente* do tempo:
$$i\hbar \frac{\partial \psi}{\partial t}=\frac{-\hbar^{2}}{2m}(\nabla^{2}\psi+V\psi)$$

- Podemos resolver esta equação da mesma forma que fizemos até, como por exemplo com Crank-Nicholson
- MAS temos que considerar o facto que a solução $\psi$ representa uma grandeza física, sendo $|\psi|^{2}$ uma distribuição de probabilidade.
- Como tal, temos que ter normalização
