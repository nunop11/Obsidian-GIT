# 5 - Matriz inversa
- Uma forma bastante direta de resolver um sistema $Ax=v$ é multiplicar os 2 lados da equação pela _inversa de A_:
$$Ax=v \Longrightarrow A^{-1}Ax = A^{-1}v \Longrightarrow x=A^{-1}v$$
- No entanto, isto não é mutio eficiente.

- E, tal como já vimos antes, fazer as coisas da forma que faríamos em álgebra está longe do mais adequado a fazer com programação.
- Assim, começamos por consderar um sistema $$AX=V$$
mas em que agora temos que $X,V$ são matrizes $N \times N$.
- Para fazer isto, podemos usar eleminação gaussiana ou LU como vimos antes. Aqui, cada coluna de $X$ será a solução correspondente a uma coluna de $V$ 
- Consideremos agora que $V=I$, sendo $I$ uma _**matriz identidade**_. Assim, por definição:
$$AX=I \Longrightarrow X=A^{-1}$$
- Na prática, fazemos a eliminanação gaussiana como até agora, mas nas partes aplicavamos as mesmas alterações à matriz $v$ faze-mo-lo à matriz $I$:
![[codigo mat inversa.png]]

- Podemos ainda usar :
```
import numpy as np
(...)
X = np.linal.inv(A)
```

#computacional #programacao #matrizes 
