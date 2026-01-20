"""1. Crea un proceso que cuente las vocales de un fichero de texto. 
Para ello crea una función que reciba una vocal y devuelva cuántas veces 
aparece en un fichero. Lanza el proceso de forma paralela para las 5 vocales. 
Tras lanzarse se imprimirá el resultado por pantalla."""

from multiprocessing import Pool
import time

# Se crea el archivo
with open('vocales.txt', 'w') as f:
        f.write("Texto de ejemplo\n")
        f.write("Hola hola hola\n")

# Se lee ese archivo y busca las vocales
def contarVocales(vocal):
    with open("vocales.txt", 'r') as f:
        return vocal, f.read().lower().count(vocal)
    

if __name__ == "__main__":
    
    inicio = time.perf_counter()
    
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    with Pool(processes=5) as pool:
        resultados = pool.map(contarVocales, vocales)
        
    for vocal, veces in resultados:
        print(f"La vocal {vocal} aparece {veces} veces")
    
    
    tiempo = time.perf_counter()
    tiempo_proceso = tiempo - inicio
    print(f"El proceso ha tardado {tiempo_proceso: .2} segundos")