### Vetores Unitários
$$(3, -2)$$
- Considere-se que temos o vetor acima. Pensemos então em cada  coordenada como um escalar.
- Ou seja, no vetor (3,-2) cada um destes escalares representa o quanto um *vetor unitário* é "esticado", como vimos no resumo [[1- Vetores]] acerca do produto de vetores com escalares
![[vetores unitarios.png]]
- Tendo um certo referencial 2D, tem-se estes vetores unitários:
    - $\hat i$, o vetor unitário em Ox, AKA $\hat e_x$
    - $\hat j$, o vetor unitário em Oy, AKA $\hat e_y$
- Em 3D teríamos ainda:
    - $\hat k$, o vetor unitário em Oz, AKA $\hat e_z$

- Ou seja, como cada uma das coordenadas representa o quanto temos que esticar $\hat i$ e $\hat j$ para que estes produtos *juntos* resultem no vetor $(3, -2)$.
- Ou seja, tem-se que
$$(3,-2)=3\hat i +(-2)\hat j$$

---
- Por outro lado, e se tivéssemos escolhidos vetores de refrência diferentes?
- Ora, o vetor obtido seria válidos na mesma, mas seria muito diferente relativamente ao uso dos vetores unitários $\hat i$ e $\hat j$.
- Isto será uma **nova base**, que veremos depois.
---

### Combinação Linear
- Sempre que sumamos 2 vetores multiplicados por escalares, como fizemos anteriormente, temos uma <ins>Combinação Linear</ins>. Tem-se isto, portanto:
 ![[combo linear (1).png]]
- Uma maneira de compreender esta nomenclatura (se bem que não é a verdadeira razão por detrás) é esta: Se os 2 vetores estiverem colocados como na figura acima e fixarmos um deles enquanto multiplicámos o outro por todos os números reais possíveis, a sua ponta irá traçar uma reta:
![[combo linear (2).png]]

- No entanto, se nenhum dos vetores estiver fixo e os multiplicarmos por números aleatórios, verificaremos que com eles podemos obter qualquer ponto do plano.
- Um outro caso é aquele em que os vetores são colineares, aí só podemos traçar uma reta
- Um último caso, e ainda menos comum, é se ambos os vetores forem $\vec 0$, aí só se fica na origem

### *Span*
- O conjunto de todos os vetores que podemos atingir com uma combinação linear, é o seu *Span*
- Ou seja, para vetores não colineares, o seu span é todos os vetores no espaço 2D. Para 2 vetores colineares o seu span é todos os vetores que estão contidos nessa reta.

#### Setas e Pontos
- Como uma espécie de truque para facilitar o raciocínio, quando se tem um vetor sozinho podemos imaginá-lo no plano como uma seta a partir da origem.
- No entanto, se tivermos um conjunto de vetores, será mais fácil de os imaginar/ilustrar representando cada um deles pelo ponto onde terminar quando partem da origem.

#### *Span* em 3D
- Se tivermos 2 vetores em 3D e precisarmos de saber o seu span, facilemente se conclui que o seu span será todos os vetores que se encontram no mesmo plano que este par de vetores. Ou seja, será um plano que passa na origem do refrencial.

### 3 vetores em 3D
- Imaginemos agora que acrescentamos um terceiro vetor a um esoaço 3D.
- A combinação linear dos 3 poderia ser represetnada por
$$a\vec u + b\vec v + c\vec w$$
- O span da combinação linear dos 3 vetores pode ser:
    - Se o terceiro vetor estiver contido no span da combinação linear dos 2 vetores iniciais, o span desta combinação linear com 3 vetores seria o mesmo
    - Se o terceiro vetor *não* estiver contido no span da combinação linear dos 2 vetores iniciais, o span desta nova combinação será todos os vetores que se encontram no espaço 3D. Para isto pode-se imaginar o seguinte exemplo: Temos os dois vetores iniciais e o seu span (vetor pela origem) representados no plano 3D. Ao colocar este novo vetor e manter os outros dois fixos, pode-se imaginar que o terceiro vetor "arrasta" o span dos outros dois até à sua extremidade.

> Ver o vídeo (8:00min) para melhor compreender o exemplo dado para o 2º caso 

## (In)Depêndencia Linear
- Quando temos n vetores, mas um deles é redundante, ou seja, *não permite* expandir o span da combinação linear dos n vetores, diz-se que se os vetores são **linearmente dependentes**.
    - Exemplo 1: O casos anterior de, em 2D, termos e vetores colineares. Para definir o seu span só precisaríamos de um deles, logo diz-se que eles são linearmente dependentes
    - Exemplo 2: O caso anterior de ter 3 vetores em 3D, mas em que um deles está contido no span da combinação linear dos outros dois.
- Por outras palavras, quando se tem 3 vetores linearmente dependentes, tem-se que:
$$\vec u = a\vec v + b\vec w$$
, ou seja, um dos vetores pode ser escrito como uma combinação linear dos outros.

- Por outro lado, se criámos um novo vetor que *permite* expandir o span da combinação linear dos vetores pré-existentes, diz-se que os vetores são **linearmente independentes**.


##### Definição técnica de BASE
- A base de um espaço vetorial é um conjunto de vetores linearmente independentes que têm um span que cobre o espaço inteiro.


#### Link do vídeo no Youtube:
https://youtu.be/k7RM-ot2NWY

#### Índice dos resumos
[[ALGA - INDEX]]

#alga 