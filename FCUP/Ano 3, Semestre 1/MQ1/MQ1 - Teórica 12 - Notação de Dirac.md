# 3.2 - Notação de Dirac
- Quando temos um vetor, ele pode ser escrito conforme as suas componentes em diferentes sistemas de coordendas. No entanto, ele existe como um objeto geométrico, mesmo sem fazer referência ao sistema de coordendas escolhido.
- Similarmente, o estado de uma partícula é um vetor no espaço de estuados de uma partícula, $\mathcal{E}$.
- Assim, é útil definir uma notação e regras de cálculo vetorial que nos permita estudar situações conforme os graus de liberdade e não uma função de onda específica.

## KET
- Um elemento $|\alpha\rangle$ de $\mathcal{E}$ é chamado de **ket**. $\alpha$ é um conjunto de rótulos que permite identificar elementos em $\mathcal{E}$. Por exemplo:
$$\psi(\vec{r})\in \mathcal{F}~~\to~~ |\psi\rangle\in \mathcal{E}_\vec{r}$$
(de notar que dentro do ket apenas aparece $\psi$, sem o $\vec{r}$, porque apenas $\psi$ descreve o estado.)

### Produto Escalar
- A 2 kets associamos:$$(|\phi\rangle,|\psi\rangle)=\langle \phi|\psi\rangle$$
a que chamamos *produto escalar* e obdece às propriedades:
    1 - Conjugado : $(\varphi,\psi)=(\varphi,\psi)^{*}$
    2 - Linear no 1º argumento : $(\varphi, \lambda_{1}\psi_{1}+\lambda_{2}\psi_{2})=\lambda_{1}(\varphi,\psi_{1})+\lambda_{2}(\varphi,\psi_{2})$
    3 - Anti-linear no 2º argumento : $(\lambda_{1}\varphi_{1}+\lambda_{2}\varphi_{2},\psi)=\lambda_{1}^{*}(\varphi_{1},\psi)+\lambda_{2}^{*}(\varphi_{2},\psi)$

- No caso de $\mathcal{E}_\vec{r}$ temos:
$$(|\phi\rangle,|\psi\rangle)=\int d^{3}r~\psi^{*}(\vec{r})\psi(\vec{r})=\int d^{3}p~ \tilde \phi^{*}(\vec{p})\tilde \psi(\vec{p})$$

### Espaço Dual de $\mathcal{E}$ (não sei nada disto tb :D)
- Podemos definir um funcional linear que a cada ket $|\psi\rangle\in \mathcal{E}$ associa um número complexo:
$$\begin{align*}
\chi: \mathcal{E}&\longrightarrow \mathbb{C}\\
|\psi\rangle &\longrightarrow \chi(|\psi\rangle)
\end{align*}$$
em que se tem a propriedade
$$\chi(\lambda_{1}|\psi_{1}\rangle+\lambda_{2}|\psi_{2}\rangle)=\lambda_{1}\chi(|\psi_{1}\rangle) + \lambda_{2}\chi(|\psi_{2}\rangle)$$
sendo que o espaço destes funcionais se denomina de *espaço dual* de $\mathcal{E}$ e se escreve como $\mathcal{E}^{*}$

## BRA
- É o nome que damos a um elemento do espaço vetorial $\mathcal{E}^{*}$. Escrevemos como $\langle \psi|$.

### Correspondência entre Kets e Bras
- Usando o produto escalar conseguimos relacionar a cada ket um bra:
$$\begin{align*}
\langle\psi| : \mathcal{E} &\longrightarrow \mathbb{C}\\
|\psi\rangle &\longrightarrow (|\psi\rangle,|\psi\rangle)=\langle \phi|\psi\rangle
\end{align*}$$
em que esta relação é anti-linear. Ou seja:
$$\lambda_{1}|\psi_{1}\rangle+\lambda_{2}|\psi_{2}\rangle~~\longrightarrow ~~ \lambda_{1}^{*}\langle\psi_{1}|+\lambda_{2}^{*}\langle\psi_{2}|$$

### Aplicação
- Conhecendo $|\psi\rangle,|\phi\rangle$ e o produto escalar $\langle \phi|\psi\rangle$, podemos aplicar as propriedades do produto escalar:
![[propriedades prod escalar.png]]

- Iremos usar elementos $\notin\mathcal{E}$ como KETs. Por exemeplo:
$$|k\rangle\to \frac{e^{i \vec{k}\cdot \vec{r}}}{(2\pi)^\frac{3}{2}}$$
não é uma função de quadrado somável, no entanto permite definir um BRA $\langle k|\in \mathcal{E}^{*}$
Podemos concluir isto porque temos:
$$\langle k|\psi\rangle= \frac{1}{(2\pi)^{\frac{3}{2}}} \int d^{3} r~ e^{-i \vec{k}\cdot \vec{r}} \psi(\vec{r})$$

## Representação de Bases na notação de Dirac
- No caso de uma base discreta $u_{f}(\vec{r})$ representamos com $|u_{n}\rangle$ ou $|n\rangle$
- No caso de uma base contínua $\omega_{\alpha}(\vec{r})$ representamos com $|\omega_{\alpha}\rangle$ ou $|\alpha\rangle$

Verifiquemos as propriedades:
**Base Ortonormada**
$$\langle u_{n}|u_{m}\rangle= \delta_{nm} \quad \quad ; \quad \quad \langle \omega_{\alpha}|\omega_{\alpha'}\rangle=\delta(\alpha-\alpha')$$

**Expansão de $\psi$**
$$|\psi\rangle= \sum_{n}c_{m}|u_{n}\rangle \quad\quad;\quad \quad |\psi\rangle = \int d \alpha~ c(\alpha)|\omega_{\alpha}\rangle$$
**Projeção de $\psi$ na base**
$$\langle u_{n}|\psi\rangle=c_{n} \quad \quad;\quad \quad \langle \omega_{\alpha}|\psi\rangle=c(\alpha)$$
**Produto escalar em componentes**
$$\langle \phi|\psi\rangle=\sum_{n} b_{n}^{*}c_{n} \quad \quad;\quad \quad \langle \phi|\psi\rangle=\int d \alpha ~b^{*}(\alpha)c(\alpha)$$
**Relação de Fecho**
$$\sum\limits_{n} |u_{n}\rangle\langle u_{n}|=1 \quad \quad;\quad \quad \int d\alpha~ |\omega_{\alpha}\rangle\langle \omega_{\alpha}|=1$$

# 3.3 - Operações Lineares
- Um operador linear é uma aplicação em $\mathcal{F}$ do tipo:
$$\begin{align*}
\hat{A}: \mathcal{F} &\longrightarrow \mathcal{F}\\
\psi(\vec{r}) &\longrightarrow \psi'(\vec{r})=\hat{A}\psi(\vec{r})
\end{align*}$$
em que, na notação de dirac, temos a propriedade:
$$\hat{A} (\lambda_{1}|\psi_{1}\rangle+ \lambda_{2}|\psi_{2}\rangle) = \lambda_{1} \hat{A}(|\psi_{1}\rangle)+\lambda_{2} \hat{A}(|\psi_{2}\rangle)$$

## Produtos de Operadores
- Tendo $\hat{A}, \hat{B}$ dois operadores lineares. O seu produto será:
$$(\hat{A}\hat{B})\psi(\vec{r})=\hat{A}\left[ \hat{B} (\psi(\vec{r}))\right]$$
- Em geral, $\hat{A}\hat{B}\neq \hat{B}\hat{A}$. Temos então o **comutador** dos 2 operadores:
$$[\hat{A},\hat{B}]=\hat{A}\hat{B}-\hat{B}\hat{A}$$
> EXEMPLO
> - Vejamos com os operadores $\hat{u},\hat{D}_{u}$ (coordenada $u$ e derivada nessa):
> $$[\hat{u},\hat{D}_{u}] \psi(\vec{r})=\left( u \frac{\partial}{\partial u} - \frac{\partial}{\partial u}u \right)\psi(\vec{r})=u \frac{\partial  \psi}{\partial u} - \frac{\partial}{\partial u}\left(u \psi \right)=u \frac{\partial  \psi}{\partial u} - \psi - u\frac{\partial \psi}{\partial u}=-\psi $$
> logo $[\hat{u},\hat{D_{u}}]=-1$

## Elementos de matriz de um operador
- Dada a ação de $\hat{A}$ num ket $|\psi\rangle$, podemos usar o produto escalar para definir a ação do operador no espaço dural / num bra $\langle \psi|$
- Vejamos a ação de $\hat{A}$ no bra:
$$(\langle \phi|\hat{A})|\psi\rangle=\langle \phi|(\hat{A}|\psi\rangle)=\langle \phi|\hat{A}|\psi \rangle$$
sendo este um *elemento da matriz de A*.