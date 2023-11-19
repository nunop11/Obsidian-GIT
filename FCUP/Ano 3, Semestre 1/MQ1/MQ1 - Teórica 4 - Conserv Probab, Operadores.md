## Lei de Conservação de Probabilidade
- A equação de Schrödinger preserva a condição de normalização: $\int |\Psi|^{2}=1$
- Consideremos uma partícula confinada no volume abaixo:
![[volume V arbitrario.png|450]]
ora, $\int |\Psi|^{2}=1$ apenas significa que a probabilidade de encontrar esta partícula *algures* no volume $\mathcal{V}$ é $1$. Como ela está *confinada* a este volume, se passar qualquer quantidade de tempo a condição de normalização terá de se manter verdadeira. Assim:
$$\int_\mathcal{V} d^{3}r|\Psi|^{2}=1 \quad \longrightarrow \quad \frac{d}{dt}\int_\mathcal{V}d^{3}r |\Psi(\vec{r}, t)|^{2}=0$$

- Ora, podemos passar a derivada temporal para dentro do integral (porque não irá variar com a posição). E temos que $|\Psi|^{2}=\Psi^{*}\Psi$ (em que $\Psi^{*}$ é o conjugado). Assim:
$$\begin{align*}
\frac{d}{dt}\int_\mathcal{V}d^{3}r |\Psi(\vec{r}, t)|^{2}&= \int_\mathcal{V} d^{3}r \frac{\partial}{\partial t}|\Psi(\vec{r}, t)|^{2}\\
&= \int_\mathcal{V} d^{3}r \left(\Psi^{*} \frac{d \Psi}{dt} + \Psi \frac{d \Psi^{*}}{dt}\right)
\end{align*}$$
 em que usamos a chainrule e a definição $|\Psi|^{2}$ acima.

- Temos a equação de Schrödinger:
$$i\hbar \frac{\partial \Psi}{\partial t}=\frac{-\hbar^{2}}{2m} \Delta \Psi + V \Psi$$
em que $\Delta=\nabla \cdot \nabla$ e podemos escrever como:
$$\frac{\partial \Psi}{\partial t}=\frac{i\hbar}{2m} \nabla \cdot \nabla \Psi - \frac{i}{\hbar}V \Psi$$
e para o conjugado temos:
$$\frac{\partial \Psi^{*}}{\partial t}=-\frac{i\hbar}{2m} \nabla \cdot \nabla \Psi^{*} + \frac{i}{\hbar}V \Psi^{*}$$
(Isto porque temos $H \Psi=E \Psi$, enquanto que temos $H \Psi^{*}= - E \Psi^{*}$)

- Se substituirmos na equação acima:
$$\begin{align*}
\int_\mathcal{V} d^{3}r \left(\Psi^{*} \frac{d \Psi}{dt} + \Psi \frac{d \Psi^{*}}{dt}\right) &= \int_\mathcal{V}d^{3}r \left[ \Psi^{*}\left(\frac{i\hbar}{2m} \nabla \cdot \nabla \Psi - \frac{i}{\hbar}V \Psi\right) + \Psi\left(-\frac{i\hbar}{2m} \nabla \cdot \nabla \Psi^{*} + \frac{i}{\hbar}V \Psi^{*}\right)  \right]\\
&= \int_\mathcal{V}d^{3}r \left[ \frac{i\hbar}{2m} \Psi^{*} \nabla \cdot \nabla \Psi - \bcancel{\frac{i}{\hbar}V\Psi\Psi^{*}} - \frac{i\hbar}{2m}\Psi \nabla \cdot \nabla \Psi^{*} + \bcancel{\frac{i}{\hbar} V \Psi^{*}\Psi}  \right]\\
&= \frac{i\hbar}{2m}\int_\mathcal{V}d^{3}r \left(\Psi^{*}\nabla \cdot \nabla \Psi - \Psi\nabla \cdot \nabla \Psi^{*} \right)\\
\end{align*}$$
ora, temos uma equação que podemos aplicar aqui: $\nabla \cdot (f \nabla g)=\nabla f \cdot \nabla g + f \nabla \cdot  \nabla g$. Ora, isto dá-nos que $f \nabla \cdot  \nabla g= \nabla \cdot (f \nabla g) - \nabla f \cdot \nabla g$. Assim temos:
$$\begin{align*}
\Psi^{*} \nabla \cdot \nabla \Psi &= \nabla \cdot (\Psi^{*}\nabla \Psi) - \nabla \Psi^{*}\nabla \Psi\\
\Psi \nabla \cdot \nabla \Psi^{*} &= \nabla \cdot (\Psi\nabla \Psi^{*}) - \nabla \Psi\nabla \Psi^{*}\\
\end{align*}$$
ao substituir acima:
$$\begin{align*}
\frac{i\hbar}{2m}\int_\mathcal{V}d^{3}r \left(\Psi^{*}\nabla \cdot \nabla \Psi - \Psi\nabla \cdot \nabla \Psi^{*} \right)&= \frac{i\hbar}{2m}\int_\mathcal{V}d^{3}r \left( \nabla \cdot (\Psi^{*}\nabla \Psi) - \bcancel{\nabla \Psi^{*}\nabla \Psi} - \nabla \cdot (\Psi\nabla \Psi^{*}) + \bcancel{\nabla \Psi\nabla \Psi^{*}} \right)\\
&= \frac{i\hbar}{2m} \int_\mathcal{V}d^{3}r \nabla \cdot (\Psi^{*}\nabla\Psi-\Psi\nabla\Psi^{*})\\
&\equiv \int_\mathcal{V} d^{3}r \nabla \cdot \vec{\mathcal{J}}=-\int_\mathcal{S}ds \vec{\mathcal{J}}\cdot \hat{n}
\end{align*}$$
em que $\vec{\mathcal{J}}=\frac{i\hbar}{2m} (\Psi^{*}\nabla\Psi-\Psi\nabla\Psi^{*})$ é o **_Vetor Corrente de Probabilidade_**

- Assim, igualando este resultado final ao termo com que começamos esta equação temos:
$$\frac{d}{dt}\int_\mathcal{V}d^{3}r |\Psi(\vec{r}, t)|^{2}=-\int_\mathcal{S}ds \vec{\mathcal{J}}\cdot \hat{n}$$
ora, vimos acima que o termo da direita tem que ser nulo, para uma partícula confinada num volume. Aqui isso faz sentido, pois temos que o fluxo da corrente de probabilidade pela superfície do volume tem que ser nulo. 


- Consideremos agora um volume $v$ dentro de $\mathcal{V}$ com superfície $s=\partial v$:
![[volume V com volume v dentro.png|450]]
- Ao aplicar a equação acima temos:
$$\frac{d}{dt}\int_\mathcal{v}d^{3}r |\Psi(\vec{r}, t)|^{2}=-\int_\mathcal{s}ds \vec{\mathcal{J}}\cdot \hat{n}$$
ora, a partícula está confinada a $\mathcal{V}$, não a $v$. Assim, faz sentido que agora não tenhamos o lado esquerdo nulo: isto simplesmente significa que a probabilidade de encontrarmos a partícula em $v$ varia consoante a posição e direção de movimento da mesma e, portanto, nem sempre será $0$. Assim, também o fluxo de probabilidade por $s$ não será necessariamente nulo.

- No entanto, $v$ deverá ser um volume arbitrário. Ou seja, se reduzirmos $v$ imenso, eventualmente vemos que a **Lei de Conservação de Probabilidade** é *local*:
$$\frac{\partial}{\partial t}|\Psi(\vec{r},t)|^{2}=- \nabla \cdot \vec{\mathcal{J}}$$

# Operadores
- Um operador $\hat{O}$ corresponde a um observável $O$ que tem valor médio $\langle O\rangle$

## Posição
- Temos que (ver coisas de FESTA) o valor médio de uma variável $x$ é $\langle x\rangle=\int dx~x\rho(x)$ em que $\rho(x)$ é a densidade de probabilidade. Assim, para uma partícula temos:
$$\langle \vec{r}\rangle= \int_\mathcal{V}d^{3}r ~\vec{r}|\Psi(\vec{r},t)|^{2} \quad \quad \longrightarrow \quad \quad \langle x^{k}\rangle=\int_{\mathcal{V}} d^{3}r~x^{k}|\Psi(\vec{r},t)|^{2}$$
- Assim, como $\langle x^{k}\rangle=\int_{\mathcal{V}} d^{3}r~x^{k}|\Psi(\vec{r},t)|^{2}=\int_\mathcal{V}d^{3}r \Psi^{*} (x^{k}) \Psi$ temos o **operador posição**: $$\hat{X^{k}}=x^{k}$$ 

## Momento
- Vejamos como é que a posição média varia no tempo:
$$\begin{align*}
\frac{d}{dt} \langle x^{k}\rangle &= \int d^{3}r~x^{k} \frac{d}{dt}|\Psi(\vec{r},t)|^{2}\\
&= \int d^{3}r~x^{k} \frac{i\hbar}{2m} \nabla^{\ell} \cdot (\Psi^{*}\nabla^{\ell}\Psi - \Psi\nabla^{\ell}\Psi^{*})
\end{align*}$$
em que se repete todo o processo da dedução acima do 1º para o 2º passo (substituir $\Psi$ com a equação de Schrödinger, usar chainrule e usar fórmula). Notemos ainda que $\nabla_{\ell}$ representa apenas a derivada parcial na componente $\ell$. Deixou-se o nabla não sei muito bem porquê.
- Usemos agora integração por partes: $\int f \frac{dg}{dx}dx=-\int \frac{df}{dx} g dx+fg|_{a}^{b}$ em que $f=x^{k}, g=\Psi^{*}\nabla^{\ell}\Psi - \Psi\nabla^{\ell}\Psi^{*}$. O último termo anula-se e ficamos com:
$$\begin{align*}
\frac{d}{dt} \langle x^{k}\rangle &= - \frac{i\hbar}{2m} \int d^{3}r \frac{\partial x^{k}}{\partial x^{\ell}}(\Psi^{*}\nabla^{\ell}\Psi - \Psi\nabla^{\ell}\Psi^{*})\\
&= - \frac{i\hbar}{2m} \int d^{3}r \delta_{\ell}^{k}(\Psi^{*}\nabla^{\ell}\Psi - \Psi\nabla^{\ell}\Psi^{*})\\
\end{align*}$$
em que temos que $\frac{\partial x^{k}}{\partial x^{\ell}}$ vai atuar como um Delta de Kronecker, daí escrever $\frac{\partial x^{k}}{\partial x^{\ell}}=\delta_{\ell}^{k}$. Ficamos então com:
$$\begin{align*}
\frac{d}{dt} \langle x^{k}\rangle &= - \frac{i\hbar}{2m} \int d^{3}r \left(\Psi^{*} \frac{\partial \Psi}{\partial x^{k}} - \Psi \frac{\partial \Psi^{*}}{\partial x^{k}}\right)\\
&= - \frac{i\hbar}{m} \int d^{3}r \Psi^{*} \frac{\partial \Psi}{\partial x^{k}}\\
&= \int d^{3}r \Psi^{*} \left(- \frac{i\hbar}{m}\frac{\partial}{\partial x^{k}}\right) \Psi = \langle v^{k}\rangle
\end{align*}$$
que é, portanto a velocidade média. Assim temos o operador velocidade $\hat{V}^{k}=-\frac{i \hbar}{m} \frac{\partial}{\partial x^{k}}$ 

- Ora, com a equação acima facilmente obtemos o valor médio do momento:
$$\langle p^{k}\rangle =m \langle v^{k}\rangle =\int d^{3}r \Psi^{*} \left(-i\hbar \frac{\partial}{\partial x^{k}}\right)\Psi$$
pelo que temos o **Operador Momento**: $$\hat{P}^{k}=-i\hbar \frac{\partial}{\partial x^{k}}=\frac{\hbar}{i} \frac{\partial}{\partial x^{k}}\equiv \frac{\hbar}{i} \nabla$$

> **EXEMPLO**
> - Vejamos como podemos obter o operador *energia cinética* usando os operadores acima.
> - A energia cinética é $T=\frac{p^{2}}{2m}=\frac{p^{k}p^{k}}{2m}$, pelo que o operador será:
> $$\hat{T}=- \frac{\hbar^{2}}{2m} \frac{\partial}{\partial x^{k}} \frac{\partial}{\partial x^{k}}=- \frac{\hbar^{2}}{2m} \Delta$$
> pelo que vemos que o operador Hamiltoniano é: $\hat{H}= \hat{T}+V$. Daí temos: $\hat{H}\Psi= E \Psi$ na equação de Schrödinger.
>
> - Podemos ainda determinar o operador *momento angular*:
> - Temos $\vec{L}=\vec{r}\times \vec{p}$. Ou seja temos: $L^{i}=\varepsilon^{ijk} x^{j} p^{k}$, tendo-se o operador: $\hat{L}=\frac{\hbar}{i} \varepsilon^{ijk} x^{j} \frac{\partial}{\partial x^{k}}$

- De uma forma geral, podemos escrever operadores utilizando os operadores posição e momento. Com eles, facilmente obtemos o valor médio do observável correspondente:
$$\langle O(\vec{r},\vec{p})\rangle=\int d^{3}r ~\Psi^{*} O\left(\vec{r},\frac{\hbar}{i} \nabla\right)\Psi $$

## Teorema de Ehrenfest
- Temos que $F=\frac{dp}{dt}$. Elaboremos então a partir do valor médio de $p$ que obtivemos acima:
$$\begin{align*}
\frac{d}{dt}\langle p^{k}\rangle &= \frac{d}{dt}\int d^{3}r ~\Psi^{*} \left(\frac{\hbar}{i} \frac{\partial}{\partial x^{k}}\right) \Psi\\
&= \int d^{3}r~ \left(\frac{\partial \Psi^{*}}{\partial t}\frac{\partial \Psi}{\partial x^{k}} + \Psi^{*} \frac{\partial}{\partial x^{k}} \frac{\partial \Psi}{\partial t}\right)
\end{align*}$$
em que se usou $\frac{d}{dt}(fg)=\frac{df}{dt}g+f \frac{dg}{dt}$ com $f=\Psi^{*}, g=\frac{\partial \Psi}{\partial x^{k}}$.
- Agora, tal como fizemos acima, usamos a equação de Schrödinger para substituir: $\frac{\partial \Psi}{\partial t}=\frac{i\hbar}{2m} \Delta \Psi - \frac{i}{\hbar}V \Psi$  ;  $\frac{\partial \Psi^{*}}{\partial t}=-\frac{i\hbar}{2m} \Delta \Psi^{*} + \frac{i}{\hbar}V \Psi^{*}$
$$\begin{align*}
\frac{d}{dt}\langle p^{k}\rangle &= \int d^{3}r \left[ \left(-\frac{i\hbar}{2m} \Delta \Psi^{*} + \frac{i}{\hbar}V \Psi^{*}\right)\frac{\partial \Psi}{\partial x^{k}} + \Psi^{*} \frac{\partial}{\partial x^{k}}\left(\frac{i\hbar}{2m} \Delta \Psi - \frac{i}{\hbar}V \Psi\right) \right]\\
&= \int d^{3}r ~\Psi^{*} \left(- \frac{\partial V}{\partial x^{k}}\right) \Psi
\end{align*}$$
sendo que não percebi como passamos da 1ª para a 2ª linha.
- Temos então o **_Teorema de Ehrenfest_**:
$$\frac{d}{dt} \langle p^{k}\rangle= \left\langle - \frac{\partial V}{\partial x^{k}}\right\rangle $$
sendo que podemos chamar a este o **Operador Força**.

# 2.2 - Partícula Livre
- Uma partícula livre é uma partícula existente num espaço em que: $V(\vec{r},t)=0$. Assim, a equação de Schrödinger fica do tipo:
$$i\hbar \frac{\partial \Psi}{\partial t}=- \frac{\hbar^{2}}{2m} \Delta \Psi$$
sendo que a solução da equação diferencial é $$\Psi_{k}(\vec{r},t)=A e^{i(\vec{k}\cdot\vec{r}-\omega t)}~~~~~~;~~~~\omega\equiv \omega(k)=\frac{\hbar k^{2}}{2m}~~~~(k=|\vec{k}|)$$

- Ora, partindo das relações de De Broglie: $E=\omega\hbar~,~ p=\hbar k$ e temos _para uma particula livre_:
$$\frac{E}{\hbar}=\omega=\frac{\hbar k^{2}}{2m}=\frac{p^{2}}{2m \hbar}$$
e isto dá-nos que: $E=\frac{p^{2}}{2m}$, que é o que temos num sistema clássico.

### Momento 
- Voltemos agora ao operador momento linear:
$$\hat{P}^{j}=\frac{\hbar}{i} \frac{\partial}{\partial x^{j}}$$
que nos dá, para uma partícula livre:
$$\hat{P}^{j}\Psi=\hat{P}^{j} \Psi_{k}(\vec{r},t)=\frac{\hbar}{i} \frac{\partial}{\partial x^{j}} \Psi_{k}(\vec{r},t)=\hbar k^{j} \Psi_{k}(\vec{r},t)$$
- Ou seja, a solução da equação de Schrödinger $\Psi_{k}$ é uma função/estado próprio do observável momento linear com valor próprio $\hbar k$.

## Paradoxo?
- Temos que, numa onda, um ponto fixo é descrito pela fase $\vec{k}\cdot\vec{r}-\omega t$. Esta viajará com velocidade de fase  $$v_{fase}=\frac{\omega}{k}=\frac{E}{p}=\frac{p}{2m}=\frac{v_{classica}}{2}$$
- De notar que a *velocidade de fase* é a velocidade com que uma ponto/região da onda com fase específica se desloca no espaço.
- Ou seja temos 2 problemas:
**Problema 1**
A particula viaja com velocidade de fase  igual a metade da velocidade clássica. Ou seja, viaja com velocidade igual a metade do *valor esperado* de velocidade.

**Problema 2**
Com a solução da equação de onda para a partícula livre que vimos acima, a função de onda não está normalizada em $\mathbb{R}^{3}$:
$$\int d^{3}r |\Psi|^{2}=|A|^{2}\int d^{3}r\to\infty $$

- Ou seja, $\Psi_{k}(\vec{r},t)$ não pode representar um estado físico!!