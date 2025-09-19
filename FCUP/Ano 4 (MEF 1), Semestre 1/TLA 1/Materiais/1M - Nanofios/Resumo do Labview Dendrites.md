## Labview
- Chama-se "Anod+Dendr" e serve para fazer a segunda anodização e para controlar $\delta_{b}$.
![[labview anodizacao.png]]
- Parametros Gerais
    - Anodization Type : Preencher com o tipo de ácido que vamos usar (Oxálico, Sulfurico, Fosfórico)
    - Nr. Samples : número de samples lol
    - Diametro Samples : lol
    - Sample ID : nome do ficheiro a guardar
    - Optional Subfolder : o que o nome diz
    - Waiting time to start : para fazer schedule de quando o programa vai trabalhar
- Parametro da segunda anodização
    - Anodization Potential , Anodization Time : o que os nomes dizem
    - Stop/Skip : podemos usar para não fazer este passo, podemos clicar depois da rotina começar só
- Redução da camada de óxido
    - Final Potential : A espessura irá reduzir desde a tensão colocada no bloco verde até esta tensão. Ver o artigo para saber que espessura/tensão queremos.
    - Stop/Skip : igual a cima
- Rotina de Homogeneização
    - Este passo é feito automaticamente, é aplicada corrente constnate para reduzir efeitos na barreira.
    - Stop/Skip : igual a cima

### NOTA
- As dendrites são frágeis. PED deverá ser executado logo que possível, depois da formação destas.
- Lavamos o eletrólito de ácido com água de-ionizada com cuidado.