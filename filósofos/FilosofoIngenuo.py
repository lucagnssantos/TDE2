import threading
import time
import random

class FilosofoIngenuo(threading.Thread):
    def __init__(self, identificador, garfo_esquerdo, garfo_direito):
        super().__init__()
        self.identificador = identificador
        self.garfo_esquerdo = garfo_esquerdo
        self.garfo_direito = garfo_direito

    def run(self):
        while True:
            print(f"Filósofo {self.identificador} pensando")
            time.sleep(random.uniform(1, 3))

            print(f"Filósofo {self.identificador} com fome")

            self.garfo_esquerdo.acquire()
            print(f"Filósofo {self.identificador} pegou o garfo esquerdo")

            time.sleep(0.5)

            self.garfo_direito.acquire()

            print(f"Filósofo {self.identificador} comendo")
            time.sleep(random.uniform(1, 2))

            self.garfo_direito.release()
            self.garfo_esquerdo.release()

            print(f"Filósofo {self.identificador} voltou a pensar")


quantidade_filosofos = 5
conjunto_garfos = [threading.Lock() for _ in range(quantidade_filosofos)]
grupo_filosofos = []

for indice in range(quantidade_filosofos):
    participante = FilosofoIngenuo(
        indice,
        conjunto_garfos[indice],
        conjunto_garfos[(indice + 1) % quantidade_filosofos]
    )
    grupo_filosofos.append(participante)

for participante in grupo_filosofos:
    participante.start()