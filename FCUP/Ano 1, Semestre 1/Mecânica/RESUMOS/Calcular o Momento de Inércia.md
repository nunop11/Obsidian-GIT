# Calcular o Momento de Inércia
- Notas tiradas de https://youtu.be/9cuKlt15yCo
- Representa o quanto um corpo resiste a alterações à sua velocidade angular. OU seja, o quanto resiste a tentativas de o tentar parar ou começar a rodar.
 - O objetivo deste resumo é saber calculá-lo:

## I de um ponto de massa
- Seja este um ponto de massa $m$ e a uma distância $r$ do ponto de referência. Assim tem-se:
$$I=mr^2$$
- Se tivermos um sistema de pontos de massa, tem-se que:
$$I_{sistema}=\sum m_ir_i^2$$
 # Corpo com distribuição de massa uniforme - caso geral
 - Imagine-se que se tem um corpo com distribuição de massa uniforme assim:
![[Corpo distribuição contínua.png]]
- Nesse caso, tem-se que 
    $$I=\int_0^M r^2 dm$$
    ## Anel (infinitamente fino)
    ### Forma 1 (Simples)
![[anel infinitamente fino.png]]
- Tendo assim um anel infinitamente fino. O centro do anel é o centro da rotação. Um ponto anel tem massa $m$ e a massa total do anel é $M$
- Consideramos que $r$ é independente de $m$.
- Partindo do caso geral tem-se então:
$$I=\int_0^Mr^2dm=r^2\int_0^Mdm \leftrightarrow$$
> $$I = r^2M$$
### Forma 2 (Mais complicado, mas geral)
-No estudo desta forma, uma vez que se considera que este tem a massa uniformemente distribuida, conclui-se que:
> $$\begin{align}
\frac{dm}{M}=\frac{dl}{L}, && \frac{dm}{M}=\frac{dA}{A}, && \frac{dm}{M}=\frac{dV}{V}
\end{align}$$
(nota: cada um destes refere-se ao comprimento (l/L), Área (A) e Volume (V) de um corpo em estudo, e como em todos estes casos se tem que a massa de uma parte é proporcional à massa do todo da mesma forma que o commprimento, área e volume da parte em estudo são proporcionais ao do todo)

- Isto permite-nos substituir o $dm$ na equção geral obtida anteriormente.
- Tem-se então que 
$$dm = M\frac{dl}{L}$$
- O "comprimento" de um anel assim é o seu diametro, logo -> $L = 2\pi r$
- Sendo theta o ângulo ao centro correspondente à zona do anel em estudo.tem-se que -> $dl=r d\theta$
 - Substituindo estas coisas na fórmula original, fica-se com:
 $$dm = M\frac{rd\theta}{2\pi r}=M\frac{d\theta}{2\pi}$$
 - Então, o momento de inércia deste anel é dado por
 $$I=\int r^2 M \frac{d\theta}{2\pi}$$
 , logo:
 $$I=\frac{Mr^2}{2\pi}\int_0^{2\pi}d\theta=\frac{Mr^2}{2\pi}.2\pi=Mr^2$$
 - Que é a equação que obtivemos anteriormente, mas agora obtivé-mo-la de uma forma simples e geral.

## Vara a rodar em torno de um eixo na ponta
![[vara a rodar em torno da extremidade.png]]
- Usamos o mesmo processo que anteriormente. Tomamos uma pequena secção da vara, com comprimento $dx$. Esta secção estará a uma distância $x$ do eixo de rotação (que consideramos estar à esquerda para simplificar os cáculos). A vara tem um comprimento L
- recordando as fórmulas obtidas anteriormente temos $$\frac{dm}{M}=\frac{dx}{L}$$
- Assim,
$$I=\int x^2M.\frac{dx}{L}$$
, logo 
$$I=\frac{M}{L}\int_0^L x^2dx=\frac{M}{L}.\frac{x^3}{3}\Biggr|_0^L=\frac{1}{3}ML^2$$
## Vara com eixo de rotação no seu centro
- Este caso é diferente do anterior. No anterior existiam pontos a uma distância máxima do eixo de rotação, pelo que se tinha I máximo. Assim, neste caso, com mais pontos mais perto do eixo, o I será sempre menor.
- Realizamos exatamente o mesmo processo que anteriormente, até chegar a  
$$I=\frac{M}{L}\int_0^L x^2dx$$
em que o intervalo de integração muda. Não estamos a estudar os pontos a que estão nas posições 0 a L relativamente ao eixo. Estaremos invés a estudar pontos nas posições $-\frac{L}{2}$ a $\frac{L}{2}$. Tem-se então:
$$I=\frac{M}{L}.\frac{x^3}{3}\Biggr|_\frac{-L}{2}^\frac{L}{2}=\frac{M}{L}[\frac{L^3}{24} + \frac{L^3}{24}]$$
, logo:
$$I=\frac{ML^2}{12}$$

## Disco de área A
![[disco de área A.png]]
- Temos então um disco que consideramos como sendo infinitamente fino. Neste, estudamos um anel de grossura $dx$, a uma distância $x$ do centro do disco
- O disco tem área $A=\pi R^2$

- Mais uma vez, usando as formulas obtidas anteriormente e aplicaremos a formula de A, tendo então:
$$\frac{dm}{M}=\frac{dA}{A}$$
- Ora, para obter $dA$, temos que fazer uma subtração. A área do nosso anel será a diferença entre a área do círculo maior, de raio R, e o círculo de raio menor, igual a $x$. Após fazer os cáculos, obtem-se que:
$$dA=2\pi x. dx$$
- Assim, aplicando o valor de $dA$ obtido e isolando o $dm$ da fórmula anterior, obtem-se:
$$dm=M.\frac{2\pi xdx}{\pi R^2}=M.\frac{2 xdx}{R^2}$$
- Aplicando a fórmula geral:
$$I=\int x^2 . \frac{2 M x. dx}{R^2}=\frac{2M}{R^2}\int x^3 dx=\frac{2M}{R^2} . \frac{x^4}{4}\Biggr|_0^R$$
- Calculando a integral, obtem-se:
$$I=\frac{1}{2}MR^2$$

## Disco com espessura L
![[disco com espessura (1).png]]
- Este disco tem uma espessura L e uma densidade igual a $\rho$  
- Mais uma vez, repete-se o método geral de antes.
- Começando com as fórmulas do íncio. Tem-se
$$\frac{dm}{M}=\frac{dv}{V} \leftrightarrow dm=\frac{M}{V}dv$$
- Tendo o valor da densidade do sólido, pode-se ainda obter que:
$$dm=\rho dv$$

![[disco com espessura (2).png]]
- No interior do disco, consideramos a existência de um disco de um anel, a uma distância $x$ do centro do disco, e com uma grossura de $dx$, tendo também uma espessura L.
-  Uma vez que a área do anel é facilmente obtida e igual a $2\pi x.dx$, e uma vez que o anel tem espessura $L$, obtem-se se a área da parte do sólido em estudo:
$$dv=2\pi x . dx. L$$
- Substituindo na equação geral, 
$$I=\int x^2 \rho.2\pi x.dx L=2\pi \rho L \int x^3dx=2\pi\rho L . \frac{x^4}{4}\Biggr|_0^R$$
- Calculando a integral, obtem-se:
$$I=2\pi\rho L .\frac{R^4}{4}=2\pi.\frac{M}{\pi R^2L}.L.\frac{R^4}{4} \leftrightarrow$$
$$I=\frac{1}{2}MR^2  $$

