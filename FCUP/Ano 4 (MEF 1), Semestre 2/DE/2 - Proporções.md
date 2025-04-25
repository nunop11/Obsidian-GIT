## Wald
- Este IC já vimos atrás
- Ele é definido por:
$$\begin{align*}
P \left(-z_{0} < \frac{\hat{p}-p}{\sqrt{\hat{p}\hat{q}/n}} < z_{0}\right) &= 1-\alpha\\
P \left(-z_{0} \sqrt{\frac{\hat{p}\hat{q}}{n}}< \hat{p}-p < z_{0}\sqrt{\frac{\hat{p}\hat{q}}{n}}\right) &= 1-\alpha\\
P \left(\hat{p}-z_{0} \sqrt{\frac{\hat{p}\hat{q}}{n}}< p < \hat{p}+z_{0}\sqrt{\frac{\hat{p}\hat{q}}{n} }\right) &= 1-\alpha\\
\end{align*}$$
e temos: $$\text{IC Wald : }\hat{p}\pm z_{1-\alpha/2} \sqrt{\frac{\hat{p}\hat{q}}{n}}$$
- Ora, podemos notar que, obviamente, nesta equação temos $p$ e $q=1-p$ que são precisamente a variável que queremos determinar e não conhecemos. Ora, para poder usar este intervalo na prática temos que usar $P,Q$ - as aproximações amostrais.
- Temos então o **intervalo de Wald** que é bastante mau


### Problemas
- Consideramos que, num certo estudo, a proporção amostral é ZERO ($p=0$) ("ninguém de uma certa amostra votou no candidato X")
    - Facilmente vemos que o IC de Wald fica: $0\pm0=[0,0]$. Isto implica que absolutamente ninguém pertence a esta proporção, o que é errado (estamos a dizer que sabemos algo com 100% de confiança)
    - A mesma coisa acontece se a proporção amostral for $p=1$ (temos $q=0$) logo ficamos com o IC: $[1,1]$
- Ou seja, sempre que $p$ estiver perto de 0 ou de 1, o IC de wal torna-se mal comportado e representa pior a realidade

## Agresti-Coull (AC)
- Este método é bruto, direto e simples. Mas funciona bem.
- Simplesmente adicionamos 4 amostras "falsas": 2 zeros e 2 uns. 
- Assim, temos a proporção amostral "*corridiga*":
$$\tilde{p}= \frac{n \hat{p}+2}{n+4}=\frac{\sum_{i=1}^{n}X_{i} + 0+0+1+1}{n+4}$$
e o IC de AC com 95% de confiança pode ser definido exatamente como o de Wald:
$$\text{IC AC 95}: \tilde{p}\pm 1.96 \sqrt{\frac{\tilde{p}(1-\tilde{p})}{n+4}}$$
(notemos que, apesar de simples, este intervalo está limitado a 95%)

### Bias
- Como seria de esperar, criar amostras falsas introduz um bias no nosso estimador
- Podemos definir:
$$\text{Bias}[\tilde{p}]=\mathbb{E}[\tilde{p}-p]=\mathbb{E} \left[\frac{n \hat{p}+2}{n+4}\right]-p=(1-2p)\frac{2}{n+4}$$
- Ou seja:
    - Para $p=1/2$ temos bias nulo
    - Consoante nos afastamos de $p=1/2$, as 4 amostras falsas fazem $\tilde{p}$ estar mais perto de $p$ do que $\hat{p}$. Assim, se $p>1/2$ temos bias "para baixo" e vice-versa
    - Quanto menor a amostra, maior o bias

### Comparação Wald-AC
- Vamos comparar os intervalos de Wald e AC através da sua probabilidade de coverage: ver quantas vezes cada IC de facto contém o parametro $p$ da população.
- Assim, se temos IC 95%, seria de esperar que contenham o valor real 95% das vezes
- Para fazer isto, fazemos uma experiência de Monte Carlo: usamos sets aleatórios e testamos os ICs. No site que estamos a seguir, foi usada a função `dbinom` do R, que foi ainda mais simples que isto.
- O resultado abaixo foi obtido para $n=25$:
![[wald vs ac, n const.png]]
e para $n=50,n=100$:
![[wald vs ac, n const 2.png]]
- De uma forma geral, vemos que o AC se comporta de forma muito mais estável. Especialmente para $p\sim0,p\sim1$ vemos que o IC de Wald é muito errático
- Notamos ainda que Wald consistentementa tem coverage **abaixo** de 95%. Por outro lado, AC consistentemente está acima de 95%

- Inversamente, podemos observar a coverage de Wald e IC, com $p$ fixo, consoante aumentamos o tamanho da amostra:
![[wal vs ac, p const.png]]
- Podemos ver que, apesar de Wald tender a melhorar (como seria de esperar), AC consistentemente é melhor.

## Wilson
- Este intervalo consiste na forma "geral" do AC, que só dá para 95%

### Score Test
- Isto é o que estudamos para verificar testes de hipóteses. 
- Para uma população normal em que estamos a analisar a hipótese nula $H_{0}:\mu=\mu_{0}$, podemos definir a estatísitca $T=\frac{\overline{X}-\mu_{0}}{\sigma/\sqrt{n}}\sim N(0,1)$
- Ora, nesse caso *rejeitamos* $H_{0}$ se $|T|>1.96$.
- Assim, **não rejeitamos** se:
$$|T|\le1.96~~\to~~ -1.96\le \frac{\overline{X}-\mu_{0}}{\sigma/\sqrt{n}}\le1.96$$
logo:
$$\overline{X}-1.96 \frac{\sigma}{\sqrt{n}}\le \mu_{0}\le \overline{X}+1.96 \frac{\sigma}{\sqrt{n}}$$
- Ou seja, temos que os valores de $\mu_{0}$ (o nosso valor previsto/referência para a média) que NÃO conseguimos rejeitar são um **intervalo**.
- Por outras palavras, vemos que isto define um IC 95% de valores possíveis de $\mu$. Alternativamente, contém os valores que só podemos rejeitar com 5% de confiança.
- Em palavras mais diretas:
    - Temos uma variávael $\theta$ em estudo
    - Temos um intervalo com $(1-\alpha)\%$ de confiança. Podemos usá-lo para avaliar uma hipótese $H_{0}:\theta=\theta_{0}$
        - Se $\theta_{0}$ está dentro do intervalo, não conseguimos rejeitar
        - Se $\theta_{0}$ não está dentro do intervalo, rejeitamos

**Proporções agora : Não bate certo**
- Ora, este método de comparar a estatísitca $T$ ao valor $z_{1-\alpha/2}$ é como fazemos os **score tests**. Para proporções, vimos que o IC estudado é o de Wald.
- Para uma proporção $p$ com valor amostral $\hat{p}$, o score test toma a forma:
$$\text{Rejeitamos }H_{0}:p=p_{0}\text{ se: }\quad\frac{\hat{p}-p_{0}}{\sqrt{\frac{p_{0}(1-p_{0})}{n}}}>1.96$$
ou seja, tal como vimos acima, podemos escrever na forma de um *intervalo de não rejeição* (a 95%):
$$p_{0}\in \hat{p}\pm 1.96 \sqrt{\frac{p_{0}(1-p_{0})}{n}}$$

- Por outro lado, estudamos que o intervalo de confiança para a variável $p$ é definido por Wald como:
$$p\in \hat{p}\pm 1.96 \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$
- Ora, vemos que estes intervalos NÃO SÃO EQUIVALENTES!
- No site que o prof meteu no moodle, é dado um exemplo: 
    - Temos uma amostra $n=25$ com 5 uns e 20 zeros. Logo temos $\hat{p}=0.2$
    - O IC Wald 95% é facilmente calculado e temos: $[0.043, 0.357]$
    - Por exemplo, consideremos um valor de teste $p_{0}=0.07$. Claramente, ele está dentro do IC.
    - MAS, ao calcular a estatísitca temos $T=2.547>1.96$, logo deveríamos ser capazes de rejeitar a hipótese $H_{0}:p=p_{0}$
    - Ou seja, estes 2 métodos, que deveriam estudar a mesma coisa com 95% de confiança, dão conclusões diferentes acerca deste $p_{0}$

**E se fizermos um "teste de Wald"?**
- Isto seria um teste de comparação como o Score Test, mas adaptado da fórmula de Wald:
$$\text{Rejeitamos }H_{0}:p=p_{0}\text{ se :} \frac{\hat{p}-p_{0}}{\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}} > 1.96$$
- Podemos comparar este teste ao Score teste. Vemos que o teste de Wald herda todos os defeitos de IC Wald: para $p$ perto de 0 ou 1, temos uma muito alta chance de cometer erros tipo 1:
![[score vs wald test, n const.png]]
- Vemos então que este teste, apesar de concordante com o IC, é muito pior do que o score teste.
- Então, porque não fazer o oposto: inverter o score teste!

### Inverter o Score Test
- Juntamos todos os valores $p_{0}$ que o score teste **não rejeita** a 95%.
- Assumindo que o score test para este cenário funciona bem e que temos um erro tipo 1 nomial de 5%, teremos então um IC com 95% de confiança. Este é o **IC Wilson**
- Temos:
$$\begin{align*}
\frac{\hat{p}-p_{0}}{\sqrt{\frac{p_{0}(1-p_{0})}{n}}} &\le z\\
(\hat{ p}-p_{0})^{2}&\le z^{2} \frac{p_{0}(1-p_{0})}{n}\\
n \hat{p}^{2}-n p_{0}^{2} -2n\hat{p}p_{0}&\le z^{2}p_{0} - z^{2}p_{0}^{2}\\
(n+z^{2})p_{0}^{2}-(2n\hat{p}+z^{2})p_{0}+n\hat{p}^{2}&\le 0
\end{align*}$$
ora, isto consiste a ver os pontos limitam a parte negativa de uma parábola. Por outra palavras, as raízes do polinómio são os limites do IC:
$$\begin{align*}
p_{0}=\frac{2n\hat{p}+z^{2} \pm \sqrt{4z^{2}n\hat{p}(1-\hat{p}) + z^{4}}}{2(n+z^{2})}
\end{align*}$$
que podemos desenvolver e obtemos:
$$p_{0}=\frac{1}{1+ \frac{z^{2}}{n}} \left[\left(\hat{p} + \frac{z^{2}}{2n}\right) \pm z \sqrt{\frac{\hat{p}(1-\hat{p})}{n}+ \frac{z^{2}}{4n^{2}}} \right]$$
e aqui temos! Até já apareceu o termo do desvio padrão de Wald.
- Notemos que, em R, fazer `prop.test()` faz o IC de Wilson.

### Entender
- Comecemos por dizer que: o intervalo de Wilson consiste em definir um compromisso entre a proporção amostral $\hat{p}$ e $\frac{1}{2}$
- Vemos que o ponto médio do IC Wilson é:
$$\begin{align*}
\tilde{p}=\frac{n}{n+z^{2}} \left(\hat{p}+ \frac{z^{2}}{2n}\right)&=  \frac{n\hat{p}+ \frac{1}{2}z^{2}}{n+z^{2}}\\
&= \frac{n}{n+z^{2}}\hat{p} + \frac{z^{2}}{n+z^{2}} \frac{1}{2}\\
&= \omega \hat{p} + (1-\omega) \frac{1}{2}
\end{align*}$$
em que definimos um peso $\omega= \frac{n}{n+z^{2}}$, que está sempre entre 0 e 1
- E daqui já percebemos a frase: o IC Wilson estará sempre centrado num valor $\tilde{p}$ entre $\hat{p}$ e $\frac{1}{2}$
- Pelo peso, vemos que:
    - Para um certo $z$ (confiança) fixo: quanto menor for a amostra ($n$ menor) mais somos "puxados" para $\tilde{p}=\frac{1}{2}$
    - Para um certo tamanho de amostra $n$ fixo: quanto maior a nossa confiança ($z$ menor) mais somos "puxados" para $\tilde{p}=\frac{1}{2}$

- Podemos definir então os desvios padrões dos 3 tipos de teste:
$$\begin{align*}
\text{Score:} &&\sigma&= \sqrt{\frac{p_{0}(1-p_{0})}{n}}\\
\text{Wald:} &&\hat{\sigma}&= \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}\\
\text{Wilson:} &&\tilde{\sigma}&= \omega\sqrt{\hat{\sigma}^{2}+ \frac{c^{2}}{4n^{2}}}
\end{align*}$$
e podemos definir o IC de Wilson como:
$$\text{IC Wilson : }\tilde{p} \pm z \tilde{\sigma}$$
que é algo muito mais "normal".

**Um meio, outra vez**
- Podemos desenvolver:
$$\begin{align*}
\tilde{\sigma}^{2}&= \omega^{2}\left(\hat{\sigma}^{2}+ \frac{z^{2}}{4n^{2}}\right)\\
&= \left(\frac{n}{n+z^{2}}\right)^{2} \left[\frac{\hat{p}(1-\hat{p})}{n} + \frac{z^{2}}{4n^{2}}\right]\\
&= \frac{1}{n+z^{2}} \left[\frac{n}{n+z^{2}} \hat{p}(1-p) + \frac{z^{2}}{n+z^{2}} \frac{1}{4} \right]\\
&= \frac{1}{n+z^{2}} \left[\omega \hat{p}(1-\hat{p}) + (1-\omega) \frac{1}{2} \frac{1}{2} \right]
\end{align*}$$
novamente, temos uma relação entre $\hat{p}$ e $\frac{1}{2}$, relacionando-se através de $\omega$.

**Wilson a 95%**
- No caso de 95% de confiança temos $z^{2}\simeq4$. Assim, podemos dizer que: $\omega\simeq \frac{n}{n+4}~,~1-\omega=\frac{4}{n+4}$. Assim temos:
$$\tilde{p}\simeq \frac{n}{n+4} \hat{p}+ \frac{4}{n+4} \frac{1}{2}= \frac{n \hat{p}+2}{n+4}$$
e vemos que isto é _exatamente_ a aproximação que fazemos no IC de AC!!!

### Wald VS Wilson
- Em sets de dados muito grandes, teremos $n\to\infty$ logo $\omega\to1$. Assim, nesses casos temos que Wald e Wilson comportam-se de forma quase igual
- De forma geral, Wilson consegue descrever de forma mais razoável a nossa incerteza acerca de $p$ para qualquer $n$
- Além disso e mais interessante para o caso de proporções, os ICs de Wilson estão sempre limitados por $[0,1]$

**Wald pode colapsar para 0, Wilson não**
- Vimos atrás como Wald pode colapsar para o "intervalo" $[0,0]$
- No caso de Wilson, vimos que a largura do intervalo é dada por:
$$2z \frac{n}{n+z^{2}} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}+ \frac{c^{2}}{4n^{2}}}$$
e vemos que, claramente, os termos $\frac{n}{n+z^{2}}, \frac{c^{2}}{4n^{2}}$ são estritamente positivos não nulos! Assim, nunca teremos um intervalo de largura nula.

**Wald pode ter valores de proporções impossíveis**
- A proporção populacional, por definição, só pode estar no intervalo $[0,1]$. Assim, os valores dentro dos ICs não deveriam estar fora destes valores, senão não fazem sentido.
- Wald é capaz de fazer precisamente isso: podemos ter valores $>1$ ou valores negativos. Nesse caso, o que temos de fazer é ignorar os valores fora de $[0,1]$. Isso é infeliz porque estamos a remover algum do significado estatístico do IC.
- Não tenho a dedução, mas dá para mostrar que Wald coloca valores negativos no IC quando $\hat{p}<1-\omega$. Analogamente, teremos valores acima de 1 quando $\hat{p}>\omega$.
    - De outra forma, o intervalo de Wald só está correto dum ponto de vista físico se $1-\omega<\hat{p}<\omega$
- Podemos escrever:
$$\begin{align*}
n(1-\omega)&< \sum\limits_{i=1}^{n}X_{i}< n\omega\\
\left\lceil n \frac{z^{2}}{n+z^{2}}\right\rceil &\le \sum\limits_{i=1}^{n} X_{i}\le \left\lfloor n \frac{n}{n+z^{2}}\right\rfloor
\end{align*}$$
(em que o termo central é o número de sucessos - $X_{i}=1$ se tivermos sucesso)
- Podemos então determinar o número máximo e mínimo de sucessos que permitem ter um IC nos limites corretos para cada $n$. Assim temos:
```R
##        n min_success max_success 
## [1,]  10           3           7 
## [2,]  11           3           8 
## [3,]  12           3           9 
## [4,]  13           3           10 
## [5,]  14           4           10 
## [6,]  15           4           11 
## [7,]  16           4           12 
## [8,]  17           4           13 
## [9,]  18           4           14 
## [10,] 19           4           15 
## [11,] 20           4           16
```
- Também dá para provar que IC Wilson $\in [0,1]$

