# 1 - Sistema Isolado em conjunto canónico
- No microcanónico tínhamos que a energia está bem definida e a temperatura (de equilíbrio) surge como consequência disso.
- No entanto, de um ponto de vista termodinâmico, a temperatura e a energia são ambas funções de estado. Assim, podemos definir um sistema em que a temperatura está definida e a partir dela podemos obter a energia: o ensemble / **conjunto Canónico**.
- Assim os macroestados são definidos por $M\equiv (T,\vec{X})$. Assim, podemos considerar o calor fornecido ao sistema.

![[canonico.png]]
- Assim, consideremos um sistema $S$. Ele é mantido a temperatura constante através do contacto com o reservatório $R$ (que consiste num outro sistema macroscópico que é grande o suficiente para que a sua temperatura não mude ao interagir com $S$).
- Assim, o hamiltoniano deste sistema total é:
$$H(\vec{\mu})=H_{S}(\vec{\mu})+H_{R}(\vec{\mu})$$
em que $N_{S}\ll N_{R}$. Temos ainda $\vec{\mu}=\vec{\mu_{S}}\otimes\vec{\mu_R}$ (em que o produto tensorial simplesmente representa a junção/combinação de todos os microestados possíveis nos sistemas $S,R$). Iremos ainda assumir que os sistemas estão em equilíbrio térmico.

- Podemos definir a probabilidade de estar no **estado de equilíbrio** $\mu_{E}$:
$$P_{E,\vec{X},N}(\vec{\mu})=\frac{\chi_{E}(E-H(\vec{\mu}))}{\Omega_{S+R}(E)}$$

## 1.1 - Probabilidade de um certo estado (de $S$)
$$\begin{align*}
P_{E,\vec{X},N}(\vec{\mu_{S}})&= \sum\limits_{\vec{\mu_{R}}}P_{E,\vec{X},N}(\vec{\mu_{S}}\otimes \vec{\mu_{R}})\\
&= \frac{\Omega_{R}(E-H_{S}(\vec{\mu_{S}}))}{\Omega_{S\otimes R}(E)}\\
&= \frac{\exp\left(\frac{S_{R}(E-H_{S}(\vec{\mu_{S}}))}{k_{B}}\right)}{\exp\left(\frac{S_{S\otimes R}(E)}{k_{B}}\right)}
\end{align*}$$
em que $E$ é a energia do sistema total. Ou seja, (focando-me na segunda linha) a probabilidade de ter um certo estado $\vec{\mu_{S}}$ no sistema $S$ é a probabilidade de o sistema $R$ ter energia $E-H_{S}(\mu_{S})$. Ou seja, estando o sistema total isolado, será a probabilidade de o sistema $R$ ter a energia que "sobra" do estado $\vec{\mu_{S}}$.
- O último passo vem de $S=k_{B}\ln \Omega(E)$

- Podemos espandir $S_{R}$ em Taylor ($f(x + h) = f(x) + f′(x)h + f′′(x) \frac{h_{2}}{2!} +\dots$):
$$\begin{align*}
S_{R}(E-H_{S}(\vec{\mu_{S}}))&= S_{R}(E)-\frac{\partial S}{\partial E}H_{S}(\vec{\mu_{S}})+\dots\\
&\approx S_{R}(E)-\frac{H_{S}(\vec{\mu_{S}})}{T}
\end{align*}$$
em que anulamos todos os termos a partir da 1ª derivada porque se $N_{R}\gg N_{S}$ então $E\gg H_{S}(\vec{\mu_{S}})$ e podemos desprezar os termos. De notar ainda que usamos $\partial_{E}S=1/T$.

e temos:
$$P_{E,\vec{X},N}(\vec{\mu_{S}})\approx\frac{\exp\left(\frac{S_{R}(E)}{k_{B}}\right)\exp\left(- \frac{H_{S}(\vec{\mu_{S}})}{k_{B}T}\right)}{\exp\left(\frac{S_{S\otimes R}(E)}{k_{B}}\right)}$$
(pelo que quanto maior for o rácio $N_{R}/N_{S}$ melhor será a aproximação)

## 1.2 - Distribuição de Boltzmann
- Temos:
$$P_{\vec{X},N}(\vec{\mu})=\frac{e^{-\beta H(\vec{\mu})}}{Z_{\vec{X},N}}$$
em que
$$\beta=\frac{1}{k_{B}T} \quad \quad;\quad \quad Z_{\vec{X},N}=\sum\limits_{\vec{\mu}}e^{-\beta H(\vec{\mu})}$$
(recordemos que $Z$ é a função partição)
- Desde logo notemos que esta função de probabilidade é idêntica em forma à da probabilidade de ter um certo momento que obtivemos para um gás ideal.

## 1.3 - Valor médio da energia:
$$\begin{align*}
\langle H\rangle &= \frac{1}{Z}\sum\limits H e^{-\beta H(\mu)}\\
&= \frac{-1}{Z}\frac{\partial}{\partial\beta}\sum\limits e^{-\beta H(\mu)}\\
&= \frac{- 1}{Z}\frac{\partial}{\partial\beta}Z\\
&= - \frac{\partial}{\partial\beta}\ln Z
\end{align*}$$
em que temos a propriedade $\frac{\partial}{\partial x}\ln f(x)=\frac{1}{f(x)} \frac{\partial f}{\partial x}$

## 1.4 - Capacidade Térmica
- Podemos então definir a capacidade térmica:
$$\begin{align*}
C_{V}&= \frac{d\langle H\rangle}{dT}\\
&= \frac{d}{dT} \frac{\partial}{\partial \beta}(-\ln Z)\\
&= \frac{\partial}{\partial \beta} \frac{d\beta}{dT}\frac{\partial}{\partial \beta}(-\ln Z)\\
&= \frac{1}{k_{B}T^{2}} \frac{\partial^{2}}{\partial\beta^{2}}\ln Z\\
&= \frac{1}{k_{B}T^{2}} \frac{\partial}{\partial \beta} \left(\frac{1}{Z}\frac{\partial Z}{\partial\beta}\right)\\
&= \frac{1}{k_{B}T^{2}} \left[ - \frac{1}{Z^{2}}\frac{\partial Z}{\partial\beta}\cdot \frac{\partial Z}{\partial\beta} + \frac{\partial^{2}Z}{\partial\beta^{2}}\cdot \frac{1}{Z} \right]\\
&= \frac{1}{k_{B}T^{2}} (\langle H^{2}\rangle-\langle H\rangle^{2})
\end{align*}$$
em que esta variância escala com $N$.

## 1.5 - Distribuição da Energia
- Aqui notamos uma coisa. De uma forma **geral**, o conjunto canónico opera de forma contínua. No microcanónico para obter uma densidade de probabilidade de um microestado $\mu$ simplesmente dividiamos o número de estados que contêm $\mu$ pelo total. Aqui, a densidade da energia é (linguagem muito incorreta incoming) a média de estados  em que a energia é aquela associada ao microestado $\mu$.
$$\begin{align*}
\rho(E)&= \langle \delta(E-H(\vec{\mu}))\rangle\\
&= \frac{1}{Z}\sum\limits_{\mu}\delta(E-H(\mu))e^{-\beta H(\mu)}\\
&= \frac{1}{Z}\exp (-\beta E)\Omega(E)\\
&= \frac{1}{Z}\exp\left(\frac{S(E)}{k_{B}}-\beta E\right)
\end{align*}$$
em que no final se usou $S(E)=k_{B}\ln\Omega(E)$. A densidade de estados aparece devido ao Delta de Dirac.

**Probabilidade Máxima**
- Uma vez que $\exp(-\beta E)$ decai muito rapidamente e $\Omega(E)$ aumenta muito rapidamente deveremos ter uma energia com probabilidade máxima, $E^{*}$. Assim:
$$\begin{align*}
\frac{d\rho}{dE}(E^{*})&= 0\\
\frac{d}{dE}\left(\frac{1}{Z}e^{\frac{S}{k_{B}}}e^{-\beta E}\right)&= 0\\ 
\frac{1}{k_{B}}\frac{dS}{dE}e^{\frac{S}{k_{B}}}e^{-\beta E} -\beta e^{-\beta E}e^{\frac{S}{k_{B}}}&= 0\\
\frac{dS}{dE}&= \beta k_{B}=\frac{1}{T}
\end{align*}$$
ou seja, a energia que tem maior probabilidade é aquela em que $\partial_{E}S=1/T$.

**Aproximação**
- Vamos expandir $\frac{S(E)}{k_{B}}-\beta E$ em torno de $E^{*}$ ($f(x)=f(a) + \frac{df}{dx}(a)(x-a) + \frac{d^{2}f}{dx^{2}}(a)\frac{(x-a)^{2}}{2!}\dots$ em que $f(E)=\frac{S(E)}{k_{B}}-\beta E$):
$$\begin{align*}
\frac{S(E)}{k_{B}}-\beta E&= \frac{S(E^{*})}{k_{B}}-\beta E^{*} + \underbrace{\frac{d}{dE}\left(\frac{S(E^{*})}{k_{B}}-\beta E^{*}\right)}_{=0}(E-E^{*}) + \frac{1}{2}\frac{d^{2}}{dE^{2}}\left(\frac{S(E^{*})}{k_{B}}-\beta E^{*}\right)(E-E^{*})^{2}+\dots\\
&= \frac{S(E^{*})}{k_{B}}-\beta E^{*} + \frac{1}{2k_{B}} \frac{d^{2}S}{dE^{2}}(E^{*})(E-E^{*})^{2}+\dots\\
\end{align*}$$
como $S,E\propto N$ então: $\frac{d^{2}S}{dE^{2}}\propto \frac{1}{N}$

- E ficamos com:
$$\rho(E)\approx \frac{\exp\left(\frac{S(E^{*})}{k_{B}}-\beta E^{*}\right)}{Z}\exp\left(- \frac{1}{2}\Biggr|\frac{d^{2}S}{dE^{2}}(E^{*})\Biggr|(E-E^{*})^{2}\right)$$
pelo que a energia por partícula $\rho(E/N)$ será uma gaussiana de valor médio $E^*/N$ e desvio padrão $1/\sqrt N$. Desta forma temos:
$$\begin{align*}
Z(\beta) &= \int Z \rho(E)dE\\
&\approx \exp\left(\frac{S(E^{*})}{k_{B}}-\beta E^{*}\right)\int\exp\left(- \frac{1}{2}\Biggr|\frac{d^{2}S}{dE^{2}}(E^{*})\Biggr|(E-E^{*})^{2}\right)dE\\
&= \exp\left(\frac{S(E^{*})}{k_{B}}-\beta E^{*}\right) \sqrt{\frac{2\pi}{\Biggr|\frac{d^{2}S}{dE^{2}}(E^{*})\Biggr|}}
\end{align*}$$

## 1.6 - Energia Livre de Helmholtz
- Podemos definir:
$$F(E^{*})=E^{*}-TS(E^{*})\approx - \frac{1}{\beta} \ln Z$$
em que, sendo $N$ suficientemente elevado podemos dizer $\frac{d^{2}S}{dE^{2}}(E^{*})\to0$. Assim fica:
$$\begin{align*}
\rho(E)Z&= \exp\left(\frac{S(E^{*})}{k_{B}}-\beta E^{*}\right)\\
\ln(\rho(E)Z)&= \frac{S(E^{*})}{k_{B}}-\beta E^{*}\\
\frac{1}{\beta}\ln(\rho(E)Z)&= \frac{S(E^{*})}{\beta k_{B}}-E^{*}\\
-\frac{1}{\beta}\ln(\rho(E)Z)&= E^{*}-TS(E^{*})\\
-\frac{1}{\beta}\ln(Z) - \cancelto{=0?}{\frac{1}{\beta} \ln(\rho(E))}&= E^{*}-TS(E^{*})=F(E^{*})\\
\end{align*}$$
e temos:
$$F(E^{*})\approx - \frac{1}{\beta}\ln Z$$

- Podemos ainda determinar a derivada na temperatura:
$$\begin{align*}
\frac{dF}{dT}(E^{*})&= \frac{dE^{*}}{dT}-\frac{d(TS(E^{*}))}{dT}\\
&= \frac{dE^{*}}{dT} - S(E^{*}) - T\frac{dS}{dT}(E^{*})\frac{dE^{*}}{dT}\\
&= \frac{dE^{*}}{dT} - S(E^{*}) - T\frac{1}{T}\frac{dE^{*}}{dT}\\
&= -S(E^{*})
\end{align*}$$
em que usamos o máximo de entropia: $\frac{dS}{dT}(E^{*})=\frac{1}{T}$. O resultado obtido bate certo com o que obtivemos em física térmica.
- Com isto podemos escrever:
$$\rho(E)=\frac{1}{Z}\exp\left(- \frac{F(E)}{k_{B}T}\right)$$

# 2 - Princípio de Equipartição
- Consideremos que um sistema é descrito por um hamiltoniano $H(\vec{p},\vec{q})$.
- Consideremos agora que reescrevemos o Hamiltoniano comm os termos de 1 partícula soltos ($\alpha,\gamma$ são constantes):
$$H(q_{i},p_{i})=\alpha q_{i}^{2}+\gamma p_{i}^{2} + H(q_{1},\dots,q_{i-1},q_{i+1},\dots,q_{N};p_{1},\dots,p_{i-1},p_{i+1},\dots,p_{N})$$
o princípio de equipartição diz-nos que a energia média associada a estas coordenadas é:
$$\langle\alpha q_{i}^{2}\rangle=\frac{1}{2}k_{B}T \quad \quad;\quad \quad \langle\gamma p_{i}^{2}\rangle= \frac{1}{2}k_{B}T$$
- Isto significa que, em média, por cada termo do hamiltoniano a energia aumenta em $\frac{1}{2}k_B T$

# 3 - Calor e Trabalho no Canónico
- Consideremos que se causa uma variação $\delta X$ nos parâmetros externos do sistema:
$$H(X+\delta X,\mu)=H(X,\mu)+\frac{\partial H}{\partial X}\delta X$$
em que podemos definir uma força generalizada:
$$\frac{\partial H}{\partial x_{i}}=-F_{i}$$
(isto bate certo em termos de unidades. Em $\frac{\partial H}{\partial X}\delta X$ temos Força x Distância = Energia)

**Energia Média**
- Como vimos acima, podemos definir a energia média de um sistema como:
$$\langle H\rangle=\int \rho(X,\mu)H(X,\mu)d\mu \quad \quad;\quad \rho(X,\mu)=\frac{\exp(-\beta H)}{Z}$$
- Ao variar os parametros externos temos: $\langle H\rangle\to \langle H\rangle + dx_{i}\langle H\rangle$ em que:
$$\begin{align*}
dx_{i}\langle H\rangle &= \int \rho \delta_{x_{i}}H+H \delta_{x_{i}}\rho~d\mu \\
&= \int \rho\frac{\partial H}{\partial x_{i}}\delta_{x_{i}}+H \delta_{x_{i}}\rho~d\mu \\
&= -\langle F_{i}\rangle \delta_{x_{i}} + \int H \delta_{x_{i}}\rho~d\mu \\
\end{align*}$$
**Trabalho**
- Na equação acima, podemos identificar o primeiro termo como sendo o termo de trabalho (tal como disse atrás, temos Força x Distância)
- Podemos desenvolvê-lo:
$$\begin{align*}
\delta W&= \int \rho\frac{\partial H}{\partial x_{i}}\delta_{x_{i}} ~d\mu\\
&= \frac{\delta_{x_{i}}}{Z}\int \frac{\partial H}{\partial x_{i}}e^{-\beta H}d\mu \\
&=   \frac{\delta_{x_{i}}}{Z} \cdot \left(- \frac{1}{\beta} \right) \frac{\partial}{\partial x_{i}}\int e^{-\beta H}d\mu\\
&= - \frac{\delta_{x_{i}}}{\beta Z}\frac{\partial Z}{\partial x_{i}}\\
&= - \delta_{x_{i}} \frac{\partial F}{\partial x_{i}}\\
&= - \left[ F(x_{i}+\delta_{x_{i}}) - F(x_{i}) \right]
\end{align*}$$
em que $F$ é a energia livre de Helmholtz e usamos $F(E^{*})\approx - \frac{1}{\beta}\ln Z$.
- Este é o trabalho realizado *pelo* sistema e será o simétrico da variação da sua energia livre. Ou seja, o trabalho realizado é a energia livre que é "perdida".

**Calor**
- Pela 1ª Lei da Termodinâmica, o 1º termo da equação da energia média ser o trabalho implica que o 2º termo é o **calor**.

- No microcanónico tínhamos que a entropia do sistema é dada por $S = k_{B}\ln \Omega(E)$. Ora, no macrocanónico a equação equivalente é:
$$S=-k_{B}\int \rho\ln \rho ~d\mu $$
- Ora, podemos escrever:
$$\begin{align*}
d_{x_{i}}S&= -k_{B} \int \delta_{x_{i}}\rho\ln \rho + \rho \frac{1}{\rho}\delta_{x_{i}}\rho~d\mu \\
&= -k_{B} \int \delta_{x_{i}} \rho [-\beta H - \ln Z] + \delta_{x_{i}}\rho~d\mu \\
&= \frac{1}{T}\int H \delta_{x_{i}}\rho d\mu + k_{B}\cancelto{=1?}{\ln Z}\int \delta_{x_{i}}\rho d\mu - k_{B}\int \delta_{x_{i}}\rho d\mu \\
&= \frac{1}{T}\int H \delta_{x_{i}}\rho d\mu
\end{align*}$$
de onde verificamos que este termo representa o calor, pela a relação $\mathscr{d}Q = TdS$.

# 4 - Função partição de Hamiltonianos sem interações
- Temos um hamiltoniano do tipo:
$$H(\mu)=\sum\limits_{i=1}^{N}H_{i}(\mu_{i})$$
- Como teremos funções $H_{i}$ idênticas para todas as partículas fica:
$$Z_{N}=\sum\limits_{\mu}e^{-\beta H}=(Z_{1})^{N} \quad \quad \textsf{(partículas iguais)}$$
se por acaso as partículas forem distintas temos:
$$Z_{N}=\frac{(Z_{1})^{N}}{N!} \quad \quad \textsf{(partículas distinguíveis)}$$

# 5 - Sistema a 2 níveis
- Vejamos este sistema, que já vimos no ensemble microcanónico.
- O hamiltoniano é definido por:
$$H=\sum\limits_{i=1}^{N}n_{i}\varepsilon$$
em que $n_{i}=\{0,1\}$ para cada partícula $i$ (ou o hamiltoniano da partícula é $0$ ou é $\varepsilon$ - 2 níveis de energia possíveis)

## 5.1 - Distribuição de probabilidade
- Temos, como sempre no canónico, que a probabilidade de a energia do sistema ser $H(\mu)$ é:
$$P(\mu)=\frac{e^{-\beta H(\mu)}}{Z_{N}(\beta)}$$
em que $\mu=(n_{1},n_{2},\dots,n_{N})$ é um vetor que tem os estados das N partículas mas eu não vou indicar.

- Desde logo, precisamos de $Z_{N}$

**Função de Partição**
- Conforme indicado acima:
$$Z_{N}(\beta)=\sum\limits_{\mu}e^{-\beta H(\mu)}=\left(\sum\limits_{n1=0,1}e^{-\beta\varepsilon n_{1}}\right)^{N}= (1+e^{-\beta\varepsilon})^{N}$$
daqui surge naturalmente uma sequência de coisas:
**Energia Média**
$$\begin{align*}
\langle E\rangle&= - \frac{d}{d\beta}\ln Z\\
&= -N \frac{d}{d\beta} \ln(1+e^{-\beta\varepsilon})\\
&= -N \frac{-\varepsilon e^{-\beta\varepsilon}}{1+e^{-\beta\varepsilon}} \\
&= \frac{N\varepsilon}{e^{\beta\varepsilon}+1} 
\end{align*}$$
**Capacidade térmica**
$$\begin{align*}
C&= \frac{d\langle E\rangle}{dT}\\
&= N\varepsilon \frac{d}{dT}\frac{1}{e^{\beta\varepsilon}+1}\\
&= N\varepsilon \frac{d\beta}{dT}\frac{d}{d\beta}\frac{1}{e^{\beta\varepsilon}+1}\\
&= - \frac{N\varepsilon}{k_{B}T^{2}} \cdot \frac{-e^{\beta\varepsilon}}{(e^{\beta\varepsilon}+1)^{2}} = \frac{N\varepsilon}{k_{B}T^{2}} \frac{e^{\beta\varepsilon}}{(1+e^{\beta\varepsilon})^{2}}
\end{align*}$$

**Energia Livre**
$$F=- \frac{1}{\beta}\ln Z=- \frac{N}{\beta}\ln(1+e^{-\beta \varepsilon})$$

**Entropia**
$$\begin{align*}
S&= - \frac{dF}{dT}\\
&= -N \frac{d\beta}{dT} \frac{d}{d\beta} \left[- \frac{1}{\beta}\ln\left(1+e^{-\beta\varepsilon}\right) \right]\\
&= \frac{N}{k_{B}T^{2}} \left[ \frac{1}{\beta^{2}}\ln\left(1+e^{-\beta\varepsilon}\right) + \frac{1}{\beta}\frac{\varepsilon e^{-\beta\varepsilon}}{1+e^{-\beta\varepsilon}} \right]\\
&= \frac{1}{T} \left[N \ln (1+e^{-\beta\varepsilon}) + \frac{\varepsilon e^{-\beta\varepsilon}}{1+e^{-\beta\varepsilon}} \right]\\
&= \frac{1}{T}\left[-F + \frac{\varepsilon}{e^{\beta\varepsilon}+1} \right]\\
&= - \frac{F}{T} + \frac{\langle E\rangle}{T}
\end{align*}$$
tendo-se verificado a relação $E=F+TS$.

**Distribuição de probabilidade**
- Já determinamos várias coisas sobre o sistema em estudo, mas voltemos ao objetivo inicial e vamos determinar a distribuição de probabilidade de 1 partícula:
$$\begin{align*}
P(n_{1}=n) &= \langle \delta_{n_{1},n}\rangle\\
&= \frac{\sum_{\mu} e^{-\beta H(\mu)} \delta_{n_{1},n}}{Z}\\
&= \frac{e^{-\beta\varepsilon n}(1+e^{-\beta\varepsilon})^{N-1}}{(1+e^{-\beta\varepsilon})^{N}}\\\\
P(n)&= \frac{e^{-\beta\varepsilon n}}{1+ e^{-\beta\varepsilon}}=\begin{cases}
\frac{1}{1+e^{-\beta\varepsilon}} & ; & n=0\\
\frac{1}{1+e^{\beta\varepsilon}} & ; & n=1\\
\end{cases}
\end{align*}$$
nota sobre o 3º passo: $e^{-\beta\varepsilon n}$ está associado à probabilidade de ter 1 partícula no estado $n=0,1$ e o termo $(1+e^{-\beta\varepsilon})^{N-1}$ associado às combinações todas que conseguimos fazer com as restantes $N-1$ partículas. Ao dividir pela função partição estamos a "normalizar" a equação.  

# 6 - Gás Ideal
- Mais um caso que vimos no microcanónico.
- Temos:
$$H = \sum\limits_{i=1}^{N} \frac{\vec{p}_{i}^{~2}}{2m} + B(\vec{r_{i}})$$
**Função de Partição**
- Para 1 partícula temos:
$$\begin{align*}
Z_{1}&= \int e^{-\beta H}d\mu\\
&= \int \exp\left(-\beta \frac{\vec{p}^{~2}}{2m}-\beta V(\vec{r})\right)\frac{d\vec{r}d\vec{p}}{h^{3}}\\
&= \frac{V}{h^{3}}\int \exp\left(-\beta \frac{p_{x}^{2}+p_{y}^{2}+p_{z}^{2}}{2m}\right)dp_{x}dp_{y}dp_{z}\\
&= \frac{V}{h^{3}} \left(\frac{2\pi m}{\beta}\right)^{\frac{3}{2}}
\end{align*}$$
em que no último passo simplesmente temos a solução do integral gaussiano em 3D dos momentos. Não percebi muito bem porquê que o potencial desapareceu ao separar o integral em posições e momentos, ficando apenas o volume $V$.

- Podemos ainda definir o **comprimento de onda térmico** $\lambda_{T}$ tendo-se:
$$Z_{1}= \frac{V}{\lambda_{T}^{3}} \quad \quad;\quad \quad \lambda_{T}= \frac{h}{\sqrt{2\pi mk_{B}T}}$$
e para as $N$ partículas fica:
$$Z_{N}=\frac{(Z_{1})^{N}}{N!}=\frac{V^{N}}{N! \cdot \lambda_{T}^{3N}}$$
de notar que estamos a considerar que as partículas são distinguíveis (?!)

**Energia Média**
$$\begin{align*}
\langle E\rangle&= - \frac{d}{d\beta}\ln Z\\
&= - \frac{d}{d\beta}(N\ln Z_{1}-\ln N!)\\
&= -N \frac{d}{d\beta}\ln \left(\frac{V}{h^{3}} \left(\frac{2\pi m}{\beta}\right)^{\frac{3}{2}}\right)\\
&= -N \frac{d}{d\beta}\left(\ln\left(\frac{V}{h^{3}} \left(2\pi m\right)^{\frac{3}{2}}\right) + \ln \left(\frac{1}{\beta^{\frac{3}{2}}}\right)\right)\\
&= - N \frac{d}{d\beta} \left(\frac{-3}{2}\ln\beta\right)\\
&= \frac{3}{2}N \cdot \frac{1}{\beta}\\
&= \frac{3}{2} N k_{B}T
\end{align*}$$
e é este o valor que já conheciamos em física térmica.

**Energia Livre**
$$\begin{align*}
F&= \frac{-1}{\beta}\ln Z\\
&= -k_{B}T (N\ln V - \ln N! - N\ln \lambda_{T}^{3})\\
&\approx -k_{B}T(N\ln V - N\ln N + N - N\ln\lambda_{T}^{3})\\
&= -k_{B}TN(\ln V - \ln N + \ln e - \ln \lambda_{T}^{3})\\
&= -k_{B}TN \left(\ln \frac{Ve}{N} - \ln \lambda_{T}^{3}\right)
\end{align*}$$
e temos o diferencial:
$$dF(T,N,V)= \left(\frac{\partial F}{\partial T}\right)_{N,V}dT + \left(\frac{\partial F}{\partial N}\right)_{V,T}dN+ \left(\frac{\partial F}{\partial V}\right)_{T,N}dV$$

**Entropia**
$$\begin{align*}
S &= - \frac{\partial F}{\partial T}\\
&= - \frac{\partial}{\partial T} \left[-k_{B}TN \left(\ln \frac{Ve}{N} - \ln \lambda_{T}^{3}\right)\right]\\
&= k_{B}N \left(\ln \frac{Ve}{N} - \ln \lambda_{T}^{3}\right) - 3k_{B}TN \frac{\partial}{\partial T}\ln \left(\frac{h}{\sqrt{2\pi mk_{B}T}}\right) \\
&= k_{B}N \left(\ln \frac{Ve}{N} - \ln \lambda_{T}^{3}\right) - 3k_{B}TN \frac{\partial}{\partial T}\ln \left(\frac{1}{\sqrt{T}}\right)\\
&= k_{B}N \left(\ln \frac{Ve}{N} - \ln \lambda_{T}^{3}\right) + \frac{3}{2} k_{B}N \\
&= - \frac{F}{T} + \frac{\langle E\rangle}{T}
\end{align*}$$
e novamente obtemos $E=F+TS$

**Pressão**
- Ainda não tínhamos referido até aqui, mas a pressão e o volume são pares conjugados. Por outras palavras:
$$p = - \frac{\partial F}{\partial V}= k_{B}NT \frac{\partial}{\partial V}\ln V= \frac{k_{B}NT}{V}$$
de onde resulta a lei dos gases ideiais:
$$pV = Nk_{B}T$$

**Potêncial Químico**
- Fazendo a última derivada da energia livre temos:
$$\begin{align*}
\mu&= \frac{\partial F}{\partial N}\\
&= -k_{B}T \frac{\partial}{\partial N} N \left(\ln \frac{Ve}{N} - \ln \lambda_{T}^{3}\right)\\
&= -k_{B}T \left[ \left(\ln \frac{Ve}{N} - \ln \lambda_{T}^{3}\right) + N\frac{\partial}{\partial N} \ln \left(\frac{1}{N}\right) \right]\\
&= \frac{F}{N} + k_{B}T
\end{align*}$$

## 6.1 - Gás ideal fechado numa caixa
- Poderíamos modelar este problema na forma:
$$V(x_{i})=\lim\limits_{V\to+\infty} V (\Theta(x-x_{R}) + \Theta(x_{L}-x))$$