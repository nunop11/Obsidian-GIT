# 9 - Quadratura Gaussiana
- Até agora, vimos apenas métodos de integração em que os pontos que usamos para determinar a integrar, pontos de sample $x_{k}$ (não me apeteceu traduzir direito), estão distribuídos uniformemente no intervalo de integração. Ora, isso é mais fácil de programar, mas nem sempre é o melhor.
- Se, ao calcular uma integral, apenas colocarmos pontos de sample em sítios estratégicos, conseguimos obter resultados melhores e mais rapidamente.

## 9.1 - Sample Points não Uniformes
- Consideremos que temos $N$ pontos sample $x_{k}$ e que, com eles, queremos fazer a integral de $f(x)$ entre $a$ e $b$. Ou seja, queremos usar a fórmula: $$\int_{a}^{b}f(x)dx\approx \sum\limits_{k=1}^{N}\omega_{k}f(x)$$
- Esta é a fórmula geral. Para entender, basta recordar o método do trapézio. A imagem de cada sample point tinha um certo peso: $\frac{1}{2},1,1,\dots,1,1,\frac{1}{2}$.
- Ou seja, podemos definir: $$\begin{align*}
\phi_{k}(x)&=  \prod\limits_{\substack{m~=~1,\dots,N\\ m~\ne~k}} \frac{(x-x_{m})}{(x_{k}-x_{m})}\\
&= \frac{x-x_{1}}{x_{k}-x_{1}}\times\dots\times \frac{x-x_{k-1}}{x_{k}-x_{k-1}}\times \frac{x-x_{k+1}}{x_{k}-x_{k+1}}\times\dots\times \frac{x-x_{N}}{x_{j}-x_{N}}
\end{align*}$$
- A isto chamamos de **polinómio interpolador**. Vemos que, para um sample point $k$ obtemos um polinómio em função de $x$, de ordem $N-1$ e que contém fatores relacionados com todos os sample points, *exceto x_k*.
- Podemos ainda ver que:
$$\phi_{k}(x_{m})=\begin{cases}1 &; &m=k\\ 0 &; &m\ne k\end{cases}=\delta_{km}$$
- Ora, isto acaba por ser o $\omega_{k}$ da equação acima. Ou seja, temos: $$\Phi(x)=\sum\limits_{k=1}^{N} f(x_{k})\phi_{k}(x)$$
De notar que quando $x=x_{m}$, temos $\Phi(x_{m})=\sum f(x_{k})\phi(x_{m})=\sum f(x_{k})\delta_{km}=f(x_{m})$, porque para todos os outros termos teremos $\delta_{km}=0$.
- Por outras palavras, graças ao delta de kronecker, temos uma combinação linear de polinómios que encaixa na função $f(x)$ em todos os pontos $x_{k}$
- Além disso, como queremos um polinómio de grau $N$ que passe por $N-1$ pontos, este polinómio é *único*.

- Ou seja, para obter a nossa aproximação, $\Phi(x)$:
$$\int_{a}^{b}f(x)dx\approx \int_{a}^{b}\Phi(x)dx= \int_{a}^{b}\sum\limits_{k=1}^{N} f(x_{k})\phi(x)dx = \sum\limits_{k=1}^{N}f(x_{k}) \int_{a}^{b}\phi_{k}(x)dx$$
Ora isto terá que ser igual à 1ª fórmula que temos nesta secção: $\int_{a}^{b}f(x)dx\approx \sum_{k=1}^{N}\omega_{k}f(x)$ . Assim, temos necessariamente que: 
$$\omega_{k}=\int_{a}^{b}\phi_{k}(x)dx$$
- Ou seja, para cada sample point $x_{k}$ apenas integramos $\phi_{k}$, o polinómio interpolador que vimos acima.
- De notar que este polinómio e, consequentemente, estes pesos serão iguais para quaisquer função $f$ que integremos, desde que usemos os mesmos sample points.
- Além disso, se quisermos integrar uma função noutro domínio, apenas precisamos de "deslizar" ou "apertar/esticar" os samples points. De uma forma geral, se temos os pesos $\omega_{k}$ num certo domínio, para converter nos pesos de um domínio $[a,b]$, fazemos: $$\begin{align*}
  x_{k}'&= \frac{1}{2}(b-a)x_{k} + \frac{1}{2}(b+a)\\
w_{k}'&= \frac{1}{2}(b-a)\omega_{k}
\end{align*}$$

## 9.2 - Sample Points da Quadratura Gaussiana
- Na secção atrás vimos como determinar o peso de cada sample point. Mas precisamos de saber como escolher os sample points em si.
- Idealmente, queremos escolher $N$ pontos de modo que consigamos obter integrais exatos até polinómios de ordem $2N-1$. De acordo com uma dedução longa que não quis aprender, para que isso aconteça, é preciso que os $N$ pontos sejam os zeros do Polinómio de Legendre de grau $N$ ,$P_{N}(x)$, reajustado ao domínio de integração. Temos os pesos:
$$\omega_{k}=\left[ \frac{2}{1-x^{2}} \left(\frac{dP_{N}}{dx} \right)^{-2} \right]_{x=x_{k}}$$
- Para uma mesma função temos, para $N=10$ e $N=100$:
![[quadratura gaussiana.png]]
- Vemos que temos mais pontos e com menos peso nos limites do intervalo.
- De notar que nas imagens acima, e em muitas funções, calcula-se $\omega_k$ de $-1$ a $1$ por razões históricas. Depois convertemos para o nosso intervalo.


- Um exemplo de aplicação com o programa `gaussxw.py` do livro:
```
from gaussxw import gaussxw

def f(x): 
    return X**4 - 2*x + 1
    
N = 3
a = 0.0
b = 2.0

# Calculate the sample points and weights, then map them 
# to the required integration domain
x,w = gaussxw(N) 
xp = 0.5*(b-a)*x + 0.5*(b+a) 
wp = 0.5*(b-a)*W

# Perform the integration 
s = 0.0
for k in range(N): 
    s += wp[k]*f(xp[k])

print(s)
```
- Ou seja:
1. Definir o número de pontos que queremos
2. Usar alguma função para obter $x_{k}$ e $\omega_{k}$ que na prática serão listas/arrays que contém os valores e pesos de cada sample point (que para a função do livro será no intervalo $[-1,1]$)
3. Usando as fórmulas do final da secção 6.1 obtemos $x_{k}',\omega_{k}'$, os sample points e pesos no nosso intervalo $[a,b]$.
4. Apenas aplicar a fórmula do sumatório que nos dá a integral.

- Também nos materiais de apoio do livro existe a função `from gaussxw import gaussxwab` que chamamos da forma `gaussxwab(N,a,b)`. Ela dá $x_{k},\omega_{k}$ já adapatado ao nosso intervalo. De notar que se tivermos de fazer vários integrais em domínios diferentes, esta função não é boa. É muito melhor usar `gaussxw()` e depois adaptar os pontos e pesos aos intervalos.

- O programa acima, apenas com 3 pontos, determinar o integral com $100\%$ exatidão. Isto era de prever. Temos $f(x)=x^{4}-2x+1$ e $N=3$. Ora, tal como vimos, este método teria completa exatidão até polinómios de grau $2N-1=5$.

- Um defeito deste método é que, se quisermos duplicar o $N$ temos que voltar a calcular $x_{k},\omega_{k}$.

## 9.3 - Erros
- Tal como determinamos a fórmula de Euler-Maclaurin para o método do trapézio, existe uma fórmula análoga para a quadratura gaussiana. O que ela nos diz é que, se aumentarmos $N$ 1 unidade, o erro de aproximação (erro resultante de não estarmos realmente a integrar $f$, mas sim uma função aproximada) diminui um fator $c/N^{2}$. Ou seja, convergemos muito rapidamente para o valor real. Na prática isto implica que *quase nunca precisamos de mais de 100 pontos*.
- Temos de notar ainda que, para que isto funcione, a função que estamos a integrar tem que ser ***suave***. Isto porque, neste método apenas avaliamos os $N$ pontos (que normalmente são poucos). Se neles houverem imperfeições, o erro será maior.

- Se tivermos uma estimativa da integral com método de Gauss usando $N$ pontos, temos $I=I_{N}+\epsilon_{N}$. Se duplicarmos $N$ temos $I=I_{2N}+\epsilon_{2N}$. Assim: $I_{N}+\epsilon_{N}=I_{2N}+\epsilon_{2N}$. Ora, vimos que este método converge muito rapidamente, ou seja, é segura assumir $\epsilon_{2N}\ll \epsilon_{N}$. Assim:
$$\epsilon_{N}\approx I_{2N}-I_{N}$$
Ou seja, $I_{2N}$ será uma aproximação tão melhor que podemos considerar que é o valor verdadeiro da integral. 
- De notar que a fórmula de erro acima faz com que tenhamos de determinar $I_{2N}$ mas apenas nos dá o erro de $I_{N}$. Assim, fazer um programa adaptativo com quadratura gaussiana muitas vezes não é útil.

#computacional #programacao #integrais 
