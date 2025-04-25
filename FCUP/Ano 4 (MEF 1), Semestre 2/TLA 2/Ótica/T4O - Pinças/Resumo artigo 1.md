    ## Micromanipulação ótica

### Intro
- Usando microscopia e lasers é possível manipular e estudar células, proteínas e outras moleculas bioquimicas.
- Normalmente, luz é usada apenas para visualizar coisas, como em microscopia.
- Mas pode ser usada para mover, segurar, guiar e exercer força em objetos microscopicos
- Há 100+ anos foi demonstrado que a luz consegue exercer força em objetos.
    - Atualmente entendemos que isto resulta da dualidade partícula-onda, em que os fotões colidem com os objetos e tranferem momento, gerando uma força na ordem de pN
- Em 1970, os primeiros resultados experimentais deste tipo de sistema. Com um feixe pouco focado, as partículas moveram-se ao longo do eixo do feixe e especialmente no centro do feixe.
- Depois viu-se que 2 feixes a propagar em direções opostas conseguem prender uma partícula com sucesso.
- Depois desenvoveu-se um sistema com 1 só feixe com armadilha de gradiente - **pinças óticas**. 
- Este artigo:
    - explica o fenomeno fiisico e o funciona
    - aplicacoes
    - sistemas que permitem fazer isto

### Como funciona?
- O processo todo é explicada pela interação luz-matéria
- Podemos ver abaixo as dinâmicas de uma particula *10x* maior que o comprimento de onda da luz do laser. 
    - Isto é o **regime de Mie**
![[Pasted image 20250422225709.png|450]]
- Temos que
    - Scattering e reflexão de luz gera uma força na direção de propagação
    - Refração da luz resulta numa força que arrasta a partícula para a região de maior intensidade luminosa (assumindo que a particula tem maior $n$ que a vizinhança)
- No regime de Mie, para determinar forças podemos meramente usar equações geométricas. 
- Ao fazer entrapmente, devemos escolher a fonte de luz de forma que a partícula não absorva luz!
- Podemos então imaginar a particula como sendo um espelho circular  etemos os raios mostrados acima.
    - A) O feixe mais intenso (centro do feixe) e o feixe fraco (esquerda) atravessam a particula da mesma forma. O feixe mais forte tem mais fotões então "empurra mais" a particula, levando-a para o centro. Esta transferência de momento ocorre porque os feixes são refratados na particula
    - B) Os feixes passam na particula de forma simétrica.  Ainda assim, as setinhas claras mostram que cada feixe aplica uma força. Isto resulta numa força a levar a partícula para o centro
    - C) Aqui vemos outro fenomeno que pode ocorrer. Podemos ter feixes a serem refletidos na particula. Ora, esses irão gerar uma força na direção de propagação
    - D) Aqui temos uma particula de Rayleigh (tamanho 10x menor que o comprimento de onda da luz). Para estas, o que importa é a sua polarizabilidade e não a transparência. A luz gera um campo E na particula e este exerce força para o centro. 
- Isto tudo reforça que o **gradiente** de intensidade luminosa regula a interação.
- Conforme em D), no *regime de Rayleigh* é mais útil pensar nas partículas com dipolos elétricos
- Apesar das figuras e cenas, entrapmente é normalmente feito no regime Lorentz-Mie - partículas aproximadamente do tamanho do comprimento de onda

*Configuração*
- Acima foi referida a existência de sistemas com 2 feixes opostos. Esse sim usa feixes mal focados
- As pinças óticas usam lentes com alta NA e precisam de feixes altamente focados. 
    - A alta NA garante entrapment no espaço 3D, paraxial e lateral.
- Para ter esta boa focagem, é preciso que a fonte tenha uma alta coerencia espacial 
![[Pasted image 20250422231749.png]]
- Coerencia temporal é muito menos importante. Podemos usar um laser fentosegundo e assim não temos o problema de coerencia
- A maioria das pinças usa uma fonte de ondas contínuas monocromáticas. 

### Setup de uma pinça
- Este artigo não foca especificamente no processo de focagem
- Veremos uma configuração usada para entrapment
![[Pasted image 20250422232841.png|500]]
- Para formar um ponto de foco no plano focal, uma lente de microscópio com magnificação elevada e com NA alto é uma boa escolha. No entanto, lentes de microscópio modernas consisteme em várias lentes juntas e formam uma imagem no infinito. 
    - Assim, usamos uma lente tubo para formar uma imagem na camara ou detetor usado
    - Este tipo de lente-no-infinito-corrigida não afeta as propriedades da pinça
- Neste sistema são usados espelhos dielétricos de alta qualidade, lentes com coating anti-reflexão. Isto é feito para minimizar perdas.

*Mover a pinça*
- Ao pinçar precisamos de mover/rodar o feixe. Mas temos de ter o cuidado de garantir que a pinça não passa para fora da amostra ou garantir que ele não se move tanto que falha um dos elementos óticos do sistema.
- Esse processo de mover a pinça pode ser feito com o conceito de conjugados óticos
    - Projetamos a back aperture (feixe à entrda) da lente microscopio num espelho. Isso é visível acima, vemos que o feixe que sai do *steering mirror* passa num espelho antes de chegar à lente. É nesse espelho abaixo da lente que podemos ver o feixe.
    - Se vermos o feixe a mover na lateral no espelho, então a ponta também irá faser isso
    - Conjugados óticos é o que criamos com as 2 lentes entre estes espelhos. Estas podem fazer efeito telescópico, que ajuda a melhor preencher a lente microscopio - isso dá um ponto mais focado.

*Dimensões*
- Devido a esta configuração e às dimensões e distâncias dos componentes, apenas podemos prender amostras de alguns microns.
- A amostra usada neste artigo consiste em 2 tiras finas com <100um de espessura. Foram ainda colocadas particulas coloidais em 10muL de agua, e tudo foi colocado na amostra.

### Considerações teóricas de traps
- De modo geral, esta área apoia-se em calibração experimental invés de forte conhecimento e previsão teórica
- Consideremos 1 partícula presa numa pinça
- O tamanho da partícula $a$ em comparação com o comprimento de onda $\lambda$ fortemente afeta como modelamos o sistema
    - Se $a\ll\lambda$ temos o regime de Rayleigh, devemos considerar a partícula como um dipolo elétrico a tentar minimizar a sua energia no campo do feixe de luz
    - Se $a\simeq\lambda$ temos regime de Loretnz-Mie e se $a\gg\lambda$ temos regime de Mie. Nestes casos podemos considerar forças da forma que vimos acima.
- Surgem problemas ao considerar a descrição exata do feixe ótico perto do foco de um sistema ótico com alto NA. Neste caso, não podemos aproximar o sistema a paraxial. 
    - Assim, para determinar os campos E,H transversos e longitudinais precisamos de considerar termos mais complexos (senão as eqs de Maxwell não são cumpridas)
    - Além disso, a difração e polarização na luz na zona do foco têm de ser consideradas.
- Com isto tudo, torna-se necessário estudar tudo com eletromagnetismo rigoroso - não chega simplesmente analisar a intensidade da luz. 
- Usamos então o formalismo de Lorentz-Mie, que explica o scattering da luz nestes casos de forma teórica

**Como temos controlo tão exato**
- Podemos então pensar: o ponto focal na amostra estará sempre limitado pela difração da luz na saída da lente microscopio: $\sim\lambda$
- Assim, como podemos controlar amostras/moleculas/particulas com dimensões de apenas algunas nanometros? 
- Para entender isto, basta olhar para como se comporta uma partícula presa na pinça. Ela comporta-se como se estivesse num **sistema harmónico 2D** - ela é puxada para o centro com uma força proporcional ao deslocamento.
- Temos uma massa presa $m$ num meio com damping $\gamma_{0}$ a uma temperatura $T$. A equação de Einstein–Ornstein–Uhlenbeck para teoria de movimento Browniano (= movimento aleatório de particulas livres num meio) temos a seguinte equação de Langevin:
$$m \frac{d^{2}x}{dt^{2}}+\gamma_{0} \frac{dx}{dt}+\kappa x= \sqrt{2k_{B}T \gamma_{0}}~\eta(t)$$
em que $\kappa$ descreve a rigidez da pinça/trap.
- O termo da direita na prática comporta-se como ruído gaussiano aleatório e representa as forças brownianas.
- No caso de amostras biológicas, temos sempre um meio aquático. Isto significa que temos um cenário de sobre-amortecimento. Assim, as partículas oscilam com frequências muito menores que no vácuo
- Assim, com as partículas mais estáveis e num meio mais viscoso, elas ficam ainda mais presas no centro da pinça. E assim se consegue resoluções melhores ainda que $\lambda$

### Estudos de 1 só molécula
- A criação de pinças óticas permitiu entender o funcionamento e comportamento de moléculas/proteínas e cenas biológicas de uma forma nunca antes conseguida
- Outra capacidade importante é a de a pinça prender um material/molecula/amostra, e essa por sua vez faz de anchor para outra substância que realmente queremos estudar.
---- segue-se uma data de dados e notas sobre coisas de biologia

### Shaping do feixe
- Mais recentemente (o artigo é de 2007 btw), tem-se vindo a fazer shaping do feixe de luz da pinça
- Tradicionalmente, usamos uma lente de microscopio e um feixe gaussiano normais. Isto resulta numa região de trap elipsoidal - o eixo maior da elipse encontra-se na direção de propagação.
    - Isto significa que é difícil controlar o potencial e forças aplicadas numa amostra em 3D
- Por exemplo, um feixe anelar (sem luz no centro) reduz o efeito de back-scattering é mais facil centrar uma amostra em posição paraxial
- Alías, se a frente de onda for mesmo bem controlada, será possível criar arrays de zonas de trap
- Nomeadamente, criou-se já vários sistemas em que temos 2 traps numa pinça. Isso é especialmente útil em quimica/biologia - isto permite prender 2 extremidades de uma proteina e assim analisa-la com muito controlo
    - Para atingir isto, usamos uma configuração estilo inferometro e um dispositivo acustico para "dividir" a luz. Pelo que percebi, isto faz a luz alternar entre as 2 traps. Se alternar rapido o suficiente, temos "2 pinças"

### Novidades (artigo de 2007 btw)
- Feixes Laguerre-Gaussianos são um tipo de luz com frente de onda controlada que permitem fazer coisas novas. 
    - Isto melhora o trapping paraxial (o centro é escuro)
    - Este tipo de feixe tem polarização espiral a rodar. Isto por sua vez cosnegue transferir momento angular de spin para particulas e assim *conseguimos rodá-las, enquanto presas*
- Outra novidade são feixes de Bessel que, teoricamente, são imunes a difração
    - Este tipo de fixe tem um centro muito estreito que é mantido ao propagar por longas distâncias
    - Com este tipo de feixe conseguimos prender várias partículas *no eixo de propagação*