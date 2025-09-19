# V0 eq teorica
Consideremos agora $V_{B}=0$. Teremos novamente uma corrente $I$ tal que $V_{+}=V_{-}=V_{A}-R_{3}I$, sendo ainda que $V_{A}-R_{3}I-R_{4}I=0$. Por fim, temos que $V_{-}=V_{0}-R_{2}I$, sendo que $V_{0}-R_{2}I-R_{1}I$. Podemos então obter:
$$\begin{align*}
V_{-}=V_{A}-R_{3}I\\
V_{A}-R_{3}I-R_{4}I=0\\
V_{-}=V_{0}-R_{2}I\\
V_{0}-R_{2}I-R_{1}I=0
\end{align*}$$
obtemos
$$\begin{align*}
I &= \frac{1}{R_{3}+R_{4}}V_{A}=\frac{1}{R_{2}+R_{1}}V_{0}
\end{align*}$$
logo
$$\begin{align*}
V_{A}-\frac{R_{3}}{R_{3}+R_{4}}V_{A}&= V_{0}-\frac{R_{2}}{R_{1}+R_{2}}V_{0}\\
\frac{R_{4}}{R_{3}+R_{4}}V_{A}&= \frac{R_{1}}{R_{1}+R_{2}}V_{0}\\
V_{0}&= \frac{R_{1}+R_{2}}{R_{1}}\frac{R_{4}}{R_{3}+R_{4}}V_{A}
\end{align*}$$



# i-
$$\begin{align*}
0&= 120- 10R_{f}(I_{0}+i_{-}+i_{+}) - 11\cdot10^{5}i_{+}-10^{5}i_{-}+10^{5}i_{+}\\
0&= 120 - 10R_{f}I_{0}-i_{+}(10\cdot10^{5}+10R_{f}) - i_{-}(10^{5}+10R_{f}) \\
120-10R_{f}I_{0}&=  i_{+}(10\cdot10^{5}+10R_{f}) + i_{-}(10^{5}+10R_{f})\\
i_{-}&= \frac{120-10R_{f}I_{0}- i_{+}(10^{6}+10R_{f})}{10^{5}+10R_{f}}
\end{align*}$$
# i+(V0)
$$\begin{align*}
V_{0}&= 60 - 5R_{f}(I_{0}+i_{-}+i_{+}) + 5\cdot10^{4}(i_{-}-12i_{+})\\
&= 60 -5R_{f}I_{0} +i_{-}(5\cdot10^{4}-5R_{f}) - i_{+}(6\cdot10^{5}+5R_{f})\\
&= 60 -5R_{f}I_{0} + \frac{120-10R_{f}I_{0}- i_{+}(10^{4}+10R_{f})}{10^{5}+10R_{f}} (5\cdot10^{4}-5R_{f}) - i_{+}(6\cdot10^{5}+5R_{f})\\
&= 60 -5R_{f}I_{0} + (120-10R_{f}I_{0})\frac{5\cdot10^{4}-5R_{f}}{10^{5}+10R_{f}} - i_{+} (10^{4}+10R_{f})\frac{5\cdot10^{4}-5R_{f}}{10^{5}+10R_{f}} - i_{+}(6\cdot10^{5}+5R_{f})\\
&= 60 -5R_{f}I_{0} + (120-10R_{f}I_{0})\frac{5\cdot10^{4}-5R_{f}}{10^{5}+10R_{f}} - i_{+}\left( (10^{4}+10R_{f})\frac{5\cdot10^{4}-5R_{f}}{10^{5}+10R_{f}}+6\cdot10^{5}+5R_{f}\right)\\\\
i_{+}&= \frac{-5R_{f}I_{0} + (120-10R_{f}I_{0})\frac{5\cdot10^{4}-5R_{f}}{10^{5}+10R_{f}}+60}{(10^{4}+10R_{f})\frac{5\cdot10^{4}-5R_{f}}{10^{5}+10R_{f}}+6\cdot10^{5}+5R_{f}} - \frac{V_{0}}{(10^{4}+10R_{f})\frac{5\cdot10^{4}-5R_{f}}{10^{5}+10R_{f}}+6\cdot10^{5}+5R_{f}}
\end{align*}$$