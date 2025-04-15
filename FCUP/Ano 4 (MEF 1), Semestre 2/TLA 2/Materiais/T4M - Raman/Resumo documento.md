## O que diz esp Raman?
- Vejamos algumas aplicações
### Identificar materiais desconhecidos
- Cada material terá um espetro único de Raman, para os quais temos uma base de dados / biblioteca
- Quanta maior a resolução do espetro obtido, melhor a especificidade química

### Distinguir materiais pela estrutura
- Com alta resolução, conseguimos distinguir estruturas muito semelhantes (mesmo estruturas com os mesmos componentes químicos)

### Investigar propriedades estruturais
![[raman espetro.png]]
- Ao analisar a variação da altura, largura e posição dos picos de Raman, podemos determinar coisas como:
    - quantidade de material
    - cristalinidade
    - se ele está em compressão ou tensão
    - temperatura do material
    - espessura da camada analisada
- Isto porque o espetro de Raman contém informação sobre vibrações de moléculas e latices. Assim, as vibrações são influenciadas pelas grandezas explicadas acima de forma muito direta e clara.

## O que nos dizem imagens de Raman
- Os dados de espetroscopia de Raman pode ser mostrado em arrays de pontos. Estes podem ser representados como perfis 1D, imagens 2D ou volumes 3D

### Análise espacial
- Podemos determinar
    - Se um material/composto está presente
    - Se algum material desconhecido está presente
    - A distribuição de materiais
    - Tamanho e forma de partículas ou regiões
    - Quantidades relativas de materiais
    - Variações de propriedades estruturais dentro da amostra
    - Espessura e composição da camada

### Quantificação de composição e props estruturais
- O brilho, contraste e cor da imagem podem mostrar informação importante.
- Ao sobrepor imagens, podemos mostrar informação de diferentes propriedades ou parâmetros ao mesmo tempo

## Porquê esp Raman?
### Vantagens
1. Obtemos informação sobre composição química e propriedades estruturais
2. Muitas aplicações - todos os não-metais têm espetro de Raman. Até metais têm espetro
3. Pouca preparação da amostra necessária - basta ter uma lente a iluminar a amostra
4. Podemos diferenciar tecidos ou células sem indicadores ou tintas
5. Análise sem contacto e sem danificar amostra
6. Um bom instrumento consegue obter um espetro de quantidade <1um de amostra
7. Opostamente, podemos analisar grandes quantidades
8. A análise pode ser feita através de containers transparentes
9. Podemos analisar amostras em água/soluções aquosas

- Além disto, Raman pode ser combinado com outras técnicas.

## Problemas
1. Raman é um efeito fraco - é preciso sensores mutio precisos e designs óticos muito eficientes
2. Fluorescencia de fundo da aomstra pode obstruir dados de Raman - pode ser minimizado usando multiplos lasers
3. A superficie da amostra pode não ser plana - tecnologia mais recente tem vindo a resolver isto
4. Lasers muito fortes podem danificar amostras - o objetivo é tentar maximizar o output de Raman com a menor potência de laser possível
5. No caso de usar um container, ele pode afetar o espetro - usar um instrumento com alto NA e num baixo volume de sampling reduz este efeito.
6. Efeito de background de lamelas de vidro pode afetar dados Raman - Podemos usar lamelas de aço inox, aço inox polido ou quartzo
7. Efeitos de raios cosmicos - se um raio cosmico incidir no detetor durante a coleta de dados, teremos um pico intenso. Existe software que remove estes picos automaticamente

## Partes do espectrometro
![[raman maquina.png]]
- O efeito de Raman é muito, apenas 1 parte em 10M da luz scattered tem shift.
- Temos acima o modelo "Renishaw's inVia Raman microscopes" tem:
    - Um ou vários lasers que podem ir de UV para IR, que têm *óticas motorizadas*. O comprimento de onda dos lasers é mudado no software
    - *Lentes objetivas* para focar a luz na amostra, com foco 100x. Funciona até com otica de imersão
    - *Lentes de espectrometro motorizadas* que automaticamente se optimizam para cada comprimento de onda
    - *Filtros de Rayleigh* que separam a luz refletida e a luz scattered, de modo que apenas a luz de Raman é vista pelo espectrometro
    - *Grating de difração* com alta dispersão para separar a luz scattered nos seus comprimentos de onda
    - Um *sensor CCD* arrefecido de forma termo elétrica
    - Um PC para recolher dados, análise e controlo do sistema

## Efeito Raman
- Espetroscopia consiste em analisar a interação da luz com os materiais, vendo a luz que é refletida ou scattered. Este comportamento varia com o material em si e com o comprimento de onda da luz usada
![[propagacao luz material.png]]
- Na espetroscopia de Raman observamos a luz scattered de forma inelástica.

![[raman tipos e rayleigh.png]]
- Quando há perda de energia temos scattering de Stokes
- Quando há ganho de energia temos scattering anti-Stokes
- Na prática, raramente se usa luz anti-Stokes porque dá-nos dados com menos energia de Raman.

### Shift de Raman
- Isto consiste na variação de energia de um átomo em vibração, após excitado por uma fonte de luz
- Quando temos ligações mais *fortes* entre átomos *leves*, teremos maior frequência de vibração e portanto um maior shift
    - Contrariamente, se temos átomos *pesados* com ligações *fracas*, teremos menor shift

## Explicação de Bandas de Raman
### Espetro VS estrutura
- Todos os materiais têm espetros de Raman *exceto metais puros*
- O espetro de Raman é representado como a intensidade da luz scattered (YY) vs Variação de energia da luz (XX)
    - As energias metidas nos XX normalmente são indicadas relativamente à energia do laser utilizado. Isto porque, claro, queremos estudar o *shift* de Raman. Ou seja, normalmente legendamos o eixo XX como 'Raman shift (cm-1)'

**Complexidade**
- Quando temos um material puro com estrutura "simples" com 1 só elemento temos um espetro bem definido e fácil de entender (EX: diamante)
- Para materiais mais complexos (EX: poliestireno) teremos menos simetria e temos vários tipos de átomos. Assim, temos diferentes geometrias e diferentes tipos de ligações

### Frequências de vibração
- Como explicado acima, a frequência de vibração depende da massa dos átomos e da força das ligações. (Átomos pesados com ligações fortes dão um shift elevado)
- Por exemplo o caso do poliestireno:
![[raman poliestireno.png]]
    - Temos vibrações de alta frequência (3000) que se devem a ligações C-H
    - Temos vibrações de menor frequência (800) que correspondem a ligações C-C. C-H tem maior frequência porque o hidrogénio é mais leve.
    - Em 1600 temos um pico que se deve a ligações duplas C=C

### Carateristicas do espetro
- Vejamos algumas informações:
    - **Frequências dos picos** - identificar o material, já que cada um tem uma fingerprint
    - **Amplitude do pico (variação de energia)** - concentração ou quantidade de material
    - **Variação de intensidade ao mudar a polarização do laser** - orientação cristalografica do material
    - **Variação da posição do pico / da banda** - aplicação de forças de compressão ou stress/tensão
    - **Variação da largura do pico** - uniformidade do comprimento das ligações

### Baixas frequências
- Podemos estudar baixas frequências (<100cm-1) 
- Estas correspondem a estruturas com átomos muito pesados ou vibrações a escalas grandes (como toda a latice vibrar)
- Ao estudar isto, podemos determinar se um material é cristalino ou layered

## Explicação de Fotoluminescência (PL)
- Quando um laser é apontado numa amostra, tanto Raman como PL podem ocorrer.
- Ora, podem acontecer os dois ao mesmo tempo. Nesse caso, PL é muito mais intenso e pode obscurar o Raman.
- PL inclui fluorescência e fosforescência. Esta ocorre quando um eletrão ganha energia e *muda de nível eletrónico*.
    - A quantidade e tipo de PL depende do laser e do material
![[fosforencencia.png]]

### Utilidade de PL
- Em certos casos, PL pode complementar a informação de Raman.
- Alguns instrumentos podem então analisar os 2 fenómenos
- PL permite estudar propriedades eletrónicas de materiais. No caso de semicondutores, permite melhor entender a estrutura da banda condutora e detetar possíveis defeitos

### Evitar PL de fundo
- Se as bandas de PL forem muito intensas e largas podem ofuscar Raman por completo, pelo que é importante conseguir remover este efeito.
- Ao usar um laser com comprimento de onda diferente poderá mover o espetro de Raman para uma região mais longe da fluorescência, pondendo até deixar de haver fluorescência de todo
- Existem sistemas que automaticamente fazem esta mudança de laser e permitem analisar várias amostras diferentes

## Explicação de imagens de Raman
![[imagem raman.png]]
- Na esquerda temos uma imagem com luz branca de uma amostra de detergente
- Na imagem da direita temos as posiçõees de 8 espécies químicas. Para isto, em cada ponto da imagem da esquerda o espetro de Raman foi comparado a espécies de referência. A cor corresponde ao espetro de referência que tem o melhor fit.

### Como dados são recolhidos
- Os dados são recolhidos e guardados num ficheiro de dados (não numa imagem!)
    - O ficheiro de dados é que depois permite obter a imagem
- Temos 2 métodos de mapping:
    - **Ponto** - O laser foca-se num ponto. Uma base motorizada mode a amostra por debaixo do laser. Analizamos então uma série de pontos, recolhendo o espetro de cada um. Temos cerca de 1000 pontos por segundo
    - **Linha** - O laser ilumina uma linha na amostra. Conseguimos então obter o espetro de vários pontos ao mesmo tempo, o que poupa tempo. 
- Temos que ter sempre em conta *undersampling* - quando o ponto/linha que o laser ilumina é menor que o espaço entre pontos de aquisição

**Imagem de Ponto:**
![[raman cobrir area 1.png]]

**Imagem de Linha:**
![[raman cobrir area 2.png]]

### Gerar as imagens
- A analise dos dados e consequente imagem obtida é feita no software da Renishaw.

### Resolução espacial
- Alguns fatores que decidem:
    - Tamanho da ponta do laser - decidida pela abertura numérica (NA) e pelo comprimento de onda da luz
    - Espaçamento entre pontos de aquisição espectrais 
    - Magnificação das óticas do espectrometro e o tamanho dos pixeis do sensor CCD

## SERS / TERS
- Estes são 2 métodos de melhorar os resultados de Raman
- Estes métodos consistem em usar nano particulas/camadas metálicas, que aumentam a quantidade de scattering Raman que se observam
- Isto permite então detetar espetros em amostras com muito baixas concentrações. No entanto, isto só funciona com tipos de amostras específicos e é precisa uma preparação de amostra mais complexa