# INTRO
- O cérebro é o sistema com maior entropia conhecida
- Ora, a internet e os sistemas de comunicações atuais acabam por funcionar como um cérebro a grande escala, ou seja, têm muito alta entropia. Para isto funcionar é então precisa muita ENERGIA
- Por questões ambientais é então fundamental encontrar alterantivas viáveis

## Tipos de armazenamento
- Podemos classificar tipos de armazenamento de energia conforme 2 variáveis:
    1. Capacidade de carga
    2. Rapidez de carregar
![[Pasted image 20250409005408.png]]

*Condensadores*
- Em condensadores, temos 2 placas condutoras com 1 isolador no centro : controlamos o fluxo de eletões/carga no espaço. Mas não controlamos o fluxo no tempo, a carga e descarga são quase instantaneas

## Baterias
- No caso de uma bateria temos um cátodo e um anodo, em que há fluxo de iões entre eles, e em que o fluxo de eletrões ocorre pelo exterior
    - Neste caso são os iões que armazenam a energia

- Ou seja, para fazer uma bateria precisamos de uma reação que crie iões e liberte eletrões (de preferência num ratio de 1:1). Queremos ainda um alto potencial químico
- Ora, todas estas prioridades são mais fáceis de encontrar na *primeira coluna da TP*. Vejamos essa coluna:
    - H - usado em células de hidrogenio
    - Li - o clássico para baterias
    - Na - o que vamos ver nesta experiencia

**Problemas**
- Problemas de interface
- A DDP pode desgastar o dieletrico e formar dendrites. Isto estraga a funcionalidade
- Normalmente usamos eletrolitos liquidos, mas não têm a maior densidade de carga. Ou seja, queremos meter "mais metal" mas isso não escala bem. Precisamos na realidade de um material com maior densidade de carga

**Porque não Lítio**
- Queremos usar baterias para reduzir o consumo de combustíveis fósseis
- Ora, qualquer solução executada terá de o ser feita à grande escala AKA muitas baterias terão de ser feitas
- Infelizmente, a extração de lítio é ambientalmente má, logo para fazer muitas baterias iremos gastar muita energia, o que é contra produtivo!
ENTAOOOO nesta experiencia iremos usar SÓDIO. Ele é muito abundante e de fácil acesso. No entanto, tem maior raio atómico, logo menor densidade de carga

## Estrutura
- Temos:
    - Cátodo de Carbono
    - Anodo de Na
    - NASICON (NC) no centro que só permite a passagem de Na+
    - Eletrolito entre anodo e NC 

- **Limitações**
    - A capacidade máxima depende do volume de Na disponível (limite do anodo)
    - Estamos limitados pela eficiencia da reação anodo-catodo
    - Comportamento do NC ?

- Acerca do **Cátodo**:
    - Feito de Carbono
    - Este componente tem de ser bom condutor
    - Para isso, tem de ser concentrado, mas tem de ser poroso para as reações ocorrerem melhor
    - Vamos então usar:
        - Fibra comercial
        - Fibra comercial com tratamento termico
        - Fibra comercial com coating AC (activated carbon)

- *NOTA*: AC pode ser feito com qualquer coisa organica. Nós examinamos um feito de cascas de amendoim
- *NOTA 2*: A fibra comercial tem um polimero que ajuda a manter-se tudo junto. O tratamento termico remove-o. Assim, temos maior porosidade e potencial quimico

## Potenciostato
- Varia a tensão, mede a corrente e vice-versa
- É o sistema com as pontas todas que enchemos de água

## Espectrometria
- Medimos um traçado que permite determinar a resistividade e capacitância do sistema
![[Pasted image 20250409012829.png]]
- Tal como acima, podemos "fitar" os dados medidos a um circuito equivalente, mas temos que ter em conta a física!!!
- A resistência medida:
    - associada ao interface onde há transferência (e acumulação) de carga
    - resistência ao movimento das cargas
    - resistência iónica e eletrónica
- Como temos um interface líquido-poroso, devemos ter algo minimamente parecido ao **circuito de Randles** : o último (g) na figura acima, sendo que o bico em baixo deve ser mais soft e mais acima

## Medida Polarização Galvanica
- Variamos a tensão com corrente constante
- Ao carregar e descarregar, esperaríamos que houvesse plateau na mesma tensão (2.4V ?)
    - Mas na prática NÃO é o caso: a carga faz plateau acima e a descarga abaixo do esperado

## Ciclovoltometria (CV)
- Entre 2 valores de tensão, variamos a tensão e medimos a corrente. Fazemos varios ciclos de subir e descer entre os limites
- Para certos V vemos picos de I porque ocorre mais reação com essa tensão
- Há picos que só vemos na carga ou descarga porque são picos que geram reações não reversíveis
- Para ter uma boa resolução precisavamos de uma taxa de variação de tensão muito baixa, para a qual não temos tempo
    - Um traçado que teria muitos picos, fica muito suavizado

- Notemos que:
    - + taxa variação de tensão == + efeito resistivo : as reações são "forçadas" a acontecer e resistem
    - - taxa variação de tensão == + efeito capacitivo : reações acontecem com calma e acumula carga

# EXECUÇÃO
## Coating
- Este coating será colocado no cátodo
- Usamos:
    - HC (hard carbon) comercial
    - PVDF - um isolador. Parece estranho colocar algo isolador no cátodo (que tem de ser condutor), mas ele aqui funciona como binder / mantem tudo unido
    - SP (super P) (black carbon) - para equilibrar o efeito de isolador do PVDF
    - NNP - solvente, colocamos a olho para garantir uma consistencia boa
- Usamos 2 concentrações de massa: 80:10:10 e 60:20:20 (HC:PVDF:SP)

**Passos**
1. Meter PVDF
2. Meter NNP para ficar liquido
3. Medir SP e meter 
4. Mexer (não metemos NNP)
5. Medir HC e meter
6. Mexer e adicionar NNP (senão ficava demasiado seco)
7. Pincelar e meter uma gota
8. Forno a 100C

- A massa do HC é a mais difícil de controlar, então medimos esse primeiro e depois calculamos as outras de acordo. Em ambos os casos tentamos medir $0.1\text{g}$ de HC
- Medições:
$$\begin{align*}
80:10:10\quad\quad&\to\quad m_{\text{HC}}=0.1241\text{g} \quad;\quad m_{\text{SP}}=0.0154\text{g} \quad;\quad m_\text{PVDF}=0.0155 \text{g}\\
60:20:20\quad\quad&\to\quad m_{\text{HC}}=0.1029\text{g} \quad;\quad m_{\text{SP}}=0.0340\text{g} \quad;\quad m_\text{PVDF}=0.0342 \text{g}\\
\end{align*}$$

- Aparte, fizemos água salgada com uma concentração de sal de 35g/L.

## Potenciostato
Medimos
1. carga e descarga com pilha e HCCF
2. Espetrometria e CV com HCCF de 60/20 (feito por nós)
3. Espetrosmetria e CV com HCCF de 80/10 (feito por nós)

- Sobre pontas:
    - C - Counter (com C-sense incluido), fio de platina
    - R - Ref, tubo com redução Ag-AgCl em que há pequeno contacto com deposito em baixo
informação de como é feita a ligação em cada modo vê-se nas fotos.
## Wetability
Medimos:
1. CCF novo
2. CCF usado
3. HCCF novo (video)
4. HCCF usado (video)
5. PSCF 7 novo (video)
6. PSCF 8 usado (video)
(PSCF é HCCF em que o caoting foi feito com casca de amendoim invés de HC comercial)