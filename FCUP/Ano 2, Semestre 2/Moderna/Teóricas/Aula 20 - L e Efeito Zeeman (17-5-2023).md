# 1 - Potencial Coulombiano - Continuação
- Conforme vimos na aula anterior, para um potencial Coulombiano temos: $V(\vec{r})= \frac{-e^{2}}{4\pi\varepsilon_{0}r}$
- Temos soluções da eq de Schrödinger do tipo:
$$\Psi_{n \ell m_{\ell}}(\vec{r})=R_{n\ell}(r) Y_{\ell}^{m_{\ell}}(\theta, \phi)$$
- Assim, consideremos que se quer saber a probabilidade de o eletrão (que está sob o efeito do potencial coulombiano gerado pelo protão) estar numa certa posição $\vec{r}$. Temos:
$$\mathcal{P}(\vec{r})=|\Psi(\vec{r})|^{2}=|R_{n\ell}(r)|^{2} |Y_{\ell}^{m_{\ell}}(\theta, \phi)|^{2}$$
- Assim, por analogia, a equação da *normalização* de uma equação de onda deste tipo é:
$$\int_{V} \mathcal{P}(\vec{r})d^{3}r =1 \Longrightarrow \int |R_{n\ell}(r)|^{2} |Y_{\ell}^{m_{\ell}}(\theta, \phi)|^{2} r^{2}\sin \theta dr d\theta d\phi=1$$
que, por convenção, separamos em 2 partes:
$$\begin{cases}\int |R_{n\ell} (r)|^{2}r^{2}dr=1\\ \int |Y_{\ell}^{m_{\ell}}(\theta, \phi)|^{2} \sin\theta ~d\theta d\phi = 1 \end{cases}$$
- Definimos então a *Probabilidade Radial*: probabilidade de o eletrão estar a uma certa distância do protão. É dada por:
$$\mathcal{P}(r)dr= |R_{n\ell} (r)|^{2}r^{2}dr \cancelto{=1}{\int |Y_{\ell}^{m_{\ell}}(\theta, \phi)|^{2} \sin\theta ~d\theta d\phi} = |R_{n\ell} (r)|^{2}r^{2}dr$$

__*EXEMPLO 1*__
- Um eletrão num átomo de Hidrogénio está no nível 1s. Qual é a probabilidade de ele estar a uma distância do protão inferior ao raio de Bohr?

- Primeiro, recordemos que estar no nível 1s significa que: $n=1, \ell=0, m_{\ell}=0$. Temos então: $$\Psi_{100}(\vec{r})=R_{10}(r)Y_{0}^{0}(\theta, \phi)$$
- Os valores de $R, Y$ supostamente estão tabelados. Temos:
$$R_{10}(r) = \frac{2}{a_{0}^{3/2}} e^{\frac{-r}{a_{0}}}\quad ;\quad Y_{0}^{0}(\theta, \phi)= \frac{1}{\sqrt{4\pi}}$$ 
- O que queremos calcular é, então:
$$\begin{align*}
\mathcal{P}(0<r<a_{0}) &= \int_{0}^{a_{0}} |R_{10}(r)|^{2} ~r^{2}dr\\
&= \int_{0}^{a_{0}} \left| \frac{2}{a_{0}^{3/2}} e^{\frac{-r}{a_{0}}} \right|^{2}r^{2}dr\\
&= \frac{4}{a_{0}^{3}} \int_{0}^{a_{0}} e^\frac{-2r}{a_{0}}r^{2}dr\\
\end{align*}$$
fazendo a substituição $x= \frac{2r}{a_{0}}$ ficamos com 
$$\mathcal{P}(0<r<a_{0}) = \frac{1}{2}\int_{0}^{2}e^{-x}dx \approx 0.32$$
> NOTA sobre $R,Y$
> - Temos que $R$ tem o seguinte formato $$R_{n \ell}(r) = (\textsf{polinómio ordem }n-1)\cdot e^{\frac{-r}{na_{0}}}$$
> - E $Y$ tem o formato: $$Y_{\ell}^{m_{\ell}}(\theta, \phi) = (\textsf{polinómio grau } \ell \textsf{ numa função trignometrica})\cdot e^{im_{\ell}\phi}$$
> - Por exemplo, temos:
> $$\Psi_{200}(\vec{r})= \frac{1}{(2a)^{3/2}} \left( 2- \frac{r}{a_{0}} \right) e^{\frac{-r}{2a_{0}}} \frac{1}{\sqrt{4\pi}}$$
> $$\Psi_{21-1}(\vec{r})= \frac{1}{\sqrt{3}(2a_{0})} \frac{r}{a_{0}} e^{\frac{-r}{2a_{0}}} \sin\theta \sqrt{\frac{3}{8\pi}} e^{-i\phi} $$

# 2 - Quantificação de $\vec{L}$
### Física Clássica
- Apenas temos $$\vec{\ell} = \vec{r} \times \vec{p}$$
### Física Quântica
- Começamos por fazer a conversão em operadores:
$$\begin{align*}
\vec{\ell} \to \vec{L}&= (\hat{L}_{x}, \hat{L}_{y}, \hat{L}_{z})\\
\vec{r} \to \vec{R}&= (\hat{X}, \hat{Y}, \hat{Z})\\
\vec{p} \to \vec{P}&= (\hat{P}_{x}, \hat{P}_{y}, \hat{P}_{z})
\end{align*}$$
- Ora, como já vimos, para as posições e momento linear temos:
$$\begin{align*}
x\to \hat{X}&=x & y\to \hat{Y}&=y & z\to \hat{Z}&=z \\
p_{x}\to \hat{P}_{x}&= \frac{\hbar}{i} \frac{\partial}{\partial x} &
p_{y}\to \hat{P}_{y}&= \frac{\hbar}{i} \frac{\partial}{\partial y} &
p_{z}\to \hat{P}_{z}&= \frac{\hbar}{i} \frac{\partial}{\partial z} &
\end{align*}$$
ou, de outra forma, $$\vec{R}=\vec{r} \quad \quad \quad;\quad \quad \quad\vec{P}=-i\hbar \nabla$$
- Assim, temos:
$$\vec{L}=-i\hbar~ \vec{r}\times \vec{\nabla} \quad \quad;\quad \quad \begin{cases}L_{x}=-i\hbar \left( y\frac{\partial}{\partial z} - z\frac{\partial}{\partial y} \right)\\ L_{y}=-i\hbar \left( z\frac{\partial}{\partial x} - x\frac{\partial}{\partial z} \right) \\ L_{z}=-i\hbar \left( x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x} \right) \end{cases}$$

- Passemos para coordenadas esféricas:
    - $\vec{r}=r \hat{u}_{r}$
    - $\nabla = \frac{\partial}{\partial r}\hat{u}_{r} + \frac{1}{r} \frac{\partial}{\partial \theta} \hat{u}_{\theta} + \frac{1}{r\sin\theta} \frac{\partial}{\partial \phi}\hat{u}_{\phi}$
- E assim temos:
$$\begin{align*}
\vec{L}&= -i\hbar \vec{r}\times \nabla = -i\hbar \left( \frac{\partial}{\partial \theta}\hat{u}_{\phi} - \frac{1}{\sin\theta} \frac{\partial}{\partial \phi} \hat{u}_{\phi} \right)\\
L^{2} &= -\hbar^{2}\left[ \frac{1}{\sin\theta} \frac{\partial}{\partial \theta}\left( \sin\theta \frac{\partial}{\partial \theta} \right) + \frac{1}{\sin^{2}\theta} \frac{\partial^{2}}{\partial\phi^{2}} \right]
\end{align*}$$
- Não escrevi a dedução mas temos: $$L^{2} = \ell(\ell+1)\hbar^{2} \quad \quad; \quad \ell\geq 0$$(em que este é o mesmo $\ell$ que temos em $\Psi_{n\ell m_{\ell}}$)
- E tem-se $$L_{z}= m_{\ell}\hbar$$
- Assim o *momento angular está quantificado*.

# 3 - Teorema de adição de 2 momentos angulares
- Temos 2 momentos angulares: $L_{1},L_{2}$ e temos a sua soma: $L=L_{1}+L_{2}$
    - $|L_{1}|=\sqrt{\ell_{1}(\ell_{1}+1)}\hbar$ ; $|L_{2}|=\sqrt{\ell_{2}(\ell_{2}+1)}\hbar$ logo temos $|L|=\sqrt{\ell(\ell+1)}\hbar$

- Temos: $$|\ell_{1}-\ell_{2}|\le \ell \le \ell_{1}+\ell_{2}$$

# 4 - Efeito de Zeeman
- Ocorre quando temos um eletrão na presença de um campo *magnético*. Consideremos então um átomo de hidrogénio num campo magnético $B$.
- Temos a ESIT assim:
$$\left[ \frac{-\hbar^{2}}{2m}\nabla^{2} + V_{coulomb} + V_{mag}\right] \Psi=E \Psi$$
Temos $\vec{F}_{mag}=-\nabla(\vec{\mu}\cdot \vec{B})$, sendo $\vec{B}$ o campo magnético e $\vec{\mu}$ o momento magnético. Assim:
$$\left[ \frac{-\hbar^{2}}{2m}\nabla^{2} + V_{coulomb} + \vec{\mu}\cdot\vec{B}\right] \Psi_{n\ell m_{\ell}} =E_{n} \Psi_{n\ell m_{\ell}}$$
- Definimos então:
    - $\vec{B}=\vec{0} \to E=E_{n}$
    - $\vec{B}\ne \vec{0} \to E = E_{n} + \vec{mu} \cdot \vec{B}$

E ficamos com $\left[ \frac{-\hbar^{2}}{2m}\nabla^{2} + V_{coulomb}\right] \Psi=E \Psi$

- Vamos supor $\vec{B}=(0,0,B)$. Temos:
$$\vec{\mu}=\frac{|e|}{2m} \vec{L} = \frac{|e|\hbar}{2m} \frac{\vec{L}}{\hbar} = \mu_{B}\frac{\vec{L}}{\hbar} \quad \quad;\quad \quad \mu_{B}=\frac{|e|\hbar}{2m}$$
e temos $$\vec{\mu} \cdot \vec{B} = (\mu_{x}, \mu_{y}, \mu_{z})\cdot(0,0,B)=\mu_{z}B=\mu_{B} \frac{L_{z}}{\hbar} = \mu_{B}\frac{m_{\ell}\hbar}{\hbar}=\mu_{B}m_{\ell}$$

#moderna #fisica #magnetismo 