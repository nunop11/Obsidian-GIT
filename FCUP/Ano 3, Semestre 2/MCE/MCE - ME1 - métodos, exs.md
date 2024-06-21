# Eq Derivadas Parciais
- Consideremos uma PDE genérica com as seguintes condições de fronteira:
$$\begin{align*}
Lu(\vec{x})&= s(\vec{x})&&;\quad \vec{x}\in U\subset \mathbb{R}^{d}\\
Bu(y)&= 0 &&;\quad \vec{y}\in \partial U
\end{align*}$$
- Ora, a equação solução $\bar u$ desta PDE será aquela que satisfaz a 2ª equação e que torna *pequeno* o resíduo:
$$R=L \bar u-s$$
- Mas surge a questão: o que é um "pequeno" neste caso? Usamos então o **método de resíduos pesados**:
    - Procuramos soluções num subespaço de dimensão $\mathcal{P}_{N}<\infty$ de um espaço de Hillbert, normalmente do espaço $L^{2}$
    - As funções base do subespaço $\mathcal{P}_{N}$ são $(\phi_{0},\dots,\phi_N)$ a que chamaremos *funções tentativa*.
    - Podemos expandir $\bar u$ em termos das funções tentativa: $\bar u(\vec{x})=\sum_{n=0}^{N}\tilde u_{n}\phi_{n}(\vec{x})$
    - Podemos deifnir as *funções de teste* $\chi_{n}$ que nos permitem definir a pequenez do resíduo $R$, usando o produto escalar: $(\chi_{n},R)=0$ $\leftarrow$ **Condição de Pequenez**

**Métodos Numéricos**
- Temos então alguns métodos numérios que podemos usar para determinar as funções tentativa:
    - *Diferença Finita* : consideramos polinómios de baixa ordem em regiões infinitesimais, com sobreposição. Isto é o que fazemos ao aproximar $u'_{i}=\frac{u_{i+1}-u_{i}}{\Delta x}$, em que o erro de truncagem corresponde a todos os termos de ordem 2+
    - *Elemento Finito* : consideramos funções suaves em regiões pequenas. Estes métodos dividem um objeto em imensas partes menores, os elementos finitos.
    - *Método Espectral* : aproximamos a solução com funções suaves que cobrem todo o dominio. 

## Tipos de Métodos Espectrais
- Desde já: em métodos espectrais as funções $\phi_{n}$ são uma base completa de funções globais suaves.
- Conforme as funções de teste, temos estes métodos:
    - **Galerkin** - As funções de teste são iguais às tentativa: $\phi_{n}=\chi_{n}$. Cada $\phi_{n}$ satisfaz a condição de fronteira
    - **Tau** -  As funções de teste são iguais às tentativa: $\phi_{n}=\chi_{n}$. As $\phi_{n}$ não satisfazem a condição de fronteira, tendo-se equações extra para isso
    - **Colocação / Pseudo-Espectral** - As funções de teste são deltas de Dirac $\chi_{n}=\delta(\vec{x}-\vec{x}_{n})$, colocadas em pontos especiais: pontos de colocação $\vec{x}_{n}$

## Galerkin
- Como $\chi_{n}=\phi_{n}$, podemos escrever (para $n\in \{0,\dots,N\}$):
$$\begin{align*}
(\chi_{n},R)=0~~~~\longrightarrow~~(\phi_{n},R)&= 0\\
(\phi_{n},L\bar u-s)&= 0\\
\left(\phi_{n},L\sum_{k=0}^{N} \tilde u_{k}\phi_{k}\right)-(\phi_{n},s)&= 0\\
\sum\limits_{k=0}^{N}\tilde u_{k}(\phi_{n},L\phi_{k})&= (\phi_{n},s)\\
\sum\limits_{k=0}^{N}L_{nk}\tilde u_{k}&= (\phi_{n},s)
\end{align*}$$
em que se definiu a matriz $L_{nk}=(\phi_{n},L\phi_{k})$
- Assim, resolvendo o sistema acima conseguimos obter os $N+1$ coeficientes $\tilde u_{k}$ e portanto temos $\bar u$

## Tau
- Novamente consideramos $\chi_{n}=\phi_{n}$, mas agora as funções tentativa não chegam para garantir as CF e portanto se fizermos como em Galerkin a solução estará errada.
- Consideremos uma base ortonormada $g_{p}$ com $p\in\{0,\dots,M+1\}~,~M+1<N+1$ na fronteira $\partial U$. Podemos escrever: $$B\phi_{n}(\vec{y})=\sum\limits_{p=0}^{M} b_{pn}g_{p}(\vec{y})$$
e da 2ª equação desta aula resulta:
$$B u(\vec{y})=0~~\to~~\sum\limits_{k=0}^{N}\sum\limits_{p=0}^{M}\tilde u_{k}b_{pk}g_{p}(\vec{y})=0$$
e daqui temos então estas $M+1$ equações $$\sum\limits_{k=0}^{N}b_{pk}\tilde u_{k}=0~~~~,~~ 0\le p\le M$$
- Assim, neste método o sistema que permite obter os  $N+1$ coeficientes $\tilde u_{k}$ consiste em:
$$\begin{cases}
\sum\limits_{k=0}^{N}L_{nk}\tilde u_{k}=(\phi_{n},s) & ; & 0\le n\le N-M-1 \\ \\
\sum\limits_{k=0}^{N}b_{pk}\tilde u_{k}=0 & ; & 0\le p\le M
\end{cases}$$
e a solução $\bar(\vec{x})=\sum_{k=0}^{N}\tilde u_{k}\phi_{k}$ deste sistema obedece à seguinte equação:
$$L\bar u(\vec{x})=s(\vec{x}) + \sum\limits_{p=0}^{M}\tau_{p}\phi_{[N-M+p]}(\vec{x})$$

## Pseudospectral / Colocação
- Temos $\chi_{n}=\delta(\vec{x}-\vec{x}_{n})$. A condição de pequenez fica:
$$\begin{align*}
(\chi_{n},R)&= 0\\
(\delta(\vec{x}-\vec{x}_{n}),R)&= 0\\
R(\vec{x_{n}})&= 0\\
L u(\vec{x}_{n})&= s(\vec{x}_{n})\\
\sum\limits_{k=0}^{N}L \phi_{k}(\vec{x}_{n})\tilde u_{k}&= s(\vec{x}_{n})
\end{align*}$$
- Impomos a CF da mesma forma que no método Tau. temos o sistema:
$$\begin{cases}
\sum\limits_{k=0}^{N}L\phi_{k}(\vec{x}_{n})\tilde u_{k}=s(\vec{x}_{n}) & ; & 0\le n\le N-M-1 \\ \\
\sum\limits_{k=0}^{N}b_{pk}\tilde u_{k}=0 & ; & 0\le p\le M
\end{cases}$$

## Mas que função tentativa escolher
- Naturalmente surge esta questão. Os métodos acima parecem fazer sentido e tudo, mas são inúteis se não soubermos que funções são $\phi_{n}$.
- Ora:
    - *Problemas Periódicos* - Polinómios trigonométricos AKA séries de Fourier
    - *Problemas Não Periódicos* - Polinómios ortogonais

# Expansões de Legendre e Chebyshev
![[polinomios.png|450]]
- Estas são 2 famílias de polinómios ortogonais, que podemos definir em 1D como:
    - **Legendre** $$\begin{align*}
\int_{-1}^{1}P_{m}(x)P_{n}(x)dx=\frac{2}{2n+1}\delta_{mn}~~~~~~~~\\P_{0}(x)=1~~,~~P_{1}(x)=x~~,~~P_{2}(x)=\frac{3}{2}x^{2}- \frac{1}{2}
\end{align*}$$
    - **Chebyshev**$$\begin{align*}
\int_{-1}^{1}T_{m}(x)T_{n}(x)\frac{dx}{\sqrt{1-x^{2}}}=\frac{\pi}{2}(1+\delta_{0n})\delta_{mn}\\
T_{0}(x)=1~~,~~T_{1}(x)=x~~,~~T_{2}(x)=2x^{2}-1
\end{align*}$$

## Propriedades de Chebyshev
- Temos que$$T_{n}(\cos\theta)=\cos(n\theta)$$
- Podemos escrever estes polinómios como uma relação de recorrência: $T_{n+1}(x)=2xT_{n}(x)-T_{n-1}(x)$
- São funções próprias do problema de Sturm-Liouville: $\frac{d}{dx} \left( \sqrt{1-x^2}\frac{dT_n}{dx} \right)= -\frac{n^2}{\sqrt{1-x^2}}T_n(x)$
- Formam uma base do espaço de Hillbert $L^{2}[-1,1]$ com a função de peso:
$$w(x)=\frac{1}{\sqrt{1-x^{2}}}$$

## Interpolação polinomial
- Consideremos $N+1$ nodos $x_{i}$ ($0\le i\le N$) com $x_{i}\in[-1,1]$.
- Podemos definir a *interpolação de Lagrange* de uma função $u(x)$:
$$I_{N}u(x)=\sum\limits_{i=0}^{N}u(x_{i})\prod\limits_{\substack{j=0\\j\neq i}}^{N}\frac{x-x_{i}}{x_{i}-x_{j}}$$
Ora, segundo o teorema de Cauchy, existirá um $x_{0}\in[-1,1]$ que minimizará a diferença $u(x)-I_{N}u(x)=\frac{1}{(N+1)!}u^{(N+1)}(x_{0})\prod_{i=0}^{N}(x-x_{i})$. Não entendi de onde veio o lado direito da equação.
- Ou seja, usando a equação acima podemos interpolar uma série de dados de forma polinomial, determinando $u(x)$ para qualquer ponto $x\in[-1,1]$.

## Interpolação de Chebyshev
- Acima, ao dizer que existirá um $x_{0}$ que minimiza a diferença $u(x)-I_{N}u(x)$, podemos tirar outra conclusão: esse $x_{0}$ também irá minimizar o produtório do lado da direita da equação: $\prod_{i=0}^{N}(x-x_{i})$
- Ora, vemos que este produto será um polinómio de grau $N+1$, em que o termo de potência $N+1$ terá coeficiente $1$: $x^{N+1}+a_{N}x^{N}+\dots+a_{1}x+a_{0}$. A isto chamamos um polinómio *mónico*.

- Ora, podemos definir polinómios de Chebyshev como:
    - De todos os polinómios mónicos de grau $n$, o único que tem o menor máximo em $[-1,1]$ será o n-ésimo polinómio de Chebyshev dividido por $2^{n-1}$: $T_{n}(x)/2^{n-1}$.

- Conforme esta informação, consideremos que os $x_{i}$ nodos são os $N+1$ zeros do polinómio de Chebyshev $T_{N+1}(x)$.
- Daqui de alguma forma resulta:
$$\prod\limits_{i=0}^{N}(x-x_{i})=\frac{1}{2^{N}}T_{N+1}(x)$$
de onde vem (???):
$$x_{i}=-\cos \left(\frac{2i+1}{2(N+1)}\pi \right)~~~~,~~0\le i\le N$$

## Expansões Espectrais
### Coeficientes contínuos exatos
- Do ponto de vista puramente teórico.
- Como vimos acima, podemos escrever uma função como uma expansão de funções tentativa $\phi_{n}\in L^{2}$. 
- Se estas funções $\phi_{n}$ forem polinómios ortogonais $\phi_{n}$ com função de peso $w(x)$, então a representação espectral de uma função $u(x)$ será simplesmente a sua *projeção* no subespaço de polinómios de ordem de 0 a N:
$$P_{N}u(x)=\sum\limits_{n=0}^{N}\tilde u_{n}\phi_{n}(x)$$
em que definimos
$$\tilde u_{n}=\frac{(\phi_{n},u)}{(\phi_{n},\phi_{m})} \quad \quad;\quad \quad (\phi_{n},u)=\int_{-1}^{1}\phi_{n}(x)u(x)w(x)dx$$
- No entanto, apesar de isto ser muito bonito não podemos calcular o integral do produto escalar com exatidão :(

### Coeficientes Discretos
- Vejamos então a 2ª melhor opção: fazer o integral atrás por integração gaussiana / quadratura gaussiana. Temos:
$$\int_{-1}^{1}f(x)w(x)dx=\sum\limits_{i=0}^{N}w_{i}f(x_{i})$$
em que os nodos $x_{i}$ são os zeros do polinómio $\phi_{N+1}$ (de ordem $N+1$) e os coeficientes $w_i$ são as soluções do seguinte sistema linear:
$$\sum\limits_{j=0}^{N}x_{j}^{i}w_{j}=\int_{-1}^{1}x^{i}w(x)dx$$
- O somatório da fórmula acima é exato para polinómios $f(x)$ de grau $\le 2N+1$
- Para incluir as condições de fronteira $[-1,1]$ simplesmente fazemos $x_{0}=-1,x_{N}=1$

- Integração *Gauss-Lobato*: consideramos $x_i$ os zeros do polinómio $P=\phi_{N+1}+\lambda \phi_{N}+\mu \phi_{N-1}$ com $\lambda,\mu$ tais que $P(-1)=P(1)=0$. Isto será exato para qualquer polinómio $f(x)$ de grau $\le 2N-1$
- Assim, podemos definir os coeficientes $\hat{u_{n}}$ como sendo a aproximação de Gauss Lobato do integral $\int_{-1}^{1}f(x)w(x)dx$, tendo-se:
$$\hat{u}_{n}=\frac{1}{(\phi_{n},\phi_{n})}\sum\limits_{i=0}^{N}w_{i}\phi_{n}(x_{i})u(x_{i})$$
e temos então:
$$I_{N}u(x)=\sum\limits_{i=0}^{N}\hat{u}_{n}\phi_{n}(x)$$
(temos isto invés da projeção $P_{N}$ de $u$)
- Se $\phi_{n}$ forem polinómios de Chebyshev tenão $\hat{u}_{n}$ podem ser calculados com a FFT (??????)

### Erro de Aliasing
- Consideremos $I_{N}u(x)$ o polinómio de interpolação de $u$, obtido usando $N+1$ nodos $x_{i}$ com quadratura Gauss-Lobato. Ou seja: $I_{N}u(x_{i})=u(x_{i})$
- Já para a projeção $P_{N}u$, não podemos garantir que ela passa em $x_{i}$, já que eles não entram na determinação da projeção.
- A diferença entre $I_{N}u,P_{N}u$ é chamada de *erro de aliasing*. Isto pode ser interpretado como os coeficientes $\hat{u}_{n}$ serem perturbados pelas altas frequências de $\tilde u_{k}$ quando $k>N$.

### Convergências
- Consideremos $u$ tal que as derivadas até grau $m$ sejam suaves. Dito isto, abaixo $u^{(m)}$ é a m-ésima derivada de $u$.
#### Legendre
**Erro de Truncagem**
$$\begin{align*}
\|P_{N}u-u\|_{L^{2}}&\le \frac{C}{N^{m}}\sum\limits_{k=0}^{m}\|u^{(k)}\|_{L^{2}}\\
\|P_{N}u-u\|_{\infty}&\le \frac{C}{N^{m-\frac12}}V(u^{(m)})
\end{align*}$$
**Erro de Interpolação**
$$\|I_{N}u-u\|_{L^{2}}\le \frac{C}{N^{m-\frac12}}\sum\limits_{k=0}^{m} \|u^{(k)}\|_{L^{2}}$$

#### Chebyshev
**Erro de Truncagem**
$$\begin{align*}
\|P_{N}u-u\|_{L_{w}^{2}}&\le \frac{C}{N^{m}}\sum\limits_{k=0}^{m}\|u^{(k)}\|_{L_{w}^{2}}\\
\|P_{N}u-u\|_{\infty}&\le \frac{C(1+\ln N)}{N^{m}}\sum\limits_{k=0}^{m}\|u^{(k)}\|_{\infty}
\end{align*}$$
**Erro de Interpolação**
$$\begin{align*}
\|I_{N}u-u\|_{L_{w}^{2}}&\le \frac{C}{N^{m}}\sum\limits_{k=0}^{m}\|u^{(k)}\|_{L_{w}^{2}}\\
\|I_{N}u-u\|_{\infty}&\le \frac{C}{N^{m}}\sum\limits_{k=0}^{m}\|u^{(k)}\|_{\infty}
\end{align*}$$

### Erro Evanescente
- Num método de diferenças finitas de ordem $k$ o erro cai com $1/N^{k}$. 
- De alguma forma as expressões de erro da interpolação de Legendre ou Chebyshev mostram que o erro cai de forma exponencial!

## EXEMPLO (ALELUIA ALGO CONCRETO)
- Consideremos a ED linear de 2ª ordem:
$$\partial_{x}^{2}u-4\partial_{x}u+4u=e^{x}+C~~~~,~~ x\in[-1,1]$$
com CF Dirichlet: $u(-1)=0~,~u(1)=0$. Temos ainda $C=\frac{-4e}{1+e^{2}}$

- A solução exata é:
$$u(x)=e^{x}-\frac{\sinh1}{\sinh2}e^{2x}+ \frac{C}{4}$$
(Tal como faziamos em computacional podemos converter qq domínimo $\xi\in[a,b]$ em $x\in[-1,1]$ usando: $x=(\xi - \frac{a+b}{2})(\frac{2}{b-a})$)

#### Chebyshev
- Vamos ver como podemos resolver esta equação com o método espectral de chebyshev.
- Vamos determinar uma solução da equação usando os 5 primeiros polinómios de chebyshev: $T_{0}(x),T_{1}(x),T_{2}(x),T_{3}(x),T_{4}(x)$. Nas equações acima: $N=4$

- Começamos por expandir o termo de fonte:
$$s(x)=e^{x}+C~~\to~~ P_{4}s(x)=\sum\limits_{n=0}^{4}\tilde s_{n}T_{n}(x) \quad ;\quad I_{4}s(x)=\sum\limits_{n=0}^{4}\hat{s}_{n}T_{n}(x)$$
com
$$\tilde s_{n}=\frac{2}{\pi(1+\delta_{0n})}\int_{-1}^{1}T_{n}(x)s(x)\frac{dx}{\sqrt{1-x^{2}}} \quad;\quad \hat{s}_{n}=\frac{2}{\pi(1+\delta_{0n})}\sum\limits_{i=0}^{4}w_{i}T_{n}(x_{i})s(x_{i})$$
- Acima vimos que como a função peso dos polinómios de chebyshev é $w(x)=\frac{1}{\sqrt{1-x^{2}}}$ então temos: $x_{i}=-\cos \left(\frac{2i+1}{2(N+1)}\pi \right)$. Assim, neste problema, temos os $N+1$ nodos:
$$x_{i}=\cos\left(i \frac{\pi}{4}\right)~,~0\le i\le 4~~~~\to~~~~ \{x_{i}\}=\left\{-1, -\frac{1}{\sqrt{2}}, 0, \frac{1}{\sqrt{2}},1 \right\}$$
- Daqui, como conhecemos os polinómios, $x_{i}$ e os pesos, podemos calcular:
$$ \hat{s}_0 = -0.03004 \;\;\; \hat{s}_1 = 1.130 \;\;\;\hat{s}_2 = 0.2715 \;\;\;\hat{s}_3 = 0.04488 \;\;\;\hat{s}_4 = 0.005474$$
Por seu lado os erros de truncagem e de aliasing (são iguais um ao outro) são:
$$ \hat{s}_n -\tilde{s}_n =  2.0\times 10^{-7}; \;\;\;3.2\times 10^{-6}; \;\;\;4.5\times 10^{-5}; \;\;\;5.4\times 10^{-4}; \;\;\;1.0\times 10^{-12}$$

- Assim, já que obtivemos estes valores a expandir $s$ em $T_{i}$, podemos escrever isto na forma matricial:
$$\tilde s=\begin{pmatrix}-0.03004 \\ 1.130 \\ 0.2715 \\ 0.04488 \\ 0.005474\end{pmatrix}$$

#### Matriz de Operadores diferenciais
- Lamento muito, mas isto vai-me ser mais fácil de explicar com notação de MQ1. Podemos escrever a matriz de um opedor numa base $\psi$ como:
$$A = \begin{pmatrix}A_{00} & A_{01} & \cdots \\ A_{10} & A_{11} & \cdots \\ \vdots & \vdots & \ddots\end{pmatrix} \quad;\quad A_{ij}=\langle\psi_{i}|A|\psi_{j}\rangle=(\ket{\psi_{i}}, A\ket{\psi_{j}})$$
(tendo-se então o produto escalar de $\ket{\psi_{i}}$ com $A\ket{\psi_{j}}$)

- Ora, para resolver equações diferenciais nesta UC temos algo parecido a isto. A base **ortonormada** que temos aqui é a de polinómios de Chebyshev. Mais concretamente, temos os 5 primeiros polinómios:
$$\begin{align*}
T_{0}(x)=1 \quad ;\quad T_{1}(x)=x \quad;\quad T_{2}(x)=2x^{2}-1\\
T_{3}(x)=4x^{3}-3x \quad;\quad T_{4}(x)=8x^{4}-8x^{2}+1
\end{align*}$$
tendo-se então matrizes de operadores $5\times5$.
- Consideremos então o operador *1ª derivada* (em $x$): $D$.
- Podemos definir as derivadas dos 5 polinómios de Chebyshev:
$$\begin{align*}
DT_{0}&= 0\\
DT_{1}&= 1=T_{0}\\
DT_{2}&= 4x=4 T_{1}\\
DT_{3}&= 12x^{2}-3=12x^{2}-6+3=6T_{2}+3T_{0}\\
DT_{4}&= 32x^{3}-16x=32x^{3}-24x+8x=8T_{3}+8T_{1}
\end{align*}$$
ou seja, podemos escrever todas as derivadas em função de outras funções da base.
- Assim, podemos definir os elementos relevantes da matriz:
$$\begin{align*}
A_{01}&= \langle T_{0}|D|T_{1}\rangle=\langle T_{0}|T_{0}\rangle=1\\
A_{12}&= \langle T_{1}|D|T_{2}\rangle=\langle T_{1}|(4T_{1})\rangle=4\langle T_{1}|T_{1}\rangle=4\\
A_{03}&= \langle T_{0}|D|T_{3}\rangle=\langle T_{0}|(6T_{2}+3T_{0})\rangle=6\langle T_{0}|T_{2}\rangle + 3\langle T_{0}|T_{0}\rangle=0+3=3\\
A_{23}&= \langle T_{2}|D|T_{3}\rangle=\langle T_{2}|(6T_{2}+3T_{0})\rangle=6\\
A_{14}&= \langle T_{1}|D|T_{4}\rangle=\langle T_{1}|(8T_{3}+8T_{1})\rangle= 8\langle T_{1}|T_{3}\rangle + 8\langle T_{1}|T_{1}\rangle=0+8=8\\
A_{34}&= \langle T_{3}|D|T_{4}\rangle=\langle T_{3}|(8T_{3}+8T_{1})\rangle=8
\end{align*}$$
todos os outros elementos são nulos, pois $\langle T_{i}|T_{j}\rangle=\delta_{ij}~,~\langle T_{i}|0\rangle=0$.
- Temos então:
$$D = \begin{pmatrix}0 & 1 & 0 & 3 & 0 \\ 0 & 0 & 4 & 0 & 8 \\ 0 & 0 & 0 & 6 & 0 \\ 0 & 0 & 0 & 0 & 8 \\ 0 & 0 & 0 & 0 & 0\end{pmatrix}$$

- Temos ainda o operador *2ª derivada*: $D_{2}$. Temos:
$$\begin{align*}
D_{2}T_{0}&= 0\\
D_{2}T_{1}&= 0 \\
D_{2}T_{2}&= 4=4T_{0}\\
D_{2}T_{3}&= 24x=24T_{1}\\
D_{2}T_{4}&= 96x^{2}-16=96x^{2}-48+32=48T_{2}+32T_{0}
\end{align*}$$
- Procedendo da mesma forma que fizemos atrás:
$$\begin{align*}
A_{02}&= \langle T_{0}|D_{2}|T_{2}\rangle=\langle T_{0}|(4T_{0})\rangle=4\\
A_{13}&= \langle T_{1}|D_{2}|T_{3}\rangle=\langle T_{1}|(24T_{1})\rangle=24\\
A_{04}&= \langle T_{0}|D_{2}|T_{4}\rangle=\langle T_{0}|(48T_{2}+32T_{0})\rangle=32\\
A_{24}&= \langle T_{2}|D_{2}|T_{4}\rangle=\langle T_{2}|(48T_{2}+32T_{0})\rangle=48
\end{align*}$$
(todos os outros elementos são nulos porque $\langle T_{i}|T_{j}\rangle=\delta_{ij}~,~\langle T_{i}|0\rangle=0$)
e podemos obter:
$$D_{2}=\begin{pmatrix}0 & 0  & 4 & 0 & 32\\ 0 & 0 &0 & 24 & 0 \\ 0 & 0 & 0  & 0 & 48\\ 0 & 0 & 0 & 0  & 0 \\0 & 0 & 0 &  0 & 0\end{pmatrix}$$
- Como esta equação diferencial consiste em $\partial_{x}^{2}-4\partial_{x}+4$ então a matriz que descreve o operador diferencial da direita é $A=D-4D_{2}+4I$, tendo-se:
$$A=\begin{pmatrix}4 & -4 & 4 & 12 & 32 \\ 0 & 4 & -16 & 24 & -32 \\ 0 & 0 & 4 & -24 & 48 \\ 0 & 0 & 0 & 4 & -32 \\ 0 & 0 & 0 & 0 & 4\end{pmatrix}$$


#### Resolução
- Ora, no início do exemplo vimos como representar o termo de fonte, $s$ como uma expansão de $T_{i}$. E vimos como determinar o operador diferencial, $A$, do lado esquerdo da esquação. 
- Ou seja, estamos quase a poder escrevê-la como: $Lu=s$. Quem diria, voltamos ao início desta aula.
- Vamos ver como resolver com os 3 métodos vistos no início da aula.

##### Resolução - GALERKIN
- Consideremos a base de Galerkin:
$$\begin{align*}
\phi_{0}(x)&= T_{2}(x)-T_{0}(x)=2x^{2}-2\\
\phi_{1}(x)&= T_{2}(x)-T_{1}(x)=4x^{2}-4x\\
\phi_{3}(x)&= T_{4}(x)-T_{0}(x)=8x^{4}-8x^{2}
\end{align*}$$
sendo que todas as funções cumprem a CF: $\phi_{i}(-1)=\phi_{i}(1)=0$; tal como tem de acontecer na base de Galerkin.
- Temos então que passar da base de Chebyshev para a de Galerkin:
$$\phi_{i}(x)=\sum\limits_{k=0}^{4}\tilde \phi_{ki}T_{k}(x)$$
tendo-se a matriz de transformação:
$$\tilde \phi_{ki}=\begin{matrix}\begin{pmatrix}-1 & 0 & -1 \\ 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix} & \begin{matrix}\to T_{0} \\ \to T_{1} \\ \to T_{2} \\ \to T_{3} \\ \to T_{4}\end{matrix} \\ \begin{matrix}\downarrow & \downarrow & \downarrow \\ \phi_{0} & \phi_{1} & \phi_{2}\end{matrix}\end{matrix}$$
((não sei deduzir isto sem perder 3h, mas com as setas dá para ter uma ideia. Simplesmente temos uma representação da definição feita acima: $\phi_{0}=1\cdot T_{2}+ (-1)\cdot T_{0}$))

- Daqui podemos escrever $$u(x)=\sum\limits_{k=0}^{4}\tilde u_{k}T_{k}(x)=\sum\limits_{i=0}^{2}\tilde{\tilde{\phi}}_{i}\phi_{i}(x)$$ (sim, representamos os coeficientes de Galerkin com 2 tils)
- Podemos fazer a conversão entre estas bases com:
$$\tilde{\mathbf{u}}=\tilde\phi \times \tilde{\tilde{\mathbf{u}}}$$
(todos em forma matricial)

**Sistema de Galerkin**
- Como vimos atrás, neste método temos $\chi_{n}=\phi_{n}$.
- Vimos acima que a condição de pequenez / condição para termos um resíduo muito reduzido é:
$$\sum\limits_{j=0}^{N}(\phi_{i},L\phi_{j})\tilde{\tilde{u}}_{j}= (\phi_{i},s)$$
e temos:
$$\begin{align*}
(\phi_{i},L\phi_{j})&= \sum\limits_{k=0}^{4}\sum\limits_{l=0}^{4}(\tilde u_{ki}T_{k},L\tilde \phi_{lj}T_{l})=\sum\limits_{k=0}^{4}\sum\limits_{l=0}^{4}\tilde\phi_{ki}\tilde\phi_{lj}(T_{k},LT_{l})\\
&= \sum\limits_{k=0}^{4}\sum\limits_{l=0}^{4}\tilde\phi_{ki}\tilde\phi_{lj} \left(T_{k},\sum\limits_{m=0}^{4}A_{ml}T_{m} \right)\\
&= \sum\limits_{k=0}^{4}\sum\limits_{l=0}^{4}\tilde\phi_{ki}\tilde\phi_{lj}\sum\limits_{m=0}^{4}A_{ml}(T_{k},T_{m})\\
&= \sum\limits_{k=0}^{4}\sum\limits_{l=0}^{4}\tilde\phi_{ki}\tilde\phi_{lj} \frac{\pi}{2}(1+\delta_{0k})A_{kl}=\frac{\pi}{2}\sum\limits_{k=0}^{4}\sum\limits_{l=0}^{4}(1+\delta_{0k})\tilde\phi_{ki}A_{kl}\tilde\phi_{lj}
\end{align*}$$
e podemos definir:
$$Q = [(1+\delta_{0k})\tilde \phi_{ki}]^{T}=\begin{pmatrix}-2 & 0 & 1 & 0 & 0 \\ 0 & -1 & 0 & 1 & 0 \\ -2 & 0 & 0 & 0 & 1\end{pmatrix}$$
- Assim, como foi referido atrás, minimizar o resíduo consiste em resolver o sistema abaixo:
$$\mathbf{Q}\times \mathbf{A} \times \tilde \phi \times \tilde{\tilde{\mathbf{u}}}=\mathbf{Q}\times \tilde{\mathbf{s}}$$
em que $\tilde{\tilde{\mathbf{u}}}=(\tilde{\tilde{u}}_{0},\tilde{\tilde{u}}_{1},\tilde{\tilde{u}}_{2})$ é a solução a resolver, já que todas as outras matrizes foram descobertas acima.

- E obtemos a solução:
$$\tilde{\tilde{u}}_{0}=-0.1596\quad;\quad \tilde{\tilde{u}}_{1}=-0.09176\quad;\quad \tilde{\tilde{u}}_{2}=-0.02949$$
- Fazendo o produto matricial à esquerda por $\tilde\phi$ obtemos:
$$\tilde{u}_0 = 0.1891 \;\; \tilde{u}_1 = 0.09176 \;\;\tilde{u}_2 = -0.1596 \;\;\tilde{u}_3 = -0.09176 \;\;\tilde{u}_4 = -0.02949 \notag$$
e temos então a solução da equação diferencial em função dos 5 primeiros polinómios de Chebyshev.

##### Resolução - TAU
- Simplesmente temos $\phi_{i}=T_{i}$
- Para os polinómios de Chebyshev temos: $T_{n}(\cos\theta)=(\cos\theta)^{n}$ logo $T_{n}(-1)=(-1)^{n}~,~T_{n}(1)=1$. Assim, o operador que garante $u(-1)=u(1)=0$ é:
$$b_{pk}=\begin{pmatrix}1 & -1 & 1 & -1 & 1 \\ 1 & 1 & 1 & 1 & 1\end{pmatrix}$$
(não percebi como se obtem esta matriz)
- Assim, fazendo aquela coisa de substituir as 2 ultimas linhas da matriz $A$ pela condição de fronteira, o sistema do método de Tau fica:
$$\begin{pmatrix}4 & -4 & 4 & 12 & 32 \\ 0 & 4 & -16 & 24 & -32 \\ 0 & 0 & 4 & -24 & 48 \\ 1 & -1 & 1 & -1 & 1 \\ 1 & 1 & 1 & 1 & 1 \end{pmatrix}\begin{pmatrix}\tilde{u}_{0} \\ \tilde{u}_{1} \\ \tilde{u}_{2} \\ \tilde{u}_{3} \\ \tilde{u}_{4}\end{pmatrix}=\begin{pmatrix}\hat{s}_{0} \\ \hat{s}_{1} \\ \hat{s_{2}} \\ 0 \\ 0\end{pmatrix}$$
e obtemos:
$$\tilde{u}_0 = 0.1456 \;\; \tilde{u}_1 = 0.07885 \;\;\tilde{u}_2 = -0.1220 \;\;\tilde{u}_3 = -0.07885 \;\;\tilde{u}_4 = -0.02360$$

##### Resolução - PSEUDO-ESPECTRAL
- Novamente temos $\phi_{i}=T_{i}$, mas agora as funções de teste são $\delta(x-x_{n})$
- Conforme vimos no início da aula, o sistema deste método é:
$$\begin{align*}
\sum\limits_{k=0}^{4}L \phi_{k}(\vec{x}_{n})\tilde u_{k}= s(\vec{x}_{n})~~\to \sum\limits_{k=0}^{4}LT_{k}(x_{n})\tilde u_{k}&= s(x_{n})\\
\sum\limits_{k=0}^{4}\sum\limits_{l=0}^{4}A_{lk}T_{l}(x_{n})\tilde u_{k}&= s(x_{n})
\end{align*}$$
que em forma matricial fica:
$$\mathbf{T}\times\mathbf{A}\times\tilde{\mathbf{u}}=\mathbf{s}$$
em que:
$$\mathbf{T}=T_{nl}=T_{l}(x_{n})= \begin{pmatrix}1 & -1  & 1 & -1 & 1 \\1 & -1/\sqrt{2} & 0 & 1/\sqrt{2} & -1 \\1 & 0 & -1 & 0 & 1 \\1  & 1/\sqrt{2} & 0 & -1/\sqrt{2} &  -1 \\1  &  1 &  1 &  1 &  1\end{pmatrix}$$
(isto é obtido diretamente de calcular $T_{0},T_{1},T_{2},T_{3},T_{4}$ em $x_{i}=\{-1,\frac{-1}{\sqrt{2}},0,\frac{1}{\sqrt{2}},1\}$)

- Por alguma razão, invés de aplicar as CF nas últimas 2 linhas da matriz $\mathbf{T}\times\mathbf{A}$ o professor colocou $b_{0k}$ na primeira e $b_{1k}$ na última, tendo-se o sistema deste método:
$$\begin{pmatrix}1 & -1& 1& -1& 1 \\4 & 6.82843 & 15.3137 & -26.1421 & 28 \\4 & -4 & 9 & 12 & -12 \\
4  & -1.17157 &  -7.31371 & 2.14214 &  28 \\1  &  1 &  1 &  1 &  1\end{pmatrix}\begin{pmatrix}\tilde{u}_0 \\ \tilde{u}_1 \\ \tilde{u}_2 \\ \tilde{u}_3 \\\tilde{u}_4\end{pmatrix}=\begin{pmatrix}0 \\ \hat{s}_{1} \\ \hat{s}_{2}\\ \hat{s}_{3}  \\ 0\end{pmatrix}$$
e obtemos:
$$ \tilde{u}_0 = 0.1875 \;\; \tilde{u}_1 = 0.08867 \;\;\tilde{u}_2 = -0.1565 \;\;\tilde{u}_3 = -0.08867 \;\;\tilde{u}_4 = -0.03104$$
