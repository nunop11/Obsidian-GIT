## 1 - Inferência Estatística
- Probabilidade é quando supomos/conhecemos os parâmetros que descrevem as populações. Ou seja, usamos os parâmetros para determinar a probabilidade de algo acerca de uma amostra
- Estatística consiste no *oposto*! Usando amostras, prevemos/estimamos os parâmetros da população.
- Invés de calcular probabilidades de certos eventos, fazemos testes de hipóteses: vemos se "a moeda é viciada?" invés de "qual é a média $\mu$?"

### NOTAÇÃO
- Letras gregas ($\mu$) descrevem a *população*
- Letras normais ($\overline{x}$) descrevem uma *amostra*

### 1.1 - Inferência estatística
- Procedimento de tirar conclusões sobre a população a partir uma amostra
- Idealmente analisávamos toda a população, mas isso é impossível
- Temos, dentro disto:
    - Estimação
    - Teste de hipóteses

#### Estimação
- Calcular, a partir de uma amostra, um certo valor que em príncipio irá corresponder ao da população.
- Se para uma certa amostra estimarmos a média, em princípio ela deverá ser uma aproximação da média da população
- Alternativamente, podemos determinar um intervalo de valores que tentam aproximar-se ao valor da população

#### Teste de hipóteses
- Analisamos uma amostra e daí concluímos algo sobre a população
- Aqui não determinamos parâmetros, verificamos certas hipóteses

### Nomes
#### Amostras
- Uma VA de dimensão $n$ com valores $(X_{1},X_{2},\dots,X_{n})$ é uma *amostra aleatória* (AA)
- Uma amostra é um valor de uma amostra aleatória ?

#### Estatística
- Uma estatística é uma VA função da amostra aleatória: $$Y=h(X_{1},X_{2},\dots,X_{n})$$
- Por exemplo, a média de uma AA é uma estatística:
$$\overline{X}=\frac{1}{n}(X_{1}+X_{2}+\dots+X_{n})$$
e também a variância:
$$S^{2}=\frac{1}{n-1}\sum (X_{i}-\overline{X})^{2}$$


### 1.2 - Estimação pontual
- Um dos objetivos da Estatística é establecer inferências entre os parâmetros de uma população a partir da amostra, como acima dito
- Consideremos que estamos a estimar $\theta$ e que usamos uma estatística $T$ para o estimar.
- Assim, cada amostra irá dar um valor diferente para $T$, ou seja $T$ é um *estimador*!
- Para uma certa amostra, o valor que $T$ nos dá é a *estimativa*.

**Estimador centrado**
- Um estimador $T$ de $\theta$ é centrado se: $$E(T)=\theta$$
- Por exemplo a média:
$$\overline{X}=\frac{1}{n}\sum X_{i} \quad;\quad E(\overline{X})=\frac{1}{n}E \left( \sum\limits X_{i} \right)=\frac{1}{n}\sum\limits E(X_{i})=\frac{1}{n} n\mu =\mu$$

**Estimador consistente**
- Um estimador centrado é *consistente em média quadrática* se a sua variância tende para zero quando $n\to\infty$.
    - Este conceito pode ser usado com estimadores não centrados, mas nesta UC não o iremos fazer
    - Existe outra definição de consistência que é mais soft mas não iremos ver
- Consideremos o estimador da variância da média:
$$\begin{align*}
\overline{X}&= \frac{1}{n}\sum X_{i}\\
V(\overline{X})&= \frac{1}{n^{2}}V\left(\sum X_{i}\right)= \frac{1}{n^{2}}\sum V(X_{i})\\
&= \frac{1}{n^{2}} n \sigma^{2}=\frac{\sigma^{2}}{n}\longrightarrow_{n\to\infty} 0
\end{align*}$$
- Ou seja, num estimador consistente temos que a distribuição do estimador é muito mais estreita que aquela da variável em si
![[dist media.png]]
- EX:
    - Para $X$ temos uma dist normal com $n=100,\sigma^{2}=50$. 
    - A variância da média será $50/100=0.5$ AKA 100 vezes menor que a variância da população!

### 1.3 - Intervalo de Confiança (IC)
- $\overline{X},S^{2}$ são estimadores bons e centrados
- Estes dão valores pontuais, ou seja, para uma certa amostra obtêm um valor que se deverá aproximar de $\mu,\sigma^{2}$
- Mas em princípio o valor obtido *nunca* será exatamente igual ao valor real destes parâmetros. Assim, torna-se mais interessante definir um *intervalo* em que achamos que é **muito provável** o valor real se encontrar - ICs

**Construir intervalo**
- Construímos um intervalo com um certo *grau de confiança* $1-\alpha$. Dizemos ainda que temos uma *significância* $\alpha$
- Precisamos então de 2 estatísticas $Y_{1},Y_{2}$ tais que:
    - $Y_{1}<Y_{2}$
    - Temos então que o intervalo de confiança é definido por: $$P(\theta\in ]Y_{1},Y_{2}[~) = 1-\alpha$$

**Amostras**
- ICs apenas fazem sentido ao falar de previsões para *populações*: determinamos o intervalo para $\mu$!
- Se tivermos dados de UMA amostra não faz qualquer sentido ver se ela nos dá um IC em que $\mu$ está ou não. Isto porque o intervalo que obtemos não é aleatório.

### 1.3.1 - IC com $\sigma^{2}$ conhecida
- Queremos estimar uma média $\mu$ de uma população usando um IC
- Consideremos que $X\sim N(\mu,\sigma^{2})$ e temos uma AA $(X_{1},X_{2},\dots,X_{n})$
- Podemos, por exemplo, definir o seguinte intervalo:
$$\left] \overline{X}-2 \frac{\sigma}{\sqrt{n}} ; \overline{X} + 2 \frac{\sigma}{\sqrt{n}}\right[$$

**Grau de confiança**
- Comecemos por determinar o grau de confiança do intervalo acima
- Ou seja, queremos saber:
$$P \left(\mu \in \left] \overline{X}-2 \frac{\sigma}{\sqrt{n}} ; \overline{X} + 2 \frac{\sigma}{\sqrt{n}}\right[ \right) = 1-\alpha$$
quanto maior for a probabilidade, melhor o IC.

- Mas por vezes temos que calcular coisas à mão. E determinar a densidade de probabilidade de uma qualquer distribuição normal pode não ser conveniente.
- Podemso rearranjar isto:
$$\begin{align*}
& P \left(\mu \in \left] \overline{X}-2 \frac{\sigma}{\sqrt{n}} ; \overline{X} + 2 \frac{\sigma}{\sqrt{n}}\right[ \right)\\
&= P \left( \overline{X}- 2 \frac{\sigma}{\sqrt{n}} < \mu < \overline{X} + 2 \frac{\sigma}{\sqrt{n}}\right)\\
&= P \left( \mu- 2 \frac{\sigma}{\sqrt{n}} < \overline{X} < \mu + 2 \frac{\sigma}{\sqrt{n}} \right)\\
&= P \left( \frac{\mu- 2 \frac{\sigma}{\sqrt{n}} - \mu}{\frac{\sigma}{\sqrt{n}}} < \frac{\overline{X}-\mu}{\frac{\sigma}{\sqrt{n}}} < \frac{\mu+ 2 \frac{\sigma}{\sqrt{n}} - \mu}{\frac{\sigma}{\sqrt{n}}}\right)\\
&= P(-2<\mathcal{U}<2)\\
&= P(\mathcal{U}<2) - P(\mathcal{U}<-2) \approx 95\%
\end{align*}$$
- Notemos então que aqui fizemos uma "redução" da distribuição:
$$X\sim N(\mu,\sigma^{2}) ~~~~\to ~~~~ \overline{X}\sim N\left(\mu,\frac{\sigma^{2}}{n}\right)~~~~\to~~~~ \frac{\overline{X}-\mu}{\sigma/\sqrt{n}}\sim N(0,1)$$

**Forma geral**
- Ou seja, para termos um IC centrado no valor desejado, temos esta forma geral que nos dá $Y_{1},Y_{2}$:
$$\text{Estimador}\pm \text{Constante} \cdot \text{Desvio padrão do estimador}$$
#### Precisão
- O termo $\text{constante}\cdot\text{desvio padrão}$ é a **precisão da estimativa**.
    - AKA a precisão é **metade da amplitude** do IC

#### "Constante"
- Vamos agora ver a constante na fórmula do IC que vimos acima
- Podemos defini-la como:
$$P(-z_{0}<\mathcal{U}<z_{0})=1-\alpha$$
![[z1-a.2.png]]
- Assim, a notação mais correta é: $$\Huge\boxed{z_{1- \tfrac{\alpha}{2}}}$$
Usamos $1-\alpha/2$ porque podemos ver que "$z_{0}$" se encontra onde temos a probabilidade:
$$P(z<z_{0})=1- \frac{\alpha}{2}$$
- Para ver isto numa tabela de $N(0,1)$ procuramos o valor de $z$ em que temos a probabilidade desejada: $1-\alpha/2$ . Na coluna do lado esquerdo temos as unidades e décimas, na linha superior temos as centésimas. Juntos formam o valor: $1.23$

- Ou seja:
$$\overline{X} \pm z_{1- \frac{\alpha}{2}} \frac{\sigma}{\sqrt{n}}$$

### 1.3.2 - IC para $\sigma^{2}$ desconhecido
- Este caso é o mais realista e comum. Basicamente nunca conhecemos $\sigma^{2}$ com antecedência
- Vimos que:
$$\overline{X}\sim N(\mu,\sigma^{2}) \quad\to\quad \frac{\overline{X}-\mu}{\sigma/\sqrt{n}}\sim N(0,1)$$
E quando não conhecemos $\sigma^{2}$ apenas temos $$S^{2}=\frac{1}{n-1} \sum (X_{i}-\overline{X})^{2}$$
Assim temos:
$$T=\frac{\overline{X}-\mu}{S/\sqrt{n}}\sim t_{n-1}$$
ou seja, temos uma distribuição **T-STUDENT**.

- Assim temos:
$$\overline{X}\pm t_{1- \frac{\alpha}{2}} \frac{S}{\sqrt{n}}$$
- Funciona exatamente da mesma forma que vimos na distribuição normal reduzida
- Para usar a tabela:
    - A coluna da esquerda tem os $\nu$'s, ou seja, vamos para onde temos $\nu=n-1$
    - Dentro dessa linha, vamos para a coluna onde temos em cima  $\alpha/2$! De realçar que temos logo *alpha a dividir por dois!!!*
    - A probabilidade que a tabela nos dá é $P(t>t_{1-\alpha/2})$. Na distribuição normal temos $P(z<z_{1-\alpha/2})$.

### 1.3.3 - IC para a variância de um pop normal
- Ou seja, queremos saber $\sigma^{2}$ e assumimos que $X\sim N(\mu,\sigma^{2})$
- Tal como atrás, determinamos a estimação de $\sigma^{2}$ usando a população $(X_{1},X_{2},\dots,X_{n})$: $$S^{2}=\frac{1}{n-1}\sum\limits (X_{i}-\overline{X})^{2}$$
- Podemos escrever: 
$$\begin{align*}
\sum\limits(X_{i}-\mu)^{2}&= \sum\limits \left[X_{i}-\overline{X}+\overline{X}-\mu \right]^{2}\\
&= \sum\limits(X_{i}-\overline{X})^{2}+\sum\limits(\overline{X}-\mu)^{2} + 2\sum\limits (X_{i}-\overline{X})(\overline{X}-\mu)\\
&= (n-1)S^{2} + n(\overline{X}-\mu)^{2} +0\\
\sum\limits \frac{(X_{i}-\mu)^{2}}{\sigma^{2}} &= \frac{(n-1)S^{2}}{\sigma^{2}} + \frac{(\overline{X}-\mu)^{2}}{\frac{\sigma^{2}}{n}}
\end{align*}$$
e é possível demonstrar (mas não vamos) que
$$\sum\limits\frac{(X_{i}-\mu)^{2}}{\sigma^{2}}\sim \chi^{2}(n) \quad;\quad \frac{(\overline{X}-\mu)^{2}}{\frac{\sigma^{2}}{n}}\sim \chi^{2}(1)$$
- Ou seja, tem-se que:
$$\frac{(n-1)S^{2}}{\sigma^{2}}\sim \chi^{2}(n-1)$$
e temos algo assim
![[distribuicao chi2 para diferente n.png]]

- E para ter o IC temos que determinar $a,b$ de modo que 
![[alpha em chi2.png]]

- Ou seja, queremos que:
$$\begin{align*}
P \left(a <  \frac{(n-1)S^{2}}{\sigma^{2}}<b \right)&= 1-\alpha\\
P \left(a\sigma^{2} <  (n-1)S^{2}<b\sigma^{2} \right)&= 1-\alpha\\
P \left(\frac{(n-1)S^{2}}{b}<\sigma^{2}<\frac{(n-1)S^{2}}{a} \right)&= 1-\alpha\\
\end{align*}$$
e temos o IC:
$$\text{IC}\to \left]\frac{(n-1)S^{2}}{b}, \frac{(n-1)S^{2}}a{}\right[$$
em que $a,b$ são tirado da tabela de chi quadrado.

>[!INFO] EX
>Consideremos que $n=35$
>Conforme a imagem acima, queremos que $P(\chi_{34}^{2}<a)=\frac{\alpha}{2}$. Assim, basta ir à tabela e ver o $a$ que nos dá isto
>Para $\alpha=5\%$ temos $P(\chi_{34}^{2}>a)=0.975$ logo $a=19.8063$
>De igual modo, queremos que $P(\chi_{34}^{2}>b)=0.025$ logo $b=51.966$

#### Distribuição aproximada de $S^{2}$
- Vimos que $\frac{(n-1)S^{2}}{\sigma^{2}}\sim \chi^{2}(n-1)$ 
- Tem-se que o valor médio de uma VA com distribuição $\chi^{2}(\nu)$ é $\nu$. Similarmente, a sua variância é $2\nu$
- Ou seja:
    - $E(S^{2})=\sigma^{2}$
    - $V(S^{2})=\frac{2\sigma^{4}}{n-1}$
- Se $\nu$ for suficientemente grande podemos aproximar isto a uma dist normal:
$$\nu\gg1 \to S^{2}\sim N(\nu,2\nu)=N \left(\sigma^{2}, \frac{2\sigma^{4}}{n-1} \right)$$

### 1.3.4 - IC para diferença de médias $\mu_{1}-\mu_{2}$ de pops normais com Var conhecida
- Ou seja, temos $X_{1}\sim N(\mu_{1},\sigma_{1}^{2})~,~X_{2}\sim N(\mu_{2},\sigma_{2}^{2})$ e temos as populações: $(X_{1}^{1},X_{2}^{1},\dots,X_{n_{1}}^{1})~,~(X_{1}^{2},X_{2}^{2},\dots,X_{n_{2}}^{2})$
- Como já vimos, temos que $$\overline{X}_{1}\sim N\left(\mu_{1},\frac{\sigma_{1}^{2}}{n_{1}}\right) \quad;\quad \overline{X}_{2}\sim N\left(\mu_{2},\frac{\sigma_{2}^{2}}{n_{2}}\right)$$
- Definimos uma nova VA: $D=\overline{X}_{1}-\overline{X}_{2}$
    - $E(D)=E(\overline{X}_{1}-\overline{X}_{2})=E(\overline{X}_{1})-E(\overline{X}_{2})=\mu_{1}-\mu_{2}$
    - $V(D) = V(\overline{X}_{1}- \overline{X}_{2})=V(\overline{X}_{1})+V(\overline{X}_{2})=\frac{\sigma^{2}_{1}}{n_{1}} + \frac{\sigma_{2}^{2}}{n_{2}}$
nota: Separamos $V(a-b)=V(a)+V(b)$ porque $a,b$ são *independentes*

- Podemos então definir que
$$D\sim N \left(\mu_{1}-\mu_{2} , \frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}} \right)$$
e podemos passar à forma reduzida:
$$\frac{D - (\mu_{1}-\mu_{2})}{\sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}}}\sim N(0,1)$$
![[chi2 reduzida.png]]
- Então, usando a tabela de $N(0,1)$ queremos determinar $z_{0}$ tal que:
$$P \left(-z_{0} < \frac{D - (\mu_{1}-\mu_{2})}{\sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}}} < z_{0} \right) = 1-\alpha $$ e o IC é definido por
$$D \pm z_{1- \alpha/2} \sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}}$$

### 1.3.5 - IC para diferença de médias $\mu_{1}-\mu_{2}$ de pops normais com Var desconhecidas mas iguais
- O mais frequente é não saber a variância
- Ou seja, temos: $X_{1}\sim N(\mu_{1},\sigma_{1}^{2})~,~X_{2}\sim N(\mu_{2},\sigma_{2}^{2})$ 
- Tal como já vimos, as médias amostrais terão as distribuições $\overline{X}_{1}\sim N(\mu_{1},\frac{\sigma_{1}^{2}}{n_{1}})~,~ \overline{X}_{2}\sim N(\mu_{2},\frac{\sigma_{2}^{2}}{n_{2}})$ 
- Ou seja, tal como vimos no caso anterior:
$$D= \overline{X}_{1}-\overline{X}_{2}\sim N \left(\mu_{1}-\mu_{2}, \frac{\sigma_{1}^{2}}{n_{1}} + \frac{\sigma_{2}^{2}}{n_{2}} \right)$$
e, novamente:
$$\frac{D - (\mu_{1}-\mu_{2})}{\sqrt{\frac{\sigma_{1}^{2}}{n_{1}}+\frac{\sigma_{2}^{2}}{n_{2}}}}\sim N(0,1)$$

- Não conhecemos a variância, então determinamos as variãncias amostrais das 2 populações:
$$S_{1}^{2}=\frac{1}{n_{1}-1} \sum (X^{1}_{i}-\overline{X}^{1})^{2} \quad;\quad S_{2}^{2}=\frac{1}{n_{2}-1} \sum (X^{2}_{i}-\overline{X}^{2})^{2}$$
- No entanto, como estamos a assumir que $\sigma_{1}^{2}=\sigma_{2}^{2}=\sigma^{2}$, fazemos uma *média ponderada* das variâncias amostrais:
$$S_{p}^{2}=\frac{(n_{1}-1)S_{1}^{2} + (n_{2}-1)S_{2}^{2}}{n_{1}+n_{2}-2}$$
- Pode ainda ser provado que
$$\frac{(\overline{X}_{1}-\overline{X}_{2}) - (\mu_{1}-\mu_{2})}{S_{p} \sqrt{\frac{1}{n_{1}} + \frac{1}{n_{2}}}}\sim t(n_{1}+n_{2}-2)$$
- E o IC é:
$$(\overline{X}_{1}-\overline{X}_{2})\pm t_{1-\alpha/2} S_{p}\sqrt{\frac{1}{n_{1}}+ \frac{1}{n_{2}}}$$
- Usamos a tabela de t-student. Encontramos a distribuição $t_{n_{1}+n_{2}-2}$ e vemos o $t_{0}$ para o qual temos: $P(t_{n_{1}+n_{2}-2}<t_{0})=1-\alpha/2$

### 1.3.6 - IC para a razão entre 2 variâncias de pops normais
- Para as médias é interessante ver a diferença entre 2 populações.
- Mas para variâncias é mais interessante/útil ver a razão $\sigma_{1}^{2}/\sigma_{2}^{2}$
- Mas nunca conhecemos as variâncias de antemão. Então usamos as variâncais de 2 amostras independentes (uma de cada população)

- Ou seja, temos $X_{1}\sim N(\mu_{1},\sigma_{1}^{2})~,~X_{2}\sim N(\mu_{2},\sigma_{2}^{2})$
- Novamente, determinamos as variâncias amostrais: $S_{1}^{2}=\frac{1}{n_{1}-1} \sum (X^{1}_{i}-\overline{X}^{1})^{2} ~,~ S_{2}^{2}=\frac{1}{n_{2}-1} \sum (X^{2}_{i}-\overline{X}^{2})^{2}$
- Da mesma forma que vimos acima, temos:
$$\begin{align*}
Z &= \frac{(n_{1}-1)S_{1}^{2}}{\sigma_{1}^{2}}\sim \chi_{n_{1}-1}^{2}\\
W &= \frac{(n_{2}-1)S_{2}^{2}}{\sigma_{2}^{2}}\sim \chi_{n_{2}-1}^{2}
\end{align*}$$
logo temos
$$\frac{\frac{Z}{n_{1}-1}}{\frac{W}{n_{2}-1}} \sim F_{n_{1}-1,n_{2}-1}$$
em que temos a distribuição F (*Fisher-Snedecor*)

- Podemos escrever:
$$\frac{\tfrac{\tfrac{(n_{1}-1)S_{1}^{2}}{\sigma_{1}^{2}}}{n_{1}-1}}{\tfrac{\tfrac{(n_{2}-1)S_{2}^{2}}{\sigma_{2}^{2}}}{n_{2}-1}}= \frac{S_{1}^{2}}{S_{2}^{2}} \frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}\sim F_{n_{1}-1,n_{2}-1}$$
![[dist F alpha.png]]

- Para determinar o IC fazemos
$$\begin{align*}
P\left(a < \frac{S_{1}^{2}\sigma_{2}^{2}}{S_{2}^{2}\sigma_{1}^{2}}<b\right)&= 1-\alpha\\
P\left(a \frac{S_{2}^{2}}{S_{1}^{2}} < \frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}< b \frac{S_{2}^{2}}{S_{1}^{2}}\right)&= 1-\alpha\\
P \left(\frac{S_{1}^{2}/S_{2}^{2}}{a}> \frac{\sigma_{1}^{2}}{\sigma_{2}^{2}} > \frac{S_{1}^{2}/S_{2}^{2}}{b}\right)&= 1-\alpha\\
\end{align*}$$
e o IC será:
$$\text{IC}~~\to~~ \left]\frac{S_{1}^{2}/S_{2}^{2}}{b},\frac{S_{1}^{2}/S_{2}^{2}}{a} \right[$$

>[!NOTE] EX
>Consideremos que temos $n_{1}=61,n_{2}=42,\alpha=10\%$
>Temos que $b$ é dado por $P(F_{60,41}>b)=\frac{\alpha}{2}=0.05$. Consultando a tabela F vemos que $b=1.64$
>Já para $P(F_{60,41}>a)=0.95$ não temos nada na tabela que nos ajude. Então fazemos a seguinte aproximação: $$a=\frac{1}{F_{41,60}(1-0.95)}=0.629$$

### 1.3.7 - IC de proporção
- Proporções são fundamentais em estudos estatísticos (EX: porção de pacientes que recuperaram com um certo tratamento)
- Vamos ver isto com um exemplo concreto
#### EXEMPLO
- Temos 1000 eleitores. Destes, 350 são a favor e 650 contra o candidato A. Queremos um IC com 99% oara a percentagem de eleitores favoráveis a A.
- Definimos $X$ como sendo a VA "número de pessoas que apoiam A"
- Como para cada pessoa consideramos que ela é favorável (sucesso) ou não é (fracasso), esta VA terá distribuição *binomial* (cada pessoa é um teste de bernoulli): $X\sim \text{Bi}(n,p)$ e em que $p$ é a probabilidade de alguém apoiar A.
- Ora, temos que a *proporção* de pessoas **da amostra** que apoiam A será: $P = \frac{X}{n}$. O IC será para a proporção **da população** : $p$ (não confundir com a probabilidade acima lol)

- Se $n$ for elevado, pelo teorema de Moivre-Laplace, teremos
$$X \sim N(np,npq)$$
- Como $P=X/n$ temos:
    - $E(P)=\frac{1}{n}E(X)=p$
    - $V(P)=\frac{1}{n^{2}}V(X)=\frac{pq}{n}$
- Ou seja: $$P\sim N\left(p, \frac{pq}{n}\right) \quad\to\quad \frac{P-p}{\sqrt{\frac{pq}{n}}}\sim N(0,1)$$
- Assim o IC é definido por:
$$\begin{align*}
P \left(-z_{0} < \frac{P-p}{\sqrt{pq/n}} < z_{0}\right) &= 1-\alpha\\
P \left(-z_{0} \sqrt{\frac{pq}{n}}< P-p < z_{0}\sqrt{p1}\right) &= 1-\alpha\\
P \left(P-z_{0} \sqrt{\frac{pq}{n}}< p < P+z_{0}\sqrt{p1}\right) &= 1-\alpha\\
\end{align*}$$
e o IC é: $$P\pm z_{1-\alpha/2} \sqrt{\frac{pq}{n}}$$
- Ora, podemos notar que, obviamente, nesta equação temos $p$ e $q=1-p$ que são precisamente a variável que queremos determinar e não conhecemos. Ora, para poder usar este intervalo na prática temos que usar $P,Q$ - as aproximações amostrais.
- Temos então o **intervalo de Wald** que é bastante mau :D
- Mais à frente (noutros ficheiros) iremos ver outros intervalos de proporções melhores

### 1.3.8 - IC da diferença entre 2 proporções
- Temos 2 pops binomiais com parâmetros $n_{1},p_{1},n_{2},p_{2}$:
![[2 pops.png]]
em que $P_{1},P_{2}$ são VAs independentes
- De forma análoga ao que vimos atrás:
$$P_{1}\sim N\left(p_{1}, \frac{p_{1}(1-p_{1})}{n_{1}}\right) \quad;\quad P_{2}\sim N\left(p_{2}, \frac{p_{2}(1-p_{2})}{n_{2}}\right)$$
logo
$$P_{1}-P_{2}\sim N \left(p_{1}-p_{2}, \frac{p_{1}(1-p_{1})}{n_{1}} + \frac{p_{2}(1-p_{2})}{n_{2}}\right)$$
e temos o IC:
$$(P_{1}-P_{2})\pm z_{0} \sqrt{\frac{p_{1}(1-p_{1})}{n_{1}} + \frac{p_{2}(1-p_{2})}{n_{2}}}$$
tal como vimos antes, normalmente não conhecemos $p_{1},p_{2}$ então usamos $P_{1},P_{2}$ no seu lugar.

### 1.3.9 - IC de pops não normais
- *Amostra pequena* - Desigualdade de Tchebycheff permite determinar um IC.
- *Amostra grande* - Usamos o teorema do limite central

#### Teorema Limite Central
- Se $n$ for alto (normalmente consideramos $n>30$), então podemos considerar que a VA tem distribuição *normal*
- Ou seja, nesse caso podemos estudar o problema de inferência exatamente como vimos nos pontos acima


## 1.4 - Testes de hipóteses
- Temos 4 tipos:
    - *Testes de ajustamento* - verificar se a amostra poderá ter sido extraída de uma certa população (como verificar se a amostra pode ter sido tirada de uma dist gaussiana). AKA testes de significância
    - *Testes de indepência* - estudar se 2 parâmetros / critérios de classificação são independentes (como salário VS tendência política). Podem ser considerados casos particulares dos testes de ajustamento.
    - *Testes de homogeneidade ou igualdade* - verificar se 2+ amostras são tiradas da mesma população
    - *Testes sobre parâmetros de populações* - vejamos melhor

### 1.4.1 - Testes sobre parâmetros de populações
- Comparamos uma população teórica a uma observada, tendo-se objetivos mais restritos que nos testes de ajustamento
- Invés de ver se a amostra virá de uma população gaussiana, vemos se vem de uma gaussiana com certa média ou variância
- Ou seja, na prática, é o mesmo que dizermos: $H_{0}: \mu=5$ 

#### Tipos de erro
![[tabela tipos de erro.png]]
- Temos então 2 tipos de erro (tipo I : falsos negativos, tipo II : falsos positivos)
- E podemos definir estes erros como:
    - Tipo I : $RH_{0}|H_{0}V ~~\to~~ \alpha=P(RH_{0}|H_{0}V)$ 
    - Tipo II : $AH_{0}|H_{0}F~~\to~~ \beta=P(AH_{0}|H_{0}F)$
- Na prática, fixamos um limite superior de erro Tipo I. Esse limite é o **nível de significância** $\alpha$! Ou seja, quanto menor este for (e mais próxima de $100\%$ a confiança do IC), menos e menos pontos iremos rejeitar então menos ocorrem erros Tipo I.

#### Potência do teste
- Consiste na probabilidade de rejeitar $H_{0}$ quando esta hipótese é de facto falsa: $$P(RH_{0}|H_{0}F)=1-\beta$$
- Esta probabilidade depende do "quão falsa" a hipótese $H_{0}$ é, mas também depende do quão provável é rejeitarmos uma hipótese $H_{0}$.

### 1.4.2 - Testes unilaterais
- Um teste bilateral é algo do tipo "ver se a média é igual ou não a X". 
- Um teste unilateral será algo do tipo "ver se a média é superior a Y"
- Apesar de parecer bastante diferente, este tipo de problemas pode ser resolvido usando ICs. Para isso, definimos a hipótese nula de forma diferente: $H_{0}: \mu \le \mu_{0} \quad;\quad H_{1}: \mu>\mu_{0}$ 
    - Rejeitamos $H_{0}$ se $\mu\gg\mu_{0}$
    - Ora, podemos definir $U_{0}=\frac{\overline{X}-\mu_{0}}{\sigma/\sqrt{n}}\sim N(0,1)$ e rejeitamos $H_{0}$ de $U_{0}$ for *elevado*
        - Rejeitamos com 95% de confiança se $U_{0}>1.96$
        - No caso *bilateral* rejeitariamos se $U_{0}>1.96$ OU $U_{0}<-1.96$

