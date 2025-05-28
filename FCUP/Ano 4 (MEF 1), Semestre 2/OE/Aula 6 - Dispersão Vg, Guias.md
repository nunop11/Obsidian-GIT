### Onda quase monocromática
- Temos que as componentes de Fourier estão restritras a um intervalo estreito $\Delta\nu$ em torno de $\nu_{0}$
![[fourier onda cromatica.png]]
vemos que a TF da função analítica apenas tem componentes de frequência positiva
- Isto é o caso de um LED: não é monocromático mas quase

### Onda não monocromática
- Podemos ver ondas deste tipo como uma sobreposição de ondas monocromáticas. 

##### Revisão de OMC
- A propagação de uma onda $y$ na direção $x$ é dada pela eq onda: $\partial_{x}^{2}y=\frac{1}{\gamma^{2}} \partial_{t}^{2}y$ 
- Esta equação tem a solução genérica $y(t,x)=a_{1}f_{1}(\gamma t-x) + a_{2}f_{2}(\gamma t+x)$ (em que $f_{i},a_{i}$ são uma função e uma constante arbitrárias)
    - $a_{1}f_{1}(\gamma t - x)$ acaba por ser uma onda que se propaga para a direita
    - $a_{2}f_{2}(\gamma t + x)$ é uma onda que se propaga para a  esquerda
- Podemos definir $\gamma=\frac{x_{2}-x_{1}}{t_{2}-t_{1}}$ AKA *velocidade de fase* que é a velocidade com que um pico da onda se irá propagar. Passaremos então a escrever $\gamma \equiv v_{f}$
- Vamos então escolher $f_{1},f_{2}$ como sendo a *função harmónica*:
$$f_{1}(\gamma t-x)=\cos[h(v_{f}t-x)]$$
queremos que: $x=0\to f_{1}(t=0,x=0)=\cos(0)=1$. Ora, se passar 1 período teremos $x=\lambda\to f_{1}(t=T,x=\lambda)=\cos(2\pi)=1$ 
- Assim, definimos que $h=2\pi/\lambda\equiv k$ !!! Ou seja:
$$f_{1}(x,t)=\cos(\omega_{f}t-kx)~~~~~~,~~ \omega_{f}=kv_{f}$$

**Sobreposição de 2 ondas com freqs diferentes**
- Temos:
$$y_{1}=a\cos(\omega_{1} t-k_{1}x) \quad;\quad y_{2}=a\cos(\omega_{2} t-k_{2}x)$$
logo
$$\begin{align*}
Y = y_{1}+y_{2}&= 2a\underbrace{\cos \left( \frac{\omega_{1}-\omega_{2}}{2}t - \frac{k_{1}-k_{2}}{2}x \right)}_\text{envolvente (varia lentamente)}\underbrace{\cos \left( \frac{\omega_{1}+\omega_{2}}{2}t - \frac{k_{1}+k_{2}}{2}x \right)}_{\text{(varia rápidamente)}}\\
&= 2a \cos \left( \frac{\omega_{1}-\omega_{2}}{2}t - \frac{k_{1}-k_{2}}{2}x \right)\cos (\overline{\omega}t-\overline{k}x)
\end{align*}$$
- Temos então a envolvente, que tem uma propagação lenta, multiplicada por uma onda principal
![[sobreposicao 2 ondas.png]]

- Temos que $v_{f1}=v_{f2}=v_{f}$ logo $$v_{f1}=\frac{\omega_{1}}{k_{1}}=\frac{\omega_{2}}{k_{2}}=v_{f2}$$
e temos, para a envolvente:
$$v_{env}=\frac{\frac{\omega_{1}-\omega_{2}}{2}}{\frac{k_{1}-k_{2}}{2}}=\frac{\Delta \omega}{\Delta k}$$
ou seja, podemos definir:
$$v_{env}\approx \frac{d\omega}{dk}=\left[\frac{dk}{d\omega} \right]^{-1}$$
(a segunda forma é "mais natural", já que $k$ depende de $\omega$ e não o oposto)

- Podemos pensar na velocidade envolvente como sendo a velocidade de propagação da energia de propagação da sobreposição de ondas! Normalmente definimos ainda que $v_{env}\equiv v_{g}$ (velocidade de grupo!)
- Temos $\omega=kv_{f}$ logo:
$$v_{g}=\frac{d\omega}{dk} = \frac{d(v_{f}k)}{dk}=v_{f} + k\frac{dv_{f}}{dk}$$
e temos $k=\frac{2\pi}{\lambda}\to dk=\frac{-2\pi}{\lambda^{2}}d\lambda$ logo:
$$v_{g}=v_{f}-\lambda \frac{dv_{f}}{d\lambda}$$


**Sobreposição de muiiiitas ondas com freqs diferentes**
- Consideremos que temos $n$ ondas monocromáticas com a mesma amplitude, distanciadas de $\delta\omega$ e inseridas num intervalo $\Delta \omega=n\delta \omega$. Consideremos que $x=0$. Temos:
![[n ondas fourier.png]]
- Temos, claro: $$\begin{align*}
y(t,x=0)&= \sum\limits_{m=0}^{n-1} a\cos[(\omega_{1}+m\delta\omega)t]\\
&= a \frac{\sin\left(\frac{n\delta\omega}{2}t\right)}{\sin\left(\frac{\delta\omega}{2}t\right)} \cos \left[ (\omega_{1}+ \tfrac{n-1}{2}\delta\omega)t \right]\\
&= a \frac{\sin \left(\frac{\Delta\omega}{2}t \right)}{\sin(\frac{\Delta\omega}{2n}t)}\cos(\overline{\omega}t)
\end{align*}$$
($\Delta\omega=n\delta\omega~~,~~\omega_{1}+ \tfrac{n-1}{2}\delta\omega$)
ora, se $n\gg1$ teremos:
$$y(t,x=0)=A\frac{\sin\alpha}{\alpha}\cos(\overline{ t})=A\text{sinc}(\alpha)\cos(\overline{\omega}t)$$
($A=na~~,~~\alpha=\frac{\Delta\omega}{2}t$)
obtemos isto porque $\frac{\alpha}{n}\ll1\to\sin(\frac{\alpha}{n})\sim \frac{\alpha}{n}$ 

- Ou seja (se imaginarmos o formato de uma função sinc) vemos que ao acrescentar mais e mais ondas teremos um pico central mais forte e os picos em torno mais fracos.

### Pulso de luz
- Consiste em uma onda EM com reduzida duração temporal
- Temos:
$$U(\vec{r},t)=A \left(t-\frac{z}{c_{0}}\right)e^{i2\pi\nu_{0}(t- \frac{z}{c_{0}})}$$
temos $A(t)$ que é a envolvente complexa e $\nu_{0}$ a frequência central do espetro do pulso.
- Ou seja, o pulso tem duranção reduzida no espaço E no tempo.
- Na prática, este pulso comporta-se como um pacote de ondas a mover no espaço.
- A onda plana monocromática é um caso especial deste tipo de onda, em que $A(t)$ é *constante*.

- Consideramos que a envolviente tem duração $\tau$, de modo que o pulso tem dimensão espacial $c_{0}\tau$
![[sobreposição n ondas.png]]
- Podemos definir a FT:
$$\begin{align*}
V(\vec{r},\nu)&= \mathcal{F}[U(\vec{r},t)]\\
&= \mathcal{F} \left[ A \left(t - \frac{z}{c_{0}} \right) e^{i2\pi\nu_{0} \left(t- \frac{z}{c_{0}}\right)} \right]\\
&= A (\nu-\nu_{0})e^{-i2\pi\nu_{0} \frac{z}{c_{0}}}
\end{align*}$$
ora, então $|V(\vec{r},\nu)|$ está centrado em $\nu_{0}$.

**Num meio**
- Temos uma onda plana pulsada a propagar-se nos zz num meio dispersivo sem perdas: $\alpha=0,n=n(\omega),c=c_{0}/n$
$$U(z,t)=A\left(t- \frac{z}{v_{g}}\right)e^{i2\pi\nu_{0}\left(t- \frac{z}{c}\right)}$$
- Podemos reescrever o termo de fase:
$$e^{i2\pi\nu_{0}(t- \frac{z}{c})}=e^{i(\omega_{0} t- \frac{\omega_{0}}{c} t)}= e^{i(\omega_{0}t-\beta z)}$$
e podemos definir a *constante de propagação do impulso no meio*:
$$\beta= \frac{\omega n(\omega)}{c_{0}}\Biggr|_{\omega=\omega_{0}}$$
e, alternativamente a _velocidade de propagação do termo de fase_: $$c=\frac{\omega}{\beta}\Biggr|_{\omega=\omega_{0}}$$
- A velocidade de grupo é a velocidade de propagação da envolvente, resultante da interferência das ondas do intervalo espetral do impulso. Podemos defini-la como:
$$v_{g}=\left(\frac{d\beta}{d\omega}\Biggr|_{\omega=\omega_{0}} \right)^{-1}$$

- Temos que o tempo de percurso envolvente, que define o pulso e a sua espessura:
$$\tau_{d}=\frac{z}{v_{g}}$$
- Ora, normalmente temos $c=c_{0}/n$. Então deverá haver uma equação semelhante que se aplica para determinar a velocidade de grupo. Temos que
$$v_{g}=\frac{c_{0}}{N(\omega)}\biggr|_{\omega=\omega_{0}} = \frac{c_{0}}{N(\lambda_{0})}\biggr|_{\lambda_{0}=\lambda_{0-central}}$$
em que $N(\omega)$ é o **índice de refração de grupo**. Esta é uma espécie de média fos índices de refração para cada frequência do pulso de luz, centrado em $\omega_{0}$.
- Sendo $\beta=\frac{\omega n(\omega)}{c_{0}}\biggr|_{\omega=\omega_{0}}$ temos:
$$\frac{1}{v_{g}}= \frac{d\beta}{d\omega}\biggr|_{\omega=\omega_{0}}$$
logo:
$$\frac{d}{d\omega} \left[ \frac{\omega n(\omega)}{c_{0}} \right]_{\omega=\omega_{0}}=\frac{N(\lambda_{0})}{c_{0}}\biggr|_{\lambda_{0}=\lambda_{0-central}}$$
de onde obtemos
$$N(\lambda_{0})_{\lambda_{0}=\lambda_{0-central}}=\left[n(\lambda_{0}) - \lambda_{0} \frac{dn}{d\lambda} \right]_{\lambda_{0}=\lambda_{0-central}}$$
- Na prática, ao estudar um pulso, ele propga-se com $v_{g}$ e é refratado pela lei de Snell com um índice de refração $N$
- Podemos fazer expansão de Taylor de $N(\lambda_{0})$:
    - O termo constante mostra que a velocidade de fase é sempre igual à de grupo.
    - Ao introduzir o termo da 1ª derivada passamos a considerar velocidades diferentes
    - O termo da 2ª derivada continua a implicar velocidades de fase e grupo diferentes, mas introduz ainda a possibilidade de a envolvente variar (alargar-se normalmente). Claro, isto é o que observa quando há dispersão!

#### Groud Velocity Dispersion
- Consideremos 2 fatias do espetro: $\nu,\nu+\delta \nu$
- Com tempos de propagação da distância $z$: $$\tau_{d|_{\nu}}=\frac{z}{v_{g|_{\nu=\nu}}}\quad;\quad \tau_{d|_{\nu+\delta\nu }}=\frac{z}{v_{g|_{\nu=\nu+\delta\nu }}}$$
- O atraso de grupo diferencial entre as fatias será:
$$d\tau=\tau_{d|_{\nu}}-\tau_{d|_{\nu+\delta\nu }}=d\left(\frac{z}{v_{g}}\right)$$
e temos:
$$d\tau=\frac{d\tau}{d\nu}d\nu=\frac{d \left(\frac{z}{v_{g}}\right)}{d\nu}d\nu=\frac{d \left(\frac{1}{v_{g}}\right)}{d\nu}zd\nu $$
e podemos escrever:
$$\delta \tau=D_{\nu}z \delta \nu$$
ou seja, para um impulso de largura espectral $\sigma_{\nu}$ centrado em $\nu_{0}$ podemos fazer a seguinte aproximação:
$$\sigma_{\tau}=|D_{\nu=\nu_{0}}|\sigma_{\nu}z$$
ou seja, o alargamento temporal pode ser simplesmente obtido com a largura espectral e a distância de propagação!
- A constante $D_\nu$ é o **coeficiente de dispersão** que podemos definir como:
$$D_{\nu}=\frac{d}{d\nu}\left(\frac{1}{v_{g}}\right)=2\pi \frac{d}{d\omega} \left(\frac{1}{v_{g}} \right)=2\pi \frac{d^{2}\beta}{d\omega^{2}}$$
**Meio dispersivo**
- Como vimos acima, para um meio dispersivo, temos que $v_{g}=\frac{c_{0}}{N}$ e $N(\lambda_{0})=n(\lambda_{0})-\lambda_{0} \frac{dn}{d\lambda_{0}}$
- Podemos então escrever:
$$\begin{align*}
D_{\nu}&= \frac{d}{d\nu}\left(\frac{1}{v_{g}} \right)\\
&= c_{0} \frac{d}{d\nu} \left(N\right)\\
&= \frac{\lambda_{0}^{2}}{c_{0}^{2}} \frac{d}{d\lambda}\left( n(\lambda_{0})-\lambda_{0} \frac{dn}{d\lambda_{0}}\right)\\
&= \frac{\lambda_{0}^{3}}{c_{0}^{2}} \frac{d^{2}n}{d\lambda_{0}^{2}}
\end{align*}$$
em que usamos $c=\lambda\nu~~\to~~ \lambda=\frac{c}{\nu}~~\to~~ d\lambda= - \frac{c}{\nu^{2}}d\nu=- \frac{\lambda^{2}}{c}d\nu~~\to~~ d\nu= - \frac{c}{\lambda^{2}}d\lambda$

- Ora, é mais comum representar a largura espectral em função do comprimento de onda invés da frequência. Logo precisamos de saber $D_{\lambda_{0}}$. Temos:
$$\begin{align*}
\sigma_{\tau}=|D_{\nu}|\sigma_{\nu}z&= |D_{\lambda_{0}}|\sigma_{\lambda}z\\
\delta \tau=D_{\nu}\delta\nu z &= D_{\lambda_{0}}\delta\lambda_{0}z\\
D_{\nu}\delta\nu&= D_{\lambda_{0}}\delta\lambda_{0}\\
D_{\lambda_{0}}&= \frac{\delta\nu}{\delta\lambda_{0}}D_{\nu}
\end{align*}$$
Logo:
$$\begin{align*}
D_{\lambda_{0}}&= \frac{d \left(\frac{c_{0}}{\lambda_{0}} \right)}{d\lambda_{0}} D_{\nu}\\
&= - \frac{c_{0}}{\lambda_{0}^{2}} \frac{\lambda_{0}^{3}}{c_{0}^{2}} \frac{d^{2}n}{d\lambda_{0}^{2}}\\
&= \frac{-\lambda_{0}}{c_{0}} \frac{d^{2}n}{d\lambda_{0}^{2}}
\end{align*}$$

##### Dispersão normal e anómala
- Ou seja, vimos que $D_{\nu},D_{\lambda_{0}}$ têm sinais opostos. Ora, este sinal não afeta o grau de alargamento do impulso. MAS afeta a fase da envolvente complexa.
- Assim, o sinal do coeficiente (na prática só temos 1 coeficiente, representado de 2 formas) determina a propagação do pulso através de certos meios.
- Se $D_{\nu}>0$ temos **dispersão normal** - Frequências mais elevadas demoram mais a proapgar. Ou seja, estas componentes chegam mais tarde.
![[dispersao normal.png]]
- Se $D_{\nu}<0$ temos **dispersão anómala** - Frequências mais elevadas têm mais velocidade e chegam mais cedo.
![[dispersao anomala.png]]

### Lorentz
- Vamos agora interligar estas grandezas ao modelo de Lorentz
- Consideremos um meio com 1 ressonância, na frequência $\nu_{0}$, com comprimento de onda $\lambda_{0}$
- Temos $\chi=\chi'+i\chi''$. Desta forma, $k$ será complexo:
$$k=k_{0}\sqrt{1+\chi}=k_{0}\sqrt{1+\chi'+i\chi''}$$
- É útil escrever este número na forma $k=\beta- i \frac{1}{2}\alpha$ e facilmente definimos $\beta=n k_{0}$
- Assim temos:
$$n- i \frac{1}{2} \frac{\alpha}{k_{0}}=\sqrt{1+\chi'+i\chi''}$$
- Na aula 4 vimos que:
$$\chi'(\nu)=\chi_{0} \frac{\nu_{0}^{2}(\nu_{0}^{2}-\nu^{2})}{(\nu_{0}^{2}-\nu^{2})^{2}+(\nu\Delta\nu)^{2}} \quad;\quad \chi''(\nu)= -\chi_{0} \frac{\nu_{0}^{2}\nu\Delta\nu}{(\nu_{0}^{2}-\nu^{2})^{2}+(\nu\Delta\nu)^{2}}$$
- Vimos nesta aula que:
$$v_{g}=\frac{c_{0}}{N}\quad;\quad D_{\lambda_{0}}=- \frac{\lambda_{0}}{c_{0}} \frac{d^{2}n}{d\lambda_{0}^{2}}  \quad;\quad N(\lambda_{0})=n(\lambda_{0})- \lambda_{0} \frac{dn}{d\lambda_{0}}$$
- Para $\chi_{0}=0.05, \Delta\nu/\nu_{0}=0.1$, temos:
![[dispersao, N e n.png]]
- Os pontos de inflexão:
    - Dão $N$ máximo - temos a menor velocidade de propagação da envolvente
    - Dão $D_{\lambda_{0}}=0$ - menor dispersão temporal
- Vemos que $n$ varia muito com $\lambda_{0}$ perto da ressonância e que $N$ explode nessa regição - isto acontece porque ele depende da derivada $\frac{dn}{d\lambda_{0}}$
- Daqui surge uma dúvida interessante, vemos que $N$ desce  para bastante abaixo de $1$, logo teremos velocidade de grupo $v_{g}=\frac{c_{0}}{N}> c_{0}$  
    - Ou seja, como é possível algo se mover mais rápido que a velocidade da luz no vácuo?? Na realidade isso não acontece - neste regime, a *informação* não se move à velocidade de grupo, logo nenhuma lei de Einstein é quebrada

#### Sílica
- Vidro de quartzo AKA sílica AKA $\text{SiO}_{2}$ 
- "Parece" vidro, mas não tem ingredientes adicionados a vidro normal para baixar a sua temperatura de fusão
- Como tal, sílica tem alta pureza e propriedades bem conhecidas
- Na região de $[0.21-3.71]\mu\text{m}$ a dependência $n(\lambda_{0})$ é descrita pela equação de Sellmeier com 3 ressonâncias:
$$n^{2}(\lambda_{0})=1 + \chi_{01}\frac{\lambda_{0}^{2}}{\lambda_{0}^{2}-\lambda_{01}^{2}} + \chi_{02}\frac{\lambda_{0}^{2}}{\lambda_{0}^{2}-\lambda_{02}^{2}} + \chi_{03}\frac{\lambda_{0}^{2}}{\lambda_{0}^{2}-\lambda_{03}^{2}}$$
![[freqs e susceps de silica.png]]
e daqui é fácil representar $n,N,D_{\lambda_{0}}$ em função de $\lambda_{0}$:
![[grafico de n e D de silica.png]]
- Tal como vimos acima com equações teóricas, para $\lambda_{0}=1.276\mu\text{m}$ temos 
    - $N$ mínimo, logo temos $v_{g}=c_{0}/N$ máximo
    - $D=0$ 

# Guias de onda
- Sistemas óticos convencionais usam elemetos óticos por onde a luz passa. Entre os elementos, a luz propaga-se no *ar*
    - Temos lentes, espelhos, polarizadores que têm o objetivo de controlar as propriedades da luz 
    - A isto chamamos de **bulk optics**
- Mas sistemas deste tipo rapidamente se tornam MUITO complexos:
![[montagem otica tradicional.png]]
- Assim, em algumas situações é possível transmitir ondas óticas através de estruturas dielétricas, evitando-se a propagação no ar - **ótica guiada**
- Na maioria dos casos, a luz é mantida dentro de um material dielétrico (alto $n$) graças ao princípio de *reflexão total*
- Podemos ter guias de vários tipos:
![[otica guiada.png]]

**Fotónica (ou Ótica) integrada** 
- Combinar num só chip vários elementos óticos que podem controlar a luz: geração de luz, focagem, divisão, combinação, isolamento, deteção, etc etc
- A estes chips chamamos de PICs - Photonic Integrated Circuits
![[sistema otica integrada.png|500]]

### História
- Inicialmente comunicava-se com meios de propagação "pelo ar" - sinais de fumo, sinais com lenço
- Mais recentemente, usam-se lasers colimados para comunicar a distâncias reduzidas:
![[lasers comunicacao.png]]
que é muito interessante e útil, mas apenas para comunicar entre edifícios e que existe comercialmente.
- Mas, em distâncias maiores, estes não funcionam devido a alta atenuação do sinal na atmosfera
- Em 1842, Colladon demonstrou reflexão interna total em jatos de água
- Em 1961, um guia de onda com lentes e espelhos foi construido
- Em 1958, Karbowiak construiu um guia de onda em tubos metálicos ocos
    - Mas este tipo de guias apenas tinham altas perdas porque apenas se colocava a luz num meio refletor, no ar
- Assim, tornou-se mais relevante desenvolver um sistema mais como os atuais. Os primeiros estudos teóricos sobre guias dielétricos começaram em 1910, por Hondros e Debye - concluiu-se que um cilindro dielétrico suspenso no ar consegue guiar uma onda EM
- Em 1920, Schreiver desenvolveu um sistema assim - havia alta propagação, com muitos modos com imensas distribuições
- Em 1936 a propagação no sistema de Schreiver foi compreendida por Carson, Mead e Schelkunoff
    - Mostrou-se que a propagação acontece com modos híbridos (componentes de E e H)
    - Provaram que cada modo tem uma frequência de corte (freq mínima possível)
    - Existe um modo de ordem mais baixa $HE_{11}$ que se propaga a qualquer frequência
- Nos 1940s foi melhor ainda entendida a propagação e as funções de atenuação. Mas era muito difícil fazer vidros tão finos e uniformes como desejado
- EM 1954, van Heel desenvolveu um guia otico coberto com um dielétrico e teve resultados promissores
- Mesmo em 1960, os vidros mais puros tinham atenuações de $500\text{dB/km}$. Pensou-se que era impossível propagação em fibras
- Em 1966, Hockham lançou um artigo fruto de 2 anos de investigação
    - Revelou-se que a atenuação elevadissima era causada por iões de impurezas nos vidros (Cu, Fe, Cr, V, água, etc)
    - Concluiu-se que o material com melhor transmissão era _**dióxido de silício / sílica**_
- Em 1970, a Corning patenteou a primeira fibra ótica de baixa perda
    - Tinha um núcleo de SiO2 e Ti, com perdas de $20\text{dB/km}$ para comp onda de $\sim850\text{nm}$
    - Foi difícil fabricar em escala / difícil reproduzir
- Em 1976, a NTT e Fujicara (Japão) desenvolveram uma fibra monomodo 1300-1500nm, com atenuação de $0.5\text{dB/km}$
    - Em 1979, estas empresas atingiram o limite teórico a 1550nm - 0.2dB/km
- Em 1975, Payne e Gambling descobriram a região de menor dispersão em fibras de sílica - por torno de 1300nm
- Em 1984 foram criadas fibras com mínimo de dispersão em 1550nm - isto é perfeito tendo em conta os resultados japoneses em 1979
- Esta é a tecnologia usada hoje em dia!

