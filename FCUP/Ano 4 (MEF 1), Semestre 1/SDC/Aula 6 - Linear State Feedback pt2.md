- OK, vimos o que isto é e como calcular o vetor $K$ que nos dá os polos desejados. Mas ainda falta ver algumas coisas:
    - Será que todos os sistemas podem ser manipulados assim?
    - Não haverá um método menos trabalhoso que este? Este método torna-se excessivamente complicado se tivermos $n>3$

### Quando podemos usar K?
- Existe um teorema demosntrado no PPT que nos diz que:
    - Existe uma matriz de feedback $K$ que permite forçar os polos que quisermos, *se e só se* o sistema for **Controlável**.
    - Aqui faz sentido a definição para "Controlável" que vimos mais atrás: um sistema é controlável se conseguirmos sempre ir de um estado $x(t_{0})$ para outro $x(t)$.

- Ou seja, se $M$ não for full-ranked nem vale a pena perder tempo a calcular polinómios e polos.

### Como calcular K
#### Método Direto
- Isto é o que vimos na aula passada. 
- Num certo sistema controlável com uma matriz de feedback $K$ queremos colocar os polos $p_{1},p_{2},\dots,p_{n}$ tendo-se o polinómio caraterístico $p(s)=(s-p_{1})(s-p_{2})\cdots(s-p_{n})$
- E teremos ainda $$\det(sI-A+BK)=p(s)$$
- Ou seja, o método *direto* consiste em simplesmente igualar este determinante ao polinómio desejado e resolver o sistema.

#### Fórmula de Ackerman,
- A fórmula de Ackerman consiste em:
$$K=\begin{pmatrix}0 & 0 & \cdots & 0 & 1\end{pmatrix}M^{-1}\phi(A)$$
em que:
    - $A$ é a matriz do sistema
    - $M$ é a matriz de controlabilidade
    - $\phi(\cdot)$ é o polinómio caraterístico aplicado a uma matriz

- Ou seja:
$$\phi(A)=A^{n}+ \alpha_{1}A^{n-1}+\cdots+\alpha_{n-1}A+\alpha_{n}I$$
- Isto pode ser usado no Matlab usando `acker(A,B,P)` em que $P$ é o vetor dos polos desejados (valores próprios do sistema controlado).

#### CCF 
- Consideremos que temos o sistema NÃO na representação CCF. 
- A matriz de transformação para a CCF é $T$, como já vimos no passado. Podemos definir:
$$T=MW ~~~~;~~~~W=\begin{pmatrix}a_{n-1} & a_{n-2} & \dots & a_{1} & 1 \\ a_{n-2} & a_{n-3} & \dots & 1 & 0 \\ \vdots & \vdots && \vdots & \vdots \\ a_{1} & 1  & \dots & 0 & 0 \\ 1 & 0 & \dots & 0 & 0\end{pmatrix}$$
- Assim temos:
$$\begin{cases}
\dot{x}=Ax+Bu \\
u=-Kx
\end{cases}\to \begin{cases}
\dot{\tilde{x}}=\tilde{A}\tilde{x} + \tilde{B}u \\
u = - \tilde{K}\tilde{x}
\end{cases}$$
em que sabemos que
$$\begin{align*}
x&= T \tilde{x}\\
\tilde{A}&= T^{-1}AT\\
\tilde{B}&= T^{-1}B\\
\tilde{C}&= CT\\
\tilde{D}&= D
\end{align*}$$
e aqui podemos calcular que
$$K=\tilde{K}T^{-1}$$
- Daqui dá para deduzir que
$$K=\begin{pmatrix}\alpha_{n}-a_{n} & \alpha_{n-1}-a_{n-1} & \cdots & \alpha_{1}-a_{1}\end{pmatrix}T^{-1}$$

### E se não for Ctrlb?
- No PPT tem informação de como contornar isto