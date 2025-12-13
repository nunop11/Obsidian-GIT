- Notas tiradas de https://kalmanfilter.net/

# Overview
## O que é?
- Um filtro de Kalman é um algoritmo que permite estimar/prever o estado de um sistema, quando temos incertezas. É muito usado em controlo, navegação e seguimento de targets
- Este site pretende introduzir o filtro de forma prática e simples. O objetivo é explicar a intuição de como funciona

## Porquê?
- Vamos ver um exemplo para entender porque usamos isto
- Consideremos um radar que deteta e segue a posição de aviões
![[radar e avioes.png]]
- Modelizando isto:
    - O avião é o *sistema*
    - Queremos estimar a *posição* do sistema, logo a posição É o **estado** do sistema
- O radar envia um feixe na direção do avião e assim deteta a sua posição
- Mas, para isso funcionar, o radar precisa de saber a direção do avião. Mas para isso, é preciso *prever* onde ele estará no próximo instante!
    - Se isto correr mal perdemos conta de onde está o avião e não o conseguimos seguir

**Dinâmico**
- Assim, precisamos de conhecer o *movimento* do avião. Precisamos de um modelo que descreva o movimento do avião ao longo do tempo: um **modelo dinâmico**
![[radar e avioes 1d.png]]
- Representemos o estado do avião como a distância $x$ para o radar
- O radar envia um feixe EM para o avião, ele é refletido e estimamos a distância a que ele se encontra através do tempo de voo do feixe. Mas conseguimos ainda estimar a **velocidade**

**Contas**
- Consideremos que no instante $t_{0}$ o radar mede a distância e velocidade do avião com alta precisão e exatidão. Medimos $x=10000\text{m}$ e $v=200\text{m/s}$. Assim, estamos no estado:
$$x_{t_{0}}=10000\text{m}$$
- Precisamos então de prever o próximo estado, num certo instante $t_{1}=t_{0}+\Delta t$. $\Delta t$ é o intervalo que escolhemos para revisitar o alvo ou **intervalo de sampling**.
- Assumindo que o avião se mantem a velocidade constante, definimos o *modelo dinâmico de velocidade*:
$$\begin{align*}
\Delta x&= v \Delta t\\
x_{t_{1}}&= x_{t_{0}}+\Delta x=x_{t_{0}}+v\Delta t
\end{align*}$$
que, para um tempo de sampling de $5\text{s}$ nos dá: $x_{t_{1}}=11000\text{m}$

- Fizemos um algoritmo simples, com assumptions básicas:
![[previsao de estado ideia geral.png]]

**Vida real**
- Na realidade, as medições do radar têm sempre incerteza e não são perfeitamente precisas. Temos ruído e aleatoriedade. 
    - A variação aleatória nas medições chama-se *ruído de medição*!

- Então surge a necessidade de saber **"quão certa é esta medição?"** Ou seja, precisamos de um algoritmo que nos dê uma estimativa assim como o quão reliable/consistente/certa ela é.
- Além disso, temos que aceitar que o o modelo dinâmico é fraco: ao assumir que o avião vai sempre à mesma velocidade, estamos a ignorar fatores externos como vento, que irão introduzir erros na estimativa.
    - A estes efeitos aleatórios chamamos de *ruído de processo*!

- Além de saber a certeza de uma estiamtiva, queremos compreender o *nível de confiança* da previsão.

**Kalman**
- Um filtro de Kalman é um algoritmo de estimar estados, que permite estimar:
    - O estado atual
    - A previsão do próximo estado
    - Uma medição da **incerteza**
- Além disso, este algoritmo é *óptimo* e minimiza a incerteza. 
- Por todas estas razões, ele é muito utilizado atualmente
![[previsao de estado ideia melhor feita.png]]

# Background
## Estado escondido
- Usamos este termo para referir o *estado do sistema*, que não conhecessemos e normalmente não podemos medir nem observar diretamente
- Normalmente, precisamos de usar várias medições para estimar o estado. 
    - Para isso podemos usar uma série de métodos matemáticos. Como o estado costuma ser uma certa variável medível, é comum fazer $n$ medições e considerar a sua média como a estimativa do estado

**Exemplo**
- Consideremos que uma certa pessoa está a estudar o seu peso. A pessoa é o sistema, enquanto que o peso é o estado.
- Consideremos que temos 5 medições do seu peso: $79.8\text{kg},80\text{kg},80.1\text{kg},79.8\text{kg},80.2\text{kg}$
    - Os valores diferentes correspondem à aleatoriedade do erro de medição das balanças. Assumimos que os valores foram medidos "seguidos", ou seja, não temos aqui nenhuma evolução temporal
- Podemos calcular a média: $$W=\frac{1}{N}\sum\limits_{n=1}^{N}W_{n}=\frac{79.8+80+80.1+79.8+80.2}{5}=79.98\text{kg}$$
- Consideramos que o estado do sistema é $W=79.98\text{kg}$. Mas notemos que existe uma incerteza, já que não medimos **todos** os possíveis valores: se fossemos medir mais uma vez, provavelmente iríamos obter um valor que não medimos antes.

## Variância e Desvio Padrão
- A **variância** $\sigma^{2}$ mede o quão espalhados os dados estão relativamente à sua média
- O **desvio padrão** $\sigma$ é a raiz quadrada da variância lol

**EXEMPLO**
- Consideremos 2 equipas de basket, em que queremos comparar as alturas dos jogadores. Temos
![[medicoes altura.png]]
- OK, vemos que as médias são iguais. Mas isso não quer dizer que as alturas das equipas são iguais: vamos avaliar as variâncias
- Começamos por calcular o desvio de cada altura à média (da sua equipa - queremos apenas ver as variâncias dentro das equipas):
$$x_{n}-\mu=x_{n}-1.914\text{m}$$
![[variacoes para altura media.png]]

- Para tornar todos os valores positivos e o set mais "uniforme" fazemos:
$$(x_{n}-\mu)^{2}=(x_{n}-1.914\text{m})^{2}$$
![[desvios quadraticos altura.png]]

- Assim, podemos calcular a variância de cada equipa ao somar os desvios quadrados:
$$\sigma^{2}=\frac{1}{N}\sum\limits_{n=1}^{N}(x_{n}-\mu)^{2}$$
e temos para as equipas A e B:
$$\sigma_{A}^{2}=0.014\text{m}^{2} \quad \quad;\quad \quad \sigma_{B}^{2}=0.0013\text{m}^{2}$$
- Ou seja, as alturas da equipa A são mais variadas. De um ponto de vista prático, isto quer dizer que teremos jogadores para diferentes posições, na equipa B não temos tanta versatilidade.
- Podemos, claro, calcular os desvios padrões:
$$\sigma_{A}=0.12\text{m} \quad \quad; \quad \quad \sigma_{B}=0.036\text{m}$$

### Fórmula
- Apesar do que usamos acima ser uma formula OK para samples pequenos, a forma mais adequada é:
$$\sigma^{2}=\frac{1}{N-1}\sum\limits_{n=1}^{N}(x_{n}-\mu)^{2}$$
em que o termo $\frac{1}{N-1}$ é a *correlação de Bessel*

## Distribuição Normal
$$f(x;\mu,\sigma^{2})=\frac{1}{\sqrt{2\pi \sigma^{2}}}e^{-\frac{(x-\mu)^{2}}{2\sigma^{2}}}$$
- A distribuição normal é descrita por esta equação e muitos processos naturais seguem-na
- Esta função descreve a PDF (função de densidade de probabilidade) da distribuição normal
- Temos que a média "move" a curva e uma maior variânvia "alarga" o pico:
![[distribuicao normal.png]]

### Variação
- Podemos definir 4 ranges importantes:
    - Dentro de $\mu\pm\sigma$ temos $68.26\%$ das possibilidades
    - Dentro de $\mu\pm2\sigma$ temos $95.44\%$ das possibilidades
    - Dentro de $\mu\pm3\sigma$ temos $99.74\%$ das possibilidades
![[regioes sigma dist normal.png]]

### Erro
- Esta distribuição é importante porque normalmente consideramos que erros de medição seguem uma distribuição normal. 
- É precisamente isso que fazemos no filtro de Kalman!

## Variáveis aleatórias (VAs)
- Uma VA descreve o estado escondido do sistema. Esta variável representa uma série de valores *possíveis* de uma certa experiência/medição
- VAs podem ser contínuas ou discretas
- Normalmente consideramos estas varíaveis como sendo normais, pelo que são caraterizadas por $\mu_{X},\sigma_{X}^{2}$

## Estimativa, exatidão, precisão
- Uma **estimativa** consiste em tentar determinar o estado escondido do sistema. 
    - Por exemplo, podemos estimar a posição de algo usando sensores. 
    - Podemos melhorar a estimativa ao usar mais e melhores sensores, assim como usar algoritmos de tracking mais avançados
    - Consideramos que **todos** os parâmetros medidos ou calculados são estimativas!!!
- A **exatidão** indica o quão perto a medição está do valor real (que não conhecemos)
- A **precisão** mede quanto uma série de medições variam
    - Notemos que um sistema de alta-precisão terá **menor incerteza**. No caso de baixa-precisão temos mais incerteza, claro
![[exatidao e precisao.png]]

**Bias**
- No caso de sistemas com alguma precisão e baixa exatidão dizemos que existe um **bias**. Isto porque quando temos uma baixa exatidão, então temos algum erro sistemático a causá-lo
- Em tudo neste tutorial assumimos que NÃO HÁ BIAS

 **Melhorar**
 - Podemos melhorar a incerteza e variância ao utilizar médias ou smoothing. 

# Filtro $\alpha-\beta-\gamma$
## EX1 - Pesar ouro
- Este exemplo consiste em estimar o estado de um sistema estático. Um sistema estático *não muda de estado* por um intervalo considerável.
    - Exemplos de sistemas estáticos: um edificio, em que o estado é a sua altura 
- Neste exemplo, queremos estimar o peso de uma barra de ouro
- Para esta tarefa, temos balanças que medem o peso sem bias, mas continuamos a ter o ruído aleatório nas medições
- Consideramos que o sistema é a barra de ouro e o estado é o seu peso.

**Medições**
- A melhor aproach será, claro, fazer várias medições e calcular a sua média:
![[medicos ao longo do tempo.png]]
- Antes de continuar, consideremos isto
![[notacao kalman.png]]
ou seja: $\hat{x}_{i,j}$ é a previsão de $x$ no instante $i$, que foi feita no instante $j$,
- Temos então
$$\begin{align*}
\hat{x}_{n,n}=\frac{1}{n}\sum\limits_{i=1}^{n}z_{i}
\end{align*}$$
- Claro, como temos um sistema **estático** temos que $\hat{x}_{n+1,n}=\hat{x}_{n,n}$ porque $x$ é constante

**História**
- A fórmula d e$\hat{x}_{n,n}$ como uma média é correta e direta, mas não é ideal para sistemas mais completos. A média será apenas uma forma de remover ruído.
- Queremos que a nossa previsão em $n$ tenha em conta as previsões já feitas em todos os instantes anteriores
    - Notemos também que para atualizar a estimativa em cada instante, precisamos de muitas medições e uma nova média em cada instante.

- Assim, será mais prático guardar a última estimativa $\hat{x}_{n-1,n-1}$ e atualizá-mo-la *após cada medição*
- Podemos usar este algoritmo:
![[previsoes peso barra de ouro.png]]
- Podemos escrever
$$\begin{align*}
\hat{x}_{n,n}&= \frac{1}{n}\sum\limits_{i=1}^{n}z_{i}\\
&= \frac{1}{n} \left[\sum\limits_{i=1}^{n-1}z_{i}+z_{n}\right]\\
&= \frac{1}{n}\sum\limits_{i=1}^{n-1}z_{i}+\frac{z_{n}}{n}\\
\\
&= \frac{1}{n}\frac{n-1}{n-1}\sum\limits_{i=1}^{n-1}z_{i}+\frac{z_{n}}{n}\\
&= \frac{n-1}{n}\hat{x}_{n-1,n-1} + \frac{z_{n}}{n}\\
&= \hat{x}_{n-1,n-1}+ \frac{1}{n}(z_{n}-\hat{x}_{n-1,n-1})
\end{align*}$$
- Queremos agora determinar uma forma de estimar $\hat{x}_{n,n-1}$. Ou seja, queremos extrapolar $\hat{x}_{n-1,n-1}$ para o instante $n$.
- Como estamos num exemplo estático isto é mais simples: consideramos que $\hat{x}_{n,n-1}=\hat{x}_{n-1,n-1}$ porque $x_{n}=x_{n-1}=x$. Fica então:
$$\hat{x}_{n,n}=\hat{x}_{n,n-1}+ \frac{1}{n}(z_{n}-\hat{x}_{n,n-1})$$
- Isto é a **Equação de Atualização de Estado** do filtro de Kalman, que podemos esquematizar na forma
![[esquema equação de atualização estado.png]]
- O "Factor" que no nosso exemplo é $1/n$, normalmente é $K_{n}$ - **ganho de Kalman**. O $n$ em índice indica que este ganho pode ser variável
- Mas como não estamos a ver Kalman "a sério" podemos representar este fator com um $\alpha$:
$$\hat{x}_{n,n}=\hat{x}_{n,n-1}+\alpha_{n}(z_{n}-\hat{x}_{n,n-1})$$
- O termo entre parenteses introduz no modelo a informação nova que adquirimos ao fazer uma medição. Com este, podemos corrigir erros das estimativas
    - Por exemplo, no nosso exemplo temos $\alpha_{n}=\frac{1}{n}$ que diminui com o tempo. No início, temos pouca informação porque temos pouca informação LOGO temos um ganho maior - cada medição vale mais. No final, já temos muita informação e temos um ganho baixo para o sistema ser mais estável.

### Algoritmo
- Antes de começar a utilizar este modelo, temos que introduzir uma **estimativa inicial / initial guess**. Esta pode ser muito fraca, mas convém estar na região do valor correto
- Temos então um algoritmo assim:
![[algoritmo filtro alfa.png]]
- Resumo:
    - **Passo 0** - inicializamos o sistema, definindo parâmetros importantes
    - **Passo 1** - medir um valor novo
    - **Passo 2** - calcular o ganho $\alpha_{n}$ e estimar o estado ATUAL com a equação de atualização de estado
    - **Passo 3** - calcular  a previsão para o estado SEGUINTE usando o modelo dinâmico

### Exemplo numérico
Vamos ver então algumas iteração deste algoritmo:
**Passo 0 - Inicialização**
- Começamos por definir a estimativa inicial do peso da barra de ouro: $\hat{x}_{0,0}=1000\text{g}$
*Estimativa*
- Como não esperamos que o valor mude e como não temos medições, simplesmente consideramos: $\hat{x}_{1,0}=\hat{x}_{0,0}=1000\text{g}$

**1ª iteração**
*Passo 1* 
- Medimos $z_{1}=996\text{g}$
*Passo 2* 
- Calculamos o ganho $\alpha_{1}=\frac{1}{1}=1$
- Prevemos o estado atual: $\hat{x}_{1,1}=\hat{x}_{1,0}+\alpha_{1}(z_{1}-\hat{x}_{1,0})=1000+1(996-1000)=996\text{g}$
*Passo 3*
- O modelo dinâmico é ESTÁTICO logo neste passo não temos nenhum modelo para aplicar: consideramos sempre a estimativa do próximo estado é igual à do atual: $\hat{x}_{2,1}=\hat{x}_{1,1}=996\text{g}$

**2ª iteração**
- No passo 3 da iteração anterior previmos o próximo instante $\hat{x}_{2,1}$. Ora como agora estamos no instante 2, isto é a previsão feita no instante anterior: $\hat{x}_{n,n-1}$
*Passo 1*
- Medimos $z_{2}=994\text{g}$
*Passo 2*
- Agora o ganho é $\alpha_{2}=\frac{1}{2}$
- A estimativa do estado atual é $\hat{x}_{2,2}=\hat{x}_{2,1}+\alpha_{2}(z_{2}-\hat{x}_{2,1})=995\text{g}$
*Passo 3*
- O sistema é estático: $\hat{x}_{3,2}=\hat{x}_{2,2}=995\text{g}$

**3ª Iteração**
$$\begin{align*}
\alpha_{3}&= \frac{1}{3}\\
z_{3}= 1021~~\to~~ \hat{x}_{3,3}&= \hat{x}_{3,2}+ \alpha_{3}(z_{3}-\hat{x}_{3,2})\\
&= 995+\frac{1}{3}(1021-995)=1003.67\text{g}\\
\hat{x}_{4,3}&= \hat{x}_{3,3}=1003.67\text{g}
\end{align*}$$

**4ª iteração**
$$\begin{align*}
\alpha_{4}&= \frac{1}{4}\\
z_{4}= 1000~~\to~~ \hat{x}_{4,4}&= \hat{x}_{4,3}+ \alpha_{4}(z_{4}-\hat{x}_{4,3})\\
&= 1003.67+\frac{1}{4}(1000-1003.67)=1002.75\text{g}\\
\hat{x}_{5,4}&= \hat{x}_{4,4}=1002.75\text{g}
\end{align*}$$

**5ª iteração**
$$\begin{align*}
\alpha_{5}&= \frac{1}{5}\\
z_{5}= 1002~~\to~~ \hat{x}_{5,5}&= \hat{x}_{5,4}+ \alpha_{5}(z_{5}-\hat{x}_{5,4})\\
&= 1002.75+\frac{1}{5}(1002-1002.75)=1002.6\text{g}\\
\hat{x}_{6,5}&= \hat{x}_{5,5}=1002.6\text{g}
\end{align*}$$

- E isto continua no exemplo no site até à 10ª iteração, tendo-se:
$$\begin{align*}
z_{6}&= 1010\text{g}\\
z_{7}&= 983\text{g}\\
z_{8}&= 971\text{g}\\
z_{9}&= 993\text{g}\\
z_{10}&= 1023\text{g}
\end{align*}$$
- Em resumo temos:
![[medicoes filtro alfa.png]]
![[resultado filtro alfa.png]]

### Quantas medições?
- Este número depende da precisão desejada. No livro a resposta é vista num apêndice :(

### Filtro alpha, sistema estacionário
$$\boxed{\hat{x}_{n,n}=\hat{x}_{n,n-1}+ \alpha_{n}(z_{n}- \hat{x}_{n,n-1})}$$

## Exemplo 2 - avião a velocidade constante
- Consideremos agora que estamos a medir a distância de um radar a um avião a mover-se em 1D a velocidade constante
- Para fazer este tipo de tarefa usamos um filtro $\alpha-\beta$
- Definimos $x_{n}$ como sendo a distância real do avião em $n$
- O problema é parecido ao que tínhamos antes, mas agora precisamos de estimar a velocidade!

### Estimar velocidade
- Temos: 
$$\dot{x}=v=\frac{dx}{dt}\approx \frac{\Delta x}{\Delta  t}$$
- Assim, considerando equações de movimento básicas temos:
$$x_{n+1}=x_{n}+\Delta t \dot{x}_{n}$$
e como temos velocidade constante então
$$\dot{x}_{n+1}=\dot{x}_{n}$$
- Este sistema de equações é a **equação de extrapolação de estado** ou  **equação de transição** ou **equação de previsão** ou **equação do modelo dinâmico** é uma das equações de Kalman
- No exemplo anterior usamos esta equação, considerando a "velocidade de variação da massa" nula

### Filtro $\alpha-\beta$
- Consideremos que o radar tem um tempo de sampling $\Delta t=5\text{s}$ e que $\hat{x}_{n-1,n-1}=30000\text{m}$ (distância do avião em $n-1$, estimada em $n-1$) e que $\hat{\dot{x}}_{n-1,n-1}=40\text{m/s}$ 
- Podemos aplicar a equação de extrapolação:
$$\begin{align*}
\hat{x}_{n,n-1}&= \hat{x}_{n-1,n-1}+\Delta t \hat{\dot{x}}_{n-1,n-1}\\
&= 30000+5\times40=30200\text{m}\\
\hat{\dot{x}}_{n,n-1}&= \hat{\dot{x}}_{n-1,n-1}=40\text{m/s}
\end{align*}$$

- Consideremos agora que se mediu $z_{n}=30110\text{m}$. Existe uma diferença de $90\text{m}$ que temos que compensar. Existem 2 possibilidades:
    - O radar tem baixa precisão
    - A velocidade do avião mudou. Neste caso, a velocidade seria: $\frac{30110-30000}{5}=22\text{m/s}$

- Para ter isto em conta, alteramos a equação de atualização de estado para a velocidade:
$$\hat{\dot{x}}_{n,n}=\hat{\dot{x}}_{n,n-1}+ \beta \frac{z_{n}-\hat{x}_{n,n-1}}{\Delta t}$$
notemos que a fração é a velocidade que teríamos de ter no intervalo $\Delta t$ para explicar o valor $z_{n}$ medido, como vimos acima ao calcular os $22\text{m/s}$

#### Beta
- Este parâmetro é definido conforme a precisão do radar/sensor

**Alta precisão**
- Consideremos que a precisão do radar em $1\sigma$ é $20\text{m}$. Neste caso, o "erro" de $90\text{m}$ é quase de certeza causado por variação da velocidade. Assim atribuímos um valor alto a beta como $\beta=0.9$
- Neste caso temos
$$\begin{align*}
\dot{x}_{n,n}&= \hat{\dot{x}}_{n,n-1}+0.9 \frac{z_{n}-\hat{x}_{n,n-1}}{\Delta t}\\
&= 40+0.9 \frac{30110-30200}{5}=23.8\text{m/s}
\end{align*}$$

**Baixa precisão**
- Consideremos que a precisão em $1\sigma$ é de $150\text{m}$. Assim, o "erro" pode perfeitamente ser causado por flutuações naturais de medição do sensor. Assim escolhemos um valor baixo para beta como $\beta=0.1$
- Ficamos com
$$\begin{align*}
\dot{x}_{n,n}&= \hat{\dot{x}}_{n,n-1}+0.1 \frac{z_{n}-\hat{x}_{n,n-1}}{\Delta t}\\
&= 40+0.1 \frac{30110-30200}{5}=38.2\text{m/s}
\end{align*}$$

- Podemos ver que isto funciona como o $\alpha$ acima: temos um ganho, que faz com que uma nova medição tenha um maior ou menor efeito na nossa estimativa.

#### Alfa
- A equação de atualização de estado é igual:
$$\hat{x}_{n,n}=\hat{x}_{n,n-1}+\alpha(z_{n}- \hat{x}_{n,n-1})$$
- Notemos que agora $\alpha$ **é constante**, não varia com $n$.
- Tal como para $\beta$, escolhemos o valor de $\alpha$ conforme a precisão do radar/sensor.
    - Se o sensor for de alta-precisão, escolhemos $\alpha$ perto de 1 e cada medição tem maior peso
    - Se o sensor tiver baixa-precisão, escolhemos $\alpha$ perto de 0 e as medições novas valem menos para desviar menos a estimativa

### Filtro $\alpha-\beta$, velocidade constante
$$\boxed{\begin{align*}
\hat{x}_{n,n}&= \hat{x}_{n,n-1}+\alpha(z_{n}-\hat{x}_{n,n-1})\\
\hat{\dot{x}}_{n,n}&= \hat{\dot{x}}_{n,n-1}+ \beta \left(\frac{z_{n}- \hat{x}_{n,n,-1}}{\Delta t}\right)
\end{align*}}$$
- NOTA: em alguma literatura, este filtro chama-se **filtro g-h**

### Algoritmo
![[algoritmo filtro ab.png]]
- Vemos que é bastante parecido ao exemplo anteriror e agora nem temos que calcular $\alpha,\beta$ em cada iteração
- Vejamos agora um exemplo com um radar de baixa precisão, com um avião lento. Isto foi escolhido para melhor representação gráfica
- Tendo em conta esta precisão temos $$\alpha=0.2 \quad;\quad \beta =0.1$$

**0ª iteração**
*Passo 0*
- Definimos $\hat{x}_{0,0}=30000\text{m}~,~\hat{\dot{x}}_{0,0}=40\text{m/s}$
(A inicialização e escolha de valores iniciais são todo um problema que vamos ignorar por agora)
*Passo 3*
- Temos
$$\begin{cases}
\hat{x}_{1,0}=\hat{x}_{0,0}+\Delta t \dot{x}_{0,0} \\
\hat{\dot{x}}_{1,0}=\hat{\dot{x}}_{0,0}
\end{cases}=\begin{cases}
\hat{x}_{1,0}=30000+5\times40=30200\text{m} \\
\hat{\dot{x}}_{1,0}=40 \text{m/s}
\end{cases}$$

**1ª iteração**
*Passo 1*
- Medimos a distância do avião:
$$z_{1}=30171\text{m}$$
*Passo 2*
- Estimamos o estado, usando a equação de atualização de estado:
$$\begin{cases}
\hat{x}_{1,1}=\hat{x}_{1,0}+\alpha (z_{1}-\hat{x}_{1,0}) \\
\hat{\dot{x}}_{1,1}=\hat{\dot{x}}_{1,0}+\beta \frac{z_{1}-\hat{x}_{1,0}}{\Delta t}
\end{cases}=\begin{cases}
\hat{x}_{1,1}=30200+0.2\times(30171-30200)=30194.2\text{m} \\
\hat{\dot{x}}_{1,1}=40+0.1 \frac{30171-30200}{5}=39.42\text{m/s}
\end{cases}$$
*Passo 3*
- Usamos a equação de extrapolação:
$$\begin{cases}
\hat{x}_{2,1}=\hat{x}_{1,1}+\Delta t \hat{\dot{x}}_{1,1} \\
\hat{\dot{x}}_{2,1}=\hat{\dot{x}}_{1,1}
\end{cases}=\begin{cases}
\hat{x}_{2,1}=30194.2+5\times39.42=30391.3\text{m} \\
\hat{\dot{x}}_{2,1}=39.42\text{m/s}
\end{cases}$$

**2ª iteração**
*Passo 1*
$$z_{2}=30353\text{m}$$
*Passo 2*
$$\begin{cases}
\hat{x}_{2,2}=\hat{x}_{2,1}+\alpha (z_{2}-\hat{x}_{2,1}) \\
\hat{\dot{x}}_{2,2}=\hat{\dot{x}}_{2,1}+\beta \frac{z_{2}-\hat{x}_{2,1}}{\Delta t}
\end{cases}=\begin{cases}
\hat{x}_{1,1}=30391.3+0.2\times(30353-30391.3)=30383.64\text{m} \\
\hat{\dot{x}}_{1,1}=40+0.1 \frac{30353-30391.3}{5}=38.65\text{m/s}
\end{cases}$$
*Passo 3*
$$\begin{cases}
\hat{x}_{3,2}=\hat{x}_{2,2}+\Delta t \hat{\dot{x}}_{2,2} \\
\hat{\dot{x}}_{3,2}=\hat{\dot{x}}_{2,2}
\end{cases}=\begin{cases}
\hat{x}_{3,2}=30383.64+5\times38.65=30576.9\text{m} \\
\hat{\dot{x}}_{3,2}=38.65\text{m/s}
\end{cases}$$

- E assim repetimos até à 10ª iteração. Temos isto:
![[medicoes filtro ab.png]]
![[resultados filtro ab.png]]

- E se tivessemos considerado um radar de alta precisão ($\alpha=0.8~,~\beta=0.5$) tínhamos:
![[resultado filtro ab com aceleracao.png]]
vemos que as flutuações nas medições afetam muito mais a previsão

## Exemplo 3 - avião com aceleração 1D
- Vimos antes um avião a mover-se com velocidade constante
- Consideremos agora um avião que se move com velocidade $50\text{m/s}$ por $20\text{s}$. Depois ele move-se com aceleração constante $8\text{m/s}^{2}$ por $35\text{s}$
![[sistema com aceleracao cinematica.png]]
- Vemos que a posição já não varia de forma linear com o tempo

### Exemplo numérico com filtro $\alpha-\beta$
- Desta vez não vou escrever os passos todos, a lógica é exatamente igual
- Começamos com a estimativa inicial: $\hat{x}_{0,0}=30000\text{m}~,~\hat{\dot{x}}_{0,0}=50\text{m/s}$
- No final, obtemos isto:
![[resultado filtro ab com mt aceleracao.png]]
vemos que o filtro claramente não consegue prever e acompanhar os dados reais

## Exemplo 4 - avião com filtro a-b-g
- Este exemplo não é visível no site sem comprar o livro :(((
- Mas basicamente passamos a estimar a aceleração. Assim introduzimos gamma, que permite corrigir a estimativa da aceleração.
- Este filtro é usado quando a aceleração varia muito rapido
(segundo chatGPT)
- Temos as equações de atualização de estado:
$$\boxed{\begin{align*}
\hat{x}_{n,n}&= \hat{x}_{n,n-1}+\alpha(z_{n}-\hat{x}_{n,n-1})\\
\hat{\dot{x}}_{n,n}&= \hat{\dot{x}}_{n,n-1}+ \beta \left(\frac{z_{n}- \hat{x}_{n,n,-1}}{\Delta t}\right)\\
\hat{\ddot{x}}_{n,n}&= \hat{\ddot{x}}_{n,n-1}+ 2\gamma \left(\frac{z_{n}- \hat{x}_{n,n,-1}}{\Delta t^2}\right)
\end{align*}}$$
- Além disso, as equações de extrapolação seriam:
$$\boxed{\begin{align*}
\hat{x}_{n+1,n}&= \hat{x}_{n,n}+\Delta t \hat{\dot{x}}_{n,n} + \frac{1}{2}\Delta t^{2}\hat{\ddot{x}}_{n,n} \\
\hat{\dot{x}}_{n+1,n}&= \hat{\dot{x}}_{n,n}+\Delta t \hat{\ddot{x}}_{n,n}\\
\hat{\ddot{x}}_{n+1,n}&= \hat{\ddot{x}}_{n,n}
\end{align*}}$$
(notemos que o passo de extrapolação prevê no final de uma iteração $n$ logo a previsão $\hat{x}_{n+1,n}$ passa a ser $\hat{x}_{n,n-1}$ ao avançar)

# Filtro Kalman 1D
## Sem ruído de processo
- O filtro de Kalman baseia-se em 5 equações. Já conhecemos 2:
    - **Eq.1** -  Equação de atualização de estado
    - **Eq.2** - Equação do modelo dinâmico ou de extrapolação de estado

**VS filtros a-b-g**
- Similarmente aos filtros $\alpha-\beta-\gamma$, filtros de Kalman utilizam um algoritmo do tipo **medir-atualizar-prever**
- Contrariamente aos filtros $\alpha-\beta-\gamma$, filtros de Kalman consideram todos os valores (medições, previsões atual e futura) como VAs com distribuição normal, descrita por uma média e variância

### Algoritmo
![[algoritmo filtro kalman.png]]

### Incerteza
![[resultado filtro alfa.png]]
- Voltemos ao gráfico obtido para o exemplo 1 do capítulo anterior, com um filtro $\alpha-\beta$. 
- O desvio entre a linha vermelha (estimativa) e a verde (valor real) é o **erro de estimativa**
- Vemos que esse erro vai diminuindo (em módulo) conforme aumentamos as iterações e número de medições. Eventualmente, este erro deverá convergir para erro.
- Nós não conseguimos saber o erro de estimação em si, mas conseguimos estimar a **incerteza**! 
- Definimos a **variância das estimativas de estado** como $p$

### Medição como VA
#### Erros
- O desvio entre a linha azul (medição) e a verde (valor real) é o **erro de medição**. Estes são aleatórios e podemos descrevê-los com uma distribuição normal com média nula e variância $\sigma^{2}$.
    - Dizemos que o *desvio padrão* $\sigma$ do erro de medição é a **incerteza de medição**!!
    - Em alguma literatura o desvio padrão é chamado erro de medição :(
- A variância dos erros de medição pode ser indicada pelo fabricante do sensor ou determinada com um processo de calibração
    - Se tivermos a estudar uma balança, podemos medir n vezes uma massa conhecida e determinar o desvio padrão dos erros de medição do peso

#### Medição
- Definimos a **variância das medições** como $r$
    - Não confundir isto com a variância do erro de medição $\sigma^{2}$
- Em sensores mais avançados isto depende de vários fatores: SNR (signal to noise), largura de feixe, largura de banda, estabilidade do clock, etc. Como isto varia com cada medição, o próprio *radar calcula a incerteza de medição* e comunica juntamente da medição
- Consideremos o exemplo das 10 medições do peso da barra de ouro. Abaixo podemos ver as medições (Azul) na distribuição PDF do sensor. Vemos que dentro da zona $1\sigma$ temos 7/10 medição: recordemos que esta zona contém 68% da probabilidade da PDF
![[medicoes vs dist normal.png]]

### Extrapolação
- Como vimos nos 2 exemplos acima (peso de barra de ouro e avião a velocidade constante), o modelo dinâmico depende completamente do sistema em questão
- No filtro de Kalman precisamos também de estudar a evolução da **variância da estimativa** $p$:
![[previsao e modelo kalman.png]]
- Vejamos como varia a variância da estimativa:
**Ex1 : peso de barra de ouro**
$$p_{n+1,n}=p_{n,n}$$
($p$ é a variância da estimativa do peso da barra)

**Ex2 : avião a velocidade constante**
$$\boxed{\begin{align*}
p_{n+1,n}^{x}&= p_{n,n}^{x}+\Delta t^{2}\cdot p_{n,m}^{v}\\
p_{n+1,n}^{v}&= p_{n,n}^{v}
\end{align*}}$$
($p^{x}$ é a variância da estimativa da posição do avião, $p^{v}$ é a variância da estimativa da velocidade)

- Notamos logo que as equações são bastante parecidas às equações para a estimativa em si. A principal diferença é o intervalo ao quadrado: $\Delta t^{2}$
    - Isto acontece porque quanto temos uma variável $x$ com variância $\sigma^{2}$, então uma certa variável $kx$ terá variância $k^{2}\sigma^{2}$.

**Equação 3**
- Estas equações para determinar a evolução da variância com um sistema dinâmico chamam-se **Equação de extrapolação da covariância** e é a 3ª equação de Kalman!

### Atualização do estado
- Para determinar o estado atual usamos a *previsão de estado anterior* e a *medição*. Ora, vimos que agora ambos têm uma variância:
![[atualizacao e modelo kalman.png]]
- O filtro de Kalman é optimo: combinamos estes 2 fatores de forma a minimizar a incerteza da estimativa do estado atual
- Assim, fazemos uma combinação linear do tipo:
$$\hat{x}_{n,n}=w_{1}z_{n}+w_{2}\hat{x}_{n,n-1} \quad \quad;\quad\quad w_{1}+w_{2}=1$$
mas esta forma implica 2 variáveis novas. Como sabemos que a soma $w_{1}+w_{2}$ dá 1, podemos fazer:
$$\hat{x}_{n,n}=w_{1}z_{n}+(1-w_{1})\hat{x}_{n,n-1}$$
e temos a relação entre as variâncias:
$$p_{n,n}=w_{1}^{2}r_{n}+(1-w_{1})^{2}p_{n,n-1}$$

- Como queremos fazer o passo optimo, temos que minimizar a variância da estimativa do estado atual:
$$\begin{align*}
\frac{dp_{n,n}}{dw_{1}}&= 0\\
2w_{1}r_{n}-2(1-w_{1})p_{n,n-1}&= 0\\
w_{1}r_{n}&= p_{n,n-1}-w_{1}p_{n,n-1}\\
w_{1}&= \frac{p_{n,n-1}}{p_{n,n-1}+r_{n}}
\end{align*}$$
- Podemos reescrever a equação acima:
$$\begin{align*}
\hat{x}_{n,n}&= w_{1}z_{n}+(1-w_{1})\hat{x}_{n,n-1}\\
&= w_{1}z_{n}+\hat{x}_{n,n-1}-w_{1}\hat{x}_{n,n-1}\\
&= \hat{x}_{n,n-1}+w_{1}(z_{n}-\hat{x}_{n,n-1})
\end{align*}$$
que é o que tínhamos no filtro $\alpha$ :0
- Substituimos:
$$\boxed{\hat{x}_{n,n}=\hat{x}_{n,n-1} + \frac{p_{n,n-1}}{p_{n,n-1}+r_{n}}(z_{n}-\hat{x}_{n,n-1})}$$

**Equação 4**
- E, tal como falamos antes, temos aqui o **ganho de Kalman**!! Podemos então defini-lo:
$$\boxed{K_{n}= \frac{p_{n,n-1}}{p_{n,n-1}+r_{n}}=\frac{\text{Variância estimativa}}{\text{Variância estimativa + Variância medição}}}$$
- Esta é a  **equação do ganho de Kalman** e é a 4ª equação de Kalman
- Notemos que este ganho está sempre entre 0 e 1

**Equação 5**
- Passemos à variância. Temos:
$$\begin{align*}
p_{n,n}&= K_{n}^{2}r_{n}+(1-K_{n})^{2}p_{n,n-1}\\
\end{align*}$$
e podemos escrever:
$$1-K_{n}=1-\frac{p_{n,n-1}}{p_{n,n-1}+r_{n}}=\frac{r_{n}}{p_{n,n-1}+r_{n}}$$
logo
$$\begin{align*}
p_{n,n}&= \left(\frac{p_{n,n-1}}{p_{n,n-1}+r_{n}}\right)^{2}r_{n}+\left(\frac{r_{n}}{p_{n,n-1}+r_{n}}\right)^{2}p_{n,n-1}\\
&= \frac{p_{n,n-1}^{2}r_{n}}{(p_{n,n-1}+r_{n})^{2}} + \frac{r_{n}^{2}p_{n,n-1}}{(p_{n,n-1}+r_{n})^{2}}\\
&= \frac{p_{n,n-1}r_{n}}{p_{n,n-1}+r_{n}}\cdot\left[\frac{p_{n,n-1}}{p_{n,n-1}+r_{n}} + \frac{r_{n}}{p_{n,n-1}+r_{n}}\right]\\
&= (1-K_{n})p_{n,n-1} \cdot[K_{n} + (1-K_{n})]\\
&= (1-K_{n})p_{n,n-1}
\end{align*}$$
e temos a 5ª e última equaçãode Kalman: **Equação de atualização da covariância**!!!
$$\boxed{p_{n,n}=(1-K_{n})p_{n,n-1}}$$
- Já que $0\le K_{n}\le1$, vemos que $p_{n,n}$ vai diminuindo com cada iteração já que $1-K_{n}\le1$
    - Quando a incerteza de medição $r$ é alta, temos um ganho baixo e $p$ converge mais devagar
    - Se tivermos alta precisão AKA incerteza $r$ baixa, então $p$ vai converger mais rapidamente 

### Parar medições
- Consideremos que estamos a medir algo e queremos garantir uma incerteza de medição de $\sigma=3\text{cm}$, então devemos repetir o algoritmo e medir pontos até termos $p=\sigma^{2}=9\text{cm}^{2}$

### RESUMO
![[resumo kalman.png]]
(estas equações não incluem o ruído de processo)
(as equações de extrapolação podem não ter nada a ver com isto, dependem do sistema em si)
(isto é uma versão simples em que temos apenas 1D. A forma geral é com matrizes)

### Algoritmo
![[algoritmo kalman.png]]
*Passo 0*
- Fazemos inicialização, apenas é feito 1 vez
- Definimos a estimativa inicial de estado $\hat{x}_{0,0}$ e de variância de estado $p_{0,0}$

*Passo 1*
- Medimos o estado, obtendo-se a medição $z_{n}$ e a sua variância/incerteza $r_{n}$

*Passo 2*
- Atualizamos o estado, tendo em conta a medição
- Os inputs deste processo são:
    - Medição $z_{n}$ e variância de medição $r_{n}$
    - Estado previsto antes $\hat{x}_{n,n-1}$ e respetiva variância $p_{n,n-1}$
- Usando o ganho de Kalman $K_{n}$, este processo gera os outputs:
    - Estimativa do estado atual $\hat{x}_{n,n}$
    - Variância da estimativa do estado atual $p_{n,n}$

*Passo 3*
- Extrapolamos o estado e variância da próxima iteração, que serão depois usado como "previsão anterior"
- Isto depende da equação do sistema dinâmico, que varia muito com o sistema em si
- Na primeira iteração consideramos a estimativa inicial como "previsão do estado anterior"

### Intuição de ganho de Kalman
- Podemos reescrever a equação de atualização de estado:
$$\begin{align*}
\hat{x}_{n,n}&= \hat{x}_{n,n-1} + K_{n}(z_{n} - \hat{x}_{n,n-1})\\
&= (1 - K_{n})\hat{x}_{n,n-1} + K_{n}z_{n}
\end{align*}$$
e assim: o ganho de Kalman é o *peso da medição*, enquanto que $1-K_{n}$ é o *estimativa de estado feita antes*

- O ganho será perto de zero quando a incerteza da medição é alta (como vimos acima) e vice-versa. 
- Isso faz sentido: menor incerteza == Kn maior == damos mais peso à medição

#### Caso de alto ganho
- Neste caso a incerteza de medição é bem menor que a de estimativa. 
- Ou seja, tendo em conta a equação de atualização de estado, vemos que a estimativa do estado atual $\hat{x}_{n,n}$ será bastante próxima de $z_{n}$
- Graficamente teríamos isto:
![[kalman 1d esquema alto ganho.png]]

#### Caso de ganho baixo
- Temos o caso oposto: temos bem mais incerteza de medição do que de estimativa
- Então, tendo o oposto, teremos uma estimativa atual próxima da estimativa feita antes:
![[kalman 1d esquema baixo ganho.png]]

### EX - altura de prédio
- Isto é um exemplo numérico
- Temos um prédio com altura de 50m (isto é a altura **real**)
- O medidor de altura tem desvio padrão / erro de medição de $5\text{m}$
- Temos 10 medições: $49.03, 48.44, 55.21, 49.98, 50.60, 52.61, 45.87, 42.64, 48.26, 55.84\text{ m}$

#### Iteração 0
**Inicialização**
- Definimos a estimativa inicial $\hat{x}_{0,0}=60\text{m}$ 
- Consideramos que a nossa estimativa tem um erro de estimação de tipo $\sigma=15 \text{m}$ logo temos uma variância $\sigma^{2}=225\text{m}^{2}=p_{0,0}$ e temos a nossa estimativa inicial de covariância

**Previsão**
- O prédio em princípio não muda de altura então consideramos um modelo dinâmico **constante**, logo as nossa estimativa para o próximo estado é:
$$\hat{x}_{1,0}=\hat{x}_{0,0}=60 \text{m}$$
e a estimativa da variância também não muda:
$$p_{1,0}=p_{0,0}=225\text{m}^{2}$$

#### Iteração 1
**Passo 1 - medir**
- Conforme acima, temos a medição $z_{1}=49.03\text{m}$
- Como visto no início, o desvio padrão do sensor é $5\text{m}$ logo temos a incerteza da medição $r_{1}=25\text{m}^{2}$ 

**Passo 2 - atualizar estado**
- Calculamos o filtro de Kalman:
$$K_{1}=\frac{p_{1,0}}{p_{1,0} + r_{1}} = \frac{255}{255 + 25} = 0.9$$
e estimamos o estado atual com a equação de cima:
$$\hat{x}_{1,1}= \hat{x}_{1,0}+K_{1}(z_{1}-\hat{x}_{1,0})=50.13\text{m}$$
e estimamos a variância deste estado:
$$p_{1,1}=(1-K_{1})p_{1,0}=22.5\text{m}^{2}$$

**Passo 3 - previsão**
- Como o modelo dinâmico é constante, logo
$$\begin{align*}
\hat{x}_{2,1}&= \hat{x}_{1,1}=50.13\text{ m}\\
p_{2,1}&= p_{1,1}=22.5\text{ m}^{2}
\end{align*}$$

#### Iteração 2
**Passo 1 - medir**
- Depois de 1 unidade de tempo, voltamos a fazer uma medição e obtemos $z_{2}=48.44\text{m}~,~r_{2}=25\text{m}^{2}$

**Passo 2 - atualizar**
- Calculamos o ganho de Kalman desta nova medição
$$K_{2}=\frac{p_{2,1}}{p_{2,1}+r_{2}}=\frac{22.5}{22.5+25}= 0.47$$
agora temos que o ganho baixo bastante: isto significa que a nossa nova medição têm uma incerteza demasiado alta e que não a podemos dar demasiada importância.
- Podemos estimar o estado atual:
$$\hat{x}_{2,2}=\hat{x}_{2,1} + K_{2}(z_{2}-\hat{x}_{2,1})=49.33\text{m}$$
e a estimativa da variância
$$p_{2,2}=(1-K_{2})p_{2,1} = 11.84\text{m}^{2}$$

**Passo 3 - previsão**
- O modelo é constante logo:
$$\begin{align*}
\hat{x}_{3,2}&= \hat{x}_{2,2}=49.33\text{m}\\
p_{3,2}&= p_{2,2}=11.84\text{m}^{2}
\end{align*}$$

#### Final
- Vamos repetindo isto com as 10 medições (logo fazemos 10 iterações)
![[ex numerico 1.png|525]]

- Podemos ver que o ganho vai descendo sempre, o que signfica que estamos a converger para uma estimativa. Isso também significa que vamos ficando mais e mais confiantes na nossa estimativa de estado atual $\hat{x}_{n,n}$
- Se fizessemos 100 iterações teríamos algo do tipo:
![[evolucao ganho kalman.png|525]]
consideramos que o filtro atinge steady-state após ~50 iterações

- Também podemos ver que as estimativas do filtro são muito robustas a variância das medições:
![[estimativas kalman 1d.png]]

- Podemos definir vários critérios de precisão:
    - Erro máximo 
    - Erro médio
    - RMSE (Root Mean Square Error)
e por erro entendemos $e=x-\hat{x}$.

- Precisamos ainda de estimar a incerteza do nosso filtro. Uma maneira "fácil" de fazer isso é definir um intervalo de confiança. Uma opção comum é o intervalode de 95%
![[zona confianca kalman 1d.png]]

## Com ruído de processo
- Isto é então o **filtro de Kalman 1D COMPLETO**

### Ruído de processo
- Na realidade, o modelo do sistema dinâmico **tem incerteza** e isto é algo que nunca vimos até agora
    - Por exemplo, um modelo constante (como "valor de resistência do componente X") pode não ser mesmo constante: o valor real pode variar entre medições
    - Se estivermos a serguir algo com um radar, as "incertezas" do modelo são variações abruptas da aceleração do alvo
- Por outro lado, podemos ter incerteza nula: se estivermos a determinar a posição de um objeto com GPS.
- Ora, essa *incerteza* É o **ruído de processo**
- Representamos este ruído com $q$
- O algoritmo do filtro de Kalman muda no sentido que *incluimos o ruído na equação de extrapolação da covariância*
![[resumo equacoes kalman 1d.png]]
(claro, as equações de extrapolação dependem muito do problema específico)

### EX - temperatura de líquido
- Temos um tanque de líquido a temperatura constante 
    - Mas isso é o que normalmente assumimos
    - Vamos considerar a presença de flutuações da temperatura do líquido
- Modelamos a temperatura como
$$x_{n}=T+w_{n}$$
em que $T$ é a temperatura "constante" e $w_{n}$ é um processo aleatório com variância $q$.

**Assumimos que...**
- Assumimos a temperatura média $T=50ºC$
- Consideremos que o modelo é exato: temos variância do ruído de processo $q=0.0001ºC$ 
- Temos um desvio padrão de medição de $0.1ºC$. 
- Fazemos medições a cada $5s$
- Devido ao processo aleatório, a **temperatura real varia**: $50.005, 49.994, 49.993, 50.001, 50.006, 49.998, 50.021, 50.005, 50, 49.997$
- E as medições feitas são: $49.986, 49.963, 50.09, 50.001, 50.018, 50.05, 49.938, 49.858, 49.965, 50.114$
- Ou seja, temos isto:
![[estimativa kalman 1d valor constante.png]]notemos que o valor real varia!!!

#### Iteração 0
**Inicialização**
- Definimos uma estimativa inicial: $\hat{x}_{0,0}=60ºC$
- Como esta estimativa inicial é só um palpite, forçamos uma variância de estimativa muito elevada de propósito. 
    - Consideremos um desvio padrão de $100ºC$ 
    - Temos $p_{0,0}=100^{2}=10000ºC^{2}$
- Se conseguirmos fazer uma estimativa melhor com menos incerteza, o filtro vai converger mais rapidamente

**Previsão**
- Consideramos um modelo de dinâmica constante: $\hat{x}_{1,0}=60ºC$
- E temos a equação de extrapolação da variância com o processo aleatório:
$$p_{1,0}=p_{0,0}+q=10000.0001ºC$$

#### Iteração 1
**Passo 1 - medir**
- Medimos $z_{1}=49.986ºC$
- Como vimos, o desvio padrão é $\sigma=0.1$ logo temos: $r_{1}=0.01ºC^{2}$

**Passo 2 - atualizar**
- Calculamos o ganho:
$$K_{1}=\frac{p_{1,0}}{p_{1,0}+r_{1}}=0.999999$$
e isto é resultado de fazermos uma estimativa inicial muito fraca: ela terá peso nulo na atualização de estado, enquanto que a medição terá todo o peso.

- Assim:
$$\begin{align*}
\hat{x}_{1,1}&= \hat{x}_{1,0}+K_{1}(z_{1}-\hat{x}_{1,0})=49.986ºC\\
p_{1,1}&= (1-K_{1})p_{1,0}=0.01ºC^{2}
\end{align*}$$

**Passo 3 - prever**
- O modelo é constante com ruído:
$$\begin{align*}
\hat{x}_{2,1}&= \hat{x}_{1,1}=49.986ºC\\
p_{2,1}&= p_{1,1}+q=0.0101ºC
\end{align*}$$

#### Iteração 2
**Passo 1 - medir**
- Medimos $z_{2}=49.963ºC$
- Novamente, temos $r_{2}=0.01ºC^{2}$ -- isto será constante, assumimos ruído de processo com variância constante

**Passo 2 - atualizar**
- Temos o ganho:
$$K_{2}=\frac{p_{2,1}}{p_{2,1}+r_{2}}=0.5$$
- E podemos estimar o estado atual
$$\begin{align*}
\hat{x}_{2,2}&= \hat{x}_{2,1}+K_{2}(z_{2}-\hat{x}_{2,1})=49.974ºC\\
p_{2,2}&= (1-K_{2})p_{2,1}=0.005ºC^{2}
\end{align*}$$

**Passo 3 - prever**
- Temos modelo constante com ruído:
$$\begin{align*}
\hat{x}_{3,2}&= \hat{x}_{2,2}=49.974ºC\\
p_{3,2}&= p_{2,2} + q = 0.0051ºC
\end{align*}$$

#### Final
- Continuamos isto até à iteração 10
![[ex numerico 2.png]]

- O ganho evoluiu desta forma
![[evolucao ganho kalman 2.png]]

- Podemos ver o intervalo 95%:
![[intervalo confianca kalman valor constante.png]]

### mais 2 EXs
- No site tem mais 2 exemplos:
    - **Exemplo 7** - estimar temperatura de tanque em aqecimento I
        - A temperatura real aumenta linearmente com o tempo e temos ruído de processo de variância $q$.
        - Neste exemplo mantivemos o modelo constante
        - As estimativas não conseguem acompanhar o valor real: ![[estimativa kalman aviao com aquecimento.png]]

    - **Exemplo 8** - estimar temperatura de tanque em aqecimento II
        - Neste caso aumentamos a variância do ruído ($q$) de 0.0001 para 0.15
        - Isto faz com que o nosso modelo seja muito mais livre, mas também fica muito mais dependente das medições (qualquer ruído afeta a nossa estimativa)
        - Temos um resultado melhor, mas muito justo das medições: ![[estimativa kalman com aceleracao e variancia alta.png]]
        - No entanto, notemos que não temos **erro de lag**
        - Neste caso, o ganho estabiliza em 0.94 logo na 2ª iteração. Ou seja, ficamos com um modelo que quase só replica as medições e introduz alguma memória

# Kalman Multivariável
- Consideramos um Filtro de Kalman Linear (LKF) assume que o sistema dinâmico é linear
- Até aqui vimos estimação de parâmetros 1D (distância, temperatura, etc) 
- Agora vamos ver como fica o filtro quando temos algo multivariável como um **espaço de estado**: $\begin{bmatrix}x\\ y\\ z\end{bmatrix}$ ou  $\begin{bmatrix}x & y & z & \dot{x} & \dot{y} & \dot{z}\end{bmatrix}$
- Ou podemos até ter um vetor 9D com posições, velocidades ou acelerações

- Assumindo aceleração costante, podemos evoluir o vetor para o próximo instante assim
$$\begin{cases}
x_{n}=x_{n-1} + \dot{x}_{n-1}\Delta t + \frac{1}{2} \ddot{x}_{n-1}\Delta t^{2} \\
y_{n}=y_{n-1} + \dot{y}_{n-1}\Delta t + \frac{1}{2} \ddot{y}_{n-1}\Delta t^{2} \\
z_{n}=z_{n-1} + \dot{z}_{n-1}\Delta t + \frac{1}{2} \ddot{z}_{n-1}\Delta t^{2} \\
\dot{x}_{n}=\dot{x}_{n-1} + \ddot{x}_{n-1}\Delta t \\
\dot{y}_{n}=\dot{y}_{n-1} + \ddot{y}_{n-1}\Delta t \\
\dot{z}_{n}=\dot{z}_{n-1} + \ddot{z}_{n-1}\Delta t \\
\ddot{x}_{n}=\ddot{x}_{n-1} \\
\ddot{y}_{n}=\ddot{y}_{n-1} \\
\ddot{z}_{n}=\ddot{z}_{n-1} \\
\end{cases}$$
mas isto é chato de escrever e é pouco efiicente. É **MUITO** mais fácil fazer isto em matrizes!! Essa é a forma do filtro de Kalman mais útil e comum

## Bases de álgebra
- Notação:
    - letras minusculas a negrito $\boldsymbol{x}$ são **vetores**
    - letras maiusculas a negrito $\mathbf{A}$ são **matrizes**
    - letras minusculas normais $x$ são *escalares ou elementos de matrizes*
    - letras maiusculas normais $A$ são *elementos de matriz*

### Álgebra e probabilidades
#### Valor esperado
$$\boxed{\mathbb{E}[X]=\mu_{X}}$$
- E temos as propriedades:
    - $E[X]=\mu_{X}=\sum x p(x)$
    - $E[a]=a$
    - $E[aX]=aE[X]$
    - $E[a\pm X]=a\pm E[X]$
    - $E[a\pm bX]=a\pm b E[X]$
    - $E[X\pm Y]=E[X]\pm E[Y]$
    - $E[XY]=E[X]E[Y]$

#### Variância
$$\boxed{V(X) = \mathbb{E}[X^{2}] - \mu_{X}^{2}}$$
- Temos as propriedades:
    - $V(a)=0$
    - $V(a\pm X)=V(X)$
    - $V(aX)=a^{2}V(x)$
        - **Cinemática**: podemos aplicar esta equação com uma posição $x$ e velocidade $v$: $$V(x)=\Delta t^{2} V(v) ~~~~,~~~~ \sigma_{x}^{2}=\Delta t^{2}\sigma_{v}^{2}$$

#### COV
$$\boxed{COV(X,Y) = \mathbb{E}[XY] - \mu_{X}\mu_{Y}}$$
- E temos as propriedades
    - $COV(X,Y)=0 ~~,~~ \text{se X,Y são independentes}$
    - $V(aX)=a^{2}V(X)$ 
    - $V(X\pm Y)=V(X) + V(Y) \pm 2 COV(X,Y)$
    - $V(XY)\neq V(X)V(Y)$

### Distribuição normal multivariável
- Mantemos a notação que acima:
    - $p_{n,n}$ é a estimativa da variância do instante atual
    - $p_{n+1,n}$ é a estimativa da variância do próximo instante
    - $r_{n}$ é a incerteza/variância da próxima medição
    - $q$ é o ruído de processo
mas no caso multivariável tudo isto passa a ser matrizes!!! Temos as matrizes $\mathbf{P}_{n,n}, \mathbf{P}_{n+1,n}, \mathbf{R}_{n}, \mathbf{Q}$
- E usamos isto porque o output do filtro de Kalman normalmente é um VA com n-dimensões: $\boldsymbol{x}=\begin{bmatrix}x\\y \end{bmatrix}$

#### Covariância
- A covariância mede o quanto 2+ variáveis se relacionam. 
- No caso 2D, isto significa "quanto é que os dados se relacionam no xOy"
![[covariancia 2d.png]]
- Por exemplo, temos que nos 2 plots de cima temos medições com baixa correlação: 
    - No 1º plot os valores parecem aleatórios
    - No 2º plot os valores de y são +/- constantes para qualquer valor de x, logo eles não se afetam um ao outro
- Nos 2 plots de baixo temos medições correlacionadas: em ambos os casos, aumentar X causa uma variação de Y.
- Podemos então definir covariância como:
$$COV(X,Y)=\frac{1}{N-1} \sum\limits_{i=1}^{N} (x_{i}-\mu_{X})(y_{i}-\mu_{Y})$$
que podemos escrever como:
$$COV(X,Y)=\frac{1}{N-1}\sum\limits_{i=1}^{N}(x_{i}y_{i}) - \frac{N}{N-1}\mu_{X}\mu_{Y}$$
ou ainda, usando $x,y$ como vetores com forma $N\times1$
$$COV(X,Y)=\frac{1}{N-1} \boldsymbol{x}^{T}\boldsymbol{y} - \frac{N}{N-1} \mu_{X}\mu_{Y}$$

#### Matriz covariância
- Vimos como determinar a covariância entre 2 VAs. Mas tendo 2VAs temos 4 combinações possíveis de covariâncias XX, XY, YX, YY
- É precisamente isso que a matriz de covariância contém:
$$\boldsymbol{\Sigma} = \begin{bmatrix}\sigma_{xx} & \sigma_{xy} \\ \sigma_{yx} & \sigma_{yy}\end{bmatrix}=\begin{bmatrix}\sigma_{x}^{2} & \sigma_{xy} \\ \sigma_{yx} & \sigma_{y}^{2}\end{bmatrix}=\begin{bmatrix}\text{V}(x) & \text{Cov}(x,y) \\ \text{Cov}(y,x) & \text{V}(y)\end{bmatrix}$$
- Claro, temos que $\text{Cov}(x,y)=\text{Cov}(y,x)$
- Se $x,y$ não tiverem correlação, os elementos fora da diagonal principal são zero
- Em $n$ dimensões temos
$$\boldsymbol{\Sigma}=\begin{bmatrix} \sigma_{1}^{2} & \sigma_{12} & \cdots & \sigma_{1n} \\ \sigma_{21} & \sigma_{2}^{2} & \cdots & \sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_{n1} & \sigma_{n2} & \cdots & \sigma_{n}^{2} \end{bmatrix}$$

##### Propriedades
1. Os elementos da diagonal principal da matriz são as variâncias dos componentes da VA multivariável.
    - Se tivermos $\boldsymbol{x}=\begin{pmatrix}x\\y\end{pmatrix}$ teremos $\text{diag}[\boldsymbol{\Sigma}]=\begin{pmatrix}\sigma_{x}^{2} & \sigma_{y}^{2}\end{pmatrix}$
2. Por serem variâncias, os valores da diagonal são não negativos. Logo, também o traço da matriz é não negativo: $$\text{tr}[\boldsymbol{\Sigma}] = \sum\limits_{i=1}^{n}\boldsymbol{\Sigma}_{ii} \ge 0$$
3. Como $COV(X,Y)=COV(Y,X)$ temos $\sigma_{ij}=\sigma_{ji}$ e a **a matriz é simétrica**
4. A matriz é positiva semidefinida
    - Uma matriz $\mathbf{A}$ é positiva semidefinida se, para qualquer vetor $\boldsymbol{v}\neq0$ temos $\boldsymbol{v}^{T}\mathbf{A}\boldsymbol{v}\ge0$
    - Isso significa ainda que os valores próprios de $\mathbf{A}$ são não negativos

##### Matriz COV e valor esperado
- Consideremos os vetores $\boldsymbol{x}=\begin{pmatrix}x_{1} \\ x_{2} \\ \vdots \\ x_{k}\end{pmatrix}~,~ \boldsymbol{\mu}_{x}=\begin{pmatrix}\mu_{x1} \\ \mu_{x2} \\ \vdots \\ \mu_{xk}\end{pmatrix}$
- Podemos definir a covariância deste vetor como sendo:
$$\text{COV}(\boldsymbol{x})= \mathbb{E} \{(\boldsymbol{x}-\boldsymbol{\mu}_{x})(\boldsymbol{x} - \boldsymbol{\mu}_{x})^{T}\}$$
que nos dá uma matriz de covariância com forma $k\times k$

#### Distribuição
- Em 1D temos:
$$p(x|\mu,\sigma)=\frac{1}{\sqrt{2\pi}\sigma}\exp \left(- \frac{(x-\mu)^{2}}{2\sigma^{2}} \right)\sim N(\mu, \sigma^{2})$$
- Ora, num espaço com $n$ dimensões temos:
$$p(\boldsymbol{x}|\boldsymbol{\mu},\boldsymbol{\Sigma})=\frac{1}{\sqrt{2\pi |\boldsymbol{\Sigma}|}}\exp \left(- \frac{1}{2} (\boldsymbol{x}-\boldsymbol{\mu})^{T}\boldsymbol{\Sigma}^{-1}(\boldsymbol{x}-\boldsymbol{\mu}) \right)$$

#### Normal bivariável
- Isto é o caso de uma distribuição normal no espaço 3D: temos $z$ a ser definido através de  $x,y$
![[Attachments/gaussiana 2d.png]]
Notemos ainda que ao projetar esta curva no plano $z=0$ temos uma elipse:
![[gaussiana 2d projecao.png]]

#### Elipse de covariância
- Vamos então ver essa elipse. Ela marca uma curva de contorno da gaussiana que, por exemplo, podemos usar para representar a região $xOy$ onde temos probabilidade de  95%
- Recordemos os 4 parâmetros que definem uma elipse:
![[elipse carateristicas.png]]
temos o ângulo $\theta$, o semieixo maior $a$ e menor $b$ e as coordenadas do seu centro $(\mu_{x},\mu_{y})$
- E podemos definir todos eles:
    - $\mu_{x}=\frac{1}{N}\sum_{i} x_{i}$
    - $\mu_{y}=\frac{1}{N}\sum_{i} y_{i}$
    - $a=\sqrt{\lambda_{1}}$ (em que $\lambda_{1}$ é o maior valor próprio da matriz $\boldsymbol{\Sigma}$)
    - $b=\sqrt{\lambda_{2}}$ (em que $\lambda_{2}$ é o segundo maior valor próprio da matriz $\boldsymbol{\Sigma}$)
    - $\theta=\arctan(\frac{v_{y}}{v_{x}})$ em que $v_{x},v_{y}$ são as coordenadas do vetor próprio associado a $\lambda_{1}$

## Equações e deduções
### Equação de extrapolação de estado
- Esta é a equação que permite estimar o estado no próximo instante: $\hat{x}_{n+1,n}$
- Esta é então a equação em que aplicamos o modelo do sistema dinâmico que descreve o sistema
- Podemos então definir uma forma geral, que encaixa com o que vimos em 1D
$$\hat{\boldsymbol{x}}_{n+1,n}= \mathbf{F}\hat{\boldsymbol{x}}_{n,n} + \mathbf{G}\boldsymbol{u}_{n}+\boldsymbol{w}_{n}$$
em que:
    - $\hat{x}_{n+1,n}$ é a estimativa do estado no próximo instante
    - $\hat{x}_{n,n}$ é a estimativa do nosso estado atual
    - $u_{n}$ é uma variável de controlo ou de input : algo **medível e determinístico**
    - $w_{n}$ é o ruído de processo : algo **não medível e aleatório**
    - $\mathbf{F}$ é a matriz de transição de estado
    - $\mathbf{G}$ é a matriz de controlo ou de transição de input
- Vejamos as dimensões:
![[variaveis eq extrapolacao estado.png]]
- E temos uma esquematização disto
![[esquema kalman multivariavel.png]]
- Ao modelar a física de um sistema, o termo de ruído de processo não aparece claro. Ele é introduzido como forma de modelar e explicar a incerteza.

**Inputs VS variáveis de estado**
- Propriedades físicas do objeto devem ser variáveis de estado
- Forças externas são inputs, que controlam o estado do objeto
- Em certos casos, a aceleração do objeto é um input (porque é como se fosse uma força externa). Nestes casos, consideramos a posição e velocidade como principais variáveis

**Exemplos**
- No site tem alguns exemplos a mostrar como se obtem $\mathbf{F,G}$ e como o sistema fica quando consideramos a aceleração uma variável de estado VS um input externo

**Exemplo: queda livre**
- Temos um objeto em queda livre. Consideremos que a altura $h$ e velocidade $\dot{h}$ são as variáveis de estado. Temos:
$$\hat{\boldsymbol{x}}_{n}=\begin{pmatrix}h_{n} \\ \dot{h}_{n}\end{pmatrix}$$
- Sabemos que $x_{n+1}=x_{n} + \Delta t \dot{x}_{n}$. Assim, temos a matriz $\mathbf{F}$:
$$\mathbf{F}=\begin{pmatrix}1 & \Delta t \\ 0 & 1\end{pmatrix}$$
- Consideramos a aceleração da gravidade como sendo um input externo. Ou seja:
$$\boldsymbol{u}_{n}=\begin{pmatrix}g\end{pmatrix}$$
- Sabemos que, quanto temos aceleração: $x_{n+1}=x_{n}+\Delta t \dot{x}_{n}+0.5\Delta t^{2}\ddot{x}_{n}$ e $\dot{x}_{n+1}=\dot{x}_{n}+ \Delta t \ddot{x}_{n}$. Assim temos:
$$\mathbf{G}=\begin{pmatrix} \frac{1}{2}\Delta t^{2} \\ \Delta t\end{pmatrix}$$
- Juntando tudo:
$$\boldsymbol{h}_{n+1}= \begin{pmatrix}1 & \Delta t \\ 0 & 1\end{pmatrix}\boldsymbol{h}_{n} + \begin{pmatrix} \frac{1}{2}\Delta t^{2} \\ \Delta t\end{pmatrix}\boldsymbol{u}_{n}$$

### SLITs
- Um filtro de Kalman linear assume um modelo SLIT
- Ou seja, o filtro de Kalman assume que o sistema em estudo é Linear e invariante no tempo
- Ser **linear** implica que:
$$y(t)=\mathcal{F}[ag(t)+bh(t)]=a \mathcal{F}[g(t)] + b \mathcal{F}[h(t)]$$
o que significa: a resposta do sistema a um conjunto de inputs é igual à soma das respostas a cada um desses inputs

- Ser **invariante no tempo** implica que a função de transferência é constante no tempo.
    - Claro, isto não quer dizer que a resposta será constante no tempo
    - Num sistema invariante no tempo, um atraso de 1 unidade no input causa um atraso de 1 unidade no input

### Modelar sistemas lineares
- A lógica é esta:
![[sistemas lineares kalman.png|500]]

#### Espaço de estados
- Este tipo de representação que já conheço é escrito como
$$\begin{align*}
\dot{x}=Ax+Bu\\
y=Cx+Du
\end{align*}$$
- De seguida o site mostra alguns exemplos de como obter a representação SS em sistemas físicos
- Também se fala no caso de um sistema ser descrito por equações diferenciais de alta ordem. Convertem uma equação numa representação SS na forma canónica controlável
    - Calculam 2 exemplos físicos em que obtemos a equação diferencial e depois a equação SS

#### Resolver a equação diferencial
- OK, voltemos a Kalman. Queremos relacionar as equações:
$$\begin{align*}
\hat{\boldsymbol{x}}_{n+1,n}&= \mathbf{F}\hat{\boldsymbol{x}}_{n,n}+\mathbf{G}\hat{\boldsymbol{u}}_{n,n}\\
\dot{x}(t) &= A x(t) + B u(t)
\end{align*}$$

##### Sem input
- Num SLIT sem input temos $\dot{x}=Ax$
- Em 1D podemos escrever $A\equiv k$ e resolvemos a equação diferencial:
$$\begin{align*}
\frac{dx}{dt}&= kx\\
\frac{dx}{x}&= kdt\\
\ln(x_{1}) - \ln(x_{0})&= k \Delta t\\
x_{1}&= e^{\ln x_{0}+k\Delta t}\\
x_{1}&= x_{0}e^{k \Delta t}
\end{align*}$$

- Em nD ficamos com:
$$x_{n+1}=x_{n} e^{\mathbf{A}\Delta t}$$
e temos que a matriz de transição é dada por:
$$\boxed{\mathbf{F} = \exp(\mathbf{A}\Delta t)}$$
- Uma forma de calcular a matriz exponencial é por série de Taylor:
$$\mathbf{F}=e^{\mathbf{A} \Delta t}=\mathbf{I} + \mathbf{A}\Delta t + \frac{(\mathbf{A}\Delta t)^{2}}{2!} + \frac{(\mathbf{A}\Delta t)^{3}}{3!}+\dots$$

##### Com input
- Não vamos deduzir. O que queremos fazer para obter a equação de extrapolação de estado é *passar SS para um sistema discreto*. Ou seja, considerando que temos um hold sampling de ordem zero, em que o input é constante entre pedaços, temos que
$$\begin{align*}
\dot{x}(t)&= \mathbf{A}x(t)+\mathbf{B}u(t)\\
&\downarrow\\
\boldsymbol{x}(t+\Delta t)&= e^{\mathbf{A}\Delta t}x(t) + \int_{0}^{\Delta t}e^{\mathbf{A}\Delta t}dt \mathbf{B} u(t)
\end{align*}$$
ou seja:
$$\boxed{\mathbf{G} = \int_{0}^{\Delta t}\exp(\mathbf{A}\Delta t)dt \cdot\mathbf{B}}$$

### Equação de extrapolação de covariância
- A equação geral é:
$$\mathbf{P}_{n+1,n}= \mathbf{FP}_{n,n}\mathbf{F}^{T}+\mathbf{Q}$$
em que:
    - $\mathbf{P}_{n,n}$ é a matriz de covariância da estimativa de estado atual
    - $\mathbf{P}_{n+1,n}$ é a covariância da estimativa para o próximo estado
    - $\mathbf{F}$ é a matriz de transição que deduzimos antes
    - $\mathbf{Q}$ é a matriz do ruído de processo
- No site deduzem a equação sem ruído. O ruído é depois adicionado para completar o modelo

### Definir a matriz de ruído Q
- Em 1D, vimos que o ruído de processo pode ser introduzido no modelo como uma variância extra $q$
    - Vimos nos exemplos que um $q$ demasiado reduzido faz com que as estimativas não consigam acompanhar as medições.
    - Já um valor muito elevado faz com que as estimativas sigam cegamente as medições
- Em nD, vimos a equação de extrapolação de estado:
$$\hat{\boldsymbol{x}}_{n+1,n}=\mathbf{F}\hat{\boldsymbol{x}}_{n,n}+\mathbf{G}\hat{\boldsymbol{u}}_{n,n}+\boldsymbol{w}_{n}$$
em que temos o ruído de processo $\boldsymbol{w}_{n}$

- Normalmente assumimos uma matriz diagonal, o que indica que o **ruído é independente**:
$$\mathbf{Q} = \begin{pmatrix}q_{11} & 0 & \cdots & 0 \\ 0 & q_{22} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & q_{kk}\end{pmatrix}$$
- Em certos casos, podemos considerar o ruído dependente do tempo! Ou seja, é algo variável e algo que pertence ao ambiente. Temos 2 tipos:
    - Modelo de ruído discreto
    - Modelo de ruído contínuo
- E se quiseres ver isto direito, compra o livro :)

### Equação de medição
- Vimos as 2 equações que estimam o futuro, o próximo estado do sistema
- Agora vamos ver as equações que permitem determinar o estado atual, algo essencial para conseguirmos estimar o futuro
- Em 1D indicamos as medições como $z_{n}$, com uma variância $r_{n}$
- Em nD, generalizamos isto:
$$\boldsymbol{z}_{n}=\mathbf{H} \boldsymbol{x}_{n} + \boldsymbol{v}_{n}$$
em que
    - $\boldsymbol{z}_{n}$ é um vetor com as medições de todos os componentes do estado
    - $\boldsymbol{x}_{n}$ é o vetor de estado **real** (sendo portanto escondido e desconhecido)
    - $\boldsymbol{v}_{n}$ é um vetor de ruído aleatório
    - $\mathbf{H}$ é a **matriz de observação**
- E temos estas formas:
![[variaveis equacao medicoes kalman.png]]

### Matriz de observação
- Muitas vezes medimos algo que não é diretamente o estado: um termómetro digital mede corrente, mas o estado que queremos conhecer é a temperatura
- Assim, usamos uma matriz $\mathbf{H}$ para fazer esta transformação entre o estado do sistema e a medição
- Notemos, claro, que o número de medições e de variáveis de estado será muitas vezes diferente. Esta matriz pretende tornar os tamanhos compatíveis

#### Scaling
- Isto é o caso de radares. Enviamos um sinal e medimos o tempo de voo dele, o que nos permite determinar a distância.
- Fazemos **scaling**:
$$\boldsymbol{z}_{n}=\begin{pmatrix} \frac{2}{c}\end{pmatrix}\boldsymbol{x}_{n}+\boldsymbol{v}_{n}~~~~\to~~~~ \mathbf{H}=\begin{pmatrix} \frac{2}{c} \end{pmatrix}$$
- Ou seja, reduzimos todas as medições com uma escala 

#### Escolha de estado
- Isto é o caso quando medimos apenas alguns dos estados num certo instante. Ou então, quando apenas alguns estados são medíveis.
- Por exemplo, se apenas o 1º, 3º e 5º estados forem medíveis, temos:
$$\boldsymbol{z}_{n}=\mathbf{H}\boldsymbol{x}_{n}+\boldsymbol{v}_{n}=\begin{pmatrix}1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1\end{pmatrix}\begin{pmatrix}x_{1} \\ x_{2} \\ x_{3} \\ x_{4} \\ x_{5}\end{pmatrix}+\boldsymbol{v}_{n}$$

#### Combinação de estados
- Para os casos em que só conseguimos medir vários estados juntos, sem os conseguir separar
$$\boldsymbol{z}_{n}=\mathbf{H}\boldsymbol{x}_{n}+\boldsymbol{v}_{n}=\begin{pmatrix}1 & 1 & 1\end{pmatrix}\begin{pmatrix}x_{1}  \\ x_{2}  \\ x_{3} \end{pmatrix}+\boldsymbol{v}_{n}=(x_{1}+x_{2}+x_{3})+\boldsymbol{v}_{n}$$

### Equação de atualização de estado
- Seguindo o formato da versão 1D, temos
$$\hat{\boldsymbol{x}}_{n,n}=\hat{\boldsymbol{x}}_{n,n-1}+ \mathbf{K}_{n}(\boldsymbol{z}_{n}- \mathbf{H}\hat{\boldsymbol{x}}_{n,n-1})$$
em que
    - $\mathbf{K}_{n}$ é o ganho de Kalman

- E temos as dimensões:
![[variaveis eq atualizacao estado.png]]
notemos especialmente a forma do ganho de Kalman.


### Equação de atualização de covariância
- Consiste em
$$\mathbf{P}_{n,n}=(\mathbf{I}-\mathbf{K}_{n}\mathbf{H})\mathbf{P}_{n,n-1}(\mathbf{I}-\mathbf{K}_{n}\mathbf{H})^{T} + \mathbf{K}_{n}\mathbf{R}_{n}\mathbf{K}_{n}^{T}$$
em que
    - $\mathbf{K}_{n}$ é o ganho de Kalman
    - $\mathbf{R}_{n}$ é a matriz de covariância do ruído de medição
    - $\mathbf{I}$ é a matriz identidade com forma $n\times n$

- No site tem toda a dedução desta equação. Quero apenas notar 2 das equações na base da dedução:
$$\mathbf{P}_{n,n}=\mathbb{E}\{(\boldsymbol{x}_{n}-\hat{\boldsymbol{x}_{n}})(\boldsymbol{x}_{n}-\hat{\boldsymbol{x}_{n}})^{T}\}=\mathbb{E}\{\boldsymbol{e}_{n}\boldsymbol{e}_{n}^{T}\} \quad;\quad \mathbf{R}_{n}=\mathbb{E}\{\boldsymbol{v}_{n}\boldsymbol{v}_n^T\}$$
(em que $\boldsymbol{e}_{n}=\boldsymbol{x}_{n}-\hat{\boldsymbol{x}}_{n}$ é o erro da estimativa)

### Equação do ganho de Kalman
- Temos
$$\mathbf{K}_{n}= \mathbf{P}_{n,n-1}\mathbf{H}^{T}(\mathbf{HP}_{n,n-1}\mathbf{H}^{T} +\mathbf{R}_{n})^{-1}$$
e notemos as semelhanças à equação 1D equivalente:
$$k_{n}=\frac{p_{n,n-1}}{p_{n,n-1}+r_{n}}=p_{n,n-1}(p_{n,n-1}+r_{n})^{-1}$$

### Equação de atualização da covariância simplificada
- Em alguma literatura, podemos ver esta equação muito mais simplificada:
$$\mathbf{P}_{n,n}=(\mathbf{I}-\mathbf{K}_{n}\mathbf{H})\mathbf{P}_{n,n-1}$$
- Isto é obtido ao substituir a equação do ganho $\mathbf{K}_{n}$ na segunda parcela da equação completa $\mathbf{P}_{n,n}=(\mathbf{I}-\mathbf{K}_{n}\mathbf{H})\mathbf{P}_{n,n-1}(\mathbf{I}-\mathbf{K}_{n}\mathbf{H})^{T} + \mathbf{K}_{n}\mathbf{R}_{n}\mathbf{K}_{n}^{T}$
- Isto é uma versão muito mais fácil de memorizar e calcular, mas pode causar erros de cálculo enormes, especialmente devido a erros de floating point. Ou seja: esta equação é **numericamente instável**

## Resumo das equações
### Algoritmo
![[algoritmo kalman multivar.png]]

### Equações
![[resumo equacoes kalman multivariavel.png]]

### Dimensões
![[resumo variaveis kalman multivariavel.png]]

# Kalman extendido / não linear
- Não tem nada no site, é preciso comprar o livro :)
- 