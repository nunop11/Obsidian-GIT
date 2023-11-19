# Eletro 1 - Aula teórica 18 (JAM)
## Dielétricos
- Temos um meio dielétrico, sem carga, coberto por cima e por baixo com condutores que têm carga positiva e negativa:
![[dieletrico 1]]
- Tal como vimos na aula T16 a capacidade de um condensador no vácuo é:
$$C_0=\varepsilon_0\frac{S}{d}=\frac{Q}{\Delta V}$$
- Mas temos que ao compará-la à capaciade de um condensador em que o meio não é o vácuo, $C$, vemos que $C=\varepsilon_rC_0$ e então:
$$\Large\varepsilon_r=\frac{C}{C_0}\quad,\quad\varepsilon_r>0$$
- Esta constante, $\varepsilon_r$ é a **constante dielétrica** ou a permitividade relativa.

### Átomos
- Temos que, num átomo, existe carga positiva no núcleo e negativa na nuvem eletrónica. 
- E normalmente, os centros de carga positiva e negativa coincidem.
- Mas, em campos elétricos pode haver um desvio. O campo mode mover o núcleo ou mover eletrões suficientes de forma que se altere o centro de carga negativa. E assim passa a haver uma distância $\delta$, muitíssimo reduzida, entre os 2 centros de carga.
- E então, com 2 centro de carga com sinal oposto a uma distância $\delta$, é gerado um **dipolo elétrico**, em que $p=q\delta$
- De notar que nesta parte da matéria, por alguma razão de que não faço ideia, o prof indicou o vetor $\vec p$ a apontar da carga negativa para a positiva.

### Polarização
- E assim, no condensador da figura acima, temos:
![[dieletrico 2]]
- Podemos ver que imediatamente junto às superfícies carregadas formam-se superfícies carregadas no interior do dieletrico, com sinal oposto à sua superfície adjacente.
- E então que se forem formados $N$ dipolos, tem-se:
$$P=Np=Nq\delta\quad\quad[C/m^2]$$
Sendo que $P$ é a **Polarização elétrica**. Ora, esta é uma grandez vetorial obtida assim:
$$\Large\vec P=n\vec p=Nq\vec \delta$$
- Temos então que o meio entre as placas neste condensador é:
    - **homogéneo** - $Q=0$ no interior (entre as superfícies interiores das placas, excluido essas superfícies), pois os dipolos estão bem distribuídos
    - **isotrópico** - porque $\vec E$ e $\vec P$ têm o mesmo sentido e direção ($\vec P$ está mostrado na imagem acima, $\vec E$ vai de V+ para V-)

- Assim, é preciso compreender que a carga que surgiu junto às placas, assim como os dipolos elétricos, *não* surgiram por movimento de cargas, mas sim porque o campo elétrico existente afastou os centros de carga positiva e negativa dos átomos.

![[dieletrico 3]]
- Vemos ainda que, como existe campo elétrico dentro do dielétrico, isto que dizer que $q_c\neq q_d$ e até que 
$$|q_d|<|q_c|$$
- E podemos também ver que o campo macroscópico, $\vec E$ (aquele que importa), é dado por:
$$\Large\vec E=\vec E_0+\vec E_d$$
Sendo que $\vec E_0$ é o campo do condensador em si, aquele definido pela DDP e pelas cargas no exterior do dielétrico. $\vec E_d$ é o campo criado pelas cargas na superfície do dielétrico. Facilmente vemos que estes dois campos terão sentidos opostos e que $E_0>E_d$

### Densidade Superficial de cargas polarização
- Imaginemos que se tem uma certa área em estudo, a superfície $s$, na superfície carregada no interior do dielétrico. Assim, o volume em estudo será $\delta s$ (delta é o comprimentos dos dipolos elétricos).
- Teremos que $qNs\delta$ é a carga total de $N$ cargas num certo volume em estudo $s\delta$
- Assim, se dividirmos isto por $s$ ficamos com a fórmula de P vista antes
  $$\Large qN\delta=P=\sigma_P$$
- Como obtivemos este valor ao dividir uma quantidade de carga por uma área, temos que isto é também uma densidade superficial de carga.
- E assim vemos que **o valor de P é uma densidade superficial de carga**, a *densidade superficial de cargas de polarização*.

![[dieletrico 4]]
- E temos então que a densidade de carga nesta camada que separa o condutor do dielétrico, $\sigma$, é dada por
$$\Large\sigma=\sigma_l-\sigma_P$$(de notar que $\sigma_l$ é a densidade superficial de cargas livres, no condutor, e $\sigma_P$ é a densidade de cargas polarizadoras, no dielétrico. Isto é uma subtração porque as duas superfícies têm carga de sinal oposto)

- E temos então que:
$$E_l-E_P=\frac{\sigma}{\varepsilon_0}=\frac{\sigma_l-\sigma_P}{\varepsilon_0}=E$$
- E deste modo, jutando as equações $E=\frac{\sigma_l-\sigma_P}{\varepsilon_0}$, $qN\delta=N=\sigma_P$ , temos que:
$$\Huge\sigma_l=\varepsilon_0E+P$$
- Se além de consideerarmos o meio *homogéneo* e *isotrópico*, também o considerarmos **linear**, temos que $P\propto E$ e, mais exatamente, que $P=\varepsilon_0\chi E$ ($\chi$(chi) é a suscetibilidade magnética do meio).
- Assim, substituindo isto na equação $\sigma_l=\varepsilon_0E+P$, temos
$$\begin{align}
\sigma_l &= \varepsilon_0E+P\\
&= \varepsilon_0E+\varepsilon_0\chi E\\
&= \varepsilon_0 (1+\chi)E\\\\
\Huge\sigma_l &= \varepsilon E
\end{align}$$
- Para compreender o último passo é preciso saber que $\varepsilon_r$, o fator que relaciona a capacidade de um condensador em que o meio entre as placas é o vácuo com um em que não é, pode ser obtido por $\varepsilon_r=1+\chi$. E então tem-se:
$$\varepsilon=\varepsilon_0\varepsilon_r$$
E temos então que 
$$D=\varepsilon_0E+P$$
$$\Huge\vec D=\varepsilon\vec E$$

#em1 #dieletrico #fisica 