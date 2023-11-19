# Eletro 1 - Aula teórica 12 (CCR)
> ⚠️ NOTA: Este resumo está fraco ⚠️ 
> O próximo resumo repete tudo mas explicado direito.


- Em *eletroestática*, a energia do sistema é o **trabalho**

## Trabalho
### Com 1 carga
- Temos que num sistema com 1 carga, 
$$W_{\infty\to A}=0$$
sendo este o trabalho realizado para trazer a carga do infinito para a posiçaõ 1.

### Com 2 cargas
- Imaginemos agora que temos 2 cargas, $q_1$ e $q_2$ a mover-se:
![[cargasMovTrabalho]]

- Ora, considerando que as cargas têm igual sinal, vemos que a carga que 2 gera em 1, F12 (representada na figura) iria desviar a carga da sua trajetória. Assim, terá de existir uma força F que anule F12 para que a trajetória seja a desejada.
- Temos então:
$$\begin{align}
dW_{12} &=-\vec F\cdot \vec ds\\
&= \left(\frac{-1}{4\pi\varepsilon_0}\frac{q_1q_2}{|\vec r_1-\vec r_2|^2}\hat u_{12}\right)\cdot \vec{ds}
\end{align}$$
- Assim, ao longo da trajetória da carga q1 de A para B, temos:
$$\begin{align}W_{A\to B}
&=\frac{-1}{4\pi\varepsilon_0}q_1q_2\int_A^B\frac{\hat u_{12}\cdot \vec ds}{|\vec r_1-\vec r_2|^2}\\
&=\frac{-1}{4\pi\varepsilon_0}q_1q_2\int_A^B\frac{ds_\text{radial}}{|\Delta \vec r|^2}dr\\
&=\frac{-1}{4\pi\varepsilon_0}q_1q_2\int_A^B\frac{d}{dr}\biggr(\frac{-1}{|\Delta \vec r|}\biggr)dr\\
&=\frac{-q_1q_2}{4\pi\varepsilon_0}\int_A^B\frac{d}{dr}\biggr(\frac{-1}{|\Delta \vec r|}\biggr)dr\\
&=\frac{+q_1q_2}{4\pi\varepsilon_0}\cdot\frac{-1}{|\Delta \vec r|}\biggr|_A^B\\
\end{align}$$

- E assim:
$$W_{A\to B}=\frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{|\Delta r|}~~(J)$$
E assim se vê porquê que $W_{\infty\to A}=0$

> NOTA: Em Movimento circular, $W=0$, porque $A=B=R$

### Com 3 cargas
Temos que:
$$\begin{align}W_3=W_{31}+W_{32}+W_{12}\end{align}$$
sendo $W_3$ o trabalho de um sistema de 3 cargas.

### Energia Eletroestática
Assim:
$$W_N=\frac12\sum_{i\neq j}^N\frac{1}{4\pi\varepsilon_0}\frac{q_iq_j}{|\Delta\vec r_{ij}|}=U_e$$
sendo $U_e$ a ***energia eletroestática***, a energia *potencial* do sistema.

## Potencial
Temos que o potencial elétrico do sistema, $\phi$, é dado por:
$$\phi=\frac Wq=-\int\frac{\vec F_e\cdot \vec dr}{q}=-\int \vec E\cdot \vec dr$$
E assim se obtem a DDP entre dois pontos $\vec r_1$ e $\vec r_2$:
$$\Delta\phi=-\int_{\vec r_1}^{\vec r_2} \vec E\cdot\vec dr=\int_{\vec r_1}^{\vec r_2}\frac{d}{d\vec r}(\phi(\vec r))d\vec r$$
> Podemos ver que a unidade $J/C$, que é o Volt

- E assim tem-se:
$$\vec E=-\frac{d}{d\vec r}\phi(\vec r)=-\vec\nabla\phi(\vec r)$$
- De notar que $\Delta\phi$ não depende da trajetória, apenas dos pontos final e inicial

#em1 #potencialE #fisica 