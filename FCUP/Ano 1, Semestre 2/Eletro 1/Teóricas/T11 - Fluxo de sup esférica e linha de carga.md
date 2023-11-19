# Eletro 1 - Aula teórica 11 (JAM)
- Como já vimos, se tivermos uma superfície esférica, de raio R, com uma carga pontual no seu centro, o módulo de campo na sua superfície é **sempre igual**, mas apenas se $\sigma$ for constante
- Temos ainda que $\vec E$ tem sempre direção e sentido radial, mas porquê?
    - Porque uma superfície é como se fosse uma combinação de aneis.

## Fluxo por superfície esférica
- Imaginemos agora que temos uma superfície esférica uniformemente carregada.
- Ora, temos que $\vec E\parallel\hat n$ e que $|\vec E|$ é constante em todos os pontos da superfície
- Assim, temos
$$\Phi=∯_\sum E\cdot\hat n~ds=E∯ds=E4\pi R^2=\frac{Q}{\varepsilon_0}$$
- Obtem-se ainda que $E(r)=\frac{Q}{4\pi\varepsilon_0 r^2}$
- Temos por fim que $$\vec E(\vec r)=\frac{Q}{4\pi\varepsilon_0|\vec r|^2}\frac{\vec r}{|\vec r|},~~r>R$$
- Nota-se ainda que se $r\gg R$,e ntão o campo comporta-se como se a esfera fosse uma carga pontual, mas não é esse o caso, claramente.
- Temos então:
![[descontinuidade superficial]]
- Assim, na superfície da superfície esférica temos uma **DESCONTINUIDADE SUPERFICIAL**. Ou seja, para $r=R$, o **Campo não está definido**
- De notar que hipoteticamente o campor $E(R^+)$ na superfície seria de $\Huge\frac{\sigma}{\varepsilon_0}$

### Linha carregada
- caso estudado na aula, com notas no caderno
- Basicamente, podemos definir uma superfície gaussiana que é um cilindro, cujo eixo de rotação é a linha de carga. Ao fazer isso, a normal das bases é perpendicular ao campo da linha, pelo que o fluxo aí é nulo. Assim, chega-se a 
$$\vec E(\vec r)=\frac{\lambda}{2\pi\varepsilon_0|\vec r|}\frac{\vec r}{|\vec r|}$$

#em1 #fluxoE #fisica 