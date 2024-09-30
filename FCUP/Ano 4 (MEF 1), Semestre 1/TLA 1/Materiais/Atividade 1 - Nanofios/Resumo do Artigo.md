### " Tunning pore filling of anodic alumina templates by accurate control of the bottom barrier layer thickness "
## 0 - Abstract
- Estudou-se relação entre a espessura da barreira porosa de alumina ($\delta_{b}$) e o crescimento de nanofios (NW) de níquel (Ni) em PAA (Alumina Porosa Anódica) 
- Ao variar a tensão de anodização final do PAA para formar dendrites (ver outro documento) na base da estrutura nano porosa e ao otimizar $\delta_{b}$, faremos com que Ni preencha $\sim100\%$ dos poros. A esta percentagem de preenchimento chama-se $f_{p}$. No entanto, se $\delta_{b}$ não estiver na gama ótima, teremos menor $f_{p}$
-  Esse  valor ótimo é $\delta_{b}=10 \text{nm}$. *Até* este valor verificou-se ainda aumento da eficiência de eletrodeposição (EE) e homogeneização dos NW. Para $\delta_{b}$ inferiores e até $10~\text{nm}$ verifica-se crescimento/preenchimento consistente em todos os poros (cada vez mais poros são preenchidos)

## 1 - Introdução
- Criação de  nanoestrutura com templates de alumina têm as vantagens:
    - o diametro dos poros pode ser controlado
    - a distribuição dos poros é extremamente concentrada
    - a latice é muito organizada e fica assim por si própria após o processo de anodização
- A estrutura usada paramcriar os NW consiste em: subestrado de Al e um de metal (Ni neste caso). Entre eles encontra-se uma camada de alumina.

- A espessura da camada de PAA segue:
$$\delta_{b}=kV_{ap}$$
($k\simeq 1.3~\text{mV}^{-1}$ é uma constante, $V_{ap}$ é a tensão aplicada na camada)
![[espessura camada PAA.png]]

- Temos 3 hipoteses de eletrodeposição para criar NWs: DC, AC e PED (eletrodeposição pulsada - pulsos DC definidos por onda quadrada)
    - DC só permite criar NW se $\delta_{b}$ for nulo ou quase
    - com AC e PED podemos ter uma camada fina de PAA. PED-PAA são uma combinação reliable

- Para poder fazer PED, o potencial de anodização $V_{ap}$ é reduzido exponencialmente após a 2a anodização, gerando-se dendrites. Estas são estruturas tipo árvore com nanoporos. Estas têm uma corrente de anodização, densidade porosa e $\delta_{b}$ específicos.
- A espessura $\delta_{b}$ é, na realidade, uma distribuição em torno de um valor médio, resultando em inhomogeneidades na espessura e composição da camada de PAA.

- A experiência abaixo explicada consiste em controlar $\delta_{b}$ com $V_{ap}$ final. Nisto, $\delta_{b}$ afeta diretamente o comportamento de deposição. Vemos como é este comportamento para $\delta_{b}$ entre 2 e 16 nm. Atingiu-se $f_{p},EE$ máximos quando $\delta_{b}=10~\text{nm}$.

## 2 - Detalhes
- PAA foi produzido com processo de oxidação eletroquímica. 
    - Usou-se uma renda (mesh) de platina como cátodo.
    - A amostra metálica (alumínio) age como ánodo. Ela é colocada em cima de uma base de cobre. Esta tem ainda a função de "cooling plate", para evitar aquecimento e ruptura dielétrica.
        - Antes do processo de anodização (que cria o PAA), a superfície de Al é tratada com um processo de eletro polimento (polishing). Isto reduz a rugosidade da superfície
        - Para fazer com que o PAA tenha grandes áreas porosas organizadas, usamos um processo de anodização com 2 passos.
        - O processo resulta numa camada porosa com $\delta_{b}=10~\mu \text{m}$. Reduzimos a espessura desta aplicando uma tensão a decrescer exponencialmente, começando com $40~\text{V}$ e acabando na tensão que permite obter a $\delta_{b}$ desejada. 
            - Para obter $\delta_{b}$ entre 2 e 16 nm, usamos voltagens entre 1.3 e 14V

- O níquel é então depositado na PAA para formar os NW. Este é então depositado usando um processo de PED.
    - Inicialmente o material é depositado com um pulso de corrente DC por 8 ms. Depois um 2º pulso com polaridade inversa por 2ms. Por fim, temos um pulso de repouso por 0.7s. Esta parte final serve para os iões se reposicionarem na superfície.
        - Os pulsos foram gerados por um Keithley 2400 SourceMeter
    - O eletrólito usado foi o chamado "Watts bath". Este foi mantido com ph 4-5 e com temperatura constante de 40ºC.

- A percentagem de poros preenchidos e o comprimento dos NW criados foram registados com um microscopio HR-SEM QUANTA-FEI.
    - Para isto, usou-se secções transversais dos NW "como depositados", assim como vistas de cima. Estas secções transversais foram obtidas ao dobrá-los até surgirem rachas na alumina (???).
    - Para avaliar a quantidade de poros preenchidos usou-se um laser de iões (1140 1 ion beam sputter deposition system by Commonwealth Scientific Corporation) para:
        - remover o Ni em excesso - deixar a amostra "limpa" e nítida
        - assim como remover 1 um do template de PAA - para expor os poros e retirar o niquel de cima
    - Com isto, determinou-se o $f_{p}$ com software opensource para analisar as imagens recolhidas.
    - Foram feitas medições das propriedades magnéticas da amostra com um magnetometro SQUID com até 2T de campo B.

## 3 - Resultados
![[NW - grafico 1.png]]
- Acima vemos $V_{dep}$ ao longo do tempo (consoante se deposita Ni).
- O V máximo é atingido quando as dendrites são preenchidas, em $t_{d}$. Esse tempo pode ser definido.
- A tensão fica depois constante enquanto os poros são preenchidos. Quando os NW começam a sair para fora ocorre uma descida súbita de $V_{dep}$ e aumenta o ruído (não está na imagem). A esta tensão chamamos $V_{e}$.
- Para uma amostra de PAA com poros de $10~\mu\text{m}$ de profundidade, demorou-se 1h a encher tudo.

![[NW - grafico 2.png]]
- Este é outro aspeto a estudar. Aqui temos $V_{i}$ - a tensão medida durante o 1º pulso de 8ms. Esta tensão está então associada à eletrodeposição da primeira camada metálida, no fundo dos poros.
- Os pontos marcado seguem a seguinte equação:
$$V_{i}-V_{0}=\frac{j}{J_{L}\sqrt{\varphi}}\delta_{b}e^{A\sqrt{ \varphi}\delta_{b}}$$
($J_{L},A$ são constantes. $\varphi$ é a altura da barreira de potencial)
- O valor de $\varphi$ medido em artigos especificamente sobre alumina é elevado. Neste artigo mediram um balor reduzido, indicando a elevada presença de contaminações devido a PAA ter sido obtida com um processo de anodização.
- $V_{0}$ é a tensão sem barreira entre os elétrodos de banca e de trabalho (???)
- Observou-se que quando aumentamos $V_{ap}$ (= tensão final de anodização do PAA ; não confundir com $V_{dep}$ - tensão medida durante um pulso de deposição), e aumenta $\delta_{b}$, também teremos maior $V_{e}$.
    - Dito isto, $V_{e}$ é influenciado também por fatores externos: contactos elétricos, PAA, eletrólitos, NWs e respetiva interface com eletrólito.

- Consideremos $\rho\sim10\Omega\text{cm}$ a resistividade do eletrólito. Podemos estimar a resistência do eletrólito como $\sim10\Omega$. A resistência da camada barreira será $17-172\Omega$ conforme a sua espessura.
- Ao subtrair $V_{e}-V_{i}$ removemos a dependencia de $V_{e}$ no circuito externo, eletrolito e camada barreira. Aliás, podemos fazer este gráfico:
![[NW - grafico 3.png]]
- Vemos no gráfico acima que a relação $[V_{e}-V_{i}](V_{ap})$ pode ser relacionada com a relação $[V_{e}-V_{i}](\delta_{b})$. E podemos então ver que existe não homogeneidade no crescimento dos NW. 

![[NW - grafico 4.png]]
- O gráfico acima mostra a relação entre $t_{d}$ (tempo para preenchimento das dendrites) vs $V_{ap},\delta_{b}$. Vemos que para $\delta_{b}$ reduzido (<9nm) este tempo é bastante maior.
    - Deste modo, amostras com $\delta_{b}<9~\text{nm}$ apresentam maior inhomogeneidade (alguns poros ficam rapidamente preenchidos, outros apresentam menor eletro deposição).
    - $t_{d}$ menor significa que passamos da fase de preenchimento para a fase de $V_{e}$ constante mais rapidamente.
    - Estas não homogeneidades no crescimento podem facilmente ser observadas ao ver imagens de SEM de amostras obtidas.

- Usando essas imagens e determinando a percentagem de poros preenchidos ($\% f_{p}$) podemos fazer este gráfico:
![[NW - grafico 5.png]]
- Mais precisamente: para $9<\delta_{b}<11~(\text{nm})$ temos $f_{p}$ acima de 95%, com preenchimento máximo a 10nm. Podemos então dizer que o valor ó:timo para preenchimento de NW de Ni usando uma membrana de PAA é: $\delta_{b}^{opt}=(10\pm1)~\text{nm}$.
    - Vemos que os gráficos c) e o gráfico acima são muito semelhantes. Isto mostra que $V_{e}-V_{i}\sim f_{p}$, como tinhamos estimado acima.

- Num processo de eletrodeposição, o rate de eletrodeposição depende da corrente de deposição que deverá ser independente dee $\delta_{b}$. Mas nesta investigação verificou-se o oposto. Isto pode ser inferido pelo seguinte gráfico:
![[NW - grafico 6.png]]
- Aqui considerou-se: $EE=m_{a}/m_{t}$ ($m_{t}$ - qttd de material depositado esperado, $m_{a}$ - qttd de material depositado real)
- Vemos que o gráfico é coerente com o gráfico de $\% f_{p}$ que temos acima -- maior eficiencia da eletrodeposição implica maior percentagem de poros preenchidos.
- O processo de eletrodeposição é descrito pela lei de faraday, tendo-se:
$$\int_{0}^{t}Idt=neN_{A} \frac{m_{t}}{M}$$
($I$ é a corrente de deposição, $n$ a valência do ião depositado)
- Para determinar a quantidade real de material depositado usou-se o Momento magnético ($M$) medido com o SQUID, a temperatura ambiente. Temos abaixo a comparação entre $M$ normalizado e o campo $H$ aplicado:
![[NW - grafico 7.png]]
- O $M_{sat}$ é uma propriedade extensiva (aumenta com a massa). Ora, o valor standard de $M_{Sat}$ para NW de Ni é $50\text{ emu g}^{-1}$. Com isto pode-se obter $m_{a}$

- O processo de PED ocorre sempre acima de $1.3\text{V}$, pelo que ocorre eletrólise da água e temos então este processo a "competir" com a deposição metálica. 

**Explicação de n\ao homogeneidade para d_b reduzido**
- A porosidade do PAA está relacionada com o número de poros $n$.
- Temos a relação $V_{\delta}=1/\sqrt{n}V_{S}$ em que $V_{\delta}$ é o potencial usado para controlar $\delta_{b}$ e $V_{S}$ o potencial usado para aumentar os poros.
    - De alguma forma (???), isto implica que para $9<\delta_{b}<16~\text{nm}$ temos 16 dendrites e apenas temos $\delta_{b}$ a variar entre cada ensaio.
    - Mas para $\delta_{b}<9$ por alguma razão temos mais dendrites, sendo que estas aumentam com a diminuição de $\delta_{b}$. Por outras palavras, aumenta a porosidade da PAA. 
        - Com maior porosidade e mais dendrites, teremos poros com distintos diâmetros. Assim, uns irão ser preenchidos antes dos outros

**Menor crescimento**
- Para menores $\delta_{b}$, como vimos acima, teremos poros muito finos preenchidos. Ora, nos poros preenchidos irá haver corrente. Esta irá causar aquecimento, que por sua vez aumenta o pH. Maior pH implica que temos evolução de hidrogénio (consiste num processo que gera moléculas de $H_{2}$ ou que as usa) e não consegues crescer NW
- Para maiores $\delta_{b}$ são necessárias maiores tensões. Estas causam evolução de hidrogénio, que causa aumento de pH na interface entre o eletrólito e a superfície de deposição. Ocorre a reação $2H_{3}O^{-}+2e^{-}=2H_{2}+2H_{2}O$, que reduz a eletrodeposição de metal. As altas tensões e flutuações de $\delta_{n}$ causam densidades de corrente elevadas em certas zonas mais finas da barreira, o que causa ruptura dielétrica. Isto é visível no pico repentido do traçado de $\delta_{b}=16~\text{nm}$ no 1º gráfico desta secção.
- Vemos então que $\delta_{b}$ afeta claramente EE.

**Outros aspetos**
- Uma maior densidade de corrente de deposição ($70~\text{mA cm}^{-2}$) permite obter maior uniformidade no crescimento dos NW, sem afetar a estrutura.
- 