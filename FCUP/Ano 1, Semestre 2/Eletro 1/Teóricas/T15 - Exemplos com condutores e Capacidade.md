# Eletro 1 - Aula teórica 15 (JAM)
- Vimos na aula anterior que um meio condutor eletroestático é um meio em que $I=0$ e que portanto $E_{int}=0$ e que assim, qualquer excesso de carga no condutor estará na sua superfície.
- Vimos ainda que isto pode ser verificado pela Lei de Gauss, porque qualquer superfície contida no condutor terá fluxo nulo e então a carga interna será também nula.
- Tem-se então:
![[dist carga condutor]]
em que $\sigma$ não é necessariamente uniforme. 

E então tem-se:
- $\vec E(P)$, num certo ponto $P$ *muito perto da* superfície do condutor é normal a esta.
- E assim, como vimos no resumo T8, $$E(0^+)-E(0^-)=\frac{\sigma}{\varepsilon_0}$$
- E, neste caso, $E(O^-)$, por estar dentro do condutor é igual a 0. Assim:
$$\Vert\vec E(P)\Vert=\frac{\sigma(P)}{\varepsilon_0}$$
- Assim, em conclusão:
    - No **interior** do condutor, $E=0$ e $\phi$ é constante.
    - **Na** superfície em si, há uma descontinuidade de campo.
    - **Mesmo junto** à superfície, o campo é normal à superfície.

### Condutor de carga nula
- Imaginemos que temos um condutor com carga nula. Ou seja, teríamos de ter:
![[condutor q=0]]
- As cargas teriam de se mover de forma a criar um polo positivo e negativo no condutor, mas de modo que a carga total seja nula. Ora, estes dois polos criariam um campo $\vec E_1$, do positivo para o negativo.
- No entanto, já vimos que o campo dentro do condutor é nulo, de forma que teria de existir um campo $\vec E_0$ de modo que $E_0+E_1=0=E_{int}$

### Condutor com cavidade
- Imaginemos agora um condutor que tem uma cavidade no seu interior, sem cargas nela:
![[cond cavidade]]
- Foquemo-nos nos pontos $A$ e $B$. Temos que $V_A=V_B$, pelo que a DDP será **sempre 0**.
- Ou seja, qualquer integral do campo $E$ entre A e B irá dar 0. Ou seja, ***não há campo na cavidade***.
- A isto se chama Gaiola de Faraday.

### Condutor com cavidade com carga dentro
- Temos agora um condutor como no caso acima, mas agora o condutor tem carga não nula e existe uma carga pontual $q_c$ no interior da cavidade:
![[cond cavidade carga]]
- Como neste caso a carga do condutor não é nula, a carga distribui-se pelas duas superfícies, interior e exterior.
- Assim, se fizermos uma superfície gaussiana que englobe a cavidade e esteja dentro do volume do condutor, temos que $E_{int}=0$, porque o campo no volume é 0 e na cavidade, como vimos anteriormente, também é 0.
- Assim, conclui-se que então $\Phi=0$ e assim $q_{int}=0$
- Como tal, a carga da superfície interior terá de ser $-q_c$ para anular a carga pontual no centro.

### Condutor esférico
- Tal como tinhamos para superfícies de carga, $$\vec E(r>a)=\frac{Q}{4\pi\varepsilon_0r^2}\hat r\quad\quad V(r>a)=\frac{Q}{4\pi\varepsilon_0r}$$
- E temos ainda que $$V(r=a)=\frac{Q}{4\pi\varepsilon_0a}=V(r<a)$$

## Capacidade de condutor esférico de raio a
- A capacidade de um condutor é obtida com 
$$C=\frac{Q}{V}$$
- Sendo $Q$ a carga do condutor e $V=\frac{Q}{4\pi\varepsilon_0a}$ o potencial na sua superfície. Assim se obtem que:
$$C=4\pi\varepsilon_0a$$
- De notar que a unidade de capacidade é o *Farad*, $1F=1CV^{-1}$. Normalmente só se usa $pF,nf,\mu F$

### Condutores em influência total
- Nota: **Influência total** ocorre quando temos 2 condutores, um dentro do outro, mas sem que eles estejam em contacto.
- Nesse caso, irá haver DDP e Campo E entre eles. Aí, $$C=\frac{Q}{\Delta V}$$

#em1 #condensador #fisica 