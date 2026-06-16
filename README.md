# Filósofos
Na versão ingênua, todos os filósofos podem pegar simultaneamente o garfo da esquerda e ficar esperando o da direita, formando um ciclo de espera e causando deadlock.
Na versão corrigida, todos os filósofos adquirem primeiro o garfo de menor índice e depois o de maior índice.
Essa estratégia elimina a condição de espera circular das condições de Coffman.
Como não existe ciclo de espera, o deadlock não pode ocorrer.
A justiça é favorecida porque, após terminar de comer, o filósofo libera ambos os garfos, permitindo que outros filósofos avancem. Nenhum filósofo mantém recursos indefinidamente.

