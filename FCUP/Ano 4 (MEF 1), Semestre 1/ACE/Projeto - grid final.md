- Nestes cálculos usamos coordenadas polares, já que estamos a trabalhar com servos então é mais fácil trabalhar com ângulos.
- Consideramos que a primeira parte do braço apresenta um ângulo $k_{1}$ relativo ao zero (mostrado abaixo). A segunda parte apresenta um ângulo $k_{2}$, relativo ao eixo de $k_{1}$. As 2 porções têm comprimentos $L_{1},L_{2}$. 
![[proj_ace_1 1|800]]
a curva a cinzento representa o range máximo do braço.

- Consideremos que queremos ir buscar um ponto à distância $L_{1}+L_{2}$. Basta rodar o braço inteiro para o ângulo $\alpha$ em que temos o objeto, como vemos na figura do lado esquerdo acima.

- Mas consideremos que o objeto está numa certa posição dentro do range, a uma distância $d<L_{1}+L_{2}$. Naturalmente, como podemos ver na figura da direita acima, temos que rodar os servos em sentidos opostos, de modo que a ponta do braço esteja na mesma na direção $\alpha$, à distância $d$.
- Assim, o objetivo é arranjar uma fórmula que permite determinar $\theta,\beta$ (quanto rodamos cada servo) de modo a atingir uma qualquer distância $d$. 

- Para melhor entender isto, consideremos um referencial alinhado com $\alpha$:
![[ace_projeto_3|750]]
- Consideremos que temos um ponto a uma distância $d$ da coluna do braço. 
- Começamos por definir $\phi$, o ratio de $d$ relativamente ao range do braço:
$$\phi=\frac{d}{L_{1}+L_{2}}$$
- Considerando a imagem acima, a soma das projeções das duas partes do braço no eixo $\alpha$ tem que ser $d$:
$$d=L_{1}\cos\beta + L_{2}\cos(\theta-\beta)$$
e para a ponta do braço estar no eixo $\alpha$, temos que ter uma soma nula das projeções dos braços na direção perpendicular a $\alpha$:
$$L_{1}\sin\beta=L_{2}\sin(\theta-\beta)$$
- Podemos escrever:
$$\sin\beta=\frac{L_{2}}{L_{1}}\sin(\theta-\beta)~~~~\to~~~~ \cos\beta=\sqrt{1-\sin^{2}\beta}=\sqrt{1- \frac{L_{2}^{2}}{L_{1}^{2}}\sin^{2}(\theta- \beta)}$$
juntando isto à equação de cima **fazer referencia no latex** temos:
$$\begin{align*}
L_{1}\sqrt{1- \frac{L_{2}^{2}}{L_{1}^{2}}\sin^{2}(\theta- \beta)}&= d - L_{2}\cos(\theta-\beta)\\
L_{1}^{2}[1- \frac{L_{2}^{2}}{L_{1}^{2}}\sin^{2}(\theta- \beta)]&= d^{2}-2dL_{2}\cos(\theta-\beta) + L_{2}^{2}\cos^{2}(\theta-\beta)\\
L_{1}^{2}-L_{2}^{2}\sin^{2}(\theta-\beta)&= d^{2}-2dL_{2}\cos(\theta-\beta)+L_{2}^{2}\cos^{2}(\theta-\beta)\\
L_{1}^{2}-L_{2}^{2}&= d^{2}-2dL_{2}\cos(\theta-\beta)
\end{align*}$$
podemos escrever: $d=\phi(L_{1}+L_{2})$ logo:
$$\begin{align*}
L_{1}^{2}-L_{2}^{2}&= d^{2}-2dL_{2}\cos(\theta-\beta)\\
L_{1}^{2}-L_{2}^{2}&= \phi^{2}L_{1}^{2}+\phi^{2}L_{2}^{2} + 2\phi^{2}L_{1}L_{2} - 2\phi L_{2}^{2}\cos(\theta-\beta)- 2\phi L_{1}L_{2}\cos(\theta-\beta)\\
L_{1}^{2}-L_{2}^{2}- \phi^{2}L_{1}^{2}-\phi^{2}L_{2}^{2} - 2\phi^{2}L_{1}L_{2} &= - 2\phi L_{2}^{2}\cos(\theta-\beta)- 2\phi L_{1}L_{2}\cos(\theta-\beta)\\
L_{1}^{2}-L_{2}^{2}- \phi^{2}L_{1}^{2}-\phi^{2}L_{2}^{2} - 2\phi^{2}L_{1}L_{2} &= -\cos(\theta-\beta) (2\phi L_{2}^{2} + 2\phi L_{1}L_{2})\\
\cos(\theta-\beta)&= \frac{L_{1}^{2}(\phi^{2}-1) + L_{2}^{2}(\phi+1) + 2\phi^{2}L_{1}L_2}{2\phi L_{2}^{2} + 2\phi L_{1}L_{2}}
\end{align*}$$
em que $L_{1},L_{2},\phi$ são valores conhecidos.

- Assim temos:
$$\begin{align*}
d&= L_{1}\cos\beta + L_{2}\cos(\theta-\beta)\\
\cos\beta&= \frac{d-L_{2}\cos(\theta-\beta)}{L_{1}}
\end{align*}$$
e determinamos $\beta$.

### Resumo
- Temos um ponto $P=(d,\alpha)$ em coordenadas polares. Conhecemos $L_{1},L_{2}$ e podemos então determinar $\phi$.
- Tendo isto obtemos:
$$\begin{align*}
\cos(\theta-\beta)&= \frac{L_{1}^{2}(\phi^{2}-1) + L_{2}^{2}(\phi^{2}+1) + 2\phi^{2}L_{1}L_2}{2\phi L_{2}^{2} + 2\phi L_{1}L_{2}}\\
&\downarrow\\
\beta&= \cos^{-1}\left(\frac{d-L_{2}\cos(\theta-\beta)}{L_{1}}\right)\\
&\downarrow\\
\theta&= \beta+\cos^{-1}\left(\tfrac{L_{1}^{2}(\phi^{2}-1) + L_{2}^{2}(\phi^{2}+1) + 2\phi^{2}L_{1}L_2}{2\phi L_{2}^{2} + 2\phi L_{1}L_{2}}\right)
\end{align*}$$

- Assim, o servo 1 fica com o ângulo $\alpha-\beta$ e o servo 2 fica com o ângulo $\theta$

- Alternativamente, podemos ter um ponto $P=(x,y)$ em coordenadas cartesianas. Facilmente convertemos estes valores em coordenadas polares $(d,\alpha)$:
$$d=\sqrt{(x-L_{1}-L_{2})^{2} + y^{2}}\quad;\quad\alpha=\sin^{-1}\left(\frac{y}{d}\right)$$

## Implementação
- Nós estudamos duas possíveis formas de implementar isto. Ou seja, formas como podemos limitar o movimento dos braços, já que cada servo apenas tem um range de 180º. 
- Decidimos que o servo 1 move-se sempre no range $[0,180]º$. Daí, temos então 2 métodos:
    1. O servo2 começa alinhado com o servo1. Para cada ponto que queremos alcançar, ele pode rodar 90º para a esquerda ou para a direita. Temos o servo 2 no range $[-90,90]º$
    2. O servo2 começa alinhado com o servo1. Para cada coordenada, ele roda sempre "para trás" do servo 1. Ou seja, para este servo o zero é quando está alinhado com o servo 1 e o 180 seria quando o servo está completamente dobrado. Temos o servo 2 no range $[-180,0]º$
- Usando python, simulamos a cobertura que cada um destes métodos nos daria:
Cobertura do método 1:
![[range -90-90.png|700]]
Cobertura do método 2:
![[range 0-180.png|700]]
- Escolhemos o método 2. Apesar de resultar numa cobertura bastante mais irregular, é evidente que temos a maior área, o que é o nosso objetivo. Verificamos que o método 1 cobre 20% dos pontos, enquanto que o método 2 cobre 26%.
- No entanto, na prática é evidente que a segunda parte do braço não pode rodar 180º para trás, já que bateria na primeira parte. Assim, montamos o nosso braço de modo a ter um range $[-120,60]º$, ou seja, 120 graus para "trás" e 60 para a "frente". Isto diminui ligeiramente a cobertura.