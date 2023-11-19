# Eletro 1 - Aula teórica 22 (CCR)
![[fio condutor]]
- Temos um condutor retilíneo, em que passa uma corrente $I$, e em que tenis as partículas a mover-se com velocidade $v$
- Temos então (sendo $N$ o número de cargas na corrente):
$$d\vec F_m=dNq\vec v\times\vec B$$
- Temos ainda que (sendo $n$ a *densidade volúmica* de carga):
$$\mathcal{\vec J}=nq\vec v=\frac{dN}{dV}q\vec v\leftrightarrow dNq\vec v=\mathcal{\vec J}dV$$
Juntando as duas equações acima:
$$d\vec F_m=\mathcal{\vec J}\times\vec B~dV$$
- Assim, ao integrar isto obtém-se:
>$$\Large\vec F_m=\mathcal{\vec J}\times\vec BSL=I\vec L\times\vec B$$

## Baloiço Magnético
![[baloiço magnético]]
- Temos uma corrente a descrever o percurso mostrado acima. A parte quadrada no centro pode rodar.
- Os vetores $\vec F_m$ nos casos a seguir serão determinados com $\vec F_m=I\vec L\times\vec B$

-- Caso 1 --
![[baloiço caso 1]]
- Neste caso vemos que o baloiço não se move

-- Caso 2 --
![[baloiço caso 2]]
- Neste caso, o baloiço move-se, porque existe uma força aplicada em $y$.
- Assim, como uma força está a gerar uma rotação, temos um torque:
$$\vec\tau=\vec r\times\vec F_m=I\vec r\times\vec L\times\vec B$$
- No entanto, ter $\vec r\times\vec L$ acaba por ser o mesmo que ter o vetor ÁREA, $\vec A$. Este é um vetor que terá módulo igual á área do quadrado no centro do fio. A sua direção será perpendicular à área em si. Já o sentido será aquele indicado pelo polegar se fecharmos a mão no sentido que a corrente tem. Por exemplo, num condutor circular na horizontal com a corrente a ir em sentido horário, o vetor área teria sentido vertical para baixo. Exemplo:
![[vetor normal área]]
- Assim temos $$\vec\tau=I\vec A\times\vec B=\vec m\times\vec B$$
Em que $\vec m$ é o vetor **momento magnético**. Ele terá o mesmo sentido e direção que $\vec A$.

- Para este mesmo movimento temos:
$$\begin{align}
dW_{F_m}=\vec F\cdot\vec dr&=Fr\cos\theta~d\theta\\
&=\vec r\cdot\vec F~d\theta\\
&=\vec m\cdot\vec B\\\\W_{F_m}=-\vec m&\cdot\vec B
\end{align}$$
- Assim temos:
> $$\Huge \vec\tau=\vec m\times\vec B\quad\quad||\quad\quad U=-\vec m\cdot\vec B$$

## Fm Total de Espira
- Imaginemos que temos uma espira fechada. Teremos sempre que $F_m total=0$, porque funciona como se fosse uma circunferência, mesmo que não seja, há sempre forças a anularem-se umas às outras.
- Mas podemos verificar isto por meios matemáticos:
$$\begin{align}
\vec F_m&=\int \mathcal{\vec J}\times\vec B~dV\\
&= \int\mathcal{\vec J}\times\vec B~S~dl\\
&= I\int \vec dl\times\vec B=\vec 0
\end{align}$$
O último passo ocorre porque ficamos com $\int_{\text{sup fechada}}\dots dl$, o que irá dar sempre 0.

> NOTA ÚTIL: Como temos $U=-\vec m\times\vec B$, podemos usar isto para ver quando é que ficamos com $U=0$. Muitas vezes isto será um mínimo de energia e, portanto, o ponto em que um certo objeto deixará de se mover por ação das forças eletromag.

## Força entre 2 fios
Tendo um sistema assim:
![[2 fios condutores]]
- Tem-se que se gera uma força magnética que um fio gera no outro:
>$$\Large d\vec F_m=\frac{\mu_0}{4\pi}\frac{I_1I_2}{r^2}[\vec dl_2 [\vec dl_1\times\vec u_r]]$$
- Para esta força, ao contrário de $F_e$:
    - Se os $\mathcal J$ dos fios tiverem o **mesmo sentido**, $F_m$ é **atrativa**.
    - Se os $\mathcal J$ dos fios tiverem **sentidos opostos**, $F_m$ é **repulsiva**.

- De notar ainda que $c=\sqrt{\frac{1}{\mu_0\varepsilon_0}}$ e então: $\Large \frac{\mu_0}{4\pi}=\frac{1}{4\pi\varepsilon_0c^2}$
- Da equação acima tira-se que:
$$dF_m(2)=I_2\vec dl_2\times\frac{\mu_0}{4\pi}\frac{I_1\vec dl_1\times\vec u_1}{r^2}$$
Aqui temos a mesma fórmula que antes, mas formulada de outra forma. Aqui podemos ver que esta é a força aplica no fio 2, e gerada pelo fio 1. Isto é especialmente indicado pelo sentido do vetor $\vec u_1$. Temos ainda que a segunda parcela é o campo gerado pelo fio 1. E sabemos isto por causa da:

## Lei de Biot-Savart
>$$\Huge d\vec B(\vec r)=\frac{\mu_0}{4\pi}\frac{I_1\vec dl_1\times\vec u_r}{r^2}$$

#em1 #biot-savart #fisica 