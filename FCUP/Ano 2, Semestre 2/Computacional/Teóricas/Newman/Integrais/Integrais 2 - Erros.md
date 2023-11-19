#  4 - Erros - Teoria
- Os integrais calculados com os métodos acima apresentam erros: de _arredondamento_ e _erros de aproximação_.
- Os segundos são muito mais significativos e são devidos ao facto que a curva que estamos a integral é apenas uma aproximação da onda teórica/que queremos integrar.

## 4.1 - Trapézio
- Consideremos novamente a integral $\int_{a}^{b}f(x)dx$.
- Consideramos a fatia entre $x_{k-1}$ e $x_{k}$. Podemos então fazer a expansão de taylor de $f(x)$ em torno de $x_{k-1}$ e temos:
$$f(x)=f(x_{k-1})+(x-x_{k-1})f'(x_{k-1}) + \frac{1}{2} (x-x_{k-1})^{2}f''(x_{k-1})+\dots $$
assim temos:
$$\begin{align*}
\int_{x_{k-1}}^{x_{k}} f(x)dx&= f(x_{k-1})\int_{x_{k-1}}^{x_{k}}dx + f'(x_{k-1})\int_{x_{k-1}}^{x_{k}}(x-x_{k-1})dx+\\
&+ \frac{1}{2}f''(x_{k-1})\int_{x_{k-1}}^{x_{k}}(x-x_{k-1})^{2}dx+\dots 
\end{align*}$$
fazendo $u=x-x_{k-1}$
$$\begin{align*}
\int_{x_{k-1}}^{x_{k}} f(x)dx&= f(x_{k-1})\int_{0}^{h}du + f'(x_{k-1})\int_{0}^{h}u~du +\\
&+ \frac{1}{2}f''(x_{k-1})\int_{0}^{h}u^{2}~du+\dots\\
&= hf(x_{k-1})+ \frac{1}{2}h^{2}f'(x_{k-1})+ \frac{1}{6}h^{3}f''(x_{k-1})+O(h^{4})
\end{align*}$$
em que $O(h^{4})$ é o resto da série, ou seja, os termos de $h^{4}$ acima, que nós consideramos desprezáveis.
- Ao fazer o mesmo com $x_{k}$ temos:
$$\begin{align*}
f(x)&= f(x_{k})+(x-x_{k})f'(x_{k}) + \frac{1}{2} (x-x_{k})^{2}f''(x_{k})+\dots \\
\\
\int_{x_{k-1}}^{x_{k}} f(x)dx&= f(x_{k})\int_{x_{k-1}}^{x_{k}}dx + f'(x_{k})\int_{x_{k-1}}^{x_{k}}(x-x_{k})dx+\\
&+ \frac{1}{2}f''(x_{k})\int_{x_{k-1}}^{x_{k}}(x-x_{k})^{2}dx+\dots \\
\\
u=x-x_{k}\\
\\
\int_{x_{k-1}}^{x_{k}} f(x)dx&= f(x_{k})\int_{0}^{h}du + f'(x_{k})\int_{0}^{h}u~du +\\
&+ \frac{1}{2}f''(x_{k})\int_{0}^{h}u^{2}~du+\dots\\
&= hf(x_{k})- \frac{1}{2}h^{2}f'(x_{k})+ \frac{1}{6}h^{3}f''(x_{k}) - O(h^{4})
\end{align*}$$
(os sinais negativos surgem porque invertemos a ordem de integração)

- Podemos então fazer a média das 2 equações que obtivemos para $\int_{x_{k-1}}^{x_{k}}f(x)dx$ e temos:
$$\begin{align*}
\int_{x_{k-1}}^{x_{k}}f(x)dx&= \frac{1}{2}h[f(x_{k-1})+f(x_{k})] + \frac{1}{4}h^{2}[f'(x_{k-1})-f'(x_{k})]+\\
&+ \frac{1}{12}h^{3}[f''(x_{k-1})+f''(x_{k})]+O(h^{4})
\end{align*}$$
- Ora, consideremos que $[x_{k-1}~;~x_{k}]$ é 1 de $N$ fatias na integral $\int_{a}^{b}f(x)dx$. Temos:
$$\begin{align*}
\int_{a}^{b}f(x)dx&= \sum\limits_{k=1}^{N}\int_{x_{k-1}}^{x_{k}}f(x)dx\\
&= \frac{1}{2}h\sum\limits_{k=1}^{N}[f(x_{k-1})-f(x_{k})] + \frac{1}{4}h^{2}[f'(a)-f'(b)]\\ 
&\quad\quad\quad\quad + \frac{1}{12}h^{3}\sum\limits_{k=1}^{N}[f''(x_{k-1})+f''(x_{k})]+O(h^4)
\end{align*}$$
Vamos então analisar esta equação por partes:
1. O 1º sumatório ($\frac{1}{2}h\sum_{k=1}^{N}[f(x_{k-1})-f(x_{k})]$) é exatamente a regra do trapézio. Ou seja, ao usar este método estamos a ignorar os outros termos da integral. Ou seja, os restantes termos são o _erro de aproximação_ do método.
2. O 2º sumatório ($\frac{1}{4}h^{2}[f'(a)-f'(b)]$) é assim porque todos os termos se anulam exceto o primeiro e último (porque temos $f_{x-k}-f_{k}$). O mesmo iria ocorrer para todos os expoentes pares: $h^{4}, h^{6},\dots$
3. O 3º sumatório ($\frac{1}{12}h^{3}\sum_{k=1}^{N}[f''(x_{k-1})+f''(x_{k})]$) é apenas a integração de $f''$ entre $a$ e $b$, utilizando a regra do trapézio. Temos: $$\begin{align*}
\int_{a}^{b}f''(x)dx&= \frac{1}{2}h\sum\limits_{k=1}^{N}[f''(x_{k-1})+f(x_{k})]+O(h^{2})\\
&\left(\times \frac{1}{6}h^{2}\right)\\
\frac{1}{6}h^{2}\int_{a}^{b}f''(x)dx + O(h^{4})&= \frac{1}{12}h^{3}\sum\limits_{k=1}^{N}[f''(x_{k-1})+f(x_{k})]\\
&\textsf{Temos que} \int f'' = f' \textsf{ , logo:}\\
\frac{1}{6}h^{2} [f'(b)-f'(a)] +O(h^{4})&= \frac{1}{12}h^{3}\sum\limits_{k=1}^{N}[f''(x_{k-1})+f(x_{k})]\\
\end{align*}$$
- Podemos então substituir o que obtivemos na equação da integral e temos:
$$\begin{align*}
\int_{a}^{b}f(x)dx&= \frac{1}{2}h\sum\limits_{k=1}^{N}[f(x_{k-1})-f(x_{k})] + \frac{1}{12}h^{2}[f'(a)-f'(b)]+O(h^4)
\end{align*}$$
- Ou seja, conseguimos simplificar a equação e temos que o erro da regra do trapézio é:
$$\epsilon=\frac{1}{12}h^{2}[f'(a)-f'(b)]$$
esta é a _fórmula de Euler-Maclaurin_ para determinar o erro da regra do trapézio (o 1º termo). De notar que os próximos termos seriam de ordem $h^{4}, h^{6}, \dots$. Assim, desde que $h$ seja reduzido podemos ignorar estes termos.

- Vemos ainda que o erro de aproximação diminui com $h$ menor. E sabemos que o erro de arredondamento é igual a $C\int f~dx$. Assim, a certo ponto, se diminuirmos $h$ muito, teríamos um erro de arredondamento maior que o de aproximação.
- Ora, a partir desse ponto, diminuir $h$ já não nos ajuda na exatidão. A exatidão será apenas melhorada ao reduzir o erro de arredondamento. Ora, este erro marca o ponto de _precisão máxima_ que podemos obter com python, porque se deve à forma como a linguagem em si funciona. 
- Ou seja, só precisamos de diminuir $h$ até que:
$$\frac{1}{12}h^{2}[f'(a)-f'(b)]\approx C\int_{a}^{b}f(x)dx$$
de onde tiramos
$$h\approx \sqrt{\frac{12C\int_{a}^{b}f(x)dx}{f'(a)-f'(b)}}$$
e como $\large h=\frac{b-a}{N}$:
$$N\approx (b-a)\sqrt{\frac{f'(a)-f'(b)}{12C\int_{a}^{b}f(x)dx}}$$
Por exemplo, se todos os termos exceto $C$ forem de ordem 1, o erro de arredondamento só se torna o maior dos 2 a partir de $N\sim 10^{8}$.
- No entanto, $10^{8}$ intervalos de integração é um número demasiado grande para a regra do trapézio. Assim, na grande maioria dos casos iremos usar um número de intervalos em que o erro de aproximação é mais significante e iremos ignorar o erro de arredondamento.

## 4.2 - Simpson
- A análise para obter isto é bem pior, mas temos:
$$\epsilon= \frac{1}{90}h^{4}[f'''(a)-f'''(b)]$$
daqui percebemos porquê que a regra de Simpson nos dá erros muito menores para $h$ pequenos.
- Neste caso, temos que:
$$N\approx (b-a)\sqrt[4]{\frac{f'''(a)-f'''(b)}{90C\int_{a}^{b}f(x)dx}}$$
- Ora, agora o erro de aproximação agora já se torna maior que o de arredondamento (e significante) quando $N=10~000$. Isto é um dado útil, porque uns poucos milhares de intervalos de integração podem ser calculados em menos de 1s, pelo que nunca precisamos de utilizar muito mais que isto com o método de Simpson.
- No entanto, devemos notar que como $\epsilon\propto f'''$ se por alguma razão a terceira derivada de $f$ num ponto for muito elevada, o erro aí também será. Ou seja, em regra geral Simpson dá os melhores resultados, mas podemos ter exceções.

# 5 - Erros - na prática
## 5.1 - Trapézio
- As fórmulas que obtivemos acima determinam erros utilizando derivadas. Ora, nem sempre podemos fazê-las. O que estamos a integrar pode não ser derivável, pode nem ser uma função matemática mas sim um conjunto de dados.

- Assim, consideremos que estamos a utilizar o método do Trapézio para calcular uma integral entre $a$ e $b$, com $N_{1}$ intervalos, sendo $h_{1}=(b-a)/N_{1}$
- A seguir, repetimos o integral, mas com $N_{2}=2N_{1}$ intervalos, ou seja, com $h_{2}=\frac{1}{2}h_{1}$. Ora, este integral, em princípio, terá um menor erro.
- Ora, como a regra do Trapézio apresenta um fator de $O(h^{2})$, ao dividir $h$ por 2, o erro diminiu para $1/4$.

- Assim, considerando que o integral teórico que queremos obter é $I$. Os integrais obtidos com $N_{1},N_{2}$ são $I_{1},I_{2}$. Como o erro é proporcional a $h^{2}$ temos $I=I_{1}+ch_{1}^{2}=I_{2}+ch_{2}^{2}$, de onde temos:
$$I_{1}+ch_{1}^{2}=I_{2}+ch_{2}^{2} \longrightarrow I_{2}-I_{1}=ch_{1}^{2}-ch_{2}^{2}=3ch_{2}^{2}$$
(porque $h_{2}=\frac{1}{2}h_{1}\rightarrow h_{1}=2h_{2}$)
- Ora, vimos acima que $\epsilon=ch^{2}$ logo:
$$\epsilon_{2}=ch_{2}^{2}= \frac{1}{3}(I_{2}-I_{1})$$
(esta equação pode ser positiva ou negativa, o que indica se o erro é por excesso ou defeito)
- Esta fórmula dá valores corretos, e é tão simples que há vezes em que podemos usar a fórmula de Euler-Macleurin e usamos esta.

## 5.2 - Simpson
- A dedução é feita num exercício. Talvez me dê ao trabalho de fazer e escrever aqui, eventualmente. Dá:
$$\epsilon_{2}=\frac{1}{15}(I_{2}-I_{1})$$

#computacional #programacao #integrais 
