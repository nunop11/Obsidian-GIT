## Aula 1
### Modelo Linear
- Vimos o previsor linear $Y=\beta_{0}+\beta_{1}X_{1}+\beta_{2}X_{2}+u~~~~,~~ u\sim N(0,\sigma^{2})$ que prevê a resposta $Y$ duma população
    - Sabemos que isto é relativo à população porque temos $u$ a ser uma distribuição. Se fosse para a amostra teríamos *resíduos* escalares
- **A resposta (Y) é contínua** porque $u$ é contínuo
- Assumimos que todos os pontos são independentes 
- Chamamos modelo "linear" porque temos uma combinação linear de $X_{i}$. Como referido na Parte 1, estes podem ser transformações funcionais:
    - Linear: $\beta_{0}+\beta_{1}X_{1}^{2} + \beta_{2}\ln_{12}(X_{2}^{14})$
    - Não Linear: $(\beta_{0}+\beta_{1}X_{1})^{3} + \sqrt{\beta_{2}X_{2}}$
- Como vimos atrás, temos a regressão ao minimizar os RSS (residual sum of squares): 
$$\begin{align*}
\text{RSS}&= \sum\limits_{i=1}^{n} \left[y_{i}- (\beta_{0} + \beta_{1}X_{1} + \beta_{2}X_{2}) \right]^{2}\\
\\
\text{Solução LSS}&: \begin{cases}
\frac{\partial \text{RSS}}{\partial \beta _{0}}=0\to \hat{\beta_{0}}\\
\frac{\partial \text{RSS}}{\partial \beta_{1}}=0\to \hat{\beta_{1}}
\end{cases}
\end{align*}$$
- Estes parâmetros são VAs: com amostras diferentes iremos obter valores diferentes
    - Queremos então determinar $\beta_{0},\beta_{1}$ - os valores para a **população**

### no R
- Fazemos o `fit` com `anova(lm(...))`
- Ao fazer `summary(fit)` e temos:
$$\begin{align*}
\text{variaveis} &&\text{fit} &&\dots &&&\text{p}\\
\text{intercept} &&\dots &&\dots &&&0.072\\
\text{X1} &&\dots &&\dots &&&0.031\\
\end{align*}$$
- Aqui temos:
    - $\text{pvalue}=0.072$ para o teste $H_{0}:\hat\beta_{0}=0$ (H0: B0 não importa). Incercept=B0
    - $\text{pvalue}=0.031$ para o teste $H_{0}:\hat\beta_{1}=0$ (H0: a variável X1 não afeta o modelo)
- **NUNCA REMOVER B0 DO MODELO**

- Com *2 variáveis*:
$$\begin{align*}
\text{variaveis} &&\text{df} &&&\text{sum squares} &&\dots &&&\text{p}\\
\dots &&X &&&\text{BSS}_{1} &&\dots &&&\text{pv}_{1}\\
\dots &&Y &&&\text{BSS}_{2}&&\dots &&&\text{pv}_{2}\\
\text{residuals} &&Z &&&\text{WSS}&&\dots &&&\text{pv}_{0}\\
\end{align*}$$

### Amostragem
- Se fizermos $N$ amostras e, em cada uma, aplicarmos o modelo linear para determinar $\hat\beta_{1}^{~i}$
- Se fizermos um histograma, ele estará centrado no $\beta_{1}$ da população. Mas para isto ser conclusivo precisamos de CENTENAS de amostras

## Aula 2 (Sofia)
### Kruskal-Wallis
- Teste Kruskal-Wallis: usado com dados ordinais ou dados contínuos não-normais
- Testa se as distribuições de 3+ amostras são diferentes; $H_{0}:\text{todos os grupos têm da mesma distribuição}$

### ANOVA
![[ANOVA desenho.png]]
- Definimos algo assim. Temos:
    - Resposta $Y$
    - Fator que estudamos. Para o fator temos 4 tratamentos/níveis
    - As medições dos 4 níveis têm médias $\hat{\mu}_{i}$
    - Definimos o nível do fator como $j$ e a réplica/unidade experimental dentro dedsse fator como $i$
- Queremos testar se $H_{0}:\mu_{1}=\mu_{2}=\mu_{3}=\mu_{4}$
- Podemos modelar isto de 2 formas:
$$\begin{align*}
Y_{ij}&= \mu_{j} + u_{ij}\\
&= \mu + \alpha_{j} + u_{ij} ~~~~~~;~~~~ \sum_{j}\alpha_{j}=0
\end{align*}$$
- A segunda opção muitas vezes é melhor! Porque nesta temos uma média global $\mu$ e podemos estudar o efeito fixo que cada tratamento $j$ introduz: $\alpha_{j}$

### EX: Máquinas
- Temos as máquinas A,B,C. Cada uma mede amostras diferentes e independentes.
- Usamos ANOVA1 clássico, porque tudo é independente e a resposta contínua. Estudamos então se as 3 máquinas introduzem um certo efeito fixo nas medições
- Para estudar as máquinas em si, usamos ANOVA com repetições: cada amostra é medida por todas as máquinas. Nesse caso temos a amostra a funcionar como um bloco.

### Design Fatorial $2^{3}$
- Temos 3 fatores, 2 categorias para cada
- Por exemplo: estudar o comportamento de 2 metais (fator 1) a 2 temperaturas diferentes (fator 2) com diferentes tratamentos de cura (fator 3).
- Temos ANOVA1:
$$Y_{ij}=\mu+\alpha_{j} + u_{ij}~~~~~~;~~~~\sum\limits_{j=1}^{3}\alpha_{j}=0~~,~~u_{ij}\sim N(0,\sigma^{2})$$
- E em design $2^{3}$ temos:
    - $i$ - replicas
    - $j$ - nivel do fator 1
    - $k$ - nivel do fator 2
    - $l$ - nível do fator 3
$$Y_{ijkl}=\mu+\alpha_{j}+\beta_{k}+\gamma_{l}+u_{ijkl}~~~~~~;~~~~ \begin{cases}
u_{ijkl}\sim N(0,\sigma^{2}) \\
\sum_{j}\alpha_{j}=0 \\
\sum_{k}\beta_{k}=0 \\
\sum_{l}\gamma_{l}=0
\end{cases}$$

### Interação em gráfico
![[interacao a partir de grafico.png]]
- Temos aqui um estudo de PAS (pressão artelial sistólica) em:
    - Homens vs Mulheres (eixo X)
    - Sujeito Normal vs Vegetariano (retas diferentes)
- Ora, vemos que as retas muito claramente se intersetam: *existe interação* entre Dieta e Género.
- **Interação só existe com > 1 rélicas**

### Desenho de Blocos Randomizados Completos
- Bloco = Grupo de unidades homogéneas

### Variância
- Num modelo do tipo
$$Y_{ij}=\mu + a_{i} + u_{ij}~~~~~~;~~~~ a\sim N(0,\sigma_{a}^{2})~,~u_{ij}\sim N(0,\sigma^{2})$$
- Temos aqui a variância da resposta: $\text{Var}[Y_{ij}]=\sigma_{a}^{2}+\sigma^{2}$
- E temos a *proporção de variância causada pelo fator i*: $$\text{ICC (Intra Class Correlation)}=\frac{\sigma_{a}^{2}}{\sigma_{a}^{2}+\sigma^{2}}$$
Tem este nome porque:
$$\text{Corr}(Y_{ij},Y_{kl})=\begin{cases}
0 & ; & i\neq k \\
\text{ICC} & ; & i=k,j\neq l \\
0 & ; & i=k, j=l
\end{cases}$$

#### no R
- Teremos algo do tipo:
$$Y_{ij}=\mu + a_{i} + u_{ij}$$
que no R nos dá:
$$\begin{align*}
\text{variavel} &&& \text{variance} && \text{std error}\\
\text{touros} &&& 116 && ...\\
\text{residuals} &&& 463 && ...
\end{align*}$$
em que $i$ corresponde ao fator "touro".
- Temos então $\sigma_{a}^{2}=116, \sigma^{2}=463$

## Aula 3
- Foi tudo só exemplos

## Aula 4
### Medições repetidas
- Temos 50 pessoas: 23H, 27M
- Em cada pessoa foram feitas 3 medições com 1 minuto de intervalo
    - Temos medições **DEPENDENTES** e não aleatórias
- Resposta e fatores:
    - Medimos $Y$ = PAS (pressão arterial) 
    - $i$ é a pessoa $i=1,\dots,50$
    - $j$ é a medição $j=1,2,3$
    - $k$ é o sexo (2 valores)

- Temos:
$$Y_{ijk}=\mu + a_{i} + \beta_{k} + u_{ijk}$$
- Notas:
    - Cada pessoa é um efeito random porque as pessoas são escolhidas random
    - Temos 1 efeito fixo de cada sexo, porque só existem 2 opções, que conhecemos

### Medições longitudinais
$$Y_{ij}=\mu + a_{i} + \beta_{j} + u_{ij}$$
- Notas:
    - $i$ é o índice da pessoa testada, escolhida random
    - $j$ é o índice do dia/intervalo de tempo da medição. Conhecido e fixo
    - Neste modelo temos 1 medição por pessoa por dia logo não temos interação $(a \beta)_{ij}$

### Efeitos nested 
- **NÃO EXISTE INTERAÇÃO**
- Para o caso em que temos uma hierarquia clara: Escola > Turma > Estudante

### Efeitos crossed
- Pode haver sistema em que temos combinação de interação/crossed e nested
- Podemos ter algo assim:
![[efeitos crossed.png]]
em que temos 1 medição por combinação I,M. Mas NÃO temos interação apesar do gráfico o indicar.
