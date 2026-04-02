## Artigos relevantes que encontrei
### Localização
L1- **Hector SLAM** - https://ieeexplore.ieee.org/abstract/document/9336995
    - Algoritmo para SLAM
    - Comparar a medição anterior e atual, para determinar a variação de pose que causa a diferença -- Scan Matching
    - Usa Gauss-Newton para fazer descida de gradiente para determinar a variação de pose mais correta
L2- **ICP** - https://www.mdpi.com/1424-8220/25/15/4541
    - Algoritmo de localização usando um mapa conhecido / teórico
    - Este método compara aquilo que medimos com o mapa real, para obter a pose que melhor explicaria este resultado -- Scan Matching
    - Mais preciso mas computacionalmente mais pesado
    - Vários artigos usam este método:
        - https://www.mdpi.com/1424-8220/25/9/2822
    - Diferentes implementações e otimizações existem
L3- **Função de Distância** - https://arxiv.org/abs/1908.01863
    - Algoritmo de localização 
    - Utiliza uma função que varia conforme a distância. Calcular a sua Hessiana permite determinar a função de probabilidade de ocupação
L4- **Marcadores de posição** - https://www.sciencedirect.com/science/article/pii/S1383762125002280?via%3Dihub#fig2
    - Não utiliza PCDs complexas e que exigem mais computação
L5- **Resumo de localização** - https://www.mdpi.com/2072-4292/17/7/1214
    - Detalha vários métodos de localização para SLAM: Filtros (Kalman), Scan Matching (ICP), grafos e deep learning
        - Métodos com filtros (EKF, UKF, etc) são os tradicionais e consistem em obter loop closures para reduzir a covariância e estimar a pose do robot
        - Fala ainda de métodos de scan matching que consistem em tratar os mapas como imagens com FFT+ICP
        - Métodos de grafo consistem em definir um grafo conforme as poses do robot ao longo do tempo. Depois aplica-se otimização para ter um bom grafo final. Isto é mais focado em SLAM, não tanto para localização como temos na tese
        - Deep learning consiste em usar modelos de aprendizagem para fazer o que EKF e scan-matching fariam. Precisa de MUITOS dados
    - Depois fala de alguns tópicos em mais investigação atualmente:
        - Ajuste de métodos SLAM na presença de pessoas no ambiente
        - SLAM com fusão de LIDAR e imagem. Combina-se dados LIDAR em formato de imagem com imagens
    - Os autores implementaram vários métodos para ver os resultados obtidos
L6- **SLAM com visão** - https://link.springer.com/article/10.1007/s42452-020-2001-3
    - Explica como pode ser feito SLAM usando features, de visão com câmara
L7- **SLAM com fusão de LIDAR e UWB** - https://ieeexplore.ieee.org/abstract/document/9450022
    - Usa scan-matching para fazer SLAM em ambientes complexos
    - Os UWB funcionam como N pontos de referencia, em que o robot consegue saber qual é o mais próximo de si
L8- **Lidar inclinado** - https://www.mdpi.com/1424-8220/20/9/2500
    - Este e outros artigos utilizam Lidares com uma inclinação específica para ver o chão à sua frente e detetar paredes conforme chegam a elas
L9- **SLAM com PCA** - https://ieeexplore.ieee.org/abstract/document/1570142
    - Implementa SLAM usando PCA para formar cluster de pontos que marcam paredes
    - Semelhante ao que estou a fazer
    - Implementa SLAM usando linhas, não landmarks
- Outros métodos que vi online: GMapping, Hector SLAM
- Basicamente todos os artigos usam ROS

### Linhas
D1- **Função de curvatura local** - https://www.icj-e.org/download/ICJE-7-5-87-91.pdf
    - Usa a curvatura local para decidir o que é reta, curva, etc. Usa os saltos de curvatura para separar os dados em segmentos
    - Permite separar os dados LiDAR em peças conforme descontinuidades da curvatura. O traçado de curvatura em cada grupo permite saber se temos linha, curva, etc
D2- **Algoritmo de deteção de linhas com seed** - https://journals.sagepub.com/doi/10.1177/1729881418755245
    - Algoritmo que obtem linhas começando com uma região seed. Depois vai-se incluindo pontos na linha até um ponto quebrar a reta
    - Tempo de execução testado num PC: 1ms
D3- **Resumo** - https://ieeexplore.ieee.org/document/1545234
    - Testaram uma série de algoritmos de deteção de linhas
    - Vários métodos (Iterativo, Hough, Split and Merge, Line regression) implicam calcular parâmetros multiplas vezes para incluir/excluir pontos
 

## Rascunhos
### Tópicos a tocar
**Intro**
- Robot at Factory 4.0 é uma competição em que:
    - Robot tem de se localizar num mapa *conhecido*
    - Detetar paredes e mover cargas entre armazens e máquinas
    - Pretende replicar ambiente industrial com objetivo didatico
- Este artigo pretende introduzir:
    - Algoritmos de deteção de linhas e localização usando apenas dados LiDAR e odometria
    - Algoritmos otimizados, que são executados em ~10ms num RP2040
    - Medidas de precisão?

**State of the art / related work**
- Na literatura normalmente encontramos o estudo de algoritmos SLAM
- Estes têm alta complexidade e frequentemente utilizam visão por câmara ou LiDARs 3D
- Os métodos utilizados (ICP, Scan-matching, GMapping) são computacionalmente pesados e precisam de ser executados por computadores mais capazes
- Em termos de algoritmos de linhas, aqueles mais conhecidos (Transformada de Hough, Split and Merge, iterativo) implicam cálculo repetido de parâmetros para encontrar a confirguração ótima de segmentos lineares.
- Ou seja: diversas fontes na literatura apresentam aquilo que é apresentado neste artido, mas com meios mais capazes de computação

### Versão 1 (PT) - First draft
Robots moveis são cada vez mais importantes no dia a dia, nomeadamente em armazéns. O principal desafio deste problema é a localização do robot no ambiente que o rodeia.

Na literatura, uma grande porção dos trabalhos focam-se na realização de SLAM, utilizando diferentes técnicas para determinar a localização do robot. (L1) introduz Hector SLAM, um método que utiliza scan-matching para determinar a variação da pose entre 2 instantes. (L2) apresenta também scan-matching, mas através de ICP, que permite uma melhor precisão com maior peso computacional. Existem ainda vários autores, que utilizam SLAM com visão por computador (L6) ou com fusão de medições (L7). É ainda possível encontrar estudos de algoritmos para localização sem aplicação SLAM, utilizando marcadores de referência (L4) ou métodos probabilísticos num ambiente conhecido (L3).

Para deteção de segmentos lineares em dados de LiDAR, vários métodos existem como "Split and Merge" e Tranformada de Hough (D3). Também podem ser utilizados métodos baseados em curvatura local (D1) e PCA (D2).

Tendo em conta a relevância deste tópico, é fundamental promover o interesse de estudantes nesta área. 
A competição Robot@Factory consiste numa simulação de um ambiente industrial em pequena escala, em que um robot deve localizar-se num ambiente conhecido, enquanto executa tarefas. Tendo em conta o objetivo didático desta competição, os algoritmos existentes são demasiado complexos. Além disso, muitos dos métodos referidos exigem grandes custos computacionais, requerendo repetidos cálculos e comparações para minimizar erros e determinar a posição do robot.

Desta forma, este artigo pretende introduzir um algoritmo para localização de um robot num ambiente conhecido, através da deteção de paredes com dados de LiDAR. Este algoritmo está otimizado para ser implementado em sistemas low-cost, podendo atingir uma precisão de XYZ.

### Versão 2 (PT) - Melhorado
A robótica móvel desempenha um papel cada vez mais importante na sociedade. Uma área em que isto é especialmente notável é logística e gestão de armazéns. Aqui, um dos principais desafios a enfrentar é o problema de localização do robot no ambiente que o rodeia.

Na literatura, uma porção significativa da investigação foca-se em sistemas de _Simultaneous Localization and Mapping_ (SLAM), empregando diversas técnicas para estimar a pose do robot. (L1) introduz Hector SLAM, um método que recorre a _scan-matching_ para determinar a variação da pose entre instantes consecutivos. Similarmente, (L2) apresenta uma abordagem de _scan-matching_, mas baseada no algoritmo _Iterative Closest Point_ (ICP), o qual permite uma precisão superior, com um custo computacional mais elevado. Adicionalmente, diversas abordagens exploram o SLAM com visão de computador (L6) ou a fusão de medições de sensores (L7). Encontram-se ainda estudos focados na localização em ambientes previamente conhecidos recorrendo a marcadores de localização (L4) ou a métodos probabilísticos com funções de distância (L3).

No que consiste na deteção de segmentos lineares em dados LiDAR, destacam-se métodos clássicos como "Split and Merge" e a Transformada de Hough (D3). São ainda encontrados artigos sobre técnicas de curvatura local (D1) e métodos baseados em *Principal Component Analysis* (PCA) (D2).

Tendo em conta a relevância deste tópico, é fundamental promover o interesse de estudantes nesta área. A competição Robot@Factory simula um ambiente industrial em pequena escala, desafiando robots a localizar-se num mapa conhecido para executar tarefas. Tendo em conta o cariz didático desta competição, os algoritmos existentes apresentam-se demasiado complexos. Além disso, muitos dos métodos referidos exigem custos computacionais apreciáveis, exigindo processos iterativos de minimização de erro que não são viáveis em todas as plataformas.

Neste contexto, este artigo propõe um algoritmo de localização para ambientes conhecidos, baseado na deteção de paredes através de dados LiDAR. A abordagem apresentada foi otimizada para implementação em sistemas _low-cost_, demonstrando capacidade para atingir uma precisão de XYZ.

### Versão 3 (ING) - First draft
Mobile robotics plays an increasingly important role e today's society, namely in logistics and storage management. In this context, one of the main challenges is determining the location of the robot in its environment.

In the literature, a considerable portion of the work focuses on Simultaneous Localization and Mapping (SLAM), where various techniques are employed to determine the robot's pose. (L1) introduces "Hector SLAM", a scan-matching mehot that determines the optimal pose variation between consecutive frames. Similarly, (L2) details a different scan-matching approach, based on Iterative Closest Point (ICP), achieving higher precision with higher computation costs. Additionally, SLAM implementions with computer vision (L6) and sensor fusion (L7) can be found. Furthermore, there are various papers about robot localization in previously known maps, using location markers (L4) or probabilistic models (L3).

Concerning detection of linear segments in LiDAR data, a special focus is given to classical methods, such as "Split and Merge" and Hough transform (D3). Some works on method based on local curvature (D1) and Principal Component Analysis (PCA) (D2) can be found.

Considering the relevance of this area, it is fundamental to promote students' interest in it. For this purpose, Robot@Factory is a competion that simulates a small scale industrial environment. Students are challenged to develop robots that can perform localization while executing tasks. Considering the didatic character of this event, the aforemention methods are frequently over complex and require computational power that isn't possible in every platform.

This paper proposes a localization algorithm, based in line detection with LiDAR data. The approach presented is optimized for low-cost applications, displaying precision of around XYZ.

### Versão 4 (ING) - Melhorado 
Mobile robotics plays an increasingly important role in today’s society, particularly in logistics and warehouse management. In this context, one of the main challenges faced is determining a robot’s location within its environment.

A significant portion of the literature focuses on Simultaneous Localization and Mapping (SLAM), where various techniques are employed to determine the robot’s pose. (L1) introduces “Hector SLAM”, a scan-matching method that estimates the optimal pose variation between consecutive frames. Similarly, (L2) presents a different scan-matching approach based on Iterative Closest Point (ICP), achieving higher precision with increased computational costs. In addition, SLAM implementations based on computer vision (L6) and sensor fusion (L7) have been studied. Furthermore, various papers explore robot localization in previously known maps, using location markers (L4) and probabilistic models (L3).

Regarding the detection of linear segments in LiDAR data, special emphasis is given to classical methods such as Split-and-Merge and Hough Transform (D3). Other approaches based on local curvature (D1) and Principal Component Analysis (PCA) (D2) have also been found in the literature.

Given the relevance of this field, promoting students’ interest in robotics and localization is essential. In this context, Robot@Factory is a competition that simulates a small-scale industrial environment, challenging students to develop robots capable of performing localization while executing tasks. Due to the educational nature of this event, the aforementioned methods are often overly complex and require computational resources that are not available on all platforms.

This paper proposes a localization algorithm based on line detection using LiDAR data. The approach presented is optimized for low-cost applications, achieving a precision of approximately XYZ.
