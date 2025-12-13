# Estimação Não Paramétrica
- Podemos definir a densidade espectral de potência de um processo estacionário como
$$P_{xx}(e^{j\omega})=\mathcal{F}\{ \lambda_{xx}(k) \}=\sum\limits_{k=-\infty}^{+\infty}\lambda_{xx}(k)e^{-j\omega k}$$
em que $\mathcal{F}$ representa a transformada de Fourier, em que:
$$\lambda_{xx}(k)=\mathbb{E}\{ x(t)x(t-k) \}$$
- Mas na realidade isto nunca é possível calcular, não temos infinitas amostras, logo o somatório de Fourier nunca terá este intervalo. Na realidade teremos de $L$ amostras (aceita este valor)

## Deduzir fórmula prática
- Ou seja, podemos representar as nossas amostras como uma janela (ou máscara em código):
$$x_{L}(t)=x(t)w(t) \quad;\quad w(t)=\begin{cases}
1 & , & 0\le t\le L-1 \\
0 & , & \text{resto dos casos}
\end{cases}$$
logo ficamos com a densidade de potência que conseguimos estimar
$$\hat{P}_{xx}(e^{j\omega})=\sum\limits_{k=-(L-1)}^{L-1}\hat{\lambda}_{xx}(k)e^{-j\omega k}$$
em que se usa a estimativa de covariância:
$$\hat{\lambda}_{xx}(k)=\frac{1}{L}\sum\limits_{t=0}^{L-1-k}x(t+k)x(t)=\frac{1}{L}\sum\limits_{t=0}^{L-1}x_{L}(t+k)x_{L}(t)$$

- Tendo em conta que $x_{L}(t)$ é uma janela aplicada em $x(t)$ podemos escrever:
$$\sum\limits_{t=0}^{L-1}x_{L}(t+k)x_{L}(t)=\sum\limits_{t=-\infty}^{+\infty}x_{L}(t+k)x_{L}(t)=x_{L}(k)*x_{L}(-k)$$

### Convolução
- Vamos ver como funciona esta operação, que tem a seguinte definição:
$$(f*g)(t)=\int_{-\infty}^{+\infty}f(\tau)g(t-\tau)d\tau$$
- Tendo um certo estado $x(t)$, podemos escrevê-lo assim usando deltas de Dirac:
$$\begin{align*}
x(t)&= \dots+x(-1)\delta(t+1)+x(0)\delta(t)+x(1)\delta(t-1)+\dots\\
&= \sum\limits_{k=-\infty}^{+\infty} x(k)\delta(t-k)
\end{align*}$$
ou seja, podemos ter uma soma infinita e apenas ficará o termo em que $k=t$.

**O sistema**
- Isto tudo é aplicado em **sistemas lineares** invariantes no tempo. Ser linear quer dizer que *a resposta de uma combinação linear de entradas será a combinação das respostas de cada uma das entrada* ou seja:
$$au_{1}(t)+bu_{2}(t)~~\longrightarrow~~ ay_{1}(t)+by_{2}(t) $$
- Sabemos ainda que, por definição um delta de Dirac origina uma *resposta impulsional* na saída de um SLIT:
$$\delta(t)~~\longrightarrow~~ h(t)$$

**O resultado**
- Apliquemos isto no somatório acima. Notemos que nisto, $x(0),x(1),\dots$ são **constantes** logo ficam de fora e temos:
$$\begin{align*}
x(0)\delta(t)~~&\longrightarrow~~ x(0)h(t)\\
x(1)\delta(t-1)~~&\longrightarrow~~ x(1)h(t-1)\\
\end{align*}$$
logo podemos ver que:
$$\sum\limits_{k=-\infty}^{+\infty}x(k)\delta(t-k)~~\longrightarrow~~ \sum\limits_{k=-\infty}^{+\infty}x(k)h(t-k)=y(t)$$
- Logo podemos ver que:
$$y(t)=x(t)*h(t)$$
e sabemos que isto é verdade.

### De volta a densidade espectral
- Aplicando esta lógica conseguimos entender como:
$$\sum\limits_{t=0}^{L-1}x_{L}(t+k)x_{L}(k)=x_{L}(k)*x_{L}(-k)$$
- E assim temos:
$$\hat{\lambda}_{xx}(k)=x_{L}(k)*x_{L}(-k)$$
- Vimos ainda que a densidade espectral é a *transformada de Fourier* da covariância. Ora podemos aproveitar o **teorema da convolução**:
$$\mathcal{F}\{(f*g)(\tau)\}= F(\omega)g(\omega)$$
logo:
$$\hat{P}_{xx}(e^{j\omega})=\mathcal{F}[\hat{\lambda}_{xx}(k)]=\frac{1}{L}X_{L}(e^{j\omega})X_{L}(e^{-j\omega})=\frac{1}{L}X_{L}(e^{j\omega})X_{L}(e^{j\omega})^{*}=\frac{1}{L}|X_{L}(e^{j\omega})|^{2}$$
e definimos a FT:
$$X_{L}(e^{j\omega})=\sum\limits_{t=-\infty}^{+\infty}x_{L}(t)e^{-j\omega t}=\sum\limits_{t=0}^{L-1}x(t)e^{-j\omega t}$$

## Valor esperado de periodograma
- Podemos deduzir:
$$\mathbb{E}\{\hat{P}_{xx}(e^{j\omega})\}=\sum\limits_{k=-(L-1)}^{L-1}\mathbb{E}\{\hat{\lambda}_{xx}(k)\}e^{-j\omega k}$$
em que
$$\mathbb{E}\{\hat{\lambda}_{xx}(k)\}=\frac{1}{L}\sum\limits_{t=0}^{L-1}\mathbb{E}\{x_{L}(t)x_{L}(t-k)\}$$
(acima usamos $x_{L}(t)x_{L}(t+k)$ porque dava jeito na dedução ig. Aqui usamos a versão com $x_{L}(t-k)$ e está correto porque a matriz de covariância é *simétrica*)

- Tal como vimos acima:
$$x_{L}(t)=\begin{cases}
x(t) & ; & 0\le t\le L-1 \\
0 & ; & t<0~~,~~t>L-1
\end{cases}$$
em que temos basicamente uma janela retangular de comprimento $L$ aplicada em $x(t)$
- E podemos definir:
$$\begin{align*}
\mathbb{E}\{\hat{\lambda}_{xx}(k)\}&= \frac{1}{L}\sum\limits_{t=0}^{L-1}\mathbb{E}\{x_{L}(t)x_{L}(t-k)\}\\
&= \frac{1}{L}\sum\limits_{t=0}^{L-1-|k|}\mathbb{E}\{x(t)x(t-k)\}\\
&= \frac{1}{L}\sum\limits_{t=0}^{L-1-|k|}\lambda_{xx}(k)\\
&= \frac{1}{L}(L-1-|k| + 1)\lambda_{xx}(k)\\
&= \frac{L-|k|}{L}\lambda_{xx}(k)
\end{align*}$$
e temos na fração uma função que descreve uma **janela triangular de Bartlett**:
$$w_{B}(t)=\begin{cases}
\frac{L-|t|}{L} & ; & |t|\le L \\
0 & ; & |t|>L
\end{cases}$$
![[janela bartlett.png]]

- Ou seja podemos escrever:
$$\mathbb{E}\{ \hat{\lambda}_{xx}(k) \}=\lambda_{xx}(k)*w_{B}(k)$$
- Pelo teorema da convolução:
$$\mathbb{E}\{ \hat{P}_{xx}(e^{j\omega}) \}=\mathcal{F}\{ \lambda_{xx}(k)w_{B}(k) \} = \frac{1}{2\pi} P_{xx}(e^{j\omega})W_{B}(e^{j(\omega-\theta)})$$
em que temos as FT:
$$\begin{align*}
P_{xx}(e^{j\omega})&= \mathcal{F}\{ \lambda_{xx}(k) \} = \sum\limits_{k=-\infty}^{+\infty}\lambda_{xx}(k)e^{-j\omega k}\\
W_{B}(e^{j\omega})&= \mathcal{F}\{ w_{B}(k) \}=\frac{1}{L} \left[ \frac{\sin(\frac{wL}{2})}{\sin(\frac{w}{2})} \right]^{2}
\end{align*}$$
- Ou seja, o valor médio é diretamente influenciado pela janela que aplicamos na amostra (Bartlett neste caso)

### Caso assintótico
- Podemos fazer um gráfico de $W_{B}(e^{j\omega})$ conforme calculado acima:
![[fourier de bartlett.png]]
- Podemos concluir que consoante $L$ aumenta ficamos apenas com picos em múltiplos de $2\pi$. Ou seja, podemos dizer que:
$$\lim_{L\to\infty}W_{B}(e^{j\omega})=2\pi \delta(\omega)$$

- Aplicando isto:
$$\lim_{L\to\infty}\mathbb{E}\{ \hat{P}_{xx}(e^{j\omega}) \}=\frac{1}{2\pi}P_{xx}(e^{j\omega})*2\pi \delta(\omega)=P_{xx}(e^{j\omega})$$
- Ou seja, temos que $\hat{P}_{xx}(e^{j\omega})$ é um **estimador não enviezado** de $P_{xx}(e^{j\omega})$.
![[fourier bartlett diferentes L.png]]

## Janelas
### Retangular
- Este é o caso que acabamos de estudar e deduzir
- É muito fácil de conceptualizar e calcular, mas temos sempre picos nas laterais de cada pico (como vemos acima)
- Temos ainda uma má resolução se não tivermos $L$ gigantesco

### Hann
- Esta janela piora (aumenta) a largura do pico principal para melhorar (diminuir) os picos laterais.
- Definimos como:
$$\begin{align*}
w_\text{Hann}(t)&= \frac{1}{2}\left[1-\cos\left(\frac{2\pi t}{N-1}\right)\right]\\
W_\text{Hann}(t)&= \frac{1}{2}D_{N}(\omega) - \frac{1}{4} D_{N}\left(\omega- \frac{2\pi}{N-1}\right)- \frac{1}{4}D_{N}\left(\omega+ \frac{2\pi}{N-1}\right)
\end{align*}$$
e temos o kernal de Dirichlet:
$$D_{N}(\omega)=e^{-j\omega \frac{N-1}{2}}\frac{\sin(\frac{N\omega}{2})}{\sin(\frac{\omega}{2})}$$
![[hann.png]]

### Hamming
- Reduz ainda mais os picos laterai, tendo aproximadamente a mesma largura de pico principal que Hann
$$\begin{align*}
w_\text{Hamming}(t)&= \begin{cases}
\alpha-\beta \cos\left(\frac{2\pi t}{N-1}\right) & , &  0\le t\le N-1\\
0 & , & \text{caso contrário}
\end{cases}\\
W_\text{Hamming}(e^{j\omega})&= \alpha D_{N}(\omega)- \frac{\beta}{2}D_{N}\left(\omega- \frac{2\pi}{N-1}\right)- \frac{\beta}{2}D_{N}\left(\omega+ \frac{2\pi}{N-1}\right)
\end{align*}$$
em que temos $\alpha=0.54~,~\beta=0.46$ e temos $D_{N}(\omega)$ o kernel de Dirichlet.
![[hamming.png]]

### Blackman
- Temos uma supressão muito boa dos picos laterais, mas menos resolução
$$\begin{align*}
w_\text{Blackman}(t)&= \begin{cases}
a_{0}-a_{1}\cos\left(\frac{2\pi t}{N-1}\right)+a_{2}\cos\left(\frac{4\pi t}{N-1}\right) & , & a\le t\le N-1\\
0 & , & \text{caso contrário}
\end{cases}\\
W_\text{Blackman}(e^{j\omega})&= a_{0}D_{N}(\omega) - \frac{a_{1}}{2}D_{N}\left(\omega-\frac{2\pi}{N-1}\right)-\frac{a_{1}}{2}D_{N}\left(\omega+\frac{2\pi}{N-1}\right) \\
&~~~~+ \frac{a_{2}}{2}D_{N}\left(\omega- \frac{4\pi}{N-1}\right)+\frac{a_{2}}{2}D_{N}\left(\omega+ \frac{4\pi}{N-1}\right)
\end{align*}$$
em que temos $a_{0}=0.42~,~a_{1}=0.50~,~a_{2}=0.08$
![[blackman.png]]

### Flat-Top
- Tem o topo achatado, como o nome indica. Isso significa que é melhor para estimar amplitudes
$$\begin{align*}
w_\text{Flat-Top}(t)&= \begin{cases}
a_{0}-a_{1}\cos\left(\frac{2\pi t}{N-1}\right)+a_{2}\cos(\frac{4\pi t}{N-1})\\
~~~~~~-a_{3}\cos\left(\frac{6\pi t}{N-1}\right)+a_{4}\cos\left(\frac{8\pi t}{N-1}\right) & , & 0\le t\le N-1\\
0 & , & \text{caso contrário}
\end{cases}\\
W_\text{Flat-Top}(e^{j\omega})&= a_{0}D_{N}(\omega) - \frac{a_{1}}{2}D_{N}\left(\omega- \frac{2\pi}{N-1}\right)- \frac{a_{1}}{2}D_{N}\left(\omega+ \frac{2\pi}{N-1}\right)\\
&~~~~~~+ \frac{a_{2}}{2}D_{N}\left(\omega- \frac{4\pi}{N-1}\right)+ \frac{a_{2}}{2}D_{N}\left(\omega+ \frac{4\pi}{N-1}\right)
\end{align*}$$
em que $a_{0}=1~,~a_{1}=1.93~,~a_{2}=1.29~,~a_{3}=0.388~,~a_{4}=0.0322$
![[Pasted image 20251207183819.png]]

### Efeitos da janela
- Janela com pico principal mais estreido - mais resolução, mais picos laterais
- Janela com pico principal mais largo - menos resolução, menos picos laterais
- Basicamente temos que fazer um *trade-off* entre **Resolução** e **Picos Laterais**
- A janela retângular é a pior em picos laterais, gerando muitos e com amplitudes significantes

## Variância do periodograma
- A variância de $\hat{P}_{xx}(e^{j\omega})$ depende dos momentos de $x(t)$ de ordem *superior à segunda*
- Ou seja, a variância deveria depende da **distribuição** de $x(t)$
- MAS, pode-se demonstrar que, *par qualquer distribuição* temos:
$$\text{var} \left\{ \hat{P}_{xx}(e^{j\omega}) \right\}\approx P_{xx}(e^{j\omega})^{2}$$
isto porque empiricamente vê-se que a variância fica quase constante para qualquer número de pontos do periodograma
- Isto implica uma coisa:o periodograma **NÃO é consistente**
    - A sua média converge para o valor real de $P_{xx}(e^{j\omega})$ como vimos acima
    - Mas vimos agora que a variância não converge para nada, ela é constante
    - Assim, dizemos que *não é consistente*, para isso era preciso converger **probabilisticamente** (toda a distribuição tinha de converger, não só a média)
    - Apenas podemos dizer que $\hat{P}_{xx}(e^{j\omega})$ é um estimador não enviezado

## Médias
- Vamos ver métodos de determinar a média do periodograma

### Método de Bartlett
1. Dividimos o sinal em $K$ segmentos *sem sobreposição*. Cada ponto fica então classificado assim: $$x^{(r)}(t)~~~~,~~~~r=1,\dots,K$$
2. Calcular o periodograma para cada segmento com janelas retangulares: $$\text{Determinar }\hat{P}_{xx}^{(r)}(e^j\omega)$$
3. A média é dada ao calcular a média dos segmentos: $$\overline{P}_{xx}(e^{j\omega})=\frac{1}{K}\sum\limits_{r=1}^{K}\hat{P}_{xx}^{(r)}(e^{j\omega})$$
- Relativamente a calcular a calcular o periodograma do sinal todo e depois calcular a média, isto reduz a variância por um fator de $1/K$

### Método de Welch
- Fazemos o mesmo que no método de Bartlett, mas:
    - Usamos janelas não retangulares (normalmente de Hann)
    - Os segmentos sobrepõe-se todos em 50% (mas podemos usar outra percentagem)
    - Normalizamos cada segmento para evitar enviesamento

- E obtemos as seguintes vantagens:
    - Redução de variância da média 
    - Melhor compromisso entre resolução e variância
    - Utiliza os dados de forma mais eficiente

### Blackman-Tukey
- Em vez de dividir o sinal em $K$ segmentos como fazem os outros métodos, dividimos a *auto-covariância* em $M$ partes:
$$\hat{P}_{xx}(e^{j\omega})=\sum\limits_{k=-M}^{M}w(k)\hat{\lambda}_{xx}(k)e^{-j\omega k}$$

- Notemos então que:
    - A janela atua no domínio do tempo, não no espetro. Então aqui estamos a aplicar uma nova janela mas no espetro
    - Conseguimos controlar diretamente o trade-off resolução - picos laterais
    - Implica que temos de estimar a autocovariância até $M$

