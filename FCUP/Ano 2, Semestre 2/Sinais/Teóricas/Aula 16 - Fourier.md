# Transformada de Fourier
- Anteriormente vimos as transformadas de Laplace, que consistem na soma de projeções segundo exponenciais complexas.
- Ora, nem todas as funções têm transformadas de Laplace. Por exemplo, $\cos(\omega t)$ só tem transformada de estiver multiplicado pela função degrau: $\cos(\omega t)u(t)$
- Outra função que não tem transformada de Laplace é a *exponencial complexa*, o que é mau, porque estas funções são as autofunções dos SLIT.

- Assim, comecemos por analisar melhor a frequência da transformada de Laplace: $s=\sigma+i\omega$. Temos:![[laplace no espaco.png]]
- Ou seja, a parte imaginária influencia a frequência e a parte real influencia a amplitude.
- Assim, se queremos estudar um certo sistema no domínio das frequências, podemos simplesmente reduzir o espaço complexo apenas ao eixo dos valores imaginários. Ou seja:
$$X(j\omega)=\int_{-\infty}^{+\infty}x(t)e^{-j\omega t}dt$$
ora, isto é a ***Transformada de Fourier*** de $x(t)$.

# Séries de Fourier
- Tendo em conta o que foi dito acima temos:
$$F[x(t)]=L[x(t)]_{s=j\omega}$$
daqui podemos escrever:
$$X(s)=F[x(t)e^{-\sigma t}]$$

- Temos um sinal $x(t)$ com período $T=\frac{2\pi}{\omega_{0}}$. Queremos saber como determinar os coeficientes $c_{k}$ tais que: $$x(t)=\sum\limits_{k=-\infty}^{+\infty}c_{k}e^{jk\omega_{0}t}$$
- Ora temos:
$$c_{k}=\frac{1}{T}\int_{0}^{T} x(t)e^{-jk\omega_{0}t}dt$$

## Representação Trigonométrica
$$\begin{align*}
x(t)=\frac{a_{0}}{2} + \sum\limits_{k=1}^{\infty}[a_{k}\cos(k\omega_{0}t)+b_{k}\sin(k\omega_{0}t)]\\
a_{k}=\frac{2}{T}\int_{0}^{T}x(t)\cos(k\omega_{0}t)dt \quad;\quad b_{k}=\frac{2}{T}\int_{0}^{T}x(t)\sin(k\omega_{0}t)dt
\end{align*}$$
- Sendo que temos 2 casos particulares:
    - $x(t)$ **par**: $x(t)=\frac{a_{0}}{2} + \sum_{k=1}^{\infty}a_{k}\cos(k\omega_{0}t)$
    - $x(t)$ **ímpar**: $x(t)=\sum_{k=1}^{\infty}b_{k}\sin(k\omega_{0}t)$

### Representação Harmónica
![[fourier harmonico.png]]

## Fourier para Não-Periódicas
- É deduzido no PPT

## Representação
- Podemos representar uma transformada de Fourier como $X(\omega)$ ou $X(j\omega)$. Iremos usar a *segunda*.

#sinais #fisica #fourier 