## Rede Recíproca
- Nas últimas aulas vimos que um vetor de rede pode ser definido por $\vec{R_{n}}=\sum_{i=1}^{3}n_{i}\vec{a_{i}}$ 
- Tendo um vetor $\vec{a}$ de uma rede de Bravais, a rede recíproca será $\vec{b}$, em que
$$\vec{b}_{i}\cdot\vec{a}_{j}=2\pi n \delta_{ij}$$
logo $\vec{a}_{i}\parallel \vec{b}_{i}~~;~~ \vec{a}_{i}\perp\vec{b}_{j}~,~i\neq j$
- O facto de $n$ poder ser um qualquer inteiro permite "inverter" e "esticar" os vetores da rede recíproca obtida. Isto deve-se às caraterísticas de simetria das redes de Bravais.

## 1D
**Rede 1D**
- Consideremos uma rede 1D na direção x, com pontos distanciados de $a$. Teremos $\vec{a}=a\hat{i}$.
- Neste caso teríamos que a rede recíproca é definida por $\vec{b}=\frac{2\pi}{a}\hat{i}$. 
- Ou seja, para uma rede linear, a rede recíproca também é linear.

**Fourier**
- Podemos escrever $f(x)=\sum_{n=-\infty}^{+\infty}\delta(x-na)$
- Logo: $$\begin{align*}
f(k)&= \int_{-\infty}^{+\infty}f(x)e^{-ikx}dx\\
&= \int_{-\infty}^{+\infty}\sum\limits_{n=-\infty}^{+\infty}\delta(x-na)e^{-ikx}dx\\
&= \sum\limits_{n=-\infty}^{+\infty}\int_{-\infty}^{+\infty}\delta(x-na)e^{-ikx}dx\\
&= \sum\limits_{n=-\infty}^{+\infty} e^{ikna}
\end{align*}$$

**Continhas Giras**
- Podemos definir $$\begin{align*}
S&= \sum\limits_{\ell=0}^{N-1}e^{i \ell aq}\\
e^{iaq}S&= \sum\limits_{\ell=0}^{N-1}e^{i\ell aq}e^{iaq}\\
&= \sum\limits_{\ell=0}^{N-1} e^{i(\ell+1)aq}
\end{align*}$$
temos $$\sum\limits_{\ell=0}^{N}e^{iaq\ell}=\sum\limits_{\ell=0}^{N-1}e^{iaq\ell}-1+e^{iNaq}=S-1+e^{iNaq}$$
logo a equação de $S$ fica:
$$\begin{align*}
e^{iaq}S&= S-1+e^{iNaq}\\
S&= \frac{e^{iNaq}-1}{e^{iaq}-1}=\frac{e^{i \frac{N}{2}aq}}{e^{i \frac{aq}{2}}}\frac{\sin\left(\frac{Naq}{2}\right)}{\sin\left(\frac{aq}{2}\right)} 
\end{align*}$$
... transição por entender ...
$$S=\sum\limits_{\ell'}N \frac{2\pi}{L} \delta\left(q-2\pi \frac{\ell'}{a}\right)$$
- Ora, recordemos que isto corresponde à transformada de Fourier da rede $\vec{a}$. 
- Podemos ainda ver que isto define as relações $\vec{a_{i}}\cdot b_{j}$ vistas acima, ou seja, a *transformada de Fourier da rede real* é a **Rede Recíproca**! Assim, usando FT e IFT podemos obter a rede real da rede recíproca e vice-versa.

**Caso Geral : 3D**
- Consideremos uma rede descrita pelos vetores $\vec{a_{1}},\vec{a_{2}},\vec{a_{3}}$. Temos:
$$\begin{align*}
\vec{b_{1}}&= 2\pi\frac{\vec{a_{2}}\times\vec{a_{3}}}{|\vec{a_{1}}\cdot(\vec{a_{2}}\times\vec{a_{3}})|}= \frac{2\pi}{V} (\vec{a_{2}}\times\vec{a_{3}})\\
\vec{b_{2}}&= \frac{2\pi}{V} (\vec{a_{3}}\times\vec{a_{1}})\\
\vec{b_{3}}&= \frac{2\pi}{V} (\vec{a_{1}}\times\vec{a_{2}})
\end{align*}$$
isto consiste em rodar os índices: $123, 231, 312$.

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
![[rede reciproca hex.png|500]]

## Raios X
- O espetro de emissão $E(\lambda)$ apresenta um traçado suave com picos no meio. Vimos em FModerna a explicação. 
    - Recordemos que os picos se devem a eletrões a descer para níveis menos energéticos e à consequente libertação de energia.
    - Na prática, usam-se filtros, de forma a isolar o *pico mais intenso*. Desta forma, ficamos com um feixe praticamente monocromático. 
        - Isto é bom, mas pode causar complicações se esse comprimento de onda for absorvido pela nossa amostra.

**Difração em estruturas de Bravais - BRAGG**
- Consideremos:
![[difracao bragg.png|600]]
- Ora, assume-se que as redes são "bons espelhos", tendo-se uma reflexão a manter o ângulo de incidência. 
- Assim, temos a diferença nos percurss percorridos:
$$\Delta s= 2d\sin\theta$$

- Mas estamos na *teoria de Bragg*, que introduziu neste caso muito simples algo: temos que ter *interferências construtivas* (que explicam os picos do espetro de emissão). Asism, a diferença de comprimento entre os percursos terá que ser uma *quantidade inteira de comprimentos de onda*:
$$2d\sin\theta=m\lambda~~~~,~~m\in\mathbb{Z}$$


- Vimos em Ótica (sqn lol) que o padrão de difração corresponde à *transformada de Fourier* do objeto que original essa difração. OU SEJA: quando um feixe é difratado por uma rede de Bravais, o padrão de difração é a *rede recíproca*. -- Teoria de Von Laue, a ver na próxima aula.