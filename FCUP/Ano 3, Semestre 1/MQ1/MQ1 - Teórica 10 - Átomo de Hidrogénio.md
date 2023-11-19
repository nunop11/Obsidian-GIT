**Cenas da Aula 9**
- Partindo da ESIT:
$$\left(\frac{-\hbar^{2}}{2m}  \nabla^{2}+V\right)\psi=E \psi$$
para um potencial central em coordenadas esféricas $V=V(r)$ obtivemos:
$$\psi= \sum\limits_{\alpha,\ell,m}C_{\alpha,\ell,m} ~\psi_{\alpha,\ell,m}(r, \theta,\phi)=\sum\limits_{\alpha,\ell,m}C_{\alpha,\ell,m} ~ R_{\alpha,\ell}(r)Y_{\ell}^{m}(\theta,\phi)$$
- Vimos ainda que $$\begin{align*}
\hat{L^{2}}Y_{\ell}^{m} &= \hbar^{2}\ell(\ell+1)Y_{\ell}^{m} \\
\hat{L_{z}}Y_{\ell}^{m} &= \hbar \underbrace{m}_{\neq~massa} Y_{\ell}^{m} \quad \quad;\quad m=-\ell,-\ell+1 ,\dots,\ell-1 ,\ell
\end{align*}$$
ou seja, os harmónicos esféricos $Y_{\ell}^{m}$ são funções próprias dos operadores $\hat{L^{2}}, \hat{L_{z}}$

**Cenas da Aula 10**
- Veremos 2 exemplos.

## Poço esférico infinito
- O potencial é definido por:
$$V(r)=\begin{cases}
\infty & ; & r>a \\
0 & ; & r\le a
\end{cases}$$
ou seja, as partículas ficam presas dentro de uma esfera de raio $r$ centrada na origem.
- Vemos ainda que isto é um caso de Potencial central.

- Fora da esfera temos $$r>a~~~~\to~~~~ \psi=0$$
- Dentro do poço apliquemos a ESIT:
$$\begin{align*}
\left(\frac{-\hbar^{2}}{2m}\nabla^{2}+{V}\right)\psi=E \psi
\end{align*}$$
- Tal como na aula anterior, fazemos a separação de variáveis: $\psi(r,\theta,\phi)=R(r)Y(\theta,\phi)$. Depois dividimos por $R \frac{Y}{r^{2}}$  e obtemos:
$$\frac{1}{R} \left[\frac{d}{dr} \left(r^{2} \frac{dR}{dr} \right)- \frac{2mr^{2}R}{\hbar^{2}} \left(V(r)-E \right)\right]= \frac{-1}{Y} \left[\frac{1}{\sin\theta} \frac{\partial}{\partial\theta}\left(\sin\theta \frac{\partial Y}{\partial\theta}\right) + \frac{1}{\sin^{2}\theta} \frac{\partial^{2}Y}{\partial\phi^{2}} \right]= \ell(\ell+1)$$
- Estudemos apenas a equação radial. Podemos reorganizá-la da forma:
$$\frac{d}{dr} \left(r^{2} \frac{dR}{dr} \right)- \frac{2mr^{2}R}{\hbar^{2}} \left(V(r)-E \right)= \ell(\ell+1)R$$
- Por fim, se fizermos a substituição $u(r)=rR(r)$ e reorganizarmos obtemos:
$$\frac{-\hbar^{2}}{2m} \frac{d^{2}u}{dr^{2}} + \left[ \underbrace{V(r) + \frac{\hbar^{2}}{2m} \frac{\ell(\ell+1)}{r^{2}}}_{V_{eff}} \right]u=Eu$$
- Ora, apliquemos ao exemplo em estudo. Temos $V(r)=0$. Ficamos com:
$$\begin{align*}
\frac{-\hbar^{2}}{2m} \frac{d^{2}u}{dr^{2}} + \frac{\hbar^{2}}{2m} \frac{\ell(\ell+1)}{r^{2}}u&= Eu\\
\frac{d^{2}u}{dr^{2}}+ \frac{\ell(\ell+1)}{r^{2}}u&= \frac{2mE}{\hbar^{2}}u\\
\frac{d^{2}u}{dr^{2}}&= \left( \frac{\ell(\ell+1)}{r^{2}}-k^{2} \right)u ~~~~;~~~~ k=\sqrt{\frac{2mE}{\hbar}}
\end{align*}$$

### $\ell=0$
Ficamos com:
$$\frac{d^{2}u}{dr^{2}}=-k^{2}u$$
que nos dá a solução trivial:
$$u(r)=A\sin(kr)+B\cos(kr)$$

- Ora, temos que $R(r)=\frac{1}{r}u(r)$

**Normalização**
- Façamos o limite $r\to0$:
$$\lim\limits_{r\to0}R(r)=\lim\limits_{r\to0}\left[\frac{A\sin(kr)+B\cos(kr)}{r}\right]=A \lim\limits_{r\to0} \frac{\sin(kr)}{r}+ B \lim\limits_{r\to0} \frac{\cos(kr)}{r}$$
- Ora, temos o limite $\lim\limits_{r\to0} \frac{\cos(kr)}{r}=\infty$. Isto não pode acontecer, porque senão temos que $R(r)$ e consequentemente $\psi(r, \theta, \phi)$ explodem junto da origem AKA a função de onda não é normalizável. Assim é necessário que $B=0$.
- Já o outro limite é $\lim\limits_{r\to0}\frac{\sin(kr)}{r}=k$. Isto não é problemático. A função de onda pode ser normalizável.
- Ficamos com $$u(r)=A\sin(kr)$$


**Condição de Fronteira**
- Temos que $u(r=a)=0$:
$$A\sin(ka)=0\to ka=n\pi \to k_{n}=\frac{n\pi}{a}~~,~~n\in\mathbb{N}$$
- De onde obtemos a quantificação da energia:
$$E_{n}=\frac{\hbar^{2}k^{2}}{2m}=\frac{\hbar^{2}n^{2}\pi^{2}}{2ma^{2}}~~,~~n\in\mathbb{N}$$

**Solução**
- Obtemos $$\psi_{n,0,0}(r,\theta,\phi)= A \frac{\sin(kr)}{r} Y_{0}^{0}(\theta,\phi)$$
- Por normalização obtemos $A=\sqrt{\frac{2}{a}}$ e sabemos que $Y_{0}^{0}=\frac{1}{\sqrt{4\pi}}$.
- Para $\ell=0,m=0$ temos:
$$\psi_{n,0,0}(r,\theta,\phi)= \sqrt{\frac{2}{4\pi a}} \frac{\sin(kr)}{r}$$

### Qualquer $\ell$
- De uma forma geral, para qualquer $\ell$ para qualquer potencial, a função $u(r)$ pode ser escrita como uma combinação linear da função de Bessel e de Newmann:
$$u(r)=Ar \mathcal{J}_{\ell}(kr)+ B r n_{\ell}(kr)$$
em que as funções de **Bessel** e **Newmann** são:
$$\begin{align*}
\mathcal{J}_{\ell}(r) &= (-x)^{\ell} \left( \frac{1}{x} \frac{d}{dx} \right)^{\ell} \frac{\sin x}{x}\\
n_{\ell}(r) &= (-x)^{\ell} \left( \frac{1}{x} \frac{d}{dx} \right)^{\ell} \frac{\cos x}{x} 
\end{align*}$$
por exemplo:
$$\begin{align*}
\mathcal{J}_{0}(x)&= \frac{\sin x}{x} &; \quad \quad \quad n_{0}(x)&= \frac{\cos x}{x}\\
\mathcal{J}_{1}(x)&= \frac{\sin x}{x^{2}}- \frac{\cos x}{x} &;\quad \quad \quad  n_{0}(x)&= \frac{\cos x}{x^{2}}- \frac{\sin  x}{x}\\
\end{align*}$$
- Voltemos ao caso específico do **poço infinito esférico**. Vemos logo que se $r\to0$, a função de Newmann explode (temos sempre $x=r$ no denominador) e a função de onda não seria normalizável. Assim, é necessário que $B=0$ e temos:
$$u(r)=A r\mathcal{J}_{\ell}(kr)$$
- Ao aplicar a condição de fronteira temos então:
$$u(a)=0~~\to~~ \mathcal{J}_{\ell}(ka)=0~~\to~~ ka=\beta_{n\ell} ~~\leftrightarrow~~ k=\frac{\beta_{n\ell}}{a}$$
em que $\beta_{n\ell}$ é o zero $n$ da função de Bessel de grau $\ell$.
![[funções Bessel.png]]

- De $k=\frac{\beta_{n\ell}}{a}$ obtemos $$E=\frac{\hbar^{2}}{2ma^{2}}\beta_{n\ell}$$
- Além disso:
$$\psi_{n,\ell,m}= A_{n,\ell} \mathcal{J}_{\ell} \left( \frac{\beta_{n\ell}}{a}r \right) Y_{\ell}^{m}(\theta,\phi) $$

# 2.7 - Átomo de Hidrogénio
- Num átomo temos 2 partículas com massa $m_{1},m_{2}$. O potencial no sistema apenas depende de $\vec{r}_{1}- \vec{r}_{2}$
- Assim: $$H(\vec{r}_{1}, \vec{r}_{2}, \vec{p}_{1}, \vec{p}_{2})=\frac{|\vec{p_{1}}|^{2}}{2m_{1}}+\frac{|\vec{p_{2}}|^{2}}{2m_{2}} + V(\vec{r_{1}}-\vec{r_{2}})$$
- Assim, é-nos conveniente passar para o referencial do CM. Assim podemos definir:
$$\begin{align*}
\vec{R}&= \frac{m_{1} \vec{r_{1}}+ m_{2} \vec{r_{2}}}{m_{1}+m_{2}} &\longleftarrow\quad \quad &\textsf{(Posição do CM)}\\
\vec{r}&= \vec{r_{1}}- \vec{r_{2}} &\longleftarrow\quad \quad &\textsf{(Posição relativa)}\\
M&= m_{1}+m_{2} &\longleftarrow \quad \quad &\textsf{(Massa total )}\\
\mu&= \frac{m_{1}m_{2}}{m_{1}+m_{2}} &\longleftarrow \quad\quad &\textsf{(Massa reduzida)}
\end{align*}$$

- E o hamiltoniano fica na forma:
$$H(\vec{R}, \vec{r}, \vec{P_{R}}, \vec{P})= \frac{|\vec{P_{R}}|^{2}}{2M} + \frac{|\vec{P}|^{2}}{2\mu}+V(\vec{r})$$
- Podemos ainda escrever:
$$\vec{L}_{CM}=\vec{R}\times M \frac{d \vec{R}}{dt} \quad \quad ;\quad \quad \vec{L}=\vec{r}\times \mu \frac{d \vec{r}}{dt}$$
em que podemos escrever: $\vec{L}_1+\vec{L}_2=\vec{L}_{CM}+\vec{L}$ (conservação do momento angular)

### Equação de Schrödinger
- Sendo $\Psi=\Psi(\vec{R},\vec{r},t)$ a equação de Shcrödinger:
$$i\hbar \frac{\partial}{\partial t}\Psi= \hat{H}(\vec{R}, \vec{r}, \frac{\hbar}{i}\nabla_{R},\frac{\hbar}{i}\nabla)\Psi=\left( - \frac{\hbar^{2}}{2m}\Delta_{\vec{R}} - \frac{\hbar^{2}}{2m}\Delta_{\vec{r}}+V(\vec{r}) \right)\Psi$$
- Podemos fazer separação de variáveis:
$$\Psi(\vec{R},\vec{r},t)= e^{-i \frac{\mathcal{E}}{\hbar}t} ~\Phi(\vec{R},\vec{r})$$
- Sendo que a ESIT fica na forma: 
$$\left( \frac{-\hbar^{2}}{2M} \Delta_{\vec{R}}- \frac{\hbar^{2}}{2\mu}\Delta_{\vec{r}}+V(\vec{r}) \right)\Phi(\vec{R},\vec{r})=\mathcal{E} \Phi(\vec{R}, \vec{r})$$

- Fazemos novamente separação de variáveis: $$\Phi(\vec{R},\vec{r})=\chi(\vec{R})\psi(\vec{r})$$
- Ao substituir na ESIT:
$$\begin{align*}
-\psi\frac{\hbar^{2}}{2M} \Delta_{\vec{R}}\chi - \chi \frac{\hbar^{2}}{2\mu}\Delta_{\vec{r}}\psi + V \chi \psi &=  \mathcal{E}\chi \psi\\
-\frac{1}{\chi}\frac{\hbar^{2}}{2M} \Delta_{\vec{R}}\chi(\vec{R})- \frac{1}{\psi}\frac{\hbar^{2}}{2\mu}\Delta_{\vec{r}}\psi(\vec{r})+V(\vec{r)}&= \mathcal{E}(\vec{R},\vec{r})
\end{align*}$$
- Podemos definir então $\mathcal{E}(\vec{R},\vec{r})=E_{CM}+E ~~~~(=E_{CM}(\vec{R})+E(\vec{r}))$
- E ficamos com:
$$\begin{align*}
-\frac{1}{\chi} \frac{\hbar^{2}}{2M} \Delta_{\vec{R}}\chi(\vec{R})&= E_{CM}\\
-\frac{1}{\psi} \frac{\hbar^{2}}{2\mu} \Delta_{\vec{r}}\psi(\vec{r}) +V(\vec{r})&= E
\end{align*}$$
que podemos reorganizar na forma:
$$\begin{cases}
-\frac{\hbar^{2}}{2M} \Delta_{\vec{R}} \chi(\vec{R})=E_{CM}\chi(\vec{R})\\
\left( - \frac{\hbar^{2}}{2\mu}\Delta_{\vec{r}} + V(\vec{r})\right)\psi(\vec{r})= E \psi(\vec{r})
\end{cases}$$
- Ora, a primeira equação depende de $\vec{R}$, ou seja, descreve o **centro de massa**, que se comporta como uma partícula livre. Isto não é suuuuuper relevante.
- A segunda equação descreve portanto o **eletrão** sendo a parte mais importante de toda esta dedução.

**ALIÁS**
- Podiamos ter partido do início a considerar que $m_{1}\gg m_{2}$, em que $m_{1}=m_{p^{+}}~~,~~m_{2}=m_{e^{-}}$. Assim: $$\mu= \frac{m_{1}m_{2}}{m_{1}+m_{2}}\simeq m_{2}=m_{e^{-}}$$
pelo que o protão está na origem sem se mover e o eletrão gira à sua volta.

### ESIT para o Eletrão
- Pegando na segunda equação do sistema acima:
$$\left( - \frac{\hbar^{2}}{2\mu}\Delta + V(\vec{r})\right)\psi(\vec{r})= E \psi(\vec{r})$$
- Consideremos o sistema em coordenadas esféricas: $\psi(\vec{r})=\psi(r,\theta,\phi)$. Além disso, consideremos que o potencial no átomo de hidrogénio é o *Potencial Coloumbiano*: $V(\vec{r})=V(r)=- \frac{e^{2}}{4\pi\varepsilon_{0}} \frac{1}{r}$. Ficamos com:
$$\begin{align*}
\left( - \frac{\hbar^{2}}{2\mu}\Delta + V(r)\right)\psi(r, \theta,\phi)&= E \psi(r,\theta,\phi)\\
\left( - \frac{\hbar^{2}}{2\mu}\Delta - \frac{e^{2}}{4\pi\varepsilon_{0}} \frac{1}{r} \right)\psi(r, \theta,\phi)&= E \psi(r,\theta,\phi)
\end{align*}$$
- Sendo que isto não passa de um **potencial central**, temos:
$$\psi(r,\theta,\phi)= \sum\limits_{\alpha,\ell,m} C_{\alpha,\ell,m} ~R_{\alpha,\ell}(r)~Y_{\ell}^{m}(\theta,\phi)$$
- Tal como atrás, fazemos separação de variáveis. Ficamos com 2 equações que têm que ser iguais a uma constante, $\ell(\ell+1)$. Depois na equação radial fazemos: $u(r)=rR(r)$ 
$$- \frac{\hbar^{2}}{2\mu} \frac{d^{2}u}{dr^{2}} + \left[ \frac{-e^{2}}{4\pi\varepsilon_{0}} \frac{1}{r} + \frac{\hbar^{2}}{2\mu} \frac{\ell(\ell+1)}{r^{2}} \right]u=Eu$$
em que se torna conveniente definir $k=\frac{\sqrt{-2\mu E}}{\hbar}$ (sendo que teremos $E<0$. Se não metessemos o sinal "-" na raiz, teríamos $k$ puramente imaginário)

- Assim resulta:
$$\frac{1}{k^{2}} \frac{d^{2}u}{dr^{2}} = \left[ 1- \frac{\mu e^{2}}{2\pi\varepsilon_{0}\hbar^{2}k} \frac{1}{kr} + \frac{\ell(\ell+1)}{(kr)^{2}}\right]u$$
definimos então $\rho=kr$ e $\rho_{0}=\frac{\mu e^{2}}{2\pi\varepsilon_{0}\hbar^{2}k}$. Ficamos com:
$$\frac{d^{2}u}{d\rho^{2}}= \left[ 1- \frac{\rho_{0}}{\rho}+ \frac{\ell(\ell+1)}{\rho^{2}} \right]u$$

#### Regiões Assintóticas
- Vejamos os limites de $u(\rho)$:
$$\rho\to\infty~~\Longrightarrow~~ \frac{d^{2}u}{d\rho^{2}}\approx u~~\Longrightarrow~~ u(\rho)\sim A e^{-\rho}+ \cancelto{não~~normalizável}{B e^{\rho}}$$
$$\rho\to0~~\Longrightarrow ~~ \frac{d^{2}u}{d\rho^{2}}\approx \frac{\ell(\ell+1)}{\rho^{2}}u~~\Longrightarrow~~ u(\rho)\sim C e^{\ell+1}+\cancelto{não~~normalizável}{D e^{-\rho}}$$
- Tendo em conta os 2 casos acima, podemos sugerir que a solução de $u(\rho)$ será do tipo:
$$u(\rho)= \rho^{\ell+1} e^{-\rho}f(\rho)$$
(em que $f(\rho)$ deverá ser uma função que não altere as condições assintóticas que vimos acima)

e podemos calcular derivadas "à bruta":
$$\begin{align*}
\frac{du}{d\rho}&= (\ell+1)\rho^{\ell}e^{-\rho}f(\rho) + \rho^{\ell+1}(-1)e^{-\rho}f(\rho) + \rho^{\ell+1}e^{-\rho} \frac{df}{d\rho}\\
&= \rho^{\ell}e^{-\rho}\left[ (\ell+1-\rho)f + \rho \frac{df}{d\rho} \right]
\end{align*}$$
$$\begin{align*}
\frac{d^{2}u}{d\rho^{2}}&= \ell \rho^{\ell-1}e^{-\rho}\left[ (\ell+1-\rho)f + \rho \frac{df}{d\rho} \right] - \rho^{\ell}e^{-\rho} \left[ (\ell+1-\rho)f + \rho \frac{df}{d\rho} \right] + \rho^{\ell}e^{-\rho}\left[ (\ell+1-\rho) \frac{df}{d\rho} - f + \frac{df}{d\rho}+ \rho \frac{d^{2}f}{d\rho^{2}} \right]\\
&= \rho^{\ell}e^{-\rho} \left[ \frac{\ell(\ell+1-\rho)}{\rho}f + \ell \frac{df}{d\rho}- (\ell+1-\rho)f -\rho \frac{df}{d\rho} + (\ell+1-\rho) \frac{df}{d\rho} - f + \frac{df}{d\rho}+ \rho\frac{d^{2}f}{d\rho^{2}}\right]\\
&= \rho^{\ell}e^{-\rho} \left[ \left(\frac{\ell(\ell+1-\rho)}{\rho} -(\ell+1-\rho)-1 \right)f + \left(\ell-\rho+ \ell+1-\rho+1 \right) \frac{df}{d\rho} + \rho \frac{d^{2}f}{d\rho^{2}} \right]\\
&= \rho^{\ell}e^{-\rho} \left[ \left(\frac{\ell(\ell+1)}{\rho}-\ell -\ell-1+\rho-1 \right)f + 2(\ell+1-\rho) \frac{df}{d\rho} + \rho \frac{d^{2}f}{d\rho^{2}} \right]\\
&= \rho^{\ell}e^{-\rho}\left[ \left( -2\ell-2+\rho+ \frac{\ell(\ell+1)}{\rho} \right)f+ 2(\ell+1-\rho) \frac{df}{d\rho} + \rho \frac{d^{2}f}{d\rho^{2}}\right]
\end{align*}$$

- Acima tínhamos: $\frac{d^{2}u}{d\rho^{2}}= \left[ 1- \frac{\rho_{0}}{\rho}+ \frac{\ell(\ell+1)}{\rho^{2}} \right]u$. Usando o que obtivemos acima temos:
$$\begin{align*}
\rho^{\ell}e^{-\rho}\left[ \left( -2\ell-2+\rho+ \frac{\ell(\ell+1)}{\rho} \right)f+ 2(\ell+1-\rho) \frac{df}{d\rho} + \rho \frac{d^{2}f}{d\rho^{2}}\right]&= \left[1- \frac{\rho_{0}}{\rho}+ \frac{\ell(\ell+1)}{\rho^{2}} \right]\rho^{\ell+1} e^{-\rho}f(\rho)\\
\left( -2\ell-2+\rho+ \frac{\ell(\ell+1)}{\rho} \right)f+ 2(\ell+1-\rho) \frac{df}{d\rho} + \rho \frac{d^{2}f}{d\rho^{2}}&= \left[\rho- \rho_{0}+ \frac{\ell(\ell+1)}{\rho} \right] f\\
\rho \frac{d^{2}f}{d\rho^{2}}+2(\ell+1-\rho) \frac{df}{d\rho} + \left[ \rho_{0}-2(\ell+1) \right]f&= 0 
\end{align*}$$

- Vamos então sugerir uma solução para $f$:
$$f(\rho)= \underbrace{\sum\limits_{j=0} a_{j} \rho^{j}}_{(0)}$$
(ou seja, $f$ será um polinómio de $\rho$)
- Façamos as derivadas:
$$\frac{df}{d\rho}= \underbrace{\sum\limits_{j=0} j a_{j} \rho^{j-1}}_{(1)} = \underbrace{\sum\limits_{j=0} (j+1)a_{j+1} \rho^{j}}_{(2)}$$
$$\frac{d^{2}f}{d\rho^{2}}=\underbrace{\sum\limits_{j=0}j(j+1) a_{j+1} \rho^{j-1}}_{(3)}$$

- Podemos reorganizar a equação acima:
$$\rho \underbrace{\frac{d^{2}f}{d\rho^{2}}}_{(3)} +2(\ell+1) \underbrace{\frac{df}{d\rho}}_{(2)} -2\rho \underbrace{\frac{df}{d\rho}}_{(1)} + \left[ \rho_{0}-2(\ell+1) \right]\underbrace{f}_{(0)}= 0$$
em que substituimos cada termos assinalado pela definição identificada acima pelo mesmo número. Ou seja:
$$\begin{align*}
\rho \sum\limits_{j=0}j(j+1) a_{j+1} \rho^{j-1} + 2(\ell+1) \sum\limits_{j=0} (j+1)a_{j+1} \rho^{j} -2\rho \sum\limits_{j=0} j a_{j} \rho^{j-1} + [\rho_{0}-2(\ell+1)]\sum\limits_{j=0} a_{j} \rho^{j}&= 0\\\\
\bcancel{\rho} \sum\limits_{j=0}j(j+1) a_{j+1} \rho^{j} \frac{1}{\bcancel{\rho}} + 2(\ell+1) \sum\limits_{j=0} (j+1)a_{j+1} \rho^{j} -2\cancel{\rho} \sum\limits_{j=0} j a_{j} \rho^{j} \frac{1}{\cancel{\rho}} + [\rho_{0}-2(\ell+1)]\sum\limits_{j=0} a_{j} \rho^{j}&= 0\\
\sum\limits_{j=0} \rho^{j} \biggr( j(j+1)a_{j+1} + 2(\ell+1)(j+1)a_{j+1}- 2j a_{j}+ [\rho_{0}-2(\ell+1)]a_{j}\biggr)&= 0
\end{align*}$$
A única forma de esta igualdade se verificar é se o termo entre parenteses for NULO para qualquer $j$. Ou seja:
$$\begin{align*}
j(j+1)a_{j+1} + 2(\ell+1)(j+1)a_{j+1}- 2j a_{j}+ [\rho_{0}-2(\ell+1)]&= 0\\
a_{j+1}\left(j(j+1)+2(\ell+1)(j+1) \right)&= a_{j}\left( 2j-\rho_{0}+2(\ell+1) \right)\\
\end{align*}$$
$$
\boxed{a_{j+1}= \frac{2(j+\ell+1)-\rho_{0}}{(j+1)(j+2\ell+2)} a_{j}}
$$
- Obtivemos então a **relação de recorrência**
---
- Ora, dissemos acima que $f(\rho)$ é uma função que tem que manter o comportamento assintótico em $\rho\to0,\rho\to\infty$ que vimos atrás. Assim, queremos saber qual o limite da série $f$.
- Para $\rho\gg1$, o que definie o comportamento de $f$ (e consequentemente de $u(\rho)$) será $j$. Ora, se $j\gg1$ temos:
$$a_{j+1}\approx \frac{2j}{j(j+1)}a_{j}=\frac{2}{j+1}a_{j}$$
Assim, sendo $a_{0}=A$ teremos:
$$a_{j}= \frac{2^{j}}{j!}A$$(não sei muito bem de onde é que isto vem)

- Assim temos:
$$f(\rho)\sim \sum A \frac{2^{j}}{j!}\rho^{j}\sim A e^{2j}$$
Que **não** é normalizável.

- Ou seja, tem que haver um *limite de termos* da série: um $j_{max}$. Este deverá ser um termo tal que $$a_{j_{max}+1}=0$$
ora, a partir da relação de recorrência ($a_{j+1}= \frac{2(j+\ell+1)-\rho_{0}}{(j+1)(j+2\ell+2)} a_{j}$) obtemos:
$$2\underbrace{(j_{max}+\ell+1)}_{n}-\rho_{0}=0~~\to~~ \rho_{0}=2n$$
em que $n\in\mathbb{N}$ é o número quântico principal.

### Bohr
- Recordemos que, de mais atrás, temos:
$$\rho_{0}= \frac{\mu e^{2}}{2\pi\varepsilon_{0}\hbar^{2}k}\quad \quad;\quad \quad k=\sqrt{\frac{-2\mu E}{\hbar}}$$
- Ora, usando isto e $\rho=2n$ podemos escrever:
$$E=- \frac{\hbar^{2}k^{2}}{2\mu}=- \frac{\mu e^{4}}{8\pi^{2}\varepsilon_{0}\hbar^{2}\rho_{0}}= - \frac{\mu}{2\hbar^{2}} \left(\frac{e^{2}}{4\pi\varepsilon_{0}}\right)^{2} \frac{1}{n^{2}}=E_{n}~~,~~n\in\mathbb{N}$$
que é a **Energia de Bohr**. Ou seja, obtivemos a fórmula dos níveis energéticos do modelo de Bohr para o átomo de Hidrogénio usando Mecânica Quântica / Schrödinger.

- Podemos aidna escrever:
$$k_{n}= \frac{\mu e^{2}}{4\pi\varepsilon_{0}\hbar^{2}} \frac{1}{n}= \frac{1}{a} \frac{1}{n} ~~~~;~~~~ a=\frac{4\pi\varepsilon_{0}\hbar^{2}}{\mu e^{2}}\approx 0.529\cdot10^{-10}m$$
em que $a$ é o **raio de Bohr**.

### $j_{max}$
- Voltemos ao $j_{max}$. Sendo $\rho_{0}=2n$ podemos reescrever a relação de recorrência como:
$$a_{j+1}= \frac{2(j+\ell+1-n)}{(j+1)(j+2\ell+2)} a_{j}$$
em que ficamos com $$j_{max}=n- (\ell+1)$$
para cada $n, \ell\le n-1$

|       | $\ell$ | $j_{max}$ | $f_{n,\ell}(k_{n}r)=\sum a_{j}\rho^{j}$                                              |
| ----- | ------ | --------- | ------------------------------------------------------------------------------------ |
| $n=1$ | $0$    | $0$       | $a_{0}\ne0~~,~~a_{1}=0~~,~~a_{2}=0~~\dots$                                           |
| $n=2$ | $0$    | $1$       | $a_{0}\ne0~~,~~a_{1}=-a_{0}~~,~~a_{2}=0~~,~~a_{3}=0~~\dots$                          |
| $n=2$ | $1$    | $0$       | $a_{0}\ne0~~,~~a_{1}=0~~,~~a_{2}=0~~\dots$                                           |
| $n=3$ | $0$    | $2$       | $a_{0}\ne0~~,~~a_{1}=-2a_{0}~~,~~a_{2}=\frac{-1}{3}a_{1}~~,~~a_3=0~~,~~a_4=0~~\dots$ |
| $n=3$ | $1$    | $1$       | $a_{0}\ne0~~,~~a_{1}=\frac{-1}{2}a_{0}~~,~~a_{2}=0~~,~~a_3=0~~\dots$                 |
| $n=3$ | $1$    | $0$       | $a_{0}\ne0~~,~~a_{1}=0~~,~~a_{2}=0~~\dots$                                           |

