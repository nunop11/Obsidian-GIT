###### Aula 3 - 27/2/2024
## 1.6 - Onda EM em Metal
- Como vimos atrás, consideremos um eletrão livre (Modelo de Drude) sujeito a um campo elétrico:
$$\frac{d\vec{p}}{dt}=- \frac{1}{\tau}\vec{p}+\vec{f}(t)$$
em que temos $\vec{f}=-e\vec{E}$ e o eletrão tem percurso livre médio $\ell=v_{0}\tau\sim1-10\dot{A}$
- Consideramos $\lambda\sim100\dot{A}$

**Campo Oscilatório**
- Consideremos agora um campo oscilatório: $\vec{E}(t)=\vec{E_{0}}e^{i\omega t}$ ou seja temos: $\vec{f}(t)=-e\vec{E_{0}}e^{i\omega t}$. De realçar que isto apenas significa que estamos a induzir uma corrente AC no metal.
- Vamos substituir isto na equação do movimento acima e sugerir sugestões do tipo $\vec{p}(t)=\vec{p_{0}}e^{i\omega t}$:
$$\begin{align*}
\frac{d\vec{p}}{dt}&= - \frac{1}{\tau}\vec{p}+\vec{f}(t)\\
\omega i\vec{p_{0}}e^{i\omega t}&= - \frac{1}{\tau}\vec{p_{0}}e^{i\omega t}-e \vec{E_{0}}e^{i\omega t}\\
&(\dots)\\
\vec{p}(t)&= \frac{e}{i\omega- \frac{1}{\tau}}\vec{E}
\end{align*}$$
e podemos então definir a densidade volúmica de corrente:
$$\vec{\mathcal{J}}(t)= \frac{ne}{m}\vec{p}= \frac{ne^{2}/m}{i\omega-1/\tau} \vec{E}= \frac{ne^{2}\tau/m}{1-i\omega\tau}\vec{E}$$
, pelo que podemos definir uma condutividade $$\sigma(\omega)=\frac{\sigma(0)}{1-i\omega\tau} \quad\quad;\quad \quad \sigma(0)=\frac{ne^{2}\tau}{m}$$
sendo que $\vec{ \mathcal{J}}=\sigma\vec{E}$
- Vemos que $\sigma(0)$ não passa da condutividade DC. $\sigma(\omega)$ é a condutividade dependente de frequência AKA **condutividade AC**.

**Maxwell**
- Recordemos as eqs de maxwell:
$$\begin{align*}
\nabla \cdot \vec{E}&= \rho/\varepsilon_{0}\\
\nabla \cdot \vec{B}&= 0\\
\nabla \times \vec{E}&= - \partial_{t}\vec{B}\\
\nabla \times \vec{H}&= \frac{4\pi}{c}{\vec{\mathcal{J}}}+ \frac{1}{c}\partial_{t}\vec{E}
\end{align*}$$
ora, recordamos que uma onda EM consiste num campo elétrico como aquele que vimos acima, mas contém ainda um campo magnético com equivalente amplitude. 

- Queremos então verificar se a equação de condutividade DC que obtivemos descreve a interação de um metal com uma *onda EM*.
    - Ora, o facto que ignoramos a força do campo magnético ao derivar $\sigma(\omega)$ não deverá fazer nenhuma diferença. Isto porque o termo adicional $- \frac{e\vec{p}}{mc}\times\vec{H}$ é muito inferior ao termo $-e\vec{E}$ (por um fator $v/c$ em que $v$ é sempre reduzido).
    - Outra coisa que assumimos foi que o campo $\vec{E}$ é uniforme no espaço, ou seja, num instante $t$ todos os eletrões livres estão sujeitos ao mesmo campo. Pode não parecer, mas isto até é uma boa aproximação. Isto porque a densidade de corrente num ponto corresponde ao que o campo fez a cada eletrão desde a sua última colisão. Ou seja, desde que o campo não varie muito ao longo de uma média distância livre ($\ell$) podemos considerar que ele é constante. Assim, a equação de $\vec{\mathcal{J}}$ determinada está correta, desde que $\lambda\gg\ell$. Normalmente isto ocorre para metais sujeitos a luz visível.

- Para metais ideais (ou boas aproximações) podemos dizer que $\vec{\mathcal{J}}=\vec{\mathcal{J}}_{\ell}+ \cancel{\nabla \times \vec{M}}$ e que $\frac{\partial\vec{p}}{\partial t}=0$
- Podemos ainda dizer que $\rho(t)=\rho_{0}e^{-t/\tau}\sim0$. Aproximamos a zero porque consideramos tempos $t\gg\tau$. Isto porque consideramos frequências na gama $f:10^{12}-10^{15}\text{Hz}$--- frequências inferiores dariam origem a efeito fotoelétrico.

- Ao fazer $\nabla\times(\nabla\times\vec{E})$ conseguimos obter:
$$\begin{align*}
\nabla(\cancelto0{\nabla \cdot \vec{E}})- \nabla^{2} \vec{E}&= \nabla \times(\nabla \times \vec{E})\\
&= \frac{1}{c}\nabla \times (-\partial_{t}\vec{H})\\
&= \frac{i\omega}{c} \nabla \times \vec{H}\\
&= \frac{i\omega}{c}(\frac{4\pi}{c}{\vec{\mathcal{J}}}- \frac{1}{c}\partial_{t}\vec{E})\\
&= \frac{i\omega}{c^{2}}(4\pi\sigma{\vec{E}}- i\omega\vec{E})\\
&= \vec{E}\left(\frac{i\omega4\pi\sigma}{c^{2}}+ \frac{\omega^{2}}{c^{2}}\right)\\
&= \frac{\omega^{2}}{c^{2}}\left(1+\frac{i4\pi\sigma}{\omega}\right)\vec{E}
\end{align*}$$
em que temos $-\nabla^{2}\vec{E}=\frac{\omega^{2}}{c^{2}}\varepsilon(\omega)\vec{E}$, logo:
$$\varepsilon(\omega)=1+i \frac{4\pi\sigma}{\omega}= 1+i \frac{4\pi\sigma(0)}{\omega(1-i\omega\tau)}=1+i \frac{4\pi ne^{2}\tau}{\omega(1-i\omega\tau)m}$$
- Se $\omega\tau\gg1$ então no denominador temos: $1-i\omega\tau\simeq -i\omega\tau$. Assim, podemos escrever:
$$i\frac{4\pi ne^{2}\tau}{\omega(1-i\omega\tau)m}\simeq-\bcancel{i}\frac{4\pi ne^{2}/m}{\bcancel{i}\omega\cancel{\tau}} \frac{\cancel{\tau}}{\omega}= - \frac{\frac{4\pi ne^{2}}{m}}{\omega^{2}}=-\frac{\omega_{p}^{2}}{\omega^{2}}$$
pelo que, para $\omega\tau\gg1$ podemos fazer a aproximação de 1º grau:
$$\varepsilon(\omega)\simeq 1- \frac{\omega_{p}^{2}}{\omega^{2}}$$
em que $\omega_{p}=\frac{4\pi ne^{2}}{m}$ é a frequênciad e plasma. Para entender melhor o que esta frequência significa, vê a página 19 do Ashcroft ou a ficha 1 (num ex deduzimos usando um modelo simplista).

### 1.6.1 - Desvio para a Ótica
> Esta parte é copiada da aula (não tem no Ashcroft), mas acima baseei-me no mesmo. 
> Deste modo, há uma variação de uma constante: no que tenho acima temos $\varepsilon=C\cdot i \frac{\sigma(0)}{\omega(1-i\omega\tau)}$. Acima (Ashcroft) temos $4\pi$, na aula tinha $4\pi/\varepsilon_{0}$ e nesta parte da aula o prof já só escreveu $1/\varepsilon_{0}$??

- Podemos definir o índice de refração complexo: $$\mathcal{N}=\sqrt{\varepsilon(\omega)}=n+ik~~\to~~ n=\text{Re}[\mathcal{N}]$$
podemos usar $\tilde n$ para representar isto.

#### Incidência normal
- Consideremos um material metálico em que incide perpendicularmente uma onda EM $\vec{E}$.
- Teremos uma refletância $\mathcal{R}=\frac{\vec{\mathcal{J}}^{r}}{\vec{\mathcal{J}}^{i}}$
- Em que podemos escrever:
$$\begin{align*}
\mathcal{R}&= |r_{\parallel}|\\
&= \left|\frac{1-\tilde n}{1+\tilde n}\right|^{2}
\end{align*}$$

- Consideremos $\omega\tau\ll1~~,~~\tau\ll 1/\omega$. Deste modo:
$$\begin{align*}
\varepsilon(\omega)&= 1+i \frac{\sigma(0)}{\omega\varepsilon_{0}(1-i\omega\tau)}= 1+i \frac{ne^{2}\tau}{\omega m\varepsilon_{0}}(1-i\omega\tau)\\
&=  1 - \frac{ne^{2}\tau}{m\omega\varepsilon_{0}}\frac{\omega\tau}{1+\omega^{2}c^{2}} + i \frac{ne^{2} \tau}{m\omega\varepsilon_{0}}\frac{1}{1+\omega^{2}c^{2}}\\
&\sim i \frac{\sigma(0)}{\omega\varepsilon_{0}}  
\end{align*}$$
ou seja, desprezamos a parte real! (Não percebi bem a dedução)
- Como no 1º termo temos $\omega\tau$ e isto é $\ll1$ então o 2o termo desparece. Depois desprezamos a unidade porque $\frac{ne^{2} \tau}{m\omega\varepsilon_{0}}\gg1$

- Assim temos
$$\begin{align*}
\tilde n(\omega)&= \sqrt{\varepsilon(\omega)}=\sqrt{\frac{\sigma(0)}{m\omega}}\sqrt{i}\\
&= \sqrt{\frac{\sigma(0)}{m\omega}} \frac{1+i}{\sqrt{2}}\\
&= \sqrt{\frac{\sigma(0)}{2m\omega}} (1+i)
\end{align*}$$

Assim:
$$\begin{align*}
\mathcal{R}&= \frac{(1-\tilde n)^{2}}{(1+\tilde n)^{2}}\\
&= \frac{n^{2}-2n+1+k^{2}}{n^{2}+2n+1+k^{2}}\\
&\sim \frac{n^{2}+k^{2}-2n}{n^{2}+k^{2}+2n}\\
&\sim \frac{1- \frac{1}{n}}{1+ \frac{1}{n}}\\
&\sim 1-\frac{2}{n}
\end{align*}$$

- Consideremos agora a que $\omega\tau\gg1$. Obtemos agora:
$$\begin{align*}
\varepsilon(\omega)\sim 1+\frac{i\sigma(\omega)}{-i\omega^{2}\tau\varepsilon_{0}}=1 - \frac{\omega_{p}^{2}}{\omega^{2}}~~,~~ \omega_{p}^{2}=\frac{ne^{2}}{m\varepsilon_{0}}
\end{align*}$$
temos permitividade real AKA os campos E e B circulam em fase.