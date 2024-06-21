###### Aula 16 - 23/4/2024 (dada por JAM)

- Continuemos o que vimos atrás.
- Consideremos um potencial periódico: $V(\vec{r})=V(\vec{r}+\vec{R})$
- E vimos que, sendo este periódico, podemos fazer FT: $V(\vec{r})=\sum\limits_{\vec{k}} V_{\vec{k}}e^{i \vec{k}\cdot\vec{r}}$

- Sabemos que um estado $\psi_{\vec{k}}=\sum\limits_{\vec{K}}C_{\vec{k}-\vec{K}}e^{i(\vec{k}-\vec{K})\cdot\vec{r}}$ terá energia $\varepsilon(\vec{k})=\frac{\hbar^{2}(k-K)^{2}}{2m}$
    - Ou seja, o modelo de Sommerfeld consiste num caso particular disto: $\vec{K}=\vec{0}$ (ou então 1 dos termos desta soma)
    - Assim, vemos que $\vec{K}$ faz com que periodicidade no espaço real gere periodicidade no espaço recíproco.
    - Além disso, um K maior implica que o espaço real é "menor" (menor periodicidade / distâncias mais curtas / etc)


**Componente contínua**
- Consideremos que temos uma série de Fourier: $f(t)=\sum a_{n}\cos(\omega_{n}t+\phi_{n})+\sum\limits b_{n} \sin(\omega_{m}t+\phi_{m})$
- Ora, quando temos $\omega_{0}$ temos seno e cosseno de uma constante, ou seja, $f(t)$ não depende do tempo. Assim, $\omega_{0}$ corresponde à *componente contínua* da função descrita por esta série.
- Da mesma forma o termo de $K=0$ corresponde à componente contínua da função de onda de um problema de potencial periódico

**Exemplo**
- Consideremos $V=V_{0}\cos\left( \frac{2\pi}{a}x\right)+V_{0}$
- Podemos escrever isto como $V = \frac{V_{0}}{2} \left[e^{i \frac{2\pi}{a}x}+e^{-i \frac{2\pi}{a}x} \right]+Ve^{i 0\cdot x}$
- E temos então:
    - $\vec{k}=\frac{2\pi}{a}\hat{i}$, com $V_{k}=V_{0}/2$
    - $\vec{k'}=- \frac{2\pi}{a}\hat{i}$, com $V_{k}=V_{0}/2$
    - Componente contínua, com amplitude $V$

**De volta à equação central**
- Vimos a equação central:
$$\left[- \frac{\hbar^{2}}{2m}(\vec{k}- \vec{K})^{2}- \varepsilon_{n}(\vec{K}) \right]C_{\vec{k}-\vec{K}} + \sum\limits_{\vec{K'}}V_{\vec{K'}-\vec{K}}C_{\vec{k}-\vec{K'}}$$
