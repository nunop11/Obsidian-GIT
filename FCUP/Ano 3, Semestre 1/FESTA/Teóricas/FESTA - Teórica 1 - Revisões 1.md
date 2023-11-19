# 1 - Introdução / Cadeira
- Temos 3 TPCs que contam 4 valores no total.
- TPCs são computacionionais, Exame é 100% analítico

**Datas dos TPCs -- IRRELEVANTE, Não vou fazer TPCs** 
- 6/10
- 10/11
- 8/12

**Livros**
- No início do semestre (revisão de estatística) o prof irá usar apontamentos dele - Não há livro !
- A meio irá seguir mais o Kardar, mas vai buscar coisas extra a outros livros
- No final irá seguir mais o Salinas
- Haverá tipo 3 tópicos que não estão em nenhum livro :)

# 2 - Revisão de Probabilidades e Estatísticas
## 2.1 - Conceitos fundamentais
### Espaço de Acontecimentos
-  Para uma dada experiência, o conjunto cujos elementos são todos os eventos possíveis.

### Evento / Acontecimento
- Elemento do Espaço do Acontecimentos, mas pode também ser uma sequência de eventos
- EXEMPLO: Consideremos o espaço de acontecimentos $\Omega=\{1,2,3,4\}$
    - $A=\{1\}$ é um evento
    - $B=\{3,4\}$ também é um evento

### Diagrama de Venn
- Muito útil para visualizar conceitos de probabilidades.

![[diagrama venn.png|500]]

- Por exemplo, no diagrama acima temos os eventos $A,B,C$ contidos no espaço $\Omega$.

#### Acontecimentos mutuamente exclusivos
- Aproveitando o diagrama acima:
    - $A,B$ são mutuamente exclusivos pois $A \cap B=\emptyset$ 
    - $B,C$ e $A,C$ *não* são mutuamente exclusivos pois $B\cap C \neq \emptyset$, $A\cap C \neq \emptyset$

#### Acontecimento complementar
- Escrito como $\bar A$, consiste no conjunto de todos os elementos de $\Omega$ que *não* estão em $A$. Em diagrama de Venn temos:
![[complementar.png|500]]
### Partição de $\Omega$
![[partição.png|450]]
- Ora, $\{A_{i}\}$ é uma partição de $\Omega$
- Uma partição de $\Omega$ é um conjunto de vários elementos de $\Omega$, **desde que**:
    - $A_{i}\cap A_{j}= \emptyset~~,~~ \forall i,j ~~(i\neq j)$  (ou seja, 2 partições não se podem "sobrepor")
    - $\bigcup\limits_{i} A_{i}=\Omega$ (as partições têm de cobrir todo o espaço) 

### Probabilidade
- Medida do quão provável é um certo evento acontecer :/ (definição do prof)
- Normalmente está entre $0$ e $1$.