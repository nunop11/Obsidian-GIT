# 4 - Distribuições por Amostragem
- Os capítulos 1 a 3 permitem-nos analisar dados. Este capítulo permite fazer a transição dos dados recolhidos para _Inferência Estatística_

- De uma certa população temos a média $\mu$  e o desvio padrão $\sigma$
- Para uma amostra aleatória com $n$ elementos temos média $\bar x$ e desvio padrão $s$
- Se fizermos várias amostras aleatórias teremos médias $\bar x_{1}, \bar x_{2}, \dots$

- À distribuição de probabilidade da variável aleatória $\bar X$, composta pelas médias de $n$ amostras, chamamos de __Distribuição por amostragem__

- De uma forma mais geral, uma VA cujos valores dependem da amostra aleatória é uma **Estatística**. 
- Uma **Distribuição por amostragem** é uma distribuição de probabilidade de uma estatística.

## 4.1 - Média amostral
- Para uma amostra aleatória $(X_{1}, X_{2}, \dots, X_{n})$ podemos obter a média, que por sua vez é uma VA, a **Média amostral**, dada por:
$$\bar X=\frac{X_{1}+X_{2}+\dots+X_{n}}{n}= \frac{1}{n}\sum\limits_{i=1}^{n}X_{i}$$
> __*EXEMPLO*__
> - Temos a população $X=\{1,2,3,4,6\}$
> - Se selecionarmos uma amostra aleatória $(X_{1},X_{2})$ teremos a média amostra: $$\bar X=\frac{X_{1}+X_{2}}{2}$$
> - Ora, a amostra pode ter 25 combinações de valores da população (alguns pares repetidos) e as médias obtidas variam bastante. Temos isto:
> ![[media amostral.png|300]]
> - Sendo que facilmente se determina que a distribuição por amostragem de $\bar X$ é:
> ![[exemplo.png]]
> - Podemos já verificar que a média de $\bar X$ é a média da população ($E(\bar X)=\mu$)

### Notas gerais
- Tendo-se $\bar X$, a média amostral de uma amostra de tamanho $n$, retirada de uma população com média $\mu$ e desvio padrão $\sigma$, temos que
$$\mu_{\bar X}=E(\bar X)=\mu$$
$$\sigma_{\bar X}=\sqrt{V(X)}=\frac{\sigma}{\sqrt{n}}$$
- Tem-se ainda que se a população original tiver distribuição normal, também $\bar X$ terá distribuição normal. Verifica-se:
![[media amostral dist.png]]
- Vemos que quanto maior foi o tamanho das amostras usadas para obter a média amostral, menor será a variebilidade de $\bar X$ e maior é a concentração dos valores em torno da média da população. Por outras palavras, quanto maior for $n$, mais provável será $\bar X$ assumir valores próximos a $\mu$

### 4.1.1 - Teorema do Limite Central
- Teorema que usamos se a população não tem distribuição normal:
> Se o tamanho da amostra $n$ for "grande", então a média amostral $\bar X$ tem distribuição _aproximadamente normal_.

- Tendo VA independentes e distribuidas identicamente $X_{1},X_{2},\dots, X_{n}$, com média $\mu$ e variância $\sigma^{2}$. Definindo $S_{n}=X_{1}+X_{2}+\dots+X_{n}$ temos
$$\lim_{n\to\infty}P \left(a\leq \frac{S_{n}-n\mu}{\sqrt{n}\sigma}\leq b\right)=\frac{1}{2\pi} \int_{a}^{b}e^{\frac{u^{2}}{2}du}~~~~~~,~~a<b$$
- Se $n$ for suficientemente grande teremos $S_{n}\sim N(n \mu, n \sigma^{2})$, pelo que$$\bar X\sim N \left(\mu, \frac{\sigma^{2}}{n}\right)$$
- O "suficientemente grande" acima depende do quão próximo da distribuição normal a população está, mas nesta UC iremos considerar que é suficiente ter:
$$\huge n\geq 30$$
- De notar que este princípio _também se aplica a distribuição Binomial_ para $n$ grande, de modo que podemos aproximar uma distribuição $Bi(n,p)$ a uma distribuição normal em que:$$\mu=np \quad \quad;\quad \quad \sigma=\sqrt{np(1-p)}$$

>__*EX*__
> -  O comprimento média dos insetos de uma determinada espécie é 15mm, sendo que o respetivo desvio padrão é 3 mm. Qual a probabilidade de uma amostra aleatória de 64 destes insetos ter um comprimento médio inferior a 10mm?
> __*Resolução*__
> - Temos 2 variáveis:
>     - $Y:$ VA que representa o comprimento em mm de 1 inseto, sendo $\mu_{Y}=15 \quad;\quad \sigma_{Y}=3$
>     - $\bar Y:$ VA representativa da média dos comprimentos em mm de 64 insetos selecionados aleatoriamente
> - Pelo limite do Limite Central temos que $\bar Y$ tem distribuição aproximadamente normal, ou seja, $$\bar Y\sim N \left(15, \frac{3^{2}}{64}\right)=N \left(15, \left(\frac{3}{8} \right)^2 \right)=N(15, 0.375^{2})$$
> - Ou seja, $$P(\bar Y<10)\cong P \left(\frac{\bar Y-15}{0.375}< \frac{10-15}{0.375} \right)=P(Z<-13.33)\approx 0$$
> - Portanto, a probabilidade é aproximadamente 0

## 4.2 - Proporção Amostral
- Como vimos, a média amostral é quantitativa e, como tal, só está definida quando a caraterística em estudo é mensurável.
- Para caraterísticas representadas por uma variável categórica, usamos _proporções_.
- Consideremos então variáveis categóricas em que há 2 possibilidades: sucesso (1), com probabilidade $p$, e insucesso (0), com probabilidade $1-p$ (EX: género de uma pessoa de uma certa população.)
- Tal como fizemos atrás com a média, podemos então ter várias amostras, de forma a ter uma nova VA: $\hat{P}$, a **Proporção amostral**, que assume os valores: $\hat{p}_{1}, \hat{p}_{2},\dots, \hat{p}_{j}$

- A proporção amostral $\hat{P}$ de sucessos em amostras de tamanho $n$ _é na realidade um média amostral_, uma vez que se definirmos os sucessos como 1 e os insucessos como 0, a proporção é a soma desses 0s e 1s a dividir por $n$, uma média.

- Tendo em conta o que foi dito acima, sendo $Y$ a VA representativa do número de sucessos numa amostra de tamanho $n$ então temos
$$\hat{P}=\frac{Y}{n}$$
- Como $Y\sim B(n,p)$ tem-se $u_{Y}=np$, $\sigma_{Y}^{2}=np(1-p)$ (Temos uma experiência de Bernoulli que segue todos os requisitos, daí ser binomial)

- Assim, temos
#### Média
$$\mu_{\hat{P}}=E(\hat{P})=p$$
#### Desvio padrão
$$\sigma_{\hat{P}}=\sqrt{\frac{p(1-p)}{n}}$$

- Tal como no caso da média, pelo Teorema do Limite Central, para $n$ suficientemente grande, $\hat{P}$ tem distribuição aproximadamente normal, ou seja:
$$n>30 \longrightarrow \hat{P}\sim N \left(p, \frac{p(1-p)}{n}\right)$$

> __*EXEMPLO*__
> - Um certo cruzamento entre plantas de ervilha doce tem probabilidade de 0.56 de produzir descendência com flores roxas e 0.44 de produzir de descendência com flores brancas
> - Vai-se selecionar 100 descendentes desse cruzamento aleatoriamente. Qual a probabilidade de a proporção de plantas com flores roxas ser inferior a 0.5?
>
> - Temos $\hat{P}$: VA que representa a proporção de plantas com flores roxas numa amostra de 100 plantas selecionadas de forma aleatória
> - Como $n=100>30$, então a VA tem distribuição aproximadamente normal. Assim, como $p=0.56$, temos $$\sigma_{\hat{P}}=\sqrt{\frac{p(1-p)}{n}}\approx 0.05$$
> - Logo, $\hat{P}\sim N(0.56, 0.05^{2})$
> - E podemos calcular a probabilidade que queremos: $$P(\hat{P}<0.5)\cong P \left( \frac{\hat{P}-0.56}{0.05}<\frac{0.05-0.56}{0.05}\right)=P(Z<-1.2)\approx 0.12$$

## 4.3 - Correção de Continuidade
- Para aproximar melhor uma distribuição discreta (ex: Binomial) a uma contínua (ex: Normal) é comum usar-se _correção de continuidade_, que consiste em associar um intervalo contínuo a cada valor da variável discreta. 

### Binomial $\to$ Normal
- Como já vimos, se $n>30$ podemos aproximar uma variável $Y$ com distribuição binomial a uma distribuição normal, ficando com $\mu=np ~~~~;~~~~ \sigma=\sqrt{np(1-p)}$ . Assim temos:
$$\frac{Y-np}{\sqrt{np(1-p)}}\sim N(0,1)$$
- Assim, para obter uma melhor aproximação devemos fazer:
![[aprox a dist normal.png]]
(A parte de fazer $\pm0.5$ é a "correção de continuidade" de Fisher e fornece uma aproximação ligeiramente mais precisa. Especialmente útil quando $n$ não é muito grnade)

>__*EXEMPLO*__
> - O tempo de vida em anos dos indivíduos de uma determinada espécie segue uma distribuição normal de média 10 e desvio padrão 3.7
> - Qual a probabilidade de num grupo de 200 indíviduos escolhidos aleatoriamente pelo menos 50 estarem vivos até ao final de 12 anos?
>
> - Temos $X$: VA que representa o tempo de vida dos indivíduos da espécie
>     - Assim $X\sim N(10, 3.7^{2})~~~~;~~~~P(X\geq 12)\approx0.2946$
> - Temos também $Y$: VA que representa o número de indivíduos (dos 200 escolhidos) que estão vivos ao fim de 12 anos. 
>     - Temos: $Y\sim Bi(200, p)~~~~;~~~~p=P(X\geq12)\approx0.2946$
>     - Como $n=200>30$ temos $$\frac{Y-200p}{200p(1-p)}\sim N(0,1) \Longrightarrow \frac{Y-58.92}{\sqrt{41.5892}}\sim N(0,1)$$
> - Assim $$P(Y\geq50)=P(Y>49.5)=P \left(\frac{Y-58.92}{\sqrt{41.5892}} > \frac{49.5-58.92}{\sqrt{41.5892}}\right)\approx = 1-P(Z\leq-1.46)\approx 0.9279$$

## 4.4 - Variância Amostral
- Da mesma forma que ao ter $n$ amostras de uma certa população temos $n$ médias e $n$ proporções, podemos ver que temos também _n variâncias_
- Ou seja, ao fazer várias amostras aleatórias de tamanho $n$, temos uma nova VA: $S^{2}$, a _variância amostral_, que apresenta valores: $s_{1}^{2}, s_{2}^{2}, \dots, s_{j}^{2}$

- Tendo-se a amostra $(X_{1}, X_{2}, \dots, X_{n})$ de uma população com distribuição normal $X\sim N(\mu, \sigma^{2})$, a variância amostral é dada por:
$$S^{2}=\frac{1}{n-1}\sum\limits_{i=1}^{n} (X_{i}-\bar X)^{2}$$
- Temos que $$E(S^{2})=\sigma^{2}$$

## 4.5 - Populações Normais – Distribuições por amostragem
- Tendo-se uma amostra $(X_{1}, X_{2},\dots, X_{n})$ uma amostra aleatória de uma população normal $X\sim N(\mu, \sigma^{2})$
- Sendo $$\bar X=\frac{1}{n}\sum\limits_{i=1}^{n}X_{i} \quad \quad; \quad \quad S^{2}=\frac{1}{n-1}\sum\limits_{i=1}^{n} (X_{i}-\bar X)^{2}$$
- Então temos
$$\frac{\bar X-\mu}{\frac{\sigma}{\sqrt{n}}}\sim N(0,1) \quad \quad;\quad\quad \frac{\bar X-\mu}{\frac{S}{\sqrt{n}}}\sim t(n-1) \quad \quad ;\quad \quad \frac{n-1}{\sigma^{2}}S^{2}\sim \chi^{2}(n-1)$$

## 4.6 - Populações Não Normais – Distribuições por amostragem
- Seja $(X_{1},X_{2},\dots,X_{n})$ uma amostra aleatória de uma população com média $\mu$ e variância $\sigma^{2}$
- Sendo $$\bar X=\frac{1}{n}\sum\limits_{i=1}^{n}X_{i} \quad \quad; \quad \quad S^{2}=\frac{1}{n-1}\sum\limits_{i=1}^{n} (X_{i}-\bar X)^{2}$$
- Temos:
$$\frac{\bar X-\mu}{\frac{\sigma}{\sqrt{n}}}\sim N(0,1) \quad \quad;\quad \quad \frac{\bar X-\mu}{\frac{S}{\sqrt{n}}}\sim N(0,1)$$

#prob-estat #matematica