- Iremos ver como resolver sistemas de equações lineares.
- Assim, consideremos este sistema:
$$\begin{cases}2\omega+x+4y+z=-4\\ 3\omega+4x-y-z=3\\ \omega-4x+y+5z=9\\ 2\omega-2x+y+3z=7 \end{cases} \Longrightarrow \begin{pmatrix}2&1&4&1\\3&4&-1&-1\\1&-4&1&5\\2&-2&1&3\end{pmatrix}\begin{pmatrix}\omega\\x\\y\\z\end{pmatrix}=\begin{pmatrix}-4\\3\\9\\7\end{pmatrix}$$
ora, podemos escrever a forma matricial como $$Ax=v$$
- Iremos ver várias técnicas úteis

# 1 - Eliminação Gaussiana
- Tendo o sistema escrito como $Ax=v$, recordemos algumas regras úteis:
    - Podemos multiplicar todos os termos de uma matriz por uma constante e a equação continua a ser válida e as solução não muda. Na forma matricial, se multiplicarmos os termos de uma linha da matriz $A$ por uma constante, também temos que multiplicar o termo dessa linha na matriz $v$.
    - Podemos combinar equações linearmente. Ou seja, se adicionarmos a uma linha da matriz $A$ um múltiplo de outra linha (e fizermos o mesmo na matriz $v$) então a solução não muda.

- Assim, conseguimos recordar ALGA. Ora, este método consiste em ir somando a linhas da matriz $A$ múltiplos de outras linhas até ficarmos com uma matriz diagonalizada.
- Ou seja, ficamos com uma matriz do tipo:
$$\begin{pmatrix}1&a_{01}&a_{02}&a_{03}\\0&1&a_{12}&a_{13}\\0&0&1&a_{23}\\0&0&0&1\end{pmatrix} \begin{pmatrix}\omega\\x\\y\\z\end{pmatrix}=\begin{pmatrix}v_{0}\\v_{1}\\v_{2}\\v_{3}\end{pmatrix}$$
isto equivale:
$$\begin{cases}\omega+a_{01}x+a_{02}y+a_{03}z=v_{0}\\ x+a_{12}y+a_{13}z=v_{1}\\ y+a_{12}z=v_{2}\\ z=v_{3}\end{cases}$$
- Daqui temos $z=v_{3}$
- Mas assim, $y=v_{2}-a_{23}z$ torna-se $y=v_{2}-a_{23}v_{3}$
- E da mesma form para $x$ e $\omega$. Basta ir substituindo "para cima".

- Assim, para resolver o sistema no topo desta página temos este código:
```
import numpy as np

A = np.array([[ 2, 1, 4, 1 ],
            [ 3, 4, -1, -1 ] , 
            [ 1, -4, 1, 5 ] , 
            [ 2, -2, 1, 3 ]], float)

v = np.array( [ -4, 3, 9, 7 ] ,float) 
N = len(v)

# Gaussian elimination 
for m in range(N):
    # Dividir todos os elementos da linha pelo elemento da diagonal
    div = A[m,m] 
    A[m, :] /= div 
    v[m] /= div
    
    # Subtrair a todas as linhas abaixo
    for i in range(m+1,N): 
        mult = A [i ,m] 
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

# Backsubstitution
x = np.empty(N,float)

# Percorrer matriz de cima para baixo e substituir
for m in range(N-1,-1,-1): 
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m, i] * x[i]

print(x)
```
- De notar que ao termo da diagonal pelo qual dividimos a linha chamamos de *pivô*

## 1.2 - Eliminação de Gauss Jordan
- Consiste em evitar fazer pivotagem. Para isso, continuamos a fazer eliminação de modo que a matriz se torna diagonal. Ou seja:
$$Ax=v\to Ix=v'\to x=v'$$
- Na prática:
```
def solveGJordan(A,v):
    M = A.copy()
    v = v.copy()
    N = len(u)

    for i in range(N):
        div = M[i,i]
        M[i,:] /= div
        v[i] /= div
        for m in range(i+1,N):
            mult = M[m,i]
            M[m,:] -= mult*M[i,:]
            v[m] -= mult*v[i]
            
# eliminar os elementos acima da diagonal
    for i in range(N-1,0,-1): 
        for m in range(i):
            mult = M[m,i]
            M[m,:] -= mult*M[i,:]
            v[m] -= mult*v[i]
            
    return v # o próprio vetor u corresponde à solução
```
- Ou seja, após fazer eliminação gaussiana da matriz, repetimos o processo com a matriz triangular, mas agora de baixo para cima. Do notar que apenas fazemos pivotagem na primeira parte. Na segunda não será necessário.
- Normalmente pior que eliminação gaussiana.

# 2 - Pivoting
$$\begin{pmatrix}0&1&4&1\\3&4&-1&-1\\1&-4&1&5\\2&-2&1&3\end{pmatrix}\begin{pmatrix}\omega\\x\\y\\z\end{pmatrix}=\begin{pmatrix}-4\\3\\9\\7\end{pmatrix}$$
- Temos este sistema. Ele é igual ao da secção anterior, mas o primeiro termo da 1ª linha é $0$. Ora, como na eliminação gaussiana dividíamos os termos pelo 1º, não podemos fazer isso quando ele é 0. Ou seja, precisamos de outro método.
- Assim, fazemos _pivoting_. Ou seja, trocamos 2 linhas (primeira e segunda), como temos abaixo:
$$\begin{pmatrix}3&4&-1&-1\\0&1&4&1\\1&-4&1&5\\2&-2&1&3\end{pmatrix}\begin{pmatrix}\omega\\x\\y\\z\end{pmatrix}=\begin{pmatrix}3\\-4\\9\\7\end{pmatrix}$$
de notar que temos também que trocar na matriz $v$, mas não trocamos na matriz $x$.

## Pivot Parcial
- Consiste em fazer a eliminação gaussiana como vimos antes mas:
1. A cada passo, ao chegar a uma linha $m$ procurar o elemento $m$ (que pertence à diagonal).
2. Ver todas as linhas abaixo e comparar o elemento $m$ de cada uma. Trocar a linha $m$ com aquela que tiver o elemento $m$ mais longe de 0.

#computacional #programacao #gauss #matrizes 