## Progressão aritmética
$$a_{n+1}=a_{n}+r$$
$$a_{n}=a_{0}+nr$$
Soma dos $M$ primeiros termos:
$$S_{M}=\frac{a_{0}+a_{M-1}}{2}\cdot M$$
- Ao calcular termos em python, a forma recursiva pode ser útil, ao contrário de em matemática.
- Em vez de calcular todos os termos um a um com a formula geral de $a_n$, é mais eficiente usar um loop e ir somando $r$

## Progressão Geométrica
$$a_{n+1}=r \cdot a_{n}$$
$$a_{n}=a_{0}\cdot r^{n}$$
Soma dos $M$ primeiros termos:
$$S_{M}=a_{0}\frac{1-r^{M}}{1-r}$$
- Ao calcular termos em python, a forma recursiva pode ser útil, ao contrário de em matemática.
- Em vez de calcular todos os termos um a um com a formula geral de $a_n$, é mais eficiente usar um loop e ir multiplicando por $r$

## Séries de Taylor
$$e^{x}=\sum\limits_{n}^{\infty}\frac{x^{n}}{n!}$$
Temos então $\LARGE a_{n}=\frac{x^{n}}{n!}$, de onde obtemos:
$$\frac{a_{n+1}}{a_{n}}=\frac{\frac{x^{n+1}}{(n+1)!}}{\frac{x^{n}}{n!}}=\frac{x}{n+1}$$
$$\Large a_{n+1}=\frac{x}{n+1}a_{n}$$

#apontamentos 
