# 1 - Princípio da Correspondência
- Todas as expressões da "Nova Física" devem coincidir com a física clássica no domínio de validade da clássica.
- Ora, a física clássica quando temos variáveis contínuas (não discretas/contáveis). 
> Por exemplo, no modelo de Bohr a energia num nível $n$ é $E_{n}=- \frac{|E_{1}|}{n^{2}}$. Vemos que consoante $n$ aumenta, a energia dos níveis vai-se tornando constante, pelo que a variável passa a ser contínua.

Analisemos então o modelo de Bohr consoante a física clássica:
- Na física clássica temos que uma carga acelerada liberta radiação. Tem-se então $f_{rad}=f_{mov}$ 
- Ora, $f_{mov}= \frac{v}{2\pi r}$ e, no modelo de Bohr: $$v_{n}= \frac{e^{2}}{4\pi \varepsilon_{0}} \frac{1}{n\hbar} \quad \quad;\quad \quad r_{n}= \frac{4\pi\varepsilon_{0}}{e^{2}} \frac{\hbar^{2}n^{2}}{m_{e}}$$
Logo $$f_{mov}=\frac{v_{n}}{2\pi r_{n}}= \left( \frac{e^{2}}{4\pi\varepsilon_{0}} \right)^{2} \frac{m_{e}}{4\pi\hbar^{3}} \frac{1}{n^{3}} \quad \quad \textsf{(Eq. 1)}$$
- Por outro lado, segundo o modelo de Bohr, temos ainda que:
$$f_{emissão}=\left( \frac{e^{2}}{4\pi\varepsilon_{0}} \right)^{2} \frac{m_{e}}{4\pi\hbar^{3}} \left(\frac{1}{n_{f}^{2}} -\frac{1}{n_{i}^{2}}\right)$$
Fazendo a substituição $n_{i}=n~~;~~n_{f}=n-1$ temos:
$$f=\left( \frac{e^{2}}{4\pi\varepsilon_{0}} \right)^{2} \frac{m_{e}}{4\pi\hbar^{3}} \frac{2n-1}{n^{2}(n-1)^{2}}$$
Para $n\to\infty$ podemos aproximar $n-1\approx n~~;~~2n-1\approx2n$. Assim, obtemos:
$$f_{emissão}(n\to\infty)=\left( \frac{e^{2}}{4\pi\varepsilon_{0}} \right)^{2} \frac{m_{e}}{4\pi\hbar^{3}} \frac{1}{n^{3}} \quad \quad \textsf{(Eq. 2)}$$

- Ora, podemos ver que as equações 1 (obtida com Física Clássica) e 2 (obtida com Física Moderna) são iguais, pois estamos no limite de validade da física clássica.

# 2 -  Espectro de Absorção
- Imaginemos que queremos saber a temperatura de uma amostra de H necessária para se ver uma risca da série de Balmer no espectro de absorção. 
    - Desde já, recordemos que série de Balmer significa que o eletrão ou sai ou acaba no nível $n=2$
    - Como queremos ter uma risca da série de Balmer no espetro de _absorção_, então o eletrão sai do nível 2 para um nível superior. (Espetro de absorção == átomo recebe energia == eletrão sobe)

- A probabilidade de um eletrão estar no nível $n=2$ é:
$$P_{2}= \frac{e^{\frac{-E_{2}}{k_{B}T}}}{e^{\frac{-E_{1}}{k_{B}T}}}=e^{- \frac{E_{2}-E_{1}}{k_{B}T}}$$
Para um átomo de hidrogénio tem-se que:
$E_{1}=-13.6~eV ~~~~;~~~~ E_{2}=\frac{E_{1}}{2^{2}}=-3.4~eV~~~~;~~~~ k_{B}= 8.65\cdot10^{-5}~eV~K^-1$ 
E como queremos saber a temperatura para a qual obtemos riscas do espectro de Balmer, é necessário que o eletrão esteja no nível $n=2$, ou seja, $P_{2}=1$
Ao mexer na equação obtemos: $T\sim 10^{6}~K$

# 3 - Estabilidade do Átomo de H
- Consideremos que temos um eletrão a orbitar o núcleo num átomo de hidrogénio, sendo que o eletrão está a cair para o núcleo ao longo do tempo.
- Do eletromagnetismo temos a equação de Larmor:
$$P= \frac{q^{2}a^{2}}{6\pi \varepsilon_{0} c^{3}}$$
(De recordar que $P$ é potência emitida por uma carga $q$ em movimento com aceleração $a$)

- No modelo de Bohr, como vimos na aula anterior:
$$E= \frac{1}{2}E_{P}= -E_{c}$$
Ora, 
$$\begin{align*}
-E_{c}&= \frac{1}{2}E_{P}\\
-\frac{1}{2}m_{e}v^{2}&= - \frac{1}{2} \frac{e^{2}}{4\pi\varepsilon_{0} r}\\
v^{2}&=  \frac{e^{2}}{4\pi\varepsilon_{0}m_{e}r}
\end{align*}$$
E temos que $\Large a=\frac{v^{2}}{r}= \frac{e^{2}}{4\pi\varepsilon_{0}m_{e}r^{2}}$

- Substituindo $a=v^{2}/r$ na equação de Larmor:
$$P = \frac{e^{2}}{6\pi\varepsilon_{0}c^{3}} \left( \frac{e^{2}}{4\pi\varepsilon_{0}m_{e}r^{2}} \right)^{2} \quad \quad \textsf{(Eq. 3)}$$

- No entanto podemos escrever:
$$\Tiny P= \frac{dE}{dt}=\frac{d}{dt}\left( \frac{1}{2}E_{P}\right)=\frac{1}{2} \frac{d}{dt}\left(\frac{e^{2}}{4\pi\varepsilon_{0}r} \right)=\frac{1}{2} \frac{e^{2}}{4\pi\varepsilon_{0}} \frac{d}{dr}\left(\frac{1}{r} \right) \frac{dr}{dt}$$
$$P=\frac{1}{2} \frac{e^{2}}{4\pi\varepsilon_{0}r^{2}} \frac{dr}{dt} \quad \quad \textsf{(Eq. 4)}$$
- Ao igualar as equações 3 e 4 temos:
$$\begin{align*}
\frac{e^{6}}{6\pi\varepsilon_{0}c^{3} (4\pi \varepsilon_{0}m_{e})^{2}} \frac{1}{r^{4}}&= \frac{1}{2} \frac{e^{2}}{4\pi\varepsilon_{0}r^{2}} \frac{dr}{dt}\\
\int_{r_{1}}^{0} r^{2}dr&= \int_{0}^{\tau} \frac{2e^{4}}{24\pi^{2}\varepsilon_{0}^{2}m_{e}^{2}}~dt  \\
\frac{2e^{4}}{24\pi^{2}\varepsilon_{0}^{2}m_{e}^{2}}\cdot \tau&= \frac{1}{3}r_{1}^3
\end{align*}$$
- Sendo que, neste caso, as integrais representam o tempo $\tau$ que o eletrão demora a cair até ao núcleo ($r=0$), começando no nível $n=1$ ($r=r_{1}$).
- Assim, ao isolar $\tau$ na equação acima e substituir os valores (que são todos conhecidos para o átomo de hidrogénio) temos $$\tau=1.05\cdot10^{-10}s$$
- Por outro lado, usando as fórmulas de $v_{n}$ e $r_{n}$ do Modelo de Bohr para o nível $n=1$, temos que o período orbital neste nível é:
$$T_{1}= \frac{2\pi r_{1}}{v_{1}}=3.95\cdot10^{-16}s$$
- Ou seja, $\tau\gg T_{1}$. Por palavras, o tempo que o eletrão demora a cair ao núcleo, _num átomo isolado!!!_, é muito maior que o período do mesmo, pelo que o átomo é estável.
- Podemos também pensar no tempo que o eletrão demora a cair no núcleo como _tempo de vida do átomo isolado_ 

# 4 - Experiência de Franck-Hertz (1914)
![[exp franck-hertz.png]]
- Temos uma montagem como na figura acima
    - O filamento $F$ aquece a faz com que sejam libertados eletrões no cátodo $C$.
    - Entre $C$ e $G$ temos uma DDP aceleradora, $V$.
    - $G$ é uma grelha
    - De $G$, os eletrões chegam ao ânodo $P$, sendo que entre $G$ e $P$ temos uma DDP retardadora, $V_0$.
    - Medimos a corrente elétrica que atinge o ânodo $P$.
    - Tudo isto ocorre dentro de uma ampola com vapor de mercúrio, Hg.

- Ao longo do seu deslocamento, os eletrões colidem com átomos de Hg. Nisto, ocorrem:
    - _Colisões Elásticas_ - $E_{f}=E_{i}$, pelo que $\Delta E_{Hg}=0$
    - _Colisões Inelásticas_ - $E_{f}\neq E_{i}$, logo $\Delta E_{Hg}\neq0$. Assim, ocorrem transições de nível por eletrões dos átomos de Hg.

- Consoante se varia a tensão aceleradora, $V$, o gráfico de $I(V)$ que se observa é:
![[fracnk-hertz i(v).png]]
- Podemos ver que logo a seguir a 4.9V temos uma descida rápida da corrente; e isso acontece para outros múltiplos de 4.9. 
- Ora, os espetros de emissão do mercúrio eram já conhecidos. E para $\lambda=254~nm$ existe uma risca no espectro. Assim:
$$\Delta E=\frac{hc}{\lambda}\longleftrightarrow 4.9 V = \frac{hc}{254~nm}$$
pelo que se tem uma igualdade.

- Ou seja, podemos compreender as descidas rápidas da corrente: para esses valores de voltagem aceleradora, a energia que os eletrões têm é exatamente aquela necessária para que a colisão com o Hg seja inelástica e ocorra uma transição de nível neste (de notar que esta é a única forma de o eletrão ceder energia ao mercúrio).
- Assim, esta experiência pode ser usada para comprovar a diferença de vários níveis orbitais.

# 5 - De Broglie (1892-1987)
- Declara que existe uma dualidade de comportamento partícula-onda na matéria. Ou seja, um corpo a mover-se com momento linear $\vec{p}$ terá um __*Comprimento de onda de Broglie*__:
$$\lambda=\frac{h}{|\vec{p}|}$$
> Por exemplo, um bola de baseball de massa $m=1~kg$ e velocidade $v=10~ms^{-1}$ (não fui eu que inventei este exemplo) ter+a comprimento de onda de $\lambda=\frac{h}{m \cdot v}=6.6\cdot10^{-35}m$

#moderna #fisica