### 4.0.1 - Grupo SU(2) e representações
### Grupo das translações
- Os operadores translação $\hat{T}_{\vec{a}}$ formam o grupo das translações, com as propriedades:
$$\begin{align*}
{T}_\vec{a}{T}_{\vec{b}}&= {T}_{\vec{a}+\vec{b}}  \quad \quad \quad \quad \quad \quad\textsf{(produto)}\\
{T}_{\vec{a}}({T}_\vec{b}{T}_{\vec{c}})&= ({T}_{\vec{a}}{T}_\vec{b}){T}_{\vec{c}} \quad \quad \quad \quad~\textsf{(associativo)}\\
{T}_{\vec{a}}\mathbb{1}&= {T}_{\vec{a}} \quad \quad \quad \quad \quad \quad \quad\textsf{(elemento neutro)}\\
\left({T}_{\vec{a}}\right)^{-1}&= \left({T}_{-\vec{a}} \right) \quad \quad \quad \quad \quad ~\textsf{(inverso)}
\end{align*}$$

- Sendo $\vec{a}$ um vetor infinitesimal, temos que as translações infinitesimais são descritas por $\vec{P}$ (demonstramos isso no exercício 9 da folha 3). Ou seja, podemos escrever:
$${T}_{\vec{a}}= e^{-i\vec{a}\cdot {\frac{\vec{P}}{\hbar}}}=\lim\limits_{n\to\infty} \left(1- i \frac{\vec{a}\cdot{\vec{P}}}{n\hbar} \right)^{n}$$
isto significa que podemos definir uma transformação finita como uma sequência infinita de transformações infinitesimais.

- Podemos então definir $P_{i}$ como sendo os *geradores das translações*.

- Grupos em que os elementos são identificados por parâmetros contínuos (neste caso temos o grupo das Translações, com o parâmetro contínuo $\vec{a}$) são chamados *grupos de Lie*. Neste caso, isto significa que translações finitas podem ser construidas ao exponenciar o gerador das translações, $\vec{P}$. Temos ainda que o produto de 2 elementos de um grupo de Lie continua a pertencer ao grupo ($T_{\vec{a}}\cdot T_\vec{b}$ pertence ao grupo das translações, pelo que é igual a $T_{\vec{a}+\vec{b}}$ como vimos acima).

### Grupo das Rotações
- Sendo $R$ uma matriz podemos escrever o grupo das rotações em $\mathbb{R}^{3}$:
$$\vec{r'}=R \vec{r} ~\Longleftrightarrow~ x'^{i}=R^{i}_{j}x ^{j} ~\Longleftrightarrow~ \begin{pmatrix}x_{1}'\\x_{2}'\\x_{3}'\end{pmatrix}=\begin{pmatrix}R_{11} & R_{12} & R_{13}\\R_{21} & R_{22} & R_{23} \\ R_{31} & R_{32} & R_{33}\end{pmatrix}\begin{pmatrix}x_{1} \\ x_{2} \\ x_{3}\end{pmatrix}$$
- Estas rotações são caraterizadas por $|\vec{r'}|^{2}=|\vec{r}|^{2}$ e temos ($R_{j}^{i}$ é o elemento da linha $i$ e coluna $j$ da matriz $R$):
$$\begin{align*}
x'^{i}x'^{j}= R_{j}^{i}x^{j}R_{k}^{j}x^{k}&= x^ix^{i}\\
(R^{T})_{i}^{j}x^{j}R_{k}^{j}x^{k}&= x^{i}x^{i}\\
(R^{T})_{i}^{j}R_{k}^{j}x^{j}x^{k}&= \delta_{ij}\delta_{ik}x^{j}x^{k}\\
(R^{T}R)_{jk}x^{j}x^{k}&= \delta_{jk}x^{j}x^{k}\\
R^{T}R&= \mathbb{1}
\end{align*}$$
por outras palavras, a matriz de rotação é *ortogonal*! 
> Nota sobre a dedução:
>     - linha 1 - partimos do facto que $|\vec{r'}|^{2}=|\vec{r}|^{2}$. Temos que $x'^{i}=R_{j}^{i}x^{j}$ 
>     - linha 2 - apenas reescrevemos a linha 1 com uma das matrizes transpostas
>     - linha 3 - introduzimos deltas de kronecker no lado direito, pelo que $x^{i}x^{i}=\delta_{ij}\delta_{ik}x^{j}x^{k}$ porque só não teremos $x^{i}x^{i}=0$ se $j=k=i$.
>     - linha 4 - reescrevemos os dois lados sem o termo $i$ (?) Não percebi muito bem

- Assim temos:
$\det(R^{T}R)=1\to(\det R)^{2}=1\to \det R=\pm1$
    - Se $\det (R)=-1$ temos reflexões ($\vec{r}\to-\vec{r}$)
    - Rotações têm $\det (R)=1$. Esta matriz 3x3 com determinante unitário é o grupo SO(3)
    - NOTA : Isto é uma propriedade: 
        $\det(A^{T}A)=\det I=1 ~,~ \det(A^{T})=\det(A)$. 
        Assim: $\det(A^{T}A)=\det(A^{T})\det(A)=(\det A)^{2}=1$.

- No grupo das translações tinhamos o parâmetro contínuo $\vec{a}$. No das Rotações temos o parâmetro $\vec{\theta}$ (o vetor em si indica a direção de rotação, o módulo do vetor indica o grau de rotação). Podemos representar:
$$\hat{R}_\vec{\theta}|\vec{r}\rangle=|R_\vec{\theta}\vec{r}\rangle$$
e para um estado representado na base das posições:
$$\begin{align*}
\hat{R}_\vec{\theta}\psi(\vec{r})&= \langle\vec{r}|\hat{R}_\vec{\theta}|\psi\rangle\\
&= \langle\vec{r}|\hat{R}_\vec{\theta}\mathbb{1}|\psi\rangle\\
&= \langle \vec{r}|\hat{R}_\vec{\theta}|\int d^{3}r'~|\vec{r'}\rangle\langle\vec{r'}|\psi\rangle\\
&= \int d^{3}r' \langle \vec{r}|\hat{R}_\vec{\theta}|\vec{r'}\rangle \langle \vec{r'}|\psi\rangle\\
&= \int d^{3}r' \langle\vec{r}|R_\vec{\theta}\vec{r'}\rangle \psi(\vec{r'})\\
&= \int d^{3}r'~ \delta(\vec{r}-R_{\theta}\vec{r'})\psi(\vec{r'})\\
&= \int d^{3}u'~\delta(\vec{r}-\vec{u})\psi(R_{\theta}^{-1}\vec{u'})  \quad \quad \quad (\vec{u'}=R_{\theta}\vec{r'}\Leftrightarrow \vec{r'}=R_{\theta}^{-1} \vec{u'})\\
&= \psi(R_{\theta}^{-1}\vec{r})
\end{align*}$$
ou seja:
$$R_\vec{\theta} \psi(\vec{r})=\psi(\underbrace{R_\vec{\theta}^{-1}\vec{r}}_{\vec{r'}})$$
ou seja, aplicar um operador de rotação em $\vec\theta$ à função de onda em $\vec{r}$ é equivalente à função de onda na posição resultante de rodar $\vec{r}$ em $-\vec{\theta}$.
- De notar que, por $R_\vec{\theta}$ ser ortogonal, $R_\vec{\theta}^{-1}=R_\vec{\theta}^{T}$

### 4.0.2 - Operador Momento Angular Orbital
- Consideremos que atuamos num sistema uma rotação descrita por $\vec{\theta}=\theta\hat{z}$. Podemos escrever:
$$R_\vec{\theta} = \begin{pmatrix}\cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 &  \\ 0 & 0 & 1\end{pmatrix}$$
- Vimos atrás que: $R_\vec{\theta} \psi(\vec{r})=\psi(R_\vec{\theta}^{-1}\vec{r})$
- Como a matriz $R$ é ortogonal temos:
$$R_\vec{\theta}^{-1}= \begin{pmatrix}\cos\theta & \sin\theta & 0 \\ -\sin\theta & \cos\theta & 0 &  \\ 0 & 0 & 1\end{pmatrix}=R_\vec{\theta}^{T}$$
podemos também escrever: $R_\vec{\theta}^{-1}=R_{-\vec{\theta}}$  (tal com explicado acima, a matriz inversa de $R_\vec{\theta}$ consiste em rodar no sentido oposto $-\vec{\theta}$)

- Usando $\cos\theta\sim1~,~\sin\theta\sim\theta$ temos:
$$\vec{r'}=R_{-\vec{\theta}}\vec{r}\approx\begin{pmatrix} 1 & \theta & 0 \\ -\theta & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}\begin{pmatrix}x \\ y \\ z\end{pmatrix}=\begin{pmatrix}x+\theta y  \\ y-\theta x \\ z\end{pmatrix}$$
ou seja temos:
$$\psi(R_\vec{\theta}^{-1}\vec{r})\approx \psi(x+\theta y, y-\theta x,z)$$
- Ora, podemos expandir isto em série de Taylor:
$$\begin{align*}
f(x,y,z)&= f(x_{0},y_{0},z_{0})+\frac{\partial f}{\partial x}|_{(x_{0},y_{0},z_{0})}(x-x_{0})+\frac{\partial f}{\partial y}|_{(x_{0},y_{0},z_{0})}(y-y_{0})+\frac{\partial f}{\partial z}|_{(x_{0},y_{0},z_{0})}(z-z_{0})\\
&\downarrow\\
\psi(x+\theta y, y- \theta x,z)&= \psi(x,y,z) + \frac{\partial\psi}{\partial x}(\theta y) + \frac{\partial \psi}{\partial y}(-\theta x)+\frac{\partial \psi}{\partial z}(0)\\
&= \left[1+\theta\left(y\frac{\partial}{\partial x}-x \frac{\partial}{\partial y}\right)\right]\psi(x,y,z)
\end{align*}$$

**Momento Angular**
- Como sabemos $\vec{L}=\vec{R}\times\vec{P}$. Ora, a componente em $z$ do momento angular será: $L_{z}=XP_{y}-YP_{x}=\frac{\hbar}{i}(x\frac{\partial}{\partial y}-y\frac{\partial}{\partial x})$
- Vemos logo as semelhanças à equação obtida atrás para as rotações:
$$\begin{align*}
R_\vec{\theta}\psi(\vec{r})&\simeq \left[1-\frac{i}{\hbar}\theta L_{z}\right]\psi(\vec{r})
\end{align*}$$
- Se generalizarmos isto para uma rotação em qualquer direção:
$$R_\vec{\theta}\psi(\vec{r})\simeq \left[1-\frac{i}{\hbar}\vec{\theta}\cdot\hat{\vec{L}}\right]\psi(\vec{r}) \quad \quad;\quad L_{i}=\varepsilon_{ijk}X^{j}P^{k}=\varepsilon_{ijk}x^{j} \frac{\partial}{\partial x^{k}}$$

- Recordando o que vimos acima, isto apenas descreve transformações infinitesimais (daí termos aproximado $\sin\theta=\theta$). Para uma rotação finita temos:
$$R_\vec{\theta}=e^{- \frac{i}{\hbar} \vec{\theta}\cdot\hat{\vec{L}}}=\lim\limits_{n\to\infty}\left(1-i \frac{\vec{\theta}}{n}\cdot \frac{\hat{\vec{L}}}{\hbar}\right)^{n}$$

## 4.1 - Representação Algébrica do Momento Angular
- Como vimos atrás, podemos definir o operador de momento angular orbital com: $\vec{L}=\vec{R}\times\vec{P}$, tendo o caso especial da componente dos $z$: $L_{z}=XP_{y}-YP_{x}=\frac{\hbar}{i}(x \frac{\partial}{\partial y}-y \frac{\partial}{\partial x})$

- Temos:
$$[L_{i},L_{j}]=i\hbar \varepsilon_{ijk}L_{k}$$
por exemplo: $[L_{x},L_{y}]=i\hbar L_{z}$ (não percebi a dedução)

$$\begin{align*}
[L_{x},L_{y}]&= \left(\frac{\hbar}{i}\right)^{2} \left[y \frac{\partial}{\partial z}-z \frac{\partial}{\partial y}, -x \frac{\partial}{\partial z}+z \frac{\partial}{\partial x} \right]\\
&= - \hbar ^{2}\left(y \frac{\partial}{\partial x}- x\frac{\partial}{\partial y}\right)\\
&= i\hbar \frac{\hbar}{i} \left(x\frac{\partial}{\partial y}-y \frac{\partial}{\partial x}\right)=i\hbar L_{z}
\end{align*}$$
podemos mostrar isto com cálculos à bruta:
$$\begin{align*}
\left[y \frac{\partial}{\partial z}-z \frac{\partial}{\partial y}, -x \frac{\partial}{\partial z}+z \frac{\partial}{\partial x} \right] &= y \frac{\partial}{\partial z}\left(-x \frac{\partial}{\partial z}+z \frac{\partial}{\partial x}\right)-z \frac{\partial}{\partial y}\left(-x \frac{\partial}{\partial z}+z \frac{\partial}{\partial x}\right) +\\
& +x \frac{\partial}{\partial z}\left(y\frac{\partial}{\partial z}-z \frac{\partial}{\partial y}\right)-z \frac{\partial}{\partial x}\left(y\frac{\partial}{\partial z}-z \frac{\partial}{\partial y}\right)\\
&= \cancel{-xy \partial_{z}^{2}} + y \partial_{x} +\bcancel{yz \partial_{z}\partial_{x}} + \xcancel{zx \partial_{y}\partial_{z}}  - z^{2}\partial_{y}\partial_{x} + \cancel{xy \partial_{z}^{2}} - x \partial_{y} - \xcancel{xz \partial_{z}\partial_{y}} - \bcancel{zy \partial_{x}\partial_{z}} + z^{2}\partial_{x}\partial_{y}\\
&= y \partial_{x} - x \partial_{y}\\
\end{align*}$$

- Podemos ainda deduzir isto com as propriedades da distribuição de cumulantes $[A+B,C]=[A,C]+[B,C]~;~ [A,B+C]=[A,B]+[A,C]$:
$$\begin{align*}
\left[y \frac{\partial}{\partial z}-z \frac{\partial}{\partial y}, -x \frac{\partial}{\partial z}+z \frac{\partial}{\partial x} \right] &= \left[y \frac{\partial}{\partial z}-z \frac{\partial}{\partial y}, -x \frac{\partial}{\partial z}\right]+ \left[y \frac{\partial}{\partial z}-z \frac{\partial}{\partial y}, z\frac{\partial}{\partial x}\right]\\
&= \left[y\frac{\partial}{\partial z},-x\frac{\partial}{\partial z}\right] + \left[-z\frac{\partial}{\partial y}, -x \frac{\partial}{\partial z}\right] + \left[y \frac{\partial}{\partial z}, z \frac{\partial}{\partial x}\right] + \left[-z \frac{\partial}{\partial y},z \frac{\partial}{\partial x}\right]\\
&= 0 + \left[-z\frac{\partial}{\partial y}, -x \frac{\partial}{\partial z}\right] + \left[y \frac{\partial}{\partial z}, z \frac{\partial}{\partial x}\right] + 0\\
&= \left[y \frac{\partial}{\partial z}, z \frac{\partial}{\partial x}\right] + \left[-z\frac{\partial}{\partial y}, -x \frac{\partial}{\partial z}\right]
\end{align*}$$
- Temos ainda as propriedades de comutação com produtos de operadores $[AB,C]=A[B,C] + [A,C]B ~;~ [A,BC]=[A,B]C + B[A,C]$:
$$\begin{align*}
\left[y \frac{\partial}{\partial z}-z \frac{\partial}{\partial y}, -x \frac{\partial}{\partial z}+z \frac{\partial}{\partial x} \right] &= \left[y \frac{\partial}{\partial z}, z \frac{\partial}{\partial x}\right] + \left[-z\frac{\partial}{\partial y}, -x \frac{\partial}{\partial z}\right]\\
&= \left[y, z \frac{\partial}{\partial x}\right] \frac{\partial}{\partial z} + y\left[\frac{\partial}{\partial z}, z \frac{\partial}{\partial x}\right] + \left[-z, -x \frac{\partial}{\partial z}\right]\frac{\partial}{\partial y} -z \left[\frac{\partial}{\partial y}, -x \frac{\partial}{\partial z}\right]\\
&= [y,z]\partial_{x}\partial_{z} + z[y, \partial_{x}]\partial_{z} + y[\partial_{z},z]\partial_{x} + yz[\partial_{z},\partial_{x}] + [-z,-x]\partial_{z}\partial_{y} -x [-z, \partial_{x}]\partial_{y} -\\
&\quad  - z[\partial_{y},-x]\partial_{z}+xz[\partial_{y},\partial_{z}] \\
&= 0 + z[y, \partial_{x}]\partial_{z} + y[\partial_{z},z]\partial_{x} + yz[\partial_{z},\partial_{x}] + 0 -x [-z, \partial_{x}]\partial_{y} - z[\partial_{y},-x]\partial_{z}+xz[\partial_{y},\partial_{z}] \\
\end{align*}$$
(Não consegui, mas esta é a dedução do MC)

---

### Definição do operador
- De forma generalizada, definimos um operador de momento angular como um conjunto de 3 observáveis $J_{x},J_{y},J_{z}$ que definem um vetor $\vec{J}=(J_{x},J_{y},J_{z})$ e satisfazem a relação:
$$[J_{i},J_{j}]=i\hbar \varepsilon_{ijk}J_{k}$$
que, tal como vimos acima, é o caso do operador do momento angular orbital $\vec{L}$ a atuar em funções de onda.
- Mais concretamente, temos:
$$\begin{align*}
[J_{x},J_{y}]&= i\hbar J_{z}\\
[J_{y},J_{z}]&= i\hbar J_{x}\\
[J_{z},J_{x}]&= i\hbar J_{y}
\end{align*}$$
- Temos que $\vec{J}^{2}=J_{x}^{2}+J_{y}^{2}+J_{z}^{2}$ comuta com qualquer componente sua (iremos usar a distribuição do comutador $[A+B,C]=[A,C]+[B,C]$):
$$\begin{align*}
[\vec{J}^{2},J_{x}]&= \left[J_{x}^{2}+J_{y}^{2}+J_{z}^{2},J_{x}\right]\\
&= [J_{x}^{2},J_{x}]+[J_{y}^{2},J_{x}]+[J_{z}^{2},J_{x}]\\
&= J_{x}[J_{x},J_{x}]+[J_{x},J_{x}]J_{x}+[J_{y}^{2},J_{x}]+[J_{z}^{2},J_{x}]\\
&= [J_{y}^{2},J_{x}]+[J_{z}^{2},J_{x}]\\
&= J_{y}[J_{y},J_{x}]+[J_{y},J_{x}]J_{y} + J_{z}[J_{z},J_{x}]+[J_{z},J_{x}]J_{z}\\
&= i\hbar (J_{y}(-J_{z})+ (-J_{z})J_{y} + J_{z}J_{y}+ J_{y}J_{z})\\
&= 0
\end{align*}$$
- Ora, pelas relações de comutação, não conseguimos encontrar uma base de vetores próprios comuns a $J_{x},J_{y},J_{z}$. No entanto, podemos encontrar uma base comum a $\vec{J}^{2}$ e uma componente. Por convenção usamos $J^{2},J_{z}$.

- Mais no início do semestre vimos Harmónicos esféricos:
$$\hat{L^{2}}Y_{\ell}^{m}(\theta, \varphi)=\hbar^{2}\ell(\ell+1 )Y_{\ell}^{m}(\theta,\varphi) \quad \quad;\quad \ell=0,1,2,\dots$$
$$\hat{L_{z}}Y_{\ell}^{m}(\theta,\varphi)=m\hbar Y_{\ell}^{m}(\theta,\varphi) \quad \quad;\quad m=-\ell,\dots,0,\dots,+\ell$$
- Podemos definir *operadores de escada*: $$J_{\pm}=J_{x}\pm i J_{y}$$
(mais ou menos como os operadores criação e aniquilação em Osciladores Harmónicos)
- Podemos determinar as relações de comutação relevantes:
$$\begin{align*}
[J_{z},J_{\pm}]&= [J_{z},J_{x}]\pm i[J_{z},J_{y}]\\
&= i\hbar J_{y} \pm i (-i\hbar J_{x})\\
&= \pm\hbar(J_{x}\pm iJ_{y})=\pm \hbar J_{\pm}\\
\\
[J_{+},J_{-}]&= [J_{x}+ i J_{y}, J_{x}-i J_{y}]\\
&= [J_{x}+iJ_{y},J_{x}] + [J_{x}+iJ_{y},-iJ_{y}]\\
&= [J_{x},J_{x}]+[iJ_{y},J_{x}]+ [J_{x},-iJ_{y}]+[iJ_{y},-iJ_{y}]\\
&= [J_{x},-iJ_{y}]+[iJ_{y},J_{x}]\\
&= -i (i\hbar J_{z}) + i(-i\hbar J_{z})=2\hbar J_{z}\\
\\
[\vec{J}^{2},J_{\pm}]&= [J_{x}^{2}+J_{y}^{2}+J_{z}^{2},J_{x}\pm iJ_{y}]\\
&= [J_{x}^{2},J_{x}\pm iJ_{y}]+[J_{y}^{2},J_{x}\pm iJ_{y}]+[J_{z}^{2},J_{x}\pm iJ_{y}]\\
&= [J_{x}^{2},J_{x}]\pm [J_{x}^{2},iJ_{y}] +  [J_{y}^{2},J_{x}]\pm [J_{y}^{2},iJ_{y}] + [J_{z}^{2},J_{x}]\pm [J_{z}^{2},iJ_{y}]\\
&= 0
\end{align*}$$
- Podemos ainda escrever:
$$\begin{align*}
\vec{J}^{2}&= \frac{1}{2}(J_{+}J_{-}+J_{-}J_{+})+J_{z}^{2}\\
&= \frac{1}{2}\left[(J_{x}+iJ_{y})(J_{x}-iJ_{y})+(J_{x}-iJ_{y})(J_{x}+iJ_{y}) \right]\\
&= \frac{1}{2} (J_{x}^{2}-iJ_{x}J_{y}+iJ_{y}J_{x}-i^{2}J_{y}^{2}+J_{x}^{2}+iJ_{x}J_{y}-iJ_{y}J_{x}-i^{2}J_{y}^{2})+J_{z}^{2}\\
&= J_{x}^{2}+J_{y}^{2}+J_{z}^{2}
\end{align*}$$
definimos assim para acomodar o caso em que $J_{x}J_{y}\neq J_{y}J_{x}$. Caso contrário podíamos simplesmente ter $\vec{J}^{2}=J_{+}J_{-}+J_{z}^{2}$.
- Podemos ainda escrever $J_{+}J_{-}=J_{x}^{2}+J_{y}^{2}-i\hbar[J_{x},J_{y}]=J_{x}^{2}+J_{y}^{2}+\hbar J_{z}$

### Base de estados próprios de $\{\vec{J}^{2},J_{z}\}$
- Chamaremos aos vetores desta base de $\ket{j,m}$, em que estamos a omitir outros números quânticos ($\ket{j,m}\equiv\ket{\alpha,j,m}$). No entanto devemos notar que frequentemente $\{\vec{J}^{2},J_{z}\}$ não forma um CCOC, pelo que se torna necessário usar um 3º índice para distinguir vetores próprios diferentes associados a um valor próprio degenerado.
- Por definição, estes vetores são vetores próprios comuns a $\vec{J}^{2},J_{z}$. Temos então os valores próprios:
$$\begin{align*}
\vec{J}^{2}\ket{j,m}&= \hbar^{2}j(j+1)\ket{j,m}\\
J_{z}\ket{j,m}&= \hbar m\ket{j,m}
\end{align*}$$
(sendo a forma destas equações idêntica à dos harmónicos esféricos)

- Os operadores $J_{x}J_{y},J_{z}$ são hermíticos e têm as mesmas dimensões que $\hbar$. Assim, sendo $\vec{J}^{2}$ a soma do quadrado de operadores hermíticos, temos que os seus valores próprios serão da forma $\lambda\hbar^{2}$. Disto resulta que $\lambda=j(j+1)\ge 0$. 

- Provamos acima que $[J_{z},J_{\pm}]=\pm\hbar J_{\pm}$. Assim, temos que $J_{\pm}\ket{j,m}$ será um vetor próprio de $J_{z}$ com valor $(m\pm1)\hbar$:
$$\begin{align*}
[J_{z},J_{\pm}]&= \pm \hbar J_{\pm}\\
J_{z}J_{\pm}-J_{\pm}J_{z}&= \pm\hbar J_{\pm}\\
J_{z}J_{\pm}&= J_{\pm}J_{z} \pm\hbar J_{\pm}\\
&\downarrow\\
J_{z}(J_{\pm}\ket{j,m})&= J_{\pm}J_{z}\ket{j,m}\pm \hbar J_{\pm}\ket{j,m}\\
&= J_{\pm}m\hbar\ket{j,m}\pm J_{\pm}\hbar \ket{j,m}\\
&= \hbar(m\pm1)(J_{\pm}\ket{j,m})
\end{align*}$$
- E podemos escrever $J_{\pm}\ket{j,m}=c_{\pm}(j,m)\ket{j,m\pm1}$ em que
$$\begin{align*}
|c_{\pm}(j,m)|^{2}&= \langle j,m|J_{\pm}^{\dagger}J_{\pm}|j,m\rangle\\
&= \langle j,m|J_{\mp}J_{\pm}|j,m\rangle\\
&= \langle j,m|(J_{x}\mp iJ_{y})(J_{x}\pm iJ_{y})|j,m\rangle\\
&= \langle j,m|J_{x}^{2}+J_{y}^{2}\pm i[J_{x},J_{y}]|j,m\rangle\\
&= \langle j,m|\vec{J}^{2}-J_{z}^{2}\mp\hbar J_{z}|j,m\rangle\\
&= \langle j,m|\biggr[(j(j+1)-m^{2}\mp m)\hbar^{2}|j,m\rangle\biggr]\\
&= (j(j+1)-m^{2}\mp m)\hbar^{2}\langle j,m|j,m\rangle\\
&= (j(j+1)-m^{2}\mp m)\hbar^{2}=(j(j+1)-m(m\pm 1))\hbar^{2}
\end{align*}$$
ou seja:
$$J_{\pm}\ket{j,m}=\hbar\sqrt{j(j+1)-m(m\pm 1)}~\ket{j,m\pm1}$$
- Uma vez que $J_{\pm}$ é um operador hermitico, é preciso que $|c_{\pm}|^{2}\ge0$ (caso contrário poderíamos ter $c_{\pm}$ complexo). Disto resulta:
$$\begin{align*}
j(j+1)-m(m\pm1)&= \begin{cases}(j-m)(j+m+1) \\(j-m+1)(j+m)\end{cases}\ge 0\\
\begin{cases}(j-m)(j+m+1)\ge0 \\(j-m+1)(j+m)\ge0\end{cases} ~~&\to~~ \begin{cases}-(j+1)\le m\le j\\-j\le m\le j+1\end{cases} ~~\to~~ -j\le m\le j 
\end{align*}$$

- Consideremos agora que temos um estado $\ket{j,m}$. Nele atuamos sucessivamente com um operador $J_{+}$. Como já vimos, este irá manter $j$ e acrescentar 1 unidade a $m$ (multiplicando ainda por uma constante $c_{+}$). Ora, é então fundamental que $|c_{+}(j,m)|^{2}$ nunca se torne negativo (na equação temos $j(j+1)-m(m+ 1)$, se $m$ continuar a aumentar e $j$ ficar constante, eventualmente ficaremos com $|c_{+}|^{2}<0$).
- Para evitar isto, consideramos que existe um valor máximo de $m$: $m=j$, tal que $$J_{+}\ket{j,j}=0$$
- Da mesma forma, consideramos que $m$ tem um valor mínimo: $m=-j$ tal que
$$J_{-}\ket{j,-j}=0$$

- Temos que $\ket{j,-j}\propto J_{-}^{2j}\ket{j,j}$. Assim, temos que $2j\in\mathbb{Z}_{0}^{+}$. Por outras palavras: $$j=0,\frac{1}{2},1,\frac{3}{2},\dots$$
com $m=-j,-j+1,\dots,j-1,j$

## Representações do Momento Angular
- Para cada $j$ temos $2j+1$ vetores (1 por cada $m$) que geram um conjunto $\mathscr{E}_{j}$ que constitui uma representação algébrica do momento angular.
- Temos:
$$\begin{align*}
J_{z}\ket{j,m}&= \hbar m\ket{j,m}\\
J_{x}\ket{j,m}&= \frac{J_{+}-J_{-}}{2}\ket{j,m}= \frac{\hbar}{2}\biggr[\sqrt{j(j+1)-m(m+1)}\ket{j,m+1} + \sqrt{j(j+1)-m(m-1)}\ket{j,m-1} \biggr]\\
J_{y}\ket{j,m}&= \frac{J_{+}-J_{-}}{2i}\ket{j,m}=\frac{\hbar}{2i}\biggr[\sqrt{j(j+1)-m(m+1)}\ket{j,m+1} - \sqrt{j(j+1)-m(m-1)}\ket{j,m-1} \biggr]\\
\end{align*}$$

- Os operadores $J_{i}$ são representados para cada $j$ por matrizes $(2j+1)(2j+1)$ com entradas:
$$\begin{align*}
\langle j,m'|J_{z}|j,m\rangle&= \hbar m \delta_{m,m'}\\
\langle j,m'|J_{x}|j,m\rangle&= \frac{\hbar}{2}\biggr[\sqrt{j(j+1)-m(m+1)}\delta_{m',m+1} + \sqrt{j(j+1)-m(m-1)}\delta_{m',m-1} \biggr]\\
\langle j,m'|J_{y}|j,m\rangle&= \frac{\hbar}{2i}\biggr[\sqrt{j(j+1)-m(m+1)}\delta_{m',m+1} - \sqrt{j(j+1)-m(m-1)}\delta_{m',m-1} \biggr]
\end{align*}$$

### EXEMPLOS
#### Singleto - $j=0$
- Simplesmente temos $\ket{0,0}$
- Temos 1 só elemento na matriz de $J_{i}$: $\bra{0,0}J_{i}\ket{0,0}=0$ 
- Nas posições, isto é representado por um harmónico esférico $Y_{0}^{0}(\theta,\varphi)=\frac{1}{\sqrt{4\pi}}$ 

#### Dubleto - $j=\frac{1}{2}$
- Representação 2D. Temos $\ket{\frac{1}{2},\frac{1}{2}},\ket{\frac{1}{2},- \frac{1}{2}}$ 
- Temos os elementos de matriz:
$$\begin{align*}
\bra{\tfrac{1}{2},m'}J_{x}\ket{\tfrac{1}{2},m}&= \frac{\hbar}{2}\begin{pmatrix}0 & 1\\1 & 0\end{pmatrix}=\frac{\hbar}{2}\sigma_{x}\\
\bra{\tfrac{1}{2},m'}J_{y}\ket{\tfrac{1}{2},m}&= \frac{\hbar}{2}\begin{pmatrix}0 & -i\\i & 0\end{pmatrix}=\frac{\hbar}{2}\sigma_{y}\\
\bra{\tfrac{1}{2},m'}J_{z}\ket{\tfrac{1}{2},m}&= \frac{\hbar}{2}\begin{pmatrix}1 & 0\\0 & -1\end{pmatrix}=\frac{\hbar}{2}\sigma_{z}
\end{align*}$$
em que a $\sigma_{i}$ chamamos de *Matrizes de Pauli*.
- Esta representação *não* corresponde a nada representado nos harmónicos esféricos. Invés disso, devemos pensar nestes estados como descrevendo graus de liberdade internos de uma partícula: **_Spin Intríseco_**. Representamos $J=S$.

> Se estiveres a ler isto e não estiveres a perceber de onde vêm as matrizes:
>    Começamos por fazer uma matriz 2x2 assim: $$\begin{matrix}m= &  \begin{matrix}-\frac12  & \frac12\end{matrix}\\ \begin{matrix}m'=-\frac{1}{2}\\ m'=\frac12\end{matrix}& \begin{pmatrix}X & X\\ X & X\end{pmatrix}\end{matrix}$$
>    e podemos até imaginar a matriz $(m',m)=\begin{pmatrix}(- \frac{1}{2},- \frac{1}{2}) & (\frac{1}{2},-\frac{1}{2})\\(-\frac{1}{2}, \frac{1}{2}) & (\frac{1}{2}, \frac{1}{2})\end{pmatrix}$
>    - Caso de $J_{x}$:
>        - Comecemos no canto superior esquerdo da matriz: temos $m=-1/2=m'$. Na equação do elemento da matriz de $J_{x}$ temo os deltas de Kronecker $\delta_{m',m+1}$ e $\delta_{m',m-1}$. Com $m=m'$ ambos os deltas são nulos e o elemento da matriz é $0$.
>        - Agora o canto superior direito: temos $m=\frac{1}{2},m'= \frac{-1}{2}$. Os deltas ficam: $\delta_{m',m+1}=\delta_{\frac{-1}{2},\frac{3}{2}}=0$ e $\delta_{m',m-1}=\delta_{- \frac{1}{2},- \frac{1}{2}}=1$. Ao substituir $j=\frac{1}{2},m=\frac{1}{2}$ na equação: $\langle j,m'|J_{x}|j,m\rangle= \frac{\hbar}{2}\sqrt{\frac{1}{2}\left(\frac{1}{2}+1\right)- \frac{1}{2}\left(\frac{1}{2}-1\right)}\delta_{m',m-1}=\frac{\hbar}{2}\sqrt{\frac{3}{4}+ \frac{1}{4}}=\frac{\hbar}{2}$
>        - Nos 2 elementos de baixo temos algo análogo ao aqui visto
>    - Caso de $J_{y}$:
>        - Igual ao caso $J_{x}$, mas como na formula temos $\frac{\hbar}{2i}$ apenas passamos o $i$ para os elementos da matriz
>    - Caso de $J_{z}$:
>        - Este é o mais simples. O delta de Kronecker presenta na equação é apenas $\delta_{m,m'}$. Ou seja, os termos não nulos são aqueles em que $m=m'$ - os elementos da diagonal. 

#### Tripleto - $j=1$
- Temos agora uma representação 3D: $\{\ket{1,1},\ket{1,0},\ket{1,-1}\}$
- Temos os elementos das matrizes:
$$\begin{align*}
\bra{1,m'}J_{x}\ket{1,m}&= \frac{\hbar}{\sqrt{2}}\begin{pmatrix}0 & 1 & 0\\1 & 0 & 1\\0 & 1 & 0\end{pmatrix}\\\\
\bra{1,m'}J_{y}\ket{1,m}&= \frac{\hbar}{i\sqrt{2}}\begin{pmatrix}0 & 1 & 0\\-1 & 0 & 1\\0 & -1 & 0\end{pmatrix}\\\\
\bra{1,m'}J_{z}\ket{1,m}&= \hbar\begin{pmatrix}1 & 0 & 0\\0 & 0 & 0\\0 & 0 & -1\end{pmatrix}\\
\end{align*}$$
- Esta é a representação associada a atuar com operadores diferenciais nos harmónicos esféricos com $\ell=1$ (os harmónicos $Y_{1}^{\pm1}(\theta,\varphi),Y_{1}^{0}(\theta,\varphi)$)

> Podemos usar a mesma lógica para deduzir estas matrizes: $$(m',m)=\begin{pmatrix}(-1,-1) & (0,-1) & (1,-1)\\(-1,0) & (0,0) & (1,0)\\(-1,1) & (0,1) & (1,1)\end{pmatrix}$$
>     - E temos, para $J_{x}$ ($\langle j,m'|J_{x}|j,m\rangle= \frac{\hbar}{2}[\sqrt{j(j+1)-m(m+1)}\delta_{m',m+1} + \sqrt{j(j+1)-m(m-1)}\delta_{m',m-1}]$):
>         - no canto superior esquerdo temos $m'=m=-1$. Logo, nenhum dos deltas $\delta_{m',m-1},\delta_{m',m+1}$ será não nulo.
>         - no elemento no centro da linha superior temos $m'=0,m=-1$. Teremos $\delta_{m',m+1}=1$ e o termo fica ($m=-1$): $\langle j,m'|J_{x}|j,m\rangle= \frac{\hbar}{2}\sqrt{j(j+1)-m(m+1)}\delta_{m',m+1}=\frac{\hbar}{2}\sqrt{2}=\frac{\hbar}{\sqrt{2}}$ 
>     - Para $J_{y}$ funciona tudo de forma idêntica. Contrariamente ao caso de $j=\frac{1}{2}$, deixamos o $i$ de fora da matriz. Os sinais negativos em alguns termos devem-se unicamente à equação dos elementos da matriz de $J_{y}$
>     - Para $J_{z}$ simplesmente aplicamos a forma. Temos elementos não nulos na diagonal, onde $m=m'$. A exceção a isto é o ponto em que $m=0$, porque o elemento será $m\hbar=0\cdot\hbar=0$.

## Comentário sobre Grupo das Rotações
### $j=0$
- Estado invariante perante a ação do grupo das rotações (porque temos simetria esférica): $R=e^{- \frac{i}{\hbar}\vec{\theta}\cdot\vec{J}}=\mathbb{1}$

### $j= \frac{1}{2}$
- Vimos atrás que
$$\sigma_{x}=\begin{pmatrix}0 & 1\\1 & 0\end{pmatrix} \quad \quad;\quad \quad \sigma_{y}=\begin{pmatrix}0 & -i\\i & 0\end{pmatrix} \quad \quad;\quad \quad \sigma_{z}= \begin{pmatrix}1 & 0\\0 & -1\end{pmatrix}$$
- Ora, no grupo das rotações teremos
$$R_\vec{\theta}= e^{- \frac{i}{\hbar}\vec{\theta}\cdot\vec{S}}=e^{- \frac{i}{\hbar}\vec{\theta}\cdot \frac{\vec{\sigma}}{2}}=\sum\limits_{n=0}^{+\infty} \frac{1}{n!}\left(-i \vec{\theta}\cdot\frac{\vec{\sigma}}{2}\right)^{n}$$
em que $\vec\sigma=(\sigma_{x},\sigma_{y},\sigma_{z})$ (Não sei o que acontece ao $\hbar$)

- Tendo 2 vetores $\vec{A},\vec{B}$ e usando as propriedades das matrizes de Pauli, é possível deduzir:
$$(\vec{\sigma}\cdot\vec{A})(\vec{\sigma}\cdot\vec{B})=(\vec{A}\cdot\vec{B})\mathbb{1}+i\vec{\sigma}(\vec{A}\times\vec{B})$$
- Mais especificamente, se considerarmos $\vec{A}=\vec{B}=\vec{u}$ (sendo este um vetor unitário) obtemos $(\vec{\sigma}\cdot\vec{u})^{2}=\mathbb{1}$. Ou seja, vemos que $$(\vec{\sigma}\cdot\vec{u})^{n}=\begin{cases}
\mathbb{1} & ; & n~~par \\
\vec{\sigma}\cdot\vec{u} & ; & n~~ímpar
\end{cases}$$
- Assim, considerando uma rotação $\vec{\theta}=\theta\vec{u}$ temos:
$$\begin{align*}
R_\vec{\theta}&= \sum\limits_{n=0}^{\infty} \frac{1}{n!}\left(-i \vec{\theta}\cdot\frac{\vec{\sigma}}{2}\right)^{n}\\
&= \sum\limits_{\substack{n=0\\ (par)}}^{\infty}\frac{(-i \frac{\theta}{2})^{n}}{n!} +\sum\limits_{\substack{n=0\\ (ímpar)}}^{\infty}\frac{(-i \frac{\theta}{2})^{n}}{n!}\vec{\sigma}\cdot\vec{u}\\
&= \cos\left(\frac{\theta}{2}\right)\mathbb{1} - i \sin \left(\frac{\theta}{2}\right)(\vec{\sigma}\cdot\vec{u})\\
&= \cos\left(\frac{\theta}{2}\right)\mathbb{1} - i \sin \left(\frac{\theta}{2}\right)(u_{x}\sigma_{x}+u_{y}\sigma_{y}+u_{z}\sigma_{z})\\
&= \cos\left(\frac{\theta}{2}\right)\mathbb{1} - i \sin \left(\frac{\theta}{2}\right)\left[\begin{pmatrix}0 & u_{x}\\ u_{x} & 0 \end{pmatrix} + \begin{pmatrix}0 & -iu_{y}\\ iu_{y} & 0\end{pmatrix} +\begin{pmatrix}u_{z} & 0\\ 0 & -u_{z}\end{pmatrix}\right]\\
&= \begin{pmatrix}\cos\frac{\theta}{2}-i\sin\frac{\theta}{2}u_{z} & (-iu_{x}-u_{y})\sin\frac{\theta}{2} \\
(-iu_{x}+u_{y})\sin\frac{\theta}{2} & \cos\frac{\theta}{2}+i\sin\frac{\theta}{2}u_{z}\end{pmatrix}
\end{align*}$$

- Sendo que $R_{2\pi\vec{u}}=-\mathbb{1}$ e para $R_{4\pi\vec{u}}=\mathbb{1}$. Ou seja, apenas ao rodar $4\pi$ voltamos aos valores iniciais.
- Esta representação 2x2 constitui a menor representação da álgebra $[J_{i},J_{j}]=i\hbar\varepsilon_{ijk}J_{k}$.

### $j=1$
- Vimos atrás que podemos escrever os harmónicos esféricos em termos das componentes do vetor na esfera unitária: $\frac{\vec{r}}{r}=\frac{(x,y,z)}{r}$
- E vimos no início da cadeira que $Y_{1}^{-1}= \sqrt{\frac{3}{8\pi}} \sin\theta e^{-i\phi}$, $Y_{1}^{0}= \sqrt{\frac{3}{4\pi}} \cos\theta$. Ora, podemos escrever estas equações como
$$Y_{1}^{\pm1}(\theta,\phi)=\mp\sqrt{\frac{3}{8\pi}}\frac{x\pm iy}{r} \quad \quad;\quad \quad Y_{1}^{0}(\theta,\phi)=\sqrt{\frac{3}{4\pi}}\frac{z}{r}$$
- Podemos pegar nestas 2 equações, reorganizá-las e obtemos
$$\begin{align*}
\sqrt{\frac{8\pi}{3}}r(Y_{1}^{1}-Y_{1}^{-1})&= -2x\\
\sqrt{\frac{8\pi}{3}}r(Y_{1}^{1}+Y_{1}^{-1})&= -2iy\\
\sqrt{\frac{4\pi}{3}}rY_{1}^{0}&= z
\end{align*}$$
- Ou seja, podemos establecer uma mudança de base entre a base cartesiana $\{\ket{x},\ket{y},\ket{z}\}$ e a base $\{\ket{1,-1},\ket{1,0},\ket{1,1}\}$:
$$\begin{pmatrix}\ket{x} \\ \ket{y} \\ \ket{z}\end{pmatrix}=\sqrt{\frac{2\pi}{3}}r \begin{pmatrix}-1 & 0 & 1 \\ i & 0 & i \\ 0 & \sqrt{2} & 0\end{pmatrix}\begin{pmatrix}\ket{1,1} \\ \ket{1,0} \\ \ket{1,-1}\end{pmatrix}$$
- Podemos determinar os elementos da matriz do momento angular:
$$\begin{align*}
\langle x_{k}|J_{i}|x_{\ell}\rangle&= \sum\limits_{m,m'=1}\langle x_{k}|1m'\rangle \langle 1m'|J_{i}|1m\rangle \langle 1m|x_{\ell}\rangle\\
&= \sqrt{\frac{3}{8\pi}} \frac{1}{r} \begin{pmatrix}-1 & 0 & 1\\ -i & 0 & -i\\ 0 & \sqrt{2} & 0\end{pmatrix}\sum\limits_{m,m'=1}\langle 1m'|J_{i}|1m\rangle \sqrt{\frac{2\pi}{3}}r \begin{pmatrix}-1 & i & 0\\ 0 & 0 & \sqrt{2}\\ 1 & i & 0\end{pmatrix}
\end{align*}$$
em que 
![[mom angular.png]]

- Conforme as matrizes de $J_{x},J_{y},J_{z}$ obtidas atrás para $j=1$ obtemos:
$$\langle x_{k}|J_{x}|x_{\ell}\rangle=\frac{\hbar}{\sqrt{2}} \frac{1}{2}\begin{pmatrix}-1 & 0 & 1\\ -i & 0 & -i\\ 0 & \sqrt{2} & 0\end{pmatrix}\begin{pmatrix}0 & 1 & 0\\1 & 0 & 1 \\0 & 1 & 0\end{pmatrix}\begin{pmatrix}-1 & i & 0\\ 0 & 0 & \sqrt{2}\\ 1 & i & 0\end{pmatrix}=i\hbar \begin{pmatrix}0 & 0 & 0\\0 & 0 & -1\\0 & 1 & 0\end{pmatrix}$$
e podemos obter para as outras componentes:
$$\begin{align*}
\langle x_{k}|J_{y}|x_{\ell}\rangle&= i\hbar \begin{pmatrix}0 & 0 & 1\\0 & 0 & 0 \\-1 & 0 & 0\end{pmatrix}\\\\
\langle x_{k}|J_{z}|x_{\ell}\rangle&= i\hbar\begin{pmatrix}0 & -1 & 0\\1 & 0 & 0\\0 & 0 & 0\end{pmatrix}
\end{align*}$$

- Voltemos às rotações e consideremos uma rotação nos z: $$R_{\theta\hat{z}}= e^{-\frac{i}{\hbar}\vec{\theta}\cdot\vec{J}}=e^{- \frac{i}{\hbar}\theta J_{z}}=\sum\limits_{n=0}^{\infty}\frac{(-i\theta)^{n}}{n!} \left(\frac{J_{z}}{\hbar}\right)^{n}$$
- Se formos multiplicando a matriz $J_{z}$ obtida acima por si própria podemos obter:
$$\left(\frac{J_{z}}{\hbar}\right)^{2}=\begin{cases}
\dfrac{J_{z}}{\hbar}  & ; & n~~ímpar \\\\
\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0\\0 & 0 & 0\end{pmatrix} & ; & n~~par
\end{cases}$$
e temos:
$$R_{\theta\hat{z}}=\mathbb{1}+\sum\limits_{\substack{n=1\\(ímpar)}}^{\infty}\frac{(-i\theta)^{n}}{n!}i \begin{pmatrix}0 & -1 & 0\\1 & 0 & 0\\0 & 0 & 0\end{pmatrix}+\sum\limits_{\substack{n=2\\(par)}}^{\infty}\frac{(-i\theta)^{n}}{n!}\begin{pmatrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & 0\end{pmatrix}$$

## 4.2 - Spin Intrínseco
### STERN-GERLACH
![[stern gerlach.png]]
- Temos um feixe de átomos de Prata a atravessar um campo magnético não uniforme.

- Se analisarmos o problema de forma clássica, os átomos são neutros e temos que $\vec{F}=q(\vec{E}+\vec{v}\times\vec{B})=\vec{0}$
- Assim, os átomos interagem com o campo devido à geração de um momento dipolar magnético. Para um dipolo perfeito temos:
$$\begin{align*}
\vec{\mu}&= IA\hat{n}=\frac{qv}{2\pi r}\pi r^{2} \hat{n}=\frac{q}{2}vr\hat{n}=\\
&= \frac{q}{2m}rmv\hat{n}=\frac{q}{2m}\vec{r}\times\vec{p}=\frac{q}{2m}\vec{L}=\\
&= \frac{q\hbar}{2m}\frac{\vec{L}}{\hbar}=\mu_{B} \frac{\vec{L}}{\hbar} 
\end{align*}$$
(em que $\mu_{B}$ é o magnetão de Bohr)

- No caso de um átomo com spin esta equação fica:
$$\vec{\mu}=-g \mu_{B}\frac{\vec{S}}{\hbar}$$
($g=1$ para um dipolo perfeito)

- Temos ainda que o vetor do momento dipolar magnético tende a alinhar-se com o vetor $\vec{B}$. Temos que o torque aplicado num dipolo magnético é $\tau=\vec{\mu}\times\vec{B}$. Quando um torque destes é aplicado num dipolo, ele tende a *precessar* (o seu eixo oscila em torno do campo lentamente, imagina o eixo da terra consoante ele orbita o sol). Assim, o Momento Dipolar irá variar no tempo devido a esse torque:
$$\begin{align*}
\frac{d\vec{S}}{dt}&= \vec{\mu}\times\vec{B}\\
&= -g\mu_{B} \frac{\vec{S}}{\hbar}\times\vec{B}
\end{align*}$$
considerando o módulo de $\vec{S}$ constante e que este vetor apenas oscila na direção $\theta$ (na realidade estamos a considerar que oscilações nas outras direções são desprezáveis em comparação):
$$\begin{align*}
S\sin\theta \frac{d\theta}{dt}&= g\mu_{B} \frac{1}{\hbar}SB\sin\theta\\
\frac{d\theta}{dt}&=\frac{g\mu_{B}B}{\hbar} 
\end{align*}$$

- A média temporal das componentes $\mu_{x},\mu_{y}$ é zero. Assim, a força que o campo $\vec{B}$ aplica num dipolo $\vec{\mu}$ é dada por
$$\vec{F}=\nabla(\vec{\mu}\cdot\vec{B})$$
e podemos considerar apenas a componente dos zz:
$$\vec{F}=\mu_{z}\nabla B_{z}$$
e assumindo que o campo na região em estudo é apenas não constante nos zz ($\partial_{x}B_{x}=0,\partial_{y}B_{y}=0$):
$$\vec{F}=\mu_{z}\frac{\partial B_{z}}{\partial z}\hat{z}$$

- Ora, na experiência de Stern-Gerlach, o desvio nos xx que a partícula apresenta no final é uma medida do momento magnético na direção zz.
- Para um feixe não polarizado, teríamos $u_{z}$ igualmente distribuido entre os valores $-|\vec{\mu}|,|\vec{\mu}|$. Isto resultaria num padrão uniforme para a dispersão das partículas. No entanto, observamos *2 picos*. Aqui a física clássica falha!

- O facto de haver 2 picos claros significa que $\mu_{z}=g\mu_{B}\frac{S_{z}}{\hbar}$ apenas tem 2 valores possíveis. A interpretação da mecânica quântica: cada átomo de Ag tem 1 eletrão desemparelhado. Ora, o momento magnético de um átomo resulta do momento angular do eletrão livre.
- Assim, como $S_{z}$ apenas pode tomar 2 valores, o subespaço $\mathscr{E}_{j}$ de momento angular tem $j=\frac{1}{2}$, de modo que temos os valores próprios $S_{z}=\pm\frac{\hbar}{2}$
- Como o momento angular orbital só pode ter valores inteiros, os resultados desta experiência indicam que o eletrão tem um grau de liberdade interno, descrito pelo estado $\mathscr{E}_{j}~,~j=\frac{1}{2}$ associado ao Spin Intríseco (ou seja, a experiência mostra que o grau de liberdade não pode ter a ver com o momento angular orbital). Temos então o estado $\ket{s,m}$ com $s=\frac{1}{2}~,~m=\pm \frac{1}{2}$. Podemos então definir:
$$\ket{\tfrac{1}{2},\tfrac{1}{2}} \equiv \ket{\uparrow} \quad \quad;\quad \quad \ket{\tfrac{1}{2},- \tfrac{1}{2}}\equiv \ket{\downarrow}$$
temos:
$$\begin{align*}
S^{2}\ket{\uparrow}&= \hbar^{2}s(s+1)\ket{\uparrow}=\frac{3\hbar^{2}}{4}\ket{\uparrow}\\
S^{2}\ket{\downarrow}&= \frac{3\hbar^{2}}{4}\ket{\downarrow}\\
S_{z}\ket{\uparrow}&= + \frac{\hbar}{2}\ket{\uparrow}\\
S_{z}\ket{\downarrow}&= - \frac{\hbar}{2}\ket{\downarrow}
\end{align*}$$
e podemos escrever as matrizes:
$$S_{x}=\frac{\hbar}{2}\sigma_{x} \quad \quad;\quad \quad S_{y}=\frac{\hbar}{2}\sigma_{y} \quad \quad ;\quad \quad S_{z}=\frac{\hbar}{2}\sigma_{z}$$

- Por fim, temos que um eletrão tem um *momento magnético intrínseco* (associado ao spin):
$$\vec{\mu_{S}}=- g_{s}\frac{\mu_{B}}{\hbar}\vec{S} \quad \quad;\quad g_{s}=2$$
e temos o momento magnético gerado pelo momento angular orbital
$$\vec{\mu_{\ell}}=- g_{\ell}\frac{\mu_{B}}{\hbar}\vec{L} \quad \quad;\quad g_{\ell}=1$$
sendo que, de modo geral temos
$$\vec{\mu}=\vec{\mu_{\ell}}+\vec{\mu_{S}}$$

## Spin de Eletrão
- Atrás vimos as variáveis $\vec{r},\vec{p}$ associadas aos operadores $R,P$ que obedecem às relações de comutação $[R_{i},P_{j}]=i\hbar \delta_{ij}$ e atuam no espaço $\mathscr{E}_\vec{r}$.
- Vamos agora ver como se pode acrescentar graus de liberdade assoaciados ao spin intrínseco. O operador do spin obedece à álgebra: $$[S_{i},S_{j}]=i\hbar \varepsilon_{ijk}S_{k}$$
e atua no espaço $\mathscr{E}_{s}$
- Ora, esta necessidade de "acrescentar" os graus de liberdade simplesmente resulta do facto que o espaço de fase completo $\mathscr{E}$ é simplesmente a junção dos 2 subespaços (orbital e de spin): $\mathscr{E}=\mathscr{E}_\vec{r}\otimes\mathscr{E}_{s}$. Para deifnir uma base usamos um CCOC *que inclua operadores de spin* (por atuarem em espaços diferentes, operadores orbitais e de spin comutam!)

- Um eletrão com spin sujeito a um campo elétrico e magnético terá um hamiltoniano do tipo:
$$\hat{H}=\frac{(\hat{\vec{P}}-q \vec{A}(\hat{\vec{R}},t))^{2}}{2m}+ q \phi(\hat{\vec{R}},t)- \vec{\mu_{S}}\cdot\vec{B}$$
temos que (sendo $g_{s}=2$) $$\vec{\mu_{S}}=- g_{s}\frac{\mu_{B}}{\hbar}\vec{S}=- \frac{2}{\hbar}\frac{q\hbar}{2m}\vec{S}=-2\frac{q\hbar}{2m} \frac{\vec{\sigma}}{2}=-\frac{q\hbar}{2m}\vec{\sigma}$$
e o Hamiltoniano fica:
$$\hat{H}=\frac{1}{2m}\left[(\hat{\vec{P}}-q\vec{A}(\hat{\vec{R}},t))^{2}-q\hbar \vec{\sigma}\cdot\vec{B} \right]+q\phi(\hat{\vec{R}},t)$$
- Podemos então escolher $\hat{\vec{R}},\hat{S_{z}}$ (podiamos escolher $S_{z}$ e $P,H,L_{z},L^{2}$) e temos a base de estados:
$$\ket{\vec{r},\sigma}=\ket{\vec{r}}\otimes\ket{\sigma} \quad \quad;\quad \quad \{\ket{\sigma}\}=\{\ket{\uparrow},\ket{\downarrow}\}$$
em que
$$\begin{align*}
R\ket{\vec{r},\sigma}&= \vec{r}\ket{\vec{r},\sigma}\\
S_{z}\ket{\vec{r},\uparrow}&= \frac{\hbar}{2}\ket{\vec{r},\uparrow}\\
S_{z}\ket{\vec{r},\downarrow}&= - \frac{\hbar}{2}\ket{\vec{r},\downarrow}
\end{align*}$$
a base é ortogonal:
$$\langle \vec{r'},\sigma'|\vec{r},\sigma\rangle=\delta(\vec{r}-\vec{r'})\delta_{\sigma \sigma'}$$
e segue a relação de fecho
$$\sum\limits_{\sigma}\int d^{3}r |\vec{r},\sigma\rangle\langle\vec{r},\sigma|=\int d^{3}r|\vec{r},\uparrow\rangle\langle\vec{r},\uparrow|+\int d^{3}r|\vec{r},\downarrow\rangle\langle\vec{r},\downarrow|=1$$
- Podemos escrever qualquer estado nesta base
$$\ket{\psi}=\mathbb{1}\ket{\psi}=\sum\limits_{\sigma}\int d^{3}r |\vec{r},\sigma\rangle\langle\vec{r},\sigma|\psi\rangle= \int d^{3}r ~\psi_{\uparrow}(\vec{r})\ket{\vec{r},\uparrow}+\psi_{\downarrow}(\vec{r})\ket{\vec{r},\downarrow}$$
e podemos então definir um estado com
$$\psi(\vec{r})=\begin{pmatrix}\psi_{\uparrow}(\vec{r}) \\ \psi_\downarrow (\vec{r})\end{pmatrix}$$
- Para bras podemos escrever algo idêntico:
$$\bra{\psi}=\bra{\psi}\mathbb{1}=\sum\limits_{\sigma}\int d^{3}r ~\langle\psi|\vec{r},\sigma\rangle\langle\vec{r},\sigma|= \int d^{3}r ~\psi_{\uparrow}^{*}(\vec{r})\bra{\vec{r},\uparrow}+\psi_{\downarrow}^{*}(\vec{r})\bra{\vec{r},\downarrow}$$
em que podemos escrever
$$\psi^{\dagger}(\vec{r})=\begin{pmatrix}\psi_{\uparrow}^{*}(\vec{r}) &  \psi_{\downarrow}^{*}(\vec{r})\end{pmatrix}$$

- Podemos fazer o produto escalar destes 2 estados (bra e ket):
$$\begin{align*}
\langle \varphi|\psi\rangle&= \langle \varphi|\biggr(\sum\limits_{\sigma} \int d^{3}r|\vec{r},\sigma\rangle\langle\vec{r}, \sigma|\biggr)|\psi\rangle\\
&= \int d^{3}r ~\varphi_{\uparrow}^{*}(\vec{r})\psi_{\uparrow}(\vec{r})+\varphi_{\downarrow}^{*}(\vec{r})\psi_{\downarrow}(\vec{r})\\
&= \int d^{3}r ~\varphi^{\dagger}(\vec{r})\psi(\vec{r}) 
\end{align*}$$
e temos a condição de normalização:
$$\langle \psi|\psi\rangle=\int d^{3}r ~\psi^{\dagger}(\vec{r})\psi(\vec{r})=1$$

- Nos casos mais simples o Hamiltoniano atua separadamente nas variáveis orbitais e de spin. Ou seja:
$$\hat{H}=H_{\vec{r}}(R,P)\otimes \mathbb{1}_{S}+ \mathbb{1}_{\vec{r}}\otimes H_{S}(S)$$
- Assim é útil considerar estados que resultam do produto tensorial de estados $\in\mathscr{E}_\vec{r},\in\mathscr{E}_S$:
$$\begin{align*}
\ket{\psi}=\ket{\varphi}\otimes \ket{\sigma}
\end{align*}$$
em que $$\begin{align*}
\ket{\varphi}&= \int d^{3}r~ \langle\vec{r}|\varphi\rangle\ket{\vec{r}} ~~~~\in\mathscr{E}_\vec{r}\\
\ket{\sigma}&= a_{\uparrow}\ket{\uparrow}+a_{\downarrow}\ket{\downarrow}~~~~\in\mathscr{E}_{S} 
\end{align*}$$
e fica
$$\psi(\vec{r})=\varphi(\vec{r})\times \begin{pmatrix}a_{\uparrow}\\a_{\downarrow}\end{pmatrix}$$
- Podemos ter  operadores que atuam nos 2 espaços ao mesmo tempo:
$$\begin{align*}
\vec{S}\cdot\vec{L}&= \frac{\hbar}{2}(\sigma_{x}L_{x}+\sigma_{y}L_{y}+\sigma_{z}L_{z})\\
&= \frac{\hbar}{2}\begin{pmatrix}L_{z} & L_{x}-iL_{y}\\ L_{x}+iL_{y} & -L_{z}\end{pmatrix}
\end{align*}$$
(recordar mais uma vez que $\sigma_{i}$ **não** são escalares - são as matrizes de Pauli - pelo que na equação acima apenas substituimos diretamente as matrizes)
- Temos então que este operador atua na forma
$$\vec{S}\cdot \vec{L}\ket{\psi}=\hbar \begin{pmatrix}L_{z} & L_{x}-iL_{y}\\ L_{x}+iL_{y} & -L_{z}\end{pmatrix} \begin{pmatrix}\psi_{\uparrow}(\vec{r})\\ \psi_{\downarrow}(\vec{r})\end{pmatrix}$$

## 4.3 - Adição Momento Angular
- Temos os operadores de momento angular $J_{1},J_{2}$ que atuam em espaços distintos $\mathscr{E}_{1},\mathscr{E}_{2}$. Sendo $J_{i}$ operadores de momento angular genérico, estes podem ser operadores de momento angular orbitar de partículas diferentes, ou até podemos ter $J_{1}=\vec{L},J_{2}=\vec{S}$ da mesma partícula.

- Consideremos que no espaço $\mathscr{E}_{i}$ temos a base $\{\ket{\alpha_{i},j_{i},m_{i}}\}$ que é base própria de $J_{i}^{2},J_{iz}$ e em que (vamos ignorar $\alpha_{i}$):
$$\begin{align*}
J_{i}^{2}\ket{j_{i},m_{i}}&= \hbar^{2}j_{i}(j_{i}+1)\ket{j_{i},m_{i}}\\
J_{iz}\ket{j_{i},m_{i}}&= \hbar m_{i}\ket{j_{i},m_{i}}\\
J_{i\pm}\ket{j_{i},m_{i}}&= \hbar\sqrt{j_{i}(j_{i}+1)-m_{i}(m_{i}\pm 1)} \ket{j_{i},m_{i}\pm1} \quad;\quad (J_{i\pm}=\tfrac{1}{2}(J_{ix}\pm iJ_{iy}))
\end{align*}$$

- Podemos então definir uma base do espaço $\mathscr{E}_{1}\otimes\mathscr{E}_{2}$: $\{\ket{\alpha_{1},j_{1},m_{1}}\otimes\ket{\alpha_{2},j_{2},m_{2}}\}$. Esta base será uma base própria dos operadores $J_{1}^{2},J_{1z},J_{2}^{2},J_{2z}$. Como já vimos atrás, não será de esperar que estes operadores comutem com $\hat{H}$ nem que formem um CCOC.

- Podemos definir o operador *momento angular total* $J=J_{1}+J_{2}$. Este deverá obedecer a 
    - $[J_{k},J_{\ell}]=i\hbar \varepsilon_{k\ell m}J_{m}$
    - $[J^{2},J_{k}]=0$
- Temos ainda que qualquer componente $J_{1k}$ comuta com $J_{1}^{2}$ e com $J_{2}^{2}$. Também será esse o caso de $J_{2k}$. Assim $J_{k}=J_{1k}+J_{2k}$ deverá obedecer a 
    - $[J_{k},J_{1}^{2}]=0$
    - $[J_{k},J_{2}^{2}]=0$
- Por fim, $J^{2}=J_{1}^{2}+J_{2}^{2}+J_{1}\cdot J_{2}=J_{1}^{2}+J_{2}^{2}+J_{1x}J_{2x}+J_{1y}J_{2y}+J_{1z}J_{2z}$ irá comutar com $J_{1}^{2},J_{2}^{2}$ porque todas as componentes $J_{1k},J_{2k}$ o fazem. Fica: 
    - $[J^{2},J_{1}^{2}]=0$
    - $[J^{2},J_{2}^{2}]=0$

### Mais Grupo das Rotações
- Vimos atrás que este grupo atua num estado $\ket{\psi}\in\mathscr{E}_{\vec{r}}$ é descrito por $R_\vec{\theta} = e^{- \frac{i}{\hbar}\vec{\theta}\cdot\vec{L}}$
- No caso de um eletrão com spin o momento angular total é $\vec J=\vec L+\vec S$ e temos o operador de rotação a atuar no espaço $\mathscr{E}_{\vec{r}}\otimes\mathscr{E}_{S}$:
$$R_\vec{\theta} = e^{- \frac{i}{\hbar}\vec{\theta}\cdot\vec{J}}=e^{- \frac{i}{\hbar} \vec{\theta}\cdot(\vec{L}+\vec{S})}=e^{- \frac{i}{\hbar}\vec{\theta}\cdot\vec{L}}e^{- \frac{i}{\hbar}\vec{\theta}\cdot\vec{S}}$$
- Consideremos um estado $\ket{\psi}$ descrito com um 2-spinor (um objeto matemático usado na física teórica e que é representado por 2 componentes complexas) de componentes $\psi_{\sigma}(\vec{r})=\langle \vec{r},\sigma|\psi\rangle$. Quando uma rotação é aplicada a este estado ficamos com um estado $\psi'$:
$$\begin{align*}
\psi_{\sigma}'(\vec{r})&= \langle \vec{r},\sigma|\psi'\rangle=\langle \vec{r},\sigma|R|\psi\rangle\\
&= \sum\limits_{\sigma'}\int d^{3}r'~ \langle \vec{r},\sigma|R|\vec{r'},\sigma'\rangle \langle \vec{r'},\sigma'|\psi\rangle\\
&= \sum\limits_{\sigma'}\int d^{3}r'~\langle \vec{r}|e^{- \frac{i}{\hbar}\vec{\theta}\cdot\vec{L}}|\vec{r'}\rangle \langle \sigma|e^{- \frac{i}{\hbar}\vec{\theta}\cdot\vec{S}}|\sigma'\rangle\langle \vec{r'},\sigma'|\psi\rangle
\end{align*}$$
e temos a expressão que nos dá as componente de $\ket{\psi}$ após a rotação.
- Podemos calcular estas componentes melhor:
    - $\langle \vec{r}|e^{- \frac{i}{\hbar}\vec{\theta}\cdot\vec{L}}|\vec{r'}\rangle=\langle R^{-1}\vec{r}|\vec{r'}\rangle=\delta(R^{-1}\vec{r}-\vec{r'})$
    - $\langle\sigma|e^{- \frac{i}{\hbar}\vec{\theta}\cdot\vec{S}}|\sigma'\rangle=R_{\sigma \sigma'}^{(S)}(\vec{\theta})$ (em que $R_{\sigma\sigma'}^{(S)}$ é a matriz que descreve a rotação $\sigma\to\sigma'$, e que é equivalente a atuar com o operador de rotação no operador spin). Vimos atrás que $R_{\sigma\sigma'}^{(S)}=\cos\frac{\theta}{2}\mathbb{1}-i\sin\frac{\theta}{2}\vec{\sigma}\cdot\frac{\vec{\theta}}{\theta}$ 
- E a equação final fica:
$$\begin{align*}
\psi_{\sigma}'(\vec{r})&= \sum\limits_{\sigma'}\int d^{3}r'~\langle \vec{r}|e^{- \frac{i}{\hbar}\vec{\theta}\cdot\vec{L}}|\vec{r'}\rangle \langle \sigma|e^{- \frac{i}{\hbar}\vec{\theta}\cdot\vec{S}}|\sigma'\rangle\langle \vec{r'},\sigma'|\psi\rangle\\
&= \sum\limits_{\sigma'}\int d^{3}r'~\delta(R^{-1}\vec{r}-\vec{r'})R_{\sigma\sigma'}^{(S)}(\vec{\theta})\psi_{\sigma'}(\vec{r'})\\
&= \sum\limits_{\sigma'}R_{\sigma\sigma'}^{(S)}(\vec{\theta})\psi_{\sigma'}(R^{-1}\vec{r})
\end{align*}$$
(isto é kinda equivalente à equação $\hat{R}_\vec{\theta}\psi(\vec{r})= \psi(R_{\theta}^{-1}\vec{r})$ obtida no início deste resumo)

- Vimos que a rotação nos deu um produto não trivial de componentes.
- Assim, invés da base $\ket{j_{1},j_{2},m_{1},m_{2}}$ de estados próprios de $J_{1}^{2},J_{2}^{2},J_{1z},J_{2z}$ será mais útil usar uma base $\ket{j_{1},j_{2},j,m}$ de estados próprios de $J_{1}^{2},J_{2}^{2},J^{2},J_{z}$. 
    - Vemos que esta base não é base própria de $J_{1z},J_{2z}$ porque $[J_{1z},J^{2}]\neq0,[J_{2z},J^{2}]\neq0$ (se escrevermos por extenso vemos que ficam termos como $[J_{1z},J_{1x}J_{2x}]\neq0$)
    - Continuamos a ter $[J^{2},J_{i}^{2}]=0$ e $[J_{z},J_{i}^{2}]=0$, pelo que a matriz de $J^{2},J_{z}$ só é $\neq0$ para estados com o mesmo $j_{1}$ ou o mesmo $j_{2}$.

- Assim, queremos saber como podemos passsar da base $\ket{j_{1},j_{2},m_{1},m_{2}}$ para a base $\ket{j_{1},j_{2},j,m}$. Temos logo 2 problemas:
    - Se fixarmos $j_{1},j_{2}$ que definem o estado $\mathscr{E}(j_{1},j_{2})=\mathscr{E}(j_{1})\otimes\mathscr{E}(j_{2})$ com dimensão $(2j_{1}+1)(2j_{2}+1)$, quais os valores possíveis de $j$?
    - Como podemos escrever $\ket{j_{1},j_{2},j,m}$ como uma combinação linear de estados de $\ket{j_{1},j_{2},m_{1},m_{2}}$?

## Valores Próprios de $J^{2},J_{z}$ no espaço $\mathscr{E}(j_{1},j_{2})$
- Iremos considerar que $j_{1}\ge j_{2}$

### Valores próprios de $J_{z}$
- Facilmente vemos que
$$J_{z}\ket{j_{1},j_{2},m_{1},m_{2}}=(J_{1z}+J_{2z})\ket{j_{1},j_{2},m_{1},m_{2}}=\hbar(m_{1}+m_{2})\ket{j_{1},j_{2},m_{1},m_{2}}$$
em que obtemos que $J_{z}$ tem o valor próprio $m=m_{1}+m_{2}$.
- Como $m_{i}=-j_{i},\dots,j_{i}$ temos que $m=-(j_{1}+j_{2}),\dots,(j_{1}+j_{2})$

#### Degenerescência
- Consideremos $j_{1}=2,j_{2}=1$. Temos $-2\le m_{1}\le2,-1\le m_{2}\le1$. Podemos representar estes pontos num gráfico:
![[degenerescencia nums quanticos.png]]
- As retas diagonais unem os pares $(m_{1},m_{2})$ que nos dão o mesmo $m=m_{1}+m_{2}$.
    - Para $m=3$ temos apenas 1 ponto: $m_{1}=2,m_{2}=1$. Temos o grau de degenerescência $g(m=3)=1$
    - Para $m=1$ (há um erro no desenho) temos 3 pontos: $(m_{1},m_{2})=(2,-1)(1,0)(0,1)$. Ou seja $g(m=1)=3$

- Podemos generalizar:
$$\begin{align*}
g(m=j_{1}+j_{2})&= 1\\
g(m=j_{1}+j_{2}-1)&= 2\\
g(m=j_{1}+j_{2}-2)&= 3\\
&\vdots\\
g(m=j_{1}-j_{2})&= 2j_{2}+1
\end{align*}$$
Para $-(j_{1}-j_{2})\le m< j_{1}-j_{2}$ temos $$g(m)=2j_{2}+1$$
Para $-(j_{1}+j_{2})\le m\le -(j_{1}-j_{2})$ usamos  $$g(m)=g(-m)$$
- No exemplo acima temos:
$$g(m)=\begin{cases}
1 & ; & m=3 \\
2 & ; & m=2 \\
3 & ; & -1\le m \le1 \\
2 & ; & m=-2 \\
1 & ; & m=-3
\end{cases}$$

### Valores próprios de $J^{2}$
- Se $j\in\mathscr{E}(j_{1},j_{2})$ então teremos $2j+1$ estados desse multipleto (dizemos multipleto porque $j=1$ seria um tripleto, etc).

- Vimos acima que $m=j_{1}+j_{2}$ apenas ocorre 1 vez ($g(m)=1$). Assim, este estado corresponde ao valor máximo de $J_{z}$ do multipleto com $j=j_{1}+j_{2}$
- O estado em que temos $m=j_{1}+j_{2}-1$ tem degenerescência $g=2$. Assim, podemos escrevê-lo como uma combinação linear associada ao multipleto com $j=j_{1}+j_{2}$ e como uma combinação associado a outro multipleto, com $j=j_{1}+j_{2}-1$
- O estado com $m=j_{1}+j_{2}-2$ tem degenerescência $g=3$. Teríamos combinações lineares assoaciadas ao multipletos $j=j_{1}+j_{2}~,~j=j_{1}+j_{2}-1~,~j=j_{1}+j_{2}-2$.
- E por aí fora até $m=j_{1}-j_{2}$. Aí passamos a ter degenerescência $g=2j_{2}-1$.
- E a partir de $m=-(j_{1}-j_{2})$ a degenerescência volta a descrecer até 1.

- Assim, os valores próprios $j$ serão:
$$j=j_{1}+j_{2}~~,~~ j_{1}+j_{2}-1 ~~,~~\dots~~,~~ |j_{1}-j_{2}|$$
- Podemos escreverr então:
$$\begin{align*}
\mathscr{E}(j_{1},j_{2})&= \mathscr{E}(j_{1})\otimes \mathscr{E}(j_{2})\\
&= \mathscr{E}(j_{1}+j_{2}) \oplus \mathscr{E}(j_{1}+j_{2}-1)\oplus\dots\oplus \mathscr{E}(|j_{1}-j_{2}|)
\end{align*}$$

## Vetores próprios de $J^{2}$ e $J_{z}$
- Considerando $j_{1},j_{2}$ fixos iremos escrever: $\ket{j_{1},j_{2},m}=\ket{j,m}$
- Vejamos como escrever o vetor próprio $\ket{j,m}$ na base $\ket{j_{1},j_{2},m_{1},m_{2}}$. Temos:
$$\ket{j,m}=\mathbb{1}\ket{j,m}=\sum\limits_{m_{1}=-j_{1}}^{j_{1}}\sum\limits_{m_{2}=-j_{2}}^{j_{2}}\ket{j_{1},j_{2},m_{1},m_{2}}\bra{j_{1},j_{2},m_{1},m_{2}}j,m\rangle$$
em que $\bra{j_{1},j_{2},m_{1},m_{2}}j,m\rangle$ são os **coeficientes de Clebsch-Gordon**. Normalmente usariamos uma tabela, mas veremos como se calculam estes coeficientes.

### Casos comuns
#### $j_{1}=j_{2}=\frac{1}{2}$
- Temos a base inicial $\ket{\tfrac{1}{2},\tfrac12, \sigma_{1},\sigma_{2}}$ associada às observáveis $S_{1}^{2},S_{2}^{2},S_{1z},S_{1z}$. Temos que $\sigma_{1}=\uparrow,\downarrow$ e $\sigma_{2}=\downarrow,\uparrow$. 
    - Temos 4 estados possíveis: $\uparrow\uparrow,\downarrow\downarrow,\uparrow\downarrow,\downarrow\uparrow$
- A base nova será $\ket{\tfrac12,\tfrac12,s,m}$ com $s=s_{1}+s_{2},s_{1}+s_{2}-1,\dots,|s_{1}-s_{2}|$. Temos $m=-s_{i},\dots,s_{i}$
    - Neste caso temos $s=1,0$ (sendo estes 2 valores possíveis, não 1=1,0)
    - Assim, para $s=1$ temos $m=-1,0,1$. Para $s=0$ temos $m=0$. Temos então 4 estados possíveis.
    - Podemos portanto representar os estados nesta base com $\ket{s,m}$ e omitir $j_{1},j_{2}$

- Podemos escreveresta mudança de base como:
$$\{ \ket{\uparrow\uparrow},\ket{\downarrow\downarrow},\ket{\uparrow\downarrow},\ket{\downarrow\uparrow}\} ~~\longrightarrow~~ \{\ket{1,1},\ket{1,0},\ket{1,-1},\ket{0,0}\}$$

#### Tripleto $\ket{1,m}$
- Temos logo o estado $\ket{1,1}=\ket{\uparrow\uparrow}$
- Podemos obter os restantes estados com $$J_{\pm}\ket{j,m}=\hbar\sqrt{j(j+1)-m(m\pm1)}\ket{j,m\pm1}$$
- E temos: $J_{-}\ket{1,1}=\hbar\sqrt{2}\ket{1,0}$. Mas podemos escrever $S_{-}=S_{1-}+S_{2-}$ e temos $S_{-}\ket{1,1}=(S_{1-}+S_{2-})\ket{\uparrow\uparrow}=\hbar\sqrt{\frac{3}{4} + \frac{1}{4}}(\ket{\downarrow\uparrow}+\ket{\uparrow\downarrow})$. Estes estados terão de ser equivalentes. Logo: $$\begin{align*}
\hbar\sqrt{2}\ket{10}&= \hbar(\ket{\downarrow\uparrow}+\ket{\uparrow\downarrow})\\
\ket{10}&= \frac{1}{\sqrt{2}}(\ket{\downarrow\uparrow}+\ket{\uparrow\downarrow})
\end{align*}$$
    - Aqui $S_{-}$ é o operador que baixa o spin total em 1 unidade. Para um sistema de 2 partículas, $S_{1-},S_{2-}$ são os operadores que baixam os spins das partículas 1 e 2 em uma unidade. Assim partindo do estado $\ket{\uparrow\uparrow}$ em que ambas as partículas têm spin 1/2 passamos a ter uma combinação dos 2 estados em que 1 das partículas tem spin 1/2 e a outra -1/2.

- Se continuarmos temos $J_{-}\ket{10}=\hbar\sqrt{2}\ket{1,-1}$. Por alguma razão, daqui obtemos $\ket{1,-1}=\ket{\downarrow\downarrow}$.

- Ou seja, para um tripleto ($s=1$) temos $$\begin{align*}
\ket{11}&= \ket{\uparrow\uparrow}\\
\ket{10}&= \tfrac1{\sqrt{2}}(\ket{\uparrow\downarrow} + \ket{\downarrow\uparrow})\\
\ket{1,-1}&= \ket{\downarrow\downarrow}
\end{align*}$$

#### Singleto $\ket{00}$
- Não faço ideia porquê, mas temos
$$\ket{00}=\tfrac{1}{\sqrt{2}}(\ket{\uparrow\downarrow} - \ket{\downarrow\uparrow})$$

### Caso Geral
- Como vimos acima:
$$\{\ket{j_{1},j_{2},m_{1},m_{2}}\}~~\longrightarrow~~ \{\ket{j_{1}+j_{2},m},\ket{j_{1}+j_{2}-1,m},\dots,\ket{|j_{1}-j_{2}|},m\}$$
Em que no estado inicial temos $m_{1}=-j_{1},\dots,j_{2}~~;~~ m_{2}=-j_{2},\dots,j_{2}$. 
Em cada estado novo $\ket{j,m}$ temos $m=-j,\dots,j$. Ou seja: $m=-(j_{1}+j_{2}),\dots,j_{1}+j_{2}~~;~~m=-(j_{1}+j_{2}-1),\dots,j_{1}+j_{2}-1~~;~~\dots$

- Podemos esquematizar isto como:
$$\mathscr{E}(j_{1})\otimes \mathscr{E}(j_{2})=\sum\limits_{\substack{\oplus\\ j=|j_{1}-j_{2}|}}^{j_{1}+j_{2}} \mathscr{E}(j)$$
- Para o multipolo $\mathscr{E}(j_{1}+j_{2})$ temos $$\ket{j=j_{1}+j_{2},m=j_{1}+j_{2}}=\ket{j_{1},j_{2},m_{1}=j_{1},m_{2}=j_{2}}$$
e podemos obter outros vetores des multipleto com $J_{-}=J_{1-}+J_{2-}$:
$$\begin{align*}
\ket{j_{1}+j_{2},j_{1}+j_{2}-1}&= J_{-}\ket{j_{1}+j_{2},j_{1}+j_{2}}\\
&= J_{1-}\ket{j_{1},j_{2},j_{1},j_{2}}+J_{2-}\ket{j_{1},j_{2},j_{1},j_{2}}\\
&= \sqrt{\frac{j_{1}}{j_{1}+j_{2}}}\ket{j_{1},j_{2},j_{1}-1,j_{2}}+ \sqrt{\frac{j_{2}}{j_{1}+j_{2}}}\ket{j_{1},j_{2},j_{1},j_{2}-1}\\
\end{align*}$$não percebi de onde vieram as constantes (raízes).

- Agora o multipleto $\mathscr{E}(j_{1}+j_{2}-1)$. Como vimos atrás, o $m$ máximo deste estado ($m=j_{1}+j_{2}-1$) terá degenerescência igual a 2. Assim, definimos:
$$\ket{j_{1}+j_{2}-1,j_{1}+j_{2}-1}=\alpha\ket{j_{1},j_{2},j_{1}-1,j_{2}}+\beta\ket{j_{1},j_{2},j_{1},j_{2}-1}$$
- Este estado deverá estar normalizado e ser ortogonal a $\ket{j_{1}+j_{2},j_{1}+j_{2}-1}$. Tal como acima, podemos obter os restantes estados usando sucessivamente $J_{-}=J_{1-}+J_{2-}$

- Por fim o multipleto $\mathscr{E}(j_{1}+j_{2}-2)$. O valor máximo de $m$ tem agora degenerescência 3. Fica:
$$\ket{j_{1}+j_{2}-2,j_{1}+j_{2}-2}=\alpha\ket{j_{1},j_{2},j_{1}-2,j_{2}}+\beta\ket{j_{1},j_{2},j_1-1,j_{2}-1}+\gamma\ket{j_{1},_{2},j_{1},j_{2}-2}$$
que tem qe ser normalizado e ortogonal a $\ket{j_{1}+j_{2},j_{1}+j_{2}-2},\ket{j_{1}+j_{2}-1,j_{2}+j_{2}-2}$.

- Prosseguindo assim podemos representar todos os estados $\ket{j,m}$ na base $\ket{j_{1},j_{2},m_{1},m_{2}}$.
