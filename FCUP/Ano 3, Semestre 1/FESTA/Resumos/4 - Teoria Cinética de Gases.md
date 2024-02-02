# 1 - Estado
## 1.1 - Microestados
- Num dado instante $t$ podemos caraterizar um sistema de $N$ partículas com o seu microestado $\mu(t)$. Ele é descrito pelas posições $\vec{q}_{i}(t)$ e momentos conjugados $\vec{p}_{i}(t)$ das partículas. 
- Podemos então definir um espaço de fase na forma:
$$\Gamma=\prod_{i=1}^{N}\vec{q}_{i} \cdot \prod_{i=1}^{N}\vec{p}_{i}$$
tendo este dimensão $6N$.

- Podemos descrever a evolução temporal do sistema com o Hamiltoniano (Equações do Movimento):
$$\huge\begin{cases}
\frac{dq_{i}}{dq}=\frac{\partial H}{\partial p_{i}} \\
\frac{dp_{i}}{dt}=-\frac{\partial H}{\partial q_{i}}
\end{cases}$$
- Temos ainda que as interações, a nível microscópico, não há perdas de energia. Assim, as interações são reversíveis no tempo. Noutras palavras: temos *simetria de inversão temporal*. Podemos escrever isto como:
$$(\vec{p},\vec{q},t)\to(-\vec{p},\vec{q},-t)$$
ou seja, se ele demora um intervalo $\Delta t$ a ir de um microestado $\mu_{0}$ para $\mu_{1}$; podemos inverter a seta do tempo e percorrer $-\Delta t$ e ele voltará a $\mu_{0}$.

## 1.2 - Macroestados
- Descrito por um conjunto de variáveis macroscópicas / funções de estado: $E,T,P,V$
- Um macroestado é compatível com vários microestados - existem muitos microestados diferentes com a mesma Energia, Pressão, etc de um macroestado $M$.

- Como descrever um macroestado:
    1. Definir o que é o macroestado (fixar uma variável macroscópica)
    2. Selecionar os microestados compatíveis com essa variável. Na prática, isto consiste em selecionar a parte do espaço de fase em estudo. A este conjunto de microestados podemos chamar *ensemble* de microestados.
    3. Considerar $\mathcal{N}$ cópias do macroestado $M$, representadas por microestados $\mu_{i}(t)\in \Gamma$ compatíveis. Estes são obtidos ao recolher amostras de forma uniforme da porção de $\Gamma$ em estudo. Iremos chamar a estes microestados compatíveis: *pontos representativos*.
    5. Criar a função $d\mathcal{N}(\vec{p},\vec{q},t)$ que diz o número de pontos representativos num volume infinitesimal $d\Gamma=\prod_{i=1}^{N}d^{3}\vec{p}_{i}d^{3}\vec{q}_{i}=\prod_{i=1}^{N}dq_{xi}dq_{yi}dq_{zi}dp_{xi}dp_{yi}dp_{zi}$ 
    6. Construimos uma densidade do espaço de fazer dada por: $$\rho(\vec{p},\vec{q},t)d\Gamma=\lim\limits_{\mathcal{N}\to+\infty}\frac{d\mathcal{N}(\vec{p},\vec{q},t)}{\mathcal{N}}$$em que temos $\int \rho(\vec{p},\vec{q},t)d\Gamma=1$

- Ou seja, para descrever um macroestado $M$ podemos usar uma distribuição de probabilidade $\rho$ associada aos microestados compatíveis.

### Observáveis
- Podemos obter o valor médio de uma observável $\mathcal{O}$ assim:
$$\langle \mathcal{O}\rangle=\int d\Gamma~\rho(\vec{p},\vec{q},t)\mathcal{O}(\vec{p},\vec{q})$$

### Estados Puros e Mistos
**Estado Puro** - se conhecemos exatamente o microestado $\mu(t)$ que descreve o estado. O microestado $\mu(t)$ está sempre a mudar. Não faz sentido falar em equilíbrio.
**Estado Misto/Mistura** -  se apenas sabemos que o estado está num microestado descrito por $\rho(\Gamma)$ (apenas temos conhecimento probabilístico). Podemos descrever o equilíbrio.

# 2 - Teorema de Liouville
- Temos a densidade de probabilidade do espaço de fase: $\rho(\vec{p},\vec{q},t)$
- Este teorema diz-nos que a densidade se comporta como a densidade de um fluído incompressível ao longo do tempo. Ou seja, se a densidade ocupa um volume $d\Gamma$ em $t$, em $t+\delta t$ o espaço que as partículas ocupam pode deformar-se mas o volume total continuará a ser $d\Gamma$:
![[liouville.png]]
- Podemos seguir a evolução temporal de $d\mathcal{N}$ estados puros dentro do volume $d\Gamma$ em torno de $(\vec{p},\vec{q})$. Podemos escrever: $d\Gamma=\prod_{i=1}^{N}d^{3}\vec{q}_{i}d^{3}\vec{p}_{i}$.
- Para cada par de coordenadas $(q_{a},p_{a})$ (isto será a posição e momento de 1 partícula dentro de $d\Gamma$, em qualquer uma das 3 direções) temos, após um intervalo $\delta t$:
$$\begin{cases}
q_{a}'&= q_{a}+\dot{q_{a}}\delta t+O(\delta t^{2})\\
p_{a}'&= p_{a}+\dot{p_{a}}\delta t+O(\delta t^{2})
\end{cases}$$
e podemos obter os diferenciais:
$$\begin{cases}
dq_{a}'=dq_{a}+\frac{d\dot{q_{a}}}{dq_{a}}dq_{a}\delta(t)+O(\delta t^{2}) \\
dp_{a}'=dp_{a}+\frac{d\dot{p_{a}}}{dp_{a}}dp_{a}\delta(t)+O(\delta t^{2})
\end{cases}$$
e temos que o volume $d\Gamma$ passa a ser $d\Gamma'=\prod_{i=1}^{N}d^{3}\vec{q_{i}}'d^{3}\vec{p_{i}}'$. A evolução do volume estará relacionada com a evolução dos seus lados. para um par $dq_{a},dp_{a}$ temos:
$$dq_{a}'dp_{a}'\longrightarrow dq_{a}dp_{a}\left[1+\left(\frac{\partial\dot{q_{a}}}{\partial q_{a}}+\frac{\partial\dot{p_{a}}}{\partial p_{a}}\right)\delta t+O(\delta t^{2})\right]$$
- Das equações do movimento temos:
$$\begin{cases}
\dot{q}=\frac{\partial H}{\partial p} \\
\dot{p}=- \frac{\partial H}{\partial q}
\end{cases}$$
e conseguimos obter:
$$\begin{align*}
\frac{\partial\dot{q_{a}}}{\partial q_{a}}&= \frac{\partial}{\partial q_{a}}\frac{\partial H}{\partial p_{a}}=\frac{\partial^{2}H}{\partial q_{a}\partial p_{a}}\\
\frac{\partial\dot{p_{a}}}{\partial p_{a}}&= -\frac{\partial}{\partial p_{a}}\frac{\partial H}{\partial q_{a}}=-\frac{\partial^{2}H}{\partial p_{a}\partial q_{a}}
\end{align*}~\Huge{\Biggr |}\normalsize \Longrightarrow \frac{\partial\dot{q_{a}}}{\partial q_{a}}+\frac{\partial\dot{p_{a}}}{\partial p_{a}}=0$$
- Isto significa que:
$$dq_{a}'dp_{a}'=dq_{a}dp_{a}$$
- Por outras palavras, em todos os pares $p_{a},q_{a}$ temos que o seu produto não se altera. Isto mostra que 
$$d\Gamma=d\Gamma'$$

- A razão $\frac{d\mathcal{N}}{dt}$ mantém-se constante, logo $\rho$ é constante:
$$\rho(\vec{p'},\vec{q'},t+\delta t)=\rho(\vec{p},\vec{q},t)$$
- Podemo escrever a densidade na forma diferencial:
$$d\rho=\frac{\partial \rho}{\partial p}dp+\frac{\partial \rho}{\partial q}dq+\frac{\partial \rho}{\partial t}dt$$
e temos que a sua derivada temporar é nula:
$$\frac{d\rho}{dt}=\frac{\partial \rho}{\partial t}+\sum\limits_{a=1}^{3N} \left(\frac{\partial\rho}{\partial p_{a}}\frac{dp_{a}}{dt}+\frac{\partial \rho}{\partial q_{a}}\frac{dq_{a}}{dt}\right)=0$$
podemos usar as equações do movimento:
$$\begin{align*}
\frac{\partial\rho}{\partial t}&= -\sum\limits_{a=1}^{3N}\left(\frac{\partial\rho}{\partial p_{a}}\left(-\frac{\partial H}{\partial q_{a}}\right) + \frac{\partial\rho}{\partial q_{a}}\frac{\partial H}{\partial p_{a}}\right)\\
\frac{\partial\rho}{\partial t}&= \sum\limits_{a=1}^{3N}\left(\frac{\partial\rho}{\partial p_{a}}\frac{\partial H}{\partial q_{a}} - \frac{\partial\rho}{\partial q_{a}}\frac{\partial H}{\partial p_{a}}\right)\\
\frac{\partial\rho}{\partial t}&= -\{\rho, H\}
\end{align*}$$
em que temos os parêntesis de Poisson:
$$\{f,g\}=\sum\limits_{i}\frac{\partial f}{\partial q_{i}}\frac{\partial g}{\partial p_{i}}-\frac{\partial f}{\partial p_{i}}\frac{\partial g}{\partial q_{i}}$$

### Evolução temporal de Observável
$$\begin{align*} 
\frac{d\langle \mathcal O\rangle}{dt} &= \int \frac{\partial \rho}{\partial t} \mathcal O\ d\Gamma \\
&= \sum_{a=1}^{3N}\int\mathcal O\left(\frac{\partial H}{\partial q_a}\frac{\partial \rho}{\partial p_a}- \frac{\partial \rho}{\partial q_a}\frac{\partial H}{\partial p_a}\right)d\Gamma \\
&= -\sum_{a=1}^{3N}\int \rho \left[\frac{\partial }{\partial p_a}\left(\mathcal O\frac{\partial H}{\partial q_a}\right)- \frac{\partial }{\partial q_a}\left(\mathcal O\frac{\partial H}{\partial p_a}\right)\right]d\Gamma \\
&= \sum_{a=1}^{3N}\int \rho \left[\frac{\partial \mathcal O}{\partial q_a}\frac{\partial H}{\partial p_a}-\frac{\partial \mathcal O}{\partial p_a}\frac{\partial H}{\partial q_a}+\mathcal O\left( \frac{\partial^2H}{\partial p_a\partial q_a} - \frac{\partial^2H}{\partial q_a\partial p_a}\right)\right]d\Gamma \\
&= \int \rho \{\mathcal O, H\} d\Gamma\\
&= \langle \{\mathcal O, H\}\rangle\\
\end{align*}$$

# 3 - Equilíbrio
- Quando temos um equilíbrio, então as propriedades do macroestado têm que ser constantes. Isto significa que:
$$\frac{\partial \rho}{\partial t}=0$$
- O que isto implica exatamente irá depender de qual a variável macroscópica em equilíbrio.

### Energia
- Neste caso temos $\rho=\rho(H,t)$. Assim:
$$\begin{align*}
\frac{\partial\rho}{\partial t}&= - \{\rho(H),H\}
\end{align*}$$
fica:
$$\begin{align*}
\frac{\partial\rho}{\partial t}&= \sum\limits_{a=1}^{3N}\left(\frac{\partial\rho(H)}{\partial p_{a}}\frac{\partial H}{\partial q_{a}} - \frac{\partial\rho(H)}{\partial q_{a}}\frac{\partial H}{\partial p_{a}}\right)\\
&= \sum\limits_{a=1}^{3N}\left(\frac{\partial\rho(H)}{\partial H}\frac{\partial H}{\partial p_{a}}\frac{\partial H}{\partial q_{a}} - \frac{\partial\rho(H)}{\partial H}\frac{\partial H}{\partial q_{a}}\frac{\partial H}{\partial p_{a}}\right)\\
&= \frac{\partial \rho}{\partial H}\sum\limits_{a=1}^{3N}\left(\frac{\partial H}{\partial p_{a}}\frac{\partial H}{\partial q_{a}} - \frac{\partial H}{\partial q_{a}}\frac{\partial H}{\partial p_{a}}\right)\\
&= \rho'(H)\{H,H\}\\
&= 0
\end{align*}$$
pelo que isto significa que temos $\rho$ a ser constante ao longo de uma superfície $H(\vec{p},\vec{q})=E$ de energia constante $E$, sendo $\rho$ uma distribuição uniforme nessa superfície.

### Outras quantidades
- Podemos definir quantidades genéricas $L_{i}(\vec{p},\vec{q})$ que se mantêm constantes no tempo. Essas quantidades são definidas por $\{L_{i},H\}=0$, porque:
$$\frac{dL_{i}}{dt}(\vec{p},\vec{q})=\{L_{i},H\}=0$$
e podemos usar estas quantidades para definir a densidade de probabilidade:
$$\rho(H,L_i,t)$$

# 4 - Hierarquia BBGKY
- Nome por extenso: hierarquia Bogoliubov-Born-Green-Kirkwood-Yvon.

### Distribuição de 1 Partícula
- Corresponde à probabiliade de encontrarmos uma partícula com um certo momento e posição. Ou seja, simplesmente selecionamos de todos os casos possíveis, aqueles que têm a posição e momento desejados:
$$f_{1}(\vec{p_{1}},\vec{q_{1}},t)=\left\langle \sum\limits_{i=1}^{N}\delta(\vec{p}-\vec{p_{i}})\delta(\vec{q}-\vec{q_{1}})\right\rangle=N\int \rho(\vec{p_{1}}=\vec{p},\vec{q_{1}}=\vec{q},\vec{p}_{2},\vec{q}_{2},\dots,\vec{p}_{N},\vec{q}_{N};t)\prod_{i=2}^{N}d\vec{p_{i}}d\vec{q_{i}}$$
em que usamos o facto que a média da soma é igual à soma das médias. De notar que quanto maior for $N$, maior a probabilidade, tal como seria de esperar.

### Distribuição de $s$ partículas
$$\begin{align*} 
f_s(\vec p_1, \dots, \vec q_s, t) &= \frac{N!}{(N-s)!}\int\rho(\vec p_1, \vec q_1, \vec p_2, \vec q_2, \dots, \vec p_N, \vec q_N)\ \prod_{i=s+1}^N d\vec p_id\vec q_i \\
&= \frac{N!}{(N-s)!}\rho_s(\vec p_1,\vec{q}_1, \dots,\vec{p}_s ,\vec q_s, t) 
\end{align*}$$
em que $\rho_{s}$ é a densidade de probabilidade normalizada (quando integrada pelas variáveis que a definem dá 1).
- O valor que $f_{s}()$ nos dá está relacionado com o número médio de partículas com os momentos e posições especificados.

## 4.1 - Gás de Interação fraca
- O hamiltoniano é definido por:
$$\mathcal{H}(\vec{p},\vec{q})=\sum\limits_{i=1}^{N}\left[\frac{\vec{p_{i}}^{2}}{2m} + U(\vec{q_{i}})\right]+ \frac{1}{2} \sum\limits^{N}_{\substack{i,j=1\\ (i\neq j)}} \mathcal{V}(\vec{q_{i}}-\vec{q_{j}})$$
temos: energia cinética através do momento e massa das partículas, potencial (externo) e um termo de interação entre 2 corpos (existem termos de interação entre 3+ corpos, mas para gases de fraca interação podemos ignorá-los).

1. Dividimos o sistema em 2 conjuntos: um com $s$ partículas, um com $N-s$ partículas
2. Reescrevemos o hamiltoniano como: $$\mathcal{H}=\mathcal{H}_{s}+\mathcal{H}_{N-s}+\mathcal{H'}$$
    - $\mathcal{H}_{s}$ é o Hamiltoniano das $s$ partículas: $$\mathcal{H}_{s}(\vec{p},\vec{q})=\sum\limits_{i=1}^{s}\left[\frac{\vec{p_{i}}^{2}}{2m} + U(\vec{q_{i}})\right]+ \frac{1}{2} \sum\limits^{s}_{\substack{i,j=1\\ (i\neq j)}} \mathcal{V}(\vec{q_{i}}-\vec{q_{j}})$$
    - $\mathcal{H}_{N-s}$ é o Hamiltoniano das $N-s$ partículas: $$\mathcal{H}_{N-s}(\vec{p},\vec{q})=\sum\limits_{i=s+1}^{N}\left[\frac{\vec{p_{i}}^{2}}{2m} + U(\vec{q_{i}})\right]+ \frac{1}{2} \sum\limits^{N}_{\substack{i,j=s+1\\ (i\neq j)}} \mathcal{V}(\vec{q_{i}}-\vec{q_{j}})$$
    - $\mathcal{H'}$ é o Hamiltoniano associado às interações entre as partículos dos conjuntos $s,N-s$: $$\mathcal{H'}(\vec{p},\vec{q})=\sum\limits_{i=1}^{s}\sum\limits_{j=s+1}^{N}\mathcal{V}(\vec{q_i}-\vec{q_j})$$

- E podemos escrever:
$$\begin{align*}
\frac{\partial\rho_{s}}{\partial t}=\int \prod_{i=s+1}^{N}dV_{i}\frac{\partial\rho}{\partial t}&= -\int \prod_{i=s+1}^{N}dV_{i}\{\rho, \mathcal{H_{s}}+\mathcal{H}_{N-s}+\mathcal{H'}\}\\
&= \int\prod_{i=s+1}^{N}dV_{i}\left(\{\rho,\mathcal{H_{s}}\}+\{\rho,\mathcal{H}_{N-s}\}+\{\rho,\mathcal{H'}\} \right)
\end{align*}$$
- Podemos então calcular os integrais dos temos dos parentesis de Poisson 1 a 1:
**1º termo**
$$\begin{align*}
\int \{\rho,\mathcal{H_{s}}\} \prod_{i=s+1}^{N} dV_{i} &= \left\{\int \rho \prod_{i=s+1}^{N} dV_{i},\mathcal{H_{s}} \right\}=\{\rho_{s},\mathcal{H_{s}}\}
\end{align*}$$
(podemos separar assim os parentesis porque $\mathcal{H_{s}}$ é para as $s$ partículas e o integral percorre as $N-s$, pelo que não depende dele)

**2º termo**
Aqui temos que fazer os parentesis antes do integral porque tanto $\mathcal{H}_{N-s}$ como o integral são para as $N-s$ partículas.
$$\begin{align*}
\int \{\rho,\mathcal{H}_{N-s}\} \prod_{i=s+1}^{N} dV_{i} &= \int \sum_{i=1}^N\left(\frac{\partial \rho}{\partial q_i}\frac{\partial \mathcal H_{N-s}}{\partial p_i} - \frac{\partial \mathcal H_{N-s}}{\partial q_i}\frac{\partial \rho}{\partial p_i}\right)\ \prod_{i=s+1}^N dV_{i}\\
&= \int \sum_{j=s+1}^N\left(\frac{\partial \rho}{\partial q_j}\frac{p_i}{m} - \left(\sum_{i=s+1}^N \frac{U(\textbf q_i)}{\partial q_j} + \frac12\sum_{k=s+1, k\ne j}^N \frac{\mathcal V(\textbf q_j - \textbf q_k)}{\partial q_j}\right)\frac{\partial \rho}{\partial p_j}\right)\ \prod_{j=s+1}^N dV_{i}\\
&= 0
\end{align*}$$
Notas:
- Os sumatórios começam apenas em $j=s+1$ porque o Hamiltoniano só é das $N-s$ partículas.
- Não sei bem porquê que se anula tudo
- O que temos a tirar é: a evolução do sistema não depende das $N-s$ partículas.

**3º Termo**
$$\begin{align*}
\int \{\rho,\mathcal{H'}\} \prod_{i=s+1}^{N} dV_{i} &= \int \sum_{i=1}^N\left(\frac{\partial \rho}{\partial q_i}\cancelto0{\frac{\partial \mathcal H'}{\partial p_i}} - \frac{\partial \mathcal H'}{\partial q_i}\frac{\partial \rho}{\partial p_i}\right)\ \prod_{i=s+1}^N dV_{i}\\
&= -\int \sum_{i=1}^N\left(\frac{\partial \mathcal H'}{\partial q_i}\frac{\partial \rho}{\partial p_i}\right)\ \prod_{i=s+1}^N dV_{i}\\
&= -\int \sum_{i=1}^s \frac{\partial \rho}{\partial p_i}\sum_{j=s+1}^N \frac{\partial \mathcal V(q_i - q_j)}{\partial q_i} + \sum_{i=s+1}^N \frac{\partial \rho}{\partial p_i}\sum_{j=1}^s \frac{\partial \mathcal V(q_j - q_i)}{\partial q_i}\ \prod_{i=s+1}^N dV_{i}
\end{align*}$$
(esta separação é simplesmente uma forma de garantir que percorremos todas as partículas; tendo-se no 1º termo $i$ a ser uma partícula do grupo $s$ e $j$ do grupo $N-s$ e depois ao contrário.)
- Não percebi o resto da dedução. No final dá:
$$\int\{\rho,\mathcal{H'}\} dV_{i}=-(N-s)\sum_{i=1}^s\int\frac{\partial \mathcal V(q_i - q_{s+1})}{\partial q_i}\cdot\frac{\partial \rho_{s+1}}{\partial p_i}\ dV_{s+1}$$

- A Equação inteira da evolução do sistema de um gás de interação fraca fica:
$$\boxed{\frac{\partial\rho_{s}}{\partial t}-\{\mathcal{H_{s}},\rho_{s}\}=(N-s)\sum_{i=1}^s\int\frac{\partial \mathcal V(q_i - q_{s+1})}{\partial q_i}\cdot\frac{\partial \rho_{s+1}}{\partial p_i}\ dV_{s+1}}$$
- De notar que:
    - Para estudar o sistema precisamos de informação de partículas fora do conjunto
    - Se deixarmos de contar as interações entre partículas o termo da direita anula-se e ficamos com uma relação de acordo com o teorema de Liouville.
    - Podemos criar uma hierarquia (BBGKY) de equações para diferentes $s$.

