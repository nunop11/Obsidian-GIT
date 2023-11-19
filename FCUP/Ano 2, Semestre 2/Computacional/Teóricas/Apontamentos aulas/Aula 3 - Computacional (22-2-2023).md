# Exponencial taylor
$$\exp(x)=\sum\limits_n^{+\infty}\frac{x^n}{n!}$$
- Podemos fazer os termos todos um a um e somar. Mas é menos eficiente:
![[Fatorial e expansao taylor de exponencial.png]]
- Mas podemos definir a série $x_n$ assim:

$$x_n = \frac{x^n}{n!}=\frac{x_{n+1}}{x_n}=\frac{\frac{x^{n+1}}{(n+1)!}}{\frac{x^n}{n!}}=\frac{x}{n+1}$$
Sendo que temos então uma série recursiva:
$$a_{n+1}=a_n\cdot \frac{x}{n+1}$$
- Pelo que podemos fazer o seguinte programa, muito mais eficiente:
![[Expansao taylor de exponencial mais eficiente.png]]

# Gráfico
- Por exemplo, para fazer um gráfico a comparar as 2 fazemos:
![[Gráfico a comparar exponencial com a sua expansão taylor.png]]

# Numpy array
- Define-se como
` a = np.array([1,2,3,4]) `

- Basicamente são listas (podemos usar indices e `for i in a:`), mas podemos fazer operações mais simples:
    - `a = a + 1` acrescenta 1 a todos os termos
    - `a = a ** 2` mete todos os termos ao quadrado
    - `b = a[0:2] * 4` faz lista que tem os 2 primeiros termos vezes 4

- Se quisermos que a função `exp_taylor2` acima funcione com np arrays:
![[calcular expansao em taylor da exponencial com np array.png]]

#apontamentos #programacao