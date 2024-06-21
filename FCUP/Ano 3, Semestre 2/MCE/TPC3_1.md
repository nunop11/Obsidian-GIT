- Sendo $v=v_{M}(1-\frac{\rho}{\rho_{M}})$
$$\begin{align*}
\frac{\partial \rho}{\partial t} + \frac{\partial(\rho v)}{\partial x}&= 0\\
\frac{\partial \rho}{\partial t} + \frac{\partial}{\partial x}\left[v_{M}\left(\rho-\frac{\rho^{2}}{\rho_{M}}\right) \right]&= 0\\
\frac{\partial \rho}{\partial t} + v_{M}\left(1-\frac{2\rho}{\rho_{M}}\right)\frac{\partial \rho}{\partial x}&= 0\\
\end{align*}$$
em que definimos $u=(1-\frac{2\rho}{\rho_{M}})$, tendo-se:
$$\frac{\partial u}{\partial n}=\frac{-2}{\rho_{M}}\frac{\partial \rho}{\partial n}~~\to~~ \frac{\partial \rho}{\partial n}=- \frac{1}{2} \rho_{M}\frac{\partial u}{\partial n}$$
logo:
$$\frac{\partial \rho}{\partial x}=- \frac{1}{2} \rho_{M}\frac{\partial u}{\partial x}~~;~~\frac{\partial \rho}{\partial t}=- \frac{1}{2} \rho_{M}\frac{\partial u}{\partial t}$$
que ao substituir na equação dá:
$$\frac{\partial u}{\partial t} + v_{M}u \frac{\partial u}{\partial x}=0$$
e sendo $v_{M}=1$ temos:
$$u_{t}+u u_{x}=0$$
, a *equação de Burger invíscida*.

- Vamos alterar o modelo de forma a ser mais realista:
$$v\rho=v_{M}\left(\rho-\frac{\rho^{2}}{\rho_{M}}\right)-\sigma \frac{\partial \rho}{\partial x}$$
e a equação fica:
$$\begin{align*}
\frac{\partial \rho}{\partial t} + \frac{\partial(\rho v)}{\partial x}&= 0\\
\frac{\partial \rho}{\partial t} + \frac{\partial }{\partial x} \left[v_{M}\left(\rho-\frac{\rho^{2}}{\rho_{M}}\right)-\sigma \frac{\partial \rho}{\partial x}\right]&= 0\\
\frac{\partial \rho}{\partial t} + v_{M}\left[1-\frac{2\rho}{\rho_{M}}\right]\frac{\partial \rho}{\partial x} - \sigma\frac{\partial^{2} \rho}{\partial x^{2}}&= 0
\end{align*}$$
juntando às equações de $\partial_{t}\rho, \partial_{x}\rho$ temos: $$\frac{\partial^{2}u}{\partial x^{2}}=- \frac{1}{2} \frac{1}{\rho_{M}}\frac{\partial^{2} \rho}{\partial x^{2}}~~\to~~\frac{\partial^{2} \rho}{\partial x^{2}}=- \frac{1}{2} \rho_{M}\frac{\partial^{2}u}{\partial x^{2}}$$
e fica:
$$\partial_{t}u + v_{M}u\partial_{x}u = \sigma \partial_{x}^{2}u$$
- Em que, novamente, se $v_{M}=1$ temos a *equação de Burger vísicida*.

- Consideremos 2 CIs diferentes:
$$\begin{align*}
&(1)~~~~ u(x,0)=\sin(2\pi x)\\
&(2)~~~~ u(x,0)=\begin{cases}
1 & ; & 0\le x< \frac{1}{2}\\
0 & ; & \frac{1}{2}\le x\le1
\end{cases}
\end{align*}$$
- Para a CI 1 consideramos *CFs periódicas*. Na prática isto significa que $u(1,t)=u(0,t)=0$
- Para a CI 2 consideramos  $u(0,t)=1$ (de recordar para equações deste tipo apenas precisamos de 1 CF)

## 1.
- Temos a equação de advecção linear:
$$\frac{\partial u}{\partial t}= v \frac{\partial u}{\partial x}$$
- Vamos resolver isto por separação de variáveis. Consideremos $u(x,t)=X(x)T(t)$. Temos:
$$\begin{align*}
X(x)\dot{T}(t)&= v\dot{X}(x)T(t)\\
\frac{\dot{T}(t)}{T(t)}&= v \frac{\dot{X}(x)}{X(x)}
\end{align*}$$
- Ora, a única forma de esta equação ser verdade é se ambos os lados forem iguais a uma constante, a que chamaremos $\omega$: 
$$\begin{cases}
\frac{\dot{T}(t)}{T(t)}=\omega \\
\frac{\dot{X}(x)}{X(x)}=\frac{\omega}{v}
\end{cases}=\begin{cases}
\dot{T}(t) = \omega T(t) \\
\dot{X}(x) = \frac{\omega}{v}X(x)= k X(x)
\end{cases}$$
- Podemos então assumir soluções do tipo:
$$T(t) = e^{i\omega t} \quad;\quad X(x)=A\sin(kx)$$
tendo-se:
$$u(x,t)=A\sin(kx+\delta)e^{i\omega t}$$
- Apliquemos as CI e CF:
##### CI 1
- Temos a CF. Seja $\delta=0$:
$$\begin{align*}
u(1,t)&= 0\\
A\sin (k)&= 0\\
k &= 2\pi n~~,~~ n\in \mathbb{Z}
\end{align*}$$
- Temos a CI:
$$\begin{align*}
A\sin(kx)&= \sin(2\pi x)\\
A\sin(2\pi nx)&= \sin(2\pi x)\\
A&= \frac{\sin(2\pi x)}{\sin(2\pi nx)}
\end{align*}$$
e fica:
$$u_{1}(x,t)=\sin(2\pi x)e^{i\omega t}$$
- Vemos que esta solução cumpre a CF e CI do tipo 1.

##### CI 2
###### $0\le x<\frac12$
- Temos a CF:
$$\begin{align*}
u(0,t)&= -1\\
\sin\delta e^{i\omega t}&= -1\\
\sin\delta&= e^{-i\omega t}\\
\sin\delta&= \cos(\omega t)\\
\delta &= \omega t+ \frac{\pi}{2}+2\pi n\\
\end{align*}$$
- Temos a CI:
$$\begin{align*}
u(x,0)&= -1\\
A\sin(kx + \omega \cdot0 + \frac{\pi}{2})&= -1\\
A\cos(kx)&= -1\\
\end{align*}$$
- Temos então:
$$\begin{align*}
u_{1}(x,t)&= A\sin(kx + \delta)e^{i\omega t}\\
&= A\cos(kx + \omega t)e^{i\omega t}\\
&= A(\cos(kx)\cos(\omega t)-\sin(kx)\sin(\omega t))e^{i\omega t}\\
&= (A\sin(kx)\sin(\omega t)-\cos(\omega t))e^{i\omega t}
\end{align*}$$

###### $\frac{1}{2}\le x\le1$
- Temos apenas a CI:
$$\begin{align*}
u(x,0)&= 0\\
A\sin(kx+\delta)&= 0\\
\end{align*}$$
logo:
$$u_{2}(x,t)=0$$

###### Juntar divisões do domínio
- Temos a condição de continuidade:
$$\begin{align*}
u_{1}\left(\frac{1}{2},t\right)&= u_{2}\left(\frac{1}{2},t\right)\\
A\sin\frac{k}{2}\sin(\omega t) - \cos(\omega t)&= 0\\
A\sin\left(\frac{k}{2}\right)&= \tan(\omega t)\\
A&= \frac{\tan\omega t}{\sin(k/2)}
\end{align*}$$
e fica:
$$u(x,t)= [\tan(\omega t)\frac{\sin(kx)}{\sin(k/2)}\sin(\omega t) - \cos(\omega t)]e^{i\omega t}$$
- Tomando a parte real:
$$\begin{align*}
u(x,t)&= \left[\frac{\sin(kx)}{\sin\left(\frac{k}{2}\right)} \frac{\sin^{2}(\omega t)}{\cos(\omega t)}-\cos(\omega t)\right]\cos(\omega t)\\
&= \frac{\sin(kx)}{\sin\left(\frac{k}{2}\right)}\sin^{2}(\omega t)-\cos^{2}(\omega t)
\end{align*}$$

## 2.
- O método de Lax-Friedrichs (LF) consiste em:
$$\begin{align*}
\frac{u(x,t+\Delta t) -\frac{1}{2}\left(u(x+h,t)+ u(x-h,t) \right)}{\Delta t}= v \frac{u(x+h,t)-u(x-h,t)}{2 \Delta x}\\
[u(x,t+\Delta t) -\frac{1}{2}\left(u(x+h,t)+ u(x-h,t) \right)]= \frac{C}{2} (u(x+h,t)-u(x-h,t))
\end{align*}$$
- Vamos fazer análise de Von Neumann. Consideremos uma solução do tipo modo de Fourier: $u=A^{n}e^{i\omega x}$. Temos:
$$$$
- Consideremos que a amplitude da solução evolui de forma constante:
$$\frac{A(t+\Delta t)}{A(t)} = \lambda~~\to~~ A(t+\Delta t)=\lambda A(t)$$
- Substituindo na equação temos:
$$\begin{align*}
\lambda Ae^{i\omega x} - \frac{1}{2} (Ae^{i\omega(x+h)}+Ae^{i\omega(x-h)}) &= \frac{C}{2} (Ae^{i\omega(x+h)}-Ae^{i\omega(x-h)})\\
\lambda- \frac{1}{2}(e^{i\omega h}+e^{-i\omega h})&= \frac{C}{2}(e^{i\omega h} - e^{-i\omega h})\\
\lambda&= \cos(\omega h) + iC\sin(\omega h)\\
\end{align*}$$
Assim, temos o módulo:
$$|\lambda|=|C|$$
logo, para haver convergência é necessário que $|\lambda|\le1$ ou seja:
$$|C|\le1~~\to~~ |\Delta t|\le |v\Delta x|$$


## 3.
- O método *upwind* consiste em fazer a derivada temporal com aproximação de derivada à frente e a derivada espacial como derivada atrás (derivada upwind).
- Aplicando isto à equação de Burger invíscida obtemos a equação do enunciado.
- Do ponto de vista de estabilidade podemos fazer novamente análise de von Neumann:
$$\begin{align*}
\frac{u^{n+1}_i - u^{n}_i}{\Delta t} &= - u^{n}_i\Bigl( \frac{u^{n}_i - u^{n}_{i-1}}{\Delta x}\Bigr)\\
\lambda Ae^{i\omega x}-Ae^{i\omega x}&= - \frac{\Delta t}{\Delta x} A e^{i\omega x} (Ae^{i\omega x}-e^{i\omega(x-\Delta x)})\\
\lambda-1 &= - \frac{\Delta t}{\Delta x} (1-e^{-i\omega \Delta x})\\
\lambda &= 1- \frac{\Delta t}{\Delta x} (1-e^{-i\omega \Delta x})\\
\end{align*}$$
