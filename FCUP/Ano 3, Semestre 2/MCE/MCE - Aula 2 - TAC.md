 - Um Raio X funciona da seguinte forma:
![[tac.png]]
um TAC funciona de forma semelhante: um sinal é lançado de um ponto, atravessa o paciente e é detetado do outro lado. Consoante variamos o ponto inicial, obtemos diferentes imagens. No final, isto permite obter uma imagem 2D ou 3D do interior do paciente, devido às reações dos difer

### Lei de Beer
$$I_{d}=I_{0}\exp\left[-\int_{0}^{d}\mu(x,E)ds\right]$$
em que obtemos $$\int_{0}^{d}\mu(s,E)ds=\log(I_{d}/I_{0})$$
ou seja, num TAC ou semelhantes exames estamos a obter dados que constituem a solução deste integral de linha de $\mu$. $\mu$ é o coeficiente de atenuação linear.
- De seguida usaremos $f(x,y)$ para representar $\mu(s,E)$ e $p(s,\phi)$ para $\log(I_{d}/I_{0})$. Queremos determinar $f$ conhecendo $p$

### Projeções e Mapas
- Temos um parque com 2 árvores. Queremos fazer uma mapa dele. As ávores estão alinhadas com sul:
![[pontos vista imagem.png|425]]

- Consideremos agora que elas não estão alinhadas com sul, mas sim com um eixo que faz 45º com Sul. A partir das fotos de Sul e Este apenas podemos concluir que teremos 1 destas distribuições:
![[pontos vista imagem 2.png]]

- Um TAC basicamente projeta uma cena 3D num plano 2D. O integral de linha que vimos também projeta num ponto:
![[projeçao de objeto 2D.png]]
- Sendo que o detetor nos dá um valor máximo onde $t$ é superior. Ou seja, fora da circunferência obtemos $s=0$. Vejamos uma imagem:
![[projeçao de objeto 2D 2.png]]
- Aqui notemos que o que se obtém na análise de 1 ponto de vista é uma função 1D $p(s)$.

- Consideremos agora um sistema não isotrópico (ângulo de onde vemos importa):
![[projecao de  2 objetos em 2 direcoes diferentes.png]]
- Aqui percebemos ainda o que significa $\phi$ em $s(p,\phi)$: é o ângulo de onde observamos o sistema.

### Caso Pontual
![[projecao ponto.png]]
- Para algo assim teremos sempre $s=r\sin\phi$. 
- Assim, se traçarmos $p(s,\phi)$ obtemos um Seno. Se representarmos os senos de muitos ângulos $\phi$ juntos temos um *sinograma*:
![[Pasted image 20240319225848.png|450]]

### EX
![[sinograma.png]]
em que temos:
![[sinograma eqs.png]]
- Agora é preciso pegar nos dados do sinograma e conseguir obter uma imagem!

## 2 - Retroprojeção
![[retroprojecao.png]]
- O problema de fazer retroprojeção é que os dados $p(s,\phi)$ consistem num valor total ao longo de toda uma direção $\phi$, pelo que perdemos informação sobre a distribuição dos dados nessa mesma direção. Deste modo, simplesmente definimos todas as linhas dessa direção com um mesmo valor.
- Repetimos para todos os $\phi$

### 2.1 - Exemplo
- Temo uma imagem de 4 pixeis:
 ![[tac processo 1.png|300]]
- Fazemos scan da imagem das direções de $0,45,90,135$ graus:
![[tac processo 2.png|300]]
- Estes são os dados $p(s,\phi)$ que temos.

- Consideremos o contrário: temos os $s$ e queremos obter a imagem.
- Definimos então todos os pontos de cada direção iguais e somamos tudo e temos:
![[tac processo 3.png]]
Evidentemente, temos 4 vezes cada valores no respetivo pixel. Podemos então normalizar e obter a configuração anterior.

## 2.2 - Caso pontual (2)
![[tac de ponto processo.png]]
- Considerando $r=1$ (distância do ponto à origem) vemos que ocorre o que temos acima.
- Conforme somamos as imagens de cada detetor temos:
![[tac aumentar direcoes.png]]

- Um caso standard é:
![[shepp logan.png]]
que é usado para fazer scan da imagem e respetivas retroprojeções.
Consoante vamos fazeendo mais scans:
![[retroprojecao passos 1.png|225]] ![[retroprojecao passos 2.png|218]] ![[retroprojecao passos 3.png|220]]
- Vemos portanto que retroprojeção é um método fraco para obter detalhes.

## 3 - Transformada de Radon
$$p(s,\phi)=\int_{-\infty}^{+\infty}dx\int_{-\infty}^{+\infty}dy~f(s,y)\cdot \delta(x\cos\phi+y\sin\phi-s)$$
em que o delta de Kronecker efetivamente faz a mudança de referencial:
![[projecao 2.png]]
$$s=xcos\phi+y\cos\phi$$
- A transformada invera será:
$$b(x,y)=\int^{\pi}p(s,\phi)|_{x\cos\phi+y\sin\phi}d\phi$$
em que temos:
$$b(x,y)=f(x,y)\times \frac{1}{\sqrt{x^{2}+y^{2}}}$$

### 3.1 - Propriedades
![[propriedades radon.png]]

### 3.2 - Teorema da Fatia Central
$$\mathcal{F}_{1}[p(s,\phi')]=\mathcal{F}_{2}[f(x,y)]_{|\phi=\phi'}$$
ou seja a FT 1D de $p$ (função 1D) é igual à fatia da FT 2D de $f$ (função 2D) em que $\phi=\phi'$

- Em imagens
![[teorema fatia central.png]]
- Isto significa que podemos saltar entre $p$ e $s$ usando FTs e IFTs.
- Consoante variamos $\phi$ e medimos $\phi$ o gráfico de Fourier efetivamente encontra-se numa grelha polar:
![[ref polar para cartesiano.png]]
o que resulta numa imagem pouco focada e com poucos detalhes: temos valores muito elevados no centro (frequências baixas) mas poucos em frequências altas

# 4 - Retroprojeção Filtrada
- Simplesmente fazemos FT de $p$:
$$\mathcal{F}[p(s)]=P(\omega)=\frac{1}{2\pi}\int_{-\infty}^{+\infty}p(s)e^{-i\omega s}ds$$
- Podemos ainda escrever:
$$f(x,y)=\mathcal{F}_{2}^{-1}(F(v_{s},v_{y}))=\int_{-\infty}^{+\infty}dv_{x}\int_{-\infty}^{+\infty}dv_{y}~F(v_{x},v_{y})e^{-i2\pi(x_{x}xv_{y}y )}$$
($v_{x},v_{y}$ são as frequências no espaço da FT 2D)
Passando para coordenadas polares:
![[demonstracao teorema fatia central.png]]
- Isto resulta na filtragem da retroespação, em que as frequências baixas são reduzidas, sendo $v_{x}=v_{y}=0$

### Receita
- Procedemos então na forma:
    1. Fazer FT da projeção: $\mathcal{F}[p(s,\phi_{1})]=P(\omega)$
    2. Multiplicar o filtro pela função rampa: $|\omega|P(\omega)$
    3. Fazer IFT deste produto: $(\int_{-\infty}^{+\infty}d\omega |\omega|e^{i2\pi\omega s})_{s=x\cos\phi+y\cos\phi}$
    4. Fazer retroprojeção desta função: $\int_{0}^{\pi}d\phi(\int_{-\infty}^{+\infty}d\omega |\omega|e^{i2\pi\omega s})_{s=x\cos\phi+y\cos\phi}$ 

- Temos então a sequência:
![[retroprojecao filtrada processo.png]]

e podemos ver retroprojeção filtrada e não filtrada lado a lado:
![[retroprojecao filtrada.png|200]] ![[retroprojecao nao filtrada.png|194]]

## 5 - Agora na prática
- A matriz que usamos tem que ter tamanho suficiente de forma que ao analisar a imagem na diagonal não cortamos a imagem (se a imagem mede 2x2, a matriz que usamos tem que ter elementos correspondentes a um comprimento de pelo menos $\sqrt{8}$).
- Percorremos cada linha perpendicular ao detetor (por exemplo, percorrer yy para detetor na horizontal)
- O sinograma consiste em uma lista de valores $s$ para um certo $\phi$
- Para obter a imagem por retro projeção, traçamos numa imagem todos os valores de $s$ para todos os $\phi$: usamos $s=x\cos\phi+y\sin\phi$ para decidir a posição dos pontos na imagem.

### Python
- Ver muito bem o jupyter que o prof vai colocar no moodle
- Usamos `np.pad` ou algo similar para fazer a matriz.
- Podemos usar `plt.pcolor(xx,yy,img)` ou imshow, em que `img` é a matriz que contém a imagem.
- Usamos a função `rotate` do módulo `skimage`
- Não consigo explicar muito melhor em texto, vê o jupyter.