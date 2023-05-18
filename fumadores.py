#programa fumadores
from threading import Semaphore, Thread
import time
import random

#diccionario de ingredientes
ingredientes = {"tabaco": ["papel" , "cerillas"], "cerillas": ["papel", "tabaco"], "papel": ["cerillas", "tabaco"]}
#semaforos
semaforoAgente = Semaphore(1)
semaforoFumador = {"papel": Semaphore(0), "tabaco": Semaphore(0), "cerillas": Semaphore(0)}
#semaforo para el mutex

rondas = 5
terminate = False
#funcion agente
def agente():
    for _ in range(rondas):
        global terminate
        if terminate:
            break
        ingrediente1 = random.choice(list(ingredientes.keys()))
        ingrediente2 = random.choice(list(ingredientes.keys()))
        print("El agente ha puesto " + ingrediente1 + " y " + ingrediente2)
        semaforoFumador[ingrediente1].release()
        semaforoFumador[ingrediente2].release()

    semaforoAgente.release()
    terminate = True
    print("El agente ha terminado")

#funcion fumador
def fumador(ingrediente):
    for _ in range(rondas):
        #semaforo fumador
        semaforoFumador[ingrediente].acquire()
        if terminate:
            break
        print("El fumador " + ingrediente + " esta fumando")
        time.sleep(1)
        print("El fumador " + ingrediente + " ha terminado de fumar")
        semaforoAgente.acquire()

threads = []
threads.append(Thread(target=agente))
for ingrediente in ingredientes.keys():
    threads.append(Thread(target=fumador, args=(ingrediente,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Todos los hilos han terminado")
