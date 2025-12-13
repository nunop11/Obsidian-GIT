## PCA

## Hu

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