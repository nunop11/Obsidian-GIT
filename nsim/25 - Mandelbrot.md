- O conjunto de Mandelbrot é definido por:
$$z_{n+1}=z_{n}^{2}+c$$
sendo a famosa imagem a representação no espaço complexo dos valores de $c$ para os quais esta sequência está _limitada_.
- Ou seja, para obter a famosa imagem temos que determinar uma forma fácil de implementar computacionalmente para saber se a sequencia está _limitada_
- Consideremos $c=a+bi$ temos (isto foi obtido com **sympy**):
$$\begin{align*}
z_{0}&= c=a+bi\\
z_{1}&= z_{0}^{2}+c=c^{2}+z_{0}\\
z_{2}&= z_{1}^{2}+c=c^{4}+2c^{3}+z_{1}\\
z_{3}&= z_{2}^{2}+c=c^{8}+4c^{7}+6c^{6}+6c^{5}+4c^{4}+z_{2}\\
z_{4}&= z_{3}^{2}+c=c^{16}+8c^{15}+28c^{14}+60c^{13}+94c^{12}+116c^{11}+114c^{10}+94c^{9}+68c^{8}+40c^{7}+20c^{6}+8c^{5}+c^{4}+z_{3}\\
z_{5}&= c^{32}+16c^{31}+ 120c^{30}+568c^{29}+1932c^{28}+5096c^{27}+10948c^{26}+19788c^{25}+30782c^{24}+41944c^{23}+50788c^{22}+55308c^{21}+54746c^{20}+49700c^{19}+41658c^{18}+32398c^{17}+23460c^{16}+15856c^{15}+10040c^{14}+5976c^{13}+3340c^{12}+1744c^{11}+844c^{10}+376c^{9}+153c^{8}+60c^{7}+22c^{6}+6c^{5}+4c^{4} + z_{4}
\end{align*}$$

e podemos definir isto na forma: $z_{n}=P_{n}+z_{n-1}$, em que:
$$\begin{align*}\\
P_{0}&= 0\\
P_{1}&= c^{2}\\
P_{2}&= c^{4}+2c^{3}\\
P_{3}&= c^{8}+4c^{7}+6c^{6}+6c^{5}+4c^{4}\\
P_{4}&= c^{16}+8c^{15}+28c^{14}+60c^{13}+94c^{12}+116c^{11}+114c^{10}+94c^{9}+68c^{8}+40c^{7}+20c^{6}+8c^{5}+c^{4}\\
P_{5}&= c^{32}+16c^{31}+ 120c^{30}+568c^{29}+1932c^{28}+5096c^{27}+10948c^{26}+19788c^{25}+30782c^{24}+41944c^{23}+50788c^{22}+55308c^{21}+54746c^{20}+49700c^{19}+41658c^{18}+32398c^{17}+23460c^{16}+15856c^{15}+10040c^{14}+5976c^{13}+3340c^{12}+1744c^{11}+844c^{10}+376c^{9}+153c^{8}+60c^{7}+22c^{6}+6c^{5}+4c^{4}\\
\end{align*}$$

isto é mt giro mas é inútil :(

- Olhemos para isto doutra forma:
$$\begin{align*}
z_{0}&= c&&= a+bi\\
z_{1}&= c^{2}+c&&= (a^{2}-b^{2})+2abi
\end{align*}$$
ou seja:
$$a_{n+1}=a_{n}^{2}-b_{n}^{2}~~~~;~~~~ b_{n+1}=2a_{n}b_{n}$$
- Deste coeficientes, o mais fácil de prever é $b_{n}$, já que tem uma relação linear. Daqui vemos que, se $a_{n}b_{n}>\frac12$ então $b$ irá aumentar.

- Podemos escrever: 
$$\begin{align*}
b_{n+1}&= 2a_{n}\cdot 2a_{n-1}b_{n-1}=4a_{n}a_{n-1}b_{n-1}\cdot 2a_{n-2}b_{n-2}=\cdots=2^{n}b_{0}\prod_{n=0}^{n}a_{n}
\end{align*}$$