## Nuvem de Pontos 
- Podemos definir:
    - **Ponto** - localização no espaço $p\in \mathbb{R}^{D}$. Se $D=2$ estamos em 2D, $D=3$ estamos em 3D, etc. Podemos ter mais dimensões, para incluir atributos como intensidade de sinal, cor, orientação, etc
    - **Nuvem de pontos** - coleção de pontos de um certo espaço. 

### Aquisição de pontos
- Como vimos atrás, existem sensores ativos e passivos.
![[tipos de metodos de aquisicao.png]]

#### Passivos
- Estes tipos de sistemas são usados em SLAM visual e estimação de posição de robots
- Este tipo de técnicas utilizam dados apresentados em imagens 2D (fotografias)
- Dois tipos comuns:
    - *Técnicas de stereo matching* - estimamos a estrutura 3D utilizando dois sets de dados 2D, associando pontos correspondentes (sabemos que o ponto X na imagem 1 representa o mesmo ponto do objeto que o ponto Y na imagem 2)
    - *Structure-from-Motion (SfM)* - obtemos muitos pontos. Com isso determinamos a estrutura 3D do objeto e a posição da câmara

- Neste tipo de técnicas temos:
    - calibração offline
    - retificação de imagem online
    - stereo matching online
    - triangulação online

![[aquisicao passiva 2 cams.png]]
- Em *stereo matching*, conhecemos o espaçamento entre as câmaras/sensores. Assim, associamos pares de pontos correspondentes aos mesmos pontos do objeto. 
- Conforme a *disparity / afastamento* de 2 pontos associados, atribuimos uma intensidade grayscale. Assim, podemos obter uma imagem que mostra a profundidade do objeto:
![[mapa profundidade passiva.png]]

**Problemas**
- Um fator que afeta muito a qualidade deste método é a **textura** do objeto. Se tivermos regiões sem qualquer textura, não temos como associar pontos e não conseguimos estimar a estrutura 3D de forma adequada. 
- Outro fator importante e causado por utilizarmos câmaras é a **iluminação**. Se tivermos num ambiente muito escuro, as imagens serão piores e a estrutura 3D será estimada pior

#### Ativos
- Envolve manipulação da cena observada
- Para fazer isso, normalmente observamos a cena/objeto com uma câmara/sensor *enquanto* emitimos um sinal com um projetor/laser. A forma como o feixe/ponto laser interage com o objeto permite estimar a sua estrutura 3D
- Este método chama-se **structured light**:
![[metodo ativo aquisicao.png]]
(O projetor e a câmara podem estar num mesmo dispositivo unidos por um braço)

- Estes métodos conseguem determinar a estrutura e geometria do objeto com precisão, através dos defietos no padrão laser
- Notemos que estamos sujeitos à luz ambiente no meio e não podemso scannar objetos refletivos ou transparentes

- Algumas approaches:
    - **temporal coded** - projetar uma série de padrões binários (preto e branco). A sua evolução permite tirar informação sobre o objeto
    - **spatial coded** - usamos um padrão muito específico e que varia ao longo do objeto
    - **direct coded** - o padrão emitido apresenta um código/sequencia binária específica, que podemos associar a cada pixel na imagem captada na câmara. Facilita a reconstrução 3D
    - **time of flight (ToF) ou medição de fase** - analisamos melhor o sinal que é refletido do objeto para o sensor

##### Temporal coded
- Queremos determinar as coordenadas de um ponto $P=(X,Y,Z)$ num objeto. Conhecemos as coordendas de um laser $(x_{L},y_{L},z_{L})$. Representamos uma câmara como um plano focal (a azul), em que o ponto $P$ é projetado, tendo as coordenadas $(x,y)$ nele.
![[temporal coded figura|654]]
- Temos que:
$$x=f \frac{X}{Z} \quad;\quad y=f \frac{Y}{Z}$$
podemos entender isto com uma semelhança de triângulos. Um da origem até $P$ e outro da origem até $(x,y)$: $$\frac{x}{f}=\frac{X}{Z} \quad;\quad \frac{y}{f}=\frac{Y}{Z}$$
isto quer dizer que, se tivermos $Z$ menor (câmara mais perto de $P$, sem alterar a sua orientação Z) veremos que $x,y$ aumentam - o ponto vai mais para longe do centro do plano.

- Nós conhecemos $(x,y)$ - são as coordenadas que medimos na imagem da câmara: o "plano focal" acaba por ser **a fotografia que tiramos**
- Conseguimos definir:
$$X=\frac{fx}{Z} \quad;\quad Y=\frac{fy}{Z}$$
ou seja, se descobrirmos $Z$ temos todas as coordenadas de $P$ !!!

**Reta laser-P**
- Podemos definir um reta entre $(x_{L},y_{L},z_{L})$ e $P$. Usemos a equação paramétrica:
$$\begin{cases}
X=x_{L}+at \\
Y=y_{L}+bt \\
Z=z_{L}+ct
\end{cases} ~~,~~ t\in[0,1]$$
e podemos escrever
$$\frac{X-x_{L}}{a} = \frac{Y-y_{L}}{b} = \frac{Z-z_{L}}{c}$$
e substituímos
$$\frac{Z \frac{x}{f}-x_{L}}{a} = \frac{Z \frac{y}{f}-y_{L}}{b} = \frac{Z-z_{L}}{c}$$
e daqui podemos usar $x,y,f$ para determinar $a,b,c,Z$

##### Temporal coded v2
- Outra opção é ter vários lasers. Consideremos que temos 7 lasers. O objetivo é fazer os cálculos como acima, determinando as coordenadas de vários pontos do objeto, para acelerar o processo de scanning.
![[temporal coded figura v2|554]]
- Mas notemos que na foto não tesmo como saber que linha veio de que laser, então não podemos fazer contas porque não sabemos as coordenadas do laser que originou o ponto $B_{i}$
- Para resolver isto, acendemos e desligamos os lasers de forma coordenada. Assim, este é que é o verdadeiro *temporal coded*. Podemos ligar os lasers de forma a fazer codigo binario:

| Instante (t) | Laser L₁ | Laser L₂ | Laser L₃ |
| ------------ | -------- | -------- | -------- |
| t₁           | 1        | 0        | 0        |
| t₂           | 0        | 1        | 0        |
| t₃           | 0        | 0        | 1        |
| t₄           | 1        | 0        | 1        |
| t₅           | 0        | 1        | 1        |

- Imaginemos que ao fazer esta variação vemos algo tipo: 100,001,010,110,011. Ao comprar os 2 padrões, podemos ver que a primeira risca é L1, a segunda é L3 e a terceira é L2

### Representação
- Como vimos, uma **nuvem de pontos** é uma coleção $P=\{p_{1},\dots,p_{n}\}$ de pontos $p_{i}\in \mathbb{R}^{3}$. Isto é feito com um array $n\times3$
- O que não referimos é que esta sequência **não tem estrutura**, ou seja, **está DESORDENADA**. Isto significa que o ponto $i$ e o ponto $i+1$ podem estar em zonas opostas da nuvem.
- A nuvem não ter estrutura implica ainda que não temos informação sobre *conexão de vertices* (NOTA: 'vertex' é 'vértice' em inglês). Por outras palavras, nada nos dados da nuvem de pontos nos diz como montar a estrutura 3D.

#### Nuvem de pontos estruturada
- Os pontos são ligados através de uma estrutura consistente. Para isso ligamos vértices (os pontos de dados passam a ser vértices ao ligá-los) adjacentes. Notemos ainda que nestas nuvens, vértices adjacentes têm indices adjacentes.
- Consideremos vértices $p(i,j)\in\mathbb{R}^{3}$ num array $m\times n\times3$. 
    - Podemos defini-los como tuplos do tipo $(x(i,j), y(i,j), z(i,j))$ em que $i\in(1,\dots,m)~,~ j\in(1,\dots,n)$
    - O $3$ na dimensão do array indica as 3 dimensões xyz
    - Podemos ainda usar um array binário 2D $m\times n$ para indicar se um certo ponto $m,n$ existe ou não
- Neste tipo de nuvens podemos ligar os pontos de várias formas, mas uma muito frequente consiste em 4 ligações a vizinhos e 2 ligações diagonais:
![[ligacao de pontos para fazer mesh.png|425]]
(em cada ponto, temos 4 ligações vermelhas e 2 ligações diagonais como vemos a azul)

#### Mapa de profundidade e Imagem de Range
- Estes são 2 casos em que usamos uma nuvem estruturada de pontos para representar um objeto 3D no espaço 2D. Usamos uma grid $(i,j)$
- Normalmente observamos os pontos como imagens a preto e branco, podendo observar a profundidade:
![[mapa de range e profundidade.png]]

- Para fazer estas imagens, atribuimos uma intensidade diferente a cada ponto (mais próximo = mais branco). Mas existe aqui uma diferença entre estas 2 representações:
    - **Imagem de range** - Cada ponto tem a sua cor controlada pela *distância radial* do ponto ao sensor que o mediu. Comum em sistemas LiDAR ou TOF
    - **Mapa de profundidade** - Cada ponto tem uma cor relacionada com a sua *distância ortogonal ao plano de visão* do sensor. Normalmente isto é a distância ao longo do eixo Z do referencial da câmara/sensor
- Este tipo de representação pode ser analisada ou criada por redes neuronais de convolução (CNNs).

#### Representação com mesh de superfície
- Temos, no espaço 3D, os vértices ligados com triângulos
- A mesh pode ser fechada ou aberta (cria ou não um volume fechado)
- Não é obrigatório usar triângulos em meshes, mas essa é a escolha mais comum de longe
![[mesh bunny.png]]
- Notemos que o tamanho (e concentração) de triângulos indica a quantidade de pontos que temos numa certa região

#### Voxels
- Equivalente a Pixeis em 3D
- Temos uma rede 3D de voxels. Para cada um temos um booleano que nos diz se existe algo ou não
![[voxel bunny.png]]

**Propriedades**
- A precisão da representação é decidida pelo tamanho de 1 voxel
- O número de voxels aumenta *cubicamente* com a precisão
- Este tipo de representação é muito bom para fazer cálculos de volume e coisas relacionadas
- Representações de voxels são armazenadas no PC como arrays 3D. Portanto, podem ser usadas por CNNs

##### Octree
- Versão optimizada de representação de voxels
- Baseia-se num sistema de árvore, em que cada nodo tem 8 filhos. Vamos subdividindo o espaço de acordo com a complexidade da estrutura. Temos então uma resolução adaptativa
![[octree.png]]

**O algoritmo**
1. Voxels completamente preenchidos ou vazios não são divididos
2. Voxels parcialmente ocupados são divididos
3. Subdividir um voxel resulta em 8 novos voxels menores
4. Voltar ao passo 1. Repetimos isto atéq« que todos os voxels estejam completamente preenchidos OU até que se atinja um certo tamanho mínimo predefinido.
![[octree evolucao.png]]

##### K-D Trees
- Representação em que vamos subdividindo o espaço ao longo de planos perpendiculares aos eixos.
![[kd tree mapa.png]]
- Por exemplo, neste exemplo em 2D temos o plano $x=8$ a dividir o espaço a meio
    - Notemos que este plano é perpendicular ao eixo dos XX

**Utilidade**
- Esta técnica permite acelerar a procura de pontos num espaço a várias dimensões. 
- Como dividimos o espaço aproximadamente "a meio", conseguimos encontrar um certo ponto muito eficientemente. Podemos pensar em binary search, como um análogo conhecido
- Como veremos abaixo no exemplo, guardamos esta informação numa árvore binária, em que cada nodo representa uma divisão do plano

**Algoritmo**
1. Organizamos os pontos segundo o eixo dos XX
2. Escolhemos a mediana desse conjunto. Se nele tivermos $x=a$, então usamos esse plano para dividir o espaço em 2 partições: $x<a$ e $x>a$. O ponto mediana NÃO fica em nenhuma das partições.
3. Para cada uma destas partições, organizamos os pontos segundo o eixo dos YY
4. Escolhemos a mediana desse conjunto e dividimos a partição conforme $y=b$
5. Repetir até todos os pontos marcarem uma divisão

**NOTA**: quanto temos um número par de pontos dentro de uma partição, podemos escolher o ponto à direita ou à esquerda do centro como "mediana". No entanto, temos que ser consistentes e escolher sempre o mesmo lado em toda a árvore!!!

**EXEMPLO**
- Vejamos uma resolução à mão a mostrar como obtemos a divisão KD-tree mostrada no gráfico acima
![[kd tree resolucao.png|500]]
![[kd tree resolucao 2.png|500]]

##### Vizinho mais próximo
- Podemos usar uma KD tree para procurar o vizinho mais próximo de um certo ponto $R$.
- Fazemos isto usando binary search:
    - Primeiro descemos pela árvore, seguindo o ponto $R$. Se $R=(10,2)$ virámos para o ramos que nos diz $x>5$ e por aí fora.
    - Quando chegamos a uma *folha* (ponta solta sem filhos), esse ponto é a nossa melhor estimativa de vizinho mais próximo. Chamemos a esse ponto $P_{best}$
    - Finalmente, fazemos um processo de backtracking. 
        - Partimos de $P_{best}$ e subimos para o nodo acima dele. Comparamos a distância entre $R$ e $P_{best}$ com a distância entre $R$ e o plano de divisão desse nodo
        - Se a distância R-Plano for *menor* que R-Pbest, exploramos o ramo oposto a $P_{best}$
        - Repetimos isto sempre à procura da menor distância para $R$

- Esta técnica tem complexidade $O(\log n)$ se a árvore for equilibrada.
    - Isto é bom, quer dizer que o tempo que demoramos a encontrar o vizinho mais próximo aumenta com $\log n$ consoante aumentamos o número de elementos na árvore ($n$)

- Podemos aplicar esta técnica para fazer **range searching** - encontrar todos os vértices dentro de um range de distância euclideana.