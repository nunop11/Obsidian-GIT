- Como vimos no Postulado 5, na física quântica representamos grandezas como operadores. Recordando o que vimos na aula anterior, na base das posições temos:
$$\begin{align*}
x\to \hat{X}&=x & y\to \hat{Y}&=y & z\to \hat{Z}&=z \\
p_{x}\to \hat{P}_{x}&= \frac{\hbar}{i} \frac{\partial}{\partial x} &
p_{y}\to \hat{P}_{y}&= \frac{\hbar}{i} \frac{\partial}{\partial y} &
p_{z}\to \hat{P}_{z}&= \frac{\hbar}{i} \frac{\partial}{\partial z} &
\end{align*}$$
- Outro exemplo é:
$$\vec{\ell}\to \vec{L}=(\hat{L}_{x}, \hat{L}_{y}, \hat{L}_z)$$
- No entanto, nos 2 exemplos acima temos que:
$$\hat{X}\hat{P}_{x}\ne \hat{P}_{x}\hat{X} \quad \quad;\quad \quad \hat{L}_{x}\hat{L}_{y}\neq \hat{L}_{y}\hat{L}_{x}$$
isto ocorre porque estes pares de grandezas são *incompatíveis*.

# 1 - Grandezas incompatíveis
1. É impossível medir simultaneamente com precisão 2 grandezas incompatíveis. Um exemplo disto é $x, p_{x}$, tal como nos é indicado pelo princípio de incerteza de Heisenberg.
2. A ordem por que medimos grandezas incompatíveis importa. Por exemplo, se medirmos primeiro $x$ com muita precisão, depois iremos medir $p_{x}$ com menos precisão.

# 2 - Quantidades Estatísticas
### Física Clássica
- Consideremos a variável aleatória $x\in [a,b]$, sendo $\mathcal{P}(x)$ a função de distribuição de probabilidade de $x$. Assim, $\int_{a}^{b}\mathcal{P}(x)dx=1$
- Temos:
    - $\langle x\rangle = \int_{a}^{b}x\mathcal{P}(x)dx$
    - $\langle x^{2}\rangle = \int_{a}^{b}x^{2}\mathcal{P}(x)dx$
    - $\langle h(x)\rangle = \int_{a}^{b} h(x)\mathcal{P}(x)dx$, sendo $h$ uma função de $x$ ???
    - $\sigma(x)=\langle x^{2}\rangle - \langle x\rangle^{2}$ 
- Assim, $$\Delta x=\sqrt{\sigma(x)}$$

### Física Quântica
- Agora fazemos 
$$\begin{align*}
x &\to \hat{X}\\
\mathcal{P}(x) &\to |\Psi(x)|^{2}=\Psi^{*}(x)\Psi(x)
\end{align*}$$
- Deste modo, o valor médio de uma grandeza física $A$ será:
$$\langle A\rangle=\int \Psi^{*}(x)A \Psi(x) dx$$
- Alguns exemplos:
$$\begin{align*}
\langle x\rangle_{t} &= \int \Psi^{*}(x) x \Psi(x) dx\\
\langle p_{x}\rangle_{t} &= \int \Psi^{*}(x) \left[ \frac{\hbar}{i} \frac{\partial}{\partial x} \right] \Psi(x) dx\\
\langle E\rangle_{t} &= \int \Psi^{*}(x) \left[ i\hbar \frac{\partial}{\partial t} \right] \Psi(x) dx
\end{align*}$$

__*EXEMPLO*__
- Tendo o caso do poço infinito:
$$\Psi(x,t)= \begin{cases} \sqrt{\frac{2}{L}}\sin \left( \frac{n\pi x}{L} \right)e^{-i \frac{E_{n}}{\hbar} t} &; &0<x<L \\ 0 &; &complementar \end{cases}$$
__*Pt. 1*__
- Veremos como obter $\langle x\rangle$ no nível fundamental, $n=1$.
- No nível fundamental temos $\Psi_{1}(x,t)= \sqrt{\frac{2}{L}} \sin \left( \frac{\pi x}{L} \right) e^{-i \frac{E_{1}}{\hbar} t}$, sendo que $E_{1}=\frac{\pi^{2}k^{2}}{2mL^{2}}$.
- Assim:
$$\langle x\rangle_{t} = \int_{-\infty}^{+\infty} \Psi^{*}(x,t) x \Psi(x,t) dx= \frac{2}{L} \int_{0}^{L} x \sin^{2} \left( \frac{\pi x}{L} \right)dx=\frac{L}{2}$$
__*Pt. 2*__
- Agora vamos calcular $\langle p_{x}\rangle$ no nível $n=1$.
- Temos:
$$\begin{align*}
\langle p_{x}\rangle_{t}&= \int_{-\infty}^{+\infty} \Psi^{*}(x,t) \left[ \frac{\hbar}{i} \frac{\partial}{\partial x} \right] \Psi(x,t) dx\\
&= \frac{-2i\hbar}{L} \int_{0}^{L} dx \left[ \sin \left( \frac{\pi x}{L} \right) \bcancel{e^{i \frac{E_{1}}{\hbar} t}} \right] \cdot\frac{\partial}{\partial x} \left[ \sin \left( \frac{\pi x}{L} \right) \bcancel{e^{-i \frac{E_{1}}{\hbar} t}} \right]\\
&= \frac{-2i\hbar}{L} \int_{0}^{L} \sin \left( \frac{\pi x}{L} \right)\cdot \frac{\pi}{L} \cos \left( \frac{\pi x}{L} \right)\\
&= 0
\end{align*}$$
__*Pt. 3*__
- Por fim, vamos determinar $\langle E\rangle$ no nível fundamental.
- Ficamos com:
$$\begin{align*}
\langle E\rangle_{t} &= \int_{-\infty}^{+\infty} \Psi^{*}(x,t) \left( i\hbar \frac{\partial}{\partial t} \right) \Psi(x,t) dx \\
&= \frac{2i\hbar}{L} \int_{0}^{L} \left[\sin\left(\frac{\pi x}{L}\right) e^{i \frac{E_{1}}{\hbar} t}\right]\cdot \frac{\partial}{\partial t}\left[\sin\left(\frac{\pi x}{L}\right) e^{-i \frac{E_{1}}{\hbar} t} \right]\\
&= E_{1}
\end{align*}$$

# 3 - Potencial Harmónico
### Física Clássica
- Temos o caso que estudamos em Mecânica:
$$E = E_{c}+E_{p}= \frac{p^{2}}{2m} + \frac{1}{2}m \omega^{2}x^{2}$$
### Física Quântica
- Começamos por fazer as conversões de grandezas para operadores:
$$\begin{align*}
x\to \hat{X} &= x\\
p_{x}\to \hat{P}_{x} &= \frac{\hbar}{i} \frac{\partial}{\partial x}\\
E &\to i\hbar \frac{\partial}{\partial t}  
\end{align*}$$
- Temos portanto que $V(x)=\frac{1}{2} m \omega^{2} x^{2}$
- Ao substituir na equação de Schrödinger independente do tempo temos:
$$\left[\frac{-\hbar^{2}}{2m} \frac{d^{2}}{dx^{2}} + \frac{1}{2}m \omega^{2} x^{2} \right]\Psi(x)=E \Psi(x)$$
- Isto descreve uma *Equação de Hermite*
- Como tal, as equações da Equação de Schrodinger são do tipo:
$$\Psi_{n}(x)= C_{n} ~\chi_{n}(\beta x) e^{-\beta^{2} \frac{x^{2}}{2}}$$
- Em que
    - $C_{n}$ é a constante de normalização
    - $\chi_{n}(\beta x)$ é o $n$ polinómio de Hermite
    - $\beta$ é uma constante relacionada com a massa e $\omega$ do oscilador.

- Os polinómios são um conjunto de funções ortogonais que dependem de $n$, tal que:
$$\chi_{n}(\beta x)= (-1)^{n} e^{\beta^{2} \frac{x^{2}}{2}} \frac{d^{n}}{dx^{n}} \left( e^{- \beta^{2} \frac{x^{2}}{2}}  \right)$$
sendo que os primeiros termos são:
$$\begin{align*}
\chi_{0}(x) &= 1\\
\chi_{1}(x) &= 2y\\
\chi_{2}(x) &= 4y^{2}-2
\end{align*}$$
- Para este sistema temos $$E_{n} = \left(n+ \frac{1}{2}\right) \hbar \omega$$
- De notar que, como $V \propto x^{2}$, então o potencial é par. Deste modo, as soluções de Schrödinger serão pares ou ímpares.

__*EXEMPLO 1*__
- Iremos mostrar que $e^{-\beta^{2} \frac{x^{2}}{2}}$ é uma solução da ESIT e determinar a energia correspondente.

- Temos então a solução:
$$\Psi_{1}(x)=e^{-\beta^{2} \frac{x^{2}}{2}} \quad \quad;\quad \quad \frac{d\Psi_{1}}{dx}= -\beta^{2} e^{-\beta^{2} \frac{x^{2}}{2}}$$
$$\frac{d^{2}\Psi_{1}}{dx^{2}} = (-\beta^{2}+ \beta^{4}x^{2}) e^{-\beta^{2} \frac{x^{2}}{2}}$$
- Ao substituir na equação de Schrödinger 
$$\left( - \frac{\hbar^{2}}{2m}[-\beta^{2} + \beta^{4}x^{2}] + \frac{1}{2}m \omega^{2} x^{2} \right) \cancel{e^{-\beta^{2} \frac{x^{2}}{2}}} = E \cancel{e^{-\beta^{2} \frac{x^{2}}{2}} }$$
de onde se tem:
$$\begin{cases} \frac{-\hbar^{2}}{2m} \beta^{4}x^{2} + \frac{1}{2}m \omega^{2}x^{2} = 0 \\
\frac{\hbar^{2}}{2m} \beta^{2}=E   \end{cases}$$
para obter este sistema: na equação acima temos uma função de $x$ igual a $E$, uma constante. Assim, as porções da equações que dependem de $x$ têm que se anular e a porção independente de $x$ tem que ser igual a $E$.
Assim, da equação de cima temos: $$\beta^{4} = \frac{m^{2}\omega^{2}}{\hbar^{2}}$$
e da equação de baixo:
$$E = \frac{\hbar\omega}{2}$$
- Ora, ao comparar isto com a equação da energia, $E_n$, temos que esta é a energia funamental: $E_{0}$.
- De notar que $n=1\to E_{1}$ seria o 1º nível excitado e assim adiante.

#moderna #fisica 