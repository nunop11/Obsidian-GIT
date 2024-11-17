## Introdução
- Temos líquido ou sólido transparente sujeito a campo B. Passa feixe de luz polarizado, propagando-se paralelamente às linhas de campo.
- A onda sai do material com o seu plano de polarização rodado - Efeito de Faraday
- Neste efeito, podemos inverter a direção em que o campo roda se invertermos o sinal do campo ou se trocarmos o lado de onde o feixe é emitido (trocar o sentido de propagação)
- A relação que descreve o ângulo é (equação de Becquerel):
$$\phi=VBd$$
![[efeito faraday.png]]

- $V$ é a **constante de Verdet**. Esta depende do comprimento de onda e temperatura e está tabelada.
- Podemos ainda escrever:
$$V=\frac{\phi}{Bd}=- \frac{1}{2} \frac{e\lambda}{mc} \frac{dn}{d\lambda}$$
alguns valores tabelados:
![[valores constante verdet.png]]

- Materiais que têm grande dispersão cromática da luz ($dn/d\lambda$ elevado) terão um maior efeito de Faraday
- Na maioria dos materiais, o índice refração no vísivel diminui rapidamente consoante o comprimento de onda aumenta. Assim, $dn/d\lambda<0$. Assim, uma onda EM que se propague na direção de $\vec{B}$ irá rodar na direção *anti-horária*
    - No documento, no final, tem uma explicação de porquê que o sentido de rotação inverte ao inverte o campo ou o sentido de propagação. Basicamente relaciona-se como a foraça que o campo magnético resulta de um produto vetorial

- Tirando alguns paramagnets, a maioria dos materiais experimentalmente comportam-se de acordo com $\phi=VlB$. 
- Na gama $\lambda=600-700\text{nm}$ o índice de refração da maioria dos materiais desce cerca de $10^{-2}$. Em unidades MKS isto resulta em $\frac{dn}{d\lambda}\simeq 10^{5}$
    - Isto permite estimar $V$ (com a fórmula teórica que tem a derivada) como sendo por volta de 17.6 radianos por tesla-metro ou 0.06 minutos por gauss-cm
    - Tendo em conta os campos que conseguimos gerar e que facilmente temos alguns centimetros de amostra, o efeito de Faraday deverá facilmente ser observado.

## Equipamento
![[montagem t1o v4.png]]
### Samples
- Neste documento usou-se 3 amostras diferentes

### Polarização e Eletromagnet
- O Eletromagnet tem pontas específicas que servem para aumentar o campo que conseguimos obter
- O polarizador e analisador (não teremos polarizador porque vamos usar um lazer e então o feixe já começa polarizado) têm ajuste *course* e *fine* do ângulo. O ajuste fine tem que ser unlocked antes de mexer no course.
- A forma como um polarizador funciona:
    - temos cadeias de moléculas de hidrocarbono que são alinhadas no fabrico do polarizador através de stretching. O material com as cadeias alinhadas é mergulhado numa solução de iodo, o que faz com que seja condutivo na direção das cadeias
    - Ou seja, o campo é absorvido na direção das cadeias
    - Ora, a direção de polarização será independente do comprimento de onda, mas o grau de polarização pode não ser.
        - Ou seja, pode acontecer que o polarizador nunca anule a intensidade de um feixe (em certos comprimentos de onda, mesmo que tenhamos o ângulo perpendicular à polarização do feixe)

### Fontes de Luz
- No documento usaram uma lâmpada incandescente com filtros de cor
- Vamos usar um laser

### Magnet
- Controlado com uma fonte DC que lhe fornece corrente
- Neste documento, mediram a tensão fornecida

## Procedimento experimental
- Foi registado o gráfico intensidade da luz VS angulo do analisador para vários valores de campo.
- Usando isto iremos obter a relação $\Delta \phi$ vs B  usando a Lei de Malus e depois obter V.

### Deteção da Luz
- Usamos um fotodetetor para encontrar o mínimo de intensidade luminosa à saída do analisador
    - Temos: fototransistor, fotorresistor e fotodiodo.
    - O fototransistor e fotodiodo têm um comportamento ~linear ao longo de uma gama vasta de intensidade, pelo que são os melhores para medir intensidades e verificar a lei de Malus
    - No documento usaram um fotodíodo de Silica em modo fotovoltaico (sem bias) e é lida a tensão de saída com um multimetro. No multimetro, ajustar as definições de forma a minimizar flutuações ao custo da resolução. No lab vamos usar um osciloscópio.
- O fotodiodo está imbutido no suporte do analisador e está ligado a um cabo BNC. 
- Teoricamente, consoante rodamos o analisador a intensidade do feixe deverá com $\cos^{2}\theta$ (Lei de Malus), em que $\theta$ é o ângulo entre polarizador e analisador.

- Podemos rodar o analisador, medir o ângulo e tensão, fazer um gráfico e ajustar:
![[I_det vs ang.png]]
- Para podermos aplicar a lei de Malus é preciso que a resposta do foto detetor se mantenha linear. 
- Temos nesta imagem que a polarização nunca é total: $m_{1}\neq0$.

**Curva Malus sem Campo**
- Medimos esta curva
- Depois de medir isto, variamos o campo B e registamos a tensão do detetor em cada campo.
- Isto deverá permitir retirar o ângulo de rotação de Faraday.

### Aquisição de Dados
**Conhecer e adaptar ao detetor**
- Rodar o analisador e encontrar o mínimo e máximo de tensão, *sem campo*.

**Verificar a Lei de Malus**
- Continuamos sem campo
- Variar o ângulo do analisador em intervalos de ~10º ao longo de um range de 360º ou mais. A tensão em função do ângulo deverá ser do tipo $\cos^2$
    - Estimar erro médio devido a flutuações
- Fazer gráfico corrente do detetor vs ângulo
- Ajustar os dados para uma equação do tipo Formula de Malus: $$I=m_{1}-m_{2}\cos^{2}(\theta-m_{3})$$
em que:
    - $m_{1}$ é a corrente mínima do detetor
    - $m_{2}$ é a amplitude da variação de corrente do detetor
    - $m_{3}$ é o ângulo entre analisador-polarizador quando tempo o mínimo de corrente do detetor
- O ajuste melhora se limitarmos os pontos de ajuste a uma gama perto de um máximo ou mínimo
- Ao aplicar o campo, a curva toda desliza através da variação de $m_{3}$
    - Nunca mexer no polarizador
    - Ou seja, começamos por ter campo nulo e obtemos $m_{3}^{0}$. Depois temos um campo B1, obtendo-se $m_{3}^{1}$. O ângulo que a polarização rodou devido ao campo é $m_{3}^{1}-m_{3}^{0}$

**Calibração do magnet**
- Medir o campo com o gaussmeter (sem a amostra), com o plano do probe perpendicular ao campo
- Fazer curva de histerese estável, para corrente/campo positivo e negativo
- **NOTA** : ao inverter o campo, meter a fonte de tensão a zero e desligada. Trocar os fios e voltar a ligar.

**Loop de histerese**
- Remover magnetismo residual do magnet:
    - Subir a tensão da fonte de tensão da fonte de alimentação do magnet para a tensão máxima que planeamos usar na experiência (50V por exemplo).
    - Descer a tensão de volta a zero, desligar a fonte e reverter polaridade.
    - Subir a tensão novamente (-40V por exemplo), voltar a zero e desligar
    - Repetir agora até 30V
    - Repetir isto na sequencia: 50, -40, 30, -20, 10, -5

- Calibrar o magnet, medindo uma curva $B(V)$. Medir o campo em várias tensões na variação: $0\to50$ e depois $50\to0\to-50$ e no final $-50\to0$. 
    - Se mantivermos esta curva de histerese, os dados que medirmos nesta série serão válidos.
    - Manter a mesma curva significa, manter o mesmo máximo e mínimo. 

**Medir dados de Faraday**
- Fazer como indicado abaixo. Fazer em 1 dos ramos da curva de histerese ($+$ para a porção positiva, $-$ para a porção negativa)
- Medir $B(V)$ e depois fazer gráfico $\Delta \phi(B)$ para $B$ a aumentar e a diminuir

**Rotação de Polarização**
- Repetir isto para cada amostra, para cada comprimento de onda e para 3+ valores de campo (além de zero campo)
1. Meter a corrente de campo que queremos. Fazer positivo e negativo para ter mais dados. Registar o ângulo de intensidade mínima medida a olho
2. Passar a usar o foto detetor. Medir a voltagem do detetor e o ângulo.
    1. Medir vários ângulos na gama em torno de onde vimos o mínimo a olho, ficando numa região estreita. NÃO procurar o mínimo
    2. Encontrar o mínimo por ajuste
    3. Medir pontos num intervalo de $\pm$ 45º em torno do mínimo em intervalos de 10º, isso deverá dar um bom conjunto de dados.
    4. Se tiramos os dados em torno de um mínimo temos $m_{1}-m_{2}\cos^{2}(m_{0}-m_{3})$
3. Outro método:
    1. fazer medições e fazer a curva de zero field
    2. meter o analisador no ângulo que dá intensidade mínima
    3. percorrer valores de campo e ver variação da intensidade que passa
    4. usando os dados e as curvas, analizar??
isto são 3 métodos diferentes, em que no 1 e no 3 fazemos tudo a olho (?)

## Análise
### Constante de Verdet
- Para todas as amostras / comprimentos de onda analisados, fazer gráfico $\Delta \phi(B)$. 
- Usar ajuste para obter a constante de Verdet e calcular respetivo erro
- Usar os 3 métodos e comparar

### Comparar dispersão de Faraday com previsão da fórmula de Cauchy
- Se houverem dados de dispersão (refração), ajustar $$n=A+ \frac{B}{\lambda^{2}}$$
- Derivar para obter $dn/d\lambda$
- Relacionar com Verdet

# Análise
- Fizemos ajuste $V(\theta)$ do tipo:
$$V = m_{1} - m_{2}\cos^{2}(\theta-m_{3})$$
e fazemos a derivada:
$$\frac{dV}{d\theta}= 2m_{2}\cos(\theta-m_{3})\sin(\theta-m_{3})$$
e o mínimo estará em:
$$\frac{dV}{d\theta}=0~~\to~~ \cos(\theta-m_{3})\sin(\theta-m_{3})=0$$
ou seja:
$$\theta=\frac{\pi}{2}+m_{3}~~~~;~~~~\theta=\pi+m_{3}$$
