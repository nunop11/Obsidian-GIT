###### Aula 13 - 11/4/2024

> NOTA: Esta aula foi um desastre
# Difração em Rede
- Vimos que ocorre difração de um feixe incidente com vetor $\vec{k}$, obtendo-se um feixe refletido com vetor $\vec{k'}$ se e só se $\vec{k}-\vec{k'}=\vec{K}$ (vetor da rede recíproca)
- Ora, sendo $d_{hkl}$ a distância entre os 2 pontos da rede real que geram a difração teremos que $K_{hkl}=2\pi/d_{hkl}$

**Num cristal**
- Temos 2 coisas a ter em conta: a difração gerada por 1 átomo e interferência das difrações dos vários átomos.
- Para o caso de um feixe Raio X, o scattering ocorre devido aos eletrões. Para o caso de um feice de neutrões, o scattering ocorre devido aos protões.

- Dentro do cristal (distâncias reduzidas em relação aos átomos), consideremos a onda plana monocromática $u_{i}(\vec{r},t)=A e^{i(\vec{k}\cdot\vec{r}-\omega t)}$
- Fora do cristal (distâncias suficientemente elevadas) consideremos a onda esférica: $u_{sc}(r,t)=f_{sc} \frac{A}{r} e^{i(k_{sc}r-\omega t)}$, ou seja, ocorre scattering do feixe inicial. Temos que $f_{sc}$ é o fator de Thomson, que não encontro online :D
- Consideremos que não há perdas, de modo que $k_{0}=k_{sc}$

- Consideremos:
![[reflexao bragg.png|500]]
- Sendo as ondas incidentes descritas por $u_{1},u_{2}$ do tipo $u=f_{sc} \frac{A}{r} e^{i(kr-\omega t)}$ Considerando que são ondas "iguais" mas com diferença de fase, temos que a onda resultante da sua interferência será:
$$\begin{align*}
u_{sc} &\sim f_{sc} \frac{A}{r} \left[ e^{ikr} + e^{i(kr+\delta)} \right]
\end{align*}$$
- Consideremos que $\vec{r}$ é $\vec{d}$ na imagem acima. Consideremos ainda que $\vec{s}=\vec{k}_{sc}/k_{sc}~,~\vec{s}_{0}=\vec{k_{0}}/k_{0}$ são os versores da direção incidente e refletida (correspondem a $\hat{n},\hat{n'}$ acima). Assim, para haver interferência construtiva a diferença de fase entre os sinais terá que ser igual (ou proporcional) à diferença de percurso dos 2 feixes, dada por:
$$\begin{align*}
\delta&= 2\pi(\vec{r}\cdot\vec{s} - \vec{r}\cdot\vec{s_{0}})\\
&= \vec{r}\cdot(\vec{k_{sc}}-\vec{k_0})=\vec{r}\cdot\vec{K}
\end{align*}$$
(sim, repetimos a dedução da aula passada)
- Ora, podemos definir as posições átomos que geram a difração como $\vec{r_{1}},\vec{r_{2}}$ logo:
$$\delta=\vec{K}\cdot(\vec{r_{1}}-\vec{r_{2}})$$

- Assim, para um sistema com 2 átomos temos:
$$\begin{align*}
u_{sc}&= f \frac{A}{r} e^{ikr}\left[e^{i\vec{s}\cdot\vec{r_{1}}} + e^{i\vec{s}\cdot\vec{r_{2}}} \right]
\end{align*}$$
e para $n$ átomos:
$$\begin{align*}
u_{sc}&= f \frac{A}{r}e^{ikr} \sum\limits_{i=1}^{n}e^{i \vec{s}\cdot\vec{r_{i}}}\\
&= \frac{A}{r} \left[f \sum\limits_{i=1}^{n}e^{i \vec{s}\cdot\vec{r_{i}}}\right] e^{ikr}\\
&= \frac{A}{r}f_{a}e^{ikr}
\end{align*}$$
- Tendo-se $f_{a}$ o **fator de fórmula atómica** (Atomic Form Factor em inglês)

### Contínuo
- Consideremos agora o caso contínuo:
$$f\sum\limits_{i=1}^{n}e^{i \vec{s}\cdot\vec{r_{i}}}~~\to~~ f\int \rho(\vec{r})e^{i \vec{s}\cdot\vec{r}}d^{3}r$$
Este integral não passa da **transformada de Fourier da rede**!

- Ora, a intensidade da radiação emitida por 1 átomo será:
$$I\propto |u_{sc}|^{2}\sim |f|^{2} \Biggr| \int \rho(\vec{r})e^{i \vec{s}\cdot\vec{r}}d^{3}r\Biggr|^{2}$$

**Fator Fórmula Atómica / Atomic Form Factor**
- Vejamos o fator de fórmula atómica em coordenadas esféricas:
$$\begin{align*}
f_{a}&\propto \int \rho(\vec{r})e^{i \vec{s}\cdot\vec{r}}d^{3}r\\
&= 4\pi\int_{0}^{R} \rho(\vec{r})r^{2} \frac{\sin(sr)}{sr}dr\\ 
\end{align*}$$
em que $s=2k\sin\theta$. Não percebi esta transição de todo
- Assim vemos que o fator depende da rede, mas também da diferença e ângulo entre os feixes incidente e refletido.
- Estes valores estão tabelados e variam da átomo para átomo.

### Toda a rede 
- Queremos agora estudar a difração que ocorre quando o feixe raio X incide na rede toda.
- Assim temos que introduzir 2 fatores:
    - $F$ - Fator de *estrutura geométrica* - relacionado com a célula primitiva
    - $S_{\vec{K}}$ - Fator de *estrutura da rede* - indica o quanto as interferências das ondas scattered irá diminuir a intensidade do pico de Bragg associado ao vetor $\vec{K}$.

- E temos
$$\begin{align*}
F&= \sum\limits_{j}f_{aj}e^{i \vec{s}\cdot\vec{\delta_{j}}}\\
S_{\vec{K}} &= \sum\limits_{\ell}e^{i \vec{K}\cdot\vec{r_{\ell}}}
\end{align*}$$
Em que:
    - $\vec{s}=\vec{k}_{sc}-\vec{k}$ é o vetor de difração que vimos acima
    - $\vec{r_{\ell}}$ é o vetor de posição de 1 célula 
    - $\vec{\delta_{\ell}}$ o vetor da posição relativa de um átomo dentro da célula
    - $f_{aj}$ é o fator de fórmula atómica do átomo $j$. Ou seja, vamos percorrer todas as células e todos os átomos dentro destas.

- Temos então o *fator de cristal*:
$$\begin{align*}
f_{cr}&= \sum\limits_{\ell}f_{a\ell} e^{i \vec{s}\cdot\vec{R_\ell}}\\
&= \sum\limits_{\ell}\sum\limits_{j} f_{aj} e^{i \vec{s}\cdot(\vec{R_{\ell}}+\vec{\delta_{j}})}\\
&= \sum\limits_{\ell}e^{i \vec{s}\cdot\vec{R_{\ell}}} \cdot\sum\limits_{j}f_{aj} e^{i \vec{s}\cdot\vec{\delta_{j}}}\\
&= S_{\vec{K}} \cdot F
\end{align*}$$
(que podemos ver como sendo um análogo ao fator de forma atómica, mas para uma rede cristalina)
em que a intensidade do feixe refletido segue:
$$I \sim |f_{cr}|^{2}$$

- Ou seja, o facto de termos  $f_{cr}=SF$ significa que só temos difração se nenhum dos 2 fatores for nulo:
    - $S$ não é nulo se $s\in\vec{K}$ - condição de Laue
    - $F$ não é nulo dependendo da base usada. Vejamos um exemplo:

## EX - BCC como Cúbica com Base
- Consideremos a seguinte rede BCC:
![[difracao em fcc- rede.png|500]]
- Vamos considerá-la uma rede cúbica simples com uma base.
- Para uma rede cública simples, ocorre difração para todos os vetores da rede recíproca
- Consideremos agora o átomo no centro do cubo. Recordemos que o átomo no centro vale por 1 e os átomos nos cantos valem por 1/4 por serem partilhados. Ou seja, temos 2 átomos nesta célula. Assim, consideremos que os 2 átomos são iguais (logo têm o mesmo $f_{aj}$) e temos:
$$\begin{align*}
\vec{K}_{hkl}&= h \vec{b_{1}}+k \vec{b_{2}}+l \vec{b_{3}}\\
\vec{R} &= n_{1}\vec{a_{1}}+n_{2}\vec{a_{2}}+n_{3}\vec{a_{3}}
\end{align*}$$
e ainda $\vec{b_{i}}\cdot\vec{a_{j}}=2\pi \delta_{ij}$ logo:
$$\begin{align*}
\vec{b_{1}}=\frac{2\pi}{a}\hat{i} \quad;\quad \vec{b_{2}}=\frac{2\pi}{a}\hat{j} \quad ;\quad \vec{b_{3}}=\frac{2\pi}{a}\hat{k}
\end{align*}$$
- Temos átomos nas posições: $$\vec\delta_{1}=(0,0,0)\quad \quad;_{\quad}\quad \vec{\delta_{2}}=\frac{a}{2}(1,1,1)$$ 
- Assim temos:
$$\begin{align*}
f_{cr}&= f_{aj}\sum\limits_{\ell}e^{i \vec{s}\cdot\vec{R}_{\ell}}\\
&= f_{aj}+ f_{aj}\exp\left[{i \vec{k}_{hkl} \cdot \vec{\frac{a}{2}}(\hat{i}+\hat{j}+\hat{k})}\right]\\
&= f_{aj}[1+e^{i\pi (h+k+l)}]\\
&= \begin{cases}
2f_{aj} &; &h+k+l=\text{par} \\
0 &; &h+k+l=\text{ímpar}
\end{cases}
\end{align*}$$

- Se formos a verificar vários $hkl$ iremos obter o seguinte espaço recíproco:
![[difracao em fcc - permitidos e n permitidos.png|450]]
em que os pontos a vermelho são os pontos em que $f_{cr}=0$.

- Ora, a rede recíproca desta célula cúbica com o átomo no centro descreve um *padrão FCC*. Ou seja, esta configuração gera a mesma difração que uma estrutura BCC!!!
- Isto mostra que podemos descrever uma rede de Bravais como uma rede com uma base e iremos obter a mesma rede recíproca. 
- Além disso, devemos notar que a introdução do átomo no centro da geometria cúbica causou **ausências** (pontos que deixaram de pertencer à rede recíproca)
