- Vimos na aula anterior que tendo um sinal $x(t)=e^{st}$, então $x(t)$ é uma função própria de um SLIT.
    - No entanto, na vida real muito raramente temos sinais de entrada que são exatamente exponenciais complexas.
- Como vimos também na aula anterior, a resposta de um SLIT  a um sinal exponencial complexa é fácil de determinar. Assim, seria muito útil representar  um sinal qualquer em função de exponenciais complexas. Para isso usamos *Transformadas de Laplace*.

$$L[x(t)]=X(s)=\int_{-\infty}^{+\infty} x(t)e^{-st}dt$$
- Na prática, estamos a "projetar" o sinal de entrada $x(t)$ em cada instante numa exponencial complexa $e^{-st}$.

> **_EXEMPLO 1_**
> - Vejamos a transformada de laplace: $$x(t)=e^{-\alpha t}u(t)~~,~~\alpha>0$$
> $$\begin{align*}
X(s)&= \int_{-\infty}^{+\infty}x(t)e^{-st}dt=\int_{0}^{+\infty} e^{-(s+\alpha)t}dt=- \frac{1}{s+\alpha}e^{-(s+\alpha)t}\bigg|_{0}^{+\infty}\\
&= - \frac{1}{s+\alpha} \left[ e^{-(\sigma+\alpha+j\omega)\cdot\infty}-e^{0} \right]=- \frac{1}{s+\alpha} \left[ e^{-(\sigma+\alpha)\cdot\infty}e^{-j\omega \cdot\infty}-e^{0} \right]\\
\end{align*}$$
> Como $\sigma+\alpha>0$, ficamos com $$X(s)=\frac{1}{s+\alpha} ~~;~~\sigma= \text{Re}(s)>-\alpha$$
> - De notar que, caso tivéssemos $x(t)=-e^{-\alpha t}u(-t)$ teríamos $\text{Re}(s)<-a$, mas a expressão da transformada de Laplace seria exatamente a mesma.

- Ora, nestes casos temos a mesma expressão, mas as funções de entrada são completamente diferentes. Ora, é também muito importante saber a *Região de convergência* (**RC**) do integral, ou seja, a zona do plano complexo $s$ em que a transformada se aplica. No primeiro caso era $\text{Re}(s)>-\alpha$, no segundo era $\text{Re}(s)<-\alpha$.

> **_EXEMPLO 2_**
> - Vejamos um exemplo de uma função de entrada composta por 2 exponenciais: $x(t)=e^{-t}u(t)+e^{-2t}u(t)$. A transformada de $x(t)$ será apenas a soma das transformadas das 2 partes: $$L[x(t)]=L[e^{-t}u(t)]+L[e^{-2t}u(t)]$$
> - Temos:
> ![[laplace exs.png]]
> Ou seja, a região de convergência de $x(t)$ é  **interseção das 2 RC** das suas componentes.

- Vemos que, de um modo geral, $X(s)$ fica com o formato $N(s)/D(s)$ sendo $N,D$ dois polinómios (do numerador e denominador, respetivamente). As raízes de $N$ dãp os **zeros** de $X$ e as de $D$ dão os **polos** (pontos em que a função se torna indefenida).
- Se $x(t)$ é real, então as raízes de $N,D$ serão reais e/ou 2 complexos conjugados.

> __*EXEMPLO 3*__
> - Vejamos agora um exemplo com o Delta de Dirac: $x(t)=2\delta(t)- \frac{34}{7}e^{-3t}u(t)+ \frac{20}{7} e^{4t}u(t)$. Temos:
>     - $L[2\delta(t)]=2$, em que a região de convergência é todo o plano $s$
>     - $L[- \frac{34}{7}e^{-3t}u(t)]=\frac{-34}{7} \frac{1}{s+3} ~~;~~ \text{Re[s]>-3}$
>     - $L[- \frac{20}{7}e^{4t}u(t)]=\frac{20}{7} \frac{1}{s-4} ~~;~~ \text{Re[s]>4}$
> - Ficamos com $$X(s)=2- \frac{34}{7} \frac{1}{s+3} + \frac{20}{7} \frac{1}{s-4} = \frac{2s^{2}-4s+4}{s^{2}-s-12}~~;~~ \text{Re}[s]>4$$
> - $x(t)$ é real. E verificamos que as raízes de $N$ são 2 complexos conjugados e as de $D$ são reais.

## Propriedades de RC
- As RC serão sempre **faixas** verticais, paralelas ao eixo imaginário. (porque a convergencia do integral apenas depende de $\sigma$ como vimos acima)
- Se $x(t)$ é um sinal com duração **finita**, então o RC será todo o plano complexo $s$.
- **Sinal Direito** - Se $x(t)$ for não nulo apenas em $t\ge T_{0}$, e se $\text{Re}[s]=\sigma_{0}$ pertencer à RC, então a RC será $\text{Re}[s]\ge \sigma_{0}$.
- **Sinal Esquerdo** - Se $x(t)$ for não nulo apenas em $t\le T_{0}$, e se $\text{Re}[s]=\sigma_{0}$ pertencer à RC, então a RC será $\text{Re}[s]\le \sigma_{0}$.
- **Sinal Bilateral** - Se $x(t)$ se estende de $-\infty$ a $+\infty$, então a RC será a reta $\text{Re}[s]=\sigma_{0}$.
- Devido à RC ser a interseção das RCs das componentes de $x(t)$:
    - Num *sinal direito*, a RC é o semiplano à direita da reta com abcissa igual ao *polo com maior parte real* (não módulo).
    - Num *sinal esquerdo*, a RC é o semiplano à esquerda da reta com abcissa igual ao *polo com menor parte real* (não módulo).

# Laplace Inversa
$$x(t)= \frac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty} X(s)e^{st}ds$$
- No entanto, como envolve cálculo complexo não iremos usar este método.

# Frações Parciais
- Como vimos em alguns dos exemplos acima, $X(s)$ é uma função racional (um polinómio a dividir por outro). Como tal, podemos representar $X(s)$ como uma soma de frações mais simples. Depois iremos determinar a transformada inversa dessas frações simples.
- Ou seja, o método é:
    1. Expandir $X(s)$ em frações simples
    2. Identificar o RC da cada fração
    3. Determinar a transformada inversa de cada fração

- Tendo a seguinte fração genérica:
$$X(s) = \frac{a_ns^n + a_{n-1}s^{n-1} + \cdots + a_1s + a_0}{b_ms^m + b_{m-1}s^{m-1} + \cdots + b_1s + b_0}$$
- Começamos por determinar os *polos* de $X(s)$ e fatorizar $D(s)$. Ficamos com:
$$X(s) = \frac{a_ns^n + a_{n-1}s^{n-1} + \cdots + a_1s + a_0}{b_m(s - p_1)(s - p_2)\cdots(s - p_m)}$$
- Temos 2 casos: *Polos simples* (todos os polos são diferentes) e *Polos múltiplos* (temos pelo menos 2 polos iguais: $p_{i}=p_{j}$ para algum $i\neq j$)
### Polos Simples
- É mais fácil decompor $X(s)$, ficando-se com:
$$X(s) = \frac{c_1}{s-p_1} + \frac{c_2}{s-p_2} + \cdots + \frac{c_m}{s - p_m}$$
- De notar que os coeficientes $c_{i}$ se chamam *resíduos*, sendo que:
$$\begin{align*} c_i &= \left[(s-p_i)X(s)\right]_{s=p_i} = \\ &= \left.\frac{a_ns^n + a_{n-1}s^{n-1} + \cdots + a_1s + a_0}{b_m(s - p_1)\cdots(s-p_{i-1})(s-p_{i+1})\cdots(s - p_m)}\right\vert_{s=p_i} \end{align*}$$

### Polos Múltiplos
- Consideremos que temos um certo polo $p_{i}$ repetido $r$ vezes. Sendo $c_{i2}$ o resíduo correspondente à 3ª repetição de $p_{i}$, temos:
$$X(s) = \frac{c_1}{s-p_1} + \cdots + \frac{c_{i1}}{s-p_i}+ \frac{c_{i2}}{(s-p_i)^2} + \cdots + \frac{c_{ir}}{(s-p_i)^r}+ \cdots + \frac{c_m}{s - p_m}$$
- Ou seja, para as frações correspondentes ao polo repetido $r$ vezes temos uma série de potências. Os resíduos são dados por:
$$\begin{align*} c_{ir} &= [(s-p_i)^rX(s)]_{s=p_i} \\ c_{i(r-1)} &= \frac{d}{ds}[(s-p_i)^rX(s)]_{s=p_i} \\ \vdots \\ c_{i(r-k)} &= \frac1{k!}\frac{d^k}{ds^k}[(s-p_i)^rX(s)]_{s=p_i} \\ \vdots \\ c_{i1} &= \frac1{(r-1)!}\frac{d^{r-1}}{ds^{r-1}}[(s-p_i)^rX(s)]_{s=p_i} \end{align*}$$
>__*EX:*__
>$$X(s)= \frac{2s^{2}+3s+3}{(s+3)^{3}(s+1)}$$
>- O polo $s=-3$ tem multiplicidade $r_{1}=3$
>- Ou seja:
>$$X(s)= \frac{c_{11}}{s+3} + \frac{c_{12}}{(s+3)^{2}}+\frac{c_{13}}{(s+3)^{3}}+ \frac{c_{2}}{s+1}$$
>- Determinemos os resíduos:
>$$\begin{align*}
c_{13}&= (s+3)^{3}X(s)|_{s=-3} = \frac{2s^{2}+3s+2}{s+1}|_{s=-3}=-6\\
c_{12}&= \frac{d}{ds}[(s+3)^{3}X(s)]_{s=-3}=\frac{2s(s+2)}{(s+1)^{2}}\Biggr|_{s=-3}= \frac{3}{2}\\
c_{13}&= \frac{1}{2 \cdot 1} \frac{d^{2}}{ds^{2}}[(s+3)^{3}X(s)]_{s=-3} = \frac{1}{2} \frac{d}{ds} \left[ \frac{2s(s+2)}{(s+1)^{2}} \right]_{s=-3} = \frac{2}{(s+1)^{3}}\Biggr|_{s=-3}= \frac{-1}{4}\\
c_{2}&= (s+1)X(s)|_{s=-1}= \frac{2s^{2}+3s+3}{(s+3)^{3}}\Biggr|_{s=-1}= \frac{1}{4}
\end{align*}$$
>- E ficamos com: $$X(s)=\frac{-1}{4} \frac{1}{s+3} + \frac{3}{2} \frac{1}{(s+3)^{2}} -6 \frac{1}{(s+3)^{3}} + \frac{1}{4} \frac{1}{s+1}$$

- Isto é portanto o método de *frações parciais*. Assim, é importante notar que se $N(s),D(s)$ forem polinómios do mesmo grau, então é preciso decompor o polinómio do numerador de forma a ficar com um valor + uma fração que $N$ tem um grau menor (basicamente dividir polinómios). Um exemplo:
![[laplace fracoes parciais.png]]

- Vejamos agora como faríamos para aplicar o que falamos atrás de fazer a transformada inversa de cada fração:
>__*EX:*__
>Consideremos que temos: $$X(s)=\frac{2s}{(s+1)(s+3)}= \frac{-1}{s+1} + \frac{3}{s+3} ~~;~~ \text{Re[s]>-1}$$
>Temos então $$\begin{align*}
X_{1}(s)&= - \frac{1}{s+1}~~;~~ \text{Re}[s]>-1\\
X_{2}(s)&= \frac{3}{s+3}~~;~~ \text{Re}[s]>-3
\end{align*}$$
> Assim, como estas frações são muito simples, apenas temos que comparar estas frações como que obtivemos nos exemplos acima em que determinamos as transformadas. Temos: $$X_{1}(s)\to x_{1}(t)=-e^{-t}u(t) \quad;\quad X_{2}(s)\to x_{2}(t)=3e^{-3t}u(t)$$
> Assim, como a RC do sinal $X(s)$ é $\text{Re}[s]>-1$, então temos um sinal *direito* definido por: $$x(t)=-e^{-t}u(t) + 3e^{-3t}u(t)$$

#sinais #fisica #laplace