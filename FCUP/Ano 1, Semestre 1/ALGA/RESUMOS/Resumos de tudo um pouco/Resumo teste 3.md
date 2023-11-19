# Resumo teste 3
# NOTAS IMPORTANTES
- rotações não têm auto valores
- se a matriz for simétrica, então os autovetores são perpendiculares
- numa transformação de Rn se o polinómio característico tiver n raizes distintas é diagonalizavel 
- vetor nulo pertence sempre a um subespaço vetorial
- tendo uma transformação Rn --> Rl a soma das dimensões do núcleo e da imagem dá n
- isto:
![[importante 1.png]]
- o espaço dos vetores perpendiculares a um vetor em R^n tem dimensão n-1
- isto:
![[importante 2.png]]
- se Ker=0 é injetiva e se (de Rn—>Rl) Im = l é sobrejetiva

## Espaços vetoriais
Um espaço vetorial V é um conjunto de duas oprações e oito propriedades. As operações são a soma e multiplicação por escalar:
Produto por um Escalar:
$$ \alpha v \in V $$
Adição:
$$ u + v \in V $$
![[propriedades espaço vetorial.png]]
- Um conjunto $S \subset V$ gera V se todos os elementos de V poderem ser escritos como combinação linear de um número linear de elementos de S

- Um conjunto $B\subset V$ é **uma base de V** se B:
    - For linearmente independente (verifica-se como sempre)
    - Gerar V 

## Transformações Lineares
Para qualquer $V$ e $W$ que sejam espaços vetoriais, $L: V \to W$ é uma transformação linear se, $\forall u, v \in V$ e $\alpha \in \mathbb R$:
- $L(u + v) = L(u) + L(v)$
- $L(\alpha v) = \alpha L(v)$

### Propriedades de transformações lineares
Sendo $L: V \to W$ uma transformação linear, sabemos que:

- $L(\textbf{0}) = \textbf{0}$
- $L$ fica determinada pelo seu valor de uma base de $V$
- $L$ pode ter inversa
- $\ker(L) = \{v\in V: L(v) = \textbf{0} \}$ → Núcleo de $L$
- $\text{Im}(L) =$ $\{w\in W|\ \exists v \in V: L(v) = w \}$ → Imagem de $L$
- $\ker(L) = \{\textbf{0}\} \leftrightarrow L \text{ é injetiva}$
- $\text{Im}(L) = W \leftrightarrow L \text{ é sobrejetiva}$
- $\text{dim } V = \text{dim ker}(L) + \text{dim Im}(L)$ se $V$ tiver dimensão finita

De recordar que trasnformações lineares são totalmente dependentes da base em que o seu domínio é definido. Assim, podemos ter matrizes de mudança de base como tínhamos para $\mathbb R^n$

### Isomorfismos
Uma transformação linear $L: V \to W$ é um isomorfismo se tiver uma inversa ($S=L^{-1}$) linear:
$$ S(L(v)) = v \quad\quad L(S(w)) = w $$
Caso exista um isomorfismo entre $S$ e $W$, então dizemos que $S$ e $W$ são isomorfos.
Para $L$ ser um isomorfismo é necessário que $\text{dim }V = \text{dim }W$.

## Núcleo e Imagem
O núcleo de $T$ é o **subespaço vetorial do domínio de $T$** formado pelo conjunto de vetores $u$ tais que $T(u) = \textbf{0}$:

$$ \ker(T) = \{u \in \mathbb R^n: T(u) = \textbf{0} \} $$
## Imagem

A imagem de uma transformação linear $T: \mathbb R^n \to \mathbb R^m$ é o **subespaço vetorial do conjunto de chegada** de $T$:

$$ \text{Im}(T) = T(\mathbb R^n) = \{v \in \mathbb R^m|\ \ \exists u \in \mathbb R^n: T(u) = v \} $$

### Transformações lineares Sobrejetivas
Uma transformação linear $L: \mathbb R^n \to \mathbb R^\ell$ é sobrejetiva se e só se:
$$ \dim \text{Im}(L) = n $$
E é injetiva se e só se:
$$ \dim \text{ker}(L) = 0 $$

## Autovalores e Autovetores
Sendo $T:R^n\rightarrow R^n$ um operador linear represetnado pelas matriz M:
- Para todo o $u\neq 0 \in \mathbb R^n$ e $\lambda\in \mathbb R$, se
$$T(u)=\lambda u$$
, então u é uma auotvetor de T e lambda é um autovalor de T
- Se um operador tiver n autovalores, existiram n autovetores, linearmente independentes.
- Para uma matriz em $\mathbb R^n$ ser diagonizavel, tem de ter n autovalores. Na versão diagonal, as entradas da matriz serão os autovalores

Also, $\langle u\rangle$ é o autoespaço associado a lambda

### Polinómio caraterístico
$$P_M(\lambda)=det(M-\lambda I)$$
- De notar que este é caraterístico ao operador em si, não há matriz, pelo que se mantem nas mudanças de bases

## Espaço dual
Ver [[12- Funcional e dual]] e [[13- Produto Escalar Geral]]

## Cónicas
Identificar:
![[tabela conicas.png]]
### Elipse
Uma elipse é uma figura geométrica plana em que a soma das distâncias dos seus pontos aos dois focos da elipse é sempre igual ([Geogebra](https://www.geogebra.org/m/xBg4a4YQ)).
Sendo os focos da elipse $F_1 = (-c, 0)$ e $F_2(c, 0)$, então a elipse é definida pela equação:
$$ \frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 $$

### Hipérbole
O módulo da diferença das distâncias aos dois focos é constante ([Geogebra](https://www.geogebra.org/m/FVfq4Sz3)).
Sendo os focos da hipérbole $F_1 = (-c, 0)$ e $F_2(c, 0)$, então a elipse é definida pela equação:
$$ \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1 $$

### Parábola
A distância de um ponto ao foco é igual à distância desse ponto a uma reta diretriz.
Sendo o foco da parábola $F = (c, 0)$ e a reta diretriz definida por $x = -c$, então a parábola é definida por:
$$ y^2 = 4cx $$
### Forma Quadrática
Uma forma quadrática é um polinómio de duas variáveis que só tem termos de grau 2:
$$ q(x, y) = ax^2 + bxy + cy^2 $$
Dada uma forma quadrática, podemos representá-la como o seguinte produto entre matrizes:
$$ q(X) = X \cdot A \cdot X^T $$
Em que $X = (x\quad y)$ e $A$ é uma matriz simétrica que representa a forma quadrática:
$$ A = \begin{pmatrix}
a & \frac{b}{2} \\
\frac{b}{2} & c
\end{pmatrix} $$

#### Máximo de uma Quadrática numa Circunferência
Podemos descobrir a direção dos eixos de uma cónica descobrindo os máximos e mínimos da sua respetiva quadrática quando está restrita à circunferência de raio $1$.
Para isso, vemos os máximos e mínimos da seguinte função:
$$ f(\theta) = q(\sin\theta, \cos\theta) $$

## Quádricas
Forma quadrática em três variáveis:
$$ \mathcal{Q}(x, y, z) = ax^2 + by^2 + cz^2 + dxy + exy + fyz $$
O conjunto $\{(x, y, z): \mathcal{Q}(x, y, z) = 1\}$ é chamado de **quádrica**.

### Matriz da Forma Quadrática
A forma quadrática pode ser escrita recorrendo ao produto entre matrizes, sendo $M$ uma matriz simétrica tal que:
$$ M = \begin{pmatrix}
a & d/2 & e/2 \\ d/2 & b & f/2 \\ e/2 & f/2 & c
\end{pmatrix} $$
Então, para $X = (x, y, z)$
$$ \mathcal{Q}(x, y, z) = X \cdot M \cdot X^T $$
. Tendo uma quadrática, podemos rodá-la em torno dos eixos Ox, Oy ou Oz
- Identificar quádricas:
![[tabela quadricas.png]]
![[tabela conicas 2.png]]

#alga