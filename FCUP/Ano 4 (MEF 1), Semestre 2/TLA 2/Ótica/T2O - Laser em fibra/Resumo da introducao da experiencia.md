## Objetivos
- Entender o funcionamento de EDFA (amplificador em fibra dopado com erbio)
- Construir um EDFA e uma laser em fibra dopada com erbio
- Medir e calcular os parametros do EDFA construido

## Teoria
### Esquema de pumping de 3 níveis
![[edfa.png]]
(nesta figura vemos esquemas de 3 e 4 níveis de pumping)
- Amplificadores oticos amplificam luz incidente, fazendo uma emissão excitada - mesmo mecanismo usado em lasers
- No caso de EDFA, o ganho ótico é gerado por iões de erbio (Er3+) que são excitados. Ocorre então *inversão de população* - isso é quando temos um nivel de maior energia mais populado que um nivel com menor energia. Como este estado não é natural, os eletroes descem de novo e é *libertada energia*
    - Assim, termos um sistema de pumping com 3 ou 4 níveis depende do dopante.
    - O dopante é excitado ao absorver fotões da luz incidente. Depois os atomos relaxam, descendo para níveis inferiores.
- A diferença entre 3 e 4 níveis:
    - No caso de 3 níveis, depois de estimular o sinal incidente, os atomos ficam no estado fundamental
    - No caso de 4 niveis, ficam num estado excitado que depois sofre uma rapida relaxação para voltar ao estado fundamental
    - Assim, para ocorrer inversão de população, é preciso pumping mais forte com o esquema de 3 niveis
- EDFA tem esquema de **3 niveis**

#### Equações de rate
- Vamos então estudar sistemas de 3 niveis
- Estas equações permitem relacionar emissão, absorção e pumping; tendo-se noção da quantidade de população em cada nivel.
- Para a população no estado 1 ($N_{1}$) (ver figura) consideramos:
    - Aumento de população em estado 1:
        - emissão espontanea do estado 2 com consntate de tempo $\tau_{21}$
        - emissão estimulada do estado 2 para amplificação, com rate $W_{s}$, que depende do fluxo de fotões
        - emissao estimulada do estado 3 com rate $W_{p}$, que depende do fluxo de fotões
    - Perda de população em estado 1:
        - pumping com rate $W_p$
        - absorção de fotoes do sinal com rate $W_s$
- De forma semelhante pensamos nos outros 2 estados e temos:
$$\begin{align*}
\frac{dN_{1}}{dt} &= \frac{N_{2}}{\tau_{21}} + W_{s}(N_{2}-N_{1}) - W_{p}(N_{1}-N_{3})\\
\frac{dN_{2}}{dt} &= \frac{N_{3}}{\tau_{32}} - \frac{N_{2}}{\tau_{21}} - W_{s}(N_{2}-N_{1})\\
\frac{dN_{3}}{dt} &= -\frac{N_{3}}{\tau_{32}} + W_{p}(N_{1}-N_{3})
\end{align*}$$
- Olhemos para a eq de N1:
    - No termo de Ws: 
        - se N2 > N1: temos mais atomos no estado 2 então eles descem para 1 e o número N1 aumenta com rate Ws
        - se N2 < N1: temos muitos atomos no estado fundamental, então eles tendem a subir espontaneamente com rate Ws
    - No termo Wp:
        - se N1 > N3: N1 diminui porque atomos sobem para 3 devido ao pumping
        - se N3 < N3: N1 aumenta porque ocorre inversão de população, que é mais forte que o pumping, ocorrendo transmissao com ritmo igual ao do pumping

### Fator de inversao de população (steady state)
- As equações que vimos descrevem uma evolução temporal. Mas se tivermos um pumping constante, eventualmente atingimos equilibrio. Temos um **steady state**
- Para haver ganho no amplificador, é preciso que haja mais transição de atomos $2\to1$ do que transição $1\to2$. Ou seja, é preciso que 2 seja mantido com maior população que 1, para haver inversão de população
- Temos o *fator de inversão de população*:
$$n_{sp}=\frac{N_{2}}{N_{1}-N_{1}}$$

- Podemos considerar que $\tau_{32}\ll\ll1$ então dizemos que um atomo que chega ao estado 3 desce logo para 2. Assim $N_{3}$ é obtido da distribuição de boltzman:
$$N_{3}=N_{2}e^{-\frac{E_{3}-E_{2}}{k_{B}T}}=\beta N_{2}$$

- Em steady state temos $dN_{1}/dt=0$. Assim temos da equação de $N_1$:
$$\frac{N_{2}}{\tau_{21}} + W_{s}(N_{2}-N_{1}) - W_{p}(N_{1}-N_{3})=0$$
podemos substituir a equação de $N_{3}$ aqui e obtemos o fator:
$$n_{sp}=\frac{N_{2}}{N_{2}-N_{1}}=\frac{W_{p}\tau_{21}+W_{s}\tau_{21}}{(1-\beta)W_{p}\tau_{21}-1}$$

- Assim, $n_{sp}$ está relacionado à potencia de pumping e do sinal através de $W_{p},W_{s}$. Relaciona-se ao comprimento de onda de pump através de $\beta$
- Se $n_{sp}=1$ temos inversão de população total
- No caso de 4 niveis temos relaxacao rapida $3\to2,1\to0$. Assim, temos $n_{sp}=1$ com pump fraco

### Ganho e saturação
- Definimos o ganho como $g=\sigma(N_{2}-N_{1})$ em que $\sigma$ é a secção transversa de transição
- Temos o espetro de ganho de EDFA
![[edfa espetros.png]]
ele é alargado pela propiedades da silica da fibra e por outros dopantes presentes.

- O ganho $g$ diminui conforme aumenta a potencia do sinal $P$. Para uma certa potência $P_{s}$ temos *saturação de ganho*:
$$g=\frac{g_{0}}{1+ P/P_{s}}$$

- Podemos definir a evolução da potência do feixe consoante se propaga na fibra (ao longo do eixo Z) como:
$$\frac{dP}{dz}=g(z)P(z)=\frac{g_{0}(z)P(z)}{1+ P(z)/P_{s}}$$
isto é integrado ao longo do comprimento *do amplificador*. Assim, na saida $z=L$ temos $P_{\text{out}}=P(L)=GP_{in}$. E definimos o **ganho de amplificação**:
$$G=G_{0}\exp \left(-\frac{G-1}{G}\frac{P_{out}}{P_{in}} \right) \quad;\quad G_{0}=\exp \left(\int_{0}^{L} g_{0}(z)dz \right)$$

### Comprimento de onda de pump e espetro absorção
![[edfa erbio diagrama e espetro.png]]
- Temos aqui o diagrama de energia e o espetro de absorção de Er3+
- Vemos que existem vários estados para onde podiamos fazer pumping
- Na prática, tem que ser um nível que seja compatível com o comprimento de onda de lazers: 800, 980, 1480, etc
    - A 800 temos baixa eficiencia de pumping
    - Mas 980 e 1480 funcionam!
- No caso de  980 temos $\beta=0$ e com 1480 temos $\beta=0.38$
- Assim, 980nm permite obter o maior fator de inversão
    - Tendo um pumping forte ($W_{p}\tau_{21}\gg1$) e um sinal fraco ($W_{s}\simeq0$) com 980nm, podemos ter $n_{sp}=1$

### Configurações
![[variacaoes de edfa.png]]
(aqui temos, de cima para baixo: forward pumping, backward pumping e forward and backward pumping)

- Osciladores servem para evitar oscilação do sinal
- Forward pumping tem melhor performance em termos de ruido
- Backward pumping temos maior potência de saturação e maior ganho
- Bidirectional pumping tem vantagens dos 2, mas maior complexidade

## Ruido
### Limite quântico
- Provou-se em 1982 que um amplificador linear **tem** de adicionar ruido ao sinal que amplifica. Este ruido é PELO MENOS equivalente a duplicar o ruido zero-point (ruido que existe mesmo com temperatura de 0K)
    - Na prática, o sinal sofre um SNR de 3dB
- Também foi deduzido a relação entre SNR de input e output, calculado a partir de campo e número de fotões:
$$\Tiny\begin{align*}
\text{campo:} \quad \quad \text{SNR}_\text{out}&= \frac{G}{2n_{sp}(G-1)+1} \text{SNR}_\text{in}\\
\text{numero:} \quad \quad \text{SNR}_\text{out}&= \frac{G^{2}\langle n_{0}\rangle}{n_{sp}^{2}(G-1)^{2} + n_{sp}(G-1) + 2n_{sp}(G-1)G\langle n_{0}\rangle + G\langle n_{0}\rangle} \text{SNR}_\text{in}
\end{align*}$$
- O primeiro é aplicado em sistemas com deteção coerente. O segundo para sitemas de deteção direta
- Temos SNR mínimo quando $n_{sp}=1$
- O limite quantico acontece quando $G\gg1$ e $\langle n_{0}\rangle\gg1$ e temos:
$$\text{SNR}_\text{out}=\frac{1}{2} \text{SNR}_\text{in}$$

### Ruido de emissao espontanea amplificado (ruido ASE)
- Como já vimos, eletroes em niveis mais altos podem descer espontaneamente para niveis inferiores. Ora, isto é pouco significante
- Mas consoante o sinal se propaga no amplificador e é amplificado, também o ruido destas transições de nivel são amplificiadas.
- Assim, quanto maior o ganho, mais este ruído é amplificado.
- Temos que a quantidade de ruido numa bandwidth $d\nu$:
$$P_{n}=h\nu n_{sp}(G(\nu)-1)d\nu$$

### Figura de ruido
- Boa para caraterizar o desempenho do amplificador:
$$F_{n} = \frac{\text{SNR}_\text{in}}{\text{SNR}_\text{out}}$$
a dedução é feita no pdf e temos:
$$F_{n}\approx 2n_{sp} $$

## Setup experimental
![[montagem edfa.png]]
- Podemos ver aqui a montagem
- WDM = multiplexador de divisao de comprimento de onda - instrumento que junta em 1 fibra vários comprimentos de onda
- É preciso ter cuidado com os couplers de fibras

## Resultados
### Medição de espetro ASE
- Meter pump (laser) com corrente máxima de 174mA = potencia de pump de 80.3mW
- Com o diodo de sinal desligado, medimos o output no OSA - isto será o espetro ASE
- Podemos ver em escala linear ou dB
- Podemos registar:
    - freq pico
    - bandwidth 3dB para freq
    - comp onda pico
    - bandwidth 3dB para comp onda = diferenca de comps onda
(não percebi bem como temos os comp onda para o bandwidth)
![[medir osa.png]]

### Medição de potencia de pump threshold
- Fixar valor do sinal input
- Variar a potencia de pump (variar corrente do laser)
- Medir a potencia de output no OSA
- Variar a potencia de pump até atingir o ponto de transparencia - para eles o threshold foi 18.3mW
- Na potencia threshold temos:
![[pico osa.png]]
- Verificaram que esta potencia não varia com o sinal input

- Fizeram ainda uma tabela em que e se varia corrente/potencia de pump. Para cada valor disto, usamos 2 valores de sinal:
![[tabela calibracao t2o.png]]
(não sei como se obtem os ganhos. Assumo que os picos dos sinais 1 e 2 são medidos no OSA)



















