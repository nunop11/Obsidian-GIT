# 1 - Introdução
## 1.1 - Inferência estatística
- Usando amostras, estimamos os parâmetros (média, variância) ou outras conclusões de uma população
- Notemos:
    - Letras gregas representam a população
    - Letras normais representam a amostra
- Dentro de inferência estatística temos:
    - **Estimação** - Determinar algo na amostra, que terá um valor correspondente na população (EX: média). Dentro disto temos ainda os ICs (intervalos de confiança)
    - **Testes de hipótese** - Determinamos a probabilidade de uma hipotese ser verdade

**Nomenclaturas**
- Definimos uma VA com $n$ valores $(X_{1},X_{2},\dots,X_{n})$ como sendo uma *amostra aleatória* (AA)
- Definimos uma *estatística* como sendo  $Y=h(X_{1},X_{2},\dots,X_{n})$ 
    - $\overline{X}=\frac{1}{n}\sum\limits X_{i}$
    - $S^{2}=\frac{1}{n-1}\sum (X_{i}-\overline{X})^{2}$

## 1.2 - Estimação pontual
- Queremos estimar um parâmetro $\theta$ de uma população, usando uma amostra.
- Usamos uma estatística $T$. 
- Com a amostra é uma VA, para qualquer amostra que usemos, iremos ter um valor diferente de $T$. Ou seja, $T$ é também um *estimador* de $\theta$.

### Estimador centrado
$$E(T)=\theta$$

### Estimador consistente
- Um estimador é *consistente em média qudrática* se $V(T)\to0$ quando $n\to\infty$.

#### Exemplos dos 2 casos acima
- O estimador da média é centrado $$E \left(\overline{X} \right)=E \left(\frac{1}{n} \sum\limits_{i}X_{i} \right)=\frac{1}{n}\sum\limits_{i}E(X_{i})=\frac{1}{n}n\mu =\mu$$
- O estimador da variância da média é consistente:
$$V(\overline{X})=V\left(\frac{1}{n}\sum\limits_{i}X_{i}\right)=\frac{1}{n}\sum\limits_{i}V(X_{i})=\frac{\sigma^{2}}{n}~~\substack{\longrightarrow\\ \tiny{n\to\infty}}~~0$$

## 1.3 - IC
- Estimadores como $\overline{X},S^{2}$ são bons e centrados mas  dão 1 valor, que varia com cada amostra, como já vimos. 
- Assim, torna-se útil indicar um intervalo onde temos uma alta confiança que está o valor real.
    - Esse intervalo tem uma confiança $1-\alpha$
    - Temos então a **significância** $\alpha$
- O IC é definido por 2 estatísticas $Y_{1},Y_{2}$ de modo que:
$$P(\theta \in ]Y_{1},Y_{2}[)=1-\alpha$$
- Este IC é sempre relativo à população, nunca à amostra

#### Forma geral
- Para termos um IC centrado no valor desejado, temos esta forma geral que nos dá $Y_{1},Y_{2}$:
$$\text{IC} = \text{Estimador}\pm \text{Constante} \cdot \text{Desvio padrão do estimador}$$

#### Precisão
- Chamamos de precisão ao termo $\text{constante}\cdot\text{desvio padrão}$ na forma geral acima
- É metade da amplitude do IC

#### "Constante"
- Veremos depois como o fazer, mas podemos transformar a maioria dos problemas numa distribuição reduzida (como $N(0,1)$) e temos:
$$P(-z_{0}<\mathcal{U}<z_{0})=1-\alpha$$
em que
![[z1-a.2.png]]
e definimos:
$$P(z<z_{0})=1- \frac{\alpha}{2}=P(z<z_{1- \frac{\alpha}{2}})$$
e é este $z_{1-\alpha/2}$ que precisamos de determinar para a fórmula do IC.

### 1.3.1 - Normal, Var conhecida
- Queremos um IC da média $\mu$ e conhecemos $\sigma$. Dizemos que $X\sim N(\mu,\sigma^{2})$
- Conforme visto acima, temos: $\overline{X}\sim N(\mu, \frac{\sigma^{2}}{n})$. Ou seja, temos o *desvio padrão* $\sigma/\sqrt{n}$.
- Definimos a distribuição reduzida deste IC:
$$Z = \frac{\overline{X} - \mu}{\sigma/\sqrt{n}}\sim N(0,1)$$
OK, não sabemos $\mu$ mas isto apenas nos diz que devemos usar a distribuição $N(0,1)$ para obter a constante na fórmula do IC. Em outros casos iremos usar outras distribuições
- Temos o IC
$$\overline{X}\pm z_{1- \frac{\alpha}{2}} \frac{\sigma}{\sqrt{n}}$$
### 1.3.2 - Normal, Var desconhecida
- Mais realista e comum
- Acima vimos que $\frac{\overline{X}-\mu}{\sigma/\sqrt{n}}\sim N(0,1)$
- Mas agora não conhecemos $\sigma$. Invés disso, temos o estimador da variância: $S^{2}=\frac{1}{n-1}\sum (X_{i}-\overline{X})^{2}$
- Dá para demonstrar que temos:
$$T=\frac{\overline{X}-\mu}{S/\sqrt{n}}\sim t_{n-1}$$
logo temos o IC
$$\overline{X}\pm t_{1- \frac{\alpha}{2}} \frac{S}{\sqrt{n}}$$

### 1.3.3 - Normal, IC de variância
- Temos novamente $X\sim N(\mu,\sigma^{2})$ mas agora queremos saber $\sigma^{2}$ invés de $\mu$
- É possível demonstrar que:
$$\frac{(n-1)S^{2}}{\sigma^{2}}\sim \chi^{2}(n-1)$$
- O IC deste sistema **não é simétrico** em torno de  $S^{2}$, como fizemos para a média, porque a distrivuição chi2 NÃO é simétrica:
![[alpha em chi2.png]]
$$\begin{align*}
P \left(a <  \frac{(n-1)S^{2}}{\sigma^{2}}<b \right)&= 1-\alpha\\
P \left(a\sigma^{2} <  (n-1)S^{2}<b\sigma^{2} \right)&= 1-\alpha\\
P \left(\frac{(n-1)S^{2}}{b}<\sigma^{2}<\frac{(n-1)S^{2}}{a} \right)&= 1-\alpha\\
\end{align*}$$
logo temos o IC:
$$\left]\frac{(n-1)S^{2}}{b}, \frac{(n-1)S^{2}}{a}\right[$$

#### S^2 aproximada
- Temos que $\frac{(n-1)S^{2}}{\sigma^{2}}\sim \chi^{2}(n-1)$
- Na distribuição chi2: $E[\chi^{2}(\nu)]=\nu~,~V[\chi^{2}(\nu)]=2\nu$. Desta forma:
$$\Tiny\begin{align*}
E\left[\frac{(n-1)S^{2}}{\sigma^{2}}\right]=n-1~~\to~~ \frac{n-1}{\sigma^{2}}\cdot E[S^{2}]=n-1~~\to~~ E[S^{2}]&= \sigma^{2}\\
V\left[\frac{(n-1)S^{2}}{\sigma^{2}}\right]=2(n-1)~~\to~~ \left(\frac{n-1}{\sigma^{2}}\right)^{2}V[S^{2}]=2n-2~~\to~~ V(S^{2})&= \frac{2\sigma^{4}}{n-1}
\end{align*}$$
logo:
$$n\gg1 ~~\to~~ S^{2}\sim N\left(\sigma^{2}, \frac{2\sigma^{4}}{n-1}\right)$$

### 1.3.4 - Normal, Diff médias, Vars conhecidas
- Temos 2 populações: $X_{1}\sim N(\mu_{1},\sigma_{1}^{2})~,~X_{2}\sim N(\mu_{2},\sigma_{2}^{2})$ e tiramos 1 amostra de cada.
- Temos, como já vimos, para a média amostral: $\overline{X}_{1}\sim N(\mu_{1}, \frac{\sigma_{1}^{2}}{n_{1}})~~,~~ \overline{X}_{2}\sim N(\mu_{2}, \frac{\sigma_{2}^{2}}{n_{2}})$
- Logo definimos $D=\overline{X}_{1}-\overline{X}_{2}$ e temos
    - $E[D]=\mu_{1}-\mu_{2}$
    - $V[D]=\frac{\sigma_{1}^{2}}{n_{1}} + \frac{\sigma_{2}^{2}}{n_{2}}$
    - $D\sim N\left(\mu_{1}-\mu_{2}, \frac{\sigma_{1}^{2}}{n_{1}}+ \frac{\sigma_{2}^{2}}{n_{2}}\right)$
- Assim temos a distribuição reduzida:
$$Z=\frac{D - (\mu_{1}-\mu_{2})}{\sqrt{\frac{\sigma_{1}^{2}}{n_{1}} + \frac{\sigma_{2}^{2}}{n_{2}}}}\sim N(0,1)$$
e temos o IC:
$$D\pm z_{1-\alpha/2}\sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}}$$

### 1.3.5 - Normal, Diff médias, Vars desconhecidas mas IGUAIS
- Tal como acavamos de ver:
$$Z=\frac{D - (\mu_{1}-\mu_{2})}{\sqrt{\frac{\sigma_{1}^{2}}{n_{1}} + \frac{\sigma_{2}^{2}}{n_{2}}}}\sim N(0,1)$$
- Mas não conhecemos as variâncias. Então usamos: $S_{1}^{2}=\frac{1}{n_{1}-1}\sum (X_{i1}-\overline{X_{1}})^{2}~,~S_{2}^{2}=\frac{1}{n_{2}-1}\sum (X_{i2}-\overline{X_{2}})^{2}$
- E definimos a média ponderada destas 2 estimativas:
$$S_{p}^{2}=\frac{(n_{1}-1)S_{1}^{2} + (n_{2}-1)S_{2}^{2}}{n_{1}+n_{2}-2}$$
E simplesmente substituimos $\sigma_{1}=S_{p}=\sigma_{2}$ na distribuição reduzida:
$$T=\frac{D-(\mu_{1}-\mu_{2})}{S_{p}\sqrt{\frac{1}{n_{1}}- \frac{1}{n_{2}}}}\sim t_{n_{1}+n_{2}-2}$$
e temos o IC:
$$\overline{X_{1}}-\overline{X_{2}}\pm t_{1-\alpha/2}\cdot S_{p}\sqrt{\frac{1}{n_{1}}+ \frac{1}{n_{2}}}$$

### 1.3.6 - Normal, Razão entre 2 Vars
- Para comparar variâncias de 2 populações, é mais interessante estudar a razão.
- Temos $X_{1}\sim N(\mu_{1},\sigma_{1}^{2})~,~X_{2}\sim N(\mu_{2},\sigma_{2}^{2})$
- Como não conhecemos as variâncias usamos os estimadores: $S_{i}^{2}=\frac{1}{n_{i}-1}\sum_{j}(X_{ij}-\overline{X_{i}})^{2}$
- Assim definimos:
$$Z=\frac{(n_{1}-1)S_{1}^{2}}{\sigma_{1}^{2}}\sim \chi^{2}_{n_{1}-1}~~~~;~~~~ W=\frac{(n_{2}-1)S_{2}^{2}}{\sigma_{2}^{2}} \sim \chi_{n_{2}-1}$$
e temos:
$$\frac{\frac{Z}{n_{1}-1}}{\frac{W}{n_{2}-1}}=\frac{S_{1}^{2}\sigma_{2}^{2}}{S_{2}^{2}\sigma_{1}^{2}}\sim F_{n_{1}-1,n_{2}-1}$$
- Nesta distribuição temos:
![[dist F alpha.png]]
logo
$$\begin{align*}
P\left(a < \frac{S_{1}^{2}\sigma_{2}^{2}}{S_{2}^{2}\sigma_{1}^{2}}<b\right)&= 1-\alpha\\
P\left(a \frac{S_{2}^{2}}{S_{1}^{2}} < \frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}< b \frac{S_{2}^{2}}{S_{1}^{2}}\right)&= 1-\alpha\\
P \left(\frac{S_{1}^{2}/S_{2}^{2}}{a}> \frac{\sigma_{1}^{2}}{\sigma_{2}^{2}} > \frac{S_{1}^{2}/S_{2}^{2}}{b}\right)&= 1-\alpha\\
\end{align*}$$
e temos a IC:
$$\left]\frac{S_{1}^{2}/S_{2}^{2}}{b}, \frac{S_{1}^{2}/S_{2}^{2}}{a}\right[$$
### 1.3.7 - Proporção 
#### Wald
- Consideremos uma experiência de bernoulli $X$ repetida $n$ vezes. Como experiência de Bernoulli só pode ser "sucesso" ou "fracasso", definimos a *proporção de sucessos* como sendo  $P=X/n$ (estimativa amostral da proporção)
    - Para a população temos a proporção $p$
- Se $n$ for elevado temos $X\sim N(np, npq)$, em que $q=1-p$
- Definimos a distribuição reduzida: $\frac{P-p}{\sqrt{pq/n}}\sim N(0,1)$
- Como não sabemos $p,q$ usamos as estimativas amostrais destas e temos:
$$\begin{align*}
P \left(-z_{0} < \frac{\hat{p}-p}{\sqrt{\hat{p}\hat{q}/n}} < z_{0}\right) &= 1-\alpha\\
P \left(-z_{0} \sqrt{\frac{\hat{p}\hat{q}}{n}}< \hat{p}-p < z_{0}\sqrt{\frac{\hat{p}\hat{q}}{n}}\right) &= 1-\alpha\\
P \left(\hat{p}-z_{0} \sqrt{\frac{\hat{p}\hat{q}}{n}}< p < \hat{p}+z_{0}\sqrt{\frac{\hat{p}\hat{q}}{n} }\right) &= 1-\alpha\\
\end{align*}$$
e temos o IC:
$$\hat{p} \pm z_{1-\alpha/2}\sqrt{\frac{\hat{p}\hat{q}}{n}}$$
- Este intervalo é mau
    - Se tivermos $\hat{p}=0$ teremos o IC $[0,0]$. Isto é impossível!
    - Se tivermos $\hat{p}=1$ teremos o IC $[1,1]$
    - Isto será mais fácil quando temos $n$ menor
    - Ou seja, o IC Wald comporta-se pior perto dos extremos da proporção

#### AC - Agresti-Coull
- Adicionamos ao Wald 4 amostras falsas: 2 sucessos e 2 fracassos (2 zeros, 2 uns). Temos então a proporção amostral corrigida:
$$\tilde{p}=\frac{n\hat{p}+2}{n+4}=\frac{\sum_{i}^{n}X_{i}+0+0+1+1}{n+4}$$
- Este IC apenas se aplica com 95% de confiança, tendo-se o IC **95% de AC**:
$$\tilde{p}\pm 1.96 \sqrt{\frac{\tilde{p}(1- \tilde{p})}{n+4}}$$

**Bias**
- Definimos o Bias da proporção corrigida:
$$\begin{align*}
\text{Bias}[\tilde{p}]=E[\tilde{p}-p]&= E \left[\frac{n\hat{p}+2}{n+4} \right]-p=\frac{np+2}{n+4}-p\\
&= \frac{2-4p}{n+4}=(1-2p)\frac{2}{n+4}
\end{align*}$$
- Quando $p=1/2$ temos Bias nulo
- Consoante nos afastamos do meio, as amostras falsas introduzem bias maior. O bias também aumenta com $n$ menor

#### Wilson
- Temos o **score test** (veremos melhor depois):
    - Para uma população normal de variância conhecida, em que queremos estudar a média $\mu$. Temos a hipótese nula: $H_{0}:\mu=\mu_{0}$
    - Definimos a estatística: $T=\frac{\overline{X}-\mu_{0}}{\sigma/\sqrt{n}}\sim N(0,1)$ 
    - Rejeitamos a hipótese nula se $|T|>z_{1-\alpha/2}$. Para 95% temos $z_{1-\alpha/2}=1.96$
    - Mas, podemos ver que com $\pm z_{1-\alpha/2}$ conseguimos definir um intervalo de $T$s em que NÃO rejeitamos H0: $-z_{0}<T<z_{0}$ 
    - Isto dá-nos então um IC 95% ao isolar $\mu_{0}$ na fórmula de $T$: $$\overline{X}-z_{0} \frac{\sigma}{\sqrt{n}}\le \mu_{0}\le \overline{X}+ z_{0}\frac{\sigma}{\sqrt{n}}$$
    - Isto é exatamente o que vimos atrás: se $\theta_{0}$ está dentro do intervalo definido assim então NÃO rejeitamos
- Ao aplicar o score test a proporções temos: $\hat{p}\pm z_{0}\sqrt{p_{0}(1-p_{0})/n}$ 
- E vimos que o IC Wald é $\hat{p}\pm z_{0}\sqrt{\hat{p}(1-\hat{p})/n}$
- Mas estes dois ICs NÃO SÃO COMPATÍVEIS
    - É possível achar exemplos em que um valor $p_{0}$ está dentro do IC Wald (não rejeitamos H0), mas que a sua estatística $T>z_{0}$ logo podemos rejeitar H0. 
    - Queremos então algo que concorde!!!
- Wald consiste então em inverter o Score Test:
    - Temos $\frac{\hat{p}-p_{0}}{\sqrt{p_{0}\frac{1-p_{0}}{n}}}\le z_{0}$
    - Passamos a raiz para o outro lado e metemos tudo ao quadrado
    - Ficamos com um polinómio de 2º grau em função de $p_{0}$
    - Fazemos a fórmula resolvente e obtemos um intervalo de $p_{0}$, o **IC Wald**: $$p_{0}=\frac{1}{1+ \frac{z^{2}}{n}} \left[\left(\hat{p} + \frac{z^{2}}{2n}\right) \pm z \sqrt{\frac{\hat{p}(1-\hat{p})}{n}+ \frac{z^{2}}{4n^{2}}} \right]$$
- Wilson nunca pode colapsar para $[0,0]$
- Wilson apenas tem valores de probabilidade possíveis (de 0 a 1). Wald pode ter valores negativos ou >1

### 1.3.8 - Diferença de proporções
- Temos 2 populações com proporções $p_{1},p_{2}$. Temos as proporções amostrais $P_{1}=X_{1}/n_{1}~,~P_{2}=X_{2}/n_{2}$
- Temos, como vimos acima: $P_{i}\sim N\left(p_{i}, \frac{p_{i}(1-p_{i})}{n_{i}}\right)$
- Logo $P_{1}-P_{2}\sim N \left(p_{1}-p_{2}, \frac{p_{1}(1-p_{1})}{n_{1}} + \frac{p_{2}(1-p_{2})}{n_{2}}\right)$
- E definimos o IC tipo Wald:
$$(P_{1}-P_{2})\pm z_{0} \sqrt{\frac{p_{1}(1-p_{1})}{n_{1}} + \frac{p_{2}(1-p_{2})}{n_{2}}}$$
e usamos as estimativas nos lugais de $p_{1},p_{2}$ que não conhecemos.

## 1.4 - Testes de hipóteses
-  4 tipos:
    - Testes *ajustamento/significância*: ver se amostra veio de uma população (do tipo gaussiana, p/EX)
    - Testes *independência*: ver se 2 parâmetros são independentes
    - Testes de *homogeneidade/igualdade*: ver se 2+ amostras foram tiradas da mesma população
    - Testes de parâmetros de populações: abaixo

### 1.4.1 - Testes de parâmetros de população
- É um caso mais restrito de testes de ajustamento: vemos se a amostra vem de uma população gaussiana COM certa média ou variância
- Para todos os ICs acima definimos estatísticas do tipo:
$$Z=\frac{\overline{X}-\mu}{\sigma/\sqrt{n}}\sim N(0,1)~~,~~T=\frac{\overline{X}-\mu}{S/\sqrt{n}}\sim t_{n-1}$$
    - Ora, para fazer um teste do tipo $H_{0}:\mu=\mu_{0}$ substituimos $\mu=\mu_{0}$ nas estatísticas e obtemos um valor de $Z,T$. 
    - REJEITAMOS $H_{0}$ se $Z>z_{1-\alpha/2}$ ou $T>t_{1-\alpha/2}$
- Isto aplica-se em qualquer caso em que conseguimos definir uma estatística que segue uma distribuição reduzida. 
    - No formulário é indicada a distribuição de todos os ICs estudados. Para cada um podemos então fazer um teste com esta lógica. 

### 1.4.2 - Testes unilaterais
- Teste bilateral é do tipo: $H_{0}:\mu=\mu_{0}~,~H_{1}:\mu\neq \mu_{0}$
- Teste unilateral é do tipo: $H_{0}:\mu>\mu_{0}~,~H_{1}:\mu\le\mu_{0}$
    - Definimos $Z=\frac{\overline{X}-\mu_{0}}{\sigma/\sqrt{n}}\sim N(0,1)$ 
    - Rejeitamos $H_{0}$ se $Z>z_{1-\alpha/2}$
    - No caso bilateral rejeitamos se $|Z|>z_{1-\alpha/2}$

# 2 - Proporções
- Originalmente fiz um resumo inteiro sobre isto, seguindo um blog que o professor disponibilizou no moodle. 
- Neste resumo incorporei isso na secção 1.3.7
- Seguimos em frente então

# 3 - Teste de Potência
- Temos os tipos de erros num teste de H0:
![[tabela hipoteses e erros.png]]
- Comecemos por entender os testes:
![[explicacao h0.png]]
- Na tabela de erros parece haver uma "contradição" ao dizer que temos um TP (true positive) quando H0 é falso e rejeitamos. Isso aocntece devido à forma como definimos H0. Normalmente, esta hipótese é algo "nulo" ou "neutro" ou "não acontece nada". 
- No caso médico, podemos ter $H_{0}$ a ser "a doença não está presente na pessoa". 
    - Assim, se uma pessoa tiver a doença, $H_{0}$ é *falso* -- a pessoa está *positiva* para a doença. 
    - Similarmente, se essa pessoa fizer o teste e der *positivo*, então rejeitamos H0 --> É FALSO que a doença não está na pessoa
    - Logo temos um *TP* se a pessoa tiver a doença e ela for detetada num teste: H0 é falso e rejeitá-mo-lo ao ter um teste positivo.

- De volta aos erros, temos: $\begin{align*}\alpha&=  p (\text{rejeitar }H_{0}~|~ H_{0} \text{ verdadeiro})=p(\text{FP})=p(\text{Erro Tipo I})\\\beta&= p(\text{não rejeitar }H_{0}~|~H_{0}\text{ falso})=p(\text{FN})=p(\text{Erro Tipo II})\end{align*}$ 
- Definimos a **potência** do teste: $1-\beta$ -- probabilidade de *rejeitar H0 quando H0 é falso*
    - Ou seja, é a probabilidade de detetar um fenómeno que existe!!

- Se $\alpha$ for reduzido iremos evitar FPs (evitamos rejeitar H0 quando ela é verdadeira, evitamos detetar algo que não existe)
    - Mas se $\alpha$ for demasiado reduzido, iremos começar a aceitar muitos casos, de modo que eventualmente vamos aceitar tantos casos que começamos a ter mais FN e $\beta$ aumenta
    - Ou seja, se forçarmos $\alpha$ muito reduzido estaremos efetivamente a ignorar efeitos reais que existem

- Ou seja:
    - $\alpha$ / pvalue medem a chance de encontrar algo que não está lá (reduzimos FP mas acabamos a não rejeitar demasiadas coisas)
    - $1-\beta$ mede a chance de encontrar um efeito real

## 3.1 - Notas do documento de Potência em R
- Para estimar o ES, **no caso de t-test** usamos o $d$ de Cohen:
$$d = \frac{|\overline{X_{A}} - \overline{X_{B}}|}{\sqrt{\frac{S_{A}^{2}+S_{B}^{2}}{2}}}$$
ou, em R:
```R
d <- abs(mean(groupA[1:10])-mean(groupB[1:10])) / sd(c(groupA[1:10]-mean(groupA[1:10]), groupB[1:10]-mean(groupB[1:10])))
```

- No `pwr.t.test` temos: `sig.level, d, n, power`. Escrevemos 3 e o programa determina o valor optimo para o outro parâmetro.
- Podemos mudar `type=` para fazer teste de potência para:
    - *paired* : 2 medições da mesma amostra
    - *two.sample* : 2 amostras independentes, o caso default e "genérico"
    - *one.samples* : Quando queremos ver se uma amostra tem média=0
- Temos teste de potência de correlações: `pwr.r.test`

## 3.2 - Testes potência não paramétricos
- Podemos ter dados de população não-gaussiana ou ordinal
- Estes métodos não assumem nada e são mais práticos

### 3.2.1 - Teste dos sinais (1 amostra)
- Localizar mediana $\tilde{\mu}$, fazendo o teste:  $\begin{align*}H_{0}:\tilde{\mu}=\tilde{\mu_{0}}\\ H_{1}:\tilde{\mu}\neq\tilde{\mu_{0}}\end{align*}$
- Criamos o set $X-\tilde{\mu_{0}}$: $(X_{1}-\tilde{\mu_{0}},X_{2}-\tilde{\mu_{0}},\dots,X_{n}-\tilde{\mu_{0}})$
- Contamos quantos valores são positivos: $N_{+}$
    - Considerando que os valores são random, temos $\frac{1}{2}$ probabilidade de um dado valor ser positivo. Temos então $N_{+}\sim\text{Bi}(n, \frac{1}{2})$
    - Removemos os zeros das contagens: não os contamos em $N_{+}$ e removemos $1$ a $n$
    - Temos então: $P(X\le N_{+})$ na distribuição $\text{Bi}(n, \frac{1}{2})$
    - Se essa probabilidade for $<\alpha$ então rejeitamos!

### 3.2.2 - Teste dos sinais (2 amostras)
- Temos 2 sets de dados $X,Y$ emparelhados (p/EX: o valor $i$ de cada um corresponde à medição do mesmo sujeito em tempos diferentes)
- Queremos saber se têm a mesma distribuição. Definimos: $\begin{align*}H_{0}:X\stackrel{d}{=}Y\\ H_{1}:X\stackrel{d}{\neq}Y\end{align*}$ 
- Fazemos isto:
    - Vamos testar se $H_{0}:X-Y=0$. Se as distribuições forem iguais, teremos igual probabilidade de ter $x_{i}-y_{i}>0$ ou $<0$. 
    - Contamos o número de subtrações com sinal positivo $N_{+}\sim \text{Bi}(n, \frac12)$
    - Fazemos a mesma lógica que acima

### 3.2.3 - Teste de Wilcoxon (2 amostras paired)
- Começamos por fazer o mesmo que em Sinais de 2 amostras: $Z_{i}=X_{i}-Y_{i}$ e calculamos o módulo $|Z_{i}|$
- Atribuimos ranks $R_{i}$ aos módulos em *ordem crescente*. Não incluimos zeros.
- Definimos ainda $R_{i}^{*}$, o rank com o sinal da diferença.
- EXEMPLO:
![[exemplo test design 2.png]]
- Definimos as estatísticas:
    - $T^{+}=\sum_{i}^{n}R_{i}\psi_{i} ~~~~ \psi_{i}=\{1~,~Z_{i}>0$ -->> Soma dos ranks de subtrações positivas
    - $T^{-}=\sum_{i}^{n}R_{i}\psi_{i} ~~~~ \psi_{i}=\{1~,~Z_{i}>0$ -->> Soma dos ranks de subtrações negativas
    - $W=T^{+}+T^{-}=\sum_{i}R_{i}^{*}$ 
    - Temos $T^{-}=\frac{n(n+1)}{2}-T^{+}$
- Para um certo $n$ apenas teremos $N$ somas possíveis de $n$ ranks com sinais diferentes.
    - Para $n=4$ temos $1+2+3+4,1-2+3+4,1+2-3+4,\dots$ -- temos 16 combinações.
    - Podemos com isto definir as probabilidades de cada valor ![[valores possiveis e probs de W.png]]

**EMPATES**
- Quando temos empates nos ranks: $|Z_{i}|=|Z_{j}|$ em que $|Z_{i}|$ é o $k$ menor rank, atribuimos a estes 2 valores o mesmo rank: $$R_{i}=R_{j}=\frac{2k+1}{2}$$

#### Assintotico
- Quando $n$ é elevado temos (TLC):
$$W~\dot\sim~N\left(0, \frac{n(n+1)(2n+1)}{6}\right)$$

- Quando $H_{0}$ é verdade, podemos definir:
$$T^{*}=\frac{T^{+} - \mathbb{E}[T^{+}]}{\sqrt{\text{Var}[T^{+}]}}=\frac{T^{+} - \frac{n(n+1)}{4}}{\sqrt{\frac{n(n+1)(2n+1)}{24}}}\sim N(0,1)$$

#### 1 variável
- Com 1 variável podemos usar Wilcoxon:
    - Definimos a variável $Z_{i}=X_{i}-\tilde{\mu_{0}}$ 
    - Aplicamos o método

### 3.2.4 - Wilcoxon-Mann-Whitney (WMN)
- Usamos Wilcoxon para estudar 2 variáveis emparelhadas/correlacionadas
    - WMN é usado para 2 amostras *independentes*, sendo que queremos determinar se são da *mesma população*

**EXEMPLO**
- Temos 2 tratamentos A,B com 15 dados totais: ![[dados com n diferentes e ranks.png]]
- Os valores são um certo parâmetro medido após aplicar o tratamento. 
    - Definimos  $\begin{align*}H_{0}&: \text{A e B são iguais}\\ H_{1}&: \text{B resulta em medições maiores}\end{align*}$
    - Temos $n$ pontos da amostra A e $m$ da amostra de B ($N=n+m$)
    - Temos $X_{1},\dots,X_{n};Y_{1},\dots,Y_{m}$. E definimos $X_{i}=e_{i}~,~Y_{j}=e_{n+j}+\Delta$
        - Os $e$ são independentes e da mesma população
        - Ou seja, escrevemos $Y$ (amostra $B$) como sendo um efeito fixo adicionado à distribuição de $X$ (que será a mesma de $e$)

- O teste de hipóteses torna-se: $\begin{align*}H_{0}: \Delta=0\\ H_{1}:\Delta>0\end{align*}$
- Conforme mostrado acima, atribuimos *ranks por ordem crescente* aos $N$ dados como se fossem **1 só set de dados**. 
- Definimos a estatística: $T_{m,n}=\sum\limits_{j=1}^{m}R_{j}$ -> SOMA DE RANKS DO MENOR SET (tratamento B neste caso)
- Esta estatística permite-nos decidir se rejeitamos H0

#### Assintótico
$$Z=\frac{T_{m,n}- \frac{m(m+n+1)}{2}}{\left[\frac{mn(m+n+1)}{12}\right]^\frac{1}{2}}~\dot\sim~\text{N}(0,1)$$
Podemos utilizar isto como estatística e rejeitar H0 se $Z<z_{1-\alpha/2}$

# 4 - ANOVA
- Usado para COMPARAR MÉDIAS, ou seja, testar a hipótese $H_{0}:\mu_{1}=\mu_{2}=\dots=\mu_{K} ~,~H_{1}:\text{pelo menos 2 médias diferentes}$

## 4.1 - Dados
- Temos $K$ amostras aleatórias de populaçõe gaussianas com variância $\sigma^{2}$ (IGUAL EM TODAS AS POPS)
$$\begin{align*}
Y_{1}&= (Y_{11},Y_{12},\dots,Y_{1n_{1}}) ~~~~;~~ Y_{1j}\sim N(\mu_{1},\sigma^{2})\\
&\vdots\\
Y_{K}&= (Y_{K1},Y_{K2},\dots,Y_{Kn_{K}}) ~~~~;~~ Y_{Kj}\sim N(\mu_{K},\sigma^{2})
\end{align*}$$

## 4.2 - Pairwise t.test
- A primeira ideia que poderiamos ter era fazer t-test par a par entre amostras: $H_{0}^{ij}:\mu_{i}=\mu_{j}~~,~~ H_{1}^{ij}:\mu_{i}\neq\mu_{j}$
- Mas isso significa que vamos acumulando erro e depois temos muito baixa confiança na nossa conclusão

## 4.3 - ANOVA à mão
- Vejamos como Fisher fez
- Como estamos a assumir variância $\sigma^{2}$ em TODAS as amostras, testar se têm a mesma média consiste em confirmar se **vêm todas da mesma população**
- Temos o número total de pontos: $N=n_{1}+n_{2}+\dots+n_{K}$
- Definimos:
    - Média global: $$\overline{\overline{Y}}=\frac{1}{N}\sum\limits_{i=1}^{K}\sum\limits_{j=1}^{n_{i}}Y_{ij}$$
    - Média da amostra $i$: $$\overline{Y_{i}}=\frac{1}{n_{i}}\sum\limits_{j=1}^{n_{i}}Y_{ij}$$
    - **TSS** - Total Sum of Squares: $$\begin{align*}
\text{TSS}&= \sum\limits_{i=1}^{K}\sum\limits_{j=1}^{n_{i}} (Y_{ij} - \overline{\overline{Y}})^{2}\\
&= \sum\limits_{i=1}^{K}\sum\limits_{j=1}^{n_{i}} (Y_{ij} - \overline{Y_{i}} + \overline{Y_{i}}- \overline{\overline{Y}})^{2}\\
&= \sum\limits_{i=1}^{K}\sum\limits_{j=1}^{n_{i}} (Y_{ij} - \overline{Y_{i}})^{2} + \sum\limits_{i=1}^{K}\sum\limits_{j=1}^{n_{i}} (\overline{Y_{i}} - \overline{\overline{Y}})^{2}\\
&= \text{WSS}+\text{BSS}
\end{align*}$$
    - **WSS** - Within Sum of Squares (dentro de cada amostra): $$\text{WSS}=\sum\limits_{i=1}^{K}\sum\limits_{j=1}^{n_{i}} (Y_{ij} - \overline{Y_{i}})^{2}$$
    - **BSS** - Between Sum of Squares (entre amostras): $$\text{BSS}=\sum\limits_{i=1}^{K}n_{i} (\overline{Y_{i}} - \overline{\overline{Y}})^{2}$$
- Temos que a variância dos dados é dada por $S^{2}=\frac{\text{WSS}}{N-K}$ - pensemos que é a soma de erros quadráticos dentro de amostras, normalizada. Usamos $N-K$ porque temos $N$ dados e perdemos $K$ graus de liberdade ao percorrer as $K$ amostras
- Também $S^{2}=\frac{\text{BSS}}{K-1}$ nos dá a variância. Funciona de forma parecida ao que vimos acima, mas dividimos por $K-1$ porque temos $K$ amostras e perdemos 1 grau de liberdade ao percorrê-los

- Por razões teóricas que não vou incluir aqui, temos:
$$F=\frac{\frac{\text{BSS}}{K-1}}{\frac{\text{WSS}}{N-K}}\sim F_{K-1,N-K}$$
(apenas se $H_{0}$ for verdade. Senão, $\frac{\text{BSS}}{K-1}$ é estimador não-centrado de $\sigma^{2}$ e $F\gg1$)
- Assim, **rejeitamos H0** (as amostras pertencem a populações diferentes / as médias das amostras são diferentes) se:
$$F> F_{K-1,N-K}^{-1}(1-\alpha)$$
- Regra geral, se $F\gg1$ podemos concluir que H0 é falsa.

#### Nota sobre ANOVA
- Então, ANOVA permite comparar médias de amostras
- Para isso, ANOVA determinar se as amostras pertencem à mesma população normal
- Mais concretamente ainda, este estudo é feito através do estudo de variâncias (WSS,BSS)
- Dito isto, não estamos a fazer teste às variâncias. Apenas as usamos para chegar a uma distribuição conhecida: a de Fisher (F)

# 5 - Modelo Linear
- Definimos o modelo linear:
$$f(x)=\beta_{0}+\sum\limits_{j}x_{j}\beta_{j}$$
em que $x_{j}$ podem ser variáveis quantitativas, transformações funcionais, etc

### MMQ / LSM
- == Método de Mínimos Quadrados ou == Least Squares Method
- Definimos a soma dos erros quadráticos:
$$\text{SSE}(\beta)=\sum\limits_{i=1}^{N}(y_{i}-f(x_{i}))^{2}=(Y-X\beta)^{T}(Y-X\beta)$$
- O melhor fit será aquele que minimiza o SSE (least squares):
$$\frac{\partial \text{SSE}}{\partial \beta}=0=-2 X^{T}(Y-X\beta)~~\to ~~ \hat{\beta}=(X^{T}X)^{-1}X^{T}Y$$

## 5.1 - Inferência
- Estamos em $\mathbb{R}^{p+1}$ e cada $x_{i}$ é uma linha da matriz $X$. Consideramos que $x_{i}$ são fixos e $Y_{i}$ controlam a variância
- Temos que: $\text{Var}(\hat{\beta})=(X^{T}X)^{-1}\sigma^{2}$
- E definimos:
$$\hat{\sigma}^{2}=\frac{1}{N-p-1} \sum\limits_{i}^{N}(Y_{i}-\hat{Y}_{i})^{2}$$
- No modelo linear, temos que $Y=\beta_{0}+\sum_{j}x_{j}\beta_{j}+\varepsilon$ em que $\varepsilon\sim N(0,\sigma^{2})$. Ora, isso quer dizer que $Y$ é normal com variância  $\sigma^{2}$. Finalmente, isso implica que: $\hat{\beta}\sim N(\beta, (X^{T}X)^{-1}\sigma^{2})$
    - Assim: $$\frac{(N-p-1)\hat{\sigma}^{2}}{\sigma^{2}}\sim \chi_{N-p-1}^{2}$$

### Testes e ICs / Z-score
- Consideremos então que temos 1 parâmetro $\hat\beta_{j}$. Temos a hipótese nula $H_{0}:\beta_{j}=0$. 
- Na matriz $(X^{T}X)^{-1}$ teremos o elemento da diagonal $\nu_{j}$ correspondente a $\hat{\beta}_{j}$
- Conforme o que vimos acima, temos: $\hat{\beta}_{j}\sim N(0, \nu_{j}\sigma^{2})$
- Com isto, teremos as Z-scores: 
    - $Z=\frac{\hat{\beta_{j}}}{\sigma\sqrt{\nu_{j}}}\sim N(0,1)$ se $\sigma$ for conhecida
    - $T=\frac{\hat{\beta_{j}}}{\hat\sigma\sqrt{\nu_{j}}}\sim t_{N-p-1}$ se $\sigma$ NÃO for conhecida

- Com isto, podemos definir os ICs:
    - $\hat{\beta_{j}}\pm z_{1-\alpha/2}\sigma\sqrt{\nu_{j}}$ se $\sigma$
    - $\hat{\beta_{j}}\pm t_{1-\alpha/2}\hat{\sigma}\sqrt{\nu_{j}}$ se $\sigma$ NÃO for conhecida

### Variáveis inúteis
- Temos um modelo 1 (*complexo*) com $p_{1}$ variáveis. Queremos ver se algumas destas variáveis são inúteis para o modelo linear
    - Definimos o modelo 0 (*simples*) com $p_{0}<p_{1}$ variáveis
- Definimos:
$$F=\frac{\frac{SSE_{0}-SSE_{1}}{p_{1}-p_{0}}}{\frac{SSE_{1}}{N-p_{1}-1}}\sim F_{p_{1}-p_{0}, N-p_{1}-1}$$
- Quando $N\gg1$ até podemos dizer $F\sim \chi_{p_{1}-p_{0}}^{2}$
- Notemos que este $F$ consiste no teste: $$H_{0}:\text{As variáveis que tiramos não importam}$$
- Isto quer dizer que se obtivermos $F>F^{-1}_{p_{1}-p_{0}, N-p_{1}-1}(1-\alpha)$ então NÃO rejeitamos H0 logo as variáveis NÃO IMPORTAM.

**Escolher as variáveis a remover**
- Podemos determinar as Z-scores como vimos acima. Removemos as variáveis em que $Z<z_{1-\alpha/2}$

--- A partir daqui não apanho nada.