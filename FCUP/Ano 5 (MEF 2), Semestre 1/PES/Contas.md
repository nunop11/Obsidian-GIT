## lambda_ee teorico
Temos $y(t)=e(t) - 0.7e(t-1)$ 
A sequência de autocovariância é dada por
$\lambda_{yy}(\tau)=\mathbb{E}[y(t)y(t-\tau)]$ 
temos:
$\lambda_{yy}(0)=\mathbb{E}[y(t)y(t)]=\mathbb{E}[e(t)^{2} - 1.4e(t)e(t-1) + 0.49e(t-1)^{2}]$
e como para ruído branco temos: $\mathbb{E}[e(t)e(t-\tau)]=\begin{cases}\sigma^{2} &, &  \tau=0 \\ 0 &, &  \tau\neq0\end{cases}$

$\lambda_{yy}(0)=1.49\sigma^{2}=5.96$

E temos:
$\lambda_{yy}(1)=\lambda_{yy}(-1)=\mathbb{E}[e(t)e(t-1) - 0.7e(t)e(t-2) - 0.7e(t-1)^{2} + 0.49e(t-1)e(t-2)]$
e fica
$\lambda_{yy}(1)=-0.7\sigma^{2}=-2.8$
