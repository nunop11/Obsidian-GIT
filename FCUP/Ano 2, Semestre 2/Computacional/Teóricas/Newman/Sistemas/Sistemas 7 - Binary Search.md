# 11 - Binary Search
- Método mais robusto para resolver equações não lineares de 1 variável $x$.
- De uma forma reduzida, definimos um intervalo em que queremos encontrar 1 solução da equação e este método vai sempre encontrá-la.

- Tendo uma equação de 1 variável qualquer, podemos sempre colocá-la na forma $\large f(x)=0$. Assim, ao procurar soluções estamos na realidade a procurar _zeros/raízes_. Esta é a base do método de Binary Search.

![[binary search.png]]

### Explicação do método
- Assim, queremos encontrar um zero de $f$ entre $x_{1}$ e $x_{2}$. 
- Começamos por determinar $f(x_{1}), f(x_{2})$. 
    - Podemos ter que um destes pontos é positivo e outro negativo. Neste caso, desde que a função $f$ seja contínua, temos pelo menos 1 zero neste intervalo.
- De seguida determinamos $f(x')$, a imagem do ponto médio do intervalo: $\large x'=\frac{1}{2}(x_{1}+x_{2})$. 	
- Se $f(x')=0$ já temos o zero. Senão, este ponto será necessariamente positivo ou negativo. Ou seja, tem o mesmo sinal que um dos pontos $f(x_{1}),f(x_{2})$ e sinal oposto ao outro. Consideremos o caso na figura acima: $f(x')$ tem sinal oposto $f(x_{1})$.
- Assim, tal como vimos antes, se $f(x_{1}),f(x')$ têm sinais opostos e $f$ é contínua, deverá haver 1 zero entre $x_{1}$ e $x'$. No entanto, a distância entre estes 2 pontos é metade daquela entre os 2 pontos iniciais.
- Assim, repetimos o processo, ficando cada iteração com um intervalo menor por um fator de 2, até encontrar o zero.

### Explicação para fazer código
1. Decidir os limites do intervalo: $x_{1},x_{2}$ e a precisão $\epsilon$ que desejamos.
2. Determinar as respetivas imagens: $f(x_{1}),f(x_{2})$ e ver se têm sinais opostos.
3. Determinar o ponto médio: $x'=\frac{1}{2}(x_{1}+x_{2})$ e calcular $f(x')$
4. Se $x'$ tem o mesmo sinal que $x_{1}$ definir $x_{1}=x'$. Caso contrário, $x_{2}=x'$
5. Voltar ao passo 2 e repetir até $|x_{1}-x_{2}|<\epsilon$. Se tivermos a precisão desejada, obter o ponto médio uma última vez e isso será o zero.

## 11.1 - Rapidez e Nº de Passos
- Tal como o método de relaxação, o _erro diminui exponencialmente com as iterações_.
- Consideremos que os pontos iniciais $x_{1},x_{2}$ estão a uma distância $\Delta$. Em cada iteração dividimos essa distância em 2. Ou seja, a distância do intervalo após $N$ iterações é $\Delta/2^{N}$. Ou seja, se queremos uma precisão $\epsilon$, o número de iterações que precisamos é:
$$N = \log_{2} \frac{\Delta}{\epsilon}$$
- Assim, este método é muito rápido. Por exemplo, se tivermos $\Delta=10^{10}, \epsilon=10^{-10}$, precisaremos apenas de $\approx 67$ passos.

## 11.2 - Aplicação e problemas
- Se $f(x_{1}),f(x_{2})$ tiverem o mesmo sinal, ou a função não tem zeros ou tem um número par. Em ambos os casos, o método não funciona.
- Muitas vezes, ao usar este método não fazemos ideia de onde esperamos ter zeros (ou se eles existem), portanto quaisquer $x_{1},x_{2}$ por mais longe que estejam servem, desde que tenham _sinais opostos_.
- Se a função, por alguma razão física, será negativa ou positiva a partir de um certo valor, devemos usar isso para definir o intervalo inicial.
- Se esperamos ter um zero num certo $x$, começar com $x_{1},x_{2}$ próximos de $x$. Se não encontrarmos zero, duplicar $x_{1},x_{2}$ e repetir.
- Outra situação em que o método falha é **raízes múltiplas par**: como temos por exemplo em $f(x)=(1-x)^{2}$. Nestes casos, a função passa no zero mas *não muda de sinal*, pelo que o método não deteta o zero.
- Por fim, este método não funciona para resolver sistemas de equações.

#computacional #programacao 
