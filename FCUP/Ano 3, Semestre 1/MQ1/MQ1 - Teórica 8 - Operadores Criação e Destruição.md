 # 2.5 - Oscilador Harmónico Quântico
- Isto é útil, não apenas quando temos um oscilador harmónico literal, mas também quando temos uma partícula a oscilar em torno de uma posição de equilíbrio (OHS costuma ser uma boa aproximação).
- O potencial harmónico 1-D é igual a $$V=\frac12 m \omega^{2} x^{2}$$
- Ao substituir na ESIT temos:
$$\left(\frac{-\hbar^{2}}{2m} \frac{d^{2}}{dx^{2}} + \frac12m\omega^{2}x^{2}\right)\psi=E \psi$$

### Método Algébrico
- Temos que $H$ não passa da soma de 2 quadrados, definimos os 2 operadores abaixo:
$$a_{\pm}=\sqrt{\frac{m\omega}{2\hbar}} (\hat{X}\mp \frac{i}{m\omega} \hat{P})=\sqrt{\frac{m\omega}{2\hbar}} \left(\hat{X}\mp \frac{\hbar}{m\omega} \frac{d}{dx}\right)$$
- Vejamos o que obtemos se aplicarmos os operadores:
$$\begin{align*}
a_{-}a_{+}f(x)&= \frac{m\omega}{2\hbar} \left[x+\frac{\hbar}{m\omega} \frac{d}{dx} \left(x- \frac{\hbar}{m\omega} \frac{d}{dx}\right)f(x)\right]\\
&= \frac{m\omega}{2\hbar} \left[x+\frac{\hbar}{m\omega} \frac{d}{dx} \left(xf- \frac{\hbar}{m\omega} f'\right)\right]\\
&= \frac{m\omega}{2\hbar} \left[x \left(xf- \frac{\hbar}{m\omega} f'\right) +\frac{\hbar}{m\omega} \left( xf- \frac{\hbar}{m\omega} f'\right)'~\right]\\
&= \frac{m\omega}{2\hbar} \left[ x^{2}f - \frac{x\hbar}{m\omega}f' + \frac{\hbar}{m\omega}\left( f + xf' -\frac{\hbar}{m\omega}f'' \right)  \right]\\
&= \frac{m\omega}{2\hbar} \left[ x^{2}f - \cancel{\frac{x\hbar}{m\omega}f'} + \frac{\hbar}{m\omega}f + \cancel{\frac{x\hbar}{m\omega}f'} -\frac{\hbar^{2}}{m^{2}\omega^{2}}f''  \right]\\
&= \frac{-\hbar}{2m\omega}f'' +\left(\frac{m\omega}{2\hbar}x^{2} + \frac{1}{2}\right)f\\
&= \frac{1}{\omega\hbar}\left[\frac{-\hbar^{2}}{2m} \frac{d^{2}}{dx^{2}}f + \frac12m\omega^{2}x^{2}f+ \frac{\omega\hbar}{2}f \right]\\
&= \frac{1}{\hbar\omega} \left(\hat{H} + \frac{\hbar\omega}{2}\right)f(x)
\end{align*}$$

- Mas podemos fazer o oposto:
$$\begin{align*}
a_{+}a_{-}f(x)&= \frac{m\omega}{2\hbar} \left[x-\frac{\hbar}{m\omega} \frac{d}{dx} \left(x+ \frac{\hbar}{m\omega} \frac{d}{dx}\right)f(x)\right]\\
&= \frac{m\omega}{2\hbar} \left[x-\frac{\hbar}{m\omega} \frac{d}{dx} \left(xf+ \frac{\hbar}{m\omega} f'\right)\right]\\
&= \frac{m\omega}{2\hbar} \left[x \left(xf+ \frac{\hbar}{m\omega} f'\right) -\frac{\hbar}{m\omega} \left( xf+ \frac{\hbar}{m\omega} f'\right)'~\right]\\
&= \frac{m\omega}{2\hbar} \left[ x^{2}f + \frac{x\hbar}{m\omega}f' - \frac{\hbar}{m\omega}\left( f +xf' +\frac{\hbar}{m\omega}f'' \right)  \right]\\
&= \frac{m\omega}{2\hbar} \left[ x^{2}f + \cancel{\frac{x\hbar}{m\omega}f'} - \frac{\hbar}{m\omega}f - \cancel{\frac{x\hbar}{m\omega}f'} -\frac{\hbar^{2}}{m^{2}\omega^{2}}f''  \right]\\
&= \frac{-\hbar}{2m\omega}f'' +\left(\frac{m\omega}{2\hbar}x^{2} - \frac{1}{2}\right)f\\
&= \frac{1}{\omega\hbar}\left[\frac{-\hbar^{2}}{2m} \frac{d^{2}}{dx^{2}}f + \frac12m\omega^{2}x^{2}f- \frac{\omega\hbar}{2}f \right]\\
&= \frac{1}{\hbar\omega} \left(\hat{H} - \frac{\hbar\omega}{2}\right)f(x)
\end{align*}$$q

- Conseguimos ainda determinar o comutador dos operadores, tendo:
$$\begin{align*}
[a_{-},a_{+}]&= a_{-}a_{+}-a_{+}a_{-}\\
&= \frac{1}{\hbar\omega} \left(\hat{H} + \frac{\hbar\omega}{2}\right) - \frac{1}{\hbar\omega} \left(\hat{H} - \frac{\hbar\omega}{2}\right)\\
&= \frac{1}{\hbar\omega}\left(\cancel{\hat{H}} + \frac{\hbar\omega}{2} - \cancel{\hat{H}} + \frac{\hbar\omega}{2}\right)=1
\end{align*}$$
de notar que se tivessemos $[a_{-},a_{+}]=0$ então diria-se que os operadores comutavam.
- Usando estes operadores e estas propriedades veremos mais à frente como resolver casos sem sequer usar a ESIT.

- Conforme o que se tem atrás podemos escrever: 
$$a_{+}a_{-}=\frac{1}{\hbar\omega} \left(\hat{H} - \frac{\hbar\omega}{2}\right)=\frac{\hat{H}}{\hbar \omega} - \frac{1}{2}\to \hat{H}= \hbar \omega \left(a_{+}a_{-}+\frac{1}{2}\right)$$
e podemos reescrever a ESIT:
$$\hbar\omega\left(a_{+}a_{-}+\frac{1}{2}\right)\psi=E \psi$$

#### Teorema
- Vamos então supor que temos uma função de onda $\psi$ e respetiva energia $E$, que são soluções da ESIT.
- Neste caso, $a_{+}\psi$ será também solução, estando associada a uma energia $E+\hbar \omega$
- Por outro lado, $a_{-}\psi$ também é solução, com energia $E-\hbar\omega$

- Daqui surgem os nomes: $a_{+}$ é o **operador criação** (aumenta energia) e $a_{-}$ é **operador destruição/aniquilação** (diminui energia).

**Demonstração**
- Demonstremos que $a_{+}\psi$ é solução, com energia $E+\hbar \omega$:
$$\begin{align*}
\hat{H}(a_{+}\psi)&= \hbar \omega\left(a_{+}a_{-}+ \frac{1}{2}\right) (a_{+}\psi)\\
&= \hbar \omega \left( a_{+}a_{-}a_{+} + \frac{1}{2}a_{+} \right)\psi\\
&= \hbar \omega a_{+}\left(a_{-}a_{+}+ \frac{1}{2}  \right)\psi\\
&= \hbar\omega a_{+} \left( a_{+}a_{-}+1+ \frac{1}{2}\right)\psi \quad \quad \quad [a_{+},a_{-}]=1 \to a_{-}a_{+}=a_{+}a_{-}+1\\
&= a_{+} \left[\underbrace{\hbar\omega\left(a_{+}a_{-}+ \frac{1}{2}\right)}_\hat{H}  + \hbar\omega \right]\psi\\
&= a_{+}(E\psi+\hbar\omega\psi)\\
\hat{H}(a_{+}\psi)&= (E+\hbar\omega)(a_{+}\psi)
\end{align*}$$

- Ou seja, temos isto:
![[operadores criacao e destruicao.png]]

- No entanto, isto levaria a crer que se formos aplicando $a_{-}$ a $E$ iremos eventualmente obter energia muito baixa, até mesmo negativa!
- Ora, isto não pode ser o caso, porque não haveria um nível fundamental de energia.

### Estado Fundamental
- Assim, eventualmente chegaremos a uma função de onda $\psi_{0}$ que já não será solução. Ou seja:
$$\begin{align*}
a_{-}\psi_{0}&= 0\\
\left(x+ \frac{\hbar}{m\omega} \frac{d}{dx}\right)\psi_{0}&= 0\\
\frac{d}{dx}\psi_{0}&= \frac{-m\omega}{\hbar}x \psi_{0} \longrightarrow \psi_{0}(x)=A e^{- \frac{m \omega}{2\hbar}x^{2}}
\end{align*}$$
- Verifiquemos o que é que esta solução dá na ESIT:
$$\begin{align*}\\
\hat{H}\psi_{0}&= E \psi_{0}\\
\hbar\omega\left(a_{+}a_{-}+ \frac{1}{2}\right)\psi_{0}&= E \psi_{0}\\
\hbar \omega (a_{+} \cancelto{=0}{a_{-}\psi_{0}}+ \frac{1}{2}\psi_{0})&= E \psi_{0}\\
\frac{\hbar\omega}{2}\psi_{0}&= E \psi_{0} \longrightarrow E = \frac{\hbar\omega}{2}
\end{align*}$$
que é, de facto, a energia fundamental do Oscilador Harmónico quântico

- Vejamos qual será a amplitude da função / verificar condição de normalização:
$$\begin{align*}
1&= \int dx |\psi_{0}|^{2}\\
&= \int dx |A|^{2} e^{-\frac{m\omega}{2\hbar}x^{2}}\\
&= |A|^{2}\sqrt{\frac{\pi\hbar}{m\omega}} ~~ \longrightarrow~~ A&= \sqrt[4]{\frac{m\omega}{\pi\hbar}}
\end{align*}$$
sendo que a raiz solução do integral veio de $e^{-\frac{m\omega}{2\hbar}x^{2}}$ ser um integral gaussiano.

### Estados Excitados
- Podemos obtê-los ao aplicar $a_{+}$ sucessivamente a $\psi_{0}$. Ou seja:
$$\psi_{n}=A_{n} (a_{+})^{n} e^{-\frac{m\omega}{2\hbar}x^{2}} \quad \quad;\quad \quad E_{n}=\left(n+\frac12\right)\hbar\omega$$
- Vejamos a proporcionalidade de $\psi_{1}$:
$$\begin{align*}
\psi_{1} &\propto \left(x- \frac{\hbar}{m\omega} \frac{d}{dx}\right)e^{-\frac{m\omega}{2\hbar}x^{2}}\\
&\propto \left( x - \frac{\bcancel{\hbar}}{\cancel{m\omega}} \left( -\frac{\cancel{m\omega}}{\xcancel{2}\bcancel{\hbar}} \xcancel{2} x \right) \right)e^{-\frac{m\omega}{2\hbar}x^{2}}\\
&\propto xe^{-\frac{m\omega}{2\hbar}x^{2}}
\end{align*}$$
- Se fizermos isto para $\psi_{2},\psi_{3}$ veremos o formato dos traçados dos modos normais:
![[primeiros niveis oscilador harmonico.png]]

## Melhorar equação de $\psi_{n}$
- Para já temos
$$\psi_{n}=A_{n} (a_{+})^{n} e^{-\frac{m\omega}{2\hbar}x^{2}}$$
mas conseguimos melhorar.

- Vamos assumir que $\psi_{n}$ estão normalizadas.
- Temos ainda que $a_{+}\psi_{n}\propto \psi_{n+1}$. Vejamos então como podemos garantir que $a_{+}\psi_{n}$ está normalizado:
$$\begin{align*}
\int dx |a_{+}\psi_{n}|^{2}&= \int dx (a_{+}\psi_{n})^{*}(a_{+}\psi_{n})\\
&= \int dx~ a_{+}^{*}\psi^{*} a_{+}\psi_{n}\\
&= \frac{m\omega}{2\hbar} \int dx~\left[ \left( x- \frac{1}{m\omega} \frac{d}{dx} \right) \psi_{n}^{*} \right]\left[ \left( x- \frac{1}{m\omega} \frac{d}{dx} \right) \psi_{n} \right]\\
\end{align*}$$
- De alguma forma que não entendi, ao fazer integração por partes, a equação transforma-se nisto:
$$\begin{align*}
\int dx|a_{+}\psi_{n}|^{2}&= \frac{m\omega}{2\hbar} \int dx~\psi_{n}^{*}\left( x+ \frac{1}{m\omega} \frac{d}{dx} \right)\left( x- \frac{1}{m\omega} \frac{d}{dx} \right) \psi_{n}\\
&= \frac{m\omega}{2\hbar} \int dx~ \psi_{n}^{*}a_{-}a_{+}\psi_{n}\\
&= \frac{m\omega}{2\hbar} \int dx~ \psi_{n}^{*}(a_{+}a_{-}+1)\psi_{n}\\
&= \frac{m\omega}{2\hbar} \int dx~ (n+1)\psi_{n}^{*}\psi_{n}\tag{*}\\
&= \frac{m\omega}{2\hbar}(n+1)
\end{align*}$$

> **Dedução do passo (`*`)**
> - Temos que $$a_{+}a_{-}\psi_{n}=a_{+}a_{-} (A_{n}(a_{+})^{n}\psi_{0})=a_{+}a_{-}(a_{+})^{n} A_{n}\psi_{0}$$
> - Ora, vamos expandir: $$\begin{align*}
a_{+}a_{-}(a_{+})^{n}&= a_{+}a_{-}a_{+}(a_{+})^{n-1}\\
&= a_{+}\underbrace{(a_{+}a_{-}+1)}_\textsf{Comutativo de $a_-a_+$}(a_{+})^{n-1}\\
&= (a_{n})^{n} + (a_{+})^{2}a_{-}(a_{+})^{n-1}\\º
&= (\dots)\\
&= n(a_{+})^{n}+(a_{+})^{n}a_{-}
\end{align*}$$
> - Voltando a substituir em cima: $$\begin{align*}
a_{+}a_{-}\psi_{n}&= a_{+}a_{-}(a_{+})^{n}A_{n}\psi_{0}\\
&= (n(a_{+})^{n}+(a_{+})^{n}a_{-})A_{n}\psi_{0}\\
&= n (a_{+})^{n}(A_{n}\psi_{0}) + (a_{+})^{n} \cancelto{=0}{a_{-}\psi_{0}} A_{n}\\
&= n \psi_{n}
\end{align*}$$

- Isto dá-nos que $$a_{+}\psi_{n}= \sqrt{n+1}\psi_{n+1} \quad \quad \quad \text{Exemplos}: \begin{cases} n=0 & \to & a_{+}\psi_{0}=\psi_{1}  & \to &  \psi_{1}=\frac{1}{\sqrt{1}}a_{+}\psi_{0}\\ n=1 & \to & a_{+}\psi_{1}=\sqrt{2}\psi_{2}& \to &  \psi_{2}=\frac{1}{\sqrt{2}}a_{+}\psi_{1}\\ n=2 & \to & a_{+}\psi_{2}=\sqrt{3}\psi_{3} & \to &  \psi_{1}=\frac{1}{\sqrt{3}}a_{+}\psi_{2}\end{cases}$$
sendo que conseguimos escrever:
$$\psi_{3}= \frac{1}{\sqrt{3}}a_{+}\psi_{2} = \frac{1}{\sqrt{3}}a_{+}\left(\frac{1}{\sqrt{2}}a_{+}\psi_{1}\right)= \frac{1}{\sqrt{3}}a_{+}\left(\frac{1}{\sqrt{2}}a_{+}\left(\frac{1}{\sqrt{1}}a_{+}\psi_{0}\right)\right)\longrightarrow \psi_{3}=\frac{1}{\sqrt{3}\sqrt{2}\sqrt{1}}(a_{+})^{3}\psi_{0} \longrightarrow (a_{+})^{3}\psi_{0}=\sqrt{3!}~\psi_{3} $$

- Ou seja, consoante fazemos isto $n$ vezes seguidas ficamos com $\sqrt{n}\sqrt{n-1}\sqrt{n-2}\cdots\sqrt{2}\sqrt{1}\psi_{n}$:
$$\int dx |(a_{+})^{n}\psi_{n}|= n!$$
- Pegando na equação $\psi_{3}=\frac{1}{\sqrt{3}\sqrt{2}\sqrt{1}}(a_{+})^{3}\psi_{0}$ acima podemos generalizar e temos:
$$\psi_{n}(x)= \frac{1}{\sqrt{n!}}(a_{+})^{n} \psi_{0}(x)= \sqrt[4]{\frac{m\omega}{\hbar\omega}} \frac{(a_{+})^{n}}{\sqrt{n!}} e^{-\frac{m\omega}{2\hbar}x^{2}}$$

### Adimensionalizar
- Recordemos que $$a_{+}= \sqrt{\frac{m\omega}{2\hbar}} \left(x- \frac{1}{m\omega} \frac{d}{dx} \right)$$
- Ora, vamos criar uma nova variável que nos permite adimensionalizar o problema: $$\xi=\sqrt{\frac{m\omega}{\hbar}}x \quad \quad;\quad \quad d\xi=dx$$
- O operador criação fica:
$$a_{+}=\frac{1}{\sqrt{2}} \left( \xi - \frac{d}{d\xi} \right)$$
e a equação de $\psi_{n}$ fica:
$$\psi_{n}(\xi)=\sqrt[4]{\frac{m\omega}{\pi\hbar}} \frac{1}{\sqrt{2^{n}n!}} \left( \xi -  \frac{d}{d\xi} \right)^{n} e^{-\frac{\xi^{2}}{2}}$$
em que temos os **polinómios de Hermite**:
$$\left( \xi -  \frac{d}{d\xi} \right)^{n} e^{-\frac{\xi^{2}}{2}}=H_{n}(\xi) e^{-\frac{\xi^{2}}{2}}$$
