## 1 - O que é
- Um thin film / filme fino é uma camada de material com espessura entre monolayer (espessura de 1 átomo) até 1000nm
- Pode ser usado em muitas áreas: microeletrónica, ótica, sensores, proteção contra corrosão, quase tudo que tem nanotech
- Litografia, Thin film deposition, Etching são os 3 processos mais importantes para micro e nano fabricação

### Propriedades Especiais
- Estrutura cristalina pode ser diferente de material em bulk - isto altera propriedades físicas, magnéticas e óticas
- Quase 2D
- Muito influenciado por efeitos de interface e de superfície
    - Substrato afeta thin film, mas thin film não afeta substrato

### Como são feitos
1. Temos uma fonte de partículas 
2. As partículas libertadas são transportadas até ao substrato
3. Partículas condensam/depositam no substrato

## 2 - Caraterísticas
### Carateristicas de uma técnica
- Deposition Rate
    - Uma deposição "rápida" terá 1um/min
- Energia das partículas
- Uniformidade do filme
    - Pode ser uniformidade na wafer, ou entre 2 wafers usadas
- Materiais que podem ser depositados
    - Uma certa técnica de deposição só poderá depositar alguns materiais
- Direção

### Step Coverage
![[step coverage.png]]
- Ou seja, cobertura com filme fine de algo não linear : por exemplo, podemos ter um alto ou um orifício na superfície em que estamos a depositar
- *Conformal* - uniformidade da cobertura - "conformal coverage" é quando temos uma camada sempre com a mesma espessura
- Em geral, queremos que a cobertura serja o mais "conformal" possível

- Isto é importante porque podemos ter um óxido com um orifício no centro. Queremos preencher com um metal, de modo a ter uma ligação elétrica com o que está debaixo do óxido

### Qualidade do filme
- A qualidade do filme depositado afeta:
    - propriedades elétricas - má deposição pode levar a más ligações
    - propriedades mecânicas - strain, stress e adesão
    - propriedades óticas

### Morfologia
**Amorfo**
- AKA sem estrutura cristalina. O que implica que não há defeitos cristalinos
- Comum para fazer isoladores

**Policristalino**
- Temos várias mini estruturas cristalinas, com diferentes tamanhos, organizações, ordens
- Melhor a temperatura ambiente

**Epitaxial**
- Um só cristal, feito camada a camada
- Muito bom para fazer semicondutores (??? - CHECKAR)

### Epitaxy
- Processo de crescer de forma ordenada uma camada monolayer. O crescimento e o que cresce é afetado pelo substrato abaixo
    - *Homoepitaxy* - crescimento de layer similar quimicamente ao substrato
    - *Heteroepitaxy* - crescimento de layer diferente quimicamente do substrato
- Depende da difusividade e de vários fatores externos 
![[epitaxy vs temp.png]]
#### Homoepitaxy
- Cria-se uma camada com alta superfície e com a mesma estrutura do substrato - é como se o substrato só aumentasse para cima, camada a camada

#### Heteroepitaxy
- Crescemos então uma camada, que *não* tem a mesma estrutura cristalina que o substrato.
- Como a camada nova não pode simplesmente flutuar sobre o substrato, este processo faz com que ocorra *strain* - a camada de cima tem que se apertar para encaixar
- Temos:
$$f=\frac{a_{f}-a_{s}}{a_{s}}$$
se o strain passar um certo patamar, ocorrem defeitos:
![[heteroepitaxy.png]]

- Para crescer uma camada com latices mismatched temos então que considerar um balanço de energia entre
    - *energia de strain* devido a distorção elástica do film
    - *auto-energia* de deslocação
- Em que temos
    - Thin films têm menos energia de strain (é menos custoso deformar o film)
    - Thick films têm mais energia de strain

## 3 - Processo de Crescimento
- Temos este esquema
![[deposicao passos.png]]
em que:
    - a - deposição
    - b - difusão
    - c - nucleação
    - d - attachment
    - e - detachment
    - f - difusão de edge
    - g - difusão degrau abaixo
    - h - nucleação em cima de ilhas
    - i - difusão de dimer

- Nucleação e crescimento ocorre junto das bordas de ilhas, porque temos maior energia de bonding
- Temos os *passos* de formação de film:
    1. Acomodação térmica
    2. Difusão na superfície
    3. Binding
    4. Nucleação
    5. Crescimento de ilhas
    6. Coalescência
    7. Continuação de crescimento

### Modos
![[modos deposicao.png]]
- Estes modos surgem porque 
    - Linha 1 - os átomos de film depositado têm melhor bonding com o substrato do que com outros átomos do film - gera-se uma camada fina junto do substrato
    - Linha 2 - os átomos de film depositado têm melhor bonding uns com os outros do que com o substrato - geram-se montezitos
    - Linha 3 - Estes modos ocorrem com materiais em que se começa por gerar camadas e depois geram-se ilhas nas camadas

**Crescimento de Ilhas**
![[formacao ilhas.png]]
- No caso de modos em que crescem camadas uma a uma (como Frank-van der Merwe). 
- Consoante os átomos se difundem, eles tendem a ocupar os espaços mais coordenados (AKA os espaços em que têm mais vizinhos)
- Temperaturas altas incentivam a formação de ilhas e agrupamentos de átomos
- Basicamente geram-se "ilhas". 
- Os átomos depositados têm mais atração uns para os outros do que com o substrato - eles têm maior tendência a ficar juntos do que a prender-se ao substrato 

**Tensão superficial**
- Compostos com alta energia de superfície tendem a minimizar a área superficial quando depositados - minimizar tensão superficial
![[angulo contacto.png]]

- Basicamente, a tensão superficial é o que permite interpretar quais os modos de crescimento presentes
- O ângulo numa gota é definido pela Lei de Young-Dupré:
![[angulo contacto 2.png]]
$$\gamma_{S}=\gamma_{FS}+\gamma_{F}\cos\varphi~~~~\to~~~~ \varphi=\cos^{-1}\left(\frac{\gamma_{S}-\gamma_{FS}}{\gamma_{F}}\right)$$
- No caso de crescimento Layer-by-layer teremos $\gamma_{S}\ge \gamma_{FS}+\gamma_{F}$
- No caso de crescimento com islands teremos $fa _{S}< \gamma_{FS}+\gamma_{F}$

**Casos comuns**
- Metais nobres não se ligam a Si/SiO2, então há tendência de se gerarem ilhas
- Prata forma sempre ilhas
- Ouro é melhor para fazer um film que prata 
- Uma camada de aderência de Ti ou Cr pode reduzir islands (Ti e Cr ligam-se ao O em SiO2)

### Cinemática de Crescimento
![[deposicao simulacao.png]]
- Bolas azuis escuras são átomos do substrato, bolas vermelhas são átomos do que estamos a usar para depositar, bolas azuis claras são contaminações/impurezas
- A energia dos átomos depositados depende muito do método usado
- A um átomo que pousou na superfície mas que ainda não foi incorporado chamamos de "*adatom*" (adsorved atom - adsorption é o processo de um átomo aderir a uma superfície).

**Fluxo**
- Durante o processo de deposição temos competição entre: a deposição em si a tirar o sistema do equilíbrio VS as difusões na superfície a tentar atingir o equilíbrio
- Um adatom vai-se movendo na superfície e perdendo energia cinática. 
- O fluxo de adatom pode ser descrito pela seguinte equação de difusão:
$$J=-D \frac{\partial c}{\partial x}$$
em que $J$ é o fluxo, $D$ é o coeficiente de difusão e $c$ a concentração 

- Temos ainda a *difusão de superfície*:
$$D=D_{0}e^{-E_{a}/k_{B}T}$$
em que $E_{a}$ é a energia de ativação.

- Podemos definir o *comprimento de difusão de superfície*:
$$\lambda\propto \left(\frac{D}{R}\right)^{\alpha}$$
que, claro, depende da competição entre difusão e deposição. $R$ é o rate de deposição e $\alpha$ é um fator

- Este comprimento $\lambda$ permite-nos inferir coisas sobre o tipo de estrutura que se formam:
![[formacao ilhas vs lambda.png|475]]
e podemos ainda ter:
![[formacao de roughness.png|236]]

### Nucleação
- Após um certo átomo se difundir na superfície e perder toda a energia cinática, ele estabiliza na posição de equilíbrio e incorpora o film.
- Com o tempo, os primeiros átomos depositados formam clusters/núcleos com outros átomos depositados. Eventualmente podemos ter uma rede de núcleos
- Este processo pode ser mostrado:
![[formacao ilhas grandes.png]]

- Ora, estes "núcleos" são islands claro. Por sua vez, estas também se podem mover e até juntar-se. A este processo chama-se de *coarsening*:
![[formacao ilhas tipos.png]]
é possível que muitas ilhas se vão juntando até que se tenha uma camada completa.

### Crescimento
- No entanto, podemos simplesmente ficar com ilhas grandes e imoveis. Consoante mais material é depositado, estas ilhas crescem verticalmente. A superfície fica irregular
![[formacao camadas.png]]

- A difusão é então um processo fortemente responsável pelo crescimento do film.
- Ora, a difusão é maioritariamente controlada pela *temperatura*.
- A energia de ativação aumenta diretamente com a temperatura de fusão do condensado que estamos a depositar.
- 