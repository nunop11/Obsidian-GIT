# SQUID
- Medimos as amostras de YBCO da PL1 no SQUID 
- Medimos: $$m_{\text{YBCO}}^{A}=(5.7 \pm0.01) \text{mg} \quad;\quad m_{\text{YBCO}}^{B}=(15.
65\pm0.01) \text{mg} \quad;\quad m_\text{Fe3Si}=(8.54\pm0.01)\text{mg}$$
- Para pesar o YBCO:
    - Meter folha de aluminio na balança
    - Tara a balança
    - Meter amostra no alumínio

- À temperatura ambiente, o YBCO é paramagnetico ($M\sim0$). O Fe3Si é ferromagnético ($M\gg1$). Assim é MUITO IMPORTANTE mantê-los separados senão as medições do SQUID não vai ter boa qualidade


## YBCO-A
- Usamos porta amsotras de latão no SQUID
- Metemos a fita só na amostra
- Setup no SQUID
    - Fizemos ZFC
    - Não fizemos calibração para achar centro da amsotra porque começamos a temperatura ambiente e temos magnetização nula (calibração ia tentar calibrar um monte de zeros)
    - Fizemos purgas com He para ter vácuo
    - Descemos até 45K
- **Sequência**:
    - Descer até T=45K a 35K/min (ou /s, não tenho a certeza)
    - Esperar 30s
    - Meter H=100Oe, s/ overshoot, 100Oe/min (este campo é baixo, mas para esta amostra deve ser bom pq ela é muito sensível)
    - Criar ficheiro
    - Medir M(T):
        - de 45K a 65K com menos pontos
        - de 65K a 115K com mais pontos
        - de 115K a 150K com menos pontos
    - Colocar H=0
    - Esperar 2s
    - Colocar T=300K
    - Esperar 5s
    - Fim


- Depois de medir, concluimos que esta amostra foi feita sem fluxo de oxigénio no passo final. A transição ocorria a 60K, não 90K

## YBCO-B
- Medido em 2º, logo a seguir ao YBCO-A, com mesma sequência
- Esta amostra de facto teve O2 no passo final da sintese de solid state. A transição ocorre por volta dos 90K
- A transição acontece se forma lenta, porque há irregularidades
- Não vimos na aula porque o FFC foi medido pelos profs antes e enviado por mail, MAS:
    - Com ZFC, ao diminuir a temperatura, a magnetização cai muito
    - Com FFC a magnetização cai pouco e é muito mais estável
    - Isto acontece porque há uma relação qualquer entre o campo externo no FFC e o campo crítico do YBCO (?)

## FE3SI
- Medimos o ciclo de histerese M(H) a 3 tempraturas
- Desta vez, como este material é ferromagnético, fizemos calibração de posição central da amostra a 500Oe. Funcionou bem

**Sequência**
1. Colocar T=380K, a 20K/min
2. Esperar 5s
3. Medir M(H): Começar em 4T, descer a -4T, subir a 4T. Fizemos sweep do tipo log(H)
4. Colocar T=200K, a 30K/min
5. Medir M(H): Começar em 4T, descer a -4T, subir a 4T. Fizemos sweep do tipo log(H)
6. Colocar T=25K, a 30K/min
7. Medir M(H): Começar em 4T, descer a -4T, subir a 4T. Fizemos sweep do tipo log(H)
8. Colocar H=0
9. Colocar T=300K, a 30K/min
10. Esperar 5s
11. Fim

# ARCH MELT
- Fizemos amostras de Fe3Si, MAS Analisamos uma nova. Ver na secção de squid
- Para fazer 1 grama de Fe3Si, obtemos da estequiometria:
$$1\text{g} ~\text{Fe}_{3}\text{Si}~~\to~~ 0.143\text{g}~\text{Si} + 0.856\text{g Fe}$$
e fizemos 2g para o caso de haver perdas
- O JP tem um excel com 3 casos:
    - Queremos uma massa total, diz a quantidade de cada reagente
    - Já pesamos Si, diz quando Fe medir e a massa total prevista
    - Já pesamos Fe, diz quando Si medir e a massa total prevista
 
- Começamos pelo Fe porque é mais difícil controlar a massa
- Medimos:
    - Massa medida: $$m_{\text{Fe}}^{m}=1.7155\text{g} \quad;\quad m_{\text{Si}}^{m}=0.28189\text{g} \quad;\quad m_{\text{Fe}_{3}\text{Si}^{m}}=1.99548\text{g} ~(\textsf{após melt!!!})$$
    - Massa prevista: $$m_{\text{Fe}}^{T}=1.714\text{g} \quad;\quad m_{\text{Si}}^{T}=0.287931\text{g} \quad;\quad m_{\text{Fe}_{3}\text{Si}}^{T}=2.005491\text{g}$$

## Sistema Arch melt
- Usa-se um sistema de 2 bombas externas, o sistema original avariou :)
    - Iremos ver os passos necessários para fazer purgas. Com o sistema original era mais fácil, era só mudar uma alavanca como tem no tutorial no sigarra
- Temos então uma bomba rotary e uma bomba de difusão
- O vácuo tem de ser bom senão vapor de água e oxigénio reagem e ocorre oxidação
- Usamos argon nas purgas e para ter uma atmosfera inerte
- A botija de Ar é de pureza 6.0: pureza de 99.9999% (0.999999). Abrimos a botija à mão lá fora. Depois, no lab de materiais, abrimo a válvula de Argon
- Para subir a câmara, usamos um *macaco hidraulico*
    - Ele tem óleo dentro e ao bombar a alavanca estamos a pressurizar o óleo, faz força e a câmara sobe aos poucos.
    - Temos uma cena que rodamos para mudar a zona para onde o oleo vai. Isto faz a câmara subir ou descer
    - Ao baixar a câmara garantimos que o o-ring está bem encaixado no sulco. Ao baixar a câmara, ele é apertado e temos vácuo
- A base do arch melt é de cobre, porque é condutor e fácil de arrefecer. Dito isto, a base é arrefecida com água 
- Temos um Getter de titânio, ele absorve O2 e outros gases reativos
- A ponta do Arch Melt é feita de tungstenio, porque tem uma alta temperatura de fusão
- Ao meter os metais na câmara, metemos o Si em baixo e o Fe por cima
    - O Fe é um metal então recebe melhor a tensão da ponta e facilita o derreter dos materiais

**Porquê arch melt**
- Em TLA1, sintetizamos YBCO usando Solid State Route porque é a única forma de combinar Y,B,C,O. Não são miscíveis
- Em TLA2, sintetizamos Fe3Si porque Fe,Si o permitem

### Medidores de pressão (!)
- Já saiu em exame
- Temos um medidor de pressão com 2 escalas
    - A de cima é a escaaa de Pirani, alta pressão. 
        - Esta mede a diferença de temperatura entre 2 pontos usando um termopar
        - Quanto maior a pressão, maior a diferença de pressão porque temos mais partículas para conduzir 
    - A de baixo é a de Penning, baixa pressão
        - Precisa de uma fonte de tensão decente, porque ioniza o ar
        - Quanto maior a pressão, maior a corrente medida (?)
- Nota sobre pressão: 1mbar (100Pa) ~= 1Torr (130Pa). Isto é util porque bombas duram décadas, então algumas ainda apresentam escalas em Torr, apesar de ser antiquado

### PURGAS
- Diffusion Pump = DP, Rotary Pump = RP
- Ligamos a RP
- Rodar a valvula que liga a RP à câmara *lentamente* para não "abafar" a RP. Se abafarmos a RP, ouvimos um barulho muito distinto
- A guilhotina abre em 2 passos, que fizemos todos. Primeiro puxa para fora, depois roda para tirar o o-ring do sítio
 - Fizemos 3 purgas.
- O tempo que isto demora depende da humidade do ar neste dia, na nossa aula foi rápido

**Passos de 1 purga**
1. Fechar a válvula guilhotina para a pressão de Ar não chegar ao fundo da DP e desligar o medidor de pressão
2. Colocar Ar até 600mBar
3. Abrir o passador (quebrar o isolamento)
4. Abrir valvula de rodar (ligar RP à camara) e ligar medidor de pressão
5. Aos $10^{-2}$ mbar, fechar válvula de rodar (isolar RP)
6. Fechar passador (ligar DP à câmara), inicar vácuo fundo
7. Repetir

No final, isolamos as bombas da câmara antes de meter Ar e fazer o melting

### MELTING
1. Abrir o passador de água fria na parede
2. Depois das purgas temos uma pressão $P_{0}$ muito baixa. Meter 700mbar de Ar na camara
3. Atrás da câmara e bombas tem um gerador de alta tensão. Ligar
4. Alinhar ponta com o getter
5. Tapar as janelas com os filtros UV e ligar a ponta
6. Andar à volta do getter sem tocar para o fundir. Estar sempre a mover para não fundir a base de cobre
7. Levar a ponta até ao Fe,Si para os fundir
8. Repetir 4-7 4 vezes para garantir que Fe,Si fundem e reagem bem

**Depois do MELTING**
1. Abrir a câara com o macaco
2. Tirar getter e amostra
3. Meter alcool e limpar amostra com a cena verde de esponja da louça e secar com papel. Isto tudo para tirar resídios orgânicos ou de tungstenio. Limpar base com álcool
4. Fechar câmara e deixar a fazer vácuo. Desta vez demora muito mais porque temos vapor do alcool

# MrSQUID (MR)
- O SQUID da Quantum Designs mede em DC (tem um modo que não é bem DC, mas também não é AC)
- O MR é um modelo educacional simples dos 90s
- Tem uma junção de josephson, que consiste em ter: Supercondutor, Isolador, Supercondutor
- Abaixo da Tc do supercondutor (SC), ocorre condução de carga *através do isolador*
    - Ou seja, basicamente temos um díodo
    - Em SCs, os condutores de carga são **pares** de eletrões, que se comportam como bosões invés de fermiões
- Seguimos o labwork do MR que tem no sigarra : mas unicamente a _1a parte_
- O suporte do MR consiste numa barra de metal, com uma placa eletrónica com a junção na ponta. Isso é mergulhado em algo que a coloque abaixo de Tc
    - Na ponta, em torno da junção, temos um shield de **mu-metal**, um material que tenha $\mu$ muito elevado ($B=\mu H$). Ou seja, o material impede o campo terrestre de interferir com a junção, que é super sensível
- A caixa de alimentação funciona a pilhas para poder ser usada longe da rede elétrica (a junção é MUITO sensível)

## Medições
- Ao variar a corrente na junção, o traçado $V(I)$ é assim:
![[curva transicao mrsquid.png]]
(este traçado é medido com o sistema a baixa temperatura, com um cabo a liga-lo à fonte)
- Ligamos o X da caixa ao CH1 e o Y ao CH2
    - X: corrente dente de serra que a caixa dá à junção
    - Y: tensão medida nos terminais da junção
- Começamos com todos os manipulos da caixa às 12h e com amplitude (do sinal dente de serra) mínima
- Ajustar a amplitude para ver melhor
- No osciloscopio:
    - Ao ver em modo Sinal vs Tempo vemos o dente de serra do CH1 e vemos um dente de serra com zona achatadas no centro (como acima) do CH2
    - Ao ver no modo XY, temos o formato visto acima
- No traçado acima, o zero encontra-se no centro da zona plana. Assim, ao aumentar Amplitude vamos conseguir chegar mais e mais fora.
    - Ou seja, para uma corrente alta (amplitude alta) há condução na junção. Abaixo de uma corrente (ampltiude) mínima, não conseguimos "forçar" corrente através do isolador