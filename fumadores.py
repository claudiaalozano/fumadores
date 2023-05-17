#programa fumadores
from threading import Semaphore, Thread
import time
import random

#diccionario de ingredientes
ingredientes = {"tabaco": ["papel" , "cerillas"], "cerillas": ["papel", "tabaco"], "papel": ["cerillas", "tabaco"]}
#semaforos
semaforoAgente = Semaphore(1)
semaforoFumador = [Semaphore(0), Semaphore(0), Semaphore(0)]
#semaforo para el mutex
mutex = Semaphore(1)

#funcion agente
def agente():
    while True:
        #semaforo agente
        semaforoAgente.acquire()
        #seleccionamos un ingrediente aleatorio
        ingrediente = random.choice(list(ingredientes.keys()))
        #imprimimos el ingrediente
        print("El agente ha puesto " + ingrediente)
        #semaforo mutex
        mutex.acquire()
        #sacamos los ingredientes del diccionario
        for i in ingredientes[ingrediente]:
            semaforoFumador[i].release()
        #liberamos el mutex
        mutex.release()

#funcion fumador
def fumador(id):
    while True:
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

