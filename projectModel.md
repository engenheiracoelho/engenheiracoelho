# < projectName >
<fig>
<img src="https://rockcontent.com/br/wp-content/uploads/sites/2/elementor/thumbs/modelo-de-projeto-p2he6clp7uhmwqd16ikv9jgz30a5liixoon908hej0.png" alt="Uma imagem relacionada ao projeto">
<figcaption>Uma imagem relacionada ao projeto</figcaption>
</fig>

## Inicialização
Para executar o projeto, utilize as ferramentas descritas na sessão *Ferramentas*.

## Ferramentas
* [IntelliJ](https://www.jetbrains.com/idea/) - IDE para desenvolvimento.

## Links importantes
* [Spring Boot Rest API](https://medium.com/better-programming/building-a-spring-boot-rest-api-a-php-developers-view-part-i-6add2e794646) -  API com Spring Boot.

# < projectName >

## Introdução

> É interessante colocar aqui uma visão bem geral, aquilo que você falaria em uma reunião rápida.  
> Vai ser a resposta que você da pra sua tia quando ela pergunta o que está fazendo da vida.

Este projeto possui o objetivo principal **< descreva o objetivo principal >**.  
Com os objetivos gerais de realizar a inserção de **< objeto >** e verificação de **< objeto >**. 

## Análise técnica

### Descrição do ambiente técnico

O sistema é composto por um banco de dados, uma interface web e um sistema embarcado. Funcionalidades principais:
> Indique os grandes blocos do sistema.

* **F1** - Nome da funcionalidade 1.
* **F2** - Nome da funcionalidade 2.
* **F3** - Nome da funcionalidade 3.
> Coloque somente o nome principal, por exemplo: Controle de usuários.

As ferramentas utilizadas para o desenvolvimento incluem **< linguagem para back-end >** que é uma linguagem de programação utilizada para o Back-end, para front-end foi utilizado **< linguagem para o front-end >** . **< Banco de dados >** atuando como sistema gerenciador de banco de dados relacional e **< gerenciador de container >** para utilizar o ambiente em container.

### Levantamento de requisitos  
Os requisitos devem ser validados com a cliente e aprovados.
> Aprovar os requisitos com o cliente é o mais importante, se não for validado o documento não será válido.

### Requisitos Funcionais
Respeitando a proposta, o sistema deverá atender os seguintes requisitos:

* **RF1** - Requisito funcional 1.
* **RF2** - Requisito funcional 2.
* **RF3** - Requisito funcional 3.

> O requisito funcional está relacinado as funcionalidades citadas. Por exemplo "Geração de relatório de determinado período de vendas". [Verifique mais detalhes aqui](https://codificar.com.br/requisitos-funcionais-nao-funcionais/).

## Regras de Negócio

_Solicitação_  

**RGN1** -  O cliente só fará a solicitação se estiver cadastrado e logado.  

_Agendamento_  

**RGN2** - O cliente só fará a agendamento se estiver 2 anos no sistema.   

> As regras de negócio estão relacionadas as dependencias do sistema, por exemplo "depois de x tempo" ou "para clientes de x perfil".

## Casos de Uso

**UC1** - *Login no sistema*

Ao entrar no sistema pela primeira vez o usuário deve cadastrar suas informações. O usuário deverá informar seu perfil.

<img src="https://d2slcw3kip6qmk.cloudfront.net/marketing/pages/chart/examples/flowchart-templates/system-flowchart.svg">

> Imagine que fosse necessário enviar um email sempre que realizado o login, esse email deveria estar no fluxograma. Esse fluxograma pode ser mais simples, apenas com o objetivo de validar com o cliente que as dependências de negócio estão validadas em cada caso de negócio.

### Mensagens internas

Rotas utilizadas pela aplicação web para executar metodos de **POST** e **GET** no banco de dados. Onde o retorno de cada uma das funções estara contido em uma sessão para renderização de páginas web.

> Aqui ficam descritos os endpoints, que podem estar em outra documentação também.  
> É interessante colocar essa documentação aqui quando a API é pequena.

| Nome | Funcionalidade|
|------|--------------|
|```GET``` /listarUsuario|Informa todos usuários registrados no banco.|
|```POST``` /insereUsuario|Insere um novo usuário.|
|```PUT``` /atualizaUsuario|Atualiza o usuário.|

## Conceitos básicos
* [Design pattern](https://www.opus-software.com.br/design-patterns/) - Design Patterns ou padrões de projetos são soluções generalistas para problemas recorrentes durante o desenvolvimento de um software. Mais informações no [catalogo de design pattern](https://refactoring.guru/design-patterns). 
