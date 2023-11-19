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
