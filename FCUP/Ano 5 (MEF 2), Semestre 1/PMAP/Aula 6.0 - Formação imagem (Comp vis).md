## Modelo de câmara pinhole
- Modelo mais simples, aplicável quando a temos lentes com distância focal longa
    - Este é o caso temos baixa distorção radial da imagem e podemos só ignorá-la
- Podemos representar o sistema de câmara ao colocar uma barreira com um orificio pequeno em frente ao cenário 3D que estamos a capturar:
![[geracao imagem camara aperture.png]]
- Consideramos isto:
    - Cada ponto do objeto 3D emite vários raios
    - Apenas alguns raios passam na abertura (ver imagem acima). Teoricamente, **1 raio de cada ponto** passa na abertura
    - Mapeamos ponto a ponto e ficamos com uma imagem invertida, como vemos acima

![[aperture vs imagem obtida.png]]
- Assim:
    - *Aumentar abertura* - o número de pontos que passam na abertura aumenta e a imagem fica desfocada
    - *Diminuir abertura* - passam menos pontos então a imagem fica mais focada (ficamos mais perto do caso teórico), mas também fica mais escura (temos menos luz)
    - *Abertura MUITO pequena* - a certo ponto a imagem volta a desfocar porque começa a ocorrer **difração**

### Lentes
- Permitem focar (ou espalhar) raios de luz. isto permite passar mais luz para a imagem, *sem a desfocar*
- Idealmente, conseguimos garantir que todos os raios que saem do objeto 3D chegam à imagem:
![[geracao imagem camara lente.png]]

#### Propriedades
- Raios que passem no centro da lente NÃO são desviados (vemos isso acima). 
- Todos os raios que são paralelos ao eixo ótico são desviados para o ponto focal
- **Distância focal (f)** - distância entre o centro da lente e o ponto focal.

#### Lei de Lens
![[lente otica geometrica.png]]
- Esta lei diz que:
$$\frac{1}{z_{0}} + \frac{1}{z_{i}}= \frac{1}{f}$$
em que temos $z_{o},z_{i}$ as posições do objeto 3D original e da imagem criada, ao longo do eixo ótico.

**Imagem em pinhole**
- Uma câmara pin-hole não *precisa de foco* quando tem uma lente:
    - Uma camara pinhole apenas foca 1 plano. Se focarmos os raios no plano focal, teremos imagem nítida. Chamamos a este de **plano de foco**
- Sendo assim, definimos a **depth of field (DF)** : range de distâncias em que podemos gerar a imagem em torno do plano de foco, de modo que ela seja perceptível. 
- Se os raios forem focados em planos antes ou depois do plano focal resultam em *circles of confusion* - obtemos blur / desfocado
![[lente circulos de confusao.png]]

**Circle of confusion (CC)**
- Depende de $\Delta z_{i}$: distância entre o plano da imagem e o plano de foco e de $d$: diâmetro de abertura
![[lente focar 2 pontos.png]]
$$CC = \frac{\Delta z_{i} \cdot d}{2z_{i}}$$
para ter uma imagem nítida convém ter $CC<1\text{ pixel}$

### Projeção de perspetiva
- Usando o modelo de câmara pinhole, podemos facilmente establecer uma relação matemática entre um ponto $(x,y)$ na imagem captada e um ponto $(X,Y,Z)$ do objeto 3D
![[projecao de ponto vida real em imagem de camara.png]]
- Na imagem acima, podemos fazer semelhança de triangulos entre o da esquerda (abaixo do eixo ótico) e o da direita (acima do eixo):
$$\frac{x}{-f}=\frac{X}{Z}~~\to~~ x= -f \frac{X}{Z}$$
- Consideremos agora o modelo de **imagem virtual**: consideramos então que a imagem está em frente ao plano de foco e não atrás
![[projecao ponto vida real versao simplificada.png]]
e perdemos o sinal negativo porque agora a imagem está em frente:
$$x = f \frac{X}{Z}$$
e temos as matrizes de transformação:
![[tipos de matrizes transformacao.png|500]]

#### Definição
- Esta projeção consiste em $\mathbb{R}^{3}\to\mathbb{R}^{2}$ e é uma projeção *linear* de matriz 
$$\begin{pmatrix}X & Y & Z\end{pmatrix}^{T} ~~\to~~ \begin{pmatrix}f \dfrac{X}{Z} &  f \dfrac{Y}{z}\end{pmatrix}^{T}$$
- E temos as propriedades:
    - linhas retas no mundo (3D) são linhas retas na imagem (2D)
    - linhas paralelas no mundo são linhas que se intersetam no vanishing point da imagem (**efeito de perspetiva**)
    - não existe uma solução única que inverta $(x,y)$ de volta para $(X,Y,Z)$
    - não se matêm formas em geral

### Cálculos
- Temos as coorenadas do ponto $P$ no referencial mundo $(X_{W},Y_{W},Z_{W})$ e o referencial da câmara $(X_{C},Y_{C},Z_{C})$ e temos a sua projeção no referencial da imagem $(x,y)$
![[captacao de ponto real por 2 camaras.png]]

- Podemos relacionar os referenciais do mundo e da câmara com uma *transformação de corpo rígido*:
    - $\mathbf{R}$ é a matriz de rotação 3x3 do referencial da câmara relativamente ao referencial mundo
    - $\mathbf{t}$ é o vetor de translação 3x1 que move o referencial da câmara relativamente ao mundo

**1. Converter mundo para camara**
- Converter mundo para camara:
$$\begin{pmatrix}X_{C} \\ Y_{C} \\ Z_{C}\end{pmatrix} = \mathbf{R} \begin{pmatrix}X_{W} \\ Y_{W} \\ Z_{W}\end{pmatrix} + \mathbf{t}$$
e podemos escrever isto em coordenadas homogéneas:
$$\begin{pmatrix}X_{C} \\ Y_{C} \\ Z_{C}\end{pmatrix}=\begin{pmatrix}\mathbf{R} & \mathbf{t}\end{pmatrix} \begin{pmatrix}X_{W} \\ Y_{W} \\ Z_{W} \\ 1\end{pmatrix}$$
e temos a **matriz extrinsica (P)** que é a matriz 3x4 definida por
$$\mathbf{P} = \begin{pmatrix}\mathbf{R} & \mathbf{t}\end{pmatrix}$$

**2. Projetar Pc para o plano da imagem (x,y)**
- Tendo o plano da imagem a uma distância $f$ do centro ótico:
![[prtojecao de ponto real para plano imagem da camara.png]]

- A projeção em perspetiva de $P_{C}$ ($P$ no referencial da câmara) no plano da imagem é dada por:
$$\alpha \begin{pmatrix}x \\ y \\ 1\end{pmatrix}=\begin{pmatrix}f & 0 & 0 \\ 0 & f & 0 \\ 0 & 0 & 1\end{pmatrix} \begin{pmatrix}X_{C} \\ Y_{C} \\ Z_{C}\end{pmatrix}$$
isto é *simplificado* e resulta de $x=f \frac{X}{Z}$

**3. Converter (x,y) para coordenadas de pixeis (u,v)**
- Consideremos
    - $(c_{x},c_{y})$ as coordenadas dos pixeis do centro da câmara
    - $(f_{x},f_{y})$ as distâncias de foco. Usamos 2 porque os pixeis no sensor podem não ser quadrados
- Assim, temos um referencial $(u,v)$ centrado no canto superior esquerdo. Temos:
$$\alpha \begin{pmatrix}u \\ v \\ 1\end{pmatrix}= \begin{pmatrix}f_{x} & \gamma & c_{x} \\ 0 & f_{y} & c_{y} \\ 0 & 0 & 1\end{pmatrix}\begin{pmatrix}X_{C} \\ Y_{C} \\ Z_{C}\end{pmatrix}$$
e aqui temos a **matriz intríseca**:
$$\mathbf{K}=\begin{pmatrix}f_{x} & \gamma & c_{x} \\ 0 & f_{y} & c_{y} \\ 0 & 0 & 1\end{pmatrix}$$
e definimos o referencial não homogéneo dos pixeis:
$$u'=\frac{u}{\alpha} \quad;\quad v'=\frac{v}{\alpha}$$

**Matriz de Projeção**
- Permite resumir a conversão toda do referencial mundo para o referencial dos pixeis
- Definimos:
$$\begin{align*}
\mathbf{M}=\mathbf{K} \mathbf{E}=\mathbf{K}\begin{pmatrix}\mathbf{R} & \mathbf{t}\end{pmatrix}
\end{align*}$$
e a transformação toda é dada por
$$\alpha \begin{pmatrix}u \\ v \\ 1\end{pmatrix} = \mathbf{K}\begin{pmatrix}\mathbf{R} & \mathbf{t}\end{pmatrix} \begin{pmatrix}X_{W} \\ Y_{W} \\ Z_{W} \\ 1\end{pmatrix}$$

## Distorção de lentes
- Normalmente resultam do facto que as lentes não são perfeitas
- Temos 2 componentes: radial e tangencial

#### Distorção radial
- Linhas retas no mundo real aparecem como curvas na imagem. 
- Isto acontece porque a lente é curva então os pontos do objeto são transmitido ao longo de eixos radiais para a câmara
- **Distorção de barril** - desvio radial negativo (força diminui com distância da câmara) (fisheye)
- **Distorção de alfinete** - desvio radial positivo (força aumenta com distância da câmara)
![[tipos de distorcao camara.png]]

#### Distorção tangencial
- A imagem parece inclinada e esticada porque temos um ângulo entre o eixo da lente e o sensor da câmara:
![[distorcao tangencial camara.png]]

#### Remover distorção
- Podemos fazer isto sabendo os coeficientes de distorção:
$$\begin{pmatrix}\delta_{u} \\ \delta_{v}\end{pmatrix}=\begin{pmatrix}u(k_{1}r^{1}+k_{2}r^{4}+k_{3}r^{6}+\dots) \\ v(k_{1}r^{1}+k_{2}r^{4}+k_{3}r^{6}+\dots)\end{pmatrix}+\begin{pmatrix}2p_{1}uv + p_{2}(r^{2}+2u^{2} \\ p_{1}(r^{2}+2v^{2})+2p_{1}v\end{pmatrix}$$
em que o primeiro termo representa a distorção radial e o segundo tangencial.

- O vetor $\delta$ apresenta o desvio causado pelo erro. Para remover a distorção, fazemos então
$$\begin{pmatrix}u^{u} \\ v^{u}\end{pmatrix}=\begin{pmatrix}u^{d} \\ v^{d}\end{pmatrix}-\begin{pmatrix}\delta^{x} \\ \delta^{y}\end{pmatrix}$$

## Calibração de câmara
- A calibração consiste em determinar os **parâmetros da câmara**: queremos uma relação entre o ponto mundo $P_{W}\in\mathbb{R}^{3}$ e a sua representação nos píxeis da imagem $(u,v)\in\mathbb{N}_{0}^{2}$
- Queremos determinar ainda as **distorções** radial e tangencial da câmara.

**Inputs**
- Recolhemos várias imagens ocm pontos cujas coordenadas 2D e 3D sejam conhecidas. 
- Para cada imagem, calculamos a matriz $\begin{bmatrix}\mathbf{R}|\mathbf{t}\end{bmatrix}$

**Outputs**
- Obtemos a matriz intrínseca $\mathbf{K}$ e a matriz extrínseca $[\mathbf{R}|\mathbf{t}]$ 
- Determinamos ainda os coeficientes de distorção

**Método**
- Para recolher imagens em que conhecemos as coordenadas 2D e 3D, usamos uma grid xadrez em que conhecemos os tamanhos dos quadrados e conhecemos a posição da tela relativamente à câmara