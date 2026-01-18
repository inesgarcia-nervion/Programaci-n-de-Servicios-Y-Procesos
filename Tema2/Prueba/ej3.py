"""Crea una función que reciba una cadena de texto y cuente cuántas letras tiene.
Desde el programa principal, lanza varios procesos que analicen diferentes cadenas.
El programa principal debe esperar a que todos terminen y luego mostrar un mensaje final."""

from multiprocessing import Process
import time

def caracteres(cadenaTexto:str):
    resultado = len(cadenaTexto)
    #resultado = int(input("Introduce un número: "))    Si pidiera un número por teclado
    print(f"Esta frase {cadenaTexto} da de resultado {resultado}")

if __name__ == '__main__':

    inicio = time.perf_counter()
    
    # Primero se crean los procesos
    p1 = Process(target=caracteres, args=("Hola que tal",))
    p2 = Process(target=caracteres, args=("¿Cómo estás?",))
    p3 = Process(target=caracteres, args=("Adiós",))
    
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




"""
Para hacerlo de otra forma (más dinámica sin repetir código):

def caracteres(cadenaTexto: str):
    resultado = len(cadenaTexto)
    print(f"La frase '{cadenaTexto}' tiene {resultado} caracteres.")

if __name__ == '__main__':

    inicio = time.perf_counter()

    frases = ["Hola que tal", "¿Cómo estás?", "Adiós"]
    procesos = []

    # Crear y arrancar procesos
    for frase in frases:
        p = Process(target=caracteres, args=(frase,))
        procesos.append(p)
        p.start()

    # Esperar a que todos terminen
    for p in procesos:
        p.join()

    fin = time.perf_counter()
    tiempo_total = fin - inicio

    print("Todos los procesos han terminado.")
    print(f"Tiempo total: {tiempo_total:.2f} segundos")

"""