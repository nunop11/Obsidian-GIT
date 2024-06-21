![[Pasted image 20240604020904.png]]
- No grafeno temos 2 átomos por célula unitária.
- Vamos então dividir os átomos em 2 grupos: $A,B$

- Podemos escrever:
$$\begin{align*}
\vec{a}_{1}&= \frac{a}{2}(3,\sqrt{3})\\
\vec{a}_{2}&= \frac{a}{2}(3,-\sqrt{3})\\
\vec{\delta}_{1}&= \frac{a}{2}(1,\sqrt{3})\\
\vec{\delta}_{2}&= \frac{a}{2}(1,-\sqrt{3})\\
\vec{\delta}_{3}&= -a(1,0)\\
\vec{K}&= \frac{2\pi}{3\sqrt{3}a}(\sqrt{3},1)\\
\vec{K'}&= \frac{2\pi}{3\sqrt{3}a}(\sqrt{3},-1)
\end{align*}$$
em que $\delta$ são os vértices da ZB1.

## Tigh-Binding
- Uma forma de representar a combinação linear de funções de onda atómicas do tight-binding é:
$$\ket{\vec{k}}=\frac{1}{\sqrt{N}}\sum\limits_{j}[A\ket{\phi_{j}^{A}}+B\ket{\phi_{j}^{B}}] e^{i\vec{k}\cdot\vec{R}_{j}}$$
em que $\ket{\phi_{j}^{A/B}}$ é a função de onda do átomo $A/B$ na célula, na posição $\vec{R}_{j}$.

### Hamiltoniano
- O hamiltoniano de tight-binding para o grafeno permite a transição entre vizinhos mais próximos de modo que os eletrões num átomo do tipo A/B podem saltar para os três átomos B/A mais próximos.
- Projetando a ESIT na base $\ket{\phi_{j}^{A}}$ temos:
$$\begin{align*}
\bra{\phi_{j}^{A}}H\ket{\vec{k}}&= E_{\vec{k}} \bra{\phi_{j}^{A}}\vec{k}\rangle\\
\frac1{\sqrt N}\left[A\varepsilon_0 e^{i\vec k\cdot\vec R_j} + B(-t)\left(e^{i\vec k \cdot\vec R_j} + e^{i\vec k\cdot(\vec R_j -\vec a_1)} + e^{i\vec k\cdot(\vec R_j - \vec a_2)}\right)\right] &= E(\vec k)\frac A{\sqrt N}e^{i\vec k \cdot\vec R_j}
\end{align*}$$
em que $\varepsilon_{0}=\bra{\phi_{h}^{A}}\hat{H}\ket{\phi_{j}^A}$ e $-t=\bra{\phi_{j}^{A}}\hat{H}\ket{\phi_{\ell}^{B}}$
- Consideremos $\vec{R}_{\ell}=\vec{R}_{j},\vec{R}_{j}+\vec{a}_{1},\vec{R}_{j}+\vec{a}_{2}$. Conseguimos (?) obter:
$$AE_{\vec{k}}=A\varepsilon_{0}-Bt(1+e^{-i\vec{k}\cdot\vec{a}_{1}}+e^{-i\vec{k}\cdot\vec{a}_{2}})$$
analogamente, para o átomo $B$ teremos:
$$BE_{\vec{k}}=B\varepsilon_{0}-At(1+e^{i\vec{k}\cdot\vec{a}_{1}}+e^{i\vec{k}\cdot\vec{a}_{2}})$$

- Assim, o problema pode ser reduzido a uma matriz 2x2:
$$\begin{vmatrix}\varepsilon_{0}-E_{\vec{k}} & -t(1+e^{-i\vec{k}\cdot\vec{a}_{1}}+e^{-i\vec{k}\cdot\vec{a}_{2}}) \\ -t(1+e^{i\vec{k}\cdot\vec{a}_{1}}+e^{i\vec{k}\cdot\vec{a}_{2}}) & \varepsilon_{0}-E_{\vec{k}}\end{vmatrix}=0$$
e temos a relação de dispersão do grafeno:
$$E_{\vec{k}}= \varepsilon_{0}\pm t [3+2\cos(\vec{k}\cdot\vec{a}_{1})+2\cos(\vec{k}\cdot\vec{a}_{2})+2\cos(\vec{a}_{1}-\vec{a}_{2})]$$
![[Pasted image 20240604022546.png]]