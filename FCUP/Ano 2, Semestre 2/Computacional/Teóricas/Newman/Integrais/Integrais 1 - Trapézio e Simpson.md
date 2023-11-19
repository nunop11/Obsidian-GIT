# Integrais
- Antes de mais, temos que:
$$\int_{a}^{b} f(x) \,dx = \lim_{M\to\infty} \sum_{n=0}^{M-1} f(a + n \frac{b-a}{M})\frac{b-a}{M} = F(b) - F(a)$$
sendo $F$ uma primitiva de $f$.
- Temos uma função $f$ que queremos integrar de $a$ a $b$. Assim:
$$I(a,b)=\int_{a}^{b}f(x)dx$$

## 1 - Regra do Retângulo
- Ora, esta é a área da curva por baixo de $f$.
![[integral retangulos.png]]
- Uma forma comum de calcular isto com computador é dividir a área em muitos retângulos como se pode ver acima. Mas isto não é a melhor aproximação.

## 2 - Regra do Trapézio
![[integral trapezio.png]]
- Dividimos o intervalo $[a,b]$ em $N$ fatias.
- Cada trapézio terá
    - Espessura $\Large h = \frac{b-a}{N}$
    - A parede da direita do trapézio $k$ está na abcissa $x=\Large a+kh$
    - A parede da esquerda do trapézio $k$ está na abcissa $x=a+kh-h=\Large a+(k-1)h$
    - A área do trapézio $k$ será então: $$A_{k}=\frac{1}{2}h [f(a+(k-1)h) + f(a+kh)]$$
> De recordar que a área de um trapézio de altura $h$ e lados paralelo $a, b$ é $$A = \frac{a+b}{2}h$$

- Obtemos então a integral ao somar estas $N$ áreas:
>$$I(a,b)\approx \sum\limits_{k=1}^{N} A_{k}=h \left[ \frac{1}{2}f(a)+ \frac{1}{2}f(b) + \sum\limits_{k=1}^{N-1}f(a+kh)\right] $$
- Maiores valores de $N$ irão dar erros menores.

## 3 - Regra de Simpson
- A regra do trapézio é simples e fácil, mas para ser precisa é necessário fazer muitas iterações. Assim, às vezes não é eficiente o suficiente. Assim, usamos outros métodos, tal como a regra de simpson.
![[integral simpson.png]]
- Este método consiste em encaixar quadráticas. Para definir uma quadrática precisamos de 3 pontos. Assim, pegamos em 2 trapézios seguidos e usamos os 3 pontos que os definem para encaixar uma quadrática. Ao calcular a área sob estas quadráticas obtemos a integral.

- Peguemos no exemplo da imagem acima. Na quadrática 1 temos 3 pontos, que podemos definir como tendo $x=0, x=-h, x=h$. Temos
$$\begin{cases}
f(0)=C \\
f(h)=Ah^{2}+Bh+C \\
f(-h)=Ah^{2}-Bh+C
\end{cases}$$
Ao resolver o sistema temos:
$$\begin{align*}
A&= \frac{1}{h^{2}} \left[\frac{1}{2}f(-h) - f(0) + \frac{1}{2}f(h) \right]\\
B&= \frac{1}{2h}[f(h)-f(-h)]\\
C&= f(0)
\end{align*}$$
A área da por debaixo da quadrática 1 será então:
>$$\int_{-h}^{h}(Ax^{2}+Bx+C)dx=\frac{2}{3}Ah^{3}+2Ch=\frac{1}{3}h[f(-h)+4f(0)+f(h)]$$

- Na prática, para aplicar esta regra, dividimos a função em muitas quadráticas e somamos a área sob cada uma para obter a área total AKA integral.

- Assim, tendo a integral entre $x=a,~x=b$, tem-se que a primeira quadrática é definida por ponto de abcissa: $x=a ~;~ x=a+h ~;~ x=a+2h$. A segunda quadrática será definida pelos em $x=a+2h ~;~ x=a+3h ~;~ x=a+4h$
- Temos então a integral completa:
$$\begin{align*}
I(a,b)&\approx \frac{1}{3}h[f(a)+4f(a+h)+f(a+2h)] + \\
&+ \frac{1}{3}h[f(a+2h)+4f(a+3h)+f(a+4h)] + \dots\\
&+ \frac{1}{3}h[f(a+(N-2)h)+4f(a+(N-1)h)+f(b)]\\
&= \frac{1}{3}h[f(a)+4f(a+h)+2f(a+2h)+4f(a+3h)+\dots+f(b)]\\
&= \frac{1}{3} h\left[f(a)+f(b) + 4\sum\limits_{\substack{\text{k ímpar}\\ 1~\dots ~N-1}}f(a+kh) + 2\sum\limits_{\substack{\text{k par}\\ 2~\dots ~N-2}}f(a+kh)\right]
\end{align*}$$
- De recordar que, em python, podemos fazer, por exemplo, a soma dos ímpares assim: `for k in range(1,N,2):`
- Ou podemos fazer tudo com um só loop e temos:
$$I(a,b)\approx \frac{1}{3}h \left[f(a)+f(b) +4\sum\limits_{k=1}^{\frac{N}{2}} f(a+(2k-1)h) + 2\sum\limits_{k=1}^{\frac{N}{2}-1}f(a+2kh) \right]$$

#computacional #programacao #integrais 
