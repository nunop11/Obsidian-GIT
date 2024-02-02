## Variável Contínua
- Consideremos que temos um intervalo finito $[a,b]$
- Podemos então definir o comprimento de uma divisão: $\large \Delta x=\frac{b-a}{M}$ 
- Consideremos agora que temos 1 número dentro de 1 divisão $i \to ]i \Delta x, (i+1)\Delta x[$
- Basta redesenhar a figura com intervalos mais curtos que se torna claro que:
$$\lim\limits_{\Delta x\to 0^{+}} P(i \Delta x)=0^{+}$$
em que $P()$ é a probabilidade de encontrar este número.

- Oremos, façamos a transição para a variável contínua: introduzindo a **densidade de probabilidade** $\rho$: $$dP= \rho(x)\Delta x$$
    - Notemos que $P(x)$ é adimensional. Ora, para iso ocorrer é preciso que $\rho(x)$ tenha as seguintes dimensões: $$[\rho(x)]=\frac{1}{[\Delta x]}$$ (Por exemplo, se $x$ for uma distância, a densidade de probabilidade terá dimensão de $\textsf{distância}^{-1}$)

- Além disso, no discreto tínhamos: $$\sum\limits_{i} P_{i}=1 \quad \quad ;\quad \quad \langle x\rangle=\sum\limits_{i} P_{i} x_{i}\tag{Variável Discreta}$$

que no contínuo fica assim:
- Além disso, no discreto tínhamos: $$\int dx ~ \rho(x) =1 \quad \quad ;\quad \quad \langle x\rangle=\int dx~ \rho(x) x\tag{Variável Contínua}$$

- Da equação do valor médio de uma variável conntínua podemos introduzir outro conceito:
### Momento
$$\langle x^{n}\rangle= \int dx~ x^{n} \rho(x)$$
- E temos então: $m_{1}=\langle x\rangle, m_{2}= \langle x^{2}\rangle$
- Consideremos que temos $$\{ m_{1},m_{2},m_{3},\dots,m_{n},\dots \}$$

E temos esta dedução do Viana que não entendi.
$$\begin{align*}
\hat{\rho}&= \langle e^{ikx}\rangle=\int dx~\rho(x)e^{ikx}\\
&= \int dx~ \rho(x) \sum\limits_{n=1}^{+\infty} \frac{(e^{ikx})^{n}}{n!}\\
&= \sum\limits_{n=1}^{+\infty} \frac{(ik)^{n}}{n!} \langle x^{n}\rangle
\end{align*}$$

### Probabilidade de acontecimento em Dist Contínua
- Tendo uma certa densidade de probabilidade $\rho(x)$ e um acontecimento $A$ com função caraterística $\chi_{A}(x)$. Dada por:
$$P_{A}=\int dx~\rho(x) \chi_{A}(x)$$

#### Exemplo
- Consideremos que temos uma variável $x$ cuja densidade de probabilidade conhecemos. Ora, vamos realizar uma segunda atividade $y$ que tem com $x$ a relação: $y=f(x)$. Queremos determinar a densidade de probabilidade de $y$
- Consideremos que consoante obtemos valores de $y$ na experiência, vamos registando a frequência de cada intervalo. Ora, se como no início da aula consideramos que realizamos a experiência $N\to\infty$ vezes (de modo que $\Delta y\to0$). Isso será dado por:
$$\begin{align*}
\rho(y)&= \lim\limits_{\Delta Y\to0^{+}} \frac{P(Y<y<Y+\Delta Y)}{\Delta Y}\\
&= \int dx~ \rho(x) \lim\limits_{\Delta Y\to0^{+}} \frac{\chi(Y<f<Y + \Delta Y)}{\Delta Y}\\
&= \int dx~ \delta (Y-f(x))
\end{align*}$$
sendo que acima se usa:
$$P(x)=\int dx~\rho(x) \chi(x) \quad \quad;\quad \quad \lim\limits_{\Delta Y\to0^{+}} \frac{\chi(Y<f<Y + \Delta Y)}{\Delta Y}=\delta(Y-f(x))$$

## Estimador da média
- Tendo um conjunto de pontos $\{ x_{1},x_{2},\dots,x_{N}\}$ em que cada um tem uma densidade de probabilidade, temos que:
$$\rho(x_{1},x_{2},\dots,x_{N})=\rho(x_{1})\rho(x_{2})\dots \rho(x_{N})=\prod\limits_{i=1}^{N} \rho(x_{i})$$
assim, temos que o valor média é dado por 
$$\begin{align*}
\langle \bar x_{N}\rangle &= \frac{1}{N} \sum\limits_{i=1}^{N} \left[\int dx_{1}dx_{2}(\cdots) dx_{N} ~x_{i} \prod\limits_{k=1}^{N} \rho(x_{k}) \right]\\
&= \frac{1}{N}\sum\limits_{i=1}^{N} \int dx_{i} \rho(x_{i})x_{i} \sum\limits_{k\neq i}\cancelto{=1}{\int dx_{k} \rho(x_{k})}\\
&= \frac{1}{N} \sum\limits_{i=1}^{N} \langle x\rangle\\
&= \langle x\rangle 
\end{align*}$$
assim concluímos que o estimador da média é um bom estimador.

## Variância
$$V^{2}=\langle x^{2}\rangle- \langle x\rangle^{2}$$
- Vejamos a dedução do estimador:
$$\begin{align*}
\langle \overline{x^{2}} - \bar x^{2}\rangle &= \frac{1}{N} \sum\limits_{i=1}^{N} \langle x_{i}^{2}\rangle - \frac{1}{N^{2}}\sum\limits_{i}\sum\limits_{j} \langle x_{i}x_{j}\rangle\\
&= \langle x^{2}\rangle - \frac{1}{N^{2}} \left(\sum\limits_{i=1}^{N} \langle x_{i}\rangle^{2} + \sum\limits_{\substack{j=1\\ j\neq i}}^{N} \langle x_{i}\rangle \langle x_{j}\rangle\right)\\
&=  \frac{N-1}{N} (\langle x^{2}\rangle - \langle x\rangle^{2})
\end{align*}$$
ora, este estimador só será bom para $N\to\infty$. Assim, um bom estimador seria:
$$var(x)=\frac{1}{N-1} \sum\limits_{i=1}^{N} (x_{i}-\bar x)^{2}$$