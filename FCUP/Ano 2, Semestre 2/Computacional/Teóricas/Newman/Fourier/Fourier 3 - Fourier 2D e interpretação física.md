# 3 - Transformadas de Fourier em 2D
- Consiste em fazer uma transformada de Fourier de uma função $f(x,y)$. Na prática, fazemos tranformada para *uma variável de cada vez*.

- Consideremos que temos uma grelha $M\times N$ de sample points.
- Começamos por fazer uma transformada para cada uma das $M$ colunas, tendo:
$$c_{ml}' = \sum\limits_{n=0}^{N-1} y_{mn} \exp \left(-i \frac{2\pi ln}{N} \right)$$
sendo que, na equação acima: estamos na coluna $m$, que tem $N$ coeficientes, um para cada valor $l$.

- A seguir pegamos no coeficiente $l$ de cada coluna $m$ e fazemos a sua transformada de Fourier tendo:
$$c_{kl}=\sum\limits_{m=0}^{M-1} c_{ml}' \exp \left( -i \frac{2\pi km}{M} \right)$$
- Ao juntar as 2 equações numa só temos:
$$c_{kl} = \sum\limits_{m=0}^{M-1}\sum\limits_{n=0}^{N-1} y_{mn} \exp \left[-i2\pi \left( \frac{km}{M} + \frac{ln}{N} \right) \right]$$
e, alternativamente:
$$y_{mn}= \frac{1}{MN} \sum\limits_{m=0}^{M-1}\sum\limits_{n=0}^{N-1} c_{kl} \exp \left[i2\pi \left( \frac{km}{M} + \frac{ln}{N} \right) \right]$$

- Novamente, se todos os $y_{mn}$ forem reais, podemos fazer aquilo de apenas determinar metade dos coeficientes para a parte de $N$, porque os restantes serão os conjugados.

# 4 - Significado Físico das Transformadas de Fourier
- Na realidade, a transformada de Fourier de uma certa função divide-a numa componente real e numa imaginária.
- Além disso, cada termo das somas que nos dão $f(x)$ representa uma onda. Ou seja, apenas estamos a somar várias ondas, em que cada uma tem um peso diferente (dado pelos coeficientes).
- Consideremos que se tem um conjunto de dados que representam um audio com frequência constante, mas com ruído. Se determinarmos os coeficientes, verificaremos que aquele com o maior módulo corresponde à frequência do sinal. Teremos muitos coeficientes com valores mais reduzidos e aparentemente aleatórios, que são causados pela existência de ruído.

#computacional #programacao #fourier
