# 19- Objetos em rotação, momento inercia

| Translação | Rotação  |
| ---------- | -------- |
| $m$        | $I$      |
| $x$        | $\theta$ |
| $v$        | $\omega$ |
| $a$        | $\alpha$ |


![[movimento circular.png]]
- Aqui temos um corpo em rotação. Descreve um percurso circular de raio $R$ e move-se com uma velocidade $v$ e com uma velocidade angular $\omega$. Temos ainda o ângulo $\theta$ que o cropo descreve num certo intervalo de tempo e a rosa a direção que o vetor velocidade terá após esse intervalo.
- Consideremos agora que o movimento não é uniforme. Ou seja, se temos:
$$v =\omega R = \dot \theta R$$
Então, após derivação da equação acima, obtemos:
$$a_{tan}=\dot \omega R= \ddot \theta R = \alpha R$$
- $\alpha$ é a **aceleração angular**. Esta é tangencial, pelo que não altera a trajetória circular. (isso seria a aceleração normal, ==não confundir!!==)
- Assim, podemos adaptar as equações estudadas no movimento 1D, fazendo estas trocas:
$$\begin{aligned}
x \rightarrow \theta \\
v \rightarrow \omega \\
a \rightarrow \alpha \\
\end{aligned}$$
- Assim obtem-se:
$$\begin{align}
\theta(t)&=\theta_0+\omega_0t+\frac{1}{2}\alpha t^2 \\
\omega(t) &=\omega_0+\alpha t
\end{align}
$$
### Energia cinética de rotação
- Tendo um disco de massa $m$, a rodar com velocidade angular $\omega$, com raio $R$. Este está a rodar em torno de um ponto C, centro de rotação.

- Assim, consideramos um ponto do disco, com massa $m_i$, que está a uma distância $r_i$ do centro de rotação C. Desta forma, a $E_c$ deste ponot é dada por $E_{c_i}=\frac{1}{2}m_i v_i^2$
    - Tendo que $v=\omega r$, da fórmula anterior tira-se: 
>$$E_{c_i}=\frac{1}{2}m_i \omega^2 r_1^2$$
Faz-se esta troca porque a velocidade tangencial do ponto escolhido será muito reduzida se o ponto estiver perto de C e muito elevaada se o ponto estiver muito longe de C. Da maneira que reformulamos a equação, $\omega$ é constante e $r_i$ muda de forma mais fácil de determinar.

- Mas como se obtem a energia cinética de todo o disco? A partir da fórmula anterior percebe-se que é assim:
$$E_{c_{disco}}=\frac{\omega^2}{2} \sum m_i r_i^2$$
### Momento de Inércia (I)
Da fórmula anterior obtem-se o momento de inércia, $I$, que é dado por:
$$I = \sum m_i r_i^2$$
- Alterando mais uma vez a fórmula anterior, obtem-se que: $$E_{c_{disco}}=\frac{1}{2} I_c \omega^2$$
- Acresta-se então à lista feita anteriormente (de passagem de movimento linear para circular) que:
$$m \rightarrow I$$
- O momento de inércia depende da forma do objeto em rotação, assim como do seu eixo de rotação.
- Para calculá-lo, ir ao final do exercício. Also, existem tabelas online.
- Vejamos alguns teoremas que permitem calcular:
### Teorema do Eixo Paralelo
![[teorema dos eixos paralelos.png]]
- Imagine-se que temos um disco de centro de massa $C$ a giral em torno de um eixo $l$. Imagine-se agora que vamos forçá-lo a girar em torno de um eixo $l^\prime$, a uma distância $d$ de $l$. Então:
$$se\hspace{5mm} l^\prime \parallel l \hspace{5mm} ,entao \hspace{5mm} I_{l^\prime}=I_l+md^2$$
### Teorema do Eixo Perpendicular
- Só se aplica se tivermos um objeto muito fino!
![[teorema dos eixos perpendiculares.png]]
- Imagine-se que temos um objeto irregular. Ele pode ser rodado por um eixo $x$, $y$ ou $z$, sendo que $z=x \times y$ 
- Nesse caso, tem-se: 
$$se\hspace{5mm} \vec z= \vec x \times \vec y \hspace{5mm} ,entao \hspace{5mm}I_z=I_x+I_y$$

---
- É executado um exemplo sobre o funcionamento de uma *flywheel*
- É estudado ainda o exemplo de momento de inércia da Terra e do Sol
- É por fim falado de estrelas de neutrons
---

#### Link do vídeo no Youtube:
https://youtu.be/fDJeVR0o__w

#### Índice dos resumos
[[MEC - INDEX]]

#mecanica #inercia #fisica