## PCA
Podemos calcular o centroide dos pontos da reta: $(\overline{x},\overline{y})$
A matriz de covariância dos pontos da reta é dada por:
$$\text{cov}(x,y)=\begin{pmatrix}S_{xx} & S_{xy} \\ S_{xy} & S_{yy}\end{pmatrix}$$
em que:
$$\begin{align*}
S_{xx}&= \sum\limits(x-\overline{x})^{2}\\
S_{yy}&= \sum\limits(y-\overline{y})^{2}\\
S_{xy}&= \sum\limits(x-\overline{x})(y-\overline{y})
\end{align*}$$
Como sabemos, o vetor próprio de $\text{cov}(x,y)$ com maior valor próprio define a *direção da reta*. O vetor com menor valor é **perpendicular** à reta. Isto consiste numa versão simplificada de PCA!!!

#### Vetores e Valores próprios
Podemos definir
$$\begin{align*}
\det(COV-\lambda I)&= 0\\
\begin{vmatrix}S_{xx}-\lambda & S_{xy} \\ S_{xy} & S_{yy}-\lambda\end{vmatrix}&= 0\\
S_{xx}S_{yy} -S_{xx}\lambda-S_{yy}\lambda+\lambda^{2}-S_{xy}^{2}&= 0\\
\lambda_{\pm}= \frac{S_{xx}+S_{yy} \pm \sqrt{S_{xx}^{2}+S_{yy}^{2}+2S_{xx}S_{yy}+4S_{xy}^{2}-4S_{xx}S_{yy}}}{2}&\\
\lambda_{\pm} = \frac{S_{xx}+S_{yy} \pm \sqrt{(S_{xx}-S_{yy})^{2}+4S_{xy}^{2}}}{2}
\end{align*}$$

Temos, para um certo vetor próprio:
$$A\vec{u}_{i} = \lambda_{i}\vec{u}_{i}$$
Logo temos:
$$\begin{align*}
\begin{pmatrix}S_{xx}u_{1}+S_{xy}u_{2}\\
S_{xy}u_{1}+S_{yy}u_{2}\end{pmatrix} = \begin{pmatrix}\lambda u_{1}\\
\lambda u_{2}\end{pmatrix}
\end{align*}~\to~\begin{cases}
u_{1}=\frac{S_{xy}}{\lambda-S_{xx}}u_{2} \\
u_{2}=\frac{S_{xy}}{\lambda-S_{yy}}u_{1}\end{cases}$$
Escolhemos então os vetores próprios:
$$\vec{u}_{-}= \begin{pmatrix}S_{xy} \\ \lambda_{-}-S_{xx}\end{pmatrix} ~~,~~\vec{u}_{+}=\begin{pmatrix}\lambda_{+}-S_{yy} \\ S_{xy}\end{pmatrix}$$
Notemos, claro, que se tivermos $S_{xy}\sim0$ temos $\lambda_{-}=S_{yy}~,~\lambda_{+}=S_{xx}$ logo fica
$$\vec{u}_{-}^{S_{xy}=0}=\begin{pmatrix}0 \\ S_{yy}-S_{xx}\end{pmatrix}=\begin{pmatrix}0 \\ 1\end{pmatrix}~,~\vec{u}_{+}^{S_{xy}=0}=\begin{pmatrix}S_{xx}-S_{yy} \\ 0\end{pmatrix}=\begin{pmatrix}1 \\ 0\end{pmatrix}$$
#### Retas
Tendo o vetor próprio que nos dá a direção perpendicular à reta ($\vec{u}_{-}$) podemos determinar a equação da reta assim:
$$ax+by+c=0~~\to~~ u_{1}^{-}x+u_{2}^{-}+c=0$$
e obtemos
$$c=- u_{1}^{-}\overline{x} - u_{2}^{-} \overline{y}$$
## Hu
Para um set de pontos em 2D temos:
$$M_{ij} = \sum_x\sum_y x^i y^j$$
e teremos
- $M_{00}$ representa uma espécie de área do conjunto de pontos
- $M_{01}, M_{10}$ são a soma dos componentes x,y
- $M_{02}, M_{20}$ medem as variâncias em x e y
- $M_{11}$ mede uma espécie de variância cruzada

### Momentos
Usando estes $M_{ij}$ podemos definir uma série de **momentos**:
$$\mu_{ij}=\sum\limits_{x}\sum\limits_{y}(x-\overline{x})^{i}(y-\overline{y})^{j}$$
Temos então:
$$\begin{align*}
\mu_{00}&= M_{00}\\
\mu_{01}&= 0\\
\mu_{10}&= 0\\
\mu_{11}&= M_{11}-\overline{x}M_{01}=M_{11}-\overline{y}M_{10}\\
\mu_{02}&= M_{02}-\overline{y}M_{01}\\
\mu_{20}&= M_{20}-\overline{x}M_{10}
\end{align*}$$
E podemos normalizar qualqer momento: $\mu_{ij}'=\frac{\mu_{ij}}{\mu_{00}}$

Tendo estes momentos definimos a matriz de covariância da imagem 2D:
$$\text{cov} = \begin{pmatrix}\mu_{20}' & \mu_{11}' \\ \mu_{11}' & \mu_{02}'\end{pmatrix}$$

### Relacionar com PCA2D
Acima definimos:
$$\begin{align*}
\overline{x}=\frac{1}{N}\sum\limits_{i}^{N}x_{i} \quad \quad &; \quad \quad \overline{y}=\frac{1}{N}\sum\limits_{i}^{N}y_{i}\\
S_{xx}=\frac{1}{N-1}\sum\limits_{i}(x_{i}-\overline{x})^{2} \quad \quad&; \quad \quad S_{yy}=\frac{1}{N-1}\sum\limits_{i}^{N}(y_{i}-\overline{y})^{2}\\
S_{xy}= \frac{1}{N-1}&\sum\limits_{i}^{N}(x_{i}-\overline{x})(y_{i}-\overline{y})
\end{align*}$$
Podemos escrever:
$$\begin{align*}
\longrightarrow M_{00}&= \sum x^{0}y^0=N\\
\longrightarrow M_{10}&= \sum x^{1}y^{0}=\Sigma x=N \overline{x}\\
\longrightarrow M_{01}&= \sum x^{0}y^{1}=N \overline{y}\\
\\
S_{xy}&= \tfrac{1}{N-1}\sum (x-\overline{x})(y-\overline{y})\\
S_{xy}&= \tfrac{1}{N-1}\sum (xy - x\overline{y} - y\overline{x} + \overline{x}\overline{y})\\
S_{xy}&= \tfrac{1}{N-1}[\Sigma xy - \overline{y}\Sigma x - \overline{x} \Sigma y+\overline{x}\overline{y}\Sigma1]\\
S_{xy}&= \tfrac{1}{N-1}[M_{11}-N\overline{x}\overline{y}-N\overline{x}\overline{y}+N\overline{x}\overline{y}]\\
\\
\longrightarrow M_{11}&= (N-1)S_{xy}+N\overline{x}\overline{y}\\
\\
S_{xx}&= \tfrac{1}{N-1}\sum (x-\overline{x})^{2}=\tfrac{1}{N-1}\sum(x^{2}-2x\overline{x} + \overline{x}^{2})\\
S_{xx}&= \tfrac{1}{N-1}[\Sigma x^{2} - 2\overline{x}\Sigma x + \overline{x}^{2}\Sigma1]\\
S_{xx}&= \tfrac{1}{N-1}[M_{20} - 2N\overline{x}^{2}+N \overline{x}^{2}]\\
\\
\longrightarrow M_{20}&= (N-1)S_{xx}+N\overline{x}^{2}\\
\longrightarrow M_{02}&= (N-1)S_{yy}+N\overline{y}^{2}
\end{align*}$$

#### Momentos com PCA
- Comecemos com $\mu_{20}$:
$$\begin{align*}
\mu_{20}&= M_{20}-\overline{x}M_{10}\\
&= (N-1)S_{xx}+N\overline{x}^{2}-\overline{x}(N\overline{x})\\
&= (N-1)S_{xx}
\end{align*}$$
- Pelo que  temos: $$\mu_{02}=(N-1)S_{yy}$$
- E temos:
$$\begin{align*}
\mu_{11}&= M_{11}-\overline{x}M_{01}\\
&= (N-1)S_{xy}+N\overline{x}\overline{y} - \overline{x}(N\overline{y})\\
&= (N-1)S_{xy}
\end{align*}$$

- Ou seja, são a mesma coisa!!! A única diferença vem de eu ter feito a normalização no PCA com $N-1$, como aparece frequentemente online. Ao normalizar os momentos temos:
$$\mu_{ij}'=\frac{\mu_{ij}}{\mu_{00}}=\frac{N-1}{N}S_{ij}$$
- Claro, isto tudo foi um exercício desnecessário. Bastava olhar para a fórmula de $\mu_{ij}$ :)))

### Ângulo
Como o objetivo destes momentos é determinar a orientação dos dados. Temos:
$$\begin{align*}
\Theta&= \frac{1}{2}\arctan \left(\frac{2\mu_{11}'}{\mu_{20}'-\mu_{02}'} \right)=\frac{1}{2}\arctan\left(\frac{2 \tfrac{N-1}{N}S_{xy}}{\tfrac{N-1}{N}S_{xx}-\tfrac{N-1}{N}S_{yy}}\right)\\
&= \frac{1}{2}\arctan \left(\frac{2S_{xy}}{S_{xx}-S_{yy}} \right)
\end{align*}$$
E com tanta coisa a normalização nem importa :)

## LSQ
### Dedução
- Temos pontos $x_{i}$ que queremos ajustar a pontos $y_{i}$ tendo-os nos vetores: $$\mathbf{x}=\begin{pmatrix}x_1 \\ x_2 \\ \vdots \\ x_N\end{pmatrix} \quad;\quad Y=\begin{pmatrix}y_{1} \\ y_{2} \\ \vdots \\ y_{N}\end{pmatrix}$$
- Queremos ajustar no modelo $$Y= X\theta =a \mathbf{x}+b$$ logo:
$$X = \begin{pmatrix} & |  & |  & \\  & \mathbf{x} & \mathbb{1}  & \\  & | & |\end{pmatrix} \quad;\quad \theta = \begin{pmatrix} a \\ b \end{pmatrix}$$
- Logo a estimativa LSQ que nos dá os parâmetros de ajuste será:
$$\hat{\theta} = (X^{T}X)^{-1}X^{T}Y$$
e podemos dizer
$$\begin{align*}
\begin{pmatrix}a\\
b\end{pmatrix} &= \left[ \begin{pmatrix}x_{1} & x_{2} & \cdots & x_{N}\\
1 & 1 & \cdots & 1\end{pmatrix} \begin{pmatrix}x_{1} & 1\\
x_{2} & 1\\
\vdots & \vdots\\
x_{N} & 1\end{pmatrix} \right]^{-1} \begin{pmatrix}x_{1} & x_{2} & \cdots & x_{N}\\
1 & 1 & \cdots & 1\end{pmatrix}\begin{pmatrix}y_{1}\\
y_{2}\\
\vdots\\
y_{N}\end{pmatrix}\\
&= \begin{bmatrix} \sum\limits_{i=1}^{N}x_{i}^{2} & \sum\limits_{i=1}^{N}x_{i}\\
\sum\limits_{i=1}^{N}x_{i} & N \end{bmatrix}^{-1}\begin{pmatrix}\sum\limits_{i=1}^{N}x_{i}y_{i}\\
\sum\limits_{i=1}^{N}y_{i}\end{pmatrix}\\
&= \frac{1}{N\sum_{i=1}^{N}x_{i}^{2} - \left(\sum_{i=1}^{N}x_{i}\right)^{2}} \begin{pmatrix}N & -\sum\limits_{i=1}^{N}x_{i}\\-\sum\limits_{i=1}^{N}x_{i} & \sum\limits_{i=1}^{N}x_{i}^{2}
\end{pmatrix}\begin{pmatrix}\sum\limits_{i=1}^{N}x_{i}y_{i}\\
\sum\limits_{i=1}^{N}y_{i}\end{pmatrix}\\
&=  \frac{1}{N\sum_{i=1}^{N}x_{i}^{2} - \left(\sum_{i=1}^{N}x_{i}\right)^{2}} \begin{pmatrix}N\sum\limits_{i=1}^{N}x_{i}y_{i}- \sum\limits_{i=1}^{N}x_{i}\sum\limits_{i=1}^{N}y_{i}\\
\sum\limits_{i=1}^{N}x_{i}^{2}\sum\limits_{i=1}^{N}y_{i}-\sum\limits_{i=1}^{N}x_{i}\sum\limits_{i=1}^{N}x_{i}y_{i}
\end{pmatrix}
\end{align*}$$
- E aproveitemos que para aplicar este método calculamos antes:
$$S_{xx}=\frac{1}{N}\sum\limits_{i=1}^{N}(x_{i}-\overline{x})^{2} \quad;\quad S_{yy}=\frac{1}{N}\sum\limits_{i=1}^{N}(y_{i}-\overline{y})^{2} \quad;\quad S_{xy}=\frac{1}{N}\sum\limits_{i=1}^{N}(x_{i}-\overline{x})(y_{i}-\overline{y})$$
logo
$$\begin{align*}
NS_{xx}&= \sum\limits_{i=1}^{N}x_{i}^{2}-2x_{i}\overline{x}+\overline{x}^{2}\\
NS_{xx}-N\overline{x}^{2}&= \sum\limits_{i=1}^{N}x_{i}^{2}-2\overline{x}\sum\limits_{i=1}^{N}x_{i}\\
\sum\limits_{i=1}^{N}x_{i}^{2}&= NS_{xx}-N \overline{x}^{2}+2N \overline{x}^{2}\\
\sum\limits_{i=1}^{N}x_{i}^{2}&=N(S_{xx}+\overline{x}^{2})\\
---\\
\sum\limits_{i=1}^{N}y_{i}^{2}&= N(S_{yy}+\overline{y}^{2})\\
---\\
NS_{xy}&= \sum\limits_{i=1}^{N}(x_{i}-\overline{x})(y_{i}-\overline{y})\\
NS_{xy}&= \sum\limits_{i=1}^{N}x_{i}y_{i}-x_{i}\overline{y}-y_{i}\overline{x}+\overline{x}\overline{y}\\
NS_{xy}-N\overline{x}\overline{y}&= \sum\limits_{i=1}^{N}x_{i}y_{i}-N\overline{x}\overline{y}-N\overline{x}\overline{y}\\
\sum\limits_{i=1}^{N}x_{i}y_{i}&= N(S_{xy}+\overline{x}\overline{y})
\end{align*}$$
- E temos:
$$\begin{align*}
\begin{pmatrix}a\\
b\end{pmatrix}&= \frac{1}{N^{2}(S_{xx}+\overline{x}^{2}) - N^{2} \overline{x}^{2}}\begin{pmatrix}N^{2}(S_{xy}+\overline{x}\overline{y})-N^{2}\overline{x}\overline{y} \\
N^{2}\overline{y}(S_{xx}+\overline{x}) - N^{2}\overline{x}(S_{xy}+\overline{x}\overline{y})\end{pmatrix}\\
&= \frac{1}{S_{xx}}\begin{pmatrix}S_{xy}\\
\overline{y}S_{xx}+\overline{x}\overline{y}-\overline{x}S_{yy}-\overline{x}^{2}\overline{y}\end{pmatrix}
\end{align*}$$

### Eixos invertidos
- Neste caso temos $$Y=\begin{pmatrix} & | & | &  \\  & \mathbf{y} & \mathbb{1} &  \\  & | & | & \end{pmatrix} \quad;\quad X = \begin{pmatrix}x_{1} \\ x_{2} \\ \vdots \\ x_{N}\end{pmatrix} \quad;\quad \theta=\begin{pmatrix}a \\ b\end{pmatrix} \quad\to\quad X = Y\theta=a \mathbf{y}+b$$
- E temos:
$$\begin{align*}
\begin{pmatrix}a\\
b\end{pmatrix} &= (Y^{T}Y)^{-1}Y^{T}X\\
&= \left[\begin{pmatrix}y_{1} & y_{2} & \cdots & y_{N}\\
1 & 1 & \cdots & 1\end{pmatrix} \begin{pmatrix}y_{1} & 1\\
y_{2} & 1\\
\vdots & \vdots\\
y_{N} & 1\end{pmatrix} \right]^{-1}\begin{pmatrix}y_{1} & y_{2} & \cdots & y_{N}\\
1 & 1 & \cdots & 1\end{pmatrix}\begin{pmatrix}x_{1}\\
x_{2}\\
\vdots\\
x_{N}\end{pmatrix}\\
&= \begin{pmatrix}\sum\limits_{i=1}^{N}y_{i}^{2} & \sum\limits_{i=1}^{N}y_{i}\\
\sum\limits_{i=1}^{N}y_{i} & N\end{pmatrix}^{-1}\begin{pmatrix}\sum\limits_{i=1}^{N}x_{i}y_{i}\\
\sum\limits_{i=1}^{N}x_{i}\end{pmatrix}\\
&= \frac{1}{N\sum_{i=1}^{N}y_{i}^{2}-(\sum_{i=1}^{N}y_{i})^{2}}\begin{pmatrix}N & -\sum\limits_{i=1}^{N}y_{i}\\
-\sum\limits_{i=1}^{N}y_{i} & \sum\limits_{i=1}^{N}y_{i}^{2}\end{pmatrix}\begin{pmatrix}\sum\limits_{i=1}^{N}x_{i}y_{i}\\
\sum\limits_{i=1}^{N}x_{i}\end{pmatrix}\\
&= \frac{1}{N\sum_{i=1}^{N}y_{i}^{2}-(\sum_{i=1}^{N}y_{i})^{2}} \begin{pmatrix}N\sum\limits_{i=1}^{N}x_{i}y_{i} - \sum\limits_{i=1}^{N}y_{i}\sum\limits_{i=1}^{N}x_{i}\\
\sum\limits_{i=1}^{N}y_{i}^{2}\sum\limits_{i=1}^{N}x_{i}-\sum\limits_{i=1}^{N}y_{i}\sum\limits_{i=1}^{N}x_{i}y_{i}\end{pmatrix}\\
&= \frac{1}{N^{2}(S_{yy}+\overline{y}^{2})-N^{2}\overline{y}^{2}}\begin{pmatrix}N^{2}(S_{xy}+\overline{x}\overline{y}) - N^{2}\overline{x}\overline{y}\\
N^{2}(S_{yy}+\overline{y})\overline{x}-N^{2}\overline{y}(S_{xy}+\overline{x}\overline{y})\end{pmatrix}\\
&= \frac{1}{S_{yy}} \begin{pmatrix}S_{xy}\\
\overline{x}S_{yy}+\overline{x}\overline{y}-\overline{y}S_{xy}-\overline{x}\overline{y}^{2}\end{pmatrix}
\end{align*}$$

### Conclusão
- Se fizermos um ajuste LSQ normal ($S_{xx}>S_{yy}$) então temos:
$$y=ax+b \quad;\quad \begin{pmatrix}a \\ b\end{pmatrix}=\frac{1}{S_{xx}}\begin{pmatrix}S_{xy}\\
\overline{y}S_{xx}+\overline{x}\overline{y}-\overline{x}S_{yy}-\overline{x}^{2}\overline{y}\end{pmatrix}$$
- Se fizermos um ajuste LSQ invertido ($S_{xx}<S_{yy}$) então temos:
$$x=ay+b \quad;\quad \begin{pmatrix}a \\ b\end{pmatrix}=\frac{1}{S_{yy}} \begin{pmatrix}S_{xy}\\
\overline{x}S_{yy}+\overline{x}\overline{y}-\overline{y}S_{xy}-\overline{x}\overline{y}^{2}\end{pmatrix}$$
- Mas não é necessário calcular $b$. Como sabemos que $(\overline x, \overline y)$ pertence à reta podemos definir:

$$b = \overline y - a \overline x$$

ou $$b = \overline x - a\overline y$$