"""5. Crea una función en Python que sea capaz de sumar todos los números 
comprendidos entre dos valores, incluyendo ambos valores y mostrar el resultado 
por pantalla. Estos valores se les pasará como argumentos. Hay que tener presente 
que el primer argumento puede ser mayor que el segundo, y habrá que tenerlo 
presente para realizar la suma.
Desde el programa principal crea varios procesos que ejecuten la función anterior. 
El programa principal debe imprimir un mensaje indicando que todos los procesos 
han terminado después de que los procesos hayan impreso el resultado."""

from multiprocessing import Process
import time

def sumar(numero1:int, numero2:int):
    inicio = min(numero1, numero2)
    fin = max(numero1, numero2)
    resultado = sum(range(inicio, fin + 1))  # Si pusiera "1 a 10", se haría de 1 a 9
    print(f"Suma desde { inicio } hasta {fin} da de resultado {resultado}")

if __name__ == '__main__':

    inicio = time.perf_counter()
    
    # Primero se crean los procesos
    p1 = Process(target=sumar, args=(1, 10))
    p2 = Process(target=sumar, args=(50, 1))
    p3 = Process(target=sumar, args=(1, 100))
    
    # Después se arrancan TODOS a la vez
    p1.start()
    p2.start()
    p3.start()
    
    # Por último, esperamos a que TODOS terminen
    p1.join()
    p2.join()
    p3.join()
    
    
    fin = time.perf_counter()
    tiempo_proceso = fin - inicio
    print(f"Proceso terminado")
    print(f"El proceso ha tardado {tiempo_proceso: .2} segundos")