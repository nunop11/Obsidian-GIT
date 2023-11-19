> Muito sinceramente, acho que este resumo está pior do que o dos outros capítulos.
# 1 - Séries de Fourier
- Qualquer função periódica definida num intervalo $0\le x<L$ pode ser escrita como uma série de Fourier.
- Se a função for par/simétrica em relação ao ponto central do intervalo $x=\frac{1}{2}L$, usamos cosseno: $$f(x)=\sum\limits_{k=0}^{\infty} \alpha_{k}\cos  \left( \frac{2\pi kx}{L} \right)$$
em que $\alpha_{k}$ é um conjunto de constantes que definem a forma da equação.
- Se a função for ímpar/anti-simétrica (rotação 180º) em relação ao ponto médio, usamos seno:
$$f(x)=\sum\limits_{k=1}^{\infty} \beta_{k}\sin \left( \frac{2\pi kx}{L} \right)$$
- Assim, para uma forma que não apresenta qualquer simetria:
$$f(x)= \sum\limits_{k=0}^{\infty} \alpha_{k}\cos  \left( \frac{2\pi kx}{L} \right) + \sum\limits_{k=1}^{\infty} \beta_{k}\sin \left( \frac{2\pi kx}{L} \right)$$
- Podemos usar $\cos\theta=\frac{1}{2}(e^{-i\theta} + e^{i\theta})$, $\sin\theta=\frac{1}{2}(e^{-i\theta} - e^{i\theta})$ e temos:
$$f(x)=\frac{1}{2}\sum\limits_{k=0}^{\infty}\alpha_{k} \left[e^{-i \frac{2\pi kx}{L}} + e^{i \frac{2\pi kx}{L}} \right] + \frac{1}{2}\sum\limits_{k=0}^{\infty}\beta_{k} \left[e^{-i \frac{2\pi kx}{L}} - e^{i \frac{2\pi kx}{L}} \right]$$
e temos:
$$f(x)=\sum\limits_{k=-\infty}^{+\infty}\gamma_{k} e^{i \frac{2\pi}{L}kx} \quad \textsf{(Eq.0)} \quad;\quad \quad \gamma_{k} = \begin{cases} \frac{1}{2}(\alpha_{-k}+i\beta_{-k}) &; &k<0\\ \alpha_{0} &; &k=0\\ \frac{1}{2}(\alpha_{k}-i\beta_{k}) &; &k>0\end{cases}$$

![[forçar periodica.png]]
- Assim, apesar de estas séries se aplicarem a funções periódicas, podemos usá-las em funções não periódicas. Na prática, é como se considerassemos uma função que repete a função $f$ no intervalo muitas vezes, e iremos obter uma boa aproximação. No entanto, de notar que se usarmos a função obtida fora deste intervalo ela irá dar resultados errados.

- Os coeficientes $\gamma_{k}$, são normalmente complexos. Para os obter:
$$\int_{0}^{L} f(x)\exp\left( -i \frac{2\pi kx}{L}\right)dx = \sum\limits_{k'=-\infty}^{+\infty} \gamma_{k'} \int_{0}^{L}\exp \left( i \frac{2\pi(k'-k)x}{L} \right)dx \quad \quad \textsf{(Eq. 1)}$$
- Na integral da direita temos:
$$\begin{align*}
\int_{0}^{L}\exp \left( i \frac{2\pi(k'-k)x}{L} \right)dx &= \frac{L}{2i\pi(k'-k)}\left[ \exp \left(i \frac{2\pi (k'-k)x}{L} \right) \right]_{0}^{L}\\
&= \frac{L}{2i\pi (k'-k)} \left[ \cancelto{=1}{e^{i 2\pi(k'-k)}} - 1 \right]\\
&= 0
\end{align*}$$
(isto porque $e^{i2\pi n}=1, \forall n\in \mathbb{Z}$).

- No entanto, se $k'=k$ vemos que $\int_{0}^{L}\exp \left( i \frac{2\pi(k'-k)x}{L} \right)dx=\int_{0}^{L}dx=L$ . Assim, regressando à Eq.1:
$$\int_{0}^{L}f(x) e^{-i \frac{2\pi kx}{L}}dx=L\gamma_{k}$$
ou seja:
$$\gamma_{k}=\frac{1}{L} \int_{0}^{L}f(x)\exp \left(-i \frac{2\pi kx}{L} \right)dx$$
- Assim, podemos obter a função usando os coeficientes de Fourier (Eq.0) ou obter os coeficientes usando a função (Eq.1).

# 2 - Discrete Fourier Transform
$$\gamma_{k}=\frac{1}{L} \int_{0}^{L}f(x)\exp \left(-i \frac{2\pi kx}{L} \right)dx$$
- Por vezes, conseguimos usar a equação acima para determinar os coeficientes de forma analítica e exata. No entanto, há casos em que isso não é possível: $f$ pode ser muito complicada, ou pode não ser uma função de todo. Nesses casos temos que determinar $\gamma_{k}$ de forma numérica, usando os métodos que vimos.

- Com o método do trapézio com $N$ intervalos temos:
$$\gamma_{k}=\frac{1}{L} \frac{L}{N} \left[ \frac{1}{2}f(0) + \frac{1}{2} f(L) + \sum\limits_{n=1}^{N-1} f(x_{n})\exp\left(-i \frac{2\pi kx}{L}\right) \right] $$ em que distribuimos os sample points da forma $x_{n}=\frac{n}{N}L$
- No entanto, como $f$ será periódica, temos por definição $f(0)=f(L)$. Assim:
$$\gamma_{k}=\frac{1}{N} \sum\limits_{n=0}^{N-1} f(x_{n})\exp \left( -i \frac{2\pi kx}{L} \right)$$

- Ora, muitas vezes temos muitos samples (como "frames" de um certo aúdio que estamos a analisar), recolhidos em intervalos de tempo iguais. Isto é algo que já temos na equação acima, mas podemos simplificar mais. Definindo $y_{n}$ como sendo o sample recolhido temos:
$$\gamma_{k}= \frac{1}{N}\sum\limits_{n=0}^{N-1} y_{n}\exp \left( -i \frac{2\pi kn}{L} \right) \quad \quad \textsf{(Eq. 0)}$$
pelo que neste formato já nem precisamos de saber os $x$ dos samples nem o tamanho do intervalo. Precisamos apenas de saber quais e quantos são os samples.
- A equação 1 define a *Transformada Discreta de Fourier* aka **DFT**, que por convenção definimos assim:
$$c_{k}=\sum\limits_{n=0}^{N-1} y_{n} \exp \left( -i \frac{2\pi kn}{N} \right) \quad \quad \textsf{(Eq. 1)}$$
- Às constantes $c_{k}$ iremos chamar de *__Coeficientes de Fourier__* (apesar de os "verdadeiros" coeficientes de fourier serem os $\gamma_{k}$)
- Apesar de termos feito esta dedução usando o método do trapézio, os coeficientes que obtemos são *exatos*.

> **Explicação**
> - Para série geométrica temos: $$\sum\limits_{k=0}^{N-1} a^{k} = \frac{1-a^{N}}{1-a}$$
> - Ora, vamos substituir $a = e^{i2\pi m/N}$:
> $$\sum\limits_{k=0}^{N-1} e^{i2\pi km/N} = \frac{1-e^{i2\pi m}}{1-e^{i2\pi m/N}}=\frac{0}{1-1e^{m/N}}=0$$
> - A única exceção é quando $m= nN, n\in \mathbb{Z}$ ($m$ é 0 ou multiplo de $N$). Neste casos, vemos logo na operação original que ficamos com $\sum\limits_{k=0}^{N-1} e^{i2\pi km/N}=N$
> (Página 304 do pdf. Acabar depois talvez)

- Temos que a série de Fourier pode ser obtida da seguinte forma: $$y_{n}=\frac{1}{N} \sum\limits_{k=0}^{N-1} c_{k}\exp \left(i \frac{2\pi kn}{N} \right) \quad \quad \textsf{(Eq. 2)}$$
- Isto é o *DFT inverso*. Isto é o equivalente à equação $f(x)=\sum_{k=-\infty}^{+\infty}\gamma_{k} \exp\left(i \frac{2\pi kx}{L}\right)$, que vimos no início desta secção. Basicamente, tal como podemos obter $\gamma_{k}$ usando $f(x)$ e vice-versa, também podemos obter $c_{k}$ usando $y_n$ _e vice-versa_. De notar ainda que, ao usar $c_{n}$ para obter $y_{n}$ usando Eq. 2 iremos obter resultados *exatos*, à exceção de erros de arredondamento.
- Notemos ainda que, ao definir $c_{n}$ removemos um fator $1/N$ da formula de $\gamma_{k}$, mas agora na formula temos um fator $1/N$ a mais em relação à formula de $f(x)$.
- De notar que a Eq.2 é melhor para usar em programação porque apenas temos que iterar até $N-1$, não até $+\infty$.

- No entanto, o DFT tem um problema: apenas conhecemos os sample points. Não sabemos nada acerca da função entre estes pontos. Ou seja, tendo os mesmos sample points, podiamos ter qualquer um dos casos abaixo:
![[fourier-entre samples.png]]

- Ainda assim, desde que a função seja minimamente suave, o DFT é suficiente.

## 2.1 - DFT com f real
- Tudo o que vimos sobre DFT funciona muito bem tanto com funções reais como complexas. No entanto, na maioria dos casos, temos funções reais pelo que podemos fazer algumas simplificações.

- Consideremos que todos os $y_{n}$ são reais e que temos $c_{k}$ sendo $\frac{1}{2}N<k<N-1$. Assim, vamos escrever $k$ como $k=N-r$ sendo $1\leq r< \frac{1}{2}N$
- Assim:
$$\begin{align*}
c_{N-r} &=  \sum\limits_{n=0}^{N-1} y_{n}\exp \left( -i \frac{2\pi (N-r)n}{N} \right)=\sum\limits_{n=0}^{N-1} y_{n} \cancelto{=1}{\exp \left( -i2\pi n \right)} \exp \left( i \frac{2\pi r n}{N} \right) \\
&= \sum\limits_{n=0}^{N-1} y_{n} \exp \left( i \frac{2\pi rn}{N} \right) = c_{r}^{*}
\end{align*}$$
em que $c_{r}^{*}$ é o conjugado de $c_{r}$.
- Ou seja, por analogia com a demonstração acima: $c_{N-1}=c_{1}^{*}~,~ c_{N-2}=c_{2}^{*}\dots$
- Assim, facilmente vemos que apenas é preciso calcular os coeficientes $c_{k}$ para $0\le k\le \frac{1}{2}N$, porque a outra metade dos coeficientes irão ser apenas os conjugados. Assim: se $N$ for par temos que calcular $\frac{1}{2}N+1$; se for ímpar temos que calcular $\frac{1}{2}(N+1)$.
    - De notar que esta quantidade, para ambos os casos, pode ser escrita em python como `N // 2+1`

---
Exemplo de uma função que calcula o DFT:
![[dft codigo.png]]

## 2.2 - Posições dos sample points
- Ao calcular uma DFT, podemos "deslizar" todos os sample points um pouco para o lado e pouco muda.

- Consideremos que deslizamos os sample points uma distância $\Delta$:
$$x_{n}' = x_{n}+\Delta=\frac{n}{N}L +\Delta$$
- Temos então:
$$\begin{align*}
c_{k}&= \sum\limits_{n=0}^{N-1} f(x_{n}+\Delta)\exp \left(-i \frac{2\pi (x_{n}+\Delta)}{L} \right)\\
&= \exp \left(-i \frac{2\pi k \Delta}{L} \right) \sum\limits_{n=0}^{N-1} f(x_{n}') \exp \left( -i \frac{2\pi k x_{n}}{L} \right)\\
&= \exp\left( -i \frac{2\pi k \Delta}{L}\right)\sum\limits_{n=0}^{N-1} y_{n}' \exp \left( -i \frac{2\pi kn}{N} \right)
\end{align*}$$
- Assim, absorvemos o fator de fase (fator antes do sumatório), definindo $c_{k}' = \exp(i2\pi k\Delta/L) c_{k}$ e temos:
$$c_{k}'=\sum\limits_{n=0}^{N-1} y_{n}' \exp \left( -i \frac{2\pi kn}{N} \right)$$

- Ou seja, na realidade não importa onde colocamos os sample points para o DFT.
- Temos então 2 tipos de DFT:
![[dft tipo 2.png]]
sendo que no tipo 1 metemos os sample points nos pontos inteiros, pelo que não temos ponto no fim do intervalo. Assim, como meio termo, no tipo 2 temos sample points nos meios pontos.

# 3 - Transformadas de Fourier em 2D
- Consiste em fazer uma transformada de Fourier de uma função $f(x,y)$. Na prática, fazemos tranformada para *uma variável de cada vez*.

- Consideremos que temos uma grelha $M\times N$ de sample points.
- Começamos por fazer uma transformada para cada uma das $M$ colunas, tendo:
$$c_{ml}' = \sum\limits_{n=0}^{N-1} y_{mn} \exp \left(-i \frac{2\pi ln}{N} \right)$$
sendo que, na equação acima: estamos na coluna $m$, que tem $N$ coeficientes, um para cada valor $l$.

- A seguir pegamos no coeficiente $l$ de cada coluna $m$ e fazemos a sua transformada de Fourier tendo:
$$c_{kl}=\sum\limits_{m=0}^{M-1} c_{ml}' \exp \left( -i \frac{2\pi km}{M} \right)$$
- Ao juntar as 2 equações numa só temos:
$$c_{kl} = \sum\limits_{m=0}^{M-1}\sum\limits_{n=0}^{N-1} y_{mn} \exp \left[-i2\pi \left( \frac{km}{M} + \frac{ln}{N} \right) \right]$$
e, alternativamente:
$$y_{mn}= \frac{1}{MN} \sum\limits_{m=0}^{M-1}\sum\limits_{n=0}^{N-1} c_{kl} \exp \left[i2\pi \left( \frac{km}{M} + \frac{ln}{N} \right) \right]$$

- Novamente, se todos os $y_{mn}$ forem reais, podemos fazer aquilo de apenas determinar metade dos coeficientes para a parte de $N$, porque os restantes serão os conjugados.

# 4 - Significado Físico das Transformadas de Fourier
- Na realidade, a transformada de Fourier de uma certa função divide-a numa componente real e numa imaginária.
- Além disso, cada termo das somas que nos dão $f(x)$ representa uma onda. Ou seja, apenas estamos a somar várias ondas, em que cada uma tem um peso diferente (dado pelos coeficientes).
- Consideremos que se tem um conjunto de dados que representam um audio com frequência constante, mas com ruído. Se determinarmos os coeficientes, verificaremos que aquele com o maior módulo corresponde à frequência do sinal. Teremos muitos coeficientes com valores mais reduzidos e aparentemente aleatórios, que são causados pela existência de ruído.

# 5 - DCT
- Vamos ver como se pode fazer uma transformada de Fourier em que usamos cossenos em vez de exponenciais complexas.

- Como vimos no início de Fourier, podemos definir funções como séries de cossenos, mas é preciso que a função seja *simétrica* em relação ao centro do intervalo escolhido.
- Ora, tendo qualquer função, é possível torná-la simétrica num intervalo finito. Para isso, apenas temos que repetir e "mirror" porções da função repetidamente. Ou seja, podemos fazer algo deste género:
![[forcar periodica v2.png]]
- Então, a partir do momento que temos uma "função" simétrica, podemos fazer a otimização: $y_{0}=y_{N},y_{1}=y_{N-1},y_{2}=y_{N-2},\dots y_{n}=y_{N-n}$
- Assim, presumindo que $N$ é par:
$$\begin{align*}
c_{k}&= \sum\limits_{n=0}^{N-1} y_{n}\exp \left( -i \frac{2\pi kn}{N} \right)\\
&= \sum\limits_{n=0}^{\frac{1}{2}N} y_{n}\exp \left( -i \frac{2\pi kn}{N} \right) + \sum\limits_{n=\frac{1}{2}N+1}^{N-1} y_{n}\exp \left( -i \frac{2\pi kn}{N} \right)\\
&= \sum\limits_{n=0}^{\frac{1}{2}N} y_{n}\exp \left( -i \frac{2\pi kn}{N} \right) + \sum\limits_{n=\frac{1}{2}N+1}^{N-1} y_{N-n}\exp \left( i \frac{2\pi k(N-n)}{N} \right)
\end{align*}$$
sendo sincero, não tenho a certeza sobre porquê que fizemos esta mudança.
- Ora, como a função é simétrica temos $N-n=n$, logo:
$$\begin{align*}
c_{k} &= \sum\limits_{n=0}^{\frac{1}{2}N} y_{n}\exp \left( -i \frac{2\pi kn}{N} \right) + \sum\limits_{n=\frac{1}{2}N+1}^{\frac{1}{2}N-1} y_{n}\exp \left( i \frac{2\pi kn}{N} \right)\\
&= y_{0} + y_\frac{N}{2} \cos\left( \frac{2\pi \frac{N}{2}}{N}\right) + 2\sum\limits_{n=1}^{\frac{1}{2}N-1}y_{n}\cos \left( \frac{2\pi kn}{N} \right)
\end{align*}$$
em que usamos $\cos\theta=\frac{1}{2}\left( e^{-i\theta}+e^{i\theta}\right)$
- Daqui já vemos que todos os $c_{k}$ vão ser reais.
- A inversa pode ser deduzida assim:
![[dct deducao.png]]
e ficamos com 
$$y_{n} = \frac{1}{N} \left[ c_{0} + c_\frac{N}{2} \cos \left(\frac{2\pi n\left(\frac{N}{2}\right)}{N} \right) + 2\sum\limits_{k=1}^{\frac{1}{2}N-1} c_{k}\cos \left(\frac{2\pi kn}{N} \right)\right]$$
- Ao $c_{k}$ chamamos de DCT - *Discrete Cosine Transform* e ao $y_{n}$ de DCT inversa.

## 5.1 - DCT Tipo 2
- Novamente, temos um tipo 2 de DCT, que apenas consiste em deslizar os sample points para o meio dos intervalos, como vimos no DFT. Neste caso, isto significa que temos $y_{n}=y_{N-1-n}$, pelo que temos:
![[dct coeficientes deducao.png]]
- Tal como no DFT, absorvemos o fator de fase (fator antes da soma) e ficamos com $$a_{k}=2\sum\limits_{n=0}^{\frac{1}{2}N-1} y_{n} \cos \left( \frac{2\pi k(n+ \frac{1}{2})}{N} \right)$$
e ficamos com a DCT inversa:
$$y_{n}=\frac{1}{N} \left[ a_{0} + 2\sum\limits_{k=1}^{\frac{1}{2}N-1} a_{k}\cos \left( \frac{2\pi k(n + \frac{1}{2})}{N}\right) \right]$$

## 5.2 -  DFT vs DCT
- Ao "forçar" funções a ser periódicas, podemos muitas vezes criar descontinuidades, basta o primeiro e último termo do intervalo não serem iguais. Ora, com DFT pode causar problemas, mas não com DCT. Assim, *DCT é melhor para funções não periódicas*.

## 5.3 - Usos tecnológicos
- A base de funcionamento de ficheiros JPEG é uma DCT tipo 2 em 2D. Basicamente, é feita a DCT da imagem original. O ficheiro apenas guarda os coeficientes uteis (com maior intensidade, e descarta os mais reduzidos, como se fossem ruído) para gerar a imagem, que depois são usados pelo computador ao abrir a imagem.
- O facto que se descarta coeficientes pode causar a existência de ruído e defeitos na imagem.
- Em geral, DCT é usado em muitas coisas que envolvem *compressão*, quer seja vídeo ou MP3. MP3 ainda descarta as frequência inaudíveis a seres humanos.


# 6 - Fast Fourier Transform
- Na DFT, que vimos antes, temos $N$ somas que temos que executar para $\frac{1}{2}N-1$ termos (presumindo que temos a DFT de uma função real). Assim, temos que executar cerca de $\frac{1}{2}N^{2}$ operações.
- Num computador, o máximo de operações que conseguimos fazer num tempo razoável é $10^{9}$
- Se igualarmos $\frac{1}{2}N^{2}=10^{9}$ temos $N\approx 45000$, que é o número máximos de sample points que conseguimos processar num tempo razoável. Em muitos casos, isso são poucos.
- Ora, o FFT, descoberto por Gauss, permite fazer mais sample points de forma rápida.

- Consideremos $N=2^{m}$. 
- A seguir, vamos dividir a soma que nos dá $c_{k}$ no DFT em 2 partes
- A primeira será composta pelos termos pares. Assim, consideramos $n=2r,~~r=0,1,\dots,\frac{1}{2}N-1$. Temos :$$E_{k}=\sum\limits_{r=0}^{\frac{1}{2}N-1} y_{2r} \exp \left( -i \frac{2\pi k \cdot2r}{N} \right)= \sum\limits_{r=0}^{\frac{1}{2}N-1} y_{2r} \exp \left( -i \frac{2\pi kr}{\frac{1}{2}N}\right)$$
    - Ora, isto é apenas outra DFT, mas agora em função de $r$ e agora com $\frac{1}{2}N$ samples. No termo $E_{k}$ o $E$ vem de even.
- A segunda é composta pelos termos ímpares, pelo que fazemos $n=2r+1$ e temos: $$\begin{align*}
\sum\limits_{r=0}^{\frac{1}{2}N-1} y_{2r+1} \exp \left( -i \frac{2\pi k(2r+1)}{N} \right)&= e^{-i2\pi k/N} \sum\limits_{r=0}^{\frac{1}{2}N-1} y_{2r} \exp \left( -i \frac{2\pi kr}{\frac{1}{2}N} \right)\\
&= e^{-i2\pi k/N} O_{k}
\end{align*}$$
    - E vemos que o termos que substituimos por $O_{k}$ ($O$ vem de odd) continua a ser uma série de fourier com $\frac{1}{2}N$ sample points.

- Ou seja, o toatl dos coeficientes é $$c_{k}=E_{k} + e^{-i2\pi k/N} O_{k}$$
- Como vimos acima, $O_{k},E_{k}$ são DFTs de uma função $f$ mas com $\frac{1}{2}N$ sample points. Ou seja, usando estes DFTs e um fator $e^{-2\pi k/N}$ facilmente calculamos $c_{k}$.
- Para obter $E_{k},O_{k}$ precisamos de um intervalo 2 vezes menor. Sendo $N$ uma potencia de base 2, se formos dividindo $N$ por 2, eventualmente iremos ficar com $N=1$. Ora, essa será uma transformada de 1 sample point. Ora, aí temos: $$c_{0}=\sum\limits_{n=0}^{0}y_{n}e^{0}=y_{0}$$

- Ora, o FFT funciona ao contrário do que temos acima. Começamos com os pontos individuais, que consideramos como sendo transformadas de Fourier em si, depois juntamos em pares, depois em grupos de 4, etc. até termos 1 só tranformada que engloba o intervalo todo.


## 6.1 - Velocidade
- No primeiro nível temos $N$ samples, o que nos dá $N$ coeficientes. Depois juntamos pares e temos $\frac{1}{2}N$ transformadas com 2 coeficientes cada (total de $N$ coeficientes). Assim vemos que temos sempre $N$ coeficientes por nível.
- Ora, o número de sample que temos é $N$ e pode ser reduzido até 1 usando $m$ níveis, tais que $N=2^{m}\leftrightarrow m = \log_{2}N$.
- Sendo que temos $N$ coeficientes por nível, com o FFT temos que determinar $N\log_{2}N$ coeficientes. 
- Para comparação, tendo $10^{6}$ sample points. Se usarmos DFT temos que fazer $\frac{1}{2}N^{2}\approx10^{11}$ operações. Com FFT apenas fazemos $N\log_{2}N\approx 10^{7}$ operações.

## 6.2 - Fórmulas de FFT
- Como vimos acima, começamos com $m=0$ e 1 transformada com $N$ sample points. Em $m=1$ temos $N/2$ pontos que foramam 2 transformadas. Ou seja, no nível $m$ temos $2^{m}$ transformadas de $\frac{N}{2^{m}}$ pontos.
- Deste modo, podemos numerar os sample points do primeiro nível como: $0,2^{m},2^{m}\times2, 2^{m}\times3\dots$.. De uma forma geral: $2^{m}r,~~r=0\dots \frac{N}{2^{m}} - 1$. 
-- Não percebo a dedução da fórmula, mas temos num nível $j=0\dots 2^{m}-1$:
$$\begin{align*}
\sum\limits_{r=0}^{\frac{N}{2^{m}}-1} y_{2^{m}r+j} \exp \left( -i \frac{2\pi k (2^{m}r+j)}{N} \right) &= e^{-i \frac{2\pi}{N}kj} \sum\limits_{r=0}^{\frac{N}{2^{m}}-1} y_{2^{m}r+j} \exp \left( -i \frac{2\pi kr}{N/2^{m}} \right)\\
&= e^{-i \frac{2\pi}{N}kj} E_{k}^{(m,j)}
\end{align*}$$

- Pegando na equação $c_{k}=E_{k} + e^{-i2\pi k/N} O_{k}$ para este caso ficamos com:
$$E_{k}^{(m,j)}=E_{k}^{(m+1,j)} + e^{-i \frac{2\pi}{N} kj}E_{k}^{(m+1,j+2^{m})}$$
- Como vimos, precisamos de $\log_{2}N$ dividões para ir de 1 transformada para $N$. Ou seja, no FFT começamos no nível $m=\log_{2}N$ (em que temos $N$ transformadas de 1 ponto) e vamos recuando até ao nível $m=0$. Assim (sendo que começamos no nível $m+1$) usamos a equação de $E_{k}^{(m,j)}$ acima para todos os $j,k$ e ir assim recuando os $m$ até chegar a $m=0$.
- No nível $m=0$ temos $$E_{k}^{0,0} = \sum\limits_{r=0}^{N-1} y_{r} \exp \left( -i \frac{2\pi kr}{N} \right)=c_{k}$$
## 6.3 - Funções FFT 
- As mais comuns:
    - `np.fft.rfft` - faz FFT com valores reais
    - `np.fft.fft` - FFT com complexos. Menos útil em física
    - `np.fft.irfft` - pega nos coeficientes, faz inverse FFT e dá os sample points.

#computacional #programacao #fourier