 # O que são?
- Uma NN é uma rede de neurónios. O termo pode descrever redes reais tipo no cérebro ou computacionais 
- Uma ANN (artificial NN) é uma rede de neurónios artificiais. Ou seja, uma ANN simula/aproxima o comportamento de uma parte do cérebro.
- De um ponto de vista mais prático, uma ANN é um sistema computacional paralelo que consiste em vários elementos simples que estão ligados de uma forma que permite fazer uma certa tarefa.

# Porquê estudar?
- São muito poderosas e eficientes (por usarem paralelismo)
- Elas adaptam-se aos dados então não precisamos de alta expertise em programação
- Toleram bem falhas e ruído

# Para que servem?
- Temos 2 objetivos possíveis
    - *Modelar um cérebro* - mais científico/académico. Pode ajudar a entender o funcionamento do cérebro e tudo o que isso implica
    - *Construção de sistemas* - mais de engenharia. Uma rede destas permite criar sistemas eficientes aplicáveis a problemas reais. Basicamente, "AI"
- Estes objetivos não competem, são complementares.

# Learning
- NN conseguem aprender e generalizar a partir dos dados. Para isto, adaptam os pesos que ligam os neurónios até que o output seja o melhor
- Por causa disto, elas podem ser aplicadas a diversos tipos de tarefas:
    - Regressão
    - Classificação
    - Reinforcement learning
    - clustering
    - otimização
enquanto que métodos "normais" (LDA, Ridge, SoftMax) são específicos para 1 tarefa.

## Forma geral de NN
- Podemos ver rdes neuronais como uma grande função composta:
$$\begin{align*}
\hat{y}&= h_{n}(\cdots(h_{2}(h_{1}(\mathbf{x},\boldsymbol{\theta}_{1}),\boldsymbol{\theta}_{2}))\cdots)\\
&= h_{n}^{\boldsymbol{\theta}_{n}}\circ h_{n-1}^{\boldsymbol{\theta}_{n-1}}\circ (\cdots)\circ h_{2}^{\boldsymbol{\theta}_{2}}\circ h_{1}^{\boldsymbol{\theta}_{1}}(\mathbf{x})
\end{align*}$$
em que cada camada funciona como uma *camada* da rede

## Multi-Layer (MLP)
- Outra forma de ver NN é assim:
$$\hat{y}=f \left(\sum\limits_{j=1}^{N}w_{j}h_{j}(\mathbf{x}) \right)$$
numa rede multi-layer temos:
![[nn.png]]
em que as camadas entre o input e o output chamam-se camadas escondidas.
- Temos então uma entrada $\mathbf{z}$. O que um perceptron a que esta está ligada calcula é:
$$\mathbf{u}=h_{j}(\mathbf{z},\boldsymbol{\theta}_{j})=\sigma(w_{j}\mathbf{z} + \mathbf{b}_{j})$$
em que $\boldsymbol{\theta}_{j}=\{w_{j},\mathbf{b}_{j}\}$
- Aqui temos:
    - $n_{i}$ - número de entradas, $n_{o}$ - número de neurónios de saída
    - $w_{j}$ é uma matriz $n_{o}\times n_{i}$
    - $\mathbf{z}$ é um vetor $n_{i}\times1$
    - $\mathbf{u}$ é um vetor $n_{o}\times1$
    - $\mathbf{b}_{j}$ é um vetor $n_{o}\times1$
(aqui "saída" não quer dizer que é o output da rede, mas sim os neurónios da camada escondida 1, a que as entradas são ligadas)
- Ou seja, consideremos que temos um sistema com 4 entradas e 2 neurónios de saída:
![[ml_1|700]]
$$\begin{pmatrix}u_{1} \\ u_{2}\end{pmatrix}=\sigma \left(\begin{pmatrix}w_{11} & w_{12} & w_{13} \\ w_{21} & w_{22} & w_{23}\end{pmatrix} \begin{pmatrix}z_{1} \\ z_{2} \\ z_{3} \\ z_{4}\end{pmatrix} + \begin{pmatrix}b_{1} \\ b_{2}\end{pmatrix} \right)$$
que nos dá este sistema:
$$\begin{cases}
u_{1}=\sigma( w_{11}z_{1}+w_{12}z_{2}+w_{13}z_{3}+w_{14}z_{4} + b_{1}) \\
u_{2}=\sigma( w_{21}z_{1}+w_{22}z_{2}+w_{23}z_{3}+w_{24}z_{4})
\end{cases}$$

## Sigma?
- Esta é a *função de ativação*! Esta é uma função não linear 

### Porque não linear?
- Se fosse linear teríamos um modelo linear:
![[ml_2|500]]
temos agora 2 camadas escondidas. Teríamos:
$$\begin{align*}
\mathbf{u}&= \sigma(w_{u}\mathbf{z} + \mathbf{b}_{u})\\
\mathbf{v}&= \sigma(w_{v}\mathbf{z} + \mathbf{b}_{v})
\end{align*}$$
e consideremos então uma função de ativação linear: $\sigma(\mathbf{x})=\mathbf{x}$. Temos:
$$\begin{cases}
\mathbf{u}= w_{u}\mathbf{z} + \mathbf{b}_{u}\\
\mathbf{v}= w_{v}\mathbf{z} + \mathbf{b}_{v}
\end{cases} \to \begin{cases}
--- \\
\mathbf{v}=w_{v}w_{u}\mathbf{z} + w_{v}\mathbf{b}_{u}+\mathbf{b}_{v}
\end{cases}$$
ou seja:
$$\mathbf{v}=W \mathbf{z} + B$$
e temos um modelo linear. Assim, ao introduzir camads NÃO aumentamos o espaço de funções que usamos.

### Escolhas normais
- A escolha mais "clássica" é o **sigmoide**:
$$\sigma(z)=\frac{1}{1-e^{-z}}$$
mas essa é a escolha mais antiquada.
- Atualmente, a escolha mais normal é a função **RELU**:
$$\sigma(z)=\begin{cases}
z &; &  z\ge0 \\
0 & ; & z<0
\end{cases}$$
- Outras escolhas possíveis:
    - Função **STEP**: $$\sigma(z)=\begin{cases}
0 & ; & z\le0 \\
1 & ; & z>0
\end{cases}$$
    - Tangente hiperbólica: $$\sigma(z)=\tanh(z)$$
- Temos abaixo o gráfico:
![[funcs ativacao.png]]
- De notar que, apesar do que fissemos acima, se quisermos fazer regressão podemos usar uma função de ativação linear.

## XOR
- Um exemplo de NN importantes é para representar uma porta XOR
- Esta porta consiste em: 1 se $x_{1},x_{2}$ forem diferentes, 0 se iguais. Isso dá-nos:
![[problema de xor.png]]
- Ora, esta gama de pontos não pode ser dividida por métodos como Softmax, porque este apenas divide o espaço de dados em 2, usando uma linha.
- O que precisamos é algo assim:
![[problema de xor solucao.png]]
- Uma maneira de conseguir isto é com uma NN com 2 camadas (quando dizemos X camadas incluímos X-1 camadas escondidas e 1 camada de output) assim:
![[problema de xor rede solucao.png]]
e funciona!

## Three-Layer
- Uma NN com 2 camadas consegue dividir/classificar vetores em classes que consistem em uniões de regiões poliédricas (?), mas não funciona para QUALQUER união
- Já uma arquitetura com 3 camadas consegue classificar qualquer união

## Learning parâmetros
-  O que precisamos de determinar para que a NN faça o que queremos é os *parâmetros*, nomeadamente os **pesos** das ligações
- Para isto, a pior função de ativação é a função *degrau*, porque não a podemos derivar em $x=0$, logo não poderemos usar métodos de descida do gradiente de forma adequada.
- Como fizemos para outros métodos, determinamos os parâmetros ao minimizar uma função de erro ou custo
- Ou seja, queremos determinar um ponto em que $\nabla E=0$
    - Isto é impossível de fazer analiticamente

## Regressão
- Neste tipo de problemas temos $$E(\mathbf{w})=\frac{1}{2}\sum\limits_{n=1}^{N} \|y(\mathbf{x}_{n},\mathbf{w})-y_{n}\|^{2}$$
e temos a função "real":
$$y=f(\mathbf{x}) + \varepsilon~~~~~~,~~~~ \varepsilon\sim N(0,\sigma_\varepsilon)$$
em que $\varepsilon$ é o ruído.

- Assim, os parâmetros ideais $W$ são obtidos ao maximizar a likelihood:
$$\begin{align*}
W&\leftarrow \text{argmax}_{W} \ln \prod P(Y^{l}|X^{l},W)\\
W&\leftarrow \text{argmin}_{W} \sum\limits_{l}(y^{l}-\hat{f}(x^{l}))^{2}
\end{align*}$$
em que $\hat{f}(x^{l})$ é a estimativa aprendida pela NN.

### Descida de Gradiente
- A maioria das técnicas de determinação de parâmetros consistem em escolher uma estimativa inicial $\mathbf{w}^{(0)}$ e melhorar a estimativa em cada iteração ao ir somando um vetor: $\mathbf{w}^{(\tau+1)}=\mathbf{w}^{(\tau)}+\Delta \mathbf{w}^{(\tau)}$
- Mais concretamente, a técnica de *descida de gradiente* consiste em:
$$\mathbf{w}^{(\tau+1)}=\mathbf{w}^{(\tau)}- \eta \nabla E(\mathbf{w}^{(\tau)})$$
ou seja
$$E(\mathbf{w}+\Delta \mathbf{w})\approx E(\mathbf{w}) + \Delta \mathbf{w}^{T}\nabla E(\mathbf{w})$$
- Ou seja:
![[ciclo otimizacao rede nn.png]]

#### Backpropagation de erro
- Método eficiente para avaliar as derivadas da função de erro AKA calcular o gradiente.
- Consiste em:
    1. Colocar um vetor de entrada $\mathbf{z}$ na NN. Calcular a saída final, usando os pesos da iteração atual
    2. Comparar a diferença entre a saída obtida e a esperada - isso é o erro $\delta$
    3. Fazer backpropagation do erro para as camadas escondidas. Ou seja, atribuir a cada camada uma parte do erro (para fazer algo do tipo: a camada 1 é responsável por 10% do erro). A fórmula geral disto será: $$\delta_{j}=h'(a_{j})\sum\limits_{k}w_{jk}\delta_{k}$$
        - $\delta_k$ é o erro da saída $k$
        - Para um neurónio oculto $j$ somamos o erro pesado associado das ligações deste a cada saída. Usamos esta fórmula para cada neurónio da linha antes da saída, linha $n-1$. 
        - Depois usamos a fórmula para a linha antes dessa ($n-2$), considerando que a linha $n-1$ é a "saída".
        - Assim sucessivamente, até termos o erro associado a cada neurónio da rede -  propagamos o erro para trás
    4. Determinar as derivadas.
        - Consideremos que temos a derivada $\frac{\partial E}{\partial w_{ij}}$, em que $w_{ij}$ é o peso da ligação que vai do neurónio $i$ da linha $k$ ao neurónio $j$ da linha $k+1$
        - Temos: $$\frac{\partial E}{\partial w_{ij}}=\delta_{j}\cdot z_{i}$$ em que temos o erro e saída dos neurónios $j,i$.

- Neste método é então útil saber as derivadas de funções de ativação:
$$h(a)=\tanh(a)~~\to~~ h'(a)=1-h(a)^{2}$$
$$h(a)=\sigma(a)~~\to~~ h'(a)=\sigma(a)(1-\sigma(a))$$
#### Algoritmo de Desc Grad + Backpropagação
1. Começar com todos os pesos iguais a valores aleatórios 
2. Repetir até convergir:
    1. Inserir o exemplo de treino na rede e calcular o output de cada neurónio. Depois o output da rede em si
    2. Para cada output calcular $\delta_{k}$ e com ele determinar $\frac{\partial E}{\partial a}=(z-y)z(1-z)$ (assumindo que $\sigma$ é um sigmoide)
    3. Para cada neurónio $j$, propagar o erro: $\delta_{j}=h'(a)\sum_{k}w_{jk}\delta_{k}$
    4. Determinar o gradiente: $\frac{\partial E}{\partial w_{ij}}=z_{i}\delta_{j}$
    5. Atualizar o vetor $\mathbf{w}$

### Treino MAP para NN
- Novamente, temos $$y=f(\mathbf{x})+\varepsilon$$
- Temos que os parâmetros ótimos são dados por:
$$W\leftarrow \text{argmax}_{W}\ln P(W)\prod_{l} P(Y^{l}|X^l,W)$$
e consideramos que $P(W)\sim N(0,\sigma I)$.
- Assim temos:
$$W\leftarrow \text{argmin}_{W} \left[ c\sum\limits_{i} w_{i}^{2} + \sum\limits_{l}(y^{l}-\hat{f}(x^{l}))^{2} \right]$$

## Classificação 
### Binária
- Usamos o sigmoide como função de ativação
- A função de ativação pode ser interpretada com a probabilidade $p_{x,w}$ de pertencer a $\mathcal{C}_{1}$
- A probabilidade de uma saída $y_{n}$ é $p_{x,w}^{y_{n}}(1-p_{x,w})^{1-y_{n}}$ (distribuição de *Bernoulli*)
- A probabilidade total dos dados de treino é $\prod_{n=1}^{N}p_{x_{n},w}^{y_{n}}(1-p_{x_{n},w})^{1-y_{n}}$
- Isto quer dizer que a função log-likelihood é:
$$\sum\limits_{n=1}^{N} y_{n}\log p_{x_{n},w} + (1-y_{n})\log(1-p_{x_{n},w})$$
e definimos a função de erro:
$$E(\mathbf{w})=-\sum\limits_{n=1}^{N} y_{n}\log p_{x_{n},w} + (1-y_{n})\log(1-p_{x_{n},w})$$
e a classificação consiste em minimizar esta função.

### Multi-class para dados nominais
- Temos uma NN com $K$ outputs. 
- Temos $K$ classes, pelo que o output $k$ corresponde à probabilidade de pertencer à classe $\mathcal{C}_{k}$
    - Assim: $\sum_{k=1}^{K}p_{k}=1$
- A probabilidade de ter uma saída $y_{n}$ é $\prod_{k=1}^{K}p_{k}^{y_{n}(k)}$ 
- A probabilidade total do dataset de treino: $\prod_{n=1}^{N}\prod_{k=1}^{K}p_{k}^{y_{n}(k)}$
- Pelo que a função log-likelihood é:
$$\sum\limits_{n=1}^{N}\sum\limits_{k=!}^{K}y_{n}(k) \log p_{k,x_{n},w}+(1-y_{n}(k))\log(1-p_{k,x_{n},w})$$
a função de erro será:
$$E(\mathbf{w})=-\sum\limits_{n=1}^{N}\sum\limits_{k=1}^{K} y_{n}(k)\log p_{k,x_{n},w} + (1-y_{n}(k))\log(1-p_{k,x_{n},w})$$
e a função de ativação será a função softmax:
$$p_{k}(\mathbf{x},\mathbf{w})=\frac{\exp(a_{k}(\mathbf{x},\mathbf{w}))}{\sum_{j}\exp(a_{j}(\mathbf{x},\mathbf{w}))}$$

## Problemas a treinar NN
### Valores iniciais
- Se usarmos um sigmoide como função de ativação e os pesos iniciais estiverem perto de zero, teremos então uma função de ativação aproximadamente linear - mau!
- Se começarmos com valores nulos a estimativa nunca evolui - mau!
- Pesos iniciais elevados fazem com que estejamos nas zonas mais horizontais do sigmoide, logo a estimativa converge pouco e temos maus resultados - mau!
    - Aliás, esta é a razão porque atualmente se usa RELU invés de sigmoide

- O que se faz então é: começamos com pesos aleatórios, mas próximos de zero. Assim, o modelo começa quase linear mas deixa de o ser consoante iteramos.
    - Por outras palavras, o modelo torna-se não linear onde necessário apenas!

### Scaling dos inputs
- É comum ajustar todos os inputs para termos média nula e desvio padrão igual a 1 (ou $\mu\in[0,1]~,~\sigma\in[-1,1]$)
- Isto garante que todos os inputs são tratados de forma igual ao fazer regularização
- Além disso, escolher pesos torna-se mais fácil. Por exemplo é costume escolher pesos como sendo valores aleatórios na gama $[-0.7,0.7]$

### Tamanho da rede
- Poderíamos escolher o tamanho da rede de modo a ser "grande que chegue" e depois calcular os pesos é uma approach fraca 
- O mais correto e escolher o número de *parâmetros* tais que:
    - seja grande o suficiente para poder distinguir classes enquanto que mantemos as semelhanças dentro de uma classe
    - não seja tão pequeno que começamos a distinguir diferenças dentro das classes : overffiting
- De forma geral, é *preferível ter mais camadas escondidas do que menos*.
    - Com camadas a menos, o modelo não terá flexibilidade para detetar aspetos não-lineares dos dados
    - Com demasiadas camadas, podemos simplesmente reduzir para quase zero os pesos "a mais" usando *regularização*.
- Assim, usamos *cross-validation* para determinar o parâmetro de regularização
- Na prática, o número de camadas escondidas que escolhemos baseia-se em tentativa e erro e conhecimento sobre os dados.

### Regularização 
- Uma forma de fazer isto é introduzir *weight decay*: $$\hat{E}(\mathbf{w})=E(\mathbf{w}) + \frac{\lambda}{2} \mathbf{w}^{T}\mathbf{w}$$
- Outra técnica é *early stopping*. Como o nome indica, consiste em parar o processo de treino da rede quando detetamos que o desempenho começou a piorar.
- Outro método é *estudar invariâncias* 
    1. Extrair caraterísticas invariantes às transformações desejadas. Por exemplo, queremos que o modelo aprenda atributos que não mudam se o input sofre rotação, translação, etc. (Ao detetar texto, uma rotação ou translação do texto não devem impedir o sistema de reconhecer)
    2. Aumentar os dados com réplicas - *data augmentation*. Por exemplo, para inputs de dados podemos fazer cópias de imagens, mas com rotações, reflexões, ruído, mudança de brilho, etc - Assim o modelo estará mais preparado para alterações e defeitos
    3. Introduzir um termo de regularização que penaliza mudanças do output quando o input é transformado. Isto vai de encontro ao ponto (1). 
    4. Fazer a arquitetura de modo a incluir as invariâncias por default. Uma forma de fazer isto é ter pesos partilhados. Este tipo de solução resulta em outros tipo de redes como redes convolucionais.

## Outros tipos de rede
### RBF
- Radial Basis Functions
- Tipo de rede NN feed-forward
- A estrutura é semelhante a MLP e com aplicações semalhantes. Mas os neurónios em si são diferentes, assim como o algoritmo de aprendizagem
- Temos:
$$g(x)=w_{0} + \sum\limits_{i=1}^{M} w_{i}\exp(-\gamma_{i}(\mathbf{x}-c_{i})^{T}(\mathbf{x}-c_{i}))$$
- Os outputs dos neurónios passam a ter um carater loca (?)
- Temos portanto 3 parâmetros: $w_{i},c_{i},\gamma_{i}$

### Redes Recorrentes
- Temos feedback - o output dos neurónios é utilizado para alterar o input.
- Isto torna estas redes boas para estudar dados temporais, já que a rede em si funciona de forma temporal.
- Apesar disso, MLP também pode ser aplicado no domínio temporal

## Treinar no tempo
### MLP
- Consideremos que com uma NN queremos prever o próximo estado de um sistema. Claro, o estado depende do passado do sistema
- Poderemos usar então uma camada escondida para armazenar o estado anterior
![[nn recorrente.png]]

mas vejamos agora a rede recorrente:
### Rede Recorrente
- Temos acima uma representação de uma rede recorrente. Mas vejamos como ela fica se a "espalhar-mos" no tempo:
![[nn recorrente 2.png]]
então como treinar?

- Ora, espalhar a rede no tempo para a treinar NÃO é boa ideia
- Temos então outras ideias:
    - Criar uma rede recurrente por treinar (pesos aleatórios)
    - Treinar um classificador cujo input é o estado interno da rede e cujo output é o que nós quisermos
    - Isto depois pode ser usado com métodos mais complexos, explicado em artigos/livros que tem no PPT
