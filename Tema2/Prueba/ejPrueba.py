"""Un proceso genera 3 números aleatorios (decimales) entre 0 y 10 y los
guarda en un fichero cuyo nombre recibe por parámetro."""

from multiprocessing import Process
import time, random

def numAleat(ruta):    # Parámetro "ruta" para que el proceso pueda guardar el fichero en la ubicación deseada.
    numRandom = [round(random.uniform(0,10),2) for i in range(3)]
    with open(ruta, "w") as f:      # Abre el fichero en modo escritura
        for n in numRandom:         # Porque ponemos n? Para recorrer la lista de números aleatorios
            f.write(f"{n}\n")   
    print(f"Numeros aleatorios: {numRandom}")


if __name__ == "__main__":
    inicio = time.perf_counter()

    p = Process(target=numAleat, args=("numeros.txt",)) # "numeros.txt" es la ruta donde se guardará el fichero
    p.start()
    p.join()

    final = time.perf_counter()
    tiempoFinal = final - inicio
    print(f"El proceso ha tardado {tiempoFinal: .2} segundos")