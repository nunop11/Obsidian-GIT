Vejamos circuitos de medição de resistência
# 1 - Métodos Simples
## Divisor de tensão
![[circ resist 1.png]]
- Temos
$$V_{0}=\frac{R_{T}}{R_{0}+R_{T}}V_{S}=\frac{\kappa}{1+\kappa}V_{S}\quad \quad;\quad \kappa=\frac{R_{T}}{R_{0}}$$
- A tensão em função de variações fica:
$$V_{0}+\Delta V_{0}=\frac{R_{T}+\Delta R_{T}}{R_{0}+\Delta R_{0}+R_{T}+\Delta R_{T}}V_{S}$$
Sendo $\kappa$ a mesma cosia que atrás, $r_{0}=\frac{\Delta R_{0}}{R_{0}}~,~ r=\frac{\Delta R_{T}}{R_{T}}$ temos:
$$\begin{align*}
V_{0}+\Delta V_{0}&= \frac{R_{T}(1+r)}{R_{0}(1+r_{0})+R_{T}(1+r)}V_{S}\\
&= \frac{\kappa(1+r)}{1+r_{0}+\kappa(1+r)}V_{S}\\
\Delta V_{0}&= \frac{\kappa(1+r)}{1+r_{0}+\kappa(1+r)}V_{S} - \frac{\kappa}{1+\kappa}V_{S}\\
&(\cdots)\\
\Delta V_{0}&= \frac{\kappa}{(1+\kappa)^{2}}(r-r_{0})(1-\eta)V_{S} 
\end{align*}$$
em que temos o *termo de não linearidade* $$\eta=1-\frac{1+\kappa}{1+r_{0}+(1+r)\kappa}$$
que causa a relação não linear entre a tensão e a resistência.

- Consideremos um caso normal: $r_{0}=\Delta R_{0}=0~,~|\Delta R_{T}|\ll R_{T}~~\to~~ r\ll1$
    - Podemos definir a **sensibilidade**: $$S=\frac{\Delta V_{0}}{\frac{\Delta R_{T}}{R_{T}}}=\frac{\Delta V_{0}}{r}\sim \frac{\kappa}{(1+\kappa)^{2}}V_{S}$$
    - E temos a potência dissipada e $R_{T}$: $$P_{T}=\frac{V_{T}^{2}}{R_{T}}=\frac{R_{T}}{(R_{0}+R_{T})^{2}}V_{S}^{2}$$
    - Logo $$S=\frac{1}{1+\kappa}\sqrt{P_{T}R_{T}}$$

- E temos que a evolução do termo de não linearidade ocorre da seguinte forma:
![[circ resist 1 eta vs kapa.png]]
e $S/V_{S}$ evolui com $\kappa$ na forma:
![[circ resist 1 S.png]]

- Vemos que o circuito é de simples implementação e que temos sensibilidade máxima para $\kappa=1$, ou seja teremos muita sensibilidade quando $R_{0}\sim R_{T}$
- Teremos comportamento kinda linear para $r$ baixo.

## Potenciómetro
![[potenciometro.png]]
- No caso em que $\Delta R=0$ (repouso) teremos $V_{0}=\frac{1}{2}V_{S}$
- No caso de variação de resistência:
$$V_{0}+\Delta V_{0}=\frac{R_{T}+\Delta R_{T}}{2R_{T}}V_{S}=(1+r) \frac{1}{2}V_{S}$$
logo
$$\Delta V_{0}=\frac{1}{2} rV_{S}$$
- Logo a sensibilidade é
$$S=\frac{\Delta V_{0}}{\frac{\Delta R_{T}}{R_{T}}}=\frac{\Delta V_{0}}{r}=\frac{1}{2}V_{S}$$
- Vemos que o comportamento é linear 

## Fonte de Corrente
![[circ resist corrente.png]]
- Simplesmente teremos $V_{0}=R_{T}I_{S}$
- Tendo em conta variações:
$$V_{0}+\Delta V_{0}=(R_{T}+\Delta R_{T})I_{S}~~\to~~ \Delta V_{0}=I_{S}\Delta R_{T}$$
- Pelo que a potência dissipada no transdutor é: $P_{T}=R_{T}I_{S}^{2}$
- E a sensibilidade: $S=R_{T}I_{S}=\sqrt{P_{T}R_{T}}$
- No entanto, devemos notar que implementações com fonte de corrente são mais difíceis / caras.

--- O problema destes 3 métodos vistos é que quando $\Delta R_{T}=0$ temos $V_{0}\neq0$. Assim, se depois amplificarmos o sinal também iremos amplificar o modo comum. Por outras palavras, corremos o risco de **saturar o amplificador**!

# 2 - Ponte de Wheatstone
# 2.1 - De tensão
![[ponte wheatstone.png]]
- Consideremos $I_{G}=0$. Daí surge:
$$V_{A}=\frac{R_{3}}{R_{1}+R_{3}}V_{S}\quad \quad;\quad \quad V_{B}=\frac{R_{4}}{R_{2}+R_{4}}V_{S}$$
logo
$$\begin{align*}
V_{AB}=V_{A}-V_{B}&= \left(\frac{R_{3}}{R_{1}+R_{3}}-\frac{R_{4}}{R_{2}+R_{4}}\right)V_{S}\\\\
&= \frac{R_{2}R_{3}-R_{1}R_{4}}{(R_{1}+R_{3})(R_{2}+R_{4})}V_{S}
\end{align*}$$
- Temos equilíbrio quando $V_{AB}=0$ AKA quando $R_{1}R_{4}=R_{2}R_{3}$

### Thevenin
![[ponte wheatstone thevenin.png|238]]
- Para definir o circuito equivalente de Thevenin temos:
    - $V_{th}=V_{AB}=\frac{R_{2}R_{3}-R_{1}R_{4}}{(R_{1}+R_{3})(R_{2}+R_{4})}V_{S}$ 
    - $R_{th}=R_{1}\parallel R_{3}+R_{2}\parallel R_{4}$ 
- Nesse caso teremos a corrente:
$$I_{G}=\frac{V_{th}}{R_{th}+R_{G}}=0~~\to~~ V_{th}=0$$

## Métodos de Medição de Resistências com Ponte
### Modo Nulo
![[ponte wheatstone amp ai potenciometro.png]]
- Variamos $R_{v}$ com valores conhecidos (por exemplo com uma caixa de resistências). Variar até atingir equilíbrio. Quando acontecer, é fácil calcular $R_{x}$

### Modo de Deflexão
![[ponte wheatstone amp ai 2.png]]
- Não impomos equilíbrio. Invés de variar resistências ou atingir o equilíbrio, simplesmente medimos a tensão
$$V_{0}=\left(\frac{R_{0}}{R_{x}+R_{0}} - \frac{1}{2}\right)K V_{s}$$
($K$ é o ganho do amplificador de Erro?)

## Tipos de Pontes de Tensão
### Quatro resistências variáveis
- Consideremos a ponte em equilíbrio: $R_{1}R_{4}=R_{2}R_{3}$. Neste caso teremos $V_{0}=0$ (sem modo comum).
- Assim, podemos medir ligeiras variações das resistências:
![[ponte wheatstone eq geral.png]]
que resulta:
$$\Delta V_{0}=\frac{\alpha}{(\alpha+1)^{2}}(r_{2}-r_{1}+r_{3}-r_{4})(1-\eta)KV_{S}$$
em que $r_{i}=\Delta R_{i}/R_{i}$ e $\alpha=R_{1}/R_{2}=R_3/R_4$. Novamente, $\eta$ é o termo de não linearidade.

- E temos
![[ponte wheatstone 4 braços ativos r.png]]

### 1 Braço Ativo
![[ponte wheatstone amp ai 3.png]]
- Consideramos a ponte em modo de deflexão: $\alpha=1$, ou seja: $R_{1}=R_{2}=R_{3}=R_{0}$. Consideramos que o transdutor é $R_{4}=R_{T}=R_{0}$
- Consideremos por fim: $r=\frac{\Delta R_{T}}{R_{T}}\ll1$
- A tensão de saída será:
$$V_{0}+\Delta V_{0}=\Delta V_{0}=\left(\frac{1}{2}- \frac{1+r}{2+r}\right)KV_{S}=- \frac{r}{4+2r}KV_{S}\simeq \frac{-1}{4} rKV_{S}$$
- Vemos que o comportamento não é linear (só se $|r|\ll1$)
- Temos a sensibilidade:
$$S=\frac{\Delta V_{0}}{r}=- \frac{\kappa}{(1+\kappa)^{2}}KV_{S}=\left(1+ \frac{1}{\kappa}\right)K \sqrt{P_{T}R_{T}} $$

### 2 Braços Ativos
![[ponte wheatstone tensao modos.png]]

### 4 Braços Ativos
![[ponte wheatstone 4 bracos ativos 2.png]]
- Familiar ne
- Permite ter uma elevada sensibilidade (assumindo $R_0$ de facto igual em todos os ramos e assumindo uma boa calibração de forma a garantir que todos os ramos variam $\pm r$)
- Pode ser mais caro de executar

# 2.2 - De Corrente
![[ponte wheatstone corrente.png]]
- Novamente consideremos que $I_{G}=0$
- Fazendo circuito equivalente de Norton entre $A,B$ (?) podemos obter:
$$V_{AB}=\frac{R_{3}(R_{2}+R_{4})-R_{4}(R_{1}+R_{3})}{R_{1}+R_{2}+R_{3}+R_{4}}I_{S}$$
![[ponte wheatstone corrente va e vb.png]]

### 1 Braço Ativo
![[ponte wheatstone corrente 1 braco.png]]

### 2 Braços Ativos
![[ponte wheatstone corrente 2 bracos.png]]
- Vemos que em geral estes circuitos comportam-se "melhor", mas em geral estas configurações são mais caras de executar.

# 3 - Ligações Longas
![[ligacoes longas.png]]
- Se tivermos ligações suficientemente longas, a resistência dos fios elétricos começa a ser relevante. 
- Assim, fazemos uma ponte de 6 fios como temos acima, com um *sensor de Kelvin*:
![[ligacoes kelvin.png]]
    - Passasse uma corrente conhecida $I$ pela resistência e medimos a queda de tensão. Assim, temos ligações *force* que injetam a corrente e *sense* que medem a queda de tensão.
    - Devido à configuração do sistema, o efeito das resistências desaparece somehow

