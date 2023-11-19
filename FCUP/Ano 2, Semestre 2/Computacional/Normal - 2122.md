## 1.a)
- As forças aplicadas no CM são:
$$\mathbf{F}_{M}=\alpha m \omega ~ \hat{e}_{x}\times \mathbf{v} \quad \quad;\quad \quad \mathbf{F}_{a}=-\gamma|\mathbf{v}|\mathbf{v} \quad \quad;\quad \quad \mathbf{F}_{g}= -mg \hat{e}_{z}$$
- Sendo que a 2ª Lei de Newton nos diz:
$$\begin{align*}
m\frac{d^{2}}{dt^{2}}\mathbf{r} &= -mg \hat{e}_{z} +\alpha m \omega ~ \hat{e}_{x}\times \frac{d}{dt}\mathbf{r} -\gamma\bigg|\tfrac{d}{dt}\mathbf{r}\bigg| \tfrac{d}{dt}\mathbf{r} 
\end{align*}$$
- As variáveis adimensionalizadas serão:
$$t*=\tau=\sqrt{\frac{m}{\gamma g}} \quad;\quad x^{*}=L=\frac{m}{\gamma}$$
E ficamos com:
$$\begin{align*}
m * \frac{1}{\tau^{2}} \frac{d^{2}}{dt^{2}}\mathbf{r} = - mg L\hat{e}_{z} + \alpha m \omega \frac{L}{\tau} \hat{e}_{x}\times \frac{d}{dt}\mathbf{r} - \gamma \frac{1}{\tau^{2}}\bigg|\tfrac{d}{dt}\mathbf{r}\bigg| \tfrac{d}{dt}\mathbf{r}\\
m\frac{d^{2}}{dt^{2}}\mathbf{r}= - mg L \tau^{2}\hat{e}_{z} + \alpha m \omega L \tau\hat{e}_{x}\times \frac{d}{dt}\mathbf{r} -\gamma\bigg|\tfrac{d}{dt}\mathbf{r}\bigg| \tfrac{d}{dt}\mathbf{r}\\
\frac{d^{2}}{dt^{2}}\mathbf{r}= - g L \tau^{2}\hat{e}_{z} + \alpha \omega L \tau\hat{e}_{x}\times \frac{d}{dt}\mathbf{r} - \frac{\gamma}{m}\bigg|\tfrac{d}{dt}\mathbf{r}\bigg| \tfrac{d}{dt}\mathbf{r}\\
\frac{1}{L}\frac{d^{2}}{dt^{2}}\mathbf{r}= - g  \tau^{2}\hat{e}_{z} + \alpha \omega \tau\hat{e}_{x}\times \frac{d}{dt}\mathbf{r} - (\frac{\gamma}{m})^{2}\bigg|\tfrac{d}{dt}\mathbf{r}\bigg| \tfrac{d}{dt}\mathbf{r}\\
\frac{1}{L}\frac{d^{2}}{dt^{2}}\mathbf{r}= - g \frac{m}{\gamma g} \hat{e}_{z} + \alpha \omega \tau\hat{e}_{x}\times \frac{d}{dt}\mathbf{r} - (\frac{\gamma}{m})^{2}\bigg|\tfrac{d}{dt}\mathbf{r}\bigg| \tfrac{d}{dt}\mathbf{r}\\
\frac{1}{L}\frac{d^{2}}{dt^{2}}\mathbf{r}= - L \hat{e}_{z} + \alpha \omega \sqrt{\frac{m}{\gamma g}}\hat{e}_{x}\times \frac{d}{dt}\mathbf{r} - (\frac{1}{L})^{2}\bigg|\tfrac{d}{dt}\mathbf{r}\bigg| \tfrac{d}{dt}\mathbf{r}
\end{align*}$$
Presumindo que $L=1$, ficamos com:
$$\frac{d^{2}}{dt^{2}}\mathbf{r} = -\hat{e}_{z} + a_{1}\hat{u}_{x}\times \frac{d}{dt}\mathbf{r} - \bigg|\tfrac{d}{dt}\mathbf{r}\bigg|\tfrac{d}{dt}\mathbf{r} \quad \quad;\quad \quad a_{1}=a \omega \sqrt{\frac{m}{\gamma g}}$$

---

## 1.b)
- Temos:
$$\frac{d^{2}}{dt^{2}}\mathbf{r} = -\hat{e}_{z} + a_{1}\hat{u}_{x}\times \frac{d}{dt}\mathbf{r} - \bigg|\tfrac{d}{dt}\mathbf{r}\bigg|\tfrac{d}{dt}\mathbf{r}$$
que podemos dividir da seguinte forma:
$$\begin{cases}
\frac{d^{2}x}{dt^{2}}= -|v_{x}|v_{x} = 0 \\
\frac{d^{2}y}{dt^{2}}=-|v_{y}|v_{y} + a_{1}v_{z} \\
\frac{d^{2}z}{dt^{2}}=-1-|v_{z}|v_{z} - a_{1} v_{y}
\end{cases}$$
Ou seja:
$$\begin{cases}
v_{y} = \frac{dy}{dt} \\
v_{z} = \frac{dz}{dt} \\
\frac{dv_{y}}{dt} = a_{1}v_{z}- v_{y} \sqrt{v_{y}^{2}+ v_{z}^{2}}\\
\frac{dv_{z}}{dt}= -1-a_{1}v_{y}-v_{z}\sqrt{v_{y}^{2}+v_{z}^{2}}
\end{cases}$$
E assim temos:
$$\begin{align*}\xi&=(y,z,v_{y},v_{z}) \\
H(\xi,t,a_{1})&=(v_{y}~,~v_{z}~,~a_{1}v_{z}-v_{y}\sqrt{v_{y}^{2}+v_{z}^{2}}~,~-1-a_{1}v_{y}-v_{z}\sqrt{v_{y}^{2}+v_{z}^{2}})\end{align*}$$

----

