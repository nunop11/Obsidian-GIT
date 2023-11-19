## 5.1 - Tipos de Estudos de Sistemas
- Podemos estudar sistemas de fluidos de várias formas:
### Estudos Diferenciais
- Consiste em estudar um problema a partir de elementos de fluidos infinitesimais e respetivas leis de conservação.
- Os detalhes não são ignorados e o resultado que obtemos descreve todo o campo de escoamento, velocidade e pressão.
- Em muitos casos é preciso usar computadores para resolver problemas com este método.

### Estudo Integral
- Usado nos problemas em que não tem interesse saber o que acontece a cada elemento de fluido, mas apenas à massa de fluido em estudo como um todo.
- Defenimos um *Volume de Controlo* que pode ser fixo ou móvel no espaço, rígido ou deformável no tempo.

### Estudo Experimental com suporte em Análise Dimensional
- Usado quando nenhum dos outros métodos permite obter resultados corretos, por exemplo no estudo da aerodinâmica de um carro de F1.
- Faz-se um estudo experimental com peças ou modelos à escala e a análise dimensional ajuda a tirar conclusões.

## 5.2 - Teorema do Transporte de Reynolds
### 5.2.1 - Dedução
- Este teorema serve de base para calcular as equações integrais de conservação de massa, momento e energia.
![[lei transporte reynolds.png]]
- Na figura acima temos a ponteado o nosso volume de controlo, $VC$, que é fixo, com a entrada $1$ e saída $2$. Temos o fluido a deslocar-se através o VC, com velocidade normal às áreas de entrada e saída, onde passa com velocidades $v_{1},v_{2}$.
- Assim, os elementos de fluido que em $t$ estavam na saída do volume (2), estarão à direita desta, a uma distância $\delta l_{2}=v_{2}\delta t$ após um intervalo de tempo $\delta t$. Já os elementos de fluido que em $t$ estão na entrada terão entrado para dentro do VC e percorrido $\delta l_{1}=v_{1}\delta t$.
- Desta forma, conforme a parte da direita da figura:
    - O volume de fluido que sai do VC no intervalo de tempo $\delta t$ passa a ocupar o volume $II$ adjacente à saída do fluido.
    - O volume de fluido que inicialmente estava à esquerda da entrada do VC e no intervalo $\delta t$ entra nele é $I$.
    - Ou seja, o volume de fluido que em $t$ está no VC passa a ocupar o volume $VC-I+II$ após o intervalo $\delta t$.

- Consideremos $B$ uma propriedade extensiva (que depende da massa do sistema). No instante inicial, $t$, temos:
$$B_{sist}(t)=B_{VC}(t)$$
após o intervalo $\delta t$ temos:
$$B_{sist}(t+\delta t)=B_{VC}(t+\delta t)-B_{I}(t+\delta t)+B_{II}(t+\delta t)$$
em que a variação de $B_{sist}$ por unidade de tempo será:
$$\begin{align*}
\frac{\delta B_{sist}}{\delta t}&= \frac{B_{sist}(t+\delta t)-B_{sist}(t)}{\delta t}\\
&= \frac{B_{VC}(t+\delta t)-B_{I}(t+\delta t)+B_{II}(t+\delta t)-\overbrace{B_{sist}(t)}^{=B_{VC}(t)}}{\delta t}\\
&= \frac{B_{VC}(t+\delta t)-B_{VC}(t)}{\delta t} - \frac{B_{I}(t+\delta t)}{\delta t} + \frac{B_{II}(t+\delta t)}{\delta t}
\end{align*}$$

- Consideremos o limite $\delta t\to0$. Vejamos cada parcela:
    - $\lim\limits_{\delta t\to0} \frac{\partial B_{sist}}{\partial t}=\frac{DB_{sist}}{Dt}$ -- Isto é a variação da propriedade $B$ no sistema como um todo por unidade de tempo. A esta derivada chamamos *derivada total ou substancial*
    - $\lim\limits_{\delta t\to0} \frac{\partial B_{VC}(t+\delta t)-B_{VC}(t)}{\partial t}$ -- Representa a variação de $B$ no VC por unidade de tempo. Podemos definir $b=B/m$ ($B$ por unidade de massa), sendo que $B=\int_{VC} \rho b dV$ (em que $dV$ é um elemento de volume infinitesimal). Fica então: $$\lim\limits_{\delta t\to0} \frac{\partial B_{VC}(t+\delta t)-B_{VC}(t)}{\partial t}=\frac{\partial B_{VC}}{\partial t}= \frac{\partial}{\partial t}\int_{VC} \rho b~dV$$
    - $\lim\limits_{\delta t\to0}\frac{B_{II}(t+\delta t)}{\delta t}$ -- Esta parcela representa a "velocidade" com que $B$ sai do VC pela área de controlo. Facilmente vemos que a porção de $B$ que temos no volume $II$ será $B_{II}(t+\delta t)=\rho_{2}b_{2}A_{2}\delta l_{2}=\rho_{2}b_{2}A_{2}v_{2}\delta t$, pelo que é trivial que: $$\lim\limits_{\delta t\to0}\frac{B_{II}(t+\delta t)}{\delta t}=\rho_{2}b_{2}A_{2}v_{2}$$
    - $\lim\limits_{\delta t\to0}\frac{B_{II}(t+\delta t)}{\delta t}$ -- Este termo representa a "velocidade" com que $B$ entra no VC pela área de controlo. Analogamente ao que fizemos para o termo anterior temos: $$\lim\limits_{\delta t\to0}\frac{B_{I}(r+\delta t)}{\delta t}=\rho_{1}b_{1}A_{1}v_{1}$$
- E temos então:
$$\frac{DB_{sist}}{Dt}= \frac{\partial}{\partial t}\int_{VC}\rho b~dV+\rho_{2}A_{2}b_{2}v_{2}-\rho_{1}A_{1}b_{1}v_{1} $$

### 5.2.2 - Teorema do Transporte de Reynolds Generalizado
- Na dedução acima assumimos que a velocidade do fluido na entrada e na saída é uniforme e perpendicular à Área de Controlo. Vamos melhorar então o resultado obtido.

![[lei transporte reynolds 2.png]]
- Seja $v$ a velocidade com que o fluido atravessa a área infinitesimal $\delta A$ na saída do VC. O volume de fluido que passa nessa área no intervalo $\delta t$ será: $$\delta V=\delta \vec{l}\cdot \delta \vec{A}= \delta t \vec{v}\cdot \hat{n}\delta A=v \delta t \cos\theta \delta A$$ (em que $\theta$ é o ângulo entre o vetor normal à área e o vetor velocidade)
- A quantidade de $b$ incluida neste volume de fluido será então: $$b \rho \delta V=b \rho v \delta t \cos\theta \delta A$$
- E podemos então escrever: $$\lim\limits_{\delta t\to0}\frac{B_{II}(t+\delta t)}{\delta t} = \int_{A_{saida}}\rho bv \cos \theta ~dA=\int_{A_{saida}}\rho b (\vec{v}\cdot \hat{n})dA$$

![[lei transporte reynolds 3.png]]
- Já na entrada do VC o vetor normal à área aponta para fora e portanto tem direção oposta à velocidade. Assim, evidentemente temos:
$$\lim\limits_{\delta t\to0}\frac{B_{I}(t+\delta t)}{\delta t}=-\int_{A_{entrada}}\rho bv\cos\theta ~dA=-\int_{A_{entrada}}\rho b (\vec{v}\cdot\hat{n})dA$$

- E podemos então fazer a relação entre o que sai e o que entra no VC:
$$\lim\limits_{\delta t\to0}\frac{B_{II}(t+\delta t)}{\delta t}-\lim\limits_{\delta t\to0}\frac{B_{I}(t+\delta t)}{\delta t}=\int_{A_{saida}}\rho b (\vec{v}\cdot \hat{n})dA-\int_{A_{entrada}}\rho b (\vec{v}\cdot\hat{n})dA=\int_{AC}\rho b (\vec{v}\cdot\hat{n})dA$$

- O Teorema de Transporte de Reynolds fica então na forma:
$$\frac{DB_{sist}}{Dt}=\frac{\partial}{\partial t}\int_{VC}\rho b ~dV+\int_{AC}\rho b ~\vec{v}\cdot\hat{n}~dA$$
- De notar que:
    - Em problemas em que o VC se move a uma velocidade constante podemos substituir $\vec{v}$ pela velocidade relativa: $\vec{v}\to \vec{v}_{rel}=\vec{v}-\vec{v}_{VC}$
    - Na maioria dos problemas desta matéria temos $\frac{DB_{sist}}{Dt}=0$, umas vez que este termo expressa a variação da Massa, Momento, etc. do sistema no tempo; se essa propriedade é conservada, este termo é nulo!

## 5.3 - Conservação de Massa
- Quando a propriedade $B$ é a massa do sistema temos $b=1$ (porque $b$ é $B$ por unidade de massa). O teorema de transporte de Reynolds fica na forma:
$$\frac{DM_{sist}}{Dt}= \frac{\partial}{\partial t}\int_{VC}\rho dV+\int_{AC}\rho \vec{v}\cdot\hat{n}~dA$$
- Ora, dentro de um sistema tem que haver conservação de massa, logo $\frac{DM_{sist}}{Dt}=0$ e fica:
$$\frac{\partial}{\partial t}\int_{VC}\rho dV+\int_{AC}\rho \vec{v}\cdot \hat{n}~dA=0$$
