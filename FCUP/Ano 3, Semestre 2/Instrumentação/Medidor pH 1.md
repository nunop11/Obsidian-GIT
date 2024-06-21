## O que é pH
- Indicação de quão ácido ou básico uma solução é, numa escala logaritmica de 0 a 14.
- Baseia-se na concentração molar de iões de hidrogénio, $H^{+}$:
$$\text{pH} = -\log_{10}[H^{+}]$$
![[escala ph.jpg|337]]
- Se pH=7 temos uma solução neutra, pelo que $[H^{+}]=10^{-7}\text{mol/L}$. O maior exemplo disto é a água.
- Se pH>7 temos uma solução básica/alcalina, pelo que temos $[H^{+}]<10^{-7}\text{mol/L}$, para uma concentração mínima de $10^{-14}\text{mol/L}$. Exemplos são detergentes e lixívia.
- Se pH>7 temos uma solução ácida, pelo que temos $[H^{+}]>10^{-7}\text{mol/L}$, para uma concentração mínima de $10^{-1}\text{mol/L}$. Exemplos são vinagre e ácido de bateria.

## Medir
- No entanto, esta definição de pH é meramente teórica. Para medir esta grandeza usamos *medidores de pH*.
- Estes consistem em ter 2 elétrodos:
    - Um de referência. 
    - Um que reage ao pH.

### de Vidro
![[sensor ph.jpg|500]]
(https://www.pt.endress.com/pt/produtos/analitica/sensores-transmissores-ph-medidor)
- Um grupo de medidores de pH tem o eletrodo de referência feito de Cloreto de prata ou calomel e o eletrodo de medição feito de vidro.
- A medição consite em detetar a diferença de potencial elétrico entre os 2 eletrodos.
- Podemos abaixo ver a relação $E(\text{pH})$ para um medidor com eletrodo de vidro:
![[tensao vs ph teorico.png]]
(https://en.wikipedia.org/wiki/Glass_electrode)
- Esta relação (parte linear) resulta da equação de Nernst ($R,F$ são as constantes do gás ideal e de Faraday):
$$E=E^{0}-\frac{2.3RT}{F}\text{pH}$$
vemos aqui logo que o comportamento é dependente da temperatura.

- Na prática, para medir usamos um instrumento do tipo:
![[ponta prova ph.png|150]]
    - Temos um um eletrodo que contacta com a solução exterior feita de um vidro especial (1) e o eletrodo de medição (2). Os dois eletrodos encontram-se mergulhados numa solução com buffere de $\text{pH}\sim7$ (3). Temos em (5) o eletrodo de referencia mergulhado numa solução de referencia (6)


### ISFET
![[isfet.jpg]]
(https://www.pt.endress.com/pt/produtos/analitica/sensores-transmissores-ph-medidor)
- **ISFET** - transistor de efeito de campo seletivo de iões (Ion Selective Field Effect Transistor)
- Na bola perto de D temos um transístor. Ligado a ele está uma fonte de tensão e um semicondutor SD.
- Os eletrões H+ (cargas postivas) acumulam-se junto ao semicondutor, causando acumulação de carga negativa e consequentemente passagem de corrente e o circuito fica fechado. Quanto maior a concentração de H+, maior a corrente.