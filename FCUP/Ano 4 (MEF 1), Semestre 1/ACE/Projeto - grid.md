- Começamos com o braço metido para a esqueerda, em que teremos $\theta_{1}=0~,~\theta_{2}=0$. As 2 porções têm comprimentos $L_{1},L_{2}$. 
- Consideremos uma grid que tem a origem no sítio onde estão os braços, à esquerda a uma distância $L_{1}+L_{2}$ da coluna 
![[proj_ace_1|600]]
a curva a cinzento representa o range máximo do braço.
- Penso que se rodarmos os servos para estes ângulos e depois os forçarmos a estar nesta configuração abaixo eles depois conseguirão rodar 180º a partir destas posições. Por verificar
- O range é:
$$\begin{cases}
0\le x\le 2L_{1}+2L_{2} \\
0\le y\le L_{1}+L_{2} \\
\sqrt{(x-L_{1}-L_{2})^{2}+y^{2}}\le L_{1}+L_{2}
\end{cases}$$

### V1
- Temos então uma posição $(x,y)$ dentro do range, a uma distância $D$.
- Uma maneira que temos é determinar o ângulo desde a coluna do braço até à posição: $\alpha$.
- Tendo esta direção, vemos a relação entre $D$ e $L_{1}+L_{2}$. 
    - Se $D=L_{1}+L_{2}$ temos $\theta_{1}=\alpha,\theta_{2}=0$ - o braço move-se como se fosse 1 só peça
- Agora, se $D=(L_{1}+L_{2})/2$ temos que aproximar a ponta do braço. Uma forma de fazer isto é rodar os 2 motores para lados opostos:
![[projeto_ace_2|750]]

- Consideremos um referencial alinhado com $\alpha$:
![[ace_projeto_3|750]]
- Consideremos que temos um ponto $(x,y)$ a uma distância $d$ da coluna do braço. 
- Se $d=L_{1}+L_{2}$ então temos $\beta=0,\theta=0$, como já vimos
- Temos:
$$d=L_{1}\cos\beta + L_{2}\cos(\theta-\beta)$$
e para a ponta do braço estar no plano de $\alpha$, temos que:
$$L_{1}\sin\beta=L_{2}\sin(\theta-\beta)$$
- Podemos escrever:
$$\sin\beta=\frac{L_{2}}{L_{1}}\sin(\theta-\beta)~~~~\to~~~~ \cos\beta=\sqrt{1-\sin^{2}\beta}=\sqrt{1- \frac{L_{2}^{2}}{L_{1}^{2}}\sin^{2}(\theta- \beta)}$$
e temos:
$$\begin{align*}
L_{1}\sqrt{1- \frac{L_{2}^{2}}{L_{1}^{2}}\sin^{2}(\theta- \beta)}&= d - L_{2}\cos(\theta-\beta)\\
L_{1}^{2}[1- \frac{L_{2}^{2}}{L_{1}^{2}}\sin^{2}(\theta- \beta)]&= d^{2}-2dL_{2}\cos(\theta-\beta) + L_{2}^{2}\cos^{2}(\theta-\beta)\\
L_{1}^{2}-L_{2}^{2}\sin^{2}(\theta-\beta)&= d^{2}-2dL_{2}\cos(\theta-\beta)+L_{2}^{2}\cos^{2}(\theta-\beta)\\
L_{1}^{2}-L_{2}^{2}&= d^{2}-2dL_{2}\cos(\theta-\beta)
\end{align*}$$
podemos escrever: $d=\phi(L_{1}+L_{2})$:
$$\begin{align*}
L_{1}^{2}-L_{2}^{2}&= d^{2}-2dL_{2}\cos(\theta-\beta)\\
L_{1}^{2}-L_{2}^{2}&= \phi^{2}L_{1}^{2}+\phi^{2}L_{2}^{2} + 2\phi^{2}L_{1}L_{2} - 2\phi L_{2}^{2}\cos(\theta-\beta)- 2\phi L_{1}L_{2}\cos(\theta-\beta)\\
L_{1}^{2}-L_{2}^{2}- \phi^{2}L_{1}^{2}-\phi^{2}L_{2}^{2} - 2\phi^{2}L_{1}L_{2} &= - 2\phi L_{2}^{2}\cos(\theta-\beta)- 2\phi L_{1}L_{2}\cos(\theta-\beta)\\
L_{1}^{2}-L_{2}^{2}- \phi^{2}L_{1}^{2}-\phi^{2}L_{2}^{2} - 2\phi^{2}L_{1}L_{2} &= -\cos(\theta-\beta) (2\phi L_{2}^{2} + 2\phi L_{1}L_{2})\\
\cos(\theta-\beta)&= \frac{L_{1}^{2}(\phi^{2}-1) + L_{2}^{2}(\phi+1) + 2\phi^{2}L_{1}L_2}{2\phi L_{2}^{2} + 2\phi L_{1}L_{2}}
\end{align*}$$
em que $L_{1},L_{2},\phi$ são coisas que conhecemos.

- Assim temos:
$$\begin{align*}
d&= L_{1}\cos\beta + L_{2}\cos(\theta-\beta)\\
\cos\beta&= \frac{d-L_{2}\cos(\theta-\beta)}{L_{1}}
\end{align*}$$
e assim determinamos $\beta$.

### Resumo
- Temos $P=(x,y)$, em que o referencial começa do lado esquerdo em baixo. Assim: $$d=\sqrt{(x-L_{1}-L_{2})^{2} + y^{2}}$$
daqui temos $$\phi=\frac{d}{L_{1}+L_{2}}$$
- Tendo isto obtemos:
$$\begin{align*}
\cos(\theta-\beta)&= \frac{L_{1}^{2}(\phi^{2}-1) + L_{2}^{2}(\phi^{2}+1) + 2\phi^{2}L_{1}L_2}{2\phi L_{2}^{2} + 2\phi L_{1}L_{2}}\\
&\downarrow\\
\beta&= \cos^{-1}\left(\frac{d-L_{2}\cos(\theta-\beta)}{L_{1}}\right)\\
&\downarrow\\
\theta&= \beta+\cos^{-1}\left(\tfrac{L_{1}^{2}(\phi^{2}-1) + L_{2}^{2}(\phi^{2}+1) + 2\phi^{2}L_{1}L_2}{2\phi L_{2}^{2} + 2\phi L_{1}L_{2}}\right)
\end{align*}$$
- E temos:
$$\alpha=\sin^{-1}\left(\frac{y}{d}\right)$$
- Assim, o servo 1 fica com o ângulo $\alpha-\beta$ e o servo 2 fica com o ângulo $\theta$

## Implementação
- Ver o notebook
- A dedução que fiz acima pode usar direções de ângulos errados, mas as equações estão certas. Depois é uma questão de trocar sinais e outras coisas que fiz no python
- Sei de duas formas de implementar isto:
    1. O servo2 começa alinhado com o servo1 e isso é $\theta=90$. Para cada coordenada que queremos alcançar, ele roda entre 0 e 180. Ou seja, roda 90º para a esquerda e para a direita. Isto parece a approach mais intuitiva.
    2. O servo2 começa alinhado com o servo1 e isso é $\theta=0$. Para cada coordenada, ele roda de 0 a 180, sempre "atrás" do servo 1. Ou seja, o zero é quando o braço está extendido e o 180 seria quando o servo está completamente dobrado. Esta approach é menos intuitiva mas dá melhor cobertura:
Cobertura de método 1:
![[Pasted image 20241130233315.png]]
Cobertura de método 2:
![[Pasted image 20241130233220.png]]

- Para o método 2 n\ao podemos ter exatamente isto. Na realidade o servo2 não pode rodar 180º para trás, bate no braço em si. Mudemos então a escala de $[0,180]$ para $[-30,150]$. A cobertura fica:
![[Pasted image 20241130234642.png]]
continuamos a ter uma cobertura grande e agora conseguimos chegar ao canto oposto. Mas quanto mais próximo do range $[0,180]$ maior será a nossa área disponível.
- O código que tenho pode facilmente ser adapatado para qualquer range que vejamos que é possível na vida real. Também penso que não será muito difícil recriar a função em C++