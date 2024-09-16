- Consideremos que a onda luminosa emitida em cada ponto da fenda é uma onda _progessiva_ esférica, sendo a sua amplitude descrita por:
$$A(r)=A_{0}e^{i(kr-\omega t)}$$
- Assim, consideremos um ponto $C$ a uma distância $r$ de um ponto $P$ no alvo. Teremos nela: $A=A_{0}e^{i(kr-\omega t)}$

- Consideremos um ponto $C'$ a distância $l$ de $C$. Este ponto estará a uma distância $d$ do ponto $P$ no alvo, chegando dele uma onda com amplitude $A'=A_{0}e^{i(kd-\omega t')}$. Usamos $t'$ porque estas ondas irão demorar tempos diferentes a chegar a $P$.
    - Mais concretamente, sendo $\delta=r-d$ temos: $\Delta t=t'-t=\frac{\delta}{c}$. Como teremos sempre $\delta\ll c$ podemos considerar $\Delta t\simeq\Delta t$: $$A'=A_{0}e^{i(k(r+\delta)-\omega t)}=A_{0}e^{i(kr-\omega t)}e^{ik\delta}= Ae^{i\frac{2\pi\delta}{\lambda}}$$
    - Extraindo a componente real: $$A'=A\cos\left(\frac{2\pi\delta}{\lambda}\right)$$

- Assim, no final temos que a amplitude total será: $A_{tot}=A+A'^{(1)}+A'^{(2)}+\dots+A'^{(n)}$ (para n fontes pontuais). Assim como a intensidade é proporcional ao quadrado da amplitude, temos: 
$$I_{tot}=A_{tot}^{2}$$
