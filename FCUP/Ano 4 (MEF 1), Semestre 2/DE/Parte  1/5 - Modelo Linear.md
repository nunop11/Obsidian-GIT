## O modelo
- Definimos como
$$f(\mathbf{x})=\beta_{0} + \sum \mathbf{x}_{j}\beta_{j}$$
em que assumimos que a condicional $\mathbb{E}(Y|\mathbf{x})$ é linear ou quase.

- As variáveis $\mathbf{x}_{j}$ podem ser:
    - quantitativas
    - transformações funcionais: $\log(x_{1}),x_2^3,\sqrt{x_3},\dots$
    - codificação numérica (=1 se ..., =0 se o oposto)
    - interações entre variáveis: $x_{1}x_2$

### MMQ / LSM (Least Square)
- Este método minimiza a soma dos quadrados dos erros (SSE - Sum of Squared Errors)
- Temos: 
$$\begin{align*}
\text{SSE}(\beta)&= \sum\limits_{i=1}^{N}(y_{i}-f(x_{i}))^{2}\\
&= \sum\limits_{i=1}^{N}\left(y_i-\beta_{0}-\sum_{j} x_{ij}\beta_{j}\right)^{2}\\
&= (Y-X\beta)^{T}(Y-X\beta)
\end{align*}$$
- Para minimizar, queremos que a derivada seja nula:
$$\frac{\partial\text{SSE}}{\partial \beta}=-2X^{T}(Y-X\beta)=0~~\to~~ \hat{\beta}=(X^{T}X)^{-1}X^{T}Y$$
- Podemos ainda ver a 2ª derivada:
$$\frac{\partial^{2}\text{SSE}}{\partial\beta\partial\beta^{T}}=2X^{T}X$$
se esta derivada não for singular, é sempre positiva.
- O caso em que $X^{T}X$ é singular (e não invertível) é quando *as colunas não sao todas independentes* -> removemos as colunas redundantes.

## Inferência
- Consideremos o caso em $\mathbb{R}^{p+1}$, em que $x_{i}$ é uma linha da matriz $X$
- Supomos que os $x_{i}$ são fixos e que os $Y_{i}$ são não correlacionados com variância $\sigma^{2}$
- Teremos que:
$$\text{Var}(\hat{\beta})=(X^{T}X)^{-1}\sigma^{2}$$
e podemos definir:
$$\hat{\sigma}^{2}=\frac{1}{N-p-1}\sum\limits_{i=1}^{N}(Y_{i}- \hat{Y}_{i})^{2}$$
- Consideramos então que:
$$Y=\beta_{0}+\sum x_{j}\beta_{j}+\varepsilon~~~~,~~ \varepsilon\sim N(0,\sigma^{2})$$
- Teremos que: $$\hat{\beta}\sim N(\beta, (X^{T}X)^{-1}\sigma^{2})~~\to~~ \frac{(N-p-1)\hat{\sigma}^{2}}{\sigma^{2}}\sim \chi_{N-p-1}^{2}$$
- Claro, $\hat{Y},\hat{\beta},\hat{\sigma}$ são as estimativas que o modelo faz para as variáveis $Y,\beta,\sigma$.

### Testes
- Consideremos $H_{0}:\beta_{j}=0~~,~~H_{1}:\beta_{j}\neq0$
- Assim, teremos $\hat{\beta_{j}}\sim N(0,\nu_{j}\sigma^{2})$ em que $\nu_{j}$ é o elemento $j$ da diagonal de $(X^{T}X)^{-1}$
    - Assim: $$\frac{\hat{\beta_{j}}}{\sigma \sqrt{\nu_{j}}}\sim N(0,1) \quad\text{e}\quad \frac{\hat{\beta_{j}}}{\hat{\sigma}\sqrt{\nu_{j}}}\sim t_{N-p-1}$$
- Assim, usando apenas os dados podemos estimar $\hat{\beta},\hat{\sigma}$ e definir intervalos de confiança:
$$\hat{\beta}_{j}\pm t_{1-\alpha/2}\hat{\sigma}\sqrt{\nu_{j}} $$

### Variáveis "inuteis"
- Consideremos que temos um modelo $1$ com $p_{1}$ variáveis - modelo *mais complexo*. Queremos ver se algumas destas variáveis são redundantes e desncessárias. 
- Então criamos um modelo $0$ com $p_{0}<p_{1}$ variáveis - *modelo mais simples*
- Podemos então calcular:
$$F=\frac{\frac{SSE_{0}-SSE_{1}}{p_{1}-p_{0}}}{\frac{SSE_{1}}{N-p_{1}-1}}$$
- Assumindo uma data de cenas, temos que: $F\sim F_{p_{1}-p_{0},N-p_{1}-1}$ (Distribuição de Schneider)
- Quando $N$ é elevado, podemos aproximar: $F\sim \chi_{p_{1}-p_{0}}^{2}$
- Podemos definir uma região de confiança:
$$C_{\beta}= \{\beta: (\hat{\beta}-\beta)^{T}X^{T}X(\hat{\beta}-\beta) \le \hat{\sigma}^{2}\chi_{p+1}(1-\alpha)\}$$

**EXEMPLO**
- Fez-se um estudo para prever o nível de antigénio na prostata a partir das variáveis preditivas (PV):
    - lcavol (log do voluma do cancro)
    - lweight (log do peso da prostata)
    - age, lbph, svi, lcp, gleason, pgg45
- Temos 97 dados. Dividiu-se em 67 de treino e 30 de teste. Aplicou-se o modelo linear. Notemos que nestes passos *apenas usamos os dados de treino*
- Determinou-se a Z score $=\frac{\hat{\beta}_{j}}{\hat{\sigma}\sqrt{\nu_{j}}}$ para cada variável:
![[exemplo prostata 1.png]]
em que, se $|\text{Z score}|>2$ temos 95% de confiança
- Assim, retiramos do modelo as variáveis "menos importantes": age, lcp, gleason, pgg45
- Calculamos $SSE_{0}$ com o novo modelo, que é mais simples
- Determinamos então: (1 é o modelo original, 0 é o simplificado)
$$F=\frac{\frac{32.81-29.43}{9-5}}{\frac{29.43}{67-9}}=1.67$$
- Temos que $P(F_{4,58}>1.67)=0.17$
- Ora, este teste consiste em verificar $H_{0}:\text{as variáveis que removemos não importam}$. Como o pvalue (a probabilidade) que determinamos deu $17\%>5\%$, então não podemos rejeitar $H_{0}$ -> as variáveis removidas parecem não importar mesmo

### Teorema Gauss-Markov
- Diz que:
$$\begin{align*}
&\LARGE{\mathscr{D}}\normalsize\text{e todos os estimadores lineares centrados para } \beta, \\
&\text{o EMMQ (Estimador de Mínima Variância Quadrática)} \\
&\text{é aquele com a menor variância}
\end{align*}$$

**Porque importa?**
- Tal como vimos atrás, definimos o EMMQ de $\theta$ como:
$$\hat{\theta}=\mathbf{a}^{T}\hat{\beta}=\mathbf{a}^{T}(X^{T}X)^{-1}X^{T}Y$$
em que $\theta=\mathbf{a}^{T}\beta$. 
- Notemos aqui que $\theta$ é uma combinação linear de parâmetros. Ou seja, $\theta$ é uma função que definimos a partir dos pesos $\beta$. 
    - Imaginemos que numa fase de treino estimamos $\hat{\beta}$. Assim, colocando valores das $p$ variáveis no vetor $\mathbf{a}$, podemos estimar uma certa grandeza: $\hat{\theta}$![[explicacao theta.png]]
- Ou seja, precisamos de estimar $\hat{\beta}$ com a menor variância possível, já que essa se vai traduzir como incerteza da estimativa $\hat{\theta}$.

**Matrizes de variância**
- Seja $\beta=(\beta_{1},\beta_{2},\dots,\beta_{p})^{T}$. O EMMQ de $\beta$ será aquele que tem a menor variância de entre todos os estimadores lineares centrados de $\beta$:
    - $\hat{V}$ for a matriz de variâncias do estimador $\hat{\beta}$ <- este é o EMMQ
    - $\tilde{V}$ é a matriz de outros estimador linear centrado
    - Assim, sendo $\hat{V}$ do EMMQ teremos sempre: $\hat{V}\preccurlyeq \tilde{V}$ (a matriz $\hat{V}$ é "menor" que a outra) então $\tilde{V}-\hat{V}$ é semi-definida como positiva. Isto quer dizer que cada parâmetro terá menor variância E que o estimador tem menor variância "global"

**Outra vantagem do EMMQ**
- Podemos definir o MSE:
$$\text{MSE}(\tilde{\theta})=\mathbb{E}[(\tilde{\theta}-\theta)^{2}]=\text{Var}(\tilde{\theta}) + [\mathbb{E}(\tilde{\theta})-\theta]^{2}=\text{Var}(\tilde{\theta})+\text{Bias}(\tilde{\theta})^{2}$$
- No entanto, esta "vantagem" não é garantida: podemos ter estimadores com bias mas menor MSE.
    - Ou seja, vemos que o EMMQ irá minimizar o MSE dentro da classe de estimadores sem bias.

**QR, sim decomposição Q-R**
- Por vezes, é mais estável numericamente decompor em QR invés de resolver diretamente $X^TX\beta=X^TY$
- Então decompomos:$$X=QR$$
- Em que temos: 
    - $Q$: shape $N\times(p+1)$, que é ortogonal -> $Q^{T}Q=I$
    - $R$: shape $(p+1)\times(p+1)$, que é triangular superior
- Usando esta nova forma, podemos definir:
$$\hat{\beta}=R^{-1}Q^{T}Y \quad;\quad \hat{Y}=QQ^{T}Y$$
(isto vem tudo direto de substituir $X=QR$ nas  equações)

##### EXEMPLO
**1 fator**
![[exemplo publicidade 1.png]]
- Normalmente usamos 2 medidas de qualidade do fit:
    - $R^{2}$
    - $\text{RSE}=\sqrt{\frac{1}{n-2}\text{RSS}}=\sqrt{\frac{1}{n-2}\sum_{i=1}^{n}(\hat{y}_{i}-y_{i})^{2}}$ que dá o valor "médio dos resíduos"
- No caso deste ajuste do exemplo temos $RSS=3.26$, ou seja, em média as vendas desviam-se da previsão do modelo linear em 3260 unidades.

**3 fatores independentes**
- Podemos agora tornar o modelo mais complexo, adicionando a publicidade de rádio e jornal:
![[exemplo publicidade 2.png]]
- Ora, isto faz sentido, mas temos um problema: se estes fatores estiverem correlacionados isto é mais complexo (como vemos no texto acima, a tabela só pode ser intepretada de forma "direta" se apenas 1/3 fatores for variável)
- Notemos algo específico: jornais parecem não afetar as vendas
    - Isto parece não fazer sentido. Mas até faz na realidade
    - Neste estudo determinou-se uma correlação de 0.35 entre rádio e jornal. O que isso significa que: num mercado em que gastamos muito dinheiro em rádio iremos ter mais vendas, mas temos também a tendência de ter gasto mais em jornais.
    - Ou seja, se fizermos uma análise linear só com Vendas VS Jornal, iremos ver que em alguns mercados as vendas aumentam "graças aos jornais". Na realidade estas estão associadas à publicidade rádio e os jornais "ficam com crédito"
- Isto tudo mostra a importância de nunca ignorar correlações.

### Algum fator é relevante?
- Como vemos se, de uma série de fatores em estudo, sabemos se *pelo menos 1* deles de facto afeta o output?
- Testamos $$\begin{align*}
H_{0}&: \beta_{1}=\beta_{2}=\dots=\beta_{p}=0\\
H_{1}&: \text{pelo menos um }\beta_{j}\text{ é não-nulo}
\end{align*}$$
- Se nenhum dos fatores importa teremos $F\sim1$
- Se de facto algum fator importa, teremos $F\gg1$
- Também o pvalue permite fazer esta conclusão. No exemplo da publicidade, vemos que há sinais/provas que TV e rádio afetam as vendas ($\text{pvalue}\sim0$), mas não para jornal. *NOTA*: estes pvalues são dos t-tests individuais dos fatores, também presentes na tabela.

- NO ENTANTO, especialmente se $p\gg1$, não chega olhar para os pvalues dos fatores
    - Podemos ter $p=100$ e nenhum dos fatores afeta o output
    - Mas, por mero acaso, podemos ter 5% dos pvalues abaixo de 0.05. Ou seja, acharíamos que 5 dos fatores afetam o output
    - Já a estatística $F$ tem o número de dados e fatores na sua fórmula. Logo, ela ajusta-se a isto e é sempre de confiança. 

### Previsores qualitativos
- "Previsores" é outro nome que podemos dar às variáveis/fatores que entram no modelo linear: os $x_{i}$

#### Previsores de 2 níveis
- Este tipo de previsor pode aparecer em qualquer situação em que temos 2 grupos diferentes
-  EX: dividir uma um estudo pelo género
$$y_{i}=\beta_{0}+\beta_{1}x+\varepsilon_{i}=\begin{cases}
\beta_{0}+\beta_{1}+\varepsilon_{i}&;&\text{mulheres} \\
\beta_{0}+\varepsilon_{i}&;&\text{homens}
\end{cases}$$
em que temos o previsor: 
$$x=\begin{cases}
1&;&\text{mulher} \\
0&;&\text{homem}
\end{cases}$$
- Neste exemplo, $\beta_{0}$ pode representar o valor médio e $\beta_{1}$ a variação média dessa grandeza que se verifica para mulheres. 
- Esta codificação define um dos géneros como "referência", já que o outro só se encontra acima dele
- Outra opção, para remover essa "referência" seria:
$$x=\begin{cases}
1 & ; & \text{mulher} \\
-1 & ; & \text{homem}
\end{cases}$$

#### Previsores com >2 níveis
- Isto é o caso de dividir um estudo conforme um fator com várias opções
- EX: etnia/raça
$$y_{i}=\beta_{0}+\beta_{1}x_{i1}+\beta_{2}x_{i2}+\varepsilon_{i}=\begin{cases}
\beta_{0}+\beta_{1}+\varepsilon_{i}  & ; & \text{Asiáticos} \\
\beta_{0}+\beta_{2}+\varepsilon_{i} & ; & \text{Caucasianos} \\
\beta_{0}+\varepsilon_{i} & ; &  \text{Africanos}
\end{cases}$$
em que
$$x_{i1}=\begin{cases}
1 & ; & \text{Asiático} \\
0 & ; & \text{Não asiático}
\end{cases}\quad;\quad x_{i2}=\begin{cases}
1 & ; & \text{Caucasiano} \\
0 & ; & \text{Não caucasiano}
\end{cases}$$
- Agora, temos que Africanos é a classe de "referência" que tem um valor médio $\beta_{0}$ para a grandeza em estudo.
- Por sua vez, $\beta_{1}$ será quanto asiáticos diferem de africanos nessa grandeza
- Finalmente, $\beta_{2}$ será quanto caucasianos diferem de africanos nessa grandeza

- Pode ser feita uma tabela de regressão. E novamente temos os pvalues de todos os fatores. E, novamente, é sempre melhor testar $H_{0}:\beta_{1}=\beta_{2}=0$ com o F-test para verificar se de facto há diferença entre as classes.
    - No exemplo com valores no PPT obtem-se pvalues perto de 1, logo parece que não há diferença entre as classes
    - Ao fazer F-test temos que o pvalue de F é $0.96$. Isto mostra que não podemos rejeitar H0, ou seja, **há** diferença 

### Interações
- A principal assunção do modelo linear com vários fatores é que: a relação output-fator é *linear* e que as relações com os vários fatores são *aditivas*
    - A parte linear é óbvia: se variarmos um previsor $X_{j}$, $Y$ variará sempre proporcionalmente. 
        - Esta simplificação pode ser removida do modelo ao adicionar termos polinomiais 
    - A parte de adição consiste em: se variarmos um previsor $X_{j}$, a resposta em $Y$ é independente dos valores nos outros previsoroes $X_{k},k\neq j$

**Remover assunção aditiva**
- Consideremos o exemplo de publicidade. Consideremos apenas os fatores 'TV' e 'radio'. Teremos:
$$Y=\beta_{0}+\beta_{1}X_{1}+\beta_{2}X_{2}+\beta_{3}X_{1}X_{2}+\varepsilon$$
que reescrevemos
$$Y=\beta_{0}+(\beta_{1}+\beta_{3}X_{2})X_{1}+\beta_{2}X_{2}+\varepsilon$$
($Y:\text{vendas},X_{1}:\text{TV},X_{2}:\text{radio}$)

- Com os dados de publicidades, obteve-se que o pvalue associado a $\beta_{3}$ é muito baixo. Ou seja, a relação TV-radio não é mesmo aditiva.
- Além disso, o $R^{2}$ aumenta 7% ao introduzir este termo
    - O $R^{2}$ aumenta de $89.7\%$ para $96.8\%$. Podemos escrever: $$\frac{96.8-89.7}{100-89.7}=69\%$$e esta é a *variebilidade* do modelo sem termo de interação que é explicado pela interação.
- **NOTA**: o princípio de hierarquia diz que, mesmo que um fator não tenha efeito no output, ele deve ser colocado no modelo se ele aparecer numa interação!

### Detetar e corrigir problemas
#### Não-linearidade
- Esta pode ser detetada com um gráfico de resíduos
- Definimos os resíduos como $e_{i}=y_{i}-\hat{y}_{i}$. 
    - Para modelos lineares simples metemos estes VS $x_{i}$
    - Para modelos com vários fatores metemos estes VS $\hat{y_{i}}$ (falor previsto)
- Simplesmente vemos o gráfico e vemos se os resíduos seguem alguma tendência (quadrática, log, etc)
- Para remover/diminuir este problema, simplesmente introduzimos transformações nos dados: $\log x,x^{2},\sqrt{x},\dots$

#### Correlação dos termos de erro
- Representamos sempre este modelo com um $\varepsilon_{i}$ no fim. Este é o erro
- Se houverem correlações então:
    1. O RSS e RSE irão subestimar o erro 
    2. A confiança e ICs serão na realidade mais estreitos do que pensamos
    3. Os pvalues também serão menores do que esperado
    4. A certo ponto, podemos excluir parametros que não devíamos

- 2 Fontes possíveis deste erro:
    - Dados temporais - dados medidos sequencialmente poderão ter erros associados a um efeito físico e portanto o erro de um certo ponto estará associado aos dos pontos vizinhos. Neste caso, devemos conseguir ver uma tendência nos resíduos (que não será devido a não linearidade!!!)
    - Correlação de sujeitos - imaginemos um estudo em que se estuda a relação Altura VS Peso. Perdemos a não correlação de erros se participarem sujeitos: da mesma família, com a mesma dieta, etc

#### Variância não contantes de erros
- Nos termos de erro fazemos outra assunção, dizemos que: $\varepsilon_{i}\sim N(0,\sigma^{2})$
- Ou seja, estamos a assumir uma variância constante de $\sigma^{2}$, igual para todos os fatores.
- Isto pode também ser visto no gráfico de resíduos:
![[variancia nao const.png]]

#### Outliers
- São pontos em que estão muito mais longe da previsão do que os restantes
- Em vários casos eles não afetam muito o fit em si, mas afetam bastante os erros RSE,RSS. Assim, o ponto outlier pode levar a conclusões erradas sobre o fit e sobre os seus fatores.
- Para decidir se um ponto é outlier.
    - Dividimos cada resíduo pelo seu erro quadrático / RSS - fazemos um gráfico de resíduos *studentized*
    - Qualquer ponto com valor $>3$ em módulo pode ser um outlier
- Se achamos que o outlier existe devido a um erro de medição ou registo podemos *remover*. Mas temos que ter cuidado porque ele pode ser resultado de um modelo fraco (por exemplo, com fatores em falta)
![[outlier.png]]

#### Pontos de alto leverage
- Outlier são pontos que têm um valor $y_{i}$ muito distante de $\hat{y}_{i}$
- Pontos de alto leverage têm o "valor errado" de $x$. Exemplo:
![[alto leverage.png]]
o ponto a vermelho parece "bater mal" com o resto dos pontos, apesar que aqui só vemos os inputs X.
- Estes pontos podem afetar muito mais o fit quando removidos.
- Eles são principalmente importantes e marcantes em regressões com 2+ fatores. 
    - Além disso, neste casos, é difícil perceber se pontos têm alto leverage simplesmente com plots.

- Então, definimos a estatística *leverage*. Para o caso de regressões com 1 fator:
$$h_{i}=\frac{1}{n} + \frac{(x_{i}-\overline{x})^{2}}{\sum_{j=1}^{n}(x_{j}-\overline{x})^{2}}$$
e podemos fazer gráficos deste tipo
![[alto leverage consequencia.png]]
notemos neste gráfico:
    - O ponto 20 tem baixo leverage e resíduos altos: é um outlier. Ele afeta os erros, mas pouco afeta o fit
    - O ponto 41 é um outlier E tem alto leverage. Ele afeta os erros e piora o fit. Combinação perigosa.

- Em geral, suspeitamos que um ponto tem alto leverage se $$h_{i}> 2 \frac{p+1}{n}$$

#### Colinearidade
- Quando 2+ previsores estão fortemente relacionados. Algo assim:
![[colinearidade.png]]
- Isto complica o fit porque torna-se muito difícil perceber o que é o efeito de cada previsor no fit
![[colinearidade efeito.png]]
- Ou seja, vemos que muitos pares de (Limit, Rating) irão dar RSS igual. Por outras palavras, será muito difícil encontrar um $\hat{\beta}$ que minimize o erro global.
- Assim, colinearidade aumenta o erro standard (RSS,RSE) de $\hat{\beta_{j}}$.
- Ainda por causa disto, torna-se mais difícil rejeitar corretamente $H_{0}:\beta_{1}=\dots=\beta_{j}=0$.

*Detetar*
- Muitos casos de colinearidade podem ser detetados ao ver *correlações elevadas* na matriz de correlação.
- Mas nem sempre é possível. Se tivermos colinearidade entre 3+ variáveis, pode não haver nenhum par de variáveis com alta correlação
    - A isto chamamos **multicolinearidade** 
    - Neste caso, a melhor forma de detetar isto é calcular o VIF (variance inflaction factor) : o ratio da variância de $\hat{\beta}_{j}$ usado para fitar o modelo todo a dividir pela variância de $\hat{\beta_{j}}$ por si só: $$\text{VIF} [\hat{\beta_{j}}]=\frac{1}{1-R^{2}_{X_{j}|X_{-j}}}$$
    - $R_{X_{j}|X_{-j}}^{2}$ é o $R^{2}$ de uma regressão de $X_{j}$ para todos os outros previsores (que são $X_{-j}$). Ou seja: fazemos uma de regressão de $X_{j}$ *em função* dos outros previsores!
    - O menor valor possível de IVF é 1 (nenhuma colinearidade). *Regra geral* : IVF acima de 5 ou 10 é uma quantidade de colinearidade preocupante
- No gráfico acima, para Age, Limit e Rating temos VIF de 1.01, 160.67, 160.59. Claramente há problemas
*Resolver*
- Temos 2 opções:
    - Remover 1 das variáveis problemáticas
    - Juntar as 2 numa só com uma média

## Selecionar variáveis
- Quanto introduzimos muitas variáveis no modelo aumentamos a variância mas baixamos o bias (*tradeoff variance-bias*)
- Além disso, claro, um modelo com menos variáveis será mais fácil de entender e interpretar fisicamente

*A tarefa*
- Temos $p$ previsores totais conhecidos no nosso problema
- Assim, para cada valor de $k~(0\le k\le p)$ vamos encontrar o conjunto de $k$ variáveis que minimiza SSE.
![[escolher variaveis algoritmo.png]]
- Logicamente, este erro irá sempre decrescer. Isto porque eventualmente iremos a gerar overfitting: o erro irá baixar mas o modelo começa a ser demasiado focado nos dados de treino especificos.

### $p>40$
#### Forward Stepwise Selection
- Começamos só com $\beta_{0}$ e vamos por ordem adicionando a variável que mais contribui para a melhoria do modelo:
    - Seja $\hat{\beta}$ o vetor com $k$ pesos com que começamos E $\tilde{\beta}$ o vetor com que ficamos no fim do passo (que consiste ao inicial + uma variável nova)
    - Definimos $$F=\frac{\text{SSE}(\hat{\beta}) - \text{SSE}(\tilde{\beta})}{\frac{\text{SSE}(\tilde{\beta})}{N-k-2}}$$ (pelo que teremos um $F$ e um $\tilde{\beta}$ para cada variável)
    - Adicionamos a variável que maximiza $F$
- Paramos o processo se o valor $F$ está abaixo do percentil 90 ou 95% de $F_{1,N-k-2}$

#### Backward Stepwise Selection
- Começamos com o modelo completo e vamos tirando variáveis
- Fazemos o mesmo processo que no Forward. Definimos o vetor atual $\hat{\beta}$ e o vetor do final do passo $\tilde{\beta}$ que tem 1 variável menos.
- Calculamos $F$
- Em cada passo, removemos a variável que minimiza $F$
- Paramos o processo se o valor de $F$ está acima do percentil 90 ou 95% de $F_{1,N-k-2}$

#### Mixed
- Como o nome indica, mistura os 2 métodos acima. 
- Em cada passo escolhe-se o melhor movimento (para a frente ou para trás). Claro, isso implica que precisamos de definir um parâmetro 

## Métodos de contração (shrinkage)
- Nos 3 métodos, as variáveis OU entram no modelo OU têm coeficiente zero. Temos uma situação binária portanto
- Assim, vamos ver métodos mais "contínuos"
- Consideremos o estimador MMQ (least squares) que temos usado: $\hat{\beta}^{MMQ}$
- O problema do $\hat{\beta}^{MMQ}$ é que alguns dos coeficientes $\hat{\beta}_{j}$ podem "explodir". Se 2+ variáveis forem muito correlacionadas, os coeficientes podem aumentar muito com sinais contrários, anulando-se. Isso pode aumentar muito mesmo o erro quadrático.
- Para evitar estas explosões, a solução é "encolher"/shrink os coeficientes.

### Ridge Regression
- Introduzimos uma penalização $L_{2}$ ao tamanho dos coeficientes:
$$\hat{\beta}^{\text{ridge}}=\text{argmin}_{\beta} \left[\sum\limits_{i=1}^{N} \left(Y_{i}-\beta_{0}-\sum\limits_{j=1}^{p}x_{ij}\beta_{j}\right)^{2}+\lambda \sum\limits_{j=1}^{p}\beta_{j}^{2}\right]$$
que podemos ainda escrever como:
$$\hat{\beta}^{\text{ridge}}=\text{argmin}_{\beta} \left[\sum\limits_{i=1}^{N} \left(Y_{i}-\beta_{0}-\sum\limits_{j=1}^{p}x_{ij}\beta_{j}\right)^{2}\right] \text{ em que: } \sum\limits_{j=1}^{p}\beta_{j}^{2}\le s$$
- Para variáveis muito correlacionadas isto dá bons resultados. 
- A escolha de $\lambda$ é **fundamental**
- Notemos que $\beta_{0}$ não deve ser encolhido, já que esta é a "resposta" do sistema quando $x_{1}=x_{2}=\dots=x_{p}=0$. 
    - Para que $\beta_{0}$ seja mais "compreensível", devemos começar por standardizar as variáveis

**Porquê que Ridge é melhor?**
- Está tudo relacionado com o tradeoff variance-bias
- Consoantes aumenta $\lambda$, a flexibilidade do modelo diminui, ou seja, diminui a variância. Com iisto aumenta o bias.
    - Se o bias aumentar menos do que diminui a variância, *temos uma melhoria*!
![[trade off que justifica ridge.png]]
- Ridge é especialmente bom quando os estimadores têm grande variância.
    - Ora, quando $Y$ e os previsões têm uma relação linear, os estimadores MMQ tendem a ter baixo bias e alta variância. Dá jeito!
- Computacionalmente, Ridge tem a vantagem que automaticamente faz a seleção de variáveis "melhores", porque remove variáveis muito correlacionadas.
- Com este método, temos o seguinte SSE, que depende de $\lambda$:
$$\text{SSE}(\lambda)=(Y-X\beta)^{T}(Y-X\beta) + \lambda \beta^{T}\beta$$
logo, a estimativa dos pesos com Ridge:
$$\hat{\beta}^{\text{ridge}}=(X^{T}X+\lambda I)^{-1}X^{T}Y$$

**SVD**
- Podemos decompor a matriz $X$ (shape $N\times p$) em SVD (vai ao Google ver o que é):
$$X=UDV^{T}$$
e temos $U$ (shape $N\times p$), $V$ (shape $p\times p$) e $D$ (shape $p\times p$) 
- Temos que $D$ é uma matriz diagonal com os elementos $d_{1}\ge d_{2}\ge\dots\ge d_{p}$
- E podemos substituir isto, obtendo-se:
$$\begin{align*}
\hat{Y}=UU^{T}Y \quad;\quad X \hat{\beta}^{\text{ridge}}&= UD(D+\lambda I)^{-1}DU^{T}Y\\
&= \sum\limits_{j=1}^{p} u_{j} \frac{d_{j}^{2}}{d_{j}^{2}+\lambda}u_{j}^{T}Y
\end{align*}$$

### LASSO
- Impõe penalização $L_{1}$ ao tamanho do coeficiente:
$$\hat{\beta}^{\text{lasso}}=\text{argmin}_{\beta}\left[\sum\limits_{i=1}^{N}\left(Y_{i}-\beta_{0}-\sum\limits_{j=1}^{p}x_{ij}\beta_{j}\right)^{2}+\lambda\sum\limits_{j=1}^{p}|\beta_{j}| \right]$$
que podemos ainda escrever como:
$$\hat{\beta}^{\text{lasso}}=\text{argmin}_{\beta} \left[\sum\limits_{i=1}^{N} \left(Y_{i}-\beta_{0}-\sum\limits_{j=1}^{p}x_{ij}\beta_{j}\right)^{2}\right] \text{ em que: } \sum\limits_{j=1}^{p}|\beta_{j}|\le s$$
- Computacionalmente, LASSO é ainda mais praticavel que Ridge
- Contrariamente ao Ridge que inclui sempre todas as variáveis, LASSO faz com que eventualmente alguns coeficientes sejam *exatamente* zero (por se usar norma $L_{1}$) - eliminamos variáveis
- Assim, LASSO cria modelos muito mais fáceis de entender, porque são *esparsos*
- Vejamos uma representação das regiões permitidas de LASSO e Ridge (respetivamente):
![[lasso vs ridge.png]]
o limite LASSO (esq) é descrito por $|\beta_{1}|+|\beta_{2}|\le s$. O limite Ridge (dir) é descrito por $\beta_{1}^{2}+\beta_{2}^{2}\le s$.
- Ora, se diminuirmos $\lambda$ (e portanto aumentarmos $s$) o suficiente, estas regiões irão conter $\hat{\beta}$ (sendo que este vetor é a estimativa dada pelo MMQ). Ou seja, se aumentarmos demasiado as tolerâncias, Ridge e LASSO acabam por fazer a mesma estimativa que um modelo sem regulação.
- As estimativas de Ridge e LASSO são o primeiro ponto em que a elipse centrada em $\hat{\beta}$ tocam na região. Como no LASSO temos um quadrado, é frequente este ponto da estimativa ser *num eixo* -> Temos 1+ coeficientes **nulos**!

### Ridge VS Lasso
- Lasso tem a vantagem de criar modelos simples e fáceis de entender
- Em termos de erro/precisão, não irá sempre dominar Ridge nem Lasso. 
    - Em geral, esperamos que Lasso seja melhor (menos erro) quando temos um modelo que pode ser reduzido a pouco previsores.
    - Por outro lado, Ridge será melhor quando temos necessariamente muitos previsores
    - MAS, na prática, não sabemos quais/quantos serão os previsores. Então, só com um método de cross validation conseguimos saber qual dos 2 métodos é melhor
- Do ponto de vista probabilistico de Bayes, dá para provar que os 2 métodos correspondem a assumir que os dados seguem um modelo linear normal com erros gaussianos, mas em que o vetor $\beta$ segue uma distribuição:
    - gaussiana no casso de Ridge
    - laplace no caso de Lasso

### Como escolher $\lambda$?
- Podemos fazer isto com cross validation em que temos vários valores a definirem vários valores em teste

## Regressão com componentes principais (PCR)
- Em vários casos, temos muitos previsores e com grandes correlações
- Consideramos então as *componentes principais* dos dados $Z_{m}$.
    - Elas são ortogonais
    - Consideramos que a regressão dos dados é apenas a soma de várias regressãos de 1 variável (univariadas): $$\hat{Y}_{PCR}=\overline{Y}+\sum_{m=1}^{M}\hat{\theta}_{m}Z_{m} \quad;\quad \hat{\theta}_{m}=\frac{\langle Z_{m},Y\rangle}{\langle Z_{m},Z_{m}\rangle}$$

- Ora, as componentes principais são combinações lineares ortogonais de dados de $X$.
    - Neste caso, com ortogonais queremos dizer que: $\langle Z_{m},Z_{n}\rangle=\delta_{m,n}$ 
    - Como temos ortogonalidade, não existe correlação entre nenhum par de componentes principais - daí podermos fazer só uma soma de regressões univariadas

- Neste modelo, tal como em ridge, é comum standardizar os dados primeiro
- Em Ridge encolhemos as componentes menos importantes. Em PCR, simplesmente removemos os $p-M$ componentes menos importantes:
![[ridge vs pcr.png]]

## Regressões de altas dimensões
![[alta dimensao.png]]
- Na esquerda temos uma regressão de baixa dimensão
- Na direita temos uma regressão com $n=2$ pontos, em que temos um fit perfeito.
- Ora, alta dimensionalidade neste contexto significa que $p\ge n$ (muitos fatores/previsores, poucos dados)
    - Neste cenário, a matriz $X^{T}X$ é singular, pelo que a fórmula de $\hat{\beta}$ (sem regulação) não funciona. 
    - Além disso, podem haver multiplas soluções $\hat{\beta}$
- Isto tudo é perigoso porque iremos facilmente ter overfitting: o erro de treino será muito baixo (ou até zero), enquanto que o erro de teste será enorme.
![[consequencias overfit.png]]
- Desta imagem, podemos tirar a seguinte conclusão: $R^{2}$ e RSS *não* são bons critérios para comparar modelos que tenham diferente número de previsores/fatores. Com isto, queremos dizer que eles não são os melhores critérios quando se fala de acrescentar ou remover previsores
    - Se $R^{2}$ aumenta de 67% para 97%, OK é boa ideia introduzir a variável
    - Se $R^{2}$ aumenta de 95% para 97%, então se calhar não é grande ideia
- Isto porque $R^{2}$ apenas tem em conta os dados de treino. Ao tirar variáveis pode parecer que melhoramos o modelo (porque R2 assim diz), mas ao introduzir dados de teste, se calhar até vemos que o modelo não tem qualquer generalização possível - o erro de teste é enorme
- Precisamos então de *prever o erro de teste*

### Approach 1
- Estimamos o erro de teste de forma indireta - ajustamos o erro de treino conforme o bias de overfitting.
- O RSS acaba por ser o erro de treino. Então, temos 4 maneiras de calcular o erro de teste:
    - **CP** : $C_{p}=\frac{1}{n}(\text{RSS}+2p\hat{\sigma}^{2})$ - estamos a introduziro segundo termo como penalização extra ao RSS
    - **AIC** : $\text{AIC}=\frac{1}{n\hat{\sigma}^{2}}(\text{RSS}+2 p\hat{\sigma}^{2})$ - identico a CP mas com normalização diferente. Este método é mais genérico, esta é a equação para o nosso caso de modelo linear com erro gaussiano
    - **BIC** : $\text{BIC}=\frac{1}{n\hat{\sigma}^{2}}(\text{RSS} + \log(n)p\hat{\sigma}^{2})$ - derivado de um ponto de vias Bayesiano, similar a CP e AIC. Novamente, isto é a versão deste método para o nosso modelo geral
    - **R2 ajustado**: $R^{2}\text{adj}=1- \frac{\text{RSS/(n-p-1)}}{\text{TSS}/(n-1)}=(1-R^{2})\frac{n-1}{n-p-1}$ - Opostamente aos outros 3 métodos, queremos maximar este critério. 
        - RSS = Residuals sum of squares (diferenças em relação ao ajuste): $\sum(y_{i}-\hat{y_{i}})^{2}$
        - TSS = Total sum of squares (diferenças em relação à média dos dados): $\sum(y_{i}-\overline{y})^{2}$
        - Maximizar $R^{2}$ é equivalente a minmizar $\frac{\text{RSS}}{n-p-1}$

### Approach 2
- Podemos prever o erro de teste diretamente: com set de validação OU com cross-validation
- Claro, neste caso fazemos menos assunções
- Este método é aplicável em mais casos, mesmo quand não sabemos bem os graus de liberdade dos dados (número de previsores)

### Approach 1 vs 2
- Antigamente, a approach 1 era usada. Mas atualmente existe muito maior poder de computação, então cross-validation é algo muito mais acessível e utilizado
- Approach 1 tem ainda o problema que não funciona de todo a alta dimensão:
    - CP, AIC, BIC falham porque estimar $\hat{\sigma}$ resulta em valores $\sim0$
    - R2 ajustado falha porque facilmente obtemos valores com $R^{2}=1$ (como vimos no gráfico de 2 pontos acima)

### Análise em alta dimensão
- Na prática, confirma-se que os métodos que melhor funcionam em alta dimensão são: Forward Stepwise Selection, Ridge, LASSO, PCR
- Podemos abaixo ver a performance de LASSO consoante aumentamos a dimensão ($p$ aumenta - metemos mais previsores / maior dimensão)
![[fits com dimensao a aumentar.png]]
- Temos, para cada $p$ o MSE de LASSO com 3 níveis diferentes de graus de liberdade. Na prática temos o MSE para 3 níveis (descendentes) de regularização de previsores. Ou seja, vemos que:
    - Em $p=20$ o menor MSE (melhor performance) ocorreu para 21 graus de liberdade AKA muito baixa regularização
    - Em $p=50$ temos a melhor performance para um nível intermédio de regularização (28 graus de liberdade out of 51)
    - Em $p=2000$ o LASSO nunca funcionou bem, porque vimos nos 2 casos anteriores que apenas ~20 previsores são necessários

- Ou seja, vemos aqui o problema de alta dimensão. 
    - Consoante aumentamos o número de previsores, arriscamos muito aumentar o overfitting do modelo.
    - Isto acontece porque a maioria dos previsores que acrescentamos são "ruído" para o modelo. Então é como se ele tivesse demasiada informação.
    - Apenas melhoraríamos o ajuste se estivessemos estritamente a acrescentar previsores com efeito no output.

- Outro grave problema de altas dimensões é a *multicolinearidade*: 
    - após de aumentar a dimensão, chegamos a um ponto que quase qualquer previsor pode ser representado como uma combinação linear de outros previsores
    - a certo ponto torna-se muito difícil eliminar variáveis até só ter as independentens
    - isto tudo contribui para que seja muito difícil perceber quais previsores importam (se é que algum importa)