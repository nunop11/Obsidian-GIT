-Baseado em https://youtu.be/vyYrvhbDhW4 -
# Dimensão, Imagem e Núcleo
## Dimensão
- Número mínimo de vetores geradores (linearmente independentes) necessários para definir um certo espaço vetorial.
- EXemplo: Para o subespaço $S=\langle (1,2,3),(0,1,1)\rangle$, $dim~S=2$

## Imagem
- Se tivermos uma transformação lienar L, ela irá pegar em vetores do espaço vetoriaç V e transformá-los em vetores do espaço vetorial W
- Assim, se escolhermos um subespaço de V, S, a transformação irá transformá-lo num subespaço de W, L(S), que é a imagem de S

- Uma analogia: imaginemos que temos uma lanterna a iluminar os espaço V. A área da superfície iluminada em W será a imagem
![[imagem de transformacao.png]]
- A imagem do espaço V inteiro tem um nome especial: *range*

### Exemplo
- Considere-se a transformação:
$$L:R^3\rightarrow R^2, ~~~~ L(\vec v)= (v_1, v_2-v_3)$$
- Assim, se tormarmos o subespaço
$$S=\{(x,2x,0)\in R^3\}$$
- A sua imagem será
$$L(x,2x,0)=(x, 2x-0)=(x,2x)=Im(S)$$


## Núcleo/Kernel
- Temos 2 espaços vetoriais V e W. Tal como na matéria anterior, temos uma transformação L que tansforma vetores de S em vetores de W. 
- O núcleo de V será o subespaço dos vetores que, após L, é igual a 0 (vetor nulo) em W.

### Exemplo
- Mais uma vez, consideremos a transformação:
$$L:R^3\rightarrow R^2, ~~~~ L(x,y,z)= (x, y-z)$$
- Para descobrir o núcleo, só temos de igualar L a 0. Assim:
$$\begin{align}
L(x,y,z)&=0 \leftrightarrow (x, y-z)=(0,0) \leftrightarrow \\
\leftrightarrow x&=0 ~~e~~y-z=0 \leftrightarrow x=0~~e~~y=z
\end{align}$$
- Assim, o núcleo de V será o subespaço vetorial dos vetores o tipo $(0,y,y)$.
- É importante recordar que o núcleo é um subespaço da imagem de V que por sua vez é um subespaço de W
- Para indicar o núcleo de um espaço vetorial V usamos: $ker(V)$.

# Verificar
- Se os cálculos forem realizados corretamente, 
$$dim Ker+dimIm=dimL$$

#alga