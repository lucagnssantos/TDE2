import threading
import time
import random

class Filosofo(threading.Thread):
    def __init__(self, identificador, garfo_esquerdo, garfo_direito):
        super().__init__()
        self.identificador = identificador
        self.primeiro_garfo = min(garfo_esquerdo, garfo_direito, key=id)
        self.segundo_garfo = max(garfo_esquerdo, garfo_direito, key=id)

    def run(self):
        while True:
            print(f"Filósofo {self.identificador} está pensando")
            time.sleep(random.uniform(1, 3))

            print(f"Filósofo {self.identificador} está com fome")

            with self.primeiro_garfo:
                with self.segundo_garfo:
                    print(f"Filósofo {self.identificador} está comendo")
                    time.sleep(random.uniform(1, 2))

quantidade_filosofos = 5

conjunto_garfos = [threading.Lock() for _ in range(quantidade_filosofos)]

grupo_filosofos = []

for indice in range(quantidade_filosofos):
    garfo_esquerdo = conjunto_garfos[indice]
    garfo_direito = conjunto_garfos[(indice + 1) % quantidade_filosofos]

    participante = Filosofo(
        indice,
        garfo_esquerdo,
        garfo_direito
    )

    grupo_filosofos.append(participante)

for participante in grupo_filosofos:
    participante.start()

for participante in grupo_filosofos:
    participante.join()