# Funcional
- Uma transformação linear $T:~V\rightarrow \mathbb R$ é um **funcional linear**

Exemplos em $\mathbb R^n$:
-   $T(u) = u_x + u_y + \dots + u_k$ → Soma das coordenadas
-   $T_v(u) = u \cdot v$ → Produto escalar um vetor qualquer $v$

Exemplos para $C^0 = \{f: f \text{ é contínua}\}$:
-   $T(f) = f(0)$ → Valor da função num ponto
-   $T(f) = f'(0)$ → Derivada **num ponto**
-   $T(f) = \int_0^1f(x)dx$ → Integral

# Espaço dual
Dado um espaço vetorial V, $V^*$ (o espaço dual de $V$) é um espaço vetorial que contem todos os funcionais lineares definidos em V:
$$V^*=\{L:V\rightarrow\mathbb R ~~~~linear\}$$
E $V^*$ é um espaço vetorial com as seguintes operações:(L e M são elementos de $V^*$ e $\alpha$ é um escalar)
- Sendo $N=L+M$, então 
$$N(v)=L(v)+M(v) ~~~~~~ N:V\rightarrow \mathbb R$$
- Sendo $N=\alpha L$, então
$$N(v)=\alpha L(v) ~~~~~~ N:V \rightarrow \mathbb R$$
- Sendo $N=0$
$$N(v)=0 ~~~~~~ N:V \rightarrow \mathbb R$$

> Nota: o espaço dual do espaço dual é o próprio espaço:
> $$V^{**}=V$$

## Base Dual
- A base de um espaço dual V* é chamada de base dual e é um conjunto ordenado de funcionais lineares tal que, dada uma base $B=[a_1,a_2,...,a_n]$ de V:
    - Sendo $B^*=[f_1,f_2,...,f_n]$ a base dual de $V^*$
    - $f_1(a_1)=1,~f_1(a_2)=0,...,f_1(a_n)=0$
    - $f_2(a_1)=0,~f_2(a_2)=1,...,f_2(a_n)=0$ (...)
    - $f_n(a_1)=0,~f_n(a_2)=0,...,f_n(a_n)=1$

Ou seja, a base dual de $V^*$ é o conjunto ordenado de funcionais lineares que, quando aplicados sobre os vetores de uma base de $V$, devolvem $1$ para apenas um valor da base, devolvendo $0$ nos restantes.
Uma combinação linear dos funcionais de $V^*$ pode ser usada para escrever qualquer funcional linear

![[exemplos dual.png]]
- Um dual de um espaço de dimensão n tem dimensão n

### Dual e produto escalar
Para cada funcional linear $L:\mathbb R^2\rightarrow \mathbb R$ existe um único elemento $v\in \mathbb R^2$ tal que $\forall u \in \mathbb R^2$,
$$L(u)=v\cdot u$$
(Prova no powerpoint da aula)

#dual #funcional #alga