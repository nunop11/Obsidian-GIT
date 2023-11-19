- Como já vimos:
$$F[x(t)]=\int_{-\infty}^{+\infty} x(t)e^{-j\omega t}dt=X(j\omega)$$
ou seja, projetamos o sinal sobre uma oscilação exponencial complexa de *amplitude constante* (diferença em relação a Laplace). De seguida somamos todas as projeções.
- Vimos ainda que a transformada de Fourier é apenas a limitação da Transformada de Laplace à parte imaginária, de modo que $F[x(t)]=L[x(t)]_{s=j\omega}$. Assim, se a RC da transformada de Laplace não contem o eixo imaginário, então não temos transformada de Fourier.
- Vejamos agora exemplos.

## Delta Dirac
$$F[\delta(t)]=1 \quad \quad;\quad \quad F[\delta(t-\tau)]=e^{-j\omega\tau}$$

## Função Retangular
![[função retangulo.png]]
Esta função pode ser definida por:
$$ret(t)=\begin{cases}1 &; &|t|\le \frac{1}{2}\\ 0 &;  &|t|>\frac{1}{2}\end{cases}$$
- Esta função tem *altura, largura e área unitárias*.
- Se determinarmos o Fourier:
$$F[ret(t)]=\int_{-\infty}^{+\infty}ret(t)e^{-j\omega t}dt=\int_{-1/2}^{+1/2} e^{-j\omega t}dt = \frac{\sin\left(\frac{\omega}{2} \right)}{\frac{\omega}{2}}=\text{senc}(\omega/2)$$
sendo que "senc" é o *seno cardinal*.
- Acerca do seno cardinal, de notar:
    - $\lim_{t\to0}\text{senc}(t)=1$
    - $\int_{-\infty}^{+\infty}\text{senc}(x)dx=\pi$

- Podemos ainda verificar que
$$F[ret(at)]=\frac{1}{|a|} \text{senc} \left( \frac{\omega}{2a} \right)$$

### Exponencial Complexa
$$F[e^{j\omega_{0}t}]=\int_{-\infty}^{+\infty}e^{j\omega_{0}t} e^{-j\omega t}dt=\int_{-\infty}^{+\infty}e^{j(\omega_{0}-\omega)t}dt$$
Ora, se $\omega_{0}\ne \omega$ então $F[e^{j\omega t}]=0$
Se $\omega_{0}=0$ então $F[e^{j\omega t}]=+\infty$

### Função $1/t$
$$F \left[ \frac{1}{t} \right] = -j\pi \text{sign}(\omega)$$
A dedução é chata e envolve o método de Cauchy por causa da descontinuidade em $t=0$, pelo que nao a passei. Está no slide 18 da aula 17.
- A função "sign" (sigma) define-se como:
$$\text{sign}(x)=\begin{cases}1 &; &x>0\\ 0 &; &x=0\\ -1 &; &x<0\end{cases}$$
- De notar ainda que podemos definir $u(t)=\frac{1}{2}+ \frac{1}{2} \text{sign}(t)$

# Propriedades
- Em geral, tanto $x(t)$ como $X(j\omega)$ têm parte real e imaginária. Ora, usando isso e decompondo ambos na sua parte par e ímpar temos:
![[decomposicao sinal fourier.png]]

- **Linearidade** - $F[af(t)+bg(t)]=aF[f(t)]+bF[g(t)]$
- **Dualidade** - As expressões da Tranformada de Fourier e da Transformada de Fourier Inversa são muito semelhantes (veremos na próxima aula). Disto resulta: $$F[f_{1}(t)]=f_{2}(\omega)\to F[f_{2}(t)]=2\pi f_{1}(-\omega)$$
    - Um exemplo:
        - Tendo $f_{1}(t)=ret(t)$, a sua transformada é $F[f_{1}(t)]=f_{2}(j\omega)=\text{sinc} \left( \frac{\omega}{2}\right)$
        - Podemos diretamente converter isto numa função de tempo: $f_{2}(t)=\text{sinc} \left( \frac{t}{2} \right)$
        - Podemos fazer a transformada de $f_{2}$: $F[f_{2}(t)]=2\pi ret(-\omega)=2\pi f_{1}(-\omega)$
- **Mudança de Escala** - Temos: $F[x(t)]=X[j\omega]\to F[x(at)]=\frac{1}{|a|} X \left( j \frac{\omega}{a} \right)$
- **Teorema da Convolução** - Tendo-se a resposta impulsional de um sistema, $h(t)$, e $H(j\omega)=F[h(t)]$ temos: $$y(t)=x(t)*h(t)\to Y(j\omega)=X(j\omega)H(j\omega)$$
- **Teorema da Multiplicação** - Tendo-se $y(t)=f(t)g(t)$ então $$Y(j\omega)=\frac{1}{2\pi} F(j\omega)*G(j\omega)$$
- **Teorema do Deslocamento** - $F[x(t-\tau)]=e^{-j\omega \tau}X(j\omega)$
- **Teorema da Modulação** - $F[e^{j\omega_{0}t}x(t)]=X[j(\omega-\omega_{0})]$
- **Teorema da Derivação** - Recordando que $\frac{dx}{dt}=x(t)* \frac{d\delta}{dt}$ temos que $$F \left[ \frac{d^{n}x(t)}{dt^{n}} \right]=(j\omega)^{n} X(j\omega)$$
    - Inversamente, temos: $$F[-jt x(t)]= \frac{dX(j\omega)}{d\omega}$$
- **Teorema da Integração** - Recordando que $\int_{-\infty}^{t}x(\tau)d\tau=x(t)*u(t)$ temos $$F \left[ \int_{-\infty}^{t} x(\tau)d\tau \right]=\frac{1}{j\omega} X(j\omega) + \pi X(0) \delta(\omega)$$
- *Transformada da func Degrau* - $F[u(t)]=\pi\delta(\omega)+ \frac{1}{j\omega}$
- **Teorema de Parseval** - Usando o teoremas da convolução e da multiplicação é possível obter: $$\int_{-\infty}^{+\infty} f(t)*g(t) dt = \frac{1}{2\pi} \int_{-\infty}^{+\infty} F(j \upsilon)G^{*}(j\upsilon)d\upsilon$$
    - O que, quando $g(t)=f(t)$ nos dá $\int_{-\infty}^{+\infty}|f(t)|^{2}dt=\frac{1}{2\pi} \int_{-\infty}^{+\infty}|F(j\omega)|^{2}d\omega$

#sinais #fisica #fourier 
