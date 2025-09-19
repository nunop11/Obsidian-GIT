###### Aula 4 - 29/2/2024
## Resultados da aula anterior
- Vimos que
$$\begin{align*}
\varepsilon(\omega)&= 1+i \frac{\sigma(0)}{\omega\varepsilon_{0}(1-i\omega\tau)}\\
&= \underbrace{1- \frac{ne^{2}\tau}{m\omega\varepsilon_{0}}\frac{\omega\tau}{1+\omega^{2}\tau^{2}}}_{\varepsilon'}+ \underbrace{i \frac{ne^{2}\tau}{m\omega\varepsilon_{0}}\frac{1}{1+\omega^{2} \tau^{2}}}_{\varepsilon''}\\
&= \varepsilon'+i\varepsilon''
\end{align*}$$

- Vimos que para $\omega\tau\to0$ temos $\varepsilon(\omega)\simeq i\frac{\omega(0)}{\omega\varepsilon_{0}}$
- Vimos que para $\omega\tau\gg1$ temos $\varepsilon(\omega)\sim1-\frac{\omega_{p}^{2}}{\omega^{2}}$
    - Isto signifca que para um certo $\omega$ temos $\varepsilon=0$, para valores menores negativos, para valores superiores positivos
    - Temos a equação de Helmholtz: $\nabla^{2}\vec{E}=\frac{\omega^{2}}{c^{2}}[1+i \frac{\sigma(\omega)}{\omega\varepsilon_{0}}]\vec{E}$
    - Que nos dá: $k^{2}c^{2}=\omega^{2}-\omega_{p}^{2}$ 

**Metais transparentes**
- A equação acima indica que para $\omega>\omega_{p}$ o material é *transparente*. Na prática isto significa que temos muito pouca reflexão, ou seja, a luz atravessa o metal: da mesma forma que luz visível atravessa vidro e vemos através dele.

## Experimentalmente
![[plasma exp]]
($\Gamma=1/\tau$)
- Vimos ainda $n,k$ em função de $\omega$. Depois vimos dados experimentais e concluímos que Drude descreve bem ouro e prata
- Drude prevê que refletância evolua assim:
![[Drude refletâncias]]
experimentalmente vimos que Prata segue direitinho este gráfico ($\sim1$ para frequências baixas, chega a 0 em $\omega=\omega_{p}$, $\mathcal{R}$ muito baixo para frequências altas). Para o ouro falha a partir de $\omega_{p}(\text{Au})$ , em que não chegamos a zero. Para o alumínio falha quase por completo, o que se deve ao comportamento por níveis eletrónicos deste metal, que Drude não considera.
- De notar que num gráfico experimental mostrado em aula em que temos $\mathcal{R}(E)$, o alumínio torna-se transparente para energias de $\sim22\text{eV}$. Isto é interessante, porque a água é opáca para frequências infra-vermelhas. Ou seja, se vissemos em IF não conseguiríamos ver através de água.

## Condução Térmica de Metal
- Um grande sucesso do modelo de Drude foi explicar a relação empirica $\kappa/\sigma\propto T$
- O modelo baseia-se, em parte, na ideia que "qualquer bom condutor elétrico será bom condutor térmico". Isto nem sempre é verdade.

- Temos uma barra de metal ao longo da direção dos xx. Introduzimos um gradiente de temperatura $\nabla T$ (constante no tempo) entre as extremidades. Se este gradiente não for muito grande, podemos dizer que temos uma relação linear entre a densidade de transporte de calor e o próprio gradiente (Lei de Fourier):
$$\vec{j}_{q}=-\kappa\nabla T$$
consideremos que o gradiente apenas causa efeitos na direção xx:
$$\vec{j_{x}}=-\kappa \frac{dT}{dx}$$
($\kappa$ é o coeficiente de condução térmica)

- Conforme a figura acima temos $x'=x-v\tau~,~x''=x+v\tau$
- Consideremos o gradiente de temperatura definido tal que $T(x')<T(x'')$
- Ou seja, *macroscopicamente* deverá ocorrer transporte de calor da direita para a esquerda (mas não transporte de eletrões!)
- Para um sistema em equilíbrio térmico consideramos que a energia que um eletrão tem após uma colisão depende da *temperatura*! Assim, aproximando cada posição xx a equilíbrio térmico, temos que os eletrões em $x''$ terão mais energia cinética do que aqueles em $x'$.
- Podemos então dizer:
$$\varepsilon(x'')=\varepsilon(x+v\tau)=\varepsilon(T(x+v\tau)) \quad;\quad \varepsilon(x')=\varepsilon(T(x-v\tau))$$
(ou seja, a energia nestas posições depende diretamente da temperatura)
- Sendo $x-x'=x''-x\simeq\ell$ podemos dizer que a energia com que um eletrão sai de $x'$ após colidir aí será a mesma com que ele chega a $x$.
- Ou seja, considerando que em $x'$ metade dos eletrões colide e vai para a esquerda e a outra metade para a esquerda, temos que deste ponto chega a $x$ uma energia $\frac{n}{2}v\varepsilon(T(x-v\tau))$. Usando a mesma lógica, de $x''$ saem eletrões para a esquerda que chegam a $x$ com uma energia total $\frac{n}{2}(-v)\varepsilon(T(x+v\tau))$
    - Aqui é importante realçar que não há corrente macroscópica: há tantos eletrões a passar em $x$ a ir $(\leftarrow)$ como a ir $(\rightarrow)$.
    - A velocidade média $v$ depende da temperatura. Mas aqui simplesmente dizemos que a dependência do sistema na temperatura está melhor reprensentado no $\varepsilon(\dots)$ do que no $v$, daí não considerarmos.
- Assim, teremos um fluxo de energia:
$$\vec{j}_{q}=\frac{n}{2}v[\varepsilon(T(x-v\tau))-\varepsilon(T(x+v\tau))]$$
- Temos a seguinte série de Taylor: $f(x + h) = f(x) + f′(x)h + f′′(x) \frac{h_{2}}{2!} +\dots$
    - Facilmente vemos que isto resulta em: $T(x\pm v\tau)=T(x)\pm v\tau\frac{dT}{dx}(x)$
    - Consequentemente: $\varepsilon(T(x\pm v\tau))=\varepsilon(T(x)\pm v\tau T'(x))=\varepsilon(T(x))\pm v\tau\frac{d\varepsilon}{dT}\left(\frac{dT}{dx}\right)$
- Logo: $$\begin{align*}
\vec{j}_{q}&= \frac{n}{2}v \left[\cancel{\varepsilon(T(x))}- v\tau\frac{d\varepsilon}{dT}\left(\frac{dT}{dx}\right) - \cancel{\varepsilon(T(x))}- v\tau\frac{d\varepsilon}{dT}\left(\frac{dT}{dx}\right) \right]\\
&= n v^{2} \tau \frac{d\varepsilon}{dT}\left(- \frac{dT}{dx}\right)
\end{align*}$$
(só não sei quão correto foi passar aquele menos para dentro dos parentesis mas bate certo com a equação da aula)
- E temos então:
$$\vec{j}_{q}=nv_{x}^{2}\tau\frac{d\varepsilon}{dT}\left(-\frac{dT}{dx}\right)$$
- Sabemos que temos $\langle v_{x}^{2}\rangle=\langle v_{y}^{2}\rangle=\langle v_{z}^{2}\rangle=\frac{1}{3}v^{2}$ logo: $\vec{j}_{q}=nv_{x}^{2}\tau\frac{d\varepsilon}{dT}\left(-\frac{dT}{dx}\right)$
- Sabemos ainda que o calor específico é dado por $$C_{V}=\left(\frac{\partial E}{\partial T}\right)_{V}~~\to~~ C_{V}=\left(\frac{\partial(N\varepsilon)}{\partial T}\right)_{V}~~\to~~c_{V}=\frac{C_{V}}{V}=n \frac{\partial\varepsilon}{\partial T}$$
e obtemos
$$\vec{j}_{q}=\frac{1}{3}v^{2}\tau c_{V} (-\nabla T)$$
pelo que, como $\vec{j}_{q}=-\kappa\nabla T$ determinamos que:
$$k=\frac{1}{3}v^{2}\tau c_{V}$$

**Clássico**
- Da física clássica temos $$c_{V}=\frac{3}{2}nk_{B}$$
- Temos, do teorema de equipartição:
$$\frac{1}{2}mv^{2}=\frac{3}{2}k_{B}T~~\to~~ v^{2}=\frac{3k_{B}}{m}T$$

**VS Experimental**
- Como já dito, na realidade verifica-se que $$\frac{k}{\sigma}\propto T$$
- Para justificar isto, Drude "espetou" as equações clássicas de $c_{V},v^{2}$ que temos acima na equação de $k$ e obteve:
$$\frac{k}{\sigma}=\frac{3}{2} \left(\frac{k_{B}}{e}\right)^{2}T~~~~\to~~~~ \frac{k}{\sigma T}=1,11\cdot10^{-8} \text{W$\Omega$/K$^{2}$}$$
o que é cerca de metade do valor tabelado para vários materiais.

**Conclusão**
- Isto parece bater certo com a realidade. Mas não. Não bate.
- O modelo de Drude falha redondamente no que toca a comportamento térmico. O facto que bateu certo foi "sorte de principiante" (Agostinho, 29/2/2024)
- O resultado obtido apenas se aplica a casos muito específicos.
- A falha deste modelo devem-se ao facto que os eletrões não transportam calor!! Quem faz isso são as oscilações dos iões da grelha. 

## Efeito Termoelétrico
- Temos efeito Peltier e Seebeck:
    - *Peltier* - Quando se aplica corrente em 2 metais/semicondutores distintos e se gera um gradiente de temperatura. Útil para fazer transfereências de calor a pequena escala.
    - *Seebeck* - Quando um gradiente de temperatura entre 2 metais gera uma diferença de potencial entre estes -- efeito responsável pelo funcionamento do termopar!

- Iremos estudar melhor o Seebeck.
- Neste efeito temos a relação: $$\vec{E}=Q\nabla T$$
- Ou seja, temos uma DDP que gera um campo elétrico. Assim teremos *transporte de carga*. Por outro lado, sendo isto um caso de efeito termoelétrico, teremos um gradiente de temperatura e, portanto, uma velocidade de *condução térmica* por este:
    - Podemos definir a velocidade de condução térmica como $v_Q$ (usamos a mesma lógica que acima): $v_{Q}=\frac{1}{2}[v(x-v\tau)-v(x+v\tau)]\simeq - v\tau \frac{dv}{dx}= -\tau \frac{d}{dx}\left(\frac{v^{2}}{2}\right)=$
    - Sendo $\langle v_{x}^{2}\rangle=\frac{1}{3}v^{2}$ podemos passar para 3D: $v_{Q}=- \frac{\tau}{6} \frac{dv^{2}}{dT}\nabla T$
    - A velocidade de transporte de carga devido ao campo elétrico será: $v_{E}=- \frac{e\tau}{m}\vec{E}$

- No equilíbrio, teremos que a velocidade de condução térmica e a velocidade de transporte de carga são iguais: 
$$\begin{align*}
\vec{v_{Q}}+\vec{v}_{cond}&= \vec{0}\\
-\tau \frac{d}{dT}\frac{v^{2}}{6}\nabla T - \frac{e\tau}{m}\vec{E} &= \vec{0}\\
\vec{E}&= \frac{1}{3e} \frac{d}{dT}\left[\underbrace{\frac{1}{2}mv^{2}}_\varepsilon \right]\nabla T\\
\vec{E}&= \frac{c_{V}}{3ne}\nabla T
\end{align*}$$
ou seja temos o coeficiente eletrotérmico (em que $c_{V}=\frac{3}{2}nk_{B}$):
$$Q=- \frac{k_{B}}{2e}$$

**Conclusão**
- Aqui, o modelo de Drude merece mérito por admitir a existência deste fenómeno.
- De resto, o modelo falha muito: para uns metais falha na ordem de grandeza de $Q$, para outros só não descreve a realidade.
- Esta e as outras falhas devem-se ao facto que o Modelo de Drude apoia-se em suposições que **não são verdade**.

# 2 - Modelo de Sommerfield
- AKA free electron model.
- Consiste em assumir que todos os eletrões são livres. 
    - Em Drude tínhamos uma rede de iões que causavam colisões e consequentemente scattering dos eletrões. 
    - Em sommerfield não temos nenhum mecanismo de scattering. Temos apenas o *princípio de exclusão* e os eletrões contidos num certo volume.
- Comecemos por recordar que o Hamiltoniano de uma "caixa vazia"  é $H=\frac{-\hbar^{2}}{2m}\nabla^{2}+V_{0}$
- Fazendo uma restruturação das energias podemos ficar com $H=\frac{-\hbar^{2}}{2m}\nabla^{2}$
- Ao obter as soluções estacionárias do Hamiltoniano (resolver ESIT) obtemos: $$\psi(\vec{r})=A e^{i \vec{k}\cdot\vec{r}} \quad \quad;\quad \quad \varepsilon(\vec{k})=\frac{\hbar^{2}k^{2}}{2m}$$
- Em MQ1 e Física Moderna as condições de fronteira que definimos para um poço infinito são: a função de onda e a sua 1ª derivada são nulas na fronteira. Isto faz com que todas as soluções que obtemos representam *ondas estacionárias*. 
- Este tipo de soluções não são os mais adequados para descrever um metal: teremos condições de fronteira **_cíclicas_**.
    - Para poço infinito 1D com extremos em $x=0,x=L$ teremos a condição de fronteira $\psi(0)=\psi(L)$ (contrariamente a $\psi(0)=\psi(L)=0$). Isto significa que podemos repetir a onda consecutivamente e temos um traçado contínuo, sem estar a "prender" a partícula demasiado.
    - O significado físico destas condições é debatido mas a conclusão é "funciona".