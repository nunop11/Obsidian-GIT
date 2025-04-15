**Eletromagnetic Wave in Dieletric**
Let's consider a eletromagnetic wave propagation through a dieletric material. Then, we have: $$|\textbf{B}_\text{wave}|=\frac{n}{c}|\textbf{E}_\text{wave}|$$
so, considering that $n$ is the refractive index of the material, $|\textbf{B}|\ll|\textbf{E}|$ and we usually can simply ignore this component of the wave.

Let's then consider that the wave is propagating in the $z$ direction and we have an external magnetic field $\mathbf{B}_{ext}$ also in the $z$ direction. This means that the electric field oscillates in the $xOy$ plane. As the wave propagates, it interacts with the electrons of the material's atoms. Each electron will be subject to a force $\textbf{f}$:
$$\textbf{f}=e(\textbf{E}+\textbf{v}\times \mathbf{B})$$
where $\mathbf{B}=\mathbf{B}_{ext}$.

**Motion of electron**
So, as an electron interacts with these forces it will oscillate in the $xOy$ plane. Then, we can write its equation of motion, where $s$ is the electron's distance from the equilibrium position:
$$m \ddot{\mathbf{s}}+ f \mathbf{s}=-e (\mathbf{E} + \dot{\mathbf{s}}\times \mathbf{B})$$
and $f$ is a restoring force constant which can be written in terms of the system's natural oscillation frequency: $f=m \omega_{0}^{2}$
 
which we can divide in the $x$ and $y$ components:
$$\begin{cases}
m \ddot{s}_{x} + f s_{x}=-eE_{x} - eB \dot{s}_{y} \\
m \ddot{s}_{y} + f s_{y}=-eE_{y} + eB \dot{s}_{x}
\end{cases}$$
Next, considering that the we can define the evolution of the position as $\mathbf{s}(t)=\mathbf{s}_{0}e^{-i\omega t}$, we can rewrite as:
$$\begin{cases}
(-m\omega^{2} + f)s_{x}- i\omega eBs_{y}=-eE_{x} \\
(-m\omega^{2} + f)s_{y}+ i\omega eBs_{x}=-eE_{y}
\end{cases}$$
which we can simplify as:
$$\begin{cases}
(\omega_{0}^{2}-\omega^{2})s_{x}-i \omega \Omega s_{y}=- \frac{e}{m}E_{x} \\
(\omega_{0}^{2}-\omega^{2})s_{y}+i \omega \Omega s_{x}=- \frac{e}{m}E_{y}
\end{cases}$$
where $\Omega=\frac{eB}{m}$ is the electron cyclotron frequency.

We can now define: 
$$E_{\pm}=E_{x}\pm i E_{y} \quad;\quad s_{\pm}=s_{x}\pm i s_{y}$$
and we can rewrite the system of equations as:
$$\begin{cases}
(\omega_{0}^{2}-\omega^{2}-\omega\Omega)s_{+}= -\frac{e}{m} E_{+} \\
(\omega_{0}^{2}-\omega^{2}+\omega\Omega)s_{-}= -\frac{e}{m} E_{-}
\end{cases}$$

**Polarization vector**
The polarization vector can be written as: $\mathbf{P}=-Ne \mathbf{s}$, where $N$ is the volume electron density of the dieletric material.
We can apply the same transformation as above:
$$P_{\pm}=P_{s}\pm i P_{y}=Ne (s_{x}\pm is_{y})=Ne s_{\pm}$$
and we have:
$$P_{\pm}=\frac{\frac{Ne^{2}}{m}E_{\pm}}{\omega_{0}^{2}-\omega^{2}-\omega\mp \Omega}$$
here, the $+$ component will correspond to a left-hand circularly polarized wave, while the $-$ corresponds to a right-hand circularly polarized

**Refraction index**
We can finally write the refraction index in the left and right had direction:
$$n_{\pm}^{2}=1+\frac{P_{\pm}}{\varepsilon_{0}E_{\pm}}=1+\frac{\frac{Ne^{2}}{\varepsilon_{0}m}}{\omega_{0}^{2}-\omega^{2}\mp \omega\Omega}$$
As we saw above, $\Omega=\frac{eB}{m}$. Then, if there is no external magnetic field applied in the $z$ direction, we get $n_{+}=n_{-}=n$. If we have a magnetic field $B>0$ then $n_{+}>n_{-}$. This means that the left-hand polarized component will propagate with a smaller phase velocity than the right-hand polarized component.

**Electric Field**
We can write the equation that defines the electric field for the left and right polarized components as:
$$\begin{cases}
E_{x}^{\pm}= E_{0}\cos \left( \frac{\omega}{c} (n_{\pm}z - ct) \right) \\
E_{y}^{\pm}= \pm E_{0}\cos \left( \frac{\omega}{c} (n_{\pm}z - ct) \right)
\end{cases}$$
We can then define the total electric field from the polarization components: $E_{x}=E_{x}^{+}+E_{x}^{-}$ and $E_{y}=E_{y}^{+}+E_{y}^{-}$.
    - We can easily see that if there's no magnetic field and $n_{+}=n_{-}$ we get $E_{y}=0$ and $E_{x}=2E_{0}\cos( \frac{\omega}{c}(nz-ct))$ 
    - However, if $B\neq0$ we get: 
$$\begin{cases}
E_{x}= 2E_{0}\cos \left[\frac{\omega}{c}\left(\frac{n_{+}+n_{-}}{2}z-ct\right) \right]\cos \left[\frac{\omega}{c}\frac{n_{+}-n_{-}}{2} z\right] \\
E_{y}= 2E_{0}\cos \left[\frac{\omega}{c}\left(\frac{n_{+}+n_{-}}{2}z-ct\right) \right]\sin \left[\frac{\omega}{c}\frac{n_{+}-n_{-}}{2} z\right]
\end{cases}$$

**Polarization angle**
We can calculate the polarization angle (relative to the $x$ axis) the following way:
$$\phi=\tan^{-1}\left(\frac{E_{y}}{E_{x}}\right)=\frac{\omega}{2c}(n_{+}-n_{-})z$$
which we can expand:
$$\phi=\frac{\omega}{2c} \frac{Ne^{2}}{m} \frac{\omega\Omega}{(\omega_{0}^{2}-\omega^{2})^{2}-(\omega\Omega)^{2}}z$$

The cyclotron frequency for an electron will be in the order of Gigahertz. If the system is oscillating at a frequency $\omega$ of at least 100 kHz, we have $\omega^{2}\gg \Omega \omega$ and therefore we can ignore the cyclotron frequency term of the denominator. We then get:
$$\phi= \frac{Ne^{3}}{2cm^{2}}\frac{\omega^{2}}{(\omega_{0}^{2}-\omega^{2})^{2}} \cdot B \cdot z$$
We can already see that this is equivalent do Becquerel's equation! Then, we can see that:
$$V = \frac{Ne^{3}}{2cm^{2}} \frac{\omega^{2}}{(\omega_{0}^{2}-\omega^{2})^{2}}$$

**Verdet constant and wavelength**
We can define the refractive index as $n=\frac{1}{2}(n_{+} + n_{-})$. Using the Taylor series expansion $\sqrt{1+x}\simeq 1 + \frac{1}{2}x$, we can derive:
$$n=1 + \frac{Ne^{2}}{2m} \frac{1}{\omega_{0}^{2}-\omega^{2}}$$
We can write: $\omega=2\pi f=2\pi c/\lambda$. Using this, we can differentiate $n$ relative to $\lambda$:
$$\begin{align*}
\frac{dn}{d\lambda}&= \frac{Ne^{2}}{2m} \frac{d}{d\lambda} \left( \frac{1}{\omega_{0}^{2}- \frac{4\pi^{2}c^{2}}{\lambda^{2}}} \right)\\
&= \frac{Ne^{2}}{2m} \frac{d}{d\lambda} \left(\frac{\lambda^{2}}{\lambda^{2}\omega_{0}^{2}-4\pi^{2}c^{2}}\right)\\
&= \frac{Ne^{2}}{m} \frac{4\pi c^{2}\lambda^{2}}{\lambda^{2}\omega_{0}^{2}-4\pi ^{2}c^{2}}\\
&= \frac{Ne^{2}}{m} \frac{1}{\lambda}\frac{\omega^{2}}{(\omega_{0}^{2}-\omega^{2})^{2}}
\end{align*}$$
Finally, using this, we can write another equation for the Verdet constant:
$$V=\frac{e}{2mc} \lambda \frac{dn}{d\lambda}$$

