# Testes de Convergência - Resumo
1. Teste de ==divergência==. Se $\lim_{n\to\infty}a_n\neq0$, a série diverge

2. Por ==tipo==
    1. Séries geométricas - Converge se $|r|<1$, diverge se $|r|\geq1$
    2. Séries telescópicas - fazer frações parciais para obter $S_n$ e descobrir $\lim_{n\to\infty}S_n$
    3. Séries P - Converge se $P>1$, diverge se $P\leq1$

3. Teste de ==Integral==. Tendo $f(n)=a_n$, se $\int_N^\infty f(x)dx$ (integral imprópria) der um número, ou seja, convergir, então $a_n$ converge. Se a integral diverge, $a_n$ diverge. Se o limite Notas: f tem de ser Positiva, Contínua, Decrescente no intervalo escolhido.

4. Se $a_n$ é positiva e "se comporta" como outra série de que conhecemos a convergência, usar teste de ==Comparação== ou teste de ==Comparação de Limite==. Casos:
    1. Se $a_n \leq b_n$, se $b_n$ converge, então $a_n$ converge
    2. Se $a_x\geq b_n$, se $b_n$ diverge, então $b_n$ diverge
    3. Se $\lim_{n\to\infty}\frac{a_n}{b_n}$ existe e $\lim\in\mathbb R^+$ então $a_n$ e $b_n$ são ambas convergentes ou divergentes. Se $\lim=0$ e $b_n$ for convergente, ambas são convergentes. Se $\lim=\infty$ e a de baixo for divergente, então são ambas divergentes.

5. Teste de ==Séries Alternadas==. Se temos $a_n$, uma série alternada, em que $\lim_{n\to\infty}a_n=0$ E $a_{n+1}\leq a_n$ ou $f'(x)<0$ (série é decrescente), então $a_n$ *converge*.

6. Teste de ==Ratio/Razão==. Usado para factoriais e séries de potências de expoente n. Casos:
    1. $\lim_{n\to\infty}|\frac{a_{n+1}}{a_n}|<1$ então a série é abs. convergente
    2. $\lim_{n\to\infty}|\frac{a_{n+1}}{a_n}|>1$ então a série é divergente
    3. $\lim_{n\to\infty}|\frac{a_{n+1}}{a_n}|=1$ então o teste para a série é inconclusivo

7. Teste das ==Raízes==. Usado para potências de expoente n. Casos:
    1. $\lim_{n\to\infty}\sqrt[n]{|a_n|}=L<1$ então a série é abs. convergente
    2. $\lim_{n\to\infty}\sqrt[n]{|a_n|}=L>1$ então a série é divergente
    3. $\lim_{n\to\infty}\sqrt[n]{|a_n|}=1$ então o teste para a série é inconclusivo


## Quando usar:
1. Teste de divergência -> Sempre. Se $\lim\neq0$, a série diverge.
2. Séries de tipo específico -> Usar se a série é uma série P, geométrica ou telescópica
3. Teste da integral -> Podemos tentar se f for PCD nalgum intervalo
4. Comparação (e Comparação de limite) -> normalmente, quando mais nenhum teste permite saber convergência
5. Teste de séries alternadas -> Quando temos série alternada, decrescente e que passa o teste 1.
6. Teste de ratio -> Quando temos fatoriais ou $a^n$
7. Teste de raiz -> Quando temos $a^n$

#anal1 #resumo #matematica 