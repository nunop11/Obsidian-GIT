## Dielétricos Lineares
- Consiste num conjunto de materiais em que temos $P\propto E$. Mais concretamente:
$$\vec{P}=\varepsilon_{0} \chi_{e} \vec{E}$$
em que $\chi_{e}$ é a *suscetibilidade elétrica* do material. 
- Notemos, no entanto, que o campo $\vec{E}$ acima é o **campo total**. Se aplicarmos um campo externo $\vec{E_{0}}$ a um dielétrico, não podemos simplesmente espetar este campo na fórmula acima. Este campo irá polarizar o material, o que vai criar um campo elétrico de polarização, que vai alterar o campo total e por sua vez a polarização, etc etc.
- Assim, é normalmente resolver o problema ao contrário. Especialmente se tivermos cargas livres, costuma ser boa ideia começar por obter o Deslocamento:
$$\vec{D}=\varepsilon_{0}\vec{E}+\vec{P}=\varepsilon_{0}\vec{E}+\varepsilon_{0}\chi_{e}\vec{E}=\varepsilon_{0}(1+\chi_{e})\vec{E}$$
em que definimos a *permitividade do material*: $$\varepsilon\equiv\varepsilon_{0}(1+\chi_{e})$$(no vácuo não há material para polarizar logo a suscetibilidade é nula e temos $\varepsilon=\varepsilon_{0}$)
e temos que, para dielétricos lineares, também temos $\vec{D}\propto\vec{E}$ em que:
$$\vec{D}=\varepsilon\vec{E}$$

- Por vezes é útil adimensionalizar a expressão da permitividade e temos a *permitividade relativa do material*:
$$\varepsilon_{r}\equiv 1+\chi_{e}=\frac{\varepsilon}{\varepsilon_{0}}$$

- Temos que $\vec{P}\propto\vec{E}$ e $\vec{D}\propto\vec{E}$. Ora, como na eletrostática o rotacional de $\vec{E}$ é nulo então o rotacional de $\vec{P}, \vec{D}$ também tem que ser? **Não**. Podemos ter rotacionais não nulos. Isto porque a proporcionalidade que vimos acima apenas se aplica *no dielétrico*. Se fizermos um percurso em torno da fronteira entre o dielétrico e o exterior (ver abaixo) temos sempre $\nabla \times \vec{E}=0$ mas temos $\oint \vec{P}\cdot d \vec{r}\neq0$. Pelo teorema de stokes, isto implica que $\nabla \times \vec{P}\neq0$.
![[rotacional de P não nulo.png]]

#### Dielétricos lineares, homogéneos e isotrópicos
- Por outro lado, se *todo* o espaço estiver coberto pelo dielétrico já não é este o caso, tendo-se:
$$\nabla \cdot \vec{D}= \rho_{\ell} \quad \quad;\quad \quad \nabla \times \vec{D}=\vec{0}$$
sendo que podemos escrever $$\vec{D}=\varepsilon \vec{E}=\varepsilon_{0}\vec{E}_{vacuo}$$
de onde resulta $$\vec{E}=\frac{\vec{E}_{vacuo}}{\varepsilon_{r}}$$
- Ora, se tivermos todo o espaço (ou pelo menos todo o espaço em que $\vec{E}_{vacuo}\neq0$) coberto pelo dielétrico, então o campo será igual àquele do vácuo mas menor por uma fração de $\varepsilon_{r}$.

- Podemos ainda, para dielétricos deste tipo, escrever $\vec{P}=\varepsilon_{0}\chi_{e}\vec{E}=\varepsilon_{0} \frac{\chi_{e}}{\varepsilon}\vec{D}$:
$$\rho_{p}=- \nabla \cdot \vec{P}=-\nabla \cdot \left(\varepsilon_{0} \frac{\chi_{e}}{\varepsilon} \vec{D} \right)=- \left(\frac{\chi_{e}}{1+\chi_{e}} \right)\rho_{\ell}$$
### Equação de Laplace
- Ora, se tivermos $\rho_{\ell}=0$ (se não houverem cargas no dielétrico) temos $\rho_{p}=0$ e então $\rho=0$. Ou seja, apenas temos cargas na superfície.
- Num caso assim podemos usar a equação de Laplace dentro do dielétrico.
- Vejamos as **condições de fronteira**:
    - Temos, como sempre, $V^{+}=V^{-}$
    - Vimos que $D^{+}-D^{-}=\sigma_{\ell}$. Ora, sendo $\sigma_{\ell}=0$ temos: $$\begin{align*}
D^{+}&= D^{-}\\
\varepsilon^{+}E^{+}_{\perp} &= \varepsilon^{-}E_{\perp}^{-}
\end{align*}$$
    - Da condição acima podemos também escrever: $$\begin{align*}
\varepsilon^{+} \left( \frac{\partial V}{\partial n}\right)^{+}=\varepsilon^{-} \left(\frac{\partial V}{\partial n} \right)^{-}
\end{align*}$$

> **EXEMPLO**
> ![[campo por esfera dielétrica.png]]
> - Temos uma esfera composta por um dielétrico homogéneo e linear. Ela é sujeita a um campo externo uniforme $\vec{E_{0}}$. Queremos resolver a equação de Laplace dentro do dielétrico.
> ![[campo por esfera dielétrica - 2.png]]
> Temos as condições de fronteira: $$\begin{cases}
r=R ~~ &\to ~~ V^{-}=V^{+}\\
r=R ~~ &\to ~~ \varepsilon \frac{\partial V^{-}}{\partial r}=\varepsilon_{0} \frac{\partial V^{+}}{\partial r}\\
r\gg R~~&\to~~ V^{+}\to-E_{0}r\cos\theta\\
\end{cases}$$
> - Numa simetria esférica o potencial elétrico é dado por $$V(r,\theta)=\sum\limits_{\ell=0}^{\infty} \left(A_{\ell}r^{\ell} + \frac{B_{\ell}}{r^{\ell+1}}\right)P_{\ell}(\cos\theta)$$
> - Para que não tenhamos $V\to\infty$ em $r=0$, temos $B_{\ell}=0$ em $V^-$ e ficamos com $$V^{-}=\sum\limits_{\ell=0}^{\infty}A_{\ell}r^{\ell}P_{\ell}(\cos\theta) $$
> - Para não termos $V\to\infty$ quando $r\to\infty$ temos $A_\ell=0$ em $V^+$. Com isso e com a 3ª condição de fronteira temos:
> $$V^{+}=-E_{0}r\cos\theta + \sum\limits_{\ell=0}^{\infty}\frac{B_{\ell}}{r^{\ell+1}}P_{\ell}(\cos\theta)$$
> - A condição de fronteira 1 diz que $V^{-}(r=R)=V^{+}(r=R)$ e temos: $$\sum\limits_{\ell=0}^{\infty}A_{\ell}R^{\ell}P_{\ell}(\cos\theta)=-E_{0}R\cos\theta + \sum\limits_{\ell=0}^{\infty}\frac{B_{\ell}}{R^{\ell+1}}P_{\ell}(\cos\theta)$$
> de onde resulta: $$\begin{cases}
A_{\ell}R^{\ell}=\frac{B_{\ell}}{R^{\ell+1}} ~~~~~~~~~~~~~~~~ (\ell\neq1) \\
A_{1}=-E_{0}+ \frac{B_{1}}{R^{3}}~~~~(\ell=1)
\end{cases}$$- Da 2ª condição temos $\varepsilon \partial_{r}V^{-}=\varepsilon_{0} \partial_{r}V^{+} \to \varepsilon_{r}\partial_{r}V^{-}=\partial_{r}V^{+}$ (Notação do Ariel :D), ou seja: $$\varepsilon_{r}\sum\limits_{\ell=0}^{\infty} \ell A_{\ell}R^{\ell}P_{\ell}(\cos\theta)=-E_{0}\cos\theta + \sum\limits_{\ell=0}^{\infty}\frac{(\ell+1)B_{\ell}}{R^{\ell+1}}P_{\ell}(\cos\theta)$$
> de onde resulta: $$\begin{cases}
\varepsilon_{r}A_{\ell}R^{\ell-1}=\frac{-(\ell+1)B_{\ell}}{R^{\ell+2}}~~~~~~~~~~ (\ell\neq1) \\
\varepsilon_{r}A_{1}=-E_{0}+ \frac{2B_{1}}{R^{3}}~~~~~~~~~~~~~(\ell=1)
\end{cases}$$
> - Ora, destes 2 conjutnos de equações resulta: $$\begin{cases}
A_{\ell}=B_{\ell}=0\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad(\ell\neq1) \\
A_{1}= - \frac{3}{\varepsilon_{r}+2}E_{0} \quad;\quad B_{1}= \frac{\varepsilon_{r}-1}{\varepsilon_{r}+2}R^{3}E_{0} ~~~~~~~~~~~~~(\ell=1)
\end{cases}$$
> e resulta $$V^{-}(r,\theta)= - \frac{3E_{0}}{\varepsilon_{r}+2}r\cos\theta=- \frac{3E_{0}}{\varepsilon_{r}+2}z$$
> ou seja, temos $$\vec{E}^{+}=- \nabla V^{+}=\frac{3}{\varepsilon_{r}+2}E_{0}\hat{z}=\frac{3}{\varepsilon_{r}+2}\vec{E_{0}}$$
> e daqui resulta que o campo é *uniforme* dentro do dielétrico.
> - Podemos ainda determinar a densidade de carga de polarização: $$\sigma_{p}=\vec{P}\cdot \hat{n}=(\varepsilon_{0}\chi_{e}\vec{E})\cdot \hat{n}=\varepsilon_{0}(\varepsilon_{r}-1) \vec{E}\cdot\hat{r}=\frac{3\varepsilon_{0}(\varepsilon_{r}-1)}{\varepsilon_{r}+2}E_{0}\hat{z}\cdot \hat{r}=\frac{3\varepsilon_{0}(\varepsilon_{r}-1)}{\varepsilon_{r}+2}E_{0}\cos\theta$$