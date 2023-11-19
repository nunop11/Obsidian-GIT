# Custo de operações
Custo de um vetor por um vetor : $N$
Custo de uma matriz por um vetor : $N^2$
Custo de uma matriz por uma matriz : $N^3$
Custo de LU para uma matriz normal : $N^3$
Custo de LU para uma matriz tridiagonal : $N$

# Pivotagem
**Pivotagem Parcial** - Trocar linhas quando o pivô é zero. Trocar pela linha em que temos o elemento nessa linha com *maio módulo*. Trocar nas matrizes $A$ e $v$
**Pivotagem** - Igual a pivotagem parcial mas trocamos pela linha com elemento de *maior valor*

## Pivotagem Total
- Além de procurar valores com maior módulo nas linhas abaixo, ver também nas colunas à direita do valor da diagonal. Assim:
- Trocar linhas em $A,v$, tal como na parcial
- Trocar colunas a $A,x$. Como não conhecemos $x$, guardamos as trocas numa matriz identidade alterada. 
![[codigo pivotagem completa gauss.png]]

# LU
- É arbitrário se é $L$ ou $U$ que fica com $1$s na diagonal. Temos que:
    - *Factorização de Doolitle* - $L$ tem 1s na diagonal
    - *Factorização de Crout* - $U$ tem 1s na diagonal
- No Newman apenas vimos Crout, pois temos $U$ a ser igual à matriz $A$ após eliminação de gauss.

## LU com Pivotagem Total
- Existe mas é um overkill absoluto

# Banded
- Seguir método indicado no Newman
- Para usar a função banded() do Newman para resolver sistema com matriz com número diferente de subdiagonais `up` e `down`:
![[codigo banded.png]]

