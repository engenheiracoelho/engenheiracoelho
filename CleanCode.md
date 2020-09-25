# Clean Code

Já fazem algumas semanas que tenho tido mentorias de software com um dev senior super abençoado, o Jesus. 
Esse artigo é um compilado de dicas que vieram nas nossas mentorias, relacionadas a clean code e code smeels. 
A ideia é repassar algumas boas práticas de clean code, de forma bem simples mas completa.

Se você é um dev que realmente busca criar bons softwares, clean code é o ABC do software, e com certeza esse artigo vai te ajudar.

## WTF, o que ta acontecento aqui ?
Se você é um dev lendo um código, essa pergunta deve ser repetida poucas vezes.
Essa é uma grande indicação de um bad smeel code, ou seja, de um código que não cheira a bem estruturado. 
Principais dicas para diminuir essa pergunta? 
 
* Use bons nomes. Eles podem ser grandes ou pequenos, o que importa mesmo é que sejam descritivos e pronunciáveis. Essa regra vale para métodos, classes, variáveis e qualquer outra estrutura.
* Nomeie cada pequena importancia. Não mantenha números mágicos no código, ou funções com propósito essencial sem explicação.
Por exemplo, se você precisa inserir como regra de negócio um upperCase, crie um método que indica a real funcionalidade da utilização da regra. 
Se não tiver o nome adequado, essa funcionalidade com certeza pode se perder com o tempo.
* Considere sempre o principio da responsabilidade unica, tanto para classes quanto para métodos. 
Ou seja, sempre devem ter uma unica funcionalidade, indicações de que isso não está acontecendo poderão ser parâmetros lógicos nos métodos, e 
* "Um código feio testado é melhor que um código bonito sem testes. Jesus,Felipe". O código testado mantem a consistência das regras de negócio, facilita as modificações e fornece clareza para a implementação do código. Não necessariamente aplicar o TDD a risca, com os principios de criação de testes antes das regras de negócio, mas o próprio Mindset do TDD é suficiente para criar códigos melhores, ou seja, pensar em testes em todas as etapas do projeto.
* Considerar a Lei de Demeter - "Um módulo não deve enxergar o interior dos objetos que ele manipula". Por exemplo, ao criar um cenário de modificação 
