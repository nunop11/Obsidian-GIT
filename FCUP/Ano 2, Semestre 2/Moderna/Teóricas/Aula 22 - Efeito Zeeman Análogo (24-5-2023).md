# Experiência de Stern-Gerlach - Recapitular
![[efeito zeeman.png]]
- Na aula anterior vimos que, ao projetar um feixe de eletrões por um campo magnético não uniforme, o feixe se dividia em partes. 
- Do modelo de Bohr temos que, para 1 eletrão temos o **momento dipolar** em relação ao momento angular:
$$\vec{\mu}_{L}=- \frac{|e|}{2m}\vec{L}=- \frac{|e|\hbar}{2m} \frac{\vec{L}}{\hbar} = - \mu_{B} \frac{\vec{L}}{\hbar} \equiv g_{\ell} \mu_{B} \frac{\vec{L}}{\hbar} \quad; \quad \textsf{sendo que}\quad g_{\ell}=-1$$
sendo que $\vec{L},\vec{\mu}_{L}$ têm direção igual, mas sentidos opostos.

- Ora, ao introduzir o **Spin** temos que: 
$$\vec{\mu}_{S}= \frac{|e|}{m}\vec{S}=2\mu_{B} \frac{\vec{S}}{\hbar}= g_{s} \mu_{B} \frac{\vec{S}}{\hbar} \quad;\quad \textsf{sendo que} \quad g_{s}=2$$
## Hipótese
- Consideremos a hipótese em que os átomos de Prata no forno na experiência de Stern-Gerlach estão a uma temperatura de $T=1000K$. Verifiquemos que eles estariam no nível fundamental.
- Ora, o número de eletrões no 1º nível excitado será:
  $$\#excitados = e^{-E^{*}/k_{B}T}$$em que $E^{*}$ é a energia desse nível
- Por outro lado, ao 
$$\# fundamental = e^{-E_{0}/k_{B}T}$$
- E temos então:
$$\frac{\# excitados}{\# fundamental}= \frac{e^{-E^{*}/k_{B}T}}{e^{-E_{0}/k_{B}T}}$$
- Ora, temos $E^{*}-E_{0}\simeq 1~eV, k_{B}=8.6\cdot10^{-5}~eV/K, T=1000K$ ficamos com  
$$\frac{\# excitados}{\# fundamental}\approx e^{-100}$$
ou seja, no cenário considerado, a probabilidade de um átomo de prata estar no 1º nível excitado é muito baixa. Assim, consideramos que os átomos estão no *estado fundamental*.

# Efeito Zeeman Anómalo
## Efeito de Zeeman Normal
- Tal como vimos atrás, a equação de Schrödinger para um átomo H sob o efeito de um campo elétrico $B$ fica:
$$\left[ - \frac{\hbar^{2}}{2m} \nabla^{2} - \frac{1}{4\pi\varepsilon_{0}} \frac{e^{2}}{r} - \vec{\mu} \cdot \vec{B} \right] \Psi=E \Psi$$

- Em que a energia total no eletrão será: $E'=E+ \vec{\mu}_{B}\cdot \vec{B}$
- Tendo $\vec{B}=(0,0,B)$ ficamos com $E'=E + \mu_{z}B$. 
- Recordando que $\vec{\mu}=\frac{|e|}{2m} \vec{L} = \frac{|e|\hbar}{2m} \frac{\vec{L}}{\hbar} = \mu_{B}\frac{\vec{L}}{\hbar}$ temos:
$$E' = E + \mu_{z}B=E+ \mu_{B} \frac{L_{z}}{\hbar} B$$
- E sendo $L_{z}=m_{\ell}\hbar$ ficamos com a fórmula geral:
$$E_{nm_{\ell}} = E_{n} + \mu_{B}m_{\ell}B$$

## Momento Angular Total
- Definimos o momento angular total como: $\vec{\mathcal{J}}=\vec{L}+\vec{S}$.
- Tal como vimos antes:
    - $|\vec{L}|=\sqrt{\ell(\ell+1)}\hbar$ , $L_{z}=m_\ell\hbar$ sendo que $-\ell\le m_{\ell}\le \ell$ 
    - $|\vec{S}|=\sqrt{s(s+1)}\hbar$, $S_{z}=m_{s}\hbar$ sendo que $-s\le m_{s}\le s$
- Assim, temos: 
$$|\mathcal{\vec{J}}|= \sqrt{j(j+1)}\hbar \quad;\quad \mathcal{J}_{z}=m_{j}\hbar \quad;\quad -j\le m_{j}\le j$$
#### Teorema de Adição de Momentos Angulares
$$|\ell-s|\le j\le |\ell+s|$$
==**EXEMPLO**==
- Ora, para um eletrão temos $s=\frac{1}{2}$, logo: $j=\left[~|\ell- \frac{1}{2}|~;~ \ell+ \frac{1}{2}~\right]$.
- No nível 1s temos $\ell=0$ e então $j=\frac{1}{2}$, pelo que $m_{j}=\frac{-1}{2},\frac{1}{2}$
- No nível 2p temos $\ell=1$ e então $j=\frac{1}{2},\frac{3}{2}$ e assim: $m_{j}=\frac{-3}{2}, \frac{-1}{2}, \frac{1}{2}, \frac{3}{2}$.

---- Havia um Exemplo mas decidi não passar ----

#moderna #fisica 