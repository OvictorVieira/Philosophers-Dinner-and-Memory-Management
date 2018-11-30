# Jantar dos Filósofos + Gerenciamento de Memória

Foi realizado o desenvolvimento para a resolução do classico problema do "Jantar do Filósofos" para a disciplina de Sistemas Operacionais da UNIVEM - Centro Universitário Eurípides de Marília, SP

Para o Jantar dos Filósofos foi utilizado a Biblioteca Threading para realizar o paralelismo utilizando trheads.
Para o Gerenciamento de Memória foram utilizados Listas(list()) e Dicionarios(disc()) para o armazenamento dos processos e indexação das páginas e frames na memória principal (Memória RAM) e memória secundária (Memória Swap).

## Integrantes do Grupo

- Victor Hugo de Souza Vieira      	R.A.: 55736-6
- Lucas Costa de Oliveira Alves		R.A.: 56365-1

### Jantar dos Filósofos

O problema pode ser resumido como cinco filósofos sentados ao redor de uma mesa redonda, cada qual fazendo exclusivamente uma das duas coisas: comendo ou pensando. Enquanto está comendo, um filósofo não pode pensar, e vice-versa.

Em geral, o problema do jantar dos filósofos é um problema genérico e abstrato que é utilizado para explicar diversas situações indesejáveis que podem ocorrer em problemas que tem como principal idéia a exclusão mútua.

### Gerenciamento de Memória

Gerenciador de Memória é a parte do SO que é responsável por cuidar de quais partes da memória estão em uso, quais estão livres, alocar memória a processos quando eles precisam, desalocar quando eles não necessitarem mais e gerenciar a troca dos processos entre a memória principal e o disco (quando a memória principal não é suficiente para manter todos os processos)

### Tecnologias

Linguagem: Python 3

### Bibliotecas

* [Threading](https://docs.python.org/3/library/threading.html) - Paralelismo baseado em threads
* [Random](https://docs.python.org/3/library/random.html) - Gerador de números aleatórios
* [Time](https://docs.python.org/3/library/time.html) - Conversor de Data
* [Math](https://docs.python.org/3/library/math.html) - Biblioteca com Funções Matematicas
