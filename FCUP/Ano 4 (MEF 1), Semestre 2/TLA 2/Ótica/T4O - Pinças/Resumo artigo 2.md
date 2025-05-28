## Sistema acessível de pinças oticas para cursos uni
- Artigo de 1998
- Aqui é proposto um sisstema de pinça ótica de feixe único com forças de gradiente, com um custo total de 6500 dolares (quase 13000 ajustando inflação)

### Intro
- Luz pode ser usada num pinça ótica para prender particulas/moleculas/ADN
- Mas quase todos os sistemas são muito caros. Neste artigo usam uma lente de microscopio bem barata e usam-se elementos óticos comercialmente disponíveis. Para montar o sistema só são precisas chaves 
    - Um aluno under graduate deverá precisar de ~95h para montar tudo
- Verificou-se que este sistema consegue prender bolas de poliestireno

### Teoria de pinça ótica
- Todo o funcionamento basei-se na transferência de momento da luz para objetos. A reflexão e refração de luz no interface mudam o momento da luz em $\Delta p$ - para haver conservação de momento tem de mudar o momento do dieletrico/objeto em $-\Delta p$ 
- Este artigo explica bastante bem o funcionamento da repulsão e a forma como os feixes movem o objeto
- Se não houvesse damping no meio envolvente (vacuo), uma partícula que entra na pinça também sairá. Num meio normal há damping logo a uma partícula pode ficar presa.
- Temos que
    - um feixe mais forte dá uma trap mais forte
    - se o tamanho do trap diminuir, a trap fica mais forte
    - a trap é mais fraca onde o gradiente de luz é menor - no centro do feixe

### Elementos de uma pinça
#### Oticas da trap
- O setup de uma pinça normal é deste tipo
![[montagem pinca otica 2.png]]
![[montagem pinca otica 3.png]]
- E penso que o segundo será o tipo que temos no lab
- Tendo uma certa objetiva de microscopio escolhida e um certo laser: maximizar a profundidade da trap consiste em ajustar o tamanho e curvatura da luz incidente de forma que a luz fique focada e garanta um máximo de gradiente de intensidade $\nabla I$
- Aumentamos $\nabla I$ ao diminuir $w_{trap}$ e manter a potência do laser constante. 	
- A difração da luz limita bastante o quanto podemos baixar $w_{trap}$. Para uma lente ideal com distância foca $f$ a focar um laser de diametro $D$ e comp onda $\lambda_{0}$ teremos:
![[largura trap pinca otica.png]]
- Com uma objetiva 100x imergida tem NA=1.25 e temos $w_{0}=0.17\mu m$ quando usamos luz vermelha $633nm$
- Para uma certa lente, a trap tem força máxima quando o diâmetro da luz $d$ é $\approx D$, o diametro da objetiva.
    - Ou seja, a trap é mais forte quando "preenchemos a objetiva"
    - Se $d<D$ teremos $w$ maior e a trap é mais fraca
    - Se $d>D$ teremos um $w$ igual a quando $d\approx D$. Mas como nem toda a luz do feixe entra na objetiva, temos menor intensidade e portanto uma trap mais baixa.
    - Usamos então 2 lentes para focar o feixe e ter o diametro certo

#### Imaging
- Para conseguir ver as particulas usamos o sistema mostrado na figura. Para isso, usa-se a luz do condensador.
- A luz passa no prisma que funciona como beam splitter e chega ao CCD
- Se for usado um microscopio com câmara, ela pode ser usada mas com um filtro de cor para facilitar/permitir a visualização da luz
- O laser, mesmo que com comprimento de onda visível, deve ser dificilmente visível na eyepiece. De qualquer forma, por uma questão de segurança, nunca se deve olhar na eye piece

### Escolher componentes
#### Laser
- Explica mt bem e cenas mas não escrevi porque claramente não vamos fazer
- Para objetos não-vivos lasers visiveis estão OK. Para vivos, laseres visiveis têm alta absorção queima a amostra
- No artigo usaram-se lasers He-Ne vermelhos e lasers Ar verdes

#### Pinhole
- Para muitas objetivas, a difração devido a um pinhola $a=40\lambda$ a 16cm  da objetiva, gera um um ponto de foco "mal focado". 
- O pinhole é então usado para focar. Ajustamos o tamanho do foco até que o diametro do feixe seja igual ao do pinhole. Nesse momento, veremos que não haverá difração. 
- Quando tiver focado o laser, tiramos o pinhole

#### Lentes
- Para minimizar aberrações, usar lentes com distância focal entre 5cm e 40cm
- Se for precisa manigicação maior que 8:1, usar lente telescopica
- É util ter coating anti-reflexão nas lentes
- Temos que ajustar a magnificação de forma que o diametro do feixe seja o diametro da objetiva.
- Aqui falamos das 2 primeiras lentes depois da fonte

#### Manipulação
- Neste sistema, movemos o suporte da amostra para a mover na pinça, invés de mover a pinça em si
- Notemos que apenas temos precisão de microns

#### Imaging
- Tanto ao ver com o CCD como na eyepiece, devemos usar filtros para reduzir a intensidade da luz

### Alinhamento
#### Preparação
- Limpar os elmentos oticos
- Os espelhos são colocados em suportes que permitem ajustar 2 ângulos do espelho. Com 2 espelhos montados conseguimos controlar completamente o feixe
    - O espelho 4 entre a ultima lente e o pinhole permite focar no pinhole
- Para fazer o alinhamento não devemos ter nenhuma lente nem a objetiva colocadas no sistema - apenas espelhos

#### Alinhamento rough
- Queremos fazer o feixe seguir o percurso previsto e acabar no espaço onde estará a objetiva. Além disso, para ter mais espaço de manobra o feixe deve estar no centro de todos os espelhos
- Ao entrar no microscopio, o feixe deve ter a posição e angulo certos. Estes podem ser controlados colocando uma *lamela* pousada horizontal na "mesa" do microscopio. A luz deve entrar no microscopio, refletir na lamela e repetir o percurso otico para trás.
- Pegamos num pedaço de papel e fazemos um furo pequeno. Metemos isso no percurso ótico. O feixe de ida passa no buraco e iremos ver o feixe de volta a bater no papel.
- Depois desse alinhamento, colocar as lentes 1 a 1. 
    - Começar com a lente mais próxima da fonte, L1
    1. centrar cada lente no feixe
    2. ajustar a lente para que a luz refletida vá diretamente para trás - isto garante que a lente está perpendicular ao feixe
- Colocar L1, depois L2. Ajustar a distância entre elas (elas formam o telescopio) até que:
    - o feixe a sair de L2 seja colimado
    - a half-width à saida de L2 seja 0.75cm
- Colocar L3 - esta é a lente que ajusta curvatura
    - para ajustar a posição desta lente, meter o pinhole $40\lambda$ a 16cm da objetiva. 
    - Ajustar posição APENAS com L3 e M4 de forma que 75% do feixe passe no pinhole
- Colocar a objetiva
    - Deve ser mais facil ver o alinhamento do feixe com a objetiva sem condensador no sítio. Depois de alinhar, colocar de volta
- Como na figura acima, ajuda ter 2 espelhos perto da objetiva: $m_{4},m_{5}$.
    - M5 está tão perto da objetiva que quase só controla o ângulo com que a luz bate na objetiva. M4 controla principalmente a posição.
    - No alinhamento, primeiro usamos M5 e depois M4

### Trapping
#### A amostra
- No artigo usaram bolas poliestireno com 3um
    - Mistura-se 40muL de água com bolas. Coloca-se na lamela e cobre-se com uma cover slip. Colocar uma gota de fluido de index matching
    - Devemos ter uma amostra com $\le50\mu m$ de espessura senão a pinça fica muito fraca devido a aberrações esféricas
    - Podemos estimar a espessura da amostra ao mover na vertical a "mesa". Mover deste ter o foco no topo até ter na base

#### Preparação
- Colocar objetiva no centro da amostra
- Ajustar o foco até conseguir ver esferas
- Ajustar fine o foco até ver as esferas no fundo da amostra
- Ajustar intensidade, aperture, posição do consensador para ter contraste máximo
    - Alinhar o CCD neste passo
- Encontrar a posição da trap. Usar apenas CCD neste passo
    - Desligar o condensador
    - Ligar o laser com muito baixa potência ou colocar um filtro forte
    - Mover a mesa até ver no CCD um ponto com fraca iluminação - temos o spot - o que vemos é o feixe a refletir na lamela na base da amostra
    - Se não virmos nada, aumentar a intensidade do laser. Fazer isso até ver
- Ligar o condensador
    - Se as bolas agora estiverem desfocadas, o plano focar do CCD e do laser não são os mesmos - as bolas presas ficarão desfocadas
        - Verificar a posição do pinhole
    - Se as bolas estiverem focadas, aumentar a potência do laser. 
    - Mover a mesa para baixo até as bolas livres estejam focadas no CCD
    - Mover a mesa para os lados até que as bolas passem pela trap.
    - Prender algumas

#### Ver o trapping
- Se o trapping for bom, as bolas "saltam" para a trap quando estão a 1 diâmetro ou por aí da trap
    - Na lateral (XY) as bolas não devem ser movidas muito mais que 1 diametro
- Se o trapping for fraco, as bolas vão para a trap mas só brevemente
- Ao mover a mesa na vertical também devemos ver a bola a estar trapped. Este trapping será mais fraco
- Todos estes movimentos da mesa têm que ser muito suaves senão as bolas sao atiradas para fora da trap
    - Vibrações podem também fazer isso
- Se uma bola se mover para a trap e desaparecer, então só temos trapping estável em X,Y. Em Z a bola é empurrada na direção de propagação da luz
- Se parece que a trap não funciona, verificar o alinhamento todo. Ver também se há agua suficiente na lamela.

#### Calibração da trap
- Podemos calibrar a trap na direção Z ao ver a velocidade com que as bolas são projetadas
- Não percebi bem como

#### Optimizar
- Para melhorar a força da trap, é bom fazer fine tuning do alinhamento
- Os 2 fatores mais controlaveis são a posição de L3 (lente curvatura) e a distância entre L1 e L2 (telescopio)
    - L3 altera a posição da trap relativamente ao foco da CCD
    - A distãncia L12 controla o tamanho do feixe que chega à objetiva (deve ser ~o diametro da objetiva para preencher bem)
- Se uma bola estiver presa mas desfocada:
    - Mover L3 até a trap e o foco de CCD estarem no mesmo plano
    - Sempre que prendemos uma bola deve ser preciso fazer isto
    - Se formos muito brutos, é possivel que a bola deixe de estar trapped ao mover L3
- Depois de ajustar L3, ajustar L12 até ter um spot de tamanho mínimo, que dá profundidade máxima. 
    - Prender uma bola
    - medir a distância de traping?
    - ajustar L12
    - medir distancia
    - ajustar L12 na mesma direção
    - medir
    - repetir de forma a encontrar profundidade máxima


