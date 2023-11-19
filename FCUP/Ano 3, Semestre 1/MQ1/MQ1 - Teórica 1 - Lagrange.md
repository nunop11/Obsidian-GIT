# 1. Introdução
## 1.1 - Revisão de Mecânica Clássica - Mecânica Analítica
### 2ª Lei de Newton
- Comecemos por recordar a 2ª Lei de Newton, que nos diz: $$\vec{F}=\frac{d \vec{p}}{dt} \quad \quad \textsf{em que:} \quad \vec{p}=m \vec{v} ~~~~;~~~~ \vec{v}= \frac{d \vec{r}}{dt}$$
pelo que podemos então escrever da forma mais conhecida: $$\boxed{\vec{F}= m \vec{a}}$$

__*EXEMPLO - Oscilador Harmónico Simples*__
- Vejamos agora um caso simples que conhecemos bastante bem: o Oscilador Harmónimo Simples (OHS). Iremos voltar a este várias vezes ao longo desta aula.
- Num oscilador destes temos simplesmente uma massa (com massa $m$) presa a uma mola (de constante de mola $k$), cujo lado oposto está fixo. Ora, na massa gera-se uma força restauradora, que "tenta" colocar a mola no seu estado de equilíbrio. Esta força é determinada pela Lei de Hooke: $$F = -kx$$
em que $x$ é a posição da massa, *relativamente à posição de equilíbrio*.
- Este comportamento é retratado na figura abaixo:
![[ohs.png]]

- Ora, apliquemos a 2ª Lei de Newton ao Oscilador Harmónico:
$$\begin{align*}
F &=  ma\\
-kx &= m \frac{d^{2}x}{dt^{2}}\\
m \frac{d^{2}x}{dt^{2}} + kx &= 0\\
\end{align*}$$
conforme o que aprendemos em Análise 3 conseguimos resolver esta equação diferencial e temos:
$$x(t)= A \cos(\omega t + \varphi) \quad \quad;\quad A=x(0)~~,~~ \varphi=\dot{x}(0) \quad \textsf{(constantes)}$$
ou seja, conseguimos prever todo o comportamento deste sistema se soubermos $A, \varphi$.

### Força Conservativa
- Uma força conservativa pode ser escrita como o gradiente de um potencial escalar. Ou seja:
$$\vec{F}=- \nabla V \quad \quad ; \quad \quad V=V(\vec{r}) ~ \rightarrow ~ \textsf{Potencial}$$
- Tem-se ainda que a energia total de um corpo é dada por: $$E=T-V$$
em que $T$ é a *Energia Cinética* e $V$ é a *Energia Potencial*.

- Consideremos um sistema "normal" em que $T=\frac12 m \vec{v}(t)^{2}$. Podemos então determinar a derivada temporal da energia:
$$\begin{align*}
\frac{dE}{dt}&= \frac{d}{dt}\left(\frac12m \vec{v}(t)^{2}+V(\vec{r}(t))\right)\\
&= \frac12m \cdot2 \vec{v}\cdot \frac{d\vec{v}}{dt} + \frac{dV}{dt}\\
&= m \vec{v}\cdot \frac{d\vec{v}}{dt} + \frac{dx^{i}}{dt} \frac{\partial V}{\partial x^{i}}\\
&= m \vec{v}\cdot \vec{a} + \vec{v} \cdot (-\vec{F})\\
&= \vec{v}\cdot \vec{F} + \vec{v} \cdot (- \vec{F})\\
&= 0
\end{align*}$$
ou seja, como a derivada da energia é 0, e portanto verificamos que sistemas em que apenas temos forças do tipo $\vec{F}=- \nabla V$ *conservam* a energia AKA *são conservativos*.

> __Notas acerca da dedução acima__
> - Na transição $m \vec{v}\cdot \vec{a} \Longrightarrow \vec{v} \cdot \vec{F}$ usou-se a 2ª Lei de Newton
> - Na parte: $\frac{dx^{i}}{dt} \frac{\partial V}{\partial x^{i}}$ está-se a usar *notação de Newton* sendo que:
> $$\frac{dx^{i}}{dt} \frac{\partial V}{\partial x^{i}} = \sum\limits_{i=1}^{N}\frac{dx^{i}}{dt} \frac{\partial V}{\partial x^{i}}$$
> sendo que o que temos acima é para um sistema de $N$ dimensões. Num sistema 3D $(x,y,z)$ temos: $x^{1}=x,x^{2}=y,x^{3}=z$, o que nos dá:
> $$\frac{dx^{i}}{dt} \frac{\partial V}{\partial x^{i}}=\sum\limits_{i=1}^{3}\frac{dx^{i}}{dt} \frac{\partial V}{\partial x^{i}}=\frac{dx}{dt}\frac{\partial V}{\partial x} + \frac{dy}{dt}\frac{\partial V}{\partial y} + \frac{dz}{dt}\frac{\partial V}{\partial z}$$
> Ora podemos escrever isto como o seguinte produto escalar:
> $$\frac{dx}{dt}\frac{\partial V}{\partial x} + \frac{dy}{dt}\frac{\partial V}{\partial y} + \frac{dz}{dt}\frac{\partial V}{\partial z} = \left(\frac{dx}{dt},\frac{dy}{dt},\frac{dz}{dt} \right)\cdot \left(\frac{\partial V}{\partial x}, \frac{\partial V}{\partial y}, \frac{\partial V}{\partial z}  \right)= \frac{d\vec{r}}{dt} \cdot \nabla V$$
> Ora, estamos a considerar um sistema em que $\vec{F}=- \nabla V$ logo:
> $$\frac{dx^{i}}{dt} \frac{\partial V}{\partial x^{i}} = \frac{d\vec{r}}{dt} \cdot \nabla V = \vec{v} \cdot (-\vec{F})$$

__*De volta ao Exemplo do Oscilador Harmónico Simples*__
- Neste sistema 1D temos $F=-kx$, pela Lei de Hooke. Ora, idealmente este sistema é conservativo. Assim: $$F=-\nabla V=-kx ~~\Longrightarrow~~ V = \frac12 kx^{2}$$
temos ainda que neste sistema o gráfico $E(x)$ é do tipo:
![[energia de ohs.png|500]]

### Princípio Variacional
- Tem-se que trajetórias físicas clássicas extremizam o funcional *ação* $S$. Por outras palavras, tendo 2 trajetórias, a trajetória que de facto ocorre (segundo a física clássica é a única possível) é aquela em que a ação é extremizada (mínima ou máxima). 
- Por exemplo, para o caso da queda de uma bola, o percurso que extremiza a ação é aquele que vai da posição inicial para o chão em linha reta, ao invés de um percurso que faça curvas antes de chegar ao chão.

> __NOTA - Funcional__
> - Uma função recebe um parâmetro/número e dá um número: $f(x): x\to \#$
> - Um funcional recebe uma função e dá um número: $S[f(x)]:f\to \#$

- A *ação* é definida como:
$$S[\vec{r}(t)]=\int_{t_{i}}^{t_{f}}dt \mathcal{L}[\vec{r}(t), \dot{\vec{r}}(t), t] \tag{Eq.1}$$

### Lagrangiano 
Definido como:
$$\boxed{\mathcal{L}=T(\dot{\vec{r}}) - V(\vec{r},t)}\tag{Eq.2}$$
- Sendo que temos 1 lagrangiano por cada dimensão do problema em estudo.

### Coordenadas generalizadas
- Num certo problema temos $N$ coordenadas generalizadas: $q_{a}(t)$. Ou seja:
$$q_{a}(t)=\{ q_{1}(t),q_{2}(t),q_{3}(t),\cdots,q_{N}(t) \}$$
$$\dot{q}_{a}(t)=\{ \dot{q}_{1}(t),\dot{q}_{2}(t),\dot{q}_{3}(t),\cdots,\dot{q}_{N}(t) \}$$
- Ou seja, podemos escrever o lagrangiano como:
$$\mathcal{L}=\mathcal{L}(q, \dot{q},t)=T(\dot{q})-V(q,t)$$

### Qual a trajetória clássica?
(Para fazer esta secção segui [este vídeo](https://www.youtube.com/watch?v=sFqp2lCEvwM))
![[dedução de eq E-L.png|450]]
- Consideremos que temos uma trajetória clássica $q(t)$ e uma trajetória $\bar q(t)= q(t)+\delta \eta(t)$, que apresenta um desvio $\delta \eta(t)$ relativamente à trajetória original. Conforme a Figura acima temos a seguinte condição de fronteira:
$$\eta(t_{i})=\eta(t_{f})=0$$

- Podemos então definir a Ação:
$$S(\delta)=\int_{t_{i}}^{t_{f}} \mathcal{L}(\bar q, \dot{\bar q},t)dt$$
Temos que $S$ apenas depende de $\delta$, porque "perdemos" a variável $t$ no integral e $\bar q,\dot{\bar q}$ dependem de $t$.
- Ora, queremos saber em que condições é que $\bar q$ é também uma trajetória clássica. Ora, para ser esse o caso é necessário que $S$ esteja num extremo, segundo o princípio variacional. Ou seja queremos ter:
$$\frac{dS}{d\delta}=0\tag{Eq.3}$$
ou seja:
$$\frac{d}{d\delta} \int_{t_{i}}^{t_{f}} \mathcal{L}(\bar q, \dot{\bar q},t)dt = 0 \longrightarrow \int_{t_{i}}^{t_{f}} \frac{\partial}{\partial \delta} \mathcal{L}(\bar q, \dot{\bar  q}, t)dt =0$$
- Ora, como $\bar q=q+\delta \eta$, temos $\bar q=\bar q(t, \delta)$. Ou seja, $\bar q,\dot{\bar q}$ dependem de $\delta$. Podemos então usar *chain rule* na derivada $\frac{\partial \mathcal{L}}{\partial \delta}$:
$$\int_{t_{i}}^{t_{f}} \left[ \frac{\partial \mathcal{L}}{\partial \bar q}\frac{\partial \bar q}{\partial \delta} + \frac{\partial \mathcal{L}}{\partial \dot{\bar q}}\frac{\partial \dot{\bar q}}{\partial \delta} \right] dt =0$$

- Temos $\bar q=q+\delta \eta$ ora: $$\frac{\partial \bar q}{\partial \delta}=\eta \quad \quad ;\quad \quad \dot{\bar q}= \dot{q}+\delta \dot{\eta} \quad \Rightarrow \quad \frac{\partial \dot{\bar q}}{\partial \delta}=\dot{\eta} $$
o que nos dá:
$$\int_{t_{i}}^{t_{f}} \left[ \frac{\partial \mathcal{L}}{\partial \bar q}\eta + \frac{\partial \mathcal{L}}{\partial \dot{\bar q}}\dot{\eta} \right] dt =0\tag{Eq.4}$$
- Façamos o integral da 2ª parcela:
$$\begin{align*}
\int_{t_{i}}^{t_{f}}\frac{\partial \mathcal{L}}{\partial \dot{\bar q}}\dot{\eta}~dt &= \frac{\partial\mathcal{L}}{\partial\dot{\bar q}} \int_{t_{i}}^{t_{f}}\dot{\eta}~dt-\int_{t_{i}}^{t_{f}}\eta \frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{\bar q}} \right)dt\\
&= \cancelto{=0}{\frac{\partial \mathcal{L}}{\partial \dot{\bar q}} \eta\biggr|_{t_{i}}^{t_{f}}}-\int\eta \frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{\bar q}} \right)dt\\
\end{align*} $$
(Acima, na primeira linha usei integração por partes. Na segunda linha, cortamos a primeira parcela porque $\eta|_{t_{i}}^{t_{f}}=0-0=0$, conforme as condições de fronteira establecidas acima.)

- Ao substituir isto na Eq. 4 ficamos com:
$$\begin{align*}
\int_{t_{i}}^{t_{f}} \left[ \frac{\partial \mathcal{L}}{\partial \bar q}\eta -\eta \frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{\bar q}} \right)\right] dt &= 0\\
\int_{t_{i}}^{t_{f}} \left[ \frac{\partial \mathcal{L}}{\partial \bar q} - \frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{\bar q}} \right)\right]\eta~ dt &= 0
\end{align*}$$
Ora, a única forma de esta igualdade se verificar é se o integrando for nulo. Ou seja, podemos escrever:
$$\boxed{\frac{\partial \mathcal{L}}{\partial q} - \frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{ q}} \right)=0}\tag{Eq.5}$$
e é esta a **_Equação de Euler-Lagrange_**.
- Ela diz-nos que se uma trajetória $q$ satisfazer esta equação diferencial, *provavelmente* ela irá extremizar a Ação. Ou seja, será uma trajetória clássica.
- No entanto, devemos notar que esta é uma condição *necessária*, não *suficiente*. Além disso, não nos diz se a ação irá atingir um máximo ou mínimo.

### Momento Conjugado
- Definimos o momento conjugado d euma trajetória $q(t)$ como sendo: $$p(t)=\frac{\partial \mathcal{L}}{\partial \dot{q}}$$
__*Voltar um última vez ao oscilador harmónico simples*__
- Como já vimos, o potencial deste sistema 1D é: $V=\frac12kx^{2}$. A energia cinética é: $T=\frac12m \dot{x}^{2}$
- Assim o lagrangiano deste sistema é:
$$\mathcal{L}=\frac12m \dot{x}^{2}-\frac12kx^{2}$$
Facilmente vemos que:
$$\frac{\partial \mathcal{L}}{\partial x}=-kx \quad \quad;\quad \quad \frac{\partial \mathcal{L}}{\partial \dot{x}}=m \dot{x}$$
Ao substituir na equação Euler-Lagrange temos:
$$\frac{\partial \mathcal{L}}{\partial q} = \frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{ q}} \right) \quad \Longrightarrow \quad -kx = m \ddot{x}$$
- Ora, isto não passa da 2ª Lei de Newton aplicada a este sistema, como vimos atrás. Por outras palavras, aplicar a equação Euler-Lagrange a este sistema dá-nos uma equação diferencial que descreve o comportamento do sistema previsto pela física clássica (a equação do movimento do OHS). 

### Teorema de Noether
- Consideremos que num certo sistema o Lagrangiano não depende de 1 variável/coordenada $q_{i}$, ou seja: $$\frac{\partial\mathcal{L}}{\partial q_{i}}=0$$
- Neste caso, a equação de Euler-Lagrange dá-nos:
$$\frac{d}{dt}\left( \frac{\partial \mathcal{L}}{\partial q_{i}} \right)=0=\frac{dp_{i}}{dt}$$
- Por palavras, o momento conjugado nesta coordenada, $p_{i}$, é **conservado**.

- Ora, isto tem implicações interessantes. Basicamente, segundo o *Teorema de Noether*, cada **simetria de conservação** corresponde a uma quantidade que é conservada. Ou seja, temos os seguintes tipos de simetria:
    - **Translação** - Sistema que funciona igual se o "deslizar-mos" para outra posição ele ocorre (por exemplo, se o sistema for uma massa a deslizar, não importa onde ela está, ela irá sempre deslizar em linha reta infinitamente) - temos conservação de momento linear.
    - **Rotação** - Sistema que funciona igual dentro de um eixo circular - temos conservação de momento angular (Por exemplo, um certo corpo terá o mesmo angular em todo o planeta, desde que esteja à mesma altura. Este sistema não terá simetria de translação, porque se o deslizarmos para "baixo", o momento angular varia.)
    - **Tempo** - Tipo de simetria que temos falado neste resumo. Quando um sistema funciona igual agora ou daqui a algum tempo - temos conservação de energia (Mesmo sistemas que consideramos como não conservativos em termos de energia, são conservativos se considerarmos todas as perdas de energia -- um sistema em que temos uma massa a deslizar numa superfície rugosa, a energia é conservada, mas é transferida da massa para a superfície).

- Assim, este teorema diz-nos que se for feita uma transformação ao referencial do sistema podemos fazer com que passe a haver conservação de alguma quantidade. Inversamente, se descobrirmos que alguma quantidade é conservada num sistema, é possível determinar a sua simetria.