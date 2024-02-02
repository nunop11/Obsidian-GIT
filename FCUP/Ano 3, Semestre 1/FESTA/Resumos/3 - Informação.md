- Temos uma mensagem com $N\in\mathbb{N}$ termos, em que para cada um temos $M\in\mathbb{N}$ valores possíveis. Sendo $p(x_{i})$ a probabilidade de escolher cada um dos elementos dos $M$ possíveis, temos que a informação associada a esta mensagem é:
$$I=\sum\limits_{i=1}^{N}(-\log_{b}p(x_{i})$$
e no caso em que todas as $M$ opções têma mesma probabilidade:
$$I=N\log_{b}M$$
($I=\sum^{N}_{i=1}(-\log_{2} \frac{1}{M})=\sum_{i=1}^{N}\log_{2}M=N\log_{2}M$)

## 3.1 - Informação no limite termodinâmico
- Este é o caso em que $N\to\infty$.
- O número de vezes que vemos o carater $m_{i}$ (de probabilidade $p_{i}$) é aproximadamente: $N_{i}=p_{i}N$. 
    - Podemos entender isto assim: $N_{i}$ é uma variável extensiva. Tal como fizemos no resumo anterior, podemos definir uma variável intensiva: $x=N_{i}/N$. Podemos então fazer um histograma de $x$. Pelo teorema do limite central, se $N$ for muito elevado, temos que este histograma segue uma distribuição normal em torno de $p_{i}$. Ora, teremos $\sigma^{2}\sim\sqrt{N}$ pelo que podemos assumir que as flutuações serão desprezáveis e $N_{i}/N\sim constante$ logo $N_{i}=p_{i}N$.
- O número de mensagens possíveis será aproximadamente o número de mensagens que contem o caráter $m_{1}$ $N_{1}$ vezes, $m_{2}$ $N_{2}$ vezes, ..., $m_{M}$ $N_{M}$ vezes. Ora, neste limite a probabilidade $p_{k}$ dos elementos da mensagem não varia, apenas variam as posições deles. 
- Assim, o número de mensagens é dado por:
$$\frac{N!}{N_{1}!\cdots N_{M-1}!}=g\ll M^{N}$$
noutras palavras: num sistema "normal" considerariamos que o número de combinações possíveis seria $M^{N}$. Ao ter o limite $N\to\infty$ ficamos com um número $g$ muito inferior.

- Podemos calcular (Stirling):
$$\begin{align*}
\log_{2}g&\simeq N\log_{2} N-N-\sum\limits_{k}(N_{k}\log_{2} N_{k}-N_{k})\\
&= N\log_{2} N - N - \sum\limits_{k}N_{k}\log_{2} N_{k}+N\\
&= N\log_{2} N-\sum\limits_{k} N_{k}\log_{2} N_{k}
\end{align*}$$
usando $N_{k}=p_{k}N$ temos:
$$\begin{align*}
\log_{2}g&\simeq N\log_{2}N-N\sum\limits_{k} (p_{k}\log_{2}p_{k}+p_{k}\log_{2}N_{k})\\
&= N\log_{2}N-N\log_{2}N - N\sum\limits_{k}p_{k}\log p_{k}\\
&= -N\sum\limits_{k}p_{k}\log_{2}p_{k} \ll N\log_{2}M
\end{align*}$$
com multiplicadores de lagrande é possível determinar que temos um máximo de informação quando $$p_{k}=\frac{1}{M}$$
AKA distribuição uniforme.
- Temos:
$$I=N\log_{2}g=N^{2}\left(-\sum\limits_{k}p_{k}\log_{2}p_{k}\right)$$

## Entropia de Shannon
- Podemos escrever a equação acima como:
$$I=N^{2}S(p_{1},\dots,p_{M})$$
pelo que temos a entropia de shannon:
$$S=-\sum\limits_{k}p_{k}\log_{2} p_{k}$$
- A entropia é 
    - mínima se $p_{k}=\delta_{lk}$ (apenas 1 elemento dos $M$ pode surgir na mensagem. Neste caso apenas importa o comprimento da mensagem) em que temos: $S=0$
    - máximo se $p_{k}=1/M$ e resulta: $S=\log_{2} M$

- De uma forma geral: se tivermos *distribuição uniforme* (entropia máxima) teremos: $$S=\log_{2}\Omega \quad \quad;\quad \Omega=\textsf{nº de estados possíveis}$$
- De outra forma, podemos definir a entropia como a falta de informação que temos sobre o fenómeno a ocorrer. Consideremos a função de probabilidade $f$ que para cada valor possível $m_{i}$ nos dá uma probabilidade. A informação desta será:
$$I[f]=\log_{2}M-S[f]$$