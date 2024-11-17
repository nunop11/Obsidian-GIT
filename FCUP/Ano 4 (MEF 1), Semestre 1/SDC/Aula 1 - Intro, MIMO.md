### Nota 
- O livro mais importante da bibliografia é o Ogata

# Matéria
- Vamos estudar:
    - sistema de malha aberta ou fechada
    - sistemas lineares
    - sistemas com tempo contínuo ou discreto
    - estudar sistemas no domínio do tempo (espaço de fase)
    - MIMO - Multiple Input Multiple Output

# Introduçãozita
## Malha aberta e fechada
- Consideremos que temos um motor que queremos controlar

**Malha aberta**
- Um controlador de malha aberta deste sistema seria:
![[sdc_1|1000]]
- Em que X será um certo input e Y será o output (no caso de um motor, a *velocidade de rotação*)
- OLC é "Open Loop Controller"
- Ora, um circuito destes tem que funcionar com uma lógica: fornecemos X volts e o motor roda a Y rpm.
    - Isto pode funcionar muito bem, mas implica que temos que conhecer esta relação e que ela tem de se comportar como previsto sempre.

**Malha Fechada**
![[sdc_2|1000]]
- Agora temos algo mais útil e que se consegue ajustar
- O fio que sai de Y e depois liga com sinal "-" à bola representa um sensor que deteta a velocidade de rotação atual do motor. Ou seja, o controlador ajusta o seu input conforme a evolução da velocidade do motor
- O sinal rodeado a azul é o *Sinal de Erro*: $Y_{ref}-Y$

## MIMO
- Um exemplo comum de um MIMO é um avião/drone:
![[sdc_3|1000]]

- Em que X inclui:
    - thrust
    - ailerons
    - rudder
    - elavator
- E em que Y inclui:
    - yaw, pitch, roll
    - velocidades angulares nas 3 direções
    - velocidade nas direções x,y,z
    - positção x,y,z

- Ou seja, neste exemplo simplificado temo 4 inputs e 12 outputs.
    - De notar aqui que não podemos estudar isto como uma séries de SISOs independentes. Se mudarmos o rudder, muda o yaw mas também mudam as velocidades porque viramos para o lado.
- Escrevemos este sistema assim:
$$U(t)=\begin{pmatrix}u_{1}(t) \\ u_{2}(t) \\ u_{3}(t) \\ u_{4}(t) \end{pmatrix}\quad ;\quad Y(t)=\begin{pmatrix}y_{1}(t) \\ y_{2}(t) \\ \vdots \\ y_{12}(t) \end{pmatrix}$$
Além disso, costumamos guardar os parâmetros atuais do sistema, que representamos como:
$$X(t) = \begin{pmatrix}x_{1}(t) \\ x_{2}(t) \\ \vdots \\ x_{n}(t) \end{pmatrix}$$
em que costumamos ter mais parâmetros atuais do que outputs. Ou seja, neste caso, $n\ge 12$

**Evolução**
- Sendo $X(t)$ os parâmetros atuais, facilmente vemos que a evolução do sistema é dada por
$$\dot{X}(t)=f(X(t),U(t)) ~~;~~X(0)=X_{0}~~,~~t\in[0,t_{f}]$$
- Num sistema linear, esta equação diferencial dá
$$\dot{X}=AX+BU$$

**Saída**
- Sendo $n$ maior que o número de saídas. Assim, $Y$ é um subset de $X$.
- Podemos escrever:
$$Y(t) = g(X(t),U(t))$$
