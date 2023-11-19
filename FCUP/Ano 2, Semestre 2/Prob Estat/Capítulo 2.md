11# 2 - Probabilidade
### Experiência aleatória
- Experiência que conduz resultados observáveis tais que:
    1. A experiência pode ser repetida um grande número de vezes em condições semelhantes
    2. conhecemos os resultados possíveis mas não podemos prever o resultado para uma amostra específica
    3. Quando é realizada um grande número de vezes em condições semelhantes, o conjunto dos resultados obtidos apresenta “Regularidade Estatística”

## 2.1 - Espaço amostral ou Espaço de resultados
- Conjunto de todos os resultados possíveis da experiência aleatória, representado por $\Omega$. Por exemplo, ao lançar um dado temos $\Omega=\{1,2,3,4,5,6\}$

## 2.2 - Acontecimento
- Um acontecimento associado a uma experiência aleatória é um subconjunto de $\Omega$, sendo que se o acontecimento for igual a
    - $\Omega$ então é um acontecimento certo
    - $\emptyset$  então é um acontecimento impossível

> EX:
>  ![[prob intro.png|350]]

## 2.3 - Teoria de Conjuntos
- Como acontecimentos não deixam de ser conjuntos, neles aplicamos operações de teoria de conjuntos:
![[teoria de conjuntos.png]]
- Sendo que temos as leis de Morgan:
$$\begin{align*}
\overline{A\cup B}=\overline A \cap \overline B\\
\overline{A\cap B}=\overline A \cup \overline B
\end{align*}$$
- Temos que 2 acontecimentos $A$ e $B$ são _mutuamente exlusivos_ ou _incompatíveis_ se não puderem ocorrer simultaneamente, ou seja, $A\cap B=\emptyset$

- Seja $E$ uma experiência aleatória para a qual temos $n$ provas independentes. Se para esta experiência tivermos uma acontecimento $A$ que ocorreu $m_{n}$ durante estas $n$ experiências temos que a _frequência relativa_ $f_{n}(A)$: $$f_{n}(A)=\frac{m_{n}}{n}$$

### Regularidade Estatística
- Quando as frequências relativas para $n$ provas independentes parecem aproximar-se de valores bem definidos consoante $n$ aumenta. Esse valor é a _probabilidade de $A$_. Ou seja, numa experiência em que há regularidade estatística temos:
$$f_{n}(A)\longrightarrow P(A)$$
(De notar que isto não é uma definição de probabilidade, mas sim uma forma de obter a probabilidade experimentalmente)

## 2.4 - Interpretações de Probabilidade
### 2.4.1 - Interpretação frequencista de probabilidade
- Probabilidade é um número entre 0 e 1. Quando temos uma experiência em que não conseguimos prever o resultado, a probabilidade de um certo acontecimento indica o frau de certeza com que ele pode (ou não) ocorrer.
- P=1 indica que o acontecimento ocorre de certeza, P=0 indica que o acontecimento é impossível.

### 2.4.2 - Definição de Laplace (Definição Clássica)
- Imaginemos que temos uma experiência em que há $m$ resultados possíveis, todos _igualmente possíveis_.
- Se um acontecimento $A$ corresponder a $k$ destes $m$ resultados possíveis, temos então $$P(A)=\frac{k}{m}=\frac{\textsf{casos favoráveis}}{\textsf{casos possíveis}}$$
- O maior problema desta definição é que ela parte do princípio que todos os resultados são igualmente possíveis. 
- Podemos ainda ver que ao dizer que todos os resultados são igualmente possíveis, estamos a dizer que os resultados são equiprováveis. Mas como este princípio é a base da definição, estamos a usar probabilidade para definiar probabilidade, ou seja, a definição é circular.

- Portanto, esta definição não deve ser aplicada quando os resultados não são igualmente possíveis nem quando temos resultados infinitos ou em número que não conseguimos determinar.

### 2.4.3 - Axiomática de Kolmogorov
- Antes de mais, uma nota sobre as propriedades das frequências de ocorrência:
> Temos uma experiência $E$ aleatória e um número $n$ de provas realizadas. 
> Para qualquer acontecimento $A$ associado à experiência $E$ temos: $$0\leq f_{n}(A)\leq1$$
> A frequência de ocorrência do acontecimento $\Omega$ é $\Large f_{n}(\Omega)=1$
> Se 2 acontecimentos $A$ e $B$ associados à experiência $E$ são _exclusivos entre si_ (A ocorre se B não, B ocorre se A não, nenhum ocorre) então temos$$f_{n}(\textsf{ocorre A ou ocorre B})= f_{n}(A)+f_{n}(B)$$

- A probabilidade é, nesta definição, uma função $P()$ que toma valores reais e definida no espaço dos acontecimentos de uma experiência aleatória $E$. É necessário que satisfaça estas condições:
1. $\large P(A)\geq0, \quad \forall A\in E$  
2. $\large P(\Omega)=1$
3. Se $A_{1},A_{2}, \dots$ são acontecimentos em número finito ou infinito, tais que $A_{i}\cap A_{j}=\emptyset$ para $i\neq j$. Assim: $\large P(A_{1}\cup A_{2}\cup\dots)=P(A_{1})+P(A_{2})+\dots$

- A partir destes 3 axiomas podemos obter mais propriedades da função probabilidade:
1. $\large P(\bar A)=1-P(A)$
2. $\large P(\emptyset)=0$
3. $\large 0\leq P(A)\leq 1$
4. $\large P(A\cup B)=P(A)+P(B)-P(A\cap B)$  <-- __*Regra da Adição*__
5. $\large P(A\cap \bar B)=P(A)-P(A\cap B)$

- De recordar novamente as __Leis de Morgan__:
$$\begin{align*}
\overline{A\cup B}=\overline A \cap \overline B\\
\overline{A\cap B}=\overline A \cup \overline B
\end{align*}$$

#### Definição Clássica de probabilidade como caso particular da Definição Axiomática
- Facilmente vemos que a definição clássica não passa de um caso da definição axiomática em que $\Omega$ é finito, tal que se tenha:
$$\Omega=\{e_{1}, e_{2},\dots,e_{N} \}\quad ;\quad P(e_{i})= \frac{1}{N}$$
- Pelo que temos então, na definição clássica: $\large P(A)= \frac{\#A}{N}$

## 2.5 - Probabilidade Condicinal
- Basicamente, ao calcular a probabilidade de um acontecimento, passamos a ter em conta que a sua ocorrência pode afetar a probabilidade de outros acontecimentos ocorrerem.

- Sejam $A$ e $B$ dois acontecimentos com $P(B)>0$. A probabilicade condicional de $A$ ocorrer dado que _B ocorreu_ é:
$$P(A|B)= \frac{P(A\cap B)}{P(B)}$$
- Na prática, isto pode aparecer como "Qual a probabilidade de a pessoa ter sangue AB, sendo que se trata de um homem?"


### 2.5.1 - Propriedades da Probabilidade Condicional
1. $\large P(\bar A|B)=1-P(A|B)$
2. $\large P(\emptyset |B)=0$
3. $0\leq P(A|B)\leq1$
4. $\large P(A\cup C|B)=P(A|B)+P(C|B)-P(A\cap C|B)$  <-- __*Regra da Adição
5. __*Lei da Multiplicação:*__$$\begin{align*}P(A\cap B)=P(B)P(A|B) \quad \quad\textsf{(desde que P(B)>0)}\\=P(A)P(B|A) \quad \quad\textsf{(desde que P(A)>0)}\end{align*}$$

### 2.5.2 - Acontecimentos independentes
- Dois acontecimentos são independentes se a ocorrência de um não afeta a probabilidade de ocorrência do outro.
- Para estes acontecimentos temos: $$P(A\cap B)=P(A)\times P(B)$$
### 2.5.3 - Teorema da Probabilidade Total
- Temos $\{A_{1},A_{2},\dots, A_{n}\}$ partições de $\Omega$ com $P(A_{i})>0 ~,~\forall i \in [1, n]$ 
- Para qualquer acontecimento $B$ temos:
$$P(B)=P(A_{1})P(B|A_{1})+P(A_{2})P(B|A_{2})+\dots+P(A_{n})P(B|A_{n})$$
> De notar que para partições finitas $A_{1},\dots,A_{n}$ de $\Omega$ temos, por definição, que: $$A_{i}\cap A_{j}=\emptyset~,~\forall i\neq j \quad \quad; \quad \quad\bigcup\limits_{i=1}^{n}A_{i}=\Omega$$


>__*EX*__
>Um teste médico é 99% eficaz a detetar uma doença quando está presente, mas também dá "falsos positivos" para 2% das pessoas saudáveis. Sendo que 0.5% da população tem a doença,
>__a)__ qual é a probabilidade de o teste dar positivo a uma pessoa escolhida ao acaso da população?
>__b)__ qual é a probabilidade de uma pessoa a quem o teste deu positivo ter mesmo a doença?
> 
> __*Resolução*__
> Temos 2 acontecimentos possíveis ao testar uma pessoa:
> - $T$ - O teste dar positivo
> - $D$ - A pessoa estar doente
> Sabemos então que $$P(T|D)=0.99 \quad ;\quad P(T|\bar D)=0.02 \quad;\quad P(D)=0.005$$
> __a)__ Queremos determinar $P(T)$. Pelo teorema da probabilidade total temos:$$\begin{align*}P(T)&= P(D\cap T)+P(\bar D\cap T)\\ &= P(D)P(T|D)+P(\bar D)P(T|\bar D)\\&= 0.005\times0.99+(1-0.005)\times0.02=0.02485=2.485\%\end{align*}$$
> De notar que aqui consideramos $D$ e $\bar D$ como todas as partições de $\Omega$
>
> __b)__ Agora queremos obter $P(D|T)$. 
> - Sabemos que: $\large P(D|T)=\frac{P(D\cap T)}{P(T)}$ 
> - Pela regra da multiplicação: $P(D\cap T)=P(D)\cdot P(T|D)=0.005\cdot0.99=0.00495$
> - Vimos na alínea a) que $P(T)=0.02485$
> Assim temos que $$P(D|T)=\frac{0.00795}{0.02485}\approx0.20$$

## 2.6 - Diagrama de Árvore
- Recurso útil para dividir um problema em partes e organizar a informação disponível
- Por exemplo, acerca da experiência de lançar uma moeda:
![[diagrama arvore.png]]
Daqui tem-se que a probabilidade de sair cara 1 vez em 2 lançamentos é: $$P=0.5\times0.5+0.5\times0.5=0.5$$
- De notar que a soma das probabilidades dos ramos que saem de uma mesma opção tem que dar $1$

### 2.7 - Tabela de Dupla Entrada
- Uma tabela de dupla entrada também é uma boa opção para organizar os dados.

#prob-estat #matematica