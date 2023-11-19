# SLIT com várias entradas e saídas
- Consideremos o seguinte sistema SLIT com $M$ entradas e $K$ saídas:
![[varias entradas e saidas slit.png]]
- Sendo $H(s)$ uma matriz, a entrada $ij$ é a função de transferência que relaciona a entrada $j$ com a saída $i$:
$$Y_{i}(s)=H_{ij}(s)X_{j}(s)$$
## Em Série
![[combinacao slits.png]]
- Tendo 2 sistemas de várias entradas e saídas em série, vemos logo que o número de saídas do Sist 1 tem que ser igual ao número de entradas do Sist 2.
- Temos: $$Y_{1}=H_{1}X \quad \quad;\quad \quad Y=H_{2}Y_{1}$$
- Ou seja, tal como vimos antes para sistemas em série: $$H(s)=H_{2}(s)H_{1}(s)$$
- No entanto, ao contrário de sistemas de 1 entrada e 1 saída, *a ordem importa*. $H=H_{2}H_{1}\neq H_{1}H_{2}$

## Em paralelo
- Neste caso, tal como vimos para sistemas de 1 entrada/saída: $$H(s)=H_{1}(s)+H_{2}(s)$$
- De notar que o sistema 1 e 2 têm que ter os mesmo números de entradas e saídas.

## Com Realimentação
![[slit com realimentacao ex.png]]
- Juntando os 2 tipo anteriores temos:
$$Y=F[X+GY]$$
de onde obtemos:
$$[I-FG]Y=FX \quad \quad;\quad I\to indentidade~,~K\times K$$
De onde se tira $Y = \frac{F}{[I-FG]}X$. Ou seja, de forma semelhante ao que tínhamos com o sistema com 1 entrada e 1 saída:
$$H(s)=[I-F(s)G(s)]^{-1}F(s)$$

# H no espaço de Estados
- Vimos atrás que um SLIT com 1 entrada e 1 saída, com 1 variável de estado $z$ pode ser represetnado da seguinte forma:
![[espaco estados diagrama blocos repetido idc.png]]
- Ora, isto dá-nos as equações:
$$\begin{align*}
\frac{dz}{dt} &= Az+Bx\\
y &=  Cz + Dx
\end{align*}$$
- Assim, podemos dividir o diagrama em blocos em 2 partes:
![[divisao diagrama blocos.png]]
Sendo:
    - $\mathbf{x}$ - vetor com $M$ sinais de entrada
    - $\mathbf{y}$ - vetor com $K$ sinais de saida
    - $\mathbf{z}$ - vetor com $N$ variáveis de estado
    - $A$ - matriz $N\times N$ 
    - $B$ - matriz $N\times M$
    - $C$ - matriz $K\times N$
    - $D$ - matriz $K\times M$

- Assim, usando o que vimos acima:
$$H_{1}=D \quad ;\quad H_{21}=B \quad;\quad H_{23}=C$$
para $H_{22}$ apenas usamos a equação de $H$ para o sistema com realimentação que vimos acima. O integrador fica $\frac{1}{s}$, tal como indicado pela propriedade de transformadas de Laplace: $L[\int x d\tau]=\frac{1}{s}X$. Ou seja:
$$H_{22}=\left[I- \frac{1}{s}A \right]^{-1}\cdot \frac{1}{s}I=[sI-A]^{-1}$$
- Ora, como $H_{21},H_{22},H_{23}$ represetam 3 subsistemas em série temos:
$$H_{2}=C[sI-A]^{-1}B$$
- E o sistema completo consiste de $H_{1},H_{2}$ em paralelo. Assim:
$$H=H_{1}+H_{2}=C[sI-A]^{-1}B+D$$

- Ora, a equação de H: $H=C[sI-A]^{-1}B+D$ que obtivemos acima é **Invariante**, ou seja, será sempre assim independentemente das variáveis usadas.

# Transformada Unilateral e SLIT
- Vimos atrás o que é uma transformada de Laplace Unilateral em termos matemáticos: $$L[x(t)]=X_{U}(t)=\int_{0}^{\infty}x(t)e^{-st}dt$$
- Esta transformada é útil para resolver *sistemas com sinal de entrada causal*, ou seja da forma: $$x(t)=f(t)u(t)$$
- Estes problemas consistem em analisar o sistema a partir do instante em que $x$ se torna não nulo (que iremos considerar como sendo $t=0$), conhecendo o sistema nesse instante: **Condições Iniciais**.

>__*EXEMPLO 1*__
>Consideremos o sistema descrito pela equação abaixo, com as seguintes condições iniciais: $$\frac{d^{2}y}{dt^{2}} + 3 \frac{dy}{dt} + 2y = x \quad \quad;\quad \begin{cases}y(0)=3\\ \frac{dy}{dt}(0)=-5\end{cases}$$
>Temos: $y(t)\to Y(s)$. Conforme o que vimos sobre transformadas unilaterais: $$\begin{align*}
\frac{dy(t)}{dt}\to sY(s)-y(0)&= sY(s)-3\\
\frac{d^{2}y(t)}{dt^{2}}\to s^{2}Y(s)- \frac{dy}{dt}(0)-sy(0)&= s^{2}Y(s)-3s+5
\end{align*}$$
> E assim a equação diferencial se torna numa equação algébrica: $$[s^{2}Y(s)-3s+5] + 3[sY(s)-3] + 2Y(s)=X(s)$$
> E de onde obtemos: $$Y(s)= \frac{X(s)}{s^{2}+3s+2} + \frac{3s+4}{s^{2}+3s+2}$$
> em que o primeiro termos corresponde à resposta do sistema para $t>0$ devido ao sinal de entrada e o segundo corresponde à resposta do sistema devido às condições iniciais.

- Ou seja, recapitulemos o que aprendemos com o exemplo 1:
    - Num sistema com sinal de entrada causal a evolução é influenciada pelo sinal de entrada/equação diferencial, mas também é influenciada pelas condições iniciais.
    - Além disso, se as condições iniciais forem todas nulas, temos que $H=Y/X$ 
    - Se as condições iniciais não forem nulas temos $Y\ne HX$.

> __*EXEMPLO 2*__
> No exemplo 1 partimos da eq dif com condições iniciais não nulas. Vamos continuar com condições inicias não nulas, mas vamos partir de $H$. Assim, temos:
> $$H(s)=\frac{1}{s^{2}+3s+2} \quad \quad;\quad \begin{cases}y(0)=2\\ \frac{dy}{dt}(0)=0\end{cases}$$
> Começamos por considerar o sistema com $t<0$, ou seja, consideramos o sistema antes de se aplicar o sinal de entrada, pelo que podemos usar: $Y=HX$. Assim: $$Ys^{2}++3Ys+Y=X\Longrightarrow \frac{d^{2}y}{dt^{2}} +3 \frac{dy}{dt} +2y = x$$
> E já está. Agora temos a equação diferencial e apenas repetimos exatamente o que fizemos no exemplo 1.
>
>Ficamos com $$Y(s)=\frac{2s^{2}+6s+1}{s^{2}+3s+2}=\frac{1/2}{s}+ \frac{3}{s+1}+ \frac{3/2}{s+2}$$
>e, ao fazer as transformadas de Laplace inversas, nos dá:
>$$y(t)= \left[ \frac{1}{2} + 3e^{-t} - \frac{3}{2} e^{-2t} \right]u(t)$$
>em que $\frac{1}{2}$ é constante no tempo e nos dá o **Regime estacionário** e os outros 2 termos nos dão o **Regime transitório**.

#sinais #fisica
