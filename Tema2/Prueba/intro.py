from multiprocessing import Process
import os
import time


def saludar(nombre:str) -> None:
    print(f"[HIJO] Hola {nombre}. PID={os.getpid()}") # Devuelve el proceso que se ha realizado


if __name__ == "__main__":
    print(f"[PADRE]. PID={os.getpid()}")
    
    p = Process(target = saludar, args =("Ana",)) # Argumentos es lo que te pide (en este caso, un str)
    inicio = time.perf_counter()
    p.start()
    p.join()     # Con esto, el proceso de padre no termina antes que el hijo (espera al otro proceso)
    
    fin = time.perf_counter()
    tiempo_proceso = fin - inicio
    print("[PADRE] El proceso ha terminado")
    print(f"El proceso ha tardado {tiempo_proceso: .2} segundos")   # La f al principio es importante (es un formateo), sino no funciona el cálculo de los segundos
    
    # multiprocessiong.Process(target = ......, args= ....)
    # start() join() --> Iniciamos procesos y nos esperamos a que termine
    
    