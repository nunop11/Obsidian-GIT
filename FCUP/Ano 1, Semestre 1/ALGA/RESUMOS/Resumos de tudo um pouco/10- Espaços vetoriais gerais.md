- Ver [[4- (Sub)espaços vetoriais]] para uma intro de espaços vetoriais (não sub-)

## Exemplos de espaços vetoriais
---- números complexos $\mathbb C$
Tendo $z=a+ib,~ a,b \in \mathbb R,~ i^2=-1$, tem-se que em R2 isso pode ser representado como $u=(a,b)$
- Se multiplicarmos z por um número real alpha, o resultado também poderá ser representado em R2, por $\alpha u =(\alpha a, \alpha b)$ 
- Se somarmos 2 numeros complexos, u e $w=\hat a+i\hat b$, o seu resultado poderá ser também representado em R2, por $u+\hat u=(a+\hat a, b+\hat b)$.
- Assim, C é um espaço vetorial 

---- espaço das formas quadráticas
Tendo $q=ax^2+bxy+cy^3, ~a,b,c\in\mathbb R$, tem-se que isso pode ser representado em R3 por $u=(a,b,c)$
- Se multiplicarmos q por um número real alpha, o resultado também pode ser represntado em R2 por $\alpha u= (\alpha a, \alpha b, \alpha c)$
- Se somarmos q a outra forma quadrática $\hat q$, a sua soma constinuará a poder ser representada em R2, como visto anteriormente para C.

---- polinómios na variável S
- representado por $\mathbb R [x]$
- Tendo $p=a_0+a_1x+a_2x^2+...+a_nx^n$ para algum n natural
- Verificando as operações de soma e multiplicação como fizemos nos exemplos acima, vemos que é de facto um espaço vetorial

---- funcções f, real de variável real
Tendo $V=\{f:\mathbb R \rightarrow \mathbb R\}$
- A soma verifica-se:
$$f+g=h ~~~~ H:R\rightarrow R ~~~~ h(x)=f(x)+g(x)$$
- A multiplicação também:
$$\alpha \in \mathbb R, ~~~~ \alpha f=h,~~~~ h:R\rightarrow R ~~~~ h(x)=\alpha f(x)$$
- O element nulo também:
$$0=f:R\rightarrow R\in V ~~~~ f(x)=0$$

> Esta demonstração aplica-se ao conjunto das funções reais de variável real que sejam contínuas e derivadas

---
## Coisas importantes
- Um subconjunto S de V gera V se todos os elementos deste poderem ser escritos como uma combinação linear de um número finito de elementos de S
- Um subconjunto é linearmente independente se $v_1,...,v_k \in V ~e~a_1,...,a_k \in \mathbb R$ e se tem:
$$a_1v_1+...+a_kv_k=0 \rightarrow a_1=a_2=...=a_k=0$$
- Um subconjunto S de V é base de V se for linearmente independente *e* gerar V.
- Um espaço vetorial V tem dim finita se contiver uma base com número finito de elementos. Assim, todas as bases de V têm o mesmo número de elementos que é a dimensão de V

# Transformações com polinómios
- Tendo os espaços vetoriais V e W, $L:V\rightarrow W$ é uma transformação linear se 
$$L(u+v)=L(u)+L(v) ~~~~e~~~~ L(\alpha v)=\alpha L(v)$$

Exemplo:
![[exemplo1.png]]
- Se $T:V\rightarrow W$ for uma transformação linear
    - T(0)=0
    - O núcleo de T é um subespaço de V
    - $Im(T)=\{w\in W: \exists~ v\in V: T(v)=w\}$ é a imagem de V
    - Se T é injetiva, ker(T)={0}
    - Se T tem inversa $T^{-1}: W \rightarrow V$, ker(T)={0} e Im(T)=W
    - T fica determinada pelos seus valores em uma base de V

- T é um **isomorfismo** se tiver uma inversa linear, ou seja, se existir $S:W\rightarrow V, S=T^{-1}$ tal que
$$S(T(v))=v ~~~~e~~~~ T(S(w))=w~~~~v\in V, w \in W$$
- Also, para T ser um isomorfismo, $dimV=dimW$
- Exemplo:
![[exemplos.png]]

#espaços_vetoriais #alga 