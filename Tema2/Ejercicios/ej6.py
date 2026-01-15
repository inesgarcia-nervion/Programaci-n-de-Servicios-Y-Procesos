"""6. Modifica el ejercicio anterior para usar un Pool para lanzar varios procesos 
de forma concurrente. Recuerda que al tener dos argumentos debes usar el método 
starmap en vez de map."""

from multiprocessing import Pool
import time

def sumar(numero1:int, numero2:int):
    inicio = min(numero1, numero2)
    fin = max(numero1, numero2)
    resultado = sum(range(inicio, fin + 1))  # Si pusiera "1 a 10", se haría de 1 a 9
    print(f"Suma desde { inicio } hasta {fin} da de resultado {resultado}")

if __name__ == '__main__':

    inicio = time.perf_counter()
    
    valores = [(1,10), (1,50), (10,1)]
    
    with Pool(processes=4) as pool:
        pool.starmap(sumar, valores)
        
    tiempo = time.perf_counter()
    tiempo_proceso = tiempo - inicio
    print(f"El proceso ha tardado {tiempo_proceso: .2} segundos\n")
    