# Eletro 1 - Aula teórica 10 (JAM)
- Na aula anterior demos a **lei de Gauss**:
$$\Phi=∯_\Sigma\vec E(\vec r)\cdot\hat n(\vec r)ds=\frac{q_{int}}{\varepsilon_0}$$
- Imaginemos agora que temos uma superfície $\Sigma$, com uma carga $q$:
![[carga pontual fluxo]]
- Ora, temos que, para os campos gerados em $\vec r_1$ e $\vec r_2$, $E_1\propto \frac{1}{r_1^2}$ e $E_2\propto \frac{1}{r_2^2}$
- Assim,$$\frac{E_1}{E_2}\propto\frac{\frac{1}{r_1^2}}{\frac{1}{r_2^2}}=\frac{r_2^2}{r_1^2}$$
- Assim, como os restantes termos ($\frac{q}{4\pi\varepsilon_0}$) de ambos os campos se iriam anular, temos que:
$$E_1\cdot r_1^2=E_2\cdot r_2^2$$
- Assim, como $d\phi_1=\vec E(\vec r_1)\cdot\hat n_1ds_1$ e $d\phi_2=\vec E(\vec r_2)\cdot\hat n_2ds_2$, então $d\phi_1=d\phi_2$
- Temos então que $E_1ds_1=E_2\cos\theta ds_2$ (obtido pelos produtos escalares)
- Assim, considerando que $E_i=\frac{1}{r_i^2}$, temos que 
$$\frac{ds_1}{r_1^2}=\cos\theta\frac{ds_2}{r_2^2}$$
- Logo, é como se $ds_2\cos\theta$ fosse uma projeção de $ds'$ na sueprfície $\Sigma$
- Deste modo temos que
$$\frac{ds_1}{r_1^2}=\frac{ds_2}{r_2^2}=d\Omega$$, em que Omega é um **ângulo sólido**

### Ângulo sólido
Podem ser calculados assim:
![[angulo solido 2]]
- Em que alpha é um Ângulo sólido.
- Temos sempre que:
$$\Huge\alpha=\frac{dl}{r^2}=\frac{dl~'}{r~'^2}$$
- Isto é para coisas em 3D. Em 2D, o r em baixo não está ao quadrado.

--- Ver o resto da demonstração no caderno ---

---
- Imaginesse agora que temos um certo ponto em que $\vec E(\vec r)=\vec0$. 
- Ora, teríamos algo assim:
![[campo nulo]]
- No entanto, se definirmos uma qualquer superfície Sigma, que contenha este ponto nela, o **flusxo não é nulo!**, uma vez que a carga interior não é nula.
- Ou seja, pela lei de Gauss podemos concluir que
    - As **linhas de campo nunca se cruzam**
    - Não há posições de equilíbrio estável

### E em sup esférica
- Imaginemos agora que temos uma superfície esférica carregada, com $\sigma$ constante
![[campo sup esferica]]
- Podemos ver que independente do local (no interior da sup esférica), $E=0$
- Podemos demonstrar isso:
    - Por exemplo, para $dE_1$, temos que $dE_1=\frac{1}{4\pi\varepsilon_0}\frac{dq_1}{r_1^2}$. Como $\sigma=\frac{dq}{ds}$, então $$dE_1=\frac{1}{4\pi\varepsilon_0}\frac{\sigma ds_1}{r_1^2}$$
    - Ora, um **ângulo sólido é uma área a dividir por uma dist^2**, então $d\Omega=\frac{ds_1}{r_1^2}$, então: $$dE_1=\frac{1}{4\pi\varepsilon_0}\sigma d\Omega$$
    - Obtemos exatamente o mesmo para $dE_2$
    - Assim, $\vec E(\vec r)=\vec 0$
- Deste modo, concluímos que a única justificação lógica para isto é que:
> Dentro de uma superfície esférica **não há linhas de campo**

#em1 #fluxoE #angulo_solido #fisica 