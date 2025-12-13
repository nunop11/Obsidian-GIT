# Não estacionaridade - Intro
- Como vimos no início do semestre, um processo é não estacionário se:
    - A sua média variar ao longo do tempo
    - A sua variância variar ao longo do tempo
    - A sua covariância variar ao longo do tempo, e não só com o desfasamento: $\lambda_{yy}(t,s)\neq\lambda_{yy}(t-s)$
- Por outras palavras, um sinal é **não estacionário** se as suas propriedades estatísticas variam!
![[exemplos sinais estacionarios e nao est.png]]
- Em vários casos, podemos facilmente identificar sinais estacionários a olho: parecem "ruído" e mantêm-se muito constantes. Sinais não estacionários variam de forma muito mais "larga" e irregular

## Tendências
Notemos as diferentes tendências:
- *Determinística* - em cada instante é acrescentado um valor ao sinal, vemos acima no traçado verde. Notemos que o sinal parece simplesmente uma reta com ruído. Assim, ao remover esta componente linear com o tempo talvez se obtenha um sinal estacionário.
    - Tendência determinística apenas implica que somamos ao sinal uma função temporal específica, pode ser linear, polinomial, exponencial, etc
    - Dizemos que a média varia de forma determinística
- *Random walk / Integração* - vemos no traçado vermelho. É uma função do tipo $y_{k}=y_{0}+\sum_{i=1}^{k}e_{i}$. A sua variância vai aumentando e obtemos traçados que podem variar de forma muito irregular e imprevisível. Usamos o termo integração porque nestas funções temos um termo integrador (veremos abaixo)
- *Estocástica* - vemos no traçado rosa. Consiste em um sinal em que acrescentamos algum sinal dependente do tempo mas que não é determinístico, é aleatório. Por exemplo, poderíamos acrescentar uma random walk a um sinal estacionário e teríamos algo deste tipo. Dizemos que a média varia de forma aleatória.
![[sinal variacao variancia.png|425]]
- *Oscilação na variância* - este tipo de sinal pode parecer estacionário à vista, mas ao analisar a variância logo detetamos este problema. Claro, podemos ter todo o tipo de variações da variância, não só oscilações. EX: flutuações no mercado
![[sinal com sazonalidade.png|425]]
- *Sazonalidade* - Apesar de ser imprevisível e variar bastante ao longo do tempo, sinais não estacionários podem seguir uma espécie de período. Isto acontece quando uma das componentes da sua função transferência é periódica. EX: consumo elétrico ao longo do tempo
![[sinal com mudanca estrutural.png|425]]
- *Mudanças estruturais* - este é o caso que vemos acima, por alguma razão uma forte perturbação faz o sinal ter um "corte". EX: impacto de uma catastrofe nas vendas de algo

## Autocorrelação e Correlação parcial
- Nas imagens acima vimos sinais não estacionários no domínio do tempo, em que pode ser difícil determinar se um sinal é estacionário a olho.
- Vejamos como ficam sinais estacionários e não estacionários no domínio da ACF e parcorr:
![[acf de estacionario e nao est.png]]
- Na ACF temos uma diferença enorme: a sequência de um sinal não estacionário desce para o zero muito muito devagar, tendo-se um traçado "largo". 
    - Notemos que este traçado mostra $\lambda_{yy}(\tau)$ e, como sabemos, em sinais não estacionários a covariância NÃO depende só do esfasamento. Ou seja, a ACF *não conta a história toda*
- Na correlação parcial é mais difícil, mas podemos notar que no sinal não estacionário temos termos fora do intervalo de confiança ($\tau=8$)
- Para ter em conta que a ACF varia com o tempo, podemos:
    - Segmentar o sinal não estacionário em porções tão pequenas que podemos considerar estacionárias e calcular a ACF
    - Fazer uma janela móvel que vai calculando a ACF e vemos a sua evolução ao longo do tempo

## Testes
- Estes testes são estatísticos e complementam a análise visual do gráfico temporal ou de ACF
- *Dickey-Fuller Aumentado (ADF)* - determina se existem integradores no sinal. Se existirem, temos algo não estacionário
- *Teste de Kwiatkowski-Phillips-Schmidt-Shin (KPSS)* - verifica se existe estacionariedade em torno de uma média constante OU em torno de uma tendência linear
- *Teste de Kruskal-Wallis (KW)* - deteta sazonalidade, ou seja, deteta se os valores variam de forma periódica

# Remover tendências
## Diferenciação
- Por vezes, quando temos integradores, simplesmente diferenciar o sinal torna-o estacionário!
- Mais concretamente, diferenciar consegue remover *tendências estocásticas ou determinísticas*
- Para uma série $y(t)$ definimos diferenciação de 1ª ordem como:
$$\Delta y(t)=y(t)-y(t-1)$$
em que notemos que perdemos 1 ponto por cada diferenciação, já que temos que fazer sempre $\Delta y(1)=y(1)-y(0)$ e não podemos calcular $\Delta y(0)$.
- Podemos generalizar e definir diferenciação de ordem $d$:
$$\Delta^{d}y(t)=(1-q^{-1})^{d}y(t)$$

## Estabilizar variância
- Vejamos métodos que permitem estabilizar sinais em que a variância varia com o tempo:
    - *Transformação logaritmica* - quando a amplitude do sinal aumenta exponencialmente com o tempo. Aplicável a casos com grandes variações de $y(t)$. Esta transformação consiste em: $$y_{tr}(t)=\log(y(t)+c)$$
    - *Transformação por raiz quadrada* - funciona como alternativa a logaritmo. "Corrige" sinais com valores muito reduzidos ou elevados, mas não muito. Consiste em $$y_{tr}(t)=\sqrt{y(t)}$$
    - *Transformação Box-Cox* - abordagem mais geral: $$y_{tr}(t)=\begin{cases}\frac{y^{\lambda}(t)-1}{\lambda}&,&\lambda\neq0\\\log(y(t)) &,&\lambda=0\end{cases}$$ sendo que o parâmetro $\lambda$ é determinado de forma a garantir a estabilização da variância. Para isso, ele deverá minimizar a soma de desvios quadrátidos: $$\lambda=\text{argmin}_{\lambda}[SSE]=\text{argmin}_{\lambda} \left[\sum_{t=1}^{N} \left(y_{tr}(t|\lambda) - \overline{y_{tr}(\lambda)}\right)^{2} \right]$$

## Remover sazonalidade
### Diferenciação sazonal
- Consiste em simplesmente subtrair em cada ponto o valor que está um intervalo $s$ atrás, sendo $s$ o "período" da sazonalidade
- Na realidade, $s$ é o número de pontos/iterações dentro de um ciclo da sazonaliade
- Definimos
$$\Delta_{s}y(t)=y(t) - y(t-s)=(1-q^{-s})y(t)$$

### Decomposição 
- Existem vários métodos, mais simples ou avançados, que permitem decompor o sinal em várias componentes: sazonais, com tendência e de ruído.
- Após esta decomposição, podemos isolar e remover as componentes sazonais, sendo possível estudar o sinal

## Tratar mudanças estruturais
### Divisão em segmentos
- Separamos a série em 2 segmentos: antes e depois do corte. Estudamos cada parte como uma série separada e comparamos resultados
![[sinal com mudanca estrutural 2 - separar.png|500]]

### Modelos
- Alguns modelos já incluem quebras estruturais neles, pelo que configuramos esses modelos para analisar a série
- Um exemplo abaixo mostra o que acontece se tivermos uma quebra, mas em que o sinal não salta, apenas muda de "declive". Neste caso, existe uma variável indicadora do modelo que marca onde temos a quebra:
![[ajuste de sinal com mudanca estrutural.png|500]]

# Modelos não estocásticos
## Integradores I(d)
- Um sinal $y(t)$ é um modelo integrador $I(d)$ se a sua d-ésima diferenciação for estacionária.
- Definimos a $d$ diferenciação como $\Delta^{d}y(t)=(1-q^{-1})^{d}y(t)$

## ARIMA
- Isto é um modelo ARMA com um integrador:
$$A(q^{-1})\Delta^{d}y(t)=C(q^{-1})e(t)$$
em que:
    - $A(q^{-1})=1+a_{1}q^{-1}+\dots+a_{n}q^{-n}$ é o polinómio AR
    - $C(q^{-1})=1+c_{1}q^{-1}+\dots+c_{m}q^{-m}$ é o polinómio MA
    - $e(t)$ é ruído branco $N(0,\sigma^{2})$
    - $\Delta^{d}$ é uma diferenciação de ordem $d$. Faz com que o termo integrador tenha ordem $d$

- Consideremos um **exemplo** ARIMA(1,1,1)
    - Neste caso temos $n=m=d=1$
![[sinal arima.png]]
- Nos 3 casos:
    - A ACF é muito larga e demora imenso a chegar a zero
    - Ao diferenciar obtemos sinais aparentemente estacionários, diferentes para cada realização

## Modelos com sazonalidade - SARIMA
- Isto é um modelo ARIMA em que introduzimos componentes AR,MA sazonais:
$$A(q^{-1})A_{s}(q^{-s})\Delta^{d}\Delta_{s}^{D}y(t)=C(q^{-1})C_{s}(q^{-s})e(t)$$
- Em que temos:
    - $A,C,\Delta^{d}$ iguais ao que vimos acima
    - $A_{s}(q^{-s})=1+a_{1}q^{-s}+\dots+a_{n}q^{-ns}$ é um polinómio AR que apenas afeta termos com sazonalidade $s$
    - $C_{s}(q^{-s})=1+c_{1}q^{-s}+\dots+c_{m}q^{-ms}$ é um polinómio MA que apenas afeta termos com sazonalidade $s$
    - $\Delta_{s}^{D}$ é um termo de derivada de ordem $D$, aplicado com sazonalidade $s$. Isto quer dizer que temos o integrador sazonal $I_{s}(D)$

### Exemplo
- Vejamos um **EXEMPLO** $SARIMA(1,0,1)(1,1,1)_{12}$ 
    - Notemos que temos um sistema com $n=m=1$, não temos integrador não sazonal. Temos uma componente sazonal com $N=M=D=1$, com período $s=12$
- Temos:
$$\begin{align*}
A(q^{-1})&= 1-0.5q^{-1}\\
A_{s}(q^{-s})&= 1-0.3q^{-12}\\
C(q^{-1})&= 1+0.4q^{-1}\\
C_{s}(q^{-s})&= 1+0.2q^{-12}\\
d=0\\
D=1
\end{align*}$$
logo
$$(1-0.5q^{-1})(1-0.3q^{-12})(1-q^{-12})y(t)=(1+0.4q^{-1})(1+0.2q^{-12})e(t)$$
- Podemos reescrever como:
$$\begin{align*}
y(t)&= \frac{1}{1-q^{-12}}\frac{1+0.2q^{-12}}{1-0.3q^{-12}}\frac{1+0.4q^{-1}}{1-0.5q^{-1}}e(t)\\
&= \frac{1}{\Delta^{D}_{s}}\frac{C_{s}(q^{-12})}{A_{s}(q^{-12})}\frac{C(q^{-1})}{A(q^{-1})}e(t)\\
&= H_{1}(q)H_{2}(q)H_{3}(q)e(t)
\end{align*}$$
ou seja, podemos escrever SARIMA como um sistema linear com 3 subsistemas em série.
- Ao realizar/simular o sistema temos
![[sinal sarima.png|375]]![[acf de sarima.png|375]]

## Modelos com tendência determinística
- Uma forma de modelar este tipo de modelos é com modelos de *regressão com tendência*
- Por exemplo, quando temos uma componente linear determinística:
$$y(t)=\beta_{0}+\beta_{1}t + e(t)$$
em que o modelo é representado pelos parametros de ajuste $\beta_{i}$

## Modelos com mudança estrutural
- Estes sistemas podem simplesmente ser representados como 2 sistemas distintos, com funções transferência distintas, dos 2 lados do corte
$$y(t)=\begin{cases}
H_{1}(q^{-1})e(t) & , & t>T_{C} \\
H_{2}(q^{-1})e(t) & , & t\le T_{C}
\end{cases}$$

# Estimação ARIMA
1. Diferenciar a série $\Delta^{d}y(t)$ de forma a remover a componente integradora. Ficamos com um sinal estacionário
2. Identificar a ordem AR e MA, através de ACF ou PACF
3. Estimar os parâmetros como fazíamos antes

# Estimação SARIMA
1. Fazer diferenciação sazonal $\Delta_{s}^{D}y(t)$ de modo a remover a componente sazonal
2. Separamos as sub-séries: dividimos $y(t)$ em $s$ sub-séries, em que cada uma corresponde a um ciclo do sinal sazonal: $$y_{1}(k)=y(ks)~,~y_{2}(k)=y(ks+1)~,~\dots~,~y_{s}(k)=y(ks+s-1)$$
3. Usando **todas** as sub-séries, estimamos os parâmetros sazonais de e $A_{s},C_{s}$. Quanto melhor for a periodicidade, melhor será a estimativa deste passo
4. Com os parâmetros e $s$, temos um modelo sazonal ajustado. Calculamos os resíduos do modelo sazonal ajustado, combinando todas as sub-séries em 1 série não sazonal: $$e(t)=y(t)-\hat{y}(t)$$ pelo que deveremos ter $e(t)$ um sinal ARIMA
5. Modelar o sistema não sazonal. Fazer o mesmo que acima para analisar este sinal e obter os parametros todos

## Estimar polinómio sazonal - EX numérico
- Consideremos a série $y(t)$ com periodo $s=3$ que tem uma componente AR sazonal:
$$A_{s}(q^{-s})=1+a_{s1}q^{-3}$$
**1.** Começamos por dividir $y(t)$ em 3 sub-séries (porque $s=3$), em que:
$$\begin{align*}
y_{1}(t)&= y(3t-2) &&,&& t=1,\dots,\text{int}(N/3)\\
y_{2}(t)&= y(3t-1) &&,&& t=1,\dots,\text{int}(N/3)\\
y_{3}(t)&= y(3t)   &&,&& t=1,\dots,\text{int}(N/3)
\end{align*}$$
**2.** Deginimos os regressores
$$\Phi=\begin{bmatrix}-y(1) \\ -y(2) \\ -y(3) \\ -y(4) \\ -y(5) \\ -y(6) \\ \vdots \\ -y(N-5) \\ -y(N-4) \\ -y(N-3) \end{bmatrix}=\begin{bmatrix}-y_{1}(1) \\ -y_{2}(1) \\ -y_{3}(1)  \\ -y_{1}(2) \\ -y_{2}(2) \\ -y_{3}(2) \\ \vdots \\ -y_{1}(\text{int}(N/3)-1) \\ -y_{2}(\text{int}(N/3)-1) \\ -y_{3}(\text{int}(N/3)-1) \end{bmatrix}$$
**3.** Definimos as observações:
$$Y=\begin{bmatrix}y(4) \\ y(5) \\ y(6) \\ y(7) \\ y(8) \\ y(9) \\ \vdots \\ y(N-2) \\ y(N-1) \\ y(N) \end{bmatrix}=\begin{bmatrix}y_{1}(2) \\ y_{2}(2) \\ y_{3}(2)  \\ y_{1}(3) \\ y_{2}(3) \\ y_{3}(3) \\ \vdots \\ y_{1}(\text{int}(N/3)) \\ y_{2}(\text{int}(N/3)) \\ y_{3}(\text{int}(N/3)) \end{bmatrix}$$
**4.** Estimar parâmetros
$$\hat{a}_{s1}=(\Phi^{T}\Phi)^{-1}\Phi^{T}Y$$
**5.** Calcular resíduos:
$$e(kT+i-1)=e_{i}(k)=y_{i}(k) + \hat{a}_{s1}y_{i}(k-1)~~~~~~\Biggr|~ \begin{matrix}i=1,2,3~~~~~~~~~~~~~~~~~ \\ k=1,\dots,\text{int}(N/3)\end{matrix}$$
**6.** Estimar os polinómios não sazonais, considerando que os resíduos seguem uma série ARIMA. Isto faz-se de forma "fácil"

# Testes de estacionaridade
## Dicley-Fuller Aumentado (ADF)
- Este teste consiste em testar:
    - $H_{0}:$ a série **não é estacionária** (e tem raiz unitária)
    - $H_{1}:$ a série *é estacionária*

- Este teste usa o modelo AR aumentado:
$$\Delta y(t)=\alpha+\beta t+\gamma y(t-1) + \sum\limits_{i=1}^{p}a_{i}\Delta y(t-i)+e(t)$$
- Ou seja, estamos a igualar a derivada ordem 1 do sinal $y$ a um sistema AR aumentado
- Este sistema AR aumentado tem:
    - uma parte AR normal em $\sum a_{i}\Delta y(t-i)$
    - $\gamma$ que carateriza a raiz unitaria
    - $e(t)\sim N(0,\sigma^{2})$ é ruído branco
    - $\alpha$ uma constante
    - $\beta t$ um termo com tendência deterministica (opcional)

- Definimos a **estatística do teste**:
$$\tau=\frac{\hat{\gamma}}{\text{std}(\hat{\gamma})}$$
em que $\hat{\gamma}$ é a estimativa LSQ que obtemos para $\gamma$. 

### Obter os parâmetros
- A equação AR aumentada é linear nos seus parâmetros, logo fazemos
$$\hat{\theta}=(\Phi^{T}\Phi)^{-1}\Phi^{T}Y$$
em que
    - $\theta=\begin{pmatrix}\alpha & \beta & \gamma & a_{1} & a_{2} & \cdots & a_{p}\end{pmatrix}^{T}$
    - $\Phi=\begin{pmatrix}\phi(1) & \phi(2) & \cdots & \phi(N) \end{pmatrix}$
    - $\phi(t)=\begin{pmatrix} 1 & t & y(t-1) & \Delta y(t-1) & \cdots & \Delta y(t-p) \end{pmatrix}$
    - $Y=\begin{pmatrix}\Delta y(1)  & \Delta y(2) &  \cdots & \Delta y(N) \end{pmatrix}$
logo teremos $$\hat{\gamma}=\hat\theta_{3}$$
- Temos a covariãncia de $\hat{\theta}$ é $P=(\Phi^{T}\Phi)^{-1}\sigma^{2}$ 
- A variância $\sigma^{2}$ é estimada:
$$\hat{\sigma}^{2}=\frac{1}{N}(Y-\Phi\hat{\theta})^{T}(Y-\Phi\hat{\theta})$$
- O desvio padrão de $\hat{\gamma}$ vai ser a raiz quadrada do elemento da diagonal de $P$ correspondente a $\gamma$:
$$\text{std}(\hat{\gamma})=\sqrt{\hat{\sigma}^{2} \cdot [(\Phi^{T}\Phi)^{-1}]_{3,3}}$$
Se $H_{0}$ for verdade, $\tau$ não segue nenhuma distribuição padrão. Assim, os valores críticos foram tabelados e calculados com simulações de Monte Carlo, dependendo do tamanho da amostra $N$ e da presençã de termos $\alpha$ e $\beta t$.

### Procedimento do teste ADF
- **1.** Especificar o modelo - Decidir se o modelo inclui os termos $\alpha,\beta t$
- **2.** Estimar os parâmetros - Ajustamos o modelo AR aumentado com método LSQ como vimos acima
- **3.** Calcular a estatística - Utilizar o $\hat{\gamma}$ como vimos acima
- **4.** Comparar $\tau$ com os valores críticos tabelados
- **5.** Decidir:
    - Se $\tau<\text{valor critico}$ rejeitamos $H_{0}$ e temos um sinal estacionário
    - Se $\tau\ge\text{valor critico}$ não rejeitamos $H_{0}$ e temos um sinal não estacionário

### Valores críticos
![[valores criticos acf.png]]

## Teste KPSS
**Teste de Kwiatkowski-Philips-Schmiedt-Shin**
- Avalia se um sinal *é* estacionário, mas temos **ao contrário do ADF**: 
    - $H_{0}:$ A série **é estacionaria** em torno de uma constante ou tendência linear
    - $H_{1}:$ A série não é estacionária

- O teste KPSS considera que a serie pode ser escrita como uma série estacionária $y(t)$, uma constante $\beta_{0}$ e uma tendência determinística $\beta_{1}t$:
$$y(t)=\beta_{0}+e(t) \quad \quad \text{OU} \quad \quad y(t)=\beta_{0}+\beta_{1}t+e(t)$$
### Estatística
- Definimos a estatística:
$$\eta=\frac{1}{N^{2}} \sum\limits_{t=1}^{N} \frac{S^{2}(t)}{\hat{\sigma}^{2}}$$

- O $S(t)$ é a soma cumulativa de todos os resíduos $\hat{e}(k)$ até ao $t$:
$$S(t)=\sum\limits_{k=1}^{t}\hat{e}(k)$$
em que estes resíduos $\hat{e}(k)$ são os resíduos do ajuste feito com a tendência ou tendência+constante.

- Podemos estimar a variância $\hat{\sigma}^{2}$ do erro $e(t)$, calculada através da densidade espectral:
$$\hat{\sigma}^{2}=\hat{\Phi}_{\hat{e}\hat{e}}(e^{j0})=\hat{\lambda}_{\hat{e}\hat{e}}(0) + \sum\limits_{\tau=1}^{\tau_{max}}\omega(\tau,\tau_{max})\hat{\lambda}_{\hat{e}\hat{e}}(\tau)$$
em que definimos a *função triangular de Bartlett*:
$$\omega(\tau,\tau_{max})=1 - \frac{\tau}{\tau_{max}+1}$$
e temos a estimativa da autocovariância obtida com os resíduos:
$$\hat{\lambda}_{\hat{e}\hat{e}}(\tau)=\frac{1}{N} \sum\limits_{t=\tau+1}^{N}\hat{e}(t)\hat{e}(t-\tau)$$

### Interpretação do teste
- Novamente, comparamos a estatística aos valores críticos tabelados e obtidos por simulações de Monte Carlo. Temos que:
    - Se $\eta<\text{valor critico}$ NÃO rejeitamos $H_{0}$ e a série **é estacionária**
    - Se $\eta\ge \text{valor critico}$ rejeitamos $H_{0}$ e a série é *não estacionária*

### Valores críticos
- Para o caso em que temos o modelo em torno de uma constante:
![[valores criticos kpss.png]]

- E para em torno de uma tendência linear:
![[valores criticos kpss 2.png]]

- Muitas funções e métodos MATLAB ou Python assumem logo estes valores e indicam-nos ao fazer o teste.

# Teste de Sazonalidade
## Teste de Kruskal-Wallis
- Ele testa sazonalidade:
    - $H_{0}:$ não há diferença entre os períodos -- a série **não tem sazonalidade**
    - $H_{1}$: há diferenças entre os períodos -- a série **tem sazonalidade**

### Estatística
$$H = \frac{12}{N(N+1)} \sum\limits_{i=1}^{k}n_{i}(\overline{R}_{i}- \overline{R})^{2}$$
em que temos:
    - $N$ o número de observações
    - $k$ é o número de períodos ou ciclos
    - $n_{i}$ é o número de observações no período $i$
    - $\overline{R}_{i}$ é a média dos *postos* no período $i$ 
    - $\overline{R}$ é a média global dos postos

- Se $H_{0}$ for verdade, teremos: $$H\sim \chi^{2}(k-1)$$
pelo que os valores críticos podem ser calculados diretamente porque temos uma distribuição padrão.

### Procedimento
- **1.** Organização de dados - dividimos a série temporal total (com os períodos todos) em $k$ grupos/sub-séries com base nos períodos. Por exemplo, cada grupo é um dia ou mês ou ano
- **2.** Ordenar os postos - ordenar a série temporal total e atribuir postos (posto $R_{i}=1$ é o valor mais baixo, $R_{i}=2$ o 2º maior, etc) a cada valor
- **3.** Calcular as médias dos postos em cada grupo/sub-série: $$\overline{R_{i}}=\frac{\sum R_{i}}{n_{i}}$$
- **4.** Calcular a estatística $H$ com a fórmula acima
- **5.** Comparar $H$ com os valores críticos da distribuição $\chi^{2}(k-1)$
- **6.** Decidir: rejeitamos $H_{0}$ se $H>\text{valor crítico}$ e **temos sazonalidade**
