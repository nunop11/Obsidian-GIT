# Fibras birrefringentes
- Vimos atrás que:
    - Quando $V<2.405$, apenas temos o modo $\text{LP}_{01}$ 
    - Este modo tem 2 estados de polarização possíveis (x,y como vimos acima), com a mesma constante de propagação. A energia é trocada entre estes 2
- Mas, em certos casos, é importante manter sempre a mesma polarização
- Assim temos fibras *birrefringentes* AKA *polarization maintaining fibers*.
- Removemos a simetria completamente circular da fibra, de uma das 2 formas:
    - Tendo secções transversas **elipticas**
    - Tendo **anisotropia** do material do núcleo
- Assim, *perdemos degenerescência* de polarização
$$\text{birrefringentes}~~~~\to~~~~ n_{1x}\neq n_{1y}~~,~~ \beta_{1x}\neq\beta_{1y}$$

## Anisotropia ótica
- Num material com anisotropia ótica temos:
    - $n_{s}$ - slow, região com maior índice de refração
    - $n_{f}$ - fast, região com menor índice de refração
- A **birrefringência da fibra** é caraterizada como
$$B=n_{s}-n_{f}$$
- Consoante luz se propaga em cada um destes eixos, acumula-se diferença de fase entreas componentes s,f. Numa distânci $L$ temos:
$$\phi_{s}=\frac{2\pi}{\lambda_{0}}n_{s}L \quad;\quad  \phi_{f}=\frac{2\pi}{\lambda_{0}}n_{f}L$$
- Ora, quando tivermos
$$\phi_{s}-\phi_{f}=2\pi$$
então temos:
$$L=\frac{\lambda_{0}}{n_{s}-n_{f}}=\frac{\lambda_{0}}{B}\equiv  L_{b}$$
e temos a **Beat Length**, $L_{b}$.
- Por outras palavras, a polarização muda ao longo da fibra mas volta ao estado inicial a cada intervalo $L_{b}$:
![[beat length.png]]

## Tipos
![[fibras birrefringentes.png]]
- Basicamente, a ideia é remover a simetria entre as direções X e Y

## Resultado
![[efeito de fibra birrefringente.png]]

# Atenuação em fibras
- A intensidade de luz ao longo da propagação $z$ numa fibra, temos perdas devido a *absorção* e *espalhamento*:
$$\begin{align*}
\text{Absorção:} \quad \quad \quad ~~ I(z)_\text{abs}&= I_{0}e^{-\alpha_{a}z}\\
\text{Espalhamento:} \quad \quad \quad I(z)_\text{scatt}&= I_{0}e^{-\alpha_{s}z}
\end{align*}$$
e podemos escrever isto juntando os dois efeitos:
$$I(z)=I_{0} e^{-\alpha z} \quad \quad;\quad \alpha=\alpha_{a}+\alpha_{s}$$
- Podemos ainda ter perdas por reflexão, curvatura, etc
- Consideremos agora a *potência ótica*. Passamos a definir a atenuação com unidades $\text{dB/km}$. 
    - Num sinal que entrou na fibra com $P_{\text{in}}$ e saiu com $P_\text{out}$ após percorrer uma distância $L$ (em km), temos: $$\alpha(\text{dB/km})= \frac{1}{L} 10\log_{10}\left[\frac{P_{\text{in}}}{P_\text{out}} \right]=\frac{1}{L}10\log_{10} \left[\frac{P(z=0)}{P(z=L)} \right]$$
- Nesta equação temos:
    - $1/L$ tem dimensões $\text{km}^{-1}$
    - $10\log_{10}(x)$ tem dimensões $\text{dB}$, em que $x=\frac{P_\text{in}}{P_\text{out}}$

- Assim, temos:
![[atenuacao grafico db.png]]
e escrevemos:
$$P(z)=P(0) e^{-0.23\alpha z} ~~~~,~~~~ 0.23=\frac{\ln10}{10}$$
temos $\frac{\ln10}{10} \cdot \frac{1}{z} 10\log_{10}(x)z= \ln10 \log_{10}(x)=\ln x$ logo fica
$$P(z)=P(0)e^{-\ln x}=\frac{P(0)}{x}=\frac{P(0)}{\frac{P(0)}{P(z)}}=P(z)$$
- Assim, introduzimos o $0.23$ como um meio de fazer as unidades da equação baterem certo.

## Absorção
- Em fibras, temos 2 principais bandas de absorção:

**Infravermelho próximo**
- Associado a vibração de átomos das moléculas
- Temos um *mínimos local* de atenuação: $$\lambda_{0}=1.3\mu\text{m}~~~~~~\to~~~~~~ \alpha=0.3 \text{dB/km}$$
**Ultravioleta**
- Associado a vibração de eletrões externos dos átomos
- Temos um *mínimo absoluto* de atenuação:
$$\lambda_{0}=1.55\mu\text{m}~~~~~~\to~~~~~~ \alpha=0.15\text{dB/km}$$

## Espalhamento/Scattering
- Já vimos aprofundadamente para guias, aplica-se aqui igual
- Ocorrem perdas devido a flutuações da densidade do material
- Temos que a potência perdida por espalhamento é dada por
$$P_\text{scatt}=\frac{\text{constante}}{\lambda_{0}^{4}}$$

## Devido a elementos na matriz de silica
- A presença de certos elementos/impurezas na silica afeta também a atenuação da fibra.
    - Iões OH geram forte atenuação na zona de 1400nm
    - Iões metálicos geram atenuação
    - Dopantes que variem o índice de refração também afetam atenuação
![[tipos atenuacao vs comp onda.png]]

## Modo
- O modo que se propaga só por si afeta a atenuação que ele sofre
- Modos de ordem mais *elevada* propagam-se distância *maiores* e sofrem *maior atenuação*
    - Desta forma, fibras multimodo têm maior atenuação que monomodo. Isto porque em monomodo apenas temos o modo de menor ordem
![[atenuacao de multi e monomodo.png]]

## Curvatura
- Quando curvamos a fibra, a parte do campo transverso que fica de fora do núcleo e na parte externa da curvatura (ver figura) tem de se mover com maior velocidade para conseguir manter a distribuição modal.
    - Aumentar a curvatura aumenta esta velocidade.
    - Eventualmente, uma parte dessa componente do campo atinge velocidade da luz - *perdemos* a radiação e temos **atenuação/perdas**
![[atenuacao curvatura.png]]
- Ou seja, para luz a uma distância radial acima de $x_{c}$ do centro do núcleo perdemos a potência ótica
- Depende do comprimento de onda da luz na fibra, mas de forma geral raios de curvatura acima de 1cm não criam perdas 

## Microcurvaturas
- Este é um tipo de defeito aleatório que podemos ter numa fibra
- Estas surgem devido a não-uniformidades durante o fabrico da fibra ou devido a pressões laterais no cableamento da fibra
![[atenuacao microcurvaturas.png]]

# Dispersão
- Um pulso de luz estreito injetado numa fibra ótica alarga no tempo devido a:
    - Dispersão modal
    - Dispersão material
    - Dispersão de guia de onda
    - Dispersão de modos de polarização
    - Dispersão não-linear

## Dispersão modal
![[dispersao modal intuitivo.png]]
- Consideremos uma fibra com $M$ modos e de comprimento $L$
- Para um modo $q$ temos uma velocidade de grupo $v_{q}$
- Como vimos atrás para fibras step-index:
$$\begin{cases}
v_\text{min}=c_{1}(1-\Delta) \\
v_\text{max}=c_{1}
\end{cases}~~\to~~ \begin{cases}
t_\text{propag|min}=\frac{L}{c_{1}} \\
t_\text{propag|max}=\frac{L}{c_{1}(1-\Delta)}
\end{cases} ~~\to~~ \begin{align*}
\Delta t&= t_\text{propag|min} - t_\text{propag|min}\\
&= \frac{L}{c_{1}} \frac{\Delta}{1-\Delta}
\end{align*}$$
- Usando uma série de Taylor, temos um resultado interessante:
$$\begin{align*}
\frac{1}{1-\Delta}=1+\Delta~~\to~~\Delta t&= \frac{L}{c_{1}}(\Delta+\Delta^{2})\\
&\approx \frac{L}{c_{1}}\Delta
\end{align*}$$

- Injetamos na fibra um pulso muito estreito. Ora, este irá excitar diferentes modos com potências diferentes. De forma geral, o pulso à saída da fibra tem **envolvente gaussiana**
- Consideremos que o pulso à entrada tem largura $\ll\Delta t$.  Definimos a *largura temporal* como sendo $\sigma_{\tau}$, a FWHM da envolvente:
$$\sigma_\tau\approx \frac{L}{c_{1}} \frac{\Delta}{2} ~~~~ \text{= dispersão modal step-index}$$
![[dispersao modal.png]]
- Para fibras longas ($>1\text{km}$) podemos configurar $n_{1},n_{2}$ de modo a ter tempos de propagação max e min que se relacionam de forma que reduzimos a dispersão:
$$\sigma_\tau=\frac{\sqrt{L}}{c_{1}} \frac{\Delta}{2}$$

## Dispersão material
![[dispersao material intuitivo.png]]
- Num meio dispersivo, cada comprimento de onda propaga-se com uma velocidade diferente
![[dispersao material.png]]
- Ou seja, um pulso de luz alarga-se conforme a relação:
$$\sigma_{\tau}=|D_{\lambda}|\sigma_{\lambda}z$$
(para um pulso de valor centrado em torno de $\lambda_{0}$, usamos esse comprimento de onda)
- Temos então:
$$D_{\lambda}=- \frac{\lambda_{0}}{c_{0}} \frac{d^{2}n}{d\lambda_{0}^{2}}$$
e temos
![[dispersao material silica.png]]
- Normalmente temos $L$ em km, $\sigma_{\tau}$ em ps, $\sigma_{\lambda}$ em nm. Assim temos:
$$[D_{\lambda}]=\text{ps/km.nm}$$
- Conforme o gráfico acima:
$$\begin{align*}
\lambda_{0}&= 0.87\mu\text{m}~~\to~~ D_{\lambda}=-80 \text{ps/km.nm}\\
\lambda_{0}&= 1.55\mu\text{m}~~\to~~ D_{\lambda}=+17 \text{ps/km.nm}\\
\lambda_{0}&= 1.312\mu\text{m}\to~~ D_{\lambda}=~0~ \text{ps/km.nm}
\end{align*}$$
e para sílica dopada  13.5% de $\text{GeO}_{2}$ temos $D_{\lambda}=0$ para $\lambda_{0}=1.370\mu\text{m}$

## Dispersão de guia de onda
- A velocidade de grupo do modo depende do comprimento de onda
    - Isto porque ele afeta a porção do modo que se propaga no núcleo e na bainha
    - O núcleo e bainha têm diferentes indices de refração logo têm diferentes velocidades de propagação da luz
    - Essa fração de potência que se propaga em cada meio é dada por $a/\lambda_{0}$
    - Assim, a velocidade de propagação do modo na fibra é a *média ponderada* das velocidades de grupo na bainha e no núcleo
    - Isto é algo que precisamos de considerar em fibras *monomodo* na região de comprimento de onda com **pouca dispersão material**.

### Coeficiente
- Se a extensão da fibra for $L$ o tempo de propagação nela é:
$$\tau=\frac{L}{v_{g}}$$
- Consideremos um pulso muito estreito (delta Dirac, duração temporal zero) excita o modo em questão. À saída teremos um pulso de duração temporal:
$$\Delta\tau=\Delta\left(\frac{L}{v_{g}}\right)= \frac{\Delta\left(\frac{L}{v_{g}}\right)}{\Delta \lambda_{0}}\Delta \lambda_{0}$$
e podemos definir $\sigma_\tau\equiv\Delta \tau$ e $\sigma_\lambda\equiv \Delta\lambda_{0}$. 
- Podemos desenvolver:
$$\begin{align*}
\sigma_{\tau}&= \frac{d\left(\frac{L}{v_{g}}\right)}{d\lambda_{0}}\sigma_{\lambda}=\frac{d\left(\frac{1}{v_{g}}\right)}{d\lambda_{0}}L \sigma_{\lambda}=D_{W}L\sigma_{\lambda}
\end{align*}$$
- E temos o **coeficiente de dispersão do guia de onda**:
$$D_{W}=\frac{d\left(\frac{1}{v_{g}}\right)}{d\lambda_{0}}$$

##### Melhorar a equação de $D_W$
- Temos
$$v_{g}=\frac{d\omega}{d\beta}\quad;\quad V=\frac{2\pi a}{\lambda_{0}}\text{NA}=\frac{a\text{NA}}{c_{0}}\omega_{0}$$
logo
$$\frac{1}{v_{g}}=\frac{1}{\frac{d\omega}{d\beta}}=\frac{d\beta}{d\omega}=\frac{d\beta}{dV}\frac{dV}{d\omega}=\frac{a\text{NA}}{c_{0}}\frac{d\beta}{dV}$$
- Assim:
$$\begin{align*}
\frac{d}{d\lambda_{0}}\left(\frac{1}{v_{g}} \right)&= \frac{d\omega}{d\lambda_{0}} \frac{d}{d\omega}\left(\frac{1}{v_{g}}\right)\\
&= - \frac{\omega}{\lambda_{0}} \frac{d}{d\omega}\left(\frac{1}{v_{g}}\right)\\
&= \frac{-V^{2}}{2\pi c_{0}} \frac{d^{2}\beta}{dV^{2}}\\
\end{align*}$$
ou seja:
$$D_{W}=-\frac{V^{2}}{2\pi c_{0}} \frac{d^{2}\beta}{dV^{2}}$$

- Para o modo $\text{LP}_{01}$ numa fibra step-index temos:
![[beta vs V para lp01.png]]
logo
![[derivadas de beta para lp01.png]]

### Coeficeitne de dispersão cromática
- Temos então o coeficiente 
$$D_\text{cromatica} = D_{\lambda}+D_{W}$$
- Para $\lambda_{0}=1.55\mu\text{m}$, tem-se que $D_{\lambda}=+17\text{ps/km.nm}$
- Assim surge uma pergunta importante: é possível, em fibras, obter uma combinação de coeficientes tal que
$$D_\text{cromatica}=0$$

## Dispersion-shifter fibers
- Este é o tipo de fibra em que foi conseguida dispersão cromática nula.
![[dispersion shift fiber.png]]
- Voltemos ao caso de 1550nm:
    - Ao ajustar o índice de refração como vemos acima, é possível obter $D_{W}=-17\text{ps/km.nm}$
    - Conjugando isto com o que vimos acima, isto quer dizer que para este comp onda temos $D_\text{cromatica}=0$!!!!
- Estas fibras têm então dispersão cromática nula para um comprimento de onda *muito bem definido*
- Com pequenas variações deste comprimento facilmente temos uma dispersão cromática elevada:
![[efeito de dispersion shift fiber.png]]

## Dispersion Flattened Fibers
- Temos agora este perfil de índice de refração:
![[dispersion flat fiber.png]]
que nos dá este comportamento:
![[efeito de dispersion flat fiber.png]]

### Nota final
- Vimos que o mínimo de dispersão material ocorre quando $D_\lambda=0$, em 1370nm.
- Vimos ainda que a atenuação é mínima em 1550nm.
- Ora, vemos que estes 2 valores são relativamente **próximos**! Assim, alterações no fabrico permitiram aproximá-los.

## Dispersão de modos de polarização (PMD)
- No modo espacial $\text{LP}_{01}$ não temos dispersão modal. 
- MAS temos 2 modos de polarização:
    - Polarização linear nos XX
    - Polarização linear nos YY

- Quando a fibra é mesmo circular e feita de um meio isotrópico, temos degenerescência dos modos de polarização.
    - Mas na realidade as fibras NÃO são assim! Temos desvios locais de isotropia, desvios de simetria circular, curvatura da fibra, etc
    - Tudo isto contribui para a criação de **dispersão de polarização**
![[dispersao polarizacao.png]]

- Numa extensão $i$ "pouco longa" da fibra podemos identificar a orientação do eixo rápido ($n_{f}$) e lento ($n_{s}$)
- Mas se formos ver uma secção seguinte $i+1$ provavelmente iremos ter uma orientação diferente.
- Isto vai-se acumulando ao longo de kms de fibra e ficamos com dispersão da polarização.
- Eventualmente, temos que esta dispersão é *não linear* com o comprimento:
$$\sigma_\text{PMD}=D_\text{PMD}\sqrt{L}$$
em que temos o coeficiente de PMD:
$$D_\text{PMD}\in[0.1,1]\text{ps/}\sqrt{\text{km}}$$

## Dispersão não-linear
- Quando a intensidade da luz é muito intensa, aparecem **efeitos não lineares**
- Como o perfil de intensidade de um modo fundamental é ~gaussiano, temos mais potência na parte central da fibra. 
- Ora, se o feixe for muito intenso, o índice de refração da própria fibra **varia** nessa zona central. Chamamos a isto _self-phase modulation_
    - Isto gera um pulso que se propaga sem alterar a sua forma: um solitão
    - Este efeito eventualmente elimina a dispersão material

## Resumo de dispersões
![[tipos dispersao.png]]

# Amplificação
- Numa ligação subaquática de fibra temos milhares de km. Com atenuações normais perderiamos o sinal todo em algumas centenas
- Assim, torna-se importante *amplificar* sinais óticos em fibras
- Até ao início da decada de 90, a única opção era:
![[amplificacao v0.png]]
- Isto é pouco elegante e pouco eficiente. Também limitava a bandwidth

**O que queremos**
- A solução ideal seria amplificação ótica - amplificar o sinal ótico diretamente, sem o converter em sinal elétrico.
- Na década de 80, estudou-se muito *comunicações óticas coerentes*, mas não funcionou bem o suficiente. Vamos ver porquê

## Comunicação coerente
- Em sistemas eletrónicos normais, enviamos informação na forma de código **binário**. Ou seja, usando 0s e 1s, podemos codificar todas as letras, número e simbolos.
- Mas como fazemos isso com um **campo ótico**??

- Uma onda plana pode ser escrita como: $\vec{E}=E_{0}\hat{e}\cos(\omega t-\vec{k}\cdot\vec{r})$. Podemos codificar o 0 e 1 como:
    - Níveis de amplitude (luz ligada e desligada): $E_{00},E_{01}$
    - Níveis de polarização: $E_{\parallel},E_{\perp}$
    - Níveis de fase: $\phi_{1},\phi_{2}$
- A forma mais simples é *modulação da amplitude* do campo (ligar e desligar)
    - Esta forma é simples, sim. Mas NÃO é a mais eficiente: mudar de nível de energia obrigada a cargas e descargas de condensadores

### Fase
- Uma opção mais atrativa seria modulação de fase:
$$U_{s}=U_{0s}e^{i(2\pi\nu _{s}t + \phi_{s})} \quad \quad\Biggr|~~ \Tiny{\begin{align*}
\phi_{s}&= \frac{2\pi n\ell}{\lambda_{0s}}+\phi_{0}\\
\nu_{s}&= \frac{c_{0}}{\lambda_{0s}}
\end{align*}}$$
(em que $\ell$ extensão da fibra, $n$ indice de refração, $\lambda_{0s}$ comprimento de onda da luz, $\phi_{0}$ fase inicial)

![[amplificacao fibra.png]]
- Mas quando temos campo de baixa amplitude, precisamos de o amplificar para poder medir a fase. Considere-se a fonte laser $U_{L}=U_{0L}e^{i(2\pi\nu_{L}t + \phi_{L})}$, que queremos usar para amplificar o sinal. Em cima entra o sinal (fonte de sinal) que queremos amplificar e no final temos o sinal de saída.
- A intensidade do sinal de saída é:
$$I_\text{out}=\frac{|U_{s}+U_{L}|^{2}}{2\eta}=I_{0s}+I_{0L} + 2 \sqrt{I_{0s}I_{0L}}\cos[2\pi(\nu_{s}-\nu_{L})t + (\phi_{s}-\phi_{L})]$$
e $2 \sqrt{I_{0s}I_{0L}}\cos[2\pi(\nu_{s}-\nu_{L})t + (\phi_{s}-\phi_{L})]$ é o termo de *interferência*. Temos ainda que $\eta$ é a impedância do meio.

- Como a fonte $U_{L}$ é local, pode ter potência muito elevada - no termo de interferência geramos ganho.
- Como este sinal será consistente e estável, podemos medir a fase! Definimos 2 níveis/valores de fase que serão o 0 e 1.

### O problema
- Ora, como vemos, a fonte do sinal e a fonte de laser $U_{L}$ estão em extremidades diferentes do coupler. Assim, a diferença de fase medida irá flutuar aleatoriamente.
- Isto quer dizer que **não temos coerencia** entre os sinais.
- Ora, sistemas de comunicação coerente ainda não são algo fazível

## Amplificação ótica - Érbio
- Érbio é um *lantanídio*:
![[erbio.png]]
- Quando colocado numa matriz de sílica, fica na forma de ião:
$$\text{Er}^{3+}=[\text{Xe}]4f^{11}$$
![[transicoes energia erbio.png]]
- Neste átomo, ao fornecer luz com comp onda 980nm, podemos excitar eletrões que passam para níveis de maior energia
- Esses níveis de maior energia têm tempo de vida muito curto e descem logo para o estado intermédio de forma não-radiativa
- Essa banda intermédia já é *estável*! Quando muitos eletrões se concentram nesta banda, eles descem e emite-se radiação com comp onda (1520-1570)nm
    - Recordemos que o mínimo de atenuação da fibra acontece para 1550nm
- Assim, ao excitar os átomos com um comprimento de onda (980nm), emitimos luz com um comprimento diferente (1550nm) que temos *menos atenuação*. Isto parece ser algo que nos permite criar **ganho**

### Como incorporar?
- Ora, tendo este elemento que parece tão util, surge uma pergunta: como fazemos a luz da fibra passar no erbio?
- Descobriu-se que a solução era **dopar a fibra com érbio**
![[amplificacao erbio.png]]
- Ou seja, ao laser de 980nm que usamos para subir eletrões para a banda mais energética chamamos de *laser de bombagem*

**NOTA**
- Olhando para o diagrama de bandas, vemos que podemos bombar eletrões diretamente para a banda intermédia com luz de 1480nm. 
- Mas nesse caso temos uma inversão de população mais fraca e temos menos ganho ótico.

### Rede de comunicação
![[edfa em sistemas reais esquema.png]]
- Vemos que o sinal fica sempre na forma ótica, apenas sendo convertido para sinal eletrónico no final.

- Além disso, ao usar fibras dispersion-flattened garantimos *muito baixa dispersão* para ~1550nm. Assim, podemos fazer um sistema em que cada fibra leva muitos "canais" com comprimentos de onda diferentes
![[multiplexacao comp onda.png]]

# Fibras Graded-Index
- Fibras step-index foram as primeiras a ser estudadas para sistemas de comunicação. Mas inicialmente era difícil fazer fibras muito finas.
    - Ora, isso era importante porque em fibras step index temos que ter mudança de indice de refração muito abrupta entre bainha e nucleoo
    - Para $2a<10\mu\text{m}$ tornava-se muito dificil o fabrico
- Assim, surgiram as fibras **graded-index**
![[graded index fiber.png]]
ou, mais detalhadamente:
![[graded index fiber esquema n.png]]

e definimos:
$$n^{2}(r)=\begin{cases}
n_{1}^{2}\left[1- 2 \left(\frac{r}{a}\right)^{p}\Delta\right] & ; & r\le a \\
n_{2}^{2} & ; & r>a
\end{cases}$$
- E consoante aumentamos $p$ (perfil de variação de $n$), temos:
![[graded index fiber diferentes p.png]]
- Para $p=2$, o fabrico é **bastante fácil**. 
- A vantagem destas fibras é que modos de maior ordem têm *maior velocidade de propagação*.
- Já modos de menor ordem enfrentam maior indice de refração e têm *menor velocidade*
- Estas 2 coisas fazem sentido: o perfil é ~parabólico, com maior $n$ no centro. Sabemos ainda que modos de maior ordem movem-se mais nas beirias, de menor ordem movem-se mais no centro
![[propagacao graded index.png]]

## Raios
- Raios *meridionais* continuam a descrever uma trajeória igual - dentro de um raio $R_{0}$
![[raios meridionais graded index.png]]

- Raios *oblíquos* descrevem trajetórias helicoidais, entre os raios $r_{\ell}$ e $R_{\ell}$
![[raios obliquos graded index.png]]

- Seguindo a lógica que vimos para fibras step-index temos:
$$\begin{align*}
p_\text{otimo}&= 2(1-\Delta)\\
\sigma_{\tau|\text{min}}&\approx \frac{L}{c_{1}} \frac{\Delta^{2}}{16}\\
\end{align*}$$
no caso da dispersão modal, isto dá-nos uma melhoria de um fator de $\Delta/8$ !!!!