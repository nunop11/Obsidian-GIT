- Capítulo sobre obtenção, organização, análise e interpretação de dados experimentais/observacionais.
![[estatistica esquema.png|475]]

# 1.1 - Amostragem
- Iremos ver modos como se pode recorrer à _recolha da informação_.

## População
- Conjunto de elementos que se pretende estudar.
- Cada elemento da população á uma _unidade estatística_.
- Por vezes, a população é identificada pelas características que se pretende estudar. Ou seja, a realidade a população acaba por ser as característica. _EX:_ num estudo em que se inquere várias pessoas sobre a sua altura e distrito de residência, a população do estudo não seriam os nomes das pessoas, mas sim os pares (altura, distrito).
- As unidades de medida devem de ser sempre indicadas.

_População Alvo_ - Conjunto completo de elementos sobre os quais queremos informação.
_População em Estudo_ - Conjunto de elementos que podem efetivamente ser incluídos no estudo. 
- Idealmente estas populações são iguais, mas nem sempre é possível. 
- Quando estas diferem, os resultados não são fiáveis, e podem até estar completamente errados.

## Amostra
- Na maioria dos casos, a população em estudo é demasiado extensa para que toda ela seja observada. Assim, é considerada apenas uma _parte da população_, a amostra.

### Amostra Aleatório Simples
- Quando os critérios usados na seleção da amostra garantem que todas as amostras do mesmo tamanho têm igual probabilidade de serem selecionadas.
- Uma forma de fazer isto: a cada membro de uma população atribiu-se um número e coloca-se numa caixa papeis com os números atribuídos. Retira-se n cartões da caixa, sendo que os n membros da população equivalente a esses números são a amostra de tamanho n.
- Quando a extração é feita _com reposição_ temos uma amostra **aleatória simples com reposição**. Quando a extração é feita _sem reposição_ temos uma amostra **aleatória simples sem reposição**. 
- As difrenças entre estes 2 tipos de amostragem simples não são significativas quando o tamanho da amostra é muito menor que o da população.

- Muitas vezes não é possível fazer recolha de uma amostra aleatória simples. _EX:_ Amostra aleatória simples de 10 coelhos na Peneda Gerês.

### Amostragem Aleatória Estratificada
- Primeiro divide-se a população em conjuntos homogéneos de indivíduos (estratos). De cada estrato faz-se uma amostra aleatória. Combinamos essas amostra e obtemos a amostra do estudo. _EX:_ Num estudo sobre caranguejos , os investigadores didiviram uma praia em 4 faixas paralelas de 5m cada. Em cada faixa (estrato) selecionam-se 25 caranguejos aleatórios.

### Notas sobre Amostragem
- A obtenção da amostra deve ser feita com cuidado e de forma _não subjetiva_, recorrendo às _Técnicas de Amostragem_.
- Na prática, a forma como se escolhe a forma de fazer amostragem envolve _bom senso, intuição_ e um _profundo conhecimento_ da situação em estudo.
- Um erro frequente resulta de, inadvertidamente, a _população alvo ser diferente da população em estudo_.

# 1.2 - Estatística Descritiva
- Num estudo, cada aspeto em estudo (temperatura corporal, por exemplo), varia de indivíduo para indivíduo, pelo que designamos de _variável de interesse_ ou _variável estatística_. 
- Assim, num estudo com uma amostra de tamanho $n$, obtemos $n$ observações das variáveis. Ou seja, _cada indivíduo dá-nos 1 obervação_, sendo designado por _unidade observacional_. _EX:_ num estudo em que se mede o peso à nascença (variável de interesse) de 150 bebés nascidos num certo hospital (amostra), a unidade observacional é "um bebé".

## Variável Estatística
- **Qualitativa** - Representa qualidade/categoria/caraterística não mensurável 
    - _Nominais ou Categóricas_ - Não têm ordem (_ex:_ cor do cabelo)
    - _Ordinais_ - Têm uma ordem natural (_ex:_ gravidade de uma doença: pouco grave, média, aguda)
- **Quantitativa** - Característica que pode ser medida ou contada
    - _Contínuas_ - Os valores encontram-se numa escala contínua (_ex:_ peso em gramas de uma alface)
    - _Discretas_ - Podem assumir 1 valor finito ou infinito (_ex:_ número de pessoas por habitação)

- No entanto, deve-se notar que não só a natureza da variável importa na sua classificação. O _rigor_ da medição, o _contexto_ e a _diversidade_ de valores também importam bastante. 
    - _Rigor_ - dependendo do rigor com que se faz a medição, uma variável quantitativa pode ser contínua ou discreta
    - _Contexto_ - influencia se uma variável qualitativa será ordinal ou categórica, ou até se é quantitativa. _Ex:_ a variável "cor" pode ser quantitativa contínua (cor espetro eletromagnético), qualitativa ordinal (cores no arco-íris) ou até qualitativa nominal (cores dos olhos de um grupo de pessoas), dependendo do contexto.
    - _Diversidade_ - quando há muitos valores disponíveis de uma variável discreta, ela é tratada como contínua

---
Estatística descritiva é a parte de estatística que se eocupa de organizar e analisar dados. Prentende-se obter informação relevante através disto.

## 1.2.1 - Organização /  Descrição Gráfica

### Dados Qualitativos
- Considerasse as diferentes categorias e obtem-se a frequência de cada uma. Faz-se uma _tabela de frequências_, que normalmente têm 2 colunas:
    - _Coluna das categorias/classes_ - indicasse as categorias observadas para a variável em estudo
    - _Coluna das frequências..._
        - _Absolutas_ - representa-se o total de elementos da amostra que pertencem a cada categoria
        - _Relativas_ - coloca-se a frequência relativa para cada categoria (que pode estar em percentagem) $$\textsf{frequência relativa} = \frac{\textsf{freq absoluta}}{\textsf{nº total de observações}}$$

- A representação gráfica mais comum para este tipo de dados é o _diagrama de barras_ (vertical ou horizontal).
    - Cada barra é um retângulo cuja altura é proporcional à frequência da categoria correspondente
    - As barras têm que ter todas a mesma largura, não se tocar e ter o mesmo espaçamento. A ordem e espaçamento entre barras é arbitrário.

### Dados Quantitativos Discretos
- Ao analisar um conjunto de observações de uma variável discreta podemos proceder de 2 formas:
1. Fazer tabela de frequências
2. Agrupar os valores em classes e só depois fazer a tabela de frequências. Fazer quando se tem muitos valores distintos e/ou poucas repetições

- Com dados quantitativos, além das frequências absolutas (fa) e frequências relativas (fr), também é comum apresentar as *frequências absolutas acumuladas* (faa) e as *frequências relativas acumuladas* (fra). As frequências acumuladas de um certo valor (que acaba por ser uma classe) é igual à soma das frequências desse valor com as frequências dos valores anteriores:
![[prob quantit discreta.png|425]]

- Para dados quantitativos discretos, a representação mais comum é também o _diagrama de barras_. Mas para estes dados, como as classes são números, a sua ordem importa.
- Se a amostra é reduzida e composta por número inteiros fazemos um _diagrama de pontos_, que é basicamente um diagrama de barras mas em vez de barras e um eixo dos yy temos filas de pontos. Permite, de forma rápida, detetar erros e "situações estranhas". 
![[diagramas barras e pontos.png]]

### Dados Quantitativos Contínuos
- Primeiro devemos aplicar os dados em intervalos (classes) e fazer a tabela de frequências das classes. Os intervalos devem ser escolhidos de forma a retratar a natureza contínua dos dados.
- Tendo um conjunto de $n$ dados, para sabermos em quantas classes $k$ devemos dividir os dados temos a _Fórmula de Sturges_:
$$k = 1+\log_{2}n\approx 1+3.322\log_{10}n$$
- No entanto, na prática recorre-se ao bom senso para escolher o número de classes.

- A representação gráfica mais comum é o _histograma_. Isto é um gráfico com barras adjacentes/encostadass cuja base é igual ao intervalo da classe e cuja área é igual ou proporcional à frequência. De notar que o detalhe do histograma depende do número de intervalos escolhidos.
![[histograma.png]]
- A _amplitude_ de cada classe (base do retângulo) é dada por:
$$h = \frac{max-min}{n}$$
(sendo max e min os limites superior e inferior de um intervalo e $n$ o número de classes em estudo)

- Temos ainda que a _densidade_ de cada classe é dada por
$$\textsf{densidade}=\frac{\textsf{freq relativa}}{h}=\frac{\textsf{freq absoluta}}{n \cdot h}$$

##### Notas
- O _histograma de frequências_ absolutas depende muito da quantidade de dados e amplitude das classes, pelo que não é adequado para fazer comparações.
- No _histograma de frequências_ relativas ($\large=\frac{\textsf{freq absoluta}}{n}$), a área total dos retângulos é $1\times h$. Este histograma já não depende da quantidade de dados, mas depende da amplitude das classes.
- No _histograma de densidades_ a área total é $1$. Isto permite fazer comparações. Quando as classes têm amplitudes diferentes só podemos usar a escala de densidades.

### Formas de histogramas

#### Distribuições simétricas
![[tendencias graficos.png]]
- A distribuição das frequências é simétrica relativamente a uma classe média.

#### Distribuições enviesadas
![[graficos enviesado.png]]
- Quando os valores são muito mais pequenos num dos lados.

#### Distribuições com caudas longas
![[grafico centrado.png]]
- Grande número de classes com frequências pequenas nos extremos

#### Curva do histograma
![[formatos graficos.png|400]]
- Para representações contínuas podemos obter uma curva suave aproximando o histograma.

### Diagrama de Caule e Folhas
- Para representar _dados quantitativos discretos_

#### Recomendações gerais
- Uma folha é um dígito à direita, um caule é os 2 dígitos à esquerda
- Normalmente, não devemos ter mais de 10/15 caules
- Podemos dividir os caules para não ter muitas folhas. Só devemos dividir os caules em 2 ou 5.

> Consideremos que temos os dados ordenados:
> 210 210 212 214 218 220 222 223 223 225 227
> ![[caule e folhas.png]]

- Assim, podemos ter que $21|2=212$ ou que $21|2=21.2$. Por esta razão, temos que indicar as _unidades_ como se vê acima.
- Podemos ainda dividir cada caula em 2 (<5 e >5)
- Podemos ver um diagrama de caule e folhas como um histograma rodado 90º e com mais informação

## 1.2.2 - Médias numéricas
- Usadas para dados quantitativos. Podem ser _de localização_ ou _de dispersão_.
- Algumas médias de localização são: média, mediana, quartis, moda.

### Média
$$\bar x=\frac{1}{n} \sum\limits_{i=1}^{n} x_{i}$$
- É a partir dela que vemos se um histograma é simétrico ou enviesado

### Mediana
- Após ordenar os dados, é a observação central. Ou seja, é o valor que divide a amostra _ordenada_ em 2. Se o número de observações for ímpar a mediana é o valor central, se for par a mediana é a média aritmética das 2 observações mais centrais.
- Ou seja, tendo a amostra ordenada $\{x_{(1)}, x_{(2)}, \dots, x_{(n)} \}$, a mediana é
    - $M=x_{(k+1)}$, se $n=2k+1$
    - $M=\frac{1}{2}(x_{(k)}+x_{(k+1)})$, se $n=2k$

#### Média VS Mediana
- Se a amostra tiver uma distribuição razoavelmente simétrica, a média e mediana têm valores próximos
- Se houverem valores da amostra que são muito diferentes da maioria, isto afeta muito mais a média que a mediana. Ou seja, a _mediana é mais robusta_ que a média.

### Percentis 
- O $k$-ésimo percentil ( $k \in ]0,100[$ ) é o valor $P_{k}$ que separa as $k\%$ menores observações da amostra (ordenada) das $(100-k)\%$ maiores.
![[percentil.png|350]]
- Existem várias formas de calcular o percentil.
- Uma forma de calcular:
    - Temos uma amostra ordenada: $x_{(1)}, x_{(2)}, x_{(1)}, \dots, x_{(n)}$ 
    - Temos então o índice $i = \frac{k}{100}n$
    - De onde se tem o percentil: $$P_{k}=\begin{cases}\frac{x_{(i)}+x_{(i+1)}}{2} \quad se~~i~~inteiro\\x_{(\lfloor i\rfloor+1)} \quad ~~~ se~~i~~não~~inteiro \end{cases}$$

### Quartis 
- Dividem a amostra em 4 partes iguais. Assim, $Q_{1}$ é o percentil 25, $Q_{2}$ é o percentil 50 e $Q_{3}$ é o percentil 75.
![[medidas localizacao.png|400]]
- A _amplitude interquartil_ $AIQ=Q_{3}-Q_{1}$ é uma medidad da dispersão da análise.
- Podemos pensar no quartil 1 como sendo a mediana da primeira metade dos dados (excluindo a média) e de forma analógica para Q3
> EX: Tendo a amostra ordenada abaixo temos:
> ![[quartis.png|300]]

### Moda
- Chama-se moda ou _valor dominante de uma amostra_ ao valor de frequência máxima. Se tivermos classes, teremos uma classe modal.
- Uma amostra pode ter mais que uma média.

## 1.2.3 - Diagrama de caixa e bigodes (boxplot)
- Usando 5 valores que facilmente calculamos podemos representar de forma muito esclarecedora a forma como os dados se distribuem. Esses 5 valores são:
    - mínimo
    - Q1
    - mediana
    - Q3
    - máximo
![[caixa bigodes.png]]

> EX:
> ![[caixa bigodes 2.png|350]]

## 1.2.4 - Diagrama Caixa de Bigodes (Modified Boxplot)
- A diferença em relação ao anterior é que os bigodes terminam maix próximo dos quartis (em vez de no máx e mín). É ainda tomada em consideração a existência de outliers.
![[caixa bigodes modified.png|500]]

#### Limites dos bigodes
- O primeiro bigode termina na menor observação, que é maior ou igual à barreira inferior $BI=Q_{1}-1.5\cdot AIQ$
- O segundo bigode termina na maior observação, que é maior ou igual à barreira superior $BI=Q_{3}+1.5\cdot AIQ$
- De recordar que $AIQ=Q_{3}-Q_{1}$

#### Outliers
- _Outliers moderados_: obervações entre as barreiras inferiores BI (incluindo esta) e BEI (excluindo esta) ou entre as barreiras superiores BS (incluindo esta) e BES (excluindo esta)
- _Outliers severos:_ observações menores ou iguais à barreira inferior BEI ou maiores ou iguais à barreira superior BES
- Se tivermos outliers que podemos verificar que são um erro, devemos tentar corrigir o erro. Se não for possível, eliminar essa observação e reavaliar os procedimentos experimentais.
- No entanto, outliers podem não ser erros. Por exemplo, se tivermos dados que corrspondem a uma população com distribuição exponencial decrescente, iremos ter um histograma com formato enviesado à direita. Assim, no diagrama de caixa de bigodes iremos ter outliers, porque alguns dados estarão acima da barreira externa superior. No entanto, esses pontos não têm nada de errado. Nestes casos, não eliminamos o outlier e usamos métodos de análise mais resistentes (como mediana em vez de média)

> EX:![[caixa bigodes modified 2.png|350]]

### Comparação de dados
- Quando temos 1 só amostra, histograma dão-nos uma visão completa dos dados.
- Os diagramas de caixa-de-bigodes permitem comparar várias amostras, especialmente no que diz razão à localização, dispersão e simetria.
- Uma caixa menos comprida indica dados mais consistentes.

## 1.2.5 - Medidas de Dispersão
- Servem para medir a variebilidade de um conjunto de dados.

### Amplitude amostral
- Diferença entre o maior e menor valor das observações
- Muito sensível ao maior e menor valor, que podem ser outliers severos

### Amplitude interquartil
$$AIQ = Q_{3}-Q_{1}$$
- Muito mais robusta que a amplitude amostral

### Desvio padrão amostral
$$s = \sqrt{\frac{\sum\limits_{i=1}^{n} (x_{i}-\bar x)^{2}}{n-1}}$$
- Medida de dispersão mais usada
- 

### Variância amostral
$$s^{2}=\frac{\sum\limits_{i=1}^{n} (x_{i}-\bar x)^{2}}{n-1}= \frac{\left(\sum\limits_{i=1}^{n}x_{i}^{2} \right) - n \bar x^{2}}{n-1}$$

## Relações entre medidas
- Estas relações são aplicáveis a distribuições de dados unimodais e razoavelmente simétricas relativamente a um valor central e sem valores discordantes.
    - Cerca de _70%_ dos valores estão no intervalo: $[\bar x-s;\bar x+s]$
    - Cerca de _95%_ dos valores estão no intervalo: $[\bar x-2s;\bar x+2s]$
    - $AIQ = Q_{3}-Q_{1}\approx 1.4\cdot s$

### Coeficiente de Variação
$$CV = \frac{s}{\bar x}$$
- Para uma dada amostra, o desvio padrão pode ser grande ou pequeno dependendo da ordem de grandez dos valores (2,34 é pouco se a média for 200, mas é muito se a média for 0,3). Uma maneira de medir a variebilidade dos dados sem que a ordem de grandeza tenha influência é o _coeficiente de variação_, cuja fórmula está acima.
- Só pode ser usado quando a média não é nula. 
- Frequentemente expresso em percentagem.
- Menor CV, maior estabilidade/consistência, menor dispersão dos dados.

## Transformar variáveis
- Por vezes queremos modar váriaveis, como ao mudar de unidades de medida. Ora, isso irá mudar as medidas de dispersão obtidas. Assim, temos que saber o tipo de transformação $X\longrightarrow Z$ que estamos a fazer.

## Transformação Linear
$$Z = aX+b$$
- Caso mais simples
- Temos o conjunto $X:x_{1},x_{2}, \dots$ para o qual temos a média e desvio padrão: $\bar x$ e $s_{X}$.
- Teremos então $z_{i}=ax_{i}+b$. Assim:
$$\bar z = a \bar x+b \quad \quad s_{Z}=|a|s_{X} \quad \quad s^{2}_{Z}=a^{2} s_{X} $$

## 1.2.6 - Dados Bivariados
- _Amostra bivariada:_ amostra em que temos pares de observações de 2 variáveis $X$ e $Y$. Queremos então relacionar essas 2 variáveis.

### X e Y categóricas
- Faz-se uma tabela de dupla entrada de frquências:

_Tabela de frequências absolutas_

|           | olhos castanhos ou pretos | olhos verdes ou azuis | outros | total |
| --------- | ------------------------- | --------------------- | ------ | ----- |
| ingleses  | 104                       | 106                   | 5      | 215   |
| alemães   | 71                        | 78                    | 1      | 150   |
| italianos | 82                        | 18                    | 2      | 102   |

_Tabela de frequências relativas_

|           | olhos castanhos ou pretos | olhos verdes ou azuis | outros | total |
| --------- | ------------------------- | --------------------- | ------ | ----- |
| ingleses  | 0.22                      | 0.23                  | 0.01   | 0.46  |
| alemães   | 0.15                      | 0.17                  | 0      | 0.32  |
| italianos | 0.18                      | 0.04                  | 0      | 0.22  |

- No entanto, se quisermos comparar as variáveis "nacionalidade" e "cor dos olhos", temos que ter uma das tabelas abaixo:
![[tabelas freqs.png|350]]
sendo que ao representar as 2 tabelas acima graficamente temos:
![[diagramas multivariaiveis.png|350]]

### X quantitativa e Y categórica
- Neste caso, temos várias observações da variável quantitativa X para cada categoria Y. Podemos então representar cada categoria com um boxplot. Ao meter todos os boxplots lado a lado podemos tirar conclusões.

### X e Y quantitativas
- Temos então uma amostra do tipo $(x_{1},y_{1}), (x_{2},y_{2}), \dots (x_{n}, y_{n})$
- Para representar estes dados usamos um _diagrama de dispersão_ (scatter plot) em que marcamos os pontos $(x_{i}, y_{i})$

## Covariância
- Tendo a amostra bivariada $(x_{1}, y_{1}), \dots (x_{n}, y_{n})$, tem-se a _covariância amostrar_:
$$q_{x,y} = \frac{1}{n-1}\sum\limits_{i=1}^{n}(x_{i}-\bar x)(y_{i}-\bar y)=\frac{\sum\limits_{i=1}^{n} x_{i}y_{i}-n\bar x \bar y}{n-1}$$

## Correlação
- AKA _coeficiente de correlação linear de Pearson_
- Quantifica o grau de relacionamento linear entre par de variáveis numa amostra. É a covariancia a dividir pelo produto dos desvios padrão:
$$r = \frac{\sum\limits_{i=1}^{n} x_{i}y_{i}-n\bar x \bar y}{(n-1) s_{X}s_{Y}}$$
- Quando mais próximo de 1, mais forte será o grau de relacionamento linear das variáveis. Quando é muito próximo de 0 não podemos tomar conclusões, só sabemos que o relacionamento não é linear.
- Só indica se 2 variáveis variam em conjunto ($r>0$, se uma variável tem valores altos a outra também). Uma correlação forte não indica causalidade, apenas poderá ser um sinal. 

#prob-estat #matematica