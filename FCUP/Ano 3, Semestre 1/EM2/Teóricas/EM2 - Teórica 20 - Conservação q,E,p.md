# Leis de Conservação
## Conservação de Energia
### Equação de Continuidade
- O que é "conservação de carga"?
    - A uma escala *global*, simplesmente significa que a carga total do universo não muda. 
    - A uma escala *local* isto significa que se a carga presente numa região do espaço muda, então essa variação é exatamente a carga que entrou ou saiu da região pela sua superfície.

- A carga numa região $\mathcal{V}$ é:
$$Q(t)=\int_\mathcal{V} \rho(\vec{r},t)d^{3}r$$
e a variação de carga será portanto o *fluxo* de carga pela superfície. Ou seja:
$$\frac{dQ}{dt}=-\oint_\mathcal{S} \vec{\mathcal{J}}\cdot d \vec{\ell}$$
usando a equação de $Q(t)$ acima e o teorema de Gauss:
$$\int_\mathcal{V}\frac{\partial \rho}{\partial t}d^{3}r=-\int_\mathcal{V} \nabla \cdot \vec{\mathcal{J}}~d^{3}r$$
de onde resulta a **Equação da Continuidade de Carga**:
$$\boxed{\frac{\partial \rho}{\partial t}=-\nabla \cdot \vec{\mathcal{J}}}$$

### Teorema de Poynting
- Em aulas anteriores determinamos que o trabalho necessário para "montar" um sistema eletrostático é:
$$W_{e}=\varepsilon_{0}\int E^{2}~d^{3}r$$
e o trabalho necessário para fazer com que uma corrente começar a andar é $$W_{m}=\frac{1}{2\mu_{0}}\int B^{2}~d^{3}r$$
- E parece natural presumir então que a energia total por unidade de volume num campo EM será:
$$u=\frac{1}{2}\left(\varepsilon_{0}E^{2}+ \frac{1}{\mu_{0}}B^{2} \right)$$

- Consideremos que temos um sistemas de cargas e correntes, que criam campos $\vec{E}$ e $\vec{B}$. Passa um intervalo de tempo $dt$, pelo que as cargas se movem. Qual será o trabalho que as forças EM exercem nas cargas?
- A forças de Lorentz para uma carga $q$ será $\vec{F}=q(\vec{E}+\vec{v}\times\vec{B})$. O trabalho exercido numa carga $q$ será:
$$\vec{F}\cdot d \vec{\ell}=q(\vec{E}+\vec{v}\times\vec{B})\cdot \vec{v}~dt=q \vec{E}\cdot\vec{v}~dt$$
e portanto, o trabalho por unidade de tempo será:
$$\frac{dW}{dt}=q \vec{E}\cdot\vec{v}$$
- Se considerarmos um sistema contínuo, a carga $q$ é escrita como $\rho d^{3}r$ e fica:
$$\frac{dW}{dt}=\rho \vec{E}\cdot \vec{v} ~d^{3}r=\int_\mathcal{V}(\vec{E}\cdot \vec{\mathcal{J}})d^{3}r$$
e obviamente o trabalho por unidade de tempo e por unidade de volume é $\vec{E}\cdot \vec{\mathcal{J}}$. Podemos chamar ainda a isto a Potência por volume.
- Podemos escrever isto de outra forma:
$$\begin{align*}
\vec{\mathcal{J}}\cdot \vec{E}&= \left(\frac{\nabla\times\vec{B}}{\mu_{0}}- \varepsilon_{0} \frac{\partial \vec{E}}{\partial t} \right) \cdot \vec{E}\\
&= \frac{1}{\mu_{0}} \vec{E}\cdot \nabla \times \vec{B} - \frac{\varepsilon_{0}}{2}\frac{\partial E^{2}}{\partial t}\\
\end{align*}$$
usemos a relação $\nabla \cdot(\vec{E}\times \vec{B})=\vec{B}\cdot(\nabla \times \vec{E})-\vec{E}\cdot(\nabla \times \vec{B})$:
$$\begin{align*}
\vec{\mathcal{J}}\cdot\vec{E}&= - \frac{1}{\mu_{0}}\nabla \cdot (\vec{E}\times\vec{B}) + \frac{1}{\mu_{0}}\vec{B}\cdot (\nabla \times \vec{E}) - \frac{\varepsilon_{0}}{2} \frac{\partial E^{2}}{\partial t}\\
&= - \frac{1}{\mu_{0}}\nabla \cdot (\vec{E}\times\vec{B}) + \frac{1}{\mu_{0}}\vec{B}\cdot \left(- \frac{\partial\vec{B}}{\partial t} \right) - \frac{\varepsilon_{0}}{2} \frac{\partial E^{2}}{\partial t}\\
&= - \frac{1}{\mu_{0}}\nabla \cdot (\vec{E}\times\vec{B}) - \frac{1}{2\mu_{0}}\frac{\partial B^{2}}{\partial t} - \frac{\varepsilon_{0}}{2} \frac{\partial E^{2}}{\partial t}\\
&= - \frac{1}{\mu_{0}}\nabla \cdot (\vec{E}\times\vec{B}) - \frac{\partial u}{\partial t}\\
&= - \nabla \cdot \vec{S} - \frac{\partial u}{\partial t}
\end{align*}$$
em que definimos o **_Vetor Poynting_**:
$$\vec{S}=\frac{\vec{E}\times\vec{B}}{\mu_{0}}$$
(por alguma razão o Avelino escreve o vetor Poynting com $\vec{N}$. Estou a usar a notação do Griffiths)

- A variação de trabalho no tempo fica portanto o **Teorema de Poynting**:
$$\begin{align*}
\frac{dW}{dt}&= - \frac{d}{dt}\int_\mathcal{V}  u~d^{3}r - \frac{1}{\mu_{0}}\int_{\mathcal{V}} \nabla \cdot \vec{S}~d^{3}r\\
&= - \frac{d}{dt}\int_\mathcal{V}  u~d^{3}r - \frac{1}{\mu_{0}}\oint_\mathcal{S} \vec{S}\cdot d \vec{s}
\end{align*}$$
em que o 1º termo representa a variação da energia dentro do volume $\vec{V}$ e o 2º representa a energia que entra e sai através de $\mathcal{S}$. 
- Por outras palavras, este teorema diz-nos que o trabalho realizado pela força EM sobre as cargas corresponde à perda de energia dos campos E,B menos a energia que sai da região.

- E se não for realizado trabalho, ou seja, e se $\vec{\mathcal{J}}=\vec{0}$ AKA não há cargas para realizar trabalho? Ficamos com 
$$\frac{dW}{dt}=0 ~~\longrightarrow~~ \int \frac{\partial u}{\partial t}d^{3}r =-\oint \vec{S}\cdot d \vec{s}$$
e ficamos com
$$\frac{\partial u}{\partial t}=-\nabla \cdot \vec{S}$$
que podemos considerar como sendo a *"Equação de continuidade da energia"*. No entanto, isto normalmente não é o caso. Os campos fazem trabalho nas cargas, que se movem e geram novos campo s por aí adiante. A energia está constante a ser trocada.

#### Meio linear, isotrópico e homogéneo
- Ficamos com:
$$\varepsilon_{0}\to\varepsilon \quad;\quad \mu_{0}\to\mu \quad;\quad \vec{\mathcal{J}}\to\vec{\mathcal{J_{\ell}}} \quad;\quad \rho\to\rho_{\ell}$$
e o vetor Poynting fica:
$$\vec{S}=\frac{\vec{E}\times\vec{B}}{\mu}=\vec{E}\times\vec{H}$$
- E a densidade de energia EM fica:
$$u = \frac{1}{2}\left(\varepsilon E^{2}+ \frac{1}{\mu} B^{2}\right)=\frac{1}{2}(\vec{D}\cdot\vec{E} + \vec{H}\cdot\vec{B})$$ 
## Conservação de Momento Linear
### 3ª Lei de Newton
![[campos de carga em movimento.png]]
- Consideremos uma carga $q$ em movimento na direção $x$. 
    - O campo elétrico que ela cria *não* é descrito pela Lei de Coulomb, mas continua a ser radial.
    - O campo magnético *não* é descrito pela Lei de Biot-Savart mas continua a ser azimutal em relação ao eixo de movimento da carga.
(Ver figura acima)

![[forças geradas por cargas em movimento relativo.png]]
- Consideremos agora que temos uma 2ª carga, a mover-se na direção $y$. Ignoremos o facto que elas iriam imediatamente mudar a sua direção. As forças EM criadas estão acima representadas. Considerou-se que $\vec{B_{1}}(q_{2})$ tem direção $-\hat{z}$ e $\vec{B_{2}}(q_{1})$ tem direção $+\hat{z}$.
- Podemos então ver que a força EM total é igual para as 2 partículas é *igual*, mas **não é oposta** (ambas têm direção $-\hat{z}$). Assim: **Em eletrodinâmica, a 3ª Lei de Newton NÃO SE APLICA**. Em eletrostática e magnetostática sim.
- No entanto, continuamos a ter conservação de momento. Isto acontece porque os campos $E,B$ têm momento!

### Tensor das Tensões Maxwell
- A força por unidade de volume numa região será:
$$\vec{f}=\rho \vec{E}+\vec{J}\times\vec{B}$$
(não confundir com a força por unidade de carga $f$ na parte da força eletromotriz)

- Usando a 1ª e 4ª equações de Maxwell:
$$\begin{align*}
\vec{f}&= (\varepsilon_{0}\nabla \cdot \vec{E})\vec{E} + \left(\frac{\nabla \times \vec{B}}{\mu_{0}} - \varepsilon_{0} \frac{\partial \vec{E}}{\partial t} \right)\times \vec{B}\\
&= \varepsilon_{0}(\nabla \cdot \vec{E})\vec{E} - \frac{1}{\mu_{0}}\vec{B}\times(\nabla\times\vec{B})  - \varepsilon_{0} \frac{\partial \vec{E}}{\partial t}\times\vec{B}
\end{align*}$$
podemos escrever 
$$\begin{align*}
\frac{\partial}{\partial t}(\vec{E}\times\vec{B})&= \frac{\partial\vec{E}}{\partial t}\times \vec{B} + \vec{E}\times \frac{\partial \vec{B}}{\partial t}\\
&= \frac{\partial\vec{E}}{\partial t}\times \vec{B} - \vec{E} \times (\nabla \times \vec{E})\\
\frac{\partial\vec{E}}{\partial t}\times \vec{B} &= \frac{\partial}{\partial t}(\vec{E}\times\vec{B}) + \vec{E} \times (\nabla \times \vec{E})
\end{align*}$$
- Substituindo na equação de $\vec{f}$:
$$\begin{align*}
\vec{f}&= \varepsilon_{0}(\nabla \cdot \vec{E})\vec{E} - \frac{1}{\mu_{0}}\vec{B}\times(\nabla\times\vec{B})  - \varepsilon_{0}\left[\frac{\partial}{\partial t}(\vec{E}\times\vec{B}) + \vec{E} \times (\nabla \times \vec{E})\right]\\
&= \varepsilon_{0} \left[ (\nabla \cdot \vec{E})\vec{E} - \vec{E} \times (\nabla \times \vec{E}) \right] -\frac{1}{\mu_{0}}\vec{B}\times(\nabla\times\vec{B})-\varepsilon_{0} \frac{\partial}{\partial t}(\vec{E}\times\vec{B})
\end{align*}$$
como $\nabla \cdot \vec{B}=0$ nada nos impede de acrescentar um termo $\frac{1}{\mu_{0}}(\nabla \cdot \vec{B})\vec{B}$:
$$\vec{f}=\varepsilon_{0} \left[ (\nabla \cdot \vec{E})\vec{E} - \vec{E} \times (\nabla \times \vec{E}) \right] +\frac{1}{\mu_{0}}\left[(\nabla \cdot \vec{B})\vec{B} -\vec{B}\times(\nabla\times\vec{B}) \right]-\varepsilon_{0} \frac{\partial}{\partial t}(\vec{E}\times\vec{B})$$


- Podemos escrever
$$\nabla(E^{2})= 2(\vec{E}\cdot\nabla)\vec{E} + 2 \vec{E}\times(\nabla\times\vec{E})$$
logo
$$\vec{E}\times(\nabla\times\vec{E})=\frac{1}{2}\nabla(E^{2}) - (\vec{E}\cdot\nabla)\vec{E}$$
e equivalentemente para $\vec{B}$: $\vec{B}\times(\nabla\times\vec{B})=\frac{1}{2}\nabla(B^{2}) - (\vec{B}\cdot\nabla)\vec{B}$.

- Ao substituir na equação de $\vec{f}$ fica:
$$\vec{f}=\varepsilon_{0}\left[(\nabla \cdot \vec{E})\vec{E} - \frac{1}{2}\nabla(E^{2}) + (\vec{E}\cdot\nabla)\vec{E}\right] + \frac{1}{\mu_{0}} \left[(\nabla \cdot \vec{E})\vec{E} - \frac{1}{2}\nabla(E^{2}) + (\vec{E}\cdot\nabla)\vec{E}\right] - \varepsilon_{0}\mu_{0} \frac{\partial\vec{S}}{\partial t}$$

- O **Tensor das Tensões de Maxwell** é definido como:
$$T_{ij} \equiv \varepsilon_{0}\left(E_{i}E_{j} - \frac{1}{2}\delta_{ij} E^{2}\right) + \frac{1}{\mu_{0}}\left(B_{i}B_{j} - \frac{1}{2}\delta_{ij}B^{2} \right)$$
- Devido ao Delta de Kronecker temos termos assim:
$$T_{xx}=\frac{1}{2}\varepsilon_{0}(E_{x}^{2}-E_{y}^{2}-E_{z}^{2}) + \frac{1}{2\mu_{0}}\left(B_{x}^{2}-B_{y}^{2}-B_{Z}^{2} \right)$$
$$T_{xy}=\varepsilon_{0}(E_{x}E_{y}) + \frac{1}{\mu_{0}}(B_{x}B_{y})$$

- Como tem 2 indices, o tensor opera mais ou menos como uma matriz. Temos então 2 produtos escalares possíveis:
$$\left(\vec{a}\cdot \stackrel{\leftrightarrow}{T} \right)_{j}=\sum\limits_{i=x,y,z}a_{i}T_{ij} \quad \quad;\quad \quad \left(\stackrel{\leftrightarrow}{T} \cdot \vec{a}\right)_{j} =\sum\limits_{i=x,y,z}a_{i}T_{ij}$$


- Podemos ainda escrever o elemento $j$ da divergência do tensor:
$$\left(\nabla \cdot \stackrel{\leftrightarrow}{T} \right)_{j}= \varepsilon_{0}\left[(\nabla \cdot \vec{E})\vec{E} + (\vec{E}\cdot\nabla)\vec{E}- \frac{1}{2}\nabla(E^{2}) \right] + \frac{1}{\mu_{0}} \left[(\nabla \cdot \vec{E})\vec{E} + (\vec{E}\cdot\nabla)\vec{E}- \frac{1}{2}\nabla(E^{2}) \right]$$
que é exatamente os primeiros 2 termos da equação de $\vec{f}$ que temos acima.

- A força por unidade de volume é então:
$$\vec{f}=\nabla \cdot \stackrel{\leftrightarrow}{T} - \varepsilon_{0}\mu_{0} \frac{\partial \vec{S}}{\partial t}$$
- A força total aplicada nas cargas na região de volume $\mathcal{V}$ é então:
$$\vec{F}=\oint_\mathcal{S} \stackrel{\leftrightarrow}{T} \cdot d \vec{s} - \varepsilon_{0}\mu_{0} \int_\mathcal{V}\vec{S}~d^{3}r$$
- No caso de um sistema estático temos $\vec{S}=\vec{0}$ e fica:
$$F=\oint_\mathcal{S}\stackrel{\leftrightarrow}{T}\cdot d \vec{s}$$
ou seja, $\stackrel{\leftrightarrow}{T}$ corresponde à força por unidade de área que atua na superfície da região em estudo AKA tensão. Mais especificamente $T_{ij}$ é a força aplicada na direção $i$ num elemento de área com direção $j$

### Conservação de Momento
- Da 2ª Lei de Newton temos:
$$\vec{F}=\frac{d \vec{p_{mec}}}{dt}$$
e da equação de $\vec{F}$ acima temos:
$$\frac{d \vec{p_{mec}}}{dt}= - \varepsilon_{0}\mu_{0} \int_\mathcal{V}\vec{S}~d^{3}r+\oint_\mathcal{S} \stackrel{\leftrightarrow}{T} \cdot d \vec{s}$$
em que $\vec{p_{mec}}$ é o momento mecânico das partículas na região $\mathcal{V}$. Esta é a equação que descreve a **conservação de momento** num sistema EM.
- Facilmente vemos que esta equação tem uma estrutura semelhante à do teorema de Poyting ($\frac{dW}{dt}= - \frac{d}{dt}\int_\mathcal{V}  u~d^{3}r - \frac{1}{\mu_{0}}\oint_\mathcal{S} \vec{S}\cdot d \vec{s}$). Parece portanto correto fazer uma interepretação semelhante.
- O 1ª termo do lado direito representa o momento armazenado nos campos:
$$\vec{p}=\mu_{0}\varepsilon_{0}\int_\mathcal{V}\vec{S}~d^{3}r$$
e o 2ª termo do lado direito é o momento a entrar ou sair do volume pela superfície $\mathcal{S}$.

- Podemos então definir a densidade de momento nos campos:
$$\vec{g}=\mu_{0}\varepsilon_{0}\vec{S}=\varepsilon_{0}(\vec{E}\times\vec{B})$$
e fluxo de momento a passar pelo volume é $-\stackrel{\leftrightarrow}{T}$.

- Se considerarmos que $\mathcal{V}$ é uma região de vácuo, então não temos partículas e não há fluxo de momento mecânico $\vec{p_{mec}}$. Como tal temos:
$$\int \frac{\partial \vec{g}}{\partial t}d^{3}r = \oint \stackrel{\leftrightarrow}{T}\cdot d \vec{s}=\int \nabla \cdot \stackrel{\leftrightarrow}{T} d^{3}r$$
ou seja:
$$\frac{\partial \vec{g}}{\partial t}= \nabla \cdot \stackrel{\leftrightarrow}{T}$$
temos então uma outra **equação de Continuidade**. 

- Uma coisa interessante de notar acerca do vetor Poynting:
    - $\vec{S}$ é densidade de energia por área e por tempo.
    - $\mu_{0}\varepsilon_{0}\vec{S}$ é densidade de momento por unidade de volume nos campos EM

- Similarmente para o tensor de tensões de  Maxwell:
    - $\stackrel{\leftrightarrow}{T}$ é a tensão eletromagnética (força por área)
    - $-\stackrel{\leftrightarrow}{T}$ é o fluxo de momento dos campos