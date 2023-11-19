# Integrais
- Antes de mais, temos que:
$$\int_{a}^{b} f(x) \,dx = \lim_{M\to\infty} \sum_{n=0}^{M-1} f(a + n \frac{b-a}{M})\frac{b-a}{M} = F(b) - F(a)$$
sendo $F$ uma primitiva de $f$.
- Temos uma função $f$ que queremos integrar de $a$ a $b$. Assim:
$$I(a,b)=\int_{a}^{b}f(x)dx$$

## 1 - Regra do Retângulo
- Ora, esta é a área da curva por baixo de $f$.
![[integral retangulos.png]]
- Uma forma comum de calcular isto com computador é dividir a área em muitos retângulos como se pode ver acima. Mas isto não é a melhor aproximação.

## 2 - Regra do Trapézio
![[integral trapezio.png]]
- Dividimos o intervalo $[a,b]$ em $N$ fatias.
- Cada trapézio terá
    - Espessura $\Large h = \frac{b-a}{N}$
    - A parede da direita do trapézio $k$ está na abcissa $x=\Large a+kh$
    - A parede da esquerda do trapézio $k$ está na abcissa $x=a+kh-h=\Large a+(k-1)h$
    - A área do trapézio $k$ será então: $$A_{k}=\frac{1}{2}h [f(a+(k-1)h) + f(a+kh)]$$
> De recordar que a área de um trapézio de altura $h$ e lados paralelo $a, b$ é $$A = \frac{a+b}{2}h$$

- Obtemos então a integral ao somar estas $N$ áreas:
>$$I(a,b)\approx \sum\limits_{k=1}^{N} A_{k}=h \left[ \frac{1}{2}f(a)+ \frac{1}{2}f(b) + \sum\limits_{k=1}^{N-1}f(a+kh)\right] $$
- Maiores valores de $N$ irão dar erros menores.

## 3 - Regra de Simpson
- A regra do trapézio é simples e fácil, mas para ser precisa é necessário fazer muitas iterações. Assim, às vezes não é eficiente o suficiente. Assim, usamos outros métodos, tal como a regra de simpson.
![[integral simpson.png]]
- Este método consiste em encaixar quadráticas. Para definir uma quadrática precisamos de 3 pontos. Assim, pegamos em 2 trapézios seguidos e usamos os 3 pontos que os definem para encaixar uma quadrática. Ao calcular a área sob estas quadráticas obtemos a integral.

- Peguemos no exemplo da imagem acima. Na quadrática 1 temos 3 pontos, que podemos definir como tendo $x=0, x=-h, x=h$. Temos
$$\begin{cases}
f(0)=C \\
f(h)=Ah^{2}+Bh+C \\
f(-h)=Ah^{2}-Bh+C
\end{cases}$$
Ao resolver o sistema temos:
$$\begin{align*}
A&= \frac{1}{h^{2}} \left[\frac{1}{2}f(-h) - f(0) + \frac{1}{2}f(h) \right]\\
B&= \frac{1}{2h}[f(h)-f(-h)]\\
C&= f(0)
\end{align*}$$
A área da por debaixo da quadrática 1 será então:
>$$\int_{-h}^{h}(Ax^{2}+Bx+C)dx=\frac{2}{3}Ah^{3}+2Ch=\frac{1}{3}h[f(-h)+4f(0)+f(h)]$$

- Na prática, para aplicar esta regra, dividimos a função em muitas quadráticas e somamos a área sob cada uma para obter a área total AKA integral.

- Assim, tendo a integral entre $x=a,~x=b$, tem-se que a primeira quadrática é definida por ponto de abcissa: $x=a ~;~ x=a+h ~;~ x=a+2h$. A segunda quadrática será definida pelos em $x=a+2h ~;~ x=a+3h ~;~ x=a+4h$
- Temos então a integral completa:
$$\begin{align*}
I(a,b)&\approx \frac{1}{3}h[f(a)+4f(a+h)+f(a+2h)] + \\
&+ \frac{1}{3}h[f(a+2h)+4f(a+3h)+f(a+4h)] + \dots\\
&+ \frac{1}{3}h[f(a+(N-2)h)+4f(a+(N-1)h)+f(b)]\\
&= \frac{1}{3}h[f(a)+4f(a+h)+2f(a+2h)+4f(a+3h)+\dots+f(b)]\\
&= \frac{1}{3} h\left[f(a)+f(b) + 4\sum\limits_{\substack{\text{k ímpar}\\ 1~\dots ~N-1}}f(a+kh) + 2\sum\limits_{\substack{\text{k par}\\ 2~\dots ~N-2}}f(a+kh)\right]
\end{align*}$$
- De recordar que, em python, podemos fazer, por exemplo, a soma dos ímpares assim: `for k in range(1,N,2):`
- Ou podemos fazer tudo com um só loop e temos:
$$I(a,b)\approx \frac{1}{3}h \left[f(a)+f(b) +4\sum\limits_{k=1}^{\frac{N}{2}} f(a+(2k-1)h) + 2\sum\limits_{k=1}^{\frac{N}{2}-1}f(a+2kh) \right]$$


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

# 6 - Métodos Adaptativos
- Até agora fizemos programas em que decidimos o número, $N$, de intervalos de integração. Ora, temos apenas escolhido números e visto o que dava. Isso funciona mas não é o mais correta.

- Desta forma, consideremos que queremos calcular um certo integral com uma certa exatidão, como "exatidão de 4 casas decimais" e queremos saber quantos intervalos calcular para obter isso.
- Presumindo que essa exatidão está dentro dos limites do Python, deverá ser possível obter essa exatidão. De notar ainda que não queremos fazer mais passos do que aqueles necessários.

- Uma forma de fazer isto é começar com um $N$ pequeno e ir duplicando até obter a exatidão desejada.
- Vimos esta fórmula na secção sobre Erros de Integrais:
$$\epsilon_{2}=\frac{1}{3}(I_{2}-I_{1}) \Longrightarrow \epsilon_{i}=\frac{1}{3}(I_{i}-I_{i-1})$$
- Ou seja, fazemo assim:
    1. Escolhemos $N_{1}=10$, pelo que $N_{2}=2N_{1}=20$. 
    2. Calculamos a integral com cada $N$ e obtemos $I_{1}, I_{2}$, respetivamente.
    3. Determinar $\epsilon_{2}$ e vemos se obtivemos um erro dentro daquilo que queremos obter em termos de exatidão (por exemplo, se temos $\epsilon<0.001$)
    4. Se não obtivemos o que queríamos, voltar a duplicar: $N_{3}=2N_{2}=40$ 
    5. Repetir sucessivamente.

**Simplificar integral**

![[metodo adaptativo.png]]

- Ora, na figura acima temos o que acontece ao duplicar o $N$. Vemos que os extremos se mantém iguais e que metade dos pontos que temos no $N_{2}$ são os mesmos que tínhamos em $N_{1}$.
- Assim, ao calcular a integral novamente com a mesma fórmula, iremos estar a recalcular termos sem necessidade para tal. 

## 6.1 - Trapézio
- Deste modo, tendo $N_{i}=2N_{i-1}$, $h_{i}=(b-a)/N_{i}$ e $h_{i}=\frac{1}{2}h_{i-1}$, então:
$$\begin{align*}
I_{i}&= h_{i}\left[\frac{1}{2}f(a)+ \frac{1}{2}f(b) +\sum\limits_{k=1}^{N_{i}-1} f(a+kh_{i}) \right]\\
&= h_{i}\left[\frac{1}{2}f(a)+ \frac{1}{2}f(b) +\sum\limits_{\substack{k~~par\\2\dots N_{i}-2}} f(a+kh_{i}) +\sum\limits_{\substack{k~~impar\\2\dots N_{i}-1}} f(a+kh_{i})\right]\\
&= h_{i}\left[\frac{1}{2}f(a)+ \frac{1}{2}f(b) +\sum\limits_{k=1}^{\frac{N_{i}}{2}-1} f(a+2kh_{i}) +\sum\limits_{\substack{k~~impar\\2\dots N_{i}-1}} f(a+kh_{i})\right]\\
\end{align*}$$
- Mas temos que $N_{i}/2=N_{i-1}$ e que $2h_{i}=h_{i-1}$ logo:
$$h_{i}\left[\frac{1}{2}f(a)+ \frac{1}{2}f(b) +\sum\limits_{k=1}^{\frac{N_{i}}{2}-1} f(a+2kh_{i}) \right]=\frac{1}{2}h_{i-1} \left[ \frac{1}{2}f(a) + \frac{1}{2}f(b) + \sum\limits_{k=1}^{N_{i-1}-1}f(a+kh_{i-1}) \right]=\frac{1}{2}I_{i-1}$$
porque facilmente vemos que o segundo termo é apenas a fórmula de uma integral com a regra do trapézio.
- Assim temos:
$$I_{i}=\frac{1}{2} I_{i-1} + h_{i} \sum\limits_{\substack{k~~impar\\ 1\dots N_{i}-1}}f(a+kh_{i})$$
- Ou seja, nunca calculamos nenhum termo 2 vezes e poupamos assim muitos cálculos.
- Para fazer a soma dos termos ímpares podemos fazer:
    - `for k in range(1,N,2)`
    - `ff[1:-1:2]`

## 6.2 - Simpson
- De forma análoga ao que tínhamos acima, para Simpson temos:
$$\epsilon_{i}=\frac{1}{15}\left( I_{i}-I_{i-1} \right)$$
- A fórmula ao que tínhamos para $I_{i}$ com a regra do trapézio é, para simpson:
$$\begin{align*}
S_{i}&= \frac{1}{3}\left[ f(a)+f(b)+2 \sum\limits_{\substack{k~~par\\2\dots N_{i}-2}}f(a+kh_{i})  \right]\\
T_{i} &= \frac{2}{3} \sum\limits_{\substack{k~~impar\\1\dots N_{i}-1}}f(a+kh_{i})
\end{align*}$$
- Conseguimos demonstrar que $\large S_{i}=S_{i-1}+T_{i-1}$ e temos:
$$I_{i}=h_{i}(S_{i}+2T_{i})$$
- Na prática, ao determinar as integrais o que fazemos é:
    1. Para um certo $N_{1}$, determinar $S_{1}, T_{1}, I_{1}$ com as fórmulas acima e verificar se o erro está dentro do que queremos em termos de precisão.
    2. Se não estiver, passar para $N_{2}=2N_{1}$. Temos $S_{2}=S_{1}+T_{1}$. Determinar $T_{2}$ com a fórmula. Temos $I_{2}=h_{2}(S_{2}+2T_{2})$
    3. Repetir até ter o erro desejado.

- Mais abstratamente
    1. Para um certo $N_{1}$, determinar $S_{1}, T_{1}, I_{1}$ com as fórmulas acima
    2. Para um certo $N_{i}$ :
        - $S_{i}=S_{i-1}+T_{i-1}$, que obtivemos antes
        - Calcular $T_{i}$ com a fórmula
        - Temos que $I_{i}=h_{i}(S_{i}+2T_{i})$

- Aqui também poupamos passos porque em cada caso fazer apenas 1 loop: para calcular $T_{i}$.





# 7 - Método de Romberg
- Vimos acima que, para a _Regra do trapézio_, $I=I_{i}+ch_{i}^{2}+O(h_{i}^{4})$, de onde temos que $\epsilon_{i}=ch_{i}^{2}$, pelo que $$ch_{i}^{2}=\frac{1}{3} (I_{i}-I_{i-1})$$
- Ao juntar as 2 equações acima temos:
$$I=I_{i}+ \frac{1}{3}(I_{i}-I_{i-1})+O(h_{i}^{4})$$
vemos que esta fórmula é exata até $h^{4}$ (porque desprezamos os termos a partir daí) e que apenas precisamos de ir buscar a integral que calculamos antes ($I_{i-1}$). Ora, isto é relativamente fácil e assim obtivemos um integral com o mesmo nível da regra de Simpson, sendo que partimos do trapézio.

- Podemos então generalizar:
$$\begin{align*}
R_{i,1} &= I_{i}\\
R_{i,2} &= I_{i} + \frac{1}{3}(I_{i}-I_{i-1})\\
&\quad logo \quad \\
R_{i,2} &= R_{i,1}+ \frac{1}{3}(R_{i,1}-R_{i-1,1})
\end{align*}$$

- Ou seja, $I = R_{i,2}+ O(h_{i}^{4})$. Mas podemos aumentar o número de termos e temos:
$$I = R_{i,2} + c_{2}h_{i}^{4}+ O(h_{i}^{6})$$
send que $c_{2}\neq c$ é uma constante e que agora os termos que "ignoramos" são de $h^{6}$ para cima.
- Repetindo a mesma análise que fizemos acima temos:
$$I= R_{i-1,2}+c_{2}h_{i-1}^{4} + O(h_{i-1}^{6})=R_{i-1,2}+ 16c_{2}h_{i}^{4} + O(h_{i}^{6})$$
aqui temos que $h_{i-1}=2h_{i}$, tal como tínhamos no método *adaptativo*. Temos ainda que, como ignoramos estes termos, $O(h_{i-1}^{6})=O(h_{i}^{6})$

- Podemos igualar as 2 equações de $I$:
$$\begin{align*}
R_{i,2} + c_{2}h_{i}^{4}+ O(h_{i}^{6})&=  R_{i-1,2}+ 16c_{2}h_{i}^{4} + O(h_{i}^{6})\\
c_{2}h_{i}^{4}&= \frac{1}{15}(R_{i,2}-R_{i-1,2})+ O(h_{i}^{6})
\end{align*}$$
- Ora, tínhamos $I = R_{i,2}+ O(h_{i}^{4})$, logo agora temos:
$$I = R_{i,2} + \frac{1}{15}(R_{i,2}-R_{i-1,2}) + O(h_{i}^{6})$$
temos agora então uma integral calculada com exatidão até à 6ª casa decimal.
- Ora, podemos continuar a repetir este processo e, assim, ir aumentando o expoente do erro: $h^{8},h^{10},\dots$
- Assim, sendo $R_{i,m}$ uma aproximação de ordem $i$ (em cada ordem duplicamos o número de intervalos), teremos uma exatidão de ordem $h^{2m-1}$ e um erro de ordem $h^{2m}$. Assim:
$$\begin{align*}
I &= R_{i,m} + c_{m}h_{i}^{2m} + O(h_{i}^{2m+2})\\
I &= R_{i-1,m} + c_{m}h_{i-1}^{2m} + O(h_{i-1}^{2m+2})=R_{i-1,m}+4^{m}c_{m}h_{i}^{2m}+O(h_{i}^{2m+2})
\end{align*}$$
(aqui usamos as mesmas técnicas que usamos acima, ao obter a equação com $O(h^{6})$)
- Ao igualar as 2 equações temos a equação do erro:
$$c_{m}h_{i}^{2m}= \frac{1}{4^{m}-1} (R_{i,m}-R_{i-1,m}) + O(h_{i}^{2m+2})$$
onde temos:
$$R_{i,m+1}= R_{i,m} + \frac{1}{4^{m}-1} (R_{i,m}-R_{i-1,m}) \quad \quad \textsf{(Eq. 1)}$$

## 7.1 - Na prática
1. Calcular as 2 primeiras tentativas, com a _regra do trapézio_: $I_{1}=R_{1,1}$ e $I_{2}=R_{2,1}$
2. Usando a Eq.1, determinar $R_{2,2}$
3. Duplicar novamente o número de intervalos, usar a regra do trapézio e temos $I_{3}=R_{3,1}$. Usar novamente a Eq.1 para obter $R_{3,2}$ e $R_{3,3}$
4. Para cada $R$ que calculamos, podemos determinar o erro e, assim, decidir parar conforme se já cumprimos o objetivo ou não.

![[romberg.png]]
- Na prática temos isto. Cada linha é um $i$ diferente e numa ordem $n$ podemos ir até $R_{n,n}$. De notar que a fórmula do erro acima permite obter o erro de todos os termos menos do último termo de cada linha. Assim, presumimos que o último termo é a nossa melhor aproximação e que o seu erro será pelo menos igual ao do penúltimo termo.

- De notar que ao fazer isto, no último termo ficamos com uma série de potências de base $h$. Ora, é importante/melhor se essa série convergir rapidamente. Se isto não acontecer (função mal comportada, flutuações, singularidades ou se conter ruído) então é melhor usar o método adaptativo.

# 8 - Aproximações Polinomiais Superiores
- Anteriormente vimos como podemos resolver integrais com o método de Simpson e do Trapézio em que, respetivamente, aproximavamos a função a uma quadrática com 3 pontos e a uma reta com 2.
- Ora, podemos fazer esta mesma técnica, mas usar $N$ pontos para definir um polinómio de ordem $N-1$. Temos:
$$\int_{a}^{b}f(x)dx\approx \sum\limits_{k=1}^{N}\omega_{k}f(x)$$
- Se fizermos a dedução temos:
![[integrais aprox polinomiais.png]]

- No entanto, se uma certa função for um polinómio de ordem $N-1$, uma "aproxímação" com um polinómio dessa ordem não será uma aproximação, será mesmo a integral.

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

# 10 - Como escolher o método
***Regra Geral :*** Integração de Romberg e Quadratura Gaussiana são os melhores métodos para integrar funções "bem comportadas" e suaves. Caso contrário, usar Simpson ou Trapézio. Isto porque apenas avaliamos funções nos sample points e nos métodos mais simples é muito mais eficiente aumentar o $N$.

Agora, um a um: 
- **Trapézio**
    - Eficiente mas menos exato
    - Bom para dados recolhidos na prática, funções "mal-comportadas" e dados com ruído.
    - Versão adaptativa pode ser útil.

- **Simpson**
    - Mais exatidão com os mesmos pontos que a Regra do Trapézio
    - Pode causar problemas ao usar com dados com ruído ou funções mal comportadas

- **Romberg**	
    - Melhor método com pontos de espaçamento uniforme.
    - Mau para funções que variem muito rápido, com ruído ou com singularidades. Isto porque este método usa muito poucos pontos.

- **Quadratura Gaussiana**
    - Muito exato com poucos pontos, mau para funções que variem muito rápido ou com ruído (semelhante a Romberg)
    - O método mais exato. Pode ser pouco eficiente.
    - O facto de usar pontos espaçados de forma não uniforme pode ser um problema.

# 11 - Integrais em Intervalos Infinitos
- Os métodos que conhecemos não funcionam numa integral assim. Ora, a solução é simplesmente **trocar de variáveis**
- Consideremos que temos $$\int_{0}^{\infty}f(x)dx$$
a mudança de variável que fazemos é: $$z= \frac{x}{1+x}\leftrightarrow x = \frac{z}{1-z}$$ de onde temos: $$dx = \frac{1}{(1-z)^{2}}dz$$
e, assim: $$\int_{0}^{\infty}f(x)dx=\int_{0}^{1} \frac{1}{(1-z)^{2}} f \left( \frac{z}{1-z} \right) dz$$
que já sabemos fazer com qualquer método.

- Outras opções de mudanças de variável:
$$z = \frac{x}{c+x}, \forall c \quad \quad; \quad \quad z = x^{\gamma}(1+x^{\gamma}),\forall \gamma$$
- Normalmente, temos que ver qual é a melhor mudança variável, dependendo do caso.

---

- Para fazer um integral de $a$ a $\infty$ faríamos uma mudança do tipo:
$$z = \frac{x-a}{1+x-a} \leftrightarrow x= \frac{z}{1-z}+ a$$
que podemos ver como primeiro fazer a mudança $y=x-a$ e depois $z = \frac{y}{1+y}$. 
- Daqui temos:
$$\int_{0}^{\infty}f(x)dx = \int_{0}^{1} \frac{1}{(1-z)^{2}} f\left(\frac{z}{1-z} + a\right)dz$$
---

- Por outro lado, se tivermos um integral de $-\infty$ a $a$, fazemos tudo igual e no fim $z\to-z$.

---

- Para integrais de $-\infty$ a $+\infty$, dividimos o integral em 2 partes: $]-\infty,0]$ e $[0, +\infty[$. Ou então dividimos de $-\infty$ a $a$ e daí a  $+\infty$.
- Podemos ainda fazer 1 só substituição:
$$x = \frac{z}{1-z^{2}} \Longrightarrow dx= \frac{1+z^{2}}{(1-z^{2})^{2}}dz$$
de onde temos:
$$\int_{-\infty}^{+\infty}f(x)dx = \int_{-1}^{1} \frac{1+z^{2}}{(1-z^{2})^{2}} f\left(\frac{z}{1-z^{2}}\right) dz$$
- Outra possibilicadade seria: 
$$x = \tan z\Longrightarrow dx = \frac{1}{\cos^{2}z} dz$$
de onde temos:
$$\int_{-\infty}^{+\infty} f(x)dx = \int_\frac{-\pi}{2}^{\frac{+\pi}{2}} \frac{1}{\cos^{2}z} f(\tan z) dz$$


# 12 - Integrais Múltiplos
- Consideremos o integral: $$I = \int_{0}^{1}\int_{0}^{1}f(x,y)dxdy$$
de onde podemos definir $$\mathcal{F}(y)= \int_{0}^{1}f(x,y)dx$$
e, portanto, $$I = \int_{0}^{1}\mathcal{F}(y)dy$$
- Uma forma de fazer isto é usar quadratura gaussiana com $N$ pontos de $x,y$ e temos $$\mathcal{F}(y)\sim \sum\limits_{i=1}^{N}\omega_{i}f(x_{i},y)\quad;\quad I\sim \sum\limits_{j=1}^{N} \omega_{j}\mathcal{F}(y_{j})$$

- No entanto, se juntarmos as 2 fórmulas acima, temos a *Fórmula do produto de Gauss-Legendre*:
$$I\sim \sum\limits_{i=1}^{N}\sum\limits_{j=1}^{N}\omega_{i}\omega_{j}f(x_{i},y_{j})$$
- Isto meio que é a quadratura gaussiana em 2 D, em que os pesos e pontos estão distribuídos numa secção do plano $xOy$. 
- No entanto, em 2D, 3D, etc. não é tão claro quais são os melhores pontos para fazer a integração.

---- PAG 195 DO PDF ----

#computacional #programacao #integrais 