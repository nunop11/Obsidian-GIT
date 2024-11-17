**Título**
Tutorial: a beginner’s guide to interpreting magnetic susceptibility data with the Curie-Weiss law

**Abstract**
- Medições de alta qualidade da susceptibilidade de um material são cada vez mais fáceis de obter, sendo muitas vezes esta uma das primeiras caraterizações feitas num material novo.
- Neste artigo temos um guia sobre como analisar dados de susceptibilidade magnética, especialmente em materiais com paramagnetismo de Curie-Weiss

## Artigo (não tem secções)
### Susceptibilidade
- A susceptibilidade de um material ($\chi$) relaciona a sua magnetização ($M$) com o campo magnético nele aplicado ($H$) - ou seja, diz-nos como é que o material corresponde a um campo externo. Normalmente temos esta relação:
$$M=\chi H$$
esta relação linear é geralmente mais correta a temperaturas altas e campos baixos.
- Podemos fazer medições de $\chi$ com campos AC ou DC, para determinar as propriedades magnéticas dinâmicas ou estáticas, respetivamente.

### SQUID
- Atualmente estas medições são feitas usando o magnetómetro SQUID (Superconducting QUantum Interference Device). Ele facilita obter medições de $\chi$ com alta qualidade, a várias temperaturas (até temperaturas muito baixas - dezenas de Kelvin). 
- O SQUID permite medir diretamente $\chi$. 
![[SQUID.png]]
como vemos na imagem acima, temos 2 junções de Josephson paralelas (uma junção de Josephson é quando temos 2 materiais supercondutores, com um isolador no meio a separá-los). Estas junções permitem detetar diferenças de fluxo magnético muito reduzidas (até $10^{-14}T$ pelo que vi online).

### Introdução
#### Unidades de Magnetismo
- Temos o sistema CGS (Centimeter - Gram - Second) e sistema SI.
- Susceptibilidade molar é normalmente escrita em unidades $\text{emu mol}^{-1}$ em CGS. Em SI temos em $\text{m}^{3}\text{ mol}^{-1}$. Para converter entre as duas, multiplicamos o valor em CGS por $4\pi \cdot10^{-6}$
    - Em CGS $\text{emu Oe}^{-1}$ é equivalente a $\text{emu}$ :D
- Neste artigo vamos usar CGS. 
- Temos aqui uma tabela de conversão:
![[conversao cgs para si.png]]

#### Contribuições para $\chi$
- *Paramagnetismo / Diamagnetismo* - Referem-se ao sinal da susceptibilidade em relação ao campo magnético aplicado. Em materiais paramagnéticos temos $\chi>0$ (a magnetização tem a direção do campo). Em diamagnéticos temos $\chi<0$ (a magnetização tem direção oposta ao campo).
- Vamos então ver as várias contribuições

##### Diamagnetismo Orbital
- Todos os materiais têm. Quando é a única fonte de magnetismo, o material é *diagmanético*.
    - É fraco, apenas da ordem de $-10^{-6}:-10^{-5} \text{emu mol}^{-1}$
    - Normalmente só materiais isoladores sem eletrões sem-par são diamagnéticos 
- Tendência dos eletrões a repelir um campo magnético. Isto gera $\chi<0$.
- De um ponto de vista clássico, podemos entender isto com a lei de Lenz: quando sujeitos a um campo externoo, os eletrões em órbita geram uma corrrente que tem tendência a tentar "anular" o campo externo, gerando um campo magnético induzido oposto.
    - Para resultados mais precisos é preciso analisar esta situação usando mecânica quântica - teoria de perturbações.
- A susceptibilidade diamagnética molar é dada por:
$$\begin{align*}
\chi_{D}&= - \frac{ne^{2}}{6m_{e}c^{2}} \langle r^{2}\rangle~~,~~ [\text{cgs}]=\text{emu mol}^{-1}\\
&= - \frac{n\mu_{0}e^{2}}{6m_{e}} \langle r^{2}\rangle ~~,~~ [\text{SI}]=\text{m}^{3}\text{ mol}^{-1}
\end{align*}$$
($n$ é o número de eletrões por mole e $\langle r^{2}\rangle$ o raio quadrático médio da órbita do eletrão. O sinal é negativo porque o campo induzido é repulsivo, como já vimos)

- Por vezes é útil subtrair aos dados de susceptibilidade a contribuição diamagnética. Esta é independente da temperatura e pode ser facilmente aproximada usando tabelas.
    - Apesar de tudo, temos também muitos casos em que esta contribuição pode ser ignorada. 

##### Paramagnetismo Curie-Weiss
- Só ocorre em materiais "magnéticos" - materiais com eletrões sem-par. 
- A temperaturas específicas (próximas da temperatura de Curie) - **temperatura crítica** - materiais paramagnéticos podem sofrer uma transição de fase para um estado *magneticamente ordenado*.
    - Isso acontece porque a uma certa temperatura as interações magnéticas entre as partículas tornam-se mais forte que a sua agitação térmica. Os momentos magnéticos alinham-se
        - Isto chama-se de "quebra de simetria" - a simetria original do sistema é desfeita.
- A **temperaturas mais elevadas** o material já se comporta novamente como um paramagnet
    - Os momentos estão desordenados, comportando-se como um gás - aleatoriamente e de forma não correlacionada.
    - Agora a agitação térmica é que é tão elevada que sobrepõe as interações magnéticas e impede alinhamento.

**Susceptibilidade**
- Temos a lei de Curie-Weiss:
$$\chi=\frac{C}{T-\theta_{CW}} ~~,~~ [\text{cgs e SI}]$$
em que:
    - $C$ é a constante de Curie, com unidades $\text{emu K mol}^{-1}$ em CGS. Está diretamente relacionado com o número de eletrões sem-par.
    - $\theta_{CW}$ é a temperatura de Curie-Weiss, com unidade $K$
    - $T$ é a temperatura do sistema em $K$
![[chi modelo curie weiss.png]]
Notas sobre o gráfioc:
    - DM e PM são contribuições de tipos específicos de diamagnetismo e paramagnetismo independententes da temperatura. O paramagnetismo de Curie-Weiss é 1+ ordem de grandeza superior.
    - No gráfico b) temos a susceptibilidade inversa. 
        - A laranja temos o PM de Curie-Weiss com $\theta_{CW}=0$. 
        - A azul temos PM CW para $\theta_{CW}>0$. Este comportamento é idêntico ao de um ferromagnet (FM)
        - A vermelho temos PM CW para $\theta_{CW}<0$. Isto é equivalente ao comportamenteo de um anti-ferromagnet (AFM)

- Esta lei mostra a tendência de os momentos magnéticos num paramagnet se alinharem com o campo.
- A constante de Curie permite-nos determinar o momento magnético efetivo em função do magnetão de Bohr: $$\begin{align*}
\mu_{eff}&= \sqrt{8C}\mu_{B}~~,~~[\text{cgs}]\\
&= 800\sqrt{C}\mu_{B}~~,~~\text{[SI]}
\end{align*}$$

**Temperatura**
- O módulo da temperatura de Curie-Weiss depende da força do campo molecular (o campo molecular de Weiss é o campo interno que tem a função de tentar alinhar as moléculas do material), que por sua vez indica a força da correlação magnética entre iões. 
    - $\theta_{CW}>0$ indica que o campo molecular se alinha com o campo externo
    - $\theta_{CW}<0$ indica que o campo molecular se opõe ao campo externo
- Conforme $T$ se aproxima de $|\theta_{CW}|$, o comportamento do sistema desvia-se do modelo de Curie-Weiss, podendo ocorrer a transição para um estando ordenado previamente referida. Ou seja, $|\theta_{CW}|$ será a temperatura crítica.
    - Para ferromagnets temos $T_{C}\sim \theta_{CW}$ ($T_{C}$ é temperatura de Curie)
    - Para antiferromagnets temos $T_{N} < |\theta_{CW}|$ ($T_{N}$ é temperature de Néel)

**Aplicabilidade**
- Os materiais que melhor seguem o comportamento do modelo de Curie-Weiss são compostos 4f (compostos que contém lantanídeos) e compostos 3d de metais de transição.
    - 4f - porque têm tão pouca energia (estão longe da banda de condução) que os seus momentos magnéticos são localizados
    - 3d - porque temos isoladores de Mott e os momentos magnéticos tornam-se localizados

**Mas há outro!**
- Até aqui só vimos casos em que um campo externo é aplicado
- Mas sempre que temos orbitais eletrónicas parcialmente preenchidas, teremos estados de maior energia de momento angular.
- Na análise atrás em que determinamos o termo de diamagnetismo orbital usamos apenas teoria de perturbações de 1ª ordem. Se usarmos 2ª ordem, teremos um termo positivo - *paramagnetismo de van Vleck*. Este termo também não depende da temperatura e é inversamente proporcional à gap de energia de estados de momento angular. Como este gap costuma ser enorme, este paramagnetismo costuma ser desprezável.

##### Paramagnetismo de Pauli e Diamagnetismo de Landau
**Pauli**
- O paramagnetimos de Pauli consiste na susceptibilidade associada a eletrões condutores livres (portanto exclusiva de metais).
- Quando temos um campo aplicado é quebrada a degenerescência de bandas de spin-up e spin-down, havendo mais spins alinhados com o campo externo do que contra. Assim temos:
$$\begin{align*}
\chi_{P}&= \mu_{B}^{2} g(E_{F})~~,~~\text{[cgs]}\\
&= \mu_{0}\mu_{B}^{2}g(E_{F})~~,~~ \text{[SI]}
\end{align*}$$
(em que $g(E_{F})$ é a densidade de testados no nível de Fermi)
- Como só conta com os eletrões perto do nível de Fermi, esta susceptibilidade costuma ser fraca: $10^{-4}-10^{-5}\text{ emu mol}^{-1}$

**Landau**
- Esta é a contribuição orbital associada a eletrões condutores.
- Num modelo de eletrão livre, o diamagnetismo de Landau tem exatamente 1/3 da intensdiade do paramagnetismo de Pauli (mas com sinal oposto).
- Na realidade, isto varia conforme a massa efetiva dos eletrões condutores varia em relação à massa de eletrões livres.

##### Paramagnetismo de momento itinerante dependente da temperatura
- As contribuições de Pauli e Landau que acabamos de ver são independentes da temperatura, mas reduzidas.
- MAS isto não é verdade em todos os materiais. Isto é o caso em materiais em que existe forte correlação e-e : *itinerant magnets* (metais com magnetismo itinerante).
    - O magnetismo local de momento surge em cada átomo, devido aos eletrões sem par.
    - Magnetismo de momento itinerante é coletivo e deve-se à **bandas eletrónicas** que *passam a energia de Fermi*.
    - Muitos metais reais encontram-se num regime mixo de magnetismo local e itinerente

- Ora, metais itinerentes também exibem paramagnetismo semelhante a Curie-Weiss: $\chi$ é inversamente proporcional a $T$.
    - Ou seja, _podemos_ ajustar dados de um destes metais a uma função de susceptibilidade Curie-Weiss, mas $\theta_{CW},\mu_{eff}$ não têm o mesmo significado físico!
- Em metais "normais" com magnetismo de momento, só alguns valores discretos de $\mu_{eff}$ são permitidos (devido a quantização dos números quânticos de momento orbital). Em metais itinerantes já não é o caso

##### Transições de Fase
- Através da medição da susceptibilidade é normalmente fácil detetar transições de fase em que ocorre ordenamento magnético ou freeze do spin - aparece uma descontinuidade
- Conseguimos aprender coisas sobre as propriedades do material usado através desta transição:
    - *Ferromagnets* - a temperatura de Curie ($T_C$) separa os regimes em que os momentos magnéticos estão ou alinhados. Temos então a transição a esta temperatura.
    - *Ferrimagnet* - Os momentos magnéticos das várias latice é oposto, como em antiferromagnetismo - mas as intensidades são diferentes então não chega a haver anulamento do momento. Invés disso, surge magnetização instantanea. Assim, o comportamento destes materiais é igual ao de ferromagnets, mas o valor de saturação da susceptibilidade é menor
    - *Antiferromagnet* - Atinge-se o máximo na temperatura de Neel e temos aí transição. Na realidade, devido a impurezas paramagneticas (que vão com $1/T$), na vida real pode medir-se a susceptibilidade a subir sempre conforme vamos para $T<T_{N}$
    - *Supercondutor* - Ao atingir a temperatura crítica ocorre uma transição para um estado de resistência nula. Em termos de susceptibilidade, ocorre uma queda súbita. Em unidades SI, a densidade volúmica de susceptibilidade desce para -1 e em CGS desce para $\frac{-1}{4\pi}$. O arrefecimento durante a transição deve ocorrer sem campo! (*ZFC* - Zero Field Cooling).
![[evolucao perfis.jpg]]
![[perfis mag vs temp.png]]

#### Considerações Práticas
- Todas as contribuições para $\chi$ que vimos acima são teóricas. Agora vamos ver como, na prática, podemos recolher dados de alta qualidade e como fazer análise de dados.
- A análise neste artigo foca-se em amostras policristalinas (em pó).
    - Neste tipo de amostras, invés de aplicar campo magnético numa direção específica conforme a rede cristalina, aplicamos o campo "em todas as direções". Fazemos medições em todas as direções e depois juntamos tudo com médias.
        - Isto implica que não retemos informação sobre anisotropia da amostra.

##### 1 - Massa
- Medir a massa da amostra antes de fazer medições

##### 2 - Optimizar as medições 
- Isto inclui
    - Montar a amostra de forma a minimizar contribuições de fundo
    - Usar massas de amostra adequadas
    - Usar intensidade de campo adequada
- Aumentar demasiado a massa e/ou campo vai aumentar o signal to noise ratio.
- Além disso, a relação $M\propto H$ pode deixar de se aplicar a campos muito altos

##### 3 - Ajustar dados para $\chi$ molar
- Temos:
$$\chi_{mol}[\text{emu mol}_{N}^{-1} \text{ Oe}^{-1}]=\frac{M [\text{emu}]}{H [\text{Oe}]} \frac{M[\text{g mol}^{-1}]}{m[\text{g}]\cdot n}$$
- Em que
    - o primeiro $M$ em emu é a magnetização
    - o segundo $M$ é a massa molar
    - $n$ é o número de iões magnéticos por unidade de formula (?)
- Quando não sabemos $n$, podemos usar $n=1$ o que nos dá $\chi$ por unidade de fórmula

##### 4 - Começar análise
- Fazer gráfico $\chi_{mol}\times T$. 
- Ver quais das contribuições vistas acima esperamos que estejam presentes (conforme a natureza da amostra).
    - Os passos abaixo são para amostras em que se espera uma contribuição Curie-Weiss.

##### 5 - Momento Magnético efetivo / Ajuste
- Fazer gráfico $\chi_{mol}^{-1}\times T$. 
- Se virmos algo ~linear, tentar ajustar com equação de Curie-Weiss:
$$\chi^{-1}=\frac{T-\theta_{CW}}{C}=\frac{T}{C}- \frac{\theta_{CW}}{C}$$
daí temos o momento magnético efetivo
$$\mu_{eff}=\sqrt{8C}\mu_{B} [\text{cgs}]=800 \sqrt{C}\mu_{B} [\text{SI}]$$
e podemos comparar isto com o valor calculado com
$$\mu_{cal}=g_{J}\sqrt{J(J+1)}\mu_{B}$$
($J$ é o momento angular total e $g_{J}$ o "tensor g")

##### 6 - Detalhe do ajuste
- O ajuste faz-se com $\chi^{-1}\times T$ e não $\chi\times T$ - para o segundo caso o ajuste vai valorizar demasiado pontos de temperatura elevada. Ora, nesses pontos estamos mais longe do comportamento Curie-Weiss desejado.
- Além disso, limitar o range para o ajuste $\chi^{-1}\times T$ à zona em que visivelmente temos menos desvios do comportamento Curie-Weiss

##### 7 - Não linear
- Se $\chi^{-1}\times T$ não for linear, teremos uma contribuição extra que não depende da temperatura.
- Ou seja (se $\theta_{CW}=0$ ): $\chi=\frac{C}{T} + \chi_{0}$
![[paramagnetismo curie ajustes.png]]
isto pode ser: diamagnetismo de core (da amostra ou do suporte), paramagnetismo de Pauli, paramagnetismo de Van Vleck
- Neste caso podemos escrever:
$$\chi=\frac{C}{T-\theta_{CW}} + \chi_{0}~~\to~~\chi^{-1}=\frac{T-\theta_{CW}}{\chi_{0}(T-\theta_{CW}) + C}$$
(confirmar se o $\chi_{0}$ obtido por ajuste faz sentido fisicamente)

#### Mas...
- Estas regras são gerais e overall úteis. Mas nem sempre.
- Podemos até conseguir um bom ajuste, mas se as contribuições que temos que assumir para tal não fizerem sentido temos um problema.
- Mesmo quando o material _devia_ seguir a equação de Curie-Weiss, há fatores que fazem o modelo não se aplicar : amostra de baixa dimensão (no sentido de aproximadamente 2D ou até 1D), crossover de high e low spin, etc
    - Estes e outros fatores causam uma dependencia $\chi(T)$ que não é a de Curie-Weiss
- Aliás, sistemas que podem ou não seguir Curie-Weiss são a maioria.

#### Magnets de terra rara 4f
![[terra rara.png|375]]
- Devido à muito elevada massa destes elementos, o coupling spin-orbita (que aumenta com $Z^{4}$) domina as outras contribuições magnéticas.
- Nestes metais temos orbitais 4f parcialmente preenchidas que são muito localizadas e isoladas de iões vizinhos por orbitais 5s e 5p - isto faz o campo elétrico cristalino mais fraco
- Além disso, estas orbitais têm muito fraca interação/overlap com iões vizinhos. Por isso, é comum encontrar materiais com temperaturas de ordenamento magnético $<1\text{K}$.
    - Por vezes though, devido ao mecanismo RKKY (ver net) podemos ter ordenamento a temperaturas ~$10\text{K}$. 

- Estes materiais em grande maioria estão quase sempre no estado trivalente: $R^{3+}$. Neste caso, podemos calcular o momento angular total $J$ com as regras de Hund (ver wikipedia):
    1. Para uma certa configuração de eletrões, a combinação com maior multiplicidade é aquela com menor energia, tendo multiplicidade $2S+1$ (S é o momento angular de spin total de todos os eletrões)
    2. O termo com maior momento angular orbital $L$ tem a menor energia
    3. Num átomo, se o nível de valência está menos de meio preenchido, a combinação com menor $J=L+S$ tem menor energia. Se mais de meio preenchido, a combinação com maior $J$ tem menor energia.
![[rare earth mu.png]]
- Usando então os valores calculados (não sei como) vemos que os valores observados são medidos, na maioria dos casos. 

**Quando CW funciona**
- Na prática, magnets rare-earth seguem o comportamento Curie-Weiss na gama de temperaturas 200-400K (a gama exata depende do metal em si, claro).
    - Excepções importantes são: $\text{Eu}^{2+},\text{Gd}^{3+},\text{Tb}^{4+}$ - estes metais têm exatamente metade da orbital 4f preenchida. Por essa razão, a componente de momento angular orbital $L$ é nula. Assim, o comportamento Curie-Weiss é observado até temperaturas muito menores. 
        - Por exemplo para $\text{Gd}_{2}\text{O}_{3}$, temos um bom comportamento de Curie-Weiss na gama 25-400K. Com estes dados podemos fazer um muito bom ajuste e determinar $\theta_{CW}$


**Porquê que CW só se aplica numa gama**
- Mas para outros metais deste grupo (sem 4f exatamente meio preenchido), pois a temperaturas elevadas teremos a contar contribuições de níveis energéticos do cristal que não existem nas baixas temperaturas em que as interações magnéticas que queremos estudar ocorrem.
- Ou seja, na maioria dos rare earth magnets ajustar para obter $\theta_{CW}$ irá sobreestimar a intensidade das interações. 
    - Por exemplo, para uma amostra de $\text{Yb}_{2}\text{O}_{3}$ numa gama 200-400K obtemos um momento magnético efetivo coerente com Hund, mas obtemos $\theta_{CW}=-81\text{K}$, o que é demasiado elevado.

- Para determinar com mais precisão teríamos de usar métodos mais complexos. Mas podemos simplesmente aproximar o efeitos de níveis energéticos excitados do cristal:
$$\chi^{-1}=8(T-\theta_{CW})\frac{\mu_{\text{eff,0}}^{2}+\mu_\text{eff,1}^{2}e^{- \frac{E_{1}}{k_{B}T}}}{1+e^{- \frac{E_{1}}{k_{B}T}}}$$
em que $E_{1}$ é a gap de energia entre o nível fundamental e o 1º nível excitado, em que $\mu_\text{eff,0/1}$ é o momento magnético efetivo dos respetivos níveis energéticos.

**Quando CW não se aplica de todo**
- Para alguns metais o CW nunca se aplica, a nenhuma temperatura.
- Isto normalmente deve-se a fatores específicos do ião.
    - Um deles é a presenta de contribuição Van Vleck. 
        - Isto ocorre com $\text{Sm}^{3+},\text{Eu}^{3+}$. Notemos acima que na tabela acima os valores observados distanciam-se bastante dos de Hung.
        - Quando é este o caso, o gráfico de $\chi^{-1}$ apresenta um formato curvo (estilo $y=\sqrt{x}$). No gráfico abaixo os pontos preenchidos são $\chi$, os brancos são $\chi^{-1}$: ![[exemplo de cw nao aplicar.png]]
    - Outro caso é quando o paramagnetismo de Pauli é forte. Aí podemos corrigir usando a equação de CW modificada.

#### Magnets de Metais Transição 3d
- No caso 4f, orbitais parcialmente preenchidas estão bem localizadas. Não estão envolvidas em condução elétrica nem reações químicas. Orbitais 3d parcialmente preenchidas estão bastante envolvidas em ambas.
    - Isto complica as coisas, porque os graus de liberdade de eletrões e de magnetismo estão interligados em compostos de metais de transição 3d. Em alguns casos podemos até passar a ter paramagnetismo.
    - Quando não passamos a ter paramagnetismo, existe uma combinação de magnetismo local e itinerante.

**Isoladores**
- Orbitais 3d parcialmente preenchidas são as mais extensas espacialmente (menos localizadas), pelo que participam em bonding químico.
- Assim, a sua sobreposição com os iões é maior e a escala energética do campo elétrico da rede cristalina é maior.
    - Aliás, nestes metais a escala de energia magnética é a maior
        - Além disso, o preenchimento das orbitais é fortemente decidido pela simetria da vizinhança.

**Momento Magnético**
- Assim, como a escala de energia é tão alterada, deixam de se aplicar as leis de Hund. Assim, também o momento magnético é diferente.
- Em 4f, como vimos, o coupling de spin orbital aumenta com $Z^{4}$ domina. Aqui é o oposto, ele pode até ser ignorado. 
- Assim, como as interações de coulomb são muito intensas (overlap entre orbitais 3d e iões vizinhos), é demasiado dificil uma orbital 3d converter-se noutra por rotação. Assim, a média temporal de momento angular orbital é ~0.

**Momento de Spin**
- Assim, em magnets 3d, o momento magnético é aproximadamente o momento spin-only. 
- Isso significa que ficamos com o problema reduzido a contar eletrões sem par. Temos então o momento spin-only:
$$\mu_{cal}=2\sqrt{S(S+1)}\mu_{B}$$
(em que $g_{S}=2$ para eletrões)

**Cal VS Obs**
![[3d mu.png]]
- Temos uma coerencia bem boa. Especialmente para iões de massa reduzida. 
- O grande overlap orbita-ião leva a temperaturas de ordenamento magnético ~100K e até ~1000K em alguns casos. Isto ocorre porque temos mais interações de troca.

- Estas interações causadas pelo overlap notam-se nas medições de $\chi$. Para MnO temos:
![[exemplo 3d.png]]
surge um pico em $T_{N}$ - ocorre uma transição para comportamento antiferromagnético. O traçado $\chi^{-1}$ (pontos brancos) segue CW desde pouco acima da temperatura de transição até ~400K. Obtemos ainda $\theta_{CW}=-610K$, o que é muito elevado mas plausível para antiferromagnets.

**Desvios de CW - 4f VS 3d**
- Em 4f temos desvios deste modelo, porque o momento magnético varia conforme estados energéticos são desocupados consoante a temperatura desce.
- Em 3d os momentos são normalmente independentes da temperatura. 
    - A exceção é quando eles *variam* com a temperatura. Isso ocorre quando a energia de estados de alto e baixo spin são semelhantes. Isso pode acontecer quando temos 4-7 eletrões sem par em configuração octaedrica.
        - Isto acontece devido a crossover de configurações de alto e baixo spin, induzido pela temperatura. Isto acontece mais quando temos elementos orgânicos e quando existem interações inter-iões quase nulas.
        - Quando temos os estados a serem desocupados em metais 4f temos uma curva suave. Quando ocorrem estes crossovers de spin causam uma queda abrupa do momento angular.
- Este último ponto pode ser observado ao fazer um gráfico de $\mu_{eff}=\sqrt{8\chi T}$ VS $T$ e temos:
![[mu eff vs T.png]]

**Desvios de CW - dimensões**
- Outro fator que faz as amostras se desviar de CW é quando têm magnetismo de dimensão reduzida: quando são 2D ou quase 1D.
    - Ou seja, fugimos de CW quando as interações responsáveis por comportamento magnético ocorrem quase exclusivamente em 1 Direção.
- Este comportamento é mais evidente em metais 3d e pode normalmente ser identificado ao analisar a sua cristalografia. As interações em 1 só direção são causadas pela organização dos iões.
- Ainda assim, isto não é suficiente. Um metal com esta caraterística devia seguir CW. No entanto, a temperatura reduzida, a escala de energia das interações spin-spin e da energia térmica tornam-se semelhantes. Além disso, o ordenamento de momentos torna-se impossível/difícil devido a termos só 1D. Assim a susceptibilidade ganha um alto largo:
![[exemplo 3d 2.png]]

#### Magnets de Metal Transição 4d e 5d
- Bastante menores em número do que 3d e 4f.
- Orbitais 4d e 5d parcialmente preenchidas são ainda mais extensas espacialmente (ainda menos localizadas) do que 3d.
    - Isto significa que o overlap orbita-ião é ainda maior e o campo elétrico cristalino é muito elevado.
    - Existe menor repulsão on-site (??)
- Uma boa porção de metais 4d e 5d *não* tem momentos magnéticos localizados. Aliás, *nenhum* metal destes tem ordenado magneticamente (no bloco 3d quase metade é ordenado)
- Assim, (com a excepção de magnetismo de Pauli), magnetismo nestes metais é basicamente inesistente
- Mas existe uma pequena fração destes metais que tem momentos magnéticos, seguindo CW com um regime paramagnético.
    - Isto acontece em sistemas com trocas inter-ião especialmente fracas:
        - magnets moleculares
        - sólidos cristalinos com espaçamentos muito grandes entre iões

- É mais difícil caraterizar o comportamento de metais deste bloco, já que se encontram algures entre o comportamento conforme Hund do bloco 4f e o comportamento do bloco 3d. 
- Devido ao campo cristalino alto e à repulsão baixa, iões 4d e 5d têm quase sempre configurações de spin reduzido. Isto limita bastante a gama de iões que podem sequer ser magnéticos

**CW e Coupling spin-orbita**
- Quando as medições de susceptibilidade seguem CW, normalmente o estydo disso permite avaliar a força do coupling spin-orbita. 
    - Consideremos que temos uma boa ideia do estado de valência de um certo ião 4d ou 5d
    - Fazemos ajuste CW e calculamos o momento paramagnético 
    - Comparamos este momento com os 2 casos limite:
        - O momento obtido ao considerar o spin só
        - O momento calculado com as regras de Hund


#### Frustração Magnética
- Este termo refere-se a materiais em que ocorrem 2 interações opostas, pelo que nenhuma delas se consegue concretizar por completo.
    - Isto pode acontecer devido a limitações causadas pela geometria da latice.
    - Também pode acontecer devido às interações em si, que podem competir
    - Ou ambos os casos acima misturados, claro
- No final isto resulta em supressão do ordenamento magnético durante a transição. Assim, acabamos com um ordenamento mais exótico ou sem ordenamento de todo.
- Usando CW podemos definir o *índice de frustração magnética*:
$$f=\frac{\theta_{CW}}{T_{N}}~~;~~f=\frac{\theta_{CW}}{T_{f}}$$
($T_{N}$ - Temperatura de ordenamento magnético, $T_{f}$ - temperatura de freeze)
Em materiais em que não ocorre ordenamento nem freeze, podemos usar a menor temperatura medida como um substituto de $T_{N}$ de modo a obter um limite de $f$.

- A lógica deste index é:
    - Para um metal sem frustração deveria ordenar-se por volta da temperatura de CW: $f\simeq1$ (em módulo pelo menos)
        - Na realidade, não temos bem isto. A maioria dos materiais sem frustração têm $f=2-5$, o que se deve a efeitos de vizinhança que o modelo CW não conta.
    - Para magnets com frustração teremos $f>5$, tendo-se até casos de $f=100$.

- Este índice é especialmente útil para metais 3d, porque nele o valor de $\theta_{CW}$ costuma ser de confiança.