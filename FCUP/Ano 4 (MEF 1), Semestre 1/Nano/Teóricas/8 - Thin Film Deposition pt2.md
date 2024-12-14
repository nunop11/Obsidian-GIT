# 1 - Evaporação
- Material tem origem num material aquecido, transportado e depositado/condensado num substrato
- Para este transporte funcione de forma eficiente, este processo é feito num vácuo alto, o que reduz as colisões com átomos do ar
- A fonte é aquecida com resistências ou EBeam
- O rate de deposição é decidido por
    - fluxo de átomos de deposição emitidos
    - geometria da fonte e wafer
- O rate de deposição pode ser bastante elevado ($>1 \mu \text{m/min}$)
- O film depositado tem alta aderência, mas é pouco conformal
- Não é usado na indústria
![[evaporacao.png]]

## Distribuição
- A distribuição angular das partículas depositadas são dadas pela *Lei de Cosseno de Knudsen* : $P(\theta)=P_{0}\cos\theta$, em que $\theta$ é o âgulo medido em relação à normal da superfície da fonte de átomos
![[evaporacao angulos.png]]
- Na vida real, os padrões de emissão costumam ser mais direcionais que isto.

**Caso circular**
- Consideremos a figura abaixo, em que temos uma câmara de vácuo circular/esférica. 
![[evaporacao camara circular.png]]
neste caso, as partículas irão incidir no substrato com um ângulo $\theta$. Assim, a quantidade de material depositado é reduzida por um fator de $\cos\theta$ (em comparação ao caso de incendência perpendicular)
![[evaporacao em substrato inclinado.png]]
- Neste mesmo caso, temos:
$$m=C \frac{\cos\theta\cos\theta}{\pi R^{2}}$$
em que: $m$ é a massa depositada, $C$ uma constante. O primeiro cosseno vem da distribuição angular que vimos acima, o segundo cosseno vem do fator com que a deposição diminui com o substrato a um ângulo $\theta$. O denominador tem a ver com ângulo sólido e cenas.
- Podemos ainda escrever
$$m\propto \frac{1}{4\pi r^{2}}$$
logo a massa depositada **não** depende do ângulo! Por exemplo, se tivessemos uma câmara circular e fizessemos evaporação, ficaria uma camada da mesma espessura em toda a superfície da câmara.

**Espessura**
- O rate de deposição é de
$$R=\sqrt{\frac{M}{2\pi \rho^{2}}} \frac{P}{\sqrt{k_{B}T}}\frac{A}{4\pi r^{2}}$$
($P$ é a pressão de vapor)
o 1º termo consiste em propriedades dos material, o 2º termo consiste na temperatura e pressão, o 3º termo consiste na geometria da câmara.

**Exemplos**
![[carateristicas evaporacao alguns elementos.png]]

## Método de aquecimento
- **Evaporador térmico** - o calor é gerado com resistências, a única que funciona com material orgânico
- **Evaporador com EBeam** - mais popular, mais caro
- **Evaporador com aquecimento indutivo** - pouco popular

### Evaporação Térmica
- Simples, robusto, muito usado
- Pode ir até ~1800ºC
- Temos coils, recipientes e outras coisas para aquecer o material fonte. Estas coisas de aquecer podem ser feitas de W. Ta ou Mo. Correntes de 20-300A
- Normalmente usasse materiais cuja pressão de vapor é razoável a 1600ºC
- O substrato é exposto a radiação visível-IR
- Contaminação vinda do crucible e da cena usada para aquecer a fonte
![[suporte evaporacao termica.png|475]]
![[tipos suporte evap termica.png|500]]

### Evaporação EBeam
![[evaporacao ebeam.png]]
- Mais complexo, mas muito versátil
- Pode atingir >3000ºC
- A evaporação ocorre num local muito concentrado 
- Ocorre menos contaminação vinda do crucible
- A wafer é aquecida menos

- Mas temos *desvantagens*
    - Geram-se raios X
    - Os rates de deposição podem ser difíceis de controlar
    - A pressão de vapor varia de forma previsível com a temperatura, mas é mais imprevisível face a EBeam

#### Alguns recipientes para aquecer a fonte
![[suportes evaporacao.png]]

### Problemas de evaporação
- Problema **Estequiométrico**
    - Compostos desfazem-se a altas temperaturas
    - Os elementos do composto, agora separados, têm rates de deposição diferentes porque têm pressões de vapor diferentes
    - Isto leva a termos um film depositado com estequiometria diferente da fonte

![[step coverage evaporacao.png]]
- **Step Coverage**
    - Preenche muito pouco ou nada as beiras verticais de degraus
    - O *coeficiente de sticking* é $S_{c}=F_{\text{reagiu}}/F_{\text{incidente}}$
        - Se o coeficiente for alto, o material fica onde acertou ao depositar. Se o coeficiente fr baixo, o material pode espalhar-se
    - No entanto, em certos contextos de R&D, esta propriedade pode ser útil. Isto porque má step coverage implica que temos uma camda boa para liftoff

### Glancing angle deposition
- Se arranjarmos uma combinação material/substrato em que temos $S_{c}$ muito elevado, podemos aproveitar esta propriedade de deposição muito direcionada.
- Com uma configuração como a seguinte, é possível manipular as estruturas criadas:
![[evaporacao substrato a rodar.png]]
e podemos fazer estruturas específicas
![[padroes feitos com evap.png]]

### Monitorizar espessura
![[monitorizacao espessura evap.png]]
- Usamos uma *QCM* (quartz crystal micro-balance)
- Isto consiste num material piezoelétrico, que gera uma corrente AC na sua frequência de ressonância
- Consoante é sujeito a mais massa, a frequência muda
- O cristal não dura muito
- Temos:
$$\Delta T_{r}\propto m_{f}\propto \rho_{f}t_{f}$$
estas coisas são : período de ressonância, massa do filme, densidade do filme, espessura do filme.

### Vantagens e Desvantagens de Evaporação em geral
**Vantagens**
- Rate de deposição pode ser bem alto
- Podemos evaporar quase qualquer elemento
- Ocorre poucos danos na superfície
- Pouca contaminação
- Pouco aquecimento do substrato

**Desvantagens**
- Difícil de controlar
- Alguns materiais têm rate de deposição muito lento
- Mau step coverage
- Danos raios X

# 2 - Epitaxy com Molecular Beam
------- slide 31