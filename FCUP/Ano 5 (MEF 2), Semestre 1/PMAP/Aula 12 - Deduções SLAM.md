(Isto na realidade é parte da Aula 11 e a Aula 12)
- Como vimos na aula 11, quando temos um robot a fazer SLAM, podemos descrever o sistema por
$$x=\begin{pmatrix}x_{R} \\ m\end{pmatrix} ~~~~,~~~~P=\begin{pmatrix}P_{x_{R}x_{R}} & P_{x_{R}m} \\ P_{mx_{R}} & P_{mm}\end{pmatrix}$$

### Dinâmica EKF
- Em EKF temos um sistema descrito por uma função não linear
- Temos que a **evolução** do sistema é dada por
$$\begin{cases}
x_{R,n+1}=f(x_{R,n}, u_{n})+w_{n} \\
P_{n+1}= f_{x}P_{n}f_{x}^{T}+Q
\end{cases}$$
em que $f(\cdot)$ é uma função não linear, $f_{x}$ é a sua matriz jacobiana e $w_{n}\sim N(0,Q)$.

### Dinâmica SLAM EKF
#### Evolução da posição
- Consideramos que os marcos estão fixos, pelo que as suas posição não mudam entre iterações:
$$\begin{pmatrix}x_{R,n+1} \\ m_{n+1}\end{pmatrix}=\begin{pmatrix}f(x_{R,n}, u_{n}) \\ m_{n}\end{pmatrix}+\begin{pmatrix}w_{n} \\ 0\end{pmatrix}$$
- Podemos ver a evolução da posição média:
$$\mu_{n+1}=f(\mu_{n},u_{n})$$

#### Evolução da covariância
- E podemos facilmente definir a jacobiana alargada para conter os marcos:
$$f_{xm}=\begin{pmatrix}f_{x} & 0 \\ 0 & I\end{pmatrix}$$
- E fica:
$$\begin{align*}
P_{n+1}&= f_{xm}P_{n}f_{xm}^{T}+Q\\
&= \begin{pmatrix}f_{x} & 0\\
0 & I\end{pmatrix}\begin{pmatrix}P_{x_{R}x_{R}} & P_{x_{R}m}\\
P_{mx_{R}} & P_{mm}\end{pmatrix}\begin{pmatrix}f_{x}^{T} & 0\\
0 & I\end{pmatrix} + \begin{pmatrix}Q & 0\\
0 & 0\end{pmatrix}\\
&= \begin{pmatrix}f_{x}P_{x_{R}x_{R}} & f_{x}P_{x_{R}m}\\
IP_{mx_{R}} & IP_{mm}\end{pmatrix}\begin{pmatrix}f_{x}^{T} & 0\\
0 & I\end{pmatrix} + \begin{pmatrix}Q & 0\\
0 & 0\end{pmatrix}\\
&= \begin{pmatrix}f_{x}P_{x_{R}x_{R}}f_{x}^{T} & f_{x}P_{x_R m}I\\
IP_{mx_{R}}f_{x}^{T} & IP_{mm}I\end{pmatrix}+\begin{pmatrix}Q & 0\\
0 & 0\end{pmatrix}\\
&= \begin{pmatrix}f_{x}P_{x_{R}x_{R}}f_{x}^{T} & f_{x}P_{x_{R}m}\\
P_{mx_{R}}f_{x}^{T} & P_{mm}\end{pmatrix}+\begin{pmatrix}Q & 0\\0
 & 0\end{pmatrix}\\
&= \begin{pmatrix}f_{x}P_{x_{R}x_{R}}f_{x}^{T}+Q & f_{x}P_{x_{R}m}\\
P_{mx_{R}}f_{x}^{T} & P_{mm}\end{pmatrix}
\end{align*}$$
Veremos abaixo como obter todas estas componentes.

### Medição feita!
- Consideramos que as medições seguem o modelo:
$$z=h(x_{R}~,~m_i)$$
ou seja: a medição que fazemos depende da posição do robot (lógico) e do marco $m_{i}$ que poderemos estar a ver
- Consideramos que foi visto um marco $m_{i}$.
- Tendo um sistema de LIDAR, o vetor de medição será sempre algo do tipo $$z=\begin{pmatrix}d \\ \alpha\end{pmatrix}$$
em que temos a distância $d$ do ponto medido ao robot e o ângulo $\alpha$ que ele faz com a orientação do robot (o angulo do marco, relativamente ao eixo dos xx será $\theta+\alpha$)

- Podemos desenvolver os valores medidos no LIDAR:
$$d=\sqrt{(x_{i}-x_{R})^{2} + (y_{i}-y_{R})^{2}} \quad;\quad \alpha=\arctan \left(\frac{y_{i}-y_{R}}{x_{i}-x_{R}} \right)$$
ou, inversamente:
$$x_{i}=x_{R}+d\cos(\alpha+\theta) \quad ;\quad y_{i}=y_{R}+d\sin(\alpha+\theta)$$
- Mas espera! Temos então a função de medição deste sistema:
$$z=h(x_{R},m_{i})=\begin{pmatrix}d \\ \alpha\end{pmatrix}=\begin{pmatrix}\sqrt{(x_{i}-x_{R})^{2} + (y_{i}-y_{R})^{2}} \\ \arctan \left(\frac{y_{i}-y_{R}}{x_{i}-x_{R}} \right)\end{pmatrix}$$
mas também temos a função inversa:
$$\boxed{m_{i}=g(x_{R},z)}=\begin{pmatrix}x_{R}+d\cos(\alpha+\theta) \\ y_{R}+d\sin(\alpha+\theta)\end{pmatrix}$$
em que $g(\cdot)$ permite **obter m a partir da posição e de 1 medição**. Ou seja, dá-nos a posição do marco a partir da nossa medição dele.

### Algoritmo de medições
1. Fazemos uma medição $z=\begin{pmatrix}d & \alpha\end{pmatrix}$
2. Usamos a função $g(\cdot)$ para calcular $m_{i}=\begin{pmatrix}x_{i} & y_{i}\end{pmatrix}$
3. Vemos se esta marca é nova ou não. Para isso, simplesmente fazemos um critério de distância. Se $m_{i}$ estiver a menos de uma distância X do marco $m_{j}$ então estamos a rever $m_{j}$
    1. Se estivermos a ver um marco novo, temos que alargar o sistema. Por exemplo, se este for o primeiro marco que encontramos: $$x\to\begin{pmatrix}x \\ m_{1}\end{pmatrix} \quad;\quad P_{xx}\to \begin{pmatrix}P_{xx} & P_{xm_{1}} \\ P_{m_{1}x} & P_{m_{1}m_{1}}\end{pmatrix}$$
4. Repetir para cada medição feita

- **NOTA**: quando falamos em marcos, normalmente referi-mo-nos a certos pontos representativos do ambiente que decidimos previamente. Por exemplo, marcos podem ser cantos das paredes, paredes em si ou outras coisas. Ou seja, em muitas iterações este algoritmo nem será usado. Isto será usado apenas ao ver um marco.

### Dedução de covariâncias
- Falta apenas definir as equações que nos permitem determinar os elementos da matriz de covariância.
**xx**
- Em EKF, sabemos que a covariância da estimativa de estado é:
$$P_{n}^{-}=f_{x}P_{n-1}^{+}f_{x}^{T} + Q$$

**mm**
- Podemos aplicar uma série de Taylor em $g(\cdot)$:
$$m=g(x,z) = g(\overline{x},\overline{z}) + g_{x}(x-\overline{x}) + g_{z}(z-\overline{z})$$
em que notemos que $g_{x},g_{z}$ são matrizes jacobianas:
$$g_{x}=\frac{\partial g(x,z)}{\partial x}\Biggr|_{x=\hat{x}_{k}} \quad;\quad g_{z}=\frac{\partial g(x,z)}{\partial z}\Biggr|_{x=z_{k}}$$
(em que $\hat{x}_{k}$ é a estimativa atualizada do estado atual)

- Tendo isto, podemos calcular $P_{mm}$:
$$\begin{align*}
P_{mm}&= \mathbb{E}\{ [g(x,z) - g(\overline{x},\overline{z})]\cdot[g(x,z)-g(\overline{x},\overline{z})]^{T} \}\\
&= \mathbb{E} \{ [g_{x}(x-\overline{x})+g_{z}(z-\overline{z})]\cdot[g_{x}(x-\overline{x})+g_{z}(z-\overline{z})]^{T} \}\\
&= \mathbb{E} \{ g_{x}(x-\overline{x})(x-\overline{x})^{T}g_{x}^{T} + g_{z}(z-\overline{z})(z-\overline{z})^{T}g_{z}^{T}+\dots \}\\
&= g_{x}P_{xx}g_{x}^{T} + g_{z}Rg_{z}^{T}
\end{align*}$$
em que simplesmente rejeitamos os termos cruzados $(x-\overline{x})(z-\overline{z})$, considerando que o a medição é independente do estado.

- Acerca da matriz **R** notemos que:
$$R=\begin{pmatrix}\sigma_{\alpha}^{2} & 0 \\ 0 & \sigma_{d}^{2}\end{pmatrix}$$
    - Notemos que $R_{12}=R_{21}=0$ assume que as medições de angulo e distância são *independentes*. Na maioria dos lidares isto está correto porque só temos um sensor laser a rodar, então as 2 funções estão separadas
    - $\sigma_{d}^{2}$ podemos obter através de calibração ou outros métodos diretos
    - $\sigma_{\alpha}^{2}\sim0$, isto porque usamos sensores laser (em LIDARs) e a variância é quase desprezável
        - O erro será da ordem de milimetros: $e\ll1$. A variância ($\propto e^{2}$) será $\sigma_{\alpha}^{2}\lll1$

- Nota sobre **gz**: 
    - Esta jacobiana tem 2 componentes dentro dela, logo: $$z=\begin{pmatrix}\alpha & d\end{pmatrix}~~\to~~ g_{z}=\begin{pmatrix}g_{\alpha} & g_{d}\end{pmatrix}$$
- Nota sobre **gx**: 
    - Esta jacobiana tem 2 componentes dentro dela, logo: $$x=\begin{pmatrix}x & y & z\end{pmatrix}~~\to~~ g_{z}=\begin{pmatrix}g_{x} & g_{y} & g_{z}\end{pmatrix}$$

**mx**
- Podemos repetir a lógica acima para, mas a misturar $m$ e $x$:
$$\begin{align*}
m&= g(x,z) = g(\overline{x},\overline{z}) + g_{x}(x-\overline{x}) + g_{z}(z-\overline{z})\\
\Delta m&= g(x,z)-g(\overline{x},\overline{z})=g_{x}(x-\overline{x}) + g_{z}(z-\overline{z})\\
\\
&\begin{cases}
\Delta x &= x- \overline{x}\\
\Delta z &= z- \overline{z}
\end{cases} ~~\to ~~ \Delta m=g_{x}\Delta x+g_{z} \Delta z\\
&~~\downarrow\\
&~~P_{ab}=\mathbb{E}\{ (a-\overline{a})(b-\overline{b})^{T} \}=\mathbb{E}\{ \Delta a \Delta b^{T} \}
\end{align*}$$
- Assim, temos a covariância cruzada:
$$\begin{align*}
P_{xm}&= \mathbb{E}\{\Delta x\Delta m^{T}\}\\
&= \mathbb{E} \{ \Delta x (g_{x}\Delta x+g_{z}\Delta z)^{T}\}\\
&= \mathbb{E} \{ \Delta x g_{x}^{T}\Delta x^{T} + \Delta x g_{z}^{T}\Delta z^{T} \}\\
&= \mathbb{E}\{\Delta x \Delta x^{T}\}g_{x}^{T} + \cancelto{\text{x,z indep}}{\mathbb{E}\{ \Delta x \Delta z^{T}\}}g_{z}^{T}\\
&= P_{xx}g_{x}^{T}\\\\
P_{mx}&= P_{xm}^{T}=g_{x}P_{xx}^{T}
\end{align*}$$

## Aplicar o SLAM EKF 
### 1. Previsão EKF
- Por definição em EKF temos:
$$x^{-}_{n+1}=f(x^{+}_{n},u_{n})$$
em que, no contexto do robot, $f(\cdot)$ representa a **odometria** do robot : permite estiamr a posição do robot sabendo a posição atual e os controlos dados.

- Podemos aplicar novamente fourier:
$$\begin{align*}
x_{n+1}^{-}-\mathbb{E}\{ x_{n+1}^{-} \} &= f(x_{n}^{+},u_{n}) - f \left(\mathbb{E} \{ x_{n}^{+},u_{n} \} \right)\\
&= \bigg( \cancel{f(\mathbb{E}[x_{n}^{+}], \mathbb{E}[u_{n}])} + f_{x}(\mathbb{E}[x_{n}^{+}], \mathbb{E}[u_{n}])\cdot(x_{n}^{+}-\mathbb{E}[x_{n}]) + \\
&+f_{u}(\mathbb{E}[x_{n}^{+}], \mathbb{E}[u_{n}])\cdot(u_{n}-\mathbb{E}[u_{n}])\bigg) - \cancel{f(\mathbb{E}\{ x_{n}^{+},u_{N} \})}\\
&= f_{x}(\mathbb{E}[x_{n}^{+}], \mathbb{E}[u_{n}])\cdot(x_{n}^{+}-\mathbb{E}[x_{n}^{+}]) + f_{u}(\mathbb{E}[x_{n}^{+}], \mathbb{E}[u_{n}])\cdot(u_{n}-\mathbb{E}[u_{n}])
\end{align*}$$
logo podemos calcular
$$\begin{align*}
P_{n+1}^{-}&= \mathbb{E}\{ [x_{n+1}^{-} -\mathbb{E}\{x_{n+1}^{-}\} ]\cdot[x_{n+1}^{-} -\mathbb{E}\{x_{n+1}^{-}\} ]^{T} \}\\
&~~\vdots ~~~~\text{(desprezar termos cruzados)}\\
&= f_{x}P_{n}^{+}f_{x}^{T} + f_{u}Qf_{u}^{T}
\end{align*}$$

### 2. Medições são feitas
- Fazemos o algoritmo que vimos acima. 
- Detetamos um marco em $z$. Vamos a cada um dos $n$ marcos que conhecemos
    - Se estamos a ver o marco $i$, então deveríamos ter medido $z=h(x,m_{i})$. Podemos usar isto para ver a distância da medição ao esperado
    - OU podemos determinar o marco que deveriamos ver, se $z$ for um marco já conhecido: $m_{j}=g(x,z)$. Podemos ver o marco $m_{i}$ a menor distância de $m_{j}$
- O marco que estamos a ver será aquele mais próximo da medição (usando um dos métodos acima) e dentro de um range de tolerância de erro que definimos

#### Marco 1
- Consideremos que vimos o nosso *primeiro* marco:
$$[x]\to\begin{bmatrix}x_{n} \\ y_{n} \\ z_{n} \\ m_{1x} \\ m_{1y}\end{bmatrix}~~~~;~~~~[P_{xx}]\to\begin{bmatrix}P_{xx} & P_{xm_{1}} \\ P_{m_{1}x} & P_{m_{1}m_{1}}\end{bmatrix}~~;~~Q\to\begin{bmatrix}Q & 0 \\ 0 & 0\end{bmatrix}~~;~~f_{x}\to\begin{bmatrix}f_{x} & 0 \\ 0 & I\end{bmatrix}$$
- Alargamos o sistema assim e calculamos $P_{m_{1}x},P_{xm_{1}},P_{m_{1}m_{1}}$

#### Marco novo
- Consideremos que encontramos um marco novo, mas já tinhamos alguns antes:
$$\begin{bmatrix}x \\ m_{1}\end{bmatrix}\to \begin{bmatrix}x \\ m_{1} \\ m_{2}\end{bmatrix}~~,~~ \begin{bmatrix}P_{xx} & P_{xm_{1}} \\ P_{m_{1}x} & P_{m_{1}m_{1}}\end{bmatrix}\to 
\left[\begin{array}{cc}\begin{array}{}\begin{matrix}P_{xx} & P_{xm_{1}} \\ P_{m_{1}x} & P_{m_{1}m_{1}}\end{matrix} \\ \hline \end{array}\Biggr| & \begin{matrix}P_{xm_{2}} \\ P_{m_{1}m_{2}}\end{matrix}\\
\begin{matrix}P_{m_{2}x} & P_{m_{2}m_{1}}\end{matrix} & P_{m_{2}m_{2}}
\end{array}\right]$$
- *Normalmente* podemos considerar as covariâncias cruzadas dos marcos nulas! Isto foi refereido na aula anterior.
    - Estas covariâncias não são necessariamente más, porque ajudam a establecer ligações entre marcos no ambiente
    - Mas no caso de termos sensores de distância (e não câmaras), o mais comum é os marcos não estarem correlacionados, logo poderemos asusmir que $P_{m_{i}m_{j}}=0$
    - Notar que considerar estas covariâncias não nulas implica estar a estudar os pontos medidos 1 a 1
    - MAS estas covariâncias podem ser mesmo **não nulas** - basta termos 2 cantos identificados na mesma iteração - a maneira como detetamos cada um tem correlações

- Como já vimos atrás, temos que expandir todas as matrizes *jacobianas*. Mas notemost:
$$h(x,m)~~\to~~ h_{x}=\begin{pmatrix}h_{x} \\ h_{y} \\ h_{\theta} \\ 0 \\ 0 \\ 0 \\ 0\end{pmatrix}~,~h_{m_{1}}=\begin{pmatrix}0 \\ 0 \\ 0 \\ h_{xm_{1}} \\ h_{ym_{2}} \\ 0 \\ 0\end{pmatrix}~,~h_{m_{2}}=\begin{pmatrix}0 \\ 0 \\ 0 \\ 0 \\ 0 \\ h_{xm_{2}} \\ h_{ym_{2}}\end{pmatrix}$$

### 3. EKF
- Aplicamos o EKF para atualizar as covariâncias, as estimativas etc
- Existem fórmulas online de como atualizar $P_{xm_{i}},P_{m_{i}m_{j}}$
