# Estabilidade de SLIT
- Na prática, um *sistema estável* significa que uma entrada limitada resulta numa saída limitada. De notar que uma funçaõ é *limitada* se $|x(t)|<M_{1}<\infty,\forall t$

- Tendo um SLIT, para ele ser estável, tem que haver alguma condição a verificar na sua resposta impulsional. Ou seja, tendo $y(t)=x(t)*h(t)$, facilmente obtemos $|y(t)|=|\int_{-\infty}^{+\infty}x(\tau)h(t-\tau)d \tau|$. Assim, para que $y(t)$ seja limitado é necessário que $$|y(t)|<M_{1}\int_{-\infty}^{+\infty}|h(t-\tau)d \tau|$$
- Assim, para $y$ ser limitado é necessário que $$\int_{-\infty}^{+\infty}h(t)dt<M_{2}<\infty $$
- Daqui se obtem o teorema:
> Um SLIT é *estável* se a RC da função transferência **contém o eixo imaginário**

## Sistema Causal
- Antes já falamos que um sistema causal é aquele em que a saída depende apenas do sinal de entrada.
- Mas, de uma forma mais formal:
> Um sistema é *causal* se 2 sinais de entrada, $x_{1},x_{2}$, iguais até $t=t_{0}$ derem origem a 2 sinais de saída, $y_{1},y_{2}$, que também são iguais até $t=t_{0}$. Ou seja: $$x_{1}(t)=x_{2}(t)~~,~~t<t_{0}\Rightarrow y_{1}(t)=y_{2}(t)~~,~~t<t_{0}$$
> Por outras palavras, para um SLIT ser causal, é necessário que a RC da função de transferência seja à direita de uma reta paralela ao eixo imaginário.

- Para um sistema linear e causal teremos:
$$x(t)=x_{1}(t)-x_{2}(t)=0~~,~~t<t_{0}\Rightarrow y(t)=y_{1}(t)-y_{2}(t)~~,~~t<t_{0}$$

- Ora, um SLIT é *linear*, *causal* e **invariante no tempo**. Assim, para um SLIT causal temos:
$$\boxed{x(t)=0~~,~~t<0\Rightarrow y(t)=0~~,~~t<0}$$
por palavras: isto indica que se só iremos ter um sinal de saída quando aplicarmos um sinal de entrada.
>Ou seja, para um SLIT ser ***causal e estável*** é necessário que todos os polos da função transferências estajam na metade esquerda do plano $s$, sendo a RC a região à direita do maior polo (não módulo).

- Como, num SLIT, $y(t)=x(t)*h(t)=h(t)*x(t)$, então se o SLIT for causal, temos $$h(t)=0~~,~~t<0 \quad \quad sendo~~que~~~~H(s)=L[h(t)]~~,~~ \text{Re}[s]>\sigma$$

# Critérios de Estabilidade
- Um SLIT é causal e estável se todos os polos estiverem à esquerda do eixo imaginário (o eixo está dentro da RC). No entanto, em certos sistema pode ser um bocado trabalhoso fazer isso. Assim temos critérios de estabilidade
## Critério de Estabilidade de Hurwitz
- Um SLIT é estável se o polinómio da base da função transferência for um polinómio de Hurwitz.
1. Para um polinómio ser de Hurwitz é que todos os *coeficientes sejam positivos*. Para $N=1,N=2$ estre critério chega

Temos a *matriz de Hurwitz*: $$\begin{pmatrix} a_1 & 1 & 0 & 0 &\dots& 0 \\ a_3 & a_2 & a_1 & 1 &\dots & 0 \\ a_5 & a_4 & a_3 & a_2 &\dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \cdots & 0 & a_N \end{pmatrix}$$
sendo que os seus menores são os **determinantes de Hurwitz**: $$\Delta_\mu = \begin{pmatrix} b_1 & 1 & 0 & 0 &\dots& 0 \\[0.2cm] b_3 & b_2 & b_1 & 1 &\dots & 0 \\ b_5 & b_4 & b_3 & b_2 &\dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ b_{2\mu - 1} & b_{2\mu - 2} & b_{2\mu - 3} & \cdots & b_{\mu + 1} & b_{\mu} \end{pmatrix}$$
Sendo $\mu \in \{1, 2, \dots, N\}$ e onde se definiu:
$$b_i = \begin{cases}
1&; &i = 0 \\
a_i &; &1 < i \le N \\
0 &; & i > N
\end{cases}$$
2. Um polinómio é de Hurwitz se todos os *determinantes de Hurwitz forem positivos* 
EX:
![[hurwitz exemplo.png]]

## Critério de Estabilidade de Routh-Hurwitz
- Tendo-se $Q$ do tipo $$Q(s)=b_{N}s^{N}+b_{N-1}s^{N-1}+b_{N-1}s^{N-2}+\cdots+b_{1}s+b_{0}$$
- Dividimos os coeficientes em 2 linhas:
$$\begin{align*}
linha~ N:\quad~~~~ b_{N} \quad b_{N-2} \quad b_{N-4} \quad\dots\\
linha~N-1:\quad b_{N-1} \quad b_{N-3} \quad b_{N-5} \quad\dots\\
\end{align*}$$
sendo que se $N$ for
    - Ímpar - $b_{1}$ é ultimo termo da linha $N$ e $b_{0}$ da linha $N-1$
    - Par - $b_{0}$ é ultimo da linha $N$ e $0$ é ultimo termo da linha $N-1$

- A linha $N-2$ é formada da seguinte forma:
$$\small linha~N-2: \frac{b_{N-1}b_{N-2}-b_{N}b_{N-3}}{b_{N-1}} \quad \frac{b_{N-1}b_{N-4}-b_{N}b_{N-5}}{b_{N-1}} \quad \frac{b_{N-1}b_{N-6}-b_{N}b_{N-7}}{b_{N-1}} \quad \dots$$
- A linha $N-3$ é definida usando as linhas $N-1,N-2$ de forma igual.
- Continuamos até chegar à linha $N-N=0$
- Esta matriz de $N+1$ linhas é a **matriz de Routh**

- O critério de Routh-Hurwitz diz então que o SLIT será estável apenas se todos os valores da primeira coluna da matriz de Routh forem *não nulos e tiverem o mesmo sinal*.
- Se o sinal dos elementos da 1ª coluna variar, o número de variações é o número de polos à direita do eixo imaginário.

# Sistemas com Realimentação
- Ao ter um sistema com realimentação, a função de transferência que obtemos inclui a influencia do percurso direto e a do percurso de realimentação. Por vezes isso é mau, porque perdemos informação acerca do percurso direto.

## Função Inversa
![[realimentacao inversa.png]]
- Este sistema pode ser descrito por $$Y=K[X-GY]$$
de onde se tira: $$\frac{Y}{X}=H = \frac{K}{1+KG}\approx \frac{1}{G}$$
- Ou seja, esta configuração terá uma função inversa a um circuito com a função $G(s)$.

## Estabilizar Ganho
- Temos o seguinte sistema com amplificador:
![[realimentacao ganho.png]]
- Que é representado por $$Y=A[X-KY]$$ de onde se, tira, tal como no caso acima: 
$$H(s)=\frac{A(s)}{1+KA(s)}\approx \frac{1}{K}$$
- De notar que, sendo $K$ constante, a função transferência desta configuração será sempre a mesma, independentemente do ganho.

## Interpretação matemática - 1ª Ordem
- Temos um circuito $X \Longrightarrow H \Longrightarrow Y$, em que $H(s)=\frac{b}{s-a}~~,a>0,b>0$
- Ora, teremos um polo em $s=a>0$, ou seja, o sistema é *instável*. Assim, queremos torná-lo estável.
- Consideremos que se faz a seguinte configuração:
![[realimentacao negativa.png]]
em que $K>0$ é uma constante.
- Aqui o sinal negativo a ligar a realimentação ao sumatório diz-nos que temos **Realimentação Negativa**

- Agora temos: 
$$Q(s)=\frac{Y}{X}=\frac{H}{1+KH}=\frac{b}{s-a+bK}$$
ou seja, temos um polo em $s=a-bK$. 
- Assim, ao regular $K$ mudamos a resposta do sistema
- Se $K> \frac{a}{b}$, o sistema torna-se *estável*.

- De notar que se, inicialmente tivéssemos $a<0$, o sistema seria estável. Nesse caso, ao introduzir $K<0$ iriamos estar a tornar o sistema instável. Aqui teríamos **Realimentação Positiva**.

## Interpretação matemática - 2ª Ordem
- Consideremos um circuito do mesmo tipo que o anterior, mas agora com $H(s)=\frac{b}{s^{2}+a}$. Aqui teríamos polos em $s=\pm \sqrt{a}$, ou seja, o sistema é imaginário porque a RC não contém o eixo imaginário para qualquer valor de $a$.
- Voltemos a repetir o processo anterior:
![[realimentacao negativa instavel.png]]
Temos:
$$H_{realimentacao} = \frac{H}{1+KH}=\frac{b}{s^{2}+a+Kb}$$
- Vemos que o coeficiente do termo $s$ do polinómio é nulo, ou seja, pelo critério de Hurwitz, o sistema é instável.

- Tentemos então fazer uma configuração de **realimentação proporcional diferencial**:
![[realimentacao negativa dif proporcional.png]]
- Agora temos:
$$H_{realimentacao}=\frac{H}{1+GH}=\frac{b}{s^{2}+a+b(K_{1}+K_{2}s)}=\frac{b}{s^{2}+bK_{2}s+(a+bK_{1})}$$
- Como só temos $N=2$, o sistema já é estável desde que $bK_{2}>0~,~a+K_{1}b>0$

# Configurações de Realimentação
![[realimentacao geral.png]]
- Como vimos nos 2 casos acima, o comportamento de um sistema com realimentação depende da função transferência do ramo de realimentação, $G(s)$. Esta é chamada de *Função transferência de Controle* ou **Controlador**. Temos então alguns tipos:
    - **Controlador proporcional** $$G(s)=K_{p} \quad \quad f(t)=K_{p}y(t)$$
    - **Controlador Diferencial** $$G(s)=K_{d}s \quad \quad f(t)=K_{d} \frac{dy}{dt}$$
    - **Controlador Integral** $$G(s)=\frac{K_{i}}{s} \quad \quad f(t)= K_{i} \int y(t)dt$$
- E podemos fazer combinações:
    - **Controlador Proporcional Diferencial** $$G(s)=K_{p}+K_{d}S \quad \quad f(t)=K_{p}y(t)+K_{d} \frac{dy}{dt}$$
    - **Controlador Proporcional Integral Diferencial** $$G(s)=K_{p}+K_{d}s+ \frac{K_{p}}{s} \quad \quad f(t)= K_{p}y(t)+K_{d} \frac{dy}{dt} + K_{i} \int y(t)dt$$

#sinais #fisica