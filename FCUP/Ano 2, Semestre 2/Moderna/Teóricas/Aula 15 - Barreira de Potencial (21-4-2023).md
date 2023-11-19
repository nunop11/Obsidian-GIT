# 1 - Barreira de Potencial
![[barreira potencial.png]]
- Temos:
$$V(x)=\begin{cases}0 &; &x<0 \\ V_{0} &; &0\leq x\leq L\\ 0 &; &x>L'\end{cases}$$


- Podemos dividir o espaço em 3 zonas: antes da barreira $k_{1}$ (x<0), dentro da barreira $k_{2}$ e após a barreira $k_{3}$ (x>L). Ora, temos que $k_{1}=k_{3}$ porque os meios são iguais.
- Assim, temos:
$$- \frac{\hbar^{2}}{2m}\Psi''(x) + V(x)\Psi(x)=E \Psi(x)$$
e temos:
$$\begin{align*}
k_{1}^{2}&=  \frac{2mE}{\hbar^{2}}>0\\
k_{2}^{2}&= \frac{2m}{\hbar^{2}}(V_{0}-E)>0 \quad ;\quad E<V_{0}\\
k_{3}^{2}&= \frac{2m}{\hbar^{2}}(E-V_{0})>0 \quad ;\quad E>V_{0}
\end{align*}$$
conforme o que já vimos com o poço infinito e com o salto de potencial.
- Assim, ao resolver a equação diferencial temos (aqui usei a atribuição de letras que tem no _Eisberg_):
$$\begin{align*}
\Psi_{1}(x)&= Ae^{ik_{1}x}+Be^{-ik_{1}x} \quad;\quad x<0\\
\Psi_{2}(x)&= Fe^{k_{2}x}+Ge^{-k_{2}x} \quad;\quad 0<x<L  \quad(E<V_{0})\\
\Psi_{2}^{\star}(x)&= Fe^{-ik_{3}x}+Ge^{ik_{3}x} \quad;\quad 0<x<L  \quad(E>V_{0})\\
\Psi_{3}(x)&= Ce^{ik_{1}x}+De^{-ik_{1}x} \quad;\quad x>L
\end{align*}$$
- No entanto, como não temos nenhum mecanismo físico para gerar reflexão dentro da barreira e a onda vem da esquerda, ficamos com $$D=0$$
- Por outro lado, não podemos ver que nunca é possível ter $G=0$, pois
    - Para $E>V_{0}$ passaríamos a ter reflexão dentro da barreira, o que é impossível.
    - Para $E<V_{0}$ temos $\Psi$ descontínuo porque $\Psi_{2}$ cresce exponencialmente.

## Caso 1 : $E<V_{0}$
- Temos as condições de fronteira resultantes da necessidade de $\Psi(x)$ ser contínua:
$$\begin{align*}
\Psi_{1}(0)=\Psi_{2}(0)\\
\Psi_{2}(L)=\Psi_{3}(L)\\
\Psi_{1}'(0)=\Psi_{2}'(0)\\
\Psi_{1}'(L)=\Psi_{2}'(L)\\
\end{align*}$$
- Ora, temos 4 equações e temos e 5 variáveis. Assim, podemos definir 4 das variáveis em função da outra. Nomeadamente, podemos definir $B,C,F,G$ em função de $A$. Isto porque $A$ apenas indica a intensidade da onda original, pelo que é arbitrária.

- O gráfico de uma função de probabilidade neste cenário é do tipo:
![[barreira probabilidade.png]]
(sendo que neste caso a barreira está entre $0$ e $a$)

- Podemos definir o número de onda dentrod a barreira como sendo $k= \frac{\sqrt{2mV_{0}}}{\hbar}$




- Temos então:
$$R = \frac{|B|^{2}}{|A|^{2}} \quad \quad ; \quad \quad \tau = \frac{|C|^{2}}{|A|^{2}}$$
- Ora, podemos escrever:
$$\small\tau=\frac{C\cdot C}{A\cdot A}=\left[1 + \frac{\sinh^{2}k_{2}L}{4\frac{E}{V_{0}}\left(1- \frac{E}{V_{0}} \right)} \right]^{-1} = \left[1 + \frac{\left(e^{k_{2}L} + e^{-k_{2}L} \right)^{2}}{16 \frac{E}{V_{0}} \left(1 - \frac{E}{V_{0}} \right) } \right]^{-1}$$
de notar que temos $k_{2}=\frac{\sqrt{2m(V_{0}-E)}}{\hbar}$, logo podemos escrever
$$k_{2}L = \frac{1}{\hbar} \sqrt{2mV_{0}L^{2} \left(1 - \frac{E}{V_{0}} \right)}$$
- Logo, no limite $V_{0}\gg E$ temos $k_{2}L= \frac{1}{\hbar} \sqrt{2mV_{0}L^{2}}$. Assim, como $V_{0}$ é muito elevado, também $k_{2}L$ será. Desta forma, o termo $e^{-k_{2}L}$ torna-se muito reduzido, pelo que aproximamos $e^{-k_{2}L}\approx0$. Também na equação de $\tau$ acima ficamos $\left(1- \frac{E}{V_{0}} \right)\to 1$ 
- Ficamos com
$$\tau \approx 16  \frac{E}{V_{0}}\left(1 - \frac{E}{V_{0}} \right) e^{-k_{2}L} = C e^{-2 G}$$
em que $G$ NÃO é um dos coeficientes das funções de onda, mas sim o *coeficiente de Gamow*.
- De notar ainda que esta apoximação só é correta quando $k_{2}L\gg1$, pelo que $\tau$ será muito reduzido.

## Teorema
- Quando $V(x)$ é uma função par ($V(x)=V(-x)$), as soluções da equação de Schrödinger vão ser *pares* ou *ímpares*.
### Demonstração
- Temos a equação de Schrödinger num ponto $x$:
$$- \frac{\hbar^{2}}{2m} \frac{d^{2}\Psi}{dx^{2}} + V(x)\Psi(x)= E \Psi(x)$$
- Se tivermos uma mudança de variável: $x\to x'$, pelo que: 
$$- \frac{\hbar^{2}}{2m} \frac{d^{2}\Psi}{dx'^{2}} + V(x)\Psi(x')= E \Psi(x')$$
se definirmos $x'=-x$ temos $$\frac{d\Psi}{dx'}= - \frac{d\Psi}{dx} \quad \quad;\quad \quad \frac{d^{2}\Psi}{dx'^{2}}= \frac{d^{2}\Psi}{dx^{2}}$$
e temos  
$$- \frac{\hbar^{2}}{2m} \frac{d^{2}\Psi(-x)}{dx^{2}} + V(-x)\Psi(-x)= E \Psi(-x)$$

- Assim, como $V(x)=V(-x)$, temos que OU $\Psi(x)=\Psi(-x)$ ou $\Psi(x)=-\Psi(-x)$, ou seja, a *função de onda é ou par ou ímpar*.

#moderna #fisica #schrodinger