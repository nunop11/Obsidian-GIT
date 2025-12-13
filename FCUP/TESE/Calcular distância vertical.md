![[dist_vertical_reta_tese]]
- Na iteração anterior fizemos uma reta de start0 até k-1. Temos então a reta definida pela vetor:
$$\vec{v}=P_{k-1}-P_{0}= \begin{pmatrix}x_{k-1}-x_{0} & y_{k-1} -y_{0}\end{pmatrix}$$
e temos:
$$\vec{w} = P_{k}-P_{0}=\begin{pmatrix}x_{k}-x_{0} & y_{k}-y_{0}\end{pmatrix}$$
- Sendo $d$ a distância entre start0 e k, temos a distância ao longo da reta:
$$d_{L}=d \times \cos(\theta) ~~,~~ \cos\theta=\frac{\vec{v}\cdot \vec{w}}{\|\vec{v}\|\|\vec{w}\|}$$
e como temos $d=\|\vec{w}\|$ temos
$$d_{L}=\frac{\vec{v}\cdot\vec{w}}{\|\vec{v}\|}$$
e temos a distância na vertical com teorema de pitágoras:
$$\begin{align*}
d_{V}&= \sqrt{\|w\|^{2} - d_{L}^{2}}= \sqrt{\frac{\|\vec{w}\|^{2}\|\vec{v}\|^{2} - (\vec{v}\cdot\vec{w})^{2}}{\|\vec{v}\|^{2}}}\\
&= \sqrt{\frac{(v_{1}^{2}+v_{2}^{2})(w_{1}^{2}+w_{2}^{2}) - (v_{1}w_{1}+v_{2}w_{2})^{2}}{\|\vec{v}\|^{2}}}\\
&= \sqrt{\frac{v_{1}^{2}w_{1}^{2}+v_{1}^{2}w_{2}^{2}+v_{2}^{2}w_{1}^{2}+v_{2}^{2}w_{2}^{2} -v_{1}^{2}w_{1}^{2}+2v_{1}w_{1}v_{2}w_{2}+v_{2}^{2}w_{2}^{2}}{\|\vec{v}\|^{2}}}\\
&= \sqrt{\frac{v_{1}^{2}w_{2}^{2}+v_{2}^{2}w_{1}^{2} +2v_{1}w_{1}v_{2}w_{2}}{\|\vec{v}\|^{2}}}\\
&= \sqrt{\frac{(v_{1}w_{2} + v_{2}w_{1})^{2}}{\|\vec{v}\|^{2}}}\\
&= \frac{v_{1}w_{2}+v_{2}w_{1}}{\|\vec{v}^{2}\|}=\frac{v_{1}w_{2}+v_{2}w_{1}}{\sqrt{v_{1}^2+v_{2}^{2}}}
\end{align*}$$
