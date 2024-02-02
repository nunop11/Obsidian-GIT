## 5.1 - Cálculo da energia e os seus estados próprios
- Consideremos um Hamiltoniano independente do tempo com a forma:
$$H=H_{0}+V \quad \quad \quad;\quad (V\ll H_{0})$$
- Em que conhecemos os vetores e valores próprios de $H_{0}$. Temos então:
$$H_{0}\ket{\varphi_{p}^{i}}=E_{p}^{0}\ket{\varphi_{p}^{i}} \quad \quad ;\quad i=1,\dots,g_{p}$$
e temos então que os vetores próprios formam uma base completa e ortonormada $\{\ket{\varphi_{p}^{i}}\}$. Ou seja:
$$\langle \varphi_{p}^{i}|\varphi_{p}^{i}\rangle=\delta_{pp'}\delta_{ii'} \quad \quad;\quad \quad \sum\limits_{p,i}\ket{\varphi_{p}^{i}}\bra{\varphi_{p}^{i}}=\mathbb{1}$$

- Vamos definir $V=\lambda W$ e podemos reescrever o Hamiltoniano:
$$H(\lambda)=H_{0}+\lambda W \quad \quad;\quad (\lambda\ll1)$$
ora, $W$ é um operador e $H(\lambda)$ representa um sistema que inicialmente conhecemos e em que é introduzida uma perturbação (cuja intensidade é representada por $\lambda$).

- Assumindo que os elementos da matriz de $W$ são da mesma ordem que os de $H$, temos:
$$H(\lambda)\ket{\psi(\lambda)}=E(\lambda)\ket{\psi(\lambda)}$$
- Vamos *sugerir* uma solução em série de potências:
$$\begin{align*}
E(\lambda)&= \varepsilon_{0}+\lambda \varepsilon_{1}+\lambda^{2}\varepsilon_{2}+\dots=\sum_{n=0}^{\infty}\lambda^{n}\varepsilon_{n}\\
\ket{\psi(\lambda)}&= \ket{0}+\lambda\ket{1}+\lambda^{2}\ket{2}+\dots=\sum\limits_{n=0}^{\infty}\lambda^{n}\ket{n}
\end{align*}$$
- Vamos agora substituir esta proposta de solução na equação dos vetores próprios:
$$(H_{0}+\lambda W)\sum\limits_{n=0}^{\infty}\lambda^{n}\ket{n}=\left(\sum\limits_{m=0}^{\infty}\lambda^{m}\varepsilon_{m}\right)\left(\sum\limits_{n=0}^{\infty}\lambda^{n}\ket{n}\right)$$
e (o início) fica
$$\Tiny\begin{align*}
(H_{0}+\lambda W)(\ket{0}+\lambda\ket{1}+\lambda^{2}\ket{2})&= (\varepsilon_{0}+\lambda\varepsilon_{1}+\lambda^{2}\varepsilon_{2})(\ket{0}+\lambda\ket{1}+\lambda^{2}\ket{2})\\
H_{0}\ket{0}+H_{0}\lambda\ket{1}+H_{0}\lambda^{2}\ket{2}+W\lambda\ket{0}+W\lambda^{2}\ket{1}+W\lambda^{3}\ket{2}&= \varepsilon_{0}\ket{0}+\varepsilon_{0}\lambda\ket{1}+\varepsilon_{0}\lambda^{2}\ket{2}+\lambda\varepsilon_{1}\ket{0}+\lambda^{2}\varepsilon_{1}\ket{1}+\lambda^{3}\varepsilon_{1}\ket{2}+\\
&+ \lambda^{2}\varepsilon_{2}\ket{0}+\lambda^{3}\varepsilon_{2}\ket{1}+\lambda^{4}\varepsilon_{2}\ket{2}\\
\lambda^{3}W\ket{2}+\lambda^{2}(H_{0}\ket{2}+W\ket{1})+\lambda(H_{0}\ket{1}+W\ket{0})+H_{0}\ket{0}&= \lambda^{4}\varepsilon_{2}\ket{2}+\lambda^{3}(\varepsilon_{1}\ket{2}+\varepsilon_{2}\ket{1}) + \lambda^{2}(\varepsilon_{0}\ket{2}+\varepsilon_{1}\ket{1}+\varepsilon_{2}\ket{0})+\\
&+ \lambda(\varepsilon_{0}\ket{1}+\varepsilon_{1}\ket{0})+\varepsilon_{0}\ket{0}
\end{align*}$$

- Ora, para que esta equação seja válida para qualquer $\lambda\ll1$, temos que igualar os coeficientes de cada potêencia $\lambda^{n}$:
$$\begin{align*}
n=0 &&\to &&&H_{0}\ket{0}=\varepsilon_{0}\ket{0}\\
n=1 &&\to &&&H_{0}\ket{1}+W\ket{0}=\varepsilon_{0}\ket{1}+\varepsilon_{1}\ket{0}~\Leftrightarrow\\
&&&&& \Leftrightarrow~(H_{0}-\varepsilon_{0})\ket{1}+(W-\varepsilon_{1})\ket{0}=0\\
n=2 &&\to &&&H_{0}\ket{2}+W\ket{1}=\varepsilon_{0}\ket{2}+\varepsilon_{1}\ket{1}+\varepsilon_{2}\ket{0}~\Leftrightarrow\\
&&&&& \Leftrightarrow~ (H_{0}-\varepsilon_{0})\ket{2}+(W-\varepsilon_{1})\ket{1}-\varepsilon_{2}\ket{0}=0
\end{align*}$$

- Podemos impor que o estado $\ket{\psi(\lambda)}$ esteja normalizado: $\langle \psi(\lambda)|\psi(\lambda)\rangle=1$.
- E como a fase de $\ket{\psi(\lambda)}$ também não é conhecida, podemos impor $\langle0|\psi(\lambda)\rangle\in\mathbb{R}$
- Destas 2 condições impostas obtemos:
    - $n=0$ - Na equação obtida acima temos $\ket{\psi}=\ket{0}$. Isto cumpre ambas as condições
    - $n=1$ - Da equação podemos obter (não sei como) $\ket{\psi}=\ket{0}+\lambda\ket{1}$.
        - Para a função estar normalizada: $$1=\langle\psi|\psi\rangle=\langle0|0\rangle+\lambda(\langle1|0\rangle+\langle0|1\rangle)=1+\lambda(\langle1|0\rangle+\langle0|1\rangle)$$Ou seja, é preciso que $\langle0|1\rangle=-\langle1|0\rangle=-\langle0|1\rangle^{*}$
        - Para a segunda condição: $$\langle0|\psi\rangle=\langle0|0\rangle+\lambda\langle0|1\rangle\in\mathbb{R}$$de onde surge a necessidade de $\langle0|1\rangle\in\mathbb{R}$.
    - $n=2$ - Obtemos da equação $\ket{\psi}=\ket{0}+\lambda\ket{1}+\lambda^{2}\ket{2}$. Das condições impostas obtemos: $\langle0|2\rangle=\langle2|0\rangle=- \frac{1}{2}\langle1|1\rangle$

### Correção a nível não degenerado (1ª ordem)
- Consideremos $\ket{\varphi_{q}}$ um vetor próprio não degenerado de $H_{0}$ com valor próprio $E_{q}^{0}$.
- Vejamos o que se obtem nas equações acima:
    - $n=0$ - Temos que $\ket{0}=\ket{\varphi_{q}}$ e $E_{q}^{0}=\varepsilon_{0}$
    - $n=1$ - A equação pode ser escrita como $(H_{0}-E_{q}^{0})\ket{1}+(W-\varepsilon_{1})\ket{\varphi_{q}}=0$
        - Podemos reescrever isto (não sei como) e obter $\ket{\psi_{q}(\lambda)}=\ket{\varphi_{q}}+\lambda\ket{1}~~,~~ E_{q}=E_{q}^{0}+\lambda \varepsilon_{1}$

- Podemos ainda projetar a equação para $n=1$ em $\ket{\varphi_{q}}$:
$$\begin{align*}
\bra{\varphi_{q}} \left[ (H_{0}-E_{q}^{0})\ket{1}+(W-\varepsilon_{1})\ket{\varphi_{q}}\right]&= 0\\
\langle\varphi_{q}|H_{0}-E_{q}^{0}|1\rangle+\langle\varphi_{q}|W-\varepsilon_{1}|\varphi_{q}\rangle&= 0\\
\langle\varphi_{q}|H_{0}|1\rangle-E_{q}^{0}\langle\varphi_{q}|1\rangle+\langle\varphi_{q}|W|\varphi_{q}\rangle-\varepsilon_{1}\langle\varphi_{q}|\varphi_{q}\rangle&= 0\\
0-0+\langle\varphi_{q}|W|\varphi_{q}\rangle-\varepsilon_{1}\cdot1&= 0\\
\varepsilon_{1}&= \langle\varphi_{q}|W|\varphi_{q}\rangle
\end{align*}$$
sendo esta a **Correção à energia**.

- Assim, em primeira ordem em teoria de perturbações a energia é dada por
$$\boxed{E_{q}=E_{q}^{0}+\lambda\langle\varphi_{q}|W|\varphi_{q}\rangle+\mathcal{O}(\lambda^{2})}$$

- Para obter a correção a $\ket{1}$ projetamos a equação para$n=1$ em $\ket{\varphi_{n}^{i}}$ (com $n\neq q$) e temos:
$$\begin{align*}
\bra{\varphi_{n}^{i}} \left[ (H_{0}-E_{q}^{0})\ket{1}+(W-\varepsilon_{1})\ket{\varphi_{q}}\right]&= 0\\
\langle\varphi_{n}^{i}|H_{0}-E_{q}^{0}|1\rangle+\langle\varphi_{n}^{i}|W-\varepsilon_{1}|\varphi_{q}\rangle&= 0\\
\langle\varphi_{n}^{i}|H_{0}|1\rangle-E_{q}^{0}\langle\varphi_{n}^{i}|1\rangle+\langle\varphi_{n}^{i}|W|\varphi_{q}\rangle-\varepsilon_{1}\langle\varphi_{n}^{i}|\varphi_{q}\rangle&= 0\\
(E_{n}-E_{q}^{0})\langle\varphi_{n}^{i}|1\rangle+\langle\varphi_{q}|W|\varphi_{q}\rangle-\varepsilon_{1}\cdot0&= 0\\
\langle\varphi_{n}^{i}|1\rangle&= \frac{\langle\varphi_{n}^{i}|W|\varphi_{q}\rangle}{E_{n}-E_{q}^{0}} \quad \quad (n\neq q)
\end{align*}$$
e podemos então escrever $\ket{\psi_{q}(\lambda)}$:
$$\boxed{\ket{\psi_{q}(\lambda)}=\ket{\varphi_{q}}+\lambda\sum\limits_{n\neq q}\sum\limits_{i=1}^{g_{n}}\frac{\langle\varphi_{n}^{i}|W|\varphi_{q}\rangle}{E_{n}-E_{q}^{0}}\ket{\varphi_{n}^{i}}+\mathcal{O}(\lambda^{2})}$$
- Claro, em ambas as equações escritas acima temos
$$E_{q}^{0}\gg\langle\varphi_{q}|V|\varphi_{q}\rangle \quad \quad;\quad \quad 1\gg\frac{\langle\varphi_{n}^{i}|V|\varphi_{q}\rangle}{E_{n}-E_{q}^{0}}$$

### Correção a um nível Degenerado (1ª Ordem)
- Temos agora um nível de energia $E_{q}^{0}$ com degenerescência $g_{q}>1$. O seu subespaço próprio $\mathscr{E}_{q}^{0}$ pode ser descrito pela base $\{\ket{\varphi_{q}^{i}},i=1,\dots,g_{q}\}$
- Analogamente ao que fizemos acima:
$$\begin{align*}
\varepsilon_{0}&= E_{q}^{0}\\
\ket{0}&= \sum\limits_{i=1}^{g_{q}}c_{i}\ket{\varphi_{q}^{i}} \quad \quad;\quad \sum\limits_{i=1}^{g_{q}}|c_{i}|^{2}=1
\end{align*}$$
- Novamente, projetamos a equação de $n=1$ em $\ket{\varphi_{q}^{i}}$:
$$\begin{align*}
\bra{\varphi_{q}^{i}} \left[ (H_{0}-E_{q}^{0})\ket{1}+(W-\varepsilon_{1})\ket{0}\right]&= 0\\
\langle\varphi_{q}^{i}|H_{0}-E_{q}^{0}|1\rangle+\langle\varphi_{q}^{i}|W-\varepsilon_{1}|0\rangle&= 0\\
0+\langle\varphi_{q}^{i}|W|0\rangle-\varepsilon_{1}\langle\varphi_{q}^{i}|0\rangle&= 0\\
\langle\varphi_{q}^{i}|W|0\rangle&= \varepsilon_{1}\langle\varphi_{q}^{i}|0\rangle\\
\sum\limits_{n}\sum\limits_{j=1}^{g_{n}}\langle\varphi_{q}^{i}|W|\varphi_{n}^{j}\rangle\langle\varphi_{n}^{j}|0\rangle&= \varepsilon_{1}c_{i}\\
\sum\limits_{n}\sum\limits_{j=1}^{g_{n}}\langle\varphi_{q}^{i}|W|\varphi_{n}^{j}\rangle c_{j}\delta_{nq}&= \varepsilon_{1}c_{i}\\
c_{j}\sum\limits_{j=1}^{g_{n}}\langle\varphi_{q}^{i}|W|\varphi_{q}^{j}\rangle&= \varepsilon_{1}c_{i}\\
W_{q}^{ij}c_{j}&= \varepsilon_{1}c_{i}
\end{align*}$$
- Para determinar a energia em 1ª ordem temos que diagonaliar a perturbação $W$ no subespaço $\mathscr{E}_{q}^{0}$. Os valores próprios $\varepsilon_{1}^{j}$ da diagonal dão-nos a energia:
$$E_{q,j}(\lambda)=E_{q}^{0}+\lambda\varepsilon_{1}^{j} \quad \quad;\quad j=1,\dots,f_{q}\le g_{q}$$
    - Se $f_{q}=g_{q}$ então deixamos de ter degenerescência
    - Se $f_{q}<g_{q}$ temos alguns estados degenerados

- Seja $\{\ket{u_{q,i}}\}\in\mathscr{E}_{q}^{0}$ a base própria de $W_{q}$
    - Se o valor próprio $\varepsilon_{1}^{i}$ for não-degenerado então o estado $\ket{0}=\ket{u_{q,i}}$ fica determinado, com energia $E_{q,i}=E_{q}^{0}+\lambda\varepsilon_{1}^{i}$ 
    - Se o valor próprio $\varepsilon_{1}^{i}$ for degenerado em $\ket{0}$, então irá pertencer a esse subespaço de $\mathscr{E}_{q}^{0}$ e o estado não fica determinado. Podemos conseguir eliminar a degenerescência em ordens superiores.

### Correção a um nível Degenerado (2ª Ordem)
- Agora iremos considerar:
$$\begin{align*}
E_{q}(\lambda)&= E_{q}^{0} + \lambda\varepsilon_{1} + \lambda^{2}\varepsilon_{2}\\
\ket{\psi_{q}(\lambda)}&= \ket{\varphi_{q}}+\lambda\ket{1}+\lambda^{2}\ket{2}
\end{align*}$$
- Acima obtivemos para $n=2$ a equação:
$$(H_{0}-\varepsilon_{0})\ket{2}+(W-\varepsilon_{1})\ket{1}-\varepsilon_{2}\ket{0}=0$$
- Vamos projetar esta equação em $\ket{\varphi_{q}}$:
$$\begin{align*}
\bra{\varphi_{q}}\biggr[(H_{0}-\varepsilon_{0})\ket{2}+(W-\varepsilon_{1})\ket{1}-\varepsilon_{2}\ket{0} \biggr]&= 0\\
\langle\varphi_{q}|H_{0}-\varepsilon_{0}|2\rangle + \langle\varphi_{q}|W-\varepsilon_{1}|1\rangle - \varepsilon_{2}\langle\varphi_{q}|0\rangle&= 0\\
0 + \langle\varphi_{q}|W|1\rangle - \varepsilon_{1}\langle\varphi_{q}|1\rangle -\varepsilon_{2}\cdot1&= 0\\
\langle\varphi_{q}|W|1\rangle - \varepsilon_{1}\cdot0 -\varepsilon_{2}&= 0\\
\varepsilon_{2}&= \langle\varphi_{q}|W|1\rangle
\end{align*}$$
podemos tornar isto em algo mais direto:
$$\begin{align*}
\varepsilon_{2}&= \langle\varphi_{q}|W|1\rangle\\
&= \langle\varphi_{q}|W\mathbb{1}|1\rangle\\
&= \sum\limits_{n\neq q}\sum\limits_{i=1}^{g_{n}}\langle\varphi_{q}|W|\varphi_{n}^{i}\rangle\langle\varphi_{n}^{i}|1\rangle\\
&= \sum\limits_{n\neq q}\sum\limits_{i=1}^{g_{n}}\langle\varphi_{q}|W|\varphi_{n}^{i}\rangle\frac{\langle\varphi_{n}^{i}|W|\varphi_{q}\rangle}{E_{n}^{0}-E_{q}^{0}}\\
&= \sum\limits_{n\neq q}\sum\limits_{i=1}^{g_{n}}\frac{|\langle\varphi_{n}^{i}|W|\varphi_{q}\rangle|^{2}}{E_{q}^{0}-E_{n}^{0}}
\end{align*}$$
e ficamos com a *correção de energia de 2ª ordem*:
$$\boxed{E_{q}(\lambda)=E_{q}^{0} + \lambda\langle\varphi_{q}|W|\varphi_{q}\rangle +\lambda^{2}\sum\limits_{n\neq q}\sum\limits_{i=1}^{g_{n}}\frac{|\langle\varphi_{n}^{i}|W|\varphi_{q}\rangle|^{2}}{E_{q}^{0}-E_{n}^{0}}+\mathcal{O}(\lambda^{3})}$$

- Tal como atrás, podemos projetar a equação de $n=2$ em $\ket{\varphi_{n}^{i}}$ e temos
$$\begin{align*}
\bra{\varphi_{n}^{i}}\biggr[(H_{0}-\varepsilon_{0})\ket{2}+(W-\varepsilon_{1})\ket{1}-\varepsilon_{2}\ket{0} \biggr]&= 0\\
\langle\varphi_{n}^{i}|H_{0}-\varepsilon_{0}|2\rangle + \langle\varphi_{n}^{i}|W-\varepsilon_{1}|1\rangle - \varepsilon_{2}\langle\varphi_{n}^{i}|0\rangle&= 0\\
(E_{n}^{0}-E_{q}^{0})\langle\varphi_{n}^{i}|2\rangle + \langle\varphi_{n}^{i}|W-\varepsilon_{1}|1\rangle - \varepsilon_{2}\cdot0&= 0\\
\langle\varphi_{n}^{i}|2\rangle&= \frac{\langle\varphi_{n}^{i}|W-\varepsilon_{1}|1\rangle}{E_{q}^{0}-E_{n}^{0}}
\end{align*}$$
- Podemos ainda representar $\ket{2}$ na base própria de $H_{0}$, $\{\ket{\varphi_{n}^{i}}\}$ :
$$\ket{2}=\sum\limits_{n}\sum\limits_{i=1}^{g_{n}}\langle\varphi_{n}^{i}|2\rangle\ket{\varphi_{n}^{i}}$$
e fica
$$\ket{2}=\langle\varphi_{q}^{2}|2\rangle\ket{\varphi_{q}}+\sum\limits_{n\neq q} \sum\limits_{i=1}^{g_{n}} \langle\varphi_{n}^{i}|2\rangle\ket{\varphi_{n}^{i}}$$
- Usando a equação de $\langle\varphi_{n}^{i}|2\rangle$ e a condição $\langle0|2\rangle=\frac{-1}{2}\langle1|1\rangle$ que obtivemos atrás:
$$\boxed{\ket{2}=- \frac{\langle1|1\rangle}{2}\ket{\varphi_{q}}+\sum\limits_{n}\sum\limits_{i=1}^{g_{n}}\frac{\langle\varphi_{n}^{i}|W-\varepsilon_{1}|1\rangle}{E_{q}^{0}-E_{n}^{0}}\ket{\varphi_{n}^{i}}}$$
sendo esta a *Correção do estado perturbado de 2ª ordem*.

- Se substituirmos $\varepsilon_{1},\ket{1}$ obtidos para a primeira ordem obtemos o resultado final.

## Estimativa do Erro em 1ª ordem
- Podemos estimar este erro ao majorar o termo de 2ª ordem.
- Definimos $\Delta E=|E_{q}^{0}-E_{m}^{0}|$ sendo $m$ o nível mais próximo. Temos sempre $|E_{n}^{0}<E_{q}^{0}|\le\Delta E$ para $n\neq q$.
- Assim:
$$\begin{align*}
|\varepsilon_{2}|=\Biggr|\sum\limits_{n\neq q}\sum\limits_{i=1}^{g_{n}}\frac{|\langle\varphi_{n}^{i}|W|\varphi_{q}\rangle|^{2}}{E_{q}^{0}-E_{n}^{0}}\Biggr|&\le \frac{1}{\Delta E}\sum\limits_{n\neq q}\sum\limits_{i=1}^{g_{n}}|\langle \varphi_{n}^{i}|W|\varphi_{q}\rangle|^{2}=\\
&= \frac{1}{\Delta E}\sum\limits_{n\neq q}\sum\limits_{i=1}^{g_{n}}\langle \varphi_{q}|W|\varphi_{n}^{i}\rangle\langle \varphi_{n}^{i}|W|\varphi_{q}\rangle=\\
&= \frac{1}{\Delta E}\langle\varphi_{q}|W\left(\sum\limits_{n\neq q}\sum\limits_{i=1}^{g_{n}} \ket{\varphi_{n}^{i}}\bra{\varphi_{n}^{i}} \right)W|\varphi_{q}\rangle\\
&= \frac{1}{\Delta E}\langle\varphi_{q}|W\left(\mathbb{1}-\ket{\varphi_{q}}\bra{\varphi_{q}}\right)W|\varphi_{q}\rangle\\
&= \frac{1}{\Delta E}\left(\langle\varphi_{q}|W^{2}|\varphi_{q}\rangle-\langle\varphi_{q}|W|\varphi_{q}\rangle^{2} \right)\\
&= \frac{\Delta W^{2}}{\Delta E}
\end{align*}$$
em que $\Delta W^{2}$ é a variância de $W$ no estado $\ket{\varphi_{q}}$.

- O erro será então:
$$|\lambda^{2}\varepsilon_{2}|\le\frac{(\Delta V)^{2}}{\Delta E}$$

## 5.2 - Estrutura fina do Átomo de Hidrogénio
- O estudo da teoria de perturbações que fizemos atrás não considera efeitos magnéticos e de spin.
- Assim, podemos definir o Hamiltoniano do átomo de hidrogénio, incluindo termos de estrutura fina:
$$H=m_{e}c^{2}+H_{0}+W_{mv}+W_{SO}+W_{D}$$
em que
*Hamiltoniano não perturbado*
$$H_{0}=\frac{p^{2}}{2m}-\frac{e^{2}}{4\pi\varepsilon_{0}r} \quad \quad;\quad m=\frac{m_{e}m_{P}}{m_{e}+m_{P}}\sim m_{e}$$
*Correção relativista da Energia cinética*
$$W_{mv}=- \frac{\vec{p}^{4}}{8m_{e}^{3}c^{2}}$$
que surge de:
$$\begin{align*}
E=e\sqrt{\vec{p}^{2}+m_{e}^{2}c^{2}}=m_{e}c^{2}\sqrt{1+\frac{\vec{p}^{2}}{m_{e}c^{2}}}&\simeq m_{e}c^{2} (1+\frac{p^{2}}{2m_{e}^{2}c^{2}}-\frac{\vec{p}^{4}}{8m_{e}^{4}c^{4}}+\dots)\\
&\simeq m_{e}c^{2} + \frac{\vec{p}^{2}}{2m_{e}}-\frac{\vec{p}^{4}}{8m_{e}^{3}c^{2}}
\end{align*}$$
Podemos ainda comparar este termo ao Hamiltoniano não perturbado:
$$\frac{W_{mv}}{H_{0}}\sim\frac{\frac{\vec{p}^{4}}{8m_{e}^{3}c^{2}}}{\frac{\vec{p}^{2}}{2m_{e}}}\sim \left(\frac{v}{c}\right)^{2}\sim \alpha^{2}=\left(\frac{1}{137}\right)^{2}$$
sendo $\alpha$ a famigerada *constante de estrutura fina*. No átomo de hidrogénio $H_{0}\sim10\text{eV}$ logo $W_{mv}\sim10^{-3}\text{eV}$.

*Termo de Spin-Órbita*
$$W_{SO}=\frac{1}{2m_{e}^{2}c^{2}} \frac{1}{R}\frac{dV(R)}{dR}\vec{L}\cdot\vec{S}$$
- Consideremos um eletrão a mover-se a velocidade $\vec{v}$ no campo elétrico criado pelo protão.
- Temos o campo elétrico a que o eletrão está sujeito: $\vec{E}=\frac{e}{2\pi\varepsilon_{0}r^{2}}\hat{r}=\frac{1}{e} \frac{dV}{dr}\hat{r}$
- O campo magnético será: $\vec{B}\sim \frac{-1}{c^{2}}\vec{v}\times\vec{E}=- \frac{\vec{v}}{e^{2}}\times \frac{1}{e} \frac{dV}{dr}\frac{\vec{r}}{r}=- \frac{1}{c^{2}m_{e}e}\frac{1}{r}\frac{dV}{dr}m_{e}\vec{v}\times\vec{r}=\frac{1}{c^{2}m_{e}e}\frac{1}{r}\frac{dV}{dr}\vec{L}$
- Assim, a energia da interação spin-campo magnético é $$W\simeq-\vec{\mu_{S}}\cdot\vec{B}=-\left(-2\mu_{B}\frac{\vec{S}}{\hbar}\right)\cdot\vec{B}=2\frac{e\hbar}{2m_{e}} \frac{\vec{S}}{\hbar}\cdot \frac{1}{c^{2}m_{e}er}\frac{dV}{dr}\vec{L}=\frac{1}{c^{2}m_{e}^{2}} \frac{1}{r} \frac{dV}{dr}\vec{S}\cdot\vec{L}$$
em que deduzimos o termo a menos de um fator de $\frac{1}{2}$. Esta diferença tem a ver com coisas que assumimos.
- Novamente, podemos estimar a relação entre esta correção e o hamiltoniano sem perturbação:
    - Temos $\vec{L}\sim\hbar~,~\vec{S}\sim\hbar~,~r\sim a_{0}~,~ \frac{dV}{dr}\sim \frac{e^{2}}{4\pi\varepsilon_{0}a_{0}^{2}}$, o que resulta em: $$\begin{align*}
W_{SO}&= \frac{1}{2c^{2}m_{e}^{2}} \frac{1}{r} \frac{dV}{dr}\vec{S}\cdot\vec{L}\sim\frac{1}{2c^{2}m_{e}^{2}} \frac{1}{a_{0}}\frac{e^{2}}{4\pi\varepsilon_{0}a_{0}^{2}}\hbar^{2}=\frac{e^{2}\hbar^{2}}{8c^{2}m_{e}^{2}a_{0}^{3}\pi\varepsilon_{0}}\\
H_{0}&= \frac{p^{2}}{2m}-\frac{e^{2}}{4\pi\varepsilon_{0}r}\sim \frac{e^{2}}{4\pi\varepsilon_{0}a_{0}}
\end{align*}$$ e fica: $$\frac{|W|}{|H_{0}|}=\frac{\hbar^{2}}{m_{e}^{2}c^{2}a_{0}^{2}}= \left(\frac{\frac{\hbar}{m_{e}a_{0}}}{c}\right)^{2}\sim \alpha^{2}$$ em que $\hbar$ tem dimensões de momento angular. Logo: $\frac{[\hbar]}{[m_{e}][a_{0}]}=\frac{m~v~r}{m~r}=v$ e temos na equação acima $\frac{v}{c}\sim\alpha$

*Termo de Darwin*
$$W_{D}=\frac{\hbar^{2}}{8m_{e}c^{2}}\Delta V(R)$$
- Este termo introduz uma correção relativista. Tem a ver com a equação de Dirac e o comportamento de uma partícula carregada em movimento, sob o efeito de um campo elétrico.
- Novamente temos $\frac{W_{D}}{|H_{0}|}\sim\alpha^{2}$.

### Estrutura Fina do Nível $n=2$
- No nível $n=1$ não existe estrutura fina. Temos simplesmente deslocamento da energia devido a $W_{mv},W_{D}$. Temos:
    - $\langle W_{mv}\rangle_{1s}=- \frac{5}{8}m_{e}c^{2}\alpha^{4}$
    - $\langle W_{D}\rangle_{1s}=\frac{1}{2}m_{e}c^{2}\alpha^{4}$
    - $\langle W_{SO}\rangle=0$

- Para $n=2$ temos nível de energia de $H_{0}$ com estados próprios $\ket{n,\ell,m}$:
$$E_{n}=\frac{m}{2\hbar} \left(\frac{e^{2}}{4\pi\varepsilon_{0}}\right)^{2} \frac{1}{n^{2}} \quad \quad;\quad \quad \Biggr\{\substack{&n\in\mathbb{N}\\ &\ell=0,\dots,n-1\\ &m_{\ell}=-\ell,\dots,0,\dots,+\ell}$$
e todos os estados têm degenerescência, devido ao spin intríseco do eletrão: $m_{s}=\pm \frac{1}{2}$. Consideremos a base $\ket{n,\ell,m_{\ell},m_{s}}$.

- A orbital 2s consiste em: $n=2,\ell=0,m_{\ell}=0,m_{s}=\pm \frac{1}{2}$
- A orbital 2p consiste em: $n=2,\ell=1,m_{\ell}=\pm1,m_{s}=\pm \frac{1}{2}$
- Ou seja, temos degenerescência $2+3\times2=8$

- Assim, para determinar o efeito de perturbação $W=W_{mv}+W_{SO}+W_{D}$ temos que diagonalizar $W$ neste subespaço 8D. Os valores próprios serão as correções à energia de 1ª ordem. Os vetores próprios são os estados correspondentes.
- Conseguimos verificar que $L^{2}$ comuta com $W$. Temos então que a matriz de $W$ é diagonal por blocos:
![[Pasted image 20240120013739.png]]

#### Nível 2s - $\ell=0$
- Temos que os termos $W_{mv},W_{D}$ mão atuam nas variáveis de spin:
$$\langle200m_{s}|W_{mv}|200m_{s}'\rangle=\delta_{m_{s}m_{s}'}\langle200|- \tfrac{p^{4}}{8m_{e}^{3}c^{2}}|200\rangle=- \tfrac{13}{128}m_{e}c^{2}\alpha^{4}\delta_{m_{s}m_{s}'}=\langle W_{mv}\rangle_{2s}\delta_{m_{s}m_{s}'}$$
$$\langle200m_{s}|W_{D}|200m_{s}'\rangle=\delta_{m_{s}m_{s}'}\langle200|\tfrac{\hbar^{2}\Delta V(R)}{8m_{e}^{2}c^{2}}|200\rangle=\tfrac{1}{16}m_{e}c^{2}\alpha^{4}\delta_{m_{s}m_{s}'}=\langle W_{D}\rangle_{2s}\delta_{m_{s}m_{s}'}$$
- Como $W_{SO}\propto\vec{L}\cdot\vec{S}$ e nesta orbital temos $\ell=0$ é imediato que $$\langle200m_{s}|W_{SO}|200m_{s}'\rangle=0$$
- E então o estado $2s$ temos energia:
$$E_{2s}=-m_{e}c^{2} \left(\frac{\alpha^{2}}{8}+\frac{5}{128}\alpha^{4}+\mathcal{O}(\alpha^{6})\right)$$

#### Nível 2p - $\ell=1$
- Temos que $W_{D},W_{mv}$ não atuam em variáveis de spin e comutam com $\vec{L}$ logo
$$\langle21m_{\ell}m_{s}|W_{mv}|21m_{\ell}'m_{s}'\rangle=\langle W_{mv}\rangle\delta_{m_{s}m_{s}'}\delta_{m_{\ell}m_{\ell}'}=- \tfrac{7}{384}m_{e}c^{2}\alpha^{4}\delta_{m_{s}m_{s}'}\delta_{m_{\ell}m_{\ell}'}$$
$$\langle21m_{\ell}m_{s}|W_{D}|21m_{\ell}'m_{s}'\rangle=\langle W_{D}\rangle\delta_{m_{s}m_{s}'}\delta_{m_{\ell}m_{\ell}'}=0$$
em que o termo de Darwin apenas tem valor médio $\neq0$ para orbitais $s$.

- O termo spin-órbita já não será nulo e temos
$$\begin{align*}
\langle 21m_{\ell}m_{s}|W_{SO}|21m_{\ell}'m_{s}'\rangle&= \langle 21m_{\ell}m_{s}|\tfrac{e^{2}}{8\pi\varepsilon_{0},m_{e}^{2}c^{2}R^{3}}\vec{L}\cdot\vec{S}|21m_{\ell}'m_{s}'\rangle\\
&= \frac{e^{2}}{8\pi\varepsilon_{0}m_{e}^{2}c^{2}}\langle \frac{1}{R^{3}}\rangle_{2p}\langle\ell=1,m_{\ell},m_{s}|\vec{L}\cdot\vec{S}|\ell=1,m_{\ell}',m_{s}' \rangle\\
&= \frac{e^{2}}{8\pi\varepsilon_{0}m_{e}^{2}c^{2}} \frac{1}{24 a_{0}^{2}}\langle\ell=1,m_{\ell},m_{s}|\vec{L}\cdot\vec{S}|\ell=1,m_{\ell}',m_{s}' \rangle\\
&= \frac{1}{48\hbar^{2}}m_{e}c^{2}\alpha^{4}\langle\ell=1,m_{\ell},m_{s}|\vec{L}\cdot\vec{S}|\ell=1,m_{\ell}',m_{s}' \rangle
\end{align*}$$
para resolver isto temos que diagonalizar $\vec{L}\cdot\vec{S}$ no subespaço em que $\ell=1,s=\frac{1}{2}$. É útil usar o operador momento angular total: $\vec J=\vec L+\vec S$. Temos
$$J^{2}=L^{2}+S^{2}+2\vec{L}\cdot\vec{S} ~~\to~~ \vec{L}\cdot\vec{S}=\frac{1}{2}(J^{2}-L^{2}-S^{2})$$
e passamos para uma base $\ket{j,M}$ com $j=\ell+s,\ell+s-1,\dots,|\ell-s|~~;~~M=-j,\dots,j$
- Nesta base o operador $\vec{L}\cdot\vec{S}$ será diagonal, com:
$$\langle j,M|\vec{L}\cdot\vec{S}|j',M'\rangle=\frac{\hbar^{2}}{2}(j(j+1)-\ell(\ell+1)-s(s+1))\delta_{jj'}\delta_{MM'}$$
por alguma razão divina isto pode ser reescrito como
$$\langle j,M|\vec{L}\cdot\vec{S}|j',M'\rangle=\frac{\hbar^{2}}{2}\left(j(j+1)- \frac{11}{4}\right)\delta_{jj'}\delta_{MM'}$$
- Assim, para um multipleto com $j=\frac{3}{2}$ temos: $\langle \tfrac32,M|\vec{L}\cdot\vec{S}|\tfrac32,M'\rangle=\frac{\hbar^{2}}{2}\delta_{MM'}$
- Para um Dubleto temos $j=\frac{1}{2}$ e ficamos com $\langle \tfrac12,M|\vec{L}\cdot\vec{S}|\tfrac12,M'\rangle=-\hbar^{2}\delta_{MM'}$

- Ou seja, se formos a calcular as energias temos:
$$\langle W_{SO}\rangle_{2p\frac12}=-\frac{\alpha^{4}}{48}m_{e}c^{2} \quad  \quad;\quad \quad \langle W_{SO}\rangle_{2p\frac32}=\frac{\alpha^{4}}{96}m_{e}c^{2}$$
e obtemos a energia total destes estados:
$$\begin{align*}
E_{2p\frac12}=-m_{e}c^{2}\left(\frac{\alpha^{2}}{8}+\frac{5\alpha^{4}}{128}+\mathcal{O}(\alpha^{6})\right)\\
E_{2p\frac32}=-m_{e}c^{2}\left(\frac{\alpha^{2}}{8}+\frac{\alpha^{4}}{128}+\mathcal{O}(\alpha^{6})\right)\\
\end{align*}$$
![[Pasted image 20240120020651.png]]
- Temos então sepração do espetro do átomo de hidrogénio, com uma separação de $\frac{4}{128}m_{e}c^{2}\alpha^{4}$.