**_ESTE "RESUMO" É LITERALMENTE INÚTIL_**
- Consideremos que uma experiência foi feita $M$ vezes, tendo-se obtido os resultados $\{ x_{1},x_{2},\dots,x_{M} \}$ em que cada um tem probabilidade $P_{k}$ de acaontecer.
- Ora, a informação associada a estes acontecimentos é $\log_{2}M=x$ 
- Por exemplo:
    - $\{0,1\}$ implica 1 bit
    - $\{0,1,2\}$ implica 2 bits
    - $\{0,1,2,3\}$ implica 2 bits

- Assim, a informação associada a uma mensagem com $N$ caratéres será:
$$N\log_{2}M=\log_{2}M^{N}$$
(pois temos $M^{N}$ combinações possíveis)

> **EXEMPLO**
> Consideremos uma mensagem com $1024$ caratéres em que temos $16$ caratéres diferentes. A informação será $1024\log_{2}16=4096~bits$
> No entanto, se apenas tivermos 1 caratér possível (isto é $P_{1}=1~;~P_{k}=0~,~k\neq1$) temos que a informação é $1~bit$.

## Limite Termodinâmico
- Neste limite temos $N\to+\infty$, $N_{k}\to P_{k}N$ (em que $N_{k}$ representa cada configuração possível do sistema)
- Podemos establecer $\sqrt{\langle N_{k}^{2}\rangle - \langle N_{k}\rangle^{2}}\propto \sqrt{N}$ (vá se lá saber pq)
- Em que o número de mensagens possíveis é $\frac{N!}{N_{1}!N_{2}!\cdots N_{M}!}\neq M!$

- Podemos fazer:
$$\begin{align*}
\log_{2} \left( \frac{N!}{N_{1}!N_{2}!\cdots N_{M}!} \right)&= \frac{\ln \left( \frac{N!}{N_{1}!N_{2}!\cdots N_{M}!} \right)}{\ln2}\\
& \underbrace{=}_\text{Fórmula de Stirling} \frac{1}{\ln2} \left( N\ln N-N- \sum\limits_{k} N_{k} \ln N_{k}-N_{k} \right)\\
&= \frac{1}{\ln2} \left( N\ln N-\sum_{k} N_{k}\ln N_{k}  \right)\\
&= \frac{1}{\ln2} \left( N\ln N- \sum\limits_{k}P_{k}N\ln P_{k}N  \right)\\
&= \frac{1}{\ln2} \left( N\ln N- \sum\limits_{k}(P_{k}N\ln P_{k} + P_{k}N\ln N ) \right)\\
&= \frac{1}{\ln2} \left( -N\sum\limits_{k} P_{k}\ln P_{k} \right)\\
&= -N \sum\limits_{k}P_{k} \log_{2}P_{k}\\
&= -N \langle \log_{2} P_{k}\rangle
\end{align*}$$

- Mas qual é a distribuição que maximiza o lagrangeano?
$$\mathcal{L}=\sum\limits_{k}P_{k}\log_{2}P_{k}- \Lambda\left(\sum\limits_{k}P_{k}-1\right)$$
- Vejamos a derivada:
$$\frac{\partial\mathcal{L}}{\partial\Lambda}=0\to \sum\limits_{k}P_{k}=1$$

$$\frac{\partial \mathcal{L}}{\partial P_{\ell}}=0\to \log_{2}\mathcal{P}_{\ell}+ \frac{1}{\ln2} - \Lambda=0$$
$$\begin{align*}
\log_{2}\mathcal{P}_{\ell}&= \Lambda- \frac{1}{\ln2}\\
\mathcal{P}_{\ell}&= 2^{\Lambda - \frac{1}{\ln2}}\\
\sum\limits_{\ell} \mathcal{P}_{\ell}&= \sum\limits_{\ell} 2^{\Lambda - \frac{1}{\ln2}}\\
1&= M 2^{\Lambda - \frac{1}{\ln2}}\\
\frac{1}{M}&= 2^{\Lambda - \frac{1}{\ln2}}\\
\mathcal{P}_{\ell}&= \frac{1}{M}~~,~~ \forall \ell
\end{align*}$$
