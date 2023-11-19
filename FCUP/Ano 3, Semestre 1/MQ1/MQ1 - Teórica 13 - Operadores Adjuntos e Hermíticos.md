## Projetores
- Na notação de Dirac, tal como já vimos, escremos o produto escalar como $\langle \phi|\psi\rangle$ (sendo que este é um *número*)
- Mas, se escrevermos $|\psi\rangle\langle \phi|$ temos um *operador*, porque podemos reescrever:
$$|\psi\rangle\langle\phi|=|\psi\rangle\langle\phi|\chi\rangle=\underbrace{(\langle \phi|\chi\rangle)}_{número} |\psi\rangle$$

- Ora, se considerarmos que o ket $|\psi\rangle$ está normalizado ($\langle \psi|\psi\rangle=1$) podemos definir a **_Projetor_** em $\psi$ assim:
$$P_{\psi}=|\psi\rangle\langle \psi|$$
pelo que podemos obter a projeção de $\phi$ em $\psi$:
$$P_{\psi}|\phi\rangle = |\psi\rangle\langle \psi|\phi\rangle = (\langle \psi|\phi\rangle)|\psi\rangle$$

- Podemos ainda ver que:
$$P_{\psi}(P_{\psi}|\phi\rangle)= P_{\psi}(|\psi\rangle\langle \psi|\phi\rangle)=\langle \psi|\phi\rangle(P_{\psi}|\psi\rangle)=\langle \psi|\phi\rangle(|\psi\rangle \underbrace{\langle \psi|\psi\rangle}_{=1} )=P_{\psi}(\phi)$$
de onde temos: $$P_{\psi}^{2}=P_\psi$$

- Consideremos que temos os vetores normalizados $|\psi_{1}\rangle,\dots|\psi_{q}\rangle$ em que $\langle \psi_{i}|\psi_{j}\rangle=\delta_{ij}$. Sendo $\mathcal{E}_{q}$ o subespaço gerado por estes $q$ vetores.
- Podemos definir o operador:
$$P_{q}=\sum\limits_{i=1}^{q} |\psi_{i}\rangle\langle \psi_{i}|$$
que projeta qualquer estado $|\psi\rangle$ no subspaço $\mathcal{E}_{q}$.

## Operador Adjunto (Hermítico Conjugado)
- A cada ket $|\psi\rangle$ conseguimos associar um bra $\langle\psi|$.
- Um operador $\hat{A}$ a atuar no ket $|\psi\rangle$ dá o ket $|\psi'\rangle=\hat{A}|\psi\rangle$
- Vamos então definir o operador adjunto de $\hat{A}$: $A^{\dagger}$ em que temos:
$$\begin{align*}
|\psi\rangle &\longrightarrow \langle\psi|\\
|\psi'\rangle=\hat{A}|\psi\rangle &\longrightarrow \langle\psi'|=\langle \hat{A}\psi|=\langle\psi|A^{\dagger}
\end{align*}$$

- Ambos os operadores são lineares: 
$$\begin{align*}
\hat{A}(\lambda_{1}|\psi_{1}\rangle+\lambda_{2}|\psi_{2}\rangle) &= \lambda_{1}(\hat{A}|\psi_{1}\rangle) + \lambda_{2}(\hat{A}|\psi_{2}\rangle)\\
(\lambda_{1}\langle\psi_{1}|+\lambda_{2}\langle\psi_{2}|)A^{+}&= \lambda_{1}(\langle\psi_{1}|A^{\dagger})+\lambda_{2}(\langle\psi_{2}|A^{\dagger})
\end{align*}$$
- Temos ainda que $\langle \psi'|\phi\rangle=\langle \phi|\psi'\rangle^{*}$ e podemos obter: $$\boxed{\langle \psi|A^{\dagger}|\phi\rangle=\langle \phi|\hat{A}|\psi\rangle}$$

### EXEMPLOS
#### 1.
- O operador adjunto de $\hat{X}$ é ele próprio.
- Para quaisquer $\phi,\psi$ temos:
$$\begin{align*}
\langle \psi|\hat{X}^{\dagger}|\phi\rangle&= \langle \phi|\hat{X}|\psi\rangle^{*}\\
&= \left(\int d^{3}r~\phi^{*}(\vec{r})\hat{X}\psi(\vec{r})\right)^{*}\\
&= \int d^{3}r~ \psi^{*}(\vec{r})x \phi(\vec{r})=\langle \psi|\hat{X}|\phi\rangle
\end{align*}$$
logo $\hat{X}^{\dagger}=\hat{X}$

#### 2. 
- Sendo $\hat{D_{u}}$ o operador derivada em $u$ temos: $$\hat{D}_{u}^{\dagger}=- \hat{D_{u}}$$
- Para quaiser $\psi,\phi$:
$$\begin{align*}
\langle \psi|\hat{D}_{u}^{\dagger}|\phi\rangle&= \langle \phi|\hat{D}_{u}|\psi\rangle^{*}\\
&= \left(\int d^{3}r~ \phi^{*}(\vec{r})\frac{\partial \psi(\vec{r})}{\partial u} \right)^{*}\\
&= \int d^{3}r~ \frac{\partial \psi^{*}(\vec{r})}{\partial u}\phi(\vec{r})\\
&= - \int d^{3}r~ \psi^{*}(\vec{r})\frac{\partial \phi(\vec{r})}{\partial u}\\
&= \langle \psi|-\hat{D}_{u}|\phi\rangle
\end{align*}$$

### Propriedades de operadores adjuntos 
$$\begin{align*}
(\hat{A}^{\dagger})^{\dagger}&= \hat{A}\\
(\lambda \hat{A})^{\dagger}&= \lambda^{*}\hat{A}^{\dagger}\\
(\hat{A}+\hat{B})^{\dagger} &= \hat{A}^{+}+\hat{B}^{\dagger}\\
(AB)^{\dagger}&= A^{\dagger}B^{\dagger}
\end{align*}$$

## Operadores Hermíticos
- Um operador é hermítico se for igual ao esu adjunto:
$$\hat{A}=\hat{A}^{\dagger}$$
pelo que temos:
$$\langle \phi|\hat{A}|\psi\rangle=\langle \phi|\hat{A}^{\dagger}|\psi\rangle=\langle \psi|\hat{A}|\phi\rangle^{*}$$
- Se $|\psi\rangle=|\phi\rangle$, então temos $\langle \psi|\hat{A}|\psi\rangle$, que é real. (esta é a combinação que usavamos em Física moderna para determinar os valores médios de $X,P,E$)

### EXEMPLOS
**1.** Como vimos acima, $\hat{X}$ é um operador hermítico
**2.** O operador derivada, $\hat{D}_{u}$, é *anti-hermítico* pois $\hat{D}_{u}^{\dagger}=-\hat{D}_{u}$
**3.** O operador momento linear é hermítico:
$$\hat{P}_{u}^{\dagger}=\left( \frac{\hbar}{i}\right)^{*} \hat{D}_{u}^{\dagger}=\frac{\hbar}{-i} (- \hat{D}_{u})=\frac{\hbar}{i}\hat{D}_{u}=\hat{P_{u}}$$
**4.** O operador Hamiltoniano é hermítico
**5.** Operador *paridade*, $\hat{\pi}$, é hermítico:
$$\begin{align*}
\langle \psi|\hat{\pi}^{+}|\phi\rangle&= \langle \phi|\hat{\pi}|\psi\rangle^{*}\\
&= \left(\int d^{3}r~ \phi^{*}(\vec{r}) \underbrace{\hat{\pi}\psi(\vec{r})}_{= \psi(-\vec{r})} \right)\\
&= \int d^{3}r~ \psi^{*}(-\vec{r}) \phi(\vec{r})\\
&= \int d^{3}r'~ \psi^{*}(\vec{r'})\phi(-\vec{r'}) \quad \quad (\vec{r'}=-\vec{r})\\
&= \int d^{3}r' \psi^{*}\hat{\pi}\phi(\vec{r})=\langle \psi|\hat{\pi}|\phi \rangle
\end{align*}$$
ou seja: $\hat{\pi}^{\dagger}=\hat{\pi}$

**6.** O projetor é hermítico:
$$\begin{align*}
\langle \phi|P_{\psi}^{\dagger}|\chi\rangle= \langle \phi|(|\psi\rangle\langle\psi|)^{\dagger}|\chi\rangle&= (\langle \chi|(|\psi\rangle\langle\psi|)|\phi\rangle)^{*}\\
&= (\langle \chi|\psi\rangle \langle \psi|\phi\rangle)^{*}\\
&= \langle \chi|\psi\rangle^{*}\langle \psi|\phi\rangle^{*}\\
&= \langle \psi|\chi\rangle \langle \phi|\psi\rangle\\
&= \langle \phi|(|\psi\rangle\langle\psi|)|\chi\rangle 
\end{align*}$$

**7.** O produto de 2 operadores hermíticos é hermítico se o *comutador for nulo*:
$$(AB)^{\dagger}=A^{\dagger}B^{\dagger}=BA=BA-AB+AB=AB-[A,B]$$

## Representação de Kets, Bras e Operadores na Notação de Dirac
- Consideremos que se tem uma base discreta com elementos $|u_{n}\rangle$. Como já vimos atrás:
$$|\psi\rangle=\sum_{n}c_{n}|u_{n}\rangle$$
- É conveniente representar assim:
    - O ket $|\psi\rangle=\sum_{n} c_{n}|u_n\rangle$ será representado por uma coluna do tipo $c_{n}\left(\matrix{c_{1}\\c_{2}\\ \vdots\\ c_{n}}\right)$ 
    - O bra $\langle\psi|=\sum_{n} b_{n}^{*}\langle u_{n}|$ será representado por linhas do tipo: $b_{n}^{*}(\matrix{b_{1}^{*} &b_{2}^{*} &\dots &b_{n}^{*}})$
    - O operador $\hat{A}$ representado por uma matriz com elementos $A_{nm}=\langle u_{n}|\hat{A}|u_{m}\rangle$. 
    - O ket $\hat{A}|\psi\rangle$ é um vetor coluna que resulta do produto da matriz $A_{nm}$ com a coluna $c_{n}$
        - Conseguimos então obter: $$b_{n}= \langle u_{n}|(\hat{A}|\psi\rangle)=\sum_{m} \langle u_{n}|\hat{A}|u_{m}\rangle \langle u_{m}|\psi\rangle=\sum\limits_{m}A_{nm}c_{m}$$
    - Sendo $|\psi\rangle=\sum_{n} b_{n}|u_{n}\rangle~,~ |\phi\rangle=\sum_{n}c_{n}|u_{n}\rangle$ podemos escrever: $$\langle \phi|\hat{A}|\psi\rangle=\sum\limits_{m,n} \langle \phi|u_{m}\rangle \langle u_{m}|\hat{A}|u_{n}\rangle \langle u_{n}|\psi\rangle=\sum\limits_{m,n} b_{n}^{*}A_{mn}c_{n}= (\matrix{b_{1}^{*} &b_{2}^{*} &\dots}) \left(\matrix{A_{11} &A_{12} &\dots \\A_{21} &\dots &\dots\\ \dots &\dots &\dots} \right)\left(\matrix{c_{1}\\c_{2}\\\vdots} \right) $$
    - O operador adjunto $\hat{A}^{+}$ é representado pela matriz transposta e composta pelo complexo conjugado dos elementos da matriz de $\hat{A}$: $$(A^{\dagger})_{mn}=\langle u_{m}|A^{\dagger}|u_{n}\rangle=\langle u_{n}|A|u_{m}\rangle^{*}= A_{nm}^{*}$$ 
        - Para um operador hermítico isto também se aplica, mas de notar que os elementos das diagonais são reais e portanto ficam inalterados.