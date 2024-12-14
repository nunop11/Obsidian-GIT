## Linear State Feedback Controller 
- Temos um sistema LTI (linear time indep), descrito por
$$\begin{cases}
\dot{x}=Ax+Bu \\
y=Cx
\end{cases}~~~~(x\in \mathbb{R}^{n},y\in\mathbb{R}^{k},u\in \mathbb{R}^{m}~;~n,k,m\in\mathbb{N})$$
que tem o polinómio caraterístico:
$$p(\lambda)=\lambda^{n}+\sum\limits_{i=1}^{N}a_{i}\lambda^{n-i}=\prod_{i=1}^{n}(\lambda+p_{i})$$

### Feedback
- Como vimos no início da UC, usar um sistema de feedback é normalmente a melhor forma de obter controlo. Vamos então introduzir um feedback:
![[sdc_4|1000]]
- Assim, introduzimos a alteração $u=-Kx$ tal que ficamos com
$$\dot{x}=(A-BK)x$$
- Ora, ao fazer isto podemos *forçar polos* no sistema. Ou seja, podemos forçar um certo polinómio caraterístico:
$$\overline{p}(\lambda)=\prod_{i=1}^{n}(\lambda+\overline{p}_{i})$$
**EXEMPLO**
- Consideremos $$A=\begin{pmatrix}0 & 1 & 0 \\ 0 & 0 & 1 \\ -6 & -11 & -6\end{pmatrix}\quad;\quad B=\begin{pmatrix}0 \\ 0 \\ 1\end{pmatrix}\quad;\quad C=\begin{pmatrix}0 & 0 & 1\end{pmatrix}$$
o polinómio caraterístico é:
$$p(s)=\det(sI-A)=s^{3}+6s^{2}+11s+6$$
- Introduzimos um sistema de feedback com $$K=\begin{pmatrix}k_{1} & k_{2} & k_{3}\end{pmatrix}$$
- Ora, o polinómio caraterístico do sistema de feedback será:
$$\overline{p}(s)=\det(sI-(A-BK))=s^{3}+ (k_{1}+6)s^{2}+(k_{2}+11)s+(k_{3}+6)$$

- Queremos então forçar no sistema os polos -3,-4,-5. Ou seja, queremos que:
$$\begin{align*}
\overline{p}(s)&= (s+3)(s+4)(s+5)\\
&= s^{3}+12s^{2}+47s+60
\end{align*}$$
ao igualar cada termos obtemos:
$$k_{1}=6~~,~~k_{2}=36~~,~~k_{3}=54$$
ou seja:
$$K=\begin{pmatrix}6 & 36 & 54\end{pmatrix}$$

