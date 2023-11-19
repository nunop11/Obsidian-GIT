## Teorema
- A solução da equação de Laplace numa região é única se $V$ for especificado na fronteira

### Demonstração
![[univocidade de solução.png]]
- Consideremos $V_{1},V_{2}$ 2 soluções da equação de Laplace com as mesmas condições. Ou seja: $\nabla^{2}V_{1}=0=\nabla^{2}V_{2}$
- Assim se definirmos $V_{3}=V_{1}-V_{2}$, este potencial será também solução pois $\nabla^{2}V_{3}=\nabla^{2}(V_{1}-V_{2})=\nabla^{2}V_{1}- \nabla^{2}V_{2}=0$
    - Além disso, temos que $V_{1}=V_{2}$ na fronteira (têm as mesmas condições de fronteira). Isso implica que $V_{3}$ será nulo na fronteira.
    - Temos ainda que $V_{3}$ é solução da equação de Laplace, pelo que não tem extremos fora da fronteira. Assim, se $V_{3}=0$ na fronteira então $V_{3}=0$ em toda a região.
- Assim temos que $V_{1}=V_{2}$. Ou seja, a **solução é único**.

## Corolário
- O potencial num volume é univocamente definido se especificarmos:
    - Densidade volúmica de carga na região.
    - Valor de potencial na fronteira.

### Demonstração
- Pode ser demonstrado de forma semelhante ao que temos acima, mas temos $\nabla^{2}V_{1}=- \frac{\rho}{\varepsilon_{0}}= \nabla^{2}V_{2}$

![[exemplo condutor com cavidades.png]]
## Teorema
- Num volume $\mathcal{V}$ conhecido, com densidade volúmica $\rho$. Nele temos regiões condutoras com carga $Q_{i}$. Nestas condições, o campo elétrico está univocamente determinado.
- Nos condutores podemos definir:
$$\frac{\partial V}{\partial n}=(\nabla V)^{+} \cdot \hat{n}=- \vec{E}^{+}\cdot \hat{n}=- E_{\perp}^{+}$$
e podemos calcular:
$$\frac{Q_{i}}{\varepsilon_{0}}= \int \vec{E}\cdot \hat{n}ds=- \int \frac{\partial V}{\partial n}ds$$

# Método das Imagens
![[metodo imagens.png]]
- Consideremos o problema acima à esquerda. Para $z=0$ temos $V=0$. No eixo dos $z$ à altura $d$ temos uma carga $q$. Podemos expressar como:
$$\nabla^{2}V=- \frac{q}{\varepsilon_{0}} \delta^{3}(\vec{r}-\vec{r}_{q})\quad \quad,\quad \quad \vec{r}_{q}=d \hat{e}_{z}$$
- Condições de fronteira
$$V=0~~,~~ z=0 \quad \quad;\quad \quad V\to0~~,~~ |\vec{r}|\gg d~~(~r\to\infty )$$
- E queremos então resolver a equação de Poisson para este sistema na região $z\ge0$ 
- Se encontrarmos uma solução para um sistema com uma geometria mais simples mas com as *mesmas condições de fronteira e densidade de carga*, essa solução também se aplicará a este sistema (porque as soluções são únicas).

- Consideremos então o sistema da figura da direita. Acrescentamos uma carga $-q$ na cota $-d$. Desta forma temos:
$$V(\vec{r})= \frac{q}{4\pi\varepsilon_{0}} \left[ \frac{1}{\sqrt{x^{2}+y^{2}+(z-d)^{2}} }- \frac{1}{\sqrt{x^{2}+y^{2}+(z+d)^{2}}}\right]$$
- Vemos logo que em $z=0$ temos $V=0$. A outra condição de fronteira também se verifica.
- Temos ainda que para $z<0$ os dois sistemas já diferem mais. No entanto, **apenas a região em que queremos resolver a equação de Poisson/Laplace**.
- Dito isto, o *método das imagens* consiste em colocar **cargas imagem** no espaço para conseguir determinar um sistema "equivalente" para facilitar a resolução da equação de Poisson.

