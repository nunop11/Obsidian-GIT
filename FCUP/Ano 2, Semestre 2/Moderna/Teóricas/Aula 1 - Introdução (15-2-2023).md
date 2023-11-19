# 1 - Limites da Validade da Força Clássica
- Até agora, no curso já estudamos 2 áreas fundamentais da física:
    - _Mecânica_
    - _Eletromagnetismo_

- Vimos ainda a _relatividade_ que
    - introduz uma nova constante, $c\approx 3 \cdot 10^{8}\text{m/s}$, a velocidade da luz no vácuo
    - está definida/estruturada como uma teoria clássica

Assim, temos:
- _Teoria Newtoniana_
    - $\Large E_c=\frac{p^2}{2m}$
    - $\Large \vec{p}=m \vec{v}$

- _Teoria Relativista_
    - $\large m=\gamma ~m_0$ (sendo $m_0$ a massa em repouso, a massa aumenta consoante nos aproximamos de $c$)
    - $\large E=E_{c}+E_{0}=E_{c}+m_{0}c^{2}=\sqrt{p^{2}c^{2}+m_{0}^{2}c^{4}}=\gamma ~m_{0}c^{2}=mc^{2}$ ; $\left(\gamma=\frac{1}{\sqrt{1-\beta^2}},~~\beta=\frac{v}{c}\right)$
    - $\large\vec{p}=\gamma m_{0} \vec{v}=m \vec{v}$

### Quando se tem que usar a teoria relativista?
- Vemos então que a teoria relativista é mais geral, de modo que a newtoniana está contida na relativista (é um caso particular em que $v\ll c$)
- Ou seja, podemos utilizar a teoria de Newton num problema se $\large v \ll c$, ou seja, $\large E_{c}\ll mc^{2}$ 

- Mais à frente no curso veremos _Física Quântica_ que:
    - introduz uma nova constante: _constante de Planck_, $h=6.06 \cdot 10^{-34} \text{Js}$

- Podemos então estudar as unidades desta constante:
$$\begin{align*}
[h]&=[\text{energia}]\times[\text{tempo}]\\
&=[\text{momento angular}]\\
&=[\text{momento linear}]\times[\text{comprimento}]\\
&=[\text{ação}]=[S]\\
&=L^{2}MT^{-1}
\end{align*}$$
- Introduzimos então uma nova grandeza: **ação**, $S$. 
- De notar que apesar de esta ter as mesmas unidades que o momento angular, $S\neq L$. Na realidade, $S$ é o produto de $L$ com um ângulo (que não tem unidades), daí as duas grandezas terem as mesmas unidades.

### Quando é preciso usar Física Quântica?
__Critério 1__: Se $\Large S\gg \hbar$, então a teoria de Newton é suficiente.

> **_EX. 1_**
> Movimento da Terra em torno do Sol. Sabemos que:
> $R=149.6 \cdot10^{6}\text{ m}$ (raio da órbita, que consideramos como circular)
> $T\approx365\text{ d}$
> $v=\frac{2\pi R}{T}\approx 29.78 \cdot10^{8}\text{ m/s}$
> $M_{\bigotimes}=5.972 \cdot 10^{24}\text{ kg}$
> 
> Temos:
> $S=(M_{\bigotimes}\cdot v)(2\pi R)\approx10^{7}\text{ Js}\gg10^{-34}\approx\hbar$; Logo a teoria de newton é suficiente.
> (Note-se que em vez de $2\pi R$ podemos pôr qualquer distância do sistema como, por exemplo, o diâmetro da Terra. Esta distância não deve afeitar a prova, qualquer que ela seja)

> **_EX. 2_**
> Movimento do eletrão no átomo de Hidrogénio (no nível fundamental). Temos que:
> $m_{e}=9.1 \cdot 10^{-3} \text{ kg}$
> $v_{e}=2.2\cdot10^{6}\text{ m/s}$
> $R=5.3\cdot10^{-11}\text{ m}$ (raio da órbita)
>
>Logo:
>$S=(m_{e}\cdot v_{e})(R)\approx 6.7\cdot10^{-34}\text{ Js}\approx\hbar$; Logo a teoria de Newton não chega. Temos que usar a física quântica.
>(Novamente, em vez de $R$ podemos colocar qualquer outra distância do sistema, como o comprimento de onda de uma transição de nível)

# 2 - Radiação Térmica do Corpo Negro (Revisão)
$$R(T)=\sigma T^{4}\quad \sigma=5.67\cdot10^{-8}$$
- Acima temos a _Lei de Stefan_, que vimos em Física Térmica.
- Tem-se que $\Large R=\frac{\textsf{energia emitida}}{\textsf{área}\times \textsf{tempo}}$ 
- Vimos ainda que
$$\lambda_{\textsf{max}}\cdot T=\text{constante}$$
- Esta é a _Lei de Wien_

### Eletromagnetismo Clássico
- Considera-se que $$radiação = onda$$ 
- O número de ondas com frequência $f$ por unidade de volume:
$$n(f)df=\frac{8\pi f^{2}}{c^{3}}df$$
- Tem-se que a energia média de um modo é $$\langle\varepsilon\rangle=k_{B}T$$
- Logo, tendo uma certa cavidade em estudo, temos:
$$\rho(T)=\frac{\langle \textsf{Energia na cavidade}\rangle}{\textsf{volume}}=\frac{8\pi f^2}{c^3}k_{B}T=\frac{4\pi}{c}R(T)$$
(em que na última igualdade vemos que há isotropia)

### Planck
- A energia média de um oscilador é $k_{B}T;  \langle E_{c}+E_{p}\rangle$
- Cada oscilador terá portanto uma energia: $\varepsilon_n=nhf$$
- Pelo que a energia média de um oscilador será: $\LARGE=\frac{hf}{e^{\beta hf}-1},\quad \beta=\frac{1}{k_{B}T}$

Temos por fim:
$$\rho_{f}(T)=\frac{4\pi f^2}{c^3}\cdot\frac{hf}{e^{\beta hf}-1}$$
# 3 - Interações da Radiação com a Matéria
- Iremos estudar interações da radiação com atómos, eletrões e núcleos
- Exemplos de interações da radiação com  _eletrões_:
    - Efeito Fotoelétrico
    - Difusão de Compton
    - Difusão de Thomson
    - Difusão de Tripleto

- Exemplos de interações da radiação com  _núcleos_:
    - Produção de pares
    - Fotodesintegração

## 3.1 - Efeito Fotoelétrico
- Descoberto por Hertz em 1887 e explicado por Einstein em 1905
- Consiste na emissão de eletrões (muitas vezes chamados de fotoeletrões) por uma superfície quando nela incide radiação eletromagnética:
![[Circuito efeito fotoeletrico.png|350]]
- Como acontece:
    - A radiação eletromagnética incide na placa C
    - São emitidos eletrões
    - Aplicasse DDP entre C e A, sendo que se cria um campo elétrico como representado acima
    - Os eletrões são "arrastados" pela força gerada pelo campo elétrico para a placa A, onde eles se coletam
- Aumentar $V_{CA}$ aumenta o número de eletrões a chegar à placa A.
- Se tivermos a DDP com sinal oposto, temos uma _DDP retardadora_. O potencial em que nenhum eletrão chega a A é o _potencial de paragem_.
- Assim, definimos 
$$i=\textsf{intensidade de corrente}=\frac{dq}{dt}=n_{e}|e|\quad; \quad n_{e}=\frac{\textsf{número de eletrões}}{\textsf{tempo}}$$
$$I=\textsf{intensidade da radiação}\longrightarrow I=\frac{1}{2}\varepsilon_{0}E^{2}\tiny\textsf{(porque consideramos que radiação = onda)}$$
![[I(i) efeito fotoeletrico.png|250]]  ![[ii(V) efeito fotoeletrico.png|400]]  ![[V0(f) efeito fotoeletrico.png|275]]

#moderna #fisica #relatividade 