###### Aula 1 - 15/2/2024

> NOTAS: 
> - Muitas das vezes em que eu usar o símbolo $\sim$ estou a falar da ordem de grandeza de algo ($x\sim1$ quer dizer que $x$ será unitário: $1,2,3,4,\dots$)

# 1 - Modelo de Drude
### Descrição básica
- Este é um modelo **_clássico_** usado para careterizar materiais, especialmente condutores.
- Consideremos um certo elemento de número atómico $Z_{a}$. Ora, este terá $Z_{a}$ protões no seu núcleo e o mesmo número de eletrões a orbitá-lo.
![[atomos metal.png|400]]
- Ora, num metal, para que a estrutura sólida se mantenha, os átomos têm que se interligar. Para isto, cada átomo liverta $Z$ eletrões, que são partilhados com os restantes átomos do sólido. Efetivamente, isto significa que temos $Z$ eletrões *livres* por átomo! Por outro lado, isto significa que, num átomo deste elemento dentro de um sólido só temos $Z_{a}-Z$ eletrões em órbita. Temos então uma rede de **iões**, com eletrões livres pelo meio. De notar que consideramos todos os iões perfeitamente iguais.

- Consideremos as seguintes caraterísticas do sólido em estudo:
    - $n$ - densidade de eletrões livres (unidades $\text{1/volume}$)
    - $\rho_{m}$ - densidade volúmica (unidades $\text{massa/volume}$)
    - $A$ - massa molar (unidades $\text{massa}$)
- Por análise dimensional vemos que $n\propto \frac{\rho_{m}}{A}$. Mais concretamente temos:
$$n=N_{A}\frac{\rho_{m}}{A}Z$$
em que $N_{A}\sim10^{23},0<\rho_{m}/A<1,Z\sim1$. Desta forma: $$n\sim10^{22}\text{cm}^{-3}$$
- Ora, a partir de uma formulação muito simplista deste modelo conseguimos estimar $n\sim10^{22}$. Ora, esta grandeza pode ser calculada experimentalmente ao medir o efeito de Hall de amostras sólidas. 2 valores medidos são: $n_{\text{Cs}}=0,91\cdot10^{22}\text{cm}^{-3}~,~n_{\text{Be}}=24,7\cdot10^{22}\text{cm}^{-3}$. Ou seja, o modelo aparenta descrever a realidade de forma minimamente correta. Vamos prosseguir com o seu estudo.

## 1.1 - Raio atómico
![[metal drude.png|400]]
- Consideremos um sólido de volume $V$, em que temos $N$ eletrões livres.
- Iremos consideremos que cada eletrão é *esférico* e tem volume $V_{s}$. Assim, sendo o raio de 1 eletrão $r_{s}$ temos $V_{s}=\frac{4}{3}\pi r_{s}^{3}$ 
- Vamos considerar que os eletrões formam um **gás clássico**, pelo que se encontram distribuidos de forma uniforme pelo material. Desta forma, será natural concluir que $V_{s}=V/N$
- Ora, disto resulta que $$V_{s}=\frac{V}{N}=\frac{1}{n}=\frac{4}{3}\pi r_{s}^{3}~~\to~~ r_{s}=\left(\frac{3}{4\pi  n}\right)^{\frac{1}{3}}$$
- E neste momento torna-se útil introduzir o raio de Bohr: $a_{0}=\frac{\hbar^{2}}{me^{2}}=0,529\dot{A}$. $r_{s}$ deverá ser desta ordem de grandeza.
- Daqui podemos ainda escrever:
$$n=\frac{4\pi r_{s}^{3}}{3}$$

## 1.2 - Pressupostos do Modelo
**_1 - Gás Clássico_**
- Consideramos o gás que os eletrões livres formam é *livre* e *independente*:
    - *livre* - os eletrões não interagem com os iões exceto quando colidem com estes. 
        - Mais tarde iremos não desprezar as interações para poder estudar conservações. Para já iremos simplesmente dizer que o ião trata das conservações: Energia "a mais"? O ião absorve-a. Conservação de momento? Ele é transferido para o ião. Hotel? Trivago.
        - Temos ainda que estas colisões são uma parte fundamental do modelo. Entre outras coisas, estas explicam a resistência elétrica de materiais.
    - *independente* - os eletrões não interagem uns com os outros.

**_2 - Tempo de relaxação_**
- Consideramos que as colisões são *estatísticas e aleatórias*
- Ou seja, dizemos que existe um **tempo médio entre colisões** $\tau$. Deste modo, a probabilidade de ocorrer uma colisão, por unidade de tempo, é $1/\tau$. De outra forma, a probabilidade de ocorrer uma colisão num intervalo $dt$ é $dt/\tau$

- E aqui surge um problema do modelo de Drude: não existe um modelo de colisão. Ou seja, não temos nenhumas equações ou pressupostos sobre as colisões que nos permitam calcular $\tau$. 
- Mais concretamente, em Drude estamos a assumir que o eletrão perde qualquer memória quando colide com o ião. Por outras palavras, a velocidade pós colisão é aleatória e completamente independente da velocidade antes da colisão -- é como se o **sistema reiniciasse**.

## 1.3 - Drift e Ohm
![[eletroes a mover em metal - drude.png|475]]
- Consideremos um sólido de metal de área transversal $S$. Para o elemento que compõe o metal, temos $Z$ eletrões livres por átomo, distribuidos no sólido com um densidade $n$. Aplicamos uma DDP nos terminais do metal. Queremos então determinar a carga que passa numa unidade de área por unidade de tempo AKA densidade de corrente.
- Começamos por assumir que todos os eletrões têm mesma velocidade média ($v_{d}$ - velocidade de drift).
- Ora, se considerarmos uma secção de comprimento $dx$ paralela à velocidade. Temos que os últimos eletrões a "passar para o lado de fora" num intervalo $dt$ são aqueles que têm exatamente velocidade $v_{d}=dx/dt$. Esta secção terá então volume $\mathcal{V}=Sv_{d}dt$.
- Ora, neste volume infinitesimal temos: $$\begin{align*}
dQ&= (-e)n\mathcal{V}\\
&= -env_{d}~Sdt\\
\frac{dQ}{Sdt}&= -env_{d}=\mathcal{J}
\end{align*}$$
ou seja:
$$\vec{\mathcal{J}}=-en\vec{v_{d}}$$
mas aqui surge a questão: quanto vale/como determinamos $v_{d}$?

#### Eletrão 1
- Consideremos um qualquer eletrão livre, eletrão 1.
- Deixemos de considerar a velocidade média.
- Vamos agora assumir que a força exercida pela DDP sobre os eletrões é igual em todos os pontos: $\vec{F_{e}}=-e\vec{E}$
- Sendo $\vec{v}_{1}(t)$ a velocidade do eletrão 1 em função do tempo, pela 2ª Lei de Newton temos:
$$\frac{d\vec{v}_{1}}{dt}=\vec{a}=- \frac{e}{m}\vec{E}~~\to~~ d\vec{v}_{1}=- \frac{e}{m}\vec{E}~dt$$
podemos simplesmente integrar a equação e temos:
$$\vec{v}_{1}(t>0)=\vec{v}_{1}(0)- \frac{e}{m}\vec{E}t$$
em que a velocidade inicial $v_{1}(0)$ corresponde à velocidade logo após a última colisão (porque o sistema reinicia)

#### Eletrão 2
- Consideremos outro eletrão.
- Ora, não podemos fazer exatamente o que fizemos para o eletrão 1. Isto porque, como já vimos, *as colisões são estatísticas*. Isto é, não podemos simplesmente definir $\vec{v}_{1}(t)=\vec{v}_{2}(t)$, porque estaríamos a assumir que os 2 eletrões colidem ao mesmo tempo, algo que não é de todo garantido.
- Assim, dizemos que $$\vec{v}_{2}(t>0)=\vec{v}_{2}'(0)-\frac{e}{m}\vec{E}t$$
em que $\vec{v}_{2}'(0)$ é um termo independente do tempo, mas que corrige a diferença de tempo entre as colisões dos eletrões

#### ... (Repetir para $10^{22}$ eletrões)
#### Valor médio
- Iremos obter que a velocidade média é igual para todos os eletrões e independente do tempo, sendo esta a velocidade de drift:
$$\vec{v}_{d}=- \frac{e}{m}\vec{E}\tau$$

- Juntando isto à densidade de corrente que determinamos acima temos:
$$\vec{\mathcal{J}}= \frac{e^{2}n\tau}{m}\vec{E}~~\Longleftrightarrow~~ \vec{\mathcal{J}}=\sigma\vec{E}$$
em que $\sigma_{dc}=\frac{e^{2}n\tau}{m}$ é a **condutividade DC** do metal. Similarmente, $\rho_{dc}=1/\sigma_{dc}$ é **resistividade DC** do metal.
- De notar que a relação acima é apenas a 1ª expansão. Podemos expandir mais a expressão (como faremos na próxima aula) e veremos que temos até termos $\vec{E}^{2}$

- Voltando à condutividade DC. Ora, a resistividade do material é algo que facilmente podemos medir (para metais, podemos usar o método dos 4 contactos como fizemos em Laboratórios de Física 1).  
- Assim temos:
$$\tau=\frac{1}{\rho}\frac{m}{e^{2}}\frac{4\pi r_{s}^{3}}{3}\sim \frac{0,22}{\rho}\left(\frac{r_{s}}{a_{0}}\right)^{3}\cdot10^{-22}~\text{s}$$
podemos escrever a resistividade em $\mu\Omega\text{cm}$ (e indicamos $\rho_{\mu}$) e fica:
$$\tau\sim \frac{0,22}{\rho_{\mu}}\left(\frac{r_{s}}{a_{0}}\right)^{3}\cdot10^{-14} ~\text{s}$$
- Medindo $\rho_{\mu}$ e estimando $r_{s}/a_{0}\sim1$ temos que $\tau\sim10^{-14}~\text{s}$
- Podemos ainda determinar o livre percurso médio $\ell$ (a distância média percorrida entre colisões) usando:
$$\ell=v_{d}\tau\sim 1-10\dot{A}$$
o que é aproximadamente a distânca entre os iões da rede do metal (o dobro do raio dos átomos).

## 1.4 - Comportamento Estatístico
- Vimos que a probabilidade por unidade de tempo de *ocorrer* uma colisão é $1/\tau$. Ou seja, podemos escrever $dp=dt/\tau$. Podemos definir a probabilidade de *não* colidir é $dP=1-dt/\tau$.
    - À probabilidade de *colidir* num intervalo $t$ chamarei $p(t)$
    - À probabilidade de *não* colidir num intervalo $t$ chamarei $P(t)$
- Ora, neste modelo que cada instante de tempo é independente dos restantes. Ou seja, a probabilidade de o eletrão não colidir agora não influencia a probabilidade de não colidir daqui a um tempo $t$. Por outras palavras: temos **eventos independentes**.

*(Baseado no ex 1.2 da Ficha 1)*
- Podemos então recordar probabilidades e temos que a probabilidade de o eletrão não colidir colidir em 2 intervalos $dt$ consecutivos é o produto das probabilidades de colidir em cada um: $(1-dt/\tau)^{2}$.
- Desta forma, a probabilidade de o eletrão não colidir num certo intervalo $t$ dividido em $N\to\infty$ intervalos infinitesimais $dt$ será:
$$\begin{align*}
P(t)&= \lim\limits_{N\to\infty} \left(1- \frac{dt}{\tau} \right)^{N}\\
&= \lim\limits_{N\to\infty}\left(1- \frac{t}{N\tau}\right)^{N}\\
&= \lim\limits_{N\to\infty}\left(1- \frac{t}{N\tau}\right)^{N}\\
&= \lim\limits_{N\to\infty}\left(\left(1- \frac{t}{N\tau}\right)^{\frac{N\tau}{t}}\right)^{\frac{t}{\tau}}\\
&= \left[\lim\limits_{N\to\infty}\left(1- \frac{t}{N\tau}\right)^{\frac{N\tau}{t}}\right]^{\frac{t}{\tau}}\\
&= [e^{-1}]^\frac{t}{\tau}=e^{\frac{-t}{\tau}}
\end{align*}$$
- Podemos simplesmente definir $t=0$ como sendo o instante em que o eletrão colide. Assim, $t>0$ será o tempo passado desde a última colisão. Como seria de esperar, consoante passa tempo torna-se cada vez menos provável *não* colidir.

*(Baseado no ex 1.3 da Ficha 1)*
- Consideremos novamente que o eletrão colidiu em $t=0$. Usando esta lógica de eventos independentes, podemos dizer que a probablidade de só voltar a colidir apenas no intervalo $[t,t+dt]$ é dada pelo produto das probabilidades:
    - de *não* colidir em $[0,t]$ AKA probablidade de não colidir num intervalo $t$
    - de *colidir* em $[t,dt]$ AKA probabilidade de colidir num intervalo $dt$. Aqui nota-se algo importante: como temos eventos independentes, apenas importa o intervalo de tempo, não quando ele ocorre.

- Assim, temos que a probabilidade de só colidir em $[t,t+dt]$, a que chamarei $\mathcal{P}_{1}$, é dada por:
$$\begin{align*}
\mathcal{P}_{1}&= P_{t} \cdot p_{dt}\\
&= e^{\frac{-t}{\tau}} \cdot \frac{dt}{\tau}\\
&= \frac{dt}{\tau}e^{\frac{-t}{\tau}}
\end{align*}$$

*(Baseado no ex 1.4 da Ficha 1)*
- Consideremos que em $T=0$ temos $N_{0}$ eletrões que não colidiram. Usando a probabilidade de não colidir $P(t)$ obtida acima, podemos definir que num instante $t>0$ teremos $N(t)=N_{0}e^{\frac{-t}{\tau}}$ eletrões que não colidiram.