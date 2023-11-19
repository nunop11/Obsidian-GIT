# Transformada de Hillbert
- É definida como:
$$\mathcal{H}[x(t)]=x(t)* \frac{1}{\pi t}$$
- Sendo a transformada inversa: $$-\mathcal{H}[\mathcal{H}[x(t)]]=x(t)$$
- A partir do operador convolução temos:
$$\mathcal{H}[x(t)]=\frac{1}{\pi} \int_{-\infty}^{+\infty} x\frac{\eta}{t-\eta}d\eta$$

## Causal
- Como vimos antes, um SLIT ser causal implica que o sinal de entrada "causa" o sinal de saída. Isto implica também que, se o sinal de entrada só começa a ser emitido em $t=t_{0}$, então não existe sinal de saída para $t<t_{0}$
- Mais especificamente, para SLITs vimos que um sinal causal é um sinal que *só pode ser não nulo* para $t\ge 0$.

- Estudemos um sinal **causal e real**. Temos: $h(t)=h(t)u(t)$ 
- A transformada de Fourier de um produto é $F[d(t)g(t)]= \frac{1}{2\pi} D(j\omega)*G(j\omega)$
- Anteriormente vimos que $F[u(t)]=\pi \delta(\omega)+ \frac{1}{j\omega}$
- Ou seja:
$$\begin{align*}
F[h(t)]&= F[h(t)u(t)]\\
H(j\omega)&= \frac{1}{2\pi} H(j\omega)* \left[ \pi \delta(\omega)+ \frac{1}{j\omega} \right]\\
H(j\omega)&= \frac{1}{2}H(j\omega) + \frac{1}{2\pi}H(j\omega)* \frac{1}{j\omega}\\
\frac{1}{2}H(j\omega)&= \frac{1}{2\pi}H(j\omega) * \frac{1}{j\omega}\\
H(j\omega)&= \frac{1}{\pi}H(j\omega)* \frac{1}{j\omega}
\end{align*}$$
podemos agora dividir $H(j\omega)=\text{Re}[H(j\omega)]+j\text{Im}[H(j\omega)]$ . Ao substituir na eq acima temos:
$$\text{Re}[H(j\omega)]+j\text{Im}[H(j\omega)]=\frac{-j}{\pi} \text{Re}[H(j\omega)] * \frac{1}{\omega} + \frac{1}{\pi}\text{Im}[H(j\omega)]* \frac{1}{\omega}$$
de onde temos:
$$\begin{align*}
\text{Re}[H(j\omega)]&= \frac{1}{\pi}\text{Im}[H(j\omega)]* \frac{1}{\omega}\\
\text{Im}[H(j\omega)]&= \frac{-j}{\pi} \text{Re}[H(j\omega)] * \frac{1}{\omega}
\end{align*}$$
- Ou seja, a amplitude e fase da transformada de Fourier de um sinal causal e real *dependem uma da outra*. Reescrevendo as expressões acima como:
$$\begin{align*}
\text{Re}[H(j\omega)]&= \mathcal{H}\{\text{Im}[H(j\omega)]\}\\
\text{Im}[H(j\omega)]&= -\mathcal{H}\{\text{Re}[H(j\omega)]\}
\end{align*}$$
conseguimos escrever:
$$\boxed{\mathcal{H}[X(j\omega)]=\frac{1}{\pi} X(j\omega)* \frac{1}{\omega} }$$
a que chamamos ***Transformada de Hillbert*** para um sinal causal, e *em termos de frequência*.

- Tendo 2 sinais $d,g$ podemos escrever:
$d(t)*g(t)=\int_{-\infty}^{+\infty}d(\tau)g(t-\tau)d\tau \to D(\omega)*G(\omega)=\int_{-\infty}^{+\infty}D(\eta)G(\omega-\eta)d\eta$
- Sendo $D(\omega)=X(j\omega)~,~G(\omega)=\frac{1}{\omega}$ ficamos com $$\mathcal{H}[X(j\omega)] = \frac{1}{\pi} \int_{-\infty}^{+\infty} \frac{X(j\eta)}{\omega-\eta}d\eta$$
- Temos aqui a *forma alternativa, em frequência*.

## Hilbert num sistema
- Como vimos acima, temos $\mathcal{H}[x(t)]=x(t)* \frac{1}{\pi t}$
- Ou seja, se tivermos um sistema em que a resposta impulsional é $h(t)=\frac{1}{\pi t}$, então o sinal de saída será a transformada de Hillbert do sinal de entrada.
- Neste sentido, podemos ainda determinar:
$$h_{Hillbert}(t)=\frac{1}{\pi t} \Longrightarrow H_{Hilbert}(j\omega)=-j\text{sign}(\omega)$$
em que usamos a função sigma.

# Sinais Analíticos
- Temos uma função $f(t)$, real e causal. Com ela definimos:
$$f_{analitico}(t)=f(t)+j \mathcal{H}[f(t)]$$

- Consideremos que temos um sinal $x(t)=\cos(\omega_{0}t)$. O sinal analítico correspondente será:
$$x_{a}(t)=\cos(\omega_{0}t)+j\sin(\omega_{0}t)=e^{j\omega_{0}t}$$
>Demonstração:
>$$ \begin{align*}
\mathcal H[x(t)] &= \left(\cos(\omega_0t) *\frac1{\pi t}\right)(t) \\
&= F^{-1}\left[F\left[\left(\cos(\omega_0t) *\frac1{\pi t}\right)(t)\right]\right] \\
&= F^{-1}\left[F[\cos(\omega_0t)] \times F[1/(\pi t)]\right] \\
&= F^{-1}[-i\pi(\delta(\omega - \omega_0) + \delta(\omega + \omega_0))\text{sgn}(\omega)] = \\
&= F^{-1}[-i\pi(\delta(\omega - \omega_0)\text{sgn}(\omega) + \delta(\omega + \omega_0)\text{sgn}(\omega))] = \\
&= F^{-1}[-i\pi(\delta(\omega - \omega_0)\text{sgn}(\omega_0) + \delta(\omega + \omega_0)\text{sgn}(-\omega_0)] = \\
&= F^{-1}[-i\pi(\delta(\omega - \omega_0) - \delta(\omega + \omega_0))] = \\
&= \sin(\omega_0t)
\end{align*} $$
de notar que aqui se usou $$\begin{array}{c|c} f(t) & F[f(t)] \\ \hline  \sin(\omega_0t) & -i\pi\left[\delta(\omega - \omega_0) - \delta(\omega + \omega_0)\right] \\[0.2cm] \cos(\omega_0t) & \pi\left[\delta(\omega - \omega_0) + \delta(\omega + \omega_0)\right] \end{array}$$

- Vimos acima, ao determinar $\mathcal{H}[\cos(\omega_{0}t)]=\sin(\omega_{0}t)$, que a transformada de Hillbert de um sinal real e causal *cria um atraso de 90 graus*.

- Podemos usar o sinal analítico para estudar a resposta real e imaginário de um SLIT, o que é possibilitado pela linearidade destes sistemas.
- Temos ainda que a transformada de Fourier de uma transformada de Hillbert não terá frequências negativas.

# Envolventes de uma Função
- No caso anterior vimos que $$x(t)=\cos(\omega_{0}t)\to x_{a}(t)=e^{j\omega_{0}t}$$sendo que ambos têm amplitude $1$.
- Ora, em geral, se tivermos um sinal $$x(t)=A(t)\cos(\omega_{0}t)~~;~~ \textsf{$A$ varia muito mais lentamente que $\omega_{0}t$}$$
então teremos $$|x_{a}(t)|\approx A(t)$$

#sinais #fisica