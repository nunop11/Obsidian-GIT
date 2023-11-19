![[descontinuidade sup.png]]
- Consideremos o plano carregado com densidade de carga $\sigma$. Consideremos o lado acima do plano como $+$ e o lado abaixo como $-$. Ou seja: $\hat{n}_{+}=- \hat{n}_{-}$
- Pelo teorema do divergente temos:
$$\oint \vec{E}\cdot d \vec{s}=\int \nabla \cdot \vec{E} d^{3}r=\int \frac{\rho}{\varepsilon_{0}} d^{3}r=\frac{\sigma A}{\varepsilon_{0}}$$
e, por outro lado:
$$\oint \vec{E}\cdot d \vec{s}=\vec{E}^{+}\cdot \hat{n}_{+}A + \vec{E}^{-} \cdot \hat{n}_{-}A=A(E_{\perp}^{+}-E_{\perp}^{-})$$
igualando as 2 equações obtidas tem-se:
$$E_{\perp}^{+}-E_{\perp}^{-}= \frac{\sigma}{\varepsilon_{0}}$$
Ou seja, existe uma **descontinuidade do campo elétrico** em superfícies carregadas.

![[descontinuidade sup tangencial.png]]
- Tendo em área acima temos que, segundo o teorema de Stokes:
$$\oint \vec{E}\cdot d \vec{r}=\int (\nabla \times \vec{E}) \cdot d \vec{s}=0$$
Podemos expandir o integral de linha:
$$\oint \vec{E}\cdot d \vec{r}= (E_{\parallel}^{+}\hat{x})\cdot(\ell \hat{x})- (E_{\parallel}^{-}\hat{x})\cdot(\ell \hat{x})= \ell(E_{\parallel}^{+}- E_{\parallel}^{-})=0$$
o que implica que:
$$E_{\parallel}^{+}=E_{\parallel}^{-}$$

- Das 2 equações que obtivemos acima (para as componentes paralelas e perpendiculares do campo) resulta:
$$\vec{E}^{+}- \vec{E}^{-} = \frac{\sigma}{\varepsilon_{0}} \hat{n}_{+}$$
- Por outro lado, o potencial é sempre contínuo.
