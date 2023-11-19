# 1 - Inferência Estatística
- Ramo da Estatística que consiste em tirar conclusões acerca de uma população a partir de uma amostra da mesma.
- Podemos então fazer uma comparação:
**Probabilidade**
    - Tirar conclusões acerca de um caso particular a partir do conhecimento do caso geral (sabendo que uma moeda é não viciada, qual a probabilidade de se obter caras 17 vezes em 40 lançamentos?)

**Inferência**
    - A partir de casos particular, tirar conclusões acerca do geral (Sendo que se observou 17 caras em 40 lançamentos, o que podemos concluir acerca de a moeda ser viciada ou não?)

- Inferência estatística pode ser dividida em 2 partes:
    - **Estimação** - a partir da análise da amostra, calcular um valor que sirva como aproximação do parâmetro correspondente na população
    - **Testes de Hipóteses**  - A partir da análise da amostra, verificar se certas hipóteses acercas dos parâmetros da população são verdadeiras

## VAs e X - NOTA
- Se a amostragem for aleatória simples com reposição, então as VA $X_{i}$ serão aleatórias e terão a mesma distribuição que $X$.

## Parâmetros
- Quantidades numéricas acerca da população que pretendemos conhecer. Consideremos, por exemplo, que queremos saber a média do peso de pessoas do sexo masculino entre os 20 e 50 anos em Portugal.
- Para uma certa amostra podemos fazer uma *estimativa* da média. Ora, podemos fazer muitas amostras diferentes com a mesma dimensão, ou seja, várias estimativas da média.
- Essas estimativas serão os valores possíveis de uma função dos elementos da amostra: o *estimador*.

# 2 - Estatística
- Uma estatística é uma VA que é função da amostra aleatória: $$Y = f(X_{1}\dots,X_{n})$$
e que não depende de parâmetros desconhecidos.

## Estimação Pontual
- Consideremos que se quer inferir acerca de um parâmetro $\theta$ de uma população a partir de uma amostra.
- Para isso, usamos um estimador $T$ de $\theta$. Um estimador é uma estatística cujo valor para uma amostra particular fornece a estimativa de $\theta$.
- Cada amostra dá um valor a $T$, pelo que obtemos uma estimativa $t$ para cada amostra.
- De notar que às vezes podemos ter estimadores diferentes que nos permitem inferir sobre o mesmo parâmetro

- Por exemplo, consideremos novamente o exemplo anterior, em que se pretende determinar a média de pesos de uma população, $\mu$. Ora, o estimador de $\mu$ para uma amostra $(X_{1},\dots,X_{10})$ iria fazer o calculo $\bar X = \tfrac{1}{10}(X_{1}+\dots+X_{n})$, o que nos dá uma estimativa da média da população.

- A análise de um estimador (e de qualquer estatística) é feita ao observar a distribuição das estimativas obtidas a partir de todas as amostras possíveis com uma certa dimensão constante.
- Ou seja, temos uma *distribuição por amostragem*, sendo que para o estimador $T$ do parâmetro $\theta$ temos a VA $T=f(X_{1},\dots,X_{n})$. A distribuição por amostragem de uma estatística depende de
    - Distribuição da população em si
    - Tamanho da amostra
    - Método de amostragem

EXEMPLO: 
![[distribuicao amostra.png]]

- Ora, distribuições amostrais são precisamente aquilo que vimos no Cap. 4. Temos:
    - **Populações normais**
        - Para uma população com média $\mu$ e variância $\sigma^{2}$, temos $\bar X=\tfrac{X_{1}+X_{2}+\dots+X_{n}}{n}, S^{2}=\tfrac{1}{n-1}\sum_{i=1}^{n}(X_{i}-\bar X)^{2}$ e também: $$\overline X \sim N(\mu,\tfrac{\sigma^{2}}{n}) \quad \quad;\quad \quad \frac{n-1}{\sigma^{2}}S^{2}\sim \chi^{2}(n-1) \quad \quad;\quad \quad \frac{\overline X-\mu}{S/\sqrt{n}} \sim t(n-1)$$
    - **Populações não normais**
        - Se considerarmos um $n$ suficientemente grande, pelo teorema do Limite Central temos: $$\overline X \approx N(\mu, \tfrac{\sigma^{2}}{n} ) \quad \quad;\quad \quad \frac{\overline X-\mu}{S/\sqrt{n}} \approx N(0,1)$$

# 3 - Proporções
- A proporção $p$ de individuos de uma população que possui uma certa caraterística é desconhecida. Considerando-se uma amostra simples com reposição de tamanho $n$ dessa população em que $X$ é a VA representativa do nº de indivíduos da amostra com essa caraterística, em que temos $$X\sim Bi(n,p)$$
- Podemos definir então $P$ a VA representativa da proporção de indivíduos da amostra com essa caraterística, tal que $$P=\frac{X}{n}$$
- Ora, se $n>25$ e $np,n(1-p)>5$ então:
$$P\approx N \left( p, \frac{p(1-p)}{n}  \right) \quad \quad;\quad \quad \frac{P-p}{\sqrt{\frac{p(1-p)}{n}}}\approx N(0,1)$$

# Propriedades de Estimadores
#### Centrado (ou não enviesado)
- Um estimador $T$ do parâmetro $\theta$ é centrado se

$$E(T)=\theta$$
#### Viés
- O viés de um estimador $T$ do parâmetro $\theta$ é dado por $\large E(T)-\theta$

#### Erro Quadratico
- O erro quadrático de um estimador $T$ do parâmetro $\theta$ é dado por
$$EQM(T)=E((T-\theta)^{2})=V(T)-(E(T)-\theta)^{2}$$
- Um estimador é *consistente em média quadrática* se $EQM\to0$ consoante $n$ aumenta.

#### Eficiência
- Tendo 2 estimadores centrados $T_{1},T_{2}$ de $\theta$, $T_{1}$ é *mais eficiente* que $T_{2}$ se $$V(T_{1})<V(T_{2})$$
#### Melhor Estimador
- Uma estimador melhor é aquele que temos
    - Variância reduzida
    - Viés reduzido
    - Centrado de preferência
    - Consistente em média quadrática
- Entre 2 estimadores, escolher o que tem *menor EQM*

### EXEMPLO
> - Queremos determinar a média de uma população.
> - O estimador mais natural será a média amostral $$\bar X = \frac{1}{n}(X_{1}+\dots+X_{n})$$
> - Sendo as VA $X_{i}\dots X_{n}$ idependentes, elas terão a mesma distribuição que a população ($X$). Assim: $E(X_{i})=\mu~~;~~\forall i$
> - Temos que o estimador é centrado: $$E(T)\to E(\bar X)=E\left(\frac{1}{n} (X_{1}+\dots+X_{n}) \right)=\frac{1}{n}E(X_{1}+\dots+X_{n})=\frac{E(X_{1})+\dots+E(X_{n})}{n}=\mu$$
> - Sendo $\sigma^{2}$ a variância da população, temos que $V(X_{i})=\sigma^{2}~~;~~\forall i$
> - Como $\bar X$ é centrado, então EQM=V. Assim, será também consistente em média quadrática $$EQM(\bar X)=V(\bar X)=\frac{\sigma^{2}}{n}\longrightarrow\substack{n\to\infty}\longrightarrow 0$$
> - A média amostral é um *bom estimador*

> No PPT há um exemplo igual ao de cima, mas para o estimador da variância, que também é centrado.

- Temos ainda que estes 2 estimadores ($\bar X,S^{2}$) são *estimadores pontuais*, porque nos dão uma estimativa específica consoante a amostra.

# 4 - Intervalos de Confiança (IC)
- Mesmo tendo um bom estimador, é quase impossível obter uma estimativa igual ao parâmetro que queremos determinar.
- Além disso, com uma estimativa pontual não conseguimos saber o quão próximo do parâmetro desconhecido está a estimativa.
- Ora, intervalos de confiança consistem em, invés de fazer uma estimativa pontual, dar um intervalo de valores que acabam por ser a nossa estimativa.

- Um intervalo de confiança para um parâmetro $\theta$ da população com um grau de confiança de $1-\alpha$ é um intervalo aleatório $]Y_{1},Y_{2}[$ tal que: $$P(\theta\in ]Y_{1},Y_{2}[)=1-\alpha$$
em que $Y_{1},Y_{2}$ são 2 estatísticas construídas a partir de uma amostra aleatória com $Y_{1}<Y_{2}$.
- De notar que numa amostra particular $(x_{1},\dots x_{n})$ não faz sentido falar de probabilidade de $\theta$ estar no intervalo correspondente $]y_{1},y_{2}[$

#### NOTA
$1-\alpha$ - *grau de confiança*
$\alpha$ - *nível de significância*

##### EX
- Se tivermos 
$$P(\theta\in ]Y_{1},Y_{2}[)=0.95$$
(em que $Y_{1},Y_{2}$ são 2 estatísticas construídas a partir de uma amostra aleatória com $Y_{1}<Y_{2}$.)
Isto significa que, considerando todas as amostras aleatórias possíveis de dimensão $n$ e construindo os respetivos intervalos de confiança, então $95\%$ deles contém o parâmetro $\theta$.
- Graficamente, isto seria representado assim:
![[int confianca.png]]

## 4.1 - IC de Média de População Normal com Variância conhecida
- Temos uma população normal ($X\sim N(\mu,\sigma^{2}$), com variância conhecida $\sigma^{2}$ e queremos determinar a sua média $\mu$.
- Sendo as amostras aleatórias temos $X_{i}\sim N(\mu,\sigma^{2})$
- Para estimar a média usamos o estimador $\bar X = \frac{1}{n} (X_{1}+\dots+X_{n})$, tal que $\bar X\sim N(\mu,\frac{\sigma^{2}}{n})$

- Queremos então definir um intervalo centrado na média amostral, ou seja: $]\bar X-a,\bar X+a[~~,~~a>0$
- E pretendemos obter: $P(\mu\in ]\bar X-a,\bar X+a[)=1-\alpha$.
- Podemos escrever isto na forma $P(|\bar X-\mu|<a)=1-\alpha$
- Tendo $\bar X$ uma distribuição normal, fazemos isto:
![[ic 1.png]]

- De seguida, apenas substituimos $\bar X$ por $\bar x$ e ficamos com o *intervalo de confiança*:
$$\left]\bar x - \frac{z_{1-\alpha/2}\sigma}{\sqrt{n}}, \bar x + \frac{z_{1-\alpha/2}\sigma}{\sqrt{n}}\right[$$
com $Z_{1-\alpha/2}$ tal que $P(Z>z_{1-\alpha/2})=1-\alpha/2$, sendo $Z\sim N(0,1)$

- Ou seja, ao usar as médias das amostras $\bar x$ com o IC com grau de confiança $1-\alpha$ para determinar a média da população $\mu$ então o erro máximo que cometemos é $$\frac{z_{1-\alpha/2}\sigma}{\sqrt{n}}$$
que é a nossa **margem de erro**.
- De notar que este intervalo foi determinado a partir do conhecimento da distribuição de probabilidade da VA.

### Variável Fulcral / Pivô para o parâmetro $\theta$
- Nome que se dá a uma função da amostra aleatória e do parâmetro $\theta$ que não depende de outros parâmetros desconhecidos e cuja distribuição é conhecida.
- Por exemplo, no exemplo acima da média o variável fulcral é $\dfrac{\bar X-\mu}{\frac{\sigma}{\sqrt{n}}}$, sendo que $\sigma$ era conhecido.

> **EXEMPLO**
> Vejamos como determinar o intervalo de confiança para um caso específico:
> ![[ic ex1.png]]

## 4.2 - Intervalos e Graus de Confiança 
- Para *diminuir* o IC (mais precisão), mantendo a dimensão da amostra, temos que *diminuir o grau de confiança*
- Para *diminuir* o IC (mais precisão), mantendo o grau de confiança, temos que *aumentar a dimensão da amostra*.

## 4.3 - IC de Média de População Normal com Variância DESconhecida
- A população é normal, ou seja, $X\sim N(\mu,\sigma^{2})$. Assim, as amostras aleatórias serão $X_{i}\sim N(\mu,\sigma^{2})$.
- Como não sabemos $\sigma^{2}$ e queremos estimar $\mu$ usamos a estatística: $$T=\frac{\bar X-\mu}{S/\sqrt{n}}\quad\quad\quad\quad \Biggr| \substack{\bar X= \frac{1}{n}(X_{1}+\dots+X_{n})\\\\S^{2}= \frac{1}{n-1}\sum\limits_{i=1}^{n}(X_{i}-\bar X)^{2}}$$
- Assim, $T$ será a nossa variável fulcral, sendo que $T\sim t(n-1)$
- Desta forma, para determinar o intervalo:
![[ic 2.png]]

## 4.4 - IC da Variância de uma População Normal
- A população é $X\sim N(\mu,\sigma^{2})$ e a amostra $X_{i}\sim N(\mu,\sigma^{2})$
- Como queremos obter a variância usamos o estimador: $$S^{2}= \frac{1}{n-1}\sum\limits_{i=1}^{n}(X_{i}-\bar X)^{2}$$
- Sendo que a variável fulcral será $$Y=\frac{n-1}{\sigma^{2}}S^{2}\sim \chi^{2}(n-1)$$
- Neste caso:
![[ic 3.png]]

### Distribuição Aproximada da Variância Amostral
- Consideremos que temos a amostra aleatória $(X_{1},\dots,X_{n})$ de uma população *normal*. Assim: $X_{i}\sim N(\mu,\sigma^{2})$
- A variável fulcral será $Y = \frac{n-1}{\sigma^{2}}S^{2}\sim \chi^{2}(n-1)$, sendo $E(Y)=n-1~,~ V(Y)=2(n-1)~,~ E(S^{2})=\sigma^{2}~,~V(S^{2})=\frac{2\sigma^{4}}{n-1}$ 
- Para $n$ grandes o suficiente pode tornar-se difícil obter quantis $a,b$ da dist $\chi^{2}(n-1)$, pelo que fazmos $$S^{2}\approx N(\sigma^{2}, \tfrac{2\sigma^{4}}{n-1})$$
- Há um exemplo no PPT

## 4.5 - IC para uma Proporção
- Vejamos isto com um exemplo:

- Numas certas eleições entrevistou-se 1000 eleitores para saber se eram a favor ou contra o candidato A. 350 eram a favor e 650 contra. Queremos encontrar um intervalo com 95% de confiança para a precentagem de eleitores na população favoráveis ao candidato A.
- Neste problema queremos determinar a *proporção* $p$ de eleitores que apoiam o candidato A, a partir de uma amostra de dimensão $n=1000$.

- Sendo $X$ a VA que representa o nº de individuos da amostra que apresenta esta carateristica. Temos $X\sim Bi(n,p)$
- Sendo $\hat{P}=\frac{X}{n}$ a VA representativa da proporção de indivíduos da amostra com essa caraterística.
- Para $n$ elevado temos $X\approx N(np,np(1-p))$. Daí temos: $E(\hat{P})=E(\frac{X}{n})=\frac{1}{n}E(X)=p ~~;~~ V(\hat{P})=V(\frac{X}{n})=\frac{1}{n^{2}}V(X)=\frac{p(1-p)}{n}$

- Pelo que conseguimos obter a variável fulcral
$\hat{P}=\frac{X}{n}\approx N(p, \frac{p(1-p)}{n})\to \frac{\hat{P}-p}{\sqrt{\frac{p(1-p)}{n}}}\approx N(0,1)$
- De onde temos:
![[ic 4.png]]

- No entanto, vemos que este intervalo é aproximado (porque fizemos uma aproximação na distribuição da variável fulcral) e depende da variável desconhecida $p$. 
- Para resolver o último problema temos:
**Método de Wilson**
![[metodo wilson.png]]
- Ou seja, o IC para uma amostra específica com valor observado $\hat{p}$ será $$]C(\hat{p})-a(\hat{p}),C(\hat{p})+a(\hat{p})[$$

Temos outros métodos:
**Método de Wald**
![[metodo wald.png]]

**Método de Agresti-Coull**
![[metodo agresti-coull.png]]

> **EXEMPLO**
> Ao ver um exemplo isto parece menos horrível:
> ![[ic ex2.png]]

> **EXEMPLO 2 - AO CONTRÁRIO KINDA**
> ![[ic ex3.png]]

## 4.6 - IC para a Diferença das médias de 2 populações normais com variâncias conhecidas
- Consideremos que queremos estimar a diferença $\mu_1-\mu_2$ para 2 populações normais com variâncias conhecidas $\sigma_{1}^{2},\sigma_{2}^{2}$. Ora, as populações serão definidas por:
![[2 populacoes normais.png]]
- Definimos então $$D=\bar X - \bar Y$$
Como D é uma combinação linear de duas variáveis normais e independentes, é também uma variável com distribuição normal.
- Temos então $E(D)=E(\bar X-\bar Y)=\mu_{1}-\mu_{2}~,~V(D)=V(\bar X)+V(\bar Y)=\frac{\sigma_{1}^{2}}{n_{1}}+ \frac{\sigma_{2}^{2}}{n_{2}}$ 
pelo que temos $$D\sim N(\mu_{1}-\mu_{2}, \tfrac{\sigma_{1}^{2}}{n_{1}} + \tfrac{\sigma_{2}^{2}}{n_{2}})$$
- Queremos um IC centrado em $D$, ou seja: $]D-a, D+a[$.
- O IC que procuramos cumpre: $P(\mu_{1}-\mu_{2}\in ]D-a,D+a[)=1-\alpha$, ou seja: $P(|D-(\mu_{1}-mu_{2})|<a)=1-\alpha$. Assim:
![[ic dif medias.png]]

## 4.7 - IC para diferença das médias de amostras emparelhadas
- O que temos na secção acima baseia-se nas 2 amostras serem independentes.
- Mas temos casos em que cada observação de uma das amostras está associada a uma observação da outra. 
- Por exemplo, se $X$ for o comprimento do braço direito de um grupo de pessoas e $Y$ o comprimento do braço esquerdo dessas mesmas pessoas (sendo $X_{1},Y_{1}$ da mesma pessoa), estes dados são indicados como $(X_{1},Y_{1})(X_{2},Y_{2})\dots$. Isto é uma *amostra aleatória emparelhada*.

- Neste caso temos $D_{i}=X_{i}-Y_{i}$, sendo que a população é dada por $D=X-Y$.
- Temos $E(D)=\mu_{1}-\mu_{2}$
- Ou seja, o IC de $\mu_{1}-\mu_{2}$ é o IC da média de $D$, que é algo que vimos como calcular atrás.

## 4.8 - IC para diferença entre 2 proporções.
- Tal como atrás, queremos estimar a diferença $p_{1}-p_{2}$ de 2 populações definidas assim:
![[2 populacoes normais prop.png]]
- Como $\hat{P}_{1},\hat{P}_{2}$ são independentes e ambas normais, também a sua diferença será: $$\hat{P}_{1}-\hat{P}_{2} \approx N\left( p_{1}-p_{2}, \frac{p_{1}(1-p_{1})}{n_{1}}+\frac{p_{2}(1-p_{2})}{n_{2}} \right)$$
- Usando o método de Wald da mesma forma que vimos atrás obtemos, para um IC com grau de confiança de $1-\alpha$:
![[ic dif proporcoes.png]]

## 4.9 - IC para parâmetros de populações Não Normais
- Nestes casos podemos usar o Teorema do Limite Central e aproximar as distribuições da média amostral e da diferença entre 2 médias.
- Tendo uma amostra aleatória $(X_{1},\dots X_{n})$ temos $$\bar X = \frac{1}{n} (X_{1}+\dots+X_{n})\approx N(\mu, \tfrac{\sigma^{2}}{n})$$

#### $\sigma^{2}$ conhecida
Temos
$$\frac{\bar{X}-\mu}{\frac{\sigma}{\sqrt{n}}}\approx N(0,1)$$
![[ic media v2.png]]

#### $\sigma^{2}$ desconhecida
![[ic media v3.png]]

#### 2 populações
Temos agora 2 populações do tipo 
![[2 populacoes.png]]
- Neste caso temos~então:
$$\bar X - \bar Y \approx N(\mu_{1}-\mu_{2}, \tfrac{\sigma_{1}^{2}}{n_{1}} + \tfrac{\sigma_{2}^{2}}{n_{2}})$$
##### $\sigma^{2}_{1},\sigma^{2}_{2}$ conhecidas
![[ic dif medias v2.png]]

> **EXEMPLO**
> ![[ic ex4.png]]
> ![[ic ex4.1.png]]

#prob-estat #matematica