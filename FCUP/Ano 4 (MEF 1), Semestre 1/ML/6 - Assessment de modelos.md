# Risco verdadeiro e Empírico
### Risco verdadeiro
- consiste na performance ideal do modelo - associado a problemas do modelo em si
- No caso de classificação, consiste na probabilidade de classificar mal um ponto : $P(f(\mathbf{x})\neq y)$
- No caso de regressão, consiste on MSE: $\mathbb{E}[f(\mathbf{x}-y)^{2}]$
- AKA *Erro de generalização*

### Risco empírico
- Corresponde à verdadeira performance do modelo *treinado* -  associado a problemas/falhas dos dados disponíveis
- No caso de classificação, consiste na proporção de exemplos mal classificados: $\frac{1}{N}\sum_{i=1}^{N}I_{f(\mathbf{x}_{i})\neq y_{i}}P(f(\mathbf{x})\neq y)$
- No caso de regressão, conssite no Average Squared Error: $\frac{1}{N}\sum_{i=1}^{N}(f(\mathbf{x}_{i})-y_{i})^{2}$

## Complexidade vs Erro
![[Pasted image 20241127182145.png|550]]
- Vemos que consoante aumentamos a complexidade do modelo usado, o risco empírico desce. Mas o risco real não desce. Invés disso ele aumenta.
    - O risco empírico aumenta porque começaremos a ter muito overfitting, pelo que a performance do modelo com os dados de treino parece ótima!
    - O risco real aumenta, porque consoante o modelo se complica mais, ele começa a criar overfitting e começa a deixar de seguir o comportamento real do sistema em estudo.
- O que este gráfico nos diz é que a certo ponto (quando os riscos divergem), o risco empírico deixa de ser uma boa indicação do risco real.
- Temos ainda que o melhor modelo possível será aquele marcado com uma linha vertical no eixo dos XX, no mínimo do risco real - temos o melhor equilíbrio ente under e overfitting.

## Comportamento de True Risk
- Queremos ter um previsor $\hat{f}_{n}$ baseado em dados de treino e que seja tão bom como um previsor ótimo, $f^{*}$.
- Assim, definimos o *Risco de Excesso*: $\mathbb{E}[R(\hat{f}_{n})]-R^{*}$ ($R$ é o risco)
    - Como $\hat{f}_{n}$ depende do set de treino, ele depende de valores aleatórios. Ou seja, por sua vez, $R(\hat{f}_{n})$ é também aleatório!
- Como já fizemos várias vezes nesta UC, podemos subtrair e somar algo. Temos então o risco de excesso:
$$\underbrace{\mathbb{E}[R(\hat{f}_{n})] - \inf_{f\in\mathcal{F  }}R(f)}_\text{Erro de estimação} + \underbrace{\inf_{f\in\mathcal{F}} R(f) - R^{*}}_\text{Erro de aproximação}$$
em que $\inf$ é o *infimum* - o maior valor menor que $R(f)$. Ou seja, é o valor de risco imediatamente abaixo do risco da função $f$ que nos dá o risco $R(f)$ mínimo. $f\in\mathcal{F}$ é um modelo usado, dentro do conjunto dos modelos.
![[Pasted image 20241127183328.png]]
ou, de uma forma mais intuitiva:
![[Pasted image 20241127183359.png]]

### Comportamento do previsor ótimo
**Previsor Ótimo**
- Consideremos uma regressão: 
$$Y=f^{*}(X) + \epsilon \quad \quad;\quad \epsilon\sim N(0,\sigma^{2})$$
ou seja, mesmo o estimador ótimo não tem erro nulo, devido ao **ruído**. O erro aqui é $\epsilon$.

**Previsor Treinado**
- Podemos determinar o risco:
$$R^{*}=\mathbb{E}_{XY}[(f^{*}(X)-Y)^{2}]=\mathbb{E}[\epsilon^{2}]=\sigma^{2}$$
- Podemos então calcular $\mathbb{E}_{D}[R(\hat{f}_{n})]$. No PPT temos a dedução completa. Isto dá:
$$\mathbb{E}_{D}[R(\hat{f}_{n})] = \mathbb{E}_{X,Y,D}[\hat{f}_{n}(X)-\mathbb{E}_{D}[\hat{f}_{n}(X)]^{2}] + \mathbb{E}_{X,Y,D}[(\mathbb{E}_{D}[\hat{f}_{n}(X)-Y^{2})]$$
- O **primeiro termo** corresponde à *variância* do previsor treinado, $\hat{f}_{n}$, conforme variamos o set de treino.
- O **segundo temo** pode ser desenvolvido (ver PPT) e temos:
$$\mathbb{E}_{X,Y,D}[(\mathbb{E}_{D}[\hat{f}_{n}(X)-Y^{2})] = \mathbb{E}_{X,Y}[(\mathbb{E}[\hat{f}_{n}(X)] - f^{*}(X))^{2}] + \mathbb{E}_{X,Y}[\epsilon^{2}]$$
    - em que a 1ª parcela é o bias ao quadrado, mede o quando o previsor treinado se desvia do previsor ótimo
    - a 2ª parcela mede a variância associada a ruído, que é a variância do previsor ótimo

**Risco de Excesso**
- Juntando tudo isto temos então:
$$\mathbb{E}_{D}[R(\hat{f}_{n})]-R^{*}=\text{variância} + \text{bias}^{2}$$
e aqui a variância corresponde ao erro de estimação e o bias ao erro de aproximação.
- *Bias* - o quando a previsão média se afasta do valor real
- *Variância* - o quanto as previsões de afastam da previsão média

### Bias-Variância
- O teorema de Bias-Variance diz-nos que: o MSE de um estimador $\hat{\theta}$ pode ser decomposto nos termos de bias e variância.
- No PPT tem uma série de deduções.
- No final temos:
![[Pasted image 20241127184639.png]]

### Famílias de Modelos VS complexidade
- KNN - Menor vizinhança (menor $k$) -> maior complexidade
- Decision Tree - Maior depth ou Mais folhas -> maior complexidade
- Regressão polinomial - maior grau de polinómio -> maior complexidade
- Regressão de kernel - menor bandwidth -> maior complexidade

# Escolha e Assessment de Modelos
1. *Seleção* - estimar a precisão de cada modelo e escolher aquele que se comporta melhor
2. *Assessment* - após escolher o melhor, estimar o seu erro com dados de teste/novos

- Numa situação *data-rich*:
    - Dividir, de forma aleatória, o data-set em 3 partes: sets de treino, validação e teste.
        - O set de treino serve para treinar o modelo e determinar os parâmetros do modelo melhores
        - O set de validação pertence ao set de treino e serve para ir confirmando a performance
        - O set de teste é o verdadeiro "novo" set de dados e serve para testar apenas o modelo escolhido, no final
    - O erro de treino pode ser determinado com $$\overline{\text{err}}=\frac{1}{N}\sum_{n=1}^{N}L(y_{i},f(x_{i}))$$
    - O erro de teste (ou de generalização) pode ser definido assim $$\text{Err}=\mathbb{E}[L(Y,f(X))]$$
    - Normalmente teremos $\overline{\text{err}}<\text{Err}$. Isto faz sentido porque quando usamos os mesmos pontos para ajustar e avaliar o modelo (como no passo de treino), teremos menor erro.

## Hold-Out
- Simplesmente dividimos os dados de *treino* em 2 conjuntos: $D_{T},D_{V}$ - set de Treino e set de Validação. Assim garantimos que nunca há overlap nem correlação entre os dados usados para treinar e validar o modelo.
- Ou seja, como funciona:
    1. Dividimos o dataset total em 3: treino, validação e teste
    2. Para cada modelo que estamos a considerar, treinamos com $D_{T}$
    3. Para cada modelo, após treinar, avaliamos a sua precisão para o $D_{V}$ - é como se fosse um teste inicial
    4. Após escolher o melhor modelo, testar esse com o set de teste. Isto irá garantir uma avaliação independente do treino
- Este método garante que o modelo selecionado é "estável", ou seja, comporta-se sempre igual para qualquer dataset.
- Basicamente o método para casos **_data-rich_**

*Problemas*
- Obviamente, este método necessita de montes e montes de dados, já que ao deixar o set de validação completamente de parte temos que ter a certeza que isso não compromete a capacidade de treino do modelo.
- Se a divisão/escolha do set de validação correr mal por azar (o conjunto é formado aleatoriamente, isto pode sempre acontecer), podemos ter erros de validação misleading e o modelo pode ter uma má performance no teste.

## Estimações / Avaliação das previsões
- Uma forma de estimar o erro de previsão é estimar o optimismo do erro de treino e usar:
$$\hat{\text{Err}}=\overline{\text{err}}+\text{optimismo}$$
### AIC
- O critério de informação de *Akaike* (AIC) diz-nos que:
$$AIC = \overline{\text{err}} + 2 \frac{d}{N} \hat{\sigma}_{\epsilon}^{2}$$
em que temos $N$ samples, $\sigma_{\epsilon}^{2}$ é a estimativa da variância do ruído (obtido com o MSE de um modelo com bias baixo) e $d$ é o número de parâmetros.
- Temos abaixo como se comporta o AIC:
![[Pasted image 20241127215642.png|500]]

### BIC
- O critério de informação de Bayes (BIC) diz que:
$$BIC = \frac{N}{\hat{\sigma}_\epsilon^{2}} \left[\overline{\text{err}} + \log (N) \frac{d}{N} \hat{\sigma}_{\epsilon}^{2}\right]$$
- Assumindo que $N>e^{2}$ ($e$ é o número de Neper), o BIC tende a penalizar modelos complexos mais que AIC. Ou seja, dá preferência a modelos simples.
- Tanto AIC como BIC são usados em casos que ajustamos dados com maximização de log-likelihood
- Esta equação é deduzida ao estudar categorização com um modelo de Bayes com aproximações.

### Minimum description length
- Definimos um critério de seleção idêntico a BIC (do ponto de vista formal)
- Consideremos que temos um modelo com parâmetros $\theta$ e pontos de dados $Z=(X,y)$. 
- Consideremos que os outputs têm probabilidades $P(y|\theta,X)$
    - Assumimos que o recetor sabe todos os inputs e queremos transmitir os outputs
    - Então o comprimento da mensagem necessário para transmitir os outputs é $=-\log P(y|\theta,X)-\log P(\theta)$
- Este método diz que devemos escolher o modelo que dá a maior probabilidade posterior. 

### Dimensão de Vapnik-Chernovenkis (VC)
- Como vimos, em certos métodos como BIC, temos que definir o número de parâmetros (AKA complexidade) do modelo
- A teoria VC dá uma forma de medir a complexidade

**A ideia**
- Medimos a complexidade através do número de funções distintas que podem ser definidas
- Uma função de hipótese é mais complexa se consegue representar vários tipos de classificação

**Definição**
- Um conjunto de pontos é *shattered* por $\mathcal{H}$ (o espaço de hipótese) se para todos os pontos existe um $h\in\mathcal{H}$ que pode representar a classe atribuída.
- Vamos então medir a complexidade vendo o número de pontos que conseguimos shatter com $\mathcal{H}$

**Exemplo**
![[Pasted image 20241127222842.png]]
por exemplo, a última imagem representa algo que tem maior complexidade, já que não podemos usar uma reta para limitar as classes.

**O jogo**
- Podemos ver o método de dimensão VC como um jogo de shattering entre nós e um adversário
- Para mostrar que $\mathcal{H}$ tem dimensão VC $\ge d$ fazemos:
    1. Escolher $d$ pontos em posições aleatórias
    2. O adversário escolhe labels/classes para esses pontos
    3. Eu escolho uma função $h\in\mathcal{H}$ que consegue separar as 2 classes de forma correta
    4. Eu ganho o jogo se conseguir arranjar uma função $h$ que faça isso. Perco se não.
- Vamos repetindo isto para vários $d$.
- A dimensão VC é o maior $d$ em que conseguimos ganhar o jogo

*Exemplos*
- Uma função linear em $p$ dimensões tem dimensão VC igual a $p+1$ que é também o número de parâmetros 

### Cross Validation
- Como já vimos, se tivessemos dados que chegue, teríamos um set de dados de validação que usaríamos para avaliar a performance do modelo.
- Definimos então a *K-fold cross-validation*. Esta pega nos dados que temos e vai escolhendo partes para ajustar o modelo e deixando 1 parte para testar/validar.
- Fazemos assim:
    1. Dividimos os dados em $K$ partes iguais. 
    2. Vamos percorrendo $k=1,2,\dots,K$ e ajustamos o modelo com a parte $k$ removida, calculando o erro de previsão associado à parte $k$.
    3. A nossa previsão final é a média ou voto da maioria dos $K$ estimadores que temos.
- Dito de outra forma, aplicamos $K$ estimadores hold-out que usam os conjuntos $k$ e não-$k$ como sets de validação e treino.
![[Pasted image 20241127224404.png|500]]

### LOO (Leave One Out)
- Isto é um caso especial de K-fold em que $K=n$.
- Por outras palavras, aplicamos $n$ estimadores hold-out em que cada um tem apenas 1 observação.
![[Pasted image 20241127224704.png|500]]

### Random Subsampling
- Mais um tipo de cross-validation
- Agora, invés de falarmos no número de partes $K$ em que dividimos os dados, falamos na *porção* dos dados que usamos para validação.
- Usamos uma porção $\alpha n$ ($0<\alpha<1$) do set de dados para validação
- Vamos quase de certeza ter pontos a pertencer a mais que 1 set de validação, o que torna os sets de validação não-independentes
- Ou seja:
    1. Fazemos $K$ ensaios. Para o ensaio $k=1,2,\dots,K$ selecionamos $\alpha n$ pontos **aleatoriamente**
    2. Usamos esses pontos aleatórios como conjunto de validação
    3. Repetimos para todos os $k$, sendo escolhendo aleatoriamente
    4. A previsão final é a média ou voto de maioria dos $K$ estimadores
![[Pasted image 20241127225134.png|500]]

### Comparação de métodos de cross-validation
- Quando temos $K$ muito elevado (LOO) teremos um bias muito reduzido porque cada ensaio tem perto de $n$ pontos de treino. Mas teremos uma maior variância porque todos os sets de validação são demasiado parecidos e podemos facilmente ter valores longe da média. Computacionalmente, torna-se muito pesado e até impossível.
- Com $K$ menor teremos variância menor mas o bias já será maior. Computação muito mais razoável.
![[Pasted image 20241127225526.png]]
- Na prática, $K=3$ já é bom
- Se tivermos dados muito esparsos podemos ter que usar LOO
- Uma escolha comum é $K=10,\alpha=0.1$

## Medidas da Classificação
### Confusion Matrix
![[Pasted image 20241127225950.png]]
- Daqui podemos definir:
    - Erro de classificação: $\frac{\text{erros}}{\text{total}}=\frac{FP+FN}{TP+TN+FP+FN}$
    - Accuracy: $1-\text{erro}=\frac{\text{correto}}{\text{total}}=\frac{TP+TN}{TP+TN+FP+FN}$
- Mas este método não consegue lidar bem com classes muito desiquilibradas.
    - Imaginemos um previsor que diz quando vai acontecer um tremor de terra. Como estes são fenómenos muito raros, se o previsor dissesse sempre que não vai acontecer, ele teria 99.999% de precisão. Mas não estamos a ter em conta que um FN é muito mais grave que um FP 

- Temos então ainda:
    - Rate de falso alarme (FA) = Rate de FP : $\frac{FP}{FP+TN}$
    - Rate de misses = Rate de FN : $\frac{FN}{TP+FN}$
    - Recall = Rate de TP : $\frac{TP}{TP+FN}$ (= 1 - Rate de misses)
    - Precisão : $\frac{TP}{TP+FP}$
- Indicar só 1 destes parâmetros não tem significado. Temos que indicar sempre pares: recall/precisão ou Miss/rate FA ou rate TP/rate FP

### Curvas ROC
- ROC = Receiver Operating Characteristic
- TPR = TP ratio ; FPR = FP ratio
- Consideremos que temos um algoritmo que vê se algo é spam.
- Muitos algoritmos calculam ainda a *confiança* $f(x)$. E define-se um **threshold** $t$.
    - Podemos então fazer algo tipo: se $f(x)> t$ temos spam, senão não.
- Teremos que:
$$\begin{align*}
\text{FPR} &= P(f(x)>t|\text{não spam})\\
\text{TPR} &= P(f(x)>t|\text{spam})
\end{align*}$$
ou seja, $t$ afeta o rate de erro do modelo.
- Temos aqui o TPR em função de FPR conforme varia $t$:
![[Pasted image 20241127231502.png]]

### Avaliar Regressões
- No caso de classificadores só temos que ver quandas vezes erramos 
- Para uma regressão é mais complicado
    - Temos valores $y_{i}$ associados a inputs $x_{i}$
    - E estaremos sempre "errados"
    - Assim, temos que usar uma medida de quanto erramos

#### MSE (Mean Square Error)
- Mais comum, mais fácil de entender 
- Mais sensível a outliers
- Pode ou não ter a raiz, chamando-se RMSE (root MSE) se tiver:
$$\begin{align*}
\text{MSE}&= \frac{1}{n}\sum\limits_{i=1}^{n} (f(x_{i})-y_{i})^{2}\\
\text{RMSE}&= \sqrt{\frac{1}{n}\sum\limits_{i=1}^{n} (f(x_{i})-y_{i})^{2}}
\end{align*}$$
- Podemos ainda definir MSE relativo à média:
$$\text{rMSE}=\sqrt{\frac{\sum\limits_{i=1}^{n} (f(x_{i})-y_{i})^{2}}{\sum\limits_{i=1}^{n} (\mu_{y}-y_{i})^{2}}}$$

#### MAE (Mean Absolute Error)
- Menos sensível a outliers:
$$\frac{1}{n}\sum\limits_{i=1}^{n}|f(x_{i})-y_{i}|$$

#### Coeficiente de correlação
- O método menos relativo à média e à escala dos valores
- Acho que é kinda o r^2?
$$\frac{n\sum\limits_{i=1}^{n}(f(x_{i})-\mu_{h})(y_{i}-\mu_{y})}{\sqrt{\sum\limits_{i=!}^{n}(f(x_{i})-\mu_{f})\cdot\sum\limits_{i=1}^{n}(y_{i}-\mu_{y})}}$$

## Bootstrap
- Método geral usado para avaliar precisão estatística
- Bootstraping consiste em estimar certas propriedades do estimador (ex: variância) ao amostrar pontos de uma distribuição.
- Dito de outra forma, bootstraping é um método de *resampling*.
- Uma forma comum de fazer isto é: 
    - pagemos no nosso dataset com $n$ observações.
    - vamos usá-lo e criar vários sets com $n$ observaçõees
    - para isto, vamos sucessivamente ir buscar aleatoriamente pontos ao dataset.
        - Claro, poderemos ter pontos repetidos dentro de um dataset

- Chamemos então $Z$ ao dataset. $Z^{*b}$ será o dataset bootstrap $b$.

- Temos o nosso dataset, $Z$. $S(Z)$ é *qualquer* quantidade calculada com os dados (pode ser a previsão do modelo, por exemplo)
- Ora, bootstrap permite estimar a variância de $S(Z)$ (ou seja, podemos estimar a variância de cada previsão!). Temos:
$$\hat{\text{Var}}[S(Z)]=\frac{1}{B-1}\sum\limits_{b=1}^{B} (S(Z^{*b})-\hat{S}^{*})^{2}$$

- Vejamos agora como estimar o erro de previsão
    - Temos uma versão *optimista*: $\hat{\text{Err}}=\frac{1}{BN}\sum_{b=1}^{B}\sum_{n=1}^{N}L(y_{n},f^{*b}(x_{n}))$. Este método é otimista porque temos os datasets bootstrap a serem o set de treino e o dataset original a ser o set de teste. Este estimador é otimista porque teremos sempre valores em comum entre estes
    - Temos a versão *LOO*: $\hat{\text{Err}}^{(1)}=\frac{1}{N}\sum_{n=1}^{N}\frac{1}{|C^{-i}|}\sum_{b\in C^{-1}}L(y_{n},f^{*b}(x_{n}))$ em que $C^{-i}$ é o conjunto de índices dos conjuntos bootstra que *não* contém a observação $i$
    - Temos ainda uma versão *diferente*: $\hat{\text{Err}}^{(.632)}=0.368\overline{\text{err}}+0.632\hat{\text{Err}}^{(1)}$ 

# Ensembles
## Métodos de fazer Ensembles
Temos:
- Fazer subsampling dos dados
- Manipular os atributos dos inputs
- Manipular os outputs
- Introduzir aleatoriedade

## Averaging de modelos - Bagging
- Usamos bootstrap para melhorar as estimativas e previsões
- Bagging é um tipo de algoritmo que:
    - melhora estabilidade e precisão de modelos de classificação e regressão
    - reduz variância
    - evita overfitting
- Ao aplicar isto a um modelo, perdemos a sua simplicidade
- Em modelos muito estáveis, o bagging não faz muita diferença

*Regressão*
- Para cada conjunto bootstrap $Z^{*b}$, ajustamos o modelo e obtemos a estimativa $f^{*b}(x)$
- A estimativa o Bagging é:
$$f_{bag}(x)=\frac{1}{B}\sum\limits_{b=1}^{B}f^{*b}(x)$$
- Em geral, ao fazer bagging a um previsor de regressão é boa ideia

*Classificação*
- Obtemos na mesma a estimativa $f^{*b}(x)$
- Consideremos esta estimativa como sendo um vetor com 1 um e $K-1$ zeros.
- A estimativa do Bagging será um vetor com $K$ valores $(p_{1},p_{2},\dots,p_{K})$ em que $p_{k}$ é a proporção de modelos que prevê $k$ para $x$. 
- A classe que o Baggin prevê é aquela com mais votos (maior $p_{k}$?)
- Aplicar bagging a um bom classificador melhora-o. Mas aplicar a um mau classificador pode piorá-lo ainda mais.

## Averaging de modelos - Boosting
- Bom com modelos **simples / learners fracos**  (Naive Bayes, regressão logística)
    - Estes têm pouca variância e não têm overfit
    - Mas têm alto bias e não conseguem resolver problemas de aprendizagem mais complexa
- Ora, *boosting* consiste em treinar **muitos learners fracos** e que juntos formam um mais robusto
    - Mais concretamente, podemos juntar vários classificadores fracos, mas que sejam bons em partes diferentes do espaço de inputs.
    - Teremos então um output que consiste na votação dos classificadores componentes.
        - A votação normalmente é pesada: classificadores com maior certeza (probabilidade) têm votos com mais peso e vice-versa.
    - Normalmente, isto tem melhor performance que 1 só classificador fraco.

### AdaBoost
- Pegamos num classificador fraco, corremos várias vezes em datasets de treino e usamos os classificadores treinados votar
- Ou seja, numa iteração $t$:
    - Vemos quão incorretamente cada exemplo foi classificado. Isto será usado para ajustar os pesos dos exemplos
    - Com a previsão desta iteração temos uma hipótese fraca: $h_{t}$
    - Essa hipótese tem uma força: $\alpha_{t}$
- E o classificador final consiste em:
$$H(X)=\text{sign} \left(\sum \alpha_{t}h_{t}(X) \right)$$

**Peso dos exemplos**
- Neste método vamos então, em cada iteração, calcular e ajustar o peso de cada observação. Podemos então definir $D(i)$ o peso do exempo $(\mathbf{x}_{i},y_{i})$
- Podemos ver este peso como sendo: o exemplo $i$ vale por $D(i)$ exemplos
- Isto significa que, em **todos os cálculos** temos que alterar tudo o que consiste em contagens para ter isto em conta:
$$\sum\limits 1(Y_{i}=y)~~~~\to~~~~ \sum\limits D(i)1(Y_{i}=y)$$

**Algoritmo**
1. Começar com os pesos todos iguais a $w_{i}=\frac{1}{N}$
2. Para $M$ passos de boosting, em que $m=1,2,\dots,M$
    1. Ajustar um classificador $G_{m}(x)$ ao set de treino com os pesos $w_{i}$
    2. Calcular o erro de treino: $\text{err}_{m}=\frac{\sum_{i=1}^{N}w_{i}I(y_{i}\neq G_{m}(x_i))}{\sum_{i=1}^{N}w_{i}}$
    3. Calcular a força desta estimativa: $\alpha_{m}=\log(\frac{1-\text{err}_{m}}{\text{err}_{m}})$
    4. Atualizar os pesos: $w_{i}\leftarrow w_{i}\exp (\alpha_{m}I(y_{i}\neq G_{m}(x_{i})))$
3. No final temos: $$G(x)=\text{sign} \left(\sum\limits_{i=1}^{M} \alpha_{m}G_{m}(x) \right)$$
- Adaboost é um modelo "Forward Stage Additive" : sequencialmente vamos adicionando funções à expansão, mas sem alterar aquelas acrescentadas antes.