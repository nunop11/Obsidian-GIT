# Eletro 1 - Aula teórica 13 (JAM)
- Temos que, num dado sistema, existe um campo $\vec E(\vec r)$, e uma carga $q>0$
- Temos ainda que a carga se está a mover de $a$ para $b$
![[mov carga força ext]]
- E como vimos na aula anterior, para que a carga descreva a trajetória desejada, existe uma força exterior aplicada nela para anular a força elétrica. Ora, essa força não terá origem eletroestática e fará trabalho:
$$W_{a\to b}=-\int_a^b\vec F_{ext}(\vec r)d\vec r=-\int_a^bq\vec E(\vec r)d\vec r$$
- E assim, podemos determinar a diferença de potencial:
$$\frac{W_{a\to b}}{q}=-\int_a^b\vec E(\vec r)d\vec r=V(b)-V(a)$$

### Caso simples: carga na origem
- Temos agora uma carga $q_c>0$ na origem e $\vec r$ o vetor unitário radial. Assim $\large\vec E(\vec r)=\frac{q_c}{4\pi\varepsilon_0}\frac{\hat r}{r^3}$
- Deste modo, 
$$V(b)-V(a)=-\int_a^b\frac{q_c}{4\pi\varepsilon_0r^2}dr=\frac{q_c}{4\pi\varepsilon_0r_b}-\frac{q_c}{4\pi\varepsilon_0r_a}$$

- Assim, considerando que a posição inicial, $a$, é o infinito. Ou seja, a carga vem do infinito para o sistema, temos que:
>$$\large V(\vec r)=\frac{q_c}{4\pi\varepsilon_0r}$$
- Podemos ver que o módulo do potencial aproxima-se de 0 consoante $r$ aumenta. Vemos ainda que se $q>0$ o potencial diminui até 0, e se $q<0$ o potencial aumenta até 0.

### Caso de algo infinito
- Se tivermos algo como uma linha ou plano infinito, temos 
$$V(\vec r)-V(P_0)= -\int_{P_0}^r\vec E(\vec r)d\vec r$$
sendo que $V(P_0)$ é um valor que admitimos como valor de referência.

## Criar sistema de cargas e Energia
- Imaginemos agora que temos um sistema vazio e que queremos criar um sistema de cargas unitárias.
-- carga 1 --
- Começamos por colocar uma carga $q_1$ em $\vec r_1$. Já sabemos que $W=0$ porque não ocorrem interações eletroestáticas.
-- carga 2 --
- De seguida, acrescentamos uma carga $q_2$ na posição $\vec r_2$. Agora já teremos que $W\neq0$. Assim,
$$\begin{align}W_{\infty\to r}&=q_2(V(r)-V(\infty))\\
&= q_2\frac{q_1}{4\pi\varepsilon_0\Vert\vec r_2-\vec r_1\Vert}
\end{align}$$
sendo $V(r)$ o potencial elétrico gerado pela carga $q_1$ a uma distância $r$ desta.
- Temos assim que a energia potencial do sistema passa de 0 para $$E_p^{1,2}=\frac{q_1q_2}{4\pi\varepsilon_0|r_2-r_1|}$$
-- carga 3 --
- Acrescentamos agora uma terceira carga, $q_3$. O seu potencial irá agora depender do potencial gerado pelas cargas 1 E 2.
- Assim,
$$\begin{align}W_{\infty\to r_3}&=q_3(v(\vec r_2)-v(\infty))\\
&= q_3\left(\frac{q_1}{4\pi\varepsilon_0|r_3-r_1|}+\frac{q_2}{4\pi\varepsilon_0|r_3-r_2|}\right)
\end{align}$$
E então a energia potencial do sistema passa a ser a energia obtida anteriormente, $E_p^{1,2}$, juntamente com o trabalho realizado para trazer a carga 3 para o sistema (no final da equação abaixo):
$$E_p^{1,2,3}=\frac{q_1q_3}{4\pi\varepsilon_0|r_3-r_1|}+\frac{q_2q_3}{4\pi\varepsilon_0|r_3-r_2|}+\frac{q_1q_2}{4\pi\varepsilon_0|r_2-r_1|}$$
-- carga N -- 
- Como já vimos, a equação acima está horrível. Assim, podemos generalizar para N cargas.
>$$\huge E_p=\frac12\sum_{i\neq j}^N\frac{q_iq_j}{4\pi\varepsilon_0|r_i-r_j|} ~~\text{OU}~~\sum_{i>j}^N\frac{q_iq_j}{4\pi\varepsilon_0|r_i-r_j|}$$
> O $\frac12$ na primeira forma ou o $i>j$ na segunda servem para garantir que não temos combinações repetidas ($q_iq_j=q_jq_i$).

### Caso especial: Linha fechada
- Imaginemos agora que a carga faz uma trajetória que começa e acaba no mesmo sítio, descrevendo assim uma linha fechada. Assim, temos que 
> $$W_{a\to a}=0=\oint \vec E(\vec r)d\vec r$$ 

- Relembremos que o campo eletroestático (constante no tempo) é conservativo, pelo que 
$$\vec E(r) = -\nabla V(\vec r)$$

## U (Energia do campo elétrico)

$$U=\frac{\varepsilon_0}{2}\int_{todo~o~espaço}|\vec E(\vec r)|^2 dVol$$
- Devemos compreender que em $E_p$ tínhamos a energia gasta para trazer as cargas e então $E$ atua como um mediador das reações entre as cargas.
- Já na fórmula de $U$, o campo $E$ atua como um **meio de transporte de energia**.

#em1 #potencialE #fisica 