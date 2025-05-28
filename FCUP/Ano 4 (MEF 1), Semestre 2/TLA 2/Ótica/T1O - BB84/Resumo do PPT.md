## Criptografia
- Tradicionalmente, usamos criptografia one-way para decifrar texto enviado entre 2 utilizadores.
![[Pasted image 20250521092259.png]]
- Usamos funções fáceis de computar e difíceis de reverter sem a chave certa.
- Em 1994, foi demonstrado um algoritmo que facilmente consegue resolver encripatções tradicionais. Mas este precisa de ser corrido num *computador quântico*. Isto significa que, se um sistema destes se tornar prático, a criptografia tradicional ficará em risco
- Assim, para continuar a ter segurança, é preciso usar sistemas de criptografia quântica. 
- Em 1984 foi establecido o 1o protocolo de criptografia quântica: **BB84**.

- Um sitema deste tipo, com QKD (quantum key distribution) seria assim:
![[Pasted image 20250521092700.png]]
temos uma chave, que é transmitida para o recetor graças a um *canal quântico*.

## Polarização de 1 fotão
![[Pasted image 20250521092921.png]]
- Sabemos que, com um polarizador, podemos escolher a orientação da polarização de um fotão (ou de um feixe)
- Assim, podemos dividir a polarização em 2 base: uma normal e uma diagonal (em 45º)

### Quântica :D
- E sabemos que, se tivermos um fotão no estado $$\ket{\psi}=\alpha \ket{0}+\beta \ket{1}$$
então a probabilidaed de medir $\pm1$ num certo sensor será:
$$\begin{cases}
\text{p(+1)} = |\alpha|^{2}~~~~\to~~~~\text{estamos no estado }\ket{0} \\
\text{p(-1)} = |\beta|^{2}~~~~\to~~~~\text{estamos no estado }\ket{1}
\end{cases}$$
- Sabemos ainda que, se as medições forem feitas na base $\{\ket{b_{0}},\ket{\beta_{1}} \}$ então temos:
$$\begin{cases}
\text{p(+1)} = |\langle b_{0}|\psi\rangle|^{2}~~~~\to~~~~\text{passamos para o estado }\ket{b_{0}} \\
\text{p(-1)} = |\langle b_{1}|\psi\rangle|^{2}~~~~\to~~~~\text{passamos para o estado }\ket{b_{1}}
\end{cases}$$
- No entanto, notamos que perdemos as probabilidades.

### Polarização em kets
- Podemos então definir as 2 bases de polarização que vimos acima em kets:
$$\begin{align*}
\ket{0º}&= \frac{1}{\sqrt{2}}\ket{45º} + \frac{1}{\sqrt{2}}\ket{-45º}\\
\ket{90º}&= \frac{1}{\sqrt{2}}\ket{45º} - \frac{1}{\sqrt{2}}\ket{-45º}\\
\\
\ket{45º} &= \frac{1}{\sqrt{2}}\ket{0º} + \frac{1}{\sqrt{2}}\ket{90º}\\
\ket{-45º} &= \frac{1}{\sqrt{2}}\ket{0º} - \frac{1}{\sqrt{2}}\ket{90º}
\end{align*}$$
(isto pode ser facilmente compreendido ao somar vetores unitarios com as direções dos 4 eixos)
- Vemos então que temos 2 bases emparelhadas.

### Medições + ou x
- Passamos a chamar as bases por $+,\times$.
- Podemos então definir os operadores das medições nestas bases (que não passam de projetar estados nos 2 vetores):
$$\begin{align*}
\hat{M}_{+}&= |0º\rangle\langle0º| - |90º\rangle\langle90º|\\
\hat{M}_{\times}&= |45º\rangle\langle45º| - |-45º\rangle\langle-45º|
\end{align*}$$
e temos as medições de kets nas suas bases
$$\begin{align*}
\hat M_{+}\ket{0º}&= \ket{0º} \quad \quad &&; \quad \quad &&~~~\hat{M}_{+}\ket{90º}= -\ket{90º}\\
\hat{M}_{\times}\ket{45º}&= \ket{45º} \quad \quad &&; \quad \quad &&\hat{M}_{\times}\ket{-45º}=-\ket{-45º}
\end{align*}$$
e ao misturar bases:
$$\hat{M}_{+}\ket{45º}= \frac{1}{\sqrt{2}}\ket{0º} - \frac{1}{\sqrt{2}}\ket{90º}$$
- E isto mostra que, ao fazer 1 medição ficamos *apenas* com $\ket{0º}$ ou $\ket{90º}$

### Obter probabilidades
- Simplesmente fazemos MUITAS medições. E definimos:
$$\begin{align*}
\text{p}(+1)&= \frac{N_{+1}}{N_{+1}+N_{-1}}\approx |\alpha|^{2}\\
\text{p}(-1)&= \frac{N_{-1}}{N_{+1}+N_{-1}}\approx|\beta|^{2}
\end{align*}$$
(em que $N_{\pm1}$ é o número de valores $\pm1$ medidos)

### Codificação
- Tendo em conta os sinais ao medir kets na própria base, definimos:
![[Pasted image 20250521094947.png]]

## Regras da comunicação BB84
### 1. Emitir chave
- A Alice escolhe a base de forma aleatória e 1 bit
- O Bob escolhe uma base
- Ambos colocam os polarizadores de forma correta para a sua base. O laser é ligado
- O Bob regista se mediu 0 ou 1
- Isto tudo é repetido muitas vezes

### 2. Apagar bases incorretas
- A Alice e o Bob percorrem todas as medições feitas e dizem um ao outro que base escolheram em cada.
    - Por exemplo, Bob passa a saber que na medição #10 ele mediu '0' na base '+', mas Alice estava na base 'x'
- Guardam apenas as medições que têm a *mesma base*. As restantes são apagadas
- A Alice e o Bob apenas comunicam entre si a base, não o valor enviado. Isto pode ser feito publicamente.
- Depois de remover os valores errados, ambos os lados ficam com a *chave de encriptação completa*.
![[Pasted image 20250521095927.png]]

- Esta chave não é predefinida pela Alice. Como todas as bases são aleatórias, a chave é definida consoante enviamos dados e será diferente de cada vez que a fizermos.

### 3. Testar se há um espião
- A Alice e o Bob comparam publicamente uma amostra de bits da chave.
- Se houver erros, então há um espião e a chave é apagada.
- Se não houver, os bits de teste são apagados (porque agora são publicos) e os restantes são a chave.
- Isto funciona assim:
    - Consideremos que alguem (Eve) está a meio da transmissao a escutar. Ela terá de medir a polarização do feixe
    - Pelo principio de Heisenberg, essas medições irão introduzir erros

### 4. Encriptar a mensagem
- Usamos a chave com que ficamos no final do passo 3.
- A alice encripta a mensagem usando essa base
- Isto pode ser feito de várias formas. Por exemplo, a Cifra de Vernam consiste em fazer XOR entre a mensagem e a chave.

### 5. Transmitir a mensagem
- A Alice emite a mensagem encriptada, publicamente.

### 6. Decriptar a mensagem
- Usando a chave, o Bob decripta a mensagem.

## Montagem Thorlabs

### Sem espião
![[Pasted image 20250521100933.png]]
- Vemos assim como o Bob mede os valores de cada polarização
- O sistema não é quântico (não medimos single photon), mas a polarização do laser permite simular perfeitamente

### Com espião
![[Pasted image 20250521101059.png]]
- Vemos que a Eve tem que medir, perceber a base e valor e enviar de volta para o Bob
- Ora, prever a base correta será muito difícil logo o valor poderá ter erros

### Half wave plate
- Temos um half wave plate na monatagem?
- Um polarizador elimita quase toda a luz do feixe, que não tenha a polarização do seu eixo
- Um Half wave plate introduz um atraso de fase de $\frac{\lambda}{2}$ em uma das componentes. Na prática, isto quer dizer que o componente **roda** a polarização *sem mudar a sua intensidade*.

- O half wave plate faz isto porque é birrefringente. Consideremos que o eixo rápido é o X. 
- Para um feixe a passar, a componente $E_{y}$ será atrasada em $\frac{\lambda}{2}$ face a $E_{x}$. Isso é feito ao introduzir na equação da onda $E_{y}$: $z\to z- \frac{\lambda}{2}$
- Ou seja:
$$\begin{align*}
\text{antes HWP}&= \begin{cases}
E_{x}(z,t)=E_{0}\cos\theta e^{i(kz-\omega t)} \\
E_{y}(z,t)=E_{0}\sin\theta e^{i(kz-\omega t)} 
\end{cases}\\
\\
\text{depois HWP}&= \begin{cases}
E_{x}(z,t)=E_{0}\cos\theta e^{i(kz-\omega t)}\\
E_{y}(z,t)=E_{0}\sin\theta e^{i(kz-\frac{k\lambda}{2}-\omega t)}=E_{0}\sin\theta e^{-i\pi}e^{i(kz-\omega t)}=-E_{0}\sin\theta e^{i(kz-\omega t)}
\end{cases}
\end{align*}$$

### Alice
![[Pasted image 20250521102610.png]]
- A Alice começa por escolher 2 sequências aleatórias: de bases $+\times$ e de bits $01$.
- Seguimos então a figura acima. 
- Usaremos isto:
![[Pasted image 20250521102721.png]]
em que devemos sempre usar a planilha -  seguir o excel invés de criar a sequencia.

### Bob
- O feixe é divido num componente assim, que permite medir 0 ou 1 em ambas as bases:
![[Pasted image 20250521101319.png]]
- Ele apenas a HWP para trocar entre as bases $+\times$:
![[Pasted image 20250521102931.png]]
em que:
    - colocamos em $0º$ para selecionar a base $+$
    - colocamos em $45º$ para selecionar a base $\times$
- Novamente, seguir a sequência e registar na planilha/excel.

### Todas as possibilidades
![[Pasted image 20250521103057.png]]
- Ou seja, apenas se as bases forem iguais existe um valor garantido para cada detetor
- **Penso que** os valores nas colunas 'detetor 0' e 'detetor 1' são as *probabilidades* de cada um dos detetores detetar luz. 
    - Notemos que normalmente estes detetores são fotodiodos que apenas detetam SIM ou NAO luz. Não medem intensidade
    - Ou seja, o bob apenas sabe o que mediu, ele não sabe que probabilidade havia de medir isso.
    - E também não dá para ele estimar a probabilidade porque nessa medição ele e a Alice escolheram a base aleatoriamente. Não dá para repetir a medição de propósito

### Eve
- Como vimos, ela tem de receber E transmitir o sinal.
- Ou seja, ela tem que fazer o papel da Alice e do Bob em simultâneo.
- Isto quer dizer que ela tem que escolher 2 bases aleatórias, esperando escolher o mesmo que Alice e Bob
- Ela será detetada neste caso, por exemplo:
![[Pasted image 20250521103939.png]]
- Conforme comparamos mais e mais bits, a probabilidade de detetar a Eve aumenta:
![[Pasted image 20250521104047.png]]
com 20bits já temos 99.7%

#### Mais a fundo
- A Eve mede o que a Alice enviou e tenta replicar para o Bob, de modo a não ser detetada
- Como Alice escolhe bases aleatoriamente, temos 2 possibilidades:
    - **Eve escolhe a mesma base que Alice** - Neste caso Eve mede corretamente. Ela então consegue enviar para Bob a informação correta. Assim temos masi 2 possibilidades:
        - *Bob escolhe a mesma base que Alice* - O Bob mede o mesmo que media com a Alice. Eve não é detetada
        - *Bob escolhe a outra base* - O Bob mede uma leitura aletória, devido à diferença de bases. Mas esta será descartada de qualquer forma ao comparar bases. Eve não é detetada.
    - **Eve escolhe a outra base** - A Eve mede algo aleatório. Ela não sabe se tem a base certa. De qualquer forma, ela irá enviar o sinal na base que recebeu, assumindo que está correta.
        - *Bob escolhe base diferente da Alice* - A medição será eliminada ao comparar bases. Eve não detetada
        - *Bob escolhe a mesma base que Alice*
            - Temos um **erro**. 
            - No passo 2, Alice e Bob confirmam que esta medição foi feita na mesma base: a medição não será descartada. 
            - Mas, neste caso, temos 2 medições *aleatórias*. Eve mediu aleatóriamente o que recebe de Alice e Bob igualmente para o que recebe de Eve. Porque $B_{A}\neq B_{E}~,~B_{E}\neq B_{O}$
            - Em metade dos casos, o Bob vai medir o mesmo que a Alice enviou e Eve não é detetada. Mas na outra metade, a medição é diferente e Eve é detetada.
            - Este caso encontra-se na tabela abaixo
![[Pasted image 20250521105418.png]]

- Assim a probabilidade de detetar a Eve será: $$P_{detet} = 1 - \left(\frac{3}{4}\right)^{n}$$
e temos o gráfico de cima.



## Experiência
- Escrito logo no caderno

## Setup
- Caderno, antes da experiência

## Aplicações
- Alguns fabricantes, como toshiba, já fizeram modelos de QKD
- Estes protocolos também são usados em redes óticas (de fibra)
- 