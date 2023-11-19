# Probabilidade - Continuação
- Tal como sabemos, podemos caraterizar a probabilidade de um evento como uma função da seguinte forma:$$P:\Omega \to [0,1]$$
## Teoremas de Komolgorov
**1 -** Não negatividade - Uma probabilidade nunca pode ser negativa
**2 -** A probabilidade do espaço de acontecimentos é $1$: $P(\Omega)=1$
**3 -** Teorema da **Aditividade**:
    - Sendo $A,B \subset \Omega$, com $A \cap B = \emptyset$ (se tivermos 2 conjuntos disjuntos) temos:$$P(A\cup B)=P(A)+P(B)$$

## Propriedades das Probabilidades
### 1 - Probabilidade do conjunto vazio
$$P(\emptyset)=0$$
> DEMO:
> É óbvio que $\Omega=\Omega \cup \emptyset$ e $\Omega\cap\emptyset=\emptyset$. Assim, pelo teorema da aditividade: 
> $$\begin{align*}
P(\Omega\cup\emptyset)&= P(\Omega)+P(\emptyset)\\
P(\Omega)&= P(\Omega)+P(\emptyset)\\
1&= 1+P(\emptyset) \quad \longrightarrow \quad P(\emptyset)=0
\end{align*}$$

### 2 - Probabilidade do Complementar
$$P(\bar A)=1-P(A)$$
> DEMO
> Temos que: $\Omega=A\cup\bar A$ e que $A\cap\bar A=\emptyset$
> Logo temos que: $$\begin{align*}
P(\Omega)&= P(A)+P(\bar A)\\
1 &=  P(A)+P(\bar A) \quad \longrightarrow \quad P(\bar A)=1-P(A)
\end{align*}$$

### 3 - Monotocidade
Consiste em: $$A\subseteq B \quad \longrightarrow \quad P(A)\le P(B)$$
> DEMO
> Temos que $B=A\cup \{B\backslash A\}$  e que $A\cap \{ B\backslash A \}=\emptyset$
> Assim, pelo teorema da aditividade: $$P(B)=P(A)+P(B\backslash A)$$
> Como probabilidades nunca são positivas, $P(B)\ge P(A)$. As probabilidades serão iguais quando $P(B\backslash A)=0$. Isto acontece quando $A=B$ ou quando os termos $\{B \backslash A\}$ têm probabilidade nula.

### 4 - Lei de Adição de Probabilidades
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

### 5 - Independência de eventos
Dois eventos $A,B\subset \Omega$ são independentes se $$P(A\cap B)=P(A)P(B) \tag{Eventos Independentes}$$
#### 5.1 - Auto Indepêndencia
- Temos  $A\subset \Omega$. Vamos *presumir* que $A$ é independente de si próprio. Nesse caso teríamos: $$P(A)=P(A\cap A)=P(A)P(A)$$
ora, isto só será verdade se $P(A)=0 \quad \vee \quad P(A)=1$
- Ou seja, os únicos conjuntos autoindependentes são $\Omega$ e $\emptyset$

#### 5.2 - Depêndencia de eventos disjuntos
- Temos 2 eventos $A,B\subset \Omega$ com $A\ne\emptyset,B\ne\emptyset$. Consideremos que são eventos disjuntos, ou seja, $A\cap B=\emptyset$.
- Ou seja: $P(A\cap B)=0$
- Se eles fossem independentes teríamos: $P(A)P(B)=0$. A única forma de isto ocorrer é se pelo menos 1 deles tiver probabilidade nula.
- *Intuição:* Se fizermos uma experiência e o evento $A$ ocorrer, sabemos que não ocorreu o $B$. Ou seja, um deles dá informação sobre o outro $\to$ não são independentes.

## Probabilidade Condicionada
- Podemos definir como $$P(A|B)=\begin{cases}
\frac{P(A\cap B)}{P(B)} &; &P(B)\ne 0 \\
0 &; &P(B)=0
\end{cases}$$
**Propriedades**
$$P(A|B)\ge0$$
$$P(\Omega|B)=1$$
$$P(A_{1}\cup A_{2}|B)=P(A_{1}|B) + P(A_{2}|B) \quad;\quad A_{1}\cap A_{2}=\emptyset$$
$$A,B~~\textsf{independentes} \quad \quad \longrightarrow \quad \quad P(A|B)=P(A)$$

# Teorema da Probabilidade Total
Sendo $A$ uma partição de $\Omega$, temos que $A_{i}$ cumpre os seguintes requisitos: $$\begin{cases}
A_{i}\cap A_{j}=\emptyset ~~,~~ i\neq j~~,~~ i,j\in\{1,2,\dots,N\} ~~~~(N\textsf{ partições}) \\
\bigcup\limits_{i=1}^{N} A_{i}=\Omega
\end{cases}$$
O teorema diz-nos que: $$P(B)=\sum\limits_{i=1}^{N} P(B|A_{i})P(A_{i})$$
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

# Teorema de Bayes
- Muito conhecido e muito usado em análise de dados, mas não iremos usar muito em FESTA.
- Facilmente fazemos a sequência de passos abaixo: 
$$\begin{align*}
P(A_{i}\cap B)&= P(B\cap A_{i})\\
P(A_{i}|B)P(B)&= P(B|A_{i})P(A_{i})\\
P(A_{i}|B)&= \frac{P(B|A_{i})P(A_{i})}{P(B)}
\end{align*}$$
se aplicarmos o teorema da probabilidade total no denominador temos:
$$P(A_{i}|B)=\frac{P(B|A_{i})P(A_{i})}{\sum_{i=1}^{N} P(B|A_{i})P(A_{i})}$$

# Valor Médio e Média
$$\bar x=\frac{1}{N} \sum\limits_{i=1}^{N} x_{i} \quad \quad \quad;\quad \quad \quad \langle x\rangle = \sum\limits_{i\in A}x_{i} P_{i}$$
- Ao contrário do que podemos pensar, as 2 grandezas acima **não são o mesmo**.
    - $\bar x$ é o **estimador da média**. Consiste em obter o valor médio de $N$ experiências aleatórias (em que se presume que todos os $x_{i}$ têm a mesma probabilidade).
    - $\langle x\rangle$ é o **valor médio**. É aplicado dentro de um espaço de eventos.

- No entanto, há 1 caso em que eles são *aproximadamente a mesma coisa*: $N\to+\infty$
$$\lim\limits_{N\to+\infty} \bar x_{n}= \langle x\rangle$$

> DEMO
> Começamos por definir uma função caraterística: $$\chi_{A}(x)=\begin{cases}
1 &; &x=A\\ 0&; &x\ne A
\end{cases}$$
> Temos que $\sum\limits_{b\in A}\chi_{A}(b)=0+0+0+\dots+1+0+0+\dots = 1$ 
> Ou seja, na fórmula do estimador da média podemos simplesmente multiplicar o sumatório acima e não perdemos a igualdade: $$\bar x_{N}=\frac{1}{N} \sum\limits_{i=1}^{N}x_{i}\sum\limits_{b\in A}\chi_{b}(x_{i})$$
> $$\bar x_{N}=\frac{1}{N}\sum\limits_{b\in A} \sum\limits_{i=1}^{N}x_{i}\chi_{b}(x_{i})$$
> Ora, neste sumatório, só quando $x_{i}=b$ é que $\chi_{b}(x_{i})\ne0$. Assim: 
> $$\begin{align*}
\bar x_{N}&= \frac{1}{N}\sum\limits_{b\in A}\sum\limits_{i=1}^{N}b\chi_{b}(x_{i})\\
&= \frac{1}{N}\sum\limits_{b\in A}b\sum\limits_{i=1}^{N} \chi_{b}(x_{i})
\end{align*}$$
> Na prática, o 2º sumatório está a fazer a contagem do número de vezes que $b$ ocorre nas $N$ atividades aleatórias. Logo: 
> $$\frac{\sum\limits_{i=1}^{N} \chi_{b}(x_{i})}{N}=\frac{N_{b}}{N}=P_{b}$$
> Assim: $$\bar x_{N}=\sum\limits_{b\in A}b P_{b}=\langle x\rangle$$

