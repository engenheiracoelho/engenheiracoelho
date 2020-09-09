# Clean Code

## Code Smells 

<p align="left">
  <img src=https://data.whicdn.com/images/247439990/original.gif> 
</p>

 # <i> "Indicativos de que algo não cheira bem no código.</i> 

O capítulo 17 do livro "Clean Code" possui as indicações de como identificar que o código cheira bem, e auxilia no entendimento dos "odores diferentes do código" indicando as categorias e dicas a seguir.

### Comentários

**C1:** Informações inapropriadas, como versão, autor e data.  
**C2:** Comentários que podem ficar obsoletos com o tempo.  
**C3:** Comentários redundantes, como a funcionalidade de um método que pode estar no nome do método.  
**C4:** Comentários mal escritos.  
**C5:** Código como comentário.

### Ambiente

**E1:** Construir requer mais de uma etapa.  
**E2:** Testes requerem mais de uma etapa.  

### Funções

**F1:** Parâmetros em excesso.  
**F2:** Parâmetros de saída não devem existir.  
**F3:** Parâmetros lógicos indicam que a função faz mais de uma coisa.  
**F4:** Função morta, que não é mais utilizada.  

### Geral

**G1:** Múltiplas linguagens em um arquivo fonte.  
**G2:** Comportamento óbvio não é implementado. "Principio da menor surpresa"
**G3:** Comportamento incorreto nos limites.
**G4:** Seguranças anuladas, testes ignorados.  
**G5:** Duplicação de código.  
**G6:** Código no nível errado de abstração.
**G7:** As classes bases dependem de suas derivadas.  
**G8:** Informações excessivas na classe.  
**G9:** Código morto.  
**G10:** Separação vertical.  
**G11:** Inconsistência.  
**G12:** Entulho.  
**G13:** Acoplamento artificial.
**G14:** Feature envy - preferencialmente os métodos da classe devem ficar interessados nas variáveis e funções da classe a qual eles pertencem, e não nas de outras classes.
**G15:** Parâmetros seletores.  
**G16:** Propósitos dificeis de entender.  
**G17:** Responsabilidade mal posicionada.  
**G18:** Modo estático inadequado.  
**G19:** Variáveis pouco descritivas.  
**G20:** Nomes de métodos que não falam o que fazem.  
**G21:** Algoritmo dificil de entender.  
**G22:** Torne dependencias lógicas em físicas.  
**G23:** Prefira polimorfismo a if...else ou switch...case.  
**G24:** Siga as convensões padrões da equipe.  
**G25:** Substitua números mágicos por constantes com nomes. 
**G26:** Seja preciso.  
**G27:** Estrutura está acima de convenção.  
**G28:** Encapsule as condições em funções que especifiquem o propósito.  
**G29:** Evite condicionais negativas.  
**G30:** Funções devem fazer uma unica coisa.
**G31:** Acoplamentos temporários ocultos.  
**G32:** Não seja arbitrário.  
**G33:** Encapsule as condições de limites.  
**G34:** Funções devem descer apenas um nível.  
**G35:** Mantenha os dados configuráveis em níveis altos.
**G36:** Evite a navegação transitiva.

### Nomes

**N1:** Escolha nomes descritivos. 
**N2:** Escolha nomes no nível apropriado de abstração.
**N3:** Use uma nomeclatura padrão onde for possível.
**N4:** Nomes não ambíguos.
**N5:** Use nomes longos para escopos grandes.
**N6:** Evite codificações.
**N7:** Nomes devem descrever efeitos colaterais.

### Testes

**T1:** Testes insuficientes. 
**T2:** Use ferramenta de cobertura.
**T3:** Não pule testes triviais.
**T4:** Um teste ignorado é uma ambiguidade. 
**T5:** Teste as condições de limites.
**T6:** Teste abundantemente bugs próximos.
**T7:** Padrões de falhas são reveladores.
**T8:** Padrões de cobertura de testes podem ser reveladores.
**T9:** Testes devem ser rápidos.































