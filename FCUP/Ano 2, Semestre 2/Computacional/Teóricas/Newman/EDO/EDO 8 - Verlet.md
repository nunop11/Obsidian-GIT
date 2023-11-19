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

#computacional #programacao #resumo 