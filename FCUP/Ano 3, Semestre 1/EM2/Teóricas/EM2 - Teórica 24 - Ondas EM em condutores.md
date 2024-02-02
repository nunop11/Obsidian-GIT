### Coeficientes de Reflexão e Transmissão de ondas EM
- Para uma onda a incidir no plano de incidência $z=0$ podemos definir a intensidade de incidência, reflexão e transmissão usando o vetor Poyting:
$$I_{I}=\langle \vec{S}_I\rangle\cdot \hat{z}=\frac{1}{2}\varepsilon_{1}v_{1}E_{0I}^{2}\cos\theta_{I}$$
$$I_{R}=\langle\vec{S_{R}}\rangle\cdot(-\hat{z})=\frac{1}{2}\varepsilon_{1}v_{1}E_{0R}^{2}\cos\theta_{R}$$
$$I_{T}=\langle \vec{S_{T}}\rangle\cdot\hat{z}=\frac{1}{2}\varepsilon_{2}v_{2}E_{0T}^{2}\cos\theta_{T}$$
e podemos definir os coeficientes de reflexão e transmissão:
$$R=\frac{I_{R}}{I_{I}}=\frac{E_{0R}^{2}}{E_{0I}^{2}}=\left(\frac{\alpha-\beta}{\alpha+\beta} \right)^{2}$$
$$T=\frac{I_{T}}{I_{I}}=\frac{E_{0T}^{2}}{E_{0I}^{2}}\underbrace{\frac{\cos\theta_{T}}{\cos\theta_{I}}}_{\alpha}\underbrace{\frac{\varepsilon_{2}v_{2}}{\varepsilon_{1}v_{1}}}_{\beta}=\alpha \beta \left(\frac{2}{\alpha+\beta} \right)^{2}$$
em que novamente temos $$R+T=1$$

# Ondas EM em condutores
- Desde que começamos a estudar ondas EM em matéria assumimos que $\rho_\ell=0,\vec{\mathcal{J_{\ell}}}=\vec{0}$, o que será o caso do vácuo e de meios isoladores.
- Como regra geral, num condutor temos, pela Lei de Ohm:
$$\vec{\mathcal{J_{\ell}}}=\sigma\vec{E}$$
e as equações de Maxwell ficam na forma:
$$\begin{align*}
\nabla \cdot \vec{E}&= \frac{1}{\varepsilon}\rho_{\ell}\\
\nabla \cdot \vec{B}&= 0\\
\nabla \times \vec{E}&= - \partial_{t}\vec{B}\\
\nabla \times \vec{B}&= \mu\sigma\vec{E}+\mu\varepsilon\partial_{t}\vec{E}
\end{align*}$$
e temos a equação de continuidade:
$$\nabla \cdot \vec{\mathcal{J_{\ell}}}=-\partial_{t}\rho_{\ell}$$
e podemos escrever:
$$\partial_{t}\rho_{\ell}=-\nabla \cdot (\sigma\vec{E})=-\sigma(\nabla \cdot \vec{E})=- \frac{\sigma}{\varepsilon}\rho_{\ell}$$
tendo esta equação diferencial as seguintes soluções:
$$\rho_{\ell}(t)=\rho_{\ell}(0) e^{- \frac{\sigma}{\varepsilon}t}$$
- Ou seja, qualquer densidade inicial de carga $\rho_{\ell}(0)$ se dissipa exponencialmente. Quando $t=\tau\equiv \frac{\varepsilon}{\sigma}$ (Tempo Caraterístico) consideramos que $\rho_{\ell}=0$. Isto bate certo com a noção que cargas livres no interior de um condutor se movem para a fronteira.
- O tempo carraterístico dá-nos uma noção do quão "bom" o condutor é. Se ele for ideal temos $\sigma=\infty,\tau=0$ e portanto nunca temos cargas livres no interior do condutor, tal como vimos no capítulo de eletrostática. No caso de um condutor "bom", temos que $\tau$ é muito inferior que os tempos caraterísticos do sistema em estudo.

**Equação de Onda**
- Não iremos estudar este estado de transição e movimento de cargas. Passemos então para um instante $t>\tau$ e temos as equações de Maxwell na forma:
$$\begin{align*}
\nabla \cdot \vec{E}&= 0\\
\nabla \cdot \vec{B}&= 0\\
\nabla \times \vec{E}&= - \partial_{t}\vec{B}\\
\nabla \times \vec{B}&= \mu\sigma\vec{E}+\mu\varepsilon\partial_{t}\vec{E}
\end{align*}$$
- Se fizermos o rotacional das equações dos rotacionais ficamos com:
$$\begin{align*}
\nabla^{2} \vec{E}&= \mu\varepsilon\partial_{t}^{2}\vec{E} + \mu\sigma \partial_{t}\vec{E}\\
\nabla^{2}\vec{B}&= \mu\varepsilon \partial_{t}^{2}\vec{B}+\mu\sigma \partial_{t}\vec{B}
\end{align*}$$
isto são as equações de onda dos campos elétrico e magnético, mas temos um termo extra (com a condutividade).

- Still, ainda podemos definir $\vec{E},\vec{B}$ como ondas:
$$\vec{E}(t,\vec{r})=\vec{E_{0}}e^{i(\vec{k}\cdot\vec{r}-\omega t)}$$
$$\vec{B}(t,\vec{r})=\vec{B_{0}}e^{i(\vec{k}\cdot\vec{r}-\omega t)}$$
em que agora o número de onda é complexo:
$$k^{2}=\mu\varepsilon\omega^{2} + i \mu \sigma \omega$$
em que:
$$\text{Re}[k]=\omega\sqrt{\frac{\varepsilon\mu}{2}} \left[\sqrt{1+\left(\frac{\sigma}{\varepsilon\omega}\right)^{2}} +1\right]^\frac{1}{2}$$
$$\text{Im}[k]=\omega\sqrt{\frac{\varepsilon\mu}{2}} \left[\sqrt{1+\left(\frac{\sigma}{\varepsilon\omega}\right)^{2}} -1\right]^\frac{1}{2}$$
se escrevermos $\vec{k}=(\text{Re}[k]+i\text{Im}[k])\hat{z}$  (uma onda a mover-se na direção zz) fica:
$$\vec{E}(t,\vec{r})=\vec{E_{0}}e^{-\text{Im}[k]z}e^{i(\text{Re}[k]z-\omega t)}$$
ou seja, a parte imaginária resulta numa atenuação da onda. Na prática, isto significa que consoante a onda EM entra no condutor ela vai enfraquecendo.
- A distância que a onda percorre no condutor até que a sua amplitude diminua para $E_{0}/e$ é:
$$d=\frac{1}{\text{Im}[k]}$$

- E podemos escrever:
$$\lambda=\frac{2\pi}{\text{Re}[k]} \quad;\quad v=\frac{\omega}{\text{Re}[k]}\quad;\quad n=\frac{c}{v}=\frac{c \text{Re}[k]}{\omega}$$
- As equações de Maxwell dizem-nos que $\nabla \cdot \vec{E}=0,\nabla \cdot \vec{B}=0$. Daqui resulta que $\vec{E},\vec{B}\perp\vec{k}$ (oscilações perpendiculares à propagação). Mais concretamente podemos escrever:
$$\vec{k}\times\vec{E}=\omega \vec{B}$$
por exemplo, podemos ter:
![[onda EM em condutor.png]]
em que:
$$\begin{align*}
\vec{E}(t,\vec{r})&= E_{0}e^{-\text{Im}[k]z}e^{i(\text{Re}[k]z-\omega t)}\hat{x}\\
\vec{B}(t,\vec{r})&= \frac{k}{\omega}\hat{z}\times\vec{E}= \frac{k}{\omega}E_{0}e^{-\text{Im}[k]z}e^{i(\text{Re}[k]z-\omega t)}\hat{y}
\end{align*}$$

**Número de onda como fasor**
- Como qualquer número complexo, podemos escrever:
$$k=|k|e^{i\phi}$$
em que:
$$|k|=\sqrt{\text{Re}[k]^{2}+\text{Im}[k]^{2}}=\omega\sqrt{\varepsilon\mu \sqrt{1+\left(\frac{\sigma}{\varepsilon\omega} \right)^{2}}} \quad \quad;\quad \quad \phi=\arctan\left(\frac{\text{Im}[k]}{\text{Re}[k]}\right)$$

- Ora, nas equações de $\vec{E},\vec{B}$ os termos $E_{0},B_{0}$ são complexos, sendo que:
$$E_{0}=|E_{0}|e^{i\delta_{E}} \quad;\quad B_{0}=|B_{0}|e^{i\delta_{B}}$$
e podemos establecer a relação:
$$|B_{0}|e^{i\delta_{B}}=\frac{|k|e^{i\phi}}{\omega}|E_{0}|e^{i\delta_{E}}$$
ou seja, passamos a ter uma diferença de fase entre os campos:
$$\delta_{B}-\delta_{E}=\phi$$
sendo que o campo magnético está *atrasado* em relação ao elétrico.

- Podemos então relacionar as amplitudes reais dos campos da forma:
$$|B_{0}|=\frac{|k|}{\omega}|E_{0}|$$

$$\Huge{\mathbf{------------FIM------------}}$$