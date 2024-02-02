# Potencial Central
- Potencial central consiste num potencial que apenas depende da distância à fonte. Ou seja: $V(\vec{r})=V(r)$. Consideremos coordenadas esféricas com a fonte de potencial na origem.
- Vejamos como resolver a ESIT:
$$\left( \frac{-\hbar^{2}}{2m} \Delta + V(r)\right) \psi(x,y,z) =E \psi(x,y,z) \quad \quad;\quad \quad \Delta= \frac{\partial}{\partial x^{2}}+\frac{\partial}{\partial y^{2}}+\frac{\partial}{\partial z^{2}}$$
ora, em coordenadas esféricas temos:
$$\left( \frac{-\hbar^{2}}{2m} \Delta + V(r)\right) \psi(r,\theta,\phi) =E \psi(r,\theta,\phi)$$
em que $$\Delta = \frac{1}{r^{2}} \frac{\partial}{\partial r} \left(r^{2} \frac{\partial}{\partial r}\right)+ \frac{1}{r^{2}\sin\theta} \frac{\partial}{\partial \theta}\left( \sin\theta \frac{\partial}{\partial \theta} \right) + \frac{1}{r^{2}\sin^{2}\theta} \frac{\partial^{2}}{\partial\phi^{2}}$$
- Façamos separação de variáveis:
$$\psi(r,\theta,\phi)=R(r) Y(\theta,\phi)$$
e temos:
$$\begin{align*}
\frac{-\hbar^{2}}{2m} \left[\frac{Y}{r^{2}} \frac{d}{dr}\left(r^{2} \frac{dR}{dr}\right) + \frac{R}{r^{2}\sin\theta} \frac{\partial}{\partial\theta}\left(\sin\theta \frac{\partial Y}{\partial\theta}\right) + \frac{R}{r^{2}\sin^{2}\theta} \frac{\partial^{2}Y}{\partial\phi^{2}} \right]+VRY &=  ERY\\
\frac{Y}{r^{2}} \frac{d}{dr}\left(r^{2} \frac{dR}{dr}\right) + \frac{R}{r^{2}\sin\theta} \frac{\partial}{\partial\theta}\left(\sin\theta \frac{\partial Y}{\partial\theta}\right) + \frac{R}{r^{2}\sin^{2}\theta} \frac{\partial^{2}Y}{\partial\phi^{2}} &=  \frac{-2m}{\hbar^{2}}RY(E-V)\\
\end{align*}$$
que, ao dividir por $R \frac{Y}{r^{2}}$, dá:
$$\begin{align*}
\frac{1}{R} \frac{d}{dr}\left(r^{2} \frac{dR}{dr}\right) + \frac{1}{Y\sin\theta} \frac{\partial}{\partial\theta}\left(\sin\theta \frac{\partial Y}{\partial\theta}\right) + \frac{1}{Y\sin^{2}\theta} \frac{\partial^{2}Y}{\partial\phi^{2}} &=  \frac{-2m r^{2}}{\hbar^{2}}(E-V)\\
\frac{1}{R} \left[\frac{d}{dr} \left(r^{2} \frac{dR}{dr} \right)- \frac{2mr^{2}R}{\hbar^{2}} \left(V(r)-E \right)\right]= \frac{-1}{Y} \left[\frac{1}{\sin\theta} \frac{\partial}{\partial\theta}\left(\sin\theta \frac{\partial Y}{\partial\theta}\right) + \frac{1}{\sin^{2}\theta} \frac{\partial^{2}Y}{\partial\phi^{2}} \right]&= \ell(\ell+1)
\end{align*}$$

em que o lado esquerdo apenas depende de $r$ (**equação radial**) e o lado direto depende de $\theta,\phi$ (**equação angular**). Por esta razão, a única forma de a igualdade se verificar é se os 2 lados forem iguais a uma constante, a que chamaremos $\ell(\ell+1)$.

## Equação Angular
$$\sin\theta \frac{\partial}{\partial\theta}\left(\sin\theta \frac{\partial Y}{\partial\theta}\right)+ \frac{\partial^{2}Y}{\partial\phi^{2}}= - \ell(\ell+1)\sin^{2}\theta Y$$
- Ora, vamos fazer uma segunda separação de variáveis: $$Y(\theta,\phi)=f(\theta)g(\phi)$$
e ficamos com:
$$g\sin\theta \frac{\partial}{\partial\theta}\left(\sin\theta \frac{df}{d\theta}\right)+f \frac{d^{2}g}{d\phi^{2}}=- \ell(\ell+1)\sin^{2}\theta fg$$
que podemos dividir por $fg$ e dá:
$$\frac{1}{f} \sin\theta \frac{\partial}{\partial \theta} \left(\sin\theta \frac{df}{d\theta} \right)+ \frac{1}{g} \frac{d^{2}g}{d\phi^{2}}=- \ell(\ell+1)\sin^{2}\theta$$
e podemos reescerver como:
$$\frac{1}{f}\left( \sin\theta \frac{\partial}{\partial \theta}\left( \sin\theta \frac{df}{d\theta} \right) + \ell(\ell+1)\sin\theta f \right)=- \frac{1}{g} \frac{d^{2}g}{d\phi^{2}}=m^{2}$$
em que, novamente, temos que o lado esquerdo apenas depende de $\theta$ e o direito apenas depende de $\phi$. Assim, ambos são constantes e iguais a $m^{2}$.

### Solução para $g(\phi)$
- Temos:
$$\frac{-1}{g} \frac{d^{2}g}{d\phi^{2}}=m^{2} ~~\to~~ \frac{d^{2}g}{d\phi^{2}}=-m^{2}g~~\longrightarrow ~~ g(\phi)=e^{im\phi}$$
- No entanto, recordemos que estamos em coordenadas esféricas e então $g(\phi)$ é uma função azimutal e tem que ser contínua e periódica, tendo que se cumprir:
$$\begin{align*}
g(\phi+2\pi)&= g(\phi)\\
e^{im(\phi+2\pi)}&= e^{im\phi}\\
e^{im\phi}e^{im2\pi}&= e^{im\phi}\\
e^{im2\pi}&= 1\\
\end{align*}$$
logo temos que $$\boxed{m\in\mathbb{Z}}$$

### Solução para $f(\theta)$
- Temos:
$$\begin{align*}
\frac{1}{f}\left( \sin\theta \frac{\partial}{\partial \theta}\left( \sin\theta \frac{df}{d\theta} \right) + \ell(\ell+1)\sin\theta f \right)&= m^{2}\\
\sin\theta \frac{\partial}{\partial \theta}\left( \sin\theta \frac{df}{d\theta} \right) + \left(\ell(\ell+1)\sin\theta - m^{2}\right) f&= 0
\end{align*}$$

em que fazemos uma substituição: $x=\cos\theta ~~;~~ \frac{d}{d\theta}=\frac{dx}{d\theta} \frac{d}{dx}=-\sin\theta \frac{d}{dx}= \sqrt{1-x^{2}} \frac{d}{dx}$. Ficamos então com:
$$\begin{align*}
(1-x^{2}) \frac{d}{dx}\left((1-x^{2}) \frac{df}{dx} \right)+ \left( \ell(\ell+1)(1-x^{2})-m^{2} \right)f &= 0\\
(1-x^{2})f'' - 2x f'+ \left( \ell(\ell+1)- \frac{m^{2}}{1-x^{2}} \right)f&= 0
\end{align*}$$

**Polinómios de Legendre**
$$\begin{align*}
\mathcal{P}_{\ell}^{m}(x)&= (-1)^{m} (1-x^{2})^{\frac{m}{2}} \frac{d^{m}}{dx^{m}} \mathcal{P}_{\ell}(x)\\
\mathcal{P}_{\ell}^{-m}(x)&= (-1)^{m} \frac{(\ell-m)!}{(\ell+m)!} \mathcal{P}_{\ell}^{m}(x)
\end{align*}$$
- Em que $\mathcal{P}_{\ell}$ é o polinómio de Legendre:
$$\mathcal{P}_{\ell}(x)= \frac{1}{2^{\ell}\ell!} \frac{d^{\ell}}{dx^{\ell}}(x^{2}-1)^{\ell} $$
 em que $\mathcal{P}_{\ell}$ nos dá um polinómio de grau $\ell$.
 - Assim, como na equação de $\mathcal{P}_{\ell}^{m}$ temos a derivada de ordem $m$ de $\mathcal{P}_{\ell}$ resulta que:
$$\begin{cases}
\mathcal{P}_{\ell}^{m}&= 0 &;\quad &m>\ell\\
\mathcal{P}_{\ell}^{m}&\neq 0 &;\quad &m\le\ell
\end{cases}$$

---
### Harmónicos Esféricos
Ou seja, as soluções de $f,g$ que obtivemos acima só fazem sentido (não são nulas) se:
$$\ell \in \mathbb{N}_{0} \quad, \quad m\in \mathbb{Z} \quad \quad;\quad \quad |m|\le \ell$$
e temos então os **harmónicos esféricos** AKA $Y_{\ell}^{m}$:
$$Y_{\ell}^{m}(\theta,\phi)= \sqrt{ \frac{2 \ell+1}{4\pi} \frac{(\ell-m)!}{(\ell+m)!}} \mathcal{P}_{\ell}^{m}(\cos \theta) e^{im\phi}$$
sendo que esta é uma **base completa** de soluções. Ou seja, a parte angular de solução da ESIT para um potencial central pode ser descrita como uma combinação linear destas funções. Assim, a solução geral da componente angular será:
$$\omega(\theta, \phi)=\sum\limits_{\ell=0}^{\infty} \sum\limits_{m=-\ell}^{+\ell} c_{\ell,m} Y_{\ell}^{m}(\theta, \phi)$$

- Vamos então ver a *condição de normalização*:
$$\begin{align*}
\int |Y|^{2} &= 1\\
\int_{0}^{2\pi}\int_{0}^{\pi}\underbrace{\sin\theta ~d\theta d\phi}_{=~d \Omega} ~(Y)^{*}(Y)&= 1\\
\delta_{m,m'} \delta_{\ell,\ell'}&= 1
\end{align*}$$

#### EXEMPLOS
$$Y_{0}^{0} = \frac{1}{\sqrt{4\pi}}$$
$$Y_{1}^{-1}= \sqrt{\frac{3}{8\pi}} \sin\theta e^{-i\phi}$$
$$Y_{1}^{0}= \sqrt{\frac{3}{4\pi}} \cos\theta$$

![[harmonicos esféricos.png]]

## Equação Radial
- Se considerarmos $R_{\alpha,\ell}(r)$ em que $\alpha$ é um parâmetro que pode surgir ao resolver a equação radial (e depende do potencial), temos:
$$\psi(r,\theta, \phi)=\sum\limits_{\alpha,\ell,m} c_{\alpha,\ell,m} R_{\alpha,\ell}(r) Y_{\ell}^{m}(\theta, \phi)$$

- Voltando atrás, a equação radial é dada por:
$$\begin{align*}
\frac{1}{R} \left[\frac{d}{dr} \left(r^{2} \frac{dR}{dr} \right)- \frac{2mr^{2}R}{\hbar^{2}} \left(V(r)-E \right)\right]&= \ell(\ell+1)\\
\frac{d}{dr} \left(r^{2} \frac{dR}{dr} \right)- \frac{2mr^{2}R}{\hbar^{2}} \left(V(r)-E \right)&= \ell(\ell+1)R
\end{align*}$$
Ora, o 1º termo irá dar: $\frac{d}{dr}\left(r^{2} \frac{dR}{dr}\right)=2rR' + r^{2}R''$. Queremos então fazer uma substituição de forma a eliminar o termo da derivada ($2rR'$). Assim:
$$u(r)=rR(r)\to R=\frac{u}{r}$$
$$\frac{dR}{dr}=\frac{-u}{r^{2}}+ \frac{1}{r}u'$$
$$\frac{d}{dr}\left(r^{2} \frac{dR}{dr}\right)= \frac{d}{dr}\left(r^{2}\left(\frac{-u}{r^{2}}+\frac{1}{r}u'\right)\right)= \frac{d}{dr}\left( -u + ru'\right) =- \frac{du}{dr}+ \frac{du}{dr} + r u'' = ru''=r \frac{d^{2}u}{dr^{2}}$$
- Substituindo na Equação radial acima:
$$r \frac{d^{2}u}{dr^{2}} - \frac{2mr^{2}}{\hbar^{2}} \frac{u}{r} (V-E)= \ell(\ell+1)\frac{u}{r}$$
multiplicando por $\frac{\hbar^{2}}{2m}$:
$$\frac{\hbar^{2}}{2m} r \frac{d^{2}u}{dr^{2}} - ru(V-E)= \frac{\hbar^{2}}{2m}\ell(\ell+1) \frac{u}{r} $$
dividir por $-r$:
$$\frac{-\hbar^{2}}{2m} \frac{d^{2}u}{dr^{2}}+ uV - Eu=\frac{-\hbar^{2}}{2m} \ell(\ell+1) \frac{u}{r^{2}}$$
e ao reorganizar obtemmos:
$$\frac{-\hbar^{2}}{2m} \frac{d^{2}u}{dr^{2}} + \left[ \underbrace{V(r) + \frac{\hbar^{2}}{2m} \frac{\ell(\ell+1)}{r^{2}}}_{V_{efetivo}=V_{eff}} \right]u=Eu$$
- Ora, vemos que a equação radial resulta na ESIT para uma função de onda $u(r)=rR(r)$, em que o potencial é $V_{eff}$.
- Esse potencial tem um termo **centrífugo**: o termo $\propto \frac{1}{r^{2}}$.
- Vemos ainda que o parâmetro $m$ (Não a massa!!) não entra nesta equação, ou seja, a energia não pode depender de $m$.

## Operador Momento Angular
- Como vimos num dos exercícios da Ficha 1, o termo centrífugo do potencial efetivo também aparece na física clássica. Aparece na forma:
$$V_{eff}=V + \frac{L^{2}}{2mr^{2}}$$
e então, ao comparar, surge a pergunta: Será que $\hbar \ell(\ell+1)=L^{2}$ ???

- Temos que $\vec{L}=\vec{r}\times \vec{p}$. Ora, temos o operador momento linear: $\hat{P}= \frac{\hbar}{i} \nabla$. Assim:
$$\hat{L}=\vec{r}\times \frac{\hbar}{i} \nabla$$
- No entanto, para relacionar este operador com a equação radial de $u(r)$ acima, temos que passar esta equação para coordenadas esféricas:
$$\vec{r}=r \hat{e}_{r}$$
$$\nabla= \hat{e}_{r} \frac{\partial}{\partial r}+ \hat{e}_{\theta} \frac{1}{r} \frac{\partial}{\partial \theta} + \hat{e}_{\phi} \frac{1}{r\sin\theta} \frac{\partial}{\partial\phi}$$
o que nos dá:
$$\begin{align*}
\hat{L}&= \vec{r}\times \nabla\\
\hat{L}&= r \hat{e}_{r} \times \left( \hat{e}_{r} \frac{\partial}{\partial r}+ \hat{e}_{\theta} \frac{1}{r} \frac{\partial}{\partial \theta} + \hat{e}_{\phi} \frac{1}{r\sin\theta} \frac{\partial}{\partial\phi} \right)\\
\hat{L}&= \frac{\hbar}{i} \left( \hat{e}_{\phi} \frac{\partial}{\partial\theta} - \hat{e}_{\theta} \frac{1}{\sin\theta} \frac{\partial}{\partial\phi} \right)
\end{align*}$$

- Ao fazer a projeção de $\hat{e}_{\phi},\hat{e}_{\theta}$ em $\hat{x},\hat{y},\hat{z}$ obtemos as componentes de $\hat{L}$ em coordenadas esféricas, nos **eixos** cartesianos:
$$\begin{align*}
\hat{L}_{x}&= \frac{\hbar}{i} \frac{\partial}{\partial\phi}\\
\hat{L}_{y}&= \frac{\hbar}{i} \left( \sin\phi \frac{\partial}{\partial\theta} + \cot\theta\cos\phi \frac{\partial}{\partial \phi} \right)\\
\hat{L}_{z}&= \frac{\hbar}{i} \left( -\cos\phi \frac{\partial}{\partial\theta} + \cot\theta\sin\phi \frac{\partial}{\partial \phi} \right)
\end{align*}$$
- No entanto, o que temos no termos centrífugo é $L^{2}$, não $L$. Assim, queremos obter $\hat{L^{2}}$:
$$\begin{align*}\\
\hat{L^{2}}&= \hat{L^{2}_{x}}+\hat{L^{2}_{y}}+\hat{L^{2}_{z}}\\
\hat{L^{2}}&= -\hbar^{2}\left[ \frac{\partial^{2}}{\partial\phi^{2}} + \left( \sin\phi \frac{\partial}{\partial\theta} + \cot\theta\cos\phi \frac{\partial}{\partial \phi} \right)\left( \sin\phi \frac{\partial}{\partial\theta} + \cot\theta\cos\phi \frac{\partial}{\partial \phi} \right) + \left( -\cos\phi \frac{\partial}{\partial\theta} + \cot\theta\sin\phi \frac{\partial}{\partial \phi} \right)\left( -\cos\phi \frac{\partial}{\partial\theta} + \cot\theta\sin\phi \frac{\partial}{\partial \phi} \right) \right]
\end{align*}$$
ora, isto é muito bonito mas não nos podemos esquecer que estamos a fazer o quadrado de *operadores*. Assim, após uma série de passos que não quis escrever obtem-se:
$$\hat{L^{2}}= -\hbar^{2} \left[ \frac{1}{\sin\theta} \frac{\partial}{\partial\theta} \left(\sin\theta \frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^{2}\theta} \frac{\partial^{2}}{\partial^{2}\phi} \right]$$
em que o que temos dentro de parêntesis retos não passa do laplaciano para uma esfera unitária. Assim podemos escrever o operador $L^{2}$ como:
$$\hat{L^{2}}= -\hbar^{2} \Delta_{\theta,\phi}$$
- Recordemos a equação angular:
$$\frac{1}{\sin\theta} \frac{\partial}{\partial\theta}\left(\sin\theta \frac{\partial Y}{\partial\theta}\right) + \frac{1}{\sin^{2}\theta} \frac{\partial^{2}Y}{\partial\phi^{2}}= -\ell(\ell+1)Y ~~ \longrightarrow ~~ \Delta_{\theta,\phi}Y=-\ell(\ell+1)Y$$
ou seja, podemos escrever:
$$\hat{L^{2}}Y= \hbar^{2} \ell(\ell+1)Y$$
- Assim verificamos que, de facto $L^2$ para os harmónicos esféricos é igual a $\hbar^{2} \ell(\ell+1)$.

- Por fim, temos ainda:
$$\hat{L}_{x}Y_{\ell}^{m}=\frac{\hbar}{i} \frac{\partial}{\partial \phi}Y_{\ell}^{m}= \frac{\hbar}{i} \frac{\partial}{\partial\phi} \left(  \sqrt{ \frac{2 \ell+1}{4\pi} \frac{(\ell-m)!}{(\ell+m)!}} \mathcal{P}_{\ell}^{m}(\cos \theta) e^{im\phi}\right) =\frac{\hbar}{i} im \sqrt{ \frac{2 \ell+1}{4\pi} \frac{(\ell-m)!}{(\ell+m)!}} \mathcal{P}_{\ell}^{m}(\cos \theta) e^{im\phi}=\hbar m Y_{\ell}^{m} $$
isto é análogo a ter $\psi=A e^{i \vec{k}\cdot \vec{r}}$ e fazer:
$$\hat{P}\psi_{\vec{k}} = \frac{\hbar}{i} \nabla \psi_{\vec{k}} = \hbar \vec{k} \psi_{\vec{k}}$$
