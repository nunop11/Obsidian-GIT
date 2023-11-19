# 15 - Momento Linear, Conservação de p e CM
> $$\vec p = m . \vec v$$
- É um vetor e as suas unidades são $kg\frac{m}{s}$
-  Têm-se ainda que:
$$\vec F= m \vec a=m\frac{d \vec v}{dt}=\frac{d(m \vec v)}{dt}$$
, logo:
> $$\vec F = \frac{d}{dt} \vec p$$

### Caso geral
![[Forças internas em sistema.png]]
- Imaginemos que temos 2 partículas num certo sistema. Consideremos que cada uma está a ser atuada por uma força exterior (a cor de rosa). No entanto, verifica-se que, cada uma das partículas faz com que na outra seja atuada uma força ($F_{ji}$ -  força atuada em J por causa de i). No entanto, pela 3ª lei de Newton, todas as paartículas serão atuadas por uma força de igual modo áquela que elas causam. Estas são as forças Internas (a amarelo).

- Assim, com tantas forças envolvidas, como é que podemos saver o momento linear total de um sistema com $n$ sistema?
- Ora, temos:
$$\begin{aligned}
\vec p_{total} &= \vec p_1 + \vec p_2 + ...+\vec p_i+... \leftrightarrow \\
\leftrightarrow \frac{d \vec p_{total}}{dt} &= \vec F_1 + \vec F_2 +...+\vec F_i +... \leftrightarrow \\
    \leftrightarrow \frac{d \vec p_{total}}{dt} &= \vec F_{total}
\end{aligned}$$
- No entanto, como, tal como se prevê, todas as forças internas se anulam (3ª Lei de Newton: Esta lei declara que estas forças têm de existir, mas também declara que se anulam). Deste modo, tem-se:

> $$\frac{d \vec p_{total}}{dt} = \vec F_{total_{ext}}$$

### Conservação de momento linear
- Como acabamos de ver, a derivada do momento linear é igual ao total das forças externas. Ora, sempre que num exercício se podem desprezar as forças externas, considera-se que **o momento é conservado**.

### Exemplos e Colisões
- É realizado um exemplo de uma colisão perfeitamente inelástica (ver [[16- Colisões e referenciais]]). Ao fazer este exemplo, verifica-se que a energia cinética do sistema é diminuida, mas não o momento. Desde que não existam forças exteriores, nada consegue alterar o momento.
- Se tiver num exercício, uma colisão perfeitamente inelástica em 2D e quiser saber em que direção será a velocidade após a colisão, preciso de me lembrar que o módulo E vetor do momento linear total do sistema são conservados. Assim, a velocidade após colisão terá a mesma direção do momento linear após colisão. 
- É realizado um exemplo teórico e prático de 2 carrinhos a moverem-se com a uma mola a prendê-los.

### Centro de Massa
- Tendo um sistema com n partículas, tem-se:
$$M_{total}.\vec r_{CM} = \sum_{i=1}^n m_i \vec r_i$$
- Logo, obtem-se:
> $$\vec r_{CM}= \frac{ \sum_{i=1}^n m_i \vec r_i}{M_{total}}$$

- Ao derivar isto em função ao tempo, obtem-se:
> $$\vec v_{CM} = \frac{1}{M_{total}}.\sum_{i=1}^n m_i \vec v_i$$

, ou seja, tem-se:
 $$\vec v_{CM} = \frac{1}{M_{total}}.\vec P_{total}$$
 - Assim, tem-se:
 > $$\vec P_{total}=M_{total}.\vec v_{CM}$$
     > - Isto é verificado pelo facto de que se derivarmos esta equação em função ao tempo obtemos $F=ma$ 

#### Link do vídeo no Youtube:
https://youtu.be/aIhScO3_I50

#### Índice dos resumos
[[MEC - INDEX]]

#mecanica #momento_linear #fisica