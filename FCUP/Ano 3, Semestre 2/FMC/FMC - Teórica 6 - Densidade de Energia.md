 ###### Aula 6 - 7/3/2024
## Ordens de Grandeza
- Na aula anterior vimos que $$k_{F}=3\pi^{2}n$$
ora, vimos no início da cadeira que:
$$n=\frac{3}{4\pi r_{s}^{3}}$$
- E temos:
$$k_{F}=3.63 \left(\frac{a_{0}}{r_{s}}\right)\times10^{10}\text{m}^{-1}\sim 1.8 \dot{A}$$
e desta forma podemos definir o comprimento de onda de Fermi:
$$\lambda_{F}=\frac{2\pi}{k_{F}}\sim 1\dot{A}$$
- Podemos ainda calcular:
$$\varepsilon_{F}=\frac{\hbar^{2}k_{F}^{2}}{2m}=\frac{\hbar^{2}}{2ma_{0}^{2}}(a_{0}k_{F})^{2}=\frac{e^{2}}{2a_{0}}(a_{0}k_{F})^{2}=50.1\left(\frac{a_{o}}{r_{s}}\right)^{2} \text{eV}\sim [1.5-15]\text{eV}$$

**Energia e Temperatura**
- Podemos definir a grandeza do intervalo de energia entre 2 k's consecutivos:
$$\begin{align*}
\Delta \varepsilon&= \frac{\hbar^{2}}{2m}[(k+\Delta k)^{2}-k^{2}]\\
&= \frac{\hbar^{2}}{2m}[\cancel{k^{2}}+2k\Delta k+\Delta k^{2}-\cancel{k^{2}}]\\
&\sim \frac{\hbar^{2}}{2m}k\Delta k=\frac{\hbar^{2}}{2m}k \frac{2\pi}{L}
\end{align*}$$
como $L\gg\dot{A}$ então a variação de energia é muito reduzida.
- Quando a temperatura $T$ aumenta os eletrões mudam de estado. Ora, só os eletrões com energia de Fermi mudam.
    - Isto ocorre devido ao princípio de exclusão: os eletrões dos estados internos não podem mudar, todos os estados que os rodeiam estão preenchidos. Estão tão "enterrados" que não conseguem mover.
    - CONFIRMAR -- Além disso, os eletrões deste nível têm maior energia ($\varepsilon\propto k^{2}$) logo a energia necessária para trocar de nível ($\Delta\varepsilon$) é menor em comparação à energia do estado
- Esta parte vai ser aprofundada direito na próxima aula.

## Energia Total
- Podemos definir:
$$E=2\sum\limits_{k\le k_{F}}\varepsilon(k)=2\sum\limits_{k\le k_{F}}\frac{\hbar^{2}}{2m}k^{2}$$
ora, temos então uma soma ao longo de uma função $F(\vec{k})$.
- Graficamente temos:
![[energia vs k]]

- Ora, esta soma é muito trabalhosa de realizar analiticamente. E seria muito conveniente conseguir tornar isto num integral. Vemos que o traçado aparente daria uma função contínua e "bem comportada", pelo que isto deverá ser possível.
- Temos:
$$\sum\limits_{\vec{k}}F(\vec{k})=\frac{1}{\left(\frac{2\pi}{L}\right)^{3}}\sum\limits_{\vec{k}}F(\vec{k})\left(\frac{2\pi}{L}\right)^{3}=\frac{L^{3}}{(2\pi)^{3}}\sum\limits_{\vec{k}}F(\vec{k})\left(\frac{2\pi}{L}\right)^{3}$$
podemos definir $\Delta^{3}\vec{k}=\left(\frac{2\pi}{L}\right)^{3}$:
$$V\sum\limits_{\vec{k}}F(\vec{k})=\frac{1}{(2\pi)^{3}}\sum\limits_{\vec{k}}F(\vec{k})\Delta^{3}\vec{k}$$
- Assim, no limite $V\to\infty$ temos:
$$\lim\limits_{V\to\infty} \frac{1}{V}\sum\limits_{\vec{k}} F(\vec{k})= \frac{1}{8\pi^{3}}\int_{\vec{k}\le\vec{k}_{F}}F(\vec{k})dk$$
- E assim temos:
$$\frac{E}{V}=2\times\frac{1}{8\pi^{3}}\int_{\vec{k}\le\vec{k}_{F}}\frac{\hbar^{2}}{2m}k^{2}~d^{3}\vec{k}=2\times\frac{1}{8\pi^{3}}\int_{\vec{k}\le\vec{k}_{F}}\frac{\hbar^{2}}{2m}k^{2}\cdot4\pi k^{2} ~ dk=\frac{\hbar^{2}k_{F}^{5}}{10\pi^{2}m}=\frac{\hbar^{2}}{10\pi^{2}m}(3\pi^{2}n)^{\frac{5}{3}}$$
- Como podemos escrever $\frac{E}{V}=\frac{E}{N} \frac{N}{V}$
$$\frac{E}{V}=\frac{\hbar^{2}k_{F}^{5}}{10\pi^{2}m}=\frac{\hbar^{2}k_{F}^{3}}{2m} \frac{k_{F}^{2}}{5\pi^{2}}=\frac{\hbar^{2}k_{F}^{3}}{2m} \underbrace{\frac{k_{F}^{2}}{3\pi^{2}}}_{\frac{N}{L^{3}}} \frac{3}{5}=\frac{3}{5}\varepsilon_{F} \frac{N}{V}$$
logo temos
$$\frac{E}{N}=\frac{3}{5}\varepsilon_{F}$$
que podemos escrever como $$\frac{E}{N}=\frac{3}{5}k_{B}T_{F}~~\to~~ T_{F}=\frac{\varepsilon_{F}}{k_{B}}=58.2\left(\frac{a_{0}}{r_{s}}\right)^{2}\times10^{4}\text{K}$$

**Densidade de Estados**
- Consideremos o espaço recíproco:
![[esferas densidade energia]]
- Temos uma superfície esférica dos estados com o número de onda $k$ e outra de $k+dk$.
- Entre estas superfícies temos um volume: $4\pi k^{2}dk$ em que temos $n_{k}$ estados com $k$. 
- Assim, podemos definir uma densidade de estados k:
$$g(\vec{k})=\frac{dn_{k}}{d^{3}k}~~\to~~ dn_{k}=g(\vec{k})d^{3}k=g(\vec{k})4\pi k^{2}dk$$
- Podemos ainda definir a densidade de estados eletrónicos:
$$g(\varepsilon)=\frac{dn_\varepsilon}{d\varepsilon}=\frac{k^{2}}{\pi^{2}}$$
que iremos ver na próxima aula.