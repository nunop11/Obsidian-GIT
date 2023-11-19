# 1 - Estabilidade do átomo de Rutherford
- A maior parte das caraterísticas do átomo de Rutherford foram confirmadas de forma experimental.
- No entanto restava uma: a sua _estabilidade_.
    - Se os eletrões estivessem em repouso, seria impossível o átomo ser estável sem que eles caíssem para o núcleo. Ora, isso não poderia acontecer pois teríamos um átomo do tamanho do núcleo, que seria portanto muito menor (4 ordens de grandeza) do que o tamanho de átomos que já tinha sido provado.
    - Podíamos então pensar que os eletrões circulam como planetas num sistema solar. No entanto, segundo o eletromagnetismo, uma carga com aceleração liberta radiação. Assim, os eletrões perderiam energia mecância e cairiam no nucleo. Além disso, o espetro de emissão dos átomos seria _contínuo_, em vez de _discreto_, como se verifica na vida real.

# 2 - Modelo De Bohr
- Temos eletrões em _órbitas circulares_ em torno do núcleo, tal que
$$\vec{F}=\frac{1}{4\pi \varepsilon_{0}} \frac{Ze^{2}}{r^{2}} \hat{n}=m \frac{v^{2}}{r}\hat{n}$$
- As únicas órbitas possíveis são aquelas em o momento angular $\ell=n \hbar,~~(n=1,2,3,\dots)$  e tem-se:
$$\vec{\ell}=n \hbar \hat{n}=\vec{r}\times m\vec{v}=mrv ~\hat{n}$$
- Quando os eletrões estão na órbita, a sua _energia é constante_. Apenas quando os eletrões transitam de órbtias é emitida energia, sendo que:
$$\begin{align*}
E=E_{c}+E_{P}=\frac{1}{2}mv^{2} - \frac{1}{4\pi \varepsilon_{0}} \frac{Ze^{2}}{r} \quad \quad \textsf{(Eq. 0)}\\
\textsf{Energia emitida: } |E_{f}-E_{i}|
\end{align*}$$
---
- Das 2 igualdades para a força $\vec{F}$ , temos que:
$$\begin{align*}
mv^{2}&= \frac{1}{4\pi \varepsilon_{0}} \frac{Ze^{2}}{r}\\
\frac{1}{2}mv^{2}&= \frac{1}{2} \left(\frac{1}{4\pi \varepsilon_{0}} \frac{Ze^{2}}{r} \right)\\
E_{c}&= \frac{-1}{2} E_{P} \quad \quad \textsf{(Eq. 1)}
\end{align*}$$
- Das 2 igualdades para o momento angular $\vec{\ell}$ temos:
$$n\hbar=mrv \leftrightarrow r = \frac{n\hbar}{mv} \quad \quad \textsf{(Eq. 2)}$$
- Ao pegar na equação 0 e fazer uma substituição conforme a equação 1 temos:
$$\begin{align*}
E=E_{c}+E_{p}=E_{c}-2E_{c}&= -\frac{1}{2}mv^{2} \quad \quad\textsf{(Eq. 3)}\\
&= -E_{c}=\frac{1}{2}E_{P}
\end{align*}$$
Como vimos na equação 2: $r= \frac{n\hbar}{mv}$, logo temos:
$$E=\frac{1}{2} E_{P}=-\frac{1}{2} \frac{1}{4\pi \varepsilon_{0}} \frac{Ze^{2}}{n\hbar}mv \quad \quad\textsf{(Eq. 4)}$$

- A partir das 2 definições de $E$ que temos acima (equações 3 e 4), podemos obter a velocidade em cada órbita:
$$-\cancel{\frac{1}{2}} \cancel{m}v^{\bcancel{2}} = - \cancel{\frac{1}{2}} \frac{1}{4\pi \varepsilon_{0}} \frac{Ze^{2}}{n\hbar} \cancel{m} \bcancel{v}$$
> $$v_{n} = \frac{1}{4\pi \varepsilon_{0}} \frac{Ze^{2}}{n\hbar}$$

- Temos na equação 2 que $r= \frac{n\hbar}{mv}$. Ao substituir $v_n$ nesta equação:
> $$r_{n} = \frac{n\hbar}{m \cdot \frac{1}{4\pi \varepsilon_{0}} \frac{Ze^{2}}{n\hbar}}=4\pi \varepsilon_{0}\frac{n^{2}\hbar^{2}}{mZe^{2}} $$

- Por fim, ao substituir $v_n$ na equação 4 temos a _Energia de cada nível_:
> $$E_{n}= \frac{-m(Ze^{2})^{2}}{2\hbar^{2}(4\pi \varepsilon_{0})^{2}} \frac{1}{n^{2}}$$

## 2.1 - Transições
- A energia de um fotão é $E_{\gamma}=hf$, assim, a frequencia da radiação emitida na transição de um eletrão de um nível inicial para um final é:
$$f = \frac{E_{i}-E_{f}}{h}= \left(\frac{1}{4\pi \varepsilon_{0}}\right)^{2} \frac{mZ^{2}e^{4}}{4\pi\hbar^{3}} \left(\frac{1}{n_{f}^{2}} - \frac{1}{n_{i}^{2}} \right)$$
(de recordar que $\hbar=\frac{h}{2\pi}$, logo $\large \hbar^{2} \cdot h=2\pi\hbar^{3}$)

- Em que podemos então definir $f=\frac{c}{\lambda}$, pelo que $\frac{1}{\lambda}=\frac{f}{c}$:
$$\frac{1}{\lambda}=\left(\frac{1}{4\pi \varepsilon_{0}}\right)^{2} \frac{mZ^{2}e^{4}}{4\pi\hbar^{3}c}\left(\frac{1}{n_{f}^{2}} - \frac{1}{n_{i}^{2}} \right)$$
E de onde podemos definir uma constante:
$$R=\left(\frac{1}{4\pi \varepsilon_{0}}\right)^{2} \frac{mZ^{2}e^{4}}{4\pi\hbar^{3}c}$$

- Temos então as várias séries do espetro de emissão, sem que $n$ é a órbita para a qual o eletrão transita

| Série    | $1/\lambda$                                              | Radiação |
| -------- | -------------------------------------------------------- | -------- |
| Lyman    | $\frac{1}{\lambda}=R(\frac{1}{1^{2}}-\frac{1}{n^{2}})~~,~~n=2,3 ...$   | UV       |
| Balmer   | $\frac{1}{\lambda}=R(\frac{1}{2^{2}} - \frac{1}{n^{2}})~~,~~n=3,4 ...$ | UV       |
| Paschen  | $\frac{1}{\lambda}=R(\frac{1}{3^{2}} - \frac{1}{n^{2}})~~,~~ n=4,5 ...$ | IV       |
| Brackett | $\frac{1}{\lambda}=R(\frac{1}{4^{2}} - \frac{1}{n^{2}})~~,~~ n=5,6 ...$ | IV       |
| Pfund    | $\frac{1}{\lambda}=R(\frac{1}{5^{2}} - \frac{1}{n^{2}})~~,~~ n=6,7 ...$ | IV       |

- Após mexer um pouco com as fórmulas, temos 
$$E_{n}=\frac{-|E_{1}|}{n^{2}}$$

# 3 -  Sistema de 2 partículas
- Consideremos um sistema com 2 partículas, de carga $q_{1},q_{2}$
Temos:
$$E=\frac{1}{2} m_{1}v_{1}^{2}+ \frac{1}{2}m_{2}v_{2}^{2}- \frac{1}{4\pi \varepsilon_{0}} \frac{q_{1}q_{2}}{|\vec{r_{1}}-\vec{r_{2}}|} \quad \quad \textsf{(Eq. 5)}$$
- Vamos então mudar o sistema de vetores, para que gire em torno de 2 vetores principais, com $\vec{R}$ o vetor que diz a posição do CM do sistema e $\vec{r}$ o vetor que dá a posição da partícula 2 em relação à 1. Temos:
$$\begin{cases}
\vec{R} = \frac{m_{1}\vec{r_{1}}+m_{2}\vec{r_{2}}}{m_{1}+m_{2}} \\
\vec{r}=\vec{r_{1}}-\vec{r_{2}}
\end{cases} =
\begin{cases}
\vec{r_{1}}= \vec{R}+\frac{m_{2}}{m_{1}+m_{2}}\vec{r} \\
\vec{r_{2}}= \vec{R}-\frac{m_{1}}{m_{1}+m_{2}}\vec{r}
\end{cases} =
\begin{cases}
\vec{r_{1}}=\vec{R} + \frac{\mu}{m_{1}}\vec{r} \\
\vec{r_{2}}=\vec{R} - \frac{\mu}{m_{2}}\vec{r}
\end{cases}$$
Sendo $\large \mu=\frac{m_{1}m_{2}}{m_{1}+m_{2}}$ a _massa reduzida_ do sistema
Definimos ainda $M=m_{1}+m_{2}$ a _massa total_ do sistema

- Temos que $\vec{v}=\dot{\vec{r}}$. Assim, definindo $\vec{V}$  como sendo a velocidade do CM, temos:
$$\begin{cases}
\vec{v_{1}}=\vec{V} + \frac{\mu}{m_{1}}\vec{v} \\
\vec{v_{2}}=\vec{V} - \frac{\mu}{m_{2}}\vec{v}
\end{cases}$$
- Sabemos que tendo o vetor $\vec{u}=\vec{a}+\vec{b}$, temos $u^{2}=|\vec{a}|^{2}+|\vec{b}|^{2}+2 \vec{a}\cdot \vec{b}$. Assim, voltando à equação 5 temos:
$$E=\frac{1}{2}m_{1} \left(V^{2}+ \frac{\mu^{2}}{m_{1}^{2}}v^{2} + 2 \frac{\mu}{m_{1}}\vec{V}\cdot \vec{v}\right)+ \frac{1}{2}m_{2} \left(V^{2}+ \frac{\mu^{2}}{m_{2}^{2}}v^{2} + 2 \frac{\mu}{m_{2}}\vec{V}\cdot \vec{v}\right)- \frac{1}{4\pi \varepsilon_{0}} \frac{q_{1}q_{2}}{r}$$

- De onde tiramos a equação:
$$E= \frac{1}{2}MV^{2}+ \frac{1}{2} \mu v^{2}+E_{P}$$
- No referencial do CM temos $\vec{V}=\vec{0}$, pelo que
$$E= \frac{1}{2}\mu v^{2} - \frac{1}{4\pi \varepsilon_{0}} \frac{q_{1}q_{2}}{r}$$
- Podemos ver que, se tivermos $\mu=m_{e}, ~ q_{1}q_{2}=Ze^2$ temos de novo a equação 0. Ou seja, a partir daqui podemos definir novamente as equações dos níveis do átomo.

#moderna #fisica #atomo