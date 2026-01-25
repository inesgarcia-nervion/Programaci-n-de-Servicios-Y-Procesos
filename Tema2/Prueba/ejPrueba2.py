"""Usar Pool para calcular el cuadrado de una lista de números en paralelo."""
from multiprocessing import Pool
import time

def cuadrado(x):
    return x * x

if __name__ == "__main__":
    inicio = time.process_time()
    
    with Pool(processes=3) as pool:                     # Crea un pool de 3 procesos porque tenemos 3 números
        numeros = [3,4,5]                               # Lista de números a procesar
        resultado = pool.map(cuadrado, numeros)         # Aplica la función cuadrado a cada número en paralelo
    
    final = time.process_time()
    tiempoFinal = final - inicio
    print(resultado)
    print(f"El proceso ha terminado en {tiempoFinal: .2} segundos")
