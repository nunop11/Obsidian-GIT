### Notas importantes
- Ativar sempre UNITS ao ligar o programa para verificar que está tudo conforme desejado
- Ver o que temos ativado no OSNAP (midpoint, tangent, parallel, perpendicular, etc) -- F3 ativa desativa OSNAP 
- Para mudar cores podemos usar as propriedades mas normalmente é mais conveniente usar layers diferentes
- Para ver como se configura layout de folha ver o PPT da aula 2
- Para alinhar viewport no Layout:
    - marcar com uma linha ou qq coisa o ponto central da figura no modelo
    - no layout fazer o mesmo, normalmente a intersetar retas
    - colocar viewport pequeno e encaixar estes pontos
    - Expandir viewport. Deve ficar tudo bem

### Shortcuts
- F3 - toggle OSNAP
- F7 - toggle grelha
- F8 - toggle modo ortogonal
- `#` - coordenadas absolutas
- @ - coordenadas relativas
- CTRL+C / CTRL+P - adivinha :D

### Comandos
- PLINE 
- XLINE - linha infinita
- RAY - linha que sai de 1 ponto e se prolonga infinitamente
- SPLINE - linha curva que passa pelos pontos que marcamos
- ARC - arco
- CIRCLE - círculo - Existem os modos TAN TAN RAD ou TAN TAN TAN que dão muito jeito
- POINT 
- ELLIPSE
- DONUT - anel com espessura (por default fica preenchido)
- MIRROR - espelhar objetos selecionados conforme eixo
- ROTATE - rodar conforme ponto central
- MTEXT - texto de 2+ linhas
- CHAMFER - une linhas, conforme angulo ou comprimento da linha que as une. Se usarmos entre 2 lados de um polígono ele traça linhas na mesma (como se cortasse as esquinas de um retângulo)
- FILLET - une linhas conforme raio dado. Também pode usado em polígonos para "arredondar" cantos.
- HATCH - preencher com padrão (podemos selecionar um ponto da região a preencher ou selecionar os objetos que a delimitam)
- TRIM - cortar pedaços de linhas
- OFFSET - repetir objeto a uma certa distância 
- EXPLODE - separar componentes de um objeto (usa isto invés de BREAKATPOINT)
- JOIN - junta objetos selecionados num só (oposto de EXPLODE)
- ALIGN - encaixar pontos de objeto em 2 pontos escolhidos (estica e roda o objeto conforme necessário)
- IMAGEATTACH - inserir imagem 
- MULTIPLE - para os comandos que desativam após usar 1 vez (FILLET por exemplo), permite usar esses comandos várias vezes seguidas
- EXTEND - estender objeto até intersetar (primeiro selecionamos o objeto que será intersetado!)
