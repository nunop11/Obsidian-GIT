- Sinal vem do latim _signalis_ que quer dizer avisar, advertir, mostrar, etc

# Informação
- Vem do latim _informatio_ (delinear, conceber ideia)
- _Dados_ - a sua existência não depende do observador (existem sem a consciencia do observador)
- _Conhecimento_ - o observador tem que estar presente

## A caixa
- Consideremos uma caixa com objetos dentro. Podemos dizer que quantos mais objetos ela tiver dentro, mais informação ela contém.
- Imaginemos que abrirmos a caixa, _de olhos fechados_, tiramos um objeto e voltamos a fechar a caixa. Ora, passamos a adquirir _conhecimento_ sobre a caixa. No entanto, a _informação_ dentro dela _diminui_.

### Exemplo
![[Destinos e Percurso.png]]
- Temos alguém a querer chegar do início do percurso até ao Destino 4. De notar que: 
    - Em cada divisão do percurso só se pode fazer _2 perguntas e respostas_: esquerda e direita.
    - Todos os 8 destinos têm a mesma "dificuldade" em chegar a eles

- Podemos ver então que temos 8 destinos, 2 opções em cada divisão do percurso e que precisamos de 3 perguntas/respostas para chegar a um destino. Temos então: $$\Huge 8=2^3$$
ou seja:
$$(\textsf{possibilidades})=(\textsf{opções por resposta})^{(\textsf{\# perguntas e respostas})}$$

- Definimos então $I=3$ como a _informação_ necessária para o viajante chegar ao seu destino.
- Ora, iremos ver casos digitais, em que portanto só há 2 opções de resposta (Sim ou Não) então temos $$I=\log_{2}8=3\textsf{ bits}$$
- Vemos então que _1 bit é a informação necessária para escolher entre 2 alternativas equiprovaveis_
- Assim, tendo $N$ perguntas possíveis (objetos na caixa) temos 
$$I=\log_{2}N=\log_{2}\left(\frac{1}{p_\textsf{elemento} }\right)~~~~(\textsf{bits})$$
Ora, podemos definir
$$h_{m_{1}}=\log_{2}\left(\frac{1}{p_{m_{1}}}\right)$$
- Logo, se a probabilidade for muito alta (por exemplo, o Sol nascer amanhã) então a informação associada é reduzida. Isto pode ser visto como "o acontecimento não afeta o dia a dia"
- Se a probabilidade for muito baixa (meteorito atingir a Terra), então a informação associada será muito elevada. Podemos interpretar isto como "este evento iria alterar a dinâmica social"

### Entropia (H)
- Definimos entropia como 
$$H=p_{m_{1}}h_{1}+p_{m_2}h_{2}+\dots+p_{m_N}h_{N}=\sum_{i=1}^{N}p_{m_{i}}\log_{2}\left(\frac{1}{p_{m_{i}}}\right)$$
## Mensagens
- Imaginemos agora uma caixa com $M$ mensagens dentro. Se a mensagem $m_{k}$ tem probabilidade $p_{k}$ de ocorrer, ela está associada a uma quantidade de informação $\Large I_{k}=\log_{2}\frac{1}{p_{k}},~~k=1,2,...,M$
- Como já vimos, se for enviada uma mensagem, a quantidade total de informação na caixa é mantida se entrar na caixa uma mensagem de igual probabilidade de ocorrência. Assim, se todas as mensagens tiverem a mesma probabilidade, é preciso entrar uma mensagem por cada mensagem enviada.
- Para codificar uma mensagem em código binário, atribui-se a cada mensagem uma _palavra binária_ (consideramos que uma palavra binário é uma sequência de 0s e 1s). Ou seja, se há $M$ mensagens, são precisas $M$ palavras binárias.

- Considera-se o número de mensagens é $\large M=2^{N}$.
- Estamos então a admitir que as mensagens são todas equiprovaveis, pelo que $\Large\sum\limits_{k=1}^{M}~p_{k}=1$ 
- Assim:
$$p_{k}=\frac{1}{M}~~~~;~~~~I_{k}=\log_{2}\frac{1}{p_k}=\log_{2}M=\log_{2}2^{N}=N$$
- Ou seja, o número de bits associado à transmissão da mensagem é igual à quantidade de binits (digitos binarios) da palavra binário da sua codificação.
    - _Bits_ - quantidade de informação associada a uma mensagem na caixa de mensagens, ou seja, informação associada a encontrar essa mensagem no meio das outras.
    - _Binits_ - número de digitos da codificaçao da mensagem em binário, ou seja, informação que, quando a mensagem é lida, passa para o leitor.

- Se na caixa de mensagens todas as mensagens tiverem igual probabilidade e estiverem em número de potência de 2, o número de bits das mensgens será igual ao número de binits associado a cada uma. Isto está explicado na equação acima ($I_{k}=N$)

- Voltando ao exemplo da caixa com $N$ elementos. Vimos que, em binário, a informação para chegar a qualquer elemento da caixa é $\Large I_{\textsf{binario}}=\log_{2}N$
- A fórmula mais geral é:
$$I \equiv K\ln N$$

## Conservação de informação
![[Conservação de informação.png]]
- Se tivermos 2 caixas, $A$ e $B$, e movermos 1 objeto de $A$ para $B$, acontece aquilo que é ilustrado acima.
- Ou seja, existe _conservação da informação_ do sistema.

# Informação Funcional
- Consideremos que temos 24 espaços para ocupar com 14 letras.
- Temos $14^{24}\approx 3.2\cdot10^{27}$ combinações possíveis.
- Podemos então ver que $I=\log_{2}{10^{24}}=92 \text{ bits}$ é a informação em bits necessária para chegar a uma sequência específica.
- Consideremos as 2 mensagens seguintes:
$$\color{red}\text{e r a r c o v a i n a v e l a r p a r a o s u i t}$$
$$\text{\color{blue}o\color{red} b a r c o\color{blue} v a i\color{red} n a v e g a r\color{blue} p a r a\color{red} o\color{blue} s u l}$$
- Ora, ambas estão associadas a 92 bits de informação
- No entanto, é claro que há uma diferença qualitativa entre as mensagens: apenas a de baixo realiza a função de comunicação.
- Assim, a mensagem de baixo tem _informação Shannon_ (o tipo de informação que vimos acima), assim como __informação funcional__, que não pode ser medida através dos métodos quantitativos que vimos até agora.

#sinais #fisica #prob-estat 