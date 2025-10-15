## Divisão longa para obter h(t)
- Partimos de: ....
    - (equacao discreta de modelo qq)
    - (passar a q^-n dos 2 lados)
    - (meter na forma $y=\frac{xxx}{yyy}e$) -- função transferência lol
    - (substituir $y=h, e=\delta$)
    - (fracao = h)

## Formas de fazer
### Diretamente à mão
![[divisao longa 1.png]]
- Esta forma é a mais normal. Quando começamos a ver um padrão a emergir é muito prático.
- Mas às vezes isto torna-se complicado e torna-se muito fácil fazer erros nos sinais e indices:
![[divisao longa 2.png]]

### Sistema
- Este método é cortesia do ChatGPT :)
- Quando estamos a fazer uma divisão longa, apenas estamos a transformar uma fração com 2 polinómios em 1 só polinómio, ou seja:
$$\frac{a_{0} + a_{1}x+a_{2}x^{2}+\dots}{b_{0}+b_{1}x+b_{2}x^{2}+\dots}=c_{0}+c_{1}x+c_{2}x^{2}+\dots$$
- É preciso que a igualdade se mantenha, então fazemos:
$$\begin{align*}
a_{0}+a_{1}x+a_{2}x^{2}+\dots&= (c_{0}+c_{1}x+c_{2}x^{2}+\dots)(b_{0}+b_{1}x+b_{2}x^{2}+\dots)\\
&= c_{0}b_{0}+c_{0}b_{1}x+c_{0}b_{2}x^{2} + c_{1}b_{0}x+c_{1}b_{1}x^{2}+c_{1}b_{2}x^{3}\\
&+c_{2}b_{0}x^{2}+c_{2}b_{1}x^{3}+c_{2}b_{2}x^{4}+\dots\\
&= c_{0}b_{0}+ (c_{0}b_{1} +c_{1}b_{0})x+(c_{0}b_{2}+c_{1}b_{1}+c_{2}b_{0})x^{2}\\
&+ (c_{2}b_{1}+\dots)x^{3}+(c_{2}b_{2}+\dots)x^{4}+\dots
\end{align*}$$
e temos que ter uma igualdade:
$$\begin{cases}
a_{0}=c_{0}b_{0} \\
a_{1}=c_{0}b_{1}+c_{1}b_{0} \\
a_{2}=c_{0}b_{2}+c_{1}b_{1}+c_{2}b_{0} \\
a_{3}=c_{2}b_{1}+c_{3}b_{0}+c_{0}b_{3}+c_{1}b_{2} \\
a_{4}=c_{2}b_{2}+c_{1}b_{3}+c_{3}b_{1}+c_{0}b_{4}+c_{4}b_{0}
\end{cases}$$
- E vamos resolvendo, sendo este sistema bem fácil:
$$\begin{cases}
c_{0}=\frac{a_{0}}{b_{0}} \\
- \\
- \\
- \\
-
\end{cases}=\begin{cases}
c_{0}=\frac{a_{0}}{b_{0}} \\
c_{1}=\frac{a_{1}}{b_{0}}-\frac{c_{0}b_{1}}{b_{0}} \\
- \\
- \\
- \\
\end{cases}=\begin{cases}
c_{0}=\frac{a_{0}}{b_{0}} \\
c_{1}=\frac{a_{1}}{b_{0}}-\frac{a_{0}b_{1}}{b_{0}^{2}} \\
c_{2}= \frac{a_{2}}{b_{0}}- \frac{c_{1}b_{1}}{b_{0}}- \frac{c_{0}b_{2}}{b_{0}} \\
- \\
- 
\end{cases}=(\cdots)$$
