![[grandezas espectrometria.png]]

- **Espetro (Luminoso/Ótico):** descrito por uma curva Energia VS Frequência $G(\nu)$
- Frequências óticas são da ordem $\nu\sim 10^{14}Hz$. Logo temos $\lambda\sim 1\mu m$. Podemos então definir as cores como limitadas entre os valores:
![[cores e comps onda.png]]

## Espetros e interação luz-matéria
- Quando materiais absorvem radiação eletromagnética, alguma energia é absorvida. A energia em excesso é emitida de volta quando o material volta ao estado fundamental, sob a forma de fotões. Isto pode ocorrer duma vez ou aos poucos.
- Consideremos que um material é exposto a radiação eletromagnética/luz. Se o material for (semi) transparente à radiação, o fenómeno de absorção de radiação irá influenciar o espetro de emissão. Se o material é opaco à radiação, podemos estudar o seu espetro de emissão.

### Tipos de espetros
**Contínuos**
- Quando obtemos um traçado contínuo :)
- Casos comuns são chamas e lâmpadas incandescentes.

**de Riscas**
- Comum para gases monoatómicos.
- O espetro de emissão corresponde às transições de nível dos eletrões no átomo.
- Podemos obter o espetro de absorçao ao expor a amostra a um contínuo de frequências e registar o espetro que ela emite. 
- O comprimento de onda da radiação emitida/absorvida é dado por:
$$\lambda_{0}=\frac{hc}{\Delta E}$$em que $\Delta E$ é a energia associada à transição eletrónica.

**de Bandas**
- Quando se tem muitas riscas, quase indistinguíveis.
- Comum para moléculas. Porque além dos níveis energéticos dos átomos, as moléculas têm os seus estados de vibração e rotação próprios.
- Quanto maior for a molecula, mais juntos estão os subníveis energéticos associados a vibração e rotação da mesma. Transições entre estes causam emissões IF ou microondas.

### Constante decaimento Fotoluminescente
**Fotoluminescência** - emissão de luz pela emissão de átomos por fotões.
- Dentro disto temos fenómenos como **fluorescência** e **fosforescência**. Ambos estes consistem em o material emitir a energia em excesso obtida dos fotões através de uma série de transições eletrónicas *em cadeia*. Na fluorescência isto ocorre com vida curta: $10^{-9}- 10^{-11}s$; na fosforescência ocorre com vida mais longa (podendo chegar a segundos ou minutos)

- Para um material exposto a radiação excitante, mal esta é desativada temos que a intensidade da radiação fluorescente emitida é dada por:
$$I=I_{0}e^\frac{-t}{\tau}$$
em que $I_{0}$ é a intensidade de luz emitida por fluorescencia em $t=0$ e $\tau$ o tempo caraterístico de desexcitação.

- Sendo o rendimento dado por 
$$\eta= \frac{\textsf{\# fotões emitidos por fluorescência }}{\textsf{\# fotões absorvidos}}<1$$

- O estudo do decaimento da intensidade de fluorescencia permite determinar $\tau$.

## Espectrómetros
### Dispersão cromática $n(\lambda)$
- O indice de refração exprime $v/c$ e depende da frequência da radiação. A dispersão cromática faz uso disto.
- Usando um prisma de material transparente, consegue-se separar as diferentes cores que formam a luz branca.
- Na atividade iremos usar um **espectrometro de desvio constante**. Neste, temos que rodar o prisma para variar a frequência que vemos AKA temos que medir cada comprimento de onda individualmente.

### Dispersão Inferométrica
- Usado em sistemas de elevada resolução
- Basicamente é como um espetrómetro de dispersão cromática, mas invés do prisma temos uma rede de difração (que pode funcionar em transmissão ou reflexão)
- Nesta atividade iremos usar um FOS - Fiber Opctic Spectometer. A luz vem de uma fibra ótica, passa por um espelho e chega a uma rede difratora refletiva. Daí a luz é dispersa e chega a um detetor.

### Medidas Espectrais
- Para amostras não luminescentes, é preciso que ela seja iluminada por uma fonte estável, conhecida.
![[teoria t6 - 1.png]]
![[teoria t6 - 2.png]]
em que $I_{ref}$ é o espetro da iluminação de referência, $I_{dark}$ é o espetro medido sem iluminação de referência, $I_{R}$ é o espetro de luz refletida e $I_{T}$ espetro de luz transmitida.

## Aquisição automática de sinal
Ocorre com:
    - Estudo de luminescência, porque o decaimento ocorre em $\Delta t\ll 1s$ : recoljemos valores em intervalos discretos $\delta t$
    - FOS, o feixe disperso é recolhido em pixeis
em ambos os casos tornamos feixes contínuos em séries de valores discretos.

### Amostragem
- Na parte da luminescência iremos usar uma montagem eletrónica. Temos um LED na gama violeta e um fotodíodo para captar o sinal da luminescência. Tudo isto esá ligado a um interface de DAQ (Digital AQuisition). Neste é preciso definir
    - Sample rate $f_{s}$ - valores por segundo
    - gama de sinal (range) - intervalo de valores de tensão a digitalizar
    - resolução digital (bit resolution)

# 3 - Preparação
- Não sei nada :))))

# 4 - Procedimento
- Achei o protocolo compreensível uwu

