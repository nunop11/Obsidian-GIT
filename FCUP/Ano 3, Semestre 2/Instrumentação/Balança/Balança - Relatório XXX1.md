## Excitação da Ponte
### Ponte de Wheatstone com strain gauge
![[ponte wheatstone com strain gauge.png]]
Temos a montagem acima. Estando na balança um objeto de massa $w$ (em gramas) temos: $R_{0}r=0.2 w ~(\text{m}\Omega)$. Podemos então definir uma resistência $R_{x}=R_{0}r=0.2w$ tal que: $R_{0}(1\pm r)=R_{0}\pm R_{x}$.
Como o objetivo deste projeto é fazer uma balança de precisão que meça massas na gama $[0,200]\text{g}$, precisamos de planear o circuito contando que teremos $R_{x}\in [0,40]\text{m}\Omega$

### Circuito
![[bal_ponte_circ2.png|500]]
Consideremos $i$ a corrente que passa em $R_{1}$, $I$ a corrente que passa em $R_{2},R_{3},R_{4}$ e $I_{z}$ a corrente que passa no Zener. Temos: $i=I+I_{z}$
Observando o circuito vemos que:
$$\begin{cases}
12-R_{1}i=6.8 \\
6.8-I(R_{2}+R_{3})=0 \\
V_{+}=6.8-R_{2}I \\
V_{-}=6.8-(R_{2}+R_{3}+R_{4})I
\end{cases}$$
Podemos obter:
$$\Delta V=V_{+}-V_{-}=6.8\frac{R_{3}+R_{4}}{R_{2}+R_{3}}$$
Como os terminais $+,-$ do Amplificador de baixo estão ambos com tensão nula, podemos escrever $V_{+}=R_{3}I~,~V_{-}=-R_{4}I$. Assim vemos que:
$$V_{+}=\frac{6.8R_{3}}{R_{2}+R_{3}} \quad \quad;\quad \quad V_{-}=\frac{-6.8R_{4}}{R_{2}+R_{3}}$$

Teremos uma corrente $I'=\Delta V/R_{0}$ na ponte. Pelo ramo de cima irá uma corrente $I_{U}$ e pelo ramo de baixo uma corrente $I_{D}$. Devido à simetria do sistema teremos $I_{U}=I_{D}=\frac{1}{2}I'=\frac{\Delta V}{2R_{0}}$ . Partindo disso, conseguimos obter: $$OUT_{+}(R_{x})= 3.4\frac{R_{3}+R_{4}}{R_{2}+R_{3}} \frac{R_{x}}{R_{0}} + 3.4\frac{R_{3}-R_{4}}{R_{2}+R_{3}}$$
logo
$$OUT_{-}(R_{x})=-3.4\frac{R_{3}+R_{4}}{R_{2}+R_{3}} \frac{R_{x}}{R_{0}} + 3.4\frac{R_{3}-R_{4}}{R_{2}+R_{3}}$$
Vemos logo que se colocarmos $R_{3}=R_{4}$, a ordenada na origem desta equação (modo comum do sinal) desaparece. No entanto, verificamos na prática que por estas tensões serem muito reduzidas, continuamos a ter offsets causados pelas caraterísticas dos componentes usados. Assim, se $R_{3}=R_{4}$ temos:
$$OUT_{\pm}= \pm 6.8\frac{R_{3}}{R_{2}+R_{3}}\frac{R_{x}}{R_{0}}$$

Escolhemos esta configuração, porque vemos que a saída apre senta uma relação linear com a resistência $R_{x}$. Além disso, tivemos em conta que devido aos 2 buffers existentes, o ruído deverá ser menor e como temos mais resistências será mais fácil controlar e ajustar a relação $OUT_{\pm}(R_{x})$.
Assim, em suma, a tensão que será amplificada pelo INA126 será:
$$\Delta OUT=OUT_{+}-OUT_{-}=6.8\frac{R_{3}+R_{4}}{R_{2}+R_{3}}\frac{R_{x}}{R_{0}}$$

## Amplificação (NÃO INV)
![[bal_amp.png|525]]
Neste circuito decidimos incluir o circuito RC na saída do INA126 de forma a fazer uma filtragem dos ruídos de frequência maior, mais no início do circuito. Colocamos $R_{op}=47\text{k}\Omega~,~C_{op}=330\text{nF}$, o que resulta numa frequência de corte de $10.26\text{Hz}$. Isto não deverá afetar a tensão, pelo que $V_{+}^{LM}=V_{OUT}^{INA}=V_{1}$ 
Após consultar a datasheet do amplificador INA126 vemos que o seu ganho é: $G = 5+\frac{80\cdot10^{3}}{R_{G}}$ logo: $V_{1}=G(OUT_{+}-OUT_{-})$
Podemos então definir o sistema de equações deste circuito:
$$\begin{cases}
V_{1}=G(OUT_{+}-OUT_{-}) \\
V_{2}-P_{1}I=V_{1} \\
V_{1}-R_{amp}I=0
\end{cases}$$
de onde podemos obter:
$$V_{2}=V_{1}\left(1+\frac{P_{1}}{R_{amp}}\right)$$
logo temos:
$$V_{2}=6.8 \left(1 + \frac{P_{1}}{R_{amp}}\right)\left(5+\frac{80\cdot10^{3}}{R_{G}}\right)\frac{R_{3}+R_{4}}{R_{2}+R_{3}}\frac{R_{x}}{R_{0}}$$

## Offset
![[bal_offs.png|750]]
No processo de testar o funcionamento da secção de amplificação, verificamos que a tensão de saída do INA126, $V_{1}$, apresentava um elevado offset: quando $R_{x}=0$ tínhamos $V_{1}=-0.707 ~(\text{V})$ quando deveríamos ter 0. Desta forma, ao amplificar o sinal medíamos tensões demasiado elevadas.
Assim, foi montado o circuito acima, introduzindo-se uma tensão de referência $V_{ref}$ que poderá ser ajustada usando o potenciometro $P_{2}$, de modo a eliminar o offset de $V_{1}$. 

Decidimos utilizar um potenciometro $P_{2}$ de $1\text{k}\Omega$, de modo a conseguir controlar o offset com maior precisão.
Consideremos que queremos uma corrente $I$ próxima de $20\mu\text{A}$ a passar no potenciometro (porquê????). Neste caso, teremos nele uma queda de potencial de $0.02V$. Ou seja, se queremos que $V_{ref}=0.710\text{V}$ teremos que ter:
$$\begin{cases}
6.8 - R_{OS1}I = 0.72 \\
0.70 - R_{OS2}I = 0 \\
\end{cases}$$
Usando a menor quantidade de resistências do laboratório, o mais próximo disto que conseguimos obter foi: $R_{OS1}=270\text{k}\Omega~,~R_{OS2}=30.9\text{k}\Omega$ para o qual temos uma corrente prevista no LTspice de cerca de $22\mu\Omega$.
Com estas resistências, conforme movemos o potenciometro conseguimos ajustar a tensão $V_{ref}$ no intervalo $[0.697, 0.720]\text{V}$, que era aquilo que pretendíamos.

## Filtragem
Decidimos visualizar a saída da amplificação no osciloscópio:
![[balanca sem filt.png|425]]
facilmente notamos que o gráfico apresenta ruído. Decidimos portanto filtrar este sinal.

![[bal_filtro.png]]
Montamos o filtro MFB passa-baixo de 4ª ordem acima. Testamo-lo no website http://sim.okawa-denshi.jp/en/Fkeisan.htm antes de montar e verificamos que este circuito tem uma frequência de corte de $10.6\text{Hz}$ e um tempo de resposta de cerca de $0.25\text{s}$. No LTspice verificamos que tem um ganho de -1.68 abaixo da frequência de corte (ocorre inversão da polaridade do sinal).
Consideramos estas caraterísticas como apropriedadas.

Após filtragem, voltamos a visualizar o sinal no osciloscópio:
![[balanca filt.png]]
Agora a FFT apresenta mais "ruído" e já não temos picos acentuados no início, o que indica que já não teremos oscilações não desejadas. O ruído terá sido eliminado.

Além disso, aumentando significativamente a escala temporal do osciloscópio podemos ver o seguinte:
![[balança colocar massa.png]]
Vemos que o sinal é oscilatório, tendo-se medido a frequência de $50\text{Hz}$ (frequência da rede), como esperado. Além disso, vemos que o circuito demora cerca de meio segundo a reagir à colocação de uma massa na balança, o que consideramos apropriado.

Para melhor compreender o efeito da filtragem sobre o sinal fizemos FFT dos dois sinais, tendo-se:



## Calibração
- Montamos então o seguinte circuito:
![[bal_total.png]]
Conforme o que foi visto acima, temos que a tensão medida no final do circuito, $V_{3}$ será:
$$V_{3}=-1.68\cdot6.8 \left(1 + \frac{P_{1}}{R_{amp}}\right)\left(5+\frac{80\cdot10^{3}}{R_{G}}\right)\frac{R_{3}+R_{4}}{R_{2}+R_{3}}\frac{R_{x}}{R_{0}}$$
O objetivo deste projeto é que $2\text{V}=200\text{g}$. Como $200\text{g}$ implica $R_{x}=40\text{m}\Omega$ teremos um declive de $50$.
Selecionamos $R_{1}=1\text{k}\Omega, R_{2}=1\text{k}\Omega, R_{3}=R_{4}=22\text{k}\Omega$. Temos $R_{0}=1\text{k}\Omega$. Temos $R_{G}=82\Omega$ de modo que o ganho do INA126 esteja perto de 1000. Deste modo temos
$$V_{3}=14.5\left(1+\frac{P_{1}}{R_{amp}}\right)R_{x}$$
ora, para o declive ser 50 é necessária a relação:
$$P_{1}=2.45 R_{amp}$$
Desta forma, colocamos $R_{amp}=2.2\text{k}\Omega$, de modo que podemos ajustar o potenciometro $P_{1}$ (de $10\text{k}\Omega$) para a ter o ganho pretendido.

# INVERSOR
Se acabarmos por decidir fazer inversor, muda o seguinte:

## Amplificação (INV)
![[bal_amp_inv.png|525]]
Neste circuito decidimos incluir o condensador opcional, tendo-se $C_{op}=330\text{nF}$ (PORQUÊ???). Temos que $V_{+}^{LM}=V_{OUT}^{INA}=V_{1}$ 
Após consultar a datasheet do amplificador INA126 vemos que o seu ganho é: $G = 5+\frac{80\cdot10^{3}}{R_{G}}$ logo: $V_{1}=G(OUT_{+}-OUT_{-})$
Podemos então definir o sistema de equações deste circuito:
$$\begin{cases}
V_{1}=G(OUT_{+}-OUT_{-}) \\
V_{1}-R_{amp}I=0 \\
V_{2}+P_{1}I=0 \\
\end{cases}$$
de onde podemos obter:
$$V_{2}=-\frac{P_{1}}{R_{amp}}V_{1}$$
logo temos:
$$V_{2}=-6.8 \frac{P_{1}}{R_{amp}}\left(5+\frac{80\cdot10^{3}}{R_{G}}\right)\frac{R_{3}+R_{4}}{R_{2}+R_{3}}\frac{R_{x}}{R_{0}}$$

%% ## Offset (INV)
![[bal_offs.png|500]]
- No processo de testar o funcionamento da secção de amplificação, verificamos que a tensão de saída do INA126, $V_{1}$ apresentava um elevado offset: quando $R_{x}=0$, com a configuração inversor teremos $V_{1}=0.694 ~(\text{V})$ (CONFIRMAR COM MORAIS), quando deveríamos ter 0. Desta forma, ao amplificar o sinal medíamos tensões demasiado elevadas.
- Assim, foi montado o circuito acima, introduzindo-se uma tensão de referência $V_{ref}$ que poderá ser ajustada usando o potenciometro $P_{2}$, de modo a eliminar o offset de $V_{1}$. 

- Decidimos utilizar um potenciometro $P_{2}$ de $1\text{k}\Omega$, de modo a conseguir controlar o offset com maior precisão.
- Consideremos que queremos uma corrente $I$ próxima de $20\mu\text{A}$ a passar no potenciometro (PORQUÊ????). Neste caso, teremos uma queda de potencial nele de $0.02V$. Ou seja, se queremos que $V_{ref}=-0.7\text{V}$ teremos que ter:
$$\begin{cases}
6.8 - R_{OS1}I = -0.72 \\
-0.68 - R_{OS2}I = -12 \\
\end{cases}$$
- Usando a menor quantidade de resistências do laboratório, o mais próximo disto que conseguimos obter foi: $R_{OS1}=390\text{k}\Omega~,~R_{OS2}=587\text{k}\Omega (560+27)\text{k}\Omega$ para o qual temos uma corrente prevista no LTspice de $19.2\mu\Omega$.
- Com estas resistências, conforme movemos o potenciometro conseguimos ajustar a tensão $V_{ref}$ no intervalo $[-0.705, -0.686]\text{V}$, que era aquilo que pretendíamos. %%

## Calibração (INV)
![[bal_total.png]]
Conforme o que foi visto acima, temos que a tensão medida no final do circuito, $V_{3}$ será:
$$V_{3}=1.68\cdot6.8 \frac{P_{1}}{R_{amp}}\left(5+\frac{80\cdot10^{3}}{R_{G}}\right)\frac{R_{3}+R_{4}}{R_{2}+R_{3}}\frac{R_{x}}{R_{0}}$$
O objetivo deste projeto é que $2\text{V}=200\text{g}$. Como $200\text{g}$ implica $R_{x}=40\text{m}\Omega$ teremos um declive de $50$.
Selecionamos $R_{1}=1\text{k}\Omega, R_{2}=1\text{k}\Omega, R_{3}=R_{4}=22\text{k}\Omega$. Temos $R_{0}=1\text{k}\Omega$. $R_{G}=82\Omega$ de modo que o ganho do INA126 esteja perto de 1000. Deste modo temos
$$V_{3}=14.5\frac{P_{1}}{R_{amp}}R_{x}$$
ora, para o declive ser 50 é necessária a relação:
$$P_{1}=3.45 R_{amp}$$
Desta forma, colocamos $R_{amp}=2.2\text{k}\Omega$, de modo que podemos ajustar o potenciometro $P_{1}$ (de $10\text{k}\Omega$) para a ter o ganho pretendido.

## Rx real (INV)
Na prática, ao fazer a calibração com o potenciometro $P_{1}$ garantimos que $200\text{g}\Leftrightarrow 2\text{V}$, logo estamos a ajustar a tensão de saída conforme a massa, não conforme $R_{x}$ (que não conseguimos medir).
Ora, acima consideramos a relação teórica: $R_{x}=0.2w$ ($R_{x}$ em $\Omega$, $w$ em kg). Com esta vimos que ocorre calibração quando $P_{1}=3.45R_{amp}$. No entanto, decidimos medir $P_{1},R_{amp}$ depois da calibração. Verificamos que, na realidade temos a relação: $$P_{1}=3.351 R_{amp}$$
Isto indica que a relação $R_{x}(w)$ usada estará errada! Consideremos então $R_{x}=Cw$. Substituindo tudo na equação de $V_{3}$:
$$V_{3}=14.5\cdot 3.351 \cdot Cw$$
Vimos que $V_{3}=2\text{V}$ quando $w=0.2\text{kg}$. Ou seja, o declive é 10:
$$1.45\cdot 3.351 \cdot C=10~~\to~~ C = \frac{10}{14.5 \cdot 3.351}=0.206$$
E temos:
$$R_{x} = 0.206w$$
