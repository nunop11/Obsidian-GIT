# Processos estocásticos
## Definição
- Existe uma grande variedade de processos/sinais (sinais de radar, cotações da bolsa, consumo de água numa cidade, tráfego numa rua, etc etc) que evoluem no tempo segundo *leis probabilisticas*
- Este tipo de processos chamam-se então de **Processos estocásticos**

- Podemos definir "processo estocástico" como:
    - Conjunto de todas as variações possíveis de uma VA, que depende do tempo
    - Família de funções temporais

- E temos ainda os nomes equivalentes
    - Série temporal
    - Função aleatória

## Notação
- Temos o espaço amostral $\Omega$ das VAs dum processo estocástico $x$ 
- Designamos este processo de $x(t, \omega)$ em que $t\in T~,~\omega\in\Omega$ são o *tempo* e *evento*
- Se fixarmos $t=t_{1}$, removemos 1 variável e temos a VA $x(t_{1}, \omega)$ que está no espaço amostrar $\Omega$
- Se fixarmos o evento $\omega=\omega_{1}$ temos a função temporal $x(t,\omega_{1})$ a que chamamos *realização*

### Exemplo
- Consideremos a evolução de temperatura ao longo de 1 dia: $x(t,\omega)$
    - Se tivermos $t=12$ (horas) temos que $x(12, \omega)$ é uma VA que descreve a temperatura ao meio-dia
    - Se fixarmos $\omega=\text{15 de outubro de 2021}$ então $x(t,\text{15 de outubro de 2021})$ é uma função que mapeia a temperatura em função das horas, no dia 15 de outubro de 2021. Isto é a *realização* desta medição no dia 15 de outubro de 2021
- Por vezes ignoramos o evento e representamos $x(t)$


## Tipos
- Podemos ter processos estocásticos
    - **Contínuos** (ou *de parâmetro contínuo*) - quando o conjunto de índices $T$ é contínuo: $T\equiv [a,b]~,~T\equiv ]a,b]~,~T\equiv \mathbb{R}=]-\infty,+\infty[$
    - **Dicreto** (ou *de parâmetro discreto*) - quando o conjunto de índices $T$ é enumerável: $T\subset \mathbb{Z}$

- Nesta UC apenas usamos *processos discretos* porque resultam de **amostragens**, pelo que isto é o caso "real".

## Distribuição
- Tendo os instantes $t_{1},t_{2},\dots,t_{k}$ do processo $x(t)$, podemos definir a VA com k-dimensões:
$$X_{t_{1}:t_{k}}=\begin{pmatrix}x(t_{1}) \\ x(t_{2}) \\ x(t_{3}) \\ \vdots \\ x(t_{k})\end{pmatrix}$$
- Temos a distribuição:
$$\begin{align*}
&P[x(t_{1})\le a_{1}, x(t_{2})\le a_{2},\dots, x(t_{k})\le a_{k}] =\\
&=  \int_{-\infty}^{a_{1}}\int_{-\infty}^{a_{2}}\cdots\int_{-\infty}^{a_{k}}p_{t_{1},t_{2},\dots,t_{k}}(x_{1},x_{2},\dots,x_{k})~dx_{1}dx_{2}\cdots dx_{k}
\end{align*}$$
em que:
    - $a_{1},a_{2},\dots,a_{k}\in\mathbb{R}$
    - $p_{t_{i}}(x_{i})$ é a função de densidade de probabilidade conjunta de $X_{t_{1}:t_{k}}$

- Notemos que $P[x(t_{1})\le a_{1}, x(t_{2})\le a_{2},\dots, x(t_{k})\le a_{k}]$ é a distribuição finita de $x(t)$ nos instantes $t_{1},t_{2},\dots t_{k}$ 
- A distribuição de $x(t)$ em si é determinada por todas as distribuições finitas, ou seja, todos os intervalos de tempo finitos
    - Se as distribuições forem gaussianas, então $x(t)$ é um *processo estocástico gaussiano*

## Média e Covariância 
- Podemos definir o **momento de ordem k** do processo estocástico:
$$\begin{align*}
&M(t_{1},t_{2},\dots,t_{k})= \mathbb{E}\{x(t_{1}), x(t_{2}),\dots, x(t_{k})\}=\\
&= \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}\cdots\int_{-\infty}^{+\infty}x_{1}x_{2}\dots x_{k} \cdot p_{t_{1},t_{2},\dots,t_{k}}(x_{1},x_{2},\dots,x_{k}) \cdot dx_{1}dx_{2}\dots dx_{k}
\end{align*}$$
- Podemos definir a *função média/média* de $\{x(t)\}$, que não passa do momento de 1ª ordem:
$$\mu_{x}(t)=\mathbb{E}[x(t)]=M_{x}(t)$$
- Temos ainda a *função de covariância*:
$$\begin{align*}
\lambda_{xx}(t,s)&= \mathbb{E}\{[x(t)-\mu_{x}(t)][x(s)-\mu_{x}(s)]\}=\\
&= M_{x}(t,s)-M_{x}(t)M_{x}(s)\\
\end{align*}$$

**Variância**
- Podemos definir esta grandeza como: $$\sigma_{x}^{2}(t)=\lambda_{xx}(t,t)$$

#### EX: Gaussiano
- Consideremos um processo estocástico gaussiano $\{x(t)\}_{t=-\infty}^{+\infty}$, com média $\mu_{x}(t)$ e covariância $\lambda_{xx}(t,s)$. 
- Para este tipo de processo, a densidade de probabilidade conjunta é dada por:
$$p_{t_{1},t_{2},\dots,t_{k}}(x_{1},x_{2},\dots,x_{k})=\frac{1}{(2\pi)^{k/2}|\Sigma|^{1/2}} \exp\left[- \frac{1}{2}\sum\limits_{i=1}^{k}\sum\limits_{j=1}^{k}\Sigma_{i,j}^{-1}[x_{i}-\mu_{x}(t_{i})][x_{j}-\mu_{x}(t_{j})]\right]$$

#### EX: Processo de Wiener
- O processo de Wiener $W(t)$ modela movimento Browniano e segue as propriedades:
    1. $W(0)=0$
    2. Para qualquer $t_{1}<t_{2}$ temos que $W(t_{2})-W(t_{1})\sim N(0,t_{2}-t_{1})$
    3. Para intervalos não sobrepostos, os incrimentos $W(t_{2})-W(t_{1})$ são independentes
    4. A função $W(t)$ é contínua e não diferencial em quase qualquer ponto

## Processos estocásticos multidimensionais
- Temos o vetor  n-D:
$$x(t)=\begin{pmatrix}x_{1}(t) \\ x_{2}(t) \\  \vdots \\ x_{n}(t)\end{pmatrix}$$
- Este tem a média vetorial:
$$\mu_{x}(t)=\mathbb{E}[x(t)]=\begin{pmatrix}\mathbb{E}[x_{1}(t)] \\ \mathbb{E}[x_{2}(t)] \\ \vdots \\ \mathbb{E}[x_{2}(t)]\end{pmatrix}= \begin{pmatrix}\mu_{x_{1}}(t) \\ \mu_{x_{2}}(t) \\ \vdots \\ \mu_{x_{n}}(t)\end{pmatrix}$$
- Agora, invés de covariância temos *covariância vetorial*:
$$\begin{align*}
\lambda_{xx}&= \mathbb{E}\{[x(t)-\mu_{x}(t)][x(s)-\mu_{x}(s)]^{T}\}\\\\
&= \begin{pmatrix}\mathbb{E}[\tilde{x}_{1}(t)\tilde{x}_{1}(t)] & \mathbb{E}[\tilde{x}_{1}(t)\tilde{x}_{2}(t)] & \cdots & \mathbb{E}[\tilde{x}_{1}(t)\tilde{x}_{n}(t)]\\
\mathbb{E}[\tilde{x}_{2}(t)\tilde{x}_{1}(t)] & \mathbb{E}[\tilde{x}_{2}(t)\tilde{x}_{2}(t)] & \cdots & \mathbb{E}[\tilde{x}_{2}(t)\tilde{x}_{n}(t)]\\
\vdots & \vdots & \ddots & \vdots\\
\mathbb{E}[\tilde{x}_{n}(t)\tilde{x}_{1}(t)] & \mathbb{E}[\tilde{x}_{n}(t)\tilde{x}_{2}(t)] & \cdots & \mathbb{E}[\tilde{x}_{n}(t)\tilde{x}_{n}(t)]\end{pmatrix}
\end{align*}$$

em que usamos a mudança de variável: $\tilde{x}_{i}(t)=x_{i}(t)-\mu_{x_{i}}(t)$ 

- Os elementos da diagonal principal de $\lambda_{xx}$ são *covariâncias* de $\{x_{i}(t)\}$ e os outros elementos todos são *convariâncias cruzadas* entre $\{x_{i}(t)\},\{x_{j}(t)\}~~,~i\neq j$

## Processos fortemente estacionários
- Um processo é estacionário quando as propriedades estatísticas NÃO mudam com o tempo
- A função de densidade de probabilidade deste tipo de processos apenas depende da diferença entre os tempos $t_{i}-t_{j}~(i\neq j)$ MAS NÃO dos instantes $t_{i},t_{j}$ em si:
$$p_{t_{1},t_{2},\dots,t_{k}}(x_{1},x_{2},\dots,x_{k})=p_{t_{1}+\tau,t_{2}+\tau,\dots,t_{k}+\tau}(x_{1},x_{2},\dots,x_{k})$$
    - Um processo é **fortemente estacionário** se esta equação é verdade para qualquer $\tau$

- Em processos fortemente estacionários temos:
$$\mu_{x}(t)=\mu \quad;\quad \lambda_{xx}(t,s)=\lambda_{xx}(t-s)$$
(a média é constante e a covariância depende diretamente da diferença temporal)
- Processos que não seguem a condição de "fortemente estacionários" mas em que temos a média e covariância conforme acima -- *processos fracamente estacionários*

### EX: Ruído branco
- Consideremos um processo $\{v(t)\}_{t=-\infty}^{+\infty}$ 
- Ele é *ruído branco* se $v(t),v(s)$ forem igualmente distribuídas e independentes para qualer $t\neq s$. Podemos escrever isto como:
$$p_{t,s}[v(t),v(s)]=p_{t}[v(t)]\cdot p_{s}[v(s)] \quad \quad,\quad t\neq s$$
- Sendo $v(t),v(s)$ VAs com distribuições iguais temos:
$$\begin{align*}
\mu_{v}(t)&= M_{v}(t)=\mathbb{E}[v(t)]=\\
&= \mathbb{E}[v(s)]=M_{v}(s)=\mu_{v}(s)=\\
&= \mu_{v}
\end{align*}$$
e como são independentes:
$$M_{v}(t,s)=\mathbb{E}[v(t),v(s)]=\mathbb{E}[v(t)]\cdot\mathbb{E}[v(s)]=\mu_{v}^{2}$$
- Assim temos:
$$\lambda_{vv}(t,s)=M_{v}(t,s)-M_{v}(t)M_{v}(s)=\begin{cases}
\mu_{v}^{2}-\mu_{v}^{2}=0 & ; & t\neq s \\
M_{v}^{2}-\mu_{v}^{2}=\sigma_{v}^{2} & ; & t=s
\end{cases}$$
- Ruído branco é portanto **fracamente estacionário**, com vemos aqui (média constante e covariância dependente de $t-s$)
- No entanto, temos ainda que ele é **fortemente estacionário** porque as suas amostras são igualmente distribuidas

- Assim, ruído branco é algo imprevisível e "aleatório" porque nunca conseguimos prever o seu valor, já que ele é independente do seu passado e futuro
    - Aqui vimos que um ruído branco $v(t)$ é independentente para quaisquer $t\neq s$

### EX oposto: Passeio aleatório
- Este é um processo estocástico NÃO estacionário
- Consideremos um ruído branco $v(t)$ com média nula e variância $\sigma_{v}^{2}\neq0$
- Podemos definir um passei aleatório como:
$$x(t)=v(1)+v(2)+\dots+v(t) \quad \quad;\quad x(0)=0$$
que podemos escrever de forma recursiva:
$$x(t)=x(t-1)+v(t) \quad \quad;\quad x(0)=0$$

**Média**
$$\mu_{x}(t)=\mathbb{E}[0+v(1)+v(2)+\dots +v(t)]=0+0+0+\dots+0=0$$

**Covariância**
$$\begin{align*}
\lambda_{xx}(t,s)&= M_{x}(t,s) - M_{v}(t)M_v(s)\\
&= M_{x}(t,s)-0\cdot0\\
&= \mathbb{E}[x(t)x(s)]\\
&= \mathbb{E}\biggr\{\big[v(1)+v(2)+\dots+v(t)\big]\big[v(1)+ v(2)+\dots+v(s)\big]\biggr\}\\
&= \mathbb{E}[v(1)^{2}]+ \mathbb{E}[v(1)v(2)] + \mathbb{E}[v(2)^{2}] + \mathbb{E}[v(2)v(1)]+\dots\dots\\
\end{align*}$$
- Ora, considerando as amostras como independentes temos:
$$i\neq j ~~\longrightarrow~~ \mathbb{E}[v(i)v(j)]=0$$
Logo ficamos com:
$$\lambda_{xx}= \begin{cases}
s \sigma_{v}^{2} & ; & t\ge s \\
t \sigma_{v}^{2} & ; & t\le s
\end{cases}=\min(t,s)\sigma_{v}^{2}$$
- Para entender porquê que isto acontece, consideremos $t=2, s=4$:
$$\begin{align*}
\lambda_{xx}(2,4)&= \mathbb{E}\{[v(1)+v(2)][v(1)+v(2)+v(3)+v(4)]\}\\
&= \mathbb{E}[v(1)^{2}] + \mathbb{E}[v(1)v(2)] + \mathbb{E}[v(1)v(3)] + \mathbb{E}[v(1)v(4)] + \\
&+ \mathbb{E}[v(2)v(1)] + \mathbb{E}[v(2)^{2}] + \mathbb{E}[v(2)v(3)] + \mathbb{E}[v(2)v(4)]\\
&= \mathbb{E}[v(1)^{2}] + 0+0+0+0+\mathbb{E}[v(2)^{2}]+0+0\\
&= \sigma_{v}^{2}+\sigma_{v}^{2}=2\sigma_{v}^{2}=t \sigma_{v}^{2}=\min(t,s)\sigma_{v}^{2}
\end{align*}$$
- Vemos então que $\lambda_{xx}\neq \lambda_{xx}(t-s)$ LOGO o processo não é estacionário!
- Para ter uma ideia, vejamos um exemplo de passeio aleatório
![[Pasted image 20250930121245.png]]

#### Passeio aleatório VS Wiener
- Consideremos o **passeio aleatório**:
$$X_{n}=\sum\limits_{i=0}^{n}X_{i} \quad \quad;\quad X_{i}\sim N\left(0, \frac{T}{n}\right)$$
em que vemos que temos a definição $x(t)=v(1)+\dots+x(t)$, em que temos $t=n$ processos estocásticos igualmente distribuidos com gaussiana de média nula e $\sigma_{v}^{2}=T/n$
- Dizemos então que $X_{n}$ é um passeio aleatório de **duração** $T$
- Se mantivermos $T$ constante e aumentarmos o número de passos $n\to\infty$, então teremos $\Delta t=\frac{T}{n}\to0$
- Assim, podemos dizer que:
$$\lim_{n\to\infty}X_{n}=W(t) \quad \quad; \quad \text{em que }W(t)\text{ é processo de Wiener}$$

### Covariância de processos estacionários
- Sem perder generalidade, consideremos apenas processos de média nula.
- Como vimos, a função de covariância para processos estacionários *apenas* depende de $t-s$. Assim, podemos escrever:
$$\lambda_{xx}(\tau)=\mathbb{E}[x(t+\tau)x(t)]= \mathbb{E}[x(t)x(t-\tau)] \quad;\quad \tau=\pm1,\pm2,\dots$$
em que podemos definir $\tau=s-t$
- Por outras palavras, estamos a escrever a covariância em função do **desfasamento** $\tau$

#### Lema 1
- Temos então 3 propriedades de processos estacionários:
    1. **Limite em zero**
        - $|\lambda_{xx}(\tau)|\le\lambda_{xx}(0)=\sigma_{x}^{2}$
        - Isto acontece porque temos maior correlação em $\tau=0$ - autocorrelação
    2. **Simetria**
        - $\lambda_{xx}(\tau)=\lambda_{xx}(-\tau)$
        - O perfil $\lambda_{xx}(\tau)$ é simétrico relativamente ao zero
    3. **Semidefinida postiiva**
        - $\sum\limits_{i=1}^{n}\sum\limits_{k=1}^{n}a_{i}a_{k}\lambda_{xx}(\tau_{i}-\tau_{k})\ge0$
        - A matriz $\lambda_{xx}$ é definida positiva. Isto basicamente garante que obtemos valores fisicamente corretos

![[Pasted image 20250930145413.png]]
- A primeira cumpre as 3 propriedades, a segunda não cumpre a propriedade 1 e a terceira não cumpre a propriedade 2

## Processos ergódicos
- Podemos definir a média temporal de uma amostra de um processo estacionário de 2ª ordem $x(t)$:
$$m_{x}=\lim_{n\to\infty} \frac{1}{2N+1}\sum\limits_{t=-N}^{N}x(t)$$
e a correlação temporal do mesmo processo:
$$r_{xx}(\tau)=\lim_{N\to\infty} \frac{1}{2N+1} \sum\limits_{t=-N}^{N}x(t+\tau)x(\tau)$$

### Média ergódica
- Um processo estocástico estacionário tem *média ergódica* se:
$$\mathbb{E}[(m_{x}-\mu_{x})^{2}]=0$$
(em que $\mu_{x}=\mathbb{E}[x(t)]$)

### Covariância ergódica
- Um processo estocástico estacionário tem *covariância ergódica* se:
$$\mathbb{E}\{[r_{xx}(\tau)-\lambda_{xx}(\tau)]^{2}\}=0$$

### "Ergódico" - definição
- Um certo processo é ergódico se a média ou cálculo temporal de algo for igual ao que esperamos matematicamente! 
- Nos 2 casos acima, a média e covariância que determinamos através de médias temporais são (em média) iguais aos valores teóricos

## Densidade espectral
- Se a função de covariância de um processo estacionário for *absolutamente somável* ($\sum_{\tau=-\infty}^{+\infty}|\lambda_{xx}(\tau)|<\infty$) então podemos determinar a sua transformada de **Fourier** 
- Ora, a transformada de Fourier da função covariância de um processo estocástico chama-se **Densidade Espectral de Potência** ou *Densidade espectral*

### Definição formal
- Se um processo estacionário $\{x(t)\}$ tiver uma função de covariância absolutamente somável então a sua densidade espectral de potência é dada por
$$\Phi_{xx}(\omega)=\sum\limits_{\tau=-\infty}^{+\infty}\lambda_{xx}(\tau)e^{-j\omega\tau}$$
- E podemos definir a covariância a partir da densidade espectral, usando a transformada inversa de Fourier:
$$\lambda_{xx}(\tau)=\frac{1}{2\pi}\int_{-\pi}^{\pi}\Phi_{xx}(\omega)e^{j\omega\tau}d\omega$$
- Notemos que para $\tau=0$ temos
$$\lambda_{xx}(0)=\frac{1}{2\pi}\int_{-\pi}^{\pi}\Phi_{xx}(\omega)d\omega$$
se o processo for ergódico, podemos ainda escrever:
$$\lambda_{xx}(0)=\lim_{N\to\infty} \frac{1}{2N+1} \sum\limits_{t=-N}^{N}x(t)^{2}$$
e (não sei como) pelo teorema de Parseval podemos definir 
$$\lim_{N\to\infty} \frac{1}{2N+1} \sum\limits_{t=-N}^{N}x(t)^{2}=P_{x}[x(t)^{2}]$$
em que $P_{x}$ é apotência do sinal!
- Ou seja, isto diz-nos que $\Phi_{xx}(\omega)$ representa a distribuição de potência de $x(t)$ no intervalo $\omega\in[-\pi, \pi]$. Daí o nome "densidade espectral de potência"

### Propriedades
#### Simetria par
$$\Phi_{xx}(\omega)=\Phi_{xx}(-\omega)$$
- Isto acontece porque $\lambda_{xx}(\tau)$ ser uma função par: $\lambda_{xx}(\tau)=\lambda_{xx}(-\tau)$

#### Não negativa
$$\Phi_{xx}(\omega)\ge0$$
- Temos que a variância de $x(t)$ é $\sigma_{x}^{2}=\frac{1}{2\pi}\int_{-\pi}^{+\pi}\Phi_{xx}(\omega)d\omega$.
- A variância, claro, tem que ser positiva e real
- Imaginemos, que temos $\Phi_{xx}<0$. Num certo intervalo $\omega_{1}<\omega<\omega_{2}$, com a filtragem adequada, seria possível fazer com que $\sigma_{x}^{2}<0$, o que é impossivel! Logo a densidade espectral TEM de ser positiva

### Propagação de processos estacionários através de sistemas dinâmicos estáveis
- Consideremos um SLIT com função transferência $G(z)$ estável
- Imaginemos agora que a entrada do sistema for um processo fracamente estacionário $\{u(t)\}$ com média nula e densidade espectral $\Phi_{uu}(\omega)$.
- A saída do sistema, que representamos como $\{y(t)\}$ será também um processo estocástico fracamente estacionário com média nula. A sua densidade espectral é dada por:
$$\Phi_{yy}(\omega)=|G(e^{j\omega})|^{2}\Phi_{uu}(\omega)$$

### Teorema 1
- Podemos fatorizar a densidade espectral $\Phi_{yy}(\omega)$ assim
$$\Phi_{yy}(\omega)=H(e^{j\omega})H(e^{-j\omega})\sigma^{2}=|H(e^{j\omega})|^{2}\sigma^{2}$$
em que usamos
$$H(z)=\sum\limits_{k=0}^{\infty}h(k)z^{-k}$$
- Isto é uma função transferência normal no espaço de estado discreto. Temos que $h(k)$ são coeficientes e $z^{-k}$ é um *unit delay / atraso de amostra*. Tem esse nome porque, tendo uma transformada Z $X(z)$ da sequência $x(k)$, teremos que:
$$z^{-1}X(z) ~~\substack{\mathcal{Z}\\ \longleftrightarrow}~~ x(k-1)$$

#### Consequência do teorema
- Tendo em conta o teorema 1 e a propagação de processos em sistemas dinâmicos (ambos acima), conseguimos modelar qualquer processo estocástico como sendo a saída de um SLIT Causal e estável em que a entrada é ruído branco:
![[Pasted image 20250930225849.png]]
- O termo de densidade espectral **também** pode ser usado para referir a transformada Z:
$$\Phi_{xx}(z)=\sum\limits_{\tau=-\infty}^{+\infty}\lambda_{xx}(\tau)z^{-\tau}$$
- Temos ainda que é preciso a função transferência ser estável para o processo ser estacionário e vice-versa.

## Previsão linear
- Seja $y(t)$ um processo estacionário de média nula. 
- O melhor previsor linear de  $y(t)$ será representado como $\hat{y}(t)$. A sua previsão no instante $t-1$ será representada como $\hat{y}(t|t-1)$. 
- Temos ainda o **erro** $\hat{e}(t)=y(t)-\hat{y}(t)=e(t)$. 
    - Quando $\hat{y}$ é o melhor previsor de $y$, o erro é **ruído branco** de média nula

### Dedução do previsor
- Temos as seguintes equações:
$$\begin{cases}
y(t)=H(z)e(t) \\
\hat{e}=y(t)-\hat{y}(t)=e(t)
\end{cases}$$
de onde podemos tirar:
$$\hat{y}(t)=y(t)-e(t)=H(z)e(t)-e(t)=e(t)[H(z)-1]$$
- Podemos ainda escrever $e(t)=H^{-1}(z)y(t)$ logo:
$$\hat{y}(t)=[1-H^{-1}(z)]y(t)$$

#### Exemplo
- Consideremos o processo estocástico dado por:
$$y(t)=u(t)+2u(t-1)$$
em que $u(t)$ é ruído branco de média nula e variância $\sigma_{u}^{2}=1$
- Podemos fazer transformada Z dos 2 lados acima:
$$Y(z)=U(z)+2z^{-1}U(z)~~\to~~ G(z)=\frac{Y(z)}{U(z)}=1+2z^{-1}=\frac{z+2}{z}$$
- Ou seja, temos a função transferência $G(z)$ tal que: $\Phi_{yy}(z)=G(z)G(z^{-1})\sigma_{u}^{2}$
- Como vimos acima, podemos definir então o estimar:
$$\begin{align*}
\hat{y}(t)&= [1-G^{-1}(z)]y(t)=\frac{2z^{-1}}{1+2z^{-1}}y(t)\\
\hat{y}(t)&= 2y(t-1) - 2\hat{y}(t-1)
\end{align*}$$
que nos permite estimar o estado com a saída e previsão anteriores. Mas esta formulação não nos diz nada. Podemos reescrever assim:
$$1-G^{-1}(z)=\frac{2z^{-1}}{1+2z^{-1}}=\frac{2}{z+2}$$
- Vemos que este sistema tem um polo em $-2$. Isto é **instável**!!!
    - É instável porque $-2$ está fora do circulo unitário no plano complexo
- Por ser instável, o erro vai-se acumulando e eventualmente a previsão "rebenta":
![[Pasted image 20250930233552.png|500]]

### Melhor previsor
- Para obter o melhor previsor, precisamos de conseguir fatorizar o espetro na forma $\Phi_{yy}(z)=H(z)H(z^{-1})\sigma_{e}^{2}$ de forma que
    - **Função transferência linear** $H(z)=\sum_k h(k)z^{-k}$
    - **Fase mínima** $h(0)=1$
- Estas 2 condições garantem que a função de transferência é estável, com fase mínima. Isto por sua vez garante que os polos estão dentro do círculo unitário

#### Exemplo - continuação
- Temos a função transferência $G(z)=2+z^{-1}$
- Queremos então fazer com que se cumpra a condição $h(0)=1$. Ou seja:
$$H(z)=K(2+z^{-1})=2K + Kz^{-1}$$
e temos $h(0)=2K~,~h(1)=K$. Assim, forçamos: $K=0.5$
- Ficamos com a função de transferência normalizada:
$$H(z)=1+0.5z^{-1}$$
- Finalmente, temos o previsor:
$$\begin{align*}
\hat{y}(t)&= [1-H^{-1}(z)]y(t)=\left[1 - \frac{1}{1+0.5z^{-1}} \right]y(t)\\
&= \frac{0.5z^{-1}}{1+0.5z^{-1}}y(t)\\
\hat{y}(t) + 0.5z^{-1}\hat{y}(t)&= 0.5z^{-1}y(t)\\
\hat{y}(t)&= 0.5y(t-1) - 0.5 \hat{y}(t-1)=\frac{y(t-1)-\hat{y}(t-1)}{2}
\end{align*}$$
- E temos um previsor em que fazemos uma previsão a partir da saída e previsão anteriores. Sabemos que este sistema é estável

**Erro**
- Podemos escrever o erro assim:
$$\begin{align*}
\hat{e}(t)&= y(t)-\hat{y}(t)=y(t) - \frac{0.5z^{-1}}{0.5z^{-1}+1}y(t)\\
&= \frac{1}{0.5z^{-1}+1}y(r) = H_{\hat{e}}(z)y(t)
\end{align*}$$
- Podemos definir a densidade espectral do sinal como
$$\Phi_{yy}(z)=G(z)G(z^{-1})\sigma_{u}^{2}=\frac{z+2}{z}\frac{z^{-1}+2}{z^{-1}}\cdot1=(z+2)(z^{-1}+2)$$
(notemos que aqui usamos a função de transferência NÃO NORMALIZADA)

- Podemos então definir a densidade espectral do erro:
$$\begin{align*}
\Phi_{\hat{e}\hat{e}}(z)&= H_{\hat{e}}(z)H_{\hat{e}}(z^{-1})\Phi_{yy}(z)\\
&= \frac{1}{0.5z^{-1}+1} \frac{1}{0.5z+1} (z+2)(z^{-1}+2)\\
&= 4
\end{align*}$$
Ou seja, temos que $\hat{e}(t)$ é **ruído branco** com variância $\sigma_{e}^{2}=4$
- Notemos que esta é maior que a variância da entrada do sistema, $\sigma_{u}^{2}=1$
![[Pasted image 20250930235644.png]]