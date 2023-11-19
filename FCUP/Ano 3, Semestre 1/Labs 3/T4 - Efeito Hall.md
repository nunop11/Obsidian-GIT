# Notas sobre Protocolo
## 2 - Introdução
- Podemos dividir materiais em 3 classes: condutores, semicondutores e isoladores. Temos:
![[tipos material.png|450]]

### Efeito Hall
- Se um material, percorrido por uma corrente $\vec{I}$, for sujeito a um campo magnético $\vec{B}$ (que não seja paralelo a $\vec{I}$), gera-se uma força $\vec{F}_{B}$ sobre as cargas em movimento que altera a sua trajetória.
![[efeito hall.png]]

- Sendo $q$ o valor da carga elétrica das cargas em movimento e $\langle \vec{v}\rangle$ a sua velocidade média, temos $$\vec{F}_{B}=q \langle \vec{v}\rangle \times \vec{B}$$
- As cargas começam a alterar a sua trajetória devido a esta força.
- Isto causa desiquilibrio de carga, o que gera um campo elétrico na direção do desvio da trajetória: $\vec{E}_{t}$.
- Este campo causa uma nova força que vai aumentado e eventualmente anula $\vec{F}_{B}$ e atinge-se equilíbrio.

- Sendo $\theta$ o ângulo entre $\langle \vec{v}\rangle$ e $\vec{B}$, no equilíbrio temos:
$$q E_{t}=q \langle v\rangle B\sin\theta ~~~~\to~~~~ E_{t}=\langle v\rangle B\sin\theta$$
- O campo $E_{t}$ está ainda relacionado proporcionalmente com a diferença de potencial $V_{H}$ (ver figura acima) entre as duas paredes, com distância $d$. Temos:
$$V_{H}=d E_{t}=d\langle v\rangle B\sin\theta$$

- A densidade de corrente que atravessa o material é dada por $j=nq \langle v\rangle$ ($n$ é a densidade volumica de portadores de carga). Sendo que $I=jS$ em que $S$ é a área da secção transversal do material, temos: $\langle v\rangle=\frac{I}{nqS}$

- Substituindo acima temos: $$V_{H}=\frac{d}{S} \frac{1}{nq} IB \sin\theta=\frac{d}{S} R_{H} IB\sin\theta$$
em que $R_{H}=\frac{1}{nq}$ é o *coeficiente de Hall* do material.
$$V_{H}=\frac{d}{S} R_{H} IB\sin\theta$$

- Temos ainda a constante *mobilidade elétrica*: $\mu=\frac{\langle v\rangle}{E}$

### Efeito Hall em Metais
- Em metais temos muitos portadores de carga livres. Assim, $n$ será elevado e $V_{H}$ reduzido AKA ocorre pouco efeito hall.

### Efeito Hall em Semicondutores
- Em semicondutores (especialmente se $n$ for reduzido) o efeito Hall, e respetivamente $V_{H}$, são mais intensos.

#### Semicondutor intrínsecos
- Materiais em que a transição de 1 eletrão do nível de valência cria naturalmente uma lacuna no nível de valência de que saiu.

#### Semicondutor extrínsecos
- Semicondutores resultantes da dopagem de semicondutores intrínsecos para melhorar a sua condutividade elétrica.
**Tipo-n** - Dopados com elementos que doam eletrões à banda de condução
**Tipo-p** - Dopados com elementos que aceitam eletrões (criando lacunas)

- Assim, como temos eletrões E lacunas num semicondutor extrínseco, a fórmula do coeficiente de Hall fica do tipo
$$R_{H}=\frac{-n \mu_{e}^{2}+ p \mu_{p}^{2}}{e(n \mu_{e}+ p \mu_{p})}$$
em que $n,p$ são as densidades dos eletrões e lacunas; $\mu_{e},\mu_{p}$ as respetivas mobilidades.

- Assim, nesta atividade, ao estudar a relação entre $V_{H}$ e $I$ e $B$, deveremos conseguir obter $V_{H},R_{H}$. Com isto, deveremos conseguir determinar o tipo de portador de carga principal do material (tipo-n ou tipo-p)

## 3 - Preparação - Perguntas
**1.** Ao usar um sistema deste tipo, conseguimos ter um campo aproximadamente perpendicular à amostra e cuja intensidade pode ser manipulada ao alterar a corrente nas bobinas.
**2.** ESTUDAR $B(I)$ 
**3.** Obter $R_{H}$ para:
    - Silício
    - Germânio
    - Cobre
    - Zinco
Estimar ordem de grandeza de $V_{H}$ para cada, para cada Tesla de $B$.
**4.** Se $V_{H}$ for positiva é tipo-p, senão é tipo-n
**5.** Alguns (?) potenciometros funcionam com efeito Hall. Logo, potenciometro anula efeito ao medir tensão??? 
**6.** Falar com Sérgio

## 4 - Execução
### 4.1 - Montagem
![[efeito hall 2.png]]
![[suporte efeito hall.png]]
### 4.2 - Procedimento
#### 4.2.1 - Calibração de $B$
- Bobinas ligadas *em série*. Ligadas a uma fonte DC e a um multimetro (para ver  a corrente). 
- Começar por medir o campo magnético entre as peças polares do eletromagnet com a sonda. Garantir que as faces da sonda estão paralelas às faces das peças polares (a sonda mede o fluxo magnético, o fluxo varia com $\cos \theta$).
- Medir o campo para muitos valores de corrente, entre $0-1.5~A$. Obter regressão polinomial $B(I)$ e assim não temos que voltar a medir o campo, podemos usar a corrente para saber o campo.

#### 4.2.2 - Amostra com $B$ fixo e variar $I_P$
1. Escolher 1 placa e montar corretamente
2. Colocar amostra entre polos do eletromagnete
3. Ter ligações:
    1. voltimetro a $U_{H}$ (tensão Hall) no suporte (5 na figura acima)
    2. voltimetro a $U_{P}$ (tensão Amostra) no suporte (10 na figura)
    3. amperimetro ligado às bobinas p/ ver corrente
    4. alimentação ligada às traseiras do suporte (11 na figura)
4. Ter display da amostra em modo corrente. Ligar tudo. Ter corrente $15-20~mA$. Ver que $V_{H}=0$ se $B=0$. Se não, rodar botão 8 na figura até termos tensão nula.
5. Colocar "Todos os valores" em 0 (isto é o que?? Corrente? Botão 8 fica igual certo?)
6. Colocar corrente de $1A$ nas bobinas
7. Variar corrente na amostra, $I_P$, entre $[-20mA,20mA]$ com o botão 1 na figura. Registar $I_{P}, V_{H},V_{P}$
8. Gráfico $V_{H}(I_{P})$. Permite calcular densidade e tipo de portadores de carga

#### 4.2.3 - Amostra com $I_P$ fixo e variar $B$ 
1. Verificar "condição zero" ($V_{H}=I_{P}=0$ se $B=0$). Repetir ponto 4 da secção 4.2.2 ???????
2. Colocar $I_{P}$ entre $15,20~mA$ (botão 1)
3. Variar corrente nas bobinas ($I_B$) entre $0,1.8~A$. Registar $I_B,V_H,V_P$
4. Gráfico $V_{H}(B)$. Permite calcular densidade e tipo de portadores de carga

#### 4.2.4 - Variação $V_H,V_P$ com temp $T_P$
0. Discutir com prof método a usar antes de começar. Fazer testrun para entender a sensibilidade do aparelho disponivel
1. Meter display em modo temperatura (botão 7 na figura)
2. Aumentar temperatura por SÓ $2s$. Carregar no botão 12, nas traseiras, por 2 segundos (not sure)
3. Registar aumento da temperatura e quanto tempo é preciso esperar para ter uma temperatura estável da amostra
4. Ajustar novamente "condição zero" se preciso
5. Passar corrente $I_{P}$ entre $15,20~mA$ e corrente de $1A$ nas bobinas
6. Subir gradualmente a $T_P$ de temp ambiente até $120\degree C$. Registar $T_P,V_H,V_P$

