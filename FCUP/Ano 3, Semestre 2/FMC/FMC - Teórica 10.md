###### Aula 10 - 21/3/2024
**Continuação**
- Como vimos na aula anterior, podemos definir as várias redes de Bravais com 2 valores $\alpha_{1},\alpha_{2}$ e um ângulo $\varphi$. Assim, podemos definir o **vetores primitivos**: $\vec{a_{1}},\vec{a_{2}}$. Assim, podemos definir o **vetor de rede**:
$$\vec{R}=n_{1}\vec{a_{1}}+n_{2}\vec{a_{2}}$$
ou seja, todos os pontos da rede podem ser definidos com uma combinação linear dos vetores primitivos, em que $n_{1},n_{2}$ têm que ser INTEIROS.

- No entanto, para alguns materiais definidos por uma grelha de Bravais, se traçarmos a rede formada pelos átomos de carbono verificamos que eles não formam uma rede de Bravais:
![[Pasted image 20240326122326.png]]

### Bravais 3D
- Temos 14 redes de Bravais, que podem ser divididas em 7 sistemas cristalinos:
![[Pasted image 20240326123655.png]]


**Sistema Cúbico**
- Rede mais simétrica, consistindo de 6 qudrados juntos.
- Simetrias:
    - rotações de 120º em torno dos eixos ternários : [111] (eixo que passa no ponto $(1,1,1)$)
    - rotçações de 90º em tornos de 3 eixos perpendiculares (?)
    - rotações de 180º em torno das arestas
    - reflexão conforme os 3 planos perpendiculares aos eixos que definem a rede - eixos quaternários. Estes 3 planos são os que nos permitem dividir o cubo em 8 cubos menores.
    - reflexão segundo os planos que contêm os eixos binários (?)
- Temos *FCC* - face centrada (pontos no centro das fases) e *BCC* - corpo centrado (ponto no centro do cubo)

**Sistema Tetragonal**
- Obtido ao esticar a rede cúbica numa direção
- Temos quase as mesma simetrias que antes, mas perdemos:
    - rotação conforme eixos ternários
    - dois eixos de rotação quaternários (?)
- Ao esticar uma FCC poderíamos dizer que temos uma tetragonal de faces centradas, mas normalmente só consideramos *tetragonal de corpo centrado*, já que são equivalentes:
![[Pasted image 20240326124849.png]]

**Sistema Ortorrômbico**
- Obtido ao deformar 2 faces da Tetragonal. 
- NOTA: na cúbica temos $a=b=c$, na tetragonal temos $a=b\neq c$ e na ortorrômbica é tudo diferente.
- Simetrias:
    - rotações de 90º segundo 3 eixos perpendiculares (?) OU 1 eixo de rotação binário e 2 planos de reflexão que se intersetam no eixo (???)

**Sistema Monoclínico**
- Obtido ao comprimir uma ortorrômbica segundo uma diagonal -- inclinar uma ortorrômbica. Perdemos os 90º em 2 faces, mas mantemos nas restantes:
![[Pasted image 20240326125830.png|182]]
- Temos como simetrias: 1 eixo de rotação binário e 1 plano de reflexão.
- Monoclínica resulta de distorcer ortorrômbica simples ou base centrada. Monoclínica base centrada resulta de distorcer ortorrômbica face centrada.

**Sistema Triclínico**
![[Pasted image 20240326163213.png|300]]
- Obtido ao comprimir uma rede monoclínico, de forma que todos os pares de lados opostos sejam diferentes, tal que $\alpha\ne\beta\ne\gamma$.
- Apenas resta a simetria de inversão espacial.

**Sistema Romboédrico / Trigonal**
![[Pasted image 20240326163334.png]]
- Obtém-se ao esticar um cúbico conforme uma diagonal, de forma que temos arestas todas iguais e ângulos iguais, mas diferentes de 90º.
- Apenas temos um eixo de simetria ternário.

**Sistema Hexagonal**
![[Pasted image 20240326163440.png|300]]
- Conforme vemos acima, pode ser visto como uma repetição do sistema trigonal.
- Todos os cristais têm o mesmo eixo ternário (?)

**Primitivas e Não-Primitivas**
![[Pasted image 20240326163559.png]]
- Das redes acima mostradas, as não marcadas a azul são primitivas, as marcadas a azul são não-primitivas

**Exemplos**
- Ver o PPT para ver exemplos bonitos.

### Continhas
- Como sabemos, redes de Bravais implicam que temos translação garantida. Assim, podemos definir uma função $f(\vec{r})$ que irá cumprir $f(\vec{r})=f(\vec{r}+\vec{R})$. Assim, podemos fazer *transformada de Fourier* e temos:
$$\begin{align*}
\text{TF}(f(\vec{r}))&= f(\vec{k})\\
&= \frac{1}{V}\int d^{3}\vec{r} ~f(\vec{r})e^{i \vec{k}\cdot \vec{r}}\\
&= \frac{1}{V}\sum\limits_{\substack{n_{1}=-\infty\\n_{2}=-\infty}}^{+\infty} \int_{V_{primitivo}}d^{3}\vec{r}~ f(\vec{r}+\vec{R})e^{i \vec{k}\cdot(\vec{r}+\vec{R})}\\
&= \frac{1}{N_{cell}} \sum\limits_{n_{1},n_{2}}e^{i \vec{k}\cdot\vec{r}} \frac{1}{V_{cell}}\int d^{3}\vec{r}~ f(\vec{r})e^{i \vec{k}\cdot\vec{r}}
\end{align*}$$
idk aqui perdi-me.

- Isto somehow implica que $k$ é discreto, logo temos uma **rede recíproca**: $\vec{K}$.