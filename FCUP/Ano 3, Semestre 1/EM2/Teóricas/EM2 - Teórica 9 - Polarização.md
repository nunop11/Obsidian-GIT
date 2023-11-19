# Campo Elétrico na Matéria
## Polarização
- Temos 2 grandes grupos de materiais: 
    - *Condutores* - Já vimos. Têm "infinitos" portadores de carga, na forma de eletrões "soltos"
    - *Isoladores / Dielétricos* - Não temos cargas livres, todas elas estão associadas a um átomo/molécula. Assim, os eletrões estão "presos" nos átomos, podendo apenas deslocar-se dentro deles.

- Assim, ao sujeitar dielétricos a um campo elétrico externo, os átomos podem ser polarizados, porque o campo gera forças opostas no núcleo e nos eletrões.
- Ora, temos então 2 efeitos a coexistir:
    - Por terem cargas opostas, o núcleo e os eletrões atraem-se
    - O campo elétrico externo cria forças que querem afastar o núcleo e os eletrões

- Temos então que cada átomo tem um pequeno dipolo em si. Temos então a **polarização atómica**:
$$\vec{p}=\alpha \vec{E}$$

### Modelo Simples
![[polarizacao de átomo - modelo simples.png]]
- Consideremos um modelo simples do átomo, com uma carga $+q$ no centro AKA núcleo. À sua volta temos uma distribuição contínua e uniforme de carga, com carga total $-q$ AKA nuvem elétronica. Consideremos que a nuvem tem densidade de carga constante e igual a $$\rho=\frac{-q}{\frac{4}{3}\pi a^{3}}$$
- Conforme a segunda figura, fazemos passar um campo externo $\vec{E}$ pelo átomo, que "desloca" o núcleo / a carga $+q$. 
- Podemos definir um volume dentro do átomo:
![[polarização - modelo simples - explicação.png]]
que terá carga $q^{*}$ (apenas consistindo de elementos da nuvem eletrónica), que podemos definir como:
$$q^{*}= \rho \cdot \frac{4}{3}\pi d^{3}=\frac{-q}{\frac{4}{3}\pi a^{3}} \frac{4}{3}\pi d^{3}=-q \frac{d^{3}}{a^{3}}$$
- Para atingirmos o equilibrio, é preciso que $E_{q^{*}}=E_{ext}$. Ora, podemos escrever:
$$E_{q^{*}} = \frac{|q^{*}|}{4\pi\varepsilon_{0}d^{3}}=\frac{qd}{4\pi\varepsilon_{0}a^{3}}=\frac{p}{4\pi\varepsilon_{0}a^{3}}$$
ora, sendo $d$ a distância a que o núcleo está do centro do átomo quando se atinge equilíbrio, então temos:
$$\frac{p}{4\pi\varepsilon_{0}a^{3}}=E\to p=4\pi\varepsilon_{0}a^{3}E$$
ou seja, $$\alpha=4\pi\varepsilon_{0}a^{3}=4\varepsilon_{0}V$$

### Modelo mais complexo - Molécula
![[molecula apolar.png]]
- No modelo que vimos acima, o átomo é uma esfera e a direção do campo é irrelevante. Not anymore.
- Num modelo como o que temos agora, a direção do campo externo importa.
- Podemos então aplicar o campo num direção $E_\perp$ ou numa direção $E_\parallel$ ou combinação de ambas. Temos então:
$$\vec{p}=\alpha_{\perp}\vec{E}_{\perp}+\alpha_{\parallel}\vec{E}_{\parallel}$$
(no caso do $CO_2$ temos que $\alpha_{\parallel}\propto2\alpha_{\perp}$)
- De uma forma generalizada temos: $$p_{i}=\sum\limits_{j} \alpha_{ij}E_{j}$$

![[molecula polar + campo eletrico.png]]
- No caso de moléculas que já têm $\vec{p}\neq0$ sem campo externo, elas tendem a alinhar-se com o campo elétrico.
- Por exemplo da molécula de água acima, temos um $\vec{p}$ da carga negativa ao centro de carga positiva. As forças que irão surgir devido ao campo estão representadas à direita: gera-se *torque*, que é descrito por:
$$\begin{align*}
\vec{M}&= (\vec{r}_{+}\times\vec{F}_{+})+(\vec{r}_{-}\times\vec{F}_{-})\\
&= \left(\frac{1}{2}\vec{d}\times q\vec{E}\right) + \left(\frac{-1}{2}\vec{d}\times (-q)\vec{E}\right)\\
&= q \vec{d} \times \vec{E}\\
&= \vec{p}\times \vec{E}
\end{align*}$$
ou seja, para que se atinja equilíbrio, a molécula irá reorganizar-se de forma a ter $\vec{p}\parallel\vec{E}$.