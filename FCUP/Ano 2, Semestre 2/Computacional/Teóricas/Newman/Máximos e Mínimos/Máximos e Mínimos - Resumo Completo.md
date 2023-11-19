- Problemas em que precisamos de obter máximos e mínimos aparecem frequentemente na física.

- De recordar que uma função pode ter vários mínimos com diferentes valores. Assim, definimos _mínimo absoluto_ como sendo o menor mínnimo e os restantes como _mínimos locais_ (sendo que podemos ter vários mínimos absolutos, se houverem vários pontos com o mesmo valor). 

- Uma forma de obter os mínimos/máximos de uma função $f(x_{1},x_{2},\dots,x_{N})$ é igualar a sua derivada a zero. Ou seja: $$\frac{\partial f}{\partial x_{i}}=0 \quad \quad;\quad \textsf{para todos os }i\in[1,N]$$
- No entanto, sem sempre podemos fazer a derivada de uma função, porque aquilo de que queremos saber o máximo ou mínimo pode apenas ser um conjunto de dados e não uma função.

# 1 - Golden Ratio Search
- Para funções de 1 variável.
- Consegue encontrar os máximos e mínimos, mas não nos diz se são locais ou absolutos.
- A lógica é semelhante à do método de binary search.
![[golden ratio.png]]
- Basicamente, se pelo menos $f(x_{2})$ ou $f(x_{3})$ for menor que $f(x_{1}),f(x_{4})$, então temos necessariamente pelo menos 1 mínimo entre $f(x_{1}),f(x_{4})$
- Podemos diminuir o intervalo ao observar $f(x_{2}),f(x_{3})$. Se $f(x_{2})<f(x_{3})$ então temos o mínimo entre $f(x_{1}),f(x_{3})$. Caso contrário, o mínimo está entre $f(x_{2}),f(x_{4})$.
- Assim, ficamos com os 3 pontos que pertencem ao intervalo que pode conter o mínimo, conforme vimos acima. Acrescentamos um 4º ponto e repetimos até ficar com um intervalo menor do que a nossa precisão desejada.

- Ora, na prática precisamos de saber com distribuir os pontos. Tendo os 2 pontos dos extremos $x_{1},x_{4}$, colocamos $x_{2},x_{3}$ distribuídos simetricamente em relação ao centro. Ou seja: $x_{2}-x_{1}=x_{4}-x_{3}$
- No entanto, devemos recordar que ao passar para o passo seguinte apenas iremos eliminar um dos pontos dos extremos (ou $x_{1}$ ou $x_{4}$). Ou seja, apesar de facilmente vermos que meter $x_{2},x_{3}$ muito próximos do centro vai tornar a iteração muito eficiente, também podemos ver que isto tornará a iteração seguinte muito pouco eficiente.
- Ou seja, o melhor é fazer algo intermédio: escolhemos $x_{2},x_{3}$ de modo a que fiquem a distâncias iguais do centro nas 2 iterações.

- Assim, vamos considerar que o mínimo está do lado esquerdo e que o segundo intervalo é $x_{1}\to x_{3}$. Assim, podemos definir $z$ como sendo a relação entre o comprimento dos intervalos das iterações 1 e 2:
$$z= \frac{x_{4}-x_{1}}{x_{3}-x_{1}}= \frac{x_{2}-x_{1}}{x_{3}-x_{1}}+1$$
e a relação entre os intervalos das iterações 2 e 3 será: $$z'=\frac{x_{3}-x_{1}}{x_{2}-x_{1}}$$
- No entanto, o nosso objetivo é descobri quais os $x_{2},x_{3}$ que nos dão eficiencia igual em todas as iterações. Assim: $z=z'$. Como $z=1/z'+1$ temos:
$$z=\frac{1}{z'}+1\longrightarrow z=\frac{1}{z}+1\longrightarrow z^{2}-z-1=0 \Longrightarrow z = 1.618\dots$$
- E, tal como poderíamos esperar pelo nome do método, obtemos o ***Golden Ratio***.

## 1.1 - Aplicação:
1. Escolher os valores dos extremos do intervalo $x_{1},x_{4}$ e definir a precisão que queremos, $\epsilon$. Usar golden ratio para obter $x_{2},x_{3}$. Basicamente $x_{3}=\frac{1}{z}(x_{4}-x_{1})$ e $x_{2}=x_{1}+(x_{4}-x_{3})$
2. Calcular a imagem de cada ponto, $f(x_{i})$. Verificar se, pelo menos, ou $f(x_{2})$ ou $f(x_{3})$ é menor que $f(x_{1})$ **e** $f(x_{4})$. Se não for o caso, mudar o intervalo.
    1. Se $f(x_{2}) < f(x_{3})$, o mínimo estará em $[x_{1},x_{3}]$. $x_{3}$ passa a ser $x_{4}'$, $x_{2}$ passa a ser $x_{3}'$ e $x_{1}$ passa a ser $x_{1}'$. Obtemos $x_{2}'$ da mesma forma que antes. 
    2. Se $f(x_{2}) > f(x_{3})$, o mínimo estará em $[x_{2},x_{4}]$. $x_{2}$ passa a ser $x_{1}'$, $x_{3}$ passa a ser $x_{2}'$ e $x_{4}$ passa a ser $x_{4}'$. Obtemos $x_{3}'$ da mesma forma que antes. 
3. Se o intervalo da iteração seguinte for maior do que a precisão desejada ($x_{4}'-x_{1}' > \epsilon$), voltar ao ponto 2. Senão, $\frac{1}{2}(x_{2}'+x_{3}')$ será a nossa aproximação final do mínimo

## 1.2 - Problemas
- Tal como Binary Search, o intervalo que escolhemos tem que conter o mínimo/máximo. Usar as mesmas técnicas para escolher o intervalo. Pode ser preciso tentativa e erro.
- Só podemos mesmo usar para funções de 1 variável.

# 2 - Método de Gauss-Newton
- Tal como já vimos, nós temos máximos e mínimos quando $f'(x)=0$. Ou seja, estes pontos não passam de *zeros da derivada*. Assim, temos o método de Newton:
$$x'=x- \frac{f'(x)}{f''(x)}$$
- Assim, tal como o método Newton-Ralphson, isto permite-nos obter máximos e mínimos de forma rápida, até para 2+ variáveis.
- MAS, só podemos usar isto quando conhecemos a função e a podemos derivar. Mas, tal como já disse muitas vezes, é comum termos apenas um conjunto de dados.


# 3 - Descida do Gradiente
- Consideremos que conseguimos fazer a 1ª derivada  num certo caso, mas não a 2ª. Podemos fazer a seguinte aproximação:
$$x'=x- \gamma f'(x)$$
em que $\gamma\approx \frac{1}{f''(x)}$. De notar que $\gamma$ pode ser uma aproximação fraca, pelo que _apenas precisa de ter a ordem de grandeza certa_.
- Ora, o sinal de $\gamma$ irá decidir se convergimos em direção a um máximo ou mínimo ($\gamma>0 \to mín ~~;~~\gamma<0\to máx$)
- O módulo de $\gamma$ irá determinar como "saltamos". Ou seja, $\gamma$ maior permite-nos convergir mais rápido, mas se for demasiado rápido pode acontecer isto: 
![[descida do gradiente.png]]

- Ou seja, queremos escolher o valor de $\gamma$ de modo a converger rapidamente, mas sem overshooting.
- Idealmente $\gamma= 1/f''(x)$. Quando não podemos determinar a segunda derivada, o melhor é fazer *tentativa e erro*.

- Por vezes, nem a 1ª derivada conseguimos calcular. Aí, fazemos a seguinte aproximação:
$$f'(x_{2})\approx \frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}$$
e temos 
$$x_{3}=x_{2}-\gamma \frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}$$
- Se $\gamma$ for um bom valor, a equação acima permite-nos convergir à velocidade do método de Newton e apenas calculamos $f$ e não as derivadas.

#computacional #programacao 