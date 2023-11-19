- Tal como vimos na aula anterior, para uma partícula livre temos:
    - Equação de Schrödinger: $$i\hbar \frac{\partial \Psi}{\partial t}=- \frac{\hbar^{2}}{2m} \Delta \Psi$$
    - Solução geral da equação de Schrödinger: $$\psi_{\vec{k}}=A e^{i(\vec{k}\cdot \vec{r}- \omega t)} \quad \quad;\quad \omega=\omega(k)=\frac{\hbar k^{2}}{2m}$$ 
    - E temos ainda o valor médio do momento de uma partícula livre: $$\hat{P}^{j}\psi_{\vec{k}}=\frac{\hbar}{i} \frac{\partial}{\partial x^{j}}\psi_{\vec{k}}=\hbar k^{j} \psi_{\vec{k}}$$
    ou seja, $\psi_{\vec{k}}$ é uma auto função de $\langle p\rangle$, com o autovalor $\hbar k^{j}$
    - Por fim, vimos que a velocidade de fase desta partícula será: $$v_{fase}=\frac{\omega}{k}=\frac{p}{2m}=\frac{v_{classica}}{2}$$
    - Ou seja, concluímos que o estado descrito acima para uma partícula livre é **fisicamente impossível**.

- Ora, veremos agora que estes estados, embora impossíveis, são úteis porque uma solução geral da equação de Schrödinger pode ser escrita como uma combinação linear de estados "de partículas livres".

- Tendo uma função de onda $\Psi(\vec{r},t)$, podemos escrever a sua transformada de Fourier:
$$\Psi(\vec{r},t)=\int \frac{d^{3}k}{\sqrt{2\pi}} \tilde \Psi(\vec{k}) e^{i(\vec{k}\cdot \vec{r}-\omega t)}=\int \frac{d^{3}k}{\sqrt{2\pi}} \tilde \Psi(\vec{k}) e^{i(\vec{k}\cdot \vec{r}- \frac{\hbar k^{2}}{2m} t)}$$
que, na prática, representa a sobreposição de muiiiitos estados com $\vec{k}$'s diferentes. A estas combinações chama-mos de **trem de ondas**.

- Geralmente, em exercícios, iremos saber $\Psi(\vec{r},0)$ e queremost determinar $\Psi(\vec{r},t)$. Assim, temos em termos de Fourier: $$\Psi(\vec{r},0)=\int \frac{d^{3}k}{\sqrt{2\pi}} \tilde \Psi(\vec{k}) e^{i(\vec{k}\cdot \vec{r})}$$

**_Teorema de Plancherel_**
$$\int_{-\infty}^{+\infty} |f(x)|^{2}dx=\int_{-\infty}^{+\infty} |f(k)|^{2}dk$$
sendo $f(k)$ a transformada de Fourier de $f(x)$. Na prática, isto diz-nos que se $\Psi(x)$ estiver normalizada, a sua transformada de Fourier também estará. A condição necessária e suficiente para que isto se verifique é que $\Psi(x)$ seja normalizável: $\int |\Psi|^{2}dx=$ finito.

**_Teorema de Parseval_**
$$\int \frac{d^{3}r}{\sqrt{2\pi}}f(\vec{r}) g^{*}(\vec{r})=\int \frac{d^{3}k}{\sqrt{2\pi}} \tilde f(k) \tilde g^{*}(k)$$
que se aplica à equação de onda e ao teorema de Plancherel no caso em que $f=g=\Psi$

## Velocidade de Grupo
- Queremos determinar a velocidade do trem de ondas de forma: $$\Psi(\vec{r},t)=\int \frac{d^{3}r}{\sqrt{2\pi}} \tilde \Psi(\vec{k}) e^{i(\vec{k}\cdot \vec{r}-\omega t)} \quad \quad;\quad \omega=\omega(k)$$
- Ora, o trem de ondas será uma função que oscila em torno de um envelope. Ora, a velocidade da partícula irá então corresponder à propagação do envelope e **não** com as oscilações em si.
![[Onda e envelope.png|500]]

- Assim, a transformada de Fourier $\tilde \Psi(\vec{k})$ vai ser uma função localizada em torno de um máximo $k_{0}$. Na realidade podia ter mais que 1 máximo, mas nesse caso a partícula podia ter mais velocidades, algo que não pretendemos estudar agora.
- Assim, vamos fazer expansão em série de Taylor de $\omega(\vec{k})$ em torno de $\vec{k}_{0}$:  $$\omega(\vec{k})=\omega(\vec{k}_{0}) + \frac{\partial \omega}{\partial k^{i}}\biggr|_{\vec{k}=\vec{k}_{0}} (k^{i}-k_{0}^{i})+\cdots$$
para simplificar a notação vamos substituir $\omega(\vec{k}_{0})=\vec{\omega}_{0}$ e $\frac{\partial \omega}{\partial k^{i}}|_{\vec{k}=\vec{k}_{0}}=\omega_{0}^{'i}$. Temos:
$$\begin{align*}
\omega(\vec{k})&= \vec{\omega_{0}} + \omega_{0}^{'i}(k^{i}-k_{0}^{i})\\
\omega(\vec{k})&= \vec{\omega_{0}} + \omega^{'i}_{0}s^{i} \quad \quad \quad \quad;\quad \quad s^{i}=k^{i}-k_{0}^{i}
\end{align*}$$
e ficamos com 
$$\Psi(\vec{r},t)\simeq \int \frac{d^{3}s}{\sqrt{2\pi}} \tilde \Psi(\vec{k_{0}}+\vec{s}) e^{i\left[ (\vec{k_{0}}+\vec{s})\cdot \vec{r} -(\vec{\omega_{0}}+ \omega_{0}^{'i}s^{i})t\right]}$$
- Podemos fazer as seguintes reorganizações no termo da exponencial:
$$e^{i\left[ (\vec{k_{0}}+\vec{s})\cdot \vec{r} -(\vec{\omega_{0}}+ \omega_{0}^{'i}s^{i})t\right]}=e^{i\left[ (\vec{k_{0}}+\vec{s})\cdot \vec{r} -(\vec{\omega_{0}}+ \vec{\omega'}\cdot \vec{s})t\right]}=e^{i(-\vec{\omega_{0}}t)} e^{i\left[ (\vec{k_{0}}+\vec{s})\cdot \vec{r} - \vec{\omega'_{0}}\cdot (\vec{k}- \vec{k_{0}}) t\right]}=e^{i(-\vec{\omega_{0}}t+ \vec{\omega'_{0}} \cdot \vec{k_{0}}t)}e^{i\left[ (\vec{k_{0}}+\vec{s})\cdot \vec{r} - \vec{\omega'_{0}}\cdot \vec{k} t\right]}$$
temos
$$\Psi(\vec{r},t)\simeq e^{i(-\vec{\omega_{0}}t+ \vec{\omega'_{0}} \cdot \vec{k_{0}}t)}\int \frac{d^{3}s}{\sqrt{2\pi}} \tilde \Psi(\vec{k_{0}}+\vec{s}) e^{i\left[ (\vec{k_{0}}+\vec{s})\cdot \vec{r} - \vec{\omega'_{0}}\cdot \vec{k} t\right]}$$
- Se considerarmos o isntante $t=0$ ficamos com:
$$\Psi(\vec{r},0)=\int \frac{d^{3}k}{\sqrt{2\pi}} \tilde \Psi(\vec{k_{0}}+\vec{s})e^{i(\vec{k_{0}}\cdot\vec{s})}$$
e podemos escrever:
$$\Psi(\vec{r},t)\simeq e^{i(-\omega_{0}t+ \vec{k_{0}}\cdot\vec{\omega_{0}'}t)} \Psi(\vec{r}-\vec{\omega_{0}'}t,0)$$
estando a equação normalizada temos:
$$|\Psi(\vec{r},t)|^{2}=|\Psi(\vec{r}- \vec{\omega_{0}'}t,0)|^{2}$$
e temos que a **velocidade de grupo** é $$\vec{\omega_{0}'}=\frac{\partial \omega}{\partial k^{i}}\biggr|_{\vec{k}=\vec{k_{0}}}=\frac{\hbar k_{0}^{i}}{m}=\frac{p_{0}^{i}}{m}$$
que já coincide com a velocidade clássica!
- Ora, a velocidade de grupo é a velocidade com que a onda de probabilidade se move. Assim, o movimento de uma partícula num sistema quântico é descrito pela velocidade de Grupo/comportamento da onda em si; não pela velocidade de Fase/comportamento de uma secção da onda.

# 2.3 - Princípio de Incerteza de Heisenberg
- Para simplificar a notação e escrever menos, vejamos a transformada de Fourier de $\Psi$ em $t=0$ em 1 dimensão:
$$\Psi(k)=\int \frac{dk}{\sqrt{2\pi}} \tilde \Psi(k) e^{ikx}$$
em que podemos escrever: $\tilde \Psi(k)=|\tilde \Psi(k)|e^{i \alpha(k)}$. 
- Vamos assumir que 
    - A amplitude da transformada não varia muito, estando a função $|\tilde \Psi(k)|$ localizada / muito concentrada na região $[k_{0}- \frac{\Delta k}{2}, k_{0}+ \frac{\Delta k}{2}]$
    - A fase $\alpha(k)$ varia lentamente. Caso contrário $\Psi$ varia de $\Psi_0$ para $-\Psi_{0}$ muito rapidamente, o que acabaria por tornar $\int dk \tilde \Psi(k)\to0$

- Teremos então algo do tipo:
![[Transformada Fourier func onda.png|500]]
(ou seja, vemos que $\Delta k$ atua como uma espécie de variância do gráfico de $|\tilde \Psi|$)

- Se $\Delta k$ for reduzido, repete-se o que tinhamos acima: $\alpha(k)$ fica muito localizada em torno de $k_{0}$. Torna-se portanto útil fazer uma expansão em série de Taylor de $\alpha(k)$ em torno de $k_{0}$:
$$\begin{align*}
\alpha(k)&= \alpha(k_{0})+ (k-k_{0}) \frac{d \alpha}{dk}\biggr|_{k=k_{0}} + \dots\\
&= \alpha(k_{0}) + (k-k_{0})x_{0}+\dots \quad \quad ;\quad \quad x_{0}=\frac{d \alpha}{dk}\biggr|_{k=k_{0}}
\end{align*}$$
repetindo o que fizemos acima com a série de Taylor de $\omega(k)$ obtemos:
$$\Psi(x)=e^{ik_{0}x+i\alpha(k_{0})}\int \frac{dk}{\sqrt{2\pi}} |\tilde \Psi(k)| e^{i(k-k_{0})(x-x_{0})}$$ 
- Temos então algumas possibilidades, conforme o valor do tempo $x-x_{0}$:
##### $x-x_{0}$ elevado
- Neste caso temos que o termo exponencial dentro da integral tem um expoente elevado. Isto vai fazer com que o integrando varie muito rápido de valor dentro do intervalo de integração. Isto vai fazer com que o integral se suprima. Temos algo do tipo:
![[transf fourier caso 1.png|500]]

- O limite que temos para que isto ocorra é $$|x-x_{0}|> \frac{1}{\Delta k}$$

##### $x-x_{0}$ baixo
- O termo exponencial já não vai fazer com que o integral se suprima. Temos:
![[transf fourier caso 2.png|500]]

##### $x=x_{0}$
- O termo exponencial é simplesmente eliminado. O integral tem o valor máximo.

- Ou seja, em resumo: O integral é máximo para $x=x_{0}$. Conforme $x$ se afasta de $x_{0}$, o integral diminui, mas continua a ser significativo. Quando chegamos a $|x-x_{0}|> \frac{1}{\Delta k}$, o integral anula-se. 
- Assim, para que o integral seja significativo é preciso ter:
$$\Delta k \cdot|x-x_{0}|\sim 1$$
que podemos escrever na forma:
$$\Delta k \Delta x\sim 1$$
- Em 2+ dimensões escreveríamos isto como:
$$\Delta k^{i} \Delta x^{i}\sim 1$$
(sendo que isto não representa uma soma, como na notação de Newton normalmente temos. Invés disso temos $N$ equações diferentes)

- Até agora temos estudado o princípio de incerteza com o $k$, a que temos chamado *momento*. Ora, na realidade este não é o verdadeiro momento, mas sim $p=\hbar k$. Ou seja, diferem apenas por uma constante.
- Podemos escrever:
$$\Psi_{k}(x)= \frac{e^{ikx}}{\sqrt{2\pi}} \quad \quad \longrightarrow \quad \quad \Psi_{p}(x)=\frac{e^{i \frac{p}{\hbar} x} }{\sqrt{2\pi \hbar}}$$ 
- E temos ainda que o valor médio do momento será:
$$\hat{P} \Psi_{p}(x)=\frac{\hbar}{i} \frac{\partial}{\partial x}\Psi_{p}(x)=\frac{\hbar}{i} \frac{\partial}{\partial x}\left(\frac{e^{i \frac{p}{\hbar} x} }{\sqrt{2\pi \hbar}}\right)=\frac{\hbar}{i}\cdot i \frac{p}{\hbar} \frac{e^{i \frac{p}{\hbar} x} }{\sqrt{2\pi \hbar}}= p \frac{e^{i \frac{p}{\hbar} x} }{\sqrt{2\pi \hbar}}= p \Psi_{p}(x)$$
- Ou seja, a função de onda para uma partícula livre está associada a um momento bem definido. Assim vemos que, apesar de não normalizável e fisicamente impossível, esta função é útil para formar uma base de estados para escrever um estado genérico.

**_Conclusão_**
- Tendo $\tilde \Psi(k)$, a transformada de Fourier da função de onda $\Psi(x)$, $|\tilde\Psi(k)|^{2}$ irá dar-nos a densidade de probabilidade do _momento da partícula_. Ou seja, dá-nos a probabilidade de a partícula ter um momento entre $[k\hbar,\hbar(k+dk)]$ (pelo que $p=\hbar k$)
- O **princípio da incerteza de Heisenberg** apenas nos diz como se relacionam as variâncias da função de onda e da sua transformada de Fourier:
$$\Delta x \Delta k \ge \frac{1}{2}$$
em que temos as funções $\Psi(x), \tilde \Psi(k)$. Recordemos ainda que as variâncias são dadas por: $\Delta x = \sqrt{\langle x^{2}\rangle - \langle x\rangle^{2}}, \Delta k = \sqrt{\langle k^{2}\rangle - \langle k\rangle^{2}}$

- Sendo $p=\hbar k$ podemos reescrever a equação acima na forma mais conhecida: $$\Delta x \Delta p \ge \frac{\hbar}{2}$$
- De notar que no estado fundamental temos $\Delta x \Delta p = \frac{\hbar}{2}$, ou seja, a relação entre as variáveis é saturada.