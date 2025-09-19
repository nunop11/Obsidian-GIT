- Vamos ver uma lei que descreve o tráfego automóvel numa auto-estrada sem entradas nem saídas na região em estudo.
- Podemos escrever a equação de Advecção como uma equação de conservação:
$$u_{t}+(vu)_{x}=0$$
em que $u$ representa a densidade de carros, que se movem a velocidade $v$. Ou seja, estudamos os carros como um conjunto. Consideremos que $u=0$ significa que não há carros nessa região e $u=1$ a estrada está completamente congestionada.
- Podemos ainda escolher as unidades do problema de mdoo que, além de ter $u$ conforme explicado acima, tenhamos $v_\text{max}=1$.

- Se considerarmos que todos os carros se movem a velocidade $v$ constante, o $v$ sai fora da derivada e voltamos à equação de advecção.
- Mas isso obviamente não é realista.
    - Consideremos que onde há mais carros a velocidade será menor, tal que quando temos $u=1$ os carros não se movem. Podemos simplesmente considerar: $$v(u)=1-u$$

- Daqui surge:
$$u_{t}+(u(1-u))_{x}=0$$
em que $u(1-u)=vu=f(u)$ é o *fluxo de carros*, quantidade de carros que passa numa secção por unidade de tempo.
- Podemos então traçar o fluxo:
![[fluxo.png|400]]
de notar que na equação de advecção o fluxo é linear.

- Fazendo a derivada temos a equação:
$$u_{t}+(1-2u)u_{x}=0$$
à derivada do fluxo $f'(u)=1-2u$ chamamos de *velocidade caraterística*, que pode ser vista como a velocidade a que se desloca a informação. (Pode ser negativa)

## Ondas de Choque
- Podemos usar o método de Lax-Friedrichs visto na parte de advecção para resolver esta equação (apesar de não ser uma equação de advecção linear!). Temos:
![[impulso.png|350]]       ![[Pasted image 20240602001423.png|350]]
- Inicialmente começamos com uma distribuição gaussiana suave. Mas conforme fizemos a evolução do sistema ficamos com algo descontínuo. Isto NÃO é um erro, NÃO é algo que ocorreu devido a instabilidade deste método.
- Explicação: Na região de baixa densidade atrás do pico, os carros deslocam-se a uma velocidade superior aos que estão na região de maior congestionamento mais à frente. Assim alcançam-nos, aumentando a densidade, e conduzindo a um aumento brusco da densidade na parte de trás do congestionamento. Isto leva, eventualmente, a um engarrafamento: carros antes do congestionamento viajam depressa (têm a estrada livre), até que de repente atingem uma zona altamente congestionada, pelo que têm que travar a fundo!

## Velocidade de Onda de Choque
- Quando simulamos uma rua com um semáforo (alta densidade de tráfego com pouca densidade mesmo antes -- temos um degrau), gera-se uma onda de choque que se move *para trás*.
- Ora, esta onda de choque move-se com uma velocidade, que podemos calcular. Traçamos uma linha a separar as zonas de alta e baixa densidade de carros.
![[Pasted image 20240602002858.png]]
    - $u_{l}$ e $u_{r}$ são as densidades de carros à esquerda e direita desta linha.

- Consoante passa tempo vão se juntando carros ao engarrafamento. Assim, temos carros um fluxo $f(u_{l})$ de carros a vir da esquerda e a juntar-se à fila. Por outro lado, podemos definir o fluxo $f(u_{r})$ de carros que se afastam da linha.
- Ora, como vimos, consoante chegam carros ao engarrafamento temos uma onda de choque a mover-se para a esquerda. Esta onda consiste numa degrau a deslizar, logo esta linha é a *parte vertical do degrau* que portanto se move com a onda de choque. Consideremos que se move com velocidade $s$.

- Assim, conforme esta se move, carros que estavam à esquerda passam para a direita.
- O fluxo de carros a deixarem de estar do lado esquerdo é $su_{l}$. O fluxo de carros que se junta ao lado direito é $su_{r}$. Para não haver acumulação de carros é preciso que estes 2 fluxos se equilibrem:
$$f(u_{l})-f(u_{r})=s(u_{l}-u_{r})$$
![[Pasted image 20240602004022.png]]
sendo esta a *condição de Rankine-Hugoniot*. Qualquer onda de choque que seja solução de uma equação hipérbolica obedece a isto!

## Ondas de Rarefação
- Consideremos agora que se faz uma condição inicial do tipo: $u=1$ para $0<x<1/2$ e $u=0$ para $1/2<x<1$ (CI II do TPC3) -- CI não contínua
- Se resolvermos a equação para este caso vemos que *não* aparece uma onda de choque.
- O que observamos é que após o instante inicial o traçado torna-se contínuo. Após o semáforo mudar para verde, os carros na frente da fila aceleram e afastam-se; de seguida os que estvam atrás destes aceleram por sua vez e afastam-se dos imediatamente atrás, e assim sucessivamente.
- Chamamos a esta uma *onda de rarefação de carros*.

- Se traçarmos *curvas caraterísiticas* e
    - Se sobrepusrem, então teremos **choque**:![[Pasted image 20240602005202.png]]
    - Se não se sobrepusrem /  afastam-se temos **rarefação**:![[Pasted image 20240602005239.png]]

- Ou, de outra forma. Tendo-se as densidades à esquerda e direita $u_{l},u_{r}$:
    - Temos **choque** se $f'(u_{l})>f'(u_{r})$ (maior velocidade caraterística à esquerda)
    - Temos **rarefação** se $f'(u_{l})<f'(u_{r})$
- Devemos aliás, ter:
$$f'(u_{l})>x> f'(u_{r})$$

## Problema de Riemann
- Os casos de semáforos acima são todos problemas de Riemann: consistem numa lei de conservação hiperbólica, com CI constante por ramos, com 1 descontinuidade:
$$u(x,0)\begin{cases}
u_{l} & ; & x<x_{0} \\
u_{r} & ; & x>x_{0}
\end{cases}$$
- O método upwind consiste em resolver com exatidão um problema de Riemann. O método Lax-Friedrichs consiste em aproximar o problema de Riemann.
- Na prática, devido ao quão complexas as soluções destes problemas se podem tornar, o melhor a usar é métodos que tentam resolver aproximadamente estes problemas.

## Korteweg-De Vries (KdV)
- Esta equação serve de modelo de ondas em meios com baixa profundidade:
$$\frac{\partial u}{\partial t} + \frac{\partial^{3}u}{\partial x^{3}} +6 u \frac{\partial u}{\partial x}= 0$$
- Podemos resolver com métodos espectrais. Começamos por reescrever a eq:
$$\partial_{t}u+3 \partial_{x}(u^{2})+\partial_{x}^{3}u=0$$
- A sua FT será:
$$\partial_{t}\hat{u} + 3ik \hat{u^{2}}-ik^{3}\hat{u}=0$$
- Podemos separar isto em partes (método *split step*):
1. A equaçao $\partial_{t}\hat{u}=ik^{3}\hat{u}$ é facilmente resolvida de forma exata
2. A equação $\partial_{T}\hat{u}=-3ik(\hat{u^{2}})$ é mais complicada. 

- O método split step consiste em fazer alteranadamente cada uma destas equações, consoante avançamos de $t$ para $t+\Delta t$ (a mesma ideia por detrás do esquema de MacCormick do TPC3). Temos:
$$\begin{align*}
\hat{u}_{1}(k,t+\Delta t)&= \hat{u}(k,t)e^{i k^{3}\Delta t}\\
\hat{u}(k,t+\Delta t)&= \hat{u}_{1}(k,t+\Delta t)-3ik\Delta t(\hat{u^{2}_{1}})
\end{align*}$$
(teremos uma solução melhor se usarmos RK4 para resolver o passo 1)
- No entanto, acima temos $\hat{u_{1}^{2}}$ que é a FT de $u_{1}$ ao quadrado. Assim:
$$\begin{align*}
\hat{u}_{1}(k,t+\Delta t)&= \hat{u}(k,t)e^{ik^{3}\Delta t}\\
\hat{u}(k,t+\Delta t)&= \hat{u}_{1}(k,t+\Delta t)-3ik\Delta t \left[ \mathcal{F}\left(\mathcal{F}^{-1}[\hat{u}_{1}(k,t+\Delta t)] \right)^{2} \right]
\end{align*}$$
e agora temos tudo em função de $\hat{u},\hat{u}_{1}$.
- A resolução simplesmente consiste em aplicar esta fórmula repetidamente e no final fazer IFFT.

- No notebook `KdV_FFT` temos uma resolução desta eq com FFT. Não entendo nada tho.