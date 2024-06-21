- Até aqui estudamos metais como meios em que temos eletrões quase livres sujeitos a potenciais fracos, causados pela rede iónica.
- Vamos agora estudar metais como coleções de átomos neutros com interações fracas.

### Átomos de Sódio
- Consideremos que temos uma rede BCC de átomos de sódio com parâmetros de centímetros. Poderíamos sem problemas estudar cada eletrão dos átomos como uma função de onda correspondente às orbitais atómicas.
- Mas se comprimirmos o sistemas (reduzir parâmetro de rede) as funções de onda passavama a sobrepôr-se, o que não convém nada.

## Método de Tight-Binding
- Usamos quando a sobreposição de funções de onda atómicas é suficiente para serem necessárias correções à descrição de átomos isolados. Mas também não podemos ter sobreposição tão intensa que a descrição atómica se torne irrelevante.
- Consideramos que nas proximidades de cada potno da rede o Hamiltoniano do cristal $H$ pode ser aproximado ao Hamiltoniano de 1 átomo $H_{at}$.
- Assumimos ainda que as funções próprias de $H_{at}$ são bem localizadas:
$$H_{at}\psi_{n}=E_{n}\psi_{n}$$
e exigimos $\psi_{n}(\vec{r})$ reduzido quando $\vec{r}$ excede a ordem de grandeza do parâmetro de rede.

**Perturbação**
- Consideremos:
$$H=H_{at}+\Delta V(\vec{r})$$
(no caso extremo em que começamos a ter sobreposição de funções de onda atómicas)

- Se $\psi_{n}$ for solução da equação com $H_{at}$ e desta última, podemos dizer que ele corresponde a uma sobreposição de $N$ níveis (que correspondem aos átomos vizinhos). Ou seja:
$$\psi_{n,\vec{k}}(\vec{r})=\sum\limits_{\vec{R}}e^{i\vec{k}\cdot\vec{R}}\psi_{n}(\vec{r}-\vec{R})$$
sendo que esta solução satisfaz o *teorema de Bloch*.

**Correção a Perturbação**
- Para corrigir a perturbação, consideremos que $\psi_{n}$ se torna reduzido antes de $V$ se tornar elevado:
![[Pasted image 20240604003209.png|450]]
- Ou seja, queremos que $$\Delta V|\psi(\vec{r})^{2}|\ll1$$
- Ou seja, queremos uma função $\psi_{n,\vec{k}}$ do tipo que temos acima, mas assim:
$$\psi_{n,\vec{k}}(\vec{r})=\sum\limits_{\vec{R}}e^{i\vec{k}\cdot\vec{R}}\phi(\vec{r}-\vec{R})$$
em que $\phi(\vec{r})$ pode não ser função própria do Hamiltoniano.
- Na realidade, estas funções são determinadas com cálculos adicionais e chamam-se *Funções de Wannier*.
- Para normalizar $\psi_{n,\vec{k}}$ devíamos multiplicá-lo por $1/\sqrt{N}$

**Funções de Wannier**
- Se $\Delta V|\psi(\vec{r})|^{2}\ll1$, então podemos (?) presumir que $\phi$ será muito próxima de $\psi_{n}$ (ou de funções degeneradas com $\psi_{n}$)
- Assim consideremos:
$$\phi(\vec{r})=\sum\limits_{n}b_{n}\psi_{n}(\vec{r})$$
- Aqui estamos então a definir $\phi$ usando apenas funções de onda atómicas localizadas. Isto é uma aproximação significativa, poruq podemos estar a incluir níveis ionizados. Ou seja, esta aproximação faz com que o método não se aplique a níveis de eletrões quase livres.

**ES**
$$\begin{align*}
H_{at}\psi_{n,\vec{k}} + \Delta V(\vec{r})\psi_{n,\vec{k}}&= E_{n}(\vec{k})\psi_{n,\vec{k}}\\
\psi_{m}^{*}H_{at}\psi_{n,\vec{k}} + \psi_{m}^{*}\Delta V(\vec{r})\psi_{n,\vec{k}}&= \psi_{m}^{*}E_{n}(\vec{k})\psi_{n,\vec{k}}\\
\int\psi_{m}^{*}H_{at}\psi_{n,\vec{k}}d^{3}r + \int\psi_{m}^{*}\Delta V(\vec{r})\psi_{n,\vec{k}}d^{3}r&=\int \psi_{m}^{*}E_{n}(\vec{k})\psi_{n,\vec{k}}d^{3}r\\
[E_{n,\vec{k}}-E_{m}]\int\psi_{m}^{*}\Delta V(\vec{r})\psi_{n,\vec{k}}d^{3}r&= \int\psi_{m}^{*}\Delta V(\vec{r})\psi_{n,\vec{k}}d^{3}r
\end{align*}$$
- E substituimos $\psi_{n,\vec{k}}(\vec{r})=\sum\limits_{\vec{R}}e^{i\vec{k}\cdot\vec{R}}\phi(\vec{r}-\vec{R})$ com $\phi(\vec{r})=\sum\limits_{n}b_{n}\psi_{n}(\vec{r})$, podendo-se obter:
$$\begin{align*} \left[E_n(\textbf k) - E_m\right]b_m =& -[E_n(\textbf k) - E_m]\sum_n \left(\sum_{\textbf R\neq0} \color{#00d100}{\int \psi_m^* (\textbf r)\psi_n(\textbf r - \textbf R)e^{i\textbf k \cdot \textbf R}d^3r}\right)b_n \,+ \\
&+ \sum_n \left(\int \psi_m^* (\textbf r)\Delta V(\textbf r) \psi_{n}(\textbf r)d^3r\right)b_n \,+ \\
&+ \sum_n \left(\sum_{\textbf R\neq 0}\color{#00d100}{\int \psi_m^* (\textbf r) \Delta V(\textbf r) \psi_n(\textbf r- \textbf R)e^{i\textbf k \cdot\textbf R}d^3r} \right)b_n \end{align*}$$
- Os integrais a verde são *integrais de overlap*. Quando acima dissemos que as funções de onda estão bem localizadas, temos que estes integrais são $\ll1$.
    - Quanto menos o overlap, menor a largura da banda (diferença entre energia máxima e mínima)
- O segundo termo também é pequeno porque $\Delta V$ só é significativo em zonas em que as interações eletrõnicas são quase nulas.
    - Esta aproximação é mais instável, mas menos importante.
    - Na prática, este termo corrige os potenciais atómicos dentro de cada célula para incluir os campos dos iões fora da célula.

**Interpretação**
- O lado esquerdo da equação também é pequeno: quando a diferença é pequena se $b_{m}$ não for e vice versa.
- Assim, $E_{n,\vec{k}}\sim E_{0}$ (um nível atómico) e todos os $b_{m}$ (execeto o desse nível atómico) são reduzidos.

**Velocidade de Eletrão em Estado de Banda**
- A velocidade média de um eletrão num nível de Bloch com vetor de onda $\vec{k}$ e energia $E_{\vec{k}}$ é:
$$\langle v(\vec{k})\rangle=\frac{1}{\hbar} \frac{\partial E(\vec{k})}{\partial\vec{k}}$$
    - Se $E$ for independente de $\vec{k}$ temos $\langle v\rangle=0$, o que faz sentido porque isto consiste no caso em que os eletrões estão presos a átomos.
    - Senão, existe uma velocidade média não nula. Os eletrões movem-se pelo cristal. Quanto menor a sobreposição de funções de onda, menor a velocidade.

## Bandas S e P
### S
- Temos todos os $b_{m}$ nulos, exceto para o coeficiente relativo à orbital s de um átomo. Temos:
$$\begin{align*}
&\left[E_{n,\vec{k}}-E_s\right] \left[1 + \sum_{\vec R \neq 0}e^{i\vec k \cdot \vec R}\int\psi_s^*(\vec r) \psi_s(\vec r- \vec R) d^3r \right] - \\ -& \int \psi_s^* (\vec r)\Delta V(\vec r)\psi_s(\vec r) d^3r - \left[\sum_{\vec R\neq 0} \int \psi_s^*(\vec r)\Delta V(\vec r)e^{i\vec k \cdot\vec R}\psi_s(\vec r- \vec R) d^3r \right] = 0
\end{align*}$$
- Em que:
    - Da equação acima usamos $m=s$
    - O primeiro somatório representa a sobreposição das orbitais dos átomos vizinhos ao átomo em $\vec{R}=\vec{0}$. Se houver simetria translacional da rede, a sobreposição de todos os átomos vizinhos é *igual*.
    - A sobreposição com átomos 2ºs vizinhos será muito menor.

- Definimos:
$$\begin{align*}
\alpha(\vec{R})&= \int\psi_{s}^{*}(\vec{r})\psi_{s}(\vec{r}-\vec{R})d^{3}r\\
\gamma(\vec{R})&= -\int \psi_{s}^{*}(\vec{r})\Delta V\psi_{s}(\vec{r}- \vec{R})d^{3}r\\
\beta&= -\int |\psi_{s}(\vec{r})|^{2}\Delta V(\vec{r})d^{3}r
\end{align*}$$
ficando a equação na forma:
$$[E_{n,\vec{k}}-E_{s}]\left[1+\sum\limits_{\vec{R}\neq0} e^{i\vec{k}\cdot\vec{R}} \alpha(\vec{R})\right]+\beta + \sum\limits_{\vec{R}\neq0}e^{i\vec{k}\cdot\vec{R}}\gamma(\vec{R})=0$$
$$E_{n,\vec{k}}= E_{s}-\frac{\beta+\sum_{\vec{R}\neq0}e^{i\vec{k}\cdot\vec{R}}\gamma(\vec{R})}{1+\sum_{\vec{R}\neq0}e^{i\vec{k}\cdot\vec{R}}\alpha(\vec{R})}$$
- Em alguns casos podemos aproximar:
$$E_{n,\vec{k}}= E_{s}-\beta-\sum_{\vec{R}\neq0}e^{i\vec{k}\cdot\vec{R}}\gamma(\vec{R})$$
**Rede Cúbica Simples**
- Consideremos uma rede cúbica simples, com parâmetro de rede $a$. Para um átomo $\vec{R}=\vec{0}$ temos 12 vizinhos:
$$\vec{R}= \frac{a}{2}(\pm1,\pm1,0)~,~ \frac{a}{2}(\pm1,0,\pm1)~,~ \frac{a}{2}(0,\pm1,\pm1)$$
logo temos:
$$\vec{k}\cdot\vec{R}=\frac{a}{2}(\pm k_{i},\pm k_{j})~~~~;~~i,j=x,y:y,z:z,x$$
- Como nesta rede $\Delta V$ tem simetria de translação e $\psi_{s}$ depende apenas de $r$ temos o mesmo $\gamma(\vec{r})$ para toods os 12 pontos:
$$\gamma=-\int \psi_{s}^{*}(x,y,z)\Delta V(x,y,z)\psi_{s}\left(x-\frac12a,y-\frac12a,z\right)dxdydz$$
tendo-se:
$$\small E_{n,\vec{k}}=E_{s}-\beta-4\gamma\left[\cos\left(\frac12k_{x}a\right)\cos\left(\frac12k_{y}a\right)+\cos\left(\frac12k_{y}a\right)\cos\left(\frac12k_{z}a\right)+\cos\left(\frac12k_{z}a\right)\cos\left(\frac12k_{x}a\right)\right]$$
- No limite de $ka$ pequenos podemos escrever:
$$E_{n,\vec{k}}=E_{s}-\beta-12\gamma+\gamma k^{2}a^{2}$$
que apenas depende do módulo de $\vec{k}$, não da sua direção. Assim, temos superfícies de energia constante *esféricas* -- Orbitais S são esféricas.

**Massa Efetiva Eletrão**
- De alguma forma, a equação mais simplificada de $E_{n,\vec{k}}$ quando comprada com a energia de um eletrão livre resulta em:
$$|\gamma(a)|=\frac{\hbar^{2}}{2ma^{2}}$$
ora $\hbar,a$ são constantes. Assim, se $\Delta V$ aumentar (e portanto $\gamma$), temos que $m$ diminui!
- Assim neste modelo referimo-nos à *massa relativa do eletrão*:
$$m^{*}=\frac{\hbar^{2}}{2a^{2}} \frac{1}{|\gamma(a)|}$$
- Se houver menor sobreposição de niveis temos $\Delta V$ menor. Assim, temos $\gamma$ menor e $m^{*}$ maior. Isto faz sentido, porque vimos que com $\Delta V$ menor os eletrões têm menor velocidade e, portanto, **mais inércia**.

### P
- As orbitais P já não têm geometria esférica. Invés disso, temos *3* coeficientes $b_{m}$ não nulos. Assim:
$$\begin{align*}
\psi_{px}&= xf(r)=\psi_{1}(\vec{r})\\
\psi_{py}&= yf(r)=\psi_{2}(\vec{r})\\
\psi_{pz}&= zf(r)=\psi_{3}(\vec{r})
\end{align*}$$
- Agora os termos de overlap ficam mais complexos, agora dependem da orientação dos nodos da rede.

**Rede Cúbica Simples**
- Temos as relações de dispersão:
$$\begin{align*} E_1(\hbar \vec{k}) &= E_p - \beta + 2\gamma_1 \cos(k_x a) - 2 |\gamma_1| \left[ \cos(k_y a) + \cos(k_z a) \right] \\
E_2 (\hbar \vec{k}) &= E_p - \beta + 2\gamma_1 \cos(k_y a) - 2 |\gamma_1| \left[ \cos(k_x a) + \cos(k_z a) \right] \\
E_3 (\hbar \vec{k}) &= E_p - \beta + 2\gamma_1 \cos(k_z a) - 2 |\gamma_1| \left[ \cos(k_x a) + \cos(k_y a) \right] \end{align*}$$
($\gamma_{1}$ indica que se considerou os 1ºs vizinhos)
- As relações de dispersão são anisotrópicas.

**Massa Efetiva**
- A massa efetiva é definida por um tensor, tendo-se:
$$\frac{1}{m_{ij}^{*}}= \frac{1}{\hbar^{2}}\frac{\partial^{2}E(\vec{k})}{\partial k_{i}\partial k_{j}}$$
pode haver massa negativa. Aqui interpretamos os eletrões como lacunas.

## Funções de Wannier
- Vamos aprofundá-las

### Funções Bloch como combinação de Wannier
- Vimos que uma função de Bloch $\psi_{n,\vec{k}}(\vec{r})$ pode ser escrita como: $$\psi_{n,\vec{r}}(\vec{r})=\sum_{\vec{R}}e^{i\vec{k}\cdot\vec{R}}\phi(\vec{r}-\vec{R})$$
(combinação de funções de Wannier)
- Mas para definir isto notamos que $\psi_{n,\vec{k}}$ é periódica na rede recíproca.
- Assim, se expandirmos esta função em Fourier em ondas planas com vetores de onda na rede real (recíproca da recíproca) temos:
$$\psi_{n,\vec{k}}=\frac{1}{\sqrt{N}}\sum\limits_{\vec{R}} f_{n}(\vec{r},\vec{R})e^{i\vec{k}\cdot\vec{R}} \quad;\quad f_{n}(\vec{r},\vec{R})=\frac{1}{\sqrt{N}}\sum\limits_{\vec{k}\in PZB}e^{-i\vec{k}\cdot\vec{R}}\psi_{n,\vec{k}}(\vec{r})$$
- Se fizermos uma translação $+\vec{R'}$ de $\vec{r},\vec{R}$ temos que:
$$f_{n}(\vec{r}+\vec{R'},\vec{R}+\vec{R'})=f_{n}(\vec{r},\vec{R})$$
ou seja, $f_{n}$ apenas dependa da diferença entre $\vec{r}, \vec{R}$:
$$f_{n}(\vec{r},\vec{R})~~\to~~ \phi(\vec{r}-\vec{R})$$

### Base Completa de Funções Ortogonais
- Temos:
$$\langle \phi_{n}(\vec{r}-\vec{R}_{j})|\phi_{n'}(\vec{r}-\vec{R}_{i})\rangle=\delta_{\vec{R}_{i},\vec{R}_{j}}\delta_{n,n'}$$

### Funções que satisfazem Bloch na base Wannier
- Vimos então que as funções de Wannier permitem descrever uma base ortogonal alternativa para descrição de níveis eletrónicos.
- Temos:
$$\begin{align*}
\phi_{n}(\vec{r}-\vec{R})&= \frac{1}{\sqrt{N}}\sum\limits_{\vec{k}}e^{-i\vec{k}\cdot\vec{R}}\psi_{n,\vec{k}}(\vec{r})\\
&= \frac{1}{\sqrt{N}}\sum\limits_{\vec{k}}e^{-i\vec{k}\cdot\vec{R}}e^{i\vec{k}\cdot\vec{r}}u_{n,\vec{k}}(\vec{r})\\
&= \frac{1}{\sqrt{N}}\sum\limits_{\vec{k}}e^{i\vec{k}\cdot(\vec{r}-\vec{R})}u_{n,\vec{k}}(\vec{r})
\end{align*}$$
e podemos fazer o inverso:
$$u_{n,\vec{k}}(\vec{r})= \frac{1}{\sqrt{N}}\sum\limits_{\vec{k}}e^{-i\vec{k}\cdot(\vec{r}-\vec{R})}\phi_{n}(\vec{r}-\vec{R})$$

### Adaptação a Tight-Binding
- Como vimos acima, para as funções de Wannier serem úteis em Tight-Binding é preciso que sejam *bem localizadas*.
- Para isso, podemos escrever as funções de Wannier com uma diferença de fase para as de Bloch de modo que sejam bem localizadas:
$$\begin{align*}
\phi_{n}(\vec{r}-\vec{R})&= \sum\limits_{\vec{k}}e^{-i\vec{k}\cdot\vec{R}}\psi_{n,\vec{k}}(\vec{r})\\
&= \frac{1}{\sqrt{NV}}\sum\limits_{\vec{k}}e^{-i\vec{k}\cdot\vec{R}}e^{i\vec{k}\cdot\vec{r}}u_{n,\vec{k}}(\vec{r})\\
&= \frac{1}{N\sqrt{\text{V}_\text{cell}}} \sum\limits_{\vec{k}}e^{i\vec{k}\cdot(\vec{r}-\vec{R})}u_{n,\vec{k}}(\vec{r})\\
&= \Phi(\vec{r}-\vec{R})u_{n,\vec{k}}(\vec{r})
\end{align*}$$

### Hamiltoniano T-B
- Ao aplicar o Hamiltoniano à funções Wannier, vemos que elas *não* são funções próprias:
$$\int \phi_{n}^{*}(\vec{r}-\vec{R'})H \phi_{n}(\vec{r}-\vec{R'})d^{3}r=\frac{1}{N}\sum\limits_{\vec{k}}E_{n}(\vec{k})e^{i\vec{k}\cdot(\vec{r}-\vec{R})}=t_{n,\vec{r},\vec{R'}}$$
sendo isto um integral de salto/overlap.

- Tem-se que:
    - Para 2 funções de Wannier de nodos distintos (mesmo sendo ortogonais), o integral acima pode não ser nulo
    - Se as funções de Wannier forem bem localizadas temos o integral de salto $t_{n,\vec{R},\vec{R'}}$ reduzido e podemos desprezar 2ºs vizinhos.

### Hamiltonio T-B com Wannier 
- Sendo as funções Wannier representadas por $\ket{\vec{R}}$:
$$H = \sum\limits_{\vec{R},\vec{R'}}\ket{\vec{R'}}\bra{\vec{R'}}H\ket{\vec{R}}\bra{\vec{R}}$$
- Aqui temos:
$$\bra{\vec{R'}}H\ket{\vec{R}}=\int \phi_{n}^{*}(\vec{r}-\vec{R'})H\phi_{n}(\vec{r}-\vec{R})d^{3}r=\frac{1}{N}\sum\limits_{\vec{k}}E_{n}(\vec k)e^{i\vec{k}\cdot(\vec{R'}-\vec{R})}$$
- Definimos:
    - $H_{\vec{R},\vec{R}}$ - *Hooping Term*
    - $H_{\vec{R},\vec{R'}}$ - *On Site Energy*
$$H = \sum\limits_{\vec{R}}\ket{\vec{R}}H_{\vec{R},\vec{R}}\bra{\vec{R}} + \sum\limits_{\vec{R'}\neq\vec{R}}\ket{\vec{R'}}H_{\vec{R},\vec{R'}}\bra{\vec{R}}$$
- Podemos escreveas funções de onda $\psi_{n,\vec{k}}(\vec{r})$ como:
$$\ket{\vec{k}}=\frac{1}{\sqrt{N}}\sum\limits_{\vec{R}}e^{i\vec{k }\cdot\vec{R}}\ket{\vec{R}}$$
- E temos a relação de dispersão:
$$\begin{align*}
\bra{\vec{R}}H\ket{\vec{R}}&= E_{\vec{k}} \langle\vec{R}\ket{\vec{k}}\\
\frac{1}{\sqrt{N}}e^{i\vec{k}\cdot\vec{R}}E + \frac{t}{\sqrt{N}}\sum\limits_{\delta}e^{i\vec{k}\cdot(\vec{R}+\delta)}&= \frac{E_{\vec{k}}}{\sqrt{N}}e^{i\vec{k}\cdot\vec{R}}\\
E_{\vec{k}}&= E+t\sum\limits_{\delta}e^{i\vec{k}\cdot\vec{\delta}}
\end{align*}$$
