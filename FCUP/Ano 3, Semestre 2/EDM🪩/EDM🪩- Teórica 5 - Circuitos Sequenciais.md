**EX1 - Televisão**
- Consideremos uma televisão com botões para mudar de canais. Temos 4 botões e 4 canais. Ora, basta ter um circuito simples em que o botão $B1$ liga o canal $CH1$ e por aí fora. Temos então um circuito combinatório
- Imaginemos agora que temos outra televisão comm 4 canais na mesma, mas agora com 2 botões: um para passar para o próximo canal, outro para passar para o anterior.
    - Já não podemos ligar 1 botão a 1 canal
    - Além disso, para termos a funcionalidade esperada temos que ter uma nova variável: o estado atual. Ou seja, só posso avançar para o canal 3 se souber que agora estou no 2. Queremos um sistema **sequencial**!

**EX2 - Tanque com eletroválvula**
![[tanque sistema.png]]
- Consideremos agora o sistema acima. Temos um tanque. Quando a água está a "tapar" o sensor VAZIO este dá sinal 1, quando "tapa" o sensor CHEIO este dá 1.
- Temos então a sequinte tabela de verdade:
![[tabela vdd tanque.png]]
e podemos até definir a expressão lógica: $ABRE=\overline{CHEIO}$
- Temos uma eletro-válvula controlada por um circuito digital que decide quando é que passa água na torneira de cima ou não AKA quando enchemos ou não o tanque.
- Ora, se a água não puder sair, o circuito é combinatório, enchemos 1 vez o tanque e pronto.
- Mas podemos ver na imagem (e o que aconteceria na vida real é isto) que temos uma saída de áfua (para consumo, por exemplo) na parte inferior do tanque. Isto trás complicações:
    - Consideremos que o tanque está cheio. Temos ABRE=0.
    - Alguém abre a saída de água, o nível baixa. 
    - Eventualmente o nível de água baixa o suficiente para que ABRE=1
    - A torneira abre e o tanque enche (consideramos que enche mais rápido que esvazia pela saída), mas só irá encher até ao nível CHEIO. Ficamos com ABRE=0
    - A água continua a sair, o nível baixa e volta-se ao estado ABRE=1.
    - Ficamos num loop. Ora, isto é mau para a durabilidade do sistema e da válvula, logo não podemos ter um sistema assim na vida real. Precisamos de um sistema **sequencial**.

# 5 - Circuitos Sequenciais
- Nos 2 exemplos que vimos acima, além das entradas (botões B1,B2 e níveis CHEIO,VAZIO) para a saída do circuito ser adequada à vida real percisamos de uma nova variável: *estado atual*. A este, podemos chamar de **variável de estado**.
- Na prática, isto significa que estamosa introduzir uma nova grandeza no estudo de circuitos: **tempo**, porque o conceito de "estado atual" e "estado seguinte" passam a existir.

## 5.1 - Variáveis de Estado
- Consiste num conjunto de 1+ bits
- Armazenados em flip-flops (memórias digitais, mais info à frente)
- Num sistema de $N$ variáveis de estado temos $2^{N}$ estados diferentes possíveis.
    - No caso da televisão acima, temos 4 canais AKA $2^{2}$ estados possíveis logo precisaríamos de 2 flip-flops
    - Como $N<\infty$ surge um nome para circuitos com variáveis de estado e memória: "Máquinas de Estados Finitos" -- Finite State Machines: **FSM**.

## 5.2 - Funcionamento
- De um modo geral, todas as FSM têm este formato:
![[Attachments/FCUP/A3S2/EDM/esquema msf.png]]
- É verificado se ocorrem mudanças de estado de acordo com um relógio bem definido:
![[ciclo msf.png]]
quando falamos de um processador com frequência de X GHz essa é a frequência deste relógio AKA a frequência com que o circuito verifica o seu estado.

### 5.2.1 - Flip Flops
![[flip flop.png]]
- Ao circuito flip-flop acima chamamos de circuito **bi-estável**. Usamos portas lógicas normais com realimentação das saídas nas entradas.
- Mas o circuito acima não tem qualquer ligação ao exterior, consistindo num circuito fechado. Assim:

#### Latch Set/Reset
![[latch set reset.png]]
(a última linha da tabela de verdade é inválida porque, por definição, temos que $QN$ é $Q$ negado, logo não podem ser iguais)
- Ou seja, quando $R=S=0$ o sistema "desliga-se" e $Q,QN$ ficam com o seu valor inicial.
- O nome vem de que quando $S=1$ (Set) ficamos com $Q=1$ e quando $R=1$ (Reset) fica $Q=0$
- Usando este circuito podemos resolver o problema do tanque de água:
![[flip flop tanque.png|415]]
    - Ou seja, a torneira abre-se quando o nível está abaixo de VAZIO (S=1). Consoante a água no tanque sobe ficamos com S=0. A torneira fecha quando a água chega ao nível CHEIO (R=1).

- Podemos ter ainda um Latch Set/Reset com Enable:
![[flip flop enable.png]]

#### Latch tipo D
![[latch tipo D.png]]
- AKA latch transparente. Este nome vem do facto que se $EN=1$ a latch é transparente (podemos ver na imagem acima, no gráfico)
- Quando $EN\to0$ o sistema fica no mesmo estado que estava antes da mudança AKA *memoriza* o estado.

#### Edge-triggered D flip-flop
- Observa bem:
![[d triggered.png]]
- A lógica é esta: 
    - O sistema muda nas **subidas** de $CLK$ (e se a entrada, $D$, variar, claro). Na figura acima estes momentos estão assinalados.

- Estes sistema pode ser representado assim:
![[tipo d representacao.png]]

- Quando há o risco de $CLK$ e $D$ mudarem de valor no mesmo instante, devemos tentar arranjar outro tipo de flip flop. Porque quando isto acontece o sistema "não sabe" se passar para 0 ou 1.

#### Outros flip-flops edge-triggered
**tipo T - toogle**
![[tipo t.png]]

**tipo JK**
![[tipo jk.png]]

## 5.3 - Síntese / Equação de MSF
- Consideremos o seguinte sistema com entrada $X$ e saída $Y$:
![[ex msf.png]]
como vemos, ele só retorna $Y=1$ se for detetada a sequência 1011. (Como já vimos, os valores de $X$ são medidos quando $CLK$ transita $0\to1$)

- Podemos então fazer o seguinte diagrama de estados:
![[esquema msf 1.png]]
espero que entendas isto porque não vou explicar passo a passo por texto.
- Em que definimos os estados:
    - $INI$ - não foi detetado nade de interessante -- estado inicial
    - $S1$ - Detetou-se $X=1$
    - $S2$ - detetou-se a sequência 10 em $X$
    - $S3$ - detetou-se a sequência 101 em $X$
    - $OK$ - detetou-se a sequência 1011 em $X$. Se chegarmos aqui, passamos para $Y=1$. Em qualquer estado seguinte voltamos a $Y=0$


- Podemos ainda esquematizar isto em tabela:
![[tabela ex msf.png]]
- De notar que o mais importante aqui é o estado *atual*, em que $S^{*}$ é o estado seguinte.
- Temos então a representação da máquina de estados finitos (MSF):
![[esquema geral msf.png]]
em que a saída apenas depende do estado.

#### Equações de Flip-flops
- Sendo $Q$ o valor atual e $Q^{*}$ o seguinte:
    - *tipo D* : $Q^{*}=D$
    - *tipo T* : $Q^{*}=\overline{T}.D+T.\overline{D}$ (o valor troca se $T=1$)
    - *tipo JK* : $Q^{*}=\overline{Q}.J+Q.\overline{K}$ (Se $K=J=1$ troca valor de $Q$, se $J=1,K=0$ fica $Q=1$, se $J=0,K=1$ fica $Q=0$)

#### Codificação de estados
- Codificados em binário
- Para codificar $N$ estados usamos $\lceil ~\log_{2}N~\rceil$ flip-flops 
    - Se $N=8=2^{3}$ usamos 3 flip-flops
    - Se $N=10$ usamos $\log_{2}10=3.3$ logo 4 flip-flops.
    - Invés da fórmula com o ceiling e logaritmo, podemos simplesmente ver que precisamos do número de flip-flops correspondentes à primeira potência base 2 acima. Para $N=10$ a potência mais próxima é $16=2^{4}$ logo precisamos de 4 flip-flops.
- Representamos um estado $S$ de 3 bits como $S=Q_{2}Q_{1}Q_{0}$.

#### Tabelas
- Podemos então definir os estados como:
![[tabela definicao de estados.png]]
esta definição influencia por completo o resto do processo de obtenção da equação do MSF. Por esta razão, na maioria dos exercícios, esta tabela será dada.

- Usando estas definições, a tabela que fizemos acima com $S,S^{*},Y$ fica assim:
![[tabela msf com flip flops.png]]

#### Obtenção do Circuito
**Tabela de Verdade**
- Usando esta tabela conseguimos facilmente fazer uma tabela de verdade em que temos as entradas $S,X$ e as saídas $S^{*},Y$:
![[tabela verdade msf.png]]
por exemplo, olhemos para a linha 3 (começando a contar no 0) se $S=001=S_{1}$ e $X=1$ então de seguida iremos ter $S^{*}=INI$ e $Y=0$, o que bate certo com a tabela que vimos inicialmente para representar o fluxo do sistema. 

- Para implementar isto de uma forma mais prática, podemos só substiruir $Q_{i}^{*}$ por $D_{i}$ usando um flip-flop tipo D:
![[tabela verdade msf com tipo d.png]]
- As linhas finais correspondem a estados que não definimos (apenas temos $INI,S_{1},S_{2},S_{3},OK$ e temos uma tabela de verdade correspondente a 8 estados) continuam a fazer parte da tabela e consequentemente do circuito que criamos para a tabela!
- Como tal, temos que definir o quê que o sistema faz no caso em que surja uma entrada destas. Temos 2 métodos usuais:
    - *custo mínimo* - assumimos que estes cenários nunca vão ocorrer e consideramos as saídas $D_{0},D_{1},D_{2},Y$ indiferentes. -- colocamos "d" na tabela : "don't care". Há o risco de irmos parar a estes estados (não percebi bem o que acontece)
    - *risco mínimo* - se o sistema for para um destes estados simplesmente voltamos a $INI=000$

**Karnaugh**
- Usamos karnaugh ou algo do Género para simplificar as expressões lógicas.
- De notar que para cada entrada $D_{2},D_{1},D_{0},Y$ temos 1 mapa de Karnaugh para resolver, pelo que temos 1 equação para cada saída.
- Para este circuito em específico (para risco mínimo) temos>
$$\begin{cases}
D_{2}=\overline{Q_{2}}.Q_{1}.X \\
D_{1}=\overline{Q_{2}}.Q_{1}.\overline{Q_{0}}.X + Q_{2}.\overline{Q_{1}}.\overline{Q_{0}}.X+\overline{Q_{2}}.Q_{0}.\overline{X} \\
D_{0}=\overline{Q_{1}}.\overline{Q_{0}}.X+\overline{Q_{2}}.\overline{Q_{0}}.X+\overline{Q_{2}}.\overline{Q_{1}}.X \\
Y=Q_{2}.\overline{Q_{1}}.\overline{Q_{0}}
\end{cases}$$

**Circuito**
![[circuito risco minimo.png]]

- Se tivessemos obtido as equações usando o método de custo minimo teríamos equações diferentes (que não vou escrever) e o circuito seria:
![[circuito custo minimo.png]]

