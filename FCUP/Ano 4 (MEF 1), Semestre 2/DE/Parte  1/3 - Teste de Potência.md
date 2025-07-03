- Antes de ver a tabela, que à primeira me fez confusão, temos isto:
![[explicacao h0.png]]
- Esta "contradição" de dizer que temos um TP (true positive) quando H0 é falso e rejeitamos, vem da forma como definimos H0. Normalmente, esta hipótese é algo "nulo" ou "neutro". 
- No caso médico, podemos ter $H_{0}$ a ser "a doença não está presente na pessoa". 
    - Assim, se uma pessoa tiver a doença, $H_{0}$ é *falso* -- a pessoa está *positiva* para a doença. 
    - Similarmente, se essa pessoa fizer o teste e der *positivo*, então rejeitamos H0 --> É FALSO que a doença não está na pessoa
    - Logo temos um *TP* se a pessoa tiver a doença e ela for detetada num teste: H0 é falso em ambos os casos.

- Podemos definir:
![[tabela hipoteses e erros.png]]
ou seja, como já indicado nesta tabela:
$$\begin{align*}
\alpha&=  p (\text{rejeitar }H_{0}~|~ H_{0} \text{ verdadeiro})\\
\beta&= p(\text{não rejeitar }H_{0}~|~H_{0}\text{ falso})
\end{align*}$$
- Por outras palavras, $\alpha$ é a probabilidade de ter um Falso Positivo (FP) e $\beta$ a probabilidade de ter um Falso Negativo (FN)
- Por sua vez, isto quer dizer:
$$\begin{align*}
\alpha&= p(\text{Erro Tipo I})\\
\beta&= p(\text{Erro Tipo II})
\end{align*}$$
- Acima de tudo, notemos que $\alpha$ é precisamente a **significância** (ou o $1-\alpha$ da confiança).
    - Em geral, escolhemos $\alpha$ como sendo um valor pequeno
- Ora, temos que a **potência do teste** é $1-\beta=p(\text{rejeitar }H_{0}~|~H_{0}\text{ falso})$
    - Queremos que seja reduzido, claro, mas este depende mais do contexto do teste
    - Podemos deifnir a potência como: a probabilidade de o teste rejeitar H0 de forma correta OU SEJA a probabilidade de detetar um fenómeno com sucesso. Logo, isto é algo claramente importante

- Ou seja, notemos que:
    - $\alpha$ reduzido implica que conseguimos evitar a maioria dos FPs
    - No entanto, se este for muito reduzido, eventualmente iremos rejeitar casos que não devíamos (FN) - logo $\beta$ aumenta. 
    - Podemos ver este caso de rejeitar casos verdadeiros como estando a ignorar efeitos reais, ou seja, casos em que o comportamento/fenómeno/relação em estudo se verifica mesmo.

- Ou seja, resumimos tudo em poucas palavras:
    - $\alpha$ / pvalue medem a chance de encontrar algo que não está lá (reduzimos FP mas acabamos a não rejeitar demasiadas coisas)
    - $\beta$ medem a chance de encontrar um efeito real

### EXEMPLO
**Contexto**
- Numa certa área a radiação p/ pessoa segue uma distribuição normal $N(\theta_{0},\sigma^{2})$ em que $\theta_{0}=1.2,\sigma^{2}=0.09$
- Quer-se construir uma central nuclear na área. A hipótese que a central não tem efeito na radiação é a hipótese nula $H_{0}: \theta=\theta_{0}$. Logo, claro, $H_{1}:\theta\neq\theta_{0}$
- No ano seguinte, obtém-se uma amostra $X_{1},X_{2},\dots,X_{n}$ da população em que $X_{i}\sim N(\theta,\sigma^{2})$ em que:
    - $\theta=\theta_{0}$ se a central não for construida
    - $\theta\in\mathbb{R}_{0}^{+}$ desconhecido se a central for contruida

**Testagem**
- Consideremos que $\alpha=0.05$ (5% probabilidade de ter um FP). Fazemos isto porque é preferível achar que a radiação irá aumentar e não chegar a acontecer isso (perigo evitado). No caso de um FN, não estaremos a fazer nada para evitar o perigo.
- Podemos fazer 2 testes:
    - $T_{1}$ - rejeitamos $H_{0}$ se $|\overline{X}-\theta_{0}|>a$ -> Bilateral, vemos se $\theta_{0}$ varia
    - $T_{2}$ - rejeitamos $H_{0}$ se $\overline{X}>\theta_{0}+b$ -> Unilateral, vemos se $\theta_{0}$ estritamente aumenta (o caso que importa neste cenário)
- Rejeitamos T1 se:
$$\begin{align*}
P(\overline{X}-\theta_{0}>a)&= 1-\alpha\\
P\left(\frac{\overline{X}-\theta_{0}}{\sigma/\sqrt{n}}>\frac{a}{\sigma/\sqrt{n}}\right)&= 1-\alpha=P(T>z_{1-\alpha/2})\\
P\left(T>\frac{a}{\sigma/\sqrt{n}}\right)&= 1-\alpha=P(T>z_{1-\alpha/2})
\end{align*}$$
logo temos:
$$z_{1-\alpha/2}~\stackrel{95\%}{=}~1.96=\frac{a}{\sigma/\sqrt{n}}~~\to~~ a=\frac{1.96\sigma}{\sqrt{n}}$$
- Rejeitamos o T2 se:
$$\begin{align*}
P(\overline{X}-\theta_{0}>a)&= 1-\alpha\\
P\left(\frac{\overline{X}-\theta_{0}}{\sigma/\sqrt{n}}>\frac{a}{\sigma/\sqrt{n}}\right)&= 1-\alpha=P(T>z_{1-\alpha})\\
P\left(T>\frac{a}{\sigma/\sqrt{n}}\right)&= 1-\alpha=P(T>z_{1-\alpha})
\end{align*}$$
logo temos:
$$z_{1-\alpha}~\stackrel{95\%}{=}~1.64=\frac{b}{\sigma/\sqrt{n}}~~\to~~ b=\frac{1.64\sigma}{\sqrt{n}}$$

**Potência dos testes - T1**
$$\begin{align*}
f(\theta)&= P(\text{rejeitar }H_{0}~|~\theta\neq \theta_{0})\\
&= P_{\theta}(|\overline{X}-\theta_{0}|>a)\\
&= 1- P_{\theta}(-a\le \overline{X}-\theta_{0}\le a)\\
&= 1-P_{\theta}(\theta_{0}-a\le \overline{X}\le \theta_{0}+a)\\
&= 1-P_{\theta} \left(\frac{-a +\theta_{0}-\theta}{\sigma/\sqrt{n}}\le \frac{\overline{X}-\theta}{\sigma/\sqrt{n}} \le \frac{a+\theta_{0}-\theta}{\sigma/\sqrt{n}} \right)\\
&= 1- \left[\Phi \left(\frac{a +\theta_{0}-\theta}{\sigma/\sqrt{n}} \right) - \Phi \left(\frac{-a +\theta_{0}-\theta}{\sigma/\sqrt{n}} \right)\right]\\
&= 1- \left[\Phi\left(1.96 + \frac{1.2-\theta}{0.3}\sqrt{n}\right)  - \Phi\left(-1.96+ \frac{1.2-\theta}{0.3}\sqrt{n}\right) \right]
\end{align*}$$


**Potência dos testes - T2**
$$\begin{align*}
g(\theta)&= P(\text{rejeitar }H_{0}~|~\theta\neq \theta_{0})\\
&= P_{\theta}(\overline{X}>\theta_{0}+b)\\
&= 1- P_{\theta}(\overline{X}\le \theta_{0}+b)\\
&= 1-P_{\theta}\left(\frac{\overline{X}-\theta}{\sigma/\sqrt{n}}\le \frac{b+\theta_{0}-\theta}{\sigma/\sqrt{n}} \right)\\
&= 1- \Phi \left(\frac{b+\theta_{0}-\theta}{\sigma/\sqrt{n}} \right)\\
&= 1-\Phi \left(1.96 + \frac{1.2-\theta}{0.3}\sqrt{n} \right)
\end{align*}$$

**Resultado**
- Temos então que a potência de T1 e T2 ($f,g$) são funções de $\theta,n$ e temos:
![[teste potencia resultado.png]]
- Normalmente escolhemos o tamanho da amostra $n$ de forma a garantir que:
    - a probabilidade de conseguirmos detetar uma diferença em $\theta$ (ou seja, o **efeito mínimo** que queremos distinguir) seja **igual ou superior** a um valor que definimos previamente — essa probabilidade é chamada de **potência** do teste.
- No caso deste problema exemplo: Vemos que $g(\theta)$ (T2) tem maior potência para $\theta>\theta_{0}$. Assim, esta é a melhor opção se *tivermos a certeza* que este não será menor que $\theta_{0}$.

## Notas sobre o documento com código R
- Muitas vezes o nosso foco está no *pvalue*, que estima a chance de erro Tipo I - FP / Falsos alarmes
- Aliás, em certos testes ignoramos mesmo os erros Tipo II, que estima a chance de não identificar um efeito real.
- Ou seja, em certos casos, ao fazer um teste tipo T-test podemos não conseguir obter o pvalue desejado. Ora, isso não significa necessariamente que precisamos de ir recolher mais dados e repetir.
- Invés disso, podemos:
    - Estudar a qualidade dos dados usados
    - Verificar se o efeito em estudo (H0) pode não acontecer de todo
    - Só depois podemos concluir que serão precisos mais dados

- A potência depende de 3 parâmetros principais:
    - A significância $\alpha$ (a chance de acontecer erros Tipo I)
    - A reliability da amostra e o seu tamanho: erros de medições muito variáveis reduzem a reliability. Remover variabilidades que não afetam o fenómeno em estudo aumentam reliability.
    - Effect Size (ES) - o quanto o fenómeno em estudo ocorre
- Deste, o mais importante de longe é o ES. Este pode ser estimado através de experiências anteriores semelhantes
- No documento é feito t-test entre 2 sets de dados com 100 pontos e com médias 10, 10.5. Num teste usando os 100 pontos conseguimos com baixo pvalue dizer que têm médias diferentes. No entanto, se só usarmos 10 pontos, já não temos tanta confiança.

### PWR
- Esta é a biblioteca que iremos usar.
- Recebe 4 variáveis (mínimo):
    - tamanho da amostra(s)
    - ES
    - nível significância (ou pvalue)
    - potência
- Quando não sabemos 1 destes mas sabemos os outros, colocamos o desconhecido com valor `NULL` e o programa determina-o.

### Amostras independentes
#### Estimar Potência - $1-\beta$
- Para estimar o ES, **no caso de t-test** usamos o $d$ de Cohen:
$$d = \frac{|\overline{X_{A}} - \overline{X_{B}}|}{\sqrt{\frac{S_{A}^{2}+S_{B}^{2}}{2}}}$$
ou, em R:
```R
d <- abs(mean(groupA[1:10])-mean(groupB[1:10])) / sd(c(groupA[1:10]-mean(groupA[1:10]), groupB[1:10]-mean(groupB[1:10])))
```
notemos: a porção com `c(...)` cria uma lista 1D com os elementos de A e B com as suas médias subtraídas. A função `sd` calcula então o desvio padrão desta lista.

- E fazemos o teste:
```R
test <- pwr.t2n.test(n1=10,n2=10,d,sig.level=.05,power=NULL)
test <- pwr.t.test(n=10,d,sig.level=.05)
```
isto determina a potência. Se fizermos `plot(test)`, iremos ver um gráfico com o compromise potência - tamanho amostra.
![[test potencia 1.png]]
- Com os 10 pontos que estávamos a usar, temos uma potência de ~15% logo temos 85% chances de Erro Tipo II -> HORRÍVEL. 
    - Por outras palavras, 85% das vezes não seria detetada diferença entra as médias das amostras (que sabemos que são diferentes)

#### Estimar tamanho da amostra - $n$
- Normalmente queremos:
    - Potência de 0.8 (80% chances de encontrar o efeito real)
    - P value de 0.05 (5% chance de encontrar um efeito que não está lá)
- Usamos `pwr.t.test` porque força A,B a terem o mesmo tamanho.
```R
test <- pwr.t.test(d=d, sig.level=0.05, power=0.8)
```
- Este teste diz-nos o valor de $n$ optimo, que permite chegar o mais perto possível deste $\alpha,1-\beta$. Ao fazer plot, obtemos o gráfico para este cenário:
![[test potencia 2.png]]
- OK, precisamos de 40 pontos por dataset. Tudo muito bonito, mas se isto for um estudo real em que cada "ponto" é uma pessoa de um grupo, isto rapidamente fica muito caro.

#### Estimar ES - $d$
- Consideremos que temos budget para ter 20 pessoas em caa grupo.
- Fazemos simplesmente `pwr.t.test`:
```R
test <- pwr.t.test(sig.level=0.05, n=20, power=0.8)
```
e obtemos uma estimativa do $d$ que permite ter o $\alpha,\beta$ desejados. 
- No caso que vimos acima, temos que $d\simeq0.9$
- Ou seja, se conseguirmos reduzir variabilidade do teste de modo que o $d$ de Cohen dê 0.9, o teste funcionará bem com $n=20$ pessoas.

#### Estimar p-value
- Consideremos agora que sabemos que $d=0.6$ e só temos budget para $n=20$ pessoas. 
- Simplesmente fazemos:
```R
test <- pwr.t.test(n=20, d=0.6, power=0.8, sig.level=NULL)
```
e vemos que temos $\alpha=0.295$. Isto é demasiado elevado e inaceitável em alguns contextos.
- Similarmente, se reduzirmos a potência para 0.76 teremos $\alpha=0.24$
    - Neste caso, as chances de erros tipo I e II

### Amostras paired
- Acima vimos como fazer a análise para amostras independentes
- Vejamos agora como trabalhar com amostras emparelhadas OU como analisar 1 só amostra.

#### Potência de teste de 2 medições da mesma amostra
```R
test <- pwr.t.test(n=50, d=0.4, sig.level=0.05, type='paired')
```
- Isto dá uma potência de 0.8
- Este teste é usado para 2 sets de valores, que correspondem a 2 sets de medições da mesma amostra
- Também pode ser um estudo do desempenho de um conjunto de pessoas em 2 condições diferentes

**Independentes**
```R
test <- pwr.t.test(n=50,d=.4,sig.level=.05,type="two.sample")
```
- A linha acima faz o teste como vimos nos pontos atrás: considerando amostras independentes. Aqui apenas explicitamos, já que 'two.sample' é o valor default

#### Potência de teste de 1 amostra
```R
test <- pwr.t.test(n=50, d=0.4, sig.level=0.05, type="one.sample")
```
- Este é o teste que fazemos quando queremos ver se a média de um set de dados é ou não zero (ou outro valor)

### Potência de Correlações
- Quando estamos a estudar a correlação de amostras, o $r$ é precisamente o ES ($d$). Assim, à exceção desta variável, usamos tudo como igual.
- Consideremos que num estudo, temos uma correlação máxima de 0.3. Fariamos:
```R
test <- pwr.r.test(n=NULL, r=0.3, sig.level=0.05, power=0.8)
```
(Notemos o `r` invés de `t` na função!!)
- Ao fazer o plot vemos que o número ideal de pontos da amostra é $n=85$, que é extremamente alto.

## Teste Potência Não-Paramétricos
- Podemos ter dados que são duma população não gaussiana ou até ordinal (pequeno, médio, grande).
- Um método chamado de não-paramétrico assume muito pouco sobre a população e abdica até da necessidade da população ser normal.
- Estes são, de longe, os métodos mais utilizados IRL

**Estatísticas de Ordem**
- Dada uma sequência de VAs (assumimos independentes) $X_{1},X_{2},\dots,X_{n}$, reescrevemos em ordem *crescente*: $X_{(1)}\le X_{(2)}\le\dots\le X_{(n)}$ 
- O termo de ordem $k$ desta sequência ordenada é a k-ésima estatística de ordem

### Teste dos sinais (1 amostra)
- Teste de localização da mediana. Seja, $\tilde{\mu}$ a mediana, temos:
$$H_{0}: \tilde{\mu}=\tilde{\mu}_{0}\quad;\quad H_{1}:\tilde{\mu}\neq\tilde{\mu}_{0}$$
- Criamos o seguinte set: $(X_{1},X_{2},\dots,X_{n})\to(X_{1}-\tilde{\mu}_{0}, X_{2}-\tilde{\mu}_{0},\dots,X_{n}-\tilde{\mu}_{0})$
- E contamos quantos valores deste novo set tem sinal positivo
- Existe $\frac{1}{2}$ de probabilidade de o sinal ser positivo ou negativo
- Assim, o número de sinais positivos segue a distribuição $\text{B}(n, \frac{1}{2})$
- Neste teste, os valores *zero* são removidos.
- Estamos a perder MUITA informação: convertemos dados absolutos em nominais.

**EXEMPLO**
- Num certo set de 10 números, queremos testar $H_{0}:\tilde{\mu}=1.70$
- Fazemos o novo set, temos 4 valores positivos, 1 zero e 5 negativos. Removemos o zero.
- Temos então $n=9$ valores e podemos estimar a distribuição $X\sim\text{B}(9, \frac{1}{2})$ 
- Ao ir à tabela de Binomial temos que: $P(X\le4)=0.5$. Como temos um teste binomial, fazemos $2P(X\le4)=1$
    - Claramente, não rejeitamos $H_{0}$

### Teste dos sinais (2 amostras emparelhadas)
- Temos agora um estudo sobre na libertação de um certo químico por mulheres grávidas. Queremos ver se este segue a mesma distribuição de dia e de noite. Assim, temos 2 sets de dados emperalhados (são relativos às mesmas grávidas)
![[exemplo test design.png]]
- Definimos então $H_{0}:X\stackrel{d}{=}Y$ (distribuição igual).
- Para testar isto, vemos ser $X-Y=0$
- Se $H_{0}$ for verdade, teremos probabilidades iguais de $x_{i}-y_{i}>0~,~x_{i}-y_{i}<0$. 
- E pronto, simplesmente fazemos a mesma coisa que antes. Definimos a VA: $N\equiv\text{Numero de sinais positivos na diferença }X-Y$ 
- Novamente, temos $N\sim B(n,\frac{1}{2})$
- Basicamente, convertemos os dados $X,Y$ num set de 1 amostra $(X-Y)$ e estudá-mo-lo com o método que vimos acima. Se a mediana desse $\tilde{\mu}$ for nula, então $X\stackrel{d}{=}Y$

### Teste de Wilcoxon (2 amostras emparelhadas)
- Usamos o sinal E o rank (posição no set ordenado)
- Também podemos usar este teste para testar hipóteses sobre a mediana de uma VA que *assumimos simétrica* (distribuição simétrica, pouco bias)
- Fazemos uma coisa assim:
![[exemplo test design 2.png]]
- Notemos que $R_{i}^{*}$ é $R_{i}\times\text{sinal}$ 
- Podemos usar estes dados de várias formas:
    - Usar a estatística $W=\sum_{i=1}^{n}R_{i}^{*}$
    - Usar a estatística de soma de ranks positivos $T^{+}=\sum_{i=1}^{n}R_{i}\psi_{i}~~~,~~\psi_{i}=\begin{cases}1&,&Z_{i}>0\\0&,&Z_{i}<0\end{cases}$ 
    - Usar a estatística de soma de ranks negativos $T^{-}=\sum_{i=1}^{n}R_{i}(1-\psi_{i})~~~,~~\psi_{i}=\begin{cases}1&,&Z_{i}>0\\0&,&Z_{i}<0\end{cases}$
- Aliás, temos:
$$W=T^{+}+T^{-}=T^{+}- \left(\tfrac{n(n+1)}{2} - T^{+} \right)=2T^{+}-\tfrac{n(n+1)}{2}$$
- Consideremos que temos $n=4$. Como $W$ consiste de uma coma de ranks com sinais diferentes, este tem apenas alguns valores possíveis:
$$W= \begin{cases}
1+2+3+4=10 &,& -1+2+3+4=8 \\
1-2+3+4=6 &,& 1+2-3+4=4 \\
1+2+3-4=2 &,& -1+2+3-4=0 \\
&\vdots&
\end{cases}$$
- No total há 16 combinações. Ao fazer todas e ver quantas vezes cada soma acontece, temos a seguinte distribuição:
![[valores possiveis e probs de W.png]]
vemos daqui que qualquer rank relativizado $R_{i}^{*}$ tem igual probabilidade de ser positivo ou negativo.
- Consideremos que foi previamente establecido que o critério de rejeição de $H_{0}$ é $|W|\ge8$. Nesse caso temos: $\alpha=P(|W|\ge 8~|~H_{0}\text{ verdadeiro})=0.25$
    - Vemos daqui que, com uma amostra tão pequena, é simplesmente impossível atingir significâncias muito reduzida

#### Dist Assintótica de $W$
- Quando $n$ é elevado, mostra-se pelo TLC que:
$$W ~\dot{\sim}~\text{N} \left(0, \frac{n(n+1)(2n+1)}{6} \right)$$

#### Empates
- Pode acontecer termos "empates" em valores $Z_{i}$ (diferenças). Ou seja:
![[exemplo dados empate.png]]
temos 2 valores $Z_{i}$ iguais, logo há 2 ranks iguais.
- Estes empates inflacionam a variância, que corrigimos:
$$\text{Var}(W)=\frac{n(n+1)(2n+1)}{6} - \frac{\sum_{i=1}^{g}(\tau_{i}-1)\tau_{i}(\tau_{i}+1)}{12}$$
em que $g$ é o número de grupos empatados e $\tau_{i}$ o número de empates no grupo $i$.

#### Estatística $T^{+}$ de Wilcoxon
- Como vimos, esta é a estatística de soma de ranks positivos:
$$T^{+}=\sum\limits_{i=1}^{n}R_{i}\psi_{i} \quad \quad ;\quad \psi_{i}=\begin{cases}1&, &Z_{i}>0 \\
0&, &Z_{i}<0
\end{cases}$$
- Adjacentemente, definimos que $$Z_{i}=\theta+e_{i}$$
(consideramos que todos os $e_{i}$ vêm de populações simétricas independentes)

**Caso 1**: $H_{1}:\theta<0$
- Para uma certa significância $\alpha$, rejeitamos $H_{0}$ se tivermos:
$$T^{+}\le t(\alpha,n)$$
em que $t(\alpha,n)$ é uma constante que depende dessas 2 grandezas e satisfaz $P(T^{+}\le t(\alpha,n))=\alpha$.

**Caso 2**: $H_{1}:\theta>0$
- Neste caso, rejeitamos $H_{0}$ se: $$T^{+} \ge \tfrac{n(n+1)}{2} - t(\alpha, n)$$
em que $P(T^{+} \ge \tfrac{n(n+1)}{2} - t(\alpha, n))=\alpha$

**Caso 3**: $H_{1}:\theta\neq0$
- Rejeitamos $H_{0}$ se:
$$T^{+}\le t(\alpha,n) \quad\text{OU}\quad T^{+} \ge \tfrac{n(n+1)}{2} - t(\alpha, n)$$
em que teremos para esse teste bilateral: $\alpha=\alpha_{1}+\alpha_{2}$

#### Distribuição assintótica de $T^{+}$
- Quando $H_{0}$ é verdade, podemos definir:
$$T^{*}=\frac{T^{+}- \mathbb{E}[T^{+}]}{(\text{Var}[T^{+}])^{\frac{1}{2}}}$$
como vimos acima, no caso assintótico:
$$T^{*}=\frac{T^{+} - \frac{n(n+1)}{4}}{\left[\frac{n(n+1)(2n+1)}{24} \right]^{\frac{1}{2}}}~\dot{\sim}~\text{N}(0,1)$$

- Tal como atrás, se houverem $Z_{i}=0$, removemos esses termos e reduzimos $n$ de acordo.

#### Comentários sobre Wilcoxon
- Neste teste vemos se há diferença entre 2 amostras emparelhadas. Para isso, estudamos a mediana da VA da diferença.
- Se tivermos 1 só variável, podemos usar Wilcoxon. Criamos a VA diferença como sendo: $Z_{i}=X_{i}-\tilde{\mu}_{0}$ e podemos testar $H_{0}:\tilde{\mu}=\tilde{\mu}_{0}$

### Teste de Wilcoxon-Mann-Whitney (WMN)
- Temos 2 amostras *independentes* e queremos testar se são da mesma população
    - Por exemplo, para ver se a amostra de controlo e de tratamento pertencem à mesma população.

**EXEMPLO**
- Estamos a testar 2 calmantes A e B para usar em reclusos violentos em motins. Temos 15 voluntários e abaixo os dados com ranks:
![[dados com n diferentes e ranks.png]]
e temos:
$$\begin{align*}
H_{0}&: \text{Não há diferença entre os calmantes A e B}\\
H_{1}&: \text{O calmante B demora mais tempo a atuar} 
\end{align*}$$
- Seja $n$ o tamanho da maior amostra e $m$ o tamanho da outra. Temos $N=n+m$ pontos. Temos as observações $X_{1},\dots,X_{n}~;~Y_{1},\dots,Y_{m}$. 
- Podemos definir que: $X_{i}=e_{i}~~,~~ Y_{j}=e_{n+j}+\Delta$
    - Em que os $e$ são todos independentes e da mesma população

- O teste que estamos a fazer resume-se então a:
$$\begin{align*}
H_{0}&: \Delta=0\\
H_{1}&: \Delta>0
\end{align*}$$
($>$ porque queremos ver se B demora mais a atuar)

- Depois de ordenar os $N$ pontos, temos $T_{m,n}=\sum_{j=1}^{m}R_{j}$ a soma dos ranks da menor amostra
- Rejeitamos $H_{0}$ se $$T_{m,n}\ge t(\alpha,m,n)$$em que $P(T_{m,n}\ge t(\alpha,m,n))=\alpha$
- Não sei porquê, mas temos que:
$$\mathbb{E} \left[T_{m,n} \right]=m \frac{m+n+1}{2}$$

**Caso oposto : Delta < 0**
- Neste caso, analogamente ao que fazíamos nos testes de Wilcoxon, rejeitamos $H_{0}$ se:
$$T_{m,n} \le m(m+n+1) - t(\alpha,m,n)$$
em que $P(T_{m,n} \le m(m+n+1) - t(\alpha,m,n))=\alpha$

**Caso bilateral**
- Tal como para Wilcoxon: rejeitamos H0 se
$$T_{m,n}\ge t(\alpha_{1},m,n) \quad\text{OU}\quad T_{m,n} \le m(m+n+1) - t(\alpha_{"},m,n)$$
em que $\alpha=\alpha_{1}+\alpha_{2}$

#### Dist assintótica de $T_{m,n}$
- Do TLC temos que:
$$\frac{T_{m,n}-\mathbb{E}[T_{m,n}]}{(\text{Var}[T_{m,n}])^{\frac{1}{2}}}~\dot\sim~\text{N}(0,1)$$
- Ora, no caso assintótico temos:
$$\frac{T_{m,n}- \frac{m(m+n+1)}{2}}{\left[\frac{mn(m+n+1)}{12}\right]^\frac{1}{2}}~\dot\sim~\text{N}(0,1)$$

#### Empates
- De forma parecida ao que fizemos acima, no caso de empates:
$$\text{Var}(T_{m,n})= \frac{mn}{12}\left(m+n+1 - \frac{\sum_{i=1}^{g}(\tau_{i}-1)\tau_{i}(\tau_{i}+1)}{(m+n)(m+n-1)} \right)$$
