
Comecemos por observar o programa Labview feito. Ele segue o seguinte fluxograma:
![[fluxograma labview.png]]

Ao testar o programa verificamos que facilmente flutuações dos valores medidos. Assim, como mostrado no fluxograma, decidimos fazer média das últimas 10 medições, em cada instante. Podemos então observar o gráfico do Labview obtido ao fazer isto:
![[traçado labview.png]]
É evidente que a realização de médias suavizou bastante os dados, eliminando-se valores muito elevados ou  muito reduzidos medidos por erro. No entanto, é evidente que os pontos correspondentes a médias terão sempre um atraso de algumas dezenas de milissegundos, mas isso não será percetível pelo utilizador.
No labview guardamos apenas os últimos 10 valores medidos pelo sensor, invés de guardar todos os valores e fazer a média os 10 últimos. Isto foi feito para reduzir a quantidade de CPU usada, já que estamos a medir 1 valor a cada 10ms e um array com todos os valores medidos tornar-se-ia demasiado grande rapidamente. 

É decidido pelo programa se o arduino deve gerar vibrações em "tempos múltiplos de 100 ms", porque esta foi a forma mais expedita que encontramos de fazer esta verificação de forma frequente e uniforme.

Discutamos agora o código do arduino, que é relativamente simples. Este consiste em medir valores de distância utilizando o TFMini e enviá-los para o Labview com o Serial (O QUE É O SERIAL, VALE A PENA ESPECIFICAR??), num loop infinito.
Depois de enviados, como vimos acima, conforme as distâncias medidas o Labview diz ao arduino para se colocar no modo de vibração A,B,C,D. O modo D consiste em não vibrar, então o arduino não faz nada. Para os restantes modos usamos a função "vibrar", que vibra durante um certo intervalo de tempo, um certo número de vezes com um espaçamento especificado (TEM QUE HAVER UMA FORMA MAIS RAPIDA DE DIZER ISTO LOL). Assim, para cada modo foi previamente definido um certo intervalo de tempo, em que o motor vibra. Aqui torna-se importante realçar que, sendo o motor de vibração um motor DC, o tempo de vibração controla a "intensidade" de vibração sentida. Isto deve-se ao facto que o motor demora alguns instantes a chegar à sua velocidade (e portanto vibração) máximas, pelo que para qualquer tempo de vibração abaixo disso iremos sentir uma velocidade diferente.
Além disso, a função faz um LED piscar em sintonia com as vibrações, tendo-se um brilho mais intenso para vibrações mais intensas.