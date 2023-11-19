# 1-Vetores
- **Vetores** têm direção e magnitude/comprimento. De notar que não têm localização, podemos _arrastá-los_ no espaço
- Quantidades que têm magnitude, mas não direção, são **escalares**
- Nestes resumos vou usar a sequinte notação:
    - $\mathbf{E}$ é um vetor, mas por vezes irei usar $\vec{E}$
    - $E$ é o módulo/magnitude do vetor
    - $(-\mathbf{E})$ é o vetor com módulo e direção igual a $\mathbf{E}$ mas sentido oposto
    -  $\hat{}$  (acento circunflexo) marca vetores unitários
    - $\vec 0$ é o vetor nulo
- **Pseudo vetores** - "vetores" que se comportam como vetores na maioria dos casos, exceto se fizermos certas transformações como rotação, reflexão, inversão dos eixos. Nesses casos, a direção de pseudo vetores não se comporta como esperado (ver ex 1.10 do Griffiths)
    - Por exemplo: ao inverter os 3 eixos, um vetor normal torna-se no seu simétrico: $\mathbf{A}\to-\mathbf{A}$. Um pseudovetor não é afetado: $\mathbf{B}\to\mathbf{B}$
    - Exemplos: torque e momento angular


## 1.1 - Operações
- Temos 4 operações:
### 1.1.1 - Soma de Vetores
![[Pasted image 20230211230929.png]]
- Podemos ver então que na soma de vetores, na realidade, _arrastamos_ o segundo vetor para a extremidade do segundo.
- Sendo que temos que a adição de vetores é:
$$\mathbf{A}+\mathbf{B}=\mathbf{B}+\mathbf{A} \quad \quad \textsf{(comutativa)}$$
$$(\mathbf{A}+\mathbf{B})+\mathbf{C} =\mathbf{B}+(\mathbf{A}+\mathbf{C}) \quad \quad \textsf{(associativa)}$$
- E vemos que ao fazer $\mathbf{A}-\mathbf{B}$, na realidade estamos a fazer $\mathbf{A}+(-\mathbf{B})$

### 1.1.2 - Multiplicação por escalar
- Aumenta o módulo do vetor (_estica-o_), mas mantém a direção. Se o escalar for negativo, inverte-se o sentido.
- Temos:
$$a(\mathbf{A}+\mathbf{B})=a \mathbf{A}+a \mathbf{B} \quad \quad \textsf{(distributiva)}$$

### 1.1.3 - Produto Escalar de vetores
![[Pasted image 20230211233034.png]]
- Tendo em conta os 2 vetores acima, o produto escalar entre eles é
$$\mathbf{A}\cdot \mathbf{B} \equiv AB\cos \theta$$
- Podemos ver o produto escalar como o módulo de $\textbf{A}$ vezes o módulo da projeção de $\textbf B$ em $\textbf A$ 
- Ou seja, o produto escalar é um escalar
- Este produto é 
$$\mathbf{A}\cdot\mathbf{B}=\mathbf{B}\cdot\mathbf{A} \quad \quad \textsf{(comutativo)}$$
$$\mathbf{A}\cdot(\mathbf{B}+\mathbf{C})=\mathbf{A}\cdot\mathbf{B}+\mathbf{A}\cdot \mathbf{C} \quad \quad \textsf{(distributiva)}$$
- Temos 3 casos particulares:
    - Se $\mathbf{A} \parallel\mathbf{B}$, então $\mathbf{A}\cdot \mathbf{B}=AB$ 
    - Se $\mathbf{A}\perp\mathbf{B}$, então $\mathbf{A}\cdot \mathbf{B}=0$
    - $\mathbf{A} \cdot \mathbf{A} = A^2$

> Tendo o triângulo abaixo 
> ![[Pasted image 20230212001843.png]]
> Temos $\mathbf{C} = \mathbf{A} -\mathbf{B}$. Se fizermos:
> $$\mathbf{C}\cdot \mathbf{C}=(\mathbf{A}-\mathbf{B})\cdot(\mathbf{A}-\mathbf{B})=\mathbf{A}\cdot \mathbf{A} - \mathbf{A}\cdot \mathbf{B} - \mathbf{B}\cdot \mathbf{A}-\mathbf{B}\cdot \mathbf{B}$$
> Obtemos:
> $$C^{2}=A^{2}+B^{2}+2AB\cos \theta$$que é a ==Lei dos Cossenos==

### 1.1.4 - Produto Vetorial
![[Pasted image 20230212002339.png]]
- Para os vetores $\vec A$ e $\vec B$, de módulos $A$ e $B$, que temos acima, tem-se que $$\mathbf{A} \times \mathbf{B} \equiv AB\sin \theta~\hat{\text{n}}$$
(sendo $\hat{\text{n}}$ o vetor unitário perpendicular a $\textbf A$ e $\textbf B$. Ele pode ter 2 direções, mas sabemos qual delas é que dá o produto vetorial através da regra da mão direita)
- Temos que o produto vetorial é
$$(\mathbf{A} \times \mathbf{B})=-(\mathbf{B} \times \mathbf{A}) \quad \quad (\textsf{anti-comutativo})$$
$$\mathbf{A} \times (\mathbf{B} +\mathbf{C})=(\mathbf{A} \times \mathbf{B}) + (\mathbf{A} \times \mathbf{C}) \quad \quad (\textsf{distributivo})$$
- Do ponto de vista geométrico, temos também que o módulo do produto vetorial dá a àrea do paralelogramo definido pelos vetores (ver a Figura 3)
- Temos ainda que, para qualquer vetor, $$\mathbf{A}\times \mathbf{A}=\vec{0}$$

## 1.2-Forma de Componentes
- Vamos agora definir vetores como um conjunto de **componentes**, definidas em coordenadas cartesianas. Assim, cada vetor será definido por 3 componentes: em $x, y$ e $z$. Sendo $\hat{x}, \hat{y}, \hat{z}$ os vetores unitários nas 3 direções, temos:
![[Pasted image 20230212004147.png]]
- Pelo que o vetor $\textbf A$ pode ser decomposto da seguinte forma:
$$\mathbf{A}=A_{x}\hat{x}+A_{y}\hat{y}+A_{z}\hat{z}$$
(Podemos ver que $A_{x}=\vec A \cdot \hat{x}$ e igual para $y$ e $z$)

- Podemos então reformular cada uma das operações de vetores que vimos acima com componentes:

#### Adição
$$\begin{align*}
\mathbf{A} + \mathbf{B} &= (A_{x}\hat{x}+A_{y}\hat{y}+A_{z}\hat{z}) + (B_{x}\hat{x}+B_{y}\hat{y}+B_{z}\hat{z})\\
&= (A_{x}+B_{x})\hat{x} + (A_{y}+B_{y})\hat{y} + (A_{z}+B_{z})\hat{z}
\end{align*}$$
#### Multiplicação por escalar
$$a\mathbf{A}=(aA_{x})\hat{x}+(aA_{y})\hat{y}+(aA_{z})\hat{z}$$
#### Produto Escalar
- Como $\hat{x}\cdot \hat{x}=\hat{y}\cdot \hat{y}=\hat{z}\cdot \hat{z}=1$  e  $\hat{x}\cdot \hat{y}=\hat{y}\cdot \hat{z}=\hat{x}\cdot \hat{z}=0$, então:
$$\mathbf{A}\cdot \mathbf{B}= A_{x}B_{x}+A_{y}B_{y}+A_{z}B_{z}$$
- Pelo que temos $\mathbf{A} \cdot \mathbf{A} = A_{x}^{2}+A_{y}^{2}+A_{z}^{2}$
- Logo temos $|\mathbf{A}|=\sqrt{\mathbf{A} \cdot \mathbf{A}}=\sqrt{A_{x}^{2}+A_{y}^{2}+A_{z}^{2}}$

#### Produto Vetorial
- Usando a mesma lógica do produto escalar (calcular produto vetorial $\hat{x}\times \hat{x},~\hat{x}\times \hat{\mathbf{y}}$, etc...), podemos obter que 
$$\mathbf{A} \times \mathbf{B} = (A_{y}B_{z}-A_{z}B_{y})\hat{x}+(A_{z}B_{x}-A_{x}B_{z})\hat{y}+(A_{x}B_{y}-A_{y}B_{x})\hat{z}$$
Sendo que podemos escrever isto como:
$$\mathbf{A}\times \mathbf{B} = \begin{vmatrix}\hat x &\hat y &\hat z \\ A_{x} &A_{y} &A_{z}  \\ B_{x} &B_{y} &B_{z}\end{vmatrix}$$

## 1.3-Produtos Triplos
- Como um produto vetorial é um vetor, podemos fazer um produto escalar ou vetorial com este.

### 1.3.1-Produto Escalar Triplo
$$\mathbf{A} \cdot (\mathbf{B}\times \mathbf{C})$$
- Do ponto de vista geométrico, $|\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C})|$ é o volume do paralelepípedo defenido por $\mathbf{A},\mathbf{B}, \mathbf{C}$. O módulo do produto vetorial dá a área da base e o produto escalar vai "projetar a base ao longo da altura".
- Por outro lado, podemos ver que podemos definir esse paralelepipedo usando outra ordem de vetores:
$$\mathbf{A}\cdot(\mathbf{B} \times \mathbf{C})=\mathbf{B} \cdot(\mathbf{C} \times \mathbf{A})=\mathbf{C} \cdot(\mathbf{A} \times \mathbf{B})$$
(note-se que se partir-mos do $\mathbf{A}$ e andarmos para a direita, em qualquer um dos casos acima a ordem alfabética mantém-se)
- Se usarmos componentes temos que:
$$\mathbf{A} \cdot(\mathbf{B} \times \mathbf{C})=\begin{vmatrix}A_{x} &A_{y} &A_{z} \\ B_{x} &B_{y} &B_{z} \\ C_{x} &C_{y} &C_{z}\end{vmatrix}$$
- Podemos ainda trocar a ordem de operações assim: $\mathbf{A} \cdot(\mathbf{B} \times \mathbf{C})=(\mathbf{A} \times \mathbf{B}) \cdot \mathbf{C}$

### 1.3.2-Produto Vetorial Triplo
$$\mathbf{A}\times (\mathbf{B}\times \mathbf{C}) = \mathbf{B}(\mathbf{A} \cdot \mathbf{C})-\mathbf{C}(\mathbf{A} \cdot \mathbf{B})$$
- Para decorar isto podemos decorar que este produto é igual a **BAC - CAB**
- Temos que $\mathbf{A} \cdot(\mathbf{B} \times \mathbf{C}) = - [(\mathbf{A} \cdot\mathbf{B}) \times \mathbf{C}]$

## 1.4 - Posição, Deslocamento e Separação
![[Pasted image 20230212142350.png]]
- O vetor que aponta da origem para a posição do ponto é o *vetor posição*: 
$$\mathbf{r} \equiv x \hat x + y \hat y +z \hat z$$
Pelo que $r =\sqrt{x^{2}+y^{2}+z^{2}}$ é a distância do ponto à origem
- Temos então $\hat r$, o *vetor radial unitário* para esse vetor posição: 
$$\hat r=\frac{\mathbf{r}}{r}=\frac{x \hat x+ y \hat y + z \hat z}{\sqrt{x^{2}+y^{2}+z^{2}}}$$
- O *vetor de deslocamento infinitesimal* (vetor que descreve deslocamento de $(x,y,z)$ para $(x+dx, y+dy, z+dz)$) é 
$$d \mathbf{l}=dx \hat x+dy \hat y+dz \hat z=d \mathbf{r}$$
### 1.4.1 - Vetor de Separação
- Imaginemos um caso comum: temos um ponto fonte, em que temos uma carga, $\mathbf{r}'$, e um ponto $\mathbf{r}$ , no qual queremos calcular o campo elétrico. Podemos então definir um *vetor e separação* entre esses 2 pontos:
$$\vec{\mathbb{r}}\equiv \mathbf{r} - \mathbf{r}'$$
Tal que $$\hat{\mathbb{r}}=\frac{\vec{\mathbb{r}}}{\mathbb{r}}=\frac{\mathbf{r}-\mathbf{r}'}{|\mathbf{r}-\mathbf{r}'|}$$
Sendo que em coordenadas cartesianas temos: 
$$\vec{\mathbb{r}}=(x-x')\hat{x}+(y-y')\hat{y}+(z-z')\hat{z}$$

## 1.5 - Transformações e Direção de Vetores
- Atrás, definimos um vetor como algo com um módulo e direção. 
- Podemos definir um vetor como sendo algo que apresenta 3 componentes que possam ser adicionados como um vetor? Não. É preciso que o vetor tenha uma direção e que se transforme de forma correta ao mudar de coordenadas.

- Consideremos que temos um vetor $\mathbf{A}=A_{x}\hat{x}+A_{y}\hat{y}+A_{z}\hat{z}$. Tal como vemos na figura abaixo, temos: $A_{y}=A\cos\theta~~,~~A_{z}=A\sin\theta$ :
![[rotacao de referencial.png]]
- Consideremos agora que rodamos o referencial um ângulo $\phi$ em torno do eixo dos $x$, que portanto não é afetado.
- Já nos $y$ e $z$, temos que $A_{y}\to \overline{A_{y}}~~,~~A_{z}\to \overline{A_{z}}$ 
- Conforme a figura acima, temos que:
$$\begin{align*}
\overline{A_{y}}&= A\cos \bar\theta=A\cos(\theta-\phi)=A(\cos \theta \cos \phi+\sin \theta\sin \phi)\\
&= \cos \phi A_{y} + \sin \phi A_{z}\\
\overline{A_{z}}&= A\sin \bar\theta=A\sin(\theta-\phi)=A(\sin \theta \cos \phi - \cos \theta \sin \phi)\\
&= -\sin \phi A_{y} + \cos \phi A_{z}
\end{align*}$$
- Em termos matriciais:
$$\begin{pmatrix}\overline{A_{y}}\\\overline{A_z}\end{pmatrix}=\begin{pmatrix}\cos \phi &\sin \phi\\ -\sin \phi&\cos \phi\end{pmatrix} \begin{pmatrix}A_{y}\\ A_{z}\end{pmatrix}$$
Ou seja, para uma transformação geral tem-se:
$$\begin{pmatrix}\overline{A_{x}}\\\overline{A_{y}}\\\overline{A_{z}}\end{pmatrix}=\begin{pmatrix}R_{xx}&R_{xy}&R_{xz}\\R_{yx}&R_{yy} &R_{yz}\\R_{zx}&R_{zy}&R_{zz}\end{pmatrix}\begin{pmatrix}A_{x}\\A_{y}\\A_{z}\end{pmatrix} \Longrightarrow \overline{A_{i}}=\sum\limits_{j=1}^{3}R_{ij}A_{j}$$

# 2 - Cálculo Diferencial
## 2.0 - Derivadas
$$df=\left( \frac{df}{dx} \right)dx$$
- Tendo uma função $f(x)$, a sua derivada, $\frac{df}{dx}$, dá-nos a relação entre uma pequena variação de $x$ ($dx$) e a variação de $f$ que esta causa ($df$).
- Sabemos ainda que, em termos geométricos, $\frac{df}{dx}$ nos dá o declive da reta tangente a $f$ num ponto $x$.

## 2.1 - Gradiente
- Consideremos a função $T(x,y,z)$ que define a temperatura num ponto de uma dada sala. 
- Temos que 
$$dT=\left(\frac{\partial T}{\partial x}\right)dx+\left(\frac{\partial T}{\partial y}\right)dy+\left(\frac{\partial T}{\partial z}\right)dz$$
- Isto mostra como $T$ irá variar se $x,y$ e/ou $z$ variar uma quantidade infinitesimal.
- Podemos ver que a equação acima tem a forma de um produto escalar, pelo que:
$$\begin{align*}
dT &=\left(\frac{\partial T}{\partial x}\hat{x}+\frac{\partial T}{\partial y}\hat{y}+\frac{\partial T}{\partial z}\hat{z}\right)\cdot(dx \hat{x}+dy \hat{y}+dz \hat{z})\\
&= (\nabla T)\cdot(d \mathbf{l})\\
&=|\nabla T||d \mathbf{l}|\cos\theta
\end{align*}$$
- Temos então o **gradiente** de $T$: $\nabla T=\frac{\partial T}{\partial x}\hat{x}+\frac{\partial T}{\partial y}\hat{y}+\frac{\partial T}{\partial z}\hat{z}$
- Do ponto de vista geométrico, o gradiente aponta na direção em que há maior aumento de $T$ (porque $dT$ será máximo quando $\cos\theta=1\to \theta=0$, ou seja, os 2 vetores têm a mesma direção). O módulo do gradiente dá o _rate_ de aumento da função.
- Se num ponto $\nabla T=0$, então $dT=0$. Ou seja, esse ponto é _estacionário_, sendo que pode ser um máximo, mínimo, ponto de sela ou nenhum. Isto pode ser comparado a como a derivada de uma função 1D é nula nos extremos.

## 2.2 - Operador Nabla / Del
- O gradiente de $T$ é, na verdade, $\nabla T=\nabla \cdot T$, em que $T$ é uma função escalar. Assim, temos o "vetor"/operador nabla:
$$\nabla \equiv\hat{x}\frac{\partial}{\partial x}+\hat{y}\frac{\partial}{\partial y}+\hat{z}\frac{\partial}{\partial z}$$
> Escrevi "vetor" entre aspas, porque sem estar a atuar numa função escalar este operador não tem significado. De tal modo, na realidade não temos nada a "multiplicar $T$ ". Nabla é na verdade um _operador vetorial_ que _atua_ em $T$.

- Este operador pode atuar de 3 formas:
    - Numa função escalar: _gradiente_ $\nabla T$
    - Numa função vetorial, com produto escalar: _divergência_ $\nabla \cdot \vec{v}$
    - Numa função vetorial, com produto vetorial: _rotacional_ $\nabla \times \vec{v}$

### 2.2.1 - Divergente
- Tendo uma função vetorial $\vec{v}=v_{x}\hat{x}+v_{y}\hat{y}+v_{z}\hat{z}$, temos que o seu divergente é 
$$\nabla \cdot \vec{v}=\frac{\partial v_{x}}{\partial x}+\frac{\partial v_{y}}{\partial y}+\frac{\partial v_{z}}{\partial z}$$
- Geometricamente, o divergente de uma função num ponto mede o quanto a função _diverge_ do ponto. Se for positivo, a função afasta-se do ponto; se for negativo, a função "acumula-se" no ponto.

### 2.2.2 - Rotacional
- Tendo uma função vetorial $\vec{v}=v_{x}\hat{x}+v_{y}\hat{y}+v_{z}\hat{z}$, temos o seu rotacional:
$$\nabla \times \vec{v}=\begin{vmatrix}\hat{x} &\hat{y} &\hat{z} \\ \frac{\partial}{\partial x} &\frac{\partial}{\partial y} &\frac{\partial}{\partial z} \\ v_{x} &v_{y} &v_{z}\end{vmatrix}$$
- Geometricamente, o rotacional de uma função num certo ponto mede o quanto a função "gira" em torno do ponto. 

## 2.3-Regras de Operações de Derivadas
- Algumas do segundário:
$$\begin{align*}
\frac{d}{dx}(f+g)&=\frac{df}{dx}+\frac{dg}{dx}\\
\frac{d}{dx}(kf)&=k\frac{df}{dx}\\
\frac{d}{dx}(fg)&=f\frac{dg}{dx}+g\frac{df}{dx}\\
\frac{d}{dx}\left(\frac{f}{g}\right)&=\frac{g\frac{df}{dx}-f\frac{dg}{dx}}{g^{2}}
\end{align*}$$
- Estas regras também se verificam com gradientes: 
$$\begin{align*}
\nabla(f+g)&=\nabla f+\nabla g\\
\nabla(kf)&=k \nabla f\\
\end{align*}$$
Estas 2 são iguais para divergência e rotacional
- Temos ainda 6 regras do produto:
$$\begin{align*}
\textsf{(gradientes)}\\
\nabla(fg)&=f \nabla g+g \nabla f\\
\nabla(\mathbf{A}\cdot \mathbf{B})&=\mathbf{A}\times(\nabla \times \mathbf{B})+\mathbf{B}\times(\nabla \times \mathbf{A})+(\mathbf{A}\cdot \nabla)\mathbf{B}+(\mathbf{B}\cdot \nabla)\mathbf{A}\\
\textsf{(divergentes)}\\
\nabla \cdot(f \mathbf{A})&=f(\nabla \cdot \mathbf{A})+\mathbf{A}\cdot(\nabla f)\\
\nabla \cdot(\mathbf{A}\times \mathbf{B})&=\mathbf{B}\cdot(\nabla \times \mathbf{A})-\mathbf{A}\cdot(\nabla \times \mathbf{B})\\
\textsf{(rotacionais)}\\
\nabla \times (f \mathbf{A})&=f(\nabla \times \mathbf{A})-\mathbf{A}\times(\nabla f)\\
\nabla \times (\mathbf{A}\times \mathbf{B})&=(\mathbf{B}\cdot \nabla)\mathbf{A}-(\mathbf{A}\cdot \nabla)\mathbf{B}+\mathbf{A}(\nabla \cdot\mathbf{B})-\mathbf{}{B}(\nabla \cdot\mathbf{A})
\end{align*}$$
(Para as provar, basta substituir os vetores e o nabla num produto normal de vetores e usar as regras do secundário)

- Temos ainda, para divisões:
$$\small\begin{align*}
\nabla \left(\frac{f}{g}\right)&=\frac{g \nabla f-f \nabla g}{g^{2}}\\
\nabla \cdot \left(\frac{\mathbf{A}}{g}\right)&=\frac{g(\nabla \cdot \mathbf{A})-\mathbf{A}\cdot(\nabla g)}{g^{2}}\\
\nabla \times \left(\frac{\mathbf{A}}{g}\right)&=\frac{g(\nabla \times \mathbf{A})+\mathbf{A}\times(\nabla g)}{g^{2}}
\end{align*}$$

## 2.4 - Segundas Derivadas
- Ao aplicar nabla 1 vez temos: gradiente, divergência e rotacional.
- Ao aplicar nabla 2 vezes temos:
    - _Divergente de gradiente_: $\nabla \cdot(\nabla T)$
        - Que é igual a: $$\nabla \cdot(\nabla T)=\frac{\partial^{2}T}{\partial x^{2}}+\frac{\partial^{2}T}{\partial y^{2}}+\frac{\partial^{2}T}{\partial z^{2}}=\nabla^{2}T$$
        - Daqui obtemos o **Laplaciano**: $$\nabla^{2}=\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}=\nabla \cdot \nabla$$
        
        - De notar que o _laplaciano de um vetor_ é $\nabla^{2}\mathbf{v}=(\nabla^{2}v_{x})\hat{x}+(\nabla^{2}v_{y})\hat{y}+(\nabla^{2}v_{z})\hat{z}$ 

    - _Rotacional de gradiente:_ $\nabla \times(\nabla T) = 0$
    - _Gradiente de divergência_: $\nabla(\nabla \cdot \vec{v})$
        - Note-se que _não_ é igual ao laplaciano de um vetor: $\nabla^{2}\mathbf{v}=(\nabla \cdot \nabla)\vec{v}\neq \nabla(\nabla \cdot \vec{v})$
    - _Divergente de rotacional_: $\nabla \cdot(\nabla \times \mathbf{v}) = 0$
    - _Rotacional de rotacional_:
        - Facilmente vemos que $$\nabla \times (\nabla \times \mathbf{v})=\nabla(\nabla \cdot \mathbf{v})-\nabla^{2}\mathbf{v}$$

- Em conclusão, todo o cálculo diferencial gira à volta do nabla e do seu comportamento como um vetor. A partir da sua definição podemos deduzir tudo o que tem acima.

# 3 - Cálculo Integral
## 3.1 - Integrais de Linha, Superfície e Volume
### Integrais de Linha
$$\int_{a}^{b}\mathbf{v}\cdot d \mathbf{l}$$
- Esta é a integral de linha do campo vetorial $\vec{v}$ ao longo de um percurso $\mathcal{P}$, de $a$ para $b$. Se o percurso for fechado ($a=b$), então representamos a integral como $$\oint \mathbf{v}\cdot d \mathbf{l}$$
- Um exemplo comum na física deste tipo de integral é o trabalho realizado por uma força ao longo de um percurso.
- _Apenas_ se o campo vetorial for **conservativo**, a integral de linha não depende do percurso.

### Integrais de Superfície
$$\int_{\mathcal{S}}\mathbf{v}\cdot d \mathbf{a} \quad \quad \left(\oint \mathbf{v}\cdot d \mathbf{a}\quad \textsf{se a superfície for fechada}\right)$$
- Aqui, $d \mathbf{a}$ corresponde a um elemento infinitesimal de área e tem direção perpendicular à superfície. Se a superfície for fechada, considerasse que tem sentido positivo de dentro para fora da superfície. Para superfícies abertas, a direção é arbitrária.
- Se o campo vetorial representar a circulação de um fluido (unidade por área por tempo) então a integral de superfície dá o fluxo do fluido através da superfície.

### Integrais de Volume
$$\int_{\mathcal{V}}T d \tau$$
- Em que $T$ é uma função escalar e $d \tau=dxdydz$ é um elemento infinitesimal de volume.
- Uma integral de volume para um campo vetorial será do tipo:
$$\int \mathbf{v}d \tau=\hat{x}\int v_{x}d \tau+\hat{y}\int v_{y}d \tau+\hat{z}\int v_{z}d \tau$$

## 3.2 - Teorema Fundamental do Cálculo
$$\int_{a}^{b}F(x)dx=f(b)-f(a)=\int_{a}^{b}\left(\frac{df}{dx}\right)dx$$
- Do ponto de vista isto significa que para obter a a integral de uma função de $x=a$ até $x=b$ podemos 
    - Ir somando $F(x), ~x\in[a,b]$, para pequenos incrementos de $x$
    - Subtrair $f(b)-f(a)$
E vão dar o mesmo.

## 3.3 - Teorema Fundamental do Gradiente
- Vimos acima (secção 2.1) que se nos movermos segundo um vetor $d \vec{\ell}_{1}$, então a variação de $T$ será $\large dT=(\nabla T)\cdot d \vec{\ell}_{1}$ . Se movermos $d \vec{\ell}_{2}$. Assim podemos entender que 
  $$\int_{\mathbf{a}}^{\mathbf{b}}(\nabla T)\cdot d \mathbf{l}=T(\mathbf{b})-T(\mathbf{a})$$
- Geometricamente, isto é o equivalente a dizer que: subir a torre eifel pelas escadas e ir medindo a elevação de cada degrau e depois somar tudo vai dar o mesmo que meter um altimetro no topo e na base e fazer a diferença vai dar o mesmo.
- Como vimos antes, integrais de linha _normalmente_ dependem do percurso. Ora, integrais de linha de gradientes não dependem. 
- Tem-se ainda que, se tivermos o integral de linha de um gradiente, num *intervalo fechado*, este vai dar **zero**.

## 3.4 - Teorema Fundamental do Divergente (Gauss / Green)
$$\int_{\mathcal{V}}(\nabla \cdot \mathbf{v})d \tau=\oint_{\mathcal{S}}\mathbf{v} \cdot d \mathbf{a}$$
em que $\mathcal{V}$ é o volume delimitado por $\mathcal{S}$.
- Se $\mathbf{v}$ representa a circulação de um fluido então o seu fluxo será dado pela parte da direta da equação. Ora, podemos ver a integral da esquerda como algo que nos dá o número de torneiras que há dentro do volume.
- Assim, podemos determinar a quantidade de fluido que está a ser produzido de 2 formas: contar o número de torneiras dentro dele OU determinar o fluxo na superfície limitante do fluido.

## 3.5 - Teorema Fundamental do Rotacional (Stokes)
$$\int_{\mathcal{S}}(\nabla \times \mathbf{v})\cdot d \mathbf{a}=\oint_{\mathcal{P}}\mathbf{v} \cdot d \mathbf{l}$$
em que $\mathcal{S}$ é a área delimitada por $\mathcal{P}$.
- Para superfícies $\mathcal{S}$ fechadas, $d \mathbf{a}$ aponta _para fora_. Mas neste caso o integral é **zero**, porque não há uma linha que delimite a superfície.
- Para superfícies $\mathcal{S}$ abertas, $d \mathbf{a}$ tem a direção dada pela regra da mão direita (Fechamos a mão com o polegar extendido (tipo 👍) na direção da integral de linha. $d \mathbf{a}$ vai ser perpendicular à superfície e com a direção que o polegar apontar)
- Temos neste teorema que a integral do rotacional depende apenas da linha que limita a superfície, e não da superfície em si.

## 3.6 - Integração por Partes
**Normal**
- A regra do produto é descrita por: $$\frac{d}{dx}(fg)=f \left( \frac{dg}{dx}\right) + g \left( \frac{df}{dx}\right)$$
- Se integrarmos os dois lados temos:
$$fg \biggr|_{a}^{b} = \int_{a}^{b}f\left(\frac{dg}{dx}\right) dx + \int_{a}^{b} g \left(\frac{df}{dx}\right)dx$$
se reorganizarmos os termos ficamos com:
$$\int_{a}^{b}f \left(\frac{dg}{dx}\right)dx=-\int_{a}^{b}g\left(\frac{df}{dx}\right)dx+ fg\biggr|_{a}^{b}$$
que é a integração por partes que conhecemos: $\int x~dy=xy - \int y~dx$ 

**Com Divergente**
- De forma semelhante, se tivermos $$\nabla \cdot (f \mathbf{A})=f(\nabla \cdot \mathbf{A})+\mathbf{A}\cdot(\nabla f)$$
- Se integrarmos isto num certo volume e usarmos o teorema do divergente ficamos com:
$$\int_\mathcal{V} f(\nabla \cdot \mathbf{A})d \tau=-\int_\mathcal{V} \mathbf{A}\cdot (\nabla f)d \tau + \oint_\mathcal{S} f \mathbf{A}\cdot d \mathbf{a}$$
ou seja, tal como acima, temos o produto entre uma função e a derivada de outra (neste caso o divergente). Vemos que o lado direito apresenta uma forma idêntica.

# 4 - Coordenadas Curvilíneas
## 4.1 - Coordenadas Esféricas
- Normalmente identificamos um ponto com coordenadas cartesianas: $(x,y,z)$. Mas por vezes pode ser mais prático usar coordenadas esféricias: $(r, \theta, \phi)$ em que:
    - $r$ é a *distância à origem* do referencial.
    - $\theta$ é o ângulo *polar* - entre o ponto e o eixo $z$, de cima para baixo.
    - $\phi$ é o ângulo *azimutal* - entre a projeção do ponto no plano $xOy$ e o eixo dos $x$, no sentido anti-horário.
![[coords esféricas.png]]

- Pela imagem acima, podemos ver que é possível escrever:
$$x=r\sin\theta\cos\phi ~~~~;~~~~ y = r\sin\theta\sin\phi~~~~;~~~~ z=r\cos\theta$$
Podemos então escrever: $\mathbf{A}=A_{r}\hat{r}+A_{\theta}\hat{\theta}+A_{\phi}\hat{\phi}$
- Podemos então obter:
$$\begin{cases}
\hat{r}= \sin\theta\cos\phi~\hat{x} + \sin\theta\sin\phi~\hat{y} + \cos\theta~\hat{z} \\
\hat{\theta}=\cos\theta\cos\phi~\hat{x} + \cos\theta\sin\phi~\hat{y} - \sin\theta~\hat{z} \\
\hat{\phi}= -\sin\phi~\hat{x} + \cos\phi~\hat{y}
\end{cases}$$
de recordar, claro, que, contrariamente a $\hat{x},\hat{y},\hat{z}$, os versores $\hat{r},\hat{\theta},\hat{\phi}$ variam em cada ponto. Como tal, eles dependem *sempre* de $\theta$ e $\phi$.
- Como tal, 
    - Não podemos somar pontos da mesma forma (Tendo $\mathbf{A}=\hat{y},\mathbf{B}=-\hat{y}$, ambos são $\hat{r}$, mas $\mathbf{A}+\mathbf{B}=\vec{0}$, não $2 \hat{r}$)
    - Não podemos colocá-los em evidência em derivadas e integrais.

![[coords esféricas - explicacao.png]]
- Conforme a imagem acima, um deslocamento infinitesimal na direção radial é apenas $$d l_{r}=dr$$
- Um deslocamento na direção polar será a "projeção" de uma pequena variação do ângulo: $$dl_{\theta}=r~d\theta$$
- De forma semelhante, na direção azimutal temos: $$dl_{\phi}= r \sin\theta~d\phi$$
- Ou seja, um deslocamento infinitesimal em coordenadas esféricas é: $$d\mathbf{l}=dr ~\hat{r}+r~d\theta ~\hat{\theta}+r\sin\theta~d\phi ~\hat{\phi}$$
- Desta forma, um volume infinitesimal, da mesma forma que em coordenadas cartesianas, será o produto dos componentes do deslocamento infinitesimal:
$$d\tau = dl_{r} dl_{\theta}dl_{\phi} = r^{2}\sin \theta ~ dr d\theta d\phi$$

- Para saber áreas infinitesimais temos que ver o problema em si. Se tivermos a integrar uma esfera, $r$ será constante, se tivermos a integrar algo no plano $xOy$, $\theta$ será constante.
- De recordar também que $r:0\to\infty~~,~~\theta:0\to\pi~~,~~\phi:0\to2\pi$

### Gradiente, Divergente, Rotacional e Laplaciano
- Vimos atrás que: $$\nabla T=\frac{\partial T}{\partial x}\hat{x}+\frac{\partial T}{\partial y}\hat{y}+\frac{\partial T}{\partial z}\hat{z}$$
ou seja, para passar para coordenadas esféricas basta fazer:
$$\frac{\partial T}{\partial x}=\frac{\partial T}{\partial r}\left(\frac{\partial r}{\partial x}\right) + \frac{\partial T}{\partial \theta}\left(\frac{\partial \theta}{\partial x}\right) + \frac{\partial T}{\partial \phi}\left(\frac{\partial \phi}{\partial x}\right)$$
e podemos usar as relações abaixo para obter as derivadas e obter a derivada parcial de $T$ em x em coordenadas esféricas. 
$$x=r\sin\theta\cos\phi ~~~~;~~~~ y = r\sin\theta\sin\phi~~~~;~~~~ z=r\cos\theta$$
Depois basta juntar os componentes $x,y,z$. Ficamos com:
**Gradiente**
$$\nabla T=\frac{\partial T}{\partial r}\hat{r} + \frac{1}{r} \frac{\partial T}{\partial \theta}\hat{\theta} + \frac{1}{r\sin\theta} \frac{\partial T}{\partial \phi}\hat{\phi}$$
**Divergente**
$$\nabla \cdot \mathbf{v}=\frac{1}{r^{2}} \frac{\partial}{\partial r}(r^{2}v_{r}) + \frac{1}{r\sin\theta} \frac{\partial}{\partial \theta}(\sin\theta v_{\theta}) + \frac{1}{r\sin\theta} \frac{\partial v_{\phi}}{\partial \phi}$$
**Rotacional**
$$\nabla \times \mathbf{v}=\frac{1}{r\sin\theta} \left[ \frac{\partial}{\partial \theta}(\sin\theta v_{\phi})- \frac{\partial v_{\theta}}{\partial \phi} \right]\hat{r} + \frac{1}{r} \left[ \frac{1}{\sin\theta} \frac{\partial v_{r}}{\partial \phi} - \frac{\partial}{\partial r}(r v_{\phi}) \right]\hat{\theta} + \frac{1}{r} \left[ \frac{\partial}{\partial r}(r v_{\theta}) - \frac{\partial v_{r}}{\partial \theta} \right]\hat{\phi}$$
Podemos escrever assim:
$$\large\nabla \times \mathbf{v}= \frac{1}{r^{2}\sin\theta} \begin{vmatrix} \hat{r} & r ~\hat{\theta} & r\sin \theta ~\hat{\phi}  \\ \frac{\partial}{\partial r} & \frac{\partial}{\partial \theta} & \frac{\partial}{\partial \phi} \\ v_{r} & r~v_{\theta}& r\sin \theta v_\phi\end{vmatrix}$$

**Laplaciano**
$$\nabla^{2}T= \frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r^{2} \frac{\partial T}{\partial r}\right) + \frac{1}{r^{2}\sin\theta} \frac{\partial}{\partial \theta}\left(\sin\theta \frac{\partial T}{\partial \theta}\right) + \frac{1}{r^{2}\sin^{2}\theta} \frac{\partial^{2}T}{\partial \phi^{2}}$$

## 4.2 - Coordenadas Cilíndricas
![[coords cilíndricas.png]]
- As coordenadas cilíndricas podem ser definidas por $(s, \phi, z)$
- Tal como fizemos nas esféricas, podemos escrever: $$x = s\cos \phi~~~~;~~~~ y=s\sin \phi ~~~~;~~~~ z=z $$
- Num exercício do livro determinamos que os vetores unitários são:
$$\begin{cases}
\hat{s} = \cos\phi~\hat{x} + \sin\phi~\hat{y} \\
\hat{\phi} = -\sin\phi~\hat{x} + \cos\phi~\hat{y} \\
\hat{z} = \hat{z} 
\end{cases}$$
- Facilmente se vê que os deslocamentos infinitesimais nas componentes destas coordenadas são: $dl_{s}=ds~~,~~ dl_{\phi}=s~d\phi~~,~~dl_{z}=dz$. Ora, isto dá-nos o vetor de *deslocamento infinitesimal*:
$$d\mathbf{l}=ds~\hat{s} + s~d\phi~\hat{\phi} + dz~\hat{z}$$
em que temos: $s:0\to\infty~~,~~\phi:0\to2\pi~~,~~z:-\infty\to\infty$

**Gradiente**
$$\nabla T=\frac{\partial T}{\partial s}\hat{s} + \frac{1}{s} \frac{\partial T}{\partial \phi}\hat{\phi} + \frac{\partial T}{\partial z}\hat{z}$$
**Divergente**
$$\nabla \cdot \mathbf{v}=\frac{1}{s} \frac{\partial}{\partial s}(s v_{s}) + \frac{1}{s} \frac{\partial v_{\phi}}{\partial \phi} + \frac{\partial v_{z}}{\partial z}$$
**Rotacional**
$$\nabla \times \mathbf{v}= \left( \frac{1}{s} \frac{\partial v_{z}}{\partial \phi} - \frac{\partial v_\phi}{\partial z} \right)\hat{s} + \left( \frac{\partial v_{s}}{\partial z} - \frac{\partial v_{z}}{\partial s} \right)\hat{\phi} + \frac{1}{s}\left[ \frac{\partial}{\partial s}(s v_{\phi}) - \frac{\partial v_{s}}{\partial \phi} \right] \hat{z}$$
Podemos escrever assim:
$$\large\nabla \times \mathbf{v}= \begin{vmatrix} \frac{\hat{s}}{s} & \hat{\phi} & \frac{\hat{z}}{s}  \\ \frac{\partial}{\partial r} & \frac{\partial}{\partial \phi} & \frac{\partial}{\partial z} \\ v_{s} & s~v_{\phi}&  v_{z}\end{vmatrix}$$
**Laplaciano**
$$\nabla^{2}T= \frac{1}{s} \frac{\partial}{\partial s}\left(s \frac{\partial T}{\partial s}\right) + \frac{1}{s^{2}} \frac{\partial^{2}T}{\partial\phi^{2}} + \frac{\partial^{2}T}{\partial z^{2}}$$

# 5 - Delta de Dirac
## 5.1 - Divergente de $\frac{1}{r^{2}} \hat{r}$
- Consideremos a função vetorial: $\large\mathbf{v} = \frac{1}{r^{2}} \hat{r}$
- Todos os pontos desta função aponta para longe da origem em todos os pontos. Ora, seria de esperar que o seu divergente fosse positivo. No entanto, se o calcularmos temos *zero*:
$$\nabla \cdot \mathbf{v}=\frac{1}{r^{2}} \frac{\partial}{\partial r} \left(r^{2} \frac{1}{r^{2}}\right)=0$$
- Isto torna-se mais estranho se usarmos esta função com o teorema do divergente. Consideremos que queremos integrar $\mathbf{v}$ numa esfera de raio $R$. Ora, a parte do teorema com área fica:
$$\oint \mathbf{v} \cdot d \mathbf{a}=\int \left( \frac{1}{R^{2}}\hat{r} \right)\cdot (R^{2}\sin \theta ~d\theta d\phi~\hat{r})=\int_{0}^{\pi}\sin\theta~d\theta \int_{0}^{2\pi}d\phi = 4\pi$$
mas o lado com a integral de volume dá $$\int_\mathcal{V} (\nabla \cdot \mathbf{v})d\tau = \int_\mathcal{V}0 ~d\tau = 0$$
- Mas porquê que o teorema não funcionou? Por causa do ponto $r=0$, em que $\mathbf{v}$ tende para infinito. Vemos assim que a integral de superfície, que não depende do raio, está correta. Por outro lado, o divergente de $\mathbf{v}$ que determinamos está errado. Ele será 0 em todos os pontos, *exceto em* $r=0$.

- Assim, vemos que o divergente desta função anula-se em todos os pontos do espaço *menos 1*. Isto é então a **funçao Delta de Dirac**.

## 5.2 - Função Delta Dirac 1-D
- Pode ser definida com:
$$\delta(x)=\begin{cases}
0 &, &x\neq0  \\ \infty & , & x=0
\end{cases}$$
sendo que:
$$\int_{-\infty}^{+\infty}\delta(x)dx=1$$

- Matematicamente, a função delta de Dirac não é mesmo uma função, porque $\delta(x=0)$ não é um número finito. É, na realidade, uma "função generalizada" / "distribuição". Por exemplo, podemos considerar que o delta de dirac é o limite de uma sequência de funções retangulares, com altura $n$ e base $1/n$.

- Vejamos agora uma consequência importante desta função. Se tivermos uma função "normal" contínua, $f(x)$ temos que o seu produto com o delta de dirac irá anular-se em todos os pontos menos em $x=0$. Ou seja: 
  $$f(x) \delta(x)=f(0) \delta(x) \longrightarrow \int_{-\infty}^{+\infty} f(x)\delta(x)dx=f(0) \int_{-\infty}^{+\infty}\delta(x)dx=f(0)\cdot 1=f(0)$$

- No entanto, se fizermos $\delta(x-a)$, temos que a função é "deslizada" $a$ para a direita. Ou seja, a funnção passa a ser nula em todos os pontos menos $x=a$, ou seja:
$$\delta(x-a)=\begin{cases}0 & , & x\ne a\\ \infty  & , & x=a\end{cases}$$
e temos:
$$\int_{-\infty}^{+\infty}~f(x)\delta(x-a)dx=f(a)$$
ou seja, é como se a função delta de Dirac *escolhesse o valor da função* no ponto do seu pico.

## 5.3 - Função Delta Dirac 3-D
- Definida por
$$\delta^{3}(\mathbf{r})=\delta(x)\delta(y)\delta(z)$$
em que $\mathbf{r}=x \hat{x}+y \hat{y} + z \hat{z}$.
- À semelhança de em 1 dimensão, temos:
$$\int_\text{todo o espaço} \delta^{3}(\mathbf{r})d \tau=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty} \delta(x)\delta(y)\delta(z)~dxdydz=1$$
e ainda:
$$\int_\text{todo o espaço} f(\mathbf{r})\delta^{3}(\mathbf{r}- \mathbf{a})d\tau=f(\mathbf{a})$$

#### Problema Acima - Divergente de $\frac{1}{r^{2}}\hat{r}$
- Como vimos acima, este divergente anula-se em todos os pontos do espaço menos em $r=0$, a origem. Assim, pelo Teorema do Divergente, vimos que o termo da integral de superfície dá $4\pi$. Assim, temos:
$$\nabla \cdot \left(\frac{\hat{r}}{r^{2}}\right)=4\pi \delta^{3}(\mathbf{r})$$
Generalizando temos:
$$\nabla \cdot \left(\frac{\hat{\mathbb{r}}}{\mathbb{r}^{2}}\right) = 4\pi \delta^{3} (\vec{\mathbb{r}})$$
em que $\mathbb{r}\equiv \mathbf{r}-\mathbf{r}'$ é o vetor separação. De notar aqui que estamos a derivar em função a $\mathbf{r}$, com $\mathbf{r}'$ constante.
Assim:
$$\nabla \left(\frac{1}{\mathbb{r}}\right)=- \frac{\hat{\mathbb{r}}}{\mathbb{r}^{2}}\longrightarrow \nabla^{2} \frac{1}{\mathbb{r}} = -4\pi \delta^{3}(\vec{\mathbb{r}})$$

# 6 - Teoria de Campos Vetoriais
## 6.1 - Teorema de Helmholtz
- Em eletromagnetismo, os campos elétrico e magnético ($\mathbf{E},\mathbf{B}$) são definidos por vetores, ou seja, funções vetoriais. Além disso, as equações de Maxwell determinam o valor do divergente e rotacional destes 2 campos.
- Assim, é valido perguntar: 
    - Sendo $F$ uma função vetorial (que pode ser $\mathbf{E}$ ou $\mathbf{B}$) e conhecendo o escalar $D$ e a função vetorial $\mathbf{C}$, tais que:
$$\nabla \cdot \mathbf{F}=D ~~~~;~~~~ \nabla \times \mathbf{F}=\mathbf{C} ~~~~(\nabla \cdot \mathbf{C}=0)$$
    conseguimos determinar $\mathbf{F}$ com estes dados?

- A resposta é: nem por isso.
- Em exercícios do livro vemos que várias funções vetoriais têm divergente e rotacional nula em todo o espaço.
- Além disso, precisamos de conhecer as *condições de fronteira*
- De seguida veremos os teoremas que nos permitem determinar $\mathbf{F}$.

## 6.2 - Potenciais
- Se o rotacional de um campo/função vetorial, $\mathbf{F}$, é sempre nulo podemos escrever $\mathbf{F}$ como sendo o gradiente de um *potencial escalar*, $V$:
$$\nabla \times \mathbf{F}=\vec{0} \longrightarrow \mathbf{F}=-\nabla V$$
(o sinal negativo é convenção) (De notar que este potencial não será único. Podemos acrescentar qualquer constante e o seu gradiente será o mesmo.)

>**_TEOREMA 1 - Campos Irrotacionais / de Rotacional Nulo_**
>Se um campo vetorial, $\mathbf{F}$, cumpre uma, cumpre todas as condições abaixo:
>- $\nabla \times \mathbf{F}=0$ em todo o espaço
>- $\int_{a}^{b} \mathbf{F}\cdot d \mathbf{l}$ não depende do percurso, apenas dos pontos inicial e final
>- $\oint \mathbf{F} \cdot d \mathbf{l}=0$ para qualquer percurso fechado
>- $\mathbf{F}$ pode ser escrito como o gradiente de uma função escalar: $\mathbf{F}=-\nabla V$


- Por outro lado, se um campo vetorial, $\mathbf{F}$, tem um divergente sempre nulo então podemos escrevê-lo como o rotacional de um *vetor potencial* $\mathbf{A}$:
$$\nabla \cdot \mathbf{F}=0 \longrightarrow \mathbf{F}= \nabla \times \mathbf{A}$$
(Novamente, o campo vetorial $\mathbf{A}$ não é único. Podemos acrescentar o gradiente de qualquer função escalar e o rotacional não é afetado.)

>**_TEOREMA 2 - Campos Solenoidais / de Divergente Nulo_**
>Se um campo vetorial, $\mathbf{F}$, cumpre uma, cumpre todas as condições abaixo:
>- $\nabla \cdot \mathbf{F}=0$ em todo o espaço
>- $\int \mathbf{F}\cdot d \mathbf{a}$ não depende da superfície, apenas da linha que a limita
>- $\oint \mathbf{F} \cdot d \mathbf{a}=0$ para qualquer superfície fechado
>- $\mathbf{F}$ pode ser escrito como o rotacional de uma função vetorial: $\mathbf{F}=\nabla \times \mathbf{A}$

- Ou seja, temos o ***teorema de Helmholtz***:
> Qualquer campo/função vetorial pode ser escrito na forma: $$\mathbf{F}=-\nabla V + \nabla \times \mathbf{A}$$
