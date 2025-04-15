**"Controlling phase transitions in MnNiGe using thermal quenching and hydrostatic pressure"**
### Abstract
- Foram estudadas transições de fase de compostos de MnNiGe ao variar condições de calor e pressão hidroestatica.
- Consoante as amostras sofrem quenching de temperatuas mais altas, as temperaturas das transições (estruturais e magnéticas) de fase baixam
- Apesar de as temperaturas de transição mudarem, análise raio X revelou que as células serão idênticas

## Introdução
- Este estudo pretende auxiliar no fabrico de materiais magnetocalóricos para refrigeração magnética
- Estudo de materiais com elevado coupling magneto-estrutural tem aumentado
- Em especial, materiais do tipo MnXGe (X é um metal de transição como Ni) têm elevado efeito magnetocalórico

*Estrutura*
- Mas este material tem ainda outra propriedade interessante: variação alta de volume aquando da transição estrutural.
- Este material cristaliza numa estrutura ortorrômbica
- Conforme varia a temperatura temos:
![[fases magneto-struct.png]]
- Segundo alguns artigos, as transições podem ser controladas dopando o material com outro elemento (substituir parcialmente o Mn, Ge ou Ni)
- Mas modificar a estequiometria, pressão aplicada ou a rapidez com que o material solidifica pode alterar bastante as transições.
    - Em versões dopadas de MnNiGe foi demonstrado que tratamentos de calor podem alterar estas transições
- Este estudo pretende ver se este tipo de tratamentos pode alterar as transições magneto, estrutural ou magnetoestrutural

*Amostras*
- Primeiro derreteu-se Mn,Ni e Ge juntos
- Porções deste material inicial foram depois processadas com annealing, quenching e/ou slow-cooling.
- Ao usar uma elevada temperatura de quenching, a temperatura de transição de estrutura baixou bastante (~200K) e a de transição magnética baixou um bocado (~50K)
    - A maior temperatura de transição obteve-se ao arrefecer a amostra lentamente de 1100 a 30ºC/h

## Preparação das amostras
- As amostras de MnNiGe foram produzidas usando quantidades estequiometricamente iguais de Mn, Ni e Ge (todos com purezas muito elevadas).
- Os materiais foram colocados em crucibles e aquecidos até 1100ºC e deixados por 12h. 
    - Depois arrefeceram naturalmente e foram esmagadas com almofariz e pilão.
    - Os materiais esmagados foram novamente aquecidos (para ter mais homogeneidade) até 1100ºC e deixados por 12h. Depois foram arrefecidos a 30ºC/h
    - O ingot obtido com este aquecimento foi chamado de SC1100 (slowly cooled) e serviu de base/fonte para o resto
- Partes da amostra fonte foram colocadas em crucibles de alumínio e selados em tubos de quartzo sob vácuo
    - As amostras foram aquecidas até 1000,1100,1200, deixadas por 12h e depois quenched. A estas amostras chamou-se AQ100, AQ1100, AQ1200
- No final, teve-se:
![[params estrutura exs.png]]

## Análise térmica
- O processo de formação do composto foi monitorizado termicamente com um calorímetro e dispositivo de termogravimetria.
- Fez-se varrimento da temperatura até 1100ºC e de volta.
- Observa-se 1 pico de 1ª ordem, associado à transição de cristalização/fusão
![[ciclo de transicao mnnige.png]]

## Resultados de magnetização
- As medições magnéticas foram feitas usando um MPMS
- As medições iso-campo foram feitas num campos de $\mu_{0}H=0.1T$ e com um varrimento de temperatura de $2$ K/min de 100K a 400K em ida e volta.

### Resultados pressão ambiente
- A magnetização medida em iso-campo e com variação de temperatura deu:
![[transicoes de varias componentes.png]]
podemos ver que ocorrem transições. As temperaturas de transição estão na tabela acima.
- No degrau da direita de cada curva temos a transição de estrutura. Para AQ1200 ocorreu na temperatura mínima (maior temp de quenching -> menor temp de transição)
- Os autores pensam que se a temp de quenching for alta o suficiente não ocorrerá transição de estrutura de todo - apenas existiria a estrutura hexagonal
    - Ou seja, uma temperatura de quenching elevada poderia levar a um material altamente organizado
- Temos este diagrama de fase:
![[diagrama de fase mnnige.png]]

### Resultados a pressão hidroestatica
- Usou-se as amostras AQ1100 e AQ1200 (que têm temperaturas de transição mais baixas) e foi medida a magnetização vs temperatura, agora com pressão hidroestatica. Para isso usou-se uma célula de pressão e óleo.
- Para ver a intensidade da pressão usou-se uma amostra de Sn presente na célula de pressão. Mediu-se a temperatura da transição supercondutora deste para ver a pressão
- Obteve-se:
![[transicao de veroes de mnnige.png]]
- Consoante a pressão é aumentada, as transições de fase de AFM spiral (Ver diagrama, são o degrau em subida) aumentam de temperatura. A temperatura da transição de estrutura (degrau em descida) diminuem de temperatura.
- Foi observado que a temperatura das transições de estrutura diminuiu de forma linear com a pressão. Temos aqui o rate com que a temperatura diminui para vários materiais:
![[rate de expansao de versoes de mnnige.png]]
- Também as temperaturas de transição spiral aumentaram de forma linear. Podemos traçar isto:
![[variacap de params struct.png]]
assim, se a pressão for suficientemente alta, a transição de estrutura poderá não ocorrer.

## Cristalografia raio X
### XRD a 100K
![[espectro de versoes de mnnige.png]]
- Mostram que há elevada pureza
- Consoante temos maior temperatura de quenching, o volume das células diminui

### XRD na transição
- A transição entre fases ortorrombica e hex pode ser considerada uma distorção, do tipo:
$$\begin{align*}
a_{ort} &\leftrightarrow c_{hex}\\
b_{ort} &\leftrightarrow a_{hex}\\
c_{ort} &\leftrightarrow \sqrt{3}a_{hex}
\end{align*}$$
![[variacao de params mnnige 2.png|425]]
- Consoante a temperatura aumenta e transitamos da estrutura ortorrômbica (baixa temp) para estrutura hexagonal (alta temp)
- Vemos que há redução de 10.4% na direção de $a_{ort}$ e 7.5% de expansão na direção de $b_{ort}$
- Nas várias amostras, apesar a temperatura de transição ser diferente a variação de volume é igual em todos.

