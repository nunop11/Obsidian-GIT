# 1 - Anti-partículas
- Partículas com a mesma massa e spin, mas com carga elétrica de sinal oposto. (definição geral). Exemplos:
$$\begin{align*}
e^{-}&\longrightarrow e^{+}~~\textsf{(Positrão)}\\
p &\longrightarrow \overline{p} ~~ \textsf{(Anti-protão)}\\
n &\longrightarrow \overline{n} ~~  \textsf{(Anti-neutrão)}\\
\mu^{-} &\longrightarrow \mu^{+} ~~ \textsf{(Anti-muão)}
\end{align*}$$
- Na realidade, é uma partícula em que todas as subpartículas são anti-partículas da original. Por exemplo, um protão é $p\approx u~u~d$ (2 quarks u e 1 quark d) e o anti-protão é $\overline{p}\approx \overline{u}~\overline{u}~\overline{d}$. Um neutrão é $n \approx d~d~u$. Mas neutrões não têm carga. Poderíamos pensar que então não existe um anti-neutrão. No entanto existe e é $\overline{n}=\overline{d}~\overline{d}~\overline{u}$.
-  A diferença entre a massa e a diferença entre o módulos das cargas é tão reduzida que não é possível medi-la.

# 2 - Produção de Pares (PP)
- De uma forma geral temos:
$$\gamma \longrightarrow  \textsf{partícula} + \textsf{anti-partícula}$$
- Alguns exemplos:
$$\begin{align*}
\gamma &\rightarrow e^{-}+e^{+}\\
\gamma &\rightarrow p + \overline p\\
\gamma &\rightarrow \mu^{-}+\mu^{+}\\
\end{align*}$$
## 2.1 - Aniquilação de Pares
- Temos
$$\textsf{partícula}+\textsf{anti-partícula}\longrightarrow \gamma, 2\gamma, 3\gamma \dots$$
## 2.2 - Mostrar que PP não ocorre no vácuo
- Imaginemos que a produção de pares ocorre no vácuo
![[produçao de pares.png|450]]

#### Conservação de Energia
$$\begin{align*}
E_{\gamma}&= E_{-}+E_{+}\\
&= (E_{c-}+m_{e}c^{2}) + (E_{c+}+m_{e}c^{2})\\
&= \gamma m_{e}c^{2}+\gamma m_{e}c^{2} \\
&= 2\gamma m_{e}c^{2} \quad ; \quad \gamma=\frac{1}{\sqrt{1-\left(\frac{v}{c}\right)^2}}\\
\end{align*}$$
- De recordar que vimos na aula 1 que $\large E=E_{c}+m_{e}c^{2}=\gamma m_{e}c^{2}$
- Estamos ainda a considerar que: $\large m_{e^{+}}\approx m_{e^{-}}=m_{e}$
- Temos então a eq.1:
$$E_{\gamma}=hf=\frac{hc}{\lambda}=2\gamma m_{e}c^{2} \quad \quad \textsf{(Eq. 1)}$$

#### Conservação de Momento Linear
$$\vec{p}_\gamma=\vec{p}_{-}+\vec{p}_{+}$$
- Consideremos apenas a componente dos $x$:
$$\begin{align*}
x:\quad \frac{h}{\lambda}&= 2p\cos\theta\\
\frac{h}{\lambda}&= 2\gamma m_{e} v \cos\theta\\
\frac{h}{\lambda}&= 2\gamma m_{e} c^{2}\left(\frac{1}{c}\right)\left(\frac{v}{c}\right)\cos\theta \quad \quad \textsf{(Eq. 2)}
\end{align*}$$
- De recordar, da aula 1, que: $\large p = \gamma m_{e} v$

- Ao multiplicar a $Eq.2$ por $c$ temos:
$$\frac{hc}{\lambda}= 2\gamma m_{e} c^{2}\left(\frac{v}{c}\right)\cos\theta$$
que claramente é diferente da $Eq.1$:
$$\frac{hc}{\lambda}=2\gamma m_{e}c^{2}$$
- E como $\frac{v}{c}<1$ e $\cos\theta<1$, temos que se obtem uma energia $E=\frac{hc}{\lambda}$ menos a partir da eq.2 do que da eq.1. Ora, isto é _impossível_. Assim, PP não pode acontecer no vácuo.

#### Conclusão
- PP só ocorre na presença de um 3º corpo:

## 2.3 - Energia Mínima para PP, PT
$$\begin{align*}
PP:\quad (E_{\gamma})_{L} &= 2 m_{e}c^{2}=2\times0.511 \frac{\text{MeV}}{c^2}c^{2}=1.022\text{ MeV}\\
PT:\quad (E_{\gamma})_{L} &= 4 m_{e}c^{2}=2.044 \text{ MeV}
\end{align*}$$
- Tem-se ainda que
$$\gamma\rightarrow p+\overline p:\quad (E_{\gamma})_{L}=2mpc^{2}\approx 2000 \text{ MeV}\approx 2 \text{ GeV}$$

### 2.3.1 - PP
- Para Produção de Pares ($\gamma\rightarrow e^{-}+e^{+}$) na vizinhança de um núcleo $N$ de massa $M$, fazemos
#### Conservação de Energia
$$\begin{align*}
E_{\gamma}+Mc^{2}&= E_{e^{-}}+E_{e^{+}}+E~'_{N}\\
E_{\gamma}+\cancel{Mc^{2}}&= (E_{c}^{-}+m_{e}c^{2})+(E_{c}^{+}+m_{e}c^{2})+(E_{c}^{N}+\cancel{Mc^{2}}) \quad \textsf{(Eq.3)}
\end{align*}$$

- A energia mínima será então $E_{\gamma}=2m_{e}c^{2}$. Isto porque temos 2 eletrões e a energia de repouso de cada eletrão é $m_{e}c^{2}$. Se considerarmos o referencial do CM então é como se o eletrão e positrão estivessem em repouso depois da colisão. Assim, se $E_{\gamma}=2m_{e}c^{2}$, ficamos com $E_{c}^{N}=0$, o que faz sentido.

### 2.3.2 - PT
- Para Produção Tripleto ($\gamma \rightarrow e^{+}+e^{-}$) na vizinhança de um eletrão $e^{0}$

- Para esta demonstração é necessário notar que:
    - A massa do eletrão (em movimento) será representada como $m$
    - A massa de repouso do eletrão é $m_{0}=m_{e}$
    - Será usada a definição relativista de massa: $\Large m = m_{0}\gamma$
    - Iremos considerar que antes da colisão o eletrão $e^{0}$ está em repouso e que após a colisão as 3 partículas têm a mesma velocidade. 

#### Conservação de momento linear
- Recordemos que $\Large p=\gamma~ m_{0} v=m v$
- Como as 3 partículas têm a mesma velocidade após a colisão, então também têm o mesmo momento linear, $p$. Assim
$$\begin{align*}
p_{\gamma}&=  p + p + p\\
p_{\gamma} &= 3m v = \frac{E_{\gamma}}{c}\\
E_{\gamma}&= 3m vc\\
E_{\gamma} &= 3m \frac{v}{c}c^{2}\\
E_{\gamma} &= 3 m c^{2} \cdot\beta 
\end{align*}$$

#### Conservação de Energia
- Recordemos que $\Large E=\gamma~m_{0}c^{2}=mc^{2}$
- Como consideramos que as velocidades das 3 partículas são iguais, após a colisão temos $E_{e^{-}}=E_{e^{+}}=E_{e^{0}}=mc^{2}$:
$$\begin{align*}
E_{\gamma} + E_{e^{0}}&= E_{e^{-}}+E_{e^{+}}+E~'_{e^{0}}\\
E_{\gamma}+m_{0}c^{2}&= mc^{2}+mc^{2}+mc^{2}\\
m_{0}c^{2} &= 3 mc^{2}-E_{\gamma}\\
m_{0}\cancel{c^{2}} &= 3m\cancel{c^{2}}(1-\beta)\\
1-\beta&= \frac{m_{0}}{3m}
\end{align*}$$

- Ora, como $\large m=m_{0}\gamma$ temos
$$\begin{align*}
1-\beta &= \frac{\cancel{m_{0}}}{3\cancel{m_{0}}\gamma}\\
3\gamma-3\gamma\beta &= 1\\
\frac{3}{\sqrt{1-\beta^{2}}}- \frac{3\beta}{\sqrt{1-\beta^{2}}} &= 1\\
3-3\beta &= \sqrt{1-\beta^{2}}\\\\
\longrightarrow \beta&= \frac{4}{5}
\end{align*}$$
- Assim temos $\gamma=\frac{5}{3}$, logo $\large m=\frac{5}{3}m_0$, ou seja $\Large m=\frac{5}{3}m_{e}$
- Podemos então substituir isto na formula da conservação do momento linear que obtivemos acima:
$$E_{\gamma}=3mc^{2} \beta=3\cdot \frac{5}{3}m_{e}c^{2}\cdot  \frac{4}{5}=4m_{e}c^{2}$$

# 3 - Referenciais
- Consideremos a colisão descrita como:
$$\text{1}+\text{2}\longrightarrow \text{3}+\text{4}$$
- Em qualquer referencial temos
    - Conservação de Energia: $E_{i}=E_{f}$
    - Conservação de Momento Linear: $p_{i}=p_{f}$

- Ou seja, para 2 referenciais $S$ e $S'$ temos:
$$\begin{align*}
E_{i}=E_{1}+E_{2} \quad ;&\quad p_{i}=p_{1}+p_{2}\\
E_{f}=E_{3}+E_{4} \quad ;&\quad p_{f}=p_{3}+p_{4}\\
E_{i}^{2}-p_{i}^{2}c^{2}\bigg|_{S}&= E_{f}^{2}-p_{f}^{2}c^{2}\bigg|_{S}\\
E_{i}^{2}-p_{i}^{2}c^{2}\bigg|_{S~'}&= E_{f}^{2}-p_{f}^{2}c^{2}\bigg|_{S~'}
\end{align*}$$
- Tem-se ainda que $\Large E^{2}-p^{2}c^{2}$ é a _Invariante de Lorentz_, que é igual em todos os referenciais.
- Normalmente iremos considerar $S$ como sendo o _referencial do LAB_ e $S'$ como _referencial do CM_.

## 3.1 - Aplicação prática
- Apliquemos isto a produção de pares na proximidade de um núcleo:
$$\begin{align*}
1+2&\longrightarrow3+4+5\\
\gamma+\textsf{nucleo}&\longrightarrow e^{-}+e^{+}+\textsf{nucleo}
\end{align*}$$
em que $2$ está em repouso em $S$ (ref Lab)
- Calculemos a invariante de lorentz na situação inicial (NOTA: $E=\sqrt{p^{2}c^{2}+m^{2}c^{4}}$ ):
$$\begin{align*}
E=E_{1}+E_{2}\quad &;\quad \vec{p}=\vec{p}_{1}+\vec{0}\quad \textsf{(Referencial do LAB)}\\
(E_{1}+E_{2})^{2}-p_{1}^{2}c^{2}&=E_{1}^{2}+E_{2}^{2}+2E_{1}E_{2}-p_{1}^{2}c^{2}\\
&= \cancel{p_{1}^{2}c^{2}} + m_{1}^{2}c^{4} + \cancelto0{p_{2}^{2}c^{2}} + m_{2}^{2}c^{4}+ 2m_{2}c^{2}\sqrt{p_{1}^{2}c^{2}+m_{1}^{2}c^{4}}-\cancel{p_{1}^{2}c^{2}}\\
&= m_{1}c^{4}+m_{2}c^{4}+2E_{1}m_{2}c^{2}
\end{align*}$$
- Calculemos a invariante de lorentz na situação final:
$$\begin{align*}
E=E_{3}+E_{4}+E_{5} \quad &;\quad \vec{p}=\vec{p}_{1}+\vec{p}_{2}+\vec{p}_{3}=\vec{0} \quad\textsf{(Referencial do CM)}\\
(E_{3}+E_{4}+E_{5})^{2}&= [(m_{3}+m_{4}+m_{5})c^{2}]^{2}
\end{align*}$$
- Ora, no caso do limite mínimo de energia, $\large \vec{p}_{3}=\vec{p}_{4}=\vec{p}_{5}=\vec{0}$, pelo que $\large E_{3}=m_{3}c^{2}, E_{4}=m_{4}c^{2}, E_{5}=m_{5}c^{2}$

- Temos então que a energia limiar do fotão ($E_{1}=E_{L}$):
$$\begin{align*}
(E^{2}-p^{2}c^{2})\bigg|_{i, S}&= (E^{2}-p^{2}c^{2})\bigg|_{f, S'}\\
m_{1}^{2}c^{4}+m_{2}^{2}c^{4}+2E_{L}m_{2}c^{2}&= (m_{3}+m_{4}+m_{5})^{2}c^{4}\\
E_{L}&= \frac{(m_{3}+m_{4}+m_{5})^{2}c^{4}-m_{1}^{2}c^{4}-m_{2}^{2}c^{4}}{2m_{2}c^{2}}
\end{align*}$$
### 3.1.1 - PP
$$\begin{align*}
1+2&\longrightarrow 3+4+5\\
\gamma+N&\longrightarrow  e^{-}+e^{+}+N
\end{align*}$$
- Ou seja, $m_{1}=m_{\gamma}=0, ~m_{3}=m_{4}=m_{e}, ~m_{2}=m_{5}=1000m_{e}\gg m_{e}$. Substituindo na equação acima temos:
$$\begin{align*}
E_{L}^{\gamma}&= \frac{(2m_{e}+M)^{2}c^{4}-M^{2}c^{4}}{2Mc^{2}}\\
&= \frac{4m_{e}^{2}c^{4}+4m_{e}Mc^{4}+\cancel{M^{2}c^{4}}-\cancel{M^{2}c^{4}}}{2Mc^{2}}\\
&= \cancelto0{\frac{4m_{e}c^{4}}{2Mc^{2}}} + \frac{4m_{e}~\cancel{M}c^{4}}{2~\cancel{M}c^{2}}\\
&= 2m_{e}c^{4}
\end{align*}$$

### 3.1.2 - PT
$$\begin{align*}
1+2 &\longrightarrow 3+4+5\\
\gamma+e^{-} &\longrightarrow e^{+}+e^{-}+e^{-}
\end{align*}$$
- Ou seja, $m_{1}=m_{\gamma}=0,~m_{2}=m_{3}=m_{4}=m_{5}=m_{e}$. Ao substituir na equação que obtivemos em 3.1, temos:
$$\begin{align*}
E_{L}^{\gamma}&= \frac{(3m_{e})^{2}c^{4}-m_{e}^{2}c^{4}}{2m_{e}c^{2}}\\
&= \frac{9m_{e}^{2}c^{4}-m_{e}^{2}c^{4}}{2m_{e}c^{2}}\\
&= 4m_{e}c^{2}
\end{align*}$$

#moderna #fisica 