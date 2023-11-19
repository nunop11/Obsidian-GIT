-Baseado em https://youtu.be/e8kAs458cVI -
# Espaço Vetorial Real
- conjuntos não vazios cujos elementos são vetores
- A esse conjunto 2 operações estão definidas operações (+ e x)
## Adição
$$u+v\in V, \forall u,v \in V$$
## Multiplicação
$$\alpha u \in V; \forall u \in V, \forall \alpha \in R$$
## Axiomas
Para $u,v,w \in V$ e $\alpha, \beta \in R$, tem-se:
### Adição
$$\begin{align}
(u+v)+w&=u+(v+w)\\
u+v&=v+u\\
\exists 0 \in V, u+0&=u\\
\exists (-u)\in V, u + (-u)&=0
\end{align}$$
### Multiplicação
$$\begin{align}
(\alpha \beta)u&=\alpha(\beta u)\\
(\alpha+\beta)u&=\alpha u +\beta u \\
\alpha(u+v)&=\alpha u + \alpha v \\
1u&=u
\end{align}$$
## Exercício 1
- Tendo um conjunto $V=\{(x,y)\in R^2,/, x\ge 0 \}$. Pretendemos saber se é um espaço vetorial.
- Consideremos que existem 2 elementos $v_1, v_2$ que pertecem a V, tal que $v_1=(x_1,y_1)~e~v_2=(x_2,y_2)$.
- Conforme as condições do espaço vetorial, sabe-se que $x_1\geq0~e~x_2\geq0$. Sabemos ainda que $y_1\in R, y_2 \in R$.

- Agora precisamos de verificar as condições e axiomas anteriores.
- Adição: $$v_1+v_2=(x_1+x_2, y_1 +y_2)$$
    - Como x1 e x2 são ambos $\geq 0$, logo a soma de eles tamvém será. A mesma lógica confirma que a soma dos ys $\in R$.
- Multiplicação: $$\alpha(v_1)=(\alpha~x_1, \alpha~y_1),~~\alpha \in R$$
    - Neste caso, como $\alpha \in R$, $\alpha x_1$ nem sempre será $\geq 0$.

- Assim, verificamos que $v_1+v_2\in V$, mas $\alpha v_1 \notin V$. Assim, **V não é um espaço vetorial**.

> Só é preciso aplicar esta lógica aos outros exercícios

---
-Baseaso em: https://youtu.be/XxUWCQaVwKM -
# Subespaço Vetorial
- Como o nome indica, é um subespaço, aka um subconjunto, uma divisão de um espaço vetorial.
- Assim teríamos S, um subespaço vetorial do espaço V:
![[subespaço.png]]
- Existem algumas regras para que um conjunto seja um subespaço vetorial:
$$\begin{align}
0 &\in S \\
u+v&\in S; u,v \in S \\
\alpha u &\in S; u \in S,\alpha \in R  
\end{align}$$
- Todos os espaços vetoriais admitem pelo menos 2 subespaços, ==os subespaços triviais==:
    - conjunto $\{0\}$, o subespaço nulo
    - o próprio espaço. Ou seja, V pode ser um subespaço de V
- Todos os outros subespaços são os ==subespaços próprios de V==.

- Por exemplo, para $R^2$, os seus subespaços vetoriais são $\{(0,0)\}~e~R^2$. Uns exemplos de espaços próprios de $R^2$ são as retas que passam pela origem.

## Exercício 1:
- Sejam $V=R^2$ e $S=\{(x,y)\in R^2 : y=3x\}$. Verifica se S é subespaço de V.
- Facilmente se pode reescrever S como $S=\{(x, 3x);x\in R\}$. Por outras palavras, os elementos de S serão os vetores de R em que a segunda componente é o triplo da primeira.

Verifiquemos então as condições:
1. Vetor nulo
$$\begin{align}
x &=0 \\
(0, 3\cdot0)&=(0,0)\in S
\end{align}$$
2. Adição
$$\begin{align}
Tendo ~~~~ v_1=(x_1, 3x_1)\in S ~~ &e ~~ v_2=(x_2, 3x_2)\in S,\\
Assim,~ v_1+v_2&=(x_1+x_2, 3x_1+3x_2)=\\
&=(x_1+x_2, 3(x_1+x_2))\end{align}$$
3. Multiplicação
$$\begin{align}
Tendo~~~~v_1=(x_1, 3x_1)\in S ~~ e ~~ \alpha \in R, tem-se:\\
\alpha v_1= \alpha(x_1, 3x_1)=(\alpha x_1, 3\alpha x_1)
\end{align}$$

- Assim, verificam-se as três condições do subespaço. Desta forma, S é um SV.

> Esta lógica permite verificar se um conjunto é um subespaço vetorial em qualquer exercício.

---

-Baseado em: https://youtu.be/R2mfAzxldUE -
# Subespaço como conjunto de vetores
Por vezes podem aparecer subespaços nesta forma:
$$S=\langle u_1,...,u_k\rangle$$
- Nesse caso, estes vetores u, de 1 a k, são os **vetores geradores** do subespaço
- Este subespaço pode ser reescrito como:
$$S=\langle u_1,...,u_k\rangle=\{a_1u_2+...+a_ku_k: a_1,...,a_k\in R\}$$
- Se na sequência da alínear anterior houver algum vetor que possa ser escrito como uma combinação de linear de outros vetores, então ele pode ser eliminado. Ou seja, os vetores geradores serão L.Independentes

- Um espaço vetorial é finitamente gerado se existe um número finito de vetores que o geram.

## Exercício 1
Temos o seguinte subespaço definido por sistema de equações. Queremos defini-lo através de vetores geradores:
$$F=\{(x,y,z)\in R^3:x+y-z=0\}$$
- Isto pode ser reescrito como $F=\{(x,y,x+y)\in R^3\}$.
- Uma estratégia prática que permite fazer isto é esta:

- Se tivermos as coordenadas gerais de um ponto de F, obtidas acima, estas podem ser divididas na soma das suas componentes:
$$(x,y,x+y)=x(1,0,1)+y(0,1,1)$$
(Se fizermos a distribuição de x e y e fizermos a soma verificaremos que isto é uma igualdade)
- Assim, concluímos que:
$$F=\langle(1,0,1),(0,1,1)\rangle$$
, que são os vetores obtidos acima

## Exercício 2
Temos o seguinte subespaço definido com vetores geradores. Pretendemos defini-lo como sistema de equações:
$$F=\langle(1,1,2),(1,0,1),(2,1,3)\rangle$$
- Como estes 3 vetores são vetores geradores, qualquer vetor deste subespaço pode ser definido como uma combinação linear deles:
$$(x,y,z)=\alpha_1(1,1,2)+\alpha_2(1,0,1)+\alpha_3(2,1,3)$$
- Distribuindo os alfas e fazendo a soma dos vetores obtem-se que:
$$(x,y,z)=(\alpha_1+\alpha_2+2\alpha_3, \alpha_1+\alpha_3, 1\alpha_1+\alpha_2+3\alpha_3)$$
- Daqui faz-se um sistema. Tira-se a matriz ampliada em que os resultados são x,y e z. Faz-se eliminção de Gauss, isola-se as variáveis e obtem-se $\alpha_1, \alpha_2 ~e~ \alpha_3$ em função de x,y e z. 
- No entanto, o objetivo será obter algo em que se tem uma igualdade a 0. No caso deste exercício, obtem-se que $z-x-y=0$, ou seja, $z=x+y$.
- Assim pode-se escrever F como sistema de equações, sendo que se conclui que este F é o mesmo subespaço do Exercício 1.

#alga #espaços_vetoriais