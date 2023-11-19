# 24- Rolamento
- Até agora, em plano inclinado, estudamos partículas a escorregar. Introduz-se agora partículas a rolar pelo plano inclinado.

### *Pure Roll*
- Tendo um corpo circular, com um ponto Q no seu centro. Verifica-se pure roll se após uma rotação do corpo, o ponto Q se desloco, na horizontal. uma distância $2\pi R$ , como representado abaixo
![[Pure Roll.png]]
- Acima estão ainda representadas $v_Q$, a velocidade do ponto Q, e $v_C$, a velocidade de um ponto na superfície do corpo em rolamento. Tem-se então que:
> $$\Large{v_Q=v_C=\omega R}$$

## Exemplo- Cilindro a rolar
- Calculemos então a aceleração de um cilindro de massa $M$, comprimento $\ell$ e raio $R$.
- Começemos por representar e dividir as forças, assim:
![[Rolamento em rampa.png]]
- Temos então representada a força gravítica, dividida nas suas duas componentes, a força de reação normal, assim como a força de atrito. Tem-se ainda representada a velocidade do ponto Q, ao centro.
- Conforme visto anteriormente:
$$v_Q=V_{circunferencia}=\omega R$$
e sabe-se que
$$a=\dot \omega R=\alpha R$$
- Podemos calcular o torque em Q:
    -  $N, F_g$ não têm efeito no torque, porque passam em Q
    - Logo, apenas $F_a$ tem efeito no torque, logo
$$\tau=RF_a=I_Q\alpha=I_Q.\frac{a}{R} \hspace{1cm} (1)$$
- Obtem-se então a primeira equação, com 2 incógnitas: $F_a$ e $a$
- Através do uso da 2ª Le de Newton, considerando as forças aplicadas no sentido da aceleração do cilindro (no sentido do movimento), podemos agora ver que:
$$Ma=Mgsen\beta-F_a \hspace{1cm}(2)$$
- E assim temos 2 equações com 2 incógnitas.
- Fazendo o cáculo matemático necessário, obtem-se que
$$a=\frac{MR^2gsen\beta}{MR^2+I_Q}$$

### Cilindro Sólido
- Para um cilindro sólido com distribuição de massa uniforme, tem-se que $I=\frac{1}{2}MR^2$
- Assim, fazendo os cálculos a partir da fórmula obtida anteriormente, obtem-se que 
$$a=\frac{2}{3}gsen\beta$$
- E assim se vê que a <ins>massa, raio e comprimento de um cilindro em rolamento não influenciam a sua aceleração.</ins>

### Cilindro oco
- Neste caso, tem-se que $I=MR^2$
- Assim, obtem-se que
$$a=\frac{1}{2}gsen\beta$$
- Vê-se assim que um *cilindro oco tem <ins>menos</ins> aceleração que um cilindro sólido*.
- Mas mais, uma vez, tendo dois cilindros ocos, a sua aceleração será sempre igual, independentemente da sua massa, comprimento e raio.

---
- Por fim, é dada uma série de exemplos muito contra-intuitivos sobre giróscopios.
---

#### Link do vídeo no Youtube:
https://youtu.be/XPUuF_dECVI

#### Índice dos resumos
[[MEC - INDEX]]

#mecanica #rolamento #fisica