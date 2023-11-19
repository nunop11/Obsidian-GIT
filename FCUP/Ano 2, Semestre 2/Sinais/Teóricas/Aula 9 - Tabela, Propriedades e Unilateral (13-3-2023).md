# Tabela de Transformadas de Laplace
![[tabela laplace 1.png]]
![[tabela laplace 2.png]]

# Propriedades
### Propriedades da RC
- Ver aula anterior

## Propriedades das Transformadas
### Linearidade
- Temos uma função $x_{1}(t)$ cuja transformada é $X_{1}(s)$ e $x_{2}(t)$ cuja transformada é $X_{2}(t)$. Assim, temos
$$L[ax_{1}(t)+bx_{2}(t)]=aX_{1}(s)+aX_{2}(s)$$
sendo que a RC da soma $aX_{1}+bX_{2}$ pode ser maior que a de $X_{1},X_{2}$.

### Translação no Tempo
- Tendo o par função-transformada: $x(t)\leftrightarrow X(s)$ com $RC=R$, podemos fazer uma translação no tempo das duas, ficando com:
$$x(t-t_{0})\leftrightarrow e^{-st_{0}} X(s)~~~~com~~~~RC=R~~~~ (\textsf{Rc fica igual})$$

### Translação no Domínio da Transformada
- Novamente, tendo o par função-transformada: $x(t)\leftrightarrow X(s)$ com $RC=R$, podemos fazer uma translação no domínio da transformada, ficando com:
$$ e^{s_{0}t} x(t)\leftrightarrow X(s-s_{0})$$
 sendo que agora a RC é *transladada* um fator $\text{Re}[s_{0}]$.

### Mudança de Escala
- Novamente, tendo o par função-transformada: $x(t)\leftrightarrow X(s)$ com $RC=R$, podemos mudar a escala. Por exemplo:
$$x(at)\leftrightarrow \frac{1}{|a|}X \left( \frac{s}{a} \right)$$
em que a RC varia conforme $a$. Se originalmente RC era $r_{1}\le \text{Re}[s]\le r_{2}$ agora será $\frac{r_{1}}{a}\le \text{Re}[s]\le \frac{r_{2}}{a}$.

### Diferenciação no tempo (derivar x)
- Novamente, tendo o par função-transformada: $x(t)\leftrightarrow X(s)$ com $RC=R$, podemos derivar $x(t)$ no tempo, ficando com:
$$\frac{d}{dt}x(t)=sX(s)$$
em que a $RC$ da deriva contém a RC original, $R$. Poderá ser maior se houver um polo em $s=0$.
- Esta propriedade permite transformar equações diferenciais em equações algébricas !!

### Diferenciação no domínio da tranformada (derivar X)
- Novamente, tendo o par função-transformada: $x(t)\leftrightarrow X(s)$ com $RC=R$, podemos derivar $X(s)$ em $s$. Ficamos com:
$$\frac{d}{ds}X(s)=-tx(t)$$
sendo que contínuamos a ter $RC=R$.
- Temos $e^{-\alpha t}u(t)\to \frac{1}{s+\alpha}$ na tabela. Se derivarmos $X(s)$ ficamos com $-te^{-\alpha t}u(t)\to \frac{-1}{(s+\alpha)^{2}}$. Se repetirmos isto $n$ vezes ficamos com outra entrada da tabela: $\frac{t^{n-1}}{(n-1)!}e^{-\alpha t}u(t)\to \frac{1}{(s+\alpha)^{n}}$

### Integração no tempo (integrar x)
- Novamente, tendo o par função-transformada: $x(t)\leftrightarrow X(s)$ com $RC=R$, podemos integrar $x(t)$ no tempo ficando com:
$$\int_{-\infty}^{\tau}x(\tau)d \tau\leftrightarrow \frac{1}{s}X(s)$$
em que a RC da integral contém $R\cap[\text{Re}[s]>0]$

# Transformada de Laplace Unilateral
- Esta variante da transformada bilateral (que vimos antes) é definida como $$X_{U}(s)=\int_{0}^{\infty}x(t)e^{-st}dt=L_{U}[x(t)]$$
- Basicamente apenas estamos a fazer a integral para $t$ positivos, o que frequentemente é útil, em *sinais causais*.
- Desta forma, apenas para um sinal causal as transformadas bilateral e unilateral são iguais.
- A RC é **sempre** a região à direita do polo com maior parte real (não módulo). Desta forma, a Transformada unilateral pode ser definida *apenas pela expressão algébrica*, ou seja, a RC não importa.

## Propriedades
- São basicamente as mesmas. 
- Vejamos as formas, associadas a um tempo inicial $t=t_{0}=0$
### Derivação
$$x(t)\to X(s)\Longrightarrow \frac{d^{n}}{dt^{n}}x(t)\to s^{n}X_{U}(s)-s^{n-1}x(0)-s^{n-2} \frac{d}{dt}x(0)-\cdots \frac{-d^{n-1}}{dt^{n-1}} x(0)$$

### Integração
$$x(t)\to X_{U}(s) \Longrightarrow \int_{0}^{\tau}x(\tau)d \tau\to \frac{1}{s}X_{U}(s)+ \frac{1}{s}\int_{-\infty}^{0}x(\tau)d \tau $$

## Teorema do Valor Inicial
- Se $x(t)$ não tiver singularidades ou impulsos em $t=0$, o seu limite á direita é:
$$x(0^{+})=\lim_{s\to \infty}sX_{U}(s)$$
EX: $x(t)=u(t)\Longrightarrow x(0^{+})=u(0^{+})=\lim_{s\to \infty}\left( s \cdot \frac{1}{s} \right)=1$, o que é verdade para a função degrau.

## Teorema do Valor Final
- Se o limite $\lim_{to\to \infty}x(t)$ existir, então:
$$\lim_{to\to \infty}x(t)=\lim_{s\to0}sX_{U}(s)$$
#sinais #fisica
