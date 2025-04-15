**Tailoring Negative Thermal Expansion via Tunable Induced Strain in La−Fe−Si-Based Multifunctional Material**

##### Abstract
- Compostos ZTE (zero exp térmica) são formados ao combinar NTE com PTE (negative e positive exp termica).
- Compostos de La,Fe e Si conseguem ter efeito magnetocalórico e NTE muito elevados. Mas torna-se então útil conseguir controlar estes fenómenos
- Neste trabalho é feito ball milling de $\text{LaFe}_{11.9}\text{Mn}_{0.27}\text{Si}_{1.29}\text{H}_{x}$. Isto aumenta o range de temperatura da transição magnetocalórica. Aumentou a zona operacional da NTE
- Ou seja, para controlar as propriedades deste material induzimos *strain*

## Intro
- Em várias industrias é útil controlar materiais de forma mecânica à escala micro ou nano. Se nesse controlo houver aquecimento do material, se este tiver expansão térmica significante, iremos ter distorções e defeitos. Assim, torna-se relevante conseguir ajustar esta propriedade
- Mais importante ainda, é necessário controlar a expansão quando temos instrumentos ou estruturas feitos de diferentes materiais (como coisas com várias camadas). Se os materiais se expandirem de forma diferente poderemos ter cracks e quebra de ligações elétricas
    - De notar que nestes casos a expansão pode ocorrer num dispositivo já assembled e que é aquecido. Ou seja, resolver o mismatch da expansão térmica pode prolongar a vida destes dispositivos
- Ou seja, queremos formar compostos com ZTE

**Natureza**
- A grande maioria dos materiias expande quando é aquecido: PTE (expansão positiva)
- Alguns materiais têm a propriedade inversa, o seu volume diminui quando aquecido: NTE (expansão negativa)
- Ora, combinando compostos com estes 2 tipos de expansão, em proprorções adequadas resulta em materiais ZTE (sem expansão)
    - Aqui, o NTE atua como um *compensador de expansão*. Assim, estes compostos têm que ser muito bem compreendidos

**NTE e magnetrostructural coupling**
- NTE normalmente surge devido a coupling magneto volume (ou magneto estrutural). Ou seja, o material tem transição estrutural e magnética que ocorrem (aproximadamente) à mesma temperatura.
    - Na temperatura de Curie ocorre alta variação da magnetização (ponto critico). Isto por sua vez provoca uma transicao estrutural
- Este tipo de fenómeno normalmente ocorre em materiais com transições de primeira ordem: LaFeSi, HfNbFe, MnZnN
- Se as propriedades dos materiais forem ajustadas, também a sua expansão será ajustada

**La(Fe,Si)**
- O material deste artigo tem efeito magnetocalórico e NTE
- Este material transita de FerroMag para ParaMag, *mantendo a mesma estrutura* cúbica.
    - O estado de alta temperatura tem baixa magnetização e o de baixa temp tem alta mag
- Ora, a estrutura mantem-se igual, mas *contrai* em 3k-30k PPM num intervalo de <50K
- Ora, esse intervalo de temperatura tem que ser maior. Ou seja, a contração do material tem que "demorar mais temperatura" a acontecer
    - Isso porque materiais PTE normalmente têm expansões mais lentas

**Alterar magnetização**
- Tando $T_{C}$ como $dM/dT$ podem ser alterados
    - ao ajustar pressão e campo magnético
    - ao alterar a estequiometria do composto
- Uma estratégia mais comum recentemente é fazer substituição química, que facilmente torna a transição mais suave
- Veremos agora como ball-milling (BM) pode também fazer isto ao introduzir strain!

## Info Experimental
- Os samples foram feitos com um arc-melter em que os reagentes foram misturados nas proporções certas. De seguida foi feita hidrogenação.
- Depois de melting, a amostra foi colocada num tubo de quartzo e annealed por 7 dias a 1050ºC numa atmosfera de Ar
- As amostras foram milled à mão por pouco tempo, ficando-se com grãos de 100um.
- 2 gramas do pó obtido foi sujeito a ball milling. 
    - De 5 em 5 minutos o processo foi parado para evitar aquecimento
- Aos 15, 30, 45, 90 e 180min de milling removeram-se amostras de 100mg
    - A essas amostras chamou-se de BM15, BM30, etc
- As amostras foram examinadas em SEM, XRD e SQUID

## Resultados
### Morfologia
![[imagens sem hists.png]]
- Vemos imagens SEM de todas as amostras.
- O tamanho médio das partículas foi reduzido de 106um para 0.39um (com 180min de BM)

### Composição de Fase, Estrutura
- Este material tem estrutura cubica do tipo FCC. 
- Nos dados XRD com refinamento Rietveld identificou-se as fases previstas.
![[mesma tec 1.png]]
- O tamanho médio das partículas foi obtido por análise estatística das imagens SEM
- O tamanho de cristalite ($D$) e o strain ($\varepsilon$) foram obtidos com a relação de *Williamson-Hall*:
$$w \cos\theta=\frac{0.94 \lambda}{D} + 4 \varepsilon\sin\theta$$
em que $w$ é a FWHM (*largura a meia altura*) do pico XRD no ângulo $\theta$ e $\lambda$ é o comprimento de onda da radiação XR usada. 
- Para utilizar esta relação:
    - para um certo pico de XRD refinado podemos determinar $w$ e $\theta$ (o ângulo do pico em si).
    - repetimos isto para o máximo de picos possível. 
    - Fazemos uma regressão linear de pontos $(w_{i},\theta_{i})$ e determinamos $D,\varepsilon$ para esse espetro

- Como seria de esperar, aumentar o tempo de milling ($t_{BM}$) diminui o tamanho médio das particulas assim como o tamanho de cristalite. 
- Como pretendido e indicado acima, o BM gera strain de forma mecância, o que foi observado neste material!
    - Isto acontece porque as cristalite diminuem de tamanho logo aumentam em número.
    - Assim temos mais desordem química e mais distorções / relaxação na superfície dos grains

- O strain comportou-se de forma mais linear com o tempo de BM, verificando-se que se introduz $1.22\times10 ^{-3}\%$ de strain por minuto de BM

### Transição magnética
- A transição NTE está relacionada com a transição magnética. Então foi registada a curva $M(T)$ das amostras.
- Podemos ver a magnetização normalizada das amostras $M(t)/M(t=250\text{K})$:
![[mesma tec 2.png]]
Poedemos ainda calcular as derivadas:
![[mesma tec 3.png]]
- Da derivada podemos determinar o FWHM ($\Delta T_{dM/dT}$) e os máximos das derivadas (rate máximo de descida da magnetização)

- Podemos então ver o FWHM e o declive máximo em função do tempo de BM:
![[mesma tec 4.png]]

- $\Delta T_{dM/dT}$ carateriza o quão larga a transição é, em termos de temperatua. Como esperado/desejado, aumentar o tempo de BM alargou a gama de temperaturas da transição.

#### Análise de Bean-Rodbell
- Modelo teórico que explica e prevê as transições de materiais com coupling magneto-estrutural.
    - Consiste na observação que o $T_{C}$ depende do volume da célula unitária (e portanto depende do strain) de acordo com um coeficiente $\beta\propto \frac{dT_{C}}{dV}$ 
    - Temos ainda um $\eta$ que depende de $\beta$ e na compressabilidade do material ($K$). Com este coeficiente: $\eta>1$ é um material forte e $\eta<1$ um material fraco.
- Foi feito então ajusta da curva $M/M_{250K}$ com este modelo e temos:
![[mesma tec 5.png]]

### Caraterização da expansão térmica
![[mesma tec 6.png]]
- A figura a) acima mostra a variação do volume da célula unitária _normalizado_ : $\Delta V(T)/V(T=250 \text{ K})=\frac{V(T) - V(T=250\text{ K})}{V(T=250\text{ K})}$
- Na figura b) vemos a derivada de $\Delta V/V_{250K}$  AKA o coeficiente de expansão térmica: $\alpha_{V}(T)$
    - Podemos obter deste gráfico o FWHM: $\Delta T_{\alpha_{V}}$
    - Podemos ainda determinal o coeficiente máximo: $\alpha_{V}(T)_{peak}$
- Na figura c) temos $\overline{\alpha}_{V}$ que é o declive de $\Delta V/V_{250K}$ em $\Delta T_{\alpha_{V}}$, assim como os valores de $\Delta T_{\alpha_{V}}$ para vários $t_{BM}$. Os $\overline{\alpha}_{V}$ foram determinados assim:
![[mesma tec 9.png]]

- Vemos que a forma como $\Delta V/V_{250K}$ evolui com o tempo de BM é muito semelhante à forma de $M/M_{250K}$.
    - Em ambos os casos as curvas vão se suavizando e alargando, sendo que em $\Delta V/V_{250K}$ não temos uma variação tão uniforme de $T_{C}$ (na magnetização o $T_{C}$ aumenta com o tempo de BM)

- Podemos ainda ver a dependência do coeficiente nos picos com BM:
![[mesma tec 7.png]]

- A alta semelhança na forma como $\overline{\alpha}_{V},\Delta T_{\alpha_{V}}$ e $\text{declive de }M/M_{250K}, \Delta T_{dM/dT}$ dependem de $t_{BM}$ parece confirmar o forte coupling MS

**Relacionar**
- Podemos agora ver o $\overline{\alpha}_{V}$ relacionado com o tamanho de cristalite e o strain:
![[mesma tec 8.png|450]]

**Nano particulas**
- As amostras de 180min e de 0min foram medidas $M(H)$ com $T=20\text{ K}$.
![[mesma tec 10.png]]
- Vemos que a magnetização de saturação de BM180 é basicamente igual à de BM0. Isto contrasta com nanopartículas de La-Fe-Si, em que temos uma magnetização de saturação 30% menor.
- Ou seja, o BM não está a alterar os momentos magnéticos no material, mas sim a introduzir desordem magnética (devido à desordem estrutural) que faz as transições MS demorarem mais (sem se perder muita magnetização de saturação)

**Comparação direta**
![[mesma tec 11.png]]
- Vemos que a variação da magnetização tem uma variação mais intensa. 
- Isto indica que o comportamento magnético é mais sensível ao strain

**Contour plot**
- Temos um contour plot com o strain (y) e tamanho de cristalite (x) para diferentes declives $\overline{\alpha}_{V}$ e $dM/dT$:
![[mesma tec 12.png]]
- Usou-se um algoritmo para estimar a divisão de cores a partir dos dados experimentais medidos
- Podemos ver um comportamento semelhante MS