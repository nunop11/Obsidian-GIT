# WiFi
- O ESP32 tem WiFi e Bluetooth. Veremos como usar WiFi com código.
- O ESP pode ligar-se a uma rede existente: *Station (STA_IF)* **OU** criar uma rede WiFi / funcionar como um *Access Point (AP_IF)*

## STA
- Começamos por dar o nome (SSID) e password da rede wifi. Normalmente colocamos isto no **boot.py**:
```python
# from mysecrets import ssid, password
import time
import network

ssid = 'mySSID'
password = 'myPassword'
wlan = network.WLAN(network.STA_IF) # ligar a rede
wlan.active(True)
if not wlan.isconnected():
    print('Connecting to network...')
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        print('.', end='')
        time.sleep(0.1)
    print(' Connected!')
print('network config:', wlan.ifconfig())
```

- Como vemos comentado acima, podemos colocar o SSID e a password num ficheiro python aparte
- No final do código temos o print de `wlan.ifconfig()`, o que corresponde a fazer print do IP. O output do código acima será algo do tipo:
![[wifi ligacao.png]]

### REST
- Os serviços REST consistem em servidores que permitem aceder a dados (normalmente em formato json). Uma das APIs acessíveis é de metereologia, como vimos na aula PL. 
- Após login no website do API podemos arranjar uma API Key. Usando o código abaixo podemos ver como usar isto para consultar o URL:
```python
from time import sleep
import urequests
from mysecrets import api_key
from ujson import dumps

def prettify(s):
    i = 0
    for c in s:
        if c in ['[', '{']:
            print(c)
            i += 2
            print(i*' ', end='')
        elif c in [']', '}']:
            print("")
            i -= 2
            print(i*' ', end='')
            print(c, end='')
        elif c == ',':
            print(c)
            print((i-1)*' ', end='')
        else:
            print(c, end='')
    print("")

while True:
    location = "Porto"
    url = "http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&appid={1}" \
        .format(location, api_key)
    r = urequests.get(url).json()
    prettify(dumps(r))
    print('Estão {0} graus na cidade do {1}, prevendo-se um máximo de {2} graus!' \
        .format(r["main"]["temp"], r["name"], r["main"]["temp_max"]))
    sleep(5)
```

## Servidor
- Podemos usar o ESP32 como um servidor web.
- No website do prof temos um exemplo usando o módulo [micropython-aioweb](https://github.com/wybiral/micropython-aioweb), que é colocado no ESP32 através do ficheiro `web.py`. Para entender melhor, consultar este github. Temos então:
```python
import web # ir buscar ao github do módulo e meter no ESP32
import uasyncio as asyncio

app = web.App(host='0.0.0.0', port=80)

# root route handler
@app.route('/')
async def handler(r, w):
    # write http headers
    w.write(b'HTTP/1.0 200 OK\r\n')
    w.write(b'Content-Type: text/html; charset=utf-8\r\n')
    w.write(b'\r\n')
    # write page body
    w.write(b'Hello world!')
    # drain stream buffer
    await w.drain()

# Start event loop and create server task
loop = asyncio.get_event_loop()
loop.create_task(app.serve())
loop.run_forever()
```

- Para aceder o site vamos ao 1º número impresso no `boot.py` quando imprimimos o IP. No caso do output mostrado acima isso é: "10.0.5.117". Se colocarmos isto no browser deveremos obter a página gerada no ESP.
- Podemos ainda colocar um ficheiro `html` no ESP e depois abri-lo:
```python
async def index_handler(r, w):
    f = open('index.html')
    w.write(f.read())
    f.close()
    await w.drain()
```
- No website do prof temos um exemplo com um `index.html` e um `main.py` que mostram como fazer o ESP mostrar um html que tem botões que permitem ligar LEDs. Isto pode ser útil para projetos futuros, podendo-se usar o website para controlar coisas do python.

## MQTT
- Este é um protocolo que podemos usar invés do HTTP. O ESP32 deixa de atuar como um servidor, passando ele e o dispositivo que lhe quer aceder (por exemplo o PC) a ser ambos clientes, ligando-se a um terceiro elemento: o broker que negoceia a troca de mensagens entre eles
- Temos então no website outro exemplo de como ter uma página que permite controlar LEDs. Usa-se um "broker" online. Meh.