# Eletro 1 - Aula teórica 5 (JAM)
- Como já vimos, se tivermos uma carga $q$, de posição $\vec r$, num sistema com $N+1$ cargas, a força nele aplicada é de
 $$\vec F=\frac{1}{4\pi\varepsilon_0}\sum_{j=1}^N\frac{q_j\cdot q}{|\vec r-\vec r_j|^3}(\vec r-\vec r_j)$$
- Podemos ver que o mesmo acontece com massas num campo gravítico. No entanto, se a massa desaparecer ($m\to0$), a força deixa de existir, mas o **campo** não. Se outra massa igual fosse colocada nesse mesmo ponto ela iria experienciar exatamente a mesma força.
- Assim, relacionando o campo gravítico ao elétrico,
$$\vec E(\vec r)=\lim_{q\to0^+}\biggr(\frac{\vec F}{q}\biggr)=\frac{1}{4\pi\varepsilon_0}\sum_{i\neq1}^N\frac{q_i}{|\vec r-\vec r_i|^3}(\vec r-\vec r_i)$$
- Temos então que:
$$\vec F=q\cdot\vec E(\vec r)$$

### Caso prático
- Na aula foi estudado o caso de ter 2 cargas iguais assim:
![[2 cargas campo]]
- Primeiro, considera-se que o ponto pode estar em qualquer ponto do espaço $x0z$. Temos isto:
![[campo fora eixos]]
- E assim,
$$\Huge\vec E(\vec r)=\begin{cases}
E_x(x,0,z)=\frac{q}{4\pi\varepsilon_0}\biggr[\frac{x}{[x^2+(z-d)^2]^{3/2}}+\frac{x}{[x^2+(z+d)^2]^{3/2}} \biggr]\\
E_z(x,0,z)=\frac{q}{4\pi\varepsilon_0}\bigg[\frac{z-d}{[x^2+(z-d)^2]^{3/2}}+\frac{z+d}{[x^2+(z+d)^2]^{3/2}} \biggr]
\end{cases}$$
- Desta forma, podemos estudar alguns casos:
1. Z = 0
- Assim, $E_z(x,0,0)=0$.
- Temos então que:
![[campo eixo x]]
- Podemos ver que, por geometria, os campos criados pelas duas cargas se anulam nas componentes em $z$.
- Assim, para um ponto num eixo perpendicular ao das duas cargas, o vetor Campo tem apenas direção nesse eixo. 
- A partir da função por ramos acima, facilmente se calcula que: 
$$\vec E(x,0,0)=\frac{2qx}{4\pi\varepsilon_0}\biggr[\frac{1}{(x^2+d^2)^{3/2}}\biggr]\hat x$$
- De notar:
    - Se o sinal da carga colocada for igual ao das cargas $q$, então uma carga no eixo dos x irá ser repelida para longe
    - Se o sinal for diferente, então a carga será atraída em direlção à origem e inicia um movimento oscilatório

2. X = 0
- Assim, temos que $E_x(0,0,z)=0$
- A partir da função por ramos, temos que
$$\vec E(0,0,z)=\frac{q}{4\pi\varepsilon_0}\biggr[\frac{z-d}{((z-d)^2)^{3/2}}+\frac{z+d}{((z+d)^2)^{3/2}}\biggr]$$
2.1. $z\approx0$, ou seja, $|z|\ll2d$ (e continua-se a ter x=0)
- Temos que $[(z-d)^2]^{3/2}\approx (d^2)^{3/2}\approx d^3$, então $\vec E=\frac{q}{4\pi\varepsilon_0}[\frac{z-d}{d^3}+\frac{z+d}{d^3}]$
- Deste modo,
$$\vec E(0,0,z\ll2d)=\frac{2q}{4\pi\varepsilon_0d^3}z\cdot \hat z$$
- Ou seja, o campo é linear a $z$.
- Podemos agora aplicar coisas de mecânia. Pela 2ª Lei de Newton, temos que $F=ma$, e para uma carga $q$, num campo elétrico criado por uma carga total $Q$, temos que $F=\frac{2qQ}{4\pi\varepsilon_0d^3}z$
- Podemos ainda ver que, se $z\approx0$, então temos um ponto entre as duas cargas. Deste modo, se imaginarmos a forma como o campo varia com a posição de uma carga neste zona, podemos ver que esta realizaria um movimento harmónico.
- Assim, como $F=-kz$, temos que $k=\frac{-2qQ}{4\pi\varepsilon_0d^3}$. E assim, temos que $\omega=\sqrt{k/m}$, então:
$$\large\omega^2=\frac{-2qQ}{4\pi\varepsilon_0md^3}$$, de notar que $\omega$ pode ser descrito como a frequência de oscilação, porque tem dimensões $T^{-1}$
- Vemos ainda que, se a carga tiver um sinal diferente das cargas $q$, então ela irá ser atraída para uma delas e não ocorre movimento oscilatório. O caso acima só se aplica se o sinal das cargas for igual.

#campoE #fisica 