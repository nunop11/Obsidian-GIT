# Montagem
- Temos a montagem sobre um sistema de refrigeração que a mantém a 1ºC (o objetivo era manter com temperatura ~0ºC)
- Entre passos excluimos 1 amostra, de modo a poder observar a evolução do processo num SEM. Para isto, tapamos as amostras com uma tampa. 
- Usamos um cátodo de platina porque a platina é um metal que não oxida e é inerte, pelo que não irá afetar os processos. (Por exemplo, podíamos usar um de cobre, mas acabaríamos por depositar cobre)
    - **NOTA** : "Ánodo atrai aniões, Cátodo atrai catiões"

# Anodização 1
*Labview e montagem*
- Usamos *ácido oxálico*
- Temos o parametro "tempo transiente" no labview, que será o tempo em que há maior variação da corrente e em que queremos mais dados.
- Na realidade, o programa crashou no final do tempo transiente. Assim, houve uns instantes que marcaram o reiniciar do programa. No total, realizamos anodização por 20 minutos
- No gráfico da segunda metade da anodização temos o gráfico a fazer uma subida e descida no final. Isto aconteceu porque a ventoinha usada para mexer a solução parou. A subida do gráfico ocorre quando a ligamos de novo e a descida quando ela se voltou a desligar.

*Início*
- Começamos com $T_{0}=7.2ºC$
- No início a corrente satura. Isto acontece porque quando começamos o processo apenas temos o alumínio. Quando são aplicados 40V através deste sistema, temos aproximadamente *zero resistência*, pelo que medimos uma corrente muito alta. O valor no gráfico satura devido a limitações de segurança do instrumento utilizado.
    - Logo de seguida a corrente cai muito rapidamente porque começa a forma-se óxido (alumina) em toda a amostra, fazendo a resistência subir. **NOTA** : alumínio é condutor, alumina é isolador

*Escolha do metal*
- Este processo de anodização é bastante industrializado, sendo usado com alumínio para o colorir e tirar o brilho.
- Pode ser usado com muitos metais, desde que não sejam nobres (ou seja, podemos usar qualquer metal que oxide: Ferro, Titânio, etc). A este grupo chamamos de *valve metals* (metais que geram oxidos muito resistivos).
    - Nesta atividade usamos alumínio, porque a relação entre as densidades atómicas deste metal e do seu óxido têm a relação que mais favorece a auto-organização da latice.
    - Mais precisamente, a densidade do alumínio é ~2.7 e a da alumina é ~4. (isto foi o que vi online, mas é estranho porque apontei que o prof disse que alumina é menos densa)
    - O processo de auto-organização é algo do tipo: conforme a alumina é sintetizada ela tem que se mover por causa do campo E, o que permite a continuação do processo de anodização. Nisto, os átomos de alumina acabam a aglomerar-se em colunas, o que gera túneis bem dispersos.
    - Dito de outra forma: a alumina reorganizasse de forma a minimizar as tensões mecânicas.
- O titânio também teria sido uma boa opção, mas seria mais dispendioso.

*Reação química*
- O alumínio faz o papel de ánodo, porque é rico em $O^{2+}$. O cátodo tem muitos eletrões livres.
    - Assim, ocorrem 2 reações que se complementam:
        - No ánodo: $2Al+3H_{2}O = Al_{2}O_{3} + 6H^{+} + 6e^{-}$ 
        - No cátodo: $6H^{+} + 6e^{-}=3H_{2}$
        - A reação de anodização do alumínio: $2Al+3H_{2}O=Al_{2}O_{3}+3H_{2}$
- Assim, ao longo do tempo, o alumínio vai-se oxidando e gera-se uma camada de alumina no topo deste. 

*Porquê ácido*
- Poderíamos pensar: porquê fazer esta reação num ácido (oxálico) invés de usar água destilada?
    - Se fizéssemo isto num meio neutro (água destilada) teríamos a corrente a cair exponencialmente conforme a espessura da camada de alumina aumenta. Eventualmente, o alumínio deixava de oxidar.
    - Ao usar um eletrólito (ácido oxálico) teremos um campo/potencial diferente ao longo da amostra. Isto vai fazer com que se gerem túneis na alumina, para "o campo conseguir atuar melhor".

*O gráfico*
- Se observarmos o gráfico $I(t)$ da anodização, vemos que ele começa elevado, atinge um mínimo e sobe, estabilizando no final.
    - O pico inicial corresponde ao já referido: no início apenas temos alumínio, logo a resistência é mínima e a corrente máxima.
    - O mínimo corresponde ao momento em que temos a espessura máxima da camada de alumina
    - Após o mínimo começam a gerar-se tuneis na camada, o que faz com que a corrente volte a subir
    - A parte horizontal e estável no final do gráfico acontece quando os túneis estão bem defenidos e a corrente consegue circular bem.

# Remoção da Alumina
*O que fizemos ao certo*
- Aquecemos a solução até ela atingir $T\sim45ºC$, invés dos 50ºC previstos. Em contrapartida prolongamos esta parte do processo para *20min invés de 15min*.
- Usamos água destilada para limpar amostra e retirar o ácido antes de introduzir a solução quente.
- Colocamos a amostra na placa de aquecimento a 100ºC e só depois introduzimos a solução.
    - Aos 5min tínhamos $T\sim 35ºC$
    - Aos 24min tínhamos $T\sim53ºC$

*Porquê?*
- Esta solução e condições de temperatura permitem remover a alumina sem afetar o alumínio. Ora, após a criação dos túneis na 1º anodização e consequente remoção, o alumínio fica com a topologia ideal para acolher alumina na 2ª anodização.
- Isto, combinado com a tendência de auto-organização da alumina que vimos acima, permite obter poros bem distribuidos. Estes encontram-se numa rede hexagonal, com defeitos nos locais onde a rede de alumínio original tem defeitos.

# 2ª Anodização
*Nota*
- Por volta dos 5min a ventoinha parou. (no gráfico do excel vemos claramente oscilações nesta região)
    - Após isso e durante a formação das dendrites, nunca parou.
- Não há muito a notar nesta parte

## Formação de Dendrites
*Campo elétrico*
- Inicialmente não temos dendrites. Assim, para a tensão de 40V temos poros de alumina com uma espessura de 40nm (verificar de onde isto veio. Artigo?)
- Ora, isto diz-nos que o campo elétrico aplicado é $E=\frac{V}{\delta}=1\text{ V nm}^{-1}=10^{9}\text{ V m}^{-1}$.
    - Nota: o campo elétrico atómico é da ordem de $V/\dot{A}$, apenas 1 ordem de grandeza superior.

*Labview*
- Nesta atividade temos uma densidade de corrente desejada de 70 mA/cm2
- Verificamos que cada amostra tem 1cm de diâmetro. Assim, vemos que a corrente limite a introduzir no labview é: $I=70 \cdot \pi \cdot (\frac{1}{2})^{2}=55\text{mA}$. 
- A porção responsável pela formação das dendrites vai de 40 a 8V de forma exponencial.

*Formação das dendrites - como ao certo?*
- Como já vimos, começamos com 40V e poros com 40nm de espessura.
- O labview reduz a tensão, ficando (por exemplo) 39V (seria algo como 39.99V) . Ora, agora temos um campo de $39/40\sim0.98\text{ V nm}^{-1}$. 
- Mas a alumina precisa de voltar aos 1 V/nm de modo a ter equilíbrio. Assim, é necessário reduzir a espessura da camada de alumina. 

- No início, isto significa que os poros (inicialmente em forma de "U") começam a ficar mais profundos mas também ficam mais estreitos (até ficarem em forma de "V").
- Eventualmente, chega um ponto em que a base do poro é tão estreita que o campo vertical não consegue reduzir a espessura da camada. Assim, o campo deixa de ser só vertical e começam a gerar-se novos tuneis para o lado (o túnel original subdivide-se). A estes túneis, claro, chamamos **dendrites**.

# Eletrodeposição
*O que fizemos aqui*
- Aquecemos a solução até ~35ºC. Enquanto esperávamos que esta aquecesse, preenchemos as amostras (não tapadas) com água destilada. Fazemos isto porque as dendrites são estruturas frágeis e não é boa ideia deixar que elas sequem.
- Nesta parte tivemos que troacr a polarização dos terminais da fonte de tensão DC relativamente ao guião? Não percebi bem
- Começamos esta parte da atividade com uma temperatura de ~32ºC
- 