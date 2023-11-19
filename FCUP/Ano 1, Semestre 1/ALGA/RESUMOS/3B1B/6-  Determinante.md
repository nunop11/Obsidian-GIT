# 6- Determinante
- Se ilustrarmos e imaginarmos figuras num referencial alterado por uma transformação veremos que áreas podem e muitas vezes alteram-se. Reparámos ainda que *todas as áreas mudam com a mesma proporção*
- Este fator de mudança da área é o seu **determinante.**
- Por exemplo:
    - Se det=2, todas as áreas vão duplicar
    - Se det=1/2, todas as áreas vão passar a ser 
    - Se det=0, todas as áreas passam a ser 0 (o espaço é comprimido numa reta ou ponto)

- No entanto devemos de recordar que o determinante pode ser negativo. Assim, as observações anteriores aplicam-se especialmente a |det|
- No entanto, ter um fator de área negativo também faz sentido. Isso indica que a área é "virada", por exemplo como se tivéssemos uma folha de papel e a virarmos de costas para cima. Ou seja, ocorre quando o referencial é virado do avesso

### Em 3D
- Em 3D, o determinante indica o quanto o *volume* de que algo muda.
- O determinante negativo e portanto a inversão de sentido é algo mais complciado. Basicamente, ao fazer a regra da mão direita:
![[regra mão direita.png]]
- Antes da transformação consegue-se equivaler cada dedo a um vetor (i,j,k).
- Ora, se após a transformação podermos continuar a fazer isto, a orientação não se alterou (e det>0). Caso contrário, se só conseguirmos com a mão esquerda, então a orientação inverteu-se e det<0

## A fórmula
$$det\left( \left[ \begin{array}{cccc}
a \hspace{5mm} b\\
c \hspace{5mm} d
\end{array}\right] \right) = ad-bc$$
(No vídeo é feita uma curta dedução de porquê que isto ocorre)
(É falado da regra do paralelogramo)
- Um paralelogramo definido pelos vetores $\vec a$ e $\vec b$ terá área igual a $det\left( \left[ \begin{array}{cccc} x_a \hspace{5mm} x_b\\ y_a \hspace{5mm} y_b \end{array}\right] \right)$
### Propriedade
Tem-se que:
$$det(M_1M_2)=det(M_1)det(M_2)$$

#### Link do vídeo no Youtube:
https://youtu.be/Ip3X9LOh2dk

#### Índice dos resumos
[[ALGA - INDEX]]

#determinante #alga