cw# Equações Diferenciais de Derivadas Parciais
- Equações do tipo $$a \frac{\partial u}{\partial y}+b\frac{\partial u}{\partial x}+c \frac{\partial^{2} u}{\partial x^{2}}+d \frac{\partial^{2} u}{\partial y^{2}}+eu=0$$
- Consistem em secções cónicas (?)
- Temos vários tipos:
    - *Elípticas* 
        - Equações de Poisson/Laplace
        - $\nabla^{2}u=f(x,y,\dots)$
    - *Parabólicas*
        - Equação de Calor e equação de Difusão
        - $\frac{\partial u}{\partial t}=\alpha\left(\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{3} u}{\partial y^{2}}\right)$
    - *Hiperbólicas*
        - Equação de Onda
        - $\frac{\partial^{2}u}{\partial t^{2}}=v^{2}\frac{\partial^{2}u}{\partial x^{2}}$

## Resolução - 1
- Temos a equação de Poisson/Laplace em 1D:
$$\frac{\partial^{2}u}{\partial x^{2}}=f(x)$$
- Começamso por dividir o intervalo em que vamos resolver a equação. Uma forma conveniente de fazer isto é dividir o intervalo de xx em intervalos iguais de tamanho $\Delta x$
- Assim, podemos definir $x_{i}=i\Delta x$

- Podemos definir:
$$\frac{\partial^{2}u}{\partial x^{2}}=\frac{u_{i-1}-2u_{i}+u_{i+1}}{(\Delta x)^{2}}+\mathcal{O}(\Delta x^{2})$$
Que podemos ver como uma "média" entre o ponto presente, o ponto anterior e o seguinte.
- Temos então
$$u_{i-1}-2u_{i}+u_{i+1}=\frac{\partial^{2}u}{\partial x^{2}}|_{x_{i}}\Delta x^{2}=f(x_{i})\Delta x^{2}$$
- Com isto, podemos obter $N$ (??? - verificar isto) equações acopladas.

- De notar que, em 2D teríamos:
$$\frac{u_{i+1,j}-2u_{i,j}+u_{i-1,j}}{\Delta x^{2}}+\frac{u_{i,j+1}-2u_{i,j}+u_{i,j-1}}{\Delta y}=f_{i,j}$$
que podemos ver como uma média entre o ponto presente, o acima, o abaixo, o à esquerda e o à direita.

### Condições de Fronteira
- Por exemplo, para $f(x)=ax+b$ temos $f'(x)=a$. Logo perdemos $b$. Assim, precisamos de *condições de fronteira* para poder obter esta informação em falta.
- Ora, precisamos de $N$ condições para uma EDDP de ordem $N$.
- Ora, nas equações de Poisson/Laplace conhecemos o valor da 2ª derivada do potencial: $\nabla^{2}u=f$. Assim, precisamos de 2 condições de Fronteira
- Para resolver a equação em 1D, usamos $i=1,\dots,N-1$ em que $i=0,N$ temos as condições de Fronteira

#### Tipos 
**Dirichlet**
- Quando sabemos o valor da função em alguns pontos: $$\alpha_{j}u(x_{j})=C_{i,j}$$

**Neumann**
- Conhecemos o fluxo da função: $$\beta_{j}\frac{\partial u}{\partial \hat{n}}(x_{j})=C_{2,j}$$

**Robin ou mistas**
- Mistura das 2 acima:
$$\alpha_{j}u(x_{j})+\beta \frac{\partial u}{\partial \hat{n}}(x_{j})=C_{3,j}$$

## Resolução - 2
- Queremos então resolver um sistema de equações acopladas.
- Poderíamos usar métodos como eliminação gaussiana. Mas para obter um bom resultado teremos de usar muitos pontos, pelo que estes métodos são demasiado lentos.
- Ora, poderíamos até usar `np.linalg.solve()`. 
    - Mas consideremos que, num problema 2D, dividimos tanto xx e yy em $10^{5}$ pontos. Assim, teríamos $10^{10}$ pontos na grelha. Ou seja, temos $10^{10}$ equações. 
    - Ora, mesmo este programa do numpy escala com $\propto N^{3}$. 
    - Se 1 equação demora $1\text{ms}=10^{-3}\text{s}$ a ser resolvidaentão este sistema iria demorar $10^{-3}(10^{10})^{3}=10^{27}\text{s}$, que é um tempo absurdo.

### Métodos Iterativos
- Estes métodos permitem-nos, de forma gradual, resolver uma equação diferencial destas. Por ser iterativo e não resolver as equações diretamente 1 a 1, este método é mais rápido que os falados acima.
- Iremos indicar um índice extra (além de $i,j$): $n$ que indica a presente iteração:
$$\frac{u_{i+1,j}^{n}-2u_{i,j}^{n}+u_{i-1,j}^{n}}{\Delta x^{2}}+\frac{u_{i,j+1}^{2}-2u_{i,j}^{n}+u_{i,j-1}^{n}}{\Delta y}=f_{i,j}^{n}$$
e temos:
$$\begin{align*}
(u_{i+1,j}^{n}-2u_{i,j}^{n}+u_{i-1,j}^{n})\Delta y^{2} + (u_{i,j+1}^{n}-2u_{i,j}^{n}+u_{i,j-1}^{n})\Delta x^{2}&= f_{i,h}^{n}\Delta x^{2} \Delta y^{2}
\end{align*}$$
e no caso em que $\Delta x=\Delta y=h$ temos>
$$u_{i,j}= \frac{u_{i+1,j}^{n}+u_{i-1,j}^{n}+u_{i,j+1}^{n}+u_{i,j-1}^{n}}{4}- f_{i,j}^{n}h^{2}$$

em 1D:
$$u_{i}^{n+1}= \frac{u_{i+1}^{n}+u_{i-1}^{n}}{2}- f_{i}^{n}h^{2}$$

#### Exemplo - Dirichlet
- Consideremos um problema dividido em 4 pontos. Temos as condições de fronteira:
    - $u_{0}=A$
    - $u_{3}=B$

- Temos então o sistema:
$$\begin{cases}
u_{0}=A \\
u_{1}=\frac{u_{0}+u_{2}}{2}+f_{1}h^{2} \\
u_{1}=\frac{u_{1}+u_{3}}{2}+f_{2}h^{2} \\
u_{3}=B
\end{cases}\to\begin{cases}
-2u_{1}+u_{2}=f_{1}h^{2}-u_{0} \\
u_{1}-2u_{2}=f_{2}h^{2}-u_{3}
\end{cases}\to A \vec{u}=\vec{b}$$
e temos:
$$\begin{pmatrix}-2 & 1\\1 & -2\end{pmatrix}\begin{pmatrix}u_{1}\\u_{2}\end{pmatrix}=\begin{pmatrix}f_{1}\\f_{2}\end{pmatrix}h^{2}-\begin{pmatrix}u_{0}\\u_{3}\end{pmatrix}$$

- Ora, vejamos como podemos obter o vetor $\vec{u}$:
---- caderno ----
- Ora, $\vec{u}$ tem que ser um vetor coluna e $\vec{b}$ um vetor linha.
- E das 2 uma: podemos incluir os valores da fronteira no vetor $\vec{u}$ ou não. A coisa mais genérica e talvez "correta" a fazer é incluir esses pontos.
    - Mas se tivermos a resolver limites de fronteira de *dirichlet* é mais prático **não** incluir estes pontos. Isto porque os seus valores são conhecidos e, como tal, em cada iteração eles seriam alterados e teríamos que estar a ir repor os valores na iteração seguinte.
    - Outra coisa a notar é que a informação contida nestes pontos é passada para o sistema através do vetor $\vec{b}$.

### $u(i,j)\to u_{k}$
---- caderno ----
- Temos então:
$$u(i,j)=u_{k}~~;~~k = jN_{x}+i$$
- Ou seja:
    - $u_{i,j\pm1}\to k'=jN_{x}+i\pm N_{x}\to k'= k\pm N_{x}$
    - $u_{i\pm1,j}\to k'=jN_{x}+i\pm1\to k'\pm1$

- E temos então (grelha com $N_{x}=6, N_{y}=5$):
$$u(i,j)= \frac{u(i+1,j)+u(-1,j)+u(i,j+1)+u(i,j-1)}{4}- f(i,j)h^{2}$$
logo:
$$\begin{align*}
u(2,2)&= \frac{u(3,2)+u(1,2)+u(2,3)+u(2,1)}{4}+f(2,2)h^{2}\\
u_{14}&= \frac{u_{15}+u_{13}+u_{20}+u_{8}}{4}+f_{14}h^{2}
\end{align*}$$

## Resolução - 3
- Usando as equações que fomos vendo acima, obtemos $u^{n+1}(i,j)~\forall i,j$. Assim, no fim de uma interação podemos medir a variação relativamente À iteração anterior de alguma forma e decidir se paramos ou não (pode ser o erro total dos pontos, o erro médio, etc)

## Métodos
### Método Jacobi
- Tendo a matriz $A$ podemos decompô-la em $A=L+D+U$ em que $Dq$ é diagonal, $L$ triangular inferior e $U$ triangular superior ($D,U$ têm a diagonal principal =0)
- Como $A\vec{u}=\vec{b}$  temos $(D+L+U)\vec{u}=\vec{b}$ donde $D\vec{u}=-(L+U)\vec{u}+\vec{b}$. Supondo que $D^{-1}$ existe e é dada por:
$$ D^{-1} = \begin{bmatrix} \frac{1}{a_{11}} & 0 & \cdots &  0 \\ 0 & \frac{1}{a_{22}} & \cdots &  0\\ \vdots & \vdots &\ddots & \vdots \\ 0 & 0 &\cdots & \frac{1}{a_{NN}} \end{bmatrix}$$
 temos $$\vec{u}=-D^{-1}(L+U)\vec{u}+D^{-1}\vec{b}$$
 E usando o método de Jacobi podemos atualizar  então ser escrita na forma matricial como: $$ \vec{u}^{m+1}=-D^{-1}(L+U)\vec{u}^{m}+D^{-1}\vec{b}$$
 Como as matrizes têm coeficientes constantes, podemos definir $T\equiv -D^{-1}(L+U)$ e a temos: $\vec{u}^{m+1}= T\vec{u}^{m}+D^{-1}\vec{b}$. (Se as condições fronteira forem de Dirichelet, $\vec{b}$ é constante e podemos também definir um $\vec{c} \equiv D^{-1}\vec{b}$, vindo $\vec{u}^{m+1}= T\vec{u}^{m}+ \vec{c}$)

- Ou seja, numa forma mais prática, podemos simplesmente fazer:
$$\begin{align}
    u_{k}^{n+1} &= \frac{1}{a_{kk}}\left[ b_k - \sum_{\substack{l=1 \\ j\neq i}}^{N} a_{kl}u_l^{n} \right]\\
    u_{k}^{n+1} &= u_{k}^{n} + \delta u_{k}^{n}\\
    \delta u_k &=\frac{1}{a_{kk}} \left[b_k-\sum^{N}_{l=1}a_{kl}u^m_l\right],\ k=1,2,\dots,N,\ l=0,1,\dots
\end{align}$$
podemos verificar a 1ª equação ao imaginar a matriz $A$ que vai ter 5 diagonais em 2D. Teremos sempre equações do tipo: $u_{14}= \frac{u_{15}+u_{13}+u_{20}+u_{8}}{4}+f_{14}h^{2}$

#### Aplicação
- Na aula o professor fez:
$$u_{ij}^{n+1}=\frac{\frac{u_{i,j+1}^{n}+u_{i,j-1}^{n}}{\Delta x^{2}}+\frac{u_{i+1,j}^{n}+u_{i-1,j}^{n}}{\Delta y^{2}}+f_{i,j}}{\frac{2}{\Delta x^{2}}+\frac{2}{\Delta y^{2}}}$$
![[Attachments/FCUP/A3S2/MCE/codigo jacobi.png]]
dividimos por $\Delta x,\Delta y$ porque os índices vão (por exemplo) de 0 a 100 mas representam valores de 0 a 1.

- Ou podemos fazer isto de forma vetorizada (mais rápido):
![[codigo jacobi vec.png]]
em que somamos os blocos de matrizes internas "correspondentes" a $i+1,j~~;~~i-1,j~~;\dots$

### Método Gauss Seidel
- Este método baseia-se no facto que algumas matrizes, em cada iteração, aproximam-se da solução, *de forma global*. Isto é o caso das matrizes de coeficientes da eq de Laplace/Poisson.
- Temos então:
$$\begin{align}
u_{k}^{n+1} =& \frac{1}{a_{kk}}\left[ b_k - \sum_{l=1}^{k-1} a_{kl}u_l^{n+1} - \sum_{l=k+1}^{N} a_{kl}u_l^{n}\right]\\
=&u_{k}^{n} + \frac{1}{a_{kk}}\left[ b_k - \sum_{l=1}^{k-1} a_{kl}u_l^{n+1} - \sum_{l=k}^{N} a_{kl}u_l^{n}\right]\\
=&u_{k}^{n} + \delta_{k}^{n}
\end{align}
$$
ou seja, usamos os valores obtidos numa iteração nela própria.
- Em forma matricial temos:
$$(D+L)\vec{u}^{m+1}= -U\vec{u}^{m}+ \vec{b}$$ ou
$$ \vec{u}^{m+1}=-(D+L)^{-1}U\vec{u}^{m}+ (D+L)^{-1}\vec{b}$$

#### Aplicação
- Fazemos basicamente o mesmo que na de Jacobi mas invés de guardar as atualizações e os valores atuais em arrays separados, guardamos tudo no mesmo.

### Método SOR (SObreRelaxação)
- Este método consiste em ampliar a correção $\delta_{k}^{n}$ por um fator racional $\omega$. A lógica é que, se em cada iteração nos aproximamos, ao acrescentar o fator $\omega$ iremos acelerar o processo.
- Podemos ainda usar um fator $\omega<1$ para abrandar -- aí usamos o nome de *sub-relaxações sucessivas*
- Se $\omega=1$ temos Gauss-Seidel e se $\omega=0$ temos Jacobi. Não sei pq mas confia
- O valor ótimo de $\omega$ depende da equação a resolver e da geometria do problema. Normalmente a melhor maneira de o obter é por tentativa e erro.
- Temos:
$$ \begin{align}
u_{k}^{n+1}=& (1-\omega) u_{k}^{n} + \omega \delta_{k}^{n} \tag{3.7}\\
=& (1-\omega) u_{k}^{n} + \frac{\omega}{a_{kk}}\left[ b_k - \sum_{l=1}^{k-1} a_{kl}u_l^{n+1} - \sum_{l=k}^{N} a_{kl}u_l^{n}\right]\\
u_{k}^{n+1}=&(1-\omega)u_{k}^{n} + \frac{\omega}{a_{kk}}\left[ b_k - \sum_{l=1}^{k-1} a_{kl}u_l^{n+1} - \sum_{l=k+1}^{N} a_{kl}u_l^{n}\right]
\end{align}
$$
Para a forma matricial fazemos:
$$(D+ \omega L)\vec{u}= \omega\vec{b} - \left[ \omega U + (\omega -1)D \right]\vec{u}$$
pelo que a iteração se pode escrever como:
$$\vec{u}^{m+1}=-(D+ \omega L)^{-1}\Big(\omega\vec{b} - \big[ \omega U + (\omega -1)D \big]\vec{u}^{m} \Big)$$
No entanto, tendo em conta que $(D+\omega L)$ é triangular, os elementos de $\vec{u}^{m+1}$ podem ser calculados sequencialmente por substituição para à frente
$$u_i^{k + 1} = ( 1 − \omega ) u_i^{k} + \frac{\omega}{a_{ii}}\Big(b_i -\sum_{j<i} a_{ij}u_j^{k+1} - \sum_{j>i} a_{ij}u_j^{k} \Big) ,\qquad i = 1,2 \ldots , N $$

#### Aplicação
- No caso das equações de Poisson/Laplace a matriz dos coeficientes tem a maioria dos elementos nula, então é mais útil usar diretamente a equação da 2ªa derivada. Definimos: $R_{k}=u^{m+1}_{k-1}+u^{m+1}_{k+1}+u^{m}_{k-n_x}+u^{m}_{k+n_x}-4u^{m}_{k}-h^2\cdot f_{k}$ e podemos escrever
$$u_{k}^{m+1}=u_{k}^m+\frac{\omega}{4}R_{k}$$

#### $\omega$ ótimo
- Para um problema com geometria retangular com $n_{x}+1,n_{y}+1$ pontos com espaçamento igual $\Delta x=\Delta y=h$ temos:
$$\omega=\frac{2}{1+\sqrt{1-\rho^{2}}}\quad\quad;\quad\quad \rho=\frac{1}{2}\left[\cos\left(\frac{\pi}{n_{x}}\right) +\cos\left(\frac{\pi}{n_{y}}\right)\right]$$
- Para um domínio não retangular de área $A$ usamos a estimativa de Garabedian:
$$\omega=\frac{2}{1+\frac{3.014h}{\sqrt{A}}}$$


### Red & Black
![[red & black.png]]
- Facilmente vemos que se um ponto for vermelho, apenas usamos pontos pretos na sua atualização e vice-versa.
- Ora, temos então que os pontos vermelhos para atualizar não dependem de outros vermelhos e igualmente para pontos pretos.
- Assim, usando numpy podemos atualizar todos os pontos vermelhos de 1 vez e depois os pretos e assim adiante.
- Além disso, podemos verificar que os pontos vermelhos se encontram nos índices $k$ pares (começando com $k=0$ no canto superior esquerdo)

#### Aplicação
Ex Código:
```
# Pseudo-código para red-black
# solução inicial u
u = np.array[...];
for k in range(len(numIterations)):
    # pontos vermelhos
    for j in enumerate(y[1:-1]):
        for i = in enumerate(x[1:-1]):
            if (mod((i + j)% 2) == 0)
                u[i, j] = 1/4 * (u[i - 1, j] + u[i + 1, j] + u[i, j - 1] + u[i, j + 1] + h**2*f[i, j])
    # pontos  pretos
    for j in enumerate(y[1:-1]):
        for i = in enumerate(x[1:-1]):
            if (mod((i + j)% 2) == 1)
                u[i, j] = 1/4 * (u[i - 1, j] + u[i + 1, j] + u[i, j - 1] + u[i, j + 1] + h**2*f[i, j])
```

## Aplicar Neumann
- Se tivermos uma caixa metálica oca no interior, teremos sempre potencial constante e campo nulo. Ou seja, temos condições de fronteira de Dirichlet
----- caderno ----
- Consideremos agora que 1 das paredes da caixa é um dielétrico. Teremos agora condição de fronteira de Neumann nessa parede. 
- Conforme a figura, teremos a condição (campo elétrico nulo na superfície) $$\frac{\partial V}{(-)\partial y}=0$$
em que o menos (-) é essencial se tivermos fronteira de Robin, mas não faz muita diferença de Neumann.

- Queremos então ver como podemos tornar isto numa equação discreta, de forma a obter sistemas semelhantes àqueles de Dirichlet.
- Simplesmente usamos a equação:
$$\frac{\partial u}{\partial y}=\frac{du_{i,0}}{dy}=\frac{u_{i,-1}-u_{i,1}}{2\Delta y}=0$$
em que usamos as derivadas ao centro!
- De notar, claro, que os pontos $u_{i,-1}$ são "nodos fantasma". Eles não existem mas usá-mo-lo para computar a derivada.
 
- Neste caso específico resulta:
$$u_{i,-1}=u_{i,1}$$
e agora simplesmente incluimos isto na equação d-7e00}$:
$$\begin{align*}
u_{i,1}+u_{i,-1}+u_{i-1,0}+u_{i+1,0}&= f_{i,0}h\\
2u_{i,1}+u_{i-1,0}+u_{i+1,0}&= f_{i,0}h
\end{align*}$$
- No caso genérico de $\beta\frac{\partial u}{\partial y}=u$ temos
$$\frac{\partial u}{\partial y}=\beta~~\to~~u_{i,-1}=\frac{1}{\beta}u_{i,1} + \frac{2}{\beta}C\Delta y~~\to~~\left(1+ \frac{1}{\beta}\right)u_{i,1}+u_{i-1,0}+u_{i+1,0}=f_{i,0}h- \frac{2}{\beta} C\Delta y$$
que resulta em
$$\left(1+ \frac{1}{\beta}\right)u_{i,1}+u_{i-1,0}+u_{i+1,0}=f_{i,0}h- \frac{2}{\beta} C\Delta y$$