(Esta aula já não é copiada dos apontamentos do Diogo. Foi uma aula de 2h)
**Variável Intensiva** - variável que não varia com o tamanho da amostra (EX: densidade da água; é a mesma independentemente do volume de água que temos)

- Num sistema física temos que as grandezas naturalmente flutuam. No entanto, se considerarmos um sistema maior, as flutuações eventualmente tornam-se negligenciáveis. 
- Assim, consideremos que uma experiência com distribuição binomial é realizada $N$ vezes, em que temos $n$ sucessos. Assim, podemos traçar o gráfico $N(n)$:
![[grafico n(N) binomial.png|450]]

- Podemos então definir a variável $x=\frac{n}{N}$ pelo que $\langle x\rangle=\frac{\langle n\rangle}{N}=p$ (probabilidade de ocorrer um sucesso).
- Temos então a variância deste gráfico: $\sigma^{2}=\langle x^{2}\rangle-\langle x\rangle= \frac{p(1-p)}{N}$, que corresponde ao desvio padrão: $\sigma=\sqrt{\frac{p(1-p)}{N}}$
- Podemos traçar um histograma de $x$:
![[x=n dividir por N.png|450]]

- Ora, se tivermos um $N$ muiiiiiito elevado temos o histograma:
![[x quando N infinito.png|450]]

- O histograma terá largura proporcional a $1/\sqrt{N}$. A distância entre 2 bins será $1/N$.
- Ora, o número de bins será da ordem de $N/\sqrt{N}=\sqrt{N}$

## Fórmula de Stirling
- Ou seja, com $N$ muito elevado podemos aproximar o sistema a um sistema contínuo. Ora, surge um problema em converter uma distribuição binomial para o contínuo: **fatoriais**. Vejamos como resolver isso.
- Um integral pode ser definido em forma integral como:
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
$$\begin{align*}\\
f(x)=M\ln(x)-x &&; \quad\quad &f(M)=M\ln M-M\\
f'(x)=\frac{M}{x}-1 &&; \quad\quad &f'(M)=0\\
f''(x)=\frac{-M}{x^{2}}&&; \quad\quad &f''(M)=\frac{-1}{M}\\
f'''(x)=\frac{2M}{x^{3}} &&; \quad\quad &f'''(M)=\frac{2}{M^{2}}
\end{align*}$$
e temos: $f(x)\simeq M\ln M-M - \frac12\frac{(x-M)^{2}}{M}+ \frac{2}{M^{2}} \frac{(x-M)^3}{3!}$ . Vemos que os termos têm $M$ no denominador, com expoente a aumentar com os termos. Ora, sendo $M$ um valor elevado, é razoável aproximar os termos após o 2º a zero. Assim ficamos com: $f(x)\sim M\ln M-\frac{1}{2} \frac{(x-M)^{2}}{M}$. Ao substituir acima ficamos com:
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


- Da aula anterior temos $$P_{N}(n)=\frac{N!}{n!(N-n)!} p^{n}(1-p)^{N-n}$$
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

- Ora, temos aqui um *integral condutor*. Isso acontece quando temos algo do tipo $e^{N f(x)}$. Na grande maioria dos casos, consoante $N$ aumenta, a função fica mais estreita à volta dos picos. Eventualmente, quando $N\to\infty$ a função torna-se uma espécie de delta de Dirac centrada num dos máximos. Por outras palavras, com $N\to\infty$ o integral da função é dominado por uma vizinhaça muito muito estreita.
![[integral condutor.png]]

- Assim surge uma questão: será que o nosso $f(x)$ acima tem um máximo? Vejamos:
$$\begin{align*}
f'(x)&= -\ln x-1 + \ln(1-x)-(1-x)\frac{-1}{1-x}+\ln p -\ln(1-p)=-\ln x + \ln(1-x)+\ln p -\ln(1-p)\\
f'(x)&= 0 \to \ln\left(\frac{1-x}{x}\right)=\ln\left(\frac{1-p}{p}\right) \to x_{Max}=p
\end{align*}$$
a função tem, então, um máximo igual à probabilidade de ocorrer um sucesso.
- Façamos então série de Taylor de $f$ em torno de $x=p$. Temos: $$f''(x)=- \frac{1}{x}- \frac{1}{1-x} \quad \quad; \quad \quad f''(p)=- \frac{1}{p}- \frac{1}{1-p}$$
e temos de trás $f(x)=- x\ln x - (1-x)\ln(1-x) + x\ln p + (1-x)\ln (1-p)$. Assim temos:
$$\ln P_{N}(Nx)=N(-\bcancel{p\ln p} - \cancel{(1-p)\ln(1-p)} + \bcancel{p\ln p}+ \cancel{(1-p)\ln(1-p)})- \frac{1}{2!}\frac{(x-p)^{2}}{p(1-p)}$$
e ficamos com:
$$\boxed{\large P_{N}(Nx)=\frac{e^{- \frac{1}{2} \frac{N(x-p)^{2}}{p(1-p)}}}{N \sqrt{2\pi \frac{p(1-p)}{N}}}}$$

---
- Consideremos que temos a densidade de probabilidade de um espaço de acontecimentos com $N$ variáveis é dada por:
$$\rho(x_{1},x_{2},\dots,x_{N})=\omega(x_{1})\omega(x_{2})\dots \omega(x_{N})$$
sendo $x=(x_{1},x_{2},\dots,x_{N})$ temos:
$$\begin{align*}
\rho(x)&= \langle \textsf{Função Indicadora}\rangle\\
&= \int dx_{1} \int dx_{2}\dots\int dx_{N}\prod\limits_{i=1}^{N}\omega(x_{i})\delta\left(x-\sum\limits_{i=1}^{N}x_{i}\right)
\end{align*}$$
- Podemos fazer a transformada de fourier desta densidade:
$$\begin{align*}
\tilde\rho(k) &= \int_{-\infty}^{+\infty}dx~\rho(x)e^{-ikx}\\
&= \int_{-\infty}^{+\infty}dx~\int dx_{1}dx_{2}\dots dx_{N} \prod\limits_{i=1}^{N} \omega(x_{i}) \delta\left(x -\sum\limits_{i=1}^{N}x_{i}\right)e^{-ikx}\\
&= \int dx_{1}dx_{2}\dots dx_{N} \prod\limits_{i=1}^{N} \omega(x_{i})\int \delta\left(x -\sum\limits_{i=1}^{N}x_{i}\right)e^{-ikx}dx\\
&= \int dx_{1}dx_{2}\dots dx_{N} \prod\limits_{i=1}^{N} \omega(x_{i}) e^{-ik\sum\limits_{i=1}^{N}x_{i}}\\
&= \left[ \int dx_{1} \omega(x_{i}) e^{-ikx_{1}} \right]^{N}\\
&= \left[ \left\langle e^{-ikx} \right\rangle_{\omega}  \right]^{N}\\
&= e^{N(\ln\left\langle e^{-ikx} \right\rangle_{\omega})}
\end{align*}$$

- Temos então:
$$\begin{align*}
\ln\tilde\rho(k) &= N \langle e^{-ikx}\rangle\\
&= N \left(-ik k_{1} + \frac{(ik)^{2}}{2!}k_{2} + \frac{(ik)^{3}}{3!}k_{3} + \frac{(ik)^{4}}{4!}k_{4}\right)\\
&= N \left(-ik \langle x\rangle_{\omega} + \frac{(ik)^{2}}{2!}(\langle x^{2}\rangle_{\omega} - \langle x\rangle_{\omega}^{2}) + \frac{(ik)^{3}}{3!}k_{3} + \frac{(ik)^{4}}{4!}k_{4}\right)
\end{align*}$$
em que se fez a decomposição do valor médio em Cumulantes.

- Ora, podemos fazer a transformada de Fourier inversa, sendo que temos:
$$\begin{align*}
\rho(x)&= \frac{1}{2\pi} \int dk~\tilde\rho(k) e^{ikx}\\
&= \frac{1}{2\pi} \int dk~e^{N \left(-ik \langle x\rangle + \frac{(ik)^{2}}{2!}\sigma^{2} + \frac{(ik)^{3}}{3!}k_{3} + \frac{(ik)^{4}}{4!}k_{4}\right)}\\
&= \frac{1}{2\pi} \int dk~ e^{-ik(N \langle x\rangle -x) + N\left(\frac{(ik)^{2}}{2!}\sigma^{2} + \frac{(ik)^{3}}{3!}k_{3} + \frac{(ik)^{4}}{4!}k_{4}\right)}\\
\end{align*}$$
podemos fazer a substituição $$y=\frac{x-N \langle x\rangle}{\sqrt{N}} \to N \langle x\rangle-x=- \sqrt{N}y  \quad \quad;\quad \quad dy=\frac{1}{\sqrt{N}}dx$$
- Ora, pode ser establecida então a relação $\rho(y)=\rho(x)\sqrt{N}$ e podemos substituir:
$$\begin{align*}
\rho(y)&= \frac{1}{2\pi} \int dk~e^{-ik \sqrt{N}y + N\left(\frac{(ik)^{2}}{2!}\sigma^{2} + \frac{(ik)^{3}}{3!}k_{3} + \frac{(ik)^{4}}{4!}k_{4}\right)}\\
&= \frac{1}{2\pi} \int dk'~e^{-ik'y + N\left(\frac{(ik')^{2}}{2!N}\sigma^{2} + \frac{(ik')^{3}}{3!N\sqrt{N}}k_{3} + \frac{(ik')^{4}}{4!N^{2}}k_{4}\right)} \quad \quad (k'=k \sqrt{N} ~~~,~~~ k= \tfrac{k'}{\sqrt{N}})\\
&= \frac{1}{2\pi}\int dk'~e^{-ik'y + \frac{(ik')^{2}}{2!}\sigma^{2}+ \frac{(ik)^{3}}{3!} \frac{k_{3}}{\sqrt{N}} + \frac{(ik')^{2}}{4!} \frac{k_{4}}{N}}
\end{align*}$$
- Ora, vemos que consoante a série de Taylor se extende, o expoente de $N$ (no denominador) aumenta. Assim, para $N$ grande podemos presumir que todos os termos a partir do terceiro se anulam. Assim:
$$\lim\limits_{N\to\infty} \rho(y)\to \rho(y)= \frac{1}{2\pi}\int dk'~ e^{-ik'y - \frac{k'^{2}\sigma^{2}}{2}}$$
podemos completar o quadrado e temos:
$$\begin{align*}
\rho(y)&= \frac{1}{2\pi} \int dk'~ e^{\frac{-\sigma^{2}}{2} \left(k'^{2}+ 2 \frac{ik}{\sigma^{2}}k' - \frac{y^{2}}{\sigma^{4}} + \frac{y^{2}}{\sigma^{4}}\right)}\\
&= \frac{e^{\frac{-y^{2}}{2\sigma^{2}}}}{2\pi} \int dk'~ e^{\frac{-\sigma^{2}}{2}(k'+ \frac{iy}{\sigma^{2}})^{2}}\\
&= \frac{e^{\frac{-y^{2}}{2\sigma^{2}}}}{\sqrt{2\pi\sigma^{2}}}
\end{align*}$$
 