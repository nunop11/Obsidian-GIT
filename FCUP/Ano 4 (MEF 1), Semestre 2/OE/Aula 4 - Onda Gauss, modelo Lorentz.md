### Campo paraxial
- Um campo ótico é *paraxial* se os vetores normais à frente de onda fazer ângulos muito pequenos com o eixo de propagação. Ou seja, é um campo que se propaga (quase) como uma onda plana.
- Ou seja, vejamos ondas quase planas
- Para definir um campo deste tipo, podemos começar por definir uma onda plana que se propaga no eixo $z$: $$U(z)=A(z) e^{-ikz}$$
    - Definimos $A(z)$ uma função que varia lentamente com $z$
- Mas este campo cumpre a equação de Hemholtz? 
- Se substituirmos $U(z)$ em $\nabla^{2}_{T}U + k^{2}U=0$, obtemos:
$$\nabla_{T}^{2}A(\vec{r}) - i2k \partial_{z}A(\vec{r})=0$$
e esta é a **equação de Helmholtz em regime paraxial**.
- A solução mais simples desta nova equação é a *onda paraboidal*:
$$A(\vec{r})_\text{parab}=\frac{A_{1}}{z}e^{-ik \frac{x^{2}+y^{2}}{2z}} ~~\to~~ U(\vec{r})_\text{parab}\frac{A_{1}}{z}e^{-ik \frac{x^{2}+y^{2}}{2z}} e^{-ikz}$$
e notemos que estamos em regime paraxial se $x,y\ll z$.

**ZETA**
- Outra solução da eq Helmholtz paraxial resulta de fazer a transformação $$z\to z-\zeta$$
e fica
$$A(\vec{r})_\text{parab}=\frac{A_{1}}{q(z)}e^{-ik \frac{x^{2}+y^{2}}{2q(z)}}~~~~;~~ q(z)=z-\zeta$$
- Ora, isto não passa de uma onda paraboidal centrada em $z=\zeta$ invés de $z=0$.

## Gaussiana!
- Ok, imaginemos agora que $\zeta$ é *complexo*. Ora, a equação de Helmholtz continua a aplicar-se. Ou seja, usar $\zeta$ complexo não tem nada de errado, mas irá alterar bastante as propriedades!
- Ora, se definirmos especificamente: $$\zeta=-iz_{0}$$
temos uma _**ONDA GAUSSIANA**_.

- Por conveniência, definimos:
$$A(\vec{r})_\text{gauss} = \frac{A_{1}}{q(z)} e^{-ik \frac{\rho^{2}}{2q(z)}}$$
em que, claro: $q(z)=z+iz_{0} ~~;~~ \rho^{2}=x^{2}+y^{2}$. A $\rho$ podemos chamar "distância ao eixo de propagação".
- Para verdadeiramente entender este tipo de onda, é útil escrever na forma:
$$\frac{1}{q(z)}= \frac{1}{z+iz_{0}} = \frac{1}{R(z)} -i \frac{\lambda}{\pi W^{2}(z)}$$
e temos:
$$R(z)=z \left[1 + \left(\frac{z_{0}}{z}\right)^{2} \right] \quad;\quad W(z)=W_{0} \sqrt{1+ \left(\frac{z}{z_{0}}\right)^{2}} ~~,~~ W_{0}=\sqrt{\frac{\lambda z_{0}}{\pi}}$$
- Ou seja, podemos escrever:
$$\boxed{U(\vec{r})_\text{gauss} = A_{0} \frac{W_{0}}{W(z)} e^{\frac{-\rho^{2}}{W^{2}(z)}}e^{-ikz - ik \frac{\rho^{2}}{2R(z)} + i\zeta(z)}}$$
(confia, não deduzas)
Temos ainda: $$A_{0}=\frac{A_{1}}{iz_{0}}\quad;\quad \zeta(z)=\arctan \left(\frac{z}{z_{0}} \right)$$
- Os parâmetros independentes desta equação são: $\lambda, A_{0} (\text{ou }A_{1}), z_{0}$.
### Intensidade
- Temos então:
$$\overline{I}=\frac{|U|^{2}}{2\eta}=\frac{\left| A_{0} \frac{W_{0}}{W(z)} e^{\frac{-\rho^{2}}{W^{2}(z)}}e^{-ikz - ik \frac{\rho^{2}}{2R(z)} + i\zeta(z)}\right|}{2\eta}=I_{0} \left[\frac{W_{0}}{W(z)} \right]^{2}e^{\frac{-2\rho^{2}}{W(z)}} $$
em que $\rho^{2}=x^{2}+y^{2}$ é a distância que vai do ponto ao eixo de propagação ($z$). Definimos: $I_{0}=\frac{|A_{0}|^{2}}{2\eta}$
- Ou seja, relativamente ao eixo de propagação, temos um perfil de densidade **gaussiano**!

![[intensidade gauss.png]]

- Em torno do eixo dos ZZ temos $\rho=0$ logo:
$$I(0,z)_\text{gauss}= \frac{I_{0}}{1 + \left(\frac{z}{z_{0}}\right)^{2}}$$
![[intensidade gauss 2.png]]
e vemos que longe da fonte ($z\gg z_{0}$) temos $I\simeq \frac{I_{0}z_{0}^{2}}{z^{2}}$. Ou seja, longe da fonte, a intensidade cai com o quadrado da distância - como numa onda esférica ou parabólica.

### Potência
- Integramos a intensidade média no plano transverso:
$$P=\int_{0}^{\infty}\overline{I}(\rho,z)dS$$
obtemos:
$$P=\frac{\pi}{2}I_{0}W_{0}^{2} ~~\to ~~ I_{0}=\frac{2P}{\pi W_{0}^{2}}$$
- Notemos que a potência é determinada assim porque *intensidade é:* "Quantidade energia que temos, por unidade de tempo, a passar numa unidade de área transversa". Por outras palavras: "Potência que passa por uma unidade de área transversa".
- Ou seja, podemos escrever:
$$\overline{I}(\rho,z)=\frac{2P}{\pi W^{2}(z)}e^{- \frac{2\rho^{2}}{W^{2}(z)}}$$

- Definimos a fração da potência que existe até uma distância radial $\rho_{0}$ do eixo de propagação:
$$\eta_{|\rho=\rho_{0}}=\frac{1}{P}\int_{0}^{\rho_{0}}\overline{I}(\rho,z) 2\pi \rho d\rho = 1 - e^{- \frac{2\rho_{0}^{2}}{W^{2}(z)}}$$
- Podemos então ver que:
    - Se $\rho=W(z)$ então temos $\eta=0.86P$ -- 86% da energia do feixe encontra-se num círculo transverso de raio $W(z)$, num certo ponto $z$ 
    - Se $\rho=1.5W(z)$ então temos $\eta=0.99P$

### $W(z)$
- Ou seja, $W(z)$ é um ótimo indicador da largura do feixe. Como $W(z)=W_{0}\sqrt{1+(\frac{z}{z_{0}})^{2}}$, vemos que o feixe vai-se alargando consoante se propaga.
    - Podemos pensar no $W$ como sendo uma espécie de desvio padrão para o perfil gaussiano.
    - Podemos até fazer o gráfico de $W(z)$:
![[W gauss.png]]
e temos uma informação importante: $$W(\pm z_{0})=\sqrt{2}W_{0}$$
**Nomenclaturas**
- Temos:
    - $W_{0}$ : Beam Waist
    - $2W_{0}$ : Spot Size

- Podemos ver que $W$ varia de forma quase linear consoante $z$ aumenta e torna-se mais linear para valores maiores.
- Podemos então aproximar para $z\gg z_{0}$: $$\theta_{0}=\frac{W_{0}}{z_{0}}~~\to~~W(z)\approx \theta_{0}z$$
- Temos: $$\theta_{0}=\frac{4}{\pi}\frac{2\lambda}{W_{0}}= \frac{4}{\pi} \cdot \frac{\lambda}{2W_{0}}$$
- Assim, quanto menor $\theta_{0}$ mais "focado" será o nosso foco (o feixe alarga-se menos).
    - Ora, este é proporcional a $\lambda$ logo podemos reduzir a sua largura ao reduzir o comprimento de onda
    - Mas, na maioria dos casos queremos *ter* um certo comprimento de onda. Assim, queremos reduzir acima de tudo o spot size ($2W_{0}$)

**Distância de foco**
- A distância (ou profundidade) de foco é muito importante em algumas aplicações de ondas gaussianas.
- Em $z=0$ temos o feixe mais "focado" possível. A partir daí, ele alarfa como vimos assim. 
- Assim, a distância de foco é o comprimento $\ell_{foco}$ em que: $$\text{largura onda}<\sqrt{2}W_{0}=\sqrt{2} \sqrt{\frac{\lambda z_{0}}{\pi}}$$
- E temos:
$$W\left(z=\frac{1}{2}\ell_{foco}\right) = W_{0} \sqrt{1+ \left(\frac{\ell_{foco}}{2z_{0}}\right)^{2}}=\sqrt{ W_{0}}$$
ou seja, temos que 
$$\ell_{foco}=2z_{0}$$
(não sei porque fazemos $z=\frac{1}{2}\ell_{foco}$)
![[dist foco gauss.png]]

- Ou seja, temos que fazer um equilíbrio entre reduzir: spot size, profundidade de foco e comprimento de onda.

**Fase**
- Podemos escrever:
$$U(\vec{r})= A_{0} \frac{W_{0}}{W(z)}e^{\frac{-\rho^{2}}{W^{2}(z)}}e^{-ikz- ik\frac{\rho^{2}}{2R}+ i \zeta(z)}=\left[A_{0} \frac{W_{0}}{W(z)} e^{\frac{-\rho^{2}}{W^{2}(z)}} \right]e^{-i\varphi(\rho,z)}$$
em que temos a *fase do campo ótico gaussiano*:
$$\varphi(\rho,z)=kz-\zeta(z) + \frac{k\rho^{2}}{2R(z)}$$

- Quando estamos no eixo de propagação (eixo dos ZZ) temos $\rho=0$ logo ficamos com: $\varphi(0,z)=kz- \zeta(z)$
    - $kz$ - fase de um onda plana
    - $\zeta(z)$ - desvio de fase, relativamente à fase de uma onda de plana

**Frente de onda**
- Acabamos de ver que a fase de uma onda gaussiana é dada por: $\varphi(\rho,z)=kz-\zeta(z) + \frac{k\rho^{2}}{2R(z)}$
- O último termo define a **curvatura** da frente de onda. Podemos ver que, consoante aumenta $z$ (a onda propaga-se) a curvatura aumenta. Vemos ainda que em $z=0$ (fonte da onda) temos curvatura nula, ou seja, temos uma *onda plana*.
![[R gauss.png]]
E temos que $R(z)=z\left(1+ \frac{z_{0}^{2}}{z^{2}}\right)$ é o *raio de curvatura*

## Parâmetros das ondas
- Temos que:
- **Onda plana**
    - Vetor de onda $\vec{k}$
    - Amplitude $A_{0}$
- **Onda esférica**
    - Fonte/origem da onda 
    - Amplitude $A_{0}$
- **Onda gaussiana**
    - Direção de propagação
    - Amplitude $A_{0}$
    - Localização do waist
    - Distância de Rayleigh $z_{0}$

- Ou seja, para a onda gaussiana temos muitos mais parâmetros.
- Ora, queremos ver como saímos da onda escalar e passamos para o tratamento de campos EM exatos.

### Vetores de campo para Gaussiana
- Temos:
$$U(\vec{r})_\text{gauss}= A_{0} \frac{W_{0}}{W(z)}e^{\frac{-\rho^{2}}{W^{2}(z)}}e^{-ikz- ik\frac{\rho^{2}}{2R}+ i \zeta(z)}$$
- Vamos então ver como obtemos os vetores.
- Para uma onda monocromática com amplitude complexa $U(\vec{r})$ (recordemos que foi daí que viemos), podemos definir o vetor potencial magnético: $$\vec{A}(\vec{r})=a_{0}U(\vec{r})\hat{x}$$
- Daí temos: $$\vec{H}(\vec{r})=\frac{1}{\mu_{0}} \nabla \times \vec{A}(\vec{r}) \quad;\quad \vec{E}(\vec{r})=\frac{1}{i\omega c} \nabla \times \vec{H}(\vec{r})$$
- Para uma onda paraboidal paraxial ($kz\gg1$) podemos aproximar que:
$$\vec{E}(\vec{r})_\text{gauss}=f(a_{0})U(\hat{r}) \left[-\hat{x} + \frac{x}{z+iz_{0}}\hat{y} \right] \quad;\quad \vec{H}(\vec{r}) = \frac{i}{\omega\mu_{0}} \nabla \times \vec{E}(\vec{r})$$
em que $f(a_{0})$ é uma função de $a_{0}$.

## Absorção
- Até agora consideramos que os meios que interagem com a luz são totalmente transparentes, ou seja, não absorve a luz.
- Mas veremos agora o caso em que há absorção.
- Notemos que um material ser transparente à luz depende do material em si, mas também do comprimento de onda (a maioria dos materiais é transparente a uns comprimentos de onda e opaco a outros)

- Para estudar onde um certo material absorve luz, é comum considerar a susceptibilidade como sendo complexa:
$$\chi=\chi'+i\chi''$$
- Daqui temos uma permitividade $\varepsilon=\varepsilon_{0}(1+\chi)$ complexa.
- Notemos que a equação de helmholtz continua a ser válida neste caso
- E recordemos que estamos a considerar: luz monocromática e tratamento escalar da radiação.
- Temos que $k$ também será complexo:
$$k=\omega c=\omega \sqrt{\varepsilon\mu _{0}}=k_{0}\sqrt{1+\chi}=k_{0}\sqrt{1+\chi'+i \chi''}$$

**k complexo**
- Assim, se $k$ é complexo, consideremos uma onda plana. Ela terá amplitude: $U(z)=A e^{-ikz}$
- Claramente é vantajoso escrever o número de onda na forma: $$k=\beta- i\frac{1}{2}\alpha$$
em que $\alpha$ é o *coeficiente de absorção do meio*. Já $\beta$ é a constante de propagação da onda.
**alpha**
- Temos:
$$U(z)=Ae^{\frac{-1}{2}\alpha z} e^{-i\beta z}$$
assim, se $\alpha>0$ temos *absorção*. Ou seja, a amplitude $A$ é atenuada por um fator $e^{\frac{-1}{2}\alpha z}$
- Sabemos que a intensidade média é $\overline{I}\propto |U^{2}|$ logo temos: $$\overline{I}\propto e^{-\alpha z}$$
- Em certos casos temos $\alpha<0$ e a intensidade do campo ótico é *ampliada*

**beta**
- Para $\beta$, no caso com $\alpha=0$ temos:
$$e^{-ikz}=e^{-in k_{0}z}~~\to~~ \beta=nk_{0}$$
ou seja, podemos definir o índice de refração na forma:
$$n= \beta/k_{0}$$

**calcular alpha e beta**
- Vejamos como determinar isto.
- Acima, definimos: $$k=\beta-i \frac{1}{2} \alpha= k_{0} \sqrt{1+\chi'+i\chi''}$$
- Temos $\sqrt{1+\chi'+i\chi''}=\sqrt{1+\chi}=\sqrt{\varepsilon/\varepsilon_{0}}=\sqrt{\varepsilon_{r}}$
- Assim:
$$\begin{align*}
\beta-i \frac{1}{2} \alpha&= k_{0} \sqrt{1+\chi'+i\chi''}\\
\frac{\beta}{k_{0}}-i \frac{1}{2} \frac{\alpha}{k_{0}}&= \sqrt{1+\chi'+i\chi''}\\
n-i \frac{1}{2} \frac{\alpha}{k_{0}}&= \sqrt{\varepsilon_{r}}\\
\end{align*}$$

- Vimos ainda que a impedância do meio é: $\eta=\sqrt{\frac{\mu}{\varepsilon}}=\sqrt{\frac{\mu_{0}}{\varepsilon}}=\frac{\sqrt{\mu_{0}}}{\sqrt{\varepsilon_{0}}\sqrt{1+\chi}}=\frac{\eta_{0}}{\sqrt{1+\chi}}$

### Meios com absorção reduzida
- Temos $\chi''\ll 1+\chi'$ 
- Assim: $$\begin{align*}
\sqrt{1+\chi'+i\chi''}&= \sqrt{(1+\chi')(1+i\delta)}\\
&= \sqrt{1+\chi'}\sqrt{1+i\delta}\\
&\approx \sqrt{1+\chi'} \left(1+i \frac{1}{2}\delta\right)\\
&= \sqrt{1+\chi'} + i \frac{\sqrt{1+\chi'}}{2}\delta
\end{align*} \quad \quad;\quad \delta =  \frac{\chi''}{1+\chi'}$$
- Assim temos:
$$\begin{align*}
n- i \frac{1}{2} \frac{\alpha}{k_{0}} &= \sqrt{1+\chi'+i\chi''}\\
n- i \frac{1}{2} \frac{\alpha}{k_{0}} &= \sqrt{1+\chi'} + i \frac{\sqrt{1+\chi'}}{2}\delta
\end{align*}$$
como $1+\chi'\gg \chi''$ podemos considerar $n\sim \sqrt{1+\chi'}$. Assim:
$$\alpha= -k_{0}\sqrt{1+\chi'}\delta=-k_{0} \frac{\chi''}{\sqrt{1+\chi'}}=- \frac{k_{0}}{n}\chi''$$
- Ou seja: 
    - $\chi'$ decide o índice de refração, que é sempre real e positivo
    - Assim, $\chi''$ decide o valor e sinal de $\alpha$. Assim, $\chi''$ decide se o meio tem ganho ou absorção. Absorção/perdas: $\chi''<0\to \alpha>0$

### Meios com absorção elevada
- Temos agora: $|\chi''|\gg |1+\chi'|$
- Fica então:
$$\sqrt{1+\chi'+i\chi''}\approx \sqrt{i\chi''}=\sqrt{-i}\sqrt{-\chi''}=\pm \frac{1}{\sqrt{2}}(1-i)\sqrt{-\chi''}$$
- Então fica:
$$n\approx \sqrt{- \frac{\chi''}{2}} \quad;\quad \alpha\approx 2k_{0} \sqrt{- \frac{\chi''}{2}}$$
- Novamente, num meio com $\chi''<0$
- Overall, este caso importa pouco

## Dispersão
- Aqui falaremos de dispersão temporal (ou frequência), não dispersão espacial.
- Ou seja: $\chi\equiv\chi(\nu),\varepsilon\equiv\varepsilon(\nu),n\equiv n(\nu),c\equiv c_{0}/n(\nu)$
![[n vs comp onda.png]]
- No caso de um feixe de luz branca (ou que tenha vários comprimentos de onda), temos que cada "cor" resultará numa resposta diferente do meio. Isto é, a luz separa-se. Uma forma de entender isso é com o gráfico acima, vemos que a luz vermelha se move com maior velocidade que a luz azul.
- Ou seja, temos o efeito de luz a dispersar num prisma de vidro

## Absorção VS Dispersão
- Num certo meio temos que a sua _resposta_ a um campo elétrico é a polarização:
$$\vec{P}=\varepsilon \chi \vec{E}$$
em que temos:
$$\chi(\nu)=\chi'(\nu)+i \chi''(\nu)$$
- Vimos ainda que num meio com baixa absorção temos:
$$n\simeq \sqrt{1+\chi'} \quad;\quad \alpha\simeq - \frac{k_{0}}{n}\chi''$$
- Se pensarmos na dispersão, podemos ver que ela consiste na variação de $n$ com a frequência $\nu$. Ou seja, a dispersão estará associada à *parte real* da susceptibilidade!

**Back to Sinais e Sistemas**
- Vimos que, de forma mais genérica, temos: $\vec{P}(\vec{r},t)=\varepsilon_{0} \chi(\vec{r},t)* \vec{E}(\vec{r},t)$
    - Recordemos teoria de sistemas lineares!! Isto é equivalente a $y(t)=h(t)*x(t)$. Assim:
        - Temos um sistema **causal**, ou seja, a saída só existe depois de termos uma certa entrada
        - Se a entrada for aplicada em $t\ge0$ a saída é nula se $t<0$.
    - Sabemos ainda que podemos chamar $h(t)$ de *resposta impulsional*, já que é o output do sistema quando o input é um delta de Dirac.
    - Sabemos ainda que, ao fazer transformada de Fourier da entrada, saída e resposta impulsional temos: $Y(j\omega)=H(j\omega)X(j\omega)$
- Ora, notemos uma coisa: $h(t)$ é uma função rela e causal. $H(j\omega)=\mathcal{F}[h(t)]$ é uma função complexa. Ora, estas duas *não são independentes*, já que se relacionam com a transformada de Hillbert.
    - Verifica-se que $\mathcal{H}\biggr[\text{Re}[H(i\omega)]\biggr]=- \text{Im}[H(i\omega)] ~~;~~ \mathcal{H}\biggr[\text{Im}[H(i\omega)]\biggr]= \text{Re}[H(i\omega)]$ 
    - Mais especificamente, as partes real e imaginária relacionam-se de acordo com as relações de Kramers-Kronig

**Back to polarização**
- Ou seja, associando a polarização de um meio a um ESIT temos:
    - $h(t)=\varepsilon_{0}\chi(t)$
    - $H(i\omega)=\varepsilon_{0}\chi(i\omega)=\varepsilon_{0}(\chi'(i\omega)+i\chi''(i\omega))$ ou seja: $H(\nu)=\varepsilon_{0}\chi(\nu)=\varepsilon_{0}(\chi'(\nu)+i\chi''(\nu))$
- Então como vimos, $\chi',\chi''$ NÃO são independentes
- Temos então as relações de Kramers-Kronig:
$$\chi'(\nu)=\frac{2}{\pi}\int_{0}^{\infty} \frac{s \chi''(s)}{s^{2}-\nu^{2}}ds \quad;\quad \chi''(\nu)=- \frac{2}{\pi}\int_{0}^{\infty} \frac{\nu\chi'(s)}{s^{2}-\nu^{2}}ds$$
ou seja:
$$n = \sqrt{1+\chi'} \quad;\quad \alpha= - \frac{k_{0}}{n} \chi''$$
NÃO são independentes.

## Modelos de Lorentz
- Em geral, quando uma onda EM se propaga dentro de um certo meio, a sua velocidade de propogação é reduzida e a onda atenuada.
- Ora, isto é consequência de a onda interagir com as cargas elétricas no meio. Estas ficam com uma polarização $\vec{P}$ que faz com que no meio hava um campo de *deslocamento elétrico*: $\vec{D}(\vec{r},t)=\varepsilon_{0} \vec{E}(\vec{r},t)+\vec{P}(\vec{r},t)$
- Vimos atrás que podemos representar a polarização do meio como o output de um SLIT em que o campo é o input: $\vec{P}(\vec{r},t)=\varepsilon_{0} \chi(\vec{r},t)* \vec{E}(\vec{r},t)$ em que $\chi=\chi'+i\chi''~~,~~ n-i \frac{1}{2} \frac{\alpha}{k_{0}}=\sqrt{1+\chi}$
- Ora, para uma onda monocromática num meio homogéneo podemos passar ao domínio das frequências: $\vec{P}(\omega)=\varepsilon_{0} \chi(\omega) \vec{E}(\omega)$
    - Assim, se determinarmos $n\equiv n(\omega)~,~c\equiv c(\omega)~,~\alpha=\alpha(\omega)$
    - Ora, o modelo de Lorentz permite determinar isto com uma abordagem *clássica*

### A lógica
- Consideramos que cada átomo tem 1 eletrão mais externo, que é o mais afetado pelo campo aplicado pela onda EM.
- Consideramos que os restantes eletrões não são afetados pelo campo. Então, o átomo fica com um momento dipolar nulo.
- Assumimos ainda que o eletrão mais externo sente a força eletroestática aplicada por 1 carga positiva no centro do átomo (as restantes cargas negativas são anuladas pelos eletrões internos)

**Momento Dipolar**
- Ou seja, definimos $x$ como sendo a **posição média** do movimento do eletrão.
    - $x=0$ sem campo aplicado
    - $x\neq0$ com campo aplicado
- Temos então o momento dipolar $p=-ex$ em 1 átomo
- O momento dipolar por unidade de volume será $P=-Nex$

#### Cinemática
**Força elétrica**
- A força elétrica devido ao campo da onda EM:
$$F_{elet} = -e E(t)$$
**Força de amortecimento**
- Esta força existe quase sempre que há movimento:
$$F_{amort} = b \frac{dx}{dt}$$
**Força de reação da mola**
- Resulta da interação do eletrão com o núcleo, consideramos que é como se existisse uma mola a ligá-los:
$$F_{mol}=k_{mol} x$$
em que $\omega_{0}=\sqrt{k_{mol}/m_{e}}$ é a *frequência natural* do conjunto eletrão-mola

**2ª Lei de Newton**
- Ao juntar tudo temos:
$$\begin{align*}
m_{e} \frac{d^{2}x}{dt^{2}} &= F_{elet} - F_{mol} - F_{amort}\\
m_{e} \frac{d^{2}x}{dt^{2}} + b \frac{dx}{dt} + k_{mol}x &= -e E(t)\\
\frac{d^{2}x}{dt^{2}} + \zeta \frac{dx}{dt} + \omega_{0}^{2} x &= - \frac{eE(t)}{m_{e}}\\
\frac{d^{2}(-eNx)}{dt^{2}} + \zeta \frac{d(-eNx)}{dt} + \omega^{2}(-eNx)&= \frac{e^{2}N}{m_{e}}E(t)\\
\frac{d^{2}P}{dt^{2}} + \zeta \frac{dP}{dt} + \omega^{2}P &=  \frac{e^{2}N}{m_{e}}E
\end{align*}$$
e podemos escrever: 
$$\frac{e^{2}N}{m_{e}}= \omega_{0}^{2}\varepsilon_{0} \underbrace{\frac{N e^{2}}{\varepsilon_{0}m_{e}\omega_{0}^{2}}}_{\chi_{0}}=\omega_{0}^{2}\varepsilon_{0}\chi_{0}$$
e temos:
$$\frac{d^{2}P}{dt^{2}} + \zeta \frac{dP}{dt} + \omega^{2}P =  \omega_{0}^{2}\varepsilon_{0}\chi_{0}E$$

**Representação Complexa**
- Vamos agora estudar esta equação, mas a representar o campo e a polarização como amplitudes complexas / fasores:
$$\begin{cases}
\mathbf{P}=P_{0} e^{i\omega t} \\
\mathbf{E}=E_{0} e^{i\omega t}
\end{cases}$$
e temos:
$$\begin{align*}
\frac{d^{2}\mathbf{P}}{dt^{2}} + \zeta \frac{d \mathbf{P}}{dt} + \omega^{2}\mathbf{P} &= \omega_{0}^{2}\varepsilon_{0}\chi_{0}\mathbf{E}\\
-\omega^{2}P_{0}e^{i\omega t} + i\zeta \omega P_{0}e^{i\omega t} + \omega_{0}^{2} P_{0}e^{i\omega t} &= \omega_{0}^{2}\varepsilon_{0}\chi_{0}E_{0}e^{i\omega t}\\
(-\omega^{2}+i\zeta\omega+\omega_{0}^{2})P_{0}&= \omega_{0}^{2}\varepsilon_{0}\chi_{0}E_{0}\\
P_{0} &= \frac{\omega_{0}^{2}\varepsilon_{0}\chi_{0}}{-\omega^{2}+i\zeta\omega + \omega_{0}^{2}}E_{0}
\end{align*}$$
e podemos escrever na forma:
$$P_{0}=\varepsilon_{0} \chi(\omega)E_{0} \quad;\quad \chi(\nu)= \frac{\omega_{0}^{2}\chi_{0}}{-\omega^{2}+i\zeta \omega + \omega_{0}^{2}}$$
e podemos escrever como:
$$\chi(\nu)=\chi_{0} \frac{\nu_{0}^{2}}{\nu_{0}^{2}-\nu^{2}+i\nu \Delta\nu} \quad,\quad \begin{cases*}
\omega= 2\pi\nu\\
\omega_{0}= 2\pi\nu_{0}\\
\Delta\nu=\frac{\zeta}{2\pi}
\end{cases*}$$
- Podemos dividir nas partes real e imaginária:
$$\chi'(\nu)=\chi_{0} \frac{\nu_{0}^{2}(\nu_{0}^{2}-\nu^{2})}{(\nu_{0}^{2}-\nu^{2})^{2}+(\nu\Delta\nu)^{2}} \quad;\quad \chi''(\nu)= -\chi_{0} \frac{\nu_{0}^{2}\nu\Delta\nu}{(\nu_{0}^{2}-\nu^{2})^{2}+(\nu\Delta\nu)^{2}}$$
e temos
![[chi gauss.png]]

##### 3 Casos
**Frequências muito abaixo da de ressonância**
- Como podemso ver nos gráficos acima, temos uma susceptibilidade real e igual a $\chi_{0}$

**Frequências muito acima da de ressonância**
- Vemos nos gráficos que $\chi'\sim0,\chi''\sim0$
- Assim, o meio simplesmente comporta-se como um vazio. Isso faz sentido, o campo oscila tão rapidamente que os átomos não conseguem reagir nem ser influenciados. De tal forma que nem chega a haver susceptibilidade

**Frequência de ressonância**
- Temos então $\nu=\nu_{0}$
- Ficamos com $$\chi'(\nu_{0})=0 ~~,~~ \chi''(\nu_{0})=-\chi_{0} Q=- \chi_{0} \frac{\nu_{0}}{\Delta \nu}$$
ora, a susceptibilidade é completamente imaginária.

**Máximo de chi'**
- Ocorre para $\nu=\nu_{0}\sqrt{1- \frac{1}{Q}}$ e temos $\chi'(\nu)=\frac{\chi_{0}Q}{2- \frac{1}{Q}}$ 

**Mínimo de chi'**
- Ocorre para $\nu=\nu_{0}\sqrt{1+ \frac{1}{Q}}$ e  temos $\chi'(\nu)=- \frac{\chi_{0}Q}{2+ \frac{1}{Q}}$

##### Fase da susceptibilidade
- Como é o caso de qualquer variável complexa, temos que o módulo de $\chi',\chi''$ decidem a fase de $\chi$
- Ora, a fase é o ângulo entre $\mathbf{P},\mathbf{E}$

##### Vizinhança da ressonância
- Vejamos o que acontece em frequências na vizinhança da ressonância. 
- Neste caso temos:
$$\nu\sim\nu_{0} ~~\to~~ \nu_{0}^{2}-\nu^{2}=(\nu_{0}+\nu)(\nu_{0}-\nu)\approx 2\nu_{0}(\nu_{0}-\nu)$$
- E ficamos com:
$$\chi(\nu)=\chi_{0} \frac{\nu_{0}^{2}}{\nu_{0}^{2}-\nu^{2}+i\nu\Delta\nu}\approx \chi_{0} \frac{\nu_{0}^{2}}{2\nu _{0}(\nu_{0}-\nu)+i\nu_{0}\Delta\nu}=\chi_{0}\frac{\nu_{0}/2}{\nu_{0}-\nu+i\Delta\nu/2}$$

- Ao separar as partes real e imaginária:
$$\begin{align*}
\chi''(\nu)&\approx -\chi_{0} \frac{\nu_{0}}{4} \frac{\Delta \nu}{(\nu_{0}-\nu)^{2} + \left(\frac{\Delta\nu}{2}\right)^{2}}\\
\chi'(\nu)&\approx 2 \frac{\nu-\nu_{0}}{\Delta\nu}\chi''(\nu) 
\end{align*}$$
- Notemos que a segunda fração em $\chi''$ é uma **função Lorentziana**, em que $\Delta\nu$ representa a largura a meia altura de $\chi''$

##### Longe da ressonância
- Temos $|\nu-\nu_{0}|\gg\Delta\nu$
- E ficamos com:
$$\chi(\nu)=\chi_{0} \frac{\nu_{0}^{2}}{\nu_{0}^{2}-\nu^{2}+i\nu \Delta\nu}\approx \chi_{0} \frac{\nu_{0}^{2}}{\nu_{0}^{2}-\nu^{2}}$$
- Como a susceptibilidade é completamente *real* então **não temos absorção**

### Meios com múltiplas ressonâncias
- Normalmente, meios dielétricos têm múltiplas ressonâncias. Isto acontece porque existem diferentes modos vibracionais eletrónicos, de rede, etc
- Ora, a susceptibilidade do meio consiste na sobreposição de todas estas ressonâncias
- Como vimos acima, nos gráficos de $\chi',\chi''$ genéricos vemos que $\chi''$ está confinado a frequências perto da ressonância. Já $\chi'$ tem valor $\chi_{0}$ para todos os valores de frequência **abaixo / inferiores** à ressonância
- Como $n\propto \chi'~,~\alpha\propto\chi''$ temos:
![[absorcao e refracao vs freq.png]]
- Notemos que cada ressonância acrescenta um *valor constante* à susceptibilidade do meio a frequências baixas

**Geral**
- Consideremos um meio com $i$ ressonâncias
- Longe de uma certa ressonância $i$ temos uma contribuição desta para a susceptibildade : $\chi^{(i)}(\nu)\approx \chi_{0i}\frac{\nu_{i}^{2}}{\nu_{i}^{2}-\nu^{2}}$ 
- Assim, a susceptibilidade total é:
$$\chi(\nu)=\sum\limits_{i} \chi_{0i}\frac{\nu_{i}^{2}}{\nu_{i}^{2}-\nu^{2}}$$
e temos:
$$n^{2}(\nu)=1+\chi(\nu)=1+\sum\limits_{i} \chi_{0i}\frac{\nu_{i}^{2}}{\nu_{i}^{2}-\nu^{2}}$$
e podemos escrever a **equação de Sellmeier**:
$$n^{2}(\lambda)=1+\sum\limits_{i} \chi_{0i}\frac{\lambda_{i}^{2}}{\lambda_{i}^{2}-\lambda^{2}}$$

### Conclusões
- Daqui vemos que átomos "maiores", com eletrões externos mais externos, temos uma 'mola' mais fraca. Ou seja, temos uma menor constante de mola e temos uma menor frequência de ressonância.
- Por comparação a isto, em átomos maiores consideramos 2 zonas de ressonância:
    - uma zona de eletrões mais internos em que temos frequências UV e RX
    - uma zona de eletrões mais externos em que temos frequências visíveis / IR
- No caso de moléculas temos ligações entre átomos, que são menos fortes do que as que ligam eletrões a núcleos. Além disso, átomos obviamente têm massas maiores que eletrões. Ou seja, as frequências de ressonância de átomos em moléculas são *as mais baixas*
- Temos:
![[polarização vs freq range longo.png]]