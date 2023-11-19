# 5 - EDOs de Ordem Superior
**2ª Ordem**
- Até agora vimos apenas equações diferenciais de 1ª ordem, que são as menos comuns na física. 
- Estas equações são do tipo:
$$\frac{d^{2}x}{dt^{2}}= f \left( x, \frac{dx}{dt}, t \right)$$
apenas fazemos $y= \frac{dx}{dt}$ e ficamos com: $\frac{dy}{dt}=f(x,y,t)$
- Ora, isto não passa de 2 equações de 1ª ordem simultaneas, tal como vimos na secção anterior.

**3ª Ordem**
- E por aí adiante. Uma Eq Dif de 3ª ordem seria do tipo:
$$\frac{d^{3}x}{dt^{3}}=f \left( x, \frac{dx}{dt}, \frac{d^{2}x}{dt^{2}}, t \right)$$
pelo que simplesmente fazemos $\frac{dx}{dt}=y$ e $\frac{dy}{dt}=z$. E temos $\frac{dz}{dt}=f(x,y,z,t)$.

**2 Variáveis de 2ª Ordem**
$$\frac{d^{2}\mathbf{r}}{dt^{2}}=\mathbf{f} \left( \mathbf{r}, \tfrac{d\mathbf{r}}{dt}, t \right)$$
e fazemos $$\frac{d\mathbf{r}}{dt}=\mathbf{s} \quad \quad;\quad \quad \frac{d\mathbf{s}}{dt}= \mathbf{f}(\mathbf{r}, \mathbf{s}, t)$$
- Sendo que se tivéssemos começado com 2 equações diferenciais, acabaríamos com 4 equações.

#computacional #programacao #eqs_difs 