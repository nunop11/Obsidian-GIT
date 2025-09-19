# Determinar capacidade térmica de Magnetite
## Intro
- No documento tem uma intro muito gira sobre a história da magnetite e algumas propriedades e resultados físicos já medidos.
- Tem ainda cuidados de segurança a manusear este material

## Teoria
- A capacidade térmica tem unidades J/K, descrevendo o aumento de energia interna de um material aquando de um aumento de temperatura.
- Temos a 1ª lei da termodinâmica: $dU=dQ+dW=TdS-PdV$. Podemos escrever: $C=dQ/dT$. Para volume constante isto iguala: $C_{V}=dU/dT=T (dS/dT)$
- A capacidade térmica é uma grandeza extensiva - aumenta com o volume de material
    - Às vezes é mais útil expressar de forma intensiva. Para isso temos:
        - calor específico: $c=C/m$
        - capacidade térmica molar: $c=C/n$ (sim, ambas usam $c$)

- Em sistemas solid-state é comum medir $c_{p}$. Em que temos:
$$c_{p}-c_{V}=9 \alpha^{2}VT/\kappa$$
em que $\alpha$ é o coeficiente de expansão térmica, $\kappa$ é a comprissibilidade e $V$ é o volume específico (volume especifico == volume que um material precisa para ter 1 kg)

- O valor clássico de Dulong-Petit para a capacidade térmica de um sólido é $c=3R$ (R é a constante de gás ideal). Esta aplica-se a muitos metais a temperatura ambiente. Para não-metais e em temperaturas mais baixas o resultado piora.
- Para entender a dependência térmica de $c$ é útil a mecânica quântica. Na teoria de Einstein tratamos um sólido com um conjunto de osciladores harmónicos, todos com frequência $\omega$.
    - À temperatura $T_{E}=\hbar\omega/k_{B}$ a teoria clássica volta a aplicar-se.
- Mas mesmo o modelo de Einstein diverge um pouco dos dados experimentais:
![[modelo einstein.png]]

- Temos o *modelo de Debye*. Este explica a relação $c=\gamma T+\beta T^{3}$ a temperaturas baixas. (O termo linear depende com a latice, o termo cúbico depende das vibrações dos eletrões - para temperaturas maiores temos $c=\gamma T$)

## Experiência
- Como determinamos $c$?
    - Aquecemos a amostra de forma precisa para introduzir uma certa energia no sistema. Depois pedimos a variação da temperatura.7
    - No modo de capacidade térmica do Versalab

![[potencia vs T.png]]

- Para melhores resultados, a montagem usada deve ter baixa thermal mass e uma condutância térmica adequada. 
- Temos uma montagem assim:
![[montagem t4a v2.png]]
- Aqui temos:
    - o termómetro e aquecedor presos na parte de baixo do suporte
    - o suporte é feito de safira (que aparentemente é um cristal de alumina, logo é um isolador)
    - temos fios finos e curtos a fazer ligação elétrica ao aquecedor e termómetro. Também oferecem uma ligação térmica e suporte estrural
    - a amostra é metida no suporte com uma camada fina de gordura que dá o contacto térmico

- O sistema está em vácuo. Este vácuo é bom o suficiente para que a condutância entre o suporte e os fios seja decidida pela condutância dos fios.
- O Versalab mede a variação de temperatura como temos acima. Os dados são ajustados em MultiVu usando um modelo.

**Modelo 1-tau**
- Temos aqui uma explicação do modelo 1-tau. O modelo 2-tau é explicado no manual de heat capacity do versalab.
- Consideramos:
$$C_{total} \frac{dT}{dt}=P(t) - K_{w}(T(t)-T_{b})$$
($C_{tot}$ é a capacidade térmica total, $P$ a potência fornecida, $K_{w}$ a condutância dos fios, $T$ a temperatura e $T_{b}$ a temperatura do banho térmico)

- Temos que $P,T$ suguem os gráficos destas grandezas acima:
$$P=\begin{cases}
P_{0} & , & 0\le t\le t_{0} \\
0 & , & t>t_{0}
\end{cases}$$
se considerarmos que $T_{on}(0)=T_{b}~,~T_{on}(t_{0})=T_{off}(t_{0})$ podemos integrar e temos:
$$T(t)=\begin{cases}
\frac{P_{0}\tau (1- e^{-t/\tau})}{C_{total}}+ T_{b} & , & 0\le t\le t_{0} \\
\frac{P_{0}\tau(1-e^{-t/\tau})e^{-(t-t_{0})/\tau}}{C_{total}} + T_{b} & , & t>t_{0}
\end{cases}$$
em que temos a constante de tempo $$\tau=\frac{C_{total}}{K_{w}}$$
- O MultiVu ajusta com método least-squares. Calculando $\tau$ a várias temperaturas, conseguimos obter a relação $C_{total}(t)$.
- Notas sobre $C_{total}$
    - Isto é a capacidade térmica _total_ do sistema amostra+suporte+gordura
    - Para determinar o $C$ da amostra (que é o que queremos), precisamos de:
        1. Calibrar o sistema - medir sem gordura nem amostra. Permite-nos determinar $K_{w}$
            - dados são guardados num ficheiro ".cal"
        2. Para cada amostra que estudamos, fazer medição com suporte + gordura, _sem amostra_. 
            - também guardado no ficheiro de calibração
        3. Finalmente, estudar o sistema todo e medir $C_{total}$. Com os dados anteriores podemos determinar $C$.

**Caraterísticas do método**
- Este método permite medir $C$ ao longo de uma vasta gama de temperaturas. Mas se usarmos poucos dados ou se eles forem mal distribuídos, podemos perder caraterísticas da relação $C(T)$.
- Assim, se quisermos medir "second order phase transitions" (????) precisamos de outra técnica

**Análise**
- Analisamos o método de slope analysis de curvas de relaxação (como é o caso da nossa curva $T_{off}$). Ou seja:
$$C_{total}=\frac{P(t)-K_{w}(T(t)-T_{b})}{dT/dt}$$
nisto, calculamos $dT/dt$ em intervalos muito curtos.

## Experiência
**Preparação de amostra**
- Duvido que façamos, mas pronto
    1. Se temos a magnetite em rocha, esmagar até ter em pó. Se a temos em pó, passar ao próximo passo
    2. Prensar o pó até ficar um pellet, usando um die e uma prensa hidraulica
        - Colocar pouco pó no die e prensar a 13k pounds

### Procedimento
**Materiais**
- Gordura Apiezon N. 
    - Temos gordura N e H. 
        - A capacidade térmica de gordura N varia muito com $T>200K$
        - Gordura H sai de debaixo da amostra a temperaturas baixas
- Microscópio para ajudar a meter a gordura
- Balança de precisão de 0.1mg ou melhor
- Algum recipiente ou forma de mexer na amostra

**Procedimento em si**
1. Colocar o módulo de medir capacidade térmica. Ativar a opção de capacidade térmica do versalab.
2. Ter o puck e shield:
![[puck.png]]
3. Ver se existe ficheiro de calibração com o número de série do puck. Se não, calibrar.
4. Preparando para colocar uma pequena quantidade de gordura na zona onde vamos pôr a amostra, colocar o puck na estação de montagem da amostra para isto, para o estabilizar. Esta estação consiste num sistema em que metemos o puck, ele é seguro por um braço curvo e é mantido no sítio por um vácuo (sucção)
5. Colocar a N grease no suporte, *sem tocar nos fios*. Também não pode chegar gordura aos fios.
6. Fazer medição com suporte+gordura:
    1. Colocar o shield firmemente.
    2. Colocar o puck no versalab e tapar o versalab com a tampa com isolações térmicas.
    3. No software de controlo, clicar em "Prepare Addenda Measurement" e seguir as instruções.
    4. Selecionar os settings default que cobre a gama de temperatura toda de 50-389K. Só precisamos de ~20 pontos. 
    5. Esta medição demora horas, portanto não fazemos no lab :)))
7. Depois da medição de addenda e de o puck arrefecer, removê-lo do versalab.
8. Pesar um pedaço de amostra, só precisamos de alguns mg. 
9. Colocar o puck na estação de montagem da amostra. 
10. Colocar a amostra por cima da gordura. Pressionara a amostra para garantir bom contacto.
11. Colocar o shield e meter o sistema no versalab como novamente.
12. Fazer medição da capacidade térmica da amostra
    1. Clicar em "Prepare Sample Measurement" e seguir as instruções
    2. Clicar na tab de measurement. Clicar em "Measure Sample Heat Capacity vs Temperature". Clicar nos settings default sugeridos, que vai medir na gama 50-300K. Vai demorar várias horas???
    3. Podemos ver a medição em tempo real. Clicar na tab de ficheiros, em "Measurement Status".
    4. Depois de acabar a medição, ir à tab de ficheiros e clicar em "Data File" na secção "View".
13. Reconfigurar a medição para observar a transição de Verwey. Para isso, podemos usar uma sequência assim: 
    - Set Temperature 100K at 12K/min. Fast Settle
    - Wait For Temperature, Delay 300 secs, No Action 
    - Sample HC at current temperature, 50 K rise, 3 times, 3 tau meas. time 
    - Set Temperature 300K at 12K/min. Fast Settle
14. A análise pode ser feita no MultiVu (vamos fazer em casa de certezinha). 
    1. Clicar em "Raw Data File Viewing and Post Processing"
    2. Selecionar slope curve analysis method

FIM.