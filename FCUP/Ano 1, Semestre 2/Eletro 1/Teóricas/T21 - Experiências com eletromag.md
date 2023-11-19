 # Eletro 1 - Aula teórica 21 (JAM)
## Experiência de Thomson
![[Exp thomson]]
- Na experiência de Thomson, tem-se, por ordem de acontecimento:
    1. Um cátodo faz com que sejam libertados eletrões para o sistema, para a parte 1 da montagem.
    2. Na parte 1, devido à diferença de potencial, um campo elétrico acelera as partículas até à fissura, a que chegam com velocidade $\vec v$
    3. Após passar na fissura, as partículas chegam à parte 2, onde existe um campo magnético que faz com que as partículas descrevam um movimento circular, até colidir com a parede, uma distância $d$ abaixo da altura original.

>Nota: Neste exemplo, iremos assumir que todos os eletrões têm velocidades iniciais iguais a 0 e que saem da fissura com velocidades iguais.

- Temos então $\Delta E_c+\Delta E_p=0$. Tendo que a energia potencial é a Energia Potencial Elétrica, então:
$$\frac12mv^2=eV\leftrightarrow v=\sqrt{\frac{2eV}{m}}$$
- E já sabemos que $v=\omega r$ e vimos na aula anterior que $\omega=\frac{eB}{m}$. Assim: 
$$R=\sqrt{\frac{2mV}{eB^2}}$$
- Ao estudar a geometria da figura acima, por teorema de Pitágora obtemos que $(R-d)^2+\ell^2=R^2$
- Assim ficamos com 
$$\frac em=\frac{8Vd^2}{B^2(d^2+\ell^2)}=\frac{2V}{B^2R^2}~~~~~~(\text{no caso em que se percorra 1 raio inteiro})$$
- Assim, esta experiência permite estudar a relação entre carga e massa.

## Filtro de Velocidades
![[filtro velocidades]]
- Este sistema tem o objetivo que os eletrões que saiam pela fissura da direita tenha uma velocidade muito bem definida (vetor. Ou seja, direção, sentido e módulo bem definidos)
> Nota: Neste caso, consideramos que as fissuras não influenciam os campos.

- Primeiro é preciso notar que para que a trajetória descrita pelo eletrão seja horizontal, e necessário que $\vec F_e+\vec F_m=\vec 0$. Assim:
$$qE=qvB\leftrightarrow v=\frac EB$$
- Assim, para garantir que a velocidade final é a desejada, só é preciso ajustar a relação E/B
- Se a direção da velocidade com que o eletrão entra na fissura da esquerda não for exatamente horizontal, mas sim ligeiramente inclinada, o campo magnético fará com que a partícula descreva um movimento curvo e colida com a placa. Isto é ilustrado no percurso a preto tracejado acima.

## Espectrómetro de massas
![[espectrometro massas]]
- Primeiro, as partículas em estudo passam por um filtro de velocidades, pelo que se sabe que a velocidade ao entrar na secção em que apenas atua o campo $\vec B_2$ é igual para todas e igual a $v=E/B_1$.
- Assim, pela 2ª Lei de Newton aplicada ao movimento circular uniforme:
$$\begin{align}
F=ma\longrightarrow qvB&=ma_n\\
qvB&=m\frac{v^2}{R}\\
qB_2&=m\frac{E}{B_1R}\\
\end{align}$$
e assim:
$$m=\frac{qB_1B_2R}{E}$$
- Assim, como $q$ é constante e $E$, $B_1$ e $B_2$ são conhecidos, então a única coisa que influencia o raio da trajetória descrita é a massa, $m$. E é deste modo que esta montagem permite determinar a massa de partículas.

## Acelerador de Partículas
![[acelerador particulas]]
- Nesta figura podemos ver as 4 fases num acelerador de partículas. Estas vão-se repetindo até que a partícula saia do sistema através de uma fissura num dos D.
- Na figura, podemos ver que enquanto a partícula descreve meia circunferência no interior de um D, é necessário que o campo elétrico entre os D inverta o seu sentido, de modo a poder acelerar a partícula quando ela sair do D.
- Assim, precisamos de calcular a frequência com que E tem de inverter.
> Nota: Neste caso estamos a considerar um acelerador relativamente pequeno, de modo que $v\ll c$. Caso contrário, seria necessário ter em conta o relativismo.

- De acordo com a segunda lei de Newton temos:
$$qv_1B=m\frac{v^2}{R}\leftrightarrow v_1=\frac{qBR}{m}$$
- Temos que o tempo, $t_v$ para percorrer meia circunferência (distância de $\frac12 2\pi R$) é dado por $$\frac122\pi R=v_1t_v\leftrightarrow \pi=\frac{qB}{m}t_v\leftrightarrow t_v=\frac mq\frac \pi B$$
- Assim vemos que o raio não influencia o tempo, pelo que este tempo para ocorrer inversão do campo é constante.
- De notar que na vida real existem aceleradores em que se atinge energias tão altas que a massa das partículas deixa de ser constante. Aí esta equação deixa de se aplicar e usa-se as equações de Einstein.

---
NOTA: Nesta aula o professor não teve tempo de mostrar o efeito Hall

#em1 #exs_praticos #fisica 