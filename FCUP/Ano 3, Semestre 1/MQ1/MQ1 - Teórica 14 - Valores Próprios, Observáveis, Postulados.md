# Vetores e Valores Próprios
- Um estado $|\psi\rangle$ é um vetor/ket próprio de um operador $\hat{A}$ se:
$$\hat{A}|\psi\rangle=\lambda|\psi\rangle \quad \quad;\quad \lambda\in\mathbb{C}$$
- O conjunto de valores de $\lambda$ que torna esta igualdade verdade é denominado de **espetro do operador** $\hat{A}$.
- Naturalmente, se $|\psi\rangle$ é um vetor próprio também $\alpha|\psi\rangle$ o será, com o mesmo valor próprio $\lambda$. Não existe ambiguidade porque consideramos os estados normalizados ($\langle \psi|\psi\rangle=1$)
- Se tivermos estados $\{|\psi_{i}\rangle\}~,~(i=1,\dots,g)$ linearmente independentes e todos com o *mesmo valor próprio*, dizemos que o valor próprio é **degenerado** com **grau de degenerescência** $g$.

### Calcular Valores próprios
- Consideramos uma base discreta $\{|u_{m}\rangle\}$ 
- Projetamos a equação dos vetores/valores próprios nesta base:
$$\begin{align*}
\langle u_{m}|\hat{A}|\psi\rangle&= \lambda \langle u_{m}|\psi\rangle\\
\sum\limits_{n} \langle u_{m}|\hat{A}\underbrace{|u_{n}\rangle \langle u_{n}|}_{=\mathbb{1}} \psi\rangle&= \lambda \langle u_{m}|\psi\rangle
\end{align*}$$
- Ora, temos 2 projeções de $\psi$:
    - $\langle u_{n}|\psi\rangle=C_{n}$
    - $\langle u_{m}|\psi\rangle=C_{m}$
- E temos o elemento da matriz do operador: $A_{mn}=\langle u_{m}|\hat{A}|u_{n}\rangle$

- E ficamos com:
$$\sum\limits_{n}A_{mn}C_{n}=\lambda C_{m} \to \sum\limits_{n}(A_{mn}-\lambda \delta_{mn})C_{n}=0$$
ora, isto não passa de um sistema de equações lineares e temos:
$$\det(A_{mn}-\lambda \delta_{mn})=0$$
e (para uma base com $N$ dimensões) isto fica na forma:
$$\begin{vmatrix}
A_{11}-\lambda &A_{12} &\dots &A_{1N}\\
A_{21} &A_{22}-\lambda &\dots &A_{2N}\\
\vdots &\vdots &\ddots & \vdots \\ 
A_{N1} &A_{N2} &\dots &A_{NN}-\lambda
\end{vmatrix}=0$$

o que nos dá um polinómio de grau $N$ em $\lambda$ que terá $N$ raízes complexas (**valores próprios**) $\lambda_{i} ~(i\in\mathbb{N})$ que podem ser degeneradas. Este resultado é independente da base usada.

### Calcular Vetores Próprios
- Acima vimos como obter os valores próprios $\lambda_{i}$. Ora, para obter os vetores próprios $|\psi_{i}\rangle=\sum_{n}c_{n}|u_{n}\rangle$ basta substituir os valores na equação:
$$\sum\limits_{n}(A_{mn}-\lambda_{i}\delta_{mn})=0$$ 
- Para $\lambda_{i}$ não degenerados nos dá $N-1$ equações independentes. Ora, temos $N$ coeficientes $c_{n}$ num vetor próprio. O coeficiente restante é dado por $\langle \psi_{i}|\psi_{i}\rangle=1$
- Se $\lambda_{i}$ tem degenerescência $g$ temos $N-g$ equações independentes, que nos permitem escrever $g$ vetores linearmente dependentes.

## Observáveis
- Recordemos algumas propriedades que vimos acima:
**i)** Se um operador $\hat{A}$ for hermítico, os seu valores próprios são **reais**: $$\hat{A}|\psi\rangle=\lambda|\psi\rangle ~~\to~~ \begin{align*}
\langle \psi|\hat{A}|\psi\rangle=\lambda \langle\psi|\psi\rangle &= \lambda\\
\langle\psi|\hat{A^{\dagger}}|\psi\rangle=\langle \psi|\hat{A}|\psi\rangle^{*}&= \lambda^{*}
\end{align*}$$
Para um operador hermítico temos $\hat{A}=\hat{A^{\dagger}}$, ou seja: $\lambda=\lambda^{*} ~\to~ \lambda\in\mathbb{R}$

**ii)** Dois vetores próprios com *valores próprios distintos* são **ortogonais**:
    - Consideremos os estados $\psi,\phi$ tais que $$\hat{A}|\psi\rangle=\lambda|\psi\rangle~~;~~ \hat{A}|\phi\rangle=\nu|\phi\rangle ~~~~ (\lambda\neq\nu)$$
    - Podemos escrever: $$\lambda\langle\phi|\psi\rangle=\langle\phi|(\hat{A}|\psi\rangle)=(\langle\phi|\hat{A})|\psi\rangle=\nu^{*}\langle\phi|\psi\rangle=\nu\langle\phi|\psi\rangle$$
    - E temos $\lambda\langle\phi|\psi\rangle=\nu\langle\phi|\psi\rangle$. Ora, temos que $\lambda\neq\nu$, pelo que a única forma de esta igualdade se veficar é se $\langle\phi|\psi\rangle=0$, ou seja, os **vetores são ortogonais**.

- Ora, já vimos que se o espaço de estados $\mathcal{E}$ tiver dimensão *finita*, os vetores próprios do operador hermítico formam uma base completa de vetores de $\mathcal{E}$.
- Já se o espaço de estados $\mathcal{E}$ tiver dimensão *infinita* isto pode não ser verdade. Nesse caso definimos um **Observável** como operador hermítico se os seus vetores próprios formarem uma base em $\mathcal{E}$.

- Consideremos o conjunto de valores próprios $\{\lambda_{i}~,~n\in\mathbb{N}\}$ do operador hermítico $\hat{A}$, que têm degenerescência $g_{n}$. Os vetores próprios correspondentes são $|\psi_{n}^{i}\rangle_{n\in\mathbb{N}}^{i=1,\dots,g_{n}}$ que são independentes com valor próprio $\lambda_n$
- Anteriormente mostramos que, para um operador hermítico, temos 
    - $\langle\psi_{m}^{i}|\psi_{n}^{j}\rangle=0$
    - $\langle\psi_{n}^{i}|\psi_{n}^{j}\rangle=\delta_{ij}$ (sendo estes 2 vetores normalizados que têm o mesmo valor próprio)

- Ou seja, podemos escrever:
$$\langle \psi_{m}^{i}|\psi_{n}^{j}\rangle=\delta_{mn}\delta^{ij}$$
- Ora, se este sistema de equações formar uma base completa AKA satisfazer a condição de fecho:
$$\sum\limits_{n}\sum\limits_{i=1}^{g_{n}} |\psi_{n}^{i}\rangle\langle \psi_{n}^{i}|=1$$
então $\hat{A}$ **é um observável**.

- Assim, de forma geral, para um sistema discreto temos que os vetores próprios são descritos por $$\hat{A}|\psi_{n}^{i}\rangle=\lambda_{n}|\psi_{n}^{i}\rangle ~~~~ (n\in\mathbb{N}~,~ i=1,\dots,g_{n})$$
e formam um sistema ortonormado:
$$\langle\psi_{m}^{i}|\psi_{n}^{j}\rangle=\delta_{mn}\delta^{ij}$$

- Para um sistema contínuo temos os vetores:
$$\hat{A}|\psi_{\nu}\rangle=\lambda(\nu)|\psi_{\nu}\rangle~~~~ (\nu_{1}<\nu<\nu_{2})$$
que também formam um sistema ortonormado:
$$\langle \psi_{\nu}|\psi_{\nu'}\rangle=\delta(\nu-\nu')$$

- Ora, um Observável pode ter um espetro contínuo, discreto ou com partes de ambos. Assim, a relação de Fecho é:
$$\sum\limits_{n}\sum\limits_{i=1}^{g_{n}}|\psi_{n}^{i}\rangle\langle\psi_{n}^{i}|+\int d \nu|\psi_{\nu}\rangle\langle\psi _{\nu}|=1$$

# 3.4 - Postulados da Mecânica Quântica
## Mecânica Clássica
1. O estado do sistema no instante $t_{0}$ é descrito por $N$ coordenadas generalizadas $q_{i}(t_{0})$ e os seus momentos conjugados $p_{i}(t_{0})$. 
2. Se o estado for conhecido em $t_{0}$, então todas as quantidades físicas ficam totalmente definidas. 
3. A Evolução temporal do sistema é determinada pelas equações canónicas: $$\dot{q_{i}}=\frac{\partial H}{\partial p_{i}} \quad;\quad \dot{p_{i}}=-\frac{\partial H}{\partial q_{i}}$$
Com os valores iniciais e estas equações, todo o sistema fica predefinido para $t>t_{0}$.

## Mecânica Quântica
>==**_Postulado 1:_**== Num instante $t_{0}$ o estado do sistema quântico é descrito por um ket $|\psi\rangle$ que pertence ao espaço de estados $\mathcal{E}$

>==**_Postulado 2:_**== Todas as quantidades físicas $\mathcal{A}$ que podem ser medidas são descritas por um operador $\hat{A}$ que atua no espaço $\mathcal{E}$. A este operador chamamos *observável*

> ==**_Postulado 3:_**== Os resultados possíveis d euma medição de $\mathcal{A}$ são os valores próprios do observável $\hat{A}$.

(De notar que estes valores medidos serão sempre reais porque o operador $\hat{A}$ é hermítico)
(Esses valores medidos/permitidos podem ser discretos ou contínuos conforme o espetro de $\hat{A}$)

>==**_Postulado 4:_**== Quando uma quantidade física $\mathcal{A}$ é medida num instante $t_{0}$ num sistema no estado $|\psi\rangle$ normalizado, o resultado tem uma natureza probabilística.
>A probabilidade de obter um valor próprio $a_{n}$ do espetro de $\hat{A}$ é (num caso discreto e não degenerado) dada por $$\mathcal{P}(a_{n})=|\langle u_{n}|\psi\rangle|^{2}$$
>Se o valor próprio $a_{n}$ tem degenerescência $g_{n}$ a sua probabilidade é $\mathcal{P}(a_{n})=\sum\limits_{i=1}^{g_{n}}|\langle u_{n}^{i}|\psi\rangle|^{2}$
>Se o espetro de $\hat{A}$ for contínuo, a densidade de probabilidade de obter um valor próprio $a(\alpha)$ será: $$\mathcal{P}(\alpha)=|\langle u_\alpha|\psi\rangle|^{2}$$
>e a probabilidade de medir um valor entre $a(\alpha)$ e $a(\alpha+d\alpha)$ é $$d\mathcal{P}(\alpha)=|\langle u_{\alpha}|\psi\rangle|^{2}d\alpha$$
>sendo que é obrigatório que o operador $\hat{A}$ seja um observável para que $\sum\limits_{n}\mathcal{P}(a_{n})=1$

- Podemos determinar o valor médio de uma observável:
$$\begin{align*}
\langle\mathcal{A}\rangle&= \sum\limits_{n}a_{n}\mathcal{P}(a_{n})=\sum\limits_{n}a_{n}|\langle u_{n}|\psi\rangle|^{2}=\sum\limits_{n} a_{n}\langle u_{n}|\psi\rangle^{*}\langle u_{n}|\psi\rangle\\
&= \sum\limits_{n}a_{n}\langle \psi|u_{n}\rangle\langle u_{n}|\psi\rangle=\sum\limits_{n}\langle \psi|\hat{A}|u_{n}\rangle\langle u_{n}|\psi\rangle\\
&= \langle \psi|\hat{A}\left(\sum\limits_{n}|u_{n}\rangle\langle u_{n}\right)|\psi\rangle=\langle\psi|\hat{A}\cdot\mathbb{1}|\psi\rangle=\langle \psi|\hat{A}|\psi\rangle=\langle \mathcal{A}\rangle
\end{align*}$$

> ==**_Postulado 5:_**== **Colapso da Função de Onda**. Se a medição da grandeza física $\mathcal{A}$ nos dá o valor $a_{n}$, o sistema físico imediatamente após a medida passa a ser descrito pela projeção normalizada de $|\psi\rangle$ no subespaço de vetores com valor próprio $a_{n}$: $$|\psi\rangle~~\to~~ \frac{\hat{P_{n}}|\psi\rangle}{\sqrt{\langle\psi|\hat{P_{n}}|\psi\rangle}} \quad;\quad \hat{P_{n}}=\sum\limits_{i=1}^{g_{n}}|u_{n}^{i}\rangle\langle u_{n}^{i}|$$
> ou no caso contínuo, se medirmos $a(\alpha)$ com incerteza $\Delta a$: $$|\psi\rangle ~~\to~~ \frac{\hat{P}_{\Delta\alpha}(\alpha)|\psi\rangle}{\sqrt{\langle \psi|\hat{P}_{\Delta\alpha}(\alpha)|\psi\rangle}} \quad;\quad \hat{P}_{\Delta\alpha}(\alpha)=\int_{\alpha-\frac{\Delta\alpha}{2}}^{\alpha+\frac{\Delta\alpha}{2}}d\alpha'~|u_{\alpha'}\rangle\langle u_{\alpha'}|$$

>==**_Postulado 6:_**== A evolução do estado do sistema no tempo é dada por $|\psi(t)\rangle$ e determinada pela equação de Schrödinger:
>$$i\hbar \frac{d}{dt}|\psi(t)\rangle=\hat{H}(t)|\psi(t)\rangle$$
>(em que $\hat{H}$ é a observável da energia total do sistema AKA Hamiltoniano)
