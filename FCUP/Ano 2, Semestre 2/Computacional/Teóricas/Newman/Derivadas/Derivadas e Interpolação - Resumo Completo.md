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
- 

# 2 - Derivadas ao centro
- Na secção 1 de derivadas vimos derivadas calculadas ao aproximar-nos do ponto $x$ por valores maiores (para a frente) ou menores (para trás) e vimos que estes métodos são pouco precisos.
- Temos então derivadas ao centro, uma mistura das 2 outras:
$$\frac{df}{dx} \approx \frac{f\left(x + \frac{h}{2}\right)- f\left(x - \frac{h}{2}\right)}{h}$$
- Tal como antes, estamos a aproximar-nos de $x$ usando 2 pontos a uma distância $h$. Mas agora os 2 pontos são pontos a distâncias $\pm \frac{h}{2}$ de $x$

## 2.1 - Erros
- Começamos com 2 séries de Taylor:
$$\begin{align*}
f\left(x + \frac{h}{2}\right)&= f(x) + \frac{1}{2}hf'(x) + \frac{1}{8}h^{2}f''(x)+ \frac{1}{48}h^{3}f'''(x)+ \dots\\
f\left(x - \frac{h}{2}\right)&= f(x) - \frac{1}{2}hf'(x) + \frac{1}{8}h^{2}f''(x)-\frac{1}{48}h^{3}f'''(x)+\dots
\end{align*}$$
Subtraímos a 2ª à 1ª e temos:
$$f'(x)=\frac{f \left( x + \frac{h}{2}\right) - f \left(x - \frac{h}{2} \right)}{h} - \frac{1}{24}h^{2}f'''(x)$$
pelo que o erro de aproximação é $$\epsilon_\textsf{aprox} = \frac{1}{24}h^{2} |f'''(x)| $$
- O erro de arredondamento é, novamente: $\epsilon_\textsf{arred}= \frac{2C|f(x)|}{h}$
- Assim, o erro total é:
$$\epsilon (h)= \frac{2C|f(x)|}{h} + \frac{1}{24}h^{2} |f'''(x)| $$

- Novamente, fazemos $\frac{d\epsilon}{dh}=0$ e temos:
$$h_\textsf{erro min}=h = \sqrt[3]{24C \left| \frac{f(x)}{f'''(x)} \right|}$$
para o qual temos:
$$\epsilon_{min}= \sqrt[3]{\frac{9}{8} C^{2} [f(x)]^{2}|f'''(x)|}$$

- Assim, este método dá-nos um erro menor, sendo que o $h$ para o qual temos o erro mínimo é _maior_.
- Por outras palavras, derivada central dá menos erro, mas derivada para frente/trás permite-nos usar um intervalo $h$ menor, o que por vezes é muito importante.



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

# 4 - Segundas Derivadas
- Por definição, é aquilo que obtemos ao aplicar a derivada à derivada. Assim, começamos por obter a derivada em 2 pontos $x\pm \frac{h}{2}$:
$$f'(x+ \frac{h}{2})\approx \frac{f(x+h)-f(x)}{h} \quad \quad;\quad \quad f'(x- \frac{h}{2})\approx \frac{f(x)-f(x-h)}{h}$$(nestas 2 equações obtemos a derivada de cada ponto a usar o método da derivada ao centro, ou seja, os pontos no denominador são $(x+ \frac{h}{2}) \pm \frac{h}{2}$.

- Usamos então mais uma vez o método da derivada ao centro, agora usando os 2 pontos acima para obter $f''(x)$:
$$\begin{align*}
f''(x) &\approx \frac{f'(x+ \frac{h}{2})-f'(x- \frac{h}{2})}{h}\\
&= \frac{\frac{f(x+h)-f(x)}{h}-\frac{f(x)-f(x-h)}{h}}{h}\\
&= \frac{f(x+h)-2f(x)+f(x-h)}{h^{2}}
\end{align*}$$
- Isto é a aproximação mais simples da segunda derivada, que iremos usar ao resolver equações diferenciais.

## 4.1 - Erros
- Novamente, começamos com expansões em série de Taylor:
$$\begin{align*}
f(x+h)=f(x)+ hf'(x) + \frac{1}{2}h^{2}f''(x) + \frac{1}{6}h^{3}f'''(x) + \frac{1}{24}h^{4}f^{(4)}(x)+\dots\\
f(x-h)=f(x)- hf'(x) + \frac{1}{2}h^{2}f''(x) - \frac{1}{6}h^{3}f'''(x) + \frac{1}{24}h^{4}f^{(4)}(x)+\dots
\end{align*} $$
- Ao somar as 2 equações e isolar $f''(x)$ temos:
$$f''(x)=\frac{f(x+h)-2f(x)+f(x-h)}{h^{2}} - \frac{1}{12}h^{2}f^{(4)}(x)+\dots$$

- Ora, daqui temos o erro de aproximação: $$\epsilon_\textsf{aprox}=\frac{1}{12} h^{2} |f^{(4)}(x)|$$
- Temos ainda o erro de arredondamento. Tal como já vimos, ao determinar um certo $f(x)$ temos um erro de arredondamento de $C|f(x)|$. Assim, ao calcular $f''(x)$ com a fórmula acima, o erro de arredondamento máximo que temos é $\frac{4C|f(x)|}{h^{2}}$. 
- Assim, o erro total é:
$$\epsilon(h)= \frac{4C|f(x)|}{h^{2}} + \frac{1}{12} h^{2} |f^{(4)}(x)|$$

- Ao fazer $\frac{d\epsilon}{dh}=0$ obtemos o $h$ que nos dá o erro mínimo:
$$h_{min}= \sqrt[4]{48C \left|\frac{f(x)}{f^{(4)}(x)} \right|}$$
que, ao substituir na fórmula de $\epsilon(h)$ nos dá o _erro mínimo_:
$$\epsilon_{min}= \sqrt{\frac{4}{3} C |f(x)f^{(4)}(x)|}$$
- Ou seja, as segunda derivadas que obtemos são tão precisas como as derivadas obtidas com aproximação à frente ou atrás.
- Tal como com derivadas normais, podemos fazer aproximações polinomiais mas no Newman não se fala.

# 5 - Derivadas Parciais
- Basicamente, só aplicamos o método de derivadas ao centro:
$$\begin{align*}
\frac{\partial f}{\partial x}(x) &= \frac{f\left(x+ \frac{h}{2}, y\right)- f\left(x- \frac{h}{2}, y\right)}{h}\\
\frac{\partial f}{\partial y}(y) &= \frac{f\left(x, y+ \frac{h}{2}\right)- f\left(x, y- \frac{h}{2}\right)}{h}
\end{align*}$$
- Usando o método de dedução que usamos na 2ª derivada, temos:
$$\small\frac{\partial^{2}f}{\partial x \partial y}(x,y) = \frac{f\left(x+ \frac{h}{2}, y+ \frac{h}{2}\right)- f\left(x- \frac{h}{2}, y+ \frac{h}{2}\right) - f\left(x+ \frac{h}{2}, y- \frac{h}{2}\right) + f\left(x- \frac{h}{2}, y- \frac{h}{2}\right)}{h^{2}}$$


# 6 - Derivadas de Dados com Ruído
- Por vezes, em vez de querer derivar uma função $f(x)$ queremos a derivada do gráfico de um conjunto de dados em que o formato é claro ao olhar, mas em que temos ruído.
- Ora, se calcularmos a derivada da "função" em cada ponto e fizemos um gráfico, veremos que o problema do ruído só piora. Isto ocorre quase sempre que fazemos isto e a razão pode ser vista na imagem abaixo:
![[dados com ruido.png]]

- O que podemos fazer:
    1. Usar $h$ maior. Basicamente, estamos a fazer o mesmo que fazemos ao usar $h$ maior para reduzir o erro de arredondamento. Ou seja, estamos a pior o erro de aproximação ao reduzir o "erro de ruído".
    2. Aproximar uma secção dos dados à volta do $x$ em que queremos derivar a uma curva. Mas não fazemos como nas aproximações de derivadas e integrais com polinómios (em que usamos 3,4 pontos). Fazemos uma regressão de quadrados mínimos.
    3. Suavizar os pontos om outro método como, por exemplo, aproximações de Fourier.


-----
-----
# Interpolação
- Temos uma função $f(x)$ que conhecemos apenas em 2 pontos $a,b$.
- **Interpolação** resume-se a tentar determinar 1 ponto de $f$ algures entre $a$ e $b$.

![[interpolacao.png]]
- O caso mais simpls é *interpolação linear*.
- Basicamente, presumimos que a função é uma reta, que terá declive: $$m=\frac{f(b)-f(a)}{b-a}$$
- Tendo um ponto $x$ como ilustrado acima, temos:
$$\begin{align*}
f(x) \approx f(a) + y &=  f(a) + \frac{f(b)-f(a)}{b-a}(x-a)\\
&= \frac{(b-x)f(a)+(x-a)f(b)}{b-a}
\end{align*}$$
de notar que esta fórmula também pode ser usada para *extrapolar* pontos além de $[a,b]$.

## Erros
- Procedemos da mesma forma que fizemos com derivadas. Começamos com 2 séries de Taylor:
$$\begin{align*}
f(a)=f(x) + (a-x)f'(x)+ \frac{1}{2}(a-x)^{2}f''(x)+\dots\\
f(b)=f(x) + (b-x)f'(x)+ \frac{1}{2}(b-x)^{2}f''(x)+\dots
\end{align*}$$
- Substituímos $f(a),f(b)$ na fórmula de $f(x)$ acima e temos:
$$f(x)= \frac{(b-x)f(a)+(x-a)f(b)}{b-a} + (a-x)(b-x)f''(x)+\dots$$
ou seja o erro é:
$$\epsilon=(a-x)(b-x)f''(x)+\dots$$
- De notar que consoante $x\to a, x\to b$ temos que $\epsilon\to0$. Isto faz sentido e indica que o erro máximo será no centro do intervalo.
- Presumindo que $f''$ varia devagar, podemos definir $b-a=h$ e temos que, no centro do intervalo, $\epsilon=\frac{1}{4}h^{2}|f''(x)|$. Ou seja, o erro de aproximação varia da mesma forma que o erro da derivada ao centro e conseguimos reduzi-lo ao *diminuir* $h$.
- No entanto, como na interpolação fazemos *somas* em vez de subtrações (que era o caso das derivadas), não precisamos de nos preocupar com erros de arredondamento.
- Se só conhecermos 2 pontos, interpolação linear é a melhor aproximação que podemos fazer.

#computacional #programacao #derivada 