## Micro magnetismo
- Consideremos apenas ferromagnets e iremos aproximar o sistema a algo contínuo.
- Neste tipo de material os momentos magnéticos tendem a alinhar
- Temos:
$$\vec{M}(\vec{r},t)=M_{S}(\vec{r})\vec{m}(\vec{r},t)$$

em que $M$ é a magnetização do material, $M_{S}$ o campo de magnetização saturada e $m$ um vetor que indica a direção da polarização num ponto num certo instante.
![[tipos magnetizacao.png]]

- Na framework de micro magnetismo temos 2 objetivos:
![[objetivos mumax.png]]

- A dinâmica da magnetização é descrita pela equação LLG:
$$\dot{\vec{m}}=- \frac{\gamma}{1+\alpha^{2}} \left( \vec{m} \times \vec{H}_{eff} + \alpha \vec{m} \times (\vec{m} \times \vec{H}_{eff}) \right) \quad;\quad \vec{H}_{eff}=\frac{-1}{\mu_{0}M_{s}}\frac{\partial E}{\partial \vec{m}}$$
ou:
$$\frac{\partial\vec{m}}{\partial t}=- \gamma' (\vec{m} \times \vec{H}_{eff}) - \alpha' \vec{m} \times (\vec{m} \times \vec{H}_{eff})$$
em que
$$\gamma'=\frac{\gamma}{1+\alpha^{2}} ~~;~~ \alpha'=\gamma'\alpha~~;~~\vec{H}_{eff}=\frac{-1}{\mu_{0}M_{S}}\frac{\partial E}{\partial \vec{m}} $$

- O termo $\vec{m}\times\vec{H}_{eff}$ descreve a *rotação/evolução* da magnetização em torno de Heff. O termo $\alpha \vec{m} \times (\vec{m} \times \vec{H}_{eff})$ é o *damping* da magnetização.
    - Temos então  um movimento em espiral da ponta da magnetização:
![[evolucao magnet.png]]
- A fórmula do campo efetivo tem $\delta E/\delta \vec{m}$ que é a *derivada funcional* da energia
- Para resolver/estudar isto determinamos a fórmula da energia total (de forma analítica). Com isso, fazemos a derivada e temos $\vec{H}_{eff}$. Com essa, determinamos a solução da LLG computacionalmente.

### Adaptações
1. Podemos ter a existência de torques de *transferência de spin*:
$$\dot{\vec{m}}=- \frac{\gamma}{1+\alpha^{2}} \left( \vec{m} \times \vec{H}_{eff} + \alpha \vec{m} \times (\vec{m} \times \vec{H}_{eff}) \right) + \tau_{STT}$$
1. Podemos ter um termo extra no campo efetivo que escala com a temperatura:
$$\vec{H}_{eff}\to \vec{H}_{eff} + \vec{H}_{th} \quad;\quad \begin{align*}
\langle \vec{H}_{th}(\vec{r},t)\rangle&= 0\\
\langle \vec{H}_{th}(\vec{r},t),\vec{H}_{th}(\vec{r'},t')\rangle &= \frac{2k_{B}T \alpha}{M_{s}\gamma}\delta(\vec{r}-\vec{r'})\delta(t-t')
\end{align*}$$

### Minimizar energia
- Temos 2 principais abordagens para minimizar a energia livre de forma numérica:
    1. Um método de minimização normal (descida de gradiente)
    2. LLG com um damping forte : remover o outro termo por completo. Ou seja: $$\dot{\vec{m}}=- \vec{m}\times(\vec{m}\times\vec{H}_{eff})$$

## MuMax3
- Package gratuito que simula micro magnetismo com um método de diferenças finitas
- Acelerado por GPU NVidia
- Usam-se kernels NVidia CUDA
- Tem uma linguagem de script e um GUI web para ver o output

### Código
- A linguagem do Mumax3 é um subset de *golang*:
```go
// definir magnetização de saturação 
Msat = 5e6

// definir uma nova variável
Freq := 1e9

for ( i := 0; i<10; i++) {
    print(i)
}

if 1+8 == 9 {
    print("Of course 1+8=9")
}
```
De notar aqui que `:=` define uma nova variável com um certo valor. Por outro lado, `=` atribui um novo valor a uma variável já existente.

### Discretização
- Começamos por criar uma caixa retangular de simulação, em que a origem se encontra no centro 
- Temos uma grid de células. Notas:
    - Todas as células são *iguais*
    - Dentro de 1 célula, temos uma magnetização uniforme (toda a célula tem 1 só vetor de magnetização)
- O tamanho da célula normalmente deve ser inferior ao exchange length (?). Definimos assim:
```go
setgridsize(256, 64, 1)
setcellsize(1e-9, 1e-9, 1e-9)
```
como é óbvio, quanto menor o tamanho da célula maior será a precisão mas pior a performance.
- Temos ainda os valores PBC (periodic boundary conditions) que é o número de repetições usadas para calcular interações dipolares:
```go
setpbc(4,0,0)
```

- A biblioteca FFT do CUDA está altamente optimizado para dimensões da grid que tenham fatores primos pequenos:
![[performance mumax3.png]]
- Ou seja, devemos usar dimensões em cada dimensão que sejam *7-smooth*
    - Um número $n$-smooth é um número em que todos os fatores primos são $<n$
    - Ou seja: $192=2^{6}\times3$ é 7-smooth. Já $190=2\times5\times19$ não é.


### Shape
- Uma shape é só uma função
- Podemos considerar uma função $f:\mathbb{R}^{3}\to \{\text{true},\text{false}\}$  em que:
$$f(x,y,z)=\begin{cases}
\text{true} &; &(x,y,z)\in\text{shape} \\
\text{false} &; &\text{restantes casos}
\end{cases}$$
- Por default, consideramos a shape como estando no centro do universo -  a origem
- Temos um set de shapes pré-definidas
- Podemos criar novas shapes ao combinar e alterar as básicas
- Podem ser usadas para:
    - definir a geometria da amostra
    - marcar regiões
    - Marcar onde temos a magnetização inicial

- Temos aqui um exemplo de como podemos usar shapes para definir um queijo:
![[codigo mumax 1.png]]

- Outra coisa que podemos fazer é criar uma shape (um anel como abaixo) e defini-lo como a geometria da amostra:
![[codigo mumax 2.png]]

### Regions
- Temos 256 regiões (de 0 a 255)
- Cada célula está associada a uma só região (que por default é a região 0)
- Em cada região temos uma série de parâmetros físicos
    - Ao atribuir células a diversas regiões podemos simular uma amostra não homogénea 
- Podemos definir a região de 1 só célula ou de todas as células dentro de uma shape:
![[codigo mumax 3.png]]

### Parâmetros materiais
- Atribuidos às 256 regiões, como acabamos de ver
- Podem ser funçõs temporais
- Podem ser escalares ou vetoriais
- São todos pré-definidos e não podemos criar novos
![[codigo mumax 4.png]]
- Aqui temos:
    - No `Msat` temos apenas `=`, o que faz com que se altere a magnetização de saturação em todas as 256 regiões
    - Também em `AnisU` alteramos o vetor unitário de anisotropia de todas as regiões
    - Na porção do centro do exemplo, alteramos `Msat` para as regiões 0 e 1, uma de cada vez, dando-lhes os valores 800e3 e 540e3
    - Finalmente, definimos `Ku1` (constante de anisotropia uniaxial) como sendo uma função sinusoidal
    - `t` é uma variável interna do Mumax3 que é o tempo

#### Excitações
- Uma excitação é um parâmetro material *regional*
- Adicionalmente, podemos adicionar um certo número de campos vetoriais dependentes de tempo e espaço da forma $g(x,y,z)f(t)$ - temos que poder separar o tempo.
- Um exemplo que temos:
![[codigo mumax 5.png]]
- A um vetor `B_ext` adicionamos um campo externo que vem de um ficheiro "antenna.ovf". Isto permite formar excitações complexas
- O `removeExtraTerms` remove os termos que adicionamos com `Add`

### Magnetização inicial
- Uma forma de fazer isto é um `config`, que é um objeto que representa a configuração de magnetização:
![[codigo mumax 6.png]]
- Temos:
    - LoadFile - podemos importar uma configuração feita previamente e guardada
    - Podemos definir a magnetização dentro de uma região, shape ou célula.

- Alguns exemplos. Notemos que acima em `config` metemos um vetor ou algo como o que vemos abaixo.
![[codigo mumax 7.png]]

### Output
- Temos 3 outputs:
    - log file - onde são feitos inputs, logs e prints
    - table.txt - permite guardar os dados que quisermos em formato de tabela 
    - ![[codigo mumax 8.png]]
    - ficheiros ".ovf" - campos escalares e vetoriais. Ou seja, podemos guardar o ficheiro.
    - ![[codigo mumax 9.png]]

### Funcionamento
![[codigo mumax 10.png]]

### Desmagnetização
![[codigo mumax 11.png]]

### Exchange Field
![[codigo mumax 12.png]]

### Termo de anisotropia de campo
![[codigo mumax 13.png]]

### Termo de campo de Dzyaloshinskii-Moriya 
![[codigo mumax 14.png]]

### Termo de campo externo
![[codigo mumax 15.png]]

### Termo de campo térmico
- Isto é um caso que já falamos atrás
![[codigo mumax 16.png]]

### Termo de campo costum
![[codigo mumax 17.png]]

### STT de Zhang-Li
![[codigo mumax 18.png]]

### SST de Slonczewski
![[codigo mumax 19.png]]

