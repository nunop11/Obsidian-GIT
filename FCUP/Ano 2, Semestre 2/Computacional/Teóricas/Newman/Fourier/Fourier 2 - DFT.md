# 2 - Discrete Fourier Transform
$$\gamma_{k}=\frac{1}{L} \int_{0}^{L}f(x)\exp \left(-i \frac{2\pi kx}{L} \right)dx$$
- Por vezes, conseguimos usar a equação acima para determinar os coeficientes de forma analítica e exata. No entanto, há casos em que isso não é possível: $f$ pode ser muito complicada, ou pode não ser uma função de todo. Nesses casos temos que determinar $\gamma_{k}$ de forma numérica, usando os métodos que vimos.

- Com o método do trapézio com $N$ intervalos temos:
$$\gamma_{k}=\frac{1}{L} \frac{L}{N} \left[ \frac{1}{2}f(0) + \frac{1}{2} f(L) + \sum\limits_{n=1}^{N-1} f(x_{n})\exp\left(-i \frac{2\pi kx}{L}\right) \right] $$ em que distribuimos os sample points da forma $x_{n}=\frac{n}{N}L$
- No entanto, como $f$ será periódica, temos por definição $f(0)=f(L)$. Assim:
$$\gamma_{k}=\frac{1}{N} \sum\limits_{n=0}^{N-1} f(x_{n})\exp \left( -i \frac{2\pi kx}{L} \right)$$

- Ora, muitas vezes temos muitos samples (como "frames" de um certo aúdio que estamos a analisar), recolhidos em intervalos de tempo iguais. Isto é algo que já temos na equação acima, mas podemos simplificar mais. Definindo $y_{n}$ como sendo o sample recolhido temos:
$$\gamma_{k}= \frac{1}{N}\sum\limits_{n=0}^{N-1} y_{n}\exp \left( -i \frac{2\pi kn}{L} \right) \quad \quad \textsf{(Eq. 0)}$$
pelo que neste formato já nem precisamos de saber os $x$ dos samples nem o tamanho do intervalo. Precisamos apenas de saber quais e quantos são os samples.
- A equação 1 define a *Transformada Discreta de Fourier* aka **DFT**, que por convenção definimos assim:
$$c_{k}=\sum\limits_{n=0}^{N-1} y_{n} \exp \left( -i \frac{2\pi kn}{N} \right) \quad \quad \textsf{(Eq. 1)}$$
- Às constantes $c_{k}$ iremos chamar de *__Coeficientes de Fourier__* (apesar de os "verdadeiros" coeficientes de fourier serem os $\gamma_{k}$)
- Apesar de termos feito esta dedução usando o método do trapézio, os coeficientes que obtemos são *exatos*.

> **Explicação**
> - Para série geométrica temos: $$\sum\limits_{k=0}^{N-1} a^{k} = \frac{1-a^{N}}{1-a}$$
> - Ora, vamos substituir $a = e^{i2\pi m/N}$:
> $$\sum\limits_{k=0}^{N-1} e^{i2\pi km/N} = \frac{1-e^{i2\pi m}}{1-e^{i2\pi m/N}}=\frac{0}{1-1e^{m/N}}=0$$
> - A única exceção é quando $m= nN, n\in \mathbb{Z}$ ($m$ é 0 ou multiplo de $N$). Neste casos, vemos logo na operação original que ficamos com $\sum\limits_{k=0}^{N-1} e^{i2\pi km/N}=N$
> (Página 304 do pdf. Acabar depois talvez)

- Temos que a série de Fourier pode ser obtida da seguinte forma: $$y_{n}=\frac{1}{N} \sum\limits_{k=0}^{N-1} c_{k}\exp \left(i \frac{2\pi kn}{N} \right) \quad \quad \textsf{(Eq. 2)}$$
- Isto é o *DFT inverso*. Isto é o equivalente à equação $f(x)=\sum_{k=-\infty}^{+\infty}\gamma_{k} \exp\left(i \frac{2\pi kx}{L}\right)$, que vimos no início desta secção. Basicamente, tal como podemos obter $\gamma_{k}$ usando $f(x)$ e vice-versa, também podemos obter $c_{k}$ usando $y_n$ _e vice-versa_. De notar ainda que, ao usar $c_{n}$ para obter $y_{n}$ usando Eq. 2 iremos obter resultados *exatos*, à exceção de erros de arredondamento.
- Notemos ainda que, ao definir $c_{n}$ removemos um fator $1/N$ da formula de $\gamma_{k}$, mas agora na formula temos um fator $1/N$ a mais em relação à formula de $f(x)$.
- De notar que a Eq.2 é melhor para usar em programação porque apenas temos que iterar até $N-1$, não até $+\infty$.

- No entanto, o DFT tem um problema: apenas conhecemos os sample points. Não sabemos nada acerca da função entre estes pontos. Ou seja, tendo os mesmos sample points, podiamos ter qualquer um dos casos abaixo:
![[fourier-entre samples.png]]

- Ainda assim, desde que a função seja minimamente suave, o DFT é suficiente.

## 2.1 - DFT com f real
- Tudo o que vimos sobre DFT funciona muito bem tanto com funções reais como complexas. No entanto, na maioria dos casos, temos funções reais pelo que podemos fazer algumas simplificações.

- Consideremos que todos os $y_{n}$ são reais e que temos $c_{k}$ sendo $\frac{1}{2}N<k<N-1$. Assim, vamos escrever $k$ como $k=N-r$ sendo $1\leq r< \frac{1}{2}N$
- Assim:
$$\begin{align*}
c_{N-r} &=  \sum\limits_{n=0}^{N-1} y_{n}\exp \left( -i \frac{2\pi (N-r)n}{N} \right)=\sum\limits_{n=0}^{N-1} y_{n} \cancelto{=1}{\exp \left( -i2\pi n \right)} \exp \left( i \frac{2\pi r n}{N} \right) \\
&= \sum\limits_{n=0}^{N-1} y_{n} \exp \left( i \frac{2\pi rn}{N} \right) = c_{r}^{*}
\end{align*}$$
em que $c_{r}^{*}$ é o conjugado de $c_{r}$.
- Ou seja, por analogia com a demonstração acima: $c_{N-1}=c_{1}^{*}~,~ c_{N-2}=c_{2}^{*}\dots$
- Assim, facilmente vemos que apenas é preciso calcular os coeficientes $c_{k}$ para $0\le k\le \frac{1}{2}N$, porque a outra metade dos coeficientes irão ser apenas os conjugados. Assim: se $N$ for par temos que calcular $\frac{1}{2}N+1$; se for ímpar temos que calcular $\frac{1}{2}(N+1)$.
    - De notar que esta quantidade, para ambos os casos, pode ser escrita em python como `N // 2+1`

---
Exemplo de uma função que calcula o DFT:
![[dft codigo.png]]

## 2.2 - Posições dos sample points
- Ao calcular uma DFT, podemos "deslizar" todos os sample points um pouco para o lado e pouco muda.

- Consideremos que deslizamos os sample points uma distância $\Delta$:
$$x_{n}' = x_{n}+\Delta=\frac{n}{N}L +\Delta$$
- Temos então:
$$\begin{align*}
c_{k}&= \sum\limits_{n=0}^{N-1} f(x_{n}+\Delta)\exp \left(-i \frac{2\pi (x_{n}+\Delta)}{L} \right)\\
&= \exp \left(-i \frac{2\pi k \Delta}{L} \right) \sum\limits_{n=0}^{N-1} f(x_{n}') \exp \left( -i \frac{2\pi k x_{n}}{L} \right)\\
&= \exp\left( -i \frac{2\pi k \Delta}{L}\right)\sum\limits_{n=0}^{N-1} y_{n}' \exp \left( -i \frac{2\pi kn}{N} \right)
\end{align*}$$
- Assim, absorvemos o fator de fase (fator antes do sumatório), definindo $c_{k}' = \exp(i2\pi k\Delta/L) c_{k}$ e temos:
$$c_{k}'=\sum\limits_{n=0}^{N-1} y_{n}' \exp \left( -i \frac{2\pi kn}{N} \right)$$

- Ou seja, na realidade não importa onde colocamos os sample points para o DFT.
- Temos então 2 tipos de DFT:
![[dft tipo 2.png]]
sendo que no tipo 1 metemos os sample points nos pontos inteiros, pelo que não temos ponto no fim do intervalo. Assim, como meio termo, no tipo 2 temos sample points nos meios pontos.

#computacional #programacao #fourier
