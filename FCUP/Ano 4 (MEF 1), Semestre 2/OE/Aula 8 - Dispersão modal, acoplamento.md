## Dispersão Modal
- Para modos com $\theta_{m}$ maiores (feixe move-se mais "na vertical"), temos um maior número de oscilações e reflexões ao longo de uma certa extensão do guia
- Como todos os feixes se movem à mesma velocidade, isto quer dizer que feixes destes modos irão demorar mais tempo a percorrer o guia
- Assim, como cada modo demora o seu tempo a percorrer o guia, temos **Dispersão Modal**

**Equações**
- Temos a condição modal: $\frac{4\pi}{\lambda} d\sin\theta_{m}-2\phi_{r,m}=2\pi m$ 
- Assumindo que $|\frac{4\pi}{\lambda}d\sin\theta_{m}|>|2\phi_{r,m}|$, temos:
$$\begin{align*}
2d\overbrace{\frac{2\pi}{\lambda}\sin\theta_{m}}^{k_{y}}-2\phi_{r,m}&= 2\pi m\\
2dk_{y}-2\phi_{r,m}&= 2\pi m
\end{align*}$$
tendo em conta as definições de $k_{x},k_{y},k_{z}/\beta$ que fizemos na aula anterior, temos que:
$$k_{y}^{2}=k^{2}-\beta^{2}= \left(\frac{\omega}{c_{1}}\right)^{2}-\beta^{2}$$
e substituimos acima:
$$\begin{align*}
2d \sqrt{\left(\frac{\omega}{c_{1}}\right)^{2}-\beta^{2}}&= 2\phi_{r,m}+2\pi m\\
\frac{\phi_{r,m}}{2} &= \frac{d}{2} \sqrt{\left(\frac{\omega}{c_{1}}\right)^{2}-\beta^{2}} - \frac{\pi m}{2}\\
\tan^{2}\left(\frac{\phi_{r,m}}{2}\right)&= \tan^{2} \left[ \frac{d}{2} \sqrt{\left(\frac{\omega}{c_{1}}\right)^{2} - \beta^{2}} - \frac{\pi m}{2}\right]
\end{align*}$$
e aplicamos a equação de $\tan \frac{\phi_{r,m}}{2}$ da aula anterior: $\tan^{2}\frac{\phi_{r,m}}{2}= \frac{\sin^{2}\theta_{C}}{\sin^{2}\theta}-1$.

*Melhorar o lado esquerdo*
- Podemos escrever:
$$\theta_{c}=\text{arcos}\left(\frac{n_{2}}{n_{1}}\right)~\to~\cos\theta_{c}=\frac{n_{2}}{n_{1}}~\to~\sin^{2}\theta_{c}=1- \left(\frac{n_{2}}{n_{1}}\right)^{2}$$
e temos
$$\cos\theta= \frac{\beta}{k}= \frac{\beta}{\omega/c_{1}}= \frac{c_{1}\beta}{\omega}~\to~\sin^{2}\theta=1- \left(\frac{c_{1}\beta}{\omega}\right)^{2}$$

*Juntar tudo*
- Juntando estas com a equação de cima:
$$\tan^{2} \left[ \frac{d}{2} \sqrt{\left(\frac{\omega}{c_{1}}\right)^{2} - \beta^{2}} - \frac{\pi m}{2}\right]=\frac{\beta^{2}- \left(\frac{\omega}{c_{2}}\right)^{2}}{\left(\frac{\omega}{c_{1}}\right)^{2}-\beta^{2}}$$
isto dá-nos a relação entre $\beta$ e $\omega$ para qualquer $m$.
- Para polarização TE temos isto:
![[freq vs beta.png]]
Por exemplo, vemos que para $\omega<\omega_{c}$ apenas temos 1 modo possível, tal como vimos para $\lambda_{0c},\nu_{c}$.
- Podemos definir:
$$\omega_{c}=2\pi\nu_{c}=\frac{\pi c_{0}}{d \sqrt{n_{1}^{2}-n_{2}^{2}}} \quad;\quad \nu_{c}=\frac{c_{0}}{2d\text{NA}}$$

- O que o gráfico acima nos diz é que: se injetarmos no guia um feixe de frequência $\omega_\text{operação}$, é possível excitar os modos $m=0,1,2$. Isto é feito ao variar o *ângulo de incidência*.
- Notemos ainda que $\omega_{c},2\omega_{c},\dots$ marcam a frequência de corte do modo 1,2,...

### Colocar a dispersão de outra forma
- Sabemos que numa onda plana a propagar-se no vazio podemos definir o índice de refração assim: $$n=\frac{c_{0}k}{\omega}$$
- Para um feixe a propagar-se num guia, podemos definir um índice de propagação: $$n_\text{efe}=\frac{c_{0}\beta}{\omega}$$
- Não tenho a dedução, mas partindo da equação de dispersão grande acima, temos:
$$\omega=\omega_{c} \frac{\sqrt{n_{1}^{2}-n_{2}^{2}}}{\sqrt{n_{1}^{2}-n_\text{efe}^{2}}}\left[m + \frac{2}{\pi}\arctan\left(\frac{\sqrt{n_{\text{efe}}^{2} -n_{2}^{2}}}{\sqrt{n_{1}^{2}-n_\text{efe}^{2}}}\right) \right]$$

### Velocidade de grupo
- A velocidade de grupo num guia é definida da mesma forma que fizemos num meio dispersivo:
$$v_{g}=\frac{d\omega}{d\beta}$$
![[freq vs vel grupo.png]]
- Usemos a lógica:
    - Um certo modo $m$ tem um ângulo de propagação $\theta_{m}$. A velocidade está associada a um número de oscilações por unidade de comprimento do guia.
    - Mas o gráfico acima mostra que a velocidade de grupo varia com a frequência. Vemos que existe uma maior variação (linha menos vertical) consoante nos aproximamos da frequência de corte. 
- Vamos ver porquê que isto acontece:

**Vg vs freq**
- Temos a condição modal: $2d \sqrt{\left(\frac{\omega}{c_{1}}\right)^{2}-\beta^{2}}=2\phi_{r}+2\pi m$. Podemos derivar em $\beta$:
$$\begin{align*}
\frac{2d}{2} \frac{1}{\sqrt{\left(\frac{\omega}{c_{1}}\right)^{2}-\beta^{2}}} \frac{d}{d\beta}\left[\left(\frac{\omega}{c_{1}}\right)^{2}-\beta^{2} \right]&= 2 \frac{d\phi_{r}}{d\beta}\\
d \cdot \frac{1}{k_{y}} \cdot \left(\frac{2\omega}{c_{1}^{2}} \frac{d\omega}{d\beta} - 2\beta\right)&= \frac{d\phi_{r}}{d\beta} + \frac{d\phi_{r}}{d\omega} \frac{d\omega}{d\beta}
\end{align*}$$
neste passo usamos: $k_{y}^{2}=(\frac{\omega}{c_{1}})^{2}-\beta^{2}$ e simplesmente dividimos o lado direito na soma de 2 derivadas parecidas lol

- Ao usar as definições dos $k_{i}$  temos:
$$\sin\theta= \frac{k_{y}}{k}=\frac{k_{y}}{\omega/c_{1}}\to k_{y}=\frac{\omega}{c_{1}}\sin\theta$$
assim como
$$\tan\theta=\frac{k_{y}}{\beta}\to \beta=\frac{\omega}{c_{1}}\cos\theta$$

- Como $v_{g}=\frac{d\omega}{d\beta}$, podemos escrever:
$$\begin{align*}
\frac{d}{\frac{\omega}{c_{1}}\sin\theta}\left(\frac{2\omega}{c_{1}^{2}}v_{g} - 2 \frac{\omega}{c_{1}}\cos\theta \right)=\frac{d\phi_{r}}{d\beta} + \frac{d\phi_{r}}{d\omega}v_{g}
\end{align*}$$
- Podemos dizer que $\frac{d\phi_{r}}{d\beta}=\Delta z~~,~~ \frac{d\phi_{r}}{d\omega}=-\Delta\tau$. Isto é decidido ao ver que estas derivadas têm dimensões de comprimento e tempo, respetivamente.
- Assim temos:
$$\begin{align*}
\frac{d}{\frac{\omega}{c_{1}}\sin\theta}\left(\frac{2\omega}{c_{1}^{2}}v_{g} - 2 \frac{\omega}{c_{1}}\cos\theta \right)&= \Delta z - v_{g}\Delta\tau\\
d \left(\frac{2v_{g}}{c_{1}}\csc\theta -2\cot\theta \right)&= \Delta z - v_{g}\Delta\tau\\
v_{g}&= \frac{d\cot\theta+\Delta z}{\frac{d}{c_{1}}\csc\theta+\Delta \tau}
\end{align*}$$

### Vg de forma intuitiva
- Quando o feixe se propaga entre 2 reflexões temos:
![[explicar vg de forma intuitiva.png]]
em que já estão marcadas as distâncias deste triângulo. Sabemos ainda todos os ângulos.
- Vemos então que $\overline{AB}=d\csc\theta$. Logo a luz demora um tempo $\frac{d\csc\theta}{c_{1}}$ a ir de A para B
- Temos ainda que, no intervalo de tempo $\frac{d\csc\theta}{c_{1}}$ o feixe  percorre uma distância $d\cot\theta$ *ao longo do guia*
- Ou seja, a **velocidade de propagação no guia** é: $\frac{d\cot\theta}{\frac{d\csc\theta}{c_{1}}}$
    - Esta equação *não* bate certo com a da velocidade de grupo, sendo que nessa temos uma distância $\Delta z$ extra percorrida, num tempo extra $\Delta\tau$!
- Isto acontece porque a reflexão NÃO acontece no interface dos meios 1 e 2, mas sim num **plano fronteira dentro do meio 2**!
![[reflexao nao é instantanea.png]]
e daqui surge a distância e tempo extras. Notemos que nesta parte "extra" o feixe move-se a velocidade $n_{2}$. Assim, a velocidade de grupo acaba por ser uma *média pesada* entre as velocidades dos percursos nos 2 meios.

- Temos que o parametro $a$ (ver figura acima) depende de $\theta,\omega$. Sabemos que $\Delta z=\frac{d\phi_{r}}{d\beta}$. Assim, podemos dizzer que: $$a=f[ \phi_{r}(\theta,\omega) ]$$
- E temos então já uma resposta: "se Vg tem a ver com o número de colisões por unidade de comprimento no guia, porquê que esta varia com a frequência?"	
    - Como está indicado acima, $a$ depende de $\phi_{r}$. Por sua vez, $\phi_{r}\equiv \phi_{r}(\omega)$! 
    - Ao mudar a frequência muda a fase $\phi_{r}$ e, como vemos na condição modal, isto irá causar um $\theta_{m}$ diferente. 

#### Efeito Goos-Hãnchen
- Este é o nome do efeito em que o feixe se "desloca lateralmente" em cada reflexão:
![[reflexao nao é instantanea 2.png]]

## Guia 2D
- Até agora estudamos guias que são planos com espessura $d$. Consideremos agora um guia que é um prisma com largura e altura $d$:
![[modos permitidos guia 2D.png]]
- Como já vimos atrás: $\vec{k}=(k_{x},k_{y},\beta)~~,~~\cos\theta_{c}=\frac{n_{2}}{n_{1}}~~,~~ k_{x}^{2}+k_{y}^{2}\le n_{1}^{2}k_{0}^{2}\sin^{2}\theta_{c}$
- Agora, temos que $k_{x},k_{y}$ são definidos pelas condições de fronteira do guia.
- Notemos ainda que agora iremos ter modos $(m_{x},m_{y})$
- Temos que o número de modos $M$ agora é dado pelo número d epontos no quarto de circulo mais interno na figura acima.
    - Temos que: 
        - Área do quarto circulo: $\frac{1}{4}\pi (n_{1}k_{0}\sin\theta_{c})^{2}$
        - Área de 1 modo: $(\frac{\pi}{d})^2$ (assumimos que cada modo é um quadrado, como tracejado na figura)
    - Assim: $$M\approx \frac{\frac{1}{4}\pi (n_{1}k_{0}\sin\theta_{c})^{2}}{(\frac{\pi}{d})^{2}}=\frac{\pi}{4} \left(\frac{2d}{\lambda_{0}}\text{NA}\right)^{2}$$
- Ora, temos $M_{\text{1D}}\approx \frac{2d}{\lambda_{0}}\text{NA}$ logo:
$$M_{\text{2D}}\approx \frac{\pi}{4} M_{\text{1D}}^{2}~~\to~~M_{\text{2D}}\approx M_{\text{1D}}^{2}$$
notemos que $\frac{\pi}{4}\approx0.78$ :)

## Geometria de Guias
![[tipos de guia planar.png]]
nesta iamgem, azul mais claro representa um $n$ maior.

- Além destas geometrias de organização de materiais, podemos ter várias configurações. Por exemplo, para o modelo "embedded strip" temos:
![[sistemas integrados com guia planar.png]]

## Acoplamento ótico
- Temos radiação ótica a ser injetada na face de entrada de um guia
- Quando a radiação incidente tem um campo transverso com *distribuição igual* à de um certo modo -> APENAS esse modo é excitado
- Se tivermos uma distribuição qualqer -> VÁRIOS modos são excitados
- Assim, a transferência de potência para um modo $m$ depende da semelhança entre a distribuição de campo transverso. Como vimos atrás, esta é definida por $u_{m}(y)$

**Contas**
- Consideremos que o campo da *fonte* ótica é $s(y)$ e estamos a injetar o feixe num guia com base vetorial $u_{m}(y)$
- Podemos então projetar na base $$s(y)=\sum\limits_{m=1}^{M}a_{m}u_{m}(y)$$
em que o modo $\ell$ será excitado com amplitude:
$$a_{\ell}=\int_{-\infty}^{+\infty}s(y)u_{\ell}(y)dy$$

### Acoplamento experimental
- Na prática, o método mais óbvio é focar a radiação ótica na face de entrada. Isto é bom especialmente para excitar 1 modo só (pelo que deve ter o modo correto).
![[acoplamento de luz em guia.png]]

- Já no caso de excitar vários modos sem grande cuidado de quais, o que importa é garantir que a radiação incide dentro do cone definido pela NA:
![[acoplamento de luz em guia 2.png]]
em que sabemso que $\text{NA}=\sin\theta_{a}=n_{1}\sin\theta_{c}=\sqrt{n_{1}^{2}-n_{2}^{2}}$

### Acoplamente lateral
![[acoplamento lateral.png]]
- A lógica é que estamos a inserir o feixe no guia diretamente numa das reflexões, pelo que ele simplesmente se propaga a partir daí.
- Com este tipo de configuração, o objetivo é excitar um certo modo $m$ ao ajustar o ângulo $\theta_{i}$. 
- Conhecemos:
    - Constante de propagação - $\beta_{m}=n_{1}k_{0}\cos\theta_{m}$
    - Componente Z do k do campo incidente - $k_{iz}=n_{2}k_{0}\cos\theta_{i}$
- Ora, para haver acoplamento lateral temos que ter:
$$\begin{align*}
k_{iz}&= \beta_{m}\\
n_{1}k_{0}\cos\theta_{m}&= n_{2}k_{0}\cos\theta_{i}
\end{align*}$$
- Vimos que:
    - O valor máximo de $\beta_{m}$ é $n_{2}k_{0}$, quando $\theta_{m}=\theta_{c}$
    - É possível ter $k_{iz}=n_{2}k_{0}$, mas apenas com $\theta_{i}=0$. Ora, nesse ângulo não temos transmissão de potência para o guia
- Assim, este método só por si não permite excitar 1 modo.

### Acoplamento com prisma
![[acoplamento prisma.png]]
- Temos então reflexão total do feixe dentro do prisma, com um ângulo $\theta_{p}$.
- Vimos também que, neste caso, a reflexão na base do prisma não é instantanea - o feixe "desliza" para o lado antes de refletir.
    - Vimos que isto acontece porque o feixe passa um pouco para além da base.
    - Temos assim um campo evanescente abaixo do prisma
- Este campo evanescente terá de conseguir chegar ao guia, ou seja, atravesar a distância $d_{p}$
- Consideremos: $d_{p}<\lambda_{0}$ e $\beta_{p}=n_{p}k_{0}\cos\theta_{p}$
    - Ora, para ter acoplamento do modo $m$ consideremos: $\beta_{p}=\beta_{m}=n_{1}k_{0}\cos\theta_{m}$
- Assim resolvemos o nosso problema. Se $n_{p}\simeq n_{1}$. será bastante facil garantir acoplamento de 1 só modo!
- Ajustando $\theta_{i}$ (mantendo a condição de reflexão total no prisma), conseguiremos excitar todos os modos.

*Inverter*
- Vejamos agora a parte a ir para o Alvo, na figura
- O modo, ao bater na parede superior do guia, pode passar para o prisma e daí seguir para o alvo.
- Assim, cada modo irá sair do prisma com um ângulo específico. Veremos várias riscas no alvo, uma de cada modo.

### Acoplamento entre modos
- O que vimos agora foi tudo acoplamento de uma fonte externa a um certo modo
- Mas e se tivermos 2 guias, podemos acoplar modos um ao outro?
- Tal como no caso do prisma, basta termos 2 guias suficientemente próximos. Os campos evanescente de um entram no outro e temos acoplamento.
- A física funciona de forma semelhante à de pendulos acoplados.

**Contas**
- Consideremos então 2 guias a uma distância $2a$:
![[acoplamento entre modos.png]]
- O guia 1 é aquele com índice de refração e por aí adiante.
- Se estes guias estivessem "soltos" teríamos:
$$\begin{align*}
\text{Guia 1}:&&E_{1}(y,z)&= a_{1}u_{1}(y)e^{-i\beta_{1} z}\\
\text{Guia 2}:&&E_{2}(y,z)&= a_{2}u_{2}(y)e^{-i\beta_{2} z}
\end{align*}$$

### Interação Fraca
- Nesta situação:
    - $u_{1},u_{2},\beta_{1},\beta_{2}$ *não* se alteram
    - $a_{1},a_{2}$ variam *pouco* na escala de $\lambda_{0}$
- Por outras palavras, nesta interação que vemos na figura acima, apenas a amplitude dos modos muda.
- Temos que: (não sei se isto é deduzido ou empirico)
$$\begin{align*}
\frac{da_{1}}{dz}&= -i C_{21} e^{i\Delta\beta z}a_{2}(z)\\
\frac{da_{2}}{dz}&= -i C_{12} e^{-i\Delta\beta z}a_{1}(z)
\end{align*}$$
em que $\Delta \beta=\beta_{1}-\beta_{2}$. Ou seja, temos equações acopladas (quem diria???) que descrevem como $a_{1},a_{2}$ evoluem ao longo da propagação nos Z.

- Podemos definir estes coeficientes de acoplamento:
$$\begin{align*}
C_{12}&= \frac{1}{2}(n_{1}^{2}-n^{2}) \frac{k_{0}^{2}}{\beta_{2}}\int_{-a-d}^{-a}u_{2}(y)u_{1}(y)dy\\
C_{21}&= \frac{1}{2}(n_{2}^{2}-n^{2}) \frac{k_{0}^{2}}{\beta_{1}}\int_{a}^{a+d}u_{1}(y)u_{}(y)dy\\
\end{align*}$$
- Considerando as condições iniciais na figura acima: $a_{1}(z=0)=a_{1}(0)~,~a_{2}(z=0)=0$
- Combinando isto com as equações 
$$\begin{align*}
a_{1}(z)&= a_{1}(0)e^{i \frac{\Delta\beta z}{2}} \left(\cos\gamma z - i \frac{\Delta \beta}{2\gamma}\sin\gamma z \right)\\
a_{2}(z)&= a_{2}(0) \frac{C_{12}}{i\gamma} e^{-i \frac{\Delta\beta}{2}}\sin\gamma z
\end{align*}$$
em que $\gamma^{2}=(\frac{\Delta\beta}{2})^{2}+C^{2}~~~~,~~C=\sqrt{C_{12}C_{21}}$

- Uma vez que $E_{i}(y,z)=a_{i}(z)u_{i}(y)e^{-i\beta_{i} z}$, temos que a potência:
$$P_{i}(z)~~\propto~~ |a_{i}(z)|^{2}$$
- Logo, podemos definir:
$$\begin{align*}
P_{1}(z)&= P_{1}(0) \left[\cos^{2}(\gamma z) + \left(\frac{\Delta\beta}{2\gamma}\right)^{2} \sin^{2}(\gamma z) \right]\\
P_{2}(z)&= P_{1}(0) \frac{|C_{12}|^{2}}{\gamma^{2}}\sin^{2}(\gamma z)
\end{align*}$$

- Então, neste caso em que o guia 1 começa com amplitude alta e o guia 2 com amplitude nula temos:
![[acoplamento entre modos 2.png]]
ou seja, temos uma certa quantidade de potência trocar a alternar entre das 2 guias:
$$P_{1}(z)+P_{2}(z)=\text{constante}$$
- Notemos que nisto apenas uma porção da potência de $P_{1}$ é que passa para $P_{2}$, como vemos no gráfico.
- Podemos ver que quando $\Delta \beta$ é grande, então $\gamma^{2}=\frac{\Delta\beta^{2}}{2^{2}}+C^{2}$ também será elevado. Assim, $P_{2}$ será menor (temos um $\gamma^{2}$ no denominador).
    - Ou seja, temos um fraco acoplamento devido a uma elevada diferença nas constantes de propagação.

#### Guias iguais
- Neste caso temos $$n_{1}=n_{2}~~\to~~ \beta_{1m}=\beta_{2m}~~\to~~ \Delta \beta=0~~\longleftarrow \text{condição Phase-Matched}$$
e temos $C_{12}=C_{21}=C$
- Sabemos que $\Delta\beta$ elevado causa mau acoplamento. Por essa lógica, $\Delta \beta=0$ deve causar um acoplamento muito bom.
- Mais exatamente, temos:
$$\begin{align*}
P_{1}(z)&= P_{1}(0)\cos^{2}(Cz)\\
P_{2}(z)&= P_{1}(0)\sin^{2}(Cz)
\end{align*}$$
e vemos que ocorre total.

- Temos:
![[acoplamento entre modos 3.png]]
e vemos que a completa transferência da potência de uma fibra para outra ocorre em intervalos de distância $z=L_{0}=\frac{\pi}{2C}$
- Ao fazer uma medição da potência média em cada guia vemos que:
$$\overline{P_{1}}=\overline{P_{2}}=\frac{1}{2}P_{0}$$
ou seja, temos um **acoplador 50/50**!

#### Acoplador
- Consideremos um acoplador assim
![[coupler.png]]
- Consideremos que o acoplador tem comprimento fixo $L=L_{0}$ (o comprimento do acoplador é o comprimento da região de alta proximidade dos guias). Consideremos ainda que este acoplador tem $n_{1}=n_{2}$
- Consideremos que $P_{1}(z=0)=P_{1}(0)~~,~~~P_{2}(z=0)=0$, tal como vimos atrás
- Ora, como vimos acima, neste sistema a potência passa completamente de um guia para o outro em intervalos de $L_{0}$. Ora, sendo $L_{0}$ o comprimento do guia, iremos fazer apenas UMA troca:
$$P_{1}(z=L_{0})=0 \quad;\quad P_{2}(z=L_{0})=P_{1}(0)$$
- A potência passa para o outro guia!!!

**Fase**
- Para o guia 1, a diferença de fase induzida na propagação de distância $L_{0}$ é: $$\phi_\text{dist,1}=\beta_{m,1}L_{0}=n_{1}k_{0}\cos\theta_{m}L_{0}$$
- Ora, o índice de refração do guia 1 pode ser alterado pela aplicação de um campo E: $\beta_{m,1}\to\beta_{m,1}+\delta\beta_{m,1}$ e temos:
$$\frac{P_{2}(\beta_{m,1}+\delta\beta_{m,1})}{P_{1}(0)}=\frac{\sin^{2}\left[\frac{\pi}{2}\sqrt{1+ \left(\frac{L_{0}\delta\beta_{m,1}}{\pi}\right)^{2}} \right]}{\left(\sqrt{1+ \left(\frac{L_{0}\delta\beta_{m,1}}{\pi}\right)^{2}}\right)^{2}}$$
e assim, deixa de passar toda a potência para o guia 2.
- No entantooooo, se tivermos: $$L_{0}\delta\beta_{m,1}=\sqrt{3}\pi$$temos $\frac{P_{2}(\beta_{m,1}+\delta\beta_{m,1})}{P_{1}(0)}=0$, logo volta a passar a potência toda para o guia 1!
- Assim, controlando um campo elétrico no guia 1 com um sinal elétrico, podemos comutar a energia $\text{guia }1\to2$ e $2\to1$.
![[coupler 2.png]]