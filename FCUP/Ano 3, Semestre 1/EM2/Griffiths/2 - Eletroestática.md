# 1 - Campo Elétrico
## 1.1 - Introdução
![[carga fonte e de teste.png]]
- Consideremos o clássico problema de eletrodinâmica:
    - Temos as cargas $q_{1},q_{2},\dots,q_{i}$ - *cargas fonte* - cujas posições (em função do tempo) são conhecidas
    - Temos a carga $Q$ - *carga de teste* - para a qual queremos determinar a posição (em funnção do tempo).

- Para resolver isto usamos o **Princípio da Sobreposição** que nos diz que a interação entre 2 cargas ($q_{1},Q$) não é afetada pela existência de outras cargas ($q_{2},q_{3},\dots$). Na prática, isto significa que, para obter a força total aplicada em $Q$ basta determinar a força aplicada nela devido a $q_{1}$ (apenas): $\mathbf{F}_{1}$. Depois a força aplicada devido a $q_{2}$ (apenas): $\mathbf{F}_{2}$ . E por aí adiante. No final basta fazer: $\mathbf{F}=\mathbf{F}_{1} + \mathbf{F}_{2}+\mathbf{F}_{3}+\dots$ (sendo $\mathbf{F}$ a força total aplicada em $Q$)

- Ora, em eletrodinâmica há muitos fatores a considerar, como velocidade e aceleração de partículas. Como tal, iremos começar com eletroestática - em que as *cargas de fonte estão estacionárias* (mas a carga de teste pode-se mover).

## 1.2 - Lei de Coulomb
- Diz-nos que a força (em vetor) aplicada numa carga de teste $Q$ devido a uma carga fonte $q$, em repouso a uma distância $\mathbb{r}$, é dada por:
$$\mathbf{F}=\frac{1}{4\pi\varepsilon_{0}} \frac{qQ}{\mathbb{r}^{2}} \hat{\mathbb{r}}$$
em que $\varepsilon_{0}$ é a *permitividade do vácuo*: $\varepsilon_{0}= 8.85 \cdot 10^{-12} ~~C^{2}N^{-1}m^{-2}$
- De notar que no vetor de separação, $\vec{\mathbb{r}}=\mathbf{r}-\mathbf{r}'$ que temos acima, $\mathbf{r}$ é a posição de $Q$ e $\mathbf{r}'$ a posição de $q$. Ou seja, $\vec{\mathbb{r}}$ vai de $q$ para $Q$.

## 1.3 - Campo Elétrico
- Se tivermos $n$ cargas pontuais $q_{1},q_{2},\dots,q_{n}$ a distâncias $\mathbb{r}_{1},\mathbb{r}_{2},\dots, \mathbb{r}_{n}$ da carga $Q$, a força total aplicada em $Q$ é:
$$\mathbf{F}=\mathbf{F}_{1}+\mathbf{F}_{2}+\dots=\frac{1}{4\pi\varepsilon_{0}} \left(\frac{q_{1}Q}{\mathbb{r}_{1}^{2}}\hat{\mathbb{r}}_{1} + \frac{q_{2}Q}{\mathbb{r}_{2}^{2}}\hat{\mathbb{r}}_{2}+\dots\right) = \frac{Q}{4\pi\varepsilon_{0}} \left(\frac{q_{1}}{\mathbb{r}_{1}^{2}}\hat{\mathbb{r}}_{1} + \frac{q_{2}}{\mathbb{r}_{2}^{2}}\hat{\mathbb{r}}_{2}+\dots\right)$$
ou seja:
$$\mathbf{F}=Q \mathbf{E} \quad \quad;\quad \quad \mathbf{E}(\mathbf{r})=\frac{1}{4\pi\varepsilon_{0}} \sum\limits_{i=1}^{n} \frac{q_{i}}{\mathbb{r}_{i}^{2}}\hat{\mathbb{r}}_{i}$$
em que $\mathbf{E}$ é, claro, o **campo elétrico**.
- De notar que temos $\mathbf{E}(\mathbf{r})$ porque definimos $\hat{\mathbb{r}}_{i}$ como sendo $\hat{\mathbb{r}}_{i}= \dfrac{\mathbf{r}-\mathbf{r}_{i}}{||\mathbf{r}-\mathbf{r}_i||}$ em que $\mathbf{r}$ é a posição do ponto em que queremos determinar o campo elétrico e que, como tal, é constante neste sumatório. 
- Podemos pensar num campo como sendo uma entidade física que existe no espaço, mas arranjar uma verdadeira definição de campo pode ser difícil

## 1.4 - Distribuições de Carga Contínua
- Até agora vimos distribuições de cargas pontuais - distribuições discretas.
- Mas se esta carga estiver distribuida de forma contínua passamos a ter um integral:
$$\mathbf{E}(\mathbf{r})=\frac{1}{4\pi\varepsilon_{0}} \int \frac{1}{\mathbb{r}^{2}}\hat{\mathbb{r}} ~dq$$
- Se a carga estiver numa linha então temos $dq = \lambda dl'$ (em que $\lambda$ é a densidade linear de carga). Similarmente, com uma superfície de carga temos $dq = \sigma da'$ ($\sigma$ é a densidade superficial de carga) e com uma distribuição volúmica de carga temos $dq=\rho d \tau'$ ($\rho$ é a densidade volúmica de carga).
- Assim, o campo é definido como:
$$\large\boxed{\mathbf{E}(\mathbf{r})=\frac{1}{4\pi\varepsilon_{0}} \int \frac{\rho(\mathbf{r'})}{\mathbb{r}^{2}} \hat{\mathbb{r}} d \tau'}$$
isto é a fórmula para distribuição volúmicas. Distribuições lineares e superficiais acabam por ser casos particulares desta, sendo que temos a mesma fórmula, mas trocamos $\rho$ por $\lambda$ e $\sigma$.
- De notar que na definição da lei de Coulomb que vimos na secção atrás $\mathbb{r}$ era o vetor separação entre a carga $Q$ e a carga $q$. Agora é o vetor de separação entre $Q$ e $dl'/da'/d\tau'$. Além disso, agora $\mathbf{r}'$ é o vetor posição de um "bocadinho" de carga da distribuição.

# 2 - Divergente e Rotacional de Campos Eletroestáticos
## 2.1 - Linhas de Campo, Fluxo e Lei de Gauss
- Por vezes, os integrais que temos que fazer para determinar um certo campo podem ser muito complicados. Assim, veremos formas de simplificar os cálculos.

**Linhas de Campo**
- Consideremos um casos muito simples: campo gerado por uma carga pontual na origem. Temos: $$\mathbf{E}(\mathbf{r})=\frac{1}{4\pi\varepsilon_{0}} \frac{q}{r^{2}} \hat{r}$$
![[linhas de campo.png]]

- Podemos então traçar as **linhas de campo**. Vemos a direção do mesmo. Além disso, tem-se que onde há maior densidade de linhas de campo, o campo elétrico é mais intenso. Na realidade temos que desenhar o diagrama das linhas de campo em 3D para verdadeiramente representar corretamente o decréscimo do campo com $1/r^2$.
- De realçar que, ao desenhar estes diagramas, devemos desenhar um número de linhas necessário para que consigamos visualizar bem o campo. Além disso e por essa mesma razão, devemos espaçar as linhas de forma uniforme. 
- De recordar ainda que as linhas vão de cargas negativas para positivas, ou de positivas para o infinito ou do infinito para negativas. 

**Fluxo**
- Podemos pensar no fluxo de um campo elétrico por uma superfície $\mathcal{S}$ como o "número de linhas de campo a passar em $\mathcal{S}$", tendo-se:
$$\Phi_{E}=\int_\mathcal{S} \mathbf{E}\cdot d \mathbf{a}$$
![[fluxo campo eletrico.png]]

**Lei de Gauss**
- Assim, torna-se natural concluir que o fluxo de um campo elétrico através de uma superfície fechada é um indicador da carga que existe dentro da superfície. Se dentro dela tivermos um carga positiva, as linhas de campo terão de "sair" da superfície em direção a uma carga negativa ou para o infinito. Por outro lado, uma carga *fora* da superfície não terá fluxo nessa superfície, porque todas as linhas que "entram" de um lado saem do outro. Isto é a lógica da lei de Gauss.

- Esta lei, mais especificamente, baseia-se no facto que o fluxo de um campo elétrico gerado por uma carga $q$ através de uma superfície esféria de raio $r$ centrada em $q$ será:
$$\oint \mathbf{E}\cdot d \mathbf{a}=\int_{0}^{\pi}\int_{0}^{2\pi} \frac{1}{4\pi\varepsilon_{0}} \left(\frac{q}{r^{2}}\hat{r}\right) \cdot (r^{2}\sin \theta ~d \theta d \phi ~\hat{r})= \frac{q}{\varepsilon_{0}}$$
- Aqui devemos notar que se $r$ aumentar, a área da superfície aumenta e o campo na superfície diminui. Mas, ambos variam com $r^{2}$, pelo que estes termos cortam. Ou seja, temos que, para **QUALQUER** superfície fechada o fluxo do campo elétrico é $\dfrac{q}{\varepsilon_{0}}$. Mais uma vez, se os $r$ não ser anulassem isto não seria possível.

- Ora, se tivermos várias cargas dentro da superfície, teremos uma *carga total interior*, $Q_{int}$, tal que:
$$\large\boxed{\oint \mathbf{E}\cdot d\mathbf{a}=\frac{Q_{int}}{\varepsilon_{0}}}$$

- Podemos, na equação acima, reescrever o integral de área com o teorema da divergência:
$$\oint_\mathcal{S} \mathbf{E}\cdot d \mathbf{a}=\int_\mathcal{V} (\nabla \cdot \mathbf{E})d \tau$$
e podemos tratar a carga dentro da superfície como uma distribuição contínua de carga:
$$Q_{int} = \int_\mathcal{V}\rho ~d \tau$$
Se substituirmos estas 2 igualdades na lei de Gauss ficamos com 
$$\large \boxed{\nabla \cdot E = \frac{\rho}{\varepsilon_{0}}}$$
isto é a *lei de Gauss diferencial*.

## 2.2 - Divergente de $\mathbf{E}$
- Consideremos:
$$\mathbf{E}(\mathbf{r})=\frac{1}{4\pi\varepsilon_{0}} \int_\text{todo o espaço} \frac{\hat{\mathbb{r}}}{\mathbb{r}^{2}} \rho(\mathbf{r}')d \tau'$$
temos então o divergente:
$$\nabla \cdot \mathbf{E}=\frac{1}{4\pi\varepsilon_{0}} \int \nabla \cdot \left(\frac{\hat{\mathbb{r}}}{\mathbb{r}^{2}}\right) \rho(\mathbf{r}') d \tau'$$
vimos na secção de análise vetorial que $$\nabla \cdot \left(\frac{\hat{\mathbb{r}}}{\mathbb{r}^{2}}\right)=4 \pi \delta^{3}(\vec{\mathbb{r}})$$
logo:
$$\nabla \cdot \mathbf{E}=\frac{1}{4\pi\varepsilon_{0}} \int 4\pi \delta^{3}(\mathbf{r}-\mathbf{r}') \rho(\mathbf{r}')d \tau'=\frac{\rho(\mathbf{r})}{\varepsilon_{0}}$$

## 2.3 - Aplicações da Lei de Gauss
- Basicamente, ao imaginar uma superfície em que aplicamos a lei de gauss - *Superfície Gaussiana* - conseguimos simplificar muitos problemas.
- Por exemplo, se queremos saber o campo gerado por uma esfera com densidade de carga, usaremos uma superfície gaussiana que é uma esfera com um um raio maior que o da esfera com carga. Com isto, conseguimos obter o módulo de $\mathbf{E}$ que, se a densidade de carga for constante, dependerá apenas da distância ao centro da esfera.

- Assim, o fator mais importante de um problema deste é a sua *simetria*. Assim, temos as superfícies gaussianas para os 3 casos clássicos:
    - *Simetria esférica* - Superfície esférica e concêntrica
    - *Simetria cilíndrica* - Superfície cilíndrica com o mesmo eixo central
    - *Simetria plana* - Superfície de formato "pillbox" (paralelepípedo ou cilindro) que atravesse a superfície.

## 2.4 - Rotacional de $\mathbf{E}$
- Novamente, consideremos um campo elétrico gerado por uma carga pontual $q$ na origem, num ponto a uma distância $r$:
$$\mathbf{E}=\frac{1}{4\pi\varepsilon_{0}} \frac{q}{r^{2}} \hat{r}$$
- Apenas pelas linhas de campo vemos que o rotacional será zero. Mas vejamos isto de uma forma mais formal.

- Calculemos o integral de linha deste campo em $\mathbf{a}\to \mathbf{b}$:
$$\int_\mathbf{a}^{\mathbf{b}} \mathbf{E}\cdot d \mathbf{l} ~~~~~~;~~~~~~ d \mathbf{l}=dr~\hat{r} + r d \theta~\hat{\theta} + r \sin \theta d \phi~\hat{\phi}$$
Ficamos então com $$\int_\mathbf{a}^{\mathbf{b}} \mathbf{E} \cdot d \mathbf{l}=\frac{1}{4\pi \varepsilon_{0}} \int_\mathbf{a}^{\mathbf{b}} \frac{q}{r^{2}}dr=\frac{-1}{4\pi\varepsilon_{0}} \Biggr|_{r_{a}}^{r_{b}} =\frac{1}{4\pi\varepsilon_{0}}\left(\frac{q}{r_{a}} - \frac{q}{r_{b}}\right)$$
- Assim, se $r_{a}=r_{b}$, ou seja, se integrarmos num percurso fechado, temos: $$\oint \mathbf{E} \cdot d \mathbf{l}=0 \longrightarrow \nabla \times \mathbf{E}=0$$
acima usamos o teorema do rotacional.

- As contas acima foram feitas para 1 carga pontual. Mas se tivermos várias cargas pontuais ficamos com:
$$\nabla \times \mathbf{E}=\nabla \times(\mathbf{E}_{1}+\mathbf{E}_{2}+\dots)=(\nabla \times \mathbf{E}_{1}) + (\nabla \times \mathbf{E}_{2})+\dots=0$$
ou seja, o rotacional do campo elétrico é *zero para qualquer distribuição estática de carga*.

# 3 - Potencial Elétrico
## 3.1 - Introdução
- Acabamos de ver que o campo elétrico é definido por uma função vetorial de *rotacional nulo*.
- Assim, podemos escrevê-lo como o gradiente de um *pontencial*. Isto permite-nos transformar problemas vetoriais em problemas escalares.
- Além disso, conforme os 4 pontos que vimos para um campo vetorial irrotacional, para um campo elétrico
    - um integral de linha depende apenas do ponto final e inicial 
    - integrais de linha em percursos fechados são sempre nulos

- Assim, podemos definir:
$$\large \boxed{V(\mathbf{r})=- \int_\mathcal{O}^{\mathbf{r}}\mathbf{E}(\mathbf{r}')\cdot d \mathbf{l}'}$$
em que $\mathcal{O}$ é um ponto de referência.
- A DDP entre 2 pontos $\mathbf{a},\mathbf{b}$ será:
$$\begin{align*}
V(\mathbf{b})-V(\mathbf{a})&= - \int_\mathcal{O}^{\mathbf{b}}\mathbf{E}\cdot d \mathbf{l} + \int_\mathcal{O}^{\mathbf{a}}\mathbf{E}\cdot d \mathbf{l} \\
&= - \int_\mathcal{O}^{\mathbf{b}}\mathbf{E}\cdot d \mathbf{l} - \int_\mathbf{a}^{\mathcal{O}}\mathbf{E}\cdot d \mathbf{l}\\
&= - \int_\mathbf{a}^{\mathbf{b}} \mathbf{E} \cdot d \mathbf{l}
\end{align*}$$
- Ora, o teorema fundamental do gradiente dá-nos que: $\large \int_{a}^{b} \nabla V \cdot d \mathbf{l}=V(b)-V(a)$
- Assim, juntando as 2 equações, ficamos com $$\int_\mathbf{a}^{\mathbf{b}}(\nabla V)\cdot d \mathbf{l} = - \int_\mathbf{a}^{\mathbf{b}}\mathbf{E}\cdot d \mathbf{l}$$
- Ou seja:
$$\large \boxed{\mathbf{E} = - \nabla \mathbf{V}}$$

## 3.2 - Notas sobre Potencial
1. **Nome** - "Potencial" $\ne$ "Energia Potencial", mas estão relacionados. Além disso, uma região em que o potencial é igual em todos os pontos diz-se *equipotencial*.
2. **Vantagem** - Podemos facilmente "saltar" entre a função escalar potencial e a função vetorial campo, basta fazer o gradiente do potencial. Isto pode parecer estranho, porque no potencial temos 1 função e no campo 3. No entanto, devido ao facto que $\nabla \times \mathbf{E}=\vec{0}$, as funções de $\mathbf{E}$ não são independentes.
3. **Ponto de referência** ($\mathcal{O}$) - Atrás usamos um "ponto de referência" para definir potencial elétrico. Ora, este é *arbitrário*. Isto porque, se fizermos uma mudança de ponto de referência temos: $$V'(\mathbf{r})=-\int_\mathcal{O~'}^{\mathbf{r}}\mathbf{E} \cdot d \mathbf{l}=-\int_\mathcal{O~'}^{\mathcal{O}}\mathbf{E}\cdot d \mathbf{l}-\int_\mathcal{O}^{\mathbf{r}}\mathbf{E} \cdot d \mathbf{l}= C + V(\mathbf{r})$$
    - Ou seja, apenas se acrescenta uma constante. Ora, se calcularmos uma DDP, como esta constante existe em ambos os potenciais, ela acaba por se anular. Além disso, ela não irá ter qualquer efeito no gradiente do potencial. Como tal, o potencial elétrico só por si não tem qualquer significado físico, porque o seu valor é arbitrário.
    - Frequentemente, usa-se $\mathcal{O}=\infty$ (um ponto infinitamente longe da carga) em que temos $V=0$. Como tal, não podemos fazer isto quando a distribuição de cargas também se extende para o infinito ou em que este "explode" no infinito. Nesses casos podemos simplesmente escolher um ponto de referencial conhecido.
4. **Princípio da Sobreposição** - Pelo princípio da sobreposição temos  $\mathbf{F}=\mathbf{F}_{1}+\mathbf{F}_{2}+\dots$. Ora, como $\mathbf{F}=Q \mathbf{E}$ temos que o princípio da sobreposiçaõ se aplica ao campo elétrico: $\mathbf{E}=\mathbf{E}_{1}+\mathbf{E}_{2}+\dots$. Ora, como o campo é gradiente do potencial facilmente vemos que: $V=V_{1}+V_{2}+\dots$. Ou seja, este princípio aplica-se ao potencial.
5. **Unidadeds** - Usasse o Volt ($V$) AKA Joule por Coulomb ($JC^{-1}$)
6. **Lei de Gauss** - Não se podemos usá-la para obter potencial a partir de campo, já que ela apenas mede o "fluxo total". Ou seja, o potencial fora de uma superfície afeta o que está dentro dela.

## 3.3 - Equações de Poisson e Laplace
- Acima vimos que $$\mathbf{E}=-\nabla V$$
- Mas sabemos ainda que $$\nabla \cdot \mathbf{E}= \frac{\rho}{\varepsilon_{0}} ~~~~~~;~~~~~~ \nabla \times \mathbf{E}= \vec{0}$$
- Ora, temos $\nabla \cdot \mathbf{E}=\nabla \cdot (- \nabla V)=- \nabla^{2} V$. Assim ficamos com a **Equação de Poisson**:
$$\large \boxed{\nabla^{2}V=- \frac{\rho}{\varepsilon_{0}}}$$

- Ora, quando não existe carga temos $\rho=0$. Aí temos a **Equação de Laplace**:
$$\large\boxed{\nabla^{2}V=0}$$

## 3.4 - Potencial de Distribuição de Carga Localizada
- Acima definimos $V$ como uma integral de $\mathbf{E}$, mas normalmente iremos trabalhar ao contrário: Usar $V$ para obter $\mathbf{E}$.
- Ora, a equação de Poisson relaciona $V$ e $\rho$. Ora, frequentemente conhecemos $\rho$. Mas ainda assim, esta equação está "ao contrário" - ela dá-nos $\rho$ a partir de $V$. Assim, queremos "inverter" a equação de Poisson.

- Consideremos uma carga pontual na origem. Temos, como já vimos atrás:
$$\mathbf{E}= \frac{1}{4\pi\varepsilon_{0}} \frac{q}{r^{2}} \hat{r}~~~~~~;~~~~~~ d \mathbf{l}=dr~\hat{r} + r d \theta~\hat{\theta} + r \sin \theta d \phi~\hat{\phi}$$
Assim:
$$\mathbf{E} \cdot d \mathbf{l}=\frac{1}{4\pi\varepsilon} \frac{q}{r^{2}} dr$$
- Logo:
$$V(r)=-\int_\mathcal{O}^{\mathbf{r}} \mathbf{E} \cdot d \mathbf{l} = \frac{-1}{4\pi\varepsilon_{0}} \int_{\infty}^{r} \frac{q}{r'~^{2}}dr' = \frac{1}{4\pi\varepsilon_{0}} \frac{q}{r}$$

- De notar aqui que o sinal "menos" na definição de $V$ serve para fazer com que potencial reduzido indique carga negativa e potencial mais elevado indique carga positiva. Assim, sendo o campo elétrico o simétrio do gradiente do potencial, o campo aponta para onde o potencial desce, ou seja, de positivo para negativo. (De recordar que um gradiente aponta para a zona de maior aumento)

- Temos então que o potencial de uma carga pontual é $V(\mathbf{r})=\frac{1}{4\pi\varepsilon_{0}} \frac{q}{\mathbb{r}}$
- O potencial gerado por $n$ cargas pontuais será:
$$V(\mathbf{r})=\frac{1}{4\pi\varepsilon_{0}} \sum\limits_{i=1}^{n} \frac{q_{i}}{\mathbb{r}_{i}}$$
- O potencial de uma distribuição contínua de carga é: $$V(\mathbf{r})=\frac{1}{4\pi\varepsilon_{0}} \int \frac{\rho(\mathbf{r}')}{\mathbb{r}} d \tau'$$
- Isto é a "inversão" da equação de poisson que queríamos. Uma delas, aliás. Isto é a solução da equação de Poisson para distribuições de carga localizadas.
- Notamos que isto é quase igual à fórmula que nos dá o campo elétrico, só que temos $\mathbb{r}$ em vez de $\mathbb{r}^{2}$ no denominador, e agora é tudo escalar.

## 3.5 - Condições de Fronteira
- A maioria dos problemas de eletroestática são do tipo: "conhecendo esta distribuição de carga, determina o campo que esta gera". A menos que a simetria permita usar a lei de gauss, temos que começar sempre por determinar o potencial.
- Ou seja, num problema de eletroestática temos 3 quantidades fundamentais: carga, campo e potencial. Ora, temos 6 fórmulas que os relacionam e que já fomos vendo neste capítulo:
![[carga, tensao e campo.png]]

- Ao resolver problemas torna-se claro que o campo elétrico apresenta uma descontinuidade ao passar numa superfície com carga. Consideremos uma superfície com densidade de carga $\sigma$. Imaginemos uma superfície gaussiana de forma "pillbox" com base de área $A$ e altura $h$ que atravessa a superfície. Pela lei de Gauss temos:
$$\oint_\mathcal{S} \mathbf{E} \cdot d \mathbf{a}=\frac{1}{\varepsilon_{0}} Q_{int} = \frac{\sigma A}{\varepsilon_{0}}$$
- Ora, para que a curvatura da superfície não seja um problema, consideremos que $h\to0,A\to0$. Ou seja, é como se tivessemos uma superfície plana com carga. Assim, o campo gerado nos lados da "pillbox" é nulo (porque estamos no limite $h\to0$ e estes lados basicamente deixam de existir). 
- Definindo $E_\text{cima}^{\perp}$ como sendo a componte do campo gerado pela superfície para "cima" que é perpendicular a esta e $E_\text{baixo}^{\perp}$ como sendo o mesmo, mas gerado para baixo. Obtemos então:
$$E_\text{cima}^{\perp}- E_\text{baixo}^{\perp} = \frac{\sigma}{\varepsilon_{0}}$$
- Ou seja, a componente do campo elétrico perpendicular à superfície apresenta uma descontinuidade de $\frac{\sigma}{\varepsilon_{0}}$ em qualquer superfície carregada.
- A componente tangente à superfície é sempre contínua. Se fizermos um "loop" a intersetar a superfície como vemos abaixo, verificasse que as componentes tangentes acima e abaixo são iguais:
![[campo acima e abaixo de plano.png]]

- Juntando as componentes perpendicular e tangente temos:
$$\mathbf{E}_\text{cima} - \mathbf{E}_\text{baixo}= \frac{\sigma}{\varepsilon_{0}} \hat{n}$$
em que $\hat{n}$ é o vetor unitário perpendicular à superfície, que aponta de cima para baixo.

- Por outro lado, o potencial é sempre contínuo atráves de uma superfície carregada. De notar que para verificar isto, fazemos $V(\mathbf{a})-V(\mathbf{b})=-\int_\mathbf{a}^{\mathbf{b}}\mathbf{E} \cdot d \mathbf{l}$ (em que $\mathbf{a}$ está acima da superfície e $\mathbf{b}$ abaixo) para o limite em que $|\mathbf{b}-\mathbf{a}|\to0$ e obtemos $V(\mathbf{b})=V(\mathbf{a})$
- Claro, como $\mathbf{E}=- \nabla V$, o gradiente do potencial já não vai manter esta continuidade na superfície. Temos que $$\nabla V_\text{cima} - \nabla V_\text{baixo} = - \frac{\sigma}{\varepsilon_{0}}\hat{n}$$
- O que nos dá:
$$\frac{\partial V_\text{cima}}{\partial n}- \frac{\nabla V_\text{baixo}}{\partial n}=- \frac{\sigma}{\varepsilon_{0}}$$
ou seja:
$$\frac{\partial V}{\partial n}=\nabla V \cdot \hat{n}$$
esta é a *derivada normal* de $V$. (Ou seja, a dericada direcional de $V$ na direção perpendicular)

# 4 - Trabalho e Energia em Eletroestática
## 4.1 - Trabalho necessário para mover uma carga
- Consideremos que se tem uma carga de teste $Q$. Queremos movê-la da posição $\mathbf{a}$ para a posição $\mathbf{b}$. Ora, queremos saber o trabalho que teríamos de fazer para que isso aconteça. 
- Ora, em cada ponto do percurso realizado, a força aplicada na carga é $\mathbf{F}=Q \mathbf{E}$. Assim, para anular esta força temos que aplicar uma força $-Q \mathbf{E}$. Ora, poderíamos aplicar uma força maior que esta (em módulo), mas isso iria gerar energia cinética desnecessariamente. Ou seja, iremos apenas estudar o caso em que se aplica a força mínima necessária.
- Assim, o trabalho ao longo do percurso será:
$$W = \int_\mathbf{a}^{\mathbf{b}}(- \mathbf{F})\cdot d \mathbf{l}=-Q\int_\mathbf{a}^{\mathbf{b}}\mathbf{E} \cdot d \mathbf{l}=Q [V(\mathbf{b})-V(\mathbf{a})]$$
vemos que o trabalho realizado não depende do percurso escolhido. Isto mostra-nos que a *força eletroestática é conservativa*. Isto já nos era indicado por o campo elétrico ser irrotacional. Podemos reescrever a equação acima como: $V(\mathbf{b})-V(\mathbf{a})=W/Q$. Ou seja, a DDP entre 2 pontos é o trabalho por unidade de carga necessários para mover uma partícula entre esses pontos.

- Por outro lado, se considerarmos $\mathbf{a}=\infty$ e $\mathbf{b}=\mathbf{r}$, ou seja, se estivermos a trazer a partícula do infinito para uma posição $\mathbf{r}$, o trabalho necessário será: $$W_{\infty \to \mathbf{r}}=Q V(\mathbf{r})$$
E neste caso ("montar" um sistema de cargas) o potencial das cargas não passa da sua energia potencial (trabalho) por unidade de carga.

## 4.2 - Energia de uma Distribuição de Cargas Pontuais
- Consideremos que temos um espaço de vácuo e queremos montar um sistema de cargas pontuais. Para isto, considerasse que as cargas são trazidas do infinito para as suas posições.
- A primeira carga, $q_{1}$, não exige realizar qualquer trabalho. 
- Ao trazer a  segunda carga, $q_{2}$, já teremos que combater a força gerada pela interação entre $q_{1},q_{2}$. Assim $W_{2}=q_{2}V_{1}(\mathbf{r}_{2})$, ou seja: $$W_{2}=\frac{1}{4\pi\varepsilon_{0}} q_{2} \left(\frac{q_{1}}{\mathbb{r}_{12}}\right)$$
(sendo que o módulo do vetor separação, neste caso, dá-nos a distância entre as 2 cargas quando já estiverem em posição)
- Para trazer a terceira carga para o sistema precisamos de combater a interação desta com $q_{1},q_{2}$. Assim: 
$$\begin{align*}
W_{3}&= q_{3}[V_{1}(\mathbf{r}_{3})+V_{2}(\mathbf{r}_{3})]\\
&= \frac{1}{4\pi \varepsilon_{0}}q_{3} \left( \frac{q_{1}}{\mathbb{r}_{13}} + \frac{q_{2}}{\mathbb{r}_{23}} \right)
\end{align*}$$
- Analogamente para $q_4$, tal que:
$$\begin{align*}
W_{3}&= q_{4}[V_{1}(\mathbf{r}_{4})+V_{2}(\mathbf{r}_{4})+V_{3}(\mathbf{r}_{4})]\\
&= \frac{1}{4\pi \varepsilon_{0}}q_{4} \left( \frac{q_{1}}{\mathbb{r}_{14}} + \frac{q_{2}}{\mathbb{r}_{24}} + \frac{q_{3}}{\mathbb{r}_{34}} \right)
\end{align*}$$
- Assim, o trabalho necessário para montar este sistema de 4 cargas é:
$$W = \frac{1}{4\pi\varepsilon_{0}} \left(\frac{q_{1}q_{2}}{\mathbb{r}_{12}} + \frac{q_{1}q_{3}}{\mathbb{r}_{13}}+ \frac{q_{1}q_{4}}{\mathbb{r}_{14}} + \frac{q_{2}q_{3}}{\mathbb{r}_{23}} + \frac{q_{2}q_{4}}{\mathbb{r}_{24}} + \frac{q_{3}q_{4}}{\mathbb{r}_{34}}\right)$$
- De forma geral:
$$W = \frac{1}{4\pi\varepsilon_{0}} \sum\limits_{i=1}^{n} \sum\limits_{j>i}^{n} \frac{q_{i}q_{j}}{\mathbb{r}_{ij}}=\frac{1}{8\pi\varepsilon_{0}} \sum\limits_{i=1}^{n} \sum\limits_{j\neq i}^{n} \frac{q_{i}q_{j}}{\mathbb{r}_{ij}}$$
acima, a primeira fórmula usa $j>i$ para garantir que não contamos os mesmos pares de interações 2 vezes. Na segunda, contamos propositadamente todos os pares 2 vezes e depois dividimos por 2. De notar, na segunda equação, torna-se evidente que a ordem em que se monta o sistema é irrelevante.
- Podemos então usar a sefunda formula para escrever isto na forma:
$$W = \frac12 \sum\limits_{i=1}^{n} q_{i} \left(\sum\limits_{j\neq i}^{n} \frac{1}{4\pi\varepsilon_{0}} \frac{q_{j}}{\mathbb{r}_{ij}} \right)$$
aqui vemos claramente que o termo entre parêntesis corresponde ao potencial gerado pela carga $q_{j}$ num ponto $\mathbf{r}_{i}$. Ou seja, para calcular o trabalho acabamos por usar o potencial de todas as cargas que, *no final*, constituem o sistema, não só as cargas que já estavam presentes no momento em que colocamos uma carga $q_{i}$. Ou seja, podemos reescrever isto na forma:
$$W =\frac12 \sum\limits_{i=1}^{n} q_{i} V(\mathbf{r_{i}})$$
- Esta é então a energia necessária para montar o sistema, ou seja, a energia armazenada no sistema.

## 4.3 - Energia de uma Distribuição Contínua de Carga
- A equação de $W$ no final da secção 4.2, para distribuições contínuas, transforma-se em:
$$W = \frac12 \int \rho V d \tau$$
mas podemos reescrever isto de outra forma.

- Usemos a Lei de Gauss para resscrever $\rho$:
$$\nabla \cdot \mathbf{E}=\frac{\rho}{\varepsilon_{0}} \longrightarrow \rho= \varepsilon_{0} \nabla \cdot \mathbf{E}\longrightarrow W = \frac{\varepsilon_{0}}{2} \int(\nabla \cdot \mathbf{E})V d \tau$$
façamos integração por partes (ver secção 3.6 do capítulo 1):
$$\begin{align*}
W &=  \frac{\varepsilon_{0}}{2} \left[- \int \mathbf{E}\cdot (\nabla V) d \tau + \oint V \mathbf{E}\cdot d \mathbf{a}\right]\\
W &= \frac{\varepsilon_{0}}{2} \left(\int_\mathcal{V} E^{2} d \tau + \oint_\mathcal{S} V \mathbf{E}\cdot d \mathbf{a}\right)
\end{align*}$$
a segunda igualdade veio de $\mathbf{E}=-\nabla V$, logo: $\mathbf{E} \cdot \nabla V=\mathbf{E} \cdot (- \mathbf{E})=- E^{2}$

- De notar agora que o volume (e respetiva superfície de limite) é um volume em que toda a distribuição de carga está contida. A equação acima funciona para qualquer volume escolhido.
- Mas porque não integrar em todo o espaço para 100% garantir que a distribuição está contida? Ora, ao fazer isto a primeira parcela só aumenta: $\mathcal{V}\to \infty$. A segunda parcela, no entanto, é eliminada: $V$ diminui com $1/r$, $E$ diminui com $1/r^{2}$ e a integral de área aumenta com $r^{2}$. Ou seja, a segunda parcela inteira diminui com $1/r$, pelo que desaparece.
- Ficamos então com:
$$\boxed{W = \frac{\varepsilon_{0}}{2} \int_\text{todo o espaço} E^{2} d \tau}$$

## 4.4 - Notas sobre Energia Eletroestática
1. **"Inconsistência"** - A equação de $W$ com $E^{2}$ vai ser sempre positiva, enquanto que aquela com $q_{i} V$ pode ser positiva ou negativa. Qual está correta?
     - Ambas estão corretas, mas indicam coisas diferentes:
         - $W =\frac12 \sum\limits_{i=1}^{n} q_{i} V(\mathbf{r_{i}})$ não considera o trabalho necessário para *criar as cargas*, apenas o trabalho necessário para as trazer do infinito para o sistema.
         - $W = \frac{\varepsilon_{0}}{2} \int E^{2} d \tau$ considera essa energia. De tal forma que se aplicarmos esta fórmula a uma carga pontual temos: $W=\infty$.
     - Ou seja, a equação com $E^{2}$ é mais completa, mas não a devemos usar em sistemas de cargas pontuais porque nesses casos é preferível ignorar a "energia de criação" das cargas.
     - Esta "inconsistência" surge de fazermos a passagem: $W =\frac12 \sum\limits_{i=1}^{n} q_{i} V(\mathbf{r_{i}}) \Longrightarrow W = \frac12 \int \rho V d \tau$. 
         - Na primeira, o termos $V(\mathbf{r}_{i})$ é o potencial de *todas as outras* cargas, daí não considerarmos a energia de criação da carga $q_{i}$. Na segunda temos um distribuição contínua, pelo que não há distinção entre uma carga e as restantes, e então contamos a energia de criação.
1. **Onde é que a energia está armazenada** - Acima temos 2 fórmulas que nos permitem obter a energia de uma distribuição contínua: uma com $\rho V$, outra com $E^{2}$. Assim, onde está armazenada a energia: na carga ou no campo?
    - Não sabemos. O que importa é saber como obter a energia total, não *onde* ela está. Sendo assim, podemos dizer que ela está armazenada no campo com uma densidade $\frac12 \varepsilon_{0} E^{2}$, ou na carga com uma densidade $\frac12 \rho V$
2. **Princípio da Sobreposição** - A energia eletroestática não cumpre este princípio: $$W = \frac{\varepsilon_{0}}{2}\int E^{2}d \tau = \frac{\varepsilon_{0}}{2}\int (\mathbf{E}_{1}+\mathbf{E}_{2})^{2}d \tau = W_{1} + W_{2} + \varepsilon_{0}\int \mathbf{E}_{1}\cdot \mathbf{E}_{2} d \tau$$

# 5 - Condutores
## 5.1 - Propriedades Básicas
- Num isolador, os eletrões estão presos aos respetivos átomos
- Num condutor tem-se 1 ou 2 eletrões livres por átomo. Um condutor ideal teria infinitas cargas livres.

Vejamos então propriedades de condutores ideiais:
#### $E=0$ dentro do condutor
- Uma razão é que, se existisse campo dentro do condutor também existiriam cargas livres dentro dele (Lei de Gauss). Ora, essas cargas iam-se mover e já não teríamos eletroestática.
- A razão mais útil é explicada pela seguinte imagem:
![[dieletrico.png]]
Temos um condutor sem carga. Se aplicarmos no condutor um campo externo $\mathbf{E}_{0}$, iram-se gerar 2 regiões com cargas opostas (por movimento dos eletrões livres da direita para a esquerda). Ora, estas regiões de carga *induzida* irão criar um segundo campo elétrico $\mathbf{E}_{1}$ que *anula o outro*.

#### $\rho=0$ dentro do condutor
- Esta expliquei acima. Se não há campo dentro do condutor, pela Lei de Gauss, também não há carga. Logo $\rho=0$. Na realidade, como o condutor é formado por átomos, temos cargas, mas a *carga total* dentro do condutor é nula.

#### Cargas livres existem apenas na superfície
- Era o único sítio possível :)

#### Condutores são equipotenciais
- Como o campo dentro do condutor é nulo, tendo 2 pontos $\mathbf{a},\mathbf{b}$ dentro ou na superfície do condutor temos que: $$V(\mathbf{b})-V(\mathbf{a})=-\int_\mathbf{a}^{\mathbf{b}}\mathbf{E}\cdot d \mathbf{l}=0 \longrightarrow V(\mathbf{b})=V(\mathbf{a})$$

#### $\mathbf{E}$ é perpendicular à superfície
- Caso contrário, as cargas na superfície iam-se mover e eventualmente eliminar a componente tangencial do campo.

## 5.2 - Cargas Induzidas
- Se tivermos um condutor e aproximarmos uma carga $+q$ iremos verificar que eles se atraem. Isto ocorre porque
    - A carga $+q$ atrai as cargas negativas para o seu lado do condutor e repele as positivas
    - OU, podemos interpretar como: a carga na superfície do condutor move-se de forma a que o conjunto de carga positiva (superfície com carga positiva e carga $+q$ ) não gerem um campo dentro do condutor.

- De notar ainda que quando se diz "dentro do condutor", queremos dizer dentro do material do condutor em si. Se houver uma cavidade em vácuo dentro do condutor, nele pode haver campo. No entanto é essencial que ao fazer uma superfície gaussiana dentro do condutor que englobe essa cavidade inteira a carga interna total seja nula. Ou seja, temos algo como abaixo:
![[condutor.png]]

- Por outro lado, se houver uma cavidade dentro do condutor em que não há carga, tem-se que o campo dentro dela também será zero. 
    ![[condutor nao tem carga dentro.png]]
    - Imaginemos que nas bordas internas do condutor / bordas da cavidade tínhamos zonas com carga positiva e com carga negativa. Tem-se que qualquer linha de campo teria que ir do positivo para o negativo. Se traçarmos um percurso fechado da carga positiva para a negativa, de volta para a positiva, temos que o percurso teria que passar pelo condutor para voltar para a positiva. Ora, no condutor o campo é nulo. Ou seja, $\oint \mathbf{E}\cdot d \mathbf{l}\ne 0$ para este percurso, o que é impossível.
- Isto é o fenómeno por trás de uma *gaiola de Faraday* / Faraday Cage.

## 5.3 - Carga Superficial e Força num Condutor
- Conforme a descontinuidade do campo elétrico numa superfície carregada que vimos atrás, o campo imediatamente fora do condutor será: $$\mathbf{E}=\frac{\sigma}{\varepsilon_{0}} \hat{n}$$
- Mas vimos ainda que conseguimos obter $\sigma$ com o potencial: $$\sigma=- \varepsilon_{0} \frac{\partial V}{\partial n}$$
estas equações permitem-nos obter a densidade de carga na superfície de um condutor, se soubermos $\mathbf{E}$ ou $V$.

![[campo na superficie de condutor.png]]
- Passemos agora à segunda parte desta secção: consideremos que numa superfície carregada é aplicada um campo externo. Assim, nas cargas vai ser aplicada uma força $\mathbf{f}=\sigma \mathbf{E}$. Mas, como sabemos, na superfície em si o campo é descontínuo. Assim, usamos o campo acima ou abaixo? Usamos a *média* (explicação de porquê na página 104 do Griffiths): $$\mathbf{f}=\sigma \mathbf{E}_\text{médio}=\frac12 \sigma (\mathbf{E}_\text{cima}+\mathbf{E}_\text{baixo})$$
- No caso de um condutor, o campo dentro é $\vec{0}$ e fora é $\frac{\sigma}{\varepsilon_{0}}\hat{n}$. Assim o campo médio é $\mathbf{E}_\text{médio}= \frac{\sigma}{2\varepsilon_{0}}\hat{n}$ e temos a força por área:
$$\mathbf{f}= \frac{\sigma^{2}}{2\varepsilon_{0}}\hat{n}$$
Isto resulta numa pressão eletroestática igual a $$P = \frac{\varepsilon_{0}}{2} E^{2}$$

## 5.4 - Condensadores
![[condutores carga oposta.png]]
- Temos 2 condutores como acima, um com carga $+Q$, outro com carga $-Q$. Devido às propriedades dos condutores, sabemos que um condutor está todo ao mesmo potencial. Assim a DDP entre eles é:
$$V = V_{+} - V_{-} =\int_{-}^{+}\mathbf{E}\cdot d \mathbf{l}$$
- Nós não conhecemos as distribuições das cargas e as formas dos condutores podem ser muito complicadas, pelo que o campo elétrico pode ser muito difícil de calcular. 
- No entanto, pela Lei de Coulomb, sabemos sempre que $\mathbf{E}=\frac{1}{4\pi\varepsilon_{0}} \int \frac{\rho}{\mathbb{r}^{2}} \hat{\mathbb{r}}~d \tau$, ou seja, $\mathbf{E}\propto \rho$. Assim, se a carga duplicar, o campo duplica (de notar que duplicar $Q$ duplica $\rho$ e vice-versa).
- Assim, se $\mathbf{E}\propto \rho$, também temos que $V\propto\rho$. Ora, a constante de proporcionalidade entre estes é a *capacidade* do sistema: $$C\equiv \frac{Q}{V}$$
sendo que esta quantidade é determinada pelo tamanho, forma e distância entre os 2 condutores. 
- Tem a unidade SI *farad* $F$ ($CV^{-1}$). De notar que esta unidade é desnecessariamente grande. Normalmente trabalhamos com microfarad e picofarad.
- Na fórmula de $C$ acima, $V=V_{+}-V_{-}$, enquanto que $Q$ será a carga do condutor positivo. Assim, $C$ é sempre positivo.
- Por vezes falasse na capacidade de 1 condutor. Nesse caso consideramos que o segundo condutor, que tem a carga negativa, é uma superfície esférica imaginária de raio infinito que envolve o condutor real.

#### Trabalho
- Para "carregar" um condensador temos que remover os eletrões da placa positiva e movê-los para a negativa. Para fazer isto temos que combater o campo elétrico (que cria uma força nos eletrões que os empurra de volta para a placa positiva).
- Assim, qual o trabalho que temos de fazer para carregar o condensador?
- Num certo ponto do "carregamento", a carga que temos na placa positiva é $q$, pelo que a DDP entre as placas é $q/C$. Pela fórmula $W=QV$ que vimos atrás, o trabalho necessário para mover o próximo bocadinho de carga será: $$dW = \frac{q}{C} dq$$
- Assim, o trabalho total necessário para carregar o condensador é: $$W = \int_{0}^{Q} \frac{q}{C}dq=\frac12 \frac{Q^{2}}{C}=\frac12 CV^{2}$$