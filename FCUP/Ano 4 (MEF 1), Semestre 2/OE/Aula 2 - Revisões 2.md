## Resposta ótica do meio
- O meio gera polarização/magnetização em resposta aos campos E,H.
- Mais concretamente:
    - $\vec{P}$ depende de $\vec{E}$
    - $\vec{M}$ depende de $\vec{H}$
- Normalmente, nas frequências e meios óticos temos uma baixa susceptibiliadde magnética logo temos $\vec{M}\simeq\vec{0}$. Por outras palavras, quase podemos ignorar o campo magnético e a magnetização.
- Assim, num meio ótico, as *proriedades óticas* são completamente definidas pela relação entre $\vec{P},\vec{E}$
- Essa relação é definida pela **susceptibilidade elétrica**: $\chi$
    - A susceptibilidade é uma grandeza tensorial de 3ª ordem: $$\vec{P}=\varepsilon_{0}\chi* \vec{E}=\varepsilon_{0}\int_{-\infty}^{t}\iiint_{\vec{r'}}\chi(\vec{r}-\vec{r'},t-t')\vec{E}(\vec{r'},t')d\vec{r'}dt'$$  (convolução)
    - Podemos ver esta convolução como definindo que a Polarização num ponto $\vec{r}$ depende de todos os pontos $\vec{r'}$ que o rodeiam. Podemos também ter um efeito de memória, logo não só o instante $t$ atual importa como também $t'<t$.
 
**Permitividade**
- Num certo meio temos: $\vec{D}=\varepsilon_{0}\vec{E}+\vec{P}$
- Podemos definir a *permitividade elétrica do meio* : $\varepsilon(\vec{r},t)$
    - Esta também é uma grandeza tensorial de 3ª ordem: $\vec{D}=\varepsilon * \vec{E}$ (convolução) $$\vec{D}=\varepsilon* \vec{E}=\int_{-\infty}^{t}\iiint_{\vec{r'}}\varepsilon(\vec{r}-\vec{r'},t-t')\vec{E}(\vec{r'},t')d\vec{r'}dt'$$(convolução)

**Permitiviade e susceptibilidade**
- Podemos definir a relação:
$$\varepsilon(\vec{r},t)=\varepsilon_{0} \left(\delta(\vec{r})\delta(t)\mathbf{I} + \chi(\vec{r},t) \right)$$
que num meio isotrópico e homogéneo fica:
$$\boxed{\varepsilon_{r}=\frac{\varepsilon}{\varepsilon_{0}}=1+\chi}$$
- Podemos ainda ver que, como $\varepsilon,\chi$ relacionam diretamente: $\vec{P}\Leftrightarrow \vec{E}$ e $\vec{D}\Leftrightarrow \vec{E}$, então estas 2 grandezas caraterizam *completamente* a resposta do material!

**Exemplo**
![[decaimento campo pulso.png|600]]
- Nota: nesta imagem, o campo elétrico é apenas um delta de Dirac em $t'$. 
- Este campo cria dipolos positivos. Depois de o campo desaparecer, os dipolos diminuem, mas fazem overshoot e tornam-se negativos. Assim, voltam a aumentar mas fazem overshoot outra vez. Assim adiante até lentamente se tornar zero.

## Equação de Onda
$$\boxed{\begin{align*}
\nabla \cdot \vec{D}&= \rho_{\text{livre}} &&&& \textsf{(Lei de Gauss)} \\
\nabla \cdot \vec{B}&= 0 &&&& \textsf{(Sem nome)}\\
\nabla \times \vec{E}&= -\partial_{t}\vec{B} &&&& \textsf{(Lei de Faraday)}\\
\nabla \times \vec{H}&= \vec{\mathcal{J}}_{\text{livre}} + \partial_{t}\vec{D} &&&& \textsf{(Lei de Ampere-Maxwell)}
\end{align*}}$$
- Estas foram definidas ao formar uma série de observações experimentais
- Mas depois foi descoberto/confirmado que se baseiam em 4 pressupostos:
    - O universo tem 4 dimensões (1 temporal, 3 espaciais)
    - Existem cargas elétricas e elas exercem forças entre si
    - Existe conservação de carga
    - A matéria está limitada pela velocidade da luz
o prof comparou a forma como estas equações têm por base estre pressupostos à forma como a mecânica quântica tem como base os seus postulados. A diferença é que a mecância quântica foi criada tendo em conta os postulados, Maxwell não.

**Dedução**
- Temos que: $\nabla \times \vec{E}=-\partial_{t}\vec{B}$. E sabemos ainda que: $\vec{B}\approx \mu_{0}\vec{H}$
- Ficamos com: $$\nabla \times \vec{E}=-\mu_{0} \partial_{t}\vec{H}$$
- Fazemos o rotacional disto:
$$\begin{align*}
\nabla \times (\nabla \times \vec{E})&= -\mu_{0} \nabla \times \partial_{t}\vec{H}\\
&= -\mu_{0} \partial_{t}(\nabla \times \vec{H})
\end{align*}$$
- Sabemos que $\nabla \times \vec{H}=\partial_{t}\vec{D} + \mathcal{J}$. Assumindo que não há carga livre, ficamos com:
$$\nabla \times(\nabla \times \vec{E}) + \mu_{0} \partial_{t}^{2}\vec{D}=0$$
- Assim, sendo $\vec{D}=\varepsilon_{0}\vec{E} + \vec{P}$, obtemos a equação de onda.

**Equação**
- Temos então:
$$\nabla \times (\nabla \times\vec{E}) + \frac{1}{c^{2}} \partial_{t}^{2}\vec{E} = -\mu_{0} \partial^{2}_{t}\vec{P}$$
- Na deduçã assumimos que:
    - Não há cargas livres nem correntes externas
- Para o campo H existe uma equação equivalente.
- Temos: $$c^{2}=\frac{1}{\mu_{0}\varepsilon_{0}}$$

### No vazio/vácuo
- Não há meio, logo não há polarização do meio.
- Ficamos com $$\nabla \times (\nabla \times \vec{E})=- \frac{1}{c^{2}} \partial_{t}^{2}\vec{E}$$
evidentemente isto tem a mesma forma que $\partial_{x}^{2}u=\frac{-1}{v^{2}}\partial_{t}^{2}u$, a equação de onda!

**Filosofia do vácuo**
- O prof realçou que vácuo não é necessariamente "vazio" mas sim a ausência de matéria e radiação.
- Apesar de "simples", o vácuo não é completamente compreendido. Existe o efeito --- (slide 35) que consiste no facto que um corpo em movimento enquanto imerso num vácuo sente/recebe radiação EM na forma de calor!
- Ou seja, a progapação de ondas EM no vácuo, apesar de descrita de forma geral com equações de Maxwell, pode implicar a oscilação de certas propriedades do vácuo. No entanto, isto é um assunto em aberto pelo que muito simplesmente não entendemos estes mecanismos nem de onde vêm. 
- Assim, por detrás do espaço-tempo poderá haver um constante murmuro/oscilação, que poderá até explicar o princípio de incerteza de Heisenberg

### Representação analítica de campos óticos
- Criamos uma função analítica $f_{an}$ a partir de uma função real.
- Para um $f$ real e causal, fazemos uma transformada de Hillbert para uma função no tempo e temos:
$$\mathcal{H}[f(t)]=\hat{f}(t)= \frac{1}{\pi}\int_{-\infty}^{t} \frac{f(\tau)}{\tau-t}d\tau$$
 - A função analítica é então:
$$f_{an}=f+ j \hat{f}$$
- Na prática, a transformada de Hillbert introduz um atraso de 90º no sinal $f$.
- Por exemplo: 
    - Temos $f(t)=\cos(\omega_{0}t)$. 
    - A sua transformada de Hillbert é $\hat{f}(t)=\sin(\omega_{0}t)$ que tem mesmo um atraso de 90º
    - Temos então a função analítica: $f_{an}=\cos(\omega_{0}t)+j\sin(\omega_{0}t)$
    - E podemos escrever isto na forma: $f_{an}=e^{j\omega_{0}t}$
- Ora, podemos escrever as funções na forma exponencial complexa precisamente devido à introdução da fase de 90º. 
- Mas, recordemos *sinais e sistemas*, sabemos que determinar a saída de um SLIT é *muito mais fácil* quando temos a entrada na forma exponencial complexa!
- Mas, claro, nós teremos a entrada sendo $f$, real. A função analítica *não* é a entrada. Felizmente, basta calcular a saída para $f_{an}$ e depois simplesmente obtemos a parte real dessa saída!
    - $f_{an} = f + j \mathcal{H}[f]$
    - $y_{an} = \text{resposta}[f_{an}]$
    - $y = \text{Re}[y_{an}]$

### Agora para o campo
- O sinal analítico do campo E de uma onda EM monocromática é:
$$\vec{E}=\vec{E}_{0} e^{i(\vec{k}\cdot\vec{r} - \omega t)}= \hat{e} E_{0} e^{i(\vec{k}\cdot\vec{r-\omega t})}$$
- Temos:
    - $\hat{e}$ - direção da polarização. Se for constante temos polarização linear. Se variar com $t$ temos polarização elíptica/circular
- Consideremos que o campo se propaga segundo $z$. Nesse caso, temos que o campo existe nas direções x e y: $$\vec{E}_{0}=\hat{e}E_{0}=\hat{x}E_{0x}+\hat{y }E_{0y}$$

**Amplitude**
- Mas podemos ter um atraso entre as componentes $x,y$. Assim, estas amplitudes $E_{0x},E_{0y}$ são na realidae amplitudes complexas!
- Temos então $$E_{0x}=|E_{0x}|e^{i\phi_{x}} \quad;\quad E_{0y}=|E_{0y}|e^{i\phi_{y}}$$
- Podemos então caraterizar a onda com 2 parâmetros:
    - *Diferença de fase* entre x e y: $$\phi=\phi_{y}-\phi_{x}$$
    - *Ângulo de polarização*: $$\alpha=\arctan \left(\frac{|E_{0y}|}{|E_{0x}|} \right)$$

- Podemos então escrever a amplitude:
$$\vec{E_{0}}=E_{0} \left[\cos\alpha \hat{x} + e^{i\phi}\sin\alpha \hat{y} \right]$$

**Onda**
- Podemos então reescrever a onda:
$$\vec{E}(z,t)=\vec{E_{0}}e^{i(kz-\omega t)}=E_{0} \left[\cos\alpha \hat{x} + e^{i\phi}\sin\alpha \hat{y} \right] e^{i(kz-\omega t)}$$
- Como vimos, o nosso campo verdadeiro é apenas a componente real disto. Este é dado por:
$$\vec{E}(z,t)= \frac{\vec{E}+\vec{E}^{*}}{2}=E_{0}\bigg([\cos\alpha \cos(kz-\omega t)]\hat{x} + [\sin\alpha\cos(kz-\omega t+\phi)]\hat{y}\bigg)$$

### Tipos de polarização
![[polarizacao esq e dir.png]]

#### Polarização elíptica
- É a solução mais geral: quando $E_{0x},E_{0y}$ têm amplitude e fase diferentes.
- O conjunto $(\phi,\alpha)$ pode ser qualquer combinação
    - Se $\phi>0$ o campo $\vec{E}$ roda no sentido oposto aos ponteiros do relógio para alguém que vê o campo a vir na sua direção
    - Se $\phi<0$ o campo roda no sentido dos ponteiros do relógio

#### Polarização linear
- Quando temos $\phi=0$ ou $\phi=\pi$
- Neste caso teremos que $\alpha$ é *constante no tempo*. Assim, também o versor $\hat{e}$ é CONSTANTE
- A onda tem apenas uma orientação

#### Polarização circular
- Caso mis restrito
- Temos necessariamente $|E_{0x}|=|E_{0y}|$ e $\phi=\pm \frac{\pi}{2}$
- Ficamos com $$\vec{E_{0}}=\frac{E_{0}}{\sqrt{2}}(\hat{x}\pm i\hat{y})$$
- Assim, se $\phi=+ \frac{\pi}{2}$ temos $\vec{E_{0}}=\frac{E_{0}}{\sqrt{2}}(\hat{x}+ i\hat{y})$ AKA *polarização circular esquerda* e podemos definir o versor dessa direção $\hat{e}_{+}=\frac{\hat{x}+i \hat{y}}{\sqrt{2}}$
- Assim, se $\phi=- \frac{\pi}{2}$ temos $\vec{E_{0}}=\frac{E_{0}}{\sqrt{2}}(\hat{x}- i\hat{y})$ AKA *polarização circular direita* e podemos definir o versor dessa direção $\hat{e}_{-}=\frac{\hat{x}-i \hat{y}}{\sqrt{2}}$
![[polarizacao esq e dir 2.png]]
(a fase não bate certo mas deve ser uma daquelas cenas de notação de ótica. Provavelmente quem fez esta imagem usou $\phi=\phi_{x}-\phi_{y}$)

## Interação de campos óticos com a matéria
- Um campo incide num material, a radiação EM incide em partículas que são movidas. Ou seja, são aceleradas.
- Como sabemos, um eletrão acelerado emite radiação (EM) que irá reagir com o campo incidente e na prática afetar a resposta.

- A resposta do meio a um campo E consiste na sua polarização. 
**Meio não dispersivo** - A polarização apenas depende do campo no instante atual, não dependendo dos campos passados. Ou seja, o material não tem "memória". Isto é uma idealização porque todos os materiais têm um certo tempo de resposta
**Meio homogéneo** - A relação entre $\vec{P},\vec{E}$ é independente das coordenadas espaciais
**Meio isotrópico** - A relação entre $\vec{P},\vec{E}$ é independente da direção do campo, pelo que $\vec{E}\parallel \vec{P}$
**Meio espacialmente não dispersivo** - A polarização num ponto apenas depende do campo nesse pontos, não é afetado pelos campos nos pontos vizinhos.

- Consideremos o caso mais simples:
### Meio Linear, não-dispersivo, *homogéneo e isotrópico*
- Neste caso ficamos com $$\vec{P}=\varepsilon_{0}\chi \vec{E}$$
- Assim, podemos escrever: $\vec{D}=\varepsilon \vec{E}$, em que:
$$\varepsilon=\varepsilon_{0}(1+\chi)$$
e definimos $\varepsilon_{r}=\varepsilon/\varepsilon_{0}$
- Definimos então o *índice de refração*: 
$$n= \frac{c_{0}}{c}=\sqrt{\varepsilon_{r}}=\sqrt{1+\chi}$$
($c_{0}$ - velocidada da luz no vácuo, $c$ - velocidade da luz no meio)

### Meio Linear, não-dispersivo, *não-homogéneo* e isotrópico
- A propagação do campo ótico num meio assim é descrita por:
$$\nabla^{2}\vec{E} + \nabla \left[\frac{1}{\varepsilon}\nabla \varepsilon \cdot \vec{E} \right] = \mu_{0} \varepsilon \partial_{t}^{2} \vec{E}$$
- Mantêm-se as fórmulas que vimos acima (de $n,\varepsilon$) mas agora temos que $\varepsilon$ é na realidade  $\varepsilon(\vec{r})$. Isto torna todo o comportamento mais instável. 
    - Claro, se $\varepsilon$ for constante, o gradiente acima torna-se nulo e voltamos à equação do sistema homogéneo

### Meio Linear, não-dispersivo, homogéneo e *anisotrópico*
- Neste caso, a direção de $\vec{E}$ importa muito.
- Em geral, como também já vimos, $\vec{E}\parallel\vec{P}$
- Dizemos então:
$$P_{i}=\sum\limits_{j}\varepsilon_{0}\chi_{ij}E_{j}$$
ou seja: **a susceptibilidade é um tensor 3x3**!!!
- Por palavras: cada componente de $\vec{P}$ é uma média pesada das componentes de $\vec{E}$
- A mesma lógica surge para o campo total:
$$D_{i}=\sum\limits_{j}\varepsilon_{ij}E_{j}$$