# ex.1
$$F(\theta)=A e^{-(6\theta/\pi)^{2}}\sin(\Omega t) mg \hat{u_{\theta}}$$
## 1.
### a)
$$\Omega=0.5, v_{0}=0, \theta_{0}=0$$

- A equação do movimento da massa é, pela 2ª lei de newton:
$$\begin{align*}
ma &= \sum F\\
m \frac{d^{2}\vec{r}}{dt^{2}} &= F(\theta) + P\\
\frac{d^{2}\vec{r}}{dt^{2}}&= \frac{1}{m} (A e^{-(6\theta/\pi)^{2}}\sin(\Omega t) mg\hat{u_\theta} + \vec{P} + \vec{T})\\
\end{align*}$$
Podemos decompor o peso em $\hat{u_\theta}$ e $\hat{u_{r}}$, sendo estas as direções, respetivamente, do ângulo e do fio. Temos:
$$\vec{P}=P\sin \theta \hat{u}_{\theta}+ P \cos\theta \hat{u}_{r}$$
- Ora, $r$, a distância entre o CM da masa e o ponto de suspensão do fio, deverá ser $\ell$, que será constante. Assim, na direção $\hat{u}_{r}$, o Peso e a Tensão têm de ser anular. Ou seja:
$$P_{r}=T_{r}\to mg\cos\theta=-T$$
- Como esta força só existe na direção do fio ($\hat{u_{r}}$), temos que a força total aplicada em $r$ é 0 e que na direção $\theta$ apenas temos o peso e a força $F$.
, logo, podemos dividir a equação domovimento em $\theta$ e $r$ e temos:
$$\frac{d^{2}\theta}{dt^{2}}=A e^{-(6\theta/\pi)^{2}}\sin(\Omega t)g - g\sin\theta$$
$$\frac{d^{2}r}{dt^{2}}= 0$$
- Podemos dividir num sistema de 2 equações diferenciais de 1ª ordem:
$$\begin{cases}
\frac{d\theta}{dt}=v_{\theta} \\
\frac{dv_{\theta}}{dt}=A e^{-(6\theta/\pi)^{2}}\sin(\Omega t)g - g\sin\theta \\
\end{cases}$$

- Além de mais, ao expressar isto em unidades $\sqrt{\frac{\ell}{g}}$, temos: $$\sqrt{\frac{\ell}{g}}=1\to \frac{\ell}{g}=1 \to \ell=g$$

### b)
- O teorema da energia cinética diz-nos que: $$W_{R}=\Delta E_{c}$$
- Ora, facilmente calculamos a variação da energia cinética:
$$\Delta E_{c}=E_{c}(f) - E_{c}(0)=E_{c}(f)$$
uma vez que a massa começa em repouso.
- Agora, o trabalho das forças:
    - Trabalho do Peso: $$W_{P}=\int_{0}^{1000} \vec{P}\cdot \vec{v}~dt = \int_{0}^{1000} mgv\cos(\frac{\pi}{2}-\theta)=mg\int_{0}^{1000}v_\theta\sin \theta dt$$
    - Trabalho da Força Externa: $$W_{F}=\int_{0}^{1000}\vec{F}\cdot \vec{v}dt = \int_{0}^{1000}v_{\theta}F(\theta)~dt$$

### c)


## 2.


## 3.
- Vimos na alínea 1. que $$T = -P\cos \theta = -mg\cos \theta$$
Ou seja, sabemos que o fio rebenta quano $T=1.3mg$. Igualando as 2 equações:
$$1.3mg = -mg \cos \theta\to \cos \theta = -1.3$$
- Por palavras, o fio irá rebentar no primeiro instante em que $\cos \theta=-1.3$

# EX.2
- Temos que:
$$\begin{align*}
V(r) &= \frac{1}{4\pi\varepsilon_{0}} \int \sigma(\theta)\log \left(\frac{|r'|^{2}}{|r'-r|^{2}}\right)ds'\\
V(r) &= \frac{ca}{\varepsilon_{0}} \frac{1}{4\pi} \int_\frac{-\pi}{6}^{\frac{\pi}{6}} \theta^{2} \int_{0}^{64}\log\left(\frac{|r'|^{2}}{|r'-r|^{2}}\right)dr' d\theta
\end{align*}$$

- Como $\sigma(\theta)$ é apenas definida no intervalo $\frac{-\pi}{6}< \theta \frac{\pi}{6}$, sendo $\vec{r}(R, \theta)=(x,y)$ um ponto da região de controlo, para os pontos da região de controlo em que $x<16$ ou em que $|\theta|>\frac{\pi}{6}$, temos que $\sigma(\theta)=0$, ou seja, não há potencial.

- Assim, os pontos da região de controlo em que termos carga induzida são dados por:
$$\vec{r}(R, \theta)\to (16, y)$$
Ora, temos que $y=R\sin \theta$ e que $R=\sqrt{x^{2}+y^{2}}=\sqrt{16^{2}+y^{2}}$. Assim: 
$$\begin{align*}
y &=  \sqrt{16^{2}+y^{2}}\cos \theta\\
y^{2} &= (16^{2}+y^{2})\cos^{2}\theta\\
y &= \sqrt{\frac{16^{2}\cos^{2}\theta}{1-\cos^{2}\theta}} = 16\arctan(\theta)
\end{align*}$$
- Assim, os pontos da região de controlo em que temos potencial não nulo são dados por:
$$(16, 16\arctan(\theta))\to (16\sqrt{1+\arctan^{2}\theta}, \theta)$$


- A partir de $$V(r) = \frac{ca}{\varepsilon_{0}} \frac{1}{4\pi} \int_\frac{-\pi}{6}^{\frac{\pi}{6}} \theta^{2} \int_{0}^{64}\log\left(\frac{|r'|^{2}}{|r'-r|^{2}}\right)dr' d\theta$$
podemos escrever:
$$F(r,\theta)=\theta^{2} \int_{0}^{64} \log\left(\frac{|r'|^{2}}{|r'-r|^{2}}\right)dr'$$
$$V(r) = \frac{1}{4\pi} \int_{\frac{-\pi}{6}}^{\frac{\pi}{6}} F(r, \theta) d \theta$$
