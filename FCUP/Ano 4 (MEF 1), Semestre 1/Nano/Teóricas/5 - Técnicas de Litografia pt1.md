## Litografia de UV extremo
- Começou-se em 2018
- Até ~13.5nm
- Mas o mínimo "normal" que temos é 193nm. Portanto isto é um salta muito elevado.
- Sempre que se muda de fonte de luz temos que ajustar o método de litografia:
![[tipos laser.png]]
- Claramente, temos que trabalhar em vácuo

### Porquê EUV? (Extreme UV)
Comparemos EUV com a técnica menor comprimento de onda a seguir a esta
**Next Excimer Laser (157nm)**
*Problemas*
- Lentes Si-O a estes comprimentos de onda absorvem.
- Assim, é preciso usar lentes de CaF2. Mas estes têm muita birrefringência e muita expansão térmica.
- Para comprimentos abaixo nenhum laser tem intensidade suficiente

**Extreme UV (13.5nm)**
*Problemas*
- Radiação EUV é muito absorvida por todos os materiais
- Nenhuma lente funciona com estes comprimentos de onda
*Vantagens!*
- Existem espelhos que funcionam a estes comprimentos de de onda e poderiam dar o resultado equivalente a lentes
- As técnicas óticas (usando espelhos) continuam a aplicar-se

Basicamente, EUV tem os mesmos problemas que Next Excimer Laser, mas os beneficios de ter comprimento de onda 1 ordem de grandeza abaixo.

### O sistema
![[euv sistema.png]]

### Fonte
- A única fonte possível destes comprimentos de onda é *plasma*.
    - Este é obtido ao aquecer um target com pulsos de laser (na ordem de ns). Atingem ~200000ºC (200k)
    - São largadas gotas do material que usamos para fazer o plasma e atingidas por um laser intenso - as gotas *são* o target.
- Consoante eletrões e iões se recombinam no plasma, são emitidos fotões de elevada frequência.
![[euv fonte.png]]

### Ótica
- Todos os materiais (sólidos, líquidos e gases) absorvem fotões com comprimento de onda de 13.5nm
- A maioria dos materiais têm refletância reduzida e índice de refração ~1 a estes comprimentos de onda
- Mas uma combinação de molybdenum e sílica tem refletância de 70%
![[reflexao euv.png]]

- Controlando a espessura e composição das camadas, podemos fazer com que a série de camadas reflita o feixe UEV. Podemos controlar o ângulo de reflexão ou controlar exatamente o comprimento de onda refletido.
- Assim, com uma série de espelho criamos um feixe exatamente o comprimento de onda e ângulo desejados.
- Com esta técnica podemos fazer espelhos grandes e bons:
![[reflexao euv imagem mciroscopio.png]]

### Masks
![[euv mask.png]]

### Resists
- É preciso que um resist usado em UEV tem que ter:
    - Alta sensibilidade (gera imagem com uma fonte fraca)
    - Alta resolução (poder obter imagens mais nítidas e minimal features melhores)
    - Out gassing reduzido - como trabalhamos em vácuo, se isto fosse elevado formavam-se bolhas

- Usamos PMMA - AKA acrílico, nos anos 60 descobriu-se que funcionava como resist
- O PMMA tem muito alta resolução MAS tem uma sensibilidade baixa (a imagem fica muito nítida, mas precisamos de um feixe forte para ele funcionar)

## Litografia Raio X
$$R = \frac{3}{2}\sqrt{\lambda(g+0.5t)}$$
- Tem comprimento de onda ainda menor: $\lambda\sim 10 \text{nm}$ até $\le 10\dot{A}$.
![[litografia xray.png]]
- A resolução é limitada pela difração de Fresnel e scattering de eletrões
- Não temos lentes, portanto não temos ampliação da imagem
- Não ocorre backscatter ou reflexões, pelo que podemos fazer iamgens com muito boa resolução, de tamanho reduzido e com paredes bem verticias.
- No entanto, é difícil obter fonte de raios-X fortes, estáveis, colimadas e de 1 só frequência

### Fonte
- Temos várias formas de arranjar uma fonte, que tem que ser muito intensa

**Plasma**
![[criacao raios x com plasma.png]]
- Produzido de forma idêntica ao que se faz em EUV, mas em que criamos um plasma mais energético para ter menor comprimento de onda
- Os raios-X são emitidos quando eletrões livres recombinam com iões ou eletrões saltam para bandas menos energéticas

**Impacto de Eletrões**
![[criacao raios x impacto de eletroes.png]]
- Eletrões são acelerados e colidem com o ânodo, libertando fotões de alta frequência
- Exige menor potência, permite maximizar emissões com range de frequências reduzido

**Synchrotron**
![[criacao raios x synchrotron.png]]
- Partículas carregadas são aceleradas de forma radial
- Permite ter muito elevadas frequências, com energias muito controladas
- Muito caro e raro, nem sempre consegue ter a intensidade necessária.

### Resists
- Precisamos que os resists tenham:
    - alta sensibilidade
    - alta resolução
- Temos então necessidades basicamente idênticas às de EUV. Usamos PMMA
- Não utilizável de forma comercial ainda - são precisas 6h de exposição.

### Masks
- Temos 1 mask e 0 lentes
- A máscara é muito difícil de fabricar, tendo vários problemas associados: frágil, defeitos facilmente ocorrem, dobras devido a expansão térmica
- As máscaras têm
    - uma camada combosta de uma mebrana fina de subestrato (Si, Si - 1-2um)
    - zonas com absorçores de raios X (Au, W)
![[mask xray.png]]
- Não é comercializável - máscaras são muito frágeis e caras. Degradam-se a cada exposição

# Técnicas Alternativas de Litografia
- Vemos que se fizermos um gráfico Resolução VS Área fabricada/hora, os vários métodos de Litografia seguem uma tendência linear:
![[metodos litogradia R x throughput.png]]
- Mas há 1 outlier: **Nanoimprint litography**. 

## Litografia de Electron Beam (E-Beam) (EBL)
- Um feixe de eletrões é emitido em direção a um PR. Claro, o feixe é muito concentrado (<5nm).
- Os padrões são *escritos diretamente* - não temos mask nem molde! Assim, claro que não temos o risco de difração que temos com litografia ótica normal.
- Ou seja: em litografia ótica normal fazemos uma wafer de uma vez, mas com pior resolução. Em E-Beam temos maior precisão mas também demora mais - fazemos 1 die de cada vez.
    - 1 wafer pode demorar horas
- Por estas razões (muito preciso mas pouco eficiente), EBeam tem 2 usos principais:
    - R&D quando é preciso chips com muito alta resolução
    - Fabrico de masks para litografia normal
![[ebeam vs lito normal.png]]
- Atualmente, EBeam é o método mais usado em contexto académico e de criação de protótipos.

- Este método é limitado por:
    - Largura do feixe - nunca conseguimos abaixo de 5nm porque não podemos apertar muitos eletrões em tão pouco espaço (eles repelem-se)
    - Óticas necessárias para concentrar o feixe
    - É preciso muita energia para ter a resolução boa
    - Forças de repulsão entre eletrões se a corrente for muito alta
    - Back-scattering dos eletrões 

### Interação E-Beam + PR/Subestrato
![[backscattering 1.png]]
- Ocorre **forward-scattering** (setas vermelhas acima): 
    - o eletrão e segue em frente ou com um ângulo reduzido
    - este é o mais comum porque os eletrões vêm com muita energia
    - muito inelástico - o eletrão perde muita energia
    - a perda de energia do eletrão faz com que seja libertado um eletrão do átomo do PR - este é o *secondary electron*
- Ou temos **back-scattering** (setas roxas acima): 
    - Menos comum. Mais problemático. Ocorre quando o eletrão colide com o núcleo
    - mais elástico e com ângulo bastante maior, emitindo um secondary electron com alta energy
    - O back scattering eventualmente faz com que o eletrão se disperse, fazendo eventualmente com que existam secondary electrons onde não é suposto. Isto é a limitação de resolução deste método.
![[backscattering 2.png]]
Ao fenómeno do feixe se espalhar chamamos de **Proximity effect**

**Soluções / Melhorias**
- Pode não parecer, mas uma forma de melhorar isto é *aumentar energia* do EBeam. Com mais energia, os eletrões penetram mais o *subestrato* e ficam menos sujeitos a ir parar à superfícies após back-scattering. 
- Pela mesma lógica do ponto acima, podemos usar um resist fino
- Outra forma é usar um subestrato com menor número atómico - menos interferências para os eletrões.
- Temos ainda outra opção, que é *reduzir a energia* - os eletrões têm pouca energia ao ponto que eles nunca chegam a sofrer back-scattering no subestrato, só no PR.
- *Basicamente*: ou fazer com que o back-scattering ocorra todo ou no PR ou no subestrato, nunca na interface.

### Resist
- Normalmente, o Resist mais usado com E-Beam é PMMA.
    - Muito barato, muito durável e fácil de manusear
    - Consiste em redes longas de polímeros, pelo que secondary electrons de baixa energia não passam
    - Permite ter alta resolução e contraste
- Mas este PR tem os defeitos:
    - Muito baixa sensibilidade, logo é muito lento a obter uma imagem
    - Baixa resistência dry etch (?)

### Scan
- Temos 2 métodos de scan (formas como o beam percorre o subestrato):
**Raster Scan**
![[ebeam raster scan.png]]
- O Beam percorre todos os pixeis, um de cada vez
- O shutter é constantemente ligado e desligado
- Bom: Fácil, repetível e ajustável
- Mau: Mais lento, mais difícil ajustar a dose previamente

**Vector Scan**
- O EBeam move-se nas direções x e y (no raster scan só move numa direção)
- Invés de mover e ir ligando e desligando o shutter, o EBeam move-se diretamente para os sítios a marcar
- Bom: Rápido, melhor para padrões mais esparsos (óbvio lol)
- Mau: O beam demora bastante a estabilizar num sítio novo, mais difícil ter placing preciso

### Electron Guns (EGuns)
- Temos 2 tipos de emissores:
**Emissor Termiónico**
- Os eletrões são expelidos da superfície ao dar-lhes energia térmica
- Usado W (tungsténio) com vácuo baico, LaB6 (Hexaboreto de lantânio) em vácuo alto
![[egun termico.png]]

- Historicamente, W é o emissor mais usado
- Os eletrões são emitidos porque a temperaturas elevadas eles têm energia térmica suficiente para ultrapassar a função de trabalho ($\phi$)
    - Temos $k_{B}T\ll \phi$ e $\phi\sim4\text{eV}$. Temos $k_{B}=8.6\cdot10^{-5} \text{eV K}^{-1}$ logo precisamos de temperaturas na ordem de $10^{5}\text{ K}$.
- Este método é barato, não necessita de vácuo muito alto (para tungsténio) e o filamento dura dezenas de horas

**Emissores de Campo**
- Aplicamos um campo elétrico forte num sólido (normalmente filamento de  W)
![[egun field.png]]     ![[egun field 2.png]]
- A ponta precisa de ser muito fina (~100nm) e precisa de estar sempre muito limpa
- A emissão de eletrões torna-se dominante para $E\sim10^{8}\text{V/cm}$
- A corrente emitida descreve um perfil não linear
- É preciso muito pouco tempo para que começe a emissão
- A largura do feixe emitido é muito reduzida
- É preciso vácuo muito alto ($10^{-10}\text{ Torr}$)

**Comparação**
![[egun data.png]]

## Litografia Ion-Beam (IBeam)
- Consiste no mesmo que EBeam mas com iões. Isto trás as seguinte diferenças:
    - O feixe penetra menos, não ocorre proximity effect
    - Como os eletrões têm mais massa, são mais lentos mas com mais momento
- Comparemos 2 casos:
![[fib vs ebeam.png]]

- Assim, IBeam é parecido a EBeam, mas com mais capacidades
    - Como EBeam, podemos escrever um padrão num PR
    - Pode ser usado em top-down (etching) ou bottom-up (deposição)
    - Pode ser usado para implantar iões e modificar materiais
    - Podemos visualizar o processo em tempo real usando SEM

- *Vantagens*
    - O proximity effect é desprezável, não se geram eletrões secundários
- *Problemas*
    - Baixo throughput
    - Mais difícil focar o IBeam
    - A baixa penetração pode ser uma desvantagem, pelo que obriga a ter um PR muito fino (<100nm para 100keV)
    - Podemos implantar o ião no resist

### Sistema IRL
![[fib sistema.png]]

### Fontes de iões
![[fib fonte.png]]
- Temos um crucible com alloys de metal derretidos
- Uma ponta de W liga-se ao crucibel e o metal líquido escorre nas beiras do W, descendo até à ponta, que é um *cone de Taylor*
- O cone de Taylor é uma estrutura formada pelo metal líquido a escorrer. Devido à tensão superfícial e campo elétrico, a ponta é muito estreita (~2nm)
    - O campo elétrico é induzido pelas power lines (e o tungsténio?)
- O campo elétrico na ponta do cone de taylor é muito alto ($>10^{8}\text{V/cm}$) e permite acelerar os iões 1-keV

- Normalmente usamos uma fonte de Ga+ (gálio), que:
    - funde a 30ºC (temperatura ambiente)
    - tem baixa pressão de vapor (em vácuo gera poucas bolhas)
    - a fonte dura ~1500h
    - tem Z=31 e então é um eletrão "pesado", o que é útil para sputtering

### Litografia FIB (Focused Ion Beam)
![[fib usos.png]]
#### FIB milling
- Possível fazer estruturas sem PR
- O rate de sputtering depende de 
    - átomo do material target
    - ião usado e a sua energia
    - ângulo de incidência
    - orientação dos cristais
- Obtemos features mínimas *maiores* que o beam: beam de 10nm gera features de 20-30nm
- Lento : $1\mu \text{m}^{3}\text{/s}$ com um feixo de 1nA
![[fib sputtering.png]]
- Vemos que ocorre implantação: alguns iões ficam a fazer parte do subestrato.

##### Re - Deposição
- Depende de
    - energia dos átomos que saem da superfície
    - coeficiente de sticking do target
    - rendimento de sputtering do target
    - feometria da feature a ser milled
- Como o nome indica, isto é algo *negativo*: após milling/sputtering, é possível as partículas que foram projetadas "voltarem para trás".
- Como podemos minimizar:
    - Começar por fazer milling de padrõe grandes e menos críticos, com corrente alta
    - Passar o IBeam múltiplas vezes
    - Alternativamente, fazer milling de padrões pequenos e críticos com corrente baixa primeiro, repetindo várias vezes

### Implantação com FIB
![[fib implantacao.png]]

### Litografia FIB com gás
- Ao introduzir um gás:
    - obtemos etching mais forte
    - etching seletivo é mais eficaz e preciso
    - fazemos deposição mais eficiente
- O gás é introduzido com agulhas próximas da superfície, a 50-150um. O gás está a $\sim10^{-5}\text{ Torr}$
![[fib com gas.png]]

- As figuras abaixo mostram porque o gás ajuda em etching (impede re-deposição) e em deposição (fornece o material a depositar):
![[fib com gas como funciona.png]]

- Temos abaixo os fatores de aumento de yield de sputtering com vários gases:
![[fib com gas beneficos data.png]]

