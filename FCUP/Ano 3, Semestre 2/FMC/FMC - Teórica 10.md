###### Aula 10 - 21/3/2024
**Continuação**
- Como vimos na aula anterior, podemos definir as várias redes de Bravais com 2 valores $\alpha_{1},\alpha_{2}$ e um ângulo $\varphi$. Assim, podemos definir o **vetores primitivos**: $\vec{a_{1}},\vec{a_{2}}$. Assim, podemos definir o **vetor de rede**:
$$\vec{R}=n_{1}\vec{a_{1}}+n_{2}\vec{a_{2}}$$
ou seja, todos os pontos da rede podem ser definidos com uma combinação linear dos vetores primitivos, em que $n_{1},n_{2}$ têm que ser INTEIROS. Temos então:
--------- caderno 1 ----------

- No entanto, para alguns materiais definidos por uma grelha de Bravais, se traçarmos a rede formada pelos átomos de carbono verificamos que eles não formam uma rede de Bravais:
---------- caderno 2 -----------

**Bravais 3D**
------------- ver pdf prof ou ashcroft ------------


**Continhas**
- Como sabemos, redes de Bravais implicam que temos translação garantida. Assim, podemos definir uma função $f(\vec{r})$ que irá cumprir $f(\vec{r})=f(\vec{r}+\vec{R})$. Assim, podemos fazer *transformada de Fourier* e temos:
$$\begin{align*}
\text{TF}(f(\vec{r}))&= f(\vec{k})\\
&= \frac{1}{V}\int d^{3}\vec{r} ~f(\vec{r})e^{i \vec{k}\cdot \vec{r}}\\
&= \frac{1}{V}\sum\limits_{\substack{n_{1}=-\infty\\n_{2}=-\infty}}^{+\infty} \int_{V_{primitivo}}d^{3}\vec{r}~ f(\vec{r}+\vec{R})e^{i \vec{k}\cdot(\vec{r}+\vec{R})}\\
&= \frac{1}{N_{cell}} \sum\limits_{n_{1},n_{2}}e^{i \vec{k}\cdot\vec{r}} \frac{1}{V_{cell}}\int d^{3}\vec{r}~ f(\vec{r})e^{i \vec{k}\cdot\vec{r}}
\end{align*}$$
idk aqui perdi-me.

- Isto somehow implica que $k$ é discreto, logo temos uma **rede recíproca**: $\vec{K}$.

