## 2.1 - Frentes de Onda
- Como já vimos, 1 frente de onda é um conjunto de pontos com a mesma fase $\phi$.
- Iremos assumir que pontos da mesma frente de onda têm a mesma amplitude e velocidade igual à velocidade de propagação da onda.

## 2.2 - Princípio de Huygens
- Diz que cada ponto de uma frente de onda emite ondas circulares/esféricas ao longo do seu movimento. Ou seja, a frente de onda num instante $t+\delta t$ será o resultado da interferência das ondas secundárias emitidas por todos os pontos da frente de onda em  $t$.

## 2.3 - Teorema de Malus ($\neq$ Lei de Malus da Polarização)
- Se seguirmos 1 ponto da frente de onda ao longo do tempo, parece que ele descreve uma trajetória perpendicular à frente de onda. Temos então o **raio ótico** (ou raio de luz) - uma representação geométrica que consiste em traçar uma linha que marca ao "percurso" da onda, sendo perpendicular à frente de onda.
- Os pontos de 2 frentes de onda diferentes ligados pelo mesmo raio ótico são *pontos correspondentes*. O teorema de Malus diz que a separação no tempo entre estes pontos é constante.
- Tudo o que disse nesta secção faz sentido mas não encontrei na net nada assim associado a "Teorema de Malus".

## 2.4 - Princípio de Fermat
- Diz que um raio de luz desloca-se entre 2 pontos no **percurso de menor tempo de viagem**.
- No entanto, pode haver casos em que o percurso da luz *maximiza* o tempo de viagem.



## 2.5 - Leis da Ótica Linear
### 2.5.1 - Luz em Espaço Homogéneo
- Raios de luz viajam em linha reta, porque esse é o percurso mais rápido.

**Princípio de Reversibilidade** - Isto é um resultado do princípio de Fermat. Se uma trajetória satisfaz esse princípio, é de prever que o mesmo percurso percorrido em sentido contrário também satisfaça o princípio. Isto revela-se útil ao alinhar sistemas óticos.

**Princípio de Snell-Descartes** - $n_{1}\sin\theta_{i}=n_{2}\sin\theta_{t}$
*Demo:*
![[refracao.png]]
- Podemos escrever o tempo $t$ para a luz ir de $A$ a $B$ como sendo $t=t_{1}+t_{2}$
- E cada um destes pode ser escrito como $t_{1}=\frac{l_{1}}{v_{1}}~,~ t_{2}=\frac{l_{2}}{v_{2}}$
- A distância total percorrida na direção dos $x$ é $x=x_{1}+x_{2}\to x_{2}=x-x_{1}$. Temos : $$l_{1}=\sqrt{x_{1}^{2}+y_{1}^{2}} \quad;\quad l_{2}=\sqrt{(x-x_{1})^{2}+y_{2}^{2}}$$
- E o tempo de voo é: $$t=\frac{\sqrt{x_{1}^{2}+y_{1}^{2}}}{v_{1}}+\frac{\sqrt{(x-x_{1})^{2}+y_{2}^{2}}}{x_{2}}$$
- Pelo princípio de Fermat, é preciso que o tempo de voo seja mínimo (ou seja, a derivada é nula): $$\frac{dt}{dx_{1}}=\frac{x_{1}}{v_{1}\sqrt{x_{1}^{2}+y_{1}^{2}}}- \frac{x-x_{1}}{v_{2}\sqrt{(x-x_{1})^{2}+y_{2}^{2}}}=0$$
- Sendo que, por definição, $\sin\theta_{1}=x_{1}/l_{1}~,~\sin\theta_{2}=x_{2}/l_{2}$ podemos escrever a equação da derivada:
$$\frac{\sin\theta_{1}}{v_{1}}-\frac{\sin\theta_{2}}{v_{2}}=0$$
de onde resulta a lei de snell: $n_{1}\sin\theta_{1}=n_{2}\sin\theta_{2}$

**Lei da Reflexão** - $\theta_{i}=\theta_{r}$
*Demo:* partindo da lei de Snell, basta colocar $n_{1}=n_{2}$ (o feixe incidente e refletido ocorrem no mesmo meio) e ficamos com $\theta_{i}=\theta_{r}$

## 2.6 - Aplicações do Fermat
- O princípio de Fermat pode ser usado para determinar a forma do interface entre 2 meios.

### 2.6.1 - Refletor Eliptico
![[espelho esferico.png]]
- Consideremos que os raios saem de P. Para que eles cheguem a Q em fase, têm que demorar todos o mesmo tempo a chegar a Q, o que implica que têm de percorrer a mesma distância.
- Consideremos a ampliação abaixo:
![[espelho esferico 2.png]]
- Temos um raio a partir de P e a percorrer o eixo ótico, sendo refletido em O e acabando em Q. A distância percorrida será $\Delta s=\overline{PO}+\overline{OQ}$. 
- Temos outro raio que vai a A e daí cheg a Q. Este irá percorrer: $\Delta s'=\overline{PA}+\overline{AQ}$
- Ora, para que estes raios cheguem em fase a Q é preciso que: $$\overline{PO}+\overline{OQ}=\overline{PA}+\overline{AQ}$$

- Pelo referencial desenhado temos
$$P=\left(\frac{d}{2},0\right) \quad;\quad Q=\left(\frac{-d}{2},0\right) \quad;\quad A=(x,y) \quad;\quad O=\left(\frac{-a}{2},0\right)$$
(em que $a$ é o eixo maior da elipse, que está centrada na origem)
- Temos então:
$$\begin{align*}
\overline{PA}&= \sqrt{\left(x - \frac{d}{2}\right)^{2}+y^{2}}\\
\overline{AQ}&= \sqrt{\left(x + \frac{d}{2}\right)^{2}+y^{2}}\\
\overline{PO}&= \frac{a}{2} + \frac{d}{2}\\
\overline{OQ}&= \frac{a}{2}- \frac{d}{2}
\end{align*}$$

- Se substituirmos na equação $\overline{PO}+\overline{OQ}=\overline{PA}+\overline{AQ}$ obtemos
$$\left(\frac{x}{a}\right)^{2}+\left(\frac{y}{b}\right)^{2}=1$$
(em que $b$ é o eixo maior da elipse)
- Ou seja, o conjunto de pontos que satisfazem a lei de Fermat é uma elipse AKA o espelho é eliptico

### 2.6.2 - Refletor Parabólico
![[espelho esferico 3.png]]
- Novamente, para que os raios cheguem em fase, eles têm todos que percorrer a mesma distância.
- Se considerarmos um raio que sai de $O'$, é refletido em $O$ e chega a $Q$, a distância percorrida é $\Delta s=\overline{O'O}+\overline{OQ}$
- Se considerarmos um raio que saia de $A'$, seja relfetido em $A$ e chegue a $Q$, a distância é $\Delta s'=\overline{A'A}+\overline{AQ}$

- De acordo com o referencial ilustrado:
$$O=(0,0) \quad;\quad O'=(d,0) \quad;\quad A=(x,y) \quad;\quad A'=(d,y) \quad;\quad Q=(q,0)$$
e podemos calcular:
$$\begin{align*}
\overline{O'O}&= d\\
\overline{OQ}&= q\\
\overline{A'A}&= d-x\\
\overline{AQ}&= \sqrt{(q-x)^{2}+y^{2}}
\end{align*}$$
de onde podemos obter:
$$x = \frac{y^{2}}{4q} = \frac{y^{2}}{16a}$$
em que $a= \frac{1}{4}q$ é a concavidade do espelho. Temos então que o espelho é *parabólico*.

### 2.6.3 - Refletor Hiperbólico
![[espelho concavo.png]]
- Nos casos atrás escolhemos P que estava num foco da elipse e $A',O'$ que estava na reta diretriz. Aqui iremos escolher $A',O'$ que estão numa circunferência de raio $r$ e centro $C'$ (acho que C' é o foco da hipérbole). Ou seja, sem o espelho, ondas que saiam desta circunferência chegariam a $C'$ com a mesma fase.
- Com um espelho como aquele ilustrado, os raios chegam todos a $c$ com a mesma fasee, pelo que a distâncias percorridas pelos raios terá de continuar a ser a mesma, $r$.
- Assim:
    - Para o raio que parte de O', reflete em O e chega a C, a distância é $\Delta s=\overline{O'O}+\overline{OC}=r$
    - Para um raio que sai de A', se reflete em A e chega a C, a distância é $\Delta s'=\overline{A'A}+\overline{AC}=r$
- Em que temos $\overline{O'C'}=r=\overline{A'C'}$
- Temos então que:
$$\overline{OC}-\overline{C'O}=\overline{AC}-\overline{C'A}$$
e podemos definir $$O=(a,0)\quad;\quad O'=(r,0) \quad;\quad A=(x,y) \quad;\quad C=(x,0)$$
e podemos escrever:
$$\left(\frac{x}{a}\right)^{2}+\left(\frac{y}{b}\right)^{2}=1$$
pelo que temos uma hipérbole, que são descritas por
![[Attachments/FCUP/A3S1/OF/hiperbole.png]]
sendo $a^{2}+b^{2}=c^{2}$.

### 2.6.4 - Dioptro de Oval Cartesiana
- Podemos usar o princípio de Fermat para determinar a forma da interface entre 2 meios óticos com índices de refração diferentes (a que chamamos **Dioptro**).

![[Attachments/FCUP/A3S1/OF/dioptro.png]]
- Temos então o caso acima. Temos feixes a partir de $P$ no meio 1 e todos eles chegam a $Q$ no meio 2.
- Ora, temos agora que a velocidade do raio muda ao trocar de meio. Temos então:
    - Para um raio que sai de P, atravessa o interface em V e chega a Q, temos a relação $c\Delta t=n_{1}\overline{PV}+n_{2}\overline{VQ}$ (podemos ver que os 2 lados da equação têm dimensão de distância)
    - Para um raio que sai de P, atravessa o interface em A e chega a Q, temos $c\Delta t'=n_{1}\overline{PA}+n_{2}\overline{AQ}$

e pelo princípio de Fermat temos
$$n_{1}\overline{PV}+n_{2}\overline{VQ}=n_{1}\overline{PA}+n_{2}\overline{AQ}$$
- Podemos centrar o referencial em V e temos
$$V=(0,0)\quad;\quad Q=(-q,0) \quad;\quad P=(p,0) \quad;\quad A=(x,y)$$
pelo que
$$\begin{align*}
\overline{PV}&= p\\
\overline{VQ}&= q\\
\overline{PA}&= \sqrt{(x-p)^{2}+y^{2}}\\
\overline{AQ}&= \sqrt{(x+q)^{2}+y^{2}}
\end{align*}$$
e podemos obter:
$$n_1 p + n_2 q = n_1 \sqrt{(x-p)^2 + y^2} + n_2 \sqrt{(x+q)^2 + y^2}$$

## 2.7 - Meios Não Homogéneos
- Consideremos um meio em que o meio é heterogéneo e em que as propriedades óticas variam de forma gradual. Efetivamente, isto resulta num meio em que ocorre uma série de refrações:
![[meio nao homogeneo.png]]

- De forma a estudar isto, podemos definir $\vec{r}=\vec{r}(s)$, ou seja, em que este depende da profundidade. 
- Podemos definir uma onda plana como:
$$\psi(\vec{r},t)=\vec{A}(\vec{r})\exp[i(k_{0}S(\vec{r})-\omega t)] \quad \quad;\quad \quad S(\vec{r})=\frac{\vec{k}(\vec{r})\cdot\vec{r}}{k_{0}}$$
e ao aplicar a equação de onda:
$$(c^{2}\nabla^{2}-n^{2}\partial_{t}^{2})\psi(\vec{r},t)=0$$
- Podemos obter a parte real:
$$\nabla^{2}A+ [n^{2}-(\nabla S)\cdot(\nabla S)]k_{0}^{2}A=0$$
e a parte imaginária
$$2(\nabla S)\cdot(\nabla A)+(\nabla^{2}S)A=0$$
- Se a variação das propriedades óticas do meio variar de forma suficientemente gradual, podemos considerar que nas sucessivas refrações a amplitude do raio não varia muito. Assim, será correto considerar $\nabla^{2}A\simeq0$. Daqui surge:
$$\nabla S\cdot\nabla S=n^{2}$$
teremos então
$$\nabla S=n\vec{u}$$
(isto é a expressão matemática correspondente ao teorema de Malus acima)
- Podemos derivar a equação acima em $s$:
$$\frac{d}{ds}\nabla S=\frac{d}{ds}(n\vec{u})=\frac{d}{ds}\left(n \frac{d\vec{r}}{ds}\right)=\nabla n$$
logo
$$\frac{1}{A} \frac{dA}{ds}=\frac{-1}{2} \frac{\nabla(n\vec{u})}{n}$$
##### EXEMPLO
- Consideremos um plano 2D, em que temos $n=n(y)$ sendo o índice de refração constante nos xx.
- O versor que descreve o movimento neste plano será $\vec{u}=(\sin\theta,\cos\theta)$
- Temos então:
$$\frac{d}{ds}[n(\sin\theta,\cos\theta)]=(0, \partial_{y}n)$$
e na 1ª componente temos
$$\frac{d}{ds}(n\sin\theta)=0$$
ou seja, $n\sin\theta$ é constnate nos xx e resulta:
$$n\sin\theta=n'\sin\theta'$$

## 2.8 - Conceitos Ótica Geométrica
### Objeto e Imagem
**Objeto** - fonte de luz ou objeto colocado no sistema ótico de forma a ser observado
**Imagem** - representação visual do objeto após a luz atravessar o sistema ótico

### Imagem Real e Virtual
**Real** - quando a imagem representa um ponto de convergência dos raios óticos
**Virtual** - o ponto de convergência representa a imagem, mas esse ponto não existe na realidade (como quando converge no mesmo lado da lente que o objeto)

### Eixo Ótico
- Linha imaginária que atravesso o centro do sistema ótico.

### Vértice
- Ponto em que o eixo ótico interseta o dispositivo ótico (lente)

### Foco
- Ponto que todos os feixes *paralelos ao eixo ótico* atravessam.
- **Real** - os raios atravessam o ponto
- **Imaginário** - quando o percurso dos raios na ausência do espelho/lente passa no ponto
- Algum dispositivos óticos não têm foco (espelho plano)

### Raios Notáveis
![[espelho esferico 4.png]]
- Para estudar uma lente e a imagem que ela gera temos 3 tipos de raios notáveis que facilmente prevemos e nos permitem obter resultados:
    - Raios incidentes *paralelos ao eixo ótico* que depois passam pelo foco
    - Raios incidentes que *passam pelo foco* e depois se tornam paralelos ao eixo ótico
    - Raios incidentes que *passam no centro do espelho* e depois seguem no mesmo ângulo e sentido oposto
- Dito isto, para determinar a imagem de um serto objeto, basta encontrar a interseção de 2 destes raios notáveis. Podemos fazer o 3º para verificar.

## 2.9 - Espelhos
### 2.9.1 - Espelho Plano
![[espelho plano.png]]
- $O$ é o objeto, o ponto de onde surgem os raios. A distância ao espelho é $o$.
- $I$ é a imagem, o ponto onde os raios (virtuais neste caso) se cruzam. Este dista $i$ do espelho. Neste espelho, $i=o$.
- Aqui devemos notar que para encontrar a imagem, extendemos os raios *refletidos* para o outro lado do espelho.

### 2.9.2 - Espelho esférico concâvo
![[espelho convexo.png]]
- Muitas vezes, este tipo de espelho é uma boa aproximação de espelhos parabólicos, hiperbólicos, etc
- Se considerarmos que os ângulos $\alpha_{1},\alpha_{2},\beta$ são muito reduzidos, podemos usar a *fórmula de Descartes* para a reflexão numa superfície esférica concâva:
$$\frac{1}{p}+ \frac{1}{q}= \frac{2}{r}$$
isto pode ser deduzido usando na figura acima, os triângulos $ABQ, ABC, ABP$ e respetivos ângulos.

#### Distância Focal
- Esta consiste na distância do vértice ao foco e é $$f=\frac{r}{2}$$
(isto pode ser obtido ao fazer $p\to\infty$ na fórmula de Descartes acima)
- Isto surge ao aproximar o espelho esférico a um parabólico. Acima, para o refletor parabólico vimos que $x=\frac{y^{2}}{4q}$. Ora, nessa equação $q$ é o foco!
    - Ora, para uma esfera / circunferência podemos escrever: $y^{2}+(x-r)^{2}=r^{2}$
    - Em que podemos definir $x$ como $x=r\pm \sqrt{r^{2}-y^{2}}$
    - E podemos expandir a raiz em série de Taylor para o caso em que $y\ll r$ e usar a subtração no $\pm$, obtendo: $$\begin{align*}
x&\approx r + r\left(1 - \frac{y^{2}}{2r^{2}}+ \frac{y^{4}}{8r^{4}}+\dots\right)\\
&\approx \frac{y^{2}}{2r} - \frac{y^{4}}{8r^{3}}+\dots
\end{align*}$$
    - Comparando isto à equação $x=\frac{y^{2}}{4q}$ da parábola obtemos $r=2f$

##### Erro da Aproximação
Acabamos de aproximar o espelho esférico a um espelho parabólico. Podemos determinar o erro associado a isto, dividindo o 2º termo da série de Taylor feita pelo 1º:
$$\delta_{xx}\equiv \frac{\frac{y^{4}}{8r^{3}}}{\frac{y^{2}}{2r}}=\frac{y^{2}}{4r^{2}}$$
ou seja:
$$y = 2\sqrt{\delta_{xx}}r$$
- Se tivermos um erro de $1\%$ teremos um erro não desprezável para distâncias inferiores a $0.2r$

#### Plano Principal do Espelho
- Se considerarmos um espelho aproximadamente plano (especialmente na zona central), teremos que os pontos de reflexão dos raios encontram-se todos num plano que é perpendicular ao eixo ótico - este é o *plano principal do espelho*.
- Ou seja, em certos espelhos ou quando consideramos uma secção muito reduzida de um espelho esférico, podemos aproximar este a um espelho plano, representado pelo plano principal. Podemos calcular o erro desta aproximação:
$$\delta_{xy}=\frac{\frac{y^{2}}{2r}}{y}=\frac{y}{2r}$$
e vemos que aproximar o espelho esférico ao plano principal é muito mais restritivo.

#### Produção de Imagem
![[imagem espelho esferico 1.png]]
- Na 1ª imagem temos o objeto colocado *em cima do foco*. Temos que os raios que saem do objeto se tornam paralelos.
- Na 2ª imagem temos imagem, mas virtual. De notar que usamos um raio paralelo ao eixo ótico (raio horizontal em cima) e um raio que passa no foco (que vem de baixo) como raios notáveis para determinar a imagem. Em ambos, tivemos que prolongar os traçados para além do espelho para obter a imagem. Isto ocorre quando temos o objeto *entre o vértice e o foco*.

![[imagem espelho esferico 2.png]]
- Na 1ª imagem temos o objeto *atrás do centro do espelho*. Este é portanto o caso em que $o>2f$. Usamos raios a sair do objeto, com um a passar no centro e um passar no foco. Temos que a imagem é real, invertida, menor que o objeto e aparece em $i\in[f,2f]$
- Na 2ª imagem temos o objeto *em cima no centro*, ou seja $o=f$. Os raios usados saem do objeto, um passa no foco, outro é paralelo ao eixo. (Podiamos ainda traçar um raio a sair do objeto, descer para o centro e infinitamente se refletir, tendo-se o mesmo ponto de interseção). A imagem encontra-se no centro, é real, igual ao objeto e invertida.
- Na 3ª imagemtemos o objeto *entre o foco e o centro*, ou seja $f<o<2f$. Usamos os mesmos raios que no caso atrás. Temos uma imagem real, invertida e maior que o objeto. Esta encontra-se em $i>2f$.

#### Fatores de Ampliação
- Podemos definir o fator de ampliação. Sendo $h_{o}$ a altura do objeto e $h_{i}$ a da imagem (dependendo do caso, isto pode não ser uma altura, mas sim a distância do objeto / imagem ao eixo ótico), teoms o *fator de ampliação transversal*:
$$m_{T}=\frac{h_{i}}{h_{o}}$$
aqui $h_{i}$ pode ser negativo, pelo que $m_{T}<0$ quando a imagem está invertida.

- Temos ainda o *fator de ampliação longitudinal*:
$$m_{L}=\frac{x_{2}'-x_{1}}{x_{2}-x_{1}}$$
para obter este, temos que ter 2 objetos nos pontos $x_{1},x_{2}$ com respetivas imagens em $x_{1}',x_{2}'$.

### 2.9.3 - Espelho Esférico Convexo
![[espelho concavo 2.png]]
- A fórmula da reflexão de Descartes fica:
$$- \frac{1}{p}+ \frac{1}{q}= \frac{2}{r}$$
- A *distância focal* é dada por
$$f= \frac{r}{2}$$
- As imagens geradas são todas virtuais (do lado oposto ao espelho) e não invertidas.

## 2.10 - Modelos de Lentes
### 2.10.1 - Dioptro
- Acima já vimos que um dioptro é o interface entre 2 meios com índices de refração diferentes, com uma forma que faz com que todos os raios emitidos num ponto $P$ se encontrem em $Q$.
- Consideremos um dioptro esférico:
![[dioptro 1.png]]
- $Q,P$ são conjugados se um objeto colocado em $P$ resulta numa imagem idêntica àquela que teríamos se o objeto estivesse em $Q$.

- Se considerarmos ângulos pequenos o suficiente para que $\sin\theta_{i}\simeq\theta_{i}$ obtemos
$$n_{1}\alpha_{1}+n_{2}\alpha_{2}=(n_{2}-n_{1})\beta$$
- Fazendo as mesmas aproximações temos
$$\frac{n_{1}}p +\frac {n_{2}}q = \frac{n_{2}-n_{1}}{r}$$

- Temos ainda que um dioptro tem 2 focos:
**Foco de Entrada**
Este é o ponto dentro do dioptro para onda convergem os raios paralelos ao eixo que vêm do exterior do dioptro.
$$f_{e}=\frac{n_{2}}{n_{2}-n_{1}}r$$
(Obtida na equação das distâncias quando $p\to\infty$)

**Foco de Saída**
Ponto fora do dioptro para onde convergem os eixos paralelos ao eixo que vêm do interior do dioptro.
$$f_{s}=\frac{n_{1}}{n_{2}-n_{1}}r$$
(Obtida na equação das distâncias quando $q\to\infty$)

- Partindo da equação das distâncias, $\frac{n_{1}}p +\frac {n_{2}}q = \frac{n_{2}-n_{1}}{r}$, podemos tirar conclusões. Presumindo que o lado direito é constante:
    - Se $p$ for muito elevado, $q$ é reduzido. Assim, o cone de raios que saem de $p$ tem um ângulo muito reduzido no bico e os raios divergem pouco. Assim, eles convergem em $q$.
    - Se $p$ for reduzindo, $q$ vai aumentando rapidamente. O ângulo no bico do cone dos raios vai aumentando e os raios vão divergindo mais e mais, pelo que percorrem maior distância no dioptro antes de convergirem. Enventualmente, quando $p=f_{s}$ temos $q\to\infty$
- Assim, para $f_{s}$ temos: $\frac{n_{1}}{p}=\frac{n_{2}-n_{1}}{r}$. Desta forma, se $p$ diminuir ainda mais, o $q$ pode tornar-se negativo e a imagem passa a ser virtual.

## 2.11 - Lentes
- Veremos 2 formas de descrever lentes:

### 2.11.1 - Combinação de 2 Dioptros
![[lente biconvexa.png]]
- A lente tem índice de refração $n_{l}$ e o meio envolvente $n_{m}$.
- Imaginamos a lente como sendo a interseção de 2 dioptros esféricos.
- Conforme a equação das distâncias temos que, para raios que saiam de $S$ temos (not sure do que se passa aqui: a imagem de S é virtual e é P', mas não entendi porquê nem o quê que estamos a presumir que tem $n_{l}$ ou $n_{m}$)
$$\frac{n_{m}}{s_{o1}}+\frac{n_{l}}{s_{i1}} = \frac{n_{l}-n_{m}}{R_{1}}$$

- Do "ponto de vista" da esfera 2 temos que isto é equivalente a ter feixes a vir de $P'$, a uma distância $s_{o2}$ no seu interior (imaginemos a esfera 2 toda a ter índice $n_{l})$.
- Claramente vemos que $|s_{o2}|=|s_{i1}|+d$. Por convenção, $s_{o2}>0,s_{i1}<0$. Ou seja: $$s_{o2}=-s_{i1}+d$$
- Ou seja, para a esfera 2 temos
$$\frac{n_{l}}{-s_{i1}+d}+\frac{n_{m}}{s_{i2}}=\frac{n_{m}-n_{l}}{R_{2}}$$

- Se somarmos as 2 equações de distâncias obtidas:
$$\begin{align*} \frac{n_m}{s_{o1}}+\frac{n_m}{s_{i2}} = (n_l - n_m)\left(\frac1{R_1} - \frac1{R_2}\right) + \frac{n_l d}{(s_{i1} - d)(s_{o2} + s_{i1})} \end{align*}$$

### 2.11.2 - Planos Principais
- Outra abordagem de estudar lentes é considerar que ela contém 2 palnos principais, em que cada um faz os raios convergir em 1 ponto focal:
![[lente dioptro.png|335]]   ![[lente dioptro 2.png]]

- De notar que estes planos não têm que ser os planos principais dos 2 dioptros que compõe a lente. Dito isto, para reduzir o erro desta aproximação basta ajustar a posição destes planos relativamente à posição dos planos dos dioptros.

### 2.11.3 - Pontos Nodais
(Isto já não é uma forma de estudar lentes)
- Alguns raios comportam-se como se passassem pelo centro da lente. Assim, usamos pontos nodais para descrever estes raios.
Ou seja:
![[raio por centro lente.png]]
Um raio que intersete o eixo ótico em $N_{1}$ parece emergir em $N_{2}$.

## 2.12 - Lentes Finas
- São as lentes em que os planos principais estão tão próximos que podemos considerá-los como sendo 1 só, sem estar a criar erros elevados.
- A **equação das lentes finas** é obtida ao aproximar $d\to0$ na equação das distâncias obtida acima, para a representação de uma lente como 2 dioptros. Temos então:
$$\begin{align*} \frac{1}{s_{o}}+\frac{1}{s_{i}} = (n_l - 2)\left(\frac1{R_1} - \frac1{R_2}\right)\end{align*}$$
em que da equação obtida atrás usamos $s_{o1}=s_{o},s_{i2}=s_{i}$ e consideramos que o meio exterior à lente é ar, pelo que $n_{m}\simeq1$

- Podemos reescrever esta equação como:
$$\frac{1}{s_{o}}+\frac{1}{s_{i}}=\frac{1}{f} \quad \quad;\quad \quad \frac{1}{f}=(n_{l}-1)\left(\frac{1}{R_{1}}-\frac{1}{R_{2}}\right)$$
sendo esta a **Equação de Gauss**.

### 2.12.1 - Raios Notáveis
- Podemos analisar isto da mesma forma que analisamos refletores esféricos. A diferença é que agora temos 2 focos, estando estes a distâncias $\pm f$.
![[imagem lente.png]]
- Temos então os raios notáveis:
    - Raios incidentes (vêm da esquerda) paralelos ao eixo ótico que passam no foco $F_{i}$.
    - Raios incidentes que passam no foco $F_{o}$ e que depois da lente se tornam paralelos ao eixo.
    - Raios que passam pelo centro da lente e seguem o seu percurso sem serem afetados pela lente.

#### Potência
- Podemos definir a **Potência** de uma lente como $$P=\frac{1}{f}$$

#### Fatores de Ampliação
Temos o fator de ampliação transversal:
$$m_{T}=\frac{y_{i}}{y_{0}}=-\frac{s_{i}}{s_{o}}$$
e longitudinal:
$$m_{L}=\frac{x_{2}'-x_{1}'}{x_{2}-x_{1}}$$

### 2.12.2 - Combinação de Lentes
![[sistema lentes.png]]
- Na lente 1 temos $$  

\frac1{s_{i1}} = \frac1{f_1} - \frac1{s_{o1}} ~~\to~~ s_{i1} = \frac{s_{o1}f_1}{s_{o1}-f_1}$$
- Na lente 2 temos $s_{o2}=d-s_{o1}$ e obtemos:
$$\begin{align*} \frac1{s_{i2}} = \frac1{f_2} - \frac1{s_{o2}} ~~\to~~ s_{i2} =\frac{(d-{s_{i1}})f_2}{(d-s_{i1}-f_2)} \end{align*}$$
- Pelo que a imagem final da configuração é:
$$s_{i2} = \frac{f_2d - \frac{f_2s_{o1}f_1}{s_{o1}-f_1}}{d - f_2 - \frac{s_{o1}f_1}{s_{o1}-f_1}}$$

#### Fatores de Ampliação Transversal
$$m_{T}=m_{T_{1}}m_{T_{2}}\cdots m_{T_{N}}$$

#### Distância Focal de Lentes Finas em Contacto
$$\frac{1}{f}=\frac{1}{f_{1}} + \frac{1}{f_{2}}+\cdots+\frac{1}{f_{N}}$$

## 2.13 - Aberrações
### 2.13.1 - Aberração Cromática
![[aberração cromatica.png]]
- Resultado do facto que os materiais das lentes terem diferentes índices de refraão para diferentes comprimentos de onda da luz.
- Pode ser substituida ao trocar a lente convexa por uma configuração de lentes com o mesmo poder de ampliação.

### 2.13.2 - Aberração Esférica
![[aberracao esferica.png]]
- Raios incidentes perto das brodas da lente não convergem tão bem.
- Esta aberração pode ser reduzida com uma forma de fabrico diferente.

## 2.14 - Formação de Imagem em Sistemas Óticos
### Matriz de Transferência
- Simplesmente uma matriz que nos dá $x,\theta$ do final do sistema a partir do inicial.

### Formulação ABCD
- Consideramos apenas raios a mover-se num plano que contém o eixo ótico.
- Sendo $e$ a entrada e $s$ a saída, temos:
$$\begin{bmatrix}x_{s}\\ \theta_{e}\end{bmatrix}=\begin{bmatrix}A & B \\ C & D\end{bmatrix}\begin{bmatrix}x_{e}\\ \theta_{e}\end{bmatrix}$$
em que: 
$$  

A = \frac{\partial x_s}{\partial x_e}\quad\quad;\quad\quad B =\frac{\partial x_s}{\partial \theta_e}\quad\quad;\quad\quad C = \frac{\partial \theta_s}{\partial x_e}\quad\quad;\quad\quad D = \frac{\partial \theta_s}{\partial \theta_e}$$
![[matriz transferencia.png]]

- O elemento $A$ é igual ao fator de amplificação transversal $m_{T}$.
- O elemento $B$ é igual a zero quando estamos no plano da imagem.

##### EXEMPLO
- Temos 2 lentes $L_{1},L_{2}$ separadas em $d_{2}$. Elas têm distâncias focais $f_{1},f_{2}$. A distância do objeto a $L_{1}$ é $d_{1}$.
- Para *cada lente* temos as matrizes:
$$T=\begin{pmatrix}1 & \alpha\\0 & 1\end{pmatrix} \quad \quad;\quad \quad M=\begin{pmatrix}1 & 0\\ - \frac{1}{f} & 1\end{pmatrix}$$
em que $\alpha$ é a distância entre os planos.
