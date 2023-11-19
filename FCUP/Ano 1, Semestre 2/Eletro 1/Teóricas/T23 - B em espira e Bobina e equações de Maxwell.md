# Eletro 1 - Aula teórica 23 (JAM & CCR)
-- $\mathcal{Agostinho}$ --
- Comecemos por recordar 2 fórmulas muito importantes que já vimos:

==Lei de Gauss Integral:==
>$$\Huge∯_\Sigma \vec E(\vec r)\cdot\hat n(\vec r)ds=\frac1{\varepsilon_0}\int_V\rho(\vec r)dV$$

==Fluxo Magnético em superfícies fechadas:==
>$$\Huge∯_\Sigma \vec B(\vec r)\cdot \hat n(\vec r)ds=0$$

---
- Na aula, foi mostrado este sistema, que consiste de uma Bobina 1, fixa e dentro de um recipiente de vidro. Do lado de fora deste existe uma bobina 2, à qual está presa uma lâmpada. Ora, verificou-se que quando estava a passar corrente AC pela bobina 1, quanto mais próxima dela estivesse a bobina 2, maior seria a intensidade da luz emitida pela lâmpada.
![[lampada bobinas]]
- Ora, ao haver corrente AC na bobina 1, esta passa a gerar um campo $B$ que varia com o tempo. Assim, de alguma forma existe tranferência de energia, de modo que é criada corrente na bobina 2, e esta corrente liga a lâmpada. No entanto, o vidro impede a passagem do campo. 
- Deste modo, esta transferência de energia tem de ter sido causadao pelo fluxo magnético numa superfície não fecahda.

- Assim, quando o fluxo magnético varia no tempo ($\frac d{dt}\Phi_B(t)\neq0$) passa a existir uma **Força Eletromotriz**. Esta força acaba por ser a DDP emtre 2 pontos: $-\oint\vec E\cdot\vec dl$ . E assim temos a **Lei de Faraday**:
>$$\Huge\frac d{dt}\iint_\Sigma\vec B(t)\cdot\hat n~ds=-\oint\vec E\cdot\vec dl$$
- No secundário tinhamos isto como $\Large\varepsilon=\frac{d\Phi_B}{dt}$
- Verificou-se ainda que se colocassemos a bobina 2 do lado de fora do tubo, a lâmpada já não se acendia. Isso será porque o campo já não varia.

-- $\mathcal{CCRosa}$ --
- Consideremos um condutor retilíneo com corrente estacionária. 
![[2 fios campo]]

Conforme o que vimos na aula anterior, temos:
$$d\vec F_m=I \vec\ell_2\times d\vec B_1\quad\quad,\quad\quad d\vec B(\vec r)=\frac{\mu_0}{4\pi}I_1\frac{\vec dl\times\vec u_R}{r^2}$$
- De notar que, para o ponto $A$, $\vec R$ é o vetor mais próximo de $I_1$; $\vec r$ é o vetor da posição relativa de $A$ em relação à contribuição de comprimento $\vec  dl$
- Como $\vec u_R$ é um vetor unitário, temos que $\vec dl\times\vec u_R=dl~\vec u_\theta$
- Ao marcar os ângulos $\phi$ como visto acima, obtemos que 
$$l=R\tan\phi\leftrightarrow dl=R\frac{1}{\cos^2\phi}d\phi$$
- Temos ainda que $R=r\cos\phi$ e então $$r^2=\frac{R^2}{\cos^2\phi}$$
- Substituindo tudo na formula de $\vec B(t)$:
$$\vec B(t)=\frac{\mu_0I_1}{4\pi}\int_{-\pi/2}^{\pi/2}\frac{R}{\cos\phi}\frac{\cos^2\phi}{R^2}d\phi\vec u_\theta=\frac{\mu_0I_1}{4\pi R}\int_{-\pi/2}^{\pi/2}\cos\phi~d\phi\vec u_\theta$$
- E assim obtemos a equação do campo magnético criado por uma linha infinita com corrente:
$$\large\vec B(R)=\frac{\mu_0I}{2\pi R}\vec u_\theta~~~~(T)$$
Sendo $\vec R$ o vetor mais curto para o fio.

### Espira
- Para uma espira, teríamos, de lado:
![[B em espira]]
- Imaginemos agora que temos uma espira circular (um anel) em que a corrente se move no sentido contra-horário (pelo que a normal será para cima). Nesse caso, o campo magnético para uma dada posição $z$ no eixo central do anel seria:
$$\vec B_\text{anel fechado}(z)=\frac{\mu_0I}{4\pi}\frac{R^2}{(R^2+z^2)^\frac32}\hat u_z$$(fórmula não deeduzida na aula)
- Se tivermos uma espira que consiste em $N$ espiras condensadas, simplesmente multiplicamos $I$ por $N$ para obter o campo.

### Bobina/Solenoide
- Uma bobina consiste de muitas espiras, umas em cima das outras
![[B de bobina]]
- Podemos ver que as linhas têm este formato e que se a corrente fosse no sentido contrário, então o campo entre as espiras seria para baixo (porque a normal seria para baixo). Vemos ainda que as linhas tentam sempre fechar-se.
- No entanto, se $L\approx\infty$, o campo não se fecha pelo que fora da bobina não há campo magnético. Isto foi o que aconteceu no exemplo do início da aula. O tubo de vidro não era infinito, mas tinha comprimento suficiente para o que o campo do lado de fora fosse *quase* nulo.

### Lei de Ampere
- Imaginemos agora que temos um fio condutor com corrente $I$. Iremos considerar uma trajetória $\Gamma$, uma circunferência de raio $R$ no plano normal ao fio. Temos então:
$$\oint_\Gamma\vec B\cdot\vec dl=\oint_\Gamma \frac{\mu_0I}{2\pi R}\hat u_\theta Rd\theta\hat u_\theta=\frac{\mu_0I}{2\pi}\int_0^{2\pi}d\theta=\mu_0I$$
- Isto é a **circulação** de B. E assim temos a **Lei de Ampere**:
>$$\Huge\oint_\Gamma\vec B\cdot\vec dl=\mu_0I\leftrightarrow\oint_\Gamma\vec B\cdot\vec dl=\mu_0\iint_\Gamma\mathcal{\vec J}\cdot\hat n~ds$$
>Deve-se notar que esta é uma das equações de Maxwell, mas ela está incompleta. Esta versão só se aplica se $E$ e $B$ forem estacionários.
 
- Na prática, $\vec B\cdot\vec dl$ dá a projeção de $\vec B$ na trajetória.
- Temos que quando $I_{int}=0$, a circulação do campo B também é 0. De certa forma asemelha-se a $Q_{int}$ na lei de Gauss.
- De notar também que é esta circulação que fez a 

### Bobina Infinita
- Imaginemos que temos uma bobina como no exemplo antes, mas de comprimento infinito:
![[Bobina infinita]]
- Com a lei de gauss imaginavamos superfícies gaussianas, em 3D. Para a lei de ampere imaginamos t rajetórias, tal com a trajetória $\Gamma$, ilustrada acima. Tal como para a lei de Gauss, o objetivo é arranjar superfícies em que a circulação sejza nula.
- Neste caso, como $\vec B\perp\vec dl$, a circulação é nula nos lados de cima e de baixo (horizontais). O lado da esquerda está fora da bobina infinita pelo que $\vec B=\vec0$ e então também tem circulação nula.
- Assim só resta o lado da direita. Temos:
$$\oint\vec B\cdot\vec dl=BL\mu_0I_{int}$$
E sabemos que no lado $L$ passam $N$ linhas. Assim $I_{int}=\frac NL I$. Logo:
$$B_{bobina~inf}=\mu_0\frac NL I=\mu_0nI$$

# Equações de Maxwell dadas:
>$$\Huge \Huge∯_\Sigma \vec E(\vec r)\cdot\hat n(\vec r)ds=\frac1{\varepsilon_0}\int_V\rho(\vec r)dV$$
>$$\Huge∯_\Sigma \vec B(\vec r)\cdot \hat n(\vec r)ds=0$$
>$$\Huge\frac d{dt}\iint_\Sigma\vec B(t)\cdot\hat n~ds=-\oint\vec E\cdot\vec dl$$
>$$\Huge\oint_\Gamma\vec B\cdot\vec dl=\mu_0\iint_\Gamma\mathcal{\vec J}\cdot\hat n~ds$$

E pronto, 
$$\Huge \text{O\quad FIM}$$

#em1 #espira #bobina #maxwell #fisica 