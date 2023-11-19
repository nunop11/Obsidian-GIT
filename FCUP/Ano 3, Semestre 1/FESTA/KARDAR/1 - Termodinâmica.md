> ==**_NOTA_**==
> Sempre que tiver um diferencial não exato devia usar algo tipo $dQ$ com uma linha através da haste do "d" (tipo $\hbar$) mas não arranjei uma forma prática de fazer isso no obsidian. Portanto, daqui em diante usarei $d$ caligráficos:$$\mathscr{d}$$. Por exemplo: $\hbar\to \mathscr{h}$

## 1.1 - Intro
**Termodinâmica** - descrição fenomonológica de propriedades de sistemas macroscópicos em equilíbrio.

## 1.2 - Lei Zero
" Se 2 sistemas A e B estão ambos em equilíbrio com um terceiro sistema, C, então em equilíbrio um com o outro"
- Podemos representar isto:
![[lei 0 termodinamica.png]]

- Esta lei implica a existência de uma função de estado *temperatura* $\Theta$, sendo que 2 sistemas em equilíbrio estão à mesma temperatura.
- Consideremos que os estados de equilíbrio de $A,B,C$ são descritos pelas coordenadas $\{A_{1},A_{2},\dots\},\{B_{1},B_{2},\dots\},\{C_{1},C_{2},\dots\}$.

- Ora, se $A$ está em equilíbrio com $C$, temos que ter uma relação entre as coordendas de $A,C$. Ou seja, se $A_{1}$ mudar, todas as outras coordenadas de $A$ e as coordenadas de $C$ terão que mudar para que se mantenha o equilíbrio. Podemos escrever isto como:
$$f_{AC}(A_{1},A_{2},\dots;C_{1},C_{2}\dots)=0$$
análogamente, para $B$ e $C$ temos:
$$f_{BC}(B_{1},B_{2},\dots;C_{1},C_{2}\dots)=0$$

- Podemos então isolar 1 coordenada, ou seja, ver como é que ela irá variar ao variar todos os outros parâmetros. Ou seja, por exemplo para a coordenada $C_1$:
$$\begin{align*}
C_{1}=F_{AC}(A_{1},A_{2},\dots;C_{2},\dots)\\
C_{1}=F_{BC}(B_{1},B_{2},\dots;C_{2},\dots)
\end{align*}$$
- Assim, se $C$ está em equilíbrio com $A$ e $B$ temos:
$$F_{AC}(A_{1},A_{2},\dots;C_{2},\dots)=F_{BC}(B_{1},B_{2},\dots;C_{2},\dots)\tag1$$
e pela lei zero temos:
$$f_{AB}(A_{1},A_{2},\dots;B_{1},B_{2},\dots)=0\tag2$$

- Podemos então escolher quaisquer 2 parâmetros $\{A,B\}$ que satisfaçam a equação 1 e deverão satisfazer a 2. Assim, $C$ torna-se irrelevante e podemos definir o equilíbrio entre $A$ e $B$ como:
$$\Theta_{A}(A_{1},A_{2},\dots)=\Theta_{B}(B_{1},B_{2},\dots)$$
ou seja, o equilíbrio entre 2 parâmetros é caraterizado por uma função termodinâmica, que relaciona/"controla" os parâmetros de cada um dos sistemas em equilíbrio.

- Ora, a função $\Theta$ pode ser comparada à força num sistema mecânico, no sentido que estes apenas entram em equilíbrio quando as forças aplicadas por um corpo no outro se anulam.

> **EXEMPLO**
> - Temos 3 sistemas:
>     - A) Fio com comprimento $L$ sujeito a tensão $F$
>     - B) Material com magnetização $M$ em campo magnético $B$
>     - C) Gás de volume $V$ a pressão $P$
> - Ora, temos então as combinações A+C e B+C:
>   ![[Pasted image 20231113210623.png]]
>   - Da experiência verifica-se que quando estes 2 sistemas estão em equilíbrio temos: $$\begin{align*}
\left(P+\frac{a}{V^{2}}\right)(V_b)(L-L_{0})-c(F-K(L-L_{0}))&= 0\\ \left(P+ \frac{a}{V^{2}}\right)(V-b)M-dB=0
\end{align*}$$o que implica $$\Theta\propto \left(P + \frac{a}{V^{2}}\right)(V-b)=c \left(\frac{F}{L-L_{0}}-K \right)=d \frac{B}{M}$$
> Ora, nestes sistemas temos 3 leis conhecidas, todas dependentes da temperatura $T$: $$\begin{cases}
\left(P +\frac{a}{V^{2}} \right)(V-b)=Nk_{B}T  &  & (\textsf{Gás de Van der Waals}) \\
M = \frac{N \mu_{B}^{2}B}{3 k_{B}T}  &  & (\textsf{Paramagnet de Curie}) \\
F = \frac{K+DT}{L-L_{0}}  &  & \textsf{(Lei de Hooke)}
\end{cases}$$

## 1.3 - A Primeira Lei
"O trabalho necessário realizar para mudar o estado de um sistema isolado depende apenas dos estados final e inicial e não dos passos intermédios."

- Num sistema mecânico em que temos uma partícula sujeita a um potencial (normalmente gravítico), o trabalho necessário para mover a partícula entre 2 posições permite-nos estudar/determinar a energia potencial no sistema.
![[Pasted image 20231113220445.png]]
- Analogamente, num sistema termodinâmico temos a energia interna $E(\vec{X})$, que pode ser determinada a menos de 1 constante através do trabalho necessário para transitar o sistema de um estado $\vec{X_{i}}$ para um estado $\vec{X_{f}}$ através d euma transformação adiabática: $$\Delta W= E(\vec{X_{f}})-E(\vec{X_{i}})$$
- Se, por outro lado, o sistema não for adiabático já não temos esta igualdade. Passa a haver uma diferença: $\Delta Q=\Delta E-\Delta W$, que é a *troca de calor* do sistema com a vizinhança. Assim, é evidente que $\Delta W,\Delta Q$ dependem de fatores externos AKA não são funções de estado. Assim, escrevemos:
$$\mathscr{d}Q=dE-\mathscr{d}W$$
- Assim, pela 1ª lei da termodinâmica, para mudar o estado é preciso que se forneça energia ao sistema, quer na forma de calor como trabalho; desde que a energia se mantenha constante.

- Frequentemente consideraremos transformações *quase-estáticas*, ou seja, transformações tão lentas que podemos considerar que o sistema está em equilibrio em todos os instantes. Desta forma, as coordenadas termodinâmicas estão sempre definidas e podem ser calculadas. 
    - Isto é equivalente a esticar uma mola de comprimento $L$ muito muito lentamente, conseguimos estudar a relação $E_{p}(L)$, sendo que a variação da energia potencial será $\int F dL$. Isto ocorre porque as forças anulam-se sempre e não perdemos energia potencial na forma de energia cinética.

- Tendo uma  função de estado $\{\vec{X}\}$ podemos dividi-la em *deslocamentos generalizados* $\{\vec{x}\}$ e as suas *forças generalizadas conjugadas* $\{\vec{J}\}$ e podemos escrever:
$$\mathscr{d}W=\sum\limits_{i}J_{i}dx_{i}$$
ou seja, para cada deslocamento temos uma força correspondente: força tensão gera deslocamento de comprimento, tensão superficial desloca área, pressão desloca volume, etc.
- Os deslocamentos são normalmente variáveis *extensivas* (dependem do tamanho do sistema) e as forças *intensivas* (independentes do tamanho). (Pensar em pressão (força) e volume (deslocamento))

### Temperatura
- Vejamos alguns aspetos ligados à 1ª Lei e à temperatura.

#### Gás Ideal
- Determinou-se de forma empirica que para um gás ideal $PV\propto T$. Vejamos como será a energia interna de um gás ideal
![[Pasted image 20231113224418.png]]
- Temos acima a **Experiência da Expansão Livre de Joule**, em que um gás ideal se expanse de forma adiabática de um volume $V_{i}$ para outro, $V_{f}$. Joule verificou que a temperatura não varia: $T_{i}=T_{f}$. 
- Ora, como a transformação é adiabática, temos $\Delta Q=0$
- Parte da experiência é que não se exerce qualquer força externa, logo $\Delta W=0$
- Ou seja, pela 1ª Lei é obrigatório que $\Delta E=0$
- Ora, se $V,P$ ambos variam nesta transformação, então a energia não pode depender deles. Temos então $E=E(T)$

#### Calor Específico
- Obtidos através da mudança de temperatura consoante se fornece calor ao sistema. Como Calor não é função de estado, o "percurso" importa!
- Para um gás podemos determinar calor específico a volume e pressão constante:
$$\begin{align*}
C_{V}&= \frac{\mathscr{d}Q}{dQ}\Biggr|_{V}=\frac{dE-\mathscr{d}W}{dT}\Biggr|_{V}=\frac{dE+PdV}{dT}\Biggr|_{V}=\frac{\partial E}{\partial T}\Biggr|_{V}\\
C_{P}&= \frac{\mathscr{d}Q}{dT}\Biggr|_{P} = \frac{dE-\mathscr{d}W}{dT}\Biggr|_{P}=\frac{dE+PdV}{dT}\Biggr|_{P}=\frac{\partial E}{\partial T}\Biggr|_{P}+P \frac{\partial V}{\partial T}\Biggr|_{P}
\end{align*}$$

#### Constantes de Força
- Rácios Infinitesimais que medem os deslocamentos da força. 
- Exemplos:
    - Compressibilidade isotérmica $\kappa_{T}=- (\frac{\partial V}{\partial P}|_{T})/V$ 
    - Suscetibilidade de um íman $\chi_{T}=\frac{\partial M}{\partial B}|_{T}/V$

## 1.4 - A Segunda Lei