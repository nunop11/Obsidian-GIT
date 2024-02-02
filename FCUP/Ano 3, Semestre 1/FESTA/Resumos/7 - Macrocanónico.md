# 1 - Sistema Isolado em Conjunto Macrocanónico
- Consideremos um sistema total composto de um sistema $S$ acoplado a um resservatório $R$. Temos:
$$H(\vec{\mu}, N,V)=H_{S}(\vec{\mu_{S}},N_{S},V_{S}) + H_{R}(\vec{\mu_{R}},N_{R},V_{R})$$
em que $N_{S}\ll N_{R}$ e $\vec{\mu}=\vec{\mu_{S}}\otimes\vec{\mu_{R}}$. Temos ainda: $E=E_{S}+E_{R},V=V_{S}+V_{R},N=N_{S}+N_{R}$

## 1.1 - Distribuição de Probabilidade
- Neste conjunto temos:
$$\rho(\vec{\mu_{S}},N_{S})= \frac{\Omega_{R}(E-H_{S}(\vec{\mu_{S}},N_{S}), N-N_{S})}{\Omega_{S\otimes R}(E,N)}$$
apesar de agora tanto a energia como o número de partículas poder variar, esta equação e sua interpretação é idêntica à que eu fiz no canónico.

- Temos:
$$\begin{align*}
\Omega_{S\otimes R}(E,N)&= \sum\limits_{N_{S}=0}^{N}\int \delta(E-H_{S}(\vec{\mu_{S},N_{S}}) - H_{R}(\vec{\mu_{R}},N-N_{S}))~ d\vec{\mu}_{S,N_{S}} d\vec{\mu}_{R,N-N_{R}}\\
&= \sum\limits_{N_{S}=0}^{N}\int_{0}^{E} \Omega_{S}(E_{S},N_{S})\Omega_{R}(E-E_{s},N-N_{S})dE
\end{align*}$$
basicamente, o integral representa todos os estados possíveis em que para $N_{S}$ partículas e a equação total dá o número total de combinações para qualquer número de partículas em $S$, $N_{S}$.

- Usando $S=-k_{B}\int \rho\ln \rho ~d\mu$ ficamos com:
$$\rho(\vec{\mu_{S}},N_{S})\propto \exp\left(\frac{S_{R}(E-E_{S},N-N_{S})}{k_{B}}\right)$$
e podemos expandir em Taylor a exponencial ($f(x+a)=f(x) + \frac{df}{dx}(x)a +\dots$, em que $x=(E,N),a=(E_{S},N_{S})$):
$$\rho(\vec{\mu_{S}},N_{S})\approx \exp\left(\frac{S_{R}(E,N)}{k_{B}} - \frac{1}{k_{B}} \frac{\partial S_{R}}{\partial E_{R}}(E) \cdot E_{S} - \frac{1}{k_{B}} \frac{\partial S_{R}}{\partial N_{R}}(N)\cdot N_{S}\right)$$
temos $$\frac{\partial S}{\partial E_{R}}(E)=\frac{1}{T} \to \frac{1}{k_{B}}\frac{\partial S_{R}}{\partial E_{R}}=\beta$$ e $$\begin{align*}
\frac{\partial E_{R}}{\partial N_{R}}&= \mu \\
-\frac{\partial E_{R}}{\partial S_{R}}\frac{\partial S_{R}}{\partial N_{R}}&= \mu \\
-T\frac{\partial S_{R}}{\partial N_{R}}&= \mu \\
\frac{-1}{k_{B}\beta}\frac{\partial S_{R}}{\partial N_{R}}&= \mu \\
\frac{1}{k_{B}}\frac{\partial S_{R}}{\partial N_{R}}&= -\beta \mu
\end{align*}$$
(só não percebi bem porquê que aparece o sinal negativo ao fazer chain rule na 2ª linha)

e a equação acima fica:
$$\rho(\vec{\mu_{S}},N_{S})\approx \exp\left(\frac{S_{R}(E,N)}{k_{B}} - \beta E_{S} + \beta\mu N_{S}\right)$$

## 1.2 - Função partição da Grande Canónica
- Define-se:
$$\begin{align*}
\mathcal{Z}_{G}(T,\mu,\vec{X})&= \sum\limits_{N_{S}=0}^{N}\int \exp(-\beta H_{S}+\beta \mu N_{S})d\mu_{S,N_{S}}\\
&= \sum\limits_{N_{S}=0}^{N}\exp(\beta \mu N_{S})\int \exp(-\beta H_{S})d\mu_{S,N_{S}}\\
&= \sum\limits_{N_{S}=0}^{N}\exp(\beta \mu N_{S})Z(\beta, N_{S},V)\\
\end{align*}$$
e temos portanto a distribuição de probabilidade:
$$\rho(\vec{\mu_{S}},N_{S})=\frac{\exp(-\beta H_{S}+\beta\mu  N_{S})}{\mathcal{Z}_{G}}$$

## 1.3 - Distribuição de probabilidade de um número de partículas
- Temos simplesmente:
$$p(N_{S})=\frac{\exp(\beta\mu  N_{S})Z(\beta,N_{S},V)}{\mathcal{Z}_{G}(\beta,\mu,V)}$$
em que, por comparação com a equação da função partição, vemos que este é o caso em que mais diretamente usamos "Probabilidade = Casos favoráveis / Casos possíveis"

**Número médio de partículas**
$$\begin{align*}
\langle N_{S}\rangle&= \sum\limits_{N_{S}=0}^{N} p(N_{S})N_{S}\\
&= \frac{\sum_{N_{S}=0}^{N}N_{S}\exp(\beta\mu  N_{S})Z(\beta,N_{S},V)}{\mathcal{Z}_{G}(\beta,\mu,V)}\\
&= \frac{1}{\beta} \frac{\sum_{N_{S}=0}^{N}N_{S} \frac{\partial}{\partial\mu}\exp(\beta\mu  N_{S})Z(\beta,N_{S},V)}{\mathcal{Z}_{G}(\beta,\mu,V)}\\
&= \frac{1}{\beta}\frac{\frac{\partial}{\partial\mu} \mathcal{Z}_{G}}{\mathcal{Z}_{G}}\\
&= \frac{1}{\beta} \frac{\partial}{\partial\mu}\ln\mathcal{Z}_{G}\\
\end{align*}$$

**Variância do Número de Partículas**
$$\begin{align*}
\langle N_{S}^{2}\rangle&= \sum\limits_{N_{S}=0}^{N} p(N_{S})N_{S}^{2}\\
&= \frac{1}{\beta^{2}}\frac{\sum_{N_{S}=0}^{N}\frac{\partial^{2}}{\partial\mu^{2}} \exp(\beta\mu N_{S})Z(\beta,N_{S},V)}{\mathcal{Z}_{G}}\\
&= \frac{1}{\beta^{2}} \frac{1}{\mathcal{Z}_{G}}\frac{\partial^{2}}{\partial\mu^{2}} \mathcal{Z}_{G}
\end{align*}$$
e obtemos a variância:
$$\begin{align*}
\langle N_{S}^{2}\rangle-\langle N\rangle^{2}&=  \frac{1}{\beta^{2}}\frac{1}{\mathcal{Z}_{G}}\frac{\partial^{2}}{\partial\mu^{2}} \mathcal{Z}_{G} - \left(\frac{1}{\beta} \frac{\partial}{\partial\mu}\ln\mathcal{Z}_{G}\right)^{2}\\
&= \frac{1}{\beta^{2}}\left(\frac{1}{\mathcal{Z}_{G}}\frac{\partial^{2}}{\partial\mu^{2}} \mathcal{Z}_{G} - \left(\frac{\partial}{\partial\mu}\ln\mathcal{Z}_{G}\right)^{2}\right)\\
&= \frac{1}{\beta^{2}}\frac{\partial^{2}}{\partial\mu^{2}}\ln \mathcal{Z}_{G}\\
&= \frac{1}{\beta}\frac{\partial}{\partial\mu}\langle N_{S}\rangle
\end{align*}$$
(em que:$\frac{\partial^2}{\partial\mu^2}\ln\mathcal Z_G = \frac{\partial}{\partial\mu}\frac{\frac{d\mathcal Z_G}{\partial\mu}}{\mathcal Z_G} = \frac1{\mathcal Z_G^2}\left(\frac{\partial^2\mathcal Z_G}{\partial\mu^2}\mathcal Z_G - \left(\frac{\partial\mathcal Z_G}{\partial\mu}\right)^2\right) = \frac1{\mathcal Z_G}\frac{\partial^2\mathcal Z_G}{\partial\mu^2} - \left(\frac{\partial}{\partial\mu}\ln\mathcal Z_G\right)^2$)
- De notar que teremos $\sigma\propto \sqrt{\langle N_{S}\rangle}$ pelo que oscilações são desprezadas no limite termodinâmico.

### Limite Termodinâmico
- Teremos
$$\begin{align*}
\mathcal{Z}_{G}&= \sum\limits_{N_{S}=0}^{N}\exp(\beta\mu N_{S})Z(\beta,N_{S},V)\\
&\approx e^{\beta\mu\langle N\rangle}Z(\beta, \langle N\rangle)\\
&= e^{\beta\mu\langle N\rangle + \beta F(\beta, \langle N\rangle)}
\end{align*}$$

- Passaremos a usar $N^*=\langle N\rangle$

## 1.4 - Grande Potencial
$$\mathcal{G}=E^{*}- TS(E^{*})-\mu N^{*}= - \frac{1}{\beta}\ln \mathcal{Z}_{G}$$
e temos o diferencial:
$$d\mathcal{G}(T,V,\mu)=\frac{\partial\mathcal{G}}{\partial T}dT+\frac{\partial\mathcal{G}}{\partial V}dV+\frac{\partial\mathcal{G}}{\partial \mu}d\mu$$
em que, pela conhecida lei $dE = SdT - pdV - Nd\mu$ temos:
$$\frac{\partial\mathcal{G}}{\partial T}=-S \quad;\quad \frac{\partial\mathcal{G}}{\partial V}=-p \quad;\quad \frac{\partial\mathcal{G}}{\partial\mu}=-N$$

# 2 - Gás Ideal
- Temos:
$$Z_{N} = \frac{V^{N}}{N! \cdot \lambda_{T}^{3N}} \quad \quad;\quad \quad \lambda_{T}=\frac{h}{\sqrt{2\pi m k_{B}T}}$$
e obtemos:
$$\begin{align*}
\mathcal{Z}_{G}&= \sum\limits_{N=0}^{+\infty} \exp(\beta\mu N)Z(\beta,N,V)\\
&= \sum\limits_{N=0}^{+\infty}\frac{e^{\beta\mu N}V^{N}}{N! \lambda_{T}^{3N}}=\sum\limits_{N=0}^{N}\frac{1}{N!} \left(\frac{\exp(\beta\mu)V}{\lambda_{T}^{3}}\right)^{N}\\
&= \exp\left(\frac{e^{\beta\mu}V}{\lambda_{T}^{3}}\right) 
\end{align*}$$
(em que ficamos com a série de Taylor de uma exponencial)

## 2.1 - Número médio de partículas
$$\begin{align*}
\langle N\rangle&= \sum\limits_{N=0}^{+\infty} N~p(N)\\
&= \sum\limits_{N=0}^{+\infty}N~\frac{\exp(\beta\mu N)Z(\beta,N,V)}{\mathcal{Z}_{G}(\beta,\mu,V)}\\
&= \frac{1}{\mathcal{Z}_{G}} \sum\limits_{N=0}^{+\infty}N\exp(\beta\mu N)\frac{V^{N}}{N!\lambda_{T}^{3N}}\\
&= \exp\left(-\frac{e^{\beta\mu}V}{\lambda_{T}^{3}}\right) ~V \frac{\partial}{\partial V}\sum\limits_{N=0}^{+\infty} \frac{e^{\beta\mu N}V^{N}}{N!\lambda_{T}^{3N}}\\
&= \exp\left(-\frac{e^{\beta\mu}V}{\lambda_{T}^{3}}\right) ~V \frac{\partial}{\partial V}\exp\left(\frac{e^{\beta\mu}V}{\lambda_{T}^{3}}\right)\\
&= \frac{e^{\beta\mu}V}{\lambda_{T}^{3}}
\end{align*}$$
em que novamente temos a série de Taylor de uma exponencial no último sumatório.

**Distribuição do número de partículas**
$$\begin{align*}
p(N)=\frac{\exp(\beta\mu N)Z}{\mathcal{Z}_{G}}&= \frac{e^{\beta\mu N}\frac{V^{N}}{N!\lambda_{T}^{3N}}}{\exp\left(\frac{e^{\beta\mu}V}{\lambda_{T}^{3}}\right)}\\
&= \frac{\frac{e^{\beta\mu N} V^{N}}{\lambda_{T}^{3N}}\frac1{N!}}{\exp\left(\langle N\rangle\right)}\\
&= \frac{\langle N\rangle^{N}\frac1{N!}}{\exp\left(\langle N\rangle\right)}\\
&= \frac{\langle N\rangle^{N} e^{-\langle N\rangle}}{N!}
\end{align*}$$
sendo esta uma distribuição de Poisson.

## 2.2 - Grande Potencial
$$\mathcal{G}=- \frac{1}{\beta}\ln \mathcal{Z}_{G}=- \frac{1}{\beta} \frac{V}{\lambda^{3}}e^{\mu\beta}$$
de onde obtemos:
**Pressão**
$$p=-\frac{\partial \mathcal{G}}{\partial V}=\frac{1}{\beta}\frac{1}{\lambda^{3}}e^{\mu\beta}$$
**Número de partículas do sistema total**
$$N=-\frac{\partial \mathcal{G}}{\partial \mu}=\frac{V}{\lambda^{3}}e^{\mu\beta}$$
**Entropia**
$$\begin{align*}
S &= - \frac{\partial \mathcal{G}}{\partial T}\\
&= - \frac{dT}{d\beta} \frac{\partial \mathcal{G}}{\partial \beta}\\
&= \frac{1}{k_{B}\beta^{2}} \left( \frac{-1}{\beta^{2}} \frac{V}{\lambda^{3}} e^{\mu\beta} + \frac{1}{\beta} \frac{V\mu}{\lambda^{3}}e^{\beta\mu} \right)\\
&= \frac{1}{k_{B}\beta^{3}}\frac{V\mu}{\lambda^{3}}e^{\beta\mu} - \frac{1}{k_{B}\beta^{4}}\frac{V}{\lambda^{3}}e^{\beta\mu}
\end{align*}$$
em que usamos $\beta=\frac{1}{k_{B}T} \to T = \frac{1}{k_{B}\beta}$.

**Lei dos gases ideiais**
- Como $p=\frac{1}{\beta} \frac{1}{\lambda^{3}} e^{\mu\beta} ~,~ N=\frac{V}{\lambda^{3}}e^{\mu\beta}$ obtemos:
$$\frac{p}{N}=\frac{\frac{1}{\beta} \frac{1}{\lambda^{3}} e^{\mu\beta}}{\frac{V}{\lambda^{3}}e^{\mu\beta}}=\frac{1}{\beta V}=\frac{k_{B}T}{V}$$
que bate certo com a lei dos gases ideiais.

# 3 - Resumos Ensembles
**Microcanónico**
- Temos $N,E,V$ constantes num sistema - Sistema isolado
- A análise começa por determinar $\Omega(E)$ e depois $$S(E)=k_{B}\ln\Omega(E)$$

**Canónico**
- Temos $T,N,V$ constantes - sistema em que podem haver trocas de calor
- Na análise começamos por determinar a função partição $Z$ e daí obtemos a energia livre de Helmholtz: $$F=-k_{B}T \ln Z$$

**Macrocanónico**
- Temos $T,\mu,V$ constantes -  pode haver troca de calor e matéria
- Começamos por determinar $\mathcal{Z}_{G}$ e daí a energia livre de Gibbs: $$G=-k_{B}T\ln \mathcal{Z}_{G}$$