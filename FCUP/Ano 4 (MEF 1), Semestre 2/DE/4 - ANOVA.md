- Derivado por RA Fisher ao estudar dados de agricultura nos 1920s
- Muito usado para analisar dados experimentais
- Usado para testar hipoteses de K médias: $$H_{0}:\mu_{1}=\mu_{2}=\dots=\mu_{K}$$
na prática, isto é um caso particular do modelo linear, que veremos depois
- No início da UC vimos t-test a comprar 2 médias. ANOVA permite comparar >2 médias

## Os Dados
- Consideremos que temos $K$ amostras aleatórias de populações gaussianas de variância $\sigma^{2}$. Temos:
$$\begin{align*}
Y_{1}&= (Y_{11},Y_{12},\dots,Y_{1n_{1}}) \quad;\quad Y_{1j}\sim \text{N}(\mu_{1},\sigma^{2})\\
Y_{2}&= (Y_{21},Y_{22},\dots,Y_{2n_{2}}) \quad;\quad Y_{2j}\sim \text{N}(\mu_{2},\sigma^{2})\\
&\dots\\
Y_{K}&= (Y_{K1},Y_{K2},\dots,Y_{Kn_{K}}) \quad;\quad Y_{Kj}\sim \text{N}(\mu_{K},\sigma^{2})\\
\end{align*}$$
- Queremos então testar $H_{0}:\mu_{1}=\mu_{2}=\dots=\mu_{K}$, em que $H_{1}:\text{pelo menos 2 médias são diferentes}$

### Primeira ideia
- Uma possibilidade seria comparar (com t-tests) as amostras 2 a 2. Isso parece OK mas aumenta muito a chance de erros
    - Consideremos que para cada para testamos $H_{0}^{ij}:\mu_{i}=\mu_{j}~,~H_{1}^{ij}=\mu_{i}\neq\mu_{j}$
    - E que em cada teste tempos uma significância de $\alpha=p(\text{rejeitar } H_{0}^{ij}~|~H_{0}^{ij}\text{ verdadeiro})$
    - Ou seja, teremos que fazer $C_{2}^{K}$ comparaçãoes
    - E definimos a significância total do processo: $$\begin{align*}
&P(\text{rejeitar pelo menos 1 }H_{0}^{ij}~|~H_{0}\text{ verdade})\\
&= 1-P(\text{não rejeitar nenhum }H_{0}^{ij}~|~H_{0}\text{ verdade} )\\
&= 1-P \biggr[(\text{ñ rej }H_{0}^{12}~|~H_{0}\text{ vdd})\cap(\text{ñ rej }H_{0}^{13}~|~H_{0}\text{ vdd})\cap\cdots\cap\cdots\biggr]\\
&= 1-\prod_{1}^{C_{2}^{K}}(1-\alpha)=1-(1-\alpha)^{C_{2}^{K}}\simeq1 
\end{align*}$$ ou seja, temos basicamente 0 confiança na nossa escolha final
- Ora, isto pode parecer algo que só vai acontecer com muitas amostras. Consideremos $K=10$ amostras  de modo que: $C_{2}^{10}=45$ logo: $1-(1-0.05)^{45}=0.9$. Se tivessemos $K=20$ teríamos $0.9999$
- Todos estes cálculos assumem que as amostras são todas independentes entre si

### Então, o que fazer?
- Fisher decidiu comparar tudo em simultaneo.
- Ora, já que todas as amostras vêm de populações normais com $\sigma^{2}$, este teste consiste em ver se todas as amostras vêm *da mesma população*!
- Então é como se tivessemos uma amostra enorme de tamanho $N=n_{1}+n_{2}+\dots+n_{K}$
- Definimos ainda a média global:
$$\overline{\overline{Y}}=\frac{1}{N}\sum\limits_{i=1}^{K}\sum\limits_{j=1}^{n_{i}}Y_{ij}$$
e a média da amostra $i$:
$$\overline{Y_{i}}=\frac{1}{n_{i}}\sum\limits_{j=1}^{n_{i}}Y_{ij} $$
- Assim temos que a Total Sum of Squares *TSS*:
$$\begin{align*}
\text{TSS}&= \sum\limits_{i=1}^{K}\sum\limits_{j=1}^{n_{i}}(Y_{ij}-\overline{\overline{Y}})^{2}\\
&= \sum\limits_{i=1}^{K}\sum\limits_{j=1}^{n_{i}}(Y_{ij}-\overline{Y_{i}} + \overline{Y_{i}}- \overline{\overline{Y}})^{2}\\
&= \sum\limits_{i=1}^{K}\sum\limits_{j=1}^{n_{i}}(Y_{ij}- \overline{Y}_{i})^{2} + \sum\limits_{i=1}^{K}\sum\limits_{j=1}^{n_{i}}(\overline{Y}_{i}-\overline{\overline{Y}})^{2} \\
&+ 2 \sum\limits_{i=1}^{K}(\overline{Y_{i}}-\overline{\overline{Y}})\sum\limits_{j=1}^{n_{i}}\cancelto{=0}{(Y_{ij}-\overline{Y})}\\
&= \text{WSS} + \text{BSS}
\end{align*}$$
- E definimos o Between Sum of Squares *BSS*:
$$\text{BSS}=\sum\limits_{i=1}^{K}n_{i}(\overline{Y_{i}}-\overline{\overline{Y}})^{2}$$
e o Within Sum of Squares *WSS*:
$$\text{WSS}=\sum\limits_{i=1}^{K}\sum\limits_{j=1}^{n_{i}}(Y_{ij}-\overline{Y_{i}})^{2}$$
- Ou seja: WSS mede variabilidade WITHIN amostras (dentro de cada amostra) e BSS mede BETWEEN amostras (compara amostras diferentes)

### Variância
- Podemos definir o estimador da variância da amostra $i$:
$$S_{i}^{2}=\frac{1}{n_{i}-1} \sum\limits_{j=1}^{n_{i}}(Y_{ij}-\overline{Y_{i}})^{2}$$
(sabemos que o valor que estamos a tentar estimar é $\sigma^{2}$)
- Podemos então combinar os estimadores das $K$ amostras, de forma a ter um estimador muito melhor da variância $\sigma^{2}$:
$$\begin{align*}
S^{2}&= \frac{(n_{1}-1)S_{1}^{2} + (n_{2}-1)S_{2}^{2}+\dots+(n_K -1)S_{K}^{2}}{n_{1}-1+n_{2}-1+\dots+n_{K}-1}\\
&= \frac{\sum_{j=1}^{n_{1}}(Y_{1j}-\overline{Y_{1}})^{2}+\sum_{j=1}^{n_{2}}(Y_{2j}-\overline{Y_{2}})^{2} + \dots+\sum_{j=1}^{n_{K}}(Y_{Kj}-\overline{Y_{K}})^{2}}{n_{1}+n_{2}+\dots+n_{K}-1-1-\dots-1}\\
&= \frac{\text{WSS}}{N-K}
\end{align*}$$

### Propriedades deste estimador
- Sabemos que $\frac{(n_{1}-1)S_{1}^{2}}{\sigma^{2}}\sim\chi_{n_{1}-1}^{2}$
    - Logo: $\mathbb{E}\left[\frac{(n_{1}-1)S_{1}^{2}}{\sigma^{2}} \right]=n_{1}-1~~\to~~ \mathbb{E} [(n_{1}-1)S_{1}^{2}]=(n_{1}-1)\sigma^{2}$
    - Isto aplica-se $\forall i~,~i=1,2,\dots,K$
- Logo:
$$\begin{align*}
\mathbb{E}\left[(n_{1}-1)S_{1}^{2}+\dots+(n_{K}-1)S_{K}^{2} \right]&= (n_{1}-1)\sigma^{2}+\dots+(n_{K}-1)\sigma^{2}\\
&= (N-K)\sigma^{2}
\end{align*}$$
e assim:
$$\mathbb{E}\left[\frac{\text{WSS}}{N-K} \right]=\sigma^{2}$$
logo este estimador não tem bias *SE $H_{0}$ FOR VERDADE*!

### Valor esperado de BSS
- Temos: $\text{BSS}=\sum_{i=1}^{K}n_{i}(\overline{Y_{i}}-\overline{\overline{Y}})^{2}$
- E podemos definir o valor esperado:
$$\begin{align*}
\mathbb{E}[\text{BSS}]&= \mathbb{E} \left[\sum\limits_{i=1}^{K} n_{i}(\overline{Y_{i}}-\overline{\overline{Y}})^{2} \right]\\
&= \mathbb{E}\left[\sum\limits_{i=1}^{K}n_{i}\overline{Y_{i}}^{2} + N \overline{\overline{Y}}^{2}-\cancelto{=0}{2 \overline{\overline{Y}}\sum\limits_{i=1}^{K}n_{i}\overline{Y_{i}}} \right]\\
&= \mathbb{E}\left[\sum\limits_{i=1}^{K}n_{i}\overline{Y_{i}}^{2} + N\overline{\overline{Y}}^{2} \right]
\end{align*}$$
- Sabemos que $\overline{Y_{i}}\sim\text{N}\left(\mu_{i}, \frac{\sigma^{2}}{n_{i}}\right)$. Ou seja: $$\text{Var}[\overline{Y}_{i}]=\frac{\sigma^{2}}{n_{i}}=\mathbb{E}[\overline{Y_{i}}^{2}]-\mu_{i}^{2}~~\to~~ \mathbb{E}[\overline{Y_{i}}^{2}]=\mu_{i}^{2}+  \frac{\sigma^{2}}{n_{i}}$$
- Sabemos ainda que $\overline{\overline{Y}}\sim\text{N}\left(\mu, \frac{\sigma^{2}}{N}\right)$ em que $\mu=\frac{1}{N}\sum_{i=1}^{K}n_{i}\mu_{i}$
- E continuamos a nossa dedução (não sem bem de onde vem o menos?):
$$\begin{align*}
\mathbb{E}[\text{BSS}]&= \sum\limits_{i=1}^{K}n_{i}\mathbb{E}[\overline{Y_{i}}^{2}] - N \mathbb{E}[\overline{\overline{Y}}^{2}]\\
&= \sum\limits_{i=1}^{K}n_{i}\left(\mu_{i}^{2}+ \frac{\sigma^{2}}{n_{i}}\right) - N \left(\mu^{2}+ \frac{\sigma^{2}}{N} \right)\\
&= \sum\limits_{i=1}^{K}n_{i}\mu_{i}^{2}+K \sigma^{2}-N\mu^{2}-\sigma^{2}\\
&= (K-1)\sigma^{2}+\sum\limits_{i=1}^{K}n_{i}\mu_{i}^{2}-N\mu ^{2}
\end{align*}$$
- Logo:
$$\mathbb{E}\left[\frac{\text{BSS}}{K-1} \right] = \sigma^{2}+ \frac{\sum\limits_{i=1}^{K}n_{i}\mu_{i}^{2}-N\mu ^{2}}{K-1}$$
logo BSS é um estimador de $\sigma^{2}$ _COM BIAS_.

#### Bias de BSS
- Vamos agora ver o bias, nomeadamente o numerador.
- Da desigualdade de Cauchy temos:
$$\left(\sum\limits_{i=1}^{K}a_{i}b_{i}\right)^{2} \le \sum\limits_{i=1}^{K}a_{i}^{2}\times\sum\limits_{i=1}^{K}b_{i}^{2}$$
- Ou seja, podemos escrever:
$$\begin{align*}
N\mu^{2}&= N \frac{(\sum_{i=1}^{K}n_{i}\mu_{i})^{2}}{N^{2}}\\
&= \frac{1}{N} \left(\sum\limits_{i=1}^{K}(\sqrt{n_{i}})(\sqrt{n_{i}}\mu_{i}) \right)^{2}\le \frac{1}{N}\underbrace{\sum\limits_{i=1}^{K}n_{i}}_{=N}\sum\limits_{i=1}^{K}n_{i}\mu_{i}^{2}=\sum\limits_{i=1}^{K}n_{i}\mu_{i}^{2}
\end{align*}$$
- Ou seja: $\sum_{i=1}^{K}n_{i}\mu_{i}^{2}-N\mu^{2}\ge0$ _sempre_.
- Temos que este numerador é $=0$ APENAS se $\mu_{i}=\mu,\forall i$ - ou seja, o numerador é zero e BSS *não tem bias* quando $H_{0}$ é **verdade**.
    - Se $H_{0}$ for falso, BSS costuma dar valores $>\sigma^{2}$

## Avaliar $H_{0}$
- Ou seja, vimos que quando $H_{0}$ é verdade:
    - $\frac{\text{BSS}}{K-1}$ estima $\sigma^{2}$ *sem bias*
    - $\frac{\text{WSS}}{N-K}$ estima $\sigma^{2}$ *sem bias*
- Ou seja, quando H0 for verdade teremos:
$$H_{0}\text{ verdadeiro então }\to F=\frac{\frac{\text{BSS}}{K-1}}{\frac{\text{WSS}}{N-K}}\approx \frac{\sigma^{2}}{\sigma^{2}}\approx1$$
- Caso contrário, teremos $F\gg1$
- Vimos acima que $\frac{\text{WSS}}{\sigma^{2}}\sim \chi_{N-K}^{2}$
- Dá para provar que quando $H_{0}$ é verdade: $\frac{\text{BSS}}{\sigma^{2}}\sim \chi_{K-1}^{2}$
- Ora, dá para demostrar que:
$$F=\frac{\frac{\text{BSS}}{K-1}}{\frac{\text{WSS}}{N-K}}\sim F_{K-1,N-K}$$
em que temos a **distribuição de Fisher-Snedecor**

- Assim, *rejeitamos* $H_{0}$ se:
$$\boxed{F=\frac{\frac{\text{BSS}}{K-1}}{\frac{\text{WSS}}{N-K}} > F_{K-1,N-K}^{-1}(1-\alpha)}$$
(em que vamos ver o termo da direita a uma tabela)

**EXEMPLO**
- Uma empresa quer estudar 4 combinações temperatura-salinidade na produção de camarão
- Cada um dos 4 tratamentos foi aplicado em 10 tanques. 
- Após 4 semanas foram tirados 100 camarões de cada um dos 40 tanques.

*Desenho experimental*
- Temos 40 tanques. Começamos por atribuir a cada tanque um tratamento de forma aleatória.
- Em R:
```R
indiv = seq(1,40,1)
T1 = rep("Treat1", times=10)
T2 = rep("Treat2", times=10)
T3 = rep("Treat3", times=10)
T4 = rep("Treat4", times=10)
design = sample(c(T1,T2,T3,T4))
names(indiv) = design
indiv
```
e podemos ver o que resulta:
![[design teste em r.png]]

*Os dados medidos*
- Depois das 4 semanas somamos o peso dos 100 camarões em cada tanque:
![[valores medios de cada tratamento nos tanques.png]]
nesta tabele temos a linha $i$ para o tratamento $i$ e de seguida o peso total nos 10 tanques com esse tratamento. No final temos o peso médio dos tanques com esse tratamento: $\overline{x_{i}}$
- O peso médio entre todos os tratamentos e tanques é $\overline{\overline{x}}=3.7863$ kg

*O teste*
- Consideremos que cada "amostra"/tratamento segue uma distribuição gaussiana. Todos têm a mesma variância $\sigma^{2}$
- Temos então a hipótese nula a testar $H_{0}:\mu_{1}=\mu_{2}=\mu_{3}=\mu_{4}$
- Podemos calcular:
$$\begin{align*}
\text{WSS}&= 10.786\\
\text{TSS}&= 24.543\\
\text{BSS}&= \text{TSS}-\text{WSS}=13.7571
\end{align*}$$
- Podemos então determinar:
$$F=\frac{\frac{BSS}{K-1}}{\frac{WSS}{N-K}}=\frac{4.5837}{0.2996}=15.31\gg1$$
- Vemos logo que as populações não são iguais. Ainda assim, podemos determinar $F_{3,36}^{-1}(1-0.05)=3.1<F$. Logo, podemos rejeitar $H_{0}$ com 95% de confiança

## ANOVA como Linear
- Como vimos, ANOVA testa *diferenças entre médias* e faz isso através de analisar a **variância**
- Como vimos, a hipótese nula é $H_{0}:\mu_{1}=\mu_{2}=\dots=\mu_{K}$
- O teste F (com a distribuição Schneider) consiste, na prática, nisto:
$$F = \frac{\text{Variância entre grupos}}{\text{Variância dentro de um grupo}}$$
- Notemos, no entanto, que ANOVA *não* testa variâncias. É considerado que todas as amostras têm distribuições com variância igual
    - Como tal, o facto se as amostras têm, de facto a mesma variância deve ser testado. Vários testes fazem isso: Levene, Bartlett, Brown-Forsythe
    - Caso não tenham todos a mesma variância, há varias opções

### Linear
- Primeiro, assumimos que $Y_{ij}\sim N(\mu_{i},\sigma^{2})$
- Podemos escrever isso como: $Y_{ij}=\mu+\beta_{i}+\varepsilon_{ij}~,~\varepsilon_{ij}\sim N(0,\sigma^{2})$
    - em que $\mu$ é a média global, $\beta_{i}$ o efeito da amostra $i$

- Assim, com esta notação, podemos escrever a hipótese nula como:
$$H_{0}:\beta_{1}=\beta_{2}=\dots=\beta_{K}=0$$
- Consideremos agora variáveis novas $X_{1},X_{2},\dots,X_{K}$ em que $X_{i}$ é $=1$ se a observação $Y_{ij}$ vem do grupo $i$ e $=0$ no caso contrário. Podemos então definir um *modelo linear*:
$$Y=\beta_{0}+\beta_{1}X_{1}+\beta_{2}X_{2}+\dots+\beta_{K}X_{K}+\varepsilon~~,~~\varepsilon\sim N(0,\sigma^{2})$$
chamemos a estas variáveis $X_{i}$ de *variáveis de indicação*
- Ora, para o modelo que define um fator em estudo com $K$ grupos, temos $K-1$ variáveis indicadoras:
$$Y=\beta_{0}+\beta_{1}X_{1}+\dots+\beta_{K-1}X_{K-1}+\varepsilon~~,~~ \varepsilon\sim N(0,\sigma^{2})$$
em que consideramos que um certo grupo é o de referência. Na definição acima temos $X_{K}$ como referência:
$$X_{K}=1-X_{1}-X_{2}-\dots-X_{K-1}$$
- Ou seja, definimos um certo grupo como sendo referência: $\beta_{0}$ é a resposta desse grupo, $\beta_{i}$ é a diferença entre a média do grupo $i$ e o referência
- EXEMPLO:
![[explicacao pratica modelo lienar.png]]

## Multiplos fatores
- Até aqui só consideramos 1 fator. Mas facilmente podemos adicionar mais
- EXEMPLO:
    - Um engenheiro está a testar a expansão térmica de diferentes materiais em diferentes temperaturas
    - Temos então 2 fatores: tipo de material (fator $A$ com $a$ níveis) e range de temperatura (fator $B$ com $b$ níveis)
    - Assim, modelamos um modelo ANOVA (sem interações) assim: $$Y_{ijk}=\mu+\alpha_{i}+\beta_{j}+\varepsilon_{ijk}~,~\varepsilon_{ijk}\sim N(0,\sigma^{2})$$
    - Se houverem interações (um efeito do material depende da temperatura): $$Y_{ijk}=\mu+\alpha_{i}+\beta_{j}+(\alpha\beta)_{ij}+\varepsilon_{ijk}$$
    - Isto, claro, pode ser escrito como um modelo linear desde que definamos corretamente as variáveis indicadoras

- Tem uma data de coisas sobre esta parte no PPT mas não passei nada