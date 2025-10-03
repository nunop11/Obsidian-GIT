# Tipos de Sensores
## Caraterização de sensores
- Temos 4 principais caraterísticas que permitem caraterizar sensores:
    - **Proprioceptivo** - sensor que mede parametros ou estados do robot
    - **Exteroceptivo** - sensores que obtêm informação sobre o ambiente
    - **Ativo** - sensores que medem reações do ambiente após emitir algo
    - **Passivo** - sensores que medem coisas do ambiente diretamente
- Vejamos como isto pode ser usado para caraterizar vários sensores:
![[Pasted image 20250924175149.png]]

### Caraterizar performance
- Temos 9 caraterísticas que caraterizam a performance/comportamento de um sensor:
    - **Range/alcance** - range entre as medições máxima e mínima
    - **Range dinâmico** - rácio entre medição máxima e mínima, em dB. No caso de algo não-potência: $20\log_{10}\left(\frac{R_\textsf{max}}{R_\textsf{min}}\right)$
    - **Resolução** - menor diferença entre valores de medição seguidos (menor divisão da escala)
    - **Sensibilidade** - rácio de variação da medição para um certo input (relacionado à quantização das medições devido a instrumentos serem digitais)
    - **Linearidade** - um sensor é linear se verificarmos que: $f(ax+by)=af(x)+bf(y)$ em que $ax+by$ é o que estamos a medir e $f(\cdot)$ a medição
    - **Frequência/rate** - velocidade com que o sensor faz medições
    - **Erro** - Diferenºa entre a medição $m$ e o valor real $g$: $e=m-g$
        - *Erro sistemático* - devido a desvios na calibração, são determinísticos e podemos compensá-los
        - *Erro aleatório* - Causados por coisas imprevisíveis, apenas probabilísticos
    - **Exatidão** - o quão próximas as medições estão do valor real: $$\text{Exatidão} = 1- \frac{\text{abs}(m-g)}{g}$$
    - **Precisão** - mede a reproducibilidade da medição. 
        - Consideremos que o ruído aleatório segue uma distribuição $\text{N}(\mu, \delta)$. A precisão é dada por $$\text{Precisão} = \frac{\text{Range}}{\delta}$$

## Tipos de sensores
### Beacons (GPS)
- Método que utiliza o tempo de chegada dos sinais de 3+ beacons para determinar a posição do robot
- O caso mais comum é, claro, GPS (notando-se que esta é especificamente a versão americana).
    - Os satélites sincronizam-se e enviam sinais para o recetor (no robot) *ao mesmo tempo*
    - Os recetores GPS são, portanto, passivos e exteroceptivos
    - Na prática, existem 4 satélites envolvidos neste processo: o quarto faz verificação temporal (que é mais preciso que os sinais de quartzo nos dispositivos)

### Sensores de motores/rodas
- Medem o estado interno e dinâmica de um robot móvel (velocidade, sentido). 
- Estamos principalmente a falar de **encoders**! Falaremos apenas  dos óticos. 
    - *Encoders absolutos* - 
    - *Encoders relativos* -
- Ambos os casos aproveitam buracos num disco para determinar a velocidade de rotação e sentido. Os buracos vão fazendo com que a quantidade de luz que chega ao encoder varie, o que permite detetar o movimento: medimos um sinal rising edge (onda quadrada).
- Nos casos com padrões mais complexos, temos variação de intensidade de luz muito mais controlada e específica. Isto permite-nos determinar a **posição/ângulo** do motor!
    - Num caso só com riscas apenas medimos picos equivalentes a 0 ou 1
    - Num caso complexo podemos medir de 0 a 1, com resoluções elevadas. Isto significa então que conseguimos saber em que posição do circulo estamos através da intensidade medida!!!
![[Pasted image 20250924181558.png]]
(Podemos ver o caso de um encoder simples e um complexo)
- Uma medida de performance de encoders é CPR (ciclos por revolução) que indica quantos picos de luz vão ser medidos em 1 volta. O normal é 2k-10k

### Sensores de Heading/Orientação
#### Bússola
- Sensores que medem a direção de um campo magnético. Exteroceptivos então, já que o campo que medem deverá ser externo ao robot
- É suposto eles medirem o campo magnético terrestre. Mas pode acontecer eles medirem coisas absurdas (como o Norte no Este ou o Norte instável). 
    - Isto acontece porque estes sensores são facilmente influenciados: qualquer fonte magnética pode perturbá-los
    - Até o metal dentro da estrutura de uma parede pode ser suficiente!
    - Isto acontece porque o campo magnético terrestre não é muiiiito "forte"
- Devido a estes problemas, sensores deste tipo são evitados em sistemas indoor

#### Giroscópio
- Outra desvantagem da bussola é que apenas nos dá orientação XY.
- Um giroscópio permite corrigir este e outros problemas de bussolas.

#### Acelerómetro
- Mede aceleração linear em X,Y,Z

#### IMU (Inertial Measurement Unit)
- Junta um giroscópio e um acelerómetro. Assim obtemos os **6 graus de liberdade**: 3 de posição e 3 de aceleração

### Sensores de Range/Distância
#### Sensor ultrassónico
![[Pasted image 20250924184110.png]]
- Usa o princípio TOF (time of flight), em que o tempo de voo $t$ e a velocidade de propagação $c$ de um sinal, dão-nos a distância do objeto que refletiu o sinal:
$$d= \frac{c\cdot t}{2}$$
(Notemos que $t$ é o tempo que passa desde que o sinal é emitido até ele ser recebido, depois de refletido no obstáculo)

- A velocidade de propagação de som num gás ideal é dada por:
![[Pasted image 20250924184209.png]]
- Em líquidos, a velocidade do som é maior:
![[Pasted image 20250924184352.png]]

- Normalmente usam-se sons na gama 40-180 kHz. É comum fazer a "coluna" com um transdutor piezoelétrico (transforma uma corrente AC em oscilação mecânica)
- Temos que ter em conta o **blanking time**: o tempo que a fonte de som fica a vibrar após emitir um sinal. Nesse tempo não podemo emitir novo sinal. Este costuma ser de alguns milisegundos
- Frequências mais baixas permitem obter ranges de medição maiores. MAS fazem com que as oscilações sejam maiores em amplitude, logo temos mais tempo de blanking.
- NÃO devemos ter vários sensores ultrassons juntos:
    - Se estiverem juntos devemos tentar que tenham frequências distintas
    - Mesmo nesse caso, eles devem fazer medições de forma não-simultânea

#### Echo / Sonars
- Sensores que produzem ondas sonoras de frequências específicas e detetam os ecos destas ondas, após refletidas em objetos.
- O que distingue isto de sensores ultrassónicos como falamos antes é que estes são os sistemas usados em contextos subaquáticos, para medir a profundidade da água. Nestes meios, recordemos, a velocidade é **5 vezes** maior que a velcoidade do som no ar!
    - Os trandutores que geram os sinais sonoros para sensorização chamam-se **projetores**.
- O sinal sonoro é emitido e, ao atingir o solo do mar diz-se que **ilumina / _ensonify_** a parte do solo que acerta
![[Pasted image 20250924185618.png|356]]

*Eco*
- Assim, a energia que é refletida de volta para cima (enviada para o receptor) É o **eco**.
    - Um eco mantem as mesmas propriedades de frequência que o sinal original
    - Medimos ecos com **hidrofones**

*Perdas*
- Consoante uma onda se propaga, ela sofre atenuação. Esta varia com a frequência da onda.
- Assim, o primeiro termo a ser considerado é a *perda por absorção* que acontece naturalmente quando a onda se propaga na água. Quando a frequência é maior, também estas perdas o são
- A onda gerada no solo quando há reflexão propaga-se de forma isotrópica (igualmente em todas as direções). Assim, há porções da onda que nunca serão detetadas : temos *perdas de espalhamento*
- Temos as perdas totais da transmissão:
$$\text{Perda transmissão} = \text{Perda Absorção} + \text{Perda Espalhamento}$$
##### SBES (Single Beam Echo Sounders)
- Iluminamos 1 ponto abaixo do projetor com uma frequência 12-200 kHz e tira medição da profundidade _nesse ponto_.

![[Pasted image 20250924224604.png]]
- Na imagem podemos ver que este método resulta em medições erradas: o som reflete em todos os obstáculos, então o primeiro eco vem do obstáculo mais próximo NÃO do obstáculo abaixo do projetor.
    - Além disso, estamos muito sujeitos a inclinações do projetor, devido a ondas no mar
- Quanto MAIOR a face do transdutor, MENOR a largura do feixe. Mais concretamente, a resolução do sonar é dada pelo *ângulo sólido* do feixe.
    - A área iluminada é  $\propto$ ao ângulo sólido do feixe OU $\propto$ quadrado da profundidade
- É ainda possível mecanicamente estabilizar o feixe para aliviar o efeito das ondas do mar
- Notemos que um eco tem que regressar antes que o próximo saia. Isto é algo que temos que ter cuidado quando a profundidade aumenta

##### MBES (Multi Beam Echo Sounders)
- Os projetores iluminam uma risca fina no solo do mal, perpendicular à trajetória do navio
![[Pasted image 20250924234208.png]]
- Mas apenas existe 1 linha de hidrofones LOGO apenas 1 linha de medições é feita (ver imagem no canto superior direito)
- Mas notemos algo importante: 
    - Temos um array de projetores. Ora, cada um emite uma onda sonora esférica. Como sabemos desde OMC, estas ondas vão interferir de forma construtiva e destrutiva. Isto faz com que a propação se torne ANISOtrópica:
        - ![[Pasted image 20250925112246.png|309]] (aqui temos 2 fendas, mas pelo principio de Huygens o padrão é o mesmo que no caso de termos 2 projetores a criar ondas esféricas)
    - Apesar disto, os hidrofones apenas captam uma área reduzida: quase que um só feixe 
    - Vemos estes 2 pontos no canto superior direito da imagem com o barco, há uma grande diferença entre a emissão e recepção de som
- Outra coisa a notar/recordar de OMC é que: para o padrão de difração acontecer como previsto, é preciso que os projetores estarem espaçados de multiplos do comprimento de onda $m\lambda~,~~ m\in\mathbb{Z}$

**Exemplo**
- Consideremos que temos 2 projetores espaçados de $\frac{1}{2}\lambda$:
![[Pasted image 20250925113005.png]]
- Tal como sabemos de OMC, o padrão de difração de algo com múltiplas fendas tem intensidade máxima no centro. No caso de projetores a criar ondas esférricas vemos o mesmo. 
- Como estamos em 3D, o que observamos é que a intensidade é máxima no eixo *perpendicular aos projetores*:
![[Pasted image 20250925113145.png]]
Ou seja, se temos um array de projetores nos XX, iremos ter intensidade de iluminação máxima nos YY. (na figura, dentro da forma temos intensidade máxima).
- No entanto, por funcionarem na base dos mesmos transdutores, os hidrofones também têm uma zona de deteção máxima perpendicular ao seu array:
![[Pasted image 20250925115130.png]]

**Beam steering**
- Nos nossos ouvidos, quando algum som vem do nosso lado direito, a orelha direita capta o som alguns nanosegundos da esquerda e assim percebes de onde veio.
- Podemos inverter esta lógica e aplicá-la em sonares. Os projetores estão sempre a emitir pulsos em sintonia. Se fizermos os *hidrofones* detetar sinal de forma desfazada (uns detetam antes, outros atrasados) conseguimos detetar o sinal que vem de um lado mais do que do outro.
- Na prática, isto permite-nos deslocar a região de intensidade de deteção máxima (que temos acima e é perpendicular ao array de hidrofones) 
- Fazendo isto repetidamente conseguimos detetar os sinais de vários ângulos quase simultaneamente

**Mills Cross**
- Para maximizar a intensidade medida, metemos então o array de hidrofones *perpendicular* ao de projetores, para captar o eixo de interferência construtiva dos projetores.
![[Pasted image 20250925114938.png]]
- Notemos que
    - o array de projetores aponta na direção de movimento do navio, para que a zona de deteção seja perpendicular a este a consigamos fazer um varrimento do fundo do mar
    - Na imagem da esquerda vemos o que acontece neste design: as zonas de deteção/emissão máxima sobrepõe-se e temos um quadrado de deteção - isto é péssimo
    - Na imagem da direita vemos o método de beam steering: a risca de deteção dos hidrofones vai-se movendo ao longo da risca de emissão
- Com este método conseguimos varrer uma seção retangular no fundo do mar, invés de uma só linha

#### LiDAR (Light Detectuib And Ranging)
- Utiliza um emissor e recetor para determinar a distância de um obstáculo
- Pode usar luz UV, IR ou visível
- O transmissor emite um feixe de luz colimada (feixe laser)
- Temos 2 tipos:
    - **LiDAR de deteção direta de energia** - mede a intensidade de luz que regressa ao receptor, mede o TOF e calcula a distância
    - **LiDAR de medição phase-shift** - mede a diferença de fase entre sinal transmitido e recebido e calcula o range

##### Phase-shift
![[Pasted image 20250925121403.png]]
- Consideremos que a distância total que o feixe tem que viajar para ser emitido e regressar é $D'$. Tendo em conta a figura temos que $D'=B+2A$
- Vemos que o feixe transmitido também viaja $B$. 
- Ou seja, a diferença de fase $\theta$ tem que ser causada por $2A$
- Temos que:
$$D = A = \frac{\lambda}{4\pi} \theta$$

##### Divergência
- Apesar de o LiDAR ser bastante focado (por ser baseado em lasers), ainda apresenta divergência
- Isto é algo que se torna especialmente grave quando estamos a tirar medidas do ar para o chão (medir altitude)
- Normalmente o ângulo sólido de LiDAR é da ordem de mrad (mili radiano)

### Sensores de Visão
- AKA câmaras
- Captam a informação diretamente da luz, tentando emitar o que um olho humano faz

#### CCD (Charged Coupled Device)
- Array de capacitors sensiveis a luz (cada píxel do CCD é um capacitor)
- A quantidade de luz/fotões que cada pixel recebe vai variar a carga do capacitor

#### CMOS (Complementary Metal Oxide Semiconductor)
- Cada pixel tem um circuito com lente, fotodíodo, amplificador e ADC. O sinal medido em cada pixel é amplificado

#### Comparação
![[Pasted image 20250925122902.png]]

**CCD**
- O CCD tem apoenas um ADC, ligado a todos os capacitors
- A carga dos capacitors vai passando para os do lado e no final é lida no ADC
- Isto quer dizer que temos um *bottle neck*: é preciso toda a informação chegar e ser lida pelo ADC para que tenhamos a imagem

**CMOS**
- Como dito acima, cada pixel tem o seu ADC então obtemos logo uma medição de luz. Por esta razão, CMOS são muito mais rápidos e ideais para câmaras de alta velocidade
- Apesar disto, estes sistemas são mais baratos porque existe mais desperdício de luz: alguma luz inside no transistor e não no fotodíodo

**Pergunta de exame: Qual é mais sensível, CCD ou CMOS?**
É o CCD. Como falamos acima, no CMOS perdemos luz que não é lida pelo fotodíodo. No CCD isso não acontece porque cada célula apenas tem o capacitor. 
Além disso, configurando o ADC do CCD podemos puxar os limites da sensibilidade da tecnologia facilmente. Claro, não podemos alterar todos os ADCs do CMOS

# Coordenadas
- Como vimos na introdução, sistemas de percepção têm sensores em várias posições e com diferentes orientações
- Assim, precisamos de considerar e estudar os *referenciais* de cada sensor
- Usaremos usar esta onvenção para definir o referencial cartesiano:
![[Pasted image 20250925123552.png]]

## Notação
- Consideremos o caso 2D por simplicidade
- Temos um referencial $B$ que representamos como $\{B\}$. Os seus eixos são $x_{B},y_{B}$
- Consideremos agora que temos um certo ponto no referencial $B$. Podemos representá-lo como:
$${}^{B}P=[p_{x},p_{y}]^{T}$$
- Podemos ainda definir a **pose** do robot, que é a sua posição E orientação:
$${}^{B}\text{Pose}_{R}=[p_{x},p_{y},\theta]^{T}$$
(em que normalmente $\theta$ é medido relativamente a $x$ como vimos acima nas mãos)
que em 3D tem a forma:
$${}^{B}\text{Pose}_{R}=[p_{x},p_{y},p_{z},\theta,\phi,\psi]$$
e os ângulos são medidos relativamente a $x,y,z$.

**Mudar de referencial**
- A pose de um referencial $\{B\}$ relativo a $\{A\}$ é escrita como ${}^{A}\xi_{B}$ 
    - para decorar a ordem: pensemos que o A vem primeiro em cima porque em cima temos "o referencial em que estamos" e temos B em A - "B está em A"
- Usando isto, podemos igualar a posição de um ponto em 2 referenciais assim:
$${}^{A}P = {}^{A}\xi_{B}{}^{B}P$$
![[Pasted image 20250925125153.png]]

- E vemos que nesta notação é facil entender que referencial estamos a converter em qual. Por exemplo, num caso com 4 referenciais, poderíamos fazer isto:
$${}^{A}\xi_{B}={}^{A}\xi_{C}{}^{C}\xi_{D}{}^{D}\xi_{B}$$
![[Pasted image 20250925141232.png]]
- Entendemos também que é relativamente fácil trocar de referenciais. Ou seja, podemos facilmente associar algo medido por um certo sensor (como estando 5m na direção xx) para algo no referencial do robot ou no referencial mundo. 
- Notemos agora que $\xi$ pode ser substituido por qualquer letra, de forma a representar alguma **transformação**!

## Transformações
- No mundo $w$ temos um robot $w$ com uma câmara $c$:
![[Pasted image 20250925141433.png]]
Vemos que a figura da direita esquematiza esta situação de forma rápida e compreensível.
- Aqui dizemos que "o robot é child do mundo" e "a câmara é child do robot". Ao contrário, "o robot é parent da câmara".
    - Usamos estes termos para reforçar que (exemplo) a câmara está contida no robot então o seu referencial estará dependente do referencial do robot: se o robot se mover, o referencial da camara irá mover igual.

### Translação
- Um vetor $t=[t_{x},t_{y},t_{z}]^{T}$ representa uma translação 3D de um objeto no referencial do parent:
$${}^{A}p={}^{B}p+t$$
![[Pasted image 20250925141854.png]]
- Neste exemplo, temos a transformação ${}^{p}t_{c}=[1.5, 1.0, 0.5]^{T}$ que representa $\{c\}$ relativamente a $\{p\}$ através de 1 translação pura. 
- Vendo os pontos 1 e 2, podemos representálos nos referenciais $\{p\},\{c\}$ e temos: $${}^{p}p_{1}=(0,0,0.5) \quad;\quad {}^{p}p_{2}=(0,0,0.5)$$
- E podemos escrever:
$$\begin{cases}
{}^{c}p_{1}={}^{p}p_{1}-{}^{p}t_{c} \\
{}^{p}p_{2}={}^{c}p_{2}+{}^{p}t_{c}
\end{cases}$$

### Rotação
- Usamos a matriz ${}^{A}R_{B}$ para descrever como pontos são transformados de $\{B\}$ para $\{A\}$ através de rotação pura:
$${}^{A}p={}^{A}R_{B}{}^{B}p$$
![[Pasted image 20250925143342.png]]

#### Propriedades de matriz de rotação
- **Ortogonal** (e normalizado)
    - As colunas são vetores unitários (senão a matriz roda e aumenta os vetores)
    - As coluna são ortogonais $u_{i}\cdot u_{j}=\delta_{ij}$
- As colunas da matriz são os vetores unitários que definem $\{B\}$ relativamente a $\{A\}$ 
- O determinante é $+1$ (implica rotação com sentido positivo - mão direita)
- $R^{-1}=R^{T}$
- ${}^{A}R_{B}=\left[{}^{B}R_{A} \right]^{-1}$
- De forma geral, rotações NÃO são comutativas

#### em 2D
![[Pasted image 20250925143912.png]]
- Para obter os pontos nas coordenadas temos:
$${}^{a}p={}^{a}R_{b}{}^{b}p$$
em que temos (sempre assim em 2D):
$${}^{a}R_{b}=\begin{pmatrix}\cos\theta & -\sin\theta \\ \sin\theta & \cos\theta\end{pmatrix}\substack{45º\\=}\begin{pmatrix}0.7 & -0.7 \\ 0.7 & 0.7\end{pmatrix}$$
- Inversamente, podemos fazer: $${}^{b}p=[{}^{a}R_{b}]^{-1}~{}^{a}p$$

#### em 3D
$$\begin{align*}
R_{x}(\theta)&= \begin{pmatrix}1 & 0 & 0\\
0 & \cos\theta & -\sin\theta\\
0 & \sin\theta & \cos\theta\end{pmatrix}\\
\\
R_{y}(\theta)&= \begin{pmatrix}\cos\theta & 0 & \sin\theta\\
0 & 1 & 0\\
-\sin\theta & 0 & \cos\theta\end{pmatrix}\\
\\
R_{z}(\theta)&= \begin{pmatrix}\cos\theta & -\sin\theta & 0 \\
\sin\theta & \cos\theta & 0\\
0 & 0 & 1\end{pmatrix}
\end{align*}$$

#### Ângulos Euler
![[Pasted image 20250927194834.png|500]]
- Podemos definir 3 rotações: **roll**, **pitch** e **yaw**

#### Tipos de rotação
##### Estáticas
- Rotações relativas ao referencial (fixo) do parent
- Normalmente referido como sequência **RPY** (Roll-Pitch-Yaw):
$$\begin{align*}
RPY(\phi,\theta,\psi)&= R_{z}(\psi)R_{y}(\theta)R_{x}(\phi)=\\\\
&= \begin{pmatrix}C\phi C\theta  & -S\phi C\psi+C\phi S\theta S\psi & S\phi S\psi+ C\phi S\theta C\psi\\
S\phi C\theta & C\phi S\psi+S \phi S\theta S\psi  & -C\phi S\psi+S\phi S\theta C\psi\\
-S\theta & C\theta S\psi & C\theta C\psi\end{pmatrix}
\end{align*}$$

##### Relativas
- Cada rotação é feita em torno dos eixos do referencial (móvel) daquilo que roda
- Existem montes de combinações possíveis: XYZ, YZX, ZXY, XZY, ZYX, YXZ, ZXZ, XYX, YZY, ZYZ, XZX, YXY. 
    - Isto acontece porque os eixos são relativos à joint em relação ao joint em rotação. Consideremos que se roda XYX, depois de rodar X temos um Y diferente de antes. Assim temos que considerar todas as combinações, incluindo repetições de eixos
- Um caso comum é 
$$\begin{align*}
R_{ZYZ}(\theta,\phi,\psi)&= R_{z}(\theta)R_{y}(\phi)R_{z}(\psi)=\\\\
&= \begin{pmatrix}C\phi C\theta C\psi - S\phi S\psi & -C\phi C\theta S\psi -S\phi C\psi  & C\phi S\theta\\
S\phi C\theta C\psi+C\phi S\psi & -S\phi C\theta S\psi+C\phi C\psi & S\phi S\theta\\
-S\theta C\psi & S\theta S\psi & C\theta\end{pmatrix}
\end{align*}$$

#### Coordenadas homogéneas
- Estas coordenadas expandem o nosso sistema em 1 dimensão. Isto permite incorporar **rotações e translações** de forma consistente. Esta técnica é computacionalmente mais eficiente
- Consideremos que um referencial $\{A\}$ pode ser representado como uma rotação e translação de $\{B\}$:
$$\begin{align*}
{}^{A}P&= {}^{A}R_{B} {}^{B}P + t\\
\begin{pmatrix}A_{x}\\
A_{y}\end{pmatrix} &= \begin{pmatrix}a & b\\
c & d\end{pmatrix} \begin{pmatrix}B_{x}\\
B_{y}\end{pmatrix} + \begin{pmatrix}t_{x}\\
t_{y}\end{pmatrix}
\end{align*}$$
- Ora, coordenadas homogéneas consistem em reescrever isto nesta forma:
$$\begin{align*}
{}^{A}P&= {}^{A}\xi_{B} {}^{A}P\\
\begin{pmatrix}A_{x}\\
A_{y}\\
1\end{pmatrix} &= \begin{pmatrix}a & b & t_{x}\\
c & d & t_y\\
0 & 0 & 1\end{pmatrix} \begin{pmatrix}B_{x}\\
B_{y}\\
1\end{pmatrix}
\end{align*}$$
ou, em 3D:
$$\begin{pmatrix}A_{x} \\ A_{y} \\ A_{z} \\ 1\end{pmatrix} = \begin{pmatrix}a & b & c & t_x \\ d & e & f & t_{y} \\ g & h & i & t_{z} \\ 0 & 0 & 0 & 1\end{pmatrix} \begin{pmatrix}B_{x} \\ B_{y} \\ B_{z} \\ 1\end{pmatrix}$$
- Vemos então que é acrescentada 1 dimensão ao passar para coordenadas homogéneas

##### Ordem
- Consideremos que vamos fazer uma transformação $\xi_{A}$ e depois $\xi_{B}$.
- Temos 2 possíveis ordens:
    - **Pré-Multiplicação** - ${}^{R}\xi_{1}=\xi_{B}\xi_{A}$, as transformações são todas aplicadas num *referencial fixo* -- temos transformações estáticas!
    - **Pós-Multiplicação** - ${}^{R}\xi_{2}=\xi_{A}\xi_{B}$, as transformações vão sendo aplicadas aos referenciais intermédios -- temos transformações relativas

**Exemplo**
- Consideremos as 2 transformações $\xi_{a}=\text{Rot}(45º)~,~\xi_{B}=\text{Trans}(x,a)$ 
- Consideremos as duas ordens possíveis: ${}^{R}\xi_{1}=\xi_{B}\xi_{A} ~,~ {}^{R}\xi_{2}=\xi_{A}\xi_{B}$ 
![[Pasted image 20250929145618.png]]
- Vemos a diferença no que fazem as 2 transformações

##### Matrizes de transformação
![[Pasted image 20250929145809.png]]
