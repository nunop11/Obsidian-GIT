### 1. Transformações - derivadas de função
Tendo-se $y'$ o resultado de $y$ após uma transformação, tal que: $$y' = ay + bz$$
se tivermos:
$$\frac{\partial f}{\partial y'}$$
podemos escrever como:
$$\frac{\partial f}{\partial y'}=\frac{\partial f}{\partial y}\frac{\partial y}{\partial y'} + \frac{\partial f}{\partial z}\frac{\partial z}{\partial y'}$$
sendo que é preciso ter $y(y',z')~~,~~ z(y',z')$.
- VER *EX 1.14*

### 2. - Transformações - divergente
Ao fazer o divergente de algo transformado (por exemplo $y'$ ser o resultado de $y$ após uma transformação) temos que fazer aquilo que está acima, para reconverter $y'$ em $y$, mas as funções também são transformadas. Ou seja, sendo $v=(f(y,z),g(y,z)$:
$$\nabla \cdot v = \frac{\partial f}{\partial y} + \frac{\partial g}{\partial z}$$
após a transformação:
$$\nabla \cdot v \longrightarrow \nabla \cdot v' = \frac{\partial f'}{\partial y'}+\frac{\partial g'}{\partial z'}$$
em que, se $y'=ay+bz$ então (não sei bem como é que isto funciona!!!!!): $$f'=af+bg$$
- Sendo que a seguir a isto ainda é preciso fazer a conversão no ponto 1. deste documento para ficar com derivadas de $y$, não de $y'$
- VER *EX 1.17*

### 3. NABLA É UM OPERADOR
- Ou seja: $$\mathbf{A}\cdot \nabla \neq \nabla \cdot \mathbf{A}$$
o segundo é o divergente de $\mathbf{A}$. O primeiro seria usado assim:
$$(\mathbf{A}\cdot \nabla)\mathbf{B}= (\mathbf{A}\cdot (\nabla B_{x}), \mathbf{A}\cdot (\nabla B_{y}), \mathbf{A}\cdot (\nabla B_{z}))$$

### 4. INTEGRAIS DE LINHA
![[integral de linha.png]]
- Consideremos acima, o integral de linha $(i)$. Mais concretamente, o vetor $d\mathbf{l}_{i}$. Ele será: $$d \mathbf{l}_{i} =(0,dy,0)$$
Ora, terá elementos não nulos nas direções em que o aponta, em que pomos o elemento infinitesimal dessa posição ($dx$ na direção dos $x$, $dy$ na direção $y$, ...). No entanto, de notar que ele é *SEMPRE POSITIVO*.
- Por exemplo na secção $(iii)$ teríamos:
$$d\mathbf{l}_{iii}=(0,dy,0)$$
e depois: $$\int_{1}^{0} (\mathbf{v}\cdot d\mathbf{l}_{iii})_{y} ~dy$$

### 5. INTEGRAIS DE SUPERFÍCIE
![[integral de linha.png]]
- Voltando ao exemplo acima, mas agora o integral de superfície que podemos fazer.
- Antes de mais, notar que a direção do vetor será indicada pela *regra da mão direita* - mais especificamente, a versão em que fechamos os dedos na direção que o percurso indica (anti-horário na imagem acima) e o polegar dá-nos a direção de $d \mathbf{a}$. Neste caso: $$d \mathbf{a}=(dy~dz,0,0)$$
Este já *pode ser negativo* (podemos ter tipo $d \mathbf{a}=(0,-dxdz,0)$). 
Neste caso, nos elementos das direções em que aponta temos os elementos infinitesimais que *não* são essa direção vetorial. Ou seja: $$\begin{align*}
d \mathbf{a} \parallel \hat{x} \to d \mathbf{a}=(dydz,0,0)\\
d \mathbf{a} \parallel \hat{y} \to d \mathbf{a}=(0,dxdz,0)\\
d \mathbf{a} \parallel \hat{z} \to d \mathbf{a}=(0,0,dxdy)
\end{align*}$$
- Vejamos agora integrais de superfície em coordenadas cilíndricas. Temos:
$$\begin{align*}
d \mathbf{a} \parallel \hat{r} \to d \mathbf{a}&= (r^{2}\sin \theta ~ d \theta d \phi,0,0)\\
d \mathbf{a} \parallel \hat{\theta} \to d \mathbf{a}&= (0,r\sin \theta~dr d \phi,0)\\
d \mathbf{a} \parallel \hat{\phi} \to d \mathbf{a}&= (0,0,r ~dr d \theta)
\end{align*}$$

### 6. COORDENADAS ESFÉRICAS
#### 6.1 - Deduzir
- Nota de como compreender e de como obter $x,y,z$ em função de $r,\theta, \phi$
    1. Temos um ponto $\mathbf{r}=(r,\theta,\phi)$
    2. As coordenadas do ponto em $(x,y,z)$ não passam dos valores da projeção do seu vetor nos eixos
    3. $r\cos \theta$ é a projeção de $\mathbf{r}$ no eixo dos $z$ devido à forma como o ângulo $\theta$ é definido. Assim: $z = r\cos \theta$
    4. Alternativamente, $r\sin \theta$ será a projeção de $\mathbf{r}$ no plano $xOy$. Assim: $x=r \sin \theta \cos \theta$ é a projeção de $\mathbf{r}$ no eixo dos $x$ e $y=r \sin \theta\sin \phi$ no eixo dos $y$.

#### 6.2 - Converter
- Temos que: $$\mathbf{r}=(x,y,z)=(r\sin\theta\cos\phi, r\sin\theta\sin\phi,r\cos\theta)$$
ora:
$$\vec{\theta}=\frac{d\mathbf{r}}{d\theta}~~~~;~~~~ \vec{\phi}=\frac{d\mathbf{r}}{d\phi}$$

