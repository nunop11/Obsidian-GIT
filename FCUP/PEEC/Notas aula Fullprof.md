### Ficheiros
- XRD da FCUP (Rigaku) dá os dados na forma de 3 ficheiros: asc, raw e ras
- Normalmente usamos o *.ras*. Dá para abrir normalmente no VSCode
- Antes de começar a trabalhar, fazer cópia do ficheiro, guardar como *.dat* e eliminar todas as linhas de informação do Setup no início (até onde tem 3 colunas de dados) 
    - Dá para automatizar isto se tivermos muitos ficheiros paraver

### Começar
#### Vesta / cif
- Fazer esta parte se tivermos um ficheiro cif ou vesta da estrutura que foi feita XRD
- Podemos ver no ficheiro em si ou ao clicar nos átomos no VESTA:
    - grupo de simetria
        - Escrevemos normalmente P n m a, Pnma
        - O Fullprof precisa de uma formatação específica, então mais vale meter o *número*: 62
    - Posições dos átomos, multiplicidade, fatores ocupação
    - Parâmetros de rede

## Fullprof
![[fpf_1.png]]
- Selecionar O EdPCR, onde iremos configurar os CIF

#### PCR
![[fpf_2.png|500]]
- A primeira opção é este botão, em que podemos colocar um cif e ele é convertido em pcr.
- Isto é bom quando o cif está bem feito e permite poupar muito trabalho
- Obtemos isto:
![[fpf_3.png|500]]
Vemos que está tudo bem. Na aba "Atoms Information" vemos as posições, B e fator de ocupação dos átomos na célula unitária.
- Carregamos em OK e voltamos ao início do EdPCR. 
- Se clicarmos em "Save Data" guarda na pasta de onde tiramos o cif, em que fica com o mesmo nome que o cif

#### Intensidade
- Este programa é focado noutras técnicas que têm intensidades menores. No nosso XRD temos intensidades da ordem de $10^{5}$ contagens por minuto.
- Assim, ele usa o chi-quadrado como referência para fazer o fit dos dados. Ora, quando temos valores tão longe do que ele espera, o chi-quadrado vai ser sempre mau e ele pode achar que "melhorou" o fit, quando na realidade está igualmente mau.
- Assim, para reduzir as chances de isto, normalizamos os dados para ficar de 0 a 1.

#### Ficheiros André
- Nos ficheiros de XRD que o andré deixou, tenho 4 colunas: yobs, ycal, bkg e diff
![[fpf_4.png]]
- Penso que seja: intensidade observada, calibrada, backgroud/base line e a diferença entre o yobs e bkg

#### Tratar Background
- Pegar no ficheiro ASC, tirar texto todo como dito acima e meter DAT
- Abrir Winplotr na barra do FPF
- Abrir ficheiro DAT com a formatação "X,Y data + INSTRM=10"
- Aparece espetro. Podemos ver e fazer zoom à vontade (ituitivo e rapido)
- Selecionar: Points Selection -> Automatic Background
    - Em geral, podemos deixar o threshold e num de iterações no default do propgrama.
- Ele gera **até 99 pontos** de background:
![[fpf_4.png]]

- Imaginemos que ele marcou como bkg um ponto que não queríamos. Fazemos: Zoom na secção onde está o ponto, de modo a ver bem as bolas -> Points Selection -> Remove Peak/Bkg -> Carregar no ponto a remover:
![[fpf_5.png]]
aqui vemos um ponto que foi removido (entre o 3º e o 4º pontos verdes)

- Outra opção é: Points Selection -> Select Background Points. 
    - Selecionamos com o lado esquerdo do rato os pontos de base 1 a 1. Ficamos com uma linha de base aproximada e que parece bem
    - Para isto, fazer zoom numa zona e ir andando para o lado com as setas enquanto selecionamos (setas não me funcionou)
    - 1 click lado direito guarda os pontos selecionados, 2 clicks reinicia o zoom.
    - "Save background points" com o mesmo nome do ficheiro PCR e fica *.bgr*

### Começar análise de dados
- Abrir o EdPCR
- Preencher cada um destes


**General**
- O title é algo que deve ajudar a identificar logo
- Selecionamos a primeira opção: Refinar espetro XRD
- Podemos selecionar a cena de optimizar, não deve ter problema

**Patterns**
- Aqui torna-se **útil** ter o DAT,PCR,BGR,CIF _todos_ com o mesmo nome!
- Vamos colocar:
    - *Data file*
        - Data File / Format - selecionar o DAT no browse. Selecionar formato X,Y,SIGMA
        - Refinement
            - X-ray : usar dados XRD -> Selecionar
            - Pattern Calculation : simular padrão XRD teórico
            - Selecionar comprimento de onda de Cobre *Cu* (no ficheiro RAS em cima é indicado o comprimento de onda e vemos que bate certo)
        - Pattern Calculation / Peak Shape
            - Normalmente selecionamos Pseudo-Voight
            - O 2theta e o range são metidos automaticamente ao meter o DAT
            - Range of calculation of FWHM : se tivermos picos muito largos, aumentar valor. MAS ao aumentar a janela podemos passsar a ignorar picos próximos, então deixamos como está e depois vemos o que mudar
    - *Background Type*
        - Os tipos normais são: 
            - Linear interpolation no caso de termos um bkg quase linear
            - Polinomio de 6 coeficientes - colocar a ordenada na origem do bkg na caixa em cima
    - *Excluded Regions*
        - Para definir regiões para eliminar, por exemplo quando temos o espetro do suporte (alumínio por Ex) a ser medido em certos ângulos
        - Simplesmente colocamos os angulos limite a rejeitar
    - *Geometry / IRF*
        - Normalmente usamos na geoemtria : "Bragg-Brentano or Debye-Scherrer  Geometry"
        -  Normalmente usamos no IRF : "None"
            -  Invés disso, podemos selecionar o FWHM. Nesse caso precisamos de saber U,V,W que podemos obter ao perguntar ao ChatGPT os valores para um Rigaku Smartlab
            - Isto acontece pq IRF é "Instrument Refinement File" e não costumamos fazer isso na FCUP
            - Para o Gonçalo o ChatGPT deu: ![[fpf_6.png]]
            - De notar que ao pedir ao Chat devemos explicar a montagem e cenas para ele encontrar IRFs de casos parecidos
        - Correções:
            - External Correction : None
            - Prefered Orientation : Não é super importante, tem a ver com o crescimento de filmes finos. Normalmente colocamos: Rietveld-Toraya
            - Outros: não mexer
    - *User Scatt Factors*
        - Não mexer :)
    - *Add*
        - Com isto e os botões ao lado, podemos fazer esta configuração toda para vários ficheiros DAT e assim fazemos fit de varios espetros de uma vez
        - Isto para certos casos específicos claro

**Phases**
- Name : algo que ajude a entender
- Calculation : Profile Matching with constant scale factor
    - Usado para começar o fit
    - Começa por ver os picos e ver se eles estão nos 2theta que deviam de estar de acordo com a estrutura (ignora-se a intensidade relativa dos picos nem os tipos de átomos sequer)
    - Outra opção: Rietveld, que selecionamos depois. Este já tem em conta os tipos de átomos e intensidades
- *Contribution to patterns*:
    - Voltar a colocar X-Ray e Pseudo-Voight
    - Selecionar "Automatically generated..." em baixo. Em iterações posteriores podemos selecionar HKL, mas na primeira ainda não existe. Ou seja, a certo ponto quando o fit estiver com a,b,c,u,v,w decentes vimos mudar aqui para HKL
        - Isso faz com que ele recomece o fit mas a começar de algo que já está OK
- *Simmetry*
    - Selecionar "Generated automatically from the symbol"
    - Meter o número do grupo de espaço e clicar no botão à direita para fazer automática.
    - Decide onde e quantas vezes um átomo que define a célula unitária é repetido nela
    - Muito importante. Se estiver mal, nada vai funcionar
    - Podemos fazer Add para meter mais fases em estudo, repetindo-se o mesmo estudo mas com outras geometrias. Isto é importante para mim, já que na amostra em pó queremos ver se a fase ortorrombica e hexagonal estão a coexistir

**Refinement**
![[fpf_7.png]]
- No topo, meter o número de ciclos alto tipo em 30
    - Quando estamos mais avançados, meter mais baixo tipo em 5/6. Senão podemos perder a solução
- Na parte do Stop Criterium, ele para antes do número de iterações se:
    - Estivermos abaixo de um certo chi quadrado - selecionar no drop down
    - Não paramos : profile matching mode - selecionar no drop down
- Reflections ordering: Each cycle
- Pattern: (*importante*)
    - Background -> Linear interpolation -> importar BRG (refinar apenas mesmo mesmo na parte final do fit)
    - Instrumental
        - Zero 
            - Introduzir shift total no pattern. 
            - Tem a ver com montagem da amostra no XRD. 
            - Meter algo do tipo +- 0.01 mas não demasiado pequeno. Clicar no visto para ficar a refinar
    - Não mexer mais nada
- Phase : (*importante*)
    - Para cada fase que temos
    - **Profile** - Janela mais importante
        - Escala - refinar apenas ao passar para Rietveld. Exceto se tivermos escala perto de 1, aí refinar logo
        - U,V,W é o que meti acima, ver ChatGPT ![[fpf_8.png]]
        - U e V *com sinais opostos*
        - Eta 0 tem a ver com o quão gaussiana ou lorentziana os picos são. Começamos com 0.5 para dizer que é meio-meio
        - X,IG vemos depois
        - Asymmetry e Prefered orientation 

**Constraints**
- Não se mexe 

**Box / Restraints**
- Não se mexe para já

**Output**
- Fazemos overwrite para atualizar o PCR. 
    - Caso contrário fazíamos 1 iteração, carregamos o PCR novo e fazemos a seguinte. Nada prático
- Podemos fazer o CIF
- *General Output Information* : 
    - OUT : Em geral, deixar tudo como está não tem mal
    - SUM : Meter visto no Analysis of goodness of fit, ajuda a ter uma ideia do fit
- *Patterns Output Information*
    - Refinement Plot on Screen : alterar o range do espetro mostrado no ajuste (mas ele usa sempre o espetro todo no fit)
    - A todos os outros ficheiros o Gonçalo disse "para já n faz falta"
    - Em cada ficheiro podemos selecionar que queremos esse output, mas para um só 
- *Phases Output Information*
    - Em cada ficheiro podemos selecionar que queremos esse output, mas para uma só phase
    - DIS : para ter informações sobre a estrutura quando temos fits em função de temp ou outra coisa
        - Penso que seleciono este para as 2 fases porque temos Fit VS tBM
    - Do resto não se falou

### Refinar
- Clicar no botão "run FPF program" na aba de cima do EdPCR

### Treinar
- Ir sempre variando
- Do tipo: correr e refinar o Instrumental, depois os parametros rede, depois U,V,W, depois eta0
- Depois tentar combinações (a e b, a e c, b e c, a e U, etc etc)
- Podemos abrir PRF com WinPltr, muito melhor que o que aparece ao correr
- Se estivermos presos num minimo local, em Phases voltar a Contribution to patterns e meter Automatically. Pode tirar-nos do minimo e correr melhor
- IR GUARDANDO VERSOES QUE REDUZAM CHI2 BASTANTE!!!!

