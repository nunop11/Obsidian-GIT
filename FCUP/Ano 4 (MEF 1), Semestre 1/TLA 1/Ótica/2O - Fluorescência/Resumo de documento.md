# 5. Medição de lifetime no domínio de freq
- Veremos formas de medir o decaimento da intensidade de fluorescencia, no domínio das frequências.
- Para isto, modula-se a emissão à mesma frequência. 
- Ora a emissão não segue exatamente o espectro de excitação. Podemos medir uma diferença de fase, que está associada ao decaimento da intensidade.
- Amostras podem apresentar perfis de decaimento muito complexos. Medições no domínio do tempo visam entender o decaimento.
- Para uma amostra com decaimento exponencial, o tempo de vida (lifetime) é definido como o tempo que passa até a intensidade cair para $1/e$ do valor inicial.
    - No domínio de frequência, o tempo de vida aparente ($\tau_\phi$) pode ser determinado com a fase ($\phi_\omega$) OU com o tempo de vida aparente determinado com modulação $\tau_{m}$
    - Os tempos de vida são específicos da amostra, mas não dão informação sobre o decaimento
    - O tempo de vida medido depende do método, de forma que normalmente $\tau_\phi\neq\tau_m$
- Neste documento explicam os métodos e tecnologias usados para fazer fluorometria com frequências (FD - Frequency Domain). Estudam que podem ser obtidos dados até 10GHz.

**Mais a fundo**
- Consideremos que uma amostra fluorescente é excitada com um pulso de luz descrito por um delta de Dirac
- A evolução temporal da intensidade de emissão será:
$$I(t)=\sum\limits_{i}\alpha_{i}e^\frac{-t}{\tau_{i}}$$
(isto é uma *multi-exponencial*, $\alpha_{i}$ são os fators pre-exponenciais e $\tau_{i}$ são os tempos de decaimento)
- Se o decaimento ocorre de acordo com só 1 tempo de decaimento ($\tau_{i}=\tau_{j}$), é fácil medir. Se esse tempo for longo, teremos que $\log I(t)\propto t$ e o tempo de decaimento é o declive.
- Mas consideremos agora que temos uma função de decaimento que depende de 2 tempos bastante diferentes: $I(t)=0.8e^{-t/5}+0.2e^{-t/20}$
![[decaimento multi exp.png]]
podemos ver ainda os $\log I$ para os 2 tempos, vemos que é bastante diferente.
![[decaimento multi exp desmos.png]]

- Se tivermos tempos com um espaçamento de $<20\%$, a diferença entre uma multi-exponencial e uma exponencial com o tempo médio é visualmente indistuinguível. De tal modo que espaçamentos tão reduzidos não podem ser determinados com medições TD e FD (domínio tempo e freq).
    - Mais concretamente, é difícil resolver somas de exponenciais porque os parâmetros estão mutio correlacionados.
    - Por essa razão precisamos de muita intensidade luminosa para tentar determinar. Isto faz com que tenhamos um alto SNR
- Temos a intensidade steady-state (intensidade luminosa quando o material está excitado, se ficar assim algum tempo - acho eu). A porção de intensidade associada a cada componente muti-exponencial é dada por:
$$f_{i}=\frac{\alpha_{i}\tau_{i}}{\sum_{k} \alpha_{k}\tau _{k}}$$

- O modelo multi-exponencial permite estudar quase todos os tipos de decaimento. Mas, dependendo da amostra, $\alpha_{i},\tau_{i}$ podem NÃO ter significado físico.
- Consideremos que temos 2 fluoróforos (fluorophores). Nesse caso:
    - Cada $\tau_{i}$ é o tempo de decaimento de cada um
    - $f_{i}$ é quanto cada um contribui para a intensidade total

## 5.1 - Teoria de Fluorometria FD
- Em medições TD a fonte de excitação é uma fonte de luz pulsada. Em medições FD é uma fonte de luz com intensidade modulada.
- Existe um ligeiro delay entre a absorção e a emissão. Assim, usamos a modulação para poder ter sinais que medem a emissão e a excitação. Consideremos uma frequência de modulação $\omega$ (radianos/s).
- A diferença de fase entre excitação e emissão é medida, sendo $\phi_\omega$. A resposta da emissão da amostra terá desmodulação por um fator $m_{\omega}$.
![[excitacao vs emissao.png]]
aqui temos uma amostra com decaimento de 5s. A azul temos a fonte modulada, com várias frequências. A verde temos a resposta da amostra.
- Isto acontece porque o lifetime de excitação é finito. Assim, a emissão nunca consegue acompanhar a excitação (fonte). Conforme aumentamos a frequência, torna-se mais difícil acompanhar e vamos perdendo cada vez mais pico-a-pico.
- A diferença de fase e desmodulação da emissão dependem da relação entre o lifetime ($\tau$) e a frequência de modução ($\omega$). Isto é visível na figura acima.
- Assim, usando a relação entre $\phi,m$ e $\omega$ podemos determinar o tempo de decaimento da amostra.

**Mais teórico**
- Vamos agora ver a razão porque ocorre diferença de fase e desmodulação de um ponto de vista mais teórico.
- Consideramos 1 fluorosforo. Vejamos a intensidade de excitação ao longo do tempo e o tempo de vida do fluorosforo.
- Consideremos que o fluorosforo está excitado em $t=0$. Temos $\omega$ de 2.5MHz, tendo-se um período de 400ns.
    - A esta frequência, o decaimento de intensidade basicamente não é visível com os olhos. Assim, a emisão segue a excitação bastante bem -  temos $\phi,m$ baixos.
    - Imaginemos que se aumenta a frequência, para algo tipo 250MHz. Agora o fluoroforo nunca deixa de estar excitado, pelo que a emissão que faz é a *média* da intensidade da fonte, apanhando-se vales e picos. Assim $\phi,m$ aumentam bastante.

**A medição em si**
- A medição FD consiste em medir $\phi,m$ para várias frequências $\omega$. Estes dados são a resposta de frequência da amostra.
- Podemos ver os valores caraterísticos destas variáveis em função da frequência:
![[dados 1 exp.png]]
- A fase é as linhas que sobem com o aumento da frequência, a demodulação é as curvas que descem.
- A fase vai de 0º a 90º com a frequência. Ora, paraser mais concreto : isto é o caso de UM fluoroforo. Assim, num decaimento multi-exponencial a fase na verdade pode ir muito acimda de 90º.
- A modulação vai de 1 até 0 (100% ate 0%). Tende para zero quando a frequência é muito maior que o rate de emissão (a emissão não consegue acompanhar).
- Normalmente apresentamos os dados em Hz ou MHz. Podemos usar radianos/s (2$\pi$ x Hz) nos cálculos.

**1 Exponencial**
- No caso de um decaimento descrito por 1 exponencial temos:
$$\tan\phi_{\omega}=\omega \tau~~~~;~~~~ m_{\omega}=\frac{1}{\sqrt{1+\omega^{2}\tau^{2}}}$$

**Multi-Exponencial**
- Para um decaimento multi-exponencial teremos algo do tipo:
![[dados 2 exp.png]]
- Pode-se fazer ajuste dos dados com métodos least-squares. Temos acima o resultado que se obtém ao ajustar estes daddos a um modelo de 1 e 2 exponenciais.
- As frequências que temos de varrer para determinar as exponenciais dependem dos tempos de vida.
    - De uma forma geral, queremos todo o range de frequência em que a fase varia. Ou seja, temos algo assim:
![[range de medicao de tau.png|425]]
 
## 5.2.8 - Medições FD
- Medições FD consistem em comparar as emissões da amostra e umas emissões de referência.
    - A emissão de referência é normalmente medida da luz refletida, scattered ou da fonte
    - A emissão da amostra é o que o nome indica
- Consideremos então que se mede a luz emitida pela amostra e pelo scatterer (?). Como estes são emitidos em tempos diferentes, medimos os dois em relação ao PMT de referência
![[excitacao vs emissao fase.png]]
**Fase**
- Começamos por medir a diferença de fase entre o scatterer e a referência ($\phi_{1}$) - esta deve-se a delays eletrónicos na emissão de luz. Depois medimos a fase entre a amostra e a referência ($\phi_{2}$)
- Conforme a figura acima, a fase associada ao comportamento de fluorescência é $$\phi_{\omega}=\phi_{2}-\phi_{1}$$

**Modulação**
- Não é costume medir a modulação do canal de referência. 
- A medição de modulação é determinada assim:
![[excitacao vs emissao modulacao.png]]
aqui tanto dá usar medições pico-a-pico ou RMS.

- Podemos dividir todos os valores de modulação medidos pela modulação da referência, servindo como uma espécie de correção. Isto pode ser usado se a modulação/amplitudes variar durante a medição devido a instabilidades da fonte ou modulação.

## 5.5.2 - Excitação com LEDs
- LEDs podem ser modulados para ter frequências na ordem de centenas de MHz.
- No livro mostram gráficos de dados obtidos ao excitar amostras químicas/biológicas com LEDs. Os dados estão bons. Diz-se que o LED conseguiu ir até 300MHz.
- LEDs têm várias vantagens
    - permitem obter instrumentos de medição mais baratos
    - o seu espectro concentrado permite excitar amostras metálicas com precisão

## 5.11.1 - Relação entre $\tau,\phi,m$
- Temos as equações:
$$\tan\phi_{\omega}=\omega \tau ~~~~;~~~~ m_{\omega}=\frac{1}{\sqrt{1+\omega^{2}\tau^{2}}}$$
vejamos as suas deduções.

**Versão 1**
- Consideremos que a excitação é fornecida por uma fonte de luz modulada de forma sinusoidal:
$$L(t)=a+b\sin\omega t$$
tal que $b/a=m_{L}$ (modulação da luz incidente)
- A emissão de fluorescência será também sinusoidal e com a mesma frequência, mas com fase:
$$N(t)=A+B\sin(\omega t-\phi)$$
em que $B/A=m_{N}$

- A intensidade de luz emitida num instante $t$ é proporcional ao número de moléculas no estado excitado (descrito por  $N(t)$). 
    - Temos $I(t)=I_{0}e^{-t/\tau}$ (considerando um modelo de 1 exponencial)
    - Ora, a quantidade de moléculas no estado $N$ será: $\frac{dI}{dt} =-\frac{I}{\tau}+L$
    - Substituindo $I=N$ (?) ficamos com: $$\omega B\cos(\omega t-\phi)=- \frac{1}{\tau}[A+B\sin(\omega t- \phi)] + a+b\sin(\omega t)$$
    - Acho que se fizermos expansão de Taylor dos cossenos e senos obtemos: 
$$\begin{align*}
a&= \frac{A}{\tau}\\
\omega\cos\phi&= \frac{\sin\phi}{\tau}\\
\omega\sin\phi+\frac{\cos\phi}{\tau}&= \frac{b}{B}
\end{align*}$$
- Da 2ª equação temos: $$\tan\phi=\omega \tau$$
- Somar o quadrado das equações 2 e 3 resulta em:
$$\omega^{2}+ \left(\frac{1}{\tau}\right)^{2}=\left(\frac{b}{B} \right)^{2}$$
e como $A=a\tau$ (1ª equação) ficamos com:
$$m=\frac{B/A}{b/a}=\frac{1}{\sqrt{1+\omega^{2}\tau^{2}}}$$

**Versão 2**
- Outra forma de definir a intensidade da luz é o integral de *convolução*:
$$I(t)=\int_{0}^{+\infty} L(t')I(t-t')dt'$$
como $I(t)=I_{0}e^{-t/\tau}$ e $L(t)=a+b\sin(\omega t)$. Podemos usar aqui cossenos porque dá mais jeito e é apenas uma questão de fase da fonte, que não interessa:
$$I(t)=I_{0}\int e^{-t'/\tau}(a+b\cos(\omega t-\omega t'))dt'$$
fazendo o integral temos
$$I(t)=I_{0}\left[a + \frac{b}{\sqrt{1+\omega^{2} \tau^{2}}}\cos(\omega t-\phi)\right]$$
daqui temos obviamente $m_{\omega}$.