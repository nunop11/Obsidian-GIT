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
