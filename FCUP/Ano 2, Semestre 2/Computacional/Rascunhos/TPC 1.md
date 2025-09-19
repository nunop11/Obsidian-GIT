- No programa abaixo determinamos os coeficientes de fourier para $f_1$, $f_{2}$ e $f_{3}$ para vários números de intervalos ($N$), utilizando a função `cn` definida no exercício 1.3
- De seguida, calculei o desvio de cada coeficiente determinado (para cada $N$, para cada função) usando a fórmula:
$$\textsf{desvio}(cn) = \frac{cn-cn_{\textsf{ teorico}}}{cn_{\textsf{ teorico}}}$$
- Recordemos que a função `cn` utiliza o método de Simpson. Assim, o seu erro não diminui linearmente com número de intervalos de integração, mas sim de forma exponencial.
- Por esta razão, os vários valores de intervalos de integração ($N$) para os quais determinei os coeficientes de Fourier ($cn$) para as 3 funções são potências de base 2. 
- No final do programa temos os gráficos de $\log(cn)$ em função de $\log(N)$. Ora, como dito acima, o erro de `cn` deveria diminuir de forma exponencial, pelo que nos gráficos de $\log(desvio)[\log(N)]$ deveriam apresentar pontos a formar uma reta.
- No entanto, podemos ver que isso não é o que acontece. 
    - No gráfico para $f_{1}$ vemos que no início (até $N\approx10^{3}$), o desvio dos coeficientes diminui de forma aproximadamente linear. Mas depois disso o desvio estabiliza e parece até aumentar ligeiramente.
    - No gráfico de $f_{2}$, o desvio é muito reduzido desde o princípio (ordem de grandez de $10^{-15}$) e aumenta consoante $N$ aumenta, mas de forma aparentemente aleatória. Parecem faltar alguns pontos.
    - O gráfico de $f_{3}$ é semelhante ao gráfico de $f_{1}$, mas como se faltassem muitos pontos no centro. Tal como no gráfico de $f_{1}$, o desvio parece aumentar ligeiramente para $N$ muito elevado.

- A partir disto podemos tirar algumas conclusões:
    - A função $f_{1}$ é a única em que o gráfico que de alguma forma segue o esperado. Isto deverá dever-se a este ser o gráfico em que o valor coeficiente é obtido de forma precisa mais lentamente e ao facto que o traçado da função $f_{1}$ ser aquele em que o valor de $y$ sobe mais lentamente.
    - Nas funções $f_{2}$ e $f_{3}$ (especialmente $f_{3}$) existem pontos em falta. Isto deve-se ao desvio nesses pontos ser $0$. Na realidade o desvio não seria exatamente zero, mas como python apenas consegue ter "floats" com até 15 ou 16 casas decimais, o valor que temos acaba por ser $0$. Deste modo, ao colocar a escala log-log, estes pontos não aparecem pois $\log(0)=-\infty$
    - Por fim, nos 3 gráficos verificamos algo que nunca seria de esperar: o desvio aumentar com o aumento de $N$. Isto poderá dever-se ao facto que, pelo menos a partir de $N=10^{2}$, em todos os gráficos temos desvios da ordem de grandeza de $10^{-15}$. Como disse acima, python só consegue manter 15 ou 16 casas decimais. Ou seja, estes desvios encontram-se no limite de precisão da linguagem de programação. Desta forma, os desvios não estão a subir, apenas vemos isso por causa de erros de aproximação do código para valores tão reduzidos.

# 2.1.a
- Para fazer uma aproximação de Fourier usei a fórmula:
$$\begin{align}
f_{N}(x)=\sum_{n=-N}^{N}c_{n}e^{ik_{n}x}.
\end{align}$$
que nos dá a imagem de um certo $x$ para uma aproximação de Fourier de ordem $N$ para a função $f(x)$

- Assim, fiz a função `apFourier` que determina o contradomínio correspondente à aproximação de Fourier, para uma função,  intervalo (domínio) e de ordem $N$ dados como argumentos. Esta função apenas aplica a fórmula acima. Para isto, temos que determinar os coeficientes de Fourier, sendo usada a função `cn` (do exercício 1.3). Ora, na função `apFourier` decidi optar por utilizar a função `cn` com "apenas" 1000 intervalos de integração, pois vimos no exercício 1.4 que a partir deste número de intervalos, os coeficientes obtidos já eram o mais próximos possíveis.

- Podemos no gráfico da parte real que, tal como esperado, a aproximação se torna rapidamente melhor, de forma que a partir de $N=16$, devido à reduzida resolução do gráfico gerado, já não é possível distinguir o gráfico teórico da aproximação.
- Podemos ver que o gráfico da parte imaginária aparenta ser apenas ruído. Isto pode dever-se a vários fatores, sendo o principal o facto que todos os valores apresentados estarem na ordem de grandeza $10^{-17}$, pelo que, mais uma vez, estamos no limite de precisão de python. Além disso, é possível que os 1000 valores de $x$ usados (assim como a resolução da imagem gerada) não serem suficientes para podermos definir suficientemente bem a rápida variação da parte imaginária do gráfico.

# 2.1.b
- No programa abaixo apena apliquei a fórmula de $D_{N}$.
- De notar que, ao definir a função que retorna $|f(x)-f_{N}(x)|$ para um certo $x$, como a integração  desta função depois é feita através de soma, basta ter o módulo desta diferença. Ter a raiz quadrada do módulo ao quadrado iria dar o mesmo valor, pelo que é desnecessário fazer isso.
- Neste programa, na função `numeradorDN` apenas se tem 100 intervalos de intregração (para fazer a integral do numerador), porque verifiquei que ao colocar, por exemplo, 1000 intervalos o tempo de execução é bastante maior e o resultado obtido é o mesmo.
---
- Neste caso, decidi fazer o gráfico com escalas log-log de base 2. Isto porque podemos ver o mesmo traçado que veríamos com log de base 10, mas temos mais detalhe no eixo dos $x$. Dito isto, podemos ver que a partir de $N\approx2^{5}=32$ o desvio da aproximação é muito reduzido, de cerca de $2^{-44}\approx10^{-15}$. A partir daí o valor do desvio parece estabilizar e até subir, mas isso deverá ser por causa de, novamente, estarmos no limite de precisão de python.
- No gráfico da parte real da aproximação de Fourier da função $f$ (exercício 2.1.a) vimos que a partir de $N=16$ já não conseguiamos distinguir o gráfico original da sua aproximação. Isso faz sentido, pois para $N\approx2^{4}$ o desvio é de cerca de $2^{-9}\approx0.02$. Apesar de não ser muito reduzido, este valor não é percetível na escala do gráfico da aproximação.

# 2.1.c
- Novamente, apenas apliquei a fórmula de $P_{M}$ no programa abaixo.
- Tal como no exercício 2.1.b, decidi colocar o gráfico com as escalas logarítmicas de base 2, para poder ver o eixo dos $x$ com mais detalhe.
---
- No gráfico de $P(M)$ vemos um traçado muito semelhante ao gráfico de $D(N)$. Isto faz sentido. $D_{N}$ indica o desvio do valor de $f(x)$ obtido por aproximação de Fourier em comparação ao valor teórico desta função. $P_{M}$ é o valor em falta na aproximação feita para que esta iguale o valor teórico. Logicamente, se faltar um maior valor à aproximação esta também terá um maior desvio. Tal como no gráfico de $D(N)$, é atingido o mínimo para $N\approx2^{5}=32$.

# 2.2
- Neste exercício repeti a análise feita função $f$ nas alíneas do exercício 2.1, mas para a função `f22`, que descreve uma função quadrada.

- No gráfico da parte real da aproximação de Fourier vemos que a função precisa de uma ordem de aproximação maior para se aproximar corretamente, de tal modo que conseguimos distinguir o traçado da função teórica das aproximações para todas as ordens testadas (de $N=1$ até $N=128$. Além disso, enquanto que não distinguíamos os traçados das aproximações a partir de $N=16$ no gráfico no exercício 2.1.a, agora conseguimos distinguir todos. 
- Vemos ainda que acima e abaixo das porções verticais da função teórica ($x=0, x=0.5, x=1$ no gráfico) temos que o traçado do valor da função teórica. Isto é o fenómeno das oscilações de Gibbs, que declara que não importa o quão grande for a ordem de aproximação da série de Fourier, teremos sempre um erros devido à função ultrapassar o valor teórico ao passar na descontinuidade.
- Na parte imaginária da aproximação de Fourier vemos um traçado muito semelhante ao do exercício 2.1.a: ruído. Este torna-se máximo nas porções verticais do gráfico.
- Os gráficos de $D(N)$ e de $P(M)$, que coloquei com escala logaritmica, apresentam um traçado linear (especialmente no gráfico de $P(M)$. Isto mostra que para esta função, ambos decrescem de forma exponencial conforme a ordem de aproximação aumenta.
- O gráfico de $D(N)$ apresenta ainda 2 picos para $N=$ e para $N=100$. Consegui verificar que estes picos se repetem consistentemente de 50 em 50, pelo que penso que este se deverá a um erro no código, mas não o consegui encontrar.
- Por fim, vemos que ambos os gráficos apresentam um traçado "em forma de serra", o que mostra que temos valores de $N$ seguidos em que $D$ e $P$ são iguais. Mais especificamente, $N=1, N=2$ têm os mesmos $P,D$, assim como $N=3,N=4$ e assim se repete. 