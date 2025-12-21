## PPT Zurique - Localização baseada em para mapa probabilístico
### Raciocínio probabilístico / Bayes
- É o nome que se dá a quando temos de tomar decisões com incertezas e informação em falta
- Fazemos estas decisões ao combinar modelos, informação anterior e dados medidos
![[Pasted image 20251213190225.png]]

### O problema
- Temos um robot a mover-se num ambiente
- Consoante se modo, partindo de uma posição que conhecemos muito bem, ele pode ir guardando e estimando a sua posição usando *odometria*
- No entanto, em cada movimento e em cada passo de odometria, temos um pouco de incerteza. Ou seja, estamos a *acumular erro*
- Para reduzir este erro e ter mais certezas, precisamos de **atualizar** as nossas informações com *medições* da posição do ambiente. Ao combinar com a odometria, isto deverá reduzir a incerteza

### Porquê approach probabilística?
- Antes de mais, não podemos esquecer que as medições dos sensores são afetadas por erros de medição. Ou seja, nunca podemos saber **exatamente** onde está o robot. Podemos apenas dizer algo tipo "o mais provável é estar neste ponto, mas existe uma área em sua volta com pelo menos X% de probabilidade de ser a posição real do robot"

### Bayes
- Usando a regra de Bayes podemos escrever:
$$p(l|i) = \frac{p(i|l)p(l)}{p(i)}$$
em que
    - $p(l)$ - probabilidade que estimamos da nossa posição $l$ antes de atualizar os dados com medições
    - $p(i|l)$ - probabilidade de medirmos $i$ quando estamos na posição $l$. Isto é basicamente o **mapa** que consideramos 
    - $p(i)$ - fator de normalização 
- Logo temos que $p(l|i)$ é a probabilidade de estarmos na posição $l$ *tendo em conta que medimos* $i$ - dá-nos como atualizar e aproveitar dados medidos!

- Podemos usar isto para *prever* o mapa usando:
$$p(l_{t}|o_{t})=\int p(l_{t}|l_{t-1}',o_{t})p(l'_{t-1})dl_{t-1}'$$
ou seja, integrado por todas as maneiras como o robot pode ter chegado à posição $l$ no instante $t$ ($l_{t}$). Notemos que $l$ representa posições do robot e $o$ medições de odometria
- Aqui podemos fazer algo para nos facilitar a vida: **assunção de Markov** - a atualização da nossa estimativa apenas depende do *estado anterior e ações desde este*

### Funções para representar posição do robot
- Consideremos o robot apenas a existir na direção $x$.
- Exemplos de distribuições:
    - **Uniforme** - quando não sabemos de todo onde o robot está. Significa que temos igual probabilidade de estar em qualquer posição.
    - **Multimodal** - uma distribuição em que temos 2+ picos, ou seja, o robot poderá estar e 2+ sítios, mas temos alguma certeza que está num deles
    - **Dirac** - quando temos 100% de certeza da posição do robot. 
    - **Gaussiana/Normal** - temos o traçado conhecido em formato de "sino" e temos: $$p(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}$$

### Descrição da localização de forma probabilística
- Consideremos que temos um robot num ambiente desconhecido. Ele começa numa posição que conhecemos a 100% (zero incerteza)
- Mas, consoante ele se move vamos ficando cada vez mais incerto da sua posição, devido a incertezas na odometria. 
- Eventualmente esta chegaria a infinito. Para impedir isto, o robot usa sensores para perceber a sua localização relativamente a alguns pontos de referência. Isto reduz a incerteza
![[Pasted image 20251213220608.png]]

- Podemos dividir este processo em 2 partes:
    - **Previsão / Ação** - o robot mexe-se com os motores e usamos a odometria para prever a sua posição. Isto aumenta a incerteza
    - **Percepção / Medição** - os sensores fazem alguma medição que permite encontrar um ponto de referência e a incerteza diminuir
![[Pasted image 20251213220814.png]]
Ou seja, o problema de localizar de forma probabilística consiste em conseguir **atualizar** estas 2 partes corretamente.

### Resolver este problema
- Temos estes *ingredientes*:
    - Distribuição de probabilidade inicial $p(x)_{t=0}$
    - Modelo do erro dos sensores do robot (encoders, etc)
    - Modelo do erro dos sensores para o exterior (LIDARs, camaras, sonars, etc)
    - Mapa do ambiente, se possível. Se não houver mapa, temos que fazer SLAM

- Para atualizar a Ação e Percepção temos que:
    - A *ação* é atualizada com o teorema de probabilidade total $p(x)=\int_{y}p(x|y)p(y)dy$
    - A *percepção* é atualizada com a regra de Bayes: $p(x|y)=\frac{p(y|x)p(x)}{p(y)}$
Isto vem tudo de cima, quando vimos $p(l|i)$. Vamos ver melhor cada fase.

#### Atualização de ação
- Apenas usamos os dados dos sensores internos (encoders, etc)
- Nesta fase, o robot pega na sua posição atual $\text{bel}(x_{t})$, baseada na estimativa anterior $\text{bel}(x_{t-1})$, e no input que demos na odometria $u_t$
- Podemos então determinar a estimatva atual:
$$\begin{align*}
\text{bel}(x_{t})&= \int p(x_{t}|u_{t},x_{t-1})\text{bel}(x_{t-1})dx_{t-1}\\
&= p(x_{t}|u_{t},x_{t-1})*\text{bel}(x_{t-1})
\end{align*}$$

#### Atualização de percepção
- Nesta fase o robot corrige a estimativa da fase de ação combinado-a com a informação dos sensores externos (LIDARs, etc):
$$\text{bel}'(x_{t})=\eta \cdot p(z_{t}|x_{t})\text{bel}(x_{t})$$
em que $\eta$ é uma constante de normalização que garante que $\int\text{bel}'(x)dx=1$

#### EX
Abaixo temos uma imagem a mostrar a evolução deste processo. Primeiro o robot vê um pilar à sua frente e define uma distribuição com 3 picos (ele poderia estar em frente a qualquer pilar). Depois move e vê um dos pilares mais perto e outro atrás. Usando isto ele percebe onde está
![[Pasted image 20251213222703.png]]

### Localização Markov
- Não vamos ver. Kalman apenas. 

## PPT Zurique - Localização com filtro de Kalman
![[Pasted image 20251213223402.png]]
- Temos acima um esquema que representa como um sistema de um robot a localizar-se com KF

### Intro a KF
- Em KF consideramos que a posição do robot segue uma distribuição gaussiana.
- A partir de medições dos sensores, temos 2 medições/estimativas da posição do robot (grandeza $q$):
    - $\hat q_{1}$ - medição $q_{1}$, que tem variância $\sigma_{1}^{2}$
    - $\hat{q}_{2}$ - medição $q_{2}$, que tem variância $\sigma^{2}_{2}$
- E podemos definir o erro quadrático pesado $S=\sum_{i} w_{i}(\hat{q}-q_{i})^{2}$
- Ora, queremos minimizar o erro, o que acontece para $$\frac{\partial S}{\partial \hat{q}}=0=2\sum\limits_{i=1}^{n}w_{i}(\hat{q}-q_{i})$$
- E podemos deduzir que:
$$\hat{q}=q_{1}+\frac{\sigma_{1}^{2}}{\sigma_{1}^{2}+\sigma_{2}^{2}} (q_{2}-q_{1}) $$
- Ou seja, temos uma estimação do centro da nossa distribuição gaussiana: $\hat{q}$. Claro, esta será a estimativa da posição do robot.
- Notemos que se $\sigma_{1}^{2}=\sigma_{2}^{2}$ temos simplesmente $\hat{q}=\frac{q_{1}+q_{2}}{2}$
![[Pasted image 20251213225446.png]]

#### Em notação Kalman
- Vemos que o rácio de variâncias dá um *ganho* è diferença $q_{2}-q_{1}$. Assim, definimos o **ganho de Kalman**: $$K_{k+1}=\frac{\sigma_{k}^{2}}{\sigma_{k}^{2}+\sigma_{z}^{2}}$$
- Num contexto em que estamos a ir atualizando as nossas estimativas de posição passo a passo, $q_{1}$ seria a nossa estimativa atual $\hat{x}_{k}$
    - Equivalentemente, $\sigma_{k}^{2}$ será a variância da estimativa atual da posição
- Já $q_{2}$ será informação nova que estamos a introduzir. No caso do robot, isto serão as medições dos sensores: $z_{k}$.
    - De forma similar, $\sigma_{z}^{2}$ será a variância da medição
- Com estas 2 grandezas, podemos obter $\hat{q}$, uma estimativa atualizada. Na prática, esta até acaba por ser uma *previsão*: $\hat{x}_{k+1}$
- Juntando tudo, podemos escrever estas equações:
$$\begin{cases}
\hat{x}_{k+1}=\hat{x}_{k}+K_{k+1}(z_{k+1}-\hat{x}_{k}) \\
\sigma_{k+1}^{2}=\sigma_{k}^{2} - K_{k+1}\sigma_{k}^{2}
\end{cases}$$

#### Modelo dinâmico
- Podemos descrever o robot em movimento como:
$$\frac{dx}{dt}=u+w$$
em que $u$ é a velocidade e $w$ o ruído.

- Assim teremos:
$$\begin{cases}
\hat{x}_{k+}=\hat{x}_{k}+u(t_{k+1}-t_{k}) \\
\sigma_{k+}^{2}=\sigma_{k}^{2}+\sigma_{w}^{2}(t_{k+1}-t_{k})
\end{cases}$$
em que notemos que $\hat{x}_{k+}$ é uma estimativa **intermédia**
    - $\hat{x}_{k}$ é a estimativa inicial do estado. Esta resulta da *previsão feita no estado anterior*
    - $\hat{x}_{k+}$ é a estimativa da dinâmica, em que aplicamos as equações físicas de dinâmica em $\hat{x}_{k}$ para ver como esta evoluiria 
    - $\hat{x}_{k+1}$ resulta de meter $\hat{x}_{k+}$ no KF, obtendo uma previsão forte

- Podemos juntar tudo para uma ter uma equação completa do KF:
$$\begin{cases}
\hat{x}_{k+1}&=\hat{x}_{k+}+K_{k+1}(z_{k+1}-\hat{x}_{k+}) \\
&= [\hat{x}_{k} + u(t_{k+1}-t_{k})] + K_{k+1}[z_{k+1}-\hat{x}_{k}-u(t_{k+1}-t_{k})] \\
K_{k+1}&= \frac{\sigma_{k+}^{2}}{\sigma_{k+}^{2}+\sigma_{z}^{2}} \\
&=\frac{\sigma_{k}^{2}+\sigma_{w}^{2}(t_{k+1}-t_{k})}{\sigma_{k}^{2}+\sigma_{w}^{2}(t_{k+1}-t_{k})+\sigma_{z}^{2}}
\end{cases}$$

### Algoritmo
![[Pasted image 20251213232411.png]]
A partir daqui o PPT mostra um monte de equações. Abaixo vou só anotar coisas ditas que sejam úteis. Equações já temos noutras aulas.

### Observação
- Numa certa iteração o robot faz observação do ambiente. Isto normalmente inplica detetar um conjunto de $n_{0}$ objervações $z_{j}$
- Estas serão **features** - *paredes, cantos, curvas, postes*
- Estas observações são feitas no referencial do robot:
![[Pasted image 20251213233130.png]]
- Notemos que as linhas são obtidas numericamente. Notemos ainda que estes dados são de LIDAR, logo no gráfico da direita temos as retas marcadas como pontos $(r,\theta)$

### Matching
- O robot vai vendo marcos e registando. 
- Quando vemos um marco e podemos associá-lo a outro que vimos antes (a posição é quase a mesma), então consideramos que reencontramos
![[Pasted image 20251213233759.png]]

## PPT Zurique : SLAM
### SLAM?
- SLAM consiste em ter um robot a *navegar* num ambiente desconhecido, ao mesmo tempo que vai criando um *mapa* desse mesmo ambiente, usando apenas *sensores onboard*

### Porquê?
- Isto é muito mais difícil que localização e mapeamento só por si. 
- Apesar disso, o mapeamento tem a vantagem de ser automático e de se adaptar a alterações no ambiente

### Como funciona
- Vejamos um exemplo de como funciona SLAM consoante um robot se move
- Consideremos que a incerteza na posição inicial é *nula*

![[Pasted image 20251213234931.png]]
- Primeiro medimos um objeto/marco A. Essa medição terá uma certa incerteza, que se manifesta como uma covariância. Usamos isso para atualizar as estimativas de posição e covariância
![[Pasted image 20251213235046.png]]
- O robot move-se para longe da posição inicial. Ora, numa região ele não vê nenhum marco. Assim, a sua covariância só aumenta, tornando-se muito elevada.
![[Pasted image 20251213235313.png]]
- O robot deteta 2 marcos **novos** agora. Mas como temos muita incerteza na posição do robot, também temos muita incerteza na posição onde estão os marcos que vimos. Em outras palavras, o *mapa que formamos está correlacionado à estimativa da posição* do robot
![[Pasted image 20251213235442.png]]
- O robot volta pra trás. A sua variância aumenta ainda mais. 
- Isto acontece porque os marcos que vimos acima eram-nos desconhecidos até ao momento em que os vimos. Ou seja, identificá-los não nos ajuda de forma nenhuma a reduzir a incerteza da posição
- Eventualmente o robot aproxima-se e consegue ver o *marco inicial*!!!
![[Pasted image 20251213235612.png]]
- Ao ver este marco A acontece **loop closure**! Finalmente encontramos algo que vimos antes. Como no início consideramos que a covariância era nula, estamos a reencontrar algo duma fase do nosso percurso em que tinhamos maior confiança
- Ou seja, rever este marco permite confirmar "estamos perto do ponto inicial". Isto então reduz a incerteza da estimativa de posição do robot
- Por sua vez, isto diminui a incerteza dos marcos B,C.

### Formulação
- A **pose** do robot em $t$ é escrita como $x_{t}$ (isto pode incluir a **posição e orientação** do robot)
    - A trajetória do robot até $t$ é $\{x_{0},x_{1},\dots,x_{t}\}$ 
- Como deu para ver no PPT anterior, $u_{t}$ representa os *inputs de controlo* que nos dão o movimento feito entre $t,t-1$.
    - A sequência de controlos feitos até ao presente é $\{u_0,u_1,\dots,u_t\}$
- O mapa **real** do ambiente é $\{m_0,m_1,\dots,m_N\}$
- Em cada instante $t$ o robot faz $k$ medições: $\{z_0,z_1,\dots,z_k\}$

- O problema SLAM consiste em:
    - *SLAM Completo* - estimar a trajetória até ao presente toda: $$p(x_{0:t},m_{0:n}|z_{0:k},u_{0:t})$$
    - *SLAM Online* - estimar apenas a posição neste instante $$p(x_t,m_{0:n}|z_{0:k},u_{0:t})$$

### Representação em esquema
![[Pasted image 20251214001406.png]]
- Vemos aqui a ideia de como funciona SLAM:
    - Um controlo $u_j$ e uma posição $x_{j-1}$ juntos decidem a posição do robot na iteração seguinte: $x_{j}$
    - Nessa posição o robot faz $k$ medições. Dessas, apenas algumas poderão ser associadas a marcos.

### Approaches de SLAM
#### Versão completa
![[Pasted image 20251214001617.png]]
- Uma versão completa com todas as ligações seria assim. Em cada uma de $m$ posições vemos quais dos $n$ marcos conseguimos ver.
- No final, temos uma série de equações das coordenadas destes pontos
- Tudo junto, isto permitiria determinar as coordenadas exatas das posições do robot e dos marcos.
- Na realidade isto não é viável, porque torna-se demasiado complexo e demoroso de calcular. Ou seja, é preciso tornar o modelo *mais esparso*

#### Filtragem
![[Pasted image 20251214001837.png]]
- Rejeitamos todas as poses do passado. 
- Para não perder a informação desses $t$ pontos, usamos um **vetor de estado** e uma **matriz de covariância**

#### Key-frames
![[Pasted image 20251214001953.png]]
- Apenas guardamos algumas poses mais representativas e assim reduzimos muito o tamanho do esquema

### EKF SLAM
- Isto consiste na approach de filtragem que vimos acima
- A informação e experiência do passado do robot são resumidas no *vetor de estado* $y_{t}$ e na *matriz de covariância* $P_{y_t}$.
- Mas notemos que: 
    - $y_{t}$ contém a pose do robot em $t$ e todos os marcos encontrados até agora
    - $P_{y_t}$ contém as matrizes de covariância de $x_{t}$ *como todos os marcos*
$$y_{t}=\begin{bmatrix} x_{t} \\ m_{1} \\ m_{2} \\ \vdots \\ m_{n-1} \end{bmatrix} \quad;\quad P_{y_{t}}=\begin{bmatrix} P_{xx} & P_{xm_{1}} & P_{xm_{2}} & \cdots & P_{xm_{n-1}} \\ P_{m_{1}x} & P_{m_{1}m_{1}} & P_{m_{1}m_{2}} & \cdots & P_{m_{1}m_{n-1}} \\ P_{m_{2}x} & P_{m_{2}m_{1}} & P_{m_{2}m_{2}} & \cdots & P_{m_{2}m_{n-1}} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ P_{m_{n-1}x} & P_{m_{n-1}m_{1}} & P_{m_{n-1}m_{3}} & \cdots & P_{m_{n-1}m_{n-1}} \end{bmatrix}$$
- Se tivermos o robot a mover em 2D temos as shapes:
    - $y_{t}\to 3+2n\times1$
    - $P_{y_{t}}\to(3+2n)\times(3+2n)$
- Em que temos $3$ variáveis da pose ($x,y,z$) e $2$ variáveis da posição de cada marco ($\alpha,r$ ou $x,y$)
- Consoante o robot se move, atualizamos $y_{t},P_{y_{t}}$ usando as equações de EKF
![[Pasted image 20251214002839.png]]
- Na próxima aula irei ver melhor as contas e deduções desta parte!

### Correlações
- Inicialmente e em muitos casos, assumimos que a matriz de covariâncias é **DIAGONAL**
- Isto significa que estamos a considerar que não há correlação/ligação entre as medições que fazemos de qualquer par de marcos
- Mas na realidade surgem sempre correlações. Isto resulta da equação de atualização da covariância: $$\hat{P}_{y_{t}}=f_{y}P_{y_{t-1}}f_{y}^{T} + f_{u}Q_{t}f_{u}^{T}$$
- Na prática, podemos entender isto: se tivermos uma câmara (sensor) a mover-se, 2 marcos que estejam pousados numa mesa à nossa frente estarão a mover-se *coerentemente* relativamente a nós. Ou seja, é evidente que as suas posições relativamente a nós estão correlacionadas.
- Notemos que ter correlações não é mau. Pelo contrário, ter muitas amostrar com correlações fortes implica que temos muitos marcos e podemos establecer muitas relações sólidas entre eles. 

### Problemas
- O vetor de estado de EKF SLAM é grande e só aumenta ao longo do tempo. Pior ainda, a matriz de covariância cresce *quadraticamente*!
- Isto quer dizer que implementar um EKF SLAM num sistema de larga escala será computacionalmente pesado.

