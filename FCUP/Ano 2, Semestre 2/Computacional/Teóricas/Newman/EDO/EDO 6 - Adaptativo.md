# 6 - Runge-Kutta Adaptativo
- Até agora, vimos casos com $h$ constante e predefinido pelo programador.
- Ora, podemos fazer o programa determinar o melhor valor de $h$ em cada passo. Por exemplo, consideremos o caso abaixo, em que queremos ter muitos pontos na parte de variação rápida:
![[rk4 adaptativo.png]]
- Para usar o método adaptativo temos 2 partes:
    - Determinar o erro dos nossos passos
    - Comparar com o erro desejado. Aumentar ou diminuir o $h$ conforme a observação.

1. Começando com $h$ reduzido (pelo sim pelo não), usar o método de Runge-Kutta como normalmente e obter os *2 primeiros pontos*, ou seja, ficar com $x(t),x(t+h),x(t+2h)$.
2. Voltar ao início e usar um intervalo $h'=2h$. Determinar 1 ponto, que será $x(t+2h)$. Ou seja, temos 2 estimativas deste valor.

- O método de Runge-Kutta tem erro de ordem $h^{5}$. Ou seja, o erro de uma estimativa será $\sim ch^{5}$
    - Sendo $x(t+2h)$ o valor real do ponto
    - A nossa primeira estimativa (com $h$ original) irá ter a seguinte relação com o valor real: $$x(t+2h)=x_{1} + 2ch^{5}$$
    - A nossa segunda estimativa (com $h'=2h$) irá ter a seguinte relação com o valor real: $$x(t+2h)=x_{2}+ 32ch^{5}$$
    - Ao igualar as 2 equações acima temos: $x_{1}=x_{2}+30ch^{5}$. Ou seja: $$\varepsilon= ch^{5}=\frac{1}{30}(x_{1}-x_{2})$$
- E é este o erro que comparamos com o erro desejado, $\varepsilon_{0}$. Mas como?

- Assim, qual será o intervalo "perfeito"? Chamemos-lhe $h'$. O seu erro seria: $$\varepsilon'=ch'^{~5} =ch^{5}(\tfrac{h'}{h})^{5}= \tfrac{1}{30} (x_{1}-x_{2})^{5}(\tfrac{h'}{h})^{5}$$
- Ora, queremos que o erro de $h'$ seja o nosso erro desejado, $\varepsilon_{0}$. Ou seja, (tendo em conta que apenas importa o módulo do erro) queremos ter: $$\tfrac{1}{30}|x_{1}-x_{2}| (\tfrac{h'}{h})^{5}=h'\varepsilon_{0}$$
e temos
$$\boxed{h'=h \left( \frac{30h\varepsilon_{0}}{|x_{1}-x_{2}|} \right)^{\frac{1}{4}}=h\rho^{\frac{1}{4}}}$$

3. Ou seja, usamos as 2 tentativas para determinar a razão $\rho$. 
    - Se $\rho>1$, então temos uma precisão melhor que a desejada. Isso acaba por ser mau, porque indica que estamos a usar intervalos inferiores ao necessário. Assim, continuamos, passando para o ponto $x(t+2h)$, mas com um intervalo maior, que será dado com exatidão pela equação acima. Ao passar para a próxima tentativa, o valor de $x(t+2h)$ que consideramos é $x_{1}$!
        - Por mero acaso, podemos ter $x_{1}\simeq x_{2}$. Nesse caso $\rho\gg1$, pelo que o método iria falhar por completo. Assim, normalmente estabelecesse um valor máximo de $\rho$, normalmente $2$.
    - Se $\rho<1$, então temos uma precisão inferior ao desejado. Assim, repetimos o passo e voltamos a $x(t)$ mas agora com um intervalo $h'$ inferior, que também é dado pela equação acima. 

- Apesar do que possa parecer, este método frequentemente demora menos ou muito menos que o método normal de Runge-Kutta.

## 6.1 - Adaptativo com 2 variáveis
- Ficamos com
$$\varepsilon_{x}=\tfrac{1}{30}(x_{1}-x_{2}) \quad \quad;\quad \quad \varepsilon_{y}=\tfrac{1}{30}(y_{1}-y_{2})$$
- E agora, a forma como usamos a fórmula acima depende do caso:
    - Se $x,y$ forem coordenadas, o erro de um ponto $(x,y)$ será $\sqrt{\varepsilon_{x}^{2}+\varepsilon_{y}^{2}}$, pelo que é isso que colocamos em vez de $\tfrac{1}{30}|x_{1}-x_{2}|$ na equação de $h'$.
    - Por outro lado, se nalgum exercício tivermos 2 variáveis em que apenas o erro de uma importa, não consideramos sequer a outra no erro.

#computacional #programacao #eqs_difs 