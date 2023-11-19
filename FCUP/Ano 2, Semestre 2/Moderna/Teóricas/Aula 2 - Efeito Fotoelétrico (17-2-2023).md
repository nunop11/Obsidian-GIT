- Na aula anterior, vimos 3 gráficos importantes: $I(V)$, $i(V)$, $V_{0}(f)$
![[I(i) efeito fotoeletrico.png|Gráfico I(i) - Gráfico 1|300]]
![[ii(V) efeito fotoeletrico.png|Gráfico i(V) - Gráfico 2|300]]
![[V0(f) efeito fotoeletrico.png|Gráfico V0 - Gráfico 3|300]]

- Estes retratam o efeito fotoelétrico num circuito do tipo daquele abaixo:
![[Circuito efeito fotoeletrico.png|300]]
- Sendo que temos então
    - $\LARGE I=\frac{\textsf{energia}}{\textsf{área}\times \textsf{tempo}}$, a intensidade da radiação que incide em $C$
    - $\LARGE i=\frac{dq}{dt}$, a intensidade da corrente elétrica que é gerada de $C$ para $A$ 
    - $V$ a diferença de potencial na fonte de tensão
    - $V_{0}$ o _potencial de paragem_, a diferença de potencial que faz com que nenhum eletrão chegue a $A$

## Teoria Ondulatória da Radiação
- Agora iremos usar esta teoria para explicar aquilo que ocorre em cada gráfico.
- De recordar que, nesta teoria, $\LARGE I=\frac{1}{2}\varepsilon_{0}cE^{2}$
#### Gráfico 1
![[I(i) efeito fotoeletrico.png|300]]
- Vemos que aumentar $I$ leva a aumento de $\vec{E}$ (campo elétrico entre C e A). Ora, $\vec{F}=-e \vec{E}=m_{e}\vec{a}=m_{e}\frac{d \vec{v}}{dt}$. Deste modo, a $E_{c}$ do eletrão aumenta, pelo que a sua energia total, $E$, também aumenta.
- Se $E$ aumentar de modo que $E>I$, então temos $\Large E=E_{\textsf{ionização}}$. Assim, há eletrões que são ejetados Quanto maior for $E$, mais eletrões são ejetados.
- Desta forma, $i$ também aumenta. Ou seja, verifica-se a relação $I(i)$ ilustrada no gráfico 1

#### Gráfico 2
![[ii(V) efeito fotoeletrico.png|500]]
- Os eletrões são ejetados. Logo, se aplicarmos uma DDP retardadora (que faça com que atua uma força que "puxe" os eletrões de volta para a placa $C$), esta pode ser alta o suficiente de modo que nenhum eletrão chegue a $A$. Ou seja, existe um _Potencial de Paragem_ ($V_{0}$) tal que $i=0$
- Opostamente, podemos aplicar uma DDP aceleradora que, como o nome indica, acelera os eletrões em direção à placa $A$. Assim, intuitivamente percebemos que irá haver uma certa DDP a partir da qual todos os eletrões ejetados chegam à placa $A$. A corrente então gerada é máxima e não depende da DDP. Essa é a _corrente de saturação_, $\Large i_{s}$  
- E podemos ver que se aumentarmos $I$, $\vec{E}$ aumenta, pelo que aumenta também a energia com que os eletrões são ejetados. No entanto isto __não explica__ porquê que temos o mesmo $V_{0}$ para 2 $I$ diferentes.

#### Gráfico 3
![[V0(f) efeito fotoeletrico.png|300]]
- Empiricamente é verificado que só se verifica efeito fotoelétrico se a frequência $f$ for maior que um valor $f_{0}$, que depende do material.
- No entanto, a teoria ondulatória da radiação diz que o efeito deveria de ocorrer para qualquer $f$, pelo que _o gráfico 3 não está explicado_

- Está ainda por explicar porquê que este efeito é quase instantâneo.

## Teoria Cospuscular da Radiação
- Iremos agora usar esta teoria para explicar os 3 gráficos.
- Nesta teoria, a energia está quantificada sob a forma da fórmula que nos dá a energia de 1 fotão: $\LARGE E_{\gamma}=hf$
- Sendo que, portanto, $\gamma$ é um fotão.
- Assim, segundo Einstein, o efeito fotoelétrico ocorre porque fotões da radiação colidem com os eletrões, de modo que a colisão pode ser descrita pela equação:
$$\LARGE \gamma + \text{e}^{-}_{\text{ligado}}=\text{e}^{-}_{\text{livre}}$$
- Temos que $$I=\frac{\textsf{energia}}{\textsf{área}\times \textsf{tempo}}=\frac{\#\gamma}{\textsf{área}\times \textsf{tempo}}\cdot E_\gamma=\frac{\# \gamma hf}{\textsf{área}\times \textsf{tempo}}$$
#### Gráfico 1
- Assim, se aumentarmos $I$, se aumenta o número de fotões ($\# \gamma$), pelo que aumenta o número de eletrões libertados da placa $C$. Assim aumenta $i$. Ou seja, verifica-se a relação $I(i)$

#### Gráfico 2
- A existência de $V_{0}$ e $i_{s}$ são ambas explicadas pela teoria ondulatória, pelo que elas já estão justificadas.
- A partir da fórmula de $I$ mostrada acima vemos que se $I$ aumentar, $\# \gamma$ aumenta também. No entanto, isto não implica que $\vec{E}$ varie. Assim, temos o mesmo $V_{0}$ para diversos $I$.

#### Gráfico 3
- Se aplicarmos a conservação de energia à colisão do fotão com o eletrão:
$$\begin{align*}
E&=E'\\
E_\gamma+E_{e^{-}_{\textsf{ligado}}} &= E_{e^{-}_{\textsf{livre}}}\\
hf+[E_{ce^{-}}+m_{e}c^{2}+Be] &=E'_{ce^{-}}+m_{e}c^{2}
\end{align*}$$
Sendo que $Be$ é a energia de ligação do eletrão na placa $C$, $E_{ce^{-}}=0$ porque o eletrão está parado na placa $C$. Vemos ainda que os termos $m_{e}c^{2}$ cortam. 
> Recorde-se da aula anterior que, segundo a teoria relativista, para um eletrão: $$E=E_{c}+E_{0}=E_{c}+mc^{2}$$

Fica então:
$$hf=E_{ce^{-}}-Be$$
E podemos reescrever isto como:
$$hf=E_{ce^{-}}+\phi \quad \quad (\phi - \textsf{trabalho de extração do eletrão})$$

- Apliquemos agora a conservação de energia ao movimento do eletrão entre $C$ e $A$. Temos:
$$\begin{align*}
E_C&=E_A\\
eV_{0}+m_{e}c^{2}&=E_{ce^{-}}+m_{e}c^{2}\\
eV_{0}&=E_{ce^{-}} \longrightarrow \Delta V=\Delta E_c
\end{align*}$$
- Tem-se que $hf_{0}=\phi$. Logo, como $hf=E_{ce^{-}}+\phi$ e $E_{ce^{-}}=eV_{0}$ temos:
$$hf=eV_{0}+hf_{0}\leftrightarrow V_{0}=\frac{h}{e}(f-f_{0})$$
- Logo a reta no gráfico 3 tem declive $\LARGE\frac{h}{e}$

### Notas Finais
1. Normalmente os eletrões ejetados têm energia $E$ na gama do $keV$ (kilo-eletron-Volt). Nesse caso, consideramos que o eletrão não é relativista. Isto porque, $m_{e}c^{2}=0.511 \text{ MeV}$
2. O efeito fotoelétrico não ocorre com eletrões livres. Neste caso teríamos:
![[Efeito fotoelétrico em eletrão livre]]
Ora, aqui vemos que se aplicarmos a conservação da energia _e_ a conservação do momento linear a este caso temos: $\LARGE E_{\gamma}=0$, o que não é possível. Assim, temos que este cenário não acontece, ou seja, o efeito fotoelétrico não acontece com eletrões livres.

#moderna #fisica #fotoeletrico