## __Projeto para disciplina de Programação Orientada a Objetos - Xadrez__

  Esse projeto buscou a implementação de um jogo de Xadrez utilizando os conceitos estudados em sala de aula, aplicando conceitos de programação orientada à objetos como herança, polimorfismo e a utilização de atributos privados.

  ---
## Arquitetura e Comportamento das Classes

O sistema foi desenhado de forma que a lógica do jogo (`Tabuleiro` e `Peca`) funcione de maneira independente da interface escolhida pelo usuário:

* **`Peca` (`xadrex_esqueleto.py`):** Classe base abstrata (`ABC`) que encapsula os atributos privados de localização (`__numeros`, `__letras`) e cor (`__cor`, onde `True` representa as Brancas e `False` as Pretas). Define o método abstrato `movimento()`, obrigando cada subclasse (`Peao`, `Torre`, `Cavalo`, `Bispo`, `Rainha` e `Rei`) a implementar sua própria regra de deslocamento e captura.
* **`Tabuleiro` (`tabuleiro.py`):** Gerencia a matriz do tabuleiro, o controle de turnos e a validação de jogadas. Antes de efetivar qualquer lance, simula o movimento para garantir que o próprio Rei não fique em xeque. Centraliza também os estados especiais da partida e lança exceções (`ValueError`) sempre que uma jogada viola as regras.
* **`Jogador` (`jogador.py`):** Armazena a identificação e a cor associada a cada participante da partida.
* **`XadrezInterface` (`interface.py`) & `XadrezTerminal` (`xadrez_terminal.py`):** Camadas de visualização e entrada de dados. Ambas consomem exatamente a mesma classe `Tabuleiro`, traduzindo cliques na tela (via `Tkinter`) ou coordenadas algébricas no console (ex.: `E2` para `E4`) para chamadas de método no motor do jogo.
* **`main.py`:** Ponto de entrada que permite escolher entre jogar na interface gráfica ou direto no terminal.

---

## Funcionalidades Implementadas

* **Movimentação completa:** Todas as peças seguem as regras oficiais do xadrez.
* **Lances especiais:**
  * **Roque** (pequeno e grande), validando se o Rei e a Torre já se moveram, se o caminho está livre e se as casas de passagem não estão atacadas.
  * **En Passant**, rastreando a última jogada do adversário.
  * **Promoção do Peão**, permitindo escolher entre Rainha, Torre, Bispo ou Cavalo ao alcançar a última fileira (tanto via janela pop-up no Tkinter quanto via menu no terminal).
* **Detecção de Xeque e Xeque-Mate:** Verificação dinâmica de casas atacadas e simulação de movimentos salvadores para encerrar a partida automaticamente.
* **Modo Híbrido de Jogo:** Suporte nativo para **Interface Gráfica (`Tkinter`)** e **Modo Texto (Terminal)** com símbolos Unicode (`♔ ♕ ♖ ♗ ♘ ♙`).

---

## Histórico de Evolução do Projeto

O desenvolvimento seguiu um ciclo iterativo ao longo das aulas:

* **15/10/2026 — Definição e Modelagem Inicial:** Definição do escopo focado primeiro no comportamento das peças e na representação lógica das regras e coordenadas do tabuleiro, deixando a interface gráfica para a etapa final.
* **22/10/2026 — Abstração, Encapsulamento e Primeiros Movimentos:** Criação da classe abstrata `Peca` com atributos privados (`__x`, `__y`, `__cor`) e métodos de acesso (`getters`/`setters`). Implementação inicial da matriz na classe `Tabuleiro`, lógica de movimentação e captura do `Peao`, criação da classe `Jogador` e entrada de movimentos por coordenadas (ex.: `A2` para `A3`).
* **29/10/2026 — Refatoração Arquitetural e Tratamento de Erros:** Substituição de retornos simples e `prints` internos por tratamento de exceções (`raise ValueError`). Implementação das demais peças do xadrez e suas respectivas lógicas de movimentação no tabuleiro. Desacoplamento das entradas de dados (`input`) de dentro das classes de negócio, transferência do controle de turno para o `Tabuleiro` e início da implementação gráfica com `Tkinter`.
* **05/11/2026 — Consolidação Dual (GUI + CLI) e Regras Avançadas:** Manutenção simultânea das duas versões (Terminal e Interface Gráfica selecionáveis pelo `main.py`), finalização dos movimentos de todas as peças, adição de Roque, En Passant, Promoção, Xeque-Mate e documentação do repositório.

---
