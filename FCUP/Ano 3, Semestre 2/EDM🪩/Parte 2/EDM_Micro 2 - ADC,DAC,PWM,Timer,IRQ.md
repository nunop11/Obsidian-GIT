# 2 - Analog
- Vimos na aula anterior pinos GPIO, em que a tensão emitida pelo MCU é apenas 0 ou 1 (lógico), que corresponde a 0V e 3.3V.
- Ora, podemos ter tensões diferentes destas, usando *saídas analógicas*.

## DAC
- O ESP32 tem um DAC (Analog to Digital Converter) que permite geral nos pinos 25 e 26 uma tensão entre 0V e 3.3V.
- Para isso, fornecemos ao DAC um número de 8 bits (de 0 a 255) que dá origem à tensão proporcional: $0$ dará $0\text{V}$ e $255$ dá $3.3\text{V}$. De resto, podemos fazer uma regra de três simples ou usar a equação do DAC:
$$V = \frac{3.3 \cdot n}{255}~~(\text{Volts})$$

- Em termos de implementação usamos a classe DAC:
```python
from machine import Pin, DAC

dac = DAC(Pin(25))

values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          25, 50, 75, 100, 125, 150, 175, 200, 225,
          245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]

for value in values:
    print(value)
    dac.write(value)
    input("Press Enter to continue...")
```
sendo que neste código damos ao pino 25 uma série de números, que causará tensões de 0 a 3.3V.

- Se medirmos as tensões emitidas com um multímetro, vemos que a relação é linear, mas temos uma ordenada na origem (que teoricamente não deveria lá estar). Mais concretamente, se dermos $0$ ao DAC a tensão emitida não é $0\text{V}$, mas sim $\sim0.1\text{V}$.
- Podemos então usar pinos DAC para emitir sinais específicos (como um seno, por exemplo).

## ADC
- O ESP32 tem também 6 pinos ADC (Analog to Digital Converter): pinos 32,33,34,35,37,38.
- Estes pinos podemos fornecer uma tensão até $3.6\text{V}$ e o ADC converte num número.

**WIDTH**
- Aqui surge uma coisa importante acerca do DAC: ao definir o pino no micropython podemos definir o parâmetro WIDTH com: `WIDTH_9BIT`, `WIDTH_10BIT`, `WIDTH_11BIT`, `WIDTH_12BIT`. Isto simplesmente define quantos bits o ADC usa para medir o sinal: se usarmos 9BITS então obteremos um número de 0 a 511 ($2^9-1$). Assim, usando-se o width $w$ podemos escrever:
$$ADC = V \cdot \frac{3.3}{2^{w}}$$
(a resolução será de $3.3/2^{w}$, porque temos os números de $0$ a $2^{w}-1$)

**ATTN**
- Na realidade, apesar de dizermos que o ADC mede tensões de 0 a 3.6V, ele só consegue medir tensões de 0 a 1V!
- Assim, para tensões acima desta gama temos que fazer *atenuação*: 
    - `ATTN_0DB`: tensões até $1\text{V}$
    - `ATTN_2_5DB`: tensões até $1.34\text{V}$
    - `ATTN_6DB`: tensões até $2\text{V}$
    - `ATTN_11DB`: tensões até $3.6\text{V}$
- A explicação destes valores é:
$$11 \text{dB} = 20\cdot\log_{10}\left(\frac{3.6}{1.0} \right)$$

**Aplicação**
- Usamos com a Classe ADC:
```python
from machine import Pin, ADC
adc = ADC(Pin(32))
adc.read()
```
- Se fizermos um gráfico $\text{ADC(V)}$ na gama $[0,3.6]\text{V}$ (ATTN_11DB) conforme variamos a Width obtemos:
![[image-2.webp|475]]
    - Cada cor corresponde a uma width: amarelo é 12Bits (vai até ~4000)
    - Vemos que a linearidade é pior que a do DAC, tendo-se dados bastante piores nas beiras da gama, tendo-se a mesma leitura do ADC para diferentes tensões.

- Se agora fizermos o gráfico $\text{ADC(V)}$ com 12 Bits conforme variamos a gama:
![[image-3.webp|475]]
    - Agora cada cor é uma gama AKA uma atenuação. Por exemplo, cinzento é `ATTN_6DB`, porque as medições param em ~2V. 
    - Ou seja, em todos estes gráficos variamos a tensão de 0 a 3.6V. No entanto em todos menos no 11dB chegamos à tensão máxima do ADC antes do fim da escala (na cinzenta isto aconteceu nos 2V, porque 1V medido no ADC corresponde a uma tensão de 2V com atenuação de 6dB). Para todas as tensões que, quando atenuadas, ultrapassam 1V o ADC simplesmente mede 1V.

## PWM
- A maioria dos MCUs têm ADCs, mas nem todos têm DACs. Invés disso, existe uma funcionalidade mais comum e que permite gerar sinais que *parecem* analógicos: PWM (Pulse Width Modulation).
- Isto consiste em geral um sinal periódico em que dizemos em que porção de 1 período temos nível lógico igual a 1. A esta porção chamamos de **duty cycle**. Ou seja:
![[image.webp|400]]
- Assim intuitivamente vemos que a tensão *média* de uma saída PWM será:
$$V = 3.3 \cdot \text{duty cycle}$$

- Ora, este sinal não é analógico. MAS
    - Se ele passar por um filtro passa-baixo as componentes de elevada frequência são eliminadas, ficando apenas a componente média. IRL, os sistemas mecânicos frequentemente aplicam um filtro destes ao sinal, tornando-o "analógico".
    - Independentemente, desde que a frequência seja suficientemente alta, estes sinais são basicamente analógicos. 
        - Por exemplo, se tivermos um LED ligado a um PWM, ao alterar o duty cycle nós apenas vemos uma variação da *intensidade* da luz. Não o vemos a piscar conforme o duty cycle.
        - Analogamente, no caso de um motor DC, ao variar o duty cycle não vemos o motor a parar e andar conforme este. Vemos o motor a rodar com velocidade proporcional ao duty cycle.

- Para aplicar isto fazemos algo tipo:
```python
from machine import Pin, PWM

pwm = PWM(Pin(21))

freqs = [1, 10, 100]
dutys = [10, 50, 90]

for freq in freqs:
    pwm.freq(freq)
    for duty in dutys:
        print("freq = {0}Hz, duty-cycle = {1}%".format(freq, duty))
        pwm.duty(int(duty*1023/100))
        input("Press Enter to continue...")

pwm.deinit()
```
- Em que notemos que para definir o duty cycle usamos um número de 10 bits:
$$\text{duty}~ = n(\%) \cdot \frac{1023}{100}$$
- A partir do momento que se define a frequência e duty do PWM, o ESP gera o sinal automaticamente, sendo que o sinal começa sempre em **1**.

### Servo
- No caso de um motor servo SG90, dar um impulso de 0.6ms coloca o motor na posição 0º e um impulso de 2.4ms coloca-o na posição 180º.
![[pwm.png]]
```python
from machine import Pin, ADC, PWM

adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

pwm = PWM(Pin(5))
pwm.freq(50)
pwm.duty(int(1.5/20*1024))
while 1:
    v = adc.read()
    a = (v-600)/(3200-600)*180
    t = (2.4-a/180*(2.4-0.6))
    pwm.duty(int(t/20*1024))

pwm.deinit()
```
- Aqui o duty/posição do Servo é definida pela tensão medida no pino 35.
- Como temos acima, a 50Hz, o período do PWM é 20ms.
- No código acima:
    - Começamos por medir a "tensão" `v` no ADC
    - A "tensão" medida na realidade é um número de 12 bits. As contas que fazemos para obter `a` consistem em resolver isso. Além disso, supostamente este código corresponde a uma tensão `v` medida num divisor de tensão
    - Por fim, convertemos `a` (a "verdadeira" tensão medida) no tempo de duração do impulso. A conversão em si não percebo uwu

## Polling e Interrupts
### Polling
- Vamos gerar um sinal PWM no pino 21. E vamos medir esse sinal no pino GPIO 5.
```python
from time import ticks_ms
from machine import Pin, PWM

pwm = PWM(Pin(21))
pwm.freq(1000) # frequency to measure
pwm.duty(512) # 50%

signal = Pin(5, Pin.IN)

count = 0

last = 0
lastState = 0

while 1:
    now = ticks_ms()
    if now - last > 1000:
        if last != 0:
            print(count)
        last = now
        count = 0

    state = signal.value()
    if lastState == 0 and state == 1:
        count += 1
    lastState = state
```

- Temos então um PWM de $1\text{kHz}$ com duty cycle de 50%. 
- A lógica deste código é: durante 1s (1000 ms) contamos todas as vezes que o sinal do PWM subiu de 0 para 1 (`lastState == 0 and state == 1`). Isto irá permitir fazer uma estimativa da frequência. Este método chama-se **polling**
- Este método funciona bem até frequências de $5.6\text{kHz}$. A partir daí o programa não consegue acompanhar o sinal PWM.

### Interrupts
- Vejamos agora como podemos usar **interrupts** para melhorar o código acima.
- Esta funcionalidade *para* o programa para correr uma função quando um certo trigger ocorre:
```python
from time import ticks_ms
from machine import Pin, PWM

pwm = PWM(Pin(21))
pwm.freq(10000) # frequency to measure
pwm.duty(512) # 50%

count = 0

last = 0

def increment(p):
    global count
    if p == signal:
        count += 1

signal = Pin(5, Pin.IN)
signal.irq(trigger=Pin.IRQ_RISING, handler=increment)

while 1:
    now = ticks_ms()
    if now - last > 1000:
        if last != 0:
            print(count)
        last = now
        count = 0
```
- Basicamente, quando o valor da tensão medida no Pino 5 sobe (`IRQ_RISING`), parasse o programa para correr a função `incremente()`
    - Honestamente não entendi muito bem o que é o parâmetro `p`
- Se quisessemos medir as descidas do valor do pino 5 usaríamos `IRQ_FALLING`.
- NOTA: IRQ significa "Interrupt ReQuest".

- Este método funciona bem até $30\text{kHz}$. A partir dessa frequência o irq começa a interromper-se a si próprio.
- Devemos notar mais uma coisa. O método *polling* será afetado por qualquer código dentro do loop while (como `sleep_ms()`). O método *interrupt* não seria afetado por isso! (O irq interrompe até o sleep)

## Timers
- A classe `Timer` do módulo `machine` permite colocar o sistema a automaticamente fazer contagens em certos intervalos de tempo:
```python
from machine import Pin, PWM, Timer

pwm = PWM(Pin(21))
pwm.freq(10000) # frequency to measure
pwm.duty(512) # 50%

count = 0

def print_cnt(t):
    global count
    print(count)
    count = 0

tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=print_cnt)

def increment(p):
    global count
    if p == signal:
        count = count + 1

signal = Pin(5, Pin.IN)
signal.irq(trigger=Pin.IRQ_RISING, handler=increment)

def loop():
    while 1:
        pass

try:
    loop()
except KeyboardInterrupt:
    print('Got Ctrl-C')
finally:
    tim.deinit()
```
- Aqui estamos a fazer medições das oscilações do PWM em 1 segundo e imprimindo as contagens feitas.
- Aqui temos a função `loop()` que tem apenas a funcionalidade de termos algo a funcionar, para depois podermos "interromper" e fazer contagens.
- Alternativamente a ter o modo `Timer.PERIODIC` em que se gera um sinal periódico, podemos usar `Timer.ONE_SHOT` em que o timer corre durante 1 segundo, imprime `count` e para.

## Low Power
- Quando temos o ESP alimentado por pilhas é essencial garantir o mínimo consumo de energia.
- O consumo de um MCU é normalmente indicado em $\text{mA}$.
    - Normalmente o consumo médio de um ESP é $45\text{mA}$ ($120\text{mA}$ se estivermos a usar WiFi). Tendo-se uma bateria com $2000\text{mAh}$ com um consumo de $120\text{mAh}$, o ESP32 ficaria ligado por menos de $17\text{h}=\frac{2000\text{mAh}}{120\text{mA}}$.
    - Se colocarmos o ESP32 em modo **DeepSleep** o consumo é apenas de $100\mu \text{A}=0.1\text{mA}$. Para uma bateria de $2000\text{mAh}$ consideremos que o ESP alterna entre 10min em DeepSleep e 5s ativado de modo que o consumo médio é $1\text{mA}$, o ESP ficaria ligado por $2000\text{h}\simeq83\text{dias}\simeq3\text{meses}$ !
- Isto é possível porque em modo DeepSleep a grande maioria dos componentes do ESP encontram-se desligados.
- O **consumo médio** de um ciclo do ESP pode ser calculado assim:
    - Consideremos um ESP num ciclo em que estamos $x$ minutos em DeepSleep e $y$ segundos em modo ativo normal. Consideremos que o consumo nestes modos é $0.1\text{mA}$ e $120\text{mA}$, respetivamente. Temos o consumo médio: $$\bar i =\frac{x\cdot60\cdot0.1\text{mA} + y \cdot 120\text{mA}}{x\cdot60 + y}$$(em que em baixo dividimos pelo tempo total de 1 ciclo destes, tendo-se sempre os tempos todos em segundos)
    - Ou seja, mais geral: $$\bar i= \frac{\Delta t_{deep}\cdot i_{deep} + \Delta t_{normal}\cdot i_{normal}}{\Delta t_{deep}+\Delta t_{normal}}$$
- Inversamente, sabendo que um circuito que esteja num modo energético com consumo $x$ (mA) permanece ligado por $y$ (h), então podemos definir a "capacidade" da pilha/bateria como:
$$C = x \cdot y~~~~(\text{mAh})$$
e daqui, considerando um ciclo com consumo médio $\bar i$, podemos definir o tempo que o circuito iria ficar ligado com esta pilha e este ciclo:
$$t=\frac{C}{\bar i}~~~~(\text{h})$$

- NOTA: Quando o ESP sai do modo DeepSleep, a contagem do `tick_ms()` é **reiniciada**. Isto costuma ser útil se quisermos que o ESP entre em DeepSleep de forma periódica.


**Acordar**
- Podemos usar o seguinte código que permite usar a ativação de um pino GPIO para "acordar" o ESP:
```python
from time import sleep
import machine
import esp32
from machine import Pin

led_red = Pin(21, Pin.OUT)
led_red.value(True)

causes = {
    1: "PWRON_RESET",
    2: "HARD_RESET",
    3: "WDT_RESET",
    4: "DEEPSLEEP_RESET",
    5: "SOFT_RESET"
}
cause = machine.reset_cause()
print(cause, causes[cause])

reasons = {
    0: "NO REASON",
    2: "EXT0_WAKE/PIN_WAKE",
    3: "EXT1_WAKE",
    4: "TIMER_WAKE",
    5: "TOUCHPAD_WAKE",
    6: "ULP_WAKE"
}
reason = machine.wake_reason()
print(reason, reasons[reason])

wakepin = Pin(14, Pin.IN)

esp32.wake_on_ext0(pin=wakepin, level=esp32.WAKEUP_ALL_LOW)

print('Im awake. Going to sleep in 5 seconds')
sleep(5)
print('Going to sleep now')
machine.deepsleep(10000)
```
de notar que, normalmente, os pinos GPIO desligam-se em modo DeepSleep.

- Outra forma de gerir o modo DeepSleep é diretamente dizer no código por quanto tempo iremos entrar no modo. Acima temos `deepsleep(10000)`, o que diz ao propgrama para entrar neste modo por 10 segundos.