## 7.1 - Introdução
![[escoamento laminar ou turbulento - experimental.png]]
- A experiência de Reynolds consiste em largar no centro de um fluido uma linha quase pontual de tinta. Na figura acima vemos o que acontece conforme o tipo de escoamento. Mais concretamente, vemos que a transição laminar > transição > turbulento ocorre ao aumentar o caudal.
- No regime laminar a velocida apenas tem a direção do escoamento. No turbulento ela tem ainda uma componente na direção normal à do escoamento.

- Ora, mas o que garante ao certo que temos regime laminar ou turbulento? O regime laminar consiste num escoamento dominado pelas forças viscosas. Como vimos no capítulo 6, a relação entre as forças viscosas e de inércia é dada pelo grupo adimensional de Reynolds. Ou seja, permite-nos saber quando é que um tipo de forças domina o outro. Experimentalmente concluiu-se que:
    - Se $\text{Re}<2100$ temos escoamento laminar.
    - Se $\text{Re}>4000$ temos escoamento turbulento.

## 7.2 - Escoamento Laminar
### 7.2.1 - Equação de Poiseuille
![[evolucao VC em escoamento laminar.png]]
Nesta figura temos um escoamento laminar  num tubo circular de diâmetro $D$. O VC inicialmente retangular (raio $r$ e comprimento $l$) em $t$ fica na forma representada em $t+\delta t$.

- As linhas de corrente / trajetórias são paralelos. Mas a velocidade das partículas depende da sua distância ao centro do tubo aka raio. Isto faz com que as paredes verticais do VC em $t$ se tornem curvas passado algum tempo.
- Quando o escoamento é estacionário e perfeitamente desenvolvido nenhuma partícula tem aceleração e o perfil de velocidades é constante.
- Ora, para que o VC não tenha aceleração é necessário que a soma das forças nele aplicadas seja nula.

- Nas paredes horizontais (como o tubo é circular isto é 1 só superfície) na figura acima geram-se forças de corte com sentido oposto ao deslocamento. Assim, tem que existir força no sentido do deslocamento.
- Essas são forças de pressão, geradas pelos elementos de fluido em movimento contra a superfície do VC. Considerando o eixo $x$ como sendo horizontal, da esquerda para a direita. 
    - Ora, os elementos a entrar no VC geram uma força de pressão positiva nos xx. 
    - Os elementos que estão à direita do VC geram força contra o seu movimento, ou seja, força de pressão megativa nos xx.

Ignorando a gravidade e considerando a pressão numa secção transversal uniforme:
![[forças aplicadas em VC em esc laminar.png]]

Da 2ª Lei de Newton:
$$ma_{x}=0=-2\pi rl \tau-(p_{1}-\Delta p)\pi r^{2} + p_{1} \pi r^{2} $$
e surge:
$$\frac{\Delta p}{l}=\frac{2\tau}{r}$$

**Perfil de Velocidade**
- Vejamos com detalhe o perfil de velocidades. Junto ao tubo temos $v=0$ (condição de não deslizamento, temos isto porque $\mu\neq0$) e no centro temos velocidade máxima, ou seja, o perfil é parabólico. Assim, sendo $\tau=-\mu \frac{dv_{x}}{dr}$, a tensão de corte é máxima junto à parede do tubo. Temos então as condições de fronteira:
$$r=0\to \tau=0 \quad;\quad r=R\to \tau=\tau_{R}$$
naturalmente, $\frac{2\tau}{r}=\frac{2\tau_{R}}{R}=\frac{4\tau_{R}}{D}$. Ou seja:
$$\frac{\Delta p}{l}=\frac{4 \tau_{R}}{D}$$ ou seja, a perda de pressão por unidade de comprimento *não depende do raio* do tubo.

- Podemos ainda escrever:
$$\tau=-\mu \frac{d v_{x}}{dr}\to \frac{dv_{x}}{dr}=- \frac{\Delta p}{2\mu l}r$$
integrando:
$$\int dv_{x}=-\frac{\Delta p}{2 \mu l}\int rdr\to v_{x}=- \frac{\Delta p}{4\mu l}r^{2}+C_{1}$$
- Devido ao fluido ter viscosidade, temos $$v_{x}(r=R)=0\to C_{1}=\frac{\Delta p}{16 \mu l}D^{2}$$
- E ficamos com:
$$\begin{align*}
v_{x}&= - \frac{\Delta p}{4\mu l}r^{2}+ \frac{\Delta p}{16 \mu l}D^{2}\\
&= \frac{\Delta p D^{2}}{16 \mu  l} \left[1 - \left(\frac{2r}{D}\right)^{2} \right]\\
&= v_{max}\left[1 - \left(\frac{r}{R}\right)^{2} \right]
\end{align*}$$
em que $$v_{max}=\frac{\Delta pD^{2}}{16\mu l}$$

**Caudal**
- O caudal é $Q=vA$. No caso deste tubo $dQ=vdA$ e definimos um anel infinitesimal de área $dA=2\pi r dr$. Fica:
$$Q=\int v_{x}(r)dA=\int v_{x}(r)2\pi r ~dr=2\pi v_{max}\int_{0}^{R}\left[1 - \left(\frac{r}{R} \right)^{2}\right]r~dr=\frac{\pi R^{2} v_{max}}{2}$$

- Podemos definir a velocidade media. Esta consiste na velocidade que os elementos de fluido teriam se o caudal fosse o mesmo e a velocidade uniforme no tubo. Temos então:
$$\bar v=\frac{Q}{A}=\frac{1}{2}v_{max}$$

**Queda de Pressão - fim**
- Voltando à equação anterior:
$$\frac{\Delta p}{l}=\frac{2\tau_{R}}{R}$$
e temos:
$$\tau_{R}=\left[-\mu \frac{dv_{x}}{dr}\right]_{r=R}=\mu \frac{4v_{max}}{D}$$
- Juntando as duas:
$$\Delta p= \frac{128\mu l}{\pi D^{4}}Q$$
que é a **_Equação de Poiseuille_** que nos dá a perda de pressão de um fluido a escoar num tubo de diâmetro $D$ numa distância $l$ com caudal $Q$. Esta podia ter sido deduzida com análise dimensional.
- Se dividirmos tudo por $\rho g$ ficamos com a perda de carga:
$$\frac{\Delta p}{\rho g}=\frac{128\mu l}{\pi \rho g D^{4}}Q$$

- Podemos ainda escrever
$$\frac{\Delta p}{\frac{1}{2}\rho \bar v^{2}} = \frac{32\mu l \bar v/D}{\frac{1}{2}\rho \bar v^{2}} =\frac{64}{\text{Re}} \frac{l}{D}$$
ou seja:
$$\Delta p=f \frac{1}{2} \rho \bar v^{2} \frac{l}{D}$$
em que $f=\frac{64}{\text{Re}}$ é o **fator de Fanning**.

#### Notas sobre EXS
- Quase sempre, em escoamento laminar, a carga cinética é desprezável!
- Em muitos problemas, calculamos a perda de carga usando a equação da energia e usando a equação de Poiseuille. Ao compará-las, conseguimos determinar o sinal da carga. O escoamento ocorre na direção em que a perda de carga for positiva. Noutros casos, igualar as 2 perdas calculadas permite obter uma incógnita de um dos lados.

##### Resistências
- Muitas vezes podemos fazer analogia entre escoamento laminar e circuitos elétricos:
$$\Delta p=\frac{128\mu l}{\pi D^{4}}Q ~~\Leftrightarrow ~~ \Delta V=RI$$
pelo que podemos pensar na perda de pressão como variação de potencial e no caudal como corrente.

- Assim, tendo um tubo de diâmetro $D_{1}$ e comprimento $l_{1}$ que a certo ponto passa a ter diâmetro $D_{2}$ por uma distância $l_{2}$, é como se tivessemos 2 resistências em série, com:
$$R_{equiv}= R_{1}+R_{2}= \frac{128\mu}{\pi} \left(\frac{l_{1}}{D_{1}^{4}} + \frac{l_{2}}{D_{2}^{4}} \right)$$

### 7.2.2 - Escoamento Laminar em 2 tubos concêntricos
- Consideremos um fluido a escoar entre 2 tubos de raios $R_{1},R_{2}$:
![[escoamento laminar por tubos concentricos.png]]
- Consideramos as tretas do costume: escoamento de fluido incompressível e newtoniano. Regime laminar perfeitamente desenvolvido em estado estacionário.
- Temos então o perfil de velocidade $v_{x}=f(r)$.

![[escoamento por tubos concentricos - volume infinitesimal.png]]
- Se considerarmos um elemento infinitesimal de fluido como na figura acima temos que as únicas 2 forças aplicadas são a força da tensão de corte e a força de pressão, que se anulam. Assim temos o balança de forças:
$$p_{x}\cdot2r\delta r-p_{x+\delta x}\cdot2r\delta r-\tau_{rx_{r}}\cdot2r\delta x+ \tau_{rx_{r+\delta r}}\cdot2(r+\delta r)\delta x=0$$
que podemos reescrever como
$$-r \frac{p_{x+\delta x}-p_{x}}{\delta x}+ \frac{\tau_{rx_{r+\delta r}}(r+\delta r)-\tau_{rx_{r}}r}{\delta r}=0$$
ou seja:
$$\begin{align*}
-r \frac{dp}{dx}+ \frac{d}{dr}(r~\tau_{rx})&= 0\\
+r \frac{\Delta p}{l}+ \frac{d}{dr}(r~\tau_{rx})&= 0\\
\frac{d}{dr}(r~\tau_{rx})&= -r \frac{\Delta p}{l}\\
\int \frac{d}{dr}(r~\tau_{rx})dr&= -\frac{\Delta p}{l}\int dr\\
r \tau_{rx}&= -\frac{\Delta p}{l} \frac{r^{2}}{2} + C_{1}\\
\tau_{rx}&= -\frac{\Delta p}{l} \frac{r}{2} + \frac{C_{1}}{r}
\end{align*}$$
(em que, sendo o escoamento horizontal e perfeitamente desenvolvido, temos $dp/dx$ constante e igual a $\Delta p/l$)

- Para fluidos Newtonianos temos, por definição:
$$\tau_{rx}=\mu\frac{d v_{x}(r)}{dr}$$
ou seja:
$$\begin{align*}
\mu\frac{d v_{x}(r)}{dr}&= -\frac{\Delta p}{l} \frac{r}{2} + \frac{C_{1}}{r}\\
v_{x}&= - \frac{r^{2}}{4\mu}\frac{\Delta p}{l} - C_{1}\ln r + C_{2}
\end{align*}$$
determinamos $C_{1},C_{2}$ devido à condição de não deslizamento: $v=0$ para $r=R_{1},R_{2}$.

### 7.2.3 - Escoamento Laminar em Coluna de Parede Molhada
- Temos um fluido a escoar junto a uma parede, por ação da gravidade:
![[escoamento laminar por parede molhada.png]]
- Agora não temos o fluido a empurrar ar e não consideramos a pressão exercida por elementos de fluido uns nos outros, temos que não há nada para anular as forças de tensão de corte.
- A ação da gravidade impede a coluna de fluido de mudar de espessura $\delta$ por causa das forças de tensão de corte.
- Apliquemos a 2ª Lei de Newton ao elemento de fluido ilustrado ($\delta W$ é o seu peso):
$$\begin{align*}
\delta W+ \sum\limits\delta F_{z-corte} &= 0\\
\rho g l \delta x - t_{xz_{x+\delta x}}l+\tau_{xz_{x}}l&= 0\\
\rho g&= \frac{t_{xz_{x+\delta x}}-\tau_{xz_{x}}}{\delta x}=\frac{d}{dx}\tau_{xz}
\end{align*}$$
- Sendo $\mu_{ar}\sim0$ temos que a tensão de corte no interface líquido-ar será nula. Assim, podemos integrar a equação acima e fica:
$$\tau_{xz}=\rho gx$$
- Daqui vem:
$$\begin{align*}
\tau_{xz}=-\mu \frac{dv_{z}(x)}{dx}&= \rho gx\\
v_{z}(x)&= -\int_{\delta}^{x} \frac{\rho g x}{\mu}dx\\
&= \frac{\rho g}{\mu}\int_{x}^{\delta}x dx\\
&= \frac{\rho g}{\mu} \left(\frac{\delta^{2}}{2}-\frac{x^{2}}{2}\right)\\
&= \frac{\rho g \delta^{2}}{2\mu}\left(1- \frac{x^{2}}{\delta^{2}}\right)=v_{max}\left(1- \frac{x^{2}}{\delta^{2}}\right)
\end{align*}$$
com $v_{max}=\frac{\rho g \delta^{2}}{2\mu}$

- Podemos ainda obter a velocidade média $\bar v_{z}=\frac{1}{A}\int_{A}v_{z}(x)dA=\frac{\rho g}{3\mu}\delta^{2}$, o que pode ser escrito como $\bar v_{z}=\frac{2}{3} v_{max}$.
- Isto também nos dá $Q=\bar v_{z}\delta=\frac{\rho g\delta^{3}}{3\mu}$

### 7.2.4 - Escoamento Laminar em Coluna de Parede Molada Inclinada
![[escoamento laminar por parede molhada inclinada.png]]
- Muito parecido ao caso anterior mas:
$$\begin{align*}
v_{max}&= \frac{\rho g\delta^{2}\sin\theta}{2\mu}\left(1- \frac{x^{2}}{\delta^{2}}\right)\\
\bar v_{z}&= \frac{1}{A}\int_{A}v_{z}(x)dA=\frac{\rho g \sin\theta}{3\mu}\delta^{2}\\
Q&= \frac{\rho g\sin\theta \delta^{3}}{3\mu}
\end{align*}$$

## 7.3 - Escoamento Turbulento
- Consideremos um tubo muito comprido. Dentro temos um fluido, inicialmente em repouso.
- Abrimos uma válvula e o fluido começa a mover-se cada vez mais rápido (sendo este rate de aumento muito lento).
    - Para números de Reynolds baixos temos um escoamento laminar
    - Para $2100<Re<4000$ estamos em fase de transição
    - A partir daí temos regime turbulento.
![[grafico regimes de escoamento.png]]

- Escoamento turbulento é caraterizado por oscilações da velocidade, pressão e tensões de corte nas 3 direções, de forma irregular e aleatória.

- Podemos definir o valor médio da velocidade:
$$\bar v_{x}= \frac{1}{\Delta t}\int_{t_{0}}^{t_{0}+\Delta t}v_{x}(x,y,z,t)dt$$
- Podemos ainda definir a *parcela de flutuação* $v'$:
$$v_{x}'(x,t)=v_{x}(x,t)-\bar v_{x}$$
cujo valor médio será obviamente zero.
- Podemos definir a média quadrática da parcela de flutuação:
$$\overline {v_{x}^{'2}}= \frac{1}{\Delta t}\int_{t_{0}}^{t_{0}+\Delta t}v_{x}^{'2}dt>0$$
sendo esta uma medida do quanto o escoamento oscila.

- Dito isto, podemos definir a **Intensidade/nível de turbulência**:
$$\mathcal{I}=\frac{\sqrt{\overline{v_{x}^{'2}}}}{\overline v_{x}}=\frac{\left[\frac{1}{\Delta t}\int_{t_{0}}^{t_{0}+\Delta t}v_{x}^{'2}dt\right]^\frac{1}{2}}{\overline v_{x}}$$
em que maior nível de turbulência, maior a amplitude das oscilações.

- Podemos definir a "viscosidade turbulenta" $\eta$ de forma a definir a tensão de corte num fluido em escoamento turbulento:
$$\tau=\eta \frac{d\bar  v_{x}}{dy}$$
em que 
$$\eta=\rho l_{m}^{2}\Biggr|\frac{d\bar v}{dy}\Biggr|$$
ou seja:
$$\tau=\rho l_{m}^{2} \left(\frac{d\bar v_{x}}{dy}\right)^{2}$$
o problema na maioria dos casos é determinar o **comprimento de mistura** $l_{m}$, que por vezes nem é constante.


- Outra forma de descrever um fluido em escoamento turbulento é definir 3 camadas conforme a proximidade à parede:
![[regiao laminar de escoamento turbulento.png]]
- Conforme os nomes indicam, em certas zonas o fluido tem comportamento viscoso e noutras comportamento turbulento. 
- Podemos então definir a tensão de corte como $\tau=\tau_{laminar}+\tau_{turbulento}=\mu\frac{dv_{x}}{dy}-\rho\overline{v_{x}'v_{y}'}$

- Ora, na sub-camada viscosa temos o seguinte perfil de velocidade:
$$\frac{\bar v_{x}(y)}{v^{*}}=\frac{yv^{*}}{\nu} \quad \quad \quad;\quad (\text{válido para }0\le\frac{yv^{*}}{\nu}\le5)$$
em que $y=R-r~,~\nu=\frac{\mu}{\rho}~,~v^{*}=\sqrt{\frac{\tau_{w}}{\rho}}$
- Na camada intermédia:
$$\frac{\bar v_{x}(y)}{v^{*}}=2,5\ln\frac{yv^{*}}{\nu}+5$$
- Na camada exterior:
$$\frac{v_{c}-\bar v_{x}(y)}{v^{*}}=2,5\ln\frac{R}{y}$$
em que $v_{c}$ é a velocidade no eixo do tubo.

- Uma equação que define bem o padrão de velocidades observado (exceto mt perto da parede ou mt perto do centro do tubo) é
$$\frac{\bar v_{x}(y)}{v_{x}}= \left(1-\frac{r}{R}\right)^{\frac{1}{n}}$$
em que $n$ depende do número de Reynolds e $n=7$ um valor usado para uma grande gama de valores de Reynolds.