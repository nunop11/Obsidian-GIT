## v0 - PT
### 2. Metodologia
#### 2.1 Algoritmo de deteção de linhas
Neste trabalho, propomos a utilização de um LiDAR 2D paralelo ao chão. Este captará nuvens de pontos nos 360º à sua volta. Após observação extensiva, concluiu-se que paredes são detetadas como clusters de pontos numa distribuição linear, devendo estes estar suficientemente afastados dos restantes pontos.

Utilizando esta informação, a nossa proposta para um algoritmo de deteção de linhas começa por dividir os pontos detetados em clusters. Para delinear estes clusters, decidimos criar um threshold para a distância entre pontos consecutivos do cluster. Estando os pontos $i,i+1$ a uma distância média $d$  (METER CODIGO A USAR MÉDIA MESMO) e o LiDAR tiver uma resolução angular $\delta$, definimos este threshold como:
$$\text{Cluster Threshold} = d\tan(\delta)\cdot \tau$$
Em que $\tau$ é um parâmetro variável para definir a sensibilidade do filtro, a ajustar conforme a precisão do LiDAR. Este critério foi definido através da divergência angular de 2 feixes LiDAR, que será de $d\tan(\delta)$ a uma distância $d$

De seguida, é calculada a matriz de covariância 2D e o centroide de cada Cluster. Usando os valores próprios da matriz, conseguimos determinar a linearidade do cluster (https://doi.org/10.5194/isprsannals-II-3-181-2014):
$$\text{Linearity} = \frac{\lambda_{1} - \lambda_{2}}{\lambda_1}$$
Esta é uma medida consistente e resistente a ruído, que observamos funcionar de forma consistente. Clusters com uma linearidade acima de um threshold $\varepsilon$ são consideradas paredes detetadas válidas.

Quando um cluster detetado tem linearidade abaixo de $\varepsilon$, pode haver diversas causas: o cluster contém duas paredes com um canto, apresenta demasiado ruído ou não contém secções lineares. No contexto da Robot@Factory, o cenário mais provável será detetar ruído no exterior da pista. De forma a fazer localização utilizando as paredes observadas, é imperativo que todas as paredes visíveis para o robot sejam detetadas.

Começamos por determinar a linearidade local em cada ponto do cluster, usando uma vizinhança de $2n$ pontos e o método de covariância explicado. Empiricamente, observamos que, consistentemente, o ponto de menor linearidade num cluster corresponde a um canto (OU LIMITE DE UMA PAREDE COM RUÍDO ATRÁS - CONFIRMAR). Assim, é calculada a linearidade de cada um destes subclusters, assinalando paredes se a linearidade for superior a $\varepsilon$.

Cada parede detetada é aramazenada através do seu centroide (coordenadas X e Y), comprimento e orientação. Para determinar o comprimento e orientação é usado PCA, projetando as extremidadades do cluster na direção principal. Estes parâmetros foram escolhidos devido à sua utilidade no algoritmo de localização. Notemos que a orientação aqui referida é a orientação da parede, observada pelo LiDAR, não a orientação global.

#### 2.2. Algoritmo de localização

Para fazer localização do robot, fizemos um algoritmo de matching das paredes observadas com as paredes de referência da pista RAF. Este matching poderia ser feito com um critério de minimização de custo (ARTIGO COM SLAM A MINIMIZAR CUSTO???) e filtro de Kalman.

No entanto, como explicado na secção 1.2 (EXPLICAÇÃO DA PISTA), a pista do nosso problema apresenta paredes com orientações e comprimentos específicos, numa simetria especial. Assim, decidimos implementar um algoritmo de matching mais eficiente, aproveitando todos os detalhes conhecidos sobre a pista. 