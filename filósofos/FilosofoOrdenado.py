import threading
import time
import random

class FilosofoOrdenado(threading.Thread):
    def __init__(self, identificador, garfo_a, garfo_b):
        super().__init__()
        self.identificador = identificador
        self.primeiro_garfo = garfo_a
        self.segundo_garfo = garfo_b

    def run(self):
        while True:
            print(f"Filósofo {self.identificador} pensando")
            time.sleep(random.uniform(1, 3))

            print(f"Filósofo {self.identificador} com fome")

            self.primeiro_garfo.acquire()
            self.segundo_garfo.acquire()

            print(f"Filósofo {self.identificador} comendo")
            time.sleep(random.uniform(1, 2))

            self.segundo_garfo.release()
            self.primeiro_garfo.release()

            print(f"Filósofo {self.identificador} voltou a pensar")


quantidade_filosofos = 5
conjunto_garfos = [threading.Lock() for _ in range(quantidade_filosofos)]
grupo_filosofos = []

for indice in range(quantidade_filosofos):
    esquerda = indice
    direita = (indice + 1) % quantidade_filosofos

    menor = min(esquerda, direita)
    maior = max(esquerda, direita)

    participante = FilosofoOrdenado(
        indice,
        conjunto_garfos[menor],
        conjunto_garfos[maior]
    )

    grupo_filosofos.append(participante)

for participante in grupo_filosofos:
    participante.start()