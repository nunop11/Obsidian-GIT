# Explicação de $R_{s},R_{z}$
O díodo de Zener usado é de 6.8V. Ou seja, quando uma corrente passa por ele ocorre uma queda de tensão de 6.8V: teremos $V_{z_{1}}=12-6.8=5.2\text{V}$. Assim, assumindo que o amplificador é ideal, teremos $V_{+}=V_{-}=V_{z_{1}}=V_{z_{2}}$.
Desta forma, a queda de tensão na resistência $R_{s}$ será também 6.8V. Desta forma, como queremos que a corrente $I_{s}$ que atravessa o transístor seja de $\sim1\text{mA}$ temos:
$$R_{s}I_{s}=6.8~~\to~~R_{s}\cdot10^{-3}=6.8~~\to~~ R_{s}=6800\Omega$$
Segundo a datasheet do díodo de Zener, a corrente que ele precisa para funcionar corretamente é $5\text{mA}$. Assim, temos:
$$V_{z_{1}}-R_{z}I_{z}=-12~~\to~~ R_{z}I_{z}=17.2~~\to~~ R_{z}\cdot 5\cdot10^{-3}=17.2~~\to~~R_{z}=3440\Omega$$

# Dedução $R(V)$ teórico - circuito 1
![[Pasted image 20240327171623.png|400]]
Como vimos acima, temos $I_{s}=10^{-3}\text{A},R_{z}=3300\Omega,R_{s}=6800\Omega$. Considerando que não há perda de corrente para a base do transístor nem queda de tensão nele. Teremos então: $V_{j}-R_{j}I_{s}=-12$ em que $V_{j}$ é a tensão no terminal "superior" da resistência. O voltimetro irá medir: $V=V_{j}-(-12)=R_{j}I_{s}$. Ou seja, temos $$V=10^{-3}R_{j}$$
Por exemplo, se medirmos $1V$ é porque temos uma resistência de $1\text{k}\Omega$. Por outras palavras, 1mV equivale a 1$\Omega$.

# Explicação de $V_{0}$
![[circuito_teorica_V0.png|400]]
Conforme a figura acima, temos um amplificador em configuração diferencial.
Consideremos o caso $V_{A}=0$. Teremos $V_{-}=V_{+}=0$. Haverá uma corrente $I$ a passar em $V_{B},V_{0}$ tal que: $V_{B}-R_{1}I=0=V_{0}-R_{2}I$. Destas equações podemos obter: $I=\frac{V_{B}}{R_{1}},V_{0}=-\frac{R_{2}}{R_{1}}V_{B}$.
Consideremos agora $V_{B}=0$. Teremos uma corrente $I$ tal que $V_{+}=V_{-}=V_{A}-R_{3}I$, sendo ainda que $V_{A}-R_{3}I-R_{4}I=0$. Por fim, temos que $V_{-}=V_{0}-R_{2}I$, sendo que $V_{0}-R_{2}I-R_{1}I=0$. Podemos então obter: $V_{0}= \frac{R_{1}+R_{2}}{R_{1}}\frac{R_{4}}{R_{3}+R_{4}}V_{A}$
Por fim, para o caso geral, basta somar estes termos:
$$V_{0}=\frac{R_{1}+R_{2}}{R_{1}}\frac{R_{4}}{R_{3}+R_{4}}V_{A}-\frac{R_{2}}{R_{1}}V_{B}$$
Ora, neste circuito temos $R_{1}=R_{3}=10\text{k}\Omega,R_{2}=R_{4}=100\text{k}\Omega$. Assim, ficamos apenas com:
$$V_{0}=10(V_{A}-V_{B})$$

# Dedução $R(V)$ teórico - circuito 2
![[Pasted image 20240327172643.png|450]]
Tal como atrás, mantemos $R_{z}=3300\Omega,R_{s}=6800\Omega$. Consideremos que não há perda de corrente no transístor, tal que $I_{A}=I_{s}=10^{-3}\text{A}$. Temos ainda $R_{1}=R_{3}=10\text{k}\Omega,R_{2}=R_{4}=100\text{k}\Omega$. Consideremos $i_{-}$ a corrente que passa em $B$ e no ramo do terminal inversor do amplificador e $i_{+}$ a corrente que passa em $A$, no terminal não-inversor e na terra. 
Imediatamente vemos que:
$$\begin{cases}
V_{B}=V_{A}-R_{j}(I_{s}+i_{+})\\
V_{A}=0-(R_{3}+R_{4})i_{+} \\
V_{B}=V_{0}-(R_{2}+R_{4})i_{-} \\
V_{B}=-12
\end{cases}$$
subtraindo a 3ª à 2ª equação:
$$\begin{align*}
V_{A}-V_{B}&= -V_{0}-(R_{3}+R_{4})i_{+}+(R_{2}+R_{4})i_{-}\\
\frac{11}{10}V_{0}&= 110\cdot10^{3}(i_{-}-i_{+})\\
\end{align*}$$
$$\begin{equation}
V_{0}= 10^{5}(i_{-}-i_{+})
\end{equation}$$
Temos ainda que $V_{B}=-12=V_{0}-i_{-}(R_{1}+R_{2})$ logo obtemos: $$i_{-}=\frac{V_{0}+12}{R_{1}+R_{2}}$$
Usando a equação (---- eq de V0 acima ----) e o facto que $R_{1}+R_{2}=1.1\cdot10^{5}\Omega$ podemos obter: $$i_{+}=\left(\frac{12}{1.1}- \frac{0.1V_{0}}{1.1}\right)\cdot10^{-5}$$
Por fim, temos:
$$\begin{align*}
V_{B}&= V_{A}-R_{j}(I_{s}+i_{+})\\
V_{0}&= 10R_{j}(I_{s}+i_{+})\\
R_{j}&= \frac{V_{0}}{10(I_{s}+i_{+})}
\end{align*}$$
$$\begin{equation}
R_{j}=\frac{V_{0}}{10I_{s}+\left(\frac{12}{1.1}- \frac{0.1V_{0}}{1.1}\right)10^{-4}}
\end{equation}$$
Teoricamente, esta equação permite-nos determinar $R_{j}$ conforme o valor de $V_{0}$ medido. Além disso, esta equação é aplicável para qualquer valor $R_{s}$, sendo que $I_{s}=6.8/R_{s}$.

## R max
Assumindo que a tensão máxima $V_{0}$ do circuito é $V_{cc}-1.5\text{V}=10.5\text{V}$, temos que a resistência máxima será dada por:
$$R_{j}^{max}=\frac{10.5}{10I_{s}+\left(\frac{12}{1.1}- \frac{0.1\cdot10.5}{1.1}\right)10^{-4}}=\frac{10.5}{10I_{s}+9.95\cdot10^{-4}}$$
Assim:
    - para $R_{s}=6800\Omega$ temos $I_{s}=1\text{mA}$ logo $R_{j}^{max}=955\Omega$ 
    - para $R_{s}=68\text{k}\Omega$ temos $I_{s}=0.1\text{mA}$ logo $R_{j}^{max}=5263\Omega$ 
    - para $R_{s}=680\text{k}\Omega$ temos $I_{s}=10\mu\text{A}$ logo $R_{j}^{max}=9589\Omega$ 
Isto foi verificado experimentalmente. Vemos ainda que, neste circuito, assumir que as correntes $i_{+},i_{-}$ são nulas é incorreto. Nas aulas práticas fizemos estas aproximações, tendo obtido resistências máximas de $1050\Omega,10.5\text{k}\Omega,105\text{k}\Omega$, o que está completamente errado.

## R min
Podemos inverter a relação obtida acima, tendo:
$$V_{0}=\frac{10I_{s}+0.001091R_{j}}{1+9\cdot10^{-6}R_{j}}$$
--- Não consigo deduzir isto :)

# Dedução $R(V)$ teórico - circuito Rf

![[circuito2_Rf.png|500]]

Como mostrado acima, acrescentamos uma resistência $R_{f}$, de modo a dividir a tensão e garantir que $V_{+}>-10.5\text{V}$ para o amplificador operar dentro da sua gama indicada. Colocamos $R_{s}=680\text{k}\Omega$, pelo que $I_{s}=10\mu\text{A}$.
Conforme a datasheet, para que o amplificador funcione temos que ter $V_{+}=V_{-}>-10.5\text{V}$. Para fazer uma estimativa do valor de resistência $R_{f}$ necessário, fizemos a aproximação $i_{+}=i_{-}=0$. Assim, temos $V_{+}=V_{A}=-12+I_{s}(R_{f}+R_{j})$ e facilmente obtemos que $R_{f}=\frac{V_{+}+12}{I_{s}}-R_{j}$. Assim, para $V_{+}=10.5\text{V}$ e $R_{j}=0\Omega$ vemos que a mínima resistência necessária para o circuito funcionar é $150\text{k}\Omega$. Tendo em conta as aproximações aqui tomadas e as resistências disponíveis no laboratório, colocamos $R_{f}=180\text{k}\Omega$.

Consideremos $I_{0}$ a corrente que vem do Emissor do Transístor, assumindo que não ocorre perda de corrente para a Base. Concentremo-nos na secção da direita do circuito. Além disso, consideremos $i_{-}$ a corrente que passa em $B$ e no ramo do terminal inversor do amplificador e $i_{+}$ a corrente que passa em $A$, no terminal não-inversor e na terra. 
zComo $I_{0}$ é da ordem de $10^{-5}\text{A}$ amperes e $R_{j},R_{f}$ são da ordem de $10^{5}\Omega$, será segundo assumir que a tensão não cai muito ao passar nestas resistências. Assim, teremos $V_{A},V_{B}<0$, pelo que a corrente $i_{+}$ se "move" da terra para $A$ e será seguro assumir que $i_{-}$ vai do amplificador para $B$. Assim teremos:
$$\begin{cases}
V_{A}=-110\cdot10^{3}i_{+} \\
V_{B}=V_{0}-110\cdot10^{3}i_{-} \\
I_{A}=I_{0}+i_{+} \\
I_{B}=I_{0}+i_{+}+i_{-}
\end{cases}$$
Assumindo que o amplificador é ideal, teremos $V_{-}=V_{+}$. Ora, podemos definir: $$\begin{cases}
V_{-}=V_{B}+10\cdot10^{3}i_{-} \\
V_{+}=V_{A}+10\cdot10^{3}i_{+}
\end{cases}$$
Assim, recuperando a equação $V_{0}=10(V_{A}-V_{B})$ podemos escrever:
$$\begin{align*}
V_{B}+10^{4}i_{-}&= V_{A}+10^{4}i_{+}\\
V_{B}-V_{A}&= 10^{4}(i_{+}-i_{-})\\
\frac{-1}{10}V_{0}&= 10^{4}(i_{+}-i_{-})\\
\end{align*}$$
$$\begin{equation}
V_{0}= 10^{5}(i_{-}-i_{+})
\end{equation}$$

Podemos ainda ver facilmente que que $V_{B}=-12+R_{f}I_{B}$. Usando as equações $V_{A}=-110\cdot10^{3}i_{+},I_{B}=I_{0}+i_{-}+i_{+}$ definidas acima, podemos obter:
$$\begin{align*}
V_{B}&= -12 + R_{f}(I_{0}+i_{-}+i_{+}) \\
V_{B}-V_{A}&= -12 + R_{f}(I_{0}+i_{-}+i_{+}) -V_{A}\\
\frac{-1}{10}V_{0}&= -12 + R_{f}(I_{0}+i_{-}+i_{+}) +110\cdot10^{3}i_{+}\\
\end{align*}$$
$$\begin{equation}
V_{0}= 120 - 10R_{f}(I_{0}+i_{-}+i_{+}) - 11\cdot10^{5}i_{+}
\end{equation}$$

E temos então as equações (1) e (2) que nos permitem determinar a relação $R(V)$ deste circuito. 
Se somarmos e subtrairmos as equações podemos obter:
$$\begin{align*}
(1)+(2):~~~~ V_{0}&= 60 - 5R_{f}(I_{0}+i_{-}+i_{+}) + 5\cdot10^{4}(i_{-}-12i_{+})\\
(2)-(1):~~~~ i_{-}&=  \frac{120-10R_{f}I_{0}- i_{+}(10^{4}+10R_{f})}{10^{5}+10R_{f}}
\end{align*}$$
E podemos substituir (4) em (3) e obtemos:
$$i_{+}= \frac{1}{(10^{6}+10R_{f})\frac{5\cdot10^{4}-5R_{f}}{10^{5}+10R_{f}}+6\cdot10^{5}+5R_{f}}\left[-5R_{f}I_{0} + (120-10R_{f}I_{0})\frac{5\cdot10^{4}-5R_{f}}{10^{5}+10R_{f}}+60 - V_{0}\right]$$

Por fim, temos a relação: $V_{B}=V_{A}-R_{j}(I_{0}+i_{+})$. Usando a equação de $i_{+}$ acima temos:
$$\begin{align*}
V_{B}&= V_{A}-R_{j}(I_{0}+i_{+})\\
V_{B}-V_{A}&= -R_{j}(I_{0}+i_{+})\\
V_{0}&= 10R_{j}(I_{0}+i_{+})\\
R_{j}&= \frac{V_{0}}{10(I_{0}+i_{+})}\\
\end{align*}$$
$$\begin{equation}
R_{j}= \frac{V_{0}}{10} \frac{(10^{6}+10R_{f})\frac{5\cdot10^{4}-5R_{f}}{10^{5}+10R_{f}}+6\cdot10^{5}+5R_{f}}{I_{0}\left((10^{6}+10R_{f})\frac{5\cdot10^{4}-5R_{f}}{10^{5}+10R_{f}}+6\cdot10^{5}+5R_{f} \right)-5R_{f}I_{0} + (120-10R_{f}I_{0})\frac{5\cdot10^{4}-5R_{f}}{10^{5}+10R_{f}}+60 - V_{0}}
\end{equation}$$
Finalmente, se substituirmos os valores $I_{0}=10^{-5}\text{A},R_{f}=180\text{k}\Omega$ obtemos:
$$R_{j}(V_{0})=\frac{\frac{470000}{19}V_{0}}{\frac{149}{19}-V_{0}}=\frac{470000V_{0}}{149-19V_{0}}$$

