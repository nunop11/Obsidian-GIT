# 1 - Limitações da Física Estatística Clássica
## 1.1 - Gás de interação reduzida
- Temos o hamiltoniano:
$$H(\vec{\mu})=\sum\limits_{i=1}^{n} \frac{\vec{p}_{i}^{2}}{2m_{i}}+U(\vec{q_{1}},\dots,\vec{q_{n}})$$
- Com ele podemos obter a função de partição canónica:
$$Z=\frac{Z_{1}^{N}}{N!} \quad \quad;\quad \quad Z_{1}=\int e^{-\beta H(\vec{\mu})}\frac{d\vec{\mu}}{h^{3n}}$$
**Deformações Moleculares**
- Às temperaturas que normalmente consideramos, as moléculas têm uma forma fixa e apenas so  frem ligeiras deformações. 
- Vejamos como determinar a sua contribuição:

**Mínimo de energia potencial**
- Vamos determinar as posições $\vec{q}_{1}^{*},\dots \vec{q}_{n}^{*}$ que minimizam a energia potencial (posições de equilíbrio):
$$U = U^*(\textbf q_i^*, \dots, \textbf q_n^*) + \frac12 \sum_{i,j=1}^n\sum_{\alpha,\beta=1}^3 \frac{\partial^2 U}{\partial q_{i,\alpha}\partial q_{j,\beta}}\Big\vert_{Q^*}(q_{i,\alpha} - q_{i,\alpha}^*)(q_{j,\beta} - q_{j,\beta}^*)+\dots$$
em que fizemos expansão em Taylor ($f(x)=f(a)+f'(a)(x-a)+ \frac{1}{2}f''(a)(x-a)$ em que $x,a$ são $\vec{q},\vec{q^{*}}$). O termo da primeira derivada não aparece por ser nulo nos pontos mínimos.
- De notar que $\alpha,\beta$ apenas decompõe os vetores nas suas componentes $x,y,z$ ($1=x,2=y,3=z$)

- Podemos escrever esta equação na forma:
$$U\approx U^{*}+ \frac{1}{2} \sum\limits_{i,j,\alpha,\beta}(q_{i,\alpha}-q_{i,\alpha}^{*})U_{i\alpha,j\beta}(q_{j\beta}-q_{j\beta}^{*})$$
em que:
    - $U^{*}$ é um vetor que tem o potêncial nas posições de equilíbrio
    - $q_{i}$ é um vetor com as posições das partículas
    - $q_{i}^{*}$ é um vetor com as posições de equilíbrio
    - $U$ é uma matriz *hessiana* da energia potencial (em que o elemento $(i,j)$ é dado por $\frac{\partial^{2}U}{\partial q_{i,\alpha}\partial q_{j,\beta}}(Q^*)$)

Nota sobre a matriz $U$:
    - Em cada bloco $(\alpha,\beta)$ temos uma submatriz $n\times n$, ou seja, $U$ tem dimensões $3n\times 3n$
    - A matriz é simétrica e diagonalizável 

>Exemplo para $n=2$:
$$\begin{align*}
\sum\limits_{i,j=1}^{2}\sum\limits_{\alpha,\beta=1}^{3}\frac{\partial^{2}U}{\partial q_{i,\alpha}\partial q_{j,\beta}}= \sum\limits_{i,j=1}^{2} &\Biggr( \frac{\partial^{2}U}{\partial q_{i,1}\partial q_{j,1}}+\frac{\partial^{2}U}{\partial q_{i,1}\partial q_{j,2}}+\frac{\partial^{2}U}{\partial q_{i,1}\partial q_{j,3}} +\\ 
&+ \frac{\partial^{2}U}{\partial q_{i,2}\partial q_{j,1}}+\frac{\partial^{2}U}{\partial q_{i,2}\partial q_{j,2}}+\frac{\partial^{2}U}{\partial q_{i,2}\partial q_{j,3}} +\\
&+ \frac{\partial^{2}U}{\partial q_{i,3}\partial q_{j,1}} +\frac{\partial^{2}U}{\partial q_{i,3}\partial q_{j,2}}+\frac{\partial^{2}U}{\partial q_{i,3}\partial q_{j,3}}\Biggr)
\end{align*}$$
em que aqui já temos a matriz para $n=1$, em que o 1º termo tem $(\alpha=1,\beta=1)$; o 2º tem $(\alpha=1,\beta=2)$; etc.
>
> Para $n=2$ o termo de $(\alpha=1,\beta=1)$ fica:
$$\begin{align*}
\sum\limits_{i,j}^{2}= &\Biggr( \frac{\partial^{3}U}{\partial q_{1,1}\partial q_{1,1}} + \frac{\partial^{3}U}{\partial q_{1,1}\partial q_{2,1}}+\\
&+ \frac{\partial^{3}U}{\partial q_{2,1}\partial q_{1,1}}+\frac{\partial^{3}U}{\partial q_{2,1}\partial q_{2,1}} \Biggr)
\end{align*}$$
>Temos então uma matriz do tipo
$$U =\begin{matrix} \begin{matrix}\beta=1  & & & & &     \beta=2  & & &  \beta=3  \\ \downarrow  & & & & &     \downarrow & & &  \downarrow\end{matrix} \\ \begin{pmatrix} \begin{matrix}~\frac{\partial^{2}U}{\partial q_{1,1}\partial q_{1,1}}  & \frac{\partial^{2}U}{\partial q_{1,1}\partial q_{2,1}} \\ 
~\frac{\partial^{2}U}{\partial q_{2,1}\partial q_{1,1}} & \frac{\partial^{2}U}{\partial q_{2,1}\partial q_{2,1}} \end{matrix}  & \Biggr|  & 2\times2  & \Biggr| & 2\times2 &  \\ ------- & + & --- & + & --- \\ 2\times2 & \biggr| & 2\times2 & \biggr| & 2\times2 \\ ------- & + & --- & + & --- \\ 2\times2 & \biggr| & 2\times2 & \biggr| & 2\times2\end{pmatrix}\end{matrix}~ \begin{matrix} \\  \\  \\ \leftarrow\alpha=1 \\  \\  \\   \leftarrow\alpha=2 \\  \\   \leftarrow\alpha=3   \end{matrix}$$

**Modos Normais**
- São obtidos ao diagonalizar a matriz $U$.
- Se podemos diagonalizar a matriz então quer dizer que, sendo $D$ uma matriz diagonal e $V$ uma mudança de base podemos obter $U=V_{i\alpha}D_{\alpha\beta}V_{\beta j}^{T}$ e temos:
$$\begin{align*}
U&\approx U^{*} + \frac{1}{2}\sum\limits_{i,j,\alpha,\beta}(q_{i}-q_{i}^{*})V_{i\alpha}D_{\alpha\beta}V_{\beta j}^{T} (q_{j}-q_{j}^{*})\\
&= U^{*} + \frac{1}{2}\sum\limits_{\alpha,\beta} \tilde u_{\alpha}k_{\alpha}\delta_{\alpha\beta}\tilde u_{\beta}\\
&= U^{*}+ \frac{1}{2}\sum\limits_{\alpha}\tilde u_{\alpha}^{2}k_{\alpha}
\end{align*}$$
basicamente o que fazemos é transformar a matriz diagonal $D$ num delta de kronecker e passar os vetores para a base própria do sistema.
- Vemos então que, na base própria do sistema, o potenial é quadrático. Por outras palavras, ficamos com um potencial que depende da energia de equilíbrio e das energia potenciais de cada harmónico $\alpha$.

**Hamiltoniano v2**
- Podemos então reescrever o Hamiltoniano de 1 MOLÉCULA na forma
$$H_{1}\approx \frac{1}{2}\sum\limits_{i=1}^{n}\frac{p_{i}^{2}}{2m}+U^{*}+ \frac{1}{2}\sum\limits_{\alpha}k_{\alpha}\tilde u_{\alpha}^{2}$$
em que ele depende das energias cinéticas das $n$ partículas da molécula, da energia de equilíbrio e das oscilações nos modos normais de cada partícula.
- Temos o valor médio:
$$\langle H_{1}\rangle= U^{*} + \frac{1}{2}k_{B}T (3n+3n-\xi)$$
em que temos:
- $3n$ graus liberdade dos momentos
- $3n$ graus de liberdade dos potenciais/posições
- $\xi$ graus de liberdade que não correspondem a variações de energia (translações, rotações,...). Estes termos não entram no hamiltoniano.

**Calor Específico Clássico**
$$C_{V}=\frac{\partial\langle H\rangle}{\partial T}=\frac{1}{2}k_{B} (3n+3n-\xi)$$
(é constante)

- Ora, experimentalmente observa-se uma variação da capacidade térmica do sistema. Ou seja, o modelo clássico nem sempre descreve a realidade. 
- A realidade é explicada pela quantização dos níveis de energia.

## 1.2 - Oscilador Harmónico
### 1.2.1 - Perspetiva Clássica
- Para um oscilador harmónico 1D temos:
$$H(x,p)= \frac{p^{2}}{2m} + \frac{1}{2}m\omega^{2}x^{2}$$
e o valor médio será (conjunto canónico) $$\langle H\rangle= k_{B}T$$
 e teremos a capacidade térmica $C_{V}=k_{B}$
### 1.2.2 - Perspetiva Quântica
- Temos
$$H_{n}=\hbar \omega \left(n + \frac{1}{2}\right)$$
e estudemos este Hamiltoniano com as técnicas que já vimos

**Função Partição**
$$\begin{align*}
Z&= \sum\limits_{n=1}^{+\infty} e^{-\beta H_{n}}\\
&= \sum\limits_{n=1}^{+\infty} e^{-\beta \hbar\omega(n+1/2)}\\
&= e^{\frac{-\beta\hbar\omega}{2}}\sum\limits_{n=1}^{+\infty}(e^{-\beta\hbar\omega})^{n}\\
&= \frac{e^{-\frac{\beta\hbar\omega}{2}}}{1-e^{-\beta\omega\hbar}}\\
&= \frac{1}{e^{\frac{\beta\hbar\omega}{2}}-e^{-\frac{\beta\hbar\omega}{2}}}\\
&= \frac{1}{2\sinh\left(\frac{2\beta\hbar\omega}{2}\right)}
\end{align*}$$
em que para eliminar o sumatório usamos a soma de uma série geométrica: $\sum_{n=1}^{+\infty}(e^{-\beta\hbar\omega})^{n}=\sum\limits^{+\infty}_{n=1}r^{n}=S_{+\infty}=\frac{r^{+\infty}-1}{r-1}=\frac{1}{1-e^{-\beta\hbar\omega}}$ 

**Energia Média**
$$\begin{align*}
\langle H\rangle &=  - \frac{\partial}{\partial\beta}\ln Z\\
&= \frac{\partial}{\partial\beta} \ln\left(e^{\frac{\beta\hbar\omega}{2}} - e^{\frac{-\beta\hbar\omega}{2}}\right)\\
&= \frac{\partial}{\partial\beta} \ln \left[e^{\frac{-\beta\hbar\omega}{2}}\left(e^{\beta\hbar\omega} - 1\right)\right]\\
&= \frac{\partial}{\partial \beta} \left(- \frac{\beta\hbar\omega}{2} + \ln (e^{\beta\hbar\omega}-1) \right)\\
&= - \frac{\hbar\omega}{2} + \frac{\hbar\omega}{e^{\beta\hbar\omega}-1}
\end{align*}$$

**Capacidade Térmica**
$$\begin{align*}
C_{V}&= \frac{\partial\langle H\rangle}{\partial T}= \frac{d\beta}{dT}\frac{\partial\langle H\rangle}{d\beta}\\
&= - \frac{1}{k_{B}T^{2}} \frac{\partial}{\partial\beta}\left(- \frac{\hbar\omega}{2} + \frac{\hbar\omega}{e^{\beta\hbar\omega}-1}\right)\\
&= - k_{B}\beta^{2} \cdot \hbar\omega (-\hbar\omega e^{\beta\hbar\omega}) \frac{1}{(e^{\beta\hbar\omega}-1)^{2}}\\
&= k_{B}\frac{(\beta\hbar\omega)^{2}e^{\beta\hbar\omega}}{(e^{\beta\hbar\omega}-1)^{2}} 
\end{align*}$$em que quando $T\to0^{+}$ temos $C_{V}\to0$ e quando $T\to\infty$ temos $C_{V}\to k_{B}$.

## 1.3 - Limite Clássico
- Podemos obter a relação entre as probabilidades de ter um oscilador harmónico quântico com energia $E_{n}$ e $E_{n-1}$:
$$\frac{P(E_{n})}{P(E_{n-1})} = \frac{e^{-\beta H_{n}}}{e^{-\beta H_{n-1}}}=e^{-\beta (H_{n}-H_{n-1})}= e^{-\beta\hbar\omega(n+ \frac{1}{2}-n+1- \frac{1}{2})}=e^{-\hbar\omega\beta}=e^{-\frac{\hbar\omega}{k_{B}T}} $$

- No caso clássico temos que o espetro seria contínuo. Ou seja, $P(E_{n})=P(E_{n-1})$. Em termos da razão acima, o limite clássico significa que $\frac{\hbar\omega}{k_{B}T}\to0$ AKA $T\to+\infty$

## 1.4 - Poço Infinito
- Vejamos o conhecido caso do poço infinito 3D. A energia é dada por:
$$E_{n_{x},n_{y},n_{z}}=\frac{\hbar^{2}\pi^{2}}{2mL^{2}}(n_{x}^{2}+n_{y}^{2}+n_{z}^{2})$$
para 2 níveis consecutivos em $x$ temos:
$$E_{111}=\frac{3\hbar^{2}\pi^{2}}{2mL^{2}} \quad \quad;\quad \quad E_{211}=\frac{6\hbar^{2}\pi^{2}}{2mL^{2}}$$
pelo que $$\Delta E=\frac{3\hbar^{2}\pi^{2}}{2mL^{2}}$$
- No limite clássico teremos
$$k_{B}T\gg\Delta E \to T\gg \frac{3\hbar^{2}\pi^{2}}{2k_{B}mL^{2}}$$

# 2 - Formulação de Física Estatística Quântica
## 2.1 - Microestados Quânticos
- Determinado por um vetor unitário $|\psi\rangle$ pertencente ao espaço de Hilbert.
- Podemos escrever:
$$|\psi\rangle=\sum\limits_{n} \langle n|\psi\rangle|n\rangle$$
em que temos a condição de normalização
$$\langle \psi|\psi\rangle=1$$
- Temos ainda $\langle \psi|n\rangle=\langle n|\psi\rangle^{*}$

## 2.2 - Observáveis
- Funções deifnidas num espaço de fase AKA funções de microestado.
- Na física quântica são representados por matrizes hermíticas, sendo que $$\mathcal{O}=\mathcal{O}^{\dagger}$$
tendo-se a propriedade $\langle \psi|\mathcal{O}^{\dagger}|\varphi\rangle=\langle \varphi|\mathcal{O}|\psi\rangle^{*}$

**Valor Médio**
$$\langle\mathcal{O}\rangle=\langle \psi|\mathcal{O}|\psi\rangle=\sum\limits_{m,n}\langle \psi|m\rangle\langle m|\mathcal{O}|n\rangle\langle n|\psi\rangle$$
Exemplo:
$$\langle U(\{\vec{q}\})\rangle=\int \prod d^{3}q_{i} \psi^{*}(\vec{q_{1}},\dots,\vec{q_{N}})U(\{\vec{q}\}) \psi(\vec{q_{1}},\dots,\vec{q_{N}})$$

## 2.3 - Evolução Temporal
- No clássico tinhamos que um microestado evoluia conforme as equações de Hamilton. 
- Na quântica temos a equação de Schrödinger:
$$i\hbar \frac{\partial}{\partial t}|\psi\rangle=\mathcal{H}|\psi\rangle$$

## 2.4 - Base própria do Hamiltoniano
- Na base própria do hamiltoniano temos:
$$\mathcal{H}|n\rangle=\mathcal{E_{n}}|n\rangle$$
(sendo $\mathcal{E_{n}},|n\rangle$ valores e vetores próprios)
- Tendo a equação de Schrödinger e a condição de ortonormalização $\langle m|n\rangle=\delta_{mn}$:
$$\begin{align*}
i\hbar \frac{\partial}{\partial t}|\psi\rangle&= \mathcal{H}|\psi\rangle\\
i\hbar \frac{\partial}{\partial t}\langle n|\psi\rangle&= \langle n|\mathcal{H}|\psi\rangle\\
i\hbar \frac{\partial}{\partial t}\langle n|\psi\rangle&= \mathcal{E_{n}}\langle n|\psi\rangle\\
\end{align*}$$
de onde surge:
$$\langle n|\psi(t)\rangle= \exp\left(-\frac{i\mathcal{E_{n}}t}{\hbar}\right)\langle n|\psi(0)\rangle$$
(sendo $\langle n|\psi\rangle$ a representação do microestado $|\psi\rangle$ na base $|n\rangle$)

## 2.5 - Operador de Evolução Temporal
- Conforme o que obtivemos acima podemos definir:
$$|\psi(t)\rangle=U(t,t_{0})|\psi(t_{0})\rangle$$
que na base própria do hamiltoniano é dado pela equação acima.

- Se Tivermos um Hamiltoniano independente do tempo teremos:
$$\begin{align*}
i\hbar \frac\partial{\partial t} U(t,t_{0}) \ket{\psi(t_{0})} &=  \mathcal HU(t,t_{0}) \ket{\psi(t_{0})} \\
&\downarrow\\
 U(t,t_{0}) &=  \exp\left[-\frac {i\mathcal H}\hbar (t-t_{0})\right]
\end{align*}$$


# 3 - Macroestados Quânticos
## 3.1 - Macroestado Clássico
- Como já vimos, podemos representar macroestados através de uma densidade de probabilidade de microestados compatíveis:
$$\rho(\vec{p},\vec{q},t)=\sum\limits_{\alpha}P_{\alpha}\prod_{i=1}^{N}\delta(q_{i}-q_{i\alpha}(t))\delta(p_{i}-p_{i\alpha}(t))$$
em que $P_{\alpha}$ é a porção de microestados compatíveis.
- Isto dá-nos:
$$\langle\overline{\mathcal{O}}\rangle=\int d\Gamma \rho(\vec{p},\vec{q},t)\mathcal{O}(\vec{p},\vec{q})$$

## 3.2 - Macroestado Quântico
- Temos:
$$\rho(t)=\sum\limits_{\alpha}P_{\alpha}\ket{\psi_{\alpha}(t)}\bra{\psi_{\alpha}(t)} $$
e podemos definir:
$$\begin{align*}
\langle\overline{\mathcal{O}}\rangle &= \sum\limits_{\alpha}P_{\alpha} \langle \psi_{\alpha}|\mathcal{O}|\psi_{\alpha}\rangle\\
&= \sum\limits_{\alpha,m,n} P_{\alpha}\langle\psi|m\rangle\langle m|\mathcal{O}|n\rangle\langle n|\psi\rangle\\
&= \sum\limits_{\alpha,m,n} P_{\alpha}\langle\psi|m\rangle\langle n|\psi\rangle \langle m|\mathcal{O}|n\rangle\\
&= \sum\limits_{m,n} \langle n|\rho|m\rangle \langle m|\mathcal{O}|n\rangle \\
&= \text{tr}(\rho\mathcal{O})
\end{align*}$$
em que no final temos o **traço** que consiste na soma dos elementos da diagonal da matriz de $\rho\mathcal{O}$.

## 3.3 - Propriedades da matriz das densidades
1. O traço é 1:
$$\begin{align*}
\text{tr}(\rho)&= \sum\limits_{n,\alpha} P_{\alpha}\langle n|\psi_{\alpha}\rangle\langle\psi_{\alpha}|n\rangle\\
&= \sum\limits_{n,\alpha}P_{\alpha} |\langle n|\psi\rangle|^{2}\\
&= \sum\limits_{\alpha}P_{\alpha}=1
\end{align*}$$
2. $\rho$ é um operador hermítico
$$\begin{align*}
\langle m|\rho^{\dagger}|n\rangle&= \langle n|\rho|m\rangle\\
&= \sum\limits_{\alpha}P_{\alpha}\langle\psi_{\alpha}|m\rangle\langle n|\psi_{\alpha}\rangle\\
&= \langle n|\rho|m\rangle
\end{align*}$$

3. É positiva
$$\begin{align*}
\langle \phi|\rho|\psi\rangle&= \sum\limits_{\alpha}P_{\alpha}\langle \phi|\psi_{\alpha}\rangle\langle\psi_{\alpha}|\phi\rangle\\
&= \sum\limits P_{\alpha}|\langle \phi|\psi_{\alpha}\rangle|^{2}\ge 0
\end{align*}$$

# 4 - Evolução temporal
- A evolução temporal é particularmente importante para saber se existe um estado de equilíbrio.

## 4.1 - Clássica
- Dada pelo teorema de Liouville:
$$\frac{d\rho}{dt}=\frac{\partial\rho}{\partial t}-\{H,\rho\}=0$$

## 4.2 - Quântica
- Dada pela equação de Schrödinger:
$$i\hbar \frac{\partial\rho}{\partial t}=[\mathcal{H},\rho]$$
tal como no caso clássico, qualquer quantidade que satisfaça $[\mathcal{H},L_{\alpha}]=0$ é conservada.

# 5 - Ensembles em FESTA Quântica
## 5.1 - Microcanónico
- Temos um sistema isolado, com energia fixa $E$.

**Matriz das densidades**
$$\rho(E)=\frac{\delta(\mathcal{H}-E)}{\Omega(E)}$$

**Base própria do Hamiltoniano**
$$\begin{align*}
\langle n|\rho|m\rangle&= \sum\limits_{\alpha}P_{\alpha}\langle n|\psi_{\alpha}\rangle\langle \psi_{\alpha}|m\rangle\\
&= \begin{cases}
\frac{1}{\Omega} & ; & \mathcal{E_{n}}=E\wedge m=n\\
0 & ; & \mathcal{E_{n}}\neq E\vee m\neq n
\end{cases}
\end{align*}$$
- A 1ª opção significa que apenas os autovalores com energia "correta" aparecem na função de onda. Ou seja, se $P_{\alpha}=\frac{1}{N}$ então ficamos com autovetores todos com o mesmo módulo, sendo o valor médio $\overline{|\langle n|\psi\rangle|}^{2}=\frac{1}{\Omega}$. No clássico isto é equivalente a ter estados equiprováveis.

- A condição de normalização da densidade $\text{tr}\rho=1$ implica que $\Omega(E)=\sum_{n}\delta(E-E_{n})$ é o número de estados próprios de $\mathcal{H}$ com energia $E$.

## 5.2 - Canónico
- Temos um sistema em contacto térmico com um reservatório a temperatura fixa $T$.

**Matriz de Densidades**
$$\rho(\beta)=\frac{\exp(-\beta\mathcal{H})}{Z(\beta)}$$
tal como no clássico.

**Função de Partição Quântica**
- Obtido com a condição de normalização:
$$Z(\beta)=\text{tr}(e^{-\beta\mathcal{H}})=\sum_{n}e^{-\beta\mathcal{E_{n}}}$$
ou seja, simplesmente percorremos os níveis de energia (discretos) de $\mathcal{H}$.

## 5.3 - Macrocanónico
- Sistema com trocas de calor e número de partículas variável.

**Matriz de Densidades**
$$\rho(\beta,\mu)=\frac{\exp(-\beta\mathcal{H}+\beta\mu N)}{\mathcal{Z}_{G}}$$
igual ao clássico.

**Função de Partição Grande Quântica**
- Novamente, obtida com a condição de normalização:
$$\mathcal{Z}_{G}(\beta,\mu)=\text{tr}(e^{-\beta\mathcal{H}+\beta\mu N})=\sum\limits_{N=0}^{\infty}e^{\beta\mu N}Z_{N}(\beta)$$

# 6 - Gás Ideal Quântico
## 6.1 - Sistemas de Partículas Idênticas
- Consideremos um gás de partículas idênticas, livres e sem estrutura interna.
- Um microestado do gás pode ser descrito pela função de onda $\psi_{n_{1},\dots,n_{N}}(\vec{q_{1}},\dots,\vec{q_N})$ - pra cada partícula, $\vec{q_{i}}$ inclui as 4 coordenadas de posição e 1 de spin, $n_{i}$ representa os números quânticos da partícula.

**Funções Simétricas e Anti-simétricas**
Simétrica: fica igual ao trocar as coordenadas de um par de partículas:
$$\psi_{S}(\dots\vec{q_{i}}\dots\vec{q_{j}}\dots)=\psi_{S}(\dots\vec{q_{j}}\dots\vec{q_{i}}\dots)$$
Anti-simétrica: muda de sinal ao trocar as coordendas de um par de partículas:
$$\psi_{S}(\dots\vec{q_{i}}\dots\vec{q_{j}}\dots)=-\psi_{S}(\dots\vec{q_{j}}\dots\vec{q_{i}}\dots)$$

## 6.2 - Postulado de Simetrização
Este postulado serve para resolver ambiguidades de sistemas de partículas idênticas:

> Quando um sistema inclui várias partículas idênticas, somente certos kets do seu espaço de estados podem descrever estados físicos.
> 
> Os kets físicos são, dependendo da natureza das partículas idênticas, ou completamente simétricos ou completamente anti-simétricos, com respeito à permutação destas partículas.
> 
> As partículas para as quais os kets físicos são simétricos/anti-simétricos chamam-se bosões/fermiões.

**Bosões** - partículas idênticas de spin inteiro associadas à representação simétrica (fotões, átomos He-4)
**Fermiões** - partículas idênticas com spin semi-inteiro associadas a representação anti-simétrica (eletrões, protões, átomos He-3)

## 6.3 - Princípio de Exclusão de Pauli
- Quando temos 2 partículas $i,j$ no mesmo estado temos:
$$\psi_{A}(\dots\vec{q_{i}}\dots\vec{q_{j}}\dots)=\psi_{A}(\dots\vec{q_{j}}\dots\vec{q_{i}}\dots)$$
- Mas se a partícula tiver representação anti-simétrica então isto implica $\psi_{A}=0$
- Assim, **não** pode existir um microestado de um gás com partículas idênticas de spin semi-inteiro em que 2+ partículas estão no mesmo estado - *princípio de exclusão de Pauli*
    - Se tivermos partículas diferentes (protão e eletrão, por exemplo) isto já não se aplica

## 6.4 - Gás numa caixa
- Temos uma partícula de massa $m$ num poço de potencial infinito de comprimento $L$.

### 6.4.1 - 1D
- A ESIT dá-nos:
$$\psi_{n}(x)=\frac{e^{-ik_{n}x}}{\sqrt{L}} \quad \quad;\quad k_{n}=\frac{2\pi n}{L}$$
e temos a energia de cada nível $n$ dada por $\varepsilon_{n}=\dfrac{\hbar k_{n}^{2}}{2m}$

### 6.4.2 - 3D
$$\psi_{n}(\vec{r})=\frac{e^{i\vec{k_{n}}\cdot\vec{r}}}{\sqrt{V}} \quad \quad;\quad \vec{k_{n}}=2\pi\left(\frac{n_{x}}{L_{x}}\hat{x}+\frac{n_{y}}{L_{y}}\hat{y}+\frac{n_{z}}{L_{z}}\hat{z}\right)$$
e as energias são dadas por $\varepsilon_{\vec{k}}=\dfrac{\hbar^{2} \vec{k}\cdot\vec{k}}{2m}$

- Ao ter uma soma $\sum_{\vec{k}} f(\vec{k})$, se $L$ for muito grande, ela transforma-se num integral: $$\sum\limits_\vec{k}f(\vec{k})=\frac{V}{(2\pi)^{3}}\int d^{3}k~f(\vec{k})$$
- E podemos introduzir a constante de Planck para adimensionalizar como faziamos atrás:
$$\frac{V}{(2\pi)^{3}}\int d^{3}k~f(\vec{k})= \frac{V}{h^{3}}\int d^{3}p~f(\vec{k})$$

## 6.5 - Energia Potencial
- Até aqui apenas consideramos a energia cinética das partículas.
- Podemos ter os seguintes casos de energia potencial:
**Vibrações Harmónicas**
$$H_{vib}=\hbar\omega\left(n+ \frac{1}{2}\right)$$

**Rotações - momento angular**
$$H_{rot}=\hbar^{2}\frac{J(J+1)}{2I}$$
**Campo Magnético**
$$H_{el}=-\mu_{B}H\sigma$$
($\sigma=\pm1$ é o spin) 

## 6.6 - Abordagem Estatística
- Do que vimos acima, podemos definir as seguinte propriedades de bosões e fermiões:
*Bosões* - partículas idêntica que **podem** ocupar o mesmo estado
*Fermiões* - partículas idêntica que **não podem** ocupar o mesmo estado

### 6.6.1 - Estados do sistema
- Começamos por identificar uma base $\ket{j}$ do Hamiltoniano, sendo que a cada estado próprio corresponde a energia $\varepsilon_{j}$
- Podemos definir:
$$\{n_{1},n_{2},\dots,n_{j},\dots\}\equiv\{n_{j}\}$$
em que $j$ é um certo estado quântico e $n_{j}$ o número de partículas nesse estado. (**número de ocupação**)
- Podemos portanto definir:
$$N=\sum\limits_{j}n_{j} \quad \quad;\quad \quad E=\sum\limits_{j}\varepsilon_{j}n_{j}$$
- Facilmente vemos que para bosões temos $n_{j}\in\mathbb{N_{0}}$ e para fermiões $n_{j}\in\{0,1\}$.

**Ensemble Canónico**
- A função partição é:
$$Z(T,V,N)=\sum\limits_{\{n_{j}\}}e^{-\beta E(\{n_{j}\})}=\sum\limits_{\{n_{j}\}}\exp\left(-\beta\sum_{j}n_{j}\varepsilon_{j}\right)~\delta_{N,\sum_{j}n_{j}}$$
(não percebo a utilidade do Delta. Não teremos sempre $N=\sum_{j}n_{j}$??)
- Esta função é dificil de calcular porque implica saber todas as combinações de estados possíveis.

**Ensemble Macrocanónico**
$$\begin{align*}
\mathcal{Z}_{G}(T,V,\mu)&= \sum\limits_{N=0}^{+\infty} e^{\beta\mu N}Z(T,V,N)\\
&= \sum\limits_{N=0}^{+\infty}e^{\beta\mu N} \sum\limits_{\{n_{j}\}}\exp\left(-\beta\sum_{j}n_{j}\varepsilon_{j}\right)~\delta_{N,\sum_{j}n_{j}}\\
&= \sum\limits_{N=0}^{+\infty}\sum\limits_{\{n_{j}\}}\exp\left(-\beta\sum_{j}n_{j}(\varepsilon_{j}-\mu)\right)~\delta_{N,\sum_{j}n_{j}}\\
&= \sum\limits_{\{n_{j}\}}\exp\left(-\beta\sum_{j}n_{j}(\varepsilon_{j}-\mu)\right)\\
&= \prod_{j}\left(\sum\limits_{n_{j}}e^{-\beta n_{j}(\varepsilon_{j}-\mu)}\right)
\end{align*}$$
este em geral é mais fácil de calcular - normalmente iremos usar macrocanónico em quântica! De recordar que, no limite termodinâmico as flutuações de $\mu$ serão desprezáveis, pelo que $\langle N\rangle=N$

- Tal como no clássico podemos calcular:
$$\begin{align*}
\langle n_j \rangle &= -\frac1\beta\frac{\partial}{\partial \varepsilon_j}\ln\mathcal Z_G\\
\mathcal G_G &= -\frac1\beta \ln \mathcal Z_G
\end{align*}$$

## 6.7 - Estatística de Bose-Einstein (BE)
- No caso de bosões, $n_{j}$ pode ir até infinito.
- Neste caso, a série $\sum_{n_{j}}e^{-\beta n_{j}(\varepsilon_{j}-\mu)}=\sum_{n_{j}}(e^{\beta(\mu-\varepsilon_{j})})^{n_{j}}$ **converge** se $$e^{\beta(\mu-\varepsilon_{j})}<1\to \mu<\min(\varepsilon_{j}) ~~,~\forall j$$
- Neste caso, a série torna-se numa *série geométrica*, sendo a sua soma:
$$\sum\limits_{n=0}^{+\infty} e^{-\beta n(\varepsilon_{j}-\mu)}=\frac{1}{1-e^{-\beta(\varepsilon_{j}-\mu)}}$$
- Se definirmos o mínimo de energia como zero, fica $\mu<0$. Mais especificamente, no caso em que $\mu\to0^{-}$ temos **condensação de Bose-Einstein**. 
    - Neste caso temos: $$\ln \mathcal{Z}_{G}(T,V,\mu)=\ln\left(\prod_{j}\frac{1}{1-e^{-\beta(\varepsilon_{j}-\mu)}}\right)=-\sum_{j}\ln(1-e^{-\beta(\varepsilon_{j}-\mu)})$$
    - Conforme $\langle n_j \rangle = -\frac1\beta\frac{\partial}{\partial \varepsilon_j}\ln\mathcal Z_G$ obtemos: $$\langle n_{j}\rangle=\frac{1}{e^{\beta(\varepsilon_{j} -\mu)}-1}$$

## 6.8 - Estatística de Fermi-Dirac (FD)
- No caso de fermiões $n_{j}$ apenas tem 2 valores possíveis: 1 ou 0.
- Assim:
$$\sum\limits_{n_{j}=0}^{1}e^{-\beta n_{j}(\varepsilon_{j}-\mu)}=1+e^{-\beta(\varepsilon_{j}-\mu)}$$

- Daqui resulta:
$$\ln \mathcal{Z}_{G}(T,V,\mu)=\sum\limits_{j}\ln(1+e^{-\beta(\varepsilon_{j}-\mu)})$$
e podemos obter:
$$\langle n_{j}\rangle=\frac{1}{e^{\beta(\varepsilon_{j}-\mu)}+1} \quad \quad;\quad 0\le \langle n_{j}\rangle\le1$$

## 6.9 - Número Médio de Partículas
- Se somarmos o número de ocupação médio para cada estado $j$ obtemos
$$\langle N\rangle=\sum\limits_{j}\langle n_{j}\rangle=\begin{cases}
\sum_{j}\frac{1}{e^{\beta(\varepsilon_{j}-\mu)}-1} &  & ; & Bose-Einstein \\
\sum_{j}\frac{1}{e^{\beta(\varepsilon_{j}-\mu)}+1} &  & ; & Fermi-Dirac
\end{cases}$$

## 6.10 - Energia Média do Gás
- De forma análogo ao que temos na secção acima:
$$\langle E\rangle=\sum\limits_{j}\varepsilon_{j}\langle n_{j}\rangle=\begin{cases}
\sum_{j}\frac{\varepsilon_{j}}{e^{\beta(\varepsilon_{j}-\mu)}-1} &  & ; & Bose-Einstein \\
\sum_{j}\frac{\varepsilon_{j}}{e^{\beta(\varepsilon_{j}-\mu)}+1} &  & ; & Fermi-Dirac
\end{cases}$$

## 6.11 - Energia independente do Spin
- Os sumatórios em $j$ feitos acima incluem termos de translação e spin, que também têm energia. Assim, devemos introduzir o termo de *spin*:
$$\sum\limits_{j}\dots=\sum\limits_{\sigma=-S}^{S}\sum\limits_{k}\dots$$
em que $S$ é o Spin. Se a energia não depender do spin, este sumatório apenas introduz um termo $2S+1$.

## 6.12 - Potencial Químico Nulo
- Vejamos agora gases em que $\mu=0$
- Isto implica que:
$$\mu = \left(\frac{\partial \mathcal F}{\partial N}\right)_{T,V} = \left(\frac{\partial G}{\partial N}\right)_{T,P} = 0$$
- Temos ainda, na função de partição grande:
$$\mathcal{Z}_{G}(T,V,\mu=0)=\sum\limits_{j}e^{-\beta\varepsilon_{j}}=Z(T,V)$$
### 6.12.1 - Estatística de Planck
- Consiste na estatística de Bose-Einstein com $\mu=0$, em que:
$$\langle n_{j}\rangle=\frac{1}{e^{\beta\varepsilon_{j}}-1}$$

## 6.13 - Limite Clássico
- Deverá haver um limite clássico em que as previsões feitas acima para fermiões e bosões convergem. Isso será quando:
$$e^{\beta(\varepsilon_{j}-\mu)}\gg1$$

### 6.13.1 - Número médio de partículas
- Como vimos acima:
$$\langle n_{j}\rangle=\begin{cases}
\frac{1}{e^{\beta(\varepsilon_{j}-\mu)}-1} &  & ; & Bose-Einstein \\\\
\frac{1}{e^{\beta(\varepsilon_{j}-\mu)}+1} &  & ; & Fermi-Dirac
\end{cases}$$
ora, no limite termodinâmico ficamos com um denominador muito reduzido.
- Podemos fazer expansão em série de Taylor:
$$\frac{1}{1+x}=1-x+x^{2}-x^{3}+\dots$$
e fica:
$$\langle n_{j}\rangle\approx e^{-\beta(\varepsilon_{j}-\mu)}$$
(pelo que ambas as estatísticas BE/FD se comportam da mesma forma neste limite)

### 6.13.2 - Função de Grande Partição
$$\ln \mathcal{Z}_{G}=\pm \sum\limits_{j}\ln(1\pm e^{-\beta(\varepsilon_{j}-\mu)})\approx \sum\limits_{i}e^{-\beta(\varepsilon_{j}-\mu)}=\sum\limits_{j}\langle n_{j}\rangle$$
em que se fez expansão em taylor do logaritmo $\ln(1\pm x)$

### 6.13.3 - Gás ideal no limite clássico
- Retomemos o espetro obtido para um gás numa caixa de potencial infinito:
$$\varepsilon_{j}=\varepsilon_{\vec{k},\sigma}=\frac{\hbar^{2}k^{2}}{2m}$$
- Temos
$$\ln\mathcal{Z}_{G}=\sum\limits_{\vec{k},\sigma}\exp\left[-\beta\left(\frac{\hbar^{2}k^{2}}{2m}-\mu\right)\right]$$
- No limite termodinâmico temos $L\to\infty$, pelo que o sumatório em $k$ pode ser substituido por um integral e temos:
$$\begin{align*} \ln \mathcal Z_G &= (2S+1)\frac{V}{(2\pi)^3}\int d^3k\, \exp\left[-\beta\left(\frac{\hbar^2k^2}{2m}- \mu\right)\right] \\ &= (2S+1)\frac{V}{(2\pi)^3}e^{\beta\mu}\left(\frac{2\pi m}{\beta\hbar^2}\right)^{3/2} \\ &= g_se^{\beta\mu}\frac V{\lambda_T^3} \end{align*}$$
em que definimos $g_{s}\equiv2S+1$ como sendo a degenerescência de spin. $\lambda_{T}$ é o comprimento de onda térmico

**Potencial Grande Canónico**
$$\mathcal{G}(\beta,\mu,X)=-\frac{1}{\beta}\ln\mathcal{Z}_{G}=-k_{B}T g_{s}\frac{V}{\lambda_{T}^{3}}e^{\beta\mu} $$

**Número média partículas**
$$\langle N\rangle=- \left(\frac{\partial\mathcal{G}}{\partial\mu}\right)_{T,V}=g_{s}\frac{V}{\lambda_{T}^{3}}e^{\beta\mu} =\ln\mathcal{Z}_{G}$$
ou seja:
$$e^{\beta\mu} = \frac{\langle N\rangle}{g_{s}V}\lambda_{T}^{3}$$

**Limite Clássico**
- O limite clássico corresponde a $$e^{\beta\mu}\ll 1 \to \frac{\langle N\rangle}{g_{s}V}\lambda_{T}^{3}\ll 1$$
- Se definirmos $a=(\frac{V}{N})^{\frac{1}{3}}$ - distância intermolecular típica obtemos:
$$g_{s}\left(\frac{a}{\lambda_{T}}\right)^{3}\gg 1$$
ou seja, atingimos limite clássico para temperaturas muito elevadas e/ou concentrações muito baixas.

## 6.14 - Gás de Bose
- Na secção atrás vimos um gás ideal genérico numa caixa de potencial infinito. Nesta e na próxima secção veremos os 2 tipos de gás ideal.
- Podemos determinar a densidade de estados do gás de Bose: $$\rho(E)=\sum\limits_{k=1}^{+\infty}\delta(\varepsilon-\varepsilon_{k})$$
- Tomando um gás ideal não relativista temos $$\varepsilon_{k}=\frac{\hbar^{2}k^{2}}{2m}$$
- No limite termodinânico $V\to\infty$ podemos substituir o sumatório em cima pelo integral. Fica:
$$\begin{align*}
\rho(E)&= \frac{V}{(2\pi)^{3}}\int d^{3}k ~\delta\left(\varepsilon-\frac{\hbar^{2}k^{2}}{2m}\right)\\
&= \frac{V}{(2\pi)^{3}}\int_{0}^{\pi}\int_{0}^{2\pi}\int_{0}^{+\infty}k^{2}\sin \theta ~dkd\theta d\phi ~\delta\left(\varepsilon-\frac{\hbar^{2}k^{2}}{2m}\right)\\
&= \frac{V}{(2\pi)^{3}}4\pi \int_{0}^{+\infty}k^{2} \delta\left(\varepsilon-\frac{\hbar^{2}k^{2}}{2m}\right)dk\\
&= \frac{V}{2\pi^{2}} \int_{0}^{+\infty}k^{2} \delta\left(\varepsilon-\frac{\hbar^{2}k^{2}}{2m}\right)dk
\end{align*}$$
e podemos fazer a mudança de variável $y=\frac{\hbar^{2}k^{2}}{2m}\to k=\sqrt{\frac{2my}{\hbar^{2}}}\to dk=\sqrt{\frac{2m}{\hbar^{2}y}}dy$:
$$\begin{align*}
\rho(E)&= \frac{V}{2\pi^{2}}\int_{0}^{+\infty} \frac{2my}{\hbar^{2}} \delta(\varepsilon-y) \sqrt{\frac{2m}{\hbar^{2}y}}dy\\
&= \frac{V}{2\pi^{2}\hbar^{3}}(2m)^{\frac{3}{2}}\int_{0}^{+\infty}\delta(\varepsilon-y)\sqrt{y}~dy\\
&= \frac{V}{2\pi^{2}\hbar^{3}}(2m)^{\frac{3}{2}} \sqrt{\varepsilon}\\
&= \frac{V}{\lambda_{T}^{3}} \frac{2}{\sqrt{\pi}}\beta^{\frac{3}{2}}\sqrt{\varepsilon}
\end{align*}$$

- Ora, esta aproximação só não é boa quando $\varepsilon_{k}\to0$.
- Como vimos acima, a função de grande partição de um gás de bosões temos:
$$\begin{align*}
\ln \mathcal{Z}_{G}(T,V,\mu)&= -\sum_{k}\ln(1-e^{-\beta(\varepsilon_{k}-\mu)})\\
&= -\sum\limits_{k}\ln(1-e^{-\beta(\varepsilon_{k}-\mu)}) - \underbrace{\ln(1-e^{\beta\mu})}_{\varepsilon_{k}=0}\\
&= -\int_{0}^{+\infty}\rho(\varepsilon_{k})\ln(1-e^{-\beta(\varepsilon_{k}-\mu)}) d\varepsilon_{k} - \underbrace{\ln(1-e^{\beta\mu})}_{\varepsilon_{k}=0}\\
\end{align*}$$
também vimos que:
$$\begin{align*}
\langle N\rangle&= - \left(\frac{\partial\mathcal{G}}{\partial\mu}\right)_{T,V}\\
&= \frac{1}{\beta} \frac{\partial}{\partial\mu}\ln\mathcal{Z}_{G}\\
&= \frac{1}{\beta}\frac{\partial}{\partial\mu}\left[-\int_{0}^{+\infty} \rho(\varepsilon_{k}) \ln(1-e^{-\beta\varepsilon_{k}}e^{\beta\mu})d\varepsilon_{k} - \ln(1-e^{\beta\mu}) \right]\\
&= \frac{1}{\beta}\left(-\int_{0}^{+\infty}\rho(\varepsilon_{k})\frac{-\beta e^{\beta\mu}e^{-\beta\varepsilon_{k}}}{1-e^{\beta\mu}e^{-\beta\varepsilon_{k}}}d\varepsilon_{k} - \frac{-\beta e^{\beta\mu}}{1-e^{\beta\mu}} \right)\\
&= \int_{0}^{+\infty}\frac{\rho(\varepsilon_{k})}{e^{-\beta\mu} e^{\beta\varepsilon_{k}}-1} d\varepsilon_{k}+\frac{e^{\beta\mu}}{1-e^{\beta\mu}}
\end{align*}$$
e podemos escrever $z=e^{\beta\mu}$:
$$\langle N\rangle=\int_{0}^{\infty}\frac{\rho(\varepsilon_{k})}{e^{\beta\varepsilon_{k}}/z-1}d\varepsilon_{k} + \frac{z}{1-z}$$

- Para resolver este integral temos a função de Jonquière / função de polilogaritmo: $$g_{n}(z)= \frac{1}{\Gamma(n)}\int_{0}^{\infty}\frac{x^{n-1}}{z^{-1}e^{x}-1}dx$$
que tem a expansão em Taylor:
$$g_{n}(z)=\sum\limits_{k=1}^{\infty}\frac{z^{k}}{k^{n}} \quad \quad;\quad0<z<1$$
- Voltemos à função de grande partição:
$$\begin{align*}
\ln\mathcal{Z}_{G}&= -\int_{0}^{+\infty}\rho(\varepsilon_{k})\ln(1-ze^{-\beta\varepsilon_{k}}) d\varepsilon_{k} - \ln(1-z)\\
&= \frac{V}{\lambda_{T}^{3}} \frac{2}{\sqrt{\pi}}\beta^{\frac{3}{2}}\int \sqrt{\varepsilon_{k}} \ln(1-ze^{-\beta\varepsilon_{k}}) d\varepsilon_{k} - \ln(1-z)\\
&= \frac{V}{\lambda_{T}^{3}} \frac{2}{\sqrt{\pi}}\beta^{\frac{3}{2}}\int \sqrt{\varepsilon_{k}} \frac{z^{n}e^{-n\beta\varepsilon_{k}}}{n} d\varepsilon_{k} - \ln(1-z)\\
\end{align*}$$
em que se usou a expansão de Taylor $\ln(1-y)=\sum\limits_{n=1}^{\infty}\frac{y^{n}}{n}$.
- Fazemos agora a substituição $x=\sqrt{\varepsilon_{k}}\to dx=\frac{1}{2\sqrt{\varepsilon_{k}}}d\varepsilon_{k}=\frac{1}{2x}d\varepsilon_{k}$
$$\begin{align*}
\ln\mathcal{Z}_{G}&=\frac{V}{\lambda_{T}^{3}} \frac{2}{\sqrt{\pi}}\beta^{\frac{3}{2}} \cdot 2 \frac{z^{n}}{n}\int_{0}^{\infty}x^{2}e^{-\beta nx^{2}}dx-\ln(1-z)\\
&= \frac{V}{\lambda_{T}^{3}} \frac{2}{\sqrt{\pi}}\beta^{\frac{3}{2}} \cdot \frac{z^{n}}{n\beta} \frac{d}{dn}\int_{-\infty}^{\infty}e^{-\beta nx^{2}}
dx-\ln(1-z)\\
&= \frac{V}{\lambda_{T}^{3}} \frac{2}{\sqrt{\pi}}\beta^{\frac{3}{2}} \cdot \frac{z^{n}}{n\beta} \frac{d}{dn} \sqrt{\frac{\pi}{n\beta}}-\ln(1-z)\\
&= \frac{V}{\lambda_{T}^{3}} \frac{2}{\sqrt{\pi}}\beta^{\frac{3}{2}} \cdot \frac{\sqrt{\pi}}{2\beta^{\frac{3}{2}}}\frac{z^{n}}{n^{\frac{5}{2}}} -\ln(1-z)
\end{align*}$$
usando a série de Taylor da função de Polilogaritmo temos:
$$\ln\mathcal{Z}_{G}=\frac{V}{\lambda_{T}^{3}}g_\frac{5}{2}(z)-\ln(1-z)$$
o que nos permite obter:
$$\langle N\rangle=k_{B}T\frac{\partial}{\partial\mu }\ln\mathcal{Z}_{G}=\frac{V}{\lambda_{T}^{3}}\frac{dg_\frac{5}{2}}{dz}+\frac{z}{1-z} $$
em que $\frac{dg_\frac{5}{2}}{dz}=\frac{d}{dz}\sum_{k}\frac{z^{k}}{k^\frac{5}{2}}=\frac{1}{z}\sum_{k}\frac{z^{k}}{k^{\frac{3}{2}}}=z^{-1}g_{3/2}(z)$ e fica
$$\langle N\rangle=\frac{V}{\lambda_{T}^{3}}g_\frac{3}{2}(z)+ \frac{z}{1-z}=N_\varepsilon -N_{0}$$
- O grande potencial fica
$$\mathcal{G}=-k_{B}T\ln\mathcal{Z}_{G}=-k_{B}T\frac{V}{\lambda_{T}^{3}}g_\frac{5}{2}(z)+k_{B}T\ln(1-z)$$
- Podemos ainda obter a pressão do gás:
$$P=- \frac{\partial\mathcal{G}}{\partial V}=\frac{k_{B}T}{\lambda_{T}^{3}}g_\frac{5}{2}(z)$$
- Temos ainda a energia intera:
$$E=-\frac{\partial}{\partial\beta}\ln\mathcal{Z}_{G}=\frac{3}{2}k_{B}T\frac{V}{\lambda_{T}^{3}}g_\frac{5}{2}(z)$$
em que $\lambda_{T}=\frac{\hbar \beta^{\frac{1}{2}}}{\sqrt{2\pi m}}$ e usamos a propriedade $\frac{\partial}{\partial\beta} \frac{1}{\lambda_{T}^{3}}=-\frac{3}{\lambda_{T}^{3}}\frac{\partial\lambda_T}{\partial\beta}$

## 6.15 - Gás de Fermi
- Num gás de fermi continuamos a ter $\varepsilon_{k}=\frac{\hbar^{2}k^{2}}{2m}$, pelo que a densidade de estados continua a ser $\rho(E)=\frac{V}{\lambda_{T}^{3}} \frac{2}{\sqrt{\pi}}\beta^{\frac{3}{2}}\sqrt{\varepsilon}$.
- Para um gás de fermi temos o fator multiplicativo $g_{s}=2s+1$ devido à degenerescência de spin (tendo o número de spin $s$, teremos o número quantico $m_{s}=-s,\dots,s$ que significa uma degenerescência de $2s+1$ estados com spin $s$). No caso de um eletrão temos $s=\frac{1}{2},g_{s}=2$.
- Acima vimos que para um gás de fermi temos
$$\ln \mathcal{Z}_{G}(T,V,\mu)=g_{s}\sum\limits_{j}\ln(1+e^{-\beta(\varepsilon_{j}-\mu)})=g_{s}\sum\limits_{j}\ln(1+ze^{-\beta\varepsilon_{k}})$$
- Desta forma, o número médio de partículas é
$$\langle N\rangle=g_{s}\sum\limits_{k=1}^{+\infty}\frac{1}{z^{-1}e^{-\beta\varepsilon_{k}}+1}$$
- Tal como para o gás de Bose, podemos definir uma função
$$f_{n}(z)=\frac{1}{\Gamma(n)}\int_{0}^{\infty}\frac{x^{n-1}}{z^{-1}e^{x}-1}=\sum\limits_{k=1}^{\infty}(-1)^{k-1} \frac{z^{k}}{k^{n}}$$
e repetindo a mesma análise que para o gás de Bose obtemos:
$$\begin{align*}
\ln\mathcal{Z}_{G}&= g_{s}\frac{V}{\lambda_{T}^{3}}f_\frac{5}{2}(z)\\
\langle N\rangle&= g_{s}\frac{V}{\lambda_{T}^{3}}f_\frac{3}{2}(z)\\
\mathcal{G}&= -k_{B}T\ln\mathcal{Z}_{G}\\
P&= g_{s}k_{B}T\frac{f_{\frac{5}{2}}(z)}{\lambda_{T}^{3}} 
\end{align*}$$

### 6.15.1 - Gás de Fermi degenerado
- No limite $T\to0$ o número de ocupação médio comporta-se como uma função heaviside:
$$\lim\limits_{T\to0}\langle n_{k}\rangle=\frac{1}{e^{\beta(\varepsilon_{k}-\mu)}+1}=\begin{cases}
0 & ; & \mu<\varepsilon_{k} \\
1 & ; & \mu>\varepsilon_{k}
\end{cases}$$
ou seja
$$\lim\limits_{T\to0}\langle n_{k}\rangle=\Theta(\mu-\varepsilon_{k})$$

#### Energia de Fermi
- Esta é uma energia $\varepsilon_{F}$ em que os níveis abaixo estão todos preenchidos e os acima todos vazios.
- No limite $T\to0$ temos
$$\varepsilon_{k}=\mu(T=0)=\frac{\hbar^{2}k^{2}}{2m}$$
o que significa que, no espaço de fase, a energia de fermi forma uma esfera (de raio $k_{F}$) que separa os níveis preenchidos dos vazios:
$$\varepsilon_{F}=\frac{\hbar^{2}k_{F}^{2}}{2m}$$
(em que um estado está ocupado se $k<k_{F}$)
- E podemos escrever o número médio de partículas:
$$\begin{align*}
\langle N\rangle&= g_{s}\sum\limits_{k=1}^{\infty}\langle n_{k}\rangle\\
&= g_{s}\frac{V}{(2\pi)^{3}}\int \Theta(\mu(T=0)-\varepsilon_{k})d^{3}k \\
&= g_{s}\frac{V}{2\pi^{2}}\int_{0}^{\infty}\Theta(\varepsilon_{F}-\varepsilon_{k})k^{2}dk\\
&= g_{s}\frac{V}{2\pi^{2}}\int_{0}^{k_{F}}k^{2}dk\\
&= g_{s}\frac{V}{2\pi^{2}}\frac{k_{F}^{3}}{3}
\end{align*}$$
e a densidade de partículas é
$$n=\frac{N}{V}=\frac{g_{s}k_{F}^{3}}{6\pi^{2}}~~~~\to~~~~ k_{F}=\sqrt[3]{\frac{6\pi^{2}n}{g_{s}}}$$
que nos dá
$$\varepsilon_{F}=\frac{\hbar^{2}}{2m}\left(\frac{6\pi^{2}n}{g_{s}}\right)^{\frac{2}{3}}$$
- Não sei porquê a temperatura de fermi é dada por $$k_{B}T_F=\varepsilon_{F}$$
- A energia intera será:
$$\begin{align*}
E_{0}&= g_{s}\sum\limits_{k=1}^{\infty}\langle n_{k}\rangle\varepsilon_{k}\\
&= g_{s}\sum\limits_{k=1}^{\infty}\Theta(\varepsilon_{F}-\varepsilon_{k})\varepsilon_{k}\\
&= g_{s}\sum\limits_{k<k_{F}}\varepsilon_{k}\\
&= g_{s}\frac{V}{2\pi^{2}}\int_{0}^{k_{F}}\frac{\hbar k^{2}}{2m}k^{2}dk\\
&= g_{s}\frac{V\hbar}{4m\pi^{2}}\frac{k_{F}^5}{5}
\end{align*}$$
de onde temos que a energia por unidade de partícula será:
$$\frac{E_{0}}{N}=\frac{3}{5}\frac{\hbar^{2}k^{2}_{F}}{2m}=\frac{3}{5}\varepsilon_{F}$$
sendo que perdemos a dependência no spin!