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