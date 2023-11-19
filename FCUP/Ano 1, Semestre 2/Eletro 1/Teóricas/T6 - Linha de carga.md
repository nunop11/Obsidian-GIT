# Eletro 1 - Aula teórica 6 (JAM)
## Distribuição Contínua
- Até agora, estivemos a estudar sistemas com um número sabido, finito e reduzido de cargas: *sistemas discretos*
- Agora estudaremos sistemas com números de cargas muito maiores, distribuidos uniformemente: *sistemas contínuos*

- Para começar temos, respestivamente, a densidade linear, superficial e volúmica de carga:
$$\lambda = \frac{Q}{L}\hspace{1cm}\sigma=\frac{Q}{S}\hspace{1cm}\rho=\frac{Q}{V}$$
- Um exemplo simples, em que queremos estudar o campo criado por um segmento de **reta** carregado num certo ponto no eixo dos z:
![[dist contínua]]
- Assim, temos que
>$$dE_z=dE\cos\alpha=\frac{dq}{4\pi\varepsilon_0d^2}\cos\alpha$$
(De notar que, neste caso, $dEz$ pode ser tida como a "contribuição" para o campo E total em z, de uma certa divisão do segmento de reta com carga, que terá carga $dq$)
- Assim, se tivermos um ponto neste segmento de reta carregado, a uma distância $x$ da origem, então temos que a distância dessa carga ao ponto no eixo $z$ em estudo é de $d=\sqrt{x^2+z^2}$
- Assim, temos que $$\cos\alpha=\frac{z}{d}=\frac{z}{\sqrt{x^2+z^2}}$$
- Podemos então substituir isto na formula anterior: $\large dE_z=\frac{dqz}{4\pi\varepsilon_0d^3}$
- Ora, $d^3=(z^2+x^2)^{\frac{3}{2}}=z^3(1+\frac{x^2}{z^2})^{3/2}=z^3(1+\tan^2\alpha)^{3/2}$
- E então,
$$\frac{1}{d^3}=\frac{1}{z^3}\frac{1}{(1+\tan^2\alpha)^{3/2}}=\frac{\cos^3\alpha}{z^3}$$
Temos ainda que $\tan\alpha=\frac{x}{z}\leftrightarrow x=z\tan\alpha\leftrightarrow dx=z~d(\tan\alpha)\leftrightarrow$
>$$dx=z\frac{d\alpha}{\cos^2\alpha}$$

Por fim, como $\lambda=Q/L$, então
>$$dq=\lambda dx$$

E finalmente, ao substituir tudo isto obtemos que $E_z=\int dE_z=\frac{\lambda}{4\pi\varepsilon_0z}\int\cos\alpha d\alpha$, e então:
$$E_z=\frac{\lambda}{2\pi\varepsilon_0z}\sin\alpha$$
(De notar que esta integral vai de $-\alpha_0$ a $+\alpha_0$)

---
- Imaginesse agora que temos uma distribuição ilimitada, ou seja, $\alpha\to\pi/2$
- Assim:
$$\vec E(0,0,z)=\frac{\lambda}{2\pi\varepsilon_0z}\hat z$$
#em1 #campoE #fisica 