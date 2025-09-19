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

#computacional #programacao #fourier
