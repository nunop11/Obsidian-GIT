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

#computacional #programacao #integrais 
