# Bottom up
## Dados
- 77% dos idosos acima de 65 anos toma varios medicamentos (https://pmc.ncbi.nlm.nih.gov/articles/PMC11493025 - 2019) x 24% da população tem >65 anos (https://www.jn.pt/nacional/artigo/um-quarto-da-populacao-ja-tem-65-ou-mais-anos/17753604 - 2025) x 10749635 portugueses (PORDATA 2024) = 1 986 533 "clientes" em Portugal
- 2622 lares em portugal (https://executivedigest.sapo.pt/mais-de-96-dos-lares-em-portugal-estao-lotados-idosos-esperam-ate-tres-anos-por-vaga - 2025)
    - APARTE nesta fonte: menos de 10% dos lares tem enfermeiros permanentes!!!
- 105 mil camas para idosos (https://www.forbespt.com/residencias-para-idosos-oferta-de-104-mil-camas-e-insuficiente-para-dar-resposta-a-procura - 2024) 
    - Os 2 pontos acima dão cerca de 40 utentes por lar

### TAM
#### Lares
- Nesta parte assumimos que todos os lares aderem e grande parte das famílias também
- Subscrição mensal do software institucional + aluger das caixas ao lar custe 3 euros por utente por mês. **Mercado**: 3x12x100k = 3.6M
    - Para este preço basiei-me no preço de 2€/utente praticado por softwares de gestão de lares (https://mysenior.com/prices)
- Aqui assumimos que a caixa e software poderiam ser usados por todos os doentes em todos os lares. Isto assume que em lares temos mais de 77% de idosos a tomar vários medicamentos

#### Casas
- Vimos que existem 2.4M de idosos em portugal. Destes, 2.3M não estão em lares.
    - Destes, 77% precisam de tomar vários medicamentos logo poderão usar as caixas: 1.77M de utentes 
    - Consideremos que 50% destes têm família próxima E poderiam/saberiam/teriam meios para usar o nosso produto. 
    - Temos 885k clientes
- Consideremos que a subscrição de funcionalidades extra no software para famílias (app) é de 3€ mensais. **Mercado:** 3x12x885k=31.86M (na prática a pessoa teria a opção de apenas pagar quando quiserem e cancelarem quando quiserem, conforme quando precisam de tomar medicamentos)
    - Escolhi este valor porque está na gama de valores de subscrições anuais de produtos de gestão familiar
- Neste caso a caixa seria vendida e não alugada, trazendo a aplicação base de graça consigo. Consideremos que custa 25 euros e tem um tempo de vida/garantia de 5 anos. Isto quer dizer que temos um rendimento anual médio de **Mercado:** 25/5 x 885k=4.4M

#### Total
- Temos um TAM total:
$$\text{TAM}=3.6+31.86+4.4=39.9\text{M€}$$
- Notemos que temos a maior "fatia" deste mercado nas subscrições da app para famílias

### SAM
- Este consiste em restringir o TAM, considerando que realisticamente nem todos os clientes vão aderir ao nosso produto
- *Lares*
    - Adoção do software + aluguer de caixas (terão que adotar sempre as 2 coisas): 40%. **Mercado:** 0.4x3.6M = 1.4M
- *Casas*
    - Adoção da caixa: 40%. **Mercado:** 0.4x4.4 = 1.76M
    - Adoção do software com subscrição (menor que da caixa): 20%. **Mercado:** 0.2x31.86M = 6.3M

- Temos o SAM:
$$\text{SAM}=1.4 + 1.76 + 6.3 = 9.46 \text{M€}$$
que é cerca de 25%

### SOM
- Consideramos que nos primeiros 3 anos conseguimos atingir 10% do nosso SAM. Assim teremos um SOM de:
$$\text{SOM}=946\text{k€}$$

## NOTAS
- Este valor não é alto, mas apenas estamos a considerar portugal. Se considerassemos a UE isto seria muito maior
- O mercado de caixas de medicamentos inteligentes está em crescimento (ver abaixo), assim como a população idosa

# Top Down
## Dados
- Determinamos que o mercado *global* de dispensadores, caixas e ferramentas para gerir medicamentos era de 2.72 mil milhões de dolares em 2024 (https://www.databridgemarketresearch.com/reports/global-smart-pill-dispenser-market)
- Outra fonte inclui todos os tipos de produtos para gerir medicamentos (hardware e software) estimando um mercado de 5.04 mil milhões de dolares em 2024 (https://www.skyquestt.com/report/medication-adherence-market)
- Apesar deste valor elevado, não existe nenhuma empresa de enormes dimensões neste mercado (mesma fonte), é quase tudo startups
- Uma fonte diz que o mercado para caixas e garrafas de medicamentos inteligentes é de 212.4M de dolares em 2025 (https://www.gminsights.com/industry-analysis/smart-pill-boxes-and-bottles-market)
- Outra fonte diz que o mercado de caixas de medicamentos inteligentes é de 172.4M de dolares em 2025 (https://www.futuremarketinsights.com/reports/smart-pill-box-market)

## Calcular
- Não sei fazer isto de forma consistente. Não há dados de mercado em portugal. Conseguiria talvez apenas se o objetivo fosse vender  na china ou USA