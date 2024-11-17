### Abstract
- **Expansão Térmica Negativa := NTE** -- quando um material contrai quando a sua temperatura baixa. Tem várias aplicações
- Neste artigo estuda-se manipulação de NTE em $\text{Mn}_{0.95}\text{Ni}_{0.05}\text{CoGe}$ (*CoGe*) através de MS (magneto estrutural) coupling a temperatura ambiente (275-345K).

### Intro
- Já foi suferido que NTE ocorre devido a desordens locais da estrutura e/ou transições de fase
    - Ambos estes casos foram comprovados em vários processos e materiais diferentes
- Controlar NTE é útil. Alguns métodos funcionais que já existem: modificação química, dopagem, nanoestruralização, hidratação, aplicar pressão.
- Vejamos manipulação de NTE de CoGe de forma magnética.

**Este composto em si**
- Para um composto de CoGe com Indium podemos atingir contração de 3.9% (muito)
- Estes compostos têm 2 fases estáveis:
    - uma fase de baixa temperatura com estrutura ortorrombica
    - uma fase de alta temperatura com estrutura hex do tipo Ni2In  
![[estrutura hex vs orto.png]]
- Estas estruturas ortorrômbica e hexagonal relacionam-se com:
    - $a_{ort}=c_{hex}$
    - $b_{ort}=a_{hex}$
    - $c_{ort}/\sqrt{3}=a_{hex}$
    - $V_{ort}/2=V_{hex}$

- Na amostra parent de McCoGe ocorre uma transição ort-hex a $T_{M}=650K$. Esta pode ser baixada usando dopagem.
- Cada uma das estruturas (só por si) tem ordenamento magnético a temperaturas $T_{C}^{ort}=345K~,~T_{C}^{hex}=275K$. 
    - Ora, se conseguirmos baixar $T_{M}$ de forma a ficar entre 275 e 345K temos *manipulação magnética de NTE*.
    - Isto é o MS coupling - temos uma interligação entre as temperaturas de ordenamento magnético e a temperatura a que mudamos de fase estrutural - controlamos o comportamento magnético e estrutural com a temperatura.
- Neste artigo (e no nosso PEEC) isto foi feito com substituição parcial de Mn por Ni.

### Secção Experimental
**Preparação de amostra**
- As amostras de $\text{Mn}_{0.95}\text{Ni}_{0.05}\text{CoGe}$ foram feitas através de arc melting quantidades precisas de Mn,Ni,Co,Ge (Manganês, Níquel, Cobalto e Germânio) num atmosfera de argon
    - Cada amostra foi derretida 4 vezes para ter mais homogeneidade
- Os ingots obtidos disto foram embrulhados com tantalo e colocados em tubos de quartzo. Foram postos em vacuo a 850ºC por 7 dias para sofrerem annealing. Depois colocados em água gelada
- Depois os pós foram moidos (almofariz) por 5 minutos até ficar em pó

**Difração Raio X**
- Foi feita difração raio X a temperatura ambiente
- Também foi feita difração raio X no range de temperaturas 20-310K

**Medição de Propriedades Físicas**
- Foi feita medição da magnetização em função da temperatura num PPMS. Feita leitura com um rate de aquecimento de 3K/min no range 2-345K

**Medições NPD**
- NPD = Neutron Power Diffraction
- Mais ou menos como difração raio X, mas com neutrões

### Resultados
#### NTE sem campo
![[constantes rede vs T.png]]
- Temos acima a evolução dos 3 parâmetros de rede ao longo da temperatura.
- A tracejado temos $T_{M}$, que desceu de 650K para 290K. Este valor foi encontrado porque é a essa temperatura que estamos mais próximos das relações ort-hex descritas acima (e indicadas na esquina inferior direita do gráfico)
- As estruturas foram determinadas com os dados de NPD usando refinamento de Rietveld (técnica de caraterização através de NPD e XRD para amostras em pó)

- A figura abaixo mostra (não sei como) que na transição $a_{hex}\to c_{ort}/\sqrt{3}$ não temos grande contração. Mas na transição $a_{hex}\to b_{ort}$ temos uma elevada expansão. Opostamente, na transição $a_{ort}\to c_{hex}$ temos uma contração enorme. 	
    - Tudo isto pode ser visto no gráfico acima.
![[heatmap constantes rede.png]]
- Esta contração enorme faz com que o volume da célula unitária diminua, por um fator de -3.74%. Isto é similar ao obtido com outros compostos com Mn, Co e Ge.

- Podemos fazer o calculo dos parametros de rede e volume médios: $L_{average}=L_{rot}f_{rot} + L_{hex}f_{hex}$ (em que $f$ é a phase fraction)
![[volume cell vs T.png|374]]
temos então os valores médios:
![[parametros rede vs T 2.png|375]]
notemos que isto apenas compreende um intervalo de 50K.
- Podemos fazer o seguinte gráfico:
![[anisotropia material.png]]
que mostra que há forte anisotropia no NTE do material - uma direção aumenta (eixo $b$, vermelho) e outra contrai (eixo $a$, azul). O $\alpha$ é o coficiente de expansão

#### NTE com campo
- Isto foi estudado com medição em NPD, com campos de 0,2,5,8 Tesla.
- A temperatura de transição de fase, $T_{M}$, aumenta com o aumento do campo.
- O que acontece é:
![[elongamento e contracao com campo.png|400]]
No primeiro gráfico temos $\Delta L/L$ no eixo de $a_{ave}$. No de baixo temos $\Delta V/V$ do volume da célula unitária. Nos gráficos pequenos dentro temos as mesmas variáveis, mas em função do campo para $T=295K$
- De uma forma resumida, temos que os coeficientes de expansão termica $\alpha_L,\alpha_V$ reduzem substancialmente (as amostras contraem e expandem menos - ficam mais perto da dimensão original)
![[valores de indice de expansão com campo.png]]

#### Resposta microscópica ao campo
- Para estudar melhor o NTE, analisou-se ainda a relação entre a temperatura e a magnetização ZFC (zero field cooled - arrefecido sem campo externo). Isto foi feito a vários campos no range 0.01-9T.
![[magnetização vs T.png|284]]
Usando os mínimos das derivadas, determinou-se para cada curva a temperatura de transição $T_{C}$. 

- Juntando estas $T_{C}$ com as $T_{M}$ medidas com NPD:
![[tM vs tC.png|164]]
vemos que a campos acima de 2T, Tc e Tm parecem seguir a mesma tendência (derivadas iguais). A diferença de alturas das retas deverá ser causada por terem sido usados rates de aquecimento a medir as 2 temperaturas.
- A variação simultanea e em sintonia de Tc e Tm no range 2-8T indica mais uma vez que temos MS coupling forte - uma das temperaturas está relacionada com a estrutura cristalina do material, outra com o seu comportamento magnético e no entanto ambas respondem de modo igual a campos externos. 
- Ora, a transição magnética a que $T_{C}$ está associada não é uma transição "normal" em que ocorre ordenamento de momentos magnéticos de forma espontanea numa temperatura critica. A transição que ocorre é fortemente relacionada com a transição estrutural de ortorrômbica (ferromagnetica) para hexagonal (paramagnetica)
    - Isto é comum em materiais magnetocaloricos com MS coupling

- Os momentos magnéticos sobem entre 0-2T e em 2T saturam:
![[momento mag vs T.png]]
o que explica porquê que Tc sobe mais rapido que Tm na gama 0-2T

**Campo e parametros de rede**
![[elongamento vs Campo por T.png]]****
- Outro fenomeno a notar é que os efeitos do campo nos parametros de rede só ocorrem a temperaturas próximas da de transição MS. 
- Temos a relação Clausius-Clapeyron:
$$\mu_{0} \frac{dH}{dT}=\frac{\Delta S_{M}}{\Delta M}~~;~~ \Delta T=\mu_{0} \left( \frac{\Delta M}{\Delta S_{M}} \right)\Delta H$$
- Aqui temos que $M,S$ são magnetização e entropia e os Delta representam as variações destas grandezas entre as fazes orto e hex do material.
- $\Delta T$ é a variação de temperatura que ocorre ao variar o campo em $\Delta H$.
- Assim, para causar uma forte variação de temperatura é preciso que $\Delta M$ seja elevado e $\Delta S_{M}$ reduzido.
- Temos que $T_{C}^{ort},T_{C}^{hex}$ são inferiores à temperatura de Curie do composto normal. Temos ainda que $M_S^{ort}>M_S^{hex}$ (magnetização de saturação). Isto pode tudo ser representado assim:
![[transição vs Campo.png]]
- Como $T_{M}$ está algures no range 275-345K, temos $\Delta M$ máximo na transição direta orto$\to$hex. Isto também permite ter o MS coupling máximo, podendo-se então ter um maior efeito magnético sobre o material.
- Uma tabela que sumariza a relevância deste material:
![[expansao termica varios materiais.png]]
