- Este PPT tem uma porção enorme a recordar e repetir coisas anteriores da UC

## Evitar overfitting
### Regularização
- Ao criar um modelo de ML, definimos: família do modelo, função de custo e método de otimização
- Regularização é algo que acrescentamos ao algoritmo de aprendizagem e que tem o objetivo de baixar o seu erro de *generalização* (menos overfitting) sem afetar muito o erro de treino.
- Na prática, ao introduzir um sistema de regularização estamos a aumentar o bias em troca de baixar a variância do modelo.
    - Assim, um bom regularizador minimiza a variância sem aumentar demasiado o bias
- Normalmente, isto consiste em introduzir um $\lambda$ na função de perda, de uma forma que estejamos a penalizar complexidade.

## ML clássico
![[tipo aprendizagem.png]]
- Que é o que temos visto.

## Deep Learning
- Terceira "geração" de AI, desde 2008.
- Consiste em aprender atributos automaticamente, diretamente dos dados
- Atinge a melhor performance

### E o modelo linear?
- Por ser algo simples, robusto e que funciona bem; normalmente é boa ideia começar por tentar usar um método linear para estudar os dados
    - Este tipo de modelo tolera erros e podemos sempre linearizar os dados ao aplicar-lhes funções

### Então, quando usar Deep?
- Existem casos em que, por mais que apliquemos funções de linearização, nunca iremos conseguir.
![[classificacao complexa.png]]
- Um dos principais casos que devemos usar deep learning é: *Classificação Binária Complexa*, como acima.
- Usando NN, podemos obter representações mais compactas dos dados input-output. 
    - Uma NN é compacta se tiver poucos parâmetros livres 
    - Uma NN compacta deverá ter melhor performance de generalização
- Ou seja, em problemas muito complexos (ver foto, detetar audio, detetar texto), é quase impossível expressar a relação entre os pixeis de forma analítica.
- Ou seja, temos modelos que encontram/formam os atributos em si: *Representation Learning*
![[tipo aprendizagem 2.png]]

# NN Convolutional
## Deep Multilayer Perceptron (DNN)
- Consiste numa NN profunda (varias layers) e wide (muitos perceptrons por linha)
![[nn densa.png]]

## Imagens
- Se tivermos uma imagem que queremos analisar com uma MLP, primeiro teremos que converter a imagem 2D num vetor muito longo 1D, pelo que perdemos informação sobre a disposição da imagem.
- Ao usá-la para aprender um modelo, ele irá otimizar esta sequencia de valores, mas basta fazer shift ou zoom na imagem e o modelo não funciona!
- Ou seja, o modelo determina pesos corretamente, mas eles variam com translação e scaling, pelo que são pesos que não úteis para estudar imagens
- Outra coisa que temos de ter em conta é que, por exemplo, para uma imagem 200x200, com uma MLP normal teremos BILIÕES de parâmetros se a rede for suficientemente deep.

### O que queremos
- Ora, naturalmente, queremos um modelo que detete algo numa imagem. Mesmo que o objeto seja: rodado, movido, deformado ou resized.
![[invariancia rotacao.png]]

## Rede Convolucional
- Este tipo de rede consiste em poder estudar imagens de grande resolução ou até vídeos
- Passamos a ter *ligações esparsas* na NN (nem todos os perceptrons ligam a todos):
![[rede não densa.png]]
- Ocorre partilha de parâmetros determinados entre redes:
![[nn densa vs nao densa.png]]
(isto reduz automaticamente o erro quando há translação)
- Pode ser usado para qualquer input numa grid (até 3D+)
- Permite reduzir imenso o número de parâmetros
![[rede convolucional.png]]
- Falamos em **filters**
    - Se temos filtros 10x10, então cada filtro irá analisar uma região 10x10 píxeis
    - Além de dividir a imagem em partes, cada filtro pode alterar os dados. Por exemplo aplicando uma função para reduzir contraste
    - Podemos aplicar vários filtros às mesmas regiões, sucessivamente
    - O tamanho dos filtros é decidido conforme os padrões que queremos que a rede aprenda.

### Convolução
- Ou seja, cada perceptron liga apenas aos seus vizinhos
- Mas falamos em convolução: isso implica que todas as ligações têm os mesmos pesos (que são partilhados):
![[tipos ligacao.png]]
- Existe então uma *camada de convolução* (kernel) que contém estes pesos
- Por exemplo, num caso 2D em que cada perceptron analiza um conjunto 2x2:
![[funcionamento cnn.png]]

### Arquitetura
- Temos:
![[tipos rede.png|425]]

### Como funciona
![[funcionamento cnn 2.png]]
- Pooling consiste em juntar grupos de dados em 1 só. Por exemplo, *max pooling* consiste em escolher o máximo dentro de cada bloco. Na imagem acima escolhemos o máximo em cada bloco 2x2. Abaixo escolhemos o máximo a cada 3 pontos:
![[ligacao nao densa 2.png|500]]
- Definimos a quantidade e tamanho das camadas de pooling conforme o quão importante é que a rede seja robusta em distorções. Em geral, o melhor é fazer pooling lentamente.

### Outros
- Existem muitas coisas diferentes que podem ser feitas, com diferentes arquiteturas:
#### R-CNN
- Esta é a técnica usada para detetar objetos em imagens. Primeiro definimos caixas que limitam os objetos. Depois temos um passo de classificação.
![[cnn particoes.png]]
#### U-Net
![[rede em u.png]]
- Esta arquitetura tem a principal função de segmentar imagens. 
    - Azul - serve para extrair informação das imagens.
    - Vermelho - diminuem a resolução espacial da imagem. Faz com que a rede consiga aprender informação em diferentes escalas.
    - Verde - faz up-sampling / aumenta a resolução da imagem. Serve para trazer a segmentação de volta à escala da entrada
    - Azul-verde - reduzir número de canais. Converte os dados na versão final
    - Cinzento - misturam canais de up e down sampling. Permite guardar detalhes das imagens.

#### Convolução transposta
![[up sampling.png]]
- Acima temos um exemplo simples. Movemos um kernel 3x3 ao longo de um input 4x4 com stride unitário.
- Isto é equivalente a INVERTER uma convolução de uma input 2x2  padded com zeros com um kernel 3x3, com stride unitário. 
- Isto permite aumentar a resolução (up-scaling!!!)

##### Stride
- Consiste no passo com que a o kernel/filtro se desloca pelo input. 
    - Se stride=1 vamos andando para os pontos ao lado. 
    - Se stride=2 vamos de 2 em 2 (saltamos 1)
- Temos:
$$\text{Tamanho saída} = \frac{\text{Tamanho Entrada} - \text{Tamanho Filtro}}{\text{Stride}} + 1$$

## Treinar NN profundas
### Problemas com o gradiente
- Em redes em que usamos sigmoide ou funções hiperbolicas como ativação, é comum ter o problema de *gradientes a anular* (vanishing, a ir para zero). Ou seja, consoante fazemos backpropagation o gradiente vai diminuindo. Quando chegamos ao início da rede ele é nulo:
![[backpropagation.png]]
    - RELU já ajuda a evitar isto
- No entanto, como estamos a usar valores numéricos, o gradiente poded **explodir**.
- Assim, temos os seguintes indícios que nos permitem inferir o que se estará a passar:
    - Gradientes a explodir: o modelo não aprende, loss oscila ou é NaN, os pesos aumentam muito ou torna-se NaN
    - Gradientes a anular: modelo aprende muito lentamente ou para, apenas os inputs perto do output mudam
- Temos algumas soluções:
    - Reduzir o tamanho dos gradientes para não explodirem
    - Usar algum método de pre-treino para garantir que o pesos começam com bons valores
    - Não ter todas as ligações das camadas feitas (dropout)
    - Batch normalization

### Problemas com learning rate
- Parâmetro mais importante e o mais difícil de acertar.
- Como seria de esperar, afeta muito a velocidade de treino, estabilização e decide se conseguimos sair de um mínimo local rumo a um mínimo melhor.
- Assim:
    - LR demasiado baixo: treino lento, difícil de sair de um sítio com gradiente baixo
    - LR demasiado alto: valores oscilam muito ou não convergem. Impossível chegar a mínimos estreitos
- Temos algumas estratégias:
    - Começar com LR grande inicialmente para garantir que os pesos iniciais random não afetam muito o resultado
    - Ir alterando o LR ao longo do treino 
- Assim, 2 formas de melhorar a convergência:
    - Ajustar o learning rate de cada dimensão separadamente
    - Substituir o gradiente pela sua moving average para aproveitar o "momento" dele (Adam)

### Regularização
- Para criar um modelo ML temos que definir a família de modelo a usar, a função de custo e o método de optimização.
- *Regularização*  pode ser definida como algo que fazemos ao modelo para que o seu erro de generalização diminua (mas não o de treino!)
    - Em termos do tradeoff bias-variancia, reduzimos a variância a aumentamos o bias. Quanto melhor a regularização, menos aumentamos o bias
- Uma forma de fazer isto é *penalizar normas* - isto é o que fazemos em Ridge, estamos a aumentar a perda de forma linear com a norma
- Outra forma consiste em *early stopping*. Como o nome indica, paramos o treino quando se deteta que a loss da validação não está a melhorar há algum tempo. Isto é feito para melhorar a performance do modelo.

### Data augmentation
- Quando a base de dados que temos não é ENORME, isto é uma técnica útil.
- Por exemplo, no caso de imagens, isto consiste em replicar uma imagem com algumas alterações (distorção, ruído, deformação, flip, mudança de cor) conforme o que queremos que a rede aprenda:
![[data augmentation.png]]

### Noise
- Regra geral, é importante que a rede seja robusta a ruído. Assim, pode ser útil inserir ruído nos pesos e/ou nas saídas

### Dropout
- Exatamente o que o nome indica:
![[dropout.png]]

## Learning Multi-Task
- Consiste em treinar uma rede com o objetivo de poder fazer uma série de tarefas
- Mais concretamente, redes podem ser treinadas para poder fazer muito bem tarefas/representações intermédias que podem ser usadas em várias tarefas distintas. Algo assim:
![[mutli task nn.png]]

## Optimizações para treinar redes profundas
- No passado, NN foram treinadas com o objetivo de se manterem convexas.
- No entanto, NN que sejam não lineares fazem com que a maioria das funções de perda não sejam convexas!

### Aprendizagem com gradiente
- Consistem em procurar exaustivamente um mínimo de perda. 
- É o método mais usado por NN
- Nomeadamente, é comum usar *descida do gradiente*. Este método baseia-se neste funcionamento que temos sempre perto de mínimos (locais e absolutos):
![[minimo vs derivada.png]]
ou seja, ao somar o gradiente (derivada em n-D) a um certo ponto, iremos parar a um ponto mais próximo do mínimo. Consoante repetimos isto, eventualmente chegamos ao mínimo em si.
- No que toca a encontrar mínimos de perda, temos:
![[minimos de loss e significados.png]]

### Computation Graph
- Isto é uma representação. 
- Uma linha/*edge* representa um argumento de função (AKA dependência). Apontam para nodos
- Um nodo/*node* para onde aponta um edge é uma **função** do nodo de onde sai.
    - Assume-se que um nodo sabe computar o seu valor e da sua derivada.
- Um exemplo simples de um graph:
![[computational graph.png]]

- Para fazer $\mathbf{x}^{T}\mathbf{Ax}$ temos:
![[computational graph 2.png]]
a rede da direita é mais direta. A rede da esquerda é mais versátil e geral.

#### Forward Propagation (FPROP)
- Consiste em seguir a ordem topológica, a ordem das setas
- Para um conjunto de entradas a rede calcula a saída de forma direta

#### Backward Propagation (BPROP)
- Fazemos a ordem inversa (da saída para as entradas)
- Calculamos a derivada de cada nó relativamente ao anterior. Com eles fazemos descida de gradiente
- Esta propagação funciona com qualquer função de ativação derivável
- Tem o dobro do custo computacional de FPROP
![[computational graph 3.png]]

### SGD
- Este método normalmente vai descendo pela loss até eventualmente atingir um ponto crítico (que pode ser um máximo, mínimo ou ponto de cela). Felizmente, na maioria dos casos atinge um mínimo.
- Massss, este mínimo apenas será local. É mais difícil garantir que vamos para um mínimo global.
- Se tivermos um sistema cuja função de perda só tem 1 mínimo (global) mas vários pontos de cela, o SGD pode mover-se entre pontos de cela, mas a performance da rede irá variar sem propriamente melhorar.
    - Neste caso, dizemos que o SGD está "preso"
    - Isto pode acontecer devido a condições iniciais demasiado más ou devido a gradientes com ruído
    - Isto pode levar a overfitting
- Ora, consoante a dimensão dos dados (dimensão as in 2D, 3D, ...) auemnta, diminui exponencialmente a chance de encontrar um mínimo (porque passam a haver muitos mais pontos de sela)

### Batch Normalization
- Consiste nisto:
![[batch normalization.png]]
- Transformamos cada batch numa distribuição normal e controlada
- Assim, cada batch transformável é diferenciável
- Isto reduz a dependência dos gradientes na escala dos valores e nos valores iniciais. Por garantir que tudo é diferenciável, estabilziamos e regularizamos a rede
- Reduz a necessidade de dropout

## Transfer Learning
- Na realidade, não é comum treinar uma rede CNN de raíz. Assim, usamos uma base de dados muito grande online. Por exemplo, VGG deep net está treinada com milhões de caras, mas para uma certa função.
- Se pegarmos nessa rede num ponto antes do fim, poderemos adaptá-la para a nossa função