# 2 - Derivadas ao centro
- Na secção 1 de derivadas vimos derivadas calculadas ao aproximar-nos do ponto $x$ por valores maiores (para a frente) ou menores (para trás) e vimos que estes métodos são pouco precisos.
- Temos então derivadas ao centro, uma mistura das 2 outras:
$$\frac{df}{dx} \approx \frac{f\left(x + \frac{h}{2}\right)- f\left(x - \frac{h}{2}\right)}{h}$$
- Tal como antes, estamos a aproximar-nos de $x$ usando 2 pontos a uma distância $h$. Mas agora os 2 pontos são pontos a distâncias $\pm \frac{h}{2}$ de $x$

## 2.1 - Erros
- Começamos com 2 séries de Taylor:
$$\begin{align*}
f\left(x + \frac{h}{2}\right)&= f(x) + \frac{1}{2}hf'(x) + \frac{1}{8}h^{2}f''(x)+ \frac{1}{48}h^{3}f'''(x)+ \dots\\
f\left(x - \frac{h}{2}\right)&= f(x) - \frac{1}{2}hf'(x) + \frac{1}{8}h^{2}f''(x)-\frac{1}{48}h^{3}f'''(x)+\dots
\end{align*}$$
Subtraímos a 2ª à 1ª e temos:
$$f'(x)=\frac{f \left( x + \frac{h}{2}\right) - f \left(x - \frac{h}{2} \right)}{h} - \frac{1}{24}h^{2}f'''(x)$$
pelo que o erro de aproximação é $$\epsilon_\textsf{aprox} = \frac{1}{24}h^{2} |f'''(x)| $$
- O erro de arredondamento é, novamente: $\epsilon_\textsf{arred}= \frac{2C|f(x)|}{h}$
- Assim, o erro total é:
$$\epsilon (h)= \frac{2C|f(x)|}{h} + \frac{1}{24}h^{2} |f'''(x)| $$

- Novamente, fazemos $\frac{d\epsilon}{dh}=0$ e temos:
$$h_\textsf{erro min}=h = \sqrt[3]{24C \left| \frac{f(x)}{f'''(x)} \right|}$$
para o qual temos:
$$\epsilon_{min}= \sqrt[3]{\frac{9}{8} C^{2} [f(x)]^{2}|f'''(x)|}$$

- Assim, este método dá-nos um erro menor, sendo que o $h$ para o qual temos o erro mínimo é _maior_.
- Por outras palavras, derivada central dá menos erro, mas derivada para frente/trás permite-nos usar um intervalo $h$ menor, o que por vezes é muito importante.

#computacional #programacao #derivada
