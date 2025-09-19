## Determinar derivadas com Chebyshev
- Temos um conjunto de pontos $(i_{0},u_{1},\dots,u_{N})$. Podemos fazer a sua interpolação com Lagrange (como vimos brevemente na aula anterior):
$$p(x) = \sum_{j=0}^{N} u_j \ell_j(x)=\sum\limits_{j=0}^{N}u_{j}\frac{\prod_{k\neq j}(x-x_{k})}{\prod_{k\neq j}(x_{j}-x_{k})}$$
(em que $\ell_{j}(x)$ é o polinómio de Lagrange $j$, sendo que $p$ será a interpolação de polinómios de modo que se passe em $u_{j}$) 

- No entanto, podemos olhar para isto como sendo a representação de um conjunto de pontos $u_{j}$ na *base de polinómios de Lagrange*!. Assim, podemos definir a derivada:
$$p'(x)=p'(x_{j})~\to~D_{ij}=\frac{d}{dx}\left(\sum\limits_{j=0}^{N}u_{j} \frac{x_{i}-x_{k}}{x_{j}-x_{k}}\right)= \begin{cases}
\frac{a_{i}}{a_{j}(x_{i}-x_{j})} & ; & i\neq j \\
\sum\limits_{k\neq j}\frac{1}{x_{i}-x_{j}} & ; & i=j
\end{cases}\quad;\quad a_{j}=\prod_{k\neq j}(x_{j}-x_{k})$$
- Consideremos então pontos escolhidos conforme a quadratura de Gauss: $x_{j}=\cos(\frac{j\pi}{N})$. Assim, na base de polinómios de Chebyshev esta matriz fica:
$$D_N = 
\begin{bmatrix} \begin{array}{@{}c|c|c@{}}
   \frac{2N^2+1}{6} & 2\frac{(-1)^j}{1-x_j} & \frac{1}{2}(-1)^N \\
   \frac{1}{2}\frac{(-1)^i}{1-x_i} & \begin{matrix}
                  &                   & \frac{(-1)^{i+j}}{x_i-x_j} \\
                  &   \frac{-x_j}{2(1-x^2_j)}   &     \\
         \frac{(-1)^{i+j}}{x_i-x_j}  &          &    
           \end{matrix} 
      & \frac{1}{2}\frac{(-1)^{N+i}}{1+x_i}   \\
   -\frac{1}{2}(-1)^N  & -2\frac{(-1)^j}{1+x_j}  & \frac{2N^2+1}{6} \\
\end{array} \end{bmatrix}$$
(PORQUÊ????)

- Assim teremos:
$$D_{N}\cdot u(\mathbf{x})\approx u'(\mathbf{x})\quad;\quad
D_{N}^{2}\cdot u(\mathbf{x})\approx u''(\mathbf{x})$$
ou seja, podemos definir o erro:
$$\varepsilon^{(1)}(x)=D_{N}\cdot u(x)-u'(x) \quad;\quad \varepsilon^{(2)}(x)=D_{N}^{2}\cdot u(x)-u''(x)$$

- Para aplicar isto iremos usar o módulo `chebPy` disponível em `https://github.com/cpraveen/chebpy`. EX de pseudocodigo:
```python
from chebPy import *
from numpy import *

f = lambda x : exp(x)*sin(5*x)

N = 5
D,x = cheb(N) # faz a seleção dos pontos x em [-1,1] e matriz D
u = f(x) # pontos sampled da função
erroD = dot(D,u) - exp(x)*(sin(5*x)+5*cos(5*x))
```
- Há um exemplo no notebook. A partir de $N=10$ já temos bem reduzidos.

## Diferenciação com FFT
- Podemos relacionar 3 séries importantes:
    - Chebyshev, em que $x\in[-1,1]$
    - Fourier, em que $\theta\in\mathbb{R}$
    - Laurent, em que $z\in\text{círculo unitário}$

- Mais concretamente, podemos escrever:
$$x=\text{Re}(z)=\frac{z+z^{-1}}{2}=\cos(\theta)\in[-1,1]$$
em que:
$$T_{n}(x)=\text{Re}(z^{n})=\frac{z^{n}-z^{-n}}{2}=\cos(n\theta)$$

- Como um polinómio de Chebyshev $T_{n}(x)$ é mónico de grau $n$, então podemos escrever um qualquer polinómio como:
$$p(x)=\sum\limits_{n=0}^{N}a_{n}T_{n}(x)~~;~~x\in[-1,1]$$
- Ora, esse polinómio pode ser escrito em expansão com polinómio de Laurent (o polinómio será auto-recíproco, $z^{n}=z^{-n}$):
$$\mathbf{p}(z)=\frac{1}{2}\sum\limits_{n=0}^{N}a_{n}(z^{n}+z^{-n})~~;~~|z|=1$$
e Fourier:
$$P(\theta)=\sum\limits_{n=0}^{N}a_{n}\cos(n\theta)~~;~~\theta\in \mathbb{R}$$
- Ora temos:
$$p(x)=\mathbf{p}(z)=P(\theta)\quad \text{se}\quad x=\text{Re}(z)=\cos(\theta)$$

- Assim, analogamente podemos definir uma função auto-recíproca $\mathbf{f}(z)$ (no círculo unitário) e uma função periódica $F(\theta)$ (em $\mathbb{R}$):
$$f(x)\quad;\quad \mathbf{f}(z)=f(\frac{z+z^{-1}}{2})\quad;\quad F(\theta)=f(\cos(\theta))$$
em que temos os pontos de Interpolação
$$x_{j}=\cos(\theta_{j})=\text{Re}(z_j)\quad;\quad \theta_{j}=j \frac{\pi}{N}\quad;\quad z_{j}=e^{i\theta_{j}}$$
e teremos $p,\mathbf{p},P$ a interpolar $f,\mathbf{f},F$ nestes pontos.

- Tendo em conta isto, vemos que será possível determinar a derivada de um polinómio $p$ usando a sua FFT (usando a ligação a Fourier, não percebi para que serve o Laurent):
### Algoritmo
1.  Obter os pontos de interpolação $(u_{0},u_{1},\dots,u_{N})$ em que $x_{j}=\cos(j\pi/N)$ e aumentá-lo para: $\mathbf{U}=(u_{0},u_{1},\dots,u_{N},u_{N-1},\dots,u_{1})$
2. Fazer FFT de $\mathbf{U}$: $\hat{U}_{k}=\frac{\pi}{N} \sum_{j=1}^{2N}e^{-ik\theta_{j}}U_{j}~,~k=-N+1,\dots,N$ (para obter os k's podes usar a função que fizeste para isso na ficha 3)
3. Calcular $\hat{W}_{k}=ik\hat{U}_{k}$ e tornar $\hat{W}_{N}=0$
4. Fazer FFT inversa: $W_{j}=\frac{1}{2\pi}\sum_{k=-N+1}^{N}e^{ik\theta_{j}}\hat{W}_{k}~~,~~j=1,\dots,2N$
5. E fica:
$$\begin{cases}
w_{j}=\frac{-W_{j}}{\sqrt{1-x_{j}^{2}}} ~~,~~j=1,\dots,N-1\\
w_{0}=\frac{1}{2\pi} \sum\limits_{n=0}^{N}' n^{2}\hat{u}_{n} \\
w_{N}=\frac{1}{2\pi}\sum\limits_{n=0}^{N}' (-1)^{n+1}n^{2}\hat{u}_{n}
\end{cases}$$
(o apóstrofo serve para indicar que nestes somatórios multiplicamos os termos $n=0,N$ por $\frac12$)

- Assim, tendo-se um polinómio $p(x)=\sum_{n=0}^{N}\alpha_{n}T_{n}(x)$ podemos fazer a mudança de variável $x=\cos\theta$ e temos:
$$P(\theta)=\sum\limits_{n=0}^{N} \alpha_{n}\cos(n\theta)$$
 e temos a derivada:
$$\begin{align*}
p'(x)&= \frac{P'(\theta)}{\frac{dx}{d\theta}}=\frac{-\sum_{n=0}^{N}n\alpha_{n}\sin(n\theta)}{-\sin\theta}\\
&= \frac{\sum_{n=0}^{N} n\alpha_{n}\sin(n\theta)}{\sqrt{1-x^{2}}}
\end{align*}$$
Não sei a utilidade desta última parte e o que ela tem a ver com o algoritmo acima

### Código
- Vejamos um pseudo código:
```python
from numpy import *
from numpy.fft import fft, ifft
from chebfftPy import chebfft # módulo no mesmo github que acima

N = 10
f = lambda x: exp(x)*sin(5*x)
xx = linspace(-1,1,100)
ff = f(xx) # valores reais da função

x = cos(arange(0,N+1)*pi/N) # pontos de quadratura gaussiana
f = f(x) # valores reais nos pontos de interpolação
erro = chebfft(f) - exp(x)*(sin(5*x)+5*cos(5*x)) 
```
- Ou seja, só é preciso literalmente espetar os valores da função nos pontos de sample nesta função e ela aplica o algoritmo por nós??? (Verificar se podemos usar este módulo em exame)
- Apenas com $N=20$ ficamos limitados pela precisão do python: $\sim10^{-10}$.

## EXS - Resolver EDOs
### Eq Poisson
- Consideremos a seguinte Eq de Poisson com termo de fonte: $u_{xx}=e^{4x}$, que queremos resolver em $]-1,1[$ com CF Dirichlet $u(\pm1)=0$
- Usamos a matriz derivada na base de Chebyshev: $D_{N}$. Aplicá-mo-la 2 vezes para fazer a segunda derivada. Aplicamos ainda a CF:
```python
N = 16
D,x = cheb(N)
D2 = dot(D,D)
D2 = D2[1:N,1:N] # para poder aplicar CF
f = lambda x : exp(4*x)
y = f(x[1:N]) # termo de fonte nos pontos de interpolação
u = zeros(N+1) # aqui temos a CF
u[1:N] = solve(D2, f) 
```
- A lógica de resolução consiste no mesmo que fizemos no final do resumo de Espectrais 1: transformamos a eq diferencial parcial num problema matricial:
$$u_{xx}=f(x)~~\to~~ D_{N}^{2} \begin{pmatrix}u_{0} \\ u_{1} \\ \vdots \\ u_{N-1} \\ u_{N}\end{pmatrix}= \begin{pmatrix}0 \\ f_{1} \\ \vdots \\ f_{N-1} \\ 0\end{pmatrix}$$
e resolvemos este sistema $D\cdot\mathbf{u}=\mathbf{f}$ em função de $\mathbf{u}$.

### Eq Poisson 2D
- Temos: $u_{xx}+u_{yy}=f(x,y)$ que iremos resolver em $\Omega\in]-1,1[^{2}$ com $f(x,y)=10\sin(8x(y-1))$ com CF Dirichlet nulas.
- Criamos uma grid $(x_{i},y_{j})=(\cos(i\pi/N),\cos(j\pi/N))$
- Podemos transformar este problema num problema matricial $A\cdot\mathbf{u}=\mathbf{f}$ usando a função `kron`, tendo-se:
$$L_{N}=I\otimes D_{N}^{2}+D_{N}^{2}\otimes I$$
tendo-se: `L = np.kron(I,D2) + np.kron(D2,I)`

```python
N = 24 
D,x = cheb(N); y=x # grelha igual em x e y
# pontos interpolação decidem meshgrid feita!
xx, yy = meshgrid(x[1:N],y[1:N]) 
xx = reshape(xx, (N-1)**2) # tornar meshgrid em matriz vetor
yy = reshape(yy, (N-1)**2)
f = 10*sin(8*xx*(yy-1)) # termo fonte 
D2 = dot(D,D)[1:N,1:N]; I = eye(N-1)
L = kron(I,D2) + kron(D2, I)
u = solve(L,f)
uu = zeros((N+1,N+1))
uu[1:N,1:N] = reshape(u, (N-1,N-1))
```

## Importância de usar quadratura gauss
- Nos exemplos todos que vimos desta matéria usamos pontos recolhidos pela equação resultante da quadratura de gauss-lobato: $x_{i}=\cos(i\frac{\pi}{N})$. 
- Pode parecer que era mais "simples" simplesmente escolher pontos distribuidos uniformemente. Vamos ver o que aconteceu num exemplo random:
![[download.svg]]
deu asneira! Vemos que, numa função que vai de 0 a 1, o erro máximo obtido foi 5 com pontos uniformamente distribuídos. Com pontos de chebyshev/gauss temos erro de 0.01.

## Eq Poisson em 2D com FFT
- Vejamos um pouco melhor o caso do último exemplo.
- Temos a equação de Poisson 2D:
$$\nabla^{2}\phi(x,y)=f(x,y)\quad;\quad (x,y)\in[0,L_{x}]\times[0,L_{y}]$$
com as CF:
$$\begin{align*}
\phi(x,0)&= \phi(x,L_{x})~~,~~x\in[0,L_{x}]\\
\frac{\partial\phi}{\partial x}(x,0)&= \frac{\partial\phi}{\partial x}(x,L_{x})~~,~~x\in[0,L_{x}]\\
\phi(x,0)&= \phi(x,L_{y})~~,~~x\in[0,L_{y}]\\
\frac{\partial\phi}{\partial y}(x,0)&= \frac{\partial\phi}{\partial y}(x,L_{y})~~,~~x\in[0,L_{y}]
\end{align*}$$
(basicamente, CFs periódicas!)

- Podemos expandir $\phi$ em Fourier:
$$\phi(x,y)=\sum\limits_{p,q=-\infty}^{\infty}\hat{\phi}_{pq}\exp\left(-2\pi p\frac{x}{L_{x}}\right)\exp\left(-2\pi q\frac{y}{L_{y}}\right)$$
e podemos fazer a mesma expansão para $f(x,y)$. Temos então os coeficientes $\hat{\phi}_{pq}~,~\hat{f}_{pq}$. 
- Substituindo as expansões na Eq de Poisson os exponenciais cortam e fica:
$$\left[\left(-i2\pi \frac{p}{L_{x}}\right)^{2}+\left[- i2\pi \frac{q}{L_{y}} \right]^{2} \right]\hat{\phi}_{pq}=\hat{f}_{pq}$$
ou seja, apenas queremos determinar os coeficientes de $\phi$!

- Tendo-se $x:x_{m}=m\Delta x~,~m=0,1,\dots,M$ e $y:y_{n}=n\Delta y~,~n=0,1,\dots,N$. A expansão truncada fica:
$$\phi_{mn}=\sum\limits_{p=0}^{M}\sum\limits_{q=0}^{N}\hat{\phi}_{pq}\exp \left(-i2\pi p \frac{m \Delta x}{L_{x}} \right)\exp \left(-i2\pi q \frac{n \Delta y}{L_{y}} \right)$$
$$f_{mn}=\sum\limits_{p=0}^{M}\sum\limits_{q=0}^{N}\hat{f}_{mn}\exp \left(-i2\pi p\frac{m\Delta x}{L_{x}} \right)\exp \left(-i2\pi q \frac{n\Delta y}{L_{y}} \right)$$
e torna-se natural definir $\Delta x=L_{x}/M~,~\Delta y=L_{y}/N$. Vemos ainda que estas 2 expansões não passam de DFTs!

### Algoritmo
1. Amostrar $f$ em $(m\Delta x,n\Delta y)$, obtendo-se $f_{mn}$
2. Fazer DFT de $f_{mn}$, obtendo-se $\hat{f}_{pq}$
3. **Dividir** $\hat{f}_{pq}$ por $\left[\left(-i2\pi \frac{p}{L_{x}}\right)^{2}+\left[- i2\pi \frac{q}{L_{y}} \right]^{2} \right]$ (Sim é assim tão direto!)
4. Fazer IDFT para obter $\hat{\phi}_{pq}$

*Um detalhe*
- O único problema deste método de operação é que não podemos usá-lo no ponto $p=q=0$ (ficamos com divisão por zero). 
- Ora, tendo a Eq Poisson com CF periódicas, conseguimos resolver sempre esta equação a menos de uma constante aditiva (se $\psi$ é solução, $\psi+c$ também será). Assim, se conseguirmos fixar $c$ eliminá-mos a ambiguidade causada por não podermos determinar $\hat{\phi}_{00}$. Temos então 2 opções boas para fixar $c$:
$$\int_{0}^{L_{x}}\int_{0}^{L_{y}}\phi(x,y)dxdy=0 \quad;\quad \int_{0}^{L_{x}}\int_{0}^{L_{y}}f(x,y)dxdy=0$$

- No notebook `FFT-Poisson2` tem um exemplo de resolução da Eq Poisson 2D, mas nunca se chega a usar esta cena de determinar o $c$?