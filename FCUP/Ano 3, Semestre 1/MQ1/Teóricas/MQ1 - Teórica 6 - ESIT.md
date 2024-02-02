# 2.4 - Equação de Schrödinger Independente do Tempo (ESIT)
- Isto é o que chamaremos à Eq Schrödinger de um sistema em que o *potencial* não varia com o tempo: $V=V(\vec{r})$. Temos:
$$i\hbar \frac{\partial}{\partial t}\Psi(\vec{r},t)= \left( \frac{-\hbar^{2}}{2m}\Delta+V(\vec{r}) \right)\Psi(\vec{r},t)$$
usemos o método de separação de variáveis: $\Psi(\vec{r},t)=\psi(\vec{r})f(t)$. Ficamos com:
$$\begin{align*}
i\hbar \frac{df}{dt} \psi(\vec{r})&= f(t)\left( \frac{-\hbar^{2}}{2m}\Delta + V(\vec{r})\psi(\vec{r}) \right)\\
i\hbar \frac{df}{dt} \frac{1}{f(t)}&= \frac{1}{\psi(\vec{r})} \left( \frac{-\hbar^{2}}{2m}\Delta + V(\vec{r})\psi(\vec{r}) \right)\\
\end{align*}$$
vemos que o lado esquerdo depende apenas de $t$ e o direito apenas de $\vec{r}$. Assim, a única forma de esta igualdade se verificar é se ambos os lados da equação forem constantes. Vamos considerar então que são ambos iguais à constante $E$:
$$\begin{cases}
\frac{i\hbar}{f(t)} \frac{df}{dt}=E\\ 
\frac{1}{\psi(\vec{r})} \left( \frac{-\hbar^{2}}{2m}\Delta + V(\vec{r})\psi(\vec{r}) \right)=E
\end{cases}$$
**Equação Temporal**
- Facilmente vemos que:
$$\begin{align*}
\frac{i\hbar}{f(t)} \frac{df}{dt}&= E\\
i \hbar \frac{df}{dt}&= Ef(t)\\
f(t) &= e^{-i \frac{E}{\hbar} t}
\end{align*}$$
aqui vemos que $\frac{E}{\hbar}= \omega$. Ou seja, $E$ será a energia, sendo que podemos usar a relação de Einstein-Planck: $E=\hbar \omega=h \nu$

**Equação de Posição**
- Temos:
$$\begin{align*}
\frac{1}{\psi(\vec{r})} \left( \frac{-\hbar^{2}}{2m}\Delta + V(\vec{r})\psi(\vec{r}) \right)&= E\\
\left( \frac{-\hbar^{2}}{2m}\Delta + V(\vec{r})\psi(\vec{r}) \right)&= E \psi(\vec{r})\\
\end{align*}$$
e temos a forma completa da solução da equação de Schrödinger: $$\Psi(\vec{r},t)=\psi(\vec{r}) e^{-i \frac{E}{\hbar} t}$$

### Hamiltoniano
- Notemos ainda que o Hamiltoniano, na física clássica tinha a forma $H= \frac{p^{2}}{2m}+V(\vec{r})$. Ora, sendo o operador do momento: $\hat{P}=\frac{\hbar}{i} \nabla$, é natural que $$\hat{H}=- \frac{\hbar^{2}}{2m} \Delta + V(\vec{r})$$
- Assim podemos escrever a equação de Schrödinger como: 
$$\hat{H} \Psi=E \Psi$$
- Relacionando com Computacional, torna-se evidente que as Energias permitidas serão os *valores próprios* de $\hat{H}$. :)

## Estado Estacionário: SEM combinações lineares
- O tipo de Função que obtivemos acima:
$$\Psi(\vec{r},t)=\psi(\vec{r}) e^{-i \frac{E}{\hbar} t}$$
é aquilo a que se chama *função de onda estacionária*. Ora, este "estacionária" não significa que a função está fixa no tempo. Invés disso, significa que a **densidade de probabilidade** é independente do tempo: $|\Psi(\vec{r},t)|^{2}=|\psi(\vec{r})|^{2}$

- O que vimos acima aplica-se a qualquer Observável que seja *explicitamente independente do tempo*. Ou seja, tendo $\mathcal{O}=\mathcal{O}\left( \vec{r}, \frac{\hbar}{i} \nabla \right)$, obtemos que:
$$\langle \mathcal{O}(\vec{r},t)\rangle=\int d^{3}r ~\Psi^{*}(\vec{r},t)\mathcal{O}\left(\vec{r},\frac{\hbar}{i}\nabla \right) \Psi(\vec{r},t)=\int d^{3}r ~ \psi^{*}(\vec{r})\mathcal{O}\left(\vec{r},\frac{\hbar}{i}\nabla \right) \psi(\vec{r})$$
isto ocorre porque $$\Psi^{*} \cdot\Psi=\psi^{*} e^{+i \frac{E}{\hbar} t} \cdot \psi e^{-i \frac{E}{\hbar} t}=1$$

- Assim, conforme o que temos acima, a energia destes **estados** é constante e dada pela relação Planck-Einstein:
$$E=\hbar \omega=h \nu$$
- Assim surge a necessidade de comparar de distinguir mecânica clássica e quântica. Quando temos *potencial independente do tempo* tem-se que:
    - **Mec Clássica** - A energia é constante em todo o movimento.
    - **Mec Quântica** - Temos estados *estacionários* com energias bem definidas.

- Daí vem o título desta secção. Estes estados simples têm energias bem definidas que não variam no tempo. No entanto, na maioria dos casos, uma partícula não é descrita por um destes estados, mas sim uma *combinação linear deles* (há várias energias permitidas).

## Estado com combinação linear
- O Operador Hamiltoniano é *linear*. Na prática isto significa que, dadas 2 funções de onda $\psi_{1},\psi_{2}$ e 2 constantes $\lambda_{1},\lambda_{2}$ temos que: $$\hat{H}[\lambda_{1}\psi_{1}(\vec{r}) + \lambda_{2} \psi(\vec{ r})]=\lambda_{1} \hat{H} \psi_{1}(\vec{r})+ \lambda_{2} \hat{H}\psi_{2}(\vec{r})$$
ou seja, sendo $\psi_{1},\psi_{2}$ soluções da ESIT, também a sua combinação linear o será.

- Podemos então escrever uma solução da ESIT como:
$$\Psi(\vec{r},t)=\sum\limits_{n=1}^{\infty} c_{n} \psi_{n}(\vec{r}) e^{-i \frac{E_{n}}{\hbar} t}$$
sendo que a solução depende fortemente dos coeficientes $c_{n}$. (Nos EXS de computacional, estes eram os autovetores)
- Temos ainda novamente que, conhecendo $\Psi(\vec{r},0)$, conseguimos obter $\Psi(\vec{r},t)$

- Com este tipo de funções, já não temos $\Psi^{*}\Psi=1$ (porque ficamos com termos cruzados em que o termo exponencial não se anula). Ou seja, a densidade de probabilidade já **não** é independente do tempo.
- Apenas $\langle H\rangle$ é conservado.

## Poço Infinito
![[Attachments/FCUP/A3S1/MQ1/poço infinito.png|500]]
- Temos aqui o nosso conhecido poço de potencial infinito, descrito por:
$$V(x)=\begin{cases}
0 & ; & 0<x<a \\
\infty & ; & x<0,x>a
\end{cases}$$
- Vejamos qual será a solução da ESIT:
    - Fora do poço temos que ter $\psi=0$. Como $V=\infty$, não temos energia suficiente para pôr a partícula lá.
    - Dentro do poço temos $V=0$. Ou seja, temos uma *partícula livre*. Logo:

$$\begin{align*}
\frac{-\hbar^{2}}{2m} \frac{d^{2}\psi}{dx^{2}}&= E \psi(x)\\
\frac{d^{2}\psi}{dx^{2}}&= -k^{2}\psi \quad \quad \quad \left(k=\sqrt\frac{2mE}{\hbar^{2}}\right)\\
\end{align*}$$
(de notar que podemos ter $E<0$, o que nos dá $k$ imaginário)
- Assim, a solução geral da equação é:
$$\psi(x)=C\sin(kx)+D\cos(kx)$$
- Apliquemos as condições de fronteira: 
    - $\psi(x=0)=0$ dá-nos que $D=0$
    - $\psi(x=a)=0$ dá: $$C\sin(ka)=0 \Leftrightarrow ka=n \pi \Leftrightarrow k_{n}=\frac{n\pi}{a}~~~~(n\in\mathbb{N})$$

- Vemos então que existe um *espectro de energia quantificada*, dado por:
$$E_{n}=\frac{\hbar^{2}k_{n}^{2}}{2m}= \frac{n^{2}\hbar^{2}\pi^{2}}{2ma^{2}}~~~~(n\in \mathbb{N})$$
