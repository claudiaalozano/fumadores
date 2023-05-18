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
mutex = Semaphore(1)
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
def fumador(id):
    for _ in range(rondas):
        semaforoFumador
        #semaforo fumador
        semaforoFumador[id].acquire()
        #imprimimos el ingrediente que ha cogido el fumador
        print("El fumador " + str(id) + " ha cogido " + list(ingredientes.keys())[id])
        #imprimimos que esta fumando
        print("El fumador " + str(id) + " esta fumando")
        #tiempo de espera
        time.sleep(2)
        #imprimimos que ha terminado de fumar
        print("El fumador " + str(id) + " ha terminado de fumar")
        #semaforo agente
        semaforoAgente.release()

threads = []
threads.append(Thread(target=agente))
for ingrediente in ingredientes.keys():
    threads.append(Thread(target=fumador, args=(ingrediente)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

