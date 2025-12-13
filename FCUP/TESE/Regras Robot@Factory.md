## Intro
- A competição baseia-se em ter um robot numa "pista" que é uma fábrica. Nela, ele terá de mover e organizar caixas. 
- A pista tem o tamanho de 2 folhas A0
- O robot tem de ver o que fazer com uma tag ArUco, mover as caixas, localizar-se e não bater com paredes.

## O robot
- Tem de caber num volume de 30x30 cm e altura de 30cm.
- Não pode comunicar com o exterior após começar a prova

## A pista
- Tem dimensões máximas de 1.7x1.2 m
- Temos:
    - 4 máquinas no centro (cada uma tem entrada e saída)
    - 2 armazens, uma no canto superior e outra no inferior. A superior para produzir/ir buscar os produtos e a inferior para entregá-los.
![[pista robot at factory.png]](as aruco tags podem ser geradas em https://chev.me/arucogen)
- Temos os índices e o referencial recomendado:
![[pista raf com arucos e indices.png]]
(os números a azul correspondem a arucos colocados na vertical, na parede de uma máquina ou armazem)
- As coordenadas são conhecidas: (incerteza de $\pm10\%$)
![[localização arucos no chao.png]]

E temos as coordenadas das máquinas e armazens:
![[localização arucos nas paredes.png]]
(notemos que estão a 10cm de altura)

- Em 3D temos:
![[simulação 3d de raf.png]]
e temos as paredes que serão medidas pelo LIDAR

## Máquinas e armazéns
![[esquema de pista raf.png]]
- Como vemos, cada máquina tem uma entrada e uma saída. O robot tem de deixar a caixa do lado esquerdo E ir buscá-la do lado direito
- Temos as dimensões exatas:
**Caixas**
![[maquinas e suas paredes - raf.png]]
**Armazéns**
![[armazem e suas parede - raf.png]]

- Temos as **_informações das paredes_**:
    - Parede esquerda: 
        - Arucos em $(-357.5, 0)~;~(-337.5,0)~;~(-357.5,-150)~;~(-337.5,-150)$
        - Centro dos pares de arucos: $(-347.5,0)~;~(-347.5,-150)$
        - Centro da parede: $(-347.5,-75)$ com orientação YY e comprimento de 32cm
    - Parede esquerda: 
        - Arucos em $(357.5, 0)~;~(337.5,0)~;~(357.5,150)~;~(337.5,150)$
        - Centro dos pares de arucos: $(347.5,0)~;~(347.5,150)$
        - Centro da parede: $(347.5,75)$ com orientação YY e comprimento de 32cm 
    - Armazem superior:
        - Arucos em $(-695,565)~;~(-545,565)~;~(-395,565)~;~(-245,565)$
        - Centro da parede: $(-470,565)$ com orientação XX e comprimento de 62cm
    - Armazem inferior:
        - Arucos em $(245,-565)~;~(395,-565)~;~(545,-565)~;~(695,-565)$
        - Centro da parede: $(470,-565)$ com orientação XX e comprimento de 62cm

## Peças
- Movem-se peças com 90mm de largura, 60mm de comprimento e 65+mm de altura
- Em cada peça existe uma placa 20x80 mm que permite levantá-la com um eletromagnet:
![[caixas - raf.png]]
- O robot deixa uma peça no lado esquerdo da máquina. Do lado direito vai levantar uma peça nova, de outra cor. Existe este sistema:
![[cores e tipo de produto raf.png]]
- Para agarrar e cenas, pode-se acrescentar algo no topo de cada peça, para agarrar melhor? Esta apenas pode aumentar a altura da peça!

## Servidor da competição
- Um servidor IEEE 802.11ac informa cada robot sobre os tipos de peça em cada onda. O robot pode pedir a informação varias vezes
- Este sistema permite ao robot saber que peças existem onde, **durante a onda**
- Protocolo:
    - O robot envia um packet UDP a pedir as peças dos armazens incoming ou outgoing com IWP ou OWP, respetivamente. O servidor envia a lista de caixas conforme as iniciais das cores: "blue, green, green, red" fica "BGGR"
    - O robot envia um packet UDP a pedir a lista de peças na máquina de tipo A ou B. Usa o string MAP ou MBP, respetivamente. O servidor envia a lista através de iniciais das cores *ou* "X" para indicar que não temos essa peça no compartimento da máquina A ou B. 
        - A lista indica os 4 compartimentos de cada tipo de máquina. Por exemplo: "BRXG" indica que temos:
            - Peça Blue no canto superior esquerdo
            - Peça Red no canto superior direito
            - Nenhuma peça no canto inferior esquerdo
            - Peça Green no canto inferior direito
            - A ordem das iniciais segue esta ordem: ![[organização de 1234 nas maquinas.png]]
    - Se for feito um pedido de informação *antes* de começar a run, o servidor envia um packet UDP a dizer "STOP"
    - O robot pode enviar um UDP a dizer "CTL" (competition time left) e o servidor envia "Txxx" em que "xxx" é o tempo em segundos até ao fim da onda atual
    - O robot pode enviar "PING" para verificar a lidação. Se estiver a funcionar, o servidor envia "PONG"

- O primeiro pedido com informação recebida por parte do robot marca o início da contagem de tempo da tentativa atual:
![[logica de comunicação com servidor udp.png]]

## Marcadores e localização
- No chão existem marcadores Aruco. Lendo o tag, sabemos o indice e as coordenadas atuais.
- Podemos usar outras técnicas para localizar
- Perto dos 4 cantos da pista existem 4 áres reservadas para as equipas deixarem marcadores. Estas áreas são quadrádos com 10cm de lado e altura max de 50cm

## Competição
- Temos 3 ondas, que devem ser feitas em 3 dias
    - Cada equipa tem 10min para testes na pista
    - Durante a run, cada equipa tem 10min para fazer o máximo de runs que conseguir/quiser
- Em cada tentativa, a pontuação é o número de partes colocadas no armazem de saida ou em máquinas
    - Para desempate usa-se o tempo da run e possiveis penalizações
- Existe uma zona específica para o robot começar:
![[zona de começar raf.png]]

### Onda 1
- Pegar nas 4 caixas que estiverem no armazem de entrada e levar para o armazem de saída
- Aqui vai ganhar quem for mais rápido

### Onda 2
- Temos 4 caixas no armazem de entrada. Mas agora *algumas* têm de ser levadas a uma máquina A ou B.
- O robot leva a caixa da entrada para o input da máquina (lado esquerdo da máquina). Depois vai buscar a caixa "processada" ao lado direito da máquina e leva para o armzem de saída
- REGRA: 2 tentativas seguidas têm que ser espaçadas de 1min, para permitir à organização repor as caixas no sítio

### Onda 3
- Aqui entram os 3 tipos de peças que vimos acima. As peças vão passar por várias máquinas:
![[tipos de produtos e o que fazer raf.png]]
(notemos que do output da máquina A para o input da máquina B basta ir para a direita)
- REGRA: novamente, tentativas têm de ser espaçadas de 1 minuto

### Problemas com o robot
- Se a equipa achar que o robot teve um problema técnico ou foi parar a uma situação/sítio de onde não vai sair pode pedir para intervir. Durante a intervenção, *o tempo não para*
- Se a equipa quiser reiniciar o robot e fazer outra tentativa, tem de pedir ao arbitro. Ele, por sua vez, deverá reposicionar as peças aleatoriamente para o robot não benificiar do reset
    - Depois *do pedido* para reiniciar, a equipa não pode mexer no robot, apenas reinicia-lo

### Parque fechado
- Até 15 minutos antes da ronda, o robot fica no parque fechado, onde as equipas não lhe podem mexer
- Um certo tempo antes de começar a ronda, a equipa pode aceder a pista (para colocar marcadores nos cantos e etc)
- Quando o arbitro indicar, a equipa coloca o robot no sitio para começar a ronda

### Classificação final
- A pontuação consiste no número de peças colocadas bem. Notemos:
    - Peças azuis são bem colocadas 1 vez (no fim)
    - Peças verdes são bem colocadas 2 vezes (numa máquina A/B e no fim)
    - Peças vermelhas são bem colocadas 3 vezes (máquina A, máquina B e no fim)
- Critérios de **desempate** caso equipas tenham o mesmo número de peças bem colocadas:
    1. Número de peças bem colocadas *no armazem de saída / no final*!
    2. Tempo para completar (soma dos melhores tempos de cada ronda)

# Juri, Arbitro, tempos
## Juri
- São quem manda e decide as regras, em casos de duvida ou problemas que surjam
- Não dá para fazer appeal das decisões do juri

## Árbitro
- Enforça as regras e dá permissão a equipas para entrar na pista, interrompe rondas, etc
- Se acontecer algo fora das regras, o arbitro tem de consultar o juri

## Contagem de tempos
- Usado um sistema automatico digital