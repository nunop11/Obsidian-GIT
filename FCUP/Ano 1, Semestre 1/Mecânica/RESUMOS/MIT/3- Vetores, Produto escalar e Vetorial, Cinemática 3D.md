# 3- Vetores, Produto escalar e Vetorial, Cinemática 3D
![[modelo de vetor.png]]
*Modelo de vetor. Se estiver virado para nós é um ponto, se estiver virado para trás é uma cruz*

## Soma de Vetores
- Podemos aplicar a regra do paralelogramo ou do triângulo:
![[Attachments/FCUP/A1S1/Mecânica/soma de vetores.png]]
- Ao fazer a subtração de vetores, por exemplo $\vec{A} - \vec{B}$ , faz-se simplesmente a soma de $\vec{A}$ com o o "simétrico" de $\vec{B}$, ou seja: $$\vec{A} - \vec{B} = \vec{A} + (-\vec{B})$$
- Graficamente, o "simétrico" de um vetor corresponde a esse vetor rodado 180 graus.

## Vetores Unitários
- Vetores unitários são vetores que têm o sentido e direção dos eixos considerados e módulo igual a 1. Representa-se pela letra do eixo com um acento circunflexo: $\hat{x}, \hat{y}, \hat{z}$.
- Por exemplo, se tivermos um ponto $A(1,4,-3)$ no sistema $(x,y,z)$, pode ser representado, usando os vetores unitários por: $$A = \hat{x} + 4\hat{y} -3\hat{z}$$
## Multiplicação de Vetores
- Enquanto que a soma de vetores pode ser simples e muito fácil de visualizar, a multiplicação destes pode ser mais complicada, apresentando dois tipos diferentes:

### Produto Escalar (.)
- Este produto é representado por um "$\cdot$"
- Este produto de vetores, como o nome indica, resulta num escalar. Tendo os vetores $A(x_A, y_A, z_A)$ e $B(x_B, y_B, z_B)$ e  sendo $\theta$ o ângulo entre estes. O produto escalar pode ser obtido assim:
    $$A \cdot B = x_A x_B + y_A y_B + z_A z_B$$
ou assim:
$$A \cdot B = |A||B|cos\theta$$
- Ambas estas fórmulas são válidas e muitas vezes o importante é saber qual é a melhor para um certo contexto. Por vezes pode ser necessário associar as duas fórmulas, por exemplo, para determinar o ângulo *theta* entre os vetores.
- Ao ver a segunda fórmula, conclui-se que se os vetores são **perpendiculares**, o produto escalar é **zero**. 

### Produto vetorial (x)
- Este produto é representado por um "$\times$" .
- Este produto de vetores, resulta num terceiro vetor. Tendo os vetores $A(x_A, y_A, z_A)$ e $B(x_B, y_B, z_B)$ e  sendo $\theta$ o ângulo entre estes. O produto vetorial pode ser obtido assim:
    

$$
A \times B = 
\begin{vmatrix}
\hat{x} & \hat{y} & \hat{z} \\ 
x_A & y_A & z_A \\ 
x_B & y_B & z_B
\end{vmatrix}
= (y_A z_B - z_A y_B)\hat{x} +(z_A x_B - x_A z_B)\hat{y} +(x_A y_B - y_A x_B)\hat{z}
$$
ou assim:
$$\vec{C} = {A} \times {B} = |A||B|sen \theta $$
>A seguir a calcular $\vec{C}$ com a segunda equação, podemos saber o seu sentido pensando assim: Como $\vec{C} = {A} \times {B}$ , pegamos no vetor $A$ e rodá-mo-lo no sentido do menor ângulo entre $A$ e $B$, até este chegar a $B$. 
Aí imagina-se um parafuso ou uma tampa de garrafa. O sentido de $\vec{C}$ é o mesmo com que o parafuso se moveria se o rodássemos no mesmo sentido que rodámos $A$.
Outra maneira de visualizar isto é a regra da mão direita:
![[regra mão direita.png]]
(nota: a seta roxa representa $A \times B$ ; o "$\times$" pode não ser visível no modo escuro do Obsidian)

>Nota: Em inglês, o produto vetorial é frequentemente chamado de *cross product*.

## Equações gerais de um ponto em função ao tempo
- Temos um ponto $P$, representado pelo vetor $r_t$ , que varia com o tempo, $t$ .
- Assim, tem-se, para este movimento:
$$r_t = x_t \hat{x} + y_t \hat{y} + z_t \hat{z}$$
Assim, usando as fórmulas e relações determinadas em [[2- Cinemática 1D, Velocidade e Aceleração]], obtem-se:
$$v_t = \frac{d r_t}{dt} = \frac{dx_t}{dt}\hat{x} + \frac{dy_t}{dt}\hat{y} + \frac{dz_t}{dt}\hat{z} = \dot{x_t}\hat{x} + \dot{y_t}\hat{y}+\dot{z_t}\hat{z}$$
> Na última parte da equação anterior usa-se a notação de Newton. Basicamente $\dot{x} = \frac{dx}{dx}$. Esta notação pode ser usada quando a variável sobre a qual estamos a derivar $x$ é fixa (neste caso, é o tempo, $t$)

- Obtem-se ainda que:
$$a_t = \frac{d^2x}{dt}= \ddot{x_t}\hat{x} + \ddot{y_t}\hat{y} + \ddot{z_t}\hat{z}$$
> Para explicar isto, na palestra no youtube foi realizado um exemplo de lançamento de projétil.

#### Link do vídeo no Youtube:
https://youtu.be/0na1JdPE_JY

#### Índice dos resumos
[[MEC - INDEX]]

#mecanica #vetores #fisica