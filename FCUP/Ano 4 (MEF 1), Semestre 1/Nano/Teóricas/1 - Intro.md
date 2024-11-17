# 1 - Introdução
### O que é nanotecnologia?
- "Termo que se refere às tecnologias que medem, manipulam ou incorporam materiais e/ou caraterísticas com pelo menos 1 dimensão entre 1 e 100 nm. Nestas dimensões emergem propriedades distintas dos materiais em escalas macroscópicas."
- "Compreensão e controlo de matéria com dimensões entre 1 e 100 nm, onde fenómenos únicos permitem aplicações inovadoras"
- "Arte e ciências de contruir coisas que fazem coisas à escala nanométrica" - Smalley

- Nanotecnologia apresenta, como dito acima, apresenta propriedades diferentes de materiais macroscópicos compostos dos mesmos elementos.
- Além disso, a escala destes materiais é comparável àquela de processos elementares como ADN.

### História
- Ao longo da historia usou-se nanotecnologia (sem saber). Por exemplo, gregos e romanos usaram nanocristais de sulfite e ouro. 
    - Os nanocristais de ouro são um caso interessante: o tamanho dos cristais influencia a cor percepcionada. Veremos melhor abaixo.
- Mais no PPT

### Aplicações
- *Circuitos integrados* - o tamanho reduzido permite obter menor consumo e maior velocidade
- *Armazenamento de dados* - o tamanho reduzido permite obter maior capacidade
- *Semicondutores* - podemos fazer fenómenos de partículas isoladas (quantom dot)
- *Fotónica* - quando temos dimensões menores que o comprimento de onda surgem fenómenos (cristais fotonicos, n negativo)
- *Biomedicina* - transporte de drogas, DNA sorting, bio sensores
- *Química* - o tamanho reduzido permite obter maior área superficial

### Superfície e Volume
- Pegando neste último ponto. Temos um cubo de átomos, com $n$ de cada lado.
    - O volume será $n^{3}$
    - A superfície é $2(4(n-1)^{2}-n(n-2))$
    - Os átomos do interior é a diferença dos 2 acima e dá $(n-2)^{3}$
- Podemos então facilmente fazer o gráfico de percentagem de átomos na superfície VS $n$:
![[porção superficie vs tamanho.png]]

**Temperatura de fusão**
- Átomos na superfície naturalmente são mais fáceis de mover
- Assim, $T_{m}$ indica a energia de binding num sólido. Ou seja, esta temperatura depende do tamanho do sólido

### 2D e menos
- No mundo macro, tudo é 3D
- Ao reduzir às escalas nano podemos criar coisas que basicamente têm menos dimensões:
    - plano quântico - 2D
    - nano fio - 1D
    - quantum dot - 0D

### Condução elétrica
- Para materiais macro a resistência elétrica é descrita por $R=\rho L/A$
- Para camadas finas de material (espessura $\lambda$) e temos algo do tipo:
![[resistividade vs espessura.png]]
- Para sistemas à escala nano temos o caso extremo de um sistema com camadas finas (em que temos uma camada com a espessura de 1 átomo):
![[contacto de fila de átomo.png]]
    - Neste caso a resistência é algo global e que não podemos dividir em partes menores

**Contacto de espessura quântica**
![[contacto 1d.png]]
- Imaginemos algo assim. 2 elementos de metal ligados por um nanofio/nanotubo. Temos basicamente uma ligação 1D com espessura $\sim \lambda_{F}$ 
- Podemos escrever:
$$I = \frac{e}{\Delta t}~~,~~ V = \frac{\Delta E}{e} ~~,~~R = \frac{V}{I}=\frac{\Delta E \Delta t}{e^{2}} $$
- Ora, a esta escala é evidente que temos comportamentos quânticos. Aplicando o princípio de incerteza $\Delta E\Delta t\ge \hbar/2$ temos:
$$R_{0}\ge \frac{\hbar}{2e^{2}}\simeq 12.9~\text{k}\Omega$$
ou seja, surge algo interessante a esta escala. Temos uma resistência mínima, $R_{0}$. Independentemente do comprimento do fio.
- Assim, temos um fenomeno que vimos várias vezes em MQ1: quantização. Por exemplo, um gráfico da condutância fica assim:
![[resistencia quantizada.png|320]]
- Esta quantização ocorre consoante acrescentamos 1 átomo à linha. Cada um acrescenta uma resistência $R_{0}$ à total.

**Ressonâncias Plasmónicas e Cor**
- Eletrões em nano partículas podem ser afetados por radiação EM. Podem oscilar, sendo considerados plasmões. Nisto, as oscilações absorvem as partes do espetro que as geram.
    - Ora, em nano particulas (NP) as oscilações estão quantizadas, oscilando em frequências específicas. Estas frequências depende do tamanho, forma e material das NP.
- Ou seja, _cor_. Se tivermos diferentes soluções com NPs de tamanhos diferentes teremos cores diferentes.
    - Maiores NP absorvem maiores comprimentos de onda.

# 2 - Técnicas de Nanofabricação
- As principais técnicas são **top-down** e **bottom-up**.
- Exemplos de top-down:
    - muitos tipos de litografia
- Exemplos de bottom-up:
    - montagem camada-a-camada
    - auto montagem molecular

## Top-Down
- Método mais tradicional
- Começamos com bloco grande de material e vamos removendo matéria até ficar só a estrutura que queremos
- Mais usado na física
- Usado para fazer microprocessadores, SSDs, MEMs, etc

## Bottom-Up
-  Criamos materiais usando síntese química. O processo é aleatório, mas pode ser ajustado com o contrlo de fatores ambientais.
- Menos caro do que top-down.
- Frequentemente escolhesse elementos a usar de modo que as estruturas se auto organizem

# 3 - Aplicações de Nanotecnologia
- Imensas:
![[aplicacoes nano.png]]
