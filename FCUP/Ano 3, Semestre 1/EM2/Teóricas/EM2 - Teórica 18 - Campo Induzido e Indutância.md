## Campo elétrico induzido
![[campo B a mover atraves de loop.png]]
Voltemos ao problema da aula anterior. Imaginemos agora que a região com o campo magnético uniforme e constante se move para a esquerda (sentido negativo dos xx) enquanto que o circuito se mantém em repouso.
- Como na prática temos a mesma situação que tinhamos antes, deveremos continuar a ter
$$\varepsilon=- \frac{d\Phi}{dt}$$
e temos portanto:
$$\varepsilon=- \frac{d}{dt}\int \vec{B}\cdot d \vec{s}=-\int \frac{\partial\vec{B}}{\partial t}\cdot d \vec{s}$$
e da definição de força eletromotriz temos:
$$\varepsilon=\int \vec{E}\cdot d \vec{\ell}=\int (\nabla \times \vec{E})\cdot d \vec{s}$$
e daqui surge a **Lei de Faraday**:
$$\nabla \times \vec{E}=- \frac{\partial\vec{B}}{\partial t}$$
- Esta pequena dedução diz-nos ainda que, no caso em que o campo magnético é que se move, o campo elétrico variável é que gera a força eletromotriz.
- Nesta lei, pode por vezes ser dificil saber qual será o sentido da corrente ou do campo (overall saber os sinais). Assim torna-se útil a **Lei de Lenz**:
$$\boxed{\begin{align*}
&\text{A corrente induzida num loop vai ter a direção que}\\
&\text{gera um campo oposto à da variação de fluxo.}
\end{align*}}$$

### Loop de Ampere
![[loop de ampere.png]]
- Na figura temos um campo vertical variável: $\vec{B}=B(t)\hat{z}$
- Consideremos que estamos numa região sem carga ($\nabla \cdot \vec{E}=0$). Devido ao campo variável temos $\nabla \times \vec{E}=- \partial_{t}\vec{B}$
- O campo elétrico induzido pelo campo magnético será portanto perpendicular a este, tendo direção azimutal $\phi$. Assim, considerando um loop de ampere de raio $\rho$. Temos portanto: $\vec{E}=E(\rho)\hat{\phi}$
- Partindo de $\nabla \times \vec{E}=- \partial_{t}\vec{B}$ podemos integrar o primeiro termo:
$$\int (\nabla \times \vec{E})\cdot d \vec{s}=\oint \vec{E}\cdot d \vec{\ell}=2\pi\rho E(\rho)$$
e ao integrar o segundo termo:
$$\int - \partial_{t}\vec{B}\cdot d \vec{s}=- \frac{d}{dt}\int \vec{B}\cdot d \vec{s}=- \frac{d}{dt} (\pi\rho^{2}B(t))$$
Igualando as 2 integrais:
$$2\pi\rho E(\rho)= \pi \rho^{2} \frac{dB}{dt} \to E(\rho)=-\frac{\rho}{2} \frac{dB}{dt}\to \vec{E}=- \frac{\rho}{2} \frac{dB}{dt} \hat{\phi}$$
em que estamos a assumir que $\frac{d\vec{B}}{dt}$ tem direção constante.
- Em indução magnética, como temos aqui, se o campo magnético variar muito lentamente no tempo, podemos considerar o problema como sendo de magnetostática.

# Indutância
![[indutancia.png]]
- Consideremos o sistema acima. Se passarmos corrente $I_{1}$ no loop 1 gera-se um campo $\vec{B_{1}}$. 
- Naturalmente algumas linhas de corrente $\vec{B_{1}}$ passam dentro da área definida pelo loop 2, gerando-se portanto o fluxo magnético $\Phi_{2}$.
- Pela Lei de Biot-Savart:
$$\vec{B_{1}}= \frac{\mu_{0}}{4\pi} I_{1}\oint \frac{d \vec{\ell_{1}}\times (\vec{r}-\vec{r'})}{|\vec{r}-\vec{r'}|^{3}}$$
e o fluxo no loop 2 será:
$$\Phi_{2}=\int \vec{B_{1}}\cdot \hat{n_{2}}ds_{2}=M_{21}I_{1}$$
em que a constante de proporcionalidade é a *indutância mútua* entre os 2 loops.

- Podemos definir uma fórmula para a indutância.
- Vamos escrever o fluxo em $2$ em termos do vetor potencial:
$$\Phi_{2}=\int \vec{B_{1}}\cdot d \vec{s_{2}}=\int (\nabla \times \vec{A_{1}})\cdot d \vec{s_{2}}=\oint \vec{A_{1}}\cdot d \vec{\ell_{2}}$$
- Vimos no capítulo da magnetostática que:
$$\vec{A}=\frac{\mu_{0}}{4\pi}\int \frac{\vec{\mathcal{J}}(\vec{r'})d^{3}r'}{|\vec{r}-\vec{r'}|}=\frac{\mu_{0}I}{4\pi}\int \frac{d \vec{\ell}}{|\vec{r}-\vec{r'}|}$$
- E podemos escrever para o fluxo:
$$\Phi_{2}=\oint \vec{A_{1}}\cdot d \vec{\ell_{2}}=\oint \left[\frac{\mu_{0}I_{1}}{4\pi}\oint \frac{d \vec{\ell_{1}}}{|\vec{r}-\vec{r'}|}\right]\cdot d \vec{\ell_{2}}=\frac{\mu_{0}I_{1}}{4\pi}\oint \oint \frac{d \vec{\ell_{1}}\cdot d \vec{\ell_{2}}}{|\vec{r}-\vec{r'}|}$$
ou seja:
$$M_{21}=\frac{\mu_{0}}{4\pi}\oint \oint \frac{d \vec{\ell_{1}}\cdot d \vec{\ell_{2}}}{|\vec{r}-\vec{r'}|}$$
a que se chama de **Fórmula de Newmann**. Ela envolve um integral de linha duplo e normalmente não é muito útil em cálculos. 
- No entanto, esta fórmula mostra-nos que a indutância mútua:
    - Apenas depende da configuração e aspetos geométricos dos loops.
    - Podemos trocar o sistema inicial (o loop 2 é que se move e gera fluxo no 1) e teremos $M_{12}$, tal que: $$M_{12}=M_{21}$$

- Consideremos agora que a corrente através do loop 1 varia. O fluxo através de 2 irá variar de forma correspondente. Ora, pela lei de Faraday isto irá induzir uma força eletromotriz no loop 2 dada por:
$$\varepsilon_{2}=- \frac{d\Phi_{2}}{dt}=-M \frac{dI_{1}}{dt}$$
(de acordo com o que vimos acima)

- Por outras palavras, ao variar a corrente em 1 induzimos uma corrente em 2.
- No entanto, a variação de fluxo em 1 também induz corrente no próprio loop 1. Temos então:
$$\Phi=LI$$
e portanto:
$$\varepsilon=-L \frac{dI}{dt}$$
em que $L$ é  **indutância** do loop.
