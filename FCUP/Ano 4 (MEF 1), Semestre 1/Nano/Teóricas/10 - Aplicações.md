# 1 - Eletrónica
- Processadores, memória RAM e storage (SSD,HDD) são fundamentais
- Temos:
![[componentes pcs.png]]

## 1.1 - Storage
**Magnético**
- Tem vindo a aumentar em termos de storage/área de ship
![[evo densidade armazenamento.png]]
- Temos vários platters/discos com informação gravada de forma magnética
    - Ou seja, guardamos dados binários como direções de magnetização
- Temos um atuactor que move um braço sobre o disco, que roda a 10000rpm
- Permite ter grandes densidades de dados a baixo custos
- Temos platter somc 10-50 nm de espessura, com grains com diâmetros 10-30nm

![[frequencia cpu.png|475]]
- Cada bit tem centenas de grains
- O bit é então decidido ao fazer média estatisticamente pelos grains. Isto permite um bom signal to noise ration

![[metodos escrever memoria.png]]
- Discos rígidos armazenam os dados de forma longitudinal ou perpendicular
- Para escrever, temos uma cabeça que vai passando e usa um campo magnético para definir spins
![[metodos de  ler memoria.png]]
- Para ler os dados usamos uma cabeça magnetoresistiva
    - Ou seja, as 2 cabeças são diferentes
    - Temos alta sensibilidade e pouco ruído
    - O sensor é contactless, logo não há desgaste do disco
    - Feitos com photolithography

### 1.2 - Spintronics
- Usando o spin de eletrões, consegue-se diminuir bastante a escala de discos rígidos
- Em metais de transição, temos spins que contribuem para transporte de carga divididos em 2 tipos:
    - spin localizado carregados por eletrões pesados 3d
    - spin itinerante carregados por eletrões light 4s 
- Temos s-d scattering entre eletrões itinerantes e localizados

### 1.3 - Magneto resistência
![[magnet resist.png]]

### 1.4 -  SSD
- Discos solid state não têm peças móveis, logo elimina-se o tempo de seek e de rotação
- O SSD é melhor que HDD em tudo menos: capacidade, preço e durabilidade
- Temos ciclos de escrita limitados

## 2 - Memórias
- A quantidade de RAM necessária à escala mundial aumenta exponencialmente
- Temos DRAM (condensadores, barato e lento), SRAM (transistores, rapido, caro) e flas (lento, vida limitada)

### 2.1 - MOSFET
- Funciona como um transistor 

### 2.2 - Flash
- Funciona como um transistor, mas com um floating gate que armazena carga. Podemos ter alta tensão positiva e negativa (a tensão faz os eletrões entrar no gat de controlo por tunneling se for alta, faz sair se for baixa)

### 2.3 - Novas tecnologias
- A maioria de novas tecnologias aproveitam o conhecimento de teorias e física quântica

#### MRAM (Magnetic RAM)
- Usamos um campo externo para inverter uma camada. Isso decide então 1 bit.
- Temos o problema que os bits vizinhos são alterados, logo não temos seletividade
- A densidaded de corrente que temos tem que passar um certo threshold para conseguirmos inverter o estado de magnetização. Na escala nano isto pode ser difícil

#### ReRAM (Resistive RAM)
- Trocamos entre ON e OFF de forma elétrica
- Escrevemos compulsos de tensão fortes
- Lemos o estado com pulsos de tensão fracos
![[reram.png]]
temos metal, isolador, metal.
- Temos um "filamento", que consiste numa ligação entre os 2 eletrodos, que ocorre consoante aniões ou catiões se movem no óxido.

**Migração de anião**
- Usamos óxido de metal de transição na camada central. Esta é a opção mais aplicável
- O processo de switch é reversível, não volatil. A leitura não é destrututiva
- Limitado à espessura dos filamentos (2-10nm)
- Podemos ter perda de energia na forma de calor
- Falta ainda conhecimento para poder otimizar o método

**Migração de catião**
![[migracao.png]]
- Os filamentos serão de 2nm
- Perdemos energia na migração em si
- O maior desafio é que para aumentar a velocidade temos que aumentar a tensão. E tensão muito alta não é prático

## 3 - Computação neuromórfica
- O botteleneck de Von Neumann diz que a RAM e a CPU não ganham performance ao longo dos anos ao mesmo ritmo, o CPU melhora muito mais rápido. Ou seja, a performance de RAM não consegue acompanhar
- Além disso, as "computações" do cérebro são feitas com um custo de energia muito mais baixo do que programação normal.
- Computação neuromórfica consiste em sistemas large-scale que emitam arquiteturas neuro-biológicas
    - É então preciso conseguir imitar as dinâmicas não lineares dos neurónios e o paralelismo e densidade
- A implementação mais comum de tentar fazer isto são **redes neuronais**!

### Neurónios artificiais
- 