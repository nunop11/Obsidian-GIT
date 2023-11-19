# 20- Momento angular e Torque
- Se uma partícula tem massa $m$ e velocidade $\vec v$, então terá momento linear $\vec p = m . \vec v$
![[intro a momento angular.png]]
- Tendo então um ponto Q. $\vec r_Q$ é o vetor posição da partícula relativamente a Q. Tem-se então o ângulo $\theta$, formado pelos vetores $\vec r_Q$ e $\vec v$.
- Tem-se assim que o vetor momento angular ($\vec L$), é dado por:
> $$\vec L_Q= \vec r_Q \times \vec p= m(\vec r_q \times v)$$
- Pela definição de módulo de produto vetorial tem-se ainda:
> $$|L_Q|=mv . r_Q sen\theta$$
 De notar nesta equação que $r_c sen\theta$ é a componente de $\vec r_Q$ perpendicular a $\vec v$, como mostrado aqui:
 ![[Componente de r perpendicular a p.png]] ($r_{\perp_c}==r_Q sen\theta$)
- Assim vê-se que o módulo e sentido do momento angular depende do ponto $Q$ de referência.
- Desta forma, $\vec p$ é algo intríseco a um corpo, $\vec L$ não



    - Tem-se 
    $$\vec L_Q= \vec r_Q \times \vec p$$
Ora, se derivar-mos isto:
$$\frac{d \vec L}{dt}_Q=\frac{d\vec r_Q}{dt}\times \vec p + \vec r_Q \times \frac{d \vec p}{dt}$$
- Sabe-se que $\frac{d\vec r_Q}{dt}= \vec v$, que é colinear a $\vec p$. Assim $\frac{d\vec r_Q}{dt}\times \vec p =0$
- Sabe-se ainda que $\frac{d \vec p}{dt}=\vec F$
- Desta forma,
> $$\frac{d \vec L}{dt}_Q = \vec r_Q \times \vec F = \tau$$
>  $\tau$ é o **Torque**
- Assim vê-se que, por exemplo, se tivermos um corpo em movimento circular uniforme. Relativamente a C, o centro da circunferência descrita, tem-se que $\vec L_C$ é diferente de 0 e constante. Por outro lado, o torque será nulo.

#### Exemplo: L num disco
- Vejamos o caso de um disco, como aquele estudado em [[19- Objetos em rotação, momento inercia]]:
![[particula i em disco a girar.png]]
- Temos um disco a rodar com $\omega$ constante. O seu centro é C. Estudemos uma dada partícula $i$, de massa $m_i$ e velocidade $\vec v_i$ . Assim, o módulo do seu momento angular relativamente a C será dado por:
$$L_{i_C}=m_i r_{i_C} v_i$$
- Fazendo a mesma troca que fizemos em [[19- Objetos em rotação, momento inercia]], como $v_i=\omega r_i$, então:
$$L_{i_C}=m_i r_{i_C}^2 \omega$$
- E como saber o momento angular relativo a C para TODO o disco? Assim:
> $$L_{disco}=\omega \sum m_i r_{i_C}^2= I_C \omega$$
> Desde que o corpo esteja a rodar em torno do seu centro de massa, esta relação verifica-se. Não é portanto preciso identificar o ponto C
- Sendo que $\frac{d\vec L}{dt}=\tau$, então, a partir da equação, tem-se:
$$\frac{d\vec L}{dt}=\frac{d}{dt}(I\omega) \leftrightarrow$$

> $$\leftrightarrow |\tau| = \alpha I$$

- São realizados diversos exemplos, práticos e experimentais sobre momento angular.

#### Link do vídeo no Youtube:
https://youtu.be/sNaaL19opxw

#### Índice dos resumos
[[MEC - INDEX]]

#mecanica #torque #fisica