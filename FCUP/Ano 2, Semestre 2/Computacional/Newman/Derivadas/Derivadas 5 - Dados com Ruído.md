# 6 - Derivadas de Dados com Ruído
- Por vezes, em vez de querer derivar uma função $f(x)$ queremos a derivada do gráfico de um conjunto de dados em que o formato é claro ao olhar, mas em que temos ruído.
- Ora, se calcularmos a derivada da "função" em cada ponto e fizemos um gráfico, veremos que o problema do ruído só piora. Isto ocorre quase sempre que fazemos isto e a razão pode ser vista na imagem abaixo:
![[dados com ruido.png]]

- O que podemos fazer:
    1. Usar $h$ maior. Basicamente, estamos a fazer o mesmo que fazemos ao usar $h$ maior para reduzir o erro de arredondamento. Ou seja, estamos a pior o erro de aproximação ao reduzir o "erro de ruído".
    2. Aproximar uma secção dos dados à volta do $x$ em que queremos derivar a uma curva. Mas não fazemos como nas aproximações de derivadas e integrais com polinómios (em que usamos 3,4 pontos). Fazemos uma regressão de quadrados mínimos.
    3. Suavizar os pontos om outro método como, por exemplo, aproximações de Fourier.

#computacional #programacao #derivada