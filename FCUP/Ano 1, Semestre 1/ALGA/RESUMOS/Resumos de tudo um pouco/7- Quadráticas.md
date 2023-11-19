# Forma Quadrática
- Dado um polinómio p(x,y) de grau 2 em duas variáveis, sem termosd e grau 1 ou 0:
$$p(x,y)=a_1x^2+a_2y^2+a_3xy$$
qual é a geometria do conjunto $\{(x,y):p(x,y)=1\}$?

- Uma forma quadrática de q em x e y é um plinómio p(x,y) em duas varáveis que só tem termos de grau 2:
$$q(x,y)=ax^2+bxy+cy^2$$
q(x,y) é um *polinómio homogéneo* de grau 2.

- Uma forma quadrática em x e y pode ser representada pelo produto por uma matriz simétrica A:
$$q(X)=X\cdot A\cdot X^T~~~~,X=(x,y)~~~~,A=\begin{pmatrix}a & b/2 \\ b/2 & c\end{pmatrix}$$
- Para melhor compreensão, pode-se escrever a fórmula acima assim:
$$q(x,y)=(x ~~ y)\cdot A \cdot \begin{pmatrix}x\\ y\end{pmatrix}$$
- Para uma forma quadrática q(x,y) e $\alpha \in R$ temos 
$$q(\alpha(x,y))=\alpha^2 q(x,y)$$
(Isto obtem-se ao esttudar o conjunto $\{(x,y):q(x,y)=\beta\}, \beta=\pm 1$)
- As formas quadráticas podem ser representadas por matrizes, sempre **simétricas**
- Vejamos uns exemplos:

1- equação de elipse
$$q(x,y)=\frac{x^2}{a^2}+\frac{y^2}{b^2} ~~~~~~~~ A=\begin{pmatrix}\frac{1}{a^2} & 0 \\ 0 & \frac{1}{b^2}\end{pmatrix}$$

2- equação de hipérbole
$$q(x,y)=\frac{x^2}{a^2}-\frac{y^2}{b^2} ~~~~~~~~ A=\begin{pmatrix}\frac{1}{a^2} & 0 \\ 0 & -\frac{1}{b^2}\end{pmatrix}$$

### Mudança de coordenadas
- Tendo $X(x_1,x_2)$ com as novas coordenadas $Y(y_1,y_2)$.
- A matriz de mudança de coordenadas, P, é dada por
$$X=Y\cdot P \leftrightarrow X^T=P^T \cdot Y^T$$
- Ora, se tivermos uma equação de uma quadrática com coordenadas em X, para obter a sua equação nas coordenadas Y, temos de fazer isto:
$$q(X)=X\cdot A\cdot X^T=Y\cdot P\cdot A\cdot P^T\cdot Y^T=\tilde q(x,y)$$
- Assim, a matriz de $q(Y)$ é $B=P\cdot A\cdot P^T$. Isto é claramente uma matriz simétrica.

- Se $B=\begin{pmatrix}d_1 & 0 \\ 0 & d_2\end{pmatrix}$ for uma matriz diagonal, então q(x,y)=1 é equação de
    - uma elipse, se $d_1>0 ~e~ d_2<0$
    - uma hipérbole se $d_1d_2<0$
    - $\varnothing$ se $d_1<0 ~e~ d_2<0$

- Se P for uma matriz de uma isometria então $P^T=P^{-1} ~~e~~ B=P\cdot A\cdot P^{-1}$
- Se B for uma matriz *diagonal*, então d1 e d2 são autovalores de A

## Teorema
- Para qualquer forma quadrática $q(x_1,x_2)=ax_1^2+bx_1x_2+cx_2^2$ existe uma isometria do plano $(x_1,x_2)=L(y_1,y_2)$ tal que ela seja tranformada na forma diagonal $\tilde d(y_1,y_2)=d_1y_1^2+d_2y_2^2$.
### Corolário
- Se A for uma matriz simétrica 2x2 então 
    - o polinómio caraterístico de A tem 2 raízes reais
    - A é diagonizável
    - os autovetores de A formam uma base ortogonal de R2

#alga #quadraticas