# Modelo de Rutherford
- _Modelo Planetário_ - eletrões orbitam o núcleo do átomo, como planetas orbitam o sol
- Uma falha deste modelo era que, segundo o eletromagnetismo, uma carga elétrica (eletrão) com aceleração emite radiação.
![[colisao thomson.png]]
- Devido a resultados experimentais, esta teoria defende que temos que a trajetória do projétil é hiperbólica. Tem-se ainda que um parametro de impacto menor causa maior difusão, pois existe um objeto de maior massa no centro do átomo: o _núcleo_.
- No estudo de uma passagem de um projetil (partícula alpha) perto de um núcleo, consideramos que que o núcleo está em repouso e que não é afetado por este processo. Consideramos ainda que os eletrões do átomo têm um efeito insignificante.
- O ângulo de difusão depende do parâmetro de impacto ($b$), sendo que temos a seguinte equação de movimento que descreve a relação entre $r$ e $\varphi$:
$$\frac{1}{r}=\frac{1}{b}\sin \varphi + \frac{D}{2b^{2}}(\cos\varphi-1)$$
sendo $D$ a distância de maior aproximação ao núcleo na trajetória do projétil.
- Temos que neste  movimento existe conservação de energia e de momento angular. Iremos definir $\vec{\ell}$ como sendo o momento angular de $\alpha$ relativamente ao núcleo.
- Antes de mais, de notar que ao calcular o momento angular temos que:
> ![[difusao thomson.png]]
> $$\vec{r}\times \vec{v}=(\vec{b}\times \vec{v})+\cancelto0{(\vec{r}_{\parallel}\times \vec{v})}$$
- Na posição $r=-\infty$ temos 
$$\begin{align*}
E_{-\infty}&= \frac{1}{2}mv_{\infty}^{2}+\cancelto0{E_{p}(-\infty)}=\frac{1}{2}mv_{8-\infty}^{2}\\
\vec{\ell}&= \vec{r}\times(n \vec{v}_{\alpha})=nv_{-\infty}b~\hat{n}
\end{align*}$$
- Na posição $r=r_\text{min}$ temos:
$$\begin{align*}
E=E_{c}+E_{p}=\frac{1}{2}mv_\text{min}^{2} + \frac{1}{4\pi \varepsilon_{0}} \frac{q_{\alpha}q_{N}}{r_\text{min}}\\
\vec{\ell}=m v_\text{min} r_\text{min}\hat{n}
\end{align*}$$
- Se aplicarmos a conservação de energia e de momento angular temos:
$$\begin{cases}
\frac{1}{2}mv_\text{min}^{2}+\frac{1}{4 \pi \varepsilon_{0}} \frac{q_{\alpha}q_{N}}{r_\text{min}}=\frac{1}{2}mv_{\infty}^{2} \\
mv_{\infty}b=mv_\text{min}r_\text{min}
\end{cases}$$
- Ao isolar $v_\text{min}$ na equação de baixo e substituir na equação de cima temos:
$$\frac{1}{2}m \left( \frac{b^{2}v_{\infty}^{2}}{r_\text{min}^{2}}\right)+ \frac{1}{4\pi \varepsilon_{0}} \frac{q_{\alpha}q_{N}}{r_\text{min}} = \frac{1}{2} m v_{\infty}^{2} $$

- Assim, como em $r_\text{min}$ (que acima dissemos que podemos chamar também de $D$) teremos que $b=0$, ou seja, é como se passasse tão perto que não há "desnível" entre as 2 partículas. Assim, temos:
$$D = \frac{1}{4\pi \varepsilon_{0}} \frac{q_{\alpha}q_{N}}{E_{c_{i}}}$$

## Parametro de Impacto e ângulo de difusão
- Pegando na equação inicial do movimento ($\frac{1}{r}=\frac{1}{b}\sin \varphi + \frac{D}{2b^{2}}(\cos\varphi-1)$) e tendo em conta que no final do movimento temos $\varphi=\pi-\theta,~r\rightarrow \infty$, obtemos:
$$\begin{align*}
\frac{1}{\infty}&= \frac{1}{b} \sin(\pi-\theta)+ \frac{D}{2b^{2}} (\cos(\pi-\theta)-1)\\
-\frac{1}{b}\sin \theta&= \frac{D}{2b^{2}}(-\cos \theta-1)\\\\
b &= \frac{D}{2} \left(\frac{\cos\theta+1}{\sin\theta}\right)=\frac{D}{2} \cot\frac{\theta}{2}= \frac{q_{\alpha}q_{N}}{8E_{c}\pi\varepsilon_{0}}\cot \frac{\theta}{2}
\end{align*}$$

## Difusão de ângulo superior a $\theta$ 
![[experiencia thomson.png]]
- Consideremos que temos um projétil a atravessar uma placa com 1 átomo de espessura. Na figura acima, cada átomo da placa é um círculo, de área $\pi R^{2}$.
- Para o projétil ser difundido com um ângulo de _pelo menos_ $\theta$, então ele terá de incidir num círculo de área $\pi b^{2}$ (de recordar que menor $b$ leva a maior ângulo de difusão $\theta$).
- Considerando que neste átomo incide um grupo de projeteis distribuídos uniformemente, a porção de projéteis que terão ângulo de difusão maior ou igual a $\theta$ será de $\Large\frac{\pi b^{2}}{\pi R^{2}}$.

- Consideremos agora uma placa real de espessura $t$, área $A$, densidade $\rho$ e composta por um material de massa molar $M$. O número de moles de átomos que compõem a placa será $\large\frac{m}{M}=\frac{\rho A t}{M}$. Temos então que o número de átomos por unidade de volume nesta placa será:
$$n=N_{A}\cdot \frac{\rho At}{M}\cdot \frac{1}{At}=\frac{N_{A}\rho}{M}$$
- Assim, o número de núcleos (que é igual ao número de átomos) numa área $a$ será $\Large na=\frac{N_{A}\rho a}{M}$
- Assim, a porção de projéteis que são difundidos com um ângulo maior ou igual a $\theta$ é $$f_{<b}=f_{>\theta}=na \pi b^{2}$$

## Fórmula de Difusão
- A fração de projeteis que incide o átomo com um parâmetro de impacto entre $\theta$ e $\theta+d \theta$ é dada pela derivada da equação acima e é:
$$df = na(2\pi b~db)$$
- Ao derivar a fórmula de $b(\theta)$ obtida acima temos:
$$db = \frac{q_{\alpha}q_{N}}{8E_{c}\pi\varepsilon_{0}}\left(-\csc^{2}\left(\frac{\theta}{2}\right)\right)\left(\frac{1}{2}d\theta \right)$$
- Ao juntar as duas equações acima temos
$$|df|=\pi n a \left( \frac{q_{\alpha}q_{N}}{8E_{c}\pi\varepsilon_{0}}\right)^{2} \csc^{2} \frac{\theta}{2}\cot \frac{\theta}{2} d \theta$$
Podemos ainda aproveitar a notação do Krane e escrever $q_{\alpha}=z \cdot e$, $q_{N}=Z \cdot e$, sendo $z,Z$ os números atómicos do projétil e núcleo e $e=1.6\cdot10^{-19}~C$ a carga unitária. Assim, temos que $\large \frac{e^{2}}{4\pi\varepsilon_{0}}=1.44 eV \cdot nm$ e podemos reescrever a equação acima:
$$|df|=\pi n a \left(\frac{zZ}{2E_{c}}\right)^{2}\left(\frac{e^{2}}{4\pi\varepsilon_{0}}\right)^{2} \csc^{2} \frac{\theta}{2}\cot \frac{\theta}{2} d \theta$$
![[difusao rutherford.png]]
- A probabilidade de um projétil ser difundido e passar pelo detetor depende da probabilidade de este ser difundido e passar num anel de raio interno $r\sin\theta$ e de espessura $rd\theta$. A unidade do anel será $dA=2\pi r \sin\theta \cdot rd\theta$.
- A probabilidade de um projetil ser difundido e passar numa unidade de área do anel é $\large\frac{|df|}{dA}=N(\theta)$, sendo que:
$$\begin{align*}
N(\theta)&= \frac{\pi n a \left(\frac{zZ}{2E_{c}}\right)^{2}\left(\frac{e^{2}}{4\pi\varepsilon_{0}}\right)^{2} \csc^{2} \frac{\theta}{2}\cot \frac{\theta}{2} \cancel{d \theta}}
{2r^{2}\sin\theta \cancel{d\theta}}\\
&= \frac{\pi n a \left(\frac{zZ}{2E_{c}}\right)^{2}\left(\frac{e^{2}}{4\pi\varepsilon_{0}}\right)^{2} \frac{1}{\sin^{2} \frac{\theta}{2}} \frac{ \cancel{\cos\frac{\theta}{2}} }{\sin \frac{\theta}{2}}}
{2r^{2}\cdot2\sin\frac{\theta}{2} \cancel{\cos\frac{\theta}{2}}}\\\\
N(\theta) &= \frac{na}{4r^{2}} \left(\frac{zZ}{2E_{c}}\right)^{2} \left(\frac{e^{2}}{4\pi\varepsilon_{0}}\right)^{2} \frac{1}{\sin^{4} \frac{\theta}{2}}=\frac{d \sigma}{d \Omega}
\end{align*}
$$
- Ora, esta é _Fórmula da Difusão de Rutherford_.
- Todas as relações lineares indicada na fórmula acima foram provadas experimentalmente.

#moderna #fisica #atomo