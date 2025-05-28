- Passo a passo de como se programou o braço SCARA porque já não me lembrava de nada

### 1 - Cinemática direta
- Temos que:
$$\begin{cases}
x = a_{1}\cos\theta_{1} + a_{2}\cos(\theta_{1}+\theta_{2}) \\
y = a_{1}\sin\theta_{1} + a_{2}\cos(\theta_{1}+\theta_{2})
\end{cases}$$
Dando ao robot 2 ângulos, conseguimos prever a posição (x,y). 

### 1.1 - DH
- Outra alternativa para fazer cinemática direta (completo overkill para um robot tão simples) é usar DH. Permite ter uma convenção mais "geral" e automática.
- Numa TP obtivemos esta tabela do diagrama de eixos do robot SCARA:

|     | $\theta$         | $d$         | $a$     | $\alpha$ |
| --- | ---------------- | ----------- | ------- | -------- |
| 1   | $\theta_{1}^{*}$ | 0           | $a_{1}$ | 0        |
| 2   | $\theta_{2}^{*}$ | 0           | $a_2$   | 180      |
| 3   | 0                | $d_{3}^{*}$ | 0       | 0        |
- Usando a função `DHMat` fornecida pelo prof conseguimos obter uma matriz DH a partir dos valores de $\theta,d,a,\alpha$. Ou seja, para cada linha/motor temos uma matriz 4x4.
    - Por exemplo, a matriz do motor 1 é obtida com: `DHMat(theta_1, 0, a_1, 0)`

- Queremos saber $x,y$ para um certo $\theta_{1}^{*},\theta_{2}^{*}$. Criamos então a função `DK3DH`, que faz cinemática direta com DH. Para isso, calculamos a matriz de cada linha e fazemos: $$T=A_{1} \times A_{2} \times A_{3}$$
A posição da ponta é dada por: $$x= T_{14} ~~~~,~~~~ y=T_{24}~~~~,~~~~ z=T_{34}$$
(as posições são os valores da última coluna da matriz)


### 2 - Cinemática inversa
![[scara-cine-inversa]]
- Agora, temos um ponto $(x,y)$ e queremos saber os ângulos $(\theta_{1},\theta_{2})$ associados a ele. 
- Começamos por definir: $\ell=\sqrt{x^{2}+y^{2}}$

##### $\theta_{2}$
- Tenhamos em conta isto. Temos o triângulo central, de lados $\ell,a_{1},a_{2}$. Pela lei dos cossenos:
$$\ell^{2}=a_{1}^{2}+a_{2}^{2}-2a_{1}a_{2}\cos\theta_{2}' ~~\to~~ \theta_{2}' = \arccos \left( \frac{-\ell^{2}+a_{1}^{2}+a_{2}^{2}}{2a_{1}a_{2}}\right)$$
e, obviamente:
$$\theta_{2}=\pi-\theta_{2}'$$

##### $\theta_{1}$
- Considerando $\theta_{1}''=\theta_{1}+\theta_{1}'$ temos:
$$\theta_{1}''=\arctan\left(\frac{y}{x}\right)$$
- Olhamos agora para o triângulo "de cima", que vai da origem ao ângulo reto no fundo. Este terá lados $\ell,a_{2}\sin\theta_{2},a_{1}+a_{2}\cos\theta_{2}$. Assim:
$$\theta_{1}'=\arctan\left(\frac{a_{2}\sin\theta_{2}}{a_{1}+a_{2}\cos\theta_{2}}\right)$$
e, claro:
$$\theta_{1}=\theta_{1}''-\theta_{1}'$$

##### Conclusão
$$\begin{align*}\\
\ell&= \sqrt{x^{2}+y^{2}}\\
\theta_{2}&= \pi- \arccos \left( \frac{-\ell^{2}+a_{1}^{2}+a_{2}^{2}}{2a_{1}a_{2}}\right)\\
\theta_{1}&= \arctan\left(\frac{y}{x}\right) - \arctan\left(\frac{a_{2}\sin\theta_{2}}{a_{1}+a_{2}\cos\theta_{2}}\right)
\end{align*}$$

### 3 - Jacobiano
- As 2 partes anteriores permitem fazer a parte "inicial" do braço: controlar diretamente onde ele vai. 
- O próximo objetivo consiste em seguir traçados ao **controlar a velocidade do motor**. Para isso usamos o jacobiano!
- Começamos por definir a posição da ponta:
$$\begin{cases}
x=p_{x}=a_{1}\cos\theta_{1} + a_{2}\cos(\theta_{1}+\theta_{2}) \\
y=p_{y}=a_{1}\sin\theta_{1} + a_{2}\sin(\theta_{1}+\theta_{2}) \\
z=p_{z}=0
\end{cases} ~~~~\to~~~~ \vec{p} = \begin{pmatrix}p_{x} \\ p_{y} \\ p_{z}\end{pmatrix}$$
- Vemos que a rotação que os 2 motores geram é o mesmo que 1 rotação em torno de $z_{0}$:
$$\gamma=\begin{pmatrix}\phi \\ \theta \\ \psi\end{pmatrix}=\begin{pmatrix}\theta_{1}+\theta_{2} \\ 0 \\ 0\end{pmatrix}$$
- Vimos em teoricas que o movimento do braço é definido por uma posição $\vec{p}$  e um set de angulos $\gamma$. Assim, definimos a *velocidade da ponta do braço*:
$$\begin{align*}
\dot{\vec{x}}&= \begin{pmatrix}\dot{\vec{p}} \\ \dot{\gamma}\end{pmatrix}= \begin{pmatrix}\frac{\partial \vec{p}}{\partial \theta_{1}}  & \frac{\partial \vec{p}}{\partial \theta_{2}} \\ \frac{\partial \gamma}{\partial \theta_{1}} & \frac{\partial \gamma}{\partial \theta_{2}}\end{pmatrix}=\begin{pmatrix}\frac{\partial p_{x}}{\partial \theta_{1}} & \frac{\partial p_{x}}{\partial \theta_{2}}\\
\frac{\partial p_{y}}{\partial \theta_{1}} & \frac{\partial p_{y}}{\partial \theta_{2}}\\
\frac{\partial p_{z}}{\partial \theta_{1}} & \frac{\partial p_{z}}{\partial \theta_{2}}\\
\frac{\partial \gamma_{1}}{\partial \theta_{1}} & \frac{\partial \gamma_{1}}{\partial \theta_{2}}\\
\vdots & \vdots\end{pmatrix}\\\\
&= \begin{pmatrix}-a_{1}\sin\theta_{1} - a_{2}\sin(\theta_{1}+\theta_{2}) & -a_{2}\sin(\theta_{1}+\theta_{2})\\
a_{1}\cos\theta_{1}+a_{2}\cos(\theta_{1}+\theta_{2})  & a_{2}\sin(\theta_{1}+\theta_{2})\\
0 & 0\\
1 & 1\\
0 & 0\\
0 & 0\end{pmatrix}\begin{pmatrix}\dot{ \theta_{1}} & 0\\
0 & \dot{\theta_{2}}\end{pmatrix}
\end{align*}$$
 
- E ficamos então com isto na forma:
$$\dot{\vec{x}}=J \dot{\vec{q}}$$
em que $\vec{\dot{q}}$ é as *velocidades na articulação*, ou seja, a velocidade de variação dos ângulos e atuadores prismaticos.

- Considerando que apenas vamos querer controlar $x,y$ e $\dot{x},\dot{y}$, podemos reduzir os parâmetros acima apenas para $p_{x},p_{y}$ e fica:

$$\dot{\vec{x}}=\begin{pmatrix}\dot{p_{x}} \\ \dot{p_{y}}\end{pmatrix}= \begin{pmatrix}\frac{\partial p_{x}}{\partial \theta_{1}} & \frac{\partial p_{x}}{\partial \theta_{2}}\\\frac{\partial p_{y}}{\partial \theta_{1}} & \frac{\partial p_{y}}{\partial \theta_{2}}\end{pmatrix}=\begin{pmatrix} - a_1 \sin(\theta_1) - a_2 \sin(\theta_1 + \theta_2) & - a_2 \sin(\theta_1 + \theta_{2}) \\ a_1 \cos(\theta_1) + a_2 \cos(\theta_1 + \theta_2) & a_2 \cos(\theta_1 + \theta_{2)}\end{pmatrix}\begin{pmatrix}\omega_{1} & 0 \\ 0 & \omega_{2}\end{pmatrix}$$

e temos o Jacobiano que aplicamos no simulador:
$$J = \begin{bmatrix}
- a_1 \sin(\theta_1) - a_2 \sin(\theta_1 + \theta_2) & - a_2 \sin(\theta_1 + \theta_2) \\
a_1 \cos(\theta_1) + a_2 \cos(\theta_1 + \theta_2) & a_2 \cos(\theta_1 + \theta_2)
\end{bmatrix}$$

##### Aplicar
- Consideremos que num certo modo (Linha ou Circulo) queremos ter uma velocidade $\vec{v}=(v_{x},v_{y})$. 
- Definimos o vetor $V=\vec{v}$, que tem shape 2x1
- Calculamos o jacobiano $J$ para os ângulos $\theta_{1},\theta_{2}$ em que os motores estão no momento atual
- Obtemos as velocidades das articulações ao fazer:
$$W = J^{-1}V$$
e temos as velocidades no vetor $W$, com shape 2x1.
- Assim, teremos $\dot{\theta_{1}}=\omega_{1}=W_{1}~~,~~\dot{\theta_{2}}=\omega_{2}=W_{2}$. Estes valores podem ser colocados diretamente no simulador.

### 4 - Linha e círculo
- Fizemos as contas para cada um destes modos, conforme apontado no caderno
- Penso que, tendo o jacobiano e o DH feito, esta parte tem a mesma implementação para qualquer configuração do braço, porque as equações apenas nos dão $\vec{v}$.