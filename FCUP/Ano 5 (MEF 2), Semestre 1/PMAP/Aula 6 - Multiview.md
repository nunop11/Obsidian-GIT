- Humanos têm 2 olhos. Usando-os, temos visão **estereoscopica**. Isso quer dizer que usamos a informação que cada olho obtem para estimar a profundidade.
    - Mais concretamente, temos os dois olhos distanceados na horizontal. Isso quer dizer que cada um vê uma imagem ligeiramente diferente do mundo 3D à sua frente
    - Assim, relacionando objetos (ver onde está o objeto X na imagem do olho esquerdo e do direito) o cérebro consegue saber as disparidades entre os olhos e com isto ter uma noção de **profundidade**
- Também com câmaras digitais temos isto: com uma câmara não sabemos a profundidade, mas com 2 podemos calcular profundidade!

# Visão estereo
## Assumption
- Consideremos a **assumption de estereo paralelo frontal**: 
    - Assumimos que as 2 câmaras estão a olhar em paralelo. 
    - As imagens que as câmaras captam são não distorcidas, coplanares e *row-aligned* - os pixeis da imagem estão organizados em linhas que são **horizontais** em ambas as imagens e **alinhadas** com o objeto real
        - Para um ponto P do objeto 3D, as suas coordenadas nas imagens das câmaras apenas terão diferenças no eixo horizontal - No eixo vertical está tudo alinhado

![[visao stereo|600]]
(Consideremos que aqui os eixos são paralelos: $z_{L}\parallel z_{R}$)
- Temos então as câmaras nos pontos $C_L,C_R$, com eixos paralelos. Assim, os seus planos de imagem são **coplanares** (em cima não mas ignoremos). Ambas estão a captar o ponto $P = (X,Y,Z)$
- Em cada uma das imagens consideremos um referencial $(u,v)$ com a origem no canto superior esquerdo. O ponto $P$ aparece nestas imagens nas coordenadas $r_{L},r_{R}$. 

## Triangulação
- Normalmente, consideremamos que a câmara da esquerda é a referência. Assim, é comum definir a origem *NA* câmara da esquerda:
![[visao stereo coords|600]]
- As coordenadas do ponto $P$ no plano da imagem consiste numa transformação 3D $\to$ 2D, em que: $(X,Y,Z)\to(x,y)$. 
- Considerando a origem na câmara esquerda como vimos acima, temos:
$$x_{L}=f \frac{X}{Z} \quad \quad;\quad \quad x_{R}=f \frac{X-\text{baseline}}{Z}$$
isto bate certo: como vemos acima, é possível termos $x_{L}>0$ e $x_{R}<0$ quando $X<\text{baseline}$.

- Podemos juntar estas 2 equações e temos:
$$Z = f \frac{\text{baseline}}{x_{L}-x_{R}}$$
e temos a **profundidade**!! Notamos que esta depende diretamente da *disparidade* entre as câmaras.

- Tendo a profundidade facilmente temos o resto das coordenadas de $P$:
$$X=f\frac{x_{L}}{Z} \quad;\quad Y=f\frac{y_{L}}{Z}$$
(e notemos que quando as imagens estão row aligned temos $y_{L}=y_{R}$)

- Este processo de obter $(X,Y,Z)$ usando as 2 câmaras é **triangulação**!!!

## Problema!
- Notemos algo acerca da equação que nos dá a profundidade:
$$Z=f \frac{\text{baseline}}{\Delta x}=\frac{\alpha}{\Delta x} \quad \quad \Delta x=\text{disparidade}$$
notemos que a relação entre a profundidade e a disparidade **NÃO É LINEAR**
- Isto tem uma implicação imediata: a resolução/sensibilidade desta equação varia com a profundidade:
    - Se tivermos um objeto perto das câmaras (profundidade baixa) ele vai aparecer em posições muito diferentes nas câmaras e temos alta resolução
    - Se tivermos um objeto muito longe temos menos resolução
- Vejamos uma representação intuitiva disto:
![[diferentes profundidades|600]]
![[visao estereo ideia.png]]

ou então, podemos ver o gráfico de $Z(\Delta x)$:
![[funcao 1 sobre x.png|650]]
- Notemos que consoante o ponto está mais longe ($Z$ mais elevado) temos $\Delta x\to0$. 

### Aumentar baseline
- Uma "solução" para isto é aumnetar a baseline. isto faz esta função cair mais lentamente:
![[funcao 1 sobre x a alargar.png|650]]
e isto, de facto, cria uma zona suave que é pouco vertical e pouco horizontal - algo desejado!
- Ou podemos ver o gráfico inverso: $\Delta x(Z)$:
![[disparidade vs profundidade.png]]

**Zona morta**
- Mas ao imaginar o sistema de câmaras vemos um problema:
![[zona morta vs baseline|900]]
podemos ver que ao afastar a câmara aumenta logo a zona que nenhuma das câmaras consegue ver.
- Ou seja:
    - Para ter dados de profundidade, precisamos da *disparidade*. Assim, precisamos que o ponto $P$ seja captado **pelas 2 câmaras** (zona verde na figura)
    - Temos a zona vermelha, que nenhuma câmara apanha e que está relacionada com o ângulo/abertura da lente da câmara
    - Temos a zona branca em que apenas 1 câmara apanha. Aí temos imagem, mas essa parte também é inútil para estudar a profundidade.

### Accuracy de profundidade
- Podemos definir a disparidade $d$ , a profundidade $Z$ e a baseline $T$. Temos: $d\propto \frac{1}{Z}$
- Podemos deifnir o erro/incerteza da profundidade $\partial Z$ que vai aumentar com $Z$ - ao afastar-nos da câmara a disparidade diminui. Ou seja: $\partial Z\propto Z$
- Vimos ainda que a baseline ajuda a melhorar esta situação, logo aumento da baseline diminui o erro. Temos: $\partial Z\propto \frac{1}{T}$
- Juntamos tudo e temos:
$$\partial Z=\frac{-Z^{2}}{fT}\partial d$$
## Correspondência
- Para extrair informação 3D com as imagens das câmaras precisamos de resolver 2 problemas:
    1. Conhecer a distância focal e a baseline - isto é a **calibração** do sistema de câmaras
    2. Para um certo pixel na imagem da esquerda $p_{L}$ temos que conhecer o pixel da direita $p_{R}$ que corresponde ao mesmo ponto $P$ do espaço 3D - isto é o **problema de correspondência**
![[disparidade vs profundidade 2.png]]

- Temos 2 tipos de maneiras de resolver isto:
    - **Denso**
        - Técnicas que minimizamos erros de disparidade à bruta: SSD, SAD, correlação cruzada
        - permite ter muitos mais pontos de disparidade mas mais pesado
        - "À bruta" e mais difícil
    - **Esparso**
        - Técnicas baseadas em determinação de features. Mais semelhante ao que fazíamos com registro de modelos 3D
        - Mais eficiente e robusto a transformações e ruído, mas temos muitos menos pontos

- Um caso de estero esparso pode resultar no seguinte agrupamento de features:
![[matches de metodo de features.png]]
Calculamos features em muitos pontos e encontramos pares de pontos (um em cada imagem) que têm boa correspondência de features.

## Epipolar constraint
- Esta é uma nova constraint que aplicamos. Ela permite reduzir este problema 2D de determinar disparities (temos que encontrar pares de pontos equivalentes em cada linha, para muitas linhas) em um problema 1D !!!
    - Isto torna este problema computacionalmente complexo em algo muito mais simples
- Além disso, estamos a generalizar a configuração da câmara - deixamos de precisar de ter eixos de visão paralelos!

### Geometria
![[plano epipolar.png]]
- Chamamos aos planos das câmaras de $I_{1},I_{2}$ e aos centroas das câmaras de $C_{1},C_{2}$

**Plano epipolar**
- Este plano é representado pelo triângulo azul. É definido pelos pontos $P,C_{1},C_{2}$
- Este plano interseta as imagens 1 e 2 numa reta: **linha epipolar** que vemos a roxo e vermelho na figura acima. 

**Epipoles**
- Os pontos ${}^{1}e,{}^{2}e$ representam as projeções de $C_{1},C_{2}$ em $2,1$ - Indicam como as câmaras se vêm uma à outra

**Linha epipolar**
- Podemos representar como ${}^{1}l,{}^{2}l$ e são obtidas ao intersetar o plano epipolar com $I_{1},I_{2}$
- Notemos que, como as câmaras estão fixas, *todas as linhas passam nos epipolos*!

#### Como funciona
- Temos então um ponto $P$ no espaço 3D. Ele resulta num ponto ${}^{1}p$ no plano $I_{1}$
- Ora, a projeção desse ponto para o plano $I_{2}$ ficará **sempre** dentro da linha epipolar ${}^{2}l$
- Ver melhor?? Maybe youtube

### Calcular
- Temos 2 métodos principais
    - **Structure from Motion (SfM)** AKA caso *não calibrado*
        - Temos a matriz **fundamental**, obtida de correspondências estero e obtemos a representação 3D com esta matriz
    - **3D reconstruction** AKA caso *calibrado*
        - Conhecemos todos os parâmetros do sistema de câmaras
        - Temos a matriz **essencial** que é obtida da geometria epipolar, que nos permite depois obter a representação 3D

#### Caso não calibrado
- Temos a matriz fundamental $\mathbf{F}$ que é 3x3 e contem:
    - Informação intríseca das 2 câmaras
    - Rotações e translações que relacionam os planos 1 e 2
- A restrição epipolar fica nesta forma:
$${}^{2}\tilde{p}^{T} ~\mathbf{F}~ {}^{1}\tilde{p}=0 $$
em que ${}^{1}\tilde{p},{}^{2}\tilde{p}$ são as coordenadas dos pontos na imagem ${}^{1}p,{}^{2}p$ MAS expressos em coordenadas homogéneas.
- Podemos ainda definir que:
$${}^{2}\tilde{l}=\mathbf{F}~{}^{1}\tilde{p}$$
ou até: ${}^{1}\tilde{l}=\mathbf{F}~{}^{2}\tilde{p}$ 
- Mas podemos achar estranho ter um produto de matrizes nulo. Mas podemos interpretar isto como produtos escalares: 
    - Quando aplicamos $\mathbf{F}$ a um ponto do plano $I_{1}$ obtemos a linha epipolar associada a esse ponto, no outro plano.
    - Assim, a equação epipolar fica: $${}^{2}\tilde{p}^{T} ~\mathbf{F}~ {}^{1}\tilde{p}={}^{2}\tilde{p}^{T}~ {}^{2}\tilde{l}$$
    - Segundo o ChatGPT, o vetor $\tilde{l}$ dá-nos um vetor NORMAL à reta. Pensamos que um plano pode ser definido por $ax+by+c=\mathbf{n}\cdot \tilde{x}$  em que $\mathbf{n}=\begin{pmatrix}a & b & c\end{pmatrix}$ é o vetor normal ao plano. A lógica aqui é a mesma. 
    - Assim, é evidente que o vetor da posição de um ponto ${}^{2}\tilde{p}$ no plano $I_{2}$ será **perpendicular** ao vetor normal da reta. Logo teremos: $${}^{2}\tilde{p}^{T}~ {}^{2}\tilde{l}=0={}^{2}\tilde{p}^{T} ~\mathbf{F}~ {}^{1}\tilde{p}$$

- Notemos que, devido a como funciona a matriz, temos 2 casos particulares:
$$\mathbf{F}~{}^{1}e=0=\mathbf{F}~{}^{2}e$$

##### Comp Vis
- Como vimos na aula 6.0 (de Computer Vision), podemos representar um ponto $P$ no plano de imagem com:
$$\tilde{p}=\mathbf{M} P$$
em que temos a matriz de projeção:
$$\mathbf{M}=\mathbf{KE}=\mathbf{K}\begin{pmatrix}\mathbf{R} & \mathbf{t}\end{pmatrix}$$
e temos:
$$\mathbf{M}_{1}=\mathbf{K}_{1}\begin{pmatrix}\mathbf{I} & \mathbf{0}\end{pmatrix} \quad;\quad \mathbf{M}_{2}=\mathbf{K}_{2}\begin{pmatrix}\mathbf{R} & \mathbf{t}\end{pmatrix}$$
(em que estamos a considerar 1 a câmara de referência, normalmente à esquerda)

- Tendo isto em conta, a matriz fundamental é dada por
$$\mathbf{F}=\mathbf{K}_{2}^{-T}[\mathbf{t}]_{\times}\mathbf{ R}\mathbf{K}_{1}^{-1}$$
- Uma nota sobre notação:
    - $\mathbf{t}=\begin{pmatrix}t_{x} & t_{y} & t_{z}\end{pmatrix}$ é o vetor de translação
    - $[\mathbf{t}]_{\times}$ é uma matriz *skew-symmetrical* ou *antissimétrica*. Isto são todas as matrizes em que $[\mathbf{t}]_{\times}^{T}=-[\mathbf{t}]_{\times}$. No caso de translação temos:
$$[\mathbf{t}]_{\times}=\begin{bmatrix}0 & -t_{z} & t_{y} \\ t_{z} & 0 & -t_{x} \\ -t_{y} & t_{x} & 0\end{bmatrix}$$

##### SVD
- Podemos fazer decomposição SVD da matriz fundamental:
$$\mathbf{F}=\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^{T}=\begin{pmatrix}\mathbf{u}_{1} & \mathbf{u}_{2} & {}^{2}\mathbf{e}\end{pmatrix}\begin{pmatrix}\sigma_{1} & 0 & 0 \\ 0 & \sigma_{2} & 0 \\ 0 & 0 & 0\end{pmatrix}\begin{pmatrix}\mathbf{v}_{1}^{T} \\ \mathbf{v}_{2}^{T} \\ {}^{1}\mathbf{e}^{T}\end{pmatrix}$$
não entendi mas prontoooo

##### Propriedades de F
- Matriz única por escala (pode dar com escala diferente mas é única para o sistema)
- Tem rank 2, porque $[\mathbf{t}]_{\times}$ tem rank 2
    - Tem 9 elementos que NÃO são independentes
    - $\det\mathbf{F}=0$
- Tem 7 DOF: 
    - 9 elementos - 1 DOF (variável em escala) - 1 DOF (determinante nulo) = 7 DOF
    - 2 de cada epipolo (coordenadas x,y de capa epipolo) = 4 DOFs
    - 3 de cada homografia que relaciona os 2 planos - Não entendi
- Ou seja, precisamos de pelo menos 7 correspondências de pontos para poder relacionar as imagens das 2 câmaras

##### Porquê o caso não calibrado?
- Até aqui consideramos este caso para considerar algo mais genérico, em que **não conhecemos**
    - As propriedaeds intrísecas das câmaras, podendo-se ter 2 câmaras diferentes no sistema
    - A localização relativa das câmaras (baseline), o que significa que não conhecemos o vetor $\mathbf{t}$
    - A matriz de rotação $\mathbf{R}$ que transforma a imagem 2 na 1

**Resolver**
- Podemos determinar primeiro correspondências com métodos de features. Tendo 8 correspondências temos a matriz $\mathbf{F}$ porque cada ponto ${}^{1}p$ tem de estar associado a um ponto ${}^{2}p$ que está na sua linha epipolar. Ou seja: ${}^{2}\tilde{p}^{T} ~\mathbf{F}~ {}^{1}\tilde{p}=0$ 
- Assim, podemos fazer um sistema de 8 equações e 7 incógnitas, uma equação por correspondência.

#### Caso calibrado
- É relativamente parecido ao caso não calibrado:
$${}^{2}\tilde{p}_{c}^{T}~\mathbf{E}~{}^{1}\tilde{p}_{c}=0$$
em que $\mathbf{E}$ é a matriz **essencial**.
- Notemos que $\tilde{p}_{c}$ são as coordenadas *normalizadas* (normalmente colocamos a origem do referencial da imagem no centro das imagens), escrita em coordenadas homogéneas.

- No caso calibrado já conhecemos os parâmetros intrísecos das câmaras logo podemos escrever:
$$\mathbf{E}=\mathbf{K}_{2}^{T}\mathbf{FK}_{1}$$
e 
$$\mathbf{E}=[\mathbf{t}]_{\times}\mathbf{R}$$
- A primeira equação diz-nos que, tal como seria de esperar, o caso calibrado é o caso não calibrado em que introduzimos as informações intrísecas das câmaras
- A segunda equação diz-nos que $\mathbf{E}$ é puramente geométrico!!!

### Retificação
- Na realidade os sistemas não são frontal paralelos
- Começamos por fazer um sistema quase paralelo e com bom alinhamento, para facilitar as contas
- Com isso feito, captados imagens de grids xadrez em que sabemos todas as dimensões.
    - Conhecer a imagem real permite-nos remover distorção e retificar!
![[processo de tratamento de imagens antes de stereo vision.png]]

- Com a imagem retificada:
    - Temos as imagens que teríamos SE o sistema fosse frontal paralelo
    - Devido ao ponto anterior, as epilines não **horizontais**
    - A matriz $\mathbf{R}$ e o vetor $\mathbf{t}$ vêm deste processo de retificação