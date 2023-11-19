# Campo auxiliar, $\vec{H}$
- Temos um material magnetizado. Podemos descrever a densidade de corrente neste como:
$$\vec{\mathcal{J}}=\vec{\mathcal{J}_{\ell}}+\vec{\mathcal{J}_{m}}$$
em que $\vec{j_{m}}=\nabla \times \vec{M}$ é a densidade de corrente de magnetização e $\vec{j_{\ell}}$ é a densidade de corrente livre, que é tudo o resto. Por exemplo, a figura da aula anterior com o material e os pequenos loops de corrente, a corrente nestes loops conta como corrente livre.

- Temos que a Lei de Ampere-Maxwell na Magnetostática é escrita como:
$$\nabla \times \vec{B}=\mu_{0}\vec{\mathcal{J}}$$
ora, ficamos com:
$$\frac{1}{\mu_{0}}(\nabla \times \vec{B})=\vec{\mathcal{J}_{\ell}}+\vec{\mathcal{J}_{m}}=\vec{\mathcal{J}_{\ell}}+\nabla \times \vec{M}$$
de onde vem:
$$\vec{\mathcal{J}_{\ell}}=\nabla \times\left(\frac{\vec{B}}{\mu_{0}}-\vec{M}\right)$$
- Onde definimos então o **Campo Auxiliar**:
$$\boxed{\vec{H}=\frac{\vec{B}}{\mu_{0}}-\vec{M}}$$
- Podemos então escrever:
$$\vec{\mathcal{J}_{\ell}}=\nabla \times \vec{H}$$
e se tomarmos a integral de área dos 2 lados:
$$\int (\nabla \times \vec{H})\cdot d\vec{s}=\int \vec{\mathcal{J}}_{\ell}\cdot d\vec{s} ~~\to~~ \oint \vec{H}\cdot d\vec{\ell}=I_{\ell}$$

- É portanto evidente que o papel de $\vec{H}$ na magnetostática é semelhante àquele de $\vec{D}$ na eletrostática. Ambos nos permitem escrever as leis de Gauss / Ampere a partir da carga / corrente livre.
- Aliás, na prática $\vec{H}$ verifica-se mais útil que $\vec{D}$. Nomeadamente em laboratório, $\vec{H}$ chega até a ser mais útil que $\vec{B}$, enquanto que nunca se fala em $\vec{D}$. 
    - Isto tem uma razão. Quando estamos a gerar um campo magnético normalmente temos bobinas, a que fornecemos uma corrente (corrente livre), daí usar $\vec{H}$. $\vec{B}$ já vai depender do material sujeito ao campo e as suas propriedades. 
    - No caso do campo elétrico, costumamos gerá-lo com uma DDP entre 2 placas, pelo que a corrente não importa e usamos logo $\vec{E}$. Se fosse mais fácil medir carga do que potencial, usariamos $\vec{D}$ invés de $\vec{E}$.

- Tal como tínhamos entre $\vec{E}$ e $\vec{D}$, para $\vec{B}$ e $\vec{H}$ também temos equações que parecem semelhantes e equivalentes. Mas não devemos interpretar isso muito diretamente.
- Mais croncretamente:
    - Temos a equação de ampere na magnetostática: $\nabla \times \vec{B}=\mu_{0}\vec{\mathcal{J}}$
    - E vimos acima que $\nabla \times \vec{H}=\vec{\mathcal{J}_{\ell}}$ 
    - Ora, apesar de parecidas estas equações não são equivalentes. Não podemos dizer algo tipo "o campo $\vec{H}$ é igual ao $\vec{B}$ mas com origem numa corrente diferente"
    - Prova disto é que, enquanto que $\nabla\cdot\vec{B}=0$, temos $$\nabla \cdot \vec{H}=\nabla \cdot \left( \frac{\vec{B}}{\mu_{0}}-\vec{M} \right)=-\nabla \cdot \vec{M}$$ pelo que apenas podemos comparar $\vec{B},\vec{H}$ diretamente quando $\nabla\cdot\vec{M}=0$.

### Condições de Fronteira
- Temos $\nabla\cdot\vec{H}=-\nabla\cdot\vec{M}$ logo:
$$\hat{n}\cdot(\vec{H^{+}}-\vec{H^{-}})=-\hat{n}\cdot(\vec{M^{+}}-\vec{M- })$$
- E temos $\nabla \times \vec{H}=\vec{\mathcal{J_{\ell}}}$ de onde surge:
$$\hat{n}\times(\vec{H^{+}}-\vec{H^{-}})=\vec{k_{\ell}}$$
(Um dia hei de deduzir)
- Estas condições de fronteira são por vezes mais úteis que as do campo $\vec{B}$.

## Meios Magnéticos Lineares e Isotrópicos
- Meios magnéticos lineares são aqueles em que:
$$\vec{M}=\chi_{m}\vec{H}$$em que $\chi_{m}$ é a *suscetibilidade magnética* (é positiva para materiais paramagnéticos e negativa para diamagnéticos)

- Podemos então escrever:
$$\hat{H}=\frac{\vec{B}}{\mu_{0}}-\vec{M}\to \vec{B}=\mu_{0}(\vec{H}+\vec{M})\to \vec{B}=\mu_{0}(1+\chi_{m})\vec{H}=\mu\vec{H}$$
em que temos a *permeabilidade do meio* $\mu$.

- Se o meio for homogéneo teremos $\chi_{m}$ constante. Daqui surge:
$$\nabla\cdot\vec{M}=\chi_{m}\nabla\cdot\vec{H}$$
usando $\nabla\cdot\vec{H}=-\nabla\cdot\vec{M}$ e fica:
$$(1+\chi_{m})\nabla\cdot\vec{M}=0\to\nabla\cdot\vec{M}=0$$
logo, se o meio é isotrópico temos $\nabla\cdot\vec{M}=0$
- De realçar novamente que, apesar de agora termos $\vec{M},\vec{H}\propto\vec{B}$, não é garantido que a divergência de $\vec{B}$ vai ser zero quando a dos outros 2 o é.

## Ferromagnetismo
- Num meio linear, os dipolos magnéticos alinham-se devido à presença de um campo magnético externo. Já os materiais ferromagnéticos não são lineares e não requerem um campo externo para manter a sua magnetização: o alinhamento dos dipolos é fixo.
- A caraterística que difere ferromagnetismo de paramagnetismo é que os dipolos têm uma tendência para apontar na mesma direção que os vizinhos. Ora, esta tendência é tão forte que quase 100% dos dipolos estão alinhados. No entanto, nem todos os materiais deste tipo são ímans por razões muito bem explicadas no Griffiths :D
![[Pasted image 20231115214510.png]]
