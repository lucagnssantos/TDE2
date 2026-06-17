import threading
import time

contador_compartilhado = 0

quantidade_threads = 8
quantidade_incrementos = 200000

controle_acesso = threading.Semaphore(1)

def executar_incrementos():
    global contador_compartilhado

    for _ in range(quantidade_incrementos):
        controle_acesso.acquire()

        try:
            valor_temporario = contador_compartilhado
            valor_temporario += 1
            contador_compartilhado = valor_temporario
        finally:
            controle_acesso.release()

inicio = time.perf_counter()

grupo_threads = []

for _ in range(quantidade_threads):
    processo = threading.Thread(target=executar_incrementos)
    grupo_threads.append(processo)
    processo.start()

for processo in grupo_threads:
    processo.join()

fim = time.perf_counter()

print(f"Esperado: {quantidade_threads * quantidade_incrementos}")
print(f"Obtido: {contador_compartilhado}")
print(f"Tempo: {fim - inicio:.4f} segundos")