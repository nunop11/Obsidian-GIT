###### "Measurement of Refractive Index of Liquids"

## Introdução
- Este refratometro mede o quanto a luz é refratada quando passa de ar para uma amostra. Como tal, serve para determinar o RI de uma amostra líquida
- O RI normalmente é indicado com uma precisão de 5 casas decimais.
- O documento tem uma introdução sobre RI e lei de snell :D
- A propagação de um feixe num certo meio depende do meio, através do seu RI. Mas também depende do feixe em si e, mais concretamente, do seu comprimento de onda. 
    - O índice de refração de um material a um certo comprimento de onda é dado por $n_{F}-n_{C}$ (veremos já abaixo o que é). A isto chamamos de *dispersão*
- Temos então o *número de Abbe*:
$$v = \frac{n_{D}-1}{n_{F}-n_{C}}$$
em que $D,F,C$ são os RI do material nos comprimentos de onda das linhas espectrais D,F,C de Fraunhofer (589.2nm, 486.1nm, 656.3nm). Materiais com pouca aberração cromática têm $v$ baixo.
- Medir este valor permite testar a pureza, concentração e condição ótica de um material.

### Refratometro de Abbe
![[abbe.png]]
- Permite medir RI a várias temperaturas
- O funcionamento deste instrumento basei-se em ter a amostra líquida entre 2 prismas: um de iluminação e um de refração.
![[abbe como funciona.png]]
- O feixe de luz é incidido no prisma de iluminação. A face de baixo do prisma é polida para que cada ponto espalhe a onda em todas as direções. Ora, o que devemos notar é que isto significa que na amostra teremos feixes em todas as direções, sempre.
- Vemos na imagem que o feixe que vai de A para B terá o maior ângulo de incidência ($\theta_{i}$) e depois o maior ângulo de refração $(\theta_{r})$
    - Todos os outros feixes terão ângulos inferiores e, juntos, resultam numa zona clara/iluminada abaixo do prisma de refração.

- Assim, amostras diferentes irão resultar em ângulos de refração diferentes. Por sua vez, isto resulta em *posições de separação dark-light diferentes*
    - Ou seja, com calibração adequada, é possível fazer com que a posição desta indique o ângulo 

- O instrumento tem ainda um sistema de compensação da dispersão. Ao rodar o respetivo knob, eliminamos a fringe de cor na linha que divide claro e escuro.

## Experimentalmente
### Medir RI de líquidos
![[procedimento abbe 1.png]]

### Determinar o número de Abbe de água
- O valor da dispersão pode ser determinado com
$$n_{F}-n_{C}=A+Ba$$
em que $A,B,a$ são funções relacionadas com RI e o Z da amostra. Estes valores estão tabelados.
- Daqui temos
$$v=\frac{n_{D}-1}{A+Ba}$$
- Ora, $n_{D}$ é medido diretamente no refratometro (usando um feixe com comprimento de onda da linha D do espetro de Sódio). 
- Para determinar $a$ (ou melhor, para determinar $Z$ para depois ver $a$ na tabela):
![[procedimento abbe 2.png]]

### Determinação de RI de água com sal
- Usando várias amostras de água com diferentes concentrações de sal podemos determinar o RI de cada uma e ver a evolução