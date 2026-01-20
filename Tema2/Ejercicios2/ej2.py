"""2. En este ejercicio vamos a lanzar varios procesos, cuyas entradas y salidas 
están enlazadas. Para ello tendremos tres procesos distintos:

Proceso 1: Va a generar 10 direcciones IP de forma aleatoria y se las enviará al
Proceso 2.

Proceso 2: Va a leer las direcciones IP que recibe del Proceso 1 y va a enviar al 
Proceso 3 únicamente aquellas que pertenezcan a las clases A, B o C.

Proceso 3: Va a leer las direcciones IP procedentes del Proceso 2 (no se sabe qué 
número llegarán) y va a imprimir por consola la dirección IP y a continuación la 
clase a la que pertenece.

	Lanza los tres procesos en orden. """

from multiprocessing import Process, Queue
import time, random

def proceso1(q1):
    for i in range(10):
        ip = ".".join(str(random.randint(0,255)) for i in range(4))
        q1.put(ip)
        print(f"Leído: {q1}")
    q1.put(None)
    print("Lectura finalizada\n")
    
def proceso2(q1, q2):
    return


if __name__ == "__main__":
    queue = Queue()
    inicio = time.perf_counter()
    
    p1 = Process(target= proceso1, args=(queue,))
    p2 = Process(target= proceso1, args=(queue,))
    p3 = Process(target= proceso1, args=(queue,))
    
    
    p1.start()
    
    
    p1.join()
    
    fin = time.perf_counter()
    tiempo_proceso = fin - inicio
    print(f"El proceso ha tardado { tiempo_proceso: .2} segundos")