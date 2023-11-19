$$\Huge{\text{Math Wars - O Despertar da Análise}}$$
*==----- O Resumo Final de Análise Real 1 -----==*

# Princípios/Axiomas/Teoremas
##### Conjuntos
- **Princípio da Indução Finita** - Permite comprovar propriedades por recursão:
    - Se $Y\subseteq\mathbb N$ , se $1\in Y$, $n\in Y \rightarrow  n+1\in Y$, então $Y=\mathbb N$
    - Provar que $2^n>n$: Seja $Y=\{n\in\mathbb N:~2^n>n\}$. $1in Y$, porque $2^1>1$. Assim, $2^{n+1}=2\cdot2^n>2n\geq n+1$. Logo $Y=\mathbb N$
- **Axioma do Supremo** - Se $A\subset\mathbb R$ é um conjunto não vazio e majorado, então tem supremo. Este garante também que todo o subconjunto não vazio e minorado de $\mathbb R$ tem ínfimo. 

##### Sucessões
- Todas as sucessões convergentes são limitadas. Logo, todas as sucessões monótonas e limitadas convergem. Além disso, uma sucessão monótona e não majorada/limitada terá limite +/- infinito.
- Se uma sucessão $(a_n)_n$ tem limite $L\in\mathbb R ~\cup \{+\infty,-\infty\}$  e $(a_{n_k})_n$ é a sua subsucessão, então $\lim_{k\to+\infty}a_{n_k}=L$ 
- Se $(a_n)_n$ é uma sequência monótona que tem uma subsucessão limitada, então $(a_n)_n$ converge.
- Todas as sucessões têm uma subsucessão monótona, logo uma sucessão limitada tem uma subsucesão convergente.
- Sucessões convergentes são sucessões de Cauchy, e vice-versa.

##### Funções
- O limite de uma função $f$ é $L$ se o limite da sequência de elementos do domínio de $f$ também for $L$. (a sucessão tem de converger)
- Se se tem 3 funções f,g,h tal que $f(x)\leq g(x)\leq h(x)$, se $\lim_{x\to a}f(x)=\lim_{x\to a}h(x)$, então $\lim_{x\to a}g(x)$ eciste e é igual aos outros dois limites.
- Se se tem 3 funções f,g,h tal que $f(x)\leq g(x)\leq h(x)$, se f e h são contínuas, g também será
- **Propriedade dos valores intermédios**: Verifica-se se qualquer que seja o par de pontos $x_0,x_1\in\mathcal I$ da função $f:\mathcal I\to\mathbb R$ tais que $x_0<x_1$ e $f(x_0)\neq f(x_1)$; para todo o $d\in[f(x_0),f(x_1)]$ existe $c\in~]x_0,x_1[$ tal que $f(c)=d$
- **TVI (Teorema dos Valores Intermédios)**: Se uma função $f:\mathcal I\to\mathbb R$ for contínua em $\mathcal I$, então ela apresenta a propriedade dos valores intermédios. Assim, a imagem de um intervalo por uma função contínua é um intervalo.
- **Corolário de TVI**: se tivermos $a<b$ e $g:[a,b]\to\mathbb R$ for uma função contínua em $[a,b]$. Se $g(a)\cdot g(b)<0$ então existe $c\in~]a,b[$ tal que $g(c)=0$.
- Se $f$ é um polinómio de grau ímpar, então $f$ é sobrejectiva e tem um zero
- Seja $f:\mathcal I\to\mathbb R$ um função contínua e injectiva, então $f$ é estritamente monótona e $f^{-1}$ é contínua
- Seja $f:[a,b]\to\mathbb  R$ uma função contínua em $[a,b]$. Então, a imagem de $f$ é um intervalo limitado e fechado. Ou sej,a $f:[a,b]\to\mathbb  R$ ,uma função contínua em $[a,b]$, então $f$ tem máximo e mínimo globais em $[a,b]$
- Se $f$ é um polinómio de grau par de grau $\geq2$, então $f$ tem um máximo ou mínimo global em $\mathbb R$
    
##### Derivadas
- Se $f:A\to\mathbb R$ for derivável em $a\in A$, então $f$ é contínua em $a$.
- Se $f:[a,b]\to\mathbb R$ atinge um máximo ou mínimo local em $c\in]a,b[$ e $f$ é derivável em $c$, então $f'(c)=0$
- Se $f:[a,b]\to\mathbb R$ atinge um máximo ou mínimo local em $c\in~]a,b[$ e $f$ é derivável em $c$, então $f'(c)=0$
- **Teorema de Rolle:** se $f:[a,b]\to\mathbb R$ é contínua em $[a,b]$, derivável em $]a,b[$ e $f(a)=f(b)$ então existe $c\in~]a,b[$ tal que $f'(c)=0$
- **Teorema de Lagrange**: Se $f:[a,b]\to\mathbb R$ é contínua em $[a,b]$ e derivável em $]a,b[$, então existe $c\in~]a,b[$ tal que $f'(c)=\frac{f(b)-f(a)}{b-a}$. Ou seja, existe um ponto do gráfico em que a reta tangente é paralela àquela que une $a$ e $b$.
- Se $f:\mathcal I\to\mathbb R$ e $g:\mathcal I\to\mathbb R$ são funções deriváveis em $\mathcal I$ e $f'(x)=g'(x)$ para $\forall x\in\mathcal I$, então $f$ e $g$ diferem por uma constante.
- **Lei de L'Hôpital**: Suponhamos que se tem $\lim_{x\to a}f(x)=\lim_{x\to a}g(x)=L$ e que existe o limite $\lim_{x\to a}\frac{f'(x)}{g'(x)}$. Tem-se então que $\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}$. Note-se que isto só se aplica quando $L=0,+\infty,-\infty$.

##### Integrais/Primitivas
- $f$ é integrável em $[a,b]$ se e só se $\forall\varepsilon>0~~\exists\mathcal P~~\text{partição de }[a,b]:~~~~S(f,\mathcal P)-s(f,\mathcal P)<\varepsilon$
- **Teorema Fundamental do Cálculo**: Tendo $F(x)=\int_a^xf$, primitiva de $f$, então tem-se que 
    - $\int_a^bf=F(b)-F(a)$
    - $F'(x)=f(x)$, $F''(x)=f'(x)$,etc
- O TFC garante que se uma função $f$ é contínua em $[a,b]$, então é primitável nesse intervalo.
- Primitivável: existe uma função cuja derivada é $f$.

# Resumo da matéria
## Conjuntos dos números reais
- $\mathbb N$- números naturais
- $\mathbb Z$- números inteiros
- $\mathbb Q$- números racionais
- $\mathbb R$- números reais

### Conjuntos minorados, majorados e limitados
- **Conjunto majorado** - um conjunto A é majorado se 
$$\exists ~M\in\mathbb R:~\forall x\in A~~~~x\leq M$$(M é majorante de A)
- **Conjunto minorado** - um conjunto A é minorado se 
$$\exists ~m\in\mathbb R:~\forall x\in A~~~~m\leq x$$(m é minorante de A)
- **Conjunto limitado** - um conjunto A é majorado se for minorado e majorado, ou seja, se 
$$\begin{align}\exists ~m, M\in\mathbb R &:~\forall x\in A~~~~m\leq x\leq M \leftrightarrow\\\leftrightarrow\exists~\ell\in\mathbb R^+ &:~\forall x\in A~~~~|x|\leq\ell\end{align}$$
($\ell=\max\{|m|,|M|\}+1$)
- Um **máximo** de A é um majorante de A que pertence a A. Um **mínimo** de A é um minorante de A que pertence a A. Note-se que só pode haver, no máximo, um de cada.

### Supremo e Ínfimo
- O **Supremo** de A é o *menor dos seus majorantes*. É portanto o mínimo do conjunto dos majorantes.
- O **Ínfimo** de A é o *maior dos seus minorantes*. É o máximo do conjunto dos minorantes.
- De notar que cada um destes é único.
- De notar também que se tiver algo tipo $A=]2,~5]$, então 5 é o máximo e o supremo. Além disso, o ínfimo de A é 2, e este conjunto não tem mínimo.

> Nota: **Caraterística** de x. Representada por $\lfloor x\rfloor$, é o maior inteiro menor ou igual a x. Exemplo $\lfloor \frac{4}{3}\rfloor =1$

### Cubconjuntos Densos de R
- Um conjunto $A\subseteq\mathbb R$ é denso em R se 
$$\forall~a,b\in\mathbb R~~~~a<b\rightarrow\exists~\alpha\in A:~~~~a<\alpha<b$$
- Ou seja, para qualquer par de números de A é possível encontrar um número entre eles. Por exemplo, $\mathbb Z$ não é denso em R

## Funções reais de variável real
- Uma função é um subconjunto não vazio do produto cartesiano, do tipo: $\mathbb R\times\mathbb R=\{(x,y):x,y\in\mathbb R\}$, sendo que dois pontos com o mesmo $x$ nunca poderão ter um $y$ diferente.
- O conjunto dos $x$ da função é o seu **domínio**. O conjunto dos $y$ é a sua **imagem**.
- O seu gráfico é dado por $\{(x,f(x)):x\in\mathbb R\}$
- Normalmente usa-se a notação $f:A\rightarrow B$, sendo que A é o domínio e B é o conjunto de chegada.

## Sucessões
- Uma família particular de funções, em que $D_f=\mathbb N$
- Em vez da notação $f:A\rightarrow B$ usaremos $(a_n)_{n~\in~\mathbb N}$ ou, simplificando, $a_n$

### Sequências monótonas
- Uma sucesão diz se **crescente** se $\forall n\in\mathbb N~~~~a_n\leq a_{n+1}$ e *estritamente crescente* se $\forall n\in\mathbb N~~~~a_n<a_{n+1}$
- Assim, uma sequência $a_n$ é **decrescente** se a sucessão $(-a_n)_{n~\in~\mathbb N}$ for crescente

### Sequências minoradas, majoradas e limitadas
- Basicamente aplica-se as mesmas definições de conjuntos, usadas acima.
    - Uma sequência é **majorada** se $\exists M\in\mathbb R:~~\forall n\in\mathbb N~~~~a_n\leq M$
    - Uma sequência é **minorada** se $\exists m\in\mathbb R:~~\forall n\in\mathbb N~~~~a_n\geq m$
    - Uma sequência é **limitada** se for majorada *e* minorada, ou seja, $\exists R\in\mathbb R^+:~~\forall n\in\mathbb N~~~~|a_n|\leq R$

### Sequências convergentes
- Uma sucessão é convergente se existir $\ell\in\mathbb R$ tal que: 
$$\forall\varepsilon>0~~\exists p_\varepsilon\in\mathbb N:~~n\geq p_\varepsilon~\rightarrow~|a_n-\ell|<\varepsilon$$
- Ou seja, como $|a_n-\ell|<\varepsilon ~\longleftrightarrow~ \ell-\varepsilon<a_n<\ell+\varepsilon$, tem-se que, para ser convergente, 
$$\lim_{n\to+\infty}a_n=\ell$$
(este limite é único)
- Se uma sucessão não converger, ou *não tem limite* ou *tem limite não real*
- Diz-se que uma sucessão tem limite $+\infty$ se $\forall\varepsilon>0,~\exists p_\varepsilon\in\mathbb N: n\geq p_\varepsilon\rightarrow a_n>\varepsilon$
- Diz-se que uma sucessão tem limite $-\infty$ se $\forall\varepsilon>0,~\exists p_\varepsilon\in\mathbb N: n\geq p_\varepsilon\rightarrow a_n<-\varepsilon$

### Operações com sucessões e limites
- Soma: 
$$(a_n)_{n\in\mathbb N}+(b_n)_{n\in\mathbb N}=(a_n+b_n)_{n\in\mathbb N}$$
- Produto: 
$$(a_n)_{n\in\mathbb N}~\cdot~(b_n)_{n\in\mathbb N}=(a_n \cdot b_n)_{n\in\mathbb N}$$
- Quociente: 
$$(a_n)_{n\in\mathbb N}~/~(b_n)_{n\in\mathbb N}=\bigg(\frac{a_n}{b_n}\bigg)_{n\in\mathbb N}$$
- Soma, produto e quociente de limites funcionam da mesma forma

> Caso específico de limites: $r^n$. Se $-1<r<1$, lim=0. Se $r=1$, lim=1.Se $r>1$, lim=+inf. E se $r\leq 1$, o limite não existe.

### Propriedades de limites de sucessões
- Se $\lim a_n=\ell$, $\lim b_n=L$ e $\forall n\in\mathbb N~~~~a_n\leq b_n$, então $\ell\leq L$
- Se $\lim a_n=\ell$, $\lim c_n=\ell$ e $\forall n\in\mathbb N~~~~a_n\leq b_n\leq c_n$, então $b_n$ converge e $\lim b_n=\ell$

### Subsucessões
- Uma subsucessão de $a_n$ é uma sucessã que se obtém escolhendo infinitos termos de $(a_n)_n$.
- Podemos representar isto como um conjunto assim: $\{a_1,a_2,a_3,...,a_k,a_{k+1},...\}$
- Assim, se uma sucessão $(a_n)_n$ tem limite $L\in\mathbb R ~\cup \{+\infty,-\infty\}$  e $(a_{n_k})_n$ é a sua subsucessão, então $\lim_{k\to+\infty}a_{n_k}=L$ 
- Para provar que uma sequência **não** tem limite basta apresetnar 2 subsequências com limites diferentes
- Se $(a_n)_n$ é uma sequência monótona que tem uma subsucessão limitada, então $(a_n)_n$ converge.
- Todas as sucessões têm uma subsucessão monótona, logo uma sucessão limitada tem uma subsucesão convergente.
- Se uma sucessão é monótona, logo converge e é limitada

### Sucessões de Cauchy
- Uma sucessão $(a_n)_n$ é de Cauchy se, a partir de uma certa ordem, os seus termos estão arbitrariamente perto uns dos outros. Ou seja,
$$\forall \varepsilon>0~~~~\exists p\in\mathbb N:~~\forall~n,m\in\mathbb N~~[n,m\geq p~~\rightarrow~~|a_n-a_m|<\varepsilon]$$
- Claramente, isto é o que acontece com sucessões convergentes. Ou seja, sucessões de Cauchy são convergentes e vice-versa.

## Funções
### Operações entre funções
- Soma: 
$$f(x)+g(x)=(f+g)(x)$$
- Produto: 
$$f(x)\cdot g(x)=(f\cdot g)(x)$$
- Inverso para a multiplicação: 
$$\frac{1}{g(x)}=\bigg(\frac{1}{g}\bigg)(x)$$
- Composição
$$f:A\rightarrow\mathbb R,~g:B\rightarrow\mathbb R~~ \longrightarrow~~g\circ f:A\rightarrow\mathbb R, (g\circ f)(x)=g(f(x))$$
Nesta operação, precisamos de saber a imagem de f. 

### Monotonia de funções
- Uma função diz-se **crescente** se $\forall ~x,a\in A~~x<a\rightarrow f(x)\leq f(a)$
- Uma função diz-se **decrescente** se $\forall ~x,a\in A~~x<a\rightarrow f(x)\geq f(a)$
- Uma função *estritamente* crescente ou decrescente poderia ser definida das maneiras acima, com a diferença que se usaria $>/<$ em vez de $\geq/\leq$

> Nota: a pré-imagem ou imagem inversa ou imagem recíproca de f é o inverso da sua imagem.

### Função sobrejectiva e injectiva
- Uma função $f:A\rightarrow B$ é **sobrejectiva** se $f(A)=B$, ou seja, se para todo o $b\in B$, a sua pré-imagem por f é um conjunto não vazio: $\forall b\in B~~\exists a\in A: ~~f(a)=b$
- Graficamente, a afirmação acima garante que cada valor de $y$ corresponde a pelo menos 1 valor de $x$

- Uma função $f:A\rightarrow B$ é **injectiva** se elementos diferentes de A têm iamgens distintas, ou seja: $f(a_1)=f(a_2)\longrightarrow a_1=a_2$. Ou seja, para cada $b\in B$, a sua pré-imagem por f é conjunto vazio ou um só elemento.
- Graficamente, isto significa que a reta horizontal que passa por cada valor de $y$ interserta f uma vez no máximo.

- Uma função $f:A\to B$ é **bijectiva** se for injectiva e sobrejectiva, ou seja, $\forall b\in B~~\exists^1 a\in A:~~~~ f(a)=b$
- Graficamente, isto significa que a reta horizontal que passa por cada valor de $y$ interserta f uma vez.

- De notar que se uma função é estritamente crescente ou decrescente, então é injectiva.

### Função inversa
- Seja $f:A\to B$ uma função injectiva. Se $Im_f=\{f(a):a\in A\}$ é a imagem de f, então a **função inversa** de f é a única função definida por 
$$g:Im_f~~\longrightarrow~~A$$
e que a cada $b\in Im_f$ associa o único $a\in A$ tal que $f(a)=b$
- A função inversa de $f$ é representada por $f^{-1}$

### Funções limitadas, majoradas e minoradas
- Ver acima. Funções limitadas, majoradas e minoradas podem ser definidas exatamente da mesma forma que sequências limitadas, majoradas e minoradas, mas com a notação de funções.

### Máximos, mínimos, ínfimo e supremo
- Seja $f:A\to\mathbb R$ uma função majorada. O **supremo** de f é o supremo do conjunto $f(A)$. O **valor máximo** de f será o máximo do conjunto $f(A)$
- As definições anólogas aplicam-se ao **ínfimo** e **valor mínimo** de f.

-- Seja $f:A\to\mathbb R$ uma função --
- O **máximo global** de f existe em $a\in A$ se $\forall x\in A~~~~ f(x)\leq f(a)$
- O **mínimo global** de f existe em $b\in A$ se $\forall x\in A~~~~ f(x)\geq f(b)$
- f tem um **máximo local** em $a\in A$ se $\exists\delta>0:~\forall x\in]a-\delta,a+\delta[~\cap~A~~~~f(x)\leq f(a)$ 
- f tem um **mínimo local** em $b\in A$ se $\exists\delta>0:~\forall x\in]b-\delta,b+\delta[~\cap~A~~~~f(x)\geq f(b)$ 

### Pontos de acumução de conjunto (p.a.)
- Dado o conjunto $A\subset\mathbb R$, diz-se que $c\in\mathbb R$ é um **ponto de acumulação** de A se 
$$\forall\delta>0~~~~(]c-\delta,c+\delta[~\setminus~\{c\}) \cap A\neq \emptyset$$
De modo an´alogo se define ponto de acumulação de A pela direita (usando-se $]c, c + \delta[$) e pela esquerda (usando-se $]c − \delta, c[$).
- Vi também esta definição online:
$$\forall\varepsilon>0,~~\exists y\in A:|x-y|<\varepsilon$$
- Ou seja, tendo $c$, ele é um ponto de acumulação de A se podermos aproximar-mo-nos dele com números infinitos de A.

### Limites de funções
#### Limite num ponto
- Seja $f:A\to\mathbb R$ uma funçã e $a\in\mathbb R$ um ponto de acumulação de A pela esquerda e pela direita. Tem-se ainda $\ell\in\mathbb R$
- Diz-se que $\ell$ é o limite de f quando x tende para $a$ se 
$$\begin{align}
\forall\varepsilon>0~~~~\exists\delta=\delta_{a,\varepsilon}>0&:\\
0<|x-a|<\delta~~~~e~~~~&x\in A\rightarrow|f(x)-\ell|<\varepsilon
\end{align}$$
Aquilo que é obtido no final ($|f(x)-\ell|<\delta$) quer dizer que, graficamente, a distância de f à reta horizontal $x=\ell$ e muito pequena, sendo menor que epsilon.

#### Limites laterais
- Se $a\in\mathbb R$ é um ponto de acumulação de A **pela direita**, diz-se que $\ell\in\mathbb R$ é o limite à direita de f quando $x\to a$ se:
$$\begin{align}
\forall\varepsilon>0~~~~\exists\delta=\delta_{a,\varepsilon}>0&:\\
0<x-a<\delta~~~~e~~~~&x\in A\rightarrow|f(x)-\ell|<\varepsilon
\end{align}$$
- Se $a\in\mathbb R$ é um ponto de acumulação de A **pela esquerda**, diz-se que $\ell\in\mathbb R$ é o limite à esquerda de f quando $x\to a$ se:
$$\begin{align}
\forall\varepsilon>0~~~~\exists\delta=\delta_{a,\varepsilon}>0&:\\
-\delta<x-a<0~~~~e~~~~&x\in A\rightarrow|f(x)-\ell|<\varepsilon
\end{align}$$

### Limites infinitos
- Sejam $f:A\to\mathbb R$ uma função e $a\in\mathbb R$ um p.a. de A pela esquerda e pela direita.
- Diz-se que o limite de f quando $x\to a$ é $+\infty$ se:
$$\begin{align}
\forall\varepsilon>0~~~~\exists\delta=\delta_{a,\varepsilon}>0&:\\
0<|x-a|<\delta~~~~e~~~~&x\in A\rightarrow f(x)<\varepsilon
\end{align}$$
- Anologamente se definem todos os outros limites em que f tende para infinito quando $x\to a$

- Seja f uma função e $\ell\in\mathbb R$. 
- Diz-se que o limite de f quando $x\to+\infty$ é $\ell$ se 
$$\begin{align}
\forall\varepsilon>0~~~~\exists\delta &=\delta_{a,\varepsilon}>0:\\
x>\delta~~~~e~~~~&x\in A\rightarrow|f(x)-\ell|<\varepsilon
\end{align}$$
- Anologamente se definem todos os outros limites em que x tende para infinito.

### Propriedade de limites
Sejam $f:A\to\mathbb R$ uma função e $a\in A$ um p.a. de A e $L\in\mathbb R\cup\{-\infty,+\infty\}$. Assim, $\lim_{x\to a}f(x)=L$ se e só se para toda a sucessão $(a_n)_n$ de elementos de A convergentes para $a$, se tem $\lim_{n\to+\infty}f(a_n)=L$.
- Por palavras mais simples, o limite de uma função $f$ é $L$ se o limite da sequência de elementos do domínio de $f$ também for $L$. (a sucessão tem de converger)

### Operações com limites
- Sendo $\alpha\in\mathbb R\cup\{-\infty,+\infty\}$ e $\ell_1,\ell_2\in\mathbb R$.
- Se $\lim_{x\to\alpha}f(x)=\ell_1,~\lim_{x\to\alpha}=\ell_2$, então $\lim_{x\to\alpha}(f+g)(x)=\ell_1+\ell_2$
- Se $\lim_{x\to\alpha}f(x)=\ell_1,~\lim_{x\to\alpha}=\ell_2$, então $\lim_{x\to\alpha}(fg)(x)=\ell_1\ell_2$
- Se $\lim_{x\to\alpha}f(x)=\ell_1\neq0$, então $\lim_{x\to\alpha}\frac{1}{f(x)}=\frac{1}{\ell_1}$
*Limite de composta:*
- Se tivermos $f:A\to B$ e $g:B\to C$, funções, e $a$ um p.a. de A. Se $\lim_{x\to a}f(x)=\ell$ ($\ell$ é p.a. de B) e $\lim_{t\to\ell}g(t)=\gamma$, então $\lim_{x\to a}(g\circ f)(x)=\gamma$
(no entanto, isto nem sempre é verdade)

### Limites e ordem
- Sejam $f:\mathbb R\to\mathbb R$ uma função monótona e $a\in\mathbb R$. Então:
    - Existem e são finitos $\lim_{x\to a^-}f(x)$ e $\lim_{x\to a^+}f(x)$
    - Se $f$ é crescente, $\lim_{x\to a^-}f(x)\leq f(a)\leq\lim_{x\to a^+}f(x)$
    - Se $f$ é decrescente, $\lim_{x\to a^-}f(x)\geq f(a)\geq\lim_{x\to a^+}f(x)$
    - Existem $\lim_{x\to\pm\infty}f(x)$

### Funções contínuas
- Esta é uma propriedade local, varia de $a$ para $a$.
- Diz-se que $f:A\to\mathbb R$ é contínua em $a\in\mathbb R$ se:
$$\forall\varepsilon>0,~\exists\delta>0:~~~~x\in A\wedge|x-a|<\delta\rightarrow |f(x)-f(a)|<\varepsilon$$
Basicamente, isto quer dizer que se considerar um x cada vez mais próximo de um ponto de acumulação $a$, as imagens de x irão aproximar-se de $f(a)$.
- Ou seja, uma função é contínua num ponto (que será um p.a.) se a função tiver o mesmo limite dos dois lados de $a$. Se $f(a)$ for real, ter-se-á:
$$\lim_{x\to a^-}f(x)=\lim_{x\to a^+}f(x)=f(a)$$

- Assim, uma função é **descontínua** em $a$ se:
    - Não existe limmite À direita ou esquerda de $a$ (isto não conta se a função não estiver definida à esquerda ou direita de $a$)
    - Existem limites à esquerda e direita, mas são diferentes.
    - Existem limites à esquerda e direita, são iguais, mas diferentes de $f(a)$

- Continuidade com sucessões: A continuidade de uma função pode ser verificada se $\lim_{n\to+\infty}f(a_n)=f(a)$

### Continuidade e operações
- Se f e g são contínuas em $a$, $f+g$ também é
- Se f e g são contínuas em $a$, $fg$ também é
- Se f e g são contínuas em $a$  e $g(a)\neq0$, $f/g$ também é
- Se $f:A\to B$ é contínua em $a$ e $g:B\to\mathbb R$ é contínua em $f(a)$, então $f\circ g$ também é contínua em $a$

### Funções reais em intervalos
- Considerando $a,b\in\mathbb R$ tais que $a<b$, temos $f:[a,b]\to\mathbb R$, uma função contínua em $[a,b]$. 
- A imagem de f será um intervalo $[m,M]$ tal que $m=\min\{f(x):x\in[a,b]\}$ e $M=\max\{f(x):x\in[a,b]\}$

### TVI
- Seja $\mathcal I$ um intervalo. Diz que que uma função $f:\mathcal I\to\mathbb R$ tem a **propriedade dos valores intermédios** se qualquer que seja o par de pontos $x_0,x_1\in\mathcal I$ tais que $x_0<x_1$ e $f(x_0)\neq f(x_1)$, para todo o $d\in[f(x_0),f(x_1)]$ existe $c\in]x_0,x_1[$ tal que $f(c)=d$
- Tem-se assim o **TVI (Teorema dos Valores Intermédios)** que diz que se uma função $f:\mathcal I\to\mathbb R$ for contínua em $\mathcal I$, então ela apresenta a propriedade dos valores intermédios. 
- Assim, a imagem de um intervalo por uma função contínua é um intervalo.
- **Corolário de TVI** declara que se tivermos $a<b$ e $g:[a,b]\to\mathbb R$ for uma função contínua em $[a,b]$. Se $g(a)\cdot g(b)<0$ então existe $c\in~]a,b[$ tal que $g(c)=0$.
- Consequências de TVI: 
    - Se $f$ é um polinómio de grau ímpar, então $f$ é sobrejectiva e tem um zero
    - Seja $\mathcal I$ um intervalo. Seja $f:\mathcal I\to\mathbb R$ um função contínua e injectiva, então $f$ é estritamente monótona e $f^{-1}$ é contínua
- Seja $f:[a,b]\to\mathbb  R$ uma função contínua em $[a,b]$. Então, a imagem de $f$ é um intervalo limitado e fechado. Ou sej,a $f:[a,b]\to\mathbb  R$ ,uma função contínua em $[a,b]$, então $f$ tem máximo e mínimo globais em $[a,b]$
- Se $f$ é um polinómio de grau par de grau $\geq2$, então $f$ tem um máximo ou mínimo global em $\mathbb R$

## Derivadas
### Derivada de função num ponto
- Seja $f:A\to\mathbb R$ uma função e $a\in A$. $f$ é **derivável em a** se *existe e é finito* o limite:
$$\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$$
- Se o limite existir, ele será o valor de $f'(a)$.
- $f$ é derivável à esquerda ou direita se o limite acima exisitir e for finito, respetivamente, se $x\to a^-$ e se $x\to a^+$
- Tem-se assim que se $f:A\to\mathbb R$ for derivável em $a\in A$, então $f$ é contínua em $a$.
- A derivada de uma função num ponto corresponde ao declive da reta tangente a $f$ no ponto de $f$ em que $x=a$

### Operações com derivadas
- **Soma**:
$$(f+g)'(a)=f'(a)+g'(a)$$
- Produto:
$$(fg)'(a)=f'(a)g(a)+f(a)g'(a)$$
- Inverso para a multiplicação:
$$\bigg(\frac{1}{g}\bigg)'(a)=-~\frac{g'(a)}{(g(a))^2}$$
- Quociente:
$$\bigg(\frac{f}{g}\bigg)'(a)=\frac{f'(a)g(a)-f(a)g'(a)}{(g(a))^2}$$
- Composição:
$$(g\circ f)'(a)=g'(f(a))f'(a)$$

### Relação entre f e f'
- Se $f:[a,b]\to\mathbb R$ atinge um máximo ou mínimo local em $c\in~]a,b[$ e $f$ é derivável em $c$, então $f'(c)=0$
- **Teorema de Rolle**: se $f:[a,b]\to\mathbb R$ é contínua em $[a,b]$, derivável em $]a,b[$ e $f(a)=f(b)$ então existe $c\in~]a,b[$ tal que $f'(c)=0$
- **Teorema de Lagrange**: Se $f:[a,b]\to\mathbb R$ é contínua em $[a,b]$ e derivável em $]a,b[$, então existe $c\in~]a,b[$ tal que $f'(c)=\frac{f(b)-f(a)}{b-a}$. Ou seja, existe um ponto do gráfico em que a reta tangente é paralela àquela que une $a$ e $b$.
- Se $f:\mathcal I\to\mathbb R$ e $g:\mathcal I\to\mathbb R$ são funções deriváveis em $\mathcal I$ e $f'(x)=g'(x)$ para $\forall x\in\mathcal I$, então $f$ e $g$ diferem por uma constante.
- Se $f:\mathcal I\to\mathbb R$ é uma função derivável em $\mathcal I$. Se para $\forall x\in\mathcal I,~~f'(x)\geq0$, então $f$ é crescente no intervalo. Se para $\forall x\in\mathcal I,~~f'(x)>0$, então $f$ é estritamente crescente no intervalo. Se para $\forall x\in\mathcal I,~~f'(x)\leq0$, então $f$ é decrescente no intervalo. Se para $\forall x\in\mathcal I,~~f'(x)<0$, então $f$ é estritamente decrescente no intervalo. 

### Regra de L'Hôpital
- Suponhamos que se tem $\lim_{x\to a}f(x)=\lim_{x\to a}g(x)=L$ e que existe o limite $\lim_{x\to a}\frac{f'(x)}{g'(x)}$. Tem-se então que $\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}$, que é a **Lei de L'Hôpital**. Note-se que isto só se aplica quando $L=0,+\infty,-\infty$.

### Relação entre f e f''
- $f''$ é a derivada de $f'$ e segunda derivada de $f$. Mais geralmente, $f^{(n)}$ é a $n$ derivada de $f$.
- Se $f'(a)=0$ e $f''(a)>0$, então f tem um mínimo em $a$
- Se $f'(a)=0$ e $f''(a)<0$, então f tem um máximo em $a$

- Seja $f:\mathcal I\to\mathbb R$ uma função definida em $\mathcal I$. $f$ é **convexa** em $\mathcal I$ se prar $\forall a,b\in\mathcal I$ com $a<b$, o gráfico de f em $[a,b]$ está abaixo da reta que une $(a,f(a))$ e $(b,f(b))$. Basicamente, tem concavidade para cima. Isto ocorre se $f''(x)>0$.
- Uma função $f$ é côncava em $\mathcal I$ se $-f$ for convexa, ou seja, se $f''(x)<0$.

## Integrais e Séries
--- Sobre estas matérias só tomei nota dos teoremas ---

## Log
- É a função definida para $x>0$ por $\log(x)=\int_1^x\frac{1}{t}dt$
- Ou seja:
$$\large\log(x)=\begin{cases}\int_1^x\frac{1}{t}dt~~~~se~~x\geq1\\\\-\int_x^1\frac{1}{t}dt~~~~se~~0<x<1\end{cases}$$
### Exp, a inversa de Log
- Tem-se que $\log^{-1}:\mathbb R\to]0,+\infty[$
- Tem-se que $(\log^{-1})'(x)=\log^{-1}(x)$
- Facilmente se percebe que a inversa de $\log$ é a **função exponencial**

$$\Huge FIM$$

#anal1 #resumo #matematica 