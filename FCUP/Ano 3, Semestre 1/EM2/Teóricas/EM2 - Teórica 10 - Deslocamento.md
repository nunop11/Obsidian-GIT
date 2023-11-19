- Como vimos na aula anterior, quer quando temos átomo, moléculas apolares ou moléculas polares, no equilíbrio ficamos com $\vec{p}\parallel\vec{E}$. Ora, para um certo material dielétrico sujeito a um campo elétrico externo teremos isso mesmo.
- De tal forma é útil definir o **Momento dipolar po unidade de volume** AKA ==**Polarização**== :
$$\vec{P}=\frac{d \vec{p}}{dV} \quad \quad;\quad \quad (dV=d^{3}r)$$

- De acordo com a aula 8, para um Dipolo temos:
$$V(\vec{r})=\frac{1}{4\pi\varepsilon_{0}} \frac{(\vec{r}-\vec{r'})\cdot \vec{p}}{|\vec{r}-\vec{r'}|^3} $$
- Ora, se considerarmos que um material dielétrico é uma distribuição volúmica de dipolos, temos:
$$V(\vec{r})=\frac{1}{4\pi\varepsilon_{0}} \int \frac{(\vec{r}-\vec{r'})\cdot \vec{P}}{|\vec{r}-\vec{r'}|^{3}}d^{3}r'$$
Substituindo $\vec{r}=(x,y,z)~,~\vec{r'}=(x',y',z')$ conseguimos provar que:
$$\nabla' \left( \frac{1}{|\vec{r}-\vec{r'}|}  \right)= \frac{\vec{r}-\vec{r'}}{|\vec{r}-\vec{r'}|^3}$$
e ficamos com
$$V(\vec{r})=\frac{1}{4\pi\varepsilon_{0}}\int \vec{P}\cdot \nabla' \left( \frac{1}{|\vec{r}-\vec{r'}|}  \right) d^{3}r'$$
> Temos que $\tfrac{1}{|\vec{r}-\vec{r'}|}$ é uma função escalar e $\vec{P}$ um campo vetorial. Assim, podemos usar: $$\nabla \cdot(f \vec{A})=\nabla f \cdot\vec{A}+f\nabla\cdot\vec{A}~~\to~~ \vec{A}\cdot\nabla f=\nabla \cdot(f\vec{A})-f\nabla\cdot\vec{a}$$

- Obtemos:
$$\begin{align*}
V(\vec{r})&= \frac{1}{4\pi\varepsilon_{0}} \left[ \int \nabla'\cdot \left(\frac{\vec{P}}{|\vec{r}-\vec{r'}|}\right)d^{3}r' - \int \frac{1}{|\vec{r}-\vec{r'}|} (\nabla'\cdot \vec{P})d^{3}r' \right]\\
&= \frac{1}{4\pi\varepsilon_{0}} \oint \frac{1}{|\vec{r}-\vec{r'}|}(\vec{P}\cdot d \vec{s'}) - \frac{1}{4\pi\varepsilon_{0}} \int \frac{1}{|\vec{r}-\vec{r'}|} (\nabla'\cdot \vec{P})d^{3}r'
\end{align*}$$
(em que usamos o teorema de Gauss)
e obtemos:
$$V(\vec{r})=\frac{1}{4\pi\varepsilon_{0}}\oint \frac{\sigma_{p}}{|\vec{r}-\vec{r'}|}ds' + \frac{1}{4\pi\varepsilon_{0}}\int \frac{\rho_{p}}{|\vec{r}-\vec{r'}|} d^{3}r'$$

- Definimos então:
#### Densidade superficial de carga de polarização
- Consideremos uma tira de um dielétrico sujeito a um campo elétrico. É como se tivessemos muitos dipolos com a mesma direção e sentido. Podemos então imaginar que muitos dipolos pequenos são o mesmo que ter um dipolo muito longo:
![[explicacao de densidade sup carga polarizacao - 1.png]]
ou seja, é como se o campo fosse movendo eletrões para a ponta da direita, até termos uma concentração de carga constante.

![[explicacao de densidade sup carga polarizacao - 2.png]]
- Consideremos agora esta tira de material dielétrico que é paralela a $\vec{P}$.
    - Sendo $|\vec{P}|=P$ a densidade volúmica de momento dipolar, temos que o momento dipolar total da secção separada será $p_{total}=P \cdot Ad$
    - No entanto, tendo em conta o que temos acima, podemos considerar a secção como sendo apenas 1 dipolo grande e temos $p_{total}=qd$.
    - Assim, temos: $$q=PA \to \sigma_{p}=\frac{q}{A}=P$$
![[explicacao de densidade sup carga polarizacao - 3.png]]
- Se, por outro lado, a superfície no final $A_{end}$ não fosse  perpendicular a $\vec{P}$ teríamos $p_{total}=qd$ como antes, mas agora teríamos $p_{total}=d \cdot \vec{P}\cdot A_{end}\hat{n}=dA_{end} \vec{P}\cdot\hat{n}$. Daqui resulta: $$q=A_{end}\vec{P}\cdot\hat{n} ~~\to~~ \sigma_{p}= \frac{q}{A_{end}}=\vec{P}\cdot \hat{n}$$

#### Densidade volúmica de carga de polarização
- Consideremos que temos uma Polarização $\vec{P}$ não uniforme e divergente:
![[distribuição de carga volumica polarizacao.png]]
- Fica claro que se gera uma acumulação de carga negativa no interior e positiva no exterior. Estando este exemplo a ocorrer num material, as cargas positivas vão acabar na superfície. 
- Ora, para que se atinja o equilíbrio é preciso que a carga total acumulada no centro do material e a aquela acumulada na superfície sejam *iguais*.

- Ora, apesar de termos partido de um caso específico, isto é algo que tem de acontecer com qualquer Polarização exercida sobre um volume. Temos então:
$$\int \rho_{p}d^{3}r= -\oint \sigma_{p} ds$$
tendo em conta a definição de $\sigma_{p}$ que fizemos acima temos:
$$\begin{align*}
\int \rho_{p}d^{3}r&= -\oint \vec{P}\cdot \hat{n} ds\\
&= -\oint \vec{P}\cdot d \vec{s}\\
&= -\int \nabla \cdot \vec{P} d^{3}r
\end{align*}$$
de onde surge:
$$\rho_{p}= - \nabla \cdot \vec{P}$$

## Deslocamento Elétrico
- Temos então as fórmulas que nos dão as densidades de carga de polarização. Ora, estas cargas são as que geram o campo de polarização.
- No entanto, num dielétrico, podemos ter outras cargas - *cargas livres* - que também geram um campo.
- Assim, a densidade total de carga no dielétrico é:
$$\rho=\rho_{p}+\rho_{\ell}$$
partindo da lei de gauss diferencial podemos escrever:
$$\varepsilon_{0}\nabla \cdot \vec{E}=\rho=\rho_{p}+\rho_{\ell}$$
conforme o que temos acimma:
$$\varepsilon_{0}\nabla \cdot \vec{E}=-\nabla \cdot \vec{P}+ \rho_{\ell}$$
e podemos escrever:
$$\begin{align*}
\nabla \cdot (\varepsilon_{0}\vec{E}+\vec{P})&= \rho_{\ell}\\
\nabla \cdot \vec{D}&= \rho_{\ell}
\end{align*}$$
em que temos o **Deslocamento Elétrico**:
$$\boxed{\vec{D}=\varepsilon_{0}\vec{E}+\vec{P}}$$
- Temos ainda:
$$\oint \vec{D}\cdot \hat{n}ds=\int \nabla \cdot\vec{D}~d^{3}r=Q_{\ell}$$
- De notar que mutias vezes conseguimos determinar $\vec{D}$ sem conhecer $\vec{P}$
- Enquanto que na eletrostática, por definição, temos $\nabla \times \vec{E}=0$, normalmente temos $\nabla\times\vec{D}\neq0$ pois:
$$\nabla \times \vec{D}=\varepsilon_{0}(\nabla\times\vec{E})+(\nabla\times\vec{P})=\nabla \times \vec{P}$$
- Desta forma, apesar de $\vec{E}$ e $\vec{D}$ resultarem em "leis de gauss" muito parecidas, não podemos simplesmente pensar num problema de dielétricos como um problema normal em que substituimos $\vec{E}$ por $\vec{D}$ e $\rho$ por $\rho_{\ell}$.
- Da mesma forma, não nos podemos esquecer que densidades de carga $\rho_{\ell}$ não são as únicas que podemos ter.

> EXEMPLO:
> Consideremos que temos uma linha de carga com densidade $\lambda$ rodeada de um material dielétrico de espessura $a$. Queremos determinar $D$
> ![[exemplo calcular deslocamento.png]]
> Definiemos uma superfície gaussiana como acima, de comprimento $L$ e raio $s$ e temos: $$\begin{align*}
\oint \vec{D}\cdot d \vec{s}&= Q_{\ell}\\
D \cdot 2\pi s L&= L \lambda\\
D &= \frac{\lambda}{2\pi s} ~~~~\to~~~~ \vec{D}=\frac{\lambda}{2\pi s}\hat{s}
\end{align*}$$
> Podemos ainda, com isto, determinar que o campo elétrico fora do dielétrico (em que $\vec{P}=\vec{0}$) será: $$\vec{E}=\frac{\vec{D}}{\varepsilon_{0}}=\frac{\lambda}{2\pi\varepsilon_{0}s}\hat{s}$$

### Descontinuidades de $\vec{D}$
- Temos que $\nabla \cdot \vec{D}=\rho_{\ell}$. Conforme o teorema de Gauss podemos escrever:
$$(\vec{D}^{+}-\vec{D}^{-})\cdot \hat{n}=\sigma_{\ell} ~~~~\to~~~~ D^{+}-D^{-}=\sigma_{\ell}$$
- Acima obtivemos que $\nabla \times \vec{D}=\nabla \times \vec{P}$. Daqui temos:
$$\begin{align*}
D_{\parallel}^{+}-P_{\parallel}^{+}=D_{\parallel}^{-}-P_{\parallel}^{-}\\
D_{\parallel}^{+}-D_{\parallel}^{-}=P_{\parallel}^{+}-P_{\parallel}^{-}
\end{align*}  ~~~~\Biggr| \Longrightarrow \nabla \times(\vec{D}-\vec{P})=\nabla \times(\varepsilon_{0}\vec{E})=\vec{0}=(\vec{D}-\vec{P})\times \hat{n} $$
