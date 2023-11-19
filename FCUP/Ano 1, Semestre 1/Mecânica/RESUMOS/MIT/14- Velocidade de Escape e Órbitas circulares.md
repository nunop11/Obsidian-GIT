# 14- Velocidade de Escape e Órbitas circulares
### Velocidade de Escape
- Representada como $v_{esc}$
- Velocidade necessária para sair da zona de atração gravitacional da Terra.
-  Ora, vejamos como esta pode ser calculada:
    - A força mecânica de um corpo é dada por:
$$\begin{aligned}
E_m & =E_c+E_p \leftrightarrow \\
\leftrightarrow E_m & =\frac{1}{2}m v_{esc}^2-\frac{mM_T G}{R_T}
\end{aligned}$$
- Ora, se um certo corpo sair da zona de atração da Terra, passa a não ter Energia Potencial. Assim, como consideramos que existe conservação da energia mecânica, se $E_p$ passa a ser igual a 0, também $E_c$ terá de ser 0. Assim, obtem-se:
$$\begin{aligned}
0 &=\frac{1}{2}mv_{esc}^2 - \frac{mM_T G}{R_T} \leftrightarrow \\
\leftrightarrow v_{esc} &=\sqrt{\frac{2M_T G}{R_T}} \approx 11.2km/s\end{aligned}$$
- Esta energia tem de ser exato. Se for menor, nunca se sairá da atração da Terra. Se for maior, ter-se-á energia cinética extra após sair da atração da Terra.

### Órbitas Circulares
- Temos um certo corpo de massa $m$ numa órbita circular de raio $R$ (nota: este é o ==raio da órbita==, não o raio da Terra ou altura da órbita) em torno da Terra, com uma velocidade $v$, de módulo constante. Tem-se então que:
$$\begin{aligned}
F_g &= F_{centripeta} \leftrightarrow \\
\leftrightarrow \frac{mM_T G}{R^2} &= m \frac{v^2}{R} \leftrightarrow \\
\leftrightarrow v_{orb}&=\sqrt{\frac{M_T G}{R}}
\end{aligned}$$
> E assim se cácula a velocidade orbital do corpo em órbita circular ($\neq v_{esc}$ ). De notar que aqui basicamente se tem que Fg é igual à Força Centrípeta. Ora, a força centrípeta tem um valor igual a massa * aceleração. Essa aceleração pode ser obtida pela fórmula $a=\frac{v^2}{r}$.

- Sabe-se ainda que 
$$T=\frac{2\pi R}{v_{orb}}$$
- Substituindo-se a fórmula obtida acima:
$$T = \frac{2\pi \sqrt{R^3}}{\sqrt{GM_T}}$$
> NOTA: Estas 2 fórmulas aplicam-se não só ao caso de um corpo a orbitar um planeta, como se aplicam também ao caso de, por exemplo, a Terra a orbitar o Sol (num caso simplificado em que se considera a sua órbita como circular, claro)
> NOTA 2: Como se pode ver, a massa do objeto não influencia de forma nenhuma a sua velocidade ou período orbital

### Energia Total em Órbita

- Voltando à formula do ínicio:
$$E = \frac{1}{2}m v_{esc}^2-\frac{mM_T G}{R_T}$$
- Substituindo $v$ pela fórmula previamente obtida para $v_{orb}$ , obtem-se:
$$E= \frac{1}{2}m\frac{GM_T}{R_t}-\frac{mM_T G}{R_T}$$
- Tem-se então que:
$$E=\frac{1}{2}E_p=-E_c$$
> A seguir a isto aborda-se Potência, que não está no programa de Mecânica, mas como ainda escrevi as notas, aqui estão:
### Potência/*Power*
$$P=\frac{dW}{dt} [J/s \leftrightarrow Watt]$$
- Ora, o trabalho W, de uma força é dado por: $W=\vec F . \vec{dr}$, sendo que F é constante
- Ora:
$$P=\frac{d}{dt}(W)=\frac{d}{dt}(\vec F . \vec{dr})=\vec{F}\frac{d\vec{r}}{dt}$$
- Ou seja, tem-se que:
$$P= \vec{F} . \vec{v}$$

---
- São realizados diversos exercícios e xemplos acerca de Potência e Energia
---


#### Link do vídeo no Youtube:
https://youtu.be/3fTVn96gUSQ

#### Índice dos resumos
[[MEC - INDEX]]

#mecanica #fisica