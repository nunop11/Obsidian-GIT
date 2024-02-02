## 8.1 - Gráfico de Moody
- Vimos no capítulo de análise dimensional que
$$\begin{align*}
\Delta p_{atrito}&= \phi(v,D,l,\varepsilon,\mu,\rho)\\
&\downarrow\\
\frac{\Delta p_{atrito}}{\frac{1}{2}\rho v^{2}}&=  \phi\left(\frac{\rho vD}{\mu}, \frac{l}{D}, \frac{\varepsilon}{D}\right)
\end{align*}$$
Além disso, se o escoamento for bem desenvolvido, temos que a perda de pressão è proporcional à distância percorrida:
$$\frac{\Delta p_{atrito}}{\frac{1}{2}\rho v^{2}}=\frac{l}{D}\phi\left(Re , \frac{\varepsilon}{D}\right)$$
em que esta equação aparece frequentemente nas formas
$$\Delta p_{atrito}=f \frac{l}{D} \frac{\rho v^{2}}{2} \quad \quad;\quad \quad \frac{\Delta p_{atrito}}{\rho g}=h=\frac{1}{2}f \frac{l}{D} \frac{v^{2}}{g}$$
em que $f=C_{f}=\phi\left(Re, \frac{\varepsilon}{D}\right)$ é o fator de atrito.

- Há então alguns comportamentos que se verfiicam empiricamente:
    - Em regime laminar $f$ é independente da rugosidade relativa $\varepsilon/D$ (só depende do Reynolds) e temos especificamente $f=64/Re$ (vem da Eq Poiseuille)
    - Para $2100<Re<4000$ o regime pode ser laminar ou turbulento, endo $f$ indefinido - AKA regime de transição
    - Para $Re$ elevado temos escoamento perfeitamente turbulento (turbulento completamente desenvolvido) e $f$ é independente de $Re$
![[grafico de moody.png|500]]

- Portanto, verifica-se graficamente todos os comportamentos previstos.

- Podemos ainda ver que, 
    - Em escoamento Laminar $\Delta p=\frac{128\mu l}{\pi D^{4}}Q$, ou seja, a perda de pressão é *proporcional* a $\mu,l,Q,D^{-4}$. Independente de $\rho,\varepsilon$
    - Em escoamento Turbulento $\Delta p=8f \frac{l}{D}\rho \frac{Q^{2}}{\pi^{2}D^{4}}$ , ou seja, a perda de pressão é proporcional a $Q^{2},l,D^{-5},\rho$. Independente de $\mu,Re$

- Para escoamentos em transição, mais perto de Turbulento ($Re>4000$) temos a aproximação de *Colebrook*:
$$\frac{1}{\sqrt{f}}=-2 \log\left(\frac{\varepsilon/D}{3,7}+\frac{2,51}{Re \sqrt{f}}\right)$$
- Para $10^{-6}<\frac{\varepsilon}{D}<10^{-2}$ e $5000<Re<10^{8}$ temos a aproximação de Miller:
$$f=\frac{1,325}{\left[\ln \left(\frac{\varepsilon}{3,7D}+\frac{5,74}{Re^{0,9}} \right) \right]^{2}}$$
- E para escoamentos turbulentos em tubos lisos ainda temos a aproximação de Blasius:
$$f=\frac{0,316}{Re^{0,25}}$$

## 8.2 - Caraterísticas de Tubagens
- No dia a dia referimo-nos a tubagens conforme o seu diâmetro nominal (diâmetro interno efetivo):
![[diametro tubos.png]]
(não percebo como o diâmetro nominal pode ser maior que o diâmetro interno mas pronto)

- Temos ainda valores tabelados de $\varepsilon$:
![[rugosidade tubos.png]]
![[rugosidade tubos 2.png]]

## 8.3 - Perdas de Carga Localizada
- Nome dado a perdas de carga, não ao longo de um tubo, mas em válvulas, cotovelos, entradas e saídas.
- Para isto usamos o *coeficiente de perdas*:
$$K=\frac{\Delta p_{atrito}}{\frac{1}{2}\rho v^{2}}~~\to~~ \frac{\Delta p}{\rho g}=K \frac{v^{2}}{2g}=h_{perdas}$$
facilmente vemos que $K=\phi(Re,$ geometria). Ora, considerando o escoamento em tubos reais perfeitamente turbulento, vemos que $K$ não depende do número de Reynolds.
- Podemos ainda escrever esta perda de carga através da distância de tubagem reta ($l_{eq}$) que seria preciso percorrer para ter a mesma perda de carga localizada:
$$h_{p}=K \frac{v^{2}}{2g}=f \frac{l_{eq}}{D}\frac{v^{2}}{2g}$$
![[coeficientes atrito tubos.png]]

### Expansão Súbita
![[expansao subita.png]]

- Usando bernoulli:
$$\begin{align*}
p_{1}+ \frac{1}{2}\rho v_{1}^{2}&= p_{2}+ \frac{1}{2}\rho v_{2}^{2}\\
\frac{p_{1}}{\rho g} + \frac{v_{1}^{2}}{2g}&= \frac{p_{2}}{\rho g}+ \frac{v_{2}^{2}}{2g}\\
\frac{p_{2}-p_{1}}{\rho g}&= \frac{v_{1}^{2}}{2g} -\frac{v_{2}^{2}}{2g}\\
h_{perdas}&= \frac{v_{1}^{2}}{2g} \left[1-\left(\frac{v_{2}}{v_{1}}\right)^{2}\right]= \frac{v_{1}^{2}}{2g} \left[1-\left(\frac{A_{2}}{A_{1}}\right)^{2}\right]=K \frac{v_{1}^{2}}{2g}
\end{align*}$$
E temos: $K=1-\left(\frac{A_{2}}{A_{1}}\right)^{2}$
- No entanto, não percebo porquê, o correto é: $$K=\left(1-\frac{A_{2}}{A_{1}}\right)^{2}$$ 
### Contração Súbita
![[contracao subita.png]]
- Confia na dedução, temos:
$$K=\left(\frac{1}{C_{c}}-1\right)^{2}$$
(em que $C_{c}=\frac{A_{1}}{A_{2}}$)

### Medidor de Orifício

- Vimos no capítulo do Bernoulli que o caudal num medidor de orifício é:
$$Q=C_{C}A_{2}\sqrt{\frac{2(p_{1}-p_{2})}{\rho \left[ 1- \left(\frac{A_{2}}{A_{1}} \right)^{2}\right]}}=C_{0}Q_{ideal}$$
- Introduzimos então o coeficiente de contração $C_{0}$ que conta com efeitos como a contração do jato e as perdas localizadas que ocorrem no orifício (sendo que estes efeitos se evidenciam mais com escoamentos mais turbulentos)
- Abaixo vemos como vários $C_{0}$ variam conforme o número de Reynolds. No final da linha temos um número que é $\beta=d/D$. De notar que na equação original (Bernoulli) $\beta$ _é_ o coeficiente de contração $C_{C}$.

![[grafico medidor orificio.png]]

## 8.4 - Perdas em tubagens não circulares
- O "diâmetro" que usamos nos cálculos é
$$D_{h}=4 \frac{A}{P_{molhado}}$$
sendo $P_{molhado}$ o **perímetro molhado** e $A$ a àrea da região onde há fluxo.

_**EXS**_
![[tubos concentricos.png]]
- Temos $A=\frac{\pi D_{2}^{2}}{4}-\frac{\pi D_{1}^{2}}{4}=\frac{\pi}{4}(D_{2}^{2}-D_{1}^{2})$ e $P_{molh}=D_{2}+D_{1}$

![[tubo retangular.png]]
- Temos $A=ab~,~P_{molh}=2a+2b$

## 8.5 - Válvulas
### Válvula de Globo
![[valvula globo.png]]
- Quando aberta, para escoamento turbulento perfeitamente desenvolvido, esta válvula tem $K=10$
- Normalmente utilizadas onde é necessário realizar operações frequentes de abertura e fecho, como também no controlo do caudal. Usado para quase tudo, altas e baixas pressões.

### Guilhotina
![[valvula guilhotina.png|475]]
- Usadas no escoamento de fluidos com sólidos em suspensão, tubagens de grandes dimensões ou quando o espaço disponível para a válvula é fator importante.
- Conforme se sobe ou desce o disco:
![[coeficientes perda vavlula guilhotina.png|500]]

### Válvula de Borboleta
![[valvula borboleta.png]]
- Usada para *regular* caudal em rede. Principalmente usado com gases ou líquidos a baixa pressão.
- Para um fluido a escoar em regime turbulento perfeitamente desenvolvido temos
![[coeficientes perda valvula borboleta.png|475]]

### Válvula de Esfera
![[valvula esfera.png|275]]
- Quando aberta, perturba o escoamento o mínimo possível. Quando fechada bloqueia o fluxo. Bom até a alta pressão. 
- Na realidade, para um fluido em regime turbulento perfeito, a válvula aberta tem $K=0,05$

### Válvula em Agulha
![[valvula agulha.png]]
- Semelhante à válvula de esfera. Mais usada com gases.

### Válvula de Retenção
![[valvula retencao.png]]
- Permite escoamento num só sentido, impede fluido de retornar.

### Escolher válvula
Ter em conta
- Função da válvula (controlar ou cortar fluxo).
- Tipo de fluido que irá passar e como reage a materiais de que valvulas possam ser feitas.
- Sistema de acionamento da válvula (manual ou automático).
- Pressão e caudal com que fluido irá passar.

## 8.6 - Aplicação
- Vê resoluções :D