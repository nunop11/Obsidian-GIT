###### Aula 2 - 20/2/2024
## 1.4 - Correntes em Drude
- Podemos escrever uma qualquer densidade volúmica de corrente como:
$$\vec{\mathcal{J}}=-ne \vec{v}=- \frac{ne}{m}\vec{p}$$

- Consideremos um metal sujeito a um campo elétrico externo, que descrevemos conforme o modelo de Drude. Para um certo eletrão livre, temos o momento linear descrito por $\vec{p}(t)$. Podemos "prever" o momento daqui a um intervalo de tempo $dt$ usando série de Taylor:
$$\begin{align*}
\vec{p}(t+dt)&= \vec{p}(t)+\frac{d\vec{p}}{dt}dt+\mathcal{O}(dt^{2})\\
&= \vec{p}(t)+\vec{f}(t)dt+\mathcal{O}(dt^{2})
\end{align*}$$
em que $\vec{f}$ é uma força externa aplicada sobre o eletrão. Se esta não existir, o eletrão teria sempre o mesmo momento.
- A esta equação introduzimos um termo probabilistico:
$$\vec{p}(t+dt)=\left(1-\frac{dt}{\tau}\right)[\vec{p}(t)+\vec{f}(t)dt+\mathcal{O}(dt^{2})]$$
ora, como vimos na aula anterior, $1-dt/\tau$ corresponde à probabilidade de uma partícula *não* colidir num intervalo $dt$. 

**Limite dt=0**
- Consideremos agora o limite em que $dt=0$. É fácil ver que $dt^{2}\sim0$. Assim, $\mathcal{O}(dt^{2})=0$.
- Podemos então desenvolver a equação:
$$\begin{align*}
\vec{p}(t+dt)&= \left(1-\frac{dt}{\tau}\right)[\vec{p}(t)+\vec{f}(t)dt+\mathcal{O}(dt^{2})]\\
&= \left(1-\frac{dt}{\tau}\right)[\vec{p}(t)+\vec{f}(t)dt]\\
&= \vec{p}(t) - \frac{\vec{p}(t)}{\tau}dt + \vec{f}(t)dt - \frac{\vec{f}(t)}{\tau}\underbrace{dt^{2}}_{\sim~0}\\
\vec{p}(t+dt)- \vec{p}(t)&= - \frac{\vec{p}(t)}{\tau}dt + \vec{f}(t)dt\\
\frac{\vec{p}(t+dt)- \vec{p}(t)}{dt}=\frac{d\vec{p}}{dt}&= - \frac{1}{\tau}\vec{p}(t)+\vec{f}(t)\\
\end{align*}$$

**Desligar campo**
- Consideremos agora que o campo elétrico desaparece. Isto implica $\vec{f}=\vec{0}$ 

- Para $t=0$ temos $\vec{p}(0)=\vec{p_{0}}$ logo $\vec{\mathcal{J}}(0)=-\frac{ne}{m}\vec{p_{0}}$
- Em $t>0$ teremos $\frac{d\vec{p}}{dt}=- \frac{1}{\tau}\vec{p}$. Podemos resolver esta equação diferencial por separação de variáveis:
$$\frac{d\vec{p}}{dt}=- \frac{1}{\tau}\vec{p}~~\to~~ \frac{d\vec{p}}{\vec{p}}=- \frac{dt}{\tau}~~\to~~\vec{p}(t)=\vec{p_{0}}~e^{- t/\tau}$$
- Ou seja, graficamente este cenário seria representado por:
![[desligar campo em drude.png|400]]
isto pode ser comparado à descarga de um condensador quando se desliga a corrente que por nele passa. O momento decai com um "atraso" relativamente à força

- Consideremos agora que, invés de se anular, $\vec{f}$ reduz para $\vec{f_{0}}$
- Neste caso, para $t>0$ teremos: $$\vec{f}(t)=\vec{f_{0}} \quad;\quad \vec{p}(t)=\vec{p_{0}}e^{-t/\tau}+\vec{f_{0}}\tau$$
sendo que para $t\gg\tau$ (pelo menos 10 vezes maior) teremos $\vec{p}(t)=\vec{f_{0}}\tau$. Por esta razão, $\vec{f_{0}}\tau$ é o *termo  permanente* da equação de $\vec{p}(t)$ acima. O outro termo é o termo de transição.

## 1.5 - Efeito de Hall
![[efeito hall figura.png|625]]
- Conforme a figura acima temos um DDP $V$ entre os terminais do metal que gera um $\vec{E_{x}}$. Por sua vez, este gera uma corrente $\vec{\mathcal{J}}_{x}$. Temos ainda um campo magnético $\vec{B}$ com direção em zz.
- Como conhecemos de EM1 e Labs, o que acontece é:
    - O campo $E_{x}$ ($E_{x}\hat{x}$) gera a corrente elétrica AKA coloca os eletrões em movimento
    - Devido ao seu movimento, os eletrões sofrem a ação de uma força magnética ($\vec{f}_{m}=-e\vec{v}\times\vec{B}$). Como a velocidade é $\vec{v}=-v_{x}\hat{x}$ (campo é positivo, logo a velocidade será negativa) e $\vec{B}=B\hat{z}$ temos $\vec{f}_{m}$ com direção $-\hat{y}$.
    - A força magnética altera o percurso (inicialmente lineares) dos eletrões, fazendo-os curvar para "cá" (yy negativo). 
    - Ao ocorrer isto, um dos lados fica com maior densidade de eletrões que o outro, o que gera uma DDP transversal (nos yy). Isto por sua vez gera um campo transversal $E_{y}$ com direção $-\hat{y}$ que puxa os eletrões de volta ao percurso "inicial"
    - Temos uma fase de transição e eventualmente ficamos com um percurso curvo e estável. 

**Coeficiente de Hall**
- No estado permanente temos $E_{y}=vB$.
- Além disso, surge um novo parâmetro: *magnetorresistência* $\rho(B)=\frac{E_{x}}{\mathcal{J}_{x}}$
- Podemos ainda definir o **coeficiente de Hall**: $R_{H}=\frac{E_{y}}{\mathcal{J}_{x}B}<0$. Ora, o coeficiente de Hall é a grandeza daqui mais fácil de medir experimentalmente. E, enquanto que o modelo de Drude prevê que este coeficiente seja sempre negativo. Mas há certos materiais que têm $R_{H}>0$, nomeadamente Alumínio e Berílio.

**Análise do movimento**
- Podemos escrever a força exercida num eletrão livre como $\vec{f}=-e\vec{E}-e\vec{v}\times\vec{B}$ (força de Lorentz). Ficamos com: $$\frac{d\vec{p}}{dt}=- \frac{1}{\tau}\vec{p}+\vec{f}=- \frac{1}{\tau}\vec{p}-e(\vec{E}+\vec{v}\times\vec{B})=\vec{0}$$
em que se iguala a $\vec{0}$, porque em regime permanente temos um sistema estacionário.
- Podemos dividir a equação acima em xx e yy:
$$\begin{cases}
x:~~ 0=- \frac{1}{\tau}p_{x}-e E_{x}- \frac{e}{m}p_{y}B \\
y:~~ 0=- \frac{1}{\tau}p_{y}-e E_{y}+ \frac{e}{m}p_{x}B  
\end{cases}$$
e podemos definir a *frequência ciclotrónica* $\omega_{c}=\frac{eB}{m}$ e a *condutividade elétrica* $\sigma_{0}=\frac{ne^{2}\tau}{m}$. 
- Recordemos ainda que $\mathcal{J}_{x}=-\frac{ne}{m}p_{x}\to p_{x}=- \frac{m}{ne}\mathcal{J_{x}}$. Ao substituir acima:
$$\begin{cases}
x:~~ e E_{x}= \frac{m}{ne\tau}\mathcal{J}_{x}+ \frac{1}{n}\mathcal{J}_{y}B \\
y:~~ e E_{y}= \frac{m}{ne\tau}\mathcal{J}_{y}- \frac{1}{n}\mathcal{J}_{x}B  
\end{cases}$$
podemos substituir $B= \frac{m}{e}\omega_{c}$:
$$\begin{cases}
x:~~ e E_{x}= \frac{m}{ne\tau}\mathcal{J}_{x}+ \frac{m}{ne}\mathcal{J}_{y}\omega_{c} \\
y:~~ e E_{y}= \frac{m}{ne\tau}\mathcal{J}_{y}- \frac{m}{ne}\mathcal{J}_{x}\omega_{c} \\
\end{cases}$$
dividimos tudo por $\frac{m}{ne}$:
$$\begin{cases}
x:~~ \frac{ne^{2}}{m}E_{x}= \frac{1}{\tau}\mathcal{J}_{x}+ \omega_{c}\mathcal{J}_{y} \\
y:~~ \frac{ne^{2}}{m} E_{y}= \frac{1}{\tau}\mathcal{J}_{y}- \omega_{c}\mathcal{J}_{x} \\
\end{cases}$$
e podemos multiplicar tudo por $\tau$:
$$\begin{cases}
x:~~ \frac{ne^{2}\tau}{m}E_{x}= \mathcal{J}_{x}+ \omega_{c}\tau\mathcal{J}_{y} \\
y:~~ \frac{ne^{2}\tau}{m} E_{y}= \mathcal{J}_{y}- \omega_{c}\tau\mathcal{J}_{x} \\
\end{cases}$$
logo:
$$\begin{cases}
x:~~ \sigma_{0}E_{x}= \mathcal{J}_{x}+ \omega_{c}\tau\mathcal{J}_{y} \\
y:~~ \sigma_{0} E_{y}= \mathcal{J}_{y}- \omega_{c}\tau\mathcal{J}_{x} \\
\end{cases}$$

- Vimos que neste problema em si $\mathcal{J}_{y}=0$ e fica:
$$\sigma_{0}E_{x}=\mathcal{J}_{x} \quad \quad;\quad \quad \sigma_{0}E_{y}=-\omega_{c}\tau\mathcal{J}_{x}$$
e temos:
$$R_{H}=\frac{E_{y}}{\mathcal{J_{x}}B}=\frac{\frac{-\omega_{c}\tau\mathcal{J}_{x}}{\sigma_{0}}}{\mathcal{J_{x}}B}=- \frac{\omega_{c}\tau}{\sigma_{0}B}=- \frac{\frac{eB}{m}\tau}{\frac{ne^{2}\tau}{m}B}=\frac{-1}{ne}$$
ou seja, o modelo de Drude, tal como dito atrás, não explica $R_{H}$ positivo.
- Outra coisa que não é explicada pelo modelo é o facto que $R_{H}$ varia com a temperatura. Ora, como $n,e$ são constantes, a única forma de hipoteticamente explicar isto seria através de $\tau$, do qual $R_{H}$ também não depende 

**Tensor**
- De notar que a equação $\mathcal{J}=\sigma E$ ou até $\vec{\mathcal{J}}=\sigma\vec{E}$ apenas se aplica quando os vetores densidade de corrente e campo elétrico são *colineares*. Se não forem, teremos o **tensor da condutividade**, que consiste numa matriz:
    - Em 3D a equação $\vec{\mathcal{J}}=\sigma\vec{E}$ fica com $\vec{\mathcal{J}},\vec{E}$ a serem vetores coluna e $\sigma$ uma matriz 3x3.  