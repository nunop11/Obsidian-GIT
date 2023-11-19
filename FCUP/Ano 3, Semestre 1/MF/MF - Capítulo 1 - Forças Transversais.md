**NOTA** - no início do PPT tem uma introdução histórica

# 0 - Coisas Importantes para a UC
## Áreas
- Área do círculo: $\pi R^{2}$
- Cilindro
    - Área Lateral: $2\pi RL$
    - Volume: $\pi R^{2}L$
- Esfera
    - Área da superfície: $4\pi R^{2}$
    - Volume: $\frac{4}{3}\pi R^{3}$
- Cone
    - Área Lateral: $\pi R \sqrt{R^{2}+H^{2}}$
    - Volume: $\frac{1}{3}\pi R^{2} H$

## Notas mais gerais
- A menos que seja dito algo em contrário, a massa volúmica da água (até 30ºC) é 1000 kg/m3
- A menos que seja dito algo em contrário, a 20ºC a viscosidade dinâmica da água é $10^{-3}$ Pa.s
- Consideramos que a acelaração da gravidade é sempre $g=10~m/s^{2}$

## Vetores
### Coordenadas Cartesianas
![[vetores.png]]
- Temos o vetor $\vec{v}=v_{a}\hat{x}+v_{b}\hat{y}$
- Temos ainda: $$v=|\vec{v}|=\sqrt{v_{a}^{2}+v_{b}^{2}} \quad \quad;\quad \quad \tan\theta=\frac{v_{b}}{v_{a}}$$

### Coordenadas Polares
![[vetores - coords polares.png]]
- Basicamente, em vez de escrever um ponto como $P(x,y)$ escrevê-mo-lo como $P(r,\theta)$. Temos:
$$r=\sqrt{x^{2}+y^{2}} \quad \quad;\quad \quad \tan\theta=\frac{y}{x}$$
e em que resulta:
$$x=r\cos\theta \quad \quad;\quad \quad y=r\sin\theta$$

## Momento de Força
![[momento.png|475]]
- Surge quando uma força é aplicada e faz algo rodar. Para saber o sentido, fechar os dedos da mão no sentido que a força faz o objeto rodar e o polegar aponta no sentido do momento.

## Forças
### Tipos
**de Contacto** - Força exterior aplicada no corpo por uma superfície em que ele toca. EX: Força de Atrito
**à Distância** - Exercida à distância. EX: Peso, exercido pela terra sobre os corpos.

### Equilíbrio
- Um corpo está em equilibrio se:
$$\sum \vec{F}=\vec{0} \quad \quad;\quad \quad \sum \vec{M}=\vec{0}$$

## Tensões
![[tensao sobre superficie.png]]
- Consideremos que nas 2 imagens temos uma placa de largura $W$ e comprimento $L$, sendo que na figura vemos o comprimento (a largura estende-se perpendicular ao ecrã). A área da placa será então $A=WL$.
- Na imagem da esquerda temos que a tensão é uniforme e está aplicada em toda a superfície. Temos $$F=p_{i}A$$
em que $p_{i}$ é a pressão aplicada, que será igual em todos os pontos e $A$ é a área do corpo/plano em que a força está aplicada.

- Na imagem da direita temos: $$F=\int_{0}^{L} p_{i}(x)W dx$$
# 1 - Forças num fluido - viscosidade
- Tendo um volume de fluido, existem 2 tipos de força que podem estar aplicadas:
    - Forças de **pressão** - normais, associadas a pressão. Do tipo: $$F_{p}=\int p(A)dA$$
    - Forças de **corte** - tangenciais, associadas a tensão de corte: $$F_{c}=\int \tau(A)dA$$(em que $\tau$ é uma tensão de corte)

## Lei de Newton para um fluido
![[força transversal.png]]
- Consideremos então que a superfície de baixo está fixa e a de cima se move com velocidade $\vec{v}$. A distância entre as placas é $y_{0}$.
- Ora, a placa de cima mover faz com a camada de átomos do fluido mais acima se mova com a mesma velocidade. As camadas abaixo são "arrastadas". A placa mais abaixo tem velocidade nula, pelo que a camada de átomos mais abaixo também não se move. Gera-se então um perfil de velocidades do tipo:
$$v_{x}(y)= \frac{v_{0}}{y_{0}} y$$
![[perfil velocidades.png]]


![[deslocamento fluidos.png|475]]
- Assim, sabendo o perfil queremos saber onde é que a linha de fluido $a-a'$ (em $t=0$) na figura acima estará após um intervalo de tempo $\delta t$. É evidente que a linha, originalmente vertical, irá transformar-se numa linha diagonal após o intervalo de tempo.
- Ora, para fluidos newtonianos observa-se que $$\tau\propto \frac{\delta\theta}{\delta t}$$
ou seja, a tensão de corte no fluido é proporcional a $\frac{\delta\theta}{\delta t}$ AKA **taxa de deformação**.
- Sendo $\delta \theta$ uma ângulo infinitesimal temos que $$\tan \delta \theta = \frac{v_{0}\delta t}{y_{0}} \simeq \delta \theta \quad\to \quad \frac{\delta\theta}{\delta t}=\frac{v_{0}}{y_{0}}$$
- Logo, se $\tau\propto \frac{\delta\theta}{\delta t}$ temos então:
$$\tau\propto \frac{dv_{x}}{dy}=\mu \frac{dv_{x}}{dy}$$
em que $\mu$ é o **coeficiente de viscosidade** ou **viscosidade** do fluido.
- Ora, sendo $v_{x}(y)$ uma relação linear, $\frac{dv_{x}}{dy}$ será constante e então também $\tau$ será constante ao longo do fluido.

- Este comportamento é semelhante a ter um baralho de cartas. Dependendo do atrito entre elas (AKA o quão nvoas as cartas são), se puxarmos a carta de cima lentamente é possível que
    - só essa carta se mova (cartas novas, atrito muito baixo)
    - acontece o caso acima, a primeira carta move $\ell_{1}$, faz a segunda mover-se $\ell_{2}<\ell_{1}$, que faz a terceira mover $\ell_{3}<\ell_{2}$, etc... (cartas não muito novas)
    - as cartas movem-se quase em bloco como 2º caso mas com deslocamentos $\ell_{i}$ muito próximos (cartas muito velhas, muito atrito)

- Ou seja:
    - Se, para uma mesma força, a viscosidade for maior, a velocidade da camada adjacente à placa em movimento será menor
    - Uma alta viscosidade faz com que o fluido se mova quase em bloco, com a diferença de deslocamento entre as placas quase nula

![[tabela viscosidade.png]]

### Viscosidade VS temperatura e pressão
- A viscosidade dos gases da maioria dos liquidos aumenta com a pressão; a da água diminui.
- A viscosidade de gases aumenta com a temperatura. Temos:
$$\frac{\mu}{\mu_{0}} \approx \left(\frac{T}{T_{0}}\right)^{n}~~~~~~\textsf{(Lei da Potência)}$$
$$\ln \frac{\mu}{\mu_{0}} \approx \frac{\left(\frac{T}{T_{0}}\right)^{\frac{3}{2}} (T_{0}+S)}{T+S}~~~~ \textsf{(Lei de Sutherland)}$$
em que $\mu_{0}$ é a viscosidade conhecida a $T=T_{0}$ e $S$ é uma função do tipo de gás.

- Para os líquidos, a relação viscosidade/temperatura é descrita por
$$\ln \frac{\mu}{\mu_{0}}\approx a + b \frac{T_{0}}{T} + \left(\frac{T_{0}}{T}\right)^{2}$$

### Fluidos não-newtonianos
![[fluidos nao newtonianos.png]]

## Reómetros
- Ver exemplos e suas resoluções no PPT