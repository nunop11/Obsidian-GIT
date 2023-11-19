## Comprimento De Onda de De Broglie (1923)
- O Modelo Bohr (que já agora é empírico) diz que, no átomo de hidrogénio as únicas órbitas permitidas são aquelas em que: $$L=n\hbar \quad \quad \quad \left(\hbar=\tfrac{h}{2\pi}\right)$$
que bate certo com a regra de quantificação da energia de Planck que nos diz que:
$$E_{n}=- \left(\frac{e^{2}}{4\pi\varepsilon_{0}}\right) \frac{m_{e}}{2\hbar^{2}} \frac{1}{n^{2}}$$
ora, no início do séc. XX queriasse saber o porquê de a energia estar quantizada assim.

- Ora, em 1923 De Broglie propôes que as partículas têm comportamento de onda. Ou seja, além de quantidades/caraterística corpusculares como campo elétrico e campo, elas também teriam associadas a quantidades ondulatórias como frequência e comprimento de onda (de De Broglie).
- Ora, segundo Einstein temos que a energia de um fotão é $E=h \nu=\hbar \omega$. Além disso, para ondas eletromagnéticas temos $E=c |\vec{p}|=cp$. Assim:
$$cp=h \nu \leftrightarrow cp=h \frac{c}{\lambda} \leftrightarrow \lambda =\frac{h}{p}=\frac{2\pi}{k}$$
- Em 1927 foi observado o padrão de difração da dupla fenda que falamos atrás com eletrões. Ora, deste resultado podemos tirar para os eletrões as mesmas conclusões que tiramos para fotões:
    - ocorrem interferências
    - o padrão de interferência indica probabilidade
    - abandono da noção clássica de trajetória

## Física Clássica ou Física Quântica??
- Para saber se, num certo problema, usamos física quântica ou clássica basta comparar $[h]$ com $[E]\times [t]$. 
- De notar que a energia que usamos para isto pode ser cinética, potencial ou a soma de ambas, porque apenas queremos saber da ordem de grandeza.

> **EXEMPLOS**
> *Oscilador Harmónico Simples* 
>     - Temos que $E_{c}=\frac12mv^{2}$. Além disso, $[\omega]=[t]^{-1}$. Assim: $[1/\omega]=[t]$. Podemos então escrever: $v=\omega A$ (em que $A$ é a amplitude do oscilador) e temos: $E_{c}=\frac12 m(\omega A)^{2}$ sendo que $[E_{c}]=[E]$ 
>     - Assim, como $h$ tem dimensão de $E \times t$ AKA dimensões de ação, temos que a ação deste problema é: $$S\sim E_{c} \cdot \Delta t \sim m v^{2} \cdot \frac{1}{\omega}\sim m (\omega A)^{2} \frac{1}{\omega}\sim m \omega A^{2}$$
>     (de notar que aqui ignoramos o $\frac{1}{2}$ porque só importa a ordem de grandeza dos termos)
>     - Consideremos um exemplo mais concreto: $m=0.1kg~,~\omega=1s^{-1}, A=0.1m$. Usando o que temos acima dá: $$S\sim 10^{-3}Js \gg h=6.626\cdot10^{-34}Js$$Ou seja, o problema é **clássico**.
> *Eletrão a oscilar*
>     - Temos que $m_{e}\sin 10^{-31}kg$. Consideremos oscilações harmónicas à escala molecular ($A\sim10^{-9}m$) a imitir radiação na zona do visível, ou seja, com $\omega\sim 10^{-14}s^{-1}$. Assim temos $$S\sim 10^{-35}Js<h$$
>     pelo que o problema será **quântico**.

### Caso do Fotão
- Para um fotão, vejamos o critério acima. Temos a energia $E$ e consideremos que ele está a oscilar com uma frequência $\omega$. Temos: $$S\sim \frac{E}{\omega}= \hbar<h$$
isto vem de $E=\hbar \omega$, pelo que teríamos um sistema quântico.
- No entanto, isto implica que $v=c$ AKA *mecânica quântica relativista*, algo que não estudaremos nesta UC.

# 2 - Função de Onda
- Antes de começar este capítulo, vamos substituir a noção clássica de trajetória (de ter uma partícula com posição e momento bem definidos) pelo conceito de estados que evoluem no tempo.
- Assim, para partículas sem spin, o seu estado é definido pela função de onda $\Psi(\vec{r},t)$ (sendo esta uma função complexa). Temos que:
    - $\Psi(\vec{r},t)$ é a *amplitude de Probabilidade*
    - $|\Psi(\vec{r},t)|^{2}=\Psi^{*}\Psi$ é a *densidade de Probabilidade*

- Deste modo, a probabilidade de, num instante $t$, encontrar uma partícula e, $[\vec{r}, \vec{r}+ d \vec{r}]$ é $$d \mathcal{P}=|\Psi(\vec{r},t)|^{2}~d^{3}r$$
- Vejamos então alguns pontos importantes

**_i) Princípio de Decomposição Espectral_**
- Quando fazemos uma medição de uma quantidade física, o valor medido pertence a um conjunto de valores permitidos.
**_ii)_**
- Cada valor próprio $a$ está associado a um estado próprio com uma função de onda $\Psi_{a}(\vec{r}, t)$.
**_iii)_**
- Se fizermos a medição em $t=t_{0}$ e medirmos a grandeza associada ao estado $a$ dá-se *colapso da função de onda* e temos: $\Psi(\vec{r}, t\ge t_{0}) = \Psi_{a}(\vec{r}, t)$
**_iv)_**
- Para uma função de onda $\Psi(\vec{r},t)$ a probabilidade de ter a partícula no estado $a$ em $t=t_{0}$ ($\mathcal{P}_{a}$) é obtida ao decompor a função de onda em funções: $$\Psi(\vec{r},t_{0})=\sum\limits_{a} c_{a} \Psi_{a}(\vec{r}) \quad \quad \longrightarrow \quad \quad \mathcal{P}_{a}=\frac{|c_{a}|^{2}}{\sum\limits_{a}|c_{a}|^{2}}$$
sendo que, se a função de onda estiver normalizada, temos $\sum\limits_{a}|c_{a}|^{2}=1$
**_v) Equação de Schrödinger_**
- Esta é a equação que determina como a função de onda irá evoluir no tempo:
$$i\hbar \frac{\partial \Psi}{\partial t}=- \frac{\hbar^{2}}{2m} \Delta \Psi+V \Psi$$
em que se usou a notação $\Delta=\nabla^{2}=\nabla \cdot \nabla\equiv \textsf{Laplaciano}$

#### Observações
- A equação de Schrödinger:
    - é linear, pelo que podemos aplicar o princípio da sobreposição.
    - é uma equação de 1ª ordem em $t$ e de 2ª ordem em $x,y,z$
    - diz-nos que se $\Psi(\vec{r},t_{0})$ for conhecida, $\Psi(\vec{r},t)$ pode ser determinado

- A probabilidade de encontrar uma partícula *algures* no espaço é 1, obviamente. Assim: $$\int d \mathcal{P}=1 \quad \longrightarrow \quad \int d^{3}r |\Psi(\vec{r},t)|^{2}=1$$
sendo esta a condição de normalização da função de onda.