###### Aula 9 - 19/3/2024
**Continuação Aula Anterior**
- Conforme o que vimos, podemos definir
$$M = - \frac{1}{V} \frac{dU}{dB}=- \mu_{B}(n_{\uparrow}-n_{\downarrow})=\mu_{0} g(\varepsilon_{F})\mu_{B}^{2}B$$
logo temos:
$$M=\chi_{P} B~~\to~~ \chi_{P}=\mu_{0}g(\varepsilon_{F})\mu_{B}^{2}$$

- Definindo $\mu=\varepsilon_{F}$ (potencial químico) e $g(\varepsilon_{F})=\frac{3}{2} \frac{n}{\varepsilon_{F}}$ obtemos:
$$\chi_{Pauli}= \frac{3}{2} \frac{n\mu_{0}\mu_{B}^{2}}{2\varepsilon_{F}}\ll1$$

## Falhas de Sommerfeld
- O que acabamos de ver *não se verifica*. Ao medir experimentalmente a susceptibilidade, os valores não ser verificam. Por exemplo:

|     | $\chi_{exp}(\times10^6)$ | $\chi_{P}(\times10^6)$ |
| --- | ------------------------ | ---------------------- |
| Li  | 2.0                      | 0.80                   |
| Na  | 2.1                      | 0.66                   |
| K   | 0.80                     | 0.13                   |
| Rb  | 0.80                     | 0.50                   |

- Além disto, e mais grave, o modelo de Sommerfeld não explica a existência de materiais que *não sejam metais*: semicondutores, isoladores, quase-metais, etc.

# Cristais
- Cristais são materiais que podemos dividir em estruturas pequenas e simples: *célula primitiva* AKA *célula Wigner-Seitz*. Usando esta, podemos fazer translação da mesma, de forma a formar toda a grelha que forma o cristal.
- 2 exemplos comuns são: grafite e diamante. São chamadas de alotrópicas, porque ambas são feitas de carbono.
- Ora, a diferente organização dos átomos é o que diferencia estes metais. Disto surgem diferenças:
    - Transparência / cor
    - Dureza
    - Condutividade (grafite conduz, diamante não)
- Mais concretamente, a estrutura do diamante é *cúbica* e a da grafite é *hexagonal*:
![[grafite e diamante.png]]

**Propriedades Translacionais**
- Como visto acima, as células primitivas têm que ter propriedades translacionais.
- Isto significa que, num material descrito por $H=\sum_{i=1}^{N}\frac{\vec{p}_{i}^{2}}{2m}+V(\vec{r})$ temos que ter:
$$V(\vec{r}+\vec{f})=V(\vec{r})$$
- Ora, o que precisamos de saber é como definir o vetor $\vec{f}$ que permite fazer a translação.

**Redes de Bravais**
- Conceito abstrato definido por cristalógrafo Bravais.
- Permite definir as grelhas com pontos permitidos pela translação. Na prática, isto significa que:
    - estamos num ponto. Olhamos numa direção
    - efetuamos uma translação. Olhamos na mesma direção e vemos exatamento o mesmo.
- Existem poucas grelhas possíveis. Para 2D apenas temos 5, para 3D temos 14.
- Os elementos que compõe as grelhas nem sempre são as células primitivas! Por exemplo, no caso de $\alpha$-quartzo ou grafite. Na grafite os hexagonos *não* são a célula primitiva.

*Bravais 2D*
![[redes 2d.png]]
Seguindo a ordem (esquerda para a direita, cima para baixo):
1. **Rede Quadrada** - simetria de reflexão conforme $x=0,y=0$ e de rotações de 90º em torno do eixo dos zz. 
2. **Rede Retangular** - obtida ao esticar rede quadrada numa direção. Mantéma  simetria de reflexão segundo $x=0,y=0$
3. **Rede Hexagonal** - simetria de reflexao nos planos $x=0,y=0$ e em rotações de 60º segundo eixo zz.
4. **Retangular Centrada** - obtida ao comprimir a rede hexagonal numa direção. Simetria de reflexão segundo $x=0,y=0$
5. **Rede Oblíqua** - sem simetria. 

- É evidente que a rede quadrada tem a maior simetria. Podemos partir dela e aplicar deformações (reduzir simetria) e obter as restantes redes:
![[hierarquia 2d.png]]
Inversamente, podemos partir da rede menos simétrica e obter as restantes.

- Qualquer uma destas simetrias com direções $\alpha_{i},\alpha_{j}$ (que fazem ângulo $\varphi$), permite gerar a grelha infinita 2D usando translações com combinações lineares de coeficientes inteiros destas 2 direções:
![[definir rede bravais com vetores.png]]