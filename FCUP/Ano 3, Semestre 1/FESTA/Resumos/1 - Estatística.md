# 1 - Revisão de Probabilidades e Estatísticas
## 1.1 - Conceitos fundamentais
### Espaço de Acontecimentos
-  Para uma dada experiência, o conjunto cujos elementos são todos os eventos possíveis.

### Evento / Acontecimento
- Elemento do Espaço do Acontecimentos, mas pode também ser uma sequência de eventos
- EXEMPLO: Consideremos o espaço de acontecimentos $\Omega=\{1,2,3,4\}$
    - $A=\{1\}$ é um evento
    - $B=\{3,4\}$ também é um evento

### Diagrama de Venn
- Muito útil para visualizar conceitos de probabilidades.

![[diagrama venn.png|500]]

- Por exemplo, no diagrama acima temos os eventos $A,B,C$ contidos no espaço $\Omega$.

#### Acontecimentos mutuamente exclusivos
- Aproveitando o diagrama acima:
    - $A,B$ são mutuamente exclusivos pois $A \cap B=\emptyset$ 
    - $B,C$ e $A,C$ *não* são mutuamente exclusivos pois $B\cap C \neq \emptyset$, $A\cap C \neq \emptyset$

#### Acontecimento complementar
- Escrito como $\bar A$, consiste no conjunto de todos os elementos de $\Omega$ que *não* estão em $A$. Em diagrama de Venn temos:
![[complementar.png|500]]
### Partição de $\Omega$
![[partição.png|450]]
- Ora, $\{A_{i}\}$ é uma partição de $\Omega$
- Uma partição de $\Omega$ é um conjunto de vários elementos de $\Omega$, **desde que**:
    - $A_{i}\cap A_{j}= \emptyset~~,~~ \forall i,j ~~(i\neq j)$  (ou seja, 2 partições não se podem "sobrepor")
    - $\bigcup\limits_{i} A_{i}=\Omega$ (as partições têm de cobrir todo o espaço) 

### Probabilidade
- Medida do quão provável é um certo evento acontecer :/ (definição do prof)
- Normalmente está entre $0$ e $1$.
- Tal como sabemos, podemos caraterizar a probabilidade de um evento como uma função da seguinte forma:$$P:\Omega \to [0,1]$$
## 1.2 - Teoremas de Komolgorov
**1 -** Não negatividade - Uma probabilidade nunca pode ser negativa
**2 -** A probabilidade do espaço de acontecimentos é $1$: $P(\Omega)=1$
**3 -** Teorema da **Aditividade**:
    - Sendo $A,B \subset \Omega$, com $A \cap B = \emptyset$ (se tivermos 2 conjuntos disjuntos) temos:$$P(A\cup B)=P(A)+P(B)$$

## 1.3 - Propriedades das Probabilidades
**1 - Probabilidade do conjunto vazio**
$$P(\emptyset)=0$$
> DEMO:
> É óbvio que $\Omega=\Omega \cup \emptyset$ e $\Omega\cap\emptyset=\emptyset$. Assim, pelo teorema da aditividade: 
> $$\begin{align*}
P(\Omega\cup\emptyset)&= P(\Omega)+P(\emptyset)\\
P(\Omega)&= P(\Omega)+P(\emptyset)\\
1&= 1+P(\emptyset) \quad \longrightarrow \quad P(\emptyset)=0
\end{align*}$$

**2 - Probabilidade do Complementar**
$$P(\bar A)=1-P(A)$$
> DEMO
> Temos que: $\Omega=A\cup\bar A$ e que $A\cap\bar A=\emptyset$
> Logo temos que: $$\begin{align*}
P(\Omega)&= P(A)+P(\bar A)\\
1 &=  P(A)+P(\bar A) \quad \longrightarrow \quad P(\bar A)=1-P(A)
\end{align*}$$

**3 - Monotocidade**
Consiste em: $$A\subseteq B \quad \longrightarrow \quad P(A)\le P(B)$$
> DEMO
> Temos que $B=A\cup \{B\backslash A\}$  e que $A\cap \{ B\backslash A \}=\emptyset$
> Assim, pelo teorema da aditividade: $$P(B)=P(A)+P(B\backslash A)$$
> Como probabilidades nunca são positivas, $P(B)\ge P(A)$. As probabilidades serão iguais quando $P(B\backslash A)=0$. Isto acontece quando $A=B$ ou quando os termos $\{B \backslash A\}$ têm probabilidade nula.

**4 - Lei de Adição de Probabilidades**
Basicamente uma fórmula mais geral do teorema da aditividade:
$$P(A\cup B)=P(A)+P(B)-P(A\cap B)$$
> DEMO
> Se desenhares um diagrama de Venn com $A,B\subset \Omega$ e $A\cup B\ne\emptyset$ facilmente vês que:$$\begin{align*}
A&= (A\cap\bar B)\cup(A\cap B)\tag{Eq. 1.1}\\
B&= (B\cap\bar A)\cup(B\cap A)\tag{Eq. 1.2}\\
A\cup B&= (A\cap \bar B)\cup (B\cap\bar A)\cup (A\cap B)\tag{Eq. 1.3}\\
\end{align*}$$
> Ora, todos estes 3 conjuntos são disjuntos. Assim, pelo teorema da aditividade: $$P(A\cup B)=P(A\cap\bar B)+P(B\cup\bar A)+P(B\cap A)$$
> Da Eq.1.1 obtemos: $$P(A)=P(A\cap\bar B)+P(A\cap B) \quad \longrightarrow \quad P(A\cap\bar B)=P(A)-P(A\cap B)$$
> Da Eq.1.2 obtemos: $$P(B)=P(B\cap\bar A)+P(B\cap A) \quad \longrightarrow \quad P(B\cap\bar A)=P(B)-P(A\cap B)$$
> Substituindo as igualdades obtidas acima na Eq.1.3 obtemos: $$P(A\cup B)=P(A)-P(A\cap B)+P(B)-P(A\cap B)+P(A\cap B)$$
> $$P(A\cup B)=P(A)+P(B)-P(A\cap B)$$

**5 - Independência de eventos**
Dois eventos $A,B\subset \Omega$ são independentes se $$P(A\cap B)=P(A)P(B) \tag{Eventos Independentes}$$
*5.1 - Auto Indepêndencia*
- Temos  $A\subset \Omega$. Vamos *presumir* que $A$ é independente de si próprio. Nesse caso teríamos: $$P(A)=P(A\cap A)=P(A)P(A)$$
ora, isto só será verdade se $P(A)=0 \quad \vee \quad P(A)=1$
- Ou seja, os únicos conjuntos autoindependentes são $\Omega$ e $\emptyset$

*5.2 - Depêndencia de eventos disjuntos*
- Temos 2 eventos $A,B\subset \Omega$ com $A\ne\emptyset,B\ne\emptyset$. Consideremos que são eventos disjuntos, ou seja, $A\cap B=\emptyset$.
- Ou seja: $P(A\cap B)=0$
- Se eles fossem independentes teríamos: $P(A)P(B)=0$. A única forma de isto ocorrer é se pelo menos 1 deles tiver probabilidade nula.
- *Intuição:* Se fizermos uma experiência e o evento $A$ ocorrer, sabemos que não ocorreu o $B$. Ou seja, um deles dá informação sobre o outro $\to$ não são independentes.

## 1.4 - Probabilidade Condicionada
- Podemos definir como $$P(A|B)=\begin{cases}
\frac{P(A\cap B)}{P(B)} &; &P(B)\ne 0 \\
0 &; &P(B)=0
\end{cases}$$
**Propriedades**
$$P(A|B)\ge0$$
$$P(\Omega|B)=1$$
$$P(A_{1}\cup A_{2}|B)=P(A_{1}|B) + P(A_{2}|B) \quad;\quad A_{1}\cap A_{2}=\emptyset$$
$$A,B~~\textsf{independentes} \quad \quad \longrightarrow \quad \quad P(A|B)=P(A)$$

# 2 - Teorema da Probabilidade Total
Sendo $A$ uma partição de $\Omega$, temos que $A_{i}$ cumpre os seguintes requisitos: $$\begin{cases}
A_{i}\cap A_{j}=\emptyset ~~,~~ i\neq j~~,~~ i,j\in\{1,2,\dots,N\} ~~~~(N\textsf{ partições}) \\
\bigcup\limits_{i=1}^{N} A_{i}=\Omega
\end{cases}$$
O teorema diz-nos que: $$P(B)=\sum\limits_{i=1}^{N} P(B|A_{i})P(A_{i})$$
(podes pensar nisto de forma kinda geométrica. É como se tivessemos a projetar $B$ em cada partição, no termo $P(B|A_{i})$, e depois estamos a multiplicar essa projeção pela probabilidade da partição em sim. Kinda como: $\vec{r'}=\sum_{i} (\vec{r}\cdot\hat{e_{i}})\hat{e_{i}}$)

> DEMO
> Temos que: $$\begin{align*}
B&= B\cap \Omega\\
&= B\cap \left( \bigcup\limits_{i=1}^{N} A_{i} \right) \\
&= \bigcup\limits_{i=1}^{N}(A_{i}\cap B) 
\end{align*}$$
> Conseguimos então dividir $B$ conforme a partição $A$.
> Se escolhermos quaisquer $i\ne j$ teremos: $(B\cap A_{i})\cap (B\cap A_{j})=\emptyset$. Assim, pelo teorema da aditividade: $$\begin{align*}
P(B)&= \sum\limits_{i=1}^{N} P(A_{i}\cap B)\\
&= \sum\limits_{i=1}^{N} P(B|A_{i})P(A_{i})
\end{align*}$$

# 3 - Teorema de Bayes
- Muito conhecido e muito usado em análise de dados, mas não iremos usar muito em FESTA.
- Facilmente fazemos a sequência de passos abaixo: 
$$\begin{align*}
P(A_{i}\cap B)&= P(B\cap A_{i})\\
P(A_{i}|B)P(B)&= P(B|A_{i})P(A_{i})\\
P(A_{i}|B)&= \frac{P(B|A_{i})P(A_{i})}{P(B)}
\end{align*}$$
se aplicarmos o teorema da probabilidade total no denominador temos:
$$P(A_{i}|B)=\frac{P(B|A_{i})P(A_{i})}{\sum_{i=1}^{N} P(B|A_{i})P(A_{i})}$$

# 4 - Valor Médio e Média
$$\bar x=\frac{1}{N} \sum\limits_{i=1}^{N} x_{i} \quad \quad \quad;\quad \quad \quad \langle x\rangle = \sum\limits_{i\in A}x_{i} P_{i}$$
- Ao contrário do que podemos pensar, as 2 grandezas acima **não são o mesmo**.
    - $\bar x$ é o **estimador da média**. Consiste em obter o valor médio de $N$ experiências aleatórias (em que se presume que todos os $x_{i}$ têm a mesma probabilidade). Mais abaixo iremos aprofundar mais este tópico.
    - $\langle x\rangle$ é o **valor médio**. É aplicado dentro de um espaço de eventos.

# 5 - Função Indicadora
- Podemos definir uma função indicadora $\chi_{A}$ que nos irá ajudar a determinar a probabilidade de um acontecimento $A$.
- E temos:
$$\begin{align*}
discreta :~~~~ P_{A}&= \langle\chi_{A}\rangle=\sum\limits_{a\in\Omega}\chi_{A}(a)P(a)\\
contínua :~~~~ P_{A}&= \langle\chi_{A}\rangle=\int_{\Omega}da~\chi_{A}(a)\rho(a)
\end{align*}$$
em que temos $\chi_{A}(a)=0$ se na partição $a$ não temos o acontecimento $A$

# 6 - Variável Aleatória
## 6.1 - Discreta
- Temos uma variável aleatória discreta $X$. A ela temos associada uma função de probabilidade $f(x)=P(X=x)$
- Sendo $D=\{x_{1},x_{2},\dots\}$ o conjunto de valores que $X$ pode assumir temos: $$0\le f(X_{i})\le 1~~,~~\sum_{x_i\in D}f(x_{i})=1$$
- A média é descrita por: $E(X)=\sum_{i}f(x_{i})x_{i}=\mu$
    - Temos: $E(aX+bY)=aE(X)+bE(Y)$

- A variância é: $V(X)=\sum_{i}f(x_{i})(x_{i}-\mu)^{2}=\sigma^{2}$
    - Podemos escrever: $\sigma^{2}=E[(X-\mu)^{2}]=E(X^{2})-E(X)^{2}$
    - Temos: $V(aX+b)=a^{2}V(X)$

- O desvio padrão é simplesmente $\sigma=\sqrt{V(X)}$

**Variáveis independentes**
- 2 variáveis aleatórias são independentes se: $$P(X\le a\wedge Y\le b)=P(X\le  a)P(Y\le b)$$
- Sendo que para variáveis $X,Y$ independentes temos:
    - $E(XY)=E(X)E(Y)$
    - $V(aX+bY)=a^{2}V(X)+b^{2}V(Y)$

**Função caraterística**
- Podemos definir a função caraterística de uma VA discreta como:
$$\phi_{X}(t)=\langle e^{iXt}\rangle=\sum\limits_{k}e^{iXt}P(X=k)$$

## 6.2 - Contínua
- Uma VA em que os valores possíveis são infinitos não numeráveis.
- Se a VA for contínua, a probabilidade de ela ter 1 valor é nula

### 6.2.1 - Revisão de Probabilidade e Estatística
- Sendo $X$ uma VA contínua, ela tem uma densidade de probabilidade $\rho$, tal que 
    - $0\le\rho(x)\le1$
    - Podemos escrever: $$\rho(x)=\lim\limits_{\Delta x\to0^{+}}\frac{P(x\le X\le x+\delta x)}{\Delta x}$$

- Para uma VA contínua temos:
$$\langle f\rangle=\int dx~f(x)\rho(x) \quad\quad;\quad\quad P_{A}=\int dx~\rho(x)\chi_{A}(x)$$

**Propriedades**
- Uma vez que $P(X=a)=0$, não importa se usamos intervalos fechados ou aberto: $P(a<X<b)=P(a\le X\le b)$.
- Naturalmente temos: $P(-\infty<X<+\infty)=\int_{-\infty}^{+\infty}\rho(x)dx=1$ (**Condição de Normalização**)

**Média e cenas**
- A média é dada por: $E(X)=\int_{-\infty}^{+\infty}\rho(x)x~dx=\mu$
    - Temos: $E(aX+bY)=aE(X)+bE(Y)$

- A variância é dada por: $V(X)=\int_{-\infty}^{+\infty}\rho(x)(x-\mu)^{2}~dx=\sigma^{2}$
    - Podemos escrever: $\sigma^{2}=E[(X-\mu)^{2}]=E(X^{2})-E(X)^{2}$
    - Temos: $V(aX+b)=a^{2}V(X)$

- Novamente, o desvio padrão é só: $\sigma=\sqrt{V(X)}$

**Variáveis independentes**
- Exatamente o mesmo que tem nas VA discretas

**Função caraterística**
- Podemos definir a função caraterística de uma VA contínua como:
$$\phi_{X}(t)=\langle e^{ixt}\rangle=\int_{-\infty}^{+\infty}e^{itX}\rho_{X}(x)dx$$

### 6.2.2 - Troca de Variável
- Consideremos que temos uma VA contínua com densidade $\rho(x)$. 
- Queremos então determinar a densidade de probabilidade da variável $y=f(x)$. Partimos da equação $P_{A}=\int dx~\rho(x)\chi_{A}(x)$. O truque está na função indicadora e no seu parâmetro. Fazemos
$$P(y<Y<y+\Delta y)=\int dx ~\chi_{y-\frac{\Delta y}{2},y+\frac{\Delta y}{2}}(f(x))~\rho(x)$$
em que definimos:
$$\chi_{y-\frac{\Delta y}{2},y+\frac{\Delta y}{2}}(f(x))=\begin{cases}
1 & ; & y-\frac{\Delta y}{2}<f(x)<y+\frac{\Delta y}{2} \\
0 & ; & caso~~contrário
\end{cases}$$
(podíamos ter definido $\chi_{A}(f(x))$ que daría $1$ apenas se $f(x)\in A=[y-\frac{\Delta y}{2},y+\frac{\Delta y}{2}]$)

- Assim, o integral irá integrar todos os pontos de $x$ em que temos $y-\frac{\Delta y}{2}<f(x)<y+\frac{\Delta y}{2}$. Os restantes serão anulados. Ficamos portanto com a probabilidade desejada.
- Pela equação que temos no início da secção 6.2.1:
$$\rho(y)=\lim\limits_{\Delta y\to0^{+}}\frac{P(y<Y<y+\Delta y)}{\Delta y}=\lim\limits_{\Delta y\to0^{+}}\int dx~\frac{\chi_{y-\frac{\Delta y}{2},y+\frac{\Delta y}{2}}(f(x))}{\Delta y}\rho(y)$$

ora, a fração dentro do integral não passa de um delta de dirac (no limite $\Delta y\to0^{+}$ a fração torna-se infinita e o intervalo da função indicadora infinitamente fino). Fica então:
$$\rho=\int dx ~ \rho(x)\delta(y-f(x))$$

### 6.2.3 - Troca de Variável com $n$ variáveis $X$
- Consideremos agora que temos $Y=g(X_{1},X_{2},\dots,X_{n})$ em que todos os $X_{i}$ são VA independentes com densidades $\rho(x_{i})$. De forma análoga ao que temos acima:
$$\rho(y)=\int_{-\infty}^{+\infty}\cdots\int_{-\infty}^{+\infty}\delta(y-g(x_{1},\dots,x_{n}))~\rho_{1}(x_{1})\cdots\rho_{n}(x_{n})~~dx_{n}\cdots dx_{1}$$
em que não poderíamos separar $\rho(x_{1},\dots,x_{n})=\rho(x_{1})\cdots\rho(x_{n})$ se as VA não fossem independentes.

#### 6.2.3.1 - Soma de Variáveis
- Este é apenas um caso particular do ponto anterior, em que: $Y=X_{1}+X_{2}=g(X_{1},X_{2})$. Temos:
$$\begin{align*}
\rho(y)&= \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}\delta(y-x_{1}-x_{2})\rho_{1}(x_{1})\rho_{2}(x_{2})dx_{2}dx_{1}\\
&= \int_{-\infty}^{+\infty}\rho_{1}(x_{1}) \left(\int_{-\infty}^{+\infty}\delta(y-x_{1}-x_{2})\rho_{2}(x_{2}) dx_{2}\right)dx_{1}
\end{align*}$$
o integral de dentro só não se anula quando $y-x_{1}-x_{2}=0\to y=x_{1}+x_{2}$. Ou seja, sendo $x_{2}=y-x_{1}$ o único valor de $x_{2}$ que "sai" do integral. A equação fica:
$$\rho(y)=\int_{-\infty}^{+\infty}\rho_{1}(x_{1})\rho_{2}(y-x_{1})dx_{1}=(\rho_{1}*\rho_{2})(y)$$
sim, isto é uma **convolução**.

# 7 - Momentos
- Temos a variável aleatória $X$. 
    - Se for discreta temos a função de probabilidade $f$
    - Se for contínua temos a densidade de probabilidade $\rho$

- Podemos então definir os momentos de $X$:
$$\begin{align*}
discreta:~~~~ \langle x^{n}\rangle&= \sum\limits_{i}x_{i}^{n}f(x)\\
contínua:~~~~ \langle x^{n}\rangle&= \int_{-\infty}^{+\infty}x^{n}\rho(x)~dx 
\end{align*}$$

# 8 - Cumulantes
- Temos a variável aleatória $X$. 
    - Se for discreta temos a função de probabilidade $f$
    - Se for contínua temos a densidade de probabilidade $\rho$

- Os cumulantes são os coeficientes $c_n$ na expressão a seguir:
$$\ln (\langle e^{ikx}\rangle) = \sum_{n=1}^{+\infty}c_n \frac{(ik)^n}{n!}$$


- Começamos com $\ln(\langle e^{ikx}\rangle)$
- Podemos expandir a exponencial em série de Taylor: $$\ln(\langle e^{ikx}\rangle)=\ln \left(\sum\limits_{n=0}^{+\infty} \frac{(ik)^{n}}{n!}\langle x^{n}\rangle\right)=\ln \left(1+\sum\limits_{n=1}^{+\infty}\frac{(ik)^{n}}{n!}\langle x^{n}\rangle\right)$$
- Temos $\log(1+x) = \sum_{n=1}^{+\infty}\frac{(-1)^{n+1}x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \cdots$. Logo:$$\ln(\langle e^{ikx}\rangle)=\sum\limits_{m=1}^{+\infty}\frac{(-1)^{m+1}}{m}\left(\sum\limits_{n=1}^{+\infty}\frac{(ik)^{n}}{n!}\langle x^{n}\rangle\right)^{m}$$
- Podemos demonstrar que temos os cumulantes:
$$\begin{align*} c_1 &= \langle x\rangle \\ c_2 &= \langle x^2\rangle - \langle x\rangle ^2 \\ c_3 &= \langle x^3\rangle - 3\langle x\rangle \langle x^2\rangle + 2\langle x\rangle^3 \\ c_4 &= \langle x^4\rangle - 4\langle x^3\rangle\langle x\rangle - 3\langle x^2\rangle^2 + 12 \langle x^2\rangle \langle x^2\rangle -6 \langle x^4\rangle \\\vdots\end{align*}$$

# 9 - Estimadores
- Tal como referido, vejamos melhor o estimador da média (entre outros).
## 9.1 - Estimador do valor médio / média
$$\bar x=\frac{1}{N}\sum\limits_{i=0}^{N-1}x_{i}$$
- Há 1 caso em que o estimador e o valor médio são aproximadamente a mesma coisa: 
$$\lim\limits_{N\to+\infty} \bar x_{n}= \langle x\rangle$$

> DEMO
> Começamos por definir uma função caraterística: $$\chi_{A}(x)=\begin{cases}
1 &; &x=A\\ 0&; &x\ne A
\end{cases}$$
> Temos que $\sum\limits_{b\in A}\chi_{A}(b)=0+0+0+\dots+1+0+0+\dots = 1$ 
> Ou seja, na fórmula do estimador da média podemos simplesmente multiplicar o sumatório acima e não perdemos a igualdade: $$\begin{align*}
\bar x_{N}=\frac{1}{N} \sum\limits_{i=1}^{N}x_{i}\sum\limits_{b\in A}\chi_{b}(x_{i})
\end{align*}$$
> Ora, neste sumatório, só quando $x_{i}=b$ é que $\chi_{b}(x_{i})\ne0$. Assim: 
> $$\begin{align*}
\bar x_{N}&= \frac{1}{N}\sum\limits_{b\in A}\sum\limits_{i=1}^{N}b\chi_{b}(x_{i})\\
&= \frac{1}{N}\sum\limits_{b\in A}b\sum\limits_{i=1}^{N} \chi_{b}(x_{i})
\end{align*}$$
> Na prática, o 2º sumatório está a fazer a contagem do número de vezes que $b$ ocorre nas $N$ atividades aleatórias. Logo: 
> $$\frac{\sum\limits_{i=1}^{N} \chi_{b}(x_{i})}{N}=\frac{N_{b}}{N}=P_{b}$$
> Assim: $$\bar x_{N}=\sum\limits_{b\in A}b P_{b}=\langle x\rangle$$

**Erro do Estimador da Média**
- O estimador da média não é exato e tem um erro associado ao seu desvio padrão.
- Vejamos então qual é a variância do estimador $\overline X$:
$$\begin{align*}
\langle \overline X^{2}\rangle-\langle\overline X\rangle^{2}&= \frac{1}{N^{2}}\sum\limits_{i,j}\langle x_{i}x_{j}\rangle-\langle x\rangle^{2}\\
&= \frac{1}{N^{2}}\sum\limits_{i}\langle x_{i}^{2}\rangle + \frac{1}{N^{2}}\sum\limits_{i\neq j} \langle x_{i}x_{j}\rangle - \langle x\rangle^{2}
\end{align*}$$
- Podemos mostrar o termo do sumatório:
> O estimador da média é $\bar x=\frac{1}{N}\sum_{i=1}^{N}x_{i}$
> Podemos definir o seu quadrado: $\bar x^{2}= \frac{1}{N^{2}}\left(\sum_{i=1}^{N}x_{i}\right)^{2}=\frac{1}{N^{2}} \sum_{i=1}^{N}x_{i}\sum_{j=1}^{N}x_{j}=\frac{1}{N^{2}}\sum_{i,j}^{N}x_{i}x_{j}$
> Assim surge: $$\langle \bar x^{2}\rangle=\frac{1}{N^{2}} \sum\limits_{i,j=1}^{N} \langle x_{i}x_{j}\rangle$$


- Vamos assumir que todos os eventos da amostra são independentes, tendo $p=\frac{1}{N}$ e $\langle x\rangle=\sum_{i=0}^{N-1}x_{i}p_{i}$. Temos:
$$\begin{align*}
\sum\limits_{i}\langle x_{i}^{2}\rangle&= \langle x^{2}\rangle N\\
\sum\limits_{i\neq j}\langle x_{i}x_{j}\rangle&= \langle x\rangle^{2}N(N-1)
\end{align*}$$
e a equação atrás pode ser reescrita copo:
$$\langle \overline X^{2}\rangle-\langle\overline X\rangle^{2}=\frac{\langle x^{2}\rangle}{N}+\frac{N-1}{N}\langle x^{2}\rangle-\langle x\rangle^{2}=\frac{\langle x^{2}\rangle-\langle x\rangle^{2}}{N}~~\to~~\text{Var}(\overline X)=\frac{\text{Var}(x)}{N}$$
logo temos o desvio padrão do estimador:
$$\sigma_{\overline X}=\frac{\sigma_{x}}{\sqrt{N}}$$

## 9.2 - Estimador da Variância
- Vejamos então como podemos estimar a variância da grandeza $x$:
$$\begin{align*}
\text{Var}(x)&= \frac{1}{N}\sum\limits_{i=1}^{N}(x_{i}-\overline X)^{2}\\
&= \frac{1}{N}\sum\limits_{i=1}^{N}(x_{i}^{2}-2x_{i}\overline X+\overline X^{2})\\
&= \frac{1}{N}\left(\sum\limits_{i=1}^{N}x_{i}^{2}-2\overline X\sum\limits_{i=1}^{N}x_{i} + \overline X^{2}\sum\limits_{i=1}^{N}1 \right)\\
&= \frac{1}{N}\sum\limits_{i=1}^{N}x_{i}^{2}- \frac{1}{N}\cdot 2N\overline X^{2} + \frac{1}{N}\cdot N\overline X^{2}\\
&= \frac{1}{N}\sum\limits_{i=1}^{N}x_{i}^{2}-\overline X^{2}
\end{align*}$$
- Podemos determinar a média da variância da grandeza $x$ (mas eu não consegui deduzir):
$$\begin{align*}
\langle\text{Var}(x)\rangle&= \frac{N-1}{N}(\langle x^{2}\rangle-\langle x\rangle^{2})
\end{align*}$$
e temos então um bom estimador da variância:
$$\text{Var}(x)= \frac{1}{N-1}\sum\limits_{i=1}^{N}(x_{i}-\overline X)^{2}$$
