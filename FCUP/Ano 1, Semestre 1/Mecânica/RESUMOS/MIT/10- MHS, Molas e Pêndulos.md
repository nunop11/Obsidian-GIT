# 10- MHS, Molas e Pêndulos
- Tendo uma mola. Ela tem um certo comprimento relaxado. O ponto onde se encontra a sua extremidade neste caso é o **ponto de quilíbrio**. No entanto, se a mola for estcada ou comprimida, haverá um deslocamento da sua extremidade em relaçao ao ponto de equilibrio.
- Mal seja realizado um tal deslocamento da extremidade da mola, gera-se uma força que pretende mover este ponto para o local do ponto de equilíbrio. Assim, esta força $F_e$ é proporcional aos deslocamento em relação ao ponto de equilibrio (**Lei de Hooke**) e tem-se:
$$F_e=-kx$$
(sendo $k$ a constante da mola)

![[mola com massa em equilibrio.png]]
- No entanto, se a mola estiver vertical e na sua extremidade existir uma massa, é importante perceber que o ponto se equilibrio é o *ponto em que $F_e$ e $mg$ são iguais*
![[mola com e sem lei de hooke.png]]
- Ao traçar um gráfico a relacionar a Força $F$ aplicada com o comprimento da mola, $x$:
    - Se se verificar que ao longo do "esticamento" da mola a relação $F(x)$ apresenta uma linah reta, a Lei de Hooke verifica-se e a mola mantem o seu cumprimento original após esticada
    - Se não esse o caso, e na relação $F(x)$ se vir uma curva do género das curvas cor de rosa representadas acima, quer dizer que a Lei de Hooke não se aplicou. Ou seja, a mola foi esticada de tal forma que se deformou permanentemente.

![[bloco a deslizar preso a mola.png]]
- Se tivermos este problema, com uma massa presa a uma mola numa superfície sem atrito, temos as forças representadas acima.
- Após estudo do movimento conclui-se que o período da oscilação é dado por:
$$T=2\pi \sqrt{\frac{m}{k}}$$
    - Assim, conclui-se que, desde que se aplique a Lei de Hooke, a posição original da massa não influencia o período. Quer a massa comece muito perto ou muito longe da posição de equilibrio, o período de oscilação será o mesmo.
- Aplicando a 2ª Lei de Newton obtem-se:
$$\begin{aligned}
ma &= -kx \\
m\ddot x + kx &=0 \\
-->>\ddot x + \frac{k}{m}x &=0 <<--
\end{aligned}$$
#### Estudo da equação acima
- Para estudar a equação acima, temos que começar por obter a função de x(t) e só depois se pode considerar a sua 2ª derivada.
- Ao estudar a posição $x$ de um ponto num movimento em função ao tempo obtem-se um gráfico de uma função periódica, e assim obtem-se:
$$x(t)=A cos(\omega t + \phi)$$
>Nesta equção, o uso de cos() ou sen() é indiferente
- Neste gráfico tem-se:
    - $A$ --> Amplitude da oscilção (deslocamento máximo da extremidade da mola) 
    - $\omega$ --> Frequência angular (em $rad/s$) (não confundir com vel. angular).
    - $\phi$ --> *phase angle*
- Conclui-se ainda que:
    - $T=\frac{2\pi}{\omega}$, uma vez que se cococar este valor na equação acima, o ângulo irá aumentar $2\pi$ e portanto passou uma oscilação, ou seja, 1 período

- Assim, como já temos $x(t)$, pode-se facilmente obter:
$$\begin{aligned}
\dot x= -A\omega sen(\omega t + \phi) && logo: \\
\ddot x = -A\omega^2cos(\omega t + \phi) && logo: \\
\ddot x = -\omega^2 x
\end{aligned}$$
- Assim, substituindo na equação que estamos a estudar, obtem-se:
$$-\omega^2x + \frac{k}{m}x=0$$
- Isto tem de se verificar, sempre. E portanto, obrigatoriamente tem-se:
$$\omega = \sqrt{\frac{k}{m}}$$
- E assim, 
$$T = \frac{2\pi}{\omega}$$
- Assim, após este estudo, conclui-se que $A$ e $\phi$, da fórmula de $x(t)$, não influenciam o período, mas em vez disso são algo dependente da situação inicial do problema. É feito um exemplo teórico que demonstra isto.
- É resolvido um exercício prático e experimental que mostra o cáculo da oscilação.
- É resolvido um caso teórico de um pêndulo oscilatório. Este caso é depois realizado de forma experimental. Não tirei notas mas pode ser útil.

#### Link do vídeo no Youtube:
https://youtu.be/tNpuTx7UQbw

#### Índice dos resumos
[[MEC - INDEX]]

#mecanica #molas #harmonico #fisica