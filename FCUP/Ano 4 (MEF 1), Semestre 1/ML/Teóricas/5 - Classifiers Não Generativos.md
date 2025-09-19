# Classifiers Discriminativos
- Nas aulas anteriores estudamos classificadores *generativos*, em que
    - Começamos por determinar as propriedades class-conditional $p(\mathbf{x}|\mathcal{C}_{k})$
    - Prevemos as propriedades prior $p(\mathcal{C}_{k})$ com o nosso conhecimento do problema
    - Usamos o teorema de Bayes $p(\mathcal{C}_{k}|\mathbf{x})=\frac{p(\mathbf{x}|\mathcal{C}_{k})p(\mathcal{C}_{k})}{p(\mathbf{x})}$ para determinar as propriedades posteriores
    - Usamos as propabilidades posterior para atribuir a classe a cada novo valor de $\mathbf{x}$

- Vamos agora ver um tipo de classificador que não é degenerativo: classificador *discriminativo*
    - Prevemos $p(\mathcal{C}_{k}|\mathbf{x})$ diretamente
    - Usamos as propabilidades posterior para atribuir a classe a cada novo valor de $\mathbf{x}$

## Regressão Logística
- Vimos que, em Naive Bayes, podemos calcular $P(y|\mathbf{x})$ ao conhecer $P(y),P(\mathbf{x}|y)$. Mas porque não calcular diretamente $P(y|\mathbf{x})$?
- Isso significaria aprender uma função $f:\mathbf{x}\to y$ em que
    - $\mathbf{x}$ é um vetor de atributos $\in\mathbb{R}$, $\{x_{1},\dots,x_{n}\}$
    - $y$ é boleano
    - todos os $x_{i}$ são condicionalmente independentes de $y$
    - Consideramos $P(x_{i}|y=y_{k})$ como sendo gaussiana $\sim \text{N}(\mu_{ik},\sigma_{i})$
    - Consideramos $P(y)$ como sendo $\sim\text{Bernoulli}(\pi)$
- Isto resulta em (Não sei como lol)

- Vejamos como é que isto fica no caso de $x_{i}$ ser contínuo
$$\begin{align*}
P(Y=1|X)&= \frac{P(Y=1)P(X|Y=1)}{P(Y=1)P(X|Y=1)+P(Y=0)P(X|Y=0)}\\
&= \frac{1}{1 + \frac{P(Y=0)P(X|Y=0)}{P(Y=1)P(X|Y=1)}}\\
&= \frac{1}{1+ \exp\left(\ln \frac{P(Y=0)P(X|Y=0)}{P(Y=1)P(X|Y=1)}\right)}\\
&= \frac{1}{1+ \exp\left(\ln\left(\frac{P(Y=0)}{P(Y=1)}\right) + \ln(\frac{P(X|Y=0)}{P(X|Y=1)})\right)}\\
&= \frac{1}{1+\exp \left(\ln \frac{1-\pi}{\pi} \right) + \sum\limits_{i}\ln \frac{P(X_{i}|Y=0)}{P(X_{i}|Y=1)} }
\end{align*}$$
no primeiro passo usamos o facto que $Y$ é boleano, logo =1 ou =0. No último passo usamos a definição de $X_{i}$ é condicionalmente independente de $Y$: $P(x_{1},x_{2},\dots,x_{n}|y)=P(x_{1}|y)P(x_{2}|y)\cdots P(x_{n}|y)$. 

- Continuemos a dedução. Sabemos que $P(x_{i}|y_{k})=\frac{1}{\sigma_{i}\sqrt{2\pi}}e^{\frac{-(x-\mu_{ik})^{2}}{2\sigma_{i}^{2}}}$, logo:
$$\begin{align*}
P(Y=1|X)&= \frac{1}{1+\exp \left(\ln \frac{1-\pi}{\pi} \right) + \sum\limits_{i}\ln \frac{P(X_{i}|Y=0)}{P(X_{i}|Y=1)} }\\
&= \frac{1}{1+\exp \left(\ln \frac{1-\pi}{\pi} + \sum\limits_{i}\ln \frac{\frac{\exp\left(\frac{-(x-\mu_{i0})^{2}}{2\sigma_{i}^{2}}\right)}{\sigma_{i}\sqrt{2\pi}}}{\frac{\exp\left(\frac{-(x-\mu_{i1})^{2}}{2\sigma_{i}^{2}}\right)}{\sigma_{i}\sqrt{2\pi}}} \right)}\\
&= \frac{1}{1+\exp \left(\ln \frac{1-\pi}{\pi} + \sum\limits_{i}\left(\ln \frac{\exp\left(\frac{-(x-\mu_{i0})^{2}}{2\sigma_{i}^{2}}+\frac{(x-\mu_{i1})^{2}}{2\sigma_{i}^{2}}\right)}{\sigma_{i}/\sigma_{i}} \right)  \right)}\\
&= \frac{1}{1+\exp \left(\ln \frac{1-\pi}{\pi} + \sum\limits_{i}\left(\frac{-(x-\mu_{i0})^{2}}{2\sigma_{i}^{2}}+\frac{(x-\mu_{i1})^{2}}{2\sigma_{i}^{2}}\right)\right)}\\
&= \frac{1}{1+\exp \left(\ln \frac{1-\pi}{\pi} + \sum\limits_{i}\left(\frac{\mu_{i0}-\mu_{i1}}{\sigma_{i}^{2}}X_{i} + \frac{\mu_{i1}^{2}-\mu_{i0}^{2}}{2\sigma_{i}^{2}}\right)\right)}\\
&= \frac{1}{1+\exp\left(w_{0}+\sum\limits_{i=1}^{n}w_{i}X_{i}\right)}
\end{align*}$$
### Mas.....
- Esta equação de $P(Y=1|X)$ implica que
$$P(Y=0|X)=\frac{\exp(w_{0}+\sum_{i}w_{i}X_{i})}{1+\exp(w_{0}+\sum_{i}w_{i}X_{i})}$$
- Por sua vez isto implica que:
$$\frac{P(Y=0|X)}{P(Y=1|X)}=\exp\left(w_{0}+\sum_{i}w_{i}X_{i}\right)$$
logo:
$$\ln \frac{P(Y=0|X)}{P(Y=1|X)}=w_{0}+\sum\limits_{i}w_{i}X_{i}$$
- Ou seja, temos um **_Classificador Linear_**!

### Aplicação
- Ou seja, condiremos um caso de classificação: $$p(\mathcal{C}_{1}|\mathbf{x})=\frac{p(\mathbf{x}|\mathcal{C}_{1})p(\mathcal{C}_{1})}{p(\mathbf{x}|\mathcal{C}_{1})p(\mathcal{C}_{1})+p(\mathbf{x}|\mathcal{C}_{2})p(\mathcal{C}_{2})}=\frac{1}{1+\frac{p(\mathbf{x}|\mathcal{C}_{2})p(\mathcal{C}_{2})}{p(\mathbf{x}|\mathcal{C}_{1})p(\mathcal{C}_{1})}}$$
- Se considerarmos: $z=\ln \frac{p(\mathbf{x}|\mathcal{C}_{1})p(\mathcal{C}_{1})}{p(\mathbf{x}|\mathcal{C}_{2})p(\mathcal{C}_{2})}$ temos:
$$p(\mathcal{C}_{1}|\mathbf{x})=\frac{1}{1+e^{-z}}$$
a isto chamamos de **função sigmoide lógistio** : $\sigma(z)=\frac{1}{1+\exp(-z)}$.
- Podemos demonstrar que: $$z=\ln \frac{\sigma}{1-\sigma}=\ln \frac{p(\mathcal{C}_{1}|\mathbf{x})}{p(\mathcal{C}_{2}|\mathbf{x})}$$
representa o log do ratio entre as probabilidades posteriores.

## Regressão Logística Mais Geral
- Consideremos o caso mais generalizado em que $y\in y_{1}\dots y_{K}$. Queremos determinar os $K-1$ pesos da equação que vimos acima:
$$\begin{align*}
k<K &: &&P(y=y_{k}|\mathbf{x})=\frac{\exp(w_{k}0+\sum_{i=1}^{n}w_{ki}x_{i})}{1+\sum_{j=1}^{K-1}\exp(w_{j0}+\sum_{i=1}^{n}w_{ji}x_{i})}\\
k=K &: &&P(y=y_{k}|\mathbf{x})=\frac{1}{1+\sum_{j=1}^{K-1}\exp(w_{j0}+\sum_{i=1}^{n}w_{ji}x_{i})}\\
\end{align*}$$
## Treinar Regressão Logística
- Definimos: $$P(\mathcal{C}_{1}|\mathbf{x}_{i})=\mu_{i}=\frac{1}{1+\exp(-\mathbf{w}^{t}\mathbf{x}_{i})}~~~~;~~~~ p(\mathcal{C}_{0}|\mathbf{x}_{i})=1-\mu_{i}=\frac{1}{1+\exp(\mathbf{w}^{t}\mathbf{x}_{i})}$$
- Temos a output em estudo $y_{i}\in\{0,1\}$
- Para ajustar usamos uma *função Goal*, que neste caso é **NLL** - Negative Log-Likelihood:
$$\text{NLL}(\mathbf{w})=-\sum\limits_{i=1}^{N}\log \left[ \mu_{i}^{y_{i}}(1-\mu_{i})^{1-y_{i}} \right]=-\sum\limits_{i=1}^{N} \left[y_{i}\log \mu_{i}+(1-y_{i})\log(-\mu_{i}) \right]$$
- Os parâmetros $\mathbf{w}$ ótimos são auqeles em que temos:
$$\mathbf{w} \leftarrow \text{argmin}_\mathbf{w} \left[-\sum\limits_{i=1}^{N} \left[y_{i}\log \mu_{i}+(1-\mu_{i})\log(1-\mu_{i}) \right] \right]$$

### MLE (Maximum Likelihood Estimation)
- Como agora temos mais dimensões, não podemos simplesmente usar MLE de forma direta. Usamos então o *gradiente* e a matriz *hessiana*:
$$\begin{align*}
\text{Gradiente}&: &g&=\sum_{i}(\mu_{i}-y_{i})\mathbf{x}_{i}=X^{t}(\mu-\mathbf{y})\\
\text{Hessiana}&: &H&= X^{t}SX~~~,~~S=\text{diag}(\mu_{i}(1-\mu_{i}))
\end{align*}$$

#### Gradiente
![[descida gradiente.png]]
- Vejamos como pode ser usado um método de descida com gradiente. Temos:
$$\nabla E(\mathbf{w})=\left(\frac{\partial E}{\partial w_{0}},\frac{\partial E}{\partial w_{1}},\cdots, \frac{\partial E}{\partial w_{n}} \right)$$
- Para chegar ao mínimo, usamos um vetor:
$$\Delta \mathbf{w}=-\eta \nabla E$$
em que, claro:
$$\Delta w_{i}=-\eta \frac{\partial E}{\partial w_{i}}$$
e vamos calculando e usando o vetor até chegar ao mínimo (?)

#### Hessiana
- Mas se usarmos a hessiana (que permite ter em conta a curvatura de $E$) podemos chegar ao mínimo de forma mais eficiente.
$$\begin{align*}
\mathbf{w}_{k+1}&= \mathbf{w}_{k}-H^{-1}g_{k}\\
&= \mathbf{w}_{k}+(X^{t}S_{k}X)^{-1}X^{t}(\mathbf{y}-\mu_{k})\\
&= (X^{t}S_{k}X)^{-1}\left[ (X^{t}S_{k}X)\mathbf{w}_{k}+X^{t}(\mathbf{y}-\mu_{k}) \right]\\
&= (X^{t}S_{k}X)^{-1}X^{t} \left[S_{k}X \mathbf{w}_{k}+\mathbf{y}-\mu_{k}\right]
\end{align*}$$
e iteramos este método de modo a chegar ao $\mathbf{w}$ ótimo.

### MAP (Maximum A Posteriori)
- Uma approach para usar este método é definir priors para $W$. Mais especificamente, distribuição normal com média 0 e covariância identidade (Distribuição Normal Padrão multidimensional). Ou seja: $W\sim \text{N}(0,I)$
- Este método evita overfitting
- A estimativa ótima obtida com MAP é:
$$W\leftarrow \text{argmax}_{W}\ln P(W)\prod_{l}P(Y_{l}|\mathbf{x}_{l},W)$$

### MLE vs MAP
- *Estimativa de Max Conditional Likelihood*  (MLE)
$$\begin{align*}
W&\leftarrow \text{argmax}_{W}\ln \prod_{l}P(Y_{l}|X_{l},W)\\
w_{i}&\leftarrow w_{i}+\eta\sum\limits_{l}X_{i}^{l}(Y^{l}-\hat{P}(Y=1|X^{l},W))
\end{align*}$$
- *Estimativa de Max A Posteriori com prior* (MAP)
$$\begin{align*}
W&\sim \text{N}(0,\sigma I)\\
W&\leftarrow \text{argmax}_{W}\ln \left[P(W)\prod_{l} P(Y^{l}|X^{l},W) \right]\\
w_{i}&\leftarrow w_{i}- \eta\lambda w_{i} + \eta\sum\limits_{l} X_{i}^{l}(Y^{l}-\hat{P}(Y^l=1|X^{l},W))
\end{align*}$$

### Regularização de MAP
$$w_{i}\leftarrow w_{i}- \eta\lambda w_{i} + \eta\sum\limits_{l} X_{i}^{l}(Y^{l}-\hat{P}(Y^l=1|X^{l},W))$$
- Nesta equação temos um termo de regularização: $\eta \lambda w_{i}$.
    - Isto ajuda a reduzir overfitting, especialmente quando os dados de treino são muito esparsos
    - Garante que os pesos $\mathbf{w}$ se mantêm próximos dos valores indicados pelos priors
    - Muito usado em regressões logísticas

# Modelos Lineares de Classificação (LDA)
- Temos um dataset $D$ de dados $\{\mathbf{x}_{i},y_{i}\}$ em que $\mathbf{x}_{i}$ são coordenadas no espaço de atributos e $y$ pertence a um conjunto discreto de valores
- *Classificação Binária* consiste no caso em que $y\in\{-1,1\}$ ou  $y\in\{0,1\}$

![[mod lineares de classificacao.png]]
- Ou seja, queremos que
$$y(\mathbf{x})=\mathbf{w}^{T}\mathbf{x}+w_{0}~~~~\mathbf{x}\in\begin{cases}
\mathcal{C}_{1} & ; & y(\mathbf{x})\ge0\\ \mathcal{C}_{2} & ; & y(\mathbf{x})<0
\end{cases}$$
- AKA *Linear Discriminant Analysis* - _**LDA**_.
    - Podemos ver estes classificadores como sendo algo que reduz a dimensão do problema. Um espaço com D-dimensões reduz-se em 1 linha
    - Como podemos ver abaixo, podemos considerar a linha de classificação como a direção em que as projeções ficam melhor separadas.
![[mod linear class resultados 1.png]]
- Tendo em conta isto e a figura, uma opção aparentemente óbvia é usar a reta que une as médias das 2 classes. Mas se as covariância não forem perpendiculares a esta reta (como na figura acima, as classes espalham-se na perpendicular à reta), obtemos isto:
![[mod linear class resultados 2.png|267]]

- Para estas 2 classes a divisão correta seria:
![[mod linear class resultados 3.png]]
ora, esta última versão é o que obtemos com o descriminant de **Fisher**

## LDA de Fisher
- Um LDA "normal" como falamos acima, dividiria as classes de forma a garantir que as médias ficam o mais separadas possíveis. 
- Este LDA, como vemos na imagem acima, foca-se em garantir que as projeções das classes nesta reta são *muito finas*, mesmo que as médias estejam mais próximas.

- A reta que divide as classes é definida como $y=\mathbf{w}^{T}\mathbf{x}$
- Imaginemos que o vetor que une as médias é adequado, logo: $\mathbf{w}\propto \mathbf{m}_{2}-\mathbf{m}_{1}$ 
- $\mathbf{m}_{i}$ são as coordenadas da média da classe $i$, tal que $\mathbf{m}_{i}=\frac{1}{N_{i}}\sum_{n\in\mathcal{C}_{i}}\mathbf{x}_{i}\mathbf{m}_{i}$
    - Podemos definir $m_{2}-m_{1}=\mathbf{w}^{T}(\mathbf{m}_{2}-\mathbf{m}_{1})$, em que $\|\mathbf{w}\|=1$
- Queremos ainda que haja uma baixa variância para cada classe: $s_{k}^{2}=\frac{1}{N_{k}}\sum_{n\in\mathcal{C}_{k}}(\mathbf{w}^{T}\mathbf{x}_{n}-m_{k})^{2}$
- Então a função objetivo de Fisher é:
$$J(\mathbf{w})=\frac{(m_{2}-m_{1})^{2}}{s_{1}^2+s_{2}^{2}}$$
que podemos reescrever como
$$J(\mathbf{w})=\frac{\mathbf{w}^{T}\mathbf{S}_{B}\mathbf{w}}{\mathbf{w}^{T}\mathbf{S}_{W}\mathbf{w}}$$
em que
$$\begin{align*}
\mathbf{S}_{B}&= (\mathbf{m}_{2}-\mathbf{m}_{1})(\mathbf{m}_{2}-\mathbf{m}_{1})^{T}\\
\mathbf{S}_{W}&= \sum\limits_{n\in\mathcal{C}_{1}}(\mathbf{x}_{n}-\mathbf{m}_{1})(\mathbf{x}_{n}-\mathbf{m}_{1})^{T} + \sum\limits_{n\in\mathcal{C}_{2}}(\mathbf{x}_{n}-\mathbf{m}_{2})(\mathbf{x}_{n}-\mathbf{m}_{2})^{T}
\end{align*}$$
e a *solução ótima* é:
$$\mathbf{w}\propto \mathbf{S}^{-1}_{W}(\mathbf{m}_{2}-\mathbf{m}_{1})$$


# Perceptron
- Família de learning machines. O tipo mais comum consiste em funções de base não-lineares seguidos de um LDA
![[perceptron.png]]
ou seja, temos
$$y(\mathbf{x},\mathbf{w})=\text{sgn}(\mathbf{w}^{T}\mathbf{x})$$
que é a mesma coisa que fizemos atrás com o LDA e as linhas a separar classes!

### Superfícies de Separação
- Para um Perceptor, esta superfície consiste numa reta. 
- Pode ser usada para separar variáveis linearmente separáveis (pode representar uma função AND, 1º foto abaixo). Falha se tivermos coisas que não se separam de forma lienar (como uma função XOR, 2º foto)
![[sup separacao.png]]

### Função de Erro
- Podemos contar o número de exemplos mal classificados para avaliar o classificador
- Consideremos que $y\in\{-1,1\}$ e que o classificador ($y(\mathbf{x}_{n})$) dá outputs conforme essa gama.
    - Neste caso, um valor estará mal classificado se $y_{n}\cdot y(\mathbf{x}_{n})<0$ (se estiver bem classificado temos 2 números iguais a multiplicarem-se, pelo que o resultado é positivo)
- Assim, podemos definir a seguinte função de erro:
$$E(\mathbf{w})=-\sum\limits_{i\in \text{mal classificados}}y_{i}\cdot y(\mathbf{x}_{i})$$

### Minimizar erro
- Começamos com pesos $\mathbf{w}$ aleatórios
- Aplicar o perceptron a cada exemplo de treino. Modificar os pesos *sempre* que o perceptron classifica algo mal: $$\mathbf{w}_{t+1}\leftarrow \mathbf{w}_{t}+\Delta \mathbf{w}_{t}~~~~;~~~~ \Delta \mathbf{w}_{t}=\eta(y_{n}-y(\mathbf{x}_{n}))\mathbf{x}_{n}$$
- Repetir isto até que deixemos de ter exemplos mal classificados
- $\eta$ é o *learning rate* - decide quanto os pesos variam
- Só converge se o dataset for separável linearmente
![[evolucao sup separacao.png]]
esta imagem mostra a evolução de $\mathbf{w}$. Na primeira imagem temos a tentativa inicial - seta preta. Na 1ª e 3ª imagem vemos os $\Delta \mathbf{w}$ (setas vermelhas) que são acrescentados a $\mathbf{w}$ para o atualizar.

### Gradiente
- Começamos por substituir a função signal por uma função contínua e derivável: $y(\mathbf{w},\mathbf{x}_{n})=\phi(\mathbf{w}^{t}\mathbf{x}_{n})$
- Temos então
$$\mathbf{w}_{t+1}\leftarrow \mathbf{w}_{t}-\eta \nabla E(\mathbf{w}_{t})$$
em que $\nabla E(\mathbf{w}_{t})=(\frac{\partial E}{\partial w_{1}},\dots, \frac{\partial E}{\partial w_{d}})$
- Mas também temos: $\mathbf{w}_{t+1}\leftarrow \mathbf{w}_{t}-\Delta \mathbf{w}_{t}$
- Assim temos:
$$\Delta \mathbf{w}_{t}=-\eta \nabla E(\mathbf{w}_{t})$$

#### Funções $\phi$
- Algumas funções típicas são:
    - **Sigmoide** $$\phi(z)=\frac{1}{1+e^{-z}}$$
    - **Tangente Hiperbólica** $$\phi(z)=\frac{e^{z}-e^{-z}}{e^{z}+e^{-z}}$$

#### Minimizar erro com gradiente
- Definir $z_{n}=\mathbf{w}^{T}\mathbf{x}_{n}$.
- A output prevista do estimador será: $\phi(z_{n})=\phi(\mathbf{w}^{T}\mathbf{x}_{n})$
- **Online Update**
    - Definimos $E(\mathbf{w})=\frac{1}{2}(\phi(z_{n})-y_{n})^{2}$
    - Teremos o gradiente: $$\frac{\partial E}{\partial \mathbf{w}}=(\phi(z_{n})-y_{n})\frac{\partial \phi}{\partial z_{n}}\frac{\partial z_{n}}{\partial \mathbf{w}}=(\phi(z_{n})-y_{n})\frac{\partial \phi}{\partial z_{n}}\mathbf{x}_{n}$$
- **Batch Update**
    - Temos $E(\mathbf{w})=\frac{1}{2}\sum_{n=1}^{N}(\phi(z_{n})-y_{n})^{2}$
    - Calculamos: $$\frac{\partial E}{\partial \mathbf{w}}=\sum_{n=1}^{N}(\phi(z_{n})-y_{n})\frac{\partial \phi}{\partial z_{n}}\frac{\partial z_{n}}{\partial \mathbf{w}}=\sum_{n=1}^{N}(\phi(z_{n})-y_{n})\frac{\partial \phi}{\partial z_{n}}\mathbf{x}_{n}$$

- Em que temos:
    - *Sigmoide* : $\frac{\partial \phi}{\partial z_{n}}=\phi(1-\phi)$
    - *Tangente Hiperbólica* : $\frac{\partial \phi}{\partial z_{n}}=1-\phi^{2}$
