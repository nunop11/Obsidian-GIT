# Método de estudo de sistemas
1. Representamos o sinal de entrada com a sua transformada de Laplace
2. Utilizamos a *função de transferência* para estudar o sinal saída
3. Usar métodos de decomposição e Laplace inversa para determinar o sinal de saída em função do tempo.

# Função Transferência - Parte 2
- Antes vimos que, sendo $x(t)=e^{s_{0}t}$, então $x$ é uma função própria do sistema, sendo que: $y(t)=\lambda_{0}e^{s_{0}t}$, sendo $\lambda_{0}$ uma constante.

- Assim, podemos fazer a transformada de Laplace de $x(t)$. Ou seja, estamos a decompor o sinal de entrada num conjunto de exponenciais. Ora, vimos que cada exponencial irá dar origem a uma saída independente. Ou seja, se fizermos transformada de Fourier da entrada, podemos relacioná-la com a saída: $$Y(s)=H_{X(s)}X(s)$$
em que $H_{X(s)}$ é a função Transferência associada a $X(s)$. Isto porque a função apenas tem em consideração as exponenciais que formam $X(s)$. Ou seja, aqui estamos a "ignorar" as exponenciais que entrem no sistema e que não formem $X(s)$.

- Assim, temos a forma mais generalizada: $$\boxed{Y(s)=H(s)X(s)}$$em que $H(s)$ é a função transferência, que depende apenas do sistema em si.
- Assim, temos 3 formas de determinar $H(s)$:
    1. Conhecer a equação diferencial do sistema
    2. Conhecer a constituição interna do sistema
    3. Observar a saída correspondente a um sinal de entrada específico/especial.

> __*EXEMPLO 1*__
> ![[circuito RC exemplo.png]]
> Temos, do modelo das impedâncias, que $$Z_{R}=R \quad;\quad Z_{C}=\frac{1}{sC}$$
> Pelas Leis de Kirchhoff e Ohm Generalizada: $$V_{out}(s)=\frac{R}{R+ \frac{1}{sC}} V_{in}(s)$$
> Substituindo os valores de $R=10\Omega,C=0.01F$ ficamos com $$\frac{V_{out}}{V_{in}}=H(s)=\frac{s}{s+10}$$
> Assim, sendo $V_{in}(t)=u(t)\to V_{in}(s)=\frac{1}{s}~~,~~ \text{Re}[s]>0$ ficamos com $$V_{out}(s)=H(s)V_{in}(s)=\frac{1}{s+10}~~,~~\text{Re}[s]>-10$$
> Fazendo a transformada inversa desta transformada comum temos: $$V_{out}(t)=L^{-1}[V_{out}(s)]=e^{-10t}u(t)$$
> o que é o esperado para um circuito RC.

>__*EXEMPLO 2*__
>![[slits em serie ex.png]]
>Neste caso, basicamente consideramos que as duas partes à esquerda e direita são sistemas separados, que têm a sua própria função transferência (no da esquerda, $V_{in}$ é entrada e $V_{int}$ saída; no da direita $V_{int}$ é entrada e $V_{out}$ saída)

## H a partir da Eq Diferencial
- Vimos no início da UC que um SLIT pode ser descrito por uma equação do tipo $$\sum\limits_{n=0}^{N}\alpha_{n} \frac{d^{n}}{dt^{n}}y(t)=\sum\limits_{m=0}^{M}\beta_{m} \frac{d^{m}}{dt^{m}}x(t)$$
- Podemos então fazer transformada de Laplace dos 2 lados. Recordado a propriedade $\frac{d}{dt}x(t)\to sX(s)$ ficamos com:
$$\frac{Y(s)}{X(s)}= \frac{\sum_{m=0}^{M}\beta_{m}s^{m}}{\sum_{n=0}^{N}\alpha_{n}s^{n}}$$
- Ora, isto é a definição da função transferência. Ou seja, nos 2 exemplos e na mini dedução acima vemos que a função transferência $H(s)$ é uma divisão entre 2 polinómios de $s$. Podemos então definir: $$H(s)=\frac{N(s)}{D(s)}$$
- Sendo $z_{i}$ os zeros de $H$ e $p_{i}$ os seus polos, podemos escrever:
$$\small H(s) = \frac{\beta_{M}s^{M} + \beta_{M-1}s^{M-1} + \cdots + \beta_{1}s + \beta_{0}}{\alpha_{N}s^{N} + \alpha_{N-1}s^{N-1} + \cdots + \alpha_{1}s + \alpha_{0}} \to H(s)=K \frac{(s-z_{1})(s-z_{2})\cdots(s-z_{M})}{(s-p_{1})(s-p_{2})\cdots(s-p_{N})}$$
- Ou seja, conhecer os polos e zeros da função permite-nos obter $H(s)$ *a menos de 1 constante* $K$.

>__*EXEMPLO 3*__
>Consideremos que temos a equação diferencial que descreve um SLIT: $$2 \frac{d^{2}y}{dt^{2}}-3 \frac{dy}{dt} +5y = 10 \frac{dx}{dt}-7x$$
>Usando a propriedade $L[\frac{d}{dt}x(t)]=sX(s)$, podemos fazer transformada dos 2 lados da equação acima e ficamos com: $$2s^{2}Y(s)-3sY(s)+5Y(s)=10sX(s)-7X(s)$$
>Ficamos com: $$H(s)=\frac{Y(s)}{X(s)}=\frac{10s-7}{2s^{2}-3s+5}$$

>__*EXEMPLO 4*__
>Podemos também fazer o inverso do exemplo 3. 
>Consideremos a seguinte função transferência: $$H(s)=\frac{s^{2}}{s^{2}+20s+100}=\frac{Y}{X}$$
>Vemos então que isto equivale a: $$s^{2}Y(s)+20sY(s)+100Y(s)=s^{2}X(s)$$
>o que equivale a: $$\frac{d^{2}y}{dt^{2}} +20 \frac{dy}{dt} +100y = \frac{d^{2}x}{dt^{2}}$$

## Representação gráfica
- No EXEMPLO 2 ficamos com $H(s)=\frac{s}{(s+10)^{2}}$. Ou seja, $s=-10$ é um *polo duplo* e $s=0$ é o *zero*. O gráfico de $|H(s)|$ no plano imaginário fica assim:
![[Hs representacao espaço complexo.png]]
- A *ordem do sistema* é igual ao *número de polos* (número de armazenadores de energia do sistema: 1 resistência e 1 condensador -> ordem 2 -> 2 polos).

## Representações de H
- Acima já vimos:
**Forma Padrão**
$$H(s) = \frac{\beta_{M}s^{M} + \beta_{M-1}s^{M-1} + \cdots + \beta_{1}s + \beta_{0}}{\alpha_{N}s^{N} + \alpha_{N-1}s^{N-1} + \cdots + \alpha_{1}s + \alpha_{0}}$$
**Forma Fatorizada**
$$H(s)=K \frac{(s-z_{1})(s-z_{2})\cdots(s-z_{M})}{(s-p_{1})(s-p_{2})\cdots(s-p_{N})}$$
**Forma das Constantes de Tempo**
$$H(s)=K \frac{(1-sT_{1})(1-sT_{2})\cdots(1-sT_{M})}{(1-s\tau_{1})(1-s\tau_{2})\cdots(1-s\tau_{N})}$$
sendo $T_{i}=\frac{-1}{z_{i}} \quad;\quad \tau_{i}=\frac{-1}{p_{i}}$

# Associação de SLITs
- Vimos no exemplo 2 que um sistema pode ser formado por 2 subsistemas, cada um com a sua função transferência.
- Ora, vejamos como é que a função transferência de um sistema pode ser obtida a partir dos seus subsistemas. Ou, melhor dizendo, vejamos como é que podemos obter a função total correspondente a vários sistemas associados.

## Sistemas em Série
![[slits serie.png]]
- Isto é o que tínhamos no exemplo 2.
- Tendo $$H_{1}(s)=\frac{Y_{1}(s)}{X(s)} \quad \quad;\quad \quad H_{2}(s)=\frac{Y(s)}{Y_{1}(s)}$$
Obtem-se: $$H(s)=H_{1}(s)H_{2}(s)$$
- Podemos concluir que a ordem dos sistemas não importa.

## Sistemas em Paralelo
![[slits paralelo.png]]
- Usando a propriedade de Linearidade:
$$\begin{align*}
Y(s)&= Y_{1}(s)+Y_{2}(s)\\
&= H_{1}X+H_{2}X\\
&= [H_{1}+H_{2}]X=H(s)X(s)
\end{align*}$$
ou seja, para 2 circuitos em paralelo:
$$H(s)=H_{1}(s)+H_{2}(s)$$
- Novamente, a ordem não importa.

## Sistemas com Realimentação
![[slits realimentacao.png]]
- Temos $$Y(s)=F(s)[X(s)+ G(s)Y(s)]$$
e ficamos com $$H(s)= \frac{F(s)}{1-F(s)G(s)}$$
- Consideremos que temos um circuito em que $G(s)$ é a função transferência. O circuito assim terá uma função transferência que será $H(s)\approx \frac{1}{G(s)}$

#sinais #fisica
