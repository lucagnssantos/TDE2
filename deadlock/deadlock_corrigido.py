import threading
import time

recurso_a = threading.Lock()
recurso_b = threading.Lock()

def processo_um():
    print("T1 tentando adquirir A")
    with recurso_a:
        print("T1 adquiriu A")
        time.sleep(0.05)
        print("T1 tentando adquirir B")
        with recurso_b:
            print("T1 concluiu")

def processo_dois():
    print("T2 tentando adquirir A")
    with recurso_a:
        print("T2 adquiriu A")
        time.sleep(0.05)
        print("T2 tentando adquirir B")
        with recurso_b:
            print("T2 concluiu")


thread_um = threading.Thread(target=processo_um)
thread_dois = threading.Thread(target=processo_dois)

thread_um.start()
thread_dois.start()

thread_um.join()
thread_dois.join()
print("Programa finalizado")