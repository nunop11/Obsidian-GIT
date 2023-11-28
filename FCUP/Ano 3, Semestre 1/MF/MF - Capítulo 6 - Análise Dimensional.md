## 6.1 - Intro
- Muitos problemas de Mec Fluídos podem ser resolvidos analiticamente, mas alguns têm que ser resolvidos experimentalmente ou através de uma mistura experimental+analítico. Veremos neste capítulo técnicas que permitem fazer isto.

- Consideremos um caso simples: fluido newtoniano, incompressível, em estado estacionário a escoar num tubo circular horizontal de secção reta constante. Queremos determinar a perda de pressão por unidade de comprimento de tubo devido à viscosidade do fluido.
- Primeiro temos que determinar quais as variáveis que afetam a perda de pressão por unidade de comprimento. temos que essas variáveis são: $D$ (diametro tubo), $\rho$ (densidade do fluido), $\mu$ (viscosidade do fluido) e $v$ (velocidade média do fluido). Temos portanto:
$$\frac{\Delta p}{l}=f(D,\rho,\mu,v)$$
pelo que o que pretendemos determinar é a função $f$.
- Assim, devemos realizar várias experiências, em que verificamos qual a perda de pressão, alterando 1 variável e mantendo as outras constantes. Ora, isto pode ser muito difícil ou até impossível (por exemplo, é muito complicado arranjar vários fluidos com a mesma massa volúmica mas com viscosidades diferentes).

- Fazendo experiências assim, para o sistema em estudo indicado, obtemos os seguintes gráficos:
![[Pasted image 20231127222112.png]]
- Ora, pode ser muito difícil obter destes gráficos uma função $f(D,\rho,\mu,v)$.

- Assim, usamos a *Análise Dimensional*.
- No exemplo do fluido no tubo acima obtemos da análise dimensional: $$\frac{D \frac{\Delta p}{l}}{\rho v^{2}}=\phi\left(\frac{\rho v D}{\mu}\right)$$
Ora, isto permite que, ao fazer o estudo experimental deste problema, não é preciso alterar 1 variável e manter 3 constantes. Aqui apenas temos 2 "variáveis" AKA 2 *grupos adimensionais*. Assim, basta variar $\frac{\rho vD}{\mu}$ e medir os valores de $\frac{D \frac{\Delta p}{l}}{\rho v^{2}}$ equivalentes e temos:
![[Pasted image 20231127223227.png|350]]
ora, esta curva é universal. Podemos fazer a experiência para um qualquer fluido de propriedades $\rho,\mu$ e num qualquer tubo de diâmetro $D$, desde que se varie a velocidade $v$.

- Podemos verificar que estes 2 grupos adimensionais são, de facto, adimensionais:
$$\begin{align*}
\frac{D \frac{\Delta p}{l}}{\rho v^{2}}&= \frac{L \frac{\left[\frac{F}{A}\right]}{L}}{\frac{M}{V}(\frac{L}{T})^{2}}=\frac{\frac{M}{L^{2}} \frac{L}{T^{2}}}{\frac{M}{L^{3}} \frac{L^{2}}{T^{2}}}=L^{0}M^{0}T^{0}\\
\frac{\rho vD}{\mu}&= \frac{\frac{M}{V} \frac{L}{T} L}{\frac{M}{Lt}}=\frac{\frac{M}{L^{3}} \frac{L}{T} L}{\frac{M}{Lt}}=M^{0}L^{0}T^{0}
\end{align*}$$
(A notação tá muito inconsistente mas intende-se ig)

## 6.2 - Análise Dimensional
### 6.2.1 - Teorema de $\Pi$ Buckingham
- O teorema de Pi Buckingham é uma equação dimensionalmente homogénea (equação em que os lados esquerdo e direito têm a mesma dimensão) que envolve $k$ variáveis e que pode ser transformada numa relação entre $k-r$ grupos adimensionais independentes. $r$ é o número mínimo de dimensões fundamentais necessárias para descrever as variáveis.
- Na maioria dos problemas de Mec Fluidos, qualquer variável pode ser escrita recorrendo às dimensões $L,M,T$.

- Consideremos que $\Pi_{i}$ é o grupo adimensional $i$. Chamaremos $u_{i}$ à variável $i$ (não necessariamento relacionado ao grupo adimensional $i$). 
- O teorema de Pi Buckingham diz-nos que a equação que relaciona as variáveis:
$$u_{1}=f(u_{1},u_{2},\dots,u_{k})$$
pode ser rearranjada na seguinte forma:
$$\Pi_{1}=\phi(\Pi_{2},\Pi_{3},\dots,\Pi_{k-r})$$

- Vejamos então como determinar os grupos adimensionais $\Pi_{i}$
#### Determinação dos $\Pi_{i}$
**Passo 1 - Listagem das variáveis envolvidas no problema**
- Este passo requere conhecimento dos processos físicos envolvidos no sistema em estudo.
- Normalmente são incluidas:
    - Variáveis que descrevem a geometria do sistema (dimensões do tubo)
    - Variáveis de definem as propriedades do fluido (viscosidade, massa volúmica, tensão superficial, etc)
    - Variáveis que descrevem o efeito de forças exteriores no sistema (aceleração da gravidade, gradiente de pressão, etc)
- É especialmente importante que as variáveis escolhidas sejam **independentes**
- *Exemplo* : $\frac{\Delta p}{l}=f(D,\rho,\mu,v)$

**Passo 2 - Exprimir cada variável em função das dimensões fundamentais**
- Simplesmente escrever as variáveis em termos das 3 dimensões fundamentais: $L,M,T$.
- *Exemplo* : $\frac{\Delta p}{l}=MT^{-2}L^{-2}~~,~~D=L~~,~~\rho=ML^{-3}~~,~~\mu=MT^{-1}L^{-1}~~,~~v=LT^{-1}$

**Passo 3 - Determinar o número de termos $\Pi_{i}$ necessários**
- Pelo teorema de Pi Buckingham, o número de termos $\Pi_{i}$ necessários é $k-r$. $k$ é o número de variáveis listadas no passo 1. $r$ é o número de dimensões fundamentais necessárias para descrever essas variáveis (normalmente teremos $r=3$).
- *Exemplo* : temos $k=5$ variáveis e usamos $r=3$ dimensões fundamentais para as definir. Pelo teorema de Pi Buckingham, podemos definir 3 grupos adimensionais.

**Passo 4 - Selecionar um número de variáveis igual ao das dimensões fundamentais**
- Da lista de variáveis do passo 1, seleciona-se um número de variáveis igual ao número de dimensões fundamentais. Usaremos essas $r$ variáveis para fazer grupos adimensionais.
- As variáveis escolhidas não devem formar um grupo adimensional ao ser combinadas entre si. Devem formar um grupo adimensional quando combinadas com uma outra variável (ver passo seguinte) !
- Não devemos escolher a variável em estudo.
- *Exemplo* : Temos $r=3$, pelo que escolhemos 3 variáveis. Não devemos escolher $\Delta p/l$ . Assim, escolhemos $D,v,\rho$.

**Passo 5 - Formar termos $\Pi_{i}$**
- Para isso, multiplicamos uma variável não selecionada no passo 4 pelas variáveis selecionadas, cada uma elevada a um expoente. Esse produto tem que ser adimensional.
- *Exemplo* :
Definimos o grupo adimensional:
$$\Pi_{i}=\frac{\Delta p}{l}D^{a_{1}}v^{b_{1}}\rho^{c_{1}}$$
e temos:
$$(ML^{-2}T^{-2}) (L)^{a_{1}}(LT^{-1})^{b_{1}}(ML^{-3})^{c_{1}}=M^{0}T^{0}L^{0} \to \begin{cases}
1+c_{1}=0\\-2-b_{1}=0\\-2+a_{1}+b_{1}-3c_{1}=0
\end{cases}$$
e obtemos $a_{1}=1,b_{1}=-2,c_{1}=-1$. Resulta o grupo adimensional: $\Pi_{i}=\frac{\frac{\Delta p}{l}D}{\rho v^{2}}$

**Passo 6 - Repetir o passo 5 com todas as variáveis não selecionadas**
- *Exemplo* :
Tomando agora a variável não selecionada $\mu$ obtemos o grupo $\Pi_{2}=\frac{\mu}{\rho vD}$

**Passo 7 - Verificar se todos os grupos obtidos nos passos 5 e 6 são mesmo adimensionais**

**Passo 8 - Escrever a função que relaciona os grupos adimensionais**
- No grupo $\Pi_{1}$ deve aparecer no numerador a variável em estudo (daí no *exemplo* termos definido os grupos assim).
- Cada grupo adimensional pode ser rearranjado, invertido ou multiplicado por outro grupo.

## 6.3 - Grupos Adimensionais Comuns
**Número de Reynolds** - Mede relação entre forças de inérica e forças viscosas que atuam num elemento de fluido. Permite distinguir entre escoamentos laminares e turbulentos (valor alto -- forças inércia sobrepõe forças viscosas -- escoamento turbulento)
$$\text{Re}=\frac{l^{2}v^{2}\rho}{lv\mu }=\frac{lv\rho}{\mu}$$

**Número de Froude** - Razão entre forças de inérica e força da gravidade que atuam em elemento de fluido. Útil quando temos escoamentos com superfície livre, escoamentos abertos para a atmosfera (como em rios, canais, em torno de barcos, etc).
$$\text{Fr}=\frac{l^{2}v^{2}\rho}{\rho g l^{3}}=\frac{v^{2}}{gl}=\frac{v}{\sqrt{gl}}$$

**Número de Euler** - Razão entre forças de pressão e forças de inércia que atuam em elemento de fluido
$$\text{Eu}=\frac{l^{2}p}{\rho v^{2}l^{2}}\to C_{f}\frac{p}{\rho v^{2}}=\frac{\Delta p}{\frac{1}{2} \rho v^{2}}$$
(sendo a última variante do número de Euler normalmente chamada *coeficiente de atrito* $C_{f}$)

**Número de Mach e de Cauchy** - Razão entre forças de inércia e forças de compressão que se exercem num elemento de fluido
$$\text{Ca}=\frac{\rho l^{2}v^{2}}{\rho v^{2} c^{2}}\to \text{Ma}=\frac{v}{c}$$($c$ é a velocidad o som. $\text{Ma}$ é literalmente a velocidade em Mach. Quando $\text{Ma}$ é reduzido, as forças de compressão não fortes o suficiente para alterar $\rho$)

**Número de Webber** - Razão entre forças de inércia e forças de tensão superficial. Importante em escoamentos comobolhas de gás e gotas em ascensão num líquido.
$$\text{We}=\frac{\rho l^{2}v^{2}}{\sigma l}\to \text{Ma}=\frac{\rho l v^{2}}{\sigma}$$

## 6.4 - Correlação de Dados Experimentais
- No livro temos um exemplo a mostrar como podemos obter uma função do tipo$\Pi_{1}=f(\Pi_{2})$ a partir dos dados experimentais.

## 6.5 - Teoria dos Modelos
### 6.5.1 - Semelhança cinemática, dinâmica e geométrica
- Consideremos que temos um protótipo $p$ em que se verifica a relação:
$$\Pi_{1,p}=\phi(\Pi_{2,p},\Pi_{3,p},\dots,\Pi_{n,p})$$
- Para um modelo $m$ à escala (pensar num modelo de um carro de F1 usado para testes) deveremos ter uma relação semelhante
$$\pi_{1,m}=\phi(\Pi_{2,m},\Pi_{3,m},\dots,\Pi_{n,m})$$
- Se fizemos o estudo garantindo que $\Pi_{2,m}=\Pi_{2,p}~,~\Pi_{3,m}=\Pi_{3,p}~,\dots$ então temos necessariamente $\Pi_{1,m}=\Pi_{1,p}$. Ou seja, se garantirmos que os grupos adimensionais conhecidos são iguais no modelo e no protótipo, podemos determinar a variável em estudo através do modelo e isso irá aplicar-se ao protótipo.
- Assim:
*Semelhança Geométrica* - ao igualar grupos adimensionais com dimensões geométricas, torna-se necessário que haja semelhança geométrica entre protótipo e modelo : o modelo tem que ser à escala do protótipo.
*Semelhança Dinâmica* - ao igualar grupos adimensionais que representam forças (Reynolds, etc) estamos a impor que o comportamento dinâmico do modelo e protótipo seja igual.
*Semelhança Cinemática* - Fica garantida ao impor as 2 semelhanças acima. Consiste em ter a mesma razão entre as velocidades e as acelerações no modelo e no protótipo.

- Para aplicar a teoria dos modelos é preciso que as 3 semelhanças se verifiquem entre o modelo e o protótipo.

### 6.5.2 - Aplicação de Teoria dos Modelos
#### 6.5.2.1 - Escoamento em tubagens
- Como vimos atrás, ao estudar a perda de pressão por unidade de comprimento do escoamento de um fluido $\rho,v,\mu$ por um tubo de diâmetro $D$ obtem-se a seguinte relação:
$$\frac{D \frac{\Delta p}{l}}{\rho v^{2}}=\phi\left(\frac{\rho v D}{\mu}\right)=\phi(\text{Re})$$
- Se agora considerassemos a perda de pressão numa distância $l$ no tubo tínhamos:
$$\frac{\Delta p}{\rho v^{2}}=\varphi\left(\frac{l}{D},\frac{\rho vD}{\mu}\right)=\varphi\left(\frac{l}{D},\text{Re}\right)$$
de notar que aqui estamos a usar as variáveis independentes $v,D,\mu,\rho$ e a considerar $\Delta p,l$ as variáveis dependentes em estudo.

- Na grande maioria dos casos, os tubos não são mesmo lisos. Apresentam pequenas rugosidades que afetam bastante a perda de pressão. Considerando $\varepsilon$ a altura média dos elementos rugosos na superfície, conseguimos obter:
$$\frac{\Delta p}{\rho v^{2}}=\psi \left(\frac{\varepsilon}{D},\frac{l}{D},\text{Re}\right)$$

- Ora, para estudar isto iremos usar um modelo do tubo. Para que haja semelhança geométrica entre eles é preciso que:
$$\frac{l_{m}}{D_{m}}=\frac{l_{p}}{D_{p}} \quad \quad;\quad \quad \frac{\varepsilon_{m}}{D_{m}}=\frac{\varepsilon_{p}}{D_{p}}$$
de onde resulta
$$\frac{l_{m}}{m_{p}}=\frac{D_{m}}{D_{p}} \quad \quad;\quad \quad \frac{\varepsilon_{m}}{\varepsilon_{p}}=\frac{D_{m}}{D_{p}}$$
o que implica:
$$\frac{l_{m}}{l_{p}}=\frac{\varepsilon_{m}}{\varepsilon_{p}}=\frac{D_{m}}{D_{p}}=\lambda$$
sendo $\lambda$ o **Fator de Escala**. Se $\lambda\ll1$ (modelo muito menor que protótipo) este estudo por ser muito complicado, porque isso implica que a rugosidade do modelo seja muito reduzida.

- Além disso, para ter semelhança diâmica é preciso que:
$$\frac{\rho_{m}D_{m}v_{m}}{\mu_{m}}=\frac{\rho_{p}D_{p} v_{p}}{\mu_{p}}~~~~\to~~~~ \frac{v_{m}}{v_{p}}=\frac{\mu_{m}}{\mu_{p}}\frac{\rho_{p}}{\rho_{m}}\frac{D_{p}}{D_{m}}$$
E se o fluido usado no modelo e protótipo for o mesmo ($\mu_{m}=\mu_{p},\rho_{m}=\rho_{p}$) temos:
$$\frac{v_{m}}{v_{p}}=\frac{D_{p}}{D_{m}}=\frac{1}{\lambda}$$
Para qualquer $\lambda<1$ temos então o fluido a escoar com mais velocidade no modelo do que no protótipo, o que por vezes pode dificultar o estudo.

- Além disso, quando temos o mesmo fluido no modelo e protótipo, para podermos relacionar os dados de um e outro é preciso que:
$$C_{f,p}=C_{f,m}~~~~\to~~~~\Delta p_{p}=\frac{\rho_{p}}{\rho_{m}} \left(\frac{v_{p}}{v_{m}}\right)^{2}\Delta p_{m}~~~~\to~~~~ \Delta p_{p}=\lambda^{2}\Delta p_{m}$$
sendo que $C_{f,p}=\frac{\Delta p_{p}}{\frac{1}{2} \rho_{p} v_{p}^{2}}$

> OU SEJA:
> 1. Igualar os grupos adimensionais geométricos e dinâmicos. Obter alguma relação, especialmente relações que tenham o fator de escala $\lambda$
> 2. Igualar coeficientes cinemáticos (coeficiente de atrito, coeficiente de arrasto, etc) para obter uma relação entre as variáveis em estudo (pressão e força de arrasto nos coeficientes listados atrás).