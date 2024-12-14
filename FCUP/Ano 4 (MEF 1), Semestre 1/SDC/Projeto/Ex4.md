## 4 v prof
### Equações da aula
$$M=\exp\left(-\frac{\pi\xi}{\sqrt{1-\xi^{2}}}\right)~~~~;~~~~ t_{s(2\%)}=\frac{4}{\xi\omega_{n}}~~,~~ t_{s(5\%)}=\frac{3}{\xi\omega_{n}}$$
logo
$$\xi=\sqrt{\frac{\ln (\frac{1}{0.05})^{2}}{\pi^{2}+\ln (\frac{1}{0.05})^{2}}}\quad;\quad \omega_{n}=\frac{2}{\xi}$$

## 4 v1
- Do livro, temos:
$$s^{2}+2\xi \omega_{n}+\omega_{n}^{2}=0$$
que está associado a uma percentagem de overshoot:
$$PO=100 e^{- \xi\pi/\sqrt{1-\xi^{2}}}$$
- Ora, o nosso sistema recebe um impulso com valor $\tau_{0}=\cdot10^{-1}$ em $t=0$. Depois disso o sistema irá equilibrar-se, voltando a $\theta=0$. Nisto, ele irá fazer overshoot, passando por valores negativos e oscilando antes de chegar a zero.
- Assim, queremos que o nosso overshoot máximo seja $5\cdot10^{-2}$, logo temos:
$$O= e^{- \xi\pi/\sqrt{1-\xi^{2}}}$$
e 
$$O_{max}=0.05$$
Assim:
$$\begin{align*}
e^{- \xi\pi/\sqrt{1-\xi^{2}}}&= 0.05\\
\frac{\xi\pi}{\sqrt{1-\xi^{2}}}&= -\ln 0.05\\
\xi \pi&= \ln20\sqrt{1-\xi^{2}}\\
\xi^{2}\pi^{2}&= (\ln20)^{2}(1-\xi^{2})\\
\xi^{2}(\pi^{2}+\ln20)^{2})&= (\ln20)^{2}\\
\xi&= \sqrt{\frac{(\ln20)^{2}}{\pi^{2}+(\ln20)^{2}}}
\end{align*}$$
- Queremos ainda que o sistema estabilize em 2 segundos. Assim temos:
$$t_{s}=2=\frac{4}{\xi\omega_{n}}$$
assim:
$$\omega_{n}=\frac{2}{\xi}= 2 \sqrt{\frac{\pi^{2}+(\ln20)^{2}}{(\ln20)^{2}}}$$

## 4 - V2
- Temos:
$$sI=\begin{pmatrix}s & 0 \\ 0 & s\end{pmatrix}\quad;\quad A=\begin{pmatrix}0 & 1 \\ \frac{mgh}{I} & 0\end{pmatrix}\quad;\quad BK=\begin{pmatrix}0 & 0 \\ \frac{k_{1}}{I} & \frac{k_{2}}{I}\end{pmatrix}$$
E assim:
$$sI-A+BK = \begin{pmatrix}s & -1 \\ \frac{k_{1}-mgh}{I} & s + \frac{k_{2}}{I}\end{pmatrix}$$
- Ao calcular o deteminante disto obtemos:
$$\det(sI-A+BK)=s^{2} +\frac{k_{2}}{I}s + {\frac{k_{1}-mgh}{I}}$$
- Ora, conforme o livro que seguimos, temos que o polinómio caraterístico de um sistema LTI com feedback pode escrito na forma:
$$p(s)=s^{2}+2\xi\omega_{n}s+\omega_{n}^{2}$$
- Como polinómios são equivalentes, temos:
$$\begin{align*}
k_{1}&= I\omega_{n}^{2} + mgh\\
k_{2}&= 2\xi\omega_{n}I
\end{align*}$$

**Função transferência**
- Os zeros de $p(s)$ são:
$$\lambda_{1}=-\xi\omega_{n} + j\omega_{n}\sqrt{1-\xi^{2}} \quad;\quad \lambda_{2}=-\xi\omega_{n} - j\omega_{n}\sqrt{1-\xi^{2}}$$
e podemos escrever a função transferência do sistema:
$$\frac{Y}{U}= \frac{1}{(s-\lambda_{1})(s-\lambda_{2})}=\frac{A}{s-\lambda_{1}}+ \frac{B}{s-\lambda_{2}}$$
- Podemos determinar os coeficientes: $A=\frac{1}{\lambda_{2}-\lambda_{1}}~,~B=\frac{1}{\lambda_{1}-\lambda_{2}}=-A$. Logo:
$$\frac{Y}{U}=\frac{1}{\lambda_{2}-\lambda_{1}} \left(\frac{1}{s-\lambda_{1}} - \frac{1}{s-\lambda_{2}}\right)$$
em que temos $\lambda_{2}-\lambda_{1}=-2j\omega_{n}\sqrt{1-\xi^{2}}$.

**Evolução temporal**
- A partir disto podemos obter:
$$\begin{align*}
y(t)&= y_{0} \cdot \frac{1}{2j\omega_{n}\sqrt{1-\xi^{2}}} (e^{\lambda_{1}t} - e^{\lambda_{2}t})\\
&= \frac{y_{0}}{2j\omega_{n}\sqrt{1-\xi^{2}}} \left(e^{t(-\xi\omega_{n}+j\omega_{n}\sqrt{1-\xi^{2}})} - e^{t(-\xi\omega_{n}-j\omega_{n}\sqrt{1-\xi^{2}})} \right)\\
&= \frac{y_{0}}{2j\omega_{n}\sqrt{1-\xi^{2}}} e^{-\xi\omega_{n}t}\left(e^{j \omega_{n}\sqrt{1-\xi^{2}}t} - e^{-j \omega_{n}\sqrt{1-\xi^{2}}t} \right)\\
&= \frac{y_{0}}{\omega_{n}\sqrt{1-\xi^{2}}} e^{-\xi\omega_{n}t}\sin (\omega_{n}\sqrt{1-\xi^{2}}t)
\end{align*}$$
isto bate certo com o livro. Mas, para garantir que temos $y(t=0)=y_{0}$ podemos introduzir uma fase: $\frac{\pi}{2}$. Isto converte o seno em cosseno:
$$y(t)=\frac{y_{0}}{\omega_{n}\sqrt{1-\xi^{2}}} e^{-\xi\omega_{n}t}\cos (\omega_{n}\sqrt{1-\xi^{2}}t)$$

**Condições que queremos**
- Queremos 2 coisas: overshoot máximo de $0.05$ e queremos que o sistema esta estabilizado em $t=2$
- Começamos pelo tempo de settling:
$$\begin{align*}
y(t=2) &= 0\\
\frac{y_{0}}{\omega_{n}\sqrt{1-\xi^{2}}} e^{-2\xi\omega_{n}}\cos (2\omega_{n}\sqrt{1-\xi^{2}})&= 0\\
\cos (2\omega_{n}\sqrt{1-\xi^{2}})&= 0\\
2\omega_{n}\sqrt{1-\xi^{2}}&= \frac{\pi}{2}\\
\omega_{n}&= \frac{\pi}{4\sqrt{1-\xi^{2}}}
\end{align*}$$
- Tendo agora $\omega_{n}(\xi)$ podemos passar à segunda condição:
- O overshoot irá acontecer quando a função desce de $y_{0}$ para o primeiro mínimo, que será abaixo de zero. Assim, queremos que o mínimo seja superior a $-0.05$.
*Tempo do overshoot*
- A função consiste num cosseno neutralizado por uma exponencial. Assim, o primeiro mínimo irá acontecer quando:
$$\begin{align*}
\cos (\omega_{n}\sqrt{1-\xi^{2}}t)&= -1\\
\omega_{n}\sqrt{1-\xi^{2}}t&= \pi\\
t&= \frac{\pi}{\omega_{n}\sqrt{1-\xi^{2}}}
\end{align*}$$
- Assim, a condição do overshoot consiste em:
$$\begin{align*}
y\left(t=\frac{\pi}{\omega_{n}\sqrt{1-\xi^{2}}}\right)&= -0.05\\
\frac{y_{0}}{\omega_{n}\sqrt{1-\xi^{2}}} e^{-\pi\xi/\sqrt{1-\xi^{2}}}\cos (\pi)&=-0.05\\
20y_{0}&= \omega_{n}\sqrt{1-\xi^{2}} e^{\pi\xi/\sqrt{1-\xi^{2}}}\\
20y_{0}&= \frac{\pi}{4}e^{\pi\xi/\sqrt{1-\xi^{2}}}\\
\ln\left(\frac{80}{\pi}y_{0}\right)&= \pi \frac{\xi}{\sqrt{1-\xi^{2}}}\\
\ln\left(\frac{80}{\pi}y_{0}\right)^{2}(1-\xi^{2})&= \pi^{2}\xi^{2}\\
\xi&= \sqrt{\frac{\ln\left(\frac{80}{\pi}y_{0}\right)^{2}}{\pi^{2}+ \ln\left(\frac{80}{\pi}y_{0}\right)^{2}}}
\end{align*}$$

## 4 - v3
- Temos:
$$sI=\begin{pmatrix}s & 0 \\ 0 & s\end{pmatrix}\quad;\quad A=\begin{pmatrix}0 & 1 \\ \frac{mgh}{I} & 0\end{pmatrix}\quad;\quad BK=\begin{pmatrix}0 & 0 \\ \frac{k_{1}}{I} & \frac{k_{2}}{I}\end{pmatrix}$$
E assim:
$$sI-A+BK = \begin{pmatrix}s & -1 \\ \frac{k_{1}-mgh}{I} & s + \frac{k_{2}}{I}\end{pmatrix}$$
- Ao calcular o deteminante disto obtemos:
$$\det(sI-A+BK)=s^{2} +\frac{k_{2}}{I}s + {\frac{k_{1}-mgh}{I}}$$
- Ora, conforme o livro que seguimos, temos que o polinómio caraterístico de um sistema LTI com feedback pode escrito na forma:
$$p(s)=s^{2}+2\xi\omega_{n}s+\omega_{n}^{2}$$
- Como polinómios são equivalentes, temos:
$$\begin{align*}
k_{1}&= I\omega_{n}^{2} + mgh\\
k_{2}&= 2\xi\omega_{n}I
\end{align*}$$

**Função transferência**
- Os zeros de $p(s)$ são:
$$\lambda_{1}=-\xi\omega_{n} + j\omega_{n}\sqrt{1-\xi^{2}} \quad;\quad \lambda_{2}=-\xi\omega_{n} - j\omega_{n}\sqrt{1-\xi^{2}}$$
e podemos escrever a função transferência do sistema:
$$\frac{Y}{U}= \frac{1}{(s-\lambda_{1})(s-\lambda_{2})}=\frac{A}{s-\lambda_{1}}+ \frac{B}{s-\lambda_{2}}$$
- Podemos determinar os coeficientes: $A=\frac{1}{\lambda_{2}-\lambda_{1}}~,~B=\frac{1}{\lambda_{1}-\lambda_{2}}=-A$. Logo:
$$\frac{Y}{U}=\frac{1}{\lambda_{2}-\lambda_{1}} \left(\frac{1}{s-\lambda_{1}} - \frac{1}{s-\lambda_{2}}\right)$$
em que temos $\lambda_{2}-\lambda_{1}=-2j\omega_{n}\sqrt{1-\xi^{2}}$.

**Evolução temporal**
- A partir disto podemos obter:
$$\begin{align*}
y(t)&= y_{0} \cdot \frac{1}{2j\omega_{n}\sqrt{1-\xi^{2}}} (e^{\lambda_{1}t} - e^{\lambda_{2}t})\\
&= \frac{y_{0}}{2j\omega_{n}\sqrt{1-\xi^{2}}} \left(e^{t(-\xi\omega_{n}+j\omega_{n}\sqrt{1-\xi^{2}})} - e^{t(-\xi\omega_{n}-j\omega_{n}\sqrt{1-\xi^{2}})} \right)\\
&= \frac{y_{0}}{2j\omega_{n}\sqrt{1-\xi^{2}}} e^{-\xi\omega_{n}t}\left(e^{j \omega_{n}\sqrt{1-\xi^{2}}t} - e^{-j \omega_{n}\sqrt{1-\xi^{2}}t} \right)\\
&= \frac{y_{0}}{\omega_{n}\sqrt{1-\xi^{2}}} e^{-\xi\omega_{n}t}\sin (\omega_{n}\sqrt{1-\xi^{2}}t)
\end{align*}$$
isto bate certo com o livro. Mas, para garantir que temos $y(t=0)=y_{0}$ podemos introduzir uma fase igual a $\pi/2$, que converte num cosseno:
$$y(t)=\frac{y_{0}}{\omega_{n}\sqrt{1-\xi^{2}}} e^{-\xi\omega_{n}t}\cos (\omega_{n}\sqrt{1-\xi^{2}}t)$$
queremos que $y(0) = y_{0}$ logo:
$$\sin(\phi)=\omega_{n}\sqrt{1-\xi^{2}}~~\to~~ \phi=\sin^{-1}(\omega_{n}\sqrt{1-\xi^{2}})$$

**Condições desejadas**
- Queremos 2 coisas: overshoot máximo de $0.05$ e queremos que o sistema esta estabilizado em $t=2$
*Tempo de settle*
- Podemos garantir que em $t=2$ o sistema está settled forçando 2 coisas que podem funcionar:
    - derivada nula
    - amplitude da exponencial em $t=2$ abaixo de uma certa tolerância $T$ (isto porque o termo exponencial é que decide a amplitude)
- Temos a derivada:
$$\frac{dy}{dt}= \frac{y_{0}}{\omega_{n}\sqrt{1-\xi^{2}}} \left[-\xi\omega_{n}e^{-\xi\omega_{n}t}\cos (\omega_{n}\sqrt{1-\xi^{2}}t) - \omega_{n}\sqrt{1-\xi^{2}}e^{-\xi\omega_{n}t}\sin (\omega_{n}\sqrt{1-\xi^{2}}t)\right]$$
que queremos que seja nula em $t=2$:
$$\sqrt{1-\xi^{2}}\sin(2\omega_{n}\sqrt{1-\xi^{2}})= -\xi\cos(2\omega_{n}\sqrt{1-\xi^{2}})$$
ora, neste instante já teríamos ângulos muito baixos, próximos de 0. Assim podemos assumir $\sin\theta\sim\theta~,~\cos\theta\sim1$ e ficamos com:
$$2(1-\xi^{2})\omega_{n}=-\xi~~\to~~ \omega_{n}=- \frac{\xi}{2-2\xi^{2}}$$
- Temos a exponencial:
$$\begin{align*}
|e^{-\xi\omega_{n}\cdot2}|&\le T\\
2\xi\omega_{n}&\ge \ln \frac{1}{T}\\
\omega_{n}&\ge \frac{1}{2\xi}\ln \frac{1}{T} 
\end{align*}$$

*Overshoot*
- A função consiste num cosseno neutralizado por uma exponencial. Assim, o primeiro mínimo irá acontecer quando:
$$\begin{align*}
\cos (\omega_{n}\sqrt{1-\xi^{2}}t)&= -1\\
\omega_{n}\sqrt{1-\xi^{2}}t&= \pi\\
t&= \frac{\pi}{\omega_{n}\sqrt{1-\xi^{2}}}
\end{align*}$$

- Aqui a melhor forma que temos é limitar a exponencial:
$$\begin{align*}
e^{-\xi\omega_{n}t}&\le  0.05+T\\
\exp \left(-\xi \omega_{n} \frac{\pi}{\omega_{n}\sqrt{1-\xi^{2}}} \right)&\le 0.05+T\\
\frac{\xi\pi}{\sqrt{1-\xi^{2}}}&\ge \ln \frac{1}{0.05+T}\\
\xi^{2}\pi^{2} &\ge \left(\ln \frac{1}{0.05+T}\right)^{2}(1-\xi^{2}) \\
\xi^{2}\left(\pi^{2}+\left(\ln \frac{1}{0.05+T}\right)^{2}\right)&\ge \left(\ln \frac{1}{0.05+T}\right)^{2}\\
\xi&\ge \sqrt{\frac{\left(\ln \frac{1}{0.05+T}\right)^{2}}{\pi^{2}+\left(\ln \frac{1}{0.05+T}\right)^{2}}}
\end{align*}$$
Assim definimos uma tolerância $T$ e temos:
$$\xi=\sqrt{\frac{\left(\ln \frac{1}{0.05+T}\right)^{2}}{\pi^{2}+\left(\ln \frac{1}{0.05+T}\right)^{2}}} \quad;\quad \omega_{n}=\frac{1}{2\xi}\ln \frac{1}{T} $$
- FUNCIONA!
## 4 - v4 - FINAL
- Temos:
$$sI=\begin{pmatrix}s & 0 \\ 0 & s\end{pmatrix}\quad;\quad A=\begin{pmatrix}0 & 1 \\ \frac{mgh}{I} & 0\end{pmatrix}\quad;\quad BK=\begin{pmatrix}0 & 0 \\ \frac{k_{1}}{I} & \frac{k_{2}}{I}\end{pmatrix}$$
E assim:
$$sI-A+BK = \begin{pmatrix}s & -1 \\ \frac{k_{1}-mgh}{I} & s + \frac{k_{2}}{I}\end{pmatrix}$$
- Ao calcular o deteminante disto obtemos:
$$\det(sI-A+BK)=s^{2} +\frac{k_{2}}{I}s + {\frac{k_{1}-mgh}{I}}$$
- Ora, conforme o livro que seguimos, temos que o polinómio caraterístico de um sistema LTI com feedback pode escrito na forma:
$$p(s)=s^{2}+2\xi\omega_{n}s+\omega_{n}^{2}$$
- Como polinómios são equivalentes, temos:
$$\begin{align*}
k_{1}&= I\omega_{n}^{2} + mgh\\
k_{2}&= 2\xi\omega_{n}I
\end{align*}$$

**Função transferência**
- Os zeros de $p(s)$ são:
$$\lambda_{1}=-\xi\omega_{n} + j\omega_{n}\sqrt{1-\xi^{2}} \quad;\quad \lambda_{2}=-\xi\omega_{n} - j\omega_{n}\sqrt{1-\xi^{2}}$$
e podemos escrever a função transferência do sistema:
$$\frac{Y}{U}= \frac{1}{(s-\lambda_{1})(s-\lambda_{2})}=\frac{A}{s-\lambda_{1}}+ \frac{B}{s-\lambda_{2}}$$
- Podemos determinar os coeficientes: $A=\frac{1}{\lambda_{2}-\lambda_{1}}~,~B=\frac{1}{\lambda_{1}-\lambda_{2}}=-A$. Logo:
$$\frac{Y}{U}=\frac{1}{\lambda_{2}-\lambda_{1}} \left(\frac{1}{s-\lambda_{1}} - \frac{1}{s-\lambda_{2}}\right)$$
em que temos $\lambda_{2}-\lambda_{1}=-2j\omega_{n}\sqrt{1-\xi^{2}}$.

**Evolução temporal**
- A partir disto podemos obter:
$$\begin{align*}
y(t)&= y_{0} \cdot \frac{1}{2j\omega_{n}\sqrt{1-\xi^{2}}} (e^{\lambda_{1}t} - e^{\lambda_{2}t})\\
&= \frac{y_{0}}{2j\omega_{n}\sqrt{1-\xi^{2}}} \left(e^{t(-\xi\omega_{n}+j\omega_{n}\sqrt{1-\xi^{2}})} - e^{t(-\xi\omega_{n}-j\omega_{n}\sqrt{1-\xi^{2}})} \right)\\
&= \frac{y_{0}}{2j\omega_{n}\sqrt{1-\xi^{2}}} e^{-\xi\omega_{n}t}\left(e^{j \omega_{n}\sqrt{1-\xi^{2}}t} - e^{-j \omega_{n}\sqrt{1-\xi^{2}}t} \right)\\
&= \frac{y_{0}}{\omega_{n}\sqrt{1-\xi^{2}}} e^{-\xi\omega_{n}t}\sin (\omega_{n}\sqrt{1-\xi^{2}}t)
\end{align*}$$

**Condições desejadas**
- Queremos 2 coisas: overshoot máximo de $0.05$ e queremos que o sistema esta estabilizado em $t=2$
*Tempo de settle*
- Podemos garantir que em $t=2$ o sistema está settled forçando a da exponencial abaixo de uma certa tolerância $T$ (isto porque o termo exponencial é que decide a amplitude)
$$\begin{align*}
|e^{-\xi\omega_{n}\cdot2}|&\le T\\
2\xi\omega_{n}&\ge \ln \frac{1}{T}\\
\omega_{n}&\ge \frac{1}{2\xi}\ln \frac{1}{T} 
\end{align*}$$

*Overshoot*
- Começamos com o ângulo nulo. Depois do impulso de torque teremos velocidade angular não nula. Isto vai fazer o ângulo aumentar. O nosso sistema tem o objetivo de reduzir o ângulo de volta para zero, mas sem passar o nível de overshoot desejado, abaixo de zero.
- A função consiste numa sinusoide com amplitude controlada por uma exponencial. Assim, o primeiro mínimo irá acontecer quando:
$$\begin{align*}
\sin (\omega_{n}\sqrt{1-\xi^{2}}t)&= -1\\
\omega_{n}\sqrt{1-\xi^{2}}t&= \frac{3\pi}{2}\\
t&= \frac{3\pi}{2\omega_{n}\sqrt{1-\xi^{2}}}
\end{align*}$$

- Aqui a melhor forma que temos é limitar a exponencial:
$$\begin{align*}
e^{-\xi\omega_{n}t}&\le  0.05+T\\
\exp \left(-\xi \omega_{n} \frac{3\pi/2}{\omega_{n}\sqrt{1-\xi^{2}}} \right)&\le 0.05+T\\
\frac{\xi\cdot 3\pi/2}{\sqrt{1-\xi^{2}}}&\ge \ln \frac{1}{0.05+T}\\
\xi^{2}\left(\frac{3\pi}{2}\right)^{2} &\ge \left(\ln \frac{1}{0.05+T}\right)^{2}(1-\xi^{2}) \\
\xi^{2}\left(\left(\frac{3\pi}{2}\right)^{2}+\left(\ln \frac{1}{0.05+T}\right)^{2}\right)&\ge \left(\ln \frac{1}{0.05+T}\right)^{2}\\
\xi&\ge \sqrt{\frac{\left(\ln \frac{1}{0.05+T}\right)^{2}}{\left(\frac{3\pi}{2}\right)^{2}+\left(\ln \frac{1}{0.05+T}\right)^{2}}}
\end{align*}$$
Assim definimos uma tolerância $T$ e temos:
$$\xi=\sqrt{\frac{\left(\ln \frac{1}{0.05+T}\right)^{2}}{\left(\frac{3\pi}{2}\right)^{2}+\left(\ln \frac{1}{0.05+T}\right)^{2}}} \quad;\quad \omega_{n}=\frac{1}{2\xi}\ln \frac{1}{T} $$

*Notas*
- Como podemos ver no gráfico abaixo, a função analítica que usamos nestas deduções não coincide completamente com o comportamento do sistema de feedback. Mas o sistema comporta-se dentro dos objetivos

- Ao variar a tolerância vemos que o overshoot e o tempo de settling tornam-se cada vez menores

- De acordo com as equações acima, podemos multiplicar o valor de $\omega_n$ por qualquer constante >1 e o sistema funciona bem, estabilizando mais rápido. Já para $\xi$, a inequação não se aplicar, uma vez que aumentar $\xi$ diminui $\omega_n$ e deixamos de cumprir os requisitos