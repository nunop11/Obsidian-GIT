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
![[gamma e kappa.png|600]]

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

- Para um certo $\ell$ temos $X_{\ell m}~(m=1,2,3,\dots,M_{\ell})$ e temos
$$k_{T_{\ell m}}=\frac{X_{\ell m}}{a}~\to~ \beta_{\ell m}^{2}=n_{1}^{2}k_{0}^{2}-k_{T_{\ell m}}^{2}~\to~ \gamma_{\ell m}^{2}=\beta_{\ell m}^{2}-n_{2}^{2}k_{0}^{2}$$

#### EX
- Consideremos o caso em que $\ell=0,V=10$:
$$\begin{align*}\ell=0:~~ X \frac{J_{\ell-1}(X)}{J_{\ell}(X)}&= -Y \frac{K_{\ell-1}(X)}{K_{\ell}(Y)}\\
X \frac{J_{-1}(X)}{J_{0}(X)}&= -Y \frac{K_{-1}(Y)}{K_{0}(Y)}\\
X \frac{J_{1}(X)}{J_{0}(X)}&= Y \frac{K_{1}(Y)}{K_{0}(Y)}
\end{align*}$$
em que:
$$J_{-1}(X)=-J_{1}(X) \quad;\quad K_{-1}(Y)=K_{1}(Y)$$
![[numero de modos grafico.png]]
- Ora, o lado esquerdo da equação é independente de $V$. Já o lado direito move-se para a direita com aumento de $V$.
- Assim, consoante aumenta $V$ aumentam o número de interseções (modos) no gráfico acima. Ora, considerando que as curvas tipo parábola são $x \frac{J_1(x)}{J_0(x)}$ vemos que:
$$\text{numero interseções = numero de zeros de }J_{\ell-1}(X)$$
apenas *quando* $X\le V$
![[numero de modos grafico com zeros.png]]

##### Zeros
- Chamamos aos zeros de $J_{\ell-1}(X)$ de $x_{\ell m}$
- Assim definimos o último zero $x_{\ell M_{\ell}}$ como:
    - $J_{\ell-1}(x_{\ell M_{\ell}})=0$
    - $x_{\ell M_{\ell}}\le V$
- Notemos, na figura acima, que $$x_{\ell m}<X_{\ell m}$$
- Ora, um modo definido por $(\ell,m)$ é **permitido** se $$\boxed{X_{\ell m}\le V~~~~;~~~~ x_{\ell m}\le V}$$
- Como vimos, as curvas "parabólicas" não dependem de $V$. Mas a curva tracejada vai para a direita com aumento de $V$. Assim, se diminuirmos $V$ iremos mover os pontos de interseção para a esquerda e temos $X_{03}\to X_{03}$!!!
- Em geral, um certo modo $(\ell,m)$ deixa de se propagar quando temos $x_{\ell m}=V$

##### Modos mínimos
**l=0**
- Vemos então que, mesmo que $V$ seja muito reduzido, temos *sempre 1 modo*: $X_{01}$ (em que $x_{01}=0$)
- Por outras palavras, o modo $\ell=0,m=1$ propaga-se **SEMPRE**

**l=1**
- Aplicando a mesma lógica, o modo mínimo de $\ell=1$ ($x_{11}$) propaga-se quando $V<x_{11}=2.405$! (supostamente este é o primeiro zero de $x \frac{J_{\ell}'}{J_{\ell}}$)
- Assim, quanto $V<2.405$ (o modo 11 não se propaga), apenas o modo 01 existe e temos uma fibra MONOMODO

## Resumo até agora:
- Fibras fracamente guiadas são as normais em comunicações óticas
- Nestas, as componetnes longitudinais são menores que as transversas: $E_{z},H_{z}\ll E_\phi,E_r,H_\phi,H_r$
- Não existe portanto grande diferença entre modos TE e TM (mesma $\beta$ e distribuição espacial em xOy)
- Os modos TE e TM são degenerados -  temos propagação modal, cada modo consiste numa radiação com polarização linear constante no plano transverso. Cada modo é identificado por um $(\ell,m)$
- Na aproximação paraxial deifnimos os modos como linearmente polarizados: modos LP
![[modos polarizados.png]]
- A *equação carateristica da aproximação paraxial* é: $$X \frac{J_{\ell-1}(X)}{J_{\ell}(X)}=-Y \frac{K_{\ell-1}(Y)}{K_{\ell}(Y)}$$
- Vimos o caso em que $\ell=0,V=10$. O número de valores diferentes de $\beta_{m}$ é igual ao número de interseções de $X\frac{J_{\ell-1}(X)}{J_{\ell}(X)}$ com $Y=\sqrt{V^{2}-X^{2}}$. 
- Outra forma de formular isso é: número de zeros $x_{\ell m}$ de $J_{\ell-1}(X)$ em que $X\le V$
- Quando $V=x_{\ell m}$, o modo $(\ell,m)$ deixa de se propagar no guia

## Caso de V muito grande
- Por outro lado, se $V\gg1$ temos  muitos zeros entre 0 e V. 
- Além disso, neste caso teremos $x\gg1$. Podemos então dizer que:
$$J_{\ell}(x)\approx \sqrt{\frac{2}{\pi x}}\cos \left[x- \left(\ell+ \frac{1}{2}\right) \frac{\pi}{2} \right]$$
logo temos zeros em $\frac{1}{2}\pi,\frac{3}{2}\pi,\frac{5}{2}\pi,\dots=(2m-1) \frac{\pi}{2}$

### Modos
- Mas os zeros que decidem onde temos polos são os zeros de $J_{\ell-1}$, não de $J_{\ell}$. Logo os zeros estão em:
$$x_{\ell m}= \left(2m+\ell - \frac{3}{2}\right) \frac{\pi}{2}$$
e como $x\gg1$ podemos escrever:
$$x_{\ell m}\approx (2m+\ell) \frac{\pi}{2}$$
(consideramos apenas $\ell\ge0$)

**Número de modos**
- Para o último modo que se propaga teremos $x_{\ell m}=x_{\ell M_{\ell}}=V$. Assim:
$$V= (2M_{\ell}+\ell) \frac{\pi}{2}~~\to~~ M_{\ell}=\frac{V}{\pi}- \frac{\ell}{2}$$
em que: $M_{0}=V/\pi$, $\ell_{\text{max}}=\frac{2V}{\pi}$ e $M_{\ell_\text{max}}=0$
- Disto temos a reta que define os estamos $(\ell,m)$ permitidos:
![[modos permitidos.png]]
- Assim, o número total de modos $M$ é: $$M= \underbrace{2}_\text{polarização} \times \underbrace{2}_\text{$\ell$ pode ser <0} \times \sum\limits_{\ell=0}^{\ell_\text{max}}M_{\ell}=  \frac{4V^{2}}{\pi^{2}}$$
notemos que:
$$\begin{align*}
\sum\limits_{\ell=0}^{\ell_\text{max}}M_{\ell}&= \sum\limits_{\ell=0}^{\frac{2V}{\pi}}\left(\frac{V}{\pi}- \frac{\ell}{2}\right)\\
&= \left(\frac{2V}{\pi}+1\right) \frac{V}{\pi}- \underbrace{\frac{1}{2}\sum\limits_{\ell=0}^{\frac{2V}{\pi}}\ell}_\text{serie aritmetica}\\\\
&= \left(\frac{2V}{\pi}+1\right) \frac{V}{\pi}- \frac{1}{2} \frac{\frac{2V}{\pi}(\frac{2V}{\pi}+0)}{2}\\
&= 2 \frac{V^{2}}{\pi^{2}}+ \frac{V}{\pi}- \frac{V^{2}}{\pi^{2}}\\
&= \frac{V^{2}}{\pi^{2}}+ \frac{V}{\pi}\\
&\approx \frac{V^{2}}{\pi^{2}}~~~~ (V\gg1)
\end{align*}$$
Ou seja:
$$M= \frac{4V^{2}}{\pi^{2}}~~~~;~~~~ V= \frac{\pi}{2} \sqrt{M}$$
o que nos dá:
![[numero de modos vs V.png]]

### Dispersão
- Temos que:
$$\begin{cases}
X_{\ell m}=k_{T_{\ell m}}a \\
\beta_{\ell m}^{2}=n_{1}^{2}k_{0}^{2}-k_{T_{\ell m}}^{2} 
\end{cases}\to~~ \beta_{\ell m}=\sqrt{n_{1}^{2}k_{0}^{2}- \frac{X_{\ell m}^{2}}{a^{2}}}$$
- Acabamos de ver que, caso $V\gg1$ temos $X_{\ell m}=(2m+\ell) \frac{\pi}{2}$
- E ficamos com:
$$\beta_{\ell m}=\sqrt{n_{1}^{2}k_{0}^{2}- (2m+\ell)^{2}\frac{\pi^{2}}{4a^{2}}}$$
- Sabemos ainda que:
$$\begin{align*}
M&= \frac{2V^{2}}{\pi^{2}}\\
&= \frac{2}{\pi^{2}} \left(2\pi \frac{a}{\lambda_{0}} \sqrt{n_{1}^{2}-n_{2}^{2}}\right)^{2}\\
&= \frac{4}{\pi^{2}} \cdot 2n_{1}^{2} \Delta \cdot a^{2} k_{0}^{2} \quad \quad \quad;\quad \Delta=\frac{n_{1}-n_{2}}{n_{1}}\\
\frac{\pi^{2}}{4 a^{2}}&= \frac{2 n_{1}^{2}\Delta k_{0}^{2} }{M} = n_{1}^{2}k_{0}^{2} \frac{2\Delta}{M}
\end{align*}$$
logo temos:
$$\beta_{\ell m}=n_{1}k_{0} \sqrt{1-2 \frac{(2m+\ell)^{2}}{M}\Delta}~~~~,~~\ell\ge0$$
- Temos a incrível expansão de taylor $\sqrt{1+x}=1+ \frac{x}{2}$ se $x\ll1$. Assim, podemos aproximar:
$$\beta_{\ell m}=n_{1}k_{0}\left(1- \frac{(2m+\ell)^{2}}{M}\Delta \right)$$
- Notemos ainda que, considerando $M=\frac{4V^{2}}{\pi^{2}}$ temos: $$\ell_\text{max}=\sqrt{M}$$

- Temos então:
![[modos permitidos 2.png]]
logo, para um certo $\ell$ temos um $m_\text{lim}$ (para um certo yy iremos bater na reta ao aumentar $m$). Assim:
$$m_\text{lim} = M_{\ell}=\frac{1}{2}\left(\frac{2V}{\pi}-\ell \right)=\frac{1}{2}(\sqrt{M}-\ell)$$

#### Juntando tudo
- Para um certo modo  $(\ell,m)$ temos:
$$\beta_{\ell m}=n_{1}k_{0}\left(1- \frac{(2m+\ell)^{2}}{M}\Delta \right)\quad;\quad \begin{align*}
\ell&= 0,1,2\dots,\sqrt{M}\\\\
m&= 1,2,3,\dots,\frac{\sqrt{M}-\ell}{2}
\end{align*}$$

#### Caso mínimo
- No caso mínimo temos $\ell=0,m=1$ logo:
$$\beta_{(\ell m)_{\text{max}}}=\beta_{01}=n_{1}k_{0}\left(1- \frac{4\Delta}{M}\right)\approx n_{1}k_{0}$$

#### Caso máximo
- Os casos máximos ocorrem quando temos pontos na reta a vermelho na figura, ou seja:
$$\ell= \frac{2V}{\pi}- 2m_{|m=M_{\ell}}~~\to~~ 2m+\ell= \frac{2V}{\pi}=\sqrt{M}$$
logo:
$$\beta_{(\ell m)_\text{min}}=n_{1}k_{0}(1- \Delta)=n_{2}k_{0}$$
- Ou seja, obtemos a partir dos índices dos modos um resultado que tinhamos obtido nos guias planares:
$$\beta_{\ell m}\in[n_{2}k_{0},n_{1}k_{0}]$$
![[beta vs V.png]]

#### Velocidades
- Sabemos que a velocidade de grupo é dada por:
$$v_{g}=\frac{d\omega}{d\beta_{\ell m}}=\frac{1}{\frac{d\beta_{\ell m}}{d\omega}}$$
- Podemos escrever:
$$M=\frac{4V^{2}}{\pi^{2}}=\frac{4}{\pi^{2}} \text{NA}^{2}a^{2}k_{0}^{2}=\frac{8\Delta}{\pi^{2}}a^{2} \left(\frac{\omega}{c_{1}}\right)^{2}$$
em que $\text{NA}^{2}=n_{1}-n_{2}=n_{1}\Delta$. 
- Temos ainda que $n_{1}k_{0}=\omega/c_1$. 
- Juntando tudo temos que:
$$\beta_{\ell m}= \frac{\omega}{c_{1}}\left[1 - \frac{\pi^{2}(2m+\ell)^{2}}{8a^{2}} \left(\frac{c_{1}}{\omega}\right)^{2} \right]$$
logo (não faço ideia como se chega a este resultado):
$$v_{g}=c_{1}\left[1- \frac{(2m+\ell)^{2}}{M} \Delta\right]$$
- Assim, como $2\le 2m+\ell\le \sqrt{M}$ temos:
$$c_{1}(1-\Delta)\le v_{g}\le c_{1}$$
- Finalmente:
    - Para modos *de ordem baixa* temos $v_{g}=c_{1} ~~(2m+\ell=2)$
    - Para modos *de ordem alta* temos $v_{g}=c_{1}(1-\Delta)~~(2m+\ell=\sqrt{M})$ 
- Temos então **Dispersão modal**
- Para o modo LP01:
![[dispersao modal lp01.png]]
    - Este gráfico mostra que para cada $\omega$ (frequência da luz AKA comprimento de onda) temos um valor permitido de $\beta_{01}$ (indicado pela linha azul). Ou seja, para um mesmo modo temos dispersão temporal.
    - Os limites  com $c_{1}\beta,c_{2}\beta$ maracam as velocidades com que cada comprimento de onda se propagaria no núcleo e no revestimento da fibra, respetivamente.

## Caso NÃO paraxial
- Consideremos a situação geral, obtendo soluções **exatas** para a equação caraterística geral:
$$(\Gamma_{\ell}+K_{\ell})(k_{1}^{2}\Gamma_{\ell} + k_{2}^{2}K_{\ell})= \left(\frac{\beta \ell}{a}\right)^{2} \left[ \frac{1}{k_{T}^{2}} + \frac{1}{\gamma^{2}} \right]^{2}$$
em que
![[gamma e kappa 2.png]]

- Depois veremos porquê, mas vamos substituir $\ell\in\mathbb{Z}_{0}^{+}$ por $\nu=0,\pm1,\pm2,\dots\in \mathbb{Z}$ logo:
$$(\Gamma_{\nu}+K_{\nu})(k_{1}^{2}\Gamma_{\nu} + k_{2}^{2}K_{\nu})= \left(\frac{\beta \nu}{a}\right)^{2} \left[ \frac{1}{k_{T}^{2}} + \frac{1}{\gamma^{2}} \right]^{2}$$
- Assim, as soluções desta equação dão-nos modos $(\nu,m)$ em que temos constantes de propagação $\beta_{\nu m}$ que descrevem **modos híbridos**

### V
- Vimos que $V$ pode ser definidos como
$$V= \sqrt{X^{2}+Y^{2}}= \frac{2\pi a}{\lambda_{0}}\text{NA}=a \sqrt{k_{T}^{2} + \gamma^{2}}$$
e podemos chamar-lhe *frequência normalizada*
- Associado a um certo $V$ podemos definir uma *constante de propagação normalizada*:
$$b_{\nu m}= \frac{a^{2}\gamma^{2}_{\nu m}}{V^{2}}=\frac{\left(\frac{\beta_{\nu m}}{k_{0}}\right)^{2}-n_{2}^{2}}{n_{1}^{2}-n_{2}^{2}}$$
- Notemos que quando $\beta_{\nu m}=n_{2}k_{0}$ temos $b_{\nu m}=0$
    - Podemos ver, pela equação acima, que $\beta/k_{0}$ é uma espécie de *indice de refracao efetivo do modo* $(\nu,m)$. Assim, ele carateriza a velocidade com que a fibra se propaga no meio
    - Temos então $n_\text{eff}= \frac{\beta_{\nu m}}{k_{0}}\in[n_{2},n_{1}]$

- Temos a seguinte relação entre $\beta/k_{0}$ e $V$:
![[relacao para modos he e te.png]]
e podemos determinar os perfis dos campos eletromagnéticos de alguns destes modos:
![[modos te, tm e ge.png]]

### Aproximação
- Consideremos agora a aproximação $n_{1}\approx n_{2}\to \Delta\ll1$. Esta significa que $k_{1}\approx k_{2}\approx \beta$, logo a equação caraterística fica
$$\beta^{2}(\Gamma_{\nu}+K_{\nu})= \beta^{2} \left(\frac{\nu}{a}\right)^{2} \left(\frac{1}{k_{T}^{2}}+ \frac{1}{\gamma^{2}}\right)^{2}$$
logo $\beta$ desaparece. Temos:
$$\Gamma_{\nu}+K_{\nu}=\pm \frac{\nu}{a}\left(\frac{1}{k_{T}^{2}}+ \frac{1}{\gamma^{2}}\right)^{2}$$
em que
$$\Gamma_{\nu}=\frac{J_{\nu}'(k_{T}r)}{k_{T}J_{\nu}(k_{T}r)_{|r=a}} \quad;\quad K_{\nu}= \frac{K_{\nu}'(\gamma r)}{K_{\nu}(\gamma r)_{|r=a}}$$
- Tendo em contra as equações que permitem discretizar as derivadas:
$$J'_{\ell}(x)=\pm J_{\ell\mp1}(x) \mp \ell\frac{J_{\ell}(x)}{x} \quad ;\quad \text{igual para }K_{\ell}'$$
obtemos uma série de combinações de sinais, que apenas resultam em 2 equações:
$$\begin{align*}
\text{Modos EH : } \quad \quad \quad \quad~\frac{J_{\nu+1}(k_{T}a)}{k_T J_{\nu}(k_{T}a)} &= - \frac{K_{\nu+1}(\gamma a)}{\gamma K_{\nu}(\gamma a)}\\
\text{Modos HE : } \quad \quad -\frac{J_{\nu-2}(k_{T}a)}{k_T J_{\nu-1}(k_{T}a)} &= \frac{K_{\nu-2}(\gamma a)}{\gamma K_{\nu-1}(\gamma a)}
\end{align*}$$

- Podemos juntar esta equaçõ numa só definindo o fator $\ell$:
$$\ell\equiv \begin{cases}
0 & ; & \text{modos TE e TM} \\
\nu+1  & ; & \text{modos EH} \\
\nu-1 & ; & \text{modos HE}
\end{cases}$$
e recuperamos a equação da aproximação paraxial:
$$X \frac{J_{\ell-1}(X)}{J_{\ell}(X)}=-Y \frac{K_{\ell-1}(Y)}{K_{\ell}(Y)}$$
- Quando fazemos aproximação paraxial estamos a converger vários valores da equação exata para 1 só modo
- Isso quer dizer que nesta aproximação temos vários modos com a mesma constante de propagação. Assim, quando 1 é excitado *todos* são excitados!
- A distribuição de campo transverso resulta na sobreposição dos campos destes modos

### Modos LP
- Podemos então definir modos LP (Linear Polarized), que têm a mesma distribuição transversa em todas as secções retas da fibra
- Todos estes modos podem ser definidos como sobreposições de modos TE, TM, HE, EH

**LP0m**
- Cada modo  $\text{LP}_{0m}$ deriva de um modo $\text{HE}_{1m}$:
![[lp em funcao de he.png]]

**LP1m**
- Cada modo $\text{LP}_{1m}$ deriva de modos $\text{TE}_{0m},\text{TM}_{0m},\text{HE}_{2m}$
![[lp em funcao de te,tm e he.png]]

**Ordem superior**
- Podemos generalizar isto.
- Cada modo  $\text{LP}_{\ell m} (\ell\ge2)$ derivada de modos $\text{HE}_{\ell+1,m}~,~\text{EH}_{\ell-1,m}$
![[lp em funcao de he e eh.png]]

### Constante de propagação normalizada
- Tudo igual a atrás
- Temos $V$, a frequência normalizada
- Com ela definimos $b_{\ell m}$, a constante de propagação normalizada
- Novamente temos $$n_\text{eff}=\frac{\beta_{\ell m}}{k_{0}}\in[n_{2},n_{1}]$$
- Para modos LP a relação $b$ VS $V$ é assim:
![[b vs V para LP.png]]
- Temos que:
    - num modo de menor ordem temos maior radiação EM no núcleo
    - num modo de maior ordem temos mais radiação na bainha

### Um pouco de teoria
- De um ponto de vista de EM clássico, a intensidade do campo EM que temos na fibra é dada pelo módulo da componente real do vetor Poynting complexo. Assim, para uma onda EM a propagar-se na direção z:
$$S_{z}=\frac{1}{2}\vec{E}\times \vec{H}^{*}$$
e temos a potência ao longo da fibra:
$$P= \frac{1}{2}\text{Re}\left[ \int_\text{secção fibra} \vec{E}\times\vec{H}^{*} \right]$$
e integramos em coordenadas cilindricas
$$\begin{align*}
P&= \frac{1}{2}\text{Re} \left[\int\limits_{0}^{+\infty}\int\limits_{0}^{2\pi} r(E_{x}H_{y}^{*} - E_{y}H_{x}^{*})d\phi dr \right]\\
&= \frac{1}{2}\text{Re} \left[\int\limits_{0}^{a}\int\limits_{0}^{2\pi} r(E_{x}H_{y}^{*} - E_{y}H_{x}^{*})d\phi dr + \int\limits_{a}^{+\infty}\int\limits_{0}^{2\pi} r(E_{x}H_{y}^{*} - E_{y}H_{x}^{*})d\phi dr \right]\\
&= P_\text{nucleo} + P_\text{bainha}
\end{align*}$$
- Na aproximação paraxial, tendo-se a energia total dos modos $\ell$ é $P_\ell$. Podemos definir a seguinte relação:
$$\frac{P_{\ell|\text{bainha}}}{P_{\ell}}=1- \frac{P_{\ell|\text{nucleo}}}{P_{\ell}}$$
![[potencia bainha normalizada vs V para cada LP.png]]