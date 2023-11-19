# 1 - Definição
- A definição mais comum de derivada é:
$$\frac{df}{dx}=\lim_{h\to0} \frac{f(x+h)-f(x)}{h}$$
como numa implementação computacional não podemos fazer o limite então usamos:
$$\frac{df}{dx} \approx \frac{f(x+h)-f(x)}{h}$$
- No entanto precisamos de fazer a distinção entre derivadas calculadas para a _frente_, como aquela acima, e derivadas calculadas para _trás_:
$$\frac{df}{dx}\approx \frac{f(x)-f(x-h)}{h}$$
- Basicamente, na primeira vamo-nos aproximando de $x$ por valores maiores que ele e na segunda por valores inferiores.
- Quando temos descontinuidades ou quando estamos perto do limite do domínio da função, podemos ter que escolher uma forma em vez da outra. Mas normalmente tanto dá.

## 1.1 - Erros
- Temos 2 fontes de erro:
    - Arredondamento de valores
    - O facto que não estamos mesmo a fazer uma derivada, mas apenas a aproximar-nos dela ao obter um declive.
- Ao contrário de integrais em que o erro de arredondamento é normalmente insignificante, com derivadas ambos importam.

- Começamos por fazer a expansão em Taylor de $f$ em torno de $x$:
$$f(x+h)=f(x)+hf'(x)+ \frac{1}{2}h^{2}f''(x)+\dots$$
- Se isolarmos o termo da derivada:
$$f'(x)= \frac{f(x+h)-f(x)}{h} - \frac{1}{2}hf''(x)+\dots$$
- Sendo que vemos que a "definição" de derivada que utilizamos em computacional na verdade ignora todos os termos da expansão acima da segunda derivada. Estes termos ignorados são o nosso _erro de aproximação_.
- Daqui temos que o módulo do erro de aproximação é $\frac{1}{2}h|f''(x)|$, ou seja, o erro diminui **linearmente** com $h$.

- No entanto, como vimos na ficha das TP de otimização/exatidão, ao fazermos subtrações de números decimais muito próximos obtemos *erros de arrendondamento elevados* (como vimos no exercício em que concluímos que a fórmula resolvente deve ser dividida em 2 equações, uma usada para determinar a solução $+ \frac{\sqrt{\Delta}}{2}$ e outra para determinar $-\frac{\sqrt{\Delta}}{2}$)
- Ora, ao reduzir $h$ para obter erros de aproximação menores, ficaremos com $f(x)\approx f(x+h)$, pelo que iremos obter erros de arrendondamentos elevados.

- Ora, a exatidão com que um computador consegue calcular $f(x)$ será $Cf(x)$, sendo $C$ a constante de erro ($\approx 10^{-16}$ em python). Ora, como $f(x)\approx f(x+h)$, então a exatidão com que calculamos $f(x+h)-f(x)$ será $\approx 2C|f(x)|$ (no máximo). Assim, o maior erro de arredondamento que poderemos obter ao calcular a derivada será $\large\frac{2C|f(x)|}{h}$.
- O erro de aproximação já vimos acima. Ou seja, o erro total que temos ao calcular uma derivada é:
$$\epsilon(h)= \frac{2C|f(x)|}{h} + \frac{1}{2}h|f''(x)|$$
Ora, queremos saber onde teremos _erro mínimo_. Para isto:
$$\frac{d\epsilon}{dh}=0\Longrightarrow \frac{-2C|f(x)|}{h^{2}} + \frac{1}{2}|f''(x)|=0$$
de onde temos:
$$h = \sqrt{4C \left| \frac{f(x)}{f''(x)} \right|}$$
- Ao substituir este $h$ na fórmula de $\epsilon(h)$ obtemos o erro mínimo que podemos obter ao calcular uma derivada: 
$$\epsilon_{min}=\sqrt{4C|f(x)f''(x)|}$$
- Assim, conseguimos escolher $h$ de forma a ter o menor erro.

- Regra geral, derivadas dão-nos metade da precisão dos outros cálculos que vimos até agora.

#computacional #programacao #derivada