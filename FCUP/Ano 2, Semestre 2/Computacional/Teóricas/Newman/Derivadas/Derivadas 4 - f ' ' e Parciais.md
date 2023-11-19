# 4 - Segundas Derivadas
- Por definição, é aquilo que obtemos ao aplicar a derivada à derivada. Assim, começamos por obter a derivada em 2 pontos $x\pm \frac{h}{2}$:
$$f'(x+ \frac{h}{2})\approx \frac{f(x+h)-f(x)}{h} \quad \quad;\quad \quad f'(x- \frac{h}{2})\approx \frac{f(x)-f(x-h)}{h}$$(nestas 2 equações obtemos a derivada de cada ponto a usar o método da derivada ao centro, ou seja, os pontos no denominador são $(x+ \frac{h}{2}) \pm \frac{h}{2}$.

- Usamos então mais uma vez o método da derivada ao centro, agora usando os 2 pontos acima para obter $f''(x)$:
$$\begin{align*}
f''(x) &\approx \frac{f'(x+ \frac{h}{2})-f'(x- \frac{h}{2})}{h}\\
&= \frac{\frac{f(x+h)-f(x)}{h}-\frac{f(x)-f(x-h)}{h}}{h}\\
&= \frac{f(x+h)-2f(x)+f(x-h)}{h^{2}}
\end{align*}$$
- Isto é a aproximação mais simples da segunda derivada, que iremos usar ao resolver equações diferenciais.

## 4.1 - Erros
- Novamente, começamos com expansões em série de Taylor:
$$\begin{align*}
f(x+h)=f(x)+ hf'(x) + \frac{1}{2}h^{2}f''(x) + \frac{1}{6}h^{3}f'''(x) + \frac{1}{24}h^{4}f^{(4)}(x)+\dots\\
f(x-h)=f(x)- hf'(x) + \frac{1}{2}h^{2}f''(x) - \frac{1}{6}h^{3}f'''(x) + \frac{1}{24}h^{4}f^{(4)}(x)+\dots
\end{align*} $$
- Ao somar as 2 equações e isolar $f''(x)$ temos:
$$f''(x)=\frac{f(x+h)-2f(x)+f(x-h)}{h^{2}} - \frac{1}{12}h^{2}f^{(4)}(x)+\dots$$

- Ora, daqui temos o erro de aproximação: $$\epsilon_\textsf{aprox}=\frac{1}{12} h^{2} |f^{(4)}(x)|$$
- Temos ainda o erro de arredondamento. Tal como já vimos, ao determinar um certo $f(x)$ temos um erro de arredondamento de $C|f(x)|$. Assim, ao calcular $f''(x)$ com a fórmula acima, o erro de arredondamento máximo que temos é $\frac{4C|f(x)|}{h^{2}}$. 
- Assim, o erro total é:
$$\epsilon(h)= \frac{4C|f(x)|}{h^{2}} + \frac{1}{12} h^{2} |f^{(4)}(x)|$$

- Ao fazer $\frac{d\epsilon}{dh}=0$ obtemos o $h$ que nos dá o erro mínimo:
$$h_{min}= \sqrt[4]{48C \left|\frac{f(x)}{f^{(4)}(x)} \right|}$$
que, ao substituir na fórmula de $\epsilon(h)$ nos dá o _erro mínimo_:
$$\epsilon_{min}= \sqrt{\frac{4}{3} C |f(x)f^{(4)}(x)|}$$
- Ou seja, as segunda derivadas que obtemos são tão precisas como as derivadas obtidas com aproximação à frente ou atrás.
- Tal como com derivadas normais, podemos fazer aproximações polinomiais mas no Newman não se fala.

# 5 - Derivadas Parciais
- Basicamente, só aplicamos o método de derivadas ao centro:
$$\begin{align*}
\frac{\partial f}{\partial x}(x) &= \frac{f\left(x+ \frac{h}{2}, y\right)- f\left(x- \frac{h}{2}, y\right)}{h}\\
\frac{\partial f}{\partial y}(y) &= \frac{f\left(x, y+ \frac{h}{2}\right)- f\left(x, y- \frac{h}{2}\right)}{h}
\end{align*}$$
- Usando o método de dedução que usamos na 2ª derivada, temos:
$$\small\frac{\partial^{2}f}{\partial x \partial y}(x,y) = \frac{f\left(x+ \frac{h}{2}, y+ \frac{h}{2}\right)- f\left(x- \frac{h}{2}, y+ \frac{h}{2}\right) - f\left(x+ \frac{h}{2}, y- \frac{h}{2}\right) + f\left(x- \frac{h}{2}, y- \frac{h}{2}\right)}{h^{2}}$$

#computacional #programacao #derivada #derivada_parcial 