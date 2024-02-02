-Baseado em https://youtu.be/5O8BEhlqtF4 -
==Importante- Reconhecer cónicas:==
![[tabela conicas.png]]
# Cónicas
- geometricamente, são as curvas resultante da interseção de um cone com um plano. 
![[conicas.png]]
- Por exmplo, esta figura acima podemos ver como se pode obter um círculo (img2), uma elipse (img3) ou um hipérbole (img4).

- Assim as cónicas possíveis são:
    - vazio
    - um ponto
    - duas retas concorrentes ou paralelas
    - uma circunferência
    - uma elipse
    - uma parábola
    - uma hipérbole

- Vamos ver então as fómrmulas reduzidas das principais

## Circunferência
- Conjunto dos pontos do plano à mesma distância de um ponto C
- Dado um ponto $C=(c_1,c_2)$ em R2, e um número real r>0, a circunferência de centro C e raio r é o conjunto de todos os pontos X=(x,y) de R2 tais que
$$d(X,C)=r$$
![[circunferencia.png]]
(d=distância)
- Como sabemos, a circunferência em conjunto com a região compreendida dentro dela é o círculo. Ao falar nas cónicas estamos a falar apenas da circunferência.
- Usando a fórmula da distância obtemos:
> $$(x-c_1)^2+(y-c_2)^2=r^2$$

---
## Elipse
- Conjunto dos pontos cuja soma das distâncias a dois pontos fixos (os focos) é constante e maior do que a distância entre eles
- Dados 2 pontos $F_1 ~~e~~ F_2$ em R2 e um número real $d>d(F_1,F_2)$, a elipse de focos $F_1 ~~e~~ F_2$ é o conjunto de todos os pontos X=(x,y) de R2 tais que 
$$d(X,F_1)+d(X,F_2)=d$$
 ![[elipse.png]]
- Assim, a equação reduzida da elipse é dada por
$$\frac{x^2}{a^2} + \frac{y^2}{b^2}=1, ~~ para~~ a>b$$
- Note-se pela figura acima que o semieixo a (da origem a $a$) é maior ao semieixo b (da origem a $b$). Assim, é necessário o "a>b". Isto ocorre porque o semieixo a contem os focos.
- Entre a,b e c temos esta relação:
$$a^2= b^2+c^2$$
- Por outro lado, se os focos estivessem no eixo dos Y, a elipse rodaria 90º e o semieixo $b$ seria maior que o $a$, logo b>a
- Nesse caso, a fórmula da elipse seria igual, mas a relação  entre a,b e c mudaria. Passaríamos a ter 
$$b^2=a^2+c^2$$

- Em resumo, tem-se:
![[elipse x2.png]]
- Por exemplo, consideremos que se tem uma elipse de centro $C=(c_1,c_2)$ e que a>b. 
![[elipse 2.png]]
- Assim, a equação seria:
> $$\frac{(x-c_1)^2}{a^2}+\frac{(y-c_2)^2}{b^2}=1$$

---
## Hipérbole
- conjunto dos pontos do plano tais que a diferença das distâncias a dois pontos fixos (os focos) é constante e menor que a distância entre os focos
- Ou seja, tendo dois pontos $F_1 ~~e~~ F_2$ em R2 e um número real $0<d<d(F_1,F_2)=2c$, a hipérbole de focos F1 e F2 é o conjunto de todos os pontos X=(x,y) de R2 tais que 
$$|d(X,F_1)-d(X,F_2)|=d$$
![[Attachments/FCUP/A1S1/ALGA/hiperbole.png]]
- Assim fica a hipérbole se os focos estiverem no eixo dos Xs (os focos são os pontos com x=c e x=-c) e o seu centro na origem. Desta forma, a equação da elipse é dada por:
$$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$$
- Se igualarmos a fórmula a 0, facilmente obtemos as coordenadas dos "zeros" hipérbole, que terão de ser (a,0) e (-a,0)
- A relação entre a,b e c tem a ver com as duas retas assíntotas da elipse, $y=\frac{b}{a}x ~~e~~ y=\frac{a}{b}x$.
- Se colocarmos os focos no eixo dos Ys, a hipérbole roda 90º, mas a fórmula mantem-se.

- No entanto, independentemente da posição dos focos, tem-se:
> $$c^2=a^2+b^2$$

- Por exemplo, consideremos que se tem uma hipérbole de centro $C=(c_1,c_2)$
![[hiperbole 2.png]] 
A sua equação seria dada por 
> $$\frac{(x-c_1)^2}{a^2}-\frac{(y-c_2)^2}{b^2}=1$$

---
## Parábola
(Nota: o video tem erros nesta parte)

- Conjunto dos pontos do plano equidistantes de um ponto fixo (o foco) e de uma reta fixa (a reta diretriz) que não contem o foco.
- Dado um ponto F e uma reta d em R2 que não contem F, a parábola de foco F e diretriz d é o conjunto de todos os pontos X=(x,y) de R2 para os quais se tem
$$d(X,F)=d(X,d)$$
![[Attachments/FCUP/A1S1/ALGA/parabola.png]]
- Temos assim a parábola para a um foco contido no eixo dos Y e uma reta diretriz paralela ao eixo dos X.
- Assim, a formúla será dada por
$$x^2=4py$$
- No entanto, a parábola pode estar virada para o lado ou para baixo. Regra geral, usar a fórmula $d(X,F)=d(X,d)$ permite obter a equação da parábola

- Por fim, vejamos o caso geral de uma parábola de vértice $V=(c_1,c_2)$,
![[parabola 2.png]]
, temos que:
> $$(x-c_1)^2=2p(y-c_2)^2$$

---
-Baseado em https://youtu.be/l7_0BF9Qme4 -

# Reconhecer cónicas
- Vamos ver maneiras de como pegar na equação geral de uma cónica e perceber qual é, assim como quais o seu centro/vertice/etc.
- Visto de outra forma, cónicas são raízes de um polinómio de grau 2 de 2 variáveis, ou seja, são soluções desta equação:
$$ax^2+bxy+cy^2+dx+ey+f=0$$
A equação de uma cónica está em forma reduzida se:
1. só tiver coeficientes de 2º grau e coeficeinte constante, não havendo coeficeinte misto de 2º grau ($xy$)
2. Se uma das variáveis tiver um coeficeinte de 1º grau, então o seu coeficiente de 2º grau é zero (o caso da parábola)

> Exemplos:
> 1. $3x^2+4xy-2x+y-1=0$ é a equação geral de uma cónica
> 2. $x^2+y^2-4=0$ é a equação reduzida de uma circunferência
> 3. $x^2-y^2-9=0$ é a eq reduzida de uma hipérbole (passasse o 9 para o outro lado e divide-se tudo por 9)
> 4. $x^2-3y-9=0$ é a eq reduzida de uma parábola
> Nos exemplos acima podemos ver que em nenhuma delas temos o termo $xy$

- Aplicando conteúdos de [[7- Quadráticas]]
- Dada a equação geral de uma cónica, associamos à sua parte de 2º grau (quadrática) um operador linear de R2,
$$L(x,y)=ax^2+bxy+cy^2$$
, cuja matriz é:
$$A=\begin{pmatrix}a&b/2\\ b/2&c\end{pmatrix}$$
(Para perceber de onde é que a equação vem, ver [[7- Quadráticas]])

- $L(x,y)=ax^2+2bxy+cy^2$ tem uma matriz A, que é diagonizável. Assim, existe uma matriz ortogonal M tal que $M^TAM=\begin{pmatrix}\alpha &0\\0&\beta \end{pmatrix}=D$
- Chamemos $u=\begin{pmatrix}x\\ y \end{pmatrix}$, logo $u^T=(x ~~ y)$ 
- Fazendo uma mudança de variável: $u=\begin{pmatrix}x\\ y \end{pmatrix}=M\begin{pmatrix}x^\prime\\ y^\prime \end{pmatrix}$, z equação anterior é transformada em:
$$L(x,y)=u^TAu \rightarrow L(x',y')=\Biggr(M\begin{pmatrix}x'\\ y'\end{pmatrix}\Biggr)^TAM\begin{pmatrix}x'\\ y' \end{pmatrix}=$$
$$=\begin{pmatrix}x'\\ y' \end{pmatrix}^TM^TAM\begin{pmatrix} x'\\ y'\end{pmatrix}=(x' ~~ y')\begin{pmatrix}\alpha &0 \\0& \beta \end{pmatrix}\begin{pmatrix}x'\\ y'\end{pmatrix}=$$
$$=\alpha x'^2+\beta y'^2$$
- Assim, concluímos que ao fazer a mudançad e variável dada pela matriz diagonal da matriz, eliminamos o termo $xy$

### Exemplo prático
- Considere-se a equção reduzida de uma cónica:
$$5x^2+4xy+2y^2-1=0$$
- Como o termo $xy$ ainda lá está, não podemos ainda concluir sobre qual cónica esta é
- Facilmente tiramos a matriz: $A=\begin{pmatrix} 5&2\\2&2 \end{pmatrix}$
- Daqui facilmente tiramos o polinómio caraterístico:
$$P_A(\lambda)=det\begin{pmatrix}5-\lambda & 2 \\ 2 & 2-\lambda \end{pmatrix}=\lambda^2 -7\lambda+6$$
- Daqui facilmente se tira que $\lambda = 6 \vee \lambda = 1$
- Ao fazer a mudança de variável com a matriz diagonal M, podemos obter que 
$$6x'^2+1y'^2-1=0 \leftrightarrow x'^2+\frac{y'^2}{6}=1$$
- Assim podemos ver que temos uma elipse
- Repare-se que acima só multiplicamos o x e o y pelos autovalores
- De notar que isto permite perceber qual é a cónica representada. No entanto, como estamos a fazer uma mudança de base, isto não nos permite desenhar a cónica.

(são feitos exemplos de equações de cónicas completas e incompletas, apenas com o $x^2, y^2$ e o termo independente)

(são realizados muitos exemplos no vídeo. Não vou passar. No teste posso meter as equações no wolfram alpha e já sei o que são)

#conicas #alga