**"Structural percolation evolution throughout the metal-to-insulator transition in NdNiO3"**
#### Abstract
- Neste artigo é estudada a mudança de fase de um filme fino de NdNiO3 depositado com orientação 001 em LaAlO3. 
- Ocorre uma MIT : Metallic to Insulating phase Transition
- A amostra foi observada com Raman e viu-se que existem uma fase ortorrombica e uma monoclinica a coexistir.

### Introdução
- Nickelates $R \text{NiO}_{3}$ são compostos que têm grande correlação entre os graus de liberdade de latice, spin e carga/orbitais eletronicas
    - Isto permite que consigamos controlar transições de fase
    - Ao fazer isto, podemos melhor entender os fenómenos eletronicos, estruturais e magneticos envolvidos na MIT. 
- Um material deste tipo que se destada é NdNiO3 (**NNO**). Ele situa-se numa região em que a MIT e a transição de Neel se distanciam (?)
- Em condições ambiente, NNO é um paramagnet metalico com estrutura ortorrombinca Pbnm.
- Abaixo de $T_{IM}=200K$ ele faz uma transição eletrónica e passa para um estado isolador. Nessa fase, ele tem estrutura monoclinia com simetria $P2_1/n$ e é anti-ferromagnético (AFM).
    - Podemos ainda definir o estado de baixa Temp como um semicondutor de baixo $\Delta$.
- No entanto, devido à natureza da MIT, durante um range de ~28K as 2 fases *coexistem*.
    - Na escala macroscópica, esta transição é de 1a ordem.
    - Na escala nano, ela comporta-se mais como de 2a ordem : o isolador converte-se em paramagnet de forma contínua

- Este fenómeno de transição e de formação de isolador já foram observados de diversas formas (como XRD a diferentes Temps)
- Existem varios dados (teoricos e exps) que parecem confirmar que a MIT é acompanhada da transição estrutural de Ortorrombica para Monoclinica
    - Pensa-se que a transição para estado AFM altera o ordenamento de eletrões, o que por sua vez incentiva a ocorrência de MIT. 
    - Ou seja: $T_{IM}=T_{N}$

- Este trabalho pretende preencher dados em falta. É feito um estudo do sequenciamento eletronico, magnetico e estrutural. 
- É feito Raman dependente de Temp, assim como estudo de resistividade e magnetização. 

### Exp
- Um filme fino de NNO foi depositado em substratos de LaAlO3 com MOCVD.
    - Todo este procedimento experimental foi feito em 1 só amostra
- A amostra foi caraterizada usando SEM e EDS (energy dispersive X-ray espectrometry). Foi ainda feita análise XRD
- As medições de resistividade foram feitas com um método normal de 4 pontas in-line. Estas foram feitas com um rate de aquecimento/arrefecimento de 2K/min no range 30-300K.
    - A tensão foi medida nas pontas de dentro
- O espetro de Raman foi medido com um laser He-Ne 633nm, no range de 100-800 cm-1. 
- Medições de ??? em função da temperatura foram feitas no range 70-300K, usando um criostado de ciclo fechado de He.
- Medições de magnetização em função de temperatura foram feitas com o SQUID no range 10-300K

### Resultados
#### Caraterização
**SEM**
- O filme fino tem superfície suave e sem defeitos:
![[filme fino raman.png]]
vemos ainda na imagem da direita que existe uma grande homogeneidade na espessura do filme. Vemos ainda que não há uma estrutura interna da camada.

**XRD**
![[xrd e espaço reciproco.png]]
- A direção de crescimento principal de NNO e LAO são próximos. Assim, os seus picos quase se sobrepõe, de modo que para obter este espectro acima foi colocada a amostra a 0.25º.
- Podemos ainda ver o espaço reciproco determinado (?)

#### STEM - scanning transmission electron microscopy
- Foi preparada um secção transversal da amostra usando FIB. Depois usando STEM foram obtidas imagens.
![[imagem sem nno.png]]
verifica-se que resceram estruturas "cube on cube", formando uma camada de 85nm (imagem da esquerda).

- Abaixo temos os resultados EDS, em que vemos as posições dos 4 elementos mostrados:
![[imagens raman nno.png]]

- Usando analise de fase geométrica (GPA) de imagens HAADF, obtivemos os mapas abaixo:
![[imagens raman strain nno.png]]
na imagem da esquerda, vemos que na maioria da região temos um strain perto de zero. Isto indica que temos um bom match entre o filme fino e o substrato.

- Na imagem abaixo temos 2 parametros de rede conforme nos afastamos do interface filme-substrato: 
![[parametro rede nno.png]]
vemos que nas camadas mais profundas temos uma variacao de $c_{pc}$. Isto bate certo com o perfil com alto strain na iamgem e) acima. Isto parece confirmar uma deformação paralela ao interface.

#### MIT e transição magnética
![[resistividade nno vs temp.png]]
- Acima podemos ver como a resistividade do filme NNO variou com a temperatura, no aquecimento e no arrefecimento.
- Esta curva é carateristica para NNO. A histerese vem da coexistência de estados metálicos e isoladores. 
-  Assim, devido à intensa histerese temos que a temperatura crítica é local. Ou seja, é diferente ao aquecer e ao arrefecer. Temos então que $T_{MI}<T_{IM}$. 
- Podemos definir *regiões* de transição. Estas foram determinadas como sendo as temperaturas em que a derivada do logaritmo da resistividade se afastam do zero.

![[resistividade nno vs temp 2.png|350]]
- O inset mostra a dependência na temperatura de $(M/H)^{-1}$ em que temos a magnetização a dividir pelo campo aplicado (que foi 100Oe).
- No gráfico em si vemos os resíduos  de ajustar os dados da fase PM à relação Curie-Weiss.

#### Coexistencia de fases
![[raman vs temp.png]]

--- Não acabei :(
