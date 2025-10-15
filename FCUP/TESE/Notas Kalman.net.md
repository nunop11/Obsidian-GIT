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
