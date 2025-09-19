# 1 - Séries de Fourier
- Qualquer função periódica definida num intervalo $0\le x<L$ pode ser escrita como uma série de Fourier.
- Se a função for par/simétrica em relação ao ponto central do intervalo $x=\frac{1}{2}L$, usamos cosseno: $$f(x)=\sum\limits_{k=0}^{\infty} \alpha_{k}\cos  \left( \frac{2\pi kx}{L} \right)$$
em que $\alpha_{k}$ é um conjunto de constantes que definem a forma da equação.
- Se a função for ímpar/anti-simétrica (rotação 180º) em relação ao ponto médio, usamos seno:
$$f(x)=\sum\limits_{k=1}^{\infty} \beta_{k}\sin \left( \frac{2\pi kx}{L} \right)$$
- Assim, para uma forma que não apresenta qualquer simetria:
$$f(x)= \sum\limits_{k=0}^{\infty} \alpha_{k}\cos  \left( \frac{2\pi kx}{L} \right) + \sum\limits_{k=1}^{\infty} \beta_{k}\sin \left( \frac{2\pi kx}{L} \right)$$
- Podemos usar $\cos\theta=\frac{1}{2}(e^{-i\theta} + e^{i\theta})$, $\sin\theta=\frac{1}{2}(e^{-i\theta} - e^{i\theta})$ e temos:
$$f(x)=\frac{1}{2}\sum\limits_{k=0}^{\infty}\alpha_{k} \left[e^{-i \frac{2\pi kx}{L}} + e^{i \frac{2\pi kx}{L}} \right] + \frac{1}{2}\sum\limits_{k=0}^{\infty}\beta_{k} \left[e^{-i \frac{2\pi kx}{L}} - e^{i \frac{2\pi kx}{L}} \right]$$
e temos:
$$f(x)=\sum\limits_{k=-\infty}^{+\infty}\gamma_{k} e^{i \frac{2\pi}{L}kx} \quad \textsf{(Eq.0)} \quad;\quad \quad \gamma_{k} = \begin{cases} \frac{1}{2}(\alpha_{-k}+i\beta_{-k}) &; &k<0\\ \alpha_{0} &; &k=0\\ \frac{1}{2}(\alpha_{k}-i\beta_{k}) &; &k>0\end{cases}$$

![[forçar periodica.png]]
- Assim, apesar de estas séries se aplicarem a funções periódicas, podemos usá-las em funções não periódicas. Na prática, é como se considerassemos uma função que repete a função $f$ no intervalo muitas vezes, e iremos obter uma boa aproximação. No entanto, de notar que se usarmos a função obtida fora deste intervalo ela irá dar resultados errados.

- Os coeficientes $\gamma_{k}$, são normalmente complexos. Para os obter:
$$\int_{0}^{L} f(x)\exp\left( -i \frac{2\pi kx}{L}\right)dx = \sum\limits_{k'=-\infty}^{+\infty} \gamma_{k'} \int_{0}^{L}\exp \left( i \frac{2\pi(k'-k)x}{L} \right)dx \quad \quad \textsf{(Eq. 1)}$$
- Na integral da direita temos:
$$\begin{align*}
\int_{0}^{L}\exp \left( i \frac{2\pi(k'-k)x}{L} \right)dx &= \frac{L}{2i\pi(k'-k)}\left[ \exp \left(i \frac{2\pi (k'-k)x}{L} \right) \right]_{0}^{L}\\
&= \frac{L}{2i\pi (k'-k)} \left[ \cancelto{=1}{e^{i 2\pi(k'-k)}} - 1 \right]\\
&= 0
\end{align*}$$
(isto porque $e^{i2\pi n}=1, \forall n\in \mathbb{Z}$).

- No entanto, se $k'=k$ vemos que $\int_{0}^{L}\exp \left( i \frac{2\pi(k'-k)x}{L} \right)dx=\int_{0}^{L}dx=L$ . Assim, regressando à Eq.1:
$$\int_{0}^{L}f(x) e^{-i \frac{2\pi kx}{L}}dx=L\gamma_{k}$$
ou seja:
$$\gamma_{k}=\frac{1}{L} \int_{0}^{L}f(x)\exp \left(-i \frac{2\pi kx}{L} \right)dx$$
- Assim, podemos obter a função usando os coeficientes de Fourier (Eq.0) ou obter os coeficientes usando a função (Eq.1).

#computacional #programacao #fourier
