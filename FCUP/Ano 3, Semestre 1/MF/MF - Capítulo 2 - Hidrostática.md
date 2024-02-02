# 2 - Hidrostática
## 2.1 - Pressão num ponto dentro de fluido
![[pressões em volume de fluido.png]]
- Consideremos o volume infinitesimal de fluido acima. Ele está em repouso, pelo que não existem tensões de corte aplicadas.
- Ora, se o fluido está em equilibrio, então a soma das forças nele aplicado é 0. Assim:
(Notemos que a força aplicada numa face será $F=pA$)
**Direção xx**
- A força total aplicada na face da direita será: $F_{-x}=p_{x}A=p_{x} \delta y  \delta z$
- A força total aplicada na face de baixo (inclinada) será $F_{+x}=p_{\theta}A=p_{\theta} \delta z \sqrt{(\delta x)^{2}+(\delta y)^{2}}$ (em que se usou o teorema de Pitágoras)
    - Ora, a força aplicada nesta face, *na direção x* será $F_{+x}=p_{\theta}A \cdot \sin\theta=p_{\theta} \delta z \sqrt{(\delta x)^{2}+(\delta y)^{2}}\sin\theta$ (faz desenhos se for preciso)
    - Podemos ainda escrever $\sin\theta=\frac{\delta y}{\sqrt{(\delta x)^{2}+(\delta y)^{2}}}$
    - Logo a força aplicada nesta fase na direção x é: $F_{+x}=p_\theta \delta z \delta y$
- Pelo que a força total aplicada nesta direção é nula, ou seja:
$$F_{+x}=F_{-x}\to p_{x} \delta y \delta z= p_{\theta} \delta z \delta y \to p_{x}=p_{\theta}$$

**Direção yy**
- A força total aplicada na face de cima é $F_{-y}=p_{y} \delta x \delta z$
- Vejamos a face inclinada.
    - Repetindo a análise acima, vemos que a força aplicada na direção y é $F_{+y}=p_{\theta} \delta z \sqrt{(\delta x)^{2}+(\delta y)^{2}}\cos\theta$; em que podemos escrever $\cos\theta= \frac{\delta x}{\sqrt{(\delta x)^{2}+(\delta y)^{2}}}$
    - Ou seja: $F_{+y}=p_{\theta} \delta z \delta x$
- No entanto, neste caso, além das forças aplicadas nas faces, temos a **força gravítica**, que atua em todo o volume e tem direção $-y$. Ora, $F_{g}=mg=g \rho V=g \rho \frac{\delta x \delta y \delta z}{2}$
- Novamente, as forças no sentido $+y$ e $-y$ têm que se anular, ou seja:
$$F_{-y}+F_{g}=F_{+y} \to p_{y} \delta x \delta z + g \rho \frac{\delta x \delta y \delta z}{2} =p_{\theta} \delta z \delta x \to p_{y} + \rho g  \frac{\delta y}{2}= p_\theta$$
- Ora, se tomarmos o limite $\delta x,\delta y, \delta z\to0$ ficamos com:
$$p_{x}=p_{y}=p_{\theta}$$
ou seja, concluimos que, num fluido em **repouso** a pressão aplicada num ponto é igual em todas as direções.

## 2.2 - Equação Fundamental da Hidrostática
- Consideremos um volume infinitesimal cúbico de fluido em repouso. Ele tem dimensões $\delta x,\delta y, \delta z$. Vamos presumir que ele ocorre uma ligeira variação da pressão em cada direção.
- Vejamos o que é preciso, em termos de pressões para que ele esteja em equilíbrio.

**Direção zz**
![[pressao volume 1.png]]
- Na face de baixo temos uma pressão $p$, pelo que a força é $F_{+y}=p \delta x \delta y$
- Na face de cima temos aplicada uma pressão $p + \frac{\partial p }{\partial z} \delta z$ (em que o segundo temos representa uma variação de pressão nesta direção). A força será $F_{-y}=\delta x \delta y\left(p + \frac{\partial p }{\partial z} \delta z\right)$
- Temos ainda aplicada a força gravítica, na direção $-y$, dada por $F_{g}=g \rho \delta x \delta y \delta z$
- Assim, fazendo o balanço das forças:
$$F_{-y}=F_{+y}+F_{g}~~\to~~ p \delta x \delta y= \delta x \delta y\left(p + \frac{\partial p }{\partial z} \delta z\right)+ g \rho \delta x \delta y \delta z ~~\to~~ \frac{\partial p}{\partial z}=-\rho g$$

**Direção xx**
![[presao volume 2.png]]
- Na face da esquerda temos uma pressão $p$, logo $F_{+x}=p \delta y \delta z$
- Na face da direita teremos $F_{-x}=\left(p + \frac{\partial p}{\partial x}\delta x\right)\delta y \delta z$
- Assim, o balanço de forças dá:
$$F_{-x}=F_{+x} ~~\to~~ \frac{\partial p}{\partial x}=0 $$

**Direção yy**
- É análoga à direção xx. Do balanço de forças obtém-se:
$$\frac{\partial p}{\partial y}=0$$

---
- Se juntarmos as 3 equações acima obtemos então:
$$\boxed{\frac{\partial p}{\partial x}\hat{i}+\frac{\partial p}{\partial y}\hat{j}+\frac{\partial p}{\partial z}\hat{k}=\nabla p= \rho \vec{g}}$$
sendo esta a **Equação fundamental da Hidrostática**

### Fluidos incompressíveis
- Fluidos em que a massa volúmica não varia com a pressão (se variar pouco podemos aproximar).
![[pressao em tubo.png|167]]
Para fluidos destes podemos simplesmente integrar a equação fundamental para determinar a diferença de pressão entre 2 pontos:
$$\int_{p_{1}}^{p_{2}}p~dp=-\rho g \int_{z_{1}}^{z_{2}}dz~~\to~~ p_{1}=p_{2}+\rho gh$$
sendo então $h$ (AKA Carga de pressão) a altura de fluido necessária para haver diferença de pressão $p_{1}-p_{2}$

### Fluidos compressíveis
- Especialmente o caso dos gases. Eles são compressíveis. Se fluirem com alta velocidade a sua massa volúmica pode variar.
- Assim, se o gás for *perfeito*:
$$p=\rho RT\to \int_{p_{1}}^{p_{2}} \frac{dp}{p}=\ln \frac{p_{2}}{p_{1}} = \frac{-g}{R}\int_{z_{1}}^{z_{2}} \frac{dz}{T}$$
($R$ é a constante dos gases perfeitos, pelo que depende do gás em si)
- Se a temperatura for constante em todo o gás temos:
$$p_{2}=p_{1} \exp \left[ - \frac{g(z_{2}-z_{1})}{RT_{0}} \right] $$

## 2.3 - Manómetros Diferenciais
- Usado para medir diferenças de pressão.
- Na sua forma mais simples consiste num tubo em U de secção transversal reduzida, em que temos um fluido de massa volúmica conhecida.
![[manometro.png]]
- O principal ponto a notar aqui é que **dentro de um mesmo fluido** os pontos com a **mesma cota** estão sujeitos à **mesma pressão**.

## 2.4 - Forças em Superfícies Submersas
- Quando uma superfície está submersa ou em contacto com um fluido em repouso, a pressão que o fluido exerce é sempre normal á superfície 
![[pressao em superficies submersas.png|500]]

### 2.4.1 - Superfícies Planas Verticais
![[janela.png]]
- Temos uma janela ABCD, de altura $b$ e comprimento $a$. Ela encontra-se na lateral de um tanque com um fluido, estando este sujeito à pressão atmosférica no topo. Queremos saber a pressão aplicada nesta janela.
- Colocou-se o referencial na superfície livre do fluido, a apontar para baixo.
- Na imagem da direita temos a vista frontal da janela, em que traçamos uma tira infinitesimal $i$ com área: $\delta A_{i}=L_{i} \delta z_{i}$. O lado de cima da tira dista $z_{i}$ do referencial. A força de pressão aplicada na tira é $\delta F_{i}=p_{i} \delta A_{i}$
- Ora, se $\delta z_{i}\to0$ a tira torna-se numa linha horizontal em que a pressão será toda igual.

- A pressão total aplicada será a pressão atmosférica + a pressão devido ao fluido até à parte de baixo da janela:
$$p_{i}=p_{atm} + \rho g z_{i} \to \delta F_{i}=(p_{atm} + \rho g z_{i}) L_{i} \delta z_{i}$$
o que, no limite $\delta z_{i}\to 0$ nos dá:
$$F=\int_{h_{0}}^{h_{o}+b}(p_{atm}+\rho gz)L dz=p_{atm}ab + \rho g~ab~ \left(h_{0} \frac{b}{2}\right)=F_{int}$$
podemos ainda obter a força que a atmosfera exerce na janela (do lado de fora do tanque):
$$p_{i}=p_{atm}\to \delta F_{i}=p_{atm}L z_{i} ~~\Longrightarrow ~~F_{ext}=\int_{h_{0}}^{h_{0}+b} p_{atm}Ldz=p_{atm} ab$$
- Ora, temos:
$$F_{total}=F_{int}-F_{ext}=\rho g~ab\left(h_{0}+ \frac{b}{2}\right)$$
pelo que a força aponta na horizonal (perpendicular à janela) de dentro para fora.

### 2.4.2 - Superfícies planas inclinadas
![[sup plana inclinada.png]]
- Consideremos que temos uma janela triangular numa parede inclinada de um tanque (inclinação $\theta$, indicada em cima) que contém um fluido em repouso sujeito a pressão atmosférica. Queremos saber a força a que a janela está sujeito e o momento que esta gera no eixo $oo'$ - ver imagem.

- A pressão a que a tira infinitesimal $i$ está sujeita é:
$$\delta p_{i}=p_{i,int}-\delta p_{i,ext}=(p_{atm}+\rho g z_{i})-p_{atm}=\rho g z_{i}$$
em que o refrencial de $z$ se encontra na superfície livre do fluido. Assim a força na tira $\delta F_{i}$ é:
$$\delta F_{i}=\rho g z_{i} \delta x_{i}L_{i}$$
- Ora, $z$ é medido na vertical, enquanto que $x$ é medido na face inclinada. Assim, podemos relacionar:
$$z=x\sin\theta$$
- Ainda assim temos 2 variáveis. Ora, o triângulo acima da tira e o triângulo inteiro são semelhantes. Ou seja podemos establecer:
$$\frac{L_{i}}{x_{i}-a}=\frac{c}{b} ~~\longrightarrow~~ L_{i}= \frac{c}{b}(x_{i}-a)$$
- Logo a força na tira pode ser escrita como $\delta F_{i}=\rho g x_{i}\sin\theta \frac{c}{b}(x_{i}-a)\delta  x_{i}$ . Logo quando $\delta x_{i}\to0$ temos:
$$F=\int_{a}^{a+b}\rho g \sin \theta \frac{c}{b} ~x(x-a)dx=\rho g \sin\theta \frac{c}{b}\left[ (a+b)^{2} \left(\frac{2b-a}{6}\right)+ \frac{a^{3}}{6} \right]$$

- Ora, para calcular o momento desta força em relação ao eixo $oo'$  basta multiplicar a força na tira infinitesimal pela distância a que essa força está do eixo de rotação (isto porque a força será sempre perpendicular à superfície submersa AKA $\vec{r}\perp\vec{F}$), ou seja:
$$\delta M_{i}=\delta F_{i}x_{i}=x_{i}\rho g x_{i}\sin\theta \frac{c}{b}(x_{i}-a)\delta  x_{i}$$o que nos dá:
$$M_{oo'}= \rho g\sin\theta \frac{c}{b}\left[(a+b)^{3} \left(\frac{3b-a}{12}\right)+ \frac{a^{4}}{12} \right]$$

### 2.4.3 - Superfícies Curvas
![[cilindro submerso 1.png]]
- Consideremos um cilindro de comprimento $L$ mergulhado num fluido em repouso.
- Podemos então definir uma tira infinitesimal como ilustrado acima. Em toda esta tira (desde que seja muito fina) teremos que a pressão tem o mesmo sentido, direção e intensidade. A sua área será:
$$\delta A_{i}=L_{i} R \delta \theta_{i}$$
(isto será especialmente válido se $\delta \theta\to0$, pois temos basicamente uma tira retangular)
![[cilindro submerso 2.png]]
pelo que podemos dividir a força aplicada na tira nas suas componentes vertical e horinzontal: $F_{V},F_{H}$
**Componente Vertical**
- A componente vertical é dada por $\delta F_{Vi}=\cos\theta_{i} \delta F_{i}=\cos\theta_{i}p_{i} L_{i}R\delta \theta_{i}$
- Em que $p_{i}=p_{atm}+ \rho g z_{i}$. Ora, temos que $z_{i}=h_{0}+(R-R\cos\theta_{i})$ (ver figura abaixo)
![[cilindro submerso 3.png]]
- Assim: $\delta F_{Vi}=[p_{atm}+ \rho g (h_{0}+R-R\cos\theta_{i})]\cos\theta_{i}RL_{i}\delta \theta_{i}$
- Ao integral de $0\to2\pi$ obtemos $$F_{V}= - \rho g \pi R^{2}L $$
que simplesmente é a impulsão a que um corpo imerso está sujeito. De acordo com o princípio de Arquimedes: a impulsão a que um corpo está sujeito corresponde ao peso do volume de fluido por ele deslocado.

**Componente Horizontal**
- Agora temos: $\delta F_{Hi}=\sin\theta_{i}\delta F_{i}=\sin\theta_{i}p_{i}(RL_{i} \delta\theta_{i})$
- E simplesmente obtemos: $\delta F_{Vi}=[p_{atm}+ \rho g (h_{0}+R-R\cos\theta_{i})]\sin\theta_{i}RL_{i}\delta \theta_{i}$ 
- Ora, ao integrar obtemos $$F_{H}=0$$

#### Método de Projeção
![[sup submersa curva.png]]
- Vejamos então como calcular a força hidrostática total aplicada na superfície curva.
- Consideremos uma tira infinitesimal correspondente ao ângulo $\delta \theta_{i}$. Ora, se intervalo de ângulo for suficientemente reduzido podemos considerar que a superfície é plana. Assim temos:
$$\delta F_{i}=p_{i} \delta A_{i}$$
**Componente Horizontal**
- A componente horizontal será $\delta F_{Hi}=p_{i} \cos\theta \delta A_{i}=p_{i} \text{proj}_{V}\delta A_{i}$ (a força horizontal estará associada à componente vertical da área)
- Para uma superfície curva mais complexa teríamos:
![[Componente horizontal força.png]]
pelo que em muitos casos ficamos com:
$$F_{H}=\int \rho g dz$$

**Componente Vertical**
![[Componente vertical força 1.png]]
- Aqui teríamos $\delta F_{Vi}=p_{i} \sin\theta_{i} \delta A_{i}$
- Em que temos $p_{i}=\rho g h_{i}$, obtendo-se $\delta F_{Vi}=\rho g h_{i}\sin\theta_{i} \delta A_{i}$
- Ora, $\sin\theta_{i}\delta A_{i}$ é a projeção horizontal da área e $h_{i}$ a distância desde a superfície livre até à tira. Assim $h_{i}\sin\theta_{i} \delta A_{i}$ é o volume desde a tira até à superfície livre.
- De uma forma geral:
![[componente vertical força 2.png]]
- Ou seja temos: $$\delta F_{Vi}=\rho g \delta V_{i} ~~ \longrightarrow ~~ F_{V}=\int_{V} \rho g dV=\rho g V$$
que é igual ao *peso do volume de fluido acima da superfície*.

##### Superfície Fechada
Para uma qualquer superfície fechada temos
![[superfície fechada.png]]
- E facilmente obtemos a componente vertical da força:
$$F_{V}=F_{V2}-F_{V1}= \rho g V_{2}-\rho g V_{1}=\rho g V_{S}$$
em que $V_{S}$ é o volume do sólido e temos que $F_{V}$ é a força de impulsão.

## 2.5 - Equilíbrio Relativo
- Se um fluido for transportado de forma que todos os seus elementos tenham a mesma velocidade, então não há deslocamento relativo entre eles e não se desenvolvem tensões de corte. Ou seja, temos um problema de Hidrostática. (Exemplo: pessoa a correr com copo de água)

- Consideremos então um tanque com líquido de massa volúmica $\rho$ que se desloca em movimento retilíneo uniformemente acelerado (na horizontal). Num volume infinitesimal de fluido temos:
![[volume fluido com aceleracao.png]]
(em que a aceleração em $x$ cria uma variação/aumento de pressão $\delta p$ com sentido oposto)
- Ora, para que o volume esteja em equilíbrio é necessário que essa pressão extra gere uma força extra que consiga anular a força de inércia (gerada pelo movimento) dada por $\delta F_{x}=a_{x} \delta m$
- Ou seja, equilibrando a força de inércia e forças de pressão dos 2 lados:
$$\begin{align*}
p \delta A - (p+\delta p)\delta A &= a_{x} \delta m\\
\cancel{p \delta A} -  \cancel{p \delta A} + \delta p \delta A &= a_{x} \delta m\\
\end{align*}$$
temos que $m=\rho V$ logo $\delta m = \rho \delta x \delta A$. Assim ficamos com:
$$\frac{\delta p}{\delta x}=- \rho a_{x}$$

o que nos dá:
$$p_{1}-p_{2} = \rho_{L} a_{x} L$$
(em que $p_{1},p_{2}$ são as pressões em 2 pontos à distância $L$)

- No entanto, continuamos a ter que a equação fundamental da hidrostática nos dá:
$$\frac{\partial p}{\partial z}=-\rho g ~~\Longleftrightarrow~~ p_{1}-p_{2}=\rho g(h_{1}-h_{2})$$
- Como a pressão num ponto é igual em todas as direções, para os pontos em que $p_{1}-p_{2}$ temos:
$$\rho a_{x} L = \rho g(h_{1}-h_{2})~~\Longrightarrow \frac{h_{1}-h_{2}}{L}=\frac{a_{x}}{g}=\tan\theta$$conforme esta figura:
![[fluido em movimento.png|213]]

### Forma Geral
- Consideremos que as forças aplicadas num volume infinitesimal com aceleração constante $\vec{a}=(a_{x},a_{y},a_{z})$:
![[variacao pressoes em volume em movimento.png]]
- Ao fazer equilibrio das forças de todas as direções obtemos:
$$\begin{cases}
\frac{\partial p}{\partial x}=-\rho a_{x} \\
\frac{\partial p}{\partial x}=-\rho a_{y} \\
\frac{\partial p}{\partial x}=-\rho (a_{z}+g) 
\end{cases} \Longrightarrow \boxed{\nabla p=-\rho (\vec{a}-\vec{g})}$$
pelo que a Equação Fundamental da Hidrostática é um caso particular desta, em que $\vec{a}=\vec{0}$

