# 1.2
- Conforme temos no enunciado, $m\frac{d^{2}X_{i}}{dt^{2}}=-k_{i}\left(X_{i}-X_{i-1}\right)+k_{i+1}\left(X_{i+1}-X_{i}\right)$. Esta equação é equivalente à segunda lei de Newton: $$ma_{i}=\sum F_{i}$$
- Ora, para termos o sistema em equilíbrio, é necessário que a resultante das forças aplicada em cada uma das molas seja nula. Ou seja, para uma certa mola $i$ temos:
$$-k_{i}\left(X_{i}-X_{i-1}\right)+k_{i+1}\left(X_{i+1}-X_{i}\right)=0$$
- Ora, podemos substituir $i$ por alguns valores:
$$\begin{align*}
i=1 : \quad -k_{1}\left(X_{1}-X_{0}\right)+k_{2}\left(X_{2}-X_{1}\right)&= 0 \Longrightarrow  X_{1}(-k_{2}-k_{1}) + X_{2}k_{2}=0\\
i=2 : \quad -k_{2}\left(X_{2}-X_{1}\right)+k_{3}\left(X_{3}-X_{2}\right)&= 0 \Longrightarrow X_{1}k_{2} + X_{2}(-k_{3}-k_{2}) + X_{3}k_{3}=0\\
&(\dots)\\
\textsf{massa }i : \quad -k_{i}\left(X_{i}-X_{i-1}\right)+k_{i+1}\left(X_{i+1}-X_{i}\right)&= 0 \Longrightarrow X_{i-1}k_{i} + X_{i}(-k_{i+1}-k_{i}) + X_{i+1}k_{i+1}=0\\
&(\dots)\\\\
i=N-1: \quad -k_{N-1}(X_{N-1}-X_{N-2})+k_{N}(X_{N}-X_{N-1})&= 0 \Longrightarrow X_{N-2}k_{N-1} + X_{N-1}(-k_{N}-k_{N-1}) + X_{N}k_{N}=0\\
i=N : \quad -k_{N}\left(X_{N}-X_{N-1}\right)+k_{N+1}\left(X_{N+1}-X_{N}\right)&= 0 \Longrightarrow X_{N-1}k_{N} + X_{N}(-k_{N+1}-k_{N}) = -Lk_{N+1}\\
\end{align*}$$
Sendo que aqui é útil recordar que $X_{0}=0, X_{N+1}=L$ e que para $N$ massas teremos $N+1$ molas (ou seja, $N+1$ constantes de mola).
- Ora, podemos escrever isto na forma de matriz:
$$\begin{pmatrix}
-k_{1}-k_{2} &k_{2} &\dots  &\dots &\dots &\dots &\dots\\ 
k_{2} &-k_{2}-k_{3} &k_{3} &\dots &\dots &\dots &\dots\\ 
\dots &\dots  &\dots &\dots &\dots &\dots &\dots\\ 
\dots &\dots &k_{i} &-k_{i+1}-k_{i} &k_{i+1}  &\dots &\dots\\ 
\dots &\dots  &\dots &\dots &\dots &\dots &\dots\\ 
\dots &\dots &\dots &\dots &k_{N-1} &-k_{N}-k_{N-1} &k_N \\ 
\dots &\dots &\dots &\dots &\dots &k_{N} &-k_{N+1}-k_{N}
\end{pmatrix}
\begin{pmatrix}X_{1} \\ X_{2}  \\ \dots \\ X_{i} \\ \dots \\ X_{N-1} \\ X_{N}\end{pmatrix}=\begin{pmatrix} 0 \\ 0 \\ \dots  \\ 0 \\ \dots \\ 0 \\ -Lk_{N+1}\end{pmatrix}$$
- Para molas todas iguais: $k_{i}=k,\forall k$. Assim, o sistema que precisamos de resolver neste exercício é:
$$\begin{pmatrix}
-2k &k &\dots  &\dots &\dots &\dots &\dots\\ 
k &-2k &k &\dots &\dots &\dots &\dots\\ 
\dots &\dots  &\dots &\dots &\dots &\dots &\dots\\ 
\dots &\dots &k &-2k &k  &\dots &\dots\\ 
\dots &\dots  &\dots &\dots &\dots &\dots &\dots\\ 
\dots &\dots &\dots &\dots &k &-2k &k \\ 
\dots &\dots &\dots &\dots &\dots &k &-2k
\end{pmatrix}
\begin{pmatrix}X_{1} \\ X_{2}  \\ \dots \\ X_{i} \\ \dots \\ X_{N-1} \\ X_{N}\end{pmatrix}=\begin{pmatrix} 0 \\ 0 \\ \dots  \\ 0 \\ \dots \\ 0 \\ -Lk\end{pmatrix}$$

- Para isto, comecei por fazer a função `sistMolasLivre` para obter a matriz $A$ e o vetor $v$. De seguida, usei a função de eliminação de Gauss com Pivotagem do exercício 1.1 para resolver este sistema linear. A lista `x` que obtemos contém as posições de equilíbrio $X^{eq}$ das $N$ massas.

----
----
---
# 1.4 b)
No enunciado acima temos a equação de $x_i(t)$. Ora, sabemos que no instante inicial $(t=0)$ temos $v=0$. Assim podemos derivar $x_{i}(t)$:
$$\frac{dx_{i}}{dt}= \sqrt{\lambda_{\beta}}\cdot U_{i\beta}A_{\beta} \cdot e^{t \sqrt{\lambda_{\beta}}} - \sqrt{\lambda_{\beta}}\cdot U_{i\beta}B_{\beta} \cdot e^{-t \sqrt{\lambda_{\beta}}}$$
pelo que $\frac{dx_{i}}{dt}(0)=0$. Daqui temos que $$A_{\beta}=B_{\beta}=C$$
- Regressamos à equação original:
$$x_{i}(t)=U_{i\beta}Ce^{t\sqrt{\lambda_{\beta}}}+U_{i\beta}Ce^{-t\sqrt{\lambda_{\beta}}}$$
ora, vimos no exercício 1.4 a) que todos os autovalores $\lambda_{\beta}$ são negativos. Assim, $\sqrt{\lambda_{\beta}}$ será uma raíz imaginária. Deste modo podemos reorganizar a equação acima:
$$\begin{align*}
x_{i}(t)&= U_{i\beta}Ce^{it\sqrt{-\lambda_{\beta}}}+U_{i\beta}Ce^{-it\sqrt{-\lambda_{\beta}}}\\
&= 2U_{i\beta}C\cos(t\sqrt{-\lambda_{\beta}})
\end{align*}$$
- Esta é a equação do movimento das massas neste sistema livre.
- Utilizando esta equação quando $t=0$ conseguimos obter $C$:
$$C=\frac{1}{2}x_{i}(0) U_{i\beta}^{-1}=\frac{1}{2}x_{i}(0)U_{i\beta}^{T}=A_{\beta}=B_{\beta}$$
aqui devemos recordar que $U_{i\beta}$ é a matriz dos autovetores, pelo que é ortogonal e então a sua matriz inversa e a sua matriz transposta são iguais.
<br>
- Assim, no código abaixo apenas defini valores de `xx0` (desvios aleatórios iniciais de $N$ massas, conforme o enunciado), e utilizei os mesmos parâmetros (constantes de mola, matriz `A`, autovalores, etc) da alínea anterior. De seguida utilizei a equação acima para obter uma lista que contém as constantes pretendidas, para cada modo normal $\beta$.
- Até ao fim deste TPC irei chamar às constantes $C=A_\beta=B_\beta$ de `ABβ`

# 1.4 c)
- Neste exercício utilizei os mesmos `kk` da alínea 1.4a) e os `ABβ, xx0` obtidos na alínea da alínea 1.4b). Comecei por definir os parâmetros iniciais deste problema, que são um array de tempos `tt` e um array com as posições de equilíbrio das $N$ massas: `xEq`. De seguida, apenas utilizei a equação obtida na alínea 1.4.b): 
$$x_{i}(t)=2U_{i\beta}A_{\beta}\cos(t \sqrt{-\lambda_{\beta}})$$
- No entanto, isto dá-nos as posições das massas em relação à sua posição de equilíbrio, mas neste exercício queremos um gráfico da posição das massas em função do tempo: $X_{i}(t)$. Para isso, a todas as posições obtidas com a equação acima para uma massa $i$ acrescentamos a posição de equilíbrio dessa massa.
<br>
Temos o resultado obtido no primeiro gráfico. Representei as posições de equilíbrio das massas com as linhas horizontais cinzentas. Podemos ver que todas as massas oscilam em volta da sua posição de equilíbrio, como esperado. No entanto, uma vez que estamos a usar constantes de mola e posições iniciais aleatórias, em algumas iterações temos massas a atravessarem-se umas às outras (no gráfico, vemos linhas a interesetarem-se), o que é fisicamente impossível. Isto deve-se ao facto que no nosso modelo não temos nenhum fator que impessa isto de ocorrer.
<br>
Como o primeiro gráfico depende de 2 conjuntos de valores aleatórios, nem sempre obtemos um gráfico $X_i(t)$ conclusivo. Assim, para podermos sempre verificar se os resultados estão corretos, decidi fazer 2 gráficos extra. Eles são obtidos da mesma forma do anterior, utilizando todas as mesmas constantes, exceto as posições iniciais `xx0` que não coloquei aleatórias, mas sim representativas de 2 casos bastante intuitivos.
No gráfico 2 temos o cenário em que as massas têm deslocamentos lineares e simétricos em relação ao centro (ou seja, a massa mais próxima da parede $x=L$ terá um deslocamento da posição de equilíbrio de $\frac{1}{N+1}$ e a massa mais próxima da parede $x=0$ terá deslocamento de $- \frac{1}{N+1}$). Ora, facilmente vemos que as massas descrevem um movimento tipo "acordeão". Neste caso temos $N=10$ massas, mas se tivessemos um número ímpar de massas, veríamos que a massa central teria um deslocamento inicial nulo e que, ao longo do tempo se iria mover relativamente pouco. Se as massas tivessem constante iguais, a massa central não se iria mover de todo.
No gráfico 3 temos o caso em que todas as massas têm um deslocamento inicial de $\frac{1}{2N+1}$. Neste caso, vemos que as massas oscilam aproximadamente em conjunto, sendo que as massas mais junto das paredes se movem menos. Isto está dentro do que esperaríamos!