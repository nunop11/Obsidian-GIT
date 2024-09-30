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