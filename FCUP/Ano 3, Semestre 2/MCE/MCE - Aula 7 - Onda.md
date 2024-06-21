# Equações Hiperbólicas
## Equação de Advecção/Convecção
$$\frac{\partial u}{\partial t}=-v \frac{\partial u}{\partial x}$$
- Esta constitui uma das equações hiperbólcias mais simples.
- Para o caso em 1D temos as condições 
    - Iniciais : $u(x,0)=u_{0}(x)$
    - Fronteira : $u(0,t)=f(t)~~\text{OU}~~u(L,t)=g(t)$ (por ser uma equação de 1 CF)
- A solução será periódica. Ou seja, para saber o erro da solução basta comparar o perfil após 1 período com o perfil inicial
- Podemos dizer isto de outra forma: a solução é constante ao longo das linhas descritas por $x-vt=\text{const}$, chamadas de *linhas caraterísticas* 

- Ou seja, verificar a qualidade das nossas soluções desta equação é simples: evoluímos no domínio temporal e comparamos o perfil após um período com aquele do período anterior. Naturalmente, a diferença entre estes será o *erro*!

### FTCS - Forward in Time, Centered in Space
- Tendo-se $\partial_{t}u=-v\partial_{x}u$, fazemos como o nome indica: derivada temporal é derivada à frente, derivada espacial é derivada ao centro. Obtem-se:
$$u_{i}^{n+1}=u_{i}^{n} - \frac{C}{2}(u_{i+1}^{n}- u_{i-1}^{n})$$
em que $C=v \frac{\Delta t}{\Delta x}$ é o número de Courant-Friedrichs-Lewy (CFL). Notemos que é *adimensional*

- A partir desta formula, em $i=0,i=N_{x}-1$ teríamos de usar pontos que não existem. Ora, devido à periodicidade obrigatória da solução impomos:
    - $i=-1:~~u_{-1}^{n}=u_{N_{x}-1}^{n}$
    - $i=N_{x}:~~ u_{N_{x}}^{n}=u_{0}^{n}=u_{N_{x}}^{n}$
    - Ou seja, temos sempre que o primeiro e último pontos ão iguais.
- Analogamente ao que nos acontecia ao resolver a equação de Calor, o número $C$ influencia muito a convergência e estabilidade do método numérico.
- Este método é bastante instável e tem dificuldade em convergir manter o formato inicial quando a CI é em degrau:
![[fcts função nao suave.png]]
vendo-se um formato que faz lembrar FT

#### Código
É só isto: (VERIFICAR SE FUNCIONA)
```python
def ftcs(u, n): # forward time centered space
    for i in range(n):
        u[1:-1] = u[1:-1] - c/2*(u[2:] - u[:-2])
    return u[1:-1]
```

#### Análise
- Este método dá sempre resultados instáveis para basicamente qualquer CFL, rapidamente se obtendo um gráfico com bastante ruído. 
- Consideremos uma solução do tipo modo de Fourier: $u_{i}^{n}=A^{n}e^{ijk \Delta x}$
- Para haver estabilidade, a *amplitude* não pode crescer:
$$\Biggr|\frac{A^{n+1}}{A^{n}}\Biggr|\le1$$
que no caso das FCTS (faz-se como fiz para FEuler, BEuler e CN) resulta em:
$$\Biggr|\frac{A^{n+1}}{A^{n}}\Biggr|^{2}=1+C^{2}\sin^{2}\theta\ge 1$$
- Pode ainda ser verificado que não há dependência em $n$, logo todos os modos crescem da mesma forma
- Vemos ainda que este método será **instável** para qualquer $C$! Por outras palavras: *FTCS é incondicionalmente estável*!

#### Mas FCTS nem sempre é inútil...
- Ora, o método é péssimo a resolver a equação de Convecção
- Mas na realidade ele resolve com elevada exatidão uma equação de convecção ajustada.
- Podemos escrever a expansão de Taylor:
$$u_{i}^{n+1}=u_{i}^{n}+u_{t}\Delta t + \frac{1}{2} u_{tt}(\Delta t)^{2}+\mathcal{O}(\Delta t^{3})$$
e ainda:
$$u_{i\pm1}^{n} = u_{i}^{n} \pm u_{x} \Delta x + \frac{1}{2} u_{xx}(\Delta x)^{2}+\mathcal{O}(\Delta x^{3})$$
e de alguma forma isto mostra que estamos na realidade a resolver a equação:
$$u_{t}+v u_{x}=- \frac{1}{2} \Delta tv^{2}u_{xx}$$
- Ora, isto consiste na equação de convecção + uma difusão (de sinal negativo: invés de a solução tender a decair, tende a crescer). Como sabemos, isto será sempre pior e mais instável, não sendo uma solução física!
- Daqui notemos que é normal surgirem termos correspondentes a difusões em sistemas de difrenças finitas, mas têm que ter sempre resultados físicos.

#### Melhorar
- Vamos agora tentar melhorar a equação original. Para isso, vamos alterar a forma como discretizamos a equação, de derivadas espaciais centrais (2ª ordem) para derivadas para a frente ou para trás (1ª ordem)

##### Downwind
- A primeira opção é *Downwind*: derivadas para a *frente* $$u_{x}=\frac{u_{i+1}^{n}-u_{i}^{n}}{\Delta x}$$

##### Upwind
- A segunda opção é *upwind*: derivadas para *atrás* $$u_{x}=\frac{u_{i}^{n}-u_{i-1}^{n}}{\Delta x}$$
- O resultado melhora bastante:
![[fcts upwind.png]]

**Análise**
- Fazendo a análise do Upswind com uma solução do tipo 1 modo de Fourier obtemos:
$$ \left|\frac{A^{n+1}}{A^{n}} \right|^2 = 1-2C(1-C)(1-\cos\theta) \le 1 $$
- Temos $(1-\cos\theta) \ge 0$ sempre. Assim, precisamos que $2C(1-C) \ge 0$, logo: $0 \le C \le 1$ é condição para a estabilidade do método _upwind_.
- Como $C= v \Delta t/\Delta x$ quer dizer que a informação não se pode propagar mais que uma célula por passo temporal.
- A análise pelas séries de Taylor leva à conclusão que este método é equivalente à equação:

$$ u_t + vu_x = \frac{1}{2}v \Delta x (1-C) u_{xx} ,$$
ou seja, também temos uma difusão, mas agora ela é física se $1-C > 0$. Também mostra que obtemos a solução exacta se $C=1.$ Este método é portanto bastante melhor que FTCS!

#### Escolha
- Se fizessemos esta análise para o _downwind_, veríamos que ele é incondicionalmente instável! 
- Na realidade a direcção a escolher está relacionada com o sinal da velocidade. Fisicamente, a nossa escolha (_upwind_) diz que usamos a informação que vem do lado do qual sopra o vento.
- Examinar o quociente das partes imaginária e real do modo de Fourier também nos diz se o método introduz atrasos de fase. Nalguns métodos pode ser elevada!

### Outros Métodos
#### Lax-Friedrichs
- Partimosda equação do FTCS $u_{i}^{n+1}=u_{i}^{n} - \frac{C}{2}(u_{i+1}^{n}- u_{i-1}^{n})$ mas substituimos $u_{i}^{n}\to \frac{1}{2}(u_{i-1}^{n}+ u_{i+1}^{n})$ e obtemos:
$$u_{i}^{n+1}=\frac{1}{2}(1+C)u_{i-1}^{n} + \frac{1}{2}(1-C)u_{i+1}^{n}$$
- O método é estável se $C<1$. No entanto, por não conter o ponto que de facto estamos a calcular pode levar a difusão mais rápida, o que não é desejado.

#### Lax-Wendroff
- Fazemos meios passos  (como CN):
$$\begin{align*}
u_{i}^{n+ \frac{1}{2}}&= u_{i}^{n} + \frac{\Delta t}{2} \left(-v \frac{\partial u^{n}}{\partial x}|_{i} \right)\\
u_{i}^{n+1}&= u_{i}^{n} + \frac{\Delta t}{2} \left(-v \frac{\partial u^{n+ \frac{1}{2}}}{\partial x}|_{i} \right) = u_{i}^{n} -v \frac{\Delta t}{\Delta x} \left( u_{i+ \frac{1}{2}}^{n+ \frac{1}{2}} - u_{i- \frac{1}{2}}^{n+ \frac{1}{2}} \right)
\end{align*}$$
(em que usamos derivadas ao centro na parte final)

- Usando Lax-Friedrichs isto somehow dá:
$$ \begin{align*}
u_{i- 1/2}^{n+1/2} &= \frac{1}{2}\left(u_{i}^{n} + u_{i-1}^{n}\right)-\frac{v\Delta t}{2\Delta x} \left(u_{i}^{n} - u_{i-1}^{n}\right)\\
u_{i+ 1/2}^{n+1/2} &= \frac{1}{2}\left(u_{i+1}^{n} + u_{i}^{n}\right) -\frac{v\Delta t}{2\Delta x} \left(u_{i+1}^{n} - u_{i}^{n}\right)\\
u_{i}^{n+1} &= u_{i}^{n} -\frac{v\Delta t}{\Delta x} \left(u_{i+1/2}^{n+1/2} - u_{i-1/2}^{n+1/2}\right)
\end{align*}$$
que somehow pode ser escrito como:
$$u_{i}^{j+1} = b_{-1}u_{i-1}^{j} + b_{0}u_{i}^{j} +b_{1}u_{i+1}^{j},$$
em que
$$ b_{-1} = \frac{C}{2}(C+1) \quad;\quad b_{0}= 1-C^2 \quad;\quad b_{1} = \frac{C}{2}(C-1)$$
- Este método é portanto explícito e de 2ª ordem no tempo e no espaço.

# Equação de Onda
$$\boxed{\frac{\partial^{2}u}{\partial t^{2}}=c^{2}\frac{\partial^{2}u}{\partial x^{2}}}$$
- Esta é a nossa velha conhecida. Permite prever a forma como uma perturbação numa corda evolui no tempo, por exemplo.
- Ora, em OMC ou Ótica usamos esta equação mas fizemos sempre aproximações, do tipo: considerar que a corda é homogénea e linear. Ora, isto pode nem sempre ocorrer. Assim, torna-se útil resolver esta equação de forma numérica.

## Método Explícito (Sem nome?)
- Temos as condições de fronteira:
![[eq onda cf.png]]
- Por termos 2 segundas derivadas, precisamos de 2 *condições* iniciais.
- Conseguimos então obter:
$$\frac{u_{i}^{n+1}-2u_{i}^{n}+u_{i}^{n-1}}{\Delta t^{2}}=c^{2}\frac{u_{i+1}^{n}-2u_{i}^{n}+u_{i-1}^{n}}{\Delta x^{2}}$$
de onde podemos obter:
$$u_{i}^{n+1}=-u_{i}^{n-1}+2u_{i}^{n}+C^{2}(u_{i+1}^{n}-2u_{i}^{n}+u_{i-1}^{n})$$
em que novamente $C=c \frac{\Delta t}{\Delta x}$ é o *número de Courant*, adimensional. Numa meio 1D homogéneo temos $c=\sqrt{T/\rho}$ (tensão e densidade da corda).
- Ora, para obter $u_{i}^{n+1}$ precisamos de $u^{n}$ e $u^{n-1}$. Mas quando começamos o algoritmo isto parece impossível, só temos 1 instante anterior. Na realidade temos a 2ª CI: $u_{t}=0$ (derivada temporal nula). Usando diferenças centrais, esta CI implica:
$$u_{t}=0~~\to~~ \frac{u_{i}^{0}-u_{i}^{-1}}{\Delta t}=0~~\to~~u_{i}^{-1}=u_{i}^{0}$$
- Se substituirmos na equação do método:
$$u_{i}^{1}=u_{i}^{0} + \frac{1}{2}C^{2}(u_{i+1}^{0}-2u_{i}^{0}+u_{i-1}^{0})$$

**Algoritmo**
1. Calcular a CI $u_i^0=I(x_i)$ para $i=0,\ldots,N_x$.
2. Calcular $u^1_i$ conforme a equação acima e aplicando as CF.
3. Para cada iteração temporal, aplicar a equação $u^{n+1}_i$ acima e aplicar CF.

**Código**
Por alguma razão o professor decidiu fazer isto com loops??
```python
# Impôr condição inicial u(x,0) = I(x)
for i in range(0, Nx+1):
    u_1[i] = I(x[i],0)
# Aplicar a fórmula especial no primeiro passo, com du/dt=0 incorporada
for i in range(1, Nx):
    u[i] = u_1[i] + 0.5*C2*(u_1[i+1] - 2*u_1[i] + u_1[i-1])
u[0] = 0;  u[Nx] = 0   # Impôr condições fronteira
# Trocar papel das variáveis antes do próximo passo (presente passa a passado, futuro passa a presente)
u_2[:], u_1[:] = u_1, u
for n in range(1, Nt):
    # Actualizar todos os nodos interiores no instante t[n+1]
    for i in range(1, Nx):
        u[i] = 2*u_1[i] - u_2[i] + C2*(u_1[i+1] - 2*u_1[i] + u_1[i-1])
    # Aplicar condições fronteira
    u[0] = 0;  u[Nx] = 0
    # Trocar papel das variáveis antes do próximo passo
    u_2[:], u_1[:] = u_1, u
```

**Estabilidade**
- À análise que vamos aqui fazer chamamos de Análise de von Neumann.
- Consdieremos uma solução da forma $u(x,t)=A^{n}e^{i\omega x}$. Assumimos que a evolução temporal da amplitude segue a equação:
$$\frac{A(t+\Delta t)}{A(t)}=\frac{A(t)}{A(t-\Delta t)}=\lambda~~\to~~ \begin{cases}
A(t+\Delta t)=\lambda A(t) \\
A(t-\Delta t)= \frac{1}{\lambda}A(t)
\end{cases}$$
- Substituindo isto na equação do método visto acima obtemos:
$$\lambda A(t)e^{i\omega x} = 2(1-C^2)e^{i\omega x}-\frac{A(t)}{\lambda}e^{i\omega x} + C^2A(t)e^{i\omega x} (e^{i\omega \Delta x} + e^{-i\omega \Delta x})$$
de onde obtemos
$$\begin{align*}
\lambda^2-2\left( 1-2C^2\sin^2\left( \frac{\omega \Delta x}{2}\right) \right)\lambda +1&=0\\
\lambda^{2}-2\alpha\lambda+1=0
\end{align*}$$
em que podemos definir:
$$\alpha = 1-2C^{2}\sin^{2}\left(\frac{\omega \Delta x}{2}\right)$$

- As soluções da equação quadrática são:
$$\lambda= \alpha\pm \sqrt{\alpha^{2}-1}=1-C^{2}\pm 2C \sqrt{C^{2}-1}$$
- Daqui temos que o sistema é estável se $C\le1$ (de notar que se $C<1$ temos $\lambda$ complexo com módulo 1). Se  $C>1$ temos um fator de ampliação $\lambda>1$ logo a solução explode.

## Crank-Nicholson (look who's back)
- Tal como fizemos para CN no caso da equação de Calor 1D, deixamos a 2ª derivada temporal igual e fazemos a 2ª derivada espacial consdierando os tempos $t, t+\Delta \frac{t}{2,}t-\Delta t/2$. Para obter os últimos 2 fazemos médias entre $t,t+\Delta t$ e $t-\Delta t,t$. Confia.
- Obtemos:
$$\left.\frac{\partial^2 u}{\partial x^2}\right|_{i,k}=\frac{(u_{i-1}^{k+1}-2u_{i}^{k+1}+u_{i+1}^{k+1})+2(u_{i-1}^{k}-2u_{i}^{k}+u_{i+1}^{k}) + (u_{i-1}^{k-1}-2u_{i}^{k-1}+u_{i+1}^{k-1})}{4\Delta x^2}$$
- Reorganizando isto de modo a ter os pontos do mesmo instante todos do mesmo lado, temos:
$$-u_{i-1}^{k+1} +2\left( 1+\frac{2}{C^2} \right) u_{i}^{k+1} - u_{i+1}^{k+1}=2\left[ u_{i-1}^{k} -2\left( 1-\frac{2}{C^2} \right) u_{i}^{k} + u_{i+1}^{k}\right]+ u_{i-1}^{k-1} -2\left(1+\frac{2}{C^2} \right)u_{i}^{k-1} + u_{i+1}^{k-1}$$

- Isto resulta em:
$$\begin{align*}
&\begin{pmatrix}2+ \frac{4}{C^{2}} & -1  & \cdots  & \cdots & 0 \\ -1 & 2+ \frac{4}{C^{2}} & -1  & \cdots & 0 \\ 0 & -1 & 2+ \frac{4}{C^{2}} & \cdots & 0 \\ \cdots & \cdots & \cdots & \ddots & \vdots \\ 0 & \cdots & 0 & -1 & 2 + \frac{4}{C^{2}}\end{pmatrix}u^{k+1} =  2 \begin{pmatrix}\frac{4}{C^{2}}-2 & 1  & \cdots  & \cdots & 0 \\ 1 & \frac{4}{C^{2}}-2 & 1  & \cdots & 0 \\ 0 & 1 & \frac{4}{C^{2}}-2 & \cdots & 0 \\ \cdots & \cdots & \cdots & \ddots & \vdots \\ 0 & \cdots & 0 & 1 & \frac{4}{C^{2}}-2\end{pmatrix}u^{k} \\\\
&+ \begin{pmatrix}-\frac{4}{C^{2}}-2 & 1  & \cdots  & \cdots & 0 \\ 1 & -\frac{4}{C^{2}}-2 & 1  & \cdots & 0 \\ 0 & 1 & -\frac{4}{C^{2}}-2 & \cdots & 0 \\ \cdots & \cdots & \cdots & \ddots & \vdots \\ 0 & \cdots & 0 & 1 & -\frac{4}{C^{2}}-2\end{pmatrix}u^{k-1}
\end{align*}$$
que podemos escrever na forma
$$A u^{k+1}=2B u^{k} + C u^{k-1}$$
- Temos $u^{1}$ determinado com:
$$-u_{i-1}^{1}+2\left(1+ \frac{2}{C^{2}}\right)u_{i}^{1}-u_{i+1}^{1}= u_{i-1}^{0}+ \left(-2+ \frac{4}{C^{2}}\right)u_{i}^{0}+u_{i+1}^{0} - \Delta t\left[v_{i-1}^{0} + \left(-2- \frac{4}{C^{2}}\right)v_{i}^{0}+v_{i+1}^{0}\right]$$
ou seja:
$$Au^{1}=Bu^{0}-\Delta t C v^{0}$$
(em que $v$ é o vetor de velocidades iniciais)

#### Estabilidade
- Repetindo análise de Neumann (sugerir solução do tipo $u^{n}(x)=A^{n}e^{i\omega x}$ em que presumimos aquelas relações de amplitude com o fator de ampliação) obtemos:
$$
\lambda^2 +2\lambda \left[\frac{1-\frac{2}{C^2}- \cos(\omega \Delta x)}{1+\frac{2}{C^2}- \cos(\omega \Delta x)}\right]+1=0.
$$
em que a solução da equação quadrática é:
$$\lambda = \frac{\left[\sin^{2} \left(\frac{\omega \Delta x}{2}\right)-\frac{1}{C^{2}}\right] \pm i\frac{2}{C^{2}} \sin^{2} \left(\frac{\omega \Delta x}{2}\right) }{\left[\sin \left(\frac{\omega \Delta x}{2}\right)+\frac{1}{C^{2}}\right]}$$
- Teremos $\lambda=1$ para **qualquer** $C$. Ou seja, é **incondicionalmente estável**!

#### Estabilidade com termo fonte
- Consideremos agora que temos um termo de fonte:
$$u^{n+1}_i = -u^{n-1}_i + 2u^n_i +C^2(u^{n}_{i+1}-2u^{n}_{i} + u^{n}_{i-1}) + \Delta t^2 f^n_i$$
- Para estudar a estabilidade do método, uma maneira que temos é  assumir uma solução e andar para trás, de modo a determinar as CIs, CFs e fonte. Por exemplo se considerarmos $u(x,t)=A \sin\left(\frac{\pi}{L}x\right)\cos\left( \frac{\pi}{a}ct\right)$, esta é a solução teórica se $f=0$, CF=0 e CIs: $u(x,0)=A\sin(\frac{\pi}{L}x)~~,~~u_{t}(x,0)=0$ 
- Ora, mesmo que conheçamos a solução analítica, simplesmente *observar* o traçado teórico VS o traçado da solução numérica NÃO é uma forma aceitável de medir erros.

- Assim, corremos o programa com passos temporais cada vez menores e vemos se a taxa de convergência é a esperada de acordo com o erro de truncagem do método.
- Uma solução que satisfaz as CF nulas é $u_{e}(x,t)=x(L-x)\sin t$. Ao colocar isto na PDE obtemos o  termo de fonte: $f=(2c^{2}-x(L-x))\sin t$. Correspondem ainda as CI: $u(x,0)=I(x)=0~,~u_{t}(x,0)=V(x)=x(L-x)$

- Como usamos diferenças centrais nas 2 derivadas, os erros de truncagem das variáveis x,t serão $\Delta x^{2},\Delta t^{2}$. Assim o erro da solução será: $$E=C_{t}\Delta t^{2}+C_{x}\Delta x^{2}$$
- Temos a equação do CFL: $C =c \Delta t/\Delta x$. Considerando um passo $\Delta t=h$, podemos escrever $\Delta x=ch/C$. Assim, podemos estudar o erro em função de $h$! (A equação que os relaciona não importa)
- Podemos definir o erro de uma solução numéria $u_{i}^{n}$ com:
$$E=\|e_{i}^{n}\|=\sqrt{\Delta t \Delta x\sum\limits_{n=0}^{N_{t}}\sum\limits_{i=0}^{N_{x}}(e_{i}^{n})^{2}}$$
em que definimos um "vetor" de erros:
$$e_{i}^{n}=u_{e}(x_{i},t_{n})-e_{i}^{n}$$

- Podemos ir diminuindo o passo: $h_{j}=2^{-j}h_{0}$. Verifica-se que (?):
$$E_{j}=K h_{j}^{r}\quad \quad;\quad \quad E_{j+1}=K h_{j+1}^{r}$$
que nos permite obter a **taxa de convergência**:
$$r = \frac{\ln \frac{E_{j+1}}{E_{j}}}{\ln \frac{h_{j+1}}{h_{j}}}$$

#### Solução de equações discretas
- Como vimos acima, com uma solução proposta ou analítica podemos estimar $r$ e com ele tirar conclusões sobre erros do programa.
- Assim, seria ideal descrobrir uma solução exata de forma numérica. Isto é possível, mas precisamos de conhecer o erro numérico, o que nem sempre é possível.

- No entanto, às vezes podemos determinar uma solução com erro numérico nulo, ou seja, uma solução que é solução da DPE e das equações discretas obtidas da discretização (o sistema de $u_{i}^{n}$ que resolvemos)
- Isto costuma ser possível quandoa solução é *polinomial de baixa ordem*. Isto é porque a truncagem despreza as derivadas de maior ordem, logo para polinómios de maior ordem não podemos garantir correção. Mais concretamente, como consideramos diferenças centrais para fazer as derivadas, logo estamos a desprezar derivadas acima da 4ª. OU SEJA, podemos arranjar uma solução de erro de truncagem nulo se tivermos uma solução polinomial de *grau inferior a QUATRO*!

**EX**
*Solução Exata*
- Consideremos a solução quadrática:
$$u_{e}(x,t)=x(L-x)\left(1+ \frac{1}{2} t\right)$$
- Ao substituir isto na DPE temos que:
    - Implica termo de fonte $f(x,t)=2(1+t)c^{2}$
    - Obedece a CF dirichlet nula
    - Implica CIs: $I(x)=x(L-x)$ e $V(x)=\frac{1}{2}x(L-x)$

*Solução Discreta*
- Vamos basicamente substituir a solução exata na versão discreta.
- Temos a grelha temporal $t_{n}=n\Delta t$. Podemos determinar as segundas derivadas de $t,t^{2}$:
$$\begin{align*}
\frac{d^{2}}{dt^{2}}[(t_{n})^{2}]&= \frac{t_{n+1}^{2}-2t_{n}^{2}+t_{n-1}^{2}}{\Delta t^{2}}=(n+1)^{2}-2n^{2}+(n-1)^{2}=2\\
\frac{d^{2}}{dt^{2}}[t_{n}]&= \frac{t_{n+1}-2t_{n}+t_{n-1}}{\Delta t^{2}}=\frac{((n+1)^{2}-2n^{2}+(n-1)^{2})}{\Delta t}=0
\end{align*}$$
E podemos fazer a 2ª derivada de $u_{e}$:
$$\frac{d^{2}}{dt^{2}}[u_{e}]=x_{i}(L-x_{i}) \frac{d^{2}}{dt^{2}} \left[1+ \frac{1}{2}t_{n} \right]=x_{i}(L-x_{i})\cdot0=0$$

- Se determinarmos $\partial_{x}^{2}[x_{i}],\partial_{x}^{2}[(x_{i})^{2}]$ da mesma forma que acima, temos
$$\frac{d^{2}}{dx^{2}}[u_{e}]=\left(1+ \frac{1}{2}t_{n}\right) \frac{d^{2}}{dx^{2}}[xL-x^{2}]=\cdots=-2(1+ \frac{1}{2}t_{n})$$
- Como vimos, para esta solução exata temos o termo de fonte $f_{i}^{n}=2(1+ \frac{1}{2}t_{n})c^{2}$. Assim, a equação de onda fica:
$$\begin{align*}
\frac{d^{2}}{dt^{2}}u_{e}&= c^{2} \frac{d^{2}}{dx^{2}}u_{e}+f\\
&\downarrow\\
0&= c^{2}\cdot -2\left(1+ \frac{1}{2}t_{n}\right)+2\left(1+ \frac{1}{2}t_{n}\right)c^{2}\\
0&= 0
\end{align*}$$
ou seja: $u_{e}$ é uma solução exata da EDDP _e_ do problema discretizado!!!

- Ou seja, ao resolver este problema poderíamos usar esta equação para verificar os valores calculados numa certa iteração, pelo que os valores numéricos deveriam ser iguais aos de $u_{e}$.
    - Isto funcionaria para qualquer $\Delta x,\Delta t$
    - As condições de estabilidade continuam a aplicar-se!

## Propriedades da Solução da Eq Onda - Fourier
- Devido ao princípio de sobreposição, podemos escrever as soluções da eq onda como:
$$u(x,t)=g_{D}(x-ct) + g_{E}(x+ct)$$
- Se tivermos as CI: $u(x,0)=I(x)$ e $u_{t}(x,0)=0$ temos até
$$u(x,t)=\frac{1}{2}I(x-ct)+ \frac{1}{2}I(x+ct)$$
ou seja, duas ondas iguais, uma a mover para direita e outra para a esquerda.

*Fourier*
- Ondas planas são soluções da eq de onda. Assim, vamos representar $I$ como uma sobreposição de ondas planas:
$$I(x)=\sum\limits_{k\in K}b_{k}e^{ikx}$$
- Claramente, os pesos $b_{k}$ serão as componentes da série de Fourier. Assim, $K$ é o conjunto (finito) de valores da FT.

### Aplicação na Discretização
- Naturalmente a solução discreta equivalente a uma série de Fourier é:
$$u_{q}^{n}=e^{i(kx_{q}-\varpi t_{n})}$$ (a frequência $\varpi$ (isto é um varpi hihi) da solução discreta pode não ser a mesma da frequência da solução exata, $\omega$)

- Podemos determinar as 2ªs derivadas desta solução discreta:
$$\begin{align*}
\frac{d^{2}}{dt^{2}}[e^{i\omega t_{n}}]&= \frac{e^{i\omega t_{n-1}}-2e^{i\omega t_{n}+e^{i\omega t_{n+1}}}}{\Delta t^{2}}\\
&= e^{i\omega \Delta t} \frac{e^{i\omega(n-1)}-2e^{i\omega n}+e^{i\omega(n+1)}}{\Delta x^{2}}\\
&= -4 \sin^{2}\left(\frac{\omega \Delta t}{2}\right)\frac{e^{i\omega n\Delta t}}{\Delta t^{2}}
\end{align*}$$
e de forma análoga para a parte espacial:
$$\frac{d^{2}}{dx^{2}}[e^{ikx_{q}}]=-4 \sin^{2}\left(\frac{\omega \Delta t}{2}\right)\frac{e^{ikq\Delta x}}{\Delta x^{2}}$$
- Ou seja, ao introduzir uma onda $u=e^{i(kx_{q}-\varpi t_{n})}$ no sistema discreto obtemos a **Relação de Dispersão Numérica**:
$$\sin^{2}(\frac{\varpi \Delta t}{2})=C^{2}\sin^{2}\left(\frac{k\Delta x}{2}\right)$$
de onde podemos tirar a *frequência da solução numérica*:
$$\varpi=\frac{2}{\Delta t}\arcsin\left(C\sin\left(\frac{k \Delta x}{2}\right)\right)$$
- A **relação de dispersão analítica** é:
$$\omega=ck$$
- Sendo que no caso em que $C=1$ temos uma coisa particular:
$$\varpi=\frac{2}{\Delta t}\frac{k \Delta x}{2}=\frac{1}{\Delta t}\frac{\omega \Delta x}{c}=\frac{\omega}{C}=\omega$$
e observaremos isto nos gráficos abaixo.
- Daqui resulta que, se $\varpi\neq\omega$, a "onda numérica" se move a uma velocidade $\tilde c=\varpi/k$. Assim, podemos comparar $c,\tilde c$ para estudar a fidelidade do sistema discreto.
- Ora, surge o interesse em comparar $\varpi$ e $\omega$ AKA ver o erro da dispersão numérica. Para isto podemos estudar uma das seguintes relações: $\varpi-\omega,\varpi/\omega,\tilde c-c,\tilde c/c$. A mais simples é $\tilde c/c=r$, a que chamaremos de **rácio de velocidades**. Definimos $p= \frac{1}{2}k\Delta x$ (número de pontos da frelha por comprimento de onda espacial) e temos:
$$r=\frac{\tilde c}{c}=\frac{2}{ck\Delta t}\arcsin(C\sin p)=\frac{1}{Cp}\arcsin(C\sin p)$$
- O comprimento de onda *mínimo* que podemos definir é $\lambda=2\Delta x$ (uma onda tem que no mínimo começar num ponto, passar 1 e acabar no 3º. Menos pontos que isto e não podemos dizer que temos uma onda).
- Temos $p=k\Delta x/2=\frac{\pi \Delta x}{\lambda}$ logo, quando $\lambda= 2\Delta x$ teremos um $p$ **máximo** de $p=\pi/2$. 
- Assim, podemos fazer um gráfico $r(C,p)$ para $p\in[0,\frac{\pi}{2}]$ e $C\in[-1,1]$ (gráfico feito por moi, cada linha é um $C$):
![[graficos eq onda C abaixo 1.png]]
- Vemos que no comprimento de onda mínimo temos o rácio de velocidades mais diferente de 1, ou seja, o maior desvio entre as soluções discreta e exata. 
- Temos os maiores desvios de 1 para $C$s menores. Vemos ainda que (como seria de esperar) este varia com $C$ de forma simétrica ao zero.
- Mais importante, para $C=1$ temos rácio constante e igual a 1: as velocidades são iguais.

### Estabilidade
- Obviamente, $\omega$ é um valor real. Mas $\varpi$ pode ser complexo (não sei como, na equação acima não há maneira de surgirem complexos). Se esse for o caso, a amplitude irá aumentar exponencial ao longo do tempo, ou seja, a solução explode.
- Assim, para garantir estabilidade temos que garantir $\varpi$ real!
- A relação $\sin^{2}(\frac{\varpi \Delta t}{2})=C^{2}\sin^{2}\left(\frac{k\Delta x}{2}\right)$ implica que o lado da direita tem que ser $\leq1$. Assim, a condição de estabilidade é:
$$C=\frac{c \Delta t}{\Delta x}\le1$$
- Se aumentarmos C observamos o seguinte comportamento:
![[graficos eq onda C acima 1.png]]
(com $p\in[0,\pi/2]~,~C\in[-2,2]$)
- Vemos que para $C>1$:
    - $r$ aumenta com $p$ invés de diminuir. Ou seja, a onda numérica passa a mover-se mais rápido que a da solução exata ($\tilde c>c$)
    - não é possível chegar ao fim do range de $p$'s em teste (daí os espaços em branco no gráfico da esquerda e as linhas interrompidas nos outros gráficos)
    - As frequências $\varpi$ explodem, tendendo para $\pm\infty$ (linhas que ficam a apontar para cima ou para baixo ao chegar a certos valores de $p$)

- No notebook o professor diz que se $C>1$, a equação de $\varpi$ deveria mudar, passando a ter um $\sinh$ e passado $\varpi$ a ser complexo. Não consegui perceber como obter isto.
- De qualquer modo, o que temos a tirar é: para $C>1$ deixamos de ter comportamentos físicos!

# 2D e 3D
**2D**
- A equação de onda discretizada em 2D fica:
$$\partial_{t}^{2}[u_{q,r}^{n}]=c^{2}\left(\partial_{x}^{2}[u_{q,r}^{n}] + \partial_{y}^{2}[u_{q,r}^{n}]\right)$$
- Considerando uma grelha $t_{n}=n\Delta t~,~x_{q}=q\Delta x~,~y_{r}=r\Delta y$ vamos sugerir a solução:
$$u_{q,r}^{n}= e^{i(k_{x}q\Delta x+k_{y}r\Delta y-\varpi n\Delta t)}$$
e daqui surge a relação de dispersão:
$$\sin^{2}\left(\frac{\varpi \Delta t}{2}\right)= C_{x}^{2}\sin^{2}p_{x}+C_{y}^{2}\sin^{2}p_{y}$$
(em que $C_{i}=\frac{c \Delta t}{\Delta i}~,~p_{i}=\frac{k_{i} \Delta i}{2}$)
e garantir que $\varpi$ é real resulta em $C_{x}^{2}+C_{y}^{2}\le1$ ou seja:
$$\Delta t\le \frac{1}{c}\left(\frac{1}{\Delta x^{2}} + \frac{1}{\Delta y^{2}}\right)^{\frac{-1}{2}}$$
- Da relação de dispersão podemos obter:
$$\varpi=\frac{2}{\Delta t}\arcsin \left((C^{2}\sin^{2}p_{x}+C_{y}^{2}\sin^{2}p_{y})^{\frac{1}{2}} \right)$$
e podemos até escrever isto em coordenadas esférica: $k_{x}=k\cos\theta,k_{y}=k\sin\theta,p_{x}=\frac{1}{2}kh\cos\theta,p_{y}=\frac{1}{2}kh\sin\theta$ e podemos escrever o ratio de velocidades:
$$r=\frac{\tilde c}{c}=\frac{1}{Ckh} \arcsin \left(C\sqrt{\sin^{2}\left(\frac{1}{2}kh\cos\theta\right) + \sin^{2} \left(\frac{1}{2}kh\sin\theta \right)}\right)$$

**3D**
- Em 3D seria tudo análogo e teríamos a condição de estabilidade:
$$\Delta t\le \frac{1}{c}\left(\frac{1}{\Delta x^{2}} + \frac{1}{\Delta y^{2}} + \frac{1}{\Delta z^{2}}\right)^{\frac{-1}{2}}$$
# Eq Onda com Coeficientes Variáveis
- Consideremos o caso em que temos a onda a mover-se num meio não homogéneo. Teremos a eq onda:
$$\frac{\partial^{2}u}{\partial t^{2}}=\frac{\partial}{\partial x}\left(q(x)\frac{\partial u}{\partial x} \right) + f(x,t)$$
em que $q(x)$ será a velocidade (?)

- Vamos começar por discretizar apenas a derivada espacial exterior:
$$\phi=q(x)\frac{\partial u}{\partial x}$$
e usaremos derivada ao centro:
$$\left.\frac{\partial \phi}{\partial x}\right|_{i}^{n} \simeq \frac{\phi_{i+\frac12}-\phi_{i-\frac12}}{\Delta x}$$
- E podemos discretizar o termo interior:
$$\phi_{i+\frac12}=q_{i+\frac12} \left.\frac{\partial u}{\partial x}\right|_{i+\frac12}^{n}\simeq q_{i+\frac12}\frac{u_{i+1}^{n}-u_{i}^{n}}{\Delta x}$$
$$\phi_{i-\frac12}=q_{i-\frac12} \left.\frac{\partial u}{\partial x}\right|_{i-\frac12}^{n}\simeq q_{i-\frac12}\frac{u_{i}^{n}-u_{i-1}^{n}}{\Delta x}$$
- Juntando tudo temos:
$$\left[\frac{\partial}{\partial x}\left( q\frac{\partial u}{\partial x}\right)\right]^n_i\approx \frac{1}{\Delta x^2}\left( q_{i+\frac{1}{2}} \left({u^n_{i+1} - u^n_{i}}\right)- q_{i-\frac{1}{2}} \left({u^n_{i} - u^n_{i-1}}\right)\right)$$

- Mas para obter isto precisamos de $q$ em pontos intermédios (que não existem na grelha espacial). Para os determinar temos 3 opções:
$$\begin{align*}
q_{i+\frac{1}{2}} &\approx\frac{1}{2}\left( q_{i} + q_{i+1}\right)\quad &\text{(média aritmética)}\\
q_{i+\frac{1}{2}} &\approx2\left( \frac{1}{q_{i}} + \frac{1}{q_{i+1}}\right)^{-1}= 2 \frac{q_{i}\cdot q_{i+1}}{q_{i}+q_{i+1}}\quad &\text{(média harmónica)}\\
q_{i+\frac{1}{2}} &\approx \sqrt{q_{i}q_{i+1}}\quad &\hbox{(média geométrica)}
\end{align*}$$
- Em geral estas médias têm as seguintes propriedades:
    - Aritmética: muito influenciada pelo valor mais alto
    - Harmónica: muito influenciada pelo valor mais baixo
    - Geométrica: útil quando os valores em estudo ($q_{i},q_{i+1}$) pertencem a um comportamento exponencial

- Na maioria dos casos (e como temos feito nas restantes EDDPs) usasse a média aritmética. Ness caso temos que a equação diferencial é resolvida com:
$$\begin{align}
u^{n+1}_i &= - u_i^{n-1}  + 2u_i^n + \left(\frac{\Delta t}{\Delta x}\right)^2\left(\frac{q_{i} + q_{i+1}}{2}(u_{i+1}^n - u_{i}^n) -
\frac{q_{i} + q_{i-1}}{2}(u_{i}^n - u_{i-1}^n)\right)+ \nonumber \Delta t^2 f^n_i
\end{align}$$

## Neumann
- Consideremos a CF Neumann $\partial_{x}u=0$ em $x=L=N_{x}\Delta x$. Teremos:
$$\frac{u_{N_{x}+1}^{n}-u_{N_{x}-1}^{n}}{2\Delta x}=0~~\to~~ u_{N_{x}+1}^{n}= u_{N_{x}-1}^{n}$$
e a equação acima fica:
$$u^{n+1}_{i}\approx- u_{i}^{n-1}+2u_{i}^{n}+\left(\frac{\Delta t}{\Delta x}\right)^{2} 2q_{i}(u_{i-1}^{n}-u_{i}^{n})+\Delta t^{2} f^{n}_{i}$$
