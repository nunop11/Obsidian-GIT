# Eletro 1 - Aula teórica 17 (CCR)
![[dipolo el]]
- Aqui temos um sistema multipolar. De notar que estes são sistemas com cargas de sinal diferente, mas de forma que $Q_{total}=0$
- Como já sabemos, $\vec E(\vec r)=\vec E_+(\vec r_+)+\vec E_-(\vec r_-)$
- E temos ainda que se $r\gg a$, então temos que $$|\vec E(r)|\propto \frac{qa}{r^3}$$

- Assim,
$$\vec E(y,z)=\vec E_y(\vec r)+\vec E_z(\vec r)$$
- No entanto, podemos tornar isto mais fácil ao passar para **coordenadas polares**, colocando o centro no ponto médio entre as cargas. Assim,
$$\vec E(r,\theta)=E_r\hat u_r+E_\theta\hat u_\theta$$
- Temos ainda que o momento dipolar, $\vec p$ é dado por $$\vec p=q\vec a$$(sendo $\vec a$ o vetor que vai do centro da carga positiva para a negativa)

- Assim, podemos determinar o potencial do dipolo:
$$V(r)=\frac{1}{4\pi\varepsilon_0}\left(\frac{q}{r_+}-\frac{q}{r_-}\right)=\frac{q}{4\pi\varepsilon_0}\left(\frac{r_--r_+}{r_-r_+}\right)$$
> Isto voi obtido somando o potencial gerado pelas cargas + e -. Para os determinar, utilizou-se a fórmula do potencial gerado por 1 carga em função da distância $r$ a esta: $V(r)=\frac{Q}{4\pi\varepsilon_0r}$

E para determinar $r_+$ e $r_-$ tem-se:
![[dist dipolo-ponto]]
- De notar que normalmente os ângulos representados com theta não seriam iguais. No entanto, se estivermos a considerar o caso de **r>>a** teremos que $r\parallel r_+\parallel r_-$ e então os ângulos não iguais.
- Assim, $$r_+=r+\frac a2\cos\theta\quad\quad r_-=r-\frac a2\cos\theta$$
- E assim, ao substituir na equação acima fica-se com 
$$V(r)=\frac{q}{4\pi\varepsilon_0}~\cdot~\frac{r-\frac a2\cos\theta-r-\frac a2\cos\theta}{r^2-\frac{a^2}{4}\cos^2\theta}$$
- Sendo que $r\gg a$, então $r^2-\frac{a^2}{4}\cos^2\theta\approx r^2$
- Assim, $$V(r)=\frac1{4\pi\varepsilon_0}\frac{qa\cos\theta}{r^2}=\frac1{4\pi\varepsilon_0}\frac{\vec p\cdot\hat u_r}{r^2}\quad (r\gg a)$$

- E então, em coordenadas polares, temos:
$$\begin{align}
\vec E(r,\theta)&=-\vec\nabla V(r)\\
&=-\left(\frac{\partial}{\partial r}\hat u_r+\frac1r\frac{\partial}{\partial\theta}\hat u_\theta+\frac{1}{\sin\theta}\frac{\partial}{\partial \phi}\hat u_\phi \right)V(r)\\\
&=-\left(\frac{-2qa\cos\theta}{4\pi\varepsilon_0r^3}\hat u_r-\frac{1}{r}\frac{qa\sin\theta}{4\pi\varepsilon_0r^2}\hat u_\theta\right)\\
&=\frac{p}{4\pi\varepsilon_0r^3}(2\cos\theta\hat u_r+\sin\theta\hat u_\theta)
\end{align}$$
- E então
$$\vec E(r,z)=\frac{p}{4\pi\varepsilon_0r^3}(3\cos\theta\hat u_r-\hat u_z)$$
### Movimento e Torque de dipolo
![[torque dipolo]]
- Vemos que para o dipolo temos que $F_r=0$
- No entanto, facilmente se conclui que estas 2 forças iriam criar rotação do dipolo em torno do seu centro. Assim, como $\vec\tau=\vec r\times\vec F$, então:
$$\vec\tau_r=\vec p\times\vec E$$
### Campo uniforme e potencial
Tendo um campo uniforme $\vec E_0$, em que tem 2 placas a uma distância $d$.
![[placas campo uniforme]]
- Temos que $U=qV$ e então:
$$U_e=qV_{ext}(r_+)+(-q)V_{ext}(r_-)=q\cdot\Delta V$$
- E na figura acima temos ainda que:
$$V=V_0-E_0d$$
e assim:
$$V(x)=V_0-E_{ext}x$$
- E deste modo, 
$$\begin{align}U_e=q\Delta V&=-qE_0\Delta x\\
&=-qE_0a\cos\theta
\end{align}$$
(De onde é que veio o $a$ e $\cos\theta$? Não faço a mínima ideia, esta é uma aula da CCR)
>$$U_e=-\vec p\cdot\vec E$$

#em1 #dipolo #fisica 