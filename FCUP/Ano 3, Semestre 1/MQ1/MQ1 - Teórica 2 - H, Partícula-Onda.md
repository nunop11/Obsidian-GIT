# Hamiltoniano
- Na prática, representa a energia total do sistema
- Definimos $H$ como dependendo das coordenadas generalizadas ($q_{a}$) e dos momentos conjugados ($p_{a}$), assim:
$$H=H(q_{a},p_{a},t)=\sum\limits_{a}\dot{q}_{a} p_{a} - \mathcal{L}(q_{a},\dot{q}_{a},t)$$
de notar que para obter o Hamiltoniano, temos que reescrever os termos $\dot{q}_{a}$ do Lagrangeano em função de $p_{a}$.

**Variação de H**
- Consideremos uma variação de posição e momento. Veremos como afeta $H$:
$$dH = \sum\limits_{a}\left(\frac{\partial H}{\partial q_{a}} d q_{a} + \frac{\partial H}{\partial p_{a}}d p_{a}\right)$$
a partir da definição de $H$ acima obtemos: (Não sei de onde vem o $d \dot{q}_{a}$)
$$\begin{align*}
dH &=  \sum\limits_{a}(p_{a}d \dot{q}_{a} + \dot{q}_{a}dp_{a})- dL\\
&= \sum\limits_{a}\left( \cancel{p_{a}d \dot{q}_{a}} + \dot{q}_{a}dp_{a}- \frac{\partial \mathcal{L}}{\partial q_{a}} dq_{a} - \cancel{\frac{\partial \mathcal{L}}{\partial \dot{q}_{a}}d \dot{q}_{a}} \right)\\
&= \sum\limits_{a}(\dot{q}_{a}dp_{a} - \dot{p}_{a} dq_{a})
\end{align*}$$
(Da 1ª para a 2ª linha usei $p_{a}=\frac{\partial \mathcal{L}}{\partial \dot{q}_{a}}$. Da 2ª para a 3ª linha usei a equação Euler-Lagrange: $\frac{\partial \mathcal{L}}{\partial q_{a}}=\frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{q}_{a}}=\frac{d}{dt} p_{a}=\dot{p_{a}}$)
- Da equação acima obtemos:
$$\frac{\partial H}{\partial q_{a}}=-\dot{p}_{a} \quad \quad; \quad \quad \frac{\partial H}{\partial p_{a}}=\dot{q}_{a}$$
são estas as **Equações Hamiltonianas**!

- De notar que, para um sistema com $N$ coordenadas generalizadas, teríamos $N$ equações de Euler-Lagrange, sendo estas equações de 2º grau. No entanto teríamos $2N$ equações Hamiltonianas, mas de 1º grau.

## Equação de Evolução Temporal de Função
(Em Mecânica Quântica, a "função" será chamada "observável")
- Sendo $f=f(q,p,t)$ temos:
$$\begin{align*}
\frac{df}{dt}&= \frac{\partial f}{\partial t} + \frac{\partial f}{\partial q} \frac{dq}{dt} + \frac{\partial f}{\partial p} \frac{dp}{dt}\\
&= \frac{\partial f}{\partial t} + \frac{\partial f}{\partial q}\dot{q} + \frac{\partial f}{\partial p} \dot{p}
\end{align*}$$
- Aqui, como temos na realidade $f=f(q(t),p(t),t)$ então a derivada no tempo fica do tipo: $\frac{\partial}{\partial t} + \frac{dq}{dt} \frac{\partial}{\partial q} + \frac{dp}{dt}\frac{\partial}{\partial p}$
- Além disso, deve-se notar que estamos a usar a notação em que: $$\frac{\partial f}{\partial q} \frac{dq}{dt} = \sum\limits_{i=1}^{N} \frac{\partial f}{\partial x^{i}} \frac{d x^{i}}{dt}$$
- Substituindo as equações de Hamilton na equação acima temos:
$$\begin{align*}
\frac{df}{dt}&= \frac{\partial f}{\partial t} + \frac{\partial f}{\partial q} \frac{\partial H}{\partial p} - \frac{\partial f}{\partial p} \frac{\partial H}{\partial q}\\
&\equiv \frac{\partial f}{\partial t} + \{f, H\}
\end{align*}$$
em que, claro: $$\{f,H\}=\frac{\partial f}{\partial q} \frac{\partial H}{\partial p} - \frac{\partial f}{\partial p} \frac{\partial H}{\partial q}$$

- Temos que, no *caso particular* em que $f=H$ ficamos com $\{f,H\}=0$. Assim tem-se: $$\frac{dH}{dt}=\frac{\partial H}{\partial t}$$
ou seja, $H$ só depende do tempo (temos conservação de Energia).

>**EXEMPLO - Oscilador Harmónico Simples**
>- Vimos na aula anterior que $$\mathcal{L}=\frac{1}{2}m \dot{x}^{2} - \frac12 k x^{2}$$
>- Obtemos o momento conjugado: $$p=\frac{\partial \mathcal{L}}{\partial \dot{x}}=m \dot{x} \quad \quad \longrightarrow \quad \quad \dot{x}=\frac{p}{m}$$
>logo:$$\mathcal{L}=\frac{p^{2}}{2m} - \frac12kx^{2}$$
>- Facilmente temos que o Hamiltoniano é: $$H=p \dot{x}- \mathcal{L}=\frac{p^{2}}{2m}+\frac12kx^{2}$$
>- Apliquemos agora as 2 equações de Hamilton:
>$$\frac{\partial H}{\partial x}=- \dot{p} \quad \longrightarrow \quad kx=- \frac{dp}{dt} \quad \quad \quad \textsf{(2ª Lei de Newton)}$$$$\frac{\partial H}{\partial \dot{x}}= \dot{x} \quad \longrightarrow \quad \frac{p}{m}= \dot{x} ~~\Leftrightarrow~~ p=m \dot{x} \quad \quad \textsf{(Verdadeiro, sabemos desde mecânica)}$$

## 1.2 - Nova Física
- A primeira grande teoria sobre a luz foi a *Teoria Corpuscular da Luz* de Newton. Surgiu então a Ótica Geométrica.
- Posteriormente, devido às equações de Maxwell e ao avanço do eletromagnetismo, no final do século XIX a teoria prevalente era a *Teoria Ondulatória da Luz*.
- No entanto, ainda em 1900 a teoria ondulatória não conseguia explicar o **corpo negro**:
![[Desastre UV.png]]
Aqui vemos que a física clássica levaria a pensar que a densidade energética aumenta muito rapidamente com a frequência. No entanto, a física moderna assim como experiências realizadas mostram que não é esse o caso. Na realidade temos um pico, a partir do qual a densidade energética diminui com a frequência. Chama-se a esta completa discordância entre as 2 teorias neste problema de "Desastre do UV".
- Assim, Planck postulou que a energia da radiação está discretizada: $$\boxed{E=n h \nu}$$
em que $n$ é o número de fotões, $h$ a constante de Planck e $\nu$ a frequência da radiação.
- Assim, o quantum da energia é o fotão, de energia $h \nu$

## Efeito Fotoelétrico (1905, Einstein)
- Consiste na remoção de eletrões de um material devido à incidência de um feixe de luz.
![[Efeito Fotoeletrico.png|361]]
- Verificou-se ainda que só há remoção de eletrões acima de uma certa frequência crítica. Ou seja, mesmo que um feixe de luz seja muito energético (muitos fotões por unidade de tempo), se a energia for inferior à necessária não irão ser libertados eletrões. Isto porque a energia de 1 fotão será sempre $h \nu$ e 1 eletrão é removido por 1 fotão **apenas**.

## Experiência de Young (1801)
![[experiencia Young.png|850]]

- Tem-se representado na figura acima:   
    - Se taparmos a fenda 2, é transmitida uma onda com intensidade $I_{1}(x)\propto |E_{1}(x)|^{2}$
    - Se taparmos a fenda 1, é transmitida uma onda com intensidade $I_{2}(x)\propto |E_{2}(x)|^{2}$
    - Se tivermos as 2 fendas abertas **NÃO** observamos $I=I_{1}+I_{2}$. Invés disso vemos $I_{12}(x)\propto |E_{1}(x)+E_{2}(x)|^{2}$ (isto torna possível que as ondas transmitidas pelas 2 fendas se anulem em certos pontos)

**E se tivessemos um feixe muito pouco energético, de forma que basicamente tenhamos 1 fotão sozinho?**
- **NÃO** se vê uma versão mais ténue do traçado que víamos com uma onda.
- **VEMOS** um impacto localizado. Isto mostra que o fotão não se divide nas 2 fendas como uma onda. Ou seja, *a teoria ondulatória não é suficiente*.

**E se, por outro lado, tivermos um feixe pouco energético, mas deixarmos passar bastante tempo, de forma a passarem $N$ fotões?**
- Se esperarmos tempo suficiente veremos que, de facto, se obtém o mesmo traçado que com ondas. Isto leva a concluir que, na realidade, o traçado acima indica a **probabilidade**.

**Conclusões da experiência de Young**
- Confirmou-se o carácter corpuscular.
- Se tivermos *muitas* partículas, recuperamos o carácter ondulatório.
- O impacto de 1 fotão individual ocorre *aleatoriamente*.
- O padrão de interferência das ondas indica probabilidade: $$I_{12}\propto |E_{1}(x)+E_{2}(x)|^{2} \equiv \mathcal{P}(x)$$

**Paradoxo**
- Porquê que, quando temos 1 fotão sozinho, faz diferença ter 1 ou 2 fendas abertas? 
    - Se tivermos 1 fenda aberta, perdemos o padrão de interferência e ficamos apenas com um pico de probabilidade em frente à fenda que diminui para cima e para baixo.
    - Se tivermos 2 fenda abertas temos que o fotão interfere consigo mesmo, *como se atravessasse as 2 fendas*!!!
- No entanto, como vimos acima, ao examinar o sistema vemos apenas 1 impacto localizado (por fotão). Isto acontece porque ao medir o sistema microscópico estamos a alterá-lo de forma fundamental: causamos o colapso da equação de onda!
- Assim, é impossível observar o padrão de interferência e ao mesmo tempo saber por onde passou o fotão.

- Torna-se então importante abandonar/restruturar conceitos da física clássica:
    - *Trajetória de partícula* - os fotões percorrem mais que 1 trajetória.
    - *Determinismo* - apenas sabemos probabilidades, não conseguimos prever o comportamento dos fotões.

## Interpretação de Copenhaga
Interpretação da mecânica quântica desenvolvida por Bohr, Heisenber, Born, etc. Diz-nos que:
- Corpúsculo e onda são conceitos *inseparáveis*, sendo até *complementares*.
- As partículas propagam-se pelo espaço como ondas, o que permite determinar probabilidades (iremos estudar mais fotões, mas isto aplica-se a eletrões também, por exemplo)
- Ao fazer uma medição causasse o *colapso da equação de onda* e a partícula passa a estar localizada.