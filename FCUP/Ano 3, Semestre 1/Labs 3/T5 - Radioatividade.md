# Notas do protocolo
## 2 - Intro
**Decaimento** - quebra instantânea de um núcleo atómico instável, com a consequente emissão de radiação
- Temos 3 principais tipos de processos radioativos:
    - decaimento $\alpha$ - emissão de núcleos de Hélio-4
    - decaimento $\beta$ - emissão de eletrões ou positrões
    - emissao $\gamma$ - emissão de fotões de elevada energia

### Atividade
= Número de decaimentos atómicos p/ unidade de tempo: $$A =\dot{N} = \frac{\Delta N}{\Delta T}$$
- Expresso em Bequerel: $Bq=s^{-1}$ 
- *Densidade de atividade* - Atividade p/ unidade de volume:  $Bq/dm^{3}$
- Quando temos fontes com alta atividade usamos **Curie**: $1~Ci=3.7\cdot10^{10}Bq$ 

### Estatística
- O decaimento radioativo é um processo de eventos independentes entre si. É caraterizado pelo parâmetro *semi-vida* $T_{1/2}$ (tempo médio necessário para que um número de átomos se reduza a metade), que vem da equação do decaimento:
$$N=N_{0}e^\frac{-t}{\tau}$$
($N$ - número de átomos no instante $t$, $\tau$ - vida média da amostra, $1/\tau$ - constante de decaimento)
- Temos:
$$T_{1/2}=\Gamma=\tau\ln(2)$$

- Probabilidade de observar $N$ decaimentos numa amostra radioativa:
$$P(N)=\frac{M^{N}}{N!}e^{-M} \quad \quad;\quad \quad M=A \times \Delta t$$
em que, portanto, $M$ é o número médio de eventos ocorridos no intervalo de tempo de contagem ($\Delta t$).

### Alcance e Proteção
- O alcance da radiação é determinado pela sua interação com a matéria
- Materiais em geral são transparentes a radiação $\gamma$. O seu alcance depende da probabilidade de interação dos fotões de energia elevada com camadas eletrónicas mais profundas ou núcleos de átomos.
- Radiação $\alpha,\beta$ são formadas de partícula com carga. Assim, estas reagem com a nuvem eletrónica e com o núcleo; ocorrendo colisões. Como resultado, a radiação perde energia ao longo do percurso e sofre dispersão / scattering.
- Assim usasse materiais (como chumbo) para proteger de radiação, porque tem um elevado número atómico, o que significa que há alta probabilidade de interação. Existem ainda outros materiais/compostos mais eficientes e seguros.

### Fontes de Radiação
- Radiação é obtida de materiais naturalmente radioativos, purificação de materiais ou equipamentos como Raio X ou CERN.
- Radiação ambiente resulta de interação de raios cósmicos de alta energia com átomos de materiais terrestres.

#### Fonte de decaimento lento
- Na atividade teremos fonte de $^{226}Ra$, armazenado em tubo metálico com abertura.
- Semi-vida de 1620 anos.
- Emissão de partículas $\alpha,\beta,\gamma$
- Atividade de 3 kBq

#### Fonte de decaimento rápido
- Teremos contentor com 2 soluções, 1 aquosa 1 orgânica, de sais de urânio.
- Emissão está associada a decaimento de Protactinio 234. Semi-vida de 1.175 minutos
- Atividade de 45 kBq
- Explicação:
    1. Solução aquosa tem U238, tório-234 (atomos filho) e Pa234 (atomos neto). U238 e Pa234 formam complexos. 
    2. Ao agitar o contentor, os complexos dissolvem-se na camada orgânica (que flutua sobre a solução aquosa). Assim, 95% do Pa234 e algum U238 sobem para o topo. Tório fica na solução aquosa
    3. Contagens estão associadas ao decaimento do Pa234
- Decaimento de U238 e de Torio-234 não entram nas contagens porque:
    - detetor não deteta partículas $\alpha,\beta$ destes (só deteta particulas $\beta$ de Pa234 com alta energia)
    - decaimento de U238 é muito lento, tório234 decai com semi-vida de 24 dias. Podemos considerar ambos como tendo atividade constante. Só contribuem para a radiação de fundo.

#### Atividade das fontes
- Radiação é emitida para fora da fonte por "janela". Direções de emissão são aleatórias, logo podemos considerar emissão como *isotrópica*.
- Mas, por causa da "janela", as partículas têm área limitada para sair. Juntamente com a distância fonte-detetor define-se um ângulo sólido.
- Tendo-se a área de deteção $S_{det}$, para uma fonte a uma distância $d$ da fonte temos que, para uma atividade detetada $C$ a atividade total é:
$$A_{t}= \frac{4\pi d^{2}}{S_{det}}(C-C_{0}) \longleftrightarrow C-C_{0}=\frac{A_{t}S_{det}}{4\pi d^{2}}$$
em que $C_{0}$ é a radiação ambiente (medida sem a fonte).

### Tubo Geiger-Muller
- Consiste em câmara cilindrica preenchida com gás ionizável para umas certas energias. Um ânodo a alta tensão recolhe a carga de ionização gerada por cada interação. Isto é transmitido como 1 contagem.
- A contagem pode ser simples (contar), ou pode ser registada a carga gerada pela ionização do gás, que está relacionada com a energia da radiação.
- Na atividade iremos usar em modo simples.
- Entre contagens há um *tempo morto* em que a eletrónica se reinicializa para a próxima medida. Por esta razão, em casos em que ocorrem muitas medidas, o detetor pode contar menos que o esperado, devido a contagens falhadas.

## 3 - Perguntas Preparação
1. a
2. Para radiação $\gamma$, intensidade deverá diminuir com $1/d^{2}$ pq é basicamente um deixe de luz. As restantes serão dispersadas consoante colidem com ar, então n sei
3. Temos $M$ eventos para contar. Tempo morto afeta se $\Delta t > 1/M$
4. domingo faço ig
## 4 - Execução
#### Equipamento
**Detetor**
- $A=0.635~cm^{2}$, tempo morto de $100~\mu s$
- Não tocar na face frontal do detetor destapado
- Podemos configurar o número $M$ de medidas de forma
    - *automática* - o tempo de recolha é automático. Dá tabela $(t,\bar N)$
    - *manual* - utilizador indica $M$ - util quando mudamos a posição/angulo do detetor entre medidas.
- Recomendado desativar a opçao de retirar a atividade ambiente automaticamente e fazer isso nós

### Medida de Atividade Ambiente
1. Afastar fontes do detetor
2. Configurar
    1. tempo $\Delta T$ que o detetor passa a fazer cada medida (tempo que passa a contar). Recomendado: 10s
    2. número de medidas a fazer, $n$
3. guardar. Ficheiro tem q ter menos de 8 carateres. Apontar no caderno.
4. Estimar atividade de fundo
5. Ver pergunta no 4.1 do protocolo

### Fonte Lenta
#### Estatística
1. Colocar fonte com saida perto do detetor, sem tocar, a alguns mm
2. Configurar $\Delta T$ de forma a ter nº médio de contagens acima de 50
    1. meter em modo automático para 100 medidas. guardar
    2. repetir para números de medidas diferentes (podemos fazer combinações de experiências para ter 1000+ medidas)
3. Mudar posição da fonte de modo a ter <10 contagens. Repetir passos acima.
4. Fazer histogramas.

#### Caraterização da fonte
1. Determinar atividade com detetor, para distâncias fonte-detetor ao longo de 30mm de 1 em 1 mm
    1. Meter software em modo manual: $\Delta t\sim 10s$, 30 medidas (aka 30 distâncias)
    2. aproximar fonte o máximo possivel
    3. começar medidas. Após cada medida, afastar fonte 1mm
2. RADIO1 - n percebi, ver protocolo / perguntar pilar
3. Gravar. 
4. Continunar mesmo processo de antes a partir da posição final, mas agora afastar 1cm de cada vez. Fazer até ter atividade próxima da atividade ambiente
5. estimar alcance com regressão linear

### Fonte Rápida
1. Meter detetor em modo automatico, a fazer contagens por pelo menos 15min com  adequado (ter em conta semi-vida ao escolher este). Iniciar
2. Colocar contentor À frente do detetor *sem agitar*. Radiação emitida sem agitar deverá ser tida como "radiação ambiente"
3. agitar durante alguns segundos e colocar no mesmo local
4. recolher dados por pelo menos 5min
5. guardar e registar nome ficheiro no caderno
6. estimar semi-vida com dados obtidos

## Outros
### Dependência angular
![[rad-angulo.png]]
1. Montar como acima
2. Registar intensidade da radiação para angulos entre -60º e +60º
3. Se formos de -60 a +60 de 10 em 10º temos 13 medidas. Registar 13 medidas no programa (aka 13mm). Colocar tempo contagem de 30s ou mais.
4. Registar dados à mão
5. Estudar relação contagens VS angulo

### Efeito de Campo Magnético
![[rad-angulo-iman.png]]
1. Montar como acima, com polo Norte para cima
2. Repetir secção acima, tal e qual
3. Inverter iman (polo norte para baixo)
4. Reptir secção acima outra vez

#### Observar radiação $\gamma$
1. Montagem acima, com polo norte para cima
2. Colocar placa de alumínio junto a abertura da fonte
3. Repetir secção do ângulo

#### Variação de $\gamma$ com distância
1. Da montagem atrás, tirar iman e transferidor. Deixar placa alumínio. Meter detetor a 3cm da fonte
2. $\gamma$ pouco afetada por ar, fonte é basicamente pontual. Esperasse que intensidade diminua com $1/d^{2}$, porque é como se tivessemos um feixe de luz.
3. Variar ao longo de 15cm, de 1 em 1cm. Intervalo de contagem de 30s
4. Meter em modo de medir rad ambiente / medida do zero.
5. repetir procedimento acima
6. Pontos 8-10 abaixo :)
![[t5-ultima parte.png]]
NAO ENTENDOOOOOO

