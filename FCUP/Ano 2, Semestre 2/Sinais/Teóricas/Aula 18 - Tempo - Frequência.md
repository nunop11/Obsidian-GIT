# Transformada Inversa de Fourier
$$F^{-1}[X(j\omega )]=\frac{1}{2\pi}\int_{-\infty}^{+\infty} X(j\omega)e^{j\omega t}d\omega=x(t)$$
- Ora, aqui vemos aquilo que falei no teorema da Dualidade: estas 2 expressões são muito semelhantes.
- Em parte, isto ocorre porque nas transformadas de Laplace estávamos a converter $tempo\to frequencia~~complexa$, ou seja, um número real num complexo. Nas transformadas de Fourier, estamos a converter $tempo\to frequencia~~angular$, que são ambos números reais.

# Relação tempo-frequencia
![[freq-tempo.png]]
- Definimos uma função $x(t)$ e a sua transformada $X(j\omega)$. 
    - $D_{1}$ será a distância temporal tal que uma função retângulo com essa largura tenha a mesma área e altura que $x(t)$. Igualmente para $B_{1}$.
- Ao usar a definições das transformadas de fourier e fourier inversa para $t=0$ obtem-se:
$$D_{1}=\frac{X(0)}{x(0)} \quad;\quad B_{1}=2\pi \frac{x(0)}{X(0)}$$
Ou seja: $$D_{1}B_{1}=2\pi $$
- Daqui vemos que o produto da largura temporal de uma função no domínio do tempo pela largura espectral da sua representação no domínio das frequências é *constante*.

- O que vimos acima é específico para funções reais e simétricas. A forma geral, e que não me apeteceu estudar com atenção, é $$D_{2}B_{2}\ge \sqrt{\frac{\pi}{2}}\Longrightarrow \Delta t \Delta \omega\ge \sqrt{\frac{\pi}{2}}$$
No PPT isto resultou numa tangente de 10 slides sobre o princípio de incerteza de heisenberg e as suas implicações 😀

#sinais #fisica 