# Ondas EM em meios materiais
- Recordemos as equações de Maxwell na matéria:
$$\begin{align*}
\nabla \cdot \vec{D}&= \rho_{\ell}\\
\nabla \cdot \vec{B}&= 0\\
\nabla \times \vec{E}&= - \frac{\partial \vec{B}}{\partial t}\\
\nabla \times \vec{H}&= \vec{\mathcal{J}_{\ell}} + \frac{\partial \vec{D}}{\partial t}
\end{align*}$$
- Se considerarmos que não há cargas nem correntes livres no meio, as equações de Maxwell ficam:
$$\begin{align*}
\nabla \cdot \vec{D}&= 0\\
\nabla \cdot \vec{B}&= 0\\
\nabla \times \vec{E}&= - \partial_{t}\vec{B}\\
\nabla \times \vec{H}&= \partial_{t}\vec{D}
\end{align*}$$
## Meios Lineares e Isotrópicos
- Nestes temos:
$$\vec{D}=\varepsilon\vec{E}\quad\quad;\quad\quad \vec{H}=\frac{\vec{B}}{\mu}$$
- Se o meio for ainda homogéneo ($\varepsilon,\mu$ iguais em todo o meio) (e continuando a considerar que não há carga ou corrente) temos as equações de Maxwell na forma:
$$\begin{align*}
\nabla \cdot \vec{E}&= 0 &;&& \nabla \cdot \vec{B}&= 0\\
\nabla \times \vec{E}&= - \partial_{t}\vec{B} &;&& \nabla \times \vec{B}&= \mu\varepsilon \partial_{t}\vec{E}
\end{align*}$$
que é quase igual à forma que vimos inicialmente, mas com $\varepsilon_{0},\mu_{0}$ trocados por $\varepsilon,\mu$.

- Já vimos que ondas EM se movem à velocidade da luz: $$c=\frac{1}{\sqrt{\varepsilon_{0}\mu_{0}}}$$
- Ora, de forma análoga, num meio como aquele que estamos a considerar temos que a velocidade de propagação de ondas EM é dada por:
$$v=\frac{1}{\sqrt{\varepsilon\mu}}=\frac{c}{n}$$
em que definimos o **Índice de Refração** do meio:
$$n\equiv \sqrt{\frac{\varepsilon\mu}{\varepsilon_{0}\mu _{0}}}\simeq \sqrt{\varepsilon_{r}}$$
(isto é válido para o vácuo, em que temos $n=1$) (A última igualdade é válida se $\mu\approx\mu_{0}$, algo que é verdade em muitos materiais)

## Incidência Perpendicular
![[interface entre meios.png]]
- Consideremos um plano $z=0$ a separar 2 meios 1 e 2 (lineares, homogéneos e isotrópicos). Temos onda incidente a propagar-se nos zz, com o campo elétrico a oscilar em xx:
$$\vec{E_{I}}(z,t)=E_{0I}e^{i(k_{1}z-\omega t)}\hat{x}$$
as ondas refletida e transmitida serão:
$$\begin{align*}
\vec{E_{R}}(z,t)&= E_{0R}e^{i(-k_{1}z-\omega t)}\hat{x}\\
\vec{E_{T}}(z,t)&= E_{0T}e^{i(k_{2}z-\omega t)}\hat{x}
\end{align*}$$

- Logo se nota que a frequência $\omega$ nunca muda!
- Assim, uma vez que $v=\omega/k$, resulta que:
$$k_{I}v_{1}=k_{R}v_{1}=k_{T}v_{2}=\omega$$

- De acordo com as condições de fronteira descritas na caixa acima, temos:
$$\begin{cases}
E_{0I}+E_{0R}= E_{0T}\\
\frac{1}{\mu_{1}v_{1}}(E_{0I}-E_{0R})= \frac{1}{\mu_{2}v_{2}}E_{0T}
\end{cases}$$
e podemos escrever:
$$E_{0R}=\left(\frac{1-\beta}{1+\beta} \right)E_{0I} \quad,\quad E_{0T}=\left(\frac{2}{1+\beta}\right)E_{0I} \quad\quad;\quad\quad \beta\equiv\frac{\mu_{1}v_{1}}{\mu_{2}v_{2}}=\frac{\mu_{1}n_{2}}{\mu_{2}n_{1}}$$

- E se $\mu_{1}\sim\mu_{2}\sim\mu_{0}$ ficamos com $\beta=v_{1}/v_{2}$ e obtemos:
$$E_{0R}=\left(\frac{v_{2}-v_{1}}{v_{2}+v_{1}}\right)E_{0I} \quad \quad;\quad \quad E_{0T}=\left(\frac{2v_{2}}{v_{2}+v_{1}}\right)E_{0I}$$
pelo que temos equações iguais àquelas que vimos para uma onda incidente no nó a unir 2 cordas diferentes. Podemos ainda escrever:
$$E_{0R}=\left(\frac{n_{1}-n_{2}}{n_{1}+n_{2}}\right)E_{0I} \quad \quad;\quad \quad E_{0T}=\left(\frac{2n_{1}}{n_{1}+n_{2}}\right)E_{0I}$$
pelo que esta relação nos permite determinar se a onda refletida está em fase ou não com a incidente.

**Energia**
- Conforme vimos na aula anterior, podemos definir a intensidade energética de uma onda como: $I=\frac{1}{2}\varepsilon vE_{0}^{2}$. 
- O **Coeficiente de Reflexão** consiste na porção de intensidade da onda incidente que é refletida:
$$R\equiv\frac{I_{R}}{I_{I}}=\left(\frac{E_{0R}}{E_{0I}}\right)^{2}=\left(\frac{n_{1}-n_{2}}{n_{1}+n_{2}}\right)^{2}$$
e o **coeficiente de transmissão** é a porção de intensidade que é transmitida:
$$T\equiv\frac{I_{T}}{I_{I}}=\frac{\varepsilon_{2}v_{2}}{\varepsilon_{1}v_{1}}\left(\frac{E_{0T}}{E_{0I}}\right)^{2}=\frac{4n_{1}n_{2}}{(n_{1}+n_{2})^{2}}$$
sendo que devido à conservação de energia temos que ter:
$$R+T=1$$

## Incidência na diagonal
![[onda a incidir na diagonal.png]]
- Assim surge uma questão: o que acontece quando uma onda EM plana e monocromática indice numa superfície plana que separa 2 meios 1 e 2 (ambos lineares, homogéneos e isotrópicos)?
- Em cima temos a situação em estudo, em que as ondas incidente, transmitida e refletida são representadas pelo seu vetor de onda $\vec{k}$. 
- Tal como já vimos atrás, na superfície de interseção entre os 2 meios teremos:
$$\boxed{\begin{align*}
\varepsilon_{1}E_{1}^{\perp}&= \varepsilon_{2}E_{2}^{\perp} &;&& \vec{E}_{1\parallel}&= \vec{E}_{2\parallel}\\
B_{1}^{\perp}&= B_{2}^{\perp} &;&& \frac{1}{\mu_{1}}\vec{B}_{1\parallel}&= \frac{1}{\mu_{2}}\vec{B}_{2\parallel}
\end{align*}}$$

- Considerando a onda incidente como sendo plana, com polarização linear, frequência $\omega$, velocidade de propagação $v_{I}$:
$$\begin{align*}
\vec{E_{I}}(t,\vec{r})&= \vec{E}_{0I}e^{i(\vec{k_{I}}\cdot\vec{r}-\omega t)}\\
\vec{B_{I}}(t, \vec{r})&= \frac{1}{v_{I}} \hat{e_{k_{I}}}\times \vec{E_{I}}
\end{align*}$$

esta equação *geral* será igual para a onda transmitida e refletida, trocando apenas $k_{I}\to k_{R},k_{T}$.

- Tal como na incidência normal, a frequência é a mesma para todas as ondas, pelo que:
$$k_{I}v_{1}=k_{R}v_{1}=k_{T}v_{2}=\omega$$

- Por uma questão de continuidade (e conforme mostrado nas condições de fronteira na caixa acima) a soma vetorial dos campos no meio 1 e 2 tem que ser nula. Ou seja, em $z=0$ temos que ter:
$$\vec{E_{I}}+\vec{E_{R}}=\vec{E_{T}}$$
e igualmente para os campos magnéticos.
- E podemos escrever essa continuidade como:
$$\vec{k_{I}}\cdot \vec{r}=k_{R}\cdot\vec{r}=\vec{k_{T}}\cdot\vec{r} \quad \quad;\quad z=0$$
$$xk_{Ix}+yk_{Iy}=xk_{Rx}+yk_{Ry}=xk_{Tx}+yk_{Ty}$$
pelo que apenas podemos verificar esta equação se:
$$\begin{align*}
k_{Ix}=k_{Rx}=k_{Tx}\\
k_{Iy}=k_{Ry}=k_{Ty}
\end{align*}$$

## Leis da Ótica Geométrica
**1.** Os vetores de onda $\vec{k_{I}},\vec{k_{R}},\vec{k_{T}}$ formam o **plano de incidência**.
**2.** Vimos acima que $k_{Iy}=k_{Ry}\to k_{I}\sin\theta_{I}=k_{R}\sin\theta_{R}$. Como a onda incidente e refletida existem no mesmo meio fica $k_{I}=k_{R}$ e temos: $$\theta_{I}=\theta_{R}$$
(sendo estes os ângulos de incidência e de reflexão)
**3.** Como $k_{Iy}=k_{Ty}$ resulta:
$$\frac{\sin\theta_{T}}{\sin\theta_{I}}=\frac{n_{1}}{n_{2}}=\frac{k_{I}}{k_{T}}=\frac{v_{2}}{v_{1}}$$
aka **LEI DE SNELL** :D

- Como não definimos condições de fronteira específicas, estas 3 leis são genéricas e qualquer tipo de onda deverá segui-las.

### Condições de fronteira
- Partindo das condições de fronteira genéricas da caixa acima, podemos determinar as condições de fronteira das amplitudes deste problema (com plano de incidência a ser $z=0$):
$$\begin{align*}
(\text{i})&&\varepsilon_{1}(E_{0Iz}+E_{0Rz})&= \varepsilon_{2}E_{0Tz}\\
(\text{ii})&&E_{0Ix}+E_{0Rx}&= E_{0Tx} &&(\text{ou }y)\\
(\text{iii})&&(B_{0Iz}+B_{0Rz})&= B_{0Tz}\\
(\text{iv})&&\frac{1}{\mu_{1}}(B_{0Ix}+B_{0Rx})&= \frac{1}{\mu_{2}}B_{0Tx} &&(\text{ou }y)
\end{align*}$$
em que $\vec{B}_{0}=\frac{1}{v}\hat{k}\times\vec{E_{0}}$. E torna-se portanto útil recordar que estes $E_{0},B_{0}$ são todos números que podem ser complexos.

## Polarização paralela ao plano incidência 
![[onda a incidir na diagonal - polarizacao.png]]
- Da condição de fronteira (i) temos:
$$\varepsilon_{1}(-E_{0I}\sin\theta_{I}+E_{0R}\sin\theta_{R})=\varepsilon_{0}(-E_{0T}\sin\theta_{T})~~\Longrightarrow~~ E_{0I}-E_{0R}= \underbrace{\frac{\varepsilon_{2}}{\varepsilon_{1}} \frac{\sin\theta_{T}}{\sin\theta_{I}}}_{\beta}E_{0T}$$
- A condição (ii) resulta em (aqui escrevemos as componentes em função de $x$ porque é a direção que os ângulos $\theta$ nos dão):
$$E_{0I}\cos\theta_{I}+E_{0R}\cos\theta_{0R}=E_{0T}\cos\theta_{T}~~\Longrightarrow~~ E_{0I}+E_{0R}=\underbrace{\frac{\cos\theta_{T}}{\cos\theta_{I}}}_{\alpha}E_{0T}$$
em que definimos as constantes:
$$\begin{align*}
\alpha&= \frac{\cos\theta_{T}}{\cos\theta_{I}}=\frac{\sqrt{1-\sin^{2}\theta_{T}}}{\cos\theta_{I}}=\frac{\sqrt{1-\left(\frac{n_{1}}{n_{2}}\right)^{2}\sin^{2}\theta_{I}}}{\cos\theta_{I}}\\\\
\beta&= \frac{\varepsilon_{2}\sin\theta_{T}}{\varepsilon_{1}\sin\theta_{I}}=\frac{\varepsilon_{2}n_{1}}{\varepsilon_{1}n_{2}}=\frac{\varepsilon_{2}}{\varepsilon_{1}} \frac{\sqrt{\varepsilon_{1}\mu_{1}}}{\sqrt{\varepsilon_{2}\mu_{2}}}=\sqrt{\frac{\mu_{1}\varepsilon_{2}}{\mu_{2}\varepsilon_{1}}} =_{(\mu_{1}=\mu_{2})}\sqrt{\frac{\varepsilon_{2}}{\varepsilon_{1}}}=\frac{n_{2}}{n_{1}}
\end{align*}$$
pelo que $\alpha$ depende do ângulo de incidência e $\beta$ apenas das caraterísticas dos meios. De notar que, tal como dito acima, é comum em muitos materiais termos $\mu_{1}\approx\mu_{2}$.

- E podemos escrever:
$$\boxed{E_{0R}=\frac{\alpha-\beta}{\alpha+\beta}E_{0I} \quad \quad;\quad \quad E_{0T}=\frac{2}{\alpha+\beta}E_{0I}}$$
em que estas são as **_Equações de Fresnel_** !!!

- Se $\theta_{I}=0$ temos o caso de incidência perpendicular que vimos atrás e resulta $\alpha=1, \theta_{I}=\theta_{T}=0$.
- Se $\theta_{I}=\frac{\pi}{2}$ temos $\theta_{T}=\arcsin\left(\frac{n_{1}}{n_{2}}\right)=_{(\mu_{1}=\mu_{2})}\arcsin\left(\frac{1}{\beta}\right)$.

- Temos ainda um ângulo intermédio, **Ângulo de Bewster** $\theta_{B}$ em que ocorre transmissão total do feixe e temos $\alpha=\beta$. Para esse ângulo apenas sobrevive a polarização perpendicular ao plano de incidência.

- Para $\alpha=\beta$  e $\mu_{1}=\mu_{2}$ temos, das suas definições:
$$\begin{align*}
\alpha&= \beta\\
\frac{\cos\theta_{T}}{\cos\theta_{I}}&= \frac{n_{2}}{n_{1}}\\
n_{1}\cos\theta_{T}&= n_{2}\cos\theta_{I}
\end{align*}$$
e temos a lei de Snell:
$$n_{1}\sin\theta_{I}=n_{2}\sin\theta_{T}$$
- Ora, estas 2 equações apenas são iguais se:
$$\theta_{T}=\frac{\pi}{2}-\theta_{I} ~~~~\Longrightarrow~~~~ \theta_I =\theta_{B}$$
- Assumindo que $\mu_{1}=\mu_{2}$, no ângulo de Brewster temos:
$$\begin{align*}
\alpha&= \beta\\
\frac{\sqrt{1-\left(\frac{n_{1}}{n_{2}}\right)^{2}\sin^{2}\theta_{B}}}{\cos\theta_{B}}&= \beta\\
\frac{\sqrt{1-\left(\frac{1}{\beta}\right)^{2}\sin^{2}\theta_{B}}}{\cos\theta_{B}}&= \beta\\
1- \frac{1}{\beta^{2}}\sin^{2}\theta_{B}&= \beta^{2}\cos^{2}\theta_{B}\\
1- \frac{1}{\beta^{2}}\sin^{2}\theta_{B}&= \beta^{2}-\beta^{2}\sin^{2}\theta_{B}\\
\sin^{2}\theta_{B}\left(\beta^{2}-\frac{1}{\beta^{2}}\right)&= \beta^{2}-1\\
\sin^{2}\theta_{B}&= (\beta^{2}-1)\left(\frac{\beta^{2}}{\beta^{4}-1} \right)=\frac{\beta^{2}}{1+\beta^{2}}
\end{align*}$$
daqui podemos ainda escrever:
$$\tan\theta_{B}\simeq \frac{n_{2}}{n_{1}}$$
- Para $n_{1}=1,n_{2}=1.5$ (vidro) pode-se traçar o seguinte gráfico:
![[Attachments/FCUP/A3S1/EM2/angulo de brewster.png]]
