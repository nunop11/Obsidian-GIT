###### Aula 5 - 5/3/2024
# Modelo de Sommerfeld
- Este modelo assume que os eletrões num metal seguem a estatística de Fermi:
$$f(\varepsilon)=\frac{1}{e^{\frac{\varepsilon-\varepsilon_{0}}{k_{B}T}}+1} $$
e segue a ESIT:
$$- \frac{\hbar^{2}}{2m} \nabla^{2} \psi=\varepsilon \psi$$
- Para soluções, podemos facilmente obter ondas planas:
$$\psi(\vec{r})=A e^{i\vec{k}\cdot\vec{r}}$$

**Metal**
- Temos uma peça de metal paralelepípeda de volume $V$ e dimensões $L_{x},L_{y},L_{z}$ que são muito elevadas comparadas com as dimensões interatómicas : $L_{x},L_{y},L_{z}\gg a\sim 10\dot{A}$
    - De notar que estes comprimentos têm que ser muito elevados para o que vamos fazer de seguida. Senão, surgem termos extrinsecos ao metal e que dependem da geometria.
    - Sendo estes valores muito elevados podemos considerar a geometria irrelavante 

**Fronteiras Cíclicas**
- Poderíamos achar que as melhores condições de fronteira para este modelo são as condições de fronteira do poço infinito: $\psi(L_{x},y,z)=\psi(x,L_{y},z)=\psi(x,y,L_{z})=0$. Mas estas têm o problema que apenas permitem ondas estacionárias como solução, algo que nos limita bastante.
- Assim, as condições de fronteira que iremos considerar são *cíclicas*. Na prática isto significa que podemos fazer translação da função em qualquer direção $x,y,z$ e temos continuidade: $$\psi(x,y,z)=\psi(x+L_{x},y,z)=\psi(x,y+L_{y},z)=\psi(x,y,z+L_{z})$$
que batem certo com o facto que o Hamiltoniano do sistema não depende da posição AKA é imune a translação.

- Notas sobre estas condições de fronteira:
    - Em 1D podemos entender estas condições como: 
        - Consideremos uma onda que é retilinia num segmento $\left[0,L_{x}\right]$
        - Se aplicarmos estas condições de fronteira, temos que esta onda pode ser atuada de translações 
        - A única forma de atuarmos um segmento de reta de translações e obtermos sempre algo contínuo é se ele pertencer a um anel.
        - Ou seja, em 1D podemos considerar estas condições de fronteira como transformar uma onda 1D numa secção de um anel 2D.
    - Em 2D e 3D é bastante mais abstrato. A lógica é que: mal um corpo passa para fora da fronteira num direção $i$, ele volta logo para $i=0$. 
    - Por exemplo, sendo um caso 1D com $L=5$, teremos $\psi(2)=\psi(7)=\psi(12)$
    - Estas fronteiras foram sugeridas por Max Born e bastante discutidas. Mas o que precisamos de reter é que:
        - Elas consistem em termos que a onda não é limitada e propaga-se infinitamente
        - No final de contas, a interpretação física destas fronteiras não importam porque funciona :D

**k quantificado**
- Como sabemos, para a ESIT deste tipo temos: $\varepsilon(\vec{k})=\frac{\hbar^{2}k^{2}}{2m}$
- Podemos escrever: $$e^{ik_{x}L}=e^{ik_{y}L}=e^{ik_{z}L}=1$$
porque apenas se isto for verdade temos:
$$k_{x}=n_{x}\frac{2\pi}{L} \quad;\quad k_{y}=n_{y}\frac{2\pi}{L} \quad;\quad k_{z}=n_{z}\frac{2\pi}{L} \quad \quad;~~ n_{i}\in\mathbb{Z},\forall i$$
porque $e^{z}=1$ só se $z=2\pi n i$. Isto vem da condição de fronteira aplicadas à onda plana.
- Podemos verificar isto:
$$\begin{align*}
\psi_{\vec{k}}(x,y,z)&= e^{i(k_{x}x+k_{y}y+k_{z}z)}\\
\psi(x+L,y,z)&= e^{i(k_{x}(x+L)+k_{y}y+k_{z}z)}=e^{ik_{x}L}\psi_\vec{k}(x,y,z)
\end{align*}$$

**Espaço de k's**
- Podemos fazer a seguinte figura, em que vemos que os k's possíveis para um certo problema:
![[grelha k's]]
- Cada ponto $(k_{x},k_{y})$ é um *estado*. Obviamente, não podemos ter eletrões nos espaço entre pontos.
- Temos $\varepsilon(k_{x},k_{y})=\frac{\hbar^{2}}{2m}(k_{x}^{2}+k_{y}^{2})$ pelo que em cada estado podemos ter 2 eletrões, com spins opostos.
- Vamos aqui definir uma nomenclatura:
    - *Espaço real* - espaço em que os eletrões existem (com x e y)
    - *Espaço recíproco* - espaço dos k's (recíproco do real)

- Como neste cenário temos $L_{i}\gg a$ então temos muitos valores de k que estão muito próximos. Isto vai-nos permitir obter resultados interessantes. 
    - Por exemplo, num metal, por unidade de volume, temos $\sim10^{22}$ eletrões. Estando 2 eletrões em cada estado, teremos $10^{22}$ k's. Mesmo que a distância entre 2 pontos seja 1cm ou até 1m; a esta escala essa distância é irrelavante.

**Momento**
- Sabemos que o momento linear de um eletrão com um vetor $\vec{k}$ será dado por $$\vec{p}=\hbar\vec{k}$$
de onde vemos que a velocidade será $\vec{v}=\frac{\hbar}{m}\vec{k}$
- Ou seja, o operador momento linear $\hat{P}=\frac{\hbar}{i}\nabla$ tem os valores próprios $\hbar \vec{k}$:
$$\hat{P}\psi=\frac{\hbar}{i}\nabla e^{i\vec{k}\cdot\vec{r}}=\hbar\vec{k}e^{i\vec{k}\cdot\vec{r}}=\hbar\vec{k}\psi$$
- Ou seja, podemos interpretar os k's como vetores de onda

**Volume no espaço recíproco**
- Conseguimos marcar uma região em torno de um estado:
![[grelha k's 2]]

- Ora, este quadrado terá área $(2\pi/L)^{2}$ pois $k_{i+1}-k_{i}=2\pi/L$. 
- Num caso em 3D teríamos um volume $(2\pi/L)^{3}$

- Assim, consideremos um volume genérico $\Omega$ do espaço recíproco.
- Nesse volume vamos ter $\frac{\Omega}{(\frac{2\pi}{L})^{3}}$ estados. Ora:
$$\frac{\Omega}{(\frac{2\pi}{L})^{3}}=\frac{\Omega}{8\pi^{3}}L^{3}=\frac{V}{8\pi^{3}}\Omega$$
ou seja, $V/8\pi^{3}$ é a densidade volúmica de estados neste espaço.
    - Aqui devemos notar algo: Na teoria temos $\frac{2\pi}{L_{x}}\frac{2\pi}{L_{y}}\frac{2\pi}{L_{z}}$ ou seja, a grelha poderia não ser quadrada e não teríamos superfícies esféricas de raio $k$. Mas na realidade podemos considerar que as distâncias entre pontos é tão baixa que mais uma vez podemos aproximar a uma grelha quadrada com esferas.
    - Isto vem em parte do facto que podemos ignorar os efeitos da fronteira (para já pelo menos). Eles só são impossíveis de desprezar quando o volume é reduzido. Aí também não podemos aproximar a grelha a grelha quadrada nem ignorar a geometria do metal.
- Podemos ainda dizer que temos $2\frac{\Omega}{\left(\frac{2\pi}{L}\right)^{3}}$ *estados eletrónicos* no volume $\Omega$

### Exemplo - $T=0$
- Temos uma estatística de Fermi
- Consideremos que temos $T=0$ e temos 6 eletrões para distribuir pelos estados. Consideremos o espaço recíproco 2D da figura acima.
    1. Começamos por colocar 2 eletrões no espaço central $(0,0)$
    2. Os espaços $(1,0);(0,1);(-1,0);(0,-1)$ têm todos a mesma energia então colocamos 1 eletrão em cada (todos com spin $\uparrow$)

- Consideremos agora $N$ eletrões. Consoante vamos acrescentando eletrões temos as linahs que unem estados com a mesma energia:
![[grelha k's 3]]

- Consoante vamos tendo $N$ maior e maior, voltamos ao que vimos acima: os pontos estão muito próximos. Assim, podemos aproximar as linhas que unem estados com energias idênticas a **circunferências**! (superfícies esféricas em 3D)

**Energia de Fermi**
- Assim, temos muitas circunferências concentricas. Podemos então definir o 1º raio que *não* é ocupado. A esse raio chamamos de **vetor de onda de Fermi** $k_{F}$. Ora, este corresponde à **energia de Fermi**. A superfície delineada é a *superfície de Fermi*
- Esse raio corresponderá ao volume: $$\Omega=\frac{4}{3}\pi k_{F}^{3}$$
- Assim, podemos escrever a seguinte:
$$2\times\frac{\frac{4}{3}\pi k_{F}^{3}}{\left(\frac{2\pi}{L}\right)^{3}}=N~~\to~~ N=\frac{k_{F}^{3}L^{3}}{3\pi^{2}}$$
ou seja:
    - o termo $\Omega/(2\pi/L)^{3}$ dá-nos, como já vimos, o número de estados contidos em $\Omega$
    - multiplicamos por 2, assumindo que *todos os níveis estão preenchidos*, tendo-se 2 eletrões em cada

- Podemos então escrever:
$$n=\frac{N}{V}=\frac{k_{F}^{3}}{3\pi^{2}}~\to~k_{F}^{3}=2\pi^{2}n$$
logo
$$\varepsilon_{F}=\frac{\hbar^{2}k_{F}^{2}}{2m}=\frac{\hbar^{2}}{2m}(3\pi^{2} n)^{\frac{2}{3}}$$
