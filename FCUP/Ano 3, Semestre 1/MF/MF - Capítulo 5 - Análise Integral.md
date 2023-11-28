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
### 5.3.1 - Dedução da Equação de Reynolds
- Quando a propriedade $B$ é a massa do sistema temos $b=1$ (porque $b$ é $B$ por unidade de massa). O teorema de transporte de Reynolds fica na forma:
$$\frac{DM_{sist}}{Dt}= \frac{\partial}{\partial t}\int_{VC}\rho dV+\int_{AC}\rho \vec{v}\cdot\hat{n}~dA$$
- Ora, dentro de um sistema tem que haver conservação de massa, logo $\frac{DM_{sist}}{Dt}=0$ e fica:
$$\frac{\partial}{\partial t}\int_{VC}\rho dV+\int_{AC}\rho \vec{v}\cdot \hat{n}~dA=0$$

(Fazer exs e tomar notas)

## 5.4 - Equação da energia - 1ª Lei Termodinâmica
### 5.4.1 - Dedução da Equação 
- Sendo $e$ a energia por unidade de massa o teorema do transporte de Reynolds fica:
$$\frac{D}{Dt}\int_{sist} e\rho ~dV=\frac{\partial}{\partial t}\int_{VC}e \rho~dV+\int_{AC}e \rho \vec{v}\cdot\hat{n}~dA$$
em que:
    - *primeiro termo* -  representa a variação da energia total do sistema por unidade de tempo
    - *segundo termo* - representa a variação da quantidade de energia que se encontra dentro do VC por unidade de tempo
    - *terceiro termo* - fluxo de energia pela AC

- Além de $e=E/M$ podemos escrever a energia por unidade de massa como a soma das componentes de energia interna, cinética e potencial:
$$e=u+ \frac{1}{2}v^{2}+gz$$
- Pela 1ª Lei da Termodinâmica, a variação da energia do sistema será dada por:
$$\frac{D}{Dt} \int_{sist} e \rho dV= \sum\limits \dot{Q}_{sist}+\sum\limits \dot{W}_{sist}$$
(em que $\dot{Q},\dot{W}$ são as energias trocadas por trocas de calor e trabalho realizado sobre/pelo sobre o sistema. Os pontos são meramente uma questão de notação)

- Tal como em física térmica, $Q,W$ positivos representam energia que entra no sistema a partir da sua vizinhança:
$$\sum\limits \dot{Q}_{sist}=\sum\limits \dot{Q_{e}}-\sum\limits \dot{Q_{s}}$$
$$\sum\limits \dot{W}_{sist}=\sum\limits \dot{W_{e}}-\sum\limits \dot{W_{s}}$$

- Para $t=t_{0}$ o sistema está todo contido no VC, pelo que:
$$\left(\sum\limits\dot{Q}+\sum\limits\dot{W} \right)_{sist}=\left(\sum\limits\dot{Q}+\sum\limits\dot{W} \right)_{VC}$$
- Usando a equação $\frac{D}{Dt} \int_{sist} e \rho dV= \sum\limits \dot{Q}_{sist}+\sum\limits \dot{W}_{sist}$ e a lei de transporte de Reynolds para energia que obtivemos no início desta secção, temos:
$$\frac{\partial}{\partial t}\int_{VC}e\rho dV+\int_{AC}e \rho \vec{v}\cdot\hat{n}dA=\left(\sum\limits\dot{Q}+\sum\limits\dot{W} \right)_{VC}$$
aka *1ª Lei da Termodinâmica aplicada a um volume de controlo*.

### Trabalho
- Há 2 formas de realizar/fornecer trabalho ao VC:
    - Trabalho sobre o veio - trabalho fornecido ao VC por pás, turbinas, pistões, etc
    - Trabalho dos elementos de Fluido sobre o VC

- Vejamos o segundo. 
![[forças aplicadas em fluxo.png]] 
- Começamos por definir o VC de forma que *não* se incluia as paredes. 
- Para estudar o trabalho realizado sobre um fluido em escoamento, vamos partir de um caso particular e simples: um fluido a escoar num tubo.
- O trabalho por unidade de tempo (potência) que as forças de tensão normais  (figura da direita) realizam ao atuar num elemento de fluido será $\delta \dot{W}_{p}$ e é dado por:
$$\delta \dot{W}_{p}=\delta \vec{F}_{p}\cdot\vec{v}$$ (daí falarmos em trabalho por unidade de tempo, porque a velocidade tem unidades $L/t$)
- As forças de tensão normais podem ser escritas como $\delta\vec{F_{p}}=-p\hat{n}\delta A$ ($\hat{n}$ é o versor normal ao elemento infinitesimal em estudo, a apontar para fora). Logo:
$$\delta \dot{W}_{p}=-p \vec{v}\cdot\hat{n}\delta A$$
e se integrarmos em todo o VC:
$$\dot{W}_{p}=\int_{AC}-p \vec{v}\cdot \hat{n} dA$$
(ficamos apenas com integral na AC invés do VC porque no interior do volume as forças de pressão anulam-se todas)

- As forças de tensão tangenciais (figura de baixo) *não realizam trabalho sobre o VC*. 
    - Nas superfícies de "entrada" e "saída" de fluido (faces da direita e esquerda na figura) temos $\vec{v}\perp\vec{F_{\tau}}$ e o trabalho será sempre nulo. 
    - Restam as superfícies de cima e baixo AKA superfícies de contacto entre o fluido e o tubo. Assim, podemos fazer dizer que o trabalho de forças de tensão tangenciais é nulo apenas se assumirmos a **condição de não deslizamento** AKA se assumirmos que a velocidade do fluido nas superfícies de contacto com o tubo é nula!!!

- Assim a 1ª Lei da Termodinâmica para um VC fica:
$$\begin{align*}
\frac{\partial}{\partial t}\int_{VC}e\rho dV+\int_{AC}e \rho \vec{v}\cdot\hat{n}dA&= \left(\sum\limits\dot{Q}+\sum\limits\dot{W} \right)_{VC}\\
&= \dot{Q} + \dot{W}_{veio} - \int_{AC}p \vec{v}\cdot \hat{n}dA
\end{align*}$$
e podemos escrever:
$$\frac{\partial}{\partial t}\int_{VC}e\rho dV+\int_{AC}\left(u + \frac{p}{\rho}+ \frac{v^{2}}{2}+gz \right) \rho \vec{v}\cdot\hat{n}dA=\dot{Q}+\dot{W}_{veio}$$

### 5.4.2 - Estado Estacionário
- Um estado estacionário é aquele em que a energia no VC é constante. Logo:
$$\frac{\partial}{\partial t}\int_{VC}e\rho dV=0 \longrightarrow \int_{AC}\left(u + \frac{p}{\rho}+ \frac{v^{2}}{2}+gz \right) \rho \vec{v}\cdot\hat{n}dA=\dot{Q}+\dot{W}_{veio}$$
- Ficamos apenas com um integral na AC. Portanto, se $p,\rho,v$ forem uniformes ao longo das superfícies de entrada e saída do VC podemos escrever:
$$\int_{AC}\left(u + \frac{p}{\rho}+ \frac{v^{2}}{2}+gz \right) \rho \vec{v}\cdot\hat{n}dA= \left(u + \frac{p}{\rho}+ \frac{v^{2}}{2}+gz \right)_{s}\dot{m_{s}}-\left(u + \frac{p}{\rho}+ \frac{v^{2}}{2}+gz \right)_{e}\dot{m_{e}}$$
em que $\dot{m}$ é caudal mássico. Os índices $e,s$ representam "entrada" e "saída".

- Assim, para sistemas estacionários, com escoamento unidimensional com propriedades distribuidas uniformemente pelas secções de entrada e saída do VC temos:
$$\left(u + \frac{p}{\rho}+ \frac{v^{2}}{2}+gz \right)_{s}\dot{m_{s}}-\left(u + \frac{p}{\rho}+ \frac{v^{2}}{2}+gz \right)_{e}\dot{m_{e}}=\dot{Q}+\dot{W}_{veio}$$
a esta equação chamaremos muitas vezes de **Equação da Energia**.

- Se não ocorrer acumulação de fluido no VC temos $\dot{m_{e}}=\dot{m_{s}}=\dot{m}$. Podemos ainda definir a **entalpia** $h=u + p/\rho$ e fica:
$$\left(h_{s}-h_{e} + \frac{v_{s}^{2}-v_{e}^{2}}{2}+g(z_{s}-z_{e}) \right)\dot{m}= \dot{Q}+\dot{W}_{veio}$$

### 5.4.3 - Aplicação a algumas máquinas
#### Estrangulamento Adiabático
- Simplificação que representa razoavelmente sistemas como: escoamento através de válvula parcialmente aberta, escoamento através de válvula de expansão de frigorífico, etc
- Se considerarmos: 
    - escoamento estacionário e horizontal
    - velocidades de entrada e saída do VC iguais
    - não há trocas de calor com o VC. 
- Obtemos da equação de energia que
$$h_{s}=h_{e}$$

#### Turbinas e Compressores
- Turbina ou máquina de expansão permite extrair trabalho de fluido em escoamento. Compressores/bombas fazem o oposto: fornecem trabalho ao fluido.
- Assumindo: 
    - escoamento estacionário
    - entrada e saída à mesma cota
    - sem trocas de calor
    - caudais mássicos de entrada e saída iguais
    - variação de energia cinética entre entrada e saída é $\sim0$
- Resulta da equação de energia:
$$\frac{\dot{W}_{veio}}{\dot{m}}=h_{s}-h_{e}$$
### 5.4.4 - Comparação entre Equação da Energia e Bernoulli
- Se tivermos um sistema estacionário, com as propriedades uniformes na entrada e saída do VC e sem trabalho no veio, temos:
$$\left(u + \frac{p}{\rho}+ \frac{v^{2}}{2}+gz \right)_{s}\dot{m_{s}}-\left(u + \frac{p}{\rho}+ \frac{v^{2}}{2}+gz \right)_{e}\dot{m_{e}}=\dot{Q}$$
dividindo tudo por $\dot{m}$ e reorganizando:
$$\frac{p_{s}}{\rho}+ \frac{v_{s}^{2}}{2} + gz_{s} = \frac{p_{e}}{\rho}+ \frac{v_{e}^{2}}{2} + gz_{e} - (u_{s}-u_{e}-q)$$
(em que definimos $q=\dot{Q}/\dot{m}$)
- A equação de Bernoulli aplicada a este sistema (sem tensões transversais AKA sem viscosidade) tem a forma:
$$\frac{p_{s}}{\rho}+ \frac{v_{s}^{2}}{2} + gz_{s} = \frac{p_{e}}{\rho}+ \frac{v_{e}^{2}}{2} + gz_{e}$$
- Assim, podemos concluir para que não haja viscosidade no escoamento, é preciso que:
$$u_{s}-u_{e}-q\simeq0$$
- Ou seja, o termo $u_{s}-u_{e}-q$ representa a energia dissipada pela viscosidade. Por outras palavras:
$$u_{s}-u_{e}-q=perdas$$
- Ou seja, podemos escrever a equação da energia na forma:
$$\frac{p_{s}}{\rho}+ \frac{v_{s}^{2}}{2} + gz_{s} = \frac{p_{e}}{\rho}+ \frac{v_{e}^{2}}{2} + gz_{e} + w_{veio}-perdas$$
(em que $w_{perdas}=\dot{W}_{perdas}/\dot{m}$)
- Podemos ler esta equação como: a energia que entra no sistema é igual àquela que saio do sistema + aquela que é perdida.

### 5.4.5 - Equação da Energia para escoamentos não uniformes
- No caso em que a velocidade não é uniforme nas superfícies de entrada e saída do VC, o integral $\int \frac{v^{2}}{2}\rho \vec{v}\cdot\hat{n}dA$ torna-se complicado. Podemos então definir:
$$\int \frac{v^{2}}{2}\rho \vec{v}\cdot\hat{n}dA= \dot{m} \left(\frac{\alpha_{s}\bar v_{s}^{2}}{2}-\frac{\alpha_{e}\bar v_{e}^{2}}{2} \right)$$
em que:
$$\alpha_{s}=\frac{\int_{A_{s}} \frac{v^{2}}{2}\rho \vec{v}\cdot\hat{n}dA}{\dot{m}\frac{\bar v_{s}^{2}}{2}} \quad \quad;\quad \quad \alpha_{e}=\frac{\int_{A_{e}} \frac{v^{2}}{2}\rho \vec{v}\cdot\hat{n}dA}{\dot{m}\frac{\bar v_{e}^{2}}{2}}$$
em que $\alpha_{s},\alpha_{e}$ são os *coeficientes de energia cinética* e $\bar v$ as velocidades médias na superfície de entrada e saída.

- A equação da energia para escoamentos não uniformes fica então:
$$\frac{p_{s}}{\rho}+ \frac{\alpha_{s}\bar v_{s}^{2}}{2} + gz_{s} = \frac{p_{e}}{\rho}+ \frac{\alpha_{e}\bar v_{e}^{2}}{2} + gz_{e} + w_{veio} -perdas$$