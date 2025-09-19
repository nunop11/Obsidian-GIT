# 3 - Aproximações Polinomiais
- Até agora, para obter derivadas, aproximamos a função entre 2 pontos a uma reta e obtemos o seu declive.
- Ora, ao calcular integrais, na regra do trapézio também aproximavamos a função entre 2 pontos a uma reta e obtíamos a área do trapézio por baixo. No entanto, em integrais vimos que podemos fazer melhores aproximações e, assim, obter resultados melhores e mais rapidamente.

- Em integrais, começamos por aproximar a função entre 2 pontos a uma parábola e obtivemos Simpson.
- Também com derivadas podemos aproximar a função entre 2 pontos a um *polinómio* e obter a sua derivada em $x$.


## Polinómio 2º Grau
- Consideremos que queremos aproximar a função a uma quadrática $y=ax^{2}+bx+c$. Para isso, precisamos de 3 pontos. Ora, obtemos melhores resultados se usarmos: $\{x, x+h, x-h\}$.
- Por exemplo, vamos considerar $x=0, x=h, x=-h$. Temos:
$$\begin{cases} ah^{2}-bh+c=f(-h)\\ c=f(0) \\ ah^{2}+bh+c=f(h) \end{cases}$$
- No entanto, não precisamos de resolver isto. Como planeamos usar a derivada do polinómio em $x$ temos:
$$\frac{d}{dx}\left[ ax^{2}+bx+c \right]_{x=0}=\left[2ax+b\right]_{x=0} = b$$
Ou seja, _apenas precisamos de b_. Do sistema acima temos:
$$b= \frac{f(h)-f(-h)}{2h}\approx \frac{df}{dx}(x=0)$$
- Podemos generalizar isto para qualquer $x$ e temos:
$$\frac{df}{dx} \approx \frac{f(x+h)-f(x-h)}{2h}$$
- Eeeeeeeeee tanto trabalho para obter o método da Derivada ao centro para pontos a uma distância de $2h$

- No entanto, podemos fazer deduções análogas a esta para polinómios de grau superior. Este método consiste em:
    1. Definir os pontos que iremos usar (=grau + 1 (3º grau = 4 pontos))
    2. Substituir cada ponto $x_{i}$ na fórmula do polinómio e igualar a $f(x_{i})$. Isto dá-nos um sistema.
    3. Obter apenas o cpeficiente que temos a multiplicar por $x$ (num polinómio do tipo $y= \dots + ax^{2}+bx+c$ seria $b$)
    4. Esse coeficiente dá-nos a fórmula da derivada obtida ao aproximar a função a esse polinómio.

- De notar:
    - Para polinómios de grau _ímpar_ usamos pontos em "pontos médio". EX: para um polinómio de 3º grau usaríamos: $x=- \frac{3}{2}h, -\frac{1}{2}h, \frac{1}{2}h, \frac{3}{2}h$.
    - Para polinómios de grau _par_ usamos pontos "pontos inteiros". EX: para um polinómio de 4º grau usaríamos: $x=-2h,-h,0,h,2h$.

- Até ao 5º grau temos:
![[derivadas aprox polinomial.png]]
por exemplo, a derivada para o 3º grau seria: $$\frac{df}{dx}= \frac{\frac{1}{24}f\left(\frac{-3}{2}h\right) - \frac{27}{24}f\left(\frac{-1}{2}h\right) + \frac{27}{24}f\left(\frac{1}{2}h\right) \frac{-1}{24}f\left(\frac{3}{2}h\right)}{h}$$
- Para derivadas em pontos $x\ne0$, temos as mesmas fórmulas mas em vez de ter $f(\frac{-1}{2}h)$ temos $f(x - \frac{1}{2}h)$.
- Os erros de cada aproximação podem ser obtidos da forma que fizemos atrás.
- No resto do livro isto não é usado, mas é útil saber.

#computacional #programacao #derivada
