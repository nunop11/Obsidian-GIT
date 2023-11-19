# Sinais e Sistemas
- Sinais são usados para transmitir informação. 
- Sistemas servem para processar sinais e, assim, processar informação.

# Passagem para o mundo digital
## 1- Registar o Sinal em certos instantes
![[Recolher Amostra de Sinal.png]]
- Para isto usa-se um circuito _sample and hold_:
![[Circuito sample and hold.png]]

- Tendo um sinal variável que nunca passa o valor $f_{\text{max}}$, então a variação mais rápida de sinal ocorre em $\Delta t=\frac{1}{f_{\text{max}}}$
- Assim, se recolhermos dados com uma frequência $f_{S}\geq 2f_{\text{max}}$, então não se perdem muitos dados, de forma que o sinal inicial pode ser completamente reconstruido.

## 2- Codificar os valores recolhidos
![[Sinal recolhido para binário.png]]
- Imaginesse que recolhemos a onda acima.
- Dividimos em faixas horizontais com diferentes diferenças de potencial. Neste caso, são 15. Acima, estas estão indicadas em código binário.
- Assim, cada ponto da onda está entre 2 valores binários da escala vertical.
- Ou seja, o sinal pode ser representado como uma série de 1 e 0.

# Miniaturização
**Lei de Moore** - Gondon Moore (co-fundador da Intel) disse em 1965 que o número de transístores dos circuitos integrados teria um aumento de 100% a cada 18-24 meses. Verificou-se.

- Os transístores fabricados hoje em dia têm uma dimensão de cerca de 10 nm. No entanto, não será possível reduzir o tamanho muito mais. Isto devido a 2 fatores:
    - *Degradação das caraterísticas* - Por exemplo, se tivermos uma camada de um certo material que atue como isolador, se reduzirmos muito o tamanho do transístor, esta camada eventualmente passará a ter apenas alguns átomos de espessura.
    - _Dissipação de potência_ 
        - Imaginemos um transístor que tenha uma energia dissipada dada por $E_{\text{pot}}=\frac{1}{2}CV^{2}$. Para $C=20 \cdot10^{-9} F, V=5V$ temos $E_{\text{pot}}=0.5 \mu J$
        - Isto pode parecer pouco, mas ao ter em conta que num processador moderno podemos ter $5 \cdot 10^{9}$ transístores em $1 ~mm^2$, vemos que a densidade de potência dissipada chega a ser semelhante à de um reator nuclear ou do nozzle do motor de um foguetão.
        - Esta dissipação causa: diminuição do tempo de vida dos componentes, aumento dos custos de funcionamento, avarias mais frequentes, etc. (É também a razão para haverem ventoinhas em computadores)

# Memresistor
- Este é um novo componente fundamental, em conjunto com resistências, bobinas e condensadores.
- Vimos anteriormente, em Eletrónica, que:
    - $dI=k_{1}dV \leftrightarrow dV=\frac{1}{k_{1}}dI~~;~~\frac{1}{k_{1}}=R$
    - $dQ=k_{2}dV~~;~~k_{2}=C$
    - $d \phi=k_{3}dI~~;~~k_{3}=L$
- Temos ainda dependências temporais: 
    - $\Large I=\frac{dQ}{dt}$
    - $\Large V=\frac{d\phi}{dt}$

- Ou seja:
![[Quadrado componentes eletrónica incompleto.png]]
- Falta-nos então relacionar Carga e Fluxo Magnético. Assim 
$$d \phi=k_{4}dQ$$
Temos 
$$k_{4}=\frac{d\phi}{dQ}=\frac{\frac{d\phi}{dt}}{\frac{dQ}{dt}}=\frac{V(t)}{I(t)}$$
que tem dimensões de resistência.

- Definiu-se então o *memresístor*: $$M \equiv \frac{d\phi}{dQ}$$
![[Memresistor.png]]
    - $M$ é uma resistência que depende do valor e sentido da corrente elétrica
    - Se a corrente se torna 0 muito rápido, $M$ terá o valor da corrente imediatamente antes do corte.

- Comporta-se como um "tubo" cujo diâmetro varia de acordo com a intensidade e direção do "fluxo". Essa variação irá portanto variar a resistência ao "fluxo". No memresistor, esse "fluxo" é a corrente elétrica.


- Assim, como vimos em eletrónica, temos:
    - Resistência
    - Capacidade de condensadores
    - Indutância de bobinas

- Ora, todos estes são invariantes no tempo. A _memresistência_ de um memresístor varia em função das condições de utilização.

- Temos então:
![[Quadrado componentes eletrónica completo.png]]

#sinais #fisica