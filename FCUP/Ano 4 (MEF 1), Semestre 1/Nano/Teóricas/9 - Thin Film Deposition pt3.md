# 1 - CVD (chemical vapor deposition)
![[cvd figura.png]]
- Este tipo de estrutura pode ser feito com CVD
![[cvd.png]]
- Usamos gases reativos (não inertes). Os gases são diretamente depositados no substrato
- Isto permite ter um controlo exato da estequiometria
- A step coverage consegue ser ótima e temos boa adesão

**Vantagens**
- É possível ter deposição rápida e com boa replicabilidade
- Permite depositar materiais dificeis de evaporar
- Pode fazer filmes epitaxiais
- Melhor coverage e film

**Desvantagens**
- Alta temperatura
- Alguns gases são tóxicos
- O filme pode não ser puro (hidrogénio pode aderir e etc)

## Reatores CVD
- O reator tem que conseguir fazer:
    - transporte do reagente e diluente para dentro da câmara
    - fornecer calor à câmara de reação
    - remover e deitar fora os produtos indesejados da reação
    - fazer um bom film com baixas contaminações
![[cvd montagem.png]]

- Os materiais fonte devem ser:
    - estáveis à temp ambiente
    - voláteis mas não demasiado
    - reagem a temperaturas abaixo da temperatura de fusão do substrato
    - criam os elementos que queremos, gerando side-products fáceis de remover
    - pouco tóxicos de preferência
- As fontes podem ser:
    - gases (mais fácil)
    - líquidos voláteis
    - sólidos sublimáveis
    - combinação destes 3 acima
- O substrato tem que ser escolhido tendo em conta a reação que queremos

![[materiais de cvd.png]]

#### Passos
1. Introduzimos elementos reativos no reator
2. O gás é ativado por calor ou plasma, ocorrem reações homogéneas no estado gasoso e os reagentes difundem-se para a superfície
3. São absorvidos pela superfície
4. A reação ocorre na superfície, de forma heterogénea
5. Desaborção dos reagentes da superfície
6. Os produtos são removidos da superfície
7. Reagentes ejetados do reator pelo exaust
![[cvd passos.png]]

- O rate de deposição é decidido pelo processo mais lento deste 7
    - Normalmente, isto costuma ser o transporte para ou para fora da superfície OU a reação na superfície (que depende da temp)
- É então importante que todas as zonas da superfície recebam as mesmas quantidades de reagente
- A forma como a reação ocorre consoante os elementos se movem ao longo da superfície faz com que fiquemos com uma região 
- Temos uma espessura média da layer $\overline{\delta}$:
$$\overline{\delta}=\frac{2}{3} \frac{L}{\sqrt{Re_{L}}} \quad;\quad Re_{L}=\frac{v_{0}\rho L}{\eta}$$
($L$ - escala de comprimento representativa da montagem, $Re$ - número de Reynolds, $v_{0}$ - velocidade de fluxo, $\eta$ - viscosidade do gás, $\rho$ - densidade do gás)

#### Esquemática
![[cvd passos 2.png]]

#### Cinemática
- Deposita-se uma camada na superfície, a camada estagnante. Conforme a reação ocorre, esta camada é gasta diretamente. Gera-se um gradiente de concentração:
![[cinematica cvd.png]]
- Podemos definir $F_{1}$ - fluxo de difusão de reagentes que entram na câmara e vão para a superfície, passando pela boundary layer, de espessura $\delta$. Temos:
$$F_{1}=D_{g} \frac{dc}{dy}\simeq D_{g}\frac{c_{g}-c_{s}}{\delta}=h_{g}(c_{g}-c_{s}) $$
Temos: $D_{g}$ - coeficiente de difusão do gás, $c_{g},c_{s}$ - concentração do gás e do sólido, $h_{g}$ - rate de transferência de massa

- Temos ainda $F_{2}$ - fluxo de reagente consumido pela reação na superfície:
$$F_{2}=k_{s}c_{s}$$
em que $k_{s}$ - rate de reação na superfície

- Em steady state teremos $F_{1}=F_{2}$, logo:
$$c_{s}=\frac{h_{g}k_{s}}{h_{g}+k_{s}}c_{g}$$
e temos o rate de growth:
 $$R=\frac{F_{2}}{N_{f}}=\frac{c_{s}}{N_{f}}=\frac{h_{g}k_{s}}{h_{g}+k_{s}} \frac{c_{g}}{N_{f}}$$
em que $N_{f}$ é a densidade atómica do film.

![[regime limitado reacao.png]]
- No caso em que $h_{g}\gg k_{s}$ (muito mais material a chegar à superfície do que material gasto em reação), logo a deposição fica completamente controlada pela reação na superfície ($h_{g}$) e temos:
$$R=k_{s} \frac{c_{g}}{N_{f}}=\frac{c_{g}}{N_{f}}k_{0}e^{-\frac{E_{A}}{k_{B}}T}$$
normalmente o regime que temos a baixas temperaturas (lado direito na figura acima, temos $1/T$). Aqui estámos a definir:
$$k_{s}=k_{0}e^{- \frac{E_{A}}{k_{B}T}}$$

- No caso oposto temos $k_{s}\gg h_{g}$ (muita mais reação do que reagentes a chegar à superfície), logo a deposição é controlada pela difusão de gás:
$$R=h_{g} \frac{c_{g}}{N_{f}}= \frac{3}{2} \frac{D_{g}c_{g}}{LN_{f}}\sqrt{Re}$$

A altas temperaturas (lado esquerdo na figura acima, temos $1/T$), a deposição é controlada pela difusão de gás.

- E temos então algo assim:
![[regimes cvd.png]]
- Se queremos um só cristal usamos alta T
    - Este tipo de sistema é controlado pela reação de superficie, $h_{g}$
    - Temos que usar configuração horizontal, em que temos menos wafers mas cada um tem crescimento uniforme
- Quando queremos algo mais preciso e critico, usamos baixa T
    - Podemos ter alto throughput, podendo colocar vários wafers seguidos na *vertical* (perpendicular ao fluxo)

### Hot wall
- Sistema que consiste em ter as paredes da câmara aquecidas. 
- Esta temperatura não pode ser demasiado baixa, os rates de deposição diminuem.

### Cold wall
- O substrato é aquecido, com um aquecedor RF (de indução)
![[cvd cold wall.png]]
- O gás circula como mostrado acima
- O perfil de transporte junto das boundaries do substrato
- As paredes serem cold, diminui a deposição de material nas paredes
- Infelizmente, o controlo de temperatura é pior

#### Tipos
- APCVD (air pressure CVD)
    - crescimento controlado por transporte de massa
    - espessura menos uniforme
    - wafers metidas de lado
- LPCVD (low pressure CVD)
    - pouco crescimento, limitado por reação de superfície
    - espessura uniforme
    - pressão de 0.1-10 Torr
    - melhor camada overall
    - Temperatura >500ºC
- PECVD (plasma enhanced CVD)
    - o plasma divide as moléculas de gás, o que permite fazer o processo com menos temperatura e pressão
    - maior pressão do que em sputtering
    - pior film que em LPCVD
- MOCVD (metal-organic CVD)

**APCVD**
![[apcvd.png]]
- muito do gás na câmara não reage, apenas serve para transporte
- Problemas
    - A alta Temp, temos que fazer configuração horizontal como acima, logo temos menos wafers
    - A baixa Temp, temos menos deposição então ter mais wafers não compensa

**LPCVD**
- No regime limitado pela transferência/transporte temos: $h_{g}=D_{g}/\delta$, mas temos que $D_{g}\propto 1/P$.
    - Consoante $P$ baixa, $D_{g},h_{g}$ aumentam.
    - Se $P$ diminuir 760x, $h_{g}$ aumenta 100x
- Como temos $h_{g}$ maior, podemos usar maior $T$ mantendo $k_{s}<h_{g}$ (regime controlado pela reação)
![[lpcvd.png]]
- Neste método, podemos colocar as wafers na vertical
- Devido à baixa pressão, este método é *muito* sensível à temperatura

**PECVD**
![[pecvd.png]]
- O plasma é criado com aquecimento RF. Este transmite energia para os átomos, que se tornam reativos
- Esta fonte de energia permite o processo a baixa T (deixa de ser preciso energia alta para excitar os átomos)
    - Aqui, temperatura baixa é <300ºC
- Como tal, é um bom método para substratos frageis a altas T

**Comparação**
![[tipos cvd tabela.png]]

**Resumo**
![[tipos cvd vantagens e desvantagens.png]]

#### Doping em CVD
- Feito durante o crescimento de filmes epitaxiais
- O dopante é colocado diretamente no substrato
- Simplesmente inserimos gases que contêm o gás
- A concentração de dopante será
    - $C\propto P_{i}$ ($P_{i}$ - pressão parcial do gás com dopante)
    - $C\propto P_{i}/v$ ($P_{i}$ - pressão parcial do gás com dopante, $v$ - rate de crescimento)

#### Deposição Seletiva
- Consiste em fazer patterning na superfície, ao longo do crescimento 3D
- Primeiro fazemos uma parte do padrão. Depois usando CVD crescemos uma camada no espaço em falta
- A superfície de crescimento atua como um co-reagente
![[cvd seletividade.png]]

#### Problemas de segurança
- os gases podem ser tóxicos, limita o tempo que se pode trabalhar com eles
- os gases podem ser inflamáveis, explosivos
- As tubagens são complexas, já que os tubos têm que ter parede dupla
- é precisa monitorização

# 2 - ALD (Atomic Layer Deposition)
![[ald.png]]
**Ciclo ALD para deposição de alumina**
![[ald exemplo.png]]
1. A $H_{2}O$ no ar é absorvido pelo substrato (sílica) e forma-se Si-O-H. Temos TMA na câmara. 
2. O TMA reage com um H da superfície e produz-se metano (a molécula a fugir na imagem do canto superior direito). Apenas o alumínio fica.
3. Introduzimos de novo $H_{2}O$. Os 2 grupos de C,H junto do Alumínio que restavam formam metano e saem. Depois, cria-se nova camada com O-H em cima do alumínio (canto inferior esquerdo)
4. Um ciclo consiste num pulso de TMA e um de $H_2O$. Roughly, cada ciclo acrecenta $1\dot{A}$ à espessura.

### Sistema
- Criamos então filmes ultra-finos com poucos nanómetros, com muita precisão
- Temos 2 caraterísticas principais:
    - o crescimento atómico ocorre layer-by-layer
    - o crescimento é muito uniforme
- Podemos usar uma grande gama de materiais: óxidos, nítridos, metais
- Bom para fazer coating de estruturas complexas

### Vantagens
- Podemos fazer filmes com estequiometria perfeita e grande uniformidade
- Controlo de espessura preciso
- Baixa temperatura possível
- Método mais soft, para materiais frageis

### Desvantagens
- Deposição lenta, mais lenta que CVD
- Alguma variedade de materiais, mas pouca

![[comparacao deposicoes.png|307]]
![[ald step coverage.png|408]]
