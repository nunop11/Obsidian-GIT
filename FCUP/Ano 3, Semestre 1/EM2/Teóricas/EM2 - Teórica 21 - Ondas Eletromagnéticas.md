# Ondas - Intro
- Podemos definir uma "onda" como sendo uma perturbação de um meio contínuo a mover-se no espaço. Normalmente consideramo-las como tendo forma e velocidade constantes. Claro, podemos ter ondas a ser absorvidas gradualmente ou ondas a dispersarem-se no espaço.

![[Attachments/FCUP/A3S1/EM2/onda progressiva.png]]
- Consideremos a onda acima, a mover-se com velocidade $v$. A função que descreve o seu formato inicial é $g(z)=f(z,0)$.
- Conforme a figura, podemos definir:
$$f(z,t)=f(z-vt,0)=g(z-vt)$$
- Ou seja, não precisamos de ter uma função $f(z,t)$ que pode depender da posição e tempo de qualquer forma. Basta ter uma função que depende destes 2 parâmetros, *especificamente na forma* $z-vt$. Isto é o que temos sempre que a onda se propaga com velocidade e forma constantes.

- Um fio que permite a propagação de uma onda apenas está a seguir a 2ª Lei de Newton, em que as forças de tensão dos 2 lados de um elemento infinitesimal de fio se anulam. É possível assim demonstrar (ver Griffiths, pág 383) que o fio com massa unitária $\mu$ e com força de tensão $T$ segue a **equação de onda** na forma:
$$\frac{\partial^{2}f}{\partial z^{2}}=\frac{\mu}{T}\frac{\partial^{2}f}{\partial t^{2}}~~\to~~ \frac{\partial^{2}f}{\partial z^{2}}=\frac{1}{v^{2}} \frac{\partial^{2}f}{\partial t^{2}}$$
(em que $v$ é a velocidade de propagação da onda)

- De notar que *todas* as funções do tipo $f(z,t)=g(z-vt)$ são soluções da equação de onda.
- Claro, como temos $v^{2}$ (e não $v$) também funções do tipo $f(z,t)=h(z+vt)$ são soluções da equação de onda, pelo que estas represntam ondas a mover-se no sentido negativo do eixo $z$ com velocidade $v$.
- Podemos portanto definir todas as soluções da Eq de Onda com uma combinação linear de $g,h$:
$$f(z,t)=g(z-vt)+h(z+vt)$$

### Condições de Fronteira de Ondas
- Consideremos que temos uma onda a propagar-se num fio com massa por comprimento $\mu_{1}$. Num certo ponto este fio une-se a outro, com $\mu_{2}\neq\mu_{1}$. Assim, teremos $v_{1}\neq v_{2}$. Consideremos que esse ponto de união se encontra em $z=0$.
- Teremos portanto uma onda incidente, refletida e transmitida. 
    - A incidente é do tipo: $f_{I}(z,t)=A_{I}e^{i(k_{1}z-\omega t)}$
    - A refletida é do tipo: $f_{R}(z,t)=A_{R}e^{i(-k_{1}z-\omega t)}$
    - A incidente é do tipo: $f_{T}(z,t)=A_{T}e^{i(k_{2}z-\omega t)}$
 
- A frequências angulares $\omega$ das ondas são todas iguais. Assim, sendo $v_{1}\neq v_{2}$ então também temos $\lambda_{1}\neq\lambda_{2}$ e temos a relação:
$$\frac{\lambda_{1}}{\lambda_{2}}=\frac{k_{2}}{k_{1}}=\frac{v_{1}}{v_{2}}$$
Aqui devemos notar que ao considerar uma "onda sinusoidal" estamos a considerar um caso ideal em que a onda está a ser gerada em $z=-\infty$ e tem propaga-se desde sempre. Se estivessemos a considerar um caso mais real, com uma onda finita teríamos combinações de funções sinusoidais. No caso do EM temos ondas mesmo sinusoidais, pelo que consideramos o caso que eles se estendem até ao infinito.

- A "onda total" que temos é portanto:
$$f(z,t)=\begin{cases}
A_{I}e^{i(k_{1}-\omega t)} + A_{R}e^{i(-k_{1}-\omega t)} \quad;\quad z<0 \\
A_{T}e^{i(k_{2}-\omega t)}\quad;\quad z>0
\end{cases}$$
- Mas temos condições de fronteira:
    - Os 2  fios não se podem separar, ou seja: $$f(0^{-},t)=f(0^{+},t)$$
    - Sendo a união entre os fios (nó) de massa desprezável, não pode existir força exercida nele. Assim, também temos que ter: $$\frac{\partial f}{\partial z}\Biggr|_{0^{-}}=\frac{\partial f}{\partial z}\Biggr|_{0^{+}}$$

- Destas condições surge:
$$A_{I}+A_{R}=A_{T} ~~\to~~ k_{1}(A_{I}-A_{R})=k_{2}A_{T}$$
e daqui podemos obter:
$$A_{R}= \left( \frac{k_{1}-k_{2}}{k_{1}+k_{2}}\right)A_{I}\quad;\quad A_{T}=\left( \frac{2k_{1}}{k_{1}+k_{2}}\right)A_{I}$$
de onde temos:
$$A_{R}=\left(\frac{v_{2}-v_{1}}{v_{2}+v_{1}} \right)A_{I}\quad;\quad A_{T}=\left(\frac{2v_{2}}{v_{2}+v_{1}} \right)$$

### Polarização de Ondas
- Uma onda a propagar-se numa mola é *longitudinal* - perturbação (contrações e extensões da mola) ocorre na direção de propagação.
- Uma onda a propagar-se num fio é *transversal* - a perturbação que ela causa ocorre perpendicular à direção de propagação. Ondas EM também.

- Ora, no caso de uma onda transversal, existem infinitas direções perpendiculares à de propagação. Polarização consiste nisso: qual a direção em que a onda oscila.
- Podemos definir 2 componentes principais: horizontal ($\hat{x}$), vertical ($\hat{y}$) e uma direção $\hat{n}$ que consiste na soma das componentes vertical e horizontal
![[polarizacao de ondas EM.png]]

em que podemos definir $$\hat{n}=\cos\theta\hat{x}+ \sin\theta\hat{y}$$

# Ondas Eletromagnéticas no Vácuo
- No vazio (meio sem carga nem corrente) temos $\rho=0,\vec{\mathcal{J}}=\vec{0}$ e as equações de Maxwell ficam na forma:
$$\begin{align*}
\nabla \cdot \vec{E}&= 0\\
\nabla \cdot \vec{B}&= 0\\
\nabla \times \vec{E}&= - \frac{\partial \vec{B}}{\partial t}\\
\nabla \times \vec{B}&= \mu_{0}\varepsilon_{0} \frac{\partial \vec{E}}{\partial t} = \frac{1}{c^{2}} \frac{\partial \vec{E}}{\partial t}
\end{align*}$$
e temos um conjunto de eqs diferenciais de 1º grau acopladas.

- Podemos fazer o rotacional da 3ª Equação:

$$\begin{align*}
\nabla \times (\nabla \times \vec{E})&= \nabla(\cancelto0{\nabla \cdot \vec{E}}) - \nabla^{2}\vec{E}\\
\nabla \times \left(- \frac{\partial \vec{B}}{\partial t} \right)&= - \nabla^{2}\vec{E}\\
- \frac{\partial}{\partial t}(\nabla \times \vec{B})&= -\nabla^{2}\vec{E}\\
\frac{1}{c^{2}} \frac{\partial^{2}\vec{E}}{\partial t^{2}}&= \nabla^{2}\vec{E}
\end{align*}$$

ou então o rotacional da 4ª Equação:
$$\begin{align*}
\nabla \times(\nabla \times \vec{B})&= \nabla(\cancelto0{\nabla \cdot \vec{B}}))-\nabla^{2}\vec{B}\\
\nabla \times \left(\frac{1}{c^{2}} \frac{\partial\vec{E}}{\partial t} \right) &= - \nabla^{2}\vec{B}\\
\frac{1}{c^{2}} \frac{\partial}{\partial t}(\nabla \times \vec{E})&= - \nabla^{2}\vec{B}\\
\frac{1}{c^{2}} \frac{\partial^{2}\vec{B}}{\partial t^{2}}&= \nabla^{2}\vec{B}
\end{align*}$$
e temos então a equação de onda para os campos elétrico e magnético:
$$\boxed{\nabla^{2}\vec{E}=\frac{1}{c^{2}}\frac{\partial^{2}\vec{E}}{\partial t^{2}} \quad \quad;\quad \quad \nabla^{2}\vec{B}=\frac{1}{c^{2}}\frac{\partial^{2}\vec{B}}{\partial t^{2}}}$$

- No entanto, podemos reescrever as 2 equações acima na forma:
$$\left(-\frac{1}{c^{2}} \frac{\partial^{2}}{\partial t^{2}} + \nabla^{2} \right)\vec{E}=\vec{0}$$
em que definimos o operador *d'Alembertiano*:
$$\square = \nabla^{2} - \frac{1}{c^{2}}\partial_{t}^{2}$$
e podemos escrever as equações de onda como:
$$\square \vec{E}=\vec{0} \quad \quad;\quad \quad \square \vec{B}=\vec{0}$$
- Estas equações já não estão acopladas, mas são de 2º grau.

## Ondas Planas e Monocromáticas
- Ondas *monocromáticas* são ondas em que a frequência angular $\omega$ é constante.
- Ondas *planas* são aquelas que se propagam em $z$, não tendo dependência em $x,y$.
- Este tipo de ondas corresponde então a campos do tipo:
$$\vec{E}=\vec{E}_{0}e^{i(\vec{k}\cdot\vec{r}-\omega t)} \quad \quad;\quad \quad \vec{B}=\vec{B}_{0}e^{i(\vec{k}\cdot\vec{r}-\omega t)}$$
considerando uma onda a propagar-se na direção $z$:
$$\vec{E}=\vec{E}_{0}e^{i(kz-\omega t)} \quad \quad;\quad \quad \vec{B}=\vec{B}_{0}e^{i(kz-\omega t)}$$
e aqui devemos notar uma coisa: as seguintes notações são equivalentes
$$\vec{E}(t,\vec{r})=\vec{E_{0}} \cos(\vec{k}\cdot\vec{r}-\omega t+\delta_{E}) \quad \quad;\quad \quad \vec{E}=\vec{E_{0}}e^{i(\vec{k}\cdot\vec{r}-\omega t)}$$
ora, o vetor $\vec{E_{0}}$ da representação complexa é na verdade complexo e inclui a fase da representação sinusoidal. O Griffiths usa $\tilde E_{0}$ para este vetor para distinguir. O Avelino não, portanto irei fazer o mesmo. No entanto, convém ter isto em conta.

- Sendo $\vec{k}=(k_{x},k_{y},k_{z})$ e $\vec{r}=(x,y,z)$ podemos escrever:
$$\vec{E}=\vec{E}_{0}e^{i(k_{x}x+k_yy+k_zz-\omega t)}$$
naturalmente temos: $$\partial_{t}\vec{E}=-i\omega \vec{E} \quad \quad;\quad \quad \boxed{\partial_{t}^{2}\vec{E}=-\omega^{2}\vec{E}}$$
similarmente:
$$\partial_{x}\vec{E}=ik_{x}\vec{E} \quad \quad;\quad \quad \partial_{x}^{2}\vec{E}=-k_{x}^{2}\vec{E}$$
- Facilmente demonstramos:
$$\nabla \cdot \vec{E}=\partial_{x}E_{x}+\partial_{y}E_{y}+\partial_{z}E_{z}= ik_{x}E_{x}+ik_{y}E_{y}+ik_{z}E_{z}=i \vec{k}\cdot \vec{E}$$
$$\boxed{\nabla \cdot \vec{E}= i \vec{k}\cdot \vec{E}}$$
e 
$$\nabla^{2}\vec{E}=\left(\nabla^{2}E_{x},\nabla^{2}E_{y}, \nabla^{2}E_{z} \right)=\left( -k_{x}^{2}E_{x}-k_{y}^{2}E_{x}-k_{z}^{2}E_{x},\cdots, \cdots \right)= (-k^{2}E_{x},-k^{2}E_{y},-k^{2}E_{z})=-k^{2}\vec{E}$$
$$\boxed{\nabla^{2}\vec{E}=-k^{2}\vec{E}}$$
e ainda
$$\boxed{\nabla \times \vec{E}=i \vec{k}\times \vec{E}}$$
(mas esta não me apeteceu deduzir)
((As demonstrações e equações em caixas acima são diretamente aplicáveis ao campo magnético $\vec{B}$))

> Usando estas definições, vamos voltar à equação de onda: $$\begin{align*}
\nabla^{2}\vec{E}&= \frac{1}{c^{2}}\partial_{t}^{2}\vec{E}\\
-k^{2}\vec{E}&= \frac{1}{c^{2}}(-\omega^{2}\vec{E}) \\
k^{2}&= \frac{\omega^{2}}{c^{2}} ~~~~\to~~~~ \boxed{\omega=ck}
\end{align*}$$
> e aqui surge a relação entre velocidade, frequência angular e número de onda.

- Desta forma, para campos EM no vazio temos:
$$\begin{align*}
\nabla \cdot \vec{E}=0 ~~&\Longrightarrow~~ \vec{k}\cdot\vec{E}=0\\
\nabla \cdot \vec{B}=0 ~~&\Longrightarrow~~ \vec{k}\cdot\vec{B}=0
\end{align*}$$
ou seja, tanto $\vec{E}$ como $\vec{B}$ são perpendiculares a $\vec{k}$ AKA perpendiculares à direção de propagação. Daí as ondas EM serem tranversais, como dito acima.

- Podemos ainda escrever:
$$\begin{align*}
\nabla \times \vec{E}&= - \partial_{t}\vec{B}\\
i \vec{k}\times \vec{E}&= -(-i\omega \vec{B})\\
\vec{B}&= \frac{1}{\omega}\vec{k}\times \vec{\vec{E}}\\
&= \frac{k}{\omega}\hat{k}\times \vec{E}\\
&= \frac{1}{v} \hat{k}\times \vec{E} = \frac{1}{c}\hat{k}\times\vec{E}
\end{align*}$$
- Inversamente:
$$\begin{align*}
\nabla \times \vec{B}&= \frac{1}{c^{2}} \partial_{t}\vec{E}\\
i \vec{k}\times \vec{B}&= \frac{1}{c^{2}}(-i \omega \vec{E})\\
\vec{E}&= \frac{c^{2}}{\omega} \vec{k}\times \vec{B}\\
&= c^{2} \frac{k}{\omega}\hat{k}\times \vec{B}\\
&= c \hat{k}\times \vec{B}
\end{align*}$$
- Destas 2 equações temos: $B_{0}=\frac{1}{c}E_{0}\to E_{0}=cB_{0}$
- Assim, podemos escrever os campos como:
$$\vec{E}(\vec{r},t)=E_{0} e^{i(\vec{k}\cdot\vec{r}-\omega t)}\hat{n} \quad \quad;\quad \quad \vec{B}=\frac{1}{c}E_{0} e^{i(\vec{k}\cdot\vec{r}-\omega t)}(\hat{k}\times \hat{n})=\frac{1}{c}\hat{k}\times\vec{E}$$
ou seja, os campos são sempre perpendiculares.

- Tal como vimos atrás, a direção de oscilação $\hat{n}$ e respetivo campo $\vec{E}$ podem ser escritos com função das suas componentes $x,y$.
![[Attachments/FCUP/A3S1/EM2/onda EM.png]]