## 0. Enviar bits PC
- Ainda não existe lidar.cpp
- Todos os bytes recebidos no robot do Serial2 são enviados para o PC por Serial.print(), imediatamente mal são recebidos.
- A ideia era receber no PC e processar tudo no python
- Rapidamente vi que o PC não consegue acompanhar processar dados + gráfico
    - Ainda por cima nesta altura ainda usava matplotlib invés de PyQt

## 1. Calcular e enviar xy
- Já existe lidar.cpp que faz todo o processamento do buffer de LiDAR (cheio) para pontos xy
    - Sem checksum, esse foi adicionado muito depois
- Aqui temos ainda já find_lines_v1
    - Esta versão usa criterios que vai vendo progressivamente consoante acrescentamos dados (distância vertical do ponto novo, erro de linearidade, distância 12/23 e erro de linearidade para o início)
    - Este algoritmo funcionava mas rapidamente mostrou defeitos: pouco eficiente, mau a separar cantos e demasiadas redundâncias
    - Já se usava PCA para fazer ajuste dos grupos "lineares" de pontos
    - Pouco estável, ao ponto que era preciso usar coisas como isnan, isinf
- Enviava-se para o PC os pontos e linhas

## 2. Calibrado e find_lines_v2 
- No lidar.cpp faz-se a calibração dos pontos conforme feito no comunicarPYTHON
- Temos find_lines_v2:
    - clusters > PCA > cantos
    - guarda tudo em arrays - pouco eficiente
- Temos find_pose_v1:
    - Validar paredes por comprimento
    - Matching: usar referencial global e ver que parede vimos mais proxima da referencia i. Isto implica confiar _*muito*_ na pose. Falhou completamente
    - Usar APENAS a parede mais próxima para estimar a pose usando transformações diretas de deslocamentos e medições.
- Enviamos linhas, pontos para PC

## 3. Calibrado e optimizado
- Penso que a única coisa que muda é que uso a tabela de valores para o seno e cosseno dentro do lidar.cpp
    - Isto reduziu imenso o tempo de execução dessa função

## 4. Pose com LiDAR
- Nesta função combinei a pose estimada por find_pose com a pose da odometria. 
- Não quis arriscar meter o robot a mover-se conforme o find_pose, então criei as variáveis udp_xe, udp_ye, etc. Cada uma destas é definida como um mini Kalman que combina a pose da odometria xe ("medição" Kalman). O udp_xe (e y,theta) funcionam como estado do Kalman. Em cada frame o find_pose_v1 atualiza o estado e juntamos a odometria
- Isto resultou em convergencia do valor sempre para a odometria. Normalmente o find_pose só introduzia ruído de forma pouco construtiva.