    # 1 - Equação do Calor
## 1.2 - Dedução 1
### Calor
- Podemos escrever a energia calorífica de um corpo como $Q=cmu$ com $c$ um calor específico, $u$ a temperatura e $m$ a massa.
- O calor específico tem unidades $[c]=L^{2}T^{-2}\Theta^{-1}$ e é a energia necessária para elevar a temperatura de um corpo em 1 grau (Kelvin)

### Lei de Fourier
- Temos
$$\begin{align*}
\frac{\text{Taxa de transferência de calor}}{Área}=- K_{0} \frac{\partial u}{\partial x}
\end{align*}$$
em que $[K_{0}]~=MLT^{-3}\Theta^{-1}$ é a *condutividade térmica* e $u$ é a **_Temperatura_**
- Por análise dimensional vemos que o fluxo de calor numa área $A$ num intervalo $\Delta t$ será: $$\text{Fluxo Calor}=\phi=-A \Delta tK_{0}\frac{\partial u}{\partial x}$$

### Conservação de Energia
- Se considerarmos uma barra de comprimento $l$ ($x\in[0,l]$) de secção transversal $A$. Consideremos que ela é **uniforme**: a densidade, calor específico, condutividade e área trasversal são constantes em toda a barra.
- Consideremos que a sua temperatura não é uniforme, sendo que apenas as extremidades podem estar expostas ao ambiente. Tendo uma tira infinitesimal entre $x$ e $x+dx$, a energia calorífica aí será:
$$q=c \times \rho A\Delta x \times u(x,t)$$
- Ora, por conservação de energia, a variação de energia térmica será igual ao calor que entra à esquerda é igual àquele que entra à direita + aquele  que é emitido. 

**EQUAÇÃO DO CALOR**
- Podemos escrever:
$$\begin{align*}\\
\Delta q&= \phi_{esquerda}+\phi_{direita}\\
c \rho A \Delta x u(x,t+\Delta t) -c \rho A \Delta x u(x,t) &= \Delta t A \Big(-K_0 \frac{\partial u}{\partial x} \Big)_x-\Delta t A \Big(-K_0 \frac{\partial u}{\partial x} \Big)_{x+\Delta x}\\
c\rho \Delta x [u(x,t+\Delta t)-u(x,t)]&= -\Delta t K_{0} \left[\frac{\partial u}{\partial x}|_{x} - \frac{\partial u}{\partial x}|_{x+\Delta x} \right]\\
\frac{u(x,t+\Delta t)-u(x,t)}{\Delta t}&= \frac{K_{0}}{c\rho}\left(\frac{\frac{\partial u}{\partial x}|_{x+\Delta x} - \frac{\partial u}{\partial x}|_{x}}{\Delta x}\right)
\end{align*}$$
que, no limite $\Delta x,\Delta t\to0$ nos dá a ==__Equação de Calor__==:
$$\frac{\partial u}{\partial t}=\kappa \frac{\partial^{2}u}{\partial x^{2}}~~~~;~~~~ \kappa=\frac{K_{0}}{c\rho}$$
em que $\kappa$ é a *difusividade térmica*, com dimensões $[\kappa]=L^{2}T^{-1}$
- De notar que esta equação descreve a forma como a temperatura varia ao longo do tempo num certo material. Ou seja, as equações de Poisson/Laplace não passam da equação do calor *estacionário* (em termos matemáticos ofc)

### Informação Necessária
Sendo esta uma equação diferencial, precisamos de alguma informação para a resolver:
    - Condição inicial (CI) : estado do sistema quando $t=0$
    - Condições de fronteira (CF) : pontos do sistema em que conhecemos o comportamento da temperatura ao longo do tempo. Tal como tínhamos para a equação de Poisson temos:
        - Condições de Dirichlet: $u(0,t)=u_{1}(t)$
        - Condições de Neumann: $-K_{0} \frac{\partial u}{\partial x}(0,t)=\phi_{1}(t)$
        - Condições de Robin: misturam as duas acima.

## 1.2 - Adimensionalizar
- As variáveis que entram nesta EDDP tem diferentes dimensões. Além disso, o facto de termos variáveis com grandezas reais podem fazer com que surjam valores muito elevados, o que com python nunca é ideal.
- Assim definimos tempo, distância e temperatura caraterísticos $\overline{L},\overline{T},\overline{\Theta}$. Com estes, podemos adimensionalizar as variáveis mais básicas deste sistema:
$$\hat{x}=\frac{l}{\overline{L}}~~;~~\hat{t}=\frac{t}{\overline{T}}~~;~~ \hat{u}(\hat{x},\hat{t})=\frac{u(x,t)}{\overline{\Theta}}~~;~~ \hat{f}(\hat{x})=\frac{f(x)}{\overline{\Theta}}$$
    - Por exemplo, para uma barra como vista acima de comprimento $\ell$, devemos definir $\overline{L}=\ell$ e ficamos com $\hat{x}$ entre 0 e 1.

- Vejamos as restantes grandezas. Por chain rule temos:
$$\begin{align*}
  \partial_{t}u & = \frac{\partial u}{\partial t} = \bar{\Theta}\frac{\partial \hat{u}}{\partial \hat{t}} \frac{\partial \hat{t}}{\partial t} = \frac{\bar{\Theta}}{\bar{T}}\frac{\partial \hat{u}}{\partial \hat{t}}\\
  \partial_{x}u & = \frac{\partial u}{\partial x} = \bar{L}\frac{\partial \hat{u}}{\partial \hat{x}}\frac{\partial \hat{x}}{\partial x} = \frac{\bar{\Theta}}{\bar{L}}\frac{\partial \hat{u}}{\partial \hat{x}}\\
  \partial_{x}^{2}u & = \frac{\bar{\Theta}}{\bar{L}^2}\frac{\partial^2 \hat{u}}{\partial \hat{x}^2},
  \end{align*}$$
(sendo $\partial_{i}^{n}u$ a $n$-derivada de $u$ segundo $i$)

- Se substituirmos na equação do calor 1D temos:
$$\frac{\partial \hat{u}}{\partial \hat{t}}=\frac{\overline{T}\kappa}{\overline{L}^{2}}\frac{\partial^{2} \hat{u}}{\partial \hat{x}^{2}}$$

se definirmos $\overline{T}=\overline{L}^{2}/\kappa$ obtemos:
$$\boxed{\frac{\partial \hat{u}}{\partial \hat{t}} =   \frac{\partial^{2} \hat{u}}{\partial \hat{x}^{2}}}~~~~,~~  0 < \hat{x} < 1~~,~~ \hat{t} > 0.$$
- Podemos fazer o mesmo para as *condições de fronteira / iniciais*:
$$\begin{align*}
\text{CI:} \quad &  \hat{u}(\hat{x},0)  = \hat{f}(\hat{x}) \quad & 0 < \hat{x} < 1\\
\text{CF:}\quad &  \hat{u}(0,\hat{t})  = \hat{u}(1,\hat{t})= 0, \quad & \hat{t}>0.
\end{align*}$$

## 1.3 - Dedução 2
- Temos a *Lei da Difusão de Fourier*, que descreve a forma como o calor se propaga (de forma oposta ao seu gradiente, de temperaturas mais altas para menores):
$$\vec{F}=- \alpha \nabla u$$
que pela Lei de Gauss nos dá:
$$\iiint \nabla \cdot \vec{F}~dV=\iint (\vec{F}\cdot\hat{n})~ds$$
Ora, o lado direito não passa do fluxo de calor. Assim:
$$\iiint \nabla \cdot \vec{F}~ dV=- \frac{\partial}{\partial t}\iiint u ~dV$$
logo:
$$\nabla \cdot \vec{F}=- \frac{\partial u}{\partial t}$$
se voltarmos a substituir a Lei de Difusão de Fourier:
$$- \frac{\partial u}{\partial t}=\nabla \cdot \vec{F}=\nabla \cdot (- \alpha \nabla u)$$
logo:
$$\text{1D:}~~~~\boxed{\frac{\partial u}{\partial t}= \alpha \frac{\partial^{2}u}{\partial x^{2}}} \quad \quad;\quad \quad \text{3D:}~~~~ \boxed{\frac{\partial u}{\partial t}=\alpha \nabla^{2}u=a \Delta u}$$

## 1.4 - Dedução 3
- Não passei, a 2ª para mim já é boa que chegue.

## 1.5 - Perdas Radiativas
- Considerando que a superfície do corpo em estudo *não* está isolada, temos que a Lei de Stefan-Boltzmann se aplica:
$$\frac{\partial Q}{\partial t}=- \frac{\partial F}{\partial x}- \mu(u^{4}-v^{4})$$
o que nos dá:
$$\frac{\partial u}{\partial t}=\frac{K}{c\rho} \frac{\partial^{2}u}{\partial x^{2}} - \frac{\mu}{c\rho}(u^{4}-v^{4})$$
em que $v$ é a *tempartura ambiente* em torno do corpo e $\mu$ um coeficiente que depende do material.

## 1.6 - Termo Fonte
- No entanto, pdoemos ter fontes de calor dentro do volume em estudo, tendo-se:
$$c\rho \frac{\partial u}{\partial t}= \nabla \cdot(K_{0}\nabla u) + q$$
em que $q$ é o **termo de fonte**. No contexto da equação de calor consiste a uma função espacial que em cada iteração acrescenta algum valor à temperatura. Se a tempratura tendia para 0 ao longo do tempo, irá passar a tender para $q(\vec{r})$.
- Se tivessemos um meio não uniforme, podemos simplesmente usar a equação que obtivemos acima diretamente: $\partial_{t}u=\nabla \cdot(\alpha \nabla u)$, sendo que iriamos usando valores de $\alpha$ diferentes.

## 1.7 - EX1
- Comecemos por ver um problema em 1D
- Consideremos CF de Dirichlet com $u=0$
- Temos:
$$\begin{align*}
\frac{\partial u}{\partial t}&= \alpha \frac{\partial^{2}u}{\partial x^{2}}~~~~;~~ t\in[0,T]\\
CI:~~u(x,0)&= I(x)~~~~;~~ x\in[0,L]\\
CF:~~u(0,t)&= 0\\
CF:~~u(L,t)&= 0
\end{align*}$$
em que conhecemos a função $I(x)$.

# Forward Euler / Euler Para a Frente
- Começamos por tornar o problem discreto, passando a ter um domínio: $[0,L]\times[0,T]$ dividido em nodos $x_{i}=i\Delta x~,~i=0,\dots,N_{x}~~;~~t_{n}=n\Delta~,~ t~n=0,\dots,N_{t}$ 
- Definimos o ponto na posição $i$ no instante $n$ como $u(x_{i},t_{n})\equiv u_{i}^{n}$
- Tendo em conta as CI e CF temos:
![[fd_stencils_1D_1.png]]

- Usando a fórmula de 1ª derivada para a frente e de 2ª derivaa e temos diretamente da equação de calor:
$$\frac{u_{i}^{n+1}-u_{i}^{n}}{\Delta t}=\alpha \frac{u_{i+1}^{n}-2 u_{i}^{n} + u_{i-1}^{n}}{\Delta x^{2}}$$
que podemos escrever como
$$u_{i}^{n+1}=u_{i}^{n} + \alpha\frac{\Delta t}{\Delta x^{2}}(u_{i+1}^{n}-2u_{i}^{n}+u_{i-1}^{n})$$
em que $\alpha\frac{\Delta t}{\Delta x^{2}}=F$ é o *número de Fourier* desta malha. E temos então uma equação de $u_{i}^{n+1}$ o único valor destes 4 que nunca conhecemos (porque representa o **futuro**):
$$u_{i}^{n+1}= u_{i}^{n}+F(u_{i+1}^{n}-2u_{i}^{n}+u_{i-1}^{n})$$

- Assim o método de Forward Euler coniste em:
    1. Caulcular as *CI*: $u_{i}^{0}=I(x_{i})$ para todos os $x_{i}=0,\dots,N_{x}$ de $t=0$
    2. Para cada $n=0,\dots,N_{t}$:
        1. Usar a equação de $u_{i}^{n+1}$ em todos os $i=1,\dots,N_{x}-1$ 
        2. Para $i=0, N_{x}$ usar condições de fronteira para obter $u_{i}^{n+1}$

- Por exemplo, para $F=0.5$ e com o sequinte padrão inicial a vermelho temos:
![[Feuler 1.png]]
sendo o traçado a azul o estado do sistema após 0.06s é. 

**Código**
- Sendo `u` o array que contém o próximo estado do sistema e `u_1` o estado atual. Na prática, após definir as condições iniciais em `u_1` basta fazer:
```python
for n in range(0, Nt):
    # Calcular u em todos os nodos internos
    for i in range(1, Nx):
        u[i] = u_1[i] + F*(u_1[i-1] - 2*u_1[i] + u_1[i+1])
    #u[1:Nx] = u_1[1:Nx] + F*(u_1[0:Nx-1] + 2*u_1[1:Nx] + u_1[2:Nx+1]) -- com arrays

    # Aplicar condições fronteira (aqui nem seria necessário! Porquê?)
    u[0] = 0;  u[Nx] = 0

    # Actualizar u_1 antes de passar ao próximo passo
    u_1[:]= u
```

**Valores de F**
- O método de Euler Para a Frente resulta em:
    - Uma solução **divergente** se $F>0.5$
    - A condição inicial em cartola (como acima) resulta numa solução com ruído em dente de serra se $F=1/2$. Se $F=1/4$ já não

# Backward Euler / Euler Para Trás
- Fazemos basicamente a mesma coisa. Usamos a fórmula de derivada para trás na parte temporal e 2ª derivada na parte espacial e temos:
$$\frac{u_{i}^{n}-u_{i}^{n-1}}{\Delta t}=\alpha \frac{u_{i+1}^{n}-2 u_{i}^{n} + u_{i-1}^{n}}{\Delta x^{2}}$$
ora, agora temos o problema oposto ao que tínhamos antes: em princípio conhecemos $u_{i}^{n-1}$ (é passado) mas não sabamos mais nenhuma variável.
- Ou seja, para $N_{x}=4$ podemos especificar esta equação:
$$\begin{align*}
\frac{u_{1}^{n}-u_{1}^{n-1}}{\Delta t}&= \alpha \frac{u_{2}^{n}-2u_{1}^{n}+u_{0}^{n}}{\Delta x^{2}}\\
\frac{u_{2}^{n}-u_{2}^{n-1}}{\Delta t}&= \alpha \frac{u_{3}^{n}-2u_{2}^{n}+u_{1}^{n}}{\Delta x^{2}}
\end{align*}$$
ou seja:
$$\begin{cases}
u_{1}^{n}=u_{1}^{n-1} + F(u_{2}^{n}-2u_{1}^{n}+u_{0}^{n})\\
u_{2}^{n}=u_{2}^{n-1} + F(u_{3}^{n}-2u_{2}^{n}+u_{1}^{n})
\end{cases}=\begin{cases}
u_{1}^{n}(1+2F) - F u_{2}^{n}=u_{1}^{n-1} + Fu_{0}^{n} \\
u_{2}^{n}(1+2F) - F u_{1}^{n}=u_{2}^{n-1} + Fu_{3}^{n}
\end{cases}$$
em que deixamos $u_{0}^{n},u_{3}^{n}$ do lado direito porque são parte da CF e portanto conhecidos. 
- Temos então:
$$\begin{pmatrix}1+2F & -F \\ -f & 1+2F\end{pmatrix}\begin{pmatrix}u_{1}^{n} \\ u_{2}^{n}\end{pmatrix}=\begin{pmatrix}u_{1}^{n-1} \\ u_{2}^{n-1}\end{pmatrix}+\begin{pmatrix}u_{0}^{n} \\ u_{3}^{n}\end{pmatrix}$$
- Se generalizarmos, temos a equação:
$$-F u_{i-1}^{n}+ (1+2F)u_{i}^{n}-Fi_{1+1}^{n}=u_{i}^{n-1}$$
(para $i=1,\dots,N_{x}-1$)
- E temos então a matriz:
$$
A =
\begin{pmatrix}
A_{1,1} & A_{1,2} & 0 &\cdots & \cdots & \cdots & \cdots & \cdots & 0 \\ 
A_{2,1} & A_{2,2} & A_{2,3} & \ddots &   & &  & &  \vdots \\ 
0 & A_{3,2} & A_{3,3} & A_{3,4} & \ddots & &  &  & \vdots \\ 
\vdots & \ddots &  & \ddots & \ddots & 0 &  & & \vdots \\ 
\vdots &  & \ddots & \ddots & \ddots & \ddots & \ddots & & \vdots \\ 
\vdots & &  & 0 & A_{i,i-1} & A_{i,i} & A_{i,i+1} & \ddots & \vdots \\ 
\vdots & & &  & \ddots & \ddots & \ddots &\ddots  & 0 \\ 
\vdots & & & &  &\ddots  & \ddots &\ddots  & A_{N_{x-2},N_{x-1}} \\ 
0 &\cdots & \cdots &\cdots & \cdots & \cdots  & 0 & A_{N_{x-2},N_{x-1}} & A_{N_{x-1},N_{x-1}}
\end{pmatrix}
$$
em que simplesmente temos
$$\begin{align*}
A_{i,i-1}&= -F\\
A_{i,i}&= 1+2F\\
A_{i,i+1}&= -F
\end{align*}$$
- Temos ainda o lado direito da equação:
$$b = \left(\begin{array}{c}
b_1\\ 
b_2\\ 
\vdots\\ 
b_i\\ 
\vdots\\ 
b_{N_x-1}
\end{array}\right)~~~~;~~ b_{i}=u_{i}^{n-1}$$

**Código**
- A matriz A tem coeficientes constantes, pelo que pode ser calculada 1 vez, no início do programa.
- O vetor b tem que ser atualizado em cada iteração, porque depende da 
- Sendo `u` o array que contém o próximo estado do sistema e `u_1` o estado atual. Assim, o código simplesmente consiste em resolver o sistema $Ax=b$ em cada iteração temporal:

```python
for n in range(0, Nt):
    # Calcular b e resolver o sistema linear
    b = u_1.copy() # b contém o estado anterior
    b[0] = b[Nx] = 0   # forçar condições de fronteira
    u[:] = scipy.linalg.solve(A, b) # resolver sistema

    # Actualizar u_1 antes de passar ao próximo passo
    u_1[:] = u
```

# Crank-Nicholson (CN)
- Fazemos a equação da 2ª derivada espacial como até agora, mas fazê-mo-la co um tempo "intermédio": $n+ \frac{1}{2}$. Ou seja, o lado direito da equação fica: $\frac{1}{\Delta x^2}\left(u^{n+\frac{1}{2}}_{i-1} - 2u^{n+\frac{1}{2}}_i + u^{n+\frac{1}{2}}_{i+1}\right)$
- Ora, este tempo intermédio entre o presente e o futuro é meramente fictício. Assim, estimá-mo-lo com uma média:
$$u_{i}^{n+ \frac{1}{2}}\sim \frac{1}{2}(u_{i}^{n}+u_{i}^{n+1})$$
- Fazendo isto para todos os termos da derivada espacial e mexendo com a equação (um dia talvez deduza) obtemos:
$$u_{i}^{n+1}- \frac{1}{2}F(u_{i-1}^{n+1}-2u_{i}^{n+1}+u_{i+1}^{n+1})= u_{i}^{n}+ \frac{1}{2}F(u_{i-1}^{n}-2u_{i}^{n}+ u_{i+1}^{n})$$
- Ora, podemos escrever isto na forma matricial:
$$A u^{n+1}=B u^{n}$$
e podemos então definir uma matriz $A$ com a mesma forma que a do Euler para Trás, tal que:
$$\begin{align*}
A_{i,i-1}&= - \frac{1}{2}F\\
A_{i,i}&= 1+F\\
A_{i,i+1}&= - \frac{1}{2}F
\end{align*}$$
No entanto, agora temos uma matriz também do lado direito:
$$\begin{align*}
B_{i,i-1}&= \frac{1}{2}F\\
B_{i,i}&= 1-F\\
B_{i,i+1}&= \frac{1}{2}F
\end{align*}$$

**Código**
- Não percebi muito bem como se implementa 

# Regra $\theta$ / Theta Method
- Podemos escrever uma equação diferencial genérica $\frac{\partial u}{\partial t}=G[u]$ sendo $G$ um operador diferencial.
- A regra theta consiste em:
$$\frac{u_{i}^{n+1}-u_{i}^{n}}{\Delta t}= \theta G[u_{i}^{n+1}] + (1-\theta)G[u_{i}^{n}]$$
- Ora:
    - Se $\theta=0$ temos o Euler para a Frente (método explícito)
    - Se $\theta=1$ temos Euler para Trás (método implícito)
    - Se $\theta=\frac{1}{2}$ temos Crank-Nicholson

# Matrizes Esparsas
- Os métodos acima usam uma matriz A com dimensões $N_{x} \times N_{x}$. Ora, em cada uma das $N_{t}$ iterações o scipy o scipy faz a solução deste sistema, usando a matriz $A$ inteira. Facilmente vemos que consoante $N_{x}$ e $N_{t}$ aumentam, os métodos rapidamente se tornam lentos. Além disto, estaremos a guardar em memória muitas "variáveis" que na relidade são zeros.
- Ou seja, o número de operações no caso acima é proporcional a $N_{x}^{3}$.
- Mas podemos usar o módulo `scipy.sparse` que tem estruturas que permitem fazer os cálculos com matrizes esparsas de forma muito mais eficiente.

**Código**
```python
from scipy.sparse import diags
import scipy.sparse as sps
import scipy.sparse.linalg as spla

Nt = 170
T = 0.020
Nx = 64
L = 1.
a = 1.

x = np.linspace(0, L, Nx+1)   # espaço
dx = x[1] - x[0]
t = np.linspace(0, T, Nt+1)    #  tempo
dt = t[1] - t[0]
u   = np.zeros(Nx+1)          # próximo tempo
u_1 = np.zeros(Nx+1)          # tempo anterior
F = a*dt/dx**2

# definir diagonais da matriz esparsa e vetor b
principal  = np.zeros(Nx+1)
inferior = np.zeros(Nx)
superior = np.zeros(Nx)
b = np.zeros(Nx+1)

# preenhcer diagonais
principal[:] = 1 + 2*F
inferior[:] = -F
superior[:] = -F 
# colocar condições fronteira na matriz
principal[0] = 1
principal[Nx] = 1

A = diags(
    diagonals=[principal, inferior, superior],
    offsets=[0, -1, 1], shape=(Nx+1, Nx+1),
    format='csr')
#print (A.todense())  # Transforma na forma densa da matriz, para verificação.

# Aplicar condição inicial  u(x,0) = I(x)
sigma = 0.05

# Inserir condição inicial
u_1[:] = gaussiana(x[:],L,a,sigma)
init = u_1.copy()

for n in range(0, Nt):
    b = u_1
    b[0] = b[-1] = 0.0  # condições fronteira
    u[:] = spla.spsolve(A, b)
    u_1[:] = u

plt.plot(x,u,'b',x,init,'r--')
plt.show()
```

# Análise - Solução Analítica Aproximada
- Como podemos ver ao usar a equação acima, o que a equação de calor (e qualquer equação de difusão) faz é: reduzir a amplitude e alargar a distribuição original.
- As soluções da equação da difusão depende de $\eta=\frac{x-c}{\sqrt{4\alpha t}}$ para um certo $c$.
- Em particular temos a solução: $$u(x,t)=a ~\text{erf}(\eta)+b \quad \quad;\quad \quad \text{erf}(\eta)= \frac{2}{\sqrt{\pi}}\int_{0}^{\eta}e^{-\zeta^{2}}d\zeta$$
sim, esta é a **função erro** :DDD

### Degrau
- Ora, para $t\to0$ a função erro descreve uma função degrau centrada em $x=0$
- Assim, para uma difusão num intervalo $x\in[0,1]$ com o estado inicial descrito por uma função degrau centrada em $x=1/2$. Podemos então definir $c=1/2,a=-1/2,b=1/2$ e temos a solução:
$$u(x,t)=\frac{1}{2}\left(1-\text{erf}\left(\frac{x- \frac{1}{2}}{\sqrt{4\alpha t}} \right)\right)$$
e temos as CF:
$$u(0,t)=\frac{1}{2}\left(1-\text{erf}\left(\frac{- \frac{1}{2}}{\sqrt{4\alpha t}} \right)\right) \quad;\quad u(1,t)=\frac{1}{2}\left(1-\text{erf}\left(\frac{\frac{1}{2}}{\sqrt{4\alpha t}} \right)\right)$$

- E temos então: $u(0,t)\sim1~,~u(1,t)\sim0$ e $u(x,t\to\infty)\sim \frac{1}{2}$ (para todos $x\in~]0,1[~$)

### Impulso Gaussiano
- Se tivermos como condição inicial um *delta de Dirac*, conforme ele diminui e se alarga no tempo, a solução da equação descreve um **feixe gaussiano**:
$$ u(x,t)= \frac{1}{\sqrt{4\pi \alpha t}} \exp \left( -\frac{(x-c)^2}{4\alpha t} \right).
$$

### Seno
- Se o estado inicial for um seno $I(x)=Q\sin(kx)$ obtemos a solução
$$u(x,t)=Q e^{-a t}\sin(kx)~~~~;~~ a=\alpha k^{2}$$
- Ou seja, o seno vai sendo atenuado ao longo do tempo. Como o rate de atenuação depende de $k^{2}$, senos de frequência maior são atenuados muito mais rapidamente.

### Equações Discretas
- A solução para um seno pode ser escrita na forma complexa:
$$u(x,t)=Q e^{-at}e^{ikx}=Q e^{-\alpha k^{2}t}e^{ikx}$$
mas podemos escrever isto como:
$$u(x,t)\approx \sum\limits_{k} b_{k} e^{-\alpha k^{2}t}e^{ikx}$$
- Podemos então definir as amplitudes de cada modo $b_{k}$: $I(x)\sim \sum_{k}b_{k} e^{ikx}$
- E podemos definir o **fator de ampliação**: $A_{e}=e^{-\alpha k^{2}t}$
- E podemos definir um *fator de ampliação genérico*: $A^{n}$

### Análise de Métodos
- Queremos determinar soluções da equação de calor com a forma $$u_{q}^{n}=A^{n}e^{ikq\Delta x}$$
**Estabilidade**
- Nas soluções reais temos que ter $|A|<1$, porque o sinal decai sempre em amplitude.
    - Se $A\in[-1,0[$ o sinal decresce mas muda de sinal em cada iteração. Isto não é verificado fisicamente.
    - Se $|A| >1$ o sinal aumenta ao longo do tempo. Isto é impossível.

**Precisão**
- Para isto estudamos a expansão em Taylor da relação $A/A_{e}$-

#### Análise de Euler para a Frente
- Substituindo a solução $u_{q}^{n}=A^{n}e^{ikq\Delta x}$ temos:
$$\begin{align*}\\
\frac{u_{i}^{n+1}-u_{i}^{n}}{\Delta t}&= \alpha \frac{u_{i+1}^{n}-2 u_{i}^{n} + u_{i-1}^{n}}{\Delta x^{2}}\\
\frac{A^{n+1}e^{ikq \Delta x}-A^{n}e^{ik q\Delta x}}{\Delta t}&= \alpha \frac{A^{n}e^{ik(q+1)\Delta x} -2 A^{n}e^{ikq\Delta x} + A^{n}e^{ik(q-1)\Delta x}}{\Delta x^{2}}\\
\frac{A^{n}e^{ikx}(A-1)}{\Delta t}&= \alpha \frac{A^{n}e^{ikx} (2-e^{ik\Delta x}-e^{-ik\Delta x})}{\Delta x^{2}}\\
\frac{A-1}{\Delta t}&= \alpha \frac{2-2\cos(k\Delta x)}{\Delta x^{2}}\\
\frac{A-1}{\Delta t}&= \alpha \frac{-4\sin^{2}\left(\frac{k\Delta x}{2}\right)}{\Delta x^{2}}\\
A&= 1-4F\sin^{2}\left(\frac{k\Delta x}{2}\right)
\end{align*}$$
ou seja:
$$u_{q}^{n}=\left(1-4F\sin^{2}\left(\frac{k\Delta x}{2}\right)\right)^{n}e^{ik q\Delta x}$$
**Estabilidade**
- Acima de tudo é preciso que $A<1$ 
    - Se $A<-1$ a equação diverge (cresce rapidamente)
    - Para $A>-1$, para o sistema convergir é preciso que (uma destas)
        - $4F\sin^{2}(k\Delta x/2)\le2$ 
        - $F\le 1/2$
        - $\Delta t\le \frac{\Delta x^{2}}{2\alpha}$

**Precisão**
- Vamos definir $p=k \Delta x$
- Temos $A_{e}=\exp(-\alpha k^{2}\Delta t)=\exp(-4Fp^{2})$
- Podemos então fazer expansão em série de Taylor de $A/A_{e}$ em função de $F$:
$$\frac{A}{A_{e}}=1-4F\sin^{2}p+2Fp^{2}-16F^{2}p^{2}\sin^{2}p+8F^{2}p^{4}+\dots$$
- Sendo $F=\alpha \frac{\Delta t}{\Delta x^{2}}$ e $\sin p<1$ podemos dizer que o erro máximo que teremos será:
$$1- 4\alpha \frac{\Delta t}{\Delta x^2} + \alpha \Delta t -4 \alpha^2 \Delta t^2 + \alpha^2 \Delta t^2\Delta x^2 \ldots$$

#### Análise de Euler Para Trás
- Fazendo o mesmo processo de substituir a solução $u_{q}^{n}=A^{n}e^{ikq\Delta x}$ na solução obtemos:
$$\begin{align*}\\
\frac{u_{i}^{n}-u_{i}^{n-1}}{\Delta t}&= \alpha \frac{u_{i+1}^{n}-2 u_{i}^{n} + u_{i-1}^{n}}{\Delta x^{2}}\\
\frac{A^{n}e^{ikq \Delta x}-A^{n-1}e^{ikq \Delta x}}{\Delta t}&= \alpha \frac{A^{n}e^{ik(q+1) \Delta x}-2 A^{n}e^{ikq \Delta x} + A^{n}e^{ik(q-1) \Delta x}}{\Delta x^{2}}\\
A^{n}-A^{n-1}&= F(A^{n}e^{ik\Delta x} - 2A^{n}+A^{n}e^{-ik \Delta x})\\
1- A^{-1}&= F(-2+2\cos(k \Delta x))\\
A^{-1}&= 1-2F(\cos(k \Delta x)-1)\\
A^{-1}&= 1-2F\left(\cos^{2}\left(\frac{k\Delta x}{2}\right)-\sin^{2}\left(\frac{k\Delta x}{2}\right)-1\right)\\
A^{-1}&= 1+4F\sin^{2}\left(\frac{k\Delta x}{2}\right)\\
A&= \left[1+4F\sin^{2}\left(\frac{k\Delta x}{2}\right)\right]^{-1}
\end{align*}$$
ou seja temos a solução:
$$u_{q}^{n}=\left( 1 + 4F\sin^2 p\right)^{-n}e^{ikq\Delta x}$$
**Estabilidade**
- Podemos ver que teremos sempre $A\in~]0,1[~$ ou seja a solução é *sempre* estável!

#### Análise de CN
- Operando da mesma forma obtemos:
$$\begin{align*}
u_{i}^{n+1}- \frac{1}{2}F(u_{i-1}^{n+1}-2u_{i}^{n+1}+u_{i+1}^{n+1})&=  u_{i}^{n}+ \frac{1}{2}F(u_{i-1}^{n}-2u_{i}^{n}+ u_{i+1}^{n})\\
A^{n+1}\left[1 - \frac{1}{2}F\left(e^{-q \Delta x}-2+e^{+q \Delta x}  \right) \right]&= A^{n}\left[1 + \frac{1}{2}F\left(e^{-q \Delta x}-2+e^{+q \Delta x}  \right) \right]\\
A \left[1-F(\cos(k\Delta x)-1) \right]&= 1+F(\cos(k\Delta x)-1)\\
A \left[1+2F\sin^{2}\left(\frac{k\Delta x}{2}\right) \right] &= 1-2F\sin^{2}\left(\frac{k\Delta x}{2}\right)\\
A&= \frac{1-2F\sin^{2}\left(\frac{k\Delta x}{2}\right)}{1+2F\sin^{2}\left(\frac{k\Delta x}{2}\right)}
\end{align*}$$

A solução numérica é portanto:
$$ u_q^n = \left(\frac{1-2F\sin^2 p}{1+2F\sin^2 p} \right)^n e^{ikq\Delta x}$$
**Estabilidade**
- Tal como o Euler para trás, este método será *sempre* estável, pois temos sempre $A\in]-1,1[$ .

