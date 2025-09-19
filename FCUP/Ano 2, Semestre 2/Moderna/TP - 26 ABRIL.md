w![[TP Moderna 26-4-2023|650]]
- Temos então 3 regiões. 
- As regiões 1 e 3 são proibídas na fisica clássica. Isto porque temos $E=E_{c}+V$. Ora, se $E<V$, então é preciso que se tenha $E_{c}<0$, o que é impossível na física clássica.

- Temos $\Psi(x,t)=X(x)T(t)=X(x) e^{-i \frac{E}{\hbar} t}$
- Vamos presumir que temos um caso independente do tempo, pelo que $\Psi(x,t)=\psi(x)$
- Como nas regiões 1 e 3 temos "meios iguais" em que $V=0$ e $E<0$ temos:

$$\begin{align}
\frac{-\hbar^{2}}{2m} \psi'' + V \psi &=  E \psi\\
- \frac{\hbar^{2}}{2m}\psi'' &= - |E| \psi \\
\frac{\hbar^{2}}{2m}\psi'' - |E| \psi &= 0 \longrightarrow r^{2} - k' ^{~2} = 0 \to r_{1,2}\in\mathbb{R}\\
\textsf{em que temos}\quad \quad k'^{~2} &= \frac{2m|E|}{\hbar^{2}} > 0\\
\end{align}$$

E assim:
$$\begin{align*}
\psi_{1}(x) &= Ce^{k'x}+ D e^{-k'x} \quad;\quad (x\le- a/2)\\
\psi_{3}(x) &= Fe^{k'x}+ G e^{-k'x} \quad;\quad (x\ge a/2)
\end{align*}$$
- Na região central, 2, temos $V=-V_{0}=-|V_{0}|$ e $E<0$, logo:

$$\begin{align*}
\frac{-\hbar^{2}}{2m} \psi'' + V \psi &=  E \psi\\
- \frac{\hbar^{2}}{2m}\psi'' -|V_{0}|\psi &= - |E| \psi \\
\frac{\hbar^{2}}{2m}\psi'' + |V_{0}|\psi - |E| \psi &= 0 \longrightarrow r^{2} + k^{2} = 0 \to r_{1,2}\notin\mathbb{R}\\
\textsf{em que temos }\quad \quad k^{2} &= \frac{2m}{\hbar^{2}}(|V_{0}|-|E|) > 0
\end{align*}$$

- De notar que o que queremos ter sempre é _**k^2 positivo**_. Isto porque $\large k=2\pi/\lambda$ não passa de um número de onda, pelo que tem de ser real, e o seu quadrado tem que ser positivo.
- Temos então:
$$\psi_{2}(x)=A' e^{ikx} + B' e^{-ikx} = A\sin kx + B\cos kx$$
- Ou seja, a função completa é:
$$\psi(x)= \begin{cases}\psi_{1}(x) = Ce^{k'x}+ D e^{-k'x} \quad &;\quad (x\le- a/2)\\
\psi_{2}(x)=A\sin kx + B\cos kx \quad &; \quad (-a/2 \le x\leq a/2)\\
\psi_{3}(x) = Fe^{k'x}+ G e^{-k'x} \quad &;\quad (x\ge a/2) \end{cases}$$

### Condições de Fronteira
- Temos logo que $\psi(-\infty)=\psi(+\infty)=0$, de onde temos obrigatoriamente $$D=F=0$$

- De seguida temos as condições de fronteira relacionadas com continuidade
$$\psi ~~ contínua \Longrightarrow \begin{cases}x=-\frac{a}{2} \to C e^{-k' \frac{a}{2}}=-A\sin\left(k \frac{a}{2}\right)+ B\cos\left(k \frac{a}{2}\right) \quad \quad \textsf{(Eq.1)}\\ x= \frac{a}{2} \to G e^{-k'\frac{a}{2}} = A\sin\left(k \frac{a}{2}\right)+ B\cos(k \frac{a}{2})\quad \quad \textsf{(Eq.2)}\end{cases}$$
- Temos:
$$\begin{align*}
\psi'(x)= \begin{cases}\psi_{1}'(x) = Ck'e^{k'x} \quad &;\quad (x\le- a/2)\\
\psi_{2}'(x)=Ak\cos kx - Bk\sin kx \quad &; \quad (-a/2 \le x\leq a/2)\\
\psi_{3}'(x) = -Gk'e^{-k'x} \quad &;\quad (x\ge a/2) \end{cases}
\end{align*}$$
e aplicamos a continuidade:
$$\psi' ~~ contínua \Longrightarrow \begin{cases}x=-\frac{a}{2} \to Ck' e^{-k' \frac{a}{2}}=Ak\cos\left(k \frac{a}{2}\right)+ Bk\sin\left(k \frac{a}{2}\right) \quad \quad \textsf{(Eq.3)}\\ x= \frac{a}{2} \to -Gk' e^{-k'\frac{a}{2}} = Ak\cos\left(k \frac{a}{2}\right)- Bk\sin(k \frac{a}{2})\quad \quad \textsf{(Eq.4)}\end{cases}$$
- Ora, temos 4 equações e 4 variáveis. Podemos fazer:
$$\begin{cases}(1)+(2)\longrightarrow \quad 2B\cos(k \frac{a}{2})=(C+G)e^{-k' \frac{a}{2}}\\(2)-(1)\longrightarrow \quad 2A\sin(k \frac{a}{2})=(G-C)e^{-k' \frac{a}{2}}\\(3)+(4)\longrightarrow \quad 2kA\cos(k \frac{a}{2})=(C-G)k' e^{-k' \frac{a}{2}}\\(3)-(4)\longrightarrow \quad 2kB\sin(k \frac{a}{2})=(C+G)k' e^{-k' \frac{a}{2}}\end{cases}$$
- Ora, podemos decompor qualquer função $\psi$ numa função par e uma ímpar. Ora, cosseno é par e seno é impar. Assim:
$$\begin{align*}
par\Longrightarrow~~apenas~~\cos\Longrightarrow~A=0\\
ímpar\Longrightarrow~~apenas~~\sin\Longrightarrow~B=0
\end{align*}$$
- Podemos começar por igualar $(C+G)e^{\frac{a}{2}}$ na primeira e terceira equações acima, tendo-se:
$$\begin{align*}
\cancel{2B}\cos\left(k \frac{a}{2}\right)&= \cancel{2B} \frac{k}{k'}\sin\left(k \frac{a}{2}\right) \\
k' &= \frac{k\sin \left(k \frac{a}{2} \right)}{\cos \left(k \frac{a}{2} \right)}\\
k' &= k\tan\left(k \frac{a}{2}\right)
\end{align*}$$

- Daquilo acima temos:
$$\frac{k'^{~2}}{k}= \tan^{2}\left(k \frac{a}{2}\right)=1 + \frac{1}{\cos^{2} \left(k \frac{a}{2} \right)}$$
e temos $$\cos^{2} \left(k \frac{a}{2}\right) = \frac{k^{2}}{k_{0}^{2}}$$
sendo $$k_{0}^{2}= \frac{2m|V_{0}|}{\hbar^{2}} \quad;\quad k^{2}=\frac{2m|E|}{\hbar^{2}} \quad;\quad k'^{~2}=\frac{2m}{\hbar^{2}}(|V_{0}|-|E|)$$
- A professora acabou a dizer que vamos fazer um gráfico em que temos:
$$\eta= \frac{k'a}{2} \quad \quad;\quad \quad \xi = \frac{ka}{2}$$

