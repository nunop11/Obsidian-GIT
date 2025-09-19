- Vejamos detalhes de vários tipos de estruturas de bandas.

## Metais de Eletrões Quase Livres
- Metais dos grupos 1,2,3,4 da TP podem ser descritos como se tivessem um potencial quase constante -> Metais de Eletrões Quase Livres.
- Assim, os eletrões podem ser descritos conforme o gás de eletrões livres de Sommerfeld!
- Na realidade, temos bandas energéticas. Mas existem fatores que as fazem comportar desta forma:
    - Iterações eletrão-ião - os livres de condução não se podem aproximar dos iões (esta região já está ocupada pelos eletrões do ião)
    - Consoante os eletrões de condução se movem, o potencial que cada um deles sente é menor ainda porque eles fazem *blindagem* dos campos dos iões.

- De acordo com o teorema de Bloch, quando temos um potencial periódico fraco, as soluções da ESIT podem ser aproximadas a ondas planas: $\psi_{\vec{k}}(\vec{r})=\sum_{\vec{K}}c_\vec{k}-\vec{K} e^{i(\vec{k}-\vec{K})\cdot\vec{r}}$ e podemos determinar $c_{\vec{k}-\vec{K}},E$ usando a equação central.

## Potencial Nulo
- Se tivermos um eletrão livre temos $V_{\vec{K}}=0~,~\forall\vec{K}$ (potencial nulo). Assim temos a equação central:
$$\left[E_{\vec{k}-\vec{K}}^{(0)}-E_{\vec{k}}  \right]c_{\vec{k}-\vec{K}}=0$$
de onde surge:
$$E_{\vec{k}-\vec{K}}^{(0)}= \frac{\hbar^{2}}{2m}(\vec{k}-\vec{K})^{2}$$
### Não Degenerado
- No caso em que apenas um $\vec{K}$ satisfaz $E_{\vec{k}-\vec{K}}^{(0)}=E_{\vec{k}}$ então todos os outros termos nulos e fica: $E_{\vec{k}-\vec{K}}^{(0)}=E_{\vec{k}}~~\to~~ \psi_{\vec{k}}\propto e^{i(\vec{k}-\vec{K})\cdot\vec{r}}$

### Degenerado
- Quando temos vários vetores $\vec{K}$ que satisfazem a equação.
- Consideremos $\vec{K}_{1},\vec{K}_{2},\dots,\vec{K}_{m}$ em que $E_{\vec{k}-\vec{K}_{1}}^{(0)}=\cdots=E_{\vec{k}-\vec{K}_{m}}^{(0)}$ e simplesmente teremos:
$$\psi_{\vec{K}}=\sum\limits_{j=1}^{m}c_{\vec{k}-\vec{K}_{j}}e^{i(\vec{k}-\vec{K}_{j})\cdot\vec{r}}$$
como qualquer combinação linear de soluções da ES é uma solução da ES, então podemos escolher quaisquer $c$.

## Potencial Fraco
- Vejamos o caso de um potencial $V(\vec{r})$ fraco.

### Não Degenerado
- Escolhendo um $\vec{k}$ e considerando um vetor $\vec{K}_{1}$ de modo que:
$$|E_{\vec{k}-\vec{K}_{1}}^{(0)} - E_{\vec{k}-\vec{K}}|\gg V_{\vec{K}}$$
sendo esta a *condição de não degenerescência*.
- Teremos:
![[Pasted image 20240603224042.png]]
a preto temos a curva de $\vec{k}-\vec{K}_{1}$ e a azul temos $\vec{k}-\vec{K}$.

- Vamos então o que o potencial faz ao nível com: $E_{\vec{k}}=E_{\vec{k}-\vec{K}_{1}}^{(0)}~,~c_{\vec{k}-\vec{K}}=0~,~\forall \vec{K}\neq\vec{K}_{1}$

**Equação Central**
- A equação central com $\vec{K'}=\vec{K}_{1}$:
$$[E_{\vec{k}}-E_{\vec{k}-\vec{K}_{1}}^{(0)}]c_{\vec{k}-\vec{K}_{1}}=\sum\limits_{\vec{K}}V_{\vec{K}-\vec{K}_{1}}c_{\vec{k}-\vec{K}}$$
- Podemos considerar $V_{0}=0$ -- esta é a componente de frequência nula do Fourier AKA modo comum. Na prática, esta componente apenas desliza o espetro de energias para o lado, então decidimos ignorá-la.
- Como $V_{0}=0~~\to~~V_{\vec{K}-\vec{K}_{1}}=0$, no somatório apenas ficam os termos com $\vec{K}\neq\vec{K}_{1}$ e podemos obter:
$$c_{\vec{k}-\vec{K}_{1}}=\sum\limits_{\vec{K}\neq\vec{K}_{1}}\frac{V_{\vec{K}-\vec{K}_{1}}c_{\vec{k}-\vec{K}}}{E_{\vec{k}}-E_{\vec{k}-\vec{K}_{1}}^{(0)}}$$

#### Determinar Coeficientes
- Isto é independente do que temos acima.
- Vimos na aula desta matéria, quando $V(\vec{r})\to0$ também temos $c_{\vec{k}-\vec{K}}\to0 ~~(\vec{K}\neq\vec{K}_{1})$.
- Partindo da equação central temos:
$$\begin{align*}
\left(E_{\vec{k}-\vec{K}}^{(0)}-E_{\vec{k}} \right)c_{\vec{k}-\vec{K}}+\sum\limits_{\vec{K'}}V_{\vec{K'}-\vec{K}}c_{\vec{k}-\vec{K'}}&= 0\\
(E_{\vec{k}}-E_{\vec{k}-\vec{K}}^{(0)})c_{\vec{k}-\vec{K}}&= V_{\vec{K}_{1}-\vec{K}}c_{\vec{k}-\vec{K}_{1}} + \sum\limits_{\vec{K'}\neq\vec{K}_{1}}V_{\vec{K'}-\vec{K}}c_{\vec{k}-\vec{K'}}\\
c_{\vec{k}-\vec{K}}&= \frac{V_{\vec{K}_{1}-\vec{K}}}{E_{\vec{k}}-E_{\vec{k}-\vec{K}}^{(0)}}c_{\vec{k}-\vec{K}_{1}} + \sum\limits_{\vec{K'}\neq\vec{K}_{1}}\frac{V_{\vec{K'}-\vec{K}}}{E_{\vec{k}}-E_{\vec{k}-\vec{K}}^{(0)}}c_{\vec{k}-\vec{K'}}
\end{align*}$$
aqui separamos o termo $\vec{K'}=\vec{K}_{1}$ porque este será bastante maior pois não há degenerescências : teremos o denominador próximo de zero

- E como os outros $c$ serão todos menores, podemos dizer:
$$c_{\vec{k}-\vec{K}}= \frac{V_{\vec{K}_{1}-\vec{K}}}{E_{\vec{k}}-E_{\vec{k}-\vec{K}}^{(0)}}c_{\vec{k}-\vec{K}_{1}} +\mathcal{O}(V^{2})$$

#### Correção de Energia
- Partindo da correção até 2ª ordem: $E_{\vec{k}}=E_{\vec{k}}^{(0)} + \bra{\vec{k}}\hat{V}\ket{\vec{k}}+\sum_{\vec{k'}\neq \vec{k}}\frac{|\bra{\vec{k}}\hat{V}\ket{\vec{k'}}|^{2}}{E_{\vec{k}}^{(0)} - E_{\vec{k'}}^{(0)}}$, podemos escrever:
$$E_{\vec{k}}=E_{\vec{k}-\vec{K}_{1}}^{(0)}+\sum\limits_{\vec{K}}\frac{|V_{\vec{K}-\vec{K}_{1}}|^{2}}{E_{\vec{k}-\vec{K}_{1}}^{(0)}-E_{\vec{k}-\vec{K}}^{(0)}}c_{\vec{k}-\vec{K}_{1}}$$
em que substituimos $E_{\vec{k}}^{(0)}=E_{\vec{k}-\vec{K}_{1}}^{(0)}$.

- Voltamos a observar o que vimos atrás: os níveis $E_{\vec{k}-\vec{K}}^{(0)}$ abaixo de $E_{\vec{k}-\vec{K}_{1}}^{(0)}$ empurram-no para cima (acrescentam energia). Os níveis acima reduzem a energia. Isto tudo será causado pelo sinal do denominador do somatório.

### Degenerado
- Temos $m$ vetores, tais que:
$$\begin{align*}
|E_{\vec{k}-\vec{K}_{i}}^{(0)}-E_{\vec{k}-\vec{K}_{j}}^{(0)}|\lesssim V_{\vec{K}}\\
|E_{\vec{k}-\vec{K}}^{(0)}-E_{\vec{k}-\vec{K}_{i}}^{(0)}|\gg V_{\vec{K}}
\end{align*}$$
(a primeira eq define o distanciamento entre valores $m$. A segunda eq não sei)

**Equações Centrais**
- Teremos uma eq Central para cada um dos $m$ vetores, que têm de ser tratadas separadamente! 
- Temos:
$$(E_{\vec{k}}-E_{\vec{k}-\vec{K}_{i}}^{(0)})c_{\vec{k}-\vec{K}_{i}}=\sum\limits_{j=1}^{m}V_{\vec{K}_{j}-\vec{K}_{i}}c_{\vec{k}-\vec{K}_{j}} + \sum\limits_{\vec{K}\neq\vec{K_{1}},\dots,\vec{K}_{m}}V_{\vec{K}-\vec{K}_{i}}c_{\vec{k}-\vec{K}}$$

**Determinar Coeficientes**
- Novamente, no limite $V(\vec{r})\to0$ temos $c_{\vec{k}-\vec{K}_{i}}\to0~,~i=1,\dots,m$
- Assim:
$$\begin{align*}
(E_{\vec{k}}-E_{\vec{k}-\vec{K}_{i}}^{(0)})c_{\vec{k}-\vec{K}_{i}}&= \sum\limits_{j=1}^{m}V_{\vec{K}_{j}-\vec{K}_{i}}c_{\vec{k}-\vec{K}_{j}} + \sum\limits_{\vec{K}\neq\vec{K_{1}},\dots,\vec{K}_{m}}V_{\vec{K}-\vec{K}_{i}}c_{\vec{k}-\vec{K}}\\
&= \sum\limits_{j=1}^{m}V_{\vec{K}_{j}-\vec{K}_{i}}c_{\vec{k}-\vec{K}_{j}} + \sum\limits_{\vec{K}\neq\vec{K_{1}},\dots,\vec{K}_{m}}V_{\vec{K}-\vec{K}_{i}} \cdot \frac{1}{E_{\vec{k}}-E_{\vec{k}-\vec{K}}^{(0)}}\sum\limits_{j=1}^{m}V_{\vec{K}_{j}-\vec{K}}c_{\vec{k}-\vec{K}_{j}} +\mathcal{O}(V^{3})\\
&= \sum\limits_{j=1}^{m}V_{\vec{K}_{j}-\vec{K}_{i}}c_{\vec{k}-\vec{K}_{j}} + \sum\limits_{j=1}^{m}\sum\limits_{\vec{K}\neq\vec{K_{1}},\dots,\vec{K}_{m}}\frac{V_{\vec{K}-\vec{K}_{i}}V_{\vec{K}_{j}-\vec{K}}}{E_{\vec{k}}-E_{\vec{k}-\vec{K}}^{(0)}}c_{\vec{k}-\vec{K}_{j}}+\mathcal{O}(V^{3})\\
&\simeq \sum\limits_{j=1}^{m}V_{\vec{K}_{j}-\vec{K}_{i}}c_{\vec{k}-\vec{K}_{j}}
\end{align*}$$
(acho que a equação usada no início para $c_{\vec{k}-\vec{K}}$  é obtida de forma semelhante à que obtivemos para o caso não degenerado)

## Níveis Energéticos perto de Plano de Bragg
- Vamos agora ver um exemplo, em que temos degenerescência de 2 níveis energéticos.
- Fixamos $\vec{k}$ e para 2 vetores $\vec{K}_{1}\neq\vec{K}_{2}$ temos:
$$\begin{align*}
|E_{\vec{k}-\vec{K}_{1}}^{(0)}-E_{\vec{k}-\vec{K}_{2}}^{(0)}|&\lesssim V_{\vec{K}}\\
|E_{\vec{k}-\vec{K}}^{(0)}-E_{\vec{k}-\vec{K}_{i}}^{(0)}|&\gg V_{\vec{K}}~~~~;~~i=1,2
\end{align*}$$

**Equações Centrais**
- Temos estas 2 eqs:
$$\begin{align*}
\left[E - E_{\vec k -\vec K_1}^{(0)}\right]c_{\vec k - \vec K_1}&=V_0c_{\vec k - \vec K_1} + V_{\vec K_2 - \vec K_1}c_{\vec k-\vec K_2} \\
\left[E - E_{\vec k -\vec K_2}^{(0)}\right]c_{\vec k - \vec K_2}&=V_0c_{\vec k-\vec K_2} + V_{\vec K_1-\vec K_2}c_{\vec k-\vec K_1}
\end{align*}$$
fazemos a mudanças de variável: $\vec{q}=\vec{k}-\vec{K}_{1}$ e $\vec{K}=\vec{K}_{2}-\vec{K}_{1}$. Temos:
$$\begin{align*}
[E-(E_{\vec{q}}^{(0)}+V_{0})]c_{\vec{q}}&= V_{\vec{K}}c_{\vec{q}-\vec{K}}\\
[E-(E_{\vec{q}-\vec{G}}^{(0)}+V_{0})]c_{\vec{q}-\vec{K}}&= V_{\vec{K}}^{*}c_{\vec{q}}
\end{align*}$$
- Para $\vec{K'}\neq \vec{K},\vec{0}$ temos: $|E_{\vec{q}}^{(0)}-E_{\vec{q}-\vec{K'}}^{(0)}|\gg V_{\vec{K}}$ 
- Para $V_{\vec{K}}$ reduzido temos: $E_{\vec{q}}^{(0)}\approx E_{\vec{q}-\vec{K}}^{(0)}$.

- Mais concretamente, teremos $E_{\vec{q}}^{(0)}=E_{\vec{q}-\vec{K}}^{(0)}$ quando $|\vec{q}|=|\vec{q}-\vec{K}|$. Ou seja, quando $\vec{q}$ pertence ao plano de Bragg. Por outras palavras: $\vec{q}$ pertence à bissetriz da linha que une $\vec{k}$ a $\vec{K}$:
![[Pasted image 20240603233325.png]]
- Ou seja, temos degenerescência quando $\vec{q}$ está próximo de um plano de Bragg. De outra forma: ocorre degenerescência para eletrões livres com vetor de onda próximo de um vetor que cumpre a condição de Von Laue.

**Correções Energéticas**
- As equações acima resulta no problema:
$$\begin{pmatrix}E_{\vec{q}}^{(0)}+V_{0} & V_{\vec{K}} \\ V_{\vec{K}}^{*} & E_{\vec{q}-\vec{K}}^{(0)}+V_{0}\end{pmatrix}\begin{pmatrix}c_{\vec{q}} \\ c_{\vec{q}-\vec{K}}\end{pmatrix}= \varepsilon \begin{pmatrix}c_{\vec{q}} \\ c_{\vec{q}-\vec{K}}\end{pmatrix}$$
que resulta em:
$$\begin{vmatrix}E_{\vec{q}}^{(0)}+V_{0}-\varepsilon & V_{\vec{K}} \\ V_{\vec{K}}^{*} & E_{\vec{q}-\vec{K}}^{(0)}+V_{0}-\varepsilon\end{vmatrix}=0$$
e resulta a equação caraterística:
$$(E_{\vec{q}}^{(0)}+V_{0}-\varepsilon)(E_{\vec{q}-\vec{K}}^{(0)}+V_{0}-\varepsilon)-|V_{\vec{K}}|^{2}=0$$
e resulta:
$$\varepsilon_\pm = \frac12(E_{\vec q}^{(0)} + E_{\vec q-\vec K}^{(0)} + 2V_0) \pm \left[\left(\frac{E_\vec q^{(0)}- E_{\vec q- \vec K}^{(0)}}{2}\right)^2 + |V_\vec K|^2\right]^{1/2}$$
- Se tivermos $E_{\vec{q}}^{(0)}=E_{\vec{q}-\vec{K}}^{(0)}$ temos:
$$\varepsilon_{\pm}=(E_{\vec{q}}^{(0)}+V_{0})\pm|V_{\vec{K}}|$$

**Superfícies de Energia Constante**
- Se tivermos $E_{\vec{q}}^{(0)}=E_{\vec{q}~\vec{K}}^(0)$ podemos aindar ver que:
$$\frac{\partial\varepsilon}{\partial\vec{q}}=\frac{\hbar^{2}}{m}\left(\vec{q}- \frac{1}{2}\vec{K} \right)$$
![[Pasted image 20240603234601.png|256]]

- Ou seja, se $\vec{q}$ estiver num plano de Bragg teremos o gradiente de $\varepsilon$ paralelo ao plano. Como o plano é perpendicular às superfícies em que a função de onda é constante, então também o gradiente de $\varepsilon$ será. Ou seja: temos superfícies de energia constante.

**Funções de Onda**
- Não tenho a certeza como, mas podemos demonstrar que:
$$c_{\vec{q}}=\pm \frac{V_{\vec{K}}}{|V_{\vec{K}}|}c_{\vec{q}-\vec{K}}$$
(em que a fração simplesmente irá dar $\pm1$ ou seja: o sinal de $V_{\vec{K}}$)
- Ora, estes termos iram dominar a expansão e temos:
$$\begin{align*}
\psi_{\vec{k}}(\vec{r})= \sum\limits_{\vec{K'}}c_{\vec{k}-\vec{K'}}e^{i(\vec{k}-\vec{K})\cdot\vec{r}}&\simeq c_{\vec{k}}e^{i\vec{k}\cdot\vec{r}} + c_{\vec{k}-\vec{K}}e^{i(\vec{k}-\vec{K})\cdot\vec{r}}\\
&= e^{i\vec{k}\cdot\vec{r}}(c_{\vec{k}}+c_{\vec{k}-\vec{K}}e^{-i\vec{K}\cdot\vec{r}})\\
&= e^{i\vec{K}\cdot\vec{r}}c_{\vec{k}-\vec{K}}\left(\pm \frac{V_{\vec{K}}}{|V_{\vec{K}}|}+e^{-i\vec{K}\cdot\vec{r}}\right)\\
&= e^{i\vec{k}\cdot\vec{r}}e^{-i\frac12\vec{K}\cdot\vec{r}}c_{\vec{k}-\vec{K}}\left(\pm \frac{V_{\vec{K}}}{|V_{\vec{K}}|}e^{i\frac12\vec{K}\cdot\vec{r}}+e^{-i\frac12\vec{K}\cdot\vec{r}}\right)\\
\end{align*}$$
- Assim, se:
    - $V_{\vec{K}}>0$ temos: $\psi_{\vec{k}}^{+}(\vec{r})\propto\cos\left(\frac12\vec{K}\cdot\vec{r}\right)~~;~~(\varepsilon_{+})$ e $\psi_{\vec{k}}^{+}(\vec{r})\propto\sin\left(\frac12\vec{K}\cdot\vec{r}\right)~~;~~(\varepsilon_{-})$ 
    - $V_{\vec{K}}<0$ temos: $\psi_{\vec{k}}^{+}(\vec{r})\propto\sin\left(\frac12\vec{K}\cdot\vec{r}\right)~~;~~(\varepsilon_{+})$ e $\psi_{\vec{k}}^{+}(\vec{r})\propto\cos\left(\frac12\vec{K}\cdot\vec{r}\right)~~;~~(\varepsilon_{-})$ 

