# Domínio das Frequências
- Em vez de estudar um SLIT no domínio do tempo, podemos estudá-lo no domínio das frequências. Basicamente, consideramos que cada sinal de entrada e saída é uma função harmónica com frequência, amplitude e fase bem definidas.
- Novamente, a resposta do sistema é a soma das repostas dos componentes.

- Temos um sistema com um sinal de entrada $x(t)$ e um sinal de saída $y(t)$. Se existir uma *função própria do sistema*, $a(t)$, tal que (sendo $\lambda$ um valor próprio):
$$x(t)=a(t)\to y(t)=\lambda a(t)$$

## Exponencial Complexa
- Consideremos um slit $S$ com a função de entrada $x(t)=C e^{st}~~;~~s=\sigma+j\omega\in\mathbb{C}$
- Definimos o sinal de saída como $y(t)=S[x(t)]$
- Então temos $$S[x(t)]=\lambda x(t)$$
> Sendo $y(t)=S[C e^{st}]$. Assim: $$\begin{align*}
y(t+\tau)&= S[C e^{s(t+\tau)}]\\
&= e^{s\tau}\cdot S[C e^{st}]\\\\
&= e^{s\tau}y(t)
\end{align*}$$
> Ou seja, a fórmula acima vem de $\lambda=y(0)~~;~~\tau\to t$. Ou seja (não sei bem porquê) temos: $$S[e^{st}]=\lambda e^{st}=\lambda x(t)$$

- Ou seja, se tivermos isto, $x(t)$ é uma função própria. Ou seja, uma *exponencial complexa é função prória de qualquer slit*.

# Função Transferência
- Ou seja, vemos que $\lambda$ é uma constante complexa que depende de $s$ e descreve o sistema quando $x(t)$ é uma exponencial complexa. Assim, definimos a **_Função Transferência do Sistema_**: $$\lambda\to H(s)$$
- E podemos definir um slit como: $$e^{st}\to \boxed{SLIT} \to H(s)e^{st}$$

>__*EXEMPLO*__
>Temos o seguinte circuito:
>![[sistema RCL slit.png]]
>Em que temos $x_{h}(t)=x_{0}e^{\sigma_{0}t}\cos(\omega_{0}t+\varphi_{0})$. Podemos então definir esta função como um conjunto de exponenciais complexas: $$\begin{align*}
x_{h}(t)&= x_{0}e^{\sigma_{0}t}\cos(\omega_{0}t+\varphi_{0})=x_{0}e^{\sigma_{0}t} \frac{1}{2} \left[ e^{j(\omega_{0}t+\varphi_{0})}+ e^{-j(\omega_{0}t+\varphi_{0})} \right]\\\\
&= U_{1}e^{s_{1}t}+ U_{2}e^{s_{2}t} \quad;~~\tiny U_{1}=\frac{x_{0}}{2}e^{j\varphi_{0}}~~;~~ U_{2}=\frac{x_{0}}{2}e^{-j\varphi_{0}}~~;~~ s_{1}=\sigma_{0}+j\omega_{0}~~;~~s_{2}=\sigma_{0}-j\omega_{0}
\end{align*}$$
>Assim, a entrada é composta por 2 exponenciais complexas, sendo que cada uma origina um sinal de saída que é a mesma exponencial multiplicada por 1 constante.
>
>De Eletróncia temos que $$V_{R}=i_{h}R~~;~~ i_{C}=C \frac{dV_{c}}{dt}~~;~~ V_{L}=L \frac{di_{L}}{dt}~~;~~ V_{C}=V_{L}$$
>E, portanto, ao aplicar as leis de Kirchhoff: $$x_{h}(t) +LC \frac{d^{2}}{dt^{2}}x_{h}(t) = Ri_{h}(t)+L \frac{d}{dt}i_{h}(t)+LCR \frac{d^{2}}{dt^{2}}i_{h}(t)$$
>como todos os coeficientes são constante, verificamos que temos um SLIT.
>
>Assim, como $x(t)$ é uma exponencial complexa e temos um SLIT, então $x(t)$ é uma funçaõ própria do sistema tal que: $$x_{h}(t)=U_{1} e^{s_{1}t}+U_{2}e^{s_{2}t} ~~ \Longrightarrow ~~ i_{h}(t)=I_{1}e^{s_{1}t} + I_{2}e^{s_{2}t}$$(em que $i_{h}(t)$ representa a saída)
>
>Ora, a equação diferencial acima indica a relação entre o sinal de entrada e saída. Como cada sinal de entrada irá resultar num sinal de saída proporcional a este, temos: $$\begin{cases}
U_{1}e^{s_{1}t}+s_{1}^{2}LCU_{1} e^{s_{1}t}= RI_{1}e^{s_{1}t} +Ls_{1}I_{1}e^{s_{1}t}+LCRs_{1}^{2}I_{1}e^{s_{1}t}\\
U_{2}e^{s_{2}t}+s_{2}^{2}LCU_{2} e^{s_{2}t}=RI_{2}e^{s_{2}t} +Ls_{2}I_{2}e^{s_{2}t}+LCRs_{2}^{2}I_{2}e^{s_{2}t}
\end{cases}$$
> Vemos logo que as exponenciais complexas cortam nas 2 equações. Assim, conseguimos obter: $$I_{1}=U_{1}, \frac{1+s_{1}^{2}LC}{R+s_{1}L+s_{1}^{2}LCR} \quad ;\quad I_{2}=U_{2}, \frac{1+s_{2}^{2}LC}{R+s_{2}L+s_{2}^{2}LCR}$$
> em que $I_{1},I_{2}$ são as amplitudes das exponenciais que compõe o sinal de saída, sendo que são portanto os *autovalores das funções próprias*.

# Modelo da Impedância
- Quando temos circuitos elétricos lineares com resistencias, bobinas e condensadores temos o *modelo da impedância*:
$$V(s)=Z(s)I(s)$$
em que:
- **Resistência** - $Z(s)=R$
- **Condensador** - $Z(s)=\frac{1}{sC}$
- **Bobina** - $Z(s)=sL$

No caso de bobinas de condensadores não há perda significativa, pelo que apenas nos interessa a relação entre a impedância destes e a frequência e temos:
- **Condensador** - $Z(s)=\frac{1}{j\omega C}$
- **Bobina** - $Z(s)=j\omega L$

#sinais #fisica
