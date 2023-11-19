- Equações Diferenciais permitem-nos representar o comportamento de um sistema de forma matemática.
__*EXEMPLO 1*__
![[slit esquema.png]]
- Temos o circuito acima. Pela lei das Malhas temos: $$\begin{align*}
v_{s}(t) - Ri(t)-v_{c}(t)=0\\
v_{s}(t)=Ri(t)+v_{c}(t)
\end{align*}$$
Vemos ainda que no condensador temos, por definição: $$i(t)=C \frac{dv_{c}(t)}{dt}$$
juntando as 2 equações: $$\begin{align*}
v_{s}(t)&= R \cdot C \frac{dv_{c}(t)}{dt}+v_{c}(t)\\
\frac{1}{RC}v_{s}(t)&= \frac{dv_{c}}{dt} + \frac{1}{RC}v_{c}(t)
\end{align*}$$
- Ora, no sistema da figura temos $x(t)=v_{s}(t)~,~y(t)=v_{c}(t)$. Assim temos a equação diferencial que descreve o sistema: $$\frac{dy(t)}{dt} + \frac{1}{RC}y(t)= \frac{1}{RC} x(t)$$
---

- Temos então 2 tipos de Eqs Dif comuns:
    - **Eq Dif Linear** - As derivadas aparecem apenas multiplicadas por coeficientes e combinadas entre si com adições.
    - **Eq Dif com Coeficientes Constante** - Os coeficientes não dependem das variáveis independentes

- A forma geral de uma *eq dif com N coeficientes constantes* é $$\sum\limits_{i=0}^{N}\alpha_{i} \frac{d^{i}y(t)}{dt^{i}} = \sum\limits_{k=0}^{M} \beta_{k} \frac{d^{k}x(t)}{dt^{k}}$$
sendo que, no máximo, o valor máximo de $M$ é $N$. Sabemos ainda que, pare resolver a equação precisamos de $N$ condições iniciais. Na maioria das vezes definimos $M=N$, porque isso não reduz a generalidade da equaçõ.

- Todos os sistemas que podem ser representados como uma eq dif com coeficientes constantes é um **SLIT** - Sistema Linear Invariante no Tempo.

# Diagrama de Blocos
- $\int_{(i)}ydt$ representa o integral repetido $i$ vezes: $$\int_{(i)}ydt=\int_{-\infty}^{t} \left[ \int_{-\infty}^{\tau_{i}} \dots\left[ \int_{-\infty}^{\tau_{2}} y(\tau_{1})d\tau_{1}\right]\dots d\tau_{i-1}\right]d\tau_{i}$$
- Começamos na equação $\sum_{i=0}^{N}\alpha_{i} \frac{d^{i}y(t)}{dt^{i}}=\sum_{k=0}^{N}\beta_{k} \frac{d^{k}x(t)}{dt^{k}}$ e integramos $N$ vezes, de modo a perder todas as derivadas:
$$\begin{align*}
\sum\limits_{i=0}^{N}a_{i}\int_{(i)}ydt&= \sum\limits_{k=0}^{N}b_{k}\int_{(k)}xdt\\
y(t)&= \frac{1}{a_{0}} \left[ \sum\limits_{k=0}^{N}b_{k} \int_{(k)}xdt - \sum\limits_{i=1}^{N}a_{1}\int_{(i)}ydt \right]
\end{align*}$$sendo $a_{i}=\alpha_{N-i}~~;~~b_{k}=\beta_{N-k}$.

__*EXEMPLO 2*__
Temos $\sum_{i=0}^{N}\alpha_{i} \frac{d^{i}y(t)}{dt^{i}}=\sum_{k=0}^{N}\beta_{k} \frac{d^{k}x(t)}{dt^{k}}$. Sendo $N=1$:
$$\begin{align*}
\alpha_{0} \frac{d^{0}y(t)}{dt^{0}} + \alpha_{1} \frac{dy(t)}{dt}&= \beta_{0} \frac{d^{0}x(t)}{dt^{0}}+\beta_{1} \frac{dx(t)}{dt}\\
\alpha_{0}y(t)+\alpha_{1} \frac{dy(t)}{dt}&= \beta_{0}x(t) + \beta_{1} \frac{dx(t)}{dt}\\
&\textsf{Integrar 1 vez:}\\
\alpha_{0}\int y(t)dt+\alpha_{1}\int \frac{dy}{dt}dt &= \beta_{0}\int x(t)+\beta_{1} \int \frac{dx}{dt}dt\\
\alpha_{0}\int y(t)dt + \alpha_{1}y(t) &= \beta_{0}\int x(t)dt + \beta_{1}x(t)\\\\
y(t) = \frac{1}{\alpha_{1}} &\left[ \beta_{0} \int x(t)dt +\beta_{1} x(t) - \alpha_{0}\int y(t)dt \right]
\end{align*}$$
sendo $a_{i}=\alpha_{N-i}~~;~~b_{k}=\beta_{N-k}$ temos $$\begin{cases}a_{0}=\alpha_{1}\\ a_{1}=\alpha_{0}\\ b_{0}=\beta_{1}\\ b_{1}=\beta_{0}\end{cases}$$
- Assim, podemos deduzir a equação de $y(t)$ de outra forma:
$$\begin{align*}
y(t)&= \frac{1}{a_{0}} \left[ \sum\limits_{k=0}^{N} b_{k}\int_{(k)}xdt - \sum\limits_{i=1}^{N} a_{i}\int_{(i)} ydt \right]\\
N=1 \Rightarrow y(t)&= \frac{1}{a_{0}} \left[ b_{0}\int_{(0)}x(t)dt + b_{1}\int_{(1)}x(t)dt - a_{1}\int_{(1)}y(t)dt \right]\\
y(t) &=  \frac{1}{a_{0}}\left[b_{0}x(t) + b_{1}\int x(t)dt - a_{1}\int y(t)dt \right]
\end{align*}$$
- Podemos representar graficamente esta última forma assim:
![[forma direta 1.png]]

## Forma Direta I
- Forma que usa os coeficientes na forma que aparecem na equação diferencial:
$$\sum\limits_{i=0}^{N} \alpha_{i} \frac{d^{i} y(t)}{dt^{i}}=\sum\limits_{k=0}^{N} \beta_{k} \frac{d^{k} y(t)}{dt^{k}}$$
- De notar que aqui temos que fazer $2N$ integrais.

## Forma Direta II
![[forma direta 2.png]]
- Continua a usar os coeficientes do Eq Dif, mas só precisamos de fazer $N$ integrações. É descrita pela equação:
$$\begin{align*} y(t) = \frac1{a_0}\left[\sum_{m=0}^Nb_m\int_{(m)}x(t)\ dt - \sum_{n=1}^Na_n \int_{(n)}\left[\sum_{m=0}^Nb_m\int_{(m)}x(t)\ dt - \sum_{n=1}^Na_n \int_{(n)}\dots\ dt\right]\ dt\right] \end{align*}$$
- Ao trabalhar com diagramas na forma direta II temos de ter atenção aos sinais, que são negativos junto do somatório à esquerda e positivos junto ao somatório à direita.

## Utilização
- Para desenvolver um sistema, começamos com a eq dif, depois fazemos o diagrama de blocos e com ele podemos criar os componentes/blocos.
- Permitem representar o sistema de uma forma mais intutuiva que a Eq Dif.

# Espaço dos Estados
- Consiste em ter um vetor de variáveis internas que determina completamente a evolução do sistema.
- Se a Eq Dif é de ordem $N$, então o espaço de estados será um sistema de $N$ equações de 1ª ordem.
- De notar que as variáveis internas são arbitrárias, porque a Eq Dif descreve a relação entrada-saída, mas não contem infromação sobre o funcionamento interno do sistema.
- Na prática, o sinal de saído é obtido através de uma *combinação linear dos valores das variáveis de estado*.

__*EXEMPLO 3*__
![[slit exemplo.png]]
- Aplicando a lei das malhas e vendo a divisão da corrente temos: 
$$\begin{cases}x(t)-R_{1}i_{1}(t) -u_{L_{1}}(t)-u_{C}(t)=0 \\ u_{C}(t) + u_{L_{2}}(t) + R_{2}i_{2}(t)=0 \\
i_{3}(t)=i_{1}(t)+ i_{2}(t)
 \end{cases}$$

- Sendo $u_{L_{1}},u_{L_{2}},u_{C}$ são potenciais conhecemos as fórmulas:
$$u_{L_{1}}(t)=L_{1} \frac{di_{1}}{dt} \quad;\quad u_{L_{2}}(t)=L_{2} \frac{di_{2}}{dt} \quad;\quad i_{3}(t)=C \frac{du_{C}}{dt}$$
e substituimos isto no sistema e ficamos com:
$$\begin{cases}x(t) - R_{1}i_{1}(t) -L_{1} \frac{di_{1}}{dt} - u_{C}(t)=0\\ u_{C}(t) + L_{2}\frac{di_{2}}{dt} + R_{2}i_{2}(t)=0 \\C \frac{du_{C}}{dt} = i_{1}(t) + i_{2}(t) \end{cases}$$
- E o sinal de saída será a tensão na saída dos terminais de $R_{2}$: $y(t)=-R_{2}i_{2}(t)$.
- Podemos então isolar os termos relacionados com as bobinas e condensador:
$$\begin{cases}
\frac{di_{1}}{dt} = - \frac{u_{C}}{L_{1}} - \frac{R_{1}}{L_{1}}i_{1} + \frac{1}{L_{1}}x\\
\frac{di_{2}}{dt} = - \frac{1}{L_{2}}u_{C} - \frac{R_{2}}{L_{2}}i_{2} \\
\frac{dU_{C}}{dt}= \frac{i_{1}}{C} + \frac{i_{2}}{C}
\end{cases}$$
que podemos escrever de forma matricial:
$$\frac{d}{dt} \begin{bmatrix}i_{1}\\ i_{2}\\ u_{C}\end{bmatrix} = \begin{bmatrix}- \frac{R_{1}}{L_{1}} &0 &- \frac{1}{L_{1}}\\ 0 &- \frac{R_{2}}{L_{2}} &- \frac{1}{L_{2}}\\ \frac{1}{C} & \frac{1}{C} &0 \end{bmatrix} \begin{bmatrix}i_{1}\\ i_{2} \\ u_{C}\end{bmatrix}+\begin{bmatrix} \frac{1}{L_{1}}\\0\\0\end{bmatrix}x$$
- Ora, acima vimos que $y=-R_{2}i_{2}$. Em termos de matrizes isso fica: $$y(t)=\begin{bmatrix}0 &-R_{2} &0\end{bmatrix}\begin{bmatrix}i_{1}\\i_{2}\\ u_{C}\end{bmatrix}$$
### Generalizado
- Tendo um sistema com $M$ entradas e $K$ saídas temos: 
$$\begin{align*}
\frac{d\mathbf{z}}{dt}&= A \mathbf{z}+B \mathbf{x}\\
\mathbf{y} &= C \mathbf{z} + D\mathbf{x}
\end{align*}$$
em que $\mathbf{x}$ é um vetor vertical com $M$ sinais de entrada, $\mathbf{y}$ vetor vertical com $K$ sinais de saída e $\mathbf{z}$ o vetor vertical com as $N$ variáveis de estado.
Temos ainda:
    - $B$ - matriz $N \times M$ - descreve como entrada influencia $\mathbf{z}$
    - $C$ - matriz $K \times N$ - descreve o efeito de $\mathbf{z}$ sobre a saída
    - $D$ -  matriz $K \times M$ - descreve influencia direta de entrada sobre saída
    - $A$ - matriz de estado, $N \times N$

- Se conhecermos o sistema no instante inicial e conhecermos o sinal de entrada entre $t_{0},t$, conseguimos determinar o estado $\mathbf{z}(t)$ em qualquer instante.

### Diagrama de Blocos
![[espaco estados diagrama blocos.png]]

## Mudança de Variável
- Por vezes temos circuitos que são descritos pela mesma SLIT, mas que são compostos por componentes diferentes. Assim, podemos redefinir $z$ tal que $$z=Tz' \quad;\quad T,N \times N$$
- E ficamos com $$\frac{dz'}{dt} = Az'+Bx \quad ;\quad y=Cz'+Dx \quad;\quad \quad\begin{cases}A = T^{-1}AT\\ B=T^{-1}B\\ C=CT\\ D=D\end{cases}$$
## Popriedades de estados
- **Controlável** - um estado $z_{n}$ é controlável se $x_{m}$ afeta diretamente $z_{n}$
- **Observável** - um estado é observável se $z_{n}$ afeta diretamente $y_{k}$

## Propriedades de sistemas
- **Controlável** - um sistema é controlável se todos os seu estados forem controláveis. (pelos seus sinais de entrada)
- **Observável** - um sistema é observável se todos os seu estados forem observáveis. (pelos seus sinais de saída)


# Estrutura Paralela
- Ora, se tivermos $T$ de forma que $A$ se torne *diagonal*, ou seja, de forma a ficarmos com $$A = \begin{bmatrix} \lambda_{1} &0 &0\\ 0 &\lambda_{2} &0\\ 0 &0 &\lambda_{3} \end{bmatrix} \quad \quad \textsf{(no caso de termos um sistema de 3ª ordem)}$$
- Neste caso temos $D=0$, e as variáveis de estado não dependem umas das outras.
- Este tipo de estrutura pode ser representado da seguinte forma:
![[estrutura paralela.png]]

## Propriedades do sistema
- Agora é muito mais simples perceber como identificar se um sistema tem as propriedades.
- Um SLIT escrito na estrutura paralela é:
    - **Controlável** se todas as entradas de $B$ forem não nulas
    - **Observável** se todas as entradas de $C$ forem não nulas
- Podemos entender isto desta forma:
    - Se o elemento $b_{nm}$ da matriz $B$ for nulo, então $z_{n}$ não pode ser controlado a partir de $x_{m}$
    - Se o elemento $c_{kn}$ da matriz $C$ for nulo, então o estado $z_{n}$ já não é obersvável a partir da saída $y_{k}$

__*EXEMPLO*__
![[exemplo espaço estados.png]]
- Comecemos por observar como passamos de um diagrama de blocos para equações diferenciais.
- De seguida passamos para um sitema.
- Consideremos agora que queremos tornar a matriz $A$ diagonal. Comecemos por determinar os seus autovalores: $$\det (A-\lambda I)=0\Leftrightarrow \lambda = -1 \vee \lambda=2$$
    - Para $\lambda=-1$: $$Av= \lambda v \to Av=-v \to -4v_{1}-6v_{2}=-v_{1}\wedge 3v_{1}+5v_{2}=-v_{2} \Rightarrow v_{1}=-2 \wedge v_{2}=1$$
    - Para $\lambda=2$: $$Av=\lambda v \to Av = 2v\to -4v_{1}-6v_{2}=2v_{1}\wedge 3v_{1}+5v_{2}=2v_{2}\Rightarrow v_{1}=-1 \wedge v_{2}=1$$
- Ou seja, os autovetores são uma certa base $\beta$: $$t_{1}=(-2,1)\quad \quad t_{2}=(-1,1)$$
- Assim, a matriz que faz a transformação da base $\beta$ para a base canónica $\kappa$ é: $$T= \begin{bmatrix}-2 &-1 \\1 &1\end{bmatrix}\quad ;\quad T^{-1} = \begin{bmatrix} -1 &-1 \\ 1 &2 \end{bmatrix}$$
- Podemos então fazer a conversão das matrizes $A,B,C,D$:
$$\begin{align*}
\bar A = T^{-1}AT &= \begin{bmatrix}-1 &0\\ 0 &2\end{bmatrix}\\
\bar B = T^{-1}B &= \begin{bmatrix}0 &1\\ 2 &1\end{bmatrix}\\
\bar C = CT &= \begin{bmatrix} -1\\ 1 \end{bmatrix}\\
\bar D = D &= \begin{bmatrix} 0\\0 \end{bmatrix}
\end{align*}$$
- Ao usar estas matrizes o diagrama fica assim:
![[estrutura paralela exemplo.png]]

#sinais #fisica
