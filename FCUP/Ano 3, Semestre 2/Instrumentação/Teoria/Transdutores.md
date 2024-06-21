# 1 - Sensores Térmicos
## 1.1 - RTD (Resistance Temperature Detector)
![[Pasted image 20240610124646.png]]
- De platina, com precisão abaixo de $0,1\degree C$.
- A sua zona de operação é $[-180,600]\degree C$ e deve operar com correntes abaixo de $1\text{mA}$ (para não haver auto aquecimento).

- O sensor segue a *equação de Callendar-Van Dusen*:
$$R=\begin{cases}
R_{0}(1+aT+bT^{2}) & ; & 0C\le T\le 600C \\
R_{0}(1+aT+bT^{2}+C(T-100)T^{3}) & ; & -200C\le T\le 0C
\end{cases}$$
![[Pasted image 20240610124939.png|350]]

- Podemos aproximar a um comportamento linear com:
$$R=R_{0}(1+\alpha T)$$
tendo-se um erro na ordem de $3\%$ para $-100C\le T\le 200C$.

- Temos as seguinte configurações:
![[Pasted image 20240610125143.png]]
e os respetivos circuitos:
![[Pasted image 20240610125221.png]]

- Podemos ainda ter a configuração:
![[Pasted image 20240610125430.png]]
em que o componente na saída do opamp é um MOSFET, que tem a função de controlar a corrente em $R_{ref}$.

## 1.2 - Termistor 
- Existem 2 tipos:
    - **NTC** - negative temperature coefficient
        - temómetros de baixas temperaturas
        - termostatos
    - **PTC** - positive temperature coefficient
        - aquecimento
        - sobrecorrente (fusiveis)

- Seguem a equação de Steinhart-Hart:
$$\frac{1}{T}=a + b \ln R+c \ln^{3}R$$
($a,b,c$ são obtidos ao medir a resistência a temperaturas conhecidas)

- A equação de steinhart-hart pode ser invertida:
$$R = \exp\left[\sqrt[3]{y- \frac{x}{2}}-\sqrt[3]{y+ \frac{x}{2}}\right] \quad;\quad x=\frac{1}{C}\left(A- \frac{1}{T}\right)~~,~~y=\sqrt{\left(\frac{B}{3C}\right)^{3}+ \left(\frac{x}{2}\right)^{2}}$$

- Para **NTC** a eq inversa fica:
$$R_{T}= R_{0}e^{\beta\left(\frac{1}{T}- \frac{1}{T_{0}}\right)}~~~~;~~ \beta_{T_{1}/T_{2}}= \frac{\ln\frac{R_{2}}{R_{1}}}{\frac{1}{T_{1}}- \frac{1}{T_{2}}}$$
- Podemos linearizar a relação em estudo da forma:
![[Pasted image 20240610213929.png]]
tendo-se $$v_{0}=\frac{R_{L}}{R_{L}+R_{T}}V_{S}=\frac{V_{S}}{1+\kappa e^{\beta \left(\frac{1}{T} - \frac{1}{T_{0}}\right)}}$$

## 1.3 - Termopar
- Temos *Efeito Seebeck* quando 2 condutores A,B diferentes são acoplados e sujetios a um gradiente de temperatura, os eletrões de um metal movem-se para o outro, tendo-se uma DDP.
![[Pasted image 20240610215634.png]]
- Tipos:
    - **K** - muito usado, mais geral. Com boa precisão e ampla faixa de temperatura
    - **J** - Faixa de temperatura menor que K, usada em sistemas mais antigos
    - **T** - muito estável, bom para baixas temperaturas
    - **E** - Maior saída de todos, boa precisão
    - **N** - Mais estável em temperaturas altas
    - **S,R,B** - de platina, muito estáveis a temperaturas elevadas. Usados para fornos.

- Ou seja, para escolher um tipo de termopar temos que considerar: faixa temperatura, precisão, ambiente de medição, estabilidade, durabiilidade e custo.

**Aplicação**
![[Pasted image 20240610220038.png]]
- Em que: $$v_{0}=\left(1+\frac{1M\Omega}{10\text{k}\Omega}\right)v_{+}=101 v_{+}$$
e, mais importante e menos especifico deste circuito:
$$v_{+}=\alpha(T_{hot}-T_{ref})$$

## 1.4 - Comparação
![[Pasted image 20240610220800.png]]

# 2 - Sensores de Luz
## 2.1 - Fotodíodo
- Já vimos montes de vezes. Fotões colidem com o fotodiodo, reduz-se a banda proibida do semicondutor e passam eletrões AKA maior corrente.
- Como tal têm uma curva caraterística:
![[Pasted image 20240610220959.png]]

- Podemos ter o fotoD em 2 modos: *fotovoltaico* (usado em paineis solares) ou *fotocondutor* (usado em sensores)

**Fotocondutor**
- Tendo-se um fotodíodo num circuito temos:
$$I_{D} = I_{SAT}(e^{\frac{qV_{A}}{k_{B}T}}-1)$$
($q$ é a carga do eletrão e $V_{A}$ a tensão fornecida)
- Por outro lado temos:
$$I_{TOTAL}= I_{SAT}\left(e^\frac{qV_{A}}{k_{B}T}-1 \right)-I_{P}$$
em que $I_{P}$ é a corrente de polarização:
![[Pasted image 20240610221255.png]]
($P$ é a intensidade da luz incidente e $R_{\lambda}$ a responsividade à luz)

- Podemos então fazer um circuito em que apenas estudamos esta corrente $I_{P}$:
![[Pasted image 20240610221527.png]]
- Sendo $A$ o ganho do circuito teremos que a "resistencia" do fotodiodo será $$R_{L}=\frac{R_{f}}{A}$$
mas como $A\to\infty$ (opamp em malha aberta), então teremos $R_{L}=0$
- Isto implida que $I_{D}=0$ logo teremos que a corrente que passa ma saída do opamp é $I_{sc}=I_{P}$!

## 2.2 - Fototransístor
![[Pasted image 20240610221918.png]]
- A base do transistor absorve fotões. Isso faz com que este circuito funcione como um fotodíodo, mas com ganho.
- São colocados em circuitos assim:
![[Pasted image 20240610222036.png]]
e
![[Pasted image 20240610222110.png]]

- Por exemplo, temos o circuito abaixo e correspondente traçado $I_{PCE}$ VS $E_{e}$ (irradiancia / potência da luz incidente)
![[Pasted image 20240610222312.png]]
em que $V_{CE}=3\text{V}~,~I_{PCE}=f(E_{e})$
- E o circuito do fototransistor é definido por:
$$RI_{PCE}<V_{CE}$$