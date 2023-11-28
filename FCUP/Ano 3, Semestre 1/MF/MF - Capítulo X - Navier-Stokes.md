- No capítulo 5 vimos métodos de análise integral / balanços macroscópicos apra estudar escoamentos de fluidos. Vejamos então como estudar um escoamento através de balanços microscópicos, usando a famosa **equação de Navier-Stokes**.

## Equação da Continuidade
- Em coordenadas cartesianas, a equação da continuidade tem a forma:
$$\frac{\partial\rho}{\partial t} + \nabla \rho \vec{v}=0$$
que para um fluido incrompressível ($\rho$ constante) nos dá:
$$\nabla \vec{v}=0$$
$$\boxed{\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}+\frac{\partial w}{\partial z}=0}$$

#### EXEMPLO
![[pistão e fluido a ser comprimido.png]]
- Consideremos um sistema como aquele representado acima. Numa câmara temos um gás que é comprimido por um pistão que se move de baixo para cima a velocidade constante $V$. A distância entre o pistão e o topo da câmara $L(t)$ é dada por:
$$L=L_{0}-Vt$$
(em que o eixo zz tem a direção indicada acima e $L_{0}=L_{t=0}$)
- Faremos então alguns pressupostos:
    - $\rho$ é uniforme em toda a câmara
    - a velocidade de escoamento do fluido apenas existe na direção z e depende do tempo: $u=v=0$  e $w=f(z,t)$
    - A velocidade varia linearmente com $z$ em todos os instantes: $w=C_{1}+C_{2}z$

- Destas hipóteses a equação de continuidade fica na forma: $$\frac{\partial\rho}{\partial t}+ \rho\frac{\partial w}{\partial z}=0$$

- Começamos por aplicar condições de fronteira:
    - $z=0 \to w=0$ (no topo da câmara o fluido não se move)
    - $z=L(t)\to w=-V$ (o fluido junto ao pistão move-se à sua velocidade)
de onde resulta:
$$w=-V \frac{z}{L(t)}$$
e podemos calcular
$$\frac{\partial w}{\partial z}=- \frac{V}{L(t)}=- \frac{V}{L_{0}-Vt}$$
- Substituindo na equação da continuidade:
$$\begin{align*}
\frac{\partial\rho}{\partial t}&= \rho \frac{V}{L_{0}-Vt}\\
\int_{\rho_{0}}^{\rho(t)} \frac{d\rho}{\rho} &= \int_{0}^{t}\frac{V}{L_{0}-Vt}dt
\end{align*}$$
e podemos adimensionalizar:
$$\rho^{*}=\frac{1}{1-t^{*}} \quad \quad;\quad \rho^{*}=\frac{\rho}{\rho_{0}} ~~;~~ t^{*}=\frac{Vt}{L_{0}}$$

### Equação Continuidade Coordenadas Cilíndricas
$$\frac{\partial\rho}{\partial t} + \frac{1}{r}\frac{\partial(\rho rv_{r})}{\partial r} + \frac{1}{r} \frac{\partial(\rho v_{\theta})}{\partial \theta} + \frac{\partial(\rho v_{z})}{\partial z}=0$$
que num fluido incompressível fica:
$$\boxed{\frac{1}{r}\frac{\partial(rv_{r})}{\partial r}+ \frac{1}{r}\frac{\partial(v_{\theta})}{\partial\theta} + \frac{\partial(\rho v_{z})}{\partial z}=0}$$
# Equação de Navier-Stokes
$$\boxed{\rho \frac{D \vec{v}}{Dt} = - \nabla p + \rho \vec{g} + \mu \nabla^{2}\vec{v}}$$
em que:
    - 1º termo ($\rho\frac{D\vec{v}}{Dt}$) é a derivada total AKA transporte convectivo da qttd de movimento
    - 2º termo ($-\nabla p$) é o gradiente de pressão
    - 3º termo ($\rho \vec{g}$) representa as forças exteriores AKA gravidade
    - 4º termo ($\mu\nabla^{2}\vec{v}$) representa a perda de quantidade de movimento devido a viscosidade

- Que para um fluido ideal se transforma na **Equação de Euler**:
$$\rho \frac{D\vec{v}}{Dt}=-\nabla p + \rho \vec{g}$$
- E podemos escrever a equação de Navier-Stokes em termos das componentes:
![[navier-stokes componentes cartesianas.png]]

- E temos ainda as componentes em coordenadas cilíndricas:
![[navier-stokes componentes cilindricas.png]]

#### EXEMPLO - Escoamento Couette 
![[exemplo escoamento couette.png|444]]
- Temos 2 placas infinitas separadas por uma distância $h$, repleta com um fluido de viscosidade $\mu$ e massa volúmica $\rho$. Na placa superior é aplicada uma força $F$, ficando esta com velocidade $V$.

- Começamos por impôr as hipóteses:
    - O escoamento é estacionário (o campo de velocidades é constante no tempo)
    - O fluido é incrompressível, newtoniano e o escoamento laminar
    - Não há gradiente de pressão na direção do escoamento AKA a força na placa superior é a única fonte do escoamento

- Da equação da continuidade temos:
$$\frac{\partial u}{\partial x}=0$$
- Peguemos agora nas componentes $x,y,z$ da equação Navier-Stokes.
    - Para $x$ temos $p_{x}=0,g_{x}=0$ e $u=u(z)$
    - Para $y$ temos $g_{y}=0, v=0$
    - Para $z$ temos $w=0$
- Fica:
$$\begin{align*}
&x: &\frac{\partial^{2}u}{\partial z^{2}}&= 0\\
&y: &\frac{\partial p}{\partial z}&= -\rho g_{z}\\
&z: &\frac{\partial p}{\partial z}&= 0
\end{align*}$$
da 1ª equação resulta: $u=C_{1}z+C_{2}$

- Temos as seguintes condições de fronteira (usando $z$ conforme o referencial acima):
    - $z=0\to u=0$
    - $z=h\to u=V$
de onde resulta:
$$u=\frac{V}{h}z$$
- No PPT tem mais exemplos:
    - Escoamento Couette com gradiente de pressão
    - Escoamento em parede molhada
    - Movimento de uma placa infinita