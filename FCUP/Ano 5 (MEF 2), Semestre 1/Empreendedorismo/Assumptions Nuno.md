## Working capital
### Days sales outstanding
- Em portugal é 60: https://bpstat.bportugal.pt/serie/12587225
- Este valore é alto, mas é o que é

### Days inventory outstanding
- Para product 2 meti zero dias, o produto 2 é software. Não existe stock
- Para produtos de saúde é comum temos DIO de vários meses para evitar rutura de stock, já que a produção e regulação são mais lentos. Podemos ter DIO acima de 150 dias
- Em produtos de eletrónica de retalho temos menos DIO, os produtos podem ser quase feitos consoante são encomendados e não existe regulamentação, tendo-se DIO na ordem de 30-40 dias
- Para o caretracker considerei um meio termo: 60 dias. Coincide ainda com o DSO

### Days payables outstanding
- Em portugal o tempo médio de pagamento entre empresas (B2B) é 60 dias (https://single-market-scoreboard.ec.europa.eu/countries/portugal_en)

## Revenue 
- Em qualquer site vemos o CAGR em $n$ anos:
$$\text{CAGR} = \left( \frac{\text{Vendas finais}}{\text{Vendas iniciais}} \right)^\frac{1}{n}-1$$
e podemos inverter a fórmula:
$$\begin{align*}
\text{CAGR} &=  \left(\frac{\text{TAM}_{0}}{\text{TAM}_{n}}\right)^{\frac{1}{n}}-1\\
\frac{\text{TAM}_{n}}{\text{TAM}_{0}}&= (1+\text{CAGR})^{n}\\
\text{TAM}_{n}&= \text{TAM}_{0}(1+\text{CAGR})^{n}
\end{align*}$$
aplicando o CAGR do mercado de e-health em portugal: 6.9%, com um uma receita de 388.7M€

- Considerando que este CAGR se pode aplicar ao nosso TAM (**assumption forte**), podemos aplicar isto ao nosso problema, em que teremos as vendas no ano $n$:
$$V(n) = \text{TAM}_{n}\cdot \alpha(n)$$
em que $\alpha(n)$ é a nossa curva de adoção. (https://www.wallstreetprep.com/knowledge/top-down-forecasting/ mostra que podemos aplicar uma fórmula deste tipo)
- Estimamos este TAM : $\text{TAM}_{0}=138.88\text{M€}$
- Assim teremos:
$$V(n) = 138.88 \cdot(1.069)^{n}\alpha(n) ~~~~(\text{M€})$$

- Logo, pretendemos que:
$$\alpha(n=5) = 1.09\%$$
- Ora, podemos modelar a nossa curva de adoção usando a **curva de Gompertz**, algo aplicado na área de saúde parare representar a adoção lenta inicial, devido a testes, regulações, etc (https://www.sciencedirect.com/science/article/abs/pii/S1386505618300455)
$$\alpha(t)=L e^{-be^{-ct}}$$
em que $L$ é o nosso valor assintótico do SOM. Temos que definir $b,c$ de forma a modelar o crescimento corretamente. Como o meu objetivo é determinar as vendas em cada ano, vamos definir um $L$ para cada produto e considerar $b,c$ sempre iguais

- Vamos ver como calculamos o $L$, conforme as estimativas do TAMSAMSOM:
    - Para as caixas temos:
        - O TAM das caixas é 7.6% do TAM 0
        - Consideramos 40% de adoção. O SOM é 10% do SAM
        - Temos $L=7.6\% \cdot 40\% \cdot 10\%=0.3\%=0.003$
    - Para a subscrição na app temos:
        - O TAM da subscrição é 91.7% do TAM 0
        - Consideramos 8% de adoção (20% dos 40% da caixa). O SOM é 10% do SAM
        - Temos $L=91.7\% \cdot 8\% \cdot 10\%=0.7\%=0.007$
    - Para os lares:
        - O TAM dos lares é 0.3% do TAM0
        - Consideramos 60% de adoção. O SOM é 10% do SAM
        - Temos $L=0.3\% \cdot 60\% \cdot 10\%=0.02\%=0.0002$

- Ou seja, temos:
$$\text{Revenue}(n) = 138.88(1.069)^{n}\cdot\underbrace{Le^{-35e^{-1.1n}}}_\text{taxa adoção}$$

## Gross margin
### Margens
- Vi online em diversas fontes que: 
    - margens para produtos de eletronica rondam 30%, devido aos custos de componentes e fabrico. Meti 20% para ter uma estimativa pessimista
    - margens para produtos de software são bem maiores, não temos tantos custos de desenvolvimento, tendo-se apenas custos de servidores e manutenção. Consideremos 70%
    - para o serviço aos lares meti 50%, como um meio termo, porque combina os 2 casos acima

### Outros custos
- Para perda de inventário
    - https://axonify.com/blog/retail-shrinkage/ - a percentagem costuma rondar 1-2%
    - Para uma estimativa muito pessimista, meti 5%
- Para custos de distribuição
    - vi muitos valores diferentes, desde 5 a 30%
    - Meti 10% como um valor médio

