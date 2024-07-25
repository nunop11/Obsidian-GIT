###### Aula 8 - 15/03/2024
**Cenas de Episódios Anteriores**
- Vimos na aula anterior:
$$\begin{align*}
c_{v}&= \frac{\partial u}{\partial T}\\
\int \frac{d^{3}k}{4\pi^3}F(\vec{k})&= \int_{0}^{\infty} g(\varepsilon)F(\varepsilon)d\varepsilon
\end{align*}$$
em que $$\varepsilon(\vec{k})=\frac{\hbar^{2}k^{2}}{2m} \quad \quad;\quad \quad g(\varepsilon)=\frac{m}{\pi^{2}\hbar^{2}}\sqrt{\frac{2m}{\hbar^{2}}}\sqrt{\varepsilon}=\frac{3}{2} \frac{n}{\varepsilon_{F}}\sqrt{\frac{\varepsilon}{\varepsilon_{F}}}$$
- Temos então:
$$u=\int_{0}^{+\infty}\varepsilon f(\varepsilon)g(\varepsilon)~d\varepsilon \quad \quad;\quad \quad n=\int_{0}^{+\infty}f(\varepsilon)g(\varepsilon)~d\varepsilon$$

- Vimos ainda que $u,n$ são definidos por integrais do tipo $I=\int_{0}^{+\infty}d\varepsilon~H(\varepsilon)f(\varepsilon)d\varepsilon$ que pode ser aproximada pela **Expansão de Sommerfeld**:
$$I = \int_{0}^{\mu}H(\varepsilon)d\varepsilon+ \frac{\pi^{2}}{6}(k_{B}T)^{2} \frac{dH}{d\varepsilon}|_{\mu} + \frac{7\pi^{4}}{360}(k_{B}T)^{4} \frac{d^{3}H}{d\varepsilon^{3}}|_{\mu}+\dots$$

**Energia por volume**
- Vimos então que $u=\int_{0}^{\infty}d\varepsilon~[\varepsilon g(\varepsilon)]f(\varepsilon)=\int_{0}^{\infty}d\varepsilon~H(\varepsilon)f(\varepsilon)$. Podemos aplicar a expansão de Sommerfeld:
$$\begin{align*}
u=\int_{0}^{\mu}d\varepsilon~ [\varepsilon g(\varepsilon)]+ \frac{\pi^{2}}{6}(k_{B}T)^{2} \frac{d}{d\varepsilon}[\varepsilon g(\varepsilon)]_\mu+\dots
\end{align*}$$
(normalmente chega ir ao 2º termo)

**Calor Específico**
- Ora, para obter $u$ precisamos do potencial químico. Podemos escrever:
$$\left(\frac{\partial \mu}{\partial T}\right)_{v}=\frac{\left(\frac{\partial N}{\partial T}\right)_{v}}{\left(\frac{\partial N}{\partial \mu}\right)_{v}}$$
- Usando $n=\int_{0}^{\infty}g(\varepsilon)f(\varepsilon)d\varepsilon$ e a sua expansão temos:
$$N=nV = V \int_{0}^{\mu}d\varepsilon g(\varepsilon)+ V \frac{\pi^{2}}{6}(k_{B}T)^{2}g'(\mu)+\dots$$
- Daqui temos
$$\left(\frac{\partial N}{\partial T}\right)_{v}=V \frac{\pi^{2}}{6}k_{B}^{2}2Tg'(\mu)+\dots$$
$$\left(\frac{\partial N}{\partial \mu}\right)_{v}=V g(\mu)+V \frac{\pi^{2}}{6}(k_{B}T)^{2}g''(\mu )$$

- Conforme a aula anterior: $g(\varepsilon)=\frac{3}{2} \frac{n}{\varepsilon_{F}} \sqrt{\frac{\varepsilon}{\varepsilon_{F}}}$ logo
$$g''(\mu)=- \frac{n}{6} \frac{1}{(\varepsilon_{F}\mu)^{\frac{3}{2}}} $$
- Assim fica:
$$\left(\frac{\partial N}{\partial \mu}\right)_{v}=V g(\mu)+V \frac{\pi^{2}}{6}(k_{B}T)^{2} \left[- \frac{n}{6} \frac{1}{\left(\varepsilon_{F}\mu\right)^{\frac{3}{2}}} \right]$$
ora, como vimos na aula 6: $\varepsilon_{F}=k_{B}T_{F}$ em que $T_{F}\sim 10^{4}\text{F}$. Assim, temos um termo $(k_{B}T)^{2}/(k_{B}T_{F})^\frac{3}{2}$. Ora, para temperaturas $T$ baixas podemos considerar que isto vai para zero. Assim, na equação acima a segunda parcela pode ser desprezada:
$$\left(\frac{\partial N}{\partial \mu}\right)_{v}=V g(\mu)$$
- Assim resulta que:
$$\left(\frac{\partial \mu}{\partial T}\right)_{v}=\frac{\left(\frac{\partial N}{\partial T}\right)_{v}}{\left(\frac{\partial N}{\partial \mu}\right)_{v}}=- \frac{\pi^{2}}{3} k_{B}^{2}T \frac{g'(\mu)}{g(\mu)}$$
- Para obter $\mu(T)$ vamos integrar esta expressão:
$$\begin{align*}
\int_{\mu(0)=\varepsilon_{F}}^{\mu(T)}d\mu &= \int_{0}^{T} - \frac{\pi^{2}}{3} k_{B}^{2}T \frac{g'(\mu)}{g(\mu)}dT\\
\mu(T)-\varepsilon_{F} &= - \frac{\pi^{2}}{6} (k_{B}T)^{2} \frac{g'(\mu)}{g(\mu)}\\
\end{align*}$$
- Podemos reorganizar e fica:
$$\begin{align*}
\mu(T)-\varepsilon_{F} &= - \frac{\pi^{2}}{6} (k_{B}T)^{2} \frac{g'(\varepsilon_{F})}{g(\varepsilon_{F})}\\
\mu(T) &= \varepsilon_{F}- \frac{\pi^{2}}{6} (k_{B}T)^{2} \frac{g'(\varepsilon_{F})}{g(\varepsilon_{F})}\\
\end{align*}$$
Ora, se considerarmos temparaturas baixas (até $\sim300\text{K}$) podemos dizer que $\mu=\varepsilon_{F}$. Mas devemos sempre recordar que apenas consideramos os 2 primeiros termos das expansões. Assim, esta expressão só é de confiança até $T^{2}$.

**Energia por Volume -- 2**
- Já temos $\mu(T)$. Voltemos então à equação de cima:
$$\begin{align*}
u &= \int_{0}^{\mu}g(\varepsilon)\varepsilon~d\varepsilon+ \frac{\pi^{2}}{6} (k_{B}T)^{2}
 \frac{d}{d\varepsilon}[\varepsilon g(\varepsilon)]_{\mu}\\
&= \int_{0}^{\mu} g(\varepsilon)\varepsilon ~d\varepsilon+ \frac{\pi^{2}}{6}(k_{B}T)^{2}g(\varepsilon_{F})+ \frac{\pi^{2}}{6}(k_{B}T)^{2}\varepsilon_{F}g'(\varepsilon_{F})\\
&= \left[\int_{0}^{\varepsilon_{F}+(\mu-\varepsilon_{F})} g(\varepsilon)\varepsilon ~d\varepsilon\right]+ \frac{\pi^{2}}{6}(k_{B}T)^{2}g(\varepsilon_{F})+ \frac{\pi^{2}}{6}(k_{B}T)^{2}\varepsilon_{F}g'(\varepsilon_{F})\\
&= \left[\int_{0}^{\varepsilon_{F}}g(\varepsilon)\varepsilon~d\varepsilon+(\mu-\varepsilon_{F})\varepsilon_{F}g(\varepsilon_{F})\right]+\frac{\pi^{2}}{6}(k_{B}T)^{2}g(\varepsilon_{F})+ \frac{\pi^{2}}{6}(k_{B}T)^{2}\varepsilon_{F}g'(\varepsilon_{F})\\
&= \int_{0}^{\varepsilon_{F}}g(\varepsilon)\varepsilon~d\varepsilon+ \left(- \frac{\pi^{2}}{6} (k_{B}T)^{2} \frac{g'(\varepsilon_{F})}{g(\varepsilon_{F})}\right)\varepsilon_{F}g(\varepsilon_{F})+\frac{\pi^{2}}{6}(k_{B}T)^{2}g(\varepsilon_{F})+ \frac{\pi^{2}}{6}(k_{B}T)^{2}\varepsilon_{F}g'(\varepsilon_{F})\\
&= \int_{0}^{\varepsilon_{F}}g(\varepsilon)\varepsilon~d\varepsilon - \cancel{\frac{\pi^{2}}{6} (k_{B}T)^{2} \varepsilon_{F}g'(\varepsilon_{F})}+\frac{\pi^{2}}{6}(k_{B}T)^{2}g(\varepsilon_{F})+ \cancel{\frac{\pi^{2}}{6}(k_{B}T)^{2}\varepsilon_{F}g'(\varepsilon_{F})}\\
&= \int_{0}^{\varepsilon_{F}}g(\varepsilon)~d\varepsilon + \frac{\pi^{2}}{6}(k_{B}T)^{2}g(\varepsilon_{F})
\end{align*}$$
em que decompusemos o intervalo de integração nos intervalos $[0,\varepsilon_{F}]$ e $[\varepsilon_{F},\mu]$.
- Temos então
$$c_{v}=\left(\frac{\partial u}{\partial T}\right)_{v}= \frac{\pi^{2}}{3}k_{B}^{2} g(\varepsilon_{F})T= \frac{\pi^{2}}{2} \left(\frac{k_{B}T}{\varepsilon_{F}}\right)nk_{B}\sim \frac{n}{\varepsilon_{F}}T$$
sendo que a relação experimental observada pode ser vista abaixo:
![[calor especifico vs temperatura.png|400]]
Em primeira vista parece que o modelo de Sommerfeld falha! Mas podemos ver que para $T\to0$ temos um traçado quase linear, é aí que o modelo se aplica melhor.

**NOTAS**
- Podemos ainda fazer o gráficto de $c_{v}/T$ vs $T$. Obviamente deveremos ter uma reta horizontal. Experimentalmente, ao analisar vários metais e ligas esta relação verifica-se.
- Podemos comparar este calor térmico com aquele previsto pela física estatística clássica: $c_{v}=\frac{3}{2}nk_{B}$. Vemos que temos um fator $\frac{\pi^{2}}{3} \frac{k_{B}T}{\varepsilon_{F}}$ a mais. Ora, mesmo a temperatura ambiente este fator é $\sim10^{-2}$. Desta forma, a contribuição dos graus de liberdade dos eletrões para o calor específico é desprezada, o que bate certo.
![[distribuição estados fermi.png]]
- Podemos interpretar isto da seguinte forma: como vemos na curva de $f(\varepsilon)$ acima, consoante aumentamos de  $T=0$ ficamos com secções curvas. Ora, há eletrões que em $T=0$ teriam energias na região a escuro e que, com o aumento da temperatura passam para a região de baixo. Ora, quanto maior for $T$ menos vertical será a secção em torno de $\varepsilon=\varepsilon_{F}$ e mais eletrões estarão no intervalo com energia superior à de Fermi.
- Assim, a temperaturas mais elevadas temos então que considerar as contribuições iónicas e eletrónicas. Podemos então escrever: $c_{v}=\gamma T+\beta T^{3}$. Assim, temos $\frac{c_{v}}{T}=\gamma+\beta T^{2}$. Se representarmos $c_{v}/T$ vs $T^{2}$ iremos obter uma reta com ordenada na origem $\gamma$. Isto é verificado experimentalmente. 

## Paramagnetismo de Pauli
- Vamos definir a suscetibilidade de um metal: $\chi$
- Recordemos:
    - *paramagnetismo Landau* - quando não sujeito a campo B momentos magnéticos desalinhados, quando sujeito alinhados
    - *diamagnetismo* - processo de resposta a um campo amplicado (lei de lens aplicada)

- Iremos agora ver o **paramagnetismo de Pauli**. Temos:
$$\chi_{L}=- \frac{1}{3} \chi_{Pauli}$$

- Neste estudo não iremos considerar o momento orbital, considerando apenas o Spin.
- Temos $u=g \mu_{B}m_{s}B$:
    - $g$ é o fator de Landau com $g\sim2$
    - $m_{s}=\pm\frac12$ 
    - $\mu_{B}=\frac{\hbar c}{2m}=5.27\cdot10^{-24}\text{Am}^{2}$
- Fica $$u=\pm \mu_{B}B$$

- Consideremos um Hamiltoniano sem campo de 1 eletrão $H_{0}^{e}= \frac{p^{2}}{2m}$ com o Hamiltoniano do sistema a ser $H_{0}=\sum_{i=1}^{N}\frac{p_{i}^{2}}{2m}$. Como consideramos eletrões de Sommerfeld, não temos termo de interação entre eletrões.
- Ora, vamos *perturbar* o sistema com um campo magnético. Temos o vetor potencial magnético: $\vec{A}(\vec{r})=\frac{\vec{B}\times\vec{R}}{2}$.
- Ficamos com
$$H=\sum\limits_{i=1}^{N} \frac{(\vec{p_{i}}-e \vec{A}(\vec{r}))^{2}}{2m}+ g\mu _{B} \vec{B}\cdot\vec{S}$$(o $-e\vec{A}$ é importante, já que a energia de ligação é $-\vec{\mu}\cdot\vec{B}$)
matemática ocorre e obtemos:
$$H=\sum\limits_{i=1}^{N} \frac{\vec{p}_{i}^{~2}}{2m} - \mu_{B}(\vec{L}+g \vec{S})\cdot \vec{B}+ \frac{e^{2}}{2m} \sum\limits_{i=1}^{N}(\vec{B}\times\vec{r}_{i})$$
em que vimos que $\vec{L}=\vec{0}$. Por alguma razão o último termo é $\sim0$ e temos:
$$H\simeq \sum\limits_{i=1} \frac{\vec{p}_{i}^{~2}}{2m}-g \mu_{B} \vec{B}\cdot\vec{S}$$
- Desta forma temos:
$$\begin{align*}
\varepsilon(k,\uparrow)&= \frac{\hbar^{2}k^{2}}{2m} - \mu_{B}B\\
\varepsilon(k,\downarrow)&= \frac{\hbar^{2}k^{2}}{2m} + \mu_{B}B
\end{align*}$$
- Aqui há algo muito importante que foi assumido: **o campo B aponta para cima**. Se apontasse para baixo, os sinais trocariam. Tal como a imagem abaixo indica, o que importa é se o spin é paralelo ou antiparalelo ao campo.
- Assim, a energia de ligação magnética é dada por $- \vec{\mu}\cdot\vec{B}$. No spin para cima temos $\text{spin}\parallel \text{campo}$ logo energia negativa. Caso contrário, são anti paralelos e produto escalar negativo. Fica $-(-\text{produto})=+\text{produto}$
- Isto significa ainda que temos 2 densidades de estados: $g(\varepsilon_{\uparrow})\propto\sqrt{\varepsilon_{\uparrow}},g(\varepsilon_{\downarrow})\propto\sqrt{\varepsilon_{\downarrow}}$ . Graficamente, representamos o up como representamos $g(\varepsilon)$ até agora. Apenas para não haver sobreposição, representamos o down ao contrário. Assim:
![[paramagnetismo pauli.png|500]]
ora, vemos a energia de Fermi. Os estados que quando $B=0$ estão nesse patamar sobem se tiverem spin up e descem se tiverem spin down. Ou seja, ficamos com estados que têm energia "a mais" devido ao gráfico de spin up subir (secção marcada acima de $\varepsilon_{F}$). Ora, estes elletrões passam para a região por preencher no spin down.

- De notar que $\mu_{B}=5.7\cdot10^{-5} \text{eV/T}$ logo $\mu_{B}B=5.7\cdot10^{-5}\text{eV}$. Ora temos que, em metais, $\varepsilon_{F}\sim 1-10\text{eV}$. Assim, como $\varepsilon_{F}\gg \mu_{B}B$ podemos usar a teoria de perturbações (como usamos para definir o Hamiltoniano). E temos ainda que as tiras acima e abaixo de $\varepsilon_{F}$ são extremamente finas.