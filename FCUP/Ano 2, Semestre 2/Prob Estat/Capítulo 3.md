# 3 - Variáveis Aleatórias e Distribuição Binomial e Normal
## 3.1 - Variável Aleatória (VA)
*__EXS:__*
    - X: nº de pontos obtidos no lançamento de um dado
    - Y: nº de crianças numa família escolhida aleatoriamente
    - Z: peso à nascença de um bebé escolhido aleatoriamente

- Temos a experiência aleatória $E$ cujo espaço de resultados é $\Omega$. 
- A _variável aleatória_ $X$ é uma função $X:\Omega\to R$ que a cada elemento de $\Omega$ atribui um número real (sendo que é assim que "transporta" probabilidade). $R_{X}$ é o subconjunto dos números reais que é imagem de $\Omega$ por $X$.
![[variavel aleatoria.png]]

- Consideremos agora que temos $B$, um subconjunto de $R_{X}$.
- A probabilidade de a variável aleatória $X$ apresentar valores em $B$ (para $B\subseteq R_{X}$) é 
$$P(X\in B)=P(A) \quad \quad;\quad \quad A=\{e:X(e)\in B\}$$
![[variavel aleatoria 2.png]]

### Variável Aleatória e População
- Como vimos no início da UC, o objetivo de estatística é estudar caraterísticas das populações. Assim, uma certa caraterística de uma população pode ser identificada como uma variável aleatória e podemos referir-nos à caracterísitica da população apenas como população $$população \longleftrightarrow variável~~X$$
> __*EXEMPLO*__
> Quer-se conduzir um estudo sobre o número de vértebras dos peixes de uma certa espécie num lago dos Estados Unidos. Assim temos:
> _População :_ peixes da espécie nesse lago
> _Caraterística em estudo :_ nº de vértebras
> _X :_ variável aleatória representativa do nº de vértebras de peixes de uma população de peixes desta espécie neste lado

- Há 2 tipos de variáveis aleatórias:
- __Discretas__ - o conjunto dos valores possíveis é finito ou infinito enumerável - Contamos
- **Contínuas** - o conjunto dos valores possíveis é um intervalo ou união de - Medimos

### 3.1.1 - Variáveis Aleatórias Discretas
- O conjunto dos valores possíveis é finito ou infinito enumerável.
- Para uma variável aleatória $X$, a sua _função de probabilidade_ é definida como $$f(x)=P(X=x)$$
- Sendo $D=\{x_{1}, x_{2},\dots\}$ o conjunto ordenado de valores possíveis de $X$ temos que $$o\leq f(x_{i})\leq1 \quad \quad \sum\limits_{i}f(x_{i})=1$$
- A função de probabilidade de uma VA discreta pode ser representada como: tabela, gráfico ou fórmula. Dá a probabilidade de a VA tomar cada um dos valores possíveis. Alguns exemplos:
![[dist probabilidade.png\|425]]            ![[grafico freq.png\|175]]

- Uma VA Discreta pode ser completamente decrita pela sua função de probabilidade.
- Mas podemos usar outros indicadores

#### Média
- AKA esperança matemática AKA valor esperado
- Para uma VA discreta temos que:
$$\textsf{Média} = \mu_{X}=E(X)=\sum\limits_{i} x_{i}P(X=x_{i})$$
#### Variância
- Para uma VA discreta temos:
$$\textsf{Variância} = \large \sigma_{X}^{2}=V(X)=\sum\limits_{i}(x_{i}-E(X))^{2}P(X=x_{i})=E(X^{2})-(E(X))^2$$

#### Desvio padrão
$$\textsf{Desvio padrão} =\sigma_{X}=\sqrt{V(X)}$$

> __NOTA :__ Tendo a função de probabilidade definida, para determinal $E(X^{2})$ aplicamos a fórmula da média, mas com os termos $x_{i}$ ao quadrado. A probabilidade fica igual. Assim: $$E(X^{2})=\sum\limits_{i}x_{i}^{2}P(X=x_{i})$$

> __*EXEMPLO*__
> É proposto um investimento de 20000€ numa pequena empresa. Após um estudo à viabilidade da empres descobriu-se que existe:
> - Probabilidade de 10% de o investimento quadriplicar em 1 ano
> - Probabilidade de 40% de a empresa falir e todo o investimento ser perdido
> - Probabilidade de 50% de se perder 1/4 do investimento
> Assim, podemos fazer uma tabela com o dinheiro após 1 ano ($y$) e a respetiva probabilidade ($f(y)$):
> ![[dist probabilidade ex.png]]
> Temos então: $$E(Y)=-20\times0.4+(-5)\times0.5+80\times0.1=-2.5$$
> Ou seja, o valor médio diz que o mais provável é perder-se dinheiro neste investimento.

### 3.1.2 - Tipos de distribuições de VA discretas

#### 3.2.1.1 - Distribuição Uniforme
- Temos uma VA $X$ que assume valores em $D=\{x_{1},\dots,x_{n}\}$
- $X$ tem uma distribuição _uniforme_ discreta se a função de probabilidade é dad por $$f(x)=\begin{cases} \frac{1}{n}&;\quad x\in D\\ 0 &;\quad x\notin D\end{cases}$$
- Neste caso temos $$E(X)=\mu_{X}= \frac{n+1}{2} \quad ;\quad V(X)=\sigma^{2}_{X}= \frac{n^{2}-1}{12}$$
- Usada quando temos situações com simetria, ou sem situações em que não se justifica considerar simetrias.
- Escreve-se $X\sim U(D)$

#### 3.2.1.2 - Distribuição de Bernoulli
- Quando temos uma experiência aleatória $E$ com 2 resultados possíveis: "Sucesso" ou "Não Sucesso". Isto é uma _Experiência de Bernoulli_
- Tendo a VA $X$ que descreve o nº de ocorrências de Sucesso numa prova da experiência. Temos: $$X=\begin{cases}1 &\textsf{se ocorreu sucesso}\\ 0 &\textsf{se não ocorreu sucesso}\end{cases}$$
- Sendo $S$ o acontecimento "ocorrer Sucesso", tem-se que $P(S)=p \quad; \quad0<p<1$ 
- Logo temos a função de probabilidade:
$$f(X)=\begin{cases}p &se~~~~x=1\\1-p &se~~~~x=0\end{cases}$$
- Neste caso podemos definir a função de probabilidade com uma equação:$$f(x)=p^{x}(1-p)^{1-x} \quad \quad \quad x= 0,1$$
- Daqui temos $$E(X)=\mu_{X}=p \quad \quad;\quad \quad V(X)=\sigma_{X}^{2}=p(1-p)$$
- Escreve-se $X \sim Ber(p)$ 

> __*EXEMPLOS*__
> X: VA que representa o sexo de um indivíduo
> Y: VA que represesnta o fator Rh do sange de um indivíduo (+ ou -)
>
> Para uma variável $Z: f(z)=0.4^{z}0.6^{1-z}~~;~~z=0,1$, temos que $E(Z)=0.4$ e que $V(Z)=0.4\times0.6=0.24$

#### 3.2.1.3 - Distribuição Binomial
- Supondo $n$ ensaios de uma mesma experiência de Bernoulli $E$, feitos de forma independente e idêntica. Para cada ensaio temos 2 possibilidades: sucesso $S$ e insucesso $\bar S$
- Sendo $p \quad; \quad0<p<1$ a probabilidade em cada um dos ensaios. Como os ensaios são independentes e idênticos a probabilidade $p$ é igual em todos.
- Temos a VA $X$ que representa o nº de sucessos nesses $n$ ensaios.
- Temos então:
$$f(x)=P(X=x)=C_{x}^{n}p^{x}(1-p)^{n-x} \quad \quad;\quad x\in \{0,1,2,\dots, n\}$$
de recordar que $\Large C_{x}^{n}= \frac{n!}{x!(n-x)!}$
- Neste caso diz-se que temos uma "distribuição binomial com parâmetros $n$ e $p$"
- Tem-se ainda que $$E(X)=np \quad \quad ;\quad \quad V(X)=np(1-p)$$
- Na prática temos isto:
![[exp gauss.png|275]]
- Escreve-se $X\sim Bi(n, p)$
- Para a distribuição binomial, graficamente temos:
![[dis binomial.png|775]]

#### Quando é que é binomial?
- Tendo uma VA $X$ representativa do número de sucessos de $n$ ensaios de uma experiência aleatória, para $X$ ter uma distribuição binomial tem que satisfazer as seguintes condições:
1. Cada ensaio só pode ter 2 resultados possíveis: sucesso ou insucesso
2. O resultado de cada ensaio é independente dos outros
3. O número de ensaios, $n$, é fixo
4. A probabilidade de ocorrer sucesso, $p$, é igual em todos os ensaios.

### 3.1.2 - Variáveis Aleatórias Contínuas
- O conjunto de valores possíveis é um intervalo (ou reunião de intervalos).
- Neste caso, as probabilidades relacionadas a uma VA contínua $X$ são dadas por uma _função densidade de probabilidade_ $f(x)\geq 0$ tal que, tendo algo como indicado abaixo, para sabermos a probabilidade de ter $a<X<b$ é dada por $$P(a<X<b)=\int\limits_{a}^{b}f(x)dx$$
![[probabilidade em grafico.png|300]]
- Por outras palavras, a probabilidade é dada pela área entre o gráfico de $f$ e o eixo horizontal, no intervalo em estudo.
    - Desta forma facilmente vemos que 
    $$P(-\infty<X<+\infty)=1 \quad;\quad P(X=a)=0$$
    - Vemos também que os limites estarem incluidos ou não é irrevelantes, ou seja $$\small P(a<X<b)=P(a\leq X<b)=P(a\leq X\leq b)=P(a<X\leq b)$$
- Podemos ainda ter algo como na figura abaixo. A área total debaixo de $f$ é 1, portanto ao calcular a área para $1<X<3$ facilmente obtemos $k$:
![[prob em grafico ex.png]]

- Novamente, podemos definir indicadores numéricos.
#### Média
- AKA esperança matemática AKA valor esperado
- Para uma VA contínua $X$ (se existir) temos que:
$$\textsf{Média}=\mu_{X}=E(X)=\int\limits_{-\infty}^{+\infty} xf(x)~dx$$
#### Variância
- Para uma VA contínua $X$ (se existir) temos:
$$\textsf{Variância}=\sigma_{X}^{2}=V(X)=\int\limits_{-\infty}^{+\infty} (x-\mu_{X})^{2}f(x)~dx = E(X^{2})-(E(X))^2$$

#### Desvio Padrão
$$\sigma_{X}=\sqrt{V(X)}$$
#### Propriedades da média e variância
- Para VA contínuas $X,Y$ e constantes $a,b$ temos:
1. $\large E(aX+b)=aE(X)+b$
2. $\large E(aX+bY)=aE(X)+bE(Y)$
3. $\large V(aX+b)=a^{2}V(X)$

- Para VA contínuas _independentes_ $X,Y$  e constantes $a,b$ temos:
1. $\large V(aX+bY)=a^{2}V(X)+b^{2}V(Y)$
2. $\large E(XY)=E(X)E(Y)$

#### Variáveis aleatórias Independentes
- Duas VA $X,Y$ são independentes se quaisquer acontecimentos $A,B$, com $A$ associado a $X$ e $B$ a $Y$, $A$ e $B$ são sempre independentes. Formalmente:
$$P(X\leq a~~~~e~~~~Y\leq b)=P(X\leq a)\cdot P(Y\leq b)$$

### 3.1.3 - Tipos de distribuições de VA contínuas

#### 3.1.3.1 - Distribuição Uniforme
- Quando temos $$f(x)= \begin{cases}\frac{1}{b-a} &a<x<b\\ 0 &x\notin~]a,b[\end{cases}$$
- Neste caso temos
$$\mu= \frac{a+b}{2} \quad \quad ;\quad \quad \sigma^{2}=\frac{(b-a)^{2}}{12}$$

#### 3.1.3.2 - Distribuição Normal
- AKA _Distribuição de Gauss_
- Para uma VA contínua com distribuição normal temos:
$$\large f(x)= \frac{1}{\sigma \sqrt{2\pi}}e^{-\frac{1}{2} \left(\frac{x-\mu}{\sigma} \right)^{2}} $$
sendo $\mu=E(X)$ a média e $\sigma=\sqrt{V(X)}$ o desvio padrão.

- Escreve-se $X\sim N(\mu, \sigma^{2})$ e diz-se "X tem distribuição normal com média $\mu$ e variância $\sigma^{2}$"

#### Gráfico da distribuição normal
![[dist normal.png|500]]
- Assim, 
    - A média indica a posição da distribuição.
    - Quanto menor o desvio padrão, maior será a concentração dos pontos.

- Vemos que é simétrica conforme a média. Ou seja, por exemplo, temos $$P(X\leq \mu-a)=P(X\geq \mu +a)$$
- A única distribuição normal que está tabelada é $\large Z= \frac{X-\mu}{\sigma} \sim N(0,1)$

> __*EXEMPLO*__
> Tendo a distribuição $Z\sim N(0,1)$ queremos calcular $P(-1<Z<0.5)$. Assim:
> $$\begin{align*}P(-1<Z<0.5) &= P(Z<0.5)-P(Z<-1)\\&= P(Z<0.5)-(1-P(~Z<1))\\&= 0.6945+0.8413-1=0.5328\end{align*}$$
> Aqui foram usados estes valores tabelados: 
> ![[dist normal Z.png|350]]

#### Quantil de VA contínua
- O quantil número $p$ (que é uma probabilidade!) de uma VA $X$ é o valor $Q(p)$ (que é um dos valores que X assume!) para o qual $$P(X\leq Q(p))=F(Q(p))=p$$
sendo $F(x)=P(X\leq x)$ a _função de distribução acumulada_ de $X$.

- Por exemplo, sendo $X\sim N(0,1)$ e $p=0.1$ então temos $Q(0.1)=-1.281552$, porque $F(-1.281552)=0.1$
- Ou seja, se $F(a)=b$, então $Q(b)=a$

#### Notação
![[quantil.png]]
- Indicamos $z_{\alpha}$ como sendo o quantil de índice $1-\alpha$.
- Conforme a imagem acima, temos que
$$P(Z<z_{\alpha})=1-\alpha \quad \quad OU \quad \quad P(Z>z_{\alpha})=\alpha$$
- Ou seja, $\Large z_{0.25}$ é o valor de $z$ para o qual a área sob a distribuição é 0.75 da área total.

> NOTA: as 2 distribuições que vêm a seguir só aparecem no PPT do capítulo 4, mas decidi colocá-las aqui, junto das outras distribuições continuas

#### 3.1.3.3 - Distribuição do Qui-Quadrado
- Uma VA $X$ tem distribuição de qui-quadrado com $n$ graus de liberdade se a sua função de densidade for dada por 
$$f(x)=\begin{cases} \frac{1}{2^{\frac{n}{2}}\cdot~ \Gamma(\frac{n}{2})} e^{\frac{-x}{2}}x^{\frac{n}{2}-1} &x>0\\0 &x\leq0 \end{cases}$$
Sendo que $n>0$ e $\Gamma(a)=\int_{0}^{\infty}x^{a-1}e^{-x}dx$. De notar ainda que se $a$ for inteiro, então $\Gamma(a)=(a-1)!$
- Nesta distribuição temos 
$$E(X)=n \quad \quad;\quad \quad V(X)=2n$$
- Escreve-se $X\sim\chi^{2}(n)$ 
![[dist qui quadrado.png|350]]
- Quando $n\to \infty$, a distribuição qui-quadrado tende para distribuição normal

#### 3.1.3.4 - Distribuição t-Student
- Uma VA $X$ tem distribuição de t de Student com $n$ graus de liberdade se a sua função de densidade for dada por 
$$f(x)=\frac{\Gamma \left(\frac{n+1}{2} \right)}{\sqrt{n \pi} ~~\Gamma(\frac{n}{2})}\left( 1 + \frac{x^{2}}{n}\right)^{- \frac{n+1}{2}}$$
- Para esta distribuição:
$$E(X)=0~~se~~n>1 \quad \quad;\quad \quad V(X)=\frac{n}{n-2}~~se~~n>2$$
- Escreve-se $X\sim t(n)$
![[dist t student.png|350]]
- Quando $n\to \infty$, a distribuição t-student tende para distribuição normal

## 3.1.4 - Avaliação da Normalidade
- Vários procedimentos estatísticos baseiam-se em as amostras virem de populações com distribuições normais.
- Assim, é importante testar a normalidade da amostra em estudo.

### Histograma
- Fazer um histograma e sobrepô-lo a uma curva normal mostra-nos se a distribuição se aproxima de normal ou não.

### Regra 68/95/99
- Se $Y$ for uma VA com distribuição normal com média $\mu$ e desvio padrão $\sigma$ temos que $$\begin{align*}
P(\mu-\sigma<Y<\mu+\sigma)&= 0.6827\approx 68\%\\
P(\mu-2\sigma<Y<\mu+2\sigma)&= 0.9545\approx 95\%\\
P(\mu-3\sigma<Y<\mu+3\sigma)&= 0.9973\approx 99\%
\end{align*}$$
- Temos amostra com $n$ observações da variável $Y$. Calculamos $\bar y$ e desvio padrão $s$ para _essa amostra_. De seguida, determina-se as percentagens de observações que estão nos 3 intervalos acima. Se as percentagens se aproximares de 68%, 95% e 99%, então a distribuição poderá ser normal.

### Gráficos de probabilidade normal (gráficos QQ) 
- gráfico que permite comparar a distribuição dos valores da amostra com uma distribuição teórica. Basicamente, para cada valor da amostra calculamos o valor teórico esperado, conforme a distribuição teórica prevista.
- O gráfico fica então com pontos ($x_{i}, y_{i}$) em que $x_{i}$ é um percentil do modelo teório e $y_{i}$ o percentil correspondente da amostra.
- Se a amostra tiver próxima da distribuição esperada, o gráfico irá ser uma reta.
- EX:
![[qq plot.png|300]]

- É de notar que mesmo quando a amostra vem de uma distribuição normal o gráfico QQ pode não ser uma reta perfeitamente alinhada.
- Quando no gráfico vemos que a distribuição _não_ é normal, uma tranformação aos dados pode fazer com que passem a ter uma distribuição normal. 
    - Por exemplo, algumas transformações habitualmente usadas quando a distribuição é enviesada para a direita: $$\sqrt{X} \quad;\quad \log(X) \quad; \quad \frac{1}{X}$$

#prob-estat #matematica