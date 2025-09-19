(Isto foi dado na aula 11)
# Difração de Raios X
- O espetro de emissão $E(\lambda)$ apresenta um traçado suave com picos no meio. Vimos em FModerna a explicação. 
    - Recordemos que os picos se devem a eletrões a descer para níveis menos energéticos e à consequente libertação de energia.
    - Na prática, usam-se filtros, de forma a isolar o *pico mais intenso*. Desta forma, ficamos com um feixe praticamente monocromático. 
        - Isto é bom, mas pode causar complicações se esse comprimento de onda for absorvido pela nossa amostra.

## Difração de Bragg
- Em 1913, Bragg (pai e filho) verificaram que materiais com estruturas cristalinas, quando sujeitos a radiação raio X geram padrões de difração muito específicos.
- Consideremos:
![[difracao bragg.png|600]]
- Ora, assume-se que as redes são "bons espelhos", tendo-se uma reflexão a manter o ângulo de incidência. 
- Assim, temos a diferença nos percursos percorridos:
$$\Delta s= 2d\sin\theta$$

- Mas estamos na *teoria de Bragg*, que introduziu neste caso muito simples algo: temos que ter *interferências construtivas* (que explicam os picos do espetro de emissão). Assim, a diferença de comprimento entre os percursos terá que ser uma *quantidade inteira de comprimentos de onda*:
$$2d\sin\theta=m\lambda~~~~,~~m\in\mathbb{Z}$$
($\theta$ é o ângulo de Bragg e $n$ é a ordem da difração)
- Daqui surge uma coisa importante de notar: se incidir um feixe com vários comprimentos de onda (uma vez que $d$ é constante) eles terão diferentes ângulos de reflexão e/ou ordens de difração.

- Vimos em Ótica (sqn lol) que o padrão de difração corresponde à *transformada de Fourier* do objeto que original essa difração. OU SEJA: quando um feixe é difratado por uma rede de Bravais, o padrão de difração é a *rede recíproca*. -- Teoria de Von Laue, a ver na próxima aula.

###### Aula 12 - 9/4/2024
- Na aula anterior vimos a *difração de Bragg*, que consiste na difração de feixes raio X a serem refletidos em diferentes camadas de uma rede cristalina
- Vejamos agora a teoria que, na opinião do Agostinho, é mais interessante:

## Difração de Von Laue (lê-se Lau-é)
![[reflexao bragg.png|500]]
- Consideremos 2 pontos da grelha. Temos 2 feixes raio X descritos pelo vetor de onda $\vec{k}$ (não tem a ver com Sommerfeld, isto é um vetor de onda *como em ótica*). Consideramos o ângulo de incidência $\theta$.
- Os feixes são refletidos, ficando com vetor de onda $\vec{k'}$ e ângulo $\theta'$
- Considerasse a reflexão perfeita AKA $|\vec{k}|=|\vec{k'}|=2\pi/\lambda$

- Vamos definir os versores das direções de incidência e de reflexão:
$$\hat{n}=\frac{\vec{k}}{k} \quad \quad,\quad \quad \hat{n'}=\frac{\vec{k'}}{k'}$$
- Facilmente vemos que $d\cos\theta=\vec{d}\cdot\hat{n}$ e $d\cos\theta'=-\vec{d}\cdot\hat{n'}$

**Interferência Construtiva**
- Como para Bragg, consideremos que a interferência dos feixes emitidos dos 2 pontos tem que ser *construtiva*
- Assim, novamente consideremos que a diferença de percurso entre os feixes tem que ser igual a uma quantidade inteira de comprimentos de onda:
$$d\cos\theta+d\cos\theta'= \vec{d}\cdot(\hat{n}-\hat{n'})=m\lambda$$
de multiplicarmos os 2 lados por $2\pi/\lambda$ temos:
$$\begin{align*}
\frac{2\pi}{\lambda}~ \vec{d}\cdot(\hat{n}-\hat{n'})&= \frac{2\pi}{\lambda} m\lambda\\
\vec{d}\cdot(\vec{k}- \vec{k'})&= 2\pi m
\end{align*}$$
- Ora, da mesma forma que consideramos $\vec{d}$ podiamos ter usado um *vetor de rede* $\vec{R}$: $$\vec{R}\cdot(\vec{k}-\vec{k'})=2\pi m \quad \Longleftrightarrow\quad  e^{i(\vec{k'}-\vec{k})\cdot \vec{R}}=1$$
- Ora, esta igualdade é quase igual a $e^{i\vec{K}\cdot\vec{R}}=1$, a relação que vimos na aula anterior para definir o vetor da rede de Bravais, $\vec{K}$!
- Assim, temos que ter a **Condição de Laue**: $$\vec{K}=\vec{k}-\vec{k'}$$
logo temos interferência construtiva se $\vec{R}\cdot\vec{K}=2\pi m$
- Ou seja, por palavras, temos difração se a diferença entre os vetores da incidência e reflexão do feixe de raio X for um vetor da rede recíproca!
- De notar que a condição de interferência construtiva de Laue fica:
$$\boxed{\vec{d}\cdot \vec{K}=2\pi m}$$

**Geometricamente**
- Podemos ainda desenvolver:
$$\begin{align*}
\vec{k'}&= \vec{k}- \vec{K}\\
\vec{k'}\cdot\vec{k'}&= (\vec{k}- \vec{K})\cdot (\vec{k}- \vec{K})\\
\cancel{|k'|}&= \cancel{|k|} + K^{2} - 2 \vec{k}\cdot\vec{K}\\
\vec{k}\cdot\vec{K}&= \frac{1}{2} K^{2}\\
\text{proj}_{\hat{u}_{K}}\vec{k}&= \frac{1}{2}K
\end{align*}$$
$$\boxed{\vec{k}\cdot\hat{u}_{K}=\frac{1}{2}K}$$
(em que $\hat{u}_{K}=\vec{K}/K$ é o versor da rede recíproca nesta direção)
- Isto diz-nos que, independentemente do vetor $\vec{k}$, a sua componente na direção do vetor da rede recíproca terá que ser metade do comprimento deste:
![[teorema de laue.png|377]]
- Ou seja, temos que um vetor $\vec{k}$ da onda incidente irá cumprir a condição de Laue (gerar interferência construtiva) se e só se a sua ponta estiver contida no plano que bisseta o vetor da rede recíproca $\vec{K}$ (é perpendicular e divide o vetor a meio). Este plano é o **plano de Bragg**


**Equivalência entre Formulações**
- Se desenharmos a difração vista acima numa rede com planos distanciados de $d_{hkl}$ (usamos os índices para o caso de ter uma rede 3D em que $d_{100},d_{010},d_{001}$ indicam as distâncias entre pontos nas direções x,y,z) vemos que:
![[bragg vs laue.png]]

- Ora, conforme ilustrado, uma vez que $\vec{K}=\vec{k}-\vec{k'}$ e $|k|=|k'|$, vemos que $\vec{K}$ é *perpendicular* ao plano de Reflexão. Ou seja: o plano de Bragg (formulação de Von Laue) é *paralelo* aos planos de reflexão (formulação de Bragg)!!!

- A condição de Laue acima dá-nos que:
$$\vec{d_{hkl}}\cdot\vec{K}=2\pi n~~\to~~ d_{hkl}K\cos\theta=2\pi n~~\to~~ K=\frac{2\pi n}{d_{hkl}}$$
($\vec{K}$ é perpendicular ao plano de reflexão. Teremos $\vec{d}$ a apontar de um ponto de reflexão para outro e portanto paralelo a $\vec{K}$. Assim temos $\cos\theta=1$)

- Mas além disso, como $\vec{K}=\vec{k'}-\vec{k}$ e conforme a imagem acima, temos:
$$K=2k\sin\theta~~\to~~ k\sin\theta=\frac{1}{2}K=\frac{1}{2}\frac{2\pi n}{d_{hkl}}=\frac{\pi n}{d_{hkl}}$$
- Ora, por fim $k=2\pi/\lambda$ logo:
$$k\sin\theta=\frac{\pi n}{d_{hkl}}~~\to~~ 2d_{hkl}\sin \theta=n \lambda$$
E recuperamos então a **Condição de Bragg**!! Assim, verificamos que as 2 formulações são equivalentes.

- Por outras palavras, para uma difração descrita por $2d_{hkl}\sin\theta=n\lambda$ corresponde a uma vetor de onda $K=\frac{2\pi n}{d_{hkl}}$
$$2d_{hkl}\sin\theta=n\lambda~~~~\longleftrightarrow~~~~ K = \frac{2\pi n}{d_{hkl}}$$
- Assim, através de um equilíbrio entre os valores de: distância entre planos, ordem de difração e comprimento de onda; podemos obter uma coisa a partir de outra.
- Por isto, é possível termos uma difração descrita por um vetor $K$ que não passa em nenhum ponto da rede. Isto ocorre quando temos difração de ordem $\neq1$

