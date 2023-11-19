# Resposta Impulsional de SLIT
Assim, consideremos
- $S$ um SLIT com função transferência $H(s)$. Temos uma função $h(t)$ tal que $H(s)=L[h(t)]$
- Temos então:
$$S[\delta(t-t_{0})]=h(t-t_{0})$$
- Ou seja, se a entrada de um sistema for o delta de dirac, a saída $h$, que é a **resposta impulsional** de $S$. 

- Por outro lado, sendo $S$ um SLIT com resposta impulsional $h$ temos:
$$S[x(t)]=x(t)*h(t)$$

- Ou seja, a resposta de um slit é a convolução entre o sinal de entrada e a resposta impulsional do sistema.

- Ou seja, esquematicamente temos:
![[convolucao e laplace.png]]

## Associação de Sistemas
### Em Série
- Sendo $S_{1},S_{2}$ SLITs com respostas impulsionais $h_{1},h_{2}$, a resposta impulsional deles em série será $$h(t)=h_{1}(t)* h_{2}(t)$$

### Em Paralelo
- Sendo $S_{1},S_{2}$ SLITs com respostas impulsionais $h_{1},h_{2}$, a resposta impulsional deles em paralelo será $$h(t)=h_{1}(t) + h_{2}(t)$$

# Sistemas Importantes
## Sistema Integrador
- Sistema em que o sinal de saída é o integral do sinal de entrada.
- Como vimos nas propriedades da convolução: $(f * u)(x)=\int_{-\infty}^{x} f(s)ds$. Ou seja, um circuito integrador terá uma resposta impulsional representada pela função degrau.
- Ora, um sistema integrador terá:
$$h(t)=u(t) \quad \quad;\quad \quad H(s)=\frac{1}{s}$$

## Sistema Diferenciador
- Sistema em que o sinal de saída é a derivada do sinal de entrada.
- Novamente, vimos nas propriedades da convolução que: $\left( f * \frac{d\delta}{dx} \right)(x)=\frac{df}{dx}$. 
- Assim, para um sistema diferenciador temos:
$$h(t)=\frac{d}{dt} \delta(t) \quad \quad;\quad \quad H(s)=s$$

## Sistema de Atraso
- Sistema em que o sinal de saída é igual ao de entrada, mas com atraso no tempo, ou seja, $y(t)=x(t-t_{0})$
- Neste caso temos:
$$h(t)=\delta(t-t_{0}) \quad \quad;\quad \quad H(s)=e^{-st_{0}}$$

## Sistema de Identificação
- Tendo um sinal conhecido $m(t)$, este sistema ajuda a determinar quando temos: $$x(t)=m(t-t_{0})$$
- Ou seja, temos: $$h(t)=m(-t)$$

# Deconvolução
- Aparece nesta aula, mas pus na aula 14 por uma questão de organização.

#sinais #fisica
