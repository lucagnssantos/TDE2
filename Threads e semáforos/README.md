# Threads e Semáforos
| Versão            | Execução | Esperado | Obtido  | Tempo (s) |
| ----------------- | -------- | -------- | ------- | --------- |
| Sem sincronização | 1        | 1600000  | 200205  | 1.3325    |
| Sem sincronização | 2        | 1600000  | 200271  | 1.3168    |
| Sem sincronização | 3        | 1600000  | 200156  | 1.2697    |
| Com semáforo      | 1        | 1600000  | 1600000 | 3.1196    |
| Com semáforo      | 2        | 1600000  | 1600000 | 3.0737    |
| Com semáforo      | 3        | 1600000  | 1600000 | 3.2294    |

Executar Parte 2 - 
python SemSincronizacao.py
python Semaforo.py

Versão sem sincronização

Nesta versão, múltiplas threads acessam e modificam simultaneamente a variável compartilhada SemSincronizacao. Como a operação de incremento não é atômica, duas ou mais threads podem ler o mesmo valor antes que a atualização seja concluída, causando perda de incrementos.

Versão com semáforo binário

A versão corrigida utiliza um semáforo binário inicializado com uma única permissão. Dessa forma, apenas uma thread por vez pode executar a seção crítica responsável pela atualização do contador.
Com a exclusão mútua garantida pelo semáforo, todas as operações de incremento são realizadas corretamente, produzindo o valor esperado de T × M.

Throughput

A versão sem sincronização tende a apresentar menor tempo de execução por não realizar bloqueios. Entretanto, o resultado pode ser incorreto devido à condição de corrida.
A versão com semáforo possui maior sobrecarga por causa das operações de aquisição e liberação do semáforo, mas garante a integridade dos dados compartilhados.
