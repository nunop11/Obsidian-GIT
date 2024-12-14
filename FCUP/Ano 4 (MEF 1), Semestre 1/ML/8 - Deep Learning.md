- Este PPT tem uma porção enorme a recordar e repetir coisas anteriores da UC

## Evitar overfitting
### Regularização
- Ao criar um modelo de ML, definimos: família do modelo, função de custo e método de otimização
- Regularização é algo que acrescentamos ao algoritmo de aprendizagem e que tem o objetivo de baixar o seu erro de *generalização* (menos overfitting) sem afetar muito o erro de treino.
- Na prática, ao introduzir um sistema de regularização estamos a aumentar o bias em troca de baixar a variância do modelo.
    - Assim, um bom regularizador minimiza a variância sem aumentar demasiado o bias
- Normalmente, isto consiste em introduzir um $\lambda$ na função de perda, de uma forma que estejamos a penalizar complexidade.

## ML clássico
![[Pasted image 20241211151218.png]]
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
![[Pasted image 20241211151721.png]]
- Um dos principais casos que devemos usar deep learning é: *Classificação Binária Complexa*, como acima.
- Usando NN, podemos obter representações mais compactas dos dados input-output. 
    - Uma NN é compacta se tiver poucos parâmetros livres 
    - Uma NN compacta deverá ter melhor performance de generalização
- Ou seja, em problemas muito complexos (ver foto, detetar audio, detetar texto), é quase impossível expressar a relação entre os pixeis de forma analítica.
- Ou seja, temos modelos que encontram/formam os atributos em si: *Representation Learning*
![[Pasted image 20241211152221.png]]

# NN Convolutional
## Deep Multilayer Perceptron (DNN)
- Consiste numa NN profunda (varias layers) e wide (muitos perceptrons por linha)
![[Pasted image 20241211152451.png]]

## Imagens
- Se tivermos uma imagem que queremos analisar com uma MLP, primeiro teremos que converter a imagem 2D num vetor muito longo 1D, pelo que perdemos informação sobre a disposição da imagem.
- Ao usá-la para aprender um modelo, ele irá otimizar esta sequencia de valores, mas basta fazer shift ou zoom na imagem e o modelo não funciona!
- Ou seja, o modelo determina pesos corretamente, mas eles variam com translação e scaling, pelo que são pesos que não úteis para estudar imagens
- Outra coisa que temos de ter em conta é que, por exemplo, para uma imagem 200x200, com uma MLP normal teremos BILIÕES de parâmetros se a rede for suficientemente deep.

### O que queremos
- Ora, naturalmente, queremos um modelo que detete algo numa imagem. Mesmo que o objeto seja: rodado, movido, deformado ou resized.
![[Pasted image 20241211152831.png]]

## Rede Convolucional
- Este tipo de rede consiste em poder estudar imagens de grande resolução ou até vídeos
- Passamos a ter *ligações esparsas* na NN (nem todos os perceptrons ligam a todos):
![[Pasted image 20241211153307.png]]
- Ocorre partilha de parâmetros determinados entre redes:
![[Pasted image 20241211153417.png]]
(isto reduz automaticamente o erro quando há translação)
- Pode ser usado para qualquer input numa grid (até 3D+)
- Permite reduzir imenso o número de parâmetros
![[Pasted image 20241211153235.png]]
- Falamos em **filters**
    - Se temos filtros 10x10, então cada filtro irá analisar uma região 10x10 píxeis
    - Além de dividir a imagem em partes, cada filtro pode alterar os dados. Por exemplo aplicando uma função para reduzir contraste
    - Podemos aplicar vários filtros às mesmas regiões, sucessivamente

### Convolução
- Ou seja, cada perceptron liga apenas aos seus vizinhos
- Mas falamos em convolução: isso implica que todas as ligações têm os mesmos pesos (que são partilhados):
![[Pasted image 20241211153723.png]]
- Existe então uma *camada de convolução* (kernel) que contém estes pesos
- Por exemplo, num caso 2D em que cada perceptron analiza um conjunto 2x2:
![[Pasted image 20241211153854.png]]

### Arquitetura
- Temos:
![[Pasted image 20241211154000.png]]

### Como funciona
![[Pasted image 20241211154104.png]]
- Pooling consiste em juntar grupos de dados em 1 só. Por exemplo, *max pooling* consiste em escolher o máximo dentro de cada bloco. Na imagem acima escolhemos o máximo em cada bloco 2x2. Abaixo escolhemos o máximo a cada 3 pontos:
![[Pasted image 20241211154609.png|500]]
- Existem muitas coisas diferentes que podem ser feitas, com diferentes arquiteturas, divisões da image, funções de ativação, etc etc. Ver PPT