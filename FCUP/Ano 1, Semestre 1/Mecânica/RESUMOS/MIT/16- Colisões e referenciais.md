# 16- Colisões e referenciais
- Colisão frontal: colisão que ocorre num só eixo, 1D
- Regra geral, numa colisão tem-se isto:
$$E_{c_{inicial}} + Q = E_{c_{final}}$$
, sendo $Q$ uma constante. Ora, 
    - Se $Q>0$, então há ganho de energia cinética e tem-se uma ==colisão superelástica==. Exemplo: explosão
    - Se $Q=0$, então há conservação de energia cinética e temse uma ==colisão elástica==
    - Se $Q<0$, então há perda de energia cinética e tem-se um ==colisão inelástica==

- Neste tipo de exercícios, a melhor estratégia é obter equações em função de $v_1, v_2, v_1^\prime, v_2^\prime$ , sendo que aquelas velocidades com a linha são as velocidades após a colisão. 

> NOTA: Ver a resolução do NdS do problema de aula da TP8

- É realizado um exemplo de colisões com medição de tempos

## Referencial do CM
- Tal como visto na aula anterior, se não houverem forças exteriores a atuar no sistema, existe conservação do momento linear. 
- Assim, podemos fazer uso do referencial do CM. Neste, tem-se que $P_{CM}=0$. Isto porque, como vimos na aula anterior, $P_{CM}=p_1+p_2+...+p_i$ e estes acabam por se anular. Este referencial pode parecer complicado, mas pode ser muito útil. [Este gif](https://qph.fs.quoracdn.net/main-qimg-e09b8a9f48cd72734dba580f2f48e2a4) pode ser muito útil para compreender este conceito.
- Assim, vejamos um exemplo prático:
![[Velocidades antes e depois de colisão.png]]
- Temos 2 martículas $m_1$ e $m_2$. Considere-se que $u_1, u_2$ são as velocidades das partículas antes da colisão e $u_1\prime, u_2^\prime$ as velocidades após a colisão, RELATIVAMENTE AO CM. Consideremos que esta é uma colisão elástica.

-  Conforme os dados, sabemos que existe conservação da energia cinética. Assim,
$$\frac{1}{2}m_1u_1^2+\frac{1}{2}m_2u_2^2=\frac{1}{2}m_1u_1^{\prime 2}+\frac{1}{2}m_2u_2^{\prime 2}$$
- Estudando este movimento com um referencial do CM, obtemos:
$$m_1u_1^\prime+m_2u_2^\prime=0$$
- Como dito antes,  $u_1, u_2$ e $u_1\prime, u_2^\prime$ são as velocidades das partículas relativamente ao CM. Para as calcular, faz-se assim:
$$\begin{aligned}
\vec u_1 &= \vec v_1 - \vec v_{CM} \\
\vec u_1^\prime &= \vec v_1^\prime - \vec v_{CM}
\end{aligned}$$
(e o mesmo para $v_2$ e $v_2^\prime$.)

### Referencial de Laboratório
- Este é o referencial "normal". Se tivermos feito os cálculos acerca de um movimento no referencial do CM e quisermos passar para ref do laboratório, precisamos de utilizar as fórmulas da posição e velocidade do CM calculadas na aula anterior, [[15 - Momento Linear, Conservação de p e CM]].

---
- São realizados exercícios teóricos e práticos sobre colisões para comparar a sua resolução usando referencial de laboratório e do CM.
---

#### Link do vídeo no Youtube:
https://youtu.be/-q-WiX-KVXo

#### Índice dos resumos
[[MEC - INDEX]]

#mecanica #colisoes #fisica
