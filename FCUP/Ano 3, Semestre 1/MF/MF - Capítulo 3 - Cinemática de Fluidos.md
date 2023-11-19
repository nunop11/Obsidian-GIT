# 3 - Cinemática do Escoamento de Fluidos
## 3.1 - Descrição Eulereana e Lagrangeana de escoamento
**Eulereana** - Descreve o campo de escoamento em termos de $p,v$ para o volume de fluido em estudo.
**Lagrangeana** - Descreve o escoamento de uma partícula de fluido no espaço e tempo.

> EXEMPLO - Autoestrada
> - Queremos estudar o tráfego de automoveis numa autoestrada.
> **Aproximação Eulereana** - Corresponde a colocar 2 controladores de tráfego, um em cada ponta da autoestrada. Ignoramos a identidade dos carros e contamos apenas quantos carros passam em cada ponta num certo intervalo de tempo.
> **Aproximação Lagrangeana** - Corresponde a controlar/monitorizar o percurso e velocidade ao longo do tempo de 1 carro específico

> EXEMPLO 2 - Água Quente a Fluir
> - Temos um "rio" em que a água começa por ser quente e vai arrefecendo.
> **Aproximação Eulereana** - Estudar a temperatura do escoamento em certos pontos. De notar que, ao fazer isto, apenas sabemos a evolução do escoamento ao longo do espaço; mas não como este evolui com o tempo.
> **Aproximação Lagrangeana** - Medir a temperatura de uma partícula e segui-la, determinando-se assim a evolução da temperatura na escala temporal.

- Assim, na maioria da mecânica de fluidos usasse a *aproximação Eulereana*. Mas há casos em que o método Lagrangeano é mais útil.

## 3.2 - Campo de Velocidade
- A velocidade é definida por um campo de velocidades:
$$\vec{v}(x,y,z,t)=v_{x}(x,y,z,t)\hat{i}+ v_{y}(x,y,z,t)\hat{j} + v_{z}(x,y,z,t) \hat{k}$$
- Na maioria dos problemas, determinar a velocidade é suficiente para conseguir obter outras propriedades do fluido, como o campo de pressão.

## 3.3 - Campo de Aceleração
- Podemos escrever:
$$\begin{align*}
\vec{a}= \frac{d \vec{v}}{dt}&= \frac{\partial \vec{v}}{\partial t} + \frac{\partial \vec{v}}{\partial x} \frac{dx}{dt} + \frac{\partial \vec{v}}{\partial y} \frac{dy}{dt} +\frac{\partial \vec{v}}{\partial z} \frac{dz}{dt}\\
&= \frac{\partial \vec{v}}{\partial t} + \frac{\partial \vec{v}}{\partial x}v_{x} + \frac{\partial \vec{v}}{\partial y}v_{y}+ \frac{\partial \vec{v}}{\partial z}v_{z}
\end{align*}$$
- Ora, podemos chamar a $\vec{a}=\frac{d\vec{v}}{dt}=\frac{D\vec{v}}{Dt}$ de *aceleração total/substancial* (derivada total/substancial da velocidade)
    - A $\frac{\partial\vec{v}}{\partial t}$ chamamos de *aceleração local* (derivada local de $\vec{v}$)
    - A $\frac{\partial \vec{v}}{\partial x}v_{x} + \frac{\partial \vec{v}}{\partial y}v_{y}+ \frac{\partial \vec{v}}{\partial z}v_{z}$ chamamos de *aceleração convectiva* (derivada convectiva de $\vec{v}$)

- Usando o operador $\nabla$ podemos escrever:
$$\vec{a}= \frac{D \vec{v}}{Dt}=\frac{\partial \vec{v}}{\partial t} + (\vec{v}\cdot \nabla)\vec{v}$$
sendo que para campos escalares, como $T=f(x,y,z,t)$, temos:
$$\frac{DT}{Dt}=\frac{\partial T}{\partial t} + \vec{v}\cdot \nabla T$$
- Voltemos ao exemplo do "rio" em que água começa a uma temperatura alta. Consideremos $T$ como sendo o campo de temperaturas que descreve este problema. Consideremos que as condições externas não se alteram, pelo que a temperatura *em cada ponto* não se altera ao longo do *tempo* -- **Campo Estacionário Não Uniforme**. Por outro lado, de ponto para ponto teremos uma temperatura diferente. Assim:
$$\frac{\partial T}{\partial t}=0 \quad \quad ; \quad \quad \frac{DT}{Dt}\neq0$$

## 3.4 - Visualização do Campo de Escoamento
### 3.4.1 - Linhas de Corrente, trajetórias, linhas de rasto e linhas de tempo
- Campos de velocidades já descrevem o escoamento por completo, mas é preciso um meio mais simples de o visualizar.
**Trajetória** - "seguir" a partícula e registar o seu percurso
**Linhas de Corrente** - Linhas desenhadas de forma a obter um traçado sempre tangente aos vetores velocidade das partículas. Num escoamento *estacionário* as linhas de corrente são iguais à trajetória. Num escoamento *não estacionário* as linhas de corrente representam a trajetória num certo instante.
**Linhas de rasto** - lugar geométrico de onde as partículas passaram anteriormente. Em escoamentos estacionários coincidem com as trajetórias e linhas de corrente
**Linha de tempo** - Desenhada ao "unir" um conjunto de partículas do fluido e ver a sua evolução no tempo.

#### Calcular linhas de corrente
![[velocidade e distancia tangente.png]]
- Consideremos um vetor velocidade $\vec{v}=(v_{x},v_{y},v_{z})$ tangente a um comprimento infinitesimal $\delta r=\sqrt{\delta_{x}^{2}+\delta_{y}^{2}+\delta_{z}^{2}}$
- Conforme a figura acima vemos que há proporcionalidade entre os comprimentos:
$$\frac{\delta x}{v_{x}}= \frac{\delta y}{v_{y}}= \frac{\delta z}{v_{z}}=\frac{\delta r}{|\vec{v}|}$$
podendo-se establecer as relações:
$$\frac{dx}{dy}=\frac{v_{x}}{v_{y}} \quad;\quad \frac{dx}{dz}=\frac{v_{x}}{v_{z}} \quad;\quad \frac{dy}{dz}= \frac{v_{y}}{v_{z}}$$
- Assim, as linhas de corrente podem ser obtidas ao integrar isto. Para isso, é preciso conhecer o campo de velocidades (que irá depender do tempo) e as coordenadas de um ponto da linha de corrente $(x_{0},y_{0},z_{0})$ que presumiremos que ocorre em $t=0$.

**EXEMPLO - PARTE 1**
- Consideremos o campo de velocidades: $$v_{x}=\frac{x}{1+t}\quad;\quad v_{y}=\frac{y}{1+2t} \quad;\quad v_{z}=0$$
só temos movimento em $x,y$ portanto.

- Vejamos então a relação:
$$\begin{align*}
\frac{dx}{dy}=\frac{v_{x}}{v_{y}} \quad \Longrightarrow \quad \frac{dx}{v_{x}}&= \frac{dy}{v_{y}}\\
\int_{x_{0}}^{x} \frac{1+t}{x}dx&= \int_{y_{0}}^{y} \frac{1+2t}{y}dy\\
(1+t)\ln \frac{x}{x_{0}}&= (1+2t)\ln \frac{y}{y_{0}}\\
y &= y_{0} \left( \frac{x}{x_{0}}\right)^{\frac{1+t}{1+2t}}
\end{align*}$$
e temos:
![[trajetoria consoante t varia.png]]

#### Determinar Equação de Trajetória
- Conhecendo o campo de velocidades, basta arranjar forma de eliminar os $t$ nas equações.

**EXEMPLO - PARTE 2**
- Vejamos agora o que obtemos ao estudar o campo de velocidades:
$$v_{x}=\frac{dx}{dt}=\frac{x}{1+t} ~~\to~~ x=C_{1}(1+t)$$
$$v_{y}=\frac{dy}{dt}= \frac{y}{1+2t} ~~\to~~ y=C_{2}\sqrt{1+2t}$$
Temos então $C_{1}=x_{0},C_{2}=y_{0}$
- Podemos fazer então:
$$\begin{align*}
x=x_{0}(1+t)&\to t=\frac{x}{x_{0}}-1\\
 y=y_{0}\sqrt{1+2t}&\to t=\frac{1}{2}\left(\left(\frac{y}{y_{0}}\right)^{2}-1\right)
\end{align*}$$
Igualando os $t$ obtemos:
$$\begin{align*}
\frac{x}{x_{0}}-1 &= \frac{1}{2}\left(\left(\frac{y}{y_{0}}\right)^{2}-1\right)\\
2\left( \frac{x}{x_{0}}-1\right)&= \left(\frac{y}{y_{0}}\right)^{2}-1\\
y &= y_{0} \sqrt{( 1+ 2\left(\frac{x}{x_{0}}-1\right)}
\end{align*}$$
em que esta equação descreve a trajetória.

#### Equação das linhas de rasto
- Consideremos $\zeta$ como sendo os instantes de tempo anteriores a $t_{0}$. 
- Tal como atrás, temos:
$$v_{x}=\frac{dx}{dt}=\frac{x}{1+t} \quad;\quad v_{y}=\frac{dy}{dt}= \frac{y}{1+2t}$$

- Integremos entre $\zeta,t_{0}$:
$$\begin{align*}
\frac{dx}{dt} &= \frac{x}{1+t}\\
\int_{x_{0}}^{x}\frac{dx}{x}&= \int_{\zeta}^{t_{0}}\frac{dt}{1+t}\\
\ln \frac{x}{x_{0}}&= \ln \frac{1-t_{0}}{1-\zeta}\\
x &= x_{0}\frac{1-t_{0}}{1-\zeta}
\end{align*}$$
$$\begin{align*}
\frac{dy}{dt}&= \frac{y}{1+2t}\\
\int_{y_{0}}^{y}\frac{dy}{y}&= \int_{\zeta}^{t_{0}}\frac{dt}{1+2t}\\
\ln \frac{y}{y_{0}} &= \frac{1}{2}\ln \frac{1+2t_{0}}{1+2\zeta}\\
y&= y_{0} \sqrt{\frac{1+2t_{0}}{1+2\zeta}}
\end{align*}$$
- Se eliminarmos $\zeta$ conseguimos obter:
$$\left(\frac{y}{y_{0}}\right)^{2}= \frac{1+2t_{0}}{1+2\left[ (1+t_{0})\left(\frac{x_{0}}{x}\right)-1 \right]}$$
![[linhas corrente, trajetoria e rasto.png]]

## 3.5 - Vetores Velocidade e Aceleração ao longo de linha de corrente
- Temos uma linha de corrente. Temos uma pequena divisão desta, $\delta s$, que é percorrida pelo fluido em escoamento num intervalo de tempo $\delta t$. Assim a velocidade na direção dessa divisão da linha de corrente é dada por $v_{s}=\frac{ds}{dt}$
- Similarmente, $a_{s}=\frac{dv_{s}}{dt}$
![[aceleracao e componentes.png]]
- A componente tangencial da aceleração vimos acima.

![[variaçao velocidade.png]]
- Consideremos que uma partícula percorre a distância $\delta s$ na linha de corrente num intervalo $\delta t$.
- A variação de $v_{s}$ nesta distância será: $\delta v_{s}=\frac{dv_{s}}{dt}\delta s$
- Temos ainda que $\delta s= v_{s} \delta t$. 
- Juntando as 2 igualdades acima temos:
$$\frac{dv_{s}}{dt}=v_{s} \frac{dv_{s}}{ds}=a_{s}$$

- De forma similar, na **componente normal** temos:
$$\delta v_{n}=\frac{dv_{n}}{ds}\delta s\to \frac{dv_{n}}{dt}=v_{s} \frac{dv_{n}}{ds}$$
- De acordo com a figura acima:
$$\tan\delta\beta= \frac{\delta s}{R} \quad \quad;\quad \quad \tan\delta\beta= \frac{\delta v_{n}}{v_{s}+\delta v_{s}}\approx \frac{\delta v_{n}}{v_{s}}$$
juntando as duas temos:
$$\frac{ds}{R}=\frac{dv_{n}}{v_{s}}\to  \frac{dv_{n}}{ds}=\frac{v_{s}}{R}$$
o que nos dá:
$$\frac{dv_{n}}{dt}= \frac{v_{s}^{2}}{R}=a_{n}$$

- Daqui temos:
$$\vec{a}=v_{s} \frac{dv_{s}}{ds}\hat{s} + \frac{v_{s}^{2}}{R}\hat{n}$$