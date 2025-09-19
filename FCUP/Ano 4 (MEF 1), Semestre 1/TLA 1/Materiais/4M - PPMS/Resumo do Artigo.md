### Abstract
- Novo método para estudar toda a resposta em temperatura de um calorimetro heat-pulse (hp) para capacidade térmica.
- Ao analisar a resposta térmica de um calorimetro hp num modelo feito por método de relaxação, foi possivel melhorar o método numérico linear de LS (least squares) para determinar a capacidade térmica.
- Neste artigo determinaram a capacidade térmica de cobre.
- O tamanho da amostra não afeta o método e a gama de temperaturas pode ser maior que a usada.

## Introdução
**HPM**
- O método heat pulse (HPM) é usado para determinar propriedades termodinâmicas de materiais. É usado o principio $C=\Delta Q/\Delta T$
    - $C$ é a capacidade térmica
    - $\Delta Q$ é a pulse heat fornecida à amostra 
    - $\Delta T$ é o aumento de temperatura causado

- Ao longo da história, foram feitas melhorias para medir amostras pequenas e manter as condições adiabáticas.
    - Ainda assim, HPM não é adequado para medir amostras pequenas a temperaturas muito reduzidas
        - Consoante a temperatura de uma amostra pequena desce, o hp necessário para medir $C$ teria de ser muito reduzido. Ora, seria tão reduzido que as perdas de calor pelas conexões da fonte à amostra já não são desprezáveis.

**Outros**
- Também se usa:
    - CWM - continuous warming method
    - ACM - AC method
    - RM - relaxation method

- Destes, ACM e RM são não-adiabáticos e permitem medir C para amotras pequenas.
- Em ambos estes métodos, a amostra é ligada a um heat sink a temperatura constante $T_0$. O $C$ é derivado de modelar a resposta térmica ao calor fornecido.
- Mas têm limitações: ambos os métodos precisam de uma ligação térmica bem escolhida. Ou seja, é preciso escolher bem a ligação de forma a ter $\tau_{1}$ apropridado ($\tau_{1}$ é uma constante de tempo que se relaciona com a tempertura de equilíbrio entre o sample holder e o heat sink)
    - Se $\tau_{1}$ for muito elevado, o tempo para atingir equilibrio do sistema seria demasiado elevado para determinar $C$
    - Se $\tau_{1}$ for muito reduzido, as reações e equilíbrio tornam-se demasiado rápidas para analizar

- Dito isto, as vantagens e desvantagens de HPM e RM são *complementares*.
    - HPM é bom para medir C de forma adiabática em amostras com C elevado
    - RM permite medir amostras pequenas de forma não-adiabática
    - Os problemas que surgem em RM quando $\tau_{1}$ é muito reduzido não ocorrem com HPM

- Assim, os autores do artigo decidiram analizar a resposta térmica de um calorimetro HPM usando um modelo RM. Assim, teríamos um método híbrido destes dois.
    - Poderíamos ter maior gama de temperaturas e o tamanho da amostra seria mais flexível
    - Este método seria facilmente usável com calorimetros HPM já existentes

- Vantagens:
    - Nem $\tau_{1}$ nem o tamanho da amostra importam
    - Podemos medir C de forma adiabática ou não
    - $C$ é calculado, sempre em conjunto com $\tau_{1},\tau_{2}$ (não sei bem o que quer dizer t2 - acho que tem a ver com tempo de resposta de circuitos eletrónicos a altas velocidades)
    - Os efeitos térmicos do sensor de temperatura podem ser incluídos nas leituras e corrigidos
    - O efeito $\tau_{2}$ é tratado

## Teoria - CFM
![[montagem t4m esquema.png|375]]
- Do esquema acima temos as equações:
$$\begin{cases}
P(t)=c' \frac{dT'}{dt}+ \lambda_{S}(T'-T) + \lambda_{l}(T'-T_{0}) \\
0 = c \frac{dT}{dt} + \lambda_{s}(T-T')
\end{cases}$$
- em que:
    - $P$ é a potência/calor fornecido
    - os termos do tipo $c \frac{dT}{dt}$ são o calor que entra
    - os termos do tipo $\lambda(T-T)$ indicam como 2 componentes interagem
    - $\lambda$ são as condutâncias térmicas das ligações
- Basicamente, a 1a equação representa como o suporte reage ao fornecimento de calor (potencia) externo
- A 2a equação (por ter zero do lado esquerdo) diz-nos que a amostra só troca calor com o suport e mostra que a evolução temporal de $T$ é completamente decidida por isto.

- Este modelo pode representar qualquer calorimetro. Basta assumir que 
    - a fonte de calor e o sensor estão ligados diretamente a um só suporte da amostra
    - a resposta térmica é instantânea
    - a condutância térmica da amostra e suporte são $\gg \lambda_{s},\lambda_{l}$
    - $c,c'$ não dependem da temperatura

- Estando o sensor bem ligado ao suporte, o que ele mede seria $T'$.
- Isolamos $T$ na equação 1 e substituimos na eq 2, obtendo:
$$\frac{cc'}{\lambda_{s}} \frac{d^{2}T'}{dt^{2}}+\left(c'+c+c \frac{\lambda_{l}}{\lambda_{s}}\right) \frac{dT'}{dt} + \lambda_{l}T'= \frac{c}{\lambda_{s}} \frac{dP}{dt}+P+\lambda_{l}T_{0}$$
- Em HPM vamos emitindo vários pulsos de calor para medir C. Ora, antes de emitir um pulso temos o sistema em equilíbrio térmico. Ou seja, no gráfico $T(t)$ começamos com uma linha horizontal. A essa linha chamamos de *linha de base* que representaremos daqui adiante como $T_{1}(t)$. Partindo da equação diferencial acima, $T_{1}$ pode ser definido por $P=0$:
$$\frac{cc'}{\lambda_{s}} \frac{d^{2}T_{1}}{dt^{2}}+\left(c'+c+c \frac{\lambda_{l}}{\lambda_{s}}\right) \frac{dT_{1}}{dt}+\lambda_{l}T_{1}=\lambda_{l}T_{0}$$
- Sendo então $T_{1}$ a linha de base, podemos definir a variação de temperatura do sistema: $T=T'-T_{1}$. Assim, subtraindo as 2 equações acima ficamos com:
$$\frac{cc'}{\lambda_{s}} \frac{d^{2}T}{dt^{2}}+\left(c'+c+c \frac{\lambda_{l}}{\lambda_{s}}\right) \frac{dT}{dt}+\lambda_{l}T=\frac{c}{\lambda_{s}} \frac{dP}{dt}+P$$
e integramos:
$$\frac{cc'}{\lambda_{s}} \frac{dT}{dt}\Biggr|_{0}^{t} + \left(c'+c+c \frac{\lambda_{l}}{\lambda_{s}}\right)T\Biggr|_{0}^{t} + \lambda_{l} \int_{0}^{t}T dt' = \frac{c}{\lambda_{s}}P(t) + \int_{0}^{t} P(t)dt'$$
e podemos isolar $T|_{0}^{t}=T(t)-T(0)$:
$$\begin{align*}
T|_{0}^{t}&= \frac{\frac{c}{\lambda_{s}}P(t)}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}} + \frac{\int_{0}^{t}P(t)dt'}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}}-\frac{\lambda_{l}\int_{0}^{t}T dt'}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}} - \frac{\frac{cc'}{\lambda} \frac{dT}{dt'}\Big|_{0}^{t}}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}}\\
&= \frac{\frac{c}{\lambda_{s}}\left(P(t) - c' \frac{dT}{dt'}\Big|_{0}^{t}\right)}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}} + \frac{\int_{0}^{t}P(t)dt'}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}}-\frac{\lambda_{l}\int_{0}^{t}T dt'}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}} 
\end{align*}$$
- Podemos definir:
$$Q(t):= \int_{0}^{t}P(t)dt' ~~,~~ V(t)=\frac{dT}{dt'}\Big|_{0}^{t}~~,~~ S(t)=\int_{0}^{T}Tdt'~~,~\Gamma(t)=T|_{0}^{t}$$
e fica:
$$\Gamma=\frac{\frac{c}{\lambda_{s}}(P-c'V)}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}}+\frac{Q}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}}-\frac{\lambda_{l}S}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}}$$
podemos ainda definir $H=P-c'V$:
$$\Gamma=\frac{\frac{c}{\lambda_{s}}H}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}}+\frac{Q}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}}-\frac{\lambda_{l}S}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}}$$

**Calcular os parâmetros**
1.  Para calcular as funções H,P,V,Q,S, é importante notar que ao recolher dados experimentais (obviamente) não teremos dados contínuos, apenas um set discreto. Teremos então dados $(t_{i},T_{i}',P_{i})$ - tempo do sample, temperatura do suporte, potência calorífica fornecida ao suporte.
2. Começamos por fazer *ajuste linear* dos dados $(t_{i},T_{i}')$ recolhidos antes do heat pulse para determinar a base line!
3. Tendo a base line, calculamos para cada sample point a variação de temperatura com: $T_{i}=T_{i}'-T_{1}(t)$.
4. Podemos usar interpolação spline cúbico (ou outro tipo de interpolação) para converter $(t_{i},P_{i}),(t_{i},T_{i})\to P(t),T(t)$. Daí podemos calcular $\Gamma,Q,V,S$
5. Assim, sabendo $c',\Gamma,H,V,Q,S$ podemos usar um método de ajuste (general linear least squares) para ajustar os pontos $(t_{i},\Gamma_{i})$ com a última equação de $\Gamma$ acima. Teremos um ajuste do tipo:
$$\Gamma(t) = h H(t) + qQ(t) + sS(t)$$
em que:
$$h=\frac{\frac{c}{\lambda_{s}}}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}}~~,~~q=\frac{1}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}}~~,~~s=\frac{-\lambda_{l}}{c'+c+c \frac{\lambda_{l}}{\lambda_{s}}}$$
6. Tendo estes coeficientes podemso determinar as grandezas desejadas:
$$\begin{cases}
\lambda_{l}=- \frac{s}{q} \\
\lambda_{s}= \frac{s}{q} + \frac{1-qc'}{h} \\
c= \frac{hs}{q^{2}}+ \frac{1}{q}-c'
\end{cases}$$

- Ainda não foi dito, mas $c'$ pode ser obtido ao pegar na equação de $\Gamma$ e assumir que $c=0$, ficando:
$$\Gamma=\frac{Q}{c'}-\frac{\lambda_{l}S}{c'}$$
e penso que chega determinar $Q,S$ e com os coeficientes do ajuste $\Gamma=q'Q+s'S$ determinamos $c'$.

**t1, t2**
- Sabemos $\lambda_l,\lambda_s,c$ podemos determinar $\tau_1,\tau_{2}$:
$$\tau_{1}=\tau_{-}~~~~;~~~~\tau_{2}=\tau_{+}$$
em que
$$\tau_{\pm}=\frac{2}{k_{1}\pm \sqrt{k_{1}^{2}-4k_{2}}} \quad;\quad k_{1}=\frac{\lambda_{s}+\lambda_{l}}{c'} + \frac{\lambda_{s}}{c}~~,~~ k_{2}=\frac{\lambda_{s}\lambda_{l}}{cc'}$$

**Notas**
- Esta técnica consiste em melhorar HPM. Mas esta dedução deverá funcionar para $P(t)$ de vários formatos (não só pulsos). Ou seja, esta técnica deverá conseguir melhorar resutados de outros métodos.

## Experiência
**Montagem**
![[montagem t4m.png|475]]
- O esquema acima mostra um sistema simples que permite demonstrar CFM. 
- O suporte é uma sheet de cobre coberta a ouro com 8x8x0.1 mm. O aquecedor é simplesmente uma resistência de 2kOhm. O sensor de temperatura é plano e fino (pesquisa "thin film resistance temperature sensor")
- Usamos GE varnish (para isolamento elétrico) para montar o aquecedor, o sensor e a amostra; tudo no suporte.

- O suporte (e todo este sistema) encontra-se suspenso por fios de nylon e num *vácuo*.
- Usamos fios de manganina (alloy de 84% cobre, 12% manganês e 4% níquel) (60 um de diâmetro), cada um com 15Ohm de resistência e 1cm de comprimento, para conectar o aquecedor. Usamos estes fios para garantir que a potência de aquecimento tem um erro abaixo de 0.5%.
- Do outro lado do sample temos 4 fios de manganina com as mesmas dimensões que ligam ao sensor de temperatura. 
    - A resistência medida neste sensor foi convertida em temperatura usando polinómios de Chebychev conforme fornecido pelo fabricante

- A temperatura do heat sink ($T_{0}$) foi controlada com um controlador de temperatura com sensor de díodo.
    - O sensor foi calibrado ao medir as temperaturas críticas de super condução de amostras de Pb e Nb
    - O sensor necessita que passe nele corrente para funcionar, portanto é evidente que ele apresenta auto-aquecimento. Mas esta potência pode ser incluida na potência calorifica fornecida ao suporte, $P$.

**Procedimento**
0. Antes de começar com os pulsos, arrefecer o sistema com o suporte até 4.5K. Usou-se radiation ou heat leak com fios de chumbo (? não encontrei nada online sobre isto??). Isto demora 8h
1. Começando com o sistema em equilíbrio térmico, fazer um ciclo de pulsos e determinar as grandezas desejadas com CFM
2. Usando estes parâmetros, regular a corrente de aquecimento e outros parâmetros importantes para automização (por exemplo de forma a garantir $\Delta  T$ adequado)
3. Quando o sistema retomar o equilíbrio, repetir este ciclo até 50K.
    - A partir de 50K é preciso ter cuidado para manter o vácuo do sistema

- Para melhorar performance de CFM podemos regular os pesos dos pontos usados em GLLS, o que poderá remover a influência de pontos ruído.

## Resultados
- Temos abaixo o gráfico da capacidade térmica determinada com HPM, SDM e CFM abaixo de 20K
![[C vs T.png]]
(HPM é quadrados brancos, SDM é triangulos brancos, CFM é bolas pretas)

- Para temperaturas menores CFM dá C menor porque este método tem em conta as perdas de calor nos fios, os outros métodos não.
- Ajustou-se os dados do CFM a um polinómio $c'_{fit}=\sum_{n=0}^{6}A_{n}T^{n}$. Temos aqui os desvios percentuais do ajuste:
![[erros C.png]]
(HPM é quadrados brancos, SDM é triangulos brancos, CFM é bolas pretas)

- Comparou-se os dados medidos na gama 0-80K a dados "de referência" obtidos por outros investigadores (Osborne para a gama 0-20K e Martin para 20-80K) e temos o erro:
![[erros C varios métodos.png]]
(HPM é quadrados brancos, SDM é triangulos brancos, CFM é bolas pretas)

- Com CFM o erro foi sempre <3%
- Ainda assim, vemos que a partir de 20K CFM determinou C consistentemente acima do valor de referência. Isto poderá ser por desvios da calibração do sensor de temperatura.
    - Para melhorar esta precisão acima de 20K seria preciso um termómetro de platina.

**Precisão**
- Podemos usar os dados <8K para determinar a relação $c=\gamma T+\beta T^{3}$ (usada para baixas temperaturas). Para isto, ajustou-se $C/T \times T^{2}$
- Nos dados vemos que CFM não foi afetado de forma relevante por $\tau_{1}$ nem $\tau_{2}$, como esperado.
    - Aliás, $\tau_{2}$ é desprezável. Se quisermos que seja notável, usamos uma amostra com C muito elevado ou má resposta térmica ao suporte. Assumindo que $\lambda_{l}\ll\lambda_{s}$ obtemos que $\tau_{2}=\lambda_{s}(1/c'+1/c)$
- Com sabemos, $\lambda_{l}$ é determinado por CFM. Assim, comparando o valor obtido com a condutância térmica de 6 fios de manganina verificou-se mais uma vez a precisão de CFM.

**Estabilidade**
- Para ver a estabilidade de CFM aqueceu-se uma amostra de Pb no range de tempo 20-300s.
- Usando os dados, ajustou-se a corrente de aquecimento para garantir que $\Delta T=0.1K$.
- Obteve-se:
![[calor especifico varios metodos.png]]
(HPM é quadrados brancos, CFM é bolas pretas)

- Aqui, cada ponto corresponde a um tempo de aquecimento usado para percorrer a gama 5-6K (10 ciclos de aquecimento, com $\Delta T=0.1K$)
- Vemos que CFM foi muito mais consistente

**Problemas**
- As principais falhas de CFM resultam da sua modelização. Mais concretamente, no modelo usado ignoramos resistência térmica entre fonte/sensor e suporte.
- Assim, se aumentarmos a resistência os dados calculados com CFM vão discordar cada vez mais com o correto.
- Ora, esta resistência térmica aumenta com a temperatura.
- Vejamos o que acontece consoante aumenta se liga o aquecedor com o sistema a diferentes temperaturas:
![[curva aquecimento diferentes tau1.png]]
(bolas brancas que são dados CFM, triângulos pretos são o ajuste feito)

- Vemos que para $T=70K$ temos um $\tau_{1}$ muito elevado (o sistema demora mais a estabilizar) e vemos que o ajuste fica bastante pior.
- Este efeito poderia ser chamado de "$\tau_{3}$ effect"
    - Para o resolver poderíamos remodelar o método, considerando agora a resistência térmica
    - Mas temos uma forma mais eficiente: reduzir os pesos ded GLLS dos pontos mais desviados
    - 