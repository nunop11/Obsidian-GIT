# 4 - Equação de Bernoulli
## 4.1 - Equação de Bernoulli ao longo de uma Linha de Corrente
- Esta equação é aplicável quando a intensidade das forças de corte são de uma ordem de grandeza inferior à das outras forças (nomeadamente gravidade e pressão).

![[bernoulli em linha de corrente.png]]
- Temos um elemento infinitesimal de fluido de dimensões $\delta n \times \delta s \times \delta y$.
- Para um fluido em estado estacionário temos a 2ª Lei de Newton:
$$\sum\limits \delta F_{s}= \delta m \cdot a_{s}= \delta m \cdot v_{s} \frac{dv_{s}}{ds}=\rho \delta V \cdot v_{s} \frac{dv_{s}}{ds}$$
- As forças que temos são:
    - Peso na direção $s$: $\delta W_{s}=-\rho g \sin\theta \delta V$
    - Força de Pressão na direção $s$:
        - $\delta p_{s}=\frac{1}{2} \left( \frac{\partial p}{\partial s}\delta s\right)$
        - Temos $\delta F_{p,s}= (p-\delta p_{s})\delta n \delta y- (p+\delta p_{s})\delta n \delta y= -2\delta p_{s} \delta n \delta y= - \frac{\partial p}{\partial s}\delta s \delta n \delta y= - \frac{\partial p}{\partial s}\delta V$

- Assim, substituindo na 2ª lei de Newton temos:
$$\delta V\left(-\rho g\sin\theta- \frac{\partial p}{\partial s}\right)=\rho v_{s} \frac{\partial v_{s}}{\partial s}\delta V$$
e vamos então tentar simplificar esta igualdade.

- Ora, podemos escrever $$\frac{1}{2}\frac{\partial v_{s}^{2}}{\partial s}=v_{s} \frac{\partial v_{s}}{\partial s}$$
![[exemplo - trigonometria.png]]
- Podemos então escrever que $\sin\theta=\delta z/\delta s$

- Ao longo da linha de corrente, a componente normal da pressão é constante, de modo que:
$$dp= \frac{\partial p}{\partial s}ds + \frac{\partial p}{\partial n}dn\to dp=\frac{\partial p}{\partial s}ds$$

- Substituindo estas 3 equações obtemos:
$$-\rho g \frac{dz}{ds}- \frac{dp}{ds}= \frac{1}{2}\rho \frac{dv^{2}}{ds} \to dp + \frac{1}{2}\rho dv^{2} + \rho g dz = 0$$
em que podemos integrar: $\int \frac{dp}{\rho} + \frac{1}{2}v^{2} + gz=C$

- Ora, se $\rho$ *não depende da pressão* (fluido incompressivel) temos:
$$p + \frac{1}{2}\rho v^{2}+ \rho g z=C$$
aka **_Equação de Bernoulli_** ao longo de uma linha de corrente. 
- Podemos interpretá-la como dizer que a energia mecânica transportada pelo fluido em escoamento (cinética + potencial + de escoamento) é **constante**. A variação de 1 delas implica a variação de pelo menos 1 das outras.

- Notemos que, para a deduzir, considerou-se:
    - Forças de cortes são desprezáveis em comparação com forças de inércia e gravidade.
    - Fluido incompressível
    - Escoamento estacionário

- Ao aplicar é necessário ter noção que:
    - A equação aplica-se ao longo da linha de corrente
    - Não há troca de calor entre fluido e exterior
    - Fluido não troca energia mecânica com o exterior

## 4.2 - 2ª Lei de Newton na direção normal de Linha de Corrente
- Nos escoamentos unidimensionais as linhas de corrente são retas ou quase. Temos então que a variação do vetor velocidade na direção normal às linhas de corrente $s$ é desprezável. Apesar disso, pode ser útil establecer a relação entre a 2ª Lei de Newton na direção normal $n$. Temos:
$$\sum \delta F_{n}= \delta m \cdot a_{n}=\rho \frac{v_{s}^{2}}{R}\delta V$$
(em que $R$ é o raio de curvatura)

- Vejamos as forças aplicadas no volume
    - Peso na direção normal: $\delta W_{n}=- \rho g \cos\theta \delta V$
    - Força de pressão na direção normal $n$:
        - $\delta p_{s}=\frac{1}{2} \left( \frac{\partial p}{\partial s}\delta s\right)$
        - Temos $\delta F_{p,n}= (p-\delta p_{n})\delta s \delta y- (p+\delta p_{n})\delta s \delta y= -2\delta p_{n} \delta s \delta y= - \frac{\partial p}{\partial n}\delta s \delta n \delta y= - \frac{\partial p}{\partial n}\delta V$

- A soma das forças dá: $\sum \delta F_{n}=\delta W_{n}+\delta F_{p,n}=\left(-\rho g \cos\theta - \frac{\partial p}{\partial n} \right)\delta V$
- Substituindo na 2ª Lei temos:
$$\rho \frac{v_{s}^{2}}{R}\delta V=\left(-\rho g \cos\theta - \frac{\partial p}{\partial n} \right)\delta V$$

![[componentes direçoes volume.png]]
e podemos establecer $\cos\theta= \delta z/\delta n$

- Na direção normal à linha de corrente, a componente $s$ da pressão é constante, de modo que:
$$dp= \frac{\partial p}{\partial s}ds + \frac{\partial p}{\partial n}dn\to dp=\frac{\partial p}{\partial n}dn$$

- Substituindo as 2 coisas acima na equação da 2ª Lei obtemos:
$$-\rho g \frac{dz}{dn} - \frac{dp}{dn}= \rho \frac{v_{s}^{2}}{R}$$

- Ora, para um gás o peso pode ser desprezado, pelo que a pressão varia diretamente com o quadrado da velocidade. 
- Se multiplicarmos tudo por $\frac{dn}{\rho}$ e integrarmos:
$$\int \frac{dp}{\rho}+\int \frac{v_{s}^{2}}{R}dn+gz=C$$
- Se a massa volúmica for independente da pressão temos:
$$p + \rho \int \frac{v_{s}^{2}}{R}dn+\rho gz=C$$

## 4.3 - Aplicações da Equação de Bernoulli
### 4.3.1 - Introdução
- Consideremos um fluido em escoamento de forma contínua, sem que haja acumulação.
![[conservacao massa.png]]
- Ora, é necessário que a massa de fluido que entra no tanque por unidade de tempo seja *igual* à massa de fluido que sai do tanque por unidade de tempo.
- Sendo $A_{1},A_{2}$ as áreas à entrada e saída e $v_{1},v_{2}$ as respetivas velocidades do fluido. Assim os volumes de fluido à entrada e saída são $v_{1}A_{1}\delta t, v_{2}A_{2}\delta t$. Desta forma, a massa de fluido correspondente a estes volumes é $\rho v_{1}A_{1}\delta t, \rho v_{2} A_{2}\delta t$.
- Desta forma, a quantidade de massa de fluido que passa na entrada e saída *por unidade de tempo* é $\rho v_{1}A_{1},\rho v_{2}A_{2}$. Isto dá-nos a **equação de conservação de massa / de continuidade**:
$$\boxed{\rho_{1}v_{1}A_{1}=\rho_{2}v_{2}A_{2}}$$

### 4.3.2 - Jactos Livres
![[linha corrente.png]]
- Considera-se o escoamento de um fluido (inicialmente num tanque de grande dimensão) através de um orifiício na sua base. Queremos determinar o caudal do escoamento e como este varia com a altura de liquido dentro do tanque.
- Comparando os pontos 1 e 2 com a equação de Bernoulli:
$$p_{1}+ \frac{1}{2}\rho v_{1}^{2}+\rho_{1}g z_{1}= p_{2} + \frac{1}{2}\rho v_{2}^{2}+\rho_{2}g z_{2}$$
- Temos que $\rho_{1}=\rho_{2}$ e consideraremos que $A_{1}\gg A_{2}$. Ora, isto implica que $v_{2}\gg v_{1}$
- A diferença de cota será $z_{1}-z_{2}=h(t)$
- E obtemos:
$$\begin{align*}
p_{1}+ \cancelto{~\sim0}{\frac{1}{2}\rho v_{1}^{2}} + \rho g z_{1} &= p_{2} + {\frac{1}{2}\rho v_{2}^{2}} +\rho g z_{2}\\
p_{1}-p_{2} &= \frac{1}{2}\rho v_{2}^{2} - \rho gh(t)
\end{align*}$$
(em que anulamos $v_{1}$ por ser muito inferior a $v_{2}$)
- Temos ainda que o ponto 1 está a pressão atmosférica. O jato, mal sai do tanque, está a pressão atmosférica. Ora, as linhas de corrente à saída são retas, pelo que a pressão não deverá mudar ao longo do jato, pelo que $p_{2}=p_{atm}$. Assim:
$$p_{1}=p_{2}=p_{atm}$$
o que nos dá:
$$\frac{1}{2}\rho v_{2}^{2}= \rho g h(t)~~\to~~ v_{2}=\sqrt{2gh(t)} $$
- Ora, sendo $A_{0}$ a área do orifício, o caudal será: $$Q=A_{0}\sqrt{2gh(t)}$$
- Na realidade, o diametro/área transversal do jato pode não coincidir com aquele do orificio, dependendo da geometria:
![[coeficiente contracao.png]]
sendo que a forma completa do caudal seria:
$$Q=C_{C}A_{0}\sqrt{2gh}$$
em que $C_{C}$ é o coeficiente de contração.

### 4.3.3 - Medidores de Caudal
- Se colocarmos uma restrição ao escoamento, de forma a gerar uma zona de baixa e uma de alta pressão, podemos determinar o caudal volumétrico através da diferença de pressões usando a Equação de Bernoulli

#### 4.3.3.1 - Venturi
![[venturi.png]]
- Usado para medir o caudal de líquidos e gases. Consiste num estreitamento suave da conduta onde está a ocorrer o escoamento, como vemos acima.
- Considerando que o escoamento é estacionário, que podemos ignorar as forças viscosas e que o fluido é incompressível; podemos aplicar a equação de Bernoulli entre os pontos 1 e 2:
$$p_{1}+ \frac{1}{2}\rho v_{1}^{2}+\cancel{\rho gz_{1}}= p_{2}+ \frac{1}{2}\rho v_{2}^{2} + \cancel{\rho gz_{2}}$$
podemos então escrever:
$$\begin{align*}
p_{1}+ \frac{1}{2}\rho v_{1}^{2} &= p_{2} + \frac{1}{2} \rho v_{2}^{2}\\
\frac{2}{\rho}(p_{1}-p_{2})&= v_{2}^{2} - v_{1}^{2}
\end{align*}$$
- Pela equação da continuidade temos $$A_{1}v_{1}=A_{2}v_{2}=Q$$
de onde obtemos: $v_{1}=\frac{A_{2}}{A_{1}}v_{2}$
- E obtemos:
$$\begin{align*}
\frac{2}{\rho}(p_{1}-p_{2})&= v_{2}^{2} - \frac{A_{2}^{2}}{A_{1}^{2}}v_{2}^{2}\\
v_{2}&= \sqrt{\frac{2(p_{1}-p_{2})}{\rho \left[ 1- \left(\frac{A_{2}}{A_{1}} \right)^{2}\right]}}
\end{align*}$$
logo o caudal é:
$$Q=A_{2}v_{2}=A_{2}\sqrt{\frac{2(p_{1}-p_{2})}{\rho \left[ 1- \left(\frac{A_{2}}{A_{1}} \right)^{2}\right]}}$$
- Mais uma vez, dependendo da geometria, a área do jato pode ser inferior a $A_{2}$ e temos:
$$Q=C_{C}A_{2}\sqrt{\frac{2(p_{1}-p_{2})}{\rho \left[ 1- \left(\frac{A_{2}}{A_{1}} \right)^{2}\right]}}$$
em que $C_{C}=\frac{A_{j}}{A_{2}}$

#### 4.3.3.2 - Medidor de Orifício
![[medidor orificio.png]]
- Este é um sistema barato e que portanto é frequentemente usado. Usasse um orifício cuja área central é conhecida.
- A fórmula do caudal é igual à do Venturi.

#### 4.3.3.3 - Descarregadores
- Consistem em sistemas em que medimos caudais de canais abertos para a atmosfera, que podem ter várias geometrias.

### Descarregador Retangular
![[descarregador.png]]
- É preciso considerar algumas hipóteses antes de poder aplicar a equação de Bernoulli:
    - Na superfície do descarregador (ponto 2) a velocidade é apenas horizontal
    - A variação de pressão na secção reta em que temos o ponto 1 é hidrostática
    - A superfície livre permanece horizontal entre os pontos 1 e 2
    - Tal como fizemos para o jato livre, $p_{2}=p_{atm}$
    - As tensões de corte são desprezáveis

- Ao aplicar a equação de Bernoulli temos:
$$\begin{align*}
p_{1}+\rho g z_{1}+ \frac{1}{2}\rho v_{1}^{2} &= p_{2}+ \rho g z_{2}+ \frac{1}{2} \rho v_{2}^{2}\\
\cancel{p_{atm}}+\rho g(H-z_{1})+\rho gz_{1}+ \frac{1}{2}\rho v_{1}^{2} &=  \cancel{p_{atm}}+\rho g z_{2}+ \frac{1}{2} \rho v_{2}^{2}\\
v_{2}&= \sqrt{2h(H-z_{2})+v_{1}^{2}}
\end{align*}$$
que será igual em todos os pontos do descarregador.

- Temos então o caudal numa tira infinitesimal:
$$\delta Q=v_{2} \delta A=v_{2}b ~\delta z_{2}$$
e podemos integrar:
$$Q= \int_{0}^{H} v_{2}b~dz=\int_{0}^{H}\sqrt{2g(H-z)+v_{1}^{2}}b~dz= \frac{2}{3}b \sqrt{2g} \left[ \left(H + \frac{v_{1}^{2}}{2g}\right)^{\frac{3}{2}} - \left( \frac{v_{1}^{2}}{2g} \right)^{\frac{3}{2}} \right]$$
- Na maioria dos casos teremos $H\gg \frac{v_{1}^{2}}{2g}$, logo:
$$Q=\frac{2}{3}b \sqrt{2g} H^{\frac{3}{2}}$$

### Descarregador Triangular
- O $v_{2}$ obtido da equação de Bernoulli será igual
- Para integrar $Q$ usamos matemática e integramos o triângulo com $z$ e obtemos:
$$Q= \frac{8}{15} \tan \frac{\theta}{2} \sqrt{2h} H^{\frac{5}{2}}$$


### 4.3.4 - Medidores de Velocidade
#### 4.3.4.1 - Tubo de Pitot
![[tubo pitot.png]]
- Este tubo é colocado no meio do fluxo, pelo que o altera, não sendo este sistema muito usado para obter medições muito rigorosas. Torna-se ainda pior se quisermos medir a velocidade de escoamento perto de uma parede ou sólido submerso.
- O ponto 2 está mesmo à entrada do tubo de Pitot, um tubo muito fino introduzido no escoamento.
- O ponto 1 está sob um outro tubo, também muito fino, com abertura para atmosfera. Neste ponto temos $p_{1}=p_{atm}+\rho gh$
- Pela equação de Bernoulli:
$$p_{1}+ \cancel{\rho gz_{1}}+ \frac{1}{2}\rho v_{1}^{2}=p_{2} + \cancel{\rho g z_{2}} + \bcancel{\frac{1}{2}\rho v_{2}^{2}}$$
em que o termo com $v_{2}$ foi anulado por $v_{2}=0$. Consideramos que, ao entrar no tubo de Pitot, o fluido "para" e toda a sua energia cinética é convertida em energia de pressão, sendo que $$p_{2}=p_{1}+ \frac{1}{2}\rho v_{1}^{2}$$
    - Em que a $p_{2}$ chamamos *pressão total*
    - Em que a $\frac{1}{2} \rho v_{1}^{2}$ chamamos *pressão dinâmica*
    - Em que a $p_{1}$ chamamos *pressão estática*

- Por outro lado, para o ponto 2 podemos escrever:
$$p_{2}=p_{atm}+\rho g H$$
- Juntando as 2 equações de $p_{2}$ obtemos:
$$v_{1}=\sqrt{2g(H-h)}$$
