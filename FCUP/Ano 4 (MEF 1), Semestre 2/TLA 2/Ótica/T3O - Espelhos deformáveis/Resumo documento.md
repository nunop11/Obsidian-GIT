##### Frentes de onda de modos de polinómio de Zernike
### Objetivos
- Familiarizar com um sistema de ótica adaptativa: sensor de frente de onda e espelho deformável
- Gerar frentes de onda do primeiro polinómio de Zernike usando um espelho deformável
- Medição de frentes de onda com um sensor de frente de onda Shack-Hartmann
- Reconstrução da frente de onda usando as medições do sensor

### Intro
- Otica adaptativa (AO) tem o objetivo de compensar aberrações da frente de onda em certos sistemas
    - EX: microscopia, comunicação laser, astronomia...
- Um sistema AO consiste em em 3 partes: sensor de frente de onda (WFS) que mede as distorções desta, espelho deformável (DM) para alterar a frente de onda e um computador que altera o DM conforme as medições do WFS
    - Estes 3 trabalham em sistema fechado, logo o WFS basicamente só mede resíduos

#### Aberrações e polinómios Zernike
- Aberrações são basicamente deviações lead ou lag em relação à aproximação paraxial
![[espelho deformavel.png]]
(ou seja, é o desvio da frente de onda em comparação a uma frente de onda paraxial)
- Consideramos $W(x,y)$ como sendo a diferença de caminho ótico entre a frente de onda real e a frente de onda paraxial (em $\mu\text{m}$) (abaixo vemos como funciona o sensor de frente de onda e vamos entender melhor isto). Podemos relacioná-la com a fase: $$\phi(x,y)=\frac{2\pi}{\lambda}W(x,y)$$
- Os polinómios de Zernike são uma base completa e ortogonal de funções que cobrem o circulo unitário. Eles são muito úteis porque os termos de menor ordem coincidem com aberrações comuns. Eles consistem em produtos de fatores de normalização, poilnómios radiais e funções azimutais
$$Z_{j}(\rho,\theta)=Z_{n}^{m}(\rho,\theta)=\begin{cases}
&\sqrt{2n+1}R_{n}^{m}(\rho)\cos(m\theta)&,~~ m\neq0~,~j\text{ par} \\
&\sqrt{2n+1}R_{n}^{m}(\rho)\sin(m\theta)&,~~ m\neq0~,~j\text{ par} \\
&\sqrt{2n+1}R_{n}^{m}(\rho)&,~~ m=0
\end{cases}$$
$n,m$ são o gra bu radial do polinómio e a frequência azimutal. O $j$ é o índice de Noll, que é simplesmente o esquema de indexação usado aqui
- O polinómio radial acima é assim:
$$R_{n}^{m}(\rho)=\sum\limits_{s=0}^{\frac{n-m}{2}}\frac{(-1)^{s}(n-s)!}{s!\left(\frac{n+m}{2} \right)! (\frac{n-m}{2}-s)!}\rho^{n-2s}$$
- Como os polinómios Zernike formam uma base, temos:
$$W(x,y)=W(\rho,\theta)=\sum\limits_{j=1}^{\infty}a_{j}Z_{j}(\rho,\theta)$$

#### WFS de Shack-Hartmann (SHWFS)
- Consiste num array 2D de microlentes. O pitch (espaçamento) das microlentes deve ser pequenos o suficiente para o sampling detetar as aberrações
- Temos este funcionamento:
![[shfws.png]]
basicamente, as lentes focam os feixes e enviam-no para detetores. Assim, estamos a fazer sampling da frente de onda com um sistema ótico!
- A distância a que um ponto se encontra do equivalente numa onda plana chama-se *gradiente / slope*.

**Uma lente**
- Para uma onda com aberração $W$, podemos aproximar a onda que chega a cada lente como uma onda plana *inclinada* (isto se a lente for menor em diametros do que a escala espacial da aberração). 
- O ponto focado está desviado do eixo de propagação (o ponto equivalente de uma onda plana) em uma distância $\delta y$:
![[espelho deformavel 2.png]]
e temos $$\tan\alpha=\frac{\delta y}{f_{ML}}=\frac{\Delta z}{\Delta y}$$
temos que $f_{ML}$ é a distância focal da microlente. Obtemos estas 2 igualdades ao ver os triângulos à direita e à esquerda da lente, respetivamente. 
- Como $z$ não é nada mais que a aberração em si, temos:
$$\tan\alpha=\frac{\partial W}{\partial y}$$
que nos dá:
$$\Delta W(x,y)=\frac{\delta x \delta y}{f_{ML}}$$

#### Reconstrução da frente de onda
- Conseguimos reconstruir a frente de onda a menos de uma constante. Esta não faz diferença em termos de imagem da frente, mas é crítico no que tocaria a inferometria
- As medições do SHWFS podem ser modeladas de forma linear:
$$\mathbf{s}=\mathbf{Ga}+\boldsymbol{\eta}$$
em que $\textbf{s}$ contém os slopes, $\boldsymbol{\eta}$ contem o ruído e $\textbf{a}$ é o vetor de coeficientes de Zernike que descrevem a onda. $\textbf{G}$ é a matriz que tem os slopes medidos no SHWFS na coluna de cada polinómio da base. 
- Basicamente: $\mathbf{G}$ tem forma $m\times N$ em que temos $m$ medições por função e usamos uma base com $N$ funções da base Zernike. Assim, $\mathbf{a}$ é um vetor com $N$ elementos - os coeficientes da $N$ funções base usadas. $\mathbf{s},\boldsymbol{\eta}$ serão vetores de $n$ elementos.

- Isto acima é o modelo teorico. Tendo as medições $\mathbf{s}$, podemos determinar a onda usando uma approach de least squares:
$$\mathbf{b}=\mathbf{H}\mathbf{s}$$
em que $\mathbf{b}$ é um vetor com coeficientes de Zernike e  $\mathbf{H}$ a matriz de reconstrução. Na maneira mais simples, definimos:
$$\mathbf{H}=(\mathbf{GG}^{T})^{-1}\mathbf{G}^{T}$$
- Ou seja, sabemos $\mathbf{s}$ porque são medições. Se determinarmos $\mathbf{H}$, temos $\mathbf{b}$. Como $\mathbf{b}$ são os coeficientes da base Zernike, temos a frente de onda.

### Setup
![[montagem t3o.png]]
- Este setup baseia-se no kit da Thorlabs.
- As lentes e espelhos estão montados num sistema de cage (gaiola?), que garante caminhos óticos constantes e bem conhecidos:
![[sistema de cage.png]]
- Esta configuração está feita de modo que o SHWFS, o DM e a saída do Laser (LS) estejam em planos óticos conjugados.
- São usaadas lentes com distância focal 75mm
- O X marca onde são colocadas amostras

### Aquisição de dados
1. Iniciar o software do SHWFS. *Depois*, lançar o software do AO-kit : AOkit2. O primeiro controla o SHWFS (lol) e o segundo o DM
2. Verificar o alinhamento do feixe. Em princípio tudo estará minimamente OK e basta mover a montagem de translação mais próxima do SHWFS até a distância PV (peak to valley) for abaixo de 0.3um
3. Verificar o alinhamento da pupila do SHWFS com o DM. No Aokit2, mover os atuadores centrais para desvio de 3um e observar a imagem da frente de onda no software do SHWFS. Ajustar a posição da pupila do SHWFS para a aberração estar no centro.
4. Colocar o diametro da pupila a 2mm no software SHWFS
5. Criar pasta para guardar ficheiros. 
6. No AOkit2, carregar Z2_Nools.spf que tem valores de desvio proporcionais ao polinómio de Zernike $Z_{2}$. 
7. No software do SHWFS guardar a frente de onda e os centroids
8. No AOkit2, colocar o espelho plano e  guardar novamente os dados no software SHWFS - isto serão as posições de referência
9. Repetir 6-8 para polinómios até $Z_{10}$ (ou $Z_{15}$ se possível)
![[software espelho deformavel.png]]
![[software shfws.png]]

#### Análise
- Queremos reconstruir a frente de onda a partir das medições. Precisamos então de um reconstrutor  $\mathbf{H}$
- Ele pode ser obtido das medições em si, usando um modelo físico-ótico AKA uma simulação do SHWFS.
    - Isto será em python usando as packages de ótica adaptativa SOAPY, AOTOOLS
- Seguir o guião, em que tem o passo a passo