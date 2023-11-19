# Eletro 1 - Aula teórica 20 (JAM)
- Vimos na aula passada que tendo numa superfície uma pequena divisão $ds$, cujo vetor normal é $\hat n$, temos que
$$\vec{\mathcal J}=nq\vec v\quad\quad e\quad\quad dI=\mathcal{\vec J}\cdot\hat n ds$$

### Modelo de Drude
- Este modelo considera que um metal é constituido por uma rede de iões, rodeados por um gás clássico de eletrões que, portanto, têm liberdade de movimento.
- Assim, os eletrões em constante movimento frequentemente colidem com iões, em colisões perfeitamente aleatórias. Considera-se assim que o tempo passado entre a ocorrência de 2 colisões como sendo $\tau$
- Anteriormente, em Em1, vimos que dentro de metais/condutores não existe campo. No entanto, neste caso dos eletrões em movimento e em colisões tem de exisitir uma DDP a fazer trabalho e criar um campo para que as cargas se movam. Assim, o condutor não está em equilíbrio eletrostático.

- Vejamos um caso mais específico:
![[rede ioes e eletrão]]
- Pela 2ª lei de Newton temos que $F_r=ma=F_e$. Assim, $\Large\vec a=\frac{-e\vec E}{m}$
- Temos então, a seguinte equação do movimento:
$$\vec v(t)=\vec v_0+\left(\frac{-e\vec E}{m}\right)t$$
Sendo $t=0$ o instante imeadiatamente após uma colisão
- Assim, fazendo a média de ambas as parcelas da equação acima para $n$ eletrões, fica-se:
$$\vec v_d=-e\frac{\vec E}{m}\tau$$
- Send que $\vec v_d$ é a **velocidade de drift**, o que acaba por ser a média das velocidades dos eletrões neste modelo.

- Anteriormente vimos que $\mathcal{\vec J}=nq\vec v$, pelo que então temos:
$$\mathcal{\vec J}=n(-e)\vec v_d=\frac{ne^2\tau}{m}\vec E$$
E assim vemos que $J\propto E$
- No entanto, temos também que $\sigma=\frac{ne^2\tau}{m}$, sendo sigma a condutividade elétrica. Assim, temos que:
>$$\Huge\mathcal{\vec J}=\sigma\vec E$$
>Ora, isto é a ***LEI DE OHM***

#### Dedução da Lei de Ohm do secundário
- Imaginemos que se tem um condutor cilindrico de diâmetro constante, em que a secção transversal tem área $S$ e o comprimento é $L$. Aplica-se uma DDP nos extremos do condutor e assim gera-se uma corrente elétrica.
- Temos que a corrente pode ser dada por $I=\mathcal JS$. Logo, $\mathcal J=I/S$
- Como o campo é uniforme, temos que $E=V/L$.
- Substituindo na equação acima:
$$\begin{align}
\mathcal J&=\sigma E\\
\frac IS &= \sigma \frac VL\\
V &=\left[\frac1\sigma\frac LS\right] I
\end{align}$$
Na parcela entre parenteses retos temos a resistividade ($\rho=1/\sigma$) e temos aspetos geométricos, log temos a resistência. Assim:
$$V=RI\leftrightarrow R=\frac VI $$

---

### Equação da Continuidade
- Imaginemos que temos uma superfície fechada $S$. Dentro dela existe uma certa carga que varia com o tempo, $Q(t)$. Ora, para ela variar é preciso que exista uma corrente elétrica a entrar/sair da superfície, o que faria com que a carga aumentasse/diminuisse.
- Assim, considerando uma pequena parte da superfície, $ds$, teríamos que:
$$dI=\mathcal{\vec J}\cdot\hat n ds$$
- Assim podemos fazer 
$$∯_S \mathcal{\vec J}\cdot\hat n~ds$$
Isto irá permitir calcular a corrente. Assim, se esta integral for:
    - igual a 0, então não há corrente
    - menor que 0, a corrente está a sair da superfície e $Q$ a diminuir
    - maior que 0, a corrente está a entrar na superfície e $Q$ a aumentar

- Assim, como a integral é igual à corrente, sabemos que a corrente é dada por $I=-\frac{dQ}{dt}$ (o menos é para o sinal da derivada bater certo com as opções acima)
- Temos ainda que $Q=\int_V\rho~dV$
- Assim:
$$∯_S \mathcal{\vec J}\cdot\hat n~ds=-\frac{dQ}{dt}\int_V\rho~dV$$
Esta é a equação da continuidade e que mostra que existe conservação de carga

### Potência
- Imagine-se que num certo sistema temos um elemento de volume, $dV$, que contém $nq$ cargas e sobre o qual é aplicado um campo elétrico $\vec E$
- Assim, iremos considerar que $dV$ se move como 1 carga, movendo-se com velocidade de drift, $\vec v$. Assim:
$$dP=\vec v\cdot \vec F$$
sendo $dP$ a potência desta unidade de volume.
- Temos que $v$ tem o mesmo sentido e direção que $F$. Assim, $$dP=vF=nqvE\quad\quad(F=QE=nqE)$$
- Assim, temos que $$dP=\mathcal{\vec J}\cdot\vec E$$
- Mas, como já vimos, se o sistema for linear tem-se que $\mathcal{J}=\sigma E$. E assim:
>$$\Huge dP=\sigma E^2$$
> Isto é a ***LEI DE JOULE***

- Esta é então a energia dissipada pelas colisões de eletrões com iões no volume $dV$. Por outras palavras, como colisões levam a tranferência de energia cinética e assim a aquecimento, esta é a energia tranferida por aquecimento AKA por *efeito de joule*

#### Dedução da Lei de Joule do secundário
- Como já vimos, $dP=\mathcal{\vec J}\cdot \vec E=\mathcal JE$, $\mathcal J=\frac IS$ e $E=\frac VL$. Assim:
$$\begin{align}
dP &=\mathcal JE\\
dP &= \frac IS\frac VL=IV\frac{1}{SL}\\
dP &= RI^2 \frac{1}{SL}\quad\quad (porque~~V=RI)\\
dP &= RI^2~\text{Vol}^{-1}
\end{align}$$
- Isto $\text{Vol}^{-1}$ faz sentido, porque os valores utilizados para determinar $dP$ são para um elemento de volume, $dV$. 
---

## Magnetismo
- Temos cargas num sistema, de tal modo que a força elétrica aplicada nelas é $q\vec E$
- Estas movem-se com velocidade $v\ll c$ 
- Ora, se o campo **variar para a carga em movimento**, $q$, esta carga é atuada por forças **não elétricas**
> Aqui deve-se notar que os campos elétricos envolvidos continuam a ser estáticos, ou seja, não variam com o tempo. No entanto, como já vimos, variam com a posição. Assim, se uma carga se mover ao longo do campo, ele irá variar ao longo do tempo, **no referencial da carga**.

- Assim temos o campo magnético: $\vec B$
- Este campo é originado em cargas que estão em movimento, *em relação ao observador*
- Antes tinhamos $\vec F=q\vec E$, agora temos:
$$\Large\vec F_m=q\vec v\times\vec B$$
- Repito, este campo e força só existem no referencial em que a carga se move. Caso contrário, existe apenas campo e força elétrica.

- Assim, para uma carga em movimento, a força nela atuada é a **Força de Lorentz**, dada por:
$$\large\vec F=\vec F_e+\vec F_m=q\vec E+q\vec v\times\vec B$$
- Ora, em muitos casos iremos ter que $B\gg E$, pelo que iremos considerar $\vec F_r=q\vec v\times\vec B$
- Assim, podem ocorrer 3 casos:
1. $\vec v\parallel\vec B$ --> Neste caso $\vec F_m=\vec0$. A partícula descreve movimento uniforme. Pouco interessante.
2. $\vec v\perp\vec B$ --> Neste caso temos $F=qvB=ma_n=m\frac{v^2}{r}$, pois a partícula descreve movimento circular uniforme. Ficasse com esta equação muito importante: $$\Large|q|B=m\frac vR$$
Daqui se tira que $\omega=\frac{qB}{m}$
3. $\vec v=\vec v_\parallel+\vec v_\perp$ --> Aqui ocorre a sobreposição dos movimentos anteriores e assim ocorre um **movimento elicoidal**. Aqui tem-se que o raio da hélice é dado por $R=\frac{mv_\perp}{|q||B|}$ e que o passo da hélice, $p$, é igual a $p=v_\parallel T$

#em1 #ohm #joule #magnetismo #fisica 