- Na eletrstática consideramos que $\vec{B}=\vec{0}~,~ \vec{\mathcal{J}}=\vec{0}$ (sem cargas em movimento não temos campo magnético nem densidade de corrente)
- Ficamos então com as equações de Maxwell: $$\begin{align*}
\nabla \cdot \vec{E}&=  \frac{\rho}{\varepsilon_{0}}\\
\nabla \times \vec{E}&=  \vec{0} ~~~~\to~~~~ \vec{E}=-\nabla V 
\end{align*}$$
as restantes equações anulam-se.

## Carga Pontual
- Vejamos este caso conhecido com a equação de Maxwell. Temos uma carga $Q$
$$\begin{align*}
\int \nabla \cdot \vec{E} ~d^{3}r&= \int \frac{\rho}{\varepsilon_{0}}~d^{3}r\\
\oint \vec{E}\cdot d \vec{s}&= \frac{Q}{\varepsilon_{0}}\\
\end{align*}$$
pela simetria, o campo gerado será radial $\vec{E}=E \hat{r}$. Assim, consideremos que o integral é feito numa superfície esférica de raio $r$, pelo que o vetor de área infinitesimal será $d \vec{s}=ds \hat{r}$. Temos:
$$\begin{align*}
\oint E \hat{r}\cdot ds \hat{r}&= \frac{Q}{\varepsilon_{0}}\\
E\oint ds&= \frac{Q}{\varepsilon_{0}}\\
E 4\pi r^{2}&= \frac{Q}{\varepsilon_{0}}\\
E&= \frac{Q}{4\pi\varepsilon_{0}r^{2}}\to \vec{E}= \frac{Q}{4\pi\varepsilon_{0}r^{2}}\hat{r}=\frac{Q}{4\pi\varepsilon_{0}r^{3}}\vec{r}
\end{align*}$$

## Energia Eletrostática
- O trabalho associada a mover uma carga $Q$ será:
$$W=\int_{\vec{r}_{A}}^{\vec{r}_{B}} \vec{F}_{ext}\cdot d \vec{r}=-Q \int_{\vec{r}_{A}}^{\vec{r}_{B}} \vec{E}\cdot d \vec{r}=Q\int_{\vec{r}_{A}}^{\vec{r}_{B}}\nabla V \cdot d \vec{r}=Q(V_{B}-V_{A})$$
- Asim, consideremos o caso do costume: trazmoes $N$ cargas do infinito para as suas posições no sistema. 
    - Para a 1ª carga ainda não temos nenhuma campo elétrico presente. Assim: $W_{1}=0$
    - Para a 2ª carga temos que fazer trabalho ao longo do percurso para contrariar a força elétrica gerada pela carga $Q_{1}$, logo $W_{2}=Q_{2}V_{1}(\vec{r}_{2})= Q_{2} \frac{1}{4\pi\varepsilon_{0}} \frac{Q_{1}}{r_{12}}$ 
    - Para a 3ª carga temos $W_{3}=Q_{3}(V_{1}(\vec{r}_{3})+V_{2}(\vec{r}_{3}))=Q_{3} \frac{1}{4\pi\varepsilon_{0}} \left(\frac{Q_{1}}{r_{13}}+ \frac{Q_{2}}{r_{23}} \right)$ 

- Assim o trabalho total será:
$$W=\frac{1}{4\pi\varepsilon_{0}} \sum\limits_{i=1}^{N} \sum\limits_{j<i}^{N} \frac{Q_{i}Q_{j}}{r_{ij}} = \frac{1}{8\pi\varepsilon_{0}} \sum\limits_{i=1}^{N} \sum\limits_{\substack{j=1\\ j\neq i}}^{N} \frac{Q_{i}Q_{j}}{r_{ij}}= \frac{1}{2} \sum\limits_{i=1}^{N}Q_{i} \underbrace{\sum\limits_{\substack{j=1 \\ j\neq1}}^{N} \frac{1}{4\pi\varepsilon_{0}} \frac{Q_{j}}{r_{ij}}}_{=V_{j}(\vec{r}_{i})}$$

### Contínuo
- Consideremos agora o limite em que temos uma distribuição contínua de cargas. A equação de cima transforma-se na forma:
$$W=\frac{1}{2} \int dQ  =\frac{1}{2} \int\rho V d^{3}r=\frac{\varepsilon_{0}}{2}\int (\nabla \cdot \vec{E})V d^{3}r$$
em que se usou $dQ=\rho d^{3}r$ e $\rho= \varepsilon_{0} (\nabla \cdot \vec{E})$
- Uma igualdade de calculo vetorial que convém saber é:
$$\nabla \cdot (f \vec{A})=f \nabla \cdot \vec{A} + \vec{A}\cdot \nabla f ~~\to~~ f \nabla \cdot \vec{A}= \nabla \cdot (f \vec{A}) - \vec{A}\cdot \nabla f$$
substituindo na equação do trabalho obtemos:
$$\begin{align*}
W &=  \frac{\varepsilon_{0}}{2} \left[ \int \nabla \cdot (V \vec{E})d^{3}r - \int \vec{E}\cdot \underbrace{\nabla V}_{=- \vec{E}}d^{3}r\right]\\
&= \frac{\varepsilon_{0}}{2} \left[ \oint V \vec{E}\cdot d \vec{s} + \int |\vec{E}|^{2}d^{3}r \right]
\end{align*}$$
em que se usou o teorema do divergente no 1º termo.
- Ora, consideremos que estamos a integrar sobre *todo o espaço*. Temos que $\vec{E}\propto \frac{1}{r^{2}}, V\propto \frac{1}{r}, d \vec{s}\propto r^{2}$. Logo $\oint V \vec{E}\cdot d \vec{s}\propto \frac{1}{r}$. Consoante $r$ aumenta o integral diminui. Assim: $\oint V \vec{E}\cdot d \vec{s}\to0$. Fica então:
$$W= \frac{\varepsilon_{0}}{2}\int |\vec{E}|^{2}d^{3}r=U_{eletrostática}$$
(de notar que esta fórmula é apropriada para distribuições de carga contínua. Por exemplo, se aplicarmos esta fórmula a uma carga pontual iremos obter energia infinita)

