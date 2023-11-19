# Eletro 1 - Aula teórica 3 (JAM)
- Não devemos de decorar leis físicas como fórmulas. Por exemplo, a 2ª Lei de Newton não é "F igual a ma", mas sim "a aceleração de um corpo é proporcional à força nela aplicada"
-  Tendo 2 cargas de prova fixas assim:
![[2 cargas]]
> NOTA: Normalmente, quando se fala em "carga de prova" ou até quando simplesmente se diz que se tem uma "carga q", presumimos que esta/s tem/têm sinal positivo
- Como já vimos, o módulo da força entre as cargas é dado por $F=k\frac{q_1q_2}{d^2}$
- Ora, quando temos 2 cargas num referencial queremos ter esta força em função dos vetores posição:
$$F_{ij}=k\frac{q_i\cdot q_j}{\Vert r_j-r_i\Vert^2}$$
    - Sendo que $F_{ij}$ é a força que a carga $q_i$ exerce na carga $q_j$. Assim, $r_{ji}$ é o vetor que representa a posição de $q_j$ em função de $q_i$, sendo que $\vec r_{ji}=\vec r_j-\vec r_i$
- Deste modo,
$$\vec F_{ij}=k\frac{q_i\cdot q_j}{\Vert \vec r_j-\vec r_i\Vert^2}\cdot\frac{\vec r_j-\vec r_i}{\Vert\vec r_j-\vec r_i\Vert}$$
- De notar ainda que $\frac{\vec u}{\Vert u\Vert}$ irá resultar em $\hat u$, o vetor unitário dessa direção.

- Tem-se ainda que 
  $$k=\frac{1}{4\pi\varepsilon_0}$$
  - $\varepsilon_0$ é a *permitividade elétrica no vácuo*, sendo que $\varepsilon_0\mu_0c^2=1$. ($\mu_o$ é a permeabilidade elétrica no vácuo)
  - O valor de $k$ varia conforme o sistema de unidades usado.
  - No SI, $\varepsilon_0=8.85\cdot10^{-12}F/m$, e portanto $k\approx9\cdot10^9~Nm^2c^{-2}$

---
Por exemplo, a atração entre o protão e o eletrão no átomo de hidrogénio é dada por $$F=\frac{e^2}{4\pi\varepsilon_0a_0^2}$$
, sendo que $e$ é normalmente a representação de uma carga unitária (= carga de um eletrão ou protão $=1,6\cdot10^{-19}C$) e $a_0$ é a distância média entre o protão e eletrão do átomo de hidrogénio.
- Além disto, se calcularmos a força gravítica que atrai o eletrão ao protão, veremos que $F_g\ll F_e$, de tal modo que aquilo que mantém os átomos unidos não é a atração gravítica, mas sim elétrica
---

## 3 Cargas
- Imagine-se agora que temos 3 cargas:
![[3 cargas]]
- E imagine-se ainda que queremos saber a força aplicada em $q_j$. De notar que para isto, **ignoramos a interação entre as restantes cargas** (por outras palavras, ignoramos como i afeta k)
- Temos então que $\large F_{r_j}=F_{ji}+F_{jk}$. Esta relação aplicasse para os vetores das forças também.
- Assim, temos o **Princípio da Sobreposição**:
 $$\vec F_j=\sum_{i=1}^N \vec F_{ij}=\sum_{i=1}^N \biggr[k\frac{q_iq_j}{\vert \vec r_j-\vec r_i\vert^2}\cdot\frac{\vec r_j-\vec r_i}{|\vec r_j-\vec r_i|} \biggr]$$


## Ponto de equilíbrio
- Imaginesse agora que temos ums sistema assim:
![[ponto de equilibrio]]
- Facilmente se vê que todas as forças aplicadas na carga $q'$, ao centro, se anulam.
- Assim, esta carga estaria em equilíbrio
- De notar ainda que os 3 vetores $\vec F$ NÃO são iguais, mas sim têm o mesmo módulo.

- Assim, apesar de $\sum \vec F_{q'}=0$, não existe uma posição de equilíbrio estável.
- Isto porque exatamente na posição central há equilíbrio, mas qualquer ligeiro desvio da carga irá retirá-la do equilíbrio.
- Por outras palavras: para que exista uma posição de equilíbrio, é necessário que esta se consiga manter.

- Assim, para que uma certa posição seja de equilíbrio estável, e necessário que:
    - $\sum \vec F=0$
    - $\sum\vec p=0$
    - ==A energia seja mínima==

Assim, o equilíbrio não depende da carga em si, mas sim das cargas que criam a força aplicada nesta carga.
Chega-se assim à definição de CAMPO

#em1 #fisica 