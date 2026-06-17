# Filósofos
Na versão ingênua, todos os filósofos podem pegar simultaneamente o garfo da esquerda e ficar esperando o da direita, formando um ciclo de espera e causando deadlock.
Na versão corrigida, todos os filósofos adquirem primeiro o garfo de menor índice e depois o de maior índice.
Essa estratégia elimina a condição de espera circular das condições de Coffman.
Como não existe ciclo de espera, o deadlock não pode ocorrer.
A justiça é favorecida porque, após terminar de comer, o filósofo libera ambos os garfos, permitindo que outros filósofos avancem. Nenhum filósofo mantém recursos indefinidamente.
Executar python FilosofoIngenuo.py e python FilosoOrdenado.py

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


# Deadlock
<img width="307" height="172" alt="image" src="https://github.com/user-attachments/assets/acc74041-b758-476e-b42e-81663c353edc" />
