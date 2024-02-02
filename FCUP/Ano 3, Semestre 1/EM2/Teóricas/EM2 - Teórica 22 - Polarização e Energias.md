## Polarização de Ondas EM
- Podia ter feito isto na parte de intro a ondas no início, mas o Avelino falou disto com campo elétrico, então também o farei.

### Polarização linear
- Quando a onda aponta sempre na mesma direção.
- Temos algo assim:
$$\vec{E}= \vec{E}_{0[R]}e^{i(\vec{k}\cdot\vec{r}-\omega t + \delta_{E})}$$
e aqui estamos a fazer a distinção entre a parte real e imaginária do vetor $\vec{E_{0}}$ (em que $\vec{E}_{0[R]}$ é a parte real). Podemos então definir o vetor inicial:
$$\vec{E_{0}}=\vec{E}_{0[R]}e^{i\delta_{E}}=e^{i \delta_{E}}\left(E_{0x[R]}\hat{x} + E_{0y[R]}\hat{y} \right)$$
ou seja, podemos separar o vetor inicial na sua parte real e na sua imaginária, que consiste na fase complexa do campo. Dentro da parte real, temos as componentes $x,y$.
- Num campo com polarização linear não existe diferença de fase entre as componentes reais 

### Polarização Circular
![[Attachments/FCUP/A3S1/EM2/polarizacao circular.png]]
- Ocorre quando temos estas 2 coisas: $$E_{0x[R]}=E_{0y[R]}~~~~;~~~~ \delta_{y}-\delta_{z}=\pm \frac{\pi}{2}$$

### Polarização Eliptíca
![[Attachments/FCUP/A3S1/EM2/polarizacao eliptica.png]]
- Este é o caso mais comum, porque temos $$E_{0x[R]}\neq E_{0y[R]}~~~~;~~~~ \delta_{x}\neq \delta_{y}$$
e fica:
$$\vec{E_{0}}=E_{0x[R]} e^{i\delta_{x}} + E_{0y[R]} e^{i\delta_{y}}$$

## Energia e Momento Linear de Ondas EM
- Consideremos uma onda monocromática com polarização linear a propagar-se na direção zz:
$$\vec{E}=E_{0}\cos(kz-\omega t+\delta)\hat{x} \quad \quad;\quad \quad \vec{B}=\frac{E_{0}}{c} \cos(kz-\omega t + \delta)\hat{y}$$
(em que $\hat{y}=\hat{k}\times \hat{x}=\hat{z}\times \hat{x}$)

**Densidade de Energia**
- Vimos no capítulo de Eletrodinâmica que a densidade de energia de um campo EM é dada por:
$$u = \frac{1}{2}\left(\varepsilon_{0}E^{2} + \frac{1}{\mu_{0}}B^{2}\right) $$
e vimos que $B=\frac{1}{c}E\to B^{2}=\frac{1}{c^{2}}E^{2}=\mu_{0}\varepsilon_{0}E^{2}$. Ficamos com:
$$u=\frac{1}{2} \left(\varepsilon_{0}E^{2}+ \frac{1}{\mu_{0}}\varepsilon_{0}\mu_{0}E^{2} \right)=\varepsilon_{0}E^{2}=\varepsilon_{0} E_{0}^{2}\cos^{2}(kz-\omega t+\delta)$$

**Vetor Poynting**
- Temos (no vazio):
$$\begin{align*}
\vec{S}=\frac{1}{\mu_{0}}(\vec{E}\times\vec{B})&= \frac{1}{\mu_{0}} E_{0}\cos(kz-\omega t+\delta)\hat{x}~\times~ \frac{E_{0}}{c} \cos(kz-\omega t + \delta)\hat{y}\\
&= c \varepsilon_{0}E_{0}^{2}\cos^{2}(kz-\omega t+\delta)\hat{z}=cu \hat{z}
\end{align*}$$
o que faz bastante sentido. Temos que o vetor Poynting aponta na direção da propagação e tem módulo igual a 'densidade de energia' x 'velocidade' AKA energia que passa numa unidade de área por unidade de tempo:
$$[S]=[c][u]=\frac{[r]}{[t]} \frac{[E]}{[r^{3}]}=\frac{[E]}{[r^{2}][t]} $$

**Momento Linear**
- Conforme o que vimos no capítulo da conservação temos:
$$\vec{g}=\frac{1}{c^{2}}\vec{S}=\frac{u}{c} \hat{z}$$

### Valores Médios
- Na prática, o que importa saber é o valor médio destas grandezas. Isto porque ondas EM frequentemente são estudadas sobre a forma de luz, pelo que as oscilações são tão rápidas que saber $u,\vec{S},\vec{g}$ num instante é impossível; qualquer medição irá contar várias oscilações. 
- Ao longo de 1 oscilação de uma onda EM o valor médio de cosseno quadrado é:
$$\langle\cos^{2}(kz-\omega t)\rangle=\frac{\int_{0}^{T}\cos(kz-\omega t)dt}{T}=\frac{\int_{0}^{2\pi}\cos^{2}\theta ~d \theta}{2\pi}=\frac{1}{2}$$
e resulta então:
$$\begin{align*}
\langle u\rangle &= \frac{1}{2}\varepsilon_{0}E_{0}^{2}\\
\langle \vec{S}\rangle &= \frac{1}{2}c \varepsilon_{0}E_{0}^{2}\hat{z}=c\langle u\rangle \hat{z}\\
\langle \vec{g}\rangle&= \frac{\langle \vec{S}\rangle}{c^{2}}= \frac{\langle u\rangle}{c}\hat{z}= \frac{1}{2} \frac{\varepsilon_{0}}{c}E_{0}^{2}\hat{z} 
\end{align*}$$
- Aqui devemos notar uma importante e frequentemente usada definição: a potência média por unidade de área de uma onda é a sua **Intensidade**:
$$I\equiv \langle S\rangle=\frac{1}{2}c \varepsilon_{0}E_{0}^{2}$$
de acordo com a análise dimensional podemos ver que: $[S]=[c][u]=\frac{[r]}{[t]} \frac{[E]}{[r^{3}]}=\frac{[E]/[t]}{[r^{2}]}=\frac{[P]}{[r^{2}]}$

### Pressão de Radiação
- Quando uma onda EM incide num objeto absorvente, ela transfere momento linear para o objeto, sendo então gerada pressão de radiação.
- Assumindo que a onda incide na perpendicular da superfície:
$$P = \frac{F}{A}=\frac{1}{A} \frac{dp}{dt}=\frac{1}{A} \frac{d}{dt}(\underbrace{|\langle \vec{g}\rangle| Ac ~dt}_{=\frac{[p]}{[r^{3}]} [r^{2}] \frac{[r]}{[t]}})$$
em que se usou a definição de $\vec{g}$ como densidade de momento linear por volume e por área. Ao multiplicar por $Ac~dt$ estamos a anular todas as grandezas menos o momento linear, tendo-se $\frac{dp}{dt}=\frac{d (|\langle \vec{g}\rangle| Ac ~dt)}{dt}$.
- Continuando:
$$P=\frac{F}{A}=\frac{1}{A} \frac{d}{dt}|\langle \vec{g}\rangle| Ac ~dt=|\langle \vec{g}\rangle|c=|\langle u\rangle|=\frac{|\langle \vec{S}\rangle|}{c}=\frac{I}{c}$$
