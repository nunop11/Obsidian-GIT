# 2. Pesquisa bibliográfica
## 2.1 - Técnicas de pesquisa (V)

- Tecnicas para ampliar ou reduzir o número de resultados - ou seja, usar filtros
- Fazemos isto porque normalmente aparece demasiada informação para conseguir ler e estudar tudo. Precisamos de restringir apenas ao útil
- **Restringir resultados**
    - Operadores:
        - **AND** - garante que os 2 termos aparecem, mas nao têm de estar juntos nem na ordem dada. Normalmente ao meter num motor de pesquisa "X Y" ele interpreta como "X and Y"
        - **NOT** - excluir dos resultados a palavra que vem depois no NOT
        - **aspas** - faz com que termos compostos aparecem todos juntos
    - Estes operadores podem ser feitos em vários campos: autor, titulo, revista, etc
    - Filtros: dependendo do motor de pesquisa, no lado esquerdo costuma aparecer uma lista de coisas por onde podemos filtrar (área, ano, autores, instituições)
    - Thesaurus: Escrevemos várias palavras "X Y Z" e o motor dá várias combinações de palavras mais pesquisadas ("X Y" ou "Z X"), assim como termos associados ou tópicos relacionados
- **Ampliar resultados**
    - Operadores:
        - **OR** - incluir palavras extra. Podemos, eg, ter: NaCl OR "Cloreto de sódio"
        - **de proximidade** - para encontrar fontes com os termos a X palavras de distância. EX:
            - «A NEAR/X B» ou «A W/X B» - A e B ambas presentes, com X palavras máximas de distância
            - Muito específico, presente em poucos operadores
        - **wildcard (?)** - para pesquisar palavras com diferentes grafias (ingles UK/US) ou singular/plural. Colocamos um "?" na zona em dúvida: "optimi?ation" ou "wom?n" 
        - __truncatura (asterico)__ - metemos isto após um prefixo para procurar variações da palavra: `"comput*"` pode dar fontes com: computational, computed, computationally, etc
- Ordem de pesquisa e Nesting:
    - AND conta como operador primário. Palavras associadas a AND têm prioridade
        - Se tivermos AND e OR, fazemos nesting: `(X OR Y) AND Z`
        - Vários motores permitem fazer multiplas caixas de pesquisa para leitura mais fácil
- Palavras vazia / stop words
    - "the", "of", "for", etc
    - Devemos ignorá-la e não as escrever na pesquisa. É melhor usar AND ou OR invés delas
- Podemos combinar técnicas de imensas formas
    - Combinar NOT com OR (`X NOT (Y OR Z)`) vai remover ainda mais termos
    - Combinar NOT com aspas permite remover casos de ambiguidade. Pesquisei "mining" mas quero mineração do solo, então posso por `mining NOT "data mining"`
    - Combinar AND e OR permite ampliar ainda mais os resultados, fazendo combinações: `(X OR Y) AND Z` dará resultados com "X Z" e "Y Z"
        - Colocar ainda uma truncatura em 1+ palavras destas, permite expandir ainda mais

## 2.2 - Sistemas de pesquisa (V)
- Hoje em dia temos informação acessível em todo o lado, especialmente se não tivermos muitos cuidados
- Mas, em investigação cientifica temos de ter informação _de boa qualidade_ - sem bias, informação falsa, etc
- Hoje em dia, muita informação cientifica está disponível online de graça. Mas MUITA está "escondida" atrás de paywalls. 
    - Instituições e universidades têm parcerias que permitem a estudantes e investigador acessar (beON)
- Podemos considerar vários parâmetros para distinguir sistemas de pesquisa:
    - natureza do sistema
    - tipo de fornecedor de informação ao sistema
    - facilidade de acesso
    - natureza do conteudo presente
    - tipo de publicações presentes
- **Natureza do sistema**
    - Bibliotecas digitais: publicações de UM editor ou organização. Contém citações e o texto em si. EX: ScienceDirect da Elsevier
    - Bases bibliográficas: informação de várias editores, contendo referências e resumos. NÃO contém o texto em si, mas indicam onde ir para o obter. EX: Scopus da Elsevier
    - Motores de pesquisa: recuperam informação de acesso aberto OU acesso com subscrição se autorizado. Contém citações e resumos, mas apenas direciona para a biblioteca digital com o texto. EX: Google scholar
    - Portais agregadores: agregam bases bibliográficas, bibliotecas digitais e sistemas de pesquisa NUM SÓ. Contém citações e ainda o texto. EX: Sistema discovery das bibliotecas UP
- **Quem fornece**
    - Editora: empresa dona dos direitos de autor, negoceia com autores, publica e divulga. EX: IEEE
    - Outros: instituições que representam autores e estão autorizadas a publicar por eles. EX: IET
- **Acesso**
    - Aberto: conteudo de acesso grátis. EX: Springer open
    - Pago: conteudo acessível apenas com subscrição (institucional ou particular). EX: Springer link
        - Para aceder a estes, pode ser preciso usar o VPN UP
- **Natureza**
    - Multidisciplinar: quando cobre várias área. EX: web of science
    - Especializado/disciplinar: uma só área ou domínio. EX: ASCE (eng civil)
- **Publicações**
    - Artigos de revistas
    - Atas de conferências
    - Teses e dissertações (RCAAP - repositório portugues)
    - Livros eletrónicos
    - Patentes
    - Relatórios técnicos

- Que sistemas de pesquisa usar para a tese!!!
    - Começar por bases bibliográficas - muita cobertura e atualizadas. Contém informação de qualidade peer-reviewed.
        - Para Engenharia, a Scopus e Web of science
    - Como motor de pesquisa, o google scholar é o mais usado
    - O sistema discovery das bibliotecas UP agrega todos os serviços abertos e os serviços subscritos pela UP. Contém um motor de pesquisa para pesquisar dentro destes.

## 2.3 - Exemplos e uso de gestores
### Endnote
- Colocamos Notes e Research Notes, que podemos selecionar para aparecer na tabela da bibliografia - para encontrar mais facilmente ou ordenar
- Nos PDFS posso meter notas de texto ou fazer highlight de texto
- Permite guardar várias referências e PDFs
- Podemos pesquisar por ambos tipos de notas
- Podemos exportar ambos tipos de notas
    - Podemos ainda criar uma bibliografia anota - contém as notas e as refs
- Notas *LINEARES* -- para não lineares usar Bubbl.us ou Miro


### Mendeley
- Podemos anotar na referênicas: *General notes*
- Podemos anotar no PDF usando sticky notes (colocamos a nota num ponto do texto) ou ao fazer highlight de texto : *Comments*
- Tanto general notes como comments aparecem na aba de *Annotations*
- Existe ainda a aba *Notebook* : criar notas globais a todas as referencias, varias paginas
- Não dá para pesquisar Annotations, apenas nas notas de notebook
- Não podemos exportar notas, só as referencias
- Notas *LINEARES* -- para não lineares usar Bubbl.us ou Miro

### Zotero
- Notas *Standalone/Independentes* - não depende de nenhum documento ou referência
- Notas *Child/Dependentes* - dependem de documento ou referência
- Temos um editor de texto das notas que permite fazer formatação diversas e fazer hiperligações externas. Podemos fazer notas nas referências
- No PDF, podemos fazer highlight de texto (com notas associadas)
    - Para guardar as notas basta fechar o leitor do pdf
    - Os PDF são abertos num leitor próprio do zotero
- Podemos pesquisar notas com a opção "Everything" ou ver todas as notas na pasta "Notes"
    - Posso pesquisar por notas standalone e child
- Para exportar selecionamos as notas em questão na pasta Notes e exportar com menu de click do lado direito. Podemos exportar em vários formatos
- Notas *LINEARES* -- para não lineares usar Bubbl.us ou Miro

## 2.4 - Gerir fontes com gestores (V)
- Começamos por fazer revisão de literatura para garantir que o nosso trabalho é util e inovador
    - Ler muita literatura em diversos formatos. Fazer boa leitura, registo e anotação de tudo que lemos
- As afirmações e ideias que apresento na tese resultam de literatura/pesquisa. Ou seja, requiro as fontes para sustentar as afirmações
    - Perder as fontes pode levar a plágio (mesmo que acidental)!!!
    - Perder fontes irá causar trabalho excessivo e demoroso numa fase mais tardia da tese (mau!!!)
- Gestores bibliográficos permitem: 
    - guardar fontes e pdfs
    - organizar as fontes para melhor eficiencia de pesquisa e leitura
    - partilhar com colaboradores e orientadores
    - fazer citações de forma fácil e correta
- Antes de escolher gestor considerar:
    - quais sao usados por meus colegas?
    - quais sao mais usados na minha comunidade (FEUP)?
    - como é que gestor X me pode ajudar?
    - como é que eu prefiro trabalhar? faz sentido com o gestor X?
    - o gestor X é gratuito? A UP tem alguma parceria?
    - a UP presta apoio tecnico ao gestor X?
- Notas para trabalhar
    - Guardar todas as fontes OK mal as leio, posso não as ver mais
    - Evitar o "sindrome" de "tenho este PDF instalado, pra próxima leio-o" ou "tenho este PDF instalado, portanto devo ter lido"
- Como **guardar** referências
    - Escrever manualmente - documentos impressos mais antigos
    - Importar referência de ferramentas online - catálogo UP, google scholar, springer link
    - Copiar as referências diretamente do PDF, se tiver um **doi**
    - Verificar se está tudo certo. 
        - Os gestores não corrigem erros de referências manuais e podem haver erros de ref importadas
        - Nunca fechar um website/pdf de uma referências sem confirmar tudo
- Como **organizar** refs
    - Organizar como funcionar melhor para mim
    - A sugestão geral é usar pastas bem definidas
    - Permite poupar muito tempo
    - Fazer algum tipo de registo de o que li e das suas notas (num gestor ou no pc)
    - Nos gestores podemos ordenar de várias formas: autor, titulo, ano, etc
- Decidir as minhas **necessidades de recuperação de informação**
    - Ou seja, registar informação de forma a reconhecer literatura posteriormente: quando li, onde encontrei, avaliação pessoal, keywords, notas pessoais, etc
- Acerca de **partilhar**
    - Posso querer partilhar fontes concretas ou partilhar toda uma biblioteca
    - Posso ainda obter feedback do orientador
- Recomendação **UP**:
    - Endnote - subscrito pela UP
    - Mendeley e Zotero, gratuitos

### Gerir fontes no Endnote
- Instalar endnote no atlas.up.pt com credencias UP
    - Posso usar ainda versao online alem da app desktop, atraves de access.clarivate.com

- **Guardar fontes**
    - Podemos: armazenar manualmente, fazer download automatico de sistemas de informação e importar de ficheiros pdf
    - **MANUAL**
        - Criar/abrir biblioteca no endnote
        - Menu > references > new references
        - Na janela que abrir: ir a reference type, escolher book
        - Preencher campos conforme *estilo Chicago* -- colocar autores como "Mary Smith", o endnote meterá o apelido primeiro
            - ESTRUTURA CHICAGO: Autor, Nome. Ano. "Título do artigo." _Nome da Revista/Coleção_ Volume (Número/issue dentro do volume da revista): páginas. DOI
        - Fechar a janela da ref, o endnote guarda sozinho
    - **IMPORTAR AUTOMATICAMENTE**
        - Aceder a um dos sistemas de informação: scopus, web of science, google scholar
        - Pesquisar o tema que quero
        - Filtrar por tipo de documento e mostrar apenas artigos
        - Posso fazer download de registos bibliograficos para o endnote
            - Ao exportar para o endnote, verificar que todos os campos estao preenchidos corretamente
    - **IMPORTAR DE PDF**
        - Descarregar o PDF para o pc através do sistema de informação ou pagina do publisher
        - Importar o pdf para o Endnote através de: File > Import > File e mudar "Import Option" para PDF
        - Se o PDF tiver um DOI acossiado, o endnote irá obtê-lo
            - Verificar se está tudo certo

- **Organizar as fontes**
    - Usamos pastas. Ir ao menu: Groups > Create Group Set e colocar nome
    - Clicar nesse Group Set com botão lado direito do rato para ver mais opções
    - Escolher "Create Group" para fazer grupo/pasta dentro do group set
    - Podemos arrastar as fontes para a pasta/grupo que queremos
        - Ao fazer isto, as fontes NÃO desaparecem da pasta principal
- **Partilhar fontes**
    - Selecionar um grupo
    - Ir ao menu: Groups > Share Group
    - Escrever um email e meter a permissão de leitura ou edição que quero

### Gerir fontes no Mendeley
- Ir a mendeley.com e criar conta. Podemos usar ainda versão app desktop para trabalhar offline

- **Guardar fontes**
    - Temos as mesmas 3 opções que no endnote
    - **MANUALMENTE**
        - Ir a mendeley.com > Library
        - Selecionar o botão Add new > add entry manually
        - Na janela nova, em "reference type" meter "book"
        - Preencher campos no estilo chicago
        - Guardar ao clicar em "Add entry"
    - **IMPORTAR**
        - Tudo igual ao endnote
    - **PDF**
        - Ir a mendeley.com > Library
        - Selecionar Add new > File(s) from computer
        - Se o pdf tiver DOI, irá ser feito tudo automaticamente
            - Confirmar tudo
        - Poderá ser possível usar o Mendeley Importer
- **Organizar fontes**
    - No painel do lado esquerdo clicar em "new collection" e assim criamos uma pasta
    - Podemos só arrastar as fontes
    - As fontes NÃO desaparecem da pasta principal ao fazer isto
- **Partilhar**
    - Ir ao painel do lado esquerdo. Na secção "private groups", clicar em "new group". 
    - Definir nome
    - Clicar no grupo com botão lado direito e selecionar "manage group". Podemos convidar gente por email
    - Arrastamos pdfs da library para o grupo para partilhar

### Gerir fontes no Zotero
- Ir a zotero.org e criar conta. Também existe a versão app desktop

- **Guardar fontes**
    - Temos as mesmas 3 versões
    - **MANUALMENTE**
        - Ir a File > New Item e selecionar o tipo de documento "book"
        - preencher estilo Chicago
            - Verificar tudo
    - **IMPORTAR AUTO**
        - Tudo igual acima
    - **PDF**
        - Simplesmente dropar / arrastar o PDF na library do zotero
        - Se tiver DOI, é tudo automático
- **Organizar fontes**
    - No menu ir a File > New Collection e colocar o nome da pasta
    - Podemos só arrastar as fontes
    - As fontes NÃO desaparecem da pasta principal ao fazer isto
- **Partilhar fontes**
    - Fazer sign-in no zotero online
    - Ir ao menu a Groups > Create a new group. Colocar nome
    - Selecionar opção de público, privado, etc
    - Depois de criar ir à opção "member settings"
    - Selecionar "send more invitations" e colocar email