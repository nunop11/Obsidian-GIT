## Modelo Lorentz (finalização)
### Ressonânicas em diferentes frequências
![[refracao vs freq imagem fixe.png]]
- Vemos que existem 3 ressonâncias, em que temos uma queda abrupta de $n$
- Para frequências acima das represetandas não temos ressonância. Isto porque a partir de certo ponto temos frequências tão altas que nada consegue vibrar em sintonia com a radiação, pelo que não existem mais ressonâncias

**Cor de objetos**
![[percepção de cor.png]]
- Consideremos um objeto (rosa) iluminado por luz branca.
- Ora, nós vemos a rosa como vermelha. Ou seja, a radiação da luz excita os eletrões dos átomos da rosa de forma que as vibrações com frequência $\sim7\cdot10^{14}\text{Hz}$ (luz vermelha) são as predominantes

## Espalhamento da luz
### Enquadramento
![[scattering luz.png|174]]
- Nome dado a quando a luz se propaga de um meio homogéneo para outro meio homogéneo e a sua direção muda: _Lei de Snell_ $$n_{1}\sin\theta_{1} = n_{2}\sin\theta_{2}$$
- Mas se o meio *não* for homogéne, a trajetória da luz será **CURVA**, pelo que fará um percurso que segue as regiões de maior densidade / índice de refração

**Ondas secundárias**
- Ora, quando uma onda EM incide no material, induz dipolos oscilantes na superfície de impacto.
- Como os dipolos oscilantes consistem de 2 cargas a oscilar, emitem *ondas EM secundárias*. Estas ondas são emitidas em todas as direções.
- Ora, estas ondas apenas nos dão interferência *construtiva* na direção da lei refratada de Snell!

### Espalhamento
- Temos a lei de snell:
![[refracao snell.png]]
$$n_{1}\sin i=n_{2}\sin r$$
- Mas e se houverem flutuações do índidce de refração em torno de um valor médio? 
- Neste caso ocorre espalhamento! Como podemos ver na imagem abaixo, ficamos com luz onde não deveríamso ter luz:
![[scattering de luz.png]]

- Ocorre devido a existência no meio de:
    - não homogeneidades localizadas
    - irregularidades
    - defeitos
    - partículas em suspensão
- Isto pode ser estudado com as equações de Maxwell. No entanto, soluções analíticas apenas são achadas para casos muito particulares

#### Espalhamento de pequenas amplitudes
- Este caso pode mas facilmente ser estudado, usando aproximações
- Uma dela é a *aproximação de Born*. Nesta, assumimos que a fonte do espalhamento pode ser modelada como sendo uma pequena perturbação na **permitividade**
- Consideremos a luz espalhada como sendo representada pela amplitude complexa $U(\vec{r})$ que cumpre a eq Helmholtz
    - Dentro do espaço em que há espalhamento temos $k(\vec{r})=k_{s}(\vec{r})$
    - No meio homogéneo envolvente temos $k(\vec{r})=k$

- Temos então:
$$\nabla^{2}U(\vec{r}) + k_{s}^{2}(\vec{r})U(\vec{r})=0$$
- Podemos dizer, claro, que:
$$\begin{align*}
\nabla^{2}U(\vec{r}) + k_{s}^{2}(\vec{r})U(\vec{r})&= 0\\
\nabla^{2}U(\vec{r}) + (k^{2}+k_{s}^{2}-k^{2})(\vec{r})U(\vec{r})&= 0\\
\nabla^{2}U(\vec{r}) + k^{2}U(\vec{r})&= - S(\vec{r})
\end{align*}$$
em que $S(\vec{r})=(k_{s}(\vec{r}-k^{2}))U(\vec{r})$ é a *fonte* do espalhamento, que está restrita ao volume onde há espalhamento (sendo zero no restante espaço).

- Uma das soluções possíveis para isto é:
$$U(\vec{r})=\iiint_{V} S(\vec{r'}) \frac{e^{-ik |\vec{r}-\vec{r'}|}}{4\pi |\vec{r}-\vec{r'}|}d\vec{r'}$$
- Mas isto **é circular!** Ou seja, temos uma equação para determinar $U(\vec{r})$, mas ela inclui $S(\vec{r})$ que *depende de* $U(\vec{r})$

##### Aproximação de Bohr
- Surge então a aproximação de Bohr, que permite resolver este problema circular
- Temos:
    - Consideramos $S(\vec{r})$ como sendo a fonte de espalhamento
    - Quanto mais forte for a onda incidente, mais forte será o espalhamento, logo definimos que a fonte depende de $U_{0}(\vec{r})$ : intensidade da onda incidente.
    - Ou seja: $$S(\vec{r})\approx (k_{s}^{2}(\vec{r})-k^{2})U_{0}(\vec{r})$$
- Removemos então o argumento circular
- Assim, podemos ver que $U=\int_{V}S(\vec{r'})\frac{e^{-ik|\vec{r'}-\vec{r}|}}{4\pi |\vec{r'}-\vec{r}|}d\vec{r'}$ não passa de uma combinação/sobreposição de ondas esféricas geradas por uma série de fontes pontuais no volume de espalhamento.
    - Ora, cada uma dessas ondas esféricas terá amplitude $S(\vec{r'})\simeq [k_{s}^{2}(\vec{r})-k^{2}]U_{0}(\vec{r'})$

##### Quando é válido?
- Ora, esta aproximação é válida quando temos espalhamento de fraca intensidade (como referido, imaginamos o fenómeno como sendo uma perturbação de propriedades do meio)
- Se tivermos um meio em que as propriedades do volume de espalhamento e do meio envolvente forem muito semelhantes, então também os índices de refração serão próximos:
$$k_{s}-k\ll1 ~~\to~~ k_{s}=\frac{2\pi n_{s}}{\lambda_{0}}\sim k=\frac{2\pi n_{meio}}{\lambda_{0}}~~\to~~ n_{s}\sim n_{meio}$$
- Assim podemos de forma minimamente correta aproximar $S\approx 2k(k_{s}-k)U_{0}$

#### Espalhamento de Rayleigh
- Este é o caso quando o volume de espalhamento tem um volume muito inferior ao comprimento de onda 
- Continuamos a considerar que o contraste entre as propriedades das 2 regiões é muito reduzido, de modo que a aproximação de Born se aplica
    - Ou seja: $S(\vec{r})\approx [k_{s}^{2}(\vec{r})-k^{2}]U_{0}(\vec{r})$ 
- Juntamente com a equação de Helmholtz, isto dá-nos: $U_{s}(\vec{r})\approx \int_{V} S(\vec{r'}) \frac{e^{-ik|\vec{r}-\vec{r'}|}}{4\pi|\vec{r}-\vec{r'}|}d\vec{r'}$
- Ora, integral é sobre um volume de espalhamento $V$. Se ele tiver dimensões $\ll\lambda$, então podemos remover a dependência espacial por completo: $S_{equivalente}\approx [k_{s}^{2}-k^{2}]U_{0}V$
- Ou seja, se tivermos a fonte na origem $\vec{r'}=0$ podemos definir: $$S_{equivalente} (\vec{r'})=(k_{s}^{2}-k^{2})U_{0}V \delta(\vec{r'})$$
logo:
$$\begin{align*}
U_{s}(\vec{r})&= \int_{V} S(\vec{r'}) \frac{e^{-ik|\vec{r}-\vec{r'}|}}{4\pi|\vec{r}-\vec{r'}|}d\vec{r'}\\
&= \int_{V}(k_{s}^{2}-k^{2})U_{0}V \delta(\vec{r'})\frac{e^{-ik|\vec{r}-\vec{r'}|}}{4\pi|\vec{r}-\vec{r'}|}d\vec{r'}\\\\
&= (k_{s}^{2}-k^{2})U_{0}V \delta(\vec{r'})\frac{e^{-ik|\vec{r}-\vec{r'}|}}{4\pi|\vec{r}-\vec{r'}|}\Biggr|_{\vec{r'}=\vec{0}}\\
&= VU_{0} (k_{s}^{2}-k^{2})\frac{e^{-ikr}}{4\pi r}
\end{align*}$$
- Ou seja:
$$U_{s}(\vec{r})= \left(\frac{VU_{0}(k_{s}^{2}-k^{2})}{4\pi}\right) \frac{e^{-ikr}}{r}$$
temos então uma **onda esférica** centrada em $\vec{r'}=\vec{0}$ (sendo essa a posição do espalhamento) que tem amplitude proporcional à da onda incidente.

##### Intensidade espalhada
- A intensidade desta onda será:
$$I_{s}(\vec{r})=\frac{|U_{s}(\vec{r}|^{2}}{2\eta}\approx \left(\frac{V^{2}U_{0}^{2}(k_{s}^{2}-k^{2})^{2}}{2\eta}\right) \frac{1}{4\pi r^{2}}= (k_{s}^{2}-k^{2})^{2} \frac{V^{2}}{4\pi r^{2}} I_{0}$$

##### Potência total espalhada
- Podemos definir esta grandeza como sendo o integral da intensidade sobre uma superfície esféria centrada no espalhamento
$$P_{s}=4\pi r^{2}I_{s}(r)=\frac{1}{4\pi} (k_{s}^{2}-k^{2})^{2} V^{2}I_{0}(0)$$
- Então notemos que $P_{s}\propto V^{2}$
- Temos: $k_{s}^{2}-k^{2}=\frac{4\pi^{2}}{\lambda_{0}^{2}} (n_{s}^{2}-n_{meio}^{2})$. Ao substituir isto na equação da potência temos:
$$P_{s}=\frac{4\pi^{3} V^{2}I_{0}(n_{s}^{2}-n_{meio}^{2})^{2}}{\lambda_{0}^{4}}$$

### Tratamento não escalar
- Como já vimos noutros casos nesta UC, para o espalhamento fizemos o estudo usando *amplitudes complexas* que cumprem a equação de Helmholtz.
- Como também já vimos, tendo a amplitude $U$ podemos definir para o espalhamento o vetor potencial magnético:
$$\vec{A}_{s}(\vec{r})=a_{0} U_{s}(\vec{r})\hat{u}$$
nota: $\hat{u}$ aponta na direção das oscilações das cargas elétricas na região de espalhamento.
- Sabemos que este potencial irá cumprir a equação de helmholtz: $\nabla^{2}\vec{A}_{s} + k_{s}^{2}\vec{A}_{s}=0$
- E sabemos que, sabendo $\vec{A}_{s}$ facilmente obtemos os campos de espalhamento:
$$\begin{cases}
\vec{H}_{s}=\frac{1}{\mu} \nabla \times \vec{A}_{s} \\
\vec{E}_{s}(\vec{r}) = \frac{1}{i\omega\varepsilon_{s}} \nabla \times \vec{H}_{s}(\vec{r})
\end{cases}$$

**Mais numérico**
- Consideremos que a direção do campo elétrico é decidida pelo fasor $\vec{E}_{0}$ e que $\theta$ é um ângulo relativo ao campo E em que queremos determinar a radiação espalhada.
- Teremos:
$$I_{s}(\vec{r},\theta)\approx (k_{s}^{2}-k^{2})^{2} \frac{V^{2}}{(4\pi r)^{2}} I_{0}(0)\sin^{2}\theta$$
- Ou seja, temos uma coisa deste género:
![[dependencia azimutal luz.png]]
notemos que o forward-scattering e o back-scattering têm a mesma intensidade.

- Podemos ainda voltar a determinar a potência espalhada com esta nova equação da intensidade. Integrá-mo-la numa superfície esférica centrada no espalhamento:
$$\begin{align*}
P_{s}\approx \int_{S}I_{s}(\vec{r,\theta})dS&= \frac{V^{2}I_{0}|k_{s}^{2}-k^{2}|^{2}}{(4\pi)^{2}}\int_{S}\frac{\sin^{2}\theta}{r^{2}}dS\\
&= \frac{V^{2}I_{0}|k_{s}^{2}-k^{2}|^{2}}{(4\pi)^{2}}\int_{S}\frac{\sin^{2}\theta}{r^{2}}r^{2}\sin\theta d\theta d\phi\\
&= \frac{V^{2}I_{0}|k_{s}^{2}-k^{2}|^{2}}{8\pi}\int_{0}^{\pi}\sin^{3}\theta d\theta\\
&= \frac{V^{2}I_{0}|k_{s}^{2}-k^{2}|^{2}}{6\pi}
\end{align*}$$
que é $2/3$ menor que o valor obtido no tratamento escalar! Isto originou-se na nova dependência de $\sin^{2}\theta$ claro.

##### Secção eficaz
- Podemos definir a secção eficaz do espalhamento $\sigma_{s}$ de forma que:
$$P_{s}=\sigma_{s}I_{0}$$
- Ou seja, podemos estudar o espalhamento como sendo uma abertura que interceta a onda incidente e recolhe energia (que corresponde à potência espalhada).
- Assim, se tivermos espalhamento fraco (Born) e um volume de espalhamento com dimensões $\ll\lambda$ (Rayleigh) então temos:
$$P_{s}=\frac{V^{2}I_{0}|k_{s}^{2}-k^{2}|^{2}}{6\pi} \quad;\quad \sigma_{s}=\frac{V^{2}|k_{s}^{2}-k^{2}|^{2}}{6\pi}$$

#### Esplhamento de Mie
- A aproximação de Born aplica-se a estruturas de qualquer tamanho, desde que o espalhamento seja fraco!
- Se o espalhamento não for fraco, a aproximação nãos e aplica e não dá para estudar o problema de forma analítica
- _EXCETO_ se o volume de espalhamento for **esférico**!! Nesse caso, independentemente da intensidade do espalhamento e da dimensão do volume, podemos estudar de forma analítica :  temos **_espalhamento de Mie_**.

- Quando temos partículas esféricas com dimensões $\ll\lambda$ temos espalhamento de Rayleigh, em que há dependência de $1/\lambda_{meio}^{4}$ :
![[rayleigh.png]]
- Quando temos partículas esféricas com dimensões $\sim\lambda$ temos espalhamento de Mie, em que há dependência de $\lambda_{meio}$:
![[mie.png]]
- Quando temos partículas esféricas com dimensões $\gg\lambda$ temos espalhamento de Mie, em que há dependência fraca de $\lambda_{meio}$:
![[mie 2.png]]

- Vejamos na prática este fenómeno:
![[mie irl.png]]

- Na prática, isto permite determinar o tamanho de partículas de forma remota.

#### Atenuação por espalhamento
- Consideremos o regime de Rayleigh
- O espalhamento de 1 só zona tem intensidade muito reduzida, como vimos. No entanto, muitas muitas zonas juntas podem resultar numa atenuação significativa da onda incidente.
- Consideremos que temos $N_{s}$ zonas de espalhamento por unidade de volume. Temos a secção eficaz de espalhamento de 1 região, $\sigma_{s}$. 
![[atenuacao espalhamento.png]]
- Temos que ao atravessar uma fatia de espessura $\Delta z$ ocorre uma diminuição da intensidade da onda incidade de $N_{s}\sigma_{s}\Delta z I$
- Ou seja:
$$\Delta I=-N_{s} \sigma_{s} \Delta z I~~\to~~ \frac{\Delta I}{\Delta z}=- (N_{s}\sigma_{s})I$$
ou seja, se $\Delta z\ll1$ temos:
$$I(z)_{espalhamento}=I_{0} e^{-\alpha_{s}z}$$
em que $\alpha_{s}=N_{s}\sigma_{s}$ é o *coeficiente de espalhamento*.
- No caso em que temos um meio com espalhamento ($s$) **E** absorção ($a$), teremos $$I(z)=I_{0}e^{-\alpha z}\quad;\quad \quad \alpha=\alpha_{s} + \alpha_{a}$$

## Propagação em meio com dispersão temporal
- Um meio dispersivo tem índice de refração e coeficiente de absorção diferentes para cada frequência
- Um impulso de luz é uma soma de ondas monocromáticas. Ora, quando um destes sofre dispersão, cada onda terá um comportamento diferente e o impulso sofre dispersão temporal.

### Fourier
- Temos uma função temporal $u(t)$ que representa uma função de onda.
- A sua transformada de Fourier é $v(\nu)=\int_{-\infty}^{+\infty} u(t)e^{-i2\pi\nu t}dt$ 
    - Temos a transformada inversa: $u(t)=\int_{-\infty}^{+\infty}v(\nu)e^{i2\pi\nu t}d\nu$
- Notemos que isto quer dizer que a função real $u(t)$ pode ser representada como uma soma infinita de ondas harmónicas, em que cada frequência $\nu$ tem um certo peso atribuído $v(\nu)$.

### Função analítica
- Vimos ainda que podemos estudar um sinal/sistema usando a sua **amplitude complexa**: $U(t)=u_{0}e^{i\omega t}$, que também podemos chamar de *função analítica* de $u(t)$
- Podemos dividir isto nas componentes real e imaginária: $U(t)=U_{r}(t)+iU_{i}(t)$
- E sabemos que estas 2 partes relacionam-se com a transformada de Hillbert:
$$U_{r}(t)=\frac{1}{\pi}\int_{-\infty}^{+\infty} \frac{U_{i}(\eta)}{t-\eta}d\eta \quad;\quad U_{i}(t)=\frac{1}{\pi}\int_{-\infty}^{+\infty} \frac{U_{r}(\eta)}{t-\eta}d\eta$$


### Juntar tudo
- Podemos então juntar estes 2 conhecimentos e temos:
$$u(t)=\int_{-\infty}^{+\infty}v(\nu)e^{i2\pi\nu t}d\nu \quad\to \quad U(t)=2\int_{0}^{+\infty} V(\nu)e^{i2\pi\nu t}d\nu$$
- Fazer o integral não ir até $-\infty$ torna-o assimétrico, de modo que $U(t)$ é **complexo**, sendo de facto a função analítica.