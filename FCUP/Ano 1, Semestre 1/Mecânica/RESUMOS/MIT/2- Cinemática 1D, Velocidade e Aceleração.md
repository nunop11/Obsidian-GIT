# 2- Cinemática 1D

### Velocidade média
- Cálculo da velocidade média de um corpo no intervalo $[a, b]s$ :
 $$
 \begin{align}
 \overline{v}_{t_a t_b} = \frac{x_b - x_a}{b-a} &&&& logo, &&&& \overline{v} = \frac{\Delta x}{\Delta t}
 \end{align}
 $$

    - É importante recordar que uma *velocidade média* é precisamente isso: uma velocidade calculada usando dois pontos e que define uma velocidade média nesse intervalo, não representando portanto o movimento no intervalo em si. Por exemplo, se um movimento partir de x=1 e acabar em x=1, a velocidade média será 0, independentemente do movimento realizado.

### Velocidade instantânea
- Se calcularmos a velocidade média entre dois pontos, enquanto vamos aproximando os pontos, temos:
$$lim_{\Delta t \rightarrow 0}=\frac{x_{t + \Delta t} - x_t}{\Delta t} = \frac{dx}{dt}$$
- Ou seja, a velocidade instantânea é a **primeira derivada de x(t)**, que pode portanto ser positiva (corpo move-se no sentido positivo), negativa (corpo move-se no sentido negativo) ou nula (corpo está em repouso).



### Aceleração média
- Cálculo da aceleração média de um corpo no intervalo $[a, b]s$ :


 $$
 \begin{align}
 \overline{a}_{t_a t_b} = \frac{v_b - v_a}{b-a} &&&& logo, &&&& \overline{a} = \frac{\Delta v}{\Delta t}
 \end{align}
 $$

> Nota: $\overline{v}$  e  $\overline{a}$  dependem de $\Delta x$ e de $\Delta v$, respetivamente. Logo, dependem dos referenciais definidos e consequentes sinais.

### Velocidade instantânea
- Se calcularmos a aceleração média entre dois pontos, enquanto vamos aproximando os pontos, temos:
$$lim_{\Delta t \rightarrow 0}=\frac{v_{t + \Delta t} - v_t}{\Delta t} = \frac{dv}{dt} = \frac{d^2 x}{dt^2}$$
- Ou seja, a aceleração instantânea é a **primeira derivada de v(t)** e portanto, é a **segunda derivada de x(t)**, que pode então ser positiva (corpo está a ganhar velocidade), negativa (corpo está a perder velocidade) ou nula (corpo move-se com velocidade constante ou está em repouso).

### Traçar e interpretar gráficos com esta informação
- Usando as informações dadas pelas equações de x(t), v(t) e a(t), pode-se traçar gráficos posição-tempo ou velocidade-tempo. Isto é possíve pois, por serem as derivadas umas das outras; num dado ponto, o valor de $v$ vai indicar o declive da reta tangente ao gráfico de $x$ e o valor de $a$ indica a sua concavidade. A partir destas relações, pode-se tirar conclusões sobre o movimento; por exemplo, quando é que a partícula está em repouso, quando é que está em movimento acelerado ou retardado, etc
- Este tipo de estudo pode ser feito no sentido inverso. Ou seja, se nos for dado um gráfico de posição, velocidade ou aceleração, podemos tirar conclusões acerca dos outros e por vezes até determinar as equações.

> Nota: No vídeo desta palestra são feitos vários exemplos práticos em que se aplica esta matéria.

#### Link da palestra no Youtube:
https://youtu.be/q9IWoQ199_o

#mecanica #fisica 