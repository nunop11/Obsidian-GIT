## 3.1 - Intro
- Em mecânica clássica, o movimento de um corpo é definido pela sua posição e velocidades.
- Como já vimos, para descrever e estudar um sistema assim, usamos coordenadas generalizadas $q_{i}(t)$ e as suas derivadas no tempo $\dot{q_{i}}(t)$. O momento conjugado de uma partícula pode ser obtido com $p_{i}=\frac{\partial\mathcal{L}}{\partial\dot{q}_{i}}$.

- Ora, $p,q$ são as variáveis dinâmicas fundamentais de um sistema. Todas as grandezas (energia, momento angular, ...) desse sistema podem ser expressas a partir delas. Por exemplo, o Hamiltoniano $\mathcal{H}(q_{i},p_{i},t)$ representa a energia do sistema e permite-nos estudar a sua evolução com as *equações de Hamilton*:
$$\frac{dq_{i}}{dt}= \frac{\partial\mathcal{H}}{\partial p_{i}} \quad \quad;\quad \quad \frac{dp_{i}}{dt}=-\frac{\partial\mathcal{H}}{\partial q_{i}}$$

- Ou seja, a descrição clássica de sistemas resume-se a:
    - O estado do sistema num instante $t_{0}$ é definido pelas $N$ coordenadas generalizadas $q_{i}(t_{0})$ e respetivos momentos conjugados $p_{i}(t_{0})$
    - Num certo instante, o valor de várias grandezas físicas é completamente determinado pela configuração num instante anterior.
    - A evolução temporal de um sistema é dada pelas equações de Hamilton. Conhecemos a evolução do sistema para sempre, se soubermos o estado inicial.

- Iremos agora ver o caso quântico.

## 3.2 - Postulados da Mecânica Quântica
### 3.2.1 - Descrição do Estado do Sistema
**1º Postulado :** Num certo instante $t_{0}$, o estado de um sistema físico isolado é definido pelo ket $\ket{\psi(t_{0})}\in \mathcal{E}$.

- Este Postulado implica um princípio de sobreposição: uma combinação de vetores de estado do sistema também será um vetor de estado.

### 3.2.2 - Descrição de Grandezas Físicas
**2º Postulado :** Todas as grandezas físicas mesuráveis $\mathcal{A}$ são descritas por um operador $A$ a atuar no espaço de estados $\mathcal{E}$. $A$ será uma observável.

### 3.2.3 - Medição de Grandezas Físicas
#### 3.2.3.1 - Resultados possíveis
**3º Postulado :** O valor medido irá ser sempre um valor próprio de $A$.

- Como $A$ é uma observável, é um operador hermítico, pelo que todos os seus valores próprios (e valores de $\mathcal{A}$ medidos) são **reais**.

#### 3.2.3.2 - Princípio de Decomposição Espectral
- Consideremos um sistema representado por um ket normalizado $\ket{\psi}$
- Como sabemos, o valor de uma grandeza $\mathcal{A}$ terá natureza probabilística. 

*Caso de Espectro Discreto e não degenerado*
- Vamos assumir que o espetro da obsrevável $A$ é discreto.
- Além disso, se considerarmos que nenhum autovalor é degenerado então temos 1 vetor próprio para cada valor próprio: $A\ket{u_{n}}=a_{n}\ket{u_{n}}$.
- Sendo $A$ uma observável, podemos formar uma base de $\mathcal{E}$ com os seus vetores próprios. Assim podemos escrever: $\ket{\psi}=\sum_{n}c_{n}\ket{u_{n}}$.

**4º Postulado (caso de espetro discreto e não degenerado):** Sendo $\ket{\psi}$ um estado normalizado e $A$ a observável associada à grandeza medida, a probabilidade de medir um valor $a_{n}$ é $$\mathcal{P}(a_{n})=|\langle u_{n}|\psi\rangle|^{2}$$em que $a_{n},\ket{u_{n}}$ são um par valor/vetor próprio de $A$.

*Caso com Espetro Discreto com valores degenerados*
- Consideremos agora que alguns valores próprios $a_{n}$ têm grau de degenerescência $g_{n}$ (tendo a eles associados $g_{n}$ vetores próprias). Temos: $A\ket{u_{n}^{i}}=a_{n}\ket{u_{n}^{i}}$ 
- Continuamos a ter uma base de $\mathcal{E}$ formada por vetores próprios de $A$ e podemos representar $\ket{\psi}$: $\ket{\psi}=\sum_{n}\sum_{i=1}^{g_{n}}c_{n}^{i}\ket{u_{n}^{i}}$

**4º Postulado (caso de espetro discreto com valores degenerados):** Sendo $\ket{\psi}$ um estado normalizado e $A$ a observável associada à grandeza medida, a probabilidade de medir um valor $a_{n}$ é $$\mathcal{P}(a_{n})=\sum\limits_{i=1}^{g_{n}}|\langle u_{n^{i}}|\psi\rangle|^{2}$$em que $a_{n}$ é valor próprio de $A$ com grau de degenerescência $g_{n}$, associado aos vetores $\{\ket{u_{n}^{i}}\}$.

- Para este teorema ser sempre correto é preciso que a probabilidade seja independente da escolha da base $\{u_{n}^{i}\}$ escolhida para o subespaço $\mathcal{E_{n}}$. Assim:
$$\ket{\psi_{n}}=\sum\limits_{i=1}^{g_{n}}c_{n}^{i}\ket{u_{n}^{i}}=\sum\limits_{i=1}^{g_{n}}\langle u_{n}^{i}|\psi\rangle\ket{u_{n}^{i}}=\sum\limits_{i=1}^{g_{n}} \ket{u_{n}^{i}}\langle u_{n}^{i}|\psi\rangle=P_{n}\ket{\psi}$$
em que $P_{n}$ é o operador que projeta no subespaço $\mathcal{E_{n}}$ associado a um valor próprio com grau de degenerescência $g_{n}$.
- Podemos escrever a probabilidade acima como $$\mathcal{P}(a_{n})=\sum\limits_{i=1}^{g_{n}}|\langle u_{n}^{i}|\psi\rangle|^{2}=\sum\limits_{i=1}^{g_{n}}|c_{n}^{i}|^{2}=\langle \psi_{n}|\psi_{n}\rangle$$
- Podemos ainda usar o facto que é hermítico ($P^{\dagger}P=P^{2}$) e que $P_{n}$ é um projetor ($P^{2}=P$) para escrever:
$$\mathcal{P}(a_{n})=\langle \psi_{n}|\psi_{n}\rangle=\langle \psi|P^{\dagger}_{n}P_{n}|\psi\rangle=\langle \psi|P_{n}^{2}|\psi\rangle=\langle\psi|P_{n}|\psi\rangle$$
ou seja, qualquer projetor na base $\mathcal{E_{n}}$ irá dar a mesma probabilidade, como pretendido.

*Caso de Espetro contínuo e não degenerado*
- Recordemos que numa base contínua temos:
$$A\ket{v_{\alpha}}=\alpha\ket{v_{\alpha}} \quad \quad;\quad \quad \ket{\psi}=\int d\alpha ~c(\alpha)\ket{v_{\alpha}}$$
- Por o espetro ser contínuo, temos uma *densidade* de probalidade:
$$\rho(\alpha)=|c(\alpha)|^{2}=|\langle v_\alpha|\psi\rangle|^{2}$$

**4º Postulado (caso de espetro contínuo não degenerado):** Sendo $\ket{\psi}$ um estado normalizado e $A$ a observável associada à grandeza medida, a probabilidade de medir um valor no intervalo entre $\alpha$ e $\alpha+d\alpha$ é: $$d\mathcal{P}(\alpha)=|\langle v_{\alpha}|\psi\rangle|^{2}d\alpha$$em que $\alpha$ é valor próprio de $A$ associado ao vetore $\{\ket{v_{\alpha}}\}$.

> **NOTA** - Normalização
> - Devemos notar que, estando $\ket{\psi}$ normalizado também a probabilidade determinado o estará, como podemos provar no caso discreto e contínuo:
> $$\begin{align*}
\sum\limits_{n}\mathcal{P}(a_{n})=\sum\limits_{n}\sum\limits_{i=1}^{g_{n}}|c_{n}^{i}|^{2}=\langle\psi|\psi\rangle&= 1\\
\int d\mathcal{P}(\alpha)=\int |\langle v_{\alpha}|\psi\rangle|^{2}d\alpha=\int \rho(\alpha)d\alpha&= 1
\end{align*}$$
> E podemos establecer equações que nos dão a probabilidade normalizada, mesmo que $\ket{\psi}$ não o esteja:
> $$\mathcal{P}(a_{n})=\frac{1}{\langle\psi|\psi\rangle}\sum\limits_{i=1}^{g_{n}}|c_{n}^{i}|^{2} \quad \quad;\quad \quad \rho(\alpha)=\frac{1}{\langle\psi|\psi\rangle}|c(\alpha)|^{2}$$

**Consequência**
- Vejamos algumas consequências da forma como definimos as probabilidades e os estados.

*1*
- Consideremos que multiplicamos um ket $\ket{\psi}$ por um operador que muda a sua fase: $\ket{\psi}\to \ket{\psi'}=e^{i\theta}\ket{\psi}$. 
- Temos que a se $\ket{\psi}$ está normalizado, também $\ket{\psi'}$ o estará: $\langle \psi'|\psi'\rangle=\langle \psi|e^{-i\theta}e^{i\theta}|\psi\rangle=\langle \psi|\psi\rangle$

*2*
- Consideremos agora que multiplicamos $\ket{\psi'}$ por uma constante: $\ket{\psi}\to\ket{\psi''}=a e^{i\theta}\ket{\psi}$
- Novamente, nada se altera em termos das probabilidades e resultados físicos obtidos. Isto porque nas equações de $P(a_{n}),\rho(\alpha)$ estamos a multiplicar por um termo $a$ no numerador e no denominador, sendo que eles se anulam

*3*
- Temos agora que ter atenção ao combinar coisas. Sim, acabamos de ver que ao fazer $\ket{\psi}\to \ket{\psi'}=e^{i\theta}\ket{\psi}$ temos que $\ket{\psi},\ket{\psi'}$ continuam a representar o *mesmo estado físico*.
- No entanto, se tivermos um estado $\ket{\varphi}=\lambda_{1}\ket{\psi_{1}}+\lambda_{2}\ket{\psi_{2}}$ e aplicarmos a seguinte transformação de fase: $\ket{\varphi}\to \ket{\varphi'}=\lambda_{1}e^{i\theta_{1}}\ket{\psi_{1}}+\lambda_{2}e^{i\theta_{2}}\ket{\psi_{2}}$ em geral teremos que $\ket{\varphi},\ket{\varphi'}$ **não** representam o mesmo estado físico. Apenas teríamos o mesmo caso se $\theta_{1}=\theta_{2}+2n\pi$. Nesse caso ficaria $\ket{\varphi'}=e^{i\theta_{1}}\ket{\varphi}$
- Ou seja, de forma geral, alterar a fase de 1 estado não altera aquilo que ele representa fisicamente. Alterar a fase relativa entre 2+ estados irá  afetar o que representam juntos.

#### 3.2.3.3 - Reduzir o Pacote de Ondas
- Consideremos um caso discreto.
- Queremos medir num certo instante a quantidade $\mathcal{A}$. Consideremos que o estado do sistema mesmo antes da medição é descrito pelo ket $\ket{\psi}$. Como já vimos, o 4º postulado diz-nos as probabilidades de obter cada valor possível. 
- No entanto, ao medir apenas medimos 1 valor. Isto é, não podemos dizer algo tipo "a probabilidade de termos medido X é de Y"; temos 100% de probabilidade de ter medido X, porque já medimos.
- Desta forma, o estado do sistema após a medição terá de ser diferente. Devemos notar que, mesmo que façamos uma segunda medição imediatamente depois da primeira (tão rápido que o sistema não evolui entre medições) iremos sempre obter o mesmo valor.

*Valor não degenerado*´
- Consideremos que se mediu um valor $a_{n}$ não degenerado. Temos algo assim:
$$\ket{\psi}\xRightarrow{(a_{n})} \ket{u_{n}}$$
![[colapso funcao onda.png]]
em que após um certo intervalo o sistema irá evoluir para um estado $\ket{\psi'}$

*Valor degenerado*
- Consideremos agora que medimos $a_{n}$, tendo este um grau de degenerescência $g_{n}$. Já vimos que podemos escrever $\ket{\psi}=\sum_{n}\sum_{i=1}^{g_{n}}c_{n}^{i}\ket{u_{n}^{i}}$
- E ao efetuar uma medição temos:
$$\ket{\psi}\xRightarrow{(a_{n})} \frac{1}{\sqrt{\sum\limits_{i=1}^{g_{n}}|c_{n}^{i}|^{2}}} \sum\limits_{i=1}^{g_{n}}c_{n}^{i}\ket{u_{n}^{i}}$$

*Caso geral*
- Podemos portanto escrever uma equação geral aos 2 casos vistos:
$$\ket{\psi}\xRightarrow{(a_{n})}\frac{P_{n}\ket{\psi}}{\sqrt{\langle \psi|P_{n}|\psi\rangle}}$$

**5º Postulado :** Se ao medir uma grandeza $\mathcal{A}$ num sistema $\ket{\psi}$ obtemos um valor $a_{n}$, o estado do sistema imediatamente a seguir à medição transforma-se na projeção $\frac{P_{n}\ket{\psi}}{\sqrt{\langle \psi|P_{n}|\psi\rangle}}$ de $\ket{\psi}$ no subespaço associado a $a_{n}$.

*Notas*
- Podemos claramente ver que o estado do sistema imediatamente após a medição será um vetor próprio de $A$ com valor próprio $a_{n}$.
- De realçar que, apesar do ponto acima, o estado não passa a ser descrito por qualquer vetor $\in\mathcal{E_{n}}$. Ele passa a ser descrito pela parte de $\ket{\psi_{n}}\in\mathcal{E_{n}}$.

### 3.2.4 - Evolução Temporal
**6º Postulado :** A evolução temporal de um estado $\ket{\psi(t)}$ é dada pela equação de Schrödinger: $$i\hbar\frac{d}{dt}\ket{\psi(t)}=H(t)\ket{\psi(t)}$$em que $H$ é o *operador hamiltoniano* do sistema.

### 3.2.5 - Regras de Quantização
- Vejamos como obter o operador $A$ associado a uma grandeza física $\mathcal{A}$, já definida em mecânica clássica.

#### 3.2.5.1 - Quantificação Canónica
- Consideremos um sistema composto de uma só partícula, sem spin, sujeita a um potencial escalar. 
    - À posição da partícula $\vec{r}(x,y,z)$ temos associado o operador $\vec{R}(X,Y,Z)$.
    - Ao momento da partícula $\vec{p}(p_{x},p_{y},p_{z})$ temos associado o operador $\vec{P}(P_{x},P_{y},P_{z})$

- Como já vimos atrás:
    - Estes 2 operadores comutam entre si: $[R_{i},R_{j}]=[P_{i},P_{j}]=0$ (ou seja, 2 componentes de $\vec{P}$ comutam)
    - O comutadotr de componentes equivalentes é $i\hbar$: $[R_{i},P_{j}]=i\hbar \delta_{ij}$ (e o comutador de componentes perpendiculares é nulo)
- Temos então:
$$\begin{align*}
[q^{i},q^{j}]&= 0\\
[p^{i},p^{j}]&= 0\\
[q^{i},p^{j}]&= i\hbar\delta_{ij}
\end{align*}$$

- Podemos expressar qualquer grandeza de um sistema em função das variáveis dinâmicas fundamentais posição e momento. Assim, podemos dizer: $$A(t)=\mathcal{A}(\vec{R},\vec{P},t)$$
- Mas isto tem alguma ambiguidade. Na expressão da grandeza $\mathcal{A}$ podemos ter:
$$\begin{align*}
\vec{r}\cdot\vec{p}&= xp_{x}+yp_{y}+zp_{z}\\
\vec{p}\cdot\vec{r}&= p_{x}x+p_{y}y+p_{z}z
\end{align*}$$
em que temos comutatividade do produto escalar.
- No entanto se aqui substituirmos os operadores $\vec{R},\vec{P}$ temos $\vec{R}\cdot\vec{P}\neq\vec{P}\cdot\vec{R}$. Além disso, nenhum destes operadores resultantes do produto é hermítico: $(\vec{R}\cdot\vec{P})^{\dagger}=\vec{P}\cdot\vec{R}$ (logo não são observáveis)

- Para isso introduzimos uma **regra de simetrização**: $\frac{1}{2}(\vec{R}\cdot\vec{P}+\vec{P}\cdot\vec{R})$.

**REGRA SIMETRIZAÇÃO:** 
Na equação da grandeza $\mathcal{A}$ devidamente "simetrizada" (isto é uma palavra?), substuimos $\vec{r},\vec{p}$ pelos operadores $\vec{R},\vec{P}$.

- Temos excepções: grandezas que apenas existem no lado quântico; não têm equivalente clássico, sendo que usamos diretamente a sua aobservável. Este é o caso do Spin.

#### 3.3.5.2 - Exemplos
**Hamiltoniano de 1 partícula em potencial escalar**
- No clássico temos:
$$\mathcal{H}(\vec{r},\vec{p})=\frac{\vec{p}^{~2}}{2m}+V(\vec{r}) \quad \quad;\quad \vec{p}=m \frac{d\vec{r}}{dt}$$

- Não precisamos de "simetrizar" a equação: nenhum dos termos da equação de $\mathcal{H}$ envolve produtos que comutem operadores.
- Simplesmente escrevemos:
$$H = \frac{\vec{P}^{2}}{2m}+V(\vec{R})$$

**Hamiltoniano de 1 partícula em potencial vetorial**
- No clássico isto é o caso do campo EM e temos:
$$\mathcal{H}(\vec{r},\vec{p})=\frac{1}{2m}[\vec{p}-q \vec{A}(\vec{r},t)]^{2} + qU(\vec{r},t) \quad\quad;\quad \vec{p}=m \frac{d\vec{r}}{dt} + q\vec{A}(\vec{r},t)$$
- Novamente, não temos nenhum produto entre operadores. Assim:
$$H(t)=\frac{1}{2m}[\vec{P}-\vec{A}(\vec{R},t)]^{2}+V(\vec{R},t) \quad \quad;\quad V(\vec{R},t)=qU(\vec{R},t)$$
- Neste sistema é preciso ter atenção que $\vec{p}\neq m\vec{v}$, em que o primeiro é identificado acima e é o momento/momento conjugado de $\vec{r}$. O segundo é o momento mecânico da partícula.

## 3.3 - Interpretação Física dos Postulados
### 3.3.1 - Regras de Quantização e Interpretação Probabilística
- Consideremos o caso 1D na direção $x$.
- Temos uma partícula um estado normalizado $\ket{\psi}$. Tal como vimos acima, a probabilidade de fazer uma medição da posição da partícula e obter um valor entre $x$ e $x+dx$ será:
$$d\mathcal{P}(x)= |\langle x|\psi\rangle|^{2}dx$$
em que $\ket{x}$ será o vetor próprio do operador $X$ com valor $x$.

- Temos ainda que à obersvável $P$ corresponde o vetor próprio $\ket{p}$ com valor $p$, a que está associada a onda plana:
$$\langle x|p\rangle=\frac{1}{\sqrt{2\pi\hbar}}e^{\frac{ipx}{\hbar}}$$

Ora, esta onda está associada a um momento bem definido $p$ e temos que a probabilidade de medir um momento entre $p$ e $p+dp$ é:
$$d\mathcal{P}(p)=|\langle p|\psi\rangle|^{2}dp=|\tilde \psi(p)|^{2}dp$$
- Muito honestamente não percebi a ligação entre estas coisas.

### 3.3.2 - Quantização de Grandezas Físicas
- O 3º Postulado explica a quantização de algumas grandezas (energia por exemplo). Mas o 3º postulado não *obriga* a que todas as grandezas sejam quantizadas. Para saber se uma grandeza é ou não quantizada temos que analisar o problema.
- Um exemplo é o átomo de hidrogénio que veremos mais à frente. Começamos pelo potencial de Coulomb, que é contínuo. E eventualmente determinamos que o espetro do Hamiltoniano é discreto, pelo que temos energia quantizada!

### 3.3.3 - Processo de Medição
- Na realidade temos uma série de fatores que afetam a medição e que não iremos considerar: por exemplo, a própria interação entre o intrumento de medida e o sistema.
- Aqui iremos assumir "medições ideais", ou seja, vamos considerar que o instrumento de medição não tem imperfeições e não afeta o sistema.

### 3.3.4 - Valor médio de uma observável
- As previsões do 4º postulado são probabilísticas. Isto implica que para as comprovar por completo teríamos de fazer $N$ de medições, em $N$ sistemas idênticos, todos no mesmo estado. Consoante $N\to\infty$ os valores medidos deverão descrever a teoria prevista pela teoria. Mas isto é obviamente impraticável. Assim temos que fazer estudo estatístico.

- O valor médio de uma observável $A$ num estado $\ket{\psi}$ será indicado como $\langle A\rangle_{\psi}$. Vamos demonstrar que:
$$\langle A\rangle_{\psi}=\langle \psi|A|\psi\rangle$$

- Consideremos que fazemos $N$ medições de sistemas no estado $\ket{\psi}$. Medimos o valor $a_{n}$ em $\mathcal{N}(a_{n})$ medições. Ou seja: $$\frac{\mathcal{N}(a_{n})}{N}\xrightarrow{~~(N\to\infty)~~}\mathcal{P}(a_{n})$$
pelo que o valor médio dos $N$ ensaios será: $\frac{1}{N}\sum_{n}a_{n}\mathcal{N}(a_{n})$. No limite $N\to\infty$ temos:
$$\begin{align*}
\langle A\rangle_{\psi}&= \sum\limits_{n}a_{n}\mathcal{P}(a_{n})\\
&= \sum\limits_{n}a_{n}\sum\limits_{i=1}^{g_{n}}\langle \psi|u_{n}^{i}\rangle\langle u_{n}^{i}|\psi\rangle\\
&= \sum\limits_{n}\sum\limits_{i=1}^{g_{n}}\langle \psi|(a_{n}|u_{n}^{i}\rangle)\langle u_{n}^{i}|\psi\rangle\\
&= \sum\limits_{n}\sum\limits_{i=1}^{g_{n}}\langle \psi|A|u_{n}^{i}\rangle\langle u_{n}^{i}|\psi\rangle\\
&= \langle\psi|A \left[\sum\limits_{n}\sum\limits_{i=1}^{g_{n}}|u_{n}^{i}\rangle\langle u_{n}^{i}|\right]|\psi\rangle\\
&= \langle \psi|A|\psi\rangle
\end{align*}$$
e demonstrou-se a relação indicada. Podemos fazer uma demosntração análoga para o caso contínuo.

- De notar que $\langle A\rangle$ é a média ao longo de vários ensaios, não a média ao longo do tempo.
- A versão da equação do valor médio para um estado não normalizado é $\langle A\rangle_{\psi}=\frac{\langle\psi|A|\psi\rangle}{\langle\psi|\psi\rangle}$
- Normalmente passamos para uma base para determinar o valor médio:
$$\begin{align*}
\langle X\rangle_{\psi}&= \langle \psi|X|\psi\rangle\\
&= \int d^{3}r~ \langle \psi|\vec{r}\rangle\langle \vec{r}|X|\psi\rangle\\
&= \int d^{3}r~ \psi^{*}(\vec{r})~ x ~\psi(\vec{r})
\end{align*}$$
$$\begin{align*}
\langle P_{x}\rangle_{\psi}&= \langle \psi|P_{x}|\psi\rangle\\
&= \int d^{3}r~ \langle \psi|\vec{r}\rangle \langle \vec{r}|P_{x}|\psi\rangle\\
&= \int d^{3}r~ \psi^{*}(\vec{r})~\frac{\hbar}{i}\frac{\partial}{\partial x}\psi(\vec{r})
\end{align*}$$

### 3.3.5 - Desvio Padrão / Variância
- A média $\langle A\rangle$ indica-nos a ordem de grandeza dos valores $\mathcal{A}$ que deveremos medir. Mas este valor não nos diz nada sobre a dispersão dos resultados.

- Assim, para determinar a dispresão dos valores de $\mathcal{A}$ fazemos a média dos quadrados da diferença entre cada valor medido e a média:
$$\Delta A = \sqrt{\langle(A-\langle A\rangle)^{2}\rangle}=\sqrt{\langle \psi|(A-\langle A\rangle)^{2}|\psi\rangle}$$
e temos:
$$\begin{align*}
\langle (A-\langle A\rangle)^{2}\rangle&= \langle A^{2} - 2A\langle A\rangle + \langle A\rangle^{2}\rangle\\
&= \langle A^{2}\rangle - 2\langle A\rangle^{2} + \langle A\rangle^{2}\\
&= \langle A^{2}\rangle-\langle A\rangle^{2}
\end{align*}$$
ou seja:
$$\Delta A=\sqrt{\langle A^{2}\rangle-\langle A\rangle^{2}}=\sigma_{A}$$
a que também podemos chamar desvio padrão de $A$. A sua variância será $\sigma_{A}^{2}$.

- Aqui surgem as famosas relações de Heisenberg:
$$\Delta X\Delta P_{x}\ge \frac{\hbar}{2} \quad;\quad \Delta Y\Delta P_{y}\ge \frac{\hbar}{2} \quad;\quad\Delta Z\Delta P_{z}\ge \frac{\hbar}{2}$$

### 3.3.6 - Princípio de Incerteza e Compatibilidade (MC)
- Acabamos de definir a variância do valor medido de uma observável:
$$\sigma^{2}_{A}=\langle A^{2}\rangle-\langle A\rangle^{2}$$
- Para um estado $\ket{\psi}$ temos:
$$\begin{align*}
\sigma_{A}^{2}&= \langle \psi|(A-\langle A\rangle)^{2}|\psi\rangle\\
&= \underbrace{\langle \psi|(A-\langle A\rangle)}_{\bra{f}}\underbrace{(A-\langle A\rangle)|\psi\rangle}_{\ket{f}}\\
&= \langle f|f\rangle
\end{align*}$$
- Se considerarmos um operador $B$ , também no estado $\ket{\psi}$, podemos definir:
$$\sigma_{B}^{2}=\langle g|g\rangle \quad \quad;\quad \quad \ket{g}=(B-\langle B\rangle)\ket{\psi}$$
- Podemos então escrever:
$$\sigma_{A}^{2}\sigma_{B}^{2}=\langle f|f\rangle\langle g|g\rangle$$
usando a desigualdade de Schwarz ($|\vec{u}||\vec{v}|\ge |\vec{u}\cdot\vec{v}|$):
$$\sigma_{A}^{2}\sigma_{B}^{2}\ge |\langle f|g\rangle|^{2}=z^{2}$$

> Para qualquer número complexo podemos escrever $|z|^{2}=(\text{Re}(z))^{2}+(\text{Im}(z))^{2}\ge (\text{Im}(z))^{2}$. Ora, a parte imaginária pode ser obtida com: $\text{Im}(z)=\frac{z-z^{*}}{2i}$.

- Podemos então escrever:
$$\sigma_{A}^{2}\sigma_{B}^{2}\ge \left(\frac{\langle f|g\rangle-\langle g|f\rangle}{2i}\right)^{2}$$

- Vamos agora calcular $\langle f|g\rangle$:
$$\begin{align*}
\langle f|g\rangle&= \langle\psi|(A-\langle A\rangle)(B-\langle B\rangle)|\psi\rangle\\
&= \langle\psi|(AB-A\langle B\rangle-\langle A\rangle B+\langle A\rangle\langle B\rangle)|\psi\rangle\\
&= \langle \psi|AB|\psi\rangle - \langle A\rangle\langle B\rangle - \langle A\rangle\langle B\rangle + \langle A\rangle \langle B\rangle\\
&= \langle AB\rangle-\langle A\rangle\langle B\rangle
\end{align*}$$
logo
$$\langle g|f\rangle=\langle f|g\rangle^{*}=\langle BA\rangle-\langle B\rangle\langle A\rangle$$
- E temos então:
$$\langle f|g\rangle-\langle g|f\rangle=\langle [A,B]\rangle$$
- Ou seja, temos:
$$\boxed{\sigma_{A}^{2}\sigma_{B}^{2}\ge \left(\frac{\langle[A,B]\rangle}{2i}\right)^{2}}$$
e esta é a forma geral do **_Princípio de Incerteza_**.

- Temos então que:
*Grandezas Compatíveis* - Quando $[A,B]=0$. Neste caso teoricamente podemos determinar as 2 grandezas $\mathcal{A,B}$ com precisão arbitrária.
*Grandezas Incompatíveis* - O contrário de acima.

#### EXEMPLO
- Consideremos agora $A=X,B=P$.Temos:
$$\begin{align*}
[X,P]\psi(x)&= \frac{\hbar}{i} \left[x \frac{d\psi}{dx}-\frac{\partial}{\partial x}(x\psi)\right]\\
&= \frac{\hbar}{i} \left[x\frac{d\psi}{dx} - \psi - x\frac{d\psi}{dx}\right]\\
&= -\frac{\hbar}{i}\psi=i\hbar\psi
\end{align*}$$
ou seja:
$$[X,P]=i\hbar$$
- Substituindo no princípio de incerteza:
$$\sigma_{X}^{2}\sigma_{P}^{2}\ge\frac{\hbar}{2}$$

## 3.4 - Implicações da Eq. Schrödinger
$$i\hbar \frac{d}{dt}\ket{\psi(t)}=H(t)\ket{\psi(t)}$$
### 3.4.1 - Propriedades da Equação
#### 3.4.1.1 - Determinismo da evolução temporal
- Conhecendo-se o estado inicial do sistema $\ket{\psi(t_{0})}$ toda a sua evolução temporal é determinada pela equação de Schrödinger. 
- O comportamente não deterministico apenas surge ao efetuar medições. Ora, entre 2 medições, o sistema comporta-se de uma forma perfeitamente deterministica.

#### 3.4.1.2 - Princípio de Sobreposição
- A equação de Schrödinger é linear e homogénea.
- Na prática, isto significa que: $$\ket{\psi(t_{0})}=\lambda_{1}\ket{\psi_{1}(t_{0})}+\lambda_{2}\ket{\psi_{2}(t_{0})} \to \ket{\psi(t)}=\lambda_{1}\ket{\psi_{1}(t)}+\lambda_{2}\ket{\psi_{2}(t)}$$

#### 3.4.1.3 - Conservação de Probabilidade
**Norma do vetor é conservada**
- Temos:
$$\frac{d}{dt}\langle \psi(t)|\psi(t)\rangle= \left[\frac{d}{dt}\bra{\psi(t)}\right]\ket{\psi(t)}+\bra{\psi(t)}\left[\frac{d}{dt}\ket{\psi(t)}\right]$$
podemos substituir a equação de Schrodinger na 2ª derivada:
$$\frac{d}{dt}\langle \psi(t)|\psi(t)\rangle= \left[\frac{d}{dt}\bra{\psi(t)}\right]\ket{\psi(t)}+ \frac{1}{i\hbar} \langle \psi(t)|H(t)|\psi(t)\rangle$$
- Podemos ainda tomar os conjugado hermíticos dos 2 lados da equação de Schrödinger:
$$\begin{align*}
i\hbar\frac{d}{dt}\ket{\psi}&= H\ket{\psi}\\
&\downarrow\\
\frac{d}{dt} \bra{\psi}&= \frac{-1}{i\hbar} \bra{\psi(t)}H^{\dagger}=\frac{-1}{i\hbar} \bra{\psi(t)}H
\end{align*}$$
e podemos também substituir:
$$\frac{d}{dt}\langle \psi(t)|\psi(t)\rangle= - \frac{1}{i\hbar} \langle \psi(t)|H\ket{\psi(t)}+ \frac{1}{i\hbar} \langle \psi(t)|H(t)|\psi(t)\rangle=0$$
ou seja, a equação de Schödinger implica que **a norma não varia ao longo do tempo**.

- Isto implica ainda que:
$$\langle \psi(t)|\psi(t)\rangle=\langle \psi(t_{0})|\psi(t_{0})\rangle=1$$

**Conservação Local de Probabilidade**
- Consideremos o sistema de 1 partícula sem spin.
- Estando a função de onda $\psi(\vec{r},t)$ normalizada temos a densidade de probabilidade:
$$\rho(\vec{r},t)=|\psi(\vec{r},t)|^{2}$$
pelo que, num instante $t$, a probabilidade de encontrar a partícula no volume infinitesimal $d^{3}r$ centrado em $\vec{r}$ é:
$$d\mathcal{P}(\vec{r},t)=\rho(\vec{r},t)d^{3}r$$
- Acima mostramos que a integral de $\rho$ em todo o espaço é constante no tempo. Mas $\rho$ não tem que ser constante no tempo em todos os pontos.

- A situação aqui presente é análoga à conservação de carga em EM: Num volume $V$ temos inicialmente uma quantidade de carga $Q$. Consideremos que num certo tempo $t$ a carga dentro de $V$ varia em $dQ$. Ora, a variação da carga dentro do volume terá que ser igual àquela que sai ou que entra no volume através da sua superfície $S$. Tudo isto é expresso pela equação: $$\frac{\partial}{\partial t}\rho(\vec{r},t)=-\nabla \cdot \vec{\mathcal{J}}(\vec{r},t)$$

- Ora, considerando que a partícula se encontra num potencial escalar (o hamiltoniano é do tipo $H=\frac{\vec{P}^{2}}{2m}+V(\vec{R},t)$), conseguimos deduzir (Cohen) da equação de Schrödinger a corrente de probabilidade:
$$\vec{\mathcal{J}}(\vec{r},t)=\frac{\hbar}{2mi}[\psi^{*}\nabla\psi-\psi\nabla\psi^{*}]= \frac{1}{m} \text{Re}\left[\psi^{*}\left(\frac{\hbar}{i}\nabla\psi\right)\right]$$
e podemos ainda determinar:
$$\nabla \cdot \vec{\mathcal{J}}=\frac{\hbar}{2mi}[\psi^{*}\Delta\psi-\psi\Delta\psi^{*}]$$
**_Exemplo_**
- Consideremos uma função de onda que descreve uma onda plana $\psi(\vec{r},t)=A e^{i(\vec{k}\cdot\vec{r}-\omega t)}$
- Podemos calcular 
$$\begin{align*}
\psi=Ae^{i(\vec{k}\cdot\vec{r}-\omega t)} ~~&;~~\psi^{*}=Ae^{-i(\vec{k}\cdot\vec{r}-\omega t)} ~~;~~ \psi\cdot\psi^{*}=|A|^{2}
\\\\
\nabla \psi&= \nabla (A e^{i k_{x}x}e^{i k_{y}y}e^{i k_{z}z}e^{-i\omega t})\\
&= \left(ik_{x} \psi,ik_{y}\psi,ik_{z}\psi \right)\\
&= i\vec{k}\psi\\
\\
\nabla\psi^{*}&= -i\vec{k}\psi^{*} 
\end{align*}$$
E podemos determinar:
$$\begin{align*}
\vec{\mathcal{J}}(\vec{r},t)&= \frac{\hbar}{2mi}(\psi^{*}\nabla\psi - \psi\nabla\psi^{*})\\
&= \frac{\hbar}{2mi} (\psi^{*}\cdot i\vec{k}\psi + \psi\cdot i\vec{k}\psi^{*})\\
&= |A|^{2}\frac{\hbar \vec{k}}{m}\\
---&------\\
&= \frac{1}{m} \text{Re} \left[ \psi^{*} \cdot \frac{\hbar}{i}\nabla \psi \right]\\
&= \frac{1}{m}\text{Re}\left[\psi^{*}\cdot \frac{\hbar}{i}\cdot i\vec{k}\psi\right]=\\
&= |A|^{2}\frac{\hbar \vec{k}}{m}
\end{align*}$$
em que mostramos a igualdade das 2 equações.
- Temos ainda que podemos reescrever a corrente de probabilidade como $$\vec{\mathcal{J}}=\rho(\vec{r},t)\vec{v}_{G}$$em que $\rho(\vec{r},t)=|\psi(\vec{r},t)|^{2}=|A|^{2}$ e $\vec{v}_{G}=\frac{\hbar\vec{k}}{m}$ é a velocidade de grupo. Ou seja, a corrente tem mesmo as unidades corretas: "probabilidade" que passa por unidade de área e por unidáde de tempo para fora do volume em estudo.

#### 3.4.1.4 - Evolução de valor médio
- Como já vimos, $\langle A\rangle(t)=\langle \psi(t)|A|\psi(t)\rangle$.
- É possível deduzir (Cohen) que este valor evolui da seguinte forma:
$$\boxed{\frac{d}{dt}\langle A\rangle= \frac{1}{i\hbar}\langle[A,H(t)]\rangle+\langle\frac{\partial A}{\partial t}\rangle}$$
em que naa mecânica clássica temos $\frac{df}{dt}=\frac{\partial f}{\partial t}+\{H,f\}$
- Ou seja, se o operador associado a uma grandeza física comutar com $H$ e não depender explicitamente do tempo então o seu valor médio é constante.
- Se aplicarmos esta equação aos operadores momento e posição obtemos (este é o teorema de Ehrenfest):
$$\begin{align*}
\frac{d}{dt}\langle\vec{R}\rangle &= \frac{1}{m}\langle\vec{P}\rangle\\
\frac{d}{dt}\langle\vec{P}\rangle &= - \langle\nabla V(\vec{R})\rangle
\end{align*}$$
(em que $[\vec{R},\frac{\vec{P}^{2}}{2m}]=\frac{i\hbar}{m}\vec{P}~,~[\vec{P},V(\vec{R})]=-i\hbar\nabla V(\vec{R})$)

**Princípio de Incerteza**
- Assim, tendo um operador $A$ que não depende do tempo, do princípio de incerteza temos:
$$\begin{align*}
\sigma_{A}^{2}\sigma_{H}^{2} \ge \left(\frac{1}{2i}\langle[A,H]\rangle\right)^{2}&= \left(\frac{1}{2i}i\hbar \frac{d}{dt}\langle A\rangle\right)^{2}= \left(\frac{\hbar}{2}\right)^{2} \left(\frac{d\langle A\rangle}{dt}\right)^{2}
\end{align*}$$
- Como o Hamiltoniano consiste na energia do sistema, podemos definir $\Delta E=\sigma_{H}$
- Podemos definir $\Delta t$, o tempo que o valor médio de $A$ demora a mudar em 1 desvio padrão: $\Delta t=\sigma_{A}/\frac{d\langle A\rangle}{dt}$.
- Podemos então escrever:
$$\Delta E\Delta t\ge \frac{\hbar}{2}$$

### 3.4.2 - Sistemas Conservativos
