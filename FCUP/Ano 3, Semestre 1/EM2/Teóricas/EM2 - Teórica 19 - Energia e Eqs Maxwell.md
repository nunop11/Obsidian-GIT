## Energia
- Para que uma corrente "corra" é preciso gastar alguma energia (aqui estamos a ignorar a energia dissipada por calor ou em resistências). Esta energia consiste no trabalho que é realizado para anular a força eletromotriz negativa que as cargas em movimento geram. Contrariamente à energia dissipada por calor ou em resistências, esta energia *não* é perdida! Ela é recuperada quando a corrente é parada.
- Esta energia pode ainda ser considerada uma "energia latente" que é armazenada no campo magnético.
- O trabalho que temos que realizar em 1 carga ao longo de 1 volta ao circuito para ocorrer corrente será $-\varepsilon$ (o menos apenas indica que o trabalho que realizamos para contrariar a força eletromotriz). Por outro lado, a quantidade de cargas que passam no circuito por unidade de tempo é $I$. Assim, o trabalho realizado nas cargas do circuito por unidade de tempo será
$$\frac{dW}{dt}=-\varepsilon  I=LI \frac{dI}{dt}$$
(em que usamos a equação determinada no final da aula anterior e em que $L$ é a indutância do fio de corrente)

- Podemo integrar esta equação no tempo:
$$W=\int dW=\int_{0}^{I_{f}}LI~dI=\frac{1}{2}LI_{f}^{2}=\frac{1}{2}LI^{2}$$
e vemos que a energia não depende do tempo que demoramos a atingir a corrente final.

- Temos $\Phi=LI$ e $\Phi=\int \vec{B}\cdot \hat{n}ds=\oint \vec{A}\cdot d \vec{\ell}$. Resulta:
$$W=\frac{1}{2}LI^{2}=\frac{1}{2}I \oint \vec{A}\cdot d \vec{\ell}=\frac{1}{2}\oint \vec{A}\cdot (Id \vec{\ell})=\frac{1}{2} \int \vec{A}\cdot \vec{\mathcal{J}}d^{3}r$$
ora, esta $\vec{\mathcal{J}}$ será $\vec{\mathcal{J_{\ell}}}$, a densidade de corrente livre. Ora, $\vec{\mathcal{J_{\ell}}}=\nabla \times \vec{H}$ e fica:
$$W=\frac{1}{2}\int \vec{A}\cdot (\nabla \times \vec{H})d^{3}r$$
usando a relação $\nabla \cdot(\vec{A}\times\vec{H})=\vec{H}\cdot \nabla \times \vec{A}-\vec{A}\times \nabla \times \vec{H}$ obtemos:
$$\begin{align*}
W&=\frac{1}{2}\left[\int (\nabla \times \vec{A})\cdot \vec{H}~d^{3}r - \int \nabla \cdot(\vec{A}\times\vec{H})~d^{3}r\right]\\
&=\frac{1}{2}\left[\int \vec{B}\cdot \vec{H}~d^{3}r - \int \nabla \cdot(\vec{A}\times\vec{H})~d^{3}r\right]\\
\end{align*}$$
ora, no último termo temos $\vec{A}\propto \frac{1}{r^{2}}~,~\vec{H}\propto \frac{1}{r^{3}}$ e $d\vec{s}\propto r^{2}$. Assim, consoante $r$ aumenta este termo desaparece e ficamos com:
$$W=\frac{1}{2}\int \vec{B}\cdot\vec{H}d^{3}r=U_{m}$$
- Para um meio linear, isotrópico e homogéneo temos $\mu_{0}\vec{\mathcal{J_{\ell}}}=\nabla \times \vec{B}$ e a dedução acima resulta em 
$$W=\frac{1}{2\mu_{0}}\int B^{2} ~d^{3}r$$

- Isto é equivalente à equação de eletrostática $U=\frac{\varepsilon_{0}}{2}\int E^{2} ~d^{3}r$ e basicamente podemos interpretar esta energia presente numa corrente elétrica da mesma forma que interpretamos a energia eletrostática.
- Ora, pode parecer estranho gastar energia para criar um campo elétrico quando ele não faz trabalho. Podemos pensar nisto doutra forma: ao criar um campo magnético estamos a variar o campo EM previamente presente. Isso implica alterar um campo elétrico e esse sim realiza trabalho.

# Equações de Maxwell
- O Griffiths faz uma explicação de como eram as equações do EM antes do maxwell as organizar e corrigir a Lei de Ampere (que não continha o termo do campo elétrico)
- Temos portanto as equações de Maxwell:
$$\boxed{\begin{align*}
&(\text{i})&&\nabla \cdot \vec{E}= \frac{\rho}{\varepsilon_{0}} &&&&\text{(Lei de Gauss)}\\
&(\text{ii})&&\nabla \cdot \vec{B}= 0 &&&&\text{(Sem Nome)}\\
&(\text{iii})&&\nabla \times \vec{E}= - \frac{\partial\vec{B}}{\partial t} &&&&\text{(Lei de Faraday)}\\
&(\text{iv})&&\nabla \times \vec{B}= \mu_{0}\vec{\mathcal{J}} + \varepsilon_{0}\mu_{0} \frac{\partial\vec{E}}{\partial t} &&&&\text{(Lei de Ampere-Maxwell)}
\end{align*}}$$
- Juntamente com a equação de Força de Lorentz:
$$\vec{F}=q(\vec{E}+\vec{v}\times\vec{B})$$
conseguimos resumir toda a física da eletrodinâmica em 5 equações (à exceção de casos com polarização e magnetização)
- Até a equação da continuidade pode ser deduzida usando estas 5:
$$\nabla \cdot \vec{\mathcal{J}}=- \frac{\partial\rho}{\partial t}$$

## Carga magnética
- As densidades de carga e corrente presentes nas equações de Maxwell são as densidades de carga e corrente *elétrica* $\rho_{e},\vec{\mathcal{J_{e}}}$  
- Consideremos, hipoteticamente, que existem cargas e correntes magnéticas, com densidades $\rho_{m},\vec{\mathcal{J_{m}}}$ (não confundir com densidade de corrente de magnetização)
- Tendo em conta a simetria das equações de Maxwell, parece seguro asusmir que neste cenário as equações de Maxwell teriam a forma:
$$\begin{align*}
\nabla \cdot \vec{E}&= \frac{\rho_{e}}{\varepsilon_{0}} &&; &&\nabla \times \vec{E}= -\mu_{0} \vec{\mathcal{J_{m}}}- \frac{\partial \vec{B}}{\partial t}\\
\nabla \cdot \vec{B}&= \mu_{0}\rho_{e} &&; && \nabla \times \vec{B}=\mu_{e} \vec{\mathcal{J_{e}}} + \mu_{0}\varepsilon_{0} \frac{\partial \vec{E}}{\partial t}
\end{align*}$$
e teríamos uma completa e muito satisfatória simetria entre as equações.

- Infelizmente isto simplesmente não é o caso. Pelo que sabemos até ao presente, *não existe carga magnética* e temos $\rho_{m}=0,\vec{\mathcal{J_{m}}}=\vec{0}$ em todo o espaço.

## Equações de Maxwell na Matéria
- Quando temos campos em materiais que passam por magnetização e polarização as equações de Maxwell que vimos acima não são as mais convenientes.

- Vimos na eletrostática que a polarização e a densidade volúmica de carga de polarização se relacionam assim:
$$\nabla \cdot \vec{P}=-\rho_{p}$$
e na magnetostática vimos que analogamente para a magnetização temos:
$$\nabla \times \vec{M}=\vec{\mathcal{J_{m}}}$$
- Ora, no caso da eletrodinâmica temos que considerar algo. Quando se varia o campo elétrico / polarização de um material, surge uma *corrente de polarização*, de densidade $\vec{\mathcal{J_{p}}}$. Temos que:
$$\vec{\mathcal{J_{p}}}= \frac{\partial \vec{P}}{\partial t}$$
- Não entendi muito bem a dedução do Griffiths. No entanto, podemos demonstrar isto. Vamos determinar o fluxo do vetor densidade de corrente:
$$\oint \vec{\mathcal{J_{p}}}\cdot d \vec{s}=\oint \frac{\partial \vec{P}}{\partial t}\cdot d \vec{s}=\frac{d}{dt}\int \vec{P}\cdot d \vec{s}=\frac{d}{dt}\int \nabla \cdot \vec{P}~d^{3}r=\frac{-d}{dt}\int \rho_{p}~d^{3}r=- \frac{dQ_{p}}{dt}$$
o que está correto.

- De notar que $\vec{\mathcal{J_{m}}}\neq \vec{\mathcal{J_{p}}}$. A densidade de carga de magnetização é gerada pelos eletrões a girar em torno do átomo e os seus spins. A densidade de polarização deve-se aos átomos se moverem quando um campo elétrico externo é aplicado.

- Assim podemos escrever a densidade de carga total num material:
$$\begin{align*}
\rho&= \rho_{\ell} +\rho_{p}\\
&= \rho_{\ell}- \nabla \cdot \vec{P}
\end{align*}$$
pelo que a lei de Gauss fica:
$$\nabla \cdot \vec{E}=\frac{1}{\varepsilon_{0}}(\rho_{\ell}-\nabla \cdot \vec{P})$$
que, no caso de um material dielétrico ($\vec{D}=\varepsilon_{0}\vec{E}+\vec{P}$) fica:
$$\nabla \cdot \vec{D}=\rho_{\ell}$$

- Podemos ainda escrever a densidade total de corrente:
$$\begin{align*}
\vec{\mathcal{J}}&= \vec{\mathcal{J_{\ell}}}+ \vec{\mathcal{J_{m}}} + \vec{\mathcal{J_{p}}}\\
&= \vec{\mathcal{J_{m}}} + \nabla \times \vec{M} + \frac{\partial \vec{P}}{\partial t}
\end{align*}$$
e a Lei de Ampere-Maxwell fica 
$$\nabla \times \vec{B}=\mu_{0} \left(\vec{\mathcal{J_{m}}} + \nabla \times \vec{M} + \frac{\partial \vec{P}}{\partial t} \right)+\mu_{0}\varepsilon_{0} \frac{\partial\vec{E}}{\partial t}$$
que, num meio com magnetização ($\vec{H}=\frac{1}{\mu_{0}}\vec{B}-\vec{M}$) fica:
$$\nabla \times \vec{H}=\vec{\mathcal{J_{\ell}}}+ \frac{\partial \vec{D}}{\partial t}$$
e temos as 4 equações de Maxwell na matéria:
$$\boxed{\begin{align*}
&(\text{i}) && \nabla \cdot \vec{D}=\rho_f\\
&(\text{ii}) && \nabla \cdot \vec{B}=0\\
&(\text{iii}) && \nabla \times \vec{E}=- \frac{\partial \vec{B}}{\partial t}\\
&(\text{iv}) && \nabla \times \vec{H}=\vec{\mathcal{J_{\ell}}}+ \frac{\partial \vec{D}}{\partial t}
\end{align*}}$$
estas apenas consistem nas equações de Maxwell, com a carga livre e carga polarizada/de magnetização separadas.
- Claro, nestas equações temos $\vec{E},\vec{D}$ e $\vec{B},\vec{H}$ e torna-se importante poder relacioná-los diretamente. Por exemplo, no caso de um material com polarização e magnetização lineares temos:
$$\vec{P}=\varepsilon_{0}\chi_{e}\vec{E}~~~~\longrightarrow~~~~ \vec{D}=\varepsilon \vec{E}$$
$$\vec{M}=\chi_{m}\vec{H}~~~~\longrightarrow~~~~ \vec{H}=\frac{1}{\mu}\vec{B}$$
- Porque $\vec{D}$ é o deslocamento elétrico, ao último termo da Lei de Faraday chamamos **corrente de deslocamento**:
$$\vec{\mathcal{J_{d}}}=\frac{\partial \vec{D}}{\partial t}$$

### Descontinuidades de $\vec{E},\vec{B},\vec{D},\vec{H}$
- Estes 4 campos serão em geral descontinuos no interface entre 2 meios diferentes ou numa superfície com densidade de carga $\sigma$ ou corrente superfícial $\vec{\kappa}$.
- Mostremos isso:
![[Pasted image 20231128180606.png]]
- Temos:
$$\nabla \cdot \vec{D}=\rho_{\ell}\to \oint \vec{D}\cdot d\vec{s}=Q_{\ell}$$
o que nos dá
$$(\vec{D^{+}}-\vec{D^{-}})\cdot \hat{n}=\sigma_{\ell}~~\to~~ D_{\perp}^{+}-D_{\perp}^{-}=\sigma_{\ell}$$
- Temos ainda que
$$\nabla \times \vec{H}=\vec{\mathcal{J_{\ell}}}+\frac{\partial \vec{D}}{\partial t}\longrightarrow \begin{align*}
\int \nabla \times \vec{H} \cdot d \vec{s}&= \int \vec{\mathcal{J_{\ell}}}\cdot d \vec{s} + \frac{d}{dt}\int \vec{D}\cdot d \vec{s}\\
\int \vec{H}\cdot d \vec{\ell}&= I_{\ell} + \frac{d}{dt}\int \vec{D}\cdot d \vec{s}
\end{align*}$$
considerando o integral de linha da figura da esquerda fica:
$$(\vec{H^{+}}-\vec{H^{-}})\times \hat{n}=\vec{\kappa_{e}} ~~\to~~ \vec{H}_{\parallel}^{+}-\vec{H}_{\parallel}^{-}=\vec{\kappa_{e}}\times \hat{n}$$

- E temos de aulas anteriores que:
$$\vec{E}_{\parallel}^{+}-\vec{E}_{\parallel}^{-}=\vec{0}$$
$$B_{\perp}^{+}-B_{\perp}^{-}=0$$