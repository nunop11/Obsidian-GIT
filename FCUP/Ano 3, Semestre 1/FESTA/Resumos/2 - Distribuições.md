# 0 - "Intro"
## 0.1 - Variáveis Extensivas e Intensivas
**Extensivas** - Dependem da extensão do sistema (EX:  massa ou volume)
**Intensivas** - Não dependem da extensão do sistema (EX: densidade)

## 0.2 - Termodinâmica e estatística
- Em muitas distribuições, se tivermos um nº suficientemente grande de amostras vemos que a dispersão relativa será muito reduzida. 
- Assim temos a Termodinâmica, em que usamos teorias microscópicas da matéria para tirar conclusões sobre o comportamento macroscópico.

# 1 - Distribuição Binomial
- Temos uma VA que tem $N$ elementos que podem ser $1$ ou $0$: $$X=\{0,0,1,0,\dots,1,0,0,1,1,\}$$
em que podemos definir $p(1)=p~,~p(0)=1-p$.
- Sendo $n$ o número de vezes que $1$ ocorre temos que a probabilidade de uma qualquer configuração ter este número de $1,0$ é:
$$p^{n}(1-p)^{N-n}$$
- Se considerarmos as posições dos $1$ e $0$ temos que a probabilidade de ter  uma certa configuração é:
$$\boxed{P(n)=\frac{N!}{n!(N-n)!}p^{n}(1-p)^{N-n}}$$
em que, se definirmos $q=1-p$ temos que a soma de todas as possibilidades é 1:
$$\begin{align*}
\sum\limits_{n=0}^{N}\frac{N!}{n!(N-n)!}p^{n}q^{N-n}=1=(p+q)^{N}
\end{align*}$$
- Aqui podemos fazer outra interpretação: Repetimos $N$ vezes uma experiência. Cada vez que a fazemos só temos 2 outcomes possíveis: $1,0$ (sucesso ou insucesso). Considerando $p$ a probabilidade de sucesso, esta repetição de experiências segue uma distribuição binomial.

**Média**
$$\begin{align*}
\langle n\rangle&= \sum\limits_{n=0}^{N}nP(n)\\
&= \sum\limits_{n=0}^{N}n\frac{N!}{n!(N-n)!}p^{n}(1-p)^{N-n}\\
&= p \frac{d}{dp}\sum\limits_{n=0}^{N}\frac{N!}{n!(N-n)!}p^{n}(1-p)^{N-n}\\
&= \lim\limits_{q\to1-p}p \frac{d}{dp}\sum\limits_{n=0}^{N}\frac{N!}{n!(N-n)!}p^{n}q^{N-n}\\
&= \lim\limits_{q\to1-p}~p \frac{d}{dp}(p+q)^{N}\\
&= pN\lim\limits_{q\to1-p}~ (p+q)^{N-1}\\
&= Np
\end{align*}$$
**Média Quadrática**
$$\begin{align*}
\langle n^{2}\rangle&= \sum\limits_{n=0}^{N}n^{2}P(n)\\
&= \sum\limits_{n=0}^{N}n^{2}\frac{N!}{n!(N-n)!}p^{n}(1-p)^{N-n}\\
&= p \frac{d}{dp}\sum\limits_{n=0}^{N}n\frac{N!}{n!(N-n)!}p^{n}(1-p)^{N-n}\\
&= p \frac{d}{dp}p \frac{d}{dp}\sum\limits_{n=0}^{N}\frac{N!}{n!(N-n)!}p^{n}(1-p)^{N-n}\\
&= \lim\limits_{q\to1-p} p \frac{d}{dp}p \frac{d}{dp}(p+q)^{N}\\
&= \lim\limits_{q\to1-p} p \frac{d}{dp}Np(p+q)^{N-1}\\
&= \lim\limits_{q\to1-p}Np((p+q)^{N-1}+p(N-1)(p+q)^{N-2})\\
&= Np[1+p(N-1)]
\end{align*}$$
(nas 2 deduções acima introduzimos o termo $p \frac{d}{dp}$. Basta fazer a derivada do somatório em $p$ e multiplicar por $p$ para ver que obtemos o termo de cima. A base deste passo é: $p \frac{d}{dp}(p^{n})=p\cdot np^{n-1}=np^{n}$)

**Variância**
$$\text{Var}(n)=\langle n^{2}\rangle-\langle n\rangle^{2}=Np(1-p)$$
**Desvio padrão**
$$\sigma_{n}=\sqrt{Np(1-p)}$$
**Coeficiente de Variação**
$$CV=\frac{\sigma_{n}}{\langle n\rangle}=\sqrt{\frac{1-p}{Np}}$$
**Função Caraterística**
- Podemos determinar:
$$\begin{align*}
\langle e^{ikn}\rangle&= \sum\limits_{n=0}^{N}e^{ikn}P(n)= \sum\limits_{n=0}^{N} \frac{N!}{n!(N-n)!}p^{n}(1-p)^{N-n}\\
&= \sum\limits_{n=0}^{N} \frac{N!}{n!(N-n)!}(pe^{ik})^{n}(1-p)^{N-n}\\
&= (pe^{ik}+1-p)^{N}\\\\
\phi_{n}(ik)&= (pe^{ik}+1-p)^{N}
\end{align*}$$
(o último passo ocorre de literalmente termos a expressão do binómio de Newton)

#### Variável Intensiva
- Por definição, $n$ será uma variável extensiva (quantos mais ensaios se fizerem, inevitavelmente teremos mais $1$s). No entanto, facilmente definimos uma **variável intensiva**:
$$x=\frac{n}{N}$$
$x$ é intensiva porque quanto maior $N$, menos $x$ irá variar (flutuações tornam-se desprezáveis).

vejamos agora os parâmetros estatísticos desta nova variável:
**Média**
$$\langle x\rangle=\frac{\langle n\rangle}{N}=p$$
**Média Quadrática**
$$\langle x^{2}\rangle=\frac{\langle n^{2}\rangle}{N^{2}}=\frac{p}{N}[1+p(N-1)]=\frac{(N-1)p^{2}+p}{N}$$
**Variância**
$$\text{Var}(x)=\langle x^{2}\rangle-\langle x\rangle^{2}=\frac{(N-1)p^{2}+p}{N}-p^{2}=\frac{p-p^{2}}{N}=\frac{p(1-p)}{N}=\frac{\text{Var}(n)}{N^{2}}$$
**Desvio padrão**
$$\sigma_{x}=\sqrt{\text{Var}(x)}=\sqrt{\frac{p(1-p)}{N}}=\frac{\sigma_{n}}{N}$$

# 2 - Passagem ao Contínuo
- Consideremos um histograma de $x$. Teremos $N$ barras.  Consideremos ainda que temos muiiiiiitas barras AKA $N$ muito elevado. Temos uma aproximação do contínuo.
- A largura da distribuição irá seguir $\sigma_{x}\propto 1/\sqrt{N}$
- A distância entre 2 barras será $\frac{1}{N}$
- A quantidade de barras no intervalo $\pm\sigma_{x}$ em torno da média será $\propto N\sigma_{x}=\sqrt{N}$

# 3 - Fórmula de Stirling
- Com $N$ muito elevado podemos aproximar o sistema binomial discreto a um sistema contínuo. Ora, surge um problema: **fatoriais**. Vejamos como resolver isso.
- Um fatorial pode ser definido em forma integral como:
$$\begin{align*}
M!&= \int_{0}^{+\infty}dx ~ x^{M}e^{-x}=I_{M}\\
&= -x^{M}e^{-x}\biggr|_{0}^{+\infty} + M\int_{0}^{+\infty}dx~x^{M-1}e^{-x}\\
&= M\int_{0}^{+\infty}dx~ x^{M-1} e^{-x}
\end{align*}$$
Ou seja:
$$I_{M}=MI_{M-1}=M(M-1)I_{M-2}=M(M-1)(\cdots)3\cdot2\cdot1=M!$$
e demonstramos então que este integral nos dá o fatorial. Substituindo $M=0,M=1$ conseguimos ainda verificar que $0!=1!=1$

- Podemos reescrever a integral acima assim:
$$M!=\int_{0}^{+\infty}dx~x^{M}e^{-x}=\int_{0}^{+\infty}dx~e^{M\ln(x)-x}=\int_{0}^{+\infty}dx~e^{f(x)} \quad\quad;\quad\quad f(x)=M\ln x-x$$
- Temos que $f'(x)=\frac{M}{x}-1$. Assim, o máximo de $f(x)$ ocorrerá em $f'(x)=0\to x=M$. 
 
- Vejamos então como fica a série de Fourier de $f$:
$$\begin{align*}
f(x)=M\ln(x)-x &&; \quad\quad &f(M)=M\ln M-M\\
f'(x)=\frac{M}{x}-1 &&; \quad\quad &f'(M)=0\\
f''(x)=\frac{-M}{x^{2}}&&; \quad\quad &f''(M)=\frac{-1}{M}\\
f'''(x)=\frac{2M}{x^{3}} &&; \quad\quad &f'''(M)=\frac{2}{M^{2}}
\end{align*}$$
e temos: $f(x)\simeq M\ln M-M - \frac1M\frac{(x-M)^{2}}{2!}+ \frac{2}{M^{2}} \frac{(x-M)^3}{3!}$ . Vemos que os termos têm $M$ no denominador, sendo que o expoente vai aumentando consoante acrescentamos termos. Ora, sendo $M$ um valor elevado, é razoável anular os termos após o 2º a zero. Assim ficamos com: $f(x)\sim M\ln M-\frac{1}{2} \frac{(x-M)^{2}}{M}$. Ao substituir acima ficamos com:
$$\begin{align*}
M!&= \int_{0}^{+\infty} dx~e^{-x}x^{M}\\
&= e^{M\ln M-M}\int_{0}^{+\infty} dx~e^{- \frac{(x-M)^{2}}{2M}}
\end{align*}$$
ora, isto **quase** é um integral gaussiano, mas de $[0,+\infty]$ invés de $[-\infty,+\infty]$. No entanto, se $M$ for muito elevado podemos aproximar os intervalos e temos: 
$$\begin{align*}
M!&= e^{M\ln M-M}\int_{0}^{+\infty} dx~e^{- \frac{(x-M)^{2}}{2M}}\\
&= \sqrt{2\pi M}e^{M\ln M-M}
\end{align*}$$
o que nos dá a **_Fórmula de Stirling_**:
$$\boxed{\ln(M!)=M\ln M-M + \frac12 \ln(2\pi M)}$$
que é uma boa aproximação a partir de $M=10$.

# 4 - Generalizar Distribuição Binomial
- Temos $$P_{N}(n)=\frac{N!}{n!(N-n)!} p^{n}(1-p)^{N-n}$$
e obtemos
$$\ln P_{N}(n)=\ln N! - \ln n! - \ln(N-n)! + n\ln p+(N-n)\ln(1-p)$$
substituindo a fórmula de Stirling:
$$\begin{align*}
\ln P_{N}(n)&= N\ln N-\cancel{N} + \frac{1}{2}\ln2\pi N- n\ln n + \bcancel{n} - \frac{1}{2}\ln2\pi n- (N-n)\ln (N-n) + \\&+ \cancel{N}-\bcancel{n} - \frac{1}{2}\ln2\pi(N-n) + n\ln p + (N-n)\ln(1-p)
\end{align*}$$
recordando que se definiu $x=n/N$, ou seja: $n=Nx$. Substituindo:
$$\begin{align*}
\ln P_{N}(Nx)&= \cancel{N\ln N} + \bcancel{\frac{1}{2}\ln2\pi N }- xN\ln x-\cancel{xN\ln N}- \bcancel{\frac{1}{2}\ln2\pi N} -(1-x)N\ln(1-x)-\\
&- \cancel{(1-x)N\ln N}- \frac{1}{2} \ln2\pi(1-x)- \frac{1}{2}\ln2\pi N + N\ln p + N(1-x)\ln(1-p)\\
&= N \left[- x\ln x - (1-x)\ln(1-x) + x\ln p + (1-x)\ln (1-p) - \frac{1}{2}\ln(2\pi x(1-x)N)\right]
\end{align*}$$

Ou seja temos: $f(x)=- x\ln x - (1-x)\ln(1-x) + x\ln p + (1-x)\ln (1-p)$. Assim fica: $$P_{N}(Nx)=\frac{e^{N f(x)}}{\sqrt{2\pi x(1-x)N}}$$

**Máximos**
- Podemos definir:
$$\begin{align*}
f'(x)&= -\ln x-1+\ln(1-x)+1+\ln p-\ln(1-p)\\
&= -\ln x +\ln(1-x)+\ln p-\ln(1-p)\\
f''(x)&= -\frac{1}{x}- \frac{1}{1-x} =-\frac{1}{x(1-x)}<0
\end{align*}$$
- Assim, temos um máximo em
$$f'(x)=0\to x=p$$

### Distribuição Normal
- Se expandirmos $f(x)$ em torno de $x=p$ conseguimos obter:
$$\ln P(Nx)\approx \frac{-1}{2}\frac{(x-p)^{2}}{p(1-p)/N}-\frac12\ln(2\pi p(1-p)N)$$e resulta:
$$P(Nx)=\frac{\exp\left(-{\frac{(x-p)^2}{2p(1-p)/N}}\right)}{\sqrt{2\pi p(1-p)N}}$$
- Temos que $P(Nx)\to0$, o que faz sentido, porque numa distribuição contínua a probabilidade de medir 1 valor só é zero.

- Podemos definir a densidade de probabilidade:
$$\rho(x)=\frac{dP}{dx}$$
como a distância entre barras consecutivas no histograma que referimos acima é $1/N$ isso significa que $dx=1/N$, logo:
$$\rho(x)=\frac{\exp\left(-{\frac{(x-p)^2}{2p(1-p)}}\right)}{\sqrt{\frac{2\pi p(1-p)}{N}}}$$
- Sendo $\mu=p$ e $\sigma^{2}=\frac{p(1-p)}{N}$ podemos escrever:
$$\rho(x)=\frac{\exp\left(-{\frac12\left(\frac{x-\mu}{\sigma}\right)^2}\right)}{\sqrt{2\pi \sigma^2}}$$
ou seja, a densidade segue uma **distribuição normal** para $N$ suficientemente elevado.

# 5 - Distribuição Normal
- Sendo $X$ uma VA com distribuição normal, temos a sua densidade de probabilidade:
$$\rho(x)=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{\frac{-1}{2} \left(\frac{x-\mu}{\sigma}\right)^{2}}$$
em que $E(X)=\mu~~,~~\text{Var}(X)=\sigma^{2}$

- A função caraterística é $$\langle e^{ikx}\rangle=\tilde \rho(ik)=\exp(ik\mu-\frac{k^{2}\sigma^{2}}{2})$$
(sendo $\tilde \rho$ a transformada de Fourier da função de densidade de probabilidade)

## 5.1 - Momentos
### Distribuição Normal Padrão
- Temos uma variável $Y$ com $\mu_{Y}=0,\sigma^{2}_{Y}=1$. 
- Podemos definir:
$$y=g(x)=\frac{x-\mu}{\sigma} \quad \quad;\quad \quad dy=\frac{dx}{\sigma}$$
e temos:
$$\begin{align*}
\rho_{Y}(y)&= \int dx~\delta(y-g(x))\rho_{X}(x)\\
&= \int dx~\delta\left(y-\frac{x-\mu}{\sigma}\right)\rho_{X}(x)\\
&= \rho_{X}(\sigma y+\mu)=\frac{1}{\sqrt{2\pi\sigma^{2}}}e^{\frac{-1}{2} \left(y\right)^{2}}=\frac{1}{\sqrt{2\pi}}e^{\frac{-1}{2} \left(y\right)^{2}}~~~~(\sigma^{2}=1)
\end{align*}$$
(em que para eliminar o integral usamos $\delta(y-\frac{x-\mu}{\sigma})\neq0\to y=\frac{x-\mu}{\sigma}\to x=\sigma y+\mu$)
- Podemos então calcular os momentos usando:
$$\langle y^{n}\rangle=\int y^{n}\rho_{Y}(y)dy=\int y^{n} \frac{1}{\sqrt{2\pi}}e^{\frac{-1}{2}y^{2}}$$
ora, para $m$ ímpar temos integral nulo porque ficamos com uma função ímpar. Podemos generalizar o integral gaussiano:
$$I_{m}(\lambda)=\int_\mathbb{R} y^{2m}\frac{1}{\sqrt{2\pi}}e^{- \frac{\lambda}{2}y^{2}}dy$$
ora, para $m$ ímpar temos integral nulo porque ficamos com uma função ímpar.
- Podemos calcular:
$$\begin{align*}
I_{0}(\lambda)=\int_\mathbb{R} \frac{1}{\sqrt{2\pi}}e^{- \frac{\lambda}{2}y^{2}}dy=\frac{\sqrt{2\pi}}{\sqrt{2\pi\lambda}}=\lambda^\frac{-1}{2}
\end{align*}$$
$$I_{1}(\lambda)=\int_\mathbb{R}\frac{1}{\sqrt{2\pi}}y^{2}e^{\frac{-\lambda}{2}y^{2}}dy=-2 \frac{d}{d\lambda}\int_\mathbb{R} \frac{1}{\sqrt{2pi}}e^{\frac{-\lambda}{2}y^{2}}dy=-2 \frac{d}{d\lambda}I_{0}=\lambda^\frac{-3}{2}$$
(basta fazer a derivada em $\lambda$ do 2º integral para entender o passo feito)
- E em forma geral:
$$I_{m}(\lambda)=(-2)^{m}\frac{d^{m}I_{0}}{d\lambda^{m}}=(2m-1)!! ~\lambda^{-(2m+1)/2}$$
- Sendo $\lambda=1$ temos os momentos:
$$\langle y^{2m}\rangle=(2m-1)!!$$

### Distribuição normal genérica
$$\langle x^n\rangle=\sum_{m=0}^n \frac{n!}{m!(n-m)!}\ \mu^{n-m}\ \sigma^m\ \langle y^m\rangle$$
esta não percebo, é só aceitar.

## 5.2 - Cumulantes
- Temos $$c_{1}=\mu \quad \quad;\quad \quad c_{2}=\sigma^{2}$$
os restantes cumulantes são todos nulos. 

# 6 - Integrais Gaussianos
- Integral do tipo:
$$\int_{-\infty}^{+\infty}e^{-x^{2}}dx=\sqrt{\pi}$$
- Uma forma de calcular isto:
$$\begin{align*}
I^{2}&= \int_{-\infty}^{+\infty}e^{-x^{2}}dx ~\cdot~\int_{-\infty}^{+\infty}e^{-y^{2}}dy\\
&= \int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}e^{-(x^{2}+y^{2})}dxdy\\
&= \int_{0}^{2\pi}\int_{0}^{+\infty}e^{-r^{2}}~rdrd\phi\\
&= 2\pi \left[- \frac{1}{2}e^{-r^{2}}\right]_{0}^{+\infty}\\
&= \pi\\
I&= \sqrt{\pi}
\end{align*}$$


## 6.1 - Integral de Gaussiana Geral:
- Consideremos a gaussiana geral: $$I=\int_{-\infty}^{+\infty}e^{-a(x+b)^{2}}dx$$
- Fazendo as substituições: $x'=x+b$ e $y'=y+b$:
$$\begin{align*}
I^{2}&= \int_{-\infty}^{+\infty}e^{-a(x+b)^{2}}dx~\cdot~\int_{-\infty}^{+\infty}e^{-a(y+b)^{2}}dy\\
&= \int_{-\infty}^{+\infty}e^{-a(x')^{2}}dx ~\cdot~\int_{-\infty}^{+\infty}e^{-a(y')^{2}}dx\\
&= \int_{-\infty}^{+\infty}e^{-a((x')^{2}+(y')^{2})}dxdy\\
&= \int_{0}^{2\pi}\int_{0}^{+\infty}e^{-a(r')^{2}}r'~dr'd\phi\\
&= 2\pi \left[-\frac{1}{2a}e^{-a(r')^{2}}\right]_{0}^{+\infty}\\
&= \frac{\pi}{a}\\
I&= \sqrt{\frac{\pi}{a}}
\end{align*}$$

# 7 - Teorema do Limite Central
- Tendo-se $N\in\mathbb{N}$ e um conjunto de VAs $x_{i}~~(i\in\{0,\dots,N-1\})$. Estas VA são 
    - independentes
    - identicamente distribuidas, sendo para cada uma delas temos uma densidade $\omega(x)$ com $E(X)=\mu~,~\text{Var}(X)=\sigma^{2}<\infty$
- Podemos definir uma VA: $$X=\sum\limits_{i=0}^{N-1}x_{i}$$
- Consideremos agora que o conjunto de VAs é uma amostra recolhida. Sendo das VA identicamente distribuidas temos que a probabilidade associada a 1 amostra em específico é:
$$\rho(\vec{r})d\vec{r}=\prod_{i=0}^{N-1}\omega(x_{i})dx_{i} \quad \quad;\quad \vec{r}=(x_{0},x_{1},\dots,x_{N-1})$$
podemos então calcular:
$$\rho(X)=\int d\vec{r}~\delta\left(X-\sum\limits_{i}x_{i}\right)\prod_{i=0}^{N-1}\omega(x_{i})$$
e podemos definir a função caraterística:
$$\begin{align*}
\phi(k)=\langle e^{-ikX}\rangle&= \int dX \rho(X)e^{-ikX}\\
&= \prod_{i=0}^{N-1}\left(\int dx_{i}~\omega(x_{i})e^{-ikx_{i}}\right)\\
&= \left(\int dx~\omega(x)e^{-ikx}\right)^{N}
\end{align*}$$
em que podemos notar que: $\phi(k)=\tilde \rho(k)$.
- Intuitivamente vemos que o máximo da função será para $k=0$.
- Podemos então fazer: $$\ln\phi=N\ln\langle e^{-ikx}\rangle$$
e podemos fazer expansão em cumulantes de $\ln\langle e^{-ikx}\rangle$:
$$\ln\phi=N\left(-ikc_1 + \frac12(-ik)^2c_2 + \frac1{3!}(-ik)^3c_3 + \frac1{4!}(-ik)^4c_4 + \cdots\right)$$
- Sendo $\phi(k)=\tilde \rho(k)$ podemos obter novamente $\rho(X)$ usando a transformada de Fourier inversa:
$$\begin{align*} \rho(X) &= \frac1{2\pi}\int_{-\infty}^{+\infty}\tilde \rho(k) e^{ikx}\ dk \\ 
&= \frac1{2\pi}\int_{-\infty}^{+\infty}\exp\left(N\left((-ik)c_1 + \frac12(-ik)^2c_2 + \frac16(-ik)^3c_3 + \frac1{24}(-ik)^4c_4 + \cdots\right)\right)e^{ikx}\ dk \\
 &= \frac1{2\pi}\int_{-\infty}^{+\infty}\exp\left((-ik)(\langle x_i\rangle N - x) + \frac12(-ik)^2\sigma^2N + \frac16(-ik)^3c_3N + \frac1{24}(-ik)^4c_4N + \cdots\right)\ dk \end{align*}$$
(em que $\sigma^{2}$ é a variância de 1 das variáveis da amostra, $x_{i}$)

- Fazemos então uma mudança de variável:
$$Y=\frac{X-N\mu}{\sqrt{N}}$$
que tem densidade de probabilidade $\rho(y)$ e obtemos:
$$\rho(y) = \frac{\sqrt N}{2\pi}\int_{-\infty}^{+\infty}\exp\left((ik)y\sqrt N + \frac12(-ik)^2\sigma^2N + \frac16(-ik)^3c_3N + \frac1{24}(-ik)^4c_4N + \cdots\right)\ dk$$
e definindo $s=k\sqrt{N}$ temos:
$$\rho(y) = \frac{1}{2\pi}\int_{-\infty}^{+\infty}\exp\left((is)y -\frac12(s)^2\sigma^2 + \frac16(-is)^3c_3/\sqrt N + \frac1{24}(-is)^4c_4/N + \cdots\right)\ ds$$
- Se $N$ for muito elevato obtemos:
$$\rho(y)\approx \frac{1}{\sqrt{2\pi\sigma^{2}}}e^{-\frac{y^{2}}{2\sigma^{2}}}$$
e podemos voltar atrás e obter:
$$\rho(X) \approx \frac1{\sqrt{2\pi N\sigma^2}}e^{-\frac{\left(x-\mu N\right)^2}{2(N\sigma)^2}}$$sendo este o **Teorema do limite central**
- Se tivermos $N$ amostras $x_i$ com distribuições idênticas $\omega(x_i)$ finitas, então consoante $N\to\infty$ mais a distribuição $\rho(X)$ se aproxima de uma distribuição normal com $\sigma^{2}_{X}=(N \sigma)^{2}$ e $\mu_{X}=\mu N$
- 