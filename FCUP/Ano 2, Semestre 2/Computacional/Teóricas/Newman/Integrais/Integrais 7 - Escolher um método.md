# 10 - Como escolher o método
***Regra Geral :*** Integração de Romberg e Quadratura Gaussiana são os melhores métodos para integrar funções "bem comportadas" e suaves. Caso contrário, usar Simpson ou Trapézio. Isto porque apenas avaliamos funções nos sample points e nos métodos mais simples é muito mais eficiente aumentar o $N$.

Agora, um a um: 
- **Trapézio**
    - Eficiente mas menos exato
    - Bom para dados recolhidos na prática, funções "mal-comportadas" e dados com ruído.
    - Versão adaptativa pode ser útil.

- **Simpson**
    - Mais exatidão com os mesmos pontos que a Regra do Trapézio
    - Pode causar problemas ao usar com dados com ruído ou funções mal comportadas

- **Romberg**	
    - Melhor método com pontos de espaçamento uniforme.
    - Mau para funções que variem muito rápido, com ruído ou com singularidades. Isto porque este método usa muito poucos pontos.

- **Quadratura Gaussiana**
    - Muito exato com poucos pontos, mau para funções que variem muito rápido ou com ruído (semelhante a Romberg)
    - O método mais exato. Pode ser pouco eficiente.
    - O facto de usar pontos espaçados de forma não uniforme pode ser um problema.

#computacional #programacao #integrais 
