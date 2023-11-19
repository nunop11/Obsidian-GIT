- Ou seja, o poço infinito temos:
    - $\psi_{n}=C \sin(k_{n}x)~~~~;~~~~ k_{n}=\frac{n\pi}{a}$
    - $E_{n}=\frac{\hbar^{2}k_{n}^{2}}{2m}= \frac{n^{2}\pi^{2}\hbar^{2}}{2ma^{2}}$

- Ora, a normalização de $\psi_{n}$ depende de $C$:
$$1=\int_{0}^{a} |C|^{2} \sin^{2}(k_{n}x)dx=|C|^{2} \frac{a}{2} ~~\to~~ C=\sqrt{\frac{2}{a}} $$
e temos que, normalizada, a função de onda fica na forma:
$$\psi_{n}(x)=\sqrt{\frac{2}{a}} \sin \left( \frac{n\pi}{a}x \right)~~~~~~~~(n\in\mathbb{N})$$

### Algumas Observações
**1.**
------------- modos normais de psi - poço -----------------
- Vemos então que as funções $\psi_{n}$ alternam entre ser par e ímpares em torno de $x=a/2$. 
- Vemos ainda que cada $\psi_{n}(x)$ tem $n-1$ zeros (sem contar com $x=0,x=a$)

**2.**
- Tem-se ainda que, como $E_{n}\ne E_{m}$, os estados $\psi_{n},\psi_{m}$ são **ortogonais**. Temos então:
$$\langle \psi_{m}| \psi_{n}\rangle=\int dx ~\psi_{m}^{*} (x) \psi_{n}(x)=\delta_{nm}~~~~ \textsf{(delta de Kronecker)}$$
- Assim, estas funções ortogonais formam uma base completa das funções de onda para $x\in[0,a]$. Qualquer função de onda solução da Eq Schrödinger normalizável pode ser escrita como uma combinação linear de estados estacionários ortogonais:
$$f(x)=\sum\limits_{n=1}^{\infty} c_{n} \psi_{n}(x)=\sqrt{\frac{2}{a}} \sum\limits_{n=1}^{\infty} c_{n}\sin\left(\frac{n\pi}{a}x\right)$$
- Ora, para UM estado basta ter $C=\sqrt{\frac{2}{a}}$ para que a função de onda esteja normalizada. Vejamos então quais os valores dos coeficientes $c_{n}$ necessários para que $f(x)$ esteja normalizado. Temos:
$$\begin{align*}
\int dx~|f(x)|^{2}&= 1\\
\int dx~f^{*}(x)f(x)&= 1\\
\int_{0}^{a} dx~ \sum\limits_{n=1}^{\infty} c_{n}^{*} \psi^{*}_{n}(x) \sum\limits_{m=1}^{\infty} c_{m} \psi_{m}(x)&= 1\\
\int_{0}^{a} dx~ \sum\limits_{n=1}^{\infty} c_{n}^{*}c_{m} \left(\psi^{*}_{n}(x) \sum\limits_{m=1}^\infty \psi_{m}(x)\right)&= 1\\
\int_{0}^{a} dx~ \sum\limits_{n=1}^{\infty} c_{n}^{*}c_{m} \delta_{nm} &= 1\\
\sum\limits_{n=1}^{\infty} dx~c_{n}^{*}c_{n}&= 1  \\
\sum\limits_{n=1}^{\infty} |c_{n}|^{2}&= 1
\end{align*}$$
em que temos que $|c_{n}|$ é a probabilidade de encontrar o sistema no estado $n$, $\mathcal{P}_{n}$.

**3.**
- Sendo $\Psi(x,t)=\sum\limits_{n=1}^{\infty} c_{n} \psi_{n} e^{^-i \frac{E_{n}}{\hbar} t}=\sqrt{\frac{2}{a}}\sum\limits_{n=1}^{\infty} c_{n} \sin\left(\frac{n\pi}{a}x\right) e^{-i\omega_{n}t}~~~~,~~~~ \omega_{n}= \frac{E_{n}}{\hbar}=\frac{n^{2}\pi^{2}\hbar}{2ma^{2}}$  
- Calculemos o valor médio do Hamiltoniano:
$$\begin{align*}
\langle H\rangle&= \int dx~ \Psi^{*}(x,t)\hat{H}\Psi(x,t)\\
&= \int dx~ \left(\sum\limits_{m=1}^{\infty} c_{m}^{*} \psi_{m}^{*} e^{i \frac{E_{m}}{\hbar}t}\right) \hat{H} \left(\sum\limits_{n=1}^{\infty} c_{n} \psi_{n} e^{i \frac{E_{n}}{\hbar} t}\right)\\
&= \sum\limits_{n,m=1}^{\infty} c_{m}^{*}c_{n} e^{-i\frac{E_{n}-E_{m}}{\hbar}t}\int dx~\psi_{m}^{*} \hat{H}\psi_{n}\\
&= \sum\limits_{n,m=1}^{\infty} c_{m}^{*}c_{n} e^{-i\frac{E_{n}-E_{m}}{\hbar}t}\int dx~\psi_{m}^{*} E_{n} \psi_{n}\\
&= \sum\limits_{n,m=1}^{\infty} c_{m}^{*}c_{n} e^{-i\frac{E_{n}-E_{m}}{\hbar}t} E_{n} \delta_{nm}\\
&= \sum\limits_{n=1}^{\infty} c_{n}^{*}c_{n} e^{0} E_{n}= \sum\limits_{n=1}^{\infty} |c_{n}|^{2}E_{n}=\sum\limits_{n=1}^{\infty} \mathcal{P}_{n}E_{n}=\langle E\rangle
\end{align*}$$

### Verificar Princípio de Incerteza de Heisenberg
- Considerando um estado simples / bem definido / sem combinações lineares, $\psi_{n}$. Sendo $\Psi(x,t)=\sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right) e^{-i \frac{E_{n}}{\hbar} t}~~~~,~~~~ E_{n}=\frac{n^{2}\pi^{2}\hbar^{2}}{2ma^{2}}$

*Posição média*
$$\begin{align*}
\langle x\rangle_{n} &= \int dx~\psi_{n}^{*} x \psi_{n}\\
&= \int_{0}^{a} dx~\sqrt{\frac{2}{a}}\left(\sin\left(\frac{n\pi}{a}x\right) e^{-i \frac{E_{n}}{\hbar} t}\right)^{*}x \sqrt{\frac{2}{a}} \left(\sin\left(\frac{n\pi}{a}x\right) e^{-i \frac{E_{n}}{\hbar} t}\right)\\
&= \frac{2}{a}\int_{0}^{a} dx~ \left(\sin\left(\frac{n\pi}{a}x\right) \cancel{e^{i \frac{E_{n}}{\hbar} t}}\right)x\left(\sin\left(\frac{n\pi}{a}x\right) \cancel{e^{-i \frac{E_{n}}{\hbar} t}}\right)\\
&= \frac{2}{a} \int_{0}^{a} dx~x\sin^{2}\left(\frac{n\pi}{a}x\right)=\frac{2}{a} \cdot \frac{a^{2}}{4}=\frac{a}{2}
\end{align*}$$
em que o integral dar $a^{2}/4$ é um resultado que conhecemos de Física Moderna

*Posição Quadrática Média*
$$\begin{align*}
\langle x^{2}\rangle_{n} &= \int dx~\psi_{n}^{*} x^{2} \psi_{n}\\
&= \int_{0}^{a} dx~\sqrt{\frac{2}{a}}\left(\sin\left(\frac{n\pi}{a}x\right) e^{-i \frac{E_{n}}{\hbar} t}\right)^{*}x ^{2}\sqrt{\frac{2}{a}} \left(\sin\left(\frac{n\pi}{a}x\right) e^{-i \frac{E_{n}}{\hbar} t}\right)\\
&= \frac{2}{a}\int_{0}^{a} dx~ \left(\sin\left(\frac{n\pi}{a}x\right) \cancel{e^{i \frac{E_{n}}{\hbar} t}}\right)x^{2}\left(\sin\left(\frac{n\pi}{a}x\right) \cancel{e^{-i \frac{E_{n}}{\hbar} t}}\right)\\
&= \frac{2}{a} \int_{0}^{a} dx~x^{2}\sin^{2}\left(\frac{n\pi}{a}x\right)=a^{2}\left(\frac{1}{3}- \frac{1}{2(n\pi)^{2}}\right)
\end{align*}$$
(porque matemática)

*Momento Médio*
$$\begin{align*}
\langle p\rangle_{n}&= \int dx~\psi_{n}^{*} \hat{P} \psi_{n}\\
&= \int_{0}^{a} dx~\sqrt{\frac{2}{a}}\left(\sin\left(\frac{n\pi}{a}x\right) e^{-i \frac{E_{n}}{\hbar} t}\right)^{*} \frac{\hbar}{i} \frac{\partial}{\partial x} \sqrt{\frac{2}{a}} \left(\sin\left(\frac{n\pi}{a}x\right) e^{-i \frac{E_{n}}{\hbar} t}\right)\\
&= \frac{2}{a}\int_{0}^{a} dx~ \left(\sin\left(\frac{n\pi}{a}x\right) \cancel{e^{i \frac{E_{n}}{\hbar} t}}\right) \frac{\hbar}{i} \frac{\partial}{\partial x} \left(\sin\left(\frac{n\pi}{a}x\right) \cancel{e^{-i \frac{E_{n}}{\hbar} t}}\right)\\
&= \frac{2}{a}\int_{0}^{a} dx~ \frac{n\pi}{a} \frac{\hbar}{i}~\sin\left(\frac{n\pi}{a}x\right)\cos\left(\frac{n\pi}{a}x\right)=0
\end{align*}$$
(confia no integral-calculator.com)

*Momento Quadrático Médio*
$$\begin{align*}
\langle p^{2}\rangle_{n}&= \int dx~\psi_{n}^{*} (\hat{P})^{2} \psi_{n}\\
&= \int_{0}^{a} dx~\sqrt{\frac{2}{a}}\left(\sin\left(\frac{n\pi}{a}x\right) e^{-i \frac{E_{n}}{\hbar} t}\right)^{*} \left(-\hbar^{2} \frac{\partial^{2}}{\partial x^{2}}\right) \sqrt{\frac{2}{a}} \left(\sin\left(\frac{n\pi}{a}x\right) e^{-i \frac{E_{n}}{\hbar} t}\right)\\
&= \frac{2}{a}\int_{0}^{a} dx~ \left(\sin\left(\frac{n\pi}{a}x\right) \cancel{e^{i \frac{E_{n}}{\hbar} t}}\right) \left(-\hbar^{2} \frac{\partial^{2}}{\partial x^{2}}\right) \left(\sin\left(\frac{n\pi}{a}x\right) \cancel{e^{-i \frac{E_{n}}{\hbar} t}}\right)\\
&= \frac{2}{a}\int_{0}^{a} dx~ (-\hbar^{2})\frac{n\pi}{a} \left(-\frac{n\pi}{a}\right)~\sin\left(\frac{n\pi}{a}x\right)\sin\left(\frac{n\pi}{a}x\right)=0\\
&= \frac{2}{a} \frac{n^{2}\pi ^{2}\hbar^{2}}{a^{2}}\int_{0}^{a}dx~ \sin^{2}\left(\frac{n\pi}{a}x\right)=\frac{2}{a} \frac{n^{2}\pi ^{2}\hbar^{2}}{a^{2}} \frac{a}{2}= \left(\frac{n\pi\hbar}{a}\right)^{2}
\end{align*}$$
(confia que o integral é igual a $\frac{a}{2}$)
- De notar aqui que: $-\hbar^{2} \frac{\partial^{2}}{\partial x^{2}} = -\hbar^{2} \Delta = 2m \hat{H}$. Assim temos: 
$$\begin{align*}
\langle p^{2}\rangle_{n}&= \int dx~\psi_{n}^{*} (\hat{P})^{2} \psi_{n}\\
&= \int_{0}^{a} dx~ \left(\psi_{n}^{*}(x) \cancel{e^{i \frac{E_{n}}{\hbar} t}}\right) \left(-\hbar^{2} \frac{\partial^{2}}{\partial x^{2}}\right) \left(\psi_{n}(x) \cancel{e^{-i \frac{E_{n}}{\hbar} t}}\right)\\
&= 2m \int dx~ \psi_{n}^{*} \hat{H} \psi_n\\
&= 2m \langle E\rangle= 2m \frac{n^{2}\pi^{2}\hbar^{2}}{2ma^{2}}=\frac{n^{2}\pi^{2}\hbar^{2}}{a^{2}}
\end{align*}$$
obtendo-se o mesmo que temos acima e verificando-se a relação $\langle E\rangle = \frac{\langle p^{2}\rangle}{2m}$

*Variâncias da Posição e Momento*
- Para a posição:
$$\Delta x= \sqrt{\langle x^{2}\rangle-\langle x\rangle^{2}}=\sqrt{a^{2}\left(\frac{1}{3}- \frac{1}{2(n\pi)^{2}}\right) - \left(\frac{a}{2}\right)^{2}}=a\sqrt{\frac{1}{12}- \frac{1}{2(n\pi)^{2}}}$$
- Para o momento:
$$\Delta p= \sqrt{\langle p^{2}\rangle- \langle p\rangle^{2}}=\sqrt{\langle p^{2}\rangle}= \frac{n\pi\hbar}{a}$$

**_Relação de Heisenberg_**
- Façamos o produto das variâncias:
$$\Delta x \Delta p= a\sqrt{\frac{1}{12}- \frac{1}{2(n\pi)^{2}}}\frac{n\pi\hbar}{a}= \sqrt{ \frac{n^{2}\pi^{2}\hbar^{2}}{12}- \frac{\hbar^{2}}{2} }=\hbar \sqrt{\frac{n^{2}\pi^{2}}{12}- \frac{1}{2}}\ge \frac{\hbar}{2}$$
verificamos então o princípio de incerteza de Heisenberg.
- De notar que se $n=1$ (estado fundamental) temos $\Delta x \Delta p\simeq 0.57\hbar$. Para todos os $n>1$ o termo dentro da raiz será maior, de forma que esta relação será sempre verdade.

## Combinação Linear de 2 estados ortogonais 
- Consideremos a função de onda $$\Psi(x,t)=\frac{1}{\sqrt{2}}(\Psi_{1}(x,t)+ \Psi_{2}(x,t))$$
- Em que podemos escrever: $\Psi_{n}=\psi_{n}(x)e^{-i\omega_{n}t}$. Além disso, consideremos: $\omega=\omega_{1}$. Assim temos: $\omega_{n}=n^{2}\omega_{1}=n^{2}\omega$. Isto tudo resulta em:
$$\Psi(x,t)=\frac{1}{\sqrt{2}} \left(\psi_{1}(x)e^{-i\omega t} + \psi_{2}(x)e^{-i4\omega t}\right)$$
e em que, novamente, temos: $\psi_{n}=\sqrt{\frac{2}{a}}\sin\left(\frac{n\pi}{a}x\right)$ e temos:
$$\Psi(x,t)=\frac{1}{\sqrt{a}} \left( \sin\left(\frac{\pi x}{a}\right)e^{-i\omega t} + \sin\left(\frac{2\pi x}{a}\right)e^{-i4\omega t}\right)$$

**Densidade de Probabilidade**
- Temos que $|A+B|^{2}=(A^{*}+B^{*})(A+B)=|A^{2}|+|B|^{2}+A^{*}B + B^{*}A$. Assim:
$$\begin{align*}
|\Psi(x,t)|^{2}&= \frac{1}{a} \left[ \sin^{2}\left(\frac{\pi x}{a}\right)+\sin^{2}\left(\frac{2\pi x}{a}\right)+\sin\left(\frac{\pi x}{a}\right)\sin\left(\frac{2\pi x}{a}\right)(e^{i3\omega t}+e^{-i3\omega t}) \right]\\
&= \frac{1}{a} \left[ \sin^{2}\left(\frac{\pi x}{a}\right)+\sin^{2}\left(\frac{2\pi x}{a}\right)+\sin\left(\frac{\pi x}{a}\right)\sin\left(\frac{2\pi x}{a}\right)\cdot2\cos(3\omega t) \right]
\end{align*}$$
ou seja, a densidade de probabilidade **varia com o tempo** (algo que tinhamos dito atrás que ia acontecer. Porque os termos exponenciais não cortam ao multiplicar $\Psi^{*}\Psi$)

**Posição média**
- Analogamente, se calcularmos a posição média temos:
$$\begin{align*}
\langle x\rangle&= \frac{1}{2}\int dx~\Psi^{*}(x,t)x\Psi(x,t)\\
&= \frac{1}{2}\int dx~ (\psi_{1}^{*}(x)e^{i\omega t}+\psi_{2}^{*}(x)e^{i4\omega t})x(\psi_{1}(x)e^{-i\omega t}+\psi_{2}(x)e^{-i4\omega t})\\
&= (\dots\textsf{matemática}\dots)\\
&= a\left(\frac{1}{2}-\frac{16}{9\pi^{2}}\cos(3\omega t)\right)
\end{align*}$$
ou seja, esta observável tambem passa a depender do tempo.