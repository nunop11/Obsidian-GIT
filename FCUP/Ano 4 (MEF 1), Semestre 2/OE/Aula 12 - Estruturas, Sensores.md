# Fibras óticas fotónicas
- Este tipo de fibras também são chamadas de *fibras óticas microestruturas* - temos túneis de ar cilindricos ao longo da fibra. Eles estão em estruturas periódicas
- O núcleo da fibra é um *defeito* nesta estrutura. Pode ser um tunel maior ou inexistente. Dizemos que temos tuneis de diâmetro $d$ e com espaçamento $\Lambda$ (pitch):
![[fibras fotonicas.png]]
- Para estas 3 fibras temos (esquerda para a direita):
    - Núcleo solido e bainha do mesmo material, coberta de tuneis de ar com diametro $d\ll\lambda$
    - Nucleo solido rodeado de bainha do mesmo material com diametro $d\sim \lambda$
    - Nucleo é um tunel de ar 

## Guiagem
### Índice efetivo
#### $d\ll\lambda_{0}$ (figura 1)
- A luz não "vê" os orifícios. Para a luz, temos o núcleo de material $n_{1}$ e na bainha temos um índice $n_{2}<n_{1}$ que consiste na *média pesada* das partes da bainha com material $n_{1}$ e das zonas com ar ($n_{ar}$)
- Temos reflexão total e tudo acontece como em fibras "normais"
- Ou seja, é como se os buracos fossem **dopantes negativos** AKA baixam o índice de refração da bainha
- O diametro dos buracos pode variar mas tem sempre que se $\ll\lambda_{0}$

#### $d\sim\lambda_{0}$ (figura 2)
- Agora a luz já vai interagir bastante com os buracos
- Cada interação luz-buraco afeta muito o comportamento global. Assim, na região dos buracos temos alterações de índice efetivo conforme o ratio de área de fibra VS área de buraco (como no caso atrás). 
- Mas agora temos um comportamento que é *muito dependente do comp onda*, ou seja, temos um meio **muito dispersivo**:
$$n_{2}\equiv n_{2}(\lambda)$$
- Mas temos algo bom: este tipo de estrutura consegue guiar luz *monomodo* no regime IF ou UV.
    - Esta propagação é monomodo quando $V_\text{eff}<2.405$ (como vimos para fibras normais) e quando $\frac{d}{\Lambda}<0.15$

### Photonic bandgap (figura 3)
- Temos então o núcleo a ser um tunel de ar!
- Ficamos com um caso oposto ao normal: $n_{1}=n_{ar}<n_{2}$. Isso quer dizer que é impossível ter propagação de luz por reflexão total

**Propagação - como?**
- A sobreposição das funções de onda dos átomos da bainha causa uma *interferência destrutiva*. Isto eventualmente faz com que a luz não se consiga propagar na bainha. Numa fibra normal isto não acontece porque não temos os tuneis.
- Assim, a luz TEM que se propagar no núcleo!!!
- Caraterísticas desta técnica:
    - Propagação no ar == poucas perdas
    - Se fizermos quase vácuo no núcleo, não temos interação luz-matéria mesmo que o feixe seja muito itenso (normalmente teriamos efeitos nao lineares)
    - Em fibras normais é dificil propagar luz UV porque ela altera as propriedades do material. Em fibras de guiagem bandgap não temos esse problema
    - Podemos guiar luz com comps onda para os quais não existem materiais transparentes (ar é transparente a tudo)
    - Podemos encher o nucleo com um gás, o que nos permite detetar a propagação: **sensorização**

- Desvantagem enorme:
    - É muito dificil fazer extensões longas destas fibras de forma uniforme

- Assim, estas fibras são usadas como elementos óticos. Nomeadamente: fontes de luz baseadas em fibras, sensores e outras coisas de fotónica.

# Estruturas em fibra
## Coupler direcional
- AKA acoplador direcional
![[coupler 1.png]]
- A luz entra e é distribuida pelas saídas, conforme a extensão da região de acoplamento.
- Podemos ter couplers 1x2 ou 1xN (2 ou N saídas, com 1 entrada só)

## Polarizador em fibra
- A logica geral é: introduzimos algo que causa altas perdas nas direções de polarização que não podemos E baixas perdas na direção correta.
![[polarizador em fibra.png]]

## WDM
- AKA Wavelength Division Multiplexer
![[wdm.png]]
- A conjugação de modos de diferentes comprimentos de onda garantem que em P2,P3 apenas temos 1 comprimento, mas em P1 temos os dois

## FBG
- AKA Rede de Bragg em Fibra
![[fbg.png]]
- Luz entra. Depois, conforme o espaçamento entre picos da rede ($\Lambda$) apenas luz com um comprimento de onda $\lambda_\text{Bragg}$ é refletida. O resto do feixe segue para a frente.
- Temos que:
$$\lambda_\text{refletido}=\lambda_\text{Bragg}=2n_{eff}\Lambda$$

## LPG
- AKA Redes de período longo, em fibra
![[lpg.png]]
- É parecido ao caso de FBG, mas com $\Lambda$ maior. Eles fazem os modos da fibra passarem a ser *modos de cladding* e depois são perdidos por absorção na bainha
- Isto faz com que "desapareçam" certos comprimentos de onda
![[lpg efeito.png]]
- Temos ressonância (maior transferência de energia do núcleo para a bainha) (maior perda de energia do núcleo) para modos em que temos:
$$\lambda_\text{ressonancia}=\left[n_{c}(\lambda) - n_{cl}^{M} \right]\Delta$$
em que $n_{c}$ é o índice de refração do núcleo e $n_{cl}^{M}$ é o índice de refração efeitvo de um modo $M$ na bainha.

## AWG
- Arrayed waveguide grating
![[Attachments/FCUP/A4S2/OE/awg.png]]
- Se formos da esquerda para a direita ele funciona como *multiplexador de comp onda*. Da direita para a esquerda como *desmultiplexador de comp onda*.
- Não percebi bem porquê que ficamos com 1 só comprimento na direita.

## Fibra multi-núcleo
![[fibra multi nucleo.png]]
- Os núcleo são múltiplos, mas estão separados ao ponto de não haver acoplamento/partilha de potência entre eles
- Uma utilização é *sensorização*: 
    - **sensor de curvatura**: ao curvar a fibra, cada núcleo irá ser afetado de forma diferente.

## Interface multi-mono modo
![[interface multi e monomodo.png]]
- Isto é exatamente o que parece. Pode operar nos 2 sentidos
- *Idealmente* cada modo da fibra multimodo é transmitido para uma fibra monomodo

# Sensorização em fibra
- A lógica de fazer medições em fibra é:
![[medicao em fibra.png]]
basicamente, a grandeza que queremos medir entra na fibra na região região de interação e altera a resposta otica.

- Assim, temos que:
    - variação $\vec{k}\cdot\vec{r}$ = sensor interferométrico
    - variação $\omega$ = sensor efeito doppler
    - variação $\lambda$ = sensor comp onda
    - variação $\vec{E}_{0}/|\vec{E}_{0}|$ = sensor polarimétrico
    - variação $|\vec{E}_{0}|$ = sensor intensidade

- Sensores podem:
    - medir em 1 ponto: single-point sensor
    - medir em vários pontos espalhados pela fibra: multi-point sensor
    - medir numa região da fibra: distributed sensor

## Modulação da Intensidade
- Sensores que se baseiam em fazer medições de intensidade luminosa quando algo é feito à fibra que altera essa propriedade:
    - geração de micro curvas
    - aplicação de pressão
    - etc

- Importante garantir que a variação do sinal APENAS se deve à grandeza que estamos a medir

## Modulação polarização da luz
- Baseiam-se em efeito de Faraday $\phi=VLB$
![[sensor modulacao polarizacao exemplo.png]]

## Modulação fase da luz
![[michelson.png]]
- Temos uma fonte $U_\text{fonte}$. Depois do divisor temos o sinal que vai em frente (Ref - $U_r$) e o que é refletido (Sinal - $U_{s}$)
- Temos $\Delta \phi\equiv \phi=\frac{4\pi}{\lambda_{0}}(n_{r}L_{r}-n_{s}L_{s})$ e temos o campo elétrico
$$U_{E}=\alpha \left[U_{r}e^{i\omega t} + U_{s}e^{i(\omega t+\phi)} \right]$$
- Dá para deduzir que, do vetor Poynting:
$$\begin{align*}
I&= U_{E}U_{H}=\eta (U_{E}+U_{E}^{*})^{2}\\
&= I_{r}+I_{s}+2 \sqrt{I_{s}I_{r}}\cos(\phi(t))
\end{align*}$$

**Deslocamento no espelho 1**
- Neste caso, as diferenças de caminho ótico geral uma fase como antes: $\phi_{0}= \frac{4\pi}{\lambda_{0}}(n_{r}L_r-n_sL_s)$
- Consideremos que dentro do espelho 1 (sinal refletido) temos um deslocamento $\ell_{s}\sin(\omega_{s}t)$
    - Definimos $\phi_{0}=\frac{4\pi n_{s}\ell_{s}}{\lambda_{0}}$ e temos $$\phi(t)=\phi_{0}-\phi_{0s}\sin(\omega_{s}t)$$
- A equação final fica igual mas muda $\phi(t)$

*Procedimento*
- Num detetor iremos medir a tensão $V_\text{out}=V_{0}[1+C\cos(\phi_{0}-\phi_{0s})\sin(\omega_{s}t)]$
- Expansimos $\cos(\phi_{0s}\sin(\omega_{s}t)), \sin(\phi_{0s}\sin(\omega_{s}t))$ em termos de funções de Bessel. 
- Se estivermos a medir pequenas variações ($\phi_{0s}\ll1$, caso mais comum) e removermos a componente DC, ficamos com $V_\text{out}=\gamma \phi_{0s}\sin(\omega_{s}t)$ em que $\gamma=V_{0}C$

### Quadratura
![[quadratura.png]]
- Garantimos que $\phi=\frac{\pi}{2}(2m+1)$ é cumprida - temos quadratura!
- Isto permite que pequenas variações de fase $\delta \phi$ causem altas variações de $V_\text{out}$. Isso quer dizer que temos máxima sensibilidade!

**Exemplo**
- No braço de sinal podemos ter uma extensão de fibra exposta a sinais sonoros. Isto vai consar micro deformações, que causam pequenas alterações na fase
- Se o sistema estiver em quadratura, estas variações são detetadas
- A intensidade de saída muda, sendo proporcional à deformação causada pelo som

### Tipos
- Michelson (em fibra)
- Mach-Zhender (em fibra)

### Largura de sinal
- Voltemos ao michelson, que temos no exemplo do deslocamento no espelho. 
- Essa dedução assume que temos 1 só comp onda/frequência no sinal
- Quando temos mais: cada frequência gera um padrão de interferência diferente.
    - O padrão observado é a soma de todos esses
![[efeito de pico  largo.png]]
- Definimos $\tau=\frac{\Delta L}{c_{0}}$ e $\gamma_{sr}(\tau)$ a função de coerência mútua (determina a visibilidade das oscilações de $V_\text{out}$)
- Além disso, o ângulo $\theta$ entre as polarizações dos sinais r,s afeta o sinal medido. Assim, temos
$$C=\gamma_{sr}(\tau)\frac{2 \sqrt{I_{r}I_{s}}}{I_{r}+I_{s}} \cos^{2}\theta$$

## Modulação comp onda da luz
- Comp onda é absoluto (não precisamos de canal de referência)
- Fazemos uma fibra com um FBG: $\lambda_\text{reflet}=\lambda_\text{Bragg}=2n_{eff}\Lambda$
- Com estas redes podemos ver diferentes respostas espectrais:
    - conforme o parametro $\Lambda$
    - conforme a diferença de fase entre 2 FBGs

**Laser**
![[modulacao comp onda exemplo.png]]
- Num sistemas destes, podemos sintonizar automaticamente o filtro para ficar em fase com a FBG. Isto cria uma cavidade ótica e temos um laser em fibra

**Multiplexer**
- Usando várias FBG, cada uma com um comp onda de reflexão específico, podemo fazer com que para trás apenas vão os comps onda que queremos e para a frente removemos esses.

## Scaterring
- A temperatura ou tensão (mecânica/deformação) aplicada na fibra alteram as propriedades de espalhamento 
    - Ao medir e processar o sinal podemos inferir estas 2 propriedades

- Temos espalhamento linear (Rayleigh) e não-linear (Raman e Brillouin)

### Rayleigh
- Espalha a luz em todas as direções
- Emitem-se pulsos de luz. Para um certo pulso (pensa em OTDR), em cada instante um sinal recebido de volta foi refletido num certa distância depois da fonte

### Brillouin
- Quando a potência é muito alta, temos comportamento não linear
- Continuamos a ter o espalhamento de Rayleigh, mas acrescentam-se os espalhamentos não lineares
- Física: o campo elétrico (feixe de luz) é tão forte que consegue polarizar o vidro (cria dipolos no dielétrico) e geram-se tensões de compressão ou expansão. A fibra muda de dimensões
- Estas deformações são mais lentas que o campo EM. Geram-se então oscilações acusticas em torno de uma frequência $\Omega$ reduzida
- Estas ondas interferem com as ondas oticas e geram maior intensidade para trás, a uma frequência $\omega_{p}-\Omega$:
![[espalhamento brillouin e rayleigh.png|221]]

- A onda ótica com freq $\omega_{p}$ sobrepõe-se com a onda espalhada Brillouin de freq $\omega_{p}-\Omega$ e geram uma *onda de batimento* com freq $\Omega$.
    - Esta é reforçada pela onda acústica do efeito visto antes e temos uma **grande modulação do ind refração**
    - Isso aumenta a intensidade da radiação espalhada
- O desvio $\Omega$ entre a luz espalhada e a do feixe EM depende da tensão mecânica do material e da temperatura.

### Raman
- Ver apontamentos de ótica
- Basicamente, luz incide e excita eletrões. Quando descem de nível emitem fotões. Isto cria uma nova componente de luz com um desvio de frequência da luz original
    - Stokes: $\nu-\delta \nu_{R}$
    - Anti-stokes: $\nu+\delta \nu_{R}$

- A sobreposição das ondas incidente (freq $\nu$) e as ondas stokes e anti-stokes resulta em ondas batimento com frequências $2\nu\pm\delta\nu_R$ e $\pm\delta\nu_R$
    - As ondas $\pm\delta\nu_R$ eventualmente sobrepõe com as ondas $\nu\pm\delta\nu_R$ e reforçam-nas

*Aplicação*
- O pico Stokes depende muito da temperatura (maior temp = maior pico)
- O pico Anti-stokes não depende da temperatura
- Ao estudar o rácios das suas intensidades, podemos definir um parametro $R$. Conhecendo-o em algumas temperaturas, podemos estimar a temperatura.

