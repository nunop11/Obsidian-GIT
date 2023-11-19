## Formas
- Os números complexos podem ser representados de várias formas:
### $i$ - Forma Algébrica
![[forma algebrica.png|400]]
$$z=x+iy \quad \quad,\quad x,y\in\mathbb{R}$$
sendo $i^{2}=-1$
- Podemos ainda escrever: $z = z' +i z''$
- Torna-se ainda evidente que: $$x=\text{Re}(z) \quad;\quad y=\text{Im}(z)$$

### $ii$ - Forma Polar
![[forma polar.png|400]]
$$z = r e^{i \varphi}$$

### $iii$ - Forma Trigonométrica
$$z=r ~\text{cis} \varphi =r(\cos \varphi + i \sin \varphi)$$
($\text{cis}$ = C-osseno, I, S-eno)

- Aqui torna-se útil recordar as fórmulas abaixo:
$$\cos \theta = \frac{e^{i \theta}+e^{-i \theta}}{2} \quad;\quad \sin \theta = \frac{e^{i \theta}-e^{-i \theta}}{2i} \quad;\quad e^{i \theta}=\cos\theta + i\sin\theta$$
- Ora, ao igualar as formas Algébrica e Trigonométrica obtemos:
$$x=r\cos\varphi \quad;\quad y=r\sin\varphi \quad;\quad r=\sqrt{x^{2}+y^{2}} \quad;\quad \varphi=\arctan\left(\frac{y}{x}\right)$$

## Operações
### $i$ - Divisão nas partes
- Como vimos na parte da Forma Algébrica, $x$ consiste na parte real e $y$ na parte imaginária de $z$. 
- Assim, $x$ e $y$ são, resptivamente, a projeção de $z$ nos eixos real e imaginário.

### $ii$ - Conjugado
$$z=x+iy=r e^{i\varphi} \quad \Rightarrow \quad z^{*} =x - iy = r e^{-i\varphi}$$
### $iii$ - Módulo e Argumento
- Basicamente:
$$\textsf{Módulo}: \quad \quad |z|=\sqrt{x^{2}+y^{2}}=r$$
$$\textsf{Argumento}: \quad \quad \arg(z)=\varphi=\arctan\left(\frac{y}{x}\right)$$
### $iv$ - Soma de 2 complexos
![[soma complexos.png|400]]
- Basicamente a soma de 2 vetores
$$z=z'+iz'' \quad ;\quad w =w'+iw''$$
e temos:
$$z+w= (z'+w') + i(z''+w'')$$
- Para isto devemos usar a forma algébrica.

### $v$ - Potência de Complexos
- Para isto temos que usar a forma polar.
$$z^{2}=\left(r e^{i \varphi} \right)^{2}=r^{2} e^{2i\varphi}$$
Geometricamente, temos então 3 casos:
![[potencia de 1 complexo.png|700]]

Por outro lado, se fizermos: $$z^{u} \quad, \quad u\in\mathbb{R}^{+}$$
observa-se algo assim:
![[potencia de N complexos.png|700]]

### $vi$ - Produto de Complexos
Sendo: $z=r_{z}e^{i \varphi_{z}}$ e $w =r_{w} e^{i \varphi_{w}}$ temos:
$$z \cdot w = r_{z}r_{w} e^{i(\varphi_{z}+\varphi_{w})}$$

## Série Geométrica com Razão Complexa
- Recordemos que uma série geométrica é do tipo: $$a_{n}=a_{0} r^{n} \quad \quad,~~n\in \mathbb{Z}~~,~~r,a_{0}\in\mathbb{R}$$
- Ora, estudemos um caso diferente:
$$u_{n}=z^{n} \quad \quad,~~n\in\mathbb{Z}~~,~~z\in\mathbb{C}$$
- Notemos que esta série não é convergente na maioria dos casos. Mesmo quando temos $|z|>1$ e ficamos com $|z^{n}|\to\infty$ ao longo da série, não estamos a convergir porque o vetor "vai rodando". Mesmo quando temos $|z|<1$ e ficamos com $|z^{n}|\to0$ com $n\to\infty$, não convergemos porque o vetor nunca aponta para a origem.
- Por outro lado, a soma dos termos da série, $S_{n}$, pode convergir. Recordemos a soma infinita:
$$S_{\infty}=\sum\limits_{n=0}^{\infty}z^{n}=\lim\limits_{n\to\infty}S_{n} ~~~~ \left( S_{n}=\sum\limits_{m=0}^{n}z^{m}\right)$$assim, há 1 caso em que a soma infinita converge: $|z|<1$
$$|z|<1 \quad \Longrightarrow \quad S_{\infty}=\frac{1}{1-z} \quad;\quad \left| S_{n}- \frac{1}{1-z} \right|\to 0$$

## Série e Tranformada de Fourier
**Séries**
- Comecemos por ver as diferentes formas de séries de Fourier:
$$\begin{align*}
f(t)&= \sum\limits_{n=0}^{\infty} s_{n}\sin(\omega_{n}t+\varphi_{n})\\
&= \sum\limits_{n=0}^{\infty} c_{n}\cos(\omega_{n}t+\varphi_{n}) \\
&= \sum\limits_{n=0}^{\infty} [a_{n}\cos(\omega_{n}t) + b_{n}\sin(\omega_{n}t)]\\
&= \sum\limits_{n=0}^{\infty} z_{n} e^{i\omega_{n}t} 
\end{align*}$$
De notar aqui que todas elas têm 2 graus de liberdade e que a diferença entre a 1a e 2a é que os termos $s_{n},c_{n}$, assim como a fase, irão diferir bastante.

**Transformada**
$$f(t)=\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty} f(\omega) e^{-i \omega t}d \omega$$
e temos ainda a transformada inversa:
$$f(\omega)=\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty} f(t) e^{i\omega t} dt$$
- De notar que os termos de normalização ($1/\sqrt{2\pi}$) diferem de autor para autor. Em OF iremos usar este valor. Outros autores usam $1/2\pi$ numa das transformadas e $1$ na outra.
