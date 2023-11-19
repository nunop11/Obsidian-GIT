# Eletro 1 - Aula teórica 7 (JAM)
## Anel
- Continuamos a ter uma distribuição linear, mas contínua, que não é ilimitada.
![[anel]]
- Podemos sempre arranjar um par de pontos do anél que anulam as componentes não-Z um do outro. Ou seja, no eixo transversal ao anel (z), o vetor $\vec E$ total só tem componente em $z$.
- Temos ainda que $d=\sqrt{R^2+z^2}$, que é sempre verdade neste caso
- Temos então que $dE_z=E\cos\alpha$, e que $\large\cos\alpha=\frac{z}{d}=\frac{z}{(R^2+z^2)^{1/2}}$
- Also, $$dE=\frac{1}{4\pi\varepsilon_0}\frac{dq}{d^2}=\frac{1}{4\pi\varepsilon_0}\frac{dq}{R^2+Z^2}$$(Nisto, considerou-se que cada "contribuição para o campo" (dE) corresponde à "contribuição" de cada carga (dq), que se estudou como se fosse pontual)

Desta forma,
$$E(z)=\int dE\cos\alpha=\frac{1}{4\pi\varepsilon_0}\frac{z}{(R^2+Z^2)^{3/2}}\int dq$$
Ora, a integral de dq é a "soma" da carga de todas as "contribuições" de carga no anel. Ou seja, $\int dq=Q$
- Assim, o campo gerado por um anel em função de z é:
$$E_z(0,0,z)=\frac{Qz}{4\pi\varepsilon_0(R^2+z^2)^{3/2}}$$
- Daqui vemos logo que $\vec E(0,0,0)=\vec 0$, sendo que o centro do anel é portanto um ponto de equilíbrio *instável*. Deste modo, se o sinal de uma carga colocada no sistema for diferente do sinal da carga do anel, esta carga irá fazer um movimento oscilatório.
- Assim, neste caso em que $|z|\ll R$, tal como visto noutro exemplo da aula anterior podemos deduzir o valor de $\omega$, e temos que
$$\omega^2=\frac{k}{m}=\frac{qQ}{4\pi\varepsilon_0R^3m}$$
- Estudou-se ainda o caso de $|z|\gg R$. Nesse caso, temos que $\vec E(0,0,z)=\frac{Q}{4\pi\varepsilon_0z^2}$. Temos portanto que, a uma distância muito longa do anel, é como se este fosse uma carga pontual. Mas não é ofc

- Nos últimos casos usou-se *módulo* de z, porque o comportamento do campo/força é exatamente igual para os dois lados do anel.

## Disco
- Recordando, $\sigma=Q/S$. Assim, dada uma contribuição de carga do disco, temos que $dq=\sigma~ds$. A área de um dos aneis que forma o disco é $ds=2\pi rdr$ (se cortassemos um dos aneis e o "esticássemos", teríamos um retângulo; trapézio na realidade, mas como $dr\ll r$ é como se fosse um retângulo)
- Assim, podemos ver que um disco é uma sobreposição de discos. Deste modo, como para o anel:
$$E=\frac{Qz}{4\pi\varepsilon_0(R^2+z^2)^{3/2}}$$
- Assim, como $dq=\sigma 2\pi rdr$, então:
$$d\vec E(0,0,z)=\frac{\sigma~2\pi r~dr~z}{4\pi\varepsilon_0(r^2+z^2)^{3/2}}$$
- Assim, como $\vec E=\int d\vec E$, então:
$$\vec E=\frac{2\pi\sigma~z}{4\pi\varepsilon_0}\int_{R_{int}}^{R_{ext}}\frac{r}{(r^2+z^3)^{3/2}}dr$$(De notar que o R_int é igual a 0 se o disco não tiver um buraco no meio)
- Assim, se $R_{int}=0$, temos que:
$$\vec E(0,0,z)=\frac{\sigma}{2\varepsilon_0}\biggr[\frac{z}{|z|}-\frac{z}{\sqrt{z^2+r^2}{}}\biggr]$$
- Se $|z|\gg R$, então voltamos a ter o caso do anel em que é como se este fosse uma carga pontual, mas não é!!
- Se $|z|\ll R$ e $R_{int}>0$, então voltamos a ter o caso do anel em que há um movimento oscilatório em que o centr do anel é o ponto de equilíbrio.
- Se $R\to\infty$, então temos o campo gerado por um plano, e então:
$$\vec E(0,0,z)=\frac{\sigma}{2\varepsilon_0}\frac{z}{|z|}\hat z$$

#em1 #campoE #fisica 