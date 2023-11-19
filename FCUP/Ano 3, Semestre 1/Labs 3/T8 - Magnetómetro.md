# NOTAS
- Magnetómetros combinam efeitos elétricos associados à magnetização com efeitos elétricos/mecânicos. 3 Tipos:
    - medir força exercida sobre amostra sujeita a H não uniforme
    - medir inducao magnet na vizinhança da amostra
    - medir fenomenos indiretos (resistencia eletrica ou strain)

- Tds os métodos de indução magnetica funcionam assim:
    - Temos uma bobina de deteçao ligada a voltimetro
    - Quando a posição relativa da amostra varia em relação à bobina de deteção

- Temos $$\vec{B}=\mu_{0}(\vec{H}+\vec{M})$$
- Grandezas:
    - $\vec{M}$ - magnetização : momento magnet p/ unidade volume
    - $\vec{H}$ - campo magnético aplicado (A/m)
    - $\vec{B}$ - densidade de fluxo de campo magnético /  indução (T)
ou seja:
    - $\vec{H}$ dá-nos campo magnético que existe na vizinhança de uma fonte 
    - $\vec{B}$ dá-nos a densidade das linahs de campo numa área na vizinhança

### VSM
![[magnetometro vsm.png]]
em que:
    1. amostra
    2. barra porta-amostra
    3. altifalante
    4. estrutura de cartao
    5. bobina de campo - ACHO que é suposto ser uma bobina grande que contorna tudo o resto -  na figura temos corte transvesal (daí fio entrar num lado e sair no outro). 1 e 6 estão dentro desta e portanto sujeitos a um campo magnético uniforme.
    6. bobinas de deteção - São 2 bobinas menores. Tambem elas são representadas na figura por corte transversal - cortornam fio 2 acima e baixo da amostra

funcionamento:
    - a barra que segura a amostra (2) é posta a vibrar com uma frequência $\sim100Hz$ graças ao altifalante e estrutura cartao (3,4)
    - isto faz com qe bobinas também oscilem para cima e para baixo. Ou seja, mantém o seu eixo alinhado com o eixo central da bobina 5 mas passam a ter movimento relativo -> passa a haver fluxo magnetico


- seja $\vec{H}=H \hat{z}$ o campo aplicada na amostra de volume $V$. O seu momento magnético será $\vec{m}=m\hat{z}$. Se houver magnetização na amostra surge uma indução magnética $\vec{B}_{\vec{M}}(\vec{r})$ na sua vizinhança
- $B_M$ será proprocional ao fluxo magnético num ponto, tendo-se:
$$\Phi_{m}^{\pm}=\pm F\left(z\pm \frac{h}{2}\right)m$$
em que $z$ é a posição da amostra e $z\pm \frac{h}{2}$ a distância desta a cada bobina de deteção (+ : cima, - : baixo)
- $F$ é uma função geometrica que depende dessa distancia, o nº de espiras das bobinas de deteção, parametros de configuração geometrica das bobinas, etc. Esta função será simétrica em torno de $z\pm \frac{h}{2}$

- O fluxo total das 2 bobinas é:
$$\Phi_{M}=\Phi_{M}^{+}(z)+\Phi_{M}^{-}(z)=\left[F\left(z+ \frac{h}{2}\right) + F \left( z- \frac{h}{2} \right)\right]=K(z)m$$
em que $K$ será uma função anti-simetrica. A sua derivada, $K'(z)$, já será simétrica outra vez.

- Se considerarmos que a amostra está centrada em $z=0$ e que o altifalante a faz vibrar de forma sinusoidal, temos $$z(t)=A\cos(\omega t)$$
em que:
    - $A$ é a amplitude de vibração. Se for suficientemente baixa, podemos desprezar a variação do campo aplicado no tempo
    - $\omega$ a freq angular associada à vibraçao do altifalante+fio

- A força eletromotriz induzida na amostra será:
$$\varepsilon(t)=- \frac{d \Phi_{M}}{dt}=K'(0)A\omega m \sin (\omega t)~~\to~~ \varepsilon(\omega)=K '(0)A\omega m$$
- Nesta atividade vamos medir apenas $\varepsilon$. Isto permite obter a variação de $M$ com $H$ a menos do fator de uma constante. Será ainda possivel observar comportamentos de histeres:
![[ciclo histerese magnetometro.png]]

## Lock-in
- importante para medir sinais fracos com muito ruido elétrico
- Na pratica, consiste em aplicar um filtro eletrico com largyra de banda baixa e sintonnizado com uma frequencia específica do sinal. Assim conseguimos isolar o ruido nessa zona. 
    - Por exemplo, consideremos que temos uma frequencia de referencia $f=10kHz$ e aplicamos um filtro lock-in com largura de banda $\Delta f=0.1Hz$. Temos fator de qualidade $Q=f/\Delta f=10^{6}$ 

- Além de filtrar, o lock-in também gera ganho no sinal / amplificação em tensão.

**lógica de funcionamento**
- temos lock-in ligado a sistema em excitação em frequencia específica e "calma" no espetro de ruído.
- Fornecem-se 2 sinais ao lock-in:
    - sinal periódico $V_{ref}$ estável e com a frequência $f_{ref}$ - freq de excitação do sinal que queremos medir
    - sinal $V_{i}$ que terá várias componentes oscilatórias com frequências arbitrárias $f_{i}$ (ou $\omega_{i}$). dentro destas teremos a frequência que queremos medir

![[amplificador lock-in.png]]
- em lock-ins de lab é comum podermos subtrair sinais de fundos, $V_{i}=V_{A}-V_{B}$
- Temos um amplificador do sinal $V_{i}$ ficando-se com $V_{s}=AV_{i}$
- **PLL** - deteta a freq principal do $V_{ref}$ - $f_{ref}$. Com esta gera um sinal sinusoidal com freq angular $\omega_{ref}$
- Teremos 2 PLL no lock-in, que gerarão sinais $\cos\omega_{ref} t,\sin\omega_{ref}t$ que estão portanto desfazados de 90º
- **PSD** - compara o sinal $V_{s}$ com o sinal $V_{ref}$, gerando o batimento entre eles.
- No Lock-in temos 2 PSD, resultando:
$$\begin{align*}
V_{X}^{PSD}=\frac{1}{2}V_{s}[\cos[(\omega_{ref}+\omega_{i})t+\phi]-\cos[(\omega_{ref}-\omega_{i})t+\phi]]\\
V_{X}^{PSD}=\frac{1}{2}V_{s}[\sin[(\omega_{ref}+\omega_{i})t+\phi]-\sin[(\omega_{ref}-\omega_{i})t+\phi]]
\end{align*}$$
- Estes 2 sinais passam por filtros passa-baixo que cortam os termos de valor alto das parcelas com $\omega_{ref}+\omega_{i}$ (estas parcelas desaparecem). Apenas passam as componentes DC com frequência $f_{ref}-f_{i}\to0 \Leftrightarrow f_{ref}\approx f_{i}$
- fica:
$$\begin{align*}
V_{x}\sim \frac{1}{2}V_{S}\cos[(\omega_{ref}-\omega_{i})+\phi]\sim \frac{1}{2}V_{S}\cos\phi\\
V_{x}\sim \frac{1}{2}V_{S}\sin[(\omega_{ref}-\omega_{i})+\phi]\sim \frac{1}{2}V_{S}\sin\phi
\end{align*}$$
em que se usou $f_{ref}-f_{i}\to0 \Leftrightarrow \omega_{ref}-\omega_{i}\to0$

- Podemos escrever o sinal de saída do lock-in como fasor $R\angle\phi$ em que:
$$R=\sqrt{V_{X}^{2}+V_{Y}^{2}} \quad \quad;\quad \quad \phi=\arctan \left(\frac{V_X}{V_Y} \right)$$
- A largura de banda do filtro é controlado através da constante de tempo, que é manobrada pelo painel frontal. Devemos escolher constante tempo 3 a 5 vezes maior que o tempo caraterístico das flutuações. Mas se for demasiado elevado, o lock-in irá esconder processos rápidos que aconteçam e que podem ser interessantes.

## Execução
![[circuitos da t8.png]]
