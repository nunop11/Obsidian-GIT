**Fiber Cavity Ring-Down Using an Optical Time-Domain Reflectometer**

### Intro
- Cavity ring-down (CRD) é um metodo de espetroscopia que permite fazer análise molecular e quimica em tempo real. A logica geral da configuração é: temos uma cavidade otica com espelhos de alta reflexao
- Recentemente (2014), tenta-se fazer uma configuração de CRD com fibras. Um loop de fibra seria a cavidade ressonante. 
- Esta técnica permite medir certos parametris fisicos: deformação, pressão, temperatura. Tenta-se ainda aplicar na area bioquimica
- Configurações normais de CRD com fibra usam um laser e um modulador. Neste artigo usam um OTDR. 
- O OTDR envia feixes para o CRD de fibra, que vem depois de um longo pedaço de fibra. Dentro do loop CRD, temos um taper de 50um, que tem 800m. Isto gera perdas no sinal CRD

### Teoria
#### CRD
- Num CRD tradicional temos
![[Pasted image 20250514230335.png]]
- Num CRD de fibra, um pulso otico é enviado para um loop de fibra. Neste loop temos 2 couplers nas 2 pontas: fonte e detetor. 
    - O loop faz o mesmo efeito que os espelhos.
- Consoante se propaga no loop, a luz sofre perdas por atenuacao. Ainda assim, o pulso irá fazer várias voltas. 
- Se medirmos o pulso num ponto, iremos ver vários "pulsos" a passsar em intervalos de $t=nL/c$ - $L$=largura da cavity, $n$=indice refracao

- Consideremos que temos um sensor de intensidade $T_{s}$ na fibra. 
- Em cada volta no loop, o feixe sobre perdas de atenuação, perdas de inserção dos couplers $T_{c}$ e a transmisão do sensor $T_{s}$. Ora, esta perda irá ser igual em cada loop.
- Assim, temos após 1 loop:
$$\frac{I_{1}}{I_{0}}= T_{s}T_{c}^{2}e^{-\alpha L}$$
depois de $k$ voltas AKA após intervalo de tempo $t_{k}$:
$$\frac{I_{k}}{I_{0}}=\left(\frac{I_{1}}{I_{0}}\right)^{k}=e^{\frac{t_{k}}{\Delta t}\ln I_{1}/I_{0}}=e^{-t_{k}/\tau}$$
e definimos a constante de tempo
$$\tau=\frac{nL}{c(\alpha L - \ln (T_{s}T_{c}^{2}))}$$

- Começamos por variar a largura do pulso no OTDR no range 0.5-20 us:
![[Pasted image 20250514231207.png]]
- Apenas 0.5 e 1 funcionam - nos outros temos saturação e sobreposição de picos
- Escolhendo isto, é uma questão de configurar/escolher o sensor de intensidade de forma a ter o $\tau$ desejado

### Exp
![[Pasted image 20250514231411.png]]
- Usou-se um OTDR comercial e mandou-se pulsos de 1us
- O pulso apssa uma fibra de 20km. Ao chegar ao coupler, passa para o loop de 800m. 
- A ponta solta com 3km serve para reduzir reflexoes de Fresnel que iria tornar o sinal instavel.
- No osciloscopio viu-se este decaimento (lido então à saída do coupler de baixo):
![[Pasted image 20250514231809.png]]
- Foi feito um ajuste exponencial e determinou-se um tempo de ring-down de 32us.

**Sensor**
- Colocou-se o sensor de intensidade na zona marcada. Este tem a utilidade de detetar perdas.
- O sensor consiste numa fibra tapered (vai ficando mais estreita) com 50um (na zona mais fina). Isto atua como um sensor de deslocamento
    - Chamamos a isto "sensor" porque podemos usar isto como um indicador. Ao dobrar o sensor, vemos que aumentam muito as perdas no CRD. Isso faz com que o decaimento lido no microscopio seja mais rapido. Em cada volta perdemos mais energia.
- O taper foi então deslocado diferentes distâncias e temos o resultado abaixo:
![[Pasted image 20250514232745.png|475]]

- Viu-se que o tempo de decaimento aumenta linearmente com o deslocamento.
- 