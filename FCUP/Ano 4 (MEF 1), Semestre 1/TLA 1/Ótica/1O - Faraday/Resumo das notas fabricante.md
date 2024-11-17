![[montagem t1o v2.png]]
![[montagem t1o v1.png]]
- Vamos usar um laser. Assim, o feixe já está polarizado e não temos polarizador
- Invés de um plano translúcido, ligamos a um oscilocópio (acho eu)

## Objetivos
- Medir campo B com o teslamometro. Medir campo B VS corrente. --- Acho que estes não vamos poder fazer. Já nos vão dar forma de obter B sabendo a corrente.
- Determinar ângulo de rotação em função do campo B. Calcular a constante de Verdet com os dados
- Se possivel, estudar constante de Verdet VS comprimento de onda

## Set-Up
- Montar conforme figuras acima
    - No lab teremos um laser invés de uma lâmpada com filtros de cor. AKA poderemos só ter 1 comprimento de onda
    - As bobinas estão em série
- A amostra tem ~30mm e é colocada nos 2 orifícios do suporte das Bobinas. 
1. Ligar o laser e mover o alvo até a imagem ser visível 
2. Colocar o eletromagnet/amostra no percurso ótico, de modo que os buracos estejam alinhados com o feixe ótico
3. Como sabemos, conforme se roda o analisador, a intensidade vai variando entre um máximo e um mínimo. Assim, para encontrar o ângulo de polarização precisamos de encontrar um deles:
    - O máximo corresponde ao ângulo de polarização
    - O mínimo faz 90º com a polarização
Como vamos ver tudo num osciloscópio, devemos procurar sempre o **mínimo** - o máximo vai fazer com que tenhamos menos resolução.
4. Ir variando a corrente (e campo). Em cada valor, rodar analisador até ter o mínimo e registar o ângulo.

## Teoria
### Conceito / Na prática
- Quando temos uma onda EM polarizada a passar num meio transparente em que temos um campo magnético, a polarização *roda*. Isto é o **efeito de Faraday**
- Vamos então ter uma amostra transparente num iman
    - Consoante passa corrente no eletromagnet e se gera campo magnético, a polarização do feixe de luz roda na direção de oscilação.
- Podemos ainda trocar as ligações das bobinas, o que inverte a corrente e o campo.

- Temos aqui o campo gerado para várias correntes, ao longo da amostra:
![[B vs dist em amostra.png]]
(isto quando não temos amostra nem feixe, isto é só medição do campo)

- Vemos que temos o campo máximo na gap entre as 2 bobinas. Assim, consideramos que a amostra (no centro da gap) estará sujeita a este campo:
![[B vs I medio.png]]

- Ou seja, o que se observa é:
    - Começamos com o analisador a anular o feixe (polarização perpendicular). No alvo teríamos escuridão ou quase
    - Depois ligamos a corrente. A polarização roda, então o analisador deixa de anular tudo, então apareceria luz.

### Fórmulas
- Imaginemos agora isto
    - Temos por exemplo $I=1A$ e o analisador num ângulo: "posição 1"
    - Invertemos a corrente: $I=-1A$
    - Ao corrigir o analisador para voltar a anular o feixe teremos de o rodar para o lado oposto, ficando este numa "posição 2"
- A diferença de ângulo entre as posições 1 e 2 é $2\Delta\phi$
- Podemos fazer a relação $\Delta \phi(B)$ e temos uma relação linear, o $\Delta \phi$ aumenta com o campo.
- Também se pode demonstrar que $\Delta \phi$ é linear com o comprimento da amostra $l$
- Podemos dizer então:
$$\Delta \phi \sim Bl$$
 e a constante de proporcionalidade é a **constante de Verdet**: $V$
 $$\Delta \phi= VlB~~\to~~ V = \frac{\Delta \phi}{lB}$$
- $V$ depende de $\lambda,n(\lambda)$ e tem unidades $\frac{\text{grau}}{\text{T m}}=\frac{\text{radiano}}{\text{T m}}$
- Temos ainda a relação empírica:
$$V(\lambda)=\frac{\pi}{\lambda} \left(\frac{(n(\lambda))^{2}-1}{n(\lambda)} \right)\left(A + \frac{B}{\lambda^{2}-\lambda_{0}^{2}}\right)$$








