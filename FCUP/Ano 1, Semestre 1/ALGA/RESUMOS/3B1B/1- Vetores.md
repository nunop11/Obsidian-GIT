# 1- Vetores

### Vetores
- Vetores podem ser representados por 
    - Uma seta
    - Um par de valores

- Ao falar destes, imaginemos setas num espaço dividido por eixos e uma grelha. Ao contrário de física, em que podem ser livremente movidos, iremos considerar que vetores são setas, com o seu ponto de partida *fixo na origem*:
![[vetor em 2d.png]]


### O referencial 
- Começamos com uma linha horizontal, será o eixo dos x. Tracemos agora uma outra linha, perpendicular a x, será o eixo dos y. Estas duas linhas terão de ter um sentido em que o seu valor aumenta. Tem-se ainda que o ponto onde estas retas se cruzam é a origem do referencial.
- De seguida, fazemos divisões menores nos dois eixos, criando-se assim a escala do referencial.
- Assim, tendo um certo vetor com coordenadas $(-1, 2)$ sabemos que, partindo da origem dor eferencial, temos de andar 1 para *trás* no eixo dos Xs e andar 2 para *cima* no eixo dos Ys.

> Nota: Por vezes, como nestes vídeos do 3b1b, em vez de representar um vetor como A=(x, y)
> Usa-se, para distinguir vetores de pontos:
> $$A=\left[ \begin{array}{ccc} x \\ y\end{array} \right]$$

---
Abaixo tem-se a introdução de soma e produto de vetores por números, que será importante e muito falado ao longo destes vídeos
### Soma de vetores - Ínicio
- Usa-se a **regra do paralegramo ou do triângulo**:
![[Attachments/FCUP/A1S1/ALGA/soma de vetores.png]]
- Para isto, pode-se imaginar que um vetor é uma instrução ("ande x para a frente e y para cima"). Nesse caso, a soma de dois vetores seria o exemplo de seguir 2 instruções seguidas.
- Por outras palavras, nota-se que, se $\vec v$ nos diz para andar 2 para cima e depois $\vec w$  nos diz para andar 1 para baixo estamosa a sumar as instruções nesta direção: 2-1=1. Ou seja, ao seguir as duas instruções estamos portanto a subir apenas 1.
- Desta forma tem-se que:
$$(x_1, y_1)+(x_2, y_2)=(x_1+x_2, y_1+ y_2)$$

### Produto de vetor por número - Ínicio
- Gráficamente, vê-se que ao multiplicar um vetor por um número positivo, o comprimento deste irá mudar. Se o número for negativo, além de o seu comprimento mudar, o vetor vai-se virar para o outro lado. 
- A isto chama-se *Scaling*. Assim, o número por que multiplicamos o vetor é um *scaler*, um **escalar**.
- Nos vídeos seguintes veremos mais a fundo, mas temos que:
$$a.(x,y)=(ax,ay)$$
#### Link do vídeo no Youtube:
https://youtu.be/fNk_zzaMoSs

#### Índice dos resumos
[[ALGA - INDEX]]

#alga #vetores