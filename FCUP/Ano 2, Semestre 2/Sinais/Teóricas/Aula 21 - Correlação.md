# Correlação
- A *correlação* entre 2 entidades acaba por ser o nível de semelhança entre elas, sendo maior quando são mais semelhantes.

- Ora, consideremos que temos 2 funções $f,g$ e fazemos o produto $f(\tau)g(\tau)$ num qualquer instante $t=\tau$. Se os valores forem semelhantes, iremos obter $f(\tau)g(\tau)>0$
- Ou seja, se somarmos estes produtos para todos os instantes, ou seja, temos:
$$\int_{-\infty}^{+\infty} f(t)g(t)dt$$
- Sendo que se este integral for $=1$ então temos *correlação total*. Se tivermos $=0$ temos *correlação nula*.
- Por razões que não me apeteceu passar, é vantajoso definirmos *correlação* como $$\int_{-\infty}^{+\infty} f(t)g^{*}(t)dt$$
- Sendo que temos a *correlação de* $f(t),g(t)$:
$$\varphi_{fg}(\tau)=\int_{-\infty}^{+\infty} f(t+\tau)g^{*}(t)dt$$
sendo que temos o caso particula $g=f$, que é a *autocorrelação de* $f$:
$$\varphi_{ff}(\tau)=\int_{-\infty}^{+\infty}f(t+\tau)f^{*}(t)dt$$
Conseguimos ainda escrever:
$$\varphi_{fg}(\tau)=f(\tau)*g(-\tau) \quad \quad;\quad \quad \varphi_{ff}(\tau)=f(\tau)* f^{*}(-\tau)$$
- De notar que, num SLIT, temos:
$$\varphi_{ys}(\tau)=y(\tau)*x^{*}(-\tau)=h(\tau)*x(\tau)*x^{*}(-\tau)=h(\tau)* \varphi_{xx}(\tau)$$

## Propriedades
- **Anti-Comutativa** - $$\varphi_{fh}(\tau)=\varphi_{hf}^{*}(-\tau)$$
- **Autocorrelação de função real é Par** - Ou seja, temos $\varphi_{ff}(\tau)=\varphi_{ff}(-\tau)$
- **Teorema de Wiener-Khinchin** - A transformada de Fourier de $\varphi_{ff}(\tau)$ dá-nos a energia por unidade de tempo do sinal na frequência $\omega$. Ou seja, tendo uma função $f(t)\to F(\omega)$ e representando a *densidade de potencia espectral* como $S(\omega)$ ficamos com $S(\omega)=|F(\omega)|^{2}$, ou seja, $F[\varphi_{ff}(\tau)]=S(\omega)$.
- **Relação com Fourier** - Temos $$F[\varphi_{fh}(\tau)]=F^{*}(\omega)H(\omega)$$

#### Propriedades de função Hermíticas
- Uma função é hermítica se $f^{*}(-x)=f(x)$. Assim:
    - **Igualdade à Convolução** - $\varphi_{fh}(\tau)=(f*h)(\tau)$
    - **Comutatividade** - $\varphi_{fh}(\tau)=\varphi_{hf}(\tau)$

#sinais #fisica