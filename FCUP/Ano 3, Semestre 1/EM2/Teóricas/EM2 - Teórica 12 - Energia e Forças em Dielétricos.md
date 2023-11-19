## Energia Armazenada em Condensador com Dielétrico
- Consideremos um condensador. Em cada placa temos uma densidade de carga $\pm\sigma_{\ell}$. Consideremos $\hat{z}$ o eixo perpendicular às placas.
- Consideremos que se introduz um dielétrico linear nele.

#### Introduzir dielétrico com $\sigma_{\ell}=0$ constante
- Por geometria, temos:
$$\vec{D}=D(z) \hat{z}~~\to~~ \nabla \times \vec{D}=\vec{0}$$
isto implica que $\nabla \times \vec{P}=\vec{0}$.
- Podemos desenvolver:
$$\begin{align*}
\vec{D}&= \sigma_{\ell}\hat{z}\\
\vec{E}&= \frac{\sigma_{\ell}}{\varepsilon}\hat{z}=\frac{\sigma_{\ell}}{\varepsilon_{0}} \frac{1}{\varepsilon_{r}}\hat{z}=\frac{1}{\varepsilon_{r}}E_{vacuo}\hat{z}
\end{align*}$$
- Daqui resulta que $V=\frac{V_{vacuo}}{\varepsilon_{r}}$. Logo:
$$C=\frac{Q_{\ell}}{V}=\varepsilon_{r}C_{vacuo}$$
(em que $C$ é a capacidade do condensador)

- Vemos ainda que $U_{vac}=\frac{1}{2}C_{vac}V_{vac}^{2}$. Então:
$$U=\frac{1}{2}CV^{2}=\frac{U_{vac}}{\varepsilon_{r}}$$

#### Introduzir dielétrico com $V$ constante
- Obviamente, temos $V=V_{vacuo}$
- Continuamos a ter $C=\varepsilon_{r}C_{vacuo}$. Isto porque a capacidade varia devido à polarização, manter a diferença de potencial não irá afetá-la.
- A energia armazenada no condensador:
$$U=\frac{1}{2}CV^{2}=\varepsilon_{r}U_{vacuo}$$
daqui resulta que:
$$U_{vacuo}=\frac{\varepsilon_{0}}{2}\int |\vec{E}|^{2}d^{3}r\to U=\frac{\varepsilon_{0}}{2}\int \varepsilon_{r}|\vec{E}|d^{3}r=\frac{1}{2}\int \varepsilon|\vec{E}|^{2}d^{3}r=\frac{1}{2}\int \vec{D}\cdot\vec{E}d^{3}r$$
provemos isto.

- Consideremos agora que temos o dielétrico já no sítio e que trazemos as cargas livres aos poucos para o sistema. O trabalho necessário para trazer um incremento $\Delta \rho_{\ell}$ será: $$\Delta W=\int (\Delta \rho_{\ell})V d^{3}r$$
- Ora, como $\nabla \cdot \vec{D}=\rho_{\ell}$ podemos escrever $\Delta \rho_{\ell}=\nabla \cdot (\Delta \vec{D})$ e fica:
$$\Delta W=\int (\nabla \cdot (\Delta \vec{D}))V d^{3}r$$
mais uma vez temos algo do tipo $(\nabla \cdot \vec{A})f$. Temos que: $$\nabla \cdot \vec{A}f=(\nabla \cdot \vec{A})f+ \vec{A}\cdot(\nabla f)$$ e podemos escrever o trabalho como:
$$\begin{align*}
\Delta W&= \int \nabla \cdot (\Delta \vec{D}V)d^{3}r - \int \Delta \vec{D}\cdot\nabla V d^{3}r\\
&= \int \nabla \cdot (\Delta \vec{D}V)d^{3}r + \int \Delta\vec{D}\cdot \vec{E}~d^{3}r\\
&= \oint  (\Delta \vec{D}V)\cdot d\vec{s} + \int \Delta\vec{D}\cdot \vec{E}~d^{3}r
\end{align*}$$
o primeiro termo será nulo se integrarmos em todo o espaço e ficamos com
$$\Delta W=\int \Delta \vec{D}\cdot \vec{E}~d^{3}r$$
- Para um dielétrico linear em específico temos:
$$\vec{D}=\varepsilon\vec{E}\to \frac{1}{2}\Delta(\vec{D}\cdot\vec{E})=\frac{\varepsilon}{2}\Delta|\vec{E}|^{2}$$
sendo $\Delta \rho_{\ell}$ um incremento infinitesimal de carga podemos dizer que $\frac{1}{2}\Delta \vec{E}\simeq \Delta \vec{E}$ e podemos continuar a desenvolver esta igualdade:
$$\frac{1}{2}\Delta(\vec{D}\cdot\vec{E})=\frac{\varepsilon}{2}\Delta|\vec{E}|^{2}=\varepsilon (\Delta \vec{E})\cdot\vec{E}=\Delta\vec{D}\cdot\vec{E}$$
e ficamos com:
$$\Delta W=\int \Delta \vec{D}\cdot \vec{E}~d^{3}r \to \Delta W=\frac{1}{2}\Delta\int \vec{D}\cdot\vec{E}~d^{3}r$$
logo provamos que
$$W=\frac{1}{2}\int \vec{D}\cdot \vec{E}~d^{3}r=U$$

## Forças em Dielétricos
- Tal como em condutores, nos dielétricos é comum termos acumulações de carga perto das densidades de carga livre. Deste modo, o dielétrico está sujeito ao campo e força elétricos.

![[deslizar dielétrico entre condensador.png]]
- Consideremos um bloco de material dielétrico parcialmente introduzido num condensador de placas planas com as dimensões indicadas acima.
- Ora, até agora consideramos sempre que $d\ll l,w$ e dissemos que o efeito de borda do campo elétrico é desprezável. Bem, aqui já não. Além da lógica, isto não é possível porque os integrais de linha dos percursos traçados abaixo (que passam pelo dielétrico) não seriam nulos: 
![[campo de borda.png]]

- Ora, voltando ao início desta secção, o dielétrico está então sujeito a este campo elétrico de borda, que é não-uniforme.
- Consideremos que se move o dielétrico uma distância infinitesimal $dx$. Para isso exercemos uma força $F_{ext}$, pelo que realizamos um trabalho $dW=F_{ext}dx$.
- Ora, para mover o material temos que exercer uma força $F_{ext}$ para poder contrariar a força elétrica que a placa exerce no dielétrico, $F$. Ou seja temos $$F=-F_{ext} \to F=\frac{-dW}{dx}$$
por outro lado, ao mover o dielétrico para fora do condensador estamos a alterar a energia nele armazenada, numa *mesma quantidade*: $dW$.

- Podemos escrever (not sure porquê):
$$V_{vac}= \frac{\sigma_{\ell}(vac)}{\varepsilon_{0}}d \quad \quad;\quad \quad V_{die}=\frac{\sigma_{\ell}(die)}{\varepsilon_{0}\varepsilon_{r}}d$$
(em que $\sigma_{\ell}(vac),\sigma_{\ell}(die)$ são as porções da densidade de carga livre que está no vácuo e no dielétrico)

- A capacidade do condensador é dada por:
$$C = C_{vacuo}+ C_{dieletrico}= \frac{Q_{vac}}{V_{vac}}+ \frac{Q_{die}}{V_{die}} =\frac{xw \sigma_{\ell}(vac)}{\frac{\sigma_{\ell}(vac)}{\varepsilon_{0}}d} + \frac{(l-x)w \sigma_{\ell}(die)}{\frac{\sigma_{\ell}(die)}{\varepsilon_{0}}d} $$
$$C=\frac{\varepsilon_{0}xw}{d} + \frac{\varepsilon_{0}\varepsilon_{r}(l-x)}{d}=\frac{\varepsilon_{0}w}{d}(\varepsilon_{r}l-\chi_{e}x)$$

#### $Q$ constante
- Consideremos que a carga total das placas $Q$ é constante. A energia armazenada no condensador será:
$$U=\frac{1}{2} \frac{Q^{2}}{C}$$
logo:
$$F=- \frac{dW}{dx}=\frac{1}{2} \frac{Q^{2}}{C^{2}} \frac{dC}{dx}=\frac{1}{2}V^{2} \frac{dC}{dx}=\frac{1}{2}V^{2} \frac{-\varepsilon_{0}\chi_{e}w}{d}=\frac{-\varepsilon_{0}\chi_{e}w}{2d}V^{2}$$

#### $V$ constante
- Consideremos agora que $V$ é constante. Agora teremos $Q_{\ell}=CV$ e não constante. Este caso é equivalente a ligar o condensador a uma fonte de pontencial. Ora, esta também está a fazer trabalho e temos:
$$dW=F_{ext}dx + V dQ$$
obtemos:
$$F=- \frac{dW}{dx}+V \frac{dQ}{dx}=- \frac{1}{2}V^{2} \frac{dC}{dx}+ V^{2} \frac{dC}{dx}=\frac{1}{2}V^{2} \frac{dC}{dx}$$
ou seja, a força é igual !!!

- Ou seja, não importa se consideramos $Q,V$ constantes. A força exercida sobre o dielétrico depende apenas da distribuição de carga livre e de polarização. No entanto, é mais fácil calcular a força com $Q$ constante.
