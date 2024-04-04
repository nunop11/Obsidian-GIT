#  Calor
- Podemos escrever a energia calorífica de um corpo como $Q=cmu$ com $c$ um calor específico, $u$ a temperatura e $m$ a massa.
- O calor específico tem unidades $[c]=L^{2}T^{-2}\Theta^{-1}$

## Lei de Fourier
- Temos
------------- notebook ----------

- Se considerarmos uma barra de secção transversal $A$. Apenas as extremidades podem estar expostas ao ambiente. Tendo uma tira infinitesimal entre $x$ e $x+dx$. O calor aí será:
$$q=c \times \rho A\Delta x \times u(x,t)$$
- Ora, por conservação de energia, o calor que entra à esquerda é igual àquele que entra à direita + aquele  que é emitido.
- Pela Lei de Fourier, temos
$$q_{x}=\frac{\partial q}{\partial x}=- k \frac{\partial u}{\partial x}$$
------- notebook ------

### Adimensionalizar
- As variáveis que entram nesta EDDP tem diferentes dimensões. Assim definimos tempo, distância e temperatura caraterísticos $\overline{L},\overline{T},\overline{\Theta}$:
![[adimensionalização.png]]
    - Se para uma barra como vista acima de comprimento $\ell$, devemos definir $\overline{L}=\ell$ e ficamos com $\hat{x}$ entre 0 e 1.

