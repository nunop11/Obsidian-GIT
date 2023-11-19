> Isto foi ensinado pelo Viana mas não está no Newman.
# 15 - Método de Jacobi
- Uma matriz $A$ é *diagonal-Dominante* se: $$|a_{ii}|> \sum\limits_{i\ne j} |aij|, \forall i$$
Ou seja, em todas as linhas, o elemento da diagonal é o maior elemento, em módulo.

- Tendo um sistema $Ax=v$, sendo $A$ diagonal-dominante, podemos escrever:
$$A=D+L+U$$
sendo esta matrizes: a sua diagona, uma triangular inferior e uma triangular superior.
- A solução poderá convergir, de modo que ao iterar várias vezes temos:
$$x_{n+1}=D^{-1}(v-(L+U)x_{n})$$
e temos $$(x_{n})_{i} = \frac{1}{a_{ii}} (v_{i}- \sum\limits_{i\ne j} a_{ij}(x_{n-1})_{j})$$(isto não passa de eliminação de gauss)

## 15.1 - Na prática
![[codigo jacobi.png]]
- Podemos ver que isto consiste em apenas aplicar a última fórmula.
- Se a matriz não for diagonal-dominante, não teremos convergência

# 16 - Método de Gauss-Seidel
- Também precisamos de ter uma matriz Diagonal-Dominante para haver convergência
- Agora definimos: $$A=L+U$$
sendo ambas matrizes triangulares (inferior e superior) com 0s na diagonal principal.

- Da iteração temos:
$$x_{n+1}=L^{-1}(v- Ux_{n})$$
e temos, para cada elemento: $$(x_{n})_{i}=\frac{1}{a_{ii}} \left(v_{i} -\sum\limits_{j=1}^{i-1}a_{ij}(x_{n})_{j} - \sum\limits_{j=i+1}^{N}a_{ij}(x_{n-1})_{j} \right)$$
## 16.1 - Na prática
![[gauss seidel.png]]

#computacional #programacao 