![[comparar listas e arrays.png]]
- Consideremos que se tem o programa acima
    - `f1` e `f2` são 2 funções matematicas
    - `mandar_fazer1` é um função que dá return da lista de imagens correspondente à lista de valores dada, para a função dada.
    - `soma_array` e `soma_lista` dão a soma dos termos de um np.array e de uma lista python

## Contar tempo de execução de função
`result = %timeit -n 10 -r 100 -o f1(x) # -n : nº Loops ; -r : nº Runs; -o : Dá um output com o valor médio`

- `result` é uma variavel que nos dá o tempo com incerteza que demora para executar a função `f(x)`
- se a seguir fizermos `result.average`, iremos obter o tempo de execução médio

![[Medir tempo de execucao de função.png]]
- Podemos fazer aquilo acima para testar uma funçao. Com um loop, geral N listas de comprimentos de 1 a N (em que cada iteração aumentamos o tamanho), e registar numa lista `resultados`, o tempo que a função demora a correr para cada tamanho de lista. No fim podemos traçar um gráfico.

#apontamentos #programacao
