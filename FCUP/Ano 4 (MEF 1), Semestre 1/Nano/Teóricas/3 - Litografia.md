# 0 - Chips
![[chip moderno foto.png]]
![[chip moderno esquema.png]]

- Chips avançados são complexos, com várias camadas. Assim, eles foram ficando maiores.
- Conforme a segunda fotografia vemos logo que as camadas precisam de estar perfeitamente bem alinhadas
- Os avanços em litografia são a principal razão porque a Lei de Moore ainda se aplica. Por isso vamos ver esse tópico melhor

## Como são feitos
- Chips atuais podem ser feitos com vários processos:
    - *litografia* - geral um padrão num photo resist
    - *thin film deposition* (método aditivo) - spin coating, chemical vapor deposition
    - *etching* (método subtrativo) - ion beam etching
    - outros

# 1 - Litografia
## 1.1 - Photolitography
- Este processo pode ser comparado à "revelação" de fotografias. Usando feixes óticos transferimos padrões num polímero fotosensível : o **photoresist** - PR
- Usamos fontes de luz, masks e PR
- Este é o passo mais importante, complexo e caro ao fazer coisas à escala nano
![[caraterisiticas chips.png]]
(a última coluna devia dizer "overlay accuracy" - a precisão com que conseguimos alinhar camadas)

- A mask funciona assim:
![[mask funcionamento.png]]

- O processo de photolitografy planar consiste nisto:
![[funcionamento de pr.png]]

- O processo inclui 20-60 passos e eles têm que estar perfeitamente alinhados. Além disso, é preciso que cada passo tenha distribuições de erro muito reduzidas.
    - Se houver distribuição de erro maior, podemos ter um chip funcional (bom yield funcional), mas noutros chips dentro da mesma batch podemos ter o completo oposto (mau yield parametrico)

- Uma só máquina de Litografia de alta qualidade pode ocupar 2 pisos. O seu laser e lentes têm que ser perfeitos e exatos. 

# 2 - Processo de Litografia
## 2.1 - Substrato
### Wafers
- Substrato fino e circular de Sílica
- Atualmente o tamanho standard é discos de diâmetro de 200mm. Mas existe com 300mm
![[tipos wafers.png]]
(o disco não é bem circular. Pode ter cortes a indicar o tipo de wafer)

- No entanto, estes discos não são feitos de Sílica pura. Existem processos necessários para fazer as wafers.

### Czochralski (CZ)
- Começamos com *electronic grade silicon* - 99.99999999999% (11 9s), que custa cerca de 100€. 
- No entanto, eletronic silicon é poli cristalino. O que queremos para fazer wafers é *ingot silicon*, que é *mono cristalino*.
- Colocamos uma pequena semente, que consiste num cristal de Si, num metal líquido (que é Si líquido).
- A semente é rodada enquanto lentamente é retirada do metal líquido. Entretanto, tudo isto ocorre dentro de um crucibel a rodar no sentido oposto à semente.
- Consoante isto ocorre, o líquido "sobe" e ficamos com um cilindro de ingot sílica com pureza de 6 9s.
![[cz.png]]
- Ao rodar, a seed induz no metal a estrutura certa.
- As zonas "float" têm mais pureza porque nunca entram em contacto com o crucible.

### Float Zone Growth
- Este método consiste em começar com um cilindro de Silica poli cristalino de alta pureza.
- Colocamos um coil RF em torno do cilindro e com este aquecemos muito a Silica, ao ponto de a derreter.
![[float zone.png]]
- Em relação ao Czochralski:
    - temos mais pureza porque nada entra em contacto com um crucible
    - se isto for feito num ambiente de certos gases, podemos dopar a Silica

### Obter wafers do ingot
![[fabrico de wafers a partir de ingot.png]]
- Cortamos em fatias com lâminas de diamante, fazemos etch para remover contaminações e polimos.
- De notar, claro, que em wafers o essencial é ter: o máximo de pureza e o mais plano possível.

## 2.2 - Promover adesão na wafer
### Limpeza
- Temos que garantir que o wafer está limpo a um nível atómico e sem contaminantes
    - Estas contaminações podem ser: óleo, água, óxidos, partículas.
- Quanto mais sujo o wafer, pior será a adesão do que colocarmos em cima.

- Ora, o que complica esta limpeza é que podemso ter muitos tipos de contaminantes para limpar e muitos tipos de wafers. E contaminantes diferentes exigem diferentes processos, assim como teremos diferentes tipos de reações dependendo da wafer.
- Assim, temos tabelas deste género:
![[limpeza wafers.png]]
- Assim, o processo de limpeza costuma incluir: limpeza com químicos, rinse e secagem.

### Prebake e Vapor coating
- Fazemos prebake para retirar água da superfície da wafer.
- Fazemos vapor coating de certos químicos que incentivam a aderência de PR. A camada assim depositada é a *prime layer*.
![[pre bake.png]]

## 2.3 - PR Spin Coating
- É colocado PR no centro da wafer. 
- Começamos por rodar o sistema devagar, a 300 rpm
- Acelaramos até 3000-7000 rpm
![[deposicao pr.png|152]]         ![[deposicao pr grafico speed.png|524]]
- Não sei bem o que faz o vácuo nem como é que ele atua aqui.

- Após o processo de rodar, geram-se uns altos nas bordars da wafer, em que temos uma camada maior de PR - *edge bead*. Esta é a razão porque os wafers são redondos apesar dos chips serem retangulares. Assim, temos a menor edge bead.
- É então depositado solvente para eliminar a eadge bead:
![[solvente para remover edge bead.png]]
podemos ainda aplicar uma fonte de luz para eliminar a edge bead.

### Artefactos do spinning
**Edge Bead**
- Especialmente mau quando temos camadas espessas de PR
 - Vista de lado:
![[edge beam de lado.png]]

**Comet Pattern**
- Ocorre quando há partículas no substrato antes do spin coating
- Fazem o PR ficar demasiado tempo no wafer
![[mercury.png]]

**Zonas sem PR**
- Ocorre quando não inserimos PR suficiente à primeira ou quando não o colocamos bem no centro.

**Pinholes**
- Pontos sem PR
- Causados por partículas no wafer ou por bolhas de ar

### Espessura
- A espessura ($t$) da camada de PR depende de:
    - velocidade de rotação - $\omega$
    - concentração da solução - $c$
    - viscosidade intrínseca - $\eta$
    - constanter do spinner (?) - $k$
    - $\alpha=0.5$ (?)
- E temos:
$$t=\frac{kc^{\beta}\eta^{\gamma}}{\omega^{\alpha}}$$
- A maioria das camadas usadas têm 1-2 um

## 2.3.1 - Photoresists
- Polímero sensível a luz e que muda de estrutura conforma sujeito a luz.
- Ele serve para gravar imagens na wafer:
![[funcao pr.png]]

### PR positivo
- As partes expostas a luz dissolvem-se
- O padrão imprimido na wafer é o mesmo da mask (onde a mask é opaca, PR fica opaco)
- Permite ter maior resolução

### PR negativo
- As partes não expostas dissolvem-se
- O padrão imprimido é o inverso da máscara (fica opaco onde a máscara é transparente)
- Mais barato

### Comparação
- Abaixo temos, da esquerda para a direita: PR positivo, mask, PR negativo
![[pr positivo e negativo.png]]
![[pr positivo e negativo 2.png]]
![[pr positivo e negativo carateristicas.png]]

### Composição
- Mais concretamente, um PR é composto de 
    - Componente fotoactivo - *PAC* - faz com que a resina dissolva ou não na presença de luz
    - Resina - atua como cola que mantém a substância sólida
    - Solvente - permite ter em forma líquida e controlar a viscosidade na deposição

### DNQ
- PR positivo mais comum
- Não pode ser usado para $\lambda$ muitos reduzidos
- No PPT tem uma análise completa da reação química que ocorre quando sujeito a luz.

### Equações de Exposição
- Seja $M$ a concentração de DNQ. Empiricamente sabemos que esta segue a equação:
$$\frac{dM}{dt}=-CIM$$
em que $I$ é a intensidade luminosa da fonte e $C$ uma constante.
- Assim, da EDO temos a concentração relativa $m$:
$$m(t)=\frac{M(t)}{M_{0}}=e^{-CIt}$$
![[m vs t.png]]
- NOTAS:
    - O eixo dos xx está em função de Dose de Exposição, que é $It$. Isto pode parecer estranho, mas sabendo o $m$ final que queremos e a intensidade $I$ da fonte, conseguimos saber por quanto tempo expor o PR a luz, usando o gráfico acima.
    - Esta queda deve-se à conversão de DNQ em ácido carboxálico
    - Aqui estamos a ignorar variações temporais de $I$, que podem frequentemente ocorrer.

- Ora, estamos a ignorar a variação da intensidade. Assim, precisamos de a ajustar usando a *Lei de Absorçao de Lambert*:
$$\frac{dI}{dz}=-\alpha I~~~~\to~~~~ I(z)=I_{0}e^{-\alpha z}$$
ou seja, a intensidade da luz cai com distância percorrida. Conforme o PAC se desfaz e a camada vai diminuido a distância que o feixe percorre aumenta, ou seja, intensidade diminui.

- Mas aqui surfe outra lei: *Lei de Beer* para um PR positivo
$$\alpha=a_{M}M+a_{P}P + a_{R}R+a_{S}S+\dots$$
em que os termos são:
    - $M$ - PAC
    - $P$ - foto produto
    - $R$ - resina
    - $S$ - solvente

- Se fizemos as mudanças de variável: $$A=(a_{M}-a_{P})M_{0} \quad;\quad B=a_{P}M_{0}+a_{R}R+a_{S}S$$
e temos
$$\alpha=Am+B$$
como $m=\exp(-CIt)$ temos $\alpha(t=0)=A+B$  e $\alpha(t\to\infty)=B$. Ou seja, quanto maior for $A$ mais a reação varia com o tempo.

- Assim, este sistema baseia-se em 2 equações diferenciais acopladas:
$$\begin{cases}
\frac{\partial m}{\partial t}=-CI(z,t)m \\
\frac{\partial I}{\partial z}=-[Am(z,t)+B]I
\end{cases}$$

### Medir A e B
- Ora, A e B não passam dos *coeficientes de absorção* da parte ativa e não ativa do PR. Assim, usando um sistema com sensores de luz podemos medir a luz que passa conforme o PR se desfaz.
- Temos:
![[determinar A,B.png]]
e podemos mostar que
$$A=\frac{1}{t}\ln\frac{T_{\infty}}{T_{0}}~~,~~B=- \frac{1}{t}\ln\frac{T_{\infty}}{T_{12}}$$
em que $T_{12}=1-\left(\frac{n_{2}-n_{1}}{n_{2}+n_{1}}\right)^{2}$ é a transmitância ar-PR
- Para certos comprimentos de onda (abaixo de $\sim300\text{nm}$) temos $A=0$

### Popriedades de PR
**Contraste**
$$\gamma=\left[\log_{10}\frac{D_{100}}{D_{0}} \right]^{-1}$$
![[contraste.png]]

- Assim, o contraste  é a capacidade do PR distinguir entre luz e escuro.
- Ou seja, maior $\gamma$ significa que o PR permite obter edges mais verticais. Um valor baixo vai causar orificios no wafer maiores do que desejado
![[contraste como funciona.png]]

**Resolução**
- Quão fina uma linha de uma mask conseguimos reproduzir na wafer
- Determinado pelo constraste, espessura, proximidade mask-PR
- Depende do PR usado e do sistema

**Sensibilidade**
- Energia necessária para criar uma reação que gere um padrão
- Afeta o yield
- Para fazer coisas menores precisamos de menor comprimento de onda e de maior sensibilidade.

**Resistência a Etching**
- Após a exposição a luz, expomos o PR a uma químico ou processo físico de etching (eliminar beiras). Esta propriedade consiste na capacidade do PR resistir a estes processos
- Muito fortemente ligado à química do PR

**Curva de Resposta Espectral**
- Comprimentos de onda a que o PR reage mais. Obviamente deve coincidir com a fonte usada

## 2.4 - Soft Bake
- Evapora os solventes do PR
- Melhora adesão, uniformidade e resistência a etching
- Impede formação de bolhas
![[soft bake.png]]

Existem 2 formas de fazer isto
**Hot Plate**
![[soft bake 2.png]]
- Aquecemos wafer de cima para baixo. Rápido.
- Necessita que a superfície seja muito plana

**Forno de convexão**
![[soft bake 3.png]]
- Solvente evapora primeiro, o que pode causar problemas
- Mais lento
- Obviamente pior

## 2.5 - Alinhamento e Exposição
- Este é o passo em que actually passamos a imagem para a wafer
- **Passo crítico** da fabricação de chips
    - Por essa razão, o mask aligner é dos equipamentos mais caros 
- Este é o passo que determina o tamnho da feature mínima
    - Atualmente, este é de 18nm, mas com tendência a baixar

### Masks
- Obviamente, contêm a imagem que queremos imprimir
- Tal como nos PR, temos 2 tipos:
    - *light-field* - maioritariamente transparentes, com a imagem opaca
    - *dark-field* - maioritariamente opacos, com a imagem transparente

**Fabrico**
![[fabrico mask.png]]
- A mask é desenhada num software CAD 
- A mask em si também é feita com um processo que usa PR. Normalmente usamos uma base de vidro e um substrato de Cr. Usando um electron beam, eliminamos Cr onde queremos que a mask seja transparente.
- Podem surgir vários defetios na mask, mas a grande maioria pode ser resolvida.

### Alinhamento
- O mask aligner usa um sistema complexo de microscópios para verificar alinhamento. Usasse *pelo menos 2* marcas para verificar alinhamento.
- As maks têm que ser alinhadas nos **seis** eixos:
    - x,y,z
    - roll, pitch, yaw (termos não oficiais)

**Erros**
![[problemas alinhamento.png]]
- O último desenho mostra run-out (a mask começa alinhada e vai-se desalinhando)
    - Isto ocorre porque temos expansão térmica da mask
    - Para coisas à escala nano, a mínima expansão da mask pode causar problemas

### Lâmpada de Mercúrio
- Frequentemente usado. Gera os primeiros 3 comprimentos de onda abaixo:
![[comprimentos de onda.png]]

## 2.6 - Bake pós-exposição (PEB)
- Suaviza a parede da PR onde houve dissolução e melhora resolução
- Permite rearranjar as partículas de PR que foram demasiado expostas ou expostas a menos (?)
- Normalmente a maior temperatura que soft bake
- Over baking causa polimerização do PR e causa problemas

## 2.7 - Development
- Colocado sobre a wafer. Serve para dissolver/remover as partes do PR que ficaram enfraqueceram com a exposição à luz. 
- Permite actually ficar com o padrão da mask na wafer.
- Usasse normalmente uma solução básica fraca.

### Passos
- Temos 3 passos:
    - *Develop* - solução colocado sobre a wafer (ainda com PR em cima). Rodar amostra para remover a maioria da solução e PR dissolvido nela
    - *Rinse* - colocar água e rodar para a remover
    - *Secar* - secar

### Problemas
![[falhas de development.png]]

### Equações
- Podemos escrever a equação que nos dá a difusão do developer para a interface com o PR:
$$r_{D}=k_{d}(D_{bulk}-D_{S})$$
Nesta equação temos:
    - $r_D$ a taxa de difusão na interface PR-developer
    - $k_{d}$ uma constante
    - $D_{bulk}$ concentração de developer na zona "bulk" (zona longe da superfície de reação)
    - $D_{S}$ concentração de developer na superfície do PR

- Podemos ainda escrever a equação que descreve a taxa de reação:
$$r_{R}=k_{R}D_{S}P^{n}$$
Nesta equação temos:
    - $r_{R}$ a taxa de reação
    - $k_R$ uma constante
    - $D_{S}$ a concentração de developer na superfície de PR
    - $P$ concentração de PAC exposto
    - $n$ número de moléculas que precisam de reagir com o developer para ser libertada uma molécula de resina

- Se considerarmos um estado de equilíbrio da reação teremos:
$$r_{D}=r_{R}=r$$
que podemos reorganizar de modo a ter:
$$r=\frac{k_{D}D(1-m)^{n}}{\frac{k_{D}}{k_{R}M_{0}^{n}}+(1-m)^{n}}$$

## 2.8 - Hard Bake
- Evaporamos todo o solvente no PR
- Melhorar resistência a etch e implementação
- Melhorar adesão, pode ocorrer shrinkage
- Hard bake longo e mais quente pode dificultar remoção de PR
    - Normalmente 100-130ºC por 1-2min

### Possíveis problemas
![[falhas hard bake.png]]
**Under-Bake**
- PR não polimeriza completamente
- PR com alta resistência a hetch
- Fraca adesão

**Over-Baking**
- Fluxo de PR e má resolução

## 2.9 - Inspeção
- Pretende-se detetar irregularidade como riscos, pinholes, manchas, contaminações
- Medimos a dimensão crítica 
- Se a wafer *não* passar a inspeção, removemos o PR e recomeçamos
- Se a wafer *passar*, podemos continuar

## 2.10 - Transferência de padrão e Remoção de PR
- Temos 2 técnicas comuns para transferir o padrão para a wafer

### Etching
- Removemos as partes da Silica que queremos, basicamente usando o PR como mask

### Liftoff
- Colocamos uma nova camada de material
- As partes não desejadas são retiradas ao remover o PR

- Para *remover o PR*:
    - Normalmente chega usar um solvente simples
        - PR positivo - acetona, TCE
        - PR negativo - MEK
    - Etching de plasma com O2
    - Alguns PRs são mais dificeis e exigem o uso de coisas mais complicadas

## 2.10 - Inspeção Final
- O que o nome indica
- Todo este processo é repetido 20-60 vezes, para depositar outros materiais e assim gerar novas funcionalidades 