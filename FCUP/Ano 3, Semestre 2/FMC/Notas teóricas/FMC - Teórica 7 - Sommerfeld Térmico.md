###### Aula 7 - 13/03/2024
**Distribuição de estados de Fermi**
- Consideremos o modelo de Sommerfeld : um sistema de $N$ eletrões livres (não sujeitos a potencial) e independentes (não colidem nem interagem entre si)
- Num certo estado $\ell$ de energia $\varepsilon_{\ell}$ definimos o *parâmetro de ocupação* $n_{\ell}$ que pode ser 0 ou 1 (1 se ocupado e vice-versa)
- Desta forma temos $N=\sum\limits_{\ell}n_{\ell}$ estados com energia total $\varepsilon=\sum\limits_{\ell}n_{\ell}\varepsilon_{\ell}$.
- Recordando Física Estatística, podemos definir a função partição: $$Z=\sum\limits_\text{estados} e^{\beta(\mu N-\varepsilon)} \quad \quad ;\quad \beta=\frac{1}{k_{B}T}$$
que podemos escrever como:
$$\begin{align*}
Z&= \sum\limits_{n_{1}=0}^{1}\sum\limits_{n_{2}=0}^{1}\sum\limits_{n_{3}=0}^{1}\cdots\sum\limits_{n_{\ell}=0}^{1}\exp\left[\beta\left({\sum\limits_{\ell}n_{\ell}(\mu-\varepsilon_{\ell})}\right)\right]\\
&= \prod_{\ell} \left\{ \sum\limits_{n_{\ell}=0}^{1}e^{\beta n_{\ell}(\mu-\varepsilon_{\ell})} \right\}\\
&= \prod_{\ell} \left[1 + e^{\beta(\mu-\varepsilon_{\ell})} \right] 
\end{align*}$$
- E podemos definir a função de grande partição
$$\begin{align*}
\mathcal{G}&= - k_{B}T\ln Z\\
&= -k_{B}T \sum\limits_{\ell} \left[\ln \left(1+ e^{\beta(\mu-\varepsilon_{\ell})} \right) \right]\\
&= -k_{B}T V \int d\varepsilon ~g(\varepsilon) \ln \left( 1+ e^{\beta(\mu-\varepsilon)}\right) \quad \quad \quad (\ell\to\infty)\\
\end{align*}$$
se derivarmos os dois lados da equação em $\mu$ temos:
$$\frac{\partial \mathcal{G}}{\partial \mu}=- \cancel{k_{B}T} V \int d\varepsilon ~g(\varepsilon)\frac{\cancel{\beta} e^{\beta(\mu-\varepsilon)}}{1+e^{\beta(\mu-\varepsilon)}}$$
- Ora, temos a equação $N=-\frac{\partial \mathcal{G}}{\partial \mu}$. Assim, se dividirmos os 2 lados por $V$ obtemos:
$$n=\int d\varepsilon~g(\varepsilon)\frac{e^{\beta(\mu-\varepsilon)}}{1+ e^{\beta(\mu-\varepsilon)}}=\int d\varepsilon~g(\varepsilon)\frac{1}{e^{\beta(\varepsilon-\mu)}+1}=\int d\varepsilon~g(\varepsilon)f(\varepsilon)$$
e vemos que obtivemos $f(\varepsilon)$, a **distribuição de Fermi**.

- Ora, como vimos na aula anterior, $g(\varepsilon)\propto\sqrt{\varepsilon}$ é a densidade de estados. Tem a forma:
![[densidade energias e energia fermi.png|500]]

- E temos que a distribuição de Fermi é representada por
![[distribuição estados em energia de sommerfeld.png]]
(sendo o eixo xx $\varepsilon-\varepsilon_{F}$, a zona mais vertical corresponde a $\varepsilon=\varepsilon_{F}$)

- Podemos ver, de uma forma gráfica, porquê que o nível de Fermi é o nível ocupado com maior energia: A densidade de estados é dada pelo produto $g\cdot f$. Como em $\varepsilon=\varepsilon_{F}$ a distribuição de Fermi cai para zero rapidamente (ou instantaneamente se $T=0K$), então o produto $g\cdot f$ e consequentemente $n$ também o faz.

**Comportamento Térmico**
- Podemos dizer que $g(\varepsilon)d\varepsilon$ é o número de estados com energia $[\varepsilon,\varepsilon+d\varepsilon]$, por unidade de volume.
- Assim, $g(\varepsilon_{F})k_{B}T$  será o número de estados por volume com energia $\varepsilon_{F}$. Nesta equação substituimos $d\varepsilon=k_{B}T$ porque a "largura" da secção curva do gráfico de $f(\varepsilon)$ é $k_{B}T$:
![[largura zona curva densidade estados fermi.png|450]]
ou seja, $g(\varepsilon_{F})k_{B}T$ é a densidade volúmica de estados com energia no intervalo $[\varepsilon_{F}- \frac{1}{2}k_{B}T,\varepsilon_{F}+ \frac{1}{2} k_{B}T]$.

- Sabemos que, pela definição de nível de Fermi, para $T=0$ temos:
$$\begin{align*}
f_{k}=1 \quad &;\quad \varepsilon_{k}<\varepsilon_{F}\\
f_{k}=0 \quad &;\quad \varepsilon_{k}>\varepsilon_{F}
\end{align*}$$
no entanto, para temos $f(\varepsilon)=\frac{1}{1^{\beta(\varepsilon-\mu)}+1}$ em $T\to0$:
$$\lim\limits_{T\to0} f= \frac{1}{\lim\limits_{T\to0} \left[\exp(\frac{\varepsilon-\mu}{k_{B}T})\right]+1}\sim \frac{1}{\exp(\frac{\varepsilon-\mu}{0})+1}$$
ou seja: 
    - se $\varepsilon>\mu$ ficamos com $f\sim \frac{1}{\exp(+\infty)+1}=\frac{1}{\infty}=0$
    - se $\varepsilon<\mu$ ficamos com $f\sim \frac{1}{\exp(-\infty)+1}=\frac{1}{0+1}=1$ 

- Ou seja, para que a definição de nível de Fermi e a distribuição de Fermi batam certo em $T=0$ é preciso que:
$$\lim\limits_{T\to0}\mu=\varepsilon_{F}$$
em metais isto verifica-se bastante bem, e até temperaturas ambiente ($\sim300\text{K}$)

**Calor específico**
*Energia*
- Sabemos que
$$c_{v}=\left(\frac{\partial u}{\partial T} \right)_{V}$$
em que temos $u=U/V$ (densidade de energia) e podemos escrever
$$u=2 \sum\limits_{k} \varepsilon(k)f(k)$$
- Em que:
    - o $2$ surge de termos 2 eletrões em cada estado de número de onda $k$. No entanto, na realidade podemos ter 1 eletrão nos níveis mais altos. Mas como $k_{B}T$ é muito reduzido, isto acaba por não importar
    - a distribuição de Fermi atua como uma espécie de restrição, removendo alguns casos do sumatório/integral. Três casos comparáveis:
        - Delta de Kronecker: $\sum_{k} f_{k} \delta_{ki}=f_{i}$
        - Delta de Dirac: $\int_{-\infty}^{+\infty} f(x)\delta(x-a)dx=f(a)$
        - Função degrau: $\int_{-\infty}^{+\infty}f(x)u(x)dx=\int_{0}^{+\infty}f(x)dx$

*Estados*
- Temos ainda:
$$n=2\int \frac{d^{3}k}{8\pi^{3}}f(\varepsilon)=\int \frac{d^{3}k}{4\pi^{3}}f(\varepsilon)$$
e podemos generalizar para o caso de ter uma função genéria $F$: $$n=\int \frac{d^{3}k}{4\pi^{3}}F(\varepsilon)f(\varepsilon)$$
- Podemos converter este integral em coordenadas esféricas:
$$n=\int_{0}^{\infty}\frac{1}{4\pi^{3}}\cdot4\pi k^{2}dk~F(\varepsilon)f(\varepsilon)=\int_{0}^{+\infty} \frac{k^{2}}{\pi^{2}} dk~F(\varepsilon)f(\varepsilon)$$
Temos que $\varepsilon_{k}=\frac{\hbar^{2}k^{2}}{2m}\to k^{2}=\frac{2m\varepsilon}{\hbar^{2}}$: 
$$n=\int_{0}^{+\infty} \frac{2m\varepsilon}{\hbar^{2}\pi^{2}}dk~F(\varepsilon)f(\varepsilon)$$
 e ainda $dk=\frac{1}{2}\sqrt{\frac{2m}{\hbar^{2}\varepsilon}}d\varepsilon$:
$$\begin{align*}
n&= \int_{0}^{+\infty} \frac{2m\varepsilon}{\hbar^{2}\pi^{2}} \frac{1}{2} \sqrt{\frac{2m}{\hbar^{2}\varepsilon}}~F(\varepsilon)f(\varepsilon)d\varepsilon\\
&= \int_{0}^{\infty} \frac{m}{\hbar^{2}\pi^{2}}\sqrt{\frac{2m\varepsilon}{\hbar^{2}}}F(\varepsilon)f(\varepsilon)d\varepsilon\\
&= \int_{0}^{\infty}g(\varepsilon)F(\varepsilon)f(\varepsilon)d\varepsilon
\end{align*}$$

- A densidade de estados corresponde ao caso mais específico de $F(\varepsilon)=\varepsilon$ e $n$ corresponde a $F(\varepsilon)=1~,~\forall\varepsilon$. Temos:
$$\begin{align*}
n=\int_{0}^{\infty}g(\varepsilon)f(\varepsilon)d\varepsilon \quad \quad;\quad \quad u=\int_{0}^{\infty}\varepsilon g(\varepsilon)f(\varepsilon)d\varepsilon
\end{align*}$$
enquanto que o integral acima fica: $n=\int_{0}^{\infty} \frac{m}{\hbar^{2}\pi^{2}}\sqrt{\frac{2m\varepsilon}{\hbar^{2}}}f(\varepsilon)d\varepsilon$

*Densidade de Estados p/ Energia*
- Pelo que podemos definir:
$$g(\varepsilon)=\begin{cases}
\frac{m}{\hbar^{2}\pi^{2}}\sqrt{\frac{2m\varepsilon}{\hbar^{2}}}  & ; & \varepsilon>0 \\
0 & ; & \varepsilon<0
\end{cases}$$
- Temos $\varepsilon_{F}=\frac{\hbar^{2}k_{F}^{2}}{2m}=\frac{\hbar^{2}}{2m}(3\pi^{2} n)^{\frac{2}{3}} ~\to~ \frac{\hbar^{2}}{m}=\frac{2\varepsilon_{F}}{(3\pi^{2}n)^{\frac{2}{3}}}~\to~ \frac{m}{\hbar^{2}}=\frac{2(3\pi^{2}n)^{\frac{2}{3}}}{2\varepsilon_{F}}$ logo podemos escrever:
$$\begin{align*}
g(\varepsilon)&= \frac{m}{\hbar^{2}\pi^{2}}\sqrt{\frac{2m\varepsilon}{\hbar^{2}}}\\
&= \frac{1}{\pi^{2}} \frac{(3\pi^{2}n)^{\frac{2}{3}}}{2\varepsilon_{F}} \sqrt{\cancel{2}\varepsilon} \sqrt{\frac{(3\pi^{2}n)^{\frac{2}{3}}}{\cancel{2}\varepsilon_{F}}}\\
&= \frac{1}{2\pi^{2}\varepsilon_{F}} \sqrt{\frac{\varepsilon}{\varepsilon_{F}}}(3\pi^{2}n)^{\frac{2}{3}}\cdot(3\pi^{2}n)^{\frac{1}{3}}\\
&= \frac{1}{2\cancel{\pi^{2}}\varepsilon_{F}}\sqrt{\frac{\varepsilon}{\varepsilon_{F}}} \cdot 3\cancel{\pi^{2}}n\\
&= \frac{3}{2} \frac{n}{\varepsilon_{F}} \sqrt{\frac{\varepsilon}{\varepsilon_{F}}}
\end{align*}$$
ou seja temos
$$g(\varepsilon)=\begin{cases}
\frac{3}{2} \frac{n}{\varepsilon_{F}} \sqrt{\frac{\varepsilon}{\varepsilon_{F}}}  & ; & \varepsilon>0 \\
0 & ; & \varepsilon<0
\end{cases}$$
em que devemos notar que:
$$g(\varepsilon_{F})=\frac{3}{2} \frac{n}{\varepsilon_{F}}$$
sendo $\varepsilon_{F}=\frac{\hbar^{2}k_{F}^{2}}{2m}$ e $n=\frac{k_{F}^{3}}{3\pi^{2}}$ temos
$$g(\varepsilon_{F})=\frac{mk_{F}}{\hbar^{2}\pi^{2}}$$

- Temos ainda o gráfico da densidade:
![[probabilidade estado ocupado.png]]
em que o gráfico de cima corresponde a $T=0\text{K}$ e o de baixo a $T>0\text{K}$.

**Resolver os Integrais**
- Vimos então os seguintes integrais:
$$\begin{align*}
n=\int_{0}^{\infty}g(\varepsilon)f(\varepsilon)d\varepsilon \quad \quad;\quad \quad u=\int_{0}^{\infty}\varepsilon g(\varepsilon)f(\varepsilon)d\varepsilon
\end{align*}$$
que não são triviais de resolver.

- Ora, podemos escrevê-los ambos como:
$$I(\mu)=\int_{0}^{\infty}d\varepsilon~H(\varepsilon)f(\varepsilon)$$
em que a função $H$ é bem comportada, contínua, etc na região $\mu=\varepsilon_{F}$ em que $F$ varia muito rapidamente.
- E podemos aplicar a **expansão de Sommerfeld** (não deduzida, porque é demasiado complicada):
$$I(\mu)=\int_{0}^{\mu}H(\varepsilon)d\varepsilon + \frac{\pi^{2}}{6} (k_{B} T)^{2} \left(\frac{dH}{d\mu}\right)_{\mu}+ \mathcal{O}(T^{4})$$