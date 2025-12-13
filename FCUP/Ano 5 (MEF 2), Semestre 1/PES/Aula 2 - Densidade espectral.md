## Densidade espectral
- Se a função de covariância de um processo estacionário for *absolutamente somável* ($\sum_{\tau=-\infty}^{+\infty}|\lambda_{xx}(\tau)|<\infty$) então podemos determinar a sua transformada de **Fourier** 
- Ora, a transformada de Fourier da função covariância de um processo estocástico chama-se **Densidade Espectral de Potência** ou *Densidade espectral*

- Notemos que matrizes de covariância são simétricas:
$$\Lambda=\begin{bmatrix}\lambda_{yy}(0) & \lambda_{yy}(1) & \cdots & \lambda_{yy}(n) \\ \lambda_{yy}(1) & \lambda_{yy}(0) & \cdots & \lambda_{yy}(n-1) \\ \vdots & \vdots & \ddots & \vdots \\ \lambda_{yy}(n) & \lambda_{yy}(n-1) & \cdots & \lambda_{yy}(0)\end{bmatrix}$$

### Definição formal
- Se um processo estacionário $\{x(t)\}$ tiver uma função de covariância absolutamente somável então a sua densidade espectral de potência é dada por
$$\Phi_{xx}(\omega)=\sum\limits_{\tau=-\infty}^{+\infty}\lambda_{xx}(\tau)e^{-j\omega\tau}$$
- E podemos definir a covariância a partir da densidade espectral, usando a transformada inversa de Fourier:
$$\lambda_{xx}(\tau)=\frac{1}{2\pi}\int_{-\pi}^{\pi}\Phi_{xx}(\omega)e^{j\omega\tau}d\omega$$
- Notemos que para $\tau=0$ temos
$$\lambda_{xx}(0)=\frac{1}{2\pi}\int_{-\pi}^{\pi}\Phi_{xx}(\omega)d\omega$$
se o processo for ergódico, podemos ainda escrever:
$$\lambda_{xx}(0)=\lim_{N\to\infty} \frac{1}{2N+1} \sum\limits_{t=-N}^{N}x(t)^{2}$$
e (não sei como) pelo teorema de Parseval podemos definir 
$$\lim_{N\to\infty} \frac{1}{2N+1} \sum\limits_{t=-N}^{N}x(t)^{2}=P_{x}[x(t)^{2}]$$
em que $P_{x}$ é apotência do sinal!
- Ou seja, isto diz-nos que $\Phi_{xx}(\omega)$ representa a distribuição de potência de $x(t)$ no intervalo $\omega\in[-\pi, \pi]$. Daí o nome "densidade espectral de potência"

### Propriedades
#### Simetria par
$$\Phi_{xx}(\omega)=\Phi_{xx}(-\omega)$$
- Isto acontece porque $\lambda_{xx}(\tau)$ ser uma função par: $\lambda_{xx}(\tau)=\lambda_{xx}(-\tau)$

#### Não negativa
$$\Phi_{xx}(\omega)\ge0$$
- Temos que a variância de $x(t)$ é $\sigma_{x}^{2}=\frac{1}{2\pi}\int_{-\pi}^{+\pi}\Phi_{xx}(\omega)d\omega$.
- A variância, claro, tem que ser positiva e real
- Imaginemos, que temos $\Phi_{xx}<0$. Num certo intervalo $\omega_{1}<\omega<\omega_{2}$, com a filtragem adequada, seria possível fazer com que $\sigma_{x}^{2}<0$, o que é impossivel! Logo a densidade espectral TEM de ser positiva

### Propagação de processos estacionários através de sistemas dinâmicos estáveis
- Consideremos um SLIT com função transferência $G(z)$ estável
- Imaginemos agora que a entrada do sistema for um processo fracamente estacionário $\{u(t)\}$ com média nula e densidade espectral $\Phi_{uu}(\omega)$.
- A saída do sistema, que representamos como $\{y(t)\}$ será também um processo estocástico fracamente estacionário com média nula. A sua densidade espectral é dada por:
$$\Phi_{yy}(\omega)=|G(e^{j\omega})|^{2}\Phi_{uu}(\omega)$$

### Teorema 1
- Podemos fatorizar a densidade espectral $\Phi_{yy}(\omega)$ assim
$$\Phi_{yy}(\omega)=H(e^{j\omega})H(e^{-j\omega})\sigma^{2}=|H(e^{j\omega})|^{2}\sigma^{2}$$
em que usamos
$$H(z)=\sum\limits_{k=0}^{\infty}h(k)z^{-k}$$
- Isto é uma função transferência normal no espaço de estado discreto. Temos que $h(k)$ são coeficientes e $z^{-k}$ é um *unit delay / atraso de amostra*. Tem esse nome porque, tendo uma transformada Z $X(z)$ da sequência $x(k)$, teremos que:
$$z^{-1}X(z) ~~\substack{\mathcal{Z}\\ \longleftrightarrow}~~ x(k-1)$$

#### Consequência do teorema
- Tendo em conta o teorema 1 e a propagação de processos em sistemas dinâmicos (ambos acima), conseguimos modelar qualquer processo estocástico como sendo a saída de um SLIT Causal e estável em que a entrada é ruído branco:
![[sistema slit com ruido branco.png]]
- O termo de densidade espectral **também** pode ser usado para referir a transformada Z:
$$\Phi_{xx}(z)=\sum\limits_{\tau=-\infty}^{+\infty}\lambda_{xx}(\tau)z^{-\tau}$$
- Temos ainda que é preciso a função transferência ser estável para o processo ser estacionário e vice-versa.

## Previsão linear
- Seja $y(t)$ um processo estacionário de média nula. 
- O melhor previsor linear de  $y(t)$ será representado como $\hat{y}(t)$. A sua previsão no instante $t-1$ será representada como $\hat{y}(t|t-1)$. 
- Temos ainda o **erro** $\hat{e}(t)=y(t)-\hat{y}(t)=e(t)$. 
    - Quando $\hat{y}$ é o melhor previsor de $y$, o erro é **ruído branco** de média nula

### Dedução do previsor
- Temos as seguintes equações:
$$\begin{cases}
y(t)=H(z)e(t) \\
\hat{e}=y(t)-\hat{y}(t)=e(t)
\end{cases}$$
de onde podemos tirar:
$$\hat{y}(t)=y(t)-e(t)=H(z)e(t)-e(t)=e(t)[H(z)-1]$$
- Podemos ainda escrever $e(t)=H^{-1}(z)y(t)$ logo:
$$\hat{y}(t)=[1-H^{-1}(z)]y(t)$$

#### Exemplo
- Consideremos o processo estocástico dado por:
$$y(t)=u(t)+2u(t-1)$$
em que $u(t)$ é ruído branco de média nula e variância $\sigma_{u}^{2}=1$
- Podemos fazer transformada Z dos 2 lados acima:
$$Y(z)=U(z)+2z^{-1}U(z)~~\to~~ G(z)=\frac{Y(z)}{U(z)}=1+2z^{-1}=\frac{z+2}{z}$$
- Ou seja, temos a função transferência $G(z)$ tal que: $\Phi_{yy}(z)=G(z)G(z^{-1})\sigma_{u}^{2}$
- Como vimos acima, podemos definir então o estimar:
$$\begin{align*}
\hat{y}(t)&= [1-G^{-1}(z)]y(t)=\frac{2z^{-1}}{1+2z^{-1}}y(t)\\
\hat{y}(t)&= 2y(t-1) - 2\hat{y}(t-1)
\end{align*}$$
que nos permite estimar o estado com a saída e previsão anteriores. Mas esta formulação não nos diz nada. Podemos reescrever assim:
$$1-G^{-1}(z)=\frac{2z^{-1}}{1+2z^{-1}}=\frac{2}{z+2}$$
- Vemos que este sistema tem um polo em $-2$. Isto é **instável**!!!
    - É instável porque $-2$ está fora do circulo unitário no plano complexo
- Por ser instável, o erro vai-se acumulando e eventualmente a previsão "rebenta":
![[previsao instavel.png|500]]

### Melhor previsor
- Para obter o melhor previsor, precisamos de conseguir fatorizar o espetro na forma $\Phi_{yy}(z)=H(z)H(z^{-1})\sigma_{e}^{2}$ de forma que
    - **Função transferência linear** $H(z)=\sum_k h(k)z^{-k}$
    - **Fase mínima** $h(0)=1$
- Estas 2 condições garantem que a função de transferência é estável, com fase mínima. Isto por sua vez garante que os polos estão dentro do círculo unitário

#### Exemplo - continuação
- Temos a função transferência $G(z)=2+z^{-1}$
- Queremos então fazer com que se cumpra a condição $h(0)=1$. Ou seja:
$$H(z)=K(2+z^{-1})=2K + Kz^{-1}$$
e temos $h(0)=2K~,~h(1)=K$. Assim, forçamos: $K=0.5$
- Ficamos com a função de transferência normalizada:
$$H(z)=1+0.5z^{-1}$$
- Finalmente, temos o previsor:
$$\begin{align*}
\hat{y}(t)&= [1-H^{-1}(z)]y(t)=\left[1 - \frac{1}{1+0.5z^{-1}} \right]y(t)\\
&= \frac{0.5z^{-1}}{1+0.5z^{-1}}y(t)\\
\hat{y}(t) + 0.5z^{-1}\hat{y}(t)&= 0.5z^{-1}y(t)\\
\hat{y}(t)&= 0.5y(t-1) - 0.5 \hat{y}(t-1)=\frac{y(t-1)-\hat{y}(t-1)}{2}
\end{align*}$$
- E temos um previsor em que fazemos uma previsão a partir da saída e previsão anteriores. Sabemos que este sistema é estável

**Erro**
- Podemos escrever o erro assim:
$$\begin{align*}
\hat{e}(t)&= y(t)-\hat{y}(t)=y(t) - \frac{0.5z^{-1}}{0.5z^{-1}+1}y(t)\\
&= \frac{1}{0.5z^{-1}+1}y(r) = H_{\hat{e}}(z)y(t)
\end{align*}$$
- Podemos definir a densidade espectral do sinal como
$$\Phi_{yy}(z)=G(z)G(z^{-1})\sigma_{u}^{2}=\frac{z+2}{z}\frac{z^{-1}+2}{z^{-1}}\cdot1=(z+2)(z^{-1}+2)$$
(notemos que aqui usamos a função de transferência NÃO NORMALIZADA)

- Podemos então definir a densidade espectral do erro:
$$\begin{align*}
\Phi_{\hat{e}\hat{e}}(z)&= H_{\hat{e}}(z)H_{\hat{e}}(z^{-1})\Phi_{yy}(z)\\
&= \frac{1}{0.5z^{-1}+1} \frac{1}{0.5z+1} (z+2)(z^{-1}+2)\\
&= 4
\end{align*}$$
Ou seja, temos que $\hat{e}(t)$ é **ruído branco** com variância $\sigma_{e}^{2}=4$
- Notemos que esta é maior que a variância da entrada do sistema, $\sigma_{u}^{2}=1$
![[previsao estavel.png]]