# 1 - Sistema isolado
- Se considerarmos um sistema isolado, temos que a energia interna do sistema, $E$, é *constante*.
- Podemos descrever este sistema por um conjunto/ensemble **microcanónico**. Conforme referido atrás, por a energia ser constante, todos os microestados deste conjunto estão restritos à superfície do espaço de estados: $\mathcal{H}(\mu)=E$ ($\mu$ é um ponto do espaço de fase)

**Medições**
- Devido à rápida variação temporal dos microestados, ao fazer uma medição apenas estamos a tomar a média de um observável num intervalo $\delta t$.

**Energia**
- Definimos um macroestado com um intervalo de energia $[E+\delta E[$ para garantir que temos microestados suficientes. Por exemplo, num espaço de estados contínuo, podemos ter uma medida 0 de estados com exatamente 1 nível de energia.
- Por fazermos isto, temos que considerar que deverá existir um fator de normalização diferente ao determinar a distribuição de probabilidade. Na realidade, ao tomar o limite termodinâmico esta diferença torna-se irrelevante.


# 2 - Espaço de Fase Discreto
- A probabilidade de encontrarmos um microestado em $\mu$ no estado de equilíbrio é:
$$P_{E,X,N}(\mu)=\frac{1}{\Omega(E)}\cdot \begin{cases}
1 & ; & E\le \mathcal{H}(\mu)\le E+\delta E \\
0 & ; & restante
\end{cases}$$
em que:
    - $E$ - nível de energia fixo
    - $X$ - conjunto de parâmetros externos ao espaço de fase (volume, campos externos, etc)
    - $N$ - nº de partículas em estudo
    - $\Omega(E)$ - nº de microestados com energia $\in[E,E+\delta E[$ 

e a isto chamamos Postulado de Boltzmann de probabilidades de equilíbrio iguais. Este postulado é coerente com o teorema de Liouville.

**Entropia**
- Podemos determinar a entropia de Shannon:
$$S_{Shannon}=-\sum\limits_{\mu}P(\mu)\ln P(\mu)=\ln \Omega(E)$$
e a entropia de Boltzmann:
$$S_{Boltzmann}=k_{B}\ln \Omega(E)$$

# 3 - Espaço de Fase Contínuo
- Temos
$$P(\mu)=\rho_{E,X,N}(\mu)d\mu$$
em que $d\mu= dx_{1}dx_{1}dy_{1}dp_{x_{1}}dp_{y_{1}}dp_{z_{1}}\dots$
- Tem-se então:
$$\rho_{E,X,N}(\mu)=\frac{\delta(E-\mathcal{H}(\mu))}{\int \delta(E-\mathcal{H}(\mu)) d\mu})=\frac{\delta(E-\mathcal{H}(\mu))}{D(E)}$$
(ou seja $D(E)=\int\delta(E-\mathcal{H}(\mu))d\mu$)

**Adimensionalizar**
- Simplesmente fazemos:
$$d\mu=\frac{dx_{1}dp_{x_{1}}\cdots dx_{N}dp_{x_{N}}}{h}$$
onde $h$ é a constante de Planck.

**Entropia**
- Temos a entropia de Shannon:
$$\begin{align*}
S_{Shannon}&= -\int \rho(\mu)\ln\rho(\mu)~d\mu \\
&= -\left[\int \frac{\delta(E-\mathcal{H}(\mu))}{D(E)}\ln \delta(E-\mathcal{H}(\mu)) d\mu - \int \frac{\delta(E-\mathcal{H}(\mu))}{D(E)}\ln D(E)d\mu\right]\\
&= \ln D(E)
\end{align*}$$
- Em que o 1º termo é eliminado porque $\ln \delta()$ diverge.
- O integral $\int \delta(E-\mathcal{H}(\mu))d\mu$ funciona assim:
$$\int \delta(f(\mu)) ~ d\mu = \begin{cases} 1 & \text{if } f(\mu) = 0 \text{ tem 1 soluão} \\ 0 & \text{caso contrário} \end{cases}$$
pelo que na dedução acima temos $\int \delta(E-\mathcal{H}(\mu))d\mu=1$ e igualmente para $D(E)$.

- Temos ainda:
$$\Omega(E)=D(E)\delta E$$
e temos então a entropia de Boltzmann:
$$S_{Boltzmann}=k_{B}\ln \Omega(E)=k_{B}\ln D(E) + \cancelto{\approx0}{k_{B}\ln\delta E}$$
$$S_{Bolztmann}=k_{B}\ln(D(E))$$
e podemos escrever:
$$e^\frac{S}{k_{B}}=D(E)$$

### Entropia é Aditiva
## Entropia é Aditiva
- Tendo 2 sistemas $A$ e $B$ isolados, com energias $E_A$ e $E_B$, então:
$$\Omega_{A+B}(E_A+E_B) = \Omega_A(E_A)\Omega_B(E_B)$$
Pois para cada estado possível de $A$ o sistema $B$ pode estar em qualquer estado
- Logo temos que:
$$ \begin{align*}
S_{A+B} &= k_B\ln \Omega_{A+B}(E_A + E_B) \\
&= k_B\ln \Omega_A(E_A) + k_B\ln \Omega_B(E_B) \\
&= S_A + S_B
\end{align*} $$

# 4 - Termodinâmica
## 4.1 - Lei Zero
- Vamos considerar 2 sistemas isolados com energias $E_{1},E_{2}$ parâmetros externos $X_{1},X_{2}$ e representados por pontos $\mu_{1},\mu_{2}$ do espaço de fase. Eles trocam calor entre si.
- Temos:
$$P(\mu)=\frac{1}{\Omega_{1}(E_{1},X_{1})}\cdot \frac{1}{\Omega_{2}(E_{2},X_{2})}$$
em que $H(\mu_{1})=E_{1},H(\mu_{2})=E_{2}$

- Podemos definir as propriedades totais dos 2 sistemas juntos:
$$E_{T}=E_{1}+E_{2} \quad \quad;\quad \quad S_{T}=S_{1}+S_{2}$$
- E então:
$$P(\mu)=\frac{1}{\Omega(E_{T})}$$
em que temos
$$\begin{align*}
\Omega(E_{T})&= \int dE_{1}dE_{2}~\Omega(E_{1})\Omega(E_{2})\delta(E_{T}-E_{1}-E_{2})\\
&= \int dE_{1}~ \Omega_{1}(E_{1})\Omega(E_{T}-E_{1})\\
&= \int e^{\frac{S_{T}}{k_{B}}} dE_{1}= \int \exp\left(\frac{S_{1}(E_{1})+S_{2}(E_{T}-E_{1})}{k_{B}}\right)dE_{1}
\end{align*}$$

**Interações**
- Podemos definir o Hamiltoniano dos sistemas em conjunto:
$$H(\mu)=H_{1}(\mu_{1})+H_{2}(\mu_{2})+V(\mu_{1},\mu_{2},X_{1},X_{2})$$
- Ora, o termo de interação será nulo no limite termodinâmico. Isto porque as energias do sistema 1 e 2 irá aumentar com o número de partículas, mas a energia associada às interações aumenta mais devagar.
- Assim, ignoramos este termo e presumimos que em $t\to\infty$ algum mecanismo irá establecer o equilíbrio entre os sistemas.

**Máximo de Entropia**
- Irá ocorrer quando os sistemas têm energia $E_{1}^{*},E_{2}^{*}$. Assim:
$$\frac{\partial S_{1}}{\partial E_{1}}(E_{1}^{*})=0 \quad \quad;\quad \quad \frac{\partial S_{2}}{\partial E_{2}}(E_{2}^{*})=0$$
ou seja:
$$\frac{\partial S_{1}}{\partial E_{1}}(E_{1}^{*})=\frac{\partial S_{2}}{\partial E_{2}}(E_{2}^{*})$$
- E temos uma relação entre as energias máximas dos dois sistemas. Uma vez que a energia total do sistema é constante e igual a $E_{T}=E_{1}+E_{2}$, conhecendo algumas destas variáveis conseguimos determinar as outras.

## 4.2 - Temperatura 
- Podemos definir:
$$\boxed{\frac{1}{T}=\frac{\partial S}{\partial E}}{}$$
ou seja, usando a relação da entropia máxima acima:
$$\frac{1}{T_{1}^{*}}=\frac{1}{T_{2}^{*}}$$
pelo que um sistema tem entropia máxima quando os seus subsistemas estão em equilíbrio térmico.

## 4.3 - Probabilidade de sistema ter uma certa energia
$$P(E_{1})=\frac{\Omega_{1}(E_{1})\Omega_{2}(E_{T}-E_{1})}{\Omega(E_{T})}$$
- Podemos calcular:
$$\begin{align*}
e^{\frac{S_{T}}{k_{B}}}&= \exp\frac1{k_B}\left(S_1(E_1) + S_2(E_T - E_1)\right) \\
&= \exp\frac1{k_B}\left(S_1(E_1^*) + S_2(E_T - E_1^*) + \frac12\frac{d^2S_1}{dE_1^2}(E_1 - E_1^*)^2 + \frac12\frac{d^2S_2}{dE_2}(E_2-E_2^*)^2 + \cdots\right) \\
&= \exp\frac1{k_B}\left(S_1(E_1^*) + S_2(E_T - E_1^*)\right)\exp\frac1{k_B}\left(\frac12\frac{d^2S_1}{dE_1^2}(E_1 - E_1^*)^2 + \frac12\frac{d^2S_2}{dE_2}(E_1^*-E_1)^2 + \cdots\right)
\end{align*}$$
em que simplesmente usamos $S_{T}=S_{1}+S_{2}$ e expandimos as funções em série de taylor em torno de $E_{1}^{*}$, pelo que a primeira derivada $dS/dE$ é nula na energia de entropia máxima.

- Assim, a função $P(E_{1})$ tem um máximo em $E_{1}^{*}$, de largura:
$$\sigma^{2}=\Biggr|\frac{d^{2}S_{1}}{sE_{1}^{2}}+\frac{d^{2}S_{2}}{dE_{2}^{2}}\Biggr|^{-1}\sim \frac{1}{\sqrt{N}}$$
em que usamos $S\propto N$ no último passo. 

# 5 - Primeira Lei da Termodinâmica
>**NOTA:** Por razões técnicas, quando temos um diferencial não exato (como do trabalho) escrevi $\mathscr{d}W$ em que o "d" caligráfico representa o "d" com um traço (do género de $\hbar$).

- Consideremos que num sistema isolado efetuamos um processo reversível. 
- Estaremos a realizar no sistema um trabalho
$$\mathscr{d}W=F\cdot \delta x$$
que fará a energia do sistema variar: $E\to E+\mathscr{d}W$
- A entropia do sistema é definida por $S(E,x)$ e é alterada em:
$$\begin{align*}
dS=\frac{\partial S}{\partial E}dE+\frac{\partial S}{\partial x}dx
\end{align*}$$
que conforme o trabalho realizado indicado acima fica:
$$dS=\left(\frac{\partial S}{\partial E}F+\frac{\partial S}{\partial x}\right)dx$$
- No entanto, se o processo é reversível, então a variação de entropia terá de ser nula:
$$\frac{\partial S}{\partial E}F=- \frac{\partial S}{\partial x} ~~\longrightarrow~~ \frac{F}{T}=-\frac{\partial S}{\partial x}$$
assim podemos escrever:
$$\begin{align*}
dS&= \frac{\partial S}{\partial E}dE+\frac{\partial S}{\partial x}dx\\
&= \frac{1}{T}dE + \left(\frac{-F}{T}\right)dx\\
dE &= TdS + Fdx=dQ-dW
\end{align*}$$

# 6 - Segunda Lei da Termodinâmica
- Retomemos os 2 sistemas inicalmente isolados que ligamos.
- Temos que se um sistema evoluir de um estado $i$ para outro $f$ e aí ficar em equilíbrio então:
$$\begin{align*}
S_{T}^{f}&> S_{T}^{i}\\
S_{1}(E_{1}^{*})+S_{2}(E_{T}-E_{1}^{*})&> S_{1}(E_{1})+S_{2}(E_{T}-E_{1})\\
S_{1}(E_{1}^{*})+S_{2}(E_{T}-E_{1}^{*}) -S_{1}(E_{1})-S_{2}(E_{T}-E_{1})&> 0\\
\end{align*}$$
- Consideremos agora que $E_{1}^{*}=E_{1}+\delta E$. Vamos expandir os primeiros 2 termos em série de Taylor:
$$\begin{align*}
S_{1}(E_{1}^{*})&= S_{1}(E_{1})+\frac{dS_{1}}{dE_{1}}(E_{1})\delta E_{1}\\
S_{2}(E_{T}-E_{1}^{*})&= S_{2}(E_{T}-E_{1})+\frac{dS_{2}}{dE_{2}}(E_{T}-E_{1})(-\delta E_{1})
\end{align*}$$
(recordar: $f(x + h) = f(x) + f′(x)h + f′′(x) \frac{h_{2}}{2!} +\dots$)

- Juntando tudo fica:
$$\begin{align*}
\left(\frac{dS_{1}}{dE_{1}}(E_{1})-\frac{dS_{2}}{dE_{2}}(E_{T}-E_{1}) \right)\delta E_{1}&> 0\\
\left(\frac{1}{T_{1}} -\frac{1}{T_{2}} \right)\delta E_{1}&> 0
\end{align*}$$
de onde resulta:
$$\begin{align*}
\delta E_{1}> 0\to T_{2}>T_{1}\\
\delta E_{1}< 0\to T_{2}<T_{1}
\end{align*}$$
ou seja, a energia vai sempre **do estado de maior temperatura para o estado de menor temperatura**!

# 7 - Critério de Estabilidade
- Quando os 2 sistemas estão num ponto com energia de máxima entropia $E_{1}^{*},E_{2}^{*}$ temos:
$$\frac{d^{2}S_{1}}{dE_{1}^{2}}(E_{1}^{*})+\frac{d^{2}S_{2}}{dE_{2}^{2}}(E_{2}^{*})\le 0$$
sendo que isto equivale a $E_{T}=E_{1}^{*}+E_{2}^{*}$

# 8 - Sistema a dois níveis
- Consideremos um sistema com $N$ partículas e 2 estados possíveis:
$$E_{1}(\textsf{Estado 0})=0 \quad \quad;\quad \quad E_{2}(\textsf{Estado 1})=\varepsilon$$
- Como já vimos, o número de microestados com uma certa energia $E$ é $\Omega_{N}(E)$.
- Tendo-se $n$ partículas com energia $\varepsilon$ / no estado 1, então a energia do sistema é: $E=n\varepsilon$
- Ora, o número de estados com energia $E_{n}$ é o número de formas distintas de escolher $n$ elementos dos $N$:
$$\Omega_{N}(E)=\frac{N!}{n!(N-n)!}$$
(Por exemplo, se $n=N$ só há 1 microestado, aquele em que todas as partículas têm energia $E$. Se $n=1$ temos $N$ microestados, qualquer uma das partículas pode ter a energia $E$. Etc etc)

- Usando a definição de entropia de Boltzmann: $S=k_{B}\ln \Omega(E)$:
$$\ln \Omega_{N}(E)=\ln N! - \ln n! - \ln(N-n)! = \frac{S}{k_{B}}$$

**Entropia**
- Usemos a fórmula de Stirling:
$$\begin{align*}
\frac{S}{k_{B}}= \ln\Omega_{N}(E)&=N\ln N +\bcancel{N} + \frac{1}{2}\ln(2\pi N)- n\ln n -\cancel{n}- \frac{1}{2}\ln(2\pi n) \\
&\quad\quad\quad\quad\quad\quad-(N-n)\ln(N-n) - \bcancel{N} + \cancel{n} - \frac{1}{2}\ln(2\pi (N-n))\\
&= N\ln N-n\ln n -(N-n)\ln(N-n) + \frac{1}{2}\ln\frac{N}{n(N-n)}
\end{align*}$$
podemos desprezar o último termo.
- Fazendo a substituição $f=n/N$:
$$\begin{align*}
\frac{S}{k_{B}}&= N\ln N- Nf\ln Nf - (N-Nf)\ln (N-Nf)\\
&= N\ln N -Nf\ln N - Nf\ln f-N\ln(N-Nf)+Nf\ln(N-Nf)\\
&= \cancel{N\ln N} -\bcancel{Nf\ln N} - Nf\ln f-\cancel{N\ln N} -N\ln(1-f)+\bcancel{Nf\ln N} +Nf\ln(1-f)\\
&= N(-\ln(1-f)) + Nf(-\ln f+\ln(1-f))\\
&= N\left[f \ln\frac{1-f}{f}-\ln(1-f)\right]\\
&= -N[(1-f)\ln(1-f)+f\ln f] 
\end{align*}$$
- Podemos reorganizar isto:
$$\frac{S}{N}=-k_{B}[(1-f)\ln(1-f)+f\ln f] $$
e podemos chamar a $\frac{S}{N}$ *entropia intensiva*.
- Podemos intuitivamente ver que a entropia máxima irá ocorrer para $f=\frac{1}{2}$ quando $T\to\infty$

**Temperatura**
- Podemos escrever:
$$\begin{align*}
\frac{1}{T}=\frac{dS}{dE}=\frac{d(Ns)}{d(N\varepsilon f)}\\
\end{align*}$$
em que $s$ é a entropia intensiva (aka entropia de 1 partícula) e usamos $E=n\varepsilon=Nef$.
- Continuando:
$$\begin{align*}
\frac{1}{T}&= \frac{1}{\varepsilon} \frac{ds}{df}=\frac{1}{\varepsilon} \frac{d}{df}(-k_{B}[(1-f)\ln(1-f)+f\ln f])\\
&= - \frac{k_{B}}{\varepsilon}\left[- \frac{d}{df}((1-f)\ln(1-f)) + \frac{d}{df}(f\ln f) \right]\\
&= - \frac{k_{B}}{\varepsilon}\left[ -\ln(1-f) -(1-f)\frac{1}{1-f} + \ln f + f\frac{1}{f} \right]\\
&= - \frac{k_{B}}{\varepsilon}\left[\ln\frac{f}{1-f}\right]
\end{align*}$$
$$\boxed{\frac{1}{T}=\frac{k_{B}}{\varepsilon}\ln\frac{1-f}{f}}$$
em que:
- $0 \le f < 1/2$ → temperatura positiva
- $1/2 = f$ → temperatura nula
- $1/2 < f \le 1$ → temperatura negativa

- De notar que a temperatura pode ser negativa, sendo que isto apenas ocorre em sistems discreto finitos. Num sistema que tenha infinitos níveis de energia ou que seja contínuo é impossível ter temperatura negativa.
- Esta temperatura negativa surge porque ao aumentar a energia diminui o número de microestados com essa energia.
- Podemos ainda escrever isto como:
$$f=\frac{1}{1+\exp(\frac{\varepsilon}{k_{B}T})} \quad \quad;\quad \quad E=\frac{\varepsilon N}{1+\exp(\frac{\varepsilon}{k_{B}T})}$$

- O máximo de energia interna ocorre quando $T\to\infty$ em que temos $E\to\frac{\varepsilon N}{2}$. Para $T\to0$ temos o mínimo, tendo-se $E=0$.

## 8.1 - Capacidade Calorífica
$$\begin{align*}
C(T)\equiv \frac{dE}{dT}&= - \frac{\varepsilon N}{[1+\exp(\frac{\varepsilon}{k_{B}T})]^{2}} \exp\left(\frac{\varepsilon}{k_{B}T}\right)\frac{-\varepsilon}{k_{B}T^{2}}\\
&= Nk_{B}\left(\frac{\varepsilon}{k_{B}T}\right)^{2}\exp\left(\frac{\varepsilon}{k_{B}T}\right) \left[1+\exp\left(\frac{\varepsilon}{k_{B}T}\right) \right]^{-2}
\end{align*}$$
temos:
    - $T\to0:C\to0$ - $C$ decai com $\exp(-\varepsilon/k_{B}T)$, algo carateristico de sistemas com energia gap entre estado fundamental e estado excitado menos energético
    - $T\to\infty:C\propto T^{-2}\to0$ - Esta tendêcia é caraterística de sistemas com máximo de estados em função da energia. 
    - Assim, $C$ tem um máximo também.

## 8.2 - Probabilidade de ter uma configuração de estados
$$P(\{m_{1},\dots,m_{N}\})=\frac{1}{\Omega_{N}(E)}\chi(H(m_{1},\dots,m_{N})=E)$$
sendo que $m=\{0,1\}$ os 2 estados possíveis.

## 8.3 - Probabilidade de ter uma partícula num nível de energia
- Consideremos que estamos a estudar a partícula $1$. O seu estado será descrito como $m_{i}$. Se $m_{i}=1$ a energia da partícula é $\varepsilon$, senão é $0$.
- Podemos escrever:
$$H(m_{1},\dots,m_{N})=\sum\limits_{i=1}^{N}m_{i}\varepsilon=m_{1}\varepsilon+\sum\limits_{i=2}^{N}m_{i}\varepsilon$$
então podemos separar:
$$P(\{m_{1},\dots,m_{N}\})=\frac{1}{\Omega_{N}(E)}\chi(H(m_{1})+H(m_{2},\dots,m_{N})=E)$$

- A probabilidade de a partícula $1$ estar num certo estado é igual à probabilidade de todas as outras partículas terem energia total compatível com a partícula $m_{1}$ estar no estado que queremos:
$$\begin{align*}
P(m_{1})&= \frac{\Omega_{N-1}(E-m\varepsilon)}{\Omega_{N}(E)}\\
&= \exp\left[\ln\Omega_{N-1}(E-m\varepsilon)-\ln\Omega_{N}(E) \right]=\exp \left[\frac{S_{N-1}(E-m_{1}\varepsilon)-S_{N}(E)}{k_{B}} \right]
\end{align*}$$
em que $\Omega_{N}(E)$ é o número de microestados disponível com uma energia $E$ para $N$ partículas. No termo $\Omega_{N-1}(E-m\varepsilon)$ temos portanto o nº de estados disponíveis em que as $N-1$ partículas ocupam uma energia de $E-m_{1}\varepsilon$. Como a energia total do sistema isolado será sempre $E$, esta é a energia que "resta" além da partícula $1$.

- Usando as equações de mais acima:
$$P(m_{1})=\frac{\Omega_{N-1}(E-m\varepsilon)}{\Omega_{N}(E)}=\frac{\frac{(N-1)!}{(N-1-n+m)!(n-m)!}}{\frac{N!}{(N-n)!n!}}$$
em que:
    - $m_{1}=0\to P(0)=1-f$
    - $m_{1}=1\to P(1)=f$

- Podemos obter então uma equação generalizada para obter a probabilidade de um estado $n$:
$$P(n)=P(0)\delta_{n0}+P(1)\delta_{n1}=(1-f)(1-n)+fn=2fn+1-(n+f)$$

# 9 - Gás Ideal
- Sistema que podemos definir pelo seguinte Hamiltoniano:
$$H=\sum\limits_{i=1}^{N}\frac{\vec{p}_{i}^{2}}{2m}+V(\vec{p}_{i})$$
em que a partícula está restrita a uma caixa de volume $V$ sendo que:
$$V(\vec{r}_{i})=\begin{cases}
0 & ; & \vec{r}\in caixa \\
+\infty & ; & senão
\end{cases}$$

> ATENÇÃO : Dedução Enorme!!!

## 9.1 - Densidade de Microestados
- Atrás tinhamos: $D(E)=\int \delta(E-H(\vec{\mu}))d\vec{\mu}$. Mencionamos ainda que a constante de Planck é usada para adimensionalizar os problemas. Ora, temos então que a densidade de microestados de um gás ideal é:
$$\begin{align*}
D(E)&= \int \frac{\delta(E-H(\vec{\mu}))}{h^{3N}}d\vec{\mu}\\
&= \int \frac{\delta(E-H(\vec{r_{1}},\dots,\vec{r_{N}},\vec{p_{N}}\dots\vec{p_{N}}))}{h^{3N}} d\vec{r_{1}}\dots d\vec{r_{N}}d\vec{p_{1}}\dots d\vec{p_{N}}\\
&= \int \frac{\delta(E-\sum_{i=1}^{N}\frac{\vec{p_{i}}^{2}}{2m})}{h^{3N}} d\vec{r_{1}}\dots d\vec{r_{N}}d\vec{p_{1}}\dots d\vec{p_{N}}
\end{align*}$$
o termo do potencial nunca aparece porque é logo anulado pelo delta de Dirac.

- Podemos separar já que o argumento do delta não depende das posições:
$$\begin{align*}
D(E)&= \int \frac{1}{h^{3N}}d\vec{r_{1}}\dots d\vec{r_{N}}\int \delta\left(E-\sum\limits_{i=1}^{N} \frac{\vec{p_{i}}^{2}}{2m}\right)d\vec{p_{1}}\dots d\vec{p_{N}}\\
&= \left(\frac{V}{h^{3}} \right)^{N} \int \delta\left(E-\sum\limits_{i=1}^{N} \frac{\vec{p_{i}}^{2}}{2m}\right)d\vec{p_{1}}\dots d\vec{p_{N}}\\
\end{align*}$$
(em que $V$ é o volume da caixa, não trocar com o potencial)

- Façamos a seguinte mudança de variável:
$$\frac{p_{i}^{\alpha}}{\sqrt{2m}}=\xi_{i+3\alpha-1} \quad \quad;\quad \quad dp_{i}^{\alpha}=\sqrt{2m}~d\xi_{i+3\alpha-1}$$
em que $i$ é uma partícula das $N$ e $\alpha=\{0,1,2\}$ representa as direções $(x,y,z)$. Por exemplo: $d\vec{p}_{1}=d\xi_{0}d\xi_{3}d\xi_{6}, d\vec{p_{2}}=d\xi_{1}d\xi_{4}d\xi_{7}$. Na prática estamos a transformar este num problema em $3N$ dimensões. A ordem dos integrais não importa, e simplesmente fazemos $d\vec{p_{1}}\dots d\vec{p_{N}}=d\xi_{0}\dots d\xi_{3N-1}$. Assim:
$$\begin{align*}
&\int \delta\left(E-\sum\limits_{i=1}^{N} \frac{\vec{p_{i}}^{2}}{2m}\right)d\vec{p_{1}}\dots d\vec{p_{N}}= \\
&= (2m)^{\frac{3N}{2}}\int \delta\left(E-\sum\limits_{i=1}^{3N-1}\xi_{i}^{2}\right)d\xi_{0}\dots d\xi_{3N-1}\\
&= (2m)^{\frac{3N}{2}}\int \delta\left(E-\sum\limits_{i=1}^{3N-3}\xi_{i}^{2} -\xi_{3N-2}^{2}-\xi_{N-1}^{2}  \right)d\xi_{0}\dots d\xi_{3N-3}d\xi_{3N-2} d\xi_{3N-1}
\end{align*}$$
e podemos fazer a seguinte substituição: $\xi_{3N-2}=\rho\cos\theta~,~\xi_{3N-1}=\rho\sin\theta$. Ficamos com:
$$\begin{align*} 
&\ (2m)^{3N/2}\int\delta\left(E-\sum_{i=1}^{3N-3}\xi_i^2 - \xi_{3N-2}^2-\xi_{3N-1}^2 \right) d\xi_0\cdots d\xi_{3N-3}d\ \xi_{3N-2}\ d\xi_{3N-1} \\
=&\ (2m)^{3N/2}\int_0^{2\pi}\int_0^{+\infty}\int_\mathbb{R}\cdots\int_{\mathbb{R}}\delta\left(E-\sum_{i=1}^{3N-3}\xi_i^2 - \rho^2 \right) d\xi_0\cdots d\xi_{3N-3}\ \rho\ d\rho\ d\theta \\
=&\ (2m)^{3N/2}(2\pi)\int_0^{+\infty}\int_\mathbb{R}\cdots\int_\mathbb{R}\delta\left(E-\sum_{i=1}^{3N-3}\xi_i^2 - \rho_0^2 \right) d\xi_0\cdots d\xi_{3N-3}\ \rho_0\ d\rho_0
\end{align*}
$$
- Podemos repetir a substituição, tendo $\rho_{0}=\rho_{1}\sin\theta,\xi_{3N-3}=\rho_{1}\cos\theta$.
- Se continuarmos a repetir isto $3N-1$ vezes ficamos com:
$$(2m)^{3N/2}\Omega_{3N}\int_0^{+\infty}\delta(E-\rho^2)\rho^{3N-1}\ d\rho$$
em que $\Omega_{3N}$ é o ângulo sólido que obtemos ao repetir a substituição tantas vezes. $\rho^{2}$ é a distância ao centro em $3N$ dimensões.

- Por fim podemos substituir $\omega=\rho^{2}~,~d\omega=2\rho d\rho$:
$$\begin{align*}
(2m)^{\frac{3N}{2}}\Omega_{3N}\int_{0}^{+\infty}\delta(E-\rho^{2})\rho^{3N-1} d\rho&= (2m)^{\frac{3N}{2}} \frac{1}{2}\Omega_{3N} \int_{0}^{+\infty}\omega^{\frac{3N-2}{2}}\delta(E-\omega)d\omega\\
&= (2m)^{\frac{3N}{2}} \frac{1}{2}\Omega_{3N} \int_{0}^{+\infty}\omega^{\frac{3N}{2}-1}\delta(E-\omega)d\omega\\\\
&= (2m)^{\frac{3N}{2}} \frac{1}{2}\Omega_{3N} \int_{-\infty}^{+\infty}\omega^{\frac{3N}{2}-1}\delta(E-\omega)\Theta(\omega)d\omega\\
&= (2m)^{\frac{3N}{2}} \frac{1}{2} \Omega_{3N}E^{\frac{3N}{2}-1} \Theta(E)
\end{align*}$$
em que usamos a função de Heaviside para que o integral ficasse em $]-\infty,+\infty[$.

**Ângulo Sólido**
- Para qualquer função $f$:

$$ \begin{align*}
\int_{\mathbb{R}^{m}} f(|\vec x|) dx_{1}\dots\ dx_{m} &= \Omega_{m}\int_{0}^{+\infty}f(x) x^{m-1} dx 
\end{align*} $$

Que é o caso que temos em cima. Podemos então escrever:
$$ \begin{align*}
\Omega_{m} &= \frac{\int_{\mathbb{R}^{m}} f(|\vec x|)\ dx_{1}\dots\ dx_{m}}{\int_{0}^{+\infty}f(x)\ x^{m-1}\ dx} 
\end{align*} $$

Vamos escolher uma função $f$ fácil de fazer integrais múltiplos, pelo que optamos por uma gaussiana da seguinte forma:

$$ \begin{align*}

f(|\textbf x|) &= \exp\left(-\frac{x_1^2}{2} - \cdots - -\frac{x_m^2}{2}\right)

\end{align*} $$

- Ficamos com:
**Numerador**
$$\int_{\mathbb{R}^{m}}f(|\vec{x}|)dx_{1}\dots dx_{m}=\left[\int_\mathbb{R} \exp\left(-\frac{x^{2}}{2}\right) \right]^{m}=(2\pi)^\frac{m}{2}$$
**Denominador**
$$\begin{align*}
I_{m}&= \int_{0}^{+\infty}\exp\left(\frac{-x^{2}}{2}\right)x^{m-1}dx\\
&= \left[\frac1{m}x^{m}\exp\left(-\frac {x^{2}}2\right)\right]_0^{+\infty} + \frac1{m}\int_{0}^{+\infty}x^{m+1}\exp\left(-\frac {x^2}2\right) dx\\
&= \frac{1}{m}I_{m+2}
\end{align*}$$
ou seja: $I_{m+2}=mI_{m}$. Podemos então escrever isto como: $I_{m}=(m-2)I_{m-2}$
- É então possível deduzir:
*m par*
$$I_{m}=(m-2)!!I_{2}=(m-2)(m-4)\dots2= 2^{\frac{m-2}{2}}\left(\frac{m-2}{2}\right)!$$
(em que $I_{2}=1$)
- Aqui definimos uma propriedade que iremos usar mais abaixo:$$(m-2)!!=2^{\frac{m-2}{2}}\left(\frac{m-2}{2}\right)!$$

*m ímpar*
$$I_{m}=(m-2)!!I_{1}=(m-2)(m-4)\dots1 \sqrt{\frac{\pi}{2}}$$
(em que $I_{1}=\sqrt{\frac{\pi}{2}}$)

e o resultado final do ângulo sólido é:
$$\Omega_{m}=\begin{cases}
\frac{(2\pi)^\frac{m}{2}}{(m-2)!!} & ; & m~~par  \\
\frac{(2\pi)^\frac{m}{2}}{(m-2)!!}\sqrt{\frac2{\pi}} & ; & m~~ímpar
\end{cases}$$
- Na realidade iremos ignorar o termo $\sqrt{2/\pi}$, tendo-se o mesmo ângulo sólido para qualquer $m$.

**Resultado Final!**
$$\begin{align*}
D_{N}(E)&= \left(\frac{N}{h^{3}}\right)^{N} (2m)^{\frac{3N}{2}} \frac{~1}{2}\Omega_{3N}~E^{\frac{3N}{2}-1}\Theta(E)\\
&= \left(\frac{N}{h^{3}}\right)^{N} (2m)^{\frac{3N}{2}} \frac{1}{2}\frac{(2\pi)^\frac{3N}{2}}{(3N-2)!!}~E^{\frac{3N}{2}-1}\Theta(E)\\
&= \left(\frac{N}{h^{3}}\right)^{N} (2m)^{\frac{3N}{2}} \frac{1}{2}\frac{(2\pi)^\frac{3N}{2}}{\left(\frac{3N-2}{2}\right)!}2^{- \frac{3N-2}{2}}~E^{\frac{3N}{2}-1}\Theta(E)\\
&= \left(\frac{N}{h^{3}}\right)^{N} (2m)^{\frac{3N}{2}} \cancel{\frac{1}{2}}\frac{(2\pi)^\frac{3N}{2}}{\left(\frac{3N-2}{2}\right)!}2^{- \frac{3N}{2}+\cancel{1}}~E^{\frac{3N}{2}-1}\Theta(E)\\\\
D_N(E)&= \frac{V^{N}}{\left(\frac{3N}{2}-1\right)!}E^{\frac{3N}{2}-1} \left(\frac{2\pi m}{h^{2}} \right)^{\frac{3N}{2}}
\end{align*}$$

## 9.2 - Entropia
$$\begin{align*}
S_{N,V}(E)&= k_{B}\ln D_{N}(E)\\
&= k_BN\left[\ln V-\frac32 \ln N - \frac32\ln\frac32+\frac32+\frac32 \ln E+\frac{3}{2}\ln\left(\frac{2\pi m}{h^2}\right)\right]
\end{align*}$$
pelo meio desta demonstração usasse a Fórmula de Stirling, mas de resto é só reorganizar termos.

## 9.3 - Temperatura
$$\frac{1}{T}=\frac{\partial S}{\partial E}=\frac{k_{B}}{E}\left(\frac{3N}{2}-1\right) \to E = \left(\frac{3N}{2}-1\right)k_{B}T$$

## 9.4 - Lei dos Gases Ideiais
- Da 1ª Lei da Termodinâmica vimos que:
$$dE = TdS + Fdx \to dE=TdS+pdV$$
- Podemos escrever o diferencial da entropia na forma:
$$dS = \frac{\partial S}{\partial E}dE+\frac{\partial S}{\partial V}dV$$
- Relacionando as duas equações temos:
$$\frac{\partial S}{\partial E}=\frac{1}{T} \quad \quad;\quad \quad \frac{\partial S}{\partial V}=\frac{p}{T}$$
a primeira já sabiamos. 
- Tendo a densidade de microestados obtida acima temos:
$$\frac{\partial S}{\partial E}=\frac{k_{B}N}{V}=\frac{p}{T}$$
e temos a *lei dos gases ideiais*:
$$pV=k_{B}NT$$

## 9.5 - Distribuição de probabilidade do momento de 1 partícula
$$\begin{align*}
\rho_{N,E,V}(\vec{p_{1}})&= \int \frac{\delta(E-H_{N})}{D_{N}(E)}\delta(\vec{p}-\vec{p_{1}}) \frac{d\vec{r_{1}}\dots d\vec{r_{N}}d\vec{p_{1}}\dots d\vec{p_{N}}}{h^{3N}}\\
&= \frac{V}{D_{N}(E)h^{3}} \int \delta\left(E-\frac{\vec{p_{1}}^{2}}{2m}-H_{N-1}\right)\frac{d\vec{r_{2}}\dots d\vec{r_{N}}d\vec{p_{2}}\dots d\vec{p_{N}}}{h^{3(N-1)}}\\
&= \frac{V}{h^{3}} \frac{D_{N-1}(E-\frac{\vec{p_{1}}^{2}}{2m})}{D_{N}(E)} 
\end{align*}$$
- No 2º passo vemos que o integral que fica é o integral que descreve uma densidade de microestados $D_{N-1}\left(E-\frac{\vec{p_{1}}^{2}}{2m}\right)$. 
- Depois de muita álgebra secante e chata de escrever em $\LaTeX$ ficamos com:
$$\rho_{N,E,V}(\vec{p_{1}})=\frac{\left(\frac{3N}2-1\right)!\cdot (E-\frac{p_1^2}{2m})^{\frac{3N}{2}-1-\frac32} }{\left(\frac{3N}2-1-\frac32\right)!\cdot E^{\frac{3N}{2}-1}\cdot(2\pi m)^{3/2}}$$
e já temos uma expressão válida da densidade de probabilidade do momento de uma partícula num gás ideal. Mas podemos melhorar isto:

$$\ln\rho_{N,E,V}(\vec{p})=\ln\frac{(\frac{3N}{2}-1)!}{(\frac{3N}{2}-1- \frac{3}{2})!} + \ln\frac{(E-\frac{p^{2}}{2m})^{\frac{3N}{2}-1- \frac{3}{2}}}{E^{\frac{3N}{2}-1}}-\frac{3}{2}\ln(2\pi m)$$
em que separamos os termos em temos com fatoriais, com energia e o outro. Por uma questão de simplificação vamos simplificar este comboio termo a termo:
**1º termo** 
Usamos Stirling
$$\begin{align*}
\ln\frac{(\frac{3N}{2}-1)!}{(\frac{3N}{2}-1- \frac{3}{2})!}&\simeq \left(\frac{3N}{2} -1\right)\ln\left(\frac{3N}{2} -1\right) - \left(\frac{3N}{2} -1\right) - \left(\frac{3N}{2}-1-\frac{3}{2} \right)\ln\left(\frac{3N}{2}-1-\frac{3}{2} \right)\\
&\quad\quad\quad\quad+\left(\frac{3N}{2}-1-\frac{3}{2} \right)\\
&=  \left(\frac{3N}{2} -1\right)\ln\frac{\frac{3N}{2}-1}{\frac{3N}{2}-1-\frac{3}{2}} - \frac{3}{2} + \frac{3}{2}\ln\left(\frac{3N}{2}-1-\frac{3}{2}\right)\\
&\sim \frac{3}{2}\ln\left(\frac{3N}{2}-1\right)
\end{align*}$$
Alerta aproximações à fisico:
    - logo no primeiro termo ignoramos os termos $\ln\sqrt{2\pi N}$ porque crescem mais devagar que os restantes
    - Na passagem para a última linha fazemos a aproximação $\frac{3N}{2}-1\simeq \frac{3N}{2}-1- \frac{3}{2}$, o que é "verdade" se $N$ for suficientemente elevado. Assim, o primeiro termo anula-se
    - Deprezamos o $\frac{-3}{2}$ solto

**2º termo**
- Simplesmente reorganizamos cenas e usamos as propriedades dos logaritmos:
$$\begin{align*}
\ln \frac{(E-\frac{p^{2}}{2m})^{\frac{3N}{2}-1- \frac{3}{2}}}{E^{\frac{3N}{2}-1}}&= \ln \frac{E^{\frac{3N}{2}-1-\frac{3}{2}}(1-\frac{p^{2}}{2mE})^{\frac{3N}{2}-1- \frac{3}{2}}}{E^{\frac{3N}{2}-1}}\\
&= \ln\frac{\left(1-\frac{p^{2}}{2mE}\right)^{\frac{3N}{2}-1-\frac32}}{E^{\frac{3}{2}}}\\
&= \left(\frac{3N}{2}-1-\frac{3}{2}\right)\ln\left(1-\frac{p^{2}}{2mE}\right) - \frac{3}{2}\ln E
\end{align*}$$

- Sendo $\ln(1-x)=-\sum_{n=1}^{+\infty}\frac{x^{n}}{n}$ podemos expandir o 1º logaritmo:
$$\begin{align*}
\ln \frac{(E-\frac{p^{2}}{2m})^{\frac{3N}{2}-1- \frac{3}{2}}}{E^{\frac{3N}{2}-1}}&= \left(\frac{3N}{2}-1-\frac{3}{2}\right) \cdot \left[-\frac{p^{2}}{2mE} - \frac{1}{2} \left(\frac{p^{2}}{2mE}\right)^{2} - \frac{1}{3}\left(\frac{p^{2}}{2mE}\right)^{3}\dots \right]- \frac{3}{2}\ln E\\
&\simeq -\left(\frac{3N}{2}-1-\frac{3}{2}\right)\frac{p^{2}}{2mE} - \frac{3}{2}\ln  E\\
&\approx -\left(\frac{3N}{2}-1\right)\frac{p^{2}}{2mE} - \frac{3}{2}\ln  E
\end{align*}$$
em que consideramos $N\gg p$ e anulamos todos os termos da série a partir do 2º. Além disso, para manter coerência com a dedução atrás consideramos $\frac{3N}{2}-1\simeq \frac{3N}{2}-1- \frac{3}{2}$

**Versão final**
$$\begin{align*}
\ln\rho_{N,E,V}(\vec{p})&= \ln\frac{(\frac{3N}{2}-1)!}{(\frac{3N}{2}-1- \frac{3}{2})!} + \ln\frac{(E-\frac{p^{2}}{2m})^{\frac{3N}{2}-1- \frac{3}{2}}}{E^{\frac{3N}{2}-1}}-\frac{3}{2}\ln(2\pi m)\\
&\approx \frac{3}{2}\ln\left(\frac{3N}{2}-1\right) -\left(\frac{3N}{2}-1\right)\frac{p^{2}}{2mE} - \frac{3}{2}\ln  E -\frac{3}{2}\ln(2\pi m)\\
&= \frac{3}{2}\ln\left(\frac{3N}{2}-1\right)-\frac{3}{2}\ln  \frac{E}{2\pi m} -\left(\frac{3N}{2}-1\right)\frac{p^{2}}{2mE}
\end{align*}$$

que nos dá:
### Distribuição de Maxwell-Boltzmann
$$\begin{align*}
\rho_{N,E,V}(\vec{p})&= \frac{\left(\frac{3N}{2}-1 \right)^{\frac{3}{2}}}{\left(\frac{E}{2\pi m}\right)^{\frac{3}{2}}} \exp\left[-\left(\frac{3N}{2}-1\right)\frac{p^{2}}{2mE}\right]\\
\end{align*}$$
usando a relação $E = \left(\frac{3N}{2}-1\right)k_{B}T$ obtida atrás:
$$\begin{align*}
\rho_{N,E,V}(\vec{p})&= \frac{\exp \left(-\frac{p^{2}}{2mk_{B}T} \right)}{(2\pi mk_{B}T)^{\frac{3}{2}}}
\end{align*}$$

## 9.6 - Paradoxo de Gibbs
- Acima determinamos que:
$$\begin{align*}
S_{N,V}(E)&= k_{B}\ln D_{N,V}(E)=k_BN\left[\ln V-\frac32 \ln N - \frac32\ln\frac32+\frac32+\frac32 \ln E+\frac{3}{2}\ln\left(\frac{2\pi m}{h^{2}}\right)\right]\\
&= k_{B}N \left[\ln V - \frac{3}{2}\ln \frac{3N}{2} + \frac{3}{2}\ln \left( E\frac{2\pi m}{h^{2}}\right) + \frac{3}{2}\ln e \right]\\
&= k_{B}N \left[\ln V + \ln \frac{(Ee)^{\frac{3}{2}} \left(\frac{2\pi m}{h^{2}}\right)^{\frac{3}{2}}}{\left(\frac{3N}{2}\right)^{\frac{3}{2}}} \right]\\
&= k_{B}N \left[\ln V + \ln \left((k_{B}Te)^{\frac{3}{2}} \left(\frac{2\pi m}{h^{2}}\right)^{\frac{3}{2}}\right)\right]\\
&= k_BN\left[\ln V + \ln \left[\frac{2\pi mk_BTe}{h^2}\right]^{3/2}\right] \\
&= k_BN\left[\ln V + \sigma\right]
\end{align*}$$ em que podemos definir (em que se usou a equação da energia interna de um gás ideal, $E=\frac{3}{2}Nk_{B}T$):
$$\sigma \equiv \ln\left[\frac{2\pi e mk_BT}{h^2}\right]^{3/2}$$

**Extensividade**
- Vejamos se a entropia é extensiva:
$$\begin{align*}
S_{\lambda N,\lambda V}(\lambda E)&= k_{B} \lambda N[\ln \lambda V+\sigma]\\
&= \lambda[k_{B}N(\ln V + \ln \lambda + \sigma)]\\
&= \lambda[S_{N,V}(E)+k_{B}\ln \lambda]\\
&= \lambda S_{N,V}(E) \left(1+ \frac{\ln\lambda}{\ln V+\sigma} \right)
\end{align*}$$
ou seja, a entropia não é extensiva. Se fosse tínhamos $S_{\lambda N,\lambda V}(E)=\lambda S_{N,V}(E)$. Isto é equivalente a dizer que: "a entropia de um sistema resultante de duplicar o tamanho e número de partículas de um sistema NÃO é $2S$". 
    - Acima dissemos e mostramos que a entropia é aditiva. Isto não contradiz essa parte? É por estarmos a tratar gases ideiais?

**Paradoxo de Gibbs Clássico**
- Consideremos um contentor com 1 parede no meio. Esta separa 2 gases ideais iguais. Assim:
$$\sigma_{1}=\sigma_{2}=\sigma \quad \quad;\quad \quad \frac{N_{1}}{V_{1}}=\frac{N_{2}}{V_{2}}$$
- Ao remover a parede fica:
$$S=k_{B}(N_{1}+N_{2})[\ln(V_{1}+V_{2})+\sigma]$$
assim, a variação de entropia ao tirar a parede é:
$$\begin{align*}
\Delta S&= S-S_{1}-S_{2}\\
&= k_{B}(N_{1}+N_{2})[\ln(V_{1}+V_{2})+\sigma] - k_{B}N_{1}(\ln V_{1}+\sigma) - k_{B}N_{2}(\ln V_{2}+\sigma)\\
&= k_{B}N_{1}\ln\frac{V_{1}+V_{2}}{V_{1}}+k_{B}N_{2}\ln\frac{V_{1}+V_{2}}{V_{2}} >0
\end{align*}$$
pelo que a entropia aumenta ao retirar a parede.

- O paradoxo clássico de Gibbs surge do facto que se voltarmos a colocar a parede estamos a repor o sistema no estado inicial, pelo que a entropia deveria baixar.
- Ora, sendo os gases iguais, a existência ou não de uma parede não deveria afetar em nada o sistema.

**Solução do Paradoxo**
- Na realidade ao repor a parede o sistema NÃO volta ao estado inicial. ficamos com 2 sistemas com os mesmos volumes e até talvez mesmos números de partículas. Mas muito certamente não temos as mesmas partículas que tinhamos inicialmente.
- Aliás, sendo este um gás ideal, as partículas são indistinguíveis. Desta forma, estamos a fazer uma contagem excessiva de estados. Para corrigir isto basta definir:
$$D(E)=\int \frac{\delta(E-H(\vec\mu))}{N!\cdot h^{3N}}d\vec\mu$$
(sendo que originalmente tínhamos $D(E)= \int \frac{\delta(E-H(\vec{\mu}))}{h^{3N}}d\vec{\mu}$)

- Desta forma a entropia pode ser corrigida e fica definida como:
$$\begin{align*}
S_{N,V}(E)&= k_{B}(\ln D_{N,V}(E))\\
&\approx k_{B}N(\ln V+\sigma)-k_{B}\ln N!\\
&\approx k_{B}N(\ln V++\sigma)-k_{B}N\ln N + k_{B}N\\
&= k_{B}N\left(\ln \frac{V}{N}+\sigma_{T}\right)
\end{align*}$$
em que definimos:
$$\sigma_{T} \equiv \ln\left[\frac{2\pi e mk_BT}{h^2}\right]^{3/2}+1$$

pelo que agora a variação de entropia já será:
$$\begin{align*}
\Delta S &= S - S_1 - S_2 \\
&= k_B(N_1+N_2)\left[\ln\frac{V_1+V_2}{N_1+N_2} + \sigma_T\right] - k_BN_1\left(\ln \frac{V_1}{N_1}+\sigma_T\right) - k_B N_2\left(\ln \frac{V_2}{N_2}+\sigma_T\right) \\
&= k_B N_1\left[\ln\frac{V_1+V_2}{N_1+N_2}-\ln \frac{V_1}{N_1}\right]+k_B N_2\left[\ln\frac{V_1+V_2}{N_1+N_2}-\ln \frac{V_2}{N_2}\right]
\end{align*}$$
em que, se os gases tiverem densidades iguais ($\frac{V_1+V_2}{N_1+N_2} = \frac{V_1}{N_1} = \frac{V_2}{N_2}$) fica $\Delta S=0$

## 9.7 - Gases Diferentes
- Consideremos agora que temos gases diferentes. A densidade de estados do sistema seria:
$$D(E) = \int\frac{\delta(E_1 - H_1(\vec \mu_1))}{N_1!\cdot h^{3N_1}}\ d\vec \mu_1\int\frac{\delta(E_2 - H_2(\vec \mu_2))}{N_2!\cdot h^{3N_2}}\ d\vec\mu_2$$
o que faria a entropia aumentar ao tirar a parede.

## 9.8 - Generalização para $d$ dimensões
- Simplesmente fazemos:
$$D^{(d)}(E) = \int\frac{\delta(E - H(\boldsymbol \mu))}{N!\cdot h^{dN}}\ d\boldsymbol \mu$$
o que, após matemática, nos daria:
$$\frac1T = \frac{k_B}{E}\left(\frac{Nd-1}{2}\right) ~~\to~~ E \approx \frac{d}{2}Nk_B T$$

