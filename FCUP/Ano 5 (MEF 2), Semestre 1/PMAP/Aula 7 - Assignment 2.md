- Anodo é a parte metálica, metemos a cobertura tipo cimento para aumentar a durabilidade
- As medições que temos que fazer estão marcadas com setas vermelhas na foto no notebook. Medimos largura da vara metálica, comprimento e largura da proteção (parte rochosa)

### 1.
- O sistema estereo moveu-se para a direita enquanto captamos imagem. Por isso é fundamental todos os frames ocorrerem no mesmo instante
    - Em princípio os indices/numeros no nome dos ficheiros vai ser sempre exatamente igual
    - Se não for igual, só retiramos estas imagens do set. Não deve ter muito efeito
- Só importar xml e retirar distorção
    - A partir desse ponto, só usamos as imagens sem distorção e retificadas

### 2.
- Escolher método (feature ou denso)
- Mostrar resultados com um par de imagens (L,R) random. Escolher algo com o anodo e parede, para ter algo de jeito

### 3.
- Converter em pcd. Ter em conta que vai ter ruido
- Usar mesmo par de imagens que em 2

### 4.
- Nada de especial a notar
- Só seguir o que é dito

### 5, 6.
- Ter em conta que vamos processar 140x2 imagens

## Critérios de avaliação
- **Qualidade das medições**
    - Vai ser avaliado o erro - quão longe estamos do valor real. O prof tem o ânodo real.
    - O grupo com os melhores valores ganha algo?
- **Automação**
    - Quão automático o código é
    - Quão fácil seria introduzir o nosso programa numa pipeline para fazer isto
    - Não queremos que seja demasiado paramétrico
    - Se fizermos retificação, podemos fazer SSD ou wtv só na horizontal sem perder pontos aqui
    - Assume-se que teremos sempre o ficheiro de calibração
- **Robustez**
    - Quão forte o modelo é contra alterações - rotações, ruido
    - Isto consiste nas escolhas:
        - Feature é mais robusto mas temos pouco pontos
        - Podemos fazer denso e aplicar filtros para ser robusto
    - Esta parte depende _muito_ do quão bem justificamos e explicamos decisões
    - Notemos que Disparidade por features pode ser feitas sem retificação 
    - Podemos testar criar datasets alterados e ver como corre