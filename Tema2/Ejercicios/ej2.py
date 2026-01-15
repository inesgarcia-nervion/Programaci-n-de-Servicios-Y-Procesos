"""2. Modifica el ejercicio anterior para que el programa principal use un Pool para
lanzar varios procesos de forma concurrente. Cambia el valor del número de procesos
y compara los tiempos que tarda en ejecutarse en los distintos casos."""

from multiprocessing import Pool
import time

def sumar(numero:int):
    resultado = sum(range(1, numero+1)) 
    print(f"Suma hasta {numero} da de resultado {resultado}")

if __name__ == '__main__':

    print("Proceso 1")
    inicio = time.perf_counter()
    with Pool(processes=1) as pool:
        #Creamos una lista con los datos de entrada
        numero = [1,2,3,4,5]
        #Ejecutamos la función sumar y le pasamos la lista con los datos
        results = pool.map(sumar, numero)
    tiempo1 = time.perf_counter()
    tiempo_proceso = tiempo1 - inicio
    print(f"El proceso 1 ha tardado {tiempo_proceso: .2} segundos\n")
        
    
    
    print("Proceso 2")
    inicio = time.perf_counter()
    with Pool(processes=2) as pool:
        #Creamos una lista con los datos de entrada
        numero = [1,2,3,4,5]
        #Ejecutamos la función sumar y le pasamos la lista con los datos
        results = pool.map(sumar, numero)
    tiempo2 = time.perf_counter()
    tiempo_proceso = tiempo2 - inicio
    print(f"El proceso 2 ha tardado {tiempo_proceso: .2} segundos\n")
    
    
    
    print("Proceso 3")
    inicio = time.perf_counter()
    with Pool(processes=3) as pool:
        #Creamos una lista con los datos de entrada
        numero = [1,2,3,4,5]
        #Ejecutamos la función sumar y le pasamos la lista con los datos
        results = pool.map(sumar, numero)
    tiempo3 = time.perf_counter()
    tiempo_proceso = tiempo3 - inicio
    print(f"El proceso 3 ha tardado {tiempo_proceso: .2} segundos")
        