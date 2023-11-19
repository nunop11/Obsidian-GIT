## Separação de Variáveis
(NOTA: As coordenadas não têm a distribuição normal. O $z$ aponta para fora do ecrã!!)
![[2 planos infinitos.png|550]]
- No sistem acima temos 2 placas infinitas paralelas ao plano $zOx$ a potencial nulo. As placas são infinitas, mas são limitadas, existindo apenas em $x\ge0$ . A parte do plano $x=0$ entre as placas é mantido a um potencial $V_{0}(y)$.
- Temos as condições de fronteira:
    - $V(x,0)=V(x,a)=0$
    - $V(0,y)=V_{0}(y)$
    - $V(\infty,y)=0$

- Vemos então que, relativamente a $z$, o plano é infinito e sempre "igual". Ou seja, temos **geometria de translação no eixo** doz $z$. Como tal, podemos escrever $V=V(x,y)$
- Assim, vamos fazer *separação de variáveis*: $V(x,y)=f(x)g(y)$. Ao substituir na equação de Laplace:
$$\begin{align*}
\nabla^{2}V=0 \to \frac{\partial^{2}V}{\partial x^{2}} + \frac{\partial^{2}V}{\partial y^{2}}&= 0\\
g \frac{d^{2}f}{dx^{2}}+ f \frac{d^{2}g}{dy^{2}}&= 0\\
\frac{1}{f} \frac{d^{2}f}{dx^{2}}&= - \frac{1}{g} \frac{d^{2}g}{dy^{2}} 
\end{align*}$$

(como em Moderna e Quântica)
- Ora, a única forma de a igualdade acima se verificar é se ambos os lados forem iguais a uma constante, a que chamaremos $k^{2}$:
$$\frac{1}{f} \frac{d^{2}f}{dx^{2}}=k^{2}= - \frac{1}{g} \frac{d^{2}g}{dy^{2}} $$
Ao resolver os 2 lados temos:
$$\begin{align*}
\frac{d^{2}f}{dx^{2}}=k^{2}f \quad \quad &;\quad \quad \frac{d^{2}g}{dx^{2}}=k^{2}g\\
f= Ae^{kx}+Be^{-kx} \quad \quad &; \quad \quad g= C\sin(ky)+D\cos(ky)
\end{align*}$$
(mini explicação: para $f$ ficamos com expoentes reais como temos assim ($\sqrt{k^{2}}$). Para $g$ ficamos com expoentes imaginários ($\sqrt{-k^{2}}$) e transformamos na forma acima)

- Apliquemos agora as condições de fronteira:
    - $V(\infty,y)=0: f=B e^{-kx}$
    - $V(x,0)=0: D=0 \to g=C\sin(kx)$ 
    - $V(x,a)=0: g=C\sin(\frac{n\pi}{a}y)$

- Isto resulta em:
$$V(x,y)=\sum\limits_{n=1}^{\infty} C_{n} e^{\frac{-n\pi}{a}x}\sin\left(\frac{n\pi}{a}y\right)$$
de onde obtemos:
$$V_{0}(y)=\sum\limits_{n=1}^{\infty} C_{n} \sin\left(\frac{n\pi}{a}y\right)$$
- Ora, isto não passa de uma série de Fourier escrita na forma de senos. Usando este facto conseguimos determinar os coeficientes $C_{n}$.
- Multipliquemos os 2 lados da equação acima por $\sin\left(\frac{n'\pi}{a}y\right)$ e integramos de $0$ a $a$:
$$\sum\limits_{n=1}^{\infty} C_{n} \int_{0}^{a} \sin\left(\frac{n\pi}{a}y\right)\sin\left(\frac{n'\pi}{a}y\right)dy=\int_{0}^{a} V_{0}(y)\sin\left(\frac{n'\pi}{a}y\right)dy$$
em que o integral da esquerda é igual a $\frac{a}{2}\delta_{n,n'}$:
$$\begin{align*}
\sum\limits_{n=1}^{\infty} C_{n} \frac{a}{2}\delta_{n,n'}&= \int_{0}^{a} V_{0}(y)\sin\left(\frac{n'\pi}{a}y\right)dy\\
C_{n}&= \frac{2}{a}\int_{0}^{a}V_{0}(y)\sin\left(\frac{n\pi}{a}y\right)dy
\end{align*}$$
em que perdemos o sumatório, pois apenas o temos com $n=n'$ será não nulo. Similarmente, do lado direito ficamos com $n'=n$.
- Consideremos agora que $V_{0}(y)=V_{0}$. Ficamos com:
$$\begin{align*}
C_{n}&= \frac{2V_{0}}{a} \int_{0}^{a}\sin\left(\frac{n\pi}{a}y\right)dy= \frac{2V_{0}}{n\pi}(1-\cos n\pi)=\begin{cases}
0 & ; & n~~par\\ \frac{4V_{0}}{n\pi}  & ; & n~~ímpar
\end{cases}
\end{align*}$$
- E ficamos então com a solução do potencial neste sistema:
$$V(x,y)= \frac{4V_{0}}{\pi} \sum\limits_{n=1,3,5,\dots}^{\infty} \frac{1}{n} e^{\frac{-n\pi}{a}x}\sin\left(\frac{n\pi}{a}y\right)$$
- Ao desenvolver a série de Fourier acima obtemos:
$$V(x,y)=\frac{2V_{0}}{\pi} \arctan \left( \frac{\sin\left(\frac{\pi}{a}y\right)}{\sin\left(\frac{\pi}{a}x\right)}\right)$$

## Geometria Esférica
![[EM2/coordenadas esfericas.png]]
- Consideremos que temos um potencial com geometria esférica, mas que não varia de forma azimutal: $V=V(r,\theta)$
- Ora, em coordenadas esféricas o laplaciano é da forma:
$$\nabla^{2}=\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r \frac{\partial}{\partial r}\right)+ \frac{1}{r^{2}\sin\theta} \frac{\partial}{\partial\theta} \left(\sin\theta \frac{\partial}{\partial\theta}\right)+ \frac{1}{r^{2}\sin^{2}\theta} \frac{\partial^{2}}{\partial\phi^{2}}$$
- Assim, para o potencial que estamos a considerar, a equação de Laplace fica da forma:
$$\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(r \frac{\partial V}{\partial r}\right)+ \frac{1}{r^{2}\sin\theta} \frac{\partial}{\partial\theta} \left(\sin\theta \frac{\partial V}{\partial\theta}\right)=0$$
em que podemos fazer *separação de variáveis*: $V(r, \theta)=R(r)\Theta(\theta)$. Temos:
$$\frac{1}{R} \frac{d}{dr}\left(r^{2} \frac{dR}{dr}\right)=- \frac{1}{\Theta\sin\theta} \frac{d}{d\theta}\left(\sin\theta \frac{d\Theta}{d\theta}\right)=\ell(\ell+1)$$
em que, novamente, temos 2 lados que dependem de 2 variáveis diferentes. Por essa razão, terão que ser ambos iguais a uma constante, que definimos como $\ell(\ell+1)$.

- Ora, para $R(r)$ temos a solução:
$$R(r)=Ar^{\ell} + \frac{B}{r^{\ell+1}}$$
- Para $\Theta(\theta)$ a solução é escrita com polinómios de Legendre:
$$\Theta(\theta)= P_{\ell} (\cos\theta)$$
em que o *polinómio de legendre* de grau $\ell$ é dado por:
$$P_{\ell}(x)= \frac{1}{2^{\ell}\ell!} \left(\frac{d}{dx}\right)^{\ell}(x^{2}-1)^{\ell}$$
- Assim, a solução da equação de Laplace para uma geometria assim seria:
$$V(r,\theta)=\sum\limits_{\ell=0}^{\infty} \left(A_{\ell}r^{\ell} + \frac{B_{\ell}}{r^{\ell+1}}\right)P_{\ell}(\cos\theta)$$