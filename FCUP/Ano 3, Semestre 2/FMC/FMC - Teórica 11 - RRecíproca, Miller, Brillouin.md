###### Aula 11 - 4/4/2024

## Rede Recíproca
### Definição matemática
- Consideremos uma rede de Bravais com pontos $\vec{R}$. 
- Consideremos ainda uma onda plana $e^{i\vec{k}\cdot\vec{r}}$. Ora, esta onda obviamente não terá a periodicidade da rede de Bravais para qualquer $\vec{k}$.
- MAS, existirá um conjunto de vetores de onda $\vec{K}$ específico para os quais a onda apresenta a periodicidade. De uma forma matemática:
$$e^{i \vec{K}\cdot\vec{r}}=e^{i\vec{K}\cdot(\vec{r}+\vec{R})}$$
ou
$$\boxed{e^{i\vec{K}\cdot\vec{R}}=1}$$
- Sendo que estas igualdades são válidas para qualquer $\vec{r}$ e para todos os pontos $\vec{R}$ da rede.

### Definição geométrica / Vetores Primitivos
- Nas últimas aulas vimos que um vetor de rede pode ser definido por $\vec{R_{n}}=\sum_{i=1}^{3}n_{i}\vec{a_{i}}$ 
- Tendo um vetor $\vec{a}$ de uma rede de Bravais, a rede recíproca será $\vec{b}$, em que
$$\vec{b}_{i}\cdot\vec{a}_{j}=2\pi n \delta_{ij}$$
logo $\vec{a}_{i}\parallel \vec{b}_{i}~~;~~ \vec{a}_{i}\perp\vec{b}_{j}~,~i\neq j$
- O facto de $n$ poder ser um qualquer inteiro permite "inverter" e "esticar" os vetores da rede recíproca obtida. Isto deve-se às caraterísticas de simetria das redes de Bravais.

**Caso Geral : 3D**
- Consideremos uma rede descrita pelos vetores $\vec{a_{1}},\vec{a_{2}},\vec{a_{3}}$. Temos:
$$\begin{align*}
\vec{b_{1}}&= 2\pi\frac{\vec{a_{2}}\times\vec{a_{3}}}{|\vec{a_{1}}\cdot(\vec{a_{2}}\times\vec{a_{3}})|}= \frac{2\pi}{V} (\vec{a_{2}}\times\vec{a_{3}})\\
\vec{b_{2}}&= \frac{2\pi}{V} (\vec{a_{3}}\times\vec{a_{1}})\\
\vec{b_{3}}&= \frac{2\pi}{V} (\vec{a_{1}}\times\vec{a_{2}})
\end{align*}$$
isto consiste em rodar os índices: $123, 231, 312$.

## 1D
**Rede 1D**
- Consideremos uma rede 1D na direção x, com pontos distanciados de $a$. Teremos $\vec{a}=a\hat{i}$.
- Neste caso teríamos que a rede recíproca é definida por $\vec{b}=\frac{2\pi}{a}\hat{i}$. 
- Ou seja, para uma rede linear, a rede recíproca também é linear.

**Fourier**
- Podemos definir a "densidade" de pontos da rede com $f(x)=\sum_{n=-\infty}^{+\infty}\delta(x-na)$
- Porque não determinar a sua FT: $$\begin{align*}
f(k)&= \int_{-\infty}^{+\infty}f(x)e^{-ikx}dx\\
&= \int_{-\infty}^{+\infty}\sum\limits_{n=-\infty}^{+\infty}\delta(x-na)e^{-ikx}dx\\
&= \sum\limits_{n=-\infty}^{+\infty}\int_{-\infty}^{+\infty}\delta(x-na)e^{-ikx}dx\\
&= \sum\limits_{n=-\infty}^{+\infty} e^{ikna}
\end{align*}$$

*Continhas Giras*
- Podemos definir $$\begin{align*}
S= \sum\limits_{\ell=0}^{N-1}e^{i \ell aq}~~\to~~e^{iaq}S= \sum\limits_{\ell=0}^{N-1}e^{i\ell aq}e^{iaq}
= \sum\limits_{\ell=0}^{N-1} e^{i(\ell+1)aq}
\end{align*}$$
temos $$\sum\limits_{\ell=0}^{N-1}e^{iaq(\ell+1)}=\sum\limits_{\ell=0}^{N-1}e^{iaq\ell}-1+e^{iNaq}=S-1+e^{iNaq}$$
> Explicação:
>     - Partimos da soma $\sum_{\ell=0}^{N-1}e^{iaq(\ell+1)}$ que vai ter termos $e^{iaq1},e^{iaq2},\dots, e^{iaqN}$. Vemos que esta soma equivale $e^{iaq}S$
>     - Decidimos substituir esta soma por $\sum\limits_{\ell=0}^{N-1}e^{iaq\ell}$, que tem os termos $1, e^{iaq1},\dots,e^{iaq(N-1)}$. Esta soma equivale $S$
>     - Ora, é evidente que (em relação à soma original) temos o termo $1$ a mais e falta o termo $e^{iaqN}$, por isso subtraimos o primeiro e somamos o segundo.

Logo podemos escrever:
$$\begin{align*}
e^{iaq}S&= S-1+e^{iNaq}\\
S&= \frac{e^{iNaq}-1}{e^{iaq}-1}=\frac{e^{iNaq/2}(e^{iNaq/2}-e^{-iNaq/2})}{e^{iaq/2}(e^{iaq/2}-e^{-iaq/2})}=\frac{e^{i \frac{N}{2}aq}}{e^{i \frac{aq}{2}}}\frac{\sin\left(\frac{Naq}{2}\right)}{\sin\left(\frac{aq}{2}\right)} 
\end{align*}$$
- Recordemos que isto continua a ser a equação da transformada de Fourier:
$$f(k)=\frac{e^{i \frac{N}{2}aq}}{e^{i \frac{aq}{2}}}\frac{\sin\left(\frac{Naq}{2}\right)}{\sin\left(\frac{aq}{2}\right)} $$
que de alguma forma é igual a:
$$f(k)=\frac{2\pi N}{L}\sum\limits_{m} \delta\left(k-2\pi \frac{m}{a}\right)$$
- Ora, vemos que isto só não é nulo se $k=\frac{2\pi}{a}m$: Podemos ver que isto bate certo as relações $\vec{a_{i}}\cdot \vec b_{j}$ vistas acima, ou seja, a *transformada de Fourier da rede real* é a **Rede Recíproca**! Assim, usando FT e IFT podemos obter a rede real da rede recíproca e vice-versa.

### Funções Periódicas na Rede
- Uma função periódica na rede será, como o nome indica, uma função que segue a equação:
$$f(\vec{r}+\vec{R})=f(\vec{r})$$
- Para este tipo de funções, ao determinar a sua FT podemos dividir o integral de todo o espaço nos integrais de cada uma das células:
$$\begin{align*}
\tilde f(\vec{k})&= \int_{\mathbb{R}^{n}}f(\vec{r})e^{-i \vec{k}\cdot\vec{r}}d\vec{r}\\
&= \sum\limits_{\vec{R}} \int_\text{cell} e^{-i \vec{k}\cdot(\vec{r'}+\vec{R})}f(\vec{r'}+\vec{R})d\vec{r'}\\
&= \sum\limits_{\vec{R}}e^{-i \vec{k}\cdot\vec{R}}\int_\text{cell} e^{-i\vec{k}\cdot\vec{r'}}f(\vec{r'})d\vec{r'}\\
&= \frac{(2\pi)^{N}}{d(\vec{R})}\sum\limits_{\vec{K}}\delta(\vec{k}-\vec{K})\cdot\tilde f_{0}(\vec{k})
\end{align*}$$
em que $\tilde f_{0}$ é o *fator de estrutura*, que veremos mais à frente. $d(\vec{R})$ é o covolume da rede real.

## 2D - Retangular
**EXEMPLO : Rede 2D**
- Consideremos uma rede real $\vec{a}$ com $\vec{a_{1}}$ com direção xx e $\vec{a_{2}}$ com direção yy (pontos distanciados de $a_{1}$ na horizontal e $a_{2}$ na vertical). Ou seja: $\vec{a_{1}}=a_{1}\hat{i}~~,~~ \vec{a_{2}}=a_{2}\hat{j}$
- Assim, temos:
$$\begin{align*}
\vec{a_{1}}\cdot \vec{b_{1}}&= 2\pi\\
\vec{a_{1}}\cdot \vec{b_{2}}&= 0\\
\vec{a_{2}}\cdot \vec{b_{1}}&= 0\\
\vec{a_{2}}\cdot \vec{b_{2}}&= 2\pi
\end{align*}$$
e daqui temos que $\vec{a_{1}}\perp \vec{b_{2}}, \vec{a_{2}}\perp \vec{b_{1}}$ logo $\vec{b_{1}}\perp\vec{b_{2}}$. Assim:
$$\vec{b_{1}}=\frac{2\pi}{a_{1}}\hat{i}~~;~~ \vec{b_{2}}= \frac{2\pi}{a_{2}}\vec{j}$$
![[rede retangular e reciproca]]
- Por alguma razão temos que ter $\vec{a_{3}}=\vec{b_{3}}=\vec{0}$, mas não apanhei.

**EXEMPLO 2 : Rede 2D rodada**
![[rede retangular e reciproca - inclinada]]
- Consideremos a rede 2D definida por:
$$\vec{a_{1}}=\frac{a}{2}\hat{i}+ \frac{a}{2}\hat{j} \quad \quad;\quad \quad \vec{a_{2}}=\frac{a}{2}\hat{i}- \frac{a}{2}\hat{j}$$
- Ora, queremos determinar:
$$\vec{b_{1}}= b_{1x}\hat{i}+ b_{1y}\hat{j} \quad \quad;\quad \quad \vec{b_{2}}= b_{2x}\hat{i}+ b_{2y}\hat{j}$$
- Tendo em conta que $\vec{a_{1}}\cdot\vec{b_{1}}=\vec{a_{2}}\cdot\vec{b_{2}}=2\pi~,~\vec{a_{1}}\cdot\vec{b_{2}}=\vec{a_{2}}\cdot\vec{b_{1}}=0$Podemos obter:
$$\vec{b_{1}}=- \frac{2\pi}{a}\hat{i} - \frac{2\pi}{a} \hat{j} \quad \quad;\quad \quad \vec{b_{2}}= - \frac{2\pi}{a} \hat{j} + \frac{2\pi}{a}\hat{j}$$

NOTA: pode parecer que temos sinais errados porque $\vec{a_{1}}\cdot\vec{b_{1}}=-2\pi$ mas recordemos que a fórmula é $\vec{a_{i}}\cdot\vec{b_{i}}=2\pi n$. Ora, nada dos impede de escolher $n=-1$. :D

Vemos que:
- A rede *recíproca de __retangular__ é __retangular__* 

## FCC/BCC
- Consideremos uma rede cúbica FCC. Podemos definir:
$$\vec{a_{1}}=\frac{a}{2}(\hat{j}+\hat{k})~~,~~\vec{a_{2}}=\frac{a}{2}(\hat{i}+\hat{k})~~,~~\vec{a_{3}}=\frac{a}{2}(\hat{i}+\hat{j})$$
![[fcc vetores.png|345]]
(na figura, $a=\vec{a_{3}}~,~b=\vec{a_{1}}~,~c=\vec{a_{2}}$)

em que $a$ é o comprimento da aresta da célula convencional. Os pontos são os pontos da rede. Ou seja, $\vec{a_{1}},\vec{a_{2}},\vec{a_{3}}$ chegam de um vértice ao centro das faces tangentes.
- Ora, vemos logo que os vetores $\vec{a_{i}}$ *não* definem a célula convencional FCC.

*Nota sobre redes*
- Temos que a célula convencional tem 4 pontos: os pontos dos vétices valem $\frac{1}{4}$ e os pontos do centro das faces vale $\frac{1}{2}$ (porque são partilhados). 
- A célula primitiva contém 1 ponto -- Sempre! O volume da célula pode mudar, mas ela tem sempre 1 só ponto.
- Assim, a célula convencional é 4 vezes maior do que a primitiva.

*Rede Recíproca*
- Usando as equações 3D de $\vec{b_{i}}$ obtem-se:
$$\vec{b_{1}}=\frac{2\pi}{a}(-\hat{i}+\hat{j}+\hat{k})~~,~~\vec{b_{2}}=\frac{2\pi}{a}(\hat{i}-\hat{j}+\hat{k})~~,~~\vec{b_{3}}=\frac{2\pi}{a}(\hat{i}+\hat{j}-\hat{k})$$
Isto **não** é uma FCC.

Vemos que:
- Invés disso, temos que *a recíproca de uma __FCC__ é uma __BCC__* 
- Naturalmente, *a recíproca de uma __BCC__ é uma __FCC__*
- De forma mais geral, *a recíproca de uma __rede de Bravais__ é uma __Rede de Bravais__*!!

## Hexagonal
![[rede hexagonal e reciproca]]
- Podemos definir os vetor $\vec{a_{1}},\vec{a_{2}}$ acima e vemos que uma possível célula primitiva é o losango desenhado.
- Ora, vemos pelos vetores da rede recíproca que:
    - A *recíproca de uma __Hexagonal plana__ é uma __Hexagonal plana rodada de 30º__*!
![[rede reciproca hex.png|425]]

## Planos de Rede
- Tendo-se uma rede $\vec{R}$, um *plano da rede* é um plano que contém pelo menos 3 pontos não colineares da rede.
- Uma *família de planos da rede* é um conjunto de planos paralelos. Uma família de planos contém todos os pontos da rede. Pode ser definida pelo vetor normal aos planos.

## Índices de Miller
- São uma forma útil de representar vetores da rede recíproca $\vec{K}$ (ou planos da rede real correspondentes). 
- Temos uma rede definida por vetores $\vec{a_{i}}$ com a rede recíproca $\vec{b_{i}}$ tal que $\vec{a_{i}}\cdot\vec{b_{j}}=2\pi\delta_{ij}$
- Tendo-se um vetor dado por: $$\vec{K}=h \vec{b}_{1} + k \vec{b}_{2}+l \vec{b}_{3}$$
escrevemos os *índices de Miller* como $(hkl)$ ou $(h,k,l)$.
- Se $\vec{a}_{i}$ definir uma célula primitiva do espaço real, para representar um plano do espaço real devemos usar $(hkl)$ de modo que estes não tenham divisores comuns. Isto porque $\vec{b}_{i}$ serão os vetores da rede recíproca primitiva.
- Para redes cúbicas (simples, FCC, BCC) escolhemos $\vec{a}_{i}$ a ser $a\hat{x},a\hat{y},a\hat{z}$. Neste caso temos $\vec{b}_{i}$ a ser $\frac{2\pi}{a}\hat{x},\frac{2\pi}{a}\hat{y},\frac{2\pi}{a}\hat{z}$. Apenas na cúbica simples teremos $\vec{b}_{i}$ a serem vetores da rede recíproca primitiva.

- Podemos então ver os planos $(010)$ para a rede cúbica:
![[familia planos 010.png]]
Vemos que os planos iriam intersetar todos os vértices do cubo. Mas se a rede for BCC teremos alguns pontos que não são incluidos nestes planos

- Por outro lado, os planos $(020)$ já incluem todos os pontos:
![[familia planos 020.png]]

- Podemos definir a distância entre planos da família:
$$d_{(hkl)}=\frac{2\pi}{|\vec{K}|}$$
que, para redes cúbicas dá:
$$d_{(hkl)}=\frac{a}{\sqrt{h^{2}+k^{2}+l^{2}}}$$
e daqui já entendemos porquê que $(020)$ inclui mais pontos que $(010)$: os planos estão menos espaçados!

- Podemos encontrar os índices de Miller de uma família de planos encontrando as suas interseções do plano mais proximo da origem com os eixos, que ocorrem nos pontos: $x_{1},x_{2},x_{3}$. Temos então a relação de *ratios*:
$$\frac{1}{x_{1}}: \frac{1}{x_{2}}: \frac{1}{x_{3}}=h:k:l$$
em que isto implica:
$$\frac{1}{x_{1}}=hA ~~;~~\frac{1}{x_{2}}=kA ~~;~~ \frac{1}{x_{3}}=lA~~~~\to~~~~ x_{1}h=x_{2}k=x_{3}l $$
- Por exemplo, se $x_{1}=2,x_{2}=2,x_{3}=3$, então temos: $h=3,h=3,l=2$ ou seja temos a família de planos $(332)$. Isto porque estes são os menores inteiros com que conseguimos satisfazer esta equação. 

**Escolha de Célula**
- Os vetores $\vec{a}_{i},\vec{b}_{i}$ não são necessariamente os vetores primitivos das redes real e recíproca, porque podemos trabalhar com qualquer célula unitária. Assim:
    - Se escolhermos uma célula *primitiva* então o menor vetor da rede recíproca com uma certa direção será aquele em que $h,k,l$ não têm divisores em comum. Se houverem divisores comuns, dividimos os índices pelos divisores comuns e os resultados definem o menor vetor da rede reciproca.
    - Se tivermos uma célula *não primitiva*, então nem todos os tripletos $hkl$ são vetores da rede recíproca. Independentemente, podemos sempre escrever $\vec{K}$ com combinações lineares de coeficientes inteiros de $\vec{b}_{i}$. 

## Zonas de Brillouin
- Definimos a rede de Bravais como sendo exatamente igual se nos deslocarmos $\vec{R}$ para o lado. Ora, isto é igual no espaço recíproco: uma onda a mover-se no cristal será igual se fizermos a transição $\vec{k}\to\vec{k}+\vec{K}$
- Assim, a grandeza física que aqui importa é o *momento*: $\hbar k$.

- Ou seja, podemos considerar uma zona de Brillouin como contendo todos os momentos possíveis exatamente 1 vez:
    - Numa zona temos $k$, logo o momento $\hbar k$. Ora, só voltamos a ter o momento em $k+K$. Assim, por definição, isso já fará parte da próxima zona de Brillouin!

- Uma *definição* é:
    - Definimos a ZB1 como o grupo de pontos em que $\vec{K}=\vec{0}$ está mais próximo que qualquer outro ponto da rede recíproca. A ZB2 é o conjunto de pontos em que $\vec{K}=\vec{0}$ é o 2º ponto da rede mais próximo. Por aí fora. Em 2D, isto resulta em algo assim:
![[zonas brillouin.png|400]]

- Notas:
    - Zonas de Brillouin 2+ são compostas de regiões separadas (apenas ZB1 é uma só região unida)
    - Pontos nas fronteiras de ZBs estão na bissetriz entre $\vec{0}$ e um certo ponto $\vec{K}$
    - Todas as zonas de Brillouin têm o mesmo comprimento/área/volume total (para 1D,2D,3D)
