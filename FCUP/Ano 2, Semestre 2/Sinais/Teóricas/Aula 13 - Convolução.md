- Tendo 2 funções $f(x),h(x)$ a sua **convolução** é definida como:
$$g(x)=\int_{-\infty}^{+\infty}f(s)h(x-s)ds=f(x)*h(x)$$

__*EX PRÁTICO*__
- Consideremos as funções abaixo, que entram na fórmula:
![[funcao ex1.png|255]]   ;   ![[func ex2.png|200]]
- Desta forma, a função $h(x-s)$ que entra na fórmula:
![[func ex2 v2.png|250]]
sendo que ao variar $x$ iremos ter o pulso a mover-se nos $xx$.
- Assim, vamos ver os difernetes casos ao resolver a integral:
#### Caso 1 : $x<0$
![[convolucao ex1.png]]
- Não há sobreposição entre os pulsos. Temos que, para todo o $x$: $f(s)h(x-s)=0$. Assim: $$\int_{-\infty}^{+\infty}f(s)h(x-s)ds=0$$
#### Caso 2 : $0\le x\le 1$
![[convolucao ex2.png]]
- Fora da zona de sobreposição continuamos a ter $f(s)h(x-s)=0$. Na zona de sobreposição temos $f(s)h(x-s)=1$. Assim: $$\int_{-\infty}^{+\infty}f(s)h(x-s)ds=\int_{0}^{x}ds=x$$
#### Caso 3 : $1\le x\le 2$
![[convolucao ex3.png]]
- Novamente, temos que fora da zona de sobreposição continuamos a ter $f(s)h(x-s)=0$. Na zona de sobreposição temos $f(s)h(x-s)=1$. Assim:$$\int_{-\infty}^{+\infty}f(s)h(x-s)ds=\int_{x-1}^{x}ds=1$$
#### Caso 4 : $2\le x<3$
![[convolucao ex4.png]]
- Novamente, temos que fora da zona de sobreposição continuamos a ter $f(s)h(x-s)=0$. Na zona de sobreposição temos $f(s)h(x-s)=1$. Assim:$$\int_{-\infty}^{+\infty}f(s)h(x-s)ds=\int_{x-1}^{2}ds=3-x$$
#### Caso 5 : $x>3$
- Agora não temos zona de sobreposição. Desta forma, voltamos a ter o mesmo que no caso 1: $$\int_{-\infty}^{+\infty}f(s)h(x-s)ds=0$$

- Se fizermos um gráfico de $g(x)$ temos:
![[convolucao grafico.png]]

## Significado / Conclusões
- Tanto $f,h$ como $g$ são funções de $x$, pelo que ao fazer a convolução não estamos a mudar variáveis
- Na prática, a convolução indica-nos o *grau de sobreposição* entre 2 funções, conforme deslocamos a função $h$.

#sinais #fisica
