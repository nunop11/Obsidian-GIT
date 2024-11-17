# FMR
**Setup**
- Infelizmente, a entrada USB do computador não funcionava e tivemos que inserior os valores de campo magnético manualmente. O computador apenas recolhida os dados do VNA 
- No laboratório, o analizador de VNA, os cabos e a amostra encontram-se numa estrutura metálica móvel
    - isto facilita a montagem de amostras
    - a estrutura e os fios apenas têm metais não magnéticos, obviamente
- O sample já se encontrava instalado quando chegamos
    - Temos um filme de 20nm de espessura de Ni-Fe (75/80% Ni, 20/25% Fe)
- Ligamos os fios assim: entrada 1 $\to$ amostra $\to$ entrada 2. Como não conseguimos medir a impedância do sistema fios+amostra, fazemos isto para medir como a impedância varia conforme o campo H.
- Invés de montar a amostra perpendicular à linha central do CPW, montamos a 45º
    - Isto é feito porque, para prender a amostra são necessarias estruturas tipo wedges. Ora, o campo MW é refletido nestas estruturas. Ao colocar a amostra a 45º estamos a reduzir as reflexões
    - Outra razão é que assim temos maior distância da amostra alinhada com os campos magnéticos

**Eletromagnet**
- Não usamos coils de Helmholtz como indicado no artigo. Invés disso, usamos eletromagnet, que será mais potente e mais preciso.**
- Foi preciso muito cuidado a colocar a amostra no eletromagnet. Existe uma zona de apenas ~1cm no centro em que temos um campo 100% uniforme.
- O iman e o seu power supply têm que receber água para arrefecimento
- O power supply vai até 100A $\to$ 1.5T

**VNA**
- O analizador de VNA demora ~45min a aquecer
- O analizador VNA gera e deteta sinal MW ao mesmo tempo
- Temos uma conexão específica entre o analizador e os cabos invés de BNC
    - Isto porque em BNC rodamos o cabo para conectar. Aqui rodamos a entrada.
    - Isso será melhor para reduzir problemas de ruído e interferência
- O setup e cabos usados permitem medir campo H em amostras com dimensões até $1\dot{A}$
- Os cabos pretos/azuis geram MW na micro escala
- Os cabos laranjas ligam-se aos nanopolos e geram MW na escala nano
    - Podem ser usados para testar nanodots e outras nanoestruturas
- Nesta atividade recolhemos os dados $S_{12}/S_{21}$, que representam a passagem da entrada 1 para a 2 ou ao contrário.
    - Dito isto, teoricamente seria a mesma coisa medir $S_{12}$ ou $S_{21}$. Na realidade, a saída 1 (not sure se era a 1 ou 2) está em piores condições, então medimos $S_{12}$
- Este analizador consegue gerar campos MW na gama $20\text{MHZ}-40\text{GHz}$

**Calibração**
- Tivemos que fazer tudo manualmente, o que não é ideal
- Irei falar de $I$. Esta é a corrente que nós colocamos no power supply. Cada corrente origina um campo H (com flutuações)
- Começamos com $I=0$. Vimos ruído no labV
- Subimos para $I=8\text{A}$. Vimos ruído, com 1 pico positivo no início da gama e 1 pico negativo no final. O positivo consiste em ruído, o negativo é uma ressonância.
- Fomos subindo o "campo" de 2 em 2 Amperes. Consoante aumentamos, o pico negativo foi desaparecendo no meio do ruído.
- Aos 20A perdemos o pico negativo.
- Assim, colocamos em 25A e calibramos. 

**Recolha de dados**
- Começamos em $I=0$ e fomos subindo o "campo" 1 em 1 Ampere até 16A.