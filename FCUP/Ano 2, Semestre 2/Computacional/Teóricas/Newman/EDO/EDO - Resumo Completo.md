# 1 - EDO de 1 Variável
- Uma equação diferencial ordinária (EDO) de 1 variável será do tipo $$\frac{dx}{dt}=f(x,t)$$
- Para determinara a solução completa de uma equação deste tipo, também precisamos de conhecer os valores iniciais: $x(t=0)$. 

## 1.1 - Método de Euler
- Tendo uma equação diferentecial do tipo $\frac{dx}{dt}=f(x,t)$ em que conhecemos $x$ num certo valor de $t$, podemos determinar o valor de $x$ após um curto intervalo $h$ usando uma série de Taylor:
$$\begin{align*}
x(t+h)&= x(t) + h \frac{dx}{dt} + \frac{1}{2}h^{2} \frac{d^{2}x}{dt^{2}} + \dots\\
&= x(t) + h f(x,t) + O(h^{2})
\end{align*}$$
(ignoramos os termos acima de $h^{2}$, porque sendo $h$ um intervalo reduzido, o seu quadrado será ainda mais reduzido AKA $\approx0$)
- Ou seja, ficamos com $$\boxed{x(t+h)=x(t)+hf(x,t)}$$
- E está. Desde que $h$ seja suficientemente reduzido, a equação acima permite-nos determinar $x$ para quantos valores de $t$ quantos quisermos, com uma precisão bem boa.
- Na prática, consideremos que temos uma equação diferencial em que conhecemos $x(t=a)$ e queremos saber a solução da equação de $a$ a $b$. Definimos um $h$ reduzido e apenas usamos esta fórmula repetidamente até ficarmos com $t=b$.

- No entanto, neste método eliminamos os termos da série de Taylor a partir de $h^{2}$. Isto dá-nos aproximações decentes, mas ao fazer isto ficamos com um erro igual a $\frac{1}{2}h [f(x(b),b)-f(x(a),a)]$, que é proporcional a $h$. Ou seja, ao diminuir $h$ para metade também o erro diminui para metade, o que não é muito. Por outro lado, $N= \frac{b-a}{h}$, ou seja para diminuir $h$ (e o erro) para metade, iremos aumentar o número de passos (e o tempo de execução) para o dobro.

# 2 - Runge-Kutta
- Conforme o que vimos na secção anterior, a causa do erro relativamente alto do método de Euler é o facto de desprezar-mos os termos da série de Taylor a partir de $h^{2}$. Assim, pode parecer sensato incluir o termo com $h^{2}$, tendo-se:
$$\frac{1}{2}h^{2} \frac{d^{2}x}{dt^{2}}= \frac{1}{2}h^{2} \frac{df}{dt}$$
mas a derivada de $f$ pode ser bastante difícil de determinar, porque nem sempre temos uma fórmula que define $f$, apenas um conjunto de valores. Mas mesmo que tenhamos uma fórmula, determinar derivadas é menos conveniente do que o método de Runge-Kutta.

- Ora, o método de Runge-Kutta consiste numa série de métodos, com diferentes graus. Aliás, o método de Euler pode ser considerado um método de Runge-Kutta: *Método de Runge-Kutta de 1º grau*.

## 2.1 - Runge-Kutta 2ª Ordem
![[metodo euler.png]]
- Uma equação diferencial $\frac{dx}{dt}=f(x,t)$ diz-nos que o declive da curva $x(t)$ num certo $t$ será $f(x,t)$.
- Ora, no Método de Euler, usamos esta informação para extrapolar o ponto $x(t+h)$ usando o ponto $x(t)$ e a função $f$. Mas vemos na imagem acima que se a solução da eq Dif for curva, então poderemos ter erros elevados.

- Consideremos agora que, partindo de $x(t)$ usamos o declive no *midpoint* $t+ \frac{1}{2}h$ para extrapolar o ponto seguinte, como temos acima. Isto normalmente irá dar aproximações melhores que o método de Euler, pelo que é a base do método Runge-Kutta de 2ª ordem.

- Em termos matemáticos, fazemos uma expansão de Taylor de $x(t+h)$ em torno de $t+ \frac{1}{2}h$:
$$\small x(t+h)=x(t+ \tfrac{1}{2}h) + \tfrac{1}{2}h \left( \frac{dx}{dt}\right)_{t+ \tfrac{1}{2}h} + \tfrac{1}{8} h^{2} \left( \frac{d^{2}x}{dt^{2}} \right)_{t+ \tfrac{1}{2}h} + O(h^{3})$$
Podemos fazer o mesmo para $x(t)$ e temos:
$$\small x(t+h)=x(t+ \tfrac{1}{2}h) - \tfrac{1}{2}h \left( \frac{dx}{dt}\right)_{t+ \tfrac{1}{2}h} + \tfrac{1}{8} h^{2} \left( \frac{d^{2}x}{dt^{2}} \right)_{t+ \tfrac{1}{2}h} + O(h^{3})$$
- Facilmente vemos que isto nos dá:
$$\begin{align*}
x(t+h)&= x(t) + h \left( \frac{dx}{dt} \right)_{t+ \tfrac{1}{2}h} + O(h^{3})\\
&= x(t) + h ~f(x(t+ \tfrac{1}{2}h), t + \tfrac12 h) + O(h^{3})
\end{align*}$$
- Notemos que agora apenas eliminamos os termos a partir de $h^{3}$, o que irá resultar em mais exatidão. Ou seja, recordando o capítulo de integrais, o termo de Runge-Kutta de 2ª ordem significa que tem alta exatidão até $h^{2}$.

- No entanto, este método implica que, para determinar $x(t+h)$ precisamos de $x(t)$, que conhecemos, e $x(t+\tfrac12)$, que não conhecemos.
- Para resolver isto, usamos o método de Euler. Ou seja, determinamos $x(t+\tfrac12h)$ usando: $x(t+\tfrac12h)=x(t)+\tfrac12hf(x,t)$. Ou seja, o processo de aplicação deste método é:

0. Começamos num ponto $x(t)$ conhecido.
1. Determinar $k_{1}=hf(x,t)$
2. Determinar $k_{2}= hf(x+\tfrac12k_{1}, t+ \tfrac12h)$, que será o declive no midpoint
3. Determinar $x(t+h)=x(t)+k_{2}$, o próximo ponto
4. Repetir o processo com $x(t+h)$ para obter $x(t+2h)$

- Para um mesmo $h$, este método é muito mais preciso que o de Euler. Aliás, podemos aumentar $h$ para reduzir o tempo de execução e ainda assim obter a mesma exatidão que o método de Euler.
- De notar que, ao fazer a aproximação com método de Euler para obter o declive no midpoint *não* estamos a aumentar o erro de forma significativa, porque o erro dessa aproximação também depende de $h^{3}$. (Demo na página 33 do Newman).

## 2.2 - Runge-Kutta 4ª Ordem
- Ao fazer um processo semelhante à dedução do método de 2ª ordem, mas mais complicado, podemos obter o seguinte método:

$$\begin{align*}
k_{1}&= hf(x,t)\\
k_{2}&= hf(x+\tfrac12k_{1}, t+\tfrac12h)\\
k_{3}&= hf(x+\tfrac12k_{2}, t+\tfrac12h)\\
k_{4}&= hf(x+k_{3},t+h)\\
x(t+h)&= x(t)+ \tfrac16(k_{1}+2k_{2}+2k_{3}+k_{4})
\end{align*}$$
- Este é o método mais comum. É preciso até $h^{4}$ e o seu erro varia com $h^{5}$. Por exemplo, para uma equação testada no Newman, os resultados obtidos para $N=1000$ com Euler são semelhante obtidos com $N=20$ com Runge-Kutta de 4ª ordem.
- De notar que, se as 5 fórmulas acima forem mal escritas no programa, poderemos obter erros elevados, mas ainda assim dificeis de ver à primeira.



# 3 - Intervalos até infinito
- Vejamos agora o que fazer se queremos obter a solução de uma Eq Dif para $t\to\infty$. Não podemos usar os métodos atrás, porque isso implicaria usar $N=\infty$ pontos.
- Ora, basta fazer o mesmo que fizemos com integrais: **mudança de variáveis**, assim:
$$u= \frac{t}{1+t} \quad \quad;\quad \quad t= \frac{u}{1-u}$$
sendo que se $t\to\infty$ então $u\to1$.

- Podemos então escrever:
$$\frac{dx}{dt}=f(x,t) \Longrightarrow \frac{dx}{du} \frac{du}{dt}=f(x,t)$$
ou seja:
$$\frac{dx}{du}= \frac{dt}{du}f(x,\tfrac{u}{1-u})$$
mas, como temos $t= \frac{u}{1-u}$, então: $\frac{dt}{du}=\tfrac{1}{(1-u)^{2}}$. Logo:
$$\frac{dx}{du}=(1-u)^{-2}f(x,\tfrac{u}{1-u})=g(x,u)$$
O que já é uma EDO normal que sabemos resolver normalmente.



# 4 - Múltiplas Variáveis
- Consideremos agora que temos 2 equações diferenciais, mas em que continuamos a ter *1 variável independente*:
$$\frac{dx}{dt}=f_{x}(x,y,t) \quad \quad;\quad \quad \frac{dy}{dt}=f_{y}(x,y,t)$$
Podemos simplesmente generalizar para qualquer número de variveis, tal que:
$$\frac{d\mathbf{r}}{dt}=\mathbf{f}(\mathbf{r},t)$$
sendo $\mathbf{r}=(x,y,\dots)$ e $\mathbf{f}(\mathbf{r},t)=(f_{x}(\mathbf{r},t),f_{y}(\mathbf{r},t),\dots)$
- Temos então a resolução com o método Runge-Kutta de 4ª ordem:
$$\begin{align*}
\mathbf{k}_{1}&= h \mathbf{f}(\mathbf{r},t)\\
\mathbf{k}_{2}&= h \mathbf{f}(\mathbf{r}+ \tfrac12 \mathbf{k_{1}},t+\tfrac12h)\\
\mathbf{k}_{3}&= h \mathbf{f}(\mathbf{r}+ \tfrac12 \mathbf{k_{2}},t+\tfrac12h)\\
\mathbf{k}_{4}&= h \mathbf{f}(\mathbf{r} + \mathbf{k}_{3},t+h)\\
\mathbf{r}(t+h)&= \mathbf{r}(t) + \tfrac16(\mathbf{k}_{1}+2\mathbf{k}_{2}+2\mathbf{k}_{3}+\mathbf{k}_{4})
\end{align*}$$
sendo que em Python, $\mathbf{r}, \mathbf{f}$ serão arrays. Assim, o código será muito parecido àquele de resolução de 1 equação diferencial. (Ver página 345 do Newman - 355 do pdf)
- Podemos pensar nisto como sendo um sistema de equações diferenciais simultaneas.


# 5 - EDOs de Ordem Superior
**2ª Ordem**
- Até agora vimos apenas equações diferenciais de 1ª ordem, que são as menos comuns na física. 
- Estas equações são do tipo:
$$\frac{d^{2}x}{dt^{2}}= f \left( x, \frac{dx}{dt}, t \right)$$
apenas fazemos $y= \frac{dx}{dt}$ e ficamos com: $\frac{dy}{dt}=f(x,y,t)$
- Ora, isto não passa de 2 equações de 1ª ordem simultaneas, tal como vimos na secção anterior.

**3ª Ordem**
- E por aí adiante. Uma Eq Dif de 3ª ordem seria do tipo:
$$\frac{d^{3}x}{dt^{3}}=f \left( x, \frac{dx}{dt}, \frac{d^{2}x}{dt^{2}}, t \right)$$
pelo que simplesmente fazemos $\frac{dx}{dt}=y$ e $\frac{dy}{dt}=z$. E temos $\frac{dz}{dt}=f(x,y,z,t)$.

**2 Variáveis de 2ª Ordem**
$$\frac{d^{2}\mathbf{r}}{dt^{2}}=\mathbf{f} \left( \mathbf{r}, \tfrac{d\mathbf{r}}{dt}, t \right)$$
e fazemos $$\frac{d\mathbf{r}}{dt}=\mathbf{s} \quad \quad;\quad \quad \frac{d\mathbf{s}}{dt}= \mathbf{f}(\mathbf{r}, \mathbf{s}, t)$$
- Sendo que se tivéssemos começado com 2 equações diferenciais, acabaríamos com 4 equações.

# 6 - Runge-Kutta Adaptativo
- Até agora, vimos casos com $h$ constante e predefinido pelo programador.
- Ora, podemos fazer o programa determinar o melhor valor de $h$ em cada passo. Por exemplo, consideremos o caso abaixo, em que queremos ter muitos pontos na parte de variação rápida:
![[rk4 adaptativo.png]]
- Para usar o método adaptativo temos 2 partes:
    - Determinar o erro dos nossos passos
    - Comparar com o erro desejado. Aumentar ou diminuir o $h$ conforme a observação.

1. Começando com $h$ reduzido (pelo sim pelo não), usar o método de Runge-Kutta como normalmente e obter os *2 primeiros pontos*, ou seja, ficar com $x(t),x(t+h),x(t+2h)$.
2. Voltar ao início e usar um intervalo $h'=2h$. Determinar 1 ponto, que será $x(t+2h)$. Ou seja, temos 2 estimativas deste valor.

- O método de Runge-Kutta tem erro de ordem $h^{5}$. Ou seja, o erro de uma estimativa será $\sim ch^{5}$
    - Sendo $x(t+2h)$ o valor real do ponto
    - A nossa primeira estimativa (com $h$ original) irá ter a seguinte relação com o valor real: $$x(t+2h)=x_{1} + 2ch^{5}$$
    - A nossa segunda estimativa (com $h'=2h$) irá ter a seguinte relação com o valor real: $$x(t+2h)=x_{2}+ 32ch^{5}$$
    - Ao igualar as 2 equações acima temos: $x_{1}=x_{2}+30ch^{5}$. Ou seja: $$\varepsilon= ch^{5}=\frac{1}{30}(x_{1}-x_{2})$$
- E é este o erro que comparamos com o erro desejado, $\varepsilon_{0}$. Mas como?

- Assim, qual será o intervalo "perfeito"? Chamemos-lhe $h'$. O seu erro seria: $$\varepsilon'=ch'^{~5} =ch^{5}(\tfrac{h'}{h})^{5}= \tfrac{1}{30} (x_{1}-x_{2})^{5}(\tfrac{h'}{h})^{5}$$
- Ora, queremos que o erro de $h'$ seja o nosso erro desejado, $\varepsilon_{0}$. Ou seja, (tendo em conta que apenas importa o módulo do erro) queremos ter: $$\tfrac{1}{30}|x_{1}-x_{2}| (\tfrac{h'}{h})^{5}=h'\varepsilon_{0}$$
e temos
$$\boxed{h'=h \left( \frac{30h\varepsilon_{0}}{|x_{1}-x_{2}|} \right)^{\frac{1}{4}}=h\rho^{\frac{1}{4}}}$$

3. Ou seja, usamos as 2 tentativas para determinar a razão $\rho$. 
    - Se $\rho>1$, então temos uma precisão melhor que a desejada. Isso acaba por ser mau, porque indica que estamos a usar intervalos inferiores ao necessário. Assim, continuamos, passando para o ponto $x(t+2h)$, mas com um intervalo maior, que será dado com exatidão pela equação acima. Ao passar para a próxima tentativa, o valor de $x(t+2h)$ que consideramos é $x_{1}$!
        - Por mero acaso, podemos ter $x_{1}\simeq x_{2}$. Nesse caso $\rho\gg1$, pelo que o método iria falhar por completo. Assim, normalmente estabelecesse um valor máximo de $\rho$, normalmente $2$.
    - Se $\rho<1$, então temos uma precisão inferior ao desejado. Assim, repetimos o passo e voltamos a $x(t)$ mas agora com um intervalo $h'$ inferior, que também é dado pela equação acima. 

- Apesar do que possa parecer, este método frequentemente demora menos ou muito menos que o método normal de Runge-Kutta.

## 6.1 - Adaptativo com 2 variáveis
- Ficamos com
$$\varepsilon_{x}=\tfrac{1}{30}(x_{1}-x_{2}) \quad \quad;\quad \quad \varepsilon_{y}=\tfrac{1}{30}(y_{1}-y_{2})$$
- E agora, a forma como usamos a fórmula acima depende do caso:
    - Se $x,y$ forem coordenadas, o erro de um ponto $(x,y)$ será $\sqrt{\varepsilon_{x}^{2}+\varepsilon_{y}^{2}}$, pelo que é isso que colocamos em vez de $\tfrac{1}{30}|x_{1}-x_{2}|$ na equação de $h'$.
    - Por outro lado, se nalgum exercício tivermos 2 variáveis em que apenas o erro de uma importa, não consideramos sequer a outra no erro.

# 7 - Método de Leapfrog
- Este método é usado para resolver eqs difs do tipo $\frac{dx}{dt}=f(x,t)$
![[Leapfrog.png]]
- Acima temos uma comparação entre o método RK2 (cima) e Leapfrog (baixo). No RK2, determinamos o midpoint e, com ele, obtemos o ponto seguinte ($t+h$). A partir dele determinamos o midppoint seguinte ($t+h+h/2$). No leapfrog usamos o midpoint para determinar o midpoint seguinte.

- De recordar que no método Runge-Kutta 2 usamos o declive no ponto ($x(t+ \frac{1}{2}h),t+ \frac{1}{2}h$) para determinar o ponto seguinte: $(x(t+h),t+h)$. De notar ainda que $f(x,t)$ nos dá o declive num ponto $x(t)$. No entanto, como normalmente não conhecemos o ponto intermédio usamos o método de Euler para o aproximar. Temos as equações:
$$\begin{align*}
x(t+\tfrac12h)&= x(t)+\tfrac12hf(x,t)\\
x(t+h) &= x(t) + h f(x(t+ \tfrac{1}{2}h), t + \tfrac12 h)
\end{align*}$$
- Este método tem um erro de ordem $h^{2}$.

- Ora, o método de Leapfrog começa da mesma forma. Começando com $x(t)$. Com este ponto determinamos $x(t+ \frac{1}{2}h)$ e $x(t+h)$. 
- As diferenças ocorrem a seguir. Em vez de obter $x(t+ \frac{3}{2}h)$ usando $x(t+h)$, usamos o midpoint anterior. Em termos matemáticos: $$x(t+ \tfrac{3}{2}h) = x(t +\tfrac12 h) + hf(x(t+h),t+h)$$
- E podemos novamente usar este midpoint para obter $x(t+2h)$:
$$x(t+2h)=x(t+h) + hf(x(t+ \tfrac32h),t+\tfrac32h)$$
- Podemos então repetir isto ao longo do intervalo pretendido. E temos as 2 fórmulas equivalentes às to RK2 acima: $$\begin{align*}
x(t+h) &= x(t) + h f(x(t+ \tfrac{1}{2}h), t + \tfrac12 h)\\
x(t+\tfrac32h)&= x(t+\tfrac12h) + hf(x(t+h),t+h)
\end{align*}$$
- O nome vem do facto que, para determinar os midpoints usamos o midpoint anterior, ou seja, "saltamos" o valor anterior.
- Tal como o RK2, o erro de 1 passo é de ordem $h^{3}$ enquanto que o erro de uma sequência de passos é de ordem $h^{2}$.
- Tal como os Runge-Kutta podemos usar isto para resolver sistemas de equações diferenciais, basta resolver a equação como sendo do tipo $\frac{d\mathbf{r}}{dt}=f(\mathbf{r},t)$
- A vantagem deste método é que tem simetria de *time reversal*.

## 7.1 - Importância/Aplicação do Leapfrog 
- Como referi na secção anterior, o método de leapfrog tem simetria de time-reversal.
- Neste método, qualquer instante $t_{1}$ é definido na íntegra por 2 valores $x(t_{1}),x(t_{1}+\tfrac12h)$. A partir destes conseguimos prever a solução da EDO para $t>t_{1}$ repetindo as equações do método de Leapfrog.
- Ora, se calcularmos a solução da EDO até um certo $t=t_{2}$, podemos usar o método de leapfrog de forma invertida (com intervalo $-h$), pelo que iremos regressar aos valores de $t_{1}$ com apenas erros de arredondamento.

> PROVA: 
> ![[Aplicação Leapfrog - deducao.png]]

- Ora, uma implicação disto é na *conservação de energia*.
- Por exemplo, no caso do movimento de um pendulo, cuja resolução com RK4 é feita num exercício, temos as equações: $$\frac{d\theta}{dt}=\omega\quad \quad \quad \quad \frac{d\omega}{dt}=\frac{-g}{\ell}\sin\theta$$
- Ora, neste caso a energia total do sistema é constante - há conservação de energia.
- No método de Runge-Kutta 4 obtemos uma boa solução, mas uma solução em que a energia apenas é *aproximadamente constante*. Aliás, se traçarmos um gráfico de energia em função do tempo para o RK2 temos: 
![[RK -  conservacao energia.png]]

- No entanto, para o método de Leapfrog a *energia é conservada*, pelo que o gráfico obtido é assim:
![[Leapfrog - Conservacao energia.png]]

- No entanto, o que devemos notar é que, para o caso do pêndulo, os 2 gráficos acima correspondem a várias oscilações consecutivas do pêndulo.
- Assim, devemos notar que no leapfrog, temos conservação de energia em 1 oscilação completa / 1 período (2 picos no traçado acima corresponderão ao mesmo ponto da oscilação, por exemplo). Ao longo de 1 período (por exemplo entre o inicio e o meio do período), no entanto, não temos conservação.

- Ou seja, o método de Leapfrog é útil para resolver sistemas com conservação de energia que se extendam por longos intervalos de tempo. Isto porque, nestes casos, após tempo suficiente, o método runge-kutta eventualmente vai desviar-se tanto da energia inicial que a solução deixar de ser correta

# 8 - Método de Verlet
- Consideremos que temos uma EDO de 2º grau como aparece em muitos problemas físicos: $\frac{d^{2}x}{dt^{2}}=f(x,t)$
- O que fizemos até agora foi dividir isto num sistema de EDOs de 1º grau: $$\begin{cases}
\frac{dx}{dt}=v\\ \frac{dv}{dt}=f(x,t)
\end{cases}$$
- Assim, definimos o vetor $\mathbf{r}=(x,v)$ e usamos RK ou leapfrog para resolver a equação $\frac{d\mathbf{r}}{dt}=\mathbf{f}(\mathbf{r},t)$

- Vejamos outra forma de fazer isto. Consideramos que conhecemos $x(t)$ e $v(t+\tfrac12h)$. Podemos usar *leapfrog* para escrever $x(t+h)$: $$x(t+h)=x(t)+h v(t+\tfrac12h)$$
assim como $v(t+\tfrac32h)$: $$v(t+\tfrac32h)=v(t+\tfrac12h)+hf(x(t+h),t+h)$$
- E podemos simplesmente repetir estas 2 equações muitas vezes para resolver a EDO.
- De notar que nunca chegamos a determinar $x$ em midpoints nem $v$ em pontos de $h$ inteiro. Assim, isto é uma melhoria em relação a usar leapfrog para o vetor $\mathbf{r}$, porque nesse caso determinavamos $x,v$ em todos os pontos, inteiros e midpoints.
- Este método apenas funciona quando temos o sistema de equações acima, em que, especificamente,
    - $dx/dt$ depende de $v$ e não $x$
    - $dv/dt$ depende de  $x$ e não $v$
- Felizmente, muitos problemas acabam por resultar em equações diferenciais deste formato.

- Um problema deste método é quando queremos calcular algo que depende de $x$ E $v$, como energia. Consideremos que estamos a estudar um lançamento. A energia cinética depende de $v$ e a potencial depende de $x$. Ou seja, para saber a energia num certo instante precisamos de conhecer $x,v$ nesse instante, algo que nunca acontece neste método.
    - Ora, para corrigir isso, basta determinar $v$ nos pontos de $h$ inteiro, usando o método de Euler, com intervalo $\tfrac12h$: $$v(t+h)=v(t+\tfrac12h)+\tfrac12hf(x(t+h),t+h)$$

## 8.1 - Aplicação
- Começamos por saber $x(t)$ e $v(t)$. Calculamos: $v(t+\tfrac12h)=v(t)+\tfrac12hf(x(t),t)$
- Repetir os seguintes passos: 
![[Verlet - deducao.png|371]]

## 8.2 - 2+ Dimensões
- Este método facilmente é convertido em 2+ dimensões. Basta definir: $\mathbf{r}=(x,y,z,\dots), \mathbf{v}=(v_{x},v_{y},v_{z},\dots)$
- Em que $k,f$ são também vetores.

# 9 - Método do Midpoint Modificado
- Outra caraterística importante do Leapfrog é que o seu erro é uma função **par** de $h$. Novamente, isto é causado pelo facto de o método ter simetria de time-reversal.

- Sabemos que 1 passo do método de leapfrog tem erro de ordem $h^{3}$, ou seja, podemos definir o erro de 1 passo como sendo uma função $\varepsilon(h)$, cujo primeiro termo é proporcional a $h^{3}$.
- Consideremos que, num intervalo $[0,h]$, o erro aumenta. Ou seja, o erro de $0\to h$ será $\varepsilon(h)$ e será *positivo*. No entanto, se formos no sentido $h\to0$ o erro irá diminuir e temos $\varepsilon(-h)$ que será *negativo*. Ou seja, podemos escrever: $$\varepsilon(-h)=-\varepsilon(h)$$
- Ora, isto é a definição de uma função *ímpar*. Assim temos: $$\varepsilon(h)=c_{3}h^{3}+c_{5}h^{5}+c_{7}h^{7}+\dots$$

- No entanto, como já vimos antes, o erro de 1 passo de Leapfrog é de ordem $h^{3}$, mas o erro resultante de fazer muitos passos de tamanho $h$ será 1 ordem menor: $h^{2}$. Ou seja, para determinar a solução de uma EDO num intervalo de tempo de duração $\Delta$ precisamos de $\Delta/h$ passos. O erro da operação total será: $\varepsilon(h)\cdot \tfrac{\Delta}{h}$. Ou seja, ficaremos com uma fórmula do erro em que as parcelas têm $h$ com expoentes pares.

- Ou seja, o erro do método de Leapfrog é par (os passos intermédios do leapfrog mais exatamente)
- No entanto, para iniciar o método de leapfrog e obter o midpoint usamos o método de Euler. Ora, este tem erro de ordem $h^{2}$. E este não apresenta parcelas com termos apenas pares, tal como vimos acima para o leapfrog. Ou seja, o facto de fazermos este primeiro passo impede-nos de ter uma função do erro do método de Leapfrog par.

**Solução**
- Consideremos que queremos determinar a solução de uma EDO num intervalor de tempo $[t,t+H]$, usando $n$ passos de tamanho $h=H/n$.
- Podemos escrever: $$\begin{align*}
x_{0}&= x(t)\\
y_{1}&= x_{0} + \tfrac12hf(x_{0},t)
\end{align*}$$
de onde temos, de uma forma geral: $$\begin{align*}
y_{m+1}&= y_{m} + hf(x_{m},t+mh)\\
x_{m+1}&= x_{m} + hf(y_{m+1},t+(m+\tfrac12)h)
\end{align*}$$
- Ou seja, os 2 valores finais que calculamos são: $y_{n}:x(t+H-\tfrac12h)$ e $x_{n}:x(t+H)$, em que normalmente considerariamos $x_{n}$ o nosso valor final de $x(t+H)$.
- No entanto, podemos determinar um outro valor de $x(t+H)$, usando $y$: $$x(t+H)=y_{n}+\tfrac12hf(x_{n},t+H)$$
- Podemos então combinar os 2 valores de $x(t+H)$, fazendo a sua média: $$x(t+H)=\frac{1}{2}[x_{n}+y_{n}+\tfrac12hf(x_{n},t+H)]$$
- Ora, devido a matemática e magia, determinar o último valor da solução desta forma faz com que os termos de expoente ímpar causados pelo método de Euler no primeiro passo se *anulem*, sendo que ficamos com um erro definido por uma *função par*.
- Este método, que consiste em fazer o Leapfrog com um passo final extra, é o **midpoint modificado**, que é basicamente inútil sozinho. A sua importância reside no facto de ser a base do método de Bulirsch-Stoer.

# 10 - Método de Bulirsch-Stoer
- Utiliza o método do midpoint modificado e extrapolação de Richardson.
- A lógica e as fórmulas são semelhantes ao método de integração de Romberg.

- Consideremos que temos a seguinte equação diferencial: $$\frac{dx}{dt}=f(x,t)$$
em que conhecemos o sistema em $t$ e queremos determinar a solução da eq dif até $t+H$.
- Apenas usamos o método de midpoint modificado para determinar a solução, mas começamos com um step $h_{1}=H$, ou seja, fazer a solução num só passo. A esta solução iremos chamar $R_{1,1}$ - $R$ não é de Rombreg, mas sim de *Richard Extrapolation*. Claro, se $H$ for um valor elevado, $R_{1,1}$ vai ser uma estimativa péssima.
- De seguida repetimos o midpoint modificado mas agora com 2 passos com intervalo $h_{2}=\tfrac12H$. A esta estimativa chamamos $R_{2,1}$
- Recorrendo ao que vimos na secção anterior, temos que o erro do método de midpoint modificado é definido por uma função de $h$ com expoentes par. Ou seja, podemos escrever: $$\begin{align*}
x(t+H)&= R_{1,1}+c_{1}h_{1}^{2}+O(h^{4}_{1})\\
x(t+H)&= R_{2,1}+c_{1}h_{2}^{2}+O(h^{4}_{2}) \tag{Eq. 10.1}
\end{align*}$$
recordando que $h_{1}=2h_{2}$ temos: $x(t+H)=R_{1,1}+4c_{1}h_{2}^{2}$        (Eq. 10.2)
- Podemos então igualar as equações 10.1, 10.2 e temos: $c_{1}h_{2}^{2}=\tfrac13(R_{2,1}-R_{1,1})$
- Ao substituir isto na equação 10.2 temos: $$x(t+H)=R_{2,1}+\tfrac13 (R_{2,1}-R_{1,1})+O(h_{2}^{4})$$
Ora, obtivemos uma nova estimativa que tem erro de ordem $h^{4}$, mas que foi obtido com 2 estimativas com erro de ordem $h^{2}$. Sim, tal como no Romberg.
- Podemos então chamar a esta nova estimativa $R_{2,2}=_{2,1}+\tfrac13 (R_{2,1}-R_{1,1})+O(h_{2}^{4})$

- Continuemos. Passamos agora a ter 3 passos com intervalos $h_{3}=\tfrac13H$. Usando o método de midpoint modificado diretamente obtemos $R_{3,1}$. Com uma dedução análoga à de cima temos: $$R_{3,2}=R_{3,1}+\tfrac45(R_{3,1}-R_{2,1})$$
- Podemos expandir o erro de $R_{3,2}$ sendo que temos $$x(t+H)=R_{3,2}+c_{2}h_{3}^{4}+O(h_{3}^{6})$$
- Tal como fizemos acima, podemos também escrever $x(t+H)=R_{2,2}+c_{2}h^{4}+O(h_{2}^{6})$
- Ora, como $h_{2}=\tfrac32 h_{3}$ temos $x(t+H)=R_{2,2}+ \frac{81}{16}c_{2}h_{3}^{4}+O(h_{3}^{6})$
- Ao igualar estas 2 equações temos: $c_{2}h_{3}^{4})=\frac{16}{65}(R_{3,2}-R_{2,2})$
- O que nos dá: $$R_{3,3}=R_{3,2}= \tfrac{16}{65}(R_{3,2}-R_{2,2})$$
e temos agora um erro de ordem $h^{6}$, apenas com 3 tentativas com o midpoint modificado (e ainda temos intervalos com 1 terço do tamanho o intervalo total!)

- Podemos generalizar isto. Cada tentativa pode ser representada como $R_{n,m}$, em que $n$ é o número de passos do midpoint modificado ($n=1\to h_{1}=H$, 1 passo) e $m$ será o número da tentativa, em que $R_{n,m}$ terá um erro de ordem $h^{2m}$. Apliquemos o processo acima para obter as fórmulas:
    - Numa certa tentativa temos $x(t+H)=R_{n,m}+c_{m}h_{n}^{2m}+O(h_{n}^{2m+2})$
    - Temos ainda: $x(t+H)=R_{n-1,m}+c_{m}h_{n-1}^{2m}+O(h_{n-1}^{2m+2})$
    - Sendo que $h_{n}=\frac{H}{n}$ e $h_{n-1}=\frac{H}{n-1}$, pelo que temos $\large h_{n-1}=\frac{n}{n-1}h_{n}$
    - Tal como antes, ao substituir isto na equação com $R_{n-1,m}$ e igualar as 2 equações de $x(t+H)$ resultantes, obtemos $$c_{m}h_{n}^{2m}=\frac{R_{n,m}-R_{n-1,m}}{(\frac{n}{n-1})^{2m}-1}\tag{Eq. 10.3}$$ o que nos dá a *fórmula geral do método de Bulirsch-Stoer*: $$R_{n,m+1}=R_{n,m}+\frac{R_{n,m}-R_{n-1,m}}{(\frac{n}{n-1})^{2m}-1}\tag{Eq. 10.4}$$

- Ora, podemos esquematizar este método desta forma, bastante familiar: 
![[Bulirsch - Stoer.png]]
Ou seja, este método funciona exatamente como a integração de Romberg. Isto ocorre porque ambos se baseiam na extrapolação de Davidson para resolver problemas diferentes.
- De notar que este método é adaptativo, temos que definir uma forma de ele parar, quando for atingida a precisão desejada.

- Um problema do Bulirsch-Stoer é que ele apenas determina o ponto final da solução da eq dif com uma precisão muito elevada. Para os restantes pontos apenas temos a solução obtida pelo método de midpoint modificado, que têm erro de ordem $h^{2}$.
- Outro ponto a notar é que, na prática, apenas estamos a expandir o erro de $x(t+H)$. Se este valor convergir de forma lenta, este método não é adequado. Assim, devemos manter $H$ *reduzido*.

- Ora, os 2 problemas acima podem facilmente ser resolvidos.
    - Consideremos que queremos a solução de uma eq dif entre $t=a$ e $t=b$. Simplesmente dividimos esse intervalo em $N$ intervalos de dimensão $\frac{b-a}{N}=H$ e aplicamos o método de Bulirsch-Stoer para cada um destes intervalos. Ora, devemos escolher $N$ grande o suficiente para ficarmos com uma imagem clara da solução, mas um $H$ reduzido o suficiente para o método convergir rapidamente / para nunca termos de fazer muitos passos.

- Este método permite-nos obter resultados melhores que o RK4 adaptativo, com menos trabalho. Tal como o método de Romberg, o Bulirsch-Stoer apenas será útil para eq difs em que a solução é minimamente suave e não varia muito rápido. Caso contrário, RK4 adaptativo será melhor.
- Além disso, este método será mais rápido que Runge-Kutta (quando a solução converge rápido).
## 10.1 - Aplicação
0. Tendo uma certa equação diferencial, dividir o intervalo em que queremos saber a solução em $N$ intervalos de dimensão $H$. Definir uma precisão desejada: $\delta$, por unidade de tempo.
1. Definir $n=1$. Usar o método do midpoint modificado para obter $R_{1,1}$.
2. Aumentar $n$ em 1 unidade e usar midpoint modificado para obter $R_{n,1}$
3. Usar a fórmula acima (Eq. 10.4) para obter $R_{n,2},R_{n,3},\dots,R_{n,n}$ (1 linha do diagrama)
4. Ao chegar ao fim da linha, usar a Eq. 10.3 para determinar o nosso erro atual. Comparar com $H\delta$ (que nos vai dar o erro desejado em cada um dos $N$ intervalos). Se o erro for maior, voltar para o passo 2. Senão, passar para o intervalo seguinte.

## 10.2 - Nota sobre o código
- Podemos guardar apenas a nossa linha atual e a linha anterior como listas/arrays.

## 10.3 - Tamanho do Intervalo
- Como vimos acima, ao resolver uma eq dif num intervalo, dividimo-lo em $N$ intervalos menores, de dimensão $H$. No entanto, nenhum destes valores pode ser muito elevado nem muito reduzido. Ou seja, surge a necessidade de determinar o melhor valor de $H$ de forma automática.

- Consideremos então que queremos obter a solução de uma eq dif de $t=a$ até $t=b$, usando $N$ intervalos menores de tamanho $H=\frac{b-a}{N}$
- Atuaremos agora de uma forma diferente da que vimos acima:
    1. Fazer o método como indicado na secção 10.1. Ora, fazer isto *apenas* até um certo valor máximo de $n$, normalmente por volta de $n=8$. Se eventualmente, em $n=n_{max}$ ainda não atingimos o erro desejado, dividimos o intervalo atual em 2 e passamos para o primeiro dos 2 subintervalos, repetindo o método nele.
    2. Fazer isto ao longo de todo o domínio em estudo. Iremos obter um resultado final com pontos distribuidos de forma não uniforme, o que faz sentido e e vai resultar numa performance melhor.

#computacional #programacao #resumo 