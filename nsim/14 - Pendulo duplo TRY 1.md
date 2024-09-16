- Consideremos um pêndulo duplo com 2 secções rigidas de comprimento $\ell$.
- Seja $\theta_{1},\theta_{2}$ os ângulos entre a vertical e a 1ª e 2ª secção rigida.
- Temos então:
$$x = \ell(\sin\theta_{1}+\sin\theta_{2}) ~~~~;~~~~ y = \ell(\cos\theta_{1}+\cos\theta_{2})$$
- Temos então as equações obtidas com o sympy:
$$\begin{align*}
\theta&: ~~~~-M\ell_{1}\ddot\theta+M\ell_{2}\sin(\phi-\theta)\dot\theta^{2}-M\ell_{2}\cos(\phi-\theta)\ddot\phi-Mg\sin\theta-\ell_{1}m\ddot\theta-mg\sin\theta=0\\
\phi&: ~~~~\ell_{1}\sin(\phi-\theta)\dot\theta^{2}+\ell_{1}\cos(\phi-\theta)\ddot\theta+\ell_{2}\ddot\phi+g\sin\phi=0
\end{align*}$$
podemos reescrever:
$$\begin{cases}
-(M+m)\ell_{1}\ddot\theta+M\ell_{2}\sin(\phi-\theta)\dot\theta^{2}-M\ell_{2}\cos(\phi-\theta)\ddot\phi-(M+m)g\sin\theta=0 \\
\ell_{2}\ddot\phi= -\ell_{1}\sin(\phi-\theta)\dot\theta^{2}-\ell_{1}\cos(\phi-\theta)\ddot\theta-g\sin\phi
\end{cases}$$
e podemos substituir na 2ª eq:
$$\begin{align*}
(M+m)\ell_{1}\ddot\theta-M\ell_{2}\sin(\phi-\theta)\dot\theta^{2}+M\cos(\phi-\theta)\ell_{2}\ddot\phi+(M+m)g\sin\theta&= 0\\
(M+m)\ell_{1}\ddot\theta-M\ell_{2}\sin(\phi-\theta)\dot\theta^{2}-M\cos(\phi-\theta) \left[\ell_{1}\sin(\phi-\theta)\dot\theta^{2}+\ell_{1}\cos(\phi-\theta)\ddot\theta+g\sin\phi \right] +(M+m)g\sin\theta&= 0\\
(M+m)\ell_{1}\ddot\theta-M\ell_{2}\sin(\phi-\theta)\dot\theta^{2}-M\cos(\phi-\theta) \ell_{1}\sin(\phi-\theta)\dot\theta^{2}-M\cos(\phi-\theta) \ell_{1}\cos(\phi-\theta)\ddot\theta-M\cos(\phi-\theta) g\sin\phi +(M+m)g\sin\theta&= 0\\
\ddot\theta(\ell_{1}(M+m) - M\ell_{2}\cos^{2}(\phi-\theta)) - \dot\theta^{2}(M\ell_{2}\sin(\phi-\theta)+M\ell_{1}\cos(\phi-\theta)\sin(\phi-\theta)) + g(\sin\theta(M+m)-M\sin\phi\cos(\phi-\theta))&= 0\\
\ddot\theta(M(\ell_{1}-\ell_{2}\cos^{2}(\phi-\theta)) +\ell_{1}m) - \dot\theta^{2}(M\sin(\phi-\theta)(\ell_{2}+\ell_{1}\cos(\phi-\theta)) + g(\sin\theta(M+m)-M\sin\phi\cos(\phi-\theta))&= 0\\
\ddot\theta(M(\ell_{1}-\ell_{2}\cos^{2}(\phi-\theta)) +\ell_{1}m) - \dot\theta^{2}(M\sin(\phi-\theta)(\ell_{2}+\ell_{1}\cos(\phi-\theta)) + g(\sin\theta(M+m)-M\sin\phi\cos(\phi-\theta))&= 0\\
\ddot\theta(M(\ell_{1}-\ell_{2}\cos^{2}(\phi-\theta)) +\ell_{1}m)= \dot\theta^{2}(M\sin(\phi+\theta)(\ell_{2}-\ell_{1}\cos(\phi-\theta)) - g(\sin\theta(M+m)-M\sin\phi\cos(\phi-\theta))&\\\\
\ddot\theta= \frac{\dot\theta^{2}(M\sin(\phi-\theta)(\ell_{2}+\ell_{1}\cos(\phi-\theta)) - g(\sin\theta(M+m)-M\sin\phi\cos(\phi-\theta))}{M(\ell_{1}-\ell_{2}\cos^{2}(\phi-\theta)) +\ell_{1}m}&
\end{align*}$$
e daqui resulta:
$$\begin{align*}
\ddot\phi&= -\frac{\ell_{1}\sin(\phi-\theta)\dot\theta^{2}+\ell_{1}\cos(\phi-\theta)\ddot\theta+g\sin\theta}{\ell_{2}}\\
\end{align*}$$
e como ao integrar numericamente o sistema uma aceleração angular de cada vez, não há problema em ter $\ddot\phi(\ddot\theta)$.

--------------

- Temos então as equações obtidas com o sympy:
$$\begin{align*}
\theta&: ~~~~-M\ell_{1}\ddot\theta+M\ell_{2}\sin(\phi-\theta)\dot\theta^{2}-M\ell_{2}\cos(\phi-\theta)\ddot\phi-Mg\sin\theta-\ell_{1}m\ddot\theta-mg\sin\theta=0\\
\phi&: ~~~~\ell_{1}\sin(\phi-\theta)\dot\theta^{2}+\ell_{1}\cos(\phi-\theta)\ddot\theta+\ell_{2}\ddot\phi+g\sin\phi=0
\end{align*}$$
podemos reescrever:
$$\begin{cases}
(M+m)\ell_{1}\ddot\theta - M\ell_{2}\sin(\phi-\theta)\dot\theta^{2}+ (M+m)g\sin\theta= -M\ell_{2}\cos(\phi-\theta)\ddot\phi \\
---
\end{cases}$$
$$\begin{cases}
\ell_{2}\ddot\phi=\frac{-(M+m)\ell_{1}\ddot\theta + M\ell_{2}\sin(\phi-\theta)\dot\theta^{2}-(M+m)g\sin\theta}{M\cos(\phi-\theta)}=-\frac{M+m}{M\cos(\phi-\theta)}\ell_{1}\ddot\theta + \ell_{2}\tan(\phi-\theta)\dot\theta^{2}-\frac{M+m}{M}g\frac{\sin(\theta)}{\cos(\phi-\theta)} \\
---------
\end{cases}$$
e podemos substituir na 2ª eq:
$$\begin{align*}
\ell_{1}\sin(\phi-\theta)\dot\theta^{2}+\ell_{1}\cos(\phi-\theta)\ddot\theta+\ell_{2}\ddot\phi+g\sin\phi&= 0\\
\ell_{1}\sin(\phi-\theta)\dot\theta^{2}+\ell_{1}\cos(\phi-\theta)\ddot\theta-\frac{M+m}{M\cos(\phi-\theta)}\ell_{1}\ddot\theta + \ell_{2}\tan(\phi-\theta)\dot\theta^{2}-\frac{M+m}{M}g\frac{\sin(\theta)}{\cos(\phi-\theta)}+g\sin\phi&= 0\\
\ell_{1}M\cos(\phi-\theta)\sin(\phi-\theta)\dot\theta^{2}+\ell_{1}M\cos^2(\phi-\theta)\ddot\theta-(M+m)\ell_{1}\ddot\theta + \ell_{2}M\sin(\phi-\theta)\dot\theta^{2}-(M+m)g\sin(\theta)+Mg\cos(\phi-\theta)\sin\phi&= 0\\
\ddot\theta(\ell_{1}M\cos^{2}(\phi-\theta) - (M+m)\ell_{1}) + \dot\theta^{2}(\ell_{1}M\cos(\phi-\theta)\sin(\phi-\theta)+\ell_{2}M\sin(\phi-\theta)) +g(M\cos(\phi-\theta)\sin(\phi) - (M+m)\sin\theta)&= 0\\
\ddot\theta\ell_{1}(M\cos^{2}(\phi-\theta)-M-m) + \dot\theta^{2}M\sin(\phi-\theta)(\ell_{1}\cos(\phi-\theta)+\ell_{2}) + g(M\cos(\phi-\theta)\sin(\phi) - (M+m)\sin\theta)&= 0\\
\ddot\theta=-\frac{\dot\theta^{2}M\sin(\phi-\theta)(\ell_{1}\cos(\phi-\theta)+\ell_{2}) + g(M\cos(\phi-\theta)\sin(\phi) - (M+m)\sin\theta)}{\ell_{1}(M\cos^{2}(\phi-\theta)-M-m)}&
\end{align*}$$
logo temos:
$$\ddot\phi=\frac{-(M+m)\ell_{1}\ddot\theta + M\ell_{2}\sin(\phi-\theta)\dot\theta^{2}-(M+m)g\sin\theta}{M\ell_{2}\cos(\phi-\theta)}$$
