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

#computacional #programacao #resumo 