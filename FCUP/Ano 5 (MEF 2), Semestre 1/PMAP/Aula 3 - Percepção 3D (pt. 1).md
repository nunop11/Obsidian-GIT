## Nuvem de Pontos 
- Podemos definir:
    - **Ponto** - localização no espaço $p\in \mathbb{R}^{D}$. Se $D=2$ estamos em 2D, $D=3$ estamos em 3D, etc. Podemos ter mais dimensões, para incluir atributos como intensidade de sinal, cor, orientação, etc
    - **Nuvem de pontos** - coleção de pontos de um certo espaço. 

### Aquisição de pontos
- Como vimos atrás, existem sensores ativos e passivos.
![[Pasted image 20251002142048.png]]

#### Passivos
- Estes tipos de sistemas são usados em SLAM visual e estimação de posição de robots
- Este tipo de técnicas utilizam dados apresentados em imagens 2D (fotografias)
- Dois tipos comuns:
    - *Técnicas de stereo matching* - estimamos a estrutura 3D utilizando dois sets de dados 2D, associando pontos correspondentes (sabemos que o ponto X na imagem 1 representa o mesmo ponto do objeto que o ponto Y na imagem 2)
    - *Structure-from-Motion (SfM)* - obtemos muitos pontos. Com isso determinamos a estrutura 3D do objeto e a posição da câmara

- Neste tipo de técnicas temos:
    - calibração offline
    - retificação de imagem online
    - stereo matching online
    - triangulação online

![[Pasted image 20251002142559.png]]
- Em *stereo matching*, conhecemos o espaçamento entre as câmaras/sensores. Assim, associamos pares de pontos correspondentes aos mesmos pontos do objeto. 
- Conforme a *disparity / afastamento* de 2 pontos associados, atribuimos uma intensidade grayscale. Assim, podemos obter uma imagem que mostra a profundidade do objeto:
![[Pasted image 20251002142752.png]]

**Problemas**
- Um fator que afeta muito a qualidade deste método é a **textura** do objeto. Se tivermos regiões sem qualquer textura, não temos como associar pontos e não conseguimos estimar a estrutura 3D de forma adequada. 
- Outro fator importante e causado por utilizarmos câmaras é a **iluminação**. Se tivermos num ambiente muito escuro, as imagens serão piores e a estrutura 3D será estimada pior

#### Ativos
- Envolve manipulação da cena observada
- Para fazer isso, normalmente observamos a cena/objeto com uma câmara/sensor *enquanto* emitimos um sinal com um projetor/laser. A forma como o feixe/ponto laser interage com o objeto permite estimar a sua estrutura 3D
- Este método chama-se **structured light**:
![[Pasted image 20251002143637.png]]
(O projetor e a câmara podem estar num mesmo dispositivo unidos por um braço)

- Estes métodos conseguem determinar a estrutura e geometria do objeto com precisão, através dos defietos no padrão laser
- Notemos que estamos sujeitos à luz ambiente no meio e não podemso scannar objetos refletivos ou transparentes

- Algumas approaches:
    - **temporal coded** - projetar uma série de padrões binários (preto e branco). A sua evolução permite tirar informação sobre o objeto
    - **spatial coded** - usamos um padrão muito específico e que varia ao longo do objeto
    - **direct coded** - o padrão emitido apresenta um código/sequencia binária específica, que podemos associar a cada pixel na imagem captada na câmara. Facilita a reconstrução 3D
    - **time of flight (ToF) ou medição de fase** - analisamos melhor o sinal que é refletido do objeto para o sensor

----------- EXPLICAÇÃO DA AULA COM A GEOMETRIA

### Representação
- Como vimos, uma **nuvem de pontos** é uma coleção $P=\{p_{1},\dots,p_{n}\}$ de pontos $p_{i}\in \mathbb{R}^{3}$. Isto é feito com um array $n\times3$
- O que não referimos é que esta sequência **não tem estrutura**, ou seja, **está DESORDENADA**. Isto significa que o ponto $i$ e o ponto $i+1$ podem estar em zonas opostas da nuvem.
- A nuvem não ter estrutura implica ainda que não temos informação sobre *conexão de vertices* (NOTA: 'vertex' é 'vértice' em inglês). Por outras palavras, nada nos dados da nuvem de pontos nos diz como montar a estrutura 3D.

#### Nuvem de pontos estruturada
- Os pontos são ligados através de uma estrutura consistente. Para isso ligamos vértices (os pontos de dados passam a ser vértices ao ligá-los) adjacentes.
- SLIDE 13