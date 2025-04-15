### Onda quase monocromática
- Temos que as componentes de Fourier estão restritras a um intervalo estreito $\Delta\nu$ em torno de $\nu_{0}$
![[Pasted image 20250402095439.png]]
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
![[Pasted image 20250402095940.png]]

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
![[Pasted image 20250402100443.png]]
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
![[Pasted image 20250402111911.png]]
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
![[Pasted image 20250402120612.png]]
- Se $D_{\nu}<0$ temos **dispersão anómala** - Frequências mais elevadas têm mais velocidade e chegam mais cedo.
![[Pasted image 20250402120620.png]]

---- SLIDE 23