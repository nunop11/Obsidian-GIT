# Notas Protocolo
## Intro Teórica
- Um feixe de luz emitido por uma fonte de luz pode ser aproximado a uma onda eletromagnética *plana*. Pode então ser descrito por um campo elétrico e magnético, mutuamente ortogonais e transversais à direção de propagação do feixe.
### Luz Polarizada Linearmente
- Ora, a direção dos campos pode variar (continuando a ser transversal à propagação) ao longo do tempo.
- Ora, se o feixe passar por um polarizador ele transforma-se numa onda linearmente polarizada, ou seja, o vetor $\vec{E}$ fica permanentemente orientado na direção de polarização $\theta$ do polarizador:
![[polarização luz.png]]
e podemos escrever:
$$\vec{E}=(\hat{x}E_{0x}+\hat{y}E_{0y})\cos(kz-\omega t)$$
![[campo eletrico onda componentes.png]]

- Consideremos agora que, após passar no polarizador com direção $\theta$ o feixe passa num polarizador com a direção de um eixo específico, o *Analisador*:
![[luz, polarizador e analisador.png]]
e conforme a geometria temos $$E_{A}=E_{P}\cos\theta$$
logo
$$P_{A}\propto |\vec{E}_{A}|^{2}~~\to~~ P(\theta)=P(0)\cos^{2}\theta$$
esta é a **Lei de Malus**

## Luz Polarizada Elipticamente
- Consideremos que as componentes $x,y$ do campo magnético do feixe inicial podem ser escritas como:
$$\begin{cases}
E_{x}=E_{0x}\cos(kz-\omega t+\phi_{0x}) \\
E_{y}=E_{0y}\cos(kz-\omega t+\phi_{0y})
\end{cases}\to\begin{cases}
E_{x}=E_{0x}\cos(kz-\omega t) \\
E_{y}=E_{0y}\cos(kz-\omega t+\phi)
\end{cases}~~~~(\phi=\phi_{0y}-\phi_{0x})$$
e conseguimos obter:
$$\left(\frac{E_{y}}{E_{0y}}\right)^{2}+ \left(\frac{E_{x}}{E_{0x}}\right)^{2}- \left(\frac{E_{y}}{E_{0y}}\right) \left(\frac{E_{x}}{E_{0x}}\right)\cos\phi=\sin^{2}\phi$$
que representa uma elipse, ou seja, temos um feixe elipticamente polarizado:
![[polarizacao eliptica.png]]
podemos escrever:
$$\tan(2\chi)=\frac{2E_{0x}E_{0y}}{E_{0x}^{2}+E_{0y}^{2}}\cos\phi\tag{1}$$

## Casos Particulares
- Voltemos à definição de uma onda em que as componentes do campo elétrico têm diferença de fase:
$$\begin{cases}
E_{x}=E_{0x}\cos(kz-\omega t) \\
E_{y}=E_{0y}\cos(kz-\omega t+\phi)
\end{cases}~~~~(\phi=\phi_{0y}-\phi_{0x})$$
### Polarização Circular
Ocorre se tivermos
$$\phi=\pm \frac{\pi}{2},\pm \frac{3\pi}{2},\pm \frac{5\pi}{2},\dots$$
e $$E_{0x}=E_{0y}=E_{0}$$
, tendo-se uma onda com polarização circular de amplitude $E_{0}$.

### Polarização Linear
Quando temos
$$\phi=\pm \pi,\pm 3\pi,\pm5\pi\dots$$
a equação 1 fica na forma: 
$$E_{y}=- \frac{E_{0y}}{E_{0x}}E_{x}$$
ou seja, temos polarização Linear.

## Propagação em Meios Óticos Anisotrópicos
- Quando uma onda eletromag plana entre num meio material o seu plano gera uma força e acelera os eletrões. Ora, segundo a física clássica uma carga com aceleração emite radiação $\propto a$.
- Desta forma, quando um feixe atravessa um feio, o feixe resultante é o feixe original sobreposto com MUITAS ondas secundárias.

- Se o meio em questão for homogéneo (com as mesmas propriedades em todo o seu volume) e isotrópico (igual de todas as direções) temos que a forma como o feixe incidente é afetado é dada pela **Lei de Snell**
- Se não for homogéneo, a velocidade do feixe varia ao longo do meio.

- Vejamos o que acontece num meio anisotrópico.
- Um meio destes tem uma estrutura rigida, de uma forma que a liberdade de movimento dos eletrões depende da direção de polarização do campo.
- Ora, quando o campo oscila na direção em que os eletrões têm mais liberdade de movimento, este emitem mais ondas secundárias e temos mais atenuação do feixe incidente e portanto um índice de refração maior: $n_{e}$ ($n$ extraordinário)
- Se o campo oscilar numa direção perpendicular à direção associada ao índice $n_{e}$, então a interação do feixe com o meio é mínima e ele mantem a maioria da sua velocidade; temos $n_{o}$ ($n$ ordinário)

![[meio anisotropico uniaxial.png]]
- Nesta atividade iremos considerar um meio anisotrópico uniaxial, descrito da forma ilustrada acima (a lâmina tem espessura $d$):
    - Um campo polarizado na direção $x$ move-se com velocidade ditada por $n_{o}$
    - Um campo polarizado na direção $z$ move-se com velocidade diada por $n_{e}$ (esta direção é o *eixo ótico do meio uniaxial*)

- À diferença $\Delta n=n_{e}-n_{o}$ chamamos *birrefringência linear do material* e temos:
$$\Delta \phi=\frac{2\pi}{\lambda_{0}}d(n_{e}-n_{o})$$
- Uma lâmina de meio comprimento de onda introduz diferença de fase:
$$\Delta \phi=(2m+1)\pi ~~, ~~ m=0,1,2,3\dots$$
- Uma lâmina de quarto de comprimento de onda introduz:
$$\Delta \phi=(2m+1) \frac{\pi}{2}~~,~~ m=0,1,2,3\dots$$
(De notar que $\Delta\phi$ é a diferença de fase entre o feixe entrar e sair da lâmina)
- Ora, isto diz-nos que um feixe que entra no meio com polarização linear pode sair dele com polarização eliptica
## Dedução de Leis a verificar
### Lei de Malus
![[esquema da t9 - pt1.png]]
- Um feixe entra num polarizador $P$ que tem o eixo de polarização a fazer $\alpha$ com o eixo $x$.
- A seguir temos um analisador $A$ que tem o eixo de polarizaçõ a fazer $\varphi$ com o eixo $x$.
- Sendo $\theta=\varphi-\alpha$ o ângulo entre os eixos dos polarizadores $P,A$ temos:
$$\frac{P(\theta)}{P_{0}}=\cos^{2}\theta$$
($P_{0}=P(\theta=0)$)

### Análise de Luz Polarizada Elipticamente
![[esquema da t9 - pt1 v2.png]]
- Temos o mesmo sistema de acima, mas entre o polarizador e o analisador temos uma lâmina de 1/4 de comprimento de onda $L$, com o eixo a fazer $\beta$ com $P$.
- Ora, se o feixe inicial tiver polarização linear e $\beta=45º$ (ver acima) temos que o feixe que sai de $L$ tem polarização circular. Nesse caso, o ângulo $\theta$ já não importa, porque o feixe emitido em $L$ passa a ser igual em todas as direções.
- Se tivermos $\beta\neq45º$, deixa de haver esta indepêndencia de $\theta$ e temos que no final a potência é do tipo $P(\theta,\beta)$. Para estudar esta relação considerasse um esquema do tipo:
![[referencial 2 da t9, pt2.png]]
em que o sistema de coordenadas está alinhado com o eixo rápido e lento da lâmina anisotrópica.

- Sendo $E_{0}$ a amplitude do feixe linear que sai de $P$ temos:
$$E_{0\eta_{1}}=E_{0}\cos\beta \quad \quad;\quad \quad E_{0\eta_{2}}=E_{0}\sin\beta$$
daqui podemos obter:
$$P_{A}=\frac{P_{0}}{2}[\cos^{2}\theta+\cos^{2}(2\beta-\theta)] \quad;\quad P_{0}=aE_{0}^{2}$$
($a$ é uma constante)

## Medida da Intensidade Ótica
- Quando um fotodetetor recebe um sinal ótico, este tem 2 componentes: o sinal em si e a luz ambiente, que podemos considerar ruido.
- Uma forma de reduzir esta segunda componente é modular o sinal usando um chopper. Nas partes do sinal em que o sinal "corta" apenas é detetado o ruido.
- Estando o chopper a fazer o sinal oscilar conforme uma onda quadrada de frequência $f$ temos que a Potencia que dele sai é:
$$P(t)=P_{0}s_{f}(t)$$
e a tensão detetada no fotodetetor é $$V(t)=\eta P_{0}s_{f}(t)$$
a que se adiciona um termo $$V_{amb}(t)=\eta P_{amb}(t)$$
- Após uma expansão em série de Fourier e se o feixe passar por um filtro de banda centrado na frequência $\omega$ temos:
$$V_{det}(t)=\frac{2\eta P_{0}}{\pi}\sin\omega t$$
o que nos permite obter $V_{0}=\eta P_{0}$

---
## Velocidade da Luz
### Determinação de $c$ por modulação da intensidade otica
- Temos um feixe ser emitido com potencia $P_{0}$. Esse feixe é modulado por uma função cosseno com profundidade de modulação $\Delta P_{0}$ e frequência $f_{m}$. Fica-se com:
$$P(t,z)=P_{0}+\Delta P\cos\left(2\pi f_{m}t- \frac{2\pi}{\Lambda}z+\phi_{0}\right)$$
em que $\Lambda$ é a distância entre 2 máximo consecutivos.
- Assim:
$$\Lambda=\frac{c}{f_{m}}$$
- No fotodetetor isto é detetado como $$V(t,z)=V_{0}+\Delta V\cos \left(2\pi f_{m}t- \frac{2\pi}{\Lambda}z+\phi_{0}\right)$$
e a diferença de faze entre 2 pontos $z_{1},z_{2}$ tais que $L=z_{2}-z_{1}$ é $$\Delta \phi=\frac{2\pi f_{m}}{c}L$$
o que nos permite obter
$$c=2\pi f_{m} \left(\frac{L}{\Delta\phi} \right)$$

- Para que $\Delta \phi$ tenha um valor não residual, é preciso que $f_{m},L$ ou ambos tenham valores significativos. Assim, nesta atividade iremos usar $f_{m}=60MHz$. Essa frequência já torna $\Delta\phi$ "decente", mas torna limitado o equipamento que se pode usar.
- Para evitar esta situação fazemos **HETERO**dinagem:
![[esquema da parte 2 da t9.png]]
- Devido a uma dedução secante, ao começar com $L=0$ podemos usar o circuito de ajuste de fase para fazer $v_{sp}(t),v_{rp}(t)$ terem a mesma fase, ficando com os máximos e mínimos nas mesmas posições temporais
- Se $\Delta t$ for o intervalo tempo entre 2 picos adjacentes temos:
$$\Delta t_{osc}=\frac{f_{m}T_{(f_{m}-f_{r})}}{c}L$$
se fizermos medição de $\Delta t$ para vários $L$ conseguimos determinar $c$.

