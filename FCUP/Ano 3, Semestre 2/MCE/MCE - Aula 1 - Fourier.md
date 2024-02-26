# 0 - Intro
## Avaliação
- 2 tpcs, data a confirmar
    - Entregar jupyter em que o MD está escrito como relatório (ou relatório ig)
- Exame como tps

## Notas
- ChatGPT e similares estritamente proibidos.

## Livros
- Lloyd Trefthen - Spectral Methodes with Mathlab -- bom para a parte core, mas a intro também é útil

# 1 - Fourier
## 1.1 - Transformadas integrais
- Transformada do tipo:
$$Tf(y)=\int_{D}K(y,x)f(x)dx$$
que é basicamente uma média podenrada de $f$. $K$ é o *núcleo* da trnasformação. 
- Se o núcleo admitir inversa, podemos ter a transformada inversa:
$$f(x)=\int_{D}K^{-1}(x,y)Tf(y)dy$$
- Núcleo de Fourier é $K(y,x)=\exp(-i2\pi y\cdot x)$

## 1.2 - Calcular numericamente
- Como uma transformada não passa de uma integral, podemos usar métodos computacionais (Riemman, Simpson, Trapézio, etc)
- Assim, podemos escrever uma transformada integral na forma
$$Df_{m}=\sum\limits_{n=1}^{N}K_{mn}f_{n}$$
- Fourier converte função complexa variável real noutra complexa variavel real (nucleo é complexo)
- Temos a transformada de Fourier:
$$F(\omega) = \int_{-\infty}^{+\infty} f(t)\exp(-i\omega t)dt$$
e a inversa
$$f(t)=\frac{1}{2\pi}\int_{-\infty}^{+\infty} F(\omega)\exp(i\omega t)d\omega$$
em que o termo $1/2\pi$ pode ser colocado na trnasformada, na inversa ou divido entre elas como $1/\sqrt{2\pi}$

## 1.3 - Propriedades Fourier
Temos as properidades:
- *Linearidade*: $\mathcal{F}(af(t)+bg(t))=a\mathcal{F}(f(t))+b\mathcal{F}(g(t))$
- *Translação*: $\mathcal{F}(f(t-a))=e^{-i\omega a}F(\omega)$
- *Escala*: $\mathcal{F}(f(at))=\frac{1}{|a|}F\left(\frac{\omega}{a}\right)$
- *Conjugação*: $\mathcal{F}(f^{*}(t))=F^{*}(-\omega)$
- *Derivada*: $\mathcal{F}(f'(t))=i\omega F(\omega)$
- *Convolução*: $\mathcal{F}(f(t)*g(t))=F(\omega)G(\omega) \Leftrightarrow \mathcal{F}^{-1}(fg)=f*g$
- *Teorema de parseval*: $\int_{-\infty}^{+\infty}|f(t)|^{2}dt=\frac{1}{2\pi}\int_{-\infty}^{+\infty}|F(\omega)|^{2}d\omega$
- *Princípio de Incerteza*: $\Delta t=\frac{1}{f(0)}\int_{-\infty}^{+\infty}|f(t)|ft~~,~~ \Delta\omega=\frac{1}{F(0)}\int_{-\infty}^{+\infty}|F(\omega)|d\omega~~;~~ \Delta\omega\Delta t\le2\pi$

## 1.4 - DFT
- A maioria dos sinais e grandezas medidos são contínuos (luz, som, etc). No entanto, o instrumento de medição usado nunca consegue medir a grandeza de forma contínua, porque isso implicaria uma recolha de dados com frequência infinita.
- Assim, recolhemos uma quantidade finita de pontos. Convertemos um sinal $x(t)$ *contínuo* num sinal *discreto* $x[n]$. Podemos chamar a isto *digitalização do sinal*.
- Temos um **período de amostragem** ($t_s$) - intervalo de tempo entre valores medidos (temos valores em $t_{s},2t_{s},3t_{s},\dots$). Podemos ainda definir a frequência de amostragem $f_{s}=1/t_{s}$
- Podemos então ver que os valores medidos são $x[n]=x(n\cdot t_{s})$ 

### 1.4.2 - Aliasing
- Problema que ocorre ao fazer recolha de sinais contínuos.
- Este é o nome do fenómeno em que 2 sinais contínuos diferentes $x(t),y(t)$ nos dão o msm sinal amostrado para uma *mesma taxa de amostragem*.
- Para uma taxa de amostragem $f_{s}$ 2 frequências $f,f'$ são *alias* se $$f'=f+kf_{s}$$
- Ou seja, tendo $x,y$ com frequências $f,f'$, se estas frequências forem alias teremos que o sinais amostrados $x[n],y[n]$ serão **iguais** para todo o $n$!
![[aliasing.png]]
vemos que todos estes sinais passam por alias. Usou-se $f_{s}=5Hz$ (verificar)
- Temos a demonstração:
$$\begin{align} y[n] = \cos(2\pi f' t) =  \cos\Big(2\pi (f + k. f_s)\frac{n}{f_s} \Big) &= \cos\Big(2\pi f \frac{n}{f_s} + 2\pi k. f_s\frac{n}{f_s} \Big)  \\
 &= \cos\Big(2\pi f \frac{n}{f_s} + 2\pi k n\Big) \\
 & = \cos\Big(2\pi f \frac{n}{f_s} \Big) = x[n]
\end{align}$$
- Vimos um exemplo com áudio. Tendo-se 2 sinais, de frequência $f_{1}=220Hz$ e $f_{s}=8000Hz$. Ao fazer amostragem deste sinal e de um sinal com frequência $f_{2}=8220Hz$, obtemos exatemente o mesmo sinal, de tal forma que o som dos sinais é igual.

### 1.4.3 - Teorema de amostragem de Nyquist-Shannon
- Como seria de prever, o aliasing não pode ser evitado!
- Este teorema permite garantir que o aliasing não afeta o sinal recolhido:
    - Temos um sinal de **banda limitada** se este puder ser decomposto numa soma ponderada de sinais sinusoidais com frequências entre $f_{-}$ e $f_{+}$. Ou seja, o tamanho da banda é $f_{+}-f_{-}$
    - O teorema diz-nos que se a banda limitada de um sinal for $f_{+}-f_{-}$, então qualquer taxa de amostragem $f_{x}>f_{+}-f_{-}$ irá permitir evitar aliasing! 
    - Temos que considerar as frequências positivas e negativas: não podemos ter $f_{-}=0$. Colocamos $f_{-}=-f_{+}$. Mais concretamente, em função do tipo $\cos(\dots)$ com frequência $f_{0}$ temos que ter $f_{S}>2f_{0}$
![[aliasing pq funciona.png|450]]
![[aliasing 2.png|450]]

## 1.5 - DFT
$$X[k]=\sum\limits_{n=0}^{N-1}x[n]\exp\left(-i2\pi\frac{nk}{N}\right)$$
- As propriedades deste são diferentes da Transformada de Fourier de tempo contínuo (TF)

### 1.5.1 - Transformada de Fourier periódicas ou em janela temporal
- Exemplo de função de calcular DFT:
![[funcao dft 1.png]]
em que
![[funcao dft 2.png]]

- Numa FT de um sinal em janela temporal (por exemplo uma função triangular entre -1 e 1 e nula no restante domínio) temos um traçado contínuo.
- Ao fazer FT de um sinal contínuo (função triangular igual à de cima com mesma amplitude, mas periódica entre -10 e 10) temos um traçado discreto (FT=0 na maioria do traçado). Apesar disso, os pontos obtidos encontram-se no traçado da função de janela temporal:
![[fourier periodica vs nao.png]]
Aqui devemos notar:
    - Como a função periódica consiste à função triangular repretida 10 vezes, temos que dividir a transformada da função contíonua por 10 -  temos 10 vezes mais "energia"
    - Podemos ver isto como sendo uma amostragem da FT da função da janela.

- Consideremos agora aplicamos à função triangular uma janela retangular ($=1$ em $[0,2]$, $=0$ no resto do domínio):
![[fourier periodica vs janela.png]]temos que a FT desta função ajanelada é a *convolução* das funções FT da função periódica e da função da janela. Neste caso, a ordem a convolução não impota.
Assim, voltamos a ter uma FT contínua. De recordar que a transformada de Fourier de uma função retangular é uma função sinc ao quadrado.

- Consideremos agora quase o mesmo caso, mas com uma janela de largura 1:
![[fourier periodica vs janela 2.png]]

- Ou seja, o que vimos acima é:
    - TF de função não periódica é contínua
    - TF de função de período $T$ é discreta com picos distanciados em $1/T$
    - TF de função de período $T$ filtrada por janela retangular de largura $T_{W}$ é contínua. Corresponde a convolução do espetro discreto da função com o contínuo da função janela.

### 1.5.2 - Amostragem
- Se tivermos uma função como abaixo à esquerda:
![[dft - o que metodo assume.png]]
a DFT assume sempre que a função é periódica, repetindo-se como mostrado à direita. Ora, isto pode não ser verdade. Por exemplo, a função podia continuar sempre a subir ou variar de qualquer outra forma. 

- A frequência máxima que podemos analisar com uma DFT é $F_{max}=N\Delta f=N/T=N/(N/F_{s})=F_{s}$ -- para sinal de período $T$ e frequência $F$. $F_{s}$ será a taxa de amostragem.

- Ao fazer DFT de um sinal sinusoidal de frequência $20Hz$ obtemos:
![[dft de periodica.png]]
ora, temos um pico em $20Hz$, como seria de esperar.
- Mas temos um pico em $980Hz$. Ora, podemos escrever este pico como $N-k$, em que $k=20$. Ora: $\exp(-i2\pi n\frac{N-k}{N})=\exp(-i2\pi n\frac{-k}{N})$.
    - Isto diz-nos que no espetro da DFT a *2ª metade é um espelho da 1ª*!! Assim, podemos simplesmente considerar a 2ª metade como tendo as mesmas frequências, mas com sinal negativo: $980Hz\to-20Hz$
    - Assim, o espetro será sempre: $$F=\left[\frac{-F_{S}}{2},\frac{-F_{S}}{2}+ \frac{F_{S}}{N},\frac{-F_{S}}{2}+ 2 \frac{F_{S}}{N},\dots,\frac{F_{S}}{2}-\frac{F_{S}}{]}{N},\frac{F_{S}}{2}\right]$$

### 1.5.3 - Spectral Leakage
- Facilita sempre a análise ter um domínio que consista a períodos inteiros, tal como fizemos em todas as funções de exemplos atrás.
- Consideremos a função $x(t)=\cos(???)$ numa janela com períodos não inteiros temos:
![[fourier intervalos nao inteiros.png]]
- Obtemos picos em intervalos constantes (neste caso específico, intervalos de $1,25Hz$).
- Além disso, o sinal em estudo tem frequência $f_{0}=2Hz$. O que se observa é que os maiores picos são aqueles mais próximos de $2$ (o maior pico da imagem encontra-se em $\pm2,5Hz$). Ou seja, a "energia" do pico em $2Hz$ é distribuido pelos picos em volta.

- A razão deste problema é que ocorre o que temos abaixo:
![[fourier intervalos nao inteiros 2.png]]
porque, como já mencionado, a DFT assume que a função é periódica. Ora, em análise de Fourier, saltos bruscos implicam usar muitas ondas sinusoidais (recorda exemplo do efeito de Gibbs). Assim, invés de ter apenas 2 picos em $\pm f_{0}$ temos vários picos para ter as várias componentes que permitem obter as secções "verticais" da função periódica que o DFT "inventa".

- Vemos abaixo a transformada de Fourier (parte real no centro, imaginária na esquerda) de uma função que consiste na subtração de 2 funções retangulares e produto disto por uma gaussiana:
![[fourier amostragem bem.png]]
vemos que a DFT aparenta seguir o traçado "teórico", a vermelho.

- Consideremos agora que para a mesma função usamos a frequência $f_{s}=5$:
![[fourier amostragem mal.png]]
já não temos uma boa sobreposição. Isto ocorre porque a taxa de amostragem é tão baixa que não temos pontos suficientes para ter dados corretos.

## 1.6 - FFT
- A DFT, como já vimos, para uma amostragem de $N$ pontos, para cada ponto calcula uma exponencial complexa em cada frequência. Ora, calculamos então $N\times N$ valores. Por outras palavras, DFT expande com $N^{2}$ / $\mathcal{O}(N^{2})$
- O algoritmo FFT permite fazer a mesma conta, mas com $\mathcal{O}(N\ln N)$

- Por exemplo, para a análise de um ficheiro com 1 milhão de pontos ($N=10^{6}$) (que até é pouco). Consideremos um processador de $1\text{GHz}$ (faz 1 ciclo em $10^{-9}\text{s}$) e vamos assumir que todas as contas são feitas em 1 ciclo (demora mais normalmente).
    - A DFT iria demorar $10^{12}\cdot10^{-9}=1000\text{s}$
    - A FFT iria demorar $10^{6}\ln(10^{6})\cdot10^{-9}\sim 10^{-2}\text{s}$

## 1.7 - Leitura
- Veremos melhor na próxima aula
- Se tivermos um ficheiro wav para ler, podemos usar a função `wavfile` do módulo `scipy.io`. 
- Este tipo de ficheiros normalmente irá ser lido como uma matriz $2\times N$ - 1 canal esquerdo e 1 canal direito (normalmente teremos som estereo). Se o som já for mono já temos uma matriz $1\times N$
- Por exemplo, para ficheiros de imagem (jpeg, png) teremos uma matriz $3\times N$ (RGB) ou $4\times N$ (RGB$\alpha$ - RGB+transparência) ou $1\times N$ (foto monocromática sem transparência)
