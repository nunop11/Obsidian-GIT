# 1 - Oscilador Harmónico - Continuação 
## Medição em sistema Harmónico
- Consideremos que temos a função de onda:
$$\Psi(x,0)= \frac{1}{\sqrt{5}} \varphi_{0}(x) - \frac{2}{\sqrt{5}} \varphi_{3}(x)$$
- Podemos ver que a função está normalizada porque: $|\Psi(x,0)|^{2}= \frac{1}{5}+ \frac{4}{5}=1$
- Facilmente vemos que, numa certa medição de energia, os valores possíveis de obter são: $$E_{0}=\frac{\hbar\omega}{2} \quad \quad;\quad \quad E_{3}= \left( 3 + \frac{1}{2} \right)\hbar \omega$$

## Oscilador Quântico em 3D
- Agora temos $$V(x,y,z) = \frac{1}{2} m \omega_{x}^{2}x^{2} + \frac{1}{2} m \omega_{y}^{2}y^{2} + \frac{1}{2} m \omega_{z}^{2}z^{2}$$
Após alguma dedução temos:
$$\begin{align*}
E_{n_{x}n_{y}n_{z}} &= \left(n_{x} + \frac{1}{2} \right)\hbar \omega_{x} + \left(n_{x} + \frac{1}{2} \right)\hbar \omega_{x} + \left(n_{x} + \frac{1}{2} \right)\hbar \omega_{x}\\
\Psi_{n_{x}n_{y}n_{z}}(x,y,z,0) &= \varphi_{n_{x}}(x) \varphi_{n_{y}}(y) \varphi_{n_{z}}(z)
\end{align*}$$

# 2 - Eq. Schödinger para Potencial Coulombiano
- Um potencial coulombiano é um potencial do tipo: 
$$V(r) = \frac{- e^{2}}{4\pi\varepsilon_{0}}$$
- No referencial com a origem no protão, temos:
$$\left[ - \frac{\hbar^{2}}{2m} \nabla^{2} - \frac{e^{2}}{4\pi\varepsilon_{0}r} \right]\Psi(\vec{r}) = E \Psi(\vec{r})$$

- Temos que, em *coordenadas esféricas*, o laplaciano fica da seguinte forma:
$$\nabla^{2} = \frac{1}{r^{2}} \frac{\partial}{\partial r} \left(r^{2} \frac{\partial}{\partial r} \right) + \frac{1}{r^{2}\sin^{2}\theta} \frac{\partial^{2}}{\partial \phi^{2}} + \frac{1}{r^{2}\sin^{2}\theta} \frac{\partial}{\partial \theta} \left( \sin \theta \frac{\partial}{\partial \theta} \right)$$
e podemos ainda reescrever a função de onda como produto de funções de $r, \theta, \phi$:
$$\Psi(\vec{r})= \Psi(r, \theta, \phi) = R(r) \Theta(\theta)\Phi(\phi)$$
mas por vezes aparece como $\Psi(\vec{r}) = R(r)Y(\theta, \phi)$
- Ao substituir na equação de Schrodinger temos:
$$\frac{-\hbar^{2}}{2m} \left[ \Theta \Phi \frac{1}{r^{2}} \frac{d}{dr}\left( r^{2} \frac{dR}{dr} \right) + R\Theta \frac{1}{r^{2}\sin \theta} \frac{d^{2}\Phi}{d\phi^{2}} + R\Phi \frac{1}{r^{2}\sin\theta} \frac{d}{d\theta}\left( \sin\theta \frac{d\Theta}{d\theta} \right) \right] + V(\vec{r})R\Theta\Phi = E R\Theta\Phi$$
- Se multiplicarmos a equação por $\frac{-2m}{\hbar^{2}} r^{2}$ e dividir $R\Theta\Phi$ temos:
$$\frac{1}{R} \frac{d}{dr} \left( r^{2} \frac{dR}{dr} \right) + \frac{1}{\sin^{2}\theta} \frac{1}{\Phi} \frac{d^{2}\Phi}{d\phi^{2}} + \frac{1}{\sin^{2}\theta} \frac{1}{\Theta} \frac{d}{d\theta} \left(\sin \theta \frac{d\Theta}{d\theta} \right) + V(\vec{r})\left(\frac{-2mr^{2}}{\hbar^{2}}\right) - E \left(\frac{-2mr^{2}}{\hbar^{2}} \right)=0$$
- Vemos que os primeiros 3 termos dependem de $r,\theta,\phi$ e os últimos 2 são constantes. Assim, podemos dividir a equação da seguinte forma, sendo que os dois ramos têm que ser iguais à mesma constante, $k$:
$$\begin{cases} 
\frac{1}{R} \frac{d}{dr} \left( r^{2} \frac{dR}{dr} \right) - \frac{2mr^{2}}{\hbar^{2}}(V(\vec{r})-E)=k \\
\frac{1}{\sin^{2}\theta} \frac{1}{\Phi} \frac{d^{2}\Phi}{d\phi^{2}} + \frac{1}{\sin^{2}\theta} \frac{1}{\Theta} \frac{d}{d\theta} \left(\sin \theta \frac{d\Theta}{d\theta} \right) = -k
\end{cases}$$
(definimos com sendo $k$ e $-k$ para manter a igualduade em que temos que a soma de tudo isto dá 0)
- Se multiplicarmos a equação de cima por $R$ e a de baixo por $\sin^{2}\theta$ temos:
$$
\begin{cases} 
\frac{d}{dr} \left( r^{2} \frac{dR}{dr} \right) - \frac{2mr^{2}}{\hbar^{2}}(V(\vec{r})-E)R=kR \\
\frac{1}{\Phi} \frac{d^{2}\Phi}{d\phi^{2}} + \frac{1}{\Theta} \frac{d}{d\theta} \left(\sin \theta \frac{d\Theta}{d\theta} \right) + k\sin^{2}\theta = 0
\end{cases}
$$
- E na equação de baixo voltamos a ter a mesma coisa. A primeira parte da equação depende de $\phi$, a segunda depende de $\theta$ e a sua soma é igual a uma constante. Assim, temos necessariamente que:
$$\begin{cases}
\frac{1}{\Phi} \frac{d^{2}\Phi}{d\phi^{2}} &= constante &= -m_{\ell}^{2} \\
\frac{1}{\Theta} \frac{d}{d\theta} \left(\sin \theta \frac{d\Theta}{d\theta} \right) + k\sin^{2}\theta &= constante &= +m_{\ell}^{2}
\end{cases}$$

- Assim temos:
## 2.1 - Números Quânticos
$$k \quad \quad;\quad \quad m_{\ell} \quad \quad;\quad \quad \ell$$
- $n$ - número quântico principal, $n=1,2,3,\dots$
- $\ell$ - número quântico orbital (ou de momento angular), $\ell=0,1,2,\dots,n-1$
- $m_{\ell}$ - número quântico magnético, $m_{\ell}=-\ell, -\ell+1,\dots,\ell$

- Ou seja, podemos escrever as soluções da Equação de Schrödinger para o potencial coulombiano assim:
$$\Psi_{n\ell m_{\ell}}(\vec{r})= R_{n\ell} Y_{\ell}^{m_{\ell}}(\theta, \varphi)$$
sendo:
    - $R_{n\ell}(\vec{r})$ a função radial
    - $Y_{\ell}^{m_{\ell}}(\theta, \varphi)$ o harmónico esférico de ordem $\ell$

## 2.2 - Níveis Orbitais
- Recordemos o que temos acima: $\Psi_{n\ell m_{\ell}}$. Ou seja, se tivermos $\Psi_{abc}$, então $n=a, \ell=b, m_{\ell}=c$.

- No nível fundamental temos $n=1$, logo $\Psi_{100}(\vec{r})$ o que é uma *orbital 1s*
- No primeiro nível excitado, ou seja, $n=2$ temos $\ell=0,1$ ; $m_{\ell}=-1,0,1$
    - Em que $\Psi_{200}(\vec{r})$ é uma *orbital 2s*
    - E em que $\Psi_{21-1}(\vec{r}), \Psi_{210}(\vec{r}), \Psi_{211}(\vec{r})$ são *orbitais 2p*

## 2.3 - Espectro
- Temos que $n$ define a camada:
    - $n=1$ - camada $K$
    - $n=2$ - camada $L$
    - $n=3$ - camada $M$
    - $n=4$ - camada $N$

- Por outro lado, $\ell$ define a subcamada:
    - $\ell=0$ - subcamada s
    - $\ell=1$ - subcamada p
    - $\ell=2$ - subcamada d
    - $\ell=3$ - subcamada f

#moderna #fisica #em1 