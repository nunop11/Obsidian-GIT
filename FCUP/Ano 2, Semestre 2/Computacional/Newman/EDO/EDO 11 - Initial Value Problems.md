# 11 -  Problemas de Valor Inicial
- Problemas deste tipo:
> Lançamos uma bola, de uma altura inicial $x=0$. Sabemos que a asua altura conforme o tempo será dada por $$\frac{d^{2}x}{dt^{2}}=-g$$
> Sabemos ainda que a bola atingiu o chão em $t_{1}$. Qual terá sido a velocidade vertical inicial da bola?

- Ou seja, é um problema em que conhecemos 2 condições, uma inicial e uma final. Com estas, queremos obter a restante condição inicial, neste caso, velocidade vertical inicial.

## 11.1 - Shooting Method
- No caso do nosso problema acima, consiste em resolver a equação diferencial com vários valores de $v_{y}(0)$ escolhidos por tentativa e erro.
- Ou seja, escolhemos uma primeira tentativa: $v_{y}=v_{1}$. Muito provavelmente, com esta velocidade inicial, a bola irá colidar com o chão num tempo diferente de $t_1$. Ou seja, iremos mudar a nossa estimativa e tentar outra vez.
- Mas como mudamos a estimativa? Ora, em princípio, podemos definir uma função $x=f(v)$ que nos dá a altura $x$ em $t_1$ para uma certa velocidade vertical inicial $v$.
- Não sabemos esta função, claro, mas podemos determinar o seu valor ao resolver a equação diferencial com a velocidade inicial $v$. Ora, o que nós queremos obter é o valor de $v$ para o qual temos $x=0$, ou seja, queremos obter o *zero* da função $f$.
- Ou seja, este método consiste em: definir uma função $f(v)$, em que conforme uma velocidade inicial $v$ recebemos a posição no tempo desejado. Usamos um método como Binary Search ou Newton-Raphson para obter o zero da função.
- De notar que, por exemplo, poderemos conhecer a distância percorrida até colidir com o chão, sendo que iriamos operar de forma semelhante.

## 11.2 - Problemas de Autovalores
- Consideremos uma partícula em 1-D com massa $m$. Temos a equação de Schrödinger:
$$\frac{-\hbar^{2}}{2m} \frac{d^{2}\psi}{dx^{2}}+V(x)\psi(x)=E \psi(x)$$
- Esta partícula está num poço de potencial infinito:
$$V(x) = \begin{cases}
0 &; & 0<x<L \\
\infty &; &restante
\end{cases}$$
- Neste problema temos a condição de fronteira: $\psi(0)=\psi(L)=0$. 
- Experimentemos então usar o método de Shooting.

- Começamos por dividir a equação:
$$\frac{d\psi}{dx}=\phi ~~~~;~~~~ \frac{d\phi}{dx}= \frac{2m}{\hbar^{2}}[V(x)-E]\psi$$
- No entanto, até agora, poderia não ser claro o quê que queremos resolver ao certo. Ora, sabemos que $\psi(0)=0$, mas qual será a outra condição inicial: $\phi(0)$? Ora, não a conhecemos. Invés disso, conhecemos $\psi(L)=0$. Ou seja, isto não passa de um problema de valores iniciais, tal como o problema do lançamento de uma bola que temos acima: Sabemos que a função de onda se anula em $x=L$, mas não sabemos a "velocidade" ($\phi$) inicial necessária para tal acontecer.
- Poderíamos então presumir que usar o método de shooting iria funcionar. Mas não, de todo.
![[Eq onda computacional.png]]
- Tal como temos acima, se aumentarmos $\phi(0)$ toda a onda será esticada, ou seja, será mais ingreme perto dos zeros. Isto dificulta o processo de os encontrar. Além disso, vemos que os zeros não mudam, ou seja, se $\phi_{1}$ não era a condição inicial correta, $\phi_{2}=2 \phi_{1}$ também não será.
- Isto ocorre porque a solução que procuramos *não existe* sempre. A solução só existe para certos valores de $E$, as chamadas _energias permitidas_.
- Uma forma de resolver problemas deste é, então, para um conjunto de condições iniciais, variar $E$ até obter $\psi(L)=0$. O valor de $E$ em que isso acontecer será um autovalor do sistema. Podemos então interpretar isto da mesma forma que o método de shooting: queremos obter um zero da função $f(E)$.