##### "Experiment on Planar Waveguides: Prism coupling"

## Teoria
- Um guia de onda step-index (**SI**) é uma camada de material com indice de refração (**RI**) alto, rodeado dos 2 lados por materiais com índice inferior:
![[Pasted image 20241126214010.png]]

- Podemos ver um guia de onda como um meio em que ocorre uma série de reflexões internas totais que ocorrem nas interfaces do material com os que o rodeiam, que têm RI inferior. Isto ocorre conforme os índices de refração e o ângulo de incidência, que tem que ser maior que o ângulo crítico.
- A condição que tem que ser cumprida para que a luz seja guiada é: 
    - As componentes da onda transversais (perpendiculares ao plano do guia de onda, transversais à propagação da onda) têm que interferir de forma a gerar uma *stangin wave*.
    - Caso contrário, teríamos transferência/fluxo de energia na direção transversa - não estaríamos a confinar a energia. Ao cumprir esta condição, garantimos que só há fluxo de energia na direção de propagação - a onda está a ser guiada.

- Ora, se a componente transversa é uma onda estacionária, então quer dizer que a temos que aplicar condições de fronteira nos extremos do guia:
![[tla1_1|1000]]
isto implica que apenas existem apenas alguns ângulos, discretos, que nos permitem que a onda seja guiada. A cada um destes ângulos chamamos de **modo**.
- Para um guia planar de espessura $d$ e RI $n_{2}$, os ângulos permitidos ($\theta_{m}$) são dados por:
$$\frac{2\pi dn_{2}\cos\theta_{m}}{\lambda_{0}}=m\pi+\phi_{1}+\phi_{3}$$
($\lambda_{0}$ é o comprimento de onda da luz, $m\in\mathbb{Z}$ e $\phi_{1},\phi_{3}$ são mudanças de fase evanescente nos interfaces com os meios 1 e 3)

### Propagação dos modos
- Cada modo se propaga com uma velocidade de fase específico. Esta velocidade é ditada pelo RI efetivo: $n_{e}=n_{2}\sin\theta_{m}$. Podemos então reescrever a equação acima:
$$\frac{2\pi d\sqrt{n_{2}^{2}-n_{e}^{2}}}{\lambda_{0}}=m\pi+\phi_{1}+\phi_{3}$$
em que
$$\phi_{i}=\tan^{-1}\xi \left(\frac{n_{e}^{2}-n_{i}^{2}}{n_{2}^{2}-n_{e}^{2}} \right)$$
- O valor da função $\xi$ depende da polarização da luz guiada. Teremos $\xi=1$ para modos TE (o campo elétrico é transversal à propagação), $\xi=n_{2}^{2}/n_{i}^{2}$ para modos TM (o campo magnético é transversal à propagação).

### Coupling do feixe
- Vejamos como o feixe pode ser "encaixado"/"inserido" no guia.
- O feixe pode ser colimado/focado para o guia de onda usando um prisma com RI alto, preso ao lado do guia. 
- Mais concretamente, para haver coupling é preciso que
    - O RI ($n_{p}$) do prisma tem que ser maior que o do guia
    - O prisma e o guia têm que ter um bom contacto ótico, para garantir que o campo evanescente da reflexão interna total entra no guia
    - O RI efetivo e a velocidade da fase da luz ao atingir a parte de baixo do prisma permite gerar um modo no guia. Este ajuste é feito ao rodar a montagem guia+prisma até termos guiagem.
![[Pasted image 20241126224020.png]]

- O índice de refração *efetivo* ($n_{ep}$) do feixe a incidir do prisma para o guia era $n_{ep}=n_{p}\sin\theta_{p}$, em que $\theta_{p}=\theta_{t}+A$ (conforme indicado na imagem acima)
- Pela lei de Snell, podemos escrever $n_{p}\sin\theta_{t}=\sin\theta_{i}$. 
- Assim, o RI *efetivo dos modos* ($n_{e}$) pode ser escrito assim:
$$n_{e}=n_{ep}=n_{p}\sin \left(A + \sin^{-1} \left( \frac{\sin\theta_{i}(m)}{n_{p}} \right) \right)$$
em $\theta_{i}(m)$ é o ângulo de incidência que resulta na criação do modo $m$.

### Retirar o feixe
- Este processo é invertível. Podemos retirar o feixe da guia de onda ao acoplar um 2º prisma, a cerca de 1-3cm do primeiro.
- Se os prismas forem iguais, o feixe sairá com o mesmo ângulo que entrou no primeiro (ver abaixo).
![[Pasted image 20241126230328.png]]

## Procedimento
1. Montar o sistema como mostrado acima. O prisma e o método de acoplamento deste usado devem estar centrados na plataforma rotativa. Rodamos o sistema para variar o ângulo de incidência do feixe. Limpar bem o prisma
2. Ajustar o polarizador para ter polarização TE (campo elétrico transversal à propagação).
    1. Primeiro, meter com polarização vertical 
    2. Temos máximo coupling do prisma ao guia na zona diretamente por baixo de onde o clamp prende o prisma (maior pressão logo menos distância).
3. Rodar a montagem até se ver uma linha contínua iluminada no guia - atingimos *guiagem de onda*. 
    1. Consoante rodamos, podemos continuar a ter coupling e guia de onda (temos uma linha), mas ela pode perder intensidade porque já não estamos no ângulo lateral ideal.
    2. Colocar o segundo prisma. Agora, ao rodar poderemos ver as 2.linhas de coupling numa folha de papel mais afastada. 
4. Medir os ângulos $\theta_{i}(m)$ relativamente à normal para os quais temos guiagem. 
    1. Determinamos o ângulo da montagem em que temos incidência normal, que acontece quando temos o feixe no mesmo plano que a superfície de incidência. Para ver isto, metemos um papel branco abaixo da montagem e vemos de cima.
    2. Os ângulos $\theta_{i}$ são a diferença entre o ângulo normal e o ângulo medido na hora que temos guiagem
5. Tendo $\theta_{i}(m)$ para todo o range, calcular $n_{e}$
6. Repetir os pontos 2-4 mas agora colocando polarização TM (campo magnético normal)
7. Na equação $\frac{2\pi d\sqrt{n_{2}^{2}-n_{e}^{2}}}{\lambda_{0}}=m\pi+\phi_{1}+\phi_{3}$ conhecemos tudo menos $n_{2}$ e $d$ (espessura e RI do guia de onda). 
    1. Se tivermos medido o ângulo para 2 modos diferentes, teremos um sistema com 2 equações, com 2 incógnitas.
    2. Para resolver isto, a melhor abordagem é um método numérico. Uma forma:
        1. Fazer plot de $d(n_{2})$ conforme determinado com as equações para $m=0$ e $m_1$, dentro do range de ângulos possível. 
        2. Os valores $d,n_{2}$ melhores poderão ser determinados ao ver a interseção das curvas.
    3. Repetir isto para as curvas obtidas em medições de polarização TE e TM
    4. Existe uma rotina de python para fazer isto no sigarra!!!

- Só não percebi como metemos a polarização TE ou TM