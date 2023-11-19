# Mudança de Base
-Baseado em : https://youtu.be/P2LTAUO1TdA -
## Referenciais
- Se tivermos um vetor, temos uma forma "normal" para o descrever. Se tivermos um vetor (2,3), então consideramos o 2 e o 3 como escalares e considerámos que para obter a extremidade do nosso vetor temos de multiplicar os vetores unitários (i e j) pela respetiva coordenadas e somar os produtos, obtendo que:
$$(2,3)=2\hat i+ 3\hat j$$
- Assim percebe-se que a maneira "normal" baseia-se nos vetores unitários que no referencial cartesiano podem ser definidos por (1,0) e (0,1).
- Desta forma, mantendo a estratégia de passar as coordenadas a uma soma de vetores básicos, podemos perceber que o nosso vetor podem ser definidos por qualquer par de vetores (não colineares), e assim obter coordenadas diferentes.

- Por outras palavras, o referencial que usamos, com os 2 eixos paralelos, um vertical e o outro horizontal, é inventado. Podemos fazer outros eixos, com uma nota importante: ==a origem do referencial (0,0) é a mesma==.
> ![[base canonica.png]] ![[base nova.png]]
- Como vemos nas figuras acima, ao mudar os vetores base, a direção sentido e tamanho da divisão dos eixos pode variar, mas a origem maném-se.

## Mudança de base
- Através de uma demonstração com animação feita no vídeo, percebe-se que se colocarmos as coordenadas dos vetores de uma nova base como colunas de uma matriz, essa será a matriz de uma [[2- Transformações Lineares]] que transforma pontos do referencial "normal" em pontos na nova base. Ou seja, é a **matriz de mudança de base**

- Mas e ao contrário? E se tivermos pontos na base nova e quisermos passar ao referencial normal? Será a inversa desta matriz.


> Nota: Sempre que digo "referencial normal" isto pode/deve de ser entendido como **base canónica**

### Transformações Lineares em nova base
- Imagine-se que temos as coordenadas de um ponto numa base nova e que lhe queremos aplicar uma transfromação (por exemplo rodar 90º)
- Ora, precisamos de ter a matriz da transformação na nova base.
- Iremos considerar que base canónica = $k$ e nova base = $\beta$
1. Primeiro precisamos de obter/saber a matriz de mudança de base $\beta \rightarrow k$ e $k \rightarrow \beta$.
2. Comecemos por multiplicar a matriz de mudança de base $\beta \rightarrow k$ pelas coordenadas do vetor em $\beta$. Assim obtemos as coordendas do ponto em k.
3. De seguida multiplicamos o resultado obtido pela matriz da transformação, para obter o vetor após a transformação, ainda em k.
4. Por fim, multiplica-se as novas coordenadas pela amtriz de mudança de base $k \rightarrow \beta$ para obter as coordenadas após a transformação em $\beta$.
Ou seja:
$$\left[M_{k, \beta}\cdot M_{transform} \cdot M_{\beta, k} \cdot \begin{pmatrix}x\\y\end{pmatrix}\right]^T$$
> Nota: É importante recordar que as operações fazem-se no sentido inverso, da direita para a esquerda. Ou seja, aquilo mais à direita será feito primeiro.

---
-Baseado em: https://youtu.be/yLi8RxqfowA-
## Verificar se vetores são base
- Se vetores forem uma base, então qualquer vetor pode ser escrito com uma combinação deles.
- Assim, eles ==têm de ser linearmente independentes==

### Verificar se são linearmente independentes:
Dois vetores serem linearmente independentes que dizer que
$$a\vec u+ b\vec v=0$$
Ou seja, tem-se que 
$$a\begin{pmatrix}x_u\\y_u\end{pmatrix}+b\begin{pmatrix}x_v\\y_v\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}$$
O que equivale a um sistema que em matriz aumentada fica assim:
$$\begin{pmatrix}ax_u & bx_v \bigm|0 \\ ay_u& by_v\bigm| 0 \end{pmatrix}$$
Assim, para verificar se os pontos são linearmente independentes, queremos saber se este sistema tem solução ou não.
- Se ==não tiver solução==, os vetores são linearmente ==dependentes==.
- Se ==tiver solução==, os vetores são linearmente ==independentes==

Ora, para verificar se tem solução ou não temos 2 métodos:

#### Maneira 1
- Como normalmente resolveríamos um sistema a partir da matriz aumentada, usar o método de Gauss de modo a simplificar a matriz e depois obter as variáveis.

#### Maneira 2
- Se calcularmos o determinante da matriz, podemos saber se tem solução trivial ou não.

---
### Calcular coordenadas numa nova base
- Tendo A e B, duas bases de R3. Precisamos de primeiro achar as matrizes de mudança de base. Depois para passar um vetor de uma base para outra, só precisamos de aplicar a matriz como se fosse uma transformação
- Consideremos então um exemplo prático:

Considere-se que temos uma base e os seus vetores:
$$\begin{align}
A &=[(1,0,1),(1,1,0),(2,2,-3)]\\
a_1&=(1,0,1)// a_2=(1,1,0)// a_3=(2,2,-3)
\end{align}$$
Considere-se que temos também que temos um vetor $\vec b(3,1,1)$ e que queremos obter as suas coordenadas em A.

Por definição, os vetores de uma base permitem reescrever qualquer vetor do espaço como uma combinação linear de si. Assim tem-se:
$$b=c_1a_1+c_2a_2+c_2a_2+c_3a_3$$
Se daqui conseguirmos obter os valores de $c_1,c_2,c_3$, estas serão as coordenadas de b em A.
Assim, se na igualdade acima substituirmos os vetores $b,a_1,a_2,a_3$ obteremos um sistema de 3 incógnitas e 3 sistemas. Se usarmos o método de Gauss facilmente o resolvemos. Neste caso, obtemos que $c_1=2,c_2=\frac{1}{3},c_3=\frac{1}{3}$. Assim, $[b]_A=(2,1/3,1/3)$

> Uma maneira de verificar o resultado obtido é verificar se
> $$[b_x]_Aa_1+[b_y]_Aa_2+[b_z]_Aa_3=b$$

### Matriz de mudança de base
- Se usarmos 3 vetores linearmente independentes, $b_1,b_2,b_3$ (que definem a base B)podemos obter a matriz de mudança de base $B\rightarrow A$, que ficaria assim:
$$M_{B,A}=\begin{pmatrix}[b_1]xA &[b_2]xA & [b_3]xA \\ [b_1]yA &[b_2]yA & [b_3]yA\\ [b_1]zA &[b_2]zA&[ b_3]zA\end{pmatrix}$$
- Ou seja, através do processo explicado anteriormente, igualando cada vetor de B a uma combinação linear dos vetores de A, obtemos as coordenadas dos vetores $b_1,b_2,b_3$ em A e fazemos com que cada uma delas seja uma coluna da matriz.
- Para obter a matriz de mudança de base $A\rightarrow B$, teríamos de fazer o processo de forma oposta.

#alga #mudança_de_base