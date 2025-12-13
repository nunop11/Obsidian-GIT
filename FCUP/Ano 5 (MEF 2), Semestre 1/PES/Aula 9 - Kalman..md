    # Previsor e filtro de Kalman
## Sistemas com perturbações
- Na aula anterior vimos como se pode estimar as variáveis de estado de SLITs
- No entanto apenas vimos sistemas **sem perturbações**. Ora, estas perturbações podem ser ruído ou funções determinísticas. De qualquer forma, são algo importante e que temos de saber modelar
- De uma forma geral:
$$\begin{cases}
x(t+1)=Ax(t) + Bu(t) + q(t) \\
y(t)=Cx(t)+Du(t)+r(t)
\end{cases}$$
em que $q(t)$ é **ruído de processo** e $r(t)$ é **ruído de observação** - são as *perturbações*
- Consideramos que as perturbações são sinais desconhecidos que afetam o desempenho do nossos obversador
- Ao considerar as perturbações, a dinâmica do erro de um estimador de Luenberger fica:
$$\tilde{x}(t+1)=(A-LC)\tilde{x}(t) + q(t) - Lr(t)$$

- Queremos ter um erro baixo, logo o problema de projetar um observador pode ser descrito como a minimização do erro. Podemos definir a função de custo a minimizar como
$$V=\sum\limits_{t=1}^{N}\|\tilde{x}(t)\|^{2}=\sum\limits_{t=1}^{N}\tilde{x}(t)^{T} \tilde{x}(t)$$
logo

### EX (motor)
- Este é o exemplo do motor, já usado na aula anterior. Temos um motor descrito pelas variáveis de estado $x_{1},x_{2}$ - posição e velocidade angulares. A saída do motor é a sua posição e a entrada é uma tensão $u(t)$. Temos basicamente um servo
- Agora vamos introduzir uma *perturbação determinística*:
$$\begin{cases}
x_{1}(t+1)=x_{1}(t)+x_{2}(t) \\
x_{2}(t+1)=0.9x_{2}(t)+10u(t)+q(t) \\
y(t)=x_{1}(t)
\end{cases}$$
ou seja:
$$x(t+1)=\begin{pmatrix}1 & 1 \\ 0 & 0.9\end{pmatrix}x(t) + \begin{pmatrix}0 \\ 10\end{pmatrix}u(t) + \begin{pmatrix}0 \\ 1\end{pmatrix}q(t)$$
e temos o observador de Luenberger para $\lambda_{1}=\lambda_{2}=0.81$:
$$\hat{x}(t+1)=A \hat{x}(t) + B u(t) + \begin{pmatrix}0.28 \\ 0.0081\end{pmatrix}\left[y(t) - \begin{pmatrix}1 & 0\end{pmatrix}\hat{x}(t)\right]$$

**Perturbação**
- Consideremos que a perturbação é assim
![[perturbacao degrau.png]]
$$q(t)=\begin{cases}
0 & , & t<200 \\
10 & , & t\ge200
\end{cases}$$
- Sendo que esta perturbação apenas afeta $x_{2}(t)$ esta perturbação consiste em induzir no motor uma velocidade constante igual a 10. Ou seja, na velocidade $x_{2}$ teremos um degrau e na posição teremos uma reta a começar em $t=200$
- Vejamos o que obtemos com o observador de Luenberger básico:
![[sinal com perturbacao degrau - fail de luenberger.png]]
e temos o erro:
![[perturbacao - erros luenberger.png]]
- Apesar da estimação da posição *parecer* bem, vemos que existe em $x_{1}$ e $x_{2}$ uma parte do erro que o observador **nunca** consegue remover - isto vem da perturbação!!!
- O que precisamos de fazer aqui é **remover a perturbação DETERMINÍSTICA**. O modelo de Luenberger consegue lidar bem com ruído branco, mas não com perturbações determinísticas (que não são incluídas no modelo)

## Rejeitar perturbações determinísticas
- Podemos ver a perturbação determinística como a saída de um sistema cuja entrada é um delta de Dirac
![[perturbacao como slit.png]]
- Considerando que a entrada do sistema não afeta diretamente a saída ($D_{q}=0$) podemos escrever no SS:
$$Q(z)=C_{q}(zI_{n_{q}}-A_{q})^{-1}B_{q}$$
e temos o sistema
$$\begin{cases}
x_{q}(t+1)=A_{q}x_{q}(t) \\
q(t)=C_{q}x_{q}(t)
\end{cases}$$
- Notemos que $u(t)=\delta(t)$ logo o termo de $B_{q}$ não aparece fora de $t=0$. Assim, em regime permanente podemos só ignorar esse termo e a entrada em geral - o sistema é *independente*
- Similarmante temos:
$$\begin{cases}
x_{r}(t+1)=A_{r}x_{r}(t) \\
r(t)=C_{r}x_{r}(t)
\end{cases}$$
- Ora, como estes 2 sistemas apenas dependem de si próprios, a única forma de termos um sinal não-ruído (*determinístico*) é se o sistema for instável!!! Se $A_{q},A_{r}$ forem estáveis não deveremos ter nada determinístico

### Reescrever SLIT com perturbações
- Podemos pegar no sistema SLIT com perturbações:
$$\begin{cases}
x(t+1)=Ax(t) + Bu(t) + q(t) \\
y(t)=Cx(t)+Du(t)+r(t)
\end{cases}$$
e escrever:
$$\begin{align*}
\begin{bmatrix}x_{q}(t+1) \\ x_{r}(t+1) \\ x(t+1)\end{bmatrix}&= \begin{bmatrix}A_{q} & \mathbf{0}_{n_{q}\times n_{r}} & \mathbf{0}_{n_{q}\times n_{r}} \\ \mathbf{0}_{n_{r}\times n_{q}} & A_{r} & \mathbf{0}_{n_{r}\times n} \\ C_{q} & \mathbf{0}_{n\times n_{r}} & A\end{bmatrix}\begin{bmatrix}x_{q}(t) \\  x_{r}(t) \\  x(t) \end{bmatrix}+\begin{bmatrix}\mathbf{0}_{n_{q}\times m} \\ \mathbf{0}_{n_{r}\times m} \\ B\end{bmatrix}u(t)\\
y(t)&= \begin{bmatrix}\mathbf{0}_{\ell\times n_{q}} & C_{r} & C\end{bmatrix}\begin{bmatrix}x_{q}(t)\\
x_{r}(t)\\
x(t) \end{bmatrix}+Du(t)
\end{align*}$$

### Modelos de perturbações determinística
Alguns casos de funções de perturbações determinísticas:
- **Degrau** (que é o integral do delta de Dirac) 
$$\begin{cases}
x_{q}(t+1)=x_{q}(t) \\
q(t)=x_{q}(t)
\end{cases}~~\to~~ \begin{cases}
A_{q}=1 \\
A_{c}=1
\end{cases}$$
- **Rampa** (que é duplo integral do delta de Dirac)
$$\begin{cases}
x_{q1}(t+1)=x_{q1}(t) \\
x_{q2}(t+1)=x_{q1}(t)+x_{q2}(t) \\
q(t)=x_{q2}(t)
\end{cases}~~\to~~ \begin{cases}
A_{q}=\begin{pmatrix}1 & 0 \\
1 & 1\end{pmatrix} \\
C_{q}=\begin{pmatrix}0 & 1\end{pmatrix}
\end{cases}$$
- **Sinusoide** com frequência $\omega_{0}$
$$\begin{cases}
x_{q1}(t+1)=\cos\omega_{0}x_{q1}(t) + \sin\omega_{0} x_{q2}(t) \\
x_{q2}(t+1)=-\sin\omega_{0}x_{q1}(t) + \cos\omega_{0}x_{q2}(t) \\
q(t)=x_{q1}(t)+x_{q2}(t)
\end{cases}~~\to~~ \begin{cases}
A_{q}=\begin{pmatrix}\cos\omega_{0} & \sin\omega_{0} \\
-\sin\omega_{0} & \cos\omega_{0}\end{pmatrix} \\
C_{q}=\begin{pmatrix}1 & 1\end{pmatrix}
\end{cases}$$
(em que notemos que $A_q$ tem os valores próprios $e^{\pm j\omega_{0}}$)

### EX (motor)
- Voltemos ao sistema que descreve a posição $x_{1}$ e a velocidade de rotação $x_{2}$ de  um motor:
$$\begin{cases}
x_{1}(t+1)=x_{1}(t)+x_{2}(t) \\
x_{2}(t+1)=0.9x_{2}(t)+10u(t)+q(t) \\
y(t)=x_{1}(t)
\end{cases}$$
em que temos a perturbação determinística:
$$q(t)=\begin{cases}
0 & , & t<200 \\
10 & , & t\ge200
\end{cases}$$
- Temos que $q(t)$ é um degrau. Como vimos acima, então temos o sistema alargado:
$$\begin{cases}
x_{q}(t+1)=x_{q}(t) \\
x_{1}(t+1)=x_{1}(t)+x_{2}(t) \\
x_{2}(t+1)=0.9x_{2}(t)+10u(t)+x_{q}(t) \\
y(t)=x_{1}(t)
\end{cases}$$
e em matrizes:
$$\begin{align*}
\begin{bmatrix}x_{q}(t+1) \\
x_{1}(t+1)\\
x_{2}(t+1) \end{bmatrix} &= \begin{bmatrix}1 & 0 & 0\\
0 & 1 & 1\\
1 & 0 & 0.9\end{bmatrix} \begin{bmatrix}x_{q}(t)\\
x_{1}(t)\\
x_{2}(t) \end{bmatrix}+ \begin{bmatrix}0\\0\\10\end{bmatrix}u(t)\\\\
y(t)&= \begin{bmatrix}0 & 0 & 1\end{bmatrix} \begin{bmatrix} x_{q}(t)\\
x_{1}(t)\\
x_{2}(t) \end{bmatrix}
\end{align*}$$
- Podemos definir o estimador de Luenberger ($\lambda_{1}=\lambda_{2}=\lambda_{3}=0.81$):
$$\small\begin{bmatrix}x_{q}(t+1) \\
x_{1}(t+1)\\
x_{2}(t+1) \end{bmatrix} = \begin{bmatrix}1 & 0 & 0\\
0 & 1 & 1\\
1 & 0 & 0.9\end{bmatrix} \begin{bmatrix}x_{q}(t)\\
x_{1}(t)\\
x_{2}(t) \end{bmatrix}+ \begin{bmatrix}0\\0\\10\end{bmatrix}u(t)+ \begin{bmatrix}0.006859\\ 0.47\\ 0.0613\end{bmatrix} \left(y(t) - \begin{bmatrix}0 & 1 & 0\end{bmatrix} \begin{bmatrix} \hat{x}_{q}(t) \\ \hat{x}_{1}(t) \\ \hat{x}_{2}(t) \end{bmatrix} \right) $$
- Este estimador funcionou muito melhor na simulação:
![[luenberger adaptado para perturbacao - resultados.png]]
Podemos até ver o erro:
![[luenberger adaptado para perturbacao - erros.png]]
- Vemos que agora a performance e quase igual para a posição e para a velocidade. Temos apenas um pico de erro no instante em que o impulso de $q(t)$ é aplicado, algo que nunca poderá ser evitado. Felizmente, este pico é rapidamente eliminado e voltamso a erro nulo.

## Perturbações como processos estocásticos ergódicos
- Isto consiste em representar perturbações $v$ como processos $v(t,\omega)$ em que
    - $v(\cdot,\omega)$ é uma VA (quando $t$ é fixo)
    - $v(t,\cdot)$ é uma realização de $v$, ou seja, a evolução temporal de um evento $\omega$
- Podemos descrever a distribuição destes processos:
    - **Média**: $$\mu_{v}(t)=\mathbb{E}\{v(t)\}=\int_{-\infty}^{+\infty}p_{v(t)}[v(t)]dv(t)$$
    - **Auto-covariância**: $$\begin{align*}\lambda_{vv}(t,s)&= \mathbb{E}\{[v(t)-\mu_{v}(t)][v(s)-\mu_{v}(s)]\}\\&= \mathbb{E} \{v(t)v^{T}(s)\} - \mu_{v}(t)\mu_{v}(s)\end{align*}$$
- Como sabemos, este processo é **estacionário** se $$\mu_{v}(t)=\mu_{v}~~~~~~,~~~~~~ \lambda_{vv}(t,s)=\lambda_{vv}(t-s)=\lambda_{vv}(\tau)$$
- E o processo é **ergódico** se os valores esperados forem iguais às médias temporais no caso assintótico:
$$\begin{align*}
\mu_{v}&= \lim_{N\to\infty}\frac{1}{2N+1}\sum\limits_{t=-N}^{N}v(t)\\
\lambda_{vv}(\tau)&= \lim_{n\to\infty}\frac{1}{2N+1}\sum\limits_{t=-N}^{N}[v(t+\tau)-\mu_{v}][v(t)-\mu_{v}]^{T}
\end{align*}$$
- Temos ainda a seguinte relação entre a covarância $\lambda_{vv}(\tau)$ e a **densidade espectral** $\Phi_{vv}(\omega)$:
$$\begin{align*}
\Phi_{vv}(\omega)&= \sum\limits_{\tau=-\infty}^{+\infty} \lambda_{vv}(\tau)e^{-j\omega\tau}\\
\lambda_{vv}(\tau)&= \frac{1}{2\pi}\int_{-\pi}^{+\pi}\Phi_{vv}(\omega)e^{j\omega\tau}d\omega
\end{align*}$$
- Podemos ver a densidade espectral do processo como a representação da distribuição da sua potência pelas diferentes frequências do espectro

## Estimar estado em SLIT com ruído estocástico
### Ruído estocástico
- Temos um sistema com ruído de processo $q(t)$ e ruído de medição $r(t)$, ambos ruído branco:
$$\begin{cases}
x(t+1)=Ax(t)+Bu(t)+q(t) \\
y(t)=Cx(t)+Du(t)+r(t)
\end{cases}$$
- Neste caso podemos escrever a seguinte matriz de valor esperado:
$$\begin{align*}
&\mathbb{E}\left\{\begin{bmatrix}q(t) \\ r(t)\end{bmatrix} \begin{bmatrix}q^{T}(t-\tau) & r^{T}(t-\tau)\end{bmatrix}\right\}=\\
&= \begin{bmatrix}\mathbb{E}\{q(t)q^{T}(t-\tau)\} & \mathbb{E}\{q(t)r^{T}(t-\tau)\}\\
\mathbb{E}\{r(t)q^{T}(t-\tau)\} & \mathbb{E}\{r(t)r^{T}(t-\tau)\} \end{bmatrix}=\\
&= \begin{cases}
\begin{bmatrix}Q & S\\
S^{T} & R\end{bmatrix} & , & \tau=0\\
\mathbb{0}_{(n+\ell)\times(n+\ell)} & , & \tau\neq0
\end{cases}
\end{align*}$$

### Estimador
- A presença destes ruídos irá afetar a performance do estimador de Luenberger, ficando-se com
$$\tilde{x}(t+1)=(A-LC)\tilde{x}(t)+q(t)-Lr(t)$$
- Ao calcular com dados ou a prever a variância de $q,r$ podemos melhorar o nosso estimador.

### EX (motor)
- Temos que $q(t)$ é um vetor com 2 elementos, representando o seu efeito sob $x_{1}$ e $x_{2}$. Assim:
$$q(t)=\begin{bmatrix}0 \\ q_{1}(t)\end{bmatrix}~~~~
\to~~~~ Q=\mathbb{E}\{q(t)q^{T}(t)\}=\begin{bmatrix}0 & 0 \\ 0 & \mathbb{E}\{q_{1}^{2}(t)\}\end{bmatrix}$$
consideremos variância $4$ logo $Q=\begin{pmatrix}0 & 0 \\ 0 & 4\end{pmatrix}$
- Já no caso de $r(t)$, temos que ele é escalar porque $y(t)$ é escalar. Assim, podemos simplesmente calcular a sua variância:
$$R=\mathbb{E}\{r^{2}(t)\}=\sigma_{r}^{2}$$
consideremos que $\sigma_{r}=50$.

- Usando estes valores e os 4 observadores abaixo (os mesmos 4 estimadores Luenberger da aula passada):
![[ganhos e lambdas luenberger - 4 observadores.png]]
podemos obter os seguintes resultados:
![[luenberger adaptado para perturbacao - 4 observadores.png]]
e podemos fazer zoom numa secção:
![[luenberger adaptado para perturbacao - 4 observadores zoomed.png]]
- Novamente vemos que os estimadores mais rápidos ($\lambda_{i}$ mais próximos de $0$) são muito mais *sensíveis* e instáveis, oscilando muito. Já o observador mais lento (observador 1) teve a melhor performance.

## Dividir o sistema em 2 partes
- Podemos dividir um sistema em 2 partes:
$$\begin{cases}
\begin{cases}
x_{d}(t+1)=Ax_{d}(t)+Bu(t) \\
y_{d}(t)=Cx_{d}(t)+Du(t)
\end{cases} \\\\
\begin{cases}
x_{s}(t+1)=Ax_{s}(t)+q(t) \\
y_{s}(t)=Cx_{s}(t)+r(t)
\end{cases}
\end{cases}$$
- Notemos algumas coisas:
    - O primeiro sistema é um modelo normal SS **sem perturbações**
    - Em $x_{s}$ temos um sistema SS *sem entradas* e **com perturbações**

- Por outras palavras: $x_{d}$ é o **sistema determinístico** *(D - deterministic)* enquanto que $x_{s}$ é o **sistema estocástico** *(S - stochastic)*
    - No primeiro sistema, conseguimos estimar $A,B,C,D$ e com eles conhecer completamente $x_{d},y_{d}$
    - Já $x_{s},y_{s}$ nunca podem ser completamente conenhecidos - $q,r$ são aleatórios.

### Somar os sistemas
- Somamos as 2 equações dos 2 sistemas:
$$\begin{align*}
x_{d}(t+1)+x_{s}(t+1)&= A [x_{d}(t)+x_{s}(t)]+Bu(t)+q(t)\\
y_{d}(t)+y_{s}(t)&= C[x_{d}(t)+x_{s}(t)]+Du(t)+r(t)
\end{align*}$$
e notamos que simplesmente temos um modelo SS com perturbações em que:
$$x(t)=x_{d}(t)+x_{s}(t)$$
- Ou seja, temos um modelo determinístico-estocástico. Vimos então como dividir um sistema nas suas 2 partes.
- Isto quer ainda dizer que podemos ter um sistema em que $x(t)$ tem variáveis de estado determinísticas e variáveis de estado estocásticas, que estimamos e estudamos separadamente!

### EX (motor)
- Esta divisão no caso do sistema do motor resulta na seguinte estimação:
![[dividir sinal em estocastico e deterministico.png]]
- Notamos que a parte estocástica varia menos e fica mais perto do zero - isto é como dividir um sinal nas componentes DC e AC

### Estimar
- Vamos ver como podemos usar esta lógica para estimar um sinal determinístico-estocástico
#### Componente determinística
- Consideremos que podemos medir $y_{d}(t)$ sem qualquer erro. Assim teremos o estimador:
$$\begin{align*}
\hat{x}_{d}(t+1)&= A \hat{x}_{d}(t)+Bu(t) + L[y_{d}(t)-C\hat{x}_{d}(t)-Du(t)]\\
\hat{y}_{d}(t)&= C\hat{x}_{d}(t)+Du(t)
\end{align*}$$
e teremos o erro:
$$\begin{align*}
\tilde{x}_{d}(t+1)&= x(t+1)-\hat{x}(t+1)\\
&= (A-LC) \tilde{x}_{d}(t)
\end{align*}$$
- Como esta componente é não-aleatória, teremos que o erro tende para zero com $t\to\infty$ (se o sistema for estável)

#### Componente estocástica
- Apliquemos o estimador de Luenberger:
$$\begin{align*}
\hat{x}_{s}(t+1)&= A\hat{x}_{s}(t)+L[y_{s}(t) - \hat{x}_{s}(t)]\\
\hat{y}_{s}(t)&= C\hat{x}_{s}(t)
\end{align*}$$
e o erro terá a dinâmica:
$$\begin{align*}
\tilde{x}_{s}(t+1)&= x_{s}(t+1)-\hat{x}_{s}(t+1)\\
&= (A-LC)\tilde{x}_{s}(t) + q(t) - Lr(t)
\end{align*}$$
logo o erro NÃO tende para zero quando $t\to\infty$ por causa dos termos $q(t),r(t)$

#### Juntar as componentes
- Como vimos acima, podemos juntar as 2 componentes num sinal determinístico-estocástico: $$\hat{x}(t)=\hat{x}_{d}(t)+\hat{x}_{s}(t)$$
- E o erro de estimação será:
$$\tilde{x}(t)=\tilde{x}_{d}(t)+\tilde{x}_{s}(t)$$
- Tendo em consta o que vimos acima, teremos que:
$$\lim_{t\to\infty}\tilde{x}(t)=\tilde{x}_{s}(t)$$
Ou seja, ficamos sempre com algum erro - a componente estocástica do sinal (isto é óbvio, mas assim temos isto mostrado com contas)

## Começar Kalman
- Vamos finalmente ver como escolhemos o ganho do estimador. No filtro de Kalman, o nosso objetivo será **minimizar a variância do erro** $\tilde{x}(t)$
- Dizemos que o ganho que minimiza essa variância é $K$ - *Ganho de Kalman*
- Como acabamos de ver, esta minimização reduz-se a minimizar a variância do erro de estimação da *componente estocástica* do sinal, que nunca podemos estimar completamente

### Minimizar raízes
- Antes de ver coisas mais práticas, vamos entender a base matemática disto
- Queremos minimizar a variância. Mas em muitos casos, teremos na realidade uma **matriz de covariância** que queremos MINIMIZAR
- Ora, minimizar uma matriz consiste em minimizar uma norma da matriz pré definida. Alguns exemplos:
    - Norma *induzida*: temos um vetor $x$ compatível com $A$ em forma. O produto $Ax$ irá dar um vetor com combinações lineares de elementos de $A$. Assim, podemos definir a norma a maior norma possível de obter de um produto $Ax$, ou seja, o quando $A$ consegue esticar um vetor $x$. $$\|A\|_{p}=\max\{\|Ax\|_{p} ~;~\|x\|_{p}=1\}$$
    - Norma *máxima*: simplesmente dizemos que a norma da matriz é o valor absoluto do maior elemento $$\|A\|_\max=\max\{|a_{ij}|\}$$
    - Norma de *Frobenius* : é uma espécie de norma euclidiana para matrizes: $$\|A\|_{F}=\sqrt{\sum\limits_{i=1}^{n}\sum\limits_{j=1}^{n}a_{ij}^{2}}=\sqrt{\text{tr}[A^{T}A]}$$

- Ok, vamos ver melhor esta última parte - a função **traço**:
$$\text{traço de }M=\text{tr}(M)=\sum\limits_{i=1}^{n}m_{ii}$$
ou seja, a soma dos elementos da diagonal principal.
- Por definição temos que $A^{T}A$ é uma matriz definida positiva (é o equivalente a ter $x^{2}$). Assim, desde que $M$ seja uma *matriz semidefinida positiva* então podemos usar $\text{tr}(M)$ como uma norma de $M$.
- Saindo de matrizes genéricas, temos que a norma para o filtro de Kalman é:
$$\text{norma Kalman }= \text{tr}(\mathbb{E}\{\tilde{x}_{s}(t)\tilde{x}_{s}^{T}(t\})$$

### Matrizes (semi)definidas positivas e negativas
- Vamos ver só mais este conceito teórico prometo
- Uma matriz $M\in\mathbb{R}^{n\times n}$ é **definida positiva** se tivermos:
$$z^{T}Mz>0 ~~~~,~~~~ \forall z\in\mathbb{R}^{n}~~\text{tal que}~~ z\neq \mathbb{0}_{n}$$
e representamos esta propriedade da matriz como: $M\succ0_{n\times n}$ (podemos usar $>$ mas vou usar o sinal curvo para distinguir do caso escalar)

- Uma matriz $M\in\mathbb{R}^{n\times n}$ é **semidefinida positiva** se tivermos:
$$z^{T}Mz\ge0~~~~,~~~~ \forall z\in\mathbb{R}^{n}~~\text{tal que}~~ z\neq \mathbb{0}_{n}$$
e representamos isso como $M\succeq0_{n\times n}$

- Uma matriz $M\in\mathbb{R}^{n\times n}$ é **definida negativa** se tivermos:
$$z^{T}Mz<0 ~~~~,~~~~ \forall z\in\mathbb{R}^{n}~~\text{tal que}~~ z\neq \mathbb{0}_{n}$$
e representamos esta propriedade da matriz como: $M\prec0_{n\times n}$ (podemos usar $>$ mas vou usar o sinal curvo para distinguir do caso escalar)

- Uma matriz $M\in\mathbb{R}^{n\times n}$ é **semidefinida negativa** se tivermos:
$$z^{T}Mz\le0~~~~,~~~~ \forall z\in\mathbb{R}^{n}~~\text{tal que}~~ z\neq \mathbb{0}_{n}$$
e representamos isso como $M\preceq0_{n\times n}$

#### Propriedades
- Se uma matriz for **definida pos/neg** TODOS os seus valores próprios serão **pos/neg**
- Uma matriz simétrica $M\in\mathbb{R}^{n\times n}$ é *semidefinida pos/neg* se tiver 1+ **valores próprios nulos** e todos os outros sejam **pos/neg**
- Matrizes *definidas* pos/neg são **não singulares**, ou seja, $\det(M)\neq0$
- Matrizes *semidefinidas* pos/neg são **singulares**, ou seja, $\det(M)=0$

- Se tivermos uma matriz definida positiva $M_{1}\succ0$ e uma semidefinida positiva $M_{2}\succeq0$ então teremos $M_{1}+M_{2}\succ0$
- Se tivermos duas matrizes semidefinidas $M_{1}\succeq0,M_{2}\succeq0$ então teremos $M_{1}+M_{2}\succeq0$
    - Estes 2 pontos aplicam-se igualmente para matrizes (semi)definidas negativas

#### Comparar tamanho de matrizes
- Se tivermos 2 matrizes simétricas $M_{1},M_{2}\in\mathbb{R}^{n\times n}$ temos que $M_{1}$ é **maior que** $M_{2}$ se $M_{1}-M_{2}\succ 0_{n\times n}$, sendo que representamos esta relação:
$$M_{1}\text{ maior que }M_{2} \quad\to\quad M_{1}\succ M_{2}$$
    - Podemos repetir isto tudo analogamente para "M1 maior ou igual que M2", "M1 menor que M2" e "M1 menor ou igual a M2"

- Outra coisa a notar: Se tivermos $M_{1},M_{2}\in\mathbb{R}^{n\times n}$ definidas positivas e tivermos $M_{1}\succ M_{2}$ então teremos $\|M_{1}\|>\|M_{2}\|$
    - De forma igual, se tivermos $M_{1}\succeq M_2$ logo $\|M_{1}\|\ge\|M_{2}\|$

### Dedução do ganho de Kalman
- Podemos definir um estimador de Luenberger:
$$\hat{x}(t+1)=A\hat{x}(t)+Bu(t)+K(t) \left[ y(t)-C\hat{x}(t)-Du(t) \right]$$
em que pretendemos determinar uma equação para $K(t)$.
- Como vimos atrás, o nosso objetivo com o filtro de Kalman é minimizar a variância do erro. Ou seja, queremos obter um ganho $K(t)$ que minimize: $$\tilde{P}(t)=\mathbb{E}\{\tilde{x}(t)\tilde{x}^{T}(t)\}$$
- Em regime permante, vimos que o estimador remove a componente determinística do erro, ficando apenas a parte estocástica. Assim, o ganho da equação acima terá de ser o *mesmo* que na equação do sistema estocástico sem entrada:
$$\begin{cases}
\hat{x}_{s}(t+1)=A \hat{x}_{s}(t)+K(t)[y(t)-C\hat{x}_{s}(t)] \\
\hat{y}_{s}(t)=C \hat{x}_{s}(t) 
\end{cases}$$
que pretende estimar o sistema:
$$\begin{cases}
x(t+1)=Ax(t)+Bu(t)+q(t) \\
y(t)=Cx(t)-Du(t) + r(t)
\end{cases}$$

#### "Sistema" do erro
- Podemos definir o erro da saída:
$$\begin{align*}
\tilde{y}_{s}(t)&= y_{s}(t)-\hat{y}_{s}(t)\\
&= y_{s}(t) - C \hat{x}_{s}(t)
\end{align*}$$
- Podemos ainda determinar o erro da estimativa de estado:
$$\begin{align*}
\tilde{x}(t+1)&= x(t+1) - \hat{x}(t+1)\\
&= Ax(t)+Bu(t) + q(t) - \hat{x}(t+1)\\
&= Ax(t)+Bu(t) + q(t) - A \hat{x}(t) - Bu(t) \\
&\quad \quad- K(t)[y(t)-C\hat{x}(t)-Du(t)]\\
&= A[x(t)-\hat{x}(t)]+q(t) - K(t)[y(t)-C \hat{x}(t) - Du(t)]\\
&\text{(regime permanente)}\\
&= A \tilde{x}(t) + q(t) - K(t)[y_s(t)-C \hat{x}_{s}(t)]\\
&= A \tilde{x}(t) + q(t) - K(t)\tilde{y}_{s}(t)
\end{align*}$$
- A passagem a regime permanente consiste em:
    - Considerar que as entradas são nulas
    - Considerar que $x(t)=x_{s}(t)~,~y(t)=y_{s}(t)$, porque a componente determinística desaparece no que toca ao erro

- Definimos 2 variáveis auxiliares:
$$\begin{align*}
\Lambda_{0}(t)&= \mathbb{E}\{\tilde{y}_{s}(t)\tilde{y}^{T}_{s}(t)\}=\mathbb{E}\{\tilde{y}(t)\tilde{y}^{T}(t)\}\in\mathbb{R}^{\ell\times\ell}\\
G(t)&= \mathbb{E}\{[A \tilde{x}(t)+q(t)]\tilde{y}^{T}(t)\}\in \mathbb{R}^{n\times\ell}
\end{align*}$$

- Calculamos o seguinte produto:
$$\begin{align*}
\tilde{x}(t+1)\tilde{x}^{T}(t+1)&= [A \tilde{x}(t) + q(t) - K(t)\tilde{y}(t)][A \tilde{x}(t) + q(t) - K(t)\tilde{y}(t)]^{T}\\
&= [A\tilde{x}(t)+q(t)][A\tilde{x}(t)+q(t)]^{T}-[A \tilde{x}(t)+q(t)]\tilde{y}^{T}(t)K^{T}(t)-\\
&~~~~-K(t)\tilde{y}(t)[A\tilde{x}(t)+q(t)]^{T}+K(t)\tilde{y}(t)\tilde{y}^{T}(t)K^{T}(t)
\end{align*}$$

- A covariância do erro será dada pelo valor esperado deste produto:
$$\small\begin{align*}
\tilde{P}(t+1)&= \mathbb{E} \{\tilde{x}(t+1)\tilde{x}^{T}(t+1)\}\\
&= \mathbb{E}\left\{[A\tilde{x}(t)+q(t)][A\tilde{x}(t)+q(t)]^{T}\right\}-\mathbb{E}\left\{[A \tilde{x}(t)+q(t)]\tilde{y}^{T}(t)\right\}K^{T}(t)-\\
&~~~~-K(t)\mathbb{E}\left\{\tilde{y}(t)[A\tilde{x}(t)+q(t)]^{T}\right\}+K(t)\mathbb{E}\left\{\tilde{y}(t)\tilde{y}^{T}(t)\right\}K^{T}(t)\\
&\text{(variáveis auxiliares)}\\
&= \mathbb{E}\left\{[A\tilde{x}(t)+q(t)][A\tilde{x}(t)+q(t)]^{T}\right\}-G(t)K^{T}(t)-K(t)G^{T}(t) + K(t)\Lambda_{0}(t)K^{T}(t)\\
&= A\mathbb{E}\{\tilde{x}(t)\tilde{x}(t)\}A^{T}+A \mathbb{E}\{\tilde{x}(t)q^{T}(t)\}+\mathbb{E}\{q(t)\tilde{x}^{T}(t)\}A^{T}+\mathbb{E}\{q(t)q^{T}(t)\}-\\
&-G(t)K^{T}(t)-K(t)G^{T}(t) + K(t)\Lambda_{0}(t)K^{T}(t)\\
&= A\tilde{P}(t)A^{T}+A \mathbb{0}_{n\times n}+\mathbb{0}_{n\times n}A^{T}+Q-G(t)K^{T}(t)-K(t)G^{T}(t) + K(t)\Lambda_{0}(t)K^{T}(t)\\
&= A\tilde{P}(t)A^{T}+Q-[G(t)K^{T}(t)-K(t)G^{T}(t)] + K(t)\Lambda_{0}(t)K^{T}(t)\\
\end{align*}$$

#### Definir termo psi 
- Temos um termo entre parenteses retos com uma estrutura interessante. Vamos tentar melhorar isso
- Podemos definir
$$\begin{align*}
\psi(K,t)&= -\mathbb{E}\{\tilde{x}(t+1)\tilde{y}(t)\}\\
&= -\mathbb{E}\left\{[A \tilde{x}(t) + q(t) - K(t)\tilde{y}(t)]\tilde{y}(t)\right\}\\
&= -\mathbb{E}\{[A\tilde{x}(t)+q(t)]\tilde{y}(t)\} +K(t) \mathbb{E}\{\tilde{y}(t)\tilde{y}(t)\}\\
&= K(t)\Lambda_{0}(t) - G(t) ~~~~\in\mathbb{R}^{n\times\ell}
\end{align*}$$
- Tendo isto, podemos calcular:
$$\small\begin{align*}
\psi(K,t)\Lambda_{0}^{-1}(t)\psi^{T}(K,t)&= [K(t)\Lambda_{0}(t) - G(t)]\Lambda_{0}^{-1}(t)[K(t)\Lambda_{0}(t) - G(t)]^{T}\\
&= [K(t)-G(t)\Lambda_{0}^{-1}(t)][K(t)\Lambda_{0}(t)-G(t)]^{T}\\
&= K(t)\Lambda_{0}(t)K^{T}(t)-K(t)G^{T}(t)-G(t)K^{T}(t)+G(t)\Lambda_{0}^{-1}(t)G^{T}(t)
\end{align*}$$
logo podemos escrever:
$$\small G(t)K^{T}(t)+K(t)G^{T}(t)=-\psi(K,t)\Lambda_{0}^{-1}(t)\psi^{T}(K,t)+K(t)\Lambda_{0}K^{T}(t)+G(t)\Lambda_{0}^{-1}(t)G^{T}(t)$$

- Ao substituir na equação de $\tilde{P}(t+1)$ obtemos:
$$\small\tilde{P}(t+1)=A\tilde{P}(t)A^{T}+Q+\psi(K,t)\Lambda_{0}^{-1}(t)\Psi^{T}(K,t)-G(t)\Lambda_{0}^{-1}(t)G^{T}(t)$$

#### Queremos minimizar
- Queremos minimizar $\tilde{P}(t+1)$. Ora, temos que $\psi(K,t)\Lambda_{0}^{-1}(t)\psi^{T}(K,t)\succeq 0_{n\times n}$ logo teremos que
$$\tilde{P}(t+1)\succeq A\tilde{P}(t)A^{T}+Q-G(t)\Lambda_{0}^{-1}(t)G^{T}(t)$$
- Ora, esta parte da equação **não depende do ganho** logo ao determinar o valor de $K$ que minimiza a covariância, simplesmente não usamos estes termos.
- Resta então apenas o termo dos psi's. Como esse termo é *semidefinido positivo*, a solução que nos dá covariância **mínima** é quando este termo é NULO:
$$\begin{align*}
\psi(K,t)\Lambda_{0}^{-1}(t)\Psi^{T}(K,t)&= 0_{n\times n}\\
\psi(K,t)&= 0_{n\times n}\\
K(t)\Lambda_{0}(t)&= G(t)\\\\
K(t)&= G(t)\Lambda_{0}^{-1}(t)
\end{align*}$$

#### Desenvolver os termos finais
- Vamos então desenvolver este termo. Temos:
$$\small\begin{align*}
\Lambda_{0}(t)&= \mathbb{E}\{\tilde{y}(t)\tilde{y}^{T}(t)\}\\
&= \mathbb{E}\left\{ [y_{s}(t)-C\hat{x}_{s}(t)][y_{s}(t)-C\hat{x}_{s}(t)]^{T} \right\}\\
&= \mathbb{E}\left\{ [Cx_{s}(t)+r(t)-C\hat{x}_{s}(t)][Cx_{s}(t)+r(t)-C\hat{x}_{s}(t)]^{T} \right\}\\
&= \mathbb{E}\left\{ [C\tilde{x}(t)+r(t)][C\tilde{x}(t)+r(t)]^{T} \right\}\\
&= \mathbb{E}\{ C\tilde{x}(t)\tilde{x}^{T}(t)C^{T} + C \tilde{x}(t)r^{T}(t)+r(t)\tilde{x}^{T}(t)C^{T}+r(t)r^{T}(t) \}\\
&= C \mathbb{E}\{\tilde{x}(t)\tilde{x}^{T}(t)\}C^{T}+C \mathbb{E}\{ \tilde{x}(t)r^{T}(t) \}+\mathbb{E}\{ r(t)\tilde{x}^{T}(t) \}C^{T}+\mathbb{E}\{r(t)r^{T}(t) \}\\
&= C \tilde{P}(t)C^{T}+C 0_{n\times\ell}+0_{\ell\times n}C^{T}+R\\
&= C\tilde{P}(t)C^{T}+R
\end{align*}$$

- E falta o termo $G(t)$ que fica:
$$\small\begin{align*}
G(t)&= \mathbb{E}\{ [A\tilde{x}(t)+q(t)]\tilde{y}^{T}(t) \}\\
&= \mathbb{E}\{ [A\tilde{x}(t)+q(t)][y_{s}(t)-C\hat{x}_{s}(t)]^{T} \}\\
&= \mathbb{E}\{ [A\tilde{x}(t)+q(t)][Cx_{s}(t)+r(t)-C\hat{x}_{s}(t)]^{T} \}\\
&= \mathbb{E}\{ [A\tilde{x}(t)+q(t)][C\tilde{x}(t)+r(t)]^{T} \}\\
&= \mathbb{E}\{ A \tilde{x}(t)\tilde{x}^{T}(t)C^{T}+A \tilde{x}(t)r^{T}(t)+q(t)\tilde{x}^{T}(t)C^{T}+q(t)r^{T}(t) \}\\
&= A \mathbb{E}\{ \tilde{x}(t)\tilde{x}^{T}(t) \}C^{T}+A \mathbb{E}\{ \tilde{x}(t)r^{T}(t) \} + \mathbb{E}\{ q(t)\tilde{x}^{T}(t) \}C^{T}+\mathbb{E}\{ q(t)r^{T}(t) \}\\
&= A\tilde{P}(t)C^{T}+A0_{n\times\ell}+0_{\ell\times n}C^{T}+S\\
&= A\tilde{P}(t)C^{T}+S
\end{align*}$$

#### Fórmula do ganho!
- Finalmente, temos uma fórmula do ganho de Kalman, que minimiza a covariância do erro:
$$K(t)=[A\tilde{P}(t)C^{T}+S][C\tilde{P}(t)C^{T}+R]^{-1}$$

### Equação de atualizar a covariância do erro
- Vimos acima que:
$$\tilde{P}(t+1)= A\tilde{P}(t)A^{T}+Q-[G(t)K^{T}(t)-K(t)G^{T}(t)] + K(t)\Lambda_{0}(t)K^{T}(t)$$
- Vimos ainda que, no caso em que temos o ganho correto ficamos com a covariância mínima:
$$\begin{align*}
\tilde{P}(t+1)&= \min_{K}[\tilde{P}(t+1)]\\
&= A\tilde{P}(t)A^{T}+Q-G(t)\Lambda_{0}^{-1}(t)G^{T}(t)
\end{align*}$$
- Ora, vimos que neste caso mínimo temos $K(t)=G(t)\Lambda_{0}^{-1}(t)$ logo temos:
$$\tilde{P}(t+1)=A\tilde{P}(t)A^{T}+Q-K(t)[A\tilde{P}(t)C^{T}+S]^{T}$$

## Previsor de Kalman
### Algoritmo
1. Inicializar
    1. Definir $\tilde{x}(0)=\mu_{x}=\mathbb{E}\{ x(0) \}$
    2. Definir $\tilde{P}(0)=\Pi(0)=\mathbb{E}\{ [\hat{x}(0)-\mu_{x}][\hat{x}(0)-\mu_{x}]^{T} \}$
2. Para cada iteração $t=1,2,\dots$ fazer isto
    1. Calcular o ganho do previsor de Kalman: $K(t)=[A\tilde{P}(t)C^{T}+S][C\tilde{P}(t)C^{T}+R]^{-1}$
    2. Atualizar as estimativas de estado e covariância do erro, assim como da saída: $$\begin{align*}\\\hat{x}(t+1)&= A\hat{x}(t)+Bu(t)+K(t)[y(t)-C\hat{x}(t)-Du(t)]\\\tilde{P}(t+1)&= A\tilde{P}(t)A^{T}+Q-K(t)[A\tilde{P}(t)C^{T}+S]^{T}\\\hat{y}(t)&= C\hat{x}(t)+Du(t)\end{align*}$$
- Temos os *inputs* do algoritmo
    - $u(t),y(t)$ - entrada e saída do sistema
    - $\mu_{x}$ - estimativa do estado inicial
    - $\Pi(0)$ - estimativa da covariância da estimativa de estado inicial
    - $Q=\mathbb{E}\{ q(t),q^{T}(t) \}$
    - $S=\mathbb{E}\{ q(t),r^{T}(t) \}$
    - $R=\mathbb{E}\{ r(t),r^{T}(t) \}$
    - $A,B,C,D$ - parâmetros do sistema

- Temos os *outputs* do algoritmo
    - $\hat{x}(t)$ - previsão do estado $x(t)$, feita no instante $t-1$ 
    - $\hat{y}(t)$ - previsão da saída $y(t)$, feita no instante $t-1$
    - $K(t)$ - ganho do previsor de Kalman
    - $\tilde{P}(t)$ - covariância do erro do previsor de kalman

### EX (motor)
- No PPT o professor aplicou o previsor de Kalman ao exemplo do motor acima, com as mesmas matrizes, mesmos $Q,R$, etc
- Observou-se que o filtro é bastante bom e consegue acompanhar sempre o sinal
- Para comprovar o desempenho, foi calculado o erro RMS do previsor de Kalman e dos 4 observadores de Luenberger observados acima. Notou-se que Kalman teve o menor erro para $x_{1}$ e $x_{2}$, batendo o observador 1 (o mais lento e melhor dos 4)
- Também foi feito gráfico do ganho de Kalmane e de componentes da matriz de covariância ao longo das iterações
    - A covariância rapidamente desceu para zero em todos os casos, mostrando que este algoritmo rapidamente se adapta ao sinal em estudo
    - Como a variância desceu rápido, também o ganho desceu. Isto acontece porque ficamos com covariância (AKA incerteza) baixa, ou seja, ficamos com mais confiança nas nossas estimativas de estado. Com o ganho menor estamos a dar *menos importância* a valor de $y(t)$ medidos e que servem para corrigir a estimativa de estado. 

## Modo estacionário
- Após algum tempo a covariância e ganho de Kalman estabilizam, atingindo-se um regime estacionário. 
- A covariância de platteau é dada pela seguinte equação:
$$\tilde{P}=A\tilde{P}A^{T}+Q-(A\tilde{P}C^{T}+S)(C\tilde{P}C^{T}+R)^{-1}(A\tilde{P}C^{T}+S)^{T}$$
- Uma forma de resolver esta equação é o *método de Jacobi*. 
- Também o ganho se torna constante:
$$K=(A\tilde{P}C^{T}+S)(C\tilde{P}C^{T}+R)^{-1}$$

- Também o sistema pode ser escrito na forma estacionária:
$$\begin{cases}
x_{p}(t+1)=Ax_{p}(t)+Bu(t)+Ke(t) \\
y(t)=Cx_{p}(t)+Du(t)+e(t)
\end{cases}$$
em que notemos que o termo do ganho de Kalman consiste num erro da estimativa da saída

## Filtro de Kalman
### Notação
- Num certo instante $t$ temos *mais informação* acerca do estado e sistema do que no instante $t-1$. 
- Ou seja, o erro da estimativa de $x(t)$ que fazemos no instante $t$ é *menor* do que a estimativa feita no instante $t-1$.
- Assim, vamos distinguir estes casos. A estimativa de $x(t)$ feita no instante $t$ é $\hat{x}(t|t)$, enquanto que aquela feita no instante $t-1$ é $\hat{x}(t|t-1)$

### Filtro
$$\hat{x}(t|t)=\hat{x}(t)+K_{f}(t)\tilde{y}(t)$$
- Em que $\hat{x}(t)$ é a previsão de $x(t)$ feita pelo *previsor* de Kalman
- $K_{f}$ é o ganho do *filtro* de Kalman
- $\tilde{y}(t)=y_{s}(t)-C\hat{x}(t)$
- No filtro de Kalman, o ganho irá garantir que $\hat{x}(t|t)$ é a **estimativa optima** de $x(t)$, minimizando a variância do erro desta estimativa.

### Calcular ganho do filtro
- Podemos definir o erro da estimativa do filtro:
$$\begin{align*}
\tilde{x}(t|t)&= x(t)- \hat{x}(t|t)\\
&= x(t)-\hat{x}(t)-K_{f}(t)\tilde{y}(t)\\
&= \tilde{x}(t)-K_{f}(t)\tilde{y}(t)
\end{align*}$$

- Podemos calcular o produto
$$\small\begin{align*}
\tilde{x}(t|t)\tilde{x}^{T}(t|t)&= [\tilde{x}(t)-K_{f}(t)\tilde{y}(t)][\tilde{x}(t)-K_{f}(t)\tilde{y}(t)]^{T}\\
&= \tilde{x}(t)\tilde{x}^{T}(t)-\tilde{x}(t)\tilde{ y}^{T}(t)K_{f}^{T}(t)-K_{f}(t)\tilde{y}(t)\tilde{x}^{T}(t)+K_{f}(t)\tilde{y}(t)\tilde{y}^{t}(t)K_{f}^{T}(t)
\end{align*}$$
e podemos calcular a variância do erro da estimativa $\hat{x}(t|t)$:
$$\small\begin{align*}
\tilde{P}(t|t)&= \mathbb{E}\{ \tilde{x}(t)\tilde{x}^{T}(t) \} - \mathbb{E}\{ \tilde{x}(t)\tilde{y}^{T}(t) \}K_{f}^{T}(t)-K_{f}\mathbb{E}\{\tilde{y}(t)\tilde{x}^{T}(t)\}+K_{f}(t)\mathbb{E}\{ \tilde{y}(t)\tilde{y}^{T}(t) \}K_{f}^{T}(t)\\
&= \tilde{P}(t)-G_{f}(t)K_{f}^{T}(t)-K_{f}(t)G_{f}^{T}(t) + K_{f}(t)\Lambda_{0}(t)K_{f}^{T}(t)\\
&= \tilde{P}(t) - [G_{f}(t)K_{f}^{T}(t)+K_{f}(t)G_{f}^{T}(t)]+K_{f}(t)\Lambda_{0}(t)K_{f}^{T}(t)
\end{align*}$$

- Novamente podemos definir $$\psi_{f}(K_{f},t)=-\mathbb{E}\{ \tilde{x}(t|t)\tilde{y}^{T}(t) \}=K_{f}\Lambda_{0}(t)-G_{f}(t)$$
que, tal como acima, nos dá:
$$\small G_{f}(t)K_{f}^{T}(t)+K_{f}(t)G_{f}^{T}(t)=-\psi_{f}(K_{f},t)\Lambda_{0}^{-1}(t)\psi_{f}^{T}(K_{f},t)+K_{f}(t)\Lambda_{0}K_{f}^{T}(t)+G_{f}(t)\Lambda_{0}^{-1}(t)G_{f}^{T}(t)$$

- Ao substituir na equação da covariância:
$$\tilde{P}(t|t)=\tilde{P}(t)+\psi_{f}(K_{f},t)\Lambda_{0}^{-1}(t)\psi_{f}^{T}(K_{f},t)-G_{f}(t)\Lambda_{0}^{-1}G_{f}^{T}(t)$$

- Mantém-se toda a lógica de acima acerca de igualar a zero o termo do psi para minimizar $\tilde{P}(t|t)$. Ao fazer isso, obtemos novamente o ganho que minimiza:
$$K_{f}(t)=G_{f}(t)\Lambda_{0}^{-1}(t)$$


- Acima vimos que $\Lambda_{0}(t)=C\tilde{P}(t)C^{T}+R$
- Vamos agora deduzir $G_{f}(t)$ **que vai dar diferente!!!!**
$$\begin{align*}
G_{f}(t)&= \mathbb{E}\{ \tilde{x}(t)\tilde{y}^{T}(t) \}\\
&= \mathbb{E}\{ \tilde{x}(t)[y_{s}(t)-C\hat{x}_{s}(t)]^{T} \}\\
&= \mathbb{E}\{ \tilde{x}(t)[Cx_{s}(t)+r(t)-C\hat{x}_{s}(t)]^{T} \}\\
&= \mathbb{E}\{ \tilde{x}(t) [C \tilde{x}(t)+r(t)]^{T} \}\\
&= \mathbb{E}\{ \tilde{x}(t)\tilde{x}^{T}(t) \}C^{T} + \mathbb{E}\{ \tilde{x}(t)r^{T}(t) \}\\
&= \tilde{P}(t)C^{T}+ 0_{n\times\ell}\\
&= \tilde{P}(t)C^{T}
\end{align*}$$
- E temos o ganho do **filtro** de Kalman:
$$K_{f}(t)=\tilde{P}(t)C^{T}[C \tilde{P}(t)+R]^{-1}$$
- E temos a covariância mínima obtida com este ganho:
$$\begin{align*}
\tilde{P}(t|t)&= \tilde{P}(t) - G_{f}(t)\Lambda_{0}^{-1}(t)G^{T}_{f}(t)\\
&= \tilde{P}(t) - \tilde{P}(t)C^{T}[C\tilde{P}(t)C^{T}+R]^{-1}C\tilde{P}^{T}(t)
\end{align*}$$
ora, o segundo termo é **semidefinido positivo**. Logo temos:
$$\tilde{P}(t|t)\preceq \tilde{P}(t)$$
- Logo, pelo menos teoricamente, o filtro de Kalman melhora ou mantém a covariância da estimativa do previsor de Kalman.

### ALGORITMO
1. Inicializar
    1. Definir $\hat{x}(0)=\mu_{x}$
    2. Definir $\tilde{P}(0)=\Pi(0)$
2. Para cada iteração $t=1,2,\dots$ fazer
    1. Calcular os ganhos do previsor e filtro de Kalman: $$\begin{align*}K(t)&= [A\tilde{P}(t)C^{T}+S][C\tilde{P}(t)C^{T}+R]^{-1}\\K_{f}(t)&= \tilde{P}(t)C^{T}[C\tilde{P}(t)C^{T}+R]^{-1}\end{align*}$$
    2. Calcular previsão do previsor e estimativa do filtro para $x,\tilde{P},y$:$$\begin{align*}\hat{x}(t+1)&= A\hat{x}(t)+Bu(t)+K(t)[y(t) - C\hat{x}(t) - Du(t)]\\\hat{x}(t|t)&= \hat{x}(t) + K_{f}(t) [y(t)-C\hat{x}(t) -Du(t)]\\\tilde{P}(t+1)&= A\tilde{P}(t)A^{T}+Q-K(t)[A\tilde{P}(t)C^{T}+S]^{T}\\\tilde{P}(t|t)&= \tilde{P}(t) - K_{f}(t)C\tilde{P}(t)\\\hat{y}(t)&= C\hat{x}(t)+Du(t)\\\hat{y}(t|t)&= C\hat{x}(t|t)+Du(t)\end{align*}$$

- Temos os *inputs* do algoritmo:
    - $u(t),y(t)$ - entrada e saída do sistema
    - $\mu_{x}$ - estimativa do estado inicial
    - $\Pi(0)$ - estimativa da covariância da estimativa de estado inicial
    - $Q=\mathbb{E}\{ q(t),q^{T}(t) \}$
    - $S=\mathbb{E}\{ q(t),r^{T}(t) \}$
    - $R=\mathbb{E}\{ r(t),r^{T}(t) \}$
    - $A,B,C,D$ - parâmetros do sistema

- Temos os *outputs* do algoritmo:
    - $\hat{x}(t)$ - previsão do estado $x(t)$, feita no instante $t-1$ 
    - $\hat{x}(t|t)$ - estimativa do estado $x(t)$, feita no instante $t$
    - $\hat{y}(t)$ - previsão do saída $y(t)$, feita no instante $t-1$
    - $\hat{y}(t|t)$ - estimativa da saída $y(t)$, feita no instante $t$
    - $K(t)$ - ganho do previsor de Kalman
    - $K_{f}(t)$ - ganho do filtro de Kalman
    - $\tilde{P}(t)$ - covariância do erro do previsor de Kalman
    - $\tilde{P}(t|t)$ - covariância do erro do filtro de Kalman

- Claro, neste PPT foi feita distinção entre previsor e filtro. Em algumas fontes simplesmente tratamos a previsão e correção da previsão/estimação como passos distintos.
- Notemos que tudo isto é o mesmo que vi em PMAP, em que as notações correspondem assim:
$$\hat{x}(t)=x^{-}_{t} \quad \quad;\quad \quad \hat{x}(t|t)=x_{t}^{+}$$

### EX (motor)
- No PPT volta-se a aplicar a matéria ao sistema do motor, com tudo igual
- Nos gráficos vemos que o filtro de Kalman tem um ótimo desempenho, parecendo melhor que o previsor
- Para confirmar esta suspeita, calculou-se o erro RMS. E vimos que o Filtro reduz **muito** o erro RMS relativamente a qualquer outro método aplicado neste problema. Mesmo a melhoria de erro do Previsor vs Filtro é maior do que aquela do Previsor VS Observador de Luenberger.
- Notemos ainda uma região do traçado de erro de estimação dos 2 algoritmos:
![[previsor vs filtro kalman.png]]
notemos que quase parece que o previsor apresenta algum "atraso" na estimação da posição do motor ($x_1$). Isto acontece porque, como vimos, o filtro utiliza mais 1 ponto na sua estimação, logo está sempre ligeiramente melhor. Ao longo de um sinal longo esta ligeira melhoria resulta numa grande diferença
- Concluímos que esta diferença de performance entre os algoritmos era previsível. Como provamos acima: $\tilde{P}(t|t)\preceq \tilde{P}(t)$ ou seja, *no pior dos casos* o Filtro tem a *mesma* performance que o Previsor! Claro, na grande maioria dos casos, o filtro será melhor.