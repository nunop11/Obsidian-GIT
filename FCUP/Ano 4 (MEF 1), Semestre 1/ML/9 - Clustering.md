# Aprendizagem Empírica
## Aprendizagem Supervisionada
- Consiste em prever os valores de 1+ outputs $Y$ para um certo valor de entrada $X$
- As previsões feitas baseiam-se num conjunto de treino $(\text{x}_{i},y_{i})$ que consiste em casos já conhecidos e/ou resolvidos
- Se $(X,Y)$ são VAs com uma densidade de probabilidade conjunta $P(X,Y)$, então a aprendizagem supervisionada consiste na estimação da densidade de probabilidade $P(Y|X)$
- Algumas approaches:
    1. Modelos generativos - Começamos por determinar a probabilidade conjunta $p(x,y)$ e com ela determinamos os posteriors $p(y|x)$
    2. Determinar a probabilidade condicional $p(y|x)$ e depois fazer a média
    3. Modelos discriminativos - determinar a densidade diretamente com os dados de treino
- O que temos visto até agora

## Aprendizagem não supervisionada
- Consiste em determinar as propriedades da distribuição $p(x)$ sem um supervisor que diz se uma previsão está correta ou errada ou quão longe.
- Mais concretamente, queremos encontrar regiões do espaço em que temos maior densidade de pontos
- Algumas técnicas:
    - **Redução de dimensão** (análise componentes principais, escalamento multidimensional, mapas auto-organizáveis) - estas técnicas tentam *resumir a informação* de dados de muitas dimensões em menores dimensões. Isso facilita a visualização e análise dos dados (é mais fácil encontrar um mínimo 2D do que 3D)
    - **Análise de clusters** - consiste em dividir os dados em clusters (os pontos dentro de um cluster são semelhantes e distintos dos outros clusters). Em princípio, os clusters indicam pontos com maior densidade de pontos AKA onde temos picos da distribuição de probabilidade. Alguns métodos: K-Means, clustering hierárquico
    - **Regras de Associação** - Tentamos encontrar relações entre as variáveis com regras simples (conjuntivas). Do tipo: "se alguém comprou gin e gelo, é provável que compre água tónica". Isto permite determinar as regiões com maior densidade.

### Regras de Associação
- Maioritariamente usado com grandes sets de dados
- Em aprendizagem não supervisionada queremos encontrar os valores de $X$ que aparecem com maior frequência.
**Algoritmo Apriori**
- O algoritmo encontra relações de semelhança entre items.
- Isto é feito com uma abordagem *bottom-up*, ou seja, começa por fazer subconjuntos pequenos e gradualmente vai combinando-os em conjuntos maiores.
    1. Primeiro, definimos um valor mínimo C. Um certo item só é considerado para as regras se aparecer em >=C observações. Fazemos a lista de items a considerar.
    2. Segundo, o algoritmo gera todas as combinações de 2 items. Para cada combinação, é verificado em quantas observações os items aparecem juntos.
    3. Depois, apenas passam para a iteração seguinte os grupos que aparecem todos juntos em >=C observações.
    4. Em cada iteração, o algoritmo acrescenta 1 item a cada combinação que sobreviveu. 
    5. Isto continua até que nenhuma combinação é contada em nenhuma observação

### Análise de Cluster
- Fazemos grupos/clusters de dados de forma que todos os pontos dentro de um cluster são mais semelhantes entre si do que com qualquer ponto fora (semelhança alta intra-class, semelhança baixa inter-class)
    - Por exemplo, alguns objetos podem ser definidos pelas suas dimensões ou pela forma como se comportam com outros objetos
- Mas o que é semelhança? Para muitos algoritmos, consideramos semelhança como sendo **proximidade / distância**
- Ou seja, agrupamos clusters de pontos mais próximos. Claramente, estes grupos marcam zonas de alta densidade de probabilidade.

#### Dissimilarity index
- NOTA: para me poupar o trabalho a escrever: DS=dissimilaridade, SS=similaridade 
- O que usamos para definir se algo é próximo/similar ou não. Consiste numa função do tipo $$\gamma: E \times E\to R$$
1. Uma função $d:E\times E\to R_{0}^{+}$ é um *índice de DS* se 
    - a) $d(x,x)=0$ para qualquer $x$ (um ponto não dista de si próprio)
    - b) $d(x_{2},x_{1})=d(x_{2},x_{1})$ (a distância não depende do sentido)
2. Um índice de DS $d$ também é um *índice de distância* se, além de a) e b), tiver a propriedade c):
    - c) $d(x_{1},x_{2})=0\to x_{1}=x_{2}$ (intuitivo)
3. Um índice de distância $d$ também é uma *função de distância* se, além de a),b) e c), tiver a propriedade d):
    - d) $d(x_{1},x_{2})\le d(x_{1},x_{3})+d(x_{3},x_{2})$ (intuitivo)
4. Uma função de distância $d$ também é *ultramética* se, além de a)-d), tiver a propriedade e):
    - e) $d(x_{1},x_{2})\le\max\{d(x_{1},x_{3}),d(x_{3},x_{2})\}$ (versão mais forte da d), faz sentido se desenharmos - se $x_3$ está perto de $x_{1}$ estará longe de $x_{2}$ e vice-versa)

**Propriedades de distâncias**
- Meio que estamos a repetir aquilo acima, mas pronto:
$$\begin{align*}
\text{Simetria} &: &&&D(A,B)&=D(B,A)\\
\text{Auto-semelhança} &: &&&D(A,A)&=0\\
\text{Separação} &: &&&D(A,B)&=0~\to~ A=B\\
\text{Desigualdade triangular} &: &&&D(A,B)&\le D(A,C) + D(B,C)
\end{align*}$$
a lógica da desigualdade triangular é que NÃO podemos dizer: "A é parecido a B, B é parecido a C. A e C são muito diferentes" - não faz sentido

**Exemplos para variáveis quantitativas**
![[Pasted image 20241231164658.png]]

**Exemplos para variáveis binárias**
------------ slide 13 ----------


#### Similarity Index
- O maus comum é o coeficiente de correlação de Pearson:
$$r_{xz}=\frac{\sum\limits_{i=1}^{D}(x_{i}-\overline{x})(z_{i}-\overline{z})}{\sqrt{\sum\limits_{i=1}^{D}(x_{i}-\overline{x})^{2}\sum\limits_{i=1}^{D}(z_{i}-\overline{z})^{2}}}$$
