**"The Verdet Constant of Light Flint Glass"**
### Abstract
- Materiais opticamente inativos podem tornar-se ativos quando sujeitos a campos B fortes. Mais concretamente, podem fazer a polarização de uma onda EM rodar
- Esse ângulo de rotação é proporcional ao campo B, comprimento do percurso ótico na amostra e a *constante de Verdet*
- Este artigo tinha o objetivo de determinar esta constante

### Introdução
- Um composto é quiral se a sua versão espelhada não pode ser transformada na original com rotações e outros tipos de formações.
    - No caso de compostos de carbono, isto normalmente acontece quando temos 1 átomo C ligado a 4 "peças" diferentes
    - Por razões, um composto deste tipo tem a capacidade de rodar a polarização de uma onda EM.
- Em 1845, Faraday descobriu que existem materiais que não reagem a luz normalmente, mas que reagem quando sujeitos a campos elevados. O sentido em que a onda EM roda depende se esta se propaga de forma paralela ou anti-paralela ao campo B
- Para estudar este fenómero, temos a *constante de Verdet* - mede o ângulo que a onda EM roda por unidade de distância e por unidade de tempo.

### Teoria
- Ou seja, no efeito Faraday, a rotação que a onda faz depende de
    - distância que a onda percorre na amostra
    - força do campo magnético a que a amostra está sujeita
    - constante de Verdet
ou seja:
$$\theta=VlB$$

- O índice de refração de um material depende se uma onda incidente está polarizada para a esquerda ou para a direita. Isto é causado pela forma como os eletrões em órbita perdem momento angular ao ser atingidos.
- Assim, de forma a estudar a relação $V(\lambda)$ desenvolve-se esta equação para estudar experimentalmente:
$$V = \frac{e}{2mc}\lambda \frac{dn}{d\lambda}$$

### Experimental
![[montagem t1o v3.png]]
- Os eletromagnets não geram um campo uniforme, pelo que se usou um gaussmeter para medir o campo B no centro da amostra.
    - Mediu-se em 9 pontos ao long da amostra, para 2 correntes diferentes.
- Em cada novo valor de corrente mediu-se o ângulo da polarização nova ao ajustar o analisador para um mínimo de luz transmitida.

### Resultados
#### B(I)
- Para a relação campo X corrente temos:
![[B vs I v2.png|475]]
em que temos o ajuste:
$$B = (747\pm2.1)I - 51.8\pm11$$
que usamos para saber o campo em cada valor de corrente sem ter o trabalho de o medir. Estes valores de campo são medidos no meio da gap entre as bobinas, que será o mesmo campo que no centro da amostra.

#### B no espaço
- Temos ainda os dados mencionados, em que medimos o campo em 9 locais ao longo da amostra, para 2 correntes:
![[B vs dist em amostra v2.png|475]]
- Aqui:
    - Relative field strength é $B/B_{0}$ ($B_{0}$ é o campo no centro da amostra)
    - Vemos que os campos relativos  para 2 correntes muito diferentes são quase iguais - a variação espacial do campo não depende da corrente.
- Para analisar isto e estimar o campo médio, fez-se ajuste dos dados correspondentes a corrente de 3A. Ajustou-se na gama $-15<x<15$ porque é a gama que corresponde ao espaço entre os orifiocs dos suportes das bobinas, sem entrar neles.
- Integrou-se a função de ajuste e obteve-se o *cmapo médio*:
$$\bar B=(1.08\pm0.07)B_{0}$$

#### Efeito Faraday
- Temos:
![[ang vs I.png|174]]
- O campo magnético aumenta linearmente com a corrente. Ao aumentar a corrente, $\theta$ aumenta. Assim, $\theta$ aumenta com o campo. Verifica-se efeito de Faraday.

### Análise/Discussão
- Podemos converter os valores de corrente acima em campo usando a equação $B(I)$ acima.
    - $B$ terá incerteza devido considerarmos o campo igual em toda a amostra
    - Para $\theta$ consideramos uma incerteza de 0.01 radianos (estimativa)
    - Para a corrente não se considerou incerteza, na execução variou muito pouco.
![[ang vs B.png]]

- Vez-se então o ajuste:
$$\theta=(1.091\pm 0.006) + (1.57\pm0.15)\cdot10^{-5}\bar B$$
pelo que a constante de Verdet será o declive da reta:
$$V=\frac{1}{l} \frac{\Delta \theta}{\Delta \bar B}$$
e fica
$$V = (4.13\pm 0.04)\cdot10^{-6}\text{ cm}^{-1}\text{G}^{-1}$$
- Depois relacionam isto com o valor que se determinaria teoricamente com a equação $V = \frac{e}{2mc}\lambda \frac{dn}{d\lambda}$