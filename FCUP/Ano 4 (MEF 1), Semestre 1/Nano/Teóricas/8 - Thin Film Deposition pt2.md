# 1 - Evaporação
- Material tem origem num material aquecido, transportado e depositado/condensado num substrato
- Para este transporte funcione de forma eficiente, este processo é feito num vácuo alto, o que reduz as colisões com átomos do ar
- A fonte é aquecida com resistências ou EBeam
- O rate de deposição é decidido por
    - fluxo de átomos de deposição emitidos
    - geometria da fonte e wafer
- O rate de deposição pode ser bastante elevado ($>1 \mu \text{m/min}$)
- O film depositado tem alta aderência, mas é pouco conformal
- Não é usado na indústria
![[evaporacao.png]]

## Distribuição
- A distribuição angular das partículas depositadas são dadas pela *Lei de Cosseno de Knudsen* : $P(\theta)=P_{0}\cos\theta$, em que $\theta$ é o âgulo medido em relação à normal da superfície da fonte de átomos
![[evaporacao angulos.png]]
- Na vida real, os padrões de emissão costumam ser mais direcionais que isto.

**Caso circular**
- Consideremos a figura abaixo, em que temos uma câmara de vácuo circular/esférica. 
![[evaporacao camara circular.png]]
neste caso, as partículas irão incidir no substrato com um ângulo $\theta$. Assim, a quantidade de material depositado é reduzida por um fator de $\cos\theta$ (em comparação ao caso de incendência perpendicular)
![[evaporacao em substrato inclinado.png]]
- Neste mesmo caso, temos:
$$m=C \frac{\cos\theta\cos\theta}{\pi R^{2}}$$
em que: $m$ é a massa depositada, $C$ uma constante. O primeiro cosseno vem da distribuição angular que vimos acima, o segundo cosseno vem do fator com que a deposição diminui com o substrato a um ângulo $\theta$. O denominador tem a ver com ângulo sólido e cenas.
- Podemos ainda escrever
$$m\propto \frac{1}{4\pi r^{2}}$$
logo a massa depositada **não** depende do ângulo! Por exemplo, se tivessemos uma câmara circular e fizessemos evaporação, ficaria uma camada da mesma espessura em toda a superfície da câmara.

**Espessura**
- O rate de deposição é de
$$R=\sqrt{\frac{M}{2\pi \rho^{2}}} \frac{P}{\sqrt{k_{B}T}}\frac{A}{4\pi r^{2}}$$
($P$ é a pressão de vapor)
o 1º termo consiste em propriedades dos material, o 2º termo consiste na temperatura e pressão, o 3º termo consiste na geometria da câmara.

**Exemplos**
![[carateristicas evaporacao alguns elementos.png]]

## Método de aquecimento
- **Evaporador térmico** - o calor é gerado com resistências, a única que funciona com material orgânico
- **Evaporador com EBeam** - mais popular, mais caro
- **Evaporador com aquecimento indutivo** - pouco popular

### Evaporação Térmica
- Simples, robusto, muito usado
- Pode ir até ~1800ºC
- Temos coils, recipientes e outras coisas para aquecer o material fonte. Estas coisas de aquecer podem ser feitas de W. Ta ou Mo. Correntes de 20-300A
- Normalmente usasse materiais cuja pressão de vapor é razoável a 1600ºC
- O substrato é exposto a radiação visível-IR
- Contaminação vinda do crucible e da cena usada para aquecer a fonte
![[suporte evaporacao termica.png|475]]
![[tipos suporte evap termica.png|500]]

### Evaporação EBeam
![[evaporacao ebeam.png]]
- Mais complexo, mas muito versátil
- Pode atingir >3000ºC
- A evaporação ocorre num local muito concentrado 
- Ocorre menos contaminação vinda do crucible
- A wafer é aquecida menos

- Mas temos *desvantagens*
    - Geram-se raios X
    - Os rates de deposição podem ser difíceis de controlar
    - A pressão de vapor varia de forma previsível com a temperatura, mas é mais imprevisível face a EBeam

#### Alguns recipientes para aquecer a fonte
![[suportes evaporacao.png]]

### Problemas de evaporação
- Problema **Estequiométrico**
    - Compostos desfazem-se a altas temperaturas
    - Os elementos do composto, agora separados, têm rates de deposição diferentes porque têm pressões de vapor diferentes
    - Isto leva a termos um film depositado com estequiometria diferente da fonte

![[step coverage evaporacao.png]]
- **Step Coverage**
    - Preenche muito pouco ou nada as beiras verticais de degraus
    - O *coeficiente de sticking* é $S_{c}=F_{\text{reagiu}}/F_{\text{incidente}}$
        - Se o coeficiente for alto, o material fica onde acertou ao depositar. Se o coeficiente fr baixo, o material pode espalhar-se
    - No entanto, em certos contextos de R&D, esta propriedade pode ser útil. Isto porque má step coverage implica que temos uma camda boa para liftoff

### Glancing angle deposition
- Se arranjarmos uma combinação material/substrato em que temos $S_{c}$ muito elevado, podemos aproveitar esta propriedade de deposição muito direcionada.
- Com uma configuração como a seguinte, é possível manipular as estruturas criadas:
![[evaporacao substrato a rodar.png]]
e podemos fazer estruturas específicas
![[padroes feitos com evap.png]]

### Monitorizar espessura
![[monitorizacao espessura evap.png|354]]
- Usamos uma *QCM* (quartz crystal micro-balance)
- Isto consiste num material piezoelétrico, que gera uma corrente AC na sua frequência de ressonância
- Consoante é sujeito a mais massa, a frequência muda
- O cristal não dura muito
- Temos:
$$\Delta T_{r}\propto m_{f}\propto \rho_{f}t_{f}$$
estas coisas são : período de ressonância, massa do filme, densidade do filme, espessura do filme.

### Vantagens e Desvantagens de Evaporação em geral
**Vantagens**
- Rate de deposição pode ser bem alto
- Podemos evaporar quase qualquer elemento
- Ocorre poucos danos na superfície
- Pouca contaminação
- Pouco aquecimento do substrato

**Desvantagens**
- Difícil de controlar
- Alguns materiais têm rate de deposição muito lento
- Mau step coverage
- Danos raios X

# 2 - Epitaxy com Molecular Beam
![[epitaxy.png]]
- Sublimamos elementos de alta pureza e eles condensam na wafer. Feito num vácuo muito alto: $10^{-11}\text{ Torr}$
- Usamos um beam de moleculas, que garante que as moléculas depositadas não colidem com as paredes da câmara nem outros átomos de gás
- A deposição ocorre a um rate de 0.1nm/s

![[epitaxy 2.png]]
- A lógica:
    - Usa-se efusão (moleculas saem de uma câmara inicial por orifícios menores que o caminho livre médio). Um dos métodos usados é Knudson cell
    - Elementos de alta pureza (como Ga, As) são aquecidos em câmaras separadas e começam a sublimar lentamente. Saem para a câmara principal por efusão
    - Os gases sublimam na wafer e podem reagir
- Este método permite fazer estruturas muito precisas

# 3 - Sputtering
- Uma técnica mais flexível, usada pela industria de ICs para depositar alloys e dielétricos
- Deposição rápida, com bom controlo de espessura
- A lógica consiste em usar um plasma para expelir material de um target. Acontece uma série de colisões em cadeia assim:
![[sputter.png]]

### Sistema
![[sputtering.png]]
- Normalmente usamos ~1000V e ~10A
- Como temos aqui, os átomos saem do target e sobem para o substrato, ficando depositados. Se trocarmos os dois de sítio, passamos a fazer etch do substrado.
- Feito em câmara com gás em pressões de 1-10 mTorr
- O rate de deposição chega a ser de dezenas de nm/min
- Um sistema DC permite depositar metais. Um sistema pulsed permite depositar metais e isoladores

### Como
1. Coloca-se na câmara um gás inerte a baixa pressão
2. Aplica-se DDP entre ânodo e cátodo
3. Iões (positivos) do gás são acelerados rumo ao cátodo (que tem carga negativa)
4. Ocorre sputtering e material do target deposita no substrado

### Deposição
$$R\propto \frac{M_{1}M_{2}}{(M_{1}+M_{2})^{2}} \frac{E_{m}}{U_{m}} \frac{1}{\cos\theta}$$
- Em que:
    - $M_{1}, M_{2}$ - massa do target e átomos do plasma
    - $E_{m}$ - E cinética do ião que colide com target
    - $U_{m}$ - Energia de bonding do átomo do material do target
    - $\theta$ - ângulo entre ângulo de incidência do ião e a normal do target

- Podemos definir o *yield de sputtering*: $$S=\frac{\# \text{médio de átomos emitidos}}{\# \text{iões incidentes}}$$

#### VS Energia
- Este aumenta com a energia:
![[sputtering yield.png]]
- Podemos acima ver que existe uma energia limite. Abaixo dela temos rendimento completamente nulo. Esta será:
$$E_\text{threshold} = \gamma \phi= \frac{(M_{1}+M_{2})^{2}}{4M_{1}M_{2}}\phi$$
em que $\phi$ é o calor de sublimação. Notemos que esta não é uma constante:
![[sublimacao de materiais.png|187]]

#### VS ângulo
![[deposicao vs angulo.png]]
- Se o ângulo $\theta$ não for muito alto (incidência quase normal), temos:
$$S\propto \frac{1}{\cos\theta}$$
- Isto faz sentido: quando menos perpendicular a incidência (maior $\theta$), mais energia é desperdiçada nos átomos do target perto da superfície de impacto
- A partir de um certo ângulo o yield baixa muito porque desperdiçamos tanta energia que os iões incidentes são refletidos

#### VS massa do ião
![[deposicao sputtering atomos.png]]
- Aumenta com a massa do ião (ou seja, ao percorrer átomos da tabela periódica)
- Temos rendimento máximo para átomo com camadas de valência completas AKA *gases nobres*

#### VS pressão da câmara
![[sputtering pressao.png]]
(ignora as setas)

- A pressões muitooo baixas basicamente nem temos plasma
- A baixas pressões temos poucos iões na câmara/plasma logo menos impactos e menos deposição.
- A alta pressão temos tantos iões que um átomo sputtered passa por dezenas de colisões antes de depositar. Nisto, pode desviar-se e ir parar às paredes da câmara

#### Step coverage
- Os átomos são emitidos/sputtered do cátodo com altas energias (10-50 eV) e em ângulos diversos. Assim:
![[step coverage sputtering.png]]
- O filme depositado será mais denso (melhor)

**Melhorar**
- Uma forma de melhor isto será rodar/inclinar o substrado ao longo da deposição, já que ocorre algo assim:
![[sputtering direcional.png]]
- Usar uma fonte com maior área
- Aquecer a fonte, o que permite maior mobilidade dos átomos depositados
- Aplicar tensão negativa (bias) no substrado para reforçar deposição 

## Sputtering de Alloys
![[sputtering metais.png]]
- A composição dos alloys é mantida consoante estes vão de target para film
    - Nisto, começamos por ter uma combinação $A_{x}B_{y}$ no target
    - Após algum tempo, em que $A$ é mais sputtered, ficamos com um sistema em equilíbrio: $A_{x'}B_{y'}$

### DC Sputtering
![[sputtering eletrico.png]]
- O que vimos atrás
- O target fica no cátodo e a wafer no ânodo 
    - Iões positivos do gás seguem o campo elétrico, que vai de "+" para "-", ou seja, vão para o cátodo
    - Num sistema de etch metemos a wafer no cátodo
- Aplicamos uma DDP alta o suficiente para ionizar o gás (como usamos gases nobres, eles perdem 1 eletrão e ficamos com átomos com carga 1+):
![[sputtering eletrico 2.png]]
- Na câmara temos iões ionizados. Um ião colide e são libertados eletrões do target. 
    - Estes eventualmente perdem energia e são recolhidos por um ião Ar+
    - Ouuu, os eletrões juntam-se a um dos eletrodos

### Magnetron sputtering
- Usamos campo magnético perto do target para prender eletrões nessa zona. 
- Os eletrões, devido ao campo B, fazem um circulo e regressam logo ao target:
![[magnetron sputtering.png]]

**Vantagens**
- A corrente de deposição aumenta 100x
- O rate de deposição aumenta 100x
- Temos que usar menor pressão de gás (~0.5mTorr), melhora qualidade do filme
![[magnetron vs dc depsoicao.png]]

**Problemas**
- Devido ao campo, maioritariamente só removemos material da região "racetrack"
- Os materiais podem atingir a temperatura de Curie
- Não podemos fazer sputtering de materiais magnéticos
![[magnetron sputtering marca alvo.png]]

### RF sputtering
- Em DC sputtering ocorre concentração de carga positiva no cátodo. Isto efetivamente reduz o campo magnético que temos na câmara e portanto reduz a deposição
![[sputtering rf.png]]
- Usamos uma fonte de tensão oscilatória. Se a frequência for >50kHz, os iões não seguem o campo e neutralizamos a tensão em cada elétrodo
- Ficamos com uma região intermédia com uma DDP. Isto é suficiente para acelerar os iões. Depois de colidir eles não ficam no target

### Reactive sputtering
- Usamos gases reativos (O2, N2)
- Serve para garantir que parte do gás *fica* no filme depositado
- Por exemplo, para depositar um filme TiN, usamos um target de Ti e um gas de N2
    - Ou seja, o material do target combina com o gás em si
- Aqui torna-se dificil controlar a estequiometria
    - Na prática, frequentemente acabamos a formar mistura de materiais (que usam os mesmos átomos base, com estequiometrias diferentes)

## Vantagens de Sputtering
- Permite depositar muitos tipos de materiais
- Permite replicar o target no filme
- Ao inverter a polaridade dos eletrodos "limpamos" ?
- Melhor step coverage e qualidade do filme do que evaporação
- Temos mais controlo e replicabilidade da deposição
- Podemos usar targets grandes
- O material do target chegará para várias deposições
- Sem dados Raios X

## Desvantagens de Sputtering
- Danificação do substrado por bombardeamento e UV
- Pressão muito maior que evaporação, maior chance de contaminação
- Para alguns materiais, deposição muito lenta
- Alguns materiais não funcionam (organicos)
- Ocorre muito aquecimento nas colisões
- Muito alta tensão elétrica (DC,RF)
- Luz UV emitida por Argon é perigosa para os olhos
- Na prática, a câmara atua como um condensador gigante. Perigo

## Sputtering VS Evaporação
![[tabela sputtering.png]]

# 4 - Pulsed Laser Deposition
![[pulsed laser dep.png]]
- Pulsos de laser concentrados evaporam o target no ponto de incidência e convertem-no em plasma
- Este plasma reverte para gás e deposita no substrato
- Estes pulsos são de fs ou ns. Usamos pulsos porque o plasma que se gera é refletido. Se o laser fosse constante iriamos atingir coisas que não queremos:
![[pulsed laser dep 2.png]]

- O tamanho dos buracos deixados no target com diametro na gama 10-75um, com ~15um de profundidade

#### Aplicações
![[apliacaoes dep.png]]