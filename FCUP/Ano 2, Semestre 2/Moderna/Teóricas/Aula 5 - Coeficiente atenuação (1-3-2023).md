# 1 - Coeficiente de atenuação linear
- Atenuação de feixe de fotões
![[Fotão a colidir com parede.png|425]]

- Temos um feixe homogéneo ($N_{0}$ fotões com energia $E_{\gamma}$ cada) a incidir num alvo de espessura $L$ feito de um material homogéneo
- $\Large \mu$ - _coeficiente de atenuação linear_ - probabilidade de um fotão sofrer uma interação, por unidade de comprimento do meio

- O número de fotões que entram nalguma interação entre $x$ e $x+dx$ é igual $N(x)\mu ~dx$ . Assim, a variação do número de fotões entre $x$ e $x+dx$ é $= N(x)-N(x+dx)$. Ora, a variação no número deve-se a alguns dos fotões entrarem em interações (p/ex, fotão a colidir com o alvo).Temos 
$$\begin{align*}
N(x)-N(x+dx)&= N(x)\mu dx\\
\frac{N(x+dx)-N(x)}{dx}&= -N(x)\mu\\
\int \frac{dN(x)}{N(x)}&= -\mu\int dx\\
N(x)&= C e^{-\mu ~x}\\\\
N(x)&= N_{0}e^{-\mu ~x}
\end{align*}$$
- Assim, o número de fotões que percorrem toda a distância $L$ é: $N(L)=N_{0}e^{-\mu~L}$
- Desta forma, o número de eletrões que sofrem interações é: $N(0)-N(L)=N_{0}-N_{0}e^{-\mu~L}$

- Tem-se que $$\mu=\mu_{\textsf{ fotoelétrico}}+\mu_{\textsf{ compton}}+\mu_{\textsf{ PP}}+\mu_{\textsf{ PT}}+\dots$$
- De notar ainda que $\mu$ depende da energia do fotão e do meio atenuador.

# 2 - Secção eficaz de um processo
- Temos um feixe monoenergético (todos os fotões têm a mesma energia) incide na perpendicular num alvo muito fino de área $A$ em que há um orifício de área $\sigma$. A probabilidade de uma partícula atravessar o orifício é:
$$\textsf{Probabilidade}=\frac{\sigma}{A}$$

- Daqui a diante, $a$ - número de projeteis, $b$ - número de alvos, $v_{a}$ - velocidade das partículas $a$, $n_{a}$ - densidade das partículas $a$
- Temos $N_{b}=n_{b}Ad$ - Número de alvos 

- Iremos estudar o acontecimento: $a$ atravessar o alvo $b$
- Temos que
$$\begin{align*}
\frac{\textsf{\# de acontecimentos}}{1s}&= \frac{\textsf{\# de partículas}}{1s}\times N_{b} ~\times \textsf{Prob de 1 acontecimento}\\
\frac{\textsf{\# de acontecimentos}}{1s}&= \frac{\textsf{\# de partículas}}{1s}\times N_{b} ~\times \frac{\sigma}{A}\\
\frac{\textsf{\# de acontecimentos}}{1s} &= \Phi_{a}~N_{b}~\sigma
\end{align*}$$
Sendo $\Large \Phi_{a} = \frac{\textsf{\# de partículas}}{\textsf{tempo . área}}=v_{a}n_{a}$

- Temos então que a secção eficaz é 
$$\text{Secção Eficaz}=\frac{\textsf{\# de acontecimentos por unidade de tempo}}{\Phi_{a}~N_{b}}$$

#moderna #fisica