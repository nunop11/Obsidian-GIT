## VS Diferenças Finitas
- Podemos escrever a equação de onda 2D como:
$$\frac{\partial^{2}u}{\partial t^{2}}= c^{2} \left(\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}\right)+s$$
- Vimos como resolver isto com diferenças finitas (no capítulo de ftcs e cenas).
- Mas podemos ver como resolver isto com o método espectral. Podemos considerar:
$$\mathcal{F}[u]=\sum_{k} \hat{u}_{k}e^{-ik_{x}x}e^{-ik_{y}y}$$
e temos:
$$\frac{\partial^{2}u}{\partial t^{2}}=\mathcal{F}^{-1}[-k^{2}_{x} \mathcal{F}[y]] + \mathcal{F}^{-1}[-k_{y}^{2} \mathcal{F}[u]]$$
- No notebook 4 de ME temos a resolução da eq onda para condições iniciais `ricker`, tendo-se:
![[somas vs espectral.png]]
Não entendi nada do código usado, mas supostamente temos um método de Fourier pseudo-espectral.

- Aqui notasse algo importante: métodos de diferenças finitas têm uma tendência a ter uma decente/alta *dispersão numérica*. O método de Fourier têm bastante menos.
    - Na imagem acima isto é óbvio. Na imagem de diferenças fintias temos dispersão anisotrópica, com precisão máxima para $\theta=\frac{\pi}{4}$
    - A imagem de Fourier não tem dispersão nem comportamento anisotrópico.



## Eq Onda 1D 2ª ordem com Chebyshev
- Nem vou escrever nada rn. Vais ter que ver o livro de ME :D

## Eq Onda 2D 2ª ordem com FFT
- Nem vou escrever nada again

## Eq Onda Elástica em 1D
- A eq onda elástica em 1D é:
$$\rho(x)\frac{\partial^{2}u(x,t)}{\partial^{2}t}=\frac{\partial}{\partial x} \left(\mu(x) \frac{\partial u(x,t)}{\partial x} \right) + f(x,t)$$
- Determinamos a 2ª derivada temporal com diferenças finitas de 3 pontos:
$$\rho_{i} \frac{u_{i}^{j+1}-2u_{i}^{j}+u_{i}^{j-1}}{dt^{2}}=\frac{\partial}{\partial x} \left(\mu(x) \frac{\partial u(x,t)}{\partial x} \right)_{i}^{j} + f_{i}^{j}$$
- Como vimos atrás, temos a matriz de diferenciação de Chebyshev:
$$D_{ij} =
  \begin{cases}
    -\frac{2 N^2 + 1}{6} \;\; \;\;  \text{para}\;\;  i  = j = N\\
    -\frac{1}{2} \frac{x_i}{1-x_i^2} \;\; \;\;  \text{para}\;\; i = j = 1,2,\ldots,N-1\\
    \frac{c_i}{c_j} \frac{(-1)^{i+j}}{x_i - x_j} \;\; \;\;  \text{para} \;\; i \neq j = 0,1,\ldots,N
  \end{cases} \quad;\quad \begin{matrix}c_{i}=2  & ; & i=0~\text{ou}~i=N \\ c_{i}=1 & ; & \text{resto}\end{matrix}$$
  em que temos $N+1$ pontos de Chebyshev $x_{i}=\cos(i\pi/N)~,~i=0,\dots,N$.

- Como também já vimos, podemso escrever: $$\partial_{x}u_{i}=D_{ij}u_{j}~~\to~~\partial_{x}u=D \cdot \mathbf{u}$$
E acho que é só usar isto para resolver a equação como já vimos uma série de vezes????? 