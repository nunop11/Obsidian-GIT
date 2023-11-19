# RESUMO DE ANALISE 2 - PARTE 2
# Funções
- Definição de Dominio, Contradomínio, limite e derivada é igual às das curvas.
- Uma função é *contínua* num ponto $X_0$ se for um ponto isoladoou se for um ponto de acumulação em que o limite for igual a $f(X_0)$
- Definições de bola, conjunto limitado, aberto e fechado é igual ao mostrado anteriormente.
- Conjuntos que são, simultaneamente, *limitados* e *fechados* são **compactos**.

- Seja f : $[a, b]\to\mathbb R$ uma função suficientemente derivável e seja $c : I \to\mathbb R$ a curva descrita em coordenadas polares pela equação $r = f(\theta)$
    - O Seu comprimento de arco será $\large\int_a^b [(f(\theta)^2+(f'(\theta))^2)]^{1/2}$

### Propriedades das derivadas
![[Pasted image 20220713114453.png]]
![[Pasted image 20220713114505.png]]
### Derivadas direcionais
$$f'(X_0;Y)=\lim_{t\to0}\frac{f(X_0+tY)-f(X_0)}{t}$$
- Esta é a derivada de $f$ no ponto $X_0$ na direção do vetor $Y$
- **Derivada parcial de f de ordem a x_i**: $\frac{\partial f}{\partial x_i}(X_0)$
- Se uma função multivariável for de classe $C^1$, quer dizer que todas as derivadas parciais de $x_1,x_2,\dots, x_n$ existem e são contínuas.

#### Derivada parcial de 2a ordem
- Pode ser $\Large \frac {\partial^2f}{\partial x_i\partial x_j}$ ou $\Large \frac{\partial^2f}{\partial^2x_i}$(se $i=j$)
    - Nota: $$\frac {\partial^2f}{\partial x_i\partial x_j}=\frac{\partial}{\partial x_i}\left(\frac{\partial f}{\partial x_j}\right)$$

## Derivada 
- Se $U\in\mathbb R^n$ for um aberto e $f:U\to\mathbb R$ tem derivada em $X_0$ ($Df_{X_0}$), então $\forall v\in\mathbb R^n$, existe $f'(X_0;v$)e temos $f'(X_0;v)=Df_{X_0}$
- Temos que $Df_{X_0}$ é uma aplicação linear de $R^n$ em $R$.
- Temos $$\Large Df_{X_0}(u)=\nabla f(X_0)\cdot u$$
- Nota: $D^2f_{X_0}$ é a segunda derivada de f em X0
- Nem todas as funções contínuas são deriváveis
- Uma função é derivável em $X_0$ se $$\lim_{X\to X_0}\frac{||f(X)-f(X_0)-Df_{X_0}(X-X_0)||}{||X-X_0||}=0$$

#### Propriedades da derivada:
![[Pasted image 20220713150616.png]]

### Superfícies de nível e grad
![[Pasted image 20220713150700.png]]
- Seja $U$ um aberto de Rn, $f:U\to\mathbb R$ uma função derivável e $c\in\mathbb R$. A superfície de nível $c$ de $f$ é $N_cf=\{X\in U:f(X)=c\}$ 
- Se $X_0\in N_cf$ e $\nabla f(X_0)\neq0$, então este vetor é **normal á hipersuperfície de nível**. 
- A *reta normal* é dada por $X=X_0+\lambda\nabla f(X_0),\quad\lambda\in\mathbb R$
- O *espaço/hiperplano tangente* é dado por $(X-X_0)\cdot\nabla f(X_0)=0$

- Seja $U$ uma aberto de $\mathbb R^n$ tal que, dados $X_1,X_2\in U$, existe uma curva contínua $\gamma:[a,b]\to U$ com $\gamma(a)=X_1,~~\gamma(b)=X_2$. Seja $f:U\to\mathbb R$ tal que $\nabla f(X)=0,~~\forall X\in U$. Então $f$ é constante.
- Seja $U$ um aberto de $\mathbb R^n$ nas condições do parágrafo acima e sejam $f,g:U\to\mathbb R$ funções deriváveis tais que $\nabla f(X)=\nabla g(X),\forall X\in U$. Então existe $C\in\mathbb R^n$ tal que $$f(X)=g(X)+C,\quad\forall X\in U$$
- **Teorema de Schwarz** - $\large\frac{\partial^2f}{\partial y\partial x}=\frac{\partial^2f}{\partial x\partial y}$ 

## FVVV (vet variavel vet)
#### Gráfico
- Se tivermos função $f:A\subseteq\mathbb R^n\to\mathbb R^m$ , então o seu gráfico será $$\text{Gra }f=\{(X,f(X)):X\in A\}\subseteq\mathbb R^{n+m}$$
exemplo: Função $R^2\to R$ tem gráfico em $R^3$

#### Função linear e afim.
- Ex de *linear*: $f(x,y)=2x+y$
- Ex de *afim*: $g(x,y)=X_0+f(X,y)$

#### Função componente
Tendo $f:\mathbb R^3\to\mathbb R^2$ dada por $f(x,y,z)=(xy,\sin(x+z))$, temos 2 funções componentes:
$$\begin{align}&f_1:\mathbb R^3\to\mathbb R && &&f_2:\mathbb R\to\mathbb R\\
&(x,y,z)\mapsto xy && && (x,y,z)\mapsto\sin(x+z)\end{align}$$
---
- As definições de limite, sup nível, continuidade, derivada parcial e direcional para funções vetoriais são iguais àquelas mostradas anteriormente.
- Propriedades:
![[Pasted image 20220713154147.png]]

### Matriz Jacobiana 
![[Pasted image 20220713154504.png]]
exemplo:
![[Pasted image 20220713155809.png]]

## Chain Rule
- Sejam $U\subseteq\mathbb R^n,V\subset\mathbb R^m$ e sejam $f:U\to R^m,g:V\to R^p$ duas funções tais que $f(U)\subseteq V\subseteq R^m$.
- Suponhamos que $f$ é derivável em $X_0\in U$ e $g$ é derivável em $f(X_0)\in V$. Então $g\circ f:U\to\mathbb R^p$ é derivável em $X_0$
- Assim temos $$D(g\circ f)_{X_0}=Dg_{f(X_0)}\circ Df_{X_0}$$
$$\mathcal J(g\circ f)_{X_0}=\mathcal Jg_{f(X_0)}\mathcal Jf_{X_0}$$



- $T:\mathbb R^m\to\mathbb R^n$ uma aplicação linear. Então existe $M\in R$ tal que $||T(v)||\leq M||v||,~~\forall v\in\mathbb R^m$

# Máximos e mínimos de funcs escalares
- Um ponto $X\in\mathbb R^n$ diz-se interior num subconjunto $D\subseteq\mathbb R^n$ se existe ε > 0 tal que $B(X; ε) \subseteq D$. (Note-se que D é aberto se e só se todos os seus pontos são interiores.)
- **Ponto crítico** - ponto em que o gradiente é nulo.

> Se $f:D\to\mathbb R$ é uma função contínua onde D é um subconjunto 
---

#### Teorema de Taylor
![[Pasted image 20220713172707.png]]


## Quádricas
$$ax^2 + by^2 + cz^2 + 2dxy + 2exz + 2fyz + gx + hy + iz$$
- A superfícies de nível deste tipo chamamos de sups quádricas
$$ ax^2 + by^2 + cz^2 + dxy + exz + fyz $$
- Podemos ainda ter funções quadráticas em $x,y,z$.

- Podemos ainda escrever a quádrica como um produto de matrizes:
$$ \begin{bmatrix} x & y & z \end{bmatrix} \begin{bmatrix}a & d & e \\ d & b & f \\ e & f & c \\\end{bmatrix} \begin{bmatrix}x \\ y \\ z\end{bmatrix}-   \begin{bmatrix}g & h & i\end{bmatrix} \begin{bmatrix}x \\ y \\ z\end{bmatrix} + j = 0 $$
($X^TAX+K^TX+j=0$)

![[Pasted image 20220713174024.png]]
![[Pasted image 20220713174044.png]]
![[Pasted image 20220713174147.png]]
### Aproximação de qudrática
$$ \begin{align*}

Q_{f,\ X_0} = f(X_0) + \nabla f(X_0) \cdot (X - X_0) + \frac12(X - X_0) \text{Hess }f(X_0)(X-X_0)^T

\end{align*} $$

## Hesseana
$$ \text{Hess }f(X_0) = \mathcal{J}(\nabla f)(X_0) =
\begin{bmatrix}
\frac{\partial^2f}{\partial x_1^2}(X_0) & \dots & \frac{\partial^2f}{\partial x_n \partial x_1}(X_0)
\\ \\ \vdots & \ddots & \vdots \\ \\
\frac{\partial^2f}{\partial x_1\partial x_n}(X_0) & \dots & \frac{\partial^2f}{\partial x_n^2}(X_0)
\end{bmatrix} $$

### Hesseana e extremos
Temos que, se $\text{Hess f}(X_0)$ tiver:
1.  Apenas autovalores positivos, $f$ tem mínimo local em $X_0$.
2.  Apenas autovalores negativos, $f$ tem máximo local em $X_0$.
3.  Autovalores positivos mas também negativos, então $X_0$ é ponto sela de $f$.
4.  Apenas autovalores maiores ou iguais a zero e algum é positivo, então $f$ tem mínimo local ou ponto sela em $X_0$ (excluímos máximo).
5.  Apenas autovalores menores ou iguais a zero e algum é negativo, então $f$ tem máximo local ou ponto sela em $X_0$ (excluímos mínimo).

## Jacobiana
![[Pasted image 20220714175821.png]]

## Teorema Sylvester
Seja $\Delta_k(f)$ o k-ésimo menor principal da matriz Hesseana de $f$ em$X_0$

Tem-se:
-   Se:
    -   $\Delta_k > 0$ para todo $k \in \{1, 2,\ \dots\ ,n \}$ **-->> MÍNIMO**
-   Então todos os autovalores de $\text{Hess } f(X_0)$ são positivos (não nulos) e, por isso, $X_0$ é um ponto de **mínimo** local de $f$.
---
-   Se:
    -   $\Delta_k < 0$ para todo $k$ ímpar com $k \in \{1, 2,\ \dots\ ,n \}$
    -   $\Delta_k > 0$ para todo $k$ par com $k \in \{1, 2,\ \dots\ ,n \}$
    -   Ou seja, se o sinal dos menores vai **alternando começando em negativo -->> MÁXIMO**
-   Então todos os autovalores de $\text{Hess } f(X_0)$ são negativos (não nulos) e $X_0$ é um ponto de **máximo** local de $f$.

---
## Convexidade de uma func
- Uma função é convexa entre 2 pontos se o seu gráfico se encontra abaixo do segmento de reta que une os pontos.
- Podemos relacionar isto com a derivada. Se $f$ é derivável e $f'$ é crescente, então $f$ é convexa. Ou então se $f$ é 2 vezes derivável e $f''>0$ então $f$ é convexa.
- Num intervalo $I$ aberto de $R$, se $f$ é convexa, então é contínua.
-  Sendo:
    -   $I$ um intervalo de $R$
    -   $f: I \to R$ uma função convexa
    -   $a$ um ponto interior de $I$
Então:
    -   $D_- f(a) = \sup_{x < a} \frac{f(x) - f(a)}{x - a}$
    -   $D_+ f(a) = \inf_{y > a} \frac{f(y) - f(a)}{y - a}$
Existem e $D_- f(a) \le D_+ f(a)$

### Desigualdade de Jensen
- Seja:
    -   $f: I \to R$ uma função convexa
    -   $x_1,\ \dots\ x_n \in I$
    -   $\alpha_1,\ \dots\ \alpha_n \in\ ]0, 1[$ tais que $\sum_{i=1}^n \alpha_i = 1$
Então tem-se:
$$ f\left(\sum_{i=1}^n \alpha_i x_i\right) \le \sum_{i=1}^n \alpha_i f(x_i) $$
Sendo a desigualdade estrita se houver pelo menos dois $x_i$ diferentes.

## Função implícita
### Funções escalares
- Seja: 
    -   $U$ um aberto de $R^{n+1}$
    -   $f: U \to R$ uma função de classe $C^k$ com $k \ge 1$
    -   $(X_0, y_0)$ um ponto de $U$ tal que $f(X_0, y_0) = c$ e $\frac{\partial f}{\partial y}(X_0, y_0) \ne 0$
    -   $X_0$ representa as primeiras $n$ componentes do ponto
    -   $y_0$ é a última componente do ponto
- Então existem:
    -   Uma bola fechada $B = B(X_0, \delta)$ de $R^n$ e
    -   Um intervalo $J =\ ]y_0 - \varepsilon, y_0 + \varepsilon[$

Tais que, sendo $\bar{J} = [y_0 - \varepsilon, y_0 + \varepsilon]$:
1.  $B \times \bar J \subseteq U$ e $\frac{\partial f}{\partial y}(X, y) \ne 0$ para todo o $(X, y) \in B \times \bar J$
2.  $\forall X \in B$ existe um único $y = \varphi(X) \in J$ tal que $f(X, y) = c$

A função $\varphi: B \to J$ assim definida é de classe $C^k$ e as suas derivadas parciais em cada ponto $X \in B$ são dadas pela fórmula:
 
> $$ \frac{\partial \varphi}{\partial x_i}(X) = -\frac{\frac{\partial f}{\partial x_i}(X, \varphi(X))}{\frac{\partial f}{\partial y}(X, \varphi(X))} $$

### Multivariável
Seja:

-   $U$ um aberto de $R^n$
-   $f: U \to R^m$ uma função com componentes $(f_1,\ \dots\ f_m)$, tal que:
    -   $\frac{\partial f_i}{\partial x_j}$ tem domínio $U$ para quaisquer $i \in \{1,\ \dots\ ,m \}$ e $j \in \{1,\ \dots\ ,n \}$

Dados $i_1,\ \dots\ i_r \in \{1,\ \dots\ n \}$ distintos, dizemos que:

$$ \frac{\partial(f_1,\ \dots\ ,f_m)}{\partial(x_{i_1},\ \dots\ ,x_{i_r})}(X_0) = \begin{bmatrix}
\frac{\partial f_1}{\partial x_{i_1}}(X_0) & \dots & \frac{\partial f_1}{\partial x_{i_r}}(X_0)
\\\vdots & & \vdots
\\\frac{\partial f_m}{\partial x_{i_1}}(X_0) & \dots & \frac{\partial f_m}{\partial x_{i_r}}(X_0)
\end{bmatrix} $$
Temos que:
-   A linha $i$ tem as derivadas parciais de $f_i$ em função a todas as variáveis escolhidas.
-   A coluna $i$ tem as derivadas parciais das componenetes de $f$ escolhidas em função de $x_{i_1}$.

## Teorema da Função Implícita
## Teorema da Função Implícita

 Seja:
 -   $U$ um aberto de $R^{n+m}$
 -   $f: U \to R^m$ uma função de classe $C^k$ com $k \ge 1$
 -   $(X_0, Y_0) \in R^n \times R^m$ um ponto de $U$ tal que:
     -   $f(X_0, Y_0) = c$
     -   $\det \left(\frac{\partial (f_1,\ \dots\ , f_m)}{\partial (x_{n+1},\ \dots\ ,x_{n+m})}(X_0, Y_0)\right) \ne 0$
 Então existem:
 -   Um aberto $V$ de $R^n$ contendo $X_0$
 -   Um aberto $W$ de $R^n$ contendo $Y_0$
 -   Uma função $\varphi: V \to W$
 Tais que:
 1.  $V \times W \subseteq U$
 2.  $\det \left(\frac{\partial (f_1,\ \dots\ , f_m)}{\partial (x_{n+1},\ \dots\ x_{n+m})}(X, Y)\right) \ne 0$ para todo $(X, Y) \in V \times W$
 3.  $\forall X \in V$, o ponto $Y = \varphi(X)$ é o único ponto de $W$ tal que $f(X, Y) = c$
 A função $\varphi$ é de classe $C^k$ e a sua matriz Jacobiana é dada por: 
 $$ \begin{align} 
\mathcal{J}\varphi_X = - \left(\frac{\partial (f_1, \dots , f_m)}{\partial (x_{n+1}, \dots ,x_{n+m})}(X, \varphi(X))\right)^{-1} \frac{\partial (f_1, \dots , f_m)}{\partial (x_1,\dots ,x_n)}(X, \varphi(X))
\end{align} $$

## Teorema da Função Inversa

Seja: 
 -   $U$ um aberto de $R^n$
 -   $f: U \to R^n$ uma função de classe $C^k$ com $k \ge 1$
 -   $X_0 \in U$ tal que $\det (\mathcal J f_{X_0}) \ne 0$
 -   $Y_0 = f(X_0)$
 Então existe:
 -   Um aberto $V \subseteq U$ que contém o ponto $X_0$
 -   Um aberto $W \subseteq R^n$
 Tal que:
 -   $f \vert_V : V \to W$ é invertível
 -   $f\vert_V$ tem inversa $g$ de classe $C^k$, sendo a sua matriz jacobiana num ponto $Y$:
     $$ \mathcal J g_Y = (\mathcal J f_{g(Y)})^{-1} $$

## Lagrange
### Teorema:
Seja:
-   $U$ um aberto de $R^n$
-   $f: U \to R$ uma função derivável
-   $g: U \to R^m$ uma função de classe $C^1$ com funções componentes $g_1, ...\ , g_m$
-   $N = N_cg$ a hipersuperfície de nível $c$ da função $g$
-   $f\vert_N$ a restrição da função $f$ ao conjunto $N$
-   $X_0$ um ponto regular de $N$
-   $X_0$ um ponto de máximo ou mínimo local de $f\vert_N$

Então $\nabla f(X_0)$ pertence ao espaço normal a $N$ em $X_0$.
Isto é, existem $\lambda_1,\ \dots\ ,\lambda_m \in R$ tal que:
$$ \nabla f(X_0) = \lambda_1 \nabla g_1(X_0) + \dots + \lambda_m \nabla g_m(X_0) $$

- Através deste gradiente vemos que ao restringir f à hipersuperfície de nível $N=N_cg$ de outra função g, os espaços normais às hipersuperfícies de f e g coincidem nos extremos locais de $f|_N$

#anal2 #resumo #matematica 