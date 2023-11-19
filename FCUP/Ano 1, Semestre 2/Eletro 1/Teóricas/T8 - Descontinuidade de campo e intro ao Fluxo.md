# Eletro 1 - Aula teórica 8 (JAM)
- Para um anel, temos que 
$$\vec E(0,0,z)=\frac{1}{4\pi\varepsilon_0}\frac{Qz}{(R^2+z^2)^{3/2}}\hat z$$
Assim, temos que $E\propto\frac{z}{(R^2+z^2)^{3/2}}$
- Daqui podemos obter a função $f(z)=\frac{z}{(R^2+z^2)^{3/2}}$, que é ímpar. Isto faz sentido, pois confirma que o campo se comporta da mesma forma atrás e à frente do anel
- Ao derivar esta função temos:
$$\frac{df}{dz}=\frac{2z^2-R^2}{(R^2+z^2)^{5/2}}$$
- Daqui (a partir de f'=0), vemos que a função f têm um máximo e um mínimo, respetivamente para $x=\frac{R}{\sqrt 2}$ e $x=-\frac{R}{\sqrt 2}$. Ora, num anel essa será a distância em que o módulo de E será maior.
---

- Como visto antes, num disco temos:
$$\vec E(0,0,z)=\frac{\sigma}{2\varepsilon_0}\biggr[\frac{z}{|z|}-\frac{z}{\sqrt{z^2+r^2}{}}\biggr]$$
- Ora, podemos definir
$$g(z)=\frac{z}{|z|}-\frac{z}{\sqrt{z^2+r^2}}$$
- Ora, $$\frac{dg}{dz}=\frac{-R^2}{(z^r+R^2)^{3/2}}$$
- Assim, vemos que g não tem máximo nem mínimo e que é sempre decrescente. 
- Ao fazer o gráfico, temos:
![[grafico campo disco]]
- Deste modo oncluímo que o máximo hipotético para um campo gerado por um disco seria $\frac{\sigma}{2\varepsilon_0}$
- E assim temos
>$$\large E(0+)-E(0^-)=\frac{\sigma}{\varepsilon_0}$$, que se aplica a todas as distribuições superficiais

- E assim vemos que no disco em si existe uma ==descontinuidade de campo==, em que ele nã está definido.
---

### Plano ilimitado
- Observando melhor o gráfico e a função $g(z)=\frac{z}{|z|}-\frac{z}{\sqrt{z^2+r^2}}$, vemos que se $R\to\infty$, então esta curva se vai achatando cada vez mais, mantendo os pontos para $z=0$ fixos.
- Assim, no caso de $R=\infty$, ou seja, no caso de o campo ser gerado por um **plano ilimitado**, o ==campo é uniforme== para z. Assim,
$$\vec E(0,0,z)_{R\to\infty}=\frac{\sigma}{2\varepsilon_0}\frac{z}{|z|}\hat z$$
- Na prática, este caso nunca se aplica mesmo. Mas existem muitos casos em que ele é uma boa aproximação.
---

## Fluxo
- Imaginesse que temos um campo de temperatura, com 3 linhas de temperatura, assim:
![[campo temp]]
- De notar que o calor flui no sentido da seta.
- Assim, $campo~T=\frac{\Delta T}{\Delta r}$ (T=temperatur; r=posição)
- Temos então 
$$campo~T=-\nabla T$$

### Gradiente (nabla)
- Dá a direção em que ocorre maior variação
- $\nabla < 0$ -- maior variação para valores menores
- $\nabla>0$ -- maior variação para valores maiores

- Com gradiente:
>$$\Huge Escalar\longrightarrow\nabla\longrightarrow Vetorial$$

## Torneira de água
- Imaginemos o exemplo de ter uma torneira com água a correr, porque há diferença de pressão entre dentro e fora da torneira. Vamos ainda assumir que todas as partículas de água se movem com a mesma velocidade.
![[torneira]]
- A água passa por uma certa superfície $\Delta S_2$. Queremos saber o caudal em $\Delta S_1$. Ora, o caudal volumétrico é dado por $Q=\frac{\Delta V}{\Delta t}$.
- Vemos logo que $\Delta S_2=\Delta S_1\cos\theta$ (escrever Delta S2 como se fosse projeção de Delta S1)
- Facilmente concluímos que, num dado intervalo, a última partícula a percorrer o tubo é aquela para que $v=d\Delta t$. 
- Assim, obtemos que $Q=v\cos\theta\Delta S_1$. E portanto, 
$$Q=(\vec v\cdot\hat n)\Delta S_1$$

#em1 #campoE #fluxoE #fisica 