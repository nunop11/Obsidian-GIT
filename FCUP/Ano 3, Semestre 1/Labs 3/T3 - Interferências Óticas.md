# NOTAS do Protocolo
## 1 - Intro Teórica
### 1.1 - Ondas
- Interferência é um fenómeno muito comum que ocorre devido à sobreposição de ondas.
- Ondas eletromagnéticas mais simples são:
    - **Planas** - Amplitude e fase iguais em planos perpendiculares à direção de propagação
    - **Monocromáticas** - Descritas por uma função periódica sinusoidal
    - **Polarização Linear** - O vetor campo elétrico tem origentação constante
Uma onda dessas:
![[Attachments/FCUP/A3S1/LABS 3/onda EM.png]]
em que temos:
$$\vec{E}=E_{y}(x,t)\hat{y}=E_{0y} \hat{y} \cos(\omega t-kx+\phi)$$
em que temos $\lambda=vT \to v=\lambda/T=\lambda \nu$

- Em meios isotrópicos (que são iguais em todas as direções) temos que: 
$$v=\frac{c}{n} \quad \quad;\quad \quad\lambda=\frac{\lambda_{0}}{n}$$
em que $n$ é o índice de refração do meio.

### 1.2 - Difração
- Fenómeno que ocorre quando uma onda passa por uma abertura ou obstáculo pequeno e que não pode ser explicado por ótica geométrica.
- Ocorre quando uma frente de onda tem a sua amplitude ou fase alteradas devido à interação com um obstáculo.
- Na teoria não há diferença, mas na prática:
    - Interferência - Quando temos um nº de ondas, $N$, reduzido.
    - Difração - Quando temos $N\to\infty$

**Princípio de Huygens**
Cada ponto de uma frente de onda não obstruída constitui, em qualquer instante, uma fonte de ondas esféricas secundárias (com a mesma frequência da onda primária). Deste modo, a amplitude do campo ótico em qualquer ponto do espaço resulta da sobreposição de todas essas ondas (tendo em conta as suas amplitudes e fases relativas).

## 2 - Inferómetro Michelson
- Inferómetro - Instrumento que permite realizar interferências entre 2+ ondas, de forma controlada. Isto pode ser usado para medir ângulos, distâncias, espetroscopia, etc.
Interferómetro Michelson:
![[inferometro michelson 1.png]]
(M1, M2 são espelhos, O é o divisor de onda, C a lâmina de compensação e D o detetor)

- A parte do feixe que vai a $M_{2}$ atravessa o refletor mais vezes, pelo que se mete $C$ para equilibrar, que deverá ter a mesma espessura que $O$. No entanto, a espessura de $O$ não tem qualquer efeito sobre o feixe, tornando-se a introdução de $C$ desnecessária. Este deverá ser o caso da experiência que iremos realizar :)

## 2.1 - Interferência entre 2 ondas esféricas
- O padrão de interferência que se observa no detetor é equivalente a ter 2 fontes esféricas nos espelhos $M_{1},M_{2}$. Ou seja:
![[inferometro michelson 2.png|500]]
em que $S_{1},S_{2}$ são 2 fontes virtuais, tais que:
$$\begin{align*}
s_{1}=2L_{1}+L_{f}+L_{a}\\
s_{2}=2L_{2}+L_{f}+L_{a} 
\end{align*}\tag{Eq.1}$$
- Desde que $s_{2}-s_{1}$ não seja demasiado elevado, temos que quando as 2 ondas chegam a $D$ têm a mesma direção. Assim, podemos tratar o problema de forma escalar, tal que:
$$E=E_{1}+E_{2}=E_{01}(r_{1})\cos(\omega t-k r_{1}) + E_{02}(r_{2}+\phi_{1})\cos(\omega t-k r_{2}+\phi_{2})$$
- Devido à elevada frequência ótica das ondas eletromagnéticas, que não são detetadas pelos fotodetetores atuais, o que importa nesta atividade é a intensidade das ondas, o valor médio temporal do vetor Poyting: $$I_{1}\equiv \langle P_{1}\rangle=v \varepsilon \langle E_{1}^{2}\rangle \quad \quad;\quad \quad I_{2}\equiv \langle P_{2}\rangle=v \varepsilon \langle E_{2}^{2}\rangle$$
no entanto, só importam as intensidades relativas, pelo que podemos considerar:
$$I_{1}=\langle E_{1}^{2}\rangle \quad \quad;\quad \quad I_{2}=\langle E_{2}^{2}\rangle$$
- No plano do detetor ($D$) temos:
$$I = \langle E^{2}\rangle=\langle(E_{1}+E_{2})^{2}\rangle=\langle E_{1}^{2}\rangle+\langle E_{2}^{2}\rangle + 2 \langle E_{1}E_{2}\rangle$$
e podemos escrever:
$$\langle E_{1}^{2}\rangle=\frac{E_{01}(r_{1})}{2}=I_{1}(r_{1}) \quad;\quad \langle E_{2}^{2}\rangle=\frac{E_{02}(r_{2})}{2}=I_{2}(r_{2})$$
$$2\langle E_{1}E_{2}\rangle = E_{01}(r_{1})E_{02}(r_{2})\cos[k(r_{1}-r_{2}) +(\phi_{1}-\phi_{2})]$$
em que $E_{01}(r_{1})=\sqrt{2I_{1}(r_{1})}~~,~~E_{02}(r_{2})=\sqrt{2I_{2}(r_{2})}$. Logo:
$$I=I_{1}(r_{1})+I_{2}(r_{2})+2\sqrt{I_{1}(r_{1})I_{2}(r_{2})}\cos[k(r_{1}-r_{2}) +(\phi_{1}-\phi_{2})]$$
- Se considerarmos que $E_{01},E_{02}$ são aproximadamente constantes no detetor $D$ (uma vez que, conforme a figura acima $R\ll r_{1},r_{2}$) temos $I_{1}\approx I_{2}=I_{0}$, logo:
$$I\simeq 2I_{0}[1+\cos[k(r_{1}-r_{2}) +(\phi_{1}-\phi_{2})]]$$
e podemos definir:
$$I\simeq 4I_{0}\cos^{2}\left(\frac{\delta}{2}\right) \quad;\quad \delta=k(r_{1}-r_{2}) +(\phi_{1}-\phi_{2}) \tag{Eq. 2}$$
o que nos dá:
$$I_{max}\simeq 4I_{0} \to \delta=2\pi m ~~~~;~~~~ m=\dots,-2,-1,0,1,2,\dots$$
$$I_{min}\simeq 0 \to \delta=(2m + 1)\pi ~~~~;~~~~ m=\dots,-2,-1,0,1,2,\dots$$
## 2.2 - Evolução das franjas de interferência com variação do caminho ótico
- Consideremos que $\phi_{1}=\phi_{2}$ e da Eq. 2 temos:
$$\delta = k(r_{1}-r_{2})=\frac{2\pi}{\lambda} (r_{1}-r_{2})=\frac{2\pi n}{\lambda_{0}}(r_{1}-r_{2}) \tag{Eq. 3}$$
(indo buscar a equação $\lambda=\frac{\lambda_{0}}{n}$ que nos dá o comprimento de onda para um meio que não o vácuo)
- Com esta igualdade, se conseguirmos determinar $\delta$ para um certo $(r_{1}-r_{2})$ conseguimos obter o índice de refração do meio.
- Por outro lado, se mantermos $(r_{1}-r_{2})$ constante variarmos o $n$, a variação de $\delta$ permite determinar a variação de $n$.

### 2.2.1 - Determinação de $n$ do ar - método 1
![[inferometro michelson 3.png|525]]  |||  ![[inferometro michelson 2.png|500]]
- Consideremos que o ponto $P$ está muito próximo do centro do eixo de simetria das ondas observadas no plano $D$ (ou seja: $R$ muito reduzido). Isto faz com que $r_{1}-r_{2}\sim s_{1}-s_{2}=2(L_{1}-L_{2})=2\Delta L$ (ver Eq.1). A partir da Eq.3 isto dá-nos:
$$\delta= \frac{4\pi n_{a}}{\lambda_{0}} \Delta L$$
ora, na prática, isto significa que no centro do alvo ($R$ muito reduzido) tivermos um máximo de intensidade temos $\delta=2\pi m$. Caso contrário temos $\delta=(2m + 1)\pi$. Assim, para passarmos de ter um máximo no centro para voltar a ter um máximo no centro, $\delta$ tem que variar $2\pi$. Isto ocorre quando $\Delta L= \frac{\lambda_{0}}{2n_{a}}$. Como no inferómetro que teremos no lab apenas 1 espelho se move (consideremos o espelho 1) consideremos que este valor de $\Delta L$ que causa $\Delta \delta=2\pi$ é $\Delta d_{|2\pi}=\frac{\lambda_{0}}{2n_{a}}$. Assim temos:
$$2\pi=\frac{4\pi n_{a}}{\lambda_{0}}\Delta d_{|2\pi}\to n_{a}=\frac{\lambda_{0}}{2\Delta d_{|2\pi}}$$
    - De forma mais geral, se ao variar a posição do espelho 1 uma distância $\Delta d$ passamos por $N$ máximos (ou mínimos, se inicialmente tínhamos um mínimo no centro) temos a fórmula:
$$\boxed{n_{a}=\frac{N \lambda_{0}}{2 \Delta d_{|N}}}\tag{Eq. 4}$$

### 2.2.2 - Determinação de $n$ do ar - método 2
- Veremos agora como se pode determinar $n_{a}$ conforme varia a pressão do ar.
- Usaremos uma célula com paredes de vidro em que a pressão no interior pode ser manipulada. Iremos variá-la de quase vácuo ($p\simeq0$) até pressão atmosférica ($p\simeq p_{atm}$). Assim ficamos com $n_{a}=n_{a}(p)$, tal que $n_{a}(p\simeq0)=1~~,~~n_{a}(p\simeq p_{atm})=n_{a|atm}$ 
- Ora, se a pressão não for muito elevada, $n_{a}$ aumenta linearmente com a pressão:
$$n_{a}(p)=n_{a}(p\simeq0)+\left(\frac{\Delta n_{a}}{\Delta p}\right)p\approx 1 + \left(\frac{\Delta n_{a}}{\Delta p}\right)p$$
ou seja: $n_{a|atm}(p)\approx 1 + \left(\frac{\Delta n_{a}}{\Delta p}\right)p_{atm}$. Ou seja, o fator que precisamos de obter é o declive da reta $n_{a}(p)$, pelo que quando $p=p_{atm}$ a equação acima dá-nos $n_{a|atm}$

- Assim:
    1. Colocamos a célula de pressão variável no ramo do espelho 1, perpendicular à direção do espelho.
    2. Colocar $p\simeq0$ e ajustar a posição do espelho 1 de forma que esteja um máximo no centro do alvo.
    3. Aumentar a pressão gradualmente até $p=p_{atm}$ e contar o número de passagens claro-escuro-claro ($N$).

- Assim, temos $\Delta p=p_{atm}$ pelo que $\Delta x=N \lambda_{0}$. Assim: $$\frac{\Delta x}{\Delta p}=\frac{N}{p_{atm}} \lambda_{0}$$
- Temos ainda que $\Delta x=2 d_{c} \Delta n_{a}$ pelo que: $$\frac{\Delta x}{\Delta p}=2 d_{c} \frac{\Delta n_{a}}{\Delta p}$$
- Juntando as 2 equações acima temos:
$$\frac{\Delta n_{a}}{\Delta p}=\frac{N\lambda_{0}}{2d_{c}p_{atm}}$$
ao substituir em $n_{a|atm}(p)\approx 1 + \left(\frac{\Delta n_{a}}{\Delta p}\right)p_{atm}$ obtemos:
$$\boxed{n_{a|atm}\approx 1+ \frac{\lambda_{0}N}{2d_{c}}}\tag{Eq. 5}$$

### 2.2.3 - Determinação do $n$ do vidro
![[refração vidro rodado.png]]
- Colocamos uma lâmina de vidro entre o divisor e o espelho 1.
- Começamos com a lâmina perpendicular ao feixe: $i=0^{º}$. Neste caso, o feixe percorre $h$ dentro do vidro e $C$ no ar. 
- Se tivermos $i\neq0^{º}$, no vidro o feixe percorre $h'$ e $C+\Delta D_{a}$ no ar. Mais especificamente, no vidro, a variação do percurso é: $h'=h+\Delta D_{v}$ em que (conforme a figura acima): $$\Delta D_{v}=h\left(\frac{1}{\cos r}-1\right)$$
como $\cos r=\sqrt{1-\sin^{2}r}$ e $\sin r=\frac{n_{a}}{n_{v}}\sin i$ obtemos: $$\Delta D_{v}=h\left(\frac{1}{\cos r}-1\right)=h\left[\frac{1}{\sqrt{1-\left(\frac{n_{a}}{n_{v}}\sin i\right)^{2}}}\right]\approx \frac{h}{2} \left(\frac{n_{a}}{n_{v}}\right)^{2}\sin^{2}i$$
(da 2º para 3º igualdade usou-se a expansão em série de Taylor de $\frac{1}{\sqrt{1-x^{2}}}$)

- Considerando $\Delta d_{|N}=\Delta D_{v}$ na Eq.4 obtemos:
$$N_{v}=\frac{h}{\lambda_{0}} \frac{n_{a}^{2}}{n_{v}} \sin^{2}i$$
em que $N_{v}$ é o número de alternâncias claro-escuro-claro que se observa ao variar o percurso da luz no vidro uma distância $\Delta D_{v}$.
- A correspondente variação do caminho no ar é dada por:
$$\Delta D_{a}=h-h'\cos(i-r)=h\left[1-\frac{\cos(i-r)}{\cos r}\right]\approx h\left(\frac{1}{2}- \frac{n_{a}}{n_{v}}\right)\sin^{2}i$$
em que a última parte foi obtida usando série de Taylor e magia.

- Considerando $\Delta d_{|N}=\Delta D_{a}$ na Eq.4 obtemos:
$$N_{a}=\frac{h}{\lambda_{0}} \left(n_{a}-2 \frac{n_{a}^{2}}{n_{v}}\right) \sin^{2}i$$
em que $N_{a}$ é o número de alternâncias claro-escuro-claro que se observa ao variar o percurso da luz no ar uma distância $\Delta D_{a}$.

- Assim, ao variar o ângulo entre a perpendicular da lâmina e o eixo do feixe de $0^{º}$ até $i$ teremos $N$ alternâncias claro-escuro-claro no centro do alvo:
$$N=N_{a}+N_{v}=\frac{h}{\lambda_{0}} \left(n_{a}- \frac{n^{2}_{a}}{n_{v}}\right)\sin^{2}i$$
pelo que conseguimos obter a equação que nos dá o coeficiente de refração do vidro com o ângulo $i$ e o número de alternâncias $N$:
$$\boxed{ n_{v}=\frac{h n_{a}^{2}\sin^{2}i}{h n_{a} \sin^{2}i-N\lambda_{0}} }\tag{Eq. 6}$$

## 3 - Difração da Luz
### 3.1 - Considerações Gerais
![[difraçao.png]]
- Consideremos que temos um caso como acima (luz a vir da esquerda e a passar na abertura, onde sofre difração) e queremos determinar a intensidade luminosa no ponto $P$.
- Usando o princípio de Huygens, cada elemento infinitesimal de área $dS$ age como uma fonte pontual de ondas esféricas que se propagam até ao ponto $P$, onde gera um campo elétrico com módulo dado por:
$$dE=\frac{E_{a}}{r} e^{i(\omega t-kr)}dS\tag{Eq. 7}$$
(em que $E_{a}$ é o módulo do campo na abertura, onde consideramos o campo constante)

- Considerando que $dS=(0,y,z)$ e $P=(X,Y,Z)$. A distância entre eles é $$r=\sqrt{X^{2}+(Y-y)^{2}+(Z-z)^{2}}$$
- Se considerarmos que $P$ está suficientemente longe da abertura temos $r\sim R$. Isto é uma boa aproximação no denominador da fração $\frac{E_{a}}{r}$ na equação de $dE$ acima. Mas no termo $kr$ do expoente, essa aproximação é péssima, porque $k=\frac{2\pi}{\lambda}$ será um valor alto, pelo que o erro da aproximação $r\sim R$ será significativo. Assim, sendo $R=\sqrt{X^{2}+Y^{2}+Z^{2}}$ ficamos com:
$$r=R \sqrt{1 + \frac{y^{2}+z^{2}}{R^{2}} -2 \frac{Yy+Zz}{R^{2}}}\approx\sqrt{1 -2 \frac{Yy+Zz}{R^{2}}}$$
(a última parte vem de $R\gg y,z$ logo $\frac{y^{2}+z^{2}}{R^{2}}\to0$)

- A partir da expansão em série de Taylor:
$$r\approx R\left(1- \frac{Yy+Zz}{R^{2}}\right)=R- \frac{Yy+Zz}{R}=- \left(-R + \frac{Yy+Zz}{R}\right)$$
o que, ao substituir na equação de $dE$ nos dá: $dE= \frac{E_{a}}{R} e^{i(\omega T-kR)} e^{ik \frac{Yy+Zz}{R}} dS$. Isto resulta em:
$$\boxed{ E(P,t)=\frac{E_{a}}{R} e^{i(\omega t-kR)}\int_\textsf{abertura} e^{ik \frac{Yy+Zz}{R}}dS }\tag{Eq. 8}$$

### 3.2 - Padrão de Interferência de Fenda
- Consideremos uma fenda muito comprida, com largura $b$. Temos abaixo a vista transversal:
![[difracao fenda linear.png]]
- Aqui é mais útil usar a Eq. 8, já que o integral de fontes não é de área, mas sim em 1 dimensão. Temos:
$$dE= \frac{E_{a}}{r} e^{i(\omega t-kr)}dy_{a}$$
- Tal como na secção atrás, $r\simeq R$ é uma boa aproximação no denominador, mas não no expoente. Aí, conforme a figura acima (aproximação na esquina inferior direita) podemos considerar que $r\parallel R$ e temos: $r \approx R-y_{a}\sin\theta$. Assim podemos substituir estas aproximações na Eq.8 e considerar apenas a parte imaginária e temos: $dE= \frac{E_{a}}{R} \sin(\omega t-k(R-y_{a}\sin\theta))dy_{a}$
- Ao integrar na abertura ($\int_{-b/2}^{+b/2}$) obtemos:
$$E(P,t)=\frac{E_{a}b}{R} \frac{\sin\left( k \frac{b}{2}\sin \theta \right)}{k \frac{b}{2}\sin \theta} \sin(\omega t - kR)$$
definimos
$$\beta\equiv k \frac{b}{2}\sin \theta= \frac{2\pi}{\lambda} \frac{b}{2}\sin\theta=\frac{\pi nb}{\lambda_{0}}\sin\theta$$
($\lambda_{0}$ é o compriemndo de onda no vácuo e $n$ o índice de refração do meio) 
e ficamos com:
$$E(P,t)=\frac{E_{a}b}{R} \frac{\sin\beta}{\beta} \sin(\omega t-kR)$$

- A intensidade da radiação em $P$ é dada por $I(P)=v \varepsilon \langle E^{2}(P,t)\rangle$ ($v$ é a velocidade da luz e $\varepsilon$ a permitividade elétrica do meio). Sendo $\langle \sin^{2}(\omega t-kR)\rangle=\frac12$ temos:
$$I(P)= \frac12 \left(\frac{E_{a}v\varepsilon b}{R}\right)^{2} \left(\frac{\sin\beta}{\beta}\right)^{2}\equiv I_{0}\text{sinc}\beta \quad \quad; \quad \quad I_{0}\equiv \frac12 \left(\frac{E_{a}v\varepsilon b}{R}\right)^{2}$$
isto já nos permite entender onde teremos máximos e mínimos da onda e etc:
![[difracao fenda linear - padrao.png]]
sendo que os mínimos ocorrem quando $$\beta=\frac{\pi n b}{\lambda_{0}}\sin \theta=m \pi \to \sin \theta= \frac{\lambda_{0}}{nb}m ~~~~,~~~~ m=\pm1,\pm2,\dots$$
- Assim, os primeiros mínimos aparecem em $m=\pm1$, ou seja $\sin\theta_{\pm1}=\pm \frac{\lambda_{0}}{nb}$. Ou seja, não temos mínimos se $|\theta_{\pm1}|\ge 90^{º}$. Assim, não ocorre difração quando: $\lambda_{0}\ge nb$

- Conforme a primeira figura desta secção: $\tan \theta=\frac{Y_{P}}{d}$. Ora, se o ângulo $\theta$ for reduzido temos $\sin \theta\sim \tan \theta\sim \theta\sim Y_{P}/d$. Ou seja temos 2 igualdades:
$$\sin \theta=\frac{Y_{P}}{d}=\frac{\lambda_{0}}{nb}m\to \boxed{b=m \frac{d \lambda_{0}}{n Y_{min|m}}~~,~~m=\pm1,\pm2,\dots }\tag{Eq. 9}$$
medindo a distância ao centro de um mínimo ($Y_{min|m}$) e sabendo o número do mínimo ($m$) conseguimos então obter a largura da fenda ($b$).

### 3.3 - Padrão de Interferência de um Fio
![[difracao fio.png]]
- Devido a razões muito bem explicadas no protocolo, este caso tem uma "fenda" complementar à da secção atrás. Assim, o comportamento da onda é igual, pelo que podemos obter a espessura do fio usando a Eq. 9.

### 3.4 - Padrão de Interferência de Abertura Circular
![[difracao abertura circular.png]]
em que começamos por colocar o problema em coordenadas esféricas (imaginar o plano $xOy$ com o ângulo $\phi/\Phi$ nos planos da abertura e de observação):
$$\begin{align*}
z=\rho\cos \phi \quad \quad \quad \quad Z=q\cos \Phi\\
y=\rho\sin \phi \quad \quad \quad \quad Y=q\sin \Phi\\
\end{align*}$$
e temos:
$$dS = \rho ~d \rho d \phi$$
e ficamos com
$$E(P,t)=\frac{E_{a} e^{i(\omega t-kR)}}{R} \int_{0}^{a} \int_{0}^{2\pi} e^{i \frac{k\rho q}{R} \cos(\phi-\Phi)} \rho ~d \phi d \rho$$
- Ora, acontece que a função a ser integrada não pode ser simplificada, pelo que temos uma famigerada **função de Bessel** (de primeira espécie de ordem zero):
$$J_{0}(u)=\frac{1}{2\pi} \int_{0}^{2\pi} e^{i u\cos \nu}d \nu$$
e reescrevemos o integral acima como:
$$E(P_{|\Phi=0},t)=\frac{E_{a} e^{i(\omega t-kR)}}{R} 2\pi \int_{0}^{a} J_{0}\left(\frac{k\rho q}{R}\right) \rho~d \rho$$
- De seguida faz-se uma passagem a função de Bessel para ordem 1 e mudança de variável e obtemos:
$$E(P_{|\Phi=0},t)=\frac{E_{a} e^{i(\omega t-kR)}}{R} 2\pi a^{2} \left[\frac{J_{1}\left(\frac{kaq}{R}\right)}{\frac{kaq}{R}}\right]=\frac{2E_{a}A e^{i(\omega t-kR)}}{R} \left[\frac{J_{1}\left(\frac{kaq}{R}\right)}{\frac{kaq}{R}}\right]$$
em que $A=\pi a^{2}$ é a área da abertura.
- Conseguimos ainda obter:
$$I(P_{|\Phi=0})=\frac{2 v \varepsilon A^{2} E_{0}^{2}}{R^{2}}\left[\frac{J_{1}\left(\frac{kaq}{R}\right)}{\frac{kaq}{R}}\right]^{2}$$
sendo que no centro do alvo temos $q=0$ logo:
$$I(P_{|\Phi=0},q=0)=\frac{v\varepsilon A^{2}E_{0}^{2}}{2R^{2}}\equiv I_{0}$$
e podemos escrever a intensidade da onda incidente no alvo a uma distância $q$ do centro como:
$$I(q)=I_{0} \left[\frac{2J_{1}\left(\frac{kaq}{R}\right)}{\frac{kaq}{R}}\right]^{2}=I_{0} \left[ \frac{2J_{1}(ka \sin\theta)}{k a \sin \theta}\right]^{2} $$
- O primeiro zero da função irá aperecer quando:
$$J_{1}(k a \sin\theta)=0\to \frac{2\pi}{\lambda}a\sin \theta=3,83\to \sin \theta\approx \theta=1,22 \frac{\lambda}{D}$$
em que $D=2a$ AKA diâmetro da abertura.

- Conforme a figura no início desta secção vemos que $\tan \theta=q/d$. Ora, considerando especificamente o 1º zero da função Intensidade temos:
$$\tan \theta_{pz}=\frac{q_{pz}}{d}\approx\sin\theta_{pz}$$
(em que $q_{pz}=q_{\textsf{primeiro zero}}$)
Ora, indo acima vemos que um zero da função ocorre quando $k a \sin\theta=3,83$. Ficamos então com:
$$k a \frac{q_{pz}}{d}=\frac{2\pi n}{\lambda_{0}} a \frac{q_{pz}}{d}=3,83$$
e obtemos a fórmula que nos permite estimar o diâmetro da fenda sabendo a distância do 1º zero ao centro do padrão de interferência:
$$\boxed{D=1,22 \frac{\lambda_{0}}{n} \frac{d}{q_{pz}}}\tag{Eq. 10}$$
sendo que, usando o 2º e 3º zeros da função de Bessel de ordem um temos:
$$D=2,23 \frac{\lambda_{0}}{n} \frac{d}{q_{sz}}$$
$$D=3,24 \frac{\lambda_{0}}{n} \frac{d}{q_{tz}}$$
(em que $q_{sz}=q_\textsf{segundo zero}$ e $q_{tz}=q_\textsf{terceiro zero}$)

- Calculamos ainda para o 4º zero e temos:
$$D_{|quarto~zero}=4,24 \frac{\lambda_{0}}{n} \frac{d}{q_{quarto~zero}}$$

**Duas Fontes**
- Até aqui, vimos o caso de a fonte estar alinhada com o eixo central da abertura, pelo que o padrão de interferência também o estará.
- Se a fonte estivesse desviada um ângulo $\varphi$ do eixo central, o padrão de interferência também o estará, para do lado oposto (ver figura abaixo)
- Ora, imaginemos agora que temos 2 fontes, ambas desviadas um ângulo $\varphi$ do eixo central, mas de lados opostos:
![[difracao 2 fontes.png]]
- Ora, prestemos então atenção ao parâmetro $\varphi_{min}$ que diz a separação mínima entre as 2 fontes (como mostrado na figura acima) para que os padrões de interferência das 2 fontes sejam distinguíveis.
- Ora, a separação mínima será aquela em que o máximo principal de 1 fonte coincide com o 1º mínimo da outra. Assim, como $\varphi_{min}=\theta_{pz}$ obtemos:
$$\boxed{\varphi_{min}=1,22 \frac{\lambda_{0}}{nD}}\tag{Eq. 11}$$

## 4 - Execução
