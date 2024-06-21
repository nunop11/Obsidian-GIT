# 1 - Incertezas
## Tipos
**Tipo A** - Natureza estatística. Consideramos como independentes. Podem ser reduzidas ao fazer mais medições
**Tipo B** - Associadas à limitações dos instrumentos. Só podem mudar se trocarmos de instrumento de medição.

## Valores e Nomes
- Podemos dizer que uma medição $V$ se encontra num intervalo de confiança $[V_{min},V_{max}]$. 
- A medição terá uma incerteza $u(V)$ tal que dizemos que a medição feita é: $V=V_{mais~~provavel}\pm u(V)$

- Algumas palavras úteis:
    - *precisão* - quão próximas *entre si* as medições estão. (mais precisão == menos dispersão)
    - *veracidade* - quão próxima a média das medições está do valor real (== exatidão)

# 2 - Tipo A
- Valor mais provavel AKA média:
$$\overline{x}= \frac{1}{N}\sum\limits_{i=1}^{N}x_{i}$$
e temos desvio padrão:
$$s_{x}=\sqrt{\frac{\sum\limits_{i=1}^{n}(x_{i}-\overline{x})^{2}}{n-1}}$$
- Temos a incerteza padrão:
$$s(\overline{x})=\frac{s_{x}}{\sqrt{N}}$$
que consiste na *incerteza da média*. Isto assume que as medições são experiências independentes e aleatórias!

# 3 - Tipo B
- No mínimo iguais aos arredondamentos dos instrumentos (por exemplo se uma balança apresenta o valor até às gramas). Mas na realidade temos incertezas acima disso.
- Um certo instrumentação de medida (nomeadamente multímetros para esta UC) são representados por $$a \frac{n-1}{n}$$
em que: $a$ é o número de dígitos 0-9 à direita e $n$ o valor máximo que o MSD (dígito mais significativo) pode assumir.
    - Por exemplo um multimetro representado por $4 \frac{3}{4}$ poderá medir valor de 0 a 49999

*Alcance/range* - valor máximo que pode ser medido
*Resolução* - menor variação da grandeza que pode ser detetada

### Incerteza
- Dada por:
$$u = u_{Leitura}\times \text{Valor Lido} + \text{LSDs}$$
sendo que a incerteza de leitura e os LSDs a incluir nesta conta são indicados na datasheet, na forma:
$$\pm[u_{Leitura}(\%) + b\times \text{LSDs}]$$

## Comportamento probabilístico
- De uma forma geral, consideremos uma VA (olha quem voltou) $X$ que segue uma distribuição de probabilidade $f$ com valor médio $\mu$
- No caso de uma medição: $X$ é o resultado da medição, $f$ está relacionado com o comportamento do instrumento, $\mu$ é o valor real da grandeza (medido se o instrumento estiver bem calibrado).

### Distribuição retangular
- Quando podemos assumir que o instrumento não tem comportamento inviesado
- A densidade é descrita por
$$f(x)=\begin{cases}
\frac{1}{a^{+}-a^{-}} & ; & a^{-}<x<a^{+} \\
0 & ; & \text{resto}
\end{cases}$$
tendo-se a média $E[X]=\frac{a^{+}+ a^{-}}{2}$ e variância $V(X)=\frac{(a^{+}+ a^{-})^{2}}{12}$

### Distribuição triangular
- Usamos no caso em que exista tendência de o valor medido se aproximar de um certo valor (inviesado)
- A densidade é descrita por
$$f(x) = \frac{2}{a^+-a^-}\begin{cases} \frac{x-a^-}{b-a^-} & \text{se }a^- < x \le b \\ \frac{a^+-x}{a^+-b} & \text{se } b < x < a^+ \\ 0 &\text{resto} \end{cases}$$
tendo-se a média $E[X]=\frac{a^- + b + a^+}{3}$ e variância $V(X)=\frac{(a^-)^2 + b^2 + (a^+)^2 - a^-a^+ - a_- b - a^+b}{18}$
- É uma coisa deste género:
![[dist prob triangular.png|425]]

No caso particular em que $b = (a^+ + a^-)/2$ temos $b = \mu$, pelo que podemos definir a incerteza como $a = (a^+-a^-)/2$ e escrever a densidade de probabilidade da seguinte forma:

$$ f(x) = \frac{1}{a}\begin{cases}
\frac{x-(\mu-a)}{a} & \text{se }\mu-a < x \le \mu \\
\frac{(\mu+a)-x}{a} & \text{se } \mu < x < \mu+a \\
0 &\text{caso contrário}
\end{cases} $$

Obtemos então o seguinte desvio padrão: $\sigma = \frac{a}{\sqrt 6}$

### Distribuição Arcsine
- Quando temos circuitos com incertezas muito diferentes (especialmente sistemas radio-frequência ou micro-ondas)
- A densidade é descrita por
$$f(x) = \begin{cases} \frac1{\pi \sqrt{(x-a^-)(a^+ - x)}} & \text{se }a^- < x < a^+ \\ 0 &\text{resto} \end{cases}$$
tendo-se a média $E[X]=\frac{a^{+}+a^{-}}{2}$ e a variância $V(X)=\frac{a^{+}-a^{-}}{2\sqrt{2}}$
- Tem a forma:
![[dist arcosin.png|400]]
Mais uma vez, podemos escrever esta densidade de probabilidade em função da média $\mu$ e da incerteza de leitura $a = (a^+-a^-)/2$ e fica:
$$ \begin{align*}
f(x) = \begin{cases}
\frac1{\pi \sqrt{[x-(\mu-a)][(\mu+a) - x]}} & \text{se } |x-\mu| < a \\
0 &\text{resto}
\end{cases}
\end{align*} $$
Obtemos então o seguinte desvio padrão: $\sigma=\frac{a}{\sqrt{2}}$

# 4 - Propagação de incertezas
- Temos um valor $Y$ que é dado por uma função de outras variáveis $X_{i}$: $Y=f(X_{1},X_{2},\dots,X_{n})$
- Consideremos:
    - $x_{i},\sigma_{i}$ o valor medido e desvio padrão de uma VA $X_{i}$
    - $\sigma_{y}$ o desvio padrão de $Y$
    - $K_{ij}$ a matriz das covariâncias das variaveis $X_{i}$: $K_{ij}=\text{Cov}(X_{i},X_{j})$

## Variância Exata
- A variância exata de $Y$ conforme as variáveis $X_{i}$ pode ser obtida, mas normalmente isto é super difícil e/ou trabalhoso
- Para isso, consideramos que a variável $Y$ pode ser escrita como uma combinação linear: $Y=a_{1}X_{1}+\dots+a_{n}X_{n}=\mathbf{a}^{T}\mathbf{X}$
- Deste modo a sua variância é:
$$\text{Var}(Y) = \sum\limits_{i,j=1}^{k}a_{i}a_{j}\text{Cov}(X_{i},X_{j})=\sum\limits_{i=1}^{k}a_{i}^{2}\text{Var}(X_{i})+\sum\limits_{i\neq j}^{k}a_{i}a_{j}K_{ij}$$

## Variância Aproximada
- Para a maioria das funções temos que usar série de Taylor (HAHAHAHAHAHA):
$$\begin{align*} f(\textbf X) &\approx f(\textbf X_0) + \nabla f(\textbf X_0) \cdot (\textbf X-\textbf X_0) \\ &= f(\textbf X_0) + \sum_{i=1}^n \frac{\partial f}{\partial x_i}(x_{0i})\cdot (x_i-x_{0i}) \\ &= \left[f(\textbf X_0) - \sum_{i=1}^n\frac{\partial f}{\partial x_i}(x_{0i})x_{0i}\right] + \sum_{i=1}^n \frac{\partial f}{\partial x_i}(x_{0i})x_i \end{align*}$$
o termo entre parentesis é uma constante, pelo que não afeta a incerteza. 
- Por esta razão (qual?) a variância é basicamente a mesma que para uma densidade descrita por uma combinação linear de variáveis:
$$V(Y)=\sum_{i=1}^n \left(\frac{\partial f}{\partial x_i}\right)^2 \sigma_i^2 + 2\sum_{i=1}^n\sum_{j> i} \left(\frac{\partial f}{\partial x_i}\right)\left(\frac{\partial f}{\partial x_j}\right) \rho_{ij}\sigma_i\sigma_j$$
