# 1 - Lei de Moore
- Diz que: o número de transístores num circuito integrado duplica a cada 18 meses. 
    - Esta lei é bastante conhecida e verificou-se de forma consistente nos últimos 50 anos.

- Mas há uma outra lei: o custo de uma planta de fabricação de chips de semicondutores duplica a cada 4 anos. Esta lei também se verifica.

# 2 - Yield / Rendimento
- Podemos definir:
    - Rendimento da wafer: $Y_{W}=\frac{\text{Wafers}_{\text{ bom}}}{\text{Wafers}_{\text{ tot}}}$
    - Rendimento do die: $Y_{D}=\frac{\text{Dies}_{\text{ bom}}}{\text{Dies}_{\text{ tot}}}$
    - Rendimento do packaging: $Y_{C}=\frac{\text{Chips}_{\text{ bom}}}{\text{Chips}_{\text{ tot}}}$
- Daqui temos o rendimento total:
$$Y_{T}=Y_{W}Y_{D}Y_{C}$$
- Isto até não parece mau. Mas consideremos que o rendimento total de 1 passo é $99\%$. Se a produção de um chip exigir 600 passos teremos um rendimento final de $0.99^{600}=0.24\%$.

## 2.1 - Rendimento Funcional
- Tendo uma certa placa com defeitos, podemos ver abaixo que quantos mais e menores Dies fizermos, melhor será o rendimento:
![[defeitos vs tamanho die.png]]
assim podemos dizer:
$$Y = f(D_{0},A_{c})$$
- Considerando que os defeitos estão distribuidos aleatoriamente e são independentes uns dos outros, podemos usar o modelo de Poisson:
$$Y = \exp(-D_{0}A_{c})$$

## 2.2 - Contaminações
- Uma das principais fontes de perda de rendimento é *contaminações*
- Tendo em conta a reduzida escala dos componentes fabricados, é natural assumir que facilmente podemos contaminar e danificar:
![[contaminação.png]]
- A razão em concreto porque contaminações estragam dies é:
![[contaminação porquê.png]]
ou seja, se a contaminação for *maior* que a dimensão caraterística ela irá fazer curto-circuito e estragar o die.

- Assim, temos este gráfico muito engraçado:
![[contaminações escala de tamanho.png]]
Ora, tudo à direita do ponto vermelho (basicamente tudo o que existe exceto átomos livres) são contaminações que irão danificar o die.

- Outro gráfico relevante:
![[tamanho probabilidade perda yield.png]]
em que as partículas mais perigosas são aquelas na gama $0.1-0.3~\mu\text{m}$. 
- Assim, para reduzir contaminação, usamos **salas limpas**.

# 3 - Sala Limpa
- Sala em que a concentração de partículas no ar é controlada. Estas salas são construidas e usadas de forma a minimizar a introdução, criação e retenção de partículas no seu interior. Para isto, são controlados parâmetros como: temperatura, humidade e pressão.
- Têm portanto a função de proteger produtos ou processos de contaminação, assim como conter perigos.

- As maiores fontes de contaminações são as pessoas: saliva, transpiração, impressões digitais, cabelos/pelos, pele seca, fibras de roupa, etc etc. Mais concretamente temos abaixo um gráfico a mostrar quantas particulas uma pessoa emite consoante se move:
![[particulas libertadas pessoa a mover.png]]

- Isto é também visível em dados de uma cleanroom. Normalmente temos zonas controladas nas bancadas com maior proteção de partículas e uma zona (o corredor / aisle) onde as pessoas circulam e temos mais partículas:
![[particulas libertadas em clean room.png]]

- Assim, de forma concreta, as fontes de partículas são:
    - Pessoas (~75%) - fontes vistas acima
    - Materiais (~20%) - produtos de madeira, cartão, papel, ventilação, coisas da estrutura da sala limpa itself
    - Equipamento e produtos (~5%) - motores elétricos, escadas, silica itself, vassouras

### Classificações de Salas Limpas
- Sistema americano
![[classes clean room 1.png]]
De uma forma geral: "Classe X significa que podem existir X partículas de $0.5\mu \text{m}$"

- Sistema ISO 14644
![[classes clean room 2.png]]

- O MNTEC (a nossa sala limpa) é classe 10000 na maioria do espaço e 1000 nas bancadas mais especializadas. E costou 1 M€ :)

--------- Para ver mais informação, ver o resumo sobre Cleanroom - a TP do Paulo Marques ------

## Filtros
- Filtros sintéticos têm maior qualidade e reduzem número de partículas 10x
- Filtros de fibras naturais têm menor qualidade e apenas reduzem 2x. Além disso, por terem fibras naturais, emitem partículas
- Os filtros mais comuns e baratos são HEPA - High Efficiency Particulate Air. Têm 99.99% a 0.3m
- Acima desses temos os ULPA - Ultra Low Penetration Air. Têm 99.999% a particulas de 0.1-0.2 um.
## Evolução de Sala Limpa
![[esquema fluxo particulas clean room.png]]~~
- Sendo $C_{n}$ a concentração de partículas na sala temos:
$$V \frac{dC_{n}}{dt}=P + FC_{n}(1-\eta) -FC_{n}$$
- Explicar termos
    - O lado esquerdo representa o fluxo de partículas (unidades particulas/tempo)
    - O 1º termo lado direito são as partículas que entram na sala de qualquer forma
    - O 2º termo são as partículas que entram (do lado esquerdo) por não passarem no filtro ($\eta$ é a eficiencia do filtro, logo $1-\eta$ é a porção que não filtra)
    - O 3º termo é as partículas que perdemos por serem filtradas
- Podemos reescrever como:
$$\frac{dC_{n}}{dt}=\frac{P}{V}- \frac{F}{V}\eta C_{n}$$
- Em que:
    - $P/V$ é a emissão de partículas por unidade de volume
    - $F/V$ será o número de mudanças de ar por minuto

- Uma solução estacionária desta EDO é:
$$C_{n}^{0}=\frac{P}{F\eta}=\frac{P}{V} \frac{V}{F} \frac{1}{\eta}$$
