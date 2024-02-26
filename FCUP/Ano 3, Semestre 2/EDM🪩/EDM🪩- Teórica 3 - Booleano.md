# 2 - Álgebra booleano
## 2.1 - Axiomas
- Consideremos a variável booleana $X$ (=0 ou =1)
- Podemos definir os axiomas básicos:
$$\begin{align*}
A_{1}&:X=0~se~X\neq1 &&;&A_{1}'&:X=1~se~X\neq0\\
A_{2}&:se~X=0~então~\overline X=1 &&;& A_{2}'&: se~X=1~então~\overline X=0\\
A_{3}&:0.0=0 &&;& A_{3}'&:1+1=1\\
A_{4}&:1.1=1 &&;& A_{4}'&:0+0=0\\
A_{5}&:0.1=1.0=0 &&;& A_{5}'&:1+0=0+1=1
\end{align*}$$
em que $.$ é o operador **AND** e $+$ é o operador **OR**. Poddemos considerar AND o "produto lógico" e OR a "soma lógica"
- AND faz-se antes de OR, mas podemos ter parentesis.
- Os axiomas com o apóstrofo são os **duais** dos sem apóstrofo.
    - Obtemos dualidade ao *trocar 1s com 0s e +s com .s*
    - Basicamente quer dizer que se uma expressão é verdade, o seu dual também.
- Para representar a **negação** podemos usar: $\overline X,X',/X$.

## 2.2 - Teoremas
- Usando os axiomas acima, podemos definir uma série de teoremas:
$$\small\begin{align*}T_{1}&:X+0=X &&;& T_{1}'&: X.1=X\\
T_{2}&:X+1=1 &&;& T_{2}'&: X.0=0\\
T_{3}&:X+X=X &&;& T_{3}'&: X.X=X\\
T_{4}&:(\overline{X})'=X\\
T_{5}&:X+X'=1 &&;& T_{5}'&: X.X'=0\\
T_{6}&:X+Y=Y+X &&;& T_{6}'&: X.Y=Y.X\\
T_{7}&:(X+Y)+Z=X+(Y+Z) &&;& T_{7}'&: (X.Y).Z=X.(Y.Z)\\
T_{8}&:X.Y+X.Z=X.(Y+Z) &&;& T_{8}'&: (X+Y).(X+Z)=X+(Y.Z)\\
T_{9}&:X+X.Y=X &&;& T_{9}'&: X.(X+Y)=X\\
T_{10}&:X.Y+X.\overline Y=X &&;& T_{10}'&: (X+Y).(X+\overline X)=X\\
T_{11}&:X.Y+\overline X.Z+Y.Z=X.Y+\overline Z&&;&T_{11}'&: (X+Y).(\overline X+Z).(Y+Z)=(X+Y).(\overline X+Z)
\end{align*}$$
Notas:
    - Os teorema 1 reflete que $0$ é o elemento neutro da soma lógica e o teorema 2 reflete que $1$ é o elemento absorvente da soma lógica. No produto lógico trocam (0 é absorvente e 1 neutro)
    - No teorema 5 temos a primeira vez em que operações lógicas *PARECEM* funcionar como teoria de conjuntos. O que temos neste teorema é como se fizessemos interseção ou reunião de um conjunto A e o seu complementar.
    - O ponto acima indicado sobre operações lógicas serem *quase* como teoria de conjuntos pode, em geral, ser usado para o raciocínio. Mas mais à frente veremos um exemplo concreto em que esta comparação pode causar confusão.
    - No teorema 9 inserimos parentesis no dual para garantir a mesma ordem de operações. Ou seja, em $T_{9}$ iríamos fazer $X.Y$ antes do OR. Ao passar para $T_{9}'$, ao colocar os parentesis, fazemos $X+Y$ antes do AND.

### 2.3.1 - Leis de Morgan
$$\overline{X.Y}=\overline X+\overline Y \quad \quad;\quad \quad \overline{X+Y}=\overline X.\overline Y$$

### 2.3.2 - EX de simplificação
- Consideremos a seguinte expressão:
$$(A.B+\overline{\overline A+B})+A.C$$
1. Apliquemos a lei de morgan ($\overline{X+Y}=\overline X.\overline Y$) na negação: $(A.B+A.\overline B)+A.C$
2. Colocamos $A$ em evidência: $A.(B+\overline B)+A.C$
3. Do teorema 5 temos $B+\overline B=1$ (reunião de conjunto com o complementar) e temos: $A.1+A.C$
4. Podemos novamente colocar $A$ em evidência: $A.(1+C)$
5. Temos que 1 é o elemento absorvente da soma logo ficamos com $A$
6. Assim: $(A.B+\overline{\overline A+B})+A.C=A$

## 2.4 - Funções Booleanas
- Este tipo de funções recebe variáveis booleanas e retorna um só valor: 1 ou 0
- Assim, uma função booleana de $N$ variáveis tem
    - Domínio consistindo nas $2^{N}$ combinações possíveis
    - Contradomínio $=\{0,1\}$

- Temos 3 formas de representar uma função booleana:
    1. Expressão algébrica - o que tivemos a fazer até agora
    2. Tabela de verdade - consiste em determinar todos os valores de $F$
    3. Circuito lógico - AND/OR gates

### 2.4.1 - Tabela de Verdade
Consiste nisto:
![[tabela vdd.png|450]]
- E torna-se útil um truque do secundário, para gerar todas as combinações possíveis sem perder nenhuma:
    - Começamos com a variável da direita (menos significativa) (Z acima) e colocamos: $0101010101\dots$ (de 1 em 1)
    - Passamos para a segunda variável (Y acima) e colocamos: $00110011\dots$ (de 2 em 2)
    - Passamos para a terceira variável (X acima) e colocamos: $000011110000\dots$ (de 4 em 4)
    - Sempre assim, com potências de base 2: de 8 em 8, de 16 em 16, etc
- Com o truque acima, podemos ainda ver que consoante descemos temos os números em base 2 ($000=0,001=1,010=2,011=3,\dots$)

- Podemos compactar a tabela. No caso acima, se $X=0,Y=0$ temos $F=1$ independentemente de $Z$, pelo que podemos só escrever $Z=x$ em que $x\in\{0,1\}$. Temos então a tabela de cima na forma:
![[tabela vdd reduzida.png|288]]

### 2.4.2 - Circuito Lógico
- Usando as portas lógicas / gates E,OU,NÃO temos:
![[circuito logico.png|500]]
em que o circuito representa a equação algébrica:
$$F(X,Y,Z)=Z.\overline X+X.Z+\overline Y.\overline Z$$
- Devemos notar algumas coisas:
    - Podemos ligar 3+ entradas a um AND ou OR: ![[and e or gate.png]]
    - Podemos colocar uma bola na entrada do AND/OR invés de estar a fazer uma porta NÃO (isto é apenas uma questão de sintese e organização):![[nao gate compactado.png]]
    
- Se colocarmos o NÃO na saída do AND / OR ficamos com as portas NAND / NOR:
![[nand e xor gates.png]]

de notar que colocar a bola na saída do AND (equivale a  $\overline{A.B}$) ou colocar nas 2 entradas (equivale a $\overline A.\overline B$) são coisas diferentes:
![[nota sobre nand e 2 naos.png]]
Isto é puramente consequência das leis de Morgan, que nos dizem que $\overline{A.B}=\overline A+\overline B$. Ou seja, uma porta NAND é equivalente a uma OR em que temos um NÃO nas 2 entradas:
![[nand leis morgan.png]]

### 2.4.3 Tabela de Verdade $\to$ Expressão Algébrica
- Antes de mais, notemos algumas denominações:
    - *Literal*: 1 variável (que btw pode ser representada por várias letras. $READY$ pode ser uma variável/literal)
    - *Termo de produto*: um produto de variáveis. EXs: $X~,~\overline Y~,~ X.\overline Y~,~X.X.X.\overline Y$
    - *Soma de produtos*: literalmente o que o nome diz. EXs: $X+Y.\overline Z+\overline Y$

#### Soma produtos / Soma Canónica ($+\times1$)
- Consideremos a tabela que vimos acima.
- Para cada ponto vamos definir um termo mínimo / *minterm* (este são produtos que apenas dá 1 para 1 linha --  não permite ambiguidade).
    - Para isto consideramos que: se $X=0$ usamos $\overline X$ no produto; se $X=1$ usamos $X$
    - Por exemplo, se $X=0,Y=0,Z=1$ temos o produto: $\overline{X}.\overline{Y}.Z$
    - Fazemos isto para cada linha.
- Temos:
![[soma prods tabela.png|450]]
(de notar que o número de linha começa em 0 porque, como já dito, cada combinação $XYZ$ representa um número binário)

- Ora, como queremos que a função booleana apenas "deixe passar" os casos verdadeiros, representamos a função como soma dos minterms com $F=1$.
- No caso acima isto resulta em: $F=\overline{X}.\overline{Y}.\overline{Z}+\overline{X}.\overline{Y}.Z+X.\overline{Y}.\overline{Z}+X.\overline{Y}.Z+X.Y.Z$
- Podemos ainda escrever isto como uma lista de minterms: $F=\sum_{(X,Y,Z)}(0,1,4,5,7)$
    - Obviamente, esta representação depende fortemente de como geramos as combinações AKA da ordem dos minterms 
- Esta solução $F$ resultaria num circuito com 1 porta OR (com 5 entradas) e 5 portas AND (com 3 entradas cada)-

#### Produto de Somas / Produto canónico ($\times+0$)
- Este método consiste em fazer o dual de cada minterm, obtendo-se os *maxterms* (um maxterm será um produto que apenas dá 0 em 1 linha). Temos:
![[prod somas tabela.png]]
- Sendo este o dual, invertemos o processo acima explicado:
    - Se $X=0$ usamos $X$ no produto; se $X=1$ usamos $\overline X$
    - Por exemplo, se $X=0,Y=0,Z=1$ temos o produto: $X+Y+\overline Z$
    - Fazemos isto para cada linha.

- Continuando a fazer tudo ao contrário, a função booleana será o produto dos maxterms em que $F=0$:
$F=(X+\overline{Y}+Z).(X+\overline Y+\overline{Z}).(\overline{X}+\overline{Y}+Z)$
- Ou podemos escrever isto como uma lista de maxterms: $F=\prod_{(X,Y,Z)}(2,3,6)$
- Aqui o circuito seria composto por 1 AND gate (de 3 entradas) e 3 OR gates (de 3 entradas cada) 

### 2.4.5 - Resumo de Representações
- Temos então:
    - Tabela de verdade - exaustivo, listar todas possibilidades
    - Lista de minterms - números das linhas em que $F=1$
    - Lista de maxterms - números das linhas em que $F=0$
    - Soma canónica - soma lógica de minterms em que $F=1$
    - Produto canónico - produto lógico de maxterms em que $F=0$
    - Circuito lógico - ligação de portas lógicas

### 2.4.6 - Exemplo Completo - Obter números positivos.
0. Consideramos um circuito que recebe um número $N$ de 3bits em C2. Queremos determinar o circuito de modo que ele nos dê $1$ quando $N>0$
1. Podemos dividir o número nos 3 bits: $N=N_{2}N_{1}N_{0}$, em que cada algarismo não passa de uma variável booleana
2. Podemos então fazer a tabela de verdade:
![[tabela vdd exemplo.png|400]]
3. Agora escolhemos um dos seguintes métodos que vimos atrás: produto de somas ou soma de produtos. Como temos três 1s e cinco 0s, escolhemos *soma de produtos* -> Escolhemos sempre a equação que nos dá menos termos! (Porque o objetivo final nesta UC é desenhar um circuito, portanto menos termos significa menos componentes logo um circuito mais simples).
    1. Temos $F=1$ nas linhas 1,2,3 logo temos $$F=\overline{N_{2}}.\overline{N_{1}}N_{0}+\overline{N_{2}}N_{1}\overline{N_{0}}+\overline{N_{2}}N_{1}N_{0}$$ (Podemos não escrever os pontos)
    2. Mas podemos simplificar isto:
        1. Metemos o $\overline{N_{2}}$ em evidência : $F=\overline{N_{2}}(\overline{N_{1}}N_{0}+N_{1}\overline{N_{0}}+N_{1}N_{0})$
        2. Metemos $N_{1}$ em evidência nos últimos 2 termos : $F=\overline{N_{2}}(\overline{N_{1}}N_{0}+N_{1}(\overline{N_{0}}+N_{0}))$
        3. Temos que $\overline{X}+X=1$ logo fica : $F=\overline{N_{2}}(\overline{N_{1}}N_{0}+N_{1})$
        4. Conforme o desenho abaixo temos: $\overline{N_{2}}(N_{1}+N_{0})$
![[espaço estados exemplo.png|450]]
> Ora, aqui surge a previamente referida confusão que podemos ter por pensar em operações lógicas como em teoria de conjuntos ou probabilidades.
> Na imagem acima temos algo que corresponderia a $A\cup B=A+B-A\cap B$ porque estávamos a "contar 2 vezes" a zona de interseção.
> Ora, esse tipo de pensamente falha em operações lógicas: $N_{0}+N_{1}=\overline{N_{1}}N_{0}+N_{1}$, porque ambas dão a "mesma resposta". Se formos a substituir $N_{1},N_{0}$ com todas as $2^2$ combinações possíveis iremos ver que de facto as operações dão sempre o mesmo. Isto vem da forma como o operador OR funciona, que não é bem como o operador Reunião de teoria de conjuntos.
> Outra coisa a apontar: Apesar de $N_{0}+N_{1}=\overline{N_{1}}N_{0}+N_{1}$, isto não implica que $N_{0}=\overline{N_{1}}N_{0}$. Apenas temos que as "respostas" das duas expressões são iguais.

4. Podemos finalmente representar o circuito que pretendemos:
![[circuito logico exemplo.png|525]]

### 2.4.7 - Mapas de Karnaugh
- Vejamos a "receita do bolo" para fazer estes mapas. Para isso, consideremos o mesmo exemplo do circuito para obter $N>0$ com 3 bits:
1. Começamos por desenhar o mapa em si. Ele terá tantas células como combinações possíveis (8 neste caso):
![[mapa karnaugh 1.png|300]]
2. Esta parte pode ser feita de inúmeras maneiras, mas o prof aconselhou vivamente fazer assim:
![[mapa karnaugh 2.png|350]]
    - Aqui, o que temos é que:
        - Na linha de cima toda temos $N_{2}=0$, na de baixo $N_{2}=1$
        - Na metade da esquerda do mapa temos $N_{1}=0$, na da direita $N_{1}=1$
        - Nas 2 colunas centrais temos $N_{0}=1$, nas restantes $N_{0}=0$
    - Invés da representação acima, normalmente só assinalaremos $N_{2}$ onde $N_{2}=1$ e igual para as restantes variáveis

3. Agora colocamos os valores de $F$ na tabela:
![[mapa karnaugh 3.png|350]]
    - Aqui o "desafio" é perceber que célula correponde a cada linha da tabela de verdade. Para isto há 1 regra:
        - as linhas correspondentes a células adjacentes (cima, baixo, esquerda e direita) só podem ter uma variável diferente. Ou seja, se uma certa célula corresponder a $100$ então uma célula adjacente nunca poderá corresponder a $011$ ou $010$, por exemplo.
    - Nos cantos (a laranja) temos o número da linha. Estas posições serão sempre as mesmas para esta configuração, só irão variar os valores de $F$ em si.

4. Fazer grupos. Neste caso, os melhores grupos a fazer seriam:
![[mapa karnaugh 4.png|350]]
    - Temos as seguintes regras:
        - Os grupos podem apenas tem números de células que sejam potências de base 2. Os grupos apenas podem ter as formas:![[mapa karnaugh 5.png|350]]
        - Podemos sobrepôr grupos (como vemos acima)
        - Temos que tentar sempre fazer os maiores grupos possíveis (acima, invés de fazer um grupo de 2 e um de 1, fazemos dois de 2)
    - Neste exemplo, de forma a melhor demonstrar o conceito, fizemos grupos de 1s e 0s. Na realidade apenas precisamos de fazer um destes: 1s se vamos usar soma de produtos ou 0s se vamos usar produto de somas

5. Tal como vimos atrás, como só temos três 1s, é mais vantajoso fazer soma de produtos. Assim temos:
    1. No grupo da esquerda (vermelho vivo) temos $N_{2}=0,N_{0}=1,N_{1}=x$. Podemos representar este grupo por $\overline{N_{2}}.N_{1}$. Tal como atrás, negamo a variável que é 0. As variáveis que não estão explicitamente definidas dentro do grupo são excluidas.
    2. No grupo da direita (vermelho claro) temos $N_{2}=0,N_{1}=1,N_{0}=x$. Temos então $\overline{N_{2}}.N_{1}$
    3. Temos então: $F=\overline{N_{2}}N_{1}+\overline{N_{2}}N_{0}=\overline{N_{2}}(N_{0}+N_{1})$, tal como obtivemos atrás com a tabela de verdades.
6. Pelas piadas, podemos fazer o produto de somas AKA grupos de 0s.
    1. Para o grupo vertical à esquerda temos $N_{2}=x,N_{0}=0,N_{0}=0$. Assim temos: $N_{1}+N_{0}$. Aqui negamos as variáveis que são 1. As variáveis que não estão explicitamente definidas dentro do grupo são excluidas.
    2. No grupo horizontal em baixo, temos $N_{2}=1,N_{1}=x,N_{0}=x$. Assim simplesmente temos $\overline{N}_{2}$
    3. Fica $F=(N_{1}+N_{0})\overline{N_{2}}$
