# 14 - Método de Newton para 2+ Variáveis
- Tendo um sistema de $N$ equações, de $N$ variáveis, começamos por o escrever da forma:
$$\begin{cases}f_{1}(x_{1},x_{2},\dots,x_{N})=0 \\ f_{2}(x_{1},x_{2},\dots,x_{N})=0\\ \quad\quad\vdots\\f_{N}(x_{1},x_{2},\dots,x_{N})=0
\end{cases}$$
- Consideremos que a solução verdadeira do sistema é $x_{1}^{*},x_{2}^{*},\dots,x_{N}^{*}$. Podemos fazer a expansão em Taylor:
$$f_{i}(x_{1}^{*},\dots,x_{N}^{*})=f_{i}(x_{1},\dots,x_{N}) + \sum\limits_{j}(x_{j}^{*}-x_{j}) \frac{\partial f_{i}}{\partial x_{j}}+\dots$$
que, na forma matricial, pode ser escrito como:
$$\mathbf{f}(\mathbf{x}^{*})=\mathbf{f}(\mathbf{x}) + \mathcal{J}\cdot(\mathbf{x}^{*}-\mathbf{x})+\dots$$
sendo:
- $\mathbf{f}$ - lista das $f_{1},\dots,f_{N}$ funções do sistema
- $\mathbf{x^{*}}$ - lista dos zeros $x_{1}^{*},\dots,x_{N}^{*}$ do sistema
- $\mathbf{x}$ -  lista dos valores das variáveis $x_{1},\dots,x_{N}$
- $\mathcal{J} \longrightarrow J_{ij}=\frac{\partial f_{i}}{\partial x_{j}}$ - Matriz *Jacobiana* $N \times N$

- Por definição de zero de uma função, $\mathbf{f}(\mathbf{x}^{*})=0$
- Se definirmos $\Delta \mathbf{x}=\mathbf{x}-\mathbf{x}^{*}$ e ignorarmos os termos acima da 1ª derivada temos:
$$\mathcal{J}\cdot \Delta \mathbf{x}=\mathbf{f}(\mathbf{x})$$
- De realçar que, em computacional, a matriz jacobiana acima consiste em calcular todas as derivadas em $\mathbf{x}$.
- Isto não passa de um sistema $Ax=v$. Podemos usar qualquer um dos métodos anteriores e obter $\Delta \mathbf{x}$.
- Assim, e recordemos que $\mathbf{x}$ é apenas a 1ª tentativa, temos a próxima tentativa:
$$\mathbf{x}'=\mathbf{x} - \Delta \mathbf{x}$$

#computacional #programacao #anal2 