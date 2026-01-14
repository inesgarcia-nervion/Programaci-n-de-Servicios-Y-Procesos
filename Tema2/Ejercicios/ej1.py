"""1. Crea una función en Python que sea capaz de sumar todos los números desde el 1 
hasta un valor introducido por parámetro, incluyendo ambos valores y mostrar el 
resultado por pantalla.
Desde el programa principal crea varios procesos que ejecuten la función anterior. 
El programa principal debe imprimir un mensaje indicando que todos los procesos 
han terminado después de que los procesos hayan impreso el resultado."""

from multiprocessing import Process
import time

def sumar(numero:int):
    resultado = sum(range(1, numero+1)) 
    print(f"Suma hasta {numero} da de resultado {resultado}")

if __name__ == '__main__':
    
    p = Process(target=sumar, args=(10,))   # Paréntesis y coma alrededor del número necesarios
    inicio = time.perf_counter()
    p.start()
    p.join()
    
    fin = time.perf_counter()
    tiempo_proceso = fin - inicio
    print(f"Proceso terminado")
    print(f"El proceso ha tardado {tiempo_proceso: .2} segundos")