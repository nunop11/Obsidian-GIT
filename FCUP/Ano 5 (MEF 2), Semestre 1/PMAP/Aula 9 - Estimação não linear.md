No final da aula anterior vimos que podemos definir um filtro de Kalman em steady state a partir desta assunção:
$$(x|z=z_{0})\sim N(x^{+},P^{+})$$

## Estimação não linear
- Começamos por assumir/considerar que
$$x\sim N(\mu, P)~~~~,~~~~ z=h(x)$$
em que, novamente, $x$ é o estado do sistema que NÃO conhecemos. O nosso objetivo com este estudo é determinar $\mu,P$ de modo a poder definir o sistema.

- A PDF de $z$ será dada por:
$$p(z)=\det(\mathcal{J}(z)) N(h^{-1}(z)|\mu,P)$$
em que $\mathcal{J}(z)$ é a matriz jacobiana de $h^{-1}(z)$, assumindo-se que $h(\cdot)$ é invertível. Notemos que esta variável continua a seguir a distribuição normal com média $\mu$ e variância $P$. Ou seja, podemos *estudar z para determinar x*!!! 

- Vamos redefinir $x$ como um sinal em torno da sua média: $$x=\mu+\delta x~~~~,~~~\delta x\sim N(0,P)$$
e podemos expandir $z$ em Taylor:
$$z=h(x)=h(\mu+\delta x)\approx h(\mu)+ \frac{dh(\mu)}{dx}\delta x+\dots$$

### Média
- Podemos calcular o valor médio de $z$:
$$\begin{align*}
\mathbb{E}[z]&= \mathbb{E}[h(x)]=\mathbb{E}[h(\mu+\delta x)]\\
&\approx \mathbb{E}\left[h(\mu) + \frac{dh(\mu)}{dx}\delta x \right] \\
&= h(\mu) + \frac{dh(\mu)}{dx}\mathbb{E}[\delta x]=h(\mu)+\frac{dh(\mu)}{dx}P\\
\mathbb{E}[z]&\approx h(\mu)
\end{align*}$$
em que, obviamente, esta aproximação será **melhor** quão **menor** for $P$.

### Covariância
$$\begin{align*}
\text{cov}[z]&= \text{cov}[h(x)]\\
&= \mathbb{E}\left[(h(x)-\mathbb{E}[h(x)]) (h(x)-\mathbb{E}[h(x)])^{T} \right]\\
&\approx \mathbb{E}\left[(h(x)-h(\mu))(h(x)-h(\mu))^{T} \right]\\
&\approx \mathbb{E}\left[\left(\frac{dh(\mu)}{dx}\delta x \right)\left(\frac{dh(\mu)}{dx}\delta x \right)^{T} \right]\\
&= \frac{dh(\mu)}{dx} \mathbb{E}[\delta x \delta x^{T}]\left(\frac{dh(\mu)}{dx}\delta x \right)^{T}\\
&= \left(\frac{dh(\mu)}{dx}\delta x \right)P\left(\frac{dh(\mu)}{dx}\delta x \right)^{T}\\
&= h_{x}(\mu)Ph_{x}^{T}(\mu)
\end{align*}$$

### Distribuição conjunta
- Por vezes é mais útil estudar a distribuição de $\begin{pmatrix}x \\ z\end{pmatrix}$
- Temos o valor médio:
$$\mathbb{E}\left[\begin{pmatrix}h \\ z\end{pmatrix}\right]=\begin{pmatrix}\mu \\ h(\mu)\end{pmatrix}$$
e temos a covariância:
$$\begin{align*}
\text{cov}\left[\begin{pmatrix}x\\
z=h(x)\end{pmatrix} \right]&\approx \mathbb{E}\left[\left(\begin{bmatrix}x\\
h(x)\end{bmatrix}-\begin{bmatrix}\mu\\
h(\mu)\end{bmatrix}\right)\left(\begin{bmatrix}x\\
h(x)\end{bmatrix}-\begin{bmatrix}\mu\\
h(\mu)\end{bmatrix}\right)^{T}\right]\\
&\approx \mathbb{E} \left[ \begin{bmatrix}\delta x\\
h_{x}(\mu)\delta x\end{bmatrix} \begin{bmatrix}\delta x\\
h_{x}(\mu)\delta x\end{bmatrix}^{T} \right]\\
&= \mathbb{E}\left[ \begin{bmatrix}I\\
h_{x}(\mu)\end{bmatrix}\delta x \delta x^{T} \begin{bmatrix}I\\
h_{x}(\mu)\end{bmatrix}^{T} \right]\\
&= \begin{bmatrix}I\\
h_{x}(\mu)\end{bmatrix} P \begin{bmatrix}I\\
h_{x}(\mu)\end{bmatrix}^{T}\\
&= \begin{bmatrix}P & Ph_{x}^{T}(\mu)\\
h_{x}(\mu)P & h_{x}(\mu)Ph_{x}^{T}(\mu)\end{bmatrix}
\end{align*}$$
- Isto é então a **aproximação linear a primeira ordem** - ficamos apenas com o primeiro termo da série de Taylor. Isto pode ser feito para ordens maiores, mas a matemática fica muito mais complexa e mais difícil de computar.
- Notemos, claro, que isto é aplicável em qualquer sistema em que $z=h(x)$ desde que $h(\cdot)$ seja invertível!!

### Modelo prático
- Temos então:
$$x\sim N(\mu,P)~~~~,~~~~ q\sim N(0,Q)~~~~,~~~~ \text{x e q independentes}$$
e temos agora o mesmo caso que acima, com ruído:
$$z=h(x)+q$$
- Ao fazer como acima a aproximação de 1ª ordem obtemos:
$$\begin{pmatrix}x \\ z\end{pmatrix}\sim N \left( \begin{bmatrix}\mu \\ \mu_{L}\end{bmatrix}~,~\begin{bmatrix}P & C_{L} \\ C_{L}^{T} & S_{L}\end{bmatrix} \right)$$
e temos
$$\begin{align*}
\mu_{L}&= h(\mu)\\
C_{L}&= Ph_{x}^{T}(\mu)\\
S_{L}&= h_{x}(\mu)Ph_{x}^{T}(\mu)+Q
\end{align*}$$
- Ora, consideramo que se fez uma medição $z=a$. Podemos aproximar o estado atal a uma distribuição normal:
$$\begin{align*}
(x|z=a)&\sim N(\overline{\mu},\overline{P})\\
K &= C_{L}S_{L}^{-1}\\
\overline{\mu}&= \mu+K(a-\mu_{L})\\
\overline{P}&= P^{-}-KC_{L}^{T}
\end{align*}$$

## Extended Kalman (EKF)
- Podemos definir o sistema como $x_{k}=f(x_{k-1})+w_{k-1}$
    - $f(\cdot)$ é uma qualquer função que descreve a dinâmica do sistema (pode não ser linear!!!). Como
- E podemos modelar as medições com outra função $z_{k}=h(x_{k})+v_{k}$
- Notemos que na realidade as funções são $f(\cdot)\equiv f_{k}(\cdot),h(\cdot)\equiv h_{k}(\cdot)$ mas não mostramos isso por simplicidade
- Temos
    - $w_{k}\sim N(0,Q_{k})$ e $v_{k}\sim N(0,R_{k})$
    - $x_{0}\sim N(\mu_{0},P_{0})$

### Aproximação
- Este método consiste em aproximar um estado em que conhecemos a medição a:
$$(x_{k}|z_{1:k})\simeq N(x_{k}|\mu_{k},P_{k})$$
- Assim, podemos fazer a previsão básica da distribuição da próxima iteração, usando a dinâmica do sistema:
$$\mu_{k}^{-}=f(\mu_{k-1}) \quad;\quad P_{k}^{-}=f_{x}(\mu_{k-1})P_{k-1}f_{x}^{T}(\mu_{k-1})$$
- E temos a correção, que segue formas parecidas ao que vimos acima:
$$\begin{align*}
S_{k}&= h_{x}(\mu_{k}^{-})P_{k}^{-}h_{x}^{T}(\mu_{x}^{-}) + R_{k}\\
K_{k}&= P_{k}^{-}h_{x}^{T}(\mu_{k}^{-})S_{k}^{-1}\\
\mu_{k}&= \mu_{x}^{-}+K_{k}(z_{k}-h(\mu_{k}^{-}))\\
P_{k}&= P_{k}^{-}-K_{k}S_{k}K_{k}^{T}
\end{align*}$$
obtendo $\mu_{k},P_{k}$ que nos dão a distribuição de $x_{k}$
- Este método tenta linearizar o sistema $f(x)$. Enquanto sabemos que o filtro de Kalman normal dá **sempre** a solução óptima, o EKF pode não funcionar de todo.

## Transformada unsected (sem cheiro)
- Novamente, assumimos $x\sim N(\mu,P)$ e $z=h(x)$ (sem ruído)

### Sigma
- Começamos por definir e calcular $2n+1$ pontos sigma:
$$\begin{align*}
\chi_{0}&= \mu\\
\chi_{i}&= \mu+ \sqrt{n+\lambda} [\sqrt{P}]_{i} \quad;\quad i=1,\dots,n\\
\chi_{i+n}&= \mu- \sqrt{n+\lambda} [\sqrt{P}]_{i} \quad;\quad i=1,\dots,n\\
\end{align*}$$
- Notemos algumas coisas aqui:
    - $\sqrt{P}(\sqrt{P})^{T}=P$
    - $[\sqrt{P}]_{i}$ é a coluna $i$ da matriz $\sqrt{P}$
    - Definimos $\lambda=\alpha^{2}(n+\kappa)-n$ 
    - Temos aqui $\alpha,\kappa$ que são parametros de ajuste que veremos mais à frente
    - Notemos, como sempre, $n$ é a **dimensão do vetor de estado**

### Propagar
- Estes pontos sigma são pontos que resumem muito caraterísticamente o comportamento da distribuição de pontos
- De seguida vamos propagá-los na função $h$. Consideremos $$Z_{i}=h(\chi_{i}) \quad;\quad i=0,1,\dots,2n$$

### Estatísticas
- Podemos deduzir a média e covariância deste conjunto de pontos sigma:
$$\begin{align*}
\mathbb{E}[h(x)]&\approx \mu_{U}=\sum\limits_{i=0}^{2n}W_{i}^{(m)}Z_{i}\\
\text{cov}[h(x)]&\approx S_{U}= \sum\limits_{i=0}^{2n}W_{i}^{(c)}(Z_{i}-\mu_{U})(Z_{i}-\mu_{U})^{T}
\end{align*}$$
e definimos os pesos:
$$\begin{align*}
W_{0}^{(m)}&= \frac{\lambda}{\lambda+n}\\
W_{0}^{(c)}&= \frac{\lambda}{\lambda+n} + (1-\alpha^{2}+\beta)\\
W_{i}^{(m)}=W_{i}^{(c)}&= \frac{1}{2(n+\lambda)}~~~~,~~ i=1,2,\dots,2n
\end{align*}$$
em que $\beta$ é o terceiro parâmetro de ajuste

### NOTAS
- $\sqrt{P}$ é a decomposição de Cholesky de $P$. Isso significa que
    - é única quando $P$ é definido positivo 
    - pode não ser única se $P$ for semidefinido positivo
    - em matlab usamos `chol(P, 'lower')`
- Como vimos, $\alpha,\beta,\kappa$ são parâmetros de refinação
    - $\alpha$ é normalmente reduzido: 0.001-0.1
    - $\beta=2$ é óptimo quando *sabemos* que a distribuição é gaussiana
    - $\kappa=0$ é uma escolha boa em muitos casos

### Exemplo
- Vejamos um exemplo. Pegou-se numa distribuição normal
![[unscented.png]]
$$\begin{pmatrix}x \\ y\end{pmatrix}\sim N \left(\begin{bmatrix}10 \\ 10\end{bmatrix}, \begin{bmatrix}64 & 0  \\ 0 & 1\end{bmatrix} \right)$$
e temos algo muito mais estreito nos Y do que nos X.
- Ora, vamos tornar isto em algo irregular ao converter os pontos para o espaço polar:
$$\begin{pmatrix}r \\ \theta\end{pmatrix}=\begin{pmatrix}\sqrt{x^{2}+y^{2}} \\ \text{atan2}(y,x)\end{pmatrix}$$
e temos aqui os resultados de EKF (linearização), unscented e monte carlo:
![[comparacao metodos.png]]

## UKF (Unscented Kalman)
### A aproximação
- Assumimos que:
$$\begin{align*}
x&\sim N(\mu,P)\\
z&= h(x)+q\\
q&\sim N(0,Q)
\end{align*}$$
em que $x,z$ são independentes

- A probabilidade conjunta sem cheiro será:
$$\begin{pmatrix}x \\ z\end{pmatrix}\sim N \left(\begin{bmatrix}\mu \\ \mu_{U}\end{bmatrix}, \begin{bmatrix}P & C_{U} \\ C_{U}^{T} & S_{U}\end{bmatrix} \right)$$
(como vimos acima no caso geral)
- Definimos:
$$\begin{align*}
\mu_{U}&= \sum\limits_{i=0}^{2n}W_{i}^{(m)}Z_{i}\\
S_{U}&=  \sum\limits_{i=0}^{2n}W_{i}^{(c)}(Z_{i}-\mu_{U})(Z_{i}-\mu_{U})^{T}+Q\\
C_{U}&= \sum\limits_{i=0}^{2n}W_{i}^{(c)}(\chi_{i}-\mu)(Z_{i}-\mu_{U})^{T}
\end{align*}$$

### O filtro
- Temos o sistema $x_{k}=f(x_{k-1})+w_{k-1}$
- E temos as medições dadas por $z_{k}=h(x_{k})+v_{k}$
- E temos a aproximação do ponto acima: $(x_{k}|z_{1:k})\sim N(x_{k}|\mu_{k},P_{k})$

#### Previsão
**1.** Começamos por definir os pontos sigma:
$$\begin{align*}
\chi_{k-1,0}&= \mu_{k-1}\\
\chi_{k-1,i}&= \mu_{k-1}+\sqrt{n+\lambda}[\sqrt{P_{k-1}}]_{i} ~~~~,~~i=1,2,\dots,n\\
\chi_{k-1,i+n}&= \mu_{k-1}-\sqrt{n+\lambda}[\sqrt{P_{k-1}}]_{i}~~~~,~~i=1,2,\dots,n
\end{align*}$$
**2.** Propagar os pontos sigma no modelo:
$$\hat{\chi}_{k,i}=f(\chi_{k-1,i})~~~~,~~ i=0,1,\dots,2n$$
**3.** Calcular a média e covariância estimadas com estes pontos
$$\begin{align*}
\mu_{k}^{-}&= \sum\limits_{i=0}^{2n}W_{i}^{(m)}\hat{\chi}_{k,i}\\
P_{k}^{-}&= \sum\limits_{i=0}^{2n}W_{i}^{(c)}(\hat{\chi}_{k,i} - \mu_{k}^{-})(\hat{\chi}_{k,i} - \mu_{k}^{-})^{T}+Q
\end{align*}$$
em que $W_{0}^{(m)}= \frac{\lambda}{\lambda+n}~,~W_{0}^{(c)}= \frac{\lambda}{\lambda+n} + (1-\alpha^{2}+\beta)~,~W_{i}^{(m)}=W_{i}^{(c)}= \frac{1}{2(n+\lambda)}$

#### Correção
**1.** Recalcular os pontos sigma, agora a partir da estimativa da covariância:
$$\begin{align*}
\chi_{k-1,0}^{-}&= \mu_{k-1}^{-}\\
\chi_{k-1,i}^{-}&= \mu_{k-1}^{-}+\sqrt{n+\lambda}\left[\sqrt{P_{k-1}^{-}}\right]_{i} ~~~~,~~i=1,2,\dots,n\\
\chi_{k-1,i+n}^{-}&= \mu_{k-1}^{-}-\sqrt{n+\lambda}\left[\sqrt{P_{k-1}^{-}}\right]_{i}~~~~,~~i=1,2,\dots,n
\end{align*}$$

**2.** Propagar estes pontos pelo modelo das medições
$$\hat{Z}_{k,i}=h(\chi_{k,i}^{-})~~~~,~~i=0,1,\dots,2n$$

**3.** Calcular a média, covariância e covariância cruzada:
$$\begin{align*}
\hat{z}_{k}&= \sum\limits_{i=0}^{2n}W_{i}^{(m)}\hat{Z}_{i}\\
S_{k}&= \sum\limits_{i=0}^{2n}W_{i}^{(c)}(\hat{Z}_{i}-\hat{z}_{k})(\hat{Z}_{i}-\hat{z}_{k})^{T}+R\\
C_{k}&= \sum\limits_{i=0}^{2n}W_{i}^{(c)}(\chi_{k,i}^{-} - \mu_{k}^{-})(\hat{Z}_{i}-\hat{z}_{k})^{T}
\end{align*}$$

**4.** Calcular o filtro de novo. Obtemos o ganho, média e covariância:
$$\begin{align*}
K_{k}&= C_{k}S_{k}^{-1}\\
\mu_{k}&= \mu_{k}^{-}+K_{k}(z_{k}-\hat{z}_{k})\\
P_{k}&= P_{k}^{-} - K_{k}S_{k}K_{k}^{T}
\end{align*}$$
Estes valores serão usados no passo 1 da estimação, acima. Claro, quando passarmos à próxima iterção este valor $P_{k}$ será $P_{k-1}$ na fórmula dos pontos sigma.