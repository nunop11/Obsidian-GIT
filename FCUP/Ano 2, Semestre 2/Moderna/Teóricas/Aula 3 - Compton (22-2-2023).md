# 1 - Difusão da Radiação pela Matéria
![[Colisão de fotão com eletrão no atomo.png|400]] ![[I'(lambda ') para difusão de compton.png|385]]

## 1.1 -  Teoria Ondulatória da Radiação
- Segundo esta teoria, temos que a radiação incidente é dada por $\large\vec{E}=\vec{E}_0\cos(\vec{k}\cdot \vec{r}-wt)$
    - Sendo que $\large\vec{k}=\frac{2\pi}{\lambda}\hat{u}$ é o _vetor de onda_, sendo que $\hat{u}$ é o versor que indica a direção de propagação da onda.
- Para o eletrão em que a radiação incide temos:
$$\vec{F}=-e \vec{E}=m_{e}\vec{a}\longrightarrow \vec{a}=\frac{-e \vec{E}_0}{m_{e}}\cos(\vec{k}\cdot \vec{r}-wt)$$
- Temos ainda que uma carga elétrica $q$ com aceleração $\vec{a}$ emite uma radiação de potência:
$$P = \frac{2}{3}\frac{q^{2}a^{2}}{4\pi\varepsilon_{0}c^{3}}$$
(Esta é a _Fórmula de Larmor não relativista_)
- Ou seja, segundo esta teoria, não deveria de ocorrer difusão a comprimentos de onda diferentes de $\lambda$, ou seja, teríamos sempre que $\lambda'=\lambda$ 

## 1.2 - Explicação de Compton (1922)
- A difusão pode ser explicada por $$\gamma+e^{-}\longrightarrow \gamma~' + e^{-}$$
![[Colisão de fotao com eletrao no referencial do eletrão.png|375]]

- Podemos ver que o fotão incidente neste processo tem que ter muito mais energia do que aqueles presentes no efeito fotoelétrico.

- No referencial do eletrão temos:
$$E_{\gamma}=p_{\gamma}c \quad E_{e}=m_{e}c^{2}\quad \vec{p}_e=\vec{0}\quad E_\gamma'=p_{\gamma'}c \quad E_{e}'=\sqrt{p_{e}^{2}c^{2}+m_{e}^{2}c^{4}}$$
#### Conservação do momento linear:
$$\begin{align*}
\vec{p}_{i}&=\vec{p}_f\\
\vec{p}_{\gamma}+ \vec{p}_{e}&=\vec{p}~'_{\gamma}+\vec{p}~'_{e}\\
\vec{p}~'_{e}&=\vec{p}_{\gamma}-\vec{p}~'_{\gamma} \quad \quad \textsf{(Eq. 1)}
\end{align*}$$
- Se fizermos o produto escalar de cada lado da equação 1 com si próprio temos:
$$
\begin{align*}
\vec{p}~'_{e}\cdot\vec{p}~'_{e}&=(\vec{p}_{\gamma}-\vec{p}~'_{\gamma})\cdot(\vec{p}_{\gamma}-\vec{p}~'_{\gamma})\\
p_{e}^{'~2}&=p_{\gamma}^{2}+p_{\gamma}^{'~2}-2p_{\gamma}p~'_{\gamma}\cos \theta \quad \quad \textsf{(Eq. 2)}\\
\end{align*}
$$
- Ao multiplicar todos os termos da Eq. 2 por $c^{2}$ temos:           $\large p_{e}^{'~~2}c^{2}=p_{\gamma}^{2}c^{2}+p_{\gamma}^{'~~2}c^{2}-2p_{\gamma}p~'_{\gamma}c^{2}\cos \theta$

#### Conservação da energia:
$$\begin{align*}
E_{i}&=E_{f}\\
E_{\gamma}+E_{e}&=E_\gamma'+E_{e}'\\
\end{align*}$$
- Se substituirmos as energias pelos valores que estão indicados acima sobre esta colisão no referencial do eletrão obtemos:
$$p_{\gamma}c + m_{e}c^{2}+ Be = p~'_{\gamma}c+\sqrt{p_{e}^{'~2}c^{2}+m_{e}^{2}c^{4}} \quad \quad \textsf{(Eq. 3)}$$
- $Be$ é a energia de ligação atómica. Ora, no átomo de hidrogénio esta é de $-13.6 \text{ eV}$. Quanto mais perto do núcleo maior esta será em módulo.
- Ora, a difusão de Compton está associada a radiações do tipo raio X em que a radiação tem uma energia que ronda os $\text{keV}$ e $\text{MeV}$. Assim, considera-se que $Be \approx 0$. Por outras palavras, estamos a _considerar eletrões livres_

- Assim, ao meter ambos os lados da eq. 3 ao quadrado temos:   
$$\begin{align*}
(\sqrt{p_{e}^{'~2}c^{2}+m_{e}^{2}c^{4}})^{2}&=(p_{\gamma}c-p~'_{\gamma}c+m_{e}c^{2})^{2}\\
p_{e}^{'~2}c^{2}+\cancel{m_{e}^{2}c^{4}}&=p_{\gamma}^{2}c^{2}+p_{\gamma}^{'~2}c^{2}-2p_{\gamma}p~'_{\gamma}c^{2}+\cancel{m_{e}^{2}c^{4}}+2p_{\gamma}c \cdot m_{e}c^{2}-2p~'_{\gamma}c \cdot m_{e}c^{2} 
\end{align*}$$
Podemos então substituir $p_{e}^{'~2}$ conforme a Eq. 2. Temos então $p_{e}^{'~2}c^{2} = p_{\gamma}^{2}c^{2}+p_{\gamma}^{'~2}c^{2}-2p_{\gamma}p~'_{\gamma}\cos \theta c^{2}$, logo:
$$\begin{align*}
\cancel{p_{\gamma}^{2}c^{2}}+\bcancel{p_{\gamma}^{'~2}c^{2}}-2p_{\gamma}p~'_{\gamma}\cos \theta c^{2}&= \cancel{p_{\gamma}^{2}c^{2}}+\bcancel{p_{\gamma}^{'~2}c^{2}}-2p_{\gamma}p~'_{\gamma}c^{2}+2p_{\gamma}m_{e}c^{3}-2p~'_{\gamma} m_{e}c^{3}\\
2p_{\gamma}p~'_{\gamma}c^{2}-2p_{\gamma}p~'_{\gamma}\cos \theta c^{2}&=2p_{\gamma}m_{e}c^{3}-2p~'_{\gamma} m_{e}c^{3}\\
2p_{\gamma}p_{\gamma}~'c^2(1-\cos\theta)&=2m_{e}c^{3}(p_{\gamma}-p_{\gamma}~')
\end{align*}$$
Dividimos os 2 lados por $2p_{\gamma}p_{\gamma}~'c^2$ e temos:
$$1-\cos\theta=m_{e}c \left(\frac{1}{p_{\gamma}~'} - \frac{1}{p_{\gamma}} \right)$$
- Já vimos que $\large E = pc = hf$, logo $\Large p=\frac{h}{\lambda}$. Ao substituir na equação acima, finalmente, temos:
$$\begin{align*}
1-\cos\theta &= \left(\frac{\lambda'}{h} - \frac{\lambda}{h}\right)m_{e}c\\
\lambda' &= \lambda+\frac{h}{m_{e}c}(1-\cos\theta)
\end{align*}$$
- Ou seja, finalmente mostramos que na teoria cospuscular da matéria, como a radiação é composta por fotões, é possível que a difusão ocorra com $\lambda'\neq \lambda$

### Observações
1. Se $\theta=0$, então $\cos\theta=1$, logo $\lambda'=\lambda$
2. A difusão de Compton é um processo não determinista. Ou seja, nunca é possível determinar tudo (há mais variáveis do que aspetos que podemos determinar)
3. Como podemos explicar $\lambda' = \lambda$ para $\theta\neq0$?
    - Na dedução acima consideramos apenas eletrões e apenas quando $Be \approx0$, ou seja, eletrões livres.
    - Imaginemos então que um fotão colide com um eletrão muito fortemente ligado ao núcleo. Podemos interpretar isto como sendo um fotão a colidir com o núcleo em si.
    - Sendo $M$ a massa do núcleo temos $\large \lambda' = \lambda+\frac{h}{Mc}(1-\cos\theta)$. Ora, como $M\approx 10^{3}m_{e}$, podemos facilmente ver que o segundo termo se torna desprezável.
4. Comprimento de onda de Compton do eletrão: $$\frac{h}{m_{e}c}=2.43 \cdot 10^{-12} \text{ m}$$

# 2 - Raios X
![[Circuito de geração de raios X.png|450]]
- Aplica-se uma tensão elevada no filamento. Ele aquece até uma temperatura elevada, de modo que libertam eletrões pelo efeito termiónico.
- Aplica-se uma DDP elevada entre A e C (de dezenas ou centenas de keV). Devido a esta, os eletrões aceleram e embatem no ânodo (A)
- Devido a esta colisão, é emitida radiação.

- O gráfico $I(\lambda)$ deste tipo de radiação é dado por:
![[I(lambda) para raios X.png|450]]

- Assim, queremos explicar:
    - Formato da função
    - Existência e qual é o $\lambda_{min}$
    - Existência do espectro discreto

## 2.1 - Segundo a TOR
![[Eletrão a passar perto ao nucleo.png|500]]

- Temos 
$$F = m_{e}a=\frac{1}{4\pi\varepsilon_{0}} \frac{ze^{2}}{r^{2}}$$
Ou seja, $\Large a \propto \frac{z}{r^{2}}$. A fórmula de Larmor não relativista, que vimos acima, diz que $\Large P\propto a^{2}$
- Ora, estas equações permitem-nos chegar à _Radiação de Bremsstrahlung_ (radiação libertada quando um eletrão livre é acelerado ao passar perto de um núcleo), que é descrita pelo Espetro Contínuo do gráfico $I(\lambda)$.
- Assim, a TOR explica o espetro contínuo, mas não explica $\lambda_{min}$ nem o espetro discreto.

> *__Raios X com protões__*
> Imaginemos que se pretendia produzir raios X com protões. Vamos comparar as potências produzidas por cada caso:
> $$\frac{P_{p}}{P_{e}}=\frac{(\frac{z}{m_{p}})^{2}}{(\frac{z}{m_{e}})^{2}}\propto \frac{m_{e}^{2}}{m_{p}^{2}}\approx (10^{-3})^{2} = 10^{-6}~~~~\longrightarrow~~~~ P_{p}=10^{-6}P_{e}$$
> Ou seja, para as mesmas condições, o processo de produção de raio X com protões iria gerar uma potência um milhão de vezes menor, pelo que é uma muito pior opção.

## 2.2 - Segundo a TCR
- Antes de mais, recordemos que que $\large E_{\gamma}=pc=\frac{hc}{\lambda}$
- A colisão em estudo é a colisão de um eletrão acelerado por uma DDP, $V$, com um protão. Após a colisão é libertado um fotão.
- Aplicando a conservação de energia a esta colisão:
$$\begin{align*}
E_{e}+E_{\text{nuc}}&=E_{e}~'+E_\text{nuc}~' + E_\gamma\\
eV + Mc^{2} &= E_{e}~' + (E_{c}+ Mc^{2})+E_\gamma
\end{align*} $$
- Consideramos que o núcleo está inicialmente em repouso e que a colisão não o afeta. Assim, $E_{c}\approx0$
- Vamos supor ainda que, na colisão, o eletrão perde toda a sua energia, ou seja, $E_{e}~'=0$
- Temos:
$$eV + \cancel{Mc^{2}}=0 + 0+ \cancel{Mc^{2}}+ \frac{hc}{\lambda} \leftrightarrow eV = \frac{hc}{\lambda}$$
- Ora, este caso particular consiste no caso em que o comprimento de onda da radiação emitida será mínimo. Assim:
$$\lambda_{min}=\frac{hc}{eV}$$
- E assim explicamos a existência e qual é o comprimento de onda mínimo.
- Só resta explicar o espetro discreto. No entanto, esse será explicado mais à frente, ao estudar modelos atómicos.

#moderna #fisica #compton