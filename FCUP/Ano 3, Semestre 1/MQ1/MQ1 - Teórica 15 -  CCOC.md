# Conjunto Completo de Observáveis que Comutam (CCOC)
**Teorema** - Se 2 observáveis $\hat{A},\hat{B}$ comutam ($[\hat{A},\hat{B}]=0$) podemos construir uma base ortonormada do espaço de estado com vetores próprios de $\hat{A}$ e $\hat{B}$ (sendo neste caso as grandezas $\mathcal{A},\mathcal{B}$ compatíveis)

## Demonstração
### $\Rightarrow$ (Comumtam $\to$ Têm base própria comum)
- Consideremos $|u_{n}^{i}\rangle$ a base dos vetores próprios de $\hat{A}$:
$$\hat{A}|u_{n}^{i}\rangle=a_{n}|u_{n}^{i}\rangle \quad\quad;\quad \substack{n=1,2,\dots\\i=1,\dots,g_{n}}$$
em que, tal como já fizemos atrás, $n$ é a direção do vetor e $g_{n}$ o seu grau de degenerescência nessa direção.
- Sabemos que $$\langle u_{n}^{i}|\hat{B}|u_{m}^{j}\rangle=0~~~~~~ (n\neq m)$$
pelo que $\hat{B}$ nesta base é diagonal por blocos:
![[Pasted image 20231116100016.png]]
- Se o valor próprio $a_{n}$ é não degenerado $\xi_{n}$ tem dimensão 1 (é 1 só número) e temos que o vetor próprio correspondente, $|u_{n}\rangle$, também é vetor próprio de $\hat{B}$.
- Se $a_{n}$ é degenerado, a matriz que represeneta $\hat{A}$ no subespaço $\xi_{n}$ é $a_{n}\mathbb{1}_{n}$.
- Na base $|u_{n}^{i}\rangle$, o operador $\hat{B}$ tem elementos $$\beta_{ij}^{n}=\langle u_{n}^{i}|\hat{B}|u_{n}^{j}\rangle \quad \quad;\quad i,j=1,\dots,g_{n}$$
mas $\hat{B}$ é uma observável logo é hermítico. Assim: $\beta_{ij}^{n}=(\beta_{ij}^{n})^{*}$ e torna-se obrigatório que o bloco seja diagonalizável. 
- Podemos então achar uma vase $|v_{n}^{i}\rangle$ em que $\hat{B}$ também é diagonal: $\hat{B}|v_{n}^{i}\rangle=b_{n}^{i}|v_{n}^{i}\rangle$.
- É então possível encontrar em cada subespaço próprio de $\hat{A}$ uma base de vetores próprios comum a $\hat{A}$ e $\hat{B}$.

### $\Leftarrow$ (Existe base própria comum $\to$ Então comutam)
- Consideremos que $\hat{A},\hat{B}$ têm uma base própria comum: $|u_{n,p}^i\rangle$ tal que:
$$\begin{align*}
\hat{A}|u_{n,p}^{i}\rangle&= a_{n}|u_{n,p}^{i}\rangle\\
\hat{B}|u_{n,p}^{i}\rangle&= b_{p}|u_{n,p}^{i}\rangle\\
\end{align*}$$
e podemos calcular:
$$\begin{align*}
\hat{A}|\hat{B}|u_{n,p}^{i}\rangle=b_{p}\hat{A}|u_{n,p}^{i}\rangle =b_{p}a_{n}|u_{n,p}^{i}\rangle\\
\hat{B}|\hat{A}|u_{n,p}^{i}\rangle=a_{n}\hat{B}|u_{n,p}^{i}\rangle =a_{n}b_{p}|u_{n,p}^{i}\rangle
\end{align*}$$
logo $$[\hat{A},\hat{B}]|u_{n,p}^{i}\rangle=0$$
ou seja, comutam!

## CCOC em si
- As observáveis $\hat{A},\hat{B},\hat{C},\dots$formam um CCOC se forem o número mínimo de Observáveis tais que:
    1. Todas as observáveis comutam entre si.
    2. Sabendo so valores própriós de $\hat{A},\hat{B},\hat{C},\dots$ determina-se 1 único vetor próprio comum.
- Um CCOC gera então uma base para o espaço de estados de um sistema físico. Os elementos dessa base são identificados pelos valores próprios correspondentes $|a_{n}b_{n},c_{n},\dots\rangle$ 

# Princípio de Incerteza
- Recordemos a definição de variância: $$\sigma_{A}^{2}=\langle \hat{A}-\langle \hat{A} \rangle\rangle^{2}=\langle \hat{A}^{2}\rangle-\langle\hat{A}\rangle^{2}$$
- E para um estado $|\psi\rangle$ temos então a variância de um operador $\hat{A}$:
$$\begin{align*}
\sigma_{A}^{2}&= \langle \psi|(\hat{A}-\langle\hat{A}\rangle)^{2}|\psi\rangle\\
&= \langle \psi|(\hat{A}-\langle\hat{A}\rangle)(\hat{A}-\langle\hat{A}\rangle)|\psi \rangle\\
&= \underbrace{\langle \psi|(\hat{A^{\dagger}}-\langle\hat{A}\rangle)}_{\langle f|}\underbrace{(\hat{A}-\langle\hat{A}\rangle)|\psi \rangle}_{|f\rangle}\to \sigma_{A}^{2}=\langle f|f\rangle\\
\end{align*}$$
- Para um operador $\hat{B}$ podemos repetir este procedimento e temos:
$$\sigma_{B}^{2}=\langle g|g\rangle ~~~~~;~~|g\rangle=(\hat{B}-\langle\hat{B}\rangle)|\psi\rangle$$

- Usemos a desigualdade de Schwarz:
$$\sigma_{A}^{2}\sigma_{B}^{2}=\langle f|f\rangle\langle g|g\rangle\ge |\langle f|g\rangle|^{2}$$
- Sendo $z$ um qualquer número complexo, temos:
$$|z|^{2}=\text{Re}(z)^{2}+\text{Im}(z)^{2}\ge \text{Im}(z)^{2}= \left[\frac{1}{2i}(z-z^{*})\right]^{2}$$
definindo $z=\langle f|g\rangle$ temos:
$$\sigma_{A}^{2}\sigma_{B}^{2}\ge \left(\frac{1}{2i} (\langle f|g\rangle-\langle g|f\rangle) \right)^{2}$$
- Podemos calcular $\langle f|g\rangle$ diretamente:
$$\begin{align*}
\langle f|g\rangle&= \langle \psi|(\hat{A}-\langle\hat{A}\rangle)(\hat{B}-\langle\hat{B}\rangle)\rangle|\psi\rangle\\
&= \langle\psi|(\hat{A}\hat{B}-\hat{A}\langle\hat{B}\rangle-\langle\hat{A}\rangle\hat{B}+\langle\hat{A}\rangle\langle\hat{B}\rangle|\psi \rangle\\
&= \langle\psi|\hat{A}\hat{B}|\psi\rangle - \langle\hat{A}\rangle\langle\hat{B}\rangle- \langle\hat{A}\rangle\langle\hat{B}\rangle+\langle\hat{A}\rangle\langle\hat{B}\rangle\\
&= \langle \hat{A}\hat{B}\rangle - \langle\hat{A}\rangle\langle\hat{B}\rangle
\end{align*}$$
(em que se usou múltiplas vezes $\langle\psi|\hat{O}|\psi\rangle=\langle\hat{O}\rangle$)

- Analogamente:
$$\langle g|f\rangle=\langle\hat{B}\hat{A}\rangle-\langle\hat{B}\rangle\langle\hat{A}\rangle$$
- De onda resulta:
$$\langle\ f|g\rangle-\langle g|f\rangle=\langle[\hat{A},\hat{B}]\rangle$$
- E daqui resulta a **Fora Geral do Princípio de Incerteza**:
$$\sigma_{A}^{2}\sigma_{B}^{2}\ge \left(\frac{1}{2i} \langle[\hat{A},\hat{B}]\rangle \right)^{2}$$
em que se $\langle\hat{A},\hat{B}\rangle\neq0$ temos que as grandezas $\mathcal{A},\mathcal{B}$ são incompatíveis, porque não é possível medi-las em simultâneo com precisão arbitrária.
- De notar que, apesar de termos um $i$ dentro do quadrado, ele irá sempre ser anulado pelo valor médio do comutador, ficando-se sempre com $\sigma_{A}^{2}\sigma_{B}^{2}\ge \textsf{valor positivo}$

- Vejamos um exemplo:
    - Temos os operadores posição $\hat{X}=x$ e momento $\hat{P}=\frac{\hbar}{i} \frac{\partial}{\partial x}$ (em 1-D).
    - Temos então: $$[\hat{X},\hat{P}]\psi(x)=\frac{\hbar}{i}\left[x \frac{d\psi}{dx}- \frac{d}{dx}\left( x \psi\right) \right]=i\hbar \psi(x)$$
    - Logo: $$\sigma_{x}^{2}\sigma_{p}^{2}\ge\left(\frac{1}{2i} i\hbar \right)^{2}=\left(\frac{\hbar}{2}\right)^{2} ~~\to~~ \sigma_{x}\sigma_{p}\ge \frac{\hbar}{2}$$ AKA princípio da Incerteza de Heisenberg !!!!

# Evolução Temporal
- Recordemos a equação de Schrödinger na notação de Dirac AKA Postulado 6 da Mecânica Quântica:
$$i\hbar \frac{d}{dt}|\psi(t)\rangle=\hat{H}(t)|\psi(t)\rangle$$
- Conhecendo a condição inicial $|\psi(t_{0})\rangle$, a evolução temporal desse sistema é completamente determinística. A mecânica quântica apresenta um caráter aleatório, que se manifesta ao fazer medições do sistema.
- Temos ainda que esta equação diferencial é linear, pelo que podemos aplicar o princípio da sobreposição.
- A probabilidade total do sistema é constante no tempo:
$$\begin{align*}
\frac{d}{dt}\langle\psi|\psi\rangle&= \frac{d\langle\psi|}{dt}|\psi\rangle + \langle\psi|\frac{d|\psi\rangle}{dt}\\
&= \frac{i}{\hbar}\langle\psi|\hat{H}^{\dagger} - \frac{i}{\hbar} \hat{H}^{\dagger}|\psi\rangle\\
&= 0
\end{align*}$$
(em que se aplicou diretamente a equação do Postulado 6)

- Podemos então escrever:
$$\frac{\partial}{\partial t}|\psi(\vec{r},t)|^{2}=-\nabla \cdot \vec{\mathcal{J}} \quad \quad;\quad \quad \mathcal{J}=\frac{i\hbar}{2m}(\psi^{*}\nabla^{*}\psi-\psi\nabla^{*}\psi^{*})$$

- E a evolução temporal do valor médio de uma grandeza $\mathcal{A}$ será:
$$\begin{align*}
\frac{d}{dt}\langle\hat{A}\rangle&= \frac{d}{dt} \langle\psi|\hat{A}|\psi\rangle\\
&= \left(\frac{d}{dt}\langle\psi| \right)\hat{A}|\psi\rangle + \langle\psi| \frac{\partial\hat{A}}{\partial t}|\psi\rangle + \langle\psi|\hat{A} \left(\frac{d}{dt} |\psi\rangle \right)\\
&= \left(\frac{i}{\hbar} \langle \psi|\hat{H}^{\dagger} \right)\hat{A}|\psi\rangle + \langle\psi| \frac{\partial\hat{A}}{\partial t}|\psi\rangle + \langle\psi|\hat{A} \left( \frac{i}{\hbar}\hat{H}|\psi\rangle \right)\\
&= \frac{i}{\hbar} \langle\psi|(\hat{H}\hat{A}-\hat{A}\hat{H})|\psi\rangle+\left\langle \frac{\partial\hat{A}}{\partial t}\right\rangle
\end{align*}$$
e temos a fórmula:
$$\frac{d}{dt}\langle\hat{A}\rangle=\left\langle \frac{\partial\hat{A}}{\partial t}\right\rangle + \frac{i}{\hbar} \langle[\hat{H},\hat{A}]\rangle$$
que é equivalente ao que tinhamos na mecânica clássica: $\frac{df}{dt}=\frac{\partial f}{\partial t}+\{H,f\}$
- Desta forma, é evidente que se um operador comutar com o Hamiltoniano ($[\hat{H},\hat{A}]=0$) e não depender explicitamente do tempo, então o valor da sua grandeza física é constante.
