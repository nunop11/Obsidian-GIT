# Distribuição Binomial
(Esta aula foi copiada dos apontamentos do Diogo)

- Temos uma variável aleatória $$X=\sum\limits_{i=1}^{N}x_{i}$$
em que temos $x\in\{ 0,1 \}$, tal que $P(0)=p~P(1)=1-p$.
- Assim, tendo uma sequência de $n$ zeros e $N$ 1s, a probabilidade de ela acontecer é: $$P_{\textsf{1 sequência}}=p^{N}(1-p)^{N-n}$$
- Ora, a probabilidade de termos $n$ zeros será:
$$P_\textsf{$n$ zeros}=\sum\limits_{\substack{i\in \Omega\\ \#\Omega=2^{N}}} P(n_{i})\cdot \delta_{n_{i}n_{j}}=p^{N}(1-p)^{N-n} \sum\limits_{i} \delta_{n_{i}n_{j}}\quad(????)$$
$$P(n)=\frac{N!}{n!(N-n)!}p^{N}(1-p)^{N-n}$$
esta é, portanto, a **Distribuição Binomial**. Podemos interpretar os $0,1$ como sucessos e insucessos ao realizar uma certa experiência. A partir de agora, consideraremos $n$ o número de sucessos e $N$ o número de vezes que a experiência foi realizada. Não faço ideia porquê que acima fazemos diferente.

- Sendo $q=1-p$, temos o valor médio de $n$:
$$\begin{align*}
\langle n\rangle &= \sum\limits_{n=0}^{N}n \frac{N!}{n!(N-n)!}p^{n}q^{N-n}\\
&= p \frac{d}{dp}\sum\limits_{n=0}^{N} \frac{N!}{n!(N-n)!}p^{n}q^{N-n}\\
&= p \frac{d}{dp}(p+q)^{N}\\
&= Np
\end{align*}$$
em que 
    - Introduzimos $p \frac{d}{dp}$ como um método de determinar o valor médio (idk, ask Chatgpt)
    - $\sum(\dots)=(p+q)^{N}=1^{N}$

- Temos ainda:
$$\begin{align*}
\langle n^{2}\rangle &= \sum\limits_{n=0}^{N}n^{2} \frac{N!}{n!(N-n)!}p^{n}q^{N-n}\\
&= p \frac{d}{dp} p\frac{d}{dp} (p+q)^{N} ~~~~(???)\\
&= Np + N(N-1)p^{2}
\end{align*}$$
e a variância:
$$\sigma^{2}=\langle n^{2}\rangle- \langle n\rangle^{2}=Np(1-p)$$
