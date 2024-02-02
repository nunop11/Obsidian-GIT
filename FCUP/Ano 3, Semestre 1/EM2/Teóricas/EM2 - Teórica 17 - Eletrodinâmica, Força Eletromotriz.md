# ELETRODINÂMICA :D
## Lei de Ohm :D
- Para fazer uma corrente fluir temos que "empurrar" as cargas. Ora, a velocidade a que a corrente se move para uma certa força aplicada $\vec{f}$ (por unidade de carga) vai depender das propriedades do material em que a corrente ocorre. Mais precisamente, depende da sua *condutividade* $\sigma$:
$$\vec{\mathcal{J}}=\sigma \vec{f}$$
- E podemos escrever a resistividade do material: $\rho=1/\sigma$ (não trocar com densidades volúmica e superficial de corrente)
- Evidentemente, condutores perfeitos teriam $\sigma=\infty,\rho=0$ e isoladores perfeitos têm $\sigma=0,\rho=\infty$.

- Iremos aqui considerar que a força que "empurra" as cargas é a Força EM AKA Força de Lorentz (novamente, por unidade de carga):
$$\vec{\mathcal{J}}=\sigma(\vec{E}+\vec{v}\times\vec{B})$$
na realidade temos que as carga em si movem-se relativamente devagar. Como tal, podemos anular o termo da velocidade:
$$\boxed{\vec{\mathcal{J}}=\sigma\vec{E}}$$
sendo esta a **Lei de Ohm**.

- No entanto parece que temos uma contradição: atrás dissemos que o campo elétrico dentro de um condutor é nulo. 
    - Ora, isso é para quando temos carga em repouso. Na equação acima esse não é o caso.
    - Além disso, devemos notar que se tivermos um condutor ideal ($\sigma=\infty$) temos que $\vec{E}=\vec{0}$ independentemente da corrente.

**Lei de Ohm - Forma mais comum**
![[lei de ohm condutor arbitrario.png]]
- Consideremos um condutor cilindrico com comprimento $\ell$ e com secção transversal de área $s$.
- A densidade de corrente será a corrente que passa na secção transversal: $\mathcal{J}=I/s$
- Mas vimos acima que $\mathcal{J}=\sigma E$. Ora, o campo num condutor será uniforme. Se a DDP entre os 2 lados do condutor for $V$ temos $E=V/\ell$.
- Fica $$\frac{I}{s}=\sigma E \to I=\frac{\sigma s}{\ell}V$$
em que podemos definir $\frac{1}{R}=\frac{\sigma s}{\ell}$ e temos:
$$V=RI$$
(em que $R$ é a resistência do condutor, medida em Ohm $\Omega=V/A$)

- Para correntes estáveis e uniformes podemos escrever:
$$\nabla \cdot \vec{E}=\frac{1}{\sigma} \nabla \cdot \vec{\mathcal{J}}=0$$
e a densidade de corrente terá que ser nula dentro do condutor. Isto é comparável ao caso de um material polarizado, no sentido que toda a densidade de carga está na superfície. De notar que neste caso o campo dentro do condutor não será necessariamente nulo. Desta forma, podemos aplicar a equação de Laplace.

- Ora, o trabalho gerado pela força que "arrasta" as cargas será
$$dW=Vdq$$
- Podemos escrever potência como trabalho por tempo, ou seja:
$$P= \frac{dW}{dt} = V \frac{dq}{dt}=VI=RI^{2}$$
para uma corrente estacionária, esta potência corresponde à potência dissipada pelo condutor na forma de calor. A esta equação chamamos **Lei de Joule**.

## Força Eletromotriz
- Consideremos um circuito simples, com uma pilha e uma lâmpada. Empiracamente facilmente se verifica que a corrente é igual em todo o percurso. No entanto, não seria de esperar que a corrente fosse mais intensa perto da pilha, porque apenas perto dela teriamos um força a "empurrar" as cargas?
- A resposta a isto é que a corrente _tem_ de se mover toda à mesma velocidade, senão teríamos acumulação de carga numa zona do circuito. Na prática é o campo elétrico que estabiliza a densidade de carga ao longo do circuito, sendo mais forte onde surgem densidades de carga excessivas. Assim, este sistema auto regula-se e ficamos com uma corrente e densidade de carga uniformes.

- Assim, temos 2 forças que "empurram" as cargas em circuitos. Por unidade de carga, temos:
$$\vec{f}=\vec{f_{f}}+\vec{E}$$
(sendo $\vec{f_f}$ a força gerada por unidade de carga pela fonte (pilha, motor, etc))

- Independentemente do mecanismo físico que gera a corrente, o efeito que a fonte tem sobre o circuito é:
$$\varepsilon\equiv\oint \vec{f}\cdot d \vec{\ell}=\oint \vec{f_{s}}\cdot d \vec{\ell}$$
em que $\varepsilon$ é a **força eletromotriz**. De notar que na realidade isto não é força nenhuma, mas sim trabalho.
- Numa fonte de corrente ideal temos $\sigma=\infty$. Logo, como $\vec{\mathcal{J}}=\sigma\vec{f}$ temos $\vec{f}=0$. Assim: $$\vec{E}=-\vec{f_{f}}$$
e a DDP entre os terminais da fonte será:
$$V=-\int_{a}^{b} \vec{E}\cdot d \vec{\ell}=\int_{a}^{b} \vec{f_{f}}\cdot d \vec{\ell}=\oint \vec{f_{f}}\cdot d \vec{\ell}=\varepsilon$$
(tornamos $\int_{a}^{b} \vec{f_{f}}\cdot d \vec{\ell}=\oint \vec{f_{f}}\cdot d \vec{\ell}$ porque fora da fonte temos $\vec{f_{f}}=\vec{0}$)
- Assim, num circuito com uma pilha, a função desta é manter uma certa DDP entre os seus terminais. Esta DDP gera um campo elétrico que causa uma corrente. O campo elétrico no resto do circuito encarrega-se de estabilizar a corrente.

### Força eletromotriz de movimento
- Quando movemos um fio através de um campo magnético, gera-se nele uma força eletromotriz e portanto uma corrente. Consideremos um sistema como o abaixo:
![[corrente a mover em campo B.png]]
- Neste caso em que $\vec{E}=\vec{0}$ temos a seguinte Força de Lorentz:
$$\vec{F}=q(\vec{E}+\vec{v}\times\vec{B})=q \vec{v}\times\vec{B}=q(v\hat{x})\times(-B\hat{z})=qvB\hat{y}\to \vec{f}_{lorentz}=vB\hat{y}$$
sendo $\vec{v}$ a velocidade com que todo o circuito se move para a direita.
- A força eletromotriz induzida ao longo da secção vertical será então:
$$\varepsilon=\int_{a}^{b}\vec{f}_{lorentz}\cdot d \vec{\ell}=\int_{a}^{b}vB\hat{y}\cdot dy\hat{y}=vB\int_{a}^{b}dy=vBh$$
de realçar que o circuito se está a mover para o lado, mas usamos $d\vec{\ell}$ para cima, perpendicular. Pode parecer estranho, mas isto acontece em todos os sistemas eletromagnéticos.
- De realçar ainda que, apesar de a força eletromotriz se gerar devido ao campo magnético, temos que este é perpendicular ao deslocamento e portanto *não faz trabalho*! Campo magnético nunca faz trabalho.

- Assim, sendo induzida a força eletromotriz, surge uma corrente. As cargas no fio começam-se a mover para cima. Por causa destas, aparece um 2º campo magnético. A força magnética por carga passa então a ser:
$$\vec{F}_{mag}=(\vec{v}+\vec{u})\times\vec{B}=(v\hat{x}+u\hat{y})\times(-B\hat{z}) =vB\hat{y}- uB\hat{x}$$
- Desta forma, é preciso aplicar uma força $\vec{f}_{ext}$ para anular o 2º termo do campo magnético. O trabalho dessa força será:
$$\int \vec{f}_{ext}\cdot d \vec{\ell}=\int u B \hat{x}\cdot (dx \hat{x}+dy \hat{y})=uB \Delta x=uBv \Delta t=uBv \frac{h}{u}=vBh=\varepsilon$$
ou seja, o trabalho realizado por carga pela força externa é igual à força eletromotriz.

**Fluxo**
- Consideremos o loop retangular acima. O Fluxo do campo magnético através dele é dado por:
$$\Phi=\int \vec{B}\cdot d \vec{s}=Bhx$$
- Ora, ao longo do tempo temos que o fluxo irá variar da forma:
$$\frac{d\Phi}{dt}=Bh \frac{dx}{dt}=-Bhv$$
ou seja, temos:
$$\boxed{\varepsilon=- \frac{d\Phi}{dt}}$$
- Esta lei verifica-se para:
    - loops não retangulares
    - loops a mover-se em qualquer direção
    - loops em campos não uniformes
    - loops com forma variável
(Ver página 307 do Griffiths para a demonstração)

- Apesar disso, é importante ter atenção à presença de interruptores, condutores, contactos que deslizam (em geral coisas que permitam percursos de corrente ambíguos).
- De notar também que à forças eletromotrizes que simplesmente não conseguimos calcular com esta lei (Disco de Faraday).
- Outro caso muito dificil de calcular é correntes parasita / correntes de Foucalt / eddy currents - correntes que surgem no interior de condutores quando expostos a campos magnéticos variáveis.