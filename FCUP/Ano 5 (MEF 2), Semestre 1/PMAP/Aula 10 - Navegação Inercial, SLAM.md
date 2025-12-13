# PPT Navegação inercial - FFI (Norwegian Defence Research Establishment)
## Intro
- O PPT começa por fazer uma revisão sobre pontos, vetores, referenciais
- Podemos definir alguns referenciais mais importantes:
![[tipos referenciais.png]]

### Referencial
- Definimos referenciais com origem num certo ponto A
- Eles são definimos através da **posição** da origem e da sua **orientação**
    - Temos *6 graus de liberdade*

### Notação de vetores neste PPT
- Podemos representar um vetor *sem referencial* (no caso de deduções) como $\vec{x}$
- Representamos os versor da base $E$ como $\vec{b}_{E,i},\vec{b}_{E,j},\vec{b}_{E,k}$
- Um vetor escrito na base $E$ fica na forma:
$$\vec{x}^{E}=x_{i}\vec{b}_{E,i}+x_{j}\vec{b}_{E,j}+x_{k}\vec{b}_{E,k}=\begin{bmatrix}x_{i} \\ x_{j} \\ x_{k}\end{bmatrix}$$
(sendo estas as componentes do vetor **neste referencial**)

- Acerca de velocidades lineares:
    - $\vec{p}_{AB}=B-A$ é o vetor *posição* que vai de A para B (dá a posição de B relativo a A)
    - ${}^{C}\vec{v}_{AB}={}^{C}\frac{d}{dt}(\vec{p}_{AB})$ é o vetor *velocidade generalizada* que dá a velocidade de A para B, no referencial C
    - $\vec{v}_{AB}={}^{A}\vec{v}_{AB}$ é o vetor *velocidade standard* que dá a velocidade de B relativamente a A! Isto quer dizer que em A importa ainda a orientação, não só a posição.
    - ${}^{C}\vec{a}_{AB}={}^{C}\frac{d^{2}}{dt^{2}}(\vec{p}_{AB})$ é o vetor *aceleração generalizada* 
    - $\vec{a}_{AB}={}^{A}\vec{a}_{AB}$ é o vetor *aceleração standard*, de B relativamente a A

- Acerca de velocidades angulares:
    - $\vec{\theta}_{AB}=\vec{k}_{AV}\cdot \beta_{AB}$ é o *produto eixo-ângulo* - nesta representação temos um eixo de rotação $\vec{k}$ e um ângulo em que queremos rodar $\beta$, passando de A para B
    - $R_{AB}$ é a *matriz de rotação* que permite representar a transformação de A para B: $x^{A}=R_{AB}x^{B}$
    - $\vec{\omega}_{AB}$ é a *velocidade angular* que descreve a velocidade de rotação de B relativamente a A

## Navegação inercial
- Consiste em estimar a posição, orientação e velocidade de um veículo
- **Navegação Inercial** consiste em fazer a navegação usando *sensores inerciais*
- Vamos então ver alguns destes sensores. Os mais comuns são acelerómetros e gyros

### Acelerómetros
![[acelerometro.png]]
- Esta versão simplesmente consiste em ter uma massa numa mola. Quando o veículo acelera, a aceleração é aplicada na massa e ela sai da sua posição de equilíbrio na mola. Ao medir o desvio da posição de equilíbrio, podemos determinar a aceleração do veículo
- Pode ser implementado um sistema de controlo que force a massa a estar perto da sua posição de equilíbrio, para reduzir histerese e reforçar a linearidade do sistema

 **Gravitação**
- Podemos (e devemos) ter em conta a aceleração da gravidade, sempre aplicada na massa
- Assim, temos uma força específica total:
$$\vec{f}_{IB}=\vec{a}_{IB}-\vec{g}_{B}=\vec{a}_{IB}- \frac{\vec{F}_{B,\text{gravidade}}}{m}$$
- Usando 3+ acelerómetros, podemos excluir esta aceleração, obtendo a força medida **em 3D**
- Acelerómetros comerciais bons 

### Gyros
AKA giroscópios
- Usamos estes para medir a velocidade angular relativa ao espaço inercial: $\vec{\omega}_{IB}$

#### Versão mecânica
![[gyro mecanico.png]]
- Este tipo de sistema consiste em *manter o momento angular*. Temos uma roda a girar, que irá resistir a qualquer mudança no momento angular no seu referencial inercial
- Uma maneira de usar isto é isolar o gyro das rotações do resto do veículo com gimbals e depois usar a posição medida no gimbal para entender as orientações do robot
    - Notemos que neste tipo de sistema o gyro vai ativamente mover-se para ficar sempre na mesma orientação

#### Versão ótica
![[gyro otico.png]]
- Usamos o efeito de Sagnac:
    - A luz tem uma componente corpuscular, logo está sujeita a efeitos inerciais. 
    - Podemos meter 2 feixes de luz a mover em direções opostas num loop de fibra ou num sistema de espelhos.
    - Se o loop rodar no sentido horário, o feixe de luz a mover-se no sentido horário vai ter que percorrer maior distância enquanto que o feixe anti-horário vai percorrer menor distância.
    - Ora, se combinarmos os 2 feixes num beam splitter e virmos o resultado num detetor, iremos ver um **padrão de difração** que depende da *velocidade angular* $\omega$ com que rodamos o loop

#### Versão coriolis
![[gyro coriolis.png]]
- Nesta versão temos uma massa a vibrar na direção radial de um sistema em rotação
- A força de coriolis ocorre **devido à rotação** e atua *perpendicular à direção original de vibração*.
- Ou seja, devido à rotação, vai surgir uma nova vibração!
- Ora, a amplitude dessa vibração tem de estar relacionada à velocidade de rotação
- Este principio é usado por MEMs, gyros "tuning fork" e gyros "wineglass"
- Estes gyros são **mais baratos e menos preciso**

### IMU
AKA *Inertial measurement unit*
- Consiste num sistema com 3 acelerómetros e 3 gyros - medimos aceleração $x,y,z$ e orientação angular nas 3 direções (roll, pitch, yaw)
- Temos 2 tipos:
    - *strapdown IMU* - os sensores inerciais são todos presos ao veículo e medem diretamente as suas acelerações e orientações
    - *gimballed IMU* - os gyros e acelerómetros estão em gimbals, isolados dos movimentos angulares do veículo - isto permite pedir acelerações num referencial fixo, invés do body frame

## Tipos de navegação
- Um IMU (que permite saber $f_{IB}^{B},\omega_{IB}^{B}$) é *suficiente* papra navegar num espaço inercial, sabendo a *velocidade, posição e orientação iniciais*
- O que se faria:
    - Integrar a aceleração medida dá estimativas da velocidade
    - Integrar uma 2ª vez permite saber a posição
    - A orientação (angular) permite integrar na direção correta e assim prever a posição

### Navegação terrestre
- Quando queremos navegar relativamente à terra $E$. Ora, a Terra *não é um sistema inercial* e temos gravidade presente. Isto complica a navegação - só integrar é má ideia
- Temos que compensar para a rotação angular da Terra nas medições de velocidades angulares: $$\omega_{EB}^{B}=\omega_{IB}^{B}-\omega_{IE}^{B}$$
- Já nas medições de aceleração temos que fazer correções para compensar:
    - Gravitação
    - Força centrifuga devido à rotação da Terra
    - Força de Coriolis devido a estarmos a mover na Terra (que é um referencial em rotação)
![[esquema sistema localizacao.png]]
- Ora isto que aqui temos tem nome:

#### INS
AKA **Inertial Navigation System**
- Isto é o nome dado à combinação IMU + software que faz as correções.
- Este tipo de sistemas dá-nos logo coisas tipo: velocidade, matriz de rotação, latitude/longitude, profundidade/altitude
![[ins.png]]

#### AINS 
AKA **Aided Inertial Navigation System**
- Para limitar o erro dos INS dá-mos-lhe uma ajuda usando outros sensores que fazem **medições diretas** para corrigir aquilo obtido do IMU
![[sensores e medicoes.png]]

### Modelar erro
- Outra coisa que pode ser útil é *modelar o erro*. Isto pode permitir melhorar as estimativas bastante. Alguns modelos de erro:
    - Ruído branco
    - Ruído colorido
    - Erro de fator de escala
    - Erro de alinhamento

## Kalman (again)
- Como já vimos, é um algoritmo recursivo para estimar o estado de um sistema
- Este modelo usa:
    - **Medições** dos sensores
    - **Modelo matemático** que descreve a evolução do sistema a ser medido e como os estados se relacionam com as medições
    - **Incerteza/precisão** das medições e estimativas de estado

- Algoritmo:
![[algoritmo kalman explicado texto.png]]

- Equações:
![[eqs kalman.png]]

### Kalman em navegação
- Aqui ele permite encontrar a posição, orientação, velocidade do veículo com alta precisão (estas propriedades constituem o estado)
- Podemos usar várias coisas como base para implementar o filtro:
    - Medições dos sensores
    - Conhecimento do sistema e do funcionamento dos sensores (modelagem matemática)
    - Variáveis de controlo

- Para podes ter erros e fazer correções Kalman, precisamos de uma série de sensores apra obter valores a comparar com o IMU:
![[sensores e medicoes 2.png]]
e temos
![[sistema localizacao com kalman.png]]
(attitude é orientação)

## Implementações práticas
### AINS
- Um veículo com um INS ou AINS pode ser implementado assim:
![[sistema navegacao com kalman 2.png]]

### NavLab
- Ferramenta usada para navegação:
![[navlab.png]]
- Temos o lado de simular, o que permite prever comportamentos de forma menos dispendiosa. Permite establecer uma **base teórica forte**
- Consegue simular:
    - qualquer percurso na Terra e próximo dela
    - sensores comuns, simulando os seus erros caraterísticos
    - evolução dos sensores e seus erros ao longo do tempo
- Usado em sistemas muito mais complexos: UAVs, ROVs, barcos autónomos
- Usado em investigação mas também em industria e até em contextos militares

## Alinhamento inicial
- É importante que a estimativa inicial de orientação (e posição) sejam decentes, para que depois a navegação seja melhor e mais precisa.
    - NOTA: um AINS bom consegue perceber a sua orientação e posição de forma ótima, MAS a estimativa inicial é tratada como um problema diferente. Isto porque se ela for horrível teremos problemas devido à linearidade do filtro de Kalman.
- Ou seja, queremos saber a orientação do veículo $B$ no referencial da Terra $E$ usando um IMU e outras medições adicionais
- *Solução*: encontrar vetores que conhecemos bem no referencial da Terra e decompô-los no referencial do veículo. Cada vetor terá 2 df então com 2 vetores conseguimos saber a orientação toda.
- Dois vetores úteis:
    - **aceleração da gravidade**
    - **velocidade angular da Terra**

## Direção vertical
- Como acelerometros medem acelerações E a gravidade, é fácil perceber quais ângulos são o pitch e roll -- rotações em torno de eixos perpendiculares ao eixo vertical
![[Attachments/roll pitch yaw.png]]

- Ora, é preciso saber os componentes da *aceleração* mesmo: $f_{IB}^{B}=a_{IB}^{B}-g_{B}^{B}$
- Para isto é preciso informação adicional. Possibilidades:
    - Medições de posição ou velocidade externas ao veículo
    - Modelar melhor o veículo

### Gyrocompassing
- Esta técnica permite saber a orientação do eixo vertical ao medir a direção da rotação da Terra no referencial inercial: $\omega_{IE}$

![[referenciais.png]]
- **Caso estático**
    - Temos $\omega_{EB}=0$ (o veículo não roda)
    - Um gyro fixo na Terra irá medir a orientação 3D do eixo de rotação da Terra: $\omega_{IB}^{B} =\omega_{IE}^{B}$
    - O angulo de yaw será dado pela medição do eixo vertical do gyro
        - Ao aproximar dos polos teremos medições menos precisas de yaw - a componente horizontal da rotação da terra diminui (na figura acima a seta vermelha fica mais vertical e a projeção no plano XY será menor)

![[detetar rotacao terra 1.png]]
- **Caso dinâmico**
    - Temos rotação do veículo: $\omega_{IB}^{B}=\omega_{IE}^{B}+\omega_{EB}^{B}$ (rotação da terra no referencial inercial + rotação do veículo no referencial terrestre)
    - Neste caso é difícil medir o eixo de rotação da terra porque $\omega_{IB}^{B}\gg \omega_{EB}^{B}$
    - Assim, fazemos gyrocompassing ao saber o *vetor gravidade ao longo do tempo*. Se ficassemos 24h parados, este vetor irá descrever um círculo consoante a Terra "gira à nossa volta"
    - Se nos movermos, podemos compensar sabendo a velocidade com que nos movemos.

## Demos
- O PPT tem algumas demos de AINS, NavLab, etc

## 7 Formas de achar heading
![[encontrar heading.png]]

# PPT - Intro a Mapeamento - Uni Freiburg
## O que é SLAM?
- Método que permite calcular as poses (posição + orientação) de um robot *ao mesmo tempo* que formamos um mapa do ambiente à sua volta
- **Localização** - Sabendo a posição dos marcos que estamos a ver, estimar a posição do robot
- **Mapeamento** - Sabendo a nossa posição, associar aquilo que vemos a marcos (ou identificar marcos novos)

### Ovo ou Galinha
- Precisamos de saber o mapa do ambiente para poder estimar a posição do robot
- Precisamos de saber a posição do robot para definir o mapa do ambiente

### Aplicação
- Como permite ter robots verdadeiramente autónomos, é muito usado e importante
- Pode ser usado em contexto indoor, outdoor e até debaixo de água

## Definir SLAM
**Sabemos:**
- Os **controlos** e comportamentos do robot (viramos à esquerda, andamos X segundos em frente, etc etc)
- **Medições** feitas por sensores no robot

**Queremos saber:**
- Um mapa do ambiente
- O percurso do robot (sequência de posições que ele teve)

## Comportamento probabilístico
- Como tudo isto é muito incerto ("achamos que está aqui") usamos uma abordagem **probabilística**. 
- Ou seja, invés de dizer "o robot está em X,Y" dizemos "a posição do robot segue esta distribuição"
    - Sendo que nessa distribuição teremos uma região de alta probabilidade e que deverá incluir a posição real do robot
- Em termos de equações:
$$\boxed{\Huge p(x_{0:T}~,~m~|~z_{1:T}~,~u_{1:T})}$$
em que:
    - $x_{0:T}$ são as posições do robot nos instantes $t=0,1,\dots,T$
    - $m$ é o mapa que obtemos (pode ser uma lista de marcos com coordenadas $m_{i}$)
    - $z_{1:T}$ são medições feitas nos instantes $t=1,\dots,T$ (pode ser um vetor incluindo medições de diversas fontes)
    - $u_{1:T}$ são as ações que o robot fez e que nos permitem perceber onde ele está (se $u_{i}$ consiste em andar 10s para a frente, sabendo $x_{i+1}$ basta recuar por 10s para chegar à posição $u_{i}$)
E notemos que a fórmula se lê: "Distribuição da nossa pose e mapa estimados, sabendo as medições e controlos feitos"

- Ou seja, temos uma sandwich de conhecimento e falta de conhecimento:
![[slam logica.png]]
- Em que:
    - os controlos que fazemos (conhecemos) controlam a posição do robot (não sabemos)
    - a posição do robot (não sabemos) afeta diretamente as medições que fazemos (conhecemos)
    - mas temos ainda que estas medições (conhecemos) são decididas pelo ambiente (cujo mapa não sabemos)
- Podemos ainda relações extra se considerarmos que os controlos são decididos com base nas medições

## Full e Online SLAM
- **Full SLAM** estima TODO o percurso do robot desde o início:
$$p(x_{0:T},m|z_{1:T},u_{1:T})$$
- **Online SLAM** estima a pose mais recente do robot, mas usando na mesma *toda a informação disponível*:
$$p(x_{t},m|z_{1:t},u_{1:t})$$
- Notemos que no FULL usamos $T$, indicando que o percurso é calculado todo *offline*, usando os instantes $t=0,1,\dots,T$
- No ONLINE usamos $t$ pelo que fazemos tudo online, usando os instantes $0,1,\dots,t$

## Dificuldade
- Ok, este problema *soa* difícil. Mas vamos ver algumas razões concretas porque o é:
    - Tanto o percurso COMO o mapa são desconhecidos
    - As estimativas do mapa e da pose são *correlacionadas*
    - Sem mais conhecimento é difícil relacionar marcos num possível mapa com observações
    - Podemos ter casos com alguma simetria em que associamos coisas que não devíamos. Isto resulta em erros enormes!![[problema slam - simetrias.png|475]]

## Algumas variações ou fatores
- SLAM volumétrico (registar todos os pontos medidos até ter um mapa consistente) ou com features (marcar pontos interessantes só. EX: paredes)
- Podemos fazer SLAM em ambientes estáticos (nada muda ao longo do tempo) ou ambientes dinâmicos
- A incerteza pode ser alta ou baixa. Visto de outra forma, podemos ter muita ou pouca confiança nas nossas estimativas (EX: se aquele quanto devia ser uma zona do ambiente de acordo com a estimativa de orientação, posso confiar nisso?)
- Podemos fazer SLAM com 1 ou vários robots a trabalhar juntos

## Implementar
- Este tema é ainda muito discutido em diversas conferências de robótica
- A base é quase sempre métodos probabilísticos
- Temos 3 paradigmas principais:
    - **Filtro de Kalman** (só vamos ver este)
    - *Filtro de partículas*
    - *Com grafos*

## Modelo de movimento e observação
![[slam modelos incluidos.png]]
- Para poder implementar qualquer coisa, temos que começar com uma base sólida para modelar movimentos feitos pelo robot e medições obtidas

### Movimento
- Este modelo consiste em prever a posição atual, sabendo a estimativa da posição anterior e o controlo aplicado: $p(x_{t}|x_{t-1},u_{t})$
- Um modelo comum e não probabilístico é o de odometria direta. 
    - O robot vai da pose $(\overline{x},\overline{y},\overline{\theta})$ para a pose que queremos determinar $(\overline{x}',\overline{y}',\overline{\theta}')$. 
    - Sabemos que aplicamos controlos que deverão causar: $u=(\delta_{\text{rot 1}},\delta_\text{trans}, \delta_{\text{rot 2}})$
![[posicoes referencial comum.png]]
e podemso isolar os componentes da pose nova.

### Observação
- Consiste em modelar a medição feita, relativamente à estimativa da pose atual: $p(z_{t}|x_{t})$