## Campos óticos
- Optoeletrónica == Fotónica
    - Fotónica é mais geral e mais sobre usar a luz (fotões) para várias aplicações
    - Fotónica é o termo que começa a ser mais usado atualmente
- Luz compreende radiação nos comprimentos de onda $[300 \mu m, 30 nm]$ - isto é enorme!

### Fotão
- Fotões apresentam propriedades tanto de onda como de corpo/matéria.
- Mas o seu comportamento _fundamental_ é o de onda
- Quando maior a freq de um fotão, mais energia ele tem
    - Ou seja, podemos ver um fotão como um pacote localizado de energia : MATÉRIA
![[pacote de onda.png]]
- Podemos definir a energia de um fotão como $$E_{fot}=h \nu$$
- Podemos o comprimento de onda de De Broglie de um eletrão como 
$$\lambda_{B}=\frac{h}{m_{e} v}$$
logo temos a frequência de um eletrão:
$$\nu_{e}=\frac{m_{e}c^{2}}{h}$$
e conseguimos determinar a energia do eletrão:
$$E_{e}=\frac{p^{2}}{2m}=h \nu_{e}$$


### Teoria quântica de campo
- No espaço-tempo existem ondas que interferem construtivamente e interferem construtivamente: gera-se um pacote localizado de energia AKA um eletrão.
    - Estas interferências logo desaparecem. Outra interferência acontece logo logo de seguida
    - Isto ocorre tão rápido que está dentro do principio de heisenberg
- Por alguma razão que não sabemos, algumas destas ondas interferem e geram estados (eletrões) que sobrevivem muito tempo: como aqueles que consituem materiais e nós!
- Interferências de outros tipos de ondas (quarks) geram protões e neutrões.
- Não sabemos porquê e como isto funciona ou acontece :)

### Propriedades fotão
- Tem frequência $\nu$
- Tem momento, que está associado à velocidade do fotão (comportamento corpuscular): $$\vec{p}=h \vec{k} \quad;\quad\vec{k}=\frac{2\pi}{\lambda_{0}}\hat{u}$$
- Temos ainda a energia: $E=h \nu$
- Temos a intensidade de luz: energia luminosa que passa por unidade de tempo e por unidade de área (área normal à propagação)
- Temos a densidade de fluxo de fotões: número de fotões por unidade de tempo e unidade de área: $$\text{densidade fluxo fotões} = \frac{1}{h\nu} = \frac{1}{\hbar\omega}$$
- Temos ainda o fluxo de fotões em si, que consiste no número de fotões que passa por unidade de tempo numa superfície normal à direção de propagação: $$\text{fluxo fotões} = \frac{P}{h\nu} =\frac{P}{\hbar\omega}$$
($P$ é a potência do feixe de luz, monocromático)

### Campo ótico
- A luz é definida pelo comportamento espacial e temporal do campo ótico, que consiste num campo E e B, determinados pelas eqs de maxwell
- O campo ótico varia no tempo com a frequência da sua onda, propagando-se na direção espcial determinada pelo vetor de onda
- O campo ótico é um campo vetorial com 5 parâmetros:
    - *Escalares*
        - Amplitude
        - Frequência
        - Fase
    - *Vetoriais*
        - Vetor de onda
        - Polarização

- Num meio, o campo é caraterizado por:
    - Campo elétrico $E$ : V/m
    - Campo magnético $H$ : A/m
    - Deslocamento elétrico $D$ : C/m2
    - Indução magnética $B$ : T ou Wb/m2
- Ou seja:
    - Campos exeternos: $E,H$ - entram na matéria
    - Campos internos: $D,B$ - gerados dentro da matéria pelos externos

- Quando um campo EM incide num material, as suas propriedades EM serão alteradas/forçadas, tendo-se $M,P$ (magnetização, polarização)

- Podemos definir os campos totais num meio:
$$\begin{cases}
\vec{D} = \varepsilon_{0} \vec{E} + \vec{P} \\
\vec{B} = \mu_{0}(\vec{H} + \vec{M})
\end{cases}$$
- Além de *indução magnética*, $\vec{B}$ pode ser chamado de *campo magnético total*
- Além de *campo magnético externo*, $\vec{H}$ pode ser chamado de *campo magnético incidente*

**Representação**
- Temos 2 vetores: $\vec{E},\vec{H}$: $$\begin{align*}
\vec{E}&= (E_{x},E_{y},E_{z})\\
\vec{H}&= (H_{x},H_{y},H_{z})\\
\end{align*}$$
ou seja, temos 6 variáveis!
- Mas pdoemos representar isto mais sucintamente com **2 funções**:
$$(\vec{E},\vec{H}) \Leftrightarrow (\phi,\vec{A})$$
que só tem 4 variáveis $(\phi, A_{x},A_{y},A_{z})$!!!

- Temos:
$$\vec{E}=- \nabla \phi - \frac{\partial \vec{A}}{\partial t}\quad ;\quad \vec{H}= \nabla \times \vec{A}$$
- Existe um certa liberdade de escolha do par $(\phi,\vec{A})$:
$$\begin{align*}
\vec{A'}&= \vec{A}+\nabla \xi\\
\phi &= \phi' - \frac{d\xi}{dt}
\end{align*}$$
em que $\xi(\vec{r},t)$ é uma qualquer função!
- Esta liberdade e variabilidade acaba por se relacionar, incidir com o teorema de Noether. Isto acontece porque podemos fazer transformações e o modelo EM continua a aplicar-se, porque existe conservação.
    - No caso deste modelo, temos uma invariância _de escala_. Isto acontece devido à **_Conservação de carga elétrica_**!
    - Noutro tipo de sistemas físicos como mecânica clássica, temos conservação de momento angular, por exemplo.