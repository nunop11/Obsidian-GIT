## 0 - Preparação
- Testamos uma strip de leds e verificamos que a biblioteca originalmente planeada não funcionava de forma desejada
- Após procurar no platformIO, usamos a biblioteca makuna/NeoPixelBus

## 1 - objetivo A
Após receber o guião, dividimos o projeto nos seguintes objetivos:
- **A** 
    - Usar Sgo para reiniciar contador
    - Usar Sesc para entrar/sair de pausa
        - Quando em pausa, piscar os LEDs acesos
    - Apagar 1 LED a cada 2s
    - Usar o Serial para dar ordens: 'g' para reiniciar, 'p' para pausar, 'r' para retomar

- **B**
    - Ao clicar em Smore, acrescentar 1 LED (adiar contagem 1 intervalo)
    - Como alternativa ao botão, usar 'm' no Serial

- **C**
    - Entrar no *modo de configuração* ao premir Smore > 3s
        - Ao premir Smore novamente >3s, guardar e aplicar as alterações feitas
        - Se premirmos Sesc enquanto em modo de configuração, sair sem mudar nada
    - Enquanto em modo config, piscar o LED de baixo
        - A cor com que pisca indica a configuração que estamos a ajustar.
        - Os LEDs acima do primeiro preenchem conforme a opção selecionada no presente
        - *Smore* seleciona a configuração a alterar, *Sgo* seleciona a opção escolhida dentro disso
    - Alternativa Serial: 'c' para entrar em modo de configuração, 's' para sair e guardar, 'e' para sair sem guardar

CONFIGURAÇÕES POSSÍVEIS:
- **o1** - Tempo entre LEDs
    - LED de baixo pisca a branco
    - Clicar Sgo roda entre: 1s, 2s, 5s, 10s
    - Escrever numero no Serial

- **o2** - Efeito de contagem
    - LED de baixo pisca a verde
    - Clicar Sgo roda entre as opções, a aplicar ao LED que se vai apagar a seguir (o de cima)
        - Desligar no fim do intervalo
        - Na segunda metade do intervalo, pisccar rápido
        - Fazer fade out, de 100% no inicio para 0% no fim
    - Usar 'o' (off), 'b' (blink) e 'f' (fade) no Serial

- **o3** - Cor da contagem
    - LED de baixo pisca a azul
    - Sgo roda entre as opções: azul, verde, amarelo, branco
    - Usar 'b', 'g', 'y', 'w' no Serial (cada letra é a inicial de cada cor)

### A
- Começamos por fazer as bases.

#### Versão 1
- Fizemos a seguinte FSM:
![[fsm_v1|750]]
**Lógica da FSM**
- Temos 2 variáveiss globais `current, color`. 
    - `current` armazena o índice do LED mais alto aceso (Se `current==4`, então os 5 primeiros LEDs deverão acender). Assim, consoante vamos avançando no tempo, `current` vai reduzindo de `maxLed` até `0` : a quantidade de LEDs acesos vai diminuindo de cima para baixo.
    - `color` guarda a cor com que os LEDs devem acender.
- A contagem de tempo era feita usando `tis`.  
    - Usou-se "40" em `tis % 2000 < 40` porque o programa apenas atualiza a máquina de estados a cada 40ms, algo que foi feito para evitar ler oscilações e sinais errados dos botões.
- Optamos por ter a variável global `current`, porque vimos que isto é algo que poderia ser útil para os objetivos seguintes (especialmente B)

**Acender LEDs**
- No final de casa iteração, são ligados os LEDs
- Para isto, usamos uma peça de código que é igual para todos os estados. Como a cor a ligar é obtida conforme cada estado, basta usar a biblioteca escolhida para acender os LEDs.
- O processo de ligar os LEDs com esta biblioteca consiste em: 
    - ligar LEDs da strip com indice <= current com a cor `color` (LEDs abaixo)
    - ligar LEDs da strip com indice > current a preto - ficam apagados (LEDs acima do current)
    - Evidentemente, se tivermos `color==black` (como no estado 0) a strip fica apagada.

**green_blink, red_blink**
- Isto é uma notação usada para indicar que os LEDs piscaram a verde ou vermelho nestes estados.
- Em termos de código, isto consiste em atribuir à variável `color` o valor `red`/`green` quando `fsm1.tis % 500 > 200` e o valor `black` no caso contrário.
- Assim, em cada iteração atribuimos a `color` o valor de cor que terá nessa iteração apenas, de modo que o código de acender a strip funciona bem.

#### Versão 2
**Problemas da versão 1**
- A primeira versão rapidamente teve problemas. 
- Como tudo aquilo que depende de tempo usa o `tis` para funcionar, a transição para a pausa e o regresso para a contagem revelaram-se muito desafiantes. 
    - Imaginemos que estamos num certo LED e restam-lhe 100ms para desligar. Ao ativar a pausa mudamos para o estado 3 e o `tis` reinicia. Ao sair da pausa e regressar ao estado 1, voltamos a ter `tis == 0` e o LED ficará 2s ligado invés de 0.1s.
    - Então precisávamos de guardar o valor de `tis` mesmo antes de sair do estado 1 e forçar esse valor de `tis` ao retornar a este estado depois da pausa, o que não podemos fazer com uma máquina de estados.

**Solução arranjada**
- Assim, alteramos a nossa abordagem. Introduzimos uma nova variável *global*: `timeClk`
    - Esta variável guarda o tempo que passou desde que começamos a contagem, no total. Ou seja, desde o início da contagem até chegar ao estado 2 (End), `timeClk` irá de 0 a 10000 independentemente de quantas pausas fazemos.
    - Aqui notemos que a funcionalidade de colocar o estado 2 em pausa não existe. Estando no estado 2 apenas podemos reiniciar ou aguardar.
- Para concretizar isto fizemos uma segunda versão da FSM:
![[fsm_v2|750]]
**restarting**
- Temos uma quarta variável global: `restarting`. 
- Vejamos como o sistema funciona sem esta variável
    - Da maneira que definimos esta FSM, o programa começa no estado 0, que define os valores iniciais de `timeClk` e `current`. Começamos com os LEDs _apagados_.
    - Os LEDs acendem-se e a contagem começa quando premimos Sgo e passamos para o estado 1.
    - Mas imaginemos agora que estávamos nos estados 1,2 ou 3 e premimos Sgo para reiniciar a contagem. A FSM transita para o estado 0. Mas este ficaria apenas à espera que Sgo volte a ser premido para a contagem começar. Isso em princípio não é desejado.
- Assim, introduzimos `restarting`:
    - Quando o utilizador deseja reiniciar a contagem esta variável é posta =1 e a FSM transita para o estado 0 como antes.
    - Na iteração seguinte, já com a FSM no estado 0, invés de esperar que Sgo seja pressionado a FSM passa logo para o estado 1 e a contagem pode começar (conforme o fluxograma acima). 
    - Antes de acabar esta iteração, `restarting` é retornado a =0
- Esta variável permite então que o programa reinicie de forma instantânea.

**LEDs**
- Nesta nova versão mantivemos tudo aquilo indicado acima sobre `color` e como acendemos os LEDs.

#### Versão 2.1 - Serial
- Simplesmente introduzimos a funcionalidade Serial.
- Usamos uma variável *local* `r` para guardar a leitura da porta Serial (quando temos algo por ler). E a máquina de estados sofre as ligeiras alterações abaixo:
![[fsm_v2.1|750]]
quando nada é enviado através do Serial (por `r` ser local) teremos `r==0` e o sistema funcionará como se o terminal Serial não existisse.

## B
- Aqui, apenas incrementamos `current` quando Smore é premido. O programa feito até agora está feito de modo que isto não causará problemas.
- Este é um processo que não é representado na máquina de estados, o que não sei se é correto ou não.
- Da maneira que fizemos (só mesmo incrementar `current`) acontecerá isto:
    - Estamos no LED 3, com 0.5s restantes.
    - Premimos Smore
    - Passamos a ter o LED 4 aceso, que se apagará em 0.5s
- Isto parece estranho, porque pode acontecer o LED novo se apagar imediatamente depois de ser ligado. Mas isto estará correto porque, conforme indicado no guião, estamos a adicionar 1 intervalo (2s) à contagem.

%% ## C
- Para já, fiz este fluxograma (não é uma FSM!!!) para tentar planear o funcionamento desta secção:
![[lab1_b_v1|800]]

- A lógica é: temos valores default de cada uma das 3 configurações. Os botões ciclam entre eles.
- São introduzidas 4 novas variáveis globais `timeSelect,timeInt,mode,timColor` e 1 local `botColor`
    - `timColor` (color) - Cor com que os LEDs acendem durante a contagem. Este valor é guardado e aplicado quando se retomar a contagem. Os LEDs passama a acender com vermelho (no final da contagem) ou com `timColor`
    - `botColor` - Cor do LED de baixo. Isto é usado durante o modo de configuração, para indicar qual configuração está a ser adaptada. Como feito anteriormente, o `_blink` indica que temos esta cor a piscar, o que é aplicado abaixo para piscar
        - `current` - mesma variável que antes. Aqui ela tem a funcionalidade de dizer quandos LEDs acima do bottom estão acesos. O número de LEDs indica o número da opção selecionada de momento (1LED - timeInt=1s)
        - Como eu estou a pensar fazer isto funcionar para já: primeiro acendemos os LEDs todos até `current`. Depois, `if` estivermos em modo configuração, ligamos o LED bottom com cor `botColor`. Assim aproveitamos o código de trás
    - `mode` - Forma como o LED de cima pisca durante a contagem. Não sei como implementar isto

- No que toca a miplementar isto, teríamos apenas um monte de `if`'s a ver se os botões são premidos e a atualizar estas variáveis constante (arranjar forma eficiente de ciclar por variáveis, maybe com array) %%

## C
- Decidimos que a melhor forma de gerir esta parte do programa será ter listas com as opções
![[lab1_b_v2|800]]
- A lógica é: temos valores default de cada uma das 3 configurações. Para cada uma destas temos uma lista que contem as opções a escolher.  
- Tinha pensado em ter as listas:
```
char timeInt = ['1','2','5','a'];
char timeCol = ['b', 'g', 'y', 'w'];
char mode = ['o', 'b', 'f'];
```

- São introduzidas 3 novas variáveis globais `indtimeCol, indTimeInt, indMode` e 1 local `botColor` (além das 3 listas acima, que são globais)
    - `botColor` - Cor do LED de baixo. Isto é usado durante o modo de configuração, para indicar qual configuração está a ser adaptada. Como feito anteriormente, o `_blink` indica que temos esta cor a piscar, o que é aplicado no final da iteração, ao acender os LEDs
        - Para acender os X LEDs acima para indicar a opção X podemos usar o índice
        - Como eu estou a pensar fazer isto funcionar para já: primeiro acendemos os LEDs todos até ao `ind+1`. Depois, `if` estivermos em modo configuração, ligamos o LED bottom com cor `botColor`. Assim aproveitamos o código de trás

### Opção 2
- Outra alternativa, talvez melhor, é ter uma lista com 3 valores, os índices:
```
int index = [1,0,0]; // (indTimeInt, indTimeCol, indMode)
```
em que temos os valores default dos índices.
- Assim, temos 2 variáveis locais `ind, config` 
    - `ind` - índice da opção selecionada. Este é o valor que rodamos ao premir Sgo. Ou seja, fazemos algo do tipo: ```
        ind = index[config];
        if ReSgo { ind ++; }
        ...
        color = indTimeCol[ind]```
    - `indConfig` - índice da configuração. Permite decidir qual a configuração a ser ajustada, pelo que roda consoante premimos Sgo. Usamos como mostrado acima. Temos $$\textsf{config}=\begin{cases}
0 & ; & \textsf{Time} \\
1 & ; & \textsf{Color} \\
2 & ; & \textsf{Mode}
\end{cases}$$ (ou seja,no exemplo de cima temos `config==1`)
- Penso que é um benefício esta versão funcionar à base de alterar variáveis locais e ter variáveis globais constantes

- Ou seja funcionaria assim:
![[lab1_b_v3|500]]