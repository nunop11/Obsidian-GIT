#### Importância
- Em 2020, $1.6\cdot10^{9}\text{ km}$ de fibra ótica foram instalados no mundo. 
- Para comparação, a distância de ida e volta Terra-Jupiter é de cerca de $1.5\cdot10^{9}\text{ km}$.

### Tipos principais
![[tipos de fibra multimodo.png]]
![[fibra monomodo.png]]

### Equações
- Podemos analisar os ângulos num esquema como o de baixo:
![[propagacao em fibra simetria.png]]
e vemos que:
$$\sin\phi_\text{min}=\frac{n_{2}}{n_{1}}~~~~;~~~~\sin\theta_{0,\text{max}}=\sqrt{n_{1}^{2}-n_{2}^{2}}$$
- *NOTA* : Aqui mudamos a notação (lol). Agora, ângulos de reflexão relativo à normal são $\phi$ e relativos â superfície são $\theta$. Nos guias usamos $\theta,\overline{\theta}$ nestas situações.

- Facilmente vemos que $\sin\theta_{0,\text{max}}$ está relacionado e identifica a **abertura numérica** da fibra:
![[abertura numerica em fibra.png]]
e isto é algo que já vimos para os guias planos.
- Podemos escrever:
$$\text{NA}=\sqrt{n_{1}^{2}-n_{2}^{2}}=\sqrt{(n_{1}-n_{2})(n_{1}+n_{2})}$$
- Se os índices de refração forem próximos podemos dizer: $n_{1}+n_{2}\approx 2n_{1}$
- E podemos definir $\Delta = \frac{n_{1}-n_{2}}{n_{1}}$
- E temos:
$$\text{NA}\approx n_{1} \sqrt{2\Delta}$$

### Tipos de raios
#### Meridionais
- Raios que se propagam, sempre contidos num plano
![[raio meridional fibra.png]]

#### Oblíquos
- A situação mais geral
- O feixe mais refletindo em planos a uma distância $R$ do centro da fibra
![[raio obliquo fibra.png]]

## Fabricação de fibras
- Ao fabricar fibras, queremos fazê-las de materiais que permitam:
    - estruturas longas e flexiveis
    - transparência em certos comprimentos de onda
    - controlar muito bem o índice de refração por dopagem
- Os materiais usados normalmente são *óxidos de vidro*, nomeadamente a **sílica SiO2** 

### Bainha
![[fibra step index.png]]
- Para ter reflexão total interna, precisamos que $n_{2}<n_{1}$ (índice bainha < índice nucleo)
- Opções:
    - **N** : Silica dopada com GeO2, **B** : Silica
    - **N** : Silica dopada com P2O5, **B** : Silica
Silica permite controlar muito o índice de refração ao dopar:
![[dopagem e n.png]]

### Processos
- A maioria das técnicas usa processos *vapor-phase oxidation*
    - Temos vapores metalicos (SiCl4 ou GeCl4) reagem com oxigénio
    - Formam-se então partículas SiO2
    - Por aquecimento estas partículas são transformadas numa mass homogénea chamada **preforma**
- Depois ela é esticada de forma a formar um fio fino e uniforme
- Caso real:
![[fabrico de silica e performa.png|244]]
- No primeiro passo após arrefecimento a fibra é revestida com uma resina que protege a bainha de contaminações
- A espessura final da fibra é decidida pela velocidade com que a enrolá-mos

### Produção de preformas
- Algumas técnicas usadas:
    - Outside Vapor-Phase Oxidation (OPVO)
    - Vapor-Phase Axial Oxidation (VAD)
    - Deposição Vapor Químico Modificado (MCVD)
    - CVD ativada por plasma (PCVD)

#### OPVD
- Processo mais antigo
- Partículas de sílica formam-se no ar através do processo descrito acima. Elas são depositadas num cilindro rotativo de cerâmica ou grafite. Podemos adicionar partículas nesta atmosfera para dopar
![[opvd.png]]
- A preforma é criada então camada a camada
- Depois removemos a vara e o tubo de vidro (poroso) é aquecido a 1400C, tornando-se em vidro solido transparente (o buraco central colapsa)

#### VAD
- Partículas de silica fabricadas da mesma forma que já vimos
- Depois são depositadas no fundo de um cilindro  de vidro
- Uma preforma porosa é obtida ao mover o cilindro na vertical. No final esta é aquecida para ficar sólida e transparente.
![[vad.png|360]]
Na câmara de baixo ocorre reação, as partículas de SiO2 criam-se e depositam na base do cilindro. Entretanto no topo temos uma seed que roda (para termos algo uniforme) e que sobe (para termos um cilindro).
- Temos as seguintes vantagens face a OPVO:
    - A preforma agora já não tem buraco central
    - Temos mais controlo no tamanho dos cilindros
    - Sistema de fabricação mais compacta

#### MCVD
![[mcvd.png]]
- As partículas são mais uma vez formadas como atrás. Depois são metidas dentro de um tubo de sílica. Este depois faz de bainha
    - As partículas usadas podem ser sílica ou sílica + um dopante
- As partículas depositam na parede interna do tubo por CVD. Depois essa massa é convertida em vidro sólido e transparente através de uma chama que se move para frente e para trás e aquece o tubo.
- Continuamos até ter a espessura total desejada
- Quando terminado, aquecemos muito o conjunto todo de forma a colapsá-lo todo num cilindro solido - a preforma

#### PCVD
![[pcvd.png]]
- Tal como em MCVD, fazemos deposição de sílica dentro de um tubo de sílica (que fará de bainha)
- O tubo é mantido a 1000-1200C durante todo o processo. 
- Usando microondas a 2.45GHz geramos um plasma no tubo. Isso faz com que depositemos vidro transparente diretamente no tubo
- Quando temos a espessura desejada simplesmente aquecemos o cilindro e ele colapsa num cilindro sólido
- MCVD e PCVD são os mais usados atualmente

### Fibras estruturadas / fotónicas
![[fibras com buracos.png]]
- Os métodos que vimos apenas fazem fibras "normais" e sólidas
- Mas por vezes podemos precisar de fibras estruturadas como vemos acima
- Depois da preforma, esticamos a fibra como normalmente
- O processo acaba por ser mais simples - Neste caso *não é preciso dopar* a fibra. Neste caso obtemos os buracos ao organizar espaços com ar dentro da preforma. Ao esticar, ficamos com a forma pretendida

### Propriedades mecânicas da fibra
- Ela tem resistência a extensão similar a alguns metais - tensão longitudinal até 14 GPa (20 para o aço)
    - Na prática, quando há defeitos e falhas na fibra, a tensão é reduzida para apenas 700-3500 MPa
- A grande diferença está na deformação:
    - fibras deformam até 1% (sem fratura) e têm deformação elástica
    - metais deformam até 20% (sem fratura) e têm deformação plástica a partir de certo ponto

#### Microfraturas
- Vimos que defeitos, falhas e microfraturas reduzem a tensão 
- Vamos modelar uma situação com uma microfratura:
![[modelagem de mricrofratura em fibra.png]]
- Para que a fibra não quebre, é preciso que:
$$h< \left(\frac{K}{\sigma \sqrt{\pi}}\right)^{2}$$
em que $K$ depende da fibra especifica que está na ordem de $0.1 \text{N/mm}^{2}$
- Vemos que $h$ diminui muito rapido consoante $\sigma$ aumenta e que será sempre muito baixo.

#### Fadiga estática
- Consiste no crescimento lento das microfraturas sob condições de tensão contínua aplicada. 
    - Humidade também aumenta este efieto - água ataca as os grupos SiO2
- Eventualmente, isto leva à rutura em tensões muito inferiores às tensões de testes de carga
- Isto pode ser reduzido com **revestimentos poliméricos**

#### Fadiga Dinâmica
- Quando a fibra é sujeita a tensões variáveis ao longo da fibra, durante instalação ou operação
    - EX: fibras em cabos aéreos, sujeitas a vento
- Para testar isto, a fibra é sujeita a tensão maior do que aquela que prevemos que ela irá enfrentar

### Cabos
- Servem para proteger a fibra com uma estrutura resistente a deformações e ao ambiente
- São importantes: a fibra só tem deformação elástica logo é péssima a absorver energia em colisões
- Permite ligar a fibra em sistemas como se fossem fios elétricos
![[cabos fibra.png]]

### Outros tipos
#### Fibras de Haletos
- Estas têm menor perda no intervalo 0.2-8 um
- Uma das melhroes composições: ZBLAN (Zirconio, Bario, Lantanio, Aluminio, Sodio)
![[fibra ZBLAN.png]]
- Este material é pior para fibras longas, porque ainda tem menos elasticidade e quebra facilmente.

#### Fibras de plástico (POF)
- Mais baratas e flexiveis
- Temos de ter diametro maior, mas também temos mais tolerancia
- Mais útil em redes locais
- O mais comum é POF PMMA (polimero) e POF PFP (perfluorinato)

## Propagação em fibras óticas
- Vamos usar uma abordagem diferente daquela para as guias. Para estas:
    - Consideramos que o campo era do tipo onda plana e propagava-se no meio segundo $\pm\theta$
    - Procuravamos os ângulos de oscilação em que as ondas planas nas direções $+\theta,-\theta$ se cruzam de forma a ter uma padrão de interferência independente de $z$:  ![[planos interferencia guia planar.png]]
    - Para estudar a diferença de fase entre as ondas usou-se Fresnel
    - Determinamos os ângulos modais. Os vetores de onda foram obtidos ao inserir estes ângulos nas equações para as ondas planas. 
    - Usou-se a equaçãi de Helmholtz para ter o campo na bainha
    - Consideramos que a polarização era constante e TE ou TM 

- Nas fibras óticas:
    - Iremos usar um método geral, com as equações de Maxwell. Esta técnica será aplicável a *qualquer circunstância*
    - Procuramos soluções de campo modal tendo em conta: a geometria do guia/fibra/etc e o perfil do índice de refração no meio

### Tipos de modos
- **Modos guiados** - propagam-se ao longo da fibra, confinados ao núcleo. Temos reflexão interna e baixa atenuação
- **Modos de radiação** - modo em que feixes saem do núcleo. A bainha tem dimensão finita e temos $n_{bainha}>n_{ar}$. Assim a luz que chega ao limite externo da bainha é principalmente absorvida. Isto resulta num modo maioritariamente na bainha, com muito alta atenuação.
- **Modos "Leaky"** - modos muito obliquos. Consoante se propagam, uma porção do feixe tem reflexao enquanto que outra passa para a bainha. Eventualmente o feixe desaparece. Este modo é uma espécie de mistura dos 2 casos acima.

## Análise teórica
- Devido à geometria das fibras, usamos *coordenadas cilindricas*:
$$\vec{E}=E_{r}\hat{r} + E_{\phi}\hat{\phi} + E_{z}\hat{z}$$

- Começamos esta análise com as equações de maxwell para meios isotrópicos, lineares e sem carga/corrente:
$$\begin{align*}
\nabla \times \vec{E}&= - \partial_{t}\vec{B}\\
\nabla \times \vec{H}&= \partial_{t}\vec{D}\\
\nabla \cdot \vec{D}&= 0\\
\nabla \cdot \vec{B}&= 0
\end{align*}$$
em que $\vec{D}=\varepsilon\vec{E}=\varepsilon_{0}\vec{E}+\vec{P}~~,~~\vec{B}=\mu\vec{H}=\mu_{0}\vec{H}+\vec{M}$

### Monocromáticas
- No caso em que procuramos soluções monocromáticas, temos que a equação de Helmholtz dá as amplitudes permitidas: $$\nabla^{2}U + n^{2}(r)k_{0}^{2}U=0$$
que em coordenadas cilindricas fica:
$$\frac{\partial^{2} U}{\partial r^{2}} + \frac{1}{r}\frac{\partial U}{\partial r} + \frac{1}{r^{2}}\frac{\partial^{2}U}{\partial\phi^{2}} + \frac{\partial^{2}U}{\partial z^{2}}+n^{2}(r)k_{0}^{2} U=0$$
- Pode parecer que temos que resolver isto em todas as direções do campo EM. Mas não. Isso será concluido ao ver a análise com equações de maxwell

### Maxwell
- Queremos ter uma onda a propagar-se nos ZZ, com direção de oscilação independente de ZZ:
$$\begin{align*}
\vec{E}&= \vec{E_{0}} e^{i(\omega t-\beta z)} \\
\vec{H}&= \vec{H_{0}} e^{i(\omega t-\beta z)} 
\end{align*}$$
(em que $\beta=k_{z}$)
- Ao colocar estes campos nas equações de maxwell e separar as componentes dos campos vetoriais:
    - *Equação de Faraday* $$\begin{align*}
\frac{1}{r} \left(\frac{\partial E_{z}}{\partial \phi} + ir \beta E_{\phi} \right) &= -i\omega\mu H_{r}\\
i\beta E_{r} + \frac{\partial E_{z}}{\partial r}&= i\omega\mu H_{\phi}\\
\frac{1}{r} \left(\frac{\partial(rE_{\phi})}{\partial r} - \frac{\partial E_{r}}{\partial \phi} \right)&= -i\omega\mu H_{z}
\end{align*}$$
    - *Equação de Ampere-Maxwell*$$\begin{align*}
\frac{1}{r}\left(\frac{\partial H_{z}}{\partial \phi} + ir \beta H_{\phi} \right)&= i\omega\varepsilon E_{r}\\
i\beta H_{r} + \frac{\partial H_{z}}{\partial r} &= -i\omega\varepsilon E_\phi\\
\frac{1}{r}\left(\frac{\partial(rH_{\phi})}{\partial r} - \frac{\partial H_{r}}{\partial \phi} \right)&= i\omega\varepsilon E_{z}
\end{align*}$$
- Vemos que estas equações têm todas a mesma forma
- Dá para establecer então que:
$$\begin{align*}
E_{r}&= \frac{-i}{q^{2}} \left(\beta \frac{\partial E_{z}}{\partial r} + \frac{\mu\omega}{r} \frac{\partial H_{z}}{\partial \phi} \right)\\
E_{\phi}&= \frac{-i}{q^{2}} \left( \frac{\beta}{r} \frac{\partial E_{z}}{\partial \phi} - \mu\omega \frac{\partial H_{z}}{\partial r} \right)\\
H_{r}&= \frac{-i}{q^{2}} \left(\beta \frac{\partial H_{z}}{\partial r} + \frac{\varepsilon\omega}{r} \frac{\partial E_{z}}{\partial \phi} \right)\\
H_{\phi}&= \frac{-i}{q^{2}} \left( \frac{\beta}{r} \frac{\partial H_{z}}{\partial \phi} - \varepsilon\omega \frac{\partial E_{z}}{\partial r} \right)\\
\end{align*}$$
em que $q^{2}=k^{2}-\beta^{2}$. Novamente, vemos que $E_{r},H_{r}$ e $E_{\phi},H_{\phi}$ têm formatos identicos.

- Ao substituir $H_{r},H_{\phi}$ em $\frac{1}{r}(\tfrac{\partial(rH_{\phi})}{\partial r} - \tfrac{\partial H_{r}}{\partial \phi})= i\omega\varepsilon E_{z}$ (equação Ampere) obtemos:
$$\frac{\partial^{2}E_{z}}{\partial r^{2}} + \frac{1}{r} \frac{\partial E_{z}}{\partial r} + \frac{1}{r^{2}}\frac{\partial ^{2}E_{z}}{\partial \phi^{2}} + q^{2}E_{z}=0$$
- Ao substituir $E_{r},E_\phi$ em $\frac{1}{r} (\tfrac{\partial(rE_{\phi})}{\partial r} - \tfrac{\partial E_{r}}{\partial \phi})= -i\omega\mu H_{z}$ (equação Faraday) obtemos:
$$\frac{\partial^{2}H_{z}}{\partial r^{2}} + \frac{1}{r}\frac{\partial H_{z}}{\partial r} + \frac{1}{r^{2}} \frac{\partial^{2}H_{z}}{\partial\phi^{2}} + q^{2}H_{z}=0$$
- Já que $n^{2}k_{0}^{2}E_{z}=(k^{2}-\beta^{2})E_{z}$, vemos que a equação dá-nos *o mesmo que a equação de Helmholtz*, quando forçamos soluções monocromáticas.
- Obtivemos então equações que nos dão $H_{z},E_{z}$ simplesmente a definir a **propagação modal**. Nada dissemos sobre a **geometria!**

#### Geometria cilindrica - fibra
- Como numa fibra temos geometria cilindrica, é preciso que $E_{z},H_{z}$ sejam periódicos em $\phi$, com período $2\pi$.
- Assim, temos que ter uma dependência em $\phi$ do tipo:
$$e^{-i\ell\phi}~~~~;~~ \ell=0,\pm1,\pm2,\dots$$
- Temos então:
$$U=E_{z}=H_{z}=u(r)e^{-i\ell\phi}e^{-i\beta z}$$
- Usando isto, as equações diferenciais de $H_{z},E_{z}$ ficam:
$$\frac{d^{2}u}{dr^{2}} + \frac{1}{r} \frac{du}{dr} + \left(n^{2}(r)k_{0}^{2}- \beta^{2}- \frac{\ell^{2}}{r^{2}} \right)u=0$$
e vemos que os campos apenas têm **dependência radial!!!**

#### Hz e Ez
- Até aqui consideramos estes campos de forma independente e equivalente.
- Na realidade, eles **estão acoplados** devido às condições de fronteira (como já sabiamos - campos elétricos e magnéticos são 2 lados da mesma moeda)
- Temos então 2 modos:
    - **Modos TE** - $E_{z}=0$
    - **Modos TM** - $H_{z}=0$
    - **Modos Híbridos** - $E_{z},H_{z}\neq0$

##### Modos Híbridos
- Dentro deste, temso 2 possíveis:
    - **Modos HE** - $H_{z}$ tem a maior contribuição para o campo
    - **Modos EH** - $E_{z}$ tem a maior contribuição para o campo
- Notemos que num guia planar, um destes campos é sempre nulo. Ou seja, só existe TE e TM

#### Perfil do índice de refração
- Este é o próximo passo.
- Vários estudos feitos em guias mostraram que, para ter modos guiados, temos a condição: $$n_{2}k_{0}\le  \beta \le n_{1}k_{0}$$
- Esta relação pode ser generalizada para fibras e temos:
![[n step index.png]]

- Podemos definir a componente transversal do número de onda:
$$k_{1}^{2}=k_{T}^{2}+\beta^{2}~~\to~~ k_{T}^{2}=k_{1}^{2}-\beta^{2}=n_{1}^{2}k_{0}^{2}-\beta^{2}$$
e definimos $\gamma^{2}=\beta^{2}-n_{2}^{2}k_{0}^{2}$. 
- Se tivermos $n_{2}k_{0}\le \beta<n_{1}k_{0}$ então:
    - $k_{T}$ real ($k_{T}^{2}>0$)
    - $\gamma$ real ($\gamma^{2}\ge0$)

- Assim, a equação diferencial de $u$ pode ser escrita como:
$$\begin{align*}
\frac{d^{2}u}{dr^{2}} + \frac{1}{r} \frac{du}{dr}+ \left(k_{T}^{2}- \frac{\ell^{2}}{r^{2}}\right)u&= 0 \quad \quad;\quad (\text{núcleo})\\
\frac{d^{2}u}{dr^{2}} + \frac{1}{r} \frac{du}{dr}- \left(\gamma^{2}+ \frac{\ell^{2}}{r^{2}}\right)u&= 0 \quad \quad;\quad (\text{bainha})\\
\end{align*}$$
- Ora, as soluções destas equações são *funções de Bessel*:
$$\begin{align*}
u(r)&= A_{n} J_{\ell}(k_{T}r) ~~,~~ r<a \quad \quad(\text{núcleo})\\
u(r)&= A_{b} J_{\ell}(\gamma r) ~~~~~,~~ r\ge a \quad \quad(\text{bainha})
\end{align*}$$
em que $J_{\ell}(x)$ é a função de Bessel de 1ª espécie de ordem $\ell$. $A_{n},A_{b}$ são constantes.

- Quando $x\gg1$ podemos escrever: $$b  $$

**Bessel modificada**
- Definimos então a função de bessel de 2ª espécie ordem $\ell$ **modificada**:
$$x\gg1 ~~~~\to~~~~ K_{\ell}(x)\approx \sqrt{\frac{\pi}{2x}} \left[1+ \frac{4\ell^{2}-1}{8x} \right]e^{-x}$$
- Assim, podemos definir que a amplitude é dada por:
$$\begin{align*}
u(r)&= A_{n} J_{\ell}(k_{T} r)~~~~,~~ r<a\\
u(r)&= A_{b}K_{\ell}(\gamma r)~~~~~~,~~r\ge a
\end{align*}$$
- Por exemplo, temos algo assim:
![[bessel e bessel modificada.png]]

- Notemos que:
    - Quando temos $k_{T}$ maior, temos maior número de oscilações do campo no núcleo
    - Quando temos maior $\gamma$, temos decaimento mais rápido e menos penetração na bainha
    - Temos que $k_{T}^{2}+\beta^{2}=\text{constante}$. Assim, se uma aumenta outra diminui. Ou temos muitas oscilações e alta penetração ou temos um campo muito constante e baixa penetração.
    - Temos ainda que $k_{T}=\sqrt{n_{1}^{2}k_{0}^{2}-\beta^{2}}$. Logo, se $k_{T}$ aumenta então $\beta$ diminui (os raios ficam mais obliquos).

#### Normalização
- Consideremos a definição: $X=k_{T}a~~,~~ Y=\gamma a$. Temos a normalização:
$$\sqrt{X^{2}+Y^{2}}=a \sqrt{n_{1}k_{0}^{2}-\beta^{2}+\beta^{2}-n_{2}^{2}k_{0}^{2}}=ak_{0}\sqrt{n_{1}^{2}-n_{2}^{2}}=\frac{2\pi a}{\lambda_{0}}\text{NA} $$
em que temos $\text{NA}=\sqrt{n_{1}^{2}-n_{2}^{2}}$ 
- Podemos então definir o **parâmtro da fibra V**:
$$V=2\pi \frac{a}{\lambda_{0}}\text{NA} = X^{2}+Y^{2}$$
- Temos que:
$$\begin{cases}
\beta=n_{1}k_{0}~~\to~~ X=0 \\
\beta=n_{2}k_{0}~~\to~~ X=V
\end{cases}$$
ou seja, a condição $n_{2}k_{0}<\beta\le n_{1}k_{0}$ implica que: $X\le V$

- Temos ainda que $n_{1}-n_{2}\ll1$ corresponde ao caso em que temos modos guiados paraxiais.
    - Ou seja, temos $E_{z},H_{z}$ com amplitudes muito menores que $E_{r},E_{\phi},H_{r},H_{\phi}$
    - Temos que o plano de polarização é $\sim \text{xOy}$