- Na aula anterior encontramos as funções $u$ definidas com funções de Bessel como uma possível solução modal.
- Continuamos essa busca. Recordemos o que queremos para definir uma função modal:
    - Ângulos de reflexão (AKA constantes de propagação $\beta$) que permitam um campo ótico com distribuição transversa independente de $z$.
- Ou seja, algo do género:
$$U(r,\phi,z)=G_{E,H}u(r)e^{-i\ell\phi}e^{-i\beta z}$$
em que $G_{E,H}$ é uma constante que varia conforme consideramos $u=E_{z}$ ou $u=H_{z}$
- Na aula anterior obtivemos então
$$u(r)=\begin{cases}
A_{n} J_{\ell}(k_{T}r) & ; & r<a \\
A_{b} K_{\ell}(\gamma r) & ; & r\ge a
\end{cases}$$

### Condições de fronteira
- Falta agora garantir que esta função cumpre as CF
- Temos que, em qualquer situação, há continuidade das componentes tangenciais dos campos E e H *na interface núcleo-bainha*:
    - Continuidade de $E_{\phi}$ e $E_{z}$
    - Continuidade de $H_\phi$ e $H_{z}$
em que, notemos, a interface ocorre num certo raio $r$ logo esse eixo é perpendicular a ela.

- Assim, considerando as constantes $A,B,C,D$ temos:
$$\begin{cases}
E_{z}(r,\phi,z)= AJ_{\ell}(k_{T}r)e^{i\ell\phi}e^{i(\omega t -\beta z)} \quad & ;\quad r<a \text{ (nucleo)}\\
H_{z}(r,\phi,z)= BJ_{\ell}(k_{T}r)e^{i\ell\phi}e^{i(\omega t -\beta z)} \quad & ;\quad r<a \text{ (nucleo)}\\
E_{z}(r,\phi,z)= CK_{\ell}(\gamma r)e^{i\ell\phi}e^{i(\omega t -\beta z)} \quad & ;\quad r\ge a \text{ (bainha)}\\
H_{z}(r,\phi,z)= DK_{\ell}(\gamma r)e^{i\ell\phi}e^{i(\omega t -\beta z)} \quad & ;\quad r\ge a \text{ (bainha)}
\end{cases}$$

#### $E_z$
- Para ter continuidade de $E_{z}$ temos (1=núcleo, 2=bainha):
$$(E_{z1}-E_{z2})_{r=a}=0~~\to~~ AJ_{\ell}(k_{T}a)=CK_{\ell}(\gamma a)$$

#### $E_\phi$
- Temos, da aula anterior, a seguinte equação deduzida das equações de Maxwell:
$$E_{\phi}= \frac{-i}{k^{2}-\beta^{2}}\left[ \frac{\beta}{r} \frac{\partial E_{z}}{\partial \phi} - \mu\omega \frac{\partial H_{z}}{\partial r}\right]$$
- Assim, para ter continuidade de $E_{\phi}$ temos:
$$\begin{align*}
(E_{\phi1}-E_{\phi2})_{r=a}&= 0\\
\frac{i}{k_{T}^{2}} \left[A \frac{i\ell\beta}{a}J_{\ell}(k_{T}a) - \beta\omega\mu k_{T}J_{\ell}'(k_{T}a) \right]&= - \frac{i}{\gamma^{2}} \left[C \frac{i\ell\beta}{a}K_{\ell}(\gamma a)- D\omega\mu\gamma K_{\ell}'(\gamma a) \right]
\end{align*}$$
em que $J_{\ell}'(k_{T}a)=\frac{dJ_{\ell}(k_{T}r)}{d(k_{T}r)}|_{r=a}~~,~~ K_{\ell}'(\gamma a)=\frac{dK_{\ell}(\gamma r)}{d(\gamma r)}|_{r=a}$ 

#### $H_z$
- Fazendo a mesma coisa que para $E_{z}$ obtemos:
$$BJ_{\ell}(k_{T}a)=DK_{\ell}(\gamma a)$$

#### $H_{\phi}$
- Das equações deduzidas de maxwell temos:
$$H_{\phi}=\frac{-i}{k^{2}-\beta^{2}} \left[\frac{\beta}{r} \frac{\partial H_{z}}{\partial \phi} + \varepsilon\omega\frac{\partial E_{z}}{\partial r} \right]$$
e obtemos, tal como acima:
$$\frac{i}{k_{T}^{2}} \left[B \frac{i\ell\beta}{a}J_{\ell}(k_{T}a) + A\omega\varepsilon_{1}k_{T}J_{\ell}'(k_{T}a) \right]= - \frac{i}{\gamma^{2}} \left[ D \frac{i\ell\beta}{a} K_{\ell}(\gamma a) + C\omega\varepsilon_{2}\gamma K_{\ell}'(\gamma a) \right]$$

#### Sistema
- Podemos juntar estas equações na forma de sistema:
$$\small\begin{cases}
AJ_{\ell}(k_{T}a)+0B-CK_{\ell}(\gamma a)+0D=0 \\
-\frac{i}{k_{T}^{2}} \left[A \frac{i\ell\beta}{a}J_{\ell}(k_{T}a) - \beta\omega\mu k_{T}J_{\ell}'(k_{T}a) \right] - \frac{i}{\gamma^{2}} \left[C \frac{i\ell\beta}{a}K_{\ell}(\gamma a)- D\omega\mu\gamma K_{\ell}'(\gamma a) \right]=0 \\
0A+BJ_{\ell}(k_{T}a)+0C-DK_{\ell}(\gamma a)=0 \\
-\frac{i}{k_{T}^{2}} \left[B \frac{i\ell\beta}{a}J_{\ell}(k_{T}a) + A\omega\varepsilon_{1}k_{T}J_{\ell}'(k_{T}a) \right] - \frac{i}{\gamma^{2}} \left[ D \frac{i\ell\beta}{a} K_{\ell}(\gamma a) + C\omega\varepsilon_{2}\gamma K_{\ell}'(\gamma a) \right]=0
\end{cases}$$
- Ora, porque não escrever isto na forma de matrizes:
$$\begin{pmatrix}J_{\ell}(k_{T}a) & 0 & -K_{\ell}(\gamma a) & 0 \\ \frac{\ell\beta}{k_{T}^{2}a}J_{\ell}(k_{T}a) & \frac{i\omega\mu}{k_{T}}J_{\ell}'(k_{T}a) & \frac{\ell\beta}{\gamma^{2}a}K_{\ell}(\gamma a) & \frac{i\omega\mu}{\gamma}K_{\ell}'(\gamma a) \\ 0 & J_{\ell}(k_{T}a) & 0 & -K_{\ell}(\gamma a)  \\ - \frac{i\omega\varepsilon_{1}}{k_{T}}J_{\ell}'(k_{T}a) & \frac{\ell\beta}{k_{T}^{2}a}J_{\ell}(k_{T}a) & - \frac{i\omega\varepsilon_{2}}{\gamma}K_{\ell}'(\gamma a) & \frac{\ell\beta}{\gamma^{2}a}K_{\ell}(\gamma a) \end{pmatrix}\begin{pmatrix}A \\ B \\ C \\ D\end{pmatrix}=0$$
- Para exisitirem soluções não triviais precisamos de ter determinante nulo:
$$\begin{vmatrix}J_{\ell}(k_{T}a) & 0 & -K_{\ell}(\gamma a) & 0 \\ \frac{\ell\beta}{k_{T}^{2}a}J_{\ell}(k_{T}a) & \frac{i\omega\mu}{k_{T}}J_{\ell}'(k_{T}a) & \frac{\ell\beta}{\gamma^{2}a}K_{\ell}(\gamma a) & \frac{i\omega\mu}{\gamma}K_{\ell}'(\gamma a) \\ 0 & J_{\ell}(k_{T}a) & 0 & -K_{\ell}(\gamma a)  \\ - \frac{i\omega\varepsilon_{1}}{k_{T}}J_{\ell}'(k_{T}a) & \frac{\ell\beta}{k_{T}^{2}a}J_{\ell}(k_{T}a) & - \frac{i\omega\varepsilon_{2}}{\gamma}K_{\ell}'(\gamma a) & \frac{\ell\beta}{\gamma^{2}a}K_{\ell}(\gamma a) \end{vmatrix}=0$$

#### Equação caraterística
- Este determinante dá-nos a **equação caraterística**:
$$(\Gamma_{\ell}+K_{\ell})(k_{1}^{2}\Gamma_{\ell}+k_{2}^{2}K_{\ell})= \left(\frac{\beta \ell}{a}\right)^{2} \left[\frac{1}{k_{T}^{2}} + \frac{1}{\gamma^{2}} \right]^{2}$$
em que:
![[Pasted image 20250521163343.png|600]]

- Para cada valor $\ell$ (*número azimutal*), temos uma equação. Cada uma destas tem várias soluções, em que cada uma corresponde a uma constante de propagação: $\beta_{\ell m}~~~~,~~m=1,2,3,\dots,M_{\ell}$
- Assim, podemos caraterizar cada modo com 2 índices: $(\ell,m)$ que descrevem as dependências radial e azimutal do modo
    - Os modos com constantes de propagação resultantes da equação caraterística são *modos híbridos*

##### $\ell=0$
- Este caso consiste em quando temos raios meridionais.
- Neste caso fica:
$$(\Gamma_{0}+K_{0})(k_{1}^{2}\Gamma_{0} + k_{2}^{2}K_{0})=0$$
podemos então dividir esta equação em 2:
$$\begin{align*}
\frac{J_{1}(k_{T}a)}{k_{T}J_{0}(k_{T}a)} + \frac{K_{1}(\gamma a)}{\gamma K_{0}(\gamma a)}&= 0~~~~\to~~~~ E_{z}=0~\Leftrightarrow~ \text{modos TE}\\\\
\frac{n_{1}^{2}k_{0}^{2}J_{1}(k_{T}a)}{k_{T}J_{0}(k_{T}a)} + \frac{n_{2}^{2}k_{0}^{2}K_{1}(\gamma a)}{\gamma K_{0}(\gamma a)}&= 0~~~~\to~~~~ H_{z}=0~\Leftrightarrow~ \text{modos TH}
\end{align*}$$

#### Aproximação paraxial
- Podemos simplificar a equação caraterística ao fazer aproximação paraxial:
$$\Delta = \frac{n_{1}-n_{2}}{n_{1}}\ll1$$
- Nesse caso temos $k_{1}\approx k_{2}$ e $k_{T}^{2}\approx -\gamma^{2}$. Assim, a equação fica:
$$\frac{k_{T}a J_{\ell}'(k_{T}a)}{J_{\ell}(k_{T}a)} = \frac{\gamma a K_{\ell}'(\gamma a)}{K_{\ell}(\gamma a)}$$
e temos, devido à propriedade das funções de Bessel:
$$\begin{align*}
J_{\ell}'(x)&= \frac{dJ_{\ell}(x)}{dx} = \pm J_{\ell\mp1} (x) \mp \ell \frac{J_{\ell}(x)}{x}\\
K_{\ell}'(x)&= \frac{dK_{\ell}(x)}{dx} = - K_{\ell\mp1} (x) \mp \ell \frac{K_{\ell}(x)}{x}
\end{align*}$$
- Assim, podemos escrever a **Equação Característica para fibras step-index na aproximação paraxial**:
$$X \frac{J_{\ell-1}(X)}{J_{\ell}(X)}=-Y \frac{K_{\ell-1}(Y)}{K_\ell(Y)}$$
- Podemos ainda escrever:
$$X^{2}+Y^{2}=V^{2} \quad \quad;\quad V= 2\pi \frac{a}{\lambda_{0}}\text{NA}$$
- $X=k_{T}a$ e $k_{T}=\sqrt{k_{1}^{2}-\beta^{2}}$, logo a *única incognita* nesta equação é $\beta$!

---------- slide 16