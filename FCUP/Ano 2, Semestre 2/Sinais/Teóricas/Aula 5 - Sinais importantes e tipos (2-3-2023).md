# Propriedades de Sinais
### Transformação Linear da variável independente
- Tendo o sinal $x(t)$, podemos fazer a transformação linear $t\rightarrow at+b$ e obtemos o sinal $x(at+b)$
- Casos particulares são
    - Reflexão em relação à origem: $x(t)\rightarrow x(-t)$
    - Translação: $x(t)\rightarrow x(t+b)$

### Sinais Pares e Ímpares
- _Sinal par_ $x(t)=x(-t)$ -  Simétrico em relação ao eixo dos $y$
- _Sinal ímpar_ $x(t)=-x(-t)$ - Ao rodar uma metade 180º em relação à origem obtemos a outra
- Todos os sinais podem ser divididos numa componente par e impar:
$$x(t)=x_{par}(t)+x_{impar}(t)$$

### Periodicidade
- Um sinal é periódico se: $\forall t, x(t)=x(t+T)$

# Sinais importantes
### Degrau Unitário
![[Attachments/FCUP/A2S2/Sinais/Degrau unitário.png]]
$$u(t)=\begin{cases}0 &t<0\\ 1 &t\geq0\end{cases}$$
## Função Sigma
![[Funcao sigma.png]]
$$sgn(t)=2u(t)-1=\begin{cases}-1 &t<0\\ 1 &t\geq0\end{cases}$$

## Função Retângulo
![[Funcao retangulo.png]]
$$rect(t)=u \left(t + \frac{1}{2}\right)-u \left(t - \frac{1}{2}\right)=\begin{cases}0 &|t|>\frac{1}{2}\\ 1 &|t|\leq \frac{1}{2}\end{cases}$$

## Função Delta de Dirac
$$\delta(t)=\frac{d}{dt}u(t) \longrightarrow u(t)=\int_{-\infty}^{t}\delta(\tau)d \tau$$
![[Delta Dirac.png]]
- Acima temos a representação usual, em que $1$ corresponde a infinito.
$$\delta(t)=\begin{cases}\infty &t=0 \\ 0 &t\neq0\end{cases}$$
- Tem-se que:
>$$\int_{-\infty}^{+\infty} \delta(t)dt = 1$$

Tem-se:
$$\begin{align*}
\forall x(t): &x(t)\delta(t)=x(0)\delta(t)\\
&x(t)\delta(t-t_{0})=x(t_{0})\delta(t-t_{0})
\end{align*}$$
pelo que
$$\large x(t)=\int_{-\infty}^{+\infty}x(\tau)\delta(t-\tau)d \tau$$

## Função Rampa Unitária
![[Attachments/Degrau Unitário.png]]
$$r(t)=\int_{-\infty}^{t}u(\tau)d \tau=t \cdot u(t)$$
### Exponencial complexa
$$x(t)=Ce^{st} \quad;\quad C=x_{0}e^{j \phi} \quad;\quad s=\sigma+j \omega$$
Pelo que se tem
$$x(t)=Ce^{st}=x_{0}e^{\sigma t}[\cos(\omega t+\phi)+j\sin(\omega t+\phi)]$$
 - Para sinais harmônicos temos $\Large x_{h}(t)=\text{Re}[x(t)]$

# Relações entrada-saída de sistemas
![[Tipos de ligações entre sistemas.png]]

# Tipos de sistemas
## Sistema sem memória
- A saída num instante depende _apenas_ da entrada nesse instante. EX: Circuitos com resistências.

## Sistema com memória
- A saída num instante depende da entrada nesse instante _e nos instantes anteriores_. EX: Circuitos com carga e descarga de condensadores.

## Sistema Invertível
- Quando cada sinal de entrada diferente dá um sinal de saída diferente. Ou seja, é um sistema em que a partir do sinal de saída podemos determinar o sinal de entrada correspondente.

## Sistema Causal
- Sinal de saída depende apenas do presente e/ou passado do sinal de entrada. _EX:_ condensador (tensão nos terminais é o sinal de saída, que depende da corrente (sinal de entrada) até ao instante $t$)
- Um sistema descrito por $y(t)=x(t)-x(t+1)$ _não_ é causal, pois depende do futuro do sistema (instante $t+1$)

## Sistema Estável
- Um sinal é estável de entrada limitada/saída limitada quando qualquer entrada limitada dá origem a uma saída limitada. 
> _**EX:**_ Bola num vale. Se a bola estiver no ponto mais baixo e uma pequena for aplicada (sinal de entrada limitado)  irá causar uma pequena oscilação no eixo dos y (sinal de saída limitado).
> Por outro lado, uma bola no topo de um monte seria um _sistema instável_, porque qualquer força aplicada irá fazer com que desça o monte todo (sinal de saída não limitado).

## Sistema invariante no tempo
- Quando uma translação no tempo leva a um mesmo sinal de saída:
$$x(t)\rightarrow y(t) \Longrightarrow x(t-t_{0})\rightarrow y(t-t_{0})$$

## Sistema Linear
- Sistema que verifica a _Propriedade da Sobreposição_:
    - Se o sinal de entrada é uma combinação linear de sinais, então o sinal de saída é a mesma combinação linear (os efeitos do sistema sobrepõem-se): $$\begin{cases}x_{1}(t)\rightarrow y_{1}(t)\\ x_{2}(t)\rightarrow y_{2}(t)\end{cases}\Longrightarrow ax_{1}(t)+bx_{2}(t)\rightarrow ay_{1}(t)+by_{2}(t)$$
- Por exemplo, $y(t)=\sin[x(t)]$ é um sistema _não-linear_. 
- Nestes sistemas, uma entrada nula dá uma saída nula.

## Sistema Incrementalmente Linear
- Basicamente um sistema linear, mas em que entrada nula dá saída não nula. Exemplo: $y(t)=2x(t)+3$

# Sistemas Lineares e Invariantes no Tempo (SLIT)
- Sistemas _lineares_ e _invariância temporal_. 
- Estas propriedades são úteis porque permitem representar muitos processos físicos. Permitem ainda estudar sistemas de forma sistemática.

#sinais #fisica
