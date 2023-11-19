# Eletro 1 - Aula teórica 14 (JAM)
### Energia de sup esférica
- Temos uma superfície esférica, de carga $Q$, raio $a$ e $\sigma=\frac{Q}{4\pi a^2}$
- E como já vimos:
$$\vec E(r)=\begin{cases}
\vec 0 &, r<a\\
\frac{Q}{4\pi\varepsilon_0r^2}\hat r&, r>a
\end{cases}$$
- Vimos ainda que $$U=\frac{\varepsilon_0}{2}\int_{\text{todo~o~espaço}}|\vec E(\vec r)|^2dV$$
- Assim, comecemos por recordar coordenadas esféricas. Temos:
    -  Vetor unitário $\hat e_r$, direção a partir da origem, para fora
    -  Vetor unitário $\hat e_\theta$, que indica a direção em que $\theta$ (ângulo polar) varia
    - Vetor unitário $\hat e_\phi$, que indica a direção em que $\phi$ (ângulo longitdinal/azimutal) varia
![[cords esféricas]]
- E temos ainda que $x=r\sin\theta\cos\phi$   e que $y=r\sin\theta\sin\phi$.
- E temos então $|\vec E(\vec r)|=\frac{Q}{4\pi\varepsilon_0 r^2}$. Assim vemos que o campo não depende de $\theta$ nem de $\phi$, apenas de $r$.
- Temos então que $|\vec E(\vec r)|^2=\frac{Q^2}{16\pi^2\varepsilon_0^2 r^4}$
- De seguida substituimos $r^2=x^2+y^2+z^2$. No entanto, isto é muito chato porque vai dar uma integral tripla muito trabalhosa com $dV=dxdydz$
- Assim, o melhor a fazer é passar $dV$ a coordenadas esféricas:
![[dV cords esféricas]]
- Primeiro devemos de notar que a figura acima não está à escala e que consideramos que as dimensões da unidade de volume $dV$ são tão reduzidas que é quase como se os lados deste "paralelepípedo" não fossem curvos. Assim, obtemos que $$dV=r^2\sin\theta ~d\theta d\phi dr$$
- E assim se tem que:
$$\begin{align}
U=\int_{\text{todo o espaço}} |\vec E(\vec r)|^2dV &=\int_a^\infty\frac{Q^2}{16\pi^2\varepsilon_0^2 r^4}r^2dr\int_0^\pi\sin\theta d\theta\int_0^{2\pi}d\phi=\\
&= \int_a^\infty\frac{Q^2}{16\pi^2\varepsilon_0^2 r^2}dr~\cdot~2~\cdot2\pi=\\
&= \frac{Q^2}{4\pi\varepsilon_0^2}\int_a^\infty\frac{1}{r^2}dr= \frac{Q^2}{4\pi\varepsilon_0^2}\left[\frac{-1}{r} \right]_a^\infty=\\
&= \frac{Q^2}{4\pi\varepsilon_0a}
\end{align}$$
- E desta forma se obtem 
$$U=\frac{\varepsilon_0}{2}\frac{Q^2}{4\pi\varepsilon_0a}=\frac{Q^2}{8\pi\varepsilon_0a}$$
- E esta é a energia que foi gasta para formar esta distribuição de carga.

### Cargas pontuais são impossíveis
- Imaginemos agora que vamos diminuindo cada vez mais o rio $a$. Teríamos que $a\to0$ e $U\to\infty$.
- No entanto, energia infinita é impossível.
- Ou seja, como uma superfície esférica de raio 0 é na realidade uma carga pontual, isto significa que, para o Eletromagnetismo clássico, **cargas pontuais são impossíveis/não existem**.

- Mas sendo assim, porquê que ao estudar a energia de um sistema de cargas pontuais não obtivemos energia infinita? Porque já tínhamos as cargas, só as metemos no sistema e estudamos a energia da interação entre elas. 


## Condutores
- A diferença entre isoladores e condutores reside na forma como permitem ou não o *movimento de cargas*: condutores permitem e isoladores não.
- Isto é causado pela **resistividade**, $\rho$, e **condutividade**, $\sigma$. Tem-se que: $$\sigma=\frac1\rho$$
- E para um *isolador ideal* temos que $\sigma=0,~\rho=\infty$.E para um *condutor ideal* temos que $\sigma=\infty,~\rho=0$.

- Imaginemos que se tem um condutor (por exemplo um metal). Nele, como é um condutor, as cargas podem-se mover livremente. No entanto, o seu movimento é tão aleatório que é como se não houvesse Corrente elétrica.
- Assim, se $I=0$, então $d\phi=0$ e então $\phi$(potencial elétrico) é constante. E como $\phi=-\int E$, então **o campo no interior é 0**.
- Deste modo, se houver excesso de carga, *a carga tem de estar na superfície do condutor*.

-- ***Mas porquê?*** --
1. Se houvesse carga no interior, os eletrões iriam-se repelir uns aos outros e eventualmente eles iriam até à superfície. Prova: $U=\frac{Q^2}{8\pi\varepsilon_0a}$. Ou seja, se $a$ aumentar, $U$ diminui e portanto atinge-se o mínimo de energia se as cargas estiverem na superfície.
2. Se $\vec E=\vec 0$ no interior, então $\Phi=∯\vec E\cdot \hat n~ds=0$ para qualquer superfície contida no condutor. Logo, pela lei de Gauss, $q_{int}=0$.

#em1 #potencialE #fisica 