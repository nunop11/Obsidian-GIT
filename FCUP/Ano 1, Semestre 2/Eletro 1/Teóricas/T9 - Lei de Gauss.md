# Eletro 1 - Aula teórica 9 (JAM)
- Na aula anterior obtivemos que $Q=(\vec v\cdot\hat n)\Delta S_1$
- Ora, aqui consideramos apenas os vetores que estão definidos/aplicados **na sup Delta S1**. Tudo o que está atrás não importa.
- De notar ainda que $\Delta S_1$ é plana e portanto o vetor normal, n, é o mesmo em toda a superfície. No exemplo da torneira, fez-se ainda a aproximação que todas as partículas se movem todas com a mesma velocidade
- No entanto, num caso real, em vez de $\vec v\cdot\hat n$, teríamos $\large\vec v(\vec r)\cdot\hat n(\vec r)$
![[v e n em sup nao plana]]
- Assim, temos o **fluxo** de um certo campo por uma dada superfície.
- Para começar temos
$$d\phi=\vec v(\vec r)\cdot\hat n(\vec r)\cdot ds$$, de notar que, apesar de a superfície em estudo ser curva, consideramos que $ds$ é uma superfície de área tão pequena que é quase como se fosse plana
- Deste modo temos:
>$$\huge\Phi=\iint_\Sigma~\vec v(\vec r)\cdot\hat n(\vec r)ds$$

---
EX
- Imaginemos que temos uma carga pontual. Para 3 posições ($\vec r_1,~ \vec r_2,~\vec r_3$) temos o campo assim:
![[campos carga pontual]]
- De realçar que, para este exemplo, é **vital** que $|\vec r_1|=|\vec r_2|=|\vec r_3|$
- Assim, temos que $|\vec E_1|=|\vec E_2|=|\vec E_3|$
- Desta forma podemos definir uma superfície esférica, a que chamaremos $\Sigma$. 
- Ora, queremos determinar $\Phi$ em $\Sigma$.
- Temos, numa secção da sup esférica:
![[fluxo sup esferica]]
- Assim temos
$$d\phi=\vec E(\vec r)\cdot\hat n(\vec r)ds$$, no entanto, no campo/fluxo em estudo, temos que $\vec E\parallel\hat n$, pelo que $d\phi=E(\vec r)ds$
- Deste modo, temos que:
$$\Phi=∯E(\vec r)ds$$
Ora, como $E(\vec r)$ é o módulo do campo então é um escalar. $ds$ é uma área. Assim, $E(\vec r)$ pode sair fora da integral:
$$\Phi=E(\vec r)∯ds$$
Ora, $∯ds$ é apenas a área da superfície fechada: $A_{\text{sup~esferica}}=4\pi R~^2$. Então:
$$\Phi=4\pi R^2E(\vec r)$$
Como $E(\vec r)=\frac{1}{4\pi\varepsilon_0}\frac{q}{R^2}$, muitos dos elementos se vão anular. Ficamos então com:
>$$\Huge\Phi=\frac{q_{\text{int}}}{\varepsilon_0}$$

- E assim chegamos à primeira lei de EM1: a ==*LEI DE GAUSS*==
- Esta declara que, para uma superfície fechada, o fluxo é sempre proporcional à carga dentro dela.
- Daqui tomamos algumas conclusão:
    - Se a carga total dentro da superfície for 0, não há fluxo. Para ajudar, podemos imaginar ou desenhar as linhas de campo. Vemos que *todas* elas começam E acabam dentro da superfície. Logo, nada flui, tudo o que sai volta a entrar, e vice-versa.
    - A **carga fora da superfície não importa para o fluxo**. Na aula foi mostrado um exemplo disto. A carga fora irá influenciar todos os vetores Campo no espaço, mas *não o fluxo*.
    - A **superfície é arbitrária**. Ou seja, a lei de gauss aplica-se a todas as superfícies, desde que sejam fechadas. Podem ser esferas, cubos, linhas, aneis, discos, etc.
    - Vemos ainda que, independentemente do formato e tamanho da superfície, desde que a carga dentro dela seja a mesma, o Fluxo também será o mesmo.

#em1 #gauss #fluxoE #fisica 