### Analítico
Temos para um certo braço robotico, em que:
$$\vec{p}=\begin{pmatrix}p_{x} \\ p_{y}\end{pmatrix}=\begin{pmatrix}(a_{1}+a_{2}+d)\cos\theta \\ (a_{1}+a_{2}+d)\sin\theta\end{pmatrix}$$
e temos os jacobiano analitico:
$$J=\begin{pmatrix}\frac{\partial p_{x}}{\partial \theta} & \frac{\partial p_{x}}{\partial d} \\ \frac{\partial p_{y}}{\partial \theta} & \frac{\partial p_{y}}{\partial d}\end{pmatrix}=\begin{pmatrix}-(a_{1}+a_{2}+d)\sin\theta & \cos\theta \\ (a_{1}+a_{2}+d)\cos\theta & \sin\theta\end{pmatrix}$$

### Geométrico (chatGPT)
## Dedução do Jacobiano Geométrico para Arquitetura RPP

### Parâmetros do Braço Robótico

A posição do efetuador final é dada por:

$$
\vec{p} =
\begin{pmatrix}
p_x \\
p_y
\end{pmatrix}
=
\begin{pmatrix}
(a_1 + a_2 + d)\cos\theta \\
(a_1 + a_2 + d)\sin\theta
\end{pmatrix}
$$

Onde:
- $\theta$: ângulo da junta revoluta (junta 1)
- $d$: deslocamento da junta prismática horizontal (junta 2)
- $a_1$, $a_2$: constantes fixas dos segmentos

### Definição do Jacobiano Geométrico

O jacobiano geométrico relaciona as velocidades articulares com a velocidade linear e angular do efetuador final:

$$
\begin{pmatrix}
\vec{v} \\
\vec{\omega}
\end{pmatrix}
=
J_g \cdot
\begin{pmatrix}
\dot{\theta} \\
\dot{d} \\
\dot{d}_z
\end{pmatrix}
$$

### Contribuições por Junta

#### Junta 1 (Revoluta – rotação em torno de $\hat{z}$)

- Eixo: $\vec{z}_0 = \hat{z} = \begin{pmatrix}0 \\ 0 \\ 1\end{pmatrix}$
- Posição do efetuador: $\vec{p}_{xy} = \begin{pmatrix}x \\ y \\ 0\end{pmatrix}$
- Contribuições:
  - Velocidade linear: 
    $$
    \vec{v}_1 = \vec{z}_0 \times \vec{p}_{xy} =
    \begin{pmatrix}
    -y \\
    x \\
    0
    \end{pmatrix}
    $$
  - Velocidade angular: 
    $$
    \vec{\omega}_1 = \vec{z}_0 =
    \begin{pmatrix}
    0 \\
    0 \\
    1
    \end{pmatrix}
    $$

#### Junta 2 (Prismática – direção radial no plano XY)

- Direção: $\vec{r} = \begin{pmatrix}\cos\theta \\ \sin\theta \\ 0\end{pmatrix}$
- Contribuições:
  - Velocidade linear:
    $$
    \vec{v}_2 = \vec{r} = 
    \begin{pmatrix}
    \cos\theta \\
    \sin\theta \\
    0
    \end{pmatrix}
    $$
  - Velocidade angular:
    $$
    \vec{\omega}_2 = \vec{0}
    $$

#### Junta 3 (Prismática – movimento vertical em $\hat{z}$)

- Direção: $\vec{z} = \begin{pmatrix}0 \\ 0 \\ 1\end{pmatrix}$
- Contribuições:
  - Velocidade linear:
    $$
    \vec{v}_3 =
    \begin{pmatrix}
    0 \\
    0 \\
    1
    \end{pmatrix}
    $$
  - Velocidade angular:
    $$
    \vec{\omega}_3 = \vec{0}
    $$

### Jacobiano Geométrico Completo

Agrupando as colunas correspondentes:

$$
J_g =
\begin{pmatrix}
\vec{v}_1 & \vec{v}_2 & \vec{v}_3 \\
\vec{\omega}_1 & \vec{\omega}_2 & \vec{\omega}_3
\end{pmatrix}
=
\begin{pmatrix}
 -y & \cos\theta & 0 \\
 x & \sin\theta & 0 \\
 0 & 0 & 1 \\
 0 & 0 & 0 \\
 0 & 0 & 0 \\
 1 & 0 & 0
\end{pmatrix}
$$

Substituindo $x = (a_1 + a_2 + d)\cos\theta$, $y = (a_1 + a_2 + d)\sin\theta$, temos:

$$
J_g =
\begin{pmatrix}
 -(a_1 + a_2 + d)\sin\theta & \cos\theta & 0 \\
 (a_1 + a_2 + d)\cos\theta & \sin\theta & 0 \\
 0 & 0 & 1 \\
 0 & 0 & 0 \\
 0 & 0 & 0 \\
 1 & 0 & 0
\end{pmatrix}
$$
