# 1 - GPIO
- **GPIO** = General Purpose Input / Output
- Basicamente um terminal do ESP32 que tanto pode ser uma entrada como uma saída, como o nome indica.

## Corrente
- Nas datasheets temos que, para o ESP32-Pico-D4, a corrente máxima que ele pode fornecer é $40$ mA, enquanto que a corrente máxima que pode receber/absorver é $28$ mA.

## Formas de Ligar
![[ledbut.webp]]
- Em regra geral, uma *resistência em série com um LED* (figuras 2,4) têm a principal função de limitar a corrente que nele passa.
    - Acima usamos $1\text{k}\Omega$ estamos a supor uma queda de 2.3V no LED, tendo-se uma corrente $\sim 1\text{mA}$. Isto é baixo, mas dá luz visível

- As *resistências em série com botões*, elas têm a função de decidir se a tensão é 1 ou zero quando se prime o botão.
    - Na figura 1 temos uma resistência **pull-up**: com um fio no seu lugar teríamos a entrada do ESP ligada a nada. Com ela, temos $1$ quando o botão *não* é premido. Caso contrário temos $0$. Temos que o botão é **Active Low**
    - Na figura 3 temos uma resistência **pull-down**: com um fio no seu lugar teríamos a entrada do ESP ligada ao ground. Com ela, temos $0$ quando o botão *não* é premido, mas a tensão não será nula. O botão é **Active High**
    - De notar ainda que: em ambos os casos, sem a resistência, ao carregar no botão ficamos com a alimentação e o ground em curto-circuito!
    - As resistência pull-up e pull-down podem não ser necessárias, porque às vezes o MCU já as inclui.

- Por fim, temos condensadores em paralelo com os botões, que têm a função de anular possíveis oscilações da tensão no botão (causadas por o motor ser um sistema mecânico). Dependendo da qualidade do botão isto pode não ser necessário.

## Tensões
- O ESP32 trabalha com uma tensão de 3.3V. Esta é então a tensão de alimentação que este MCU emite e a tensão que ele deverá receber nos terminais.
- Se por alguma razão for necessário este circuito interagir com um sensor ou sistema com tensão de 5V, teremos que usar um circuito *adaptador de nível*:
![[image-9.webp|475]]
- Se a diferença de tensões for muito maior poderá ser preciso um circuito mais complexo, com relays e transístores.

## MicroPython
![[ledButBoardPins-624x398.webp]]
- É só python
- Para ativar um pino (e com ele um LED ou algo similar) usamos a classe `Pin` do módulo `machine`. EX: colocar LED a piscar:
```python
from time import sleep
from machine import Pin

led_red = Pin(21, Pin.OUT)

print("Blink")
while True:
    led_red.value(True)
    sleep(1)
    led_red.value(False)
    sleep(1)
```

- Ou seja, apenas usamos o método `.value()` para ligar (`True`) e desligar (`False`) o pino. 
- Podemos ainda definir um pino em função do outro: (EX: LED ativado por botão)
```python
from machine import Pin

led_green = Pin(19, Pin.OUT)
button_left = Pin(23, Pin.IN, Pin.PULL_UP)
button_right = Pin(18, Pin.IN, Pin.PULL_UP)

print("Follow")
while button_right.value():
    led_green.value(not button_left.value())
```
Aqui o `button_right` apenas tem a função de parar o programa. Quando premimos o  `button_left` ligamos o LED.
Temos o parâmetro `Pin.PULL_UP`: graças a ele poderíamos não usar resistências Pull-Up IRL. 
- Acerca dos valores dos botões:
    - Vemos na imagem acima que quando o botão da esquerda não é premido a entrada 23 está ligada aos 3.3V. Assim, o botão é Active Low e logo `button_left.value()==False` implica que o botão está premido.
    - No botão da direita temos o oposto. Quando ele não é premido temos o pino 18 ligado ao ground (tem um fio a ligar ao ramo do condensador). O botão é portanto Active High e `button_right.value()==True` ocorre quando o botão é premido.

## Classes e Asyncio
- Estas são 2 ferramentas muito úteis de MicroPython mas nem pensar que vou fazer um resumo sobre isto.