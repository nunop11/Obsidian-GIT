### Meio Linear, *dispresivo*, homogéneo e isotrópico
- Um meio dispersivo, que é o caso de todos os meios reais, o vetor $\vec{P}$ *não reage instantaneamnete* ao campo $\vec{E}$. Ou seja, há um **tempo de resposta**
- Podemos ver o campo E como o input de um sistema, em que gera oscilações nos eletrões, que se encontram num meio dielétrico (a estrutura atómica)
- Assim, podemos então dizer que o meio tem uma *memória*
- Quando o tempo de resposta é $\ll$ as outras constantes de tempo do sistema, podemos dizer que o meio é *aproximadamente não dispersivo*
- Como a resposta do meio consiste na oscilação de eletrões (movimento) podemos descrever o sistema com uma equação deste tipo
$$a_{2} \partial_{t}^{2}\vec{P}+a_{1}\partial_{t}\vec{P}+a_{0}\vec{P}= \vec{E}$$
- Considerando o ponto de vista em que vemos este meio como um sistema, temos que a output ($y$) pode ser determinada se soubermos a entrada $x$ e o sistema em si $h$: $y(t)=h(t)*x(t)$ 
    - Ou seja: $$\vec{P}(t)=\varepsilon_{0}\chi(t)*\vec{E}(t)$$
- Também no caso de sistema, podemos sempre fazer o estudo no domínio das frequências: $Y(i\omega)=H(i\omega)X(i\omega)$, que é uma equação equivalente à de cima. Assim:
$$\vec{P}(i\omega)=\varepsilon \chi(i\omega)\vec{E}(i\omega)$$


### Meio *não-linear*, não-dispersivo, homogéneo, isotrópico
- Isto quer dizer que não temos $\vec{P}\propto\vec{E}$
- Para estudar esta resposta, consideramos as equações de Maxwell em que *não* temos cargas nem correntes livres
- Podemos deduzir:
$$\nabla \times (\nabla \times \vec{E})=-\mu_{0} \partial_{t}^{2}\vec{D}$$
- E temos $\nabla \times (\nabla \times \vec{E})= \nabla \cdot (\nabla \cdot \vec{E}) - \nabla^{2}\vec{E}$.
- Sabemos ainda que $\vec{D}=\varepsilon_{0}\vec{E}+\vec{P}$
- E obtemos: $\nabla \cdot(\nabla \cdot \vec{E}) - \nabla^{2}\vec{E} = -\mu_{0}\varepsilon_{0} \partial_{t}^{2}\vec{E}-\mu_{0} \partial_{t}^{2}\vec{P}$
- Que é o mesmo que: 
$$\nabla^{2}\vec{E}- \frac{1}{c^{2}} \partial_{t}^{2} \vec{E} = \mu_{0} \partial_{t}^{2}\vec{P}$$
já que, sendo $\vec{D}=\varepsilon \vec{E}$ temos $\vec{E}=\frac{1}{\varepsilon}\vec{D}$. Sabemos que, num meio sem cargas livres temos $\nabla \cdot \vec{D}=0= \nabla \cdot \vec{E}$.

- Esta equação de onda aplica-se a todos os meios *homogéneos e isotrópicos* que podem ser (não-)dispersivos e (não-)lineares
- Temos então $\vec{P}$ a ser uma função não linear de $\vec{E}$ : $\vec{P}=\Psi(\vec{E})$
    - A solução mais simples da equação de onda é $\vec{P}=\Psi(\vec{E})=a_{2}\vec{E}^{2} + a_{1}\vec{E}$

- **NOTA** - se $\vec{E}_{1},\vec{E}_{2}$ são soluções da equação diferencial, a sua soma $\vec{E}_{1}+\vec{E}_{2}$ em geral NÃO é solução. Isto vem do facto que a equação não é linear.

## Outra representação
- Vimos que podemos representar o campo ótico como:
$$\vec{E}=\vec{E}_{0} e^{i(\vec{k}\cdot\vec{r}-\omega t)}=\hat{e}E_{0}e^{i(\vec{k}\cdot\vec{r}-\omega t)}$$
isto é a representação do campo como uma onda plana.
- Consideremos agora que a componente espacial é só uma função *genérica*. Temos a componente real:
$$\vec{E}=\vec{E}_{0}(\vec{r})\cos(\omega t- \phi(\vec{r}))$$
em que $\phi(\vec{r})$ tem de ser válido pelas equações de Maxwell.
- Podemos escrever ainda assim:
$$\vec{E}=\text{Re} \left[\vec{E}_{0}(\vec{r})e^{-i\phi(\vec{r})}e^{i\omega t} \right]$$
e podemos definir a **_amplitude complexa do campo ótica_**:
$$\vec{E}(\vec{r})=\vec{E}_{0}(\vec{r})e^{-i\phi(\vec{r})}$$

em que, claro, $\vec{E}(\vec{r},t)=\vec{E}(r)e^{i\omega t}$
- Fazemos o mesmo para **todos** os campos:
$$\vec{B}(\vec{r},t)=\vec{B}(\vec{r})e^{i\omega t} ~~;~~ \vec{D}(\vec{r},t)=\vec{D}(\vec{r})e^{i\omega t}~~;~~\vec{H}(\vec{r},t)=\vec{H}(\vec{r})e^{i\omega t}~~;~~ \vec{P}(\vec{r},t)=\vec{P}(\vec{r})e^{i\omega t}~~;~~ \vec{M}(\vec{r},t)=\vec{M}(\vec{r})e^{i\omega t}$$

- Isto é bom porque permite simplificar as equações de Maxwell, já que $\partial_{t}e^{at}=ae^{at}$ :
$$\boxed{\begin{align*}
\nabla \times \vec{H}(\vec{r}) &= i\omega \vec{D}(\vec{r})\\
\nabla \times \vec{E}(\vec{r}) &= -i\omega \vec{B}(\vec{r})\\
\nabla \cdot \vec{D}(\vec{r}) &= 0\\
\nabla \cdot \vec{B}(\vec{r}) &= 0
\end{align*}}$$
e temos:
$$\begin{align*}
\vec{D}(\vec{r})&= \varepsilon_{0}\vec{E}(\vec{r}) + \vec{P}(\vec{r})\\
\vec{B}(\vec{r}) &= \mu_{0}(\vec{H}(\vec{r}) + \vec{M}(\vec{r}))
\end{align*}$$
Notar que tudo isto são amplitudes complexas!

- Podemos então definir a *intensidade* do campo ótico com o módulo do **vetor POYNTING**:
$$\begin{align*}
\vec{S}&= \vec{E}\times \vec{H}\\
&= \text{Re} \left[\vec{E}(\vec{r})e^{i\omega t} \right]\times \text{Re} \left[\vec{H}(\vec{r})e^{i\omega t} \right]\\
&= \frac{\vec{E}(\vec{r})e^{i\omega t} + \vec{E}^{*}(\vec{r})e^{-i\omega t}}{2}\times\frac{\vec{H}(\vec{r})e^{i\omega t} + \vec{H}^{*}(\vec{r})e^{-i\omega t}}{2}\\
&= \frac{1}{4} \left[ \vec{E}(\vec{r})\times\vec{H}^{*}(\vec{r}) + \vec{E}^{*}(\vec{r})\times\vec{H}(\vec{r}) + e^{i2\omega t}\vec{E}(\vec{r})\times\vec{H}(\vec{r}) + e^{-i2\omega t}\vec{E}^{*}(\vec{r})\times\vec{H}^{*}(\vec{r}) \right]
\end{align*}$$
- Ora, o campo ótico tem frequências demasiado altas para conseguir estudar e acompanhar na vida real. Assim, consideramos o seu **valor médio**:
$$\begin{align*}
\langle \vec{S}\rangle &= \langle \vec{E}(\vec{r})\times\vec{H}\left(\vec{r} \right)\rangle \\
&= \frac{1}{4} \left[\vec{E}(\vec{r})\times\vec{H}^{*}(\vec{r}) +  \vec{E}^{*}(\vec{r})\times\vec{H}(\vec{r}) \right]\\
&= \frac{1}{2} \left[\vec{S}_{0} + \vec{S}_{0}^{*} \right]\\
\\
\vec{S}_{0}&= \frac{\vec{E}(\vec{r}) \times \vec{H}^{*}(\vec{r})}{2}\\
\end{align*}$$
- Ou seja, podemos definir a **intensidade MÉDIA** como sendo: $\overline{I}=\text{Re}[\vec{S}_{0}]$
    - Quase sempre se fala apenas na intensidade MÉDIA, então é comum escrever $I$ invés de $\overline{I}$. Mas o professor insiste que é fundamental nunca esquecer que falamos do valor médio.
- Consideramos que $\vec{S}_{0}$ é a _amplitude complexa do vetor Poynting_.
### Alguns meios:
#### Meio linear, não-dispersivo, homogéneo e isotrópico (e não magnético)
- Como já vimos, temos
$$\vec{D}(\vec{r})=\varepsilon \vec{E}(\vec{r}) \quad;\quad \vec{B}(\vec{r})=\mu \vec{H}(\vec{r})$$
- Em termos das equações de Maxwell, isto resume-se ao caso em que consideramos um meio ideal sem cargas nem correntes livres:
$$\begin{align*}
\nabla \times \vec{H}(\vec{r}) &= i\omega \vec{D}(\vec{r})=i\omega\varepsilon\vec{E}(\vec{r})\\
\nabla \times \vec{E}(\vec{r}) &= -i\omega \vec{B}(\vec{r})=-i\omega\mu \vec{H}(\vec{r})\\
\nabla \cdot \vec{D}(\vec{r}) &= 0\\
\nabla \cdot \vec{B}(\vec{r}) &= 0
\end{align*}$$
notando-se que estas equações utilizam as *amplitudes complexas*!

#### Meio linear, não-dispersivo, *não-homogéneo* e isotrópico
- Temos $$\varepsilon\equiv \varepsilon(\vec{r})$$
- E mantêm-se exatamente as equações acima, para um meio homogéneo. Apenas temos que ter em consideração esta variação de $\varepsilon$.

### Dependências espaciais de odnas monocromáticas
- Consideremos um meio linear, não-dispersivo, homogéneo e isotrópico
#### Onda Plana
![[Attachments/FCUP/A4S2/OE/onda plana.png]]
- As frentes de onda são planos que simplesmente se movem numa direção
- Definimos $\phi(\vec{r})=\vec{k}\cdot\vec{r}$, ou seja:
$$\begin{align*}
\vec{E}(\vec{r})&= \vec{E}_{0}e^{-i\vec{k}\cdot\vec{r}}\\
\vec{H}(\vec{r})&= \vec{H}_{0}e^{-i\vec{k}\cdot\vec{r}}
\end{align*}$$

- Colocamos isto nas equações de maxewll e temos:
$$\begin{align*}
\vec{k} \times \vec{H_{0}}&= -\omega \varepsilon \vec{E}_{0}\\
\vec{k}\times \vec{E}_{0}&= \omega \mu \vec{H}_{0}
\end{align*}$$
- Daqui temos que $\vec{k},\vec{E}_{0},\vec{H}_{0}$ são **mutuamente ortogonais**.
- Temos ainda:
$$\begin{cases}
H_{0}=\frac{\omega \varepsilon}{k}E_{0} \\
H_{0}=\frac{k}{\omega\mu} E_{0}
\end{cases}\to \frac{\omega\varepsilon}{k}=\frac{k}{\omega\mu}\to k=\omega \sqrt{\varepsilon\mu }=\frac{\omega}{c}$$
podemos definir o **índide de refração** $n$ e temos: $c=\frac{1}{n}c_{0}$ logo:
$$k=\frac{n\omega}{c_{0}}=nk_{0}$$

- E definimos a **impedância do meio**:
$$\eta=\frac{E_{0}}{H_{0}}=\sqrt{\frac{\mu}{\varepsilon}}$$
que no vácuo é $\eta_{0}=377 \Omega$ (isto não tem grande significado físico, apenas temos Ohms porque essa é a unidade que resulta de dividir E/H)
    - Acerca desta grandeza, temos que $\eta=\eta_{0}/n$, tal como para a velocidade
    - 

- Já a intensidade média é $$\overline{I}=\text{Re} \left[ \vec{S}_{0} \right]=\frac{E_{0}^{2}}{2\eta}$$
que no vácuo, se tivermos $\overline{I}=10 \text{W cm}^{-2}$ temos $\vec{E}_{0}=87 \text{V cm}^{-1}$
- Esta onda tem uma frequência temporal bem definida. Mas tem uma direção de propagação também muito bem definida. Assim, podemos considerar que tem frequência espacial bem definida
    - Por isso, este tipo de onda é usada como a base de transformadas de Fourier

#### Onda Esférica
- Temos $\vec{E}(\vec{r})=\vec{E_{0}}(\vec{r})e^{-i\phi(\vec{r})}$
- Num caso esférico consideramos que o esta equação *não é vetorial*, mas sim escalar (já que ele só depende do raio). Para isso, temos que ter um campo polarizado.
- Consideremos que o campo E está polarizado segundo $x$. Ficamos com:
$$E_{x}(\vec{r})=E_{0x}(\vec{r})e^{-i\phi(\vec{r})}$$
- Vimos atrás que num meio linear,ND,H,I temos que que $$\nabla^{2}E_{x} - \frac{1}{c^{2}}\partial_{t}^{2}E_{x}=0$$
logo temos a equação de Helmholtz:
$$\nabla^{2}U+k^{2}\partial_{t}^{2}U=0$$
em que:$$k=\omega\sqrt{\varepsilon\mu} ~~,~~ U\equiv U(\vec{r},t)=U(\vec{r})e^{i\omega t}=E_{x}(\vec{r},t)$$
- Podemos determinar a intensidade média e temos
$$\overline{I}=\frac{E_{0x}^{2}}{2\eta}$$
e esta equação é *idêntica* ao que vimos para ondas planas! De facto, esta equação aplica-se para muitas geometrias de campo ótico, sendo que este apenas tem que ser **monocromática**!

- Podemos definir a onda como perdendo intensidade/amplitude consoante se afasta da sua origem. Ou seja:
$$E_{x}=\frac{E_{0x}}{r}e^{-ikr}$$

### Dipolo
- Temos 2 cargas opostas, como vemos abaixo:
![[Attachments/FCUP/A4S2/OE/dipolo.png]]
- Ou seja, temos um momento dipolar $\vec{p}_{e}=qd\hat{x}$ que vai sempre da carga negativa para a positiva.
- Se o momento dipolar variar de formar harmónica: $\vec{p}_{e}=\vec{p_{0e}}\cos\omega t$, então será emitida uma *onda EM com essa frequência* $\omega$
    - Isto é o que acontece no caso de um material a ser polarizado por um campo ótico monocromático
![[dipolo evolucao.png]]

**Ponto distante**
- A uma distância $r\gg d$, um obsercador (que esteja no eixo $x$) verá uma carga *positiva* quando $\vec{p}_{e}$ aponta para $+x$ e *negativa* quando aponta para $-x$
- Consideremos então que o campo nesse ponto pode ser definido como $U(\vec{r})=\frac{1}{4\pi} \frac{e^{-ikr}}{r}$ 

#### Campos
- Vamos definir o *potencial vetor*: $\vec{A}=a_{0}U(\vec{r})\hat{x}$, em que: $a_{0}=\|\vec{p_{0e}}\|\mu_{0}\omega$. 
    - Este vetor irá permitir determinar as componentes do campo no ponto
- Sendo $U(\vec{r})$ a equação que temos acima, fica: $$\vec{A}(\vec{r})=\frac{a_{0}}{4\pi} \frac{e^{-ikr}}{r} \hat{x}$$
e sabemos que podemos definir $\vec{B}=\nabla \times \vec{A}=\mu \vec{H}$
- Assim temos:
$$\vec{H}(\vec{r})=\frac{a_{0}}{2\pi\mu} \left(\nabla \times \frac{e^{-ikr}}{r}\hat{x}\right)$$
- E vimos que, para um campo ótico representado por amplitudes complexas num meio sem correntes/cargas livres, a lei de Ampere-Maxwell fica:
$$\nabla \times \vec{H}=i\omega \vec{D}=i\omega \varepsilon \vec{E}$$
logo
$$\vec{E}(\vec{r})=\frac{1}{i\omega\varepsilon} (\nabla \times \vec{H}(\vec{r}))$$

![[ref esferico.png]]
- Se considerarmos um referencial **esférico** estas equações dão-nos:
$$\begin{align*}
\vec{H}(\vec{r})&= h_{0}\sin\theta \left(1+ \frac{1}{ikr}\right) U(\vec{r}) \hat{\phi}\\
\vec{E}(\vec{r})&= 2e_{0} \cos\theta \left(\frac{1}{ikr}+ \frac{1}{(ikr)^{2}}\right)U(\vec{r})\hat{r} + e_{0} \sin\theta \left(1+\frac{1}{ikr}+ \frac{1}{(ikr)^{2}}\right)U(\vec{r})\hat{\theta}
\end{align*}$$
em que:
$$e_{0}=-\mu_{0}\omega^{2}|\vec{p_{0e}}| ~~;~~ h_{0}=- \frac{\omega^{2}}{c} |\vec{p_{0e}}|~~;~~ U(\vec{r})=\frac{1}{4\pi} \frac{e^{-ikr}}{r}$$
- Vemos que os dois campos não dependem de $\phi$, apenas $r,\theta$. Ou seja, temos *simetria azimutal*!

#### Ponto muito longe
- Para $kr\gg 1$ as expressões acima simplificam porque podemos desprezar os termos $1/kr$.Ou seja fica:
$$\begin{align*}
\vec{E}(\vec{r})&\approx e_{0}U(\vec{r})\sin\theta ~\hat{\theta}\\
\vec{H}(\vec{r})&\approx h_{0}U(\vec{r})
\sin\theta~\hat{\phi}\end{align*}$$
ou seja, são ortogonais entre si e ortogonais à direção radial: $\vec{E}$ é polar e $\vec{H}$ é azimutal.
![[onda esferica campos.png]]

- Consideremos agora que $\theta\approx \frac{\pi}{2}, \phi\approx \frac{\pi}{2}$. Ficamos com:
$$\begin{align*}
\vec{E}(\vec{r})&\approx e_{0}U(\vec{r}) ~\hat{\theta}\\
\vec{H}(\vec{r})&\approx h_{0}U(\vec{r})
~\hat{\phi}\end{align*}$$
- Consideremos agora os versores, nas coordenadas *cartesianas*:
$$\hat{\theta}=-\sin\theta\hat{x} + \cos\theta\cos\phi\hat{y} + \cos\theta\sin\phi\hat{z}$$
e fazemos a seguinte aproximação super sus:
$$\sin\theta\approx1 ~~;~~ \cos\theta\approx  \frac{x}{z} ~~;~~ \cos\phi\approx \frac{y}{z}$$
e fica:
$$\hat{\theta}\approx -\hat{x} + \frac{x}{z} \hat{z}$$
- Assim, para $z$ elevado:
$$\vec{E}(\vec{r})\approx e_{0}U(\vec{r}) \hat{\theta}\approx e_{0}U(\vec{r}) \left(- \hat{x} + \frac{x}{z} \hat{z}\right)\approx -e_{0}U(\vec{r})\hat{x}$$
e podemos definir: $U(\vec{r})\equiv U(z)=\frac{1}{4\pi} \frac{e^{-ikz}}{z}$ logo:
$$\vec{E}(\vec{r})=\frac{-e_{0}}{4\pi} \frac{e^{-ikz}}{z} \hat{x}$$
AKA *ONDA PLANA*.
- Apesar dos passos suspeitos que fizemos para chegar aqui, isto faz sentido:
![[onda esf frente onda.png]]

**Dependência de THETA**
- Voltemos atrás, à versão dos campos para um ponto longínquo:
$$\begin{align*}
\vec{E}(\vec{r})&\approx e_{0}U(\vec{r})\sin\theta ~\hat{\theta}\\
\vec{H}(\vec{r})&\approx h_{0}U(\vec{r})
\sin\theta~\hat{\phi}\end{align*}$$
vemos que temos dependência em $\sin\theta$. Ora, neste caso, quando $\theta=0$ ou $\theta=\pi$ teremos campos nulos!!!
- Ou seja, existe uma dependência toroidal:
![[frente onda torius.png]]

**E dipolo magnetico??**
- Neste caso teremos campos idênticos, mas com as direções trocadas (para $kr\gg1$):
$$\begin{align*}
\vec{E}(\vec{r})&\approx e_{0}U(\vec{r})\sin\theta ~\hat{\phi}\\
\vec{H}(\vec{r})&\approx h_{0}U(\vec{r})\sin\theta~\hat{\theta}\end{align*}$$
em que as constantes mudam:
$$e_{0}=\mu \frac{\omega^{2}}{c} |\vec{p_{0e}}|~~;~~ h_{0}= \left(\frac{\omega}{c}\right)^{2}|\vec{p_{0e}}|$$
- Este tipo de dipolo atua como um *antena ótica*:
![[frente onda dipolo map.png]]