## Raman em geral
- O Raman  do IFIMUP faz espectroscopia a alta temperatura e/ou alta pressão.
- Espetroscopia Raman consiste em detetar fonões de alta energia da 1ZB
    - De notar que, mais especificamente, vemos os fotões do centro da 1ZB e não todos  
- No instrumento é preciso ter uma rede de difração de alta qualidade - ela influencia muito a resolução obtida
- Usamos um laser para excitar a amostra (pode ser verde, IR ou He-Ne). Este encontra-se num sistema fechado, sendo que o laser é automaticamente desligado quando algo é aberto.
    - Nas palavras do agostinho, é muito difícil fazer asneira ou magoar-nos no Raman
    - Se fizermos algo mal (ex: escolher a rede de difração errada para o laser selecionado), o sistema só não faz nada
- As medições ficam na unidade $\text{cm}^{-1}$, que pode ser convertida com:
$$\boxed{1 \text{THz} = 33.3 \text{cm}^{-1}}$$
esta escala é usada porque costuma dar números menores e "mais simples".
- Ao mudar o laser NÃO muda o espetro. Isto porque ele já tem freqs relativas à do laser  
- Um laser diferente permite reduzir ou evitar fluorescência
- Não dá com metais porque o fotão não é scattered devido aos eletroes livres. Como fotão não volta, não podemos usar raman porque não há imagem
- Os picos stokes têm mt mais intensidade porque acontece muito mais, devido a razões probabilísticas: é mais fácil o fotão ceder energia do que absorver.
- Materiais mais perfeitos têm mais sintonia e picos mais estreitos.

### Alto arrefecimento
- Existem 2 criostatos no lab:
    - Um sistema aberto que permite descer até 4K usando Hélio *líquido*. Podemos aplicar campo até 7T. Para estudar uma amostra neste criostato, usamos uma espécie de periscopio para ligar o Raman à janela de quartzo amorfo
    - Um sistema fechado que permite descer até 10K usando Hélio *gasoso*
- Temperatura mais baixa - contratações - átomos mais juntos - vibram mais - freq maior - espetro vai para a direita  
    - Picos ficam mais finos a baixa temperatura pq átomos estão mais juntos e vibram em sintonia
- Maior largura == menos tempo semivida. Largura e semivida têm relação inversamente proporcional  
- Ao aquecer os picos ficam muito largos porque as oscilações são mais rápidas, e é difícil distinguir picos. Ao arrefecer, fica tudo mais estável e lento então picos ficam mais finos. Ou seja, temperatura inferior ajuda a distinguir frequências dos picos. As freqs não mudam com a temperatura 

### Componentes
- Temos 2 redes de dirfação: 1800 linhas/mm e 2400 linhas/mm. Estão ambas montadas no instrumento e o software escolhe a correta de acordo com o laser selecionado
    - Ambas estas redes são boas com lasers verdes ou vermelhos
- Temos um CCD que está a -70C, graças a um peltier cooler
- Existe um filtro de rejeição que corta bastante o efeito de Scattering de Rayleigh e outros efeitos indesejados
- Existe um analisador. Alguns fonões mudam a polarização da luz do laser. Podemos estudar isso

## O software
- Selecionamos/ligamos a câmara. Baixamos a lente manualmente, até a imagem ficar focada
- Podemos fazer isto com os parafusos micrométricos ou com a trackpad com uma bola
- Também ajustamos a intensidade de luz fornecida, de modo que seja visível algo
- Quando parece bem, ligamos o laser. Focamos. Desligamos tudo

### Setup
**Range**
- Definir janela em cm-1: estática ou enhanced
    - **Estático/static** : a rede está parada e fixamos uma gama de valores. Espetro aparece instantaneamente no software
    - **Enhanced** : a rede roda lentamente e medimos em contínuo, permite uma gama maior mas demora mais a medir. O espetro aparece gradualmente, das freqs altas para as baixas
- Escolher laser
- Escolher rede

**Aquisição**
- Colocar médias
- Definir potência do laser 
    - Existe um excel que diz que potência escolher para uma certa rede, ganho, comprimento de onda, etc
    - Escolhemos 3.3mA para rede 1800, ganho 50x, laser verde
- Escolher filtro
- Acumulações e tempos de aquisição
    - O Raman mede X vezes (acumulação) por Y segundos. Ele combina estas X medições para minimizar o SNR

**File**
- Definir nome do ficheiro de dados inicial "ABC"
- Depois consoante guardamos mais coisas o software liga "ABC-1" e por aí fora
- Estes ficheiros são txt e só têm as frequências e intensidades

**Depois do software**
- Depois de colocar tudo no software, apagar as luzes
- Ligar laser e câmara, mover lentes até laser ficar focado num ponto

# AMOSTRAS
## Pirite
- AKA dissulfeto de ferro
- Tem estrutura FCC e efeito Raman forte

### Setup
- Fizemos zoom, reduzimos intensidade da luz. Repetimos isto até estar bem focado
- Depois, ligamos o lazer e fizemos zoom até ele está focado em 1 ponto

**Software**
- Range: 83-1800cm-1, estático
- Aquisição: 10s, 3 acumul
- Laser: 10%, verde
- Rede 1800

### Medidas
1. Focado numa zona limpa
2. Focado numa zona menos limpa, rodado 90º, com o mesmo setup acima
3. Tudo igual à 2. *Mudança*: agora temos aquisição de 20s, acumul 3

- Obtemos 3 picos em torno de 200cm-1 (bate certo com artigo que vimos)
    - Só vemos 3 porque os fonões podem ser pequenos (?) e temos um sistema de simetria centrada
    - Nas medições 2 e 3 temos picos menos simétricos porque podem ter 2 fonões misturados

## Silício
- Isto foi um pedaço de wafer
- Isto não é sílica (o óxido), mas sim "Si" mesmo
- Vimos as bandas de fonões do Si e tem 1 fonão ótico com dupla degenerescência. Este está em 15.6THz  (520 cm-1)
- Não apontei bem o setup, mas vimos o esperado

- Fizemos fit do pico Si com lorentziana e bateu muito certo com pico em 520.47THz  
- Tiramos o filtro e vimos o pico Rayleigh praticamente no zero
- Vemos o pico de raman de Si que bate certo com centro 1ZB  
- Temos um alto a freq maior. Esta corresponde ao efeito raman 2a ordem.  
- Mudamos range para +/-100cm-1. Assim devíamos ver pico stokes forte, pico anti stokes na freq simétrica mas bastante mais fraco. Não vimos pq filtro cortou :(  
- O pico Rayleigh que vimos é muito fraco e estreito por causa do filtro. Sem ele teriamos um pico muito mais largo e alto.

## Água
- Água H2O tem 9 graus de liberdade:
    - 3 de translação (x,y,z)
    - 3 de rotação (roll, pitch, yaw)
    - 3 de vibrações internas
- Para as vibrações internas, temos 3 modos normais:
    1. Em fase, com frequência $\nu_{s}=3400cm^{-1}$ (os dois Hs sobem e descem em sintonia)
    2. Anti fase, com frequência $\nu_{as}>\nu_{s}$ (um H sobe, outro desce)
    3. Bending, com frequêncai $v_{b}=1400cm^{-1}$ (os Hs vão na direção e para longe do centro da molécula, em sintonia)

- Devido a pontes de hidrogénio, as moléculas estão sempre a ligar-se entre si e ficamos com picos muito largos
- Medimos em água líquida, sendo que esta está num tubo de quartzo

### Focar
- Para focar, tivemos que usar logo o laser (com uma luz teríamos reflexão)
    - Ao aproximar a lentes, aparecem manchas de luz
    - Ao aproximar mais, as manchas aumentam e aproximam-se. Continuam. Forma-se um ponto "gordo"
        - Focamos na superfície externa do tubo de quartzo
    - Eventualmente o ponto desfoca. Continuamos a aproximar. Repete-se o processo anterior. 
        - Agora estamos a focar na superfície interna do quartzo
    - Continuamos a aproximar mais um pedaço. Eventualmente desfoca uma 2a vez e fica tudo escuro. Neste ponto estamos a ver a água em si

### Setup
- Range:
    - Não pode ser estático, porque nenhuma gama do instrumento irá cobrir $\nu_{a},\nu_{as},\nu_{b}$
    - Usamos *enhanced* de 1000 a 3000 (apanha os 3 modos)
- Aquisição: 10s, 1 acumul
- Como temos enhanced demora mais do que estes 10s
- Laser: 50% ("água não queima")
- Vimos o espetro esperado: 3 picos muito largos, em que os picos de A,AS se misturam. Vimos ainda um pico entre B e S, que é gerado pelas redes H

### Medições
1. metemos estático - deu erro?
2. Metemos enhanced e 1 acumulação
3. Metemos enhanced e 2 acumulações
4. Metemos enhanced 100-3000 com 2 acumulações

- Na 3a vimos um pico extra muito random. Isto é o que é chamado de "cosmic rays" - um fotodíodo do CCD descarregou. Chamamos de "cosmic ray" mas na realidade não é bem isso (estamos no piso -2, os raios não penetram tanto betão)

## Artigo
- Seguimos o artigo no sigarra, com o mesmo substrato e filme fino crescido em cima dele

- Usamos um Linkam (esta é a marca, mas aparece logo ao meter no google)
- Podemos ir até +600C (água aquecida e pressão) e podemos ir abaixo de 0C (N2 líquido)
- Permite medir a temperatura, Raman e ainda a resistividade com 4 pontas
- **Ao arrefecer**, temos que fazer vácuo na câmara para a água no ar não congelar, o que iria impedir a espetroscopia
    - Se escapar algum, temos que repetir tudo
- Metemos papel de rolo por baixo do linkam, porque fica tudo gelado ao arrefecer, então ficava tudo molhado
- Ligamos o tubo da garrafa de azoto ao linkam e deixamos o tubo na ligação oposta solto, para fazer de exhaust
- Vimos a imagem da câmara a desfocar enquanto a amostra arrefece. Isto mostra que ela contrai.
- Esperamos que o sistema arrefeça a amostra até -193C  
- Quando imagem deixou de desfocar, medimos. Temperatura estabilizou.
- O substrato não tem transição estrutural, logo os seus picos não mudam de posição.  
- Entre os picos grandes, temos um pico da fase de 193C perto de um da fase de 20C, à esquerda. 
    - Mas NAO são msm fonao. Se fosse, o 193 ia para a direita do 20 pq expansão térmica. 
    - O pico 193C (e um pequenino à direita) é na verdade um pico da estrutura mono clínica que não existe no 20C

### Purga
- Colocamos de 20C a 40C, num rate de 115C/min. Ficamos em 40C por 1000 minutos
- Tapamos todas as saídas de azoto. No tubo de exaust tapamos com o dedo. Vamos tapando e destapando por uns minutos.
    - Quando tapamos, N2 acumula-se na câmara e aumenta a pressão
    - Ao destapar, o azoto sai com pressão e "arrasta" CO2 e H2O para fora


### TUBO
- Metemos um tubo de ar comprimido (?) sobre o linkam. Este garante que não se forma gelo no vidro e o Raman consegue ver
    - No final, ao desligar, vimos que ficou logo tudo coberto de gelo
