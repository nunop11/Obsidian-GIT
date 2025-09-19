# 13 - Método da Secante
- Como vimos, o método de Newton exige ter uma função para a derivada de $f$
- No entanto, isto nem sempre é possível. Assim, podemos "adaptar" o método de Newton, usando conhecimentos do capítulo de derivadas.

1. Começamos com os pontos $x_{1},x_{2}$, que escolhemos. Ao contrário de binary search, não precisa de estar um de cada lado do zero.
2. Calculamos uma aproximação da derivada em $x_{2}$: $$f'(x_{2})\approx \frac{f(x_{2})-f(x_{1})}{x_{2}-x_{1}}$$
3. Aplicamos o método de Newton ($x_{2}=x_{1}-f(x_{1})/f'(x_{1})$) com esta aproximação da derivada: $$x_{3}=x_{2}-f(x_{2}) \frac{x_{2}-x_{1}}{f(x_{2})-f(x_{1})}$$
4. Repetir como no método de Newton.

- Ora, de notar que neste método precisamos de usar as *duas últimas tentativas*, ao contrário de usar apenas a última no método de Newton.

#computacional #programacao 
