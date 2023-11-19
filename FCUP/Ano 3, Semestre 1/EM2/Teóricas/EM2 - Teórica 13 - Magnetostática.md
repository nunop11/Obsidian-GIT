# Magnetostática
- Até agora vimos eletrostática AKA sistemas com cargas imóveis, sem campo magnético presente.
- Veremos agora *magnetostática* AKA sistemas com campos magnéticos, mas sem campos elétricos. Ou seja:
$$\vec{E}=0 \quad \quad;\quad \quad \rho=0$$
- Da equação de Faraday resulta: $\frac{\partial}{\partial t}\vec{B}=0$, ou seja, temos campos magnéticos constantes no tempo, o que faz sentido para o nome "magnetostática".

- Tal como na eletrostática, continuamos a ter que: $$\nabla \cdot \vec{B}=0 ~~ \Longleftrightarrow ~~ \vec{B}=\nabla \times \vec{A}$$
ou seja: $\vec{B}$ é um campo solenoidal, pelo que pode ser escrito como rotacional de outro campo $\vec{A}$, a que chamaremos **Vetor potencial**.
- Este campo vetorial do potencial pode ser definido a menos de um gradiente:
$$\vec{A'}=\vec{A}+\nabla f ~~\to~~ \vec{B'}=\nabla \times \vec{A'}=\nabla \times \vec{A} + \cancelto0{\nabla \times (\nabla f)}=\vec{B}$$

- Da equação de Ampere-Maxwell ("Ampere-Manca", fonte: Pai) resulta:
$$\nabla \times \vec{B}=\mu_{0}\vec{\mathcal{J}}$$

## Monopolo / carga magnética
- Vejamos se é possível ter um monopolo AKA carga AKA fonte de campo magnético.
- Para o campo elétrico tínhamos que uma carga $q$ gera um campo radial descrito por $\vec{E}(r)=\frac{q}{4\pi\varepsilon_{0}r^{2}}\hat{r}$
- Consideremos então que existe um monopolo magnético, que gera um campo radial $\vec{B}=B(r)\hat{r}$. Temos:
$$\nabla \cdot \vec{B}=0 \quad\to\quad \int \nabla \cdot \vec{B}~d^{3}r=0=\oint \vec{B}\cdot d \vec{s}$$
ou seja, temos que ter $\vec{B}=0$ para qualquer área fechada. Ou seja, **não existem** monopolos magnéticos.

## Potencial Vetor
- Como vimos acima, o campo definido pode ser definido com $\vec{A}$, a menos de 1 gradiente. Por outras palavras, isto significa que: O campo magnético $\vec{B}=\nabla \times \vec{A}$ é *invariante* pela transformação $\vec{A}\to \vec{A'}=\vec{A}+\nabla \chi$. 
- Ora, nada nos impede de impôr a condição $\nabla \cdot \vec{A'}=0$ (porque continuaremos a ter um campo magnético correto). Temos:
$$\nabla \cdot \vec{A'}=\nabla \cdot \vec{A}+ \nabla^{2}\chi=0 ~~\to~~ \boxed{\nabla^{2}\chi=-\nabla \cdot \vec{A}}$$
(pelo que esta equação terá sempre solução)

---

- Voltando ao campo, temos:
$$\begin{align*}
\nabla \times \vec{B} &= \mu_{0}\vec{\mathcal{J}}\\
&= \nabla \times (\nabla \times \vec{A})\\
&= \nabla (\nabla \cdot \vec{A}) - \nabla^{2}A\\
\end{align*}$$
com a condição $\nabla \cdot \vec{A}=0$ ficamos com:
$$\boxed{\nabla^{2}\vec{A}=- \mu_{0}\vec{\mathcal{J}}}$$

> NOTA: Laplaciano de campo vetorial
> - Para uma função escalar temos: $$\nabla^{2}f= \frac{\partial^{2}f}{\partial x^{2}}+\frac{\partial^{2}f}{\partial y^{2}}+\frac{\partial^{2}f}{\partial z^{2}}$$
> - Para um campo vetorial temos: $$\nabla^{2}\vec{A}=\left( \nabla^{2}A_{x}, \nabla^{2} A_{y}, \nabla^{2}A_{z} \right)$$

- Podemos ver que esta equação é bastante semelhante à *equação de Poisson*:
$$\nabla^{2}V=- \frac{\rho}{\varepsilon_{0}}$$
que tinha a solução $$V = \frac{1}{4\pi\varepsilon_{0}}\int \frac{\rho(\vec{r'})}{|\vec{r}-\vec{r'}|}d^{3}r'$$

- Ora, a equação acima funciona da mesma forma só que vetorial. Temos então a solução:
$$\vec{A}(\vec{r})= \frac{\mu_{0}}{4\pi} \int \frac{\vec{\mathcal{J}}(\vec{r'})}{|\vec{r}-\vec{r'}|}d^{3}r'$$
- Verifiquemos apenas se a condição $\nabla \cdot \vec{A}=0$:
    - Temos que $\nabla=(\partial_{x},\partial_{y},\partial_{z})$  logo este não afeta $\vec{\mathcal{J}}(\vec{r'})$ e temos: $$\begin{align*}
\nabla \cdot  \vec{A}&= \frac{\mu_{0}}{4\pi} \int \nabla\left(\frac{1}{|\vec{r}-\vec{r'}|}\right) \cdot \vec{\mathcal{J}}(\vec{r'})~d^{3}r'\\
&= - \frac{\mu_{0}}{4\pi} \int \nabla'\left(\frac{1}{|\vec{r}-\vec{r'}|}\right) \cdot \vec{\mathcal{J}}(\vec{r'})~d^{3}r'\\
&= - \frac{\mu_{0}}{4\pi} \int \left[ \nabla'\cdot \left(\frac{\vec{\mathcal{J}}(\vec{r'})}{|\vec{r}-\vec{r'}|} \right)- \frac{\nabla'\cdot\vec{\mathcal{J}}(\vec{r'})}{|\vec{r}- \vec{r'}|} \right]d^{3}r'=0
\end{align*}$$
não sei bem porquê que isto é verdade, mas é.

