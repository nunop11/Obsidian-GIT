# 6 - Matriz Tridiagonal
- Este é um caso especial que frequentemente aparece em física. Temos um sistema $Av=x$, mas com $$A = \begin{pmatrix}a_{00} &a_{01} &0 &0 &0 \\ a_{10} &a_{11} &a_{12} &0 &0 \\0  &a_{21}&a_{22} &a_{23} &0 \\ 0 &0  &a_{32} &a_{33} &a_{34} \\ 0 &0 &0 &a_{43} &a_{44} \end{pmatrix}$$
- Ou seja, apenas temos elementão _não-zero na diagonal e subdiagonais superior e inferior_.
- Neste caso, eliminação gaussiana é suficiente. Isto porque, nem precisamos de fazer o método inteiro. Isto porque apenas precisamos de subtrair uma certa linha `m` à linha `m+1` e a mais nenhuma (porque ficaríamos com `A[m+2, :] -= 0 * A[m, :]`)
- Após a eliminação gaussiana, ficamos com uma matriz com 1s na diagonal principal e números não-zero apenas na diagonal superior. Tudo o resto são 0s. Ou seja, também a backsubstitution é mais simples.

- Mais concretamente, na backsubstitution ficamos com algo do tipo:
![[backsubstitution.png]]
- Ao método de eliminação de gauss simplificado explicado acima chamamos de _Thomas Algorithm_. Para matrizes tridiagonais, isto costuma ser mais rápido que o `np.linalng.solve`

# 7 - Matriz Banded
- Matrizes em que há mais do que 1 subdiagonal diferente de 0 acima e abaixo.
![[matriz banded.png]]
- Basicamente, podemos resolver estas matrizes ao simplificar o Thomas Algorithm:
    - Temos uma matriz com `N` subdiagonais não nulas, acima e abaixo
    - Ao fazer eliminação gaussiana, se tivermos na linha `m`:
        - Comparamos o elemento da diagonal, `A[m, m]`, apenas com os elementos na zona `A[m:m+N , m]` (`N` linhas abaixo da linha atual) para fazer pivotagem parcial.
        - Apenas subtraímos a linha `A[m, :]` às `m` linhas abaixo.
    - Fazemos backsubstitution conforme temos na imagem na secção acima, mais ou menos.

- Isto é um tipo comum de sistemas em física, pelo que é útil escrever um código geral que podemos usar sempre.

#computacional #programacao #matrizes 
