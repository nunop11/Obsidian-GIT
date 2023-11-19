### Potencial Esférico - EXEMPLO
![[campo por esfera condutora.png|400]]
- Consideremos o exemplo acima: um condutor esférico de raio $R$ imerso num campo elétrico constante $\vec{E}=E_{0}\hat{z}$. Queremos então a solução da Equação de Laplace na forma $V(r,\theta)$ para $r>R$.
- Temos as condições de fronteira:
    1. $r\to\infty$ : $V\to -E_{0}z+C=-E_{0}r\cos\theta+C$ (porque longe da esfera o potencial apenas é gerado pelo campo externo uniforme e temos $V=Ed$)
    2. $V(r=R,\theta)=0$ porque temos um condutor

- Da aula passado temos que, em coordenadas esféricas, a solução da Equação de Laplace é da forma: $$V(r,\theta)=\sum\limits_{\ell=0}^{\infty} \left(A_{\ell}r^{\ell} + \frac{B_{\ell}}{r^{\ell+1}}\right)P_{\ell}(\cos\theta)$$
- Assim, da *2ª* condição de fronteira temos:
$$\begin{align*}
V(R,\theta)=0 ~~\to~~ A_{\ell}R^{\ell}+ \frac{B_{\ell}}{R^{\ell+1}}&= 0\\
B_{\ell}&= - A_{\ell} R^{2\ell+1}
\end{align*}$$
e fica:
$$V(r,\theta)=\sum\limits_{\ell=0}^{\infty} A_{\ell}\left(r^{\ell} - \frac{R^{2\ell+1}}{r^{\ell+1}} \right) P_{\ell}(\cos\theta) $$

Da *1ª* condição de fronteira obtemos então:
$$r\to\infty \Rightarrow V(r,\theta)\to - E_{0}r\cos\theta+C$$
Ora, como $r\to\infty$ então $\frac{R^{2\ell+1}}{r^{\ell+1}}\to0$ e ficamos com:
$$\sum\limits A_{\ell}r^{\ell} P_{\ell}(\cos\theta)=-E_{0}r\cos\theta+C$$
Ora, vemos que do sumatorio apenas temos 2 termos: $\ell=0,\ell=1$. Assim é necessário que:
$$\begin{cases}
A_{0} = C \\
A_{1} = -E_{0} \\
A_{\ell} = 0 ~~,~~\ell>1
\end{cases}$$
(recordando que $P_{1}(\cos\theta)=\cos\theta$ )

- E podemos escrever a solução da equação de Laplace:
$$V(r,\theta)= C\left(1- \frac{R}{r}\right) - E_{0} \left( r - \frac{R^{3}}{r^{2}} \right)\cos\theta$$
em que $C=0$ se o condutor for neutro / sem carga na superfície.

- Consideremos portanto que o condutor em estudo é neutro. Temos: $$\begin{align*}
V(r,\theta)&= -E_{0} \left(r-\frac{R^{3}}{r^{2}}\right)\cos\theta \\
&= -E_{0}r\cos\theta + E_{0} \frac{R^{3}}{r^{2}}\cos\theta
\end{align*}$$
- Ora, o 1º termo é o potencial devido ao campo externo. O 2º termo é devido a densidades de carga na superfície.

> NOTA : Notar aqui a diferença entre *neutro* e *sem densidades de carga na superfície*. Ao tornar $C=0$ assumimos que o condutor é neutro, ou seja, **antes de haver campo** não tinha qualquer carga na superfície. Na solução da eq de Laplace obtivemos um termo que indica o potencial gerado por densidades de carga na superfície; estas devem-se ao campo externo.

- Vejamos então a densidade de carga induzida:
$$\begin{align*}
\sigma(\theta)&= \varepsilon_{0} (\vec{E}^{+}\cdot \hat{n} - \vec{E}^{-}\cdot \hat{n})\\
&= \varepsilon_{0}(\vec{E}^{+}\cdot \hat{r})= - \varepsilon_{0} (\nabla V)^{+} \cdot \hat{r}\\
&= -\varepsilon_{0} \left(\frac{\partial V}{\partial n}\right)^{+}= -\varepsilon_{0} \left(\frac{\partial V}{\partial r}\hat{r} \right)\cdot \hat{r}\\
&= \varepsilon_{0} \left( E_{0} + 2 \frac{R^{3}}{r^{2}}E_{0} \right)_{r=R} \cos\theta\\
&= 3 \varepsilon_{0}E_{0}\cos\theta
\end{align*}$$
Ora, isto faz sentido. Temos densidade de carga positiva para $\theta<\frac{\pi}{2}$ e negativa em caso contrário. 

# Expansão Multipolar
- Distribuição de carga numa região de comprimento caraterístico $R$ com carga total $Q_{total}$. Tem a caraterística que para $r\gg R$ a distribuição comporta-se de forma pontual ou seja: $V(\vec{r})\simeq \frac{Q_{total}}{4\pi\varepsilon_{0}r} + O(\frac{1}{r^{2}})$
- Vejamos então os casos em que $Q_{total}=0$.

## Distribuição Discreta de Carga
### Dipolo
![[dipolo.png]]
- Temos:
$$V(\vec{r})= \frac{q}{4\pi\varepsilon_{0}} \left(\frac{1}{r_{+}}- \frac{1}{r_{-}} \right)$$
- Podemos escrever:
$$\begin{align*}
\vec{r}_{\pm} \pm \frac{d}{2}\hat{z}&= \vec{r}\\
\vec{r}_{\pm} &= \vec{r} \mp \frac{d}{2} \hat{z}\\
\end{align*}$$
e daí tem-se:
$$\begin{align*}
r_{\pm}^{2}&= \vec{r}_{\pm}\cdot \vec{r}_{\pm}= \left(\vec{r} \mp \frac{d}{2} \hat{z}\right)\cdot \left(\vec{r} \mp \frac{d}{2} \hat{z}\right)\\
&= r^{2} + \frac{d^{2}}{4} \mp d~\vec{r}\cdot \hat{z}= r^{2}+ \frac{d^{2}}{4}\mp dr\cos\theta\\
&= r^{2}\left(1+ \frac{d^{2}}{4r^{2}} \mp \frac{d}{r}\cos\theta\right)
\end{align*}$$

- Por outro lado temos:
$$\frac{1}{r_{\pm}} = \frac{1}{r} \left( 1 \mp \frac{d}{r}\cos\theta + \frac{d^{2}}{4r^{2}}\right)^\frac{-1}{2}$$

ao fazer a expansão em série de Taylor de $\frac{1}{\sqrt{1\pm\alpha}}$:
$$\frac{1}{\sqrt{1\pm\varepsilon}}=(1\pm\varepsilon)^{\frac{-1}{2}}\to (1\pm\varepsilon)^{\alpha}\sim 1\pm \alpha\varepsilon+ O(\varepsilon^{2})$$
e temos:
$$\frac{1}{r_{\pm}}\approx \frac{1}{r} \left( 1 \pm \frac{d}{2r}\cos\theta\right) $$
(eliminamos os termos a partir de $\varepsilon^{2}$ porque $|\varepsilon|=\left|\frac{d}{r}\right|\ll1$ )

- Com a definição de $\frac{1}{r_{\pm}}$ acima podemos escrever:
$$\frac{1}{r_{+}}- \frac{1}{r_{-}}=\frac{d}{r^{2}} \cos\theta $$
o que nos dá:
$$V(\vec{r})=\frac{qd\cos\theta}{4\pi\varepsilon_{0}r^{2}}$$
e podemos escrever:
$$V(\vec{r})= \frac{1}{4\pi\varepsilon_{0}}\left( \frac{qd\cos\theta}{r^{2}} \right)= \frac{1}{4\pi\varepsilon_{0}} \left( \frac{q\vec{d}\cdot\vec{r}}{r^{2}}\right)=\frac{\vec{p}}{4\pi\varepsilon_{0}r^{3}}\cdot\hat{r}$$
E temos então o **momento dipolar elétrico** $\vec{p}=q \vec{d}$

## Distribuição Contínua de Carga
- Vejamos um caso geral de distribuição de carga contínua:
![[dipolo dist continua.png]]
em que temos:
$$V(\vec{r})=\frac{1}{4\pi\varepsilon_{0}} \int \frac{\rho(\vec{r'})d^{3}r'}{|\vec{r}-\vec{r'}|}$$
e podemos escrever:
$$|\vec{r}-\vec{r'}|^{2}=(\vec{r}-\vec{r'})\cdot(\vec{r}-\vec{r'})=r^{2}+r'^{2} - 2rr'\cos\theta'= r^{2}\left( 1-2 \frac{r'}{r}\cos\theta'+ \left(\frac{r'}{r} \right)^{2} \right)$$
logo $$|\vec{r}-\vec{r'}|=r \sqrt{1 - 2 \frac{r'}{r} \cos\theta' + \left(\frac{r'}{r} \right)^{2}}=r \sqrt{1 + \frac{r'}{r}\left( \frac{r'}{r} - 2\cos\theta' \right)}=r \sqrt{1+\varepsilon}$$
em que $\varepsilon=\frac{r'}{r}\left( \frac{r'}{r} - 2\cos\theta' \right)$

- Ora, no integral temos o inverso disto, logo fazemos expansão em série de Taylor:
$$\begin{align*}
\frac{1}{|\vec{r}-\vec{r'}|}&= \frac{1}{r} (1+\varepsilon)^{\frac{-1}{2}} \stackrel{(Taylor)}{=} \frac{1}{r} \left(1- \frac{\varepsilon}{2} + \frac{3}{8}\varepsilon^{2} - \frac{5}{16}\varepsilon^{3}+\dots \right)\\
&= \frac{1}{r} \left(1+ \frac{r'}{r}\cos\theta' +  \left(\frac{r'}{r}\right)^{2} \left(\frac{3\cos^{2}\theta'-1}{2} \right) + \left(\frac{r'}{r}\right)^{3} \left(\frac{r\cos^{3}\theta'-3\cos\theta'}{2} \right) \right)\\
&= \frac{1}{r} \sum\limits_{n=0}^{\infty}\left(\frac{r'}{r}\right)^{n} P_{n}(\cos\theta')
\end{align*}$$

- Ficamos então com:
$$V(\vec{r})= \frac{1}{4\pi\varepsilon_{0}}\sum\limits_{n=0}^{\infty} \frac{1}{r^{n+1}} \int (r')^{n} P_{n}(\cos\theta')\rho(\vec{r'}) d^{3}r'$$
sendo esta a **expansão multipolo** do potencial. Temos vários tipos de multipolos:
![[multipolos.png]]

### Monopolo
- Consiste em ter $n=0$ pelo que resulta $$V_{monopolo}= \frac{Q}{4\pi\varepsilon_{0}r}$$
que é o potencial de uma carga pontual, algo que faz sentido.

### Dipolo
- Consideramos $n=1$ e obtemos:
$$\begin{align*}
V_{dipolo}&= \frac{1}{4\pi\varepsilon_{0}r^{2}} \int r' P_{1}(\cos\theta') \rho(\vec{r'})
 d^{3}r'= \frac{1}{4\pi\varepsilon_{0}r^{2}} \int r' \cos\theta' \rho(\vec{r'}) d^{3}r'\\
&= \frac{1}{4\pi\varepsilon_{0}r^{3}} \int (\vec{r}\cdot\vec{r'})\rho(\vec{r'})d^{3}r' = \frac{\vec{r}\cdot\int \vec{r'}\rho(\vec{r'}) d^{3}r'}{4\pi\varepsilon_{0}r^{3}}\\
&= \frac{\vec{p}\cdot \vec{r}}{4\pi\varepsilon_{0}r^{3}} = \frac{p\cos\theta}{4\pi\varepsilon_{0}r^{2}} 
\end{align*}$$
em que temos $\vec{p}=\text{momento dipolar elétrico}=\int \vec{r'}\rho(\vec{r'})d^{3}r'=\int \vec{r'} dq(\vec{r'})$

- Ora, o momento dipolar elétrico numa densidade de carga contínua:
    - Depende do tamanho, forma e densidade de carga em si
    - É definido relativamente a um ponto de origem
    - Se $Q_{total}=0$ o momento dipolar elétrico é independente da origem

![[coordenadas esféricas 2.png]]

- Vamos então determinar o campo elétrico associado ao dipolo (continuando a usar coordenadas esféricas independentes de $\varphi$):
$$\begin{align*}
\vec{E}_{dipolo}&= - \nabla V_{dipolo}= - \left(\frac{\partial V_{dipolo}}{\partial r}\hat{r} + \frac{1}{r} \frac{\partial V_{dipolo}}{\partial\theta}\hat{\theta} \right)\\
&= \frac{2p\cos\theta}{4\pi\varepsilon_{0}r^{3}}\hat{r} + \frac{1}{r} \frac{p\sin\theta}{4\pi\varepsilon_{0}r^{2}}\hat{\theta}\\
&= \frac{3p\cos\theta}{4\pi\varepsilon_{0}r^{3}}\hat{r} - \frac{p\cos\theta}{4\pi\varepsilon_{0}r^{3}}\hat{r} + \frac{p\sin\theta}{4\pi\varepsilon_{0}r^{3}}\hat{\theta}\\
&= \frac{3p\cos\theta}{4\pi\varepsilon_{0}r^{3}}\hat{r} - \frac{p}{4\pi\varepsilon_{0}r^{3}} \underbrace{\left( -\cos\theta\hat{r}+\sin\theta\hat{\theta}\right)}_{=-\hat{z}}\\
&= \frac{1}{4\pi\varepsilon_{0}r^{3}}(3(\vec{p}\cdot\hat{r})\hat{r}-\vec{p})
\end{align*}$$
sendo que temos
![[Attachments/FCUP/A3S1/EM2/dipolo real e teorico.png]]