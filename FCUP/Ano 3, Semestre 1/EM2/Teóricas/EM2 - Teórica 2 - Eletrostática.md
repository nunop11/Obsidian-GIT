# Equações de Maxwell
$$\begin{align*}
\nabla \cdot \vec{E}&= \frac{\rho}{\varepsilon_{0}} \tag{1}\\
\nabla \cdot \vec{B}&= 0\tag{2}\\
\nabla \times \vec{E} + \frac{\partial}{\partial t}\vec{B}&= 0 \tag{3} \\
\nabla \times \vec{B}-\varepsilon_{0}\mu_{0} \frac{\partial}{\partial t}\vec{E}&= \mu_{0} \vec{j} \tag{4}\\
\end{align*}$$
# Força de Lorentz
$$\vec{F}=q(\vec{E}+\vec{v}\times \vec{B})$$

# Resultados Importantes de EM1
Sendo $V=V(x,y,z)$ um campo escalar,  $\vec{E}, \vec{B}$ os campos elétrico e magnético e $\vec{A}$ um campo vetorial.
$$\begin{align*}
\nabla \times \vec{E}=0 \quad &\longrightarrow \quad \vec{E}=- \nabla V\\
\nabla \cdot \vec{B}=0 \quad &\longrightarrow \quad \vec{B}= \nabla \times \vec{A}\\
\int_{\vec{r}_{a}}^{\vec{r}_{b}} \nabla V \cdot d \vec{r}&= \int_{\vec{r}_{a}}^{\vec{r}_{b}}=V(\vec{r_{b}})-V(\vec{r}_{a})\\
\int \nabla \cdot \vec{E} ~d^{3}r&= \oint \vec{E}\cdot d \vec{s} \quad \quad \quad \textsf{(Teorema de Gauss)} \\
\int (\nabla \times \vec{E})\cdot d \vec{s}&= \oint \vec{E} \cdot d \vec{r} \quad \quad \quad \textsf{(Teorema de Stokes)}
\end{align*}$$

# Eletrostática
- Para aplicar as equações de Maxwell a estes problemas iremos fazer 2 alterações diretas: $$\vec{j}=\vec{0} \quad \quad;\quad \quad \vec{B}=\vec{0}$$
ora, devido à 4ª equação de Maxwell isto dá-nos: $$\frac{\partial}{\partial t}\vec{E}=\vec{0} \quad \longrightarrow \quad \vec{E}=\vec{E}(r)$$
ou seja, em eletro **estática** o campo elétrico é invariante no tempo.

- Assim, devido às 2 alterações acima, apenas a 1ª e 3ª equação são relevantes, ficando elas na forma: $$\nabla \cdot \vec{E}= \frac{\rho}{\varepsilon_{0}} \quad \quad ;\quad \quad \nabla \times \vec{E}=\vec{0}$$
- Também a Força de Lorentz se altera, ficando na forma: $$\vec{F}=q \vec{E}$$

**EXEMPLO - Carga Pontual na Origem**
- Pela simetria vemos que o campo gerado por esta carga $q$ será radial, tendo-se: $$\vec{E}(\vec{r})=E(r) \hat{e}_{r} \quad \quad;\quad \hat{e}_{r}=\hat{r}= \frac{\vec{r}}{r}$$
- Comecemos então com $\nabla \cdot \vec{E}=\frac{\rho}{\varepsilon_{0}}$. Podemos integrar os dois lados no volume que consiste em uma esfera de raio $r$ e centrada em $q$. Assim: $$\int \nabla \cdot \vec{E} ~d^{3}r=\int \frac{\rho}{\varepsilon_{0}} d^{3}r$$
aplicando o teorema de Gauss e tornado o lado esquerdo numa integral de área, na superfície esférica de raio $r$ centrada em $q$:
$$\begin{align*}
\oint \vec{E}\cdot d \vec{s}&= \int \frac{\rho}{\varepsilon_{0}} d^{3}r\\
\oint E(r) \hat{e}_{r} \cdot ds \hat{e}_{r}&= \frac{1}{\varepsilon_{0}}\int \rho~d^{3}r\\
E(r)\oint ds &= \frac{1}{\varepsilon_{0}}\\
4\pi r^{2} E(r)&= \frac{q}{\varepsilon_{0}}\\
E(r)&= \frac{q}{4\pi\varepsilon_{0}r^{2}} \quad \longrightarrow\quad  \vec{E}(\vec{r})=\frac{q}{4\pi\varepsilon_{0}} \frac{1}{r^{2}} \hat{e}_{r}=\frac{q}{4\pi\varepsilon_{0}} \frac{\vec{r}}{r^{3}}  
\end{align*}$$
que é a Lei de Coulomb, pelo que temos o resultado esperado.

**E se a carga estivesse fora da origem?**
- Consideremos que a carga $q$ está na posição $\vec{r}_{q}$.  Teríamos: $$\vec{E}(\vec{r})=\frac{q}{4\pi\varepsilon_{0}} \frac{(\vec{r}-\vec{r}_{q})}{|\vec{r}-\vec{r}_{q}|^{3}}$$

**EXEMPLO - Potencial de Carga pontual q na origem**
$$\begin{align*}
\vec{E}\cdot d\vec{r}&= \frac{q}{4\pi\varepsilon_{0}} \frac{1}{r^{2}} \hat{e}_{r} \cdot (dr \hat{e}_{r} + d_{\perp}\hat{e}_{\perp})\\
&= \frac{q}{4\pi\varepsilon_{0}} \frac{dr}{r^{2}}
\end{align*}$$
e assim temos:
$$\int_{\infty}^{\vec{r}} \vec{E}\cdot d \vec{r}=\frac{q}{4\pi\varepsilon_{0}} \int_{\infty}^{\vec{r}} \frac{dr}{r^{2}}=\frac{-q}{4\pi\varepsilon_{0}r}$$

## Equação de Poisson
- Temos: $$\begin{cases}
\nabla \cdot \vec{E}= \frac{\rho}{\varepsilon_{0}} \\ \vec{E}=-\nabla V
\end{cases} \Longrightarrow \nabla \cdot (-\nabla V)=\frac{\rho}{\varepsilon_{0}} ~~\Longleftrightarrow~~ \nabla^{2}V=- \frac{\rho}{\varepsilon_{0}}$$