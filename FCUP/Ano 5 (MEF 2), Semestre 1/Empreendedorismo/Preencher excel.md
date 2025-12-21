## Working Capital
### Days sales outstanding (DSO)
- *Tempo médio (dias) que a empresa demora a receber dinheiro de venda*
- Isto representará a eficiencia do negócio e os canais que temos disponíveis para venda. Assim, o melhor será considerar um número maior nos primeiros anos e depois descer
- A fórmula completa é:
$$\text{DSO} = \frac{\text{contas a receber}}{\text{vendas totais}}\times \text{\# dias}$$
- Casos:
    - vendas website - 1 dia
    - vendas pagas por transferencia - 7+ dias
    - vendas B2B - 30+ dias, pode ter contratos mais longos

- Considerei (por recomendação do chat):
    - 2025, 2026 - 30 dias
    - 2027... - 15 dias

### Days Inventory Outstanding (DIO)
- *Tempo médio (dias) que a empresa mantém um produto em stock até o vender*
- Um valor mais baixo indica que vendemos o stock mais rápido e teremos maior fluxo de vendas, MAS também teremos de ter produção mais acelerada
- Fórmula:
$$\text{DIO} = \frac{\text{valor médio do stock}}{\text{custo dos produtos vendidos}}\times365 ~~~~(\text{média anual})$$
- Meti produto 1 : 60 dias. Isto assume que não vendemos demasiado rápido mas que temos um stock decente.
    - Poderíamos descer nos últimos anos, considerando que há evolução da nossa supply chain.
- Meti o produto 2 a zeros, porque só temos 1 produto físico (caixa), no caso das subscrições o conceito de stock não se aplica. Mas não sei se zeros foi boa ideia porque isso implica que o sotck se vende logo?

### Days Payables Outstanding (DPO)
- *Tempo médio (dias) que a empresa demora a pagar a fornecedores*
- Do que vi na net, em Portugal costuma ser 30-60 dias. Mas o mais normal é 30. Meti 60 para considerar um inicio mais lento.

## Revenue Stream
### Revenue produto 1 : caixa
- Como é uma peça de hardware que temos de fabricar, as margens serão as mais baixas
- Notemos que esta componente apenas contem a parte de **venda a famílias**. Tendo em conta o TAMSAMSOM, nos primeiros 5 anos consideramos que seria possivel vender caixas a 4% do mercado, ou seja: 0.04x1.77M = 70k caixas
- Decidimos ainda que cada unidade custaria 30€. Dividimos por 5 porque temos 5 anos de garantia, logo se comprei uma caixa agora, não comprarei outra por 5 anos.

### Revenue produto 2 : app premium
- Este é um rendimento **mensal** e que terá margens muito maiores, já que os únicos custos são a manutenção e atualizações da app.
- Decidimos que custaria 6€ por mês
- Em termos de números, considerei o que vimos no TAMSAMSOM, tendo-se que 20% dos clientes que comprem a caixa também compraram a subscrição.
    - Na tabela considerei que esta percentagem irá subir lentamente nos últimos anos 

### Serviço : aluguer e dashboard para lares
- Considerei isto um serviço porque é algo continuado e em que teremos de fazer manutenção. Além disso, esta componente implica deslocamento de técnicos a lares para fazer manutenção de caixas e apoio técnico e cenas
- Terá ainda a menor revenue de longe.
- Vimos que aqui temos um preço de 4€ / 10 utentes / mês
- No TAMSAMSOM consideramos que, nos primeiros 5 anos conseguiríamos alcançar 6% do mercado de lares em Portugal. Ou seja, venderíamos ao equivalente de 0.06x100k = 6k clientes (6k idosos em lares teriam acesso à app)
    - Ao converter isto em número de servicos, vemos que é preciso vender 6000/10 = 600 servicos nos primeiros 5 anos.

## Gross Margin
### Gross Margin : 
- Definida como:
$$\text{Gross Margin} = \frac{\text{Revenue} - \text{COGS}}{\text{Revenue}} \times100$$
em que $\text{COGS} = \text{Cost of Goods Sold}$

### Produto 1 : caixa
- Do que vi online, para produtos inteligentes em empresas de reduzida escala, as margens costumam rondar 20-40%. Consideremos 20%. 
    - Na tabela considerei que esta vai subindo nos últimos anos, consoante se melhora a supply chain e os métodos de fabrico
- Notemos que com cada caixa a ser vendida a 25€, isto significa que cada uma custa 20€ a ser fabricada

### Produto 2 : app
- Consideremos uma margem de cerca de 70% (vi online que 70-80% é um range comum para produtos software)
- Com cada subscrição a custar 3€ mensais, temos que 0.9€ por mês por subscrição são gastos em despesas de manutenção

### Margem de Serviços: lares
- Em termos de margens, considerei que serão parecidas às da aplicação, mas um pouco menores devido a custos de manutenção de caixas e dashboard. Considerei margens de 50%

### Perda inventário
- É o que o nome indica. Na internet vi que tipicamente em retalho ele ronda os 1-2%. Vamos ser pessimistas e meter 5% (em tudo acima escolhi a opção mais pessimista)

### Custo de distribuição
- Ronda os 5-10%. Coloquei 10%
- 