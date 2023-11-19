# 1 - Poço Não Infinito
- Neste caso temos:
$$V(x)=\begin{cases}0 &; &0\leq x\leq L  \\ V_{0} &; &x<0 ~~;~~x>L\end{cases}$$
- Devido à forma como o calculamos, no fundo do poço ($0\leq x\leq L$) a solução que temos é:
$$\Psi(x)=A\sin kx+B\cos kx$$
sendo que $A,B$ serão diferentes.
- A solução geral para as partes fora do poço, em que $V=V_{0}$, será $\Psi=C_{1}e^{kx}+C_{2}e^{kx}$. Assim:
$$\Psi(x<0)=Ce^{k'x}+De^{-k'x} \quad \quad;\quad \quad \Psi(x>L)=Fe^{k'x}+Ge^{-k'x}$$
mas temos $x=-\infty$ na primeira equação e $x=\infty$ na segunda. Assim, para não ter $\Psi=\infty$, temos que ter $D=F=0$ e assim:
$$\Psi(x<0)=Ce^{k'x} \quad \quad;\quad \quad \Psi(x>L)=Ge^{-k'x}$$
- Assim temos:
    - condições de continuidade de $\Psi$ em $x=0,~x=L$ (2 equações)
    - condições de continuidade de $\frac{d\Psi}{dx}$ em $x=0,~x=L$ (2 equações)
    - condição de normalização (1 equação)
- Ou seja, temos 5 equações para determinar as constantes. Isto é possível e direto, mas muito trabalhoso. 
- Ora, não é possível determinar uma fórmula direta que nos dê a energia, como no poço infinito.
- Além disso, como temos um potêncial máximo possível, temos *níveis de energia limitados*. 
![[poço nao finito energia.png]]
