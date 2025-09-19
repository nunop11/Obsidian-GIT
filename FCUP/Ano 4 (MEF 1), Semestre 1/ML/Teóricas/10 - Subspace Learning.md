# Tipos de aprendizagem
## Supervisionada
- Prevemos o valor de 1+ outputs $Y$ usando um set de inputs $X$
- As previsões são feitas após treinar um modelo com um set de treino $(\mathbf{x}_{i},\mathbf{y}_{i})$. Estes são casos já resolvidos em que $\mathbf{y}_{i}$ estão corretos
- Considerando que $(X,Y)$ são VAs com densidade de probabilidade conjunta $P(X,Y)$, então podemos ver a aprendizagem supervisionada como um problema de estimar as probabilidades posterior $P(Y|X)$
- Assim, temos 3 approachs para resolver o problema de atribuir $Y$:
    - *modelos generativos*: primeiro determinar a distribuição conjunta $p(x,y)$ (ou $p(x,\mathcal{C}_{k})$). Usar estas para obter as posteriors $p(y|x)$
    - primeiro determinar as densidades $p(y|x)$ e com estas determinar a média de condicionais
    - determinar uma função de regressão diretamente dos dados de treino

## Não supervisionado
- Aprendizagem não supervisionada determina as propriedades da densidade $p(x)$. Sem um supervisor que nos diz se uma resposta é correta ou errada, estes modelos determinam o valor correto ou um nível de erro.
- Temos:
    - existem vários métodos (self-organizing maps, principal curves...) que funcionam para dados com baixas dimensões
    - cluster analysis
    - association rules

### Self-organizing maps (SOM)
- Começamos com um set de datapoints $\mathbf{x}_{i}\in\mathbb{R}^{d}$ e um set de protótipos no mesmo espaço $p_{i}\in\mathbb{R}^{d}$
- Podemos fazer uma analogia entre este método e K-means
    - encontramos o protótipo mais "próximo" do ponto de dados atual. Esse é o "protótipo vencedor".
    - associados esse datapoint atual ao protótipo 
    - atualizamos o protótipo para ter em conta os dados
    - isto minimiza o erro médio de quantização: $\tfrac{1}{N}\sum_{n=1}^{N}\sum_{k=1}^{K}\|x_{n}-p_{k}\|^{2}$
- Ou seja, é uma espécie de K-means em alta dimensão
- Podemos ainda introduzir o conceito de "vizinhança" nos protótipos
    - podemos com isso implementar K-means

#### Vizinhanças
- protótipos estão associados a certos datapoints (coordenadas) numa estrutura de *baixa-dimensão* (manifold) no espaço de destino (normalmente um espaço 2d ou 3d - algo mais "normal")
- A vizinhança é definida como uma função $h$ neste manifold
    - Aqui podemos ter protótipos "adjacentes"/próximos. Isto não quer necessariamente dizer que eles são semelhantes, só que têm uma distância reduzida.

#### Treino
Apesar da descrição do método parecer K-means, o processo de treino faz lembrar mais algo tipo o método de Newton-Raphson

1. Escolhemos um novo sample $x_{n}$ 
2. Calculamos o protótipo mais "próximo" $p^{*}$, definido como: $$\text{dist}(x_{n},p^{*})=\min_{k}\{\text{dist}(x,p_{k})\}$$
3. Atualizamos o step para a próxima iteração: $$p_{k}(t+1)\leftarrow p_{k}(t) + \alpha(t) h(t,p^{*},p_{k})(x_{n}-p_{k}(t))$$
4. Repetir os passos 1-3 enquanto ciclamos pelos $x_{n}$ pontos do dataset. Mais concretamente, percorremos todos os pontos do dataset. Após varrer todo o dataset repetimos, agora usando os protótipos atualizados ($t+1$). Podemos ver estes $t$ como *epochs*.

**Exemplo 1**
![[subspace treino.png]]
- Consideremos que temos uma estrutura de 1 dimensão (uma linha)
- Temos então "vizinhanças simples" - um vizinho da esquerda e um da direita
- Ou seja, transformamos um espaço 2D (como a trajetória de um braço articulado). Queremos mapear isto num espaço 1D. 
    - Por exemplo, uma forma de o fazer é usar a diferença $\phi_{2}-\phi_{1}$. 

![[subspace treino evo.png]]
no caso deste exemplo, consoante fazemos epochs, o mapa vai-se organizando de forma a passar pelos pontos de treino, como vemos acima.

**Exemplo 2**
![[subspace treino evo 2.png]]
- Neste exemplo temos uma rede 2x5 que começa com pesos *aleatórios*, daí a forma irregular. Esta é a projeção 2D de coordenadas 3D
- O "+" verde marca um ponto de treino novo. Quando um ponto é adicionado, primeiro vemos qual é o ponto do mapa mais próximo (Azul escuro - ponto vencedor). Esse ponto e os seus vizinhos (verde-azul) movem-se, de modo que a rede "estique" e passe pelo novo ponto de treino

**Exemplo 3**
![[conversao em espaço menor.png]]

#### Notas sobre SOM
- Como facilmente prevemos, a inicialização da rede influencia o treino e os resultados.
- **Fold-Back problem**
    - Por definição, em SOM estamos a colapsar dados n-D em dados 3D ou 2D. Este problema é mais falado no caso 2D
    - Ao colapsar os dados, podemos estar a gerar distorções ou auto-inserções, devido à natural perda de informação
    - Isto resulta no mapa dobrar-se sobre si mesmo
    - Exemplo do chatGPT: "Imagine um SOM treinado para mapear dados de cores RGB em um espaço 2D. Se houver uma forte concentração de pontos vermelhos em um canto e pontos azuis no outro, mas no meio há uma mistura de cores, o SOM pode "dobrar" partes do mapa para tentar ajustar esses padrões, criando regiões onde pontos vermelhos e azuis podem acabar próximos, mesmo que no espaço original eles estejam distantes."
    - Isto ocorre quando temos muitas mais dimensões dos inputs do que neurónios/pontos do mapa
    - Para resolver isto, temos que reiniciar o mapa e alterar parâmetros. Possívelmente aumentar o número de pontos do mapa
- **Principal component axis**
    - Se os pontos nvoos inseridos estiverem no eixo de maior crescimento dos valores, teremos uma melhor performance
- **Parâmetros de SOM**
    - Learning rate: $\alpha$. Deverá diminuir com o tempo, porque vamos aproximando dos valores corretos
    - Threshold de vizinhança: definir um raio máximo. Também diminui ao longo do tempo
    - Função de medir a distância
    - Número de protótipos e pontos
- Se a vizinhança for muito pequena, ela pode chegar a um ponto em que cada vizinhança só tem 1 ponto. Perdemos a ligação espacial entre os protótipos. O modelo converge para um mínimo local que corresponde a K-means.

### Principal Component Analysis (PCA)
- Acima vimos SOM como sendo um método que forma um mapa que mantém as caraterísticas de um conjunto de dados de alta dimensão. Ou seja, temos um mapa em que pontos mais próximos representam dados mais semelhantes
- Outra forma de ver SOM é pensar nos pontos do mapa como algo que aponta para a distribuição dos dados de treino. Ou seja, cada ponto corresponde a um sample desta distribuição (a distribuição está a ser discretizada). Onde temos mais pontos no mapa é onde teremos maior concentração de samples.

- Este método consiste em assumir que os dados ou a sua principal componente podem se contidos em 1 subespaço d-dimensional próximo. 
![[colapsar em plano.png]]
- Assim, os eixos deste subespaço são uma forma de representar os dados. O PCA consiste em *definir estes eixos*

**Como funciona - lógica**
![[projecao.png]]
- No caso acima, $(X^{1},X^{2})$ é o referencial original e $(Y^{1},Y^{2})$ é o novo referencial.
- Ora, $Y^{2}$ é perpendicular a $Y^{1}$. Assim, o objetivo do PCA é encontrar o $Y^{1}$ que minimiza o erro de aproximar $P_{i}\simeq P_{i}'$, ou seja: $\min\sum_{n}\overline{P_{n}P_{n}'}^{2}$
    - Notemos que numa regressão linear minimizamos os resíduos: $\min\sum_{n}\overline{P_{n}P_{n}''}^{2}$

- Do teorema de pitágoras, temos: $\overline{OP_{i}}^{2}=\overline{OP_{i}'}^{2}+\overline{P_{i}P_{i}'}^{2}$ 
    - Ou seja, minimizar $\sum_{i}\overline{P_{i}P_{i}'}^{2}$ é *o mesmo que* minimizar $\sum_{i}\overline{OP_{i}'}^{2}$
    - Se normalizarmos o set de dados, de modo que a média seja *zero*, então $\sum_{i}\overline{OP_{i}'}^{2}$ é a **variância** de $Y^{1}$.

**Como funciona - mais geral**
- Consideremos então uma VA $\mathbf{x}\in \mathbb{R}^{d}$ com matriz de covariância $C_{x}$
- O objetivo é arranjar um $\mathbf{y}$ (transformação de $\mathbf{x}$ noutro referencial) tal que $\mathbf{y}=\mathbf{w}^{T}\mathbf{x}$, em que $\|\mathbf{w}\|=1$
    - É ainda necessário que os componentes sejam não correlacionados
    - É ainda necessário que as variâncias estejam sempre a descer da primeira à última

- A solução deste problema é dada pelos valores próprios da matriz $C_{x}$.
    - Estes são definidos como $\lambda_{1},\dots,\lambda_{n}$ em que $\lambda_{1}\ge\lambda_{2}\ge\cdots\ge\lambda_{n}$
- A variância associada a uma variável $\mathbf{y}_{i}$ é dada pelo valor próprio $\lambda_{i}$.
- Consequentemente, a componente $\mathbf{y}_{j}$ compõe uma porção de $\tfrac{\lambda_{j}}{\sum_{i=1}^{n}\lambda_{i}}$ 
- Num espaço com $D$ dimensões, teremos $D$ valores de lambda. Mas, se **não** guardarmos todas as dimensões mas só as $q$ primeiras/principais, *só preservamos uma porção da variância*, dada por: $\tfrac{\sum_{i=1}^{q}\lambda_{i}}{\sum_{i=1}^{n}\lambda_{i}}$

**Exemplo**
- Temos dados que podem ser projetados no eixo $1$ com uma matriz $u_{1}$ tal que $u_{1}^{T}u_{1}=1$
- A variância dos dados projetados neste eixo será $\tfrac{1}{N}\sum_{n}\{u_{1}^{T}\mathbf{x}_{n} - u_{1}^{T}\overline{\mathbf{x}}\}^{2}=u_{1}^{T}Su_{1}$ em que definimos $$S=\frac{1}{N}\sum\limits_{n}(\mathbf{x}_{n}-\overline{\mathbf{x}})(\mathbf{x}_{n}-\overline{\mathbf{x}})^{T}$$
- Usando o método de multiplicadores de Lagrange, maximizamos este problema com $u_{1}^{T}Su_{1}+\lambda_{1}(1-u_{1}^{T}u_{1})$
- Isto dá-nos: $$Su_{1}=\lambda_{1}u_{1}$$
em que a variância é dada por $\lambda_{1}$
- Ou seja, teremos variância máxima quando $u_{1}$ é igual ao vetor próprio com o maior valor próprio

#### Curvas e Superfícies principais
- Uma curva principal é uma generalização do estudo de componente principal, em que arranjamos uma curva invés de um eixo retilíneo
- Mais concretamente arranjamos 1 curva 1D (num referencial curvo) em que aproximamos os dados
- Uma superfície principal é o mesmo, mas em 2D
- Poderíamos criar superfícies principais em dimensão 3+, mas isso não é usado porque o aspeto de visualização é perdido
![[curvas principais.png]]

### Escalamento multidimensional (MDS)
- Os métodos todos que vimos (SOM,PCA,curvas principais) mapeiam dados de alta dimensão D num manifold de dimensão d menor.
- Escalamento multidimensional faz algo semelhante:
    1. Começamos com observações $\mathbf{x}_{1},\mathbf{x}_{2},\dots,\mathbf{x}_{N}\in \mathbb{R}^{d}$
    2. MDS encontra valores $z_{1},z_{2},\dots,z_{N}\in\mathbb{R}^k$ com $k<d$, que têm as *mesmas distâncias entre pares*. Estes $z_{i}$ são achados ao minimizar isto: $$S_{D}(z_{1},z_{2},\dots,z_{N})=\sum\limits_{i\neq i'}(\|x_{i}-x_{i'}\|-\|z_{i}-z_{i'}\|)^{2}$$(ou seja, minimizamos a diferença entre a distância entre $x_{i},x_{i'}$ e entre os $z$ equivalentes)
- Isto, mais concretamente, é MDS de least-squares OU escalamento kruskal-shephard
- Notemos que este método funcionará se soubermos as distâncias entre os pares de pontos invés dos pontos em si
- O mínimo de $S_{D}$ é achado com descida de gradiente

**Sammon mapping**
- Versão de MDS, em que minizamos
$$S_{D}(z_{1},z_{2},\dots,z_{N})=\sum\limits_{i\neq i'}\frac{(\|x_{i}-x_{i'}\|-\|z_{i}-z_{i'}\|)^{2}}{\|x_{i}-x_{i'}\|}$$
aqui estamos a dar importância a pontos de dados $x_{i},x_{i'}$ que estejam próximos

**Produto interno centrado**
- Escalamento pretende manter as similaridades: $s_{ii'}$. Podemos defini-las como um produto interno centrado:
$$s_{ii'}=<x_{i}-\overline{x},x_{i'}-\overline{x}>$$
e minimizamos
$$\sum\limits_{i\neq i'}(s_{ii'}- <z_{i}-\overline{z}, z_{i'}-\overline{z}>)^{2}$$

### ISOMAP
- Mapeamento de atributos de forma isométrica
- Fazemos um graph de vizinhança
- Daí, calculamos as distâncias mais curtas
- Fazemos então um embedding d-dimensões

### Embedding Localmente Linear
- Calculamos os vizinhos de cada datapoint
- Calculamos os epsos que melhor reconstroem cada datapoint a partir dos seus vizinhos. 
- Calcular os vetor que melhor reconstruímos usando os pesos 

