## "Linewidth de Ressonância Ferromagnética em filmes metálicos finos : comparação de métodos de medição"

# Abstract
- Para medir a linewidth de FMR (ressonância ferromagnética) usou-se os métodos:
    - SL - stripline
    - VNA - vector network analyzer
    - PIMM - pulsed inductive microwave magnetometer
- Nisto,
    - fez-se medições SL-FMR para a gama de frequências 1.5-5.5 GHz
    - fez-se medições VNA-FMR e PIMM para a gama 1.6-8 kA/m (20-100 Oe)
        - 1 Oe = 1 Oersted = $\frac{1000}{4\pi}$ A/m $\simeq$ 80 A/m

# Intro
- Sistema de armazenamento de dados magnéticos têm atingido rates de transferência de dados mais altos, assim como densidade de armazenamento em área (o artigo é de 2006)
    - exemplo: MRAM (RAM com tecnologia magnética)
- O que permite guardar dados na memória é a capacidade de o campo magnético trocar de valor lógico (switching speed). Ora, esta velocidade é limitada pelo damping magnético dos materiais do filme fino.
- Para medir o FMR e os mecanismos de damping temos 3 técnicas:
    - **SL** - stripline - medir linewidth de FMR ao varrer o campo a uma frequência fixa.
    - **VNA** - vector network analyzer - permite analizar os parâmetros de rede de um sistema elétrico. Mede linewidth a varrer frequência com campo fixo.
    - **PIMM** - pulsed inductive microwave magnetometry - detetar switching magnético de forma indutiva. Usa waveguides para guiar, detetar e processamento digital do sinal. 

- Vantagens e desvantagens:
    - *SL*
        - Simples de fazer
        - Pouca sensibilidade
    - *VNA*
        - aproveita a capacidade de análise de amplitude e fase de instrumentos VNA modernos
        - precisa de uma calibração cuidada e subtração de sinais de referência
    - *PIMM*
        - usa DC para excitação de campo invés de microondas. Obtém dados de decaimento da magnetização que correspondem a uma larga banda de frequências de FMR. Não tem calibração complexa
        - Análise dos dados complexa, requere subtrair o pulso de fundo

- O objetivo deste relatório é comparar as medições de linewidth de FMR medida com os 3 métodos. Para comparar, usou-se a linewidth:
    - medida com varrimento de campo a "half power" de SL-FMR
    - medida com varrimento de frequência de VNA-FMR
    - análise FFT do PIMM

# Os Métodos e os Samples
## SL-FMR
**Resumido**
- Variamos o campo magnético estático para uma frequência de micro-ondas constante
- Obtemos um perfil de absorção de FMR
- A linewidth é $\Delta H_{SL}$ e é a largura a meio máximo
![[curva ressonancia magnetica.png]]

**Como deve ser**
- É usada uma linha de transmissão não-ressonante. Na figura abaixo, isto é a "strip line" (que dá nome ao método LOLLLL)
![[sl.png]]
- O $h, H$ na figura *não* são medições. $H$ é o campo magnético externo gerado pelos imans dos 2 lados do sample. $h$ é o campo micro-ondas.
- Notas:
    - A strip line tem $50 \Omega$, serve para excitar o sample e tem 2 planos de ground
    - Temos 2 isoladores coaxiais (entrada e saída) para reduzir standing wave ratio (isto é o ratio entre ondas refletidas e transmitidas. Se este fosse alto, poderíamos ter ondas a voltar para a fonte micro-ondas e danificá-la)
    - Temos um díodo de schottky (estes díodos têm altas velocidades de switching) que serve para deteção
    - Os amplificadores lock-in e modulation coils servem para obter o perfil "derivada da potência absorvida VS campo"

*Samples e campos*
- O sample é colocado num dos ground planes da strip line - garante homogeneidade do campo microondas aplicado.
- O campo MW fica abaixo de 1 mW para a resposta ser linear
- O campo H aplicado é paralelo à strip line e perpendicular ao campo MW
    - A amostra é anisotrópica. O campo H atua na amostra no "easy axis" (a direção mais fácil de magnetizar o material)

*Dados*
- Os dados experimentais da derivada (devido ao lock-in) costumam ser simétricos e com pouco ruído. Ao integrar numericamente obtemos uma lorentziana:
![[sl dados.png]]
(esta imagem foi obtida para um campo MW a 3GHz)
- Daqui obtemos diretamente $\Delta H_{SL}$ - é simplesmente a largura da curva a meio máximo, como indicado acima.
    - Os erros obtidos estiveram aaixo de  1 Oe
- O campo de ressonância foi de $8.08\pm0.04$ kA/m = $101\pm0.5$ Oe.
- Temos $\Delta H_{SL}=1.5\pm0.04$ kA/m

## VNA-FMR
**Resumido**
- Variamos a frequência micro-ondas com um campo magnético estático fixo
- Obtemos o espetro de absorção FMR a partir da medição de parâmetros  S:
    - *S parameters AKA Scattering parameters* - elementos de uma matriz matemática que descreve o comportamento de um sistema elétrico quando estimulado por sinal elétrico. Com frequências na ordem de GHz é mais fácil medir isto do que correntes e tensões. S parameters descrevem a relação input-output.
- Podemos então medir a linewidth de varrimento de frequências $\Delta f_{VNA}$, também no meio máximo.

**Como deve ser**
- Obtemos os parâmetros de FMR a partir dos S parameters VS frequência MW e campo H.
- Usamos este sistema:
![[vna.png]]
- O campo MW é guiado por um CPW (coplanar waveguide - um tipo de linha de transmissão que tem a strip que carrega o sinal e os planos ground do mesmo lado)
    - Ou seja, o sample (conforme a foto acima) tem o campo MW a passar pela linha central junto a ele, enquanto se mantém em contacto com o ground em cima e em baixo
    - A strip central mede 100um de largura
- O campo H é gerado por Helmholtz coils (os 2 aneis geram um campo magnético uniforme entre eles) e é perpendicular ao campo MW
- A análise do sinal é feita com um instrumento VNA

*Gamas de campos*
- Como já referido, obtemos S para campo H fixo. Foram determinados estes valores para campos fixos na gama 1.6-8.4 kAm. Para cada um foi feito varrimento de frequência até GHz
- Para campos FMR abaixo de 3.72 kA/m o campo de referência (???) foi 8.4 kA/m. Para campos acima de 3.72, colocou-se o campo de referência (???) em 748 A/m
    - Penso que campo FMR é o valor do campo H que geramos. O campo referência é o valor de campo H que usamos para comparar os dados à teoria?

*Análise*
- Baseando num modelo de Barry (?) em que assumimos que o modo dominante no CPW é o modo TEM (modo transverso), o parâmetro de permeabilidade MW é:
$$U(f)=\pm \frac{i \ln\left(\frac{S_{21-H}(f)}{S_{21-ref}(f)}\right)}{\ln(S_{21-ref}(f))}$$
(o sinal serve para que a componente imaginária disto seja negativa perto do pico de FMR)
- $S_{21-H}$ é o parâmetro $S_{21}$ no campo FMR
- $S_{21-ref}$ é o parâmetro $S_{21}$ no campo de referência

- Idealmente, $\text{-Im}(U)$ VS $f$ seria o perfil de perdas FMR. $\text{Re}(U)$ VS $f$ seria o perfil de dispersão.
![[vna dados.png]]
(estes dados correspondem a um campo H fixo de 3.22 kA/m) (No canto superior direito temos a curva teórica de perda)
- Colocou-se o eixo easy do sample alinhado com a linha do CPW.
- Notemos que no gráfico acima é evidente que os traçados de $-\text{Im}(U),\text{Re}(U)$ não representam os perfis de perda e de dispersão como esperado.
    - -Im(U) não é simétrico e chega a atingir valores negativos
    - Re(U) foge muito do traçado previsto para frequências >2.3GHz
- Estes desvios têm 2 razões:
    1. Ao determinar a proximidade dos valores de campo FMR e de referência desprezamos a presença de *reflexões*. 
        - Isto faz com que tenhamos offsets e distorções. Estas devem-se ao facto que temos resposta FMR embebida nos dados de referência.
        - Faz ainda com que nas medições se misture as componentes real e imaginária da susceptibilidade real $\chi(f)$.
    2. ???

*Ajuste*
- A susceptibilidade complexa a uma frequência $f$, num filme fino magnetizado ao longo do eixo easy, pode ser escrita em FMR como:
$$\chi(f)=\left(\frac{|\gamma|\mu_{0}}{2\pi}\right)^{2}\frac{M_{S}(H_{ext}+H_{k}+M_{S})}{f_{res}^{2}-f(f-i\Delta f_{VNA})}$$
em que: $M_{S}$ é a magnetização de saturação, $H_{k}$ é o parametro de rede de  anisotropia uniaxial, $f_{res}$ é a freq de ressonância, $\gamma$ é o ratio giromagnético do eletrão, $\Delta f_{VNA}$ é a frequência de linewidth - aquilo que queremos saber.
- Assim, para determinar $\Delta f_{VNA}$ foi feito o seguinte ajuste dos dados:
$$U_{fit}(f)=C[1+\chi_{0}+\chi(f)e^{i\phi}]$$($C$ é uma constante real, $\chi_{0}$ é uma constante de offset complexa, $\phi$ é o ajuste de fase)
- Além de $\Delta f_{VNA}$, estas equações permitem obter $f_{res}$. Assim, foi feito o ajuste real e imaginário. As linhas "normais" por detrás das bolas no gráfico acima consistem ao ajuste feito - vemos que parece correto.
    - Foi então determinado $f_{res}=2$ GHz, $\Delta f_{VNA}=236\pm12$ MHz.

## PIMM
**Resumido**
- Aplicamos um campo magnético de excitação transverso (perpendicular) ao campo estático, na forma de impulso.
- Detetamos a resposta na magnetização $m(t)$ e fazemos FFT para obter $m(\omega)$. 
- Do perfil de magnetização podemos medir $\Delta f_{PIMM}$ a meio máximo.

**Como deve ser**
- Neste método determina-se os parâmetros de perda do material ferromagnético através do decaimento da magnetização dinâmica em resposta a um campo magnético pulsado (invés de campo MW!)

![[pimm.png]]
(o sample é colocado num CPW, tudo ligado como no VNA. A tira central da CPW mede  220um)
- Novamente, o filme foi colocado com o eixo easy paralelo à tira do CPW
- $H_{ext}$ continua a ser o campo "horizontal" gerado pelos coils A - serve para gerar o campo estatico perpendicular a $h$. Assim, ele controla a resposta de ringing e a medição
- Mas agora $h$ é o campo pulsado, proporcionado pelo CPW. 
- Temos ainda os coils B. Estes geram um campo estático, que permite obter um sinal de referência se ocorrer ringing.

![[pimm dados.png]]
- Estes dados foram obtidos para campos A na gama 1.6 - 8 kA/m
- O campo pulsado do CPW têm tempo de rise de 50ps e duração de 10ns. A amplitude máxima é 64 A/m.
- A combinação de campos estáticos e pulsados permite ter uma reposta linear.

- A resposta da magnetização dinâmica à subida inicial do campo pulsado é medida em 4 passos:
    1. Temos um campo B $H_{B}$ de 5.6 kA/m a ser aplicado para saturar o filme na direção hard.
    2. Colocado $H_{B}$ a zero. Aplicar $H_{A}$ (na direção easy). Aplicar o campo pulsado $h(t)$ e medir $V_{A}(t)$ por tempos 0.5ns antes da 1ª subida do pulso até 10ns depois da subida
    3. Colocado $H_{A}$ a zero. Aplicar $H_{B}$ a 5.6 kA/m. aplicar $h(t)$ e medir $V_{B}(t)$
    4. A resposta à subida do pulso é $V_{R}=V_{A}-V_{B}$ (resposta de ringing)
    5. Fazer FFT de $V_{R}$ (ver imagem acima). Isto permite obter os perfis de absorção e dispersão VS frequência.

- Com este método determinou-se $f_{res}=2.53\pm0.05$ GHz, $\Delta f_{PIMM}=236\pm11$ MHz. Isto é bastante concordante com os resultados de VNA

## Samples
- Usamos samples de Permalloy (80% Ni, 20% Fe).
- O alloy é feito com deposição com técnica de sputtering em subestratos de vidro de 1x1 cm2 (com um uma camada de 5nm de Ta - Tantalo)
- Os filmes foram depositados à temperatura ambiente e sob um campo de 2kA/m (25 Oe)
    - Usou-se 2 samples de 50 nm (S50A, S50B) e um de 100nm (S100).
        - S50A usado para SL-FMR
        - S100 usado para PIMM
        - S50B usado para VNA-FMR
- Os filmes tinham anisotropia 

## Relações de Linewidth de campo e frequência
- Como vimos, SL-FMR dá-nos uma linewidth de varrimento de campo (a frequência constante) e VNA-FMR e PIMM dão-nos linewidth de varrimento de frequência.
- Ora, a linewidth é uma medida das perdas do campo MW. Como podemos confirmar que estes tipos diferentes de medição são compativeis?

- Uma forma é usar a curva campo FMR vs Frequência e converter todas as linewidths em campo ou frequência.
- Para um filme fino com anisotropia uniaxial e magnetizado por um campo $H_{ext}$ segundo o eixo easy, temos a frequência FMR de Kittel:
$$f_{kittel}(H_{ext})=\frac{|\gamma|}{2\pi}\mu_{0}\sqrt{(H_{ext}+H_{k})(H_{ext}+H_{k}+M_{S})}$$
esta relação pode ser invertida para obter: $H_{kittel}(f)$.
- Vemos que o campo e frequência FMR não ser relacionam linearmente. Isto significa que não temos uma relação linear entre:
    - linewidth $\Delta H$ para uma frequência $f$ e campo FMR  $H_{kittel}(f)$
    - linewidth $\Delta f$ para um campo  $H_{ext}$ e frequência FMR $f_{kittel}(H_{ext})=f$
- Se as linewidths forem reduzidas (em relação ao campo ou frequência) podemos dizer:
$$\Delta f=\Delta H \frac{\partial f_{kittel}(H_{ext})}{\partial H_{ext}}\Biggr|_{H_{ext}=H_{kittel}(f)}=|\gamma|P_{A}(f)\Delta H$$
$$\Delta H=\Delta g \frac{\partial H_{kittel}(f)}{\partial f}\Biggr|_{f=f_{kittel}(H_{ext})}=\frac{\Delta f}{|\gamma|P_{A}(f)}$$
no caso de uma película fina como a nossa temos:
$$P_{A}(f)=\sqrt{1+ \left(\frac{|\gamma|\mu_{0}M_{S}}{4\pi f}\right)^{2}}$$

## Comparações dos métodos
![[fmr data 1.png]]
![[fmr data 2.png]]
- Os 2 gráficos acima mostram os 3 métodos em comparação, conforme colocamos todos em $\Delta H$ ou $\Delta f$.
- SL é representado por círculos pretos, VNA por triângulos pretos e PIMM por círculos brancos.
- Nas conversões usou-se $|\gamma|/2\pi=28$ GHz/T e $H_{k}=480$ A/m.
- Os valores de linewidth são consistentes para todos os casos.

- Podemos fazer um ajuste linear do tipo $\Delta H=\Delta H_{0} + \frac{4\pi\alpha}{|\gamma|}f$
    - Esta equação em específico tem a ver com modelos definidos em outros artigos
- Os ajustes feitos e esta equação, apontam para $\alpha\simeq0.007$ para filmes de 50 e 100nm. Valor comum para filmes metálicos finos com baixa perda.

- Podemos ainda fazer um ajuste não linear: $\Delta f=(|\gamma|\Delta H_{0}+4\pi\alpha f)\sqrt{1+ \left(\frac{|\gamma|\mu_{0}M_{S}}{4\pi f}\right)^{2}}$
- Isto explica o aumento de $\Delta f$ para frequências <3GHz e para o achatar do traçado para frequências >3GHz.
- 