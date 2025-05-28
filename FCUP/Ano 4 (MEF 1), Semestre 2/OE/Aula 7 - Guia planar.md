## Algumas tecnologias
### Sensores em fibra ótica
![[sensor em fibra otica esquema.png]]
- Ou seja, a grandeza ou fenómeno a medir altera as propriedades da luz que se propaga na fibra ótica na região de interação

### Estado da arte
- Atualmente, o máximo atingido é 2000km entre repetidores de sinal, com uma frequência de 8 THz
    - Temos 200 canais de comprimentos de onda diferentes
    - Estes canais e frequência dão: 40Gb/s
- Existe atualmente uma vasta mas fundamental rede de fibras óticas que sustentam a internet

# Guias dielétricos planares
- Um guia de onda dielétrico planar tem esta estrutura:
![[propagacao em guia plano.png]]
em que, necessariamente, $$\boxed{n_{1}> n_{2}}$$
- **NOTA**: uma explicação de notação. $\theta$ marca um ângulo do *feixe com a superfície*. $\overline{\theta}$ marca um ângulo do *feixe com a normal*.
- A condição para reflexão total é $\overline{\theta}>\overline{\theta}_{C}$, em que: $\overline{\theta}_{C}=\text{arcsin}\left(\frac{n_{2}}{n_{1}}\right)$
- Olhemos agora para os ângulos do feixe guiado na figura (feixe da direita). Temos que: $\theta=\frac{\pi}{2} -\overline{\theta}$. 
    - Sabemos que $\overline{\theta}>\overline{\theta}_C$ porque o feixe mantém-se no guia. Assim, temos: $$\theta<\frac{\pi}{2} - \overline{\theta_{C}}~~\to~~\theta<\text{arcos}\left(\frac{n_{2}}{n_{1}}\right)=\theta_{c}$$
- Assim, temos os ângulos críticos normal e tangente:
$$\overline{\theta_{C}}=\text{arcsin}\left(\frac{n_{2}}{n_{1}}\right) \quad;\quad \theta_{C}=\text{arcos}\left(\frac{n_{2}}{n_{1}}\right)$$

### Independente de Z
- Pretendemos formar modos de propagação que tenham o mesmo efeito que a sobreposição de 2 ondas planas com separação $2\theta$ que seja constante ao longo de Z!
- Ou seja, há **certos angulos** (não qualquer angulo!) que dão *modos de propagação*
![[ondas planas interferencia guia plano.png]]

- Para ter isto, precisamos que isto aconteça:
![[ondas planas interferencia guia plano 2.png]]
- Consideremos $\phi_{1}$ a fase da onda que se propaga até B (e passa em A)
- Consideremos $\phi_{2}$ a fase da onda que se propaga até C (e passa em A)
- Temos que ter continuidade em A, logo acontecer o que temos acima, é preciso que
$$\phi_{2}=\phi_{1}+2\pi m~~~~~~,~~ m=0,1,2,\dots$$
que podemos escrever como $\Delta \phi=2\pi m$

### Condição Modal
- Vamos agora de volta à figura do topo deste resumo. Consideremos a onda que se propaga ao longo de $\theta$ (em direção a A e B). Temos:
$$\lambda=\frac{\lambda_{0}}{n_{1}}~~,~~c_{1}=\frac{c_{0}}{n_{1}}~~,~~k_{1}=n_{1}k_{0}$$
em que
$$k_{x}=0~~,~~k_{y}=n_{1}k_{0}\sin\theta~~,~~k_{z}=n_{1}k_{0}\cos\theta$$
(aqui temos $x$ a ser o eixo perpendicular à pagina e Y,Z mostrados na figura)
- Também vemos por geometria, que:
$$\overline{AC}-\overline{AB}=2d\sin\theta$$
($d$ é a espessura/altura do guia)

- Podemos considerar que a fase inicial (antes da primeira reflexão) é $\phi_{r}$. Temos 2 reflexões então usamos $2\phi_{r}$
- Além disso, podemos definir a diferença de fase definida pela diferença na distância percorrida pelos feixes AB e AC: $\frac{2\pi}{\lambda}(2d\sin\theta)$ -> $\vec{k}\cdot\vec{r}$ 
- Juntando tudo, temos a equação que nos dá os ângulos dos modos - a *condição modal*:
$$\boxed{\frac{2\pi}{\lambda}\cdot 2d\sin\theta - 2 \phi_{r}=2m\pi}$$
pelo que ao alterar o valor de $m$ sabemos o ângulo do modo $m$.

### Modos 
- Consideremos polarização TE: $\vec{E}=E_{x}\hat{x}$
- Neste cenário temos o campo perpendicular ao plano de incidência (no ponto A). 
- Pelas eqs de Fresnel, o campo incidente $E_{i\perp}$ e refletido $E_{r\perp}$ têm uma diferença de fase.
- Ora, consoante $\theta$ vai de $0\to\theta_{C}$ temos que $\phi_{r}$ vai de $0\to\pi$. Mais concretamente, temos:
$$\tan \frac{\phi_{r}}{2} = \sqrt{\frac{\sin^{2}\theta_{c}}{\sin^{2}\theta}-1}$$
da condição modal podemos escrever:
$$\tan \frac{\phi_{r}}{2}=\tan \left[ \frac{\pi d\sin\theta}{\lambda} - \frac{m\pi}{2} \right]$$
- Juntando as 2 equações acima temos:
$$\tan \left[ \frac{\pi d\sin\theta}{\lambda} - \frac{m\pi}{2} \right]=\sqrt{\frac{\sin^{2}\theta_{c}}{\sin^{2}\theta}-1}$$
- Ora, aqui temos 2 coisas muito distintas:
    - No termo da *esquerda*, consoante $m$ varia temos 2 famílias de funções: $$\tan \left[ \frac{\pi d\sin\theta}{\lambda} - \frac{m\pi}{2} \right]=\begin{cases} \tan\left[\pi \frac{d}{\lambda}\sin\theta\right] & ; & m\text{ par} \\\cot\left[\pi \frac{d}{\lambda}\sin\theta\right] & ; & m\text{ impar}\end{cases}$$
    - No da direita temos uma função que decresce em função de $\sin\theta$
- Podemos olhara para esta equação de outra forma: os ângulo modais $\theta_{m}$ são os **pontos de interseção** destas 2 funções de $\sin\theta$.

![[angulos modais permitidos.png]]
(LHS e RHS são os lados esquerdo e direito da equação)

- Assim, teremos:
$$\vec{k}=\left(0, n_{1}k_{0}\sin\theta_{m}, n_{1}k_{0}\cos\theta_{m} \right)$$
- É ainda normal usar a seguinte notação para assinalar a componente na *direção do guia* (neste caso ZZ):
$$\beta_{m}=n_{1}k_{0}\cos\theta_{0}\in [n_{2}k_{0},n_{1}k_{0}]$$
porque
$$\theta_{m}\in[o,\theta_{C}]\quad\to\quad\cos\theta_{m}\in \left[1,\cos\theta_{C}\right]$$
ora, sabemos que $$\theta_{C}=\text{arcos} \left[\frac{n_{2}}{n_{1}} \right]~~\to~~ \cos\theta_{C}=\frac{n_{2}}{n_{1}}$$
logo $\cos\theta_{m}\in[1,n_{2}/n_{1}]$
![[Screenshot_1.png]]
- Ao representar assim, vemos que haverá sempre um número máximo de modos: $M$
- Ora, esse número será :
$$M=\left\lceil\frac{\sin\theta_{C}}{\frac{\lambda}{2d}}\right\rceil=\left\lceil2 \frac{d}{\lambda_{0}} \sqrt{n_{1}^{2}-n_{2}^{2}}\right\rceil= \left\lceil 2\nu  \frac{d}{c_{0}}\sqrt{n_{1}^{2}-n_{2}^{2}}\right\rceil$$
em que usamos $\left\lceil\dot{~}\right\rceil$ para indicar que $M$ é o inteiro imediatamente acima do que está dentro.

### Abertura numérica (NA)
- Definimos 
![[abertura numerica.png]]  
$$\text{NA}=\sin\theta_{a}$$
ou seja, $\theta_{a}$ é o ângulo máximo com que raios a incidir no guia vindos do ar *podem ser guiados*.
- Temos que (não tenho dedução):
$$\text{NA}=\sqrt{n_{1}^{2}-n_{2}^{2}}$$
- Podemos então escrever: $M=\left\lceil2 \frac{d}{\lambda_{0}}\text{NA}\right\rceil$

#### Monomodo e Corte
- Da equação de $M$ é evidente que quando$$2 \frac{d}{\lambda_{0}}\text{NA}<1 \quad \quad\longleftarrow \quad \text{Condição Monomodo}$$
**apenas 1 modo existe**!!!
- Neste caso temos um guia ==monomodo==

- Na introdução histórica referimos que existe um **comprimento de onda de corte**. Também vem desta equação: $\frac{2d}{\lambda_{0}}\text{NA}<1~~\to~~\lambda_{0}>2d\text{NA}$
    - Ou seja, para comprimentos de onda _acima_ de $\lambda_{0C}=2d\text{NA}$ SÓ há 1 modo.
    - Daqui, claro, podemos definir a **frequência de corte** : $\nu_{C}=\frac{c_{0}}{2d\text{NA}}$, em que para frequências *abaixo* desta SÓ há 1 modo.
- Vemos daqui que podemos ainda escrever:
$$M=\left\lceil \frac{\nu}{\nu_{C}}\right\rceil$$
isto é uma equação muito mais simples e direta, que permite rapidamente entender o número de modos.
- Temos então:
![[numero de modos e freq critica.png]]

### Campo TE
- Vamos agora determinar o campo transverso associado ao ângulo $\theta_{m}$
- Na figura de cima de todo, consideremos as ondas que se propagam acima e abaixo do ponto da primeira reflexão ($\pm\theta_{m}$):
$$\begin{align*}
E_{+\theta_{m}}&= A_{m}e^{i(\omega t-n_{1}k_{0}y\sin\theta_{m} - n_{1}k_{0}z\cos\theta_{m})}\\
E_{-\theta_{m}}&= A_{m}e^{i(\omega t+n_{1}k_{0}y\sin\theta_{m} - n_{1}k_{0}z\cos\theta_{m}+\phi_{0})}
\end{align*}$$
Logo o campo em $x$ para o modo $m$ será:
$$E_{x,m}=E_{+\theta_{m}}+E_{-\theta_{m}}$$

**Figura altamente geométrica**
- Consideremos agora:
![[OE-fig1|950]]
- O feixe bate em B e é refletido com ângulo $\theta$ dos dos lados. Na figura projetamos o ponto B num segundo feixe (a linha que liga B ao feixe de baixo é perpendicular a este)
    - $\theta$ é o ângulo de reflexão do modo com a superfície do guia
    - $\alpha$ é o ângulo entre a superfície do guia e a projeção de B no feixe de baixo
    - $\zeta=\alpha-\theta$
- Vendo o triângulo verde: $180=\alpha+90+\theta~\to~\alpha=90-\theta$
- Logo: $\zeta=90-2\theta$
- Olhando para o triangulo laranja temos $L=\frac{d}{2\sin\theta}$
- Olhando para o triângulo definido pelas beiras de $\zeta$ temos: $\sin\zeta=\frac{K}{L}$
    - No lado esquerdo temos: $\sin(90-2\theta)=\cos(2\theta)=1-2\sin^{2}\theta$
    - Do lado direito: $2K\sin\theta/d$
    - Juntando tudo: $$K=\frac{d(1-2\sin^{2}\theta)}{2\sin\theta}$$
- Assim, $$L-K=d\sin\theta$$
- Assim, a diferença de fase entre o feixe de cima refletido e o feixe de baixo quando ambos chegam a P é: $\frac{2\pi}{\lambda}(L-K)=\frac{2\pi}{\lambda}d\sin\theta$
- Além disso, como os 2 feixes não intersetam ao mesmo tempo no guia, assumimos que o feixe de cima tem uma fase $\phi_{r}$.
- Assim, a diferença de fase em P é:
$$\frac{2\pi}{\lambda}d\sin\theta-\phi_{r}$$

**De volta ao campo**
- A figura de cima não é nada mais que uma representação da interseção entre um campo $E_{-\theta_{m}}$ (feixe de cima) com um campo com um $E_{+\theta_{m}}$ (feixe de baixo)
- Ou seja, podemos definir:
$$\phi_{0}=\text{fase}_{-\theta}-\text{fase}_{+\theta}=\frac{2\pi}{\lambda}d\sin\theta-\phi_{r}$$
e temos a equação $\tan \frac{\phi_{r}}{2} = \sqrt{\frac{\sin^{2}\theta_{c}}{\sin^{2}\theta}-1}$ , que nos dá $\phi_{r}$.

- Temos então a fase do campo em X.
- Nas aulas TP supostamente deduziram isto, mas temos que o campo:
$$E_{x,m}=a_{m}u_{m}(y)e^{-i\beta_{m}z}e^{i\omega t} \quad\quad;\quad - \frac{d}{2}\le y\le \frac{d}{2}$$
em que $u_{m}$ é uma função normalizada e ortogonal no intervalo de $y$ :
$$u_{m}(y)=\begin{cases}
\mu_{m}\cos \left(\frac{2\pi n_{1}\sin\theta_{m}}{\lambda}y \right)  & ; & m \text{ par} \\
\overline{\mu}_{m}\sin \left(\frac{2\pi n_{1}\sin\theta_{m}}{\lambda}y \right)  & ; & m \text{ impar}
\end{cases}$$
em que $a_{m},\mu_{m},\overline{\mu}_{m}$ são constantes.

- Desta equação vemos que o campo NÃO se anula em $y=\pm \frac{d}{2}$. 

**Continuidade**
- Se a onda está a ser guiada ela está contida dentro do guia
- Assim, para $|y|\ge \frac{d}{2}$ é preciso que o campo seja nulo.
- Temos que $E_{xm}=a_{m}u_{m}(y)e^{-i\beta_{m}z}e^{i\omega t}$. 
    - A dependência em $z$  é $e^{-i\beta_{m}z}$
    - Ora, numa interface as componentes tangentes de $\vec{E},\vec{H}$ têm de ter continuidade. Neste caso, $z$ é a unica direção tangente.
    - Assim, deveremos ter a mesma dependência em $z$ para $|y|\ge \frac{d}{2}$ 

- Ao aplicar a equação de Helmholtz a este problema obtemos:
$$\frac{d^{2}u_{m}(y)}{dy^{2}}-\gamma_{m}^{2}u_{m}(y)=0$$
em que $\gamma_{m}^{2}=\beta_{m}^{2}-n_{2}^{2}k_{0}^{2}$.

- Isto dá-nos a solução:
$$u_{m}(y)=B_{m}w^{\pm \gamma_{m}y}$$
($B_{m}$ é uma constante)
- Para modos guiados, vimos nos limites de $k_{z}=\beta_{m}$ que: $\beta_{m}> n_{2}k_{0}$. Assim, teremos $\gamma_{m}^{2}>0$ logo temos $\gamma_{m}$ real.
- Assim, escolhemos o sinal correto para que o campo não aumente exponencialmente fora do guia:
$$u_{m}^{\text{fora guia}}(y)=\begin{cases}
B_{m} e^{-\gamma_{m}y} & ; & y> \frac{d}{2} \\
B_{m} e^{+\gamma_{m}y} & ; & y< -\frac{d}{2}
\end{cases}$$
notemos que isto é uma *onda evanescente* de cada lado do guia. Esta tem profundidade de penetração $\gamma_{m}$ !
- Tendo em conta que $\gamma_{m}^{2}=\beta_{m}^{2}-n_{2}^{2}k_{0}^{2}$, podemos escrever:
$$\gamma_{m}= n_{2}k_{0} \sqrt{\frac{\cos^{2}\theta_{m}}{\cos^{2}\theta_{C}}-1}$$
quando $\theta_{m}$ aumenta, $\gamma_{m}$ diminui. 

**O perfil**
![[modos transversais.png]]
- Notamos que para $m=0$ temos um campo aproximadamente gaussiano
- Podemos ter outra interpretação: as funções $u_{m}(y)$ *formam uma base* que permite obter todos os perfis dos modos.
    - Esta base é ortonormada como já referimos: $\int_{-\infty}^{+\infty}u_{m}(y)u_{n}(y)dy=\delta_{nm}$
- Notemos que o efeito de alargamento de um feixe gaussiano é completamente compensado num modo.

### TM
- Temos que $\vec{H}=\sqrt{\frac{\varepsilon}{\mu}} \frac{\vec{k}}{|\vec{k}|}\times \vec{E}$ 
- Ora, para estudar o caso de polarização TM apenas muda a equação com que determinamos $\phi_{r}$:
$$\tan\phi_{r}=\sqrt{\frac{\cos^{2}\theta- \cos^{2}\theta_{C}}{\sin\theta\cos^{2}\theta_{C}}}$$
