# Nome: Lucas Gabriel Nunes dos Santos
# Link do video: https://youtu.be/bMbJ1P6ieGo ou https://www.youtube.com/watch?v=bMbJ1P6ieGo
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
deadlock_reprodução:
<img width="237" height="106" alt="image" src="https://github.com/user-attachments/assets/6228208d-75a7-44a1-9189-91b9947dd4da" />


deadlock_corrigido:
<img width="267" height="169" alt="image" src="https://github.com/user-attachments/assets/aa3397d9-680d-4c9a-9285-c24f5690b76e" />

Por que ocorre o deadlock?
Na versão problemática:

T1 adquire o Lock A.
T2 adquire o Lock B.
T1 espera o Lock B.
T2 espera o Lock A.

Cada thread fica aguardando um recurso que está em posse da outra, formando um ciclo de espera.

Condições de Coffman presentes
Exclusão mútua
Apenas uma thread pode possuir cada lock por vez.
Manter e esperar
Cada thread mantém um lock enquanto aguarda outro.
Não preempção
O lock não pode ser retirado à força da thread que o possui.
Espera circular
T1 espera B enquanto possui A.
T2 espera A enquanto possui B.

Como as quatro condições estão presentes simultaneamente, ocorre deadlock.
