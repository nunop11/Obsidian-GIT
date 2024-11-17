# 1 - Litografia Ótica
- Temos 3 métodos principais de exposição da wafer
![[tipos litografia otica.png]]
da esquerda para a direita:
## Contact Printing
![[litografia otica contacto.png]]
$$R=\frac{3}{2}\sqrt{\frac{1}{2}\lambda t}$$
- PR em contacto com a mask (magnificação 1:1)
- Simples e barato
- A resolução é próxima do comprimento de onda
- Modos:
    - Soft - mask e wafer fazem contacto
    - Hard - usamos vácuo entre mask e wafer para os forçar junts
- Problemas
    - Cada contacto desgasta a mask, pelo que ela tem um tempo de vida limitado
    - Estamos limitados pelos defeitos da mask
    - Partículas podem infiltrar-se entre a mask e a wafer

## Proximity Printing
![[litografia otica proximidade.png]]
$$R=\frac{3}{2}\sqrt{\lambda\left(g+ \frac{1}{2}t\right)}$$
- Temos uma gap de 10-20 um entre a wafer e a mask
- Devido a difração, a resolução é limitada a 2-4um (no anterior podemos ter nm)
- Não há contacto, pelo que a mask dura mais tempo
- Continuamos  ter magnificação 1:1

## Projection Printing
![[litografia otica projecao.png]]
- A imagem da mask é projetada na wafer por um sistema ótico
- A magnificação é M:1 (0.25um e acima)
- Temos a wafer a _centimetros_ da mask
- Também chamado de "step-and-repeat" ou "step-and-scan"
- Vantagens
    - Mask nunca toca wafer
    - Podemos ter de-magnificação até 10x (iamgem 10x menor que mask) 
        - mais fácil fazer mask sem defeitos
- Problemas
    - Temos que andar a percorrer 1 die de cada vez (imagem projetada é muito focada)
    - Pelo ponto acima, demora mais a expor a wafer inteira
    - Complexo e caro

### Sistema step-and-repeat
- Vamos die a die. Normalmente usamos demagnificação de 4x
- Processo:
    - Luz UV é emitido por fonte
    - Passa por mask
    - Passa por lente que foca e reduz ao tamanho de 1 die
    - A wafer é movida em x,y,z,phi

### Sistema step-and-scan
- O mais usado atualmente em contextos industriais
- Tem que estar isolado de fontes de vibrações
- Mask demagnificadas 4x
- Não percebi bem como funciona

# 2 - Ótica
## 2.1 - Difração
- Pode ser definida como a dobra de uma onda ao passar numa fenda ou edge
- Comprimentos de onda menores sofrem menos difração
![[difracao.png]]

- Assim, aplicando aos 3 métodos vistos temos
![[difracao vs tipos litografia otica.png]]
vemos que, principalmente, a difração afeta a resolução e formato da imagem da mask transmitida.

- Ao usar uma lente, podemos intensificar o pico central:
![[difracao s lente.png|350]]       ![[difracao c lent.png|450]]
Ora, se a lente for grande que chegue teremos um perfil quase igual ao perfil que saiu da fenda. Ou seja, eliminamos o efeito da difração. Assim:
![[difracao vs tamanho da lente.png]]

- Quando ocorre difração, a luz espalha-se. Uma lente permite concentrar luz. Então colocamos uma lente para recolher um feixe difratado
- Ora, como as lentes reais têm diâmetro finito, nunca é possível recolher toda a luz. Perdemos alguma luz.
![[difracao com lente evolucao feixe.png]]

### Numerical Aperture (NA)
- Mede a capacidade de captar luz de uma lente. Quanto maior NA, mais luz é captada. Podemos definir como $\text{NA}=\sin(\alpha)\simeq \frac{D}{2f}$ ($\alpha$ é o ângulo desde o feixe central ao topo da lente, partindo do ponto de foco)
- Ora, como seria de prever, para litografia ótica queremos lentes com o maior NA possível
- No entanto, as aberrações das lentes aumentam com NA.
    - Ainda assim, avanços têm permitido aproximar do limite máximo no ar: $NA=1$

### Critério de Rayleigh
- Basicamente, diz que: tendo 2 fontes de difração, a resolução máxima que temos ($R$) é o valor máximo em que as imagens das 2 fontes podem ser distinguidas.
    - Ou seja, para qualquer valor $<R$ as imagens como aparecem como uma só.

- De uma forma geral isto resulta em:
$$R=k_{1}\frac{\lambda}{\text{NA}}$$
($\lambda$ é o comprimento de onda e $\text{NA}$ a numerical aperture)
- Acerca de $k_{1}$
    - Constante sem significado físico
    - Obtido experimentalmente, depende do sistema, propriedades do PR, etc

## 2.2 - Depth of Focus (DOF)
![[dof.png]]
- Pensemos em fotos:
    - Grande DOF permite ter fotos que mostram grandes cenas em que tudo está focado
    - Pequeno DOF permite ter aquelas fotos em que temos um objeto próximo, como tudo em volta desfocado
- De uma forma geral:
    - Maior NA, menor DOF
    - Menor NA, maior DOF

**Na litografia**
- Consideremos que superfície na wafer para onde queremos transmitir um padrão é irregular, com diferentes altura. Um DOF limitado será um problema.
- Pode, por vezes, ser mais problemático que resolução

- Consideremos:
![[opd.png]]
- Teremos o melhor foco nos pontos B e C se os caminhos óticos para cada um forem iguais (os feixes chegariam em fase)
- Ora, podemos calcular o OPD (Optical Path Difference - Diferença Caminho Ótico):
$$\text{OPD}=\delta(1-\cos\theta)\simeq \frac{1}{2}\delta\sin^{2}\theta$$
OK, obviamente é impossível que tenham o mesmo caminho ótico

- Então, quão alta pode ser a OPD? Também segundo o *critério de Rayleigh*, o caminho ótico entre 2 fontes de difração nunca pode ultrapassar $\lambda/4$ (diferença de fase de 90º). Assim:
$$\begin{align*}
\text{OPD}&< \frac{\lambda}{4}\\
\text{DOF}=2\delta_\text{Max} &< \frac{1}{2}\frac{1}{1-\cos\theta}\simeq\frac{\lambda}{\sin^{2}\theta}=\frac{\lambda}{\text{NA}^{2}} 
\end{align*}$$
($\text{DOF}=2\delta_{\text{Max}}$ vem da difura acima onde temos marcado o que é o DOF)

- Assim, para ter imagens no limite de resolução precisamos de
$$\text{DOF}=k_{2}\frac{\lambda}{\text{NA}^{2}}$$

- E assim temos: $\text{DOF}\propto \text{NA}^{-2}~,~R\propto \text{NA}^{-1}$. Assim, se aumentarmos NA: diminuir $R$ (bom, melhor resolução) e diminui ainda mais DOF (mau).
- Assim, é preferível reduzir $\lambda$ invés de aumentar $\text{NA}$
- Além disso, como provavelmente teremos $\text{DOF}$ limitado, devemos focar sempre mais no centro da camada de PR.

## 2.3 - Wafer Plana
- A wafer deve ser altamente planizada
- Usamos Planarização Química e Mecânica:
    - Temos wafer a rodar
    - É colocada contra um pad a rodar também
    - Existe uma substância entre eles que serve para planizar a wafer
![[planarizacao.png]]

## 2.4 - Reflexões
- Ocorrem inteferências entre o feixe incidente no PR e reflexões do feixe originadas na superfície e em relevos na wafer. Estas são uma das maiores fonte de variações na linewidth do processo
- Se a wafer for refletiva, nas zonas expostas podemos ter uma distribuição de intensidade *periódica* - efeito de standing wave
![[standing wave.png]]
ou seja, podemos causar desenvolvimento a ritmos diferentes. Isto levará a um perfil em zigzag:
![[standing wave consequencia.png]]

- Este perfil de standing wave pode ser descrito como:
$$I\propto \underbrace{e^{-\alpha z}+Re^{-\alpha(2t-z)}}_{\text{Amplitude média}} - \underbrace{2\sqrt{R}e^{-\alpha t}}_{\text{Amplitude}}\cos \left[\underbrace{\frac{4\pi n_{\text{PR}}(t-z)}{\lambda}}_{\text{período de standing wave}\sim150\text{nm}} + \phi_{23}\right]$$
- Para evitar:
    - Aumentar a absorção do PR 
    - Reduzir refletividade do wafer
    - O post exposure bake pode suavizar o zigzag

## 2.5 - Limite de Resolução
$$R=k_{1}\frac{\lambda}{\text{NA}}$$
- Como vimos, $\text{NA}$ tem o limite teórico de 1 
- $k_{1}$ é experimental e atualmente ronda 0.28. O limite físico é 0.25
- Ou seja, o parâmetro que verdadeiramente controla e limita o limite de resolução é o *comprimento de onda*. Atualmente as fontes de luz que temos são:
![[comprimento de onda 2.png]]
- Assim, para diminuir o commprimento de onda, seria preciso
    - fontes de luz novas
    - lentes novas 
    - realizar este processo em vácuo
- Também $k_{1}$ poderia teoricamente ser reduzido
    - usar camda anti-refletiva no PR
    - alterar aspetos do processo
- NA apenas pode ser melhorado de 1 forma
    - Litografia de imersão - consiste em fazer a litografia com o sistema submerso em óleo

- Dito isto, por mais dificil que pareça, temos estes dados:
![[resolução evolucao.png]]
sendo que, para estes valores, temos $R\sim36\text{nm}$. Ora, estes dados já são  de 2010

## 2.6 - Optical Proximity Correction (OPC)
- Pode ser usado para compensar efeitos de difração
- Ao projetar uma mask perdemos os cantos afiados por causa de difração
- OPC consiste em alterar a forma das masks de forma a reverter este efeito:
![[opc.png|418]]        ![[opc funcionamento.png|525]]

- Isto pode ser visto como um processo de *litografia inversa*
    - Usamos modelos para prever a correção necessária 
- Isto faz com que cada nodo da mask otimizada precise de mais precisão
- Modelos de PR empiricos têm que ser recalibrados para cada mudança do processo

## 2.7 - Maks de mudança de fase
- Melhoram capacidade de resolução de litografia ótica atual
- Modula a fase E a amplitude da luz transmitida
- As interferência entre feixes permitem controlar intensidade e campo E
    - Isto vai para os dois lados, podemos usar interferências construtivas e destrutivas

## 2.8 - Immersion Litography
- Voltemos a isto que referi acima
![[litografia otica de imersao.png]]
- Além deste aspeto de reduzir a dispersão da luz, temos:
$$\lambda'=\frac{\lambda}{n_\text{liquido}}<\lambda$$
ou seja, podemos melhorar imediatamente certos resultados.
- Também o DOF e NA poderiam ser melhorados
- Ora, a máquina de litografia de 300M€ que já falamos usa, claro, immersion litography

- Mas nem tudo é perfeito, temos alguns problemas
    - Torna-se necessaria uma quantidade absurda de água, já que estamos a falar de litografia de projeção imersa, temos que projetar 1 die de cada vez, trocar a água e continuar
    - Vibrações são transferidas para a lente
    - O líquido iria aquecer quando sujeito ao feixe de luz
    - Estariamos sujeitos a um novo conjunto de defeitos e contaminações
    - As lentes poderiam ser danificadas
