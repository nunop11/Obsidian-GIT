# Quantificação Canónica
- Temos um sistema clássico com variáveis canónicas $\{ q^{i},p^{i}\}$. 
- Esse sistema passa a ser descrito na mecânica quântica por um vetor $|\psi\rangle\in\mathcal{E}$.
- Impomos então relações canónicas de comutação entre os observáveis relacionados às variáveis $q^{i}$ e os momentos conjugados $p^{i}$:
$$[\hat{q}^{i},\hat{q}^{j}]=0 \quad;\quad [\hat{p}^{i},\hat{p}^{j}]=0 \quad;\quad [\hat{q}^{i},\hat{p}^{j}]=i\hbar \delta^{ij}$$

- Desta forma, qualquer grandeza física escrita em função das variáveis canónicas  $\mathcal{A}(q^{i},p^{i},t)$ dá origem a um operador do tipo:
$$\hat{A}(\hat{q}^{i},\hat{p}^{i},t)$$
- Este processo é ambiguo porque $\hat{q}^{i},\hat{p}^{i}$ não comutam.
- Nos apontamentos tem exemplos.

## Representações de $|\vec{r}\rangle,|\vec{p}\rangle$ 
- A posição e o momento são variáveis incompatíveis e normalmente usamos estados próprios destes operadores para expressar a função de onda.
- Na base de Dirac obtemos:
$$\psi_\vec{r_{0}}(\vec{r})=\delta(\vec{r}-\vec{r_{0}})\longrightarrow |\vec{r_{0}}\rangle$$
$$\psi_{\vec{p}}(\vec{r})= \frac{1}{(2\pi\hbar)^{\frac{3}{2}}} e^{i \frac{\vec{p}\cdot\vec{r}}{\hbar}} \longrightarrow |\vec{p}\rangle$$
em que se tem as mesmas propriedades que já vimos muitas vezes:
![[bases da posicao e do momento.png]]

- Podemos projetar $|\vec{p}\rangle$ na base das posições:
$$\langle\vec{r}|\vec{p}\rangle=\int d^{3}r~\delta(\vec{r}-\vec{r'})\frac{1}{(2\pi\hbar)^{\frac{3}{2}}} e^{i \frac{\vec{p}\cdot\vec{r}}{\hbar}}=\frac{1}{(2\pi\hbar)^{\frac{3}{2}}} e^{i \frac{\vec{p}\cdot\vec{r}}{\hbar}}$$

- Podemos ainda estudar a projeção de $\vec{p}|\psi\rangle$ na base $|u\rangle$ ($u$ é uma das posições de $\vec{r}$):
$$\begin{align*}
\langle u|\hat{p}|\psi\rangle&= \langle u|\mathbb{1}|\hat{p}|\psi\rangle\\
&= \int dp\langle u|p\rangle\langle p|\hat{p}|\psi\rangle \quad \quad \textsf{(relação de fecho em 1D)}\\
&= \int dp\langle u|p\rangle ~p~ \langle p|\psi\rangle\\
&= \int dp~ \frac{1}{(2\pi\hbar)^{\frac{3}{2}}} e^{i \frac{\vec{p}\cdot\vec{r}}{\hbar}} ~p~ \tilde \psi(p)\\
&= \frac{\hbar}{i} \frac{d}{du} \int dp \frac{1}{(2\pi\hbar)^{\frac{3}{2}}} e^{i \frac{\vec{p}\cdot\vec{r}}{\hbar}}\tilde \psi(p)\\
&= \frac{\hbar}{i} \frac{d}{du} \psi(u) \quad \quad \textsf{(Fourier Inversa)}\\
&= \frac{\hbar}{i} \frac{d}{du} \langle u|\psi\rangle
\end{align*}$$
ou, de forma direta:
$$\langle u|(\hat{p}|\psi\rangle)=\frac{\hbar}{i} \frac{d}{du} \langle u|\psi\rangle$$
isto é portanto a ação do operador $\hat{p}$ sobre um estado $\psi$ na base $|u\rangle$.

- É análogo mostrar que a ação de $\hat{u}$ na base de $|\vec{p}\rangle$ é dada por 
$$\langle p|(\hat{u}|\psi\rangle)= i\hbar \frac{d}{dp} \langle p|\psi\rangle$$

- Vejamos então a ação do comutador $[\hat{u},\hat{p}]$ sobre um estado na base $|u\rangle$:
$$\begin{align*}
\langle u|[\hat{u},\hat{p}]|\psi\rangle&= \langle u|\hat{u}\hat{p}-\hat{p}\hat{u}|\psi\rangle\\
&= u \langle u|\hat{p}|\psi\rangle - \frac{\hbar}{i} \frac{d}{du} \langle u|\hat{u}|\psi\rangle
\end{align*}$$
(aqui em ambos os termos temos algo parecido. No 2º temos $\langle u|\hat{p}|\phi\rangle=\frac{\hbar}{i} \frac{d}{du}\langle u|\phi\rangle$ em que $\phi=\hat{x}|\psi\rangle$)
$$\begin{align*}
&= u \frac{\hbar}{i} \frac{d}{du} \langle u|\psi\rangle - \frac{\hbar}{i} \frac{d}{du} (u\langle u|\psi\rangle)\\
&= i\hbar \langle u|\psi\rangle
\end{align*}$$
(Não percebi o último termo)

- Como $|\psi\rangle$ é um estado arbitrário podemos escrever:
$$\langle u|[\hat{u},\hat{p}]|\psi\rangle=i\hbar \langle u|\psi\rangle \longrightarrow [\hat{u},\hat{p}]=i\hbar \mathbb{1}$$

# 4 - Teoria Geral do Momento Angular
## 4.0.1 - Grupo SU(2) e representações
### Grupo das translações
- No exercício 9 da folha 3 obtemos que o operador momento linear está relacionado com o operador translação $\hat{T}_{\vec{a}}|\vec{r}\rangle=|\vec{r}+\vec{a}\rangle$.
- Foi então obtido que:
$$\hat{T}_{\vec{a}}=\exp\left(-i\vec{a}\cdot \frac{\hat{\vec{p}}}{\hbar}\right)\simeq 1-i \frac{\vec{a}\cdot\hat{\vec{p}}}{\hbar}=1-\vec{a}\cdot\nabla ~~~~;~~~~ \hat{\vec{p}}=\frac{\hbar}{i}\nabla$$
- Os operadores translação $\hat{T}_{\vec{a}}$ formam o grupo das translações, com as propriedades:
$$\begin{align*}
\hat{T}_\vec{a}\hat{T}_{\vec{b}}&= \hat{T}_{\vec{a}+\vec{b}}  \quad \quad \quad \quad \quad \quad\textsf{(produto)}\\
\hat{T}_{\vec{a}}(\hat{T}_\vec{b}\hat{T}_{\vec{c}})&= (\hat{T}_{\vec{a}}\hat{T}_\vec{b})\hat{T}_{\vec{c}} \quad \quad \quad \quad~\textsf{(associativo)}\\
\hat{T}_{\vec{a}}\mathbb{1}&= \hat{T}_{\vec{a}} \quad \quad \quad \quad \quad \quad \quad\textsf{(elemento neutro)}\\
\left(\hat{T}_{\vec{a}}\right)^{-1}&= \left(\hat{T}_{-\vec{a}} \right) \quad \quad \quad \quad \quad ~\textsf{(inverso)}
\end{align*}$$

- Sendo $\vec{a}$ um vetor infinitesimal, temos que as translações infinitesimais são descritas por $\hat{\vec{p}}$

- Podemos escrever:
$$\hat{T}_{\vec{a}}= e^{-i\vec{a}\cdot \hat{\frac{\vec{p}}{\hbar}}}=\lim\limits_{n\to\infty} \left(1- i \frac{\vec{a}\cdot\hat{\vec{p}}}{n\hbar} \right)^{n}$$
ou seja, podmemos definir uma transformação finita como uma sequência infinita de transformações infinitesimais.
- Podemos então definir $\hat{p}_{i}$ como sendo os *geradores das translações*.

- Grupos em que os elementos são identificados por parâmetros contínuos (neste caso $\vec{a}$) são chamados *grupos de Lie*.

### Grupo das Rotações
- Sendo $R$ uma amtriz podemos escrever o grupo das rotações em $\mathbb{R}^{3}$:
$$\vec{r'}=R \vec{r} ~\Longleftrightarrow~ x'^{i}=R^{i}_{j}x ^{j} ~\Longleftrightarrow~ \begin{pmatrix}x_{1}'\\x_{2}'\\x_{3}'\end{pmatrix}=\begin{pmatrix}R_{11} & R_{12} & R_{13}\\R_{21} & R_{22} & R_{23} \\ R_{31} & R_{32} & R_{33}\end{pmatrix}\begin{pmatrix}x_{1} \\ x_{2} \\ x_{3}\end{pmatrix}$$
- Estas rotações são caraterizadas por $|\vec{r'}|^{2}=|\vec{r}|^{2}$ e temos:
$$\begin{align*}
x'^{i}x'^{j}= R_{j}^{i}x^{j}R_{k}^{j}x^{k}&= x^ix^{i}\\
(R^{T})_{i}^{j}x^{j}R_{k}^{j}x^{k}&= x^{i}x^{i}\\
(R^{T})_{i}^{j}R_{k}^{j}x^{j}x^{k}&= \delta_{j}^{i}\delta_{k}^{i}x^{j}x^{k}\\
(R^{T}R)_{jk}x^{j}x^{k}&= \delta_{jk}x^{j}x^{k}\\
R^{T}R&= \mathbb{1}
\end{align*}$$
por outras palavras, a matriz de rotação é *ortogonal*!

- Assim temos:
$$\det(R^{T}R)=1 \Leftrightarrow (\det R)^{2}=1 \Leftrightarrow \det R=\pm1$$
    - Se $\det (R)=-1$ temos reflexões ($\vec{r}\to-\vec{r}$
    - Rotações têm $\det (R)=1$. Esta matriz 3x3 com determinante unitário é o grupo SO(3)

- No grupo das translanções tinhamos o parâmetro contínuo $\vec{a}$. No das Rotações temos o parâmetro $\vec{\theta}$ que indica a direção e ângulo de rotação. Assim:
$$\hat{R}_\vec{\theta}|\vec{r}\rangle=|R_\vec{\theta}\vec{r}\rangle$$
e para um estado representado na base das posições:
$$\begin{align*}
\hat{R}_\vec{\theta}\psi(\vec{r})&= \langle\vec{r}|\hat{R}_\vec{\theta}|\psi\rangle\\
&= \langle\vec{r}|\hat{R}_\vec{\theta}|\mathbb{1}|\psi\rangle\\
&= \langle \vec{r}|\hat{R}_\vec{\theta}|\int d^{3}r'~|\vec{r'}\rangle\langle\vec{r'}|\psi\rangle\\
&= \int d^{3}r' \langle \vec{r}|\hat{R}_\vec{\theta}|\vec{r'}\rangle \langle \vec{r'}|\psi\rangle\\
&= \int d^{3}r' \langle\vec{r}|R_\vec{\theta}\vec{r'}\rangle \psi(\vec{r'})\\
&= \int d^{3}r'~ \delta(\vec{r}-R_{\theta}\vec{r'})\psi(\vec{r'})\\
&= \int d^{3}u'~\delta(\vec{r}-\vec{u})\psi(R_{\theta}^{-1}\vec{u'})  \quad \quad \quad (\vec{u'}=R_{\theta}\vec{r'}\Leftrightarrow \vec{r'}=R_{\theta}^{-1} \vec{u'})\\
&= \psi(R_{\theta}^{-1}\vec{r})
\end{align*}$$
