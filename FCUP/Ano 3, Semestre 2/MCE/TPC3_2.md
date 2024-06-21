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
- Para a CI 1 consideramos *CFs periódicas*
- Para a CI 2 consideramos  $u(0,t)=1$ (de recordar para equações deste tipo apenas precisamos de 1 CF)

## 1.
- Temos a equação de advecção linear:
$$\frac{\partial u}{\partial t}+\frac{\partial(v\rho)}{\partial x}=0~~\to~~{\partial x}\frac{\partial u}{\partial t}= -v \frac{\partial u}{\partial x}$$
- Como sabemos que a solução da equação de advecção linear simplesmente consiste na onda inicial a "moder-se para o lado", podemos considerar a solução uma onda progessiva, ou seja:
$$u(x,t)=f_{0}\left(x-vt\right)$$
- Vamos então ver as 2 CFs:
##### CF tipo I
- Temos:
$$f_{0}(x)=\sin(2\pi x)$$
logo temos:
$$u(x,t)=\sin\left(2\pi \left(x-vt\right)\right)=\sin\left(2\pi x-2\pi vt\right)$$
e facilmente verificamos que esta é uma solução analítica:
$$\left.\begin{matrix}
\frac{\partial }{\partial t}\sin(2\pi x-2\pi vt)= -2\pi v\cos(2\pi x-2\pi vt)\\
\frac{\partial}{\partial x}\sin(2\pi x - 2\pi vt)= +2\pi\cos(2\pi x-2\pi vt)
\end{matrix}~\right\}\to \frac{\partial u}{\partial t}=-v \frac{\partial u}{\partial x} $$
logo:
$$u_{1}(x,t)=\sin(2\pi(x+vt))$$

##### CF tipo 2
- Temos:
$$f_{0}(x)=\begin{cases}
-1 & ; & 0\le x<\frac{1}{2} \\
0 & ; & \frac{1}{2}\le x\le1
\end{cases}$$
- Logo:
$$u(x,t)=\begin{cases}
-1 & ; & 0\le x+vt<\frac{1}{2} \\
0 & ; & \frac{1}{2}\le x+vt\le1
\end{cases}= \begin{cases}
-1 & ; & -vt\le x< \frac{1}{2}-vt \\
0 & ; & \frac{1}{2}-vt \le x\le 1-vt
\end{cases}$$
- Também verificamos que esta solução é analiticamente correta:
$$\left.\begin{matrix}
\frac{\partial }{\partial t}u(x,t)= 0\\
\frac{\partial}{\partial x}u(x,t)= 0
\end{matrix}~\right\}\to \frac{\partial u}{\partial t}=-v \frac{\partial u}{\partial x} $$
- Para garantir a CF: $u_{2}(0,t)=-1$ basta alterar a função:
$$u=\begin{cases}
-1 & ; & 0\le x< \frac{1}{2}-vt \\
0 & ; & \frac{1}{2}-vt \le x\le 1-vt
\end{cases}$$

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
\frac{u^{n+1}_i - u^{n}_i}{\Delta t} &= - vu^{n}_i\Bigl( \frac{u^{n}_i - u^{n}_{i-1}}{\Delta x}\Bigr)\\
\lambda Ae^{i\omega x}-Ae^{i\omega x}&= - v\frac{\Delta t}{\Delta x} A e^{i\omega x} (Ae^{i\omega x}-Ae^{i\omega(x-\Delta x)})\\
\lambda-1 &= - C Ae^{i\omega x}(1-e^{-i\omega \Delta x})\\
\lambda &= 1- C Ae^{i\omega x}(1-e^{-i\omega \Delta x})\\
\end{align*}$$

E podemos desenvolver:
$$\begin{align*}
Ae^{i\omega x}(1-e^{-i\omega \Delta x})&= A (e^{i\omega x}-e^{i\omega(x-\Delta x)})\\
&= A \left[ \cos(\omega x)+i\sin(\omega x) -\cos(\omega (x-\Delta x))-i\sin(\omega (x-\Delta x))\right]\\
&= A\left[ -2\sin\left(\omega\frac{x+x-\Delta x}{2}\right)\sin \left( \omega\frac{x-x+\Delta x}{2}\right) +2i\cos \left(\omega \frac{x+x-\Delta x}{2}\right)\sin\left(\omega\frac{x-x+\Delta x}{2}\right)\right]\\
&= A\left[-2\sin\left(\frac{\omega}{2}(2x-\Delta x)\right) \sin\frac{\omega\Delta x}{2} + 2i\cos\left(\frac{\omega}{2}(2x-\Delta x)\right)\sin \frac{\omega\Delta x}{2}\right]\\
&= 2A\sin\left(\frac{\omega\Delta x}{2}\right)[-\sin\left(\frac{\omega}{2}(2x-\Delta x)\right)+i\cos\left(\frac{\omega}{2}(2x-\Delta x)\right)]\\
|Ae^{i\omega x}(1-e^{-i\omega \Delta x})|&= 2A\sin\left(\frac{\omega\Delta x}{2}\right)
\end{align*}$$
- Logo:
$$\lambda=1-2A(t)C\sin\left(\frac{\omega \Delta x}{2}\right)$$

%% - Para haver estabilidade é preciso que:
$$|\lambda|\le1~~\to~~ 0\le CAe^{i\omega x}(1-e^{-i\omega \Delta x})\le2$$
$$\begin{align*}
0&\le CA\le \frac{2e^{-i\omega x}}{1-e^{-i\omega\Delta x}}\\
0&\le CA\le \frac{2e^{i\omega (\Delta x/2-x)}}{e^{i\omega \Delta x/2}-e^{-i\omega\Delta x/2}}\\
0&\le CA\le \frac{e^{i\omega (\Delta x/2-x)}}{i\sin(\omega \frac{\Delta x}{2})}\\
0&\le CA\le \frac{\cos( \omega(\frac{\Delta x}{2}-x))+i\sin( \omega(\frac{\Delta x}{2}-x))}{i\sin(\omega \frac{\Delta x}{2})}\\
0&\le CA\le \frac{\cos( \omega\frac{\Delta x}{2})\cos(\omega x) + \sin(\omega\frac{\Delta x}{2})\sin(\omega x) + i\sin( \omega\frac{\Delta x}{2})\cos(\omega x) - i\cos(\omega\frac{\Delta x}{2})\sin(\omega x)}{i\sin(\omega \frac{\Delta x}{2})}\\
0&\le CA\le -i \cot\left(\omega \frac{\Delta x}{2}\right)\cos(\omega x) -i \sin(\omega x) +\cos(\omega x) -\cot\left(\omega\frac{\Delta x}{2}\right)\sin(\omega x) \\
0&\le CA \le \left(\cos(\omega x)-\cot\left(\omega\frac{\Delta x}{2}\right)\sin(\omega x)\right)-i \left(\cot\left(\omega \frac{\Delta x}{2}\right)\cos(\omega x) + \sin(\omega x)\right)\\
0&\le |CA|\le \sqrt{\cos^{2}(\omega x) +\sin^{2}(\omega x)\cot^{2}\left(\omega\frac{\Delta x}{2}\right) -2\cos(\omega x)\sin(\omega x)\cot\left(\omega\frac{\Delta x}{2}\right)+}\\
&\quad\quad\quad\quad\quad\quad \overline{+ \cos^{2}(\omega x)\cot^{2}\left(\omega\frac{\Delta x}{2}\right)+\sin^{2}(\omega x) +2\cos(\omega x)\sin(\omega x)\cot\left(\omega\frac{\Delta x}{2}\right)}\\
0&\le |CA|\le \sqrt{1+\cot^{2}\left(\omega \frac{\Delta x}{2}\right)}\\
0&\le |CA|\le \Biggr|\csc\left(\omega\frac{\Delta x}{2}\right)\Biggr|
\end{align*}$$ %%

- Decidi tentar verificar isto com código. Da equação $\frac{u^{n+1}_i - u^{n}_i}{\Delta t} + au^{n}_i\Bigl( \frac{u^{n}_i - u^{n}_{i-1}}{\Delta x}\Bigr)= 0$ podemos obter:
$$u_{i}^{n+1}= u_{i}^{n}[1-C (u_{i}^{n}-u_{i-1}^{n})]$$

#### :'(
No 1º e 2º gráficos vemos os valores máximos e mínimos que $C$ pode ter e que garantem uma solução estável. Imediatamente vemos que existem várias zonas em que o gráfico é branco. Isto significa que o valor é _indefinido_.  
Vamos ver um exemplo concreto: consideremos $\omega=2$. Fica $\cot^2(\omega \frac{\Delta x}{2})=\cot^2(\Delta x)$. Ora, se $\Delta x=0.1$ temos $\cot^2(\omega\frac{\Delta x}{2})\simeq100$. Conforme $\Delta x$ diminui temos que $C_{\text{max}}\to\sqrt{-\infty},C_{\text{min}}\to\sqrt{-\infty}$, que não é um número. Assim facilmente vemos que para um problema com $x\in[0,1]$ como aquele em estudo, não conseguiremos determinar uma solução com uma resolução espacial adequada (sendo que $0.1$ é $10\%$ da escala!).

No 3º gráfico vemos o que acontece ao tentar resolver a equação de Burger invíscida com o método de upwind. A solução rapidamente se torna instável, deixando até de percorrer o domínio todo a partir de certos valores de tempo (para $t=18$ o traçado termina em $x\simeq0.5$, dando erro a partir daí).
Além disso, só temos apenas 20 pontos espaciais, notando-se a baixa suavidade dos traçados. 

## 4.
- Temos $u=(1-\frac{2\rho}{\rho_{M}})$. Daqui podemos obter:
$$\begin{align*}
F  &=  \rho v_{\text{max}} \Bigl(1 - \frac{\rho}{\rho_{\text{max}}} \Bigr)\\
&= \rho v_\text{max} \left(1- \frac{1}{2}(1-u)\right)\\
&= \frac{1}{2}v_\text{max}\rho(1+u)\\
\end{align*}$$

## 5.
- No MacCormick temos:
$$\frac{\partial u}{\partial t}=- \frac{\partial F}{\partial x}$$
- Para a equação de Burger Víscida isto fica:
$$\frac{\partial u}{\partial t}=-\frac{\partial F}{\partial x} + \sigma \frac{\partial^{2}u}{\partial x^{2}}$$
Sendo $\frac{\partial^{2}u}{\partial x^{2}}=\frac{u_{i-1}-2u_{i}+u_{i+1}}{\Delta x^{2}}$, decidi adaptar o esquema de MacCormick usado acima da sequinte forma:
$$\bar{u}^{n+1}_i=u^{n}_i-\frac{\Delta t}{\Delta x}(F^{n}_{i+1}-F^{n}_i) + \sigma\frac{\Delta t}{\Delta x^{2}}(u_{i-1}^{n}-2u_{i}^{n}+u_{i+1}^{n})$$
$$u^{n+1}_i = \frac{1}{2}(\bar{u}^{n+1}_i + u^n_i) -\frac{\Delta t}{ 2\Delta x}(\bar{F}^n_i-\bar{F}^n_{i-1})$$
- Deixei o segundo termo igual, visto que este é o termo corretor, que tem a função de aproximar $u$ de $\bar u$. Assim, acrescentei a segunda derivada ao termo *predictor*.