## Pré-processamento de modelos 3D
### Fontes de incerteza
- Fontes de incerteza causam ruído nos dados. Isto cria orificios, picos e outros defeitos nos nossos pontos/meshes
- Por sua vez, isto afeta as features que detetamos e extraímos
![[Pasted image 20251011201226.png]]

- Existem imensas fontes de incerteza, que devemos ter sempre em conta ao adquirir e analisar dados:
![[Pasted image 20251011201300.png]]

### Filtragem
- Ora, como em princípio temos sempre *algum* ruído nos dados, um importante passo de pré-processamento é **filtragem de ruído**
- Este passo por vezes é acompanhado de downsampling

#### Baseada em intensidade 
- Filtramos conforme o valor de intensidade de um ponto medido
- Pontos com baixa intensidade indicam medições de range fracas e de pouca confiança. 
    - Por exemplo, se usarmos um sistema LiDAR teremos pontos de baixa intensidade em reflexões em materiais transparentes/translúcidos. Nestes casos a distância medida terá um erro maior que esperado
- Podemos definir o threshold de intensidade mínima que aceitamos através de um histograma. Podemos simplesmente remover pontos abaixo desse threshold 
- Este threshold irá ser influenciado pela eletrónica e funcionamento do sensor usado
- Além de materiais transparentes, baixa intensidade permite detetar e filtrar: fumo, pó, nevoeiro, vapor, etc

#### Baseada em range
- Temos um objeto em 3D. Quando usamos um sensor (como um sensor laser), ele na cria uma imagem 2D em que cada pixel indica a **profundidade** desse ponto do objeto
    - Temos ruído em superfícies refletivas ou transparentes
    - Temos descontinuidades nos pontos em bordas
- Assim, escolhemos um ponto e analisamos o seu plano de vizinhos. Ao calcular o **desvio padrão** podemos fazer filtragem
    - Em zonas com desvio padrão baixo teremos uma zona mais suave do modelo 3D (está tudo "mais junto")
    - Quando o desvio padrão for muito elevado, teremos  algo mais irregular e possivelmente com ruído

#### Baseado em planaridade local
- Normalmente, temos dados de maior confiança quando temos estruturas mais planares 
- Para estudar isto usamos a **matriz de covariância 3D** (AKA tensor da estrutura 3D), calculada com todos os pontos de uma vizinhança 
- Escolhemos então os valores próprios $\lambda_{1}\ge \lambda_{2}\ge\lambda_{3}\ge0$ (normalmente escolhemos os 3 maiores valores próprios). Com eles, definimos linearidade (L), planaridade (P) e espalhamento/scattering (S):
$$L = \frac{\lambda_{1}-\lambda_{2}}{\lambda_{1}}~~,~~P=\frac{\lambda_{2}-\lambda_{3}}{\lambda_{1}}~~,~~ S=\frac{\lambda_{3}}{\lambda_{1}}$$

## Features 3D
- Temos 2 tipos de features, conforme o seu contexto no modelo:
    - **Local features** - determinados conforme a zona de vizinhança de um certo ponto no objeto 3D
    - **Global features** - caraterizam a geometria, topologia do objeto 3D como um todo (altura, largura, etc)

### Features locais
- Estas features recolhem então informação sobre a forma e outras propriedades de uma região do objeto, *em torno de um Keypoint*
- Estas features são mais robustas que as globais: resistem a
    - Oclusão (coisas a tapar o objeto)
    - Clutter (quando temos muita coisa em torno do objeto)
- Permitem então associar pedaços de objetos

### Keypoints
- Vejamos 2 conceitos importantes:
    - **Deteção de keypoint** - pontos de interesse que nos permitem caraterizar o objeto de forma eficiente
    - **Descrição de keypoint / Descriptor** - vetor de informação retirada em torno dos keypoints e que permite identificá-los

#### Desafios
- Alguns fatores que dificultam a extração de features locais
    - **Resolução** - se tivermos dados com muita resolução teremos dados geométricos melhores mas um maior preço computacional
    - **Ruído** nos dados ou dados em falta
    - **Pose** - A posição do objeto e a posição do sensor que recolheu os dados podem variar, mas o objeto é sempre o mesmo e as features têm que refletir isso
    - **Clutter** - se nos nossos dados tivermos vários objetos, iremos ter que separar o objeto em estudo daquilo que não nos interessa
    - **Deformação** - um objeto não rigido pode deformar-se durante a captação de pontos (EX: balão a esvaziar lentamente) e os dados ficam inconsistentes
- Ou seja, é importante termos *repetibilidade, precisão, quantidade* (de pontos) *e unicidade/capaidade de distinguir*. Precisamos também de definir critérios!

#### Detetar keypoints
- Temos 2 métodos principais:
    - **Deteção de keypoints de escala-fixa** 
        - Procuramos keypoints usando vizinhanças de tamanho predefinido de acordo com a escala do objeto
        - A cada ponto da vizinhança atribuímos uma pontuação de distinctiveness. O ponto "mais distinto" é o keypoint
    - **Deteção de keypoints de escala-adaptativa**
        - Construímos um espaço de escala: pegamos no objeto e replicamos com diferentes níveis de suavização. Consoante a suavização aumenta, perdemos os detalhes e ficamos apenas com os elementos fundamentais e maiores - mudamos a escala do objeto artificialmente: se tivermos algo muito suavizado será o mesmo que termos algo muito reduzido
        - Assim, os keypoints são pontos que são os mais distintos da sua vizinhança e que são relevantes a várias escalas (de forma que não sejam relevantes só em escalas reduzidas ou grandes)
        - Isto resulta em keypoints que mantêm a sua relevância **independentemente da escala**. Um algoritmo popular que faz isto é SIFT

- Normalmente usamos pontos de alta curvatura, porque consideramos como sendo mais ricos em informação sobre a forma do objeto:
![[Pasted image 20251012161213.png]]

#### Fixed Scale: Métodos de curvatura
- Como referido acima, pontos de altura curvatura costumam ser associados a altos níveis de informação sobre o objeto. Assim, vejamos como podemos usar esta propriedade para estudar objetos
- Consideremos que temos um ponto $P$ num modelo. Podemos definir o seu vetor normal $\mathbf{n}(P)$ e um vetor tangente $\mathbf{v}(P)$. 
- Com estes 2 vetores podemos definir o **plano normal** e a **curva normal**
    - O plano normal é aquele que contém $\mathbf{n}$ e $\mathbf{v}$
    - A curva normal é a interseção do plano normal com a superfície do objeto
![[Pasted image 20251012162945.png]]
- Assim, podemos definir a **curvatura normal** $\kappa_{n}(\mathbf{v})$ que nos dá uma medida do desvio entre o vetor tangente $\mathbf{v}$ e a curva normal. Por outras palavras, mede o quanto a superfície curva 
- Tal como temos infinitos vetores tangentes $\mathbf{v}$, também temos infinitas curvas normais, ambos obtidos ao rodar $\mathbf{v}$ em torno de $\mathbf{n}$

**Como calcular**
![[Pasted image 20251012164053.png]]
- Ora, a curvatura consiste em "quanto varia o ângulo ao longo desta superfície" ou seja: $\kappa=\frac{d\theta}{ds}$ 
- Assim, tendo em conta um ponto $p_{2}$ em que o ângulo entre a superfície e o vetor tangente é $\delta$, podemos definir a curvatura:
$$\begin{align*}
\kappa(p_{2})=\frac{d\theta}{ds}&\approx \frac{\Delta \theta}{\Delta s}\\
&= \frac{\delta}{\text{distância média entre pontos}}\\
&= \frac{\delta}{(s_{1}+s_{2})/2}
\end{align*}$$

**Direções de curvatura**
- Ao rodar $\mathbf{v}$ em torno de $\mathbf{n}$, iremos obter valores de curvatura diferentes
- Ora, teremos duas *curvaturas principais*: uma curvatura mínima $\kappa_{1}$ e uma curvatura máxima $\kappa_{2}$. Associadas a estas, temos duas direções **ortogonais** $e_{1},e_{2}$
    - A razão porque estes dois vetores são ortogonais é demonstrável e acontece sempre! Usamos o operador de forma (que aparece mais abaixo) para provar isto 

- Ou seja, podemos definir o vetor tangente em função destas direções: $\mathbf{v}(P)=u_{t}\mathbf{e}_{1}+v_{t}\mathbf{e}_{2}$
- Segundo o teorema de curvatura de Euler, temos
$$\kappa(\theta)=\kappa_{1}\cos^{2}\theta+\kappa_{2}\sin^{2}\theta$$
em que $\theta$ é o ângulo entre $\mathbf{v}$ e $\mathbf{e}_{1}$.

**Tipos de curvatura**
- Podemos definir 2 tipos de curvatura, que nos permitem resumir a curvarura numa vizinhança com 1 só valor:
    - **Curvatura média** $$H = \frac{\kappa_{1}+\kappa_{2}}{2}$$
    - **Curvatura gaussiana** $$G=\kappa_{1}\kappa_{2}$$
- Estas 2 curvaturas são invariantes com *translação e rotação*, mas **não invariantes de escala**
    - Isto faz sentido: ao aumentar a escala de um ponto numa zona curva, a curvatura vai diminuir. Ao aproximar-nos muito de uma esfera passamos a ver algo quase plano.

- Curvatura gaussiana é menos intuitiva, mas permite categorizar superfícies como:
    - Elipticas ou esféricas: $G>0$
    - Hiperbólicas: $G<0$
    - Parabólicas ou planas: $G=0$
- De uma forma geral temos (esta figura usa $K$ para representar $G$):
![[Pasted image 20251012170119.png]]

- Ao aplicar os 2 tipos de curvatura ao modelo de um coelho temos (curvatura média na direita e curvatura gaussiana na direita):
![[Pasted image 20251012170154.png]]

**Operador de forma**
- Definimos como
$$S(\mathbf{v})=\frac{d\mathbf{n}}{d\mathbf{v}}$$
e consiste na curvatura em $P$ na direção de $\mathbf{v}$
- E temos que:
    - Os valores próprios de $S$ são as curvaturas principais $\kappa_{1},\kappa_{2}$
    - O determinante de $S$ é a curvatura gaussiana $G$
    - O traço/trace (soma dos elementos da diagonal principal) de $S$ é o dobro da curvatura média $H$
    - Os vetores próprios são $\mathbf{e}_{1},\mathbf{e}_{2}$ e ortogonais
        - Isto acontece porque o operador é simétrico: $\langle S\mathbf{u},\mathbf{v}\rangle=\langle\mathbf{u},S\mathbf{u}\rangle$
        - Como consequência disso temos 2 valores próprios reais e 2 vetores próprios correspondentes que são ortogonais: $$\begin{cases}S\mathbf{e}_{1}=\kappa_{1}\mathbf{e}_{1} \\ S\mathbf{e}_{2}=\kappa_{2}\mathbf{e}_{2}\end{cases}$$

#### Fixed Scale: LSP
- AKA **Local surface patch**
- Este método define o **indice de forma**:
$$s=\frac{2}{\pi}\arctan\left(\frac{\kappa_{2}+\kappa_{1}}{\kappa_{2}-\kappa_{1}}\right)$$
- Numa vizinhança, um certo ponto $i$ é *keypoint* se tiver um indice de forma **máximo ou mínimo**:
$$\begin{align*}
s_{I}=\max_{i=1,\dots,n}s(P_{i}) \quad;\quad s_{I}\ge(1+\alpha)\mu\\
s_{I}=\min_{i=1,\dots,n}s(P_{i}) \quad;\quad s_{I}\le(1-\beta)\mu
\end{align*}$$
em que $\mu$ é o indice médio da vizinhança e $\alpha,\beta$ são parametros que controlam a deteção de keypoints.

#### Fixed Scale: Variação de superfície
- Os 2 métodos que vimos acima (curvatura e index de forma) são **invariantes com translação e rotação**
- Mas existe algo que é **invariante com translação e escala**: *ângulos* entre o vetor normal da superfície e o referencial usado.
- Neste método definimos a *matriz de covariância* dos pontos da vizinhança. Por definição, esta matriz representa a **variação** dos pontos.
- Mais concretamente, os seus valores próprios $\lambda_{1},\lambda_{2},\lambda_{3}$ (estes são os 3 menores valores próoprios) permitem tirar conclusões sobre os keypoints 

**ISS (Intrinsic Shape Signatures)**
- Detetamos keypoints usando os 3 maiores valores próprios $\lambda_{1},\lambda_{2},\lambda_{3}$ ($\lambda_{1}$ é o maior) e temos $$\frac{\lambda_{2}}{\lambda_{1}}<\rho_{12} \quad;\quad \frac{\lambda_{3}}{\lambda_{2}}<\rho_{23}$$
(no powerpoint diz que $\lambda_{1}$ é o menor valor próprio mas acho que é erro. A documentação do open3d indica que ele é o maior)
- Ou seja, calculamos estes rácios e consideramos keypoints os pontos em que os rácios estão abaixo de $\rho_{12},\rho_{23}$, em que estes são thresholds.

**3D Harris**
- Estamos a estudar se um ponto $P$ será keypoint. Da sua vizinhança subtraímos as coordenadas do **centroide** para passar os vizinhos para um referencial centrado no centroide.
- Depois garantimos que o vetor normal em $P$ está alinhado com o eixo dos zz. Isto vai facilitar o passo seguinte
- Os pontos são depois ajustados a uma superfície quádrica: $z=ax^{2}+by^{2}+cxy+dx+ey+f$
- Definimos uma matriz de simetria ($E$) usando os coeficientes $a,b,c,d,e,f$ da função quádrica
- Temos então a resposta de Harris 3D:
$$h(P)=\det(E) - \alpha \cdot \text{tr}(E)^{2}$$
(em que $\text{tr}$ é o traço)
- E temos:
    - $h\sim0$ se estivermos numa zona plana: variação baixa em todas as direções
    - $h$ reduzido ou intermédio se estivermos numa borda: variação alta numa direção
    - $h$ elevado se estivermos num canto ou ponto de alta curvatura: variação elevada em todas as direções

#### Adaptive Scale 
- Nestes casos fazemos filtragem/suavização do objeto 3D para simular diferentes escalas

**Salient Points**
- Similar a SIFT

**Variação de superfície multi-escala**
- Partindo do ponto $P$, determinamos a matriz de covariância da vizinhança de raio $\delta$. Vamos variando o raio da vizinhança para simular diferentes escalas
- Temos a variância:
$$\sigma(P,\delta)=\frac{\lambda_{1}}{\lambda_{1}+\lambda_{2}+\lambda_{3}}$$
- Repetimos isto para vários $P$
- Os keypoints serão os pontos com variância máxima ao longo do eixo de $\delta$ 's

#### Aparte: Vetor normal e tangente
- O vetor normal $\mathbf{n}(P)$ pode ser calculado num ponto $P$ ao conhecer os seu vizinhos
- Podemos definir um vetor $\mathbf{v}=u_{t}f_{u}+v_{t}f_{v}$ como vetor tangente (mas noetemos que existem infinitos vetores tangetes em qualquer ponto)
![[Pasted image 20251012161530.png]]

- Os vetores tangentes que definiem $\mathbf{v}$ podem ser definidos como derivadas:
$$f_{u}(u,v)=\frac{\partial f(u,v)}{\partial u} \quad;\quad f_{v}(u,v)=\frac{\partial f(u,v)}{\partial }$$
e temos o vetor normal unitário:
$$\mathbf{n}(u,v)=\frac{f_{u}(u,v)\times f_{v}(u,v)}{\|f_{u}(u,v)\times f_{v}(u,v)\|}$$

- Claro, num computador fazemos as derivadas usando diferenças finitas:
$$\begin{align*}
z_{x}&= \frac{\partial z(x,y)}{\partial x}=\frac{z(x+1,y)-z(x,y)}{\sigma_{x}}\\
z_{y}&= \frac{\partial(x,y)}{\partial y}=\frac{z(x,y+1)-z(x,y)}{\sigma_{y}}
\end{align*}$$
em que $z(x,y)$ é a função que descreve a superfície do objeto ao mover em $x,y$. $\sigma_{x},\sigma_{y}$ são os espaçamentos $x,y$ - estes serão variáveis num modelo 3D e são calculados entre  $(x+1,y)$ e $(x,y)$.

- Claro, como alternativas a esta discretização de diferença para a frente, temos diferença para trás e diferenças centrais. 
- Todas estas técnicas de diferenças finitas são muito sujeitas a ruído e devemos suavizar os dados
- Tendo as derivadas $z_{x},z_{y}$ podemos definir o vetor normal:
$$\mathbf{n}(P)=\frac{\begin{pmatrix}-z_{x} & -z_{y} & 1\end{pmatrix}^{T}}{\sqrt{z_{x}^{2}+z_{y}^{2}+1}}$$

##### Fit de superfícies
**Plano**
- Outra maneira de determinar o vetor normal é fitar um plano ao ponto $P$ e seus vizinhos. O vetor normal ao plano é o vetor normal em $P$
- Claro, ao fazer isto estamos a assumir uma planaridade decente na vizinhança de $P$

**Superfície quádrica**
- Isto é o equivalente a uma parábola em 3D e definimos como:
$$Ax^{2}+By^{2}+Cz^{2}+D+Exy+Fxz+Gx+Hyz+Jy+Kz=0$$
que nos dá
$$z_{x}=-\frac{2Ax+Ey+Fz+G}{2Cz+Fz+Hy+K} \quad;\quad z_{y}=-\frac{2By+Ex+Hz+J}{2Cz+Fz+Hy+K}$$

## Descriptors
- Um descriptor de features locais tem o objetivo de capturar informação geométrica distinta e única dessa região da superfície
    - Na prática, usamos um vetor com valores numéricos
- Veremos 3 approaches:
    - **Signature** - Usamos atributos/caraterísitcas de sample points à volta de um keypoint
    - **Histograma** - Fazemos histogramas de medições geométricas à volta de um keypoint
    - **Covariância** - Permite combinar atributos heterogéneos/de dimensões diferentes
- Claro, este passo é feito depois de determinar os keypoints, obtendo-se a informação dos descriptors em torno dos keypoints

### Signature : método splash
0. Queremos definir um descriptor num keypoint $P$
1. Geramos um círculo/esfera com raio $r$ em torno de $P$
2. Definimos um conjunto de pontos $p_{\theta}$ na intercepção da esfera com a superfície do objeto, em intervalos angulares regulares $\Delta\theta$
3. Definimos um LRF (local reference frame) usando o vetor normal em $P$ ($\mathbf{n}$) e o plano tangente em $P$
![[Pasted image 20251012234618.png]]
- Algumas informações que podemos extrair com este método e guardar no descriptor:
    - curvatura
    - ângulos de torsão 
    - distâncias verticais entre o plano tangente e os pontos $p_\theta$
    - etc

### Histograma de distribuições espaciais
0. Definimos um LRF no keypoint. Isto permite ter invariância de rotação e translação
1. Dividimos a região em torno do keypoint em várias partes. Cada uma corresponde a um "contentor"
2. Em cada contentor guardamos o número de ocorrências de alguns atributos da superfície

**Referencial**
- Podemos definir um referencial centrado no keypoint $P$ - chamamos a estes referenciais de *object centered*
- Tendo o ponto $P$ e o seu vetor normal $\mathbf{n}$, podemos definir 2 coordenadas cilíndricas: distância radial $\alpha$ e distância na direção normal $\beta$ 
- Temos então:
![[Pasted image 20251013001140.png]]

**Funcionamento**
- Para um certo vizinho $Q$, determinamos as coordenadas cilíndricas $(\alpha,\beta)$:
$$\beta=(Q-P)\cdot \mathbf{n} \quad;\quad \alpha=\sqrt{\|Q-P\|^{2}-\beta^{2}}$$
- Fazendo isto para todos os pontos vizinhos, podemos fazer um histograma 2D, em que temos as quantidade de pontos em bins de $\alpha,\beta$ (basicamente um heatmap)
- A estes heatmaps/imagens chamamos de **spin images** - este nome vem do facto que estas imagens são invariante em translação e rotação. São ainda robustas a clutter e oclusão

### Histograma de atributos geométricos (PFH)
- PFH = Point Feature Histogram

1. Selecionamos os KNN do keypoint $P$ (temos uma esfera de raio $r$)
2. Conhecendo o vetor normal em cada ponto, podemos:
    1. Comparar pares de pontos vizinhos $q_{i},q_{j}$ e comparamos os seus vetores normais $\mathbf{n}_{i},\mathbf{n}_{j}$
    2. Entre $q_{i},q_{j}$ escolhemos $q_{s}$ como o ponto que tem o vetor normal mais paralelo à linha que une $q_{i},q_{j}$. O outro ponto é referido como $q_{t}$
    3. Podemos definir um referencial de Darboux: $$\begin{align*}\mathbf{u}&= \mathbf{n}_{s}\\\mathbf{v}&= (q_{t}-q_{s})\times \mathbf{u}\\\mathbf{w}&= \mathbf{u}\times\mathbf{v}\end{align*}$$
    4. Tendo estes vetores, podemos definir 4 features:$$\begin{align*}f_{1}&= \mathbf{v}\cdot\mathbf{n}_{t}\\f_{2}&= \|q_{t}-q_{s}\|\\f_{3}&= \mathbf{u} \cdot\frac{(q_{t}-q_{s})}{\|q_{t}-q_{s}\|}\\f_{4}&= \arctan\left(\frac{\mathbf{w}\cdot\mathbf{n}_{t}}{\mathbf{u}\cdot\mathbf{n}_{t}}\right)\end{align*}$$
    5. O descriptor PFH consiste em dividir cada uma destas 4 features em $N$ bins. Depois juntamos tudo num histograma 4D com $N^{4}$ pontos

### Métodos de covariância
- Calculamos vários tipos de atributos (numéricos) e juntá-mo-los num vetor $x_{i}=(a,b,\dots)\in \mathbb{R}^{d}$ para cada ponto $P_{i}$. 
- Definimos:
$$R=\frac{1}{n-1}\sum\limits_{i=1}^{N}(x_{i}-\mu)\cdot(x_{i}-\mu)^{T}$$
em que $\mu$ é a média dos atributos todos, de todos os pontos
- Exemplos de atributos:
    - Canais RGB
    - Módulo do gradiente
    - Coordenadas de cada ponto relativamente ao centro do LRF
    - Distância entre vizinhos
    - Combinações de fatores
    - etc
