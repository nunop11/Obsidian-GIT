- Temos:
$$I\ddot{\theta}=mgh\sin\theta+ \frac{mhv^{2}}{r}\cos\theta + \tau$$
### Ponto Eq
- Fazemos:
$$\begin{align*}
0&= mgh\sin\theta+ \frac{mhv^{2}}{r}\cos\theta\\
g\sin\theta&= \frac{-v^{2}}{r}\cos\theta\\
\tan\theta&= \frac{-v^{2}}{gr}\\
\theta_{0}&= \tan^{-1}\left(\frac{-v^{2}}{gr}\right)
\end{align*}$$
- O controlador da 4. não funciona porque agora o sistema não estabiliza em 0.

### Controlador novo
- Podemos expandir em taylor em torno de $\theta_{0}$:
$$\begin{align*}
\sin\theta&= \sin\theta_{0} + \cos\theta_{0}(\theta-\theta_{0})\\
\cos\theta&= \cos\theta_{0}-\sin\theta_{0}(\theta-\theta_{0})
\end{align*}$$
logo:
$$\begin{align*}
I\ddot{\theta}&= mgh\sin\theta_{0} + mgh\cos\theta_{0}(\theta-\theta_{0}) + \frac{mv^{2}h}{r}\cos\theta_{0}- \frac{mv^{2}h}{r}\sin\theta_{0}(\theta-\theta_{0}) + \tau\\
&= \theta \left(mgh\cos\theta_{0} - \frac{mv^{2}h}{r}\sin\theta_{0} \right) + \left[mgh(\sin\theta_{0} - \theta_{0}\cos \theta_{0}) + \frac{mv^{2}h}{r}(\cos\theta_{0} + \theta_{0}\sin\theta_{0}) \right] + \tau\\
\ddot{\theta}&= \frac{\alpha}{I}\theta + \frac{\tau+\beta}{I}\\
\end{align*}$$
podemos definir a entrada de outra forma:
$$\ddot{\theta}= \frac{\alpha}{I}\theta+\tilde{u}~~~~;~~~~ \tilde{u}=\frac{u+\beta}{I}$$
logo:
$$\dot{x} = \begin{pmatrix}0 & 1 \\ \frac{\alpha}{I} & 0\end{pmatrix}x + \begin{pmatrix}0 \\ 1\end{pmatrix}\tilde{u} \quad \quad;\quad \quad y=\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}x$$

### Condições
- Temos:
$$M=\exp\left(-\frac{\pi\xi}{\sqrt{1-\xi^{2}}}\right)~~~~;~~~~ t_{s(2\%)}=\frac{4}{\xi\omega_{n}}~~,~~ t_{s(5\%)}=\frac{3}{\xi\omega_{n}}$$
o que nos permite calcular
$$\xi=\sqrt{\frac{\ln (\frac{1}{0.05})^{2}}{\pi^{2}+\ln (\frac{1}{0.05})^{2}}}\quad;\quad \omega_{n}=\frac{2}{\xi}$$
- Teremos então o caso de feedback em que:
$$u=-Kx~~\to~~ \tilde{u}=\frac{-Kx+\beta}{I}$$

### Polinómio caraterísitco
- Para estas novas matrizes $A,B$ temos:
$$A-BK=\begin{pmatrix}0 & 1 \\ \alpha/I  & 0\end{pmatrix} - \begin{pmatrix}0 \\ 1/I\end{pmatrix}\begin{pmatrix}k_{1} & k_{2}\end{pmatrix}=\begin{pmatrix}0 & 1 \\ \frac{\alpha-k_{1}}{I} & \frac{-k_{2}}{I}\end{pmatrix}$$
$$\begin{align*}
sI-(A-BK) &= \begin{pmatrix}s & -1\\
\frac{k_{1}-\alpha}{I} & s + \frac{k_{2}}{I}\end{pmatrix}
\end{align*}$$
logo
$$\det [sI-A+BK] = s^{2}+ \frac{k_{2}}{I}s + \frac{k_{1}-\alpha}{I}$$
e como sabemos isto será equivalente a $s^{2} + 2\xi \omega_{n} + \omega_{n}^{2}$. Logo:
$$\frac{k_{2}}{I}= 2\xi\omega_{n}~~\to~~ k_{2}=2I\xi\omega_{n}$$
$$\frac{k_{1}-\alpha}{I}=\omega_{n}^{2}~~\to~~ k_{1}=\alpha+I\omega_{n}^{2}$$