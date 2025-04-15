## iso-DISTORT
- Utiliza software do suite Isotropy. Tem distorções fisicas (deslocamento, ordenamento de átomos, momentos magnéticos, momentos de rotação, strain) em transições de fase geradas por representações irredutíveis
- Inclui:
    - ferramentas de visualização de distorções em 3D e os seus padrões de difração
    - descrição detalhada de cada modo de simetria da estrutura pai que contribuem para a distorcida
    - variedade de formatos de output
    - lista de dominios equivalentes da est distorcida
    - representação irredutível da matriz que representa a distorção
    - ficheiros das estruturas na árvore entre as ests parent e child

> [!warning]
> SG - space group
> IR - representação irredutível

**Intro**
- Estrutura cristalina sofre distorção e reduz simetria. Mas nisso, *nem todos* os elementos de simetria são perdidos. Aqueles que ficam formam a simetria do SG da superestrutura e estão num subgrupo da estrutura pai (original, com maior simetria)
    - Esses subgrupos podem ser referidos como "subgrupo de isotropia" da est pai ou "simetria de distorção" da simetria pai
- ISODISTORT permite prever/determinar os tipos de distorção e simetrias que podem originar de uma estrutura pai

**Mudança de base**
- Podemos ver os parametros de rede, coordenadas xyz dos átomos, ocupação e momentos magnéticos como uma base
- Podemos ainda ver os graus de liberdade de uma distorção que causa alterações estruturais como vetor base de um *espaço de distorção* generalizado
- O ISODISTORT gera novos vetores base em torno da simetria, que descrevem o espaço de distorções. Estes não passam de combos lineares de vetores base da est pai. 
- Em geral, o ISODISTORT dá uma matriz quadrada que tranforma a est pai na estrutura distorcida, através de uma mudança de base. Os parâmetros da nova base irão descrever coisas fisicamente significantes e que estão relacionadas com a transição em si.

**1º e 2º ordem**
- Uma IR primaria consegue passar para a est distorcida de uma só vez (a IR sozinha faz tudo). Se duas IR têm que ser combinadas para obter a estrutura distorcida, temos IRs primaris superposed
- IRs secundarios são calculados pelo ISODISTORT e gera parametros de 2a ordem

### Search
- Depois de colocar o CIF
- Selecionar tipos de distorções a procurar
**All special K-Points**
- "Special KPoints" são pontos do espaço reciproco em que não há variação de parâmetros
- Os IRs associados a estes pontos e às distorções desejadas já estão pré-calculados e estão numa base de dados
- Método deve ser suficiente para casos simples
- Dá lista de subgrupos de isotropia e os K-points associados, IRs e parametros

**Método geral**
- Escolher 1 ponto K da ZB1
    - Isso aparece no dropdown na notação de 2 livros e nas coordenadas dos vetores base
- Especificar a,b,c quando necessário em que metemos '1/2' invés de '0.5'
- Podemos estudar o caso de *IRs sobrepostos*: metemos um certo número e depois indicamos o K-point de cada um desses passos

**K pontos arbitrários**
- Procura todas as simetrias de distorção do SG indicado pelo utilizador

**Decompor est distorcida**
- Bom para comparar estruturas que experimentalmente conhecemos.
- Decompõe a estrutura nos modos de simetria da estrutura pai
- Damos cif da estrutura distorcida
*Base*
- Escrever a base dist em função da base pai
- Tipos de átomos têm de bater certo, claro
- Outra opção é selecionar das opções do dropdown
- Muito importante
- Penso que temos que associar de forma que as orientações estejam corretas
*Origem*
- Se há shift e o conhecemos, especificar pode facilitar/acelerar o estudo
*Atom matching*
- Para decompor, é preciso associar os átomos das 2 estruturas
- Método 'nearest-site' associa diretamente os mais próximos de cada est
- 'Robust' vê todas as possibilidades

##  iso-SUBGROUP
- Usa as matrizes no iso-IR
- Inserimos o SG da est pai. Podemos inserir um número de IRs a sobrepor
**K vector**
- Escolher 1 ponto na ZB1
- Colocar ponto e colocar parametros como *racionais*! (4.071 = 4071/1000)
**IR**
- Para cada K-point irá aparecer um dropdown com as IRs associadas
- Para cada uma temos a notação de Miller/Love e de Kovalev
**Tabela**
- Gera uma tabela com OPD, subgrupo, base, origem, etc de cada IR
- Calculado em tempo real. Pode demorar
