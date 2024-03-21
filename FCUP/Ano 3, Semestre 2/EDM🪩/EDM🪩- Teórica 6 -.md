## Projeto de Circuitos Sequenciais Síncronos
- O processo de síntese de FSMs que vimos na aula anterior funciona bem, mas só é aplicável para circuitos pequenos.
- Para circuitos mais complexos fazemos *decomposição hierárquica de FSMs*: uma FSM controla outras. Para isto, podemos criar funções padrão.

### Circuito Síncrono
- Todos os flip-flops têm o mesmo sinal. 
- O circuito é combinacional entre os flip-flops. Podemos esquematizar assim:
![[Pasted image 20240314093358.png]]

### Funções Sequenciais Padrão
**Registos** - armazena vários bits em paralelo. Basicamente um flip-flop de vários bits.
**Contadores** - percorrem uma sequência de estados cíclica. Podem ser binários, aleatórios, crescente ou decrescente.
**Registos de deslocamento** - deslocam os bits a cada tick.
veremos agora cada um destes:

## Registos
- Consiste num conjunto de flip-flops tipo D que permite armazenar vários bits:
![[Pasted image 20240314095943.png]]
- Temos registos com
    - 4,6,8... bits -- consiste em ter N entradas e N saídas
    - CLR -- Clear, uma entrada que quando ativada torna as saídas todas 0
    - EN -- Enable
![[Pasted image 20240314100232.png]]

## Contadores
### Assíncrono
- Contam em binário, decimal ou outras sequências. Podem ser síncronos ou assíncronos.
- Podem ser usados para regular comportamento de uma FSM 
- Podemos fazer um com contador com Flip-flops tipo T:
![[Pasted image 20240314100446.png]]
a imagem explica bastante bem. Sendo $Q_{2}$ o MSB temos a sequência de acontecimentos:
    - Temos sempre $EN=1$. Assim, sempre que a entrada CLK é ativada o valor muda.
    - $Q_{i}=0$ temos 0
    - $Q_{1}=1$ devido ao CLK.
    - Na próxima subida do CLK, $Q_{1}=0$ mas isto ativa a entrada CLK do 2º FF tipo T logo ficamos com $Q_{1}=1$. Temos o número $010_{2}=2_{10}$
    - CLK sobe e fica $Q_{1}=1$ (sem afetar $Q_{2}$). Temos $011_{2}=3_{10}$
    - O CLK sobe, ficamos $Q_{1}=0$. Isto faz $Q_{2}$ mudar para 0. Isto por sua vez faz mudar $Q_{2}$ para 1. Fica o número $100_{2}=4_{10}$
    - por aí fora....

### Síncrono
![[Pasted image 20240314101139.png]]
- Ser síncrono significa que todos os FF têm o mesmo sinal CLK. Atingimos a funcionalidade ao ter as entradas $T_{1},T_{2}$ a depender de $Q_{0},Q_{1}$ (do bit anterior).
- Podemos ainda fazer isto com FF tipo D:
![[Pasted image 20240314102234.png]]

### Contador com Load (LD)
![[Pasted image 20240314101940.png]]
- Quando o canal LD é ativado todos os Mux passam para a entrada $1$. Assim, o contador passa para o número $D_{2}D_{1}D_{0}$. Isto permite, por exemplo, contar $1,2,3,6$.

### 74x163
- Temos:
![[Pasted image 20240314102508.png]]
as 2 entradas EN são redundância e nem o prof tentou explicar.

### Exemplo
- O PPT todo é exemplos.