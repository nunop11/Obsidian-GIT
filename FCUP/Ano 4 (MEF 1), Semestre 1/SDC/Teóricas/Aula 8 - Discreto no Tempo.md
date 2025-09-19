## Tipos de Sinais
- Temos sinais...
    - Contínuos no tempo
    - Discretos no tempo
    - Analógicos
    - Digitais
    - Que correspondem a sampled-data
    - Quantized

- Mas, mais concretamente eles podem ser representados com esta matriz:
![[sdc_5|800]]

- Ora, até agora vimos sinais/sistemas do tipo "analógico". Vamos agora coemçar a ver sistemas do tipo "sampled-data".

**Sistema Analógico**
- O sistema é descrito por um sistema de *equações diferenciais*:
$$\begin{cases}
\dot{x}=Ax+Bu \\
y=Cx+Du
\end{cases}$$
e usamos a *transformada de Laplace*:
$$\begin{align*}
sX(s)&= AX(s)+BU(s)\\
Y(s)&= CX(s)+DU(s)
\end{align*}$$

**Sistema Discreto no tempo**
- O sistema é descrito por um sistema de *equações algébricas*:
$$\begin{cases}
x_{k+1}=Ax_{k}+Bu_{k} \\
y_{k}= Cx_{k}+Du_{k}
\end{cases}$$
e usamos o *domínio z*:
$$\begin{align*}
zX(z)&= AX(z)+BU(z)\\
Y(z)&= CX(z)+DU(z)
\end{align*}$$