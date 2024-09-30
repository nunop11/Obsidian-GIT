## Sourcemeter
- Ligamos a saída vermelha ao sample a preta ao eletrólito.

## O Ciclo
![[ciclo de pulsos.png]]
- Temos:
    - *Pulso de Discarga* - Tem a função de descarregar a capacidade da camada de barreira e eliminar o campo E gerado no interface de onde acabaram de se depositar iões. A tensão deste pulso é igual à tensão final usada para criar os poros.
    - *Pulso de Deposição* - Serve para "forçar" os iões a depositar. Esta tensão deverá causar uma elevada densidade de corrente, que deverá aumentar o número de deposições.
    - *Pulso de Repouso* - Consiste num intervalo de tempo grande com $V=0$. Serve para os iões se ajustarem e estabilizarem após a deposição. Este pulso permite obter maior homogeneidade e reduz a evolução de hidrogénio.

## Labview
- Chama-se "PulseDepo" e servepara fazer PED. 
x\![[labview dep.png]]
- Parametros gerais
    - Sample ID : Nome do ficheiro a guardar
    - Optional Subfolder : o que o nome diz

- Pulso Descarga
    - Potential : o mesmo usado para criar as dendrites
    - Time : 2 ms
    - Current Limit Protection, Current Limit  : mesmo valor que em Current Limit da secção vermelha
- Pulso Deposição
    - Potential : Se corrente for abaixo de $100 \text{mA}$, podemos meter -40V. Senão metemos até -21 V
    - Time : 8 ms
    - Current Limit Protection, Current Limit : colocar os mesmo valor nos 2 campos, é a corrente aplicada durante deposição. 
        - Ou seja, usar este parametro para decidir qual será o potencial acima.
        - Decidimos previamente qual o limite de **densidade de corrente aplicada**, ou seja, temos que usar esta para calcular a corrente limite.
            - Iremos fazer poros até 6V (7.8 nm) com densidade 70 $\text{mA cm}^{-2}$ 
- Puslo Repouso
    - Rest time : 0.7s / 700 ms


