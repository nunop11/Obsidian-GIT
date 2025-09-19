- Passemos agora a algo útil para ML.
- Temos pontos de treino $(y_{n},x_{n})~,~n=1,2,\dots,N$ que usamos para estimar um parâmetro desconhecido $\hat{\theta}$. No entanto, notemos que cada ponto é um VA
- Se mudarmos os pontos de treino iremos mudar a nossa estimativa.
- Ou seja: a estimativa determinada com um conjunto de dados é também uma VA.
    - Assim surge a questão: quão boa será uma estimativa e como o podemos saber?

- Usando um certo conjunto de dados, $(\boldsymbol{y},X)$, a nossa estimativa $\hat{\theta}\in\mathbb{R}$ será calculada da forma:
$$\hat{\theta}=f(\boldsymbol{y},X)$$
conforme x,y são VAs, também a estimativa o será. Assim, de forma geral temos:
$$\hat{\boldsymbol{\theta}}=f(\mathbf{y},\text{X})$$
- Esta função $f$ é aquilo a que chamamos de **estimador**.

### MSE
- Uma forma razoável de medir a performance do estimador em relação ao valor real $\theta_{0}$ temos o "mean square error" = MSE:
$$\text{MSE}=\mathbb{E}\left[(\hat{\boldsymbol{\theta}} - \theta_{0})^{2} \right]$$
em que a média $\mathbb{E}$ é feita com **todos os conjuntos** de tamanho $N$.
- Se MSE for baixo, então o estimador será bom.

### Bias e Variância
- Na equação de MSE acima podemos acrescentar e subtrair $\mathbb{E}[\hat{\boldsymbol{\theta}}]$ dentro dos parentesis e temos:
$$\begin{align*}
\text{MSE} &= \mathbb{E}\left[ \left((\hat{\boldsymbol{\theta}}-\mathbb{E}[\hat{\boldsymbol{\theta}}]) + (\mathbb{E}[\hat{\boldsymbol{\theta}}] - \theta_{0}) \right)^{2} \right]\\
&= \mathbb{E}\left[ (\hat{\boldsymbol{\theta}}-\mathbb{E}[\hat{\boldsymbol{\theta}}])^{2}\right] + 2\cancelto{=0}{\mathbb{E}\left[ (\hat{\boldsymbol{\theta}}-\mathbb{E}[\hat{\boldsymbol{\theta}}])(\mathbb{E}[\hat{\boldsymbol{\theta}}] - \theta_{0})\right]} + \mathbb{E}\left[(\mathbb{E}[\hat{\boldsymbol{\theta}}] - \theta_{0}) \right]\\
&= \underbrace{\mathbb{E}\left[ (\hat{\boldsymbol{\theta}}-\mathbb{E}[\hat{\boldsymbol{\theta}}])^{2}\right]}_{\text{Variancia}} + \underbrace{\mathbb{E}\left[(\mathbb{E}[\hat{\boldsymbol{\theta}}] - \theta_{0}) \right]}_{\text{Bias}^{2}}\\
\end{align*}$$

- Ou seja, podemos decompor o MSE em 2 termos:
    - um termo que quantifica a variância da distribuição do nosso estimador em torno da sua média
    - um termo que quantifica o quanto a média do nosso estimador se afasta do valor real

- À primeira, podemos achar que ajustar o estimador de forma que o nosso bias desapareça é bom, ou seja, garantir que $\mathbb{E}[\hat{\boldsymbol{\theta}}]=\theta_{0}$. Mas isso não é verdade.
- Um bom estimador é aquele com MSE mínimo. E reduzir o bias não garante isto.
    - Pelo contrário, um estimador com bias nulo (constrained) costuma ter maior MSE do que um estimador unconstrained.
    - Por outras palavras, um estimador biased otimizado não pode fazer pior que um sem bias.

## Método de Máxima Verosimillhança (Likelihood)
- Passemos agora a usar informação relacionada à natureza estatística dos dados na tarefa de estimar um certo parâmetro. Vamos ver um método geral que no futuro iremos aprofundar mais.

- Temos $N$ observações: $\mathcal{X}=\{\boldsymbol{x}_{1},\boldsymbol{x}_{2},\dots,\boldsymbol{x}_{N}\}$ retiradas de uma certa distribuição. 
- Consideremos a *combinação* destas observações (que são na verdade VAs) segue uma pdf de um *tipo conhecido*: $p(\mathcal{X};\boldsymbol{\theta})$, em que $\boldsymbol{\theta}\in\mathbb{R}^{K}$ é desconhecido. Ou seja, queremos determinar $\boldsymbol{\theta}$!
- Esta função pdf: $p(\mathcal{X};\boldsymbol{\theta})$ é a *função de verosimilhança/likelihood* de $\boldsymbol{\theta}$ em função das observações $\mathcal{X}$.
- Ora, o método de max likelihood diz-nos que o parâmetro é dado por:
$$\hat{\boldsymbol{\theta}}_{ML}:=\underset{\boldsymbol{\theta}}{\text{argmax}}~p(\mathcal{X};\boldsymbol{\theta})$$

- Como sabemos que o logaritmo de alguma coisa é monótono crescente (monótono crescente = função sobe ou fica consntate, nunca desce), será ainda mais útil calcular o maximizante do logaritmo de $p$:
$$\frac{\partial \ln p(\mathcal{X};\boldsymbol{\theta})}{\partial \boldsymbol{\theta}}\Biggr|_{\boldsymbol{\theta}=\boldsymbol{\theta}_{ML}}=0$$
ao logaritmo de $p$ chamamos *função de log-likelihood*

### EX
- Temos os VeAs $\boldsymbol{x}_{1},\boldsymbol{x}_{2},\dots,\boldsymbol{x}_{N}$ observados de uma distribuição normal com *cov conhecida* e *média desconhecida*. Ou seja definimos a função de likelihood:
$$p(\boldsymbol{x}_{n};\boldsymbol{\mu})= \frac{1}{(2\pi)^{l/2}|\Sigma|^{1/2}}\exp \left(\frac{-1}{2} (\boldsymbol{x}_{n}-\mu)^{T} \Sigma^{-1} (\boldsymbol{x}_{n}-\boldsymbol{\mu}) \right)$$
(de notar que aqui temos $N$ funções $p$)

- A função de log-likelihood combinada será:
$$L(\boldsymbol{\mu})=\ln \prod_{n=1}^{N}p(\boldsymbol{x}_{n},\boldsymbol{\mu})=- \frac{N}{2}\ln((2\pi)^{l}|\Sigma|) - \frac{1}{2}\sum\limits_{n=1}^{N}(\boldsymbol{x}_{n}-\mu)^{T} \Sigma^{-1} (\boldsymbol{x}_{n}-\boldsymbol{\mu})$$
- Ao derivar isto dá:
$$\frac{\partial L(\boldsymbol{\mu})}{\partial \boldsymbol{\mu}}:= \begin{bmatrix}\frac{\partial L}{\partial \mu_{1}}\\ \frac{\partial L}{\partial \mu_{2}}\\\vdots\\\frac{\partial L}{\partial \mu_{l}}\end{bmatrix}=\sum\limits_{n=1}^{N}\Sigma^{-1} (\boldsymbol{x}_{n} - \boldsymbol{\mu})$$
- Logo, se igualarmos a 0 dá para obter:
$$\hat{\boldsymbol{\mu}}_{ML}=\frac{1}{N}\sum\limits_{n=1}^{N} \boldsymbol{x}_{n}$$
