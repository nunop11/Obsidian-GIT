# 10 - Método de Relaxação
- Consideremos que temos a seguinte equação:
$$x = 2 - e^{-x}$$
- Um método computacional comum para resolver equações é _iteração_. Basicamente, escolhemos um valores inicial e continuamos a partir daí:
$$\begin{align*}
x_{0}&= 1 \\
x_{1}&= 2 - e^{-1} \approx 1.632 \\
x_{2}&= 2- e^{-1.632} \approx 1.804
\end{align*}$$
- Ora, é preciso ter uma equação do tipo $\large x=f(x)$, em que $f$ é uma função conhecida. Por vezes temos que reorganizar a função para ficar nesta forma.
- Além disso, isto apenas funciona quando $f(x)$ ***converge***.
- Mesmo aí, devemos notar que a função $f$ pode ter 2 ou mais soluções. No entanto, podemos resolver isto ao variar $x$. Isto porque este método irá converter para a solução mais próxima de $x_{0}$.

- Às vezes, em vez de converger, o método começa a oscilar entre2 valores, tal como acontecer com $x=e^{1-x^{2}}~~;~~x_{0}=\frac{1}{2}$. Por vezes, podemos resolver isto  ao restruturar a equação. No exemplo acima, se fizermos logaritmos dos 2 lados e reorganizarmos algumas coisas conseguimos obter $x=\sqrt{1-\log x}$ . Esta equação já converge.

## 10.1 - Explicação analítica
- Consideremos a equação $x=f(x)$, que tem a solução $x=x^{*}$ 
- Assim, algures durante o método iremos ter $x'$ (que consideramos que está próximo de $x^{*}$), sendo que a tentativa anterior é $x$. Assim, temos $x'=f(x)$. Podemos expandir isto em série de Taylor:
$$x' = f(x) = f(x^{*}) + (x-x^{*})f'(x*)$$(em que ignoramos os termos a partir da 2ª derivada)
- Ora, $x^{*}$ é a solução pelo que $f(x^{*})=x^{*}$. Podemos então escrever a equação acima como: $$x'-x^{*}=(x-x^{*})f'(x^{*})$$
- Ou seja, a distância a que estamos da solução numa certa tentativa é apenas multiplicada pela derivada de $f$ na solução ao passar para a tentativa seguinte.
- Ou seja, o método apenas converge se $\large |f'(x^{*})|<1$. Este é o *critério a verificar*.
- No entanto, se tivermos $|f'(x^{*})|>1$, na maioria dos casos teremos $|(f^{-1})'(x^{*})|<1$. Ou seja, se a função não converter, queremos transformá-la na **função ivnersa**.

- Ou seja, neste método só iremos obter a solução se o método convergir. Por vezes, uma função em que o método não converge pode ser resolvida ao usar a função inversa. Mesmo aí, o método pode não ser útil.

## 10.2 - Rate de conversão
- Assumindo que uma certa função $f$ converge, é importante saber o quão rápido o faz.
- Isto é-nos dado pela equação que vimos acima: $\large x' -x^{*}=(x-x^{*})f'(x^{*})$. Como $f'(x^{*})$ é constante, temos que a distância à solução diminui *exponencialmente* com o número de iterações. Existem métodos mais rápidos, mas isto é bom.

- No entanto, também é útil saber quando parar de iterar.
- Se precisamos apenas de uma solução rápida e *precisão não é o nosso maior foco*. Por exemplo, consideremos que apenas queremos uma precisão de 6 casas decimais. Assim, podemos simplesmente iterar até vermos que as primeiras 6 casas deixam de variar.

- Por outro lado, podemos querer ser *muito precisos* ou se queremos parar mal tenhamos a precisão desejada (por *performance*). Vejamos como proceder:
- Seja $\epsilon$ o erro de 1 certa iteração, tal que $x^{*}=x+\epsilon$ em que, novamente, $x^{*}$ é a solução verdadeira. Analogamente, $\epsilon'$ ser+a o erro da iteração $x'$. Daqui temos $x-x^{*}=-\epsilon~~,~~x'-x^{*}=\epsilon'$. Assim, podemos reescrever:
$$x'-x^{*}=(x-x^{*})f'(x^{*}) \Longrightarrow \epsilon'=\epsilon f'(x^{*})\leftrightarrow \epsilon= \frac{\epsilon'}{f'(x^{*})}$$
Ou seja:
$$x^{*}=x+\epsilon=x+\frac{\epsilon'}{f'(x^{*})}=x'+\epsilon'$$
Daqui temos:
$$\epsilon'= \frac{x-x'}{1 - \frac{1}{f'(x^{*})}}\sim \frac{x-x'}{1- \frac{1}{f'(x)}}$$
Aqui presumimos que $x$ está próximo de $x^{*}$, daí $f'(x^{*})\approx f'(x)$
- Assim, deste modo podemos determinar o erro da nossa tentativa, usando a _tentativa anterior e sem saber o valor real_. 
- No entanto, isto implica que conheçamos $f$ e consigamos determinar $f'$. Por vezes, podemos ter que obter derivadas, como vimos na devida secção.

- Mas podemos fazer isto sem usar derivadas.
- Tendo 3 tentativas consecutivas: $x,x',x''$, tem-se que o erro da última é $$\epsilon''\approx \frac{x'-x''}{1- \frac{1}{f'(x)}}$$
- Ora, temos que $f'(x)\approx \frac{f(x)-f(x')}{x-x'}$ para 2 pontos $x,x'$ próximos. Temos ainda que, neste método, cada $x'$ é a imagem do $x$ anterior, $f(x)=x'$ e $f(x')=x''$. Ou seja, $f'(x)\approx \frac{x'-x''}{x-x'}$
- Assim, ao substituir na equação de $\epsilon''$ acima, temos:
$$\epsilon''= \frac{x'-x''}{1- \frac{x-x'}{x'-x''}}= \frac{(x'-x'')^{2}}{2x'-x-x''}$$
- Ou seja, podemos obter o erro sem derivadas, se mantivermos as últimas 3 tentativas.

## 10.3 - Relaxação para 2+ variáveis
- Se tivermos $N$ equações de $N$ variáveis $x_{1},x_{2},\dots,x_{N}$ que consguimos reescrever na forma:
$$\begin{align*}
x_{1}&= f_{1}(x_{1},x_{2},\dots,x_{N})\\
x_{2}&= f_{2}(x_{1},x_{2},\dots,x_{N})\\
&\dots\\
x_{N}&= f_{N}(x_{1},x_{2},\dots,x_{N})
\end{align*}$$
- Podemos escolher valores iniciais para cada variável e utilizar o método da relaxação. Se após um certo número de iterações todas as variáveis tiverem valores constantes, essas serão as soluções do sistema de equações não-lineares.
- No entanto, mais uma vez, é preciso que todas as funções convirjam.

## 10.4 - Sobre-relaxação sucessiva
- Acrescentamos um parâmetro $\omega$ para fazer overshoot ao passar para a próxima tentativa. Na prática, se $\omega$ for um bom valor, isto vai fazer com que tenhamos convergência mais rápido. Isto assemelha-se ao que temos no método de *Descida do Gradiente* na secção de Máximos e Mínimos.
- Temos:
$$x'=(1+\omega)f(x)-\omega x$$send o erro:
$$\epsilon'=\frac{x-x'}{1- \frac{1}{(1+\omega)f'(x)-\omega x} }$$
- $\omega$ é obtido por tentativa e erro. Se:
    - *omega postivo* - convergência direta e mais rápida
    - *omega negativo* - convergência oscilatória com amplitudes cada vez menores

#computacional #programacao 