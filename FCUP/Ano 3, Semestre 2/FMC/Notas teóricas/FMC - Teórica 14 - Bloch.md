###### Aula 14 - 16/4/2024 (dada por EVC)
# Eletrões num Potencial
## Teorema de Bloch
- Como os iões estão distribuídas de forma periódica e simétrica na rede de Bravais, surge um problema importante: como se comporatrão os eletrões se o sistema estiver sujeito a potencial periódico $V(\vec{r})=V(\vec{r}+\vec{R})$:
![[potencial periodico.png|370]]
- Consideremos o Hamiltoniano $$\hat{H}=\frac{\hat{\vec{P}}}{2m}+\hat{V}$$
que na base das posições $\langle \vec{r}\ket{\hat{H}|\vec{r}}$ nos dá
$$H_{\vec{r}}(\vec{r})=- \frac{\hbar^{2}}{2m}\nabla^{2}_{\vec{r}} + V(\vec{r})$$
- Para a ESIT tem soluções do tipo:
$$H_{\vec{r}}\Psi_{\vec{k},n}(\vec{r})= E_{\vec{k},n}\Psi_{\vec{k},n}(\vec{r})$$
ora, isto implica que como $V(\vec{r}+\vec{R})=V(\vec{r})$, para cada $\vec{k}$ podemos ter mais que uma solução; sendo $n$ o *índice de banda*.

- O **==teorema de Bloch==** diz-nos que: "estados próprios $\psi$ do Hamiltoniano de 1 eletrão $H$ (com potencial periódico) podem ser definos como **ondas planas** com a mesma periodicidade da rede de Braivais", pelo que temos funções de onda do tipo:
$$\Psi_{\vec{k},n}(\vec{r})=e^{i \vec{k}\cdot\vec{r}}u_{\vec{k},n}(\vec{r})$$
(No Ashcroft - Capítulo 8 há uma demonstração deste teorema com operadores de translação)

**O que é k**
- O $\vec{k}$ é basicamente o mesmo que no Sommerfeld. No entanto, aí tínhamos que cada k é um estado diferente. Em Bloch deixamos de ter isso, como vimos acima.

**CF Cíclicas / de Born-Von Karman**
- Consideremos condições de fronteira cíclicas.
    - Consideremos um sistema com $N$ células unitárias, $N=N_{1}N_{2}N_{3}$ (sendo $N_{i}$ o número de células na direção $i$)
    - Temos então: $$\Psi(\vec{r}+N_{i}\vec{a_{i}})=\Psi(\vec{r}+\vec{R})=\Psi(\vec{r})$$em que vemos de forma intuitiva que $N_{i} \vec{a_{i}}=\vec{R}$
- Podemos conjugar isto com a função de onda solução da ESIT que vimos acima:
$$\begin{align*}
\Psi(\vec{r}+N_{i}\vec{a_{i}})&= e^{i \vec{k}\cdot(\vec{r}+N_{i}\vec{a_{i}})}u(\vec{r})\\
&= e^{i \vec{k}\cdot(N_{i}\vec{a_{i}})}\Psi(\vec{r})
\end{align*}$$
- Como o potencial e a função de onda são periódicos temos:
$$e^{i \vec{k}\cdot(N_{i}\vec{a_{i}})}\Psi(\vec{r})=\Psi(\vec{r})$$
Logo é necessário que:
$$\boxed{e^{i N_{i} \vec{k}\cdot\vec{a_{i}}}=1} \quad \quad;\quad \quad N_{i}\vec{k}\cdot\vec{a}_{i}=2\pi m_{i}~~,~m_{i}\in\mathbb{Z}$$
- Ou seja:
$$\begin{align*}
\vec{k}=\sum\limits_{i} \frac{m_{i}}{N_{i}}\vec{b}_{i}
\end{align*}$$
(em que $\vec{b}$ é vetor base da rede recíproca, em que $\vec{a_{i}}\cdot\vec{b_{i}}=2\pi m\delta_{ij}$)
- Usando isto podemos definir o volume ocupado por 1 estado:
$$\Delta k= \frac{\vec{b_{1}}}{N_{1}}\cdot\left(\frac{\vec{b_{2}}}{N_{2}}\times\frac{\vec{b_{3}}}{N_{3}}\right)=\frac{1}{N}[\vec{b_{1}}\cdot(\vec{b_{2}}\times\vec{b_{3}})]$$
recordando ALGA, vemos que o produto de $\vec{b_{i}}$ que temos acima corresponde ao *determinante* dos vetores $\vec{b_{1}},\vec{b_{2}},\vec{b_{3}}$ que definem um paralelepípedo, ou seja, o volume da célula primitiva.
- Sabemos que esse volume é $\frac{(2\pi)^{3}}{v}~,~ v=V/N$ logo resulta:
$$\Delta k=\frac{(2\pi)^{3}}{V}$$

### Transformada de Fourier de Função Periódica
- Consideremos uma função periódica: $f(x)=f(x+L)$. Claramente, isto é o caso da função de onda considerada acima.
- Podemos então definir a série:
$$f(x)=\sum\limits f_{k}e^{ikx}~~~~;~~~~k=\frac{2\pi}{L}~,~n\in\mathbb{Z}$$
em que podemos definir a transformada de Fourier:
$$f_{k}=\frac{1}{L}\int_{0}^{L}e^{-ikx}f(x)dx$$

**3D - ESIT**
- Consideremos a função de onda 3D que vimos atrás: $\Psi(\vec{r})=\Psi(\vec{r}+N_{i}\vec{a_{i}})$
- Podemos definir a série:
$$\Psi(\vec{r})=\sum\limits_{\vec{k}}f_{\vec{k}}e^{i \vec{k}\cdot\vec{r}}$$
logo temos
$$f_{\vec{k}}=\frac{1}{V}\int dr~e^{-i \vec{k}\cdot\vec{r}}\Psi(\vec{r})$$

### De volta à Física
- Ora, como $\Psi,V$ são ambas funções periódicas, podemos escrever as suas séries de Fourier:
$$\Psi(\vec{r})=\sum\limits_{\vec{q}}c_{\vec{q}} e^{i \vec{q}\cdot\vec{r}} \quad \quad;\quad \quad V(\vec{r})=\sum\limits_{\vec{K}}V_{\vec{K}}e^{i \vec{k}\cdot\vec{r}}$$
(em que $\vec{K}$ é o vetor da rede recíproca, análogo de $\vec{R}$) (podemos expandir desta forma todas as funções que obedecem a este tipo de CF)

- Vamos reescrever a ESIT:
$$\begin{align*}\\
\left(- \frac{\hbar^{2}}{2m}\nabla^{2}+V(\vec{r})\right)\Psi&= E \Psi\\
\left(- \frac{\hbar^{2}}{2m}\nabla^{2}+\sum\limits_{\vec{K}}V_{\vec{K}}e^{i \vec{k}\cdot\vec{r}}\right)\left(\sum\limits_{\vec{q}} c_{\vec{q}}e^{i \vec{q}\cdot\vec{r}}\right)&= E \left(\sum\limits_{\vec{q}} c_{\vec{q}}e^{i \vec{q}\cdot\vec{r}}\right)\\
\sum\limits_{\vec{q}}\frac{\hbar^{2}}{2m}q^{2}c_{\vec{q}}e^{i \vec{q}\cdot\vec{r}} + \sum\limits_{\vec{q},\vec{K}}V_{\vec{K}}c_{\vec{q}}e^{i(\vec{k}+\vec{K})\cdot\vec{r}}&=  E \left(\sum\limits_{\vec{q}} c_{\vec{q}}e^{i \vec{q}\cdot\vec{r}}\right)\\
\end{align*}$$
podemos definir $\vec{q}+\vec{K}=\vec{q'}$ e temos:
$$\begin{align*}
\sum\limits_{\vec{q}}\frac{\hbar^{2}}{2m}k^{2}c_{\vec{k}}e^{i \vec{k}\cdot\vec{r}} + \sum\limits_{\vec{q'},\vec{K}}V_{\vec{K}}c_{\vec{q'}-\vec{K}}e^{i\vec{q'}\cdot\vec{r}}&=  E \left(\sum\limits_{\vec{q}} c_{\vec{q}}e^{i \vec{q}\cdot\vec{r}}\right)\\
\sum\limits_{\vec{q}} e^{i \vec{q}\cdot\vec{r}}\left[\left( \frac{\hbar^{2}}{2m}q^{2}-E \right)c_{\vec{q}}+\sum\limits_{\vec{K'}}V_{\vec{K'}}c_{\vec{k}-\vec{K'}}\right]&= 0\\
\end{align*}$$
(no 2º passo simplesmente mudamos a soma de $\vec{k'}$ para uma soma de $\vec{k}$ e mudamos $\vec{K}$ para $\vec{K'}$, "porque estamos a somar os valores todos, então vai dar ao mesmo" - Dudu)
- Ora, é conveniente escrever $\vec{q}=\vec{k}-\vec{K}$ (em que $\vec{k}$ será um ponto na 1ZB) e temos:
$$\sum\limits_{\vec{q}} e^{i \vec{q}\cdot\vec{r}}\left[\left( \frac{\hbar^{2}}{2m}(\vec{k}-\vec{K})^{2}-E \right)c_{\vec{k}-\vec{K}}+\sum\limits_{\vec{K'}}V_{\vec{K'}}c_{\vec{k}-\vec{K'}}\right]=0$$
e fazemos $\vec{K'}\to \vec{K'}-\vec{K}$:
$$\sum\limits_{\vec{q}} e^{i \vec{q}\cdot\vec{r}}\left[\left( \frac{\hbar^{2}}{2m}(\vec{k}-\vec{K})^{2}-E \right)c_{\vec{k}-\vec{K}}+\sum\limits_{\vec{K'}}V_{\vec{K'}-\vec{K}}c_{\vec{k}-\vec{K'}}\right]=0$$

- Isto resulta então na **Equação Central**:
$$\left( \frac{\hbar^{2}}{2m}(\vec{k}-\vec{K})^{2}-E \right)c_{\vec{k}-\vec{K}}+\sum\limits_{\vec{K'}}V_{\vec{K'}-\vec{K}}c_{\vec{k}-\vec{K'}}=0$$
não entendi como, isto significa que podemos substituir $\vec{k}\to \vec{k}-\vec{K}$ na expansão Fourier da função de onda, o que resulta em:
$$\Psi_{\vec{k}}(\vec{r})=e^{i \vec{k}\cdot\vec{r}}\left(\sum\limits_{\vec{K}}c_{\vec{k}-\vec{K}}e^{-i \vec{K}\cdot\vec{r}} \right)$$
- Assim, tendo em conta a periodicidade, temos:
$$\Psi_{\vec{k}+\vec{K'}}(\vec{r})=e^{i (\vec{k}+\vec{K'})\cdot\vec{r}}\left(\sum\limits_{\vec{K'}}c_{\vec{k}+\vec{K'}-\vec{K}}e^{i (\vec{K'}-\vec{K})\cdot\vec{r}} \right)$$
e notemos que isto tem que ser equivalente a:
$$\Psi_{\vec{k},n}(\vec{r})=e^{i \vec{k}\cdot\vec{r}}u_{\vec{k},n}(\vec{r})$$
- Ou seja, $n$ indica a ZB em que está o $\vec{k}$ associado. $n$ é o *índice de banda*. 
- Os $k$ que representam bandas diferentes podem ser escritos em função daqueles da ZB1 mais um vetor $\vec{K}$.
