## gchannels
### CLASS: command frame
- Esta classe define um frame dos comandos que recebemos. Dentro dela temos os parametros:
    - `suffix` - indice ou ordem do comando, veremos abaixo
    - `command` - nome do comando que estamos a trata
    - `text, value` - as partes texto e numerica do comando

- A classe tem ainda as funções:
- `command_is` 
    - Compara uma string `c` ao `command`. Se forem iguais retorna 1, senão 0. 
    - A função `strncmp` dá 0 se iguais e 1 se diferentes
    - Diz se um string c é o comando atual

- `command_prefix_is` 
    - Recebe um string `c`. Definimos `i` que é o comprimento de `c` ou um tamanho máximo definido
    - Usamos `!strncmp` para comparar `c` aos primeiros `i` carateres de `command`
        - Se forem iguais então `c` é *prefixo* de `command` 
        - O **sufixo** será o que vem depois de `c`, então colocamos `suffix=atoi(command+i)`
        - Notemos que `atoi` converte um string para inteiro.
    - Esta função faz isto: `command='SET10'` e inserimos `c='SET'` logo esta função atribui `suffix=10`
    - `suffix` é variável global e guarda o sufixo/indice do command

### CLASS: gchannels 
- Esta classe trata de enviar, ler e processar comandos.
     - Comandos têm formato `COMMAND PARAMETER;`
    - Tokens têm formato `TOKEN;`
    - Na realidade, a função de enviar um carater, na realidade só o mete num buffer. O buffer é constantemente preenchido, enviado, esvaziado, repetir

- A class funciona +/- como uma FSM, tendo um parametro `state`. 
- As funções usadas para enviar e processar comandos são definidas ao inicializar a classe.

- Processar um carater funciona numa FSM na função `process_char` e é algo assim:
    - se estivermos no estado `gs_wait_for_data` então vamos analisar o carater `b` como sendo o primeiro do comando ou token. Passamos ao estado `gs_reading_command` ou `gs_reading_token`
    - se o carater `b` for um espaço, apagamos o carater anterior do comando
    - quando estamos a ler um *comando* e `b` é `;` ou `Enter` o comando acabou e processamos. Nesse caso:
        - Separamos a parte texto (`COMMAND`) e a parte numerica (`PARAMETER`), que são separadas por um espaço
        - Após separadas são guardadas em `frame.text` e `frame.value`
        - O `frame` é enviado para a função `process_command` e podemso analisar este comando
    - No caso de estarmos a ler um *token* e `b` indica o fim, processamos igual. Mas agora só temos parte numérica. 
    - Quando não marcamos o fim e ainda não chegamos ao limite de tamanho do buffer, guardamos `b` no buffer

### CLASS: Commands list
- Esta classe consiste numa lista de comandos, num formato `items[i]`, sendo a lista de items um dos parametros da classe. Abaixo temos os outros parametros
- Depois temos uma parte para gerir a lista de comandos: `commands_list_t`
    - Temos uma série de funções para registar um comando, sabendo o seu nome e pointer. Várias funções recolhem estas informações para `items[count]`:
        - `_type` - aparte - string, int ou float
        - `pvalue` - aparte - pointer, pode ser pivalue (int), psvalue (string) ou pfvalue (float)
        - `max_string_size` - aparte - (string apenas)
        - `command` - comum - copiamos o `command_name` para este parametro de `items[count]`
        - `command_hash` - comum - hash calculada para identificar e comparar comandos facilmente
        - `send, recv` - comum - dois parametros para indicar se um comando deve ser enviado ou recebido
        - `sparse_send` - comum - para indicar se um comando deve ser enviado sparse (enviar sparse são comandos que enviamos, até atingir um numero maximo de parametros)
        - `store` - comum - diz se é para armazenar
    - Temos uma função `process_read_command` (**IMPORTANTE**) para processar um comando `frame_data` que veio da função`process_char` acima. 
        - Recordemos que esta função gera um `frame` com os parametros `text` e `value` que nos dão o nome e valor do comando
        - Começamos por calcular o hash do frame
        - Vamos iterar por todos os comandos dentro de `items` (dentro da lista de comandos) , procurando um comando que coincida com `frame`
            - Se o item `i` tiver `recv==0` não devíamos de o estar a ler e passamos ao próximo
            - Comparamos o hash de `items[i]` ao hash do `frame`. Isto é mais rapido a comparar.
            - Se o hash for igual, comparamos os nomes usando `command_is`
            - Se os nomes forem iguais, o índice do comando `frame` que estamos a ler é `idx=i`. Paramos de iterar e procurar o comando
        - Quando encontramos, colocamos o *valor* do `frame` no comando a que ela corresponde
        - Ou seja, *esta função atualiza o valor de um comando*

- Finalmente, temos 2 funções para enviar comandos.
    - Elas usam a classe `gchannels` para enviar os comandos. Usam as funções `send_command` que vimos acima e que se adapta a se estamos a enviar strings, ints ou floats

## file_gchannels
- Este ficheiro apenas tem uma serie de funções que usam LittleFS, uma biblioteca para ler, processar e enviar ficheiros no raspberry pi pico
- `send_file`
    - envia um ficheiro `filename` via `gchannels`, usando a classe e funções do `gchannels.cpp`
    - enviamos o conteudo byte a byte para poupar a memoria

- `save_commands`
    - recebe um `commands_list_t` e escreve todos os comandos num ficheiro `filename`

- `load_commands`
    - Funciona basicamente igual ao `send_file`
    - Esse apenas lia o ficheiro e enviava tudo, este lê o ficheiro e processa cada carater com `process_char` 
    - Assim, o ficheiro conterá uma lista de comandos que vamos processar e guardar 
        - PENSO que dentro do `process_char` podemos processar e registar o comando com a class de `command_list`

## control
- Este ficheiro é basicamente uma FSM enorme que controla coisas no robot. Ela está dividida entre 2 funções:
    - `next_state_rules` - decide qual o próximo estado
    - `state_action_rules` - decide o que fazer em cada estado
    - Estas 2 funções vêm do `state_machines.cpp`
- Alguns estados:
    - *MOVER NA PISTA R@F*
    - Calculamos `e_xy` que dá o erro entre a posição estimada e a posição em que devíamos estar na trajetória 
    - **0** - Robot parado
        - Modo idle
        - Define a velocidade e vel angular 
    - **1** - Ir para caixa 1
        - Vimos para este se estávamos em **0**, a parede está a mais de 10cm, antes estava a menos de 5cm (afastamos rápido) e TIS > 1s
        - Seguir linha até caixa
    - **2** - Ligar solenoide (eletromagnet) e pegar na caixa
        - Vimos para este estado se estávamos em **1** e a parede está a menos de 4cm
        - Seguir linha
    - **3** - Recuar com a caixa
        - Vimos para este estado se estávamos em **2** e TIS passa 0.1s
        - Ter solenoide ligado daqui adiante
        - Definir $v=-0.1,\omega=0$ para recuar
    - **4** - Virar para trás
        - Vimos para este estado se estávamos em **3** e temos `rel_s` abaixo de $-0.12$ m
        - Definir $v=0,\omega=2.5$ para rodar no sítio
    - **5** - Viajar para localização final da caixa
        - Vimos para este estado se estávamos em **4** e temos `rel_theta` acima de 170º
        - Seguir linha
    - **6** - Avançar um pouco enquanto rodamos para meter a caixa no sítio
        - Vimos para este estado se estávamos em **5** e todos os IRLine vêm uma linha
        - $v=0.05,\omega=-0.2$
    - **7** - Não sei
        - Vimos para este estado se estávamos em **6** e não sei
        - Seguir linha
    - **8** - Largar caixa e recuar
        - Vimos para este estado se estávamos em **7** e TIS > 2s
        - Desligar solenoide
        - Durante 2ms meter $v=-0.1$
    - **10** - Teste 
    - *TESTES DE PID*
    - **100** - Parar controlo remoto
        - Estado entrado manualmente para testes
        - Vimos parar a este estado se estávamos em `ts_set_theta` e o erro `e_xy` é menor de 5cm
        - $v_{req}=\omega_{req}=0$
    - **101** - Ligar controlo remoto
        - Estado entrado manualmente para testes
        - Ligar modo de controlo `cm_kinematics` - controlamos $v,\omega$ do robot diretamente
        - Definimos $v=v_{req},\omega=\omega_{req}$
    - **102** - Controlar o PID
        - Estado entrado manualmente para testes
        - Ligar modo de controlo `cm_pid`
    - *MODOS DE MOVER*
    - **ts_set_theta** - Modo "set theta"
        - Ligar modo de controlo `cm_kinematics`
        - Aplicar função `set_theta` do `trajectories.cpp`
    - **ts_goto_xy** - Modo "ir para ponto x,y"
    - **ts_follow_line** - Modo "seguir linha"
    - **ts_follow_circle** - Modo "seguir circulo"
    - **ts_follow_track** - Modo de seguir pista com sensor IR
        - Todos estes últimos 4 funcionam igual ao `set_theta`
        - Todos estes estados são entrados manualmente ou noutros ficheiros
    - *CONTROLAR TENSÃO*
    - **200** - Forçar paragem dos motores
        - Vimos para este estado se estávamos em **202** com TIS > 2s e nenhum IRLine vê uma linha  
        - Forçamos $u_{1}=u_{2}=0$
    - **201** - Testes remotos de tensão
        - Estado entrado manualmente
        - $u_{1}=u_{1req},u_{2}=u_{2req}$
    - **202** - Igualzinho ao 201
        - A diferença é que podemos ir para o 200
    - **203** - Erro. Para testar mensagens de erro?
        - Reencaminha para o estado anterior
    - *MOTOR BENCH*
    - **mb_heat_motor**
        - Modo controlo `cm_voltage`
        - Coloca em $u_{1}$ a tensão de warm-up do motor bench
    - **mb_goto_voltage**
        - Vimos para este estado se estávamos em `mb_heat_motor` e TIS passa o tempo de warm-up do motor bench, em que se coloca $u_{1req}$ a zero
        - Só liga modo de controlo `cm_voltage`
    - **mb_acc_measure**
        - Vimos para este estado se estávamos em `mb_goto_voltage` e TIS passa o tempo de settle do motor bench, em que se zera as somas de i,w,n
        - Permite enviar uma mensagem ao robot
        - Vai-se fazendo a soma de valores medidos de corrente e $\omega$ e guarda-se o número de medições
        - Quando eventualmente temos n > total_measures:
            - É calculada a média de $i,\omega$ : $\Delta i/n,\Delta \omega/n$ 
            - A tensão $u_{1}$ e a corrente/velocidade angular média são enviadas usando `send_string` do `gchannels.cpp` 
            - Incrementar  $u_{1req}$ em 1 step de voltagem
                - Se com este incremento $u_{1req}$ não passa a tensão máxima, zeramos $i,\omega,n$ e voltamos a `mb_goto_voltage` (em que voltaremos a este estado)
                - Se passamos a tensão máxima, zeramos $u_{1req}$ e vamos para **200** - Houve erro nos cálculos então paramos tudo
        - Esta função faz um varrimento? Variamos a tensão em steps. Para cada valor de $u_{1}$ calculamos $\overline{i},\overline{\omega}$.
- Criamos uma instância da classe FSMs, em que colocamos a FSM de controlo (que vimos acima) e a LED_fsm, que controla o LED do robot para indicar o estado (ver `state_machines.cpp`)

## motor_bench (mb)
- Apenas tem a classe `motor_bench_t` que tem um monte de parametros relacionados a tensões e coisas do motor
- Literalmente temos estes valores só:
    - `warm_up_voltage` = 5 (volts)
    - `warm_up_time` = 4 (segundos???)
    - `settle_time` = 1.5 (segundos???)
    - `total_measures` = 32 (numero de medições a considerar)
    - `voltage_step` = 0.25 (incremento de tensão)
    - `max_voltage` = 5.1 (volts)

## state_machines (FSM)
*STATE_MACHINE* **(CLASSE FSM)**
- Isto é uma classe `state_machine_t` que nos permite ter FSM completas
- Temos os parâmetros:
    - state, next_state, prev_state
    - tes_ms, tis_ms, tis, actions_count
- E as funções:
    - `set_next_state` - coloca um valor `astate` em `next_state` *sem fazer mais nada*
    - `force_state` - coloca o valor `astate` em `next_state`. Chama as 2 funções seguintes para forçar o estado:
        - `update_state` - função normal de atualizar estado (atualizar state, prev_state), atualizar tes (tempo de entrada no estado) e meter tis a zero. Aplicamos `do_enter_state_actions`, que por sua vez aplicar `enter_state_actions_rules`. Acho que pode ser costumizado
        - `do_state_actions` - incrementar `actions_count` e aplicar a função `state_actions_rules` que é costumizável ao criar a instância da classe FSM, como fizemos em `control`
    - `calc_next_state` - atualiza TIS e aplica `next_state_rules` - isto é a função que determina se mudamos de estado e para qual. Ela é definida ao inicializar como fizemos em `control`
    - `time_since` - calcula diferença de tempos entre "presente" e `when`
    - `do_state_actions` - só aplica o `state_actions_rules` e incrementa `actions_count` 
        - Aplica as ações necessárias no estado

*STATE MACHINES (PLURAL)* **(CLASSE FSMs)**
- Esta classe contem várias FSM dentro dela
- Assim temos os parâmetros:
    - `psm[]` - Lista de FSM que são da classe acima `state_machine_t`, pelo que têm todos os parametros e funções acima
    - `count` - número de FSM guardadas em `psm`
- E temos as funções:
    - `register_state_machine` - recebe uma FSM e coloca-a em PSM se ainda não enchemos a lista
    - `calc_next_states`, `update_states`, `do_enter_states_actions`, `do_states_actions` - fazem o mesmo que as funções da classe FSM (`calc_next_state`, `update_state`, etc) só que calculam para **todas as FSM dentro** de `psm`. Notemos que aplicam as funções da classe FSM para cada FSM
    - `step` - Usada para iterar o sistema. Aplica as funções `calc_next_states`, `update_states` e `do_states_actions`. Ou seja:
        - Ver se e para que estado mudamos
        - Atualizar para o estado novo se necessário
        - Aplicar as ações do estado novo

## pico4drive
- Esta classe permite controlar e aproveitar esta placa
- Inicializamos os pinos, um SerialTiny para comunicar entre o RP2040 e o pico4drive e definimos as configurações dos pinos analog
    - Definimos ainda todos os pinos como outputs
- Temos ainda as funções:
    - `update` - lemos o SerialTiny. O valor `b` nele permite calcular a voltagem da bateria EEE o estado do botão
    - `voltage_to_PWM` - usando a voltagem da bateria obtemos o PWM correspondente a uma tensão `u`
    - `set_driver_PWM` 
        - Temos um `PWM_max` que é o valor máximo que podemos meter no PWM
        - Queremos introduzir um valor `new_PWM` no motor
        - Num pino metemos `PWM_max`. No outro pino metemos `PWM_max - abs(new_PWM)`
        - Esta função existe em 2 versões: uma em que damos 2 pinos `a,b` e outra em que damos o número de um dos driver, pelo que a função seleciona logo os 2 pinos desse driver
    - `set_driver_voltage` - Com `voltage_to_PWN` obtemos o PWM correspondente à nossa voltagem `new_voltage`. Ao colocar esse PWM no motor, estaremos a meter essa voltagem no driver.

## PID
- implementa e calcula um PID
- Não vou explicar muito mas isto aplicar estruturas masi complexas de CPP
- Os parametros que temos são: Kfd, Kf, Kc, Ki, Kd
- Uma interpretação do chat para estes parametros:
$$u(t)=K_{p}e(t) + K_{i}\int e(t)dt + K_{d}\frac{de(t)}{dt} + K_{f}~r(t) + K_{fd}\frac{dr(r)}{dt}$$
em que $r(t)$ é o canal de referência

## robot
- Este ficheiro principalmente calcula coisas do robot
- Temos a classe `robot_t` que tem os parâmetros:
    - `stopped` - diz se está parado ou não
    - `wheel_dist` - distância entre as rodas (12.5cm)
    - `wheel_radius` (6.89cm/2)
    - `dv_max`, `dw_max` - incrementos máximos de velocidade da roda e velocidade angular do motor
    - `dt` (40ms) - intervalo entre iterações do código
    - `follow_k`, `follow_v` - fatores de ganho 

- Temos as funções:
    - `odometry` - fa calculos de $v,\omega,x,y$ estimados
        - Para $\omega$ : $w_{ie}=\text{encoder}_{i} \cdot \frac{2\pi}{64 \cdot 2 \cdot 1920}$
        - Para $v$ : $v_{ie}=w_{ie} \cdot \text{raio roda}$
        - Para $v$ do carro : $v_{e}=\frac{v_{1e}+v_{2e}}{2}$
        - Para $\omega$ do carro : $\omega_{e}=\frac{v_{1e}-v_{e2}}{\text{dist entre rodas}}$ 
        - Tendo em conta estes valores, podemos estimar o quanto andamos e quanto rodamos em `dt` : $ds=v_{e}dt~~,~~d\theta=\omega_{e}dt$
        - Assim: $$\begin{align*}x_{e} &= x_{e}^{(\text{prev})} + ds\cos(\theta+ \tfrac{1}{2}d\theta)\\y_{e} &= y_{e}^{(\text{prev})} + ds\sin(\theta+ \tfrac{1}{2}d\theta)\\\theta_{e}&= \theta_{e}^{(\text{prev})} + d\theta\end{align*}$$
        - Temos ainda `rel_s` e `rel_theta` que são o somatorio dos valores de $ds,d\theta$. Ou seja, medem o *displacement radial e angular total* relativo à posição inicial do robot
    - `setRobotVW` - alteramos os valores de `v_req` e `w_rep` para serem iguais a uns certos `Vnom`, `Wnom`. Usado acima no `control.cpp`
    - `acelerationLimit` 
        - Determinamos a diferença `dv` entre  a velocidade requerida `v_req` e a velocidade `v_ref`, repetindo para `w_req` e `w_ref`
            - `v_ref` e `w_ref` serão valores que indicam a velocidade atual, logo `dv` e `dw` indicam o quanto temos que variar a velocidade para ficar como queríamos 
        - Aplicamos a função  `constraint` para `dv` e `dw`:
            - Se estiverem `-dv_max < dv < dv_max` então temos `dv = dv`
            - Se tivermos `dv > dv_max` temos `dv = dv_max`
            - Se tivermos `dv < -dv_max` temos `dv = -dv_max`
        - Notemos que a variação da velocidade com um `dt` reduzido é efetivamente a **aceleração** linear `dv` e angular `dw`. Assim, esta função garante que apenas aceleramos dentro dos limites estipulados
    - `calcMotorsVoltage`
        - Tendo em conta o modo de controlo fazemos:
            - Em `cm_voltage` escolhemos e temos logo a tensão dos motores e a função acaba aqui
            - Em `cm_pid` controlamos `w1ref` e `w2ref` diretamente 
            - Em `cm_kinematics` calculamos v1,v2,w1,w2 ref com as equações de cinemática do robot diferencial
        - Usando os valores de referencia e coisas do PID calcula-se u1 e u2
    - Depois tem funções para seguir linhas do IRLine que não importa
    - Tem 2 funções de mandar comando que são importadas do gchannels e estão aqui para facilitar o uso, basta fazer  `robot.send_command(X, Y)`

## trajectories
- Primeiro, temos uma compilação de funções para vir buscar:
    - `sqr` - $x^{2}$
    - `norm` - $\sqrt{x^{2}+y^{2}}$
    - `normalize` - $x=x/\text{norm},y=y/\text{norm}$ -- altera 2 variáveis `x,y` diretamente com floats sem retornar nada
    - `dist` - $\sqrt{(x_{1}-x_{0})^{2}+ (y_{1}-y_{0})^{2}}$ -- calcula a distância entre 2 pontos $(x_{0},y_{0}),(x_{1},y_{1})$
    - `normalize_angle` - pega em `angle` e força a estar no range $[-\pi,\pi]$
    - `diff_angle` - calcula a diferença *normalizada* entre ângulos *normalizados* usando a finção acima

- Temos ainda a classe `trajectory_t` que pode ser chamada fora deste ficheiro com `traj.`
- Parâmetros:
    - `Pf.x,Pf.y` - coordenadas do ponto final / destino
    - `thetaf` - orientação com que o robot deve chegar ao destino
    - `C.x, C.y` - coordenadas do centro (seguir circulo) 
    - `Pi.x, Pi.y` - coordenadas de onde o robot devia começar (pode não começar aí, pelo que fazemos correções)
    - `radius` - raio da trajetória (seguir circulo)
    - outros fatores e ganhos ($k_n,k_\theta$)
- Funções. Cada uma é um modo de deslocação:
    - `set_theta`
        - Robot roda no sítio até ter a orientação que queremos
        - $w_{req}=k_{\theta}e_{\theta}$
    - `goto_xy`
        - Robot vai em linah reta para um ponto xy ( `Pf`)
        - Esta função como está por default só mete o robot a andar em linha reta. Seria preciso:
            - Usar `set_theta` para orientar e meter virado para `Pf`
            - Meter `v_req=v_nom` até chegar ao ponto
    - `follow_line`, `follow_circle` - incompleto
    - `follow_track` - para seguir uma linha no chão com IRLine

# MAIN.CPP
- Começamos por definir uma série de coisas base:
    - incluir bibliotecas (Arduino, Wifi, WifiUdp, LittleFS, etc)
    - definir uma data de coisas necessárias para ligação UDP
    - definir a pico4drive e o seu encoder, assim como os pinos de cada um
    - definir pinos dos motores e do solenoid
    - Tem linhas opcionais para um sensor TOF, um INA266 e um MPU
    - definir pinos e ligação do LIDAR LDS
    - incluir ficheiros de robot e trajectories
    - temos 2 funções para ler e processar os dados dos sensores IRLine
    - incluir os 2 ficheiros de gchannels. Temos as instancias `udp_commands` e `serial_commands` que têm portanto todas as funções e parametros gchannels
    - Temos ainda a instancia `pars_list` da classe `commands_list`

- Definimos a função `process_command` que recebe um comando `frame`
    - Começamos por usar a função `process_read_command` de `pars_list` para ver se este comando existe na lista e retorna um `frame` novo, com as partes `text`,`value` no formato que queremos para comandos ou tokens
    - A função então vai *um a um* ver se frame é cada comando e atribui o valor
        - Se temos `frame -> 'u2' 1` fazemos `u1_req = 1`
    - Os comandos considerados:
        - u1, u2, w1, w2
        - st - força a entrar  num estado com a classe `pfsm` de `state_machines.cpp`
        - dt - alterar o intervalo de tempo das iterações
        - v, w
        - sl - PWM do solenoide
        - xr, yr, tr - mudar $x_{e},y_{e},\theta_{e}$ 
            - Estes comandos serão **uteis** para configurar onde o robot acha que está
        - pl - load parametros
        - ps - guardar parametros
        - ssid - mudar o nome da rede wifi a ligar
        - pass - mudar a password para o canal wifi
            - notemos que estas 2 obviamente não podem ser mandadas por UDP 
        - wifi - se value=1 reiniciamos o wifi, se value=0 desligar wifi
        - httpota - parar robot e fazer cenas http idk
        - cat - enviar ficheiro com comandos
        - udp - enviar um packet udp com o value
        - s2 (lidar) - controlar o lidar, abaixo vem mais detalhes. Este comando tem formato `s2 TEXT`. Comandos mais importantes:
            - text = b - ligar motor / rodar lidar
            - text = e - desligar motor

- Mais funções:
    - `read_PIO_encoders`
    - `serial_write` - faz `Serial.write` de um `buffer` e envia-o por UDP
    - `wifi_list` - para listar todas as redes wifi encontradas

- Tem pedaços condicionais:
    - para se tivermos Arduino OTA (para enviar codigo para o rasp wireless inves de por cabo)
    - para se tivermos um INA266

- Temos o `setup`
    - Definir o LED builtin, pinos de encoders, pinos dos motores das rodas, pinos do solenoide
    - Inicializar encoders e pico4drive
    - **Registar comandos CONSTANTES 1 a 1** no `pars_list`
        - Para alterar algo em `pars_list` é aqui
        - Cada comando está associado a uma variável em `PID`, `robot` ou `traj`
        - Estes parametros constantes são coisas tipo: posições inicial, centro ou final do `traj`; K's do `PID`, etc
    - Inicializamos o PID e os seus parametros (que são diferentes do que temos em  `pars_list`)
    - Temos a lista de SSIDs e passwords
    - Temos um loop infinito até que o robot se ligue a uma rede wifi
        - Quando conseguir, é enviado por Serial (apenas, por UDP não) o canal e rede a que ligamos
    - Definimos os pinos e cenas do LIDAR, que tem ligação UART no `Serial2`

- Finalmente, temos o `loop`
    - Enviamos *apenas por Serial* o IP e port UDP a que estamos ligados 
    - Um if lê e processa comandos no UDP, processando um carater de cada vez com `process_char`
    - Um if lê o serial
    - Um if lê o serial2 - lemos o **lidar**
        - À data de escrever isto, o programa guarda cada pedaço `b` lido no serial 2 num `buffer`
        - Quando cheio, este buffer é enviado por UDP para o PC, onde os bytes são processados e convertidos em valores de distancia. 
        - Mudarei isto ASAP
    - Atualizamos o pico4drive e fazemos load dos parametros se pedido
    - Agora a parte apenas feita nos intervalos `interval`
        - Lemos os encoder e sensores IRLine
        - Atualizar a odometria
        - Fazemos `control(robot)` o que atualiza a FSM e calcula tudo do robot
        - Isto permite atualizar as velocidade linear e angular do robot
        - Com isso, calculamos as tensões dos motores com `calcMotorsVoltage` (de `robot.cpp`) e usamos `voltage_to_PWM` (de `pico4drive.cpp`) para definir os PWMs e controlar os motores e meter mesmo as velocidades que queremos
        - Aplicar estes PWMs nos motores com  `set_driver_PWM`
        - Temos um modo de debug ativado com  `debug_level`
            - Todos os comandos são impressos 1 a 1
            - Isto pode ser facilmente observado no comrobot
            - 