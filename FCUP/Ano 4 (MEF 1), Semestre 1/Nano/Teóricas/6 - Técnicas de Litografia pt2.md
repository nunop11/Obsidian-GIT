## Nanoimprint Litography (NIL)
- Temos uma boa resolução com uma muito alta throughput
- Isto é o único outlier do gráfico "resolução X throughput", tendo melhor resolução do que esperado para o seu throughput.
- De forma muito simples, consiste em imprimir os padrões desejados num subestrato ao "estampar"
    - Comparável a uma máquina de waffles ou a uma impressora de Gutenberg
- Isto é o caso dos CDs: temos pequenas marcas feitas no plástico com um molde.
- Quando falamos de litografia, podemos usar o molde para imprimir (imprint) e depois usamos ion beam para "limpar" a impressão.
- Tem uma data de problemas, mas mal eles são resolvidos conseguimos fazer padrões com muito alta resolução com alto througput de forma barata.

### Comparação
![[nil tipos comparacao.png]]

### NIL térmico
![[nil termico.png]]
- Bom para fazer 1 camada só, porque é um processo simples. Mas para 2+ camadas não é boa ideia, é muito difícil alinhar camadas distintas.
- O método parece pior que UV em tudo, mas é um método simples e versátil, funcionando com muitos materiais diferentes. Basicamente usado em tudo o que tenha uma só camada
- Pressão e temperatura:
![[t nil grafico tempo.png]]
    1. Subimos a temperatura para aumentar a maleabilidade do subestrato
    2. Quando a maleabilidade for boa que chegue, aumentar a pressão para imprimir
    3. Baixar pressão, baixar temperatura
- A temperatura normal é 100-200ºC, a pressão normal é 20-50 bar

#### Resist
- boa adesão ao subestrato, com espessura uniforme em todo o subestrato
- deve transferir o padrão de forma consistente e precisa, sem se apegar ao molde
- baixa pressão necessária para imprinting funcionar
- baixa viscosidade durante imprinting
- deve manter estabilidade térmica durante os vários processos
- resistência a etching de plasma
- resistência mecânica

### NIL curado com UV
![[nil curado uv.png]]
- Pode ser feito a temperatura ambiente e pressão reduzida (~bar)
- O "curado com UV" significa que o resist torna-se sólido quando exposto a radiação UV
    - Isto implica que o molde ou o subestrato tem que ser transparente a UV
    - Quase qualquer material que endurece quando sujeito a UV serve como resist
- O alinhamento é mais fácil que em NIL térmico

- O pó é um problema mais forte aqui
    - O resist líquido "apanha" pó e este n pode ser soprado
    - No entanto, por a pressão ser menor, a área que uma partícula de pó não é muito maior que esta (mais ou menos como em litografia ótica)

#### Adesão Molde - polímero UV - substrato
![[interface nil.png]]
- Idealmente,
    - o polímero e o molde não aderem
    - o substrato e o polímero aderem muito bem

### Problemas de NIL
- *Área grande* 
    - Temos uma grande área que tem que ter toda uma pressão uniforme
    - Para ajudar com isto, colocamos o sistema molde+subestrato rodeado de uma alta pressão
- *Limpar molde* - o molde tem que estar sempre limpo
- *Coisas grandes e pequenas* - se houverem coisas de vários tamanhos, teremos irregularidade na força que precisamos de aplicar
- *Ar preso* - pode ficar ar preso e gerar defeitos. Para isto usamos vácuo

### Moldes
- Para garantir que o mold e subestrato estão bem encaixados e justos, usamos alta pressão em toda a volta:
![[nil pressao.png]]
- Historicamente, usa-se Si, quartz ou Ni
- Cada vez se usam moldes de polímeros, flexiveis
- Idealmente temos:
    - baixa expansão térmica
    - fabrico sem defeitos, ou com defeitos que podemos corrigir 
    - resistência/durabilidade química e mecânica
- Para garantir que uma parte do subestrato não "volta" com o molde, usamos uma camada *anti-sticking* -- Muito importante!

#### PDMS
- Este é um material transparente e flexível. Podemos fazer moldes flexíveis com ele, o que é útil para superfícies curvas
- Não é tão útil para altas resoluções (<100nm), porque é preciso muita pressão e o PDMS não é rígido o suficiente e deforma-se

### Camada de PR / Camada residual
![[nil altura resist.png]]
- A camada de PR que temos depois o NIL nas zonas baixas (zonas para remover) não pode ser
    - muito baixa - as zonas altas poderão não ficar completamente preenchidas, aumenta desgaste do molde
    - muito alta - tornará o etching mais difícil, iremos remover PR daz zonas altas e das suas laterais, dificulta a transferência de padrões

#### Calcular altura inicial adequada
![[nil pr movimento.png]]
- O polímero não é compressível, então tem que haver conservação de volume.
    - Como vemos acima, $h_{0}$ muito elevado leva a $h_{f}$ muito elevado, o que dificulta a transferência do padrão
    - Se $h_{0}$ for muito baixo, $h_{f}$ será ~0 e teremos maior desgaste e danificação do molde.
- Temos:
$$\begin{align*}
h_{0}\sum\limits_{i=1}^{N}(s_{i}+w_{i})&= h_{f} \sum\limits_{i=1}^{N}(s_{i}+w_{i}) + h_{r}\sum\limits_{i=1}^{N}w_{i}\\
h_{0}&= h_{f}+\frac{h_{r}\sum\limits_{i=1}^{N}w_{i}}{\sum\limits_{i=1}^{N}(s_{i}+w_{i})}
\end{align*}$$
- A esta camada final de dimensões $h_{f},h_{r}$ chamamos de *camada residual*.

### Contaminações
- Em litografia ótica, contaminações são más - geram defeitos do tamanho da contaminação (um partícula com 1 um gera um defeito com 1 um)
- Em NIL, contaminações são ainda piores - a partícula causa uma ligeira deformação do molde, o que causa um defeito num raio em torno da contaminação
    - Aqui temos principalmente o pó
- Pode ainda acontecer termos uma contaminação *debaixo* do substrato. Consoante estes são pressionados, a wafer pode estalar ou deformar.
    - Para reduzir isto, a combinação molde+wafer é envolvida em algo mole, como papel ou plástico

### Imprinting 3D
- Usando moldes mais complexos e espessos, podemos fazer imprints 3D:
![[nil foto.png]]

### Aplicações
**Armazenamento de dados**
- DVD
- Discos magnéticos
- CD

**Bio médico**
- Chips de eletroforese de ADN

**Displays**
- Cristais Líquidos
- Polarizador e difusor

**Optoeletrónica**
- Cristais fotónicos
- Guias de onda - componentes óticos com dimensões menores que o comprimento de onda

**Nano eletrónica**
- Transístor de 1 eletrão
- Eletrónica molecular

## SPM - Scanning Probe Microscopy 
- Tem a melhor precisão possível - manipular átomo a átomo, mas tem muito baixo throughput
- Dentro desta categoria temos muitas técnicas:
    - STM - Scanning Tunneling Microscopy
    - AFM - Atomic Force Microscopy
    - LFM - Lateral Force Microscopy
    - ...

### STM - Scanning Tunneling Microscopy
![[stm.png]]
- Este método baseia-se em quantum tunelling:
    - Se tivermos 2 elétrodos metálicos e através deles for aplicada uma tensão, então surge uma corrente de tunelling entre os elétrodos (mesmo que o meio entre eles seja isolador)
- Se recordarmos física moderna, temos:
![[tunneling.png]]

- O processo de microscopia corresponde a isto:
![[stm zoom.png]]
a ponta move-se nas direções x,y,z e deteta o que tem por baixo medindo a corrente.
- Daqui também conseguimos entender porquê que temos precisão de 1 átomo.

## Scanning Proble Litography
Vejamos alguns tipos

### Resist Exposure
![[spl.png]]
- Aqui, a ponta atua como uma fonte de eletrões e assim expõe o resist (como EBeam)
- Isto pode ser feito com STM e AFM
- A resolução é de 20-40nm, sendo limitada por o beam divergir (porque não temos lentes para o concentrar)

### Oxidação
![[spl 2.png]]
- Aplicamos voltagem entre o sample e a ponta (~5-10V)
- O campo criado causa oxidação da sílica ou metais do substrato
    - Além disso, ioniza moléculas de água no ar, que originam iões OH- que atuam com oxidante.
- Podemos usar STM ou AFM
- Isto permite então fazer linhas de óxido (por exemplo, uma linha de SiO2)

### Manipulação Atómica
- Apesar do título, podemos manipular átomos soltos ou moléculas.
- Alterando o sinal da tensão aplicada entre a ponta e o substrato, podemos depositar ou remover átomos
![[manipulacao atomica.png]]
- Isto permite ter a melhor resolução fisicamente possível

#### com STM
![[stm 2.png]]
- Aplicamos tensão entre ponta e substrato
- Eventualmente, a força lateral aplicada nos átomos excede a barreira de potencial necessária para o átomo saltar em direção ao centro da ponta, onde temos campo máximo.
- Para moléculas, usando um campo mais forte podemos polarizá-las e fazê-las saltar em direção à ponta.
- Usando STM, já foram feitas muitas imagens bonitas.

#### com AFM
- Consiste mais em "empurrar" as estruturas:
![[afm.png]]

### Nanofabricação com AFM
#### Nanoindentação
- Removemos material do substrato, deixando trenches com a mesma forma da ponta.
- Permite ter muita precisão de alignment
- Não são precisos alguns dos passos "tradicionais", como etching - cortamos diretamente o substrato
- Este processo é "dirty" - deixa debris na wafer
- A ponta de AFM desgasta-se mais rápido
![[afm foto.png]]

#### Scratching
- Exatametne o que o nome indica
- Tem caraterísticas semelhantes a nanoindentação
- Abaixo vemos o debris deixado:
![[afm restos.png]]

### Millipede
- Inspirado numa centopeia, como o nome indica
- Temos pontas independentes que contactam com um polímero
    - As pontas são aquecidas com uma resistência no contacto (aquecendo até ~400ºC). O calor enfraquece o polímero e deixa uma marca da ponta.
- Para ler o que foi escrito, usamos a resistência a ~300ºC. A ponta desce quando passa numa indentação
- Uma vantagem é que podemos ter muitas pontas num só instrumento, e cada uma pode ser controlada independentemente.
    - Numa experiência usou-se 1024 pontas. Mas isto necessita de demasiada energia/potência

### Dip Pen Nanolitography
![[dip pen.png]]
- Baseado em AFM
- A ponta de AFM está coated com uma "tinta" e é assim usada para "escrever" na superfície.
- Esta técnica, apesar de parecer simples, é compatível com materiais duros e moles em escalas até inferiores a 100nm.
- Útil em coisas químicas e bio - é a única técnica que usa líquidos.
    - Pode até depositar coisas biológicas : ADN, biomoléculas
- Funciona a temperatura ambiente (depende das condições e materiais específicos)
- É possível atingir escalas de 15nm, mas é preciso condições muito específicas
- A ponta pode ser feita com FIB

- Mas este método tem problemas:
    - muito, muito lento
    - as tintas e substratos nem sempre "combinam" - isto gera limitações
    - a superfície tem que ser muito suave/lisa
    - é impossível "desligar" a ponta - apenas a levantamos e pode ou não cair moléculas ao fazer isto

- Mas também existem evoluções futuras deste método:
    - criar arrays paralelos (wtv that means)
    - controlar independentemente cada ponta
    - fazer arrays mais complexos a alta velocidade

# EXTRA
- No PPT tem ainda:
    - Template Base Litography
        - Nanoporous Alumina Templates
    - Soft Litography
        - Micro contact printing