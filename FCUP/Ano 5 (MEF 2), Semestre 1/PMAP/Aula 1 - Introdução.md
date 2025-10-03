# Introdução
## Professor
- Andry Pinto
- amgp@fe.up.pt
- Assunto os emails: `PM[.....]` 

## Introdução a PMAP
- Um sistema autónomo precisa de:
    - detetar/sense o ambiente que o rodeia
    - gerir informação parcial e incerta
    - entender e definir ações de forma a atingir o seu objetivo
    - implementar essas ações
sendo que isto ocorre de forma cíclica:
![[Pasted image 20250920185029.png]]

- Podemos esquematizar um processo de perceção da seguinte forma:
![[Pasted image 20250920185307.png]]

- E podemos representar um sistema autónomo desta forma:
![[Pasted image 20250920185424.png]]

### Deteção / Sensing
- Antes disto, tem que se fazer passos de calibração e alinhamento dos dados, para não termos bias forçados
- Os dados de sensing (pedidos pelos sensores e que são tratados pelo sistema de perceção) VÃO variar para cenários indoor ou outdoor
- As condições do ambiente afetam a perceção do sistema, normalmente na forma de incertezas
- Num sistema autónomo podemos ter uma série de sensores (câmaras, LIDARs, RADARs, ultrassom, etc) que temos que combinar para ter boa informação

### Dados VS Informação
- **Dados**
    - Coleção de valores. Representam factos, instruções, medições. Podem ser números, caratéres ou outro tipo
- **Informação**
    - Dados processados, organizados ou classificados de forma útil para a tarefa/requisitos.
    - Podemos ter vários requisitos:
        - Precisão (incerteza baixa)
        - Completo
        - Pronto quando necessário

### Extração de informação
- Separar dados com significado de dados inúteis. Aos dados inúteis ou sem informação chamamos de **ruído**
- Tendo os dados significantes são então interpretados, combinados, modificados, interligados, estruturados, etc. O resultado disso é a *informação*

- Em situações mais complexas, usamos diferentes fontes de dados (sensores) para definir várias features do ambiente. Com estas podemos definir objetos no ambiente.
![[Pasted image 20250921200807.png]]

### Modelos para representar cenários
- No caso de muitos robots, o ambiente/cenário que os rodeia influencia muito as ações que eles executam
- Deteção e Representação de Cenários é feita através de dados dos sensores
- Podemos então ter representações de vários tipos:
![[Pasted image 20250924164128.png|500]]
    - Na 1ª imagem temos mapeamento 3D, em que assinalamos os pontos medidos pelos sensores (profundidade de vários pontos no fundo aquático).
    - Na 2ª imagem vemos uma figura que representa uma versão 2D de um cenário. A preto temos zonas que o robot não consegue alcançar. Os circulos vermelhos serão obstáculos ou outros robots. Na imagem 2b) temos a versão da figura ao considerar as cinemáticas do nosso robot (certas limitações que alteram a forma como se move e impedem de alcançar certos pontos).

![[Pasted image 20250924165001.png]]
    - Na 1ª imagem vemos:
        - a) robot real num cenário real (caixa não muito grande)
        - b) a nuvem de pontos que este robot usa. No entanto notemos a quantidade enorme de pontos, algo que pode ser desnecessário e até prejudicial em certos casos
    - Na 2ª imagem vemos a representação 2D (visto de cima) de um cenário. A preto temos obstáculos e a diferentes tons de cinzento temos um gradiente de custo (mais escuro = mais perto de obstáculos). Este método chama-se "map-matching espaço-temporal". O robot mede o que o rodeia e compara a este mada de forma a localizar-se.

## A UC em si
### Programa
- **Sensores**
    - Câmara
    - LiDAR
    - Sonar
    - De inércia

- **Imagens** : *Processamento e análise*
    - Aquisição de imagens de intensidade e cor
    - Calibração de câmara
    - Extração de features e outliers
    - Metrologia de 1 view
    - Geometria de multiplas views
    - Estimação de objetos e tracking destes

- **Nuvens de pontos** : *Processamento e análise*
    - Aquisição de nuvens de pontos (frma ativa e passiva)
    - Filtros, extração de features e registo

- **Percepção multimodal**
    - Calibração de sistemas multi-sensores
    - Fusão de sensores (KF, Bayes)
    - Representação de cenários

- **SLAM** : *Localização e Mapeamento Simultâneos*

### Calendários
![[Pasted image 20250924173718.png]]

### Avaliação
$$\text{Nota final} = 75\% \text{CF} + 25\% \text{Exame}$$
em que temos a componente de avalição distribuída:
$$\text{CF} = 20\% \text{Assig}_{1} + 25\% \text{Assig}_{2} +30\% \text{Assig}_{3}$$
- Todos os componentes têm nota mínima (8 valores assumo eu)
- Apenas se pode fazer melhoria/recurso no exame
- Nos assignments, 25% é retirado à nota por cada dia atrasado :0