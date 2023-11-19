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

#computacional #programacao #integrais 
