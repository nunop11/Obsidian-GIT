## Classificação 
------ slide 13
- Como vimos atrás, na tarefa de regressão apenas usamos os últimos 5 -atributos, que são aqueles que são quantitativos.
- Para classificação ponderamos usar apenas os atributos qualitativos, mas concluímos que seria melhor usar todos os 10 atributos, já que teremos mais informação para o modelo aprender. Acreditamos que isto poderia melhorar a exatidão.

- O principais modelos que estudamos para fazer classificação foram: LDA, softmax e redes neuronais.
- Para ter uma perspetiva geral, decidimos treinar e testar o LDA e softmax usando os sets de treino e de validação. 
    - Para LDA obtivemos 84% de exatidão.
    - Para softmax obtivemos por volta de 50%, mesmo para vários learning rates. Verificamos ainda que, devido à inicialização aleatória, a exatidão do modelo variava bastante de cada vez que ele era treinado.
- Ora, vemos que ambos os modelos têm uma performance insatisfatória. Sabemos ainda que em LDA nada pode ser feito para optimizar a performance além de data augmentation.
- Assim, de modo a tentar melhorar os resultados com os dados que temos, decidimos implementar uma rede neuronal densa

------ slide 14
- Podemos aqui ver a arquitetura definida para esta rede neuronal.
- Temos uma rede pouco profunda, com apenas 3 camadas ocultas. Outra caraterística principal é que, após a 1ª camada oculta, gradualmente diminuimos o número de neurónios. Isto fará com que a informação do input seja movida de forma correta ao longo da rede.
- Na última camada usamos softmax como função de ativação, o que contibui para o uso desta rede para classificação.
- Na primeira e segunda camada, que são as com maior número de neurónios, usamos dropout. Isto irá reduzir as chances de a rede fazer overfitting.
- Por fim, em todas as camadas ocultas fizemos batch normalization. Isto ajudará a estabilizar a rede.
- Como decidimos não fazer validação k-fold, esta rede foi treinada usando  os sets de treino e validação. O set de teste foi usado no fim para avaliar a rede final. O treino foi feito usando o CUDA, no GPU. Isto permitiu reduzir o tempo de treino em ordens de grandeza.

------ slide 15
- Aqui vemos a forma como implementamos a rede neuronal, com pytorch. Outras implementações, com mais camadas ou mais neurónios, foram testadas. No entanto, foram obtidos resultados semelhantes com uma performance pior.
- Temos ainda a class de early-stop implementada. Esta interrompe o treino da rede se a loss de treino não melhorar após um certo número de iterações. Graças a esta class, o treino da nossa rede demorou 71 epochs, o que demorou apenas 5 minutos.

------ slide 16
- A rede que treinamos teve uma exatidão de teste de cerca de 96%. Prevemos que se o treino fosse menos optimizado e extendido por mais tempo, a exatidão seria melhor.
- Anteriormente referimos que o atributo "type of PV module" foi erradamente convertido em valores númericos. Esta boa performance indica que isso não foi prejudicial. Isto pode ter ocorrido por 2 razões:
    - este atributo não tem uma forte correlação com o nível de eficiência, logo a sua má conversão nunca afetaria muito as previsões
    - outra possibilidade é que este atributo está igualmente distribuido entre os 4 níveis, de modo que a errada conversão "prejudicou" por igual todos os níveis, sendo pouco notável.
