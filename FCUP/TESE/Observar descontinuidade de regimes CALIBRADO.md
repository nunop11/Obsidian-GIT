- A 65cm:
![[Pasted image 20260129194417.png]]
Existe quebra da parede mas temos uma quebra constante de cerca de 4cm. O algoritmo consegue detetar a parede (a 70cm o algoritmo aceita esta quebra dentro da sua tolerância). Esta quebra ocorre devido a pontos acima e abaixo do centro estarem a uma distância em que trocamos de regime.
- A 67cm:
![[Pasted image 20260129194430.png]]
Apenas a parte central da parede é detetada. Agora teremos uma maior porção da parede a distâncias do regime 2, pelo que terão maior desvio padrão. Assim, um certo ponto pode "calhar" num regime ou outro conforme o ruído.
- A 68cm:
![[Pasted image 20260129194437.png]]
Temos o mesmo efeito que em 67cm mas pior. Quase toda a parede está no regime 2, mas nem toda. Isto gera instabilidade e a parede quebra-se. Quase nunca é detetada.
- A 69cm:
![[Pasted image 20260129194545.png]]
Vemos algo parecido aos 68cm.
- A 70cm:
![[Pasted image 20260129195238.png|286]]
Alguns pontos ficam no regime 1 devido ao ruído, mas a parede é frequentemente detetada. 