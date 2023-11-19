# 12 - Método de Newton-Raphson
***AKA Método de Newton***
![[newton raphson.png]]
- Tal como no Binary Search, começamos por colocar a equação num formato $f(x)=0$
- Primeiro escolhemos 1 ponto inicial $x$. Usando o declive da tangente nesse ponto obtemos outro. Assim:
    - Em $x$ temos: $\large f'(x)\approx f\frac{x}{\Delta x}$
    - Daí temos a nossa próxima tentativa: $$\begin{align*}x' &= x-\Delta x\\ x' &= x - \frac{f(x)}{f'(x)}\end{align*}$$
- E é isto. Este método, apesar de tornar necessário que saibamos a derivada, permite obter o zero rapidamente.
- Além disso, este método tende a levar-nos para o zero mais próximo de $x$. Assim, se houver vários zeros, basta variar $x$ que eventualmente conseguiremos obter todos os zeros.

## 12.1 - Erros
- Tal como antes, vamos considerar $x^{*}$ o zero verdadeiro
- Novamente, temos a série de Taylor:
$$f(x^{*})= f(x)+ (x^{*}-x)f'(x) + \frac{1}{2}(x^{*}-x)^{2}f''(x)+\dots $$
- Mas, como $x^{*}$ é um zero, $f(x^{*})=0$. Dividindo tudo por $f'(x)$ temos:
$$x^{*}= \left[ x- \frac{f(x)}{f'(x)} \right] - \frac{1}{2}(x^{*} -x)^{2} \frac{f''(x)}{f'(x)}+\dots$$
mas, tal como definimos antes: $x' = x - \frac{f}{f'}$, logo:
$$x^{*}=x' - \frac{1}{2}(x^{*} -x)^{2} \frac{f''(x)}{f'(x)}+\dots$$
- Ora, definindo $x^{*}=x+\epsilon$ temos $\epsilon=x^{*}-x$. Analogamente, $x^{*}=x' + \epsilon'$. Juntando esta 2 equações com a de cima temos
$$\epsilon'= \left[ \frac{-f''(x)}{2f'(x)} \right]\epsilon^{2}$$
- Ou seja, o erro evolui de forma **quadrática**: $\epsilon\to \epsilon^{2}$. Isto é bastante mais rápido que os métodos de relaxação e binary search. Na prática isto quer dizer que se o erro inicial for $\epsilon_{0}$ e se tivermos $\frac{-f''(x)}{2f'(x)}\approx~constante~=c$, então após $N$ iterações o erro será $\epsilon\approx (c \epsilon_{0})^{2^{N}}$. Ou seja, será a *exponencial de uma exponencial*.

### 12.1.1 - Erros, mas útil
- No entanto, na prática não precisamos de fazer derivadas.
- Temos que $x^{*}=x+\epsilon$ e $x^{*}=x'+\epsilon'=x'+c \epsilon^{2}$ (conforme a fórmula do erro teórico). Ao igualar as 2 equações temos:
$$\begin{align*}
x+\epsilon&= x' + c \epsilon^{2}\\
x' - x &= \epsilon-c \epsilon^{2}\\
x' - x &= \epsilon(1-c \epsilon) \approx \epsilon
\end{align*}$$
- Ou seja, para saber o erro de uma tentativa $x$ basta ver a ***distância para a tentativa seguinte***, $x'$.
- Outra forma de interpretar isto é ver que este método converge tão rápido que a próxima tentativa já é tão boa que basicamente já é o zero.
- Por outro lado, para obter o erro em $x'$ precisamos de fazer a iteração anterior.

## 12.2 - Problemas
1. Para usar este método temos que saber a derivada $f'$
2. O método nem sempre converge.
    - Isto pode acontecer por a derivada ser muito baixa e então ao fazer $x' = x - \frac{f}{f'}$ apenas nos estamos a afastar do zero.
    - Por outro lado podemos ter um caso como na figura abaixo em que a derivada no ponto em que estamos apontar para o lado oposto ao zero:
![[newton raphson 2.png]]

#computacional #programacao 
