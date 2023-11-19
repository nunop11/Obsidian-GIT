# 3- Transformações Lineares e Matrizes
- Transformação Linear:
    - Transformação $\approx$ função -> Basicamente recebe vetor e dá outro vetor. O termo transformação vem de que pretende pensar numa transformação como um movimento. Ou seja, imagina-se que o vetor inicial se move e estica até ser o vetor final.
    - Linear -> Graficamente são transformações em que:
        1. Linhas mantêm-se linhas, não se dobram
        2. A origem mantem-se no sítio
        - Basicamente, mantem as linhas paralelas e com espaços uniformes

- Ora, para estudar isto de forma númerica precisamos apenas de sabes o que acontece a $\hat i$ e $\hat j$. Isto porque se tivermos $\vec v = 2\hat i - 1\hat j$, como a transformação é linear, esta relação não se irá alterar após uma transformação. Ou seja 
$$\vec v (transformado)=2(\hat i(transformado))-1(\hat j(transformado))$$
- Assim conclui-se que, se após a transformação $\hat i = (a,b), \hat j = (c,d)$, então tem-se que um vetor que inicialmente tinha as coordenas $\hat u=x\hat i + y\hat j$ após a transformação passará a ter as coordenadas:
$$\hat v=x(a,b)+y(c,d) = (xa+yc, xb + yd)$$
- Assim, é comum colocar-se as  coordenadas de i e j após a transformação numa matriz 2x2, assim:
$$M=\left[ \begin{array}{cccc}
x_i \hspace{5mm} x_j\\
y_i \hspace{5mm} y_j
\end{array}\right]$$

- Assim, facilmente se deduz que:
$$T(x,y)=\left[ M.\left[ \begin{array}{cccc}
x\\
y 
\end{array}\right]\right]^T$$

#### Link do vídeo no Youtube:
https://youtu.be/kYB8IZa5AuE

#### Índice dos resumos
[[ALGA - INDEX]]

#matrizes #alga #transformacoes 