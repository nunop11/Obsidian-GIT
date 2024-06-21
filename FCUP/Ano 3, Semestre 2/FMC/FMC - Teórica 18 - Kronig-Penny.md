###### Aula 18 - 2/5/2024
%% - Consideremos as ondas planas $\psi_{\vec{q}},\psi_{\vec{q}-\vec{K}}$ correspondentes a sistemas *não perturbados*. Com elas, podemos escrever qualquer função perturbada: $$\Psi(\vec{r})=c_{\vec{q}}\psi_{\vec{q}} + c_{\vec{k}-\vec{K}}\psi_{\vec{q}-\vec{K}}$$
- Na aula passada supostamente fizemos isto, mas esta equação em combinação com a equação Central dá-nos:
$$(\varepsilon-\varepsilon_{\vec{q}}^{0})c_{\vec{q}}=V_{\vec{K}}c_{\vec{q}-\vec{K}} \quad \quad;\quad \quad (\varepsilon-\varepsilon_{\vec{q}-\vec{K}}^{0})c_{\vec{q}-\vec{K}}=V_{-\vec{K}}c_{\vec q}$$
Em termos matriciais, estas equações dão:
$$\begin{vmatrix}\varepsilon-\varepsilon_{\vec{q}}^{0} & -V_\vec{K} \\ -V_{\vec{K}}^{*} & \varepsilon-\varepsilon_{\vec{q}-\vec{K}}^{0}\end{vmatrix}=0$$


**Hamiltoniano Matriz**
- Podemos escrever o elemento da amtriz como:
$$\bra{\vec{q}}H\ket{\vec{q}}=\bra{\vec{q}}H_{0}\ket{\vec{q}} + \bra{\vec{q}}V\ket{\vec{ q}}$$
- Assim, como $V(x)=\sum_{\vec{K}}V_{\vec{K}}e^{i Kx}$ temos $\bra{\vec{q}}V\ket{\vec{q}}=\int \Psi_{\vec{q}}^{*} V(x)\Psi_{\vec{q}}dx=\frac{1}{L} \int e^{-iqx}V(x)e^{iqx}dx=\frac{1}{L}\int V(x)dx=0$.
- Além disso, temos que $\bra{\vec{q}}H_{0}\ket{\vec{q}}=\varepsilon^{0}_{\vec{q}}$. Como o sistema é periódico com $\vec{K}$, teremos: 
$$H = \begin{pmatrix}\varepsilon_{\vec{q}}^{0} & ? \\  ? & \varepsilon_{\vec{q}-\vec{K}}^{0}\end{pmatrix}$$


- Vejamos agora os termos das diagonais:
$$\begin{align*}
\bra{\vec{q}}V\ket{\vec{q}-\vec{K}}&= \int \Psi_{\vec{q}}^{*}V(x)\Psi_{\vec{q}-\vec{K}}dx\\
&= \int \frac{1}{\sqrt{L}}e^{-iqx}V(x) \frac{1}{\sqrt{L}}e^{i\left(q- \frac{2\pi}{a}\right)x}\\
&= \frac{1}{L}\int V(x) e^{-i\frac{2\pi}{a}x}\\
&= \frac{1}{L}\int \sum\limits_{\vec{K}}V_{\vec{K}}e^{i (K- \frac{2\pi}{a})x}
\end{align*}$$
- Ora, quando $K=\frac{2\pi}{a}$, o somatório fica apenas $V_{K}$. Como temos periodicidade iremos ter sempre isto em $\vec{q}-\vec{K}$ e temos:
$$H = \begin{pmatrix}\varepsilon_{\vec{q}}^{0} & -V_{\vec{K}} \\  -V_{\vec{K}}^{*} & \varepsilon_{\vec{q}-\vec{K}}^{0}\end{pmatrix}$$
(não sei de onde vem o sinal negativo nos $V$s)
- Verificamos que se fizermos $H-I\varepsilon$ ficamos exatamente com a mesma matriz que obtivemos na aula anterior com a equação Central.

- Daqui (???) podemos obter:
$$\varepsilon=\frac{\varepsilon_{\vec{q}}^{0}+\varepsilon_{\vec{q}-\vec{K}}^{0}}{2} \pm \left[\left(\frac{\varepsilon_{\vec{q}}^{0}- \varepsilon_{\vec{q}-\vec{K}}^{0}}{2}\right)^{2} + |V_{\vec{K}}|^{2}\right]^{\frac{1}{2}}$$

### $q=\frac{\pi}{a}$
- Da teoria de perturbações resulta $\varepsilon\left(\frac{\pi}{a}\right)=\varepsilon_{q= \frac{\pi}{a}}\pm |V_{\vec{K}}|$ (?????????)
- Isto permite (?) obter $$c_{\vec{q}}=\pm \frac{V_{\vec{K}}}{|V_{\vec{K}}|}c_{\vec{q}-\vec{K}}$$
e daqui podemos obter:
$$\Psi_{+}(\vec{r})\propto \cos\left(\frac{\vec{k}\cdot\vec{r}}{2}\right) \quad \quad;\quad \quad \Psi_{-}(\vec{r})\propto \sin\left(\frac{\vec{k}\cdot\vec{r}}{2}\right)$$

### $q$ perto de $\frac{\pi}{a}$
??????????????
 %%
# Modelo de Kronig-Penney
- Temos:
![[kronig penney.png]]
- A equação de Schrödinger tem a forma:
$$- \frac{\hbar^{2}}{2m}\frac{d^{2}\Psi}{dx^{2}} + V(x)\Psi = \varepsilon \Psi$$
logo
$$\frac{d^{2}\Psi}{dx^{2}}+ \frac{2m}{\hbar^{2}}(\varepsilon-V(x))\Psi=0$$
- Vamos assumir soluções do tipo $\Psi(x)=e^{ikx}u(x)$. 
- A 2ª derivada fica: $\frac{d^{2}\Psi}{dx^{2}}=\left(-k^{2}u(x)+2ik \frac{du}{dx}+ \frac{d^{2}u}{dx^{2}}\right)e^{ikx}$
- A equação fica:
$$\frac{d^{2}u}{dx^{2}}+ 2ik \frac{du}{dx} + \left[-k^{2} + \frac{2m}{\hbar^{2}}(V(x)-\varepsilon)\right]u(x)=0$$

### $-b\le x\le 0$
- Agora, nas barreiras de potencial temos $V(x)=V_{0}$. Daqui resulta:
$$\frac{d^{2}u}{dx^{2}}+ 2ik \frac{du}{dx} + \left[-k^{2} + \gamma^{2}\right]u(x)=0$$
em que definimos $\gamma^{2}=\frac{2m}{\hbar^{2}}(V_{0}-\varepsilon)$

- Podemos então resolver a equação diferencial e obtemos:
$$u(x)= A e^{(-ik+\gamma)x} + Be^{(-ik-\gamma)x}$$

### $0\le x\le a$
- Agora temos potencial nulo. Daqui simplesmente surge:
$$\frac{d^{2}u}{dx^{2}}+ 2ik \frac{du}{dx} + \left[-k^{2} - \beta^{2}\right]u(x)=0$$
em que definimos $\beta= \frac{2m}{\hbar^{2}}\varepsilon$

- Daqui temos a solução $$u(x) = C e^{i(-k+\beta)x}+D e^{i(-k-\beta)x}$$

### CF
- Temos então as seguintes 4 condições de fronteira:
$$\Psi(a) \quad;\quad \Psi(0) \quad;\quad \Psi'(a) \quad;\quad \Psi'(0)$$
- Com estas iremos obter **4 eqs lineares em A,B,C,D**!
- Isto é algo que já fizemos várias vezes.
- Obtemos:
$$\frac{\gamma^{2}-\beta^{2}}{2\beta\gamma}\sinh \gamma b \sin \beta a + b\cosh \gamma \cos \beta a = \cos(k(a+b))$$
- Consoante $b\to0~,~V_{0}\to\infty$ temos que ter $\gamma^{2}b$ finito, com: $$\lim\limits_{\substack{b\to0\\V_{0}\to\infty}}\frac{\gamma^{2}ab}{2}=P$$
- Neste caso temos ainda que a equação acima fica na forma:
$$\underbrace{P \frac{\sin \beta a}{\beta a} + \cos \beta a}_f=\cos ka$$
- Se representarmos $f(ka)$ teremos a forma de uma onda sinusoidal que vai diminuindo amplitude (seno cardinal). Ora, em alguns intervalos teremos uma amplitude $f(ka)>1$. Ora, a equação $f(ka)=\cos ka$  não terá solução nesse intervalo, ou seja, temos uma **zona proibída**! Assim, este modelo explica bandas proibidas usando um modelo muito mais simples.