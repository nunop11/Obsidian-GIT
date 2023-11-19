# Eletro 1 - Aula teórica 16 (JAM)
#### Nota sobre a aula anterior
- Falamos de como normalmente só se usa pico, nano e micro Farad. 
- Isto deve-se ao facto que $C=\frac{Q}{\Delta V}$ e como $C_{esfera}=4\pi\varepsilon_0a$, então para ter uma capacidade de $1F$ era necessário que o raio do condutor fosse $a=9\cdot10^9~\text m$

## Condensador de 2 placas
![[condensador 2 placas]]
- Acima vemos 2 placas carregadas, a de cima com carga positiva, a de baixo com carga negativa. As setas desenhadas representam as linhas do campo criado pela carga negativa (azul) e pela carga postiiva (vermelho).
- Podemos ver que o campo do lado de fora das placas é nulo.
- Podemos também ver que nas beiras das placas o campo elétrico curva-se. Isto chama-se de **efeito de borda**. Quando a distância entre as placas for muito menor do que as placas (distância de milimetros para placas com centimetros de lado), podemos ignorar este efeito.

![[condensador placas paralelas]]
- Primeiro, iremos considerar que $d\ll L$ para poder ignorar o efeito de borda.
- Assumindo que as placas são equivalentes a planos infinitos temos que, *para cada uma das placas*, $E=\frac{\sigma}{2\varepsilon_0}$
- Assim, o campo entre as placas, tendo em conta o campo criado por cada uma delas, será igual a $E=\sigma/\varepsilon_0$ e$E=\Delta V/d$ (isto vem da integral $\Delta V=-\int E$ entre as duas placas)
- E como $\sigma=\frac QS$, tem-se que $$\frac{Q}{S\varepsilon_0}=\frac{\Delta V}{d}$$
- Logo, $$C=\frac{Q}{\Delta V}=\frac{S\varepsilon_0}{d}$$
, que nos dá a capacidade de um condensador de 2 placas paralelas *ideal*.
- Se a carga por $\Delta V$ aumentar ou se as placas se aproximarem haverá aumento da capacidade, mas se elas se aproximarem demasiado pode ocorrer descarga.

#### Energia do condensador
- Tendo em conta uma pequena contribuição de carga do condensador, $dq$, temos que $$dW=V\cdot dq=\frac{q}{C}dq=dU_e$$
- Logo, $$U_e=\int_0^Q\frac{q}{C}dq=\frac{Q^2}{2C}=\frac12C(\Delta V)^2$$
- E como $C=\frac{\varepsilon_0S}{d}$, então 
$$\begin{align}U_e&=\frac12\varepsilon_0\frac Sd(\Delta V)^2\\
&= \frac 12\varepsilon_0\frac{S}{d^2}(\Delta V)^2d\\
&= \frac12\varepsilon_0Sd\left(\frac{\Delta V}{d}\right)^2
\end{align}$$
- E como $Sd$ (área x distância) é o volume entre as placas e $\frac{\Delta V}{d}$ é o campo elétrico, então:
$$U_e=\frac12\varepsilon_0E^2V$$
- Isto também pode ser obtido utilizando a integral $U_e=\frac{\varepsilon_0}{e}\int|E|^2dV$

### Pressão do Campo E
- Imaginemos mais uma vez o condensador do exemplo acima:
![[condensador placas paralelas]]
- Consideremos o campo criado pela placa de cima, $E_+$, e uma área $ds$ da placa de baixo.
- Queremos saber a força que o campo $E_+$ cria em $ds$.
- Considerando que as placas são ilimitadas e que $dq=\sigma ds$, tem-se
$$dF=|dq|E_+=\sigma ds\frac{\sigma}{2\varepsilon_0}=\frac{\sigma^2}{2\varepsilon_0}ds$$
- E temos que $P=F/A$, logo
$$P=\frac{dF}{ds}=\frac{\sigma^2}{2\varepsilon_0}$$
- Esta é a pressão eletroestática
- De notar que para gerar pressão é necessário que ocorra algum tipo de *colisão*. Ou seja, o campo elétrico faz com que ocorra uma **tranferência de momento linear**. Exemplo: radiação eletromagnética pode mover poeiras espaciais.

#em1 #condensador #fisica 