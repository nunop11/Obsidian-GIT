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
os sinais são assim porque o servo 1 está num ângulo $\alpha$ então pode recuar. O servo 2 está em 0, logo só pode avançar
- A posição $(x,y)$ pode ser escrita em função de:
$$\begin{cases}
x-L_{1}-L_{2}=L_{1}\cos\alpha+L_{2}\cos\alpha \\
y=L_{1}\sin\alpha+L_{2}\sin\alpha
\end{cases}$$
- Ao variar os ângulos de modo a ir para o ponto $\frac{x}{2},\frac{y}{2}$ teremos:
$$\begin{cases}
\frac{x}{2}-L_{1}-L_{2}=L_{1}\cos(\alpha-\beta)+L_{2}\cos(\alpha+\beta) \\
\frac{y}{2}=L_{1}\sin(\alpha-\beta)+L_{2}\sin(\alpha+\beta)
\end{cases}$$
- Ora, como $x$ e $y$ não mudam, os 2 sistemas são equivalentes:
$$\begin{cases}  
L_{1}\cos\alpha+L_{2}\cos\alpha= 2L_{1}\cos(\alpha-\beta)+2L_{2}\cos(\alpha+\beta)+L_{1}+L_{2} \\
L_{1}\sin\alpha+L_{2}\sin\alpha=2L_{1}\sin(\alpha-\beta)+2L_{2}\sin(\alpha+\beta)
\end{cases}$$
somemos o quadrado das equações:
**lado esquerdo**
$$\begin{align*}
&L_{1}^{2}\cos^{2}\alpha+L_{2}^{2}\cos^{2}\alpha + 2L_{1}L_{2}\cos^{2}\alpha + L_{1}^{2}\sin^{2}\alpha+L_{2}^{2}\sin^{2}\alpha+2L_{1}L_{2}\sin^{2}\alpha=\\
&= L_{1}^{2}+L_{2}^{2}+2L_{1}L_{2}=\\
&= (L_{1}+L_{2})^{2}
\end{align*}$$
**lado direito**
*quadrado da equação 1*
$$\begin{align*}
&(2L_{1}\cos(\alpha-\beta)+2L_{2}\cos(\alpha+\beta))^{2}+(L_{1}+L_{2})^{2}+2(2L_{1}\cos(\alpha-\beta)+2L_{2}\cos(\alpha+\beta))(L_{1}+L_{2})=\\
&= 4L_{1}^{2}\cos^{2}(\alpha-\beta)+4L_{2}^{2}\cos^{2}(\alpha+\beta)+4L_{1}L_{2}\cos(\alpha+\beta)\cos(\alpha-\beta) + (L_{1}+L_{2})^{2}+\\
&+ 4(2L_{1}^{2}\cos(\alpha-\beta)+2L_{1}L_{2}\cos(\alpha-\beta) + 2L_{1}L_{2}\cos(\alpha+\beta)+2L_{2}^{2}\cos(\alpha+\beta))=\\
&= 4 [L_{1}^{2}\cos^{2}(\alpha-\beta)+L_{2}^{2}\cos^{2}(\alpha+\beta) + L_{1}L_{2}\cos(\alpha+\beta)\cos(\alpha-\beta) +2L_{1}^{2}\cos(\alpha-\beta)+ \\
&+2L_{1}L_{2}\cos(\alpha-\beta) + 2L_{1}L_{2}\cos(\alpha+\beta)+2L_{2}^{2}\cos(\alpha+\beta)] + (L_{1}+L_{2})^{2}
\end{align*}$$
*quadrado da equação 2*
$$4 (L_{1}^{2}\sin^{2}(\alpha-\beta) + L_{2}^{2}\sin^{2}(\alpha+\beta) + L_{1}L_{2}\sin(\alpha+\beta)\sin(\alpha-\beta))$$
*soma*
$$\begin{align*}
&(L_{1}+L_{2})^{2}+ 4 [L_{1}^{2}+L_{2}^{2} + L_{1}L_{2}(\cos(\alpha+\beta)\cos(\alpha-\beta)+\sin(\alpha+\beta)\sin(\alpha-\beta)) +\\
&+ 2L_{1}^{2}\cos(\alpha-\beta)+2L_{1}L_{2}\cos(\alpha-\beta) + 2L_{1}L_{2}\cos(\alpha+\beta)+2L_{2}^{2}\cos(\alpha+\beta)]
\end{align*}$$

*simplificar 1ª parcela complicada*
- Podemos usar as fórmulas de somas de senos e cossenos:
$$\begin{align*}
&\cos(\alpha+\beta)\cos(\alpha-\beta) + \sin(\alpha+\beta)\sin(\alpha-\beta)=\\
&= (\cos\alpha\cos\beta-\sin\alpha\sin\beta)(\cos\alpha\cos\beta+\sin\alpha\sin\beta) + (\sin\alpha\cos\beta+\cos\alpha\sin\beta)(\sin\alpha\cos\beta-\cos\alpha\sin\beta)\\
&= \cos^{2}\alpha\cos^{2}\beta-\sin^{2}\alpha\sin^{2}\beta + \sin^{2}\alpha\cos^{2}\beta-\cos^{2}\alpha\sin^{2}\beta\\
&= \cos^{2}\beta-\sin^{2}\beta\\
&= \cos(2\beta)
\end{align*}$$

*simplificar 2ª parcela complicada*
$$\begin{align*}
&L_{1}^{2}\cos(\alpha-\beta) + L_{1}L_{2}\cos(\alpha-\beta)+L_{1}L_{2}\cos(\alpha+\beta)+L_{2}^{2}\cos(\alpha+\beta)=\\
&= L_{1}^{2}\cos(\alpha-\beta) + L_{1}L_{2} (\cos\alpha\cos\beta+\sin\alpha\sin\beta+\cos\alpha\cos\beta-\sin\alpha\sin\beta)+L_{2}^{2}\cos(\alpha+\beta)=\\
&= L_{1}^{2}\cos(\alpha-\beta)+L_{2}^{2}\cos(\alpha+\beta) + 2L_{1}L_{2}\cos\alpha\cos \beta
\end{align*}$$
*quadrado do lado direito - final*
$$(L_{1}+L_{2})^{2} + 4 [L_{1}^{2}+L_{2}^{2}+L_{1}L_{2}\cos(2\beta) +L_{1}^{2}\cos(\alpha-\beta)+L_{2}^{2}\cos(\alpha+\beta) + 2L_{1}L_{2}\cos\alpha\cos \beta]$$

**igualar as somas**
- Os $(L_{1}+L_{2})^{2}$ cortam logo
$$\begin{align*}
0&= L_{1}^{2}+L_{2}^{2}+L_{1}L_{2}\cos(2\beta) +L_{1}^{2}\cos(\alpha-\beta)+L_{2}^{2}\cos(\alpha+\beta) + 2L_{1}L_{2}\cos\alpha\cos\beta\\
-L_{1}^{2}(1+\cos(\alpha-\beta))&= L_{2}^{2}(1+\cos(\alpha+\beta)) + L_{1}L_{2}(1+2\cos\alpha\cos\beta)
\end{align*}$$
