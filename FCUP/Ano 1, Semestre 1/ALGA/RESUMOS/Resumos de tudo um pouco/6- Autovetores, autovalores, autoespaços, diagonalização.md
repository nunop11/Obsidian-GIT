-Baseado em https://youtu.be/PFDu9oVAE-g -
# Autovetores e autovalores
- Em inglês são *eigenvalues* e *eigenvectores*

- Consideremos uma tranformação linear em 2D
- Se nos focarmos num certo vetor, podemos visualizar o seu **span**, ou seja, a reta em que está contido.
![[autovetor1.png]]
- No entanto, na maioria dos casos, o vetor deixará de estar no seu span após a tranformação linear
- No entanto, alguns vetores não. Nesses casos, a transformação apenas estica ou contorce o vetor, como se fosse um escalar.
- Os vetores unitários muitas vezes mantê-se no seu span. No entanto, isto depende basntante da transformação a ser feita.
- Por exemplo, uma transformação de rotação não tem nenhum autovalor
- Como já deu para prever, estes vetores são ==autovetores==.

- Por outro lado, ==autovalores== são o quanto um vetor é "esticado". Por exemplo, um autovalor de 2 quer dizer que é esticado de forma a ter o dobro do comprimento. Se o autovalor for -1/2 quer dizer que é esticado de forma a passar a ter metade do módulo E é virado para o lado oposto AKA é rodado 180º.
- De notar que os autovetores correspondentes a autovalores diferentes serão sempre L.Independentes

## Calcular
- Se tivermos um autovetor $\vec v$, temos que:
$$A\vec v=\lambda \vec v$$, pelo que A é a matriz da transformação e lambda é o autovalor

- Assim, como sabemos que $\lambda \vec v$ será o resultado de multiplicar todos os termos de v por lambda. Ou seja, $A\vec v=(\lambda I)\vec v$. (I=matriz identidade)
- Assim, colocando o v em evidência:
$$(A-\lambda I)\vec v=\vec 0$$
- Desta forma, se tivermos, por exemplo $A=\begin{pmatrix}a&b \\ c&d \end{pmatrix}$, então,
$$A-\lambda I=\begin{pmatrix}a-\lambda & b \\ c & d-\lambda\end{pmatrix}$$
- Assim, como vimos em [[6-  Determinante]], o determinante determina as porporções de algo após uma tranformção. Ora, ao ter este produto da matriz com o vetor v, é como se tivessemos uma transformação aplicada no vetor v. Assim, concluímos que $det(A-\lambda I)=0$
- Assim, $\lambda$ será dado por $det(A-\lambda I)=0$

# Autoespaços
- São o span do autovetor
- Por outras palavras, são a reta em que o autovetor está contido.

# Polinómio caraterístico
- É o polinómio de lambdas obtido do determinante de $A-\lambda I$.
- Representado por $P_A(\lambda)$
- **Caraterístico ao operador linear, não à matriz**

# Propriedade
![[propriedade autovetores.png]]

# Diagonalização
- Se tivermos uma matriz A cujo polinómio caraterístico tem n raízes, ou seja, que tem n autovalores em Rn, então ela pode ser diagonalizada. Ou seja, ==para uma raiz de Rn poder ser diagonalizada tem de ter n autovalores.==
- Assim, o que fazemos é uma mudança de base:
$$D=M_{k,\beta}\cdot A\cdot M_{\beta,k}$$
em que $\beta$ é a base dos autovalores.
- Disto iremos obter:
$$D=\begin{pmatrix}\lambda_1&0\\0& \lambda_2\end{pmatrix}$$
em que lambda 1 e 2 são os autovalores de A
- Na matriz diagonal acima, se houverem n autovalores diferentes, haverão n autovetores L.Independentes

#autovetores #autovalores #alga 