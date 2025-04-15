  # Aprendizagem Empírica
## Aprendizagem Supervisionada
- Consiste em prever os valores de 1+ outputs $Y$ para um certo valor de entrada $X$
- As previsões feitas baseiam-se num conjunto de treino $(\text{x}_{i},y_{i})$ que consiste em casos já conhecidos e/ou resolvidos
- Se $(X,Y)$ são VAs com uma densidade de probabilidade conjunta $P(X,Y)$, então a aprendizagem supervisionada consiste na estimação da densidade de probabilidade $P(Y|X)$
- Algumas approaches:
    1. Modelos generativos - Começamos por determinar a probabilidade conjunta $p(x,y)$ e com ela determinamos os posteriors $p(y|x)$
    2. Determinar a probabilidade condicional $p(y|x)$ e depois fazer a média
    3. Modelos discriminativos - determinar a densidade diretamente com os dados de treino
- O que temos visto até agora

## Aprendizagem não supervisionada
- Consiste em determinar as propriedades da distribuição $p(x)$ sem um supervisor que diz se uma previsão está correta ou errada ou quão longe.
- Mais concretamente, queremos encontrar regiões do espaço em que temos maior densidade de pontos
- Algumas técnicas:
    - **Redução de dimensão** (análise componentes principais, escalamento multidimensional, mapas auto-organizáveis) - estas técnicas tentam *resumir a informação* de dados de muitas dimensões em menores dimensões. Isso facilita a visualização e análise dos dados (é mais fácil encontrar um mínimo 2D do que 3D)
    - **Análise de clusters** - consiste em dividir os dados em clusters (os pontos dentro de um cluster são semelhantes e distintos dos outros clusters). Em princípio, os clusters indicam pontos com maior densidade de pontos AKA onde temos picos da distribuição de probabilidade. Alguns métodos: K-Means, clustering hierárquico
    - **Regras de Associação** - Tentamos encontrar relações entre as variáveis com regras simples (conjuntivas). Do tipo: "se alguém comprou gin e gelo, é provável que compre água tónica". Isto permite determinar as regiões com maior densidade.

### Regras de Associação
- Maioritariamente usado com grandes sets de dados
- Em aprendizagem não supervisionada queremos encontrar os valores de $X$ que aparecem com maior frequência.
**Algoritmo Apriori**
- O algoritmo encontra relações de semelhança entre items.
- Isto é feito com uma abordagem *bottom-up*, ou seja, começa por fazer subconjuntos pequenos e gradualmente vai combinando-os em conjuntos maiores.
    1. Primeiro, definimos um valor mínimo C. Um certo item só é considerado para as regras se aparecer em >=C observações. Fazemos a lista de items a considerar.
    2. Segundo, o algoritmo gera todas as combinações de 2 items. Para cada combinação, é verificado em quantas observações os items aparecem juntos.
    3. Depois, apenas passam para a iteração seguinte os grupos que aparecem todos juntos em >=C observações.
    4. Em cada iteração, o algoritmo acrescenta 1 item a cada combinação que sobreviveu. 
    5. Isto continua até que nenhuma combinação é contada em nenhuma observação

### Análise de Cluster
- Fazemos grupos/clusters de dados de forma que todos os pontos dentro de um cluster são mais semelhantes entre si do que com qualquer ponto fora (semelhança alta intra-class, semelhança baixa inter-class)
    - Por exemplo, alguns objetos podem ser definidos pelas suas dimensões ou pela forma como se comportam com outros objetos
- Mas o que é semelhança? Para muitos algoritmos, consideramos semelhança como sendo **proximidade / distância**
- Ou seja, agrupamos clusters de pontos mais próximos. Claramente, estes grupos marcam zonas de alta densidade de probabilidade.

#### Dissimilarity index
- NOTA: para me poupar o trabalho a escrever: DS=dissimilaridade, SS=similaridade 
- O que usamos para definir se algo é próximo/similar ou não. Consiste numa função do tipo $$\gamma: E \times E\to R$$
1. Uma função $d:E\times E\to R_{0}^{+}$ é um *índice de DS* se 
    - a) $d(x,x)=0$ para qualquer $x$ (um ponto não dista de si próprio)
    - b) $d(x_{2},x_{1})=d(x_{2},x_{1})$ (a distância não depende do sentido)
2. Um índice de DS $d$ também é um *índice de distância* se, além de a) e b), tiver a propriedade c):
    - c) $d(x_{1},x_{2})=0\to x_{1}=x_{2}$ (intuitivo)
3. Um índice de distância $d$ também é uma *função de distância* se, além de a),b) e c), tiver a propriedade d):
    - d) $d(x_{1},x_{2})\le d(x_{1},x_{3})+d(x_{3},x_{2})$ (intuitivo)
4. Uma função de distância $d$ também é *ultramética* se, além de a)-d), tiver a propriedade e):
    - e) $d(x_{1},x_{2})\le\max\{d(x_{1},x_{3}),d(x_{3},x_{2})\}$ (versão mais forte da d), faz sentido se desenharmos - se $x_3$ está perto de $x_{1}$ estará longe de $x_{2}$ e vice-versa)

**Propriedades de distâncias**
- Meio que estamos a repetir aquilo acima, mas pronto:
$$\begin{align*}
\text{Simetria} &: &&&D(A,B)&=D(B,A)\\
\text{Auto-semelhança} &: &&&D(A,A)&=0\\
\text{Separação} &: &&&D(A,B)&=0~\to~ A=B\\
\text{Desigualdade triangular} &: &&&D(A,B)&\le D(A,C) + D(B,C)
\end{align*}$$
a lógica da desigualdade triangular é que NÃO podemos dizer: "A é parecido a B, B é parecido a C. A e C são muito diferentes" - não faz sentido

**Exemplos para variáveis quantitativas**
![[tipos de distancias.png]]

**Exemplos para variáveis binárias**
- Para este tipo de variáveis normalmente não usamos distância para medir a similaridade. 
- Consideremos 2 vetores $\mathbf{x},\mathbf{z}$ cujos componentes são binários: $\mathbf{x}=\begin{pmatrix}x_{1} & x_{2} & \cdots & x_{d}\end{pmatrix}^{T}~,~\mathbf{z}=\begin{pmatrix}z_{1} & z_{2} & \cdots & z_{d}\end{pmatrix}^{T}$
- Percorremos todas as coordenadas $k$ e contamos quantas vezes ocorrem os 4 casos possíveis:
    - a) $x_{k}=1,z_{k}=1$
    - b) $x_{k}=1,z_{k}=0$
    - c) $x_{k}=0,z_{k}=1$
    - d) $x_{k}=0,z_{k}=0$
![[casos de variaveis binarias.png|133]]
- E temos uma série de coeficientes/índices:
    - Matching coefficient: $\frac{a+b}{a+b+c+d}$
    - Índice de Russel e Rao: $\frac{a}{a+b+c+d}$
    - Índice de Jacard: $\frac{a}{a+b+c}$

##### Edit distance / Transformation distance
- Uma forma de medir a semelhança (ou falta dela) entre 2 objetos consiste em transformar um deles no outro e ver quanto esforço foi necessário.
    - Esse esforço será a distância
- Tipo assim:
![[distancia como medida de esforço.png]]

#### Similarity Index
- O mais comum é o coeficiente de correlação de Pearson:
$$r_{xz}=\frac{\sum\limits_{i=1}^{D}(x_{i}-\overline{x})(z_{i}-\overline{z})}{\sqrt{\sum\limits_{i=1}^{D}(x_{i}-\overline{x})^{2}\sum\limits_{i=1}^{D}(z_{i}-\overline{z})^{2}}}$$

### Categorias de algoritmos de clustering
- Clustering com hierarquia
- Clustering sem hierarquia
    - Clustering combinatório ou de partições: trabalhamos diretamente com os dados, sem referência a uma densidade de probabilidade
    - Clustering baseado em modelo: assumimos que os dados são samples de uma população com uma distribuição específica
    - Existem ainda modelos que atuam de forma não-paramétrica, determinando de forma direta os máximos de densidade

#### Clustering combinatório ou de partições
- Os dados são divididos em K clusters de modo que: cada observação está em 1 cluster e todos os clusters são disjuntos.
- Fazemos todas as combinações possíveis.
- Queremos encontrar a combinação de clusters que optimiza uma certa função de avaliação 
    - Por exemplo, se esta nos dá a distância total, queremos minimizá-la. Essa função seria: $J(C)=\frac{1}{2}\sum_{k=1}^{K}\sum_{C(i)=k}\sum_{C(i')=k}d(x_{i},x_{i'})$
    - Podemos simplificar esta função se definirmos um coeficiente binário $r_{nk}=\{0,1\}$ que nos diz se uma observação $\mathbf{x}_{k}$ está numa partição/cluster $k$. Ficamos com:$$J(C)=\frac{1}{2}\sum\limits_{k=1}^{K}\sum\limits_{i=1}^{N}\sum\limits_{j=1}^{N}r_{ik}r_{jk}d(x_{i},x_{j})$$
    - Esta função mede a distância total entre pontos da mesma classe (um termo só é não-nulo se $i,j$ ambos pertencem à classe $k$)
    - Podemos calcular a dispersão total e converter $J(C)$ num valor relativo $J/T$, sendo $T=\frac{1}{2}\sum_{i=1}^{N}\sum_{j=1}^{N}d(x_{i},x_{j})$
- Assim, análise de clusters é mais um problema de otimização.
- O método acima indicado expande de forma combinatória, que está relacionada com fatoriais. Assim, isto só é fazível se tivermos datasets pequenos. 
- Assim, um método fazível consiste em começar com uma combinação inicial. Depois, vamos fazendo alterações em busca de uma optimização local.

##### K-means
- Principalmente para valores quantitativos
- Usamos distância euclidiana: $J(C)=\sum_{k=1}^{K}\sum_{i=1}^{N}\sum_{j=1}^{N}r_{ik}r_{jk}\|x_{i}-x_{j}\|^{2}$
- Mas, podemos reescrever isto como algo relativo ao valor médio:
$$\sum\limits_{i=1}^{N}\sum\limits_{j=1}^{N}\|x_{i}-x_{j}\|^{2}=2N\sum\limits_{i=1}^{N}\|x_{i}-\overline{x}\|^{2}$$
e ficamos com
$$J(C)=\sum\limits_{k=1}^{K}\sum\limits_{i=1}^{N}r_{ik}\|x_{i}-\mu_{k}\|^{2}$$
- Queremos então determinar os $r_{nk},\mu_{k}$ que minimizam $J$

- Como fazer K-means:
    1. Escolher valores iniciais $\{\mu_{k}\}$
    2. Repetir estes passos várias vezes:
        1. Minimizar $J$ relativamente a $r_{nk}$, com $\mu_{k}$ fixo. Para isso, definir: $$r_{nk}=\begin{cases}1 & ; &k=\text{argmin}_{j}\|x_{n}-\mu_{j}\|^{2} \\0 & ; & \text{restantes casos}\end{cases}$$ (ou seja, atribuir cada ponto ao cluster com centro mais próximo dele)
        2. Minimizar$J$ relativamente a $\mu_{k}$, com $r_{nk}$ fixo. Teremos um mínimo onde a derivada é nula. Como $J$ é quadrático com $\mu_{k}$, a sua derivada será linear. Para a zerar temos $$\mu_{k}=\frac{\sum\limits_{n}r_{nk}\mathbf{x}_{n}}{\sum\limits_{n}r_{nk}}$$(isto não passa de calcular a média dos pontos em cada cluster)
        3. Ou seja: ponto 2.1 altera os pontos que estão atribuidos a cada cluster. O ponto 2.2 altera as médias um pouco, de acordo com isso. Lentamente, estes passos vão convergendo para um mínimo de $J$.
- Vejamos um exemplo de como este método funciona na prática:
![[evolucao algoritmo clustering.png]]

##### Soft K-means
- Como acabamos de ver, em K-means os coeficietes $r_{nk}$ só podem ser 0 ou 1.
- Ou seja, se tivermos um ponto exatamente entre 2 centroides, temos que o colcoar num só cluster, o que não é muito correto.
- Assim, em soft k-means temos: $r_{nk}\in[0,1]$, em que:
$$r_{nk}=\frac{G (\|x_{n}-\mu_{k}\|^{2})}{\sum_{\ell=1}^{K}G(\|x_{n}-\mu_{\ell}\|^{2})}$$em que $G()$ é uma função decrescente.

##### K-medoids
- K-means tem 2 problemas causados por usarmos distância euclidiana:
    - Todos os dados têm que ser quantitativos não binários
    - Por ser quadrática, esta distância dá (demasiada) importância a distâncias grandes. Assim, este método será bastante afetado por outliers.
- Uma forma de generalizar isto é usar uma função que mede a DS $d(\cdot,\cdot)$.
- Teremos então
    1. Para uma combinação de clusters: em cada cluster, encontrar a observação que minimiza a distância às outras observações: $$i_{k}^{*}=\text{argmin}_{i:C(i)=k}\sum\limits_{C(i')=k}d(x_{i},x_{i'})$$ e passamos a ter novas estimativas de centroides de clusters: $m_{k}=x_{i_{k}^{*}}$
    2. Para a nova combinação de centrodies $\{m_{1},\cdots,m_{K}\}$: minimizar o erro ao atribuir cada ponto à classe do centroide mais próximo: $$C(i)=\text{argmin}_{1\le k\le K}d(x_{i},m_{k})$$
    3. Repetir 1 e 2 até as atribuições dos pontos a clusters não mudarem.

#### Clustering baseado em modelo
##### Mistura de gaussianas
- Assumimos que os dados são observações tiradas de uma distribuição  que é a mistura de K "fontes de dados" - os clusters
- Assumindo que cada uma dessas "fontes" tem distribuição normal, a distribuição dos dados será:$$p(\mathbf{x})=\sum\limits_{k=1}^{K}\pi_{k}N(\mathbf{x}|\mu_{k},\sigma_{k})$$
em que $\sum_{k}\pi_{k}=1$
- As probabilidades posterior $p(k|\mathbf{x}_{n})$ dizem-nos se uma observação $n$ pertence a um cluster $k$. Estas podem ser determinadas com o teorema de Bayes:
$$r_{nk}=p(k|\mathbf{x}_n)=\frac{p(\mathbf{x}_{n}|k)p(k)}{\sum_{j=1}^{K}p(\mathbf{x}_{n}|j)p(j)}=\frac{\pi_{k}N(\mathbf{x}_{n}|\mu_{k},\sigma_{k})}{\sum_{j=1}^{K}\pi_{j}N(\mathbf{x}_{n}|\mu_{j},\sigma_{j})}$$
em que $\pi_{k}=p(j)$.
- E temos a log-likelihood:
$$\ln p(X|\pi,\mu,\sigma)=\sum\limits_{n=1}^{N}\ln \left[\sum\limits_{k=1}^{K}\pi_{k} N(\mathbf{x}|\mu_{k},\sigma_{k}) \right]$$

**Algoritmo de maximização de expectativa - Algoritmo EM**
- Encontrar um extremo, como sabemos, consis em tornar a derivada nula. Queremos minimizar o log-likelihood, logo:
    - Tornar a derivada de $\ln p$ relativamente a $\mu_{k}$ nula: $$\mu_{k}=\frac{1}{N_{k}}\sum\limits_{n=1}^{N}r_{nk}\mathbf{x}_{n}$$
    - Tornar a derivadade $\ln p$ relativamente a $\sigma_{k}$ nula: $$\sigma_{k}=\frac{1}{N_{k}}\sum\limits_{n=1}^{N}r_{nk} \cdot(\mathbf{x}_{n}-\mu_{k})(\mathbf{x}_{n}-\mu_{k})^{T}$$
    - Tornar a derivada de $\ln p$ relativamente a $\pi_{k}$ nula: $$\pi_{k}=\frac{N_{k}}{N}$$
- Em que $N_{k}=\sum_{n=1}^{N}r_{nk}$ é o número de pontos no cluster $k$.

**O algoritmo em si**
1. Inicializar as médias $\mu_{k}$, covariâncias $\sigma_{k}$ e coeficientes de mixing $\pi_{k}$
2. Passo **E** (Expectativa) - Determinar os coeficientes $r_{nk}=\frac{\pi_{k}N(\mathbf{x}_{n}|\mu_{k},\sigma_{k})}{\sum_{j=1}^{K}\pi_{j}N(\mathbf{x}_{n}|\mu_{j},\sigma_{j})}$
3. Passo **M** (Maximização) - Atualizar os valores da média, covariância e mixing:
$$\begin{align*}
\mu_{k}^{\text{new}}&= \frac{1}{N_{k}}\sum\limits_{n=1}^{N}r_{nk}\mathbf{x}_{n}\\
\sigma_{k}^{\text{new}}&= \frac{1}{N_{k}}\sum\limits_{n=1}^{N}r_{nk} \cdot(\mathbf{x}_{n}-\mu_{k}^{\text{new}})(\mathbf{x}_{n}-\mu_{k}^{\text{new}})^{T}\\
\pi_{k}^{\text{new}}&= \frac{N_{k}}{N}
\end{align*}$$
![[evolucao algoritmo clustering 2.png]]
- Pode ser demonstrado que EM converge para um máximo dos posteriors, sem nunca calcular diretamente a log likelihood.

**EM - mais teórico**
- Temos os dados $\mathbf{x}$ e os parâmetros $\boldsymbol{\theta}$. Assumimos um qualquer prior $p(\boldsymbol{\theta})$
- Sabemos que uma probabilidade posterior $p(\boldsymbol{\theta}|\mathbf{x})$ é proporicional a $p(\mathbf{x}|\boldsymbol{\theta})p(\boldsymbol{\theta})$
- Seria mais fácil determinar $\boldsymbol{\theta}$ com MAP se tivessemos mais dados $\mathbf{z}$ tal que:
$$p(\mathbf{x}|\boldsymbol{\theta})=\int p(\mathbf{x};\mathbf{z}|\boldsymbol{\theta})d \mathbf{z}$$
- EM é um algoritmo iterativo que converge para um MAP de $p(\boldsymbol{\theta}|\mathbf{x})$.

- Podemos definir $\boldsymbol{u}=(\mathbf{x};\mathbf{z})$ como sendo os *dados completos*, em que $p(\boldsymbol{u}|\boldsymbol{\theta})$ é a *função de likelihood completa*
- Em vários casos, os dados extra ($\mathbf{z}$) são inseridos de forma artificial, de modo a fazer com que EM funciona em casos difíceis.
    - Especialmente quando é difícil maximizar $p(\mathbf{x}|\boldsymbol{\theta})$ em relação a $\boldsymbol{\theta}$, mas em que existe um modelo $p(\mathbf{x};\mathbf{z}|\boldsymbol{\theta})$ fácil de maximizar em relação a $\boldsymbol{\theta}$.

- Tecnicamente, o algoritmo funciona assim:
![[em teoricamente.png]]

#### Clustering hierárquico
- Não é preciso especificar o número de clusters $K$
- Usam uma medida de DS entre grupos de observações, baseando-se na DS entre pares de elementos dentro de um grupo
- Gera-se uma representação hierárquica: os clusters de um nível são criados ao juntar aqueles do grupo abaixo.
    - No nível mais alto temos 1 só cluster, no nível mais baixo cada cluster tem 1 observação.
- Temos 2 estratégias opostas: bottom-up (ir juntando) ou top-down (ir dividindo)
- Naturalmente, o DS dentro de um grupo de observações é *crescente* consoante subimos o nível e agrupamos mais clusters com este.
- Temos:
![[cluster hierarquia.png]]
- A altura da linha horizontal que une 2 clusters é proporcional ao nível de DS entre os 2 grupos filhos (por exemplo: entre $g,h$ temos pouca DS, entre $a,\{b,c,d,e\}$ temos muita DS)
- Estamos a impor uma estrutura hierárquica, *mesmo que não exista*

##### DS inter-grupo
- Queremos sempre unir os grupos com menor distância. A diferença é na forma como calculamos a distância. Temos 3 maneiras
    - a) Single linkage (SL):
    $$d(A,B)=\min_{x\in A,y\in B}d(x,y)$$
    - b) Complete linkage (CL): 
    $$d(A,B)=\max_{x\in A,y\in B}d(x,y)$$
    - c) Group average (GA):
    $$d(A,B) = \frac{1}{\text{card}(A)\text{card}(B)}\sum\limits_{x\in A,y\in B}d(x,y)$$
![[tipos dists cluster hierarquico.png]]

**SL - distância euclidiana**
![[cluster hierarquico sl.png]]
- O que definimos em baixo é uma *matriz de distância*. Nela temos todas as combinações de conjuntos e respetivas distâncias.
- Vamos agrupando os pontos. Na matriz, o que acontece é que temos sempre uma matriz upper-triangular. Juntamos a combinação que corresponde ao menor valor (2,3 acima)
    - $a,b$ são os pontos mais próximos. Juntamos.
    - $\{a,b\}$ está mais próximo de $c$ do que de $d$. Além disso, está mais próximo de $c$ do que $c,d$ estão um do outro. Jutamos.
    - A menor distância entre $\{a,b,c\}$ e $d$ é 4. Juntamos.
- Como podemos ver, SL tende a criar cadeias como vimos acima. Ou seja, podemos obter clusters com alto diâmetro.

**CL - distância euclidiana**
![[cluster hierarquico cl.png]]
- A lógica é parecida, mas agora queremos a maior distância. Novamente, juntamos a combinção que corresponde ao menor valor da matriz (2,4 acima). 
- A diferença é que ao medir, por exemplo $d(\{a,b\},c)$ usamos a maior distância possível: 5 (comprimento do segmento que une o $a$ ao $c$. No SL usaríamos o segmento que une $b$ e $c$) 

## Aprendizagem Semi-Supervisionada
- Em **aprendizagem supervisionada** descobrimos padrões nos dados que relacionam os atributos com os outputs/classificações. Esses padrões são usados para prever os valores de dados futuros.
- Em **aprendizagem não supervisionada** as dadas não têm labels. Exploramos os dados para encontrar estruturas neles.
- Em **aprendizagem semi-supervisionada** temos uma mistura de dados labeled e não labeled. Normalmente, temos muitos dados unlabeled disponíveis. Tentamos aproveitar os dados todos para ter melhor resultados do que só com não supervisionada.
- Uma forma de fazer isto é usar um set de dados labeled de tamanho decente. Com esta treinamos um classificador C. Com esse, podemos depois label dados sem label.

### Dados e labels
- Dados labeled são dados que sabemos que correspondem a uma certa classe/label.
- Mas estes são difíceis de obter porque:
    - implicam que alguém atribui labels manualmente
    - podem obrigar que experts façam o labelling
    - fazer o labelling é muito consumidor de tempo

