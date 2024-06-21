# 3 - Serial
- Até agora vimos várias formas (GPIOs) de enviar 1 bit de informação, o que é suficiente para saber o estado de um botão ou para ativar 1 LED.
- Mas precisamos de formas de enviar e receber mais informação.

- O que vimos atrás pode ser considerado como protocolo em paralelo: 1 pino GPIO == 1 bit
- Vamos agora ver **protocolos em série** (Serial Interface). Isto consiste em mandar os bits em sequência.

## UART
- Universal Asynchronous Receiver/Transmitter
- Este protocolo é o mais simples e, como diz o nome, é assíncrono. Isto porque não existe necessariamente um clock: o MCU e o dispostivo em comunicação com ele decidem quantos bits serão transmitidos or segundo. 
- Para decidir isso temos o **baud rate**, que pode ter um de vários valores: 4800, 9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600. Ou seja, tendo-se um baud rate de $x$, cada bit tem a duração de $1/x$.

- Temos as entradas TXD,RXD que são de Transmissão e Recessão:
![[UART.webp]]
- Quando não há dados a ser enviados ("bus idle") ambas as linhas têm valor 1. 
- Sendo enviada informação, temos um *start bit = 0*, 8 bits de dados e um *stop bit = 1*.
    - Os bits de informação podem não ser 8, mas se não for dito nada no enunciado assumimos que são.
    - Os bits de informação são enviados do LSB para o MSB. Mas por vezes isto pode ser alterado.
- O stop bit pode ter uma duração pode ter duração de 1 ou 2 bits.
- Entre os bits de informação e o stop bit podemos ter o *bit de paridade*, que tem a função de garantir que o número de bits =1 é par ou ímpar (previamente definido), de modo a detetar erros de transmissão.
![[UART_bits.webp]]
- Ou seja, podemos resumir a sequência de dados a: $$\underbrace{0}_\text{start bit} ~, [8 \text{ bits de dados}],~\underbrace{1}_{\text{stop bit}}$$

**Aplicação**
- Usamos a classe `UART`:
```python
from machine import UART, Pin
from utime import sleep_ms

uart = UART(1)
uart.init(baudrate=9600, bits=8, parity=0, stop=1, tx=2, rx=4)

def send_msg(p):
    if p == bon:
        uart.write('L1')
    if p == boff:
        uart.write('L0')

def check_msg():
    if uart.any():
        msg = uart.read().decode()
        if msg == 'L1':
            led.value(True)
        if msg == 'L0':
            led.value(False)

led = Pin(21, Pin.OUT)
led.value(False)

bon = Pin(23, Pin.IN, Pin.PULL_UP)
bon.irq(trigger=Pin.IRQ_FALLING, handler=send_msg)

boff = Pin(18, Pin.IN, Pin.PULL_UP)
boff.irq(trigger=Pin.IRQ_FALLING, handler=send_msg)

def loop():
    while True:
        check_msg()
        sleep_ms(10)

try:
    loop()
except KeyboardInterrupt:
    print('Got Ctrl-C')
finally:
    uart.deinit()
    bon.irq(handler=None)
    boff.irq(handler=None)
    print("Finishing...")
```

- A sequência de 8bits é lida pelo python como um byte, pelo que temos que converter de volta em string usando `uart.read().decode()`
- Acima definimos `parity=0`. Isto significa que queremos que o bit paridade seja escolhido de modo que haja número par de 1s. Podíamos ter posto `parity=1`, que dava 1s ímpares. Temos ainda `parity=None` que faz com que a paridade não seja considerada e este bit extra não exista.
- A mensagem `'L0'` referida acima pode ser enviada com a sequência:
![[uart sequencia.png]]
em que usamos a tabela ASCII para converter, em que cada símbolo corresponde a um número 0-127.

## SPI
- UART é assíncrono, SPI e I2C são métodos síncronos, porque o MCU e o dispostivo com que ele está a comunicar têm um sinal de relógio comum. Nestes 2 protocolos temos ainda os conceitos de *master* (o ESP32) e *slave* (dispositivo)

- SPI = Serial Peripheral Interface 
![[400px-SPI_8-bit_circular_transfer.webp]]
- Em SPI temos então a ligação de clock (SCLK), MISO (Master Input Slave Output) e MOSI (Master Output Slave Input). Os bits são enviados ao ritmo do clock.
- Para comunicar entre 1 Master e vários Slaves temos entradas de seleção:
![[350px-SPI_three_slaves.webp]]
(sendo que apenas a entrada MISO do Slave selecionado será ativa. As restantes estarão em modo "alta impedância")
- Neste protocolo podemos então ter emissão e receção de dados em simultâneo!

**Aplicação**
- Usamos a classe `SPI` do módulo `machine`.
- Ao fazer o `init` da classe definimos:
    - Identificador (1 ou 2 ?)
    - Frequência do relógio (`baudrate`)
    - Pinos a usar para ligar SCK, MISO, MOSI ao 
    - Modo SPI : polaridade e fase. Este modo pode ser definido explicitando `polarity,phase` ou usando os modos 0,1,2,3:
![[spi-modes.webp]]
(A polaridade define se o relógio em repouso é igual a 1 ou 0. A phase decide em que parte da onda medimos as oscilações)
- Os pinos de seleção indicados acima (se necessários) são definidos com pinos GPIO no programa.

- Vejamos um exemplo de código:
```python
from machine import Pin, ADC, SPI

spi = SPI(1) # spi 1 (?)
spi.init(baudrate=2000000, firstbit=SPI.MSB, polarity=0, phase=0,
    sck=Pin(14), mosi=Pin(12), miso=Pin(13))

cs = Pin(27, Pin.OUT) # sinal de select (SS)
cs.value(1) # o select é ativo no 0 !

adc = ADC(Pin(33))
adc.atten(ADC.ATTN_11DB)  # 3.6V
adc.width(ADC.WIDTH_9BIT) # 0..511

cmd_byte = 0b00_01_00_10

def loop():
    while True:
        data_byte = int(input("Enter pot position (0..255): "))

        cs.value(0)
        spi.write(bytes([cmd_byte, data_byte]))
        cs.value(1)

        print('ADC value: ', int(adc.read() / 2))

try:
    loop()
except KeyboardInterrupt:
    print('Got Ctrl-C')
finally:
    spi.deinit()
    print("Finishing...")
```
(este código serve para interagir com um potenciometro digital, mas não é o que interessa mais)
- Temos:
    - Podemos definir se é o MSB ou LSB que vem primeiro no `init`
    - Acerca do command byte idk. Temos isto na datasheet do potenciometro:
      ![[SPI_waves.webp|400]]
    - Vemos que na realidade são enviados 16 bits, 8 de command e 8 de dados.

## I2C
- Temos 2 linhas: *SDA* (Serial DAta) e *SCL* (Serial CLock)
- As ligações são feitas nesta forma:
![[I2C.webp]]
em que não existe forma elétronica de selecionar com que slave o master quer comunicar. Para isso cada slave terá um endereço de 7bits  usado para comunicar.
- Temos resistências Pull-Up porque as ligações são feitas com saída em dreno-aberto.

**Aplicação**
- Usamos a classe `I2C` do módulo `machine`, chocante.
- Ao fazer o `init` da classe definimos:
    - Identificador (0 ou 1 ?)
    - Frequência do relógio (`freq`)
    - Os pinos onde se liga SDA e SCL
- Para outro contexto de ligação a um potenciometro digital temos:
```python
from machine import Pin, ADC, I2C

i2c = I2C(1, freq=100000, scl=Pin(25), sda=Pin(26))

adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)  # 3.6V
adc.width(ADC.WIDTH_9BIT) # 0..511

I2C_ADDR = 0x2C
inst_byte = 0b00000_000

def printI2CDevices():
    print('Scan i2c bus...')
    devices = i2c.scan()
    print('Found {0} I2C device(s): '.format(len(devices)), end='')
    for device in devices:  
        print('{0} '. format(hex(device)), end='')
    print()

def loop():
    while True:
        data_byte = int(input("Enter position (0..255): "))

        if data_byte == -1:
            printI2CDevices()
        elif data_byte == -2:
            buf = i2c.readfrom(I2C_ADDR, 1)
            print('Position:', buf[0])
        else:
            i2c.writeto(I2C_ADDR, bytes([inst_byte, data_byte]))
            print('ADC value: ', int(adc.read() / 2))

try:
    loop()
except KeyboardInterrupt:
    print('Got Ctrl-C')
finally:
    print("Finishing...")
```
- Temos:
    - A função `printI2CDevices()`, que nos mostra que o ESP consegue fazer scan e determinar quais os endereços dos dispostivos ligados em I2C.

- Na prática pode ser mandado um número de bytes diferente conforme o dispositivo slave. Neste caso, ao escrever temos 4 bytes, tal temos em `i2c.writeto(I2C_ADDR, bytes([inst_byte, data_byte]))`:
![[I2C_waves.webp|550]]
- O primeiro byte enviado consiste no endereço do potenciometro digital, `I2C_ADDR`. Mas na prática o endereço do dispositivo tem apenas 7 bits; o 8º consistem num bit que indica se estamos a fazer leitura (1) ou escrita (0): $R/\overline{W}$. O ESP faz isto sozinho.
    - No máximo podemos ligar o ESP a 4 dispositivos por I2C

- A comunicação é começada por uma **start condition**: Descida de SDA com SCL=1. A comunicação é encerrada por uma **stop condition**: Subida de SDA com SCL=1. Todas as outras transições de SDA ocorrem com SCL=0.

- Por fim, notemos que em I2C na realidade são enviados conjuntos de **9 bits**: no final de todos os conjuntos de 8 bits temos um **bit de acknowledgement** que serve para saber se está tudo bem. 
    - O bit a seguir ao byte com os dados mandados na leitura/escrita serve para o master/slave confirmar que receberam os dados. O bit a seguir ao endereço serve para o slave confirmar que está presente.
    - Se $\text{ACK}=1$ a mensagem não foi bem trasmitida, se $\text{ACK=0}$ correu tudo bem.


